#!/usr/bin/env python3
"""Resample the reported independent extrema from the literal source.

No cached source packet is used in the new values.  Independently assemble
the two fundamental forms, then compute generalized symmetric eigenvalues.
This is a finite source/operator audit, not a continuous certificate.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy.linalg import eigvalsh


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    out = importlib.util.module_from_spec(spec)
    sys.modules[name] = out
    spec.loader.exec_module(out)
    return out


def main():
    ap = argparse.ArgumentParser()
    for key in ("scripts", "prepared", "observer", "state", "observation", "candidate",
                "target-definition", "ramp-master", "coast-master", "output"):
        ap.add_argument("--"+key, type=Path, required=True)
    args = ap.parse_args()
    started = time.monotonic()
    prepare = load(Path(__file__).with_name("2ecf-polar-c2-prefix-prepare.py"), "extreme_prepare")
    consumer = load(Path(__file__).with_name("2ecf-polar-c2-prefix-observe.py"), "extreme_consumer")
    saved, definition, basis, caches, mods, *_ = prepare.validate_prepared(args)
    state = json.loads(args.state.read_text())
    observation = json.loads(args.observation.read_text())
    src = json.loads(args.observer.read_text())
    if (state["preparedSHA256"] != prepare.sha(args.prepared)
            or observation["preparedSHA256"] != prepare.sha(args.prepared)
            or observation["stateSHA256"] != prepare.sha(args.state)
            or observation["sourceObserverSHA256"] != prepare.sha(args.observer)):
        raise ValueError("Audit must use the actual saved state and observed extrema")
    nodes, angles = np.asarray(src["physicalNodes"]), np.asarray(src["angles"])
    raw = np.load(src["files"]["jets"], mmap_mode="r")
    radius = np.load(src["files"]["radius"], mmap_mode="r")
    z = np.asarray(state["z"]).reshape(basis.nb, basis.na)
    rows = []
    with mods["background"].NonfoldPolarBackground(args.scripts, args.candidate,
            args.target_definition, args.ramp_master, args.coast_master) as source:
        if source.metadata != saved["sourceMetadata"]:
            raise ValueError("Literal actual source and g changed")
        for key in ("worstMetric", "worstCurvature"):
            label = observation["statistics"][key]
            s, u = float(label["s"]), float(label["u"])
            si, ui = int(np.argmin(abs(nodes-s))), int(np.argmin(abs(angles-u)))
            if nodes[si] != s or abs(angles[ui]-u) > 1e-14:
                raise ValueError("Reported extreme is not an actual saved physical sample")
            # Consume the original cached floating angle, then additionally
            # report any label addition rounding, rather than silently changing u.
            u = float(angles[ui])
            direct = source.sample(np.array([s]), np.array([u]))
            background = direct["jets"][0, :, 0]
            correction = consumer.direct_packet(basis, np.array([s]), z, np.array([u]))[0, :, 0]
            packet = background+correction
            x, xs, xu, xss, xsu, xuu = packet
            target = float(direct["radius"][0, 0])
            cross = np.cross(xs, xu)
            norm = np.linalg.norm(cross)
            normal = cross/norm
            first = np.array([[xs@xs, xs@xu], [xs@xu, xu@xu]])
            second = np.array([[normal@xss, normal@xsu], [normal@xsu, normal@xuu]])
            scale = np.diag([1., 1./target])
            gram = scale@first@scale
            metric_eigen = np.linalg.eigvalsh(gram-np.eye(2))
            curv = eigvalsh(second, first)
            rows.append(dict(kind=key, s=s, actualPhysicalAngle=u,
                labelAngularRounding=float(label["u"]-u),
                sourceSixJetMaximumAbsoluteDifference=float(np.max(abs(background-raw[si, :, ui]))),
                sourceRadiusJetMaximumAbsoluteDifference=float(np.max(abs(direct["radius"][0]-radius[si]))),
                ownMetricSpectralError=float(np.max(abs(metric_eigen))),
                ownPrincipalCurvatures=curv.tolist(), ownMaximumCurvature=float(np.max(abs(curv))),
                sigma=float(norm/target), normalizedGram=gram.tolist(),
                sourceMeridionalSpeed=float(np.linalg.norm(background[1])),
                correctionMeridionalSpeed=float(np.linalg.norm(correction[1])),
                actualMeridionalSpeed=float(np.linalg.norm(xs)),
                sourceSecondRadialDerivativeNorm=float(np.linalg.norm(background[3])),
                correctionSecondRadialDerivativeNorm=float(np.linalg.norm(correction[3])),
                sameLiteralSourceWithoutInterpolation=True))
    child = source.exit_receipt["targetDefinitionOracle"]
    if child.get("actualOSExitCode") != 0 or child.get("naturalExit") is not True:
        raise ArithmeticError("Actual fresh target source did not naturally exit zero")
    out = dict(schema="2ecf-independent-extreme-literal-resampling-two-forms-v1",
        preparedSHA256=prepare.sha(args.prepared), stateSHA256=prepare.sha(args.state),
        observationSHA256=prepare.sha(args.observation), sourceObserverSHA256=prepare.sha(args.observer),
        entrySHA256=prepare.sha(__file__), sourceExit=source.exit_receipt, extrema=rows,
        finiteSamplesOnly=True, continuousCertificate=False, seconds=time.monotonic()-started)
    digest = prepare.write(args.output, out)
    print(json.dumps(dict(event="actual_extreme_source_audit", SHA256=digest,
        seconds=out["seconds"], extrema=rows)), flush=True)


if __name__ == "__main__":
    main()
