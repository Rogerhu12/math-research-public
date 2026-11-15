#!/usr/bin/env python3
"""Small source-bound candidate checks: standard-library artifact IO only."""
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
REQUEST = TOPIC/'notes/R792-CM-candidate-field-checks-public-request.json'
RESULT = 'R792-original-CM-candidate-field-checks'
FINAL = 'p41-original-CM-candidate-field-checks-certificate.json'
PREFIX = 'R792-CM-candidate-'
BUNDLE = 'R792-CM-candidate-retained-inputs.tar.gz'
MANIFEST = 'full-outputs-manifest.json'
REFERENCE = 'full-outputs-manifest-reference.json'
INPUT_RECEIPT = 'retained-inputs-receipt.json'
META = (MANIFEST,'run-receipt.json','core-receipt.json','public-actions-input.json')
PARENT_FINAL = 'p41-original-CM-response-beta-DAG-certificate.json'
PARENT_BUNDLE = 'R792-CM-DAG-retained-inputs.tar.gz'
DAG_IO_SHA = '96045ab00c4b5f4a674031ddb7100b07af98ab5bd5b8560ab56665c0d8cdee66'
DAG_CORE_SHA = 'afb49c1ac4245674d29364789e817b566517e1f5bf6d506cee684ed03fa34b8b'
FIELD_CORE_SHA = 'f196cb805d1ca91e8995866032a0a3ec3f96aac06e03b67a7c1f196fff759251'
IO = None
H64 = re.compile(r"[0-9a-f]{64}")

STRATEGY = {
    "input": "the completed 518-digit scalar-RR suggestions and original R791 h0",
    "field": "original Q(b,zeta), integral-coordinate conversion B=lambda*b, s=1+2*zeta",
    "candidate_x": "3*h0*(q^2-b)/d, only if candidate d is nonzero",
    "necessary_checks": ["c(q)=-q", "c(d)=-d", "q^2-b!=0", "d!=0", "x^3=q^2-b", "c(x)=zeta^2*x"],
    "original_value_rowspace_zero_A1_proved": False,
    "original_coordinates_accepted": False,
    "old_CM_RR_Hom_isogeny_constants_or_DAG_recomputed": False,
    "degree21_cubic_root_norm_algorithm_executed": False}


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
    path = S/safe(item["dag_wrapper"])
    assert path.name == "R792_public_original_CM_response_beta_DAG.py"
    assert sha(path) == item["dag_wrapper_sha256"] == DAG_IO_SHA
    source = importlib.util.spec_from_file_location("frozen_beta_DAG_IO_only", path)
    IO = importlib.util.module_from_spec(source)
    source.loader.exec_module(IO)
    IO.load_io(item)


def guard(item, request):
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("This consumer executes only in public repository Actions.")
    assert request.resolve() == REQUEST.resolve()
    assert item["result"] == RESULT and item["p"] == 41 and item["producer_inputs_pending"] is False
    assert item["core"] == "R792_original_CM_candidate_field_checks.py"
    assert item["wrapper"] == "R792_public_original_CM_candidate_field_checks.py"
    for name, pin in (("core", item["core_sha256"]), ("wrapper", item["wrapper_sha256"]),
                      ("dag_core", DAG_CORE_SHA), ("field_core", FIELD_CORE_SHA)):
        assert sha(S/safe(item[name])) == pin == item[name+"_sha256"]
    for proof in item["proofs"].values():
        assert sha(topic_path(proof["path"])) == proof["sha256"]
    assert sha(REPO/"README.md") == item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md") == item["readme_sha256"]["topic"]
    assert 0 < item["budget_minutes"] <= 300
    parent = item["parent_source"]
    assert parent["result"] == "R792-original-CM-response-beta-DAG" and parent["core_sha256"] == DAG_CORE_SHA
    assert parent["expected_conclusion"] == "success"
    load_io(item)


def parent_names(directory):
    directory = Path(directory)
    cert = read(directory/PARENT_FINAL)
    return sorted(set(META) | {PARENT_FINAL, INPUT_RECEIPT, cert["stage_manifest"]["file"]} |
                  {cert[key]["file"] for key in ("source_audit", "denominator_nonzero_proofs", "original_point_DAG", "downstream_interface")})


