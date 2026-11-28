#!/usr/bin/env python3
"""Full fixed-g polar LM with audited complete sparse-jet angular normal.

An explicit old-to-new implementation transition preserves every physical
objective field and recomputes the identical baseline/group statistics.
Actual prior accepts remain inherited and are never counted again.

All 12789 Cartesian coefficients, both complete grids, all 13 original rows
and the q=2 area row are retained.  At eta=lambda the published complete-band
factor is the exact physical LM normal matrix; two triangular solves give
the same direction as the one-step whitened LSMR solve.  The original true
normal residual and full nonlinear objective are evaluated explicitly.
"""
from __future__ import annotations
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"
import argparse
import copy
import gc
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np

SCHEMA = "2ecf-polar-C2-G10-same-g-full-normal-LM-v1"
HELPER_SHA = "8e8d40c05ba5b5e15c49be4c7d91c882d93007567f67caa19a4a43ad39bc2084"
PARENT_ENTRY_SHA = "18ba78db845473cfeef6125cde41e733b36ce096963e01ab1fec43041dadc37a"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        allow_nan=False).encode()).hexdigest()


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def write(path, value):
    path = Path(path)
    if path.exists():
        raise FileExistsError("Fresh actual output required: " + str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, separators=(",", ":"), allow_nan=False) + "\n")
    return sha(path)


def emit(event, **value):
    print(json.dumps(dict(event=event, **value), allow_nan=False), flush=True)


def scalar(value):
    return dict(R2=value["squaredNorm"], metric=value["maxRelativeMetric"],
        curvature=value["maxCurvature"], eta=value["minImmersion"],
        sigma=value["areaBarrierStatistics"]["minAreaRatio"],
        held=value["minHeldDistance"], areaR2=value["areaBarrierStatistics"]["squaredNorm"])


