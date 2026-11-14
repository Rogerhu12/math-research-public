#!/usr/bin/env python3
"""Byte-only comparison of actual66/67 fixed-model inputs and saved B arrays.

No scientific package is imported. NPY/NPZ payloads are parsed as bytes;
no floating-point value, norm, matrix action or new model is computed. Full
chain A inputs which were not exported remain explicitly reported identities.
Cross-run differences are evidence, not an additional scientific acceptance.
"""
from __future__ import annotations

import argparse
import ast
import gzip
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import struct
import sys
import traceback
import zipfile


PARENT_WARM = "3b25ea84dfababece99e1dc098d56cdcebd94737e428e509140e818d48e8eb1e"
PARENT_STATUS = "037fb9eeaeb196f74976188efb9515736396f2c86a44fde4e93251e92ca01466"
BASE_SOURCE = "9d750fcba45624f23dbae19ca44fded0437f1f5dc15943879cbf046064fe22ee"
CHANGED_SOURCE = "7de5e7d01efa9464e9c0d671c94d3b70a6e093dc1b3fd844944456ebb46fbbb5"
DOMAIN_SOURCE = "16157412cbb4af0d01ade0cb3e373413fda175059186ccf17ef3b1d727d27ce1"
BASE_SCHEMA = "exact-constraint-twenty-query-condensed-complete-H-warm-v1"
CHANGED_SCHEMA = "exact-constraint-twenty-query-lambda27-condensed-complete-H-warm-v1"
READ_CHUNK = 1024 * 1024


def require(test, message):
    if not test:
        raise ValueError(message)


def sha_file(path):
    digest = hashlib.sha256()
    size = 0
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(READ_CHUNK), b""):
            size += len(block)
            digest.update(block)
    return dict(bytes=size, sha256=digest.hexdigest())


def safe_path(root, name):
    require(isinstance(name, str) and "\\" not in name,
            "A declared relative POSIX file name is required")
    path = PurePosixPath(name)
    require(not path.is_absolute() and path.parts and
            all(item not in ("", ".", "..") for item in path.parts),
            "A relative artifact path may not escape its root")
    root = Path(root).resolve()
    out = (root / name).resolve()
    require(out.is_relative_to(root) and out.is_file(), "Missing declared file: " + name)
    return out


