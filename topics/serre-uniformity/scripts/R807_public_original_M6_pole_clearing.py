#!/usr/bin/env python3
"""R807 public runner: one exact V4 block and four source-bound M6 clearing rows."""
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
REQUEST = TOPIC/"notes/R807-public-original-M6-pole-clearing-request.json"
RESULT = "R807-original-M6-pole-clearing"
FINAL = "p41-original-M6-pole-clearing-certificate.json"
INPUT_BUNDLE = "R807-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
LABELS = {"R775", "R786", "R805"}
PRODUCER_META = ("full-outputs-manifest.json", "run-receipt.json",
                 "core-receipt.json", "public-actions-input.json")
META = {"public-actions-input.json", "retained-inputs-receipt.json",
        "resume-receipt.json", "run-receipt.json", "core-receipt.json"}
M6 = "R775-basis-M6-complete.json.gz"
M6_SHA = "70ff7536b50bf99ffb422b7c17dd320b535738fcfcc562fd1597eebcb7a0b299"
P2 = "R775-basis-power-2.json.gz"
P2_SHA = "734a61e967c51ba3c9cd93eaff1a81fba165600110abb941dfdbbeed41b6ebe4"
M2_INDICES = (0, 1, 2, 3, 4, 73)
P2_INDICES = (0, 1, 2, 3, 4, 73, 218, 345)
OLD_PAIR_ALIASES = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3,
                    (0, 4): 4, (0, 73): 73, (1, 73): 218, (2, 73): 345}
NEW_PAIRS = {
    "R805-new-monomial-003-073.json.gz": ([3, 73], 9155,
        "4ecfd61fd3e47d49231075da11bcce17e1e4e577d8c4266d44e3e2b2267d45a4"),
    "R805-new-monomial-004-073.json.gz": ([4, 73], 9163,
        "e94730bd1cc3ddad1e0c6ae3c2710c1ac0419a5097629d8631d2509ab65eb450")}
M6_RECIPES = {
    690: {"factor": "E4", "index": 0, "kind": "elliptic_layer_product", "power": 1},
    691: {"factor": "E4", "index": 73, "kind": "elliptic_layer_product", "power": 1},
    692: {"kind": "level_one", "name": "E6"},
    693: {"kind": "level_one", "name": "eta12"}}
GROUP_COUNTS = {"R775": 7, "R786": 982, "R805": 8}


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
        assert left["files"][name] == right["files"][name], ("shared producer file", name)


def matching_configuration(tag, item):
    assert tag["result"] == RESULT and tag["source_sha256"] == item["core_sha256"]
    assert tag["python_flint"] == "0.9.0" and tag["p"] == 41
    for key in ("R805_proof_sha256", "R807_method_sha256", "retained_artifacts",
                "qY_count", "V4_dimension", "auxiliary_prime_start", "reconstruct_every_digits"):
        assert tag[key] == item[key]
    assert tag["qY_count"] == 55 and tag["V4_dimension"] == 962
    assert tag["full_real_coordinate_rows"] == 1100
    assert tag["basis_integer_scale"] == str(82**8) and tag["original_M2_scale"] == str(82**2)
    assert tag["projection_original_M2_indices"] == [0, 1, 2, 3, 4]
    assert tag["extra_M6_indices"] == [690, 691, 692, 693]
    assert tag["real_coordinate_order"] == "20*n+r; v=xi^-10*qY; t=xi+xi^-1"
    assert tag["existing_R805_pair_prefix_count"] == 41 and tag["new_pair_tail_interval"] == [41, 55]
    assert tag["original_V4_basis_order_preserved"] is True
    for key in ("old_M2_V2_V4_prefixes_recomputed", "existing_R805_pair_prefixes_recomputed",
                "R803_mixed_coordinates_consumed", "local_high_jets_computed"):
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
    """Pure IO; a transport carrier never replaces the original mathematical identity."""
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
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == spec["core_sha256"]
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
    if label == "R786":
        match = re.fullmatch(r"R786-exact-power-([124])-row-(\d{4})\.json\.gz", name)
        if match:
            power, index = int(match[1]), int(match[2])
            return ((power == 4 and 0 <= index < 962) or
                    (power == 1 and index in M2_INDICES) or
                    (power == 2 and index in P2_INDICES))
    return False