def run(args):
    started = time.monotonic()
    prepare = module(args.prepare_entry, "polar_prefix_prepare")
    prepared, definition, basis, caches, mods, oldprepared, olddef, oldbasis = prepare.validate_prepared(args)
    stream = mods["stream"]
    fullnormal_path = args.scripts / "6a65-cartesian-complete-radial-normal-two-grid-area.py"
    parent_path = args.scripts / "6a65-geometry-nonfold-polar-q2-full-normal-v2.py"
    if sha(fullnormal_path) != HELPER_SHA or sha(parent_path) != PARENT_ENTRY_SHA:
        raise ValueError("The complete original physical-H or parent entry changed")
    fast_entry = Path(__file__).with_name("2ecf-polar-complete-sparse-jet-normal.py")
    normal = module(fast_entry, "polar_G10_fast_complete_normal")
    audit = json.loads(args.normal_audit.read_text())
    if (normal.ORIGINAL_SHA != HELPER_SHA
            or audit["schema"] != "2ecf-actual-complete-G10-sparse-jet-normal-audit-v1"
            or audit["normalEntrySHA256"] != sha(fast_entry)
            or audit["preparedSHA256"] != sha(args.prepared)
            or (audit["actualRows"],audit["actualColumns"]) != (4291840,12789)
            or audit["fullPhysicalNormalRelativeResidual"] > 1e-7):
        raise ValueError("Actual complete prepared-space normal audit required")
    parent_entry = module(parent_path, "polar_prefix_parent_entry")
    joint = module(args.scripts / "6a65-geometry-gap-window-two-grid-cartesian.py", "polar_prefix_joint")
    areaop = module(args.scripts / "6a65-geometry-area-ratio-power-two.py", "polar_prefix_area")
    config = stream.point.PointConfig(**definition["pointConfig"])
    recipe = copy.deepcopy(definition["recipe"])
    recipe["cachePointBlocks"] = False
    stream_entry = Path(__file__).with_name("2ecf-polar-complete-two-grid-streamed.py")
    memory = module(stream_entry, "polar_G10_actual_streamed_two_grid")
    memory.install(joint)
    weights = {k: {n: .5 * np.asarray(v, float) for n, v in prepared["caches"][k]["weights"].items()}
        for k in caches}
    area = dict(targetAreaRatio=.5, strength=1., reciprocalPower=2)
    model = dict(schema=SCHEMA + "-definition", preparedSHA256=sha(args.prepared),
        sourceIdentity=definition["sourceIdentity"], basis=basis.definition,
        pointConfig=definition["pointConfig"], recipe=recipe, area=area,
        preparationEntrySHA256=sha(args.prepare_entry), solveEntrySHA256=sha(__file__),
        fullNormalHelperSHA256=HELPER_SHA, targetMetricUnchanged=True,
        fullNormalAssemblyEntrySHA256=sha(fast_entry),
        sparseAngularKernelEntrySHA256=normal.KERNEL_SHA,
        actualCompleteNormalAuditSHA256=sha(args.normal_audit),
        fullNormalExactAlgebraRearrangedOnly=True,
        allOriginal13RowsAndQ2AreaRetained=True, allCrossChannelCovariancesRetained=True,
        directDirection="-T T^T J^T r with T T^T=(J^T J + lambda S)^(-1)",
        adaptiveDamping=dict(initial=args.initial_damping, minimum=1e-12, maximum=1e4,
            acceptedFullStepGainOver075="lambda/3", acceptedGainUnder025OrShortStep="2*lambda",
            otherwise="lambda", rejectedNormalAttempt="10*lambda"),
        nonlinearAccept="full objective decrease and Armijo slope condition",
        entireCentralOpenCylinderFixed=True, trueTailAndCuffFixed=True,
        completePrefixCorrectionReleased=True, independentObserverIncluded=False, oldThirdObserverRadialsNowTraining=True,
        denseSobolevUsesNewFullQuadrature=True, old205QuadratureObjectiveNotIdentified=True,
        streamedPointEntrySHA256=sha(stream_entry), completePointBlocksRecomputedFromFrozenSource=True,
        allRowsWeightsAndPhysicalH2UnchangedByStreaming=True,
        unusedNormalBandAndAugmentedRHSReleasedAfterFactor=True)
    model_sha = canonical(model)
    provenance, checks = None, None
    implementation_history = []; transition = False
    damping = args.initial_damping
    own = attempts = 0
    if args.state is not None:
        state = json.loads(args.state.read_text())
        previous = copy.deepcopy(model)
        for key in ("fullNormalAssemblyEntrySHA256", "sparseAngularKernelEntrySHA256",
                "actualCompleteNormalAuditSHA256", "fullNormalExactAlgebraRearrangedOnly"):
            previous.pop(key)
        prior_entry = Path(__file__).with_name("2ecf-polar-c2-g10-solve.py")
        previous["solveEntrySHA256"] = sha(prior_entry)
        valid_same = state.get("modelDefinition") == model
        valid_transition = state.get("modelDefinition") == previous
        if (state.get("schema") != SCHEMA + "-state"
                or canonical(state["modelDefinition"]) != state["modelDefinitionSHA256"]
                or not (valid_same or valid_transition)):
            raise ValueError("Identical physical objective and exact declared implementation required")
        implementation_history = copy.deepcopy(state.get("implementationHistory", []))
        transition = valid_transition
        if transition:
            implementation_history.append(dict(parentStateSHA256=sha(args.state),
                previousModelDefinitionSHA256=state["modelDefinitionSHA256"],
                previousSolveEntrySHA256=sha(prior_entry),newSolveEntrySHA256=sha(__file__),
                onlyCompleteNormalAngularAlgebraRearranged=True,
                sourceTargetBasisRowsWeightsSobolevAndAcceptanceUnchanged=True,
                inheritedActualAccepts=state["ownExtendedAcceptedSteps"],
                inheritedAcceptsCountedAgain=False,newNonlinearAttemptsBeforeBaseline=0,
                independentlyPaidCompleteNormalAuditSHA256=sha(args.normal_audit)))
        z = np.asarray(state["z"], float).reshape(basis.nb, basis.na)
        own, attempts = state["ownExtendedAcceptedSteps"], state["ownExtendedAttempts"]
        damping = state["nextDamping"]
        provenance, checks = state["initialWarmProvenance"], state["actualFullDerivativeCheck"]
        if type(own) is not int or type(attempts) is not int or not 0 <= own <= attempts:
            raise ValueError("Actual own step counters required")
    elif args.warm_state is not None:
        old = json.loads(args.warm_state.read_text())
        allowed = {
            "2ecf-polar-C2-full-prefix-fixed-g-full-normal-LM-v1-state": "2ecf-polar-c2-prefix-solve.py",
            "2ecf-polar-C2-independent-zero-source-fixed-g-full-normal-LM-v1-state": "2ecf-polar-c2-prefix-zero-solve.py",
        }
        oldmodel = old["modelDefinition"]
        if (old.get("schema") not in allowed or old["preparedSHA256"] != prepared["parentPreparedSHA256"]
                or oldmodel["basis"] != basis.definition or oldmodel["sourceIdentity"] != definition["sourceIdentity"]
                or oldmodel["pointConfig"] != definition["pointConfig"]
                or canonical(oldmodel) != old["modelDefinitionSHA256"]
                or oldmodel["solveEntrySHA256"] != sha(Path(__file__).with_name(allowed[old["schema"]]))):
            raise ValueError("Warm transfer requires the exact same complete field and target g")
        z = np.asarray(old["z"], float).reshape(basis.nb, basis.na).copy()
        if z.ravel().tolist() != old["z"]:
            raise ArithmeticError("Every actual parent coefficient must be preserved")
        provenance = dict(kind="exact same-space coefficient copy; changed finite quadrature",
            parentStateSHA256=sha(args.warm_state), parentPreparedSHA256=prepared["parentPreparedSHA256"],
            parentSchema=old["schema"], parentAcceptedSteps=old["ownExtendedAcceptedSteps"],
            parentAttempts=old["ownExtendedAttempts"], parentCountsBorrowedAsNew=False,
            all12789CoefficientValuesPreservedExactly=True, targetMetricChanged=False,
            sourcePositionChanged=False, correctionSpaceChanged=False, actualOldFieldExactlyContained=True,
            quadratureChanged=True, oldObjectiveCostNotIdentified=True)
    elif args.zero:
        z = np.zeros((basis.nb, basis.na))
        provenance = dict(kind="independent literal source with all 12789 correction coefficients zero",
            parentCountsBorrowedAsNew=False, ownAcceptedStepsAtStart=0,
            targetMetricChanged=False, sourcePositionChanged=False)
    else:
        raise ValueError("Dense initial state needs an exact old full field or an explicit independent zero")
    if z.shape != (87, 147) or not np.all(np.isfinite(z)):
        raise ValueError("All actual finite 12789 coefficients required")
    value, groups = areaop.observe(joint, stream, basis, caches, weights, z, config, recipe, area)
    if transition:
        if value != state["evaluation"] or groups != state["groupValues"]:
            raise ArithmeticError("Complete actual baseline changed during implementation transition")
        implementation_history[-1]["actualCompleteBaselineAndGroupsIdentical"] = True
    prefix = args.prefix.resolve()
    parent_sha = None if args.state is None else sha(args.state)
    common = dict(schema=SCHEMA + "-state", modelDefinition=model,
        modelDefinitionSHA256=model_sha, initialWarmProvenance=provenance,
        implementationHistory=implementation_history,
        sourceIdentity=definition["sourceIdentity"], preparedSHA256=sha(args.prepared),
        targetMetricUnchanged=True, all12789Columns=True, full14Rows=True,
        continuousMetricCertified=False, wholeClosedReachCertified=False)
    initial = dict(common, z=z.ravel().tolist(), ownExtendedAcceptedSteps=own,
        ownExtendedAttempts=attempts, accepted=False, parentStateSHA256=parent_sha,
        actualFullDerivativeCheck=checks, nextDamping=damping,
        evaluation=value, groupValues=groups, warmBaselineOnly=args.state is None)
    initial_sha = write(str(prefix) + "-initial.json", initial)
    emit("expanded_polar_initial", SHA256=initial_sha, columns=basis.dimension,
        rows=value["rowCount"], ownAcceptedSteps=own, **scalar(value))
    outputs = []
    for step in range(1, args.steps+1):
        linear = areaop.CompleteAreaTwoGrid(joint, stream, basis, caches, weights, z, config, recipe, area)
        baseline = linear.statistics
        trace, accepted, selected = [], False, None
        augmented = None
        for attempt in range(1, 7):
            if augmented is not None:
                del augmented
                gc.collect()
            tick = time.monotonic()
            augmented = normal.SameSobolevAreaFullBandAugmented(linear, damping, eta=damping)
            # The direct physical solve uses only the factor, scales, and old S.
            # Its independent full J/JT residual does not use the saved band/RHS.
            released = augmented.blocks.normal_band.nbytes + augmented.rhs.nbytes
            del augmented.blocks.normal_band, augmented.rhs
            gc.collect()
            emit("actual_unused_linear_storage_released", bytes=released,
                completeRowsRetained=linear.shape[0], columns=basis.dimension)
            gradient = augmented.raw_transpose(linear.residual)
            dz = -augmented.blocks.unpack(augmented.blocks.transpose(gradient))
            residual = augmented.physical_normal_residual(dz)
            norm_info = parent_entry.physical_normal_statistics(residual, gradient)
            refinement = []
            for refinement_index in range(3):
                if norm_info["originalPhysicalNormalRelativeResidual"] <= 1e-10:
                    break
                dz -= augmented.blocks.unpack(augmented.blocks.transpose(residual))
                residual = augmented.physical_normal_residual(dz)
                norm_info = parent_entry.physical_normal_statistics(residual, gradient)
                refinement.append(norm_info)
            if checks is None:
                rng = np.random.default_rng(20261128)
                vector = rng.standard_normal(basis.dimension)
                vector /= np.linalg.norm(vector)
                direction = linear.unpack(vector)
                jv = augmented.raw_matvec(direction)
                cotangent = rng.standard_normal(linear.shape[0])
                lhs, rhs = float(jv @ cotangent), float(direction.ravel() @ augmented.raw_transpose(cotangent).ravel())
                adjoint = abs(lhs-rhs) / max(1., abs(lhs), abs(rhs))
                fdchecks = []
                for eps in (1e-6, 1e-7, 1e-8):
                    plus = areaop.residual(stream, basis, caches, weights, z+eps*direction, config, recipe, area)
                    minus = areaop.residual(stream, basis, caches, weights, z-eps*direction, config, recipe, area)
                    error = float(np.linalg.norm((plus-minus)/(2*eps)-jv)/max(1., np.linalg.norm(jv)))
                    fdchecks.append(dict(epsilon=eps, relativeL2=error))
                    del plus, minus
                    if error < 2e-5:
                        break
                checks = dict(actualColumns=basis.dimension, actualRows=linear.shape[0],
                    adjointRelativeError=adjoint, finiteDifference=fdchecks,
                    actualNonzeroWarmField=bool(np.any(z != 0.)), fullPrefixColumnsIncluded=True,
                    actualG10DenseQuadratureUsed=True)
                if adjoint > 1e-10 or error > 2e-5:
                    raise ArithmeticError("The actual full new-space derivative check failed")
                del direction, vector, jv, cotangent
                emit("expanded_polar_complete_derivative", **checks)
            jv = augmented.raw_matvec(dz)
            slope, jv2 = float(gradient.ravel() @ dz.ravel()), float(jv @ jv)
            normalrow = dict(kind="complete_original_physical_normal", damping=damping,
                attempt=attempt, seconds=time.monotonic()-tick,
                directBandSolve=True, etaEqualsLambda=True, originalSobolevPreserved=True,
                assembly=augmented.blocks.receipt, **norm_info,
                residualRefinement=refinement, slope=slope,
                predictedFullStepReduction=-2*slope-jv2)
            trace.append(normalrow)
            emit("expanded_polar_normal", **{k: v for k, v in normalrow.items() if k != "assembly"})
            if slope < 0 and -2*slope-jv2 > 0:
                for alpha in (1., .5, .25, .125, .0625, .03125, .015625, .0078125):
                    try:
                        trial, trialgroups = areaop.observe(joint, stream, basis, caches,
                            weights, z+alpha*dz, config, recipe, area)
                        ok = (trial["squaredNorm"] < baseline["squaredNorm"]
                            and trial["squaredNorm"] <= baseline["squaredNorm"]+2e-4*alpha*slope)
                        row = dict(kind="actual_full_nonlinear_trial", damping=damping,
                            alpha=alpha, accepted=bool(ok), **scalar(trial))
                        trace.append(row); emit("expanded_polar_trial", **row)
                        if ok:
                            predicted = -2*alpha*slope-alpha*alpha*jv2
                            gain = (baseline["squaredNorm"]-trial["squaredNorm"])/predicted
                            z, value, groups = z+alpha*dz, trial, trialgroups
                            accepted, selected = True, alpha
                            if alpha == 1 and gain > .75:
                                nextdamping = max(1e-12, damping/3)
                            elif gain < .25 or alpha < 1:
                                nextdamping = min(1e4, 2*damping)
                            else:
                                nextdamping = damping
                            break
                    except (ValueError, ArithmeticError, FloatingPointError) as exc:
                        row = dict(kind="actual_domain_rejection", alpha=alpha, damping=damping,
                            accepted=False, actualValueEvaluated=False, error=str(exc))
                        trace.append(row); emit("expanded_polar_trial", **row)
            if accepted:
                break
            damping = min(1e4, 10*damping)
        attempts += 1
        own += int(accepted)
        if not accepted:
            nextdamping, gain = damping, None
        current = dict(common, z=z.ravel().tolist(), parentStateSHA256=parent_sha,
            newModelInitialSHA256=initial_sha, ownExtendedAcceptedSteps=own,
            ownExtendedAttempts=attempts, accepted=accepted, alpha=selected,
            actualFullDerivativeCheck=checks, dampingUsed=damping,
            nextDamping=nextdamping, actualToPredictedReduction=gain,
            baseline=baseline, evaluation=value, groupValues=groups, trace=trace)
        path = Path(str(prefix) + f"-step{step:02d}-state.json")
        parent_sha = write(path, current)
        outputs.append(dict(path=str(path), SHA256=parent_sha, accepted=accepted,
            ownAcceptedSteps=own, **scalar(value)))
        emit("expanded_polar_state", SHA256=parent_sha, accepted=accepted,
            ownAcceptedSteps=own, nextDamping=nextdamping, seconds=time.monotonic()-started, **scalar(value))
        damping = nextdamping
        del augmented, linear, gradient, dz, jv
        gc.collect()
        if not accepted:
            break
    report = dict(schema=SCHEMA + "-report", modelDefinition=model, modelDefinitionSHA256=model_sha,
        inputStateSHA256=None if args.state is None else sha(args.state),
        warmStateSHA256=None if args.warm_state is None else sha(args.warm_state),
        ownExtendedAcceptedSteps=own, ownExtendedAttempts=attempts,
        outputs=outputs, initialWarmProvenance=provenance,
        actualNewAcceptedSteps=sum(int(row["accepted"]) for row in outputs),
        seconds=time.monotonic()-started, actualOSExitSuppliedByCaller=True,
        continuousMetricCertified=False, wholeClosedReachCertified=False,
        independentThirdObserverComputed=False)
    digest = write(str(prefix) + "-report.json", report)
    emit("expanded_polar_complete", SHA256=digest, ownAcceptedSteps=own, seconds=report["seconds"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scripts", type=Path, required=True)
    ap.add_argument("--prepare-entry", type=Path,
        default=Path(__file__).with_name("2ecf-polar-c2-g10-prepare.py"))
    ap.add_argument("--prepared", type=Path, required=True)
    ap.add_argument("--prefix", type=Path, required=True)
    ap.add_argument("--normal-audit", type=Path, required=True)
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--state", type=Path)
    group.add_argument("--warm-state", type=Path)
    group.add_argument("--zero", action="store_true")
    ap.add_argument("--steps", type=int, default=1)
    ap.add_argument("--initial-damping", type=float, default=1e-4)
    args = ap.parse_args()
    if not 0 <= args.steps <= 20 or not math.isfinite(args.initial_damping) or args.initial_damping <= 0:
        raise ValueError("A finite explicit batch and positive damping are required")
    if args.scripts.parents[2] in args.prefix.resolve().parents:
        raise ValueError("Actual arrays remain outside Git")
    run(args)


if __name__ == "__main__":
    main()
