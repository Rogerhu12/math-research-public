#!/usr/bin/env python3
"""Inspect the latest ended R787 checkpoint by source-bound ZIP64 HTTP Range; IO only."""
import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R787-public-ended-checkpoint-io-request.json"
IO_NAME = "R824_public_original_global_polar_generators.py"
IO_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
CORE_SHA = "93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04"
RESULT = "R787-ended-checkpoint-source-IO-review"
ORIGINAL = "R787-original-power5-function-relation"
REFERENCE = "full-outputs-manifest-reference.json"
HISTORY = "dixon-checkpoint-history.json"
COMPACTION = "dixon-output-compaction-receipt.json"
DIXON = re.compile(r"R787-prime-(\d+)-dixon-(\d{8})\.json\.gz")


def sha(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            value.update(block)
    return value.hexdigest()


assert sha(S/IO_NAME) == IO_SHA
loader = importlib.util.spec_from_file_location("R787_ended_checkpoint_frozen_IO", S/IO_NAME)
IO = importlib.util.module_from_spec(loader)
loader.loader.exec_module(IO)


def run(out):
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    request = IO.read(REQUEST)
    assert request["audit_script_sha256"] == sha(__file__)
    assert request["io_helper_sha256"] == IO_SHA
    assert sha(REPO/"README.md") == request["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md") == request["readme_sha256"]["topic"]
    item = dict(request["original_producer"])
    assert item["result"] == ORIGINAL and item["core_sha256"] == CORE_SHA
    assert item["expected_conclusion"] == "failure"
    out.mkdir(parents=True, exist_ok=True)
    selected = out/"selected-original-R787"
    selected.mkdir(parents=True, exist_ok=True)
    transfer = out.parent/"R787-range-transfer"
    archive = IO.Archive(item, transfer, whole=False)
    selected_specs = {}
    try:
        refs = archive.by_name.get(REFERENCE, [])
        assert len(refs) == 1 and 0 < refs[0].file_size < 1024*1024
        with archive.zip.open(refs[0]) as stream:
            raw_ref = stream.read(1024*1024+1)
        assert len(raw_ref) == refs[0].file_size
        reference = json.loads(raw_ref)
        assert reference["result"] == ORIGINAL and reference["manifest_file"] == "full-outputs-manifest.json"
        assert reference["full_outputs_artifact"] == item["artifact_name"]
        assert IO.H64.fullmatch(reference["manifest_sha256"])
        assert reference["manifest_bytes"] > 0 and reference["file_count"] > 0
        (selected/REFERENCE).write_bytes(raw_ref)
        selected_specs[REFERENCE] = IO.file_spec(selected/REFERENCE)
        if item.get("manifest_sha256") is not None:
            assert item["manifest_sha256"] == reference["manifest_sha256"]
        item["manifest_sha256"] = reference["manifest_sha256"]
        item["manifest_bytes"] = reference["manifest_bytes"]
        item["manifest_file_count"] = reference["file_count"]
        mp = archive.extract_bound("full-outputs-manifest.json", item["manifest_sha256"],
                                   selected/"full-outputs-manifest.json", item["manifest_bytes"])
        selected_specs[mp.name] = IO.file_spec(mp)
        manifest = IO.read(mp)
        assert manifest["result"] == ORIGINAL
        files = {row["file"]: row for row in manifest["files"]}
        assert len(files) == len(manifest["files"]) == reference["file_count"]
        assert set(archive.by_name) == set(files)|{"full-outputs-manifest.json", REFERENCE}
        for name, row in files.items():
            IO.check_spec(row)
            assert len(archive.by_name[name]) == 1
            assert archive.by_name[name][0].file_size == row["bytes"]

        def raw(name, permanent=True):
            row = files[name]
            directory = selected if permanent else transfer
            path = archive.extract_bound(name, row["sha256"], directory/name, row["bytes"])
            if permanent:
                selected_specs[name] = IO.file_spec(path)
            return IO.read(path)

        run_receipt = raw("run-receipt.json")
        core_receipt = raw("core-receipt.json")
        initial = raw("public-actions-input.json")
        assert run_receipt["result"] == core_receipt["result"] == initial["result"] == ORIGINAL
        assert run_receipt["complete"] is False and run_receipt["process_exit_code"] != 0
        assert str(run_receipt["workflow_run_id"]) == item["run_id"]
        assert run_receipt["source_commit"] == initial["source_commit"] == item["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == core_receipt["source_sha256"] == CORE_SHA
        assert initial["driver_sha256"] == request["original_wrapper_sha256"]
        assert initial["job"]["wrapper_sha256"] == request["original_wrapper_sha256"]
        assert core_receipt["complete"] is False
        assert run_receipt["core_receipt_sha256"] == files["core-receipt.json"]["sha256"]
        assert initial["root_readme_sha256"] == request["original_readme_sha256"]["root"]
        assert initial["topic_readme_sha256"] == request["original_readme_sha256"]["topic"]
        logs = {}
        for name in ("public-actions-run.log", "core.log"):
            if name in files:
                row = files[name]
                path = archive.extract_bound(name, row["sha256"], selected/name, row["bytes"])
                selected_specs[name] = IO.file_spec(path)
                with path.open("rb") as stream:
                    stream.seek(max(0, row["bytes"]-16384))
                    logs[name] = stream.read().decode("utf-8", errors="replace")
        early = {"result": RESULT, "original_producer": item,
                 "original_run_receipt": run_receipt, "original_core_receipt": core_receipt,
                 "original_log_tails": logs, "new_mathematical_arithmetic_executed": False}
        print("R787_ENDED_CHECKPOINT_FAILURE_REASON="+json.dumps(
            early, sort_keys=True, separators=(",", ":")), flush=True)

        history = raw(HISTORY) if HISTORY in files else None
        records = {}
        if history is not None:
            assert history["result"] == ORIGINAL
            assert history["history_contains_only_name_bytes_sha256_prime_digits"] is True
            for row in history["checkpoints"]:
                match = DIXON.fullmatch(row["file"])
                assert match and row["prime"] == int(match[1]) and row["digits"] == int(match[2])
                IO.check_spec(row)
                assert row["file"] not in records
                records[row["file"]] = row
        compaction = raw(COMPACTION) if COMPACTION in files else None
        if compaction is not None:
            assert compaction["result"] == ORIGINAL
            assert compaction["same_exact_core_sha256"] == CORE_SHA
            assert compaction["only_failed_run_without_success_certificate_compacted"] is True
            assert compaction["non_Dixon_complete_stages_removed"] is False
        prior_restore = raw("resume-receipt.json") if "resume-receipt.json" in files else None
        if "retained-inputs-receipt.json" in files:
            raw("retained-inputs-receipt.json")
        search = raw("R787-search-state.json.gz") if "R787-search-state.json.gz" in files else None
        latest = {}
        for name, row in files.items():
            match = DIXON.fullmatch(name)
            if match:
                prime, digits = int(match[1]), int(match[2])
                if prime not in latest or digits > latest[prime][0]:
                    latest[prime] = (digits, row)
                if name in records:
                    assert IO.plain(records[name]) == IO.plain(row)
        assert latest, "Ended source has no completed lift member."
        summaries = []
        for prime, (digits, row) in sorted(latest.items()):
            chart_name = "R787-prime-"+str(prime)+"-chart.json.gz"
            selection_name = "R787-prime-"+str(prime)+"-selection.json.gz"
            chart, selection = raw(chart_name), raw(selection_name)
            assert chart["complete"] is selection["complete"] is True
            tag = chart["configuration"]
            assert selection["configuration"] == tag
            assert tag["source_sha256"] == CORE_SHA and tag["python_flint"] == "0.9.0"
            # Only one latest complete lift per prime is fetched and decoded, without arithmetic.
            lift = raw(row["file"], permanent=False)
            assert lift["complete"] is True and lift["configuration"] == tag
            assert lift["prime"] == prime and lift["digits"] == digits
            assert lift["chart_sha256"] == files[chart_name]["sha256"]
            assert lift["full_original_modular_relations_verified"] is True
            previous = lift.get("previous_completed_checkpoint_sha256")
            if digits > 1:
                previous_name = "R787-prime-"+str(prime)+"-dixon-"+str(digits-1).zfill(8)+".json.gz"
                assert previous_name in records and records[previous_name]["sha256"] == previous
            if compaction is not None:
                assert any(IO.plain(value) == IO.plain(row)
                           for value in compaction["latest_complete_lifts_retained"])
            branch_names = sorted(name for name in files if re.fullmatch(
                r"R787-prime-"+str(prime)+r"-branch-\d{2}\.json\.gz", name))
            summary = {
                "prime": prime, "actual_latest_complete_Dixon_digits": digits,
                "actual_latest_complete_lift": IO.plain(row),
                "latest_lift_bytes_and_sha256_verified_in_this_IO_read": True,
                "latest_lift_complete_and_configuration_verified": True,
                "previous_completed_checkpoint_sha256": previous,
                "actual_chart": IO.plain(files[chart_name]),
                "actual_selection": IO.plain(files[selection_name]),
                "actual_modular_Schur_rank": chart["actual_modular_rank"],
                "chosen_free_column": chart["chosen_free_column"],
                "original_branch_member_count_in_bound_manifest": len(branch_names),
                "original_branch_vectors_not_rehashed_again_in_this_subset_read": True,
                "full_original_modular_relations_verified_by_original_core": True,
                "configuration_sha256": IO.fingerprint(tag)}
            summaries.append(summary)
            del lift
            (transfer/row["file"]).unlink()
        assert "R787-retained-producer-inputs.tar.gz" in files
        resume_spec = dict(item)
        resume_spec.pop("certificate_name", None)
        resume_spec.pop("files", None)
        summary = dict(early,
            complete=True, selected_original_files=[selected_specs[name] for name in sorted(selected_specs)],
            actual_manifest_file_count=len(files), actual_ZIP_regular_member_count=len(archive.by_name),
            actual_latest_lifts=summaries, compact_name_bytes_sha_history_count=len(records),
            original_compaction_receipt=compaction,
            actual_search_state=search,
            original_input_bundle_identity_only=IO.plain(files["R787-retained-producer-inputs.tar.gz"]),
            original_previous_restore_identity_only=None if prior_restore is None else prior_restore.get("source"),
            original_previous_restore_latest=None if prior_restore is None else prior_restore.get("actual_prime_branch_and_latest_lift"),
            R787_same_core_next_resume_spec=resume_spec,
            original_full_manifest=IO.file_spec(mp),
            archive_subset_transfer=archive.receipt(),
            all_ZIP_bytes_or_all_original_outputs_rehashed_in_this_subset_review=False,
            restored_or_recomputed_mathematical_stages=False,
            reproducible_raw_outputs_published_to_git_or_release=False,
            read_at_utc=dt.datetime.now(dt.timezone.utc).isoformat())
        IO.save(out/"R787-ended-checkpoint-source-IO-summary.json", summary)
        IO.save(out/"R787-ended-checkpoint-source-IO-input.json", {
            "result": RESULT, "request": request, "audit_script_sha256": sha(__file__),
            "actual_audit_source_commit": os.environ["GITHUB_SHA"],
            "actual_audit_workflow_run_id": os.environ["GITHUB_RUN_ID"]})
        printable = dict(summary)
        # The preceding restore's 14 large branch identities are already preserved in the selected receipt.
        printable.pop("original_previous_restore_latest")
        if printable.get("actual_search_state") is not None:
            printable["actual_search_state"] = {key:value for key,value in
                printable["actual_search_state"].items() if key != "configuration"}
        print("R787_ENDED_CHECKPOINT_IO_SUMMARY="+json.dumps(
            printable, sort_keys=True, separators=(",", ":")), flush=True)
        return 0
    finally:
        archive.close()


if __name__ == "__main__":
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    raise SystemExit(run(args.output))
