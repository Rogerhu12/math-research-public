#!/usr/bin/env python3
"""R813 source-bound runner for two original S3 Wronskian inputs."""
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
REQUEST = TOPIC/"notes/R813-public-original-Wronskian-derivation-inputs-request.json"
RESULT = "R813-original-Wronskian-derivation-inputs"
FINAL = "p41-original-Wronskian-derivation-inputs-certificate.json"
INPUT_BUNDLE = "R813-retained-producer-inputs.tar.gz"
R806_INPUT_BUNDLE = "R806-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
LABELS = {"R805", "R786", "R806"}
PRODUCER_META = ("full-outputs-manifest.json", "run-receipt.json",
                 "core-receipt.json", "public-actions-input.json")
META = {"public-actions-input.json", "retained-inputs-receipt.json",
        "resume-receipt.json", "run-receipt.json", "core-receipt.json"}
R805_CORE_SHA = "730a7d8f51d76d1153386c63f2e082285ada4573a2baf8d87d1825d3ce75b420"
R806_CORE_SHA = "b014f9b3cb4923421e6a879eddb4da58dd0baefb28d61a2191f6b0a33e51810d"
R805_PROOF_SHA = "b48d9f8dd5d8d1a89aa2574ab7f9ee014b83ca21baf41694252b9c53993571e8"
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



def producer_identity(spec):
    keys = ("result", "run_id", "source_commit", "core_sha256",
            "manifest_sha256", "certificate_name")
    answer = {key: spec[key] for key in keys}
    answer["certificate_sha256"] = spec["files"][spec["certificate_name"]]
    return answer


def S_mapping():
    return [{"S_row": i, "normal_basis_row": a, "power_of_z": j}
            for i, (a, j) in enumerate((a, j) for a, eps in enumerate(EPS) for j in range(4-eps))]


def matching_configuration(tag, item):
    assert tag["result"] == RESULT and tag["source_sha256"] == item["core_sha256"]
    assert tag["python_flint"] == "0.9.0" and tag["p"] == 41
    for key in ("R813_proof_sha256", "R813_method_sha256", "qY_count",
                "original_D0_qY_multiplier", "target_names", "reconstruct_every_digits"):
        assert tag[key] == item[key]
    assert tag["producer_identities"] == {
        label: producer_identity(item["retained_artifacts"][label]) for label in sorted(LABELS)}
    assert tag["qY_count"] == 41 and tag["full_coordinate_rows"] == ROWS
    assert tag["S3_basis_dimension"] == DIM and tag["normal_basis_rank"] == FREE
    assert tag["normal_basis_degrees"] == EPS
    assert tag["original_M2_integer_scale"] == str(82**2)
    assert tag["original_V2_integer_scale"] == str(82**4)
    assert tag["original_S3_integer_scale"] == str(82**6)
    assert tag["original_D0_qY_multiplier"] == ["1", "82"] and tag["target_names"] == ["g", "h"]
    assert tag["reconstruct_every_digits"] == 8
    assert tag["Wronskian_generation"] == "D0(tau*s)-2*s*D0(tau); all tau*e_i are old V2[i]"
    assert tag["old_S3_selection_inverse_or_original_product_prefixes_recomputed"] is False
    assert tag["actual_Mg_Mh_Gamma_or_height_computed"] is False
    assert len(tag["actual_w0_original_M2_integer_coordinates"]) == 146
    assert tag["actual_w0_original_M2_integer_coordinates"][:2] == ["0", "0"]
    assert len(tag["coordinate_row_indices"]) == DIM


def allowed_group_name(label, spec, name):
    if name in set(PRODUCER_META)|set(spec["files"]):
        return True
    if label == "R786":
        match = re.fullmatch(r"R786-exact-power-([123])-row-(\d{4})\.json\.gz", name)
        return bool(match and 0 <= int(match[2]) < DIMS[int(match[1])])
    return name.startswith(label+"-") and name.endswith(".json.gz")


