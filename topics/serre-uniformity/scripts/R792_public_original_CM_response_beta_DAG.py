#!/usr/bin/env python3
"""Read-only public IO runner for the original beta_C expression consumer.

Only source metadata, compressed bytes and schema are processed here.  The
mathematical core is never imported.  Historical rule hashes are separate.
"""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import tarfile
import time

S = Path(__file__).resolve().parent
TOPIC = S.parent
REPO = TOPIC.parents[1]
REQUEST = TOPIC/"notes/R792-CM-response-beta-DAG-public-request.json"
RESULT = "R792-original-CM-response-beta-DAG"
FINAL = "p41-original-CM-response-beta-DAG-certificate.json"
PREFIX = "R792-CM-DAG-"
BUNDLE = "R792-CM-DAG-retained-inputs.tar.gz"
INPUT_RECEIPT = "retained-inputs-receipt.json"
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"
META = (MANIFEST, "run-receipt.json", "core-receipt.json", "public-actions-input.json")
BASE_KEYS = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
RANGE_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
H64 = re.compile(r"[0-9a-f]{64}")
IO = None
SOURCES = {
    "CM": {"result": "R787-original-implicit-CM-value", "certificate": "p41-original-implicit-CM-value-certificate.json"},
    "R791": {"result": "R791-original-Hom-Galois-and-eta-inputs", "certificate": "p41-original-Hom-Galois-and-eta-input-certificate.json"}}
CM_KEYS = ("source_audit", "implicit_expression", "denominator_unit_witness", "power5_CM_values_and_jets", "exact_eZ",
           "A_response", "B_response", "modular_value", "coordinate_candidates", "stage_manifest")

STRATEGY = {
    "existing_formula": "R791(791R.16), with R792(792.7) and the original nonzero h0",
    "point": "beta_C=f4(c1) in C(L): y^2=x^3+b; degree1206; f4(c0)=O",
    "coordinate": "z=a-1 at original c1=4424",
    "exact_response_semantics": "unit-chart linear functionals, never the modular response arrays",
    "nonzero_denominators": "B0 from completed modular witness; Q,N from original geometry",
    "output_representation": "content-addressed exact arithmetic DAG with proof-bound inverse nodes",
    "primitive_descent": "f_R(c1)=[1-zeta^2]f4(c1), original v and kappa retained",
    "numerical_expansion_or_root_search": False,
    "old_CM_Hom_or_Norm_arithmetic_recomputed": False,
    "point_additions_eta_or_heights_in_scope": False}


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


def load_io(item):
    global IO
    path = S/safe(item["io_helper"])
    assert path.name == "R824_public_original_global_polar_generators.py"
    assert sha(path) == item["io_helper_sha256"] == RANGE_SHA
    module = importlib.util.spec_from_file_location("implicit_CM_frozen_Range_only_IO", path)
    IO = importlib.util.module_from_spec(module)
    module.loader.exec_module(IO)


def pack_sources(retained, expanded, target):
    temporary = target.with_name(target.name+".tmp")
    with temporary.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, compresslevel=2) as compressed:
            with tarfile.open(fileobj=compressed, mode="w") as archive:
                for label in sorted(expanded):
                    for name in sorted(expanded[label]["files"]):
                        path = bound(retained/label, expanded[label]["files"][name])
                        member = archive.gettarinfo(str(path), arcname=label+"/"+name)
                        member.uid = member.gid = 0
                        member.uname = member.gname = ""
                        member.mtime = 0
                        with path.open("rb") as stream:
                            archive.addfile(member, stream)
    temporary.replace(target)


def unpack_sources(path, retained, inventory):
    expected = {label+"/"+name: row for label, source in inventory.items() for name, row in source["files"].items()}
    seen = set()
    with tarfile.open(path, "r:gz") as archive:
        for member in archive:
            assert member.isfile() and member.name in expected and member.name not in seen
            assert not Path(member.name).is_absolute() and ".." not in Path(member.name).parts
            row = expected[member.name]
            assert member.size == row["bytes"]
            output = retained/member.name
            output.parent.mkdir(parents=True, exist_ok=True)
            temporary = output.with_name(output.name+".tmp")
            digest = hashlib.sha256()
            with archive.extractfile(member) as source, temporary.open("wb") as stream:
                for block in iter(lambda: source.read(1024*1024), b""):
                    digest.update(block)
                    stream.write(block)
            assert digest.hexdigest() == row["sha256"]
            temporary.replace(output)
            seen.add(member.name)
    assert seen == set(expected)


