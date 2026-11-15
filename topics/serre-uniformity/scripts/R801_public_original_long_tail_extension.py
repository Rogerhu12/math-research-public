#!/usr/bin/env python3
"""R801 public runner: original selected prefixes, only missing exact tails."""
import argparse
import datetime as dt
from functools import lru_cache
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

from p41_public_actions_recovery import publish, read, save, sha
from R786_public_exact_power5_short_basis import download, find_hash

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R801-public-original-long-tail-extension-request.json"
RESULT = "R801-original-power6-to8-long-tails"
FINAL = "p41-original-power6-to8-long-tails-certificate.json"
INPUT_BUNDLE = "R801-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
LABELS = {"R775", "R786", "R795", "R799", "R800"}
PRODUCER_META = ("full-outputs-manifest.json", "run-receipt.json",
                 "core-receipt.json", "public-actions-input.json")
META = {"public-actions-input.json", "retained-inputs-receipt.json",
        "resume-receipt.json", "run-receipt.json", "core-receipt.json"}
DIMS = {1: 146, 2: 418, 3: 690, 4: 962, 5: 1234, 6: 1506, 7: 1778, 8: 2050}
FIRST = {6: 109, 7: 96, 8: 109}
FRONTIERS = {6: (142,), 7: (170, 172, 176), 8: (193, 196)}
ANCHORS = (0, 1, 73)


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
    assert tag["python_flint"] == "0.9.0" and tag["p"] == 41 and tag["level"] == 82
    for key in ("R801_proof_sha256", "R801_method_sha256", "retained_artifacts",
                "primary_new_intervals", "primary_frontiers", "auxiliary_max_exponent",
                "generate_additional_pencil_V3_tail"):
        assert tag[key] == item[key]
    assert tag["primary_new_intervals"] == {"6": [109, 142], "7": [96, 176], "8": [109, 196]}
    assert tag["primary_frontiers"] == {str(p): list(stops) for p, stops in FRONTIERS.items()}
    assert tag["auxiliary_max_exponent"] == 195 and tag["generate_additional_pencil_V3_tail"] is False
    assert tag["primary_dimensions"] == {"6": 1506, "7": 1778, "8": 2050}
    assert tag["integer_scales"] == {str(p): str(82**(2*p)) for p in range(1, 9)}
    assert tag["v_parameter"] == "v=xi41^-10*qY" and tag["t_parameter"] == "t=xi41+xi41^-1"
    for key in ("ordinary_basis_reselected", "old_coefficients_recomputed", "Laurent_Dixon_or_rational_map_computed"):
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
    """Read-only identity/manifest view over already downloaded exact producers."""
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
        assert str(run["workflow_run_id"]) == str(spec["run_id"]) and run["source_commit"] == spec["source_commit"]
        assert run["core_receipt_sha256"] == sha(self.paths["core-receipt.json"])
        assert core["complete"] is True and core["source_sha256"] == spec["core_sha256"]
        assert initial["result"] == spec["result"] and initial["source_commit"] == spec["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
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

    def inventory(self, key):
        spec = self.certificate[key]
        value = self.stage(spec)
        files = {row["file"]: plain_spec(row) for row in value["files"]}
        assert len(files) == len(value["files"])
        return files


def allowed_group_name(label, spec, name):
    if name in set(PRODUCER_META)|set(spec["files"]):
        return True
    if label == "R775":
        return name == "R775-basis-M2.json.gz" or bool(re.fullmatch(r"R775-basis-power-[2-6]\.json\.gz", name))
    if label == "R786":
        return name in {"R786-exact-power5-basis-index.json.gz", "R786-exact-stages-manifest.json.gz"} or \
            bool(re.fullmatch(r"R786-exact-power-[1-5]-row-\d{4}\.json\.gz", name))
    if label == "R795":
        return name in {"R795-exact-power6-basis-index.json.gz", "R795-exact-stages-manifest.json.gz"} or \
            bool(re.fullmatch(r"R795-exact-power-6-row-\d{4}\.json\.gz", name))
    if label == "R799":
        return name.startswith("R799-") and name.endswith(".json.gz")
    if label == "R800":
        return name.startswith("R800-") and name.endswith(".json.gz")
    return False


def extract_bundle(bundle, target, specs, mode):
    """Only regular two-level data files; no execution or raw archive extraction."""
    target.mkdir(parents=True, exist_ok=True)
    seen, selected = set(), 0
    allowed_labels = LABELS if mode == "self" else {"R775", "R786", "R795"}
    with tarfile.open(bundle, "r:gz") as archive:
        for member in archive:
            relative = Path(member.name)
            assert member.isfile() and not relative.is_absolute() and ".." not in relative.parts
            assert len(relative.parts) == 2 and relative.parts[0] in allowed_labels
            group, name = relative.parts
            assert allowed_group_name(group, specs[group], name)
            assert str(relative) not in seen
            seen.add(str(relative))
            if mode == "R799" and group != "R795" and name not in set(PRODUCER_META)|set(specs[group]["files"]):
                continue
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
            selected += 1
    assert selected
    return selected


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


def row_shape(data, count, real=True):
    assert len(data["integer_qY_xi_coefficients"]) == count
    assert all(len(row) == 40 for row in data["integer_qY_xi_coefficients"])
    if real:
        assert len(data["integer_v_t_coefficients"]) == count
        assert all(len(row) == 20 for row in data["integer_v_t_coefficients"])


def select_original_inputs(producers):
    """Only source identity/recipe closure and structural checks; no arithmetic."""
    p775, p786, p795, p799, p800 = (producers[label] for label in ("R775", "R786", "R795", "R799", "R800"))
    bases, stages775 = {}, {row["file"]: row for row in p775.certificate["stages"]}
    assert p775.certificate["all_recipes_defined_over_original_K"] is True
    assert p775.tag["prime"] == 739 and p775.tag["xi41_mod_ell"] == 538
    for power in range(1, 7):
        name = "R775-basis-M2.json.gz" if power == 1 else "R775-basis-power-"+str(power)+".json.gz"
        data = p775.stage(stages775[name])
        assert data["rank"] == len(data["basis"]) == DIMS[power]
        assert data["coefficient_bound"] >= 272*power
        assert data["characteristic_zero_independence_certified_by_unit_reduction"] is True
        minor = data["actual_nonzero_minor"]
        assert minor["rows"] == minor["columns"] == DIMS[power] and minor["prime"] == 739
        assert int(minor["determinant_mod_ell"]) % 739
        bases[power] = data["basis"]
        if power <= 5:
            assert p786.tag["R775_completed_prefix_producer"]["files"][name] == stages775[name]["sha256"]
    assert sorted({row["recipe"]["left_index"] for row in bases[6]}) == list(ANCHORS)
    for row in bases[6]:
        assert row["recipe"]["kind"] == "product" and row["recipe"]["left_power"] == 1
        assert row["recipe"]["right_power"] == 5
    inv786 = p786.inventory("stages_manifest")
    idx786 = p786.stage(p786.certificate["basis_index"])
    assert idx786["dimension"] == len(idx786["basis_rows"]) == 1234
    assert [row["index"] for row in idx786["basis_rows"]] == list(range(1234))
    assert p786.certificate["exact_K_basis_prefix_bound_qY"] == 128
    assert p786.certificate["basis_in_original_R775_saved_order"] is True
    inv795 = p795.inventory("stage_manifest")
    idx795 = p795.stage(p795.certificate["basis_index"])
    assert idx795["dimension"] == len(idx795["basis_rows"]) == 1506
    assert [row["index"] for row in idx795["basis_rows"]] == list(range(1506))
    assert p795.certificate["exact_K_basis_prefix_bound_qY"] == 81
    assert p795.certificate["basis_in_original_R775_saved_order"] is True
    assert p795.certificate["all_original_R775_mod739_short_series_compared"] is True
    assert p795.certificate["all_original_real_cyclotomic_transports_verified"] is True
    inv799 = p799.inventory("stage_manifest")
    idx799six = p799.stage(p799.certificate["power6_tail_index"])
    assert idx799six["dimension"] == len(idx799six["basis_rows"]) == 1506
    assert [row["index"] for row in idx799six["basis_rows"]] == list(range(1506))
    assert idx799six["first_exponent"] == 82 and idx799six["last_exponent_exclusive"] == 109
    assert p799.certificate["three_original_anchor_basepoint_free_input_verified"] is True
    assert p799.certificate["new_exact_basis_dimensions"] == {"7": 1778, "8": 2050}
    assert p799.certificate["new_exact_basis_bounds_qY"] == {"7": 95, "8": 108}
    selected799 = {}
    for power in (7, 8):
        index = p799.stage(p799.certificate["basis_indices"][str(power)])
        assert index["ordinary_power"] == power and index["dimension"] == len(index["basis_rows"]) == DIMS[power]
        assert index["bound_qY"] == FIRST[power]-1 and index["integer_scale"] == str(82**(2*power))
        assert index["full_original_real_coordinates"] == 20
        assert index["all_exact_rows_compared_with_selecting_modular_columns"] is True
        assert index["characteristic_zero_basis_certified"] is True
        assert [row["index"] for row in index["basis_rows"]] == list(range(DIMS[power]))
        assert len({row["file"] for row in index["basis_rows"]}) == DIMS[power]
        positions = [row["candidate_position"] for row in index["basis_rows"]]
        assert positions == sorted(set(positions))
        minor = index["actual_nonzero_minor"]
        assert minor == p799.certificate["actual_new_nonzero_minors"][str(power)]
        assert minor["rows"] == minor["columns"] == DIMS[power]
        assert minor["determinant_mod_prime"] % minor["prime"]
        assert len(set(minor["coordinate_row_indices"])) == DIMS[power]
        assert all(0 <= i < 20*FIRST[power] for i in minor["coordinate_row_indices"])
        assert minor["selected_basis_column_indices"] == list(range(DIMS[power]))
        assert minor["all_entries_from_saved_exact_integer_rows"] is True
        selected799[power] = index["basis_rows"]
    inv800 = p800.inventory("stage_manifest")
    idx800 = p800.stage(p800.certificate["basis_tail_index"])
    assert idx800["dimension"] == len(idx800["tail_rows_in_original_order"]) == 146
    assert idx800["first_exponent"] == 129 and idx800["last_exponent_exclusive"] == 196
    assert idx800["integer_scale"] == "6724"
    assert p800.certificate["all_new_original_mod739_coefficients_verified"] is True
    assert p800.certificate["all_new_real_tangent_involutions_verified"] is True

    @lru_cache(maxsize=None)
    def leaves(power, index):
        assert 1 <= power <= 6 and 0 <= index < DIMS[power]
        if power == 1:
            return (index,)
        recipe = bases[power][index]["recipe"]
        assert recipe["kind"] == "product"
        left, right = recipe["left_power"], recipe["right_power"]
        assert 0 < left < power and 0 < right < power and left+right == power
        return tuple(sorted(leaves(left, recipe["left_index"])+leaves(right, recipe["right_index"])))

    aliases, needed, multipliers = {}, set(), {}
    for power in (2, 3):
        for index in range(DIMS[power]):
            key = leaves(power, index)
            assert key not in aliases
            aliases[key] = (power, index)

    def add_original(power, index):
        assert 1 <= power <= 6 and 0 <= index < DIMS[power]
        if (power, index) in needed:
            return
        needed.add((power, index))
        if power > 1:
            recipe = bases[power][index]["recipe"]
            assert recipe["kind"] == "product"
            assert 0 < recipe["left_power"] < power and 0 < recipe["right_power"] < power
            assert recipe["left_power"]+recipe["right_power"] == power
            for side in ("left", "right"):
                add_original(recipe[side+"_power"], recipe[side+"_index"])

    def add_multiplier(key):
        assert len(key) in (2, 3) and key == tuple(sorted(key)) and all(a in ANCHORS for a in key)
        if key in multipliers:
            return
        multipliers[key] = aliases.get(key)
        if key in aliases:
            add_original(*aliases[key])
        elif len(key) == 2:
            for index in key:
                add_original(1, index)
        else:
            add_multiplier(key[:2])
            add_original(1, key[2])

    for index in range(1506):
        add_original(6, index)
    for power in (7, 8):
        for row in selected799[power]:
            recipe = row["recipe"]
            assert recipe["right_power"] == 6 and 0 <= recipe["right_index"] < 1506
            original = bases[6][recipe["right_index"]]["recipe"]
            if power == 7:
                assert recipe["kind"] == "product" and recipe["left_power"] == 1
                key = (recipe["left_index"], original["left_index"])
            else:
                assert recipe["kind"] == "triple_product" and recipe["anchor_powers"] == [1, 1]
                assert len(recipe["anchor_indices"]) == 2
                key = tuple(recipe["anchor_indices"])+(original["left_index"],)
            add_multiplier(tuple(sorted(key)))
            add_original(5, original["right_index"])
    assert len([key for key in multipliers if len(key) == 2]) <= 6
    assert len([key for key in multipliers if len(key) == 3]) <= 10

    for power, index in sorted(needed):
        if power == 6:
            continue
        name = "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"
        spec = inv786[name]
        if power == 5:
            assert plain_spec(idx786["basis_rows"][index]) == spec
        data = p786.stage(spec)
        assert data["recipe"] == bases[power][index]["recipe"]
        assert data["weight"] == 2*power and data["bound_qY"] == 128
        assert data["integer_scale"] == str(82**(2*power))
        assert data["original_R775_finite_coefficients_verified"] is True
        row_shape(data, 129, real=False)
        if power == 1:
            tail = idx800["tail_rows_in_original_order"][index]
            assert tail["file"] == "R800-original-M2-tail-row-"+str(index).zfill(4)+".json.gz"
            assert plain_spec(tail) == inv800[tail["file"]]
            value = p800.stage(tail)
            assert value["index"] == index and value["recipe"] == data["recipe"]
            assert value["weight"] == 2 and value["integer_scale"] == "6724"
            assert value["first_exponent"] == 129 and value["last_exponent_exclusive"] == 196
            assert value["original_R786_prefix"] == plain_spec(spec)
            assert value["all_new_original_mod739_coefficients_verified"] is True
            assert value["all_new_real_tangent_involutions_verified"] is True
            assert value["old_prefix_recomputed"] is False and value["old_prefix_bytes_modified"] is False
            row_shape(value, 67)
    for index in range(1506):
        recipe = bases[6][index]["recipe"]
        old, tail = idx795["basis_rows"][index], idx799six["basis_rows"][index]
        assert old["file"] == "R795-exact-power-6-row-"+str(index).zfill(4)+".json.gz"
        assert tail["file"] == "R799-original-power6-tail-row-"+str(index).zfill(4)+".json.gz"
        assert plain_spec(old) == inv795[old["file"]] and plain_spec(tail) == inv799[tail["file"]]
        data = p795.stage(old)
        assert data["index"] == index and data["recipe"] == recipe
        assert data["weight"] == 12 and data["integer_scale"] == str(82**12) and data["bound_qY"] == 81
        assert data["original_R775_finite_coefficients_verified"] is True
        assert data["all_original_phase_involutions_verified"] is True and data["averaging_used"] is False
        factors = data["original_R786_factor_rows"]
        assert len(factors) == 2
        for factor, power, j in zip(factors, (1, 5), (recipe["left_index"], recipe["right_index"])):
            name = "R786-exact-power-"+str(power)+"-row-"+str(j).zfill(4)+".json.gz"
            assert factor["power"] == power and factor["index"] == j and plain_spec(factor) == inv786[name]
            assert name in p786.selected
        row_shape(data, 82)
        data = p799.stage(tail)
        assert data["index"] == index and data["recipe"] == recipe
        assert data["weight"] == 12 and data["integer_scale"] == str(82**12)
        assert data["first_exponent"] == 82 and data["last_exponent_exclusive"] == 109
        assert data["old_R795_prefix"] == plain_spec(old)
        assert data["original_R775_mod739_tail_verified"] is True
        assert data["all_original_phase_involutions_verified"] is True
        assert data["old_prefix_recomputed"] is False and data["old_prefix_bytes_modified"] is False
        row_shape(data, 27)
    for power in (7, 8):
        for row in selected799[power]:
            assert plain_spec(row) == inv799[row["file"]]
            assert row["all_current_prime_coordinates_verified"] is True
            data = p799.stage(row)
            assert data["recipe"] == row["recipe"] and data["ordinary_power"] == power
            assert data["weight"] == 2*power and data["integer_scale"] == str(82**(2*power))
            assert data["bound_qY"] == FIRST[power]-1
            assert data["all_initial_modular_coordinates_verified"] is True
            assert data["all_original_phase_involutions_verified"] is True
            assert data["old_input_arithmetic_recomputed"] is False and data["unrequested_high_coefficients_generated"] is False
            row_shape(data, FIRST[power])
    for producer in producers.values():
        # Every explicitly pinned file is part of the active five-group carrier.
        for name in producer.spec["files"]:
            assert name in producer.selected, ("unused pinned input", producer.label, name)
    return {"required_original_power_row_counts": {
                str(power): sum(p == power for p, _ in needed) for power in range(1, 7)},
            "actual_anchor_multiplier_aliases": [
                {"anchor_multiset": list(key), "original_power_index_alias": list(value) if value else None}
                for key, value in sorted(multipliers.items())],
            "R799_final_selected_short_row_count": 1778+2050,
            "R795_original_power6_prefix_count": 1506, "R799_original_power6_tail_count": 1506,
            "all_sizes_sha256_original_schemas_and_parent_identities_verified": True,
            "original_recipe_graph_only_no_arithmetic_reexecution": True}


def prepare_inputs(item, out):
    specs = item["retained_artifacts"]
    assert set(specs) == LABELS
    inputs = out.parent/"retained"
    present = [(inputs/label/"full-outputs-manifest.json").exists() for label in LABELS]
    transferred = all(present)
    assert transferred or not any(present), "Partial unverified R801 input carrier"
    if transferred:
        producers = {label: Producer(label, specs[label], [inputs/label]) for label in sorted(LABELS)}
    else:
        downloaded = {}
        for label in ("R799", "R800", "R775", "R786"):
            directory = out.parent/("downloaded-"+label)
            download(specs[label], directory, require_complete=True)
            downloaded[label] = directory
        p799 = Producer("R799", specs["R799"], [downloaded["R799"]])
        for label in ("R775", "R786", "R795"):
            same_producer(p799.initial["job"]["retained_artifacts"][label], specs[label])
            same_producer(p799.tag["retained_artifacts"][label], specs[label])
        bundle_name = "R799-retained-producer-inputs.tar.gz"
        bundle = p799.bound(bundle_name)
        carried = out.parent/"R799-carried-original-inputs"
        extract_bundle(bundle, carried, specs, "R799")
        producers = {"R799": p799, "R800": Producer("R800", specs["R800"], [downloaded["R800"]]),
                     "R795": Producer("R795", specs["R795"], [carried/"R795"])}
        for label in ("R775", "R786"):
            # The parent carrier can supply old small metadata absent from an original ZIP.
            # Every accepted byte is still bound to that ORIGINAL producer manifest.
            producers[label] = Producer(label, specs[label], [carried/label, downloaded[label]])
    for parent in ("R795", "R799", "R800"):
        producer = producers[parent]
        for label, child in producer.tag["retained_artifacts"].items():
            if label in specs:
                same_producer(child, specs[label])
                same_producer(producer.initial["job"]["retained_artifacts"][label], specs[label])
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
        "all_inputs_from_same_core_active_R801_bundle": transferred,
        "fresh_original_producers_downloaded": [] if transferred else ["R799", "R800", "R775", "R786"],
        "R795_original_prefixes_transferred_from_bound_R799_parent_bundle": not transferred,
        "input_bundle": file_spec(out/INPUT_BUNDLE),
        "all_final_R799_selected_short_rows_retained_for_next_relation_consumer": True,
        "no_E1_or_seed_rows_in_this_active_bundle": True,
        "old_arithmetic_recomputed": False})
    return inputs


