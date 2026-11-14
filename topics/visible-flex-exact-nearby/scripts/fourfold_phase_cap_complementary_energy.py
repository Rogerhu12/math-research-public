#!/usr/bin/env python3
"""Complementary-energy finite lower candidate for the true positive cap.

The represented flux is exactly divergence free: p_k is continuous P1,
q_k=-p_k'/(4ik), k!=0, p_0 is globally constant and q_0 is cellwise constant.
For exact integrals this is a genuine lower bound for the full cap DN form,
including the regular mean slot. This runner uses floating quadrature and
tail midpoints and therefore records a candidate, not a directed certificate.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import cho_factor, cho_solve

from fourfold_phase_cap_low_schur import ActualCapGeometry


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--primal', type=Path, default=Path(
        'notes/2026-11-12-actual-cap-low-Schur-M4.json'))
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    primal = json.loads(args.primal.read_text())
    array_path = Path(primal['arrays']['path'])
    if not primal['complete'] or sha(array_path) != primal['arrays']['sha256']:
        raise ValueError('complete fixed primal finite cap data required')
    object_path = Path(primal['object_path'])
    if sha(object_path) != primal['object_sha256']:
        raise ValueError('actual cap graph changed')
    with np.load(array_path, allow_pickle=False) as saved:
        mesh = saved['mesh'].copy()
        upper = saved['augmented_DN'].copy()
        frequencies = saved['frequencies'].copy()
    modes, n = primal['modes'], len(frequencies)
    indices = np.arange(-modes, modes+1)
    nonzero = np.flatnonzero(frequencies)
    nn, cells = len(nonzero), len(mesh)-1
    # P nonzero modes at all radial nodes, one global P0, then one Q0/cell.
    mean_flux = nn*len(mesh)
    qmean_start = mean_flux+1
    dimension = qmean_start+cells
    normal = np.zeros((dimension, dimension), dtype=complex)
    load = np.zeros((dimension, n+1), dtype=complex)
    load[np.arange(nn), nonzero] = -1
    load[mean_flux, modes], load[mean_flux, -1] = -1, 1
    geometry = ActualCapGeometry(object_path, primal['primitive_nodes'])
    exact_knots = {Fraction(float(x)) for key, values in geometry.base.frozen.items()
                   if key.endswith('_knots') for x in values}
    exact_knots |= {-x for x in exact_knots}
    gx, gw = leggauss(primal['radial_gauss_order'])
    lag = indices[:, None]-indices[None, :]
    calls, wall, cpu = 0, time.monotonic(), time.process_time()
    minimum_determinant = np.inf
    for cell, (left, right) in enumerate(zip(mesh, mesh[1:])):
        width = right-left
        dofs = np.r_[cell*nn+np.arange(nn), (cell+1)*nn+np.arange(nn),
                     mean_flux, qmean_start+cell]
        local = np.zeros((len(dofs), len(dofs)), complex)
        cuts = sorted({Fraction(float(left)), Fraction(float(right))}
                      |{q for q in exact_knots if left < q < right})
        for exact_left, exact_right in zip(cuts, cuts[1:]):
            a, b = float(exact_left), float(exact_right)
            h = float(exact_right-exact_left)
            if h <= 0:
                continue
            for radial, weight in zip((a+b)/2+h*gx/2, h*gw/2):
                aa, bb, cc, _, _ = geometry.coefficients(radial, primal['angular_nodes'])
                determinant = aa*cc-bb*bb
                if np.min(determinant) <= 0:
                    raise ValueError('sampled inverse grounded positive form failed')
                minimum_determinant = min(minimum_determinant, float(np.min(determinant)))
                inverse_matrices = []
                for value in (cc/determinant, -bb/determinant, aa/determinant):
                    coefficient = np.fft.fft(value)/primal['angular_nodes']
                    inverse_matrices.append(coefficient[lag % primal['angular_nodes']])
                A, B, C = inverse_matrices
                P, Q = np.zeros((n, len(dofs)), complex), np.zeros((n, len(dofs)), complex)
                shape = ((right-radial)/width, (radial-left)/width)
                for side, derivative in ((0, -1/width), (1, 1/width)):
                    column = side*nn+np.arange(nn)
                    P[nonzero, column] = shape[side]
                    Q[nonzero, column] = -derivative/(1j*frequencies[nonzero])
                P[modes, -2], Q[modes, -1] = 1, 1
                local += weight*(P.conj().T@A@P+P.conj().T@B@Q
                                 +Q.conj().T@B@P+Q.conj().T@C@Q)
                calls += 1
        normal[np.ix_(dofs, dofs)] += local
        if (cell+1) % 24 == 0:
            print(json.dumps(dict(progress='complementary grounded cap',
                cells=cell+1, total=cells, coefficient_calls=calls)), flush=True)
    gamma = np.asarray(primal['actual_tail_chosen_midpoints'])
    if np.min(gamma[nonzero]) <= 0:
        raise ValueError('positive actual-tail nonmean entries required')
    outer = cells*nn+np.arange(nn)
    normal[outer, outer] += 1/gamma[nonzero]
    defect = float(np.linalg.norm(normal-normal.conj().T, 2))
    # Hermitian rounding is a definition of this floating candidate only.
    normal = (normal+normal.conj().T)/2
    solution = cho_solve(cho_factor(normal, lower=True), load)
    lower = load.conj().T@solution
    gap = (upper-lower+(upper-lower).conj().T)/2
    constant = np.zeros(n+1); constant[modes] = constant[-1] = 1
    residual = normal@solution-load
    report = dict(kind='floating_complementary_energy_cap_DN_lower_candidate',
        complete=True, rigorous_DN_enclosure=False, source_sha256=sha(__file__),
        primal_report_path=str(args.primal), primal_report_sha256=sha(args.primal),
        actual_object_sha256=primal['object_sha256'], exact_delta_fraction=primal['exact_delta_fraction'],
        source_dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_cap_low_schur.py','fourfold_phase_core_low_block.py',
            'fourfold_phase_symmetric_geometry.py')},
        modes=modes, flux_dimension=dimension, physical_frequencies=frequencies.tolist(),
        radial_interval=primal['physical_radial_interval'], radial_elements=cells,
        mean_slots_retained=True,
        flux_representation='continuous P1 p_k, q_k=-p_k_prime/(4ik), k!=0; p0 global constant; q0 cellwise constant',
        dual_form='integral flux* B^-1 flux plus <Gamma^-1 p_R,perp,p_R,perp>',
        dual_boundary_functional='-<p_left,g_left>+p0*xi_regular',
        coefficient_calls=calls, sampled_grounded_determinant_lower=minimum_determinant,
        floating_normal_Hermitian_defect=defect,
        floating_linear_residual=float(np.linalg.norm(residual, 2)),
        lower_Hermitian_defect=float(np.linalg.norm(lower-lower.conj().T, 2)),
        lower_constant_kernel_residual=float(np.linalg.norm(lower@constant)),
        finite_upper_minus_lower_eigenvalues=np.linalg.eigvalsh(gap).tolist(),
        finite_upper_minus_lower_norm=float(np.linalg.norm(gap, 2)),
        limitations=[
            'Exact integrals and actual positive tail entries give a full cap DN lower form with every retained Dirichlet/regular-mean input.',
            'This computation uses floating true-geometry approximations, quadrature and tail midpoints; it is not yet a directed upper/lower enclosure.',
            'Angular complement is represented in the true primal/dual variational principle, not deleted by assuming the Galerkin solution exact.',
            'No final cutoff or full core/cap infinite Schur inverse follows.'],
        CPU_seconds=time.process_time()-cpu, wall_seconds=time.monotonic()-wall)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    arrays = args.out.with_suffix('.npz')
    np.savez_compressed(arrays, mesh=mesh, frequencies=frequencies, dual_flux=solution,
        lower_DN=lower, primal_DN=upper, gap=gap, load=load)
    report['arrays'] = dict(path=str(arrays), sha256=sha(arrays), bytes=arrays.stat().st_size)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key:report[key] for key in ('flux_dimension','finite_upper_minus_lower_norm',
        'finite_upper_minus_lower_eigenvalues','lower_constant_kernel_residual','CPU_seconds','wall_seconds')}, indent=2),flush=True)


if __name__ == '__main__':
    main()
