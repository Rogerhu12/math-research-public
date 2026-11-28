#!/usr/bin/env python3
"""R729 all-row common-slack dual recovery after a real dependent-blocker return.

Import and pure report reading use only the standard library. NumPy is imported
only by recover(), inside the original public Actions scientific entry. This
module never evaluates F, J, J*, a normal root, a geometry point, or a new row.
The original QPv3 report remains a separate, unchanged complete object.
"""
import hashlib
import json
import math
import os
from pathlib import Path
import time
import traceback

SCHEMA = 'R729-all-row-common-slack-dual-cyclic-recovery-v1'
REPORT_SCHEMA = 'R729-actual-common-slack-dual-recovery-v1'
BINDING_SCHEMA = 'R729-complete-original-QP-and-recovery-readout-v1'
ROLE = 'common_slack_dual_recovery'
DIRECTION_KEY = 'R729_common_slack_fallback'
DEFINITION_KEY = 'R729_common_slack_recovery_definition'
ORIGINAL_QP_SCHEMA = 'fullspace-feasible-active-set-cg-reliable-update-v3'
ORIGINAL_QP_SOURCE_SHA256 = 'fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4'
TRIGGERS = ('dependent_blocker_at_zero_step', 'dependent_blocker_after_feasible_step')
THEOREM = {
    'path': 'results/R729-common-slack-all-row-dual-coercivity-and-feasible-recovery.md',
    'bytes': 16220,
    'sha256': 'd6104084c6a96651e478ab4c0b7f25124ca5859ae03e49fdb4d3a35c9264c87a',
    'git_blob_sha': 'a66c19196b798957a6f905c23e47b2b500b60dd8',
    'publication': 'f687c963cbc899e211a3d083c12b2f1b7e322d4d',
}
ORIGINAL_SCOPE = ('The complete unchanged QPv3 attempt before optional recovery; '
    'its face projected gradient, multipliers, step norm and linear violation '
    'are not diagnostics of a subsequently selected R729 direction.')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def digest(value):
    return (isinstance(value, str) and len(value) == 64
        and all(c in '0123456789abcdef' for c in value))


def finite(value):
    return type(value) in (int, float) and math.isfinite(value)


def definition():
    return dict(schema=SCHEMA, source_sha256=sha(__file__), theorem=THEOREM,
        original_QP_source_sha256=ORIGINAL_QP_SOURCE_SHA256,
        original_QP_schema=ORIGINAL_QP_SCHEMA,
        trigger_phase='restoration', trigger_statuses=list(TRIGGERS),
        original_QP_runs_first_and_report_is_retained_in_full=True,
        all_original_physical_rows_and_nonnegative_slack_row_retained=True,
        objective='.5*(tau0+t)^2+.5*mu^2*(dot(z,z)+t*t)',
        diagonal_H='diag(mu^2 I_n,1+mu^2)',
        dual='min_{lambda>=0} .5 lambda^T (C H^-1 C^T) lambda + (b+C H^-1 q)^T lambda',
        q='tau0 times the last unit vector',
        initialization='lambda=0; never import signed old active-face multipliers',
        coordinate_rule='lambda_i=max(0,lambda_i-(G lambda+r)_i/G_ii)',
        sweep='Visit EVERY augmented row once, in the original complete row order',
        budget='Original maxiter minus original actual advances; this many full sweeps, not CG advances',
        full_sweep_stationarity_early_stop=False,
        full_Gram_construction='All physical column blocks and the complete common-slack column',
        full_Gram_working_symmetrization='0.5*G+0.5*G.T; no eigenvalue/rank truncation or added regularization',
        recovery='For the final finite dual iterate only: t=max(-tau0/(1+mu^2),max_i((u_i z-b_i)/beta_i))',
        candidates='Original returned direction, zero direction, and the final dual slack-repaired direction',
        selection='Smallest recomputed original regularized objective among finite candidates feasible at the original finite tolerance; stable ties retain the earlier candidate',
        source_matrix_reads='Original complete virtual C and original physical row matrix; complete column order and actual positive row scales',
        final_diagnostics='Reread original C and its transpose, not just the accumulated Gram',
        finite_failure='Retain a previously verified original or zero direction and all errors; never adopt an unverified recovered direction',
        old_face_gradient_used_as_dual_stationarity=False,
        floating_gap_or_stationarity_is_an_outward_certificate=False,
        nonlinear_acceptance_changed=False, new_field_or_root_or_derivative_calls=0,
        metric_QP_changed=False, current_QP_rank_tolerance_changed=False,
        duplicate_complete_row_cache_created=False)


def _error(stage, error):
    return dict(stage=stage, type=type(error).__name__,
        exception_module=type(error).__module__, message=str(error),
        representation=repr(error),
        traceback=traceback.format_exception(type(error), error, error.__traceback__))


def _array_record(np, value):
    a = np.ascontiguousarray(value, dtype=np.float64)
    h = hashlib.sha256()
    h.update(str(a.dtype).encode())
    h.update(repr(tuple(a.shape)).encode())
    h.update(a.tobytes(order='C'))
    return dict(dtype=str(a.dtype), shape=list(a.shape), bytes=int(a.nbytes),
        sha256=h.hexdigest())


def _numerical_objective(np, value, tau0, mu2):
    squared_norm = float(value @ value)
    data = .5*float(tau0+value[-1])**2
    regularization = .5*mu2*squared_norm
    total = data+regularization
    if not all(math.isfinite(v) for v in (squared_norm, data, regularization, total)):
        raise FloatingPointError('Nonfinite original common-slack objective')
    return dict(coordinate_squared_norm=squared_norm,
        coordinate_norm=float(np.linalg.norm(value)), data_objective=data,
        regularization_objective=regularization, regularized_objective=total,
        common_slack_increment=float(value[-1]), common_slack=float(tau0+value[-1]))