def extract_bundle(bundle, target, specs, original_R806=False):
    """Only unchanged flat producer files; no links, traversal or arithmetic."""
    target.mkdir(parents=True, exist_ok=True)
    seen, count = set(), 0
    groups = {"R805", "R786"} if original_R806 else LABELS
    with tarfile.open(bundle, "r:gz") as archive:
        for member in archive:
            relative = Path(member.name)
            assert member.isfile() and not relative.is_absolute() and ".." not in relative.parts
            assert len(relative.parts) == 2 and str(relative) not in seen
            seen.add(str(relative))
            group, name = relative.parts
            assert group in groups and group in specs
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


def select_completed_basis_inputs(p805, p786):
    """Schema/SHA audit of already complete bases, independent of any future R806 value."""
    assert p805.spec["core_sha256"] == R805_CORE_SHA
    same_producer(p805.tag["retained_artifacts"]["R786"], p786.spec)
    same_producer(p805.initial["job"]["retained_artifacts"]["R786"], p786.spec)
    assert p805.tag["R805_proof_sha256"] == R805_PROOF_SHA
    cert = p805.certificate
    assert cert["completed_scope"] == "pencil_and_graded_free_basis"
    assert cert["affine_free_module_rank"] == FREE and cert["graded_free_basis_degrees"] == [1, 144, 127]
    assert cert["degree3_S_basis_dimension"] == DIM and cert["degree3_S_prefix_count"] == 41
    assert cert["degree3_S_full_real_coordinates"] == ROWS
    assert cert["all_S_rows_original_and_real_coordinates_verified"] is True
    assert cert["original_82_scales_preserved"] is True
    inventory805 = p805.inventory("stage_manifest")
    inventory786 = p786.inventory("stages_manifest")
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
    assert aliases["source_powers"] == [1, 2, 3] and len(aliases["rows"]) == 1254
    old_aliases = {(row["power"], row["index"]): row for row in aliases["rows"]}
    assert len(old_aliases) == 1254
    assert p786.certificate["exact_K_basis_prefix_bound_qY"] == 128
    assert p786.certificate["basis_in_original_R775_saved_order"] is True
    for i in range(146):
        alias = old_aliases[2, i]
        name = "R786-exact-power-2-row-"+str(i).zfill(4)+".json.gz"
        assert alias["sorted_M2_leaf_indices"] == sorted((0, i))
        assert alias["source"] == dict(plain_spec(p786.entries[name]), producer="R786")
        assert plain_spec(alias["source"]) == inventory786[name]
    return {"certificate": cert, "pencil": pencil, "free": free, "index": index,
            "aliases": aliases, "old_aliases": old_aliases, "minor": minor,
            "inventory805": inventory805, "inventory786": inventory786}