def review_parent(item, retained):
    parent, root = item["parent_source"], retained/"DAG"
    assert sha(root/MANIFEST) == parent["manifest_sha256"] and (root/MANIFEST).stat().st_size == parent["manifest_bytes"]
    m = read(root/MANIFEST)
    assert m["result"] == parent["result"] and len(m["files"]) == parent["manifest_file_count"]
    inventory = {row["file"]: plain(row) for row in m["files"]}
    inventory[MANIFEST] = file_spec(root/MANIFEST)
    names = parent_names(root)
    files = {name: inventory[name] for name in names}
    assert len(names) == parent["selected_file_count"]
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
    assert core["source_sha256"] == public["core_sha256"] == parent["core_sha256"]
    assert public["wrapper_sha256"] == parent["wrapper_sha256"] == DAG_IO_SHA
    assert public["root_readme_sha256"] == parent["original_readme_sha256"]["root"]
    assert public["topic_readme_sha256"] == parent["original_readme_sha256"]["topic"]
    assert cert["complete"] is True and fingerprint(cert["configuration"]) == parent["configuration_sha256"]
    assert cert["exact_original_beta_C_as_expression_certified"] is True
    assert cert["expanded_coordinates_exactly_certified"] is False
    receipt = read(root/INPUT_RECEIPT)
    assert receipt["sources"] == public["job"]["sources"]
    assert plain(receipt["input_bundle"]) == plain(parent["input_bundle"]) == inventory[PARENT_BUNDLE]
    children = IO.review_all(public["job"], retained)
    assert children == receipt["expanded_sources"] == public["expanded_sources"]
    tag = cert["configuration"]
    assert IO.expected_tag(public["job"], children) == tag
    for name in names:
        if name.endswith(".json.gz"):
            stage = read(root/name)
            assert stage["complete"] is True and stage["configuration"] == tag
    for row in read(bound(root, cert["stage_manifest"]))["files"]:
        assert files[row["file"]] == plain(row)
    return dict(children, DAG=dict(parent, files=files))


def prepare(item, out, allow_download=True):
    retained = out.parent/(out.name+"-retained")
    if (out/INPUT_RECEIPT).exists() and (out/BUNDLE).exists():
        receipt = read(out/INPUT_RECEIPT)
        assert receipt["parent_source"] == item["parent_source"]
        assert file_spec(out/BUNDLE) == receipt["input_bundle"]
        IO.unpack_sources(out/BUNDLE, retained, receipt["expanded_sources"])
        expanded = review_parent(item, retained)
        assert expanded == receipt["expanded_sources"]
        return retained, expanded
    assert allow_download
    parent, root = item["parent_source"], retained/"DAG"
    root.mkdir(parents=True, exist_ok=True)
    transfer = out.parent/(out.name+"-parent-transfer")
    archive = IO.IO.Archive(parent, transfer, whole=True)
    try:
        archive.extract_bound(MANIFEST, parent["manifest_sha256"], root/MANIFEST, parent["manifest_bytes"])
        files = {row["file"]: plain(row) for row in read(root/MANIFEST)["files"]}
        def take(names):
            archive.extract_many([(name, files[name]["sha256"], root/name, files[name]["bytes"])
                                  for name in names if name != MANIFEST])
        take([PARENT_FINAL])
        take(parent_names(root))
        bundle = plain(parent["input_bundle"])
        assert files[PARENT_BUNDLE] == bundle
        archive.extract_bound(PARENT_BUNDLE, bundle["sha256"], transfer/PARENT_BUNDLE, bundle["bytes"])
        receipt = read(root/INPUT_RECEIPT)
        assert file_spec(transfer/PARENT_BUNDLE) == bundle == plain(receipt["input_bundle"])
        IO.unpack_sources(transfer/PARENT_BUNDLE, retained, receipt["expanded_sources"])
        expanded = review_parent(item, retained)
        IO.pack_sources(retained, expanded, out/BUNDLE)
        source_receipt = {"result": RESULT, "parent_source": parent, "expanded_sources": expanded,
            "input_bundle": file_spec(out/BUNDLE), "source_transport": archive.receipt(),
            "selected_source_file_count": sum(len(value["files"]) for value in expanded.values()),
            "all_source_bytes_and_original_parent_child_bindings_verified": True,
            "old_CM_RR_Hom_or_DAG_arithmetic_recomputed": False}
        save(out/INPUT_RECEIPT, source_receipt)
        print("INPUT_REVIEW="+json.dumps({key: source_receipt[key] for key in ("selected_source_file_count", "input_bundle",
            "all_source_bytes_and_original_parent_child_bindings_verified", "old_CM_RR_Hom_or_DAG_arithmetic_recomputed")}), flush=True)
        return retained, expanded
    finally:
        archive.close()


def expected_tag(item, expanded):
    return {"result": RESULT, "source_sha256": item["core_sha256"], "p": 41, "python_flint": "0.9.0",
        "dag_core_sha256": DAG_CORE_SHA, "field_core_sha256": FIELD_CORE_SHA,
        "proofs": item["proofs"], "source_identities": {key: IO.source_identity(value) for key, value in expanded.items()},
        "strategy": STRATEGY, "budget_excluded_from_mathematical_identity": True}


