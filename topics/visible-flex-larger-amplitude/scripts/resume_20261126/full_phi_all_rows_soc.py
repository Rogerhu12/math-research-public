#!/usr/bin/env python3
"""Parent-row SOC by projection onto ALL literal old halfspaces.

Public repository Actions only.  Parent field/source/location binding and
true nonlinear row reads are inherited verbatim from the published v1 helper.
The new numerical step is min ||e||^2/2 subject to C e <= k, with
k_j = min(b_j-C_j d, -c_j(d)-tau||d||^3) for EVERY fixed-parent row.
Thus every old linear margin and every local nonlinear correction target
participates in the same projection.  No row is removed.

A nonnegative dual coordinate solve uses a streamed Gram matrix only as a
small dual operator, never its inverse.  The final correction is reconstructed
from the ORIGINAL row matrix and ALL constraints are read back directly.
A finite feasible iterate is only a proposal; actual Phi, full geometry,
corrected prediction and damping belong to the unchanged outer driver.
"""
from dataclasses import dataclass
import hashlib
import json
import math
import mmap
import os
from pathlib import Path


SCHEMA = 'full-Phi-all-old-rows-constrained-SOC-proposal-v2'
ROW_SCHEMA = 'complete-actual-margin-neighborhood-diverse-inequalities-v2'
INEQUALITY_SHA = 'e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8'
TAIL_FACTORY_SHA = '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'
SIX_FIELDS = ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')


def require_actions():
    if not (os.environ.get('GITHUB_ACTIONS', '').lower() == 'true'
            and os.environ.get('GITHUB_REPOSITORY') == 'Rogerhu12/math-research-public'):
        raise RuntimeError('SOC scientific arrays and field reads belong in public repository Actions')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    allow_nan=False).encode()).hexdigest()


def array_sha(value):
    # Called only after require_actions; input vectors are small relative to
    # the original residual/cache.  Include dtype/shape to identify the array.
    import numpy as np
    a = np.ascontiguousarray(value)
    h = hashlib.sha256(str(a.dtype).encode()+repr(a.shape).encode())
    h.update(memoryview(a).cast('B'))
    return h.hexdigest()


def finite_number(value, name, *, lower=None, strict=False):
    if isinstance(value, bool):
        raise ValueError(name+' is not a numerical parameter')
    x = float(value)
    if not math.isfinite(x) or (lower is not None and (x <= lower if strict else x < lower)):
        raise ValueError(name+' is outside its declared finite range')
    return x


def integer(value, name):
    if isinstance(value, bool) or int(value) != value:
        raise ValueError(name+' must be an exact integer')
    return int(value)


def _discard(a):
    if (hasattr(a, '_mmap') and hasattr(a._mmap, 'madvise')
            and hasattr(mmap, 'MADV_DONTNEED')):
        a._mmap.madvise(mmap.MADV_DONTNEED)


def _dot(a, v, block_columns):
    import numpy as np
    result = np.zeros(a.shape[0])
    for first in range(0, a.shape[1], block_columns):
        last = min(a.shape[1], first+block_columns)
        block = np.ascontiguousarray(a[:, first:last])
        result += block @ v[first:last]
        del block
        _discard(a)
    return result


def _transpose(a, v, block_columns):
    import numpy as np
    result = np.empty(a.shape[1])
    for first in range(0, a.shape[1], block_columns):
        last = min(a.shape[1], first+block_columns)
        block = np.ascontiguousarray(a[:, first:last])
        result[first:last] = block.T @ v
        del block
        _discard(a)
    return result



