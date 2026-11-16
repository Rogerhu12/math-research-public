#!/usr/bin/env python3
"""Original comparison first jets: standard-library input and output IO only."""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
import re
from pathlib import Path
import signal
import subprocess
import sys
import tarfile
import time

S = Path(__file__).resolve().parent
TOPIC = S.parent
REPO = TOPIC.parents[1]
REQUEST = TOPIC/'notes/R792-Hom-comparison-log-jets-public-request.json'
RESULT = 'R792-original-Hom-comparison-log-jets'
FINAL = 'p41-original-Hom-comparison-log-jets-certificate.json'
PREFIX = 'R792-Hom-log-jets-'
BUNDLE = 'R792-Hom-log-jets-retained-inputs.tar.gz'
MANIFEST = 'full-outputs-manifest.json'
REFERENCE = 'full-outputs-manifest-reference.json'
INPUT_RECEIPT = 'retained-inputs-receipt.json'
META = (MANIFEST,'run-receipt.json','core-receipt.json','public-actions-input.json')
PARENT_FINAL = 'p41-original-Hom-word-point-DAG-certificate.json'
PARENT_BUNDLE = 'R792-Hom-word-DAG-retained-inputs.tar.gz'
POINT_IO_SHA = 'bb0cce85ff6e4f7df2dd9e4a153b21e6e1a14038ee35800ec9c91f7edecfda9a'
POINT_CORE_SHA = '719c170ac00cf7b15db0d74b5a58998f2901ad838db33dc9d01fd29acd36805a'
DAG_CORE_SHA = 'afb49c1ac4245674d29364789e817b566517e1f5bf6d506cee684ed03fa34b8b'
IO = None
H64 = re.compile(r"[0-9a-f]{64}")

STRATEGY = {
    "original_point_program": "R844 original 529 exact nodes imported unchanged",
    "original_differential": "dx/(2y), coordinate z=a-1 at the same original c1",
    "new_scope": "f and five original g_j=(1+T^j)f, their coordinate first jets and five original comparison first jets",
    "tangents": "linear combinations of the original twelve R791 integer-Hom tangents",
    "logarithmic_derivative": "6*y_u*h_u/x_u; no logarithm branch",
    "norm_derivative": "actual seven sigma conjugates; same Q-defined parameter",
    "inverse_proof": "same-point R843 non-torsion via original nonzero integral Hom word",
    "original_comparison_constants_preserved": True,
    "old_CM_Hom_point_or_nontorsion_arithmetic_recomputed": False,
    "nonzero_jet_expanded_coordinates_eta_or_height_certified": False,
}

def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    data = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        with temporary.open("wb") as raw:
            with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, compresslevel=2) as stream:
                stream.write(data)
    else:
        temporary.write_bytes(data)
    temporary.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def safe(name):
    assert isinstance(name, str) and Path(name).name == name and name not in (".", "..") and "\\" not in name
    return name


def plain(row):
    answer = {key: row[key] for key in ("file", "bytes", "sha256")}
    safe(answer["file"])
    assert isinstance(answer["bytes"], int) and answer["bytes"] >= 0 and H64.fullmatch(answer["sha256"])
    return answer


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def bound(root, row):
    row = plain(row)
    path = Path(root)/row["file"]
    assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
    return path


def topic_path(relative):
    result = (TOPIC/relative).resolve()
    assert result.is_relative_to(TOPIC.resolve())
    return result


def output_manifest(out):
    rows = [file_spec(path) for path in sorted(out.iterdir()) if path.is_file() and
            path.name not in (MANIFEST, REFERENCE) and not path.name.endswith(".tmp")]
    save(out/MANIFEST, {"result": RESULT, "files": rows,
        "temporary_active_checkpoint_retention_days": 1,
        "reproducible_tables_in_git_or_release": False})
    save(out/REFERENCE, {"result": RESULT, "manifest": file_spec(out/MANIFEST)})


