#!/usr/bin/env python3
"""Complete original-panel homogeneous strip budget in fixed optimal frames.

Only the positive constant frame of each existing panel changes. The original
true r, r_x, log(w)_x, widths and source ordering are consumed unchanged.
All frame jumps and both endpoint coordinate conversions are paid, including
frames below one. This does not establish a nonlinear Green or Schur inverse.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_real_head_source_enclosure import exact_q, ball_record
from closure_real_head_green_enclosure import ball
from closure_split_joint_io import read, digest, iter_array
from tail_outer_background_column_flow import analytic_energy_step

HERE = Path(__file__).resolve().parent
FROZEN = {
    "tail_outer_background_column_flow.py": "5b548692afa79035e8ac612c8148de0f4ed2a22e9c40ee7592fa36913156193c",
    "closure_real_head_source_enclosure.py": "97ff78a171b284cd8d5acc8dc233bcfe1f0b7c428ce2fbbd5b7104bd0ecb8c47",
    "closure_split_joint_io.py": "cd03e2fc375e19c8b4d291b601e423a37c584a3e4402957c9f377e82b8cce390",
}


def positive_log(value):
    return max(arb(0), value.log().upper())


def step(row, previous, minimum, old_balance, old_gamma):
    r, rx, ell = (ball(row[k]) for k in ("radius", "radius_x", "log_w_x"))
    s = rx/r
    if not s > 0:
        raise ArithmeticError("The original source ratio is not strictly positive")
    sl, su, el, eu = s.lower(), s.upper(), ell.lower(), ell.upper()
    # The exact minimizer over b >= b_min has this squared value. Rounding
    # produces one exact positive dyadic frame, then its bound is recomputed.
    square = max(minimum*minimum, (eu/su).upper(), (-(el+eu)/(sl+su)).upper())
    candidate = square.sqrt().upper()
    dx = exact_q(F(row["x_right"])-F(row["x_left"]))
    if not dx > 0 or not candidate >= minimum:
        raise ArithmeticError("The original panel or chosen fixed frame is invalid")
    phase = (abs(s*candidate+ell/candidate).upper()*dx/2).upper()
    # Retain the original frame whenever its certified bound is better.
    fallback = not bool(phase <= old_gamma)
    b = old_balance if fallback else candidate
    phase = old_gamma if fallback else phase
    forward = (max((-s-ell).upper(), (-2*ell).upper())*dx).upper()
    backward = (max((s+ell).upper(), (2*ell).upper())*dx).upper()
    if previous is not None:
        forward = (forward+positive_log(previous/b)).upper()
        backward = (backward+positive_log(b/previous)).upper()
    return b, phase, forward, backward, fallback


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cell-manifests", nargs="+", type=Path, required=True)
    parser.add_argument("--old-flow", type=Path, required=True)
    parser.add_argument("--cut-trace", type=Path, required=True)
    parser.add_argument("--out-prefix", type=Path, required=True)
    parser.add_argument("--minimum-frame", default="1/256")
    parser.add_argument("--precision", type=int, default=192)
    parser.add_argument("--rss-kib", type=int, default=40960)
    args = parser.parse_args()
    ctx.prec = args.precision
    started = time.monotonic()
    out = args.out_prefix.with_suffix(".json")
    if out.exists():
        raise FileExistsError("Use a fresh complete-panel output prefix")
    for name, expected in FROZEN.items():
        if digest(HERE/name) != expected:
            raise ValueError("A frozen panel/interval dependency changed: "+name)
    minimum = exact_q(F(args.minimum_frame))
    if not 0 < minimum <= 1:
        raise ValueError("Require a positive fixed minimum frame no greater than one")
    old, cut = read(args.old_flow), read(args.cut_trace)
    manifests = [read(p) for p in args.cell_manifests]
    cells = [v["cell"] for v in manifests]
    if cells != [11, 10] or old["cells_completed"] != cells or old["failure"] is not None:
        raise ValueError("This comparison requires the original complete cells11/10")
    if cut["outer_strip"] != "1/64":
        raise ValueError("The fixed outer strip differs")
    gap = ball(cut["gap"])
    hashes = {str(p): digest(p) for p in args.cell_manifests+[args.old_flow, args.cut_trace]}
    old_records = {row["cell"]: row for row in old["cell_rows"]}
    common_inputs = manifests[0]["original_metadata"]["input_hashes"]
    if any(v["original_metadata"]["input_hashes"] != common_inputs for v in manifests):
        raise ValueError("The original true source/radius identity differs")
    total = {name: [arb(0), arb(0), arb(0)] for name in ("old", "new")}
    previous = {name: None for name in total}
    first = dict(previous)
    all_rows, files, count, fallback_count = [], [], 0, 0

    def memory_gate():
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > args.rss_kib:
            raise MemoryError("The declared observed RSS guard failed")

    memory_gate()
    for manifest in manifests:
        cell = manifest["cell"]
        if not all(manifest["checks"].values()):
            raise ValueError("An original true panel ledger has an unpaid gate")
        sums = {name: [arb(0), arb(0), arb(0)] for name in total}
        cell_count, groups = 0, []
        if sorted(v["source_segment"] for v in manifest["groups"]) != list(range(9)):
            raise ValueError("All nine original source segments are required")
        for group in sorted(manifest["groups"], key=lambda v: v["source_segment"]):
            path = Path(group["path"])
            if digest(path) != group["sha256"] or str(path) not in old["input_hashes"]:
                raise ValueError("An original complete source group changed")
            hashes[str(path)] = group["sha256"]
            segment = group["source_segment"]
            packet = args.out_prefix.with_name(args.out_prefix.name+f"-cell{cell:03d}-seg{segment}-panels.jsonl.gz")
            if packet.exists():
                raise FileExistsError("Never overwrite a completed source-group packet")
            rawhash = hashlib.sha256()
            group_count = 0
            segment_sums = {name: [arb(0), arb(0), arb(0)] for name in total}
            with packet.open("wb") as raw:
                with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0) as gz:
                    for index, row in enumerate(iter_array(path, "panels")):
                        if row["segment"] != segment:
                            raise ValueError("Original source panel order differs")
                        ob, og, of, oi = analytic_energy_step(row, previous["old"])
                        nb, ng, nf, ni, fallback = step(row, previous["new"], minimum, ob, og)
                        fallback_count += int(fallback)
                        if not ng <= og:
                            raise ArithmeticError("The complete-panel phase budget increased")
                        for name, b, values in (("old", ob, [og, of, oi]), ("new", nb, [ng, nf, ni])):
                            if first[name] is None:
                                first[name] = b
                            previous[name] = b
                            for k, value in enumerate(values):
                                sums[name][k] = (sums[name][k]+value).upper()
                                segment_sums[name][k] = (segment_sums[name][k]+value).upper()
                        record = dict(index=index, x_left=row["x_left"], x_right=row["x_right"],
                            original_frame=ball_record(ob), chosen_frame=ball_record(nb),
                            old_phase=ball_record(og), new_phase=ball_record(ng),
                            new_forward_with_jump=ball_record(nf), new_backward_with_jump=ball_record(ni),
                            used_original_frame=fallback)
                        data=(json.dumps(record,separators=(",",":"))+"\n").encode()
                        rawhash.update(data);gz.write(data)
                        count, cell_count, group_count = count+1, cell_count+1, group_count+1
                        if count % 64 == 0:
                            memory_gate()
            if group_count != group["panels"] or packet.stat().st_size >= 5_000_000:
                raise ValueError("The full group count or repository file-size gate failed")
            files.append(dict(path=str(packet), bytes=packet.stat().st_size, sha256=digest(packet),
                              uncompressed_sha256=rawhash.hexdigest(), panels=group_count))
            groups.append(dict(segment=segment, panels=group_count,
                               sums={k: [ball_record(v) for v in values] for k, values in segment_sums.items()}))
            print(json.dumps(dict(event="complete_original_segment",cell=cell,segment=segment,
                                  panels=group_count,seconds=time.monotonic()-started)),flush=True)
        if cell_count != manifest["panels"]:
            raise ValueError("The complete original cell was not consumed")
        for name in total:
            total[name] = [(a+b).upper() for a,b in zip(total[name],sums[name])]
        original_phase = ball(old_records[cell]["all_mode_homogeneous_energy"]["cumulative_phase_upper"])
        if not original_phase.contains(total["old"][0]):
            raise ArithmeticError("The old complete source-phase budget did not reproduce")
        budgets = {}
        for name in total:
            g, f, i = total[name]
            # Both factors are required when a chosen exact frame is below one.
            f = (f+positive_log(1/first[name])+positive_log(previous[name])).upper()
            i = (i+positive_log(1/previous[name])+positive_log(first[name])).upper()
            budgets[name] = dict(cumulative_phase_upper=ball_record(g),
                physical_forward_log_prefactor_upper=ball_record(f),
                physical_backward_log_prefactor_upper=ball_record(i),
                sufficient_strip_gate=bool(g < gap),
                strip_margin=ball_record(gap-g))
        result = dict(cell=cell, panels=cell_count, groups=groups, budgets=budgets,
                      original_complete_phase_reproduced=True)
        all_rows.append(result)
        checkpoint=args.out_prefix.with_name(args.out_prefix.name+f"-completed-cell{cell:03d}.json")
        checkpoint.write_text(json.dumps(result,indent=2)+"\n")
        files.append(dict(path=str(checkpoint),bytes=checkpoint.stat().st_size,sha256=digest(checkpoint)))
        memory_gate()
    result = dict(scope=__doc__, cells=cells, panels=count, requested_panels=sum(v["panels"] for v in manifests),
        rows=all_rows, files=files, original_frame_fallback_panels=fallback_count,
        minimum_frame=args.minimum_frame, true_available_strip_gap=ball_record(gap),
        input_hashes=hashes, source_sha256={**FROZEN,Path(__file__).name:digest(Path(__file__))},
        gates=dict(all_original_panels_consumed=count==old["panels"], original_source_phase_reproduced=True,
            each_panel_phase_not_increased=True, all_frame_jumps_paid=True,
            both_endpoint_coordinate_factors_paid=True, no_source_or_nonlinear_equation_changed=True),
        full_frequency_homogeneous_only=True, nonlinear_Green_or_Schur_inverse_paid=False,
        complete_outer_solution_claimed=False, elapsed_seconds=time.monotonic()-started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if not all(result["gates"].values()):
        raise ArithmeticError("A declared complete-stream identity gate failed")
    out.write_text(json.dumps(result,indent=2)+"\n")
    memory_gate()
    print(json.dumps(dict(event="complete_frame_budget",panels=count,
        new_phase=result["rows"][-1]["budgets"]["new"]["cumulative_phase_upper"]["display"],
        sufficient_strip_gate=result["rows"][-1]["budgets"]["new"]["sufficient_strip_gate"],
        seconds=time.monotonic()-started)),flush=True)


if __name__ == "__main__":
    main()
