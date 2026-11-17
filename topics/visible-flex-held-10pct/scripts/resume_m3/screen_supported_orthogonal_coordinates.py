#!/usr/bin/env python3
"""Read-only finite probe of stable coordinates for the same supported span.

The exact proposed functions use orthonormal polynomials for W^2 dphi, followed
by a fixed two-column elimination of mean/primary moments.  This script uses
finite Gauss quadrature to screen that construction; it does not certify the
continuous moments, modify the core source, solve a BVP, or diagnose its full
Jacobian.  Every reported coordinate equality is a finite numerical check.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
from couple_m3_smallcut_secant import accepted_anchor


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def recurrence(x, alpha, beta, p0):
    """P_j and its first two x derivatives, evaluated by three-term recurrence."""
    x = np.asarray(x)
    P = [np.full_like(x, p0)]
    D = [np.zeros_like(x)]
    DD = [np.zeros_like(x)]
    for j, a in enumerate(alpha):
        v = (x - a) * P[j]
        d = P[j] + (x - a) * D[j]
        dd = 2 * D[j] + (x - a) * DD[j]
        if j:
            v -= beta[j - 1] * P[j - 1]
            d -= beta[j - 1] * D[j - 1]
            dd -= beta[j - 1] * DD[j - 1]
        P.append(v / beta[j])
        D.append(d / beta[j])
        DD.append(dd / beta[j])
    return tuple(np.asarray(v) for v in (P, D, DD))


def projected_jets(phi, basis, alpha, beta, p0, C):
    x = np.cos(basis.n * phi)
    xp = -basis.n * np.sin(basis.n * phi)
    xpp = -basis.n ** 2 * x
    P, D, DD = recurrence(x, alpha, beta, p0)
    W, Wp, Wpp = basis._cutoff(basis._local(phi), 2)
    U = W * P
    Up = Wp * P + W * D * xp
    Upp = Wpp * P + 2 * Wp * D * xp + W * (DD * xp ** 2 + D * xpp)
    return tuple(v[2:] - C.T @ v[:2] for v in (U, Up, Upp))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--checkpoint', type=Path, required=True)
    p.add_argument('--control-transition', type=float, default=.4)
    p.add_argument('--gauss-order', type=int, default=512)
    p.add_argument('--comparison-points', type=int, default=2049)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if a.gauss_order < 64 or a.comparison_points < 257:
        raise ValueError('Insufficient finite probe resolution')
    r = json.loads(gzip.decompress(a.checkpoint.read_bytes()))
    accepted_anchor(r, a.checkpoint)
    if r.get('core_control_path') != 'raw-mean-primary-compact-v1':
        raise ValueError('Expected the completed actual raw m3 input')
    n, M = r['config']['base_mode'], r['config']['modes']
    if n != 3:
        raise ValueError('This probe follows the actual m3 endpoint design')
    settings = r['core_round_settings']
    lib = Path(__file__).with_name('round_raw_lib')
    sys.path.insert(0, str(lib))
    from complementary_moment_basis import ComplementaryMomentBasis
    from tight_moment_interval_bounds import install
    install()
    basis = ComplementaryMomentBasis(n, M, settings['halfwidth'],
        a.control_transition, center=settings['center'], lock_fundamental=True,
        precision=settings['coefficient_precision'])
    L = np.pi / n
    edges = [0., L - basis.a - basis.eps, L - basis.a]
    nodes, weights = np.polynomial.legendre.leggauss(a.gauss_order)
    phi = np.concatenate([(lo + hi) / 2 + (hi - lo) / 2 * nodes
                          for lo, hi in zip(edges[:-1], edges[1:])])
    weight = np.concatenate([(hi - lo) / (2 * L) * weights
                             for lo, hi in zip(edges[:-1], edges[1:])])
    x = np.cos(n * phi)
    W = basis._cutoff(basis._local(phi), 0)[0]
    w2 = weight * W ** 2
    p0 = float(1 / np.sqrt(w2.sum()))
    polynomials = [np.full_like(x, p0)]
    alpha, beta = [], []
    for j in range(M):
        pj = polynomials[j]
        aj = float(np.sum(w2 * x * pj ** 2))
        next_p = (x - aj) * pj
        if j:
            next_p -= beta[-1] * polynomials[j - 1]
        bj = float(np.sqrt(np.sum(w2 * next_p ** 2)))
        if not bj > 0:
            raise ArithmeticError('The positive finite quadrature norm vanished')
        alpha.append(aj)
        beta.append(bj)
        polynomials.append(next_p / bj)
    P = np.asarray(polynomials)
    U = W * P
    test = np.stack((np.ones_like(x), x))
    moments = (test * weight) @ U.T
    K = moments[:, :2]
    C = np.linalg.solve(K, moments[:, 2:])
    B = U[2:] - C.T @ U[:2]
    gram = (B * weight) @ B.T
    expected = np.eye(M - 1) + C.T @ C
    eigen = np.linalg.eigvalsh(gram)
    raw = basis.support_jets(phi, 0, 1.)[0]
    singular_raw = np.linalg.svd(raw * np.sqrt(weight), compute_uv=False)
    raw_c = np.asarray(r['parameters'][1:]) * np.asarray(r['central_correction_scales'])
    physical_b = raw_c @ raw
    coordinates = np.linalg.solve(expected, (B * weight) @ physical_b)
    comparison = np.linspace(0, L, a.comparison_points)
    raw_jets = basis.support_jets(comparison, 2, 1.)
    new_jets = projected_jets(comparison, basis, alpha, beta, p0, C)
    differences = [float(np.max(abs(raw_c @ old - coordinates @ new)))
                   for old, new in zip(raw_jets, new_jets)]
    k_inverse_norm = float(np.linalg.norm(np.linalg.inv(K), 2))
    diagnostics = dict(
        finite_orthonormal_gram_error=float(np.max(abs((U * weight) @ U.T - np.eye(M + 1)))),
        finite_constraint_residual=float(np.max(abs((test * weight) @ B.T))),
        finite_projected_gram_identity_error=float(np.max(abs(gram - expected))),
        finite_projected_gram_eigen_min=float(eigen[0]),
        finite_projected_gram_eigen_max=float(eigen[-1]),
        finite_projected_gram_condition=float(eigen[-1] / eigen[0]),
        K_inverse_norm=k_inverse_norm,
        theoretical_uniform_gram_upper_evaluated_numerically=1 + 1.5 * k_inverse_norm ** 2,
        raw_physical_L2_sample_matrix_condition=float(singular_raw[0] / singular_raw[-1]),
        raw_physical_L2_sample_gram_condition_via_svd=float((singular_raw[0] / singular_raw[-1]) ** 2),
        prior_weighted_high_moment_schur_condition=basis.constants['support_condition'],
        input_support_jet_sample_differences=differences,
        input_control_rho_sample_difference=float(np.max(abs(
            raw_c @ (raw_jets[0] + raw_jets[2]) -
            coordinates @ (new_jets[0] + new_jets[2])))))
    out = dict(scope=__doc__, command=sys.argv, input=str(a.checkpoint.resolve()),
        input_sha256=sha(a.checkpoint), n=n, modes=M,
        halfwidth=basis.a, control_transition=basis.eps, center=basis.center,
        gauss_order_per_nonzero_piece=a.gauss_order,
        comparison_points=a.comparison_points, diagnostics=diagnostics,
        finite_recurrence=dict(p0=p0, alpha=alpha, beta=beta),
        finite_low_constraint_matrix=K.tolist(), finite_constraint_corrections=C.tolist(),
        input_physical_raw_coefficients=raw_c.tolist(),
        finite_transformed_input_coordinates=coordinates.tolist(),
        source_sha256={str(f.resolve()):sha(f) for f in [Path(__file__),
            Path(__file__).with_name('couple_m3_smallcut_secant.py'), *sorted(lib.glob('*.py'))]},
        interpretation='This is an isolated numerical coordinate screen for the exact lambda-one '
            'supported finite span.  Exact continuous recurrence/moment coefficients would require '
            'their own enclosure before a new production evaluator.  A bounded L2 Gram does not '
            'bound a C2 norm, prove good BVP Jacobian conditioning, produce an accepted solution, '
            'or change the active endpoint run.')
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(diagnostics, indent=2))


if __name__ == '__main__':
    main()
