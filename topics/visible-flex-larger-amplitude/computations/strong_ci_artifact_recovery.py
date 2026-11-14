#!/usr/bin/env python3
"""Recover the immutable first strong CI artifact; perform no mathematics.

Only artifact13983440730 from run43302113873 is accepted. The downloaded ZIP
is streamed and checked against its original Actions SHA256. Every extracted
path is restricted to that run's two notes prefixes. Existing files are kept
only when their complete byte hash matches. The original ci-stable manifest
is then verified without editing any original output. No Node, RHS, Jacobian,
BVP, Git mutation or new numerical acceptance occurs here.
This revision bounds the serialized report and encodes nonfinite diagnostics;
it does not infer the still-unread first recovery exception from those changes.
"""
from __future__ import annotations
import argparse
import datetime
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import shutil
import stat
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile

REPOSITORY = "Rogerhu12/math-research"
ARTIFACT = 13983440730
ORIGINAL_RUN = 43302113873
ZIP_SHA256 = "27c0e11f6ab2c0fc45338dd186c0fdd36cfe7f2f962f1b849f509708054331fb"
ORIGINAL_STABLE_SHA256 = "cba8f854bd6cbc2c64ff68e7c96a2c956aac6a4379a0a235edefd084a67f5be6"
PREFIX = "2026-11-12-strong-actual-q096-ci-actions-43302113873-1-strong"
RUN_DIRECTORY = "ci-recovery-43302113873-1-strong"
TOPIC = Path("topics/visible-flex-larger-amplitude")
SELF_SHA = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def digest(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            value.update(block)
    return value.hexdigest()


def atomic_json(path, value):
    path = Path(path)
    data = (json.dumps(value, indent=2, allow_nan=False)+"\n").encode()
    if len(data) >= 100000:
        raise ValueError("The recovery report must stay below100KB")
    temporary = path.with_name(path.name+".tmp-"+str(os.getpid()))
    with temporary.open("xb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())
    try:
        os.link(temporary, path)
    finally:
        temporary.unlink()


class SafeRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, newurl):
        parsed = urllib.parse.urlparse(newurl)
        host = (parsed.hostname or "").lower()
        if (parsed.scheme != "https" or not (
                host == "api.github.com" or host.endswith(".blob.core.windows.net")
                or host.endswith(".githubusercontent.com"))):
            raise ValueError("Artifact redirect left the explicitly expected HTTPS storage hosts")
        result = super().redirect_request(request, fp, code, message, headers, newurl)
        if result is not None:
            # The storage redirect is signed independently; never forward the
            # GitHub credential to a blob host (or persist its signed URL).
            result.remove_header("Authorization")
            result.remove_header("Cookie")
        return result


def download(archive, token):
    url = f"https://api.github.com/repos/{REPOSITORY}/actions/artifacts/{ARTIFACT}/zip"
    opener = urllib.request.build_opener(SafeRedirect())
    attempts = []
    for attempt in range(1, 5):
        temporary = archive.with_name(archive.name+".partial-"+str(os.getpid()))
        if temporary.exists():
            raise FileExistsError("An owned incomplete download already exists; use a fresh work directory")
        request = urllib.request.Request(url, headers={
            "Accept":"application/vnd.github+json",
            "Authorization":"Bearer "+token,
            "X-GitHub-Api-Version":"2022-11-28",
            "User-Agent":"visible-flex-immutable-artifact-recovery",
        })
        try:
            value = hashlib.sha256()
            count = 0
            with opener.open(request, timeout=60) as response, temporary.open("xb") as stream:
                while True:
                    block = response.read(1024*1024)
                    if not block:
                        break
                    count += len(block)
                    if count > 100_000_000:
                        raise ValueError("The declared35.8MB artifact exceeded the bounded recovery size")
                    value.update(block)
                    stream.write(block)
                stream.flush()
                os.fsync(stream.fileno())
            if value.hexdigest() != ZIP_SHA256:
                raise ValueError("Downloaded artifact ZIP SHA256 differs from the original Actions digest")
            os.link(temporary, archive)
            temporary.unlink()
            attempts.append(dict(attempt=attempt, success=True, bytes=count))
            return dict(artifact_id=ARTIFACT, run_id=ORIGINAL_RUN, bytes=count,
                sha256=value.hexdigest(), expected_sha256=ZIP_SHA256,
                complete_zip_digest_equal=True, attempts=attempts,
                credential_written_to_file=False, signed_download_URL_retained=False)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ConnectionError) as error:
            if temporary.exists():
                temporary.unlink()
            code = error.code if isinstance(error, urllib.error.HTTPError) else None
            # Do not emit exception text, redirect URLs, request headers or the
            # credential. Record only the concrete transport class/status.
            attempts.append(dict(attempt=attempt, success=False,
                error_type=type(error).__name__, http_status=code))
            print(json.dumps(dict(event="artifact_download_transport_failure",
                attempt=attempt, error_type=type(error).__name__, http_status=code)), flush=True)
            if attempt == 4 or code in (401, 403, 404):
                raise RuntimeError("Immutable artifact transport failed; status="+str(code)) from None
            time.sleep(2**(attempt-1))
        finally:
            request = None


