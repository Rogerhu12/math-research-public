#!/usr/bin/env python3
"""Small NONZERO complete-operator check for the same-quadratic block solver.

Dense matrices are deliberately limited to this 91-column fixture.  This is
not a Cauchy checkpoint, source reconstruction, nonlinear LM acceptance, or
continuous surface result.  The production helper itself remains streaming.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy.sparse.linalg import lsmr

HERE = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE/filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


stream = load("channel_fixture_stream", "6a65-cartesian-complete-stream.py")
blocks = load("channel_fixture_blocks", "6a65-cartesian-exact-channel-blocks.py")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def relative(a, b):
    return float(np.linalg.norm(np.asarray(a)-np.asarray(b))/
                 max(1., np.linalg.norm(a), np.linalg.norm(b)))


def background(nodes, N):
    # Complete literal six-jets of this finite surface of revolution.
    s = np.asarray(nodes)[:, None]
    u = 2*np.pi*np.arange(N)[None, :]/N
    r = .8+.05*np.cos(12*s)
    rs, rss = -.6*np.sin(12*s), -7.2*np.cos(12*s)
    co, si = np.cos(u), np.sin(u)
    out = np.zeros((len(nodes), 6, N, 3))
    out[:, 0, :, 0], out[:, 0, :, 1], out[:, 0, :, 2] = r*co, r*si, .1+.3*s
    out[:, 1, :, 0], out[:, 1, :, 1], out[:, 1, :, 2] = rs*co, rs*si, .3
    out[:, 2, :, 0], out[:, 2, :, 1] = -r*si, r*co
    out[:, 3, :, 0], out[:, 3, :, 1] = rss*co, rss*si
    out[:, 4, :, 0], out[:, 4, :, 1] = -rs*si, rs*co
    out[:, 5, :, 0], out[:, 5, :, 1] = -r*co, -r*si
    return out, np.broadcast_to(.76+.02*np.cos(3*s), (len(nodes), N))


def dense_band(band):
    n = band.shape[1]
    matrix = np.zeros((n, n))
    for d in range(band.shape[0]):
        for j in range(n-d):
            matrix[j+d, j] = matrix[j, j+d] = band[d, j]
    return matrix


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError("Fresh finite diagnostic output required")
    started = time.monotonic()
    rng = np.random.default_rng(202611261339)
    basis = stream.HalfTurnBasis(.1, 1.1, 7, 4)
    N = 12  # Valid N > 2M, but 2M above rFFT half-grid: exercise conjugate alias.
    cuts = np.unique(np.r_[0., basis.breaks, 1.3])
    xi, wi = np.polynomial.legendre.leggauss(3)
    nodes = np.concatenate([(a+b)/2+(b-a)*xi/2 for a, b in zip(cuts[:-1], cuts[1:])])
    w = np.concatenate([(b-a)*wi/2 for a, b in zip(cuts[:-1], cuts[1:])])
    weights = dict(metric=w, curvature=.003*w, geometry=2*w)
    coefficients = rng.normal(size=(basis.nb, basis.na))*2e-5
    config = stream.point.PointConfig(metric_tau=.05, curvature_tau=1e6,
                                     curvature_guide=9.5, true_cuff_height=.51,
                                     central_a=1.436024268143396)
    linear = stream.CompleteStreamingLinearized(
        basis, nodes, weights, background, coefficients, N, config,
        block=5, cache_point_blocks=True)
    damping = .03
    augmented = blocks.SameSobolevAugmented(linear, damping, eta=.1)
    n = basis.dimension
    if n != 91:
        raise ValueError("Dense diagnostic restricted to its declared 91 columns")
    eye = np.eye(n)
    dense_started = time.monotonic()
    J = np.column_stack([augmented.raw_matvec(eye[:, k]) for k in range(n)])
    LT = np.column_stack([augmented.blocks.old_factor(eye[:, k], True).ravel()
                          for k in range(n)])
    H = J.T@J
    channel_errors = []
    for channel in range(basis.na):
        indices = np.arange(basis.nb)*basis.na+channel
        channel_errors.append(relative(H[np.ix_(indices, indices)],
                                       dense_band(augmented.blocks.normal_blocks[channel])))
    S = LT.T@LT
    regularizer_errors = []
    for channel in range(basis.na):
        indices = np.arange(basis.nb)*basis.na+channel
        regularizer_errors.append(relative(S[np.ix_(indices, indices)],
                                           dense_band(augmented.blocks.old_bands[channel])))
    ids = np.repeat(np.arange(basis.nb), basis.na)
    offband = abs(ids[:, None]-ids[None, :]) > 5
    offband_maximum = float(np.max(np.abs(H[offband])))
    Aold = np.vstack((J, np.sqrt(damping)*LT))
    T = np.column_stack([augmented.unpack(eye[:, k]).ravel() for k in range(n)])
    Adirect = np.column_stack([augmented.operator.matvec(eye[:, k]) for k in range(n)])
    augmented_matrix_error = relative(Adirect, Aold@T)
    old_direction = np.linalg.lstsq(Aold, augmented.rhs, rcond=None)[0]
    new_coordinate = np.linalg.lstsq(Adirect, augmented.rhs, rcond=None)[0]
    new_direction = augmented.unpack(new_coordinate).ravel()
    direction_error = relative(old_direction, new_direction)
    old_q = float(np.linalg.norm(Aold@old_direction-augmented.rhs)**2)
    new_q = float(np.linalg.norm(Aold@new_direction-augmented.rhs)**2)
    quadratic_error = relative(old_q, new_q)
    physical_residual = augmented.physical_normal_residual(new_direction)
    direct_residual = (H+damping*S)@new_direction+J.T@linear.residual
    normal_residual_error = relative(physical_residual, direct_residual)
    normal_scaled = float(np.linalg.norm(physical_residual)/max(1., np.linalg.norm(J.T@linear.residual)))
    x, y = rng.normal(size=n), rng.normal(size=augmented.shape[0])
    left, right = augmented.operator.matvec(x)@y, x@augmented.operator.rmatvec(y)
    adjoint_error = relative(left, right)
    dense_seconds = time.monotonic()-dense_started
    iterative_started = time.monotonic()
    result = lsmr(augmented.operator, augmented.rhs, damp=0., atol=1e-11, btol=1e-11,
                  conlim=1e12, maxiter=600)
    iterative_direction = augmented.unpack(result[0]).ravel()
    iterative_seconds = time.monotonic()-iterative_started
    iterative_normal = float(np.linalg.norm(augmented.physical_normal_residual(iterative_direction))/
                             max(1., np.linalg.norm(J.T@linear.residual)))
    verified = bool(
        max(channel_errors) < 2e-11 and max(regularizer_errors) < 2e-13 and
        offband_maximum == 0. and augmented_matrix_error < 2e-13 and
        direction_error < 2e-8 and quadratic_error < 2e-11 and
        normal_residual_error < 2e-6 and normal_scaled < 2e-8 and adjoint_error < 2e-12 and
        np.count_nonzero(coefficients) == coefficients.size)
    report = dict(
        schema="6a65-nonzero-complete-channel-block-same-LM-finite-fixture-v1",
        fixtureSHA256=sha(__file__), solverSHA256=sha(HERE/"6a65-cartesian-exact-channel-blocks.py"),
        streamSHA256=sha(HERE/"6a65-cartesian-complete-stream.py"),
        pointSHA256=sha(HERE/"6a65-cartesian-complete-point-operator.py"),
        finiteSourceKind="literal-six-jet-surface-of-revolution-plus-nonzero-complete-Cartesian-coefficients",
        coefficientLittleEndianFloat64SHA256=hashlib.sha256(coefficients.astype('<f8').tobytes()).hexdigest(),
        coefficientsNonzero=int(np.count_nonzero(coefficients)), seed=202611261339,
        columns=n, physicalRows=linear.shape[0], fullAngles=N, maxFrequency=basis.M,
        angularMomentConjugateAliasActuallyUsed=2*basis.M>N//2,
        baseline=linear.statistics, damping=damping, assembly=augmented.blocks.receipt,
        maximumChannelBlockRelativeError=max(channel_errors),
        oldRegularizerBandRelativeError=max(regularizer_errors),
        completePhysicalNormalOffbandMaximum=offband_maximum,
        explicitAugmentedMatrixRelativeError=augmented_matrix_error,
        completeAugmentedAdjointRelativeError=adjoint_error,
        denseSameQuadraticDirectionRelativeError=direction_error,
        oldQuadraticMinimum=old_q, newQuadraticMinimum=new_q,
        quadraticMinimumRelativeError=quadratic_error,
        physicalNormalResidualImplementationDifference=normal_residual_error,
        denseDirectionRelativePhysicalNormalResidual=normal_scaled,
        finiteDenseDiagnosticSeconds=dense_seconds,
        actualLSMR=dict(istop=int(result[1]), iterations=int(result[2]), normr=float(result[3]),
                        normar=float(result[4]), norma=float(result[5]), conda=float(result[6]),
                        normx=float(result[7]), seconds=iterative_seconds,
                        iterativeConvergenceReported=int(result[1]) in (1,2,4,5),
                        directionRelativeError=relative(iterative_direction, old_direction),
                        relativePhysicalNormalResidual=iterative_normal),
        verified=verified, completeNonlinearLMAcceptances=0, actualCauchySourceConsumed=False,
        production7760ColumnSolvePerformed=False, sourceOrMetricChanged=False,
        denseMatricesOnlyInThisSmallFixture=True,
        continuousCertificate=False, strongTargetComplete=False,
        seconds=time.monotonic()-started)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps(report, allow_nan=False), flush=True)
    if not verified:
        raise AssertionError("Complete finite same-quadratic check failed")


if __name__ == "__main__":
    main()
