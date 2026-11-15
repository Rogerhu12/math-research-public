#!/usr/bin/env python3
"""R806 source-bound public runner for one original primitive multiplier."""
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
REQUEST = TOPIC/"notes/R806-public-original-primitive-multiplication-request.json"
RESULT = "R806-original-primitive-multiplication"
FINAL = "p41-original-primitive-multiplication-certificate.json"
INPUT_BUNDLE = "R806-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
LABELS = {"R805", "R786"}
PRODUCER_META = ("full-outputs-manifest.json", "run-receipt.json",
                 "core-receipt.json", "public-actions-input.json")
META = {"public-actions-input.json", "retained-inputs-receipt.json",
        "resume-receipt.json", "run-receipt.json", "core-receipt.json"}
R805_CORE_SHA = "730a7d8f51d76d1153386c63f2e082285ada4573a2baf8d87d1825d3ce75b420"
R805_INPUT_BUNDLE = "R805-retained-producer-inputs.tar.gz"
DIMS = {1: 146, 2: 418, 3: 690}
DIM, ROWS, FREE = 690, 820, 272
EPS = [0]+[1]*144+[2]*127


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
        assert run["core_receipt_sha256"] == sha(self.paths["core-receipt.json"])
        assert initial["core_sha256"] == spec["core_sha256"]
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
    for key in ("R805_proof_sha256", "R806_method_sha256", "retained_artifacts",
                "qY_count", "auxiliary_prime_start", "dixon_group_columns", "reconstruct_every_digits"):
        assert tag[key] == item[key]
    assert tag["qY_count"] == 41 and tag["full_coordinate_rows"] == ROWS
    assert tag["S_basis_dimension"] == DIM and tag["normal_affine_basis_rank"] == FREE
    assert tag["normal_affine_basis_degrees"] == EPS
    assert tag["basis_integer_scale"] == str(82**6)
    assert tag["original_tau_index"] == 0
    assert tag["auxiliary_prime_start"] == 1000000007
    assert tag["dixon_group_columns"] == tag["reconstruct_every_digits"] == 8
    assert tag["family_parameter_bound"] == 143*(272*271//2)
    assert tag["cyclic_determinant_degree_bound"] == 36458
    assert tag["candidate_order"] == "e2; each e_j,e2+e_j for j=3..145; then sum(a^(i-1)*b_i),a=1..D"
    assert tag["search_order"] == "diagonals candidate_index+prime_index+integer_z0; distinct residues only"
    assert tag["matrix_convention"] == "column input E_a, row output E_b; M_ba(z)"
    assert tag["old_R805_ranks_selection_or_saved_products_recomputed"] is False
    assert tag["characteristic_zero_Krylov_matrix_or_inverse_computed"] is False


def allowed_group_name(label, spec, name):
    if name in set(PRODUCER_META)|set(spec["files"]):
        return True
    if label == "R786":
        match = re.fullmatch(r"R786-exact-power-([123])-row-(\d{4})\.json\.gz", name)
        return bool(match and 0 <= int(match[2]) < DIMS[int(match[1])])
    if label == "R805":
        return name.startswith("R805-") and name.endswith(".json.gz")
    return False


def extract_bundle(bundle, target, specs, original_R805=False):
    target.mkdir(parents=True, exist_ok=True)
    seen, count = set(), 0
    with tarfile.open(bundle, "r:gz") as archive:
        for member in archive:
            relative = Path(member.name)
            assert member.isfile() and not relative.is_absolute() and ".." not in relative.parts
            assert len(relative.parts) == 2 and str(relative) not in seen
            seen.add(str(relative))
            group, name = relative.parts
            if original_R805:
                assert group in {"R775", "R786", "R799"}
                if group != "R786":
                    continue
            else:
                assert group in LABELS
            assert group in specs and allowed_group_name(group, specs[group], name), (group, name)
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


def select_original_inputs(producers, item):
    """Only hashes, source identity, shapes and saved flags. No new arithmetic."""
    p805, p786 = producers["R805"], producers["R786"]
    assert p805.spec["core_sha256"] == R805_CORE_SHA
    same_producer(p805.tag["retained_artifacts"]["R786"], p786.spec)
    same_producer(p805.initial["job"]["retained_artifacts"]["R786"], p786.spec)
    assert p805.tag["R805_proof_sha256"] == item["R805_proof_sha256"]
    cert = p805.certificate
    assert cert["completed_scope"] == "pencil_and_graded_free_basis"
    assert cert["affine_free_module_rank"] == FREE and cert["graded_free_basis_degrees"] == [1, 144, 127]
    assert cert["degree3_S_basis_dimension"] == DIM and cert["degree3_S_prefix_count"] == 41
    assert cert["degree3_S_full_real_coordinates"] == ROWS
    assert cert["all_S_rows_original_and_real_coordinates_verified"] is True
    assert cert["original_82_scales_preserved"] is True
    inventory805 = p805.inventory("stage_manifest")
    def stage805(spec):
        assert plain_spec(spec) == inventory805[spec["file"]]
        return p805.stage(spec)
    pencil = stage805(cert["pencil_stage"])
    free = stage805(cert["graded_free_basis_stage"])
    index = stage805(cert["S_basis_index"])
    aliases = stage805(cert["alias_index"])
    minor = stage805(index["short_minor"])
    assert pencil["actual_rank"] == 690 and pencil["basepoint_free_certified_by_actual_unit_minor"] is True
    assert pencil["n"] == cert["actual_pencil_n"]
    assert free["degree_distribution"] == [1, 144, 127]
    assert free["degree1_original_indices"] == list(range(2, 146))
    assert len(free["degree2_original_indices"]) == 127
    assert free["pencil_stage"] == cert["pencil_stage"]
    assert minor["actual_rank"] == 690 and minor["full_coordinate_rows"] == ROWS
    assert minor["actual_determinant_mod_prime"] % minor["prime"]
    assert len(minor["row_indices"]) == 690 and minor["row_indices"] == sorted(set(minor["row_indices"]))
    assert all(0 <= i < ROWS for i in minor["row_indices"])
    assert minor["column_indices"] == list(range(DIM))
    assert minor["all_source_rows"] == index["basis_rows"]
    assert index["dimension"] == len(index["basis_rows"]) == 690
    assert index["integer_scale"] == str(82**6)
    assert index["all_original_and_real_coordinates_verified"] is True
    assert index["not_old_R786_V3_coefficient_basis"] is True
    for i, spec in enumerate(index["basis_rows"]):
        assert spec["index"] == i
        row = stage805(spec)
        assert row["index"] == i and row["recipe"] == spec["recipe"]
        assert row["integer_scale"] == str(82**6) and row["qY_count"] == 41
        assert row["free_basis_stage"] == cert["graded_free_basis_stage"]
        assert row["all_original_and_real_coordinates_verified"] is True
        assert row["V3_membership_has_original_product_generation_witness"] is True
        assert len(row["integer_v_t_coefficients"]) == 41
        assert all(len(line) == 20 for line in row["integer_v_t_coefficients"])
        assert len(row["integer_qY_xi_coefficients"]) == 41
        assert all(len(line) == 40 for line in row["integer_qY_xi_coefficients"])
    old_monomials = []
    for name, spec in inventory805.items():
        if name.startswith("R805-new-monomial-") and name.endswith(".json.gz"):
            row = stage805(spec)
            leaves = row["sorted_M2_leaf_indices"]
            assert leaves == sorted(leaves) and len(leaves) in (2, 3)
            assert row["qY_count"] == 41 and row["integer_scale"] == str(82**(2*len(leaves)))
            assert row["all_original_and_real_coordinates_verified"] is True
            assert row["old_recipe_alias_exists"] is False and row["old_saved_product_recomputed"] is False
            assert len(row["integer_v_t_coefficients"]) == len(row["integer_qY_xi_coefficients"]) == 41
            old_monomials.append(name)
    assert aliases["source_powers"] == [1, 2, 3] and len(aliases["rows"]) == 1254
    old_aliases = {(row["power"], row["index"]): row for row in aliases["rows"]}
    assert len(old_aliases) == 1254
    assert p786.certificate["exact_K_basis_prefix_bound_qY"] == 128
    assert p786.certificate["basis_in_original_R775_saved_order"] is True
    inventory786 = p786.inventory("stages_manifest")
    for power in (1, 2, 3):
        for i in range(DIMS[power]):
            name = "R786-exact-power-"+str(power)+"-row-"+str(i).zfill(4)+".json.gz"
            row = p786.stage(inventory786[name])
            alias = old_aliases[power, i]
            assert alias["source"] == dict(plain_spec(p786.entries[name]), producer="R786")
            assert alias["recipe"] == row["recipe"]
            assert len(alias["sorted_M2_leaf_indices"]) == power
            assert row["weight"] == 2*power and row["bound_qY"] == 128
            assert row["integer_scale"] == str(82**(2*power))
            assert row["original_R775_finite_coefficients_verified"] is True
            assert len(row["integer_qY_xi_coefficients"]) == 129
            assert all(len(line) == 40 for line in row["integer_qY_xi_coefficients"])
    for producer in producers.values():
        assert all(name in producer.selected for name in producer.spec["files"]), (producer.label, "unused pinned input")
    return {"old_R805_S_basis_rows": 690, "old_R805_complete_monomial_stages": len(old_monomials),
        "old_R786_power1_rows": 146, "old_R786_power2_rows": 418, "old_R786_power3_alias_rows": 690,
        "qY_prefix_count_consumed": 41,
        "old_large_inverse_or_rank_recomputed": False,
        "old_or_new_mathematical_arithmetic_executed_during_input_selection": False,
        "all_sizes_sha256_and_original_schemas_verified": True}


def prepare_inputs(item, out):
    specs = item["retained_artifacts"]
    assert set(specs) == LABELS
    inputs = out.parent/"retained"
    present = [(inputs/label/"full-outputs-manifest.json").exists() for label in LABELS]
    transferred = all(present)
    assert transferred or not any(present), "Partial unverified R806 input carrier"
    old_carrier = None
    if transferred:
        producers = {label: Producer(label, specs[label], [inputs/label]) for label in sorted(LABELS)}
    else:
        directory = out.parent/"downloaded-R805"
        download(specs["R805"], directory, require_complete=True)
        p805 = Producer("R805", specs["R805"], [directory])
        carrier = p805.bound(R805_INPUT_BUNDLE)
        assert sha(carrier) == specs["R805"]["input_bundle_sha256"]
        assert carrier.stat().st_size == specs["R805"]["input_bundle_bytes"]
        old_carrier = dict(file_spec(carrier), producer=specs["R805"])
        original_inputs = out.parent/"R805-carried-original-inputs"
        extract_bundle(carrier, original_inputs, specs, original_R805=True)
        p786 = Producer("R786", specs["R786"], [original_inputs/"R786"])
        producers = {"R805": p805, "R786": p786}
    selection = select_original_inputs(producers, item)
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
        "all_inputs_from_same_core_active_R806_bundle": transferred,
        "fresh_original_producers_downloaded": [] if transferred else ["R805"],
        "original_R786_carrier": old_carrier,
        "R786_recovered_from_original_R805_carrier": not transferred,
        "unused_R775_R799_inputs_transferred": False,
        "input_bundle": file_spec(out/INPUT_BUNDLE), "old_arithmetic_recomputed": False})
    return inputs