class _OriginalRows:
    """Finite column streams, with no full physical-row duplicate.

    The virtual augmented matrix is read through the unchanged CommonSlackRows
    interface. Physical g is independently recomputed from its original matrix,
    original row scale and original g. Hashes describe full column-block order;
    they are not mislabeled as a row-major NumPy array digest.
    """
    def __init__(self, np, matrix, bounds, row_metadata, block_columns, counts):
        self.np = np
        self.matrix = matrix
        self.bounds = np.asarray(bounds, dtype=np.float64)
        self.m, self.n = matrix.shape
        self.block = int(block_columns)
        self.counts = counts
        self.virtual_digest = None
        self.physical_digest = None
        self.gs = np.asarray([r['physical_g'] for r in row_metadata], dtype=np.float64)
        self.scales = np.asarray([r['row_normalization_scale'] for r in row_metadata], dtype=np.float64)
        self.beta = -np.asarray(matrix[:, self.n-1:self.n], dtype=np.float64)[:, 0]
        self.counts['actual_slack_column_reads'] += 1
        if (self.block < 1 or self.bounds.shape != (self.m,)
                or self.gs.shape != (self.m-1,) or self.scales.shape != (self.m-1,)
                or not np.isfinite(self.bounds).all() or not np.isfinite(self.beta).all()
                or np.any(self.beta <= 0) or self.beta[-1] != 1.
                or not np.isfinite(self.gs).all() or not np.isfinite(self.scales).all()
                or np.any(self.scales <= 0)):
            raise ValueError('Every actual common-slack coefficient and original row is required')
        expected = -np.r_[np.asarray(matrix.slack_column, dtype=np.float64), -1.]
        if not np.array_equal(self.beta, expected):
            raise ValueError('The actual full common-slack column differs from its source object')

    def pass_rows(self, *, vectors=None, transpose=None, gram_mu2=None, physical=None):
        np = self.np
        vectors = {} if vectors is None else vectors
        physical = {} if physical is None else physical
        for value in vectors.values():
            if value.shape != (self.n,) or not np.isfinite(value).all():
                raise ValueError('Keep one finite complete augmented direction per actual row product')
        for value in physical.values():
            if value.shape != (self.n-1,) or not np.isfinite(value).all():
                raise ValueError('Keep every complete original physical step coordinate')
        if transpose is not None and (transpose.shape != (self.m,)
                or not np.isfinite(transpose).all()):
            raise ValueError('Keep the full finite multiplier vector')
        products = {key: np.zeros(self.m) for key in vectors}
        physical_products = {key: np.zeros(self.m-1) for key in physical}
        transposed = None if transpose is None else np.empty(self.n)
        gram = None if gram_mu2 is None else np.zeros((self.m, self.m))
        h = hashlib.sha256()
        h.update(json.dumps(dict(shape=[self.m,self.n],dtype='float64',
            column_block_size=self.block), sort_keys=True,separators=(',',':')).encode())
        hp = hashlib.sha256()
        hp.update(json.dumps(dict(shape=[self.m-1,self.n-1],dtype='float64',
            column_block_size=self.block), sort_keys=True,separators=(',',':')).encode())
        self.counts['full_virtual_row_passes_started'] += 1
        if physical:
            self.counts['full_original_physical_row_passes_started'] += 1
        for first in range(0, self.n, self.block):
            last = min(self.n, first+self.block)
            block = np.ascontiguousarray(self.matrix[:,first:last], dtype=np.float64)
            self.counts['virtual_column_blocks_read'] += 1
            self.counts['virtual_column_bytes_read'] += int(block.nbytes)
            if block.shape != (self.m,last-first) or not np.isfinite(block).all():
                raise FloatingPointError('An actual complete C column block is nonfinite or changed shape')
            h.update(block.tobytes(order='C'))
            for key, value in vectors.items():
                products[key] += block @ value[first:last]
                self.counts['virtual_block_matvec_products'] += 1
            if transpose is not None:
                transposed[first:last] = block.T @ transpose
                self.counts['virtual_block_transpose_products'] += 1
            physical_last = min(last, self.n-1)
            width = max(0,physical_last-first)
            if gram is not None:
                if width:
                    qblock = block[:,:width]
                    gram += (qblock @ qblock.T)/gram_mu2
                    self.counts['Gram_physical_column_products'] += 1
                if last == self.n:
                    last_column = block[:,-1]
                    gram += np.outer(last_column,last_column)/(1.+gram_mu2)
                    self.counts['Gram_common_slack_column_products'] += 1
            if physical and width:
                original = np.ascontiguousarray(self.matrix.matrix[:,first:physical_last],
                    dtype=np.float64)
                self.counts['physical_column_blocks_read'] += 1
                self.counts['physical_column_bytes_read'] += int(original.nbytes)
                if original.shape != (self.m-1,width) or not np.isfinite(original).all():
                    raise FloatingPointError('An actual original physical C block is nonfinite or changed shape')
                hp.update(original.tobytes(order='C'))
                for key,value in physical.items():
                    physical_products[key] += original @ value[first:physical_last]
                    self.counts['physical_block_matvec_products'] += 1
                del original
            del block
        actual = h.hexdigest()
        if self.virtual_digest is not None and actual != self.virtual_digest:
            raise ValueError('The original complete C bytes changed during common-slack recovery')
        self.virtual_digest = actual
        if physical:
            actual_physical = hp.hexdigest()
            if self.physical_digest is not None and actual_physical != self.physical_digest:
                raise ValueError('The original complete physical row bytes changed')
            self.physical_digest = actual_physical
            self.counts['full_original_physical_row_passes_completed'] += 1
        self.counts['full_virtual_row_passes_completed'] += 1
        all_values = list(products.values())+list(physical_products.values())
        if transposed is not None:
            all_values.append(transposed)
        if gram is not None:
            all_values.append(gram)
        if any(not np.isfinite(value).all() for value in all_values):
            raise FloatingPointError('An actual full row product overflowed or became nonfinite')
        return products, physical_products, transposed, gram

    def candidate(self, label, value, *, tau0, mu2, tolerance, result=None):
        np = self.np
        if result is None:
            result = self.pass_rows(vectors={label:value},physical={label:value[:-1]})
        cy = result[0][label]
        physical_values = result[1][label]
        physical_g = self.gs+self.scales*physical_values
        slack = self.bounds-cy
        if not np.isfinite(physical_g).all() or not np.isfinite(slack).all():
            raise FloatingPointError('Actual selected physical g or original C slack is nonfinite')
        maximum = float(np.max(cy-self.bounds,initial=0.))
        answer = dict(label=label, coordinate_words=_array_record(np,value),
            physical_coordinate_words=_array_record(np,value[:-1]),
            **_numerical_objective(np,value,tau0,mu2),
            normalized_row_values=cy.tolist(), normalized_final_slack=slack.tolist(),
            maximum_linear_violation=maximum,
            minimum_normalized_slack=float(np.min(slack)),
            original_normalized_physical_row_values=physical_values.tolist(),
            original_selected_linear_physical_g=physical_g.tolist(),
            maximum_selected_linear_physical_g=float(np.max(physical_g)),
            original_finite_feasibility_tolerance=tolerance,
            eligible_at_original_finite_tolerance=bool(maximum<=tolerance),
            binary64_row_products_nonpositive=bool(maximum==0.),
            original_complete_C_reread=True,
            original_complete_physical_C_reread=True,
            exact_primal_upper_bound_certified=False)
        return answer