def load_io(item):
    global IO
    path = S/safe(item["point_wrapper"])
    assert path.name == "R792_public_original_Hom_word_point_DAG.py"
    assert sha(path) == item["point_wrapper_sha256"] == POINT_IO_SHA
    source = importlib.util.spec_from_file_location("frozen_original_Hom_point_IO_only", path)
    IO = importlib.util.module_from_spec(source)
    source.loader.exec_module(IO)
    IO.load_io(item)

def guard(item, request):
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("This consumer executes only in public repository Actions.")
    assert request.resolve() == REQUEST.resolve()
    assert item["result"] == RESULT and item["p"] == 41 and item["producer_inputs_pending"] is False
    assert item["core"] == "R792_original_Hom_comparison_log_jets.py"
    assert item["wrapper"] == "R792_public_original_Hom_comparison_log_jets.py"
    for name, pin in (("core", item["core_sha256"]), ("wrapper", item["wrapper_sha256"]),
                      ("dag_core", DAG_CORE_SHA)):
        assert sha(S/safe(item[name])) == pin == item[name+"_sha256"]
    for proof in item["proofs"].values():
        assert sha(topic_path(proof["path"])) == proof["sha256"]
    assert sha(REPO/"README.md") == item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md") == item["readme_sha256"]["topic"]
    assert 0 < item["budget_minutes"] <= 300
    parent = item["parent_source"]
    assert parent["result"] == "R792-original-Hom-word-point-DAG" and parent["core_sha256"] == POINT_CORE_SHA
    assert parent["expected_conclusion"] == "success"
    load_io(item)


def parent_names(directory):
    directory = Path(directory)
    cert = read(directory/PARENT_FINAL)
    stage_manifest = read(bound(directory, cert["stage_manifest"]))
    return sorted(set(META) | {PARENT_FINAL, INPUT_RECEIPT, cert["stage_manifest"]["file"]} |
                  {row["file"] for row in stage_manifest["files"]})

def review_parent(item, retained):
    parent, root = item["parent_source"], retained/"POINTS"
    assert sha(root/MANIFEST) == parent["manifest_sha256"] and (root/MANIFEST).stat().st_size == parent["manifest_bytes"]
    manifest = read(root/MANIFEST)
    assert manifest["result"] == parent["result"] and len(manifest["files"]) == parent["manifest_file_count"]
    inventory = {row["file"]: plain(row) for row in manifest["files"]}
    inventory[MANIFEST] = file_spec(root/MANIFEST)
    names = parent_names(root)
    files = {name: inventory[name] for name in names}
    assert len(names) == parent["selected_file_count"] == 10
    assert fingerprint([files[name] for name in names]) == parent["selected_files_sha256"]
    for row in files.values():
        bound(root, row)
    run, core, public = (read(root/name) for name in META[1:])
    cert = read(root/PARENT_FINAL)
    assert files[PARENT_FINAL] == plain(parent["certificate"])
    assert run["result"] == core["result"] == public["result"] == cert["result"] == parent["result"]
    assert run["complete"] is True and run["process_exit_code"] == 0 and run.get("error") is None
    assert core["complete"] is True and core["certificate_sha256"] == files[PARENT_FINAL]["sha256"]
    assert run["core_receipt_sha256"] == files["core-receipt.json"]["sha256"]
    assert str(run["workflow_run_id"]) == str(parent["run_id"])
    assert public["source_commit"] == run["source_commit"] == parent["source_commit"]
    assert core["source_sha256"] == public["core_sha256"] == parent["core_sha256"] == POINT_CORE_SHA
    assert public["wrapper_sha256"] == parent["wrapper_sha256"] == POINT_IO_SHA
    assert public["root_readme_sha256"] == parent["original_readme_sha256"]["root"]
    assert public["topic_readme_sha256"] == parent["original_readme_sha256"]["topic"]
    assert cert["complete"] is True and fingerprint(cert["configuration"]) == parent["configuration_sha256"]
    for flag in ("actual_nontorsion_source_verified", "five_original_R791_addition_points_as_exact_DAG",
                 "all_addition_denominators_certified_by_original_Hom_words",
                 "original_Galois_transport_and_T7_phase_preserved",
                 "original_R791_comparison_function_values_as_exact_DAG"):
        assert cert[flag] is True
    assert cert["expanded_coordinates_exactly_certified"] is False
    assert cert["actual_eta_or_height_computed"] is False and cert["new_addition_count"] == 5
    assert cert["point_program_node_count"] == 529
    receipt = read(root/INPUT_RECEIPT)
    assert receipt["parent_source"] == public["job"]["parent_source"]
    assert plain(receipt["input_bundle"]) == plain(parent["input_bundle"]) == inventory[PARENT_BUNDLE]
    children = IO.review_parent(public["job"], retained)
    assert children == receipt["expanded_sources"] == public["expanded_sources"]
    tag = cert["configuration"]
    assert IO.expected_tag(public["job"], children) == tag
    for name in names:
        if name.endswith(".json.gz"):
            stage = read(root/name)
            assert stage["complete"] is True and stage["configuration"] == tag
    for row in read(bound(root, cert["stage_manifest"]))["files"]:
        assert files[row["file"]] == plain(row)
    program = read(bound(root, cert["point_program"]))
    assert program["node_count"] == 529 and program["imported_R841_node_count"] == 50
    assert program["imported_R841_nodes_unchanged"] is True
    assert len(program["addition_branches"]) == 5
    assert len(program["five_original_eta_addition_inputs"]) == 5
    return dict(children, POINTS=dict(parent, files=files))

