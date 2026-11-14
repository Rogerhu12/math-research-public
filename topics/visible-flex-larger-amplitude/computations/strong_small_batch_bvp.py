#!/usr/bin/env python3
"""Explicit smaller radial batches around the accepted-iterate BVP wrapper.

The original radial and collocation function bodies stay unchanged. Only
their optional batch-size defaults change in this fresh process. An immutable
configuration record is included in every iterate's source hash map and in
the final design provenance. The optional real-state inspection does not
take a Newton step or produce a nonlinear solution.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import gc
import hashlib
import inspect
import json
from pathlib import Path
import sys
import time
import numpy as np
import scipy.integrate as integrate
import root_radial_batching as radial
import root_block_collocation as blocks
import strong_checkpointed_tangent_bvp as checkpointed

HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def comparison(a, b):
    a, b = np.asarray(a), np.asarray(b)
    if a.shape != b.shape or not np.isfinite(a).all() or not np.isfinite(b).all():
        raise ValueError('Invalid batching comparison arrays')
    difference = abs(a-b)
    maximum = float(np.max(difference, initial=0.))
    normalized = float(np.max(difference/np.maximum(1., abs(a)), initial=0.))
    # This is a numerical implementation comparison, not a certified error.
    return dict(shape=list(a.shape), bitwise_equal=bool(np.array_equal(a, b)),
                max_abs_difference=maximum, max_component_normalized_difference=normalized,
                worst_abs_index=list(map(int, np.unravel_index(np.argmax(difference), difference.shape)))
                    if difference.size else None,
                numerical_agreement=normalized <= 2e-10)


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--radial-batch-size', type=int, required=True)
    parser.add_argument('--collocation-batch-size', type=int, required=True)
    parser.add_argument('--batch-check-output', type=Path)
    opts, remaining = parser.parse_known_args()
    if not 1 <= opts.radial_batch_size <= 48 or not 1 <= opts.collocation_batch_size <= 24:
        raise ValueError('This adapter only reduces the reviewed 48/24 batches')
    if '--out-prefix' not in remaining:
        raise ValueError('A fresh output prefix is required')
    prefix = Path(remaining[remaining.index('--out-prefix')+1])
    record_file = prefix.with_name(prefix.name+'-radial-batches.json')
    if record_file.exists() or (opts.batch_check_output and opts.batch_check_output.exists()):
        raise ValueError('Refusing to replace a batching configuration or check')
    functions = (radial.value, radial.state_jacobian, blocks.prepare_sys)
    old_defaults = tuple(f.__defaults__ for f in functions)
    if old_defaults != ((48,), (48,), (24,)):
        raise ValueError('Original radial/collocation defaults changed')
    for function in functions:
        if list(inspect.signature(function).parameters)[-1] != 'batch_size':
            raise ValueError('Unexpected batching function signature')
    hashes = {str(path): digest(path) for path in (
        Path(__file__), HERE/'root_radial_batching.py', HERE/'root_block_collocation.py',
        HERE/'strong_checkpointed_tangent_bvp.py')}
    configuration = dict(scope=__doc__, radial_batch_size=opts.radial_batch_size,
        collocation_interval_batch_size=opts.collocation_batch_size,
        original_radial_batch_size=48, original_collocation_interval_batch_size=24,
        function_bodies_changed=False, radial_point_formulas_changed=False,
        floating_order_identity_claimed=False,
        physical_data_or_acceptance_changed=False, source_sha256=hashes)
    temporary = record_file.with_name(record_file.name+'.tmp')
    temporary.write_text(json.dumps(configuration, indent=2)+'\n')
    temporary.replace(record_file)
    record = dict(file=str(record_file), sha256=digest(record_file), **configuration)

    def set_batches(radial_size, collocation_size):
        radial.value.__defaults__ = (radial_size,)
        radial.state_jacobian.__defaults__ = (radial_size,)
        blocks.prepare_sys.__defaults__ = (collocation_size,)

    set_batches(opts.radial_batch_size, opts.collocation_batch_size)
    OriginalRecorder = checkpointed.Recorder

    class BatchRecorder(OriginalRecorder):
        def __init__(self, prefix, source_hashes):
            super().__init__(prefix, {**source_hashes, **hashes,
                                     str(record_file): record['sha256']})

    checkpointed.Recorder = BatchRecorder
    original_solve = integrate.solve_bvp

    def solve(fun, bc, x, y, p, **kwargs):
        obj = fun.__self__
        obj.design_provenance['radial_batch_configuration'] = record
        if opts.batch_check_output is None:
            return original_solve(fun, bc, x, y, p, **kwargs)
        started = time.time()
        indices = np.unique(np.linspace(0, len(x)-1, 49).round().astype(int))
        xx, yy, pp = np.asarray(x)[indices], np.asarray(y)[:, indices], np.asarray(p).copy()
        hh, n, m, k = np.diff(xx), yy.shape[0], len(xx), len(pp)
        jac = kwargs['fun_jac']

        def collect(radial_size, collocation_size):
            set_batches(radial_size, collocation_size)
            obj.select(pp)
            rhs = fun(xx, yy, pp)
            state_jac, parameter_jac = jac(xx, yy, pp)
            gc.collect()
            operands = []
            for j, name in enumerate(obj.control_names):
                # The exact existing root_triple_core_bvp.py formula. These
                # extra evaluations are diagnostic only, never a new Jacobian.
                step = 1e-6*max(.1, abs(obj.cfg[name]+pp[j]))
                plus, minus = pp.copy(), pp.copy()
                plus[j] += step;minus[j] -= step
                fp, fm = fun(xx, yy, plus), fun(xx, yy, minus)
                fd = (fp-fm)/(2*step)
                operands.append(dict(column=j, name=name, step=step, plus=fp,
                    minus=fm, difference=fd,
                    actual_column_reproduced_bitwise=bool(np.array_equal(fd, parameter_jac[:, j, :]))))
                gc.collect()

            def bounded_jac(*args):
                try:
                    return jac(*args)
                finally:
                    gc.collect()

            col, sys_jac = blocks.prepare_sys(n, m, k, fun, bc, bounded_jac,
                kwargs['bc_jac'], xx, hh)
            col_values, middle, values, middle_values = col(yy, pp)
            boundary = bc(yy[:, 0], yy[:, -1], pp)
            matrix = sys_jac(yy, pp, middle, values, middle_values, boundary)
            return dict(rhs=rhs, state_jacobian=state_jac,
                parameter_jacobian=parameter_jac, collocation=col_values,
                midpoint_state=middle, midpoint_rhs=middle_values, boundary=boundary,
                block_a=matrix.a, block_b=matrix.b, block_p=matrix.c,
                boundary_a=matrix.boundary_a, boundary_b=matrix.boundary_b,
                boundary_p=matrix.boundary_p), operands

        print(json.dumps(dict(event='radial_batch_check_begin', modes=obj.M,
            angular=obj.nt, selected_nodes=m, parameter_count=k)), flush=True)
        baseline, baseline_fd = collect(48, 24)
        candidate, candidate_fd = collect(opts.radial_batch_size, opts.collocation_batch_size)
        checks = {key: comparison(baseline[key], candidate[key]) for key in baseline}
        fd_checks = []
        eps = np.finfo(float).eps
        for old, new in zip(baseline_fd, candidate_fd):
            if old['column'] != new['column'] or old['step'] != new['step']:
                raise RuntimeError('The parameter difference formula changed')
            j, h = old['column'], old['step']
            dplus, dminus = abs(new['plus']-old['plus']), abs(new['minus']-old['minus'])
            plus_scale = np.maximum(1., np.maximum(abs(new['plus']), abs(old['plus'])))
            minus_scale = np.maximum(1., np.maximum(abs(new['minus']), abs(old['minus'])))
            plus_units = float(np.max(dplus/plus_scale)/eps)
            minus_units = float(np.max(dminus/minus_scale)/eps)
            a, b = baseline['parameter_jacobian'][:, j, :], candidate['parameter_jacobian'][:, j, :]
            delta = abs(b-a)
            allowance = 8*eps*(np.maximum(1., abs(a))+np.maximum(1., abs(b)))
            bound = (dplus+dminus)/(2*h)+allowance
            reproduced = old['actual_column_reproduced_bitwise'] and new['actual_column_reproduced_bitwise']
            fd_checks.append(dict(column=j, control=old['name'], original_fd_step=h,
                plus_rhs=comparison(old['plus'], new['plus']),
                minus_rhs=comparison(old['minus'], new['minus']),
                max_plus_rhs_component_eps_units=plus_units,
                max_minus_rhs_component_eps_units=minus_units,
                baseline_actual_column_reproduced_bitwise=old['actual_column_reproduced_bitwise'],
                candidate_actual_column_reproduced_bitwise=new['actual_column_reproduced_bitwise'],
                max_jacobian_column_difference=float(np.max(delta)),
                max_operand_difference_bound=float(np.max(bound)),
                exceeds_operand_bound=bool(np.any(delta>bound)),
                passed=bool(reproduced and plus_units <= 128 and minus_units <= 128
                            and np.all(delta <= bound))))
        accepted = (all(v['numerical_agreement'] for key, v in checks.items()
                        if key != 'parameter_jacobian') and all(v['passed'] for v in fd_checks))
        obj.select(pp)
        report = dict(scope='One actual complete same-chart BVP state, restricted to 49 saved radial nodes. Compare independent radial batching of the real RHS, full state and physical-control Jacobian, and direct collocation blocks. No Newton/factorization/new solution.',
            inspection_only=True, nonlinear_solution=False, finished=True,
            all_compared_arrays_bitwise_equal=all(v['bitwise_equal'] for v in checks.values()),
            original_strict_array_gate_passed=all(v['numerical_agreement'] for v in checks.values()),
            numerical_agreement=accepted, comparisons=checks,
            finite_difference_operand_checks=fd_checks,
            comparison_gate='Every non-PJ array meets the original comparison threshold. Each actual PJ control column must be reproduced bitwise by the unchanged centered formula, each F+/F- operand changes by at most128 component eps units, and the PJ difference fits the observed operand difference divided by2h plus8eps arithmetic allowance. This changes no BVP residual or acceptance gate.',
            modes=obj.M,
            angular=obj.nt, original_nodes=len(x), selected_node_indices=indices.tolist(),
            selected_nodes=m, parameter_count=k, configuration=record,
            actual_profile=dict(obj.flow(pp[0]).cfg), reference_chart_coefficients=obj.ref_coeff.tolist(),
            reference_chart_frequencies=list(getattr(obj, 'ref_frequencies', [2, 4])),
            tangent_warm=getattr(obj, '_strong_tangent_info', None),
            seconds=time.time()-started)
        opts.batch_check_output.write_text(json.dumps(report, indent=2)+'\n')
        print(json.dumps(dict(event='radial_batch_check_completed', passed=accepted,
            bitwise_equal=report['all_compared_arrays_bitwise_equal'], seconds=report['seconds'])), flush=True)
        if not accepted:
            raise RuntimeError('Radial batching real-state comparison failed')
        raise RuntimeError('Radial batching inspection complete; no BVP requested')

    integrate.solve_bvp = solve
    sys.argv = [sys.argv[0]]+remaining
    try:
        checkpointed.main()
        if opts.batch_check_output:
            if not opts.batch_check_output.exists():
                raise RuntimeError('Batching inspection did not reach the real solver entry')
            result = json.loads(opts.batch_check_output.read_text())
            if not result.get('numerical_agreement'):
                raise RuntimeError('Batching inspection did not pass')
    finally:
        integrate.solve_bvp = original_solve
        checkpointed.Recorder = OriginalRecorder
        for function, defaults in zip(functions, old_defaults):
            function.__defaults__ = defaults


if __name__ == '__main__':
    main()
