#!/usr/bin/env python3
"""R787 same-core continuation with complete streamed IO review and compact lift history."""
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
import zipfile

from p41_public_actions_recovery import read, save, sha
from R786_public_exact_power5_short_basis import api, download, find_hash

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO / "topics/serre-uniformity"
REQUEST = TOPIC / "notes/R787-public-original-power5-relation-request.json"
RESULT = "R787-original-power5-function-relation"
FINAL = "p41-original-power5-function-relation-certificate.json"
REFERENCE = "full-outputs-manifest-reference.json"
INPUT_BUNDLE = "R787-retained-producer-inputs.tar.gz"
SMALL = {"public-actions-input.json", "retained-inputs-receipt.json",
         "resume-receipt.json", "run-receipt.json", "core-receipt.json"}


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Actual arithmetic belongs to public repository Actions.")


def topic_path(relative):
    path = Path(relative)
    assert not path.is_absolute() and ".." not in path.parts
    return TOPIC / path


def prepare_inputs(item, out):
    inputs = out.parent / "retained"
    records = []
    assert set(item["retained_artifacts"]) == {"R781", "R786"}
    for label, spec in item["retained_artifacts"].items():
        directory = out.parent / ("downloaded-" + label)
        target = inputs / label
        target.mkdir(parents=True, exist_ok=True)
        reused_transfer = (target / "full-outputs-manifest.json").exists()
        if reused_transfer:
            directory = target
            metadata = api("repos/Rogerhu12/math-research-public/actions/runs/" + spec["run_id"])
            assert metadata["head_sha"] == spec["source_commit"]
            assert metadata["status"] == "completed" and metadata["conclusion"] == "success"
        else:
            download(spec, directory, require_complete=True)
        mp = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
        manifest = read(mp)
        assert manifest["result"] == spec["result"]
        entries = {row["file"]: row for row in manifest["files"]}
        rp = find_hash(directory, "run-receipt.json", entries["run-receipt.json"]["sha256"])
        run = read(rp)
        assert run["source_commit"] == spec["source_commit"]
        assert run["workflow_run_id"] == spec["run_id"]
        assert run["complete"] is True and run["process_exit_code"] == 0
        cn = spec["certificate_name"]
        certificate_sha = spec["files"][cn]
        assert entries[cn]["sha256"] == certificate_sha
        cp = find_hash(directory, cn, certificate_sha)
        certificate = read(cp)
        assert certificate["complete"] is True and certificate["result"] == spec["result"]
        tag = certificate["configuration"]
        assert tag["source_sha256"] == spec["core_sha256"]
        assert tag["python_flint"] == "0.9.0"
        if label == "R786":
            assert certificate["exact_power5_basis_dimension"] == 1234
            assert certificate["exact_K_basis_prefix_bound_qY"] == 128
            assert certificate["basis_integer_scale"] == "13744803133596058624"
            assert certificate["all_original_R775_mod739_short_series_compared"] is True
            assert tag["R786_proof_sha256"] == item["R786_proof_sha256"]
            index_spec = certificate["basis_index"]
            assert entries[index_spec["file"]]["sha256"] == index_spec["sha256"]
            ip = find_hash(directory, index_spec["file"], index_spec["sha256"])
            assert ip.stat().st_size == index_spec["bytes"]
            index = read(ip)
            assert index["complete"] is True and index["configuration"] == tag
            assert index["dimension"] == 1234 and index["bound_qY"] == 128
            rows = index["basis_rows"]
            assert len(rows) == 1234 and [r["index"] for r in rows] == list(range(1234))
            for row in rows:
                assert entries[row["file"]]["sha256"] == row["sha256"]
                assert entries[row["file"]]["bytes"] == row["bytes"]
            needed = [index_spec["file"]] + [row["file"] for row in rows]
        else:
            assert certificate["original_map_index"] == 4
            assert certificate["original_map_degree"] == "1206"
            assert certificate["actual_cusp_order"] == 1
            assert certificate["normalized_Laurent_R_bound"] == 142
            assert certificate["all_original_real_tangent_phases_verified"] is True
            assert certificate["all_recurrence_coefficients_verified_exactly"] is True
            needed = ["R781-original-real-field-input.json.gz"]
            needed += ["R781-inverse-free-Laurent-" + str(n).zfill(3) + ".json.gz"
                       for n in range(130)]
        assert len(needed) == len(set(needed))
        for name in needed:
            row = entries[name]
            source = find_hash(directory, name, row["sha256"])
            assert source.stat().st_size == row["bytes"]
            data = read(source)
            assert data["complete"] is True and data["configuration"] == tag
            if source.resolve() != (target / name).resolve():
                shutil.copyfile(source, target / name)
        for source, name in ((mp, "full-outputs-manifest.json"), (cp, cn), (rp, "run-receipt.json")):
            if source.resolve() != (target / name).resolve():
                shutil.copyfile(source, target / name)
        records.append({"label": label, "producer": spec,
                        "producer_run_and_source_verified": True,
                        "original_artifact_digest_verified_on_this_download": not reused_transfer,
                        "inputs_from_verified_active_resume_bundle": reused_transfer,
                        "certificate_sha256": certificate_sha,
                        "complete_source_bound_files_copied": len(needed),
                        "all_copied_file_sizes_and_sha256_verified": True,
                        "source_inventory": "producer full-outputs-manifest.json"})
    save(out / "retained-inputs-receipt.json", {
        "artifact_groups": records, "completed_producer_mathematics_recomputed": False})
    bundle = out / INPUT_BUNDLE
    if not bundle.exists():
        with tarfile.open(bundle, "w:gz") as archive:
            for path in sorted(inputs.rglob("*")):
                if path.is_file():
                    archive.add(path, arcname=str(path.relative_to(inputs)), recursive=False)
    return inputs


