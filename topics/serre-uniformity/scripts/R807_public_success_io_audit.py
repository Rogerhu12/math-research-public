#!/usr/bin/env python3
"""Read-only public Actions audit of the actual R807 success, plus an actual main pull."""
import argparse
import ast
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import time
import zipfile

REPOSITORY = "Rogerhu12/math-research-public"
SOURCE = "2c44d02595d57c22b5ea2c10defa93f63252061d"
RUN = "43707939269"
ARTIFACT = 14159481627
ARCHIVE_BYTES = 60771931
ARCHIVE_SHA = "74c801509f554024d0246bf62227e38c30f4e84a14d4e0af8fa917350f875a56"
RESULT = "R807-original-M6-pole-clearing"
FINAL = "p41-original-M6-pole-clearing-certificate.json"
ARTIFACT_NAME = "serre-global-"+RESULT+"-"+RUN+"-1"
BUNDLE = "R807-retained-producer-inputs.tar.gz"
TOPIC = "topics/serre-uniformity"
WRAPPER = "R807_public_original_M6_pole_clearing.py"
READMES = ("README.md", TOPIC+"/README.md")
COORDINATE_INDICES = (690, 691, 692, 693)


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    temporary.write_text(json.dumps(value, sort_keys=True, indent=2)+"\n", encoding="utf-8")
    temporary.replace(path)


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def plain_spec(row):
    return {key: row[key] for key in ("file", "bytes", "sha256")}


def command(args, cwd=None):
    completed = subprocess.run(args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               text=True, check=True)
    return completed.stdout.strip()


def api(path):
    return json.loads(command(["gh", "api", path]))


