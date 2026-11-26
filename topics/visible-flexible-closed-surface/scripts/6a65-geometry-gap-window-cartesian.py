#!/usr/bin/env python3
"""Complete fixed-g Cartesian solve for the explicit new gap-window source.

The source has its own kind and own natural-perimeter metric. Corrections
are supported only after the certified coast, retaining its entire prefix
and all true R205 tail jets. All periodic Cartesian Fourier channels are
included; no symmetry is claimed for an unfiltered background.
"""
from __future__ import annotations
import os
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"
import argparse
from dataclasses import asdict
import gc
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import traceback
import uuid
import numpy as np
from scipy.sparse.linalg import lsmr

SCHEMA = "6a65-explicit-gap-window-full-periodic-fixed-g-Cartesian-v1"


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        allow_nan=False).encode()).hexdigest()


def write(path, value):
    path = Path(path)
    if path.exists():
        raise FileExistsError("New actual output required: "+str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, separators=(",", ":"), allow_nan=False)+"\n")
    return sha(path)


def emit(event, **value):
    print(json.dumps(dict(event=event, **value), allow_nan=False), flush=True)


def periodic_basis(stream, lo, hi, J, M):
    """Same complete quintic radial map, all three real periodic components."""
    basis = stream.HalfTurnBasis(lo, hi, J, M)
    channels = []
    for component in range(3):
        channels.append((component, 0, "cos"))
        for k in range(1, M+1):
            channels.extend(((component, k, "cos"), (component, k, "sin")))
    basis.channels = channels
    basis.na = len(channels)
    basis.modes = np.array([k for _, k, _ in channels], dtype=int)
    basis.dimension = basis.nb*basis.na
    basis.definition = dict(
        **{key: value for key, value in basis.definition.items()
           if key not in ("schema", "angularChannels", "dimension",
                          "channelOrder", "reflectionRestriction")},
        schema="6a65-full-real-periodic-Cartesian-clamped-quintic-basis-v1",
        angularChannels=basis.na, dimension=basis.dimension,
        channelOrder=[dict(component=i, frequency=k, kind=t) for i, k, t in channels],
        allPeriodicCartesianComponents=True, properHalfTurnRestriction=False,
        reflectionRestriction=False, backgroundSymmetryAssumed=False)
    return basis


def default_recipe():
    return dict(schema=SCHEMA, sourceKind="gap105-short-window-natural-metric-v1",
        basis=dict(radialBasisCount=32, maxAngularFrequency=12,
                   support="coast_end_to_developed_cut", allRealPeriodicChannels=True),
        angles=128, observerAngles=192, observerSubdivisions=2,
        quadrature=dict(metricGauss=2, curvatureGauss=2, geometryGauss=2),
        normalizationQuadrature=1024, window=.2, heapMB=128,
        radialBlock=12, sourceBatchSize=4, cachePointBlocks=True,
        preconditioner=dict(kind="banded_sobolev_h2", beta0=.01, beta1=1., beta2=.001),
        lm=dict(damping=1e-4, maxDampingAttempts=3, alphas=[1., .5, .25, .125],
                armijo=1e-4),
        lsmr=dict(maxIterations=80, atol=1e-6, btol=1e-6,
                  conditionLimit=1e10))


