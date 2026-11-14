#!/usr/bin/env python3
"""Resume only the missing42 exact phase germs in this public repository.

The original mathematical source and completed127 native checkpoints are
copied without modification. Scientific files live in an immutable runner
snapshot while terminal Git publishes small new checkpoints. No token is
written into any file, command log, native, or commit.
"""
from __future__ import annotations

import argparse
import datetime
import gzip
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

TOPIC = Path(__file__).resolve().parents[1]
REPO = TOPIC.parents[1]
RELATIVE_TOPIC = Path("topics/visible-flex-exact-nearby")
RULES = ("README.md", str(RELATIVE_TOPIC / "README.md"))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == ".gz" else raw)


def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(data, indent=2, allow_nan=False) + "\n").encode()
    if path.suffix == ".gz":
        raw = gzip.compress(raw, mtime=0)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_bytes(raw)
    temporary.replace(path)


class Worker:
    def __init__(self, args):
        self.args = args
        self.started = time.monotonic()
        self.child = None
        self.interrupted = False
        self.artifact = args.artifact_dir.resolve()
        self.artifact.mkdir(parents=True, exist_ok=True)
        self.native = self.artifact / "native"
        self.native.mkdir(exist_ok=True)
        self.log = self.artifact / "producer.stdout.log"
        self.statusfile = self.artifact / "process.json"
        self.run_label = os.environ.get("GITHUB_RUN_ID", "local") + "-" + os.environ.get("GITHUB_RUN_ATTEMPT", "1")
        self.name = "run-" + self.run_label
        self.science = self.artifact.parent / ("visible-exact-phase-science-" + self.run_label)
        self.dest = TOPIC / "notes/phase_transport_complete_ci" / self.name
        self.state = dict(kind="actual_exact_phase_transport_resume127_public_CI", complete=False,
            repository="Rogerhu12/math-research-public", run_id=os.environ.get("GITHUB_RUN_ID"),
            run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"), workflow_commit=os.environ.get("GITHUB_SHA"),
            worker_source_sha256=sha(__file__), started_utc=now(), child_exit_code=None,
            reused_completed_germs=127, requested_new_germs=[127, 169],
            seed_candidate_recomputed=False, completed127_transport_recomputed=False,
            readme_checks=[], published_checkpoints=[])
        self.env = dict(os.environ, GIT_TERMINAL_PROMPT="0", PYTHONDONTWRITEBYTECODE="1",
                        OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1")
        helper = '!f() { printf "%s\\n" "username=x-access-token" "password=$GITHUB_TOKEN"; }; f'
        self.gitbase = ["git", "-c", "safe.directory=" + str(REPO), "-c", "gc.auto=0",
            "-c", "maintenance.auto=false", "-c", "credential.helper=", "-c", "credential.helper=" + helper]
        self.read_commit = None

    def git(self, arguments, check=True):
        result = subprocess.run(self.gitbase + arguments, cwd=REPO, env=self.env, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=240)
        if check and result.returncode:
            print(result.stdout, flush=True)
            raise RuntimeError("actual terminal git " + arguments[0] + " failed")
        return result

    def sync(self):
        if self.read_commit is None:
            self.read_commit = self.git(["rev-parse", "HEAD"]).stdout.strip()
        self.git(["pull", "--rebase", "--no-tags", "origin", "main"])
        head = self.git(["rev-parse", "origin/main"]).stdout.strip()
        difference = self.git(["diff", self.read_commit, head, "--", *RULES]).stdout
        self.state["readme_checks"].append(dict(time=now(), before=self.read_commit, after=head, changed=bool(difference)))
        if difference:
            (self.artifact / "README-difference.txt").write_text(difference)
            self.state["readme_difference_requires_researcher_consumption"] = True
            print("ACTUAL_README_CHANGE\n" + difference, flush=True)
            raise RuntimeError("new rules require active researcher consumption; original native prefix is retained")
        self.read_commit = head
        self.state["last_read_commit"] = head

    def stage_exact_inputs(self):
        if sha(self.args.manifest) != self.args.manifest_sha:
            raise ValueError("the exact resume manifest changed")
        self.manifest = read(self.args.manifest)
        if os.environ.get("GITHUB_REPOSITORY") != self.manifest["repository"]:
            raise ValueError("this worker runs only in its authorized public repository")
        if self.manifest["reused_completed_germs"] != 127 or self.manifest["requested_new_germs"] != [127, 169]:
            raise ValueError("the worker must reuse the complete127 prefix and compute only the remaining42")
        for path, expected in self.manifest["readme_sha256"].items():
            if sha(REPO / path) != expected:
                raise ValueError("current repository rules differ from the reviewed resume manifest")
        packages = {name: importlib.metadata.version(name) for name in self.manifest["packages"]}
        if packages != self.manifest["packages"] or ".".join(map(str, sys.version_info[:3])) != self.manifest["python_version"]:
            raise ValueError("the original exact arithmetic runtime is required")
        for relative, expected in self.manifest["files"].items():
            path = Path(relative)
            if path.is_absolute() or ".." in path.parts:
                raise ValueError("a scientific input path escapes the public checkout")
            source = REPO / path
            if sha(source) != expected:
                raise ValueError("a pinned scientific source/input changed: " + relative)
            target = self.science / path
            target.parent.mkdir(parents=True, exist_ok=True)
            raw = source.read_bytes()
            if target.exists() and target.read_bytes() != raw:
                raise ValueError("an immutable scientific snapshot differs")
            if not target.exists():
                target.write_bytes(raw)
        self.science_topic = self.science / RELATIVE_TOPIC
        seeds = self.science / self.manifest["seed_transport_directory"]
        for index in range(127):
            source = seeds / f"transport-germ{index:04d}.json.gz"
            doc = read(source)
            if doc["last_complete_germ"] != index or not doc["complete_requested_prefix"]:
                raise ValueError("the original complete transport seed changed")
            target = self.native / source.name
            if target.exists() and target.read_bytes() != source.read_bytes():
                raise ValueError("a native output conflicts with the original completed prefix")
            if not target.exists():
                target.write_bytes(source.read_bytes())
        # Earlier attempts contain only their new germs; every one extends
        # the same exact original127-prefix, and duplicates must be identical.
        for index in range(127, 169):
            choices = sorted((TOPIC / "notes/phase_transport_complete_ci").glob(f"*/transport-germ{index:04d}.json.gz"))
            if not choices:
                break
            hashes = {sha(path) for path in choices}
            if len(hashes) != 1:
                raise ValueError("different published exact-source histories require researcher resolution")
            raw = choices[0].read_bytes()
            target = self.native / choices[0].name
            if target.exists() and target.read_bytes() != raw:
                raise ValueError("a previously published resume endpoint changed")
            if not target.exists():
                target.write_bytes(raw)
        self.state.update(input_manifest_sha256=self.args.manifest_sha,
            scientific_input_count=len(self.manifest["files"]), all_pinned_inputs_verified=True,
            package_versions=packages, python_version=sys.version,
            original_mathematical_source_unchanged=True,
            exact_candidate_sha256=self.manifest["candidate_sha256"],
            actual_starting_complete_germs=len(list(self.native.glob("transport-germ*.json.gz"))))
        save(self.statusfile, self.state)

    def snapshot(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        entries = []
        for path in sorted(self.native.glob("*.gz")):
            if path.name.startswith("transport-germ") and int(path.name[14:18]) < 127:
                continue
            raw = path.read_bytes()
            if len(raw) > 5_000_000:
                self.state.setdefault("artifact_only_large_files", {})[path.name] = dict(bytes=len(raw), sha256=sha(path))
                continue
            target = self.dest / path.name
            target.write_bytes(raw)
            entries.append(dict(file=path.name, bytes=len(raw), sha256=sha(path)))
        if self.log.exists():
            raw = gzip.compress(self.log.read_bytes(), mtime=0)
            if len(raw) <= 5_000_000:
                (self.dest / "producer.stdout.log.gz").write_bytes(raw)
        self.state.update(snapshot_utc=now(), wall_seconds=time.monotonic() - self.started,
            native_files=entries, observed_complete_transport_germs=len(list(self.native.glob("transport-germ*.json.gz"))))
        save(self.statusfile, self.state)
        save(self.dest / "process.json", self.state)

    def publish(self, final=False):
        self.sync()
        self.snapshot()
        relative = str(self.dest.relative_to(REPO))
        self.git(["add", "--sparse", "--", relative])
        if self.git(["diff", "--cached", "--quiet"], check=False).returncode == 0:
            return
        label = "complete" if final else "checkpoint"
        self.git(["commit", "-m", "visible-exact: " + label + " exact phase transport after reused127 germs"])
        while True:
            pushed = self.git(["push", "--no-thin", "origin", "HEAD:refs/heads/main"], check=False)
            print(pushed.stdout, flush=True)
            if pushed.returncode == 0:
                commit = self.git(["rev-parse", "HEAD"]).stdout.strip()
                self.state["published_checkpoints"].append(dict(time=now(), commit=commit, final=final))
                save(self.statusfile, self.state)
                print("ACTUAL_PHASE_CHECKPOINT_PUBLISHED " + commit, flush=True)
                return
            if not any(word in pushed.stdout for word in ("fetch first", "non-fast-forward", "rejected", "failed to update ref")):
                raise RuntimeError("actual push failed outside the concurrent-main-update case")
            self.sync()

    def terminate(self, reason):
        if self.child is None or self.child.poll() is not None:
            return
        self.state["termination_reason"] = reason
        os.killpg(self.child.pid, signal.SIGTERM)
        try:
            self.child.wait(timeout=20)
        except subprocess.TimeoutExpired:
            os.killpg(self.child.pid, signal.SIGKILL)
            self.child.wait(timeout=20)

    def run(self):
        if not os.environ.get("GITHUB_TOKEN"):
            raise RuntimeError("terminal Git publication identity is unavailable")
        self.git(["config", "user.name", "github-actions[bot]"])
        self.git(["config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"])
        self.sync()
        self.stage_exact_inputs()
        command = [sys.executable, "-u", str(self.science_topic / "scripts/fourfold_codazzi_phase_full_transport_Taylor.py"),
            "--candidate", str(self.science / self.manifest["candidate_path"]),
            "--root-contract", str(self.science / self.manifest["root_contract_path"]),
            "--scalar", str(self.science / self.manifest["first_scalar_path"]),
            "--scalar-dir", str(self.science_topic / "notes/phase_scalar_high7_ci"),
            "--resume", "--out-dir", str(self.native)]
        self.state["actual_command"] = command
        save(self.statusfile, self.state)
        with self.log.open("ab") as stream:
            self.child = subprocess.Popen(command, cwd=self.science_topic, env=self.env,
                stdout=stream, stderr=subprocess.STDOUT, start_new_session=True)
            previous = time.monotonic()
            while self.child.poll() is None:
                if self.interrupted:
                    self.terminate("actual runner signal observed")
                    break
                if time.monotonic() - self.started > self.args.compute_minutes * 60:
                    self.terminate("bounded runner allocation reached; same-source complete prefix retained")
                    break
                if time.monotonic() - previous > self.args.checkpoint_minutes * 60:
                    self.publish()
                    previous = time.monotonic()
                time.sleep(5)
        self.state["child_exit_code"] = self.child.returncode
        report_path = self.native / "report.json.gz"
        result = read(report_path) if report_path.exists() else {}
        complete = bool(self.child.returncode == 0 and result.get("whole_negative_domain") and result.get("processed_germs") == 169)
        if complete:
            consumer = [sys.executable, "-u", str(self.science_topic / "scripts/fourfold_codazzi_phase_complete_transport_cover.py"),
                "--transport-dir", str(self.native), "--scalar-cover", str(self.science / self.manifest["scalar_cover_path"]),
                "--root-contract", str(self.science / self.manifest["root_contract_path"]),
                "--out", str(self.native / "complete-169-cover.json.gz")]
            with self.log.open("ab") as stream:
                consumed = subprocess.run(consumer, cwd=self.science_topic, env=self.env,
                    stdout=stream, stderr=subprocess.STDOUT, timeout=1200)
            self.state["consumer_exit_code"] = consumed.returncode
            self.state["consumer_command"] = consumer
            complete = consumed.returncode == 0
        self.state.update(complete=complete, completed_utc=now(), all_original_failures_retained=True,
            whole_transport_complete=bool(result.get("whole_negative_domain")))
        self.publish(final=True)
        if not complete:
            raise RuntimeError("the actual complete169 phase transport was not obtained; valid prefix retained")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--artifact-dir", type=Path, required=True)
    parser.add_argument("--compute-minutes", type=int, default=310)
    parser.add_argument("--checkpoint-minutes", type=int, default=10)
    worker = Worker(parser.parse_args())
    def interrupted(signum, frame):
        worker.interrupted = True
        worker.state["runner_signal"] = int(signum)
    signal.signal(signal.SIGTERM, interrupted)
    signal.signal(signal.SIGINT, interrupted)
    try:
        worker.run()
    except BaseException as error:
        worker.terminate("worker exception: " + type(error).__name__)
        worker.state.update(complete=False, worker_exception=type(error).__name__ + ": " + str(error),
            child_exit_code=None if worker.child is None else worker.child.poll(),
            wall_seconds=time.monotonic() - worker.started)
        save(worker.statusfile, worker.state)
        raise


if __name__ == "__main__":
    main()