def safe_relative(name):
    if "\\" in name or "\x00" in name:
        raise ValueError("Invalid artifact member path")
    original = PurePosixPath(name)
    if original.is_absolute() or ".." in original.parts:
        raise ValueError("Artifact contains an absolute or parent traversal path")
    text = original.as_posix()
    long_prefix = TOPIC.as_posix()+"/notes/"
    if text.startswith(long_prefix):
        text = text[len(long_prefix):]
    elif text.startswith("notes/"):
        text = text[len("notes/"):]
    if not (text.startswith(PREFIX) or text.startswith(RUN_DIRECTORY+"/")):
        raise ValueError("Artifact member is outside the two exact original run prefixes")
    relative = PurePosixPath(text)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("Invalid normalized artifact path")
    return Path(relative.as_posix())


def restore(archive, notes):
    rows = []
    seen = set()
    with zipfile.ZipFile(archive) as bundle:
        for entry in bundle.infolist():
            if entry.is_dir():
                continue
            if stat.S_ISLNK(entry.external_attr >> 16):
                raise ValueError("Artifact symbolic links are not accepted")
            relative = safe_relative(entry.filename)
            if relative.as_posix() in seen:
                raise ValueError("Duplicate artifact member")
            seen.add(relative.as_posix())
            target = notes/relative
            if target.is_symlink():
                raise ValueError("Do not overwrite a symbolic-link destination")
            target.parent.resolve().relative_to(notes.resolve())
            target.parent.mkdir(parents=True, exist_ok=True)
            target.parent.resolve().relative_to(notes.resolve())
            temporary = target.with_name(target.name+".ci-restore-"+str(os.getpid())+".tmp")
            value = hashlib.sha256()
            count = 0
            try:
                with bundle.open(entry) as source, temporary.open("xb") as output:
                    while True:
                        block = source.read(1024*1024)
                        if not block:
                            break
                        count += len(block)
                        if count > 100_000_000:
                            raise ValueError("An artifact member exceeded the explicit bounded size")
                        value.update(block)
                        output.write(block)
                    output.flush()
                    os.fsync(output.fileno())
                if count != entry.file_size:
                    raise ValueError("Artifact member size differs after complete CRC reading")
                actual = value.hexdigest()
                reused = False
                if target.exists():
                    if not target.is_file() or target.stat().st_size != count or digest(target) != actual:
                        raise FileExistsError("Original run destination already contains different bytes: "+relative.as_posix())
                    reused = True
                else:
                    try:
                        os.link(temporary, target)
                    except FileExistsError:
                        if not target.is_file() or target.stat().st_size != count or digest(target) != actual:
                            raise FileExistsError("Concurrent destination has different bytes: "+relative.as_posix())
                        reused = True
                rows.append(dict(path="notes/"+relative.as_posix(), bytes=count,
                    sha256=actual, original_bytes_restored=True, existing_identical_file=reused))
            finally:
                if temporary.exists():
                    temporary.unlink()
    if len(rows) != 72:
        raise ValueError("The original72-file artifact member count differs")
    return rows