def extract_bundle(bundle, target, specs):
    target.mkdir(parents=True, exist_ok=True)
    seen, counts = set(), {label: 0 for label in LABELS}
    with tarfile.open(bundle, "r:gz") as archive:
        for member in archive:
            relative = Path(member.name)
            assert member.isfile() and not relative.is_absolute() and ".." not in relative.parts
            assert len(relative.parts) == 2
            group, name = relative.parts
            assert group in LABELS and allowed_group_name(group, specs[group], name)
            assert str(relative) not in seen
            seen.add(str(relative))
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
            counts[group] += 1
    assert counts == GROUP_COUNTS and len(seen) == 997
    return counts


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
    """Read/hash/schema only: retain exactly the original three-group continuation closure."""
    p775, p786, p805 = (producers[label] for label in ("R775", "R786", "R805"))
    for label in ("R775", "R786"):
        same_producer(p805.initial["job"]["retained_artifacts"][label], producers[label].spec)
        same_producer(p805.tag["retained_artifacts"][label], producers[label].spec)
    m6 = p775.cert_stage(M6, M6_SHA)
    assert m6["rank"] == len(m6["basis"]) == 694
    assert m6["characteristic_zero_independence_certified_by_unit_reduction"] is True
    assert p775.tag["prime"] == 739 and p775.tag["xi41_mod_ell"] == 538
    for index, row in enumerate(m6["basis"][:690]):
        assert row["recipe"] == {"kind": "power_basis", "power": 3, "index": index}
    for index, recipe in M6_RECIPES.items():
        assert m6["basis"][index]["recipe"] == recipe
    p2 = p775.cert_stage(P2, P2_SHA)
    assert p2["rank"] == len(p2["basis"]) == 418
    aliases = {}
    for index, row in enumerate(p2["basis"]):
        recipe = row["recipe"]
        assert recipe["kind"] == "product" and recipe["left_power"] == recipe["right_power"] == 1
        pair = tuple(sorted((recipe["left_index"], recipe["right_index"])))
        aliases.setdefault(pair, index)
    assert all(aliases[pair] == index for pair, index in OLD_PAIR_ALIASES.items())
    assert all(tuple(pair) not in aliases for pair, size, digest in NEW_PAIRS.values())
    assert p786.tag["R775_completed_prefix_producer"]["files"][P2] == P2_SHA
    assert p786.certificate["exact_K_basis_prefix_bound_qY"] == 128
    assert p786.certificate["basis_in_original_R775_saved_order"] is True
    inventory = p786.inventory("stages_manifest")
    needed = [(4, i) for i in range(962)]+[(1, i) for i in M2_INDICES]+[(2, i) for i in P2_INDICES]
    for power, index in needed:
        name = "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"
        data = p786.stage(inventory[name])
        assert data["weight"] == 2*power and data["bound_qY"] == 128
        assert data["integer_scale"] == str(82**(2*power))
        assert data["original_R775_finite_coefficients_verified"] is True
        assert len(data["integer_qY_xi_coefficients"]) == 129
        assert all(len(row) == 40 for row in data["integer_qY_xi_coefficients"])
        if power == 2:
            assert data["recipe"] == p2["basis"][index]["recipe"]
    certificate = p805.certificate
    assert certificate["completed_scope"] == "pencil_and_graded_free_basis"
    assert certificate["degree3_S_prefix_count"] == 41
    assert certificate["original_82_scales_preserved"] is True
    previous = p805.inventory("stage_manifest")
    for name, (pair, size, digest) in NEW_PAIRS.items():
        assert previous[name]["bytes"] == size and previous[name]["sha256"] == digest
        data = p805.stage(previous[name])
        assert data["sorted_M2_leaf_indices"] == pair
        assert data["weight"] == 4 and data["integer_scale"] == str(82**4) and data["qY_count"] == 41
        assert data["all_original_and_real_coordinates_verified"] is True
        assert data["old_recipe_alias_exists"] is False and data["old_saved_product_recomputed"] is False
        assert len(data["integer_qY_xi_coefficients"]) == len(data["integer_v_t_coefficients"]) == 41
        assert all(len(row) == 40 for row in data["integer_qY_xi_coefficients"])
        assert all(len(row) == 20 for row in data["integer_v_t_coefficients"])
        expected = []
        for index in pair:
            source_name = "R786-exact-power-1-row-"+str(index).zfill(4)+".json.gz"
            expected.append(dict(inventory[source_name], producer="R786"))
        assert data["factor_sources"] == expected
    for label, producer in producers.items():
        assert all(name in producer.selected for name in producer.spec["files"])
        assert len(producer.selected) == GROUP_COUNTS[label], (label, len(producer.selected))
    return {"old_V4_rows": 962, "old_M2_indices": list(M2_INDICES),
        "old_V2_indices": list(P2_INDICES), "read_prefix_count_only": 55,
        "old_R805_pair_prefix_count": 41, "only_possible_new_pair_tail_interval": [41, 55],
        "old_R805_pair_prefixes": list(NEW_PAIRS),
        "selected_group_counts": GROUP_COUNTS, "selected_original_file_count": 997,
        "all_sizes_sha256_original_schemas_and_parent_identities_verified": True,
        "new_mathematical_arithmetic_executed_during_input_selection": False}


