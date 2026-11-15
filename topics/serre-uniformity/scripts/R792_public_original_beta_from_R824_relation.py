#!/usr/bin/env python3
"""Public IO runner for one original beta point from a real R824 exact relation."""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import signal
import subprocess
import sys
import tarfile

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R792-public-original-beta-from-R824-request.json"
RESULT = "R792-original-beta-from-R824-relation"
FINAL = "p41-original-beta-from-R824-relation-certificate.json"
BUNDLE = "R792-R824-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
IO_NAME = "R824_public_original_global_polar_generators.py"
IO_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
ADAPTER_NAME = "R824_original_exact_relation_adapter.py"
ADAPTER_SHA = "5a6a100a561ce02350a5d538df908d4cca9575e21b251a848a3bfba9d3df1958"
FRAMEWORK_NAME = "R792_original_beta_composition.py"
FRAMEWORK_SHA = "7b7a5483e560f2d244092af486c8aed606b18c1f3557dddb3b850a290b4e343d"
CORE_NAME = "R792_original_beta_from_R824_relation.py"
CORE_SHA = "a8a33d32b19525896a137fcf02c3fbf07ced88207839e9c89f16c9c527e827bf"
METHOD_SHA = "68877a988f4df5dc3a7609ea46d4f40129d40af40b5467200456829df730d818"
PROOF_SHA = "75362e44da996c4c481b548816bfeb532f799bde47f63400bcc7791e0aa5f46b"
FIELD_SHA = "f196cb805d1ca91e8995866032a0a3ec3f96aac06e03b67a7c1f196fff759251"
LABELS = {"R735", "R775", "R786", "R790", "R791", "R824"}
SCALE5 = "13744803133596058624"
MODEL = "p41-original-CM-model-certificate.json"
MODEL_SHA = "752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574"
R786_CERT_SHA = "dc6c23568f80b861d839280846c3250063abdfb2716a20481779816bb7cd37d9"
R786_INDEX_SHA = "0bb7cfeda48d6759f1553dec74485a28dc16e31cf3d500a095963888973c9b35"
R791_CERT_SHA = "94429377ebd63ff8bdcb9fd1d9468fc2e28e981db2b10b8c494d15c05e073d46"
TANGENTS = "R791-original-twelve-CM-tangents.json.gz"
TANGENTS_SHA = "32be372f46560ce7cfc0af40666cdc32b39170bfc7b6ec32b92ea747a0629e7e"
HOM = "R791-original-Hom-Galois-matrices.json.gz"
HOM_SHA = "f3793ddc7680b718a4448d45587661182986a3558db346ad0a2c9031c8952183"
BASIS_FILES = {
    1: ("R775-basis-M2.json.gz", "51113988c90b301cb6117fec5c294b77110e1826bf00229b7993ba82144f5d3d"),
    2: ("R775-basis-power-2.json.gz", "734a61e967c51ba3c9cd93eaff1a81fba165600110abb941dfdbbeed41b6ebe4"),
    3: ("R775-basis-power-3.json.gz", "00361e5155c429de5c54b613b8a3cb46ac9530c554e1a812823748bb2bf5fe18"),
    4: ("R775-basis-power-4.json.gz", "85beb7662eee64f4eca9e205314a6625506e3041bea199985489c7cf1f62dd4e"),
    5: ("R775-basis-power-5.json.gz", "7aff6faa89a91649db5549bbf9360647534bff6f9586ce3f5963e322d33c30ba")}
DIMS = {1:146, 2:418, 3:690, 4:962, 5:1234}


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


assert sha(S/IO_NAME) == IO_SHA
assert sha(S/ADAPTER_NAME) == ADAPTER_SHA
loader = importlib.util.spec_from_file_location("R792_R824_frozen_IO", S/IO_NAME)
IO = importlib.util.module_from_spec(loader)
loader.loader.exec_module(IO)
loader = importlib.util.spec_from_file_location("R792_R824_relation_IO", S/ADAPTER_NAME)
adapter = importlib.util.module_from_spec(loader)
loader.loader.exec_module(adapter)
read, save, file_spec = IO.read, IO.save, IO.file_spec
plain, fingerprint, META = IO.plain, IO.fingerprint, IO.META