def output_manifest(out):
    rows = [file_spec(path) for path in sorted(out.iterdir()) if path.is_file() and
            path.name not in (MANIFEST, REFERENCE) and not path.name.endswith(".tmp")]
    save(out/MANIFEST, {"result": RESULT, "files": rows,
        "temporary_active_checkpoint_retention_days": 1,
        "reproducible_tables_in_git_or_release": False})
    save(out/REFERENCE, {"result": RESULT, "manifest": file_spec(out/MANIFEST)})


def source_identity(source):
    answer = {key: source[key] for key in BASE_KEYS}
    answer.update(configuration_sha256=source["configuration_sha256"],
                  selected_files_sha256=source["selected_files_sha256"], certificate=plain(source["certificate"]))
    return answer


def selected_names(label, directory):
    directory = Path(directory)
    names = set(META) | {SOURCES[label]["certificate"], INPUT_RECEIPT}
    certificate = read(directory/SOURCES[label]["certificate"])
    if label == "CM":
        names.update(certificate[key]["file"] for key in CM_KEYS)
        jets = read(directory/certificate["power5_CM_values_and_jets"]["file"])
        ez = read(directory/certificate["exact_eZ"]["file"])
        names.update(row["file"] for row in jets["completed_blocks"])
        names.update(row["file"] for row in ez["blocks"])
    else:
        names.update(row["file"] for row in certificate["stages"])
    return sorted(names)


def guard(item, request):
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Execution belongs to this public repository's Actions.")
    assert request.resolve() == REQUEST.resolve()
    assert item["result"] == RESULT and item["p"] == 41 and item["producer_inputs_pending"] is False
    assert item["core"] == "R792_original_CM_response_beta_DAG.py"
    assert item["wrapper"] == "R792_public_original_CM_response_beta_DAG.py"
    assert sha(S/item["core"]) == item["core_sha256"] and sha(__file__) == item["wrapper_sha256"]
    assert set(item["proofs"]) == {"interface", "R791", "R792", "unit_chart"}
    for proof in item["proofs"].values():
        assert sha(topic_path(proof["path"])) == proof["sha256"]
    assert sha(REPO/"README.md") == item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md") == item["readme_sha256"]["topic"]
    assert 0 < item["budget_minutes"] <= 300 and set(item["sources"]) == set(SOURCES)
    for label, source in item["sources"].items():
        assert source["result"] == SOURCES[label]["result"] and source["expected_conclusion"] == "success"
        assert source["manifest_bytes"] > 0 and source["manifest_file_count"] > 0
        assert H64.fullmatch(source["configuration_sha256"]) and H64.fullmatch(source["selected_files_sha256"])
    load_io(item)