def restore_resume(item, out):
    previous = item.get("resume")
    if previous is None:
        return
    directory = out.parent/"downloaded-R806-continuation"
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
    for key in ("result", "p", "core_sha256", "R805_proof_sha256", "R806_method_sha256",
                "retained_artifacts", "qY_count", "auxiliary_prime_start", "requested_stage",
                "dixon_group_columns", "reconstruct_every_digits"):
        assert initial["job"][key] == item[key], "Changed continuation identity: "+key
    bundle = bound(INPUT_BUNDLE)
    extract_bundle(bundle, out.parent/"retained", item["retained_artifacts"])
    shutil.copyfile(bundle, out/INPUT_BUNDLE)
    completed, current = 0, 0
    for name in entries:
        if not (name.startswith("R806-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        source = bound(name)
        data = read(source)
        matching_configuration(data["configuration"], item)
        if name.endswith("-dixon-current.json.gz"):
            assert data["complete"] is False
            assert data["complete_coordinates_claimed"] is False
            assert data["only_current_full_lift_vector_retained"] is True
            assert data["digits"] >= 1 and int(data["modulus"]) > 1
            current += 1
        else:
            assert data["complete"] is True
            completed += 1
        shutil.copyfile(source, out/name)
    save(out/"resume-receipt.json", {"result": RESULT, "producer": previous,
        "same_exact_core_sha256": item["core_sha256"],
        "complete_checkpoint_files_copied": completed, "current_Dixon_checkpoint_files_copied": current,
        "original_two_group_input_bundle_restored": True,
        "completed_products_modular_screens_and_rational_groups_preserved": True,
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
        "new_arithmetic": "only missing original products, modular primitive screens, accepted rational multiplier full820",
        "old_saved_products_recomputed": False,
        "M6_clearing_functions_polar_divisors_eta_or_height_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41 and item["producer_inputs_pending"] is False
        assert sha(core) == item["core_sha256"] and sha(__file__) == item["wrapper_sha256"]
        assert sha(proof) == item["R805_proof_sha256"] and sha(method) == item["R806_method_sha256"]
        assert sha(S/"R786_public_exact_power5_short_basis.py") == item["download_helper_sha256"]
        assert sha(S/"p41_public_actions_recovery.py") == item["io_helper_sha256"]
        assert item["qY_count"] == 41 and item["auxiliary_prime_start"] == 1000000007
        assert item["dixon_group_columns"] == item["reconstruct_every_digits"] == 8
        assert item["requested_stage"] == "primitive_multiplication_and_cyclic_certificate"
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
                error = "Budget reached; complete products, modular screens, rational groups and latest Dixon vectors retained."
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
        "actual_primitive_multiplier_computed": complete,
        "old_saved_products_recomputed": False,
        "M6_clearing_functions_polar_divisors_eta_or_height_computed": False,
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
    assert cert["completed_scope"] == "primitive_multiplication_and_cyclic_certificate"
    assert cert["normal_affine_basis_rank"] == FREE and cert["S_basis_dimension"] == DIM
    assert cert["qY_count"] == 41 and cert["full_coordinate_rows"] == ROWS
    assert cert["integer_scale"] == str(82**6)
    for key in ("exact_polynomial_multiplication_computed", "all272_columns_verified_in_all820_original_rows",
                "actual_cyclic_minor_certified", "original_function_field_primitive_generator_certified",
                "normal_integral_basis_preserved"):
        assert cert[key] is True
    for key in ("old_R805_ranks_selection_or_saved_products_recomputed",
                "characteristic_zero_Krylov_matrix_or_inverse_computed", "field_coordinate_transport_computed",
                "M6_clearing_computed", "original_function_DAG_computed",
                "polar_ideals_or_KM_representatives_computed", "actual_eta_rigidification_or_height_computed"):
        assert cert[key] is False
    assert not list(out.glob("R806-*-dixon-current.json.gz"))
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
    stages = {}
    for name, spec in entries.items():
        assert name.startswith("R806-") and name.endswith(".json.gz")
        stages[name] = stage(spec)
    def local(spec):
        assert plain_spec(spec) == entries[spec["file"]]
        return stages[spec["file"]]
    producers = {label: Producer(label, item["retained_artifacts"][label], [out.parent/"retained"/label])
                 for label in sorted(LABELS)}
    def source(spec):
        label = spec["producer"]
        if label == "R806":
            assert plain_spec(spec) == entries[spec["file"]]
        else:
            producers[label].bound(spec["file"], spec)
    p805, p786 = producers["R805"], producers["R786"]
    same_producer(p805.tag["retained_artifacts"]["R786"], p786.spec)
    original = p805.certificate
    chart = local(cert["coordinate_chart"])
    assert chart["original_R805_S_basis_index"] == original["S_basis_index"]
    assert chart["original_R805_pencil"] == original["pencil_stage"]
    assert chart["original_R805_free_basis"] == original["graded_free_basis_stage"]
    assert chart["original_R805_alias_index"] == original["alias_index"]
    index805 = p805.stage(original["S_basis_index"])
    minor805 = p805.stage(index805["short_minor"])
    pencil805 = p805.stage(original["pencil_stage"])
    assert chart["original_R805_short_minor"] == index805["short_minor"]
    assert chart["coordinate_row_indices"] == cert["configuration"]["coordinate_row_indices"] == minor805["row_indices"]
    assert cert["configuration"]["actual_sigma_integer_n"] == pencil805["n"]
    assert cert["configuration"]["original_R805_S_basis_index"] == original["S_basis_index"]
    assert cert["configuration"]["original_R805_short_minor"] == index805["short_minor"]
    assert chart["all_original_S_basis_rows"] == index805["basis_rows"]
    assert chart["full_rows"] == ROWS and chart["columns"] == DIM
    assert chart["integer_scale"] == str(82**6) and chart["normal_affine_basis_degrees"] == EPS
    for spec in chart["all_original_S_basis_rows"]:
        p805.bound(spec["file"], spec)
    accepted = local(cert["accepted_candidate"])
    candidate = accepted["candidate_index"]
    prime, z0 = accepted["prime"], accepted["z0"]
    assert candidate == cert["actual_candidate_index"]
    assert accepted["actual_cyclic_rank"] == FREE and accepted["actual_determinant_mod_prime"] % prime
    assert 0 <= z0 < prime and z0 <= 36458
    assert accepted["original_coordinate_chart"] == cert["coordinate_chart"]
    assert accepted["original_function_field_primitive_generator_certified"] is True
    assert accepted["characteristic_zero_Krylov_matrix_or_inverse_computed"] is False
    definition = local(accepted["candidate_definition"])
    assert definition["candidate_index"] == candidate
    assert definition["membership_in_original_V1_by_generation"] is True
    assert definition["w0_original_M2_integer_coordinates"] == accepted["w0_original_M2_integer_coordinates"] == \
        cert["actual_w0_original_M2_integer_coordinates"]
    assert len(definition["w0_original_M2_integer_coordinates"]) == 146
    inverse = local(accepted["fixed_minor_inverse"])
    assert inverse["prime"] == prime and inverse["prime_proved"] is True
    assert inverse["coordinate_row_indices"] == minor805["row_indices"]
    assert inverse["original_coordinate_chart"] == cert["coordinate_chart"]
    assert inverse["modular_inverse_identity_verified"] is True
    assert inverse["new_row_selection_or_old_R805_rank_recomputed"] is False
    assert inverse["characteristic_zero_inverse_matrix_formed"] is False
    assert len(inverse["inverse_mod_prime"]) == DIM
    assert all(len(row) == DIM for row in inverse["inverse_mod_prime"])
    modular = local(accepted["source_modular_multiplier"])
    assert modular["candidate_index"] == candidate and modular["prime"] == prime
    assert modular["fixed_minor_inverse"] == accepted["fixed_minor_inverse"]
    assert modular["candidate_definition"] == accepted["candidate_definition"]
    assert modular["all820_modular_equations_verified"] is True
    assert modular["weighted_polynomial_support_verified"] is True
    assert modular["genuine_characteristic_zero_V3_membership_by_generation"] is True
    assert len(modular["coordinates_mod_prime"]) == DIM
    assert all(len(row) == FREE for row in modular["coordinates_mod_prime"])
    product_index = local(modular["product_index"])
    assert product_index["candidate_index"] == candidate
    assert product_index["candidate_definition"] == accepted["candidate_definition"]
    assert product_index["product_columns"] == modular["product_columns"]
    assert product_index["column_count"] == FREE and product_index["full_coordinate_rows"] == ROWS
    assert len(product_index["product_columns"]) == FREE
    for column, spec in enumerate(product_index["product_columns"]):
        assert spec["column"] == column
        row = local(spec)
        assert row["candidate_index"] == candidate and row["column"] == column
        assert row["input_normal_basis_degree"] == EPS[column]
        assert row["candidate_definition"] == accepted["candidate_definition"]
        assert row["integer_scale"] == str(82**6) and row["qY_count"] == 41
        assert row["membership_in_original_V3_by_generation"] is True
        assert row["all_original_and_real_coordinates_verified"] is True
        assert len(row["integer_v_t_coefficients"]) == 41 and all(len(line) == 20 for line in row["integer_v_t_coefficients"])
        assert len(row["integer_qY_xi_coefficients"]) == 41 and all(len(line) == 40 for line in row["integer_qY_xi_coefficients"])
        for term in row["monomial_sources"]:
            source(term["source"])
    cyclic = local(accepted["cyclic_witness"])
    assert cyclic["candidate_index"] == candidate and cyclic["prime"] == prime and cyclic["z0"] == z0
    assert cyclic["source_modular_multiplier"] == accepted["source_modular_multiplier"]
    assert cyclic["actual_cyclic_rank"] == FREE and cyclic["actual_determinant_mod_prime"] == accepted["actual_determinant_mod_prime"]
    assert cyclic["primitive_generator_certified_by_actual_minor"] is True
    assert cyclic["characteristic_zero_nonprimitive_claimed_from_failure"] is False
    assert len(cyclic["successful_krylov_matrix_mod_prime"]) == FREE
    assert all(len(row) == FREE for row in cyclic["successful_krylov_matrix_mod_prime"])
    assert cert["actual_cyclic_minor"] == {"prime": prime, "z0": z0, "rank": FREE,
                                         "determinant_mod_prime": cyclic["actual_determinant_mod_prime"]}
    columns = []
    for spec in cert["exact_coordinate_groups"]:
        data = local(spec)
        assert data["candidate_index"] == candidate
        assert data["accepted_primitive_candidate"] == cert["accepted_candidate"]
        assert data["fixed_minor_inverse"] == accepted["fixed_minor_inverse"]
        assert data["source_modular_multiplier"] == accepted["source_modular_multiplier"]
        assert data["actual_prime"] == prime and data["actual_Dixon_digits"] >= 1
        assert int(data["actual_reconstruction_modulus"]) > 1
        assert data["basis_dimension"] == DIM and data["full_coordinate_rows"] == ROWS
        assert data["integer_scale"] == str(82**6)
        for key in ("all820_original_coordinates_verified", "weighted_polynomial_support_verified",
                    "reduction_equals_successful_modular_multiplier",
                    "rational_reconstruction_used_uniform_strict_rectangular_bound"):
            assert data[key] is True
        cc = data["column_indices"]
        assert 1 <= len(cc) <= 8
        assert len(data["coordinate_numerators"]) == DIM
        assert all(len(row) == len(cc) for row in data["coordinate_numerators"])
        assert len(data["column_denominators"]) == len(cc) and all(int(x) > 0 for x in data["column_denominators"])
        assert data["source_rhs"]["product_index"] == modular["product_index"]
        assert data["source_rhs"]["column_indices"] == cc
        assert data["source_rhs"]["product_columns"] == [modular["product_columns"][i] for i in cc]
        assert fingerprint(data["source_rhs"]) == data["rhs_binding_sha256"]
        columns.extend(cc)
    assert columns == list(range(FREE)) and len(cert["exact_coordinate_groups"]) == 34
    interface = local(cert["polynomial_multiplier"])
    assert interface["candidate_index"] == candidate and interface["accepted_primitive_candidate"] == cert["accepted_candidate"]
    assert interface["coordinate_groups"] == cert["exact_coordinate_groups"]
    assert interface["normal_affine_basis_rank"] == FREE and interface["normal_affine_basis_degrees"] == EPS
    assert interface["all272_columns_verified_in_all820_original_rows"] is True
    assert interface["all_weighted_support_zeros_verified"] is True
    assert interface["reduction_equals_successful_modular_multiplier"] is True
    assert interface["actual_cyclic_witness"] == accepted["cyclic_witness"]
    mapping = interface["S_row_to_polynomial_coefficient"]
    assert len(mapping) == DIM
    for row, entry in enumerate(mapping):
        if row < 4:
            output, power = 0, row
        elif row < 436:
            output, power = 1+(row-4)//3, (row-4) % 3
        else:
            output, power = 145+(row-436)//2, (row-436) % 2
        assert entry == {"S_row": row, "normal_basis_row": output, "power_of_z": power}
    assert interface["normal_integral_basis_preserved"] is True and interface["K_z_w_assumed_normal"] is False
    for name, data in stages.items():
        if name.startswith("R806-new-monomial-"):
            assert data["old_recipe_alias_exists"] is False and data["old_R805_product_exists"] is False
            assert data["old_saved_product_recomputed"] is False
            assert data["all_original_and_real_coordinates_verified"] is True
            for spec in data["factor_sources"]:
                source(spec)
        if name.endswith("-cyclic.json.gz"):
            assert data["characteristic_zero_nonprimitive_claimed_from_failure"] is False
        if name.endswith("-rejected-fixed-minor.json.gz"):
            assert data["characteristic_zero_rank_loss_claimed"] is False
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
