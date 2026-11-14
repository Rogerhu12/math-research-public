#!/usr/bin/env python3
"""Exact dyadic reread of every row of the captured actual28 native model.

Scientific work runs only in this public repository's Actions. The
frozen band source is imported lazily only for its complete CapturedArrays
identity checks; no factorization, native worker, RK, Jacobian, trial or
floating dot product is executed by this consumer.

Every finite binary64 operand is decoded from its original little-endian
bits as an integer times a power of two. Products and residual sums are
accumulated exactly in the universal unit 2**-2148. Comparisons after
division by the actual positive binary64 sigma use integer cross-products.
The result concerns the saved finite arrays, never an exact derivative of
the underlying nonlinear flow and never a new scientific acceptance gate.
"""
from __future__ import annotations

import argparse
from collections import deque
from concurrent.futures import ProcessPoolExecutor
from decimal import Decimal, localcontext
import gzip
import hashlib
import importlib.util
import json
import math
import multiprocessing
import os
from pathlib import Path
import re
import resource
import struct
import sys
import time


HERE = Path(__file__).resolve().parent
BAND_SOURCE_NAME = "geometry_20261114_native_captured_band_correction.py"
BAND_SOURCE_SHA = "b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390"
CAPTURE_RESULT_SHA = "ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7"
CAPTURE_MANIFEST_SHA = "3ed8c1bf3458f2f5852c5e74ebaec77292233a6b940b494c73e4289bbdf95ae3"
FULL_J_SHA = "394ca2cc7c28ead3ffb963502ad24df86126c32f6e4eef10079495a753320a19"
ORIGINAL_DELTA_SHA = "d3734cf4587acbddbc32c80e49223fc6db4e8077190c8c875c22f218219031f2"
SCHEMA = "captured-native-complete-exact-dyadic-residual-v1"
UNIT_EXPONENT = -2148
FRAC_MASK = (1 << 52)-1
HIDDEN_BIT = 1 << 52
M, K, DEPTH = 112, 224, 576
TOTAL_ROWS = M+DEPTH*K+M
J_PRODUCTS_PER_DIRECTION = DEPTH*K*K


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Exact residual science belongs only to this public repository's Actions")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def read_json(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True,
        separators=(",", ":"), allow_nan=False)+"\n").encode("ascii")


def write_json(path, value, compressed=False):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = json_bytes(value)
    if compressed:
        raw = gzip.compress(raw, mtime=0)
    with path.open("xb") as stream:
        stream.write(raw)
    return dict(file=str(path.name), bytes=len(raw),
        sha256=hashlib.sha256(raw).hexdigest())


def replace_progress(path, value):
    # Only this new output's diagnostic progress file is replaced.
    temporary = Path(path).with_name(Path(path).name+".writing")
    with temporary.open("wb") as stream:
        stream.write(json_bytes(value))
    os.replace(temporary, path)


def same(left, right, label):
    if left != right:
        raise ValueError("Exact residual input binding differs: "+label)


def load_frozen_binding():
    require_actions()
    source = HERE/BAND_SOURCE_NAME
    same(sha(source), BAND_SOURCE_SHA, "frozen original band-reader source")
    spec = importlib.util.spec_from_file_location("_visible_actual28_band_binding", source)
    if spec is None or spec.loader is None:
        raise ImportError("Cannot load the pinned original capture binding")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    same(module.CAPTURE_RESULT_SHA, CAPTURE_RESULT_SHA, "actual28 result")
    same(module.CAPTURE_MANIFEST_SHA, CAPTURE_MANIFEST_SHA, "actual28 raw manifest")
    same(module.FULL_J_SHA, FULL_J_SHA, "actual28 whole Jacobian bytes")
    return module


def read_raw_array(capture, name):
    """Read/hash the original raw bytes without conversion through floats."""
    entry = capture.arrays[name]
    pieces, h, total = [], hashlib.sha256(), 0
    for descriptor in entry["chunks"]:
        path = capture.directory/descriptor["file"]
        raw = path.read_bytes()
        same(len(raw), descriptor["bytes"], "raw reread size "+name)
        same(hashlib.sha256(raw).hexdigest(), descriptor["raw_sha256"],
            "raw reread hash "+name)
        pieces.append(raw)
        h.update(raw)
        total += len(raw)
    same(total, entry["total_bytes"], "complete raw reread bytes "+name)
    same(h.hexdigest(), entry["raw_sha256"], "complete raw reread hash "+name)
    return b"".join(pieces)


