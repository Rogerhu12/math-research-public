"""Targeted physical-turn nodes for the unchanged radial bump target.

This resolves known internal phase knots and observed short-turn curvature
peaks. It does not globally refine the mesh, change g, or change Fourier K.
An integration provider can use these x/h/coords with its declared rule.
"""
import numpy as np
from fd2d_gc_raw_bump_clean import coalesce_computational_mesh
from fd2d_gc_raw_bump_cylinder import CylinderRawBumpDAE


class TurnResolvedRawBumpDAE(CylinderRawBumpDAE):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        base_mesh = self.x.copy()
        base_coalescence = self.mesh_coalescence
        additions = []
        for index, piece in enumerate(self.profile.base.segments):
            kind, label = piece['kind'], piece.get('label', '')
            fractions = []
            if kind == 'turn':
                fractions = [.04, .08, .5, .92, .96]
                if label == 'redeepen_after_partial_return':
                    fractions.append(.8)
            elif kind == 'phase_bridge' and piece['L'] <= .04:
                fractions = [.25, .5, .75]
                if label == 'cut_second_jet_brake':
                    fractions += [.125, .875]
            if fractions:
                points = piece['s0']+piece['L']*np.array(sorted(fractions))
                additions.append(dict(physical_segment_index=index, kind=kind, label=label,
                    s0=float(piece['s0']), s1=float(piece['s1']),
                    fractions=sorted(fractions), actual_nodes=points.tolist()))
        seed_end = float(self.seed_weight_definition['end'])
        raw = np.unique(np.r_[base_mesh, seed_end,
            np.concatenate([np.asarray(q['actual_nodes']) for q in additions])])
        self.x, self.mesh_coalescence = coalesce_computational_mesh(raw,
            relative_tolerance=base_coalescence['relative_tolerance'])
        self.N = len(self.x)
        self.h = np.diff(self.x)
        self.size = self.N*self.q+self.parameter_count
        self.residual_size = self.N*self.q+2*self.K+2
        self.coords = {k:np.asarray(v,float) for k,v in self.chart.coordinates(self.x).items()}
        self._operator_cache = {}
        self.fixed_central_nodes = np.flatnonzero(self.x <= self.profile.central_end)
        self.central_field_definition = dict(self.central_field_definition,
            fixed_node_indices=self.fixed_central_nodes.tolist())
        self.representation_kind = 'targeted_turn_mesh_exact_central_cylinder_v1'
        self.targeted_mesh_definition = dict(schema='fd2d-targeted-physical-turn-mesh-v1',
            original_computational_mesh=base_mesh.tolist(),
            base_mesh_coalescence=base_coalescence,
            targeted_additions=additions, explicit_seed_decay_end=seed_end,
            actual_nodes=self.x.tolist(), original_node_count=len(base_mesh),
            actual_node_count=self.N, physical_profile_changed=False,
            angular_chart_changed=False, Fourier_order_changed=False,
            finite_radial_equations_changed=True,
            reason='Observed short-turn interior target-curvature peak and large retained radial residuals; no global angular increase')

    def parameter_layout(self):
        out = super().parameter_layout()
        out['targeted_mesh_definition'] = self.targeted_mesh_definition
        return out

    def warm_from_actual_P1(self, mesh, corrections, parameters):
        mesh, y, p = np.asarray(mesh,float), np.asarray(corrections,float), np.asarray(parameters,float)
        if y.shape != (len(mesh),self.q) or p.shape != (self.parameter_count,):
            raise ValueError('Wrong P1 array dimensions')
        if mesh[0] != self.x[0] or mesh[-1] != self.x[-1] or np.any(np.diff(mesh)<=0):
            raise ValueError('Wrong physical domain or old mesh ordering')
        yy = np.column_stack([np.interp(self.x,mesh,y[:,j]) for j in range(self.q)])
        before = np.r_[yy.ravel(),p.copy()]
        vector = self.impose_linear_boundary_values(before)
        back = np.column_stack([np.interp(mesh,self.x,yy[:,j]) for j in range(self.q)])
        return vector, dict(schema='fd2d-targeted-P1-same-profile-warm-v1',
            old_node_count=len(mesh), new_node_count=self.N,
            maximum_P1_old_node_roundtrip_error=float(np.max(abs(back-y))),
            exact_cylinder_projection_change=float(np.max(abs(vector-before))),
            parameters_unchanged=bool(np.array_equal(self.unpack(vector)[1],p)),
            target_metric_changed=False, finite_radial_equations_changed=True,
            nonlinear_solve_performed=False)