class Cached:
    def __init__(self, record):
        self.nodes = np.asarray(record["nodes"], float)
        self.u = np.asarray(record["angles"], float)
        self.jets = np.load(record["files"]["jets"], mmap_mode="r")
        self.radius = np.load(record["files"]["radius"], mmap_mode="r")
        if (self.jets.shape != (len(self.nodes), 6, len(self.u), 3)
            or self.radius.shape != (len(self.nodes), 3)
            or self.jets.dtype != np.dtype("<f8") or self.radius.dtype != np.dtype("<f8")
            or self.jets.flags.writeable or self.radius.flags.writeable):
            raise ValueError("Read-only exact saved six-jet/radius shapes required")
        for key in ("jets", "radius"):
            if sha(record["files"][key]) != record["SHA256"][key]:
                raise ValueError("Actual fixed-source cache bytes changed: "+key)
        if not np.all(np.diff(self.nodes) > 0):
            raise ValueError("Strictly ordered actual cache nodes required")
        self.bb = np.broadcast_to(self.radius[:, 0, None], (len(self.nodes), len(self.u)))

    def __call__(self, nodes, N):
        nodes = np.asarray(nodes, float)
        index = np.searchsorted(self.nodes, nodes)
        if (N != len(self.u) or np.any(index >= len(self.nodes))
            or not np.array_equal(self.nodes[index], nodes)):
            raise ValueError("No interpolation or alternate source angles allowed")
        return self.jets[index], self.bb[index]

    def target_curvature(self):
        K = -self.radius[:, 2]/self.radius[:, 0]
        i = int(np.argmax(np.abs(K)))
        return dict(formula="K_g=-a_ss/a for this frozen new natural metric",
            maxAbsolute=float(abs(K[i])), signed=float(K[i]), s=float(self.nodes[i]),
            radius=self.radius[i].tolist(), necessaryReachCurvatureLimit=1/.097**2,
            exceedsNecessaryReachCurvatureLimit=bool(abs(K[i]) > 1/.097**2),
            numericalSamplingOnly=True, continuousBound=False)


def validate_recipe(recipe):
    if recipe.get("schema") != SCHEMA or recipe.get("sourceKind") != "gap105-short-window-natural-metric-v1":
        raise ValueError("Explicit new-source recipe required")
    J, M = (recipe["basis"][k] for k in ("radialBasisCount", "maxAngularFrequency"))
    N, NO = recipe["angles"], recipe["observerAngles"]
    if (type(J) is not int or not 4 <= J <= 160 or type(M) is not int or not 2 <= M <= 64
        or type(N) is not int or N % 2 or N <= 8*M
        or type(NO) is not int or NO % 2 or NO <= N):
        raise ValueError("Declared complete basis and resolved training/observer angles required")
    if (recipe["basis"]["support"] != "coast_end_to_developed_cut"
        or recipe["basis"]["allRealPeriodicChannels"] is not True):
        raise ValueError("Certified prefix must be retained with all periodic correction channels")
    return J, M, N, NO