def prepare(item, out, allow_download=True):
    retained = out.parent/(out.name+"-retained")
    if (out/INPUT_RECEIPT).exists() and (out/BUNDLE).exists():
        receipt = read(out/INPUT_RECEIPT)
        assert receipt["parent_source"] == item["parent_source"]
        assert file_spec(out/BUNDLE) == receipt["input_bundle"]
        IO.IO.IO.unpack_sources(out/BUNDLE, retained, receipt["expanded_sources"])
        expanded = review_parent(item, retained)
        assert expanded == receipt["expanded_sources"]
        return retained, expanded
    assert allow_download
    parent, root = item["parent_source"], retained/"POINTS"
    root.mkdir(parents=True, exist_ok=True)
    transfer = out.parent/(out.name+"-parent-transfer")
    archive = IO.IO.IO.IO.Archive(parent, transfer, whole=True)
    try:
        archive.extract_bound(MANIFEST, parent["manifest_sha256"], root/MANIFEST, parent["manifest_bytes"])
        files = {row["file"]: plain(row) for row in read(root/MANIFEST)["files"]}
        def take(names):
            archive.extract_many([(name, files[name]["sha256"], root/name, files[name]["bytes"])
                                  for name in names if name != MANIFEST])
        take([PARENT_FINAL])
        take([read(root/PARENT_FINAL)["stage_manifest"]["file"]])
        take(parent_names(root))
        bundle = plain(parent["input_bundle"])
        assert files[PARENT_BUNDLE] == bundle
        archive.extract_bound(PARENT_BUNDLE, bundle["sha256"], transfer/PARENT_BUNDLE, bundle["bytes"])
        receipt = read(root/INPUT_RECEIPT)
        assert file_spec(transfer/PARENT_BUNDLE) == bundle == plain(receipt["input_bundle"])
        IO.IO.IO.unpack_sources(transfer/PARENT_BUNDLE, retained, receipt["expanded_sources"])
        expanded = review_parent(item, retained)
        IO.IO.IO.pack_sources(retained, expanded, out/BUNDLE)
        source_receipt = {"result": RESULT, "parent_source": parent, "expanded_sources": expanded,
            "input_bundle": file_spec(out/BUNDLE), "source_transport": archive.receipt(),
            "selected_source_file_count": sum(len(value["files"]) for value in expanded.values()),
            "all_source_bytes_and_original_parent_child_bindings_verified": True,
            "old_CM_Hom_point_or_nontorsion_arithmetic_recomputed": False}
        save(out/INPUT_RECEIPT, source_receipt)
        print("INPUT_REVIEW="+json.dumps({key: source_receipt[key] for key in ("selected_source_file_count", "input_bundle",
            "all_source_bytes_and_original_parent_child_bindings_verified", "old_CM_Hom_point_or_nontorsion_arithmetic_recomputed")}), flush=True)
        return retained, expanded
    finally:
        archive.close()