def stable_job(item):
    return {key: value for key, value in item.items() if key not in ("resume", "budget_minutes")}


def restore(item, out):
    source = item.get("resume")
    if source is None:
        return
    assert source["result"] == RESULT and source["core_sha256"] == item["core_sha256"]
    root = out.parent/(out.name+"-resume")
    archive = IO.IO.Archive(source, root, whole=False)
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
        "--dag-core", str(S/item["dag_core"]), "--field-core", str(S/item["field_core"]),
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
        "original_coordinates_accepted": False, "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()}
    save(out/"run-receipt.json", run)
    for path in out.glob("*.tmp"):
        path.unlink()
    output_manifest(out)
    print("RUN_RECEIPT="+json.dumps(run), flush=True)
    if not complete:
        raise SystemExit(code or 1)


def verify(item, out, request):
    m = read(out/MANIFEST)
    assert m["result"] == RESULT and plain(read(out/REFERENCE)["manifest"]) == file_spec(out/MANIFEST)
    files = {row["file"]: plain(row) for row in m["files"]}
    assert len(files) == len(m["files"])
    assert set(files) == {p.name for p in out.iterdir() if p.is_file() and p.name not in (MANIFEST, REFERENCE)}
    for row in files.values():
        bound(out, row)
    retained, expanded = prepare(item, out, allow_download=False)
    tag = expected_tag(item, expanded)
    public, run = read(out/"public-actions-input.json"), read(out/"run-receipt.json")
    assert public["job"] == item and public["request_sha256"] == sha(request)
    assert public["expanded_sources"] == expanded and public["expanded_job_sha256"] == fingerprint(dict(item, retained_sources=expanded))
    assert public["core_sha256"] == item["core_sha256"] and public["wrapper_sha256"] == item["wrapper_sha256"]
    assert public["source_commit"] == run["source_commit"]
    core = None
    if "core-receipt.json" in files:
        core = read(out/"core-receipt.json")
        assert core["result"] == RESULT and core["source_sha256"] == item["core_sha256"]
        assert run["core_receipt_sha256"] == files["core-receipt.json"]["sha256"]
        assert core["original_coordinates_accepted"] is False
    else:
        assert run["core_receipt_sha256"] is None and run["complete"] is False
    stages = {}
    for name, row in files.items():
        if name.startswith(PREFIX) and name.endswith(".json.gz"):
            data = read(out/name)
            assert data["complete"] is True and data["configuration"] == tag
            stages[name] = row
    if FINAL not in files:
        print("PARTIAL_IO_REVIEW="+json.dumps({"complete": False, "stages": len(stages), "source_and_output_bytes_verified": True}), flush=True)
        raise SystemExit(1)
    final = read(out/FINAL)
    assert final["result"] == RESULT and final["complete"] is True and final["configuration"] == tag
    assert core["complete"] is True and core["certificate_sha256"] == files[FINAL]["sha256"]
    assert run["complete"] is True and run["process_exit_code"] == 0
    for flag in ("original_value_rowspace_zero_A1_proved", "original_coordinates_accepted",
                 "expanded_original_coordinates_exactly_certified", "old_R792_success_recipe_produced", "actual_eta_or_height_computed",
                 "old_CM_RR_Hom_or_isogeny_constants_recomputed", "degree21_cubic_root_norm_algorithm_executed"):
        assert final[flag] is False
    inventory = read(bound(out, final["stage_manifest"]))
    assert inventory["complete"] is True and inventory["configuration"] == tag
    expected = {name: row for name, row in stages.items() if not name.startswith(PREFIX+"stage-manifest-")}
    assert {row["file"]: plain(row) for row in inventory["files"]} == expected
    for key in ("exact_candidate_inputs", "necessary_field_checks"):
        assert expected[final[key]["file"]] == plain(final[key])
    checks = read(bound(out, final["necessary_field_checks"]))
    assert checks["flags"] == final["flags"] and checks["all_necessary_field_checks_passed"] == final["all_necessary_field_checks_passed"]
    assert isinstance(final["all_necessary_field_checks_passed"], bool)
    assert checks["original_value_rowspace_zero_A1_proved"] is False and checks["original_coordinates_accepted"] is False
    print("COMPLETE_IO_REVIEW="+json.dumps({"complete": True, "source_files": sum(len(s["files"]) for s in expanded.values()),
        "all_necessary_field_checks_passed": final["all_necessary_field_checks_passed"], "flags": final["flags"],
        "original_coordinates_accepted": False, "certificate": files[FINAL], "stage_manifest": final["stage_manifest"]}), flush=True)


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