def review_source(label, item, directory):
    source, directory = item["sources"][label], Path(directory)
    assert (directory/MANIFEST).stat().st_size == source["manifest_bytes"]
    assert sha(directory/MANIFEST) == source["manifest_sha256"]
    manifest = read(directory/MANIFEST)
    assert manifest["result"] == source["result"]
    inventory = {row["file"]: plain(row) for row in manifest["files"]}
    assert len(inventory) == len(manifest["files"]) == source["manifest_file_count"]
    inventory[MANIFEST] = file_spec(directory/MANIFEST)
    names = selected_names(label, directory)
    assert len(names) == source["selected_file_count"]
    files = {name: inventory[name] for name in names}
    for row in files.values():
        bound(directory, row)
    assert fingerprint([files[name] for name in names]) == source["selected_files_sha256"]
    run, core, public = (read(directory/name) for name in META[1:])
    cert = read(directory/SOURCES[label]["certificate"])
    assert files[SOURCES[label]["certificate"]] == plain(source["certificate"])
    assert run["result"] == core["result"] == public["result"] == cert["result"] == source["result"]
    assert str(run["workflow_run_id"]) == str(source["run_id"])
    assert run["source_commit"] == public["source_commit"] == source["source_commit"]
    assert run["complete"] is True and run["process_exit_code"] == 0 and run.get("error") is None
    assert core["complete"] is True and core["source_sha256"] == source["core_sha256"]
    assert core["certificate_sha256"] == source["certificate"]["sha256"]
    if run.get("core_receipt_sha256") is not None:
        assert run["core_receipt_sha256"] == files["core-receipt.json"]["sha256"]
    assert public.get("core_sha256", public["job"]["core_sha256"]) == source["core_sha256"]
    assert public.get("wrapper_sha256", public.get("driver_sha256")) == source["wrapper_sha256"]
    assert public["root_readme_sha256"] == source["original_readme_sha256"]["root"]
    assert public["topic_readme_sha256"] == source["original_readme_sha256"]["topic"]
    assert cert["complete"] is True
    tag = cert["configuration"]
    assert fingerprint(tag) == source["configuration_sha256"] and tag["source_sha256"] == source["core_sha256"]
    if label == "CM":
        assert cert["original_map_index"] == 4 and cert["original_map_degree"] == "1206"
        assert cert["source_Dixon_digits"] == 518
        assert cert["exact_implicit_relation_defined"] is True
        assert cert["exact_finite_y_implicit_expression_defined"] is True
        assert cert["all_14_branches_units"] is True and cert["characteristic_zero_B0_nonzero_certified"] is True
        assert cert["expanded_coordinates_exactly_certified"] is False
        assert cert["old_R792_success_recipe_produced"] is False
        mathfiles = {row["file"]: plain(row) for row in read(bound(directory, cert["stage_manifest"]))["files"]}
        for key in CM_KEYS:
            row = plain(cert[key])
            assert row == files[row["file"]]
            if key != "stage_manifest":
                assert row == mathfiles[row["file"]]
        for name in names:
            if not name.endswith(".json.gz"):
                continue
            data = read(directory/name)
            assert data["complete"] is True and data["configuration"] == tag
            if name != cert["stage_manifest"]["file"]:
                assert files[name] == mathfiles[name]
    else:
        assert cert["original_index4_c1_tangent_nonzero"] is True
        assert cert["selected_real_map_recipe"] == "f+c(f)" and cert["selected_real_map_degree"] == "3618"
        for row in cert["stages"]:
            row = plain(row)
            assert files[row["file"]] == row
            data = read(directory/row["file"])
            assert data["complete"] is True and data["configuration"] == tag
    return dict(source, files=files)


def download_source(label, item, directory, transfer):
    source, directory = item["sources"][label], Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    archive = IO.Archive(source, transfer, whole=False)
    try:
        archive.extract_bound(MANIFEST, source["manifest_sha256"], directory/MANIFEST, source["manifest_bytes"])
        files = {row["file"]: plain(row) for row in read(directory/MANIFEST)["files"]}
        def take(names):
            archive.extract_many([(name, files[name]["sha256"], directory/name, files[name]["bytes"])
                                  for name in sorted(set(names)) if name != MANIFEST])
        take(set(META) | {SOURCES[label]["certificate"], INPUT_RECEIPT})
        cert = read(directory/SOURCES[label]["certificate"])
        if label == "CM":
            take(cert[key]["file"] for key in CM_KEYS)
        else:
            take(row["file"] for row in cert["stages"])
        take(selected_names(label, directory))
        return archive.receipt()
    finally:
        archive.close()


def review_all(item, retained):
    return {label: review_source(label, item, retained/label) for label in SOURCES}


def prepare_sources(item, out, allow_download=True):
    retained = out.parent/(out.name+"-retained")
    receipt_path = out/INPUT_RECEIPT
    if receipt_path.exists() and (out/BUNDLE).exists():
        old = read(receipt_path)
        assert old["result"] == RESULT and old["sources"] == item["sources"]
        assert file_spec(out/BUNDLE) == old["input_bundle"]
        unpack_sources(out/BUNDLE, retained, old["expanded_sources"])
        expanded = review_all(item, retained)
        assert expanded == old["expanded_sources"]
        return retained, expanded
    assert allow_download
    transfer = out.parent/(out.name+"-transfers")
    transports = [download_source(label, item, retained/label, transfer/label) for label in SOURCES]
    expanded = review_all(item, retained)
    pack_sources(retained, expanded, out/BUNDLE)
    receipt = {"result": RESULT, "sources": item["sources"], "expanded_sources": expanded,
        "input_bundle": file_spec(out/BUNDLE), "source_transport_receipts": transports,
        "selected_original_file_count": sum(len(s["files"]) for s in expanded.values()),
        "all_selected_original_bytes_and_schema_verified": True,
        "CM_full_input_carrier_downloaded": False, "old_mathematics_recomputed": False,
        "historical_readmes_compared_to_current_rules": False}
    save(receipt_path, receipt)
    print("INPUT_REVIEW="+json.dumps({key: receipt[key] for key in ("selected_original_file_count", "input_bundle",
        "all_selected_original_bytes_and_schema_verified", "CM_full_input_carrier_downloaded", "old_mathematics_recomputed")}), flush=True)
    return retained, expanded


