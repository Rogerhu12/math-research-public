#!/usr/bin/env python3
"""Inspect and preserve the completed original full-flow output artifact.

This does not run a density or an ODE. It verifies the transport digest and
the complete saved output inventory, prints a small arithmetic-gate summary,
then publishes the original scientific bytes using terminal git on a fresh
branch based on current main. No personal access token is embedded or saved.
"""
from __future__ import annotations
import gzip, hashlib, json, os, subprocess, sys, time, zipfile
from pathlib import Path, PurePosixPath
from urllib.error import HTTPError
from fourfold_ci_complete_parameter_flow_v2 import download_artifact, portable, immutable_write, sha, read, save

RUN = 43301401638
ARTIFACT = 13982013301
SIZE = 8728467
DIGEST = "ff4126d25d86b5867cc3a99d66d09fda234797989d7b5fb19f6c58ac5249ca18"
ROOT = Path("data/phase_ring_continuation/step5_complete_flow_ci_43301401638")
SUMMARY = Path("notes/2026-11-12-complete-flow-43301401638-arithmetic-summary.json")
SCRIPT = Path("scripts/fourfold_ci_inspect_complete_flow_v2.py")
WORKFLOW = Path(".github/workflows/visible-exact-complete-flow-inspect.yml")


def git(args, *, capture=True):
    workspace = Path(os.environ["GITHUB_WORKSPACE"])
    import base64
    header = "AUTHORIZATION: basic "+base64.b64encode(
        ("x-access-token:"+os.environ["GITHUB_TOKEN"]).encode()).decode()
    command = ["git", "-c", "safe.directory="+str(workspace),
               "-c", "http.https://github.com/.extraheader="+header, *args]
    result = subprocess.run(command, cwd=workspace, text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None)
    if result.returncode:
        raise RuntimeError("git operation failed: "+args[0]+": "+
                           ((result.stderr or "")[-4000:]))
    return result.stdout or ""


