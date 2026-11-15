#!/usr/bin/env python3
"""R803 public runner: old source-bound prefixes, five new mixed forms, finite RHS."""
import argparse
import datetime as dt
import hashlib
import itertools
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
REQUEST = TOPIC/"notes/R803-public-original-M6-mixed-Hodge-ratios-request.json"
RESULT = "R803-original-M6-mixed-Hodge-ratios"
FINAL = "p41-original-M6-mixed-Hodge-ratios-certificate.json"
INPUT_BUNDLE = "R803-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
LABELS = {"R774", "R775", "R786", "R794", "R759"}
PRODUCER_META = ("full-outputs-manifest.json", "run-receipt.json",
                 "core-receipt.json", "public-actions-input.json")
META = {"public-actions-input.json", "retained-inputs-receipt.json",
        "resume-receipt.json", "run-receipt.json", "core-receipt.json"}
M6 = "R775-basis-M6-complete.json.gz"
M6_SHA = "70ff7536b50bf99ffb422b7c17dd320b535738fcfcc562fd1597eebcb7a0b299"
SCALARS = "R774-original-L-cubic-scalars.json.gz"
SCALARS_SHA = "b5b1232fa0585e6437d0e8d5f92b81efe672e91ed417bce7f6bc66c6456d596e"
MODULE = "R794-original-CM-module-and-finite-norm-candidates.json.gz"
MODULE_SHA = "c7dbe30e9cc1d63032f8428cc47e6539ba328c3e35cd8e9186c9ec5dc95c47fc"
SELECTED = "R794-selected-original-low-degree-eta-basis.json.gz"
SELECTED_SHA = "5b96f623e1f43d834a7db21064ff2cb101284b9a4038e5434eb291b6e73f6e0f"
MAPS = "R759-original-integral-maps-and-bounded-recovery-input.json.gz"
MAPS_SHA = "037b56d016d502408173319d76a3067a65dd50250c31bc2225c0fca598396ecc"
H3_INPUTS = {
    "R774-exact-H3-qY-0001-0032.json.gz": "4ded35d80590f86802c55c3cb73e04e5e38e834823d47b21dc5b0bbaaa6aa612",
    "R774-exact-H3-qY-0033-0064.json.gz": "80a7ed979e5a4f283082211891af8e6e4be0bfc098c34106bffb9881620d5708"}


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


def matching_configuration(tag, item):
    assert tag["result"] == RESULT and tag["source_sha256"] == item["core_sha256"]
    assert tag["python_flint"] == "0.9.0" and tag["p"] == 41
    for key in ("R803_proof_sha256", "R803_method_sha256", "retained_artifacts",
                "qY_count", "M6_dimension", "mixed_indices", "coordinate_indices",
                "auxiliary_prime_start", "reconstruct_every_digits"):
        assert tag[key] == item[key]
    assert tag["qY_count"] == 42 and tag["M6_dimension"] == 694 and tag["full_coordinate_rows"] == 1680
    assert tag["mixed_indices"] == [1, 2, 3, 4, 5] and tag["coordinate_indices"] == [0, 1, 2, 3, 4, 5]
    assert tag["basis_integer_scale"] == str(82**6) and tag["Hodge_common_denominator"] == 1722
    assert tag["coordinate_basis"] == "b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b"
    assert tag["qY_parameter"] == "exp(2*pi*i*tau/82); original reference cusp"
    for key in ("old_U0_Hodge_monomials_Hom_periods_or_ordinary_basis_recomputed",
                "second_c1_phase_or_real_descent_isogeny_applied", "characteristic_zero_inverse_matrix_formed"):
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


def allowed_group_name(label, spec, name):
    if name in set(PRODUCER_META)|set(spec["files"]):
        return True
    if label == "R774":
        match = re.fullmatch(r"R774-cubic-monomial-(\d{2})\.json\.gz", name)
        return bool(match and 0 <= int(match[1]) < 56)
    if label == "R786":
        match = re.fullmatch(r"R786-exact-power-([13])-row-(\d{4})\.json\.gz", name)
        return bool(match and ((match[1] == "3" and 0 <= int(match[2]) < 690) or
                              (match[1] == "1" and int(match[2]) in (0, 73))))
    return False