def verify_bundle(bundle, producers):
    expected = {label+"/"+name: file_spec(path) for label, producer in producers.items()
                for name, path in producer.selected.items()}
    seen = set()
    with tarfile.open(bundle, "r:gz") as archive:
        for member in archive:
            assert member.isfile() and member.name in expected and member.name not in seen
            row = expected[member.name]
            assert member.size == row["bytes"]
            digest = hashlib.sha256()
            with archive.extractfile(member) as stream:
                for block in iter(lambda: stream.read(1024*1024), b""):
                    digest.update(block)
            assert digest.hexdigest() == row["sha256"]
            seen.add(member.name)
    assert seen == set(expected) and len(seen) == 997


def prepare_inputs(item, out):
    specs = item["retained_artifacts"]
    assert set(specs) == LABELS
    inputs = out.parent/"retained"
    present = [(inputs/label/"full-outputs-manifest.json").exists() for label in LABELS]
    transferred = all(present)
    assert transferred or not any(present), "Partial unverified R807 input carrier"
    transport = []
    if transferred:
        producers = {label: Producer(label, specs[label], [inputs/label]) for label in sorted(LABELS)}
    else:
        producers = {}
        for label in sorted(LABELS):
            producer_spec = specs[label]
            carrier = producer_spec.get("input_carrier")
            download_spec = carrier if carrier is not None else producer_spec
            if carrier is not None:
                assert label == "R805" and carrier["role"] == "unchanged_original_selected_files"
                assert carrier["original_result"] == producer_spec["result"]
                assert carrier["original_run_id"] == producer_spec["run_id"]
                assert carrier["original_source_commit"] == producer_spec["source_commit"]
            directory = out.parent/("downloaded-"+label)
            download(download_spec, directory, require_complete=True)
            producers[label] = Producer(label, producer_spec, [directory])
            transport.append({"label": label, "downloaded_artifact": download_spec,
                "original_mathematical_producer_preserved": True})
    assert producers["R805"].tag["R805_proof_sha256"] == item["R805_proof_sha256"]
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
        temporary = out/(INPUT_BUNDLE+".tmp")
        with tarfile.open(temporary, "w:gz") as archive:
            for label in sorted(LABELS):
                for name in sorted(producers[label].selected):
                    archive.add(inputs/label/name, arcname=label+"/"+name, recursive=False)
        temporary.replace(out/INPUT_BUNDLE)
    verify_bundle(out/INPUT_BUNDLE, producers)
    save(out/"retained-inputs-receipt.json", {"result": RESULT, "groups": groups, "selection": selection,
        "all_inputs_from_same_core_active_R807_bundle": transferred,
        "fresh_transport_artifacts": transport, "input_bundle": file_spec(out/INPUT_BUNDLE),
        "all997_bundle_members_individually_size_and_sha256_verified": True,
        "audit_carrier_substituted_for_original_mathematical_source": False,
        "old_arithmetic_recomputed": False})
    return inputs