def minimum_norm_halfspaces(C, bounds, *, block_columns=32768,
                            feasibility_tolerance=2e-11, dual_tolerance=1e-12,
                            max_sweeps=20000, refresh_sweeps=64):
    """Numerical dual projection; no full row-rank assumption or row deletion.

    For min ||e||^2/2 with Ce<=k, the dual minimizes
    0.5*lambda^T(C C^T)lambda + k^T lambda, lambda>=0.
    Each scalar update minimizes that dual exactly in one coordinate.
    Small dual residuals are recomputed; acceptance uses direct original C.
    A budget-limited but directly feasible iterate may still be proposed,
    with minimum_norm_convergence_claimed=False.  Nothing is called exact.
    """
    require_actions()
    import numpy as np
    import time
    began = time.monotonic()
    m, n = C.shape
    k = np.asarray(bounds, dtype=float)
    if k.shape != (m,) or not np.isfinite(k).all():
        raise ValueError('Complete finite correction bounds are required')
    if m == 0:
        return np.zeros(n), dict(status='empty_halfspace_family', complete=True,
            numerical_feasible=True, minimum_norm_convergence_claimed=True,
            scientific_exact_certificate=False)
    gram = np.zeros((m,m))
    for first in range(0,n,block_columns):
        block = np.ascontiguousarray(C[:, first:first+block_columns])
        if not np.isfinite(block).all():
            raise ValueError('Nonfinite literal parent row matrix')
        gram += block @ block.T
        del block
        _discard(C)
    gram = (gram+gram.T)*.5
    diagonal = np.diag(gram).copy()
    preparation_seconds = time.monotonic()-began
    if not np.isfinite(gram).all() or np.any(diagonal<=0):
        return None, dict(status='nonpositive_or_nonfinite_Gram_diagonal', complete=True,
            numerical_feasible=False, minimum_norm_convergence_claimed=False,
            rows_removed=False, scientific_exact_certificate=False,
            preparation_seconds=preparation_seconds)
    lam = np.zeros(m)
    grad = k.copy()
    trace=[]
    dual_converged=False
    maximum_delta=0.
    sweep=0
    for sweep in range(1,max_sweeps+1):
        maximum_delta=0.
        for i in range(m):
            old=float(lam[i])
            new=max(0., old-float(grad[i])/float(diagonal[i]))
            delta=new-old
            if delta:
                lam[i]=new
                grad += delta*gram[:,i]
                maximum_delta=max(maximum_delta,abs(delta))
        if (sweep%refresh_sweeps==0 or sweep==1
                or maximum_delta<=dual_tolerance or sweep==max_sweeps):
            grad=gram@lam+k
            projected=np.where(lam>0, grad, np.minimum(grad,0.))
            pg=float(np.max(np.abs(projected),initial=0.))
            if len(trace)<512 or sweep==max_sweeps:
                trace.append(dict(sweep=sweep, projected_dual_gradient_inf=pg,
                    negative_dual_gradient_inf=float(np.max(-grad,initial=0.)),
                    dual_variable_norm=float(np.linalg.norm(lam)),
                    active_dual_coordinates=int(np.count_nonzero(lam))))
            if not np.isfinite(lam).all() or not np.isfinite(grad).all():
                return None, dict(status='nonfinite_dual_iterate', complete=True,
                    numerical_feasible=False, minimum_norm_convergence_claimed=False,
                    rows_removed=False, scientific_exact_certificate=False,
                    sweeps=sweep, trace=trace)
            if pg<=dual_tolerance:
                dual_converged=True
                break
    # The Gram is only the dual search operator.  Reconstruct with actual C,
    # then independently read all original rows, including dependent rows.
    e=-_transpose(C,lam,block_columns)
    ce=_dot(C,e,block_columns)
    if not np.isfinite(e).all() or not np.isfinite(ce).all():
        return None, dict(status='nonfinite_original_row_reconstruction', complete=True,
            numerical_feasible=False, minimum_norm_convergence_claimed=False,
            rows_removed=False, scientific_exact_certificate=False,
            sweeps=sweep, trace=trace)
    slack=k-ce
    violation=float(np.max(-slack,initial=0.))
    direct_gradient=slack
    direct_projected=np.where(lam>0,direct_gradient,np.minimum(direct_gradient,0.))
    direct_pg=float(np.max(np.abs(direct_projected),initial=0.))
    energy=float(e@e)
    objective=.5*energy
    dual_objective=-.5*energy-float(k@lam)
    gap=objective-dual_objective
    numerical_feasible=violation<=feasibility_tolerance
    minimum_norm_convergence=bool(dual_converged and direct_pg<=max(dual_tolerance,feasibility_tolerance))
    report=dict(schema='original-all-row-halfspace-dual-projection-v1',complete=True,
        status=('converged_numeric' if minimum_norm_convergence and numerical_feasible
                else 'sweep_limit_feasible' if numerical_feasible
                else 'no_feasible_correction_within_sweeps'),
        method='Cyclic exact scalar minimization of the nonnegative Gram dual; direct original-row reconstruction',
        rows=m,ambient_coordinates=n,rows_removed=False,full_row_rank_required=False,
        Gram_inverse_formed=False,Gram_only_for_dual_search=True,
        correction_formula='e=-C^T lambda using the original complete row matrix',
        max_sweeps=max_sweeps,sweeps=sweep,refresh_sweeps=refresh_sweeps,
        dual_tolerance=dual_tolerance,feasibility_tolerance=feasibility_tolerance,
        numerical_feasible=bool(numerical_feasible),
        minimum_norm_convergence_claimed=minimum_norm_convergence,
        scientific_exact_certificate=False,
        dual_variables=lam.tolist(),correction_row_values=ce.tolist(),
        correction_halfspace_slack=slack.tolist(),
        actual_maximum_violation=violation,
        direct_projected_dual_gradient_inf=direct_pg,
        original_row_vs_Gram_gradient_max_abs=float(np.max(np.abs(direct_gradient-grad),initial=0.)),
        primal_objective=objective,dual_objective=dual_objective,
        floating_primal_dual_gap=gap,
        complementarity_max_abs=float(np.max(np.abs(lam*slack),initial=0.)),
        preparation_seconds=preparation_seconds,seconds=time.monotonic()-began,trace=trace,
        infeasibility_proved=False,
        note='No feasible finite iterate is not a Farkas certificate. Numeric gap is diagnostic only.')
    return (e if numerical_feasible else None),report