def guard():
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"


def check(item):
    assert item["result"] == RESULT and item["p"] == 41
    assert item["producer_inputs_pending"] is False
    assert set(item["retained_artifacts"]) == LABELS
    assert item["coarse_jet_order"] == 1
    assert item["core"] == CORE_NAME and item["core_sha256"] == sha(S/CORE_NAME) == CORE_SHA
    assert item["wrapper_sha256"] == sha(__file__)
    assert item["beta_framework"] == FRAMEWORK_NAME
    assert item["beta_framework_sha256"] == sha(S/FRAMEWORK_NAME) == FRAMEWORK_SHA
    assert item["relation_adapter"] == ADAPTER_NAME
    assert item["relation_adapter_sha256"] == sha(S/ADAPTER_NAME) == ADAPTER_SHA
    assert item["field_core_sha256"] == sha(S/item["field_core"]) == FIELD_SHA
    assert item["R792_proof_sha256"] == sha(IO.topic_path(item["proof"])) == PROOF_SHA
    assert item["relation_adapter_method_sha256"] == sha(IO.topic_path(item["method"])) == METHOD_SHA
    assert item["io_helper"] == IO_NAME and item["io_helper_sha256"] == IO_SHA
    assert sha(REPO/"README.md") == item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md") == item["readme_sha256"]["topic"]
    adapter.plain(item["relation_spec"])
    for source in item["retained_artifacts"].values():
        assert IO.H64.fullmatch(source["archive_sha256"])
        assert IO.H64.fullmatch(source["manifest_sha256"])
        assert IO.H64.fullmatch(source["core_sha256"])
        assert isinstance(source["artifact_id"], int) and source["artifact_id"] > 0