def select_original_inputs(producers, item):
    """Select the exact already-complete source closure. This function performs no new arithmetic."""
    assert set(producers) == LABELS
    p805, p786, p806 = (producers[label] for label in ("R805", "R786", "R806"))
    basis = select_completed_basis_inputs(p805, p786)
    cert805, cert806 = p805.certificate, p806.certificate
    assert p806.spec["core_sha256"] == R806_CORE_SHA
    assert p806.spec["result"] == "R806-original-primitive-multiplication"
    assert p806.tag["R805_proof_sha256"] == R805_PROOF_SHA
    for label in ("R805", "R786"):
        same_producer(p806.tag["retained_artifacts"][label], producers[label].spec)
        same_producer(p806.initial["job"]["retained_artifacts"][label], producers[label].spec)
    assert cert806["completed_scope"] == "primitive_multiplication_and_cyclic_certificate"
    assert cert806["normal_affine_basis_rank"] == FREE and cert806["S_basis_dimension"] == DIM
    assert cert806["qY_count"] == 41 and cert806["full_coordinate_rows"] == ROWS
    assert cert806["integer_scale"] == str(82**6)
    for key in ("exact_polynomial_multiplication_computed", "all272_columns_verified_in_all820_original_rows",
                "actual_cyclic_minor_certified", "original_function_field_primitive_generator_certified",
                "normal_integral_basis_preserved"):
        assert cert806[key] is True
    inventory806 = p806.inventory("stage_manifest")
    def stage806(spec):
        assert plain_spec(spec) == inventory806[spec["file"]]
        return p806.stage(spec)
    chart = stage806(cert806["coordinate_chart"])
    index = basis["index"]
    assert chart["original_R805_pencil"] == cert805["pencil_stage"]
    assert chart["original_R805_free_basis"] == cert805["graded_free_basis_stage"]
    assert chart["original_R805_S_basis_index"] == cert805["S_basis_index"]
    assert chart["original_R805_short_minor"] == index["short_minor"]
    assert chart["all_original_S_basis_rows"] == index["basis_rows"]
    assert chart["full_rows"] == ROWS and chart["columns"] == DIM
    assert chart["integer_scale"] == str(82**6) and chart["normal_affine_basis_degrees"] == EPS
    I = chart["coordinate_row_indices"]
    assert I == basis["minor"]["row_indices"]
    accepted = stage806(cert806["accepted_candidate"])
    definition = stage806(accepted["candidate_definition"])
    assert accepted["original_coordinate_chart"] == cert806["coordinate_chart"]
    assert accepted["original_function_field_primitive_generator_certified"] is True
    assert accepted["actual_cyclic_rank"] == FREE
    assert accepted["actual_determinant_mod_prime"] % accepted["prime"]
    assert definition["candidate_index"] == accepted["candidate_index"] == cert806["actual_candidate_index"]
    assert definition["original_integer_scale"] == str(82**2)
    w0 = definition["w0_original_M2_integer_coordinates"]
    assert len(w0) == 146 and w0[:2] == ["0", "0"] and any(int(x) for x in w0)
    assert accepted["w0_original_M2_integer_coordinates"] == w0
    assert cert806["actual_w0_original_M2_integer_coordinates"] == w0
    multiplier = stage806(cert806["polynomial_multiplier"])
    assert multiplier["accepted_primitive_candidate"] == cert806["accepted_candidate"]
    assert multiplier["coordinate_chart"] == cert806["coordinate_chart"]
    assert multiplier["w0_original_M2_integer_coordinates"] == w0
    assert multiplier["all272_columns_verified_in_all820_original_rows"] is True
    assert multiplier["normal_integral_basis_preserved"] is True
    assert multiplier["coefficient_field"] == "Q, certified by exact original rational coordinate equations"
    assert multiplier["S_row_to_polynomial_coefficient"] == S_mapping()
    inverse = stage806(accepted["fixed_minor_inverse"])
    assert inverse["original_coordinate_chart"] == cert806["coordinate_chart"]
    assert inverse["original_R805_short_minor"] == index["short_minor"]
    assert inverse["coordinate_row_indices"] == I and inverse["fixed_minor_dimension"] == DIM
    assert inverse["modular_inverse_identity_verified"] is True
    assert inverse["new_row_selection_or_old_R805_rank_recomputed"] is False
    assert inverse["prime"] == accepted["prime"] and inverse["prime"] > 82
    assert inverse["prime_proved"] is True
    assert len(inverse["inverse_mod_prime"]) == DIM
    assert all(len(row) == DIM for row in inverse["inverse_mod_prime"])
    n = int(basis["pencil"]["n"])
    support = sorted({0, 1} | ({73} if n else set()) | {i for i, value in enumerate(w0) if int(value)})
    for i in support:
        for power in (1, 2):
            alias = basis["old_aliases"][power, i]
            name = "R786-exact-power-"+str(power)+"-row-"+str(i).zfill(4)+".json.gz"
            source = dict(plain_spec(p786.entries[name]), producer="R786")
            assert alias["source"] == source
            assert alias["sorted_M2_leaf_indices"] == ([i] if power == 1 else sorted((0, i)))
            spec = basis["inventory786"][name]
            assert plain_spec(source) == spec
            row = p786.stage(spec)
            assert row["recipe"] == alias["recipe"]
            assert row["weight"] == 2*power and row["bound_qY"] == 128
            assert row["integer_scale"] == str(82**(2*power))
            assert row["original_R775_finite_coefficients_verified"] is True
            assert len(row["integer_qY_xi_coefficients"]) == 129
            assert all(len(line) == 40 for line in row["integer_qY_xi_coefficients"])
    for producer in producers.values():
        assert all(name in producer.selected for name in producer.spec["files"]), (producer.label, "unused pinned input")
    configuration = {
        "result": RESULT, "source_sha256": item["core_sha256"], "python_flint": "0.9.0",
        "R813_proof_sha256": item["R813_proof_sha256"], "R813_method_sha256": item["R813_method_sha256"],
        "p": 41, "qY_count": 41, "full_coordinate_rows": ROWS,
        "S3_basis_dimension": DIM, "normal_basis_rank": FREE, "normal_basis_degrees": EPS,
        "original_M2_integer_scale": str(82**2), "original_S3_integer_scale": str(82**6),
        "original_V2_integer_scale": str(82**4), "original_D0_qY_multiplier": ["1", "82"],
        "producer_identities": {label: producer_identity(producers[label].spec) for label in sorted(LABELS)},
        "original_pencil": cert805["pencil_stage"], "original_S3_basis_index": cert805["S_basis_index"],
        "original_graded_free_basis": cert805["graded_free_basis_stage"],
        "original_coordinate_chart": cert806["coordinate_chart"],
        "actual_primitive_candidate": cert806["accepted_candidate"],
        "actual_candidate_definition": accepted["candidate_definition"],
        "actual_w0_original_M2_integer_coordinates": w0,
        "actual_sigma_integer_n": n, "reused_R806_modular_inverse": accepted["fixed_minor_inverse"],
        "actual_reused_prime": inverse["prime"], "coordinate_row_indices": I,
        "target_names": ["g", "h"], "reconstruct_every_digits": item["reconstruct_every_digits"],
        "Wronskian_generation": "D0(tau*s)-2*s*D0(tau); all tau*e_i are old V2[i]",
        "old_S3_selection_inverse_or_original_product_prefixes_recomputed": False,
        "actual_Mg_Mh_Gamma_or_height_computed": False,
    }
    matching_configuration(configuration, item)
    return {
        "old_R805_S3_basis_rows": DIM, "actual_original_M2_support": support,
        "old_R786_M2_rows": len(support), "old_R786_V2_rows": len(support),
        "all146_tau_e_i_aliases_verified_against_original_inventory": True,
        "original_alias_source_dictionary_includes_exact_producer_field": True,
        "qY_prefix_count_to_be_consumed": 41,
        "actual_R806_candidate_index": accepted["candidate_index"], "actual_sigma_integer_n": n,
        "actual_reused_prime": inverse["prime"],
        "actual_R806_full_coordinate_groups_consumed": False,
        "original_modular_inverse_read_without_recomputation": True,
        "all_selected_sizes_sha256_and_original_schemas_verified": True,
        "new_mathematical_arithmetic_executed_during_input_selection": False,
        "expected_core_configuration": configuration,
    }



