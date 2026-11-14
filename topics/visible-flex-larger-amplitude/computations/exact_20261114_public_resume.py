#!/usr/bin/env python3
"""Complete the interrupted RK24/RK48 common-grid and closed-assembly work.

Run on this public repository's GitHub Actions. The two genuine fixed-H
shooting solves are already complete and archived; this driver does not
repeat them. It rebuilds their Cartesian node readouts in RUNNER_TEMP and
runs the existing source-knot-preserving comparison pipeline. Large,
reproducible node arrays stay on the runner. Only compact reports, hashes,
the three closed meshes, and their normal samples are returned in --out.

These are finite numerical calculations. Completing this job does not
certify a continuous reach bound, an exact limit, or the amplitude goal.
"""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time


def sha(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def read(path: Path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def utc() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def write(path: Path, value) -> None:
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")


def prepare_public_source(repo: Path, work: Path, out: Path) -> Path:
    """Restore the public numerical subset and verify every pinned byte."""
    manifest_path = repo / "topics/visible-flex-larger-amplitude/computations/source-dependencies.json"
    manifest = read(manifest_path)
    prefix = "topics/visible-flexible-closed-surface/"
    entries = [row for row in manifest["files"] if row["path"].startswith(prefix)]
    omitted = [row["path"] for row in manifest["files"] if not row["path"].startswith(prefix)]
    if len(entries) != 79 or len(manifest["files"]) != 91 or any(not p.endswith(".md") for p in omitted):
        raise ValueError("The pinned public numerical source subset changed")
    revision = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
    source_root = work / "public-source"
    restored = []
    for row in entries:
        relative = Path(row["path"])
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError("Unsafe repository-relative source path")
        # These are existing public-repository paths. No private remote,
        # private commit fetch, account token, or unverified cache is used.
        raw = subprocess.check_output(["git", "-C", str(repo), "show", revision + ":" + row["path"]])
        if len(raw) != row["bytes"] or hashlib.sha256(raw).hexdigest() != row["sha256"]:
            raise ValueError("Public source does not match the pinned bytes: " + row["path"])
        target = source_root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream:
            stream.write(raw)
        restored.append(dict(path=row["path"], bytes=len(raw), sha256=row["sha256"]))
    source = source_root / "topics/visible-flexible-closed-surface"
    record = dict(
        source_revision=manifest["source_revision"],
        source_revision_meaning="All restored numerical file bytes match this original pinned manifest",
        actual_public_repository="Rogerhu12/math-research-public", actual_public_commit=revision,
        source_manifest_sha256=sha(manifest_path), verified_file_count=len(restored),
        full_manifest_file_count=len(manifest["files"]), full_91_file_manifest_restored=False,
        restored_files=restored, omitted_nonexecuted_markdown=omitted,
        scope="Public numerical subset only. The twelve other-topic Markdown references are not required by the resolved RK readout/comparison pipeline.")
    write(source / "source-origin.json", record)
    write(out / "public-source-preparation.json", record)
    return source


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--source-topic", type=Path,
                        help="Optional prepared source; otherwise restore and hash-check the 79 public numerical files")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--comparison-processes", type=int, choices=(1, 2), default=2)
    args = parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise ValueError("Numerical execution belongs to this repository's GitHub Actions")
    if os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public":
        raise ValueError("This driver must run in Rogerhu12/math-research-public")

    repo = args.repo_root.resolve()
    topic = repo / "topics/visible-flex-larger-amplitude"
    comp, notes = topic / "computations", topic / "notes"
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    if any(out.iterdir()):
        raise ValueError("Use a fresh result directory")
    work = Path(tempfile.mkdtemp(prefix="visible-flex-exact-resume-", dir=os.environ.get("RUNNER_TEMP")))
    source = args.source_topic.resolve() if args.source_topic else prepare_public_source(repo, work, out)
    solve24 = notes / "2026-11-14-exact-resume-fixedH-RK24-r1"
    solve48 = notes / "2026-11-14-exact-resume-fixedH-RK48-r1"
    stem = "2026-11-13-strong-q126-m32-tail2-actual-r1"
    baseline_config = notes / (stem + "-config.json")
    baseline_response = notes / (stem + "-tail-response_0003.json.gz")
    lifecycle = out / "public-exact-lifecycle.jsonl"
    started = time.monotonic()
    commands, archive = [], []
    env = os.environ.copy()
    env.update(OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")

    def event(value):
        with lifecycle.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(value, ensure_ascii=False, allow_nan=False) + "\n")
        print(json.dumps(value, ensure_ascii=False, allow_nan=False), flush=True)

    def run(label, argv):
        row = dict(label=label, argv=list(map(str, argv)), started_utc=utc())
        event(dict(event="start", **row))
        before = time.monotonic()
        with (out / (label + ".log")).open("wb") as stream:
            result = subprocess.run(row["argv"], cwd=repo, env=env, stdout=stream, stderr=subprocess.STDOUT, check=False)
        row.update(actual_exit_code=result.returncode, seconds=time.monotonic() - before, finished_utc=utc())
        commands.append(row)
        event(dict(event="exit", **row))
        if result.returncode:
            raise RuntimeError(f"{label} exited {result.returncode}")

    def retain(path: Path, relative: Path):
        """Copy only a meaningful bounded output; always retain its hash."""
        record = dict(produced_file=str(path), bytes=path.stat().st_size, sha256=sha(path))
        destination = out / "reports" / relative
        if record["bytes"] > 1_000_000 and path.suffix in (".json", ".jsonl", ".log"):
            compressed = gzip.compress(path.read_bytes(), mtime=0)
            destination = destination.with_name(destination.name + ".gz")
            if len(compressed) < 5_000_000:
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(compressed)
            else:
                destination = None
        elif record["bytes"] < 5_000_000:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, destination)
        else:
            destination = None
        if destination is not None:
            record.update(retained_file=str(destination.relative_to(out)), retained_bytes=destination.stat().st_size,
                          retained_sha256=sha(destination))
        else:
            record["not_retained"] = "Reproducible output exceeds the repository's single-file limit"
        archive.append(record)

    hashes = {str(p.relative_to(repo)): sha(p) for p in (
        Path(__file__).resolve(), comp / "exact_20261114_RK48_cusp_pipeline_v3.py",
        comp / "exact_20261114_resolved_radial_readout.mjs", baseline_config, baseline_response,
        solve24 / "result.json", solve24 / "config.json", solve24 / "response.json.gz",
        solve48 / "result.json", solve48 / "config.json", solve48 / "response.json.gz")}
    write(out / "public-exact-intent.json", dict(
        schema="public-fixed-H-RK24-RK48-resume-intent-v1", started_utc=utc(), source_sha256=hashes,
        repository=os.environ["GITHUB_REPOSITORY"], actions_run_id=os.environ.get("GITHUB_RUN_ID"),
        actions_sha=os.environ.get("GITHUB_SHA"), working_directory=str(work),
        comparison_processes=args.comparison_processes, repeated_shooting_solves=False, scope=__doc__))

    success, failure = False, None
    pipeline = work / "RK48-source-partition"
    try:
        for directory, steps in ((solve24, 24), (solve48, 48)):
            result, config, response = (read(directory / name) for name in ("result.json", "config.json", "response.json.gz"))
            if not (result.get("finished") and result.get("success") and result.get("actual_exit_code") == 0
                    and response.get("converged") and response["residual"] < config["solveTolerance"]
                    and response.get("audit") and response.get("heightJetJacobian") and config["steps"] == steps):
                raise ValueError(f"The archived RK{steps} input is not a complete successful solve")
            expected = result.get("output_files", {}).get("response.json.gz")
            if expected != sha(directory / "response.json.gz"):
                raise ValueError(f"The archived RK{steps} response hash differs from its terminal record")
        old_readout = work / "RK24-regular-eight"
        run("RK24-rebuild-eight", [
            "node", "--expose-gc", "--max-old-space-size=384", "--max-semi-space-size=4",
            comp / "exact_20261114_resolved_radial_readout.mjs", "--repo-root", repo,
            "--source-topic", source, "--config", solve24 / "config.json", "--response", solve24 / "response.json.gz",
            "--baseline-config", baseline_config, "--baseline-response", baseline_response,
            "--levels", "1,8", "--out-dir", old_readout])
        run("RK48-source-partition", [
            sys.executable, "-u", comp / "exact_20261114_RK48_cusp_pipeline_v3.py",
            "--repo-root", repo, "--source-topic", source, "--solve-dir", solve48,
            "--old-solve-dir", solve24, "--old-readout", old_readout,
            "--out", pipeline, "--comparison-processes", args.comparison_processes])
        terminal = read(pipeline / "terminal.json")
        if not (terminal.get("finished") and terminal.get("success")
                and all(row["actual_exit_code"] == 0 for row in terminal["commands"])):
            raise ValueError("The common-grid/closed pipeline did not finish successfully")
        success = True
    except Exception as error:
        failure = str(error)
    finally:
        # Do not turn an interrupted stage checkpoint into a completed comparison.
        # The small component result and pipeline terminal retain their true status.
        if (work / "RK24-regular-eight/result.json").is_file():
            retain(work / "RK24-regular-eight/result.json", Path("RK24-readout-result.json"))
        if pipeline.is_dir():
            for path in sorted(pipeline.iterdir()):
                if path.is_file() and path.suffix in (".json", ".jsonl", ".npz", ".log"):
                    retain(path, Path(path.name))
            for dirname in ("regular48", "cusp24", "cusp48-eight", "cusp48-sixteen"):
                for name in ("result.json", "intent.json"):
                    path = pipeline / dirname / name
                    if path.is_file():
                        retain(path, Path(dirname) / name)
            closed = pipeline / "closed"
            if closed.is_dir():
                for path in sorted(closed.iterdir()):
                    if path.is_file():
                        retain(path, Path("closed") / path.name)
        write(out / "public-exact-artifacts.json", dict(files=archive,
              omitted_reproducible_arrays="Cartesian node payloads and large complete/background tables remain in RUNNER_TEMP"))
        result = dict(schema="public-fixed-H-RK24-RK48-resume-terminal-v1", finished=True,
                      success=success, failure=failure, finished_utc=utc(), seconds=time.monotonic() - started,
                      commands=commands, source_sha256=hashes, task_completed=False,
                      repeated_shooting_solves=False, scope=__doc__)
        write(out / "public-exact-terminal.json", result)
        event(dict(event="terminal", success=success, failure=failure, seconds=result["seconds"]))
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