def verify_original_manifest(topic, notes):
    manifest = notes/(PREFIX+"-ci-stable-files.json")
    if digest(manifest) != ORIGINAL_STABLE_SHA256:
        raise ValueError("Original CI stable-manifest SHA256 differs")
    data = json.loads(manifest.read_text())
    checked = []
    for item in data["files"]:
        relative = Path(item["path"])
        if relative.is_absolute() or ".." in relative.parts or not relative.as_posix().startswith("notes/"+PREFIX):
            raise ValueError("Original stable manifest points outside this exact run")
        file = topic/relative
        if not file.is_file() or file.stat().st_size != item["bytes"] or digest(file) != item["sha256"]:
            raise ValueError("Original stable output is missing or differs: "+relative.as_posix())
        checked.append(relative.as_posix())
    return dict(path=str(manifest.relative_to(topic)), sha256=digest(manifest),
        complete_original_files_verified=len(checked), all_original_recorded_hashes_equal=True,
        original_manifest_was_not_rewritten=True,
        original_solver_success_and_audit_complete=data.get("original_solver_success_and_audit_complete"),
        complete_topic_acceptance_claimed=False)


def compact(value, depth=0):
    if isinstance(value, float) and not math.isfinite(value):
        return dict(nonfinite_original_diagnostic=repr(value), original_file_not_modified=True)
    if value is None or isinstance(value, (bool, int, float)):
        return value
    if isinstance(value, str):
        return value if len(value) <= 1400 else value[:1400]+" [truncated for small recovery report]"
    if isinstance(value, list):
        if len(value) <= 64 and all(x is None or isinstance(x, (str, bool, int, float)) for x in value):
            return value
        return dict(kind="list", length=len(value))
    if isinstance(value, dict):
        if depth >= 5:
            return dict(keys=sorted(value))
        skipped = {"source_sha256", "local_source_hashes", "source_transform",
            "sourceTransforms", "replacements", "explicit_transforms"}
        return {key:(dict(omitted_source_metadata=True, entries=len(child))
                if key in skipped and isinstance(child, (list, dict)) else compact(child, depth+1))
            for key, child in value.items()}
    return dict(type=type(value).__name__)



def bounded_summary(summary):
    # The complete immutable summary remains a separate original file. Select
    # the scientific terminal values explicitly; source transforms and long
    # planning dictionaries do not belong in this small transport report.
    keys = (
        "solver_success", "audit_pending", "error", "message", "modes", "nodes",
        "config", "gauge_amplitude", "actual_primary_amplitude", "parameters",
        "central_correction_scales", "frozen_profile", "core", "meridian_length",
        "max_rms_collocation_residual", "summary", "numerical_meridian_chart",
        "raw_collocation_checkpoint", "prescribed_actual_core", "seconds")
    result = {key:compact(summary[key]) for key in keys if key in summary}
    tail = summary.get("actual_tail", {})
    result["actual_tail"] = {key:compact(tail[key]) for key in (
        "config", "config_sha256", "client_kind", "coupling",
        "actual_physical_bc_tolerance", "requests", "final_response",
        "residual", "jets", "audit", "seam_nonmean") if key in tail}
    result["actual_tail"]["outer_history"] = [
        {key:compact(value) for key,value in row.items()
            if isinstance(value,(str,bool,int,float)) or value is None}
        for row in tail.get("outer_history", [])]
    design = summary.get("actual_augmented_continuation", {})
    result["actual_augmented_continuation"] = {key:compact(design[key]) for key in (
        "actual_low_core", "scaled_low_core_constraint_max", "final_physical_profile",
        "original_outer_true_tail_acceptance_preserved",
        "inner_iterates_never_accepted_as_coupled_solutions",
        "actual_targets", "fixed_external_profile_shifts") if key in design}
    result["unabridged_summary_kept_at_original_path"] = True
    return result