def main():
    start = time.monotonic()
    download_dir = Path("ci-output/complete-flow-inspection")
    download_dir.mkdir(parents=True, exist_ok=True)
    archive_path = None
    for attempt in range(10):
        try:
            archive_path = download_artifact(ARTIFACT, SIZE, DIGEST, download_dir)
            break
        except HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 9:
                raise
            print("BOUNDED_ARTIFACT_BACKOFF", exc.code, 30, flush=True)
            time.sleep(30)
    if archive_path is None:
        raise RuntimeError("the completed output artifact remains unavailable")
    restored = []
    with zipfile.ZipFile(archive_path) as archive:
        for entry in archive.infolist():
            name = portable(entry.filename)
            if entry.is_dir():
                continue
            try:
                name.relative_to(PurePosixPath(str(ROOT)))
            except ValueError:
                continue
            raw = archive.read(entry)
            immutable_write(name, raw)
            restored.append(str(name))
    inventory_path = ROOT/"files.json.gz"
    inventory = read(inventory_path)
    if sha(ROOT/"execution.json") != inventory["execution_sha256"]:
        raise ValueError("full-flow inventory names another execution")
    files = {}
    for item in inventory["files"]:
        path = Path(portable(item["path"]))
        path.relative_to(ROOT)
        if (not path.is_file() or path.stat().st_size != item["bytes"]
            or sha(path) != item["sha256"]):
            raise ValueError("completed flow output inventory mismatch")
        if item["path"] in files:
            raise ValueError("duplicate complete output inventory path")
        files[item["path"]] = item
    if set(restored) != set(files) | {str(inventory_path)}:
        raise ValueError("an output artifact file is outside its full inventory")
    g0 = read(ROOT/"g0/index.json.gz")
    center = read(ROOT/"center_chronological/report.json.gz")
    hybrid = read(ROOT/"hybrid_chronological/report.json.gz")
    endpoint = read(ROOT/"actual_endpoint.json.gz")
    if any(not item.get("complete") or not item.get("whole_forward_leg")
           or item.get("completed_segments") != 550 for item in (g0, center, hybrid)):
        raise ValueError("the actual saved flow is not the complete 550-segment input")
    for item in (center, hybrid):
        link = item["coefficients"]
        if sha(link["path"]) != link["sha256"]:
            raise ValueError("complete chronological coefficient bytes changed")
    endpoint_fields = (
        "kind","stage","failure","complete_true_center_return",
        "complete_true_uniform_parameter_box","actual_R31_accepted",
        "source_sha256","descriptor_sha256","exact_delta_fraction",
        "exact_parameter_half_width","widths","finite_H_constants","half",
        "half_real_mean","real_inverse_constants","accepted_half_twist_lower",
        "uniform_inverse_gate","uniform_first_and_second_endpoint_bounds",
        "true_uniform_parameter_tightening","sharp_half","full_square","R31",
        "finite_endpoint_coefficients","scope")
    summary = dict(kind="actual_full_flow_gate_summary", complete=True,
        original_run=RUN, original_artifact_id=ARTIFACT,
        original_artifact_sha256=DIGEST, inventory_sha256=sha(inventory_path),
        all_original_output_bytes_verified=True, source_sha256=sha(__file__),
        no_density_or_ODE_recomputed=True,
        g0=dict(path=str(ROOT/"g0/index.json.gz"),sha256=sha(ROOT/"g0/index.json.gz"),
            completed_segments=g0["completed_segments"],leaves=len(g0["leaves"]),
            summary=g0["summary"],exact_final_time=g0["exact_final_time"]),
        center=dict(path=str(ROOT/"center_chronological/report.json.gz"),
            sha256=sha(ROOT/"center_chronological/report.json.gz"),
            coefficients=center["coefficients"],signed_zero_modes_C=center["signed_zero_modes_C"],
            signed_zero_modes_D=center["signed_zero_modes_D"]),
        hybrid=dict(path=str(ROOT/"hybrid_chronological/report.json.gz"),
            sha256=sha(ROOT/"hybrid_chronological/report.json.gz"),
            coefficients=hybrid["coefficients"],signed_zero_modes_C=hybrid["signed_zero_modes_C"],
            signed_zero_modes_D=hybrid["signed_zero_modes_D"]),
        endpoint={name:endpoint[name] for name in endpoint_fields if name in endpoint})
    encoded = json.dumps(summary, separators=(",",":"))
    if len(encoded.encode()) > 95000:
        raise ValueError("arithmetic summary exceeds the small-text integration limit")
    save(SUMMARY, summary)
    print("FLOW_SUMMARY_JSON_BEGIN", flush=True)
    print(encoded, flush=True)
    print("FLOW_SUMMARY_JSON_END", flush=True)
    source_bytes = SCRIPT.read_bytes()
    workspace = Path(os.environ["GITHUB_WORKSPACE"])
    workflow_bytes = (workspace/WORKFLOW).read_bytes()
    # The fetched main is the publication base, never a forced update.
    git(["fetch","--filter=blob:none","--depth=1","origin","main"])
    base_sha = git(["rev-parse","FETCH_HEAD"]).strip()
    branch = "visible-exact-complete-flow-results-"+os.environ["GITHUB_RUN_ID"]
    git(["switch","-c",branch,"FETCH_HEAD"])
    # The executing script is already loaded; preserve its exact source too.
    SCRIPT.write_bytes(source_bytes)
    (workspace/WORKFLOW).write_bytes(workflow_bytes)
    selected = [Path(name) for name in files] + [inventory_path, SUMMARY, SCRIPT]
    for path in selected:
        size = path.stat().st_size
        if size >= 5_000_000 or (size > 1_000_000 and path.suffix != ".gz"):
            raise ValueError("publication exceeds repository compressed-data size rules")
    topic = Path("topics/visible-flex-exact-nearby")
    relative = [str(topic/path) for path in selected] + [str(WORKFLOW)]
    git(["add","--sparse","--",*relative])
    git(["-c","user.name=github-actions[bot]",
         "-c","user.email=41898282+github-actions[bot]@users.noreply.github.com",
         "commit","-m","visible-flex: preserve complete 550 flow and actual failed R31 gates"])
    commit_sha = git(["rev-parse","HEAD"]).strip()
    git(["push","origin","HEAD:refs/heads/"+branch])
    publication = dict(complete=True, branch=branch, commit_sha=commit_sha,
        main_base_sha=base_sha, summary_sha256=sha(SUMMARY),
        scientific_files=len(files)+1, original_artifact_sha256=DIGEST,
        wall_seconds=time.monotonic()-start)
    save(download_dir/"publication.json", publication)
    print("PUBLICATION", json.dumps(publication), flush=True)
    archive_path.unlink()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