def restore_resume(item, out):
    previous = item.get("resume")
    if previous is None:
        return
    directory = out.parent/"downloaded-R801-continuation"
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

    initial, old_run = read(bound("public-actions-input.json")), read(bound("run-receipt.json"))
    assert initial["source_commit"] == old_run["source_commit"] == previous["source_commit"]
    assert str(old_run["workflow_run_id"]) == str(previous["run_id"])
    for key in ("result", "p", "core_sha256", "R801_proof_sha256", "R801_method_sha256",
                "retained_artifacts", "primary_new_intervals", "primary_frontiers",
                "auxiliary_max_exponent", "generate_additional_pencil_V3_tail"):
        assert initial["job"][key] == item[key], "Changed continuation identity: "+key
    bundle = bound(INPUT_BUNDLE)
    extract_bundle(bundle, out.parent/"retained", item["retained_artifacts"], "self")
    shutil.copyfile(bundle, out/INPUT_BUNDLE)
    count = 0
    for name in entries:
        if not (name.startswith("R801-") and name.endswith(".json.gz")) and name != FINAL:
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
        "completed_nonoverlapping_tail_segments_preserved": True,
        "all_R799_selected_prefixes_transferred_with_current_active_carrier": True,
        "completed_mathematical_stages_recomputed": False})