def expected_tag(item, expanded):
    return {"result": RESULT, "source_sha256": item["core_sha256"], "p": 41,
        "proofs": item["proofs"], "source_identities": {key: source_identity(value) for key, value in expanded.items()},
        "strategy": STRATEGY, "arithmetic": "source-bound exact symbolic DAG; no coordinate reconstruction",
        "budget_excluded_from_mathematical_identity": True}


def stable_job(item):
    return {key: value for key, value in item.items() if key not in ("resume", "budget_minutes")}


def restore(item, out):
    source = item.get("resume")
    if source is None:
        return
    assert source["result"] == RESULT and source["core_sha256"] == item["core_sha256"]
    root = out.parent/(out.name+"-resume")
    archive = IO.Archive(source, root, whole=False)
    try:
        archive.extract_bound(MANIFEST, source["manifest_sha256"], root/MANIFEST, source["manifest_bytes"])
        data = read(root/MANIFEST)
        assert data["result"] == RESULT
        files = {row["file"]: plain(row) for row in data["files"]}
        for name in ("public-actions-input.json", "run-receipt.json", INPUT_RECEIPT):
            row = files[name]
            archive.extract_bound(name, row["sha256"], root/name, row["bytes"])
        old, run = read(root/"public-actions-input.json"), read(root/"run-receipt.json")
        assert stable_job(old["job"]) == stable_job(item)
        assert old["source_commit"] == run["source_commit"] == source["source_commit"]
        assert str(run["workflow_run_id"]) == str(source["run_id"])
        wanted = [name for name in files if name.startswith(PREFIX) and name.endswith(".json.gz")]
        wanted += [BUNDLE, INPUT_RECEIPT]
        if FINAL in files:
            wanted.append(FINAL)
        archive.extract_many([(name, files[name]["sha256"], out/name, files[name]["bytes"]) for name in wanted])
        tag = expected_tag(item, read(out/INPUT_RECEIPT)["expanded_sources"])
        for name in wanted:
            if name.startswith(PREFIX) and name.endswith(".json.gz"):
                stage = read(out/name)
                assert stage["complete"] is True and stage["configuration"] == tag
        if (out/FINAL).exists():
            final = read(out/FINAL)
            assert final["complete"] is True and final["configuration"] == tag
            for row in read(bound(out, final["stage_manifest"]))["files"]:
                bound(out, row)
        save(out/"resume-source-receipt.json", {"result": RESULT, "source": source,
            "transport": archive.receipt(), "mathematical_stages_recomputed_by_restore": False})
    finally:
        archive.close()


