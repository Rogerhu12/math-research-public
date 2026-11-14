"""Explicit mesh/seed-lifting representation of the physical-bump raw GC field.

The target a(s), its compact bumps, the angular chart and tail lifting are
unchanged from RawBumpDAE. Only computational knots are coalesced and the
accurate central seed is retained throughout the exact central cylinder.
These are changes of the finite field representation, not changes of g.
"""
from __future__ import annotations

import numpy as np
from fd2d_gc_raw_bump_dae import RawBumpDAE
from fd2d_gc_raw_lifted_dae import step5


def seed_weight(s, definition):
    """Declared quintic plateau/decay; return value and physical s derivative."""
    if definition.get('step') != 5:
        raise ValueError('Only the explicit quintic step is defined')
    left, right = float(definition['start']), float(definition['end'])
    if not 0 <= left < right:
        raise ValueError('The seed decay interval must have positive length')
    q, dq = step5((np.asarray(s, float)-left)/(right-left))
    return 1-q, -dq/(right-left)


def coalesce_computational_mesh(mesh, *, relative_tolerance=1e-12):
    """Keep the last representative of each scale-small adjacent cluster.

    The original physical segments are not an argument and are never edited.
    Endpoints remain the original endpoints. All moved/removed nodes and the
    actual maximum displacement are returned as part of the definition.
    """
    old = np.asarray(mesh, float)
    if old.ndim != 1 or len(old) < 2 or np.any(np.diff(old) <= 0):
        raise ValueError('Expected an ordered, strictly increasing old mesh')
    scale = max(1., abs(old[0]), abs(old[-1]), old[-1]-old[0])
    tolerance = float(relative_tolerance)*scale
    if not 0 < tolerance < 1e-6*scale:
        raise ValueError('Use a small, positive scale-aware mesh tolerance')
    groups = []
    start = 0
    for j in range(1, len(old)+1):
        if j == len(old) or old[j]-old[j-1] > tolerance:
            groups.append(np.arange(start, j))
            start = j
    selected = np.array([g[-1] for g in groups])
    selected[0] = 0
    selected[-1] = len(old)-1
    new = old[selected].copy()
    displacement = np.concatenate([abs(old[g]-old[k]) for g, k in zip(groups, selected)])
    clusters = [dict(old_indices=g.tolist(), old_values=old[g].tolist(),
                     representative=float(old[k]), retained_old_index=int(k))
                for g, k in zip(groups, selected) if len(g) > 1]
    return new, dict(schema='fd2d-scale-aware-computational-mesh-coalescence-v1',
        relative_tolerance=float(relative_tolerance), scale=float(scale),
        absolute_tolerance=float(tolerance), original_nodes=old.tolist(),
        actual_nodes=new.tolist(), original_count=len(old), actual_count=len(new),
        original_minimum_cell=float(np.min(np.diff(old))),
        actual_minimum_cell=float(np.min(np.diff(new))), clusters=clusters,
        maximum_displacement=float(np.max(displacement, initial=0.)),
        physical_segments_changed=False, physical_profile_functions_changed=False,
        angular_chart_function_changed=False)


