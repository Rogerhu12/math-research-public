#!/usr/bin/env python3
"""R805 public source-bound runner for the pencil and graded free basis only."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import tarfile

from p41_public_actions_recovery import read, save, sha
from R786_public_exact_power5_short_basis import download, find_hash

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R805-public-original-affine-pencil-free-basis-request.json"
RESULT = "R805-original-affine-pencil-free-basis"
FINAL = "p41-original-affine-pencil-free-basis-certificate.json"
INPUT_BUNDLE = "R805-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
LABELS = {"R775", "R786", "R799"}
PRODUCER_META = ("full-outputs-manifest.json", "run-receipt.json",
                 "core-receipt.json", "public-actions-input.json")
META = {"public-actions-input.json", "retained-inputs-receipt.json",
        "resume-receipt.json", "run-receipt.json", "core-receipt.json"}
P6 = "R775-basis-power-6.json.gz"
INDEX799 = "R799-original-power7-basis-index.json.gz"
INDEX799_SHA = "b7889ae6e3ccf8607ce40215d68ca65f0075ac2f8638284690d8a4108e244847"
SELECT799 = "R799-power7-selection-progress.json.gz"
SELECT799_SHA = "3da403c7552b496e3b337f13f9bc7aa35b2d48cbeced025c675f24b226ee01d1"
DIMS = {1: 146, 2: 418, 3: 690}


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematical execution belongs to public repository Actions.")



def topic_path(relative):
    path = Path(relative)
    assert not path.is_absolute() and ".." not in path.parts
    return TOPIC/path



def plain_spec(row):
    return {key: row[key] for key in ("file", "bytes", "sha256")}



def file_spec(path):
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}



def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()



def same_producer(left, right):
    for key in ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256", "certificate_name"):
        assert str(left[key]) == str(right[key]), ("producer identity", key)
    name = left["certificate_name"]
    assert left["files"][name] == right["files"][name]
    for name in set(left["files"]) & set(right["files"]):
        assert left["files"][name] == right["files"][name], ("shared producer file", name)



def locate(directories, name, digest):
    assert Path(name).name == name
    for directory in directories:
        path = directory/name
        if path.is_file() and sha(path) == digest:
            return path
    for directory in directories:
        try:
            return find_hash(directory, name, digest)
        except ValueError:
            pass
    raise ValueError("Bound original file/SHA absent: "+name)



class Producer:
    """Pure IO: source receipts, full original manifest, and selected unchanged files."""
    def __init__(self, label, spec, directories):
        self.label, self.spec = label, spec
        self.directories = tuple(Path(path) for path in directories)
        mp = locate(self.directories, "full-outputs-manifest.json", spec["manifest_sha256"])
        manifest = read(mp)
        assert manifest["result"] == spec["result"]
        self.entries = {row["file"]: row for row in manifest["files"]}
        assert len(self.entries) == len(manifest["files"])
        self.paths = {"full-outputs-manifest.json": mp}
        self.selected = dict(self.paths)
        for name in PRODUCER_META[1:]:
            self.select(name)
        run, core, initial = (read(self.paths[name]) for name in PRODUCER_META[1:])
        assert run["result"] == spec["result"] and run["complete"] is True and run["process_exit_code"] == 0
        assert str(run["workflow_run_id"]) == str(spec["run_id"])
        assert run["source_commit"] == initial["source_commit"] == spec["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["result"] == core["result"] == spec["result"]
        assert core["complete"] is True and core["source_sha256"] == spec["core_sha256"]
        if label == "R794":
            assert initial["job"]["core_sha256"] == spec["core_sha256"]
            assert "core_receipt_sha256" not in run and "core_sha256" not in initial
        else:
            assert run["core_receipt_sha256"] == sha(self.paths["core-receipt.json"])
            assert initial["core_sha256"] == spec["core_sha256"]
            if label == "R759":
                assert "job" not in initial
            else:
                assert initial["job"]["core_sha256"] == spec["core_sha256"]
        self.initial = initial
        name = spec["certificate_name"]
        assert self.entries[name]["sha256"] == core["certificate_sha256"] == spec["files"][name]
        self.certificate = read(self.select(name))
        assert self.certificate["complete"] is True and self.certificate["result"] == spec["result"]
        self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == spec["core_sha256"] and self.tag["python_flint"] == "0.9.0"

    def bound(self, name, expected=None):
        assert Path(name).name == name
        row = self.entries[name]
        if expected is not None:
            assert plain_spec(row) == plain_spec(expected)
        if name in self.spec["files"]:
            assert row["sha256"] == self.spec["files"][name]
        if name not in self.paths:
            path = locate(self.directories, name, row["sha256"])
            assert path.stat().st_size == row["bytes"]
            self.paths[name] = path
        return self.paths[name]

    def select(self, name, expected=None):
        path = self.bound(name, expected)
        self.selected[name] = path
        return path

    def stage(self, row):
        path = self.select(row["file"], row)
        data = read(path)
        assert data["complete"] is True and data["configuration"] == self.tag
        return data

    def cert_stage(self, name, digest=None):
        stages = {row["file"]: row for row in self.certificate["stages"]}
        assert len(stages) == len(self.certificate["stages"])
        if digest is not None:
            assert stages[name]["sha256"] == digest
        return self.stage(stages[name])

    def inventory(self, key):
        value = self.stage(self.certificate[key])
        files = {row["file"]: plain_spec(row) for row in value["files"]}
        assert len(files) == len(value["files"])
        return files



def transfer(paths, target):
    target.mkdir(parents=True, exist_ok=True)
    for name, path in paths.items():
        assert Path(name).name == name
        destination = target/name
        if path.resolve() == destination.resolve():
            continue
        if destination.exists():
            assert destination.stat().st_size == path.stat().st_size and sha(destination) == sha(path)
        else:
            shutil.copyfile(path, destination)



def output_manifest(out):
    artifact = "serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    rows = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name in ("full-outputs-manifest.json", REFERENCE):
            continue
        rows.append({"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path), "artifact": artifact,
                     "included_in_git": False,
                     "eligible_for_reviewed_small_metadata": path.name in META and path.stat().st_size < 100_000})
    mp = out/"full-outputs-manifest.json"
    save(mp, {"result": RESULT, "files": rows, "temporary_active_checkpoint_artifact": artifact,
        "temporary_active_checkpoint_retention_days": 1,
        "reproducible_rows_certificates_or_input_bundles_in_git_or_release": False})
    save(out/REFERENCE, {"result": RESULT, "manifest_file": mp.name, "manifest_sha256": sha(mp),
        "manifest_bytes": mp.stat().st_size, "file_count": len(rows), "full_outputs_artifact": artifact,
        "manifest_in_git": False, "automatic_git_or_release_publication": False})


def matching_configuration(tag, item):
    assert tag["result"] == RESULT and tag["source_sha256"] == item["core_sha256"]
    assert tag["python_flint"] == "0.9.0" and tag["p"] == 41
    for key in ("R805_proof_sha256", "R805_method_sha256", "retained_artifacts",
                "qY_count", "auxiliary_prime_start"):
        assert tag[key] == item[key]
    assert tag["qY_count"] == 41 and tag["auxiliary_prime_start"] == 739
    assert tag["source_powers"] == [1, 2, 3]
    assert tag["source_dimensions"] == {str(r): DIMS[r] for r in DIMS}
    assert tag["basis_scales"] == {str(r): str(82**(2*r)) for r in DIMS}
    assert tag["tau_original_index"] == 0 and tag["sigma_formula"] == "e1+n*e73"
    assert tag["graded_free_basis_degree_distribution"] == [1, 144, 127]
    assert tag["old_saved_products_recomputed"] is False


def allowed_group_name(label, spec, name):
    if name in set(PRODUCER_META)|set(spec["files"]):
        return True
    if label == "R786":
        match = re.fullmatch(r"R786-exact-power-([123])-row-(\d{4})\.json\.gz", name)
        return bool(match and 0 <= int(match[2]) < DIMS[int(match[1])])
    return False


def extract_bundle(bundle, target, specs):
    target.mkdir(parents=True, exist_ok=True)
    seen, count = set(), 0
    with tarfile.open(bundle, "r:gz") as archive:
        for member in archive:
            relative = Path(member.name)
            assert member.isfile() and not relative.is_absolute() and ".." not in relative.parts
            assert len(relative.parts) == 2
            group, name = relative.parts
            assert group in LABELS and str(relative) not in seen
            seen.add(str(relative))
            assert allowed_group_name(group, specs[group], name), (group, name)
            destination = target/relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            temporary = destination.with_name(destination.name+".tmp")
            with archive.extractfile(member) as source, temporary.open("wb") as output:
                shutil.copyfileobj(source, output)
            if destination.exists():
                assert destination.stat().st_size == member.size and sha(destination) == sha(temporary)
                temporary.unlink()
            else:
                temporary.replace(destination)
            count += 1
    assert count
    return count


def select_original_inputs(producers):
    """Only source hashes and schemas; no field, product or rank arithmetic."""
    p775, p786, p799 = (producers[label] for label in ("R775", "R786", "R799"))
    power6 = p775.cert_stage(P6)
    assert power6["rank"] == len(power6["basis"]) == 1506
    assert power6["characteristic_zero_independence_certified_by_unit_reduction"] is True
    anchors = set()
    for row in power6["basis"]:
        recipe = row["recipe"]
        assert recipe["kind"] == "product" and recipe["left_power"] == 1 and recipe["right_power"] == 5
        anchors.add(recipe["left_index"])
    assert anchors == {0, 1, 73}
    assert p799.tag["retained_artifacts"]["R775"]["files"][P6] == p775.entries[P6]["sha256"]
    assert p799.certificate["three_original_anchor_basepoint_free_input_verified"] is True
    entry = p799.certificate["basis_indices"]["7"]
    assert entry["file"] == INDEX799 and entry["sha256"] == INDEX799_SHA
    old = p799.stage(entry)
    assert p799.entries[SELECT799]["sha256"] == SELECT799_SHA
    assert old["dimension"] == 1778 and old["ordinary_power"] == 7
    assert old["anchor_indices"] == [0, 1, 73]
    assert old["two_anchor_basepoint_free_certified_by_actual_minor"] is False
    assert old["actual_nonzero_minor"]["prime"] == 739
    assert old["actual_nonzero_minor"]["determinant_mod_prime"] == 534
    assert old["candidate_cursor"] == 4518
    rows = old["basis_rows"]
    assert len(rows) == 1778
    assert rows[1757]["index"] == 1757 and rows[1757]["recipe"]["left_index"] == 1
    assert rows[1758]["index"] == 1758 and rows[1758]["recipe"]["left_index"] == 73
    assert all(row["recipe"]["left_index"] in (0, 1) for row in rows[:1758])
    assert p786.certificate["exact_K_basis_prefix_bound_qY"] == 128
    assert p786.certificate["basis_in_original_R775_saved_order"] is True
    inventory = p786.inventory("stages_manifest")
    for power in (1, 2, 3):
        for index in range(DIMS[power]):
            name = "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"
            data = p786.stage(inventory[name])
            assert data["weight"] == 2*power and data["bound_qY"] == 128
            assert data["integer_scale"] == str(82**(2*power))
            assert data["original_R775_finite_coefficients_verified"] is True
            assert len(data["integer_qY_xi_coefficients"]) == 129
            assert all(len(row) == 40 for row in data["integer_qY_xi_coefficients"])
            if power == 1:
                assert data["recipe"]["kind"] == "det_semilinear_E1_pair_trace"
            else:
                recipe = data["recipe"]
                assert recipe["kind"] == "product"
                lp, rp = recipe["left_power"], recipe["right_power"]
                assert lp < power and rp < power and lp+rp == power
                assert 0 <= recipe["left_index"] < DIMS[lp]
                assert 0 <= recipe["right_index"] < DIMS[rp]
    for producer in producers.values():
        assert all(name in producer.selected for name in producer.spec["files"]), (producer.label, "unused pinned input")
    return {"old_power1_rows": 146, "old_power2_rows": 418, "old_power3_alias_rows": 690,
        "old_coefficients_consumed_count_qY": 41,
        "old_two_anchor_prime": 739, "old_two_anchor_rank_from_saved_order": 1758,
        "old_large_R799_echelon_matrix_transferred": False,
        "old_or_new_mathematical_arithmetic_executed_during_input_selection": False,
        "all_sizes_sha256_and_original_schemas_verified": True}


def prepare_inputs(item, out):
    specs = item["retained_artifacts"]
    assert set(specs) == LABELS
    inputs = out.parent/"retained"
    present = [(inputs/label/"full-outputs-manifest.json").exists() for label in LABELS]
    transferred = all(present)
    assert transferred or not any(present), "Partial unverified R805 input carrier"
    if transferred:
        producers = {label: Producer(label, specs[label], [inputs/label]) for label in sorted(LABELS)}
    else:
        producers = {}
        for label in sorted(LABELS):
            directory = out.parent/("downloaded-"+label)
            download(specs[label], directory, require_complete=True)
            producers[label] = Producer(label, specs[label], [directory])
    selection = select_original_inputs(producers)
    groups = []
    for label in sorted(LABELS):
        producer = producers[label]
        transfer(producer.selected, inputs/label)
        actual = {path.name for path in (inputs/label).iterdir() if path.is_file()}
        assert actual == set(producer.selected), (label, "unexpected retained input")
        groups.append({"label": label, "producer": specs[label], "file_count": len(actual),
                       "original_manifest_and_selected_file_hashes_verified": True})
    if not (out/INPUT_BUNDLE).exists():
        with tarfile.open(out/INPUT_BUNDLE, "w:gz") as archive:
            for path in sorted(inputs.rglob("*")):
                if path.is_file():
                    archive.add(path, arcname=path.relative_to(inputs).as_posix(), recursive=False)
    save(out/"retained-inputs-receipt.json", {
        "result": RESULT, "groups": groups, "selection": selection,
        "all_inputs_from_same_core_active_R805_bundle": transferred,
        "fresh_original_producers_downloaded": [] if transferred else sorted(LABELS),
        "input_bundle": file_spec(out/INPUT_BUNDLE),
        "unused_R799_rows_or_large_echelon_state_in_active_bundle": False,
        "old_arithmetic_recomputed": False})
    return inputs


def restore_resume(item, out):
    previous = item.get("resume")
    if previous is None:
        return
    directory = out.parent/"downloaded-R805-continuation"
    download(previous, directory, require_complete=False)
    manifest = read(find_hash(directory, "full-outputs-manifest.json", previous["manifest_sha256"]))
    assert manifest["result"] == RESULT
    entries = {row["file"]: row for row in manifest["files"]}
    assert len(entries) == len(manifest["files"])

    def bound(name):
        row = entries[name]
        path = find_hash(directory, name, row["sha256"])
        assert path.stat().st_size == row["bytes"]
        return path

    initial, run = read(bound("public-actions-input.json")), read(bound("run-receipt.json"))
    assert initial["source_commit"] == run["source_commit"] == previous["source_commit"]
    assert str(run["workflow_run_id"]) == str(previous["run_id"])
    for key in ("result", "p", "core_sha256", "R805_proof_sha256", "R805_method_sha256",
                "retained_artifacts", "qY_count", "auxiliary_prime_start", "requested_stage"):
        assert initial["job"][key] == item[key], "Changed continuation identity: "+key
    bundle = bound(INPUT_BUNDLE)
    extract_bundle(bundle, out.parent/"retained", item["retained_artifacts"])
    shutil.copyfile(bundle, out/INPUT_BUNDLE)
    count = 0
    for name in entries:
        if not (name.startswith("R805-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        source = bound(name)
        data = read(source)
        assert data["complete"] is True
        matching_configuration(data["configuration"], item)
        shutil.copyfile(source, out/name)
        count += 1
    save(out/"resume-receipt.json", {"result": RESULT, "producer": previous,
        "same_exact_core_sha256": item["core_sha256"], "complete_checkpoint_files_copied": count,
        "original_three_group_input_bundle_restored": True,
        "completed_new_products_ranks_and_S_basis_rows_preserved": True,
        "completed_mathematical_stages_recomputed": False})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core, proof, method = S/item["core"], topic_path(item["proof"]), topic_path(item["method"])
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {"result": RESULT, "p": 41,
        "source_repository": "Rogerhu12/math-research-public", "source_commit": source,
        "job": item, "core_sha256": sha(core), "proof_sha256": sha(proof), "method_sha256": sha(method),
        "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "workflow_sha256": sha(REPO/item["workflow"]),
        "download_helper_sha256": sha(S/"R786_public_exact_power5_short_basis.py"),
        "io_helper_sha256": sha(S/"p41_public_actions_recovery.py"),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "new_arithmetic": "only missing original monomials, actual pencil and graded free basis q0..40",
        "old_saved_products_recomputed": False,
        "primitive_M6_clearing_functions_polar_divisors_eta_or_height_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41 and item["producer_inputs_pending"] is False
        assert sha(core) == item["core_sha256"] and sha(__file__) == item["wrapper_sha256"]
        assert sha(proof) == item["R805_proof_sha256"] and sha(method) == item["R805_method_sha256"]
        assert sha(S/"R786_public_exact_power5_short_basis.py") == item["download_helper_sha256"]
        assert sha(S/"p41_public_actions_recovery.py") == item["io_helper_sha256"]
        assert item["qY_count"] == 41 and item["auxiliary_prime_start"] == 739
        assert item["requested_stage"] == "pencil_and_graded_free_basis"
        restore_resume(item, out)
        retained = prepare_inputs(item, out)
        config = out.parent/"job-config.json"
        save(config, item)
        command = [sys.executable, "-u", str(core), "--config", str(config), "--proof", str(proof),
            "--method", str(method), "--retained", str(retained), "--output", str(out),
            "--budget-minutes", str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60+120)
            except subprocess.TimeoutExpired:
                error = "Budget reached; completed source-bound products, actual ranks and basis rows retained."
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                code = 124
    except Exception as exception:
        error = type(exception).__name__+": "+str(exception)
    path = out/"core-receipt.json"
    receipt = read(path) if path.exists() else {"complete": False}
    complete = code == 0 and receipt.get("complete") is True
    save(out/"run-receipt.json", {"result": RESULT, "p": 41, "complete": complete,
        "process_exit_code": code, "error": error, "source_commit": source,
        "workflow_run_id": os.environ["GITHUB_RUN_ID"], "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "execution_environment": "public-repository-github-actions",
        "core_receipt_sha256": sha(path) if path.exists() else None,
        "actual_pencil_and_graded_free_basis_computed": complete,
        "old_saved_products_recomputed": False,
        "primitive_M6_clearing_functions_polar_divisors_eta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete, "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    run, receipt = read(out/"run-receipt.json"), read(out/"core-receipt.json")
    assert run["result"] == RESULT and run["complete"] is True and run["process_exit_code"] == 0
    assert run["core_receipt_sha256"] == sha(out/"core-receipt.json")
    assert receipt["result"] == RESULT and receipt["complete"] is True
    assert receipt["source_sha256"] == item["core_sha256"] and receipt["certificate_sha256"] == sha(out/FINAL)
    cert = read(out/FINAL)
    assert cert["result"] == RESULT and cert["complete"] is True and cert["p"] == 41
    matching_configuration(cert["configuration"], item)
    assert cert["completed_scope"] == "pencil_and_graded_free_basis"
    assert cert["affine_free_module_rank"] == 272 and cert["graded_free_basis_degrees"] == [1, 144, 127]
    assert cert["degree3_S_basis_dimension"] == 690 and cert["degree3_S_prefix_count"] == 41
    assert cert["degree3_S_full_real_coordinates"] == 820
    assert cert["all_S_rows_original_and_real_coordinates_verified"] is True
    assert cert["original_82_scales_preserved"] is True
    for key in ("old_saved_V1_V2_V3_products_recomputed", "old_two_anchor_V7_mod739_rank_recomputed",
                "primitive_multiplication_computed", "field_coordinate_transport_computed",
                "M6_clearing_computed", "function_DAG_computed",
                "polar_ideals_or_KM_representatives_computed", "actual_eta_rigidification_or_height_computed"):
        assert cert[key] is False

    def stage(spec):
        assert Path(spec["file"]).name == spec["file"]
        path = out/spec["file"]
        assert file_spec(path) == plain_spec(spec)
        data = read(path)
        assert data["complete"] is True
        matching_configuration(data["configuration"], item)
        return data

    inventory = stage(cert["stage_manifest"])
    entries = {row["file"]: plain_spec(row) for row in inventory["files"]}
    assert len(entries) == len(inventory["files"])
    headers = {}
    for name, spec in entries.items():
        assert name.startswith("R805-") and name.endswith(".json.gz")
        headers[name] = stage(spec)
    for key in ("alias_index", "pencil_stage", "graded_free_basis_stage", "S_basis_index"):
        assert plain_spec(cert[key]) == entries[cert[key]["file"]]
    producers = {label: Producer(label, item["retained_artifacts"][label], [out.parent/"retained"/label])
                 for label in sorted(LABELS)}

    def source(spec):
        label = spec["producer"]
        if label == "R805":
            assert plain_spec(spec) == entries[spec["file"]]
        else:
            producers[label].bound(spec["file"], spec)

    aliases = headers[cert["alias_index"]["file"]]
    assert aliases["source_powers"] == [1, 2, 3] and len(aliases["rows"]) == 1254
    assert aliases["three_anchor_basepoint_free_input_verified"] is True
    assert aliases["old_basis_or_rank_arithmetic_recomputed"] is False
    source(aliases["three_anchor_power6_source"])
    old_record = aliases["old_two_anchor_record"]
    assert old_record["prime"] == 739 and old_record["actual_two_anchor_rank_from_saved_selection"] == 1758
    assert old_record["selection_stage_sha256"] == SELECT799_SHA
    assert old_record["characteristic_zero_two_anchor_failure_claimed"] is False
    source(old_record["source"])
    for row in aliases["rows"]:
        assert row["power"] in DIMS and 0 <= row["index"] < DIMS[row["power"]]
        assert len(row["sorted_M2_leaf_indices"]) == row["power"]
        assert row["sorted_M2_leaf_indices"] == sorted(row["sorted_M2_leaf_indices"])
        source(row["source"])
    pencil = headers[cert["pencil_stage"]["file"]]
    assert pencil["actual_rank"] == cert["actual_pencil_rank"] == 690
    assert pencil["n"] == cert["actual_pencil_n"] and 0 <= pencil["n"] <= 272
    assert pencil["prime"] == cert["actual_pencil_prime"]
    assert pencil["actual_determinant_mod_prime"] == cert["actual_pencil_minor"]
    assert pencil["actual_determinant_mod_prime"] % pencil["prime"]
    assert pencil["basepoint_free_certified_by_actual_unit_minor"] is True
    assert pencil["original_alias_index_sha256"] == cert["alias_index"]["sha256"]
    assert pencil["full_row_count"] == 820 and pencil["full_column_count"] == 836
    for key, bound in (("row_indices", 820), ("column_indices", 836)):
        assert len(pencil[key]) == 690 and pencil[key] == sorted(set(pencil[key]))
        assert all(0 <= i < bound for i in pencil[key])
    free = headers[cert["graded_free_basis_stage"]["file"]]
    assert free["pencil_stage"] == cert["pencil_stage"]
    assert free["degree_distribution"] == [1, 144, 127] and free["affine_free_module_rank"] == 272
    assert free["degree1_original_indices"] == list(range(2, 146))
    assert free["degree1_change_of_basis_determinant"] == 1
    assert len(free["degree2_original_indices"]) == 127
    assert free["degree2_original_indices"] == sorted(set(free["degree2_original_indices"]))
    assert all(0 <= i < 418 for i in free["degree2_original_indices"])
    assert free["actual_pencil_degree2_subspace_rank"] == 291 and free["actual_degree2_rank"] == 418
    assert free["actual_determinant_mod_prime"] % free["prime"]
    assert free["integer_scale"] == str(82**4)
    for spec in free["degree2_original_sources"]:
        source(spec)
    index = headers[cert["S_basis_index"]["file"]]
    assert index["dimension"] == 690 and index["qY_count"] == 41 and index["full_coordinate_rows"] == 820
    assert index["integer_scale"] == str(82**6) and len(index["basis_rows"]) == 690
    assert index["original_pencil_stage"] == cert["pencil_stage"]
    assert index["graded_free_basis_stage"] == cert["graded_free_basis_stage"]
    assert index["not_old_R786_V3_coefficient_basis"] is True
    assert index["all_original_and_real_coordinates_verified"] is True
    for i, spec in enumerate(index["basis_rows"]):
        assert spec["index"] == i and plain_spec(spec) == entries[spec["file"]]
        row = headers[spec["file"]]
        assert row["index"] == i and row["recipe"] == spec["recipe"]
        assert row["integer_scale"] == str(82**6) and row["qY_count"] == 41
        assert row["all_original_and_real_coordinates_verified"] is True
        assert row["V3_membership_has_original_product_generation_witness"] is True
        assert row["old_saved_products_recomputed"] is False
        assert row["free_basis_stage"] == cert["graded_free_basis_stage"]
        assert len(row["integer_qY_xi_coefficients"]) == 41
        assert all(len(values) == 40 for values in row["integer_qY_xi_coefficients"])
        assert len(row["integer_v_t_coefficients"]) == 41
        assert all(len(values) == 20 for values in row["integer_v_t_coefficients"])
        for term in row["monomial_sources"]:
            source(term["source"])
    minor_spec = index["short_minor"]
    assert plain_spec(minor_spec) == entries[minor_spec["file"]]
    minor = headers[minor_spec["file"]]
    assert minor["actual_rank"] == 690 and minor["full_coordinate_rows"] == 820
    assert minor["full_columns"] == 690 and minor["all_source_rows"] == index["basis_rows"]
    assert minor["column_indices"] == list(range(690))
    assert len(minor["row_indices"]) == 690 and minor["row_indices"] == sorted(set(minor["row_indices"]))
    assert all(0 <= i < 820 for i in minor["row_indices"])
    assert minor["actual_determinant_mod_prime"] % minor["prime"]
    assert cert["degree3_S_actual_minor"] == {"prime": minor["prime"], "rank": 690,
                                            "determinant": minor["actual_determinant_mod_prime"]}
    for name, data in headers.items():
        if name.startswith("R805-new-monomial-"):
            assert data["qY_count"] == 41 and data["old_recipe_alias_exists"] is False
            assert data["old_saved_product_recomputed"] is False
            assert data["all_original_and_real_coordinates_verified"] is True
            for spec in data["factor_sources"]:
                source(spec)
    bundle = read(out/"retained-inputs-receipt.json")["input_bundle"]
    assert bundle["file"] == INPUT_BUNDLE and file_spec(out/INPUT_BUNDLE) == bundle
    return 0


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["compute", "verify"])
    mode = parser.parse_args().mode
    out = Path(os.environ["RUNNER_TEMP"])/"serre-global"/RESULT/"output"
    if mode == "compute":
        request = read(REQUEST)
        assert request["session"] == "serre-public-astra-20261115"
        return compute(request["job"], out)
    item = read(out/"public-actions-input.json")["job"]
    return verify(item, out)


if __name__ == "__main__":
    sys.exit(main())