def prepare(args, stream, helper, background):
    start = time.monotonic()
    prefix = args.prefix.resolve()
    if any(prefix.parent.glob(prefix.name+"-*")):
        raise FileExistsError("Fresh prepare prefix required")
    recipe = json.loads(args.recipe.read_text()) if args.recipe else default_recipe()
    J, M, N, NO = validate_recipe(recipe)
    saved = json.loads(args.checkpoint.read_text())
    scope = "local-actual-new-source" if args.run_id is None else "actual-same-job-new-source"
    if args.run_id is not None and args.run_id <= 0:
        raise ValueError("A supplied real runner ID must be positive")
    run_identity = dict(scope=scope, actualRunId=args.run_id, executionUUID=str(uuid.uuid4()))
    cv, gv = saved["curvatureOptions"], saved["geometryOptions"]
    with background.GapPrefixWindowBackground(
            args.scripts, args.candidate, args.checkpoint, args.ramp_master, args.coast_master,
            window=float(recipe["window"]), quadrature=recipe["normalizationQuadrature"],
            heap_mb=recipe["heapMB"]) as source:
        identity = background.bind_new_source_metadata(source.metadata, source.expected_hashes)
        basis = periodic_basis(stream, source.b, source.S, J, M)
        cuts = np.unique(np.r_[source.integration_cuts, basis.breaks])
        orders = [recipe["quadrature"][k] for k in ("metricGauss", "curvatureGauss", "geometryGauss")]
        nodes, weights = helper.quadrature(cuts, source.S, *orders,
            float(cv["nodeShare"]), float(gv["nodeShare"]), float(cv["weight"]), float(gv["weight"]))
        config = stream.point.PointConfig(
            metric_tau=float(saved["metricTau"]), curvature_tau=float(saved["curvatureTau"]),
            curvature_guide=float(cv["guide"]), true_cuff_height=source.metadata["Z"],
            central_a=source.metadata["centralA"])
        obs_nodes = helper.observation_nodes(cuts, int(recipe["observerSubdivisions"]))
        trap = np.zeros(len(obs_nodes))
        h = np.diff(obs_nodes)/source.S
        trap[:-1] += h/2
        trap[1:] += h/2
        obs_weights = dict(metric=trap, curvature=float(cv["weight"])*trap,
                           geometry=float(gv["weight"])*trap)
        records = {}
        for label, ss, nn, ww in (("training", nodes, N, weights),
                                  ("observer", obs_nodes, NO, obs_weights)):
            emit("new_gap_actual_cache_start", kind=label, nodes=len(ss), angles=nn,
                 columns=basis.dimension, allThirteenRows=len(ss)*nn*13)
            cache = source.cache(ss, 2*np.pi*np.arange(nn)/nn, str(prefix)+"-"+label,
                                 batch_size=recipe["sourceBatchSize"])
            records[label] = dict(
                nodes=ss.tolist(), angles=cache["u"].tolist(),
                weights={k: v.tolist() for k, v in ww.items()},
                files=cache["files"],
                SHA256=dict(jets=sha(cache["files"]["jets"]), radius=sha(cache["files"]["radius"]),
                            report=sha(cache["files"]["report"])),
                sourceDefinitionSHA256=source.metadata["sourceDefinitionSHA256"])
            emit("new_gap_actual_cache_written", kind=label,
                 jetsSHA256=records[label]["SHA256"]["jets"],
                 radiusSHA256=records[label]["SHA256"]["radius"],
                 seconds=time.monotonic()-start)
            del cache
        metadata = source.metadata
    # Reuse is allowed only after the actual oracle naturally exits zero.
    if source.exit_receipt["originalOracle"]["actualOSExitCode"] != 0 or not source.exit_receipt["originalOracle"]["naturalExit"]:
        raise ArithmeticError("Actual original source did not finish naturally")
    definition = dict(sourceIdentity=identity, basis=basis.definition, recipe=recipe,
        pointConfig=asdict(config), completePhysicalCuts=cuts.tolist(),
        correctionSupport=[source.b, source.S], certifiedPrefixSupport=[0, source.b],
        completeHalfDomain=[0, source.cuff], runIdentity=run_identity,
        cacheIdentity={key: dict(SHA256=value["SHA256"], nodes=value["nodes"], angles=value["angles"],
                                weights=value["weights"], sourceDefinitionSHA256=value["sourceDefinitionSHA256"])
                       for key, value in records.items()},
        operatorSources=dict(stream=sha(args.scripts/"6a65-cartesian-complete-stream.py"),
            point=sha(args.scripts/"6a65-cartesian-complete-point-operator.py"),
            quadrature=sha(args.scripts/"6a65-cartesian-independent-experiment-v3.py"),
            background=sha(args.background), entry=sha(__file__)))
    report = dict(schema=SCHEMA+"-prepared", definition=definition,
        definitionSHA256=canonical(definition), sourceMetadata=metadata, caches=records,
        rawArraysPublished=False, originalSourceUnchanged=True, newSourceAcceptedSteps=0,
        actualNaturalChildExit=source.exit_receipt, sourceBindingComplete=True,
        seconds=time.monotonic()-start, continuousCertificate=False, strongTargetComplete=False)
    out = Path(str(prefix)+"-prepared.json")
    digest = write(out, report)
    emit("new_gap_source_ready", prepared=str(out), preparedSHA256=digest,
         columns=basis.dimension, seconds=report["seconds"])
    return report