def prepare_inputs(item, out):
    assert item["result"] == RESULT and item["p"] == 41
    assert item["producer_inputs_pending"] is False, "The real successful R806 producer is still pending."
    specs = item["retained_artifacts"]
    assert set(specs) == LABELS and all(isinstance(specs[label], dict) for label in LABELS)
    out.mkdir(parents=True, exist_ok=True)
    inputs = out.parent/"retained"
    present = [(inputs/label/"full-outputs-manifest.json").exists() for label in sorted(LABELS)]
    transferred = all(present)
    assert transferred or not any(present), "Partial unverified R813 retained input carrier"
    original_carrier = None
    if transferred:
        producers = {label: Producer(label, specs[label], [inputs/label]) for label in sorted(LABELS)}
    else:
        directory = out.parent/"downloaded-R806"
        download(specs["R806"], directory, require_complete=True)
        p806 = Producer("R806", specs["R806"], [directory])
        carrier = p806.bound(R806_INPUT_BUNDLE)
        assert sha(carrier) == specs["R806"]["input_bundle_sha256"]
        assert carrier.stat().st_size == specs["R806"]["input_bundle_bytes"]
        original_carrier = dict(file_spec(carrier), producer_identity=producer_identity(specs["R806"]))
        carried = out.parent/"R806-carried-original-inputs"
        extract_bundle(carrier, carried, specs, original_R806=True)
        producers = {"R806": p806}
        for label in ("R805", "R786"):
            producers[label] = Producer(label, specs[label], [carried/label])
    selection = select_original_inputs(producers, item)
    groups = []
    for label in sorted(LABELS):
        producer = producers[label]
        transfer(producer.selected, inputs/label)
        actual = {path.name for path in (inputs/label).iterdir() if path.is_file()}
        assert actual == set(producer.selected), (label, "unexpected retained input")
        groups.append({"label": label, "producer_identity": producer_identity(specs[label]),
                       "file_count": len(actual), "original_manifest_and_selected_file_hashes_verified": True})
    if not (out/INPUT_BUNDLE).exists():
        temporary = out/(INPUT_BUNDLE+".tmp")
        with tarfile.open(temporary, "w:gz") as archive:
            for path in sorted(inputs.rglob("*")):
                if path.is_file():
                    archive.add(path, arcname=path.relative_to(inputs).as_posix(), recursive=False)
        temporary.replace(out/INPUT_BUNDLE)
    save(out/"retained-inputs-receipt.json", {
        "result": RESULT, "groups": groups, "selection": selection,
        "all_inputs_from_same_core_active_R813_bundle": transferred,
        "fresh_original_producers_downloaded": [] if transferred else ["R806"],
        "original_R805_R786_carrier": original_carrier,
        "R805_R786_recovered_from_original_R806_carrier": not transferred,
        "old_independent_R805_R786_artifacts_required": False,
        "R806_full_multiplier_coordinate_groups_transferred": False,
        "input_bundle": file_spec(out/INPUT_BUNDLE), "old_arithmetic_recomputed": False,
        "new_mathematical_arithmetic_executed": False})
    return inputs


