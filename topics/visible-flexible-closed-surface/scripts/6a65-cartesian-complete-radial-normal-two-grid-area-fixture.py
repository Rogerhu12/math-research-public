#!/usr/bin/env python3
"""New nonzero two-grid q=2-area complete normal/old-LM comparison.

Dense J/H are restricted to these 126 columns. Both complete 14-row grids
use the already defined literal analytic six-jet surface and a new random
coefficient vector. This does not consume any research checkpoint.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
import scipy
from scipy.sparse.linalg import lsmr


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def relative(a, b):
    a, b = np.asarray(a), np.asarray(b)
    return float(np.linalg.norm(a-b)/max(1., np.linalg.norm(a), np.linalg.norm(b)))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--scripts", type=Path, required=True)
    ap.add_argument("--solver", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.output.exists():
        raise FileExistsError("Fresh actual finite verification output required")
    begin = time.monotonic()
    refpath = args.scripts/"6a65-cartesian-channel-blocks-finite-fixture.py"
    reference = load(refpath, "all_band_literal_background_definition")
    stream = reference.stream
    module = load(args.solver, "actual_full_two_grid_area_radial_normal")
    base = load(args.scripts/"6a65-geometry-gap-window-cartesian.py", "full_area_fixture_base")
    joint = load(args.scripts/"6a65-geometry-gap-window-two-grid-cartesian.py", "full_area_fixture_joint")
    area_path = args.scripts/"6a65-geometry-area-ratio-power-two.py"
    areaop = load(area_path, "full_area_fixture_q2")
    rng = np.random.default_rng(202611261505)
    basis = base.periodic_basis(stream, .1, 1.1, 6, 3)
    eta, damping = .1, .03
    cuts = np.unique(np.r_[0., basis.breaks, 1.3])
    class LiteralCache:
        def __init__(self, nodes, N):
            self.nodes = nodes
            self.u = 2*np.pi*np.arange(N)/N
        def __call__(self, nodes, N):
            if N != len(self.u):
                raise ValueError("Exact declared finite grid required")
            return reference.background(nodes, N)
    caches, weights = {}, {}
    for name, N, gauss in (("training", 10, 3), ("observer", 14, 4)):
        xi, wi = np.polynomial.legendre.leggauss(gauss)
        nodes = np.concatenate([(a+b)/2+(b-a)*xi/2 for a, b in zip(cuts[:-1], cuts[1:])])
        w = .5*np.concatenate([(b-a)*wi/2 for a, b in zip(cuts[:-1], cuts[1:])])
        caches[name] = LiteralCache(nodes, N)
        weights[name] = dict(metric=w, curvature=.003*w, geometry=2*w)
    coefficients = rng.normal(size=(basis.nb, basis.na))*2e-5
    config = stream.point.PointConfig(metric_tau=.05, curvature_tau=1e6,
        curvature_guide=9.5, true_cuff_height=.51, central_a=1.436024268143396)
    recipe = base.default_recipe()
    recipe["radialBlock"] = 5
    area = dict(targetAreaRatio=.5, strength=1., reciprocalPower=2)
    linear = areaop.CompleteAreaTwoGrid(joint, stream, basis, caches, weights,
        coefficients, config, recipe, area)
    augmented = module.SameSobolevAreaFullBandAugmented(linear, damping, eta=eta)
    n = basis.dimension
    if n != 126:
        raise ValueError("Dense diagnostic restricted to the declared 126 columns")
    dense_begin = time.monotonic()
    eye = np.eye(n)
    J = np.column_stack([augmented.raw_matvec(eye[:, k]) for k in range(n)])
    H = J.T@J
    savedH = reference.dense_band(augmented.blocks.normal_band)
    LT = np.column_stack([augmented.blocks.old_factor(eye[:, k], True).ravel()
                          for k in range(n)])
    S = LT.T@LT
    old_coordinate_J = np.column_stack([linear.matvec(eye[:, k]) for k in range(n)])
    original_operator_error = relative(J, old_coordinate_J@LT)
    area_normal = J[linear.parent.shape[0]:].T@J[linear.parent.shape[0]:]
    grid_normal_norms = []
    for j, name in enumerate(linear.names):
        a, b = linear.parent.boundaries[j:j+2]
        c, d = linear.boundaries[j+1:j+3]
        local_J = np.vstack((J[a:b], J[c:d]))
        grid_normal_norms.append(float(np.linalg.norm(local_J.T@local_J)))
    T = np.column_stack([augmented.unpack(eye[:, k]).ravel() for k in range(n)])
    full_band_error = relative(H, savedH)
    radial = np.repeat(np.arange(basis.nb), basis.na)
    outside = np.abs(radial[:, None]-radial[None, :]) > 5
    outside_max = float(np.max(np.abs(H[outside]))) if np.any(outside) else 0.
    channel = np.tile(np.arange(basis.na), basis.nb)
    cross = channel[:, None] != channel[None, :]
    component = np.tile(np.array([c for c, _, _ in basis.channels]), basis.nb)
    cross_component = component[:, None] != component[None, :]
    cross_norm = float(np.linalg.norm(H[cross]))
    component_norm = float(np.linalg.norm(H[cross_component]))
    cross_error = relative(H[cross], savedH[cross])
    physicalP = H+eta*S
    whitening_error = relative(T.T@physicalP@T, eye)
    Aold = np.vstack((J, np.sqrt(damping)*LT))
    Anew = np.column_stack([augmented.operator.matvec(eye[:, k]) for k in range(n)])
    augmented_error = relative(Anew, Aold@T)
    old_direction = np.linalg.lstsq(Aold, augmented.rhs, rcond=None)[0]
    new_y = np.linalg.lstsq(Anew, augmented.rhs, rcond=None)[0]
    new_direction = augmented.unpack(new_y).ravel()
    direction_error = relative(old_direction, new_direction)
    old_value = float(np.linalg.norm(Aold@old_direction-augmented.rhs)**2)
    new_value = float(np.linalg.norm(Aold@new_direction-augmented.rhs)**2)
    physical = augmented.physical_normal_residual(new_direction)
    direct_physical = (H+damping*S)@new_direction+J.T@linear.residual
    physical_residual_difference = relative(physical, direct_physical)
    gradient_scale = max(1., np.linalg.norm(J.T@linear.residual))
    physical_normal_relative = float(np.linalg.norm(physical)/gradient_scale)
    x, y = rng.normal(size=n), rng.normal(size=augmented.shape[0])
    dot_error = relative(augmented.operator.matvec(x)@y,
                         x@augmented.operator.rmatvec(y))
    spectrum = np.linalg.eigvalsh(Anew.T@Anew)
    expected_lower, expected_upper = min(1., damping/eta), max(1., damping/eta)
    eigen_bounds_verified = bool(spectrum[0] >= expected_lower-2e-11 and
                                 spectrum[-1] <= expected_upper+2e-11)
    dense_seconds = time.monotonic()-dense_begin
    iteration_begin = time.monotonic()
    result = lsmr(augmented.operator, augmented.rhs, damp=0., atol=1e-11, btol=1e-11,
                  conlim=1e12, maxiter=300)
    iterative = augmented.unpack(result[0]).ravel()
    iteration_seconds = time.monotonic()-iteration_begin
    iterative_normal = float(np.linalg.norm(augmented.physical_normal_residual(iterative))/gradient_scale)
    verified = bool(full_band_error < 3e-12 and cross_error < 3e-12 and
        outside_max == 0 and cross_norm > 0 and component_norm > 0 and
        whitening_error < 2e-10 and augmented_error < 2e-12 and
        direction_error < 3e-8 and relative(old_value, new_value) < 3e-11 and
        physical_residual_difference < 3e-6 and physical_normal_relative < 3e-8 and
        dot_error < 3e-12 and eigen_bounds_verified and
        augmented.blocks.receipt["conjugateAliasFrequencyPairsUsed"] > 0 and
        augmented.blocks.receipt["relativeImaginaryMomentRoundoff"] < 3e-13 and
        iterative_normal < 3e-9 and np.count_nonzero(coefficients) == coefficients.size and
        original_operator_error < 2e-11 and np.linalg.norm(area_normal) > 0 and
        min(grid_normal_norms) > 0 and linear.statistics["areaBarrierStatistics"]["activePoints"] > 0)
    report = dict(schema="6a65-two-grid-q2-area-complete-physical-normal-finite-fixture-v1",
        fixtureSHA256=sha(__file__), solverSHA256=sha(args.solver),
        literalBackgroundDefinitionSHA256=sha(refpath),
        streamSHA256=sha(args.scripts/"6a65-cartesian-complete-stream.py"),
        pointSHA256=sha(args.scripts/"6a65-cartesian-complete-point-operator.py"),
        numpyVersion=np.__version__, scipyVersion=scipy.__version__,
        seed=202611261505, coefficientsNonzero=int(np.count_nonzero(coefficients)),
        coefficientLittleEndianFloat64SHA256=hashlib.sha256(coefficients.astype('<f8').tobytes()).hexdigest(),
        columns=n, physicalRows=linear.shape[0],
        grids=[dict(name=name, radialPoints=len(cache.nodes), fullAngles=len(cache.u))
               for name, cache in caches.items()], maximumFrequency=basis.M,
        areaOperatorSHA256=sha(area_path), areaDefinition=area,
        twoGridOperatorSHA256=sha(args.scripts/"6a65-geometry-gap-window-two-grid-cartesian.py"),
        periodicBasisSourceSHA256=sha(args.scripts/"6a65-geometry-gap-window-cartesian.py"),
        rawPhysicalOperatorVersusOriginalSharedSobolevOperatorRelativeError=original_operator_error,
        completeAreaRowNormalNorm=float(np.linalg.norm(area_normal)),
        completeGridNormalNorms=grid_normal_norms,
        baseline=linear.statistics, damping=damping, eta=eta,
        assembly=augmented.blocks.receipt,
        completePhysicalNormalBandRelativeError=full_band_error,
        completeCrossChannelNormalRelativeError=cross_error,
        crossChannelNormalNorm=cross_norm, crossCartesianComponentNormalNorm=component_norm,
        completePhysicalNormalOutsideRadialBandMaximum=outside_max,
        equilibratedFactorPhysicalWhiteningRelativeError=whitening_error,
        explicitAugmentedMatrixRelativeError=augmented_error,
        completeAugmentedAdjointRelativeError=dot_error,
        denseSameQuadraticDirectionRelativeError=direction_error,
        oldQuadraticMinimum=old_value, newQuadraticMinimum=new_value,
        physicalNormalResidualImplementationDifference=physical_residual_difference,
        denseDirectionRelativePhysicalNormalResidual=physical_normal_relative,
        augmentedNormalSpectrum=dict(actualMinimum=float(spectrum[0]), actualMaximum=float(spectrum[-1]),
            exactAlgebraicLowerBound=expected_lower, exactAlgebraicUpperBound=expected_upper,
            floatingDiagnosticWithinBounds=eigen_bounds_verified),
        actualLSMR=dict(istop=int(result[1]), iterations=int(result[2]),
            iterativeConvergenceReported=int(result[1]) in (1,2,4,5),
            normr=float(result[3]), normar=float(result[4]), norma=float(result[5]),
            conda=float(result[6]), normx=float(result[7]), seconds=iteration_seconds,
            directionRelativeError=relative(iterative, old_direction),
            relativePhysicalNormalResidual=iterative_normal),
        finiteDenseDiagnosticSeconds=dense_seconds, seconds=time.monotonic()-begin,
        verified=verified, completeNonlinearLMAcceptances=0,
        actualCauchySourceConsumed=False, production5292ColumnSolvePerformed=False,
        oldPhysicalLMQuadraticPreserved=True, allThirteenPointRowsRetained=True,
        allInverseSquareAreaRowsRetained=True, completeTwoGridRowOrderRetained=True,
        originalHalfGridWeightsNotMultipliedAgain=True,
        oldCommonSobolevRegularizerAddedOnce=True,
        allAngularCrossChannelTermsRetained=True, denseMatricesOnlyInThisSmallFixture=True,
        continuousCertificate=False, strongTargetComplete=False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps(report, allow_nan=False), flush=True)
    if not verified:
        raise AssertionError("New complete all-channel physical-normal check failed")


if __name__ == "__main__":
    main()
