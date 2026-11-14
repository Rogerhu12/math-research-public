#!/usr/bin/env python3
"""Replay original cell0/segment1 with tighter SAME true capped R48 moments.

The original candidate's old five-moment and bubble enclosures are first
reproduced bitwise by the frozen evaluator. Only then the same real integrals
are intersected with the complete R80 Taylor certificate and the same endpoint
formula is evaluated again. This changes interval enclosures, not the candidate,
metric, endpoints, source leaves, complete mean root, or actual derivative.
Every finite J mode and the R77 zero-mode constraint remain.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import ast
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import types


ORIGINAL_SHA = "b5196622ed649c6e3a3d6ad3227f30b0c54651d402c5866cfa2102d5e6def2d4"
MOMENT_SOURCE_SHA = "88ca736fe426fc3aa9d7f09507aba4f11dd80ea7100dcbec346df6d542b53c6b"


def refine_same_true_moments(args, segment, path, old_moments, old_total,
                             old_candidate, inputs, source_hashes):
    from closure_split_joint_io import read, digest, iter_array
    from closure_real_head_green_enclosure import ball
    from closure_real_head_source_enclosure import ball_record
    from tail_outer_centered_quartic_fields_v2 import finite, intersection
    from tail_outer_positive_moment_panels import MOMENT_KEYS, add_moments, zero_moments
    from tail_outer_weighted_compatible import make_weighted_candidate

    if segment != 1:
        raise ValueError("This completed capped-moment certificate covers original segment1 only")
    meta, resource = map(read, (args.moment_summary, args.moment_resource))
    if (meta["cell"] != 0 or meta["segment"] != segment or not all(meta["gates"].values())
            or resource["exitcode"] != 0 or resource["termination_signal"] is not None):
        raise ValueError("The complete R80 certificate must have a formal successful exit")
    command = resource["command"]
    prefix = command[command.index("--out-prefix")+1]
    if (Path(prefix+"-summary.json") != args.moment_summary
            or Path(prefix+"-resource.json") != args.moment_resource):
        raise ValueError("The moment resource and mathematical result belong to different runs")
    expected_source = Path(__file__).with_name("tail_outer_capped_true_moments.py")
    if digest(expected_source) != MOMENT_SOURCE_SHA:
        raise ValueError("The actual capped moment formula changed")
    for name, checksum in meta["source_hashes"].items():
        if digest(Path(__file__).with_name(name)) != checksum:
            raise ValueError("A completed capped-moment dependency changed: "+name)
        source_hashes[name] = checksum
    for name, checksum in meta["input_hashes"].items():
        if inputs.get(name) != checksum:
            raise ValueError("The refined moments belong to a different original candidate/source")
    source_hashes[Path(__file__).name] = digest(__file__)
    for p in (args.moment_summary, args.moment_resource):
        inputs[str(p)] = digest(p)
    primary = Path(meta["output"])
    if digest(primary) != meta["output_sha256"]:
        raise ValueError("The complete true-moment primary changed")
    inputs[str(primary)] = meta["output_sha256"]

    moments, total, count = [], zero_moments(), 0
    source_rows = iter_array(path, "panels")
    covered, header, trailer = Fraction(0), False, False
    with gzip.open(primary, "rt") as stream:
        for line in stream:
            row = json.loads(line)
            if row["kind"] == "header":
                if header or count or row["input_hashes"] != meta["input_hashes"]:
                    raise ValueError("The actual true-moment header identity is inconsistent")
                if row["source_hashes"] != meta["source_hashes"] or row["segment"] != segment:
                    raise ValueError("The true-moment source/segment identity changed")
                header = True
                continue
            if row["kind"] == "complete_true_local_moment_trailer":
                if not header or trailer or not row["complete_original_piece"]:
                    raise ValueError("The true moment trailer is not a complete original piece")
                if row["counts"] != meta["counts"]:
                    raise ValueError("The true moment complete counts differ")
                trailer = True
                continue
            if not header or trailer or row["kind"] != "complete_true_local_moment_leaf":
                raise ValueError("Unexpected content in the complete true-moment stream")
            old = next(source_rows)
            left, right = Fraction(row["x_left"]), Fraction(row["x_right"])
            if (row["panel"] != count or left != covered or not left < right <= 1
                    or left != Fraction(old["x_left"]) or right != Fraction(old["x_right"])
                    or row["original_parent"] != old["original_parent"]):
                raise ValueError("A refined true integral does not match its complete original leaf")
            at = left
            for part in row["true_partition"]:
                if Fraction(part["left"]) != at or not at < Fraction(part["right"]) <= right:
                    raise ValueError("The real Taylor/root partition is incomplete")
                at = Fraction(part["right"])
            if at != right:
                raise ValueError("A complete old leaf lost a true subinterval")
            intersection(finite(ball(row["width"])), ball(old["width"]))
            values = {key: intersection(finite(ball(row["moments"][key])), old_moments[count][key])
                      for key in MOMENT_KEYS}
            if any(not v > 0 for v in values.values()):
                raise ArithmeticError("A true positive full-leaf moment lost strict positivity")
            moments.append(values)
            total = add_moments(total, values)
            covered, count = right, count+1
    if (not header or not trailer or covered != 1 or count != len(old_moments)
            or count != meta["counts"]["original_leaves"] or next(source_rows, None) is not None):
        raise ValueError("The refined local moment cover is not the complete original piece")
    total = {key: intersection(intersection(total[key], ball(meta["total_local_positive_moments"][key])),
                               old_total[key]) for key in MOMENT_KEYS}
    candidate = make_weighted_candidate(old_candidate["left"], old_candidate["right"], total)
    for mode in candidate["bubble_coefficient"]:
        candidate["bubble_coefficient"][mode] = intersection(
            finite(candidate["bubble_coefficient"][mode]), old_candidate["bubble_coefficient"][mode])
    report = dict(
        complete_refined_integral_count=count,
        original_candidate_enclosures_bitwise_checked_before_refinement=True,
        identical_true_integral_definition_and_shared_two_jets=True,
        actual_capped_source_and_warp_retained=True,
        no_true_integral_midpoint_selection=True,
        total_local_positive_moments={key: ball_record(v) for key,v in total.items()},
        old_bubble_coefficients={str(m): ball_record(v) for m,v in old_candidate["bubble_coefficient"].items()},
        refined_bubble_coefficients={str(m): ball_record(v) for m,v in candidate["bubble_coefficient"].items()},
        certificate=str(args.moment_summary), certificate_sha256=digest(args.moment_summary))
    return moments, total, candidate, report


def main():
    original = Path(__file__).with_name("tail_outer_original_piece_finite_j.py")
    raw = original.read_text()
    if hashlib.sha256(raw.encode()).hexdigest() != ORIGINAL_SHA:
        raise ValueError("The original fully recorded evaluator changed")
    edits = [
        ('    args = parser.parse_args()',
         '    parser.add_argument("--moment-summary", type=Path, required=True)\n'
         '    parser.add_argument("--moment-resource", type=Path, required=True)\n'
         '    args = parser.parse_args()'),
        ('    ctx.prec = 192',
         '    if selected != [1]:\n'
         '        raise ValueError("Use this actual capped certificate only on original segment1")\n'
         '    ctx.prec = 192'),
        ('weights = {m: ((1+m)*(exact_q(tau)*m).exp()).upper() for m in modes}',
         'weights = {m: ((1+m)*(exact_q(tau)*m).exp()).upper() for m in range(0, 2*max(modes)+1, 2)}'),
        ('        output = args.out.with_name(args.out.stem+f"-segment{j}.jsonl.gz")',
         '        moments, total, candidate, refinement = _refine_true_moments(\n'
         '            args, j, path, moments, total, candidate, inputs, source_hashes)\n'
         '        suffix = [zero_moments() for unused in range(len(moments)+1)]\n'
         '        for i in range(len(moments)-1, -1, -1):\n'
         '            suffix[i] = add_moments(moments[i], suffix[i+1])\n'
         '        output = args.out.with_name(args.out.stem+f"-segment{j}.jsonl.gz")'),
        ('                same_whole_piece_candidate=True),',
         '                same_whole_piece_candidate=True, same_true_moment_refinement=refinement),'),
        ('            original_total_moments_and_bubble_enclosures_identical=True,',
         '            original_enclosures_bitwise_checked_before_refinement=True,\n'
         '            same_true_moment_refinement=refinement,'),
        ('            all_original_total_moments_and_bubbles_identical=True,',
         '            original_enclosures_bitwise_checked_before_refinement=True,\n'
         '            complete_same_true_capped_integrals_and_candidate_preserved=True,'),
        ('status="Complete selected original-piece same-candidate finite-J/R77 audit",',
         'status="Complete same-candidate R64/J/R77 replay after true capped-moment refinement",'),
    ]
    transformed = raw
    for before, after in edits:
        if transformed.count(before) != 1:
            raise ValueError("A narrow unchanged-evaluator insertion anchor changed")
        transformed = transformed.replace(before, after)
    reverse = transformed
    for before, after in reversed(edits):
        reverse = reverse.replace(after, before)
    if reverse != raw:
        raise AssertionError("Removing all explicit moment refinements did not recover the old evaluator")
    ast.parse(transformed, filename=str(original))
    module = types.ModuleType("tail_outer_same_capped_moment_replay")
    module.__file__ = str(original)
    module._refine_true_moments = refine_same_true_moments
    exec(compile(transformed, str(original), "exec"), module.__dict__)
    module.__doc__ = __doc__
    module.main()


if __name__ == "__main__":
    main()