class CleanRawBumpDAE(RawBumpDAE):
    """Same physical target and parameters, explicit improved finite field."""
    def __init__(self, *args, mesh_relative_tolerance=1e-12, **kwargs):
        super().__init__(*args, **kwargs)
        self.legacy_seed_weight_definition = dict(kind='origin_decay', start=0.,
            end=min(.55, .4*self.profile.end), step=5)
        self.seed_weight_definition = dict(kind='central_plateau',
            start=float(self.profile.central_end),
            end=max(min(.55, .4*self.profile.end),
                    self.profile.central_end+.05*(self.profile.end-self.profile.central_end)),
            step=5)
        # Preserve the physical/profile segment objects and all chart formulas.
        # Only node evaluations of the same functions are recomputed below.
        self.x, self.mesh_coalescence = coalesce_computational_mesh(self.x,
            relative_tolerance=mesh_relative_tolerance)
        self.N = len(self.x)
        self.h = np.diff(self.x)
        self.size = self.N*self.q+self.parameter_count
        self.residual_size = self.N*self.q+2*self.K+2
        self.coords = {k: np.asarray(v, float) for k, v in self.chart.coordinates(self.x).items()}
        self._operator_cache = {}
        self.representation_kind = 'coalesced_mesh_central_seed_plateau_v1'

    def parameter_layout(self):
        out = super().parameter_layout()
        out['field_representation_kind'] = self.representation_kind
        out['seed_weight_definition'] = self.seed_weight_definition.copy()
        return out

    def lifting(self, delta, tail_parameters):
        out = super().lifting(delta, tail_parameters)
        old, old_s = seed_weight(self.x, self.legacy_seed_weight_definition)
        new, new_s = seed_weight(self.x, self.seed_weight_definition)
        dw, dws = new-old, new_s-old_s
        vn = self.seed[:, None]*dw
        sxn = self.seed[:, None]*dws
        xin = self.seed_xi[:, None]*dw
        out['values'][:, :, 0] += vn
        out['x'][:, :, 0] += sxn
        out['xi'][:, :, 0] += xin
        ops = self.operators(delta)
        fn = -ops['jet']['c'][None, :]*vn+ops['adv']*xin-sxn
        out['forcing'][:, :self.e] += (self.PE@fn).T
        # No tail or profile value-jet column changes: the seed is fixed.
        # Profile derivatives of c*(l-n) use these actual updated fields in
        # the inherited full analytic raw Jacobian and complement consumer.
        out['seed_weight_definition'] = self.seed_weight_definition.copy()
        return out

    def warm_from_bump(self, mesh, corrections, parameters, *, old_seed_definition):
        """P1 radial re-evaluation plus explicit retained-mode lift conversion.

        Parameters are unchanged. The nonrepresentable seed complement is
        not suppressed: its actual field change is quantified and reported.
        The result is an initial field, not a solution or refinement claim.
        """
        mesh = np.asarray(mesh, float)
        y, p = np.asarray(corrections, float), np.asarray(parameters, float)
        if y.shape != (len(mesh), self.q) or p.shape != (self.parameter_count,):
            raise ValueError('Wrong physical-bump warm dimensions')
        if np.any(np.diff(mesh) <= 0) or mesh[0] != self.x[0] or mesh[-1] != self.x[-1]:
            raise ValueError('The actual P1 warm domain differs from this physical domain')
        interp = np.column_stack([np.interp(self.x, mesh, y[:, j]) for j in range(self.q)])
        old_weight, _ = seed_weight(self.x, old_seed_definition)
        new_weight, _ = seed_weight(self.x, self.seed_weight_definition)
        retained_seed = self.PE@self.seed
        yy = interp.copy()
        yy[:, :self.e] += (old_weight-new_weight)[:, None]*retained_seed[None, :]
        before_boundary = np.r_[yy.ravel(), p.copy()]
        vector = self.impose_linear_boundary_values(before_boundary)
        high = self.seed-self.E@retained_seed
        high_change = high[:, None]*(new_weight-old_weight)[None, :]
        old_at_old = np.column_stack([np.interp(mesh, self.x, interp[:, j]) for j in range(self.q)])
        report = dict(schema='fd2d-physical-bump-explicit-P1-and-seed-warm-v1',
            old_seed_weight_definition=dict(old_seed_definition),
            new_seed_weight_definition=self.seed_weight_definition.copy(),
            original_nodes=mesh.tolist(), new_nodes=self.x.tolist(),
            parameters_unchanged=bool(np.array_equal(self.unpack(vector)[1], p)),
            maximum_P1_roundtrip_correction_change=float(np.max(abs(old_at_old-y))),
            retained_seed_change_maximum=float(np.max(abs(yy-interp))),
            sampled_seed_omitted_maximum=float(np.max(abs(high))),
            actual_node_field_change_from_seed_reexpression_maximum=float(np.max(abs(high_change))),
            boundary_projection_change_maximum=float(np.max(abs(vector-before_boundary))),
            physical_target_changed=False, nonlinear_solve_performed=False,
            scope='Explicit P1 re-evaluation and retained Fourier lifting conversion; omitted seed change retained in the actual new field')
        return vector, report