def validate_prepared(args, stream, background):
    saved = json.loads(args.prepared.read_text())
    if saved.get("schema") != SCHEMA+"-prepared" or saved.get("sourceBindingComplete") is not True:
        raise ValueError("An actual complete prepared new-source cache is required")
    definition = saved["definition"]
    if saved["definitionSHA256"] != canonical(definition):
        raise ValueError("Prepared definition identity mismatch")
    sources = definition["operatorSources"]
    actual = dict(stream=sha(args.scripts/"6a65-cartesian-complete-stream.py"),
        point=sha(args.scripts/"6a65-cartesian-complete-point-operator.py"),
        quadrature=sha(args.scripts/"6a65-cartesian-independent-experiment-v3.py"),
        background=sha(args.background), entry=sha(__file__))
    if sources != actual:
        raise ValueError("Complete operator or source adapter changed")
    meta = saved["sourceMetadata"]
    identity = background.bind_new_source_metadata(meta, meta["sourceDefinition"]["sourceHashes"])
    # This metadata was sealed by prepare after independent live-oracle binding.
    if identity != definition["sourceIdentity"]:
        raise ValueError("Frozen new-source definition changed")
    natural = saved["actualNaturalChildExit"]["originalOracle"]
    if natural.get("actualOSExitCode") != 0 or natural.get("naturalExit") is not True:
        raise ValueError("Prepared source lacked actual natural zero exit")
    J, M, N, NO = validate_recipe(definition["recipe"])
    lo, hi = definition["correctionSupport"]
    if lo != meta["b"] or hi != meta["S"] or definition["certifiedPrefixSupport"] != [0, lo]:
        raise ValueError("Certified entire prefix or true tail would be changed")
    basis = periodic_basis(stream, lo, hi, J, M)
    if basis.definition != definition["basis"]:
        raise ValueError("Complete periodic correction space changed")
    caches = {}
    for label, row in saved["caches"].items():
        if definition["cacheIdentity"][label] != dict(
                SHA256=row["SHA256"], nodes=row["nodes"], angles=row["angles"],
                weights=row["weights"], sourceDefinitionSHA256=row["sourceDefinitionSHA256"]):
            raise ValueError("Grid/cache identity changed")
        if sha(row["files"]["report"]) != row["SHA256"]["report"]:
            raise ValueError("Actual cache receipt bytes changed")
        caches[label] = Cached(row)
    return saved, definition, basis, caches