def extract_bundle(bundle, target, specs, parent=False):
    """Regular two-level data only; parent R791 data is deliberately not transferred."""
    target.mkdir(parents=True, exist_ok=True)
    seen, count = set(), 0
    with tarfile.open(bundle, "r:gz") as archive:
        for member in archive:
            relative = Path(member.name)
            assert member.isfile() and not relative.is_absolute() and ".." not in relative.parts
            assert len(relative.parts) == 2
            group, name = relative.parts
            assert group in ({"R759", "R791"} if parent else LABELS)
            assert str(relative) not in seen
            seen.add(str(relative))
            if parent and group == "R791":
                continue
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


def select_original_inputs(producers):
    """Read/hash/schema checks only; no old or new field arithmetic is executed."""
    p774, p775, p786, p794, p759 = (producers[label] for label in ("R774", "R775", "R786", "R794", "R759"))
    same_producer(p794.initial["job"]["retained_artifacts"]["R759"], p759.spec)
    same_producer(p794.tag["retained_artifacts"]["R759"], p759.spec)
    for name in (MAPS, p759.spec["certificate_name"]):
        assert p774.tag["retained_input_sha256"][name] == p759.entries[name]["sha256"]
    assert p774.tag["H_normalization"] == "H=alpha*F/1722; alpha^3=4"
    assert p774.tag["cube_normalization"] == "H^3=4*F^3/1722^3"
    assert p774.tag["c1_phase_applied_a_second_time"] is False
    for key in ("qY_constant_coefficient_zero", "exact_H_cubed_nonzero", "no_Neron_Manin_or_KS_scale_changed"):
        assert p774.certificate[key] is True
    witness = p774.cert_stage(SCALARS, SCALARS_SHA)
    triples = [list(row) for row in itertools.combinations_with_replacement(range(6), 3)]
    assert len(triples) == 56 and witness["triples"] == triples
    assert len(witness["rational_row_scales"]) == 14
    assert len(witness["primitive_integer_matrix"]) == 14
    assert all(len(row) == 112 for row in witness["primitive_integer_matrix"])
    maps = p759.cert_stage(MAPS, MAPS_SHA)
    assert maps["selected_index"] == 4 and maps["selected_degree"] == "1206"
    assert maps["Z_basis_rank"] == 12 and maps["O_K_rank"] == 6 and maps["c1_coset"] == 4424
    all_maps = maps["all_twelve_integral_map_differential_vectors_in_original_omega_basis"]
    assert len(all_maps) == 12 and all(len(row) == 6 for row in all_maps)
    assert all_maps[4] == witness["selected_original_v_in_omega_basis"]
    for row in all_maps:
        for pair in row:
            assert len(pair) == 2
            for polynomial in pair:
                assert len(polynomial["numerator"]) <= 7 and int(polynomial["denominator"]) > 0
    module = p794.cert_stage(MODULE, MODULE_SHA)
    assert module["cyclic_basis"] == "T^k*f4, k=0..11; original R791 column action"
    assert module["Phi21_ascending"] == ["1", "-1", "0", "1", "-1", "0", "1", "0", "-1", "1", "0", "-1", "1"]
    matrix = module["cyclic_basis_matrix"]
    assert len(matrix) == 12 and all(len(row) == 12 for row in matrix)
    assert all(value[1] == "1" for row in matrix for value in row)
    assert [row[0] for row in matrix] == [["1" if i == 4 else "0", "1"] for i in range(12)]
    selected = p794.cert_stage(SELECTED, SELECTED_SHA)
    assert selected["selected_candidate_indices"] == [0, 3, 1, 21, 15]
    assert selected["original_kappa_e_R_q_c0_c1_preserved"] is True and len(selected["selected_maps"]) == 5
    for row in selected["selected_maps"]:
        assert len(row["a_in_Q_T_mod_Phi21"]) == 12
        assert all(value[1] == "1" for value in row["a_in_Q_T_mod_Phi21"])
    for index, triple in enumerate(triples):
        data = p774.cert_stage("R774-cubic-monomial-"+str(index).zfill(2)+".json.gz")
        assert data["indices"] == triple and data["G_exponent_range_exclusive"] == [0, 820]
        assert data["xi_basis_degree"] == 40
        for key in ("real_coefficients_flat_qY_xi", "s_coefficients_flat_qY_xi"):
            assert len(data[key]) == 32800
    covered = {0}
    for name, digest in H3_INPUTS.items():
        data = p774.cert_stage(name, digest)
        first, stop = data["first_exponent"], data["last_exponent_exclusive"]
        assert (first, stop) in ((1, 33), (33, 65))
        assert data["rational_row_scale_stage_sha256"] == SCALARS_SHA
        assert data["coefficient_layout"] == "14 rows (b^i,s*b^i), columns (qY exponent,xi^r), r0..39"
        assert len(data["integer_numerators"]) == 14
        assert all(len(row) == (stop-first)*40 for row in data["integer_numerators"])
        assert not covered.intersection(range(first, min(stop, 42)))
        covered.update(range(first, min(stop, 42)))
    assert covered == set(range(42))
    m6 = p775.cert_stage(M6, M6_SHA)
    assert m6["rank"] == len(m6["basis"]) == 694
    assert m6["characteristic_zero_independence_certified_by_unit_reduction"] is True
    assert p775.tag["prime"] == 739 and p775.tag["xi41_mod_ell"] == 538
    for index, row in enumerate(m6["basis"][:690]):
        assert row["recipe"] == {"kind": "power_basis", "power": 3, "index": index}
    assert [row["recipe"] for row in m6["basis"][690:]] == [
        {"kind": "elliptic_layer_product", "factor": "E4", "power": 1, "index": 0},
        {"kind": "elliptic_layer_product", "factor": "E4", "power": 1, "index": 73},
        {"kind": "level_one", "name": "E6"}, {"kind": "level_one", "name": "eta12"}]
    stages775 = {row["file"]: row for row in p775.certificate["stages"]}
    for name in ("R775-basis-M2.json.gz", "R775-basis-power-3.json.gz"):
        assert p786.tag["R775_completed_prefix_producer"]["files"][name] == stages775[name]["sha256"]
    inventory = p786.inventory("stages_manifest")
    needed = [(3, index) for index in range(690)]+[(1, 0), (1, 73)]
    for power, index in needed:
        name = "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"
        data = p786.stage(inventory[name])
        assert data["weight"] == 2*power and data["bound_qY"] == 128
        assert data["integer_scale"] == str(82**(2*power))
        assert data["original_R775_finite_coefficients_verified"] is True
        assert len(data["integer_qY_xi_coefficients"]) == 129
        assert all(len(row) == 40 for row in data["integer_qY_xi_coefficients"])
    for producer in producers.values():
        assert all(name in producer.selected for name in producer.spec["files"]), (producer.label, "unused pinned input")
    return {"old_power3_rows": 690, "old_M2_indices": [0, 73],
        "old_Hodge_monomials": 56, "old_H3_blocks": list(H3_INPUTS),
        "old_H3_coverage_consumed": [0, 42], "old_G_triple_coverage_consumed": [0, 41],
        "old_integer_cyclic_Hom_columns": [1, 2, 3, 4, 5],
        "all_sizes_sha256_original_schemas_and_parent_identities_verified": True,
        "old_or_new_mathematical_arithmetic_executed_during_input_selection": False}