class Source(IO.Producer):
    """The true legacy R735/R791 schemas and the true completed R824 stage."""

    def __init__(self, label, item, directory, archive=None, relation_spec=None):
        self.label, self.item, self.directory, self.archive = label, item, Path(directory), archive
        self.directory.mkdir(parents=True, exist_ok=True)
        self.selected = {}
        mp = self.materialize(META[0], item["manifest_sha256"])
        self.manifest = read(mp)
        assert self.manifest["result"] == item["result"]
        self.files = {row["file"]: row for row in self.manifest["files"]}
        assert len(self.files) == len(self.manifest["files"])
        for row in self.files.values():
            IO.check_spec(row)
        run, core, initial = (self.raw(name) for name in META[1:])
        assert run["result"] == initial["result"] == item["result"]
        if "result" in core:
            assert core["result"] == item["result"]
        else:
            assert label == "R735", "Only the actual legacy R735 receipt omits result."
        assert str(run["workflow_run_id"]) == str(item["run_id"])
        assert run["source_commit"] == initial["source_commit"] == item["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert core["source_sha256"] == item["core_sha256"]
        if label == "R791":
            assert "core_receipt_sha256" not in run
            assert initial["job"]["core_sha256"] == item["core_sha256"]
        else:
            assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
            assert initial["core_sha256"] == item["core_sha256"]
        name = item.get("certificate_name")
        self.certificate, self.tag = None, None
        if name is None:
            assert label == "R824" and relation_spec is not None
            assert item["allow_completed_checkpoint"] is True and item["expected_conclusion"] == "failure"
            assert run["complete"] is False and core["complete"] is False
            assert run["process_exit_code"] in item["accepted_checkpoint_exit_codes"]
            assert run["process_exit_code"] != 0
            assert item["configuration_stage"] == relation_spec["file"]
            assert plain(self.files[relation_spec["file"]]) == plain(relation_spec)
            value = self.raw(relation_spec["file"])
            assert value["complete"] is True
            self.tag = value["configuration"]
        else:
            assert run["complete"] is True and run["process_exit_code"] == 0 and core["complete"] is True
            assert core["certificate_sha256"] == item["files"][name] == self.files[name]["sha256"]
            self.certificate = self.raw(name)
            assert self.certificate["complete"] is True
            if label == "R735":
                identity = self.certificate["identity"]
                assert identity["source_sha256"] == item["core_sha256"]
                assert identity["p"] == 41 and identity["python_flint"] == "0.9.0"
                assert self.certificate["original_b_not_a_replacement_twist"] is True
                assert self.files[name]["sha256"] == MODEL_SHA
            else:
                assert self.certificate["result"] == item["result"]
                self.tag = self.certificate["configuration"]
        if self.tag is not None:
            assert self.tag["source_sha256"] == item["core_sha256"] and self.tag["python_flint"] == "0.9.0"
        self.initial = initial

    def stage(self, entry):
        value = super().stage(entry)
        assert self.tag is not None
        return value


def select_sources(sources, item):
    assert set(sources) == LABELS
    model, recipes = sources["R735"], sources["R775"]
    r786, r790, r791, r824 = (sources[key] for key in ("R786", "R790", "R791", "R824"))
    assert model.files[MODEL]["sha256"] == MODEL_SHA
    assert r786.files[r786.item["certificate_name"]]["sha256"] == R786_CERT_SHA
    assert r791.files[r791.item["certificate_name"]]["sha256"] == R791_CERT_SHA
    adapter.same_producer(r790.tag["retained_artifacts"]["R775"], recipes.item)
    # R786 bound an earlier ended R775 prefix run.  Its five exact recipe
    # files are reused byte-for-byte by the later successful R775 producer.
    # Preserve both source identities and compare the actual file SHAs below.
    basis = r786.stage(r786.certificate["basis_index"])
    assert r786.certificate["basis_index"]["sha256"] == R786_INDEX_SHA
    assert basis["dimension"] == 1234 and basis["bound_qY"] == 128
    assert basis["integer_scale"] == SCALE5
    assert [row["index"] for row in basis["basis_rows"]] == list(range(1234))
    recipe_data = {}
    for power, (name, digest) in BASIS_FILES.items():
        assert recipes.files[name]["sha256"] == digest
        data = recipes.stage(name)
        assert data["rank"] == DIMS[power] and len(data["basis"]) == DIMS[power]
        assert data["characteristic_zero_independence_certified_by_unit_reduction"] is True
        assert r786.tag["R775_completed_prefix_producer"]["files"][name] == digest
        recipe_data[power] = data
    cm = r790.certificate
    assert cm["p"] == 41 and cm["M2_dimension"] == 146 and cm["cm_jet_order"] == 5
    assert cm["original_psi_values_and_first_coarse_jets_verified"] is True
    assert cm["original_M2_scale"] == "6724" and cm["R786_power5_product_scale"] == SCALE5
    assert cm["distinct_retained_M2_seeds"] == 5 and cm["actual_reflected_seed_pairs"] == 10
    inventory = r790.stage(cm["stage_manifest"])
    entries = {row["file"]: plain(row) for row in inventory["files"]}
    assert inventory["M2_output_rows"] == cm["M2_output_rows"] and len(cm["M2_output_rows"]) == 146
    r790.prefetch(row["file"] for row in cm["M2_output_rows"])
    for index, entry in enumerate(cm["M2_output_rows"]):
        assert plain(entry) == entries[entry["file"]]
        assert entry["file"] == "R790-M2-CM-jet-"+str(index).zfill(4)+".json.gz"
        data = r790.stage(entry)
        assert data["index"] == index and data["integer_scale"] == "6724"
        assert data["original_recipe"] == recipe_data[1]["basis"][index]["recipe"]
        assert data["R786_power1_scale_preserved"] is True
        assert data["M2_recipe_source_sha256"] == BASIS_FILES[1][1]
        assert data["original_c1"] == 4424
        for key in ("value_K_1_zeta", "derivative_z_K_1_zeta"):
            assert len(data[key]) == 2 and all(len(pair) == 2 and int(pair[1]) > 0 for pair in data[key])
    stage_rows = {row["file"]: row for row in r791.certificate["stages"]}
    assert stage_rows[TANGENTS]["sha256"] == TANGENTS_SHA
    assert stage_rows[HOM]["sha256"] == HOM_SHA
    tangent, hom = r791.stage(stage_rows[TANGENTS]), r791.stage(stage_rows[HOM])
    assert tangent["original_map_index"] == 4 and tangent["original_map_degree"] == "1206"
    assert tangent["original_map_c1_tangent_nonzero"] is True and tangent["zero_flags"][4] is False
    assert hom["all_84_coordinates_verified"] is True and hom["all_three_actions_integral_unimodular"] is True
    for key in ("complex_conjugation_matrix", "zeta_matrix"):
        assert len(hom[key]) == 12 and all(len(row) == 12 for row in hom[key])
    relation = r824.stage(item["relation_spec"])
    r824.prefetch(row["file"] for row in relation["full_relation_verification_stages"])
    if r824.certificate is not None:
        r824.stage(r824.certificate["stage_manifest"])
        r824.stage(r824.certificate["generator_index"])
    actual = adapter.OriginalWeightFiveRelation(
        r824.directory, r824.item, item["relation_spec"], r786.item,
        r786.certificate["basis_index"], model.certificate["minimal_polynomial"])
    for entry in actual.selected.values():
        r824.materialize(entry["file"], entry["sha256"], entry["bytes"])
    return {"actual_R824_relation_receipt": actual.receipt(),
            "old_R786_basis_index": plain(r786.certificate["basis_index"]),
            "old_R790_M2_row_count": 146, "old_R775_recipe_dimensions": {str(k): v for k, v in DIMS.items()},
            "original_map_index": 4, "original_map_degree": 1206,
            "old_q_rows_CM_traces_or_Hom_matrices_recomputed": False,
            "new_field_arithmetic_performed_by_IO": False}


def expected_tag(item):
    return {
        "result": RESULT, "source_sha256": item["core_sha256"], "python_flint": "0.9.0",
        "R792_proof_sha256": PROOF_SHA, "relation_adapter_method_sha256": METHOD_SHA,
        "beta_framework_sha256": FRAMEWORK_SHA, "relation_adapter_sha256": ADAPTER_SHA,
        "field_core_sha256": FIELD_SHA, "coarse_jet_order": 1,
        "retained_artifacts": item["retained_artifacts"],
        "actual_R824_relation": plain(item["relation_spec"]),
        "original_map_index": 4, "original_map_degree": "1206",
        "original_R787_reserved_target_recomputed": False,
        "original_R824_denominator_and_content_reinserted": False}


def verify_bundle(path, groups, destination=None):
    expected = {(label, row["file"]): row for label, group in groups.items() for row in group["files"]}
    assert len(expected) == sum(len(group["files"]) for group in groups.values())
    seen = set()
    with tarfile.open(path, "r|gz") as archive:
        for member in archive:
            name = PurePosixPath(member.name)
            assert member.isfile() and len(name.parts) == 2 and not name.is_absolute()
            assert ".." not in name.parts and "\\" not in member.name
            key = tuple(name.parts)
            assert key in expected and key not in seen
            row = expected[key]
            assert member.size == row["bytes"]
            seen.add(key)
            target, temporary, output = None, None, None
            if destination is not None:
                target = Path(destination)/name
                target.parent.mkdir(parents=True, exist_ok=True)
                temporary = target.with_name(target.name+".download")
                output = temporary.open("wb")
            count, digest = 0, hashlib.sha256()
            try:
                with archive.extractfile(member) as raw:
                    for block in iter(lambda: raw.read(4*1024*1024), b""):
                        count += len(block)
                        digest.update(block)
                        if output is not None:
                            output.write(block)
            finally:
                if output is not None:
                    output.close()
            assert count == row["bytes"] and digest.hexdigest() == row["sha256"]
            if temporary is not None:
                if target.exists():
                    assert file_spec(target) == plain(row)
                    temporary.unlink()
                else:
                    temporary.replace(target)
    assert seen == set(expected)
    return len(seen)


def input_bundle(out, sources):
    groups = {label: source.closure_receipt() for label, source in sorted(sources.items())}
    temporary = out/(BUNDLE+".tmp")
    with temporary.open("wb") as stream:
        with gzip.GzipFile(fileobj=stream, mode="wb", compresslevel=2, mtime=0) as compressed:
            with tarfile.open(fileobj=compressed, mode="w|") as archive:
                for label, source in sorted(sources.items()):
                    for name, path in sorted(source.selected.items()):
                        info = archive.gettarinfo(str(path), arcname=label+"/"+name)
                        assert info.isfile()
                        info.uid = info.gid = 0
                        info.uname = info.gname = ""
                        info.mtime = 0
                        with path.open("rb") as raw:
                            archive.addfile(info, raw)
    temporary.replace(out/BUNDLE)
    count = verify_bundle(out/BUNDLE, groups)
    return groups, file_spec(out/BUNDLE), count


def restore(item, out, retained):
    previous = item.get("resume")
    if previous is None:
        return None
    assert previous["result"] == RESULT and previous["core_sha256"] == CORE_SHA
    archive = IO.Archive(previous, out.parent/"resume-transfer", whole=True)
    try:
        directory = out.parent/"resume-metadata"
        directory.mkdir(parents=True, exist_ok=True)
        mp = archive.extract_bound(META[0], previous["manifest_sha256"], directory/META[0])
        manifest = read(mp)
        assert manifest["result"] == RESULT
        files = archive.verify_all(manifest)
        def old(name):
            row = files[name]
            return archive.extract_bound(name, row["sha256"], directory/name, row["bytes"])
        initial, run, core = (read(old(name)) for name in ("public-actions-input.json", "run-receipt.json", "core-receipt.json"))
        old_item = initial["job"]
        assert initial["source_commit"] == run["source_commit"] == previous["source_commit"]
        assert str(run["workflow_run_id"]) == str(previous["run_id"])
        assert core["source_sha256"] == initial["core_sha256"] == CORE_SHA
        assert run["core_receipt_sha256"] == files["core-receipt.json"]["sha256"]
        assert expected_tag(old_item) == expected_tag(item)
        receipt = read(old("retained-inputs-receipt.json"))
        assert receipt["configuration"] == expected_tag(item) and receipt["complete"] is True
        assert plain(receipt["bundle"]) == plain(files[BUNDLE])
        for label in LABELS:
            assert receipt["producers"][label]["identity"] == IO.identity(item["retained_artifacts"][label])
        count = verify_bundle(old(BUNDLE), receipt["producers"], retained)
        stages = []
        for name, row in files.items():
            if name.startswith("R792-") and name.endswith(".json.gz"):
                path = archive.extract_bound(name, row["sha256"], out/name, row["bytes"])
                value = read(path)
                assert value["complete"] is True and value["configuration"] == expected_tag(item)
                stages.append(plain(row))
        result = {"result": RESULT, "resumed": True, "previous": previous,
            "all_original_manifest_bytes_SHA_verified": len(files),
            "all_original_input_bundle_members_SHA_verified": count,
            "complete_stages_restored": stages, "archive": archive.receipt()}
        save(out/"resume-receipt.json", result)
        return result
    finally:
        archive.close()


def prepare(item, out):
    check(item)
    out.mkdir(parents=True, exist_ok=True)
    retained = out.parent/"retained"
    retained.mkdir(parents=True, exist_ok=True)
    resumed = restore(item, out, retained)
    sources, archives = {}, {}
    try:
        for label in sorted(LABELS):
            source_item = item["retained_artifacts"][label]
            archive = None
            if resumed is None:
                archive = IO.Archive(source_item, out.parent/("download-"+label), whole=False)
                archives[label] = archive
            sources[label] = Source(label, source_item, retained/label, archive, item["relation_spec"])
        schema = select_sources(sources, item)
        groups, bundle, count = input_bundle(out, sources)
        receipt = {"result": RESULT, "complete": True, "configuration": expected_tag(item),
            "producers": groups, "bundle": bundle, "file_count": count,
            "source_schema": schema,
            "source_transfers": {label: archive.receipt() for label, archive in archives.items()},
            "all_selected_source_members_and_new_bundle_members_SHA_verified": True,
            "new_field_arithmetic_performed_by_IO": False}
        save(out/"retained-inputs-receipt.json", receipt)
        if resumed is None:
            save(out/"resume-receipt.json", {"result": RESULT, "resumed": False})
        print("R792_R824_INPUT_REVIEW="+json.dumps({
            "actual_R824_relation": item["relation_spec"],
            "actual_R824_source_state": schema["actual_R824_relation_receipt"]["actual_source_state"],
            "original_selected_source_files": count, "bundle": bundle,
            "all_selected_source_and_bundle_SHA_verified": True,
            "synthetic_R787_relation_created": False,
            "new_field_arithmetic_performed_by_IO": False}), flush=True)
        return retained
    finally:
        for archive in archives.values():
            archive.close()


def output_manifest(out):
    for path in out.iterdir():
        if path.is_file() and path.name.endswith((".tmp", ".download", ".partial")):
            path.unlink()
    artifact = "serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    rows = [dict(file_spec(path), artifact=artifact, included_in_git=False)
            for path in sorted(out.iterdir()) if path.is_file() and path.name not in (META[0], REFERENCE)]
    assert not any(path.is_dir() for path in out.iterdir())
    save(out/META[0], {"result": RESULT, "files": rows,
        "temporary_active_checkpoint_artifact": artifact, "temporary_active_checkpoint_retention_days": 1,
        "reproducible_data_in_git_or_release": False})
    save(out/REFERENCE, {"result": RESULT, "manifest_file": META[0],
        "manifest_bytes": (out/META[0]).stat().st_size, "manifest_sha256": sha(out/META[0]),
        "file_count": len(rows), "full_outputs_artifact": artifact,
        "automatic_git_or_release_publication": False})


