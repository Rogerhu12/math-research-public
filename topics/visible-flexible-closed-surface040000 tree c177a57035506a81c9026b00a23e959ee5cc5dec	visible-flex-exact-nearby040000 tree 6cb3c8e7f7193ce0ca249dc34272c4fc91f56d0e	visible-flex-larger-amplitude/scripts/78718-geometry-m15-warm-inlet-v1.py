#!/usr/bin/env python3
"""Read-only inlet diagnostic of the UNSOLVED saved M15 warm start.

No BVP, tail call, flow integration, parameter update or candidate generation.
The saved first PP value and the literal original initial callback are compared.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import time

for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import numpy as np

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
WARM_SHA = "cbffc43255e1ba4b70dd4f6cf3622a6af249b9efd6bc9fc6e82f6d150e69defc"


def identity(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return dict(path=str(path), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def axes(y, q, reference):
    m = (len(y)-1)//3
    result = {}
    for sigma, label in ((1, "psi_zero"), (-1, "psi_pi_over_3")):
        b = F.from_float(float(y[0]))
        for j in range(1, m+1):
            b += sigma**j*(F.from_float(float(y[j]))+3*j*F.from_float(float(y[m+j])))
        r = F.from_float(float(q))*b/(1-sigma*8*F.from_float(float(reference)))
        g = r*(2+r)
        result[label] = dict(relative_tangent_exact=str(r), G_relative_exact=str(g),
                             G_relative=float(g), abs_above_2e_minus_9=abs(g)>F(1, 500000000))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--linear-port", type=Path, required=True)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    started = time.monotonic()
    cp_id = identity(args.checkpoint)
    if cp_id["sha256"] != WARM_SHA:
        raise ValueError("Not the declared M15 warm start")
    small = json.loads(gzip.decompress(args.checkpoint.read_bytes()))
    if small["solver_success"] or small["status"] != "UNSOLVED_Z_ONLY_HERMITE_INITIAL_GUESS":
        raise ValueError("The intended object is an unsolved saved warm start")
    inputs = [cp_id, identity(args.linear_port)]
    for part in small["pp_coefficient_chunks"]:
        row = identity(args.checkpoint.parent/part["file"])
        if any(row[k] != part[k] for k in ("bytes", "sha256")):
            raise ValueError("Changed PP part")
        inputs.append(row)
    path = HERE/"db6f-prefix-flat-geometry-source.py"
    spec = importlib.util.spec_from_file_location("m15_warm_inlet_loader", path)
    loader = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loader)
    rec, obj, flow, sol = loader.source(args.checkpoint, args.linear_port, args.source_root)
    if not (obj.fixed and obj.M == 15 and obj.base_mode == 3 and rec["chart"]["values"][0] == 1):
        raise ValueError("Unexpected source coordinates")
    p = np.asarray(rec["parameters"], float)
    if not np.array_equal(obj.pscale, np.asarray(rec["central_correction_scales"], float)):
        raise ValueError("Saved normalization scales differ")
    callback = obj.initial(p).copy()
    core = obj._core
    if obj.support_amplitude != rec["actual_primary_amplitude"]:
        raise ValueError("Literal support amplitude replay differs")
    saved = np.asarray(sol.sol.c[-1, 0, :], float).copy()
    if not np.array_equal(saved, sol.sol(0.0)):
        raise ValueError("First PP value convention differs")
    n = 4096
    angular = flow.angular(n)
    b, b1, unused_b2 = flow.basis(n)
    exact = core.evaluate(angular[1])
    fresh = flow.project((exact["F"]-angular[4])[None, :, :], b)[:, 0]/obj.q
    rows = []
    for label, y in (("saved_first_PP_value", saved),
                     ("literal_initial_callback_N2048", callback),
                     ("same_core_reprojected_N4096", fresh)):
        first = angular[5]+flow.values((obj.q*y)[:, None], b1)[0]
        metric = np.sum(first*first, axis=1)/angular[2]**2-1
        rows.append(dict(representation=label, axes=axes(y, obj.q, rec["warp_reference_q"]),
                         G_relative_FFT_l1=float(np.sum(np.abs(np.fft.fft(metric)/n))),
                         G_relative_max_sampled=float(np.max(np.abs(metric)))))
    report = dict(schema="78718-M15-unsolved-warm-inlet-v1", scope=__doc__,
                  input_bindings=inputs, diagnostic_script=identity(__file__),
                  source_loader=identity(path), source_root=str(args.source_root.resolve()),
                  checkpoint_status=rec["status"], checkpoint_solver_success=rec["solver_success"],
                  modes=obj.M, material_base_mode=obj.base_mode, source_nodes=len(rec["mesh"]),
                  gauge_amplitude=obj.q, actual_support_amplitude=obj.support_amplitude,
                  support_coefficient_count=len(core.coefficients),
                  support_coefficients_sha256_little_endian_f64=hashlib.sha256(np.asarray(core.coefficients,dtype="<f8").tobytes()).hexdigest(),
                  literal_saved_parameters_replayed=True, pscale_matches_saved=True,
                  saved_vs_callback_physical_coefficient_max=float(obj.q*np.max(np.abs(saved-callback))),
                  callback_vs_N4096_physical_coefficient_max=float(obj.q*np.max(np.abs(callback-fresh))),
                  angular_metric_diagnostic_samples=n, continuous_FFT_bound=False, rows=rows,
                  BVP_calls=0, tail_calls=0, flow_integrations=0, new_candidate=False,
                  seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n")
    print(json.dumps(dict(status="COMPLETED_READ_ONLY_M15_WARM_INLET", output=identity(args.out),
                          unsolved=True, summaries=[dict(representation=r["representation"],
                          G_relative_FFT_l1=r["G_relative_FFT_l1"],
                          psi_zero=r["axes"]["psi_zero"]["G_relative"],
                          psi_pi_over_3=r["axes"]["psi_pi_over_3"]["G_relative"]) for r in rows],
                          saved_vs_callback=report["saved_vs_callback_physical_coefficient_max"],
                          callback_vs_N4096=report["callback_vs_N4096_physical_coefficient_max"],
                          seconds=report["seconds"]), sort_keys=True))


if __name__ == "__main__":
    main()