def compute(item, out, request):
    out.mkdir(parents=True, exist_ok=True)
    restore(item, out)
    retained, expanded = prepare_sources(item, out)
    config = dict(item, sources=expanded)
    config_path = out.parent/(out.name+"-expanded-config.json")
    save(config_path, config)
    save(out/"public-actions-input.json", {"result": RESULT, "source_commit": os.environ["GITHUB_SHA"],
        "source_repository": os.environ["GITHUB_REPOSITORY"], "job": item,
        "expanded_job_sha256": fingerprint(config), "expanded_sources": expanded,
        "core_sha256": item["core_sha256"], "wrapper_sha256": item["wrapper_sha256"],
        "request_sha256": sha(request), "proofs": item["proofs"],
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    command = [sys.executable, str(S/item["core"]), "--config", str(config_path), "--topic", str(TOPIC),
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
    core = read(cp) if cp.exists() else None
    complete = code == 0 and core is not None and core.get("complete") is True and (out/FINAL).exists()
    run = {"result": RESULT, "complete": complete, "process_exit_code": code, "error": error,
        "source_commit": os.environ["GITHUB_SHA"], "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ.get("GITHUB_RUN_ATTEMPT", "1"),
        "core_receipt_sha256": sha(cp) if core is not None else None,
        "expanded_coordinates_exactly_certified": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()}
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
    assert set(files) == {path.name for path in out.iterdir() if path.is_file() and path.name not in (MANIFEST, REFERENCE)}
    for row in files.values():
        bound(out, row)
    retained, expanded = prepare_sources(item, out, allow_download=False)
    tag = expected_tag(item, expanded)
    public, run = read(out/"public-actions-input.json"), read(out/"run-receipt.json")
    assert public["job"] == item and public["request_sha256"] == sha(request)
    assert public["expanded_sources"] == expanded and public["expanded_job_sha256"] == fingerprint(dict(item, sources=expanded))
    assert public["core_sha256"] == item["core_sha256"] and public["wrapper_sha256"] == item["wrapper_sha256"]
    assert public["source_commit"] == run["source_commit"]
    assert public["root_readme_sha256"] == item["readme_sha256"]["root"]
    assert public["topic_readme_sha256"] == item["readme_sha256"]["topic"]
    core = None
    if "core-receipt.json" in files:
        core = read(out/"core-receipt.json")
        assert run["core_receipt_sha256"] == files["core-receipt.json"]["sha256"]
        assert core["result"] == RESULT and core["source_sha256"] == item["core_sha256"]
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
        print("PARTIAL_IO_REVIEW="+json.dumps({"completed_stage_count": len(stages), "core_receipt_present": core is not None,
            "all_bytes_and_sources_verified": True, "complete": False}), flush=True)
        raise SystemExit(1)
    final = read(out/FINAL)
    assert final["complete"] is True and final["result"] == RESULT and final["configuration"] == tag
    assert run["complete"] is True and run["process_exit_code"] == 0 and core["complete"] is True
    assert core["certificate_sha256"] == files[FINAL]["sha256"]
    assert final["original_map_index"] == 4 and final["original_map_degree"] == "1206"
    assert final["original_c1_coordinate"] == "z=a-1"
    for key in ("exact_original_beta_C_as_expression_certified", "exact_original_descent_point_as_expression_certified"):
        assert final[key] is True
    for key in ("expanded_coordinates_exactly_certified", "old_R792_expanded_coordinate_recipe_produced",
                "original_abstract_A_coordinate_preimage_recovered", "actual_eta_or_height_computed", "new_CM_Hom_root_or_Norm_arithmetic"):
        assert final[key] is False
    inventory = read(bound(out, final["stage_manifest"]))
    assert inventory["complete"] is True and inventory["configuration"] == tag
    current = {row["file"]: plain(row) for row in inventory["files"]}
    assert current == {name: row for name, row in stages.items() if not name.startswith(PREFIX+"stage-manifest-")}
    for key in ("source_audit", "denominator_nonzero_proofs", "original_point_DAG", "downstream_interface"):
        row = plain(final[key])
        assert current[row["file"]] == row
    program = read(bound(out, final["original_point_DAG"]))
    assert program["format"] == "original-L-arithmetic-DAG-v1"
    assert program["expanded_coordinates_exactly_certified"] is False
    seen = set()
    for node in program["nodes"]:
        assert set(node["inputs"]) <= seen
        payload = {key: value for key, value in node.items() if key != "id"}
        assert fingerprint(payload) == node["id"] and node["id"] not in seen
        seen.add(node["id"])
    assert program["node_count"] == len(seen) and set(program["roots"].values()) <= seen
    assert set(program["exact_response_leaves"]) == {"A0", "A1", "B0", "B1"}
    print("COMPLETE_IO_REVIEW="+json.dumps({"complete": True, "output_manifest_files": len(files),
        "retained_source_files": sum(len(s["files"]) for s in expanded.values()), "node_count": program["node_count"],
        "beta_C_exact_expression": True, "f_R_c1_exact_expression": True, "expanded_coordinates_exactly_certified": False,
        "actual_eta_or_height_computed": False, "certificate": files[FINAL], "stage_manifest": final["stage_manifest"]}), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=("compute", "verify"))
    parser.add_argument("--request", type=Path, default=REQUEST)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    item = read(args.request)["job"]
    guard(item, args.request)
    if args.operation == "compute":
        compute(item, args.output, args.request)
    else:
        verify(item, args.output, args.request)


if __name__ == "__main__":
    main()