def _legacy_candidate(np, value, original_report, *, tau0, mu2, tolerance):
    """A retained original-return fallback is explicitly not a new C reread."""
    answer = dict(label='original_QPv3',coordinate_words=_array_record(np,value),
        physical_coordinate_words=_array_record(np,value[:-1]),
        **_numerical_objective(np,value,tau0,mu2),
        normalized_row_values=original_report['normalized_row_values'],
        normalized_final_slack=original_report['normalized_final_slack'],
        maximum_linear_violation=original_report['maximum_linear_violation'],
        original_finite_feasibility_tolerance=tolerance,
        eligible_at_original_finite_tolerance=bool(
            original_report['maximum_linear_violation']<=tolerance),
        original_complete_C_reread=False,
        retained_original_QPv3_complete_C_return=True,
        original_complete_physical_C_reread=False,
        exact_primal_upper_bound_certified=False)
    return answer


def _select(candidates):
    eligible = [(record,value) for record,value in candidates
        if record['eligible_at_original_finite_tolerance']]
    if not eligible:
        raise ArithmeticError('No finite candidate satisfies the original finite linear feasibility tolerance')
    return min(eligible,key=lambda item:item[0]['regularized_objective'])


def _dual_scalars(np, lam, gradient, gram, r):
    pg = lam-np.maximum(0.,lam-gradient)
    psi = .5*float(lam @ (gram @ lam))+float(r @ lam)
    answer = dict(dual_psi=psi,nonnegative_multiplier_sum=float(np.sum(lam)),
        multiplier_max=float(np.max(lam,initial=0.)),
        Gram_projected_gradient_mapping_norm=float(np.linalg.norm(pg)),
        Gram_projected_gradient_mapping_max=float(np.max(np.abs(pg),initial=0.)))
    if not all(math.isfinite(value) for value in answer.values()):
        raise FloatingPointError('A finite dual diagnostic overflowed')
    return answer