def encoded_size(value):
    return len((json.dumps(value, indent=2, allow_nan=False)+"\n").encode())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--work-root", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    topic = args.repo.resolve()/TOPIC
    notes = topic/"notes"
    output = args.out.resolve() if args.out.is_absolute() else (topic/args.out).resolve()
    output.relative_to(notes.resolve())
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        raise FileExistsError("Use a fresh recovery report")
    work = args.work_root.resolve()/("strong-artifact13983440730-"+output.stem)
    work.mkdir(parents=True, exist_ok=False)
    archive = work/"original-artifact.zip"
    token = os.environ.pop("GH_TOKEN", None)
    os.environ.pop("GITHUB_TOKEN", None)
    if not token:
        raise ValueError("This pure artifact-recovery stage requires its ephemeral GH_TOKEN")
    report = dict(scope=__doc__, created_utc=utc(), entry_sha256=SELF_SHA,
        repository=REPOSITORY, original_run_id=ORIGINAL_RUN, artifact_id=ARTIFACT,
        expected_zip_sha256=ZIP_SHA256, status="artifact-recovery-started",
        mathematical_recomputation=False, Node_processes=0, new_BVP=False,
        original_local_r7_terminal_status="unknown",
        full_environment_never_serialized=True)
    try:
        report["download"] = download(archive, token)
        token = None
        report["restored_files"] = restore(archive, notes)
        report["original_stable_manifest"] = verify_original_manifest(topic, notes)
        summary_path = notes/(PREFIX+"-summary.json")
        terminal_path = notes/(PREFIX+"-ci-terminal.json")
        resource_path = notes/(PREFIX+"-resource.json")
        summary = json.loads(summary_path.read_text())
        terminal = json.loads(terminal_path.read_text())
        resource = json.loads(resource_path.read_text())
        report.update(status="complete-byte-verified-original-artifact-restoration",
            finished_utc=utc(), summary_file=str(summary_path.relative_to(topic)),
            summary_sha256=digest(summary_path), formal_original_solver_success=summary.get("solver_success"),
            formal_original_audit_pending=summary.get("audit_pending"),
            original_summary=bounded_summary(summary), original_ci_terminal=compact(terminal),
            original_owned_wait4_resource=compact(resource),
            original_logs_unmodified=True, ordinary_git_publication_delegated_to_root_runner=True,
            original_publication_failure="git diff --cached --check rejected original SciPy log trailing spaces",
            complete_topic_acceptance_claimed=False)
        if encoded_size(report) >= 96000:
            report["original_summary"] = {key:compact(summary[key]) for key in (
                "solver_success", "audit_pending", "error", "message", "modes", "nodes",
                "gauge_amplitude", "actual_primary_amplitude", "max_rms_collocation_residual",
                "summary", "core", "frozen_profile", "prescribed_actual_core") if key in summary}
            report["original_summary"]["actual_tail"] = {
                key:compact(summary.get("actual_tail",{}).get(key)) for key in (
                    "residual","audit","seam_nonmean","final_response","actual_physical_bc_tolerance")}
        if encoded_size(report) >= 96000:
            report["restored_files"] = dict(count=len(report["restored_files"]),
                original_manifest=report["original_stable_manifest"],
                note="Complete hashes stay in the original stable manifest; all were checked.")
        report["recovery_report_bytes_before_final_field"] = encoded_size(report)
        atomic_json(output, report)
        print(json.dumps(dict(event="strong_original_CI_artifact_restored",
            artifact_id=ARTIFACT, files=72,
            original_stable_hashes_verified=report["original_stable_manifest"]["complete_original_files_verified"],
            summary_sha256=report["summary_sha256"], solver_success=summary.get("solver_success"),
            audit_pending=summary.get("audit_pending"), output=str(output),
            mathematical_recomputation=False, original_local_r7="unknown")), flush=True)
    except BaseException as error:
        token = None
        # Preserve a bounded failure record without network exception URLs or
        # authentication material. Original numerical/accepted files are never
        # deleted or modified on this path.
        failure = dict(scope=__doc__, entry_sha256=SELF_SHA,
            artifact_id=ARTIFACT, expected_zip_sha256=ZIP_SHA256,
            status="artifact-recovery-failed", finished_utc=utc(),
            error_type=type(error).__name__,
            error_message=(str(error)[:4000] if isinstance(error, (ValueError, FileExistsError, RuntimeError))
                else "See the concrete error class; network URLs and credentials are not logged."),
            completed_download=compact(report.get("download")),
            original_stable_manifest=compact(report.get("original_stable_manifest")),
            original_local_r7_terminal_status="unknown", mathematical_recomputation=False)
        print(json.dumps(dict(event="artifact_recovery_failed",
            error_type=failure["error_type"], error_message=failure["error_message"])), flush=True)
        if not output.exists():
            atomic_json(output, failure)
        raise RuntimeError("Immutable strong artifact recovery failed: "+type(error).__name__) from None


if __name__ == "__main__":
    main()
