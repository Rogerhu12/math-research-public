#!/usr/bin/env python3
"""One complete independent fixed-g Cartesian LM experiment.

Consumes an actual Cauchy state and its already executed same-field observer.
All arrays/checkpoints stay outside Git. This program never publishes,
changes a Cauchy counter, accesses credentials, or substitutes its model
for the caller's original Cauchy observer.
"""
import argparse
from dataclasses import asdict
import gc
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time
import traceback
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.sparse.linalg import lsmr

HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


stream = load("independent_cartesian_stream", HERE/"6a65-cartesian-complete-stream.py")
oracle_module = load("independent_cartesian_oracle", HERE/"6a65-cartesian-oracle-background.py")


def sha(path):
    return oracle_module.sha256(path)


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                           allow_nan=False).encode()).hexdigest()


def write_json(path, value):
    path = Path(path)
    if path.exists():
        raise FileExistsError("Fresh independent experiment output required: "+str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, separators=(",", ":"), allow_nan=False)+"\n")
    return sha(path)


def emit(event, **fields):
    print(json.dumps(dict(event=event, **fields), allow_nan=False), flush=True)


def integer(value, label, low, high):
    if type(value) is not int or not low <= value <= high:
        raise ValueError(label+" outside the explicit allowed range")
    return value


def quadrature(cuts, end, metric_order, curvature_order, geometry_order,
               curvature_share, geometry_share, curvature_weight, geometry_weight):
    """All physical partitions retained; fixed rows independent of LM trials."""
    cuts = np.unique(np.asarray(cuts, dtype=float))
    if cuts.ndim != 1 or cuts[0] != 0 or not np.all(np.diff(cuts) > 0):
        raise ValueError("Complete physical integration partition required")
    rows = {}

    def add(s, key, w):
        values = rows.setdefault(float(s), dict(metric=0., curvature=0., geometry=0.))
        values[key] += float(w)

    for key, order, share, scale in (
            ("metric", metric_order, 0., 1.),
            ("curvature", curvature_order, curvature_share, curvature_weight),
            ("geometry", geometry_order, geometry_share, geometry_weight)):
        gx, gw = leggauss(order)
        gx, gw = (gx+1)/2, gw/2
        if share:
            for i, s in enumerate(cuts):
                length = (s-cuts[i-1] if i else 0)+(cuts[i+1]-s if i+1 < len(cuts) else 0)
                add(s, key, scale*share*length/(2*end))
        if share < 1:
            for lo, hi in zip(cuts[:-1], cuts[1:]):
                for x, w in zip(gx, gw):
                    add(lo+(hi-lo)*x, key, scale*(1-share)*(hi-lo)*w/end)
    nodes = np.array(sorted(rows))
    weights = {key: np.array([rows[s][key] for s in nodes])
               for key in ("metric", "curvature", "geometry")}
    return nodes, weights


def observation_nodes(cuts, subdivisions):
    nodes = [float(cuts[0])]
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        nodes.extend(float(lo+(hi-lo)*j/subdivisions) for j in range(1, subdivisions+1))
    return np.unique(nodes)


class CachedBackground:
    def __init__(self, cache):
        self.cache = cache
        self.nodes = np.asarray(cache["s"])
        self.N = len(cache["u"])

    def __call__(self, nodes, N):
        nodes = np.asarray(nodes)
        if N != self.N:
            raise ValueError("A new angular observer needs a new direct source cache")
        index = np.searchsorted(self.nodes, nodes)
        if np.any(index >= len(self.nodes)) or not np.array_equal(self.nodes[index], nodes):
            raise ValueError("No interpolation of actual source samples is allowed")
        return self.cache["jets"][index], self.cache["bb"][index]


def normalized_value(value):
    return {
        **value,
        "curvature": {"maxCurvature": value["maxCurvature"],
                      "thresholdPoints": value["curvatureThresholdPoints"]},
        "geometry": {"maxAbsoluteY": value["maxAbsoluteY"],
                     "minHeldDistance": value["minHeldDistance"],
                     "maxRadius": value["maxRadius"],
                     "maxAdjustedHeightExcess": value["maxAdjustedHeightExcess"],
                     "maximumViolations": value["geometryMaximumViolations"]},
    }


