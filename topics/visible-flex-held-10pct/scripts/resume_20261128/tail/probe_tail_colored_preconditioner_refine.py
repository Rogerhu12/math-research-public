#!/usr/bin/env python3
"""Probe colored preconditioning with complete true-residual correction rounds.

Every seed contains all columns of one Fourier color in Q or Pi separately.
Recovering a near-band entry includes all distant same-color contributions;
the resulting P is explicitly approximate, not the exact band of J. The
operator and final residual retain every actual stored J entry, all shooting
unknowns, and every boundary row. The complete saved A is applied in long-double before conversion to the GMRES vector dtype. No native JVP or nonlinear acceptance occurs.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import json
from pathlib import Path
import resource
import time

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import LinearOperator, gmres, splu

from tail_full_state_tangent_predictor import load, ref, module, read_packet


def verified(item):
    if ref(item['path']) != item:
        raise ValueError('Recorded input identity changed: ' + item['path'])
    return Path(item['path'])


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--predictor-summary', type=Path, required=True)
    p.add_argument('--outdir', type=Path, required=True)
    p.add_argument('--bandwidth', type=int, default=4)
    p.add_argument('--max-restart-cycles', type=int, default=3)
    a = p.parse_args()
    out = a.outdir.resolve(); out.mkdir(parents=True, exist_ok=False)
    source = load(a.predictor_summary)
    packet = read_packet(verified(source['accepted_source_packet']))
    record = load(verified(source['actual_fresh_native_record']))
    bg = load(verified(source['original_scaling']))
    M, K, L = bg['M'], bg['K'], bg['depth']; n = (L+1)*K
    if not 0 <= a.bandwidth < M:
        raise ValueError('Declare a finite band containing every mode diagonal')
    colors = 2*a.bandwidth+1; directions = 2*colors
    states = np.asarray(packet['response']['checkpoint']['states'])
    if states.shape != (L+1, K):
        raise ValueError('Complete original states are required')
    helper = module('_colored_preconditioner_wire', a.repo/'topics/visible-flex-held-10pct/scripts/resume_n4_tail/native_extended/parallel_native_batch.py')
    wire = verified(record['input']).read_bytes(); shape = helper.split_wire(wire)
    if (shape['modes'], shape['count'], shape['jac']) != (M, L, 1):
        raise ValueError('Complete actual last full J required')
    data = verified(record['output']).read_bytes()
    blocks, failed = helper.output_records(data, shape, L, shape['token'], 0)
    if failed is not None:
        raise ValueError('Complete successful original J required')
    J = np.empty((L, K, K)); flows = np.empty((L, K))
    for s, (start, end, status) in enumerate(blocks):
        values = np.frombuffer(data, dtype='<f8', count=(K+2)*(K+1), offset=start+8)
        flows[s] = values[:K]
        J[s] = values[K+2:].reshape(K+2, K)[:K]
        flows[s, M:] /= bg['portRatios'][s]
        J[s, M:] /= bg['portRatios'][s]
    sc = np.asarray(bg['scales']); ratio = sc[1:]/sc[:-1]; deep = np.asarray(bg['deepGraph'])
    b = np.empty((L+1, K)); b[:L] = (flows-states[:-1])/sc[:-1, None]
    b[L, :M] = (np.asarray(bg['desiredTarget'])-states[0, :M])/sc[0]
    b[L, M:] = -(states[-1, M:]-deep*states[-1, :M])/sc[-1]
    b = b.ravel(); bnorm = float(np.max(abs(b)))
    jl = J.astype(np.longdouble); rl = ratio.astype(np.longdouble); gl = deep.astype(np.longdouble)
    def matvec(v):
        v = np.asarray(v, np.longdouble).reshape(L+1, K); result = np.empty_like(v)
        result[:L] = v[:-1]-rl[:, None]*np.einsum('nij,nj->ni', jl, v[1:])
        result[L, :M] = v[0, :M]; result[L, M:] = v[-1, M:]-gl*v[-1, :M]
        return np.asarray(result.ravel(), float)
    def residual(z):
        v = np.asarray(z, np.longdouble).reshape(L+1, K); r = np.empty_like(v)
        r[:L] = v[:-1]-rl[:, None]*np.einsum('nij,nj->ni', jl, v[1:])
        r[L, :M] = v[0, :M]; r[L, M:] = v[-1, M:]-gl*v[-1, :M]
        return b.astype(np.longdouble)-r.ravel()
    Ainf = max(1., float(np.max(1+ratio[:, None]*np.sum(abs(J), axis=2))), float(np.max(1+abs(deep))))
    seed = np.zeros((K, directions))
    column_color = (np.arange(K)//M)*colors+(np.arange(K)%M)%colors
    seed[np.arange(K), column_color] = 1.
    started = time.monotonic()
    products = np.einsum('nij,jc->nic', J, seed)
    product_seconds = time.monotonic()-started
    ri, ci = np.indices((K, K)); keep = np.abs(ri % M-ci % M) <= a.bandwidth
    ii, jj = ri[keep], ci[keep]
    approximate = products[:, ii, column_color[jj]]
    exact_band = J[:, ii, jj]
    alias = approximate-exact_band
    maximum_alias = float(np.max(abs(alias)))
    relative_alias = maximum_alias/float(np.max(abs(exact_band)))
    del exact_band, alias
    rows = []; cols = []; values = []
    for s in range(L):
        rows.extend((s*K+np.arange(K)).tolist()); cols.extend((s*K+np.arange(K)).tolist()); values.extend([1.]*K)
        rows.extend((s*K+ii).tolist()); cols.extend(((s+1)*K+jj).tolist()); values.extend((-ratio[s]*approximate[s]).tolist())
    for j in range(M):
        rows.extend([L*K+j, L*K+M+j, L*K+M+j]); cols.extend([j, L*K+M+j, L*K+j]); values.extend([1., 1., -deep[j]])
    P = coo_matrix((values, (rows, cols)), shape=(n, n)).tocsc(); P.eliminate_zeros()
    del rows, cols, values, approximate
    started = time.monotonic()
    lu = splu(P, permc_spec='COLAMD', diag_pivot_thresh=1., options={'Equil': True})
    factor_seconds = time.monotonic()-started
    calls = 0; history = []
    def operator(v):
        nonlocal calls
        calls += 1
        return matvec(lu.solve(v))
    A = LinearOperator((n, n), matvec=operator, dtype=float)
    started = time.monotonic()
    y, info = gmres(A, b, rtol=1e-8, atol=0., restart=40, maxiter=a.max_restart_cycles,
                   callback=lambda r: history.append(float(r)), callback_type='pr_norm')
    z = lu.solve(y); gmres_seconds = time.monotonic()-started
    initial_actual_residual = float(np.max(abs(residual(z))))
    refinement_rows = []
    for refinement in range(3):
        true_rhs = residual(z)
        if float(np.max(abs(true_rhs))) <= 1e-8*bnorm:
            break
        local_history = []; prior_calls = calls; started = time.monotonic()
        dy, local_info = gmres(A, np.asarray(true_rhs, float), rtol=1e-8, atol=0.,
            restart=40, maxiter=a.max_restart_cycles,
            callback=lambda r: local_history.append(float(r)), callback_type='pr_norm')
        correction = lu.solve(dy)
        trial = np.asarray(z.astype(np.longdouble)+correction.astype(np.longdouble), float)
        trial_error = float(np.max(abs(residual(trial))))
        row = dict(refinement=refinement+1, rhs_linf=float(np.max(abs(true_rhs))),
            gmres_info=int(local_info), inner_iterations=len(local_history),
            full_A_products=calls-prior_calls, wall_seconds=time.monotonic()-started,
            final_true_residual_linf=trial_error,
            residual_history_first=local_history[:3], residual_history_last=local_history[-3:])
        refinement_rows.append(row)
        if trial_error >= float(np.max(abs(true_rhs))):
            row['retained_previous_better_solution'] = True
            break
        z = trial
    rr = residual(z); maximum = float(np.max(abs(rr)))
    normwise = maximum/(Ainf*float(np.max(abs(z)))+bnorm)
    report = dict(scope=__doc__, source=ref(__file__), predictor_summary=ref(a.predictor_summary),
        actual_native_record=source['actual_fresh_native_record'], accepted_source_packet=source['accepted_source_packet'],
        M=M, stages=L, unknowns=n, bandwidth=a.bandwidth, colors_per_field=colors,
        full_seed_directions=directions, seed_entries='1 in each same-color mode of exactly one of Q/Pi; no missing modes',
        maximum_column_count_per_color=int(np.max(np.sum(seed, axis=0))),
        approximate_P_includes_far_mode_aliasing=True, exact_band_of_J_claimed=False,
        maximum_alias_error_from_exact_band=maximum_alias,
        maximum_alias_relative_to_maximum_exact_band_entry=relative_alias,
        simulated_full_direction_product_seconds=product_seconds,
        P_nnz=int(P.nnz), LU_nnz=int(lu.L.nnz+lu.U.nnz), factor_seconds=factor_seconds,
        gmres_seconds=gmres_seconds, gmres_info=int(info), inner_iterations=len(history),
        initial_longdouble_residual_linf=initial_actual_residual,
        true_residual_refinement_rows=refinement_rows,
        overall_true_rhs_relative_gate_passed=maximum/bnorm<=1e-8,
        all_actual_matrix_products=calls, rtol=1e-8, restart=40, max_restart_cycles=a.max_restart_cycles,
        residual_history_first=history[:5], residual_history_last=history[-5:],
        final_original_longdouble_residual_linf=maximum,
        relative_rhs_residual_linf=maximum/bnorm,
        original_normwise_backward_error=normwise, original_backward_error_gate_passed=normwise<1e-11,
        actual_A_all_entries_retained=True, all_boundary_rows_retained=True,
        actual_A_matvec_precision='np.longdouble accumulated then binary64 GMRES vector',
        native_JVP_implemented=False, nonlinear_solve_invoked=False, predictor_accepted=False,
        resource_peak_self_maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        complete_surface=False)
    (out/'summary.json').write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(report, indent=2, allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