def plain_spec(row):
    return {key: row[key] for key in ("file", "bytes", "sha256")}


def file_spec(path):
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def matching_configuration(tag, item):
    assert tag["result"] == RESULT and tag["source_sha256"] == item["core_sha256"]
    assert tag["python_flint"] == "0.9.0"
    assert tag["R786_proof_sha256"] == item["R786_proof_sha256"]
    assert tag["R787_method_sha256"] == item["R787_method_sha256"]
    assert tag["R781_field_core_sha256"] == item["field_core_sha256"]
    assert tag["retained_artifacts"] == item["retained_artifacts"]
    assert tag["original_map_index"] == 4 and tag["original_map_degree"] == "1206"
    assert tag["ordinary_power"] == 5 and tag["basis_dimension"] == 1234
    assert tag["qY_bound"] == 128 and tag["full_L_unknown_dimension_over_Q"] == 14
    assert tag["Laurent_exponents"] == [-1, 127] and tag["t_coordinates"] == 20
    assert tag["Schur_shape"] == [1326, 1214]
    assert tag["auxiliary_prime_start"] == item["auxiliary_prime_start"]
    assert tag["reconstruct_every_digits"] == item["reconstruct_every_digits"]
    assert tag["composite_modulus_matrix_inversion"] is False
    assert tag["completed_producer_arithmetic_recomputed"] is False


DIXON = re.compile(r"R787-prime-(\d+)-dixon-(\d{8})\.json\.gz")
HISTORY = "dixon-checkpoint-history.json"


def history_records(value):
    rows = value.get("checkpoints", []) if value is not None else []
    seen = {}
    for row in rows:
        name = row["file"]
        match = DIXON.fullmatch(name)
        assert match and row["prime"] == int(match[1]) and row["digits"] == int(match[2])
        assert row["bytes"] > 0 and re.fullmatch(r"[0-9a-f]{64}", row["sha256"])
        if name in seen:
            assert seen[name] == row
        seen[name] = row
    return seen


def checkpoint_record(row):
    match = DIXON.fullmatch(row["file"])
    assert match
    return dict(plain_spec(row), prime=int(match[1]), digits=int(match[2]))


def save_history(out, records, source=None):
    previous = read(out/HISTORY) if (out/HISTORY).exists() else None
    sources = list(previous.get("reviewed_sources", [])) if previous else []
    if source is not None and source not in sources:
        sources.append(source)
    save(out/HISTORY, {"result": RESULT, "checkpoints": [records[name] for name in sorted(records)],
        "reviewed_sources": sources, "history_contains_only_name_bytes_sha256_prime_digits": True,
        "old_full_lift_vectors_retained_as_history": False,
        "mathematical_checkpoint_contents_modified": False})


