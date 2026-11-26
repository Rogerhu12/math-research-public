#!/usr/bin/env python3
"""One actual interior finite-difference check of the new window's full jets.

This is an interface check on the declared input, not a whole-field value,
an accepted optimization step, or a continuous error certificate.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import sys
import time
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scripts-dir", type=Path, required=True)
    ap.add_argument("--candidate", type=Path, required=True)
    ap.add_argument("--checkpoint", type=Path, required=True)
    ap.add_argument("--ramp-master", type=Path, required=True)
    ap.add_argument("--coast-master", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    here = Path(__file__).resolve().parent
    source = here/"6a65-geometry-cauchy-short-window.py"
    spec = importlib.util.spec_from_file_location("actual_short_window_check", source)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    oracle = module.ActualCauchyOracle(
        here/"6a65-geometry-cauchy-source-radial-cuts.cjs", args.scripts_dir,
        args.candidate, args.checkpoint)
    started = time.monotonic()
    try:
        master = module.ShortWindowMaster(oracle, args.scripts_dir, args.ramp_master, args.coast_master, .2)
        s, u, h = master.b+.071, np.asarray([.947, 3.641]), 2e-5
        center = master.normalized(s, u, 256)
        radial = {k: master.normalized(s+k*h, u, 256) for k in (-2, -1, 1, 2)}
        angular = {k: master.normalized(s, u+k*h, 256) for k in (-2, -1, 1, 2)}
        def fd(table, key):
            return (-table[2][key]+8*table[1][key]-8*table[-1][key]+table[-2][key])/(12*h)
        def error(actual, expected):
            return dict(absolute=float(np.max(np.linalg.norm(actual-expected, axis=-1))),
                        relative=float(np.max(np.linalg.norm(actual-expected, axis=-1)
                            /np.maximum(1., np.linalg.norm(expected, axis=-1)))))
        checks = dict(
            X_s=error(fd(radial,"X"),center["Xs"]),
            X_ss=error(fd(radial,"Xs"),center["Xss"]),
            X_su_from_s=error(fd(radial,"Xu"),center["Xsu"]),
            X_u=error(fd(angular,"X"),center["Xu"]),
            X_su_from_u=error(fd(angular,"Xs"),center["Xsu"]),
            X_uu=error(fd(angular,"Xu"),center["Xuu"]),
        )
        scalar_checks = dict(
            a_s=abs(float(fd(radial,"f"))-center["fs"]),
            a_ss=abs(float(fd(radial,"fs"))-center["fss"]),
        )
        passed = max(q["relative"] for q in checks.values()) < 2e-6 and max(scalar_checks.values()) < 2e-6
        report = dict(
            schema="6a65-compact-window-normalized-complete-two-jets-direction-check-v1",
            source=oracle.metadata, sourceWasInterfaceProbeOnly=oracle.metadata["interfaceProbeOnly"],
            location=dict(s=s,u=u.tolist()),step=h,quadrature=256,checks=checks,
            naturalPerimeterDerivativeErrors=scalar_checks,allDeclaredChecksPassed=passed,
            sourceSHA256=sha(source),entrySHA256=sha(__file__),
            candidateSHA256=sha(args.candidate),checkpointSHA256=sha(args.checkpoint),
            rampMasterSHA256=sha(args.ramp_master),coastMasterSHA256=sha(args.coast_master),
            oracleMaximumHigherJetConsistency=oracle.maximum_consistency,
            oracleRequests=oracle.counter,actualWholeFieldBaselines=0,actualAcceptedSteps=0,
            continuousCertificate=False,
        )
    finally:
        code = oracle.close()
    report.update(oracleActualOSExitCode=code,seconds=time.monotonic()-started,
                  OSExitCode=None,externalExitReceiptRequired=True)
    args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps({key:value for key,value in report.items() if key!="source"},allow_nan=False),flush=True)
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