def recover(original_step, original_report, row_matrix, bounds, *,
            record, model_identity, args, phase, damping):
    """Return the actual direction to the unchanged original nonlinear trials.

    There is no new CLI or independent solve. The existing actual complete C,
    all row metadata, bounds, original report and original numerical arguments
    are the inputs. A new high-dimensional primal candidate is constructed only
    after the budgeted full dual sweeps, not after every coordinate or sweep.
    """
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('The complete scientific recovery runs only in public repository Actions')
    import numpy as np
    if (phase not in ('metric','restoration') or record.get('phase')!=phase
            or original_report.get('schema')!=ORIGINAL_QP_SCHEMA
            or not digest(model_identity)):
        raise ValueError('Keep the actual original phase, complete QPv3 report and full model identity')
    limit = args.restoration_maxiter if phase=='restoration' else args.maxiter
    advances = original_report.get('advances')
    if (type(limit) is not int or limit<0 or type(advances) is not int
            or not 0<=advances<=limit or original_report.get('maxiter')!=limit
            or not finite(damping) or damping<=0
            or float(original_report.get('damping')).hex()!=float(damping).hex()):
        raise ValueError('The fallback consumes the same actual damping and remaining original budget')
    point = (record.get('starting_geometry') or {}).get('current_full_point_sha256')
    if not digest(point):
        raise ValueError('The complete actual starting field point is required')
    original_identity = canonical(original_report)
    enabled = phase=='restoration' and original_report['status'] in TRIGGERS
    remaining = limit-advances if enabled else 0
    started = time.monotonic()
    counts = {key:0 for key in (
        'actual_slack_column_reads','full_virtual_row_passes_started',
        'full_virtual_row_passes_completed','full_original_physical_row_passes_started',
        'full_original_physical_row_passes_completed','virtual_column_blocks_read',
        'virtual_column_bytes_read','virtual_block_matvec_products',
        'virtual_block_transpose_products','Gram_physical_column_products',
        'Gram_common_slack_column_products','physical_column_blocks_read',
        'physical_column_bytes_read','physical_block_matvec_products')}
    answer = dict(schema=REPORT_SCHEMA,definition_identity_sha256=canonical(definition()),
        source_sha256=sha(__file__),phase=phase,index=record['index'],serial=record['serial'],
        model_identity_sha256=model_identity,current_full_point_sha256=point,
        original_QP_report_identity_sha256=original_identity,
        original_QP_status=original_report['status'],
        original_QP_diagnostics_scope=ORIGINAL_SCOPE,
        triggered=enabled,attempted=False,status='not_triggered',
        budget=dict(original_limit=limit,original_CG_advances=advances,
            remaining_full_sweeps=remaining,full_sweeps_started=0,
            full_sweeps_completed=0,coordinate_visits=0,nonzero_coordinate_updates=0,
            incomplete_sweep_coordinate_visits=0,
            original_advances_are_not_dual_sweeps=True,
            coordinate_updates_are_not_CG_advances=True),
        actual_stream_counts=counts,history=[],errors=[],candidates=[],
        selected_direction_source='original_QPv3',
        selected_direction_changed=False,fallback_adopted=False,
        actual_selected_direction=None,final_original_C_reread_complete=False,
        final_diagnostics=None,dual_multipliers=None,input_binding=None,
        numerical_diagnostics_only=True,exact_gap_certificate=False,
        exact_primal_upper_bound_certified=False,
        original_nonlinear_line_search_and_acceptance_unchanged=True,
        original_finite_feasibility_tolerance=float(args.qp_feasibility_tolerance),
        additional_field_root_J_or_transpose_calls=0,
        original_report_retained_whole_and_unmodified=True)
    record[DIRECTION_KEY] = answer
    if not enabled:
        answer['seconds'] = time.monotonic()-started
        return original_step
    if remaining==0:
        answer.update(status='no_remaining_full_sweep_budget',
            seconds=time.monotonic()-started)
        return original_step

    tolerance = float(args.qp_feasibility_tolerance)
    tau0 = float(row_matrix.tau0)
    mu2 = float(damping)**2
    original = np.asarray(original_step,dtype=np.float64)
    metadata = record['complete_selected_inequalities']
    quadratic = record['quadratic_model']
    if (not math.isfinite(tolerance) or tolerance<0 or not math.isfinite(tau0)
            or not math.isfinite(mu2) or mu2<=0 or not math.isfinite(1.+mu2)
            or original.ndim!=1 or original.shape!=(row_matrix.shape[1],)
            or not np.isfinite(original).all()
            or row_matrix.record.get('schema')!='complete-all-typed-C-common-slack-phase-I-v1'
            or row_matrix.record.get('all_original_rows_retained') is not True
            or row_matrix.shape!=(len(metadata['rows'])+1,len(original))
            or row_matrix.m!=len(metadata['rows']) or row_matrix.n!=len(original)-1
            or quadratic.get('original_rows')!=len(metadata['rows'])
            or quadratic.get('augmented_rows')!=len(metadata['rows'])+1
            or quadratic.get('tau_initial')!=tau0
            or float(quadratic['damping']).hex()!=float(damping).hex()):
        raise ValueError('Bind the entire actual source-defined common-slack problem before recovery')
    real_bounds = np.asarray(bounds,dtype=np.float64)
    if (real_bounds.shape!=(row_matrix.shape[0],)
            or not np.isfinite(real_bounds).all()
            or _array_record(np,real_bounds)!=_array_record(np,np.asarray(row_matrix.bounds,dtype=np.float64))
            or _array_record(np,real_bounds)!=_array_record(np,np.asarray(original_report['normalized_bounds'],dtype=np.float64))
            or float(np.min(real_bounds)) < -tolerance):
        raise ValueError('The original complete bounds or feasible zero-start contract changed')
    original_words = _array_record(np,original)
    legacy = _legacy_candidate(np,original,original_report,tau0=tau0,mu2=mu2,tolerance=tolerance)
    if not legacy['eligible_at_original_finite_tolerance']:
        raise ValueError('The complete original dependent-blocker return is not a retained finite feasible direction')
    selected_data,selected = legacy,original
    retained_data,retained = legacy,original
    answer['attempted'] = True
    source_path = Path(type(row_matrix).__getitem__.__code__.co_filename).resolve()
    answer['input_binding'] = dict(
        common_slack_class_source=dict(path=str(source_path),sha256=sha(source_path),
            bytes=source_path.stat().st_size),
        actual_original_QP_report_identity_sha256=original_identity,
        complete_selected_inequalities_identity_sha256=canonical(metadata),
        row_shape=list(row_matrix.shape),physical_row_count=len(metadata['rows']),
        full_physical_coordinate_count=len(original)-1,
        bounds_words=_array_record(np,real_bounds),
        normalized_bounds_identity_sha256=canonical(original_report['normalized_bounds']),
        original_coordinate_words=original_words,tau_initial=tau0,
        tau_initial_binary64_hex=tau0.hex(),damping=float(damping),
        damping_binary64_hex=float(damping).hex(),mu_squared=mu2,
        original_block_columns=int(args.active_block_columns),
        all_rows_in_original_order=True,no_row_rank_truncation=True,
        original_gradient_row_scaling_not_recomputed=True,
        complete_virtual_C_column_stream_sha256=None,
        complete_original_physical_C_column_stream_sha256=None,
        digest_order='Complete contiguous column blocks in increasing column order, with recorded shape/dtype/block size; not a row-major array digest')
    rows = None
    lam = gram = r = xdual = None
    stage = 'initial_original_and_zero_actual_C_reads'
    recovered_successfully = False
    try:
        with np.errstate(over='raise',invalid='raise',divide='raise'):
            rows = _OriginalRows(np,row_matrix,real_bounds,metadata['rows'],
                args.active_block_columns,counts)
            zero = np.zeros_like(original)
            initial = rows.pass_rows(vectors={'original_QPv3':original,'zero':zero},
                physical={'original_QPv3':original[:-1],'zero':zero[:-1]})
            original_data = rows.candidate('original_QPv3',original,tau0=tau0,mu2=mu2,
                tolerance=tolerance,result=initial)
            zero_data = rows.candidate('zero',zero,tau0=tau0,mu2=mu2,
                tolerance=tolerance,result=initial)
            answer['candidates'].extend([original_data,zero_data])
            retained_data,retained = _select([(original_data,original),(zero_data,zero)])
            selected_data,selected = retained_data,retained
            answer['input_binding']['common_slack_beta_words'] = _array_record(np,rows.beta)
            answer['input_binding']['common_slack_beta'] = rows.beta.tolist()
            answer['input_binding']['minimum_beta'] = float(np.min(rows.beta))

            stage = 'complete_all_column_Gram'
            _,_,_,gram = rows.pass_rows(gram_mu2=mu2)
            asymmetry = float(np.max(np.abs(gram-gram.T),initial=0.))
            gram = .5*gram+.5*gram.T
            diagonal = np.diag(gram).copy()
            if not np.isfinite(gram).all() or np.any(diagonal<=0):
                raise FloatingPointError('A finite positive complete Gram diagonal is required; no rank repair is substituted')
            r = real_bounds-rows.beta*(tau0/(1.+mu2))
            lam = np.zeros(rows.m)
            h = r.copy()
            if not np.isfinite(r).all():
                raise FloatingPointError('Nonfinite full dual linear term')
            answer['Gram'] = dict(shape=[rows.m,rows.m],bytes=int(gram.nbytes),
                whole_words=_array_record(np,gram),
                original_stream_roundoff_asymmetry_max=asymmetry,
                working_symmetrization='.5*G+.5*G.T',
                minimum_diagonal=float(np.min(diagonal)),
                maximum_diagonal=float(np.max(diagonal)),
                beta_minimum=float(np.min(rows.beta)),
                positive_orthant_coercivity_coefficient=float(np.min(rows.beta))**2/(1.+mu2),
                all_physical_columns_retained=True,all_rows_retained=True,
                inverse_or_pseudoinverse_used=False,eigenvalue_or_rank_truncation_used=False,
                extra_regularization_used=False,original_complete_row_cache_duplicated=False)
            stage = 'complete_cyclic_dual_sweeps'
            for sweep in range(remaining):
                answer['budget']['full_sweeps_started'] += 1
                before = counts.copy()
                updates = 0
                max_update = 0.
                start_visits = answer['budget']['coordinate_visits']
                h = gram @ lam+r
                if not np.isfinite(h).all():
                    raise FloatingPointError('Nonfinite full dual gradient before a sweep')
                for index in range(rows.m):
                    answer['budget']['coordinate_visits'] += 1
                    answer['budget']['incomplete_sweep_coordinate_visits'] += 1
                    proposal = float(lam[index]-h[index]/diagonal[index])
                    if not math.isfinite(proposal):
                        raise FloatingPointError('Nonfinite complete-row coordinate minimizer')
                    new_value = max(0.,proposal)
                    difference = new_value-float(lam[index])
                    if difference!=0.:
                        next_h = h+gram[:,index]*difference
                        if not np.isfinite(next_h).all():
                            raise FloatingPointError('Nonfinite dual gradient update; previous legal multipliers are retained')
                        lam[index] = new_value
                        h = next_h
                        updates += 1
                        answer['budget']['nonzero_coordinate_updates'] += 1
                        max_update = max(max_update,abs(difference))
                recomputed = gram @ lam+r
                defect = float(np.max(np.abs(recomputed-h),initial=0.))
                if not np.isfinite(recomputed).all() or np.any(lam<0):
                    raise FloatingPointError('The complete sweep did not retain a finite nonnegative dual iterate')
                h = recomputed
                values = _dual_scalars(np,lam,h,gram,r)
                answer['history'].append(dict(full_sweep=sweep+1,
                    complete_original_row_visits=answer['budget']['coordinate_visits']-start_visits,
                    nonzero_coordinate_updates=updates,maximum_coordinate_change=max_update,
                    Gram_gradient_accumulation_defect=defect,**values,
                    high_dimensional_primal_candidate_constructed=False,
                    additional_original_row_passes=counts['full_virtual_row_passes_started']-
                        before['full_virtual_row_passes_started']))
                answer['budget']['full_sweeps_completed'] += 1
                answer['budget']['incomplete_sweep_coordinate_visits'] = 0

            stage = 'final_dual_physical_direction'
            _,_,ctl,_ = rows.pass_rows(transpose=lam)
            xdual = -ctl/mu2
            xdual[-1] = -(ctl[-1]+tau0)/(1.+mu2)
            if not np.isfinite(xdual).all():
                raise FloatingPointError('The original complete transpose produced a nonfinite dual physical direction')
            zzero = xdual.copy()
            zzero[-1] = 0.
            products,_,_,_ = rows.pass_rows(vectors={'dual':xdual,'physical_only':zzero})
            lower_rows = (products['physical_only']-real_bounds)/rows.beta
            if not np.isfinite(lower_rows).all():
                raise FloatingPointError('The complete-row optimal slack repair is nonfinite')
            lower = float(np.max(lower_rows))
            unconstrained = -tau0/(1.+mu2)
            repaired = xdual.copy()
            repaired[-1] = max(unconstrained,lower)
            answer['slack_repair'] = dict(
                original_all_row_lower_bounds=lower_rows.tolist(),
                maximum_original_row_lower_bound=lower,
                unconstrained_scalar_minimizer=unconstrained,
                selected_scalar_minimizer=float(repaired[-1]),
                original_tau_nonnegative_row_included=True,
                upward_rounding_or_extra_margin_added=False,
                exact_optimal_scalar_formula=True,
                binary64_evaluation_is_not_exact_arithmetic=True)
            stage = 'recovered_candidate_actual_full_C'
            new_data = rows.candidate('R729_dual_final_slack_repaired',repaired,
                tau0=tau0,mu2=mu2,tolerance=tolerance)
            answer['candidates'].append(new_data)
            selected_data,selected = _select([(retained_data,retained),(new_data,repaired)])
            recovered_successfully = True
            answer['status'] = 'complete_remaining_full_sweeps_and_actual_candidate'
    except Exception as error:
        answer['errors'].append(_error(stage,error))
        selected_data,selected = retained_data,retained
        answer['status'] = 'finite_recovery_failure_retained_original_or_zero'
        recovered_successfully = False

    # This is a fresh final original-C read even if the selected candidate is an
    # earlier retained one. A failed final reread never licenses a new direction.
    stage = 'final_selected_original_C_and_transpose_reread'
    try:
        with np.errstate(over='raise',invalid='raise',divide='raise'):
            if rows is None:
                raise RuntimeError('The complete original row stream was not initialized')
            vectors = {'selected':selected}
            if recovered_successfully:
                vectors['dual'] = xdual
            final = rows.pass_rows(vectors=vectors,
                physical={'selected':selected[:-1]},
                transpose=(lam if recovered_successfully else None))
            fresh = rows.candidate('selected',selected,tau0=tau0,mu2=mu2,
                tolerance=tolerance,result=final)
            fresh['label'] = selected_data['label']
            if not fresh['eligible_at_original_finite_tolerance']:
                raise ArithmeticError('The final full original C read rejects the selected finite candidate')
            selected_data = fresh
            answer['final_original_C_reread_complete'] = True
            if recovered_successfully:
                cy, cdual, ct = final[0]['selected'],final[0]['dual'],final[2]
                hg = mu2*selected
                hg[-1] = (1.+mu2)*selected[-1]+tau0
                hd = mu2*xdual
                hd[-1] = (1.+mu2)*xdual[-1]+tau0
                actual_dual_gradient = real_bounds-cdual
                gram_gradient = gram @ lam+r
                mapping = lam-np.maximum(0.,lam-actual_dual_gradient)
                constant = .5*tau0*tau0
                qct = ct.copy()
                qct[-1] += tau0
                hinv_qct = qct/mu2
                hinv_qct[-1] = qct[-1]/(1.+mu2)
                dual_value = constant-.5*float(qct @ hinv_qct)-float(real_bounds @ lam)
                gap = fresh['regularized_objective']-dual_value
                difference = selected-xdual
                h_difference = mu2*difference
                h_difference[-1] = (1.+mu2)*difference[-1]
                square_term = .5*float(difference @ h_difference)
                complementary_term = float(lam @ (real_bounds-cy))
                diagnostics = dict(
                    actual_dual_objective=dual_value,
                    actual_selected_primal_objective=fresh['regularized_objective'],
                    numerical_primal_dual_gap=gap,
                    numerical_gap_square_term=square_term,
                    numerical_gap_complementary_term=complementary_term,
                    numerical_gap_identity_defect=gap-square_term-complementary_term,
                    actual_C_dual_gradient=actual_dual_gradient.tolist(),
                    actual_C_dual_projected_gradient_mapping_norm=float(np.linalg.norm(mapping)),
                    actual_C_dual_projected_gradient_mapping_max=float(np.max(np.abs(mapping),initial=0.)),
                    original_C_versus_Gram_dual_gradient_defect=float(np.max(np.abs(
                        actual_dual_gradient-gram_gradient),initial=0.)),
                    actual_C_selected_primal_stationarity_norm=float(np.linalg.norm(hg+ct)),
                    actual_C_dual_primal_stationarity_norm=float(np.linalg.norm(hd+ct)),
                    actual_C_selected_maximum_complementarity=float(np.max(
                        np.abs(lam*(real_bounds-cy)),initial=0.)),
                    actual_C_dual_maximum_complementarity=float(np.max(
                        np.abs(lam*(real_bounds-cdual)),initial=0.)),
                    actual_C_selected_maximum_linear_violation=fresh['maximum_linear_violation'],
                    actual_C_unrepaired_dual_maximum_linear_violation=float(np.max(
                        cdual-real_bounds,initial=0.)),
                    old_face_projected_gradient_reused=False,
                    exact_KKT_or_gap_certificate=False,
                    finite_sweep_convergence_claimed=False)
                if any(not math.isfinite(value) for key,value in diagnostics.items()
                        if type(value) in (int,float)):
                    raise FloatingPointError('Nonfinite actual original-C final dual diagnostic')
                answer['final_diagnostics'] = diagnostics
    except Exception as error:
        answer['errors'].append(_error(stage,error))
        answer['status'] = 'final_diagnostic_failure_retained_original_or_zero'
        selected_data,selected = retained_data,retained
        answer['final_original_C_reread_complete'] = False
        answer['final_diagnostics'] = None
        recovered_successfully = False
        if rows is not None:
            try:
                selected_data = rows.candidate(retained_data['label'],retained,
                    tau0=tau0,mu2=mu2,tolerance=tolerance)
                if not selected_data['eligible_at_original_finite_tolerance']:
                    raise ArithmeticError('The retained candidate fails the final original C reread')
                answer['final_original_C_reread_complete'] = True
            except Exception as retained_error:
                answer['errors'].append(_error('retained_candidate_final_C_reread',retained_error))
                selected_data,selected = legacy,original
                answer['final_original_C_reread_complete'] = False

    if canonical(original_report)!=original_identity or _array_record(np,original)!=original_words:
        raise ValueError('The full original QPv3 report or returned direction was modified')
    if rows is not None:
        answer['input_binding']['complete_virtual_C_column_stream_sha256'] = rows.virtual_digest
        answer['input_binding']['complete_original_physical_C_column_stream_sha256'] = rows.physical_digest
    if lam is not None and np.isfinite(lam).all() and np.all(lam>=0):
        answer['dual_multipliers'] = lam.tolist()
    answer['actual_selected_direction'] = selected_data
    answer['selected_direction_source'] = selected_data['label']
    answer['selected_direction_changed'] = selected_data['coordinate_words']!=original_words
    answer['fallback_adopted'] = selected_data['label']=='R729_dual_final_slack_repaired'
    answer['seconds'] = time.monotonic()-started
    return selected