def restore_resume(item, out):
    previous = item.get("resume")
    if previous is None:
        return
    directory = out.parent/"downloaded-R813-continuation"
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
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert str(run["workflow_run_id"]) == str(previous["run_id"])
    assert initial["result"] == run["result"] == RESULT
    assert initial["core_sha256"] == item["core_sha256"]
    for key in ("result", "p", "core_sha256", "R813_proof_sha256", "R813_method_sha256",
                "qY_count", "target_names", "original_D0_qY_multiplier", "reconstruct_every_digits",
                "requested_stage"):
        assert initial["job"][key] == item[key], "Changed continuation identity: "+key
    for label in sorted(LABELS):
        same_producer(initial["job"]["retained_artifacts"][label], item["retained_artifacts"][label])
    bundle = bound(INPUT_BUNDLE)
    extract_bundle(bundle, out.parent/"retained", item["retained_artifacts"])
    shutil.copyfile(bundle, out/INPUT_BUNDLE)
    completed, current, canonical_tag = 0, 0, None
    for name in entries:
        if not (name.startswith("R813-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        source = bound(name)
        data = read(source)
        tag = data["configuration"]
        matching_configuration(tag, item)
        if canonical_tag is None:
            canonical_tag = tag
        assert tag == canonical_tag, "Mixed dynamic source identities in continuation"
        if name.endswith("-dixon-current.json.gz"):
            assert data["complete"] is False and data["complete_coordinates_claimed"] is False
            assert data["only_current_full_lift_vector_retained"] is True
            assert data["target_names"] == ["g", "h"]
            assert data["digits"] >= 1 and int(data["modulus"]) > 1
            current += 1
        else:
            assert data["complete"] is True
            completed += 1
        shutil.copyfile(source, out/name)
    assert current <= 1
    save(out/"resume-receipt.json", {"result": RESULT, "producer": previous,
        "same_exact_core_sha256": item["core_sha256"],
        "complete_checkpoint_files_copied": completed, "current_Dixon_checkpoint_files_copied": current,
        "all_three_original_producer_groups_restored": True,
        "completed_original_linear_inputs_weighted_products_and_exact_coordinates_preserved": True,
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
        "new_arithmetic": "only two weighted formal convolutions and two original S3 coordinates, full820",
        "old_S3_rank_inverse_or_unweighted_products_recomputed": False,
        "actual_Mg_Mh_Gamma_or_height_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41 and item["producer_inputs_pending"] is False
        assert sha(core) == item["core_sha256"] and sha(__file__) == item["wrapper_sha256"]
        assert sha(proof) == item["R813_proof_sha256"] and sha(method) == item["R813_method_sha256"]
        assert sha(S/"R786_public_exact_power5_short_basis.py") == item["download_helper_sha256"]
        assert sha(S/"p41_public_actions_recovery.py") == item["io_helper_sha256"]
        assert item["qY_count"] == 41 and item["target_names"] == ["g", "h"]
        assert item["original_D0_qY_multiplier"] == ["1", "82"]
        assert item["reconstruct_every_digits"] == 8
        assert item["requested_stage"] == "two_original_S3_Wronskian_inputs"
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
                error = "Budget reached; complete Wronskian stages and only the latest exact Dixon lift retained."
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
        "two_original_Wronskian_inputs_computed": complete,
        "old_S3_rank_inverse_or_unweighted_products_recomputed": False,
        "actual_Mg_Mh_or_Gamma_computed": False,
        "actual_original_y_derivative_or_function_DAG_computed": False,
        "actual_polar_divisors_eta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete, "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    assert item["producer_inputs_pending"] is False
    initial, run, receipt = (read(out/name) for name in
                            ("public-actions-input.json", "run-receipt.json", "core-receipt.json"))
    assert initial["job"] == item
    assert initial["result"] == run["result"] == receipt["result"] == RESULT
    assert initial["core_sha256"] == receipt["source_sha256"] == item["core_sha256"]
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert run["complete"] is True and run["process_exit_code"] == 0 and receipt["complete"] is True
    assert run["source_commit"] == initial["source_commit"]
    assert run["core_receipt_sha256"] == sha(out/"core-receipt.json")
    assert receipt["certificate_sha256"] == sha(out/FINAL)
    cert = read(out/FINAL)
    assert cert["result"] == RESULT and cert["complete"] is True and cert["p"] == 41
    tag = cert["configuration"]
    matching_configuration(tag, item)
    retained = read(out/"retained-inputs-receipt.json")
    assert retained["result"] == RESULT
    assert retained["selection"]["expected_core_configuration"] == tag
    assert retained["selection"]["all146_tau_e_i_aliases_verified_against_original_inventory"] is True
    assert retained["selection"]["all_selected_sizes_sha256_and_original_schemas_verified"] is True
    assert retained["selection"]["new_mathematical_arithmetic_executed_during_input_selection"] is False
    assert file_spec(out/INPUT_BUNDLE) == retained["input_bundle"]
    assert cert["completed_scope"] == receipt["completed_scope"] == "two_original_S3_Wronskian_inputs"
    assert cert["target_names"] == ["g", "h"] and cert["actual_rational_RHS_columns"] == 2
    assert cert["S3_basis_dimension"] == DIM and cert["qY_count"] == 41 and cert["full_coordinate_rows"] == ROWS
    assert cert["normal_basis_rank"] == FREE and cert["normal_basis_degrees"] == EPS
    assert cert["regular_degree_bound"] == 3
    for key in ("actual_sigma_integer_n", "actual_w0_original_M2_integer_coordinates", "actual_reused_prime"):
        assert cert[key] == tag[key]
    assert cert["original_D0_qY_multiplier"] == ["1", "82"]
    assert cert["original_M2_integer_scale"] == str(82**2)
    assert cert["original_V2_integer_scale"] == str(82**4)
    assert cert["original_S3_integer_scale"] == str(82**6)
    for key in ("all820_original_coordinates_verified_for_both_targets", "both_original_normal_vectors_actually_nonzero",
                "original_1_over82_and_all_integer_scales_preserved"):
        assert cert[key] is True
    for key in ("old_S3_rank_inverse_or_unweighted_products_recomputed", "actual_Mg_Mh_or_Gamma_computed",
                "actual_original_y_derivative_or_function_DAG_computed", "actual_polar_divisors_eta_or_height_computed"):
        assert cert[key] is False
    manifest_spec = cert["stage_manifest"]
    assert file_spec(out/manifest_spec["file"]) == manifest_spec
    manifest = read(out/manifest_spec["file"])
    assert manifest["complete"] is True and manifest["configuration"] == tag
    stages = {row["file"]: row for row in manifest["files"]}
    assert len(stages) == len(manifest["files"])
    actual = {path.name for path in out.glob("R813-*.json.gz")
              if not path.name.startswith("R813-stage-manifest-")}
    assert actual == set(stages)
    assert not list(out.glob("R813-*-dixon-current.json.gz"))
    for name, spec in stages.items():
        assert file_spec(out/name) == spec
        value = read(out/name)
        assert value["complete"] is True and value["configuration"] == tag
    def stage(spec):
        assert plain_spec(spec) == stages[spec["file"]]
        return read(out/spec["file"])
    chart = stage(cert["source_coordinate_interface"])
    assert chart["coordinate_row_indices"] == tag["coordinate_row_indices"]
    assert chart["S3_dimension"] == DIM and chart["full_coordinate_rows"] == ROWS
    assert chart["original_S3_integer_scale"] == str(82**6)
    assert chart["original_R805_S3_basis_index"] == tag["original_S3_basis_index"]
    assert chart["original_R806_coordinate_chart"] == tag["original_coordinate_chart"]
    assert chart["reused_R806_modular_inverse"] == tag["reused_R806_modular_inverse"]
    assert chart["S3_row_to_polynomial_coefficient"] == S_mapping()
    coordinates = stage(cert["exact_coordinate_stage"])
    assert coordinates["target_names"] == ["g", "h"] and coordinates["column_indices"] == [0, 1]
    assert coordinates["S3_basis_dimension"] == DIM and coordinates["full_coordinate_rows"] == ROWS
    assert coordinates["normal_basis_rank"] == FREE
    assert coordinates["all820_original_coordinates_verified"] is True
    assert coordinates["both_original_Wronskians_actually_nonzero"] is True
    assert coordinates["original_1_over82_and_all_integer_scales_preserved"] is True
    assert coordinates["rational_reconstruction_used_uniform_strict_rectangular_bound"] is True
    assert coordinates["source_coordinate_interface"] == cert["source_coordinate_interface"]
    assert coordinates["reused_R806_modular_inverse"] == tag["reused_R806_modular_inverse"]
    assert coordinates["actual_prime"] == tag["actual_reused_prime"]
    assert coordinates["actual_Dixon_digits"] >= 1
    assert len(coordinates["coordinate_numerators"]) == DIM
    assert all(len(row) == 2 for row in coordinates["coordinate_numerators"])
    assert len(coordinates["column_denominators"]) == 2
    assert all(int(denominator) > 0 for denominator in coordinates["column_denominators"])
    assert len(coordinates["original_target_rational_scales"]) == 2
    assert len(coordinates["source_target_prefixes"]) == 2
    for column, target in enumerate(("g", "h")):
        prefix = stage(coordinates["source_target_prefixes"][column])
        assert prefix["target"] == target and prefix["qY_count"] == 41
        assert prefix["full_coordinate_rows"] == ROWS
        assert len(prefix["primitive_integer_v_t_coordinates"]) == ROWS
        assert prefix["original_rational_scale"] == coordinates["original_target_rational_scales"][column]
        assert len(prefix["original_rational_scale"]) == 2 and int(prefix["original_rational_scale"][1]) > 0
        assert prefix["original_D0_qY_multiplier"] == ["1", "82"]
        assert prefix["source_M2_scale"] == str(82**2)
        assert prefix["source_old_V2_scale"] == str(82**4)
        assert prefix["coordinate_basis_S3_scale"] == str(82**6)
        assert prefix["scale_82_not_adjusted_by_weight_guess"] is True
        assert prefix["ordinary_V3_membership_by_original_Wronskian_proof"] is True
        assert prefix["qY_xi_and_v_t_representations_exactly_agree"] is True
        assert prefix["constant_cusp_coefficient_exactly_zero"] is True
        assert prefix["actual_full_prefix_nonzero"] is True
        linear = stage(prefix["original_linear_form_and_old_product"])
        weighted = stage(prefix["new_weighted_formal_product"])
        assert linear["target"] == weighted["target"] == target
        assert linear["all_tau_e_i_products_read_from_original_V2_aliases"] is True
        assert linear["old_product_coefficients_recomputed"] is False
        assert weighted["one_new_weighted_convolution_per_target"] is True
        assert weighted["source_original_s_and_tau_s"] == prefix["original_linear_form_and_old_product"]
        assert weighted["this_formal_product_alone_claimed_to_be_a_modular_section"] is False
        assert weighted["old_unweighted_tau_s_product_recomputed"] is False
    interface = stage(cert["normal_vector_interface"])
    assert interface["target_column_indices"] == {"g": 0, "h": 1}
    assert interface["source_exact_S3_coordinates"] == cert["exact_coordinate_stage"]
    assert interface["source_coordinate_interface"] == cert["source_coordinate_interface"]
    assert interface["S3_row_to_polynomial_coefficient"] == S_mapping()
    assert interface["normal_basis_rank"] == FREE and interface["normal_basis_degrees"] == EPS
    assert interface["regular_degree_bound"] == 3
    assert interface["actual_R806_primitive_candidate"] == tag["actual_primitive_candidate"]
    assert interface["actual_R806_polynomial_multiplier_index"] == cert["source_actual_R806_primitive_multiplier"]
    assert interface["all820_original_coordinates_verified"] is True
    assert interface["original_1_over82_and_all_integer_scales_preserved"] is True
    assert interface["original_Mw_coordinate_values_consumed"] is False
    assert interface["actual_Mg_Mh_or_Gamma_computed"] is False
    assert interface["actual_original_y_derivative_or_function_DAG_computed"] is False
    assert interface["actual_polar_divisors_eta_or_height_computed"] is False
    output_inventory = read(out/"full-outputs-manifest.json")
    assert output_inventory["result"] == RESULT
    files = {row["file"]: row for row in output_inventory["files"]}
    assert len(files) == len(output_inventory["files"])
    for name, row in files.items():
        assert file_spec(out/name) == plain_spec(row)
    assert FINAL in files and INPUT_BUNDLE in files and manifest_spec["file"] in files
    print(json.dumps({"result": RESULT, "verified": True,
        "actual_rational_RHS_columns": 2, "full_coordinate_rows": ROWS,
        "actual_Mg_Mh_or_Gamma_computed": False,
        "actual_polar_divisors_eta_or_height_computed": False}), flush=True)
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
