#!/usr/bin/env python3
"""Original1372 full-block residual readback after a saved height/slope gauge solve.

Actions only. Original actual28/41 J, residuals, target, far graph, and sigma are
retained. A separately identified, finite longdouble-to-binary64 coordinate
representation is equilibrated and factorized. Every returned original delta
is checked by the unchanged complete exact dyadic original-row kernel.
No ODE/J/root/native/trial/acceptance is executed.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib
import json
import os
from pathlib import Path
import resource
import struct
import time
import traceback

import numpy as np
import scipy

HERE = Path(__file__).resolve().parent
GAUGE_NAME = 'exact_20261114_rawcell0_gauge_system.py'
GAUGE_SHA = '24a51a4e804859bcdbed78b133599a073c6a0a890039e5fe5500281ef7e90b92'
EQUIL_NAME = 'geometry_20261114_native_equilibrated_band_correction.py'
EQUIL_SHA = '8f5cb5da0826e3deedf935eca2e62b91c6628861804b2e66c6f853e9459e1dd3'
STEP_DRIVER_NAME = 'exact_20261114_rawcell0_step_equilibrated_correction.py'
STEP_DRIVER_SHA = '30a467e8f08d73fcdcd8a69b2d911e0d9f57489c3397c21c775ed1ec4f6cabe6'
AUXILIARY_ORIGINAL_RHS_EXPONENT = -2048
SCALING = 'saved-node-G-cut-alpha-row-then-original-sigma-dyadic-row-column-equilibration-v1'


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for data in iter(lambda: stream.read(1 << 20), b''):
            h.update(data)
    return h.hexdigest()


def load_pinned(name, digest):
    path = HERE/name
    if sha(path) != digest:
        raise ValueError('Frozen independent helper changed: '+name)
    module = importlib.import_module(Path(name).stem)
    if Path(module.__file__).resolve() != path.resolve():
        raise ImportError('Unexpected helper import path '+name)
    return module


def pair(value):
    """The exact dyadic represented by one saved finite binary64 coefficient."""
    a, b = float(value).as_integer_ratio()
    return a, -(b.bit_length()-1)


def pair_multiply(left, right):
    return left[0]*right[0], left[1]+right[1]


def pair_add(left, right):
    if left[0] == 0:
        return right
    if right[0] == 0:
        return left
    e = min(left[1], right[1])
    return (left[0] << (left[1]-e))+(right[0] << (right[1]-e)), e


def compact_pair(value):
    a, e = value
    if a == 0:
        return ['0x0', 0]
    shift = (abs(a) & -abs(a)).bit_length()-1
    return [hex(a >> shift), e+shift]


class ScopedWriter:
    def __init__(self, B, original, gauge, producer, scope):
        self.B, self.original, self.gauge = B, original, gauge
        self.producer, self.scope = producer, scope

    def __getattr__(self, name):
        return getattr(self.B, name)

    def annotate(self, value):
        if not isinstance(value, dict):
            return value
        result = dict(value,
            wrapper_producer_source_sha256=self.producer,
            original1372_matrix_identity_sha256=self.original.binding['new_matrix_identity_sha256'],
            formed_gauge_matrix_identity_sha256=self.gauge.binding['formed_matrix_identity_sha256'],
            coordinate_identity_sha256=self.gauge.coefficient_identity,
            matrix_scope=self.scope,
            native_accepted=False, task_completed=False)
        if self.scope == 'formed-binary64-gauge-matrix':
            result.update(
                unqualified_original_matrix_in_reused_equilibration_means_saved_formed_gauge_matrix=True,
                original_matrix_not_replaced=False,
                formed_gauge_entries_are_not_changed_between_equilibration_passes=True,
                dyadic_scaling_has_separate_reversibility_ledger=True,
                exact_conjugacy_to_original1372_matrix_claimed=False,
                original1372_exact_sigma_residual_is_the_only_direction_comparison=True)
        else:
            result.update(
                exact_residuals_use_original1372_untransformed_arrays=True,
                norm_uses_original_explicit_sigma_words=True,
                auxiliary_evaluator_RHS_row_exponent=AUXILIARY_ORIGINAL_RHS_EXPONENT,
                auxiliary_evaluator_RHS_is_never_used_in_a_solve=True,
                actual_refinement_RHS_is_rebuilt_from_exact_original_ledger_and_saved_dyadic_G=True)
        return result

    def write(self, path, value, compressed=False):
        return self.B.write(path, self.annotate(value), compressed=compressed)


class ExactGaugeRightHandSide:
    """Exact original dyadics -> exact saved-G row action -> one rounded RHS."""
    def __init__(self, original, gauge, kernel, Q, rows, output, B):
        self.original, self.gauge, self.kernel = original, gauge, kernel
        self.Q, self.rows, self.output, self.B = Q, rows, output, B
        self.M, self.K, self.D = original.M, original.K, original.depth
        self.alpha = [pair(x) for x in gauge.alpha]
        self.eta = [pair(x) for x in gauge.eta]
        self.beta = [[pair(x) for x in row] for row in gauge.beta]

    def transform(self, kind, node, source):
        if kind == 'cut':
            if len(source) != self.M or node != 0:
                raise ValueError('Complete original cut row block required')
            return [pair_multiply(self.alpha[0], p) for p in source]
        if kind == 'far':
            if len(source) != self.M or node != self.D:
                raise ValueError('Complete original far row block required')
            return source
        if kind != 'stage' or len(source) != self.K or not 0 <= node < self.D:
            raise ValueError('Complete original stage block required')
        if node > self.gauge.active_last:
            return source
        top = [pair_multiply(self.alpha[node], source[j]) for j in range(self.M)]
        bottom = [pair_add(pair_multiply(self.beta[node][j], source[j]),
                           pair_multiply(self.eta[node], source[self.M+j]))
                  for j in range(self.M)]
        return top+bottom

    def build(self, blocks, label, source_identity):
        N = (self.D+1)*self.K
        rhs = np.empty(N, dtype=np.float64)
        rounded = zeroed = exact_zeros = completed = rows_seen = 0
        examples = []
        expected = [('cut', 0)]+[('stage', n) for n in range(self.D)]+[('far', self.D)]
        exact_transformed_hash = hashlib.sha256()
        for (kind, node, source), expected_block in zip_strict(blocks, expected):
            if (kind, node) != expected_block:
                raise ValueError('Original complete exact row order changed')
            transformed = self.transform(kind, node, source)
            start = 0 if kind == 'cut' else self.M+node*self.K
            canonical = dict(kind=kind, node=node, first_global_equation_row=start,
                             exact_transformed_unscaled_rows=[compact_pair(x) for x in transformed])
            exact_transformed_hash.update(self.kernel.json_bytes(canonical))
            for j, (m, e) in enumerate(transformed):
                r = start+j
                value, info = self.Q.round_dyadic(-m, e+int(self.rows[r]))
                rhs[r] = value
                rounded += int(info['rounded'])
                zeroed += int(info['underflow_to_zero'])
                exact_zeros += int(info['exact_zero'])
                if info['rounded'] and len(examples) < 8:
                    examples.append(dict(
                        global_equation_row=r, kind=kind, node=node, local_row=j,
                        exact_transformed_residual=compact_pair((m, e)),
                        final_row_exponent=int(self.rows[r]),
                        rounded_rhs_float64le_hex=struct.pack('<d', value).hex()))
            completed += 1
            rows_seen += len(transformed)
        if completed != self.D+2 or rows_seen != N or not np.isfinite(rhs).all():
            raise ValueError('The full original/G/scaled RHS is incomplete or nonfinite')
        record = self.output.save(label+'-actual-gauge-rhs', rhs,
            'One nearest/ties-even rounding of negative exact saved-G times original residual times final dyadic row scale')
        details = dict(
            schema='native-gauge-exact-original-ledger-RHS-v1', label=label,
            source=source_identity, original1372_matrix_identity_sha256=self.original.binding['new_matrix_identity_sha256'],
            coordinate_identity_sha256=self.gauge.coefficient_identity,
            cut_multiplier='saved alpha0', far_multiplier='identity',
            stage_multiplier='saved alpha,beta,eta applied exactly as dyadic coefficients',
            equation_rows=N, blocks=completed, exact_dyadic_row_action_before_final_rounding=True,
            exact_transformed_unscaled_rows_canonical_jsonl_sha256=exact_transformed_hash.hexdigest(),
            rounded_rows=rounded, underflow_to_zero_rows=zeroed, exact_zero_rows=exact_zeros,
            examples=examples, actual_rhs=record,
            source_ledger_plus_saved_G_plus_row_exponents_reconstruct_all_rhs_values=True,
            native_accepted=False)
        self.B.write(self.output.directory/(label+'-actual-gauge-rhs.json'), details)
        return rhs, details

    def initial(self):
        E, original = self.kernel, self.original
        cut = E.decoded_array(original.raw('cut-residual'), self.M, 'original complete cut residual')
        stages = E.decoded_array(original.raw('stage-residuals'), self.D*self.K,
                                 'original complete stage residuals')
        far = E.decoded_array(original.raw('end-residual'), self.M, 'original complete far residual')
        def blocks():
            yield 'cut', 0, cut
            for n in range(self.D):
                yield 'stage', n, stages[n*self.K:(n+1)*self.K]
            yield 'far', self.D, far
        return self.build(blocks(), 'initial', dict(
            kind='unchanged-original1372-base-residuals',
            cut_sha256=hashlib.sha256(original.raw('cut-residual')).hexdigest(),
            stages_sha256=hashlib.sha256(original.raw('stage-residuals')).hexdigest(),
            far_sha256=hashlib.sha256(original.raw('end-residual')).hexdigest()))

    def from_exact_ledger(self, descriptor, direction_sha, iteration):
        path = self.B.safe_file(self.output.directory, descriptor['file'])
        self.B.same(path.stat().st_size, descriptor['bytes'], 'complete original exact ledger size')
        self.B.same(sha(path), descriptor['sha256'], 'complete original exact ledger bytes')
        def blocks():
            with gzip.open(path, 'rt') as stream:
                for line in stream:
                    item = json.loads(line)
                    kind, node = item['kind'], item['node']
                    self.B.same(item['direction_float64le_sha256'], direction_sha,
                                'same original-coordinate direction in exact ledger')
                    start = 0 if kind == 'cut' else self.M+node*self.K
                    self.B.same(item['first_global_equation_row'], start, 'original equation row order')
                    if kind == 'stage':
                        self.B.same(item['original_J_stage_sha256'],
                                    self.original.J_rows[node]['raw_sha256'],
                                    'exact ledger still uses the original untransformed J')
                    yield kind, node, [(int(a, 16), int(e)) for a, e in item['all_exact_unscaled_rows']]
        return self.build(blocks(), f'iteration-{iteration:02d}',
                          dict(kind='complete-original-exact-ledger', file=descriptor,
                               original_delta_sha256=direction_sha))


def zip_strict(left, right):
    sentinel = object()
    a, b = iter(left), iter(right)
    while True:
        x, y = next(a, sentinel), next(b, sentinel)
        if x is sentinel and y is sentinel:
            return
        if x is sentinel or y is sentinel:
            raise ValueError('Incomplete or excess original exact row blocks')
        yield x, y


def checkpoint(B, output, original, gauge, delta, source_sha, name, restricted=False):
    row_data = [dict(node=n, state=row.tolist(),
                     negative_zero_columns=np.flatnonzero((row == 0)&np.signbit(row)).tolist())
                for n, row in enumerate(delta)]
    schema = ('complete-original577-restriction-of-gauge1372-direction-v1' if restricted
              else 'complete-original1372-direction-from-saved-node-gauge-v1')
    return B.write(output.directory/name, dict(
        schema=schema, source_sha256=source_sha,
        original_input_binding=original.binding,
        gauge_binding_file=gauge.binding_file,
        gauge_matrix_identity_sha256=gauge.binding['formed_matrix_identity_sha256'],
        coordinate_identity_sha256=gauge.coefficient_identity,
        original1372_matrix_identity_sha256=original.binding['new_matrix_identity_sha256'],
        scaling=SCALING, M=original.M, K=original.K,
        depth=original.original_depth if restricted else original.depth,
        original_depth=original.original_depth, step_depth=original.depth,
        old_to_new=original.old_to_new, restricted_to_original_nodes=restricted,
        delta_float64le_sha256=hashlib.sha256(B.float_bytes(delta)).hexdigest(),
        rows=row_data, actual_coordinates_are_original_Q_Pi=True,
        original_nonlinear_readback_required=True, old_long_J_defect_is_not_a_gate=True,
        no_native_solve=True, no_nonlinear_trial=True,
        native_accepted=False, task_completed=False), compressed=True)


def public_norm(kernel, record):
    return None if record is None else kernel.public_record(record)


def small_summary(report, result_file):
    return dict(
        schema='native-gauge-original1372-band-summary-v1',
        source_sha256=report['source_sha256'],
        gauge_source_sha256=GAUGE_SHA, original_adapter_sha256=report.get('original_adapter_sha256'),
        original1372_matrix_identity_sha256=report.get('original1372_matrix_identity_sha256'),
        formed_gauge_matrix_identity_sha256=report.get('formed_gauge_matrix_identity_sha256'),
        coordinate_identity_sha256=report.get('coordinate_identity_sha256'),
        actual_step_result_sha256=report['actual_step_result_sha256'],
        modes=112, shape_dimension=224, original_depth=576, step_depth=1372,
        diagnostic_completed=report['diagnostic_completed'],
        linear_direction_computed=report['linear_direction_computed'],
        best_iteration=report.get('best_iteration'),
        best_exact_original1372_sigma_norm=report.get('best_exact_original1372_sigma_norm'),
        iteration_original_exact_norms=[
            dict(iteration=h['iteration'], norm=h['exact_original1372_residual']['exact_global_original_sigma_norm'],
                 strictly_improved=h['strictly_improved_original1372_sigma_norm'],
                 complete_original_rows=h['exact_original1372_residual']['exact_rows'],
                 delta=h['delta'], checkpoint=h['direction_checkpoint'],
                 exact_ledger=h['exact_original1372_residual']['all_exact_residual_rows'])
            for h in report['refinement_history']],
        refinement_stop_reason=report.get('refinement_stop_reason'),
        step_delta=report.get('step_delta'),
        step_direction_checkpoint=report.get('step_direction_checkpoint'),
        restricted_old_node_delta=report.get('restricted_old_node_delta'),
        restricted_direction_checkpoint=report.get('restricted_direction_checkpoint'),
        lapack_factor_info=report.get('lapack_factor_info'),
        factorization_seconds=report.get('factorization_seconds'),
        LU_shares_input_storage=report.get('LU_shares_input_storage'),
        band_bytes=report.get('band_bytes'),
        memory_budget=report.get('memory_budget'),
        gauge_formation_summary=report.get('gauge_formation_summary'),
        final_array_manifest=report.get('array_manifest'), full_result=result_file,
        elapsed_seconds=report['elapsed_seconds'], maximum_RSS_kib=report['maximum_RSS_kib'],
        actual_error=report.get('actual_error'),
        failure_traceback_file=report.get('failure_traceback_file'),
        original_native_calls=0, new_J_calls=0, new_ODE_steps=0, nonlinear_trials=0,
        exact_residual_is_for_saved_original_arrays_not_exact_nonlinear_DF=True,
        no_transformed_norm_substituted_for_original_sigma_norm=True,
        no_new_scientific_acceptance_gate=True, native_accepted=False, task_completed=False)


def main():
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or
            os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('This offline finite-system computation runs only in the public repository Actions')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--capture-directory', type=Path, required=True)
    parser.add_argument('--step-directory', type=Path, required=True)
    parser.add_argument('--step-result-sha256', required=True)
    parser.add_argument('--expected-original-matrix-sha256', required=True)
    parser.add_argument('--equilibration-passes', type=int, default=3)
    parser.add_argument('--refinement-steps', type=int, default=3)
    parser.add_argument('--exact-workers', type=int, default=2)
    parser.add_argument('--max-band-bytes', type=int, default=4*1024**3)
    parser.add_argument('--max-transformed-j-bytes', type=int, default=512*1024**2)
    parser.add_argument('--out', type=Path, required=True)
    a = parser.parse_args()
    if (not 0 <= a.equilibration_passes <= 8 or not 0 <= a.refinement_steps <= 8 or
            not 1 <= a.exact_workers <= 4 or a.max_band_bytes <= 0 or a.max_transformed_j_bytes <= 0):
        raise ValueError('Explicit bounded work and complete-array resource budgets are required')
    a.out = a.out.resolve()
    if (a.out.exists() or a.out.is_relative_to(a.capture_directory.resolve()) or
            a.out.is_relative_to(a.step_directory.resolve())):
        raise ValueError('Use a new independent output directory')
    a.out.mkdir(parents=True)
    started = time.monotonic()
    source_sha = sha(__file__)
    output = None
    B = None
    report = dict(
        schema='native-gauge-original1372-equilibrated-band-correction-v1',
        source_sha256=source_sha, gauge_source_sha256=GAUGE_SHA,
        equilibration_source_sha256=EQUIL_SHA, old_driver_utilities_sha256=STEP_DRIVER_SHA,
        actual_step_result_sha256=a.step_result_sha256,
        expected_original_matrix_sha256=a.expected_original_matrix_sha256,
        scaling=SCALING, diagnostic_completed=False, linear_direction_computed=False,
        refinement_history=[], requested_equilibration_passes=a.equilibration_passes,
        requested_refinement_steps=a.refinement_steps, exact_workers=a.exact_workers,
        original_native_calls=0, new_J_calls=0, new_ODE_steps=0, nonlinear_trials=0,
        scientific_acceptance_unchanged=True, native_accepted=False, task_completed=False,
        NumPy=np.__version__, SciPy=scipy.__version__,
        BLAS_threads={key:os.environ.get(key) for key in
                      ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS')})
    try:
        G = load_pinned(GAUGE_NAME, GAUGE_SHA)
        Q = load_pinned(EQUIL_NAME, EQUIL_SHA)
        S = load_pinned(STEP_DRIVER_NAME, STEP_DRIVER_SHA)
        A = G.load_adapter()
        B = A.load_binding()
        kernel = Q.exact_module()
        report['exact_depth_independent_kernel_sha256'] = Q.EXACT_SHA
        report['original_binding_helper_sha256'] = A.BAND_SHA
        report['original_capture_result_sha256'] = A.CAPTURE_SHA
        B.same(a.step_result_sha256, G.STEP_RESULT_SHA, 'actual41 result argument')
        B.same(a.expected_original_matrix_sha256, G.ORIGINAL_MATRIX_SHA,
               'actual42 original matrix argument')
        original = A.RawCell0StepSystem(a.capture_directory, a.step_directory,
                                       a.step_result_sha256, B)
        B.same(original.binding['new_matrix_identity_sha256'], a.expected_original_matrix_sha256,
               'same original1372 complete finite matrix')
        report['original_adapter_sha256'] = G.ADAPTER_SHA
        report['original1372_matrix_identity_sha256'] = original.binding['new_matrix_identity_sha256']
        report['original_input_binding'] = B.write(a.out/'original-input-binding.json.gz',
                                                 original.binding, compressed=True)
        output = B.OutputArrays(a.out)
        report['memory_budget'] = S.memory_contract(original, a.max_band_bytes, a.exact_workers)
        report['memory_budget'].update(
            transformed_J_disk_budget_bytes=a.max_transformed_j_bytes,
            transformed_J_is_streamed_one_full_block_at_a_time=True,
            longdouble_work_is_block_local=True)
        if report['memory_budget']['band_bytes'] > a.max_band_bytes:
            raise MemoryError('The full required band exceeds the declared resource budget; no dimensions are reduced')
        gauge = G.RawCell0GaugeSystem(original, output, a.max_transformed_j_bytes)
        report['gauge_formation_summary'] = dict(
            file='gauge-formation-summary.json', bytes=(a.out/'gauge-formation-summary.json').stat().st_size,
            sha256=sha(a.out/'gauge-formation-summary.json'))
        report['formed_gauge_matrix_identity_sha256'] = gauge.binding['formed_matrix_identity_sha256']
        report['coordinate_identity_sha256'] = gauge.coefficient_identity
        report['original_bound_system_arrays'] = original.export_inputs(output)
        F = ScopedWriter(B, original, gauge, source_sha, 'formed-binary64-gauge-matrix')
        O = ScopedWriter(B, original, gauge, source_sha, 'original1372-exact-residual-readback')
        rows, columns, equilibration = Q.choose_exponents(
            gauge, G.GaugeScaleContext(gauge, kernel), output, F, a.out, a.equilibration_passes)
        report['equilibration'] = F.annotate(equilibration)
        ab, kl, ku = Q.assemble(gauge, rows, columns, output, F, report)
        rhs_builder = ExactGaugeRightHandSide(original, gauge, kernel, Q, rows, output, B)
        initial_rhs, report['initial_rhs'] = rhs_builder.initial()
        M, K, D = original.M, original.K, original.depth
        # The frozen exact evaluator also emits a rounded auxiliary RHS. It
        # is never solved. At most224 products of finite binary64 numbers
        # have magnitude below2^2056; scale2^-2048 guarantees this diagnostic
        # cannot overflow. Its possible underflows cannot alter exact rows.
        auxiliary_rows = np.full((D+1)*K, AUXILIARY_ORIGINAL_RHS_EXPONENT, dtype=np.int64)
        report['auxiliary_original_evaluator_row_exponents'] = Q.save_integer(
            output, 'original-exact-evaluator-auxiliary-row-exponents', auxiliary_rows,
            'Unused diagnostic RHS only; all exact integer rows and original sigma comparisons are unaffected')
        evaluator = Q.ExactOriginalResidual(original, A.DynamicExactContext(original, kernel),
                                            O, output, auxiliary_rows, a.exact_workers)
        B.write(a.out/'pre-factor-scientific-inputs.json', dict(
            source_sha256=source_sha, original_matrix=report['original1372_matrix_identity_sha256'],
            formed_matrix=report['formed_gauge_matrix_identity_sha256'],
            coordinate_identity=gauge.coefficient_identity, initial_rhs=report['initial_rhs'],
            exact_readback_scope='all original1372 rows with original sigma',
            native_accepted=False))
        factor_start = time.monotonic()
        pointer = ab.__array_interface__['data'][0]
        lu, piv, info = Q.dgbtrf(ab, kl, ku, overwrite_ab=1)
        report.update(
            lapack_factor_info=int(info), factorization_seconds=time.monotonic()-factor_start,
            LU_shares_input_storage=bool(np.shares_memory(lu, ab)),
            LU_retains_input_pointer=pointer == lu.__array_interface__['data'][0],
            LU_Fortran_byte_sha256=hashlib.sha256(memoryview(lu.ravel(order='F')).cast('B')).hexdigest())
        report['memory_budget'].update(
            actual_LU_shares_input_storage=report['LU_shares_input_storage'],
            actual_LU_bytes=int(lu.nbytes),
            maximum_RSS_kib_after_factorization=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        del ab
        report['pivot_array'] = Q.save_integer(output, 'lapack-pivots', piv,
                                               'Complete saved-gauge system pivot vector')
        factor_summary = {key:report[key] for key in
            ('lapack_factor_info', 'factorization_seconds', 'LU_shares_input_storage',
             'LU_retains_input_pointer', 'LU_Fortran_byte_sha256', 'band_shape',
             'band_bytes', 'matrix_formation', 'formed_matrix_entry_scales',
             'pivot_array', 'memory_budget')}
        F.write(a.out/'factorization.json', factor_summary)
        if info < 0:
            raise RuntimeError('dgbtrf rejected argument '+str(-info))
        if info > 0:
            raise FloatingPointError('dgbtrf returned zero pivot '+str(info))

        def solve_rhs(rhs, label):
            before = time.monotonic()
            column = np.array(rhs[:, None], dtype=np.float64, order='F', copy=True)
            solved, status = Q.dgbtrs(lu, kl, ku, column, piv, overwrite_b=1)
            if status:
                raise RuntimeError('dgbtrs returned info='+str(status))
            if not np.isfinite(solved).all():
                raise FloatingPointError('The complete gauge solution is nonfinite')
            z = solved[:, 0]
            scaling = Q.ScalingLedger()
            xi = scaling.apply(z, columns, dict(kind='recover-saved-G-coordinates', label=label)).reshape(D+1, K)
            scaled_file = output.save(label+'-dyadically-scaled-gauge-direction', z.reshape(D+1, K),
                                      'All solved coordinates before column power-of-two recovery')
            xi_file = output.save(label+'-saved-G-coordinate-direction', xi,
                                  'All xi words before the explicit triangular original-coordinate recovery')
            recovered, recovery = gauge.restore(xi, label)
            detail = dict(
                label=label, lapack_solve_info=int(status), seconds=time.monotonic()-before,
                solved_scaled_direction=scaled_file, saved_G_direction=xi_file,
                column_recovery=scaling.report(), original_coordinate_recovery=recovery)
            B.write(a.out/(label+'-solve-and-recovery.json'), detail)
            return recovered, detail

        delta, report['initial_solve'] = solve_rhs(initial_rhs, 'initial')
        best = best_rhs = best_exact = best_iteration = None
        for iteration in range(a.refinement_steps+1):
            delta_file = output.save(f'iteration-{iteration:02d}-original1372-delta', delta,
                                    'Actual binary64 restored original Q/Pi coordinates')
            state = checkpoint(B, output, original, gauge, delta, source_sha,
                               f'gauge-original-direction-iteration-{iteration:02d}.json.gz')
            auxiliary_rhs, exact, exact_report = evaluator.evaluate(delta, iteration)
            del auxiliary_rhs
            direction_sha = hashlib.sha256(B.float_bytes(delta)).hexdigest()
            rhs_error = None
            try:
                rhs, rhs_report = rhs_builder.from_exact_ledger(
                    exact_report['all_exact_residual_rows'], direction_sha, iteration)
            except (OverflowError, FloatingPointError) as error:
                rhs = None
                rhs_error = repr(error)
                rhs_report = dict(actual_error=rhs_error, completed=False,
                    original_exact_readback_still_complete=True,
                    no_rhs_thresholding_or_mode_omission=True)
            improved = best is None or Q.exact_smaller(exact, best_exact)
            history = dict(
                iteration=iteration, delta=delta_file, direction_checkpoint=state,
                exact_original1372_residual=exact_report,
                actual_gauge_refinement_rhs=rhs_report,
                strictly_improved_original1372_sigma_norm=improved)
            report['refinement_history'].append(history)
            B.write(a.out/f'gauge-iteration-{iteration:02d}.json', history)
            if not improved:
                report['refinement_stop_reason'] = 'Original exact sigma norm did not strictly improve; retain the previous direction'
                break
            best, best_rhs, best_exact, best_iteration = delta.copy(), rhs, exact, iteration
            if exact['_integer'] == 0:
                report['refinement_stop_reason'] = 'All saved original linear row defects are exactly zero; no nonlinear acceptance is asserted'
                break
            if iteration == a.refinement_steps:
                report['refinement_stop_reason'] = 'Explicit finite refinement budget exhausted'
                break
            if rhs_error is not None:
                report['refinement_stop_reason'] = 'The exact saved-G residual cannot be represented as a finite scaled RHS; retain the complete read-back direction'
                break
            try:
                increment, correction_report = solve_rhs(best_rhs, f'refinement-{iteration+1:02d}')
            except (FloatingPointError, RuntimeError) as error:
                history['following_error_correction_failure'] = repr(error)
                report['refinement_stop_reason'] = 'The following correction solve failed; retain the complete read-back direction'
                break
            history['following_error_correction'] = correction_report
            output.save(f'refinement-{iteration+1:02d}-original1372-increment', increment,
                        'Original-coordinate recovery of the gauge correction for exact original e')
            with np.errstate(over='ignore', under='ignore', invalid='ignore'):
                candidate = best+increment
            if not np.isfinite(candidate).all():
                history['following_nonfinite_candidate'] = output.save(
                    f'iteration-{iteration+1:02d}-nonfinite-candidate', candidate,
                    'Actual rejected finite-arithmetic update; previous finite direction retained')
                report['refinement_stop_reason'] = 'The binary64 correction update became nonfinite'
                break
            if B.float_bytes(candidate) == B.float_bytes(best):
                report['refinement_stop_reason'] = 'The proposed complete binary64 update is byte-identical'
                break
            delta = candidate
        if best is None:
            raise RuntimeError('No complete original-coordinate direction was read back')
        report['best_iteration'] = best_iteration
        report['best_exact_original1372_sigma_norm'] = public_norm(kernel, best_exact)
        report['step_delta'] = output.save(
            'complete-original1372-gauge-produced-delta', best,
            'Complete original-coordinate direction selected only by original1372 exact sigma norm')
        report['step_direction_checkpoint'] = checkpoint(
            B, output, original, gauge, best, source_sha, 'gauge-original-direction-checkpoint.json.gz')
        restricted = np.array(best[np.asarray(original.old_to_new)], copy=True)
        report['restricted_old_node_delta'] = output.save(
            'complete-original577-restricted-delta', restricted,
            'Exact oldToNew row selection from full original-coordinate delta; no old576 solve claim')
        report['restricted_direction_checkpoint'] = checkpoint(
            B, output, original, gauge, restricted, source_sha,
            'gauge-restricted-original577-direction.json.gz', restricted=True)
        report['linear_direction_computed'] = True
        report['old576_long_matrix_diagnostic_not_computed'] = dict(
            reason='The existing actual42 result already distinguishes old long-J diagnostic from original1372 norm; no new optional diagnostic is needed here',
            used_as_acceptance_gate=False, original_nonlinear_trial_still_required=True)
        report['diagnostic_completed'] = True
    except Exception as error:
        report['actual_error'] = repr(error)
        trace = traceback.format_exc()
        path = a.out/'failure-traceback.txt'
        with path.open('x') as stream:
            stream.write(trace)
        report['failure_traceback_file'] = dict(file=path.name, bytes=path.stat().st_size, sha256=sha(path))
    finally:
        if B is None:
            # Pure output fallback only; the actual numerical helper import
            # failure is preserved without claiming a completed computation.
            def writer(path, value, compressed=False):
                raw = (json.dumps(value, ensure_ascii=False, allow_nan=False)+'\n').encode()
                if compressed:
                    raw = gzip.compress(raw, mtime=0)
                with Path(path).open('xb') as stream:
                    stream.write(raw)
                return dict(file=Path(path).name, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        else:
            writer = B.write
        if output is not None:
            report['array_manifest'] = writer(a.out/'output-array-manifest.json', dict(
                schema='native-gauge-original1372-output-arrays-v1',
                source_sha256=source_sha, gauge_source_sha256=GAUGE_SHA,
                original1372_matrix_identity_sha256=report.get('original1372_matrix_identity_sha256'),
                formed_gauge_matrix_identity_sha256=report.get('formed_gauge_matrix_identity_sha256'),
                arrays=output.entries, all_arrays_artifact_only=True,
                native_accepted=False, task_completed=False))
        report['elapsed_seconds'] = time.monotonic()-started
        report['maximum_RSS_kib'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        result_file = writer(a.out/'result.json.gz', report, compressed=True)
        summary = small_summary(report, result_file)
        raw = (json.dumps(summary, ensure_ascii=False, allow_nan=False)+'\n').encode()
        if len(raw) >= 90000:
            # Preserve complete science in full result; keep the guaranteed
            # small transport report, not a numerical size acceptance gate.
            summary['iteration_original_exact_norms'] = [
                {key:h[key] for key in ('iteration', 'norm', 'strictly_improved', 'complete_original_rows')}
                for h in summary['iteration_original_exact_norms']]
            summary['summary_receipt_references_reduced_for_text_transport'] = True
        raw = (json.dumps(summary, ensure_ascii=False, allow_nan=False)+'\n').encode()
        if len(raw) >= 90000:
            summary = {key:summary[key] for key in (
                'schema', 'source_sha256', 'gauge_source_sha256',
                'original1372_matrix_identity_sha256', 'formed_gauge_matrix_identity_sha256',
                'diagnostic_completed', 'linear_direction_computed', 'best_iteration',
                'best_exact_original1372_sigma_norm', 'full_result',
                'elapsed_seconds', 'maximum_RSS_kib', 'native_accepted', 'task_completed')}
            summary['all_iteration_details_and_receipts_in_full_result'] = True
        summary_file = writer(a.out/'summary.json', summary)
        print(json.dumps(dict(
            event='native_gauge_original1372_finished',
            diagnostic_completed=report['diagnostic_completed'],
            linear_direction_computed=report['linear_direction_computed'],
            best_original_sigma_norm=report.get('best_exact_original1372_sigma_norm'),
            summary=summary_file, native_accepted=False, task_completed=False)), flush=True)
    return 0 if report['diagnostic_completed'] else 2


if __name__ == '__main__':
    raise SystemExit(main())