def stage_bytes(capture):
    expected, total, h = 0, 0, hashlib.sha256()
    size = K*K*8
    for descriptor in capture.arrays["stage-jacobians"]["chunks"]:
        raw = (capture.directory/descriptor["file"]).read_bytes()
        same(len(raw), descriptor["bytes"], "J chunk reread bytes")
        same(hashlib.sha256(raw).hexdigest(), descriptor["raw_sha256"],
            "J chunk reread hash")
        h.update(raw); total += len(raw)
        for stage in range(descriptor["row_start"], descriptor["row_stop"]):
            same(stage, expected, "original complete stage order")
            start = (stage-descriptor["row_start"])*size
            value = raw[start:start+size]
            same(len(value), size, "one complete original J stage")
            yield stage, value
            expected += 1
    same(expected, DEPTH, "every original J stage visited")
    same(total, DEPTH*size, "every original J byte reread")
    same(h.hexdigest(), FULL_J_SHA, "whole original J reread hash")


def decode_bits(word):
    """Exactly x=m*2**e. Signed zeros represent the same real zero."""
    exponent = (word >> 52) & 0x7ff
    if exponent == 0x7ff:
        raise ValueError("An exact real residual needs finite binary64 operands; bits="+f"{word:016x}")
    mantissa = word & FRAC_MASK
    if exponent:
        mantissa |= HIDDEN_BIT
        power = exponent-1075
    else:
        power = -1074
    if word >> 63:
        mantissa = -mantissa
    return mantissa, power


def decoded_array(raw, count, label):
    same(len(raw), count*8, "decoded input byte count "+label)
    values = []
    for index, (word,) in enumerate(struct.iter_unpack("<Q", raw)):
        try:
            values.append(decode_bits(word))
        except ValueError as error:
            raise ValueError(label+" index "+str(index)+": "+str(error)) from None
    same(len(values), count, "all binary64 words decoded "+label)
    return tuple(values)


def unit_value(pair):
    mantissa, exponent = pair
    return mantissa << (exponent-UNIT_EXPONENT)


def compact_unit(value):
    """Canonical signed odd hex coefficient and its binary exponent."""
    if value == 0:
        return ["0x0", 0]
    absolute = abs(value)
    trailing = (absolute & -absolute).bit_length()-1
    return [hex(value >> trailing), UNIT_EXPONENT+trailing]


def sigma_denominator(word):
    mantissa, exponent = decode_bits(word)
    if mantissa <= 0:
        raise ValueError("Every actual original sigma must be strictly positive")
    # e/sigma=(integer*2^-2148)/(m_sigma*2^e_sigma).
    return mantissa << (exponent-UNIT_EXPONENT)


def fraction_record(numerator, denominator):
    if denominator <= 0:
        raise ValueError("Positive exact denominator required")
    divisor = math.gcd(abs(numerator), denominator)
    n, d = numerator//divisor, denominator//divisor
    with localcontext() as context:
        context.prec = 72
        display = format(Decimal(n)/Decimal(d), ".63E")
    return dict(numerator=str(n), denominator=str(d),
        decimal_display_64_significant_digits=display,
        display_never_used_for_comparison=True)


def row_order(kind, node, row):
    if kind == "cut":
        return row
    if kind == "stage":
        return M+node*K+row
    if kind == "far":
        return M+DEPTH*K+row
    raise ValueError("Unknown original row kind")


def max_record(kind, node, row, value, sigma_word):
    denominator = sigma_denominator(sigma_word)
    return dict(kind=kind, node=node, row=row,
        global_equation_row=row_order(kind, node, row),
        component=("Q" if row < M else "Pi") if kind == "stage"
            else "Q" if kind == "cut" else "Pi-minus-original-GQ",
        mode=(row % M)+1 if kind == "stage" else row+1,
        original_sigma_float64le_hex=struct.pack("<Q", sigma_word).hex(),
        exact_unscaled_dyadic=compact_unit(value),
        exact_signed_scaled_residual=fraction_record(value, denominator),
        exact_absolute_scaled_residual=fraction_record(abs(value), denominator),
        _integer=value, _denominator=denominator)


