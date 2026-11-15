#!/usr/bin/env python3
"""Read two completed R806 columns by Range; no new multiplication or arithmetic."""
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R806-completed-column-one-small-IO-request.json"
RESULT = "R806-completed-column-one-small-IO-review"
SOURCE_RESULT = "R806-original-primitive-multiplication"
CERT = "p41-original-primitive-multiplication-certificate.json"
REFERENCE = "full-outputs-manifest-reference.json"
HELPER_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
H64 = re.compile(r"[0-9a-f]{64}")
INTEGER = re.compile(r"-?(0|[1-9][0-9]*)")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    temporary = path.with_name(path.name+".tmp")
    temporary.write_bytes(raw)
    temporary.replace(path)


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def plain(value):
    row = {key: value[key] for key in ("file", "bytes", "sha256")}
    assert Path(row["file"]).name == row["file"] and row["file"] not in ("", ".", "..")
    assert type(row["bytes"]) is int and row["bytes"] >= 0 and H64.fullmatch(row["sha256"])
    return row


def integer_metadata(value):
    assert isinstance(value, str) and INTEGER.fullmatch(value)
    return {"decimal_digits": len(value.lstrip("-")), "bit_length": abs(int(value)).bit_length(),
            "text_sha256": hashlib.sha256(value.encode()).hexdigest(), "zero": value == "0"}