def run(args):
    start = time.monotonic()
    prefix = args.prefix.resolve()
    scripts = args.scripts.resolve()
    repository = scripts.parents[2]
    if prefix == repository or repository in prefix.parents:
        raise ValueError("Independent raw outputs must remain outside the Git repository")
    if any(prefix.parent.glob(prefix.name+"-*")):
        raise FileExistsError("Fresh independent experiment prefix required")
    recipe = json.loads(args.recipe.read_text())
    if recipe.get("schema") != "6a65-complete-fixed-g-Cartesian-experiment-recipe-v1":
        raise ValueError("Explicit complete Cartesian recipe required")
    if recipe.get("sourceKind") != "actual-short-Cauchy-checkpoint":
        raise ValueError("A new geometric source needs its own declared adapter")
    J = integer(recipe["basis"]["radialBasisCount"], "radial basis", 4, 160)
    M = integer(recipe["basis"]["maxAngularFrequency"], "maximum frequency", 2, 64)
    N = integer(recipe["angles"], "training angles", 32, 2048)
    if N % 2 or N <= 8*M:
        raise ValueError("Training N must be even and greater than the pure-correction quartic frequency 8M")
    observer_N = integer(recipe["observation"]["angles"], "observer angles", N, 4096)
    if observer_N % 2 or observer_N <= N:
        raise ValueError("Independent observer must use a strictly larger even angle count")
    subdivisions = integer(recipe["observation"]["radialSubdivisions"], "observer subdivisions", 2, 16)
    block = integer(recipe.get("radialBlock", 16), "radial block", 1, 64)
    source = json.loads(args.source.read_text())
    old_observer = json.loads(args.observer.read_text())
    source_hash, candidate_hash, original_observer_hash = sha(args.source), sha(args.candidate), sha(args.observer)
    observer_model = old_observer.get("mathematicalObservationSchema", old_observer.get("schema"))
    if observer_model != "6a65-Cauchy-same-field-refined-metric-observation-v1":
        raise ValueError("The actual parent observer must identify the Cauchy mathematical source")
    if old_observer.get("inputs", {}).get("inputSHA256") != source_hash:
        raise ValueError("Parent observer did not consume these exact source bytes")
    if old_observer.get("inputs", {}).get("candidateSHA256") != candidate_hash:
        raise ValueError("Parent observer belongs to a different physical candidate")
    if not all(old_observer.get(k) is True for k in (
            "fieldCoefficientsUnchanged", "physicalMetricUnchanged", "sourceAngularPrimitiveUnchanged")):
        raise ValueError("Parent observer lacks unchanged-field receipts")
    if args.run_id < 1 or len(args.source_epoch) != 40:
        raise ValueError("Actual run and explicit source epoch required")
    files = {
        "initial": Path(str(prefix)+"-initial.json"),
        "state": Path(str(prefix)+"-state.json"),
        "observer": Path(str(prefix)+"-observer.json"),
        "report": Path(str(prefix)+"-report.json"),
    }
    actual_source_counts = source["cauchyAcceptedSteps"]
    if type(actual_source_counts) is not int or actual_source_counts < 0:
        raise ValueError("Actual parent count must be read, never forecast")
    emit("independent_cartesian_source_start", sourceStateSHA256=source_hash,
         originalObserverSHA256=original_observer_hash, originalCauchyAcceptedSteps=actual_source_counts,
         requestedJ=J, requestedM=M, trainingAngles=N, observerAngles=observer_N)
    with oracle_module.OracleBackground(
            scripts, args.candidate, args.source,
            wrapper=scripts/"6a65-geometry-cauchy-source-radial-cuts.cjs",
            heap_mb=recipe.get("oracleHeapMB", 256)) as original:
        identity = stream.point.bind_source_metadata(original.metadata, {
            **original.expected_hashes, "runId": args.run_id,
            "sourceEpoch": args.source_epoch, "observerSHA256": original_observer_hash})
        basis = stream.HalfTurnBasis(original.c, original.S, J, M,
                                    recipe["basis"].get("normalizedBreaks"))
        cuts = np.unique(np.r_[original.integration_cuts, basis.breaks])
        curv_options, geom_options = source["curvatureOptions"], source["geometryOptions"]
        metric_tau, curvature_tau = float(source["metricTau"]), float(source["curvatureTau"])
        config = stream.point.PointConfig(
            metric_tau=metric_tau, curvature_tau=curvature_tau,
            curvature_guide=float(curv_options["guide"]),
            true_cuff_height=float(original.metadata["Z"]),
            central_a=float(original.metadata["centralA"]))
        q = recipe["quadrature"]
        orders = [integer(q[name], name, 2, 16) for name in
                  ("metricGauss", "curvatureGauss", "geometryGauss")]
        nodes, weights = quadrature(cuts, original.S, *orders,
                        float(curv_options["nodeShare"]), float(geom_options["nodeShare"]),
                        float(curv_options["weight"]), float(geom_options["weight"]))
        grid_definition = dict(nodes=nodes.tolist(), radialWeights={k: v.tolist() for k, v in weights.items()},
                               fullPhysicalCuts=cuts.tolist(), angles=N, angularWeight=1/N,
                               radialNormalization="physical ds / original S",
                               completeHalfDomain=[0, original.cuff], targetMetricFrozen=True)
        emit("independent_cartesian_training_cache_start", radialPoints=len(nodes), points=len(nodes)*N,
             columns=basis.dimension, rows=len(nodes)*N*13, sourcePrimitiveAngles=original.metadata["primitiveAngles"])
        cache = original.cache(nodes, 2*np.pi*np.arange(N)/N, str(prefix)+"-training",
                               batch_size=recipe.get("sourceBatchSize", 4))
        background = CachedBackground(cache)
        coefficients = np.zeros((basis.nb, basis.na))
        gc.collect()
        linear = stream.CompleteStreamingLinearized(
            basis, nodes, weights, background, coefficients, N, config, block=block,
            preconditioner=recipe["preconditioner"],
            cache_point_blocks=bool(recipe.get("cachePointBlocks", False)))
        baseline = normalized_value(linear.statistics)
        common = dict(
            model="complete-proper-half-turn-Cartesian-fixed-g",
            source={"inputSHA256": source_hash, "candidateSHA256": candidate_hash,
                    "observerSHA256": original_observer_hash, "sourceEpoch": args.source_epoch,
                    "runId": args.run_id, "sourceIdentity": identity},
            originalCauchyAcceptedSteps=actual_source_counts,
            originalCauchyStateChanged=False, originalCauchyCounterChanged=False,
            basis=basis.definition, gridSHA256=canonical_sha(grid_definition),
            gridDefinition=grid_definition, pointConfig=asdict(config),
            sourcePrimitiveAngles=original.metadata["primitiveAngles"],
            dimension=basis.dimension, rowCount=linear.shape[0], targetMetricFrozen=True,
            completeHalfDomain=[0, original.cuff], correctionSupport=[original.c, original.S],
            allSixEndpointJetsFixed=True, allThirteenPointRowsRetained=True,
            recipeSHA256=sha(args.recipe), entrySHA256=sha(__file__),
            denseNormalConstructed=False, continuousCertificate=False, strongTargetComplete=False)
        initial = dict(common, schema="6a65-complete-Cartesian-fixed-g-initial-v1",
                       z=coefficients.ravel().tolist(), cartesianAcceptedSteps=0,
                       accepted=False, baseline=baseline, evaluation=baseline)
        initial_hash = write_json(files["initial"], initial)
        emit("independent_cartesian_actual_baseline", R2=baseline["squaredNorm"],
             metric=baseline["maxRelativeMetric"], curvature=baseline["maxCurvature"],
             held=baseline["minHeldDistance"], initialSHA256=initial_hash)
        lm_config, solve_config = recipe["lm"], recipe["lsmr"]
        damping = float(lm_config["lambda"])
        if not np.isfinite(damping) or damping <= 0:
            raise ValueError("Explicit positive LM damping required")
        max_damping = integer(lm_config["maxDampingAttempts"], "LM damping attempts", 1, 5)
        maxiter = integer(solve_config["maxIterations"], "LSMR iteration limit", 1, 400)
        alphas = [float(v) for v in lm_config["alphas"]]
        if not alphas or any(not np.isfinite(v) or not 0 < v <= 1 for v in alphas):
            raise ValueError("Explicit actual line-search fractions required")
        armijo = float(lm_config["armijo"])
        if not 0 < armijo < 1:
            raise ValueError("Explicit Armijo coefficient required")
        gradient = linear.operator.rmatvec(linear.residual)
        trace, accepted, chosen_alpha, evaluation = [], False, None, baseline
        for attempt in range(1, max_damping+1):
            solve_start = time.monotonic()
            result = lsmr(linear.operator, -linear.residual, damp=math.sqrt(damping),
                          atol=float(solve_config["atol"]), btol=float(solve_config["btol"]),
                          conlim=float(solve_config["conditionLimit"]), maxiter=maxiter,
                          show=bool(solve_config.get("show", False)))
            y = result[0]
            if not np.all(np.isfinite(y)):
                raise ArithmeticError("Actual LSMR direction is nonfinite")
            dcoeff = linear.unpack(y)
            jv = linear.operator.matvec(y)
            slope = float(gradient@y)
            predicted = float(-2*slope-jv@jv)
            solve = dict(attempt=attempt, damping=damping, istop=int(result[1]), iterations=int(result[2]),
                         normr=float(result[3]), normar=float(result[4]), norma=float(result[5]),
                         conda=float(result[6]), normx=float(result[7]), slope=slope,
                         predictedUndampedReduction=predicted, seconds=time.monotonic()-solve_start,
                         iterativeConvergenceReported=int(result[1]) in (1, 2, 4, 5),
                         completeColumns=basis.dimension, completeRows=linear.shape[0])
            trace.append(dict(kind="complete_matrix_free_solve", **solve))
            emit("independent_cartesian_full_solve", **solve)
            if slope < 0 and predicted > 0:
                for alpha in alphas:
                    trial = coefficients+alpha*dcoeff
                    try:
                        trial_value = normalized_value(stream.observe(
                            basis, nodes, weights, background, trial, N, config, block))
                        decreases = (trial_value["squaredNorm"] < baseline["squaredNorm"] and
                                     trial_value["squaredNorm"] <= baseline["squaredNorm"]+2*armijo*alpha*slope)
                        record = dict(kind="actual_complete_trial", attempt=attempt, alpha=alpha,
                                      actualValueEvaluated=True, domainRejected=False, accepted=bool(decreases),
                                      squaredNorm=trial_value["squaredNorm"], metric=trial_value["maxRelativeMetric"],
                                      curvature=trial_value["maxCurvature"], held=trial_value["minHeldDistance"])
                        trace.append(record)
                        emit("independent_cartesian_trial", **record)
                        if decreases:
                            coefficients, evaluation = trial, trial_value
                            accepted, chosen_alpha = True, alpha
                            break
                    except (ValueError, ArithmeticError, FloatingPointError) as error:
                        record = dict(kind="actual_trial_domain_rejection", attempt=attempt, alpha=alpha,
                                      actualValueEvaluated=False, domainRejected=True, accepted=False,
                                      error=str(error))
                        trace.append(record)
                        emit("independent_cartesian_trial", **record)
            if accepted:
                break
            damping *= 10
        state = dict(common, schema="6a65-complete-Cartesian-fixed-g-checkpoint-v1",
                     parentCartesianInitialSHA256=initial_hash, z=coefficients.ravel().tolist(),
                     cartesianAcceptedSteps=int(accepted), accepted=accepted,
                     status="accepted_actual_full_trial" if accepted else "actual_attempt_stalled_input_retained",
                     baseline=baseline, evaluation=evaluation, alpha=chosen_alpha,
                     completeAttemptCount=1, trace=trace)
        if not accepted and np.any(coefficients != 0):
            raise ArithmeticError("Unaccepted Cartesian state changed its zero input")
        state_hash = write_json(files["state"], state)
        emit("independent_cartesian_state", accepted=accepted, ownAcceptedSteps=int(accepted),
             stateSHA256=state_hash, R2=evaluation["squaredNorm"],
             metric=evaluation["maxRelativeMetric"], curvature=evaluation["maxCurvature"])
        del linear, gradient, cache, background
        gc.collect()
        obs_nodes = observation_nodes(cuts, subdivisions)
        # Observer weights report a finite complete value only; maximum fields
        # use every point, including the fixed true tail. No new fit is made.
        trapezoid = np.zeros(len(obs_nodes))
        h = np.diff(obs_nodes)/original.S
        trapezoid[:-1] += h/2
        trapezoid[1:] += h/2
        obs_weights = dict(metric=trapezoid,
                           curvature=float(curv_options["weight"])*trapezoid,
                           geometry=float(geom_options["weight"])*trapezoid)
        emit("independent_cartesian_refined_observer_cache_start",
             radialPoints=len(obs_nodes), points=len(obs_nodes)*observer_N)
        obs_cache = original.cache(obs_nodes, 2*np.pi*np.arange(observer_N)/observer_N,
                                  str(prefix)+"-observing", batch_size=recipe.get("sourceBatchSize", 4))
        obs_value = normalized_value(stream.observe(
            basis, obs_nodes, obs_weights, CachedBackground(obs_cache),
            coefficients, observer_N, config, block))
        observed = dict(
            schema="6a65-complete-Cartesian-fixed-g-same-field-observer-v1",
            inputs={"cartesianStateSHA256": state_hash, "candidateSHA256": candidate_hash,
                    "originalCauchyStateSHA256": source_hash, "originalObserverSHA256": original_observer_hash},
            fieldCoefficientsUnchanged=True, physicalMetricUnchanged=True,
            sourceAngularPrimitiveUnchanged=True, sourcePrimitiveAngles=original.metadata["primitiveAngles"],
            pointCount=len(obs_nodes)*observer_N, fullAngles=observer_N,
            actualCompleteHalfDomain=[0, original.cuff], fixedSourceIdentity=identity,
            evaluation=obs_value, worstMetric=obs_value["worstMetric"],
            worstCurvature=obs_value["worstCurvature"], minImmersion=obs_value["minImmersion"],
            allSixEndpointJetsFixed=True, numericalSampleOnly=True,
            capBudgetStillConditionalOnCompleteCore=True,
            continuousCertificate=False, strongTargetComplete=False)
        observer_hash = write_json(files["observer"], observed)
        emit("independent_cartesian_actual_refined_observer", observerSHA256=observer_hash,
             metric=obs_value["maxRelativeMetric"], curvature=obs_value["maxCurvature"],
             held=obs_value["minHeldDistance"], points=observed["pointCount"])
    if sha(args.source) != source_hash or sha(args.observer) != original_observer_hash:
        raise ArithmeticError("Independent experiment changed its original input files")
    report = dict(
        schema="6a65-independent-complete-Cartesian-experiment-scalar-report-v1",
        originalCauchyStateSHA256=source_hash, originalCauchyObserverSHA256=original_observer_hash,
        originalCauchyAcceptedSteps=actual_source_counts, originalCauchyStateAndCounterUnchanged=True,
        runId=args.run_id, sourceEpoch=args.source_epoch, sourceKind=recipe["sourceKind"],
        sourceIdentity=identity, recipeSHA256=sha(args.recipe), entrySHA256=sha(__file__),
        initialSHA256=initial_hash, stateSHA256=state_hash, observerSHA256=observer_hash,
        initialFile=str(files["initial"]), stateFile=str(files["state"]), observerFile=str(files["observer"]),
        dimension=basis.dimension, radialBasisCount=basis.nb, maximumAngularFrequency=basis.M,
        angularChannels=basis.na, fullTrainingAngles=N, sourcePrimitiveAngles=original.metadata["primitiveAngles"],
        completeRows=state["rowCount"], accepted=accepted, ownAcceptedSteps=int(accepted),
        alpha=chosen_alpha, baseline=baseline, evaluation=evaluation, refinedObservation=obs_value,
        actualSourceChildExitReceipt=original.exit_receipt,
        trace=trace, completeTargetMetricFrozen=True, allThirteenPointRowsRetained=True,
        sourceRawPublished=False, acceptedCauchyStepsAddedByThisExperiment=0,
        seconds=time.monotonic()-start, OSExitCode=None, externalExitReceiptRequired=True,
        continuousCertificate=False, strongTargetComplete=False)
    report_hash = write_json(files["report"], report)
    emit("independent_cartesian_experiment_complete", reportSHA256=report_hash,
         ownAcceptedSteps=int(accepted), originalCauchyStateUnchanged=True,
         originalCauchyAcceptedSteps=actual_source_counts, seconds=report["seconds"])
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scripts", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--observer", type=Path, required=True)
    parser.add_argument("--prefix", type=Path, required=True)
    parser.add_argument("--recipe", type=Path, required=True)
    parser.add_argument("--source-epoch", required=True)
    parser.add_argument("--run-id", type=int, required=True)
    args = parser.parse_args()
    try:
        run(args)
    except BaseException as error:
        failure = dict(schema="6a65-independent-Cartesian-actual-process-failure-v1",
                       error=str(error), traceback=traceback.format_exc(), continuousCertificate=False,
                       strongTargetComplete=False, acceptedStepsNotInferred=True)
        path = Path(str(args.prefix)+"-failure.json")
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(failure, indent=2)+"\n")
        raise


if __name__ == "__main__":
    main()