def better(candidate, incumbent):
    if incumbent is None:
        return True
    left = abs(candidate["_integer"])*incumbent["_denominator"]
    right = abs(incumbent["_integer"])*candidate["_denominator"]
    return left > right or (left == right and
        candidate["global_equation_row"] < incumbent["global_equation_row"])


def public_record(value):
    if isinstance(value, dict):
        return {key:public_record(child) for key, child in value.items()
            if not key.startswith("_")}
    if isinstance(value, (list, tuple)):
        return [public_record(child) for child in value]
    return value


def stage_job(task):
    """One exact full K-by-K stage, shared J decoding for all directions."""
    require_actions()
    stage, raw, residuals, direction_rows = (
        task["stage"], task["J"], task["residuals"], task["directions"])
    same(len(raw), K*K*8, "worker's full original J bytes")
    labels = list(direction_rows)
    next_rows = [direction_rows[label][1] for label in labels]
    current_rows = [direction_rows[label][0] for label in labels]
    all_rows = {label:[] for label in labels}
    maximum = {label:(None, None) for label in labels}
    nonzero_products = {label:0 for label in labels}
    base_maximum = (None, None)
    words = struct.iter_unpack("<Q", raw)
    j_nonzero, j_negative_zero = 0, 0
    for row in range(K):
        residual_integer = unit_value(residuals[row])
        if base_maximum[0] is None or abs(residual_integer) > abs(base_maximum[0]):
            base_maximum = (residual_integer, row)
        accumulators = [residual_integer-unit_value(current[row])
            for current in current_rows]
        for column in range(K):
            word = next(words)[0]
            try:
                jm, je = decode_bits(word)
            except ValueError as error:
                raise ValueError(f"J stage {stage} row {row} column {column}: {error}") from None
            if word == (1 << 63):
                j_negative_zero += 1
            if jm:
                j_nonzero += 1
                for index, label in enumerate(labels):
                    dm, de = next_rows[index][column]
                    if dm:
                        accumulators[index] += (jm*dm) << (je+de-UNIT_EXPONENT)
                        nonzero_products[label] += 1
        for label, value in zip(labels, accumulators):
            all_rows[label].append(compact_unit(value))
            previous = maximum[label][0]
            if previous is None or abs(value) > abs(previous):
                maximum[label] = (value, row)
    if next(words, None) is not None:
        raise ValueError("Unexpected extra J words after the full stage")
    return dict(stage=stage, J_stage_raw_sha256=hashlib.sha256(raw).hexdigest(),
        J_words_visited=K*K, J_nonzero_words=j_nonzero,
        J_negative_zero_words=j_negative_zero, base_maximum=base_maximum,
        directions={label:dict(rows=all_rows[label],
            maximum_integer=maximum[label][0], maximum_row=maximum[label][1],
            original_product_positions=K*K,
            nonzero_exact_integer_products=nonzero_products[label])
            for label in labels})


def boundary_job(kind, residuals, direction_pairs, far_graph):
    require_actions()
    labels = list(direction_pairs)
    results = {label:dict(rows=[], maximum_integer=None, maximum_row=None,
        original_product_positions=0, nonzero_exact_integer_products=0) for label in labels}
    base_maximum = (None, None)
    for row in range(M):
        base = unit_value(residuals[row])
        if base_maximum[0] is None or abs(base) > abs(base_maximum[0]):
            base_maximum = (base, row)
        for label in labels:
            direction = direction_pairs[label]
            if kind == "cut":
                value = unit_value(direction[row])+base
            elif kind == "far":
                qm, qe = direction[row]
                gm, ge = far_graph[row]
                product = (gm*qm) << (ge+qe-UNIT_EXPONENT)
                value = unit_value(direction[M+row])-product+base
                results[label]["original_product_positions"] += 1
                if gm and qm:
                    results[label]["nonzero_exact_integer_products"] += 1
            else:
                raise ValueError("Unknown original boundary kind")
            results[label]["rows"].append(compact_unit(value))
            old = results[label]["maximum_integer"]
            if old is None or abs(value) > abs(old):
                results[label]["maximum_integer"] = value
                results[label]["maximum_row"] = row
    return dict(base_maximum=base_maximum, directions=results)


