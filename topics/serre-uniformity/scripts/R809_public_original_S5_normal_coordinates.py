#!/usr/bin/env python3
"""R809 public runner: one S5 block and incrementally requested actual normal vectors."""
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
REQUEST = TOPIC/"notes/R809-public-original-S5-normal-coordinates-request.json"
RESULT = "R809-original-S5-normal-coordinates"
FINAL = "p41-original-S5-normal-coordinate-certificate.json"
INPUT_BUNDLE = "R809-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
REQUIRED = {"R805", "R786", "R803", "R807"}
TARGETS = ["C"+str(j) for j in range(6)]+["A", "B"]
FIELD_BASIS = "b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b"
PRODUCER_META = ("full-outputs-manifest.json", "run-receipt.json",
                 "core-receipt.json", "public-actions-input.json")
META = {"public-actions-input.json", "retained-inputs-receipt.json",
        "resume-receipt.json", "run-receipt.json", "core-receipt.json"}
R805_CORE_SHA = "730a7d8f51d76d1153386c63f2e082285ada4573a2baf8d87d1825d3ce75b420"
DIMS = {1: 146, 2: 418, 3: 690, 4: 962, 5: 1234}
DIM, ROWS, FREE = 1234, 1380, 272
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


def producer_identity(spec):
    answer = {key: spec[key] for key in
              ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256", "certificate_name")}
    answer["certificate_sha256"] = spec["files"][spec["certificate_name"]]
    return answer


def matching_configuration(tag, item):
    assert tag["result"] == RESULT and tag["source_sha256"] == item["core_sha256"]
    assert tag["python_flint"] == "0.9.0" and tag["p"] == 41
    for key in ("R809_proof_sha256", "R809_method_sha256", "qY_count",
                "auxiliary_prime_start", "dixon_group_columns", "reconstruct_every_digits"):
        assert tag[key] == item[key]
    assert tag["qY_count"] == 69 and tag["full_coordinate_rows"] == ROWS
    assert tag["S_basis_dimension"] == DIM and tag["normal_affine_basis_rank"] == FREE
    assert tag["normal_basis_degrees"] == EPS
    assert tag["basis_integer_scale"] == str(82**10)
    assert tag["basis_producers"] == {label: producer_identity(item["retained_artifacts"][label])
                                     for label in ("R805", "R786", "R807")}
    assert tag["coefficient_field_basis"] == FIELD_BASIS
    assert tag["dixon_group_columns"] == 7 and tag["reconstruct_every_digits"] == 8
    assert tag["old_R805_ranks_or_original_R786_prefixes_recomputed"] is False
    assert tag["requested_targets_budget_and_future_R787_excluded_from_basis_identity"] is True


def matching_target(tag, basis_tag, item):
    assert tag["basis_configuration_sha256"] == fingerprint(basis_tag)
    target = tag["target"]
    assert target in TARGETS and tag["coefficient_field_basis"] == FIELD_BASIS
    labels = ("R803", "R807") if target.startswith("C") else ("R787",)
    assert tag["target_producers"] == {label: producer_identity(item["retained_artifacts"][label])
                                      for label in labels}
    assert tag["regular_degree_bound"] == (4 if target.startswith("C") else 5)
    if target.startswith("C"):
        assert tag["literal_tau_factor_highest_S5_terms_zero"] is True
        assert tag["normal_function"] == "theta*U_"+target[1:]+"/tau^4"
    else:
        assert tag["normal_function"] == target+"/tau^5"
        assert tag["common_R787_denominator_or_content_reinserted"] is False


def allowed_group_name(label, spec, name):
    if name in set(PRODUCER_META)|set(spec["files"]):
        return True
    if label == "R786":
        match = re.fullmatch(r"R786-exact-power-([12345])-row-(\d{4})\.json\.gz", name)
        if match:
            return 0 <= int(match[2]) < DIMS[int(match[1])]
        return name.startswith("R786-") and name.endswith(".json.gz")
    return label in {"R805", "R803", "R807", "R787"} and name.startswith(label+"-") and name.endswith(".json.gz")


def extract_bundle(bundle, target, specs):
    target.mkdir(parents=True, exist_ok=True)
    seen, count = set(), 0
    with tarfile.open(bundle, "r:gz") as archive:
        for member in archive:
            relative = Path(member.name)
            assert member.isfile() and not relative.is_absolute() and ".." not in relative.parts
            assert len(relative.parts) == 2 and str(relative) not in seen
            seen.add(str(relative))
            label, name = relative.parts
            assert label in specs and allowed_group_name(label, specs[label], name)
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
    """Only existing JSON schemas, receipts and hashes; no flint or mathematical core."""
    p805, p786, p803, p807 = (producers[label] for label in ("R805", "R786", "R803", "R807"))
    assert p805.spec["core_sha256"] == R805_CORE_SHA
    for producer in (p805, p803, p807):
        same_producer(producer.tag["retained_artifacts"]["R786"], p786.spec)
    same_producer(p807.tag["retained_artifacts"]["R805"], p805.spec)
    inventories = {}
    for label, producer in producers.items():
        key = "stages_manifest" if label == "R786" else "stage_manifest"
        inventories[label] = producer.inventory(key)
    def stage(label, spec):
        assert plain_spec(spec) == inventories[label][spec["file"]]
        return producers[label].stage(spec)
    cert805, cert803, cert807 = p805.certificate, p803.certificate, p807.certificate
    assert cert805["completed_scope"] == "pencil_and_graded_free_basis"
    assert cert805["affine_free_module_rank"] == FREE
    assert cert805["all_S_rows_original_and_real_coordinates_verified"] is True
    pencil = stage("R805", cert805["pencil_stage"])
    free = stage("R805", cert805["graded_free_basis_stage"])
    alias = stage("R805", cert805["alias_index"])
    S3index = stage("R805", cert805["S_basis_index"])
    assert pencil["basepoint_free_certified_by_actual_unit_minor"] is True
    assert pencil["actual_rank"] == 690
    assert free["degree1_original_indices"] == list(range(2, 146))
    assert len(free["degree2_original_indices"]) == 127
    assert S3index["dimension"] == 690 and S3index["integer_scale"] == str(82**6)
    previous_leaves = set()
    for name, spec in inventories["R805"].items():
        if name.startswith("R805-new-monomial-") and name.endswith(".json.gz"):
            value = stage("R805", spec)
            leaves = tuple(value["sorted_M2_leaf_indices"])
            assert 2 <= len(leaves) <= 3 and leaves == tuple(sorted(leaves))
            assert value["qY_count"] == 41
            assert value["integer_scale"] == str(82**(2*len(leaves)))
            assert value["all_original_and_real_coordinates_verified"] is True
            assert len(value["integer_qY_xi_coefficients"]) == len(value["integer_v_t_coefficients"]) == 41
            assert all(len(row) == 40 for row in value["integer_qY_xi_coefficients"])
            assert all(len(row) == 20 for row in value["integer_v_t_coefficients"])
            previous_leaves.add(leaves)
    assert p786.certificate["exact_K_basis_prefix_bound_qY"] == 128
    assert p786.certificate["basis_in_original_R775_saved_order"] is True
    if "basis_index" in p786.certificate:
        stage("R786", p786.certificate["basis_index"])
    old_alias = {(row["power"], row["index"]): row for row in alias["rows"]}
    assert len(old_alias) == 1254
    recipes = {}
    for power in DIMS:
        for index in range(DIMS[power]):
            name = "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"
            data = stage("R786", inventories["R786"][name])
            assert data["weight"] == 2*power and data["bound_qY"] == 128
            assert data["integer_scale"] == str(82**(2*power))
            assert data["original_R775_finite_coefficients_verified"] is True
            assert len(data["integer_qY_xi_coefficients"]) == 129
            assert all(len(row) == 40 for row in data["integer_qY_xi_coefficients"])
            recipes[power, index] = data["recipe"]
            if (power, index) in old_alias:
                old = old_alias[power, index]
                assert old["recipe"] == data["recipe"]
                assert plain_spec(old["source"]) == plain_spec(p786.entries[name])
    assert cert803["M6_dimension"] == 694 and cert803["qY_count"] == 42
    assert cert803["all84_rational_RHS_columns_verified_in_all1680_original_rows"] is True
    assert cert803["original_b_and_s_coordinate_basis_preserved"] is True
    M6 = stage("R803", cert803["basis_index"])
    stage("R803", cert803["ratio_interface"])
    assert M6["dimension"] == 694 and len(M6["basis_rows"]) == 694
    for index in range(690):
        assert M6["basis_rows"][index]["recipe"] == {"kind": "power_basis", "power": 3, "index": index}
        name = "R786-exact-power-3-row-"+str(index).zfill(4)+".json.gz"
        assert plain_spec(M6["basis_rows"][index]["source"]) == plain_spec(p786.entries[name])
    for j in range(6):
        data = stage("R803", cert803["coordinate_stages"][str(j)])
        assert data["j"] == j and data["basis_dimension"] == 694
        assert data["basis_integer_scale"] == str(82**6)
        assert data["coefficient_field_basis"] == FIELD_BASIS
        assert data["all1680_original_coordinates_verified"] is True
        rows = data["coefficients_in_integer_scaled_original_M6_basis"]
        assert len(rows) == 694 and all(len(row) == 14 for row in rows)
        assert all(len(pair) == 2 and int(pair[1]) > 0 for row in rows for pair in row)
    for index in range(690, 694):
        name = "R803-new-original-M6-short-row-"+str(index)+".json.gz"
        data = stage("R803", inventories["R803"][name])
        assert data["index"] == index and data["bound_qY"] == 41
        assert data["integer_scale"] == str(82**6)
        assert data["new_complete_short_row_verified_against_original_M6_mod739"] is True
        assert len(data["integer_qY_xi_coefficients"]) == 42
        assert all(len(row) == 40 for row in data["integer_qY_xi_coefficients"])
    name = "R803-mixed-original-Hodge-scalars-j1.json.gz"
    b_model = stage("R803", inventories["R803"][name])["original_b_model"]
    assert cert807["actual_nonzero_theta_constructed"] is True
    assert cert807["all_four_M6_products_verified_in_all1100_rows"] is True
    theta = stage("R807", cert807["theta_stage"])
    index = stage("R807", cert807["cleared_coordinate_index"])
    assert index["theta_stage"] == cert807["theta_stage"]
    assert plain_spec(index["source_original_M6"]) == plain_spec(M6["original_M6_stage"])
    assert theta["source_original_M2_indices"] == list(range(5))
    assert len(theta["lambda"]) == 5
    assert theta["theta_in_original_integer_scaled_M2_basis"] == theta["lambda"]+[["0", "1"]]*141
    assert theta["theta_nonzero_by_original_independent_M2_input"] is True
    for key, spec in cert807["cleared_coordinate_stages"].items():
        assert key in {"690", "691", "692", "693"}
        value = stage("R807", spec)
        assert value["all1100_rows_verified"] is True
    assert set(cert807["cleared_coordinate_stages"]) == {"690", "691", "692", "693"}
    for spec in cert807["actual_new_pair_tail_stages"]:
        value = stage("R807", spec)
        assert value["first_exponent"] == 41 and value["last_exponent_exclusive"] == 55
        assert value["only_new_sum_band_convolved"] is True
        pair = tuple(value["sorted_M2_leaf_indices"])
        assert pair in previous_leaves
        assert len(value["integer_qY_xi_coefficients"]) == len(value["integer_v_t_coefficients"]) == 14
    if "R787" in producers:
        p787 = producers["R787"]
        cert = p787.certificate
        assert cert["actual_y_map_recovered"] is True
        assert cert["exact_nonzero_A_B_relation_verified"] is True
        assert cert["exact_verified_orders"] == 129 and cert["original_map_index"] == 4
        same_producer(p787.tag["retained_artifacts"]["R786"], p786.spec)
        relation = stage("R787", cert["relation_spec"])
        assert relation["original_R786_basis_order"] is True
        assert relation["basis_integer_scale"] == str(82**10)
        assert relation["field"]["original_b_minimal_polynomial"] == b_model
        assert int(relation["field"]["lambda"]) > 0
        assert relation["L_basis"] == "B^i*s^j, j=0..1 outer, i=0..6; B=lambda*b"
        assert relation["candidate_only_until_full_exact_verification"] is False
        assert relation["full_129_original_relations_verified"] is True
        for key in ("A_integer_L_coordinates", "B_integer_L_coordinates"):
            assert len(relation[key]) == DIM and all(len(row) == 14 for row in relation[key])
    assert set(item["requested_target_groups"]) <= set(TARGETS)
    assert not set(item["requested_target_groups"]) & {"A", "B"} or "R787" in producers
    return {
        "all_original_receipts_hashes_configurations_and_required_schemas_verified": True,
        "R786_original_degree1_through5_rows": sum(DIMS.values()),
        "R805_actual_new_monomial_prefixes": len(previous_leaves),
        "R803_original_coordinate_groups": list(range(6)),
        "R807_actual_new_pair_tail_count": len(cert807["actual_new_pair_tail_stages"]),
        "original_sigma_integer_n": pencil["n"],
        "requested_target_groups": item["requested_target_groups"],
        "original_b_model": b_model,
        "new_mathematical_arithmetic_executed": False,
    }


def prepare_inputs(item, out):
    specs = item["retained_artifacts"]
    labels = set(specs)
    assert REQUIRED <= labels <= REQUIRED | {"R787"}
    inputs = out.parent/"retained"
    inputs.mkdir(parents=True, exist_ok=True)
    producers, downloaded, restored, cached_downloads = {}, [], [], []
    for label in sorted(labels):
        present = inputs/label/"full-outputs-manifest.json"
        if present.exists():
            producer = Producer(label, specs[label], [inputs/label])
            restored.append(label)
        else:
            directory = out.parent/("downloaded-"+label)
            existing = list(directory.rglob("full-outputs-manifest.json")) if directory.exists() else []
            if existing:
                producer = Producer(label, specs[label], [directory])
                cached_downloads.append(label)
            else:
                download(specs[label], directory, require_complete=True)
                producer = Producer(label, specs[label], [directory])
                downloaded.append(label)
        producers[label] = producer
    selection = select_original_inputs(producers, item)
    groups = []
    for label in sorted(labels):
        producer = producers[label]
        transfer(producer.selected, inputs/label)
        actual = {path.name for path in (inputs/label).iterdir() if path.is_file()}
        assert actual == set(producer.selected), (label, "unexpected or incomplete retained input set")
        groups.append({"label": label, "producer": specs[label], "file_count": len(actual),
                       "original_manifest_and_all_selected_file_hashes_verified": True})
    previous_bundle = file_spec(out/INPUT_BUNDLE) if (out/INPUT_BUNDLE).exists() else None
    temporary = out/(INPUT_BUNDLE+".tmp")
    with tarfile.open(temporary, "w:gz") as archive:
        for path in sorted(inputs.rglob("*")):
            if path.is_file():
                archive.add(path, arcname=path.relative_to(inputs).as_posix(), recursive=False)
    temporary.replace(out/INPUT_BUNDLE)
    save(out/"retained-inputs-receipt.json", {
        "result": RESULT, "groups": groups, "selection": selection,
        "previous_active_input_bundle": previous_bundle,
        "source_groups_reused_from_active_R809_bundle": restored,
        "fresh_original_producers_downloaded": downloaded,
        "original_producers_reused_from_verified_local_download_cache": cached_downloads,
        "missing_later_producers_added_without_replacing_existing_identity": True,
        "input_bundle": file_spec(out/INPUT_BUNDLE), "old_arithmetic_recomputed": False,
    })
    return inputs


def restore_resume(item, out):
    previous = item.get("resume")
    if previous is None:
        return
    directory = out.parent/"downloaded-R809-continuation"
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
    old = initial["job"]
    for key in ("result", "p", "core_sha256", "R809_proof_sha256", "R809_method_sha256",
                "qY_count", "auxiliary_prime_start", "dixon_group_columns", "reconstruct_every_digits"):
        assert old[key] == item[key], "Changed continuation identity: "+key
    assert set(old["retained_artifacts"]) <= set(item["retained_artifacts"])
    for label, spec in old["retained_artifacts"].items():
        same_producer(spec, item["retained_artifacts"][label])
    bundle = bound(INPUT_BUNDLE)
    extract_bundle(bundle, out.parent/"retained", old["retained_artifacts"])
    shutil.copyfile(bundle, out/INPUT_BUNDLE)
    complete, current = 0, 0
    for name in entries:
        if not (name.startswith("R809-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        source = bound(name)
        data = read(source)
        matching_configuration(data["configuration"], item)
        if "target_configuration" in data:
            matching_target(data["target_configuration"], data["configuration"], item)
            assert data["target_configuration_sha256"] == fingerprint(data["target_configuration"])
        if name.endswith("-dixon-current.json.gz"):
            assert data["complete"] is False and data["complete_coordinates_claimed"] is False
            assert data["only_current_full_lift_vector_retained"] is True
            current += 1
        else:
            assert data["complete"] is True
            complete += 1
        shutil.copyfile(source, out/name)
    save(out/"resume-receipt.json", {
        "result": RESULT, "producer": previous, "same_exact_core_sha256": item["core_sha256"],
        "previous_requested_target_groups": old["requested_target_groups"],
        "new_requested_target_groups": item["requested_target_groups"],
        "complete_checkpoint_files_copied": complete, "current_Dixon_checkpoint_files_copied": current,
        "old_completed_scope_certificate": entries.get(FINAL),
        "existing_producer_identity_preserved_and_new_producers_only_appended": True,
        "basis_and_completed_target_mathematical_stages_recomputed": False,
    })


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
        "new_arithmetic": "only missing S5 products and target transport; shared exact 1234 block, actual targets full1380",
        "old_saved_products_recomputed": False,
        "actual_polar_ideal_or_eta_or_height_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41 and item["producer_inputs_pending"] is False
        assert sha(core) == item["core_sha256"] and sha(__file__) == item["wrapper_sha256"]
        assert sha(proof) == item["R809_proof_sha256"] and sha(method) == item["R809_method_sha256"]
        assert sha(S/"R786_public_exact_power5_short_basis.py") == item["download_helper_sha256"]
        assert sha(S/"p41_public_actions_recovery.py") == item["io_helper_sha256"]
        assert item["qY_count"] == 69 and item["auxiliary_prime_start"] == 1000000007
        assert item["dixon_group_columns"] == 7 and item["reconstruct_every_digits"] == 8
        assert item["requested_target_groups"] and set(item["requested_target_groups"]) <= set(TARGETS)
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
                error = "Budget reached; completed basis, actual targets, exact groups and latest divided-residual Dixon vectors retained."
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
        "requested_target_groups": item["requested_target_groups"],
        "completed_target_groups": receipt.get("completed_target_groups", []),
        "actual_original_y_normal_vectors_computed": receipt.get("actual_original_y_normal_vectors_computed", False),
        "old_saved_products_recomputed": False,
        "actual_polar_ideal_or_eta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete, "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    core = read(out/"core-receipt.json")
    run = read(out/"run-receipt.json")
    assert run["result"] == core["result"] == RESULT
    assert run["complete"] is True and run["process_exit_code"] == 0 and core["complete"] is True
    assert run["core_receipt_sha256"] == sha(out/"core-receipt.json")
    assert core["source_sha256"] == item["core_sha256"]
    assert core["certificate_sha256"] == sha(out/FINAL)
    cert = read(out/FINAL)
    assert cert["result"] == RESULT and cert["complete"] is True
    matching_configuration(cert["configuration"], item)
    assert cert["p"] == 41 and cert["S5_dimension"] == DIM
    assert cert["qY_count"] == 69 and cert["full_real_coordinates"] == ROWS
    assert cert["normal_basis_rank"] == FREE and cert["normal_basis_degrees"] == EPS
    assert cert["coefficient_field_basis"] == FIELD_BASIS
    assert cert["basis_integer_scale"] == str(82**10)
    assert cert["requested_target_groups"] == item["requested_target_groups"]
    completed = cert["completed_target_groups"]
    assert completed == [target for target in TARGETS if target in completed]
    assert set(item["requested_target_groups"]) <= set(completed)
    assert cert["completed_rational_RHS_columns"] == 14*len(completed)
    assert cert["actual_original_y_normal_vectors_computed"] is ({"A", "B"} <= set(completed))
    assert cert["all_112_rational_targets_computed"] is (len(completed) == 8)
    assert cert["all_requested_targets_verified_in_all1380_rows"] is True
    assert cert["all_completed_C_targets_highest_S5_coefficients_zero"] is True
    assert cert["original_scalar_and_field_normalizations_preserved"] is True
    assert cert["actual_polar_ideal_or_eta_or_height_computed"] is False
    assert cert["characteristic_zero_Krylov_inverse_computed"] is False
    assert cert["basis_identity_excludes_requested_scope_budget_and_future_R787"] is True
    manifest = read(out/"full-outputs-manifest.json")
    assert manifest["result"] == RESULT
    files = {row["file"]: row for row in manifest["files"]}
    assert len(files) == len(manifest["files"])
    for name, spec in files.items():
        path = out/name
        assert Path(name).name == name and path.stat().st_size == spec["bytes"] and sha(path) == spec["sha256"]
        assert spec["included_in_git"] is False
    reference = read(out/REFERENCE)
    assert reference["manifest_sha256"] == sha(out/"full-outputs-manifest.json")
    inputs = out.parent/"retained"
    if not all((inputs/label/"full-outputs-manifest.json").exists() for label in item["retained_artifacts"]):
        extract_bundle(out/INPUT_BUNDLE, inputs, item["retained_artifacts"])
    producers = {label: Producer(label, spec, [inputs/label])
                 for label, spec in item["retained_artifacts"].items()}
    selection = select_original_inputs(producers, item)
    assert selection["new_mathematical_arithmetic_executed"] is False
    tag = cert["configuration"]
    p805, p807 = producers["R805"], producers["R807"]
    assert tag["actual_sigma_integer_n"] == read(p805.paths[p805.certificate["pencil_stage"]["file"]])["n"]
    assert tag["actual_R807_available_pair_tails"] == p807.certificate["actual_new_pair_tail_stages"]
    inventory_spec = cert["stage_manifest"]
    assert plain_spec(files[inventory_spec["file"]]) == plain_spec(inventory_spec)
    inventory = read(out/inventory_spec["file"])
    assert inventory["complete"] is True and inventory["configuration"] == tag
    stages = {row["file"]: row for row in inventory["files"]}
    assert len(stages) == len(inventory["files"])
    for name, spec in stages.items():
        assert plain_spec(files[name]) == plain_spec(spec)
        data = read(out/name)
        assert data["complete"] is True and data["configuration"] == tag
        if "target_configuration" in data:
            matching_target(data["target_configuration"], tag, item)
            assert data["target_configuration_sha256"] == fingerprint(data["target_configuration"])
        assert not name.endswith("-dixon-current.json.gz")
    def stage(spec, target=None):
        assert plain_spec(spec) == plain_spec(stages[spec["file"]])
        data = read(out/spec["file"])
        assert data["complete"] is True and data["configuration"] == tag
        if target is not None:
            assert data["target_configuration"] == cert["completed_target_configurations"][target]
            assert data["target_configuration_sha256"] == fingerprint(data["target_configuration"])
        return data
    basis = stage(cert["S5_basis_index"])
    assert basis["dimension"] == DIM and basis["qY_count"] == 69
    assert basis["integer_scale"] == str(82**10)
    assert len(basis["basis_rows"]) == DIM
    expected = [(a, j) for a, eps in enumerate(EPS) for j in range(6-eps)]
    for index, (row, pair) in enumerate(zip(basis["basis_rows"], expected)):
        assert row["index"] == index
        assert (row["normal_basis_index"], row["z_degree"]) == pair
        assert row["normal_basis_degree"] == EPS[pair[0]]
        data = stage(row["source"])
        assert data["recipe"] == row["recipe"] and data["index"] == index
        assert data["all_original_term_phases_and_scales_verified"] is True
        assert len(data["integer_v_t_coefficients"]) == 69
        assert all(len(part) == 20 for part in data["integer_v_t_coefficients"])
    minor = stage(cert["minor_stage"])
    assert minor["actual_rank"] == DIM and minor["full_coordinate_rows"] == ROWS
    assert minor["column_indices"] == list(range(DIM))
    assert len(minor["row_indices"]) == DIM and minor["row_indices"] == sorted(set(minor["row_indices"]))
    assert all(0 <= value < ROWS for value in minor["row_indices"])
    assert minor["prime"] == cert["actual_prime"]
    assert minor["actual_determinant_mod_prime"] == cert["actual_short_minor_determinant"]
    assert minor["actual_determinant_mod_prime"] % minor["prime"]
    assert minor["minor_is_from_actual_69_term_matrix"] is True
    assert minor["S5_basis_index"] == cert["S5_basis_index"]
    inverse = stage(cert["modular_inverse_stage"])
    assert inverse["minor_stage"] == cert["minor_stage"]
    assert inverse["inverse_product_exactly_verified_mod_prime"] is True
    assert inverse["composite_modulus_matrix_inversion"] is False
    assert len(inverse["inverse_mod_prime"]) == DIM
    assert all(len(row) == DIM for row in inverse["inverse_mod_prime"])
    assert set(cert["normal_vectors"]) == set(completed)
    for target in completed:
        target_tag = cert["completed_target_configurations"][target]
        matching_target(target_tag, tag, item)
        vector = stage(cert["normal_vectors"][target], target)
        assert vector["target"] == target and vector["normal_basis_rank"] == FREE
        assert vector["regular_degree_bound"] == (4 if target.startswith("C") else 5)
        assert vector["coefficient_field_basis"] == FIELD_BASIS
        assert vector["S5_basis_index"] == cert["S5_basis_index"]
        assert vector["normal_vector_actually_nonzero"] is True
        assert vector["all1380_original_coordinates_verified"] is True
        assert vector["weighted_polynomial_support_verified"] is True
        assert vector["original_field_and_scalar_normalizations_preserved"] is True
        assert vector["actual_polar_ideal_or_eta_or_height_computed"] is False
        covered, nonzero = [], False
        for spec in vector["coordinate_groups"]:
            data = stage(spec, target)
            indices = data["column_indices"]
            assert indices in [list(range(7)), list(range(7, 14))]
            assert data["all1380_original_coordinates_verified"] is True
            assert data["fixed_minor_inverse"] == cert["modular_inverse_stage"]
            assert data["S5_basis_index"] == cert["S5_basis_index"]
            assert data["rational_reconstruction_used_uniform_strict_rectangular_bound"] is True
            assert data["coefficient_field_basis"] == FIELD_BASIS
            assert data["basis_integer_scale"] == str(82**10)
            values = data["coordinate_numerators"]
            denominators = data["column_denominators"]
            scales = data["original_target_rational_scales"]
            assert len(values) == DIM and all(len(row) == len(indices) for row in values)
            assert len(denominators) == len(scales) == len(indices)
            assert all(int(value) > 0 for value in denominators)
            assert all(len(pair) == 2 and int(pair[1]) > 0 for pair in scales)
            target_prefix = stage(data["source_full_target"], target)
            assert scales == [target_prefix["rational_scales"][k] for k in indices]
            for (a, degree), row in zip(expected, values):
                for k, value in enumerate(row):
                    if target.startswith("C") and degree > 4-EPS[a]:
                        assert int(value) == 0
                    if int(value) and int(scales[k][0]):
                        nonzero = True
            covered.extend(indices)
        assert covered == list(range(14)) and nonzero
    interface = stage(cert["normal_function_interface"])
    assert interface["normal_vectors"] == cert["normal_vectors"]
    assert interface["actual_normal_ring_multipliers_or_field_quotients_computed"] is False
    assert interface["actual_derivation_polar_ideal_eta_or_height_computed"] is False
    print(json.dumps({"result": RESULT, "complete": True, "completed_target_groups": completed,
        "completed_rational_RHS_columns": 14*len(completed),
        "full_coordinate_rows": ROWS, "actual_prime": cert["actual_prime"],
        "actual_short_minor_determinant": cert["actual_short_minor_determinant"],
        "actual_polar_ideal_or_eta_or_height_computed": False}), flush=True)
    return 0


def main():
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["prepare", "compute", "verify"])
    parser.add_argument("--request", type=Path, default=REQUEST)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.mode == "prepare":
        assert args.output is not None, "Pure IO preparation requires an explicit output directory."
        args.output.mkdir(parents=True, exist_ok=True)
        request = read(args.request)
        assert request["session"] == "serre-public-astra-20261115"
        prepare_inputs(request["job"], args.output)
        print(json.dumps({"pure_IO_only": True, "receipt": str(args.output/"retained-inputs-receipt.json"),
                          "new_mathematical_arithmetic_executed": False}), flush=True)
        return 0
    guard()
    out = args.output or Path(os.environ["RUNNER_TEMP"])/"serre-global"/RESULT/"output"
    if args.mode == "compute":
        request = read(args.request)
        assert request["session"] == "serre-public-astra-20261115"
        return compute(request["job"], out)
    item = read(out/"public-actions-input.json")["job"]
    return verify(item, out)


if __name__ == "__main__":
    sys.exit(main())