def run(args, stream, background):
    start = time.monotonic()
    prepared, definition, basis, caches = validate_prepared(args, stream, background)
    prefix = args.prefix.resolve()
    if any(prefix.parent.glob(prefix.name+"-*")):
        raise FileExistsError("Fresh complete solve prefix required")
    recipe = definition["recipe"]
    conf = stream.point.PointConfig(**definition["pointConfig"])
    training, observer = caches["training"], caches["observer"]
    N, NO = recipe["angles"], recipe["observerAngles"]
    weights = {k: np.asarray(v, float) for k, v in prepared["caches"]["training"]["weights"].items()}
    oweights = {k: np.asarray(v, float) for k, v in prepared["caches"]["observer"]["weights"].items()}
    prepared_sha = sha(args.prepared)
    coefficients = np.zeros((basis.nb, basis.na))
    own_count = attempts = 0
    if args.state:
        state = json.loads(args.state.read_text())
        for key, expected in (("schema", SCHEMA+"-checkpoint"), ("preparedSHA256", prepared_sha),
                               ("definitionSHA256", prepared["definitionSHA256"]),
                               ("entrySHA256", sha(__file__))):
            if state.get(key) != expected:
                raise ValueError("Own actual state changed "+key)
        coefficients = np.asarray(state["z"], float).reshape(basis.nb, basis.na)
        own_count, attempts = state["ownAcceptedSteps"], state["attemptCount"]
        if not np.all(np.isfinite(coefficients)):
            raise ValueError("Finite complete saved coefficients required")
    parent_hash = sha(args.state) if args.state else None
    common = dict(schema=SCHEMA+"-checkpoint", preparedSHA256=prepared_sha,
        definitionSHA256=prepared["definitionSHA256"], sourceIdentity=definition["sourceIdentity"],
        basis=basis.definition, correctionSupport=definition["correctionSupport"],
        entirePrefixPreserved=True, trueTailAndCuffPreserved=True,
        allThirteenPointRowsRetained=True, allCartesianPeriodicChannelsRetained=True,
        backgroundSymmetryAssumed=False, originalCauchyStateUnchanged=True,
        targetMetricFrozen=True, sourceParameterVectorUnchanged=True,
        pointConfig=asdict(conf), entrySHA256=sha(__file__),
        completeHalfDomain=definition["completeHalfDomain"],
        continuousCertificate=False, strongTargetComplete=False)
    target = dict(training=training.target_curvature(), observer=observer.target_curvature())
    emit("new_gap_fixed_target_curvature", **target)
    if target["observer"]["exceedsNecessaryReachCurvatureLimit"]:
        emit("new_gap_necessary_curvature_obstruction", diagnostic=target)
    before = stream.observe(basis, training.nodes, weights, training, coefficients, N, conf, recipe["radialBlock"])
    observed_before = stream.observe(basis, observer.nodes, oweights, observer, coefficients, NO, conf, recipe["radialBlock"])
    initial = dict(common, z=coefficients.ravel().tolist(), ownAcceptedSteps=own_count,
        attemptCount=attempts, accepted=False, parentStateSHA256=parent_hash,
        evaluation=before, observed=observed_before, targetGaussianCurvature=target)
    initial_hash = write(str(prefix)+"-initial.json", initial)
    emit("new_gap_actual_complete_initial", initialSHA256=initial_hash,
        columns=basis.dimension, rows=before["rowCount"], R2=before["squaredNorm"],
        metric=before["maxRelativeMetric"], curvature=before["maxCurvature"],
        denseMetric=observed_before["maxRelativeMetric"], denseCurvature=observed_before["maxCurvature"])
    outputs = []
    damping = float(recipe["lm"]["damping"])
    for iteration in range(1, args.steps+1):
        linear = stream.CompleteStreamingLinearized(
            basis, training.nodes, weights, training, coefficients, N, conf,
            block=recipe["radialBlock"], preconditioner=recipe["preconditioner"],
            cache_point_blocks=recipe["cachePointBlocks"])
        baseline = linear.statistics
        gradient = linear.operator.rmatvec(linear.residual)
        trace, accepted, alpha_selected = [], False, None
        evaluation = baseline
        for attempt in range(1, int(recipe["lm"]["maxDampingAttempts"])+1):
            tick = time.monotonic()
            result = lsmr(linear.operator, -linear.residual, damp=math.sqrt(damping),
                atol=recipe["lsmr"]["atol"], btol=recipe["lsmr"]["btol"],
                conlim=recipe["lsmr"]["conditionLimit"], maxiter=recipe["lsmr"]["maxIterations"])
            y = result[0]
            if not np.all(np.isfinite(y)):
                raise ArithmeticError("Nonfinite complete solve direction")
            direction = linear.unpack(y)
            jv = linear.operator.matvec(y)
            slope = float(gradient@y)
            predicted = float(-2*slope-jv@jv)
            solve = dict(kind="actual_complete_LSMR", attempt=attempt, damping=damping,
                istop=int(result[1]), iterations=int(result[2]), normr=float(result[3]),
                normar=float(result[4]), normA=float(result[5]), condA=float(result[6]),
                normx=float(result[7]), slope=slope, predictedReduction=predicted,
                completeColumns=basis.dimension, completeRows=linear.shape[0],
                seconds=time.monotonic()-tick)
            trace.append(solve)
            emit("new_gap_actual_complete_LSMR", iteration=iteration, **solve)
            if slope < 0 and predicted > 0:
                for alpha in recipe["lm"]["alphas"]:
                    candidate = coefficients+float(alpha)*direction
                    try:
                        value = stream.observe(basis, training.nodes, weights, training, candidate, N,
                                               conf, recipe["radialBlock"])
                        decreased = (value["squaredNorm"] < baseline["squaredNorm"] and
                            value["squaredNorm"] <= baseline["squaredNorm"]+
                            2*recipe["lm"]["armijo"]*alpha*slope)
                        row = dict(kind="actual_full_trial", alpha=alpha, accepted=bool(decreased),
                            actualValueEvaluated=True, R2=value["squaredNorm"],
                            metric=value["maxRelativeMetric"], curvature=value["maxCurvature"],
                            minImmersion=value["minImmersion"], held=value["minHeldDistance"])
                        trace.append(row)
                        emit("new_gap_actual_trial", iteration=iteration, **row)
                        if decreased:
                            coefficients, evaluation, accepted = candidate, value, True
                            alpha_selected = alpha
                            break
                    except (ValueError, ArithmeticError, FloatingPointError) as error:
                        row = dict(kind="actual_domain_rejected_trial", alpha=alpha, accepted=False,
                                   actualValueEvaluated=False, error=str(error))
                        trace.append(row)
                        emit("new_gap_actual_trial", iteration=iteration, **row)
            if accepted:
                break
            damping *= 10
        attempts += 1
        own_count += int(accepted)
        # Same exact six-jet field, denser full angle/physical sampling.
        observed = stream.observe(basis, observer.nodes, oweights, observer, coefficients, NO,
                                  conf, recipe["radialBlock"])
        state = dict(common, z=coefficients.ravel().tolist(), ownAcceptedSteps=own_count,
            attemptCount=attempts, ownAcceptedStepsAdded=int(accepted), accepted=accepted,
            parentStateSHA256=parent_hash, originalInitialSHA256=initial_hash,
            baseline=baseline, evaluation=evaluation, observed=observed,
            alpha=alpha_selected, trace=trace, targetGaussianCurvature=target)
        path = Path(str(prefix)+f"-step{iteration:02d}-state.json")
        parent_hash = write(path, state)
        outputs.append(dict(path=str(path), stateSHA256=parent_hash,
            accepted=accepted, ownAcceptedSteps=own_count, attemptCount=attempts,
            evaluation=evaluation, observed=observed))
        emit("new_gap_actual_state_saved", iteration=iteration, stateSHA256=parent_hash,
            accepted=accepted, ownAcceptedSteps=own_count, R2=evaluation["squaredNorm"],
            metric=evaluation["maxRelativeMetric"], curvature=evaluation["maxCurvature"],
            observedMetric=observed["maxRelativeMetric"], observedCurvature=observed["maxCurvature"],
            held=observed["minHeldDistance"], seconds=time.monotonic()-start)
        del linear, gradient
        gc.collect()
        if not accepted:
            break
    # Retain byte identity of the fixed source arrays across all actual trials.
    for name, cache in prepared["caches"].items():
        for key in ("jets", "radius"):
            if sha(cache["files"][key]) != cache["SHA256"][key]:
                raise ArithmeticError("Frozen actual source cache changed during solve")
    report = dict(schema=SCHEMA+"-solve-report", preparedSHA256=prepared_sha,
        definitionSHA256=prepared["definitionSHA256"], initialSHA256=initial_hash,
        outputs=outputs, ownAcceptedSteps=own_count, attemptCount=attempts,
        completeColumns=basis.dimension, allThirteenRowsRetained=True,
        fullPeriodicSpace=True, certifiedEntirePrefixRetained=True,
        actualFixedSourceCachesUnchanged=True, seconds=time.monotonic()-start,
        OSExitCode=None, externalExitReceiptRequired=True,
        continuousCertificate=False, strongTargetComplete=False)
    digest = write(str(prefix)+"-report.json", report)
    emit("new_gap_actual_solve_complete", reportSHA256=digest,
         ownAcceptedSteps=own_count, seconds=report["seconds"])
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("prepare", "solve"))
    ap.add_argument("--scripts", type=Path, required=True)
    ap.add_argument("--background", type=Path, default=Path(__file__).with_name("6a65-geometry-gap-window-background.py"))
    ap.add_argument("--prefix", type=Path, required=True)
    ap.add_argument("--candidate", type=Path)
    ap.add_argument("--checkpoint", type=Path)
    ap.add_argument("--ramp-master", type=Path)
    ap.add_argument("--coast-master", type=Path)
    ap.add_argument("--recipe", type=Path)
    ap.add_argument("--run-id", type=int)
    ap.add_argument("--prepared", type=Path)
    ap.add_argument("--state", type=Path)
    ap.add_argument("--steps", type=int, default=3)
    args = ap.parse_args()
    if not 1 <= args.steps <= 20:
        raise ValueError("Explicit actual attempt count required")
    if args.scripts.parents[2] in args.prefix.resolve().parents:
        raise ValueError("Raw source caches/checkpoints must remain outside Git")
    stream = module(args.scripts/"6a65-cartesian-complete-stream.py", "gap_full_periodic_stream")
    helper = module(args.scripts/"6a65-cartesian-independent-experiment-v3.py", "gap_original_quadrature")
    background = module(args.background, "gap_explicit_actual_background")
    try:
        if args.mode == "prepare":
            prepare(args, stream, helper, background)
        else:
            run(args, stream, background)
    except BaseException as error:
        failure = dict(schema=SCHEMA+"-actual-failure", error=str(error),
            traceback=traceback.format_exc(), acceptedStepsNotInferred=True,
            continuousCertificate=False, strongTargetComplete=False)
        path = Path(str(args.prefix)+"-failure.json")
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(failure, indent=2)+"\n")
        raise


if __name__ == "__main__":
    main()

