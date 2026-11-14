#!/usr/bin/env python3
"""Prepared R41 input gates on all109 real outer segment endpoints.

Only previously certified R26 widths are summed. Saved complete Q/Pi
states define explicit angular candidates. At the outer cut the complete
saved H is preserved exactly, instead of silently reusing binary Q at a
different real radius. Optional finite roots produce candidate Khat only;
R41's complete polynomial residual supplies the angular error bound.

No radial integration, fundamental matrix, BVP or Node task is run.
Endpoint certificates are not continuous radial-solution certificates.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_real_head_source_enclosure import exact_q, ball_record
from closure_real_head_green_enclosure import load_json, ball
from closure_real_outer_radius import OuterCell
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_saved_port_norms import FiniteMomentumRoot, point_profile
from tail_r41_connection_polynomial import fields, candidate_K, certify


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("response", "radius-ledger", "ready-reference", "source-topic", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--polynomial-state-index", type=int, action="append", default=[])
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a fresh output for the prepared endpoint calculation")
    ctx.prec = 192
    started = time.monotonic()
    packet, raw = load_json(args.response)
    radius_data, rraw = load_json(args.radius_ledger)
    old_ready, oraw = load_json(args.ready_reference)
    if not packet["response"]["converged"] or radius_data["status"] != "complete":
        raise ValueError("A successful actual response and complete R26 ledger are required")
    if hashlib.sha256(oraw).hexdigest() != radius_data["ready_sha256"]:
        raise ValueError("The real-radius ledger belongs to a different source")
    ready = packet["ready"]
    for key in ("frozenWarpAlpha", "exactSourceConstants"):
        if ready["rationalDeepModel"][key] != old_ready["rationalDeepModel"][key]:
            raise ValueError("The real-source model differs at "+key)
    if ready["shallowSourceParameters"]["cells"] != old_ready["shallowSourceParameters"]["cells"]:
        raise ValueError("The full160 shallow calibration table differs")
    head = SourceValues(ready)
    head.params = ready["rationalDeepModel"]["physicalParameters"]
    geometric = ["rCut", "wCut", "width", "curvatureBound", "delta0", "R",
        "a", "orientation", "prefixR", "prefixEnd", "prefixReturnStart",
        "protectCell", "slopeCap", "capTransition", "capMode", "valleyControls",
        "pulseCaps", "valleyCaps", "warpWeightLevels", "rCuff", "oldCut",
        "epsilonScale", "prefixRByCell"]
    for key in geometric:
        if head.params.get(key) != old_ready["rationalDeepModel"]["physicalParameters"].get(key):
            raise ValueError("Real geometry differs at "+key)
    saved = packet["response"]["checkpoint"]
    cfg = saved["parameters"]
    M, parts = cfg["modes"], cfg["shootingParts"]
    stride = 9*parts
    if (cfg["physicalDepth"] != 12
            or saved["rawNode"] != [stride*n for n in range(13)]
            or len(saved["states"]) != 12*stride+1
            or len(saved["cutHeight"]) != M
            or any(len(row) != 2*M or not all(map(math.isfinite, row))
                   for row in saved["states"])
            or saved["rawStates"] != [saved["states"][i] for i in saved["rawNode"]]):
        raise ValueError("The complete physical state grid is not the expected12 by9 grid")
    cells = {item["cell"]: item for item in radius_data["cells"]}
    if sorted(cells) != list(range(12)):
        raise ValueError("All12 real outer cells are required")
    radii = {12: ball(radius_data["node12"])}
    for n in range(11, -1, -1):
        radii[n] = radii[n+1]+ball(cells[n]["width"])
    rho = (head.a*head.log2).exp()
    modes = [cfg["spacing"]*(j+1) for j in range(M)]
    requested = set(args.polynomial_state_index)
    valid_indices = set(range(0, 12*stride+1, parts))
    if not requested <= valid_indices:
        raise ValueError("Polynomial requests must name original segment endpoints")
    if requested and cfg["orientation"] != 1:
        raise ValueError("The optional diagnostic finite-root helper is orientation+1 only")
    root = (FiniteMomentumRoot(M, cfg["spacing"], cfg["quadrature"],
                               cfg["projectionFloor"]) if requested else None)
    rows = []

    def record(n, j, x, index, radius, momentum_factor):
        cell = OuterCell(head, n)
        w, wr, source = point_profile(cell, cell.segments[j], x)
        mu = head.eps_phys*(head.a*(head.d0*arb(2)**-n).log()).exp()
        state = saved["states"][index]
        if index == 0:
            H = [exact_q(value) for value in saved["cutHeight"]]
            convention = "Complete saved binary cutHeight held fixed at the true real Rout"
        else:
            H = [radius**4*exact_q(value) for value in state[:M]]
            convention = "Saved binary Q defines a candidate height at this true real radius"
        Pi = [momentum_factor*exact_q(value) for value in state[M:]]
        P, G = fields(H, Pi, modes, radius, w, mu, cfg["orientation"])
        certificates = {name: certify(P, G, w, tau) for name, tau in
                        (("tau0", Fraction(0)), ("tau1over64", Fraction(1, 64)))}
        row = dict(state_index=index, source_cell=n, source_segment=j,
            source_x=str(x), radius=ball_record(radius), w=ball_record(w),
            wr=ball_record(wr), mu=ball_record(mu), source_point=source,
            local_momentum_multiplier=ball_record(momentum_factor),
            height_convention=convention, complete_saved_mode_count=M,
            certificates=certificates)
        if index in requested:
            local_state = ([float((height/radius**4).mid()) for height in H]
                           +[float(value.mid()) for value in Pi])
            L, diagnostic = root.solve(local_state, radius=float(radius.mid()),
                w=float(w.mid()), mu=float(mu.mid()))
            Khat = candidate_K(H, L.tolist(), modes, radius, w)
            row["finite_candidate_diagnostic"] = diagnostic
            row["candidate_L_orthonormal_cosine"] = L.tolist()
            row["certificates_with_candidate"] = {
                name: certify(P, G, w, tau, Khat) for name, tau in
                (("tau0", Fraction(0)), ("tau1over64", Fraction(1, 64)))}
        rows.append(row)

    for n in range(12):
        widths = {item["segment"]: ball(item["width"])
                  for item in cells[n]["segments"]}
        if sorted(widths) != list(range(9)):
            raise ValueError("An original segment width is missing")
        for j in range(8, -1, -1):
            radius = radii[n+1]+sum((widths[k] for k in range(j+1)), arb(0))
            index = n*stride+(8-j)*parts
            record(n, j, Fraction(1), index, radius, rho if j == 8 else arb(1))
    record(11, 0, Fraction(0), 12*stride, radii[12], arb(1))
    if [row["state_index"] for row in rows] != sorted(valid_indices):
        raise AssertionError("All109 original endpoints must occur exactly once")
    result = dict(
        status="All109 saved endpoint candidates assessed on the true real source; continuous radial certification remains open",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", rows=rows,
        all_saved_modes_retained=True, exact_cut_height_preserved=True,
        exact_real_momentum_gauge=True, new_radial_integrations=0,
        node_process_started=False, new_BVP=False,
        physical_depth=cfg["physicalDepth"], modes=M,
        whole_radial_solution_certified=False,
        gates_count={key: sum(bool(row["certificates"][key]["full_connection_root_gate"])
                             for row in rows) for key in ("tau0", "tau1over64")},
        input_hashes={str(args.response): hashlib.sha256(raw).hexdigest(),
            str(args.radius_ledger): hashlib.sha256(rraw).hexdigest(),
            str(args.ready_reference): hashlib.sha256(oraw).hexdigest()},
        source_hashes={name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in (Path(__file__).name, "tail_r41_connection_polynomial.py",
                         "tail_outer_saved_port_norms.py", "closure_real_outer_radius.py",
                         "closure_real_head_source_enclosure.py",
                         "tail_r33_middle_ordered_physical.py")},
        finite_root_pinned_source_sha256=hashlib.sha256(
            (args.source_topic/"scripts/78718-tail-fourier-root-momentum.mjs").read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    payload = (json.dumps(result, indent=2)+"\n").encode()
    if args.out.suffix == ".gz":
        payload = gzip.compress(payload, mtime=0)
    elif len(payload) >= 1_000_000:
        raise ValueError("Endpoint ledgers above1MB must use gzip")
    if len(payload) >= 5_000_000:
        raise ValueError("The endpoint ledger exceeds the repository limit")
    args.out.write_bytes(payload)
    print(json.dumps(dict(output=str(args.out), rows=len(rows),
        gates_count=result["gates_count"], seconds=result["elapsed_seconds"],
        RSS_KiB=result["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
