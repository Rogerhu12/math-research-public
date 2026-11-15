#!/usr/bin/env python3
"""R804: four original producer groups, exact point nodes, read-only publication boundary."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
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
REQUEST = TOPIC/"notes/R804-public-original-selected-CM-points-request.json"
RESULT = "R804-original-selected-CM-point-values"
FINAL = "p41-original-selected-CM-point-values-certificate.json"
INPUT_BUNDLE = "R804-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
LABELS = {"R792", "R735", "R791", "R794"}
DIRECT = ("R792", "R794")
PRODUCER_META = ("full-outputs-manifest.json", "run-receipt.json",
                 "core-receipt.json", "public-actions-input.json")
META = {"public-actions-input.json", "retained-inputs-receipt.json",
        "resume-receipt.json", "run-receipt.json", "core-receipt.json"}
MODEL = "p41-original-CM-model-certificate.json"
MODEL_SHA = "752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574"
HOM = "R791-original-Hom-Galois-matrices.json.gz"
HOM_SHA = "f3793ddc7680b718a4448d45587661182986a3558db346ad0a2c9031c8952183"
DESCENT = "R791-original-real-descent-and-eta-basis-inputs.json.gz"
DESCENT_SHA = "24a894163f136a4e8c71b117e373f8fafb66a6e0c94b4efe3f141f78bb39b968"
SELECTED = "R794-selected-original-low-degree-eta-basis.json.gz"
SELECTED_SHA = "5b96f623e1f43d834a7db21064ff2cb101284b9a4038e5434eb291b6e73f6e0f"
FIELD_CORE_SHA = "f196cb805d1ca91e8995866032a0a3ec3f96aac06e03b67a7c1f196fff759251"
CANDIDATES = [0, 3, 1, 21, 15]
DEGREES = [1485, 1521, 1602, 1674, 1728]
R792_POINT = "R792-original-beta-C-and-real-descent-point.json.gz"


BETA_SCHEMAS = {
    "R792-original-beta-composition": {
        "core_sha256": "7b7a5483e560f2d244092af486c8aed606b18c1f3557dddb3b850a290b4e343d",
        "certificate_name": "p41-original-beta-composition-certificate.json",
        "point_key": "point_spec", "manifest": "R792-stage-manifest.json.gz",
        "bundle": "R792-retained-producer-inputs.tar.gz",
        "parent_groups": {"R735", "R775", "R786", "R787", "R790", "R791"}},
    "R792-original-beta-from-R824-relation": {
        "core_sha256": "a8a33d32b19525896a137fcf02c3fbf07ced88207839e9c89f16c9c527e827bf",
        "certificate_name": "p41-original-beta-from-R824-relation-certificate.json",
        "point_key": "point_stage", "manifest": "R792-R824-stage-manifest.json.gz",
        "bundle": "R792-R824-retained-producer-inputs.tar.gz",
        "parent_groups": {"R735", "R775", "R786", "R824", "R790", "R791"}},
}


def beta_schema(spec):
    value = BETA_SCHEMAS[spec["result"]]
    assert spec["core_sha256"] == value["core_sha256"]
    assert spec["certificate_name"] == value["certificate_name"]
    return value


def parent_contract(label, spec):
    if label == "R792":
        return beta_schema(spec)
    assert label == "R794" and spec["result"] == "R794-original-low-degree-eta-basis"
    return {"bundle": "R794-retained-producer-inputs.tar.gz", "parent_groups": {"R759", "R791"}}


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


def same_producer(left, right):
    for key in ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256", "certificate_name"):
        assert str(left[key]) == str(right[key]), ("producer identity", key)
    name = left["certificate_name"]
    assert left["files"][name] == right["files"][name]
    for name in set(left["files"]) & set(right["files"]):
        assert left["files"][name] == right["files"][name]


def matching_configuration(tag, item):
    assert tag["result"] == RESULT and tag["source_sha256"] == item["core_sha256"]
    assert tag["python_flint"] == "0.9.0" and tag["p"] == 41
    for key in ("R804_proof_sha256", "R804_point_interface_sha256", "field_core_sha256",
                "retained_artifacts", "selected_candidate_indices", "selected_addition_node_count"):
        assert tag[key] == item[key]
    assert tag["field_core_sha256"] == FIELD_CORE_SHA
    assert tag["selected_candidate_indices"] == CANDIDATES and tag["selected_addition_node_count"] == 8
    beta_input = beta_schema(item["retained_artifacts"]["R792"])
    assert tag["actual_beta_input_result"] == item["retained_artifacts"]["R792"]["result"]
    assert tag["actual_beta_input_point_field"] == beta_input["point_key"]
    assert tag["original_model_certificate_sha256"] == MODEL_SHA
    assert tag["original_map_index"] == 4 and tag["original_map_degree"] == "1206"
    assert tag["original_c1"] == 4424 and tag["T_seventh_power"] == "zeta^2"
    assert tag["original_target"] == "C_b:y^2=x^3+b; L=Q(b,zeta); original b"
    assert tag["Hom_word_basis"] == "1,T,...,T^11 modulo original Phi21; zeta=T^14; zeta^2=T^7"
    for key in ("original_A_coordinate_lift_computed", "R803_global_M6_coordinates_consumed",
                "old_beta_periods_Hom_matrices_or_Laurent_recomputed"):
        assert tag[key] is False


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
    """Pure IO only: the original full manifest and unchanged producer files."""
    def __init__(self, label, spec, directories):
        assert label in LABELS
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
        run, receipt, initial = (read(self.paths[name]) for name in PRODUCER_META[1:])
        assert run["result"] == spec["result"] and run["complete"] is True and run["process_exit_code"] == 0
        assert str(run["workflow_run_id"]) == str(spec["run_id"])
        assert run["source_commit"] == initial["source_commit"] == spec["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["result"] == spec["result"]
        if label == "R735":
            assert "result" not in receipt and receipt["p"] == 41
        else:
            assert receipt["result"] == spec["result"]
        assert receipt["complete"] is True and receipt["source_sha256"] == spec["core_sha256"]
        if label in ("R791", "R794"):
            assert "core_receipt_sha256" not in run and "core_sha256" not in initial
            assert initial["job"]["core_sha256"] == spec["core_sha256"]
        else:
            assert run["core_receipt_sha256"] == sha(self.paths["core-receipt.json"])
            assert initial["core_sha256"] == spec["core_sha256"]
        self.initial = initial
        name = spec["certificate_name"]
        assert self.entries[name]["sha256"] == receipt["certificate_sha256"] == spec["files"][name]
        self.certificate = read(self.select(name))
        assert self.certificate["complete"] is True
        if label == "R735":
            assert name == MODEL and self.entries[name]["sha256"] == MODEL_SHA
            identity = self.certificate["identity"]
            assert identity["source_sha256"] == spec["core_sha256"]
            assert identity["p"] == 41 and identity["python_flint"] == "0.9.0"
            assert self.certificate["original_b_not_a_replacement_twist"] is True
            self.tag = None
        else:
            assert self.certificate["result"] == spec["result"]
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
        data = read(self.select(row["file"], row))
        assert data["complete"] is True and data["configuration"] == self.tag
        return data

    def cert_stage(self, name, digest):
        stages = {row["file"]: row for row in self.certificate["stages"]}
        assert len(stages) == len(self.certificate["stages"])
        assert stages[name]["sha256"] == digest
        return self.stage(stages[name])


def point_encoding(data):
    """Only encoding validation. Exact curve arithmetic is confined to the core."""
    if data["status"] == "infinity":
        assert data["projective_coordinates"] == ["0", "1", "0"]
        return
    assert data["status"] == "finite" and data["projective_z"] == "1"
    for key in ("x_original_L", "y_original_L"):
        value = data[key]
        assert isinstance(value, list) and len(value) == 2
        for component in value:
            assert set(component) == {"numerator", "denominator"}
            assert isinstance(component["denominator"], str) and component["denominator"] != "0"
            assert isinstance(component["numerator"], list)
            assert all(isinstance(coefficient, str) for coefficient in component["numerator"])


def select_original_inputs(producers):
    assert set(producers) == LABELS
    r792, r735, r791, r794 = (producers[label] for label in ("R792", "R735", "R791", "R794"))
    beta_input = beta_schema(r792.spec)
    assert r735.spec["result"] == "R732-p41-original-CM-model"
    assert r791.spec["result"] == "R791-original-Hom-Galois-and-eta-inputs"
    assert r794.spec["result"] == "R794-original-low-degree-eta-basis"
    for label in ("R735", "R791"):
        same_producer(r792.initial["job"]["retained_artifacts"][label], producers[label].spec)
        same_producer(r792.tag["retained_artifacts"][label], producers[label].spec)
    same_producer(r794.initial["job"]["retained_artifacts"]["R791"], r791.spec)
    same_producer(r794.tag["retained_artifacts"]["R791"], r791.spec)
    assert r791.tag["field_helper_sha256"] == r792.tag["field_core_sha256"] == FIELD_CORE_SHA
    assert r791.tag["retained_inputs"][MODEL] == MODEL_SHA
    assert r791.tag["retained_inputs"]["R754-gamma-descent.json.gz"] == \
        "cf37105d407ace9df6b86a80d112b58915202bfecfc9e2fd118f4be76af2b1d0"
    hom, descent = r791.cert_stage(HOM, HOM_SHA), r791.cert_stage(DESCENT, DESCENT_SHA)
    assert hom["gamma_order"] == 21 and hom["gamma_seventh_power"] == "zeta^2"
    assert hom["Phi21_ascending"] == [1, -1, 0, 1, -1, 0, 1, 0, -1, 1, 0, -1, 1]
    assert hom["all_84_coordinates_verified"] is True and hom["all_three_actions_integral_unimodular"] is True
    assert hom["remaining_elliptic_factor_included"] is False
    assert len(hom["rho_iterates_zero_through_seven"]) == 8
    assert descent["selected_real_map_degree"] == "3618" and descent["selected_real_map_recipe"] == "f+c(f)"
    assert descent["selected_real_map_Hom_coordinates"] == ["0", "0", "0", "0", "1", "0", "-1", "0", "0", "0", "0", "0"]
    for key in ("unknown_original_kappa_set_to_one", "original_vdagger_v_replaced_by_scalar", "original_q_alpha_or_c1_changed"):
        assert descent[key] is False
    selected = r794.cert_stage(SELECTED, SELECTED_SHA)
    assert selected["selected_candidate_indices"] == CANDIDATES
    assert selected["original_kappa_e_R_q_c0_c1_preserved"] is True
    assert [row["candidate_index"] for row in selected["selected_maps"]] == CANDIDATES
    assert [str(row["map_degree"]) for row in selected["selected_maps"]] == [str(value) for value in DEGREES]
    for row in selected["selected_maps"]:
        assert len(row["original_Hom_integer_column"]) == len(row["a_in_Q_T_mod_Phi21"]) == 12
        assert all(coefficient[1] == "1" for coefficient in row["a_in_Q_T_mod_Phi21"])
    cert = r792.certificate
    assert cert["p"] == 41 and cert["original_map_index"] == 4 and cert["original_map_degree"] == "1206"
    for key in ("actual_beta_C_computed", "actual_real_descent_image_computed"):
        assert cert[key] is True
    for key in ("original_A_coordinate_lift_computed", "actual_heights_or_uniformity_computed"):
        assert cert[key] is False
    point_spec = cert[beta_input["point_key"]]
    assert cert["stage_manifest"]["file"] == beta_input["manifest"] and point_spec["file"] == R792_POINT
    if r792.spec["result"] == "R792-original-beta-from-R824-relation":
        assert cert["original_y_ratio_preserved"] is True
        assert cert["synthetic_R787_producer_or_relation_file_created"] is False
        assert cert["original_R824_denominator_and_content_reinserted"] is False
    inventory = r792.stage(cert["stage_manifest"])
    entries = {row["file"]: row for row in inventory["files"]}
    assert len(entries) == len(inventory["files"])
    assert plain_spec(entries[R792_POINT]) == plain_spec(point_spec)
    point = r792.stage(point_spec)
    assert point["original_map_index"] == 4 and point["original_map_degree"] == "1206"
    assert point["original_c1"] == 4424 and point["original_c0_image"] == "O"
    assert point["actual_beta_C_computed"] is True and point["actual_real_descent_image_computed"] is True
    assert point["original_A_coordinate_lift_computed"] is False
    if point["point_status"] == "infinity":
        assert point["beta_C"] == point["real_descent_image"] == "O"
    else:
        assert point["point_status"] == "finite"
        for names in (("x_original_L", "y_original_L"), ("x_real_descent_Fb", "y_real_descent_Fb")):
            point_encoding({"status": "finite", "projective_z": "1",
                            "x_original_L": point[names[0]], "y_original_L": point[names[1]]})
        for key in ("original_elliptic_equation_verified", "original_Galois_direction_verified",
                    "real_descent_elliptic_equation_verified"):
            assert point[key] is True
    return {"four_original_producer_groups_bound": True,
            "actual_R792_original_beta_stage": plain_spec(point_spec),
            "actual_beta_input_result": r792.spec["result"],
            "actual_beta_input_point_field": beta_input["point_key"],
            "actual_R792_original_beta_point_status": point["point_status"],
            "same_original_R791_bound_by_both_R792_and_R794": True,
            "original_R754_sigma_rho_reused_from_certified_R791_stage": True,
            "original_b_model_and_original_v_kappa_preserved": True,
            "new_R754_period_or_Hom_computation": False,
            "old_q_rows_or_Laurent_stages_transferred": False}


def allowed_group_name(label, spec, name):
    if name in set(PRODUCER_META)|set(spec["files"]):
        return True
    return label == "R792" and name in (beta_schema(spec)["manifest"], R792_POINT)


def extract_bundle(bundle, target, specs, parent=None, child=None):
    """Select only required regular, two-level files from an active carrier."""
    assert (parent is None) == (child is None)
    target.mkdir(parents=True, exist_ok=True)
    seen, count = set(), 0
    with tarfile.open(bundle, "r:gz") as archive:
        for member in archive:
            relative = Path(member.name)
            assert member.isfile() and not relative.is_absolute() and ".." not in relative.parts
            assert len(relative.parts) == 2 and str(relative) not in seen
            seen.add(str(relative))
            group, name = relative.parts
            assert group in (LABELS if parent is None else parent_contract(parent, specs[parent])["parent_groups"])
            if parent is not None and group != child:
                continue
            if not allowed_group_name(group, specs[group], name):
                assert parent is not None, (group, name)
                continue
            destination = target/relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            temporary = destination.with_name(destination.name+".tmp")
            with archive.extractfile(member) as source, temporary.open("wb") as output:
                shutil.copyfileobj(source, output)
            assert temporary.stat().st_size == member.size
            if destination.exists():
                assert destination.stat().st_size == member.size and sha(destination) == sha(temporary)
                temporary.unlink()
            else:
                temporary.replace(destination)
            count += 1
    assert count
    return count


def transfer(paths, target):
    target.mkdir(parents=True, exist_ok=True)
    for name, path in paths.items():
        destination = target/name
        assert Path(name).name == name
        if path.resolve() == destination.resolve():
            continue
        if destination.exists():
            assert destination.stat().st_size == path.stat().st_size and sha(destination) == sha(path)
        else:
            shutil.copyfile(path, destination)


def prepare_inputs(item, out):
    specs = item["retained_artifacts"]
    assert set(specs) == LABELS
    inputs = out.parent/"retained"
    present = [(inputs/label/"full-outputs-manifest.json").exists() for label in LABELS]
    restored = all(present)
    assert restored or not any(present), "Partial unverified R804 input carrier"
    parent_transfers = []
    if restored:
        producers = {label: Producer(label, specs[label], [inputs/label]) for label in sorted(LABELS)}
    else:
        producers = {}
        for label in DIRECT:
            directory = out.parent/("downloaded-"+label)
            download(specs[label], directory, require_complete=True)
            producers[label] = Producer(label, specs[label], [directory])
        for parent_label, child_label in (("R792", "R735"), ("R794", "R791")):
            parent = producers[parent_label]
            same_producer(parent.initial["job"]["retained_artifacts"][child_label], specs[child_label])
            same_producer(parent.tag["retained_artifacts"][child_label], specs[child_label])
            bundle_name = parent_contract(parent_label, parent.spec)["bundle"]
            bundle = parent.bound(bundle_name)
            carried = out.parent/(parent_label+"-carried-original-inputs")
            count = extract_bundle(bundle, carried, specs, parent_label, child_label)
            producers[child_label] = Producer(child_label, specs[child_label], [carried/child_label])
            parent_transfers.append({"parent": parent_label, "child": child_label,
                "source_bundle": plain_spec(parent.entries[bundle_name]),
                "selected_carried_file_count": count,
                "original_parent_recorded_source_run_core_manifest_and_certificate_match": True})
    selection = select_original_inputs(producers)
    groups = []
    for label in sorted(LABELS):
        producer = producers[label]
        transfer(producer.selected, inputs/label)
        actual = {path.name for path in (inputs/label).iterdir() if path.is_file()}
        assert actual == set(producer.selected), (label, "unexpected retained input")
        groups.append({"label": label, "producer": specs[label], "file_count": len(actual),
                       "original_manifest_all_selected_bytes_sha_and_schema_verified": True})
    if not (out/INPUT_BUNDLE).exists():
        temporary = out/(INPUT_BUNDLE+".tmp")
        with tarfile.open(temporary, "w:gz") as archive:
            for path in sorted(inputs.rglob("*")):
                if path.is_file():
                    archive.add(path, arcname=path.relative_to(inputs).as_posix(), recursive=False)
        temporary.replace(out/INPUT_BUNDLE)
    save(out/"retained-inputs-receipt.json", {"result": RESULT, "groups": groups, "selection": selection,
        "all_inputs_from_same_core_active_R804_bundle": restored,
        "fresh_original_producers_downloaded": [] if restored else list(DIRECT),
        "parent_bundle_transfers": parent_transfers, "input_bundle": file_spec(out/INPUT_BUNDLE),
        "only_required_four_group_files_retained": True, "old_arithmetic_recomputed": False})
    return inputs


def restore_resume(item, out):
    previous = item.get("resume")
    if previous is None:
        return
    directory = out.parent/"downloaded-R804-continuation"
    download(previous, directory, require_complete=False)
    mp = find_hash(directory, "full-outputs-manifest.json", previous["manifest_sha256"])
    manifest = read(mp)
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
    for key in ("result", "p", "core_sha256", "R804_proof_sha256", "R804_point_interface_sha256",
                "field_core_sha256", "retained_artifacts", "selected_candidate_indices", "selected_addition_node_count"):
        assert initial["job"][key] == item[key], "Changed continuation identity: "+key
    bundle = bound(INPUT_BUNDLE)
    extract_bundle(bundle, out.parent/"retained", item["retained_artifacts"])
    shutil.copyfile(bundle, out/INPUT_BUNDLE)
    count = 0
    for name in entries:
        if not (name.startswith("R804-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        source = bound(name)
        data = read(source)
        assert data["complete"] is True
        matching_configuration(data["configuration"], item)
        shutil.copyfile(source, out/name)
        count += 1
    save(out/"resume-receipt.json", {"result": RESULT, "producer": previous,
        "same_exact_core_sha256": item["core_sha256"], "complete_checkpoint_files_copied": count,
        "four_group_original_input_bundle_restored": True,
        "completed_exact_point_nodes_preserved": True, "completed_mathematical_stages_recomputed": False})


def output_manifest(out):
    artifact = "serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    rows = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name in ("full-outputs-manifest.json", REFERENCE):
            continue
        rows.append(dict(file_spec(path), artifact=artifact, included_in_git=False,
            eligible_for_reviewed_small_metadata=path.name in META and path.stat().st_size < 100_000))
    mp = out/"full-outputs-manifest.json"
    save(mp, {"result": RESULT, "files": rows, "temporary_active_checkpoint_artifact": artifact,
        "temporary_active_checkpoint_retention_days": 1,
        "reproducible_points_certificates_or_input_bundles_in_git_or_release": False})
    save(out/REFERENCE, {"result": RESULT, "manifest_file": mp.name, "manifest_sha256": sha(mp),
        "manifest_bytes": mp.stat().st_size, "file_count": len(rows), "full_outputs_artifact": artifact,
        "manifest_in_git": False, "automatic_git_or_release_publication": False})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core, field_core = S/item["core"], S/item["field_core"]
    proof, interface = topic_path(item["proof"]), topic_path(item["interface"])
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {"result": RESULT, "p": 41,
        "source_repository": "Rogerhu12/math-research-public", "source_commit": source,
        "job": item, "core_sha256": sha(core), "field_core_sha256": sha(field_core),
        "proof_sha256": sha(proof), "interface_sha256": sha(interface),
        "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "workflow_sha256": sha(REPO/item["workflow"]),
        "download_helper_sha256": sha(S/"R786_public_exact_power5_short_basis.py"),
        "io_helper_sha256": sha(S/"p41_public_actions_recovery.py"),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "new_arithmetic": "eight original selected-map point additions, original Galois transports and vbeta check",
        "old_beta_periods_Hom_matrices_or_Laurent_recomputed": False,
        "original_A_kernel_preimage_global_polar_divisors_eta_or_heights_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41 and item["producer_inputs_pending"] is False
        assert sha(core) == item["core_sha256"] and sha(__file__) == item["wrapper_sha256"]
        assert sha(proof) == item["R804_proof_sha256"] and sha(interface) == item["R804_point_interface_sha256"]
        assert sha(field_core) == item["field_core_sha256"] == FIELD_CORE_SHA
        assert sha(S/"R786_public_exact_power5_short_basis.py") == item["download_helper_sha256"]
        assert sha(S/"p41_public_actions_recovery.py") == item["io_helper_sha256"]
        assert item["selected_candidate_indices"] == CANDIDATES and item["selected_addition_node_count"] == 8
        restore_resume(item, out)
        retained = prepare_inputs(item, out)
        config = out.parent/"job-config.json"
        save(config, item)
        command = [sys.executable, "-u", str(core), "--config", str(config), "--proof", str(proof),
            "--interface", str(interface), "--field-core", str(field_core), "--retained", str(retained),
            "--output", str(out), "--budget-minutes", str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60+120)
            except subprocess.TimeoutExpired:
                error = "Budget reached; completed source-bound original point nodes retained for continuation."
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
        "actual_five_original_CM_points_computed": complete, "actual_original_vbeta_verified": complete,
        "original_A_coordinate_lift_computed": False,
        "global_polar_divisors_eta_values_or_heights_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete, "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    """All byte/schema/dependency checks, without importing the mathematical core."""
    run, receipt, initial = (read(out/name) for name in ("run-receipt.json", "core-receipt.json", "public-actions-input.json"))
    assert run["result"] == RESULT and run["complete"] is True and run["process_exit_code"] == 0
    assert run["core_receipt_sha256"] == sha(out/"core-receipt.json")
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert run["source_commit"] == initial["source_commit"]
    assert initial["job"] == item
    for key in ("core_sha256", "field_core_sha256"):
        assert initial[key] == item[key]
    assert initial["driver_sha256"] == item["wrapper_sha256"]
    assert receipt["result"] == RESULT and receipt["complete"] is True
    assert receipt["source_sha256"] == item["core_sha256"] and receipt["certificate_sha256"] == sha(out/FINAL)
    assert receipt["all_five_original_CM_points_computed"] is True and receipt["actual_original_vbeta_verified"] is True
    assert receipt["original_A_coordinate_lift_computed"] is False
    assert receipt["global_polar_divisors_eta_values_or_heights_computed"] is False
    cert = read(out/FINAL)
    assert cert["result"] == RESULT and cert["complete"] is True and cert["p"] == 41
    tag = cert["configuration"]
    matching_configuration(tag, item)
    assert cert["selected_candidate_indices"] == CANDIDATES and cert["selected_map_degrees"] == DEGREES
    assert cert["selected_addition_node_count"] == 8
    for key in ("all_five_original_CM_points_computed", "all_five_short_Hom_words_match_original_R794",
                "all_original_elliptic_point_equations_verified", "point_branches_include_O_opposites_doubling_and_two_torsion",
                "point_collisions_not_decided_by_Hom_labels", "original_T7_equals_zeta2_preserved", "actual_original_vbeta_verified"):
        assert cert[key] is True
    for key in ("R803_global_M6_coordinates_consumed", "old_beta_periods_Hom_matrices_or_Laurent_recomputed",
                "original_A_coordinate_lift_computed", "global_polar_divisors_computed", "eta_values_computed", "heights_computed"):
        assert cert[key] is False
    manifest = read(out/"full-outputs-manifest.json")
    assert manifest["result"] == RESULT
    entries = {row["file"]: row for row in manifest["files"]}
    assert len(entries) == len(manifest["files"])
    for name, row in entries.items():
        assert Path(name).name == name and file_spec(out/name) == plain_spec(row)
    source_inputs = {label: Producer(label, item["retained_artifacts"][label], [out.parent/"retained"/label])
                     for label in sorted(LABELS)}
    selection = select_original_inputs(source_inputs)
    carried = read(out/"retained-inputs-receipt.json")
    assert carried["result"] == RESULT and carried["selection"] == selection
    assert carried["input_bundle"] == file_spec(out/INPUT_BUNDLE)
    assert carried["only_required_four_group_files_retained"] is True and carried["old_arithmetic_recomputed"] is False
    actual_carried = {}
    with tarfile.open(out/INPUT_BUNDLE, "r:gz") as archive:
        import hashlib
        for member in archive:
            relative = Path(member.name)
            assert member.isfile() and len(relative.parts) == 2 and ".." not in relative.parts
            group, name = relative.parts
            assert group in LABELS and str(relative) not in actual_carried
            assert name in source_inputs[group].selected
            digest = hashlib.sha256()
            with archive.extractfile(member) as stream:
                for block in iter(lambda: stream.read(1024*1024), b""):
                    digest.update(block)
            expected = file_spec(source_inputs[group].selected[name])
            assert member.size == expected["bytes"] and digest.hexdigest() == expected["sha256"]
            actual_carried[str(relative)] = expected
    expected_names = {label+"/"+name for label, producer in source_inputs.items() for name in producer.selected}
    assert set(actual_carried) == expected_names
    inventory_spec = cert["stage_manifest"]
    assert file_spec(out/inventory_spec["file"]) == inventory_spec
    inventory = read(out/inventory_spec["file"])
    assert inventory["complete"] is True and inventory["configuration"] == tag
    stages = {row["file"]: row for row in inventory["files"]}
    assert len(stages) == len(inventory["files"])
    headers = {}
    for name, row in stages.items():
        assert plain_spec(entries[name]) == row and file_spec(out/name) == row
        data = read(out/name)
        assert data["complete"] is True and data["configuration"] == tag
        matching_configuration(data["configuration"], item)
        if "point" in data:
            point_encoding(data["point"])
        if name.startswith("R804-point-node-"):
            assert len(data["Hom_word"]) == 12
            assert data["original_elliptic_equation_verified"] is True
            assert data["specialized_point_comparison_not_Hom_inequality_selects_addition_branch"] is True
            for dependency in data["sources"]:
                assert dependency == stages[dependency["file"]]
        headers[name] = data
    reference = cert["reference_beta_stage"]
    assert reference == stages[reference["file"]]
    ref = headers[reference["file"]]
    assert ref["source_original_point"] == dict(selection["actual_R792_original_beta_stage"], producer="R792")
    assert ref["old_beta_recomputed"] is False and ref["original_c0_translation_added"] is False
    addition_names = [name.removeprefix("R804-point-node-").removesuffix(".json.gz")
        for name, data in headers.items() if data.get("operation", {}).get("kind") == "selected_Hom_addition"]
    assert len(addition_names) == 8 and set(addition_names) == set(cert["selected_addition_node_names"])
    selected = read(source_inputs["R794"].selected[SELECTED])
    original_maps = {row["candidate_index"]: row for row in selected["selected_maps"]}
    assert set(cert["selected_point_stages"]) == {str(value) for value in CANDIDATES}
    for candidate, degree in zip(CANDIDATES, DEGREES):
        spec = cert["selected_point_stages"][str(candidate)]
        assert spec == stages[spec["file"]]
        data, old = headers[spec["file"]], original_maps[candidate]
        assert data["candidate_index"] == candidate and data["map_degree"] == str(degree)
        assert data["original_Hom_integer_column"] == old["original_Hom_integer_column"]
        assert data["actual_R794_a_in_Q_T_mod_Phi21"] == old["a_in_Q_T_mod_Phi21"]
        assert data["computed_short_chain_Hom_word"] == [pair[0] for pair in old["a_in_Q_T_mod_Phi21"]]
        final_node = data["source_final_point_node"]
        assert final_node == stages[final_node["file"]]
        assert data["point"] == headers[final_node["file"]]["point"]
        assert data["actual_original_Hom_word_matched"] is True and data["actual_g_at_original_c1_computed"] is True
        assert data["original_elliptic_equation_verified"] is True and data["original_c0_image"] == "O"
        assert data["global_polar_divisor_eta_or_height_computed"] is False
    phase_spec = cert["original_T7_phase_check"]
    assert phase_spec == stages[phase_spec["file"]]
    phase = headers[phase_spec["file"]]
    assert phase["actual_reference_point_identity_verified"] is True and phase["original_Hom_T_order"] == 21
    assert phase["T7_was_not_replaced_by_identity"] is True
    for key in ("T7_point", "zeta2_point"):
        assert phase[key] == stages[phase[key]["file"]]
    assert headers[phase["T7_point"]["file"]]["point"] == headers[phase["zeta2_point"]["file"]]["point"]
    image_spec = cert["original_vbeta_stage"]
    assert image_spec == stages[image_spec["file"]]
    image = headers[image_spec["file"]]
    assert image["source_original_beta_node"] == reference
    assert image["source_original_point"] == ref["source_original_point"]
    for key in ("actual_original_isogeny_image_verified", "original_Fb_coordinates_verified", "original_v_and_kappa_preserved"):
        assert image[key] is True
    for key in ("unknown_original_kappa_set_to_one", "original_vdagger_v_replaced_by_scalar",
                "original_A_coordinate_lift_computed", "global_polar_divisors_eta_values_or_heights_computed"):
        assert image[key] is False
    print(json.dumps({"result": RESULT, "verified": True, "selected_points": 5,
        "selected_addition_nodes": 8, "stage_files": len(stages), "retained_files": len(actual_carried),
        "actual_original_vbeta_verified": True, "original_A_coordinate_lift_computed": False}), flush=True)
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
    return verify(read(out/"public-actions-input.json")["job"], out)


if __name__ == "__main__":
    sys.exit(main())