def bind_band_direction(module, capture, directory, expected_result_sha):
    if not directory or not expected_result_sha or not re.fullmatch(r"[0-9a-f]{64}", expected_result_sha):
        raise ValueError("A new band direction needs its actual directory and explicit result SHA256")
    directory = Path(directory).resolve()
    same(sha(directory/"result.json"), expected_result_sha, "actual new band result bytes")
    result = read_json(directory/"result.json")
    if (result.get("schema") != "original-captured-native-full-band-correction-v1"
            or result.get("source_sha256") != BAND_SOURCE_SHA
            or result.get("capture_result_sha256") != CAPTURE_RESULT_SHA
            or result.get("linear_direction_computed") is not True
            or result.get("native_accepted") is not False
            or result.get("task_completed") is not False
            or result.get("original_native_calls") != 0
            or result.get("new_J_calls") != 0 or result.get("nonlinear_trials") != 0
            or result.get("scaling") not in ("none", "original-sigma")):
        raise ValueError("Require an actually computed complete direction from the frozen original band source")
    same(read_json(directory/"input-binding.json"), capture.binding,
        "same complete original capture binding")
    manifest_descriptor = result["array_manifest"]
    manifest_path = module.safe_file(directory, manifest_descriptor["file"])
    same(manifest_path.stat().st_size, manifest_descriptor["bytes"], "band array-manifest bytes")
    same(sha(manifest_path), manifest_descriptor["sha256"], "band array-manifest hash")
    manifest = read_json(manifest_path)
    same(manifest.get("source_sha256"), BAND_SOURCE_SHA, "band array producer")
    same(manifest.get("capture_result_sha256"), CAPTURE_RESULT_SHA, "band array capture")
    same((result.get("M"), result.get("K"), result.get("depth")),
        (M, K, DEPTH), "band complete original layout")
    descriptor = result["new_delta"]
    matches = [entry for entry in manifest["arrays"]
        if entry.get("name") == "complete-original-coordinate-delta"]
    if len(matches) != 1 or matches[0] != descriptor:
        raise ValueError("The restored complete band direction is not uniquely bound by the manifest")
    same(descriptor.get("dtype"), "<f8", "band original-coordinate dtype")
    same(descriptor.get("order"), "C", "band original-coordinate order")
    same(descriptor.get("shape"), [DEPTH+1, K], "every restored native coordinate")
    same(descriptor.get("bytes"), (DEPTH+1)*K*8, "full restored direction bytes")
    path = module.safe_file(directory, descriptor["file"])
    raw = path.read_bytes()
    same(len(raw), descriptor["bytes"], "actual restored direction byte count")
    same(hashlib.sha256(raw).hexdigest(), descriptor["sha256"], "actual restored direction SHA")
    return raw, dict(kind="actual-restored-band-direction",
        band_result_sha256=expected_result_sha, band_source_sha256=BAND_SOURCE_SHA,
        band_array_manifest_sha256=manifest_descriptor["sha256"],
        band_scaling=result["scaling"], original_coordinate_delta=descriptor,
        band_diagnostic_completed=result.get("diagnostic_completed"),
        no_band_scaled_coordinate_vector_substituted=True,
        native_acceptance_not_asserted=True)


def stage_raw_for_witness(capture, stage):
    size = K*K*8
    for descriptor in capture.arrays["stage-jacobians"]["chunks"]:
        if descriptor["row_start"] <= stage < descriptor["row_stop"]:
            raw = (capture.directory/descriptor["file"]).read_bytes()
            same(hashlib.sha256(raw).hexdigest(), descriptor["raw_sha256"], "witness J chunk")
            start = (stage-descriptor["row_start"])*size
            return raw[start:start+size]
    raise ValueError("The exact global witness has no original J stage")