def prepare_inputs(item, out):
    specs = item["retained_artifacts"]
    assert set(specs) == LABELS
    inputs = out.parent/"retained"
    present = [(inputs/label/"full-outputs-manifest.json").exists() for label in LABELS]
    transferred = all(present)
    assert transferred or not any(present), "Partial unverified R803 input carrier"
    if transferred:
        producers = {label: Producer(label, specs[label], [inputs/label]) for label in sorted(LABELS)}
    else:
        downloaded = {}
        for label in ("R774", "R775", "R786", "R794"):
            directory = out.parent/("downloaded-"+label)
            download(specs[label], directory, require_complete=True)
            downloaded[label] = directory
        producers = {label: Producer(label, specs[label], [directory]) for label, directory in downloaded.items()}
        parent = producers["R794"]
        same_producer(parent.initial["job"]["retained_artifacts"]["R759"], specs["R759"])
        same_producer(parent.tag["retained_artifacts"]["R759"], specs["R759"])
        bundle = parent.bound("R794-retained-producer-inputs.tar.gz")
        carried = out.parent/"R794-carried-original-inputs"
        extract_bundle(bundle, carried, specs, parent=True)
        producers["R759"] = Producer("R759", specs["R759"], [carried/"R759"])
    selection = select_original_inputs(producers)
    groups = []
    for label in sorted(LABELS):
        producer = producers[label]
        transfer(producer.selected, inputs/label)
        actual = {path.name for path in (inputs/label).iterdir() if path.is_file()}
        assert actual == set(producer.selected), (label, "unexpected retained input")
        groups.append({"label": label, "producer": specs[label], "file_count": len(actual),
                       "original_manifest_and_all_selected_files_verified": True})
    if not (out/INPUT_BUNDLE).exists():
        with tarfile.open(out/INPUT_BUNDLE, "w:gz") as archive:
            for path in sorted(inputs.rglob("*")):
                if path.is_file():
                    archive.add(path, arcname=path.relative_to(inputs).as_posix(), recursive=False)
    save(out/"retained-inputs-receipt.json", {
        "result": RESULT, "groups": groups, "selection": selection,
        "all_inputs_from_same_core_active_R803_bundle": transferred,
        "fresh_original_producers_downloaded": [] if transferred else ["R774", "R775", "R786", "R794"],
        "R759_original_Hom_differentials_transferred_from_bound_R794_parent_bundle": not transferred,
        "input_bundle": file_spec(out/INPUT_BUNDLE),
        "unused_ordinary_high_powers_or_R791_R797_data_in_this_active_bundle": False,
        "old_arithmetic_recomputed": False})
    return inputs


