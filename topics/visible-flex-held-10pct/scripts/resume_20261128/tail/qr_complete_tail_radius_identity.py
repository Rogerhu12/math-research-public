#!/usr/bin/env python3
"""Verify only the exact radius-chart identity of one complete unscaled tail.

The complete original v2 seam validator, actual spectrum/shared-node contract,
and the genuine lambda-one complete-prefix-QR source gate remain mandatory. Only the separately
bound final physical-endpoint H is used; the raw candidate is never substituted.
No prefix geometry, BVP, native solve, metric, immersion or embedding proof is
constructed here. A nonidentical cut radius remains a nonidentity chart.
"""
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
import ast
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import resource
import sys
import time
from types import SimpleNamespace
import numpy as np

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
TOPIC = SCRIPTS.parent
sys.path[:0] = [str(SCRIPTS/"resume_20261126"), str(HERE.parent/"tail")]
from seam_export_tail_geometry_v2 import read, sha, ref, checked, bind_height
from seam_certify_tail_geometry_v2 import validate_inputs
from seam_tail_spectrum_v2 import validate_spectrum_container
from seam_cut_height_compatibility import load_packet

REVIEWED_METHODS = {
    ("ActualFiniteTailV2", "__init__"):
        "1998c00898bdcfa33c541313dcc507ab131e774c94bbfa96b0170cd25fd22997",
    ("ActualCutTarget", "__init__"):
        "6454741fcfd69ae551e7442a5ef950b4ecca042ff1bbe043d263a62c930be169",
    ("ActualCutTarget", "perturbation_radius"):
        "7a183a91eac2fb81412e722e76dad82820ca420925ab2f7042be4ffd07049e02",
}


def write(path, record):
    path.write_text(json.dumps(record, indent=2, allow_nan=False)+"\n")


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def exact_binary(value):
    if isinstance(value, (bool, np.bool_)) or not np.isfinite(value):
        raise ValueError("Require a finite real literal radius")
    if isinstance(value, (int, np.integer)):
        return Q(int(value))
    numerator, denominator = value.as_integer_ratio()
    return Q(numerator, denominator)


def complete_height_bytes(value, M):
    result = np.asarray(value, dtype="<f8")
    if result.shape != (M,) or not np.all(np.isfinite(result)):
        raise ValueError("A complete finite height vector is required")
    return result.tobytes()


def require_unscaled(identity):
    if (isinstance(identity.get("factor"), bool)
            or exact_binary(identity["factor"]) != 1
            or identity.get("factor_exact_binary") != "1"
            or identity.get("role") != "unscaled_reference_height_candidate"
            or identity.get("unscaled_reference_request_verified") is not True):
        raise ValueError("The actual tail is warm-scaled; a genuine unscaled factor-one height is required")


def verify_reviewed_radius_source(path):
    text = path.read_text()
    found = {}
    for cls in ast.parse(text).body:
        if not isinstance(cls, ast.ClassDef):
            continue
        for function in cls.body:
            key = (cls.name, getattr(function, "name", None))
            if key in REVIEWED_METHODS:
                found[key] = hashlib.sha256(ast.get_source_segment(text, function).encode()).hexdigest()
    if found != REVIEWED_METHODS:
        raise ValueError("The reviewed complete-tail/radius definition changed; review the new source explicitly")
    return {".".join(key):value for key, value in found.items()}


def prefix_height(source_run, coupling_summary):
    if coupling_summary is None:
        raise ValueError('A genuine lambda-one complete-prefix-QR coupling summary is required')
    from qr_actual_coupled_prefix import accepted_coupled
    record, physical, binding, provenance = accepted_coupled(source_run, coupling_summary)
    del physical
    return record, binding["candidate_H"], dict(
        source_kind="actual_lambda_one_qr_chord_final_physical_height", gate=provenance["adapter"],
        source_run=ref(source_run), raw_candidate_is_height_definition=False,
        coupling_summary=provenance["coupling_summary"],
        endpoint_binding=provenance["endpoint_binding"],
        bound_endpoint_packet=binding["packet"],
        final_physical_height_is_definition=True,
        final_height_bitwise_equal_raw_candidate=provenance["raw_height_bitwise_equal"],
        complete_coupled_gate_provenance=provenance)