def _plain_int(value):
    return type(value) is int and value>=0


def _vector(value, length):
    return isinstance(value,list) and len(value)==length and all(finite(v) for v in value)


def _word_record(value, length):
    return (isinstance(value,dict) and value.get('dtype')=='float64'
        and value.get('shape')==[length] and value.get('bytes')==8*length
        and digest(value.get('sha256')))


def _checked_candidate(value, *, m, n, tolerance):
    if (not isinstance(value,dict)
            or value.get('label') not in ('original_QPv3','zero','R729_dual_final_slack_repaired')
            or not _word_record(value.get('coordinate_words'),n)
            or not _word_record(value.get('physical_coordinate_words'),n-1)
            or not _vector(value.get('normalized_row_values'),m)
            or not _vector(value.get('normalized_final_slack'),m)
            or value.get('original_finite_feasibility_tolerance')!=tolerance
            or value.get('exact_primal_upper_bound_certified') is not False
            or not all(finite(value.get(k)) for k in ('coordinate_squared_norm',
                'coordinate_norm','data_objective','regularization_objective',
                'regularized_objective','common_slack_increment','common_slack',
                'maximum_linear_violation'))
            or value['maximum_linear_violation']<0
            or value.get('eligible_at_original_finite_tolerance') is not
                (value['maximum_linear_violation']<=tolerance)):
        raise ValueError('A recovered candidate lost its full original finite-QP meaning')
    if value.get('original_complete_C_reread') is True:
        if (value.get('original_complete_physical_C_reread') is not True
                or not _vector(value.get('original_normalized_physical_row_values'),m-1)
                or not _vector(value.get('original_selected_linear_physical_g'),m-1)
                or not finite(value.get('maximum_selected_linear_physical_g'))):
            raise ValueError('Keep the complete actual physical g read as well as the normalized C read')
    elif (value.get('label')!='original_QPv3'
            or value.get('retained_original_QPv3_complete_C_return') is not True):
        raise ValueError('Only the complete original return may be retained without a successful new C read')
    return value


