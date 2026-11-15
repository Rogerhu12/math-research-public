#!/usr/bin/env python3
"""Standard-library IO runner for the original implicit CM value consumer.

No mathematical core is imported.  Historical source README hashes are bound
separately from current execution rules.  Range transfer verifies the selected
members; the advertised whole ZIP digest is not called a new whole-ZIP hash.
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
REQUEST = TOPIC/"notes/R787-implicit-CM-value-public-request.json"
RESULT = "R787-original-implicit-CM-value"
FINAL = "p41-original-implicit-CM-value-certificate.json"
PREFIX = "R787-implicit-CM-"
BUNDLE = "R787-implicit-CM-retained-inputs.tar.gz"
INPUT_RECEIPT = "retained-inputs-receipt.json"
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"
META = (MANIFEST, "run-receipt.json", "core-receipt.json", "public-actions-input.json")
BASE_KEYS = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
RANGE_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
OLD_TAG_SHA = "71ea66416a42e024de61cf5927bc493fbc8422dc1b5970d75c51bd788d88529d"
CURRENT = "R787-prime-1000000753-dixon-00000518.json.gz"
CHART = "R787-prime-1000000753-chart.json.gz"
BLOCKS = "R787-prime-1000000753-rational-blocks.json.gz"
SELECTION = "R787-prime-1000000753-selection.json.gz"
R790_BUNDLE = "R790-retained-producer-inputs.tar.gz"
SOURCES = {
    "R787": {"result": "R787-original-power5-function-relation", "certificate": None},
    "R790": {"result": "R790-original-CM-fiber-jets", "certificate": "p41-original-CM-fiber-jets-certificate.json"},
    "R775": {"result": "R775-p41-original-K-defined-RR-bases", "certificate": "p41-original-K-defined-RR-basis-certificate.json"},
    "R786": {"result": "R786-exact-original-power5-short-basis", "certificate": "p41-exact-original-power5-short-basis-certificate.json"}}
BASIS_NAMES = ["R775-basis-M2.json.gz"]+["R775-basis-power-"+str(i)+".json.gz" for i in range(2, 6)]
H64 = re.compile(r"[0-9a-f]{64}")
DECIMAL = re.compile(r"-?(0|[1-9][0-9]*)")
IO = None
STRATEGY = {
    "CM_target": "original P1 over c1=4424, z=a-1",
    "exact_K_basis": "1,s; s=1+2*zeta; s^2=-3",
    "integral_L_basis": "B^i*s^j, j=0..1 outer, i=0..6; B=lambda*b",
    "product_rule": "(v,d)*(w,e)=(v*w,d*w+v*e)",
    "denominator_response": "exact e_j Z first; no separate Z*C expansion",
    "modular_inverse": "stored branch evaluation inverse at ell, then scalar Newton doubling",
    "coordinate_reconstruction": "one strict scalar RR suggestion per coordinate; never exact acceptance",
    "accurate_acceptance_executed": False,
    "old_q_rows_Schur_inverse_Dixon_CM_traces_recomputed": False,
    "fixed_block_size": 32}


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


def source_identity(source):
    answer = {key: source[key] for key in BASE_KEYS}
    answer.update(configuration_sha256=source["configuration_sha256"],
                  selected_files_sha256=source["selected_files_sha256"])
    if source.get("certificate"):
        answer["certificate"] = source["certificate"]
    return answer


def selected_names(label):
    names = set(META)
    certificate = SOURCES[label]["certificate"]
    if certificate:
        names.add(certificate)
    if label == "R787":
        names.update((CURRENT, CHART, BLOCKS, SELECTION))
    elif label == "R790":
        names.add("R790-stage-manifest.json.gz")
        names.update("R790-M2-CM-jet-"+str(i).zfill(4)+".json.gz" for i in range(146))
    elif label == "R775":
        names.update(BASIS_NAMES)
    else:
        names.add("R786-exact-power5-basis-index.json.gz")
    return sorted(names)


def load_io(item):
    global IO
    path = S/safe(item["io_helper"])
    assert path.name == "R824_public_original_global_polar_generators.py"
    assert sha(path) == item["io_helper_sha256"] == RANGE_SHA
    module = importlib.util.spec_from_file_location("implicit_CM_frozen_Range_only_IO", path)
    IO = importlib.util.module_from_spec(module)
    module.loader.exec_module(IO)


def guard(item, request):
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Execution belongs to this public repository's GitHub Actions.")
    assert request.resolve() == REQUEST.resolve()
    assert item["result"] == RESULT and item["p"] == 41 and item["producer_inputs_pending"] is False
    assert item["core"] == "R787_implicit_CM_value.py" and item["wrapper"] == "R787_implicit_CM_value_public.py"
    assert sha(S/item["core"]) == item["core_sha256"] and sha(__file__) == item["wrapper_sha256"]
    assert sha(topic_path(item["proof"])) == item["proof_sha256"]
    assert sha(REPO/"README.md") == item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md") == item["readme_sha256"]["topic"]
    assert 0 < item["budget_minutes"] <= 300 and set(item["sources"]) == set(SOURCES)
    for label, source in item["sources"].items():
        assert source["result"] == SOURCES[label]["result"]
        assert source["selected_file_count"] == len(selected_names(label))
        assert H64.fullmatch(source["selected_files_sha256"])
        assert H64.fullmatch(source["configuration_sha256"])
        assert source["manifest_bytes"] > 0 and source["manifest_file_count"] > 0
    assert item["sources"]["R787"]["configuration_sha256"] == OLD_TAG_SHA
    assert item["sources"]["R787"]["expected_conclusion"] == "failure"
    assert all(item["sources"][key]["expected_conclusion"] == "success" for key in ("R790", "R775", "R786"))
    load_io(item)


def source_review(label, item, directory):
    """Check retained original bytes/schema only, without any field arithmetic."""
    source = item["sources"][label]
    directory = Path(directory)
    mp = directory/MANIFEST
    assert mp.stat().st_size == source["manifest_bytes"] and sha(mp) == source["manifest_sha256"]
    manifest = read(mp)
    assert manifest["result"] == source["result"]
    files = {row["file"]: plain(row) for row in manifest["files"]}
    assert len(files) == len(manifest["files"]) == source["manifest_file_count"]
    files[MANIFEST] = file_spec(mp)
    selected = {name: files[name] for name in selected_names(label)}
    for row in selected.values():
        bound(directory, row)
    assert fingerprint([selected[name] for name in sorted(selected)]) == source["selected_files_sha256"]
    run, core, public = (read(directory/name) for name in META[1:])
    assert run["result"] == core["result"] == public["result"] == source["result"]
    assert str(run["workflow_run_id"]) == str(source["run_id"])
    assert run["source_commit"] == public["source_commit"] == source["source_commit"]
    assert core["source_sha256"] == public["core_sha256"] == source["core_sha256"]
    assert public["driver_sha256"] == source["wrapper_sha256"]
    assert public["root_readme_sha256"] == source["original_readme_sha256"]["root"]
    assert public["topic_readme_sha256"] == source["original_readme_sha256"]["topic"]
    assert run.get("error") is None
    if run.get("core_receipt_sha256") is not None:
        assert run["core_receipt_sha256"] == selected["core-receipt.json"]["sha256"]
    if label == "R787":
        assert run["process_exit_code"] in source["accepted_checkpoint_exit_codes"]
        assert run["complete"] is False and core["complete"] is False
        assert core["error"].startswith("BudgetStop:")
        chart, selection, blocks = (read(directory/name) for name in (CHART, SELECTION, BLOCKS))
        tag = chart["configuration"]
        assert fingerprint(tag) == OLD_TAG_SHA
        for data in (chart, selection, blocks):
            assert data["complete"] is True and data["configuration"] == tag
        assert chart["actual_modular_rank"] == 1186 and chart["chosen_free_column"] == 1186
        assert len(chart["pivot_columns"]) == len(chart["pivot_rows"]) == 1186
        assert blocks["exact_E0_Z_zero_verified"] is True and blocks["A_inverse_over_Q_computed"] is False
        assert len(blocks["Z_pivot_integer_rows"]) == 20 and all(len(row) == 1214 for row in blocks["Z_pivot_integer_rows"])
        assert len(blocks["A_pivot_rows"]) == 1234 and len(blocks["A_remaining_rows"]) == 1326
        for flag in ("prime_proved", "all_14_L_branches_distinct", "all_kappa_reductions_invertible", "all_rational_denominators_units"):
            assert selection[flag] is True
        # The 73 MB completed current is SHA-verified here; only the Actions core
        # parses its large arrays and performs the normalized-coordinate audit.
        assert selected[CURRENT] == source["checkpoint"]
        assert selected[CURRENT]["sha256"] == "4997a05b79ab9e7c7f9286fc483b1f459ff6e23fa18df5344bd8ef0eb80f10f5"
    else:
        assert run["complete"] is True and run["process_exit_code"] == 0 and core["complete"] is True
        certificate = read(bound(directory, source["certificate"]))
        assert certificate["result"] == source["result"] and certificate["complete"] is True
        assert core["certificate_sha256"] == source["certificate"]["sha256"]
        tag = certificate["configuration"]
        if label == "R790":
            assert certificate["M2_dimension"] == 146 and certificate["cm_jet_order"] == 5
            assert certificate["original_psi_values_and_first_coarse_jets_verified"] is True
            assert certificate["original_M2_scale"] == "6724"
            assert certificate["R786_power5_product_scale"] == "13744803133596058624"
            assert certificate["distinct_retained_M2_seeds"] == 5 and certificate["actual_reflected_seed_pairs"] == 10
            assert plain(certificate["stage_manifest"]) == source["stage_manifest"]
            inventory = read(bound(directory, source["stage_manifest"]))
            assert inventory["complete"] is True and inventory["configuration"] == tag
            entries = {row["file"]: plain(row) for row in inventory["files"]}
            assert inventory["M2_output_rows"] == certificate["M2_output_rows"]
            assert len(certificate["M2_output_rows"]) == 146
            for index, row in enumerate(certificate["M2_output_rows"]):
                assert plain(row) == selected[row["file"]] == entries[row["file"]]
                data = read(directory/row["file"])
                assert data["complete"] is True and data["configuration"] == tag and data["index"] == index
                assert data["integer_scale"] == "6724" and data["original_c1"] == 4424
                assert data["R786_power1_scale_preserved"] is True
                for key in ("value_K_1_zeta", "derivative_z_K_1_zeta"):
                    assert len(data[key]) == 2 and all(len(pair) == 2 for pair in data[key])
        elif label == "R775":
            assert certificate["all_recipes_defined_over_original_K"] is True
            for name, dimension in zip(BASIS_NAMES, (146, 418, 690, 962, 1234)):
                data = read(directory/name)
                assert data["complete"] is True and data["configuration"] == tag
                assert data["rank"] == dimension and len(data["basis"]) == dimension
                assert data["characteristic_zero_independence_certified_by_unit_reduction"] is True
        else:
            assert certificate["exact_power5_basis_dimension"] == 1234
            assert certificate["basis_in_original_R775_saved_order"] is True
            assert plain(certificate["basis_index"]) == source["index"]
            index = read(bound(directory, source["index"]))
            assert index["complete"] is True and index["configuration"] == tag
            assert index["dimension"] == 1234 and index["bound_qY"] == 128
            assert index["integer_scale"] == "13744803133596058624"
    assert tag["source_sha256"] == source["core_sha256"] and fingerprint(tag) == source["configuration_sha256"]
    result = {key: source[key] for key in BASE_KEYS}
    result.update(configuration_sha256=source["configuration_sha256"],
                  selected_files_sha256=source["selected_files_sha256"], files=selected)
    if source.get("certificate"):
        result["certificate"] = source["certificate"]
    return result, tag


def review_all(item, retained):
    expanded, tags = {}, {}
    for label in SOURCES:
        expanded[label], tags[label] = source_review(label, item, retained/label)
    for label in ("R775",):
        inherited = tags["R790"]["retained_artifacts"][label]
        for key in BASE_KEYS:
            assert str(inherited[key]) == str(expanded[label][key])
    for key in BASE_KEYS:
        assert str(tags["R787"]["retained_artifacts"]["R786"][key]) == str(expanded["R786"][key])
    for name in BASIS_NAMES:
        assert tags["R786"]["R775_completed_prefix_producer"]["files"][name] == expanded["R775"]["files"][name]["sha256"]
    assert tags["R790"]["retained_artifacts"]["R775"]["files"][SOURCES["R775"]["certificate"]] == expanded["R775"]["certificate"]["sha256"]
    return expanded


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


def download_parent(label, item, directory, transfer):
    source = item["sources"][label]
    directory.mkdir(parents=True, exist_ok=True)
    archive = IO.Archive(source, transfer, whole=False)
    try:
        archive.extract_bound(MANIFEST, source["manifest_sha256"], directory/MANIFEST, source["manifest_bytes"])
        data = read(directory/MANIFEST)
        files = {row["file"]: plain(row) for row in data["files"]}
        names = [name for name in selected_names(label) if name != MANIFEST]
        archive.extract_many([(name, files[name]["sha256"], directory/name, files[name]["bytes"])
                              for name in names])
        if label == "R790":
            carrier = plain(source["R775_input_bundle"])
            assert carrier == files[R790_BUNDLE]
            archive.extract_bound(carrier["file"], carrier["sha256"], transfer/carrier["file"], carrier["bytes"])
        return archive.receipt()
    finally:
        archive.close()


def extract_R775(item, carrier, destination):
    assert file_spec(carrier) == item["sources"]["R790"]["R775_input_bundle"]
    wanted = set(selected_names("R775"))
    seen = set()
    with tarfile.open(carrier, "r:gz") as archive:
        for member in archive:
            assert member.isfile() and not Path(member.name).is_absolute() and ".." not in Path(member.name).parts
            parts = Path(member.name).parts
            if len(parts) != 2 or parts[0] != "R775" or parts[1] not in wanted:
                continue
            assert parts[1] not in seen
            target = destination/parts[1]
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.extractfile(member) as stream, target.open("wb") as output:
                shutil.copyfileobj(stream, output, 1024*1024)
            seen.add(parts[1])
    assert seen == wanted


def prepare_sources(item, out, allow_download=True):
    retained = out.parent/(out.name+"-retained")
    receipt_path = out/INPUT_RECEIPT
    transports = []
    if receipt_path.exists() and (out/BUNDLE).exists():
        old = read(receipt_path)
        assert old["result"] == RESULT and old["sources"] == item["sources"]
        assert file_spec(out/BUNDLE) == old["input_bundle"]
        if not allow_download or not all((retained/label/name).exists() for label in SOURCES for name in selected_names(label)):
            unpack_sources(out/BUNDLE, retained, old["expanded_sources"])
        expanded = review_all(item, retained)
        assert expanded == old["expanded_sources"]
        return retained, expanded
    assert allow_download
    transfer = out.parent/(out.name+"-source-transfers")
    for label in ("R787", "R790", "R786"):
        transports.append(download_parent(label, item, retained/label, transfer/label))
    extract_R775(item, transfer/"R790"/R790_BUNDLE, retained/"R775")
    expanded = review_all(item, retained)
    pack_sources(retained, expanded, out/BUNDLE)
    receipt = {"result": RESULT, "sources": item["sources"], "expanded_sources": expanded,
        "input_bundle": file_spec(out/BUNDLE), "selected_original_file_count": sum(len(v["files"]) for v in expanded.values()),
        "source_transport_receipts": transports, "all_selected_original_bytes_and_schema_verified": True,
        "old_mathematics_recomputed": False, "historical_readmes_compared_to_current_rules": False}
    save(receipt_path, receipt)
    print("INPUT_REVIEW="+json.dumps({"selected_original_file_count": receipt["selected_original_file_count"],
        "input_bundle": receipt["input_bundle"], "all_selected_original_bytes_and_schema_verified": True,
        "old_mathematics_recomputed": False}), flush=True)
    return retained, expanded


def expected_tag(item, expanded):
    return {"result": RESULT, "source_sha256": item["core_sha256"], "proof_sha256": item["proof_sha256"],
        "arithmetic": "exact Python Fraction and original rank14 monic integer ring", "p": 41,
        "auxiliary_prime": 1000000753, "source_Dixon_digits": 518, "canonical_free_column": 1186,
        "source_identities": {label: source_identity(source) for label, source in expanded.items()},
        "strategy": STRATEGY, "original_map_index": 4, "original_map_degree": "1206",
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
        manifest = read(root/MANIFEST)
        assert manifest["result"] == RESULT
        files = {row["file"]: plain(row) for row in manifest["files"]}
        for name in ("public-actions-input.json", "run-receipt.json", INPUT_RECEIPT):
            row = files[name]
            archive.extract_bound(name, row["sha256"], root/name, row["bytes"])
        old = read(root/"public-actions-input.json")
        run = read(root/"run-receipt.json")
        assert stable_job(old["job"]) == stable_job(item)
        assert old["source_commit"] == run["source_commit"] == source["source_commit"]
        assert str(run["workflow_run_id"]) == str(source["run_id"])
        assert old["core_sha256"] == source["core_sha256"]
        wanted = [name for name in files if name.startswith(PREFIX) and name.endswith(".json.gz")]
        wanted.extend((BUNDLE, INPUT_RECEIPT))
        if FINAL in files:
            wanted.append(FINAL)
        for name in wanted:
            row = files[name]
            archive.extract_bound(name, row["sha256"], out/name, row["bytes"])
        selected = read(out/INPUT_RECEIPT)
        tag = expected_tag(item, selected["expanded_sources"])
        for name in wanted:
            if name.startswith(PREFIX) and name.endswith(".json.gz"):
                stage = read(out/name)
                assert stage["complete"] is True and stage["configuration"] == tag
        if (out/FINAL).exists():
            final = read(out/FINAL)
            assert final["complete"] is True and final["configuration"] == tag
            inventory = read(bound(out, final["stage_manifest"]))
            assert inventory["configuration"] == tag
            for row in inventory["files"]:
                bound(out, row)
        save(out/"resume-source-receipt.json", {"result": RESULT, "source": source,
            "restored_complete_stage_count": len(wanted)-2-int(FINAL in wanted),
            "restored_source_carrier_and_receipt": True, "transport": archive.receipt(),
            "mathematical_stages_recomputed_by_restore": False})
    finally:
        archive.close()


def output_manifest(out):
    rows = [file_spec(path) for path in sorted(out.iterdir()) if path.is_file() and
            path.name not in (MANIFEST, REFERENCE) and not path.name.endswith(".tmp")]
    save(out/MANIFEST, {"result": RESULT, "files": rows,
        "temporary_active_checkpoint_retention_days": 1,
        "reproducible_tables_in_git_or_release": False})
    save(out/REFERENCE, {"result": RESULT, "manifest": file_spec(out/MANIFEST)})


def compute(item, out, request):
    out.mkdir(parents=True, exist_ok=True)
    restore(item, out)
    retained, expanded = prepare_sources(item, out)
    config = dict(item, retained_sources=expanded)
    config_path = out.parent/(out.name+"-expanded-config.json")
    save(config_path, config)
    input_record = {"result": RESULT, "source_commit": os.environ["GITHUB_SHA"],
        "source_repository": os.environ["GITHUB_REPOSITORY"], "job": item,
        "expanded_job_sha256": fingerprint(config), "expanded_sources": expanded,
        "core_sha256": item["core_sha256"], "wrapper_sha256": item["wrapper_sha256"],
        "proof_sha256": item["proof_sha256"], "request_sha256": sha(request),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()}
    save(out/"public-actions-input.json", input_record)
    command = [sys.executable, str(S/item["core"]), "--config", str(config_path),
        "--proof", str(topic_path(item["proof"])), "--retained", str(retained), "--output", str(out),
        "--budget-minutes", str(item["budget_minutes"])]
    error, returncode = None, 1
    with (out/"core.log").open("ab") as stream:
        process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT, start_new_session=True)
        try:
            returncode = process.wait(timeout=item["budget_minutes"]*60+900)
        except subprocess.TimeoutExpired:
            error, returncode = "outer_timeout", 124
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=15)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
    core_path = out/"core-receipt.json"
    core = read(core_path) if core_path.exists() else None
    complete = returncode == 0 and core is not None and core.get("complete") is True and (out/FINAL).exists()
    run = {"result": RESULT, "complete": complete, "process_exit_code": returncode, "error": error,
        "source_commit": os.environ["GITHUB_SHA"], "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ.get("GITHUB_RUN_ATTEMPT", "1"),
        "core_receipt_sha256": sha(core_path) if core is not None else None,
        "execution_environment": "public-repository-github-actions",
        "expanded_coordinates_exactly_certified": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()}
    save(out/"run-receipt.json", run)
    for path in out.glob("*.tmp"):
        path.unlink()
    output_manifest(out)
    print("RUN_RECEIPT="+json.dumps(run, sort_keys=True), flush=True)
    if not complete:
        raise SystemExit(returncode if returncode else 1)


def verify(item, out, request):
    manifest = read(out/MANIFEST)
    assert manifest["result"] == RESULT
    assert plain(read(out/REFERENCE)["manifest"]) == file_spec(out/MANIFEST)
    files = {row["file"]: plain(row) for row in manifest["files"]}
    assert len(files) == len(manifest["files"])
    assert set(files) == {path.name for path in out.iterdir() if path.is_file() and path.name not in (MANIFEST, REFERENCE)}
    for row in files.values():
        bound(out, row)
    retained, expanded = prepare_sources(item, out, allow_download=False)
    tag = expected_tag(item, expanded)
    public, run = read(out/"public-actions-input.json"), read(out/"run-receipt.json")
    assert public["job"] == item and public["request_sha256"] == sha(request)
    assert public["core_sha256"] == item["core_sha256"] and public["wrapper_sha256"] == item["wrapper_sha256"]
    assert public["source_commit"] == run["source_commit"]
    assert public["expanded_sources"] == expanded
    assert public["expanded_job_sha256"] == fingerprint(dict(item, retained_sources=expanded))
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
    stage_specs = {}
    for name, row in files.items():
        if not (name.startswith(PREFIX) and name.endswith(".json.gz")):
            continue
        stage = read(out/name)
        assert stage["complete"] is True and stage["configuration"] == tag
        if "expanded_coordinates_exactly_certified" in stage:
            assert stage["expanded_coordinates_exactly_certified"] is False
        stage_specs[name] = row
    if not run["complete"]:
        assert run["process_exit_code"] != 0
        if core is not None:
            assert core["complete"] is False
        print("PARTIAL_IO_REVIEW="+json.dumps({"complete": False, "manifest_entries": len(files),
            "complete_stages": len(stage_specs), "all_original_input_files_verified": 176,
            "expanded_coordinates_exactly_certified": False}), flush=True)
        raise SystemExit(1)
    assert run["process_exit_code"] == 0 and core["complete"] is True
    cert = read(out/FINAL)
    assert cert["complete"] is True and cert["configuration"] == tag and cert["result"] == RESULT
    assert core["certificate_sha256"] == files[FINAL]["sha256"]
    assert cert["source_Dixon_digits"] == 518 and cert["new_Dixon_digits_computed"] == 0
    assert cert["original_map_index"] == 4 and cert["original_map_degree"] == "1206"
    assert cert["exact_implicit_relation_defined"] is True
    for flag in ("expanded_coordinates_exactly_certified", "actual_beta_point_eta_or_height_computed", "old_R792_success_recipe_produced"):
        assert cert[flag] is False
    inventory = read(bound(out, cert["stage_manifest"]))
    assert inventory["complete"] is True and inventory["configuration"] == tag
    recorded = {row["file"]: plain(row) for row in inventory["files"]}
    assert len(recorded) == len(inventory["files"])
    assert recorded == {name: row for name, row in stage_specs.items() if not name.startswith(PREFIX+"stage-manifest-")}
    for key in ("source_audit", "power5_CM_values_and_jets", "exact_eZ", "A_response", "B_response", "denominator_unit_witness", "implicit_expression"):
        assert plain(cert[key]) == recorded[cert[key]["file"]]
        bound(out, cert[key])
    witness = read(out/cert["denominator_unit_witness"]["file"])
    assert len(witness["B0_values_at_original_14_branches"]) == len(witness["nonzero_flags"]) == 14
    assert witness["all_14_branches_units"] == cert["all_14_branches_units"]
    assert witness["characteristic_zero_B0_nonzero_certified"] == cert["characteristic_zero_B0_nonzero_certified"]
    assert cert["exact_finite_y_implicit_expression_defined"] == cert["characteristic_zero_B0_nonzero_certified"]
    assert witness["modular_zero_claimed_to_prove_characteristic_zero_zero"] is False
    assert witness["common_zero_or_point_at_infinity_claimed"] is False
    expression = read(out/cert["implicit_expression"]["file"])
    assert expression["unit_chart_solve"]["shape"] == [2420, 2420]
    assert expression["unit_chart_solve"]["free_column"] == 1186
    assert expression["unit_chart_solve"]["matrix_or_inverse_expanded"] is False
    assert expression["original_relation_exactly_defined_by_unit_chart"] is True
    assert expression["original_finite_CM_y_expression_defined"] == cert["characteristic_zero_B0_nonzero_certified"]
    assert expression["bordered_determinant_zero_or_exact_rowspace_acceptance_executed"] is False
    for key in ("A_response", "B_response"):
        response = read(out/cert[key]["file"])
        assert response["digits"] == 518
        for field in ("value", "derivative_z"):
            assert len(response[field]) == 14 and all(isinstance(x, str) and DECIMAL.fullmatch(x) for x in response[field])
        assert response["relation_denominator_or_content_not_reinserted"] is True
    if cert["modular_value_computed"]:
        assert cert["all_14_branches_units"] is True
        quotient = read(bound(out, cert["modular_value"]))
        assert quotient["only_modular_values_computed"] is True and quotient["all14_original_quotient_identities_verified"] is True
        assert len(quotient["value_y0"]) == len(quotient["derivative_z_y0"]) == 14
        inverse = read(bound(out, quotient["ring_inverse"]))
        assert inverse["digits"] == 518 and inverse["full14_product_equals_one"] is True
        candidate = read(bound(out, cert["coordinate_candidates"]))
        assert candidate["candidate_only"] is True and candidate["may_be_consumed_by_old_R792_success_path"] is False
        assert candidate["exact_bordered_determinant_or_rowspace_zero_certificate_obtained"] is False
        assert candidate["x_coordinate_or_beta_point_claimed"] is False
        for data in candidate["candidates"].values():
            assert len(data["coordinates"]) == 14
            assert all(row is None or len(row) == 2 for row in data["coordinates"])
    else:
        assert cert["all_14_branches_units"] is False and cert["modular_value"] is None and cert["coordinate_candidates"] is None
    print("COMPLETE_IO_REVIEW="+json.dumps({"result": RESULT, "complete": True,
        "manifest_entries": len(files), "complete_stage_count": len(recorded),
        "original_input_files": sum(len(source["files"]) for source in expanded.values()),
        "all_14_branches_units": cert["all_14_branches_units"],
        "characteristic_zero_B0_nonzero_certified": cert["characteristic_zero_B0_nonzero_certified"],
        "modular_value_computed": cert["modular_value_computed"],
        "expanded_coordinates_exactly_certified": False, "seconds": cert["seconds"],
        "certificate": files[FINAL], "stage_manifest": cert["stage_manifest"]}), flush=True)


def main():
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("compute", "verify"))
    parser.add_argument("--request", type=Path, default=REQUEST)
    parser.add_argument("--output", type=Path, default=TOPIC/"computations/R787-implicit-CM-value/output")
    args = parser.parse_args()
    request = read(args.request)
    item = request["job"]
    guard(item, args.request)
    if args.mode == "compute":
        compute(item, args.output, args.request)
    else:
        verify(item, args.output, args.request)


if __name__ == "__main__":
    main()
