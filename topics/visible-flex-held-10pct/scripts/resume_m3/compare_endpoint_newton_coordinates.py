#!/usr/bin/env python3
"""Read-only comparison of one actual saved endpoint state's Newton matrix.

The failed checkpoint contains a physical quintic interpolant, not the exact
last solve_bvp cubic.  Its node values and inverse source chart reconstruct a
finite state; the recomputed RMS quantifies the replay.  The original accepted
tail call 2 supplies exactly the affine DN used by that failed inner problem.

The second linear system changes only coordinates for the parameter columns.
Both mapped steps are tested in the same original J.  No nonlinear step is
taken, no source core is replaced, and neither solve is an accepted BVP.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
from datetime import datetime, timezone
import gc
import gzip
import json
from pathlib import Path
import sys
import time
import numpy as np
from numpy.polynomial import Chebyshev
from scipy.integrate import _bvp
from scipy.interpolate import PPoly
from scipy.sparse import csc_matrix, hstack
from scipy.sparse.linalg import LinearOperator, onenormest, splu
from m3_raw_diagnostic_model import RawDiagnosticEnvironment, sha


def event(name, **kwargs):
    print(json.dumps(dict(event=name,
        utc=datetime.now(timezone.utc).isoformat(), **kwargs)), flush=True)


def parameter_matrix(probe, scales, q):
    """Old raw physical c=A*z; then old dimensionless dp=S*dnewp.

    P_j's coefficients of T_k, k>=2, determine A: subtracting U_0,U_1
    only changes degrees zero and one.  The recorded finite quadrature
    recurrence supplies a numerical invertible matrix, not a new core.
    """
    rec = probe['finite_recurrence']
    alpha, beta = rec['alpha'], rec['beta']
    M = len(scales) + 1
    if len(alpha) != M or len(beta) != M:
        raise ValueError('The coordinate recurrence order does not match the state')
    polys = [Chebyshev([rec['p0']])]
    for j in range(M):
        nxt = Chebyshev([-alpha[j], 1.]) * polys[j]
        if j:
            nxt -= beta[j-1] * polys[j-1]
        polys.append(nxt / beta[j])
    A = np.zeros((M-1, M-1))
    for j in range(2, M+1):
        A[:j-1, j-2] = polys[j].coef[2:]
    diagonal = np.diag(A)
    if (not np.isfinite(A).all() or not np.all(diagonal > 0.) or
            np.any(np.tril(A, -1) != 0.)):
        raise ArithmeticError('The proposed finite coordinate map is not triangular/invertible')
    new_scale = q*q
    S = np.eye(M)
    S[1:, 1:] = A * new_scale / scales[:, None]
    return S, dict(
        definition='c_raw=A*z; z=q_gauge^2*p_new; dp_old=S*dp_new. '
            'The profile delta parameter is unchanged. Only Newton parameter '
            'columns are transformed; the physical evaluator retains its original raw c.',
        finite_recurrence_source='A fixed numerical matrix from the already recorded '
            'W^2 coordinate screen; no claim of exact continuous recurrence coefficients.',
        new_uniform_physical_scale=new_scale,
        A=A.tolist(), S=S.tolist(),
        A_diagonal_min=float(diagonal.min()),
        A_diagonal_max=float(diagonal.max()),
        A_condition_2=float(np.linalg.cond(A)),
        S_condition_2=float(np.linalg.cond(S)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--coordinate-probe', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--estimate-iterations', type=int, default=5)
    args = parser.parse_args()
    started = time.monotonic()
    run = args.run.resolve()
    command = json.loads((run/'continuation-command.json').read_text())['command']
    def argument(key):
        return command[command.index('--'+key)+1]
    state_path = run/'seed.json.gz'
    record = json.loads(gzip.decompress(state_path.read_bytes()))
    if record['solver_success']:
        raise ValueError('This diagnostic is specifically the recorded failed endpoint')
    if record['config']['fixed_metric'] or record['core_round_settings']['homotopy'] != 1.:
        raise ValueError('Expected the nonfixed actual circle-endpoint design')
    source = Path(argument('source-topic'))
    bridge = Path(argument('short-bridge'))
    profile = json.loads(Path(argument('profile')).read_text())
    chart = json.loads(Path(argument('chart')).read_text())
    port_path = Path(argument('linear-port'))
    port = json.loads(port_path.read_text()); port['_sha256'] = sha(port_path)
    settings = record['core_round_settings']
    M, N = record['config']['modes'], record['config']['angular']
    env = RawDiagnosticEnvironment(source, bridge, chart, settings)
    obj = env.make(settings, profile, port, record['gauge_amplitude'], M, N,
                   False, record['warp_reference_q'])
    obj.pscale = np.asarray(record['central_correction_scales'])
    obj.bcweights = np.full(M, record['config']['physical_bc_tol']/record['config']['bc_tol'])
    par = np.asarray(record['parameters'])
    obj.initial(par)
    f = obj.flow(par[0])
    if profile['delta'] + par[0] != record['frozen_profile']['delta']:
        raise ValueError('The original profile delta was not reconstructed exactly')
    from curve_stable_prefix_bvp import load_checkpoint
    decoded = load_checkpoint(state_path)
    physical = np.asarray(decoded['mesh'])
    pp = PPoly.construct_fast(np.asarray(decoded['pp_coefficients']), physical,
                             extrapolate=False, axis=1)
    x = obj.inverse_chart(physical, par[0])
    y = pp(physical)
    h = np.diff(x)
    if not np.all(h > 0.):
        raise ValueError('The reconstructed source chart is not increasing')
    chart_error = float(abs(obj.chart(x, par[0])[0]-physical).max())
    tail_path = run/'seed_tail_0002.json.gz'
    tail = json.loads(gzip.decompress(tail_path.read_bytes()))
    if not tail['response']['converged']:
        raise ValueError('The recorded inner problem lacks an accepted true-tail anchor')
    obj.tail = env.coupler.AffineTailForInnerBVP(
        tail['request']['height'], tail['response'], M)
    n, m, k = obj.n, len(x), len(par)
    col_fun, jac = _bvp.prepare_sys(n, m, k, obj.fun, obj.bc,
                                   obj.fun_jac, obj.bc_jac, x, h)
    event('reconstructed_state', n=n, nodes=m, parameters=k, chart_error=chart_error)
    col, mid, rhs, rhs_mid = col_fun(y, par)
    bc = obj.bc(y[:,0], y[:,-1], par)
    residual = np.r_[col.ravel(order='F'), bc]
    spline = _bvp.create_spline(y, rhs, x, h)
    rms = _bvp.estimate_rms_residuals(obj.fun, spline, x, h, par,
                                       1.5*col/h, rhs_mid)
    replay = dict(recorded_max_rms=record['max_rms_collocation_residual'],
        reconstructed_max_rms=float(rms.max()),
        max_rms_difference=float(abs(rms.max()-record['max_rms_collocation_residual'])),
        original_residual_max=float(abs(residual).max()),
        original_bc_max=float(abs(bc).max()),
        physical_chart_reconstruction_error=chart_error,
        provenance='The quintic stores the original left-node y values. Its last endpoint '
            'is evaluated from the final quintic, and physical mesh nodes are inverted through '
            'the original chart. This is not asserted bitwise identical to the lost raw final '
            'solve_bvp cubic or its last Newton Jacobian.')
    event('matrix_build_start', **replay)
    build_start = time.monotonic()
    J = jac(y, par, mid, rhs, rhs_mid, bc)
    J.sort_indices()
    build_seconds = time.monotonic() - build_start
    if not np.isfinite(J.data).all():
        raise ArithmeticError('The original Jacobian contains a nonfinite entry')
    event('matrix_ready', shape=list(J.shape), nnz=J.nnz, seconds=build_seconds)
    probe = json.loads(args.coordinate_probe.read_text())
    if (probe['n'] != 3 or probe['modes'] != M or
            probe['halfwidth'] != settings['halfwidth'] or
            probe['control_transition'] != settings['control_transition'] or
            probe['center'] != settings['center']):
        raise ValueError('The coordinate screen has different supported-window parameters')
    S, coordinate = parameter_matrix(probe, obj.pscale, obj.q)
    nf = n*m
    original_parameter = J[:,nf:].toarray()
    transformed_parameter = original_parameter @ S
    J_original_abs = abs(J)
    original_norm = float(J_original_abs.sum(axis=0).max())
    results = {}
    original_step = None
    for name in ('original', 'fixed_parameter_right_coordinates'):
        active = J if name == 'original' else hstack(
            (J[:,:nf], csc_matrix(transformed_parameter)), format='csc')
        factor_start = time.monotonic()
        event('factor_start', variant=name, nnz=active.nnz)
        LU = splu(active)
        factor_seconds = time.monotonic()-factor_start
        local_step = LU.solve(residual)
        mapped = local_step.copy()
        if name != 'original':
            mapped[nf:] = S @ local_step[nf:]
        error = J @ mapped - residual
        denominator = J_original_abs @ abs(mapped) + abs(residual)
        relative_backward = float(np.max(abs(error)/np.maximum(denominator, np.finfo(float).tiny)))
        # onenormest is a numerical lower estimate of ||A^-1||_1, not a certificate.
        inverse = LinearOperator(active.shape, dtype=np.dtype(float),
            matvec=lambda z: LU.solve(z), rmatvec=lambda z: LU.solve(z, trans='T'),
            matmat=lambda z: LU.solve(z), rmatmat=lambda z: LU.solve(z, trans='T'))
        np.random.seed(20261118)
        estimate_start = time.monotonic()
        inverse_estimate = float(onenormest(inverse, t=2, itmax=args.estimate_iterations))
        matrix_norm = original_norm if name == 'original' else float(abs(active).sum(axis=0).max())
        row = dict(factor_seconds=factor_seconds,
            lu_nnz=int(LU.L.nnz+LU.U.nnz),
            matrix_1_norm=matrix_norm,
            inverse_1_norm_estimate=inverse_estimate,
            condition_1_estimate=matrix_norm*inverse_estimate,
            condition_estimate_seconds=time.monotonic()-estimate_start,
            mapped_original_linear_residual_max=float(abs(error).max()),
            mapped_original_linear_residual_relative=float(abs(error).max()/abs(residual).max()),
            mapped_original_componentwise_backward_error=relative_backward,
            mapped_original_step_max=float(abs(mapped).max()),
            mapped_original_field_step_max=float(abs(mapped[:nf]).max()),
            mapped_original_parameter_step=mapped[nf:].tolist(),
            mapped_physical_control_step=(obj.pscale*mapped[nf+1:]).tolist(),
            original_coordinate_merit_norm_squared=float(np.dot(mapped,mapped)))
        if original_step is None:
            original_step = mapped.copy()
        else:
            difference = mapped-original_step
            row.update(mapped_step_difference_max=float(abs(difference).max()),
                mapped_field_step_difference_max=float(abs(difference[:nf]).max()),
                mapped_field_step_relative_difference=float(abs(difference[:nf]).max()/abs(original_step[:nf]).max()),
                mapped_physical_control_step_difference_max=float(abs(obj.pscale*difference[nf+1:]).max()))
        results[name] = row
        event('linear_comparison', variant=name, **row)
        del inverse, LU, local_step, mapped, error, denominator
        if name != 'original':
            del active
        gc.collect()
    output = dict(scope=__doc__, command=sys.argv, run=str(run),
        failed_input=dict(path=str(state_path),sha256=sha(state_path),
            solver_success=record['solver_success']),
        failed_chunks=[dict(path=str(z),sha256=sha(z)) for z in sorted(run.glob('seed_coeff_*.npy.gz'))],
        affine_tail=dict(path=str(tail_path),sha256=sha(tail_path)),
        coordinate_probe=dict(path=str(args.coordinate_probe.resolve()),sha256=sha(args.coordinate_probe)),
        settings=settings,physical_profile=record['frozen_profile'],
        q_gauge=obj.q,actual_q=obj.support_amplitude,parameters=par.tolist(),
        original_control_scales=obj.pscale.tolist(),replay=replay,
        matrix=dict(shape=list(J.shape),nnz=J.nnz,build_seconds=build_seconds,
                    radial_nodes=m,angular=N),
        parameter_coordinate=coordinate,comparisons=results,
        source_sha256={**env.sources,str(Path(__file__).resolve()):sha(__file__)},
        seconds=time.monotonic()-started,
        interpretation='This is one reconstructed failed finite state. Condition numbers are '
            'numerical one-norm estimates, not strict bounds. A coordinate improvement does not '
            'establish a nonlinear basin, overcome the observed domain/merit rejections, fix '
            'the initializer, or produce an accepted endpoint. All residual comparisons use '
            'the original Jacobian and original unknowns; no physical equations or gates changed.')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(output,indent=2)+'\n')
    event('finished', output=str(args.out), seconds=output['seconds'])


if __name__ == '__main__':
    main()