def expected_tag(item, expanded):
    return {"result": RESULT, "source_sha256": item["core_sha256"], "p": 41,
        "dag_core_sha256": DAG_CORE_SHA,
        "proofs": item["proofs"], "source_identities": {key: IO.IO.IO.source_identity(value) for key, value in expanded.items()},
        "strategy": STRATEGY, "budget_excluded_from_mathematical_identity": True}


def stable_job(item):
    return {key: value for key, value in item.items() if key not in ("resume", "budget_minutes")}


def restore(item, out):
    source = item.get("resume")
    if source is None:
        return
    assert source["result"] == RESULT and source["core_sha256"] == item["core_sha256"]
    root = out.parent/(out.name+"-resume")
    archive = IO.IO.IO.IO.Archive(source, root, whole=False)
    try:
        archive.extract_bound(MANIFEST, source["manifest_sha256"], root/MANIFEST, source["manifest_bytes"])
        files = {row["file"]: plain(row) for row in read(root/MANIFEST)["files"]}
        for name in ("public-actions-input.json", "run-receipt.json", INPUT_RECEIPT):
            row = files[name]
            archive.extract_bound(name, row["sha256"], root/name, row["bytes"])
        public, run = read(root/"public-actions-input.json"), read(root/"run-receipt.json")
        assert stable_job(public["job"]) == stable_job(item)
        assert public["source_commit"] == run["source_commit"] == source["source_commit"]
        assert str(run["workflow_run_id"]) == str(source["run_id"])
        wanted = [name for name in files if name.startswith(PREFIX) and name.endswith(".json.gz")]+[BUNDLE, INPUT_RECEIPT]
        if FINAL in files:
            wanted.append(FINAL)
        archive.extract_many([(name, files[name]["sha256"], out/name, files[name]["bytes"]) for name in wanted])
        tag = expected_tag(item, read(out/INPUT_RECEIPT)["expanded_sources"])
        for name in wanted:
            if name.endswith(".json.gz"):
                data = read(out/name)
                assert data["complete"] is True and data["configuration"] == tag
        if (out/FINAL).exists():
            final = read(out/FINAL)
            assert final["complete"] is True and final["configuration"] == tag
            for row in read(bound(out, final["stage_manifest"]))["files"]:
                bound(out, row)
        save(out/"resume-source-receipt.json", {"result": RESULT, "source": source, "transport": archive.receipt(),
            "old_mathematics_recomputed_by_restore": False})
    finally:
        archive.close()