def read_json(root, name, receipts):
    path = safe_path(root, name)
    raw = path.read_bytes()
    receipts[name] = dict(file=name, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def check_file(root, descriptor, name_key="file"):
    name = descriptor[name_key]
    path = safe_path(root, name)
    actual = sha_file(path)
    require(actual["bytes"] == descriptor["bytes"], "File length differs: " + name)
    require(actual["sha256"] == descriptor["sha256"], "File SHA differs: " + name)
    return path, dict(file=name, **actual)


def product(shape):
    count = 1
    for value in shape:
        require(type(value) is int and value >= 0, "NPY dimensions are nonnegative integers")
        count *= value
    return count


def c_order_bytes(payload, shape, itemsize, is_fortran):
    """Reorder storage bytes only; no numeric decoding or arithmetic."""
    if not is_fortran or len(shape) < 2 or product(shape) == 0:
        return payload
    count = product(shape)
    f_strides = []
    stride = 1
    for dim in shape:
        f_strides.append(stride)
        stride *= dim
    output = bytearray(len(payload))
    for flat_c in range(count):
        remain = flat_c
        flat_f = 0
        for dim, f_stride in zip(reversed(shape), reversed(f_strides)):
            index = remain % dim
            remain //= dim
            flat_f += index * f_stride
        start = flat_c * itemsize
        old_start = flat_f * itemsize
        output[start:start + itemsize] = payload[old_start:old_start + itemsize]
    return bytes(output)


def npy_bytes(stream):
    require(stream.read(6) == b"\x93NUMPY", "A genuine NPY member is required")
    version = stream.read(2)
    require(version in (b"\x01\x00", b"\x02\x00", b"\x03\x00"), "Supported actual NPY header version")
    length_bytes = stream.read(2 if version == b"\x01\x00" else 4)
    require(len(length_bytes) == (2 if version == b"\x01\x00" else 4), "Complete NPY length")
    length = int.from_bytes(length_bytes, "little")
    require(length <= 100000, "Only a small scalar dtype/shape NPY header is expected")
    header_bytes = stream.read(length)
    require(len(header_bytes) == length, "Complete NPY header")
    header = ast.literal_eval(header_bytes.decode("utf-8" if version == b"\x03\x00" else "latin1"))
    require(set(header) == {"descr", "fortran_order", "shape"}, "Actual scalar NPY header fields")
    dtype = header["descr"]
    require(isinstance(dtype, str) and re.fullmatch(r"[<|][fiu][1248]", dtype),
            "No object, structured or unsupported scalar dtype")
    require(type(header["fortran_order"]) is bool, "Explicit NPY storage order")
    shape = header["shape"]
    require(isinstance(shape, tuple), "NPY shape tuple")
    itemsize = int(dtype[2:])
    expected_bytes = product(shape) * itemsize
    payload = stream.read()
    require(len(payload) == expected_bytes, "Complete NPY payload without trailing bytes")
    raw = c_order_bytes(payload, shape, itemsize, header["fortran_order"])
    prefixed = hashlib.sha256(str(shape).encode("ascii") + b"\0" +
                              dtype.encode("ascii") + b"\0" + raw).hexdigest()
    return raw, dict(shape=list(shape), dtype=dtype, bytes=len(raw), sha256=prefixed,
                     raw_sha256=hashlib.sha256(raw).hexdigest(),
                     original_NPY_fortran_order=header["fortran_order"])


def check_identity(actual, expected, label):
    for key in ("shape", "dtype", "bytes", "sha256"):
        require(actual[key] == expected[key], label + ": array " + key + " differs")


def check_npz(root, descriptor, name_key="file", expected_arrays=None, keep_raw=False):
    path, record = check_file(root, descriptor, name_key)
    arrays = descriptor.get("arrays") if expected_arrays is None else expected_arrays
    require(isinstance(arrays, dict) and arrays, "Explicit NPZ array ledger")
    raw_arrays, verified = {}, {}
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        require(len(names) == len(set(names)), "No repeated NPZ members")
        require(set(names) == {name + ".npy" for name in arrays}, "NPZ members match the whole array ledger")
        for name, expected in arrays.items():
            with archive.open(name + ".npy") as stream:
                raw, actual = npy_bytes(stream)
            check_identity(actual, expected, record["file"] + "/" + name)
            verified[name] = actual
            if keep_raw:
                raw_arrays[name] = raw
    record["arrays"] = verified
    return record, raw_arrays


def check_archived_array(root, reference):
    expected = reference["array_identity"]
    parts = reference["parts"]
    require(isinstance(parts, list) and parts, "All parts of an exported array are required")
    current = 0
    actual_records = []
    full_raw_digest = hashlib.sha256()
    full_identity = hashlib.sha256(str(tuple(expected["shape"])).encode() + b"\0" +
                                   expected["dtype"].encode() + b"\0")
    total_bytes = 0
    for item in parts:
        left, right = item["leading_slice"]
        require(left == current and right > left, "Complete ordered array partition")
        path = safe_path(root, item["file"])
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
        require(len(names) == 1 and names[0].endswith(".npy"), "One complete saved part per NPZ")
        key = names[0][:-4]
        row, raw = check_npz(root, item, expected_arrays={key:item["array"]}, keep_raw=True)
        payload = raw[key]
        require(row["arrays"][key]["shape"] == [right-left, *expected["shape"][1:]],
                "Part dimensions match the full array slice")
        require(row["arrays"][key]["dtype"] == expected["dtype"], "Identical full-array dtype")
        current = right
        total_bytes += len(payload)
        full_raw_digest.update(payload)
        full_identity.update(payload)
        actual_records.append(row)
    require(current == expected["shape"][0] and total_bytes == expected["bytes"],
            "All full-array bytes accounted for")
    require(full_identity.hexdigest() == expected["sha256"], "Complete reconstructed array SHA")
    return dict(array_identity=expected, raw_sha256=full_raw_digest.hexdigest(),
                complete_parts=actual_records)


def check_raw(root, descriptor):
    path = safe_path(root, descriptor["file"])
    actual = sha_file(path)
    require(actual["bytes"] == descriptor["bytes"] and
            actual["sha256"] == descriptor["raw_sha256"], "Complete raw array bytes/SHA differ")
    return dict(file=descriptor["file"], shape=descriptor["shape"], dtype=descriptor["dtype"], **actual)


def read_model(directory, expected_source, expected_schema, expected_damping):
    root = Path(directory).resolve()
    files = {}
    binding = read_json(root, "condensed-live-model-binding.json", files)
    result = read_json(root, "condensed-QP-result.json.gz", files)
    manifest = read_json(root, "condensed-array-manifest.json", files)
    domain = read_json(root, "domain-operator/manifest.json", files)
    status = read_json(root, "driver-status.json", files)
    entry = binding["condensed_QP_entry"]
    require(entry["entry_source_sha256"] == expected_source and entry["schema"] == expected_schema,
            "Bind the actual declared producer, not another numerical attempt")
    require(entry["actual_parent_warm_sha256"] == PARENT_WARM and
            entry["actual_parent_status_sha256"] == PARENT_STATUS, "Both models use actual64")
    require(binding["damping"] == expected_damping, "Read the explicit intended damping")
    require(entry["twenty_query_operator_source_sha256"] == DOMAIN_SOURCE,
            "Retain the same frozen twenty-query operator")
    require(status["schema"] == expected_schema, "Status belongs to the actual producer")
    require(manifest["result"] == files["condensed-QP-result.json.gz"], "Manifest binds the complete result")
    require(result["condensed_QP_entry"] == entry, "Whole scientific result retains the current entry")
    require(domain["model_sha256"] == binding["B_model_sha256"], "Actual B identity is bound")

    domain_records = []
    for descriptor in domain["files"]:
        row, _ = check_npz(root / "domain-operator", descriptor, name_key="path")
        row["query"] = descriptor.get("query")
        domain_records.append(row)
    require(len({item["file"] for item in domain_records}) == len(domain_records), "Unique B filenames")
    archived = {key:check_archived_array(root, result[key]) for key in
                ("original_b", "original_g", "original_c")}
    for key in ("original_b", "original_g"):
        require(archived[key]["array_identity"] == binding[key], "Original bound " + key + " retained")
    full_report = result["complete_chain_QR_report"]
    local_report = result["condensation_report"]
    require(full_report["damping"] == expected_damping and
            local_report["damping"] == expected_damping, "Both roots use the actual new damping")
    require(full_report["input_arrays"] == local_report["original_factor_input_arrays"],
            "Condensation uses the same complete A/W/S as its factor")
    raw_root = {name:check_raw(root / "condensed-root", descriptor)
                for name, descriptor in local_report["output_arrays"].items()}
    return dict(directory=str(root), small_files=files, parent=entry,
        damping=binding["damping"], schema=expected_schema,
        scientific_binding={key:binding[key] for key in
            ("original_A_shape", "original_weights", "original_g", "original_b", "chart_scale", "local_indices")},
        B_model_sha256=binding["B_model_sha256"],
        B_base_identity=domain["base_identity"], B_query_specs=domain["query_specs"],
        B_capture_identity=domain["capture"], verified_B_payloads=domain_records,
        verified_original_arrays=archived,
        original_C_recorded_identity=binding["original_C"],
        recorded_full_A_input_arrays=full_report["input_arrays"],
        full_A_arrays_recomputed_or_exported_here=False,
        complete_QR_factor_array_records=full_report["factor_arrays"],
        complete_QR_factor_payloads_exported=all(item.get("file") is not None
                                              for item in full_report["factor_arrays"].values()),
        verified_condensed_root_arrays=raw_root,
        original_factor_report=full_report,
        original_condensation_report=local_report,
        original_recovery_report=result["actual_recovery_report"],
        original_final_evidence=result["final_selected_evidence"])


def comparison(base, changed):
    a = {item["file"]:item for item in base["verified_B_payloads"]}
    b = {item["file"]:item for item in changed["verified_B_payloads"]}
    names = sorted(set(a) | set(b))
    rows = []
    for name in names:
        if name not in a or name not in b:
            rows.append(dict(file=name, present_in_both=False, same_raw_arrays=False))
            continue
        ar, br = a[name], b[name]
        aa, bb = ar["arrays"], br["arrays"]
        arrays = []
        for key in sorted(set(aa) | set(bb)):
            present = key in aa and key in bb
            same = present and all(aa[key][k] == bb[key][k] for k in
                                   ("shape", "dtype", "bytes", "raw_sha256", "sha256"))
            arrays.append(dict(array=key, same_complete_verified_raw_bytes_by_SHA256=same,
                               baseline=aa.get(key), changed=bb.get(key)))
        rows.append(dict(file=name, present_in_both=True,
            compressed_file_SHA_equal=ar["sha256"] == br["sha256"],
            actual_query_record_equal=ar["query"] == br["query"],
            same_raw_arrays=all(item["same_complete_verified_raw_bytes_by_SHA256"] for item in arrays),
            arrays=arrays))
    original_arrays = {key:dict(
        baseline=base["verified_original_arrays"][key]["array_identity"],
        changed=changed["verified_original_arrays"][key]["array_identity"],
        same_actual_complete_raw_sha256=(base["verified_original_arrays"][key]["raw_sha256"] ==
                                         changed["verified_original_arrays"][key]["raw_sha256"]))
        for key in base["verified_original_arrays"]}
    scientific = {key:dict(equal=base["scientific_binding"][key] == changed["scientific_binding"][key],
                           baseline=base["scientific_binding"][key], changed=changed["scientific_binding"][key])
                  for key in base["scientific_binding"]}
    full_A = {key:dict(equal=base["recorded_full_A_input_arrays"][key] ==
                                  changed["recorded_full_A_input_arrays"][key],
                       baseline=base["recorded_full_A_input_arrays"][key],
                       changed=changed["recorded_full_A_input_arrays"][key])
              for key in base["recorded_full_A_input_arrays"]}
    return dict(B_file_count=len(rows), B_array_count=sum(len(row.get("arrays", ())) for row in rows),
        B_payloads=rows, all_verified_B_payloads_equal=all(row["same_raw_arrays"] for row in rows),
        original_arrays=original_arrays, scientific_binding_records=scientific,
        original_full_A_input_records=full_A,
        complete_A_input_payloads_not_exported_and_not_locally_recomputed=True,
        scientific_full_A_equality_scope="Equality of the original Actions complete input raw-SHA records; complete L/R matrices were not exported",
        B_query_specs_equal=base["B_query_specs"] == changed["B_query_specs"],
        B_base_identity_equal=base["B_base_identity"] == changed["B_base_identity"],
        metadata_B_model_SHA=dict(baseline=base["B_model_sha256"], changed=changed["B_model_sha256"],
            equal=base["B_model_sha256"] == changed["B_model_sha256"],
            metadata_difference_not_by_itself_a_scientific_array_difference=True),
        expected_changed_C=dict(baseline=base["original_C_recorded_identity"],
            changed=changed["original_C_recorded_identity"],
            equal=base["original_C_recorded_identity"] == changed["original_C_recorded_identity"],
            C_and_roots_expected_rebuilt_under_new_damping=True),
        new_scientific_acceptance_gate=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--changed", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    require(not args.out.exists(), "Use a new byte-only audit output directory")
    args.out.mkdir(parents=True)
    summary = dict(schema="actual66-67-same-base-model-byte-comparison-v1",
        scientific_arrays_recomputed=False, scientific_modules_imported=False,
        norms_or_matrix_actions_or_fraction_arithmetic_computed=False,
        only_actual_saved_scalar_reports_copied=True, cross_run_comparison_is_not_acceptance_gate=True)
    try:
        base = read_model(args.baseline, BASE_SOURCE, BASE_SCHEMA, 270.0)
        changed = read_model(args.changed, CHANGED_SOURCE, CHANGED_SCHEMA, 27.0)
        compared = comparison(base, changed)
        detail = dict(baseline=base, changed=changed, comparison=compared)
        raw = (json.dumps(detail, separators=(",", ":"), allow_nan=False) + "\n").encode()
        path = args.out / "complete-byte-detail.json.gz"
        path.write_bytes(gzip.compress(raw, mtime=0))
        summary.update(completed=True, detail=dict(file=path.name, **sha_file(path)),
            B_file_count=compared["B_file_count"], B_array_count=compared["B_array_count"],
            all_verified_B_payloads_equal=compared["all_verified_B_payloads_equal"],
            all_original_b_g_c_payloads_equal=all(v["same_actual_complete_raw_sha256"] for v in compared["original_arrays"].values()),
            all_scientific_binding_records_equal=all(v["equal"] for v in compared["scientific_binding_records"].values()),
            all_original_full_A_input_records_equal=all(v["equal"] for v in compared["original_full_A_input_records"].values()),
            B_base_identity_equal=compared["B_base_identity_equal"],
            B_query_specs_equal=compared["B_query_specs_equal"],
            metadata_B_model_SHA=compared["metadata_B_model_SHA"],
            expected_changed_C=compared["expected_changed_C"],
            original_complete_A_and_QR_factor_payloads_not_exported=True)
        code = 0
    except Exception as error:
        summary.update(completed=False, exception=repr(error), traceback=traceback.format_exc())
        code = 1
    summary["reader_source"] = dict(file=Path(__file__).name, **sha_file(__file__))
    (args.out / "summary.json").write_text(json.dumps(summary, indent=2, allow_nan=False) + "\n")
    print(json.dumps(summary, allow_nan=False))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