def bind_report(report):
    """Pure stdlib binding and a per-direction checker; no numerical arrays read.

    The legacy direction readout remains unchanged. Its old QP fields are
    explicitly attributed to the original attempt. This separate complete
    result identifies the actual direction passed to the original outer trial.
    """
    expected = definition()
    roles = report['source_sha256_by_role']
    if (roles.get(ROLE)!=sha(__file__) or roles.get('qp')!=ORIGINAL_QP_SOURCE_SHA256
            or report.get(DEFINITION_KEY)!=expected
            or not digest(report.get('source_sha256'))
            or not digest(report.get('model_identity_sha256'))):
        raise ValueError('Bind the complete new kernel and the unchanged full original QPv3 source')
    definition_identity = canonical(expected)
    model = report['model_identity_sha256']
    driver = report['source_sha256']

    def check(value):
        qp = value['qp']
        recovery = value.get(DIRECTION_KEY)
        phase = value['phase']
        actual_trigger = phase=='restoration' and qp.get('status') in TRIGGERS
        limit = report['restoration_maxiter'] if phase=='restoration' else report['maxiter']
        if (not isinstance(recovery,dict) or recovery.get('schema')!=REPORT_SCHEMA
                or recovery.get('source_sha256')!=roles[ROLE]
                or recovery.get('definition_identity_sha256')!=definition_identity
                or qp.get('schema')!=ORIGINAL_QP_SCHEMA
                or recovery.get('original_QP_report_identity_sha256')!=canonical(qp)
                or recovery.get('original_QP_status')!=qp.get('status')
                or recovery.get('original_QP_diagnostics_scope')!=ORIGINAL_SCOPE
                or recovery.get('phase')!=phase or recovery.get('index')!=value['index']
                or recovery.get('serial')!=value['serial']
                or recovery.get('model_identity_sha256')!=model
                or recovery.get('current_full_point_sha256')!=(value.get(
                    'starting_geometry') or {}).get('current_full_point_sha256')
                or recovery.get('triggered') is not actual_trigger
                or recovery.get('numerical_diagnostics_only') is not True
                or recovery.get('exact_gap_certificate') is not False
                or recovery.get('exact_primal_upper_bound_certified') is not False
                or recovery.get('original_nonlinear_line_search_and_acceptance_unchanged') is not True
                or recovery.get('additional_field_root_J_or_transpose_calls')!=0
                or recovery.get('original_report_retained_whole_and_unmodified') is not True
                or float(value['actual_damping']).hex()!=float(qp['damping']).hex()):
            raise ValueError('Keep the whole old QP attempt separate from the actual new direction')
        budget = recovery['budget']
        remaining = limit-qp['advances'] if actual_trigger else 0
        integer_keys = ('original_limit','original_CG_advances','remaining_full_sweeps',
            'full_sweeps_started','full_sweeps_completed','coordinate_visits',
            'nonzero_coordinate_updates','incomplete_sweep_coordinate_visits')
        if (not all(_plain_int(budget.get(k)) for k in integer_keys)
                or budget['original_limit']!=limit or qp['maxiter']!=limit
                or budget['original_CG_advances']!=qp['advances']
                or budget['remaining_full_sweeps']!=remaining
                or not 0<=budget['full_sweeps_completed']<=budget['full_sweeps_started']<=remaining
                or budget['full_sweeps_started']-budget['full_sweeps_completed']>1
                or budget['original_CG_advances']+budget['full_sweeps_started']>limit
                or budget['nonzero_coordinate_updates']>budget['coordinate_visits']
                or budget.get('original_advances_are_not_dual_sweeps') is not True
                or budget.get('coordinate_updates_are_not_CG_advances') is not True
                or not isinstance(recovery.get('history'),list)
                or not isinstance(recovery.get('errors'),list)
                or not finite(recovery.get('seconds')) or recovery['seconds']<0):
            raise ValueError('Preserve the complete original budget and distinguish its units')
        counts = recovery['actual_stream_counts']
        if (not isinstance(counts,dict) or not all(_plain_int(v) for v in counts.values())
                or counts['full_virtual_row_passes_completed']>counts['full_virtual_row_passes_started']
                or counts['full_original_physical_row_passes_completed']>
                    counts['full_original_physical_row_passes_started']):
            raise ValueError('Actual full original-C streams cannot be inferred from Gram updates')
        attempted = actual_trigger and remaining>0
        if recovery.get('attempted') is not attempted:
            raise ValueError('Only the two declared restoration blockers can consume remaining sweeps')
        if not attempted:
            if (budget['full_sweeps_started'] or budget['coordinate_visits']
                    or recovery['history'] or recovery['errors'] or recovery['candidates']
                    or any(counts.values())
                    or recovery.get('selected_direction_source')!='original_QPv3'
                    or recovery.get('selected_direction_changed') is not False
                    or recovery.get('fallback_adopted') is not False
                    or recovery.get('actual_selected_direction') is not None
                    or recovery.get('input_binding') is not None
                    or recovery.get('final_diagnostics') is not None):
                raise ValueError('A nontriggered QP remains exactly the original path')
            return dict(recovery,original_legacy_fields_scope=ORIGINAL_SCOPE,
                actual_direction_scope='Unchanged original QPv3 direction; no R729 row pass or new candidate')

        inp = recovery['input_binding']
        physical_rows = value['complete_selected_inequalities']['selected_rows']
        m = physical_rows+1
        n = report['original_variables']+1
        tol = recovery['original_finite_feasibility_tolerance']
        if (not isinstance(inp,dict) or not finite(tol) or tol<0
                or inp.get('common_slack_class_source',{}).get('sha256')!=driver
                or inp.get('actual_original_QP_report_identity_sha256')!=canonical(qp)
                or inp.get('complete_selected_inequalities_identity_sha256')!=canonical(
                    value['complete_selected_inequalities'])
                or inp.get('row_shape')!=[m,n] or inp.get('physical_row_count')!=physical_rows
                or inp.get('full_physical_coordinate_count')!=n-1
                or not _word_record(inp.get('bounds_words'),m)
                or inp.get('normalized_bounds_identity_sha256')!=canonical(qp['normalized_bounds'])
                or not _word_record(inp.get('original_coordinate_words'),n)
                or inp.get('tau_initial')!=value['quadratic_model']['tau_initial']
                or inp.get('tau_initial_binary64_hex')!=float(inp['tau_initial']).hex()
                or inp.get('damping_binary64_hex')!=float(value['actual_damping']).hex()
                or inp.get('damping')!=value['actual_damping']
                or inp.get('all_rows_in_original_order') is not True
                or inp.get('no_row_rank_truncation') is not True
                or inp.get('original_gradient_row_scaling_not_recomputed') is not True
                or len(recovery['history'])!=budget['full_sweeps_completed']
                or not 0<=budget['incomplete_sweep_coordinate_visits']<=m
                or budget['coordinate_visits']!=m*budget['full_sweeps_completed']+
                    budget['incomplete_sweep_coordinate_visits']):
            raise ValueError('Keep the full actual common-slack problem and every complete sweep')
        for index,sweep in enumerate(recovery['history']):
            if (sweep.get('full_sweep')!=index+1 or sweep.get('complete_original_row_visits')!=m
                    or not _plain_int(sweep.get('nonzero_coordinate_updates'))
                    or not 0<=sweep['nonzero_coordinate_updates']<=m
                    or sweep.get('high_dimensional_primal_candidate_constructed') is not False
                    or sweep.get('additional_original_row_passes')!=0):
                raise ValueError('A dual sweep must visit all rows, without inventing a primal candidate')
        for error in recovery['errors']:
            if (not isinstance(error,dict)
                    or not all(isinstance(error.get(k),str) for k in
                        ('stage','type','exception_module','message','representation'))
                    or not isinstance(error.get('traceback'),list)
                    or not all(isinstance(v,str) for v in error['traceback'])):
                raise ValueError('Retain each complete original finite failure record')
        for candidate in recovery['candidates']:
            _checked_candidate(candidate,m=m,n=n,tolerance=tol)
        chosen = _checked_candidate(recovery['actual_selected_direction'],m=m,n=n,tolerance=tol)
        if (chosen.get('eligible_at_original_finite_tolerance') is not True
                or recovery.get('selected_direction_source')!=chosen['label']
                or recovery.get('selected_direction_changed') is not
                    (chosen['coordinate_words']!=inp['original_coordinate_words'])
                or recovery.get('fallback_adopted') is not
                    (chosen['label']=='R729_dual_final_slack_repaired')
                or float(chosen['coordinate_norm']).hex()!=float(value['coordinate_step_norm']).hex()
                or float(chosen['common_slack']).hex()!=float(value['computed_common_slack']).hex()):
            raise ValueError('The actual outer trial must receive the explicitly selected complete direction')
        diagnostics = recovery.get('final_diagnostics')
        if recovery.get('status')=='complete_remaining_full_sweeps_and_actual_candidate':
            eligible=[c['regularized_objective'] for c in recovery['candidates']
                if c['eligible_at_original_finite_tolerance']]
            if (not eligible or chosen['regularized_objective']>min(eligible)
                    or budget['full_sweeps_completed']!=remaining or recovery['errors']):
                raise ValueError('Select the best available finite feasible candidate after all declared sweeps')
        if recovery.get('fallback_adopted'):
            if (recovery.get('final_original_C_reread_complete') is not True
                    or chosen.get('original_complete_C_reread') is not True
                    or not isinstance(diagnostics,dict)):
                raise ValueError('A recovered direction requires its actual final original-C diagnostics')
        if diagnostics is not None:
            if (diagnostics.get('old_face_projected_gradient_reused') is not False
                    or diagnostics.get('exact_KKT_or_gap_certificate') is not False
                    or diagnostics.get('finite_sweep_convergence_claimed') is not False
                    or not _vector(diagnostics.get('actual_C_dual_gradient'),m)
                    or not _vector(recovery.get('dual_multipliers'),m)
                    or any(v<0 for v in recovery['dual_multipliers'])):
                raise ValueError('Do not relabel the old face gradient or finite gap as a dual certificate')
        outer_g = value['selected_linear_physical_g']
        if not _vector(outer_g,physical_rows):
            raise ValueError('Keep the original outer complete selected physical g list')
        inner_g = chosen.get('original_selected_linear_physical_g')
        comparison = None if inner_g is None else dict(
            complete_original_physical_row_count=physical_rows,
            all_binary64_words_equal=all(float(a).hex()==float(b).hex()
                for a,b in zip(inner_g,outer_g)),
            maximum_absolute_difference=max((abs(a-b) for a,b in zip(inner_g,outer_g)),default=0.),
            scope='Two actual full reads in their original working arithmetic; not an error certificate')
        return dict(recovery,original_legacy_fields_scope=ORIGINAL_SCOPE,
            actual_direction_scope='The selected finite linear-QP direction passed to unchanged full nonlinear trials',
            original_outer_full_physical_g_reread_comparison=comparison)

    for phase in ('metric','restoration'):
        for value in report.get(phase+'_directions',[]):
            check(value)
    binding = dict(schema=BINDING_SCHEMA,source_sha256=sha(__file__),
        definition=expected,definition_identity_sha256=definition_identity,
        actual_driver_sha256=driver,actual_model_identity_sha256=model,
        actual_complete_source_role_count=len(roles),
        original_QP_source_sha256=roles['qp'],
        original_legacy_direction_QP_fields_scope=ORIGINAL_SCOPE,
        actual_metric_direction_count=len(report.get('metric_directions',[])),
        actual_restoration_direction_count=len(report.get('restoration_directions',[])),
        actual_triggered_direction_count=sum(
            value[DIRECTION_KEY]['triggered']
            for phase in ('metric','restoration') for value in report.get(phase+'_directions',[])),
        actual_adopted_recovered_direction_count=sum(
            value[DIRECTION_KEY]['fallback_adopted']
            for phase in ('metric','restoration') for value in report.get(phase+'_directions',[])),
        original_full_report_objects_retained=True,
        numerical_arrays_recomputed=False,field_or_root_or_J_calls=0,
        continuous_or_nonlinear_feasibility_claimed=False)
    return binding,check