def compute(item, out, request):
    out.mkdir(parents=True, exist_ok=True)
    restore(item, out)
    retained, expanded = prepare(item, out)
    config = dict(item, retained_sources=expanded)
    config_path = out.parent/(out.name+"-config.json")
    save(config_path, config)
    save(out/"public-actions-input.json", {"result": RESULT, "job": item, "source_commit": os.environ["GITHUB_SHA"],
        "source_repository": os.environ["GITHUB_REPOSITORY"], "core_sha256": item["core_sha256"],
        "wrapper_sha256": item["wrapper_sha256"], "request_sha256": sha(request),
        "expanded_sources": expanded, "expanded_job_sha256": fingerprint(config),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    command = [sys.executable, str(S/item["core"]), "--config", str(config_path), "--topic", str(TOPIC),
        "--dag-core", str(S/item["dag_core"]),
        "--retained", str(retained), "--output", str(out), "--budget-minutes", str(item["budget_minutes"])]
    error, code = None, 1
    with (out/"core.log").open("ab") as stream:
        process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT, start_new_session=True)
        try:
            code = process.wait(timeout=item["budget_minutes"]*60+900)
        except subprocess.TimeoutExpired:
            error, code = "outer_timeout", 124
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=15)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
    cp = out/"core-receipt.json"
    receipt = read(cp) if cp.exists() else None
    complete = code == 0 and receipt is not None and receipt.get("complete") is True and (out/FINAL).exists()
    run = {"result": RESULT, "source_commit": os.environ["GITHUB_SHA"], "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ.get("GITHUB_RUN_ATTEMPT", "1"), "complete": complete, "process_exit_code": code,
        "error": error, "core_receipt_sha256": sha(cp) if receipt is not None else None,
        "expanded_coordinates_exactly_certified": False, "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()}
    save(out/"run-receipt.json", run)
    for path in out.glob("*.tmp"):
        path.unlink()
    output_manifest(out)
    print("RUN_RECEIPT="+json.dumps(run), flush=True)
    if not complete:
        raise SystemExit(code or 1)


def verify(item, out, request):
    manifest = read(out/MANIFEST)
    assert manifest["result"] == RESULT and plain(read(out/REFERENCE)["manifest"]) == file_spec(out/MANIFEST)
    files = {row["file"]: plain(row) for row in manifest["files"]}
    assert len(files) == len(manifest["files"])
    assert set(files) == {p.name for p in out.iterdir() if p.is_file() and p.name not in (MANIFEST, REFERENCE)}
    for row in files.values():
        bound(out, row)
    retained, expanded = prepare(item, out, allow_download=False)
    tag = expected_tag(item, expanded)
    public, run = read(out/"public-actions-input.json"), read(out/"run-receipt.json")
    assert public["job"] == item and public["request_sha256"] == sha(request)
    assert public["expanded_sources"] == expanded
    assert public["expanded_job_sha256"] == fingerprint(dict(item, retained_sources=expanded))
    assert public["core_sha256"] == item["core_sha256"] and public["wrapper_sha256"] == item["wrapper_sha256"]
    assert public["source_commit"] == run["source_commit"]
    core = read(out/"core-receipt.json") if "core-receipt.json" in files else None
    if core is not None:
        assert core["result"] == RESULT and core["source_sha256"] == item["core_sha256"]
        assert run["core_receipt_sha256"] == files["core-receipt.json"]["sha256"]
        assert core["expanded_coordinates_exactly_certified"] is False
    else:
        assert run["core_receipt_sha256"] is None and run["complete"] is False
    stages = {}
    for name, row in files.items():
        if name.startswith(PREFIX) and name.endswith(".json.gz"):
            data = read(out/name)
            assert data["complete"] is True and data["configuration"] == tag
            stages[name] = row
    if FINAL not in files:
        print("PARTIAL_IO_REVIEW="+json.dumps({"complete": False, "stages": len(stages),
            "source_and_output_bytes_verified": True}), flush=True)
        raise SystemExit(1)
    final = read(out/FINAL)
    assert final["result"] == RESULT and final["complete"] is True and final["configuration"] == tag
    assert core is not None and core["complete"] is True and core["certificate_sha256"] == files[FINAL]["sha256"]
    assert run["complete"] is True and run["process_exit_code"] == 0
    for flag in ("actual_nontorsion_source_verified",
                 "original_comparison_logarithmic_first_jets_as_exact_expressions",
                 "original_comparison_first_jets_as_exact_expressions",
                 "all_new_inverse_nodes_have_original_nonzero_Hom_proofs",
                 "original_comparison_constants_preserved"):
        assert final[flag] is True
    for flag in ("old_CM_Hom_point_or_nontorsion_arithmetic_recomputed",
                 "expanded_coordinates_exactly_certified", "any_logarithmic_jet_proved_nonzero",
                 "original_value_rowspace_zero_A1_proved", "original_rigidification_computed",
                 "global_polar_divisors_computed", "actual_eta_or_height_computed"):
        assert final[flag] is False
    assert final["original_map_index"] == 4 and final["original_map_degree"] == 1206
    assert final["new_point_addition_count"] == 0 and final["imported_R844_node_count"] == 529
    inventory = read(bound(out, final["stage_manifest"]))
    assert inventory["complete"] is True and inventory["configuration"] == tag
    expected = {name: row for name, row in stages.items() if not name.startswith(PREFIX+"stage-manifest-")}
    assert {row["file"]: plain(row) for row in inventory["files"]} == expected
    assert len(expected) == final["complete_math_stage_count"] == 2
    for key in ("source_audit", "jet_program"):
        assert expected[final[key]["file"]] == plain(final[key])
    program = read(bound(out, final["jet_program"]))
    old_cert = read(retained/"POINTS"/PARENT_FINAL)
    old = read(bound(retained/"POINTS", old_cert["point_program"]))
    assert program["imported_R844_node_count"] == old["node_count"] == 529
    assert program["nodes"][:529] == old["nodes"] and program["imported_R844_nodes_unchanged"] is True
    known = {}
    for node in program["nodes"]:
        payload = {key: value for key, value in node.items() if key != "id"}
        assert fingerprint(payload) == node["id"] and node["id"] not in known
        assert all(key in known for key in node["inputs"])
        known[node["id"]] = payload
    assert len(known) == program["node_count"] == final["point_program_node_count"]
    assert all(value in known for value in program["roots"].values())
    assert program["original_parameter"] == "z=a-1" and program["original_differential"] == "dx/(2y)"
    assert program["source_original_point_program"] == {
        "source_group": "POINTS", **plain(old_cert["point_program"])}
    assert program["source_original_twelve_tangents"]["sha256"] == "32be372f46560ce7cfc0af40666cdc32b39170bfc7b6ec32b92ea747a0629e7e"
    point_records = {row["id"]: row for row in old["point_records"]}
    jets = program["point_first_jets"]
    assert [row["label"] for row in jets] == ["f", "g1", "g2", "g3", "g4", "g5"]
    for row in jets:
        point = point_records[row["original_point_id"]]
        assert row["original_Hom_coordinates"] == point["original_Hom_coordinates"]
        assert row["original_coordinates"] == point["coordinates"]
        assert row["nonzero_x_certified_by_original_Hom_word"] is True
        for key in ("h", "derivative_z_x", "derivative_z_y", "logarithmic_derivative_y2_minus_b",
                    "trace_logarithmic_derivative_y2_minus_b"):
            assert row[key] in known
    comparisons = program["original_comparison_first_jets"]
    assert [row["j"] for row in comparisons] == [1, 2, 3, 4, 5]
    for row, old_row in zip(comparisons, old["five_original_eta_addition_inputs"]):
        assert row["j"] == old_row["j"] and row["original_rj"] == old_row["original_rj"]
        assert row["original_comparison_value_root"] == old_row["comparison_function_value_root"]
        assert row["logarithmic_derivative_z"] in known and row["derivative_z"] in known
        assert row["actual_seven_sigma_trace_used"] is True
        assert row["original_value_and_all_norm_constants_unchanged"] is True
        assert row["original_c0_rigidification_applied"] is False
    for node in program["nodes"][529:]:
        if node["operation"] == "inverse":
            proof = node["nonzero_certificate"]
            point = point_records[proof["original_point_id"]]
            assert proof["original_Hom_coordinates"] == point["original_Hom_coordinates"]
            assert node["inputs"] == [point["coordinates"]["x"]]
            assert proof["source_same_point_nontorsion"] == program["source_actual_same_point_nontorsion"]
    print("COMPLETE_LOG_JET_IO_REVIEW="+json.dumps({
        "complete": True, "source_files": sum(len(s["files"]) for s in expanded.values()),
        "node_count": program["node_count"], "imported_R844_nodes_unchanged": True,
        "new_point_addition_count": 0, "original_comparison_count": 5,
        "expanded_coordinates_exactly_certified": False,
        "any_logarithmic_jet_proved_nonzero": False, "actual_eta_or_height_computed": False,
        "certificate": files[FINAL], "stage_manifest": final["stage_manifest"]}), flush=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=("compute", "verify"))
    parser.add_argument("--request", type=Path, default=REQUEST)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    item = read(args.request)["job"]
    guard(item, args.request)
    (compute if args.operation == "compute" else verify)(item, args.output, args.request)


if __name__ == "__main__":
    main()