def restore_resume(item, out):
    previous = item.get("resume")
    if previous is None:
        return
    directory = out.parent/"downloaded-R807-continuation"
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
    for key in ("result", "p", "core_sha256", "R805_proof_sha256", "R807_method_sha256",
                "retained_artifacts", "qY_count", "V4_dimension", "auxiliary_prime_start",
                "reconstruct_every_digits", "requested_stage"):
        assert initial["job"][key] == item[key], "Changed continuation identity: "+key
    bundle = bound(INPUT_BUNDLE)
    extract_bundle(bundle, out.parent/"retained", item["retained_artifacts"])
    shutil.copyfile(bundle, out/INPUT_BUNDLE)
    count = 0
    for name in entries:
        if not (name.startswith("R807-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        source = bound(name)
        data = read(source)
        assert data["complete"] is True
        matching_configuration(data["configuration"], item)
        shutil.copyfile(source, out/name)
        count += 1
    save(out/"resume-receipt.json", {"result": RESULT, "producer": previous,
        "same_exact_core_sha256": item["core_sha256"], "complete_checkpoint_files_copied": count,
        "three_group_original_input_bundle_restored": True,
        "completed_projections_theta_member_coordinates_and_pair_tails_preserved": True,
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
        "new_arithmetic": "one962 V4 block, five selected-row projections, true138x5 kernel, four cleared M6 rows",
        "old_M2_V2_V4_or_R805_pair_prefixes_recomputed": False,
        "R803_mixed_coordinates_consumed": False,
        "theta_Uj_local_high_jets_polar_divisors_eta_or_height_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41 and item["producer_inputs_pending"] is False
        assert sha(core) == item["core_sha256"] and sha(__file__) == item["wrapper_sha256"]
        assert sha(proof) == item["R805_proof_sha256"] and sha(method) == item["R807_method_sha256"]
        assert sha(S/"R786_public_exact_power5_short_basis.py") == item["download_helper_sha256"]
        assert sha(S/"p41_public_actions_recovery.py") == item["io_helper_sha256"]
        assert item["qY_count"] == 55 and item["V4_dimension"] == 962
        assert item["auxiliary_prime_start"] == 1000000007 and item["reconstruct_every_digits"] == 8
        assert item["requested_stage"] == "four_extra_M6_rows_cleared"
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
                error = "Budget reached; exact completed projections/theta/coordinates and current Dixon lift retained."
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
        "actual_nonzero_theta_and_four_original_M6_clearing_coordinates_computed": complete,
        "old_M2_V2_V4_or_R805_pair_prefixes_recomputed": False,
        "theta_Uj_local_high_jets_polar_divisors_eta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete, "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    """Pure IO review of actual producer checks; no field/matrix arithmetic is repeated."""
    run, receipt = read(out/"run-receipt.json"), read(out/"core-receipt.json")
    assert run["result"] == RESULT and run["complete"] is True and run["process_exit_code"] == 0
    assert run["core_receipt_sha256"] == sha(out/"core-receipt.json")
    assert receipt["result"] == RESULT and receipt["complete"] is True
    assert receipt["source_sha256"] == item["core_sha256"] and receipt["certificate_sha256"] == sha(out/FINAL)
    for key in ("actual_nonzero_theta_constructed", "actual_M6_pole_clearing_computed",
                "all_four_M6_products_verified_in_all1100_rows"):
        assert receipt[key] is True
    assert receipt["polar_divisors_eta_rigidification_or_height_computed"] is False
    certificate = read(out/FINAL)
    assert certificate["result"] == RESULT and certificate["complete"] is True and certificate["p"] == 41
    matching_configuration(certificate["configuration"], item)
    assert certificate["completed_scope"] == "four_extra_M6_rows_cleared"
    assert certificate["V4_dimension"] == 962 and certificate["qY_count"] == 55
    assert certificate["full_real_coordinate_rows"] == 1100
    assert certificate["ordinary_V4_integer_scale"] == str(82**8)
    for key in ("actual_nonzero_theta_constructed", "actual_M6_pole_clearing_computed",
                "five_selected_row_projections_exactly_verified", "all_four_M6_products_verified_in_all1100_rows",
                "global_degree1092_vs_cusp_order1100_bound_used", "rank_four_not_preassigned"):
        assert certificate[key] is True
    for key in ("individual_five_target_membership_claimed", "ninth_rhs_for_M6_index692_solved",
                "old_M2_V2_V4_or_R805_pair_prefixes_recomputed", "characteristic_zero_inverse_matrix_formed",
                "R803_mixed_coordinates_consumed", "theta_Uj_functions_computed", "local_high_jets_computed",
                "primitive_multiplication_computed", "polar_divisors_eta_rigidification_or_height_computed"):
        assert certificate[key] is False
    assert certificate["exact_right_hand_sides_solved"] == 8

    def stage(spec):
        assert Path(spec["file"]).name == spec["file"]
        path = out/spec["file"]
        assert file_spec(path) == plain_spec(spec)
        data = read(path)
        assert data["complete"] is True
        matching_configuration(data["configuration"], item)
        return data

    inventory = stage(certificate["stage_manifest"])
    entries = {row["file"]: plain_spec(row) for row in inventory["files"]}
    assert len(entries) == len(inventory["files"])
    for name, spec in entries.items():
        assert name.startswith("R807-") and name.endswith(".json.gz")
        assert not name.endswith("-dixon-current.json.gz"), "Finished job retains an unresolved exact RHS lift."
        # Do not keep every matrix/prefix resident during IO verification.
        data = stage(spec)
        del data
    inputs = out.parent/"retained"
    producers = {label: Producer(label, item["retained_artifacts"][label], [inputs/label]) for label in sorted(LABELS)}
    selection = select_original_inputs(producers)
    assert producers["R805"].tag["R805_proof_sha256"] == item["R805_proof_sha256"]

    def source(spec):
        label = spec["producer"]
        if label == "R807":
            assert plain_spec(spec) == entries[spec["file"]]
        else:
            producers[label].bound(spec["file"], spec)

    def referenced(spec):
        assert plain_spec(spec) == entries[spec["file"]]
        return stage(spec)

    basis = referenced(certificate["basis_index"])
    assert basis["dimension"] == 962 and basis["qY_count"] == 55 and basis["full_real_coordinates"] == 1100
    assert basis["integer_scale"] == str(82**8) and basis["source_prefix_only_read"] == [0, 55]
    assert basis["old_V4_coefficients_recomputed"] is False and len(basis["basis_rows"]) == 962
    source(basis["original_R786_stages_manifest"])
    for index, row in enumerate(basis["basis_rows"]):
        assert row["index"] == index
        source(row["original_source"])
        assert row["original_source"]["producer"] == "R786"
        assert row["original_source"]["file"] == "R786-exact-power-4-row-"+str(index).zfill(4)+".json.gz"
        source(row["adapted_stage"])
        adapted = referenced(row["adapted_stage"])
        assert adapted["ordinary_power"] == 4 and adapted["index"] == index
        assert adapted["source_original_row"] == row["original_source"]
        assert adapted["original_recipe"] == row["original_recipe"]
        assert adapted["source_prefix_range"] == [0, 55] and adapted["qY_count"] == 55
        assert adapted["integer_scale"] == str(82**8)
        assert adapted["original_xi_inversion_and_phase_verified"] is True
        assert adapted["old_qY_coefficients_recomputed"] is False
        assert len(adapted["integer_v_t_coefficients"]) == 55
        assert all(len(values) == 20 for values in adapted["integer_v_t_coefficients"])
    minor = referenced(certificate["minor_stage"])
    assert minor["basis_index"] == certificate["basis_index"]
    assert minor["full_rows"] == 1100 and minor["columns"] == 962
    assert minor["prime_proved"] is True and minor["modular_inverse_identity_verified"] is True
    assert minor["all_entries_from_original_exact_short_rows"] is True
    assert minor["characteristic_zero_basis_independence_certified"] is True
    assert minor["characteristic_zero_inverse_matrix_formed"] is False
    rows = minor["coordinate_row_indices"]
    assert len(rows) == 962 and rows == sorted(set(rows)) and all(0 <= i < 1100 for i in rows)
    assert minor["selected_basis_column_indices"] == list(range(962))
    assert minor["actual_determinant_mod_prime"] % minor["prime"]
    assert len(minor["inverse_mod_prime"]) == 962 and all(len(row) == 962 for row in minor["inverse_mod_prime"])
    assert certificate["actual_short_minor"] == {
        "prime": minor["prime"], "rank": 962, "coordinate_row_indices": rows,
        "determinant_mod_prime": minor["actual_determinant_mod_prime"]}
    assert certificate["minor_stage"]["file"] == "R807-original-V4-accepted-short-minor.json.gz"
    assert len(certificate["projection_stages"]) == len(certificate["projection_target_stages"]) == 5

    def check_solution(spec, target_spec, mode, label):
        data = referenced(spec)
        assert data["label"] == label and data["mode"] == mode
        assert data["source_target_stage"] == target_spec
        assert data["original_V4_basis_index"] == certificate["basis_index"]
        assert data["minor_stage"] == certificate["minor_stage"]
        assert data["basis_dimension"] == 962 and data["basis_integer_scale"] == str(82**8)
        assert len(data["solution_numerators"]) == 962 and int(data["solution_common_denominator"]) > 0
        assert data["actual_prime"] == minor["prime"] and data["actual_Dixon_digits"] >= 1
        assert data["all962_selected_rows_verified"] is True
        assert data["all1100_rows_verified"] is (mode == "member")
        assert data["individual_V4_membership_claimed"] is (mode == "member")
        assert data["rational_reconstruction_used_uniform_strict_rectangular_bound"] is True
        assert data["characteristic_zero_inverse_matrix_formed"] is False
        assert data["old_basis_coefficients_recomputed"] is False
        target = referenced(target_spec)
        assert data["target_denominator_restored_exactly"] == target["common_denominator"]
        return data

    for j, (spec, target_spec) in enumerate(zip(certificate["projection_stages"], certificate["projection_target_stages"])):
        target = referenced(target_spec)
        assert target["projection_M2_index"] == j and target["source_M6_index"] == 692
        assert target["source_M6_recipe"] == M6_RECIPES[692]
        assert target["individual_target_V4_membership_claimed"] is False
        assert target["old_M2_or_M6_prefixes_recomputed"] is False
        assert target["qY_count"] == 55 and target["full_real_coordinates"] == 1100
        assert target["product_integer_scale"] == str(82**8)
        assert target["common_denominator"] == "1" and len(target["integer_numerators"]) == 1100
        for key in ("source_M2_adaptation", "source_original_M2", "source_original_M6"):
            source(target[key])
        check_solution(spec, target_spec, "projection", "E6-projection-j"+str(j))
    residual = referenced(certificate["residual_kernel_stage"])
    assert residual["projection_stages"] == certificate["projection_stages"]
    assert residual["projection_target_stages"] == certificate["projection_target_stages"]
    assert residual["original_V4_basis_index"] == certificate["basis_index"]
    assert residual["minor_stage"] == certificate["minor_stage"]
    complement = [i for i in range(1100) if i not in set(rows)]
    assert len(complement) == 138 and residual["residual_original_row_indices"] == complement
    rank = residual["actual_rank"]
    assert type(rank) is int and 0 <= rank <= 4
    assert certificate["actual_residual_rank"] == rank
    assert certificate["actual_residual_kernel_dimension"] == 5-rank
    assert len(residual["residual_integer_numerators"]) == 138
    assert all(len(row) == 5 for row in residual["residual_integer_numerators"])
    assert len(residual["residual_column_denominators"]) == 5
    assert all(int(value) > 0 for value in residual["residual_column_denominators"])
    assert len(residual["pivot_columns"]) == len(residual["independent_original_row_indices"]) == rank
    assert residual["pivot_columns"] == sorted(set(residual["pivot_columns"]))
    assert residual["free_columns"] == [i for i in range(5) if i not in residual["pivot_columns"]]
    assert len(residual["rref_nonzero_rows"]) == rank
    assert all(len(row) == 5 for row in residual["rref_nonzero_rows"])
    assert len(residual["full_nullspace_basis"]) == 5-rank
    assert all(len(row) == 5 for row in residual["full_nullspace_basis"])
    assert residual["chosen_smallest_free_column"] == residual["free_columns"][0]
    assert int(residual["actual_nonzero_rank_minor"][0]) != 0
    assert int(residual["actual_nonzero_rank_minor"][1]) > 0
    assert residual["all_138_rows_for_all_kernel_basis_vectors_verified"] is True
    assert residual["rank_four_was_not_preassigned"] is True
    assert residual["all962_selected_row_residuals_zero_verified"] is True
    assert residual["individual_five_projection_membership_claimed"] is False
    assert len(residual["lambda"]) == 5 and all(len(pair) == 2 and int(pair[1]) > 0 for pair in residual["lambda"])
    first = residual["first_nonzero_lambda_index"]
    assert 0 <= first < 5 and residual["lambda"][first] == ["1", "1"]
    assert all(int(pair[0]) == 0 for pair in residual["lambda"][:first])
    theta = referenced(certificate["theta_stage"])
    assert theta["residual_kernel_stage"] == certificate["residual_kernel_stage"]
    assert theta["lambda"] == residual["lambda"] and theta["actual_residual_rank"] == rank
    assert theta["first_nonzero_lambda_index"] == first == certificate["theta_first_nonzero_original_M2_index"]
    assert theta["theta_in_original_integer_scaled_M2_basis"] == residual["lambda"]+[["0", "1"] for _ in range(141)]
    assert theta["source_original_M2_indices"] == [0, 1, 2, 3, 4]
    assert theta["original_M2_integer_scale"] == str(82**2)
    assert theta["theta_nonzero_by_original_independent_M2_input"] is True
    assert theta["theta_at_P0_and_P1_has_two_zeros_by_original_E6_principal_parts"] is True
    assert theta["global_comparison_degree_bound"] == 1092
    assert theta["certified_cusp_zero_order_times_degree"] == 1100
    for key in ("new_CM_jets_used", "full_142_dimensional_clearing_space_recomputed",
                "original_P0_P1_qY_or_M2_basis_changed"):
        assert theta[key] is False
    coordinates = certificate["cleared_coordinate_stages"]
    assert set(coordinates) == {"690", "691", "692", "693"}
    assert theta["M6_index692_cleared_coordinate_stage"] == coordinates["692"]
    derived = referenced(coordinates["692"])
    assert derived["M6_index"] == 692 and derived["source_M6_recipe"] == M6_RECIPES[692]
    source(derived["source_original_M6"])
    assert derived["residual_kernel_stage"] == certificate["residual_kernel_stage"]
    assert derived["projection_stages"] == certificate["projection_stages"]
    assert derived["original_V4_basis_index"] == certificate["basis_index"]
    assert derived["minor_stage"] == certificate["minor_stage"] and derived["lambda"] == residual["lambda"]
    assert len(derived["solution_numerators"]) == 962 and int(derived["solution_common_denominator"]) > 0
    assert len(derived["target_integer_numerators"]) == 1100 and int(derived["target_common_denominator"]) > 0
    assert derived["basis_dimension"] == 962 and derived["basis_integer_scale"] == str(82**8)
    for key in ("all1100_rows_verified", "exact_global_V4_membership_certified",
                "coordinates_obtained_from_five_existing_projections"):
        assert derived[key] is True
    assert derived["a_ninth_right_hand_side_solved"] is False
    for index in (690, 691, 693):
        solution = referenced(coordinates[str(index)])
        target_spec = solution["source_target_stage"]
        target = referenced(target_spec)
        assert target["M6_index"] == index and target["source_M6_recipe"] == M6_RECIPES[index]
        assert target["theta_stage"] == certificate["theta_stage"]
        source(target["source_original_M6"])
        assert len(target["integer_numerators"]) == 1100 and int(target["common_denominator"]) > 0
        assert target["qY_count"] == 55 and target["full_real_coordinates"] == 1100
        assert target["product_integer_scale"] == str(82**8)
        assert target["lambda_denominator_preserved"] is True
        assert target["eta_shift_original_phase_is_one"] is (index == 693)
        assert target["old_M2_V2_V4_or_R805_pair_prefixes_recomputed"] is False
        for component in target["component_sources"]:
            assert int(component["integer_lambda_numerator"]) != 0
            assert 0 <= component["lambda_index"] < 5
            for row in component.get("sources", []):
                source(row)
            if "source" in component:
                source(component["source"])
        check_solution(coordinates[str(index)], target_spec, "member", "M6-index-"+str(index))
    tails = certificate["actual_new_pair_tail_stages"]
    assert len(tails) <= 2 and len({row["file"] for row in tails}) == len(tails)
    expected_tail_pairs = [[j, 73] for j in (3, 4) if int(residual["lambda"][j][0]) != 0]
    actual_tail_pairs = []
    for spec in tails:
        tail = referenced(spec)
        pair = tail["sorted_M2_leaf_indices"]
        assert pair in ([3, 73], [4, 73])
        actual_tail_pairs.append(pair)
        assert tail["first_exponent"] == 41 and tail["last_exponent_exclusive"] == 55
        assert tail["weight"] == 4 and tail["integer_scale"] == str(82**4)
        assert tail["packed_stride"] == 79 and tail["maximum_unreduced_xi_degree"] == 78
        assert len(tail["integer_qY_xi_coefficients"]) == len(tail["integer_v_t_coefficients"]) == 14
        assert all(len(row) == 40 for row in tail["integer_qY_xi_coefficients"])
        assert all(len(row) == 20 for row in tail["integer_v_t_coefficients"])
        for key in ("only_new_sum_band_convolved", "original_phase_and_xi_inversion_verified"):
            assert tail[key] is True
        for key in ("old_R805_q0_through40_recomputed", "old_saved_V2_alias_recomputed"):
            assert tail[key] is False
        source(tail["source_completed_R805_prefix"])
        for spec in tail["source_original_M2_factors"]:
            source(spec)
        for a, b, c, d in tail["convolution_rectangles"]:
            assert 0 <= a < b <= 55 and 0 <= c < d <= 55
            assert a+c >= 41 and b+d-2 < 55
    assert sorted(actual_tail_pairs) == expected_tail_pairs
    index = referenced(certificate["cleared_coordinate_index"])
    assert index["extra_M6_indices"] == [690, 691, 692, 693]
    assert index["coordinate_stages"] == coordinates and index["theta_stage"] == certificate["theta_stage"]
    assert index["residual_kernel_stage"] == certificate["residual_kernel_stage"]
    assert index["original_V4_basis_index"] == certificate["basis_index"]
    assert index["ordinary_V4_integer_scale"] == str(82**8)
    assert index["original_M6_integer_scale"] == str(82**6)
    assert index["original_theta_M2_integer_scale"] == str(82**2)
    assert index["four_original_M6_recipes"] == {str(i): recipe for i, recipe in M6_RECIPES.items()}
    assert index["new_pair_tail_stages"] == tails
    for key in ("all_four_members_verified_in_all1100_real_coordinates",
                "all_five_initial_columns_are_only_selected_row_projections", "actual_nonzero_theta_constructed"):
        assert index[key] is True
    assert index["R803_mixed_coordinates_consumed"] is False and index["theta_Uj_functions_computed"] is False
    receipt = read(out/"retained-inputs-receipt.json")
    assert receipt["selection"] == selection
    assert receipt["all997_bundle_members_individually_size_and_sha256_verified"] is True
    assert receipt["audit_carrier_substituted_for_original_mathematical_source"] is False
    bundle = receipt["input_bundle"]
    assert bundle["file"] == INPUT_BUNDLE and file_spec(out/INPUT_BUNDLE) == bundle
    verify_bundle(out/INPUT_BUNDLE, producers)
    manifest = read(out/"full-outputs-manifest.json")
    assert manifest["result"] == RESULT
    seen = set()
    for row in manifest["files"]:
        assert row["file"] not in seen and Path(row["file"]).name == row["file"]
        assert file_spec(out/row["file"]) == plain_spec(row)
        seen.add(row["file"])
    assert seen == {path.name for path in out.iterdir() if path.is_file()
                    and path.name not in ("full-outputs-manifest.json", REFERENCE)}
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