def worst_witness(capture, record, direction_raw, inputs):
    kind, node, row = record["kind"], record["node"], record["row"]
    if kind == "stage":
        J = stage_raw_for_witness(capture, node)
        return dict(equation="sum_j J[n,i,j]*delta[n+1,j] - delta[n,i] + r[n,i]",
            full_original_J_row_float64le_hex=J[row*K*8:(row+1)*K*8].hex(),
            full_next_delta_float64le_hex=direction_raw[(node+1)*K*8:(node+2)*K*8].hex(),
            current_delta_float64le_hex=direction_raw[(node*K+row)*8:(node*K+row+1)*8].hex(),
            original_residual_float64le_hex=inputs["stage-residuals"][(node*K+row)*8:(node*K+row+1)*8].hex(),
            original_sigma_float64le_hex=inputs["original-scales"][node*8:(node+1)*8].hex(),
            original_J_stage_sha256=hashlib.sha256(J).hexdigest(),
            original_stage_location=capture.live["stages"][node])
    if kind == "cut":
        return dict(equation="delta[0,Q,i] + captured_cut_residual[i]",
            current_delta_float64le_hex=direction_raw[row*8:(row+1)*8].hex(),
            original_residual_float64le_hex=inputs["cut-residual"][row*8:(row+1)*8].hex(),
            original_sigma_float64le_hex=inputs["original-scales"][:8].hex())
    start = DEPTH*K
    return dict(equation="delta[N,Pi,i] - original_far_G[i]*delta[N,Q,i] + captured_far_residual[i]",
        delta_Pi_float64le_hex=direction_raw[(start+M+row)*8:(start+M+row+1)*8].hex(),
        original_far_G_float64le_hex=inputs["original-far-graph"][row*8:(row+1)*8].hex(),
        delta_Q_float64le_hex=direction_raw[(start+row)*8:(start+row+1)*8].hex(),
        original_residual_float64le_hex=inputs["end-residual"][row*8:(row+1)*8].hex(),
        original_sigma_float64le_hex=inputs["original-scales"][DEPTH*8:(DEPTH+1)*8].hex())


