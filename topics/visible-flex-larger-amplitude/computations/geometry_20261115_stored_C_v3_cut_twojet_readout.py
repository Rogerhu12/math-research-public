#!/usr/bin/env python3
"""Actual R286/v3 original-binary-cut two-jet hull; public Actions only.

Read every retained leaf of one actual point query and the complete leaf
stream identity. Exact dyadic comparisons and widths are new readout
arithmetic, not new integrals. No stored finite source or derivative is
relabelled as the explicit continuous-C target. Raw ledgers stay temporary.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import struct
import sys

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R286-v3-original-binary-cut-complete-twojet-hull-v1"
ENTRY_NAME = "geometry_20261115_stored_continuous_E_cover_v3.py"
ENTRY_SHA256 = "f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df"
RESULT_SCHEMA = "R286-original-stored-convention-C-continuous-E-cover-v3"
MODEL_SCHEMA = "R286-original-stored-continuous-model-convention-C-v1"
QUERY_SCHEMA = "R286-original-stored-convention-C-closed-queries-v1"
QUERY_ID = "original-binary-config-cut-point"
FIELDS = ("E", "E_r", "E_rr")
SUMMARY_LIMIT = 90000


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Exact two-jet readout arithmetic only in the named public Actions repository")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(",", ":"), allow_nan=False)+"\n").encode()


def unique(items):
    out = {}
    for key, value in items:
        if key in out:
            raise ValueError("Duplicate JSON key")
        out[key] = value
    return out


def json_value(raw):
    return json.loads(raw, object_pairs_hook=unique,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError("Nonfinite JSON token")))


def file_receipt(path, root=None):
    path = Path(path)
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            digest.update(block)
            size += len(block)
    return dict(file=str(path.relative_to(root)) if root else path.name,
                bytes=size, sha256=digest.hexdigest())


def read_bound(path, expected):
    raw = Path(path).read_bytes()
    if sha(raw) != expected:
        raise ValueError("Actual original file SHA differs: "+str(path))
    data = gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw
    return json_value(data), dict(file=Path(path).name, bytes=len(raw),
        sha256=expected, decoded_bytes=len(data), decoded_sha256=sha(data))


def within(directory, relative):
    relative = PurePosixPath(relative)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("A source descriptor escaped the original result directory")
    path = directory/relative
    if path.is_symlink() or not path.resolve().is_relative_to(directory.resolve()):
        raise ValueError("A source descriptor is not an owned original path")
    return path


def checked_descriptor(directory, desc):
    path = within(directory, desc["file"])
    actual = file_receipt(path, directory)
    if any(actual[key] != desc[key] for key in ("file", "bytes", "sha256")):
        raise ValueError("Original descriptor bytes differ: "+desc["file"])
    return path, actual


def rational(value):
    if type(value) is int:
        return Fraction(value)
    if type(value) is float and math.isfinite(value):
        return Fraction(*value.as_integer_ratio())
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError("Expected an actual finite original scalar or exact rational")


def number_bits(value):
    if type(value) not in (int, float) or not math.isfinite(value):
        raise ValueError("The original config cut must be a finite JSON number")
    return struct.pack("<d", value).hex()


def dyadic(value):
    if not isinstance(value, dict) or set(value) != {"mantissa", "binary_exponent"}:
        raise ValueError("Use a complete producer dyadic endpoint, not its display")
    text = value["mantissa"]
    exponent = value["binary_exponent"]
    if not isinstance(text, str) or re.fullmatch(r"-?(0|[1-9][0-9]*)", text) is None:
        raise ValueError("Invalid dyadic mantissa")
    if type(exponent) is not int:
        raise ValueError("Invalid dyadic exponent")
    return int(text), exponent


def compare(a, b):
    ma, ea = dyadic(a)
    mb, eb = dyadic(b)
    exponent = min(ea, eb)
    left, right = ma << (ea-exponent), mb << (eb-exponent)
    return (left > right)-(left < right)


def interval(value):
    if not isinstance(value, dict) or "lower" not in value or "upper" not in value:
        raise ValueError("The complete original interval endpoints are absent")
    lo, hi = value["lower"], value["upper"]
    if compare(lo, hi) > 0:
        raise ValueError("Reversed original interval")
    return dict(lower=dict(lo), upper=dict(hi))


def hull_add(acc, value):
    value = interval(value)
    if acc is None:
        return value
    return dict(lower=acc["lower"] if compare(acc["lower"], value["lower"]) <= 0 else value["lower"],
                upper=acc["upper"] if compare(acc["upper"], value["upper"]) >= 0 else value["upper"])


def full_width(value):
    lo, elo = dyadic(value["lower"])
    hi, ehi = dyadic(value["upper"])
    exponent = min(elo, ehi)
    numerator = (hi << (ehi-exponent))-(lo << (elo-exponent))
    if numerator < 0:
        raise AssertionError("A full hull width cannot be negative")
    return dict(mantissa=str(numerator), binary_exponent=exponent)


def write_json(path, value):
    raw = canonical(value)
    with Path(path).open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    return dict(file=Path(path).name, bytes=len(raw), sha256=sha(raw))


def arguments(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--result-sha256", required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--config-sha256", required=True)
    parser.add_argument("--query-recipe", type=Path, required=True)
    parser.add_argument("--query-recipe-sha256", required=True)
    parser.add_argument("--out", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv=None):
    args = arguments(argv)
    require_actions()
    directory = args.directory.resolve()
    if args.out.exists():
        raise ValueError("Use a new request-owned output directory")
    for path in (directory, args.config, args.query_recipe):
        if path.resolve().is_relative_to(args.out.resolve()):
            raise ValueError("The new readout must not own an original input")
    result, result_receipt = read_bound(directory/"result.json", args.result_sha256)
    config, config_receipt = read_bound(args.config, args.config_sha256)
    recipe, recipe_receipt = read_bound(args.query_recipe, args.query_recipe_sha256)
    if result["schema"] != RESULT_SCHEMA or result["source_sha256"] != ENTRY_SHA256:
        raise ValueError("Use the actual frozen v3 result")
    if (result["target_model_schema"] != MODEL_SCHEMA
            or result["repository"] != REPOSITORY
            or result["run_id"] != os.environ["GITHUB_RUN_ID"]
            or result["source_commit"] != os.environ["GITHUB_SHA"]):
        raise ValueError("The actual same-run continuous target identity differs")
    if (result["original_real_profile_and_model_C_unchanged"] is not True
            or result["model_choice_is_explicit_and_not_original_finite_output_relabel"] is not True):
        raise ValueError("Do not silently reassign the continuous target")
    if recipe["schema"] != QUERY_SCHEMA or recipe["config_sha256"] != args.config_sha256:
        raise ValueError("Use the actual config-bound original query recipe")
    cut = rational(config["rCut"])
    targets = [row for row in recipe["queries"] if row["id"] == QUERY_ID]
    if len(targets) != 1 or recipe["queries"][0]["id"] != QUERY_ID:
        raise ValueError("The original cut point must be the unique first query")
    target = targets[0]
    if (target["kind"] != "closed-rational-radius-interval"
            or rational(target["left"]) != cut or rational(target["right"]) != cut
            or target.get("left_closed", True) is not True
            or target.get("right_closed", True) is not True):
        raise ValueError("The point query changed the actual binary config cut")
    binding_path, binding_receipt = checked_descriptor(directory, result["input_binding"])
    binding = json_value(binding_path.read_bytes())
    if (binding["schema"] != RESULT_SCHEMA+"-input-binding"
            or binding["source_sha256"] != ENTRY_SHA256
            or binding["config"]["sha256"] != args.config_sha256
            or binding["config"]["bytes"] != config_receipt["bytes"]
            or binding["query_input"]["sha256"] != args.query_recipe_sha256
            or binding["query_input"]["bytes"] != recipe_receipt["bytes"]):
        raise ValueError("The source input binding differs")
    if (number_bits(binding["physical_parameters"]["rCut"]) != number_bits(config["rCut"])
            or binding["convention"]["schema"] != MODEL_SCHEMA
            or binding["convention"]["deep_definition"] != "original-exact-root-family"):
        raise ValueError("Original binary cut or root-family model identity differs")
    for key, role in (("calibration_ledger_sha256", "calibration_ledger"),
                      ("stored_reference_sha256", "stored_reference")):
        if recipe[key] != binding[role]["sha256"]:
            raise ValueError("The point recipe changed an original ready input")
    query_path, query_receipt = checked_descriptor(directory, result["query_results"])
    queries = json_value(query_path.read_bytes())
    if queries["schema"] != RESULT_SCHEMA+"-queries":
        raise ValueError("The complete original query output schema differs")
    found = [row for row in queries["results"] if row["query"]["id"] == QUERY_ID]
    if len(found) > 1:
        raise ValueError("Duplicate actual point-query result")
    point = found[0] if found else None
    if point is not None:
        q = point["query"]
        if (q["index"] != 0 or q["kind"] != "closed-rational-radius-interval"
                or rational(q["left"]) != cut or rational(q["right"]) != cut
                or q["left_closed"] is not True or q["right_closed"] is not True):
            raise ValueError("Actual point-query endpoint identity differs")
    complete = bool(point is not None
        and point.get("complete_closed_domain_bound") is True
        and point.get("domain_containment_proved") is True
        and point.get("continuous_model_family_conditions_proved") is True
        and result["full_finite_head_complete"] is True
        and result["declared_continuous_model_family_conditions_proved"] is True)
    row_span = point.get("leaf_ledger_rows") if point else None
    if complete:
        # This checks the existing domain certificate against its original
        # dyadic lower endpoint; it does not choose a new cut or tolerance.
        denominator = cut.denominator
        if denominator <= 0 or denominator & (denominator-1):
            raise ValueError("The bound original binary cut ceased to be dyadic")
        cut_endpoint = dict(mantissa=str(cut.numerator),
            binary_exponent=-(denominator.bit_length()-1))
        outer = interval(result["natural_outer_radius"])
        if (compare(cut_endpoint, outer["lower"]) > 0
                or cut < rational(binding["physical_parameters"]["rCuff"])):
            raise ValueError("The actual point-domain certificate and its original bounds disagree")
        if (not isinstance(row_span, dict)
                or type(row_span.get("first")) is not int
                or type(row_span.get("stop")) is not int
                or not 0 <= row_span["first"] < row_span["stop"]):
            raise ValueError("A complete point query has no full leaf span")
    leaf_desc = result["ledgers"]["query_inverse_cover"]
    leaf_path = within(directory, leaf_desc["file"])
    digest = hashlib.sha256()
    total_bytes = all_rows = selected_rows = unresolved_rows = 0
    kind_counts = {}
    unions = {key:None for key in FIELDS}
    with leaf_path.open("rb") as stream:
        for raw in stream:
            digest.update(raw)
            total_bytes += len(raw)
            index = all_rows
            all_rows += 1
            if not complete or not row_span["first"] <= index < row_span["stop"]:
                continue
            row = json_value(raw)
            if (row["query_id"] != QUERY_ID
                    or row["entire_possible_inverse_fragment_included"] is not True):
                raise ValueError("Point-query leaf ownership or full inclusion differs")
            if row["kind"] not in ("head", "deep"):
                raise ValueError("Unknown actual source leaf kind")
            if type(row["work_resolution_met"]) is not bool:
                raise ValueError("Preserve the actual work-resolution flag")
            for key in FIELDS:
                unions[key] = hull_add(unions[key], row[key])
            selected_rows += 1
            unresolved_rows += int(not row["work_resolution_met"])
            kind_counts[row["kind"]] = kind_counts.get(row["kind"], 0)+1
    actual_leaf_receipt = dict(file=leaf_desc["file"], bytes=total_bytes,
        rows=all_rows, sha256=digest.hexdigest())
    if any(actual_leaf_receipt[k] != leaf_desc[k] for k in ("file", "bytes", "rows", "sha256")):
        raise ValueError("The complete original leaf stream identity differs")
    if complete:
        if selected_rows != row_span["stop"]-row_span["first"]:
            raise ValueError("The complete point-query leaf span was not read")
        # Re-hulling the original E leaves can avoid an extra display-ball
        # rounding, but it must lie within the original reported E ball.
        original_E = interval(point["E"])
        if (compare(original_E["lower"], unions["E"]["lower"]) > 0
                or compare(original_E["upper"], unions["E"]["upper"]) < 0):
            raise ValueError("The actual leaf E hull escaped the reported query enclosure")
        jet = {key:dict(unions[key], exact_full_width=full_width(unions[key])) for key in FIELDS}
    else:
        jet = None
    report = dict(schema=SCHEMA, source_sha256=sha(Path(__file__).read_bytes()),
        run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        actual_producer=dict(file=ENTRY_NAME,sha256=ENTRY_SHA256,schema=RESULT_SCHEMA),
        target_model_schema=MODEL_SCHEMA,
        continuous_model_choice_is_explicit=True,
        actual_source_result=result_receipt,
        actual_original_config=config_receipt,
        actual_original_query_recipe=recipe_receipt,
        actual_input_binding=binding_receipt,
        actual_query_results=query_receipt,
        complete_original_query_leaf_stream=actual_leaf_receipt,
        original_query_id=QUERY_ID,
        original_binary_cut=dict(source_key="config.rCut",
            float64le_hex=number_bits(config["rCut"]),exact_rational=str(cut),
            query_value_not_renormalised=True),
        actual_point_query=point,
        point_twojet_enclosure_complete=complete,
        same_point_E_Er_Err_enclosures=jet,
        selected_leaf_span=row_span,
        selected_original_leaf_count=selected_rows,
        selected_leaf_kind_counts=kind_counts,
        selected_original_work_resolution_unmet_count=unresolved_rows,
        all_point_leaf_rows_retained_in_hull=complete,
        original_point_domain_certificate_exact_bounds_cross_checked=complete,
        no_derivative_tolerance_gate_added=True,
        derivative_work_resolution_requested_by_original_v3=False,
        original_v3_work_resolution_scope="E-value width only; neither Er nor Err width is a new acceptance test",
        original_root_choice_scope="uniform-for-every-admissible-original-exact-root-sequence",
        original_exact_deep_root_choice_resolved=False,
        original_natural_outer_radius=result["natural_outer_radius"],
        original_natural_outer_radius_minus_nominal_binary_cut=result["natural_outer_radius_minus_nominal_binary_cut"],
        original_source_complete=result["full_finite_head_complete"],
        original_all_query_domain_bounds_complete=result["all_requested_closed_query_bounds_complete"],
        original_all_query_work_resolution_complete=result["numerical_work_resolution_complete"],
        original_unvisited_query_suffix=result["unvisited_query_suffix"],
        original_error=result["error"],
        new_readout_arithmetic=["exact-dyadic-endpoint-comparison","original-point-domain-bound-comparison",
            "complete-point-leaf-hull","exact-full-width"],
        new_integrals_or_ODEs_or_J_or_nonlinear_solves=0,
        actual_finite_selector_or_old_point_derivatives_certified=False,
        actual_accepted_field_or_same_field_metric_threshold_paid=False,
        cut_DN_or_finite_head_linear_transfer_created=False,
        valid_coarse_hulls_not_discarded_for_missing_work_resolution=True,
        raw_leaf_payload_not_copied_to_stdout_or_new_result=True,
        raw_outputs_are_request_owned_temporary_recomputable_data=True,
        unpaid_reason=None if complete else
            "The original same-run point domain/source coverage was not complete; no two-jet hull is fabricated")
    args.out.mkdir(parents=True)
    desc = write_json(args.out/"cut-twojet-readout.json", report)
    summary = dict(report, actual_readout_file=desc)
    raw = canonical(summary)
    if len(raw) > SUMMARY_LIMIT:
        print(json.dumps(dict(event="request144_cut_twojet_summary_over_budget",
            bytes=len(raw),sha256=sha(raw),actual_readout_file=desc,
            full_temporary_result_retained=True,no_mathematical_failure_inferred=True)),flush=True)
        return 70
    print("BEGIN_REQUEST144_ORIGINAL_C_CUT_TWOJET_SUMMARY",flush=True)
    print(raw.decode(),end="",flush=True)
    print("END_REQUEST144_ORIGINAL_C_CUT_TWOJET_SUMMARY",flush=True)
    print(json.dumps(dict(event="request144_cut_twojet_identity",bytes=len(raw),
        sha256=sha(raw),actual_readout_file=desc,
        hash_scope="producer canonical UTF8 JSON including its final LF")),flush=True)
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a") as stream:
            stream.write("cut_twojet_summary="+raw.decode().rstrip("\n")+"\n")
            stream.write("cut_twojet_summary_bytes="+str(len(raw))+"\n")
            stream.write("cut_twojet_summary_sha256="+sha(raw)+"\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