@dataclass
class Proposal:
    # Arrays remain runner raw.  report alone is JSON serializable.
    candidate: object
    augmented_step: object
    correction: object
    report: dict


class ParentRowsSOC:
    """Bind literal parent rows once, then optionally propose ONE correction.

    source_sha256_by_role is the current driver's actual source dictionary.
    model_definition is None for original, context.definition() for R671.
    It must describe the operator currently being evaluated, after any seed
    migration.  All module arguments are the same bound objects that built C;
    in R671 this includes point_adapter and the patched fields_block.
    """

    def __init__(self, problem, parent_x, row_matrix, bounds, metadata, *,
                 geometry_module, point_module, observed_module, inequality_module,
                 source_sha256_by_role, observation_carrier_sha256,
                 model_definition=None, parent_bundle_sha256=None,
                 block_columns=32768):
        require_actions()
        import numpy as np
        self.q = problem
        self.x = np.array(parent_x, dtype=np.float64, copy=True)
        if self.x.shape != (problem.free_size,) or not np.isfinite(self.x).all():
            raise ValueError('SOC parent is not the complete finite free-coordinate vector')
        self.C = row_matrix
        if (len(self.C.shape) != 2 or self.C.dtype != np.dtype('float64')
                or self.C.shape[1] < 1):
            raise ValueError('SOC needs the literal float64 augmented-coordinate row matrix')
        self.b = np.array(bounds, dtype=float, copy=True)
        self.meta = json.loads(json.dumps(metadata, allow_nan=False))
        self.sources = dict(source_sha256_by_role)
        self.geometry = geometry_module
        self.point = point_module
        self.observed = observed_module
        self.block_columns = integer(block_columns, 'block_columns')
        if self.block_columns < 1:
            raise ValueError('block_columns must be positive')
        if self.meta.get('schema') != ROW_SCHEMA:
            raise ValueError('Unknown parent inequality semantics')
        for role, module in (('geometry', geometry_module), ('point', point_module),
                             ('implementation', observed_module), ('inequalities', inequality_module)):
            actual = sha(module.__file__)
            if self.sources.get(role) != actual:
                raise ValueError('SOC source identity differs from parent role '+role)
        if self.sources['inequalities'] != INEQUALITY_SHA:
            raise ValueError('This SOC implementation consumes the frozen v2 row definition only')
        self.model = json.loads(json.dumps(model_definition, allow_nan=False))
        context = getattr(problem, 'reference_tail_context', None)
        if context is not None:
            if self.model != context.definition():
                raise ValueError('R671 SOC model differs from the actual operator context')
        if self.model is None:
            if context is not None:
                raise ValueError('Original SOC identity cannot hide an R671 operator')
        else:
            if (self.model.get('source_sha256') != TAIL_FACTORY_SHA
                    or self.sources.get('exact_tail') != TAIL_FACTORY_SHA
                    or getattr(point_module, 'reference_tail_adapter_source_sha256', None) != TAIL_FACTORY_SHA):
                raise ValueError('R671 SOC needs the actual canonical factory and point adapter')
            if self.model.get('M') != problem.M:
                raise ValueError('R671 model M does not match the current complete operator')
            if self.model.get('original_observation_carrier_sha256') != observation_carrier_sha256:
                raise ValueError('R671 SOC observation identity differs from its canonical model')
            if float(self.model['lambda_value']) != 0. and context is None:
                raise ValueError('Nonzero R671 SOC cannot use the original field operator')
        actual_fields_source = sha(geometry_module.fields_block.__code__.co_filename)
        expected_fields_source = (TAIL_FACTORY_SHA if self.model is not None
                                  else self.sources.get('observed_geometry'))
        if actual_fields_source != expected_fields_source:
            raise ValueError('SOC six-jet function is not the current model-bound field adapter')
        actual_point_fields_source = sha(point_module.fields_at.__code__.co_filename)
        expected_point_fields_source = (TAIL_FACTORY_SHA if self.model is not None
                                        else self.sources['point'])
        if actual_point_fields_source != expected_point_fields_source:
            raise ValueError('SOC arbitrary fields are not the current model-bound point adapter')
        m = self.C.shape[0]
        if (self.b.shape != (m,) or not np.isfinite(self.b).all()
                or self.meta.get('selected_rows') != m or len(self.meta.get('rows', ())) != m):
            raise ValueError('SOC rows, bounds and parent metadata are not the same complete set')
        if m and (not isinstance(self.C, np.memmap)
                  or Path(self.C.filename).resolve() != Path(self.meta['row_cache']).resolve()):
            raise ValueError('SOC matrix is not the literal parent v2 row-cache file')
        self.reach_ratio = finite_number(self.meta['reach_ratio'], 'reach_ratio', lower=0, strict=True)
        self.safety = finite_number(self.meta['safety'], 'safety', lower=0, strict=True)
        if not self.safety < 1:
            raise ValueError('SOC retains the original numerical safety less than one')
        self.rows = self.meta['rows']
        for i, row in enumerate(self.rows):
            if row.get('index') != i or float(row['normalized_bound']) != self.b[i]:
                raise ValueError('SOC parent row order or literal bound changed')
            norm = finite_number(row['gradient_coordinate_norm'], 'parent row norm', lower=0, strict=True)
            product = finite_number(row['current_product'], 'parent product', lower=0)
            if (float(row['actual_product_margin']) != self.safety-product
                    or (self.safety-product)/norm != self.b[i]):
                raise ValueError('SOC bound is not the literal parent product margin divided by parent norm')
            self._curvature_location(row['curvature_point'])
            self._radius_location(row['radius_point'])
        self.identity = dict(
            parent_coordinate_sha256=array_sha(self.x), parent_bundle_sha256=parent_bundle_sha256,
            observation_carrier_sha256=observation_carrier_sha256,
            source_sha256_by_role=self.sources, model_definition=self.model,
            bound_fields_block_source_sha256=actual_fields_source,
            bound_point_fields_source_sha256=actual_point_fields_source,
            model_definition_sha256=None if self.model is None else canonical_sha(self.model),
            J=int(problem.J), M=int(problem.M), P=int(problem.P),
            N=int(problem.N), full_N=int(getattr(problem, 'full_N', problem.N)),
            coordinate_size=int(self.C.shape[1]), row_count=m,
            parent_rows_metadata_sha256=canonical_sha(self.meta),
            parent_height=float(self.x[-1]))
        self.attempted = False

    def _curvature_location(self, value):
        q = self.q
        if not isinstance(value, (list, tuple)) or not value:
            raise ValueError('Missing literal curvature-row address')
        if value[0] == 'grid' and len(value) == 4:
            stage = integer(value[1], 'stage'); angle = integer(value[2], 'angle')
            branch = integer(value[3], 'branch')
            if not (0 <= stage < q.P and 0 <= angle < q.N and branch in (0, 1)):
                raise ValueError('Curvature grid row is outside this observation/angle carrier')
            return ('grid', stage, angle, branch)
        if value[0] == 'arbitrary' and len(value) == 5:
            cell = integer(value[1], 'cell'); u = finite_number(value[2], 'u')
            phi = finite_number(value[3], 'phi'); branch = integer(value[4], 'branch')
            if not (0 <= cell < q.J-1 and 0 <= u <= 1 and branch in (0, 1)):
                raise ValueError('Arbitrary curvature row is outside this material carrier')
            return ('arbitrary', cell, u, phi, branch)
        raise ValueError('Unknown curvature-row address, not a generic numerical tuple')

    def _radius_location(self, value):
        if not isinstance(value, (list, tuple)) or not value:
            raise ValueError('Missing literal radius partner')
        if tuple(value) in (('fixed_core',), ('cap_height',)):
            return tuple(value)
        if value[0] == 'grid_radius' and len(value) == 3:
            loc = self._curvature_location(('grid', value[1], value[2], 0))
            return ('grid_radius', *loc[1:3])
        if value[0] == 'arbitrary_radius' and len(value) == 4:
            loc = self._curvature_location(('arbitrary', *value[1:], 0))
            return ('arbitrary_radius', *loc[1:4])
        raise ValueError('Unknown radius partner; never replace it by trial maximum diameter')

    def read_fixed_values(self, point):
        """Read c_i(z) with each parent's n_i and exact fixed pair, no pullback."""
        require_actions()
        import numpy as np
        point = np.asarray(point, dtype=float)
        if point.shape != self.x.shape or not np.isfinite(point).all():
            raise ValueError('Fixed-row trial is not the full finite field coordinate vector')
        try:
            p = self.q.prepare(point)
        except (FloatingPointError, OverflowError, np.linalg.LinAlgError) as error:
            return dict(complete=False, failed_row=None, reason='numeric_prepare_failure',
                        arithmetic_error=repr(error), rows=[])
        field_cache, curvature_cache, diameter_cache = {}, {}, {}
        records = []
        residuals = np.empty(len(self.rows))

        def fields(loc):
            # Keep grid synthesis in its grid convention; do not replace it
            # by an arbitrary trig evaluation with merely close floating bits.
            key = tuple(loc)
            if key not in field_cache:
                if key[0] == 'grid':
                    result = self.geometry.single_fields(self.q, p, key[1], key[2])
                elif key[0] == 'arbitrary':
                    result = self.point.fields_at(self.q, p, *key[1:], self.observed)
                else:
                    raise ValueError('Internal field location must have an explicit kind')
                if (set(result) != set(SIX_FIELDS)
                        or any(np.shape(result[k]) != (3,) for k in SIX_FIELDS)):
                    raise ValueError('Bound geometry provider is not the declared complete six-jet interface')
                field_cache[key] = result
            return field_cache[key]

        try:
            for i, row in enumerate(self.rows):
                loc = self._curvature_location(row['curvature_point'])
                rloc = self._radius_location(row['radius_point'])
                if loc not in curvature_cache:
                    f = fields(loc[:-1])
                    if not all(np.isfinite(f[k]).all() for k in SIX_FIELDS):
                        return dict(complete=False, failed_row=i, reason='nonfinite_six_jets', rows=records)
                    area = float(np.linalg.norm(np.cross(f['Fs'], f['Fphi'])))
                    if not math.isfinite(area) or area <= 0:
                        return dict(complete=False, failed_row=i, reason='nonpositive_area', rows=records)
                    value, _, principal = self.geometry.curvature_cotangent(f, loc[-1])
                    if not math.isfinite(value) or not math.isfinite(principal['principal_gap']):
                        return dict(complete=False, failed_row=i, reason='nonfinite_principal_value', rows=records)
                    curvature_cache[loc] = (float(value), float(principal['principal_gap']), area)
                value, gap, area = curvature_cache[loc]
                if rloc not in diameter_cache:
                    if rloc[0] == 'fixed_core':
                        diameter = 2.
                    elif rloc[0] == 'cap_height':
                        diameter = 2*abs(float(p.height))
                    else:
                        kind = 'grid' if rloc[0] == 'grid_radius' else 'arbitrary'
                        f = fields((kind, *rloc[1:]))
                        diameter = 2*float(np.linalg.norm(f['F']))
                    if not math.isfinite(diameter) or diameter <= 0:
                        return dict(complete=False, failed_row=i, reason='nonpositive_partner_diameter', rows=records)
                    diameter_cache[rloc] = diameter
                diameter = diameter_cache[rloc]
                norm = float(row['gradient_coordinate_norm'])
                product = self.reach_ratio*diameter*abs(value)
                residuals[i] = (product-self.safety)/norm
                if not math.isfinite(product) or not math.isfinite(residuals[i]):
                    return dict(complete=False, failed_row=i, reason='nonfinite_normalized_product', rows=records)
                records.append(dict(index=i, curvature_point=list(loc), radius_point=list(rloc),
                    parent_gradient_coordinate_norm=norm, signed_curvature=value,
                    principal_gap=gap, area=area, diameter=diameter, product=product,
                    normalized_constraint_value=float(residuals[i]),
                    curvature_sign_changed=bool(float(row['signed_curvature'])*value <= 0),
                    cap_height_sign_changed=bool(rloc[0] == 'cap_height'
                        and self.identity['parent_height']*float(p.height) <= 0),
                    endpoint_simple_nonzero=bool(gap > 0 and value != 0
                        and row['principal_metadata']['principal_gap'] > 0 and row['signed_curvature'] != 0)))
        except (FloatingPointError, OverflowError, np.linalg.LinAlgError) as error:
            return dict(complete=False, failed_row=len(records), reason='numeric_point_read_failure',
                        arithmetic_error=repr(error), rows=records)
        # Identity/shape/API ValueError exceptions intentionally propagate.
        return dict(complete=True, coordinate_sha256=array_sha(point), rows=records,
            normalized_constraints=residuals.tolist(),
            maximum_product=max((r['product'] for r in records), default=0.),
            positive_normalized_rows=np.flatnonzero(residuals > 0).tolist(),
            fixed_parent_norms=True, trial_radius_partner_reselected=False,
            branch_scope='Same ordered principal branch at the same physical row; endpoint gaps are readings, not a pathwise Lipschitz certificate')

    def propose(self, coordinate_step, lift, full_trial_point, full_trial, *, tau,
                workdir, rank_tolerance=2e-12, feasibility_tolerance=2e-11):
        """Return Proposal; caller owns true corrected acceptance and fallback.

        Default eligibility is exactly alpha=1, finite/domain/descent true,
        and an actually evaluated, complete geometry screen false.  One such
        invocation is consumed, even if no parent row is positive or the complete halfspace solve returns no feasible correction.
        A second invocation on this object is an identity/control-flow error.
        """
        require_actions()
        import numpy as np
        report = dict(schema=SCHEMA, source_sha256=sha(__file__), identity=self.identity,
            attempted=False, proposal_available=False, complete=False,
            full_true_Phi_acceptance_performed=False, full_true_geometry_acceptance_performed=False,
            fallback='Unmodified parent + alpha*T*d ray; keep every newly remembered point',
            complete_step_space_retained=True, norm='Original augmented Euclidean norm from the main parent QP',
            continuous_geometry_certified=False, theorem_L_gamma_tau_threshold_established=False)
        eligible = (float(full_trial['alpha']) == 1. and bool(full_trial['finite'])
            and bool(full_trial['feasible']) and bool(full_trial['descent'])
            and not bool(full_trial['curvature_feasible'])
            and full_trial.get('curvature_points') is not None
            and full_trial.get('curvature_filter') is not None)
        if not eligible:
            report.update(complete=True, reason='Not an original full-step true-geometry-only rejection')
            return Proposal(None, None, None, report)
        if self.attempted:
            raise ValueError('This parent direction already consumed its one SOC attempt')
        self.attempted = True
        report['attempted'] = True
        if full_trial['curvature_points'].get('complete') is not True:
            report.update(complete=True, reason='Full trial has an incomplete/singular geometry read')
            return Proposal(None, None, None, report)
        tau = finite_number(tau, 'SOC cubic tau', lower=0)
        rank_tolerance = finite_number(rank_tolerance, 'rank_tolerance', lower=0, strict=True)
        feasibility_tolerance = finite_number(feasibility_tolerance, 'feasibility_tolerance', lower=0)
        d = np.asarray(coordinate_step, dtype=float)
        if d.shape != (self.C.shape[1],) or not np.isfinite(d).all():
            raise ValueError('SOC direction is not the original complete augmented coordinate vector')
        trial_point = np.asarray(full_trial_point, dtype=float)
        expected_point = self.x+lift(d)
        if trial_point.shape != self.x.shape or not np.array_equal(trial_point, expected_point):
            raise ValueError('SOC full trial does not equal its bound parent plus the same T*d')
        del expected_point
        cd = _dot(self.C, d, self.block_columns)
        old_slack = self.b-cd
        a = float(np.linalg.norm(d))
        report.update(tau=tau, tau_role='Explicit numerical cubic inward policy, not a proven R680 threshold',
            rank_tolerance=rank_tolerance, feasibility_tolerance=feasibility_tolerance,
            coordinate_norm=a, coordinate_step_sha256=array_sha(d),
            original_normalized_row_values=cd.tolist(), original_slack=old_slack.tolist(),
            original_maximum_linear_violation=float(np.max(-old_slack, initial=0.)),
            normalized_bounds=self.b.tolist(), full_trial_coordinate_sha256=array_sha(trial_point))
        if report['original_maximum_linear_violation'] > feasibility_tolerance:
            report.update(complete=True, reason='Main direction fails the complete literal old-row feasibility tolerance')
            return Proposal(None, None, None, report)
        values = self.read_fixed_values(trial_point)
        report['full_trial_fixed_parent_rows'] = values
        if not values['complete']:
            report.update(complete=True, reason='Cannot read all fixed parent nonlinear rows')
            return Proposal(None, None, None, report)
        r = np.asarray(values['normalized_constraints'])
        remainder = r-(cd-self.b)
        report['actual_nonlinear_minus_parent_linear'] = remainder.tolist()
        indices = np.flatnonzero(r > 0)
        report['correction_parent_row_indices'] = indices.tolist()
        if not len(indices):
            report.update(complete=True, reason='No positive fixed-parent residual; no SOC row set and no attribution of the full rejection',
                absence_scope='Could be an unselected pair, an additional absolute cap, or different numerical point evaluation; not a proved new-peak cause')
            return Proposal(None, None, None, report)
        if a == 0:
            report.update(complete=True, reason='Zero original direction; no fabricated SOC improvement')
            return Proposal(None, None, None, report)
        if not math.isfinite(a):
            report.update(complete=True, reason='Original augmented norm overflow', coordinate_norm=None)
            return Proposal(None, None, None, report)
        try:
            cubic = tau*a**3
        except OverflowError:
            cubic = float('inf')
        h = r[indices]+cubic
        report.update(cubic_inward_scalar=cubic, right_hand_side=h.tolist(),
            right_hand_side_policy='h_i=c_i(d)+tau*||d||^3, I={i:c_i(d)>0}',
            noncorrected_old_rows='All retained in the literal postcorrection C_j slack check')
        if not np.isfinite(h).all():
            report.update(complete=True, reason='Nonfinite declared SOC right hand side',
                          cubic_inward_scalar=None, right_hand_side=None)
            return Proposal(None, None, None, report)
        directory = Path(workdir)
        directory.mkdir(parents=True, exist_ok=False)
        # All literal old halfspaces participate in the optimization itself.
        # Every fixed-parent nonlinear value imposes its corrected RHS too.
        correction_bounds = np.minimum(old_slack, -r-cubic)
        report['correction_halfspace_bounds'] = correction_bounds.tolist()
        report['correction_halfspace_policy'] = (
            'k_j=min(b_j-C_j*d,-c_j(d)-tau*||d||^3) for EVERY original row j')
        report['noncorrected_old_rows'] = 'All retained as literal inequalities INSIDE the projection and in direct readback'
        e, projection = minimum_norm_halfspaces(
            self.C, correction_bounds, block_columns=self.block_columns,
            feasibility_tolerance=feasibility_tolerance,
            dual_tolerance=max(1e-14, min(1e-12, feasibility_tolerance/16)),
            max_sweeps=20000, refresh_sweeps=64)
        report['constrained_projection'] = projection
        if e is None:
            report.update(complete=True, reason='No numerically feasible complete-row SOC correction returned; original ray retained')
            return Proposal(None, None, None, report)
        ce = _dot(self.C, e, self.block_columns)
        z = d+e
        # Re-read C(d+e) directly, not only its accumulated C*d+C*e.
        cz = _dot(self.C, z, self.block_columns)
        slack = self.b-cz
        physical = np.array([row['current_product'] for row in self.rows])
        norms = np.array([row['gradient_coordinate_norm'] for row in self.rows])
        report.update(correction_norm=float(np.linalg.norm(e)),
            correction_over_original_norm=float(np.linalg.norm(e))/a,
            corrected_coordinate_norm=float(np.linalg.norm(z)), correction_sha256=array_sha(e),
            corrected_augmented_step_sha256=array_sha(z), correction_normalized_row_values=ce.tolist(),
            selected_SOC_inequality_slack=(-h-ce[indices]).tolist(),
            selected_SOC_inequality_maximum_violation=float(np.max(ce[indices]+h, initial=0.)),
            all_correction_halfspace_slack=(correction_bounds-ce).tolist(),
            all_fixed_parent_nonlinear_target_slack=(-r-cubic-ce).tolist(),
            all_fixed_parent_nonlinear_target_maximum_violation=float(np.max(r+cubic+ce,initial=0.)),
            corrected_normalized_row_values=cz.tolist(), corrected_slack=slack.tolist(),
            literal_Cd_plus_Ce_discrepancy_max_abs=float(np.max(np.abs(cz-cd-ce), initial=0.)),
            corrected_maximum_linear_violation=float(np.max(-slack, initial=0.)),
            old_physical_linear_products=(physical+norms*cd).tolist(),
            corrected_physical_linear_products=(physical+norms*cz).tolist(),
            actual_physical_margin_allowance_from_numerical_tolerance=(norms*feasibility_tolerance).tolist(),
            all_old_rows_rechecked=True)
        if (report['corrected_maximum_linear_violation'] > feasibility_tolerance
                or report['all_fixed_parent_nonlinear_target_maximum_violation'] > feasibility_tolerance):
            report.update(complete=True, reason='SOC breaks at least one literal old-row margin; original ray retained')
            return Proposal(None, None, None, report)
        candidate = self.x+lift(z)
        if not np.isfinite(candidate).all():
            report.update(complete=True, reason='Nonfinite corrected physical field')
            return Proposal(None, None, None, report)
        report['corrected_fixed_parent_rows'] = self.read_fixed_values(candidate)
        report.update(complete=True, proposal_available=True, reason='Candidate requires actual corrected Phi and full known-point geometry',
            corrected_candidate_coordinate_sha256=array_sha(candidate),
            base_point_unchanged=True, original_ray_unchanged=True,
            kernel_note='Parent rows use the same T; e=-C^T lambda lies in ran(C^T), orthogonal to ker(T) in exact arithmetic. Numeric feasible output is a proposal; exact minimum norm is claimed only by the separate mathematical theorem, not by floating-point diagnostics')
        return Proposal(candidate, z, e, report)