def run():
    sys.set_int_max_str_digits(0)
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    request = read(REQUEST)
    item = request["job"]
    assert item["result"] == RESULT and item["producer_inputs_pending"] is False
    assert sha(__file__) == item["reader_sha256"]
    helper = S/item["io_helper"]
    assert sha(helper) == item["io_helper_sha256"] == HELPER_SHA
    module_spec = importlib.util.spec_from_file_location("R806_completed_column_Range_IO", helper)
    io = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(io)
    root = Path(os.environ["RUNNER_TEMP"])/"serre-R806-completed-column-one-IO"
    out = root/"output"
    out.mkdir(parents=True, exist_ok=True)
    source = item["source"]
    archive = io.Archive(source, root/"Range-cache", whole=False)
    try:
        path = archive.extract_bound("full-outputs-manifest.json", source["manifest_sha256"],
                                     out/"full-outputs-manifest.json", source["manifest_bytes"])
        manifest = read(path)
        assert manifest["result"] == SOURCE_RESULT
        entries = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
        assert set(archive.by_name) == set(entries) | {"full-outputs-manifest.json", REFERENCE}
        members = archive.by_name[REFERENCE]
        assert len(members) == 1 and members[0].file_size < 1048576
        raw = archive.zip.read(members[0])
        assert len(raw) == members[0].file_size
        (out/REFERENCE).write_bytes(raw)
        reference = read(out/REFERENCE)
        assert reference["result"] == SOURCE_RESULT
        assert reference["manifest_sha256"] == source["manifest_sha256"]
        assert reference["manifest_bytes"] == source["manifest_bytes"]
        assert reference["file_count"] == len(entries)
        for row in source["files"].values():
            assert plain(row) == entries[row["file"]]
        requested = sorted(row["file"] for row in source["files"].values())
        assert len(requested) == len(set(requested))
        assert all(entries[name]["bytes"] < 2*1024*1024 for name in requested)
        archive.extract_many([(name, entries[name]["sha256"], out/name, entries[name]["bytes"])
                              for name in requested])
        initial = read(out/"public-actions-input.json")
        run_receipt = read(out/"run-receipt.json")
        core = read(out/"core-receipt.json")
        cert = read(out/CERT)
        assert initial["result"] == run_receipt["result"] == core["result"] == cert["result"] == SOURCE_RESULT
        assert initial["source_commit"] == run_receipt["source_commit"] == source["source_commit"]
        assert str(run_receipt["workflow_run_id"]) == str(source["run_id"])
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == core["source_sha256"] == source["core_sha256"]
        assert initial["driver_sha256"] == initial["job"]["wrapper_sha256"] == source["wrapper_sha256"]
        assert run_receipt["complete"] is core["complete"] is cert["complete"] is True
        assert run_receipt["process_exit_code"] == 0 and run_receipt["error"] is None
        assert run_receipt["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
        assert core["certificate_sha256"] == entries[CERT]["sha256"]
        assert cert["p"] == 41 and cert["completed_scope"] == "primitive_multiplication_and_cyclic_certificate"
        assert cert["normal_affine_basis_rank"] == 272 and cert["S_basis_dimension"] == 690
        assert cert["full_coordinate_rows"] == 820 and cert["qY_count"] == 41
        assert cert["all272_columns_verified_in_all820_original_rows"] is True
        assert cert["exact_polynomial_multiplication_computed"] is True
        tag = cert["configuration"]
        assert tag["source_sha256"] == source["core_sha256"]
        def stage(row):
            row = plain(row)
            assert row == entries[row["file"]]
            data = read(out/row["file"])
            assert data["result"] == SOURCE_RESULT and data["complete"] is True
            assert data["configuration"] == tag
            return data
        index = stage(cert["stage_manifest"])
        indexed = {row["file"]: plain(row) for row in index["files"]}
        assert len(indexed) == len(index["files"])
        for row in source["files"].values():
            if row["file"].startswith("R806-") and row["file"] != cert["stage_manifest"]["file"]:
                assert row == indexed[row["file"]]
        chart = stage(cert["coordinate_chart"])
        multiplier = stage(cert["polynomial_multiplier"])
        accepted = stage(cert["accepted_candidate"])
        definition = stage(source["files"]["candidate_definition"])
        group_spec = source["files"]["coordinate_group000"]
        assert plain(cert["exact_coordinate_groups"][0]) == group_spec
        assert plain(multiplier["coordinate_groups"][0]) == group_spec
        group = stage(group_spec)
        assert group["group"] == 0 and group["column_indices"] == list(range(8))
        assert group["all820_original_coordinates_verified"] is True
        assert group["weighted_polynomial_support_verified"] is True
        assert group["reduction_equals_successful_modular_multiplier"] is True
        assert group["integer_scale"] == cert["integer_scale"] == chart["integer_scale"]
        assert group["accepted_primitive_candidate"] == cert["accepted_candidate"]
        assert multiplier["normal_affine_basis_rank"] == 272
        assert multiplier["normal_affine_basis_degrees"] == [0]+[1]*144+[2]*127
        assert multiplier["coordinate_chart"] == cert["coordinate_chart"]
        assert multiplier["all272_columns_verified_in_all820_original_rows"] is True
        assert multiplier["normal_integral_basis_preserved"] is True
        assert accepted["candidate_index"] == definition["candidate_index"] == cert["actual_candidate_index"] == 0
        assert cert["actual_w0_original_M2_integer_coordinates"] == ["0", "0", "1"]+["0"]*143
        mapping = multiplier["S_row_to_polynomial_coefficient"]
        assert len(mapping) == 690 and [row["S_row"] for row in mapping] == list(range(690))
        assert len({(row["normal_basis_row"], row["power_of_z"]) for row in mapping}) == 690
        assert all(type(row["normal_basis_row"]) is int and 0 <= row["normal_basis_row"] < 272
                   and type(row["power_of_z"]) is int and 0 <= row["power_of_z"] < 4 for row in mapping)
        numerators = group["coordinate_numerators"]
        denominators = group["column_denominators"]
        assert len(numerators) == 690 and all(len(row) == 8 for row in numerators)
        assert len(denominators) == 8
        columns = []
        for column in (0, 1):
            denominator = denominators[column]
            assert INTEGER.fullmatch(denominator) and not denominator.startswith("-") and denominator != "0"
            nonzero = []
            for row, mapping_row in enumerate(mapping):
                value = numerators[row][column]
                assert isinstance(value, str) and INTEGER.fullmatch(value)
                if value != "0":
                    nonzero.append({"S_row": row, "normal_basis_row": mapping_row["normal_basis_row"],
                                    "power_of_z": mapping_row["power_of_z"], "numerator": value,
                                    "denominator": denominator})
            full_column = {
                "result": RESULT, "complete": True, "source_group": group_spec,
                "source_polynomial_interface": plain(cert["polynomial_multiplier"]),
                "original_configuration_sha256": hashlib.sha256(
                    json.dumps(tag, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
                "input_normal_basis_column": column, "coordinate_numerators":
                    [row[column] for row in numerators],
                "column_denominator": denominator, "S_row_mapping": mapping,
                "nonzero_original_coefficients": nonzero,
                "only_previously_completed_bytes_read": True,
                "new_matrix_product_or_coordinate_reconstruction_computed": False,
            }
            name = "R806-completed-original-column-"+str(column)+".json"
            save(out/name, full_column)
            one_basis = None
            if len(nonzero) == 1 and nonzero[0]["power_of_z"] == 0:
                row = nonzero[0]
                if row["numerator"] == denominator:
                    one_basis = {"normal_basis_row": row["normal_basis_row"], "coefficient": "1"}
                elif row["numerator"] == "-"+denominator:
                    one_basis = {"normal_basis_row": row["normal_basis_row"], "coefficient": "-1"}
            short = len(nonzero) <= 16 and len(denominator) <= 120 and \
                    all(len(row["numerator"].lstrip("-")) <= 120 for row in nonzero)
            columns.append({
                "input_normal_basis_column": column,
                "source_denominator_metadata": integer_metadata(denominator),
                "actual_nonzero_coefficient_count": len(nonzero),
                "actual_nonzero_support_prefix": [{key: row[key] for key in
                    ("S_row", "normal_basis_row", "power_of_z")} for row in nonzero[:32]],
                "support_prefix_truncated": len(nonzero) > 32,
                "single_signed_original_normal_basis_vector": one_basis,
                "exact_small_relation": nonzero if short else None,
                "large_coefficient_strings_omitted_from_log": not short,
                "full_original_column": spec(out/name),
            })
        assert columns[0]["single_signed_original_normal_basis_vector"] == \
               {"normal_basis_row": 1, "coefficient": "1"}
        selected = [spec(out/name) for name in sorted(requested)]
        summary = {
            "result": RESULT, "complete": True, "source": source,
            "output_source_manifest": spec(out/"full-outputs-manifest.json"),
            "complete_original_manifest_count": len(entries),
            "selected_original_files": selected,
            "selected_files_all_original_size_SHA_verified": True,
            "actual_candidate_index": 0, "actual_w0_original_M2_index": 2,
            "normal_basis_convention": multiplier["matrix_convention"],
            "original_S3_integer_scale": group["integer_scale"],
            "original_R805_free_basis": multiplier["original_R805_free_basis"],
            "original_R805_S_basis_index": multiplier["original_R805_S_basis_index"],
            "columns": columns, "source_transfer": archive.receipt(),
            "mathematical_core_or_flint_imported": False,
            "new_W_or_W_times_vg_or_LLL_or_CRT_or_RR_computed": False,
            "R815_multiplier_or_derivation_certified_by_this_IO": False,
        }
        save(out/"R806-completed-column-one-IO-summary.json", summary)
        print("R806_COMPLETED_COLUMN_ONE_IO_SUMMARY="+json.dumps(summary, sort_keys=True), flush=True)
        return 0
    finally:
        archive.close()


if __name__ == "__main__":
    sys.exit(run())