def verify(args):
    started = time.monotonic()
    out = args.outdir.resolve()
    out.mkdir(parents=True, exist_ok=False)
    record = dict(schema="actual-complete-tail-radius-identity-v1", status="checking",
        source=ref(__file__), geometry_bundle=ref(args.geometry_bundle),
        source_run=ref(args.source_run), constants=ref(args.constants),
        normalization=ref(args.normalization_certificate),
        radius_chart_identity_proved=False, complete_bundle_validated=False,
        original_tail_metric_reused=False, metric_certificate_executed=False,
        immersion_or_embedding_proved=False, prefix_C2_seam_proved=False,
        complete_surface=False, large_prefix_geometry_constructed=False,
        nonlinear_solves_executed=0)
    try:
        bundle, chain, manifest, index, constants = validate_inputs(
            args.geometry_bundle, args.constants, args.normalization_certificate)
        require_unscaled(bundle["height_identity"])
        if (bundle.get("all_stages_exported") is not True
                or bundle.get("complete_finite_C2_stage_chain") is not True
                or index.get("all_stages_exported") is not True
                or index.get("all_finite_stage_adjacencies_verified") is not True):
            raise ValueError("The entire actual finite stage chain is required")
        source, expected_H, source_gate = prefix_height(args.source_run, args.coupling_summary)
        M = int(source["modes"])
        packet = checked(bundle["accepted_packet"])
        identity = bundle["height_identity"]
        reference_H = checked(identity["reference"])
        for part in identity["reference_key"].split("."):
            reference_H = reference_H[part]
        wanted = complete_height_bytes(expected_H, M)
        for value in (reference_H, packet["request"]["height"],
                      packet["response"]["checkpoint"]["cutHeight"]):
            if complete_height_bytes(value, M) != wanted:
                raise ValueError("The actual unscaled packet is not this source's complete defining H")
        if packet["config"]["modes"] != M:
            raise ValueError("The complete prefix and tail state dimensions differ")
        if (args.coupling_summary is not None
                and bundle["accepted_packet"] != source_gate["bound_endpoint_packet"]):
            raise ValueError("The coupled source requires its actual final physical-endpoint packet")
        port = checked(bundle["source_port"])
        if port["parameters"] != source["physical_tail_parameters"]:
            raise ValueError("The prefix and actual complete tail use different physical parameters")
        closed_path = HERE.parent/"tail/actual_closed_map_v2.py"
        method_hashes = verify_reviewed_radius_source(closed_path)
        closed = module("_radius_actual_closed_definition", closed_path)
        # This actual class revalidates EVERY stage's full spectrum, exact
        # shared two-jets and unreset cumulative mean, and compares the newly
        # computed complete index to the bound canonical index. It constructs
        # no prefix, solves nothing and reads only the selected complete map.
        cap = closed.ActualFiniteTailV2(args.geometry_bundle, out/"verified-node-index.json")
        if (cap.S != index["finite_stage_count"]
                or set(cap.entries) != set(range(cap.S))
                or any(cap.parameters.get(k) != v for k, v in port["parameters"].items())
                or any(cap.parameters.get(k) != v for k, v in constants["parameters"].items())):
            raise ValueError("The complete actual map/background/port definitions differ")
        stage_entry = cap.entries[0]
        stage = checked(stage_entry)
        validate_spectrum_container(stage, bundle["spectrum"], stage=True)
        cut_node = stage["nodes"][-1]
        if (stage["rawCell"] != 0 or stage["rawSegment"] != 8 or stage["rawRight"] != 1
                or cut_node["canonicalNode"] != 0 or cut_node["xi"] != 1
                or cut_node["sourceX"] != 1):
            raise ValueError("The selected endpoint is not the actual outermost stage-0 cut")
        c = exact_binary(cut_node["radiusJS"])
        Rc = exact_binary(cap.parameters["rCut"])
        if (exact_binary(cap.c) != c or Q(index["cut_node"]["R_exact_binary"]) != c
                or exact_binary(constants["parameters"]["rCut"]) != Rc
                or exact_binary(port["parameters"]["rCut"]) != Rc):
            raise ValueError("The actual closed-map fields do not use the same literal radii")
        delta = c-Rc
        record.update(complete_bundle_validated=True, source_kind=source_gate["source_kind"],
            prefix_source_gate=source_gate, height_identity=identity,
            expected_complete_height_sha256=hashlib.sha256(wanted).hexdigest(),
            accepted_packet=bundle["accepted_packet"], spectrum_contract=bundle["spectrum_contract"],
            finite_scope=bundle["finite_scope"], planar_modes=bundle["spectrum"]["planar_modes"],
            height_modes=bundle["spectrum"]["height_modes"],
            full_stage_count=cap.S, all_stage_spectra_and_shared_means_revalidated=True,
            original_canonical_index=bundle["canonical_node_index"],
            independently_recomputed_index=ref(out/"verified-node-index.json"),
            actual_stage0=stage_entry, saved_cut_radius_exact=str(c),
            physical_cut_radius_exact=str(Rc), reparameterization_delta_exact=str(delta),
            closed_map_source=ref(closed_path), reviewed_radius_methods=method_hashes,
            actual_closed_cap_c_exactly_saved_stage0_radius=True,
            current_radius_method_default_width_exact=str(exact_binary(.02)))
        if delta:
            record.update(status="validated_complete_bundle_has_nonidentity_radius_chart",
                radius_chart_identity_proved=False,
                separate_inverse_chart_transfer_required=True,
                R75_outer_radius_domain_c_le_Rc=bool(c <= Rc))
            return record, 2
        # The reviewed method depends only on c and R. This object is an
        # explicit two-scalar radius-evaluator input, NOT a fabricated prefix
        # or a constructed closed-map target. The proof is delta==0 exactly;
        # these numerical calls merely check the same live evaluator's path.
        radius_input = SimpleNamespace(c=cap.c, R=float(cap.parameters["rCut"]))
        numeric_delta = cap.c-np.longdouble(radius_input.R)
        if exact_binary(numeric_delta) != 0:
            raise ArithmeticError("The live radius evaluator did not retain the exact zero delta")
        diagnostics = []
        for R in (np.longdouble(0), np.longdouble(radius_input.R)/2,
                  np.longdouble(radius_input.R)-np.longdouble(.02), np.longdouble(radius_input.R)):
            r, first, second = closed.ActualCutTarget.perturbation_radius(radius_input, R)
            if exact_binary(r) != exact_binary(R) or exact_binary(first) != 1 or exact_binary(second) != 0:
                raise ArithmeticError("The reviewed zero-delta evaluator contradicts its exact formula")
            diagnostics.append(dict(R_exact=str(exact_binary(R)), r_exact=str(exact_binary(r)),
                first_exact=str(exact_binary(first)), second_exact=str(exact_binary(second))))
        record.update(status="complete_unscaled_tail_radius_chart_identity_proved",
            radius_chart_identity_proved=True, live_evaluator_delta_exact="0",
            identity_domain_exact=["0", str(Rc)],
            mathematical_identity="r(R)=R, r'(R)=1, r''(R)=0; the defining real delta c-Rc is exactly zero",
            proof_basis="Literal rational endpoint equality plus the bound reviewed radius formula; not a finite sample inference",
            numerical_radius_function_diagnostics=diagnostics,
            separate_inverse_chart_transfer_required=False)
        return record, 0
    except Exception as error:
        record.update(status="complete_tail_radius_identity_not_verified", error=repr(error))
        return record, 1
    finally:
        record.update(seconds=time.monotonic()-started,
            maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        write(out/"radius-identity.json", record)


def negative_warm(args):
    started = time.monotonic()
    out = args.outdir.resolve()
    out.mkdir(parents=True, exist_ok=False)
    background = TOPIC/"notes/2026-11-20-m3-m24-warm050-execution.json"
    packet, response, _, _, M, _ = load_packet(args.tail_response, args.source_port, background)
    if not 0 < args.warm_factor < 1:
        raise ValueError("This negative check requires a genuinely warm-scaled actual packet")
    warm = bind_height(packet, args.height_reference, args.height_reference_key,
                       args.warm_factor, args.height_arithmetic)
    rejected = {}
    for key, callback in (
            ("actual_warm_identity_rejected_by_unscaled_gate", lambda:require_unscaled(warm)),
            ("same_actual_packet_rejected_for_literal_factor_one", lambda:bind_height(
                packet, args.height_reference, args.height_reference_key, 1., args.height_arithmetic))):
        try:
            callback()
        except ValueError as error:
            rejected[key] = str(error)
        else:
            raise AssertionError("The actual warm source was incorrectly allowed as unscaled: "+key)
    report = dict(status="actual_warm_packet_correctly_rejected_as_unscaled",
        source=ref(__file__), packet=ref(args.tail_response), source_port=ref(args.source_port),
        reference=ref(args.height_reference), actual_warm_height_identity=warm,
        modes=M, original_packet_converged=response["converged"],
        original_packet_residual=response["residual"], rejection_messages=rejected,
        synthetic_packet_or_bundle_created=False, full_height_positive_gate_executed=False,
        complete_bundle_available=False, radius_chart_identity_proved=False,
        full_bundle_positive_verifier_execution_pending=True,
        metric_or_embedding_proved=False, nonlinear_solves_executed=0,
        maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        seconds=time.monotonic()-started)
    write(out/"negative-warm-check.json", report)
    return report, 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    positive = sub.add_parser("verify")
    for key in ("geometry-bundle", "source-run", "constants", "normalization-certificate", "outdir"):
        positive.add_argument("--"+key, type=Path, required=True)
    positive.add_argument("--coupling-summary", type=Path, required=True)
    negative = sub.add_parser("negative-warm-check")
    for key in ("tail-response", "source-port", "height-reference", "outdir"):
        negative.add_argument("--"+key, type=Path, required=True)
    negative.add_argument("--height-reference-key", required=True)
    negative.add_argument("--warm-factor", type=float, required=True)
    negative.add_argument("--height-arithmetic", choices=("python", "numpy"), required=True)
    args = parser.parse_args()
    record, code = verify(args) if args.command == "verify" else negative_warm(args)
    print(json.dumps({key:record[key] for key in ("status", "radius_chart_identity_proved", "seconds")}), flush=True)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