def output_manifest(out):
    artifact = "serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    rows = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name in ("full-outputs-manifest.json", REFERENCE):
            continue
        rows.append({"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path), "artifact": artifact,
                     "included_in_git": path.name in META and path.stat().st_size < 100_000})
    mp = out/"full-outputs-manifest.json"
    save(mp, {"result": RESULT, "files": rows, "temporary_active_checkpoint_artifact": artifact,
        "temporary_active_checkpoint_retention_days": 1,
        "reproducible_rows_certificates_or_input_bundles_in_git_or_release": False})
    save(out/REFERENCE, {"result": RESULT, "manifest_file": mp.name, "manifest_sha256": sha(mp),
        "manifest_bytes": mp.stat().st_size, "file_count": len(rows), "full_outputs_artifact": artifact,
        "manifest_in_git": mp.stat().st_size < 100_000})


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
        "publication_helper_sha256": sha(S/"p41_public_actions_recovery.py"),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "new_arithmetic": "only V6 q109..141, selected V7 q96..175, selected V8 q109..195 and missing recipe dependencies",
        "original_basis_reselected_or_prefixes_recomputed": False,
        "actual_original_function_polar_divisor_beta_eta_or_height_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41 and item["producer_inputs_pending"] is False
        assert sha(core) == item["core_sha256"]
        assert sha(proof) == item["R801_proof_sha256"] and sha(method) == item["R801_method_sha256"]
        assert sha(__file__) == item["wrapper_sha256"]
        assert sha(S/"R786_public_exact_power5_short_basis.py") == item["download_helper_sha256"]
        assert sha(S/"p41_public_actions_recovery.py") == item["publication_helper_sha256"]
        assert item["primary_new_intervals"] == {"6": [109, 142], "7": [96, 176], "8": [109, 196]}
        assert item["primary_frontiers"] == {str(p): list(stops) for p, stops in FRONTIERS.items()}
        assert item["auxiliary_max_exponent"] == 195 and item["generate_additional_pencil_V3_tail"] is False
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
                error = "Budget reached; complete exact disjoint tail segments retained for immediate continuation."
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                code = 124
    except Exception as exception:
        error = type(exception).__name__+": "+str(exception)
    rp = out/"core-receipt.json"
    receipt = read(rp) if rp.exists() else {"complete": False}
    complete = code == 0 and receipt.get("complete") is True
    save(out/"run-receipt.json", {"result": RESULT, "p": 41, "complete": complete,
        "process_exit_code": code, "error": error, "source_commit": source,
        "workflow_run_id": os.environ["GITHUB_RUN_ID"], "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "execution_environment": "public-repository-github-actions",
        "core_receipt_sha256": sha(rp) if rp.exists() else None,
        "actual_original_selected_long_tails_completed": complete,
        "old_coefficients_recomputed_or_basis_reselected": False,
        "actual_original_function_polar_divisor_beta_eta_or_height_computed": False,
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
    assert cert["primary_dimensions"] == {"6": 1506, "7": 1778, "8": 2050}
    assert cert["primary_new_intervals"] == item["primary_new_intervals"]
    assert cert["actual_primary_frontiers"] == {str(p): list(stops) for p, stops in FRONTIERS.items()}
    for key in ("all_extended_original_power2_to6_tails_match_original_mod739_reference",
                "all_new_rows_have_full_original_phase_involution_checks",
                "all_selected_R799_short_rows_retained_for_the_next_consumer"):
        assert cert[key] is True
    for key in ("old_coefficients_recomputed", "ordinary_basis_reselected",
                "original_power6_coefficients_after141_generated",
                "primary_power7_after175_or_power8_after195_generated",
                "new_E1_M2_Laurent_Dixon_function_polar_divisor_eta_or_height_computed"):
        assert cert[key] is False

    def output_stage(spec):
        assert Path(spec["file"]).name == spec["file"]
        path = out/spec["file"]
        assert path.stat().st_size == spec["bytes"] and sha(path) == spec["sha256"]
        data = read(path)
        assert data["complete"] is True
        matching_configuration(data["configuration"], item)
        return data

    inventory = output_stage(cert["stage_manifest"])
    entries = {row["file"]: plain_spec(row) for row in inventory["files"]}
    assert len(entries) == len(inventory["files"])
    tail_headers = {}
    for name, spec in entries.items():
        assert name.startswith("R801-") and name.endswith(".json.gz")
        data = output_stage(spec)
        if not name.startswith("R801-tail-"):
            continue
        key, power = data["node_key"], data["ordinary_power"]
        first, stop = data["first_exponent"], data["last_exponent_exclusive"]
        assert 2 <= power <= 8 and 0 <= first < stop <= 196
        assert data["weight"] == 2*power and data["integer_scale"] == str(82**(2*power))
        assert data["node_fingerprint"] == fingerprint(data["node_identity"])
        assert data["node_identity"]["node_key"] == key and data["node_identity"]["ordinary_power"] == power
        assert data["all_original_phase_involutions_verified"] is True
        assert data["old_coefficients_recomputed"] is False
        assert data["original_prefix_bytes_modified"] is False
        assert data["coefficients_outside_this_missing_interval_generated"] is False
        if key.startswith("o"):
            assert first >= (109 if power == 6 else 129)
            assert stop <= (142 if power == 6 else 196)
            assert data["original_R775_mod739_reference_verified"] is True
        elif key.startswith("n"):
            assert power in (7, 8) and first >= FIRST[power] and stop <= FRONTIERS[power][-1]
            assert data["original_R775_mod739_reference_verified"] is None
        else:
            assert key.startswith("a") and power in (2, 3)
            assert data["original_R775_mod739_reference_verified"] is None
        row_shape(data, stop-first)
        tail_headers[name] = {k: data[k] for k in ("node_key", "node_fingerprint", "node_identity",
            "first_exponent", "last_exponent_exclusive", "previous_segments", "source_dependencies")}

    for key in ("dependency_plan", "auxiliary_coverage_index", "original_prefix_retention_index"):
        assert plain_spec(cert[key]) == entries[cert[key]["file"]]
    plan = output_stage(cert["dependency_plan"])
    nodes = {node["node_key"]: node for node in plan["nodes"]}
    assert len(nodes) == len(plan["nodes"])
    assert plan["all_original_recipe_valuations_verified_from_certified_old_prefixes"] is True
    assert plan["old_rows_or_basis_selection_recomputed"] is False
    assert plan["flattened_primary_7_8_do_not_require_original_6_after_141"] is True
    for power in (6, 7, 8):
        target = plan["primary_targets"][str(power)]
        assert len(target) == len(set(target)) == DIMS[power]
        prefix = "o06-i" if power == 6 else "n"+str(power).zfill(2)+"-i"
        assert target == [prefix+str(i).zfill(4) for i in range(DIMS[power])]

    retained_root = out.parent/"retained"
    producers = {label: Producer(label, item["retained_artifacts"][label], [retained_root/label])
                 for label in sorted(LABELS)}
    seen_sources = set()

    def check_source(source):
        spec = plain_spec(source)
        label, name = source["producer"], source["file"]
        assert 0 <= source["first"] < source["stop"] <= 196
        if label == "R801":
            assert entries[name] == spec
            header = tail_headers[name]
            assert header["first_exponent"] == source["first"] and header["last_exponent_exclusive"] == source["stop"]
        else:
            assert label in LABELS
            producer = producers[label]
            assert plain_spec(producer.entries[name]) == spec
            if (label, name) not in seen_sources:
                producer.bound(name, spec)
                seen_sources.add((label, name))

    grouped = {}
    for name, header in tail_headers.items():
        key = header["node_key"]
        assert key in nodes and header["node_fingerprint"] == nodes[key]["node_fingerprint"]
        grouped.setdefault(key, []).append((header["first_exponent"], header["last_exponent_exclusive"], name))
    all_ledgers = {}
    for key, node in nodes.items():
        identity = {k: node[k] for k in ("node_key", "ordinary_power", "original_recipe", "factor_nodes",
                                         "integer_scale", "original_reference_index")}
        assert fingerprint(identity) == node["node_fingerprint"]
        assert node["integer_scale"] == str(82**(2*node["ordinary_power"]))
        ledger, stop = list(node["original_input_segments"]), 0
        for source in ledger:
            assert source["first"] == stop
            check_source(source)
            stop = source["stop"]
        assert stop == node["old_coverage_stop"]
        for first, last, name in sorted(grouped.get(key, [])):
            header = tail_headers[name]
            assert first == stop and header["previous_segments"] == ledger
            assert header["node_identity"] == identity
            assert [entry["node_key"] for entry in header["source_dependencies"]] == node["factor_nodes"]
            for dependency in header["source_dependencies"]:
                assert dependency["node_fingerprint"] == nodes[dependency["node_key"]]["node_fingerprint"]
                assert 0 <= dependency["required_stop"] <= 196
                for source in dependency["source_segments"]:
                    check_source(source)
            source = dict(entries[name], producer="R801", first=first, stop=last)
            ledger.append(source)
            stop = last
        all_ledgers[key] = ledger

    for power in (6, 7, 8):
        specs = cert["completed_frontier_indices"][str(power)]
        assert len(specs) == len(FRONTIERS[power])
        assert cert["basis_tail_indices"][str(power)] == specs[-1]
        for stop, spec in zip(FRONTIERS[power], specs):
            assert entries[spec["file"]] == plain_spec(spec)
            data = output_stage(spec)
            assert data["ordinary_power"] == power and data["dimension"] == len(data["basis_rows"]) == DIMS[power]
            assert data["new_first_exponent"] == FIRST[power] and data["coverage_stop"] == stop
            assert data["integer_scale"] == str(82**(2*power))
            assert data["all_rows_complete_through_this_frontier"] is True
            assert data["basis_reselected"] is False and data["old_prefix_recomputed"] is False
            assert [row["index"] for row in data["basis_rows"]] == list(range(DIMS[power]))
            assert [row["node_key"] for row in data["basis_rows"]] == plan["primary_targets"][str(power)]
            for row in data["basis_rows"]:
                node, ledger = nodes[row["node_key"]], all_ledgers[row["node_key"]]
                assert row["node_fingerprint"] == node["node_fingerprint"]
                assert row["original_recipe"] == node["original_recipe"]
                assert row["original_prefix_segments"] == node["original_input_segments"]
                assert row["new_tail_segments"] == [s for s in ledger if s["producer"] == "R801" and s["first"] < stop]
                assert row["new_tail_segments"] and row["new_tail_segments"][0]["first"] == FIRST[power]
                assert row["new_tail_segments"][-1]["stop"] == stop

    retained = output_stage(cert["original_prefix_retention_index"])
    assert retained["file_count"] == len(retained["files"])
    actual = {(row["producer"], row["file"]): plain_spec(row) for row in retained["files"]}
    expected = {(source["producer"], source["file"]): plain_spec(source)
                for node in nodes.values() for source in node["original_input_segments"]}
    assert actual == expected
    for label, name in actual:
        producers[label].bound(name, actual[(label, name)])
    for key in ("all_selected_R799_short_rows_included",
                "all_original_R795_and_R799_power6_prefix_segments_included",
                "all_required_R786_lower_power_prefixes_included",
                "next_relation_consumer_must_transfer_these_original_files_in_the_active_bundle"):
        assert retained[key] is True
    assert retained["prefix_bytes_modified"] is False
    auxiliary = output_stage(cert["auxiliary_coverage_index"])
    assert auxiliary["no_extra_pencil_V3_rows_requested"] is True
    assert auxiliary["only_actual_dependency_closure_extended"] is True
    assert {row["node_key"] for row in auxiliary["nodes"]} == {
        key for key, node in nodes.items() if node["ordinary_power"] <= 5}
    for row in auxiliary["nodes"]:
        ledger = all_ledgers[row["node_key"]]
        assert row["actual_coverage_stop"] == (ledger[-1]["stop"] if ledger else 0)
        assert row["new_tail_segments"] == [s for s in ledger if s["producer"] == "R801"]
    bundle = read(out/"retained-inputs-receipt.json")["input_bundle"]
    assert bundle["file"] == INPUT_BUNDLE and file_spec(out/INPUT_BUNDLE) == bundle
    return 0


def publish_small(item, out):
    if not (out/"full-outputs-manifest.json").exists():
        output_manifest(out)
    manifest = read(out/"full-outputs-manifest.json")
    publication = out.parent/"publication"
    publication.mkdir(parents=True, exist_ok=True)
    for row in manifest["files"]:
        if row["included_in_git"]:
            assert row["file"] in META and row["bytes"] < 100_000 and sha(out/row["file"]) == row["sha256"]
            shutil.copyfile(out/row["file"], publication/row["file"])
    shutil.copyfile(out/REFERENCE, publication/REFERENCE)
    if (out/"full-outputs-manifest.json").stat().st_size < 100_000:
        shutil.copyfile(out/"full-outputs-manifest.json", publication/"full-outputs-manifest.json")
    return publish(item, publication, artifact_prefix="serre-global")


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["compute", "verify", "publish"])
    mode = parser.parse_args().mode
    out = Path(os.environ["RUNNER_TEMP"])/"serre-global"/RESULT/"output"
    if mode == "compute":
        request = read(REQUEST)
        assert request["session"] == "serre-public-astra-20261115"
        return compute(request["job"], out)
    item = read(out/"public-actions-input.json")["job"]
    return verify(item, out) if mode == "verify" else publish_small(item, out)


if __name__ == "__main__":
    sys.exit(main())