def compute(item, out):
    guard()
    check(item)
    out.mkdir(parents=True, exist_ok=True)
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    for name in (FINAL, "run-receipt.json", "core-receipt.json", META[0], REFERENCE):
        (out/name).unlink(missing_ok=True)
    save(out/"public-actions-input.json", {
        "result": RESULT, "source_repository": "Rogerhu12/math-research-public",
        "source_commit": source, "job": item, "core_sha256": CORE_SHA,
        "driver_sha256": sha(__file__), "beta_framework_sha256": FRAMEWORK_SHA,
        "relation_adapter_sha256": ADAPTER_SHA, "field_core_sha256": FIELD_SHA,
        "proof_sha256": PROOF_SHA, "method_sha256": METHOD_SHA, "io_helper_sha256": IO_SHA,
        "request_sha256": sha(REQUEST), "workflow_sha256": sha(REPO/item["workflow"]),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    code, error, process = 1, None, None
    try:
        retained = prepare(item, out)
        configuration_path = out.parent/"R792-R824-math-config.json"
        save(configuration_path, item)
        command = [sys.executable, str(S/item["core"]), "--config", str(configuration_path),
            "--proof", str(IO.topic_path(item["proof"])), "--method", str(IO.topic_path(item["method"])),
            "--field-core", str(S/item["field_core"]), "--retained", str(retained), "--output", str(out),
            "--budget-minutes", str(item["budget_minutes"])]
        def stop(signum, frame):
            if process is not None and process.poll() is None:
                process.send_signal(signum)
        signal.signal(signal.SIGTERM, stop)
        signal.signal(signal.SIGINT, stop)
        with (out/"core.log").open("w") as log:
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, text=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                error = "Outer wallclock limit reached; complete stages and the latest source-bound checkpoint retained."
                if process.poll() is None:
                    process.terminate()
                try:
                    process.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait()
                code = 124
    except BaseException as exc:
        error = type(exc).__name__+": "+str(exc)
        print("R792_R824_RUNNER_ERROR="+error, flush=True)
        code = 1
    finally:
        if not (out/"core-receipt.json").exists():
            save(out/"core-receipt.json", {
                "result": RESULT, "complete": False, "source_sha256": CORE_SHA,
                "runner_error": error, "process_exit_code": code,
                "complete_source_bound_stages_preserved": True})
        complete = code == 0 and (out/FINAL).exists() and read(out/"core-receipt.json")["complete"] is True
        receipt = {"result": RESULT, "source_commit": source,
            "workflow_run_id": os.environ["GITHUB_RUN_ID"], "workflow_run_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
            "process_exit_code": code, "complete": complete,
            "core_receipt_sha256": sha(out/"core-receipt.json"),
            "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "runner_error": error, "automatic_git_or_release_publication": False}
        save(out/"run-receipt.json", receipt)
        output_manifest(out)
        print("R792_R824_RUN_RECEIPT="+json.dumps(receipt, sort_keys=True), flush=True)
    return code


def verify(out):
    """Complete byte/source/schema review, without importing either arithmetic core."""
    out = Path(out)
    manifest = read(out/META[0])
    assert manifest["result"] == RESULT
    files = {row["file"]: row for row in manifest["files"]}
    assert len(files) == len(manifest["files"])
    assert {path.name for path in out.iterdir() if path.is_file()} == set(files) | {META[0], REFERENCE}
    for name, row in files.items():
        IO.check_spec(row)
        assert file_spec(out/name) == plain(row)
    ref = read(out/REFERENCE)
    assert ref["manifest_sha256"] == sha(out/META[0])
    assert ref["manifest_bytes"] == (out/META[0]).stat().st_size and ref["file_count"] == len(files)
    initial, run, core = (read(out/name) for name in ("public-actions-input.json", "run-receipt.json", "core-receipt.json"))
    item = initial["job"]
    assert initial["result"] == run["result"] == core["result"] == RESULT
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert initial["source_commit"] == run["source_commit"]
    assert initial["core_sha256"] == item["core_sha256"] == core["source_sha256"] == CORE_SHA
    assert initial["driver_sha256"] == item["wrapper_sha256"]
    assert initial["beta_framework_sha256"] == FRAMEWORK_SHA
    assert initial["relation_adapter_sha256"] == ADAPTER_SHA
    assert initial["proof_sha256"] == PROOF_SHA and initial["method_sha256"] == METHOD_SHA
    assert run["complete"] is True and run["process_exit_code"] == 0 and core["complete"] is True
    assert run["core_receipt_sha256"] == files["core-receipt.json"]["sha256"]
    assert core["certificate_sha256"] == files[FINAL]["sha256"]
    receipt = read(out/"retained-inputs-receipt.json")
    assert receipt["complete"] is True and receipt["configuration"] == expected_tag(item)
    assert set(receipt["producers"]) == LABELS
    assert plain(receipt["bundle"]) == plain(files[BUNDLE])
    retained = out.parent/"retained"
    count = verify_bundle(out/BUNDLE, receipt["producers"], retained)
    assert count == receipt["file_count"]
    sources = {label: Source(label, item["retained_artifacts"][label], retained/label,
                             relation_spec=item["relation_spec"]) for label in LABELS}
    schema = select_sources(sources, item)
    assert schema == receipt["source_schema"]
    for label, source in sources.items():
        group = receipt["producers"][label]
        assert group["identity"] == IO.identity(item["retained_artifacts"][label])
        assert {row["file"] for row in group["files"]} == set(source.selected)
    cert = read(out/FINAL)
    tag = expected_tag(item)
    assert cert["result"] == RESULT and cert["complete"] is True and cert["configuration"] == tag
    inventory_spec = cert["stage_manifest"]
    assert plain(inventory_spec) == plain(files[inventory_spec["file"]])
    inventory = read(out/inventory_spec["file"])
    assert inventory["complete"] is True and inventory["configuration"] == tag
    stages = {row["file"]: plain(row) for row in inventory["files"]}
    assert len(stages) == len(inventory["files"])
    assert {name for name in files if name.startswith("R792-") and name.endswith(".json.gz")} == set(stages) | {inventory_spec["file"]}
    def stage(entry):
        assert plain(entry) == stages[entry["file"]] == plain(files[entry["file"]])
        data = read(out/entry["file"])
        assert data["complete"] is True and data["configuration"] == tag
        return data
    for entry in stages.values():
        stage(entry)
    relation_receipt = stage(cert["relation_source_receipt"])
    for key, value in schema["actual_R824_relation_receipt"].items():
        assert relation_receipt[key] == value
    assert cert["actual_R824_relation"] == item["relation_spec"]
    assert cert["original_R824_free_column"] == relation_receipt["actual_free_column"]
    assert cert["original_y_ratio_preserved"] is True
    for key in ("original_R787_reserved_target_recomputed", "synthetic_R787_producer_or_relation_file_created",
                "original_R824_denominator_and_content_reinserted", "original_A_coordinate_lift_computed",
                "actual_heights_or_uniformity_computed"):
        assert cert[key] is False
    assert cert["actual_beta_C_computed"] is True and cert["actual_real_descent_image_computed"] is True
    assert cert["original_map_index"] == 4 and cert["original_map_degree"] == "1206"
    assert cert["original_M2_scale"] == "6724" and cert["original_power5_scale"] == SCALE5
    assert cert["original_h0_nonzero"] is True and cert["original_Galois_direction_input_verified"] is True
    jets = stage(cert["section_jet_stage"])
    assert jets["original_basis_rows"] == 1234 and jets["original_c1"] == 4424
    assert jets["derivative_order"] == 1 and jets["coarse_coordinate"] == "z=a-1"
    assert jets["original_M2_scale"] == "6724" and jets["original_power5_scale"] == SCALE5
    assert jets["division_by_M2_values_used"] is False
    assert jets["old_q_series_or_basis_or_CM_traces_recomputed"] is False
    assert jets["common_denominator_and_integer_content_reinserted"] is False
    point = stage(cert["point_stage"])
    assert point["point_status"] == cert["point_status"]
    assert point["common_zero_order"] == cert["common_zero_order"] in (0, 1)
    assert point["actual_beta_C_computed"] is True and point["actual_real_descent_image_computed"] is True
    assert point["original_A_coordinate_lift_computed"] is False and point["actual_heights_or_uniformity_computed"] is False
    assert point["quotient_derivative_independently_compared"] is cert["quotient_derivative_independently_compared"]
    if point["point_status"] == "finite":
        for key in ("original_elliptic_equation_verified", "original_Galois_direction_verified",
                    "real_descent_elliptic_equation_verified", "no_extra_c1_phase_or_base_translation"):
            assert point[key] is True
        assert point["quotient_derivative_independently_compared"] is (point["common_zero_order"] == 0)
        for key in ("x_original_L", "y_original_L", "u_original_Fb", "v_original_Fb",
                    "y_derivative_original_z", "x_real_descent_Fb", "y_real_descent_Fb"):
            assert key in point
    else:
        assert point["point_status"] == "infinity" and point["beta_C"] == point["real_descent_image"] == "O"
        assert point["original_y_pole_order"] == 3 and point["pole_order_from_original_nonzero_tangent"] is True
    summary = {"result": RESULT, "complete": True,
        "source_commit": initial["source_commit"], "workflow_run_id": run["workflow_run_id"],
        "whole_output_manifest_files_verified": len(files), "all_retained_input_bundle_members_verified": count,
        "complete_math_stages_verified": len(stages), "actual_R824_relation": item["relation_spec"],
        "actual_R824_free_column": cert["original_R824_free_column"],
        "actual_beta_C_computed": True, "actual_real_descent_image_computed": True,
        "point_status": point["point_status"], "common_zero_order": point["common_zero_order"],
        "original_A_coordinate_lift_computed": False, "actual_heights_or_uniformity_computed": False,
        "point_stage": cert["point_stage"], "certificate": file_spec(out/FINAL),
        "stage_manifest": inventory_spec, "core_seconds": cert["seconds"],
        "new_mathematical_arithmetic_executed_by_verifier": False}
    print("R792_R824_COMPLETE_IO_REVIEW="+json.dumps(summary, sort_keys=True, separators=(",", ":")), flush=True)
    return summary


def main():
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--prepare-only", action="store_true")
    args = parser.parse_args()
    if args.verify:
        verify(args.output)
        return 0
    item = read(REQUEST)["job"]
    if args.prepare_only:
        guard()
        prepare(item, args.output)
        return 0
    return compute(item, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