def stream_archive(spec, directory):
    metadata = api("repos/Rogerhu12/math-research-public/actions/runs/"+spec["run_id"])
    assert metadata["head_sha"] == spec["source_commit"] and metadata["status"] == "completed"
    if spec.get("expected_conclusion"):
        assert metadata["conclusion"] == spec["expected_conclusion"]
    artifact = api("repos/Rogerhu12/math-research-public/actions/artifacts/"+str(spec["artifact_id"]))
    assert artifact["name"] == spec["artifact_name"] and not artifact["expired"]
    assert artifact["workflow_run"]["id"] == int(spec["run_id"])
    assert artifact["workflow_run"]["head_sha"] == spec["source_commit"]
    assert artifact["digest"] == "sha256:"+spec["archive_sha256"]
    if "archive_bytes" in spec:
        assert artifact["size_in_bytes"] == spec["archive_bytes"]
    directory.mkdir(parents=True, exist_ok=True)
    archive = directory/"original-continuation.zip"
    if not archive.exists():
        temporary = archive.with_suffix(".zip.tmp")
        digest, count = hashlib.sha256(), 0
        command = ["gh", "api", "repos/Rogerhu12/math-research-public/actions/artifacts/"+
                   str(spec["artifact_id"])+"/zip"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            with temporary.open("wb") as output:
                for block in iter(lambda: process.stdout.read(4*1024*1024), b""):
                    output.write(block)
                    digest.update(block)
                    count += len(block)
            error = process.stderr.read().decode("utf-8", errors="replace")
            status = process.wait()
            if status:
                raise RuntimeError("Original artifact download failed: "+error[:2000])
            assert count == artifact["size_in_bytes"], ("actual ZIP bytes", count, artifact["size_in_bytes"])
            assert digest.hexdigest() == spec["archive_sha256"], "Actual streamed ZIP digest mismatch"
            temporary.replace(archive)
        finally:
            if process.poll() is None:
                process.kill()
                process.wait()
    else:
        assert archive.stat().st_size == artifact["size_in_bytes"] and sha(archive) == spec["archive_sha256"]
    return archive, {"artifact_id": spec["artifact_id"], "artifact_name": spec["artifact_name"],
        "bytes": archive.stat().st_size, "sha256": spec["archive_sha256"],
        "actual_streamed_archive_bytes_and_sha256_verified": True,
        "run_status": metadata["status"], "run_conclusion": metadata["conclusion"]}


def read_member_json(archive, info):
    with archive.open(info) as stream:
        return json.load(stream)


def streamed_original_outputs(spec, directory):
    archive_path, archive_record = stream_archive(spec, directory)
    retained = directory/"selected-output"
    retained.mkdir(parents=True, exist_ok=True)
    records = {}
    with zipfile.ZipFile(archive_path) as archive:
        infos = {}
        for info in archive.infolist():
            relative = Path(info.filename)
            assert not relative.is_absolute() and ".." not in relative.parts
            if info.is_dir():
                continue
            assert relative.name not in infos, "Ambiguous original artifact basename"
            assert ((info.external_attr >> 16) & 0o170000) != 0o120000
            infos[relative.name] = info
        assert "full-outputs-manifest.json" in infos
        raw_manifest = archive.read(infos["full-outputs-manifest.json"])
        assert hashlib.sha256(raw_manifest).hexdigest() == spec["manifest_sha256"]
        if "manifest_bytes" in spec:
            assert len(raw_manifest) == spec["manifest_bytes"]
        manifest = json.loads(raw_manifest)
        assert manifest["result"] == RESULT
        entries = {row["file"]: row for row in manifest["files"]}
        assert len(entries) == len(manifest["files"])
        assert all(Path(name).name == name for name in entries)
        if "manifest_file_count" in spec:
            assert len(entries) == spec["manifest_file_count"]
        assert set(infos) == set(entries)|{"full-outputs-manifest.json", REFERENCE}
        run = read_member_json(archive, infos["run-receipt.json"])
        initial = read_member_json(archive, infos["public-actions-input.json"])
        receipt = (read_member_json(archive, infos["core-receipt.json"])
                   if "core-receipt.json" in infos else None)
        assert run["result"] == initial["result"] == RESULT
        assert run["source_commit"] == initial["source_commit"] == spec["source_commit"]
        assert str(run["workflow_run_id"]) == str(spec["run_id"])
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["core_sha256"] == spec["core_sha256"]
        if receipt is not None:
            assert receipt["result"] == RESULT
            assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
            assert receipt["source_sha256"] == initial["core_sha256"]
            if spec.get("expected_conclusion") == "failure":
                assert run["complete"] is False and receipt["complete"] is False
        else:
            # The wrapper can finish its manifest after its outer timeout kills
            # the core before the core writes a receipt.  This is not success.
            assert spec.get("expected_conclusion") == "failure"
            assert run["complete"] is False and run["process_exit_code"] == 124
            assert run["core_receipt_sha256"] is None
        success_inventory = False
        if FINAL in infos:
            final = read_member_json(archive, infos[FINAL])
            success_inventory = final.get("complete") is True
        if receipt is None:
            assert success_inventory is False
        latest = {}
        for name, row in entries.items():
            match = DIXON.fullmatch(name)
            if match:
                record = checkpoint_record(row)
                records[name] = record
                prime = record["prime"]
                if prime not in latest or record["digits"] > latest[prime]["digits"]:
                    latest[prime] = record
        wanted = {name for name in entries if not DIXON.fullmatch(name)}
        wanted.update(records if success_inventory else (row["file"] for row in latest.values()))
        verified_bytes, verified_files = 0, 0
        for name, info in infos.items():
            expected = entries.get(name)
            if expected is not None:
                assert info.file_size == expected["bytes"]
            keep = name in wanted or name in ("full-outputs-manifest.json", REFERENCE)
            path = retained/name
            temporary = path.with_name(path.name+".tmp")
            output = temporary.open("wb") if keep else None
            digest, count = hashlib.sha256(), 0
            try:
                with archive.open(info) as stream:
                    for block in iter(lambda: stream.read(4*1024*1024), b""):
                        digest.update(block)
                        count += len(block)
                        if output is not None:
                            output.write(block)
            finally:
                if output is not None:
                    output.close()
            assert count == info.file_size
            if expected is not None:
                assert digest.hexdigest() == expected["sha256"], name
                verified_files += 1
                verified_bytes += count
            elif name == "full-outputs-manifest.json":
                assert digest.hexdigest() == spec["manifest_sha256"]
            if keep:
                temporary.replace(path)
        assert verified_files == len(entries)
        reference = read(retained/REFERENCE)
        assert reference["result"] == RESULT and reference["manifest_sha256"] == spec["manifest_sha256"]
        assert reference["manifest_bytes"] == len(raw_manifest) and reference["file_count"] == len(entries)
    # Every ZIP member has been read completely and every manifest entry has passed.
    archive_path.unlink()
    return retained, entries, initial, run, records, latest, success_inventory, {
        "archive": archive_record, "original_manifest_sha256": spec["manifest_sha256"],
        "original_manifest_file_count": verified_files, "original_manifest_total_bytes": verified_bytes,
        "zip_regular_member_count": len(infos),
        "all_manifest_members_streamed_and_size_sha256_verified": True,
        "source_core_receipt_present": receipt is not None,
        "source_missing_core_receipt_is_failed_outer_timeout": receipt is None,
        "certificate_inventory_present_and_preserved": success_inventory,
        "archive_removed_only_after_complete_hash_review": True}


def restore_bundle(bundle, target, specs):
    target.mkdir(parents=True, exist_ok=True)
    seen = {}
    with tarfile.open(bundle, "r:gz") as archive:
        for member in archive:
            relative = Path(member.name)
            assert member.isfile() and not relative.is_absolute() and ".." not in relative.parts
            assert len(relative.parts) == 2 and relative.parts[0] in ("R781", "R786")
            assert member.name not in seen
            path = target/relative
            path.parent.mkdir(parents=True, exist_ok=True)
            temporary = path.with_name(path.name+".tmp")
            digest, count = hashlib.sha256(), 0
            with archive.extractfile(member) as stream, temporary.open("wb") as output:
                for block in iter(lambda: stream.read(4*1024*1024), b""):
                    digest.update(block)
                    count += len(block)
                    output.write(block)
            assert count == member.size
            if path.exists():
                assert path.stat().st_size == count and sha(path) == digest.hexdigest()
                temporary.unlink()
            else:
                temporary.replace(path)
            seen[member.name] = {"file": relative.name, "bytes": count, "sha256": digest.hexdigest()}
    groups = []
    for label, spec in specs.items():
        manifest_name = label+"/full-outputs-manifest.json"
        assert seen[manifest_name]["sha256"] == spec["manifest_sha256"]
        manifest = read(target/manifest_name)
        assert manifest["result"] == spec["result"]
        entries = {row["file"]: row for row in manifest["files"]}
        assert len(entries) == len(manifest["files"])
        names = [name for name in seen if name.startswith(label+"/")]
        for name in names:
            row = seen[name]
            if name != manifest_name:
                assert row == plain_spec(entries[row["file"]]), ("original bundle member", name)
        run = read(target/label/"run-receipt.json")
        cert = read(target/label/spec["certificate_name"])
        assert run["result"] == spec["result"] and run["complete"] is True and run["process_exit_code"] == 0
        assert str(run["workflow_run_id"]) == str(spec["run_id"]) and run["source_commit"] == spec["source_commit"]
        assert cert["result"] == spec["result"] and cert["complete"] is True
        assert cert["configuration"]["source_sha256"] == spec["core_sha256"]
        assert seen[label+"/"+spec["certificate_name"]]["sha256"] == spec["files"][spec["certificate_name"]]
        if label == "R781":
            expected = {"full-outputs-manifest.json", "run-receipt.json", spec["certificate_name"],
                        "R781-original-real-field-input.json.gz"}
            expected.update("R781-inverse-free-Laurent-"+str(n).zfill(3)+".json.gz" for n in range(130))
        else:
            index_spec = cert["basis_index"]
            index = read(target/label/index_spec["file"])
            assert file_spec(target/label/index_spec["file"]) == plain_spec(index_spec)
            assert index["complete"] is True and index["configuration"] == cert["configuration"]
            assert index["dimension"] == 1234 and len(index["basis_rows"]) == 1234
            expected = {"full-outputs-manifest.json", "run-receipt.json", spec["certificate_name"], index_spec["file"]}
            expected.update(row["file"] for row in index["basis_rows"])
        assert {Path(name).name for name in names} == expected
        groups.append({"label": label, "run_id": spec["run_id"], "source_commit": spec["source_commit"],
            "core_sha256": spec["core_sha256"], "manifest_sha256": spec["manifest_sha256"],
            "certificate_sha256": spec["files"][spec["certificate_name"]], "file_count": len(names),
            "all_members_checked_against_original_manifest": True})
    assert len(seen) == 1372 and {row["label"]: row["file_count"] for row in groups} == {"R781": 134, "R786": 1238}
    return {"input_bundle": file_spec(bundle), "member_count": len(seen), "groups": groups,
        "all_original_bundle_member_bytes_and_sha256_verified": True}


def latest_checkpoint_summary(out, latest, records, item):
    summary = []
    for prime, record in sorted(latest.items()):
        path = out/record["file"]
        data = read(path)
        assert data["complete"] is True
        matching_configuration(data["configuration"], item)
        assert data["prime"] == prime and data["digits"] == record["digits"]
        assert data["full_original_modular_relations_verified"] is True
        assert len(data["A_L_coordinates"]) == 1234 and all(len(row) == 14 for row in data["A_L_coordinates"])
        assert len(data["C_L_coordinates"]) == 1214 and all(len(row) == 14 for row in data["C_L_coordinates"])
        previous = data.get("previous_completed_checkpoint_sha256")
        if record["digits"] > 1:
            name = "R787-prime-"+str(prime)+"-dixon-"+str(record["digits"]-1).zfill(8)+".json.gz"
            assert name in records and records[name]["sha256"] == previous
        stem = "R787-prime-"+str(prime)
        selection, chart = read(out/(stem+"-selection.json.gz")), read(out/(stem+"-chart.json.gz"))
        for row in (selection, chart):
            assert row["complete"] is True
            matching_configuration(row["configuration"], item)
            assert row["prime"] == prime
        assert data["chart_sha256"] == sha(out/(stem+"-chart.json.gz"))
        assert selection["all_14_L_branches_distinct"] is True
        assert len(selection["roots_B_s"]) == 14
        branch_records = []
        for branch in range(14):
            branch_path = out/(stem+"-branch-"+str(branch).zfill(2)+".json.gz")
            row = read(branch_path)
            assert row["complete"] is True
            matching_configuration(row["configuration"], item)
            assert row["prime"] == prime and row["branch"] == branch
            assert row["chart_sha256"] == data["chart_sha256"]
            assert row["actual_Schur_rank"] == chart["actual_modular_rank"]
            assert row["all_2560_original_uncleared_rows_verified"] is True
            branch_records.append({"branch": branch, "actual_Schur_rank": row["actual_Schur_rank"],
                "actual_selected_minor_det_mod_prime": row["selected_minor_det_mod_prime"],
                "file": file_spec(branch_path)})
        summary.append({"prime": prime, "actual_modular_Schur_rank": chart["actual_modular_rank"],
            "actual_complete_branch_count": len(branch_records), "branches": branch_records,
            "latest_complete_Dixon_digits": record["digits"], "latest_checkpoint": plain_spec(record),
            "previous_completed_checkpoint_sha256": previous,
            "original_chart_sha256": data["chart_sha256"],
            "full_original_modular_relations_verified": True})
        del data
    return summary


def restore_resume(item, out):
    spec = item.get("resume")
    if spec is None:
        return
    directory = out.parent/"reviewed-R787-continuation"
    selected, entries, initial, run, records, latest, success_inventory, review = streamed_original_outputs(spec, directory)
    for key in ("result", "p", "core", "core_sha256", "field_core", "field_core_sha256", "method",
                "R787_method_sha256", "proof", "R786_proof_sha256", "auxiliary_prime_start",
                "reconstruct_every_digits", "retained_artifacts"):
        assert initial["job"][key] == item[key], ("Changed mathematics on continuation", key)
    assert initial["core_sha256"] == initial["job"]["core_sha256"] == item["core_sha256"]
    if (selected/HISTORY).exists():
        if not (out/HISTORY).exists():
            shutil.copyfile(selected/HISTORY, out/HISTORY)
        previous_records = history_records(read(selected/HISTORY))
        for name, record in previous_records.items():
            if name in records:
                assert records[name] == record
            records[name] = record
    assert INPUT_BUNDLE in entries
    bundle = selected/INPUT_BUNDLE
    assert file_spec(bundle) == plain_spec(entries[INPUT_BUNDLE])
    bundle_review = restore_bundle(bundle, out.parent/"retained", item["retained_artifacts"])
    shutil.copyfile(bundle, out/INPUT_BUNDLE)
    copied, full_lifts = 0, []
    for path in sorted(selected.iterdir()):
        name = path.name
        if not (name.startswith("R787-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        row = entries[name]
        assert file_spec(path) == plain_spec(row)
        data = read(path)
        assert data["complete"] is True
        matching_configuration(data["configuration"], item)
        destination = out/name
        if destination.exists():
            assert file_spec(destination) == plain_spec(row)
        else:
            shutil.copyfile(path, destination)
        copied += 1
        if DIXON.fullmatch(name):
            full_lifts.append(plain_spec(row))
        del data
    assert copied
    source_record = {"run_id": spec["run_id"], "source_commit": spec["source_commit"],
        "artifact_id": spec["artifact_id"], "archive_sha256": spec["archive_sha256"],
        "manifest_sha256": spec["manifest_sha256"], "all_original_outputs_verified": True}
    save_history(out, records, source_record)
    latest_summary = latest_checkpoint_summary(out, latest, records, item)
    review.update({"result": RESULT, "source": source_record, "same_exact_core_sha256": item["core_sha256"],
        "same_original_proof_method_field_core_and_producer_inputs": True,
        "complete_mathematical_files_restored": copied,
        "actual_prime_branch_and_latest_lift": latest_summary,
        "complete_lift_history_count": len(records), "full_lift_vectors_restored": full_lifts,
        "old_full_lifts_discarded_only_after_complete_original_hash_review": len(records)-len(full_lifts),
        "original_input_bundle_review": bundle_review,
        "mathematical_core_imported_during_restore": False,
        "completed_mathematical_stages_recomputed": False,
        "restored_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    save(out/"resume-receipt.json", review)
    print("RESTORE_REVIEW="+json.dumps(review, sort_keys=True, separators=(",", ":")), flush=True)
    # The reviewed selected transport copy is redundant after the exact continuation copy exists.
    shutil.rmtree(selected)


def prune_failed_lifts(item, out):
    """Only remove superseded complete lift vectors; never invalidate a successful certificate inventory."""
    if (out/FINAL).exists() and read(out/FINAL).get("complete") is True:
        return
    run = read(out/"run-receipt.json") if (out/"run-receipt.json").exists() else None
    if run is not None and run.get("complete") is True:
        return
    records = history_records(read(out/HISTORY)) if (out/HISTORY).exists() else {}
    groups = {}
    for path in sorted(out.glob("R787-prime-*-dixon-*.json.gz")):
        match = DIXON.fullmatch(path.name)
        assert match
        data = read(path)
        assert data["complete"] is True
        matching_configuration(data["configuration"], item)
        record = checkpoint_record(file_spec(path))
        assert data["prime"] == record["prime"] and data["digits"] == record["digits"]
        assert data["full_original_modular_relations_verified"] is True
        if path.name in records:
            assert records[path.name] == record
        records[path.name] = record
        groups.setdefault(record["prime"], []).append((record, data.get("previous_completed_checkpoint_sha256")))
        del data
    keep, remove = [], []
    for prime, rows in groups.items():
        rows.sort(key=lambda row: row[0]["digits"])
        for record, previous in rows:
            if record["digits"] > 1:
                prior = "R787-prime-"+str(prime)+"-dixon-"+str(record["digits"]-1).zfill(8)+".json.gz"
                assert prior in records and records[prior]["sha256"] == previous
        keep.append(rows[-1][0])
        remove.extend(row[0] for row in rows[:-1])
    save_history(out, records)
    # History is durable in the same next artifact before any original vector is removed.
    for record in remove:
        path = out/record["file"]
        assert file_spec(path) == plain_spec(record)
        path.unlink()
    save(out/"dixon-output-compaction-receipt.json", {"result": RESULT,
        "only_failed_run_without_success_certificate_compacted": True,
        "same_exact_core_sha256": item["core_sha256"], "latest_complete_lifts_retained": keep,
        "superseded_complete_lift_count": len(remove),
        "superseded_complete_lift_bytes": sum(row["bytes"] for row in remove),
        "all_discarded_name_bytes_sha256_retained_in": HISTORY,
        "non_Dixon_complete_stages_removed": False, "mathematical_checkpoint_contents_modified": False})


def output_manifest(out):
    item = read(out / "public-actions-input.json")["job"]
    prune_failed_lifts(item, out)
    artifact = ("serre-global-" + RESULT + "-" + os.environ["GITHUB_RUN_ID"] + "-"
                + os.environ["GITHUB_RUN_ATTEMPT"])
    rows = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name in ("full-outputs-manifest.json", REFERENCE):
            continue
        rows.append({"file": path.name, "bytes": path.stat().st_size,
                     "sha256": sha(path), "artifact": artifact,
                     "included_in_git": False,
                     "eligible_for_reviewed_small_metadata": path.name in SMALL and path.stat().st_size < 100_000})
    mp = out / "full-outputs-manifest.json"
    save(mp, {"result": RESULT, "files": rows,
              "temporary_active_checkpoint_artifact": artifact,
              "reproducible_relation_tables_in_git_or_release": False,
              "temporary_active_checkpoint_retention_days": 1})
    save(out / REFERENCE, {"result": RESULT, "manifest_file": mp.name,
                          "manifest_sha256": sha(mp), "manifest_bytes": mp.stat().st_size,
                          "file_count": len(rows), "full_outputs_artifact": artifact,
                          "manifest_in_git": False,
                          "automatic_git_or_release_publication": False})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core, field_core = S / item["core"], S / item["field_core"]
    method, proof = topic_path(item["method"]), topic_path(item["proof"])
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out / "public-actions-input.json", {
        "result": RESULT, "p": 41, "source_repository": "Rogerhu12/math-research-public",
        "source_commit": source, "job": item, "core_sha256": sha(core),
        "field_core_sha256": sha(field_core), "method_sha256": sha(method),
        "proof_sha256": sha(proof), "driver_sha256": sha(__file__),
        "request_sha256": sha(REQUEST), "root_readme_sha256": sha(REPO / "README.md"),
        "topic_readme_sha256": sha(TOPIC / "README.md"),
        "publication_helper_sha256": sha(S / "p41_public_actions_recovery.py"),
        "download_helper_sha256": sha(S / "R786_public_exact_power5_short_basis.py"),
        "workflow_sha256": sha(REPO / item["workflow"]),
        "retained_artifacts": item["retained_artifacts"], "resume": item.get("resume"),
        "budget_minutes": item["budget_minutes"],
        "arithmetic": "original L relation from completed original power5 basis and Laurent stages",
        "run_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/" + os.environ["GITHUB_RUN_ID"],
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "actual_y_map_claimed_before_run": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert not item.get("producer_inputs_pending", True)
        assert sha(core) == item["core_sha256"]
        assert sha(__file__) == item["wrapper_sha256"]
        assert sha(S / "R786_public_exact_power5_short_basis.py") == item["download_helper_sha256"]
        assert sha(S / "p41_public_actions_recovery.py") == item["io_helper_sha256"]
        assert sha(field_core) == item["field_core_sha256"]
        assert sha(method) == item["R787_method_sha256"]
        assert sha(proof) == item["R786_proof_sha256"]
        restore_resume(item, out)
        inputs = prepare_inputs(item, out)
        config = out.parent / "job-config.json"
        save(config, item)
        command = [sys.executable, "-u", str(core), "--retained", str(inputs),
                   "--output", str(out), "--config", str(config), "--proof", str(proof),
                   "--method", str(method), "--field-core", str(field_core),
                   "--budget-minutes", str(item["budget_minutes"])]
        with (out / "public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT,
                                       start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"] * 60 + 120)
            except subprocess.TimeoutExpired:
                error = "Budget reached; source-bound complete stages retained for continuation."
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                code = 124
    except Exception as exception:
        error = type(exception).__name__ + ": " + str(exception)
    rp = out / "core-receipt.json"
    receipt = read(rp) if rp.exists() else {"complete": False}
    complete = code == 0 and receipt.get("complete") is True
    save(out / "run-receipt.json", {
        "result": RESULT, "p": 41, "complete": complete, "process_exit_code": code,
        "error": error, "source_commit": source, "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "execution_environment": "public-repository-github-actions",
        "core_receipt_sha256": sha(rp) if rp.exists() else None,
        "actual_y_map_recovered": complete, "beta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete,
                      "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    run = read(out / "run-receipt.json")
    assert run["result"] == RESULT and run["complete"] is True
    receipt = read(out / "core-receipt.json")
    assert sha(out / "core-receipt.json") == run["core_receipt_sha256"]
    assert receipt["result"] == RESULT and receipt["complete"] is True
    assert receipt["source_sha256"] == item["core_sha256"]
    assert sha(out / FINAL) == receipt["certificate_sha256"]
    cert = read(out / FINAL)
    assert cert["complete"] is True and cert["result"] == RESULT and cert["p"] == 41
    tag = cert["configuration"]
    assert tag["source_sha256"] == item["core_sha256"] and tag["python_flint"] == "0.9.0"
    assert tag["R786_proof_sha256"] == item["R786_proof_sha256"]
    assert tag["R787_method_sha256"] == item["R787_method_sha256"]
    assert tag["R781_field_core_sha256"] == item["field_core_sha256"]
    assert tag["retained_artifacts"] == item["retained_artifacts"]
    assert cert["original_map_index"] == 4 and cert["original_map_degree"] == "1206"
    assert cert["exact_nonzero_A_B_relation_verified"] is True
    assert cert["original_full_L_retained"] is True
    assert cert["exact_verified_Laurent_exponents"] == [-1, 127]
    assert cert["exact_verified_t_coordinates"] == 20
    assert cert["actual_y_map_recovered"] is True and cert["beta_or_height_computed"] is False
    for key in ("relation_spec", "stage_manifest"):
        spec = cert[key]
        assert Path(spec["file"]).name == spec["file"]
        path = out / spec["file"]
        assert path.stat().st_size == spec["bytes"] and sha(path) == spec["sha256"]
        data = read(path)
        assert data["complete"] is True and data["configuration"] == tag
        if key == "stage_manifest":
            for row in data["files"]:
                assert Path(row["file"]).name == row["file"]
                path = out / row["file"]
                assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
    # Full characteristic-zero arithmetic is certified by the core once.
    # This pass only verifies the provenance and completed product hashes.
    return 0


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["compute", "verify"])
    args = parser.parse_args()
    out = Path(os.environ["RUNNER_TEMP"]) / "serre-global" / RESULT / "output"
    if args.mode == "compute":
        request = read(REQUEST)
        assert request["session"] == "serre-public-astra-20261115"
        return compute(request["job"], out)
    item = read(out / "public-actions-input.json")["job"]
    assert item["result"] == RESULT
    return verify(item, out)


if __name__ == "__main__":
    sys.exit(main())
