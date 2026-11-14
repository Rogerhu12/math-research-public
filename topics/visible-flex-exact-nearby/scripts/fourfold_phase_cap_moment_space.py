#!/usr/bin/env python3
"""Reuse actual cap Fourier moments for primal/dual approximation spaces.

This is floating exploration. The boundary cutoff is kept fixed while the
interior angular or radial polynomial spaces change. One geometry pass saves
all B and B^-1 moments needed for P1/P2/P3, avoiding repeated 5400-point work.
The exact variational upper/lower identities are R88; no quadrature or native
coefficient error is certified by this numerical cache.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from numpy.polynomial import Polynomial
from numpy.polynomial.legendre import leggauss
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import splu

from fourfold_phase_cap_low_schur import ActualCapGeometry


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save_report(path, report, **arrays):
    path.parent.mkdir(parents=True, exist_ok=True)
    binary = path.with_suffix('.npz')
    np.savez_compressed(binary, **arrays)
    report['arrays'] = dict(path=str(binary), sha256=sha(binary), bytes=binary.stat().st_size)
    path.write_text(json.dumps(report, indent=2)+'\n')


def read_arrays(report):
    path = Path(report['arrays']['path'])
    if sha(path) != report['arrays']['sha256']:
        raise ValueError('saved floating moment/finite space arrays changed')
    with np.load(path, allow_pickle=False) as data:
        return {key:data[key].copy() for key in data.files}


def build(args):
    report = json.loads(args.primal.read_text())
    original = read_arrays(report)
    mesh = original['mesh']
    if sha(report['object_path']) != report['object_sha256']:
        raise ValueError('the actual cap object changed')
    if not 0 < args.max_lag < report['angular_nodes']//2:
        raise ValueError('retained moment frequencies exceed the original angle grid')
    geometry = ActualCapGeometry(report['object_path'], report['primitive_nodes'])
    exact_knots = {Fraction(float(x)) for key, values in geometry.base.frozen.items()
                   if key.endswith('_knots') for x in values}
    exact_knots |= {-x for x in exact_knots}
    lags = np.arange(-args.max_lag, args.max_lag+1)
    moments = np.zeros((len(mesh)-1, 2, 3, 7, len(lags)), complex)
    gx, gw = leggauss(report['radial_gauss_order'])
    calls, wall, cpu = 0, time.monotonic(), time.process_time()
    for cell, (left, right) in enumerate(zip(mesh, mesh[1:])):
        cuts = sorted({Fraction(float(left)), Fraction(float(right))}
                      |{q for q in exact_knots if left < q < right})
        for exact_left, exact_right in zip(cuts, cuts[1:]):
            a, b = float(exact_left), float(exact_right)
            h = float(exact_right-exact_left)
            if h <= 0:
                continue
            for radial, weight in zip((a+b)/2+h*gx/2, h*gw/2):
                aa, bb, cc, _, _ = geometry.coefficients(radial, report['angular_nodes'])
                determinant = aa*cc-bb*bb
                if np.min(determinant) <= 0:
                    raise ValueError('the sampled inverse form is not positive')
                values = np.asarray([aa, bb, cc, cc/determinant, -bb/determinant, aa/determinant])
                coefficients = np.fft.fft(values, axis=1)/report['angular_nodes']
                retained = coefficients[:, lags % report['angular_nodes']].reshape(2, 3, -1)
                t = (radial-left)/(right-left)
                powers = t**np.arange(7)
                moments[cell] += weight*retained[:, :, None, :]*powers[None, None, :, None]
                calls += 1
        if (cell+1) % 24 == 0:
            print(json.dumps(dict(progress='actual cap reusable moments', cells=cell+1,
                total=len(mesh)-1, coefficient_calls=calls)), flush=True)
    identity = {key:report[key] for key in ('object_path','object_sha256','exact_delta_fraction',
                 'origin_inputs_sha256','direction_sha256','physical_radial_interval',
                 'primitive_nodes','angular_nodes','radial_gauss_order')}
    answer = dict(kind='floating_actual_cap_full_Fourier_moments_for_primal_and_complementary_spaces',
        complete=True, rigorous_integrals=False, source_sha256=sha(__file__),
        source_dependency_sha256={'fourfold_phase_cap_low_schur.py':sha(Path(__file__).with_name('fourfold_phase_cap_low_schur.py'))},
        primal_report_path=str(args.primal), primal_report_sha256=sha(args.primal), **identity,
        max_lag=args.max_lag, max_radial_power=6, radial_elements=len(mesh)-1,
        coordinate='t=(r-left)/(right-left) separately on each saved FE element',
        moment_order=['cell','B or inverse B','11,12,22','radial power 0..6','Fourier lag'],
        exact_tail_input_sha256=report['actual_tail_input_sha256'],
        coefficient_calls=calls, CPU_seconds=time.process_time()-cpu, wall_seconds=time.monotonic()-wall,
        scope='Floating actual-geometry moments; exact infinite primitive, angular alias, quadrature and arithmetic fees remain separate.')
    save_report(args.out, answer, mesh=mesh, lags=lags, moments=moments)
    print(json.dumps(dict(complete=True, CPU_seconds=answer['CPU_seconds'],
        wall_seconds=answer['wall_seconds'], bytes=answer['arrays']['bytes'])), flush=True)


def shapes(degree):
    if degree not in (1, 2, 3):
        raise ValueError('this saved moment cache supports radial P1/P2/P3')
    # For these degrees the coefficients are dyadic, so the intended nodal
    # polynomials are represented exactly before radial-width division.
    answer = []
    for j in range(degree+1):
        coefficients = [Fraction(1)]
        node = Fraction(j, degree)
        for k in range(degree+1):
            if k == j:
                continue
            other = Fraction(k, degree)
            updated = [Fraction(0)]*(len(coefficients)+1)
            for q, value in enumerate(coefficients):
                updated[q] -= other*value/(node-other)
                updated[q+1] += value/(node-other)
            coefficients = updated
        answer.append(Polynomial([float(x) for x in coefficients]))
    return answer


def energy(local_moments, radial, angular):
    """Polynomial maps radial[t],angular[t] into the physical Fourier slots."""
    result = np.zeros((radial.shape[-1], radial.shape[-1]), complex)
    for p in range(radial.shape[0]):
        for q in range(radial.shape[0]):
            R, T, S, U = radial[p], angular[p], radial[q], angular[q]
            A, B, C = local_moments[:, p+q]
            result += R.conj().T@A@S+R.conj().T@B@U+T.conj().T@B@S+T.conj().T@C@U
    return result


def sparse_from_locals(locals_, dofs_, size, extra=()):
    rr, cc, vv = [], [], []
    for matrix, dofs in zip(locals_, dofs_):
        row, column = np.meshgrid(dofs, dofs, indexing='ij')
        rr.append(row.ravel()); cc.append(column.ravel()); vv.append(matrix.ravel())
    for index, value in extra:
        rr.append(np.array([index])); cc.append(np.array([index])); vv.append(np.array([value]))
    return coo_matrix((np.concatenate(vv), (np.concatenate(rr), np.concatenate(cc))),
                       shape=(size, size)).tocsc()


def solve(args):
    from flint import ctx
    from fourfold_phase_finite_tail_DN import finite_tail_entries
    report = json.loads(args.cache.read_text())
    data = read_arrays(report)
    if not report['complete'] or 2*args.interior_modes > report['max_lag']:
        raise ValueError('insufficient completed actual moment cache')
    if not 0 <= args.boundary_modes <= args.interior_modes:
        raise ValueError('boundary modes must be contained in the interior space')
    ctx.prec = 256
    tail = finite_tail_entries(Path('notes/2026-11-12-positive-family-natural-graft.json'),
        Path('notes/2026-11-12-actual-exterior-robin-certificate.json'),
        Path('notes/2026-11-12-common-core-exterior-parameter-interval.json'), args.interior_modes)
    if tail['input_sha256'] != report['exact_tail_input_sha256']:
        raise ValueError('the actual infinite-tail family changed')
    from flint import arb
    M, B, degree = args.interior_modes, args.boundary_modes, args.radial_degree
    shape = shapes(degree)
    frequencies = 4*np.arange(-M, M+1)
    n, nb = len(frequencies), 2*B+1
    mesh, raw = data['mesh'], data['moments']
    cells, radial_nodes = len(mesh)-1, degree*(len(mesh)-1)+1
    indices = np.arange(-M, M+1)
    lag = indices[:, None]-indices[None, :]+report['max_lag']
    nonzero = np.flatnonzero(frequencies); nn = len(nonzero)
    gamma = np.zeros(n)
    for j, frequency in enumerate(indices):
        if frequency:
            gamma[j] = float(arb(tail['entries'][abs(frequency)-1]['true_Robin']['ball']).mid())
    primal_local, primal_dofs, dual_local, dual_dofs = [], [], [], []
    pmean = radial_nodes*nn
    qmean_start = pmean+1
    dual_dimension = qmean_start+degree*cells
    D = np.diag(1j*frequencies)
    wall, cpu = time.monotonic(), time.process_time()
    for cell, h in enumerate(np.diff(mesh)):
        moments = raw[cell, :, :, :, lag]
        # NumPy advanced indices move the two Fourier axes to the front.
        moments = np.moveaxis(moments, (0,1), (-2,-1))
        if moments.shape != (2,3,7,n,n):
            raise ValueError('unexpected moment Toeplitz shape')
        radial = np.zeros((degree+1,n,(degree+1)*n), complex)
        angular = np.zeros_like(radial)
        for local, poly in enumerate(shape):
            cols = slice(local*n,(local+1)*n)
            for power, value in enumerate(poly.coef):
                angular[power,:,cols] = value*D
            for power, value in enumerate(poly.deriv().coef):
                radial[power,:,cols] = value*np.eye(n)/h
        primal_local.append(energy(moments[0], radial, angular))
        primal_dofs.append((cell*degree+np.arange(degree+1))[:,None]*n+np.arange(n)[None,:])
        primal_dofs[-1] = primal_dofs[-1].ravel()
        nd = (degree+1)*nn+1+degree
        radial = np.zeros((degree+1,n,nd), complex)
        angular = np.zeros_like(radial)
        dofs = []
        for local, poly in enumerate(shape):
            cols = local*nn+np.arange(nn)
            dofs.extend(((cell*degree+local)*nn+np.arange(nn)).tolist())
            for power, value in enumerate(poly.coef):
                radial[power,nonzero,cols] = value
            for power, value in enumerate(poly.deriv().coef):
                angular[power,nonzero,cols] = -value/(h*1j*frequencies[nonzero])
        radial[0,M,(degree+1)*nn] = 1
        dofs.append(pmean)
        for power in range(degree):
            angular[power,M,(degree+1)*nn+1+power] = 1
            dofs.append(qmean_start+cell*degree+power)
        dual_local.append(energy(moments[1], radial, angular))
        dual_dofs.append(np.asarray(dofs))
    K = sparse_from_locals(primal_local, primal_dofs, radial_nodes*n,
        [(n*(radial_nodes-1)+j,gamma[j]) for j in nonzero])
    HD = sparse_from_locals(dual_local, dual_dofs, dual_dimension,
        [(nn*(radial_nodes-1)+j,1/gamma[nonzero[j]]) for j in range(nn)])
    fixed = np.r_[np.arange(n), n*(radial_nodes-1)+M]
    free = np.setdiff1d(np.arange(K.shape[0]),fixed)
    V = np.zeros((K.shape[0],nb+1),complex)
    selected = M-B+np.arange(nb)
    V[selected,np.arange(nb)] = 1
    V[-n+M,-1] = 1
    V[free] = splu(K[free][:,free]).solve(-(K[free][:,fixed]@V[fixed]))
    # Preserve the exact constant trial under the mean+xi input combination.
    constant = np.zeros(K.shape[0]); constant[np.arange(radial_nodes)*n+M] = 1
    V[:,-1] = constant-V[:,B]
    upper = V.conj().T@(K@V)
    load = np.zeros((dual_dimension,nb+1),complex)
    lookup = {int(mode):j for j,mode in enumerate(nonzero)}
    for column, index in enumerate(selected):
        if index != M:
            load[lookup[int(index)],column] = -1
    load[pmean,B],load[pmean,-1] = -1,1
    flux = splu(HD).solve(load)
    flux[:,-1] = -flux[:,B]
    lower = load.conj().T@flux+flux.conj().T@load-flux.conj().T@(HD@flux)
    upper=(upper+upper.conj().T)/2;lower=(lower+lower.conj().T)/2
    gap=upper-lower
    kernel=np.zeros(nb+1);kernel[B]=kernel[-1]=1
    answer=dict(kind='floating_cap_fixed_boundary_primal_dual_space_comparison',
        complete=True, rigorous_energy_bounds=False, source_sha256=sha(__file__),
        cache_report_path=str(args.cache), cache_report_sha256=sha(args.cache),
        object_sha256=report['object_sha256'],exact_delta_fraction=report['exact_delta_fraction'],
        boundary_modes=B,interior_modes=M,radial_polynomial_degree=degree,
        radial_elements=cells,primal_dimension=K.shape[0],dual_dimension=HD.shape[0],
        mean_slots_retained=True,finite_energy_gap_eigenvalues=np.linalg.eigvalsh(gap).tolist(),
        finite_energy_gap_norm=float(np.linalg.norm(gap,2)),
        upper_constant_kernel_residual=float(np.linalg.norm(upper@kernel)),
        lower_constant_kernel_residual=float(np.linalg.norm(lower@kernel)),
        source_and_quadrature_error_paid=False,
        CPU_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-wall,
        scope='Fixed physical boundary cutoff; only cap interior trial spaces changed. Exact variational identities apply after genuinely directed energy integration, not from this floating gap alone.')
    save_report(args.out,answer,upper_DN=upper,lower_DN=lower,energy_gap=gap,
        primal_trial=V,dual_flux=flux,mesh=mesh,frequencies=frequencies)
    print(json.dumps({key:answer[key] for key in ('boundary_modes','interior_modes','radial_polynomial_degree',
        'finite_energy_gap_norm','finite_energy_gap_eigenvalues','CPU_seconds','wall_seconds')},indent=2),flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    bp=sub.add_parser('build')
    bp.add_argument('--primal',type=Path,default=Path('notes/2026-11-12-actual-cap-low-Schur-M4.json'))
    bp.add_argument('--max-lag',type=int,default=32)
    bp.add_argument('--out',type=Path,required=True)
    sp=sub.add_parser('solve')
    sp.add_argument('--cache',type=Path,required=True)
    sp.add_argument('--interior-modes',type=int,required=True)
    sp.add_argument('--boundary-modes',type=int,default=4)
    sp.add_argument('--radial-degree',type=int,default=1)
    sp.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    (build if args.command=='build' else solve)(args)


if __name__=='__main__':
    main()