def restore_resume(item, out):
    previous = item.get("resume")
    if previous is None:
        return
    directory = out.parent/"downloaded-R803-continuation"
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
    for key in ("result", "p", "core_sha256", "R803_proof_sha256", "R803_method_sha256",
                "retained_artifacts", "qY_count", "M6_dimension", "mixed_indices", "coordinate_indices",
                "auxiliary_prime_start", "reconstruct_every_digits"):
        assert initial["job"][key] == item[key], "Changed continuation identity: "+key
    bundle = bound(INPUT_BUNDLE)
    extract_bundle(bundle, out.parent/"retained", item["retained_artifacts"])
    shutil.copyfile(bundle, out/INPUT_BUNDLE)
    count = 0
    for name in entries:
        if not (name.startswith("R803-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        source = bound(name)
        data = read(source)
        assert data["complete"] is True
        matching_configuration(data["configuration"], item)
        shutil.copyfile(source, out/name)
        count += 1
    save(out/"resume-receipt.json", {
        "result": RESULT, "producer": previous, "same_exact_core_sha256": item["core_sha256"],
        "complete_checkpoint_files_copied": count, "five_group_original_input_bundle_restored": True,
        "completed_mixed_prefixes_and_exact_coordinate_groups_preserved": True,
        "latest_Dixon_lift_and_exact_residual_preserved": True,
        "completed_mathematical_stages_recomputed": False})


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
        "new_arithmetic": "four M6 rows q0..41, five mixed Hodge prefixes and six groups of14 exact M6 RHS",
        "old_U0_Hodge_monomials_Hom_periods_or_ordinary_basis_recomputed": False,
        "actual_original_y_functions_polar_divisors_beta_eta_or_height_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41 and item["producer_inputs_pending"] is False
        assert sha(core) == item["core_sha256"] and sha(__file__) == item["wrapper_sha256"]
        assert sha(proof) == item["R803_proof_sha256"] and sha(method) == item["R803_method_sha256"]
        assert sha(S/"R786_public_exact_power5_short_basis.py") == item["download_helper_sha256"]
        assert sha(S/"p41_public_actions_recovery.py") == item["io_helper_sha256"]
        assert item["qY_count"] == 42 and item["M6_dimension"] == 694
        assert item["mixed_indices"] == [1, 2, 3, 4, 5] and item["coordinate_indices"] == [0, 1, 2, 3, 4, 5]
        assert item["auxiliary_prime_start"] == 1000000007 and item["reconstruct_every_digits"] == 8
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
                error = "Budget reached; completed mixed stages and current exact Dixon residual retained for continuation."
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
        "actual_five_original_mixed_differential_ratios_computed": complete,
        "old_U0_Hodge_monomials_Hom_periods_or_ordinary_basis_recomputed": False,
        "actual_original_y_functions_polar_divisors_beta_eta_or_height_computed": False,
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
    assert cert["M6_dimension"] == 694 and cert["qY_count"] == 42
    assert cert["xi_coordinate_count"] == 40 and cert["full_original_coordinate_rows"] == 1680
    assert cert["basis_integer_scale"] == str(82**6)
    assert cert["new_basis_row_indices"] == [690, 691, 692, 693]
    assert cert["old_ordinary_power3_rows_reused"] == 690
    assert cert["new_mixed_Hodge_products"] == [1, 2, 3, 4, 5]
    assert cert["exact_coordinate_groups"] == [0, 1, 2, 3, 4, 5]
    for key in ("all84_rational_RHS_columns_verified_in_all1680_original_rows",
                "all_original_1722_and_82power6_scales_preserved", "original_b_and_s_coordinate_basis_preserved",
                "five_original_mixed_differential_ratios_computed"):
        assert cert[key] is True
    for key in ("old_U0_Hodge_monomials_Hom_periods_or_ordinary_basis_recomputed",
                "characteristic_zero_inverse_matrix_formed",
                "actual_original_y_functions_polar_divisors_beta_eta_or_height_computed"):
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
        assert name.startswith("R803-") and name.endswith(".json.gz")
        data = stage(spec)
        assert not name.endswith("-dixon-current.json.gz"), "Finished job still contains an unresolved RHS lift."
        headers[name] = data
    for key in ("basis_index", "ratio_interface"):
        assert plain_spec(cert[key]) == entries[cert[key]["file"]]
    basis = headers[cert["basis_index"]["file"]]
    assert basis["dimension"] == 694 and basis["qY_count"] == 42 and basis["xi_coordinate_count"] == 40
    assert basis["integer_scale"] == str(82**6) and basis["old_power3_rows_read"] == 690
    assert basis["new_short_rows"] == [690, 691, 692, 693]
    assert basis["original_basis_order_and_recipes_preserved"] is True
    assert basis["old_coefficients_recomputed"] is False and len(basis["basis_rows"]) == 694
    inputs = out.parent/"retained"
    producers = {label: Producer(label, item["retained_artifacts"][label], [inputs/label]) for label in sorted(LABELS)}

    def source(spec):
        label = spec["producer"]
        if label == "R803":
            assert plain_spec(spec) == entries[spec["file"]]
        else:
            producer = producers[label]
            producer.bound(spec["file"], spec)

    source(basis["original_M6_stage"])
    for index, row in enumerate(basis["basis_rows"]):
        assert row["index"] == index and row["source_prefix_read"] == [0, 42]
        assert row["old_coefficients_recomputed"] is False
        source(row["source"])
        if index < 690:
            assert row["recipe"] == {"kind": "power_basis", "power": 3, "index": index}
            assert row["source"]["producer"] == "R786"
            assert row["source"]["file"] == "R786-exact-power-3-row-"+str(index).zfill(4)+".json.gz"
        else:
            data = headers[row["source"]["file"]]
            assert data["index"] == index and data["recipe"] == row["recipe"]
            assert data["weight"] == 6 and data["integer_scale"] == str(82**6) and data["bound_qY"] == 41
            assert data["new_complete_short_row_verified_against_original_M6_mod739"] is True
            assert data["old_M2_or_power3_prefix_recomputed"] is False
            assert data["coefficients_after_qY41_generated"] is False
            assert len(data["integer_qY_xi_coefficients"]) == 42
            assert all(len(values) == 40 for values in data["integer_qY_xi_coefficients"])
            for old_source in data["original_factor_sources"]:
                source(old_source)
    accepted = [name for name in entries if re.fullmatch(r"R803-prime-\d+-short-minor\.json\.gz", name)]
    assert len(accepted) == 1
    minor = headers[accepted[0]]
    assert minor["full_rows"] == 1680 and minor["columns"] == 694
    assert minor["basis_index_sha256"] == cert["basis_index"]["sha256"]
    assert minor["prime_proved"] is True and minor["modular_inverse_identity_verified"] is True
    assert minor["characteristic_zero_basis_independence_certified"] is True
    assert minor["characteristic_zero_inverse_matrix_formed"] is False
    assert len(minor["coordinate_row_indices"]) == 694
    assert minor["coordinate_row_indices"] == sorted(set(minor["coordinate_row_indices"]))
    assert all(0 <= i < 1680 for i in minor["coordinate_row_indices"])
    assert minor["selected_basis_column_indices"] == list(range(694))
    assert minor["actual_determinant_mod_prime"] % minor["prime"]
    assert len(minor["inverse_mod_prime"]) == 694 and all(len(row) == 694 for row in minor["inverse_mod_prime"])
    assert cert["actual_nonzero_short_minor"] == {
        "prime": minor["prime"], "rows": 694, "columns": 694,
        "coordinate_row_indices": minor["coordinate_row_indices"],
        "determinant_mod_prime": minor["actual_determinant_mod_prime"]}
    for j in range(1, 6):
        scalar = headers["R803-mixed-original-Hodge-scalars-j"+str(j)+".json.gz"]
        assert scalar["j"] == j and scalar["pure_U0_scalars_recomputed"] is False
        assert scalar["old_Hom_Galois_columns_or_periods_recomputed"] is False
        assert scalar["extra_rho_j_or_c1_phase_applied"] is False
        assert len(scalar["primitive_integer_matrix"]) == 14
        assert all(len(row) == 112 for row in scalar["primitive_integer_matrix"])
        assert len(scalar["rational_row_scales"]) == 14
        source(scalar["source_cyclic_stage"])
        source(scalar["source_original_Hom_differentials"])
        mixed = headers["R803-new-mixed-Hodge-prefix-j"+str(j)+".json.gz"]
        assert mixed["j"] == j and mixed["first_exponent"] == 0 and mixed["last_exponent_exclusive"] == 42
        assert mixed["xi_coordinate_count"] == 40 and mixed["L_coordinate_count"] == 14
        assert mixed["old_monomial_exponents_read"] == [0, 41]
        assert mixed["qY_shift_applied_exactly_once"] is True
        assert mixed["old_U0_or_shared_monomial_coefficients_recomputed"] is False
        assert mixed["coefficients_after_qY41_generated"] is False
        assert mixed["rational_row_scales"] == scalar["rational_row_scales"]
        assert len(mixed["integer_numerators"]) == 14 and all(len(row) == 1680 for row in mixed["integer_numerators"])
        assert plain_spec(mixed["mixed_scalar_stage"]) == entries[mixed["mixed_scalar_stage"]["file"]]
        assert len(mixed["source_old_monomials"]) == 56
        for old_source in mixed["source_old_monomials"]:
            source(old_source)
    assert set(cert["coordinate_stages"]) == {str(j) for j in range(6)}
    for j in range(6):
        spec = cert["coordinate_stages"][str(j)]
        assert plain_spec(spec) == entries[spec["file"]]
        data = headers[spec["file"]]
        assert data["j"] == j and data["basis_dimension"] == 694 and data["basis_integer_scale"] == str(82**6)
        assert data["original_M6_basis_index"] == cert["basis_index"]
        assert data["coefficient_field_basis"] == cert["configuration"]["coordinate_basis"]
        assert data["all1680_original_coordinates_verified"] is True
        assert data["rational_reconstruction_used_uniform_strict_rectangular_bound"] is True
        assert data["old_U0_recomputed"] is False and data["characteristic_zero_inverse_matrix_formed"] is False
        assert data["actual_prime"] == minor["prime"] and data["actual_Dixon_digits"] >= 1
        assert data["minor_stage"] == entries[accepted[0]]
        assert fingerprint(data["source_rhs"]) == data["source_rhs_binding_sha256"]
        assert data["source_rhs"]["j"] == j and len(data["source_rhs"]["rational_row_scales"]) == 14
        for old_source in data["source_rhs"]["original_sources"]:
            source(old_source)
        for key in ("coefficients_in_integer_scaled_original_M6_basis", "coefficients_in_unscaled_original_M6_basis"):
            rows = data[key]
            assert len(rows) == 694 and all(len(row) == 14 for row in rows)
            assert all(len(pair) == 2 and int(pair[1]) > 0 for row in rows for pair in row)
    ratios = headers[cert["ratio_interface"]["file"]]
    assert ratios["denominator_coordinate_index"] == 0 and ratios["numerator_coordinate_indices"] == [1, 2, 3, 4, 5]
    assert ratios["coordinate_stages"] == cert["coordinate_stages"]
    assert ratios["U0_nonzero_from_original_R774_certificate"] is True
    assert ratios["all_six_exact_forms_identified_by_full42_term_injective_prefix"] is True
    assert ratios["five_original_mixed_differential_ratios_computed"] is True
    assert ratios["actual_original_y_functions_polar_divisors_beta_eta_or_height_computed"] is False
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