def pull_and_compare(root, last_read):
    repo = root/"actual-partial-clone"
    if not (repo/".git").exists():
        command(["git", "clone", "--filter=blob:none", "--sparse", "--depth", "1",
                 "--branch", "main", "--no-checkout",
                 "https://github.com/"+REPOSITORY+".git", str(repo)])
        command(["git", "sparse-checkout", "set", "--no-cone",
                 "/README.md", "/"+TOPIC+"/README.md"], repo)
        command(["git", "checkout", "main"], repo)
    before = command(["git", "rev-parse", "HEAD"], repo)
    pull_output = command(["git", "pull", "--rebase", "origin", "main"], repo)
    after = command(["git", "rev-parse", "HEAD"], repo)
    remote = command(["git", "rev-parse", "origin/main"], repo)
    assert after == remote
    for commit in {last_read, SOURCE}:
        probe = subprocess.run(["git", "cat-file", "-e", commit+"^{commit}"], cwd=repo,
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if probe.returncode:
            command(["git", "fetch", "--filter=blob:none", "--depth", "1", "origin", commit], repo)
    diff = command(["git", "diff", last_read, after, "--", *READMES], repo)
    receipt = {"source_repository": REPOSITORY, "actual_partial_clone": True,
        "filter": "blob:none", "sparse_readme_checkout_only": True,
        "command": "git pull --rebase origin main", "before_head": before,
        "after_head": after, "origin_main": remote, "last_read_rules_commit": last_read,
        "actual_pull_completed_at_utc": now(), "readme_differences_present": bool(diff),
        "root_readme_sha256": sha(repo/READMES[0]),
        "topic_readme_sha256": sha(repo/READMES[1]), "pull_output": pull_output}
    save(root/"audit-output"/"actual-pull-and-readme-receipt.json", receipt)
    print("ACTUAL_PULL_RECEIPT="+json.dumps(receipt, sort_keys=True), flush=True)
    if diff:
        print("README_DIFF_BEGIN\n"+diff+"\nREADME_DIFF_END", flush=True)
        raise RuntimeError("Actual README changes require parent review before this audit continues.")
    print("README_DIFF_EMPTY", flush=True)
    return repo, receipt


def download_zip(root):
    run = api("repos/"+REPOSITORY+"/actions/runs/"+RUN)
    assert str(run["id"]) == RUN and run["head_sha"] == SOURCE
    assert run["status"] == "completed" and run["conclusion"] == "success"
    artifact = api("repos/"+REPOSITORY+"/actions/artifacts/"+str(ARTIFACT))
    assert artifact["id"] == ARTIFACT and artifact["name"] == ARTIFACT_NAME
    assert artifact["expired"] is False and str(artifact["workflow_run"]["id"]) == RUN
    assert artifact["digest"] == "sha256:"+ARCHIVE_SHA
    assert artifact["size_in_bytes"] == ARCHIVE_BYTES
    archive = root/"original-R807-success.zip"
    if not archive.exists():
        temporary = archive.with_suffix(".zip.tmp")
        with temporary.open("wb") as output:
            subprocess.run(["gh", "api", "repos/"+REPOSITORY+"/actions/artifacts/"+str(ARTIFACT)+"/zip"],
                           stdout=output, check=True)
        temporary.replace(archive)
    assert archive.stat().st_size == ARCHIVE_BYTES and sha(archive) == ARCHIVE_SHA
    return archive, {"run_id": RUN, "source_commit": SOURCE,
        "artifact_id": ARTIFACT, "artifact_name": ARTIFACT_NAME,
        "archive_bytes": ARCHIVE_BYTES, "archive_sha256": ARCHIVE_SHA,
        "artifact_expires_at": artifact["expires_at"], "run_conclusion": run["conclusion"],
        "actual_downloaded_zip_size_and_sha256_verified": True}


def unpack_zip(archive, output):
    output.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as z:
        members = {}
        for info in z.infolist():
            relative = Path(info.filename)
            assert not relative.is_absolute() and ".." not in relative.parts
            if info.is_dir():
                continue
            assert relative.name not in members, "Duplicate output basename"
            members[relative.name] = info
        for name in ("full-outputs-manifest.json", "full-outputs-manifest-reference.json"):
            assert name in members
            target = output/name
            with z.open(members[name]) as source, target.open("wb") as stream:
                shutil.copyfileobj(source, stream, 1024*1024)
        manifest = read(output/"full-outputs-manifest.json")
        reference = read(output/"full-outputs-manifest-reference.json")
        assert manifest["result"] == reference["result"] == RESULT
        assert reference["manifest_sha256"] == sha(output/"full-outputs-manifest.json")
        assert reference["manifest_bytes"] == (output/"full-outputs-manifest.json").stat().st_size
        entries = {row["file"]: row for row in manifest["files"]}
        assert len(entries) == len(manifest["files"]) == reference["file_count"]
        assert set(members) == set(entries)|{"full-outputs-manifest.json", "full-outputs-manifest-reference.json"}
        total = 0
        for name, row in entries.items():
            assert Path(name).name == name
            assert members[name].file_size == row["bytes"]
            target = output/name
            if target.exists() and target.stat().st_size == row["bytes"] and sha(target) == row["sha256"]:
                total += row["bytes"]
                continue
            temporary = target.with_name(target.name+".tmp")
            h, count = hashlib.sha256(), 0
            with z.open(members[name]) as source, temporary.open("wb") as stream:
                for block in iter(lambda: source.read(1024*1024), b""):
                    stream.write(block)
                    h.update(block)
                    count += len(block)
            assert count == row["bytes"] and h.hexdigest() == row["sha256"], name
            temporary.replace(target)
            total += count
    return entries, {"zip_file_members": len(members), "full_manifest_file_count": len(entries),
                    "all_full_manifest_sizes_sha256_verified": True,
                    "full_manifest": file_spec(output/"full-outputs-manifest.json"),
                    "uncompressed_manifest_bytes_total": total}


def frozen_sources(repo, root, output):
    initial = read(output/"public-actions-input.json")
    run = read(output/"run-receipt.json")
    assert initial["source_repository"] == REPOSITORY
    assert initial["source_commit"] == run["source_commit"] == SOURCE
    assert str(run["workflow_run_id"]) == RUN and run["workflow_attempt"] in (1, "1")
    item = initial["job"]
    assert item["result"] == RESULT and item["producer_inputs_pending"] is False
    request_path = TOPIC+"/notes/R807-public-original-M6-pole-clearing-request.json"
    specs = {
        TOPIC+"/scripts/"+item["core"]: initial["core_sha256"],
        TOPIC+"/scripts/"+WRAPPER: initial["driver_sha256"],
        TOPIC+"/scripts/R786_public_exact_power5_short_basis.py": initial["download_helper_sha256"],
        TOPIC+"/scripts/p41_public_actions_recovery.py": initial["io_helper_sha256"],
        TOPIC+"/"+item["proof"]: initial["proof_sha256"],
        TOPIC+"/"+item["method"]: initial["method_sha256"],
        request_path: initial["request_sha256"],
        item["workflow"]: initial["workflow_sha256"],
        READMES[0]: initial["root_readme_sha256"],
        READMES[1]: initial["topic_readme_sha256"],
    }
    assert item["core_sha256"] == initial["core_sha256"]
    assert item["wrapper_sha256"] == initial["driver_sha256"]
    assert item["R805_proof_sha256"] == initial["proof_sha256"]
    assert item["R807_method_sha256"] == initial["method_sha256"]
    assert item["download_helper_sha256"] == initial["download_helper_sha256"]
    assert item["io_helper_sha256"] == initial["io_helper_sha256"]
    frozen = root/"frozen-producer-source"
    checked = {}
    for relative, digest in specs.items():
        path = Path(relative)
        assert not path.is_absolute() and ".." not in path.parts
        target = frozen/path
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("wb") as stream:
            subprocess.run(["git", "show", SOURCE+":"+relative], cwd=repo, stdout=stream, check=True)
        assert sha(target) == digest, relative
        if target.suffix == ".py":
            ast.parse(target.read_text(encoding="utf-8"), filename=relative)
        checked[relative] = file_spec(target)
    request = read(frozen/request_path)
    assert request["session"] == "serre-public-astra-20261115" and request["job"] == item
    return frozen, item, checked


def unpack_and_verify_input_bundle(bundle, retained, item):
    retained.mkdir(parents=True, exist_ok=True)
    actual = {}
    with tarfile.open(bundle, "r:gz") as tar:
        for member in tar:
            relative = Path(member.name)
            assert member.isfile() and not relative.is_absolute() and ".." not in relative.parts
            assert len(relative.parts) == 2 and str(relative) not in actual
            label, name = relative.parts
            assert label in {"R775", "R786", "R805"}
            target = retained/relative
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = target.with_name(target.name+".tmp")
            digest, count = hashlib.sha256(), 0
            with tar.extractfile(member) as source, temporary.open("wb") as stream:
                for block in iter(lambda: source.read(1024*1024), b""):
                    stream.write(block)
                    digest.update(block)
                    count += len(block)
            assert count == member.size
            temporary.replace(target)
            actual[str(relative)] = {"bytes": count, "sha256": digest.hexdigest()}
    assert len(actual) == 997, ("Actual retained member count", len(actual))
    groups = []
    for label in sorted(item["retained_artifacts"]):
        spec = item["retained_artifacts"][label]
        mp = retained/label/"full-outputs-manifest.json"
        assert sha(mp) == spec["manifest_sha256"]
        manifest = read(mp)
        assert manifest["result"] == spec["result"]
        entries = {row["file"]: row for row in manifest["files"]}
        assert len(entries) == len(manifest["files"])
        count = 0
        for relative, row in actual.items():
            group, name = Path(relative).parts
            if group != label:
                continue
            count += 1
            if name == "full-outputs-manifest.json":
                assert row["sha256"] == spec["manifest_sha256"]
            else:
                expected = entries[name]
                assert row == {"bytes": expected["bytes"], "sha256": expected["sha256"]}, relative
        groups.append({"label": label, "file_count": count, "result": spec["result"],
            "run_id": spec["run_id"], "source_commit": spec["source_commit"],
            "core_sha256": spec["core_sha256"], "manifest_sha256": spec["manifest_sha256"],
            "certificate_name": spec["certificate_name"],
            "certificate_sha256": spec["files"][spec["certificate_name"]],
            "all_carried_member_sizes_sha256_verified": True})
    return actual, groups


def run_frozen_io_verify(frozen, output, retained, item):
    assert "flint" not in sys.modules
    scripts = frozen/TOPIC/"scripts"
    sys.path.insert(0, str(scripts))
    location = importlib.util.spec_from_file_location("R807_frozen_pure_IO_wrapper", scripts/WRAPPER)
    module = importlib.util.module_from_spec(location)
    location.loader.exec_module(module)
    assert "flint" not in sys.modules
    producers = {label: module.Producer(label, spec, [retained/label])
                 for label, spec in item["retained_artifacts"].items()}
    selection = module.select_original_inputs(producers)
    carried = read(output/"retained-inputs-receipt.json")
    assert carried["selection"] == selection
    assert carried["input_bundle"] == file_spec(output/BUNDLE)
    for row in carried["groups"]:
        label = row["label"]
        assert row["producer"] == item["retained_artifacts"][label]
        assert row["file_count"] == len(producers[label].selected)
        assert {p.name for p in (retained/label).iterdir()} == set(producers[label].selected)
    status = module.verify(item, output)
    assert status == 0 and "flint" not in sys.modules
    assert not any(name.startswith("R807_original_M6") for name in sys.modules)
    return {"frozen_wrapper_verify_unmodified": True,
            "frozen_wrapper_verify_returncode": status,
            "all_original_source_chains_and_selected_schemas_verified": True,
            "mathematical_core_imported": False, "flint_imported": False,
            "new_mathematical_arithmetic_executed": False}


def summary_and_selected(root, output, item, archive_record, output_record, source_records,
                         input_members, groups, verify_record, pull_receipt, seconds):
    certificate = read(output/FINAL)
    manifest = read(output/certificate["stage_manifest"]["file"])
    stage_entries = {row["file"]: plain_spec(row) for row in manifest["files"]}
    assert len(stage_entries) == len(manifest["files"])
    assert certificate["V4_dimension"] == 962 and certificate["qY_count"] == 55
    assert certificate["full_real_coordinate_rows"] == 1100
    assert certificate["actual_nonzero_theta_constructed"] is True
    assert certificate["actual_M6_pole_clearing_computed"] is True
    assert certificate["five_selected_row_projections_exactly_verified"] is True
    assert certificate["all_four_M6_products_verified_in_all1100_rows"] is True
    assert certificate["rank_four_not_preassigned"] is True
    assert certificate["individual_five_target_membership_claimed"] is False
    minor = read(output/certificate["minor_stage"]["file"])
    theta = read(output/certificate["theta_stage"]["file"])
    residual = read(output/certificate["residual_kernel_stage"]["file"])
    index = read(output/certificate["cleared_coordinate_index"]["file"])
    assert theta["lambda"] == residual["lambda"]
    assert theta["actual_residual_rank"] == residual["actual_rank"] == certificate["actual_residual_rank"]
    assert certificate["actual_residual_kernel_dimension"] == len(residual["full_nullspace_basis"])
    assert index["coordinate_stages"] == certificate["cleared_coordinate_stages"]
    rhs = []
    for j, spec in enumerate(certificate["projection_stages"]):
        data = read(output/spec["file"])
        assert data["mode"] == "projection" and data["label"] == "E6-projection-j"+str(j)
        assert data["all962_selected_rows_verified"] is True and data["all1100_rows_verified"] is False
        rhs.append({"kind": "selected_row_projection", "original_M2_index": j, "file": plain_spec(spec),
            "actual_prime": data["actual_prime"], "actual_Dixon_digits": data["actual_Dixon_digits"],
            "solution_denominator_decimal_digits": len(data["solution_common_denominator"]),
            "all962_selected_rows_verified": True, "individual_V4_membership_claimed": False})
    coordinates = []
    for i in COORDINATE_INDICES:
        spec = certificate["cleared_coordinate_stages"][str(i)]
        data = read(output/spec["file"])
        assert data["all1100_rows_verified"] is True
        record = {"M6_index": i, "file": plain_spec(spec),
            "basis_dimension": data["basis_dimension"], "basis_integer_scale": data["basis_integer_scale"],
            "solution_common_denominator_decimal_digits": len(data["solution_common_denominator"]),
            "all1100_rows_verified": True}
        if i == 692:
            assert data["coordinates_obtained_from_five_existing_projections"] is True
            assert data["a_ninth_right_hand_side_solved"] is False
            record["derived_from_actual_residual_kernel_without_new_RHS"] = True
        else:
            assert data["mode"] == "member" and data["label"] == "M6-index-"+str(i)
            record["actual_prime"] = data["actual_prime"]
            record["actual_Dixon_digits"] = data["actual_Dixon_digits"]
            rhs.append({"kind": "cleared_member", "M6_index": i, "file": plain_spec(spec),
                "actual_prime": data["actual_prime"], "actual_Dixon_digits": data["actual_Dixon_digits"],
                "all1100_rows_verified": True})
        coordinates.append(record)
    assert len(rhs) == certificate["exact_right_hand_sides_solved"] == 8
    selected_dir = root/"audit-output"/"selected-original-R807"
    selected_dir.mkdir(parents=True, exist_ok=True)
    selected_names = {FINAL, "full-outputs-manifest.json", "full-outputs-manifest-reference.json",
                      "run-receipt.json", "core-receipt.json", "public-actions-input.json",
                      certificate["stage_manifest"]["file"], certificate["basis_index"]["file"],
                      certificate["theta_stage"]["file"], certificate["residual_kernel_stage"]["file"],
                      certificate["cleared_coordinate_index"]["file"]}
    selected_names.update(spec["file"] for spec in certificate["cleared_coordinate_stages"].values())
    for name in sorted(selected_names):
        shutil.copyfile(output/name, selected_dir/name)
    encoded_lambda = json.dumps(theta["lambda"], separators=(",", ":"))
    lambda_summary = theta["lambda"] if len(encoded_lambda) <= 2048 else {
        "original_theta_stage": certificate["theta_stage"],
        "coordinate_numerator_decimal_lengths": [len(pair[0]) for pair in theta["lambda"]],
        "coordinate_denominator_decimal_lengths": [len(pair[1]) for pair in theta["lambda"]]}
    summary = {"result": "R807-actual-success-pure-IO-review",
        "reviewed_original_result": RESULT, "source_commit": SOURCE, "run_id": RUN,
        "archive": archive_record, "outputs": output_record,
        "actual_original_core_sha256": item["core_sha256"],
        "actual_frozen_wrapper_sha256": item["wrapper_sha256"],
        "certificate": file_spec(output/FINAL),
        "stage_manifest": file_spec(output/certificate["stage_manifest"]["file"]),
        "stage_count": len(stage_entries), "V4_dimension": 962,
        "qY_count": 55, "full_real_coordinate_rows": 1100,
        "basis_integer_scale": certificate["ordinary_V4_integer_scale"],
        "actual_short_minor": {"prime": minor["prime"], "rank": 962,
            "determinant_mod_prime": minor["actual_determinant_mod_prime"],
            "coordinate_row_count": len(minor["coordinate_row_indices"]),
            "file": certificate["minor_stage"]},
        "actual_residual_rank": residual["actual_rank"],
        "actual_kernel_dimension": len(residual["full_nullspace_basis"]),
        "actual_nonzero_rank_minor": residual["actual_nonzero_rank_minor"],
        "theta_lambda_in_original_first_five_integer_scaled_M2_rows": lambda_summary,
        "theta_first_nonzero_original_M2_index": theta["first_nonzero_lambda_index"],
        "theta_stage": certificate["theta_stage"],
        "residual_kernel_stage": certificate["residual_kernel_stage"],
        "cleared_coordinate_index": certificate["cleared_coordinate_index"],
        "actual_eight_rational_RHS": rhs, "actual_four_cleared_coordinate_stages": coordinates,
        "C692_obtained_from_five_projections_without_ninth_rhs": True,
        "all_four_members_have_full1100_exact_certification": True,
        "actual_new_pair_tail_stages": certificate["actual_new_pair_tail_stages"],
        "old_M2_V2_V4_or_R805_pair_prefixes_recomputed": False,
        "original_input_bundle": file_spec(output/BUNDLE),
        "original_input_bundle_member_count": len(input_members), "original_producer_groups": groups,
        "core_elapsed_seconds": certificate["seconds"], "audit_elapsed_seconds": seconds,
        "frozen_source_files": source_records, "verification": verify_record,
        "actual_pull": pull_receipt, "all_full_output_and_input_bundle_member_hashes_verified": True,
        "raw_matrices_or_lift_vectors_in_job_log": False,
        "automatic_git_or_release_publication": False,
        "theta_Uj_functions_local_high_jets_polar_divisors_eta_or_height_claimed": False,
        "selected_original_continuation_files": [file_spec(selected_dir/name) for name in sorted(selected_names)],
        "audit_execution": {"repository": os.environ["GITHUB_REPOSITORY"],
            "source_commit": os.environ["GITHUB_SHA"], "run_id": os.environ["GITHUB_RUN_ID"],
            "attempt": os.environ["GITHUB_RUN_ATTEMPT"], "audit_script_sha256": sha(__file__)}}
    save(root/"audit-output"/"R807-success-IO-review-summary.json", summary)
    print("R807_IO_REVIEW_SUMMARY="+json.dumps(summary, sort_keys=True, separators=(",", ":")), flush=True)
    print("R807_IO_REVIEW_SUMMARY_FILE="+json.dumps(file_spec(root/"audit-output"/"R807-success-IO-review-summary.json")), flush=True)
    return summary


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
        raise SystemExit("This read-only producer audit runs in the public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--last-read-commit", default="f59c795c69c05bed6efa45a937ab352def8e5972")
    parser.add_argument("--root", type=Path, default=Path(os.environ["RUNNER_TEMP"])/"serre-R807-io-audit")
    args = parser.parse_args()
    started = time.monotonic()
    args.root.mkdir(parents=True, exist_ok=True)
    (args.root/"audit-output").mkdir(parents=True, exist_ok=True)
    repo, pull_receipt = pull_and_compare(args.root, args.last_read_commit)
    archive, archive_record = download_zip(args.root)
    output = args.root/"review"/"output"
    entries, output_record = unpack_zip(archive, output)
    frozen, item, source_records = frozen_sources(repo, args.root, output)
    assert plain_spec(entries[BUNDLE]) == file_spec(output/BUNDLE)
    retained = output.parent/"retained"
    members, groups = unpack_and_verify_input_bundle(output/BUNDLE, retained, item)
    verify_record = run_frozen_io_verify(frozen, output, retained, item)
    summary_and_selected(args.root, output, item, archive_record, output_record, source_records,
                         members, groups, verify_record, pull_receipt, time.monotonic()-started)
    return 0


if __name__ == "__main__":
    sys.exit(main())
