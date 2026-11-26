#!/usr/bin/env python3
"""One new gap=21/20, v=9/200 Cauchy/R137 prefix.

This consumes the old numerical implementations, not an old field or seed.
It never changes their defaults and never evaluates a right connector.
"""
from __future__ import annotations

import os
for _thread_variable in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_thread_variable] = "1"
import argparse
import hashlib
import importlib.util
import json
import sys
import time
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def emit(value):
    print(json.dumps(value, allow_nan=False), flush=True)


def write(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def difference(left, right):
    return {key: float(np.max(np.linalg.norm(left[key] - right[key], axis=1)))
            for key in ("P", "V", "A", "Pu", "Vu", "Puu")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scripts-dir", type=Path, required=True)
    ap.add_argument("--budget-script", type=Path,
                    default=Path(__file__).with_name("6a65-geometry-central-gap-held-budget.py"))
    ap.add_argument("--output-prefix", type=Path, required=True)
    args = ap.parse_args()
    prefix = args.output_prefix
    if Path(str(prefix) + "-seed.json").exists():
        raise FileExistsError("Fresh complete prefix required")
    prefix.parent.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    budget = load("coupled_gap_exact_budget", args.budget_script)
    w = load("coupled_gap_warm_implementation", args.scripts_dir / "6a65-geometry-cauchy-unit-t-warm.py")
    p, ports, core = w.p, w.ports, w.core
    exactA, exactB = budget.central_box(F(21, 20), denominator=10**17)
    A, B = float(sum(exactA) / 2), float(sum(exactB) / 2)
    c, ramp, v, coast = 13 / 128, .06, .045, .02
    candidate = p.Candidate(A, B, ramp, v)
    target_a0 = float((budget.P0[0] + budget.P0[1]) / 4)
    assert abs(candidate.ellipse.a0 - target_a0) < 5e-13
    seed = dict(
        schema="6a65-new-coupled-gap-exact-definition-numerical-seed-v1",
        exactCentralDefinition="P(A,B)=P(7/5,1/2), A-B=21/20; unique positive solution",
        exactCentralAInterval=[str(x) for x in exactA],
        exactCentralBInterval=[str(x) for x in exactB],
        inheritedGapLengthDesign=dict(centralSeed=dict(
            requestedGap=1.05, actualCentralA=A, actualCentralB=B,
            actualCentralGap=A-B, targetReferenceRadius=target_a0,
        )),
        numericalRadius=candidate.ellipse.a0,
        radiusRoundoffFromReference=candidate.ellipse.a0-target_a0,
        parameters=dict(centralLength=c, rampLength=ramp, v=v, coastLength=coast),
        newGeometryAndMetricDesign=True, oldFieldOrSeedInherited=False,
        exactContinuumCertificate=False,
        scriptSHA256=digest(__file__), budgetSHA256=digest(args.budget_script),
    )
    seed_file = Path(str(prefix) + "-seed.json")
    write(seed_file, seed)
    emit(dict(event="new_seed", centralA=A, centralB=B, a0=candidate.ellipse.a0,
              gap=A-B, v=v, ramp=ramp, coast=coast))
    flow = p.hybrid.Hybrid(candidate, 191, 2, 30000)
    y = flow.initial()
    y[flow.shape_size:].reshape(flow.work, 12)[:, 2] = c
    diagnostic_s = np.linspace(0, ramp, 65)
    sol = solve_ivp(
        flow.rhs, (0, ramp), y, method="DOP853", rtol=2e-12,
        atol=2e-14/(1+flow.active_wave)**2, max_step=.0005, t_eval=diagnostic_s,
    )
    if sol.status != 0 or sol.t[-1] != ramp:
        raise RuntimeError("Actual new Cauchy flow did not reach its endpoint")
    state_file = Path(str(prefix) + "-accepted-cauchy-states.npz")
    np.savez_compressed(state_file, s=sol.t, state=sol.y,
                        centralA=A, centralB=B, centralLength=c, ramp=ramp, v=v)
    rows, coefficients = [], []
    master_indices = set(range(0, len(diagnostic_s), 4))
    for j, (s, state) in enumerate(zip(sol.t, sol.y.T)):
        data = flow.frame(float(s), state)
        native = np.asarray(data["values"], float)
        row = flow.diagnostics(float(s), state)
        Xu = np.asarray(flow.derivative(data["values"][:, 2:5]), float)
        area = np.linalg.norm(np.cross(native[:, 5:8], Xu), axis=1)
        native_scale = float(data["a"]) / candidate.ellipse.a0 * np.asarray(flow.ell0, float)
        row["minimumRelativeArea"] = float(np.min(area/native_scale))
        row["minimumBothHeldDistance"] = min(
            float(np.min(np.linalg.norm(native[:, 2:5] - np.array([0, sign*A, 0]), axis=1)))
            for sign in (-1, 1)
        )
        rows.append(row)
        if j in master_indices:
            l = (native[:, 1]**2 + float(data["K"])) / native[:, 0]
            acc = l[:, None] * native[:, 11:14]
            coefficients.append(np.fft.fft(np.stack((native[:, 2:5], native[:, 5:8], acc), axis=1), axis=0)/flow.work)
    ramp_file = Path(str(prefix) + "-ramp-master.npz")
    np.savez_compressed(
        ramp_file, sx=sol.t[::4], coefficients=np.stack(coefficients),
        wave=np.fft.fftfreq(flow.work, 1/flow.work), centralA=A, centralB=B,
        centralLength=c, a0=candidate.ellipse.a0, ramp=ramp, v=v, modes=191,
    )
    ramp_report = dict(
        status=sol.status, nfev=sol.nfev, rhsCalls=flow.calls,
        nodes=65, masterNodes=17, workAngles=flow.work,
        maximumMetric=max(q["metric"] for q in rows),
        maximumOwnCurvature=max(q["actual_curvature"] for q in rows),
        minimumN=min(q["minimum_n"] for q in rows),
        minimumRelativeArea=min(q["minimumRelativeArea"] for q in rows),
        minimumBothHeldDistance=min(q["minimumBothHeldDistance"] for q in rows),
        maximumProjectionDefect=max(q["projection_defect"] for q in rows),
        rows=rows, finiteCauchyNotExactContinuumSolution=True,
        stateSHA256=digest(state_file), masterSHA256=digest(ramp_file),
    )
    write(str(prefix) + "-ramp-report.json", ramp_report)
    emit({key: value for key, value in dict(event="cauchy_complete", **ramp_report).items()
          if key != "rows"})
    native_end = np.asarray(flow.frame(ramp, sol.y[:, -1])["values"], float)
    raw_curve = core.Curve(native_end[:, 2:5], 95)
    target = float(candidate.profile([ramp])[0][0])
    curve = w.tail.fixed_module.FixedRadiusCurve(raw_curve, target)
    coast_file = Path(str(prefix) + "-coast-master.npz")
    np.savez_compressed(
        coast_file, curve_modes=raw_curve.modes, curve_coefficients=raw_curve.coeff,
        unnormalized_radius=raw_curve.a, exact_target_radius=target,
        v=v, length=coast, degree=95,
    )
    u = 2*np.pi*np.arange(1024)/1024
    data = curve.inlet(u, v)
    terminal = core.propagate(target, v, coast, data)
    k = data["m"]/data["n"]
    ku = data["m_u"]/data["n"] - data["m"]*data["n_u"]/data["n"]**2
    Bfield = v*(1+k*k)-ku
    negative = Bfield < 0
    if np.any(negative):
        wfocus = target/(-Bfield[negative])
        focus = np.hypot(target/v+wfocus, wfocus*k[negative])-target/v
        minimum_focus = float(np.min(focus))
    else:
        minimum_focus = None
    generator = data["e1"]-k[:, None]*data["e2"]
    held_along = []
    for sign in (-1, 1):
        marker = np.array([0, sign*A, 0])
        near_w = np.clip(
            -np.einsum("ij,ij->i", data["X"]-marker, generator)
            /np.einsum("ij,ij->i", generator, generator), 0, terminal["w"],
        )
        nearest = data["X"]+near_w[:, None]*generator
        held_along.append(float(np.min(np.linalg.norm(nearest-marker, axis=1))))
    coast_rows = []
    for sigma in np.linspace(0, coast, 9):
        out = core.at_material(target, v, float(sigma), u, lambda t: curve.inlet(t, v))
        area = np.linalg.norm(np.cross(out["X_s"], out["X_u"]), axis=1)
        coast_rows.append(dict(
            sigma=float(sigma), metric=float(np.max(out["metric"])),
            ownCurvature=float(np.max(out["actual_curvature"])),
            minimumRelativeArea=float(np.min(area/(target+v*sigma))),
            minimumD=float(np.min(out["D"])),
            minimumMaterialDerivative=float(np.min(out["U_t"])),
        ))
    master = w.WarmMaster(ramp_file, coast_file, right_length=.75, coast_length=coast)
    left = master.ramp_port(16, u, repair=False)
    right = master.coast_port(0., u)
    inlet_difference = difference(left, right)
    central_difference = difference(
        master.ramp_port(0, u), ports.central_port(A, B, c, u)
    )
    terminal_port = master.coast_port(coast, u)
    port_file = Path(str(prefix) + "-coast-complete-ports.npz")
    port_arrays = {}
    for side, port in (("left", right), ("right", terminal_port)):
        for key in ("P", "V", "A", "Pu", "Vu", "Au", "Puu", "Vuu", "Auu"):
            port_arrays[side+"_"+key] = port[key]
    np.savez_compressed(port_file, u=u, **port_arrays)
    # The published consumer explicitly repairs the final Hermite cell.
    # Evaluate that actual C2 prefix, including its arclength normalization.
    check_u = 2*np.pi*np.arange(512)/512
    check_s = np.unique(np.r_[0., c, c+np.linspace(0,ramp,33),
                              c+ramp+np.linspace(0,coast,5)])
    repaired_rows = []
    saved = {key: [] for key in ("X", "Xs", "Xu", "Xss", "Xsu", "Xuu", "f", "fs", "fss", "mean", "unitT")}
    for j, s in enumerate(check_s):
        raw = master.jet(float(s), check_u)
        norm = master.normalized(float(s), check_u, 1024)
        rd, nd = ports.diagnostics(raw, A), ports.diagnostics(norm, A)
        rd["minimumRelativeArea"] = rd["minimumArea"]/raw["f"]
        nd["minimumRelativeArea"] = nd["minimumArea"]/norm["f"]
        repaired_rows.append(dict(s=float(s), raw=rd, normalized=nd,
                                  normalizationScale=norm["normalizationScale"]))
        for key in saved:
            saved[key].append(norm[key])
        if j % 12 == 0 or j == len(check_s)-1:
            emit(dict(event="repaired_prefix_sample", index=j, total=len(check_s),
                      s=float(s), metric=nd["maximumRelativeMetric"],
                      curvature=nd["maximumOwnCurvature"]))
    sample_file = Path(str(prefix) + "-repaired-prefix-samples.npz")
    np.savez_compressed(sample_file, s=check_s, u=check_u,
                        **{key: np.asarray(value) for key, value in saved.items()})
    coast_report = dict(
        exactFiniteFourierCurveDegree=95, exactMetricRadiusDefinition="a0+v*ramp/2",
        numericalNormalizationScale=curve.normalization,
        minimumDAlongEachSampledRuling=float(min(target, np.min(terminal["D"]))),
        maximumCurvatureAlongEachSampledRuling=float(max(
            np.max(np.abs(data["n"])*(1+k*k)),
            np.max(np.abs(target*data["n"]*(1+k*k)/terminal["D"])),
        )),
        minimumHeldAlongEachSampledRuling=min(held_along),
        minimumSampledFocus=minimum_focus, minimumInletN=float(np.min(data["n"])),
        maximumAbsMOverN=float(np.max(np.abs(k))), minimumB=float(np.min(Bfield)),
        wholeSigmaPerRulingExtremaUseAffineGenerator=True,
        continuousAngularCertificate=False, angles=1024, rows=coast_rows,
        centralCylinderTwoJetDifference=central_difference,
        actualCauchyToExactCoastTwoJetDifference=inlet_difference,
        completePortSHA256=digest(port_file), masterSHA256=digest(coast_file),
    )
    report = dict(
        schema="6a65-new-coupled-gap105-v045-actual-Cauchy-R137-prefix-v1",
        seed=seed, seedSHA256=digest(seed_file), ramp=ramp_report, coast=coast_report,
        repairedC2Prefix=dict(
            lastCellLength=ramp/16, replacementIsExplicitNewField=True,
            rows=repaired_rows, sampleSHA256=digest(sample_file),
            maximumMetric=max(q["normalized"]["maximumRelativeMetric"] for q in repaired_rows),
            maximumOwnCurvature=max(q["normalized"]["maximumOwnCurvature"] for q in repaired_rows),
            minimumRelativeArea=min(q["normalized"]["minimumRelativeArea"] for q in repaired_rows),
            minimumHeld=min(q["normalized"]["minimumHeld"] for q in repaired_rows),
        ),
        providerSources={name: digest(args.scripts_dir/name) for name in (
            "6a65-geometry-cauchy-unit-t-warm.py",
            "6a65-geometry-central-cauchy-r137.py",
            "fd2d-gc-ellipse-hybrid-flow.py",
            "fd2d-gc-ellipse-flow.py",
            "6a65-geometry-r137-two-connectors.py",
            "6a65-geometry-r137-exact-inlet-consumer.py",
        )},
        scriptSHA256=digest(__file__), seconds=time.monotonic()-started,
        newGeometryAndMetricDesign=True, oldCurvatureOrHeldCertificateInherited=False,
        rightConnectorEvaluations=0, fullClosedSurface=False,
        wholeClosedReachCertified=False, continuousCertificate=False,
        OSExitCode=None, externalExitReceiptRequired=True,
    )
    report_file = Path(str(prefix) + "-report.json")
    write(report_file, report)
    emit(dict(
        event="prefix_complete", outputSHA256=digest(report_file),
        rampMetric=ramp_report["maximumMetric"],
        rampCurvature=ramp_report["maximumOwnCurvature"],
        repairedMetric=report["repairedC2Prefix"]["maximumMetric"],
        repairedCurvature=report["repairedC2Prefix"]["maximumOwnCurvature"],
        coastMinimumD=coast_report["minimumDAlongEachSampledRuling"],
        inletTwoJets=inlet_difference, seconds=report["seconds"],
    ))


if __name__ == "__main__":
    main()