def main():
    require_actions()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture-directory", type=Path, required=True)
    parser.add_argument("--capture-result-sha256", default=CAPTURE_RESULT_SHA)
    parser.add_argument("--which", choices=("original", "band", "both"), default="original")
    parser.add_argument("--band-directory", type=Path)
    parser.add_argument("--expected-band-result-sha256")
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if not 1 <= args.workers <= 8:
        raise ValueError("Use an explicit finite worker count between1 and8")
    same(args.capture_result_sha256, CAPTURE_RESULT_SHA, "actual28 complete capture result")
    out = args.out.resolve()
    if os.path.lexists(args.out) or out.exists():
        raise ValueError("Use a new independent exact-residual output directory")
    if out.is_relative_to(args.capture_directory.resolve()):
        raise ValueError("The exact output must be independent of the read-only input capture")
    if args.band_directory is not None and out.is_relative_to(args.band_directory.resolve()):
        raise ValueError("The exact output must be independent of the input band artifact")
    out.mkdir(parents=True)
    started = time.monotonic()
    report = dict(schema=SCHEMA, source_sha256=sha(__file__),
        frozen_binding_source_sha256=BAND_SOURCE_SHA,
        exact_complete_residual_finished=False, native_accepted=False, task_completed=False,
        original_native_calls=0, new_J_calls=0, nonlinear_trials=0,
        floating_dot_products_for_residuals=0,
        scientific_acceptance_gate_added=False,
        exact_derivative_of_original_flow_claimed=False,
        original_rows_expected=TOTAL_ROWS, original_stage_product_positions_per_direction=J_PRODUCTS_PER_DIRECTION,
        M=M, K=K, depth=DEPTH, workers=args.workers,
        universal_exact_unit_binary_exponent=UNIT_EXPONENT)
    completed_stages, records = 0, []
    pool, ledger = None, None
    try:
        module = load_frozen_binding()
        capture = module.CapturedArrays(args.capture_directory, args.capture_result_sha256)
        same((capture.M, capture.K, capture.depth), (M, K, DEPTH), "complete original native layout")
        write_json(out/"capture-input-binding.json", capture.binding)
        input_names = ("stage-residuals", "cut-residual", "end-residual",
            "original-scales", "original-far-graph")
        inputs = {name:read_raw_array(capture, name) for name in input_names}
        residuals = decoded_array(inputs["stage-residuals"], DEPTH*K, "all stage residuals")
        cut = decoded_array(inputs["cut-residual"], M, "all cut residuals")
        far = decoded_array(inputs["end-residual"], M, "all far residuals")
        far_graph = decoded_array(inputs["original-far-graph"], M, "complete original diagonal far graph")
        same(len(inputs["original-scales"]), (DEPTH+1)*8, "all original sigma words")
        sigma_words = tuple(word for (word,) in struct.iter_unpack("<Q", inputs["original-scales"]))
        for word in sigma_words:
            sigma_denominator(word)
        raw_directions, direction_binding = {}, {}
        if args.which in ("original", "both"):
            raw = read_raw_array(capture, "original-delta")
            same(hashlib.sha256(raw).hexdigest(), ORIGINAL_DELTA_SHA, "complete original correction")
            raw_directions["original"] = raw
            direction_binding["original"] = dict(kind="actual28-original-correction",
                raw_sha256=ORIGINAL_DELTA_SHA, bytes=len(raw),
                source="complete original captured original-delta array")
        if args.which in ("band", "both"):
            raw, binding = bind_band_direction(module, capture,
                args.band_directory, args.expected_band_result_sha256)
            raw_directions["band"] = raw
            direction_binding["band"] = binding
        decoded = {label:decoded_array(raw, (DEPTH+1)*K, "all "+label+" direction coordinates")
            for label, raw in raw_directions.items()}
        labels = list(decoded)
        model = dict(schema=SCHEMA, exact_consumer_sha256=report["source_sha256"],
            frozen_binding_source_sha256=BAND_SOURCE_SHA, capture_binding=capture.binding,
            original_raw_array_sha256={name:capture.arrays[name]["raw_sha256"] for name in input_names},
            full_original_J_sha256=FULL_J_SHA,
            directions={label:dict(binding=direction_binding[label],
                raw_sha256=hashlib.sha256(raw_directions[label]).hexdigest(),
                bytes=len(raw_directions[label]), dtype="<f8", order="C", shape=[DEPTH+1,K])
                for label in labels},
            row_order="cut M; depth complete K-row stages; far M",
            original_sigma_by_equation="cut sigma0; stage n sigma_n; far sigma_N")
        model_sha = hashlib.sha256(json_bytes(model)).hexdigest()
        report["exact_model_sha256"] = model_sha
        report["input_model"] = write_json(out/"exact-input-model.json", model)
        global_max = {label:None for label in labels}
        node_max = {label:[None]*(DEPTH+1) for label in labels}
        base_global = None
        base_node = [None]*(DEPTH+1)
        positions = {label:0 for label in labels}
        multiplications = {label:0 for label in labels}
        rows_seen = {label:0 for label in labels}
        J_words_seen, J_negative_zeros = 0, 0
        ledger = (out/"completed-exact-blocks.jsonl").open("x", encoding="ascii")

        def consume(kind, node, result, J_stage_sha=None):
            nonlocal base_global
            sigma_word = sigma_words[node]
            base_value, base_row = result["base_maximum"]
            br = max_record(kind, node, base_row, base_value, sigma_word)
            if better(br, base_global):
                base_global = br
            if better(br, base_node[node]):
                base_node[node] = br
            row_count = K if kind == "stage" else M
            for label in labels:
                data = result["directions"][label]
                same(len(data["rows"]), row_count, "every exact result row")
                mr = max_record(kind, node, data["maximum_row"],
                    data["maximum_integer"], sigma_word)
                if better(mr, global_max[label]):
                    global_max[label] = mr
                if better(mr, node_max[label][node]):
                    node_max[label][node] = mr
                rows_seen[label] += row_count
                positions[label] += data["original_product_positions"]
                multiplications[label] += data["nonzero_exact_integer_products"]
                name = "stage-"+f"{node:05d}" if kind == "stage" else kind
                relative = "exact-row-blocks/"+label+"/"+name+".json.gz"
                row_hash = hashlib.sha256(json_bytes(data["rows"])).hexdigest()
                value = dict(schema="complete-native-exact-dyadic-row-block-v1",
                    exact_model_sha256=model_sha, direction=label,
                    kind=kind, node=node, row_count=row_count,
                    first_global_equation_row=row_order(kind, node, 0),
                    original_sigma_float64le_hex=struct.pack("<Q", sigma_word).hex(),
                    original_J_stage_sha256=J_stage_sha,
                    direction_raw_sha256=model["directions"][label]["raw_sha256"],
                    residual_encoding="Each [signed odd coefficient in hex, binary exponent] is their exact product; real zero is [0x0,0].",
                    all_exact_unscaled_residual_rows=data["rows"],
                    canonical_rows_json_sha256=row_hash,
                    exact_block_maximum=public_record(mr),
                    original_product_positions=data["original_product_positions"],
                    nonzero_exact_integer_products=data["nonzero_exact_integer_products"],
                    no_thresholding_or_omitted_nonzero_product=True)
                descriptor = write_json(out/relative, value, compressed=True)
                descriptor.update(file=relative, direction=label, kind=kind,
                    node=node, row_count=row_count,
                    exact_model_sha256=model_sha, canonical_rows_json_sha256=row_hash)
                records.append(descriptor)
                ledger.write(json_bytes(descriptor).decode("ascii"))
            ledger.flush()

        cut_result = boundary_job("cut", cut,
            {label:decoded[label][:K] for label in labels}, far_graph)
        consume("cut", 0, cut_result)

        def tasks():
            for node, raw in stage_bytes(capture):
                yield dict(stage=node, J=raw,
                    residuals=residuals[node*K:(node+1)*K],
                    directions={label:(decoded[label][node*K:(node+1)*K],
                        decoded[label][(node+1)*K:(node+2)*K])
                        for label in labels})

        def consume_stage(result):
            nonlocal completed_stages, J_words_seen, J_negative_zeros
            node = result["stage"]
            same(node, completed_stages, "ordered complete exact stage completion")
            consume("stage", node, result, result["J_stage_raw_sha256"])
            completed_stages += 1
            J_words_seen += result["J_words_visited"]
            J_negative_zeros += result["J_negative_zero_words"]
            if completed_stages % 8 == 0 or completed_stages == DEPTH:
                progress = dict(schema=SCHEMA, exact_model_sha256=model_sha,
                    exact_complete_residual_finished=False,
                    completed_stages=completed_stages, expected_stages=DEPTH,
                    rows_completed_by_direction=rows_seen,
                    current_global_exact_maxima={label:public_record(global_max[label]) for label in labels},
                    completed_block_count=len(records),
                    elapsed_seconds=time.monotonic()-started,
                    native_accepted=False, scientific_acceptance_gate_added=False)
                replace_progress(out/"progress.json", progress)
                print(json.dumps(dict(event="complete_native_exact_rows_progress",
                    completed_stages=completed_stages, expected_stages=DEPTH,
                    directions=labels, elapsed_seconds=progress["elapsed_seconds"])), flush=True)

        if args.workers == 1:
            for task in tasks():
                consume_stage(stage_job(task))
        else:
            pool = ProcessPoolExecutor(max_workers=args.workers,
                mp_context=multiprocessing.get_context("spawn"))
            pending, source = deque(), iter(tasks())
            for unused in range(2*args.workers):
                task = next(source, None)
                if task is None:
                    break
                pending.append(pool.submit(stage_job, task))
            while pending:
                consume_stage(pending.popleft().result())
                task = next(source, None)
                if task is not None:
                    pending.append(pool.submit(stage_job, task))
            pool.shutdown(wait=True)
            pool = None
        same(completed_stages, DEPTH, "all original stages exactly accumulated")
        same(J_words_seen, J_PRODUCTS_PER_DIRECTION, "every original J word checked as finite")
        far_result = boundary_job("far", far,
            {label:decoded[label][DEPTH*K:(DEPTH+1)*K] for label in labels}, far_graph)
        consume("far", DEPTH, far_result)
        ledger.close()
        node_reports = {}
        maxima = {}
        for label in labels:
            same(rows_seen[label], TOTAL_ROWS, "every cut/stage/far row "+label)
            same(positions[label], J_PRODUCTS_PER_DIRECTION+M, "every original product position "+label)
            if any(value is None for value in node_max[label]):
                raise ValueError("An original residual node is missing")
            node_reports[label] = [public_record(record) for record in node_max[label]]
            record = global_max[label]
            maxima[label] = public_record(record)
            witness = dict(schema="complete-native-exact-global-maximizer-witness-v1",
                exact_model_sha256=model_sha, direction=label,
                exact_global_maximum=public_record(record),
                operands=worst_witness(capture, record, raw_directions[label], inputs),
                original_direction_sha256=model["directions"][label]["raw_sha256"],
                all_rows_visited_before_global_claim=True,
                exact_finite_saved_arrays_only=True)
            maxima[label]["full_original_binary_operand_witness"] = write_json(
                out/("exact-global-witness-"+label+".json"), witness)
        if any(value is None for value in base_node):
            raise ValueError("An original residual base node is missing")
        node_report = dict(schema="complete-native-exact-node-maxima-v1",
            exact_model_sha256=model_sha,
            assignment="node0 includes cut and stage0; interior node n contains stage n; final node contains far rows",
            directions=node_reports,
            exact_stored_base_residual_node_maxima=[public_record(value) for value in base_node])
        report["per_node_maxima"] = write_json(out/"per-node-maxima.json.gz", node_report, compressed=True)
        report["exact_global_maxima"] = maxima
        report["exact_stored_base_residual_norm"] = public_record(base_global)
        report["exact_linear_defect_to_stored_base_residual_ratios"] = {}
        for label in labels:
            value = global_max[label]
            if base_global["_integer"] == 0:
                ratio = None
            else:
                ratio = fraction_record(abs(value["_integer"])*base_global["_denominator"],
                    value["_denominator"]*abs(base_global["_integer"]))
            report["exact_linear_defect_to_stored_base_residual_ratios"][label] = ratio
        if set(labels) == {"original", "band"}:
            old, new = global_max["original"], global_max["band"]
            report["band_to_original_exact_max_norm_ratio"] = (
                fraction_record(abs(new["_integer"])*old["_denominator"],
                    new["_denominator"]*abs(old["_integer"]))
                if old["_integer"] else None)
        report["exact_row_block_manifest"] = write_json(out/"exact-row-block-manifest.json",
            dict(schema="complete-native-exact-row-block-manifest-v1",
                exact_model_sha256=model_sha, blocks=records,
                completed_block_count=len(records), all_row_blocks_artifact_only=True,
                no_publication_size_limit_used_as_scientific_gate=True))
        report.update(exact_complete_residual_finished=True,
            completed_stages=completed_stages, exact_rows_by_direction=rows_seen,
            original_J_words_visited=J_words_seen,
            original_J_negative_zero_words=J_negative_zeros,
            original_product_positions_by_direction=positions,
            nonzero_exact_integer_multiplications_by_direction=multiplications,
            every_saved_finite_nonzero_term_retained=True,
            maximum_integer_accumulator_bit_bound=4204,
            sigma_division_compared_exactly=True,
            all_norm_comparisons_use_integer_cross_products=True,
            IEEE_signed_zero_bits_preserved_in_input_binding=True,
            exact_real_zero_is_canonical=True,
            complete_model_source_not_reinterpreted_as_exact_flow_derivative=True)
        replace_progress(out/"progress.json", dict(schema=SCHEMA,
            exact_model_sha256=model_sha, exact_complete_residual_finished=True,
            completed_stages=completed_stages, exact_rows_by_direction=rows_seen,
            native_accepted=False, scientific_acceptance_gate_added=False))
    except Exception as error:
        report.update(error=repr(error), completed_stages=completed_stages,
            completed_exact_block_count=len(records),
            partial_exact_blocks_do_not_establish_complete_norm=True)
    finally:
        if pool is not None:
            pool.shutdown(wait=True, cancel_futures=True)
        if ledger is not None and not ledger.closed:
            ledger.close()
        report["elapsed_seconds"] = time.monotonic()-started
        report["parent_maximum_RSS_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        report["terminated_children_maximum_RSS_kib"] = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
        write_json(out/"result.json", report)
    print(json.dumps(dict(event="complete_native_exact_rows_finished",
        exact_complete_residual_finished=report["exact_complete_residual_finished"],
        completed_stages=completed_stages, native_accepted=False,
        scientific_acceptance_gate_added=False)), flush=True)
    return 0 if report["exact_complete_residual_finished"] else 2


if __name__ == "__main__":
    raise SystemExit(main())

