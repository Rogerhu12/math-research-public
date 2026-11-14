#!/usr/bin/env python3
"""Build and audit NEW physical-r candidates from true substage moments.

All shared nonmean H/Hr/Hrr data are copied from the original saved-node
candidate.  The polynomial coordinate is now physical radius, so its bubble
and interior field are explicitly NEW.  Complete R64 mean roots, their actual
derivatives, every finite J mode and R77 are checked on the full moment cover.
No PDE second derivative is substituted. No integral or ODE is performed.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_split_joint_io import read, digest
from closure_real_head_green_enclosure import ball
from closure_real_head_source_enclosure import exact_q, ball_record
from tail_outer_weighted_compatible import normalized_endpoint_jet, make_weighted_candidate, MOMENT_KEYS
from tail_outer_centered_quartic_fields_v2 import weighted_panel_fields, intersection, finite
from tail_outer_candidate_domain import nonnegative_integral
from tail_outer_general_mean_bounds import general_mean_and_defect
from tail_outer_substage_span_refinement import (
    finite_complete_J, MINIMUM_FIELDS, compact_ball, rounded_dyadic, atomic_json)
from tail_outer_original_piece_finite_j import r77


EXPECTED = {
    "tail_outer_physical_substage_moments.py": "fff04ec7e4547fc23d00f25ac6794eb5e2429ef14bebbe29c8cd74731e90ff77",
    "tail_outer_original_piece_finite_j.py": "b5196622ed649c6e3a3d6ad3227f30b0c54651d402c5866cfa2102d5e6def2d4",
    "tail_outer_general_mean_bounds.py": "4b16b860eb89d7b8f19d7f8ff05642ea0122b0a2016d4be623d5483430023a5c",
    "tail_outer_substage_span_refinement.py": "85bf30e818e7ab92107a5f5a537225afb9273877327bf6e0092b303b01a1b5d8",
    "tail_outer_weighted_compatible.py": "03c88b010447c78e4fb6bb26f0d3704fafd23510d16cc00084f315daa07f3d1b",
    "tail_outer_centered_quartic_fields_v2.py": "671f6b0c02b3a59dcac79129dc8e73cff4baebe9ec477ee5509e3425f9fb086b",
    "tail_outer_candidate_domain.py": "17d6b7d85be80f8f40b3eec411ae49a73c51c6b624d030df57b94202a7d08690",
}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("candidate", "moment-summary", "moment-resource", "out-prefix"):
        p.add_argument("--" + name, type=Path, required=True)
    p.add_argument("--rss-limit-mib", type=int, default=40)
    a = p.parse_args()
    summary_path = Path(str(a.out_prefix) + "-summary.json")
    recovery_path = Path(str(a.out_prefix) + "-recovery.json")
    if any(path.exists() for path in (summary_path, recovery_path)):
        raise FileExistsError("Use a fresh NEW physical-substage candidate prefix")
    ctx.prec, ctx.threads = 192, 1
    started = time.monotonic()
    inputs = {str(path): digest(path) for path in (a.candidate, a.moment_summary, a.moment_resource)}
    old, meta, usage = read(a.candidate), read(a.moment_summary), read(a.moment_resource)
    if (old["cell"] != 0 or meta["cell"] != 0 or old["segment"] != meta["segment"]
            or not all(old["gates"].values()) or not all(meta["gates"].values())
            or usage["exitcode"] != 0 or usage["termination_signal"] is not None
            or old["modes"] != meta["modes"] or old["tau"] != meta["tau"]
            or old["nodes"] != meta["nodes"]
            or meta["input_hashes"].get(str(a.candidate)) != inputs[str(a.candidate)]
            or not meta["new_candidate_definition"]):
        raise ValueError("Completed true physical moments and all original shared two-jets are required")
    command = usage["command"]
    prefix = command[command.index("--out-prefix") + 1]
    if Path(prefix + "-summary.json") != a.moment_summary:
        raise ValueError("The formal moment exit belongs to another actual run")
    sources = {name: digest(Path(__file__).with_name(name)) for name in EXPECTED}
    if sources != EXPECTED:
        raise ValueError("A frozen numerical source changed")
    for record in (old, meta):
        for path, checksum in record["input_hashes"].items():
            if digest(Path(path)) != checksum:
                raise ValueError("An actual physical moment input changed: " + path)
        for name, checksum in record["source_hashes"].items():
            if digest(Path(__file__).with_name(name)) != checksum:
                raise ValueError("An actual mathematical source changed: " + name)
            sources[name] = checksum
    sources[Path(__file__).name] = digest(__file__)
    modes, tau, nodes, segment = old["modes"], F(old["tau"]), old["nodes"], old["segment"]
    del old
    cutoff = max(modes)
    weights = {m: ((1 + m) * (exact_q(tau) * m).exp()).upper()
        for m in range(0, 2 * cutoff + 1, 2)}
    parts, global_bounds, global_minima = [], {}, {}
    completed = 0
    # Bind the complete requested material set before writing any field
    # header, so every primary has exactly the final common input identity.
    for source_part in meta["parts"]:
        source = Path(source_part["output"])
        if digest(source) != source_part["output_sha256"]:
            raise ValueError("A complete physical moment primary changed")
        inputs[str(source)] = source_part["output_sha256"]

    def memory():
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak > a.rss_limit_mib * 1024:
            raise MemoryError("The NEW physical candidate exceeded its RSS observation gate")
        return peak

    def checkpoint(phase, **extra):
        atomic_json(recovery_path, dict(status="Only complete recorded parts; no whole new segment claim",
            phase=phase, parts=parts, completed_panels=completed, input_hashes=inputs,
            source_hashes=sources, elapsed_seconds=time.monotonic() - started, **extra))

    def endpoint(node, width):
        jets = {key: {int(m): ball(value) for m, value in node["shared_physical_jets"][key].items()}
            for key in ("H", "Hr", "Hrr")}
        w, wr = ball(node["w"]), ball(node["wr"])
        return normalized_endpoint_jet(jets["H"], jets["Hr"], jets["Hrr"],
            w=w, radius_u=width, log_w_u=width * wr / w)

    def accumulate(bounds, minima, values, answer, witness):
        for key, value in values.items():
            value = finite(value).upper()
            if key not in bounds or value > bounds[key]["value"]:
                bounds[key] = dict(value=value, witness=witness)
        for key in MINIMUM_FIELDS:
            value = finite(answer[key]).lower()
            if not value > 0:
                raise ArithmeticError("A complete mean or inverse margin failed")
            if key not in minima or value < minima[key]["value"]:
                minima[key] = dict(value=value, witness=witness)

    def records(table):
        return {key: dict(value=ball_record(row["value"]), witness=row["witness"])
            for key, row in table.items()}

    try:
        for source_part in meta["parts"]:
            k = source_part["part"]
            lo, hi = F(k, 8), F(k + 1, 8)
            if (F(source_part["source_left"]) != lo or F(source_part["source_right"]) != hi
                    or source_part["original_shared_left_node"] != k
                    or source_part["original_shared_right_node"] != k + 1):
                raise ValueError("The physical moment source interval changed")
            width = ball(source_part["true_width"])
            if not width > 0:
                raise ArithmeticError("A physical candidate interval has no positive width")
            candidate = make_weighted_candidate(endpoint(nodes[k], width), endpoint(nodes[k + 1], width),
                {key: ball(source_part["total_true_physical_moments"][key]) for key in MOMENT_KEYS})
            source = Path(source_part["output"])
            if digest(source) != source_part["output_sha256"]:
                raise ValueError("The complete physical primitive/moment primary changed")
            inputs[str(source)] = source_part["output_sha256"]
            output = Path(str(a.out_prefix) + f"-part{k:02d}-fields.jsonl.gz")
            if output.exists():
                raise FileExistsError("Do not overwrite an actual new-candidate primary")
            count, covered, header, trailer = 0, lo, False, False
            bounds, minima = {}, {}
            with gzip.open(source, "rt") as inp, gzip.open(output, "xt", compresslevel=6) as out:
                out.write(json.dumps(dict(kind="header", cell=0, segment=segment, part=k,
                    coordinate="physical r derivatives, r_r=1; source x for complete coverage",
                    NEW_physical_candidate=True, complete_J_cosine_modes=list(range(0, 2 * cutoff + 1, 2)),
                    input_hashes=dict(inputs), source_hashes=sources), separators=(",", ":")) + "\n")
                for line in inp:
                    row = json.loads(line)
                    if row["kind"] == "header":
                        if (header or count or row["input_hashes"] != meta["input_hashes"]
                                or row["source_hashes"] != meta["source_hashes"]
                                or row["part"] != k or not row["NEW_candidate_moments"]):
                            raise ValueError("The physical moment primary header changed")
                        header = True
                        continue
                    if row["kind"] == "trailer":
                        if trailer or not row["complete"] or row["panels"] != count:
                            raise ValueError("The complete physical moment trailer changed")
                        trailer = True
                        continue
                    if (not header or trailer or row["kind"] != "complete_new_physical_substage_moment_leaf"
                            or row["panel"] != count):
                        raise ValueError("An unexpected physical moment record was found")
                    ll, rr = F(row["source_left"]), F(row["source_right"])
                    if ll != covered or not ll < rr <= hi or not ball(row["source_radius_x"]) > 0:
                        raise ValueError("The full source-to-physical interval cover failed")
                    u = intersection(ball(row["u"]), arb(0).union(arb(1)))
                    before = {key: nonnegative_integral(row["prefix_moments"][key]) for key in MOMENT_KEYS}
                    after = {key: nonnegative_integral(row["suffix_moments"][key]) for key in MOMENT_KEYS}
                    H, K, Kr = weighted_panel_fields(candidate, u=u, u_x=1 / width,
                        prefix_moments=before, suffix_moments=after)
                    radius, w, ell = ball(row["radius"]), ball(row["w"]), ball(row["log_w_r"])
                    answer = general_mean_and_defect(H, K, Kr, modes=modes, weights=weights,
                        radius=radius, radius_x=arb(1), w=w, log_w_x=ell)
                    if not answer["gate"]:
                        raise ArithmeticError("A complete new-candidate R64 gate failed: "
                            + str((k, count, answer.get("failure"))))
                    full = finite_complete_J(H, K, Kr, radius=radius,
                        g=dict(w=w, radius_x=arb(1), log_w_x=ell), r64=answer, cutoff=cutoff, weights=weights)
                    values = dict(answer["bounds"], **full["bounds"], **r77(full, answer, w))
                    witness = dict(segment=segment, part=k, panel=count,
                        source_left=str(ll), source_right=str(rr), physical_u=ball_record(u))
                    accumulate(bounds, minima, values, answer, witness)
                    accumulate(global_bounds, global_minima, values, answer, witness)
                    result_row = dict(kind="complete_new_physical_substage_R64_J_R77_leaf", **witness,
                        complete_mean_of_defined_new_candidate=True, actual_derivative_coordinate="physical r",
                        source={key: compact_ball(value) for key, value in (
                            ("radius", radius), ("radius_x", arb(1)), ("w", w), ("log_w_x", ell),
                            ("physical_conversion_factor", full["physical_conversion_factor"]))},
                        bounds_upper={key: rounded_dyadic(value, upper=True) for key, value in values.items()},
                        gates_lower={key: rounded_dyadic(answer[key], upper=False) for key in MINIMUM_FIELDS},
                        full_J_cosine_intervals=[compact_ball(full["coefficients"][m])
                            for m in range(0, 2 * cutoff + 1, 2)],
                        actual_nonmean_jet_cosine_intervals={key: [compact_ball(2 * field[m].real) for m in modes]
                            for key, field in (("H", H), ("Kbar", K), ("Kbar_r", Kr))})
                    out.write(json.dumps(result_row, separators=(",", ":")) + "\n")
                    count, completed, covered = count + 1, completed + 1, rr
                    if count % 64 == 0:
                        checkpoint("complete physical field leaves", active_part=k, active_count=count,
                            active_output=str(output))
                        memory()
                if not (header and trailer and covered == hi and count == source_part["panels"]):
                    raise ValueError("The complete true physical moment cover was not audited")
                out.write(json.dumps(dict(kind="trailer", complete=True, panels=count, part=k,
                    complete_source_and_physical_cover=True), separators=(",", ":")) + "\n")
            if output.stat().st_size >= 5_000_000:
                raise ArithmeticError("The field primary exceeds the file limit")
            parts.append(dict(part=k, source_left=str(lo), source_right=str(hi), panels=count,
                true_width=source_part["true_width"], physical_coordinate="u=(r-r_left)/true_width",
                original_shared_node_indices=[k, k + 1],
                total_true_physical_moments=source_part["total_true_physical_moments"],
                bubble_coefficients={str(m): ball_record(v) for m, v in candidate["bubble_coefficient"].items()},
                bounds=records(bounds), minima=records(minima),
                output=str(output), output_sha256=digest(output), bytes=output.stat().st_size))
            checkpoint("complete new physical candidate part", active_part=k)
            print(json.dumps(dict(event="complete_new_physical_candidate_part", part=k, panels=count,
                Darboux=str(bounds["R77_full_physical_Darboux_upper"]["value"]),
                seconds=time.monotonic() - started, peak_RSS_KiB=memory())), flush=True)
    except BaseException as error:
        checkpoint("failed", error=dict(type=type(error).__name__, message=str(error)))
        raise
    result = dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", scope=__doc__,
        status="Complete requested NEW physical-r shared-jet candidate audits",
        cell=0, segment=segment, modes=modes, tau=str(tau), parts=parts, nodes=nodes,
        first_part=meta["first_part"], stop_part=meta["stop_part"], total_panels=completed,
        whole_segment_candidate_audited=meta["whole_segment_moment_cover"],
        bounds=records(global_bounds), minima=records(global_minima),
        gates=dict(formal_true_physical_moment_exit0_and_all_inputs_checked=True,
            original_shared_physical_two_jets_reused_exactly=True,
            all_requested_physical_source_intervals_complete=True,
            complete_R64_mean_and_its_actual_derivative=True,
            physical_radial_derivatives_not_PDE_substitutes=True,
            every_finite_J_mode_through_twice_height_cutoff=True,
            complete_R77_constraint_every_leaf=True,
            NEW_candidate_not_old_source_x_candidate=True),
        input_hashes=inputs, source_hashes=sources, original_moment_inputs=meta["input_hashes"],
        complete_mean_height="One common free integration constant; full mean roots glue at all retained physical two-jets",
        new_source_evaluation_integral_ODE_or_Node=False, exact_outer_solution_or_Schur_inverse_claimed=False,
        elapsed_seconds=time.monotonic() - started, peak_RSS_KiB=memory())
    with summary_path.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps(dict(event="complete_requested_new_physical_candidates", output=str(summary_path),
        panels=completed, gates=result["gates"], seconds=result["elapsed_seconds"],
        peak_RSS_KiB=result["peak_RSS_KiB"])), flush=True)


if __name__ == "__main__":
    main()
