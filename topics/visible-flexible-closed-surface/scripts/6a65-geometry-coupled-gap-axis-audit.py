#!/usr/bin/env python3
"""Read one accepted new prefix and audit its mirror-axis budget and inlet."""
from __future__ import annotations
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import argparse
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path
import numpy as np
from scipy.integrate import simpson


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scripts-dir", type=Path, required=True)
    ap.add_argument("--prefix", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.output.exists():
        raise FileExistsError("Fresh audit output required")
    started = time.monotonic()
    w = load("coupled_axis_warm", args.scripts_dir/"6a65-geometry-cauchy-unit-t-warm.py")
    prefix = str(args.prefix)
    state_path = Path(prefix+"-accepted-cauchy-states.npz")
    data = np.load(state_path)
    A, B, L, v = (float(data[k]) for k in ("centralA", "centralB", "ramp", "v"))
    candidate = w.p.Candidate(A, B, L, v)
    flow = w.p.hybrid.Hybrid(candidate, 191, 2, 30000)
    axis = flow.work//4
    samples = []
    for s, state in zip(data["s"], data["state"].T):
        values = flow.decode(state)
        f, fp, fpp = (float(x[0]) for x in candidate.profile([float(s)]))
        n, m = (float(values[axis, j]) for j in (0, 1))
        mu = float(flow.derivative(values[:, 1:2])[axis, 0])*flow.a0/float(flow.ell0[axis])
        samples.append(dict(s=float(s), f=f, fp=fp, fpp=fpp, n=n, m=m,
                            mu=mu, signedDensity=f*n*mu, mirrorSquaredDensity=f*fp*m*m))
    midpoint = len(samples)//2
    entry, middle = samples[0], samples[midpoint]
    Jenergy = (middle["f"]**2*middle["n"]**2+middle["fp"]**2-flow.a0**2*entry["n"]**2)/2
    Jquadrature = float(simpson(
        np.array([q["signedDensity"] for q in samples[:midpoint+1]]),
        x=np.array([q["s"] for q in samples[:midpoint+1]]),
    ))
    Jrequired = (.097**2*middle["fpp"]**2+middle["fp"]**2-flow.a0**2*entry["n"]**2)/2
    master = w.WarmMaster(Path(prefix+"-ramp-master.npz"), Path(prefix+"-coast-master.npz"),
                          right_length=.75, coast_length=.02)
    u = 2*np.pi*np.arange(1024)/1024
    phase, tu, tuu = master.angles(u)
    co = master.coefficients[0]
    val = np.einsum("uk,kcj->ucj", phase, co).real
    dt = np.einsum("uk,kcj->ucj", phase, co*(1j*master.wave[:, None, None])).real
    dtt = np.einsum("uk,kcj->ucj", phase, co*(-master.wave[:, None, None]**2)).real
    du = dt*tu[:, None, None]
    duu = dtt*tu[:, None, None]**2+dt*tuu[:, None, None]
    raw = dict(P=val[:, 0], V=val[:, 1], A=val[:, 2], Pu=du[:, 0], Vu=du[:, 1], Puu=duu[:, 0])
    exact = w.ports.central_port(A, B, float(data["centralLength"]), u)
    central_difference = {
        key: float(np.max(np.linalg.norm(raw[key]-exact[key], axis=1))) for key in raw
    }
    out = dict(
        schema="6a65-new-gap-actual-accepted-prefix-axis-and-central-port-audit-v1",
        midpoint=middle,
        entryNormalCurvature=entry["n"],
        energyInferredSignedIntegral=Jenergy,
        recordedGridSimpsonSignedIntegral=Jquadrature,
        differenceIncludesUnboundedQuadratureError=Jquadrature-Jenergy,
        curvatureCapNecessaryIntegralThreshold=Jrequired,
        energyBudgetMarginOverNecessaryThreshold=Jenergy-Jrequired,
        maximumAxisM=float(max(abs(q["m"]) for q in samples)),
        nativeAcceptedCentralPortToExactCylinderTwoJetDifference=central_difference,
        consumerCentralSeamIsExactByDefinition=True,
        zeroCentralDifferenceInMainReportIsDefinitionNotIndependentTest=True,
        stateSHA256=sha(state_path), mainReportSHA256=sha(prefix+"-report.json"),
        scriptSHA256=sha(__file__), seconds=time.monotonic()-started,
        newFieldEvaluations=0, newODEIntegrations=0,
        continuousIntegralCertificate=False,
    )
    args.output.write_text(json.dumps(out, indent=2, allow_nan=False)+"\n")
    print(json.dumps(out, allow_nan=False), flush=True)


if __name__ == "__main__":
    main()
