#!/usr/bin/env python3
"""Regenerate the observed strong branch, then consume it in the same job.

Only scalar receipts and source/output hashes are published. Every full state,
normal and stdout file stays in runner/temp. A request names the explicit next
objective transition; no old fixed-peak set is silently used for a long run.
"""
from __future__ import annotations
import argparse
import base64
from datetime import datetime, timezone
import hashlib
import io
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import selectors
import shutil
import subprocess
import sys
import tarfile
import time

TOPIC = Path("topics/visible-flexible-closed-surface")
SCRIPTS = TOPIC / "scripts"
RULES = ["README.md", str(TOPIC / "README.md")]
HANDOFF = TOPIC / "HANDOFF.md"
HANDOFF_MARKER = "<!-- 6a65-ci-rules -->"
CANDIDATE = TOPIC / "notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json"
INITIAL = TOPIC / "notes/2026-11-13-fd2d-R211-full-half-01-initial.json"
METRIC_RUNNER = "6a65-run-metric-branch-recovered-20261126.cjs"
GAP_INIT = "6a65-geometry-gap-length-value.cjs"
GAP_RUNNER = "6a65-geometry-run-gap-length.cjs"
PEAK_RUNNER = "6a65-geometry-run-fixed-peak.cjs"
ANGULAR_INIT = "6a65-gap-fixed-peak-angular-injection.cjs"
OBSERVER = "6a65-gap-refined-metric-observer.cjs"
REQUEST_SCHEMA = "6a65-strong-branch-actions-request-v1"
FOLLOWUP_SCHEMA = "6a65-strong-branch-same-job-followup-v1"
GAP_SCHEMA = "6a65-gap-length-R215-checkpoint-v1"
PEAK_SCHEMA = "6a65-fixed-peak-metric-R215-checkpoint-v1"


def utc():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def json_sha(value):
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    return hashlib.sha256(encoded).hexdigest()


def number(value):
    return "—" if value is None else format(value, ".15g") if isinstance(value, (int, float)) else str(value)


def concurrent_push_rejection(message):
    # This includes the actual run-45767322734 ref-CAS failure, while leaving
    # permission, hook and network failures visible instead of retrying them.
    return bool(re.search(
        r"non-fast-forward|fetch first|\[rejected\]|"
        r"cannot lock ref ['\"]refs/heads/main['\"][^\n]*(?:is at [0-9a-f]+ but expected [0-9a-f]+|incorrect old value provided)|"
        r"\[remote rejected\][^\n]*->\s*main\b[^\n]*(?:is at [0-9a-f]+ but expected [0-9a-f]+|incorrect old value provided)",
        message, re.IGNORECASE))


def field(value, dotted, default=None):
    for part in dotted.split("."):
        if not isinstance(value, dict) or part not in value:
            return default
        value = value[part]
    return value


def positive_integer(value, label, maximum):
    if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= maximum:
        raise ValueError(f"{label} must be an integer from 1 through {maximum}")
    return value


def script_name(value):
    if not isinstance(value, str) or not re.fullmatch(r"6a65-[A-Za-z0-9_.-]+\.cjs", value):
        raise ValueError("A topic-local 6a65-*.cjs entry name is required")
    return value


def suffix(value):
    if not isinstance(value, str) or not re.fullmatch(r"-[A-Za-z0-9_-]+\.json", value):
        raise ValueError("A plain -name.json output suffix is required")
    return value


def parse_plan(request):
    if request.get("schema") != REQUEST_SCHEMA:
        raise ValueError("Unknown strong-branch request schema")
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,80}", str(request.get("request_id", ""))):
        raise ValueError("Plain request_id required")
    if not re.fullmatch(r"[0-9a-f]{40}", str(request.get("rules_read_commit", ""))):
        raise ValueError("The root session's actually read rules commit is required")
    heap = positive_integer(request.get("heap_mb", 512), "heap_mb", 8192)
    if heap < 64:
        raise ValueError("heap_mb must be at least 64")
    observation = request.get("observation", {})
    if not isinstance(observation, dict):
        raise ValueError("observation must be an object")
    positive_integer(observation.get("radial_subdivisions", 4), "radial_subdivisions", 32)
    positive_integer(observation.get("half_angle_intervals", 128), "half_angle_intervals", 512)
    stages = request.get("continuations")
    if not isinstance(stages, list) or not 1 <= len(stages) <= 12:
        raise ValueError("One through twelve explicit same-job continuation stages are required")
    labels, total_steps = set(), 0
    placeholders = {"{candidate}", "{source}", "{observer}", "{prefix}", "{recipe}"}
    for stage in stages:
        if not isinstance(stage, dict):
            raise ValueError("Each continuation must be an object")
        label = stage.get("label", "")
        if not re.fullmatch(r"[A-Za-z0-9_-]{1,50}", label) or label in labels:
            raise ValueError("Unique plain continuation labels are required")
        labels.add(label)
        if stage.get("transition_kind") not in (
                "fixed_rows_new_objective", "new_discretization_and_geometry_guide", "same_field_radial_refinement"):
            raise ValueError("The new objective/discretization transition must be named explicitly")
        for key in ("init_script", "run_script"):
            script_name(stage.get(key))
        for key in ("initial_suffix", "checkpoint_suffix"):
            suffix(stage.get(key))
        if stage.get("report_suffix") is not None:
            suffix(stage["report_suffix"])
        for key in ("initial_schema", "checkpoint_schema", "accepted_counter"):
            if not isinstance(stage.get(key), str) or not stage[key] or len(stage[key]) > 160:
                raise ValueError(f"Explicit {key} required")
        for key in ("init_arguments", "run_arguments"):
            args = stage.get(key)
            if not isinstance(args, list) or not args or len(args) > 20:
                raise ValueError("Explicit bounded argv arrays are required")
            for value in args:
                if not isinstance(value, (str, int, float)) or isinstance(value, bool):
                    raise ValueError("argv entries must be strings or numbers")
                if isinstance(value, str) and ("{" in value or "}" in value) and value not in placeholders:
                    raise ValueError("Only complete documented argv placeholders are accepted")
            if "{candidate}" not in args or "{source}" not in args or "{prefix}" not in args:
                raise ValueError("Each entry must explicitly consume candidate/source/prefix")
        if "{recipe}" in stage["init_arguments"] and not stage.get("recipe"):
            raise ValueError("The requested recipe placeholder needs a tracked small input")
        count = positive_integer(stage.get("steps"), "continuation steps", 60)
        prior = stage.get("prior_observed_steps", 0)
        if isinstance(prior, bool) or not isinstance(prior, int) or not 0 <= prior <= count:
            raise ValueError("prior_observed_steps must be between zero and requested steps")
        total_steps += count
    if total_steps > 60:
        raise ValueError("At most sixty continuation steps per scalar report")
    return stages


class RulesChanged(RuntimeError):
    pass


class Controller:
    def __init__(self, args):
        self.repo = Path(__file__).resolve().parents[3]
        self.out = args.out_dir.resolve()
        if self.out.is_relative_to(self.repo):
            raise ValueError("Raw runner outputs must stay outside the Git worktree")
        self.out.mkdir(parents=True, exist_ok=False)
        self.frozen = self.out / "source"
        request_path = (self.repo / args.request).resolve()
        if not request_path.is_relative_to(self.repo / TOPIC / "ci-requests"):
            raise ValueError("Request must be in the topic ci-requests directory")
        self.request = json.loads(request_path.read_text())
        self.plan = parse_plan(self.request)
        tail = self.request.get("same_job_followup")
        if not isinstance(tail, dict):
            raise ValueError("An explicit same_job_followup reception path is required")
        self.followup_path = Path(tail.get("path", ""))
        if self.followup_path.is_absolute() or self.followup_path.parent != TOPIC / "ci-requests" or not re.fullmatch(r"6a65-[A-Za-z0-9_-]+\.json", self.followup_path.name):
            raise ValueError("The followup packet must be a named small topic ci-request")
        if self.followup_path == args.request:
            raise ValueError("The followup path must not be the workflow's trigger request")
        self.poll_seconds = positive_integer(tail.get("poll_seconds", 30), "poll_seconds", 60)
        if self.poll_seconds < 15:
            raise ValueError("Use at least fifteen seconds between followup pulls")
        self.request_sha = sha(request_path)
        shutil.copyfile(request_path, self.out / "request.json")
        self.heap = self.request.get("heap_mb", 512)
        observation = self.request.get("observation", {})
        self.observer_radial = observation.get("radial_subdivisions", 4)
        self.observer_angles = observation.get("half_angle_intervals", 128)
        self.rules_read = self.request["rules_read_commit"]
        self.checked_rules, self.last_pull = self.rules_read, 0.0
        self.run_id, self.attempt = os.environ.get("GITHUB_RUN_ID", ""), os.environ.get("GITHUB_RUN_ATTEMPT", "1")
        self.repository = os.environ.get("GITHUB_REPOSITORY", "")
        if self.repository != "Rogerhu12/math-research-public" or not self.run_id.isdigit() or not self.attempt.isdigit():
            raise ValueError("This controller requires the actual authorized repository/Actions run")
        self.report = TOPIC / f"notes/2026-11-26-6a65-actions-strong-{self.run_id}-{self.attempt}.md"
        token = os.environ.get("GH_TOKEN", "")
        if not token:
            raise ValueError("GH_TOKEN environment credential is required")
        self.auth = os.environ.copy()
        self.auth["GIT_TERMINAL_PROMPT"] = "0"
        count = int(self.auth.get("GIT_CONFIG_COUNT", "0"))
        self.auth["GIT_CONFIG_COUNT"] = str(count + 2)
        self.auth[f"GIT_CONFIG_KEY_{count}"] = "http.https://github.com/.extraheader"
        self.auth[f"GIT_CONFIG_VALUE_{count}"] = "AUTHORIZATION: basic " + base64.b64encode(("x-access-token:" + token).encode()).decode()
        self.auth[f"GIT_CONFIG_KEY_{count + 1}"] = "credential.helper"
        self.auth[f"GIT_CONFIG_VALUE_{count + 1}"] = ""
        # Rebase needs identity too; these two local settings contain no secret.
        self.git("config", "--local", "user.name", "github-actions[bot]")
        self.git("config", "--local", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
        self.source_commit = self.git("rev-parse", "HEAD", emit=False).stdout.strip()
        self.rows, self.transitions, self.observations, self.receipts, self.pulls = [], [], [], [], []
        self.source_epochs, self.followup_packets, self.used_followups = [], [], set()
        self.used_stage_labels = {s["label"] for s in self.plan}
        self.awaiting = None
        self.stall = None
        self.started, self.status, self.failure = utc(), "running", None
        self.publication_failed = False
        self.source_hashes, self.source_digest = {}, None
        self.controller_sha = sha(Path(__file__))
        self.manifest_path = self.out / "scalar-run-manifest.json"
        self.git("switch", "-c", f"visible-flex-6a65-strong-{self.run_id}-{self.attempt}")
        self.freeze_sources()
        if self.git("cat-file", "-e", self.rules_read + "^{commit}", check=False, emit=False).returncode:
            self.git("fetch", "--filter=blob:none", "--depth=1", "origin", self.rules_read)
        self.sync_rules("startup")
        self.save()

    def git(self, *arguments, check=True, emit=True):
        result = subprocess.run(["git", *arguments], cwd=self.repo, env=self.auth, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if emit and result.stdout:
            print(result.stdout, end="", flush=True)
        if emit and result.stderr:
            print(result.stderr, end="", file=sys.stderr, flush=True)
        if check and result.returncode:
            raise RuntimeError(f"git {arguments[0]} exited {result.returncode}")
        return result

    def freeze_sources(self, commit=None):
        snapshot = commit or self.source_commit
        prefix = f"source-{len(self.source_epochs):03d}"
        destination = self.out / prefix
        tracked = self.git("ls-tree", "-r", "-z", "--name-only", snapshot, "--", str(SCRIPTS), emit=False).stdout.split("\0")
        paths = {Path(p) for p in tracked if p} | {CANDIDATE, INITIAL}
        entries = {METRIC_RUNNER, GAP_INIT, GAP_RUNNER, PEAK_RUNNER, ANGULAR_INIT, OBSERVER,
                   Path(__file__).name}
        for stage in self.plan:
            entries.update((stage["init_script"], stage["run_script"]))
            if stage.get("recipe"):
                rel = Path(stage["recipe"])
                if rel.is_absolute() or ".." in rel.parts or not rel.is_relative_to(TOPIC):
                    raise ValueError("Recipe must be a topic-local relative path")
                size = int(self.git("cat-file", "-s", f"{snapshot}:{rel.as_posix()}", emit=False).stdout)
                if size >= 100_000:
                    raise ValueError("Only a small reproducible recipe may be frozen")
                paths.add(rel)
        for name in entries:
            if SCRIPTS / name not in paths:
                raise ValueError(f"Required entry is not tracked in the trigger commit: {name}")
        # Snapshot the named public ancestor, not a changing checkout. Archive
        # paths are checked individually; no unchecked extractall is used.
        archived = subprocess.run(["git", "archive", "--format=tar", snapshot, "--", *map(str, sorted(paths))],
            cwd=self.repo, env=self.auth, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if archived.returncode:
            print(archived.stderr.decode(errors="replace"), file=sys.stderr, flush=True)
            raise RuntimeError("Could not freeze the declared source commit")
        destination.mkdir(parents=True, exist_ok=False)
        found = set()
        with tarfile.open(fileobj=io.BytesIO(archived.stdout), mode="r:") as archive:
            for member in archive:
                relative = PurePosixPath(member.name)
                if relative.is_absolute() or ".." in relative.parts:
                    raise ValueError("Unexpected archived path")
                if member.isdir():
                    continue
                rel = Path(relative)
                if rel not in paths or not member.isfile():
                    raise ValueError("Expected tracked regular source files only")
                dest = destination / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                with archive.extractfile(member) as handle:
                    dest.write_bytes(handle.read())
                found.add(rel)
        if found != paths:
            raise RuntimeError("Declared source snapshot is incomplete")
        self.frozen = destination
        inventory = [{"path": rel.as_posix(), "sha256": sha(self.frozen / rel)} for rel in sorted(paths)]
        self.source_digest = json_sha(inventory)
        (self.out / f"{prefix}-inventory.json").write_text(json.dumps(inventory, indent=2) + "\n")
        candidate_sha = sha(self.frozen / CANDIDATE)
        if self.source_epochs and candidate_sha != self.source_epochs[0]["candidate_sha256"]:
            raise RuntimeError("A same-job source update changed the frozen physical candidate input")
        self.source_epochs.append({"epoch": prefix, "commit": snapshot, "inventory_sha256": self.source_digest,
                                   "candidate_sha256": candidate_sha, "utc": utc()})
        for rel in {CANDIDATE, INITIAL} | {SCRIPTS / n for n in entries}:
            self.source_hashes[f"{prefix}/{rel}"] = sha(self.frozen / rel)
        for stage in self.plan:
            if stage.get("recipe"):
                self.source_hashes[f"{prefix}/{stage['recipe']}"] = sha(self.frozen / stage["recipe"])
        self.node_version = subprocess.check_output(["node", "--version"], text=True).strip()

    def pull_rules_once(self, reason):
        # Call with a clean worktree; commit this pull's H/report receipt
        # before any subsequent pull or numerical work.
        print("RUN git pull --rebase origin main", flush=True)
        pulled = self.git("pull", "--rebase", "origin", "main", check=False)
        repaired = False
        if pulled.returncode:
            self.resolve_handoff_marker_rebase()
            repaired = True
        remote = self.git("rev-parse", "origin/main", emit=False).stdout.strip()
        diff = self.git("diff", self.checked_rules, remote, "--", *RULES).stdout
        self.pulls.append({"utc": utc(), "reason": reason, "from": self.checked_rules,
                           "to": remote, "readme_diff_empty": not bool(diff.strip()),
                           "pull_command_exit": pulled.returncode, "handoff_marker_rebase_repaired": repaired})
        handoff = self.git("rev-parse", f"{remote}:{HANDOFF}", check=False, emit=False)
        self.pulls[-1]["handoff_blob_at_pull"] = handoff.stdout.strip() if not handoff.returncode else None
        self.last_pull = time.monotonic()
        if diff.strip():
            (self.out / "UNREVIEWED_README_DIFF.patch").write_text(diff)
            self.status = "unreviewed_readme_change"
            self.failure = "README changed; the root session must read the printed diff and update the request."
            print("UNREVIEWED_README_DIFF: no automatic-compliance claim; numeric child stops.", flush=True)
        else:
            self.checked_rules = remote
        self.write_handoff_receipt(remote, reason, bool(diff.strip()))
        self.save()
        return bool(diff.strip())

    def resolve_handoff_marker_rebase(self):
        while True:
            conflicts = self.git("diff", "--name-only", "--diff-filter=U", emit=False).stdout.splitlines()
            if conflicts != [str(HANDOFF)] or self.git("rev-parse", "--verify", "REBASE_HEAD", check=False, emit=False).returncode:
                raise RuntimeError("Pull/rebase failed outside a verified CI-marker-only HANDOFF conflict")
            base = self.git("show", f":1:{HANDOFF}", emit=False).stdout
            upstream = self.git("show", f":2:{HANDOFF}", emit=False).stdout
            picked = self.git("show", f":3:{HANDOFF}", emit=False).stdout
            def split_marker(text):
                lines = text.splitlines(keepends=True)
                markers = [line for line in lines if line.startswith(HANDOFF_MARKER)]
                if len(markers) > 1:
                    raise RuntimeError("Cannot reconcile duplicate HANDOFF markers")
                return "".join(line for line in lines if not line.startswith(HANDOFF_MARKER)), markers
            base_other, _ = split_marker(base)
            picked_other, markers = split_marker(picked)
            if base_other != picked_other or len(markers) != 1:
                raise RuntimeError("Conflicting local HANDOFF change is not exclusively this CI marker")
            # During rebase, stage 2 is the public upstream text and stage 3
            # is the local commit being replayed. Preserve stage 2 byte for
            # byte outside the single marker, then replay only that marker.
            lines = upstream.splitlines(keepends=True)
            positions = [i for i, line in enumerate(lines) if line.startswith(HANDOFF_MARKER)]
            if len(positions) > 1:
                raise RuntimeError("Upstream HANDOFF has duplicate markers")
            if positions:
                lines[positions[0]] = markers[0]
            else:
                lines.insert(1, markers[0])
            merged = "".join(lines)
            if split_marker(merged)[0] != split_marker(upstream)[0]:
                raise RuntimeError("Marker reconciliation changed upstream nonmarker text")
            (self.repo / HANDOFF).write_text(merged)
            self.git("add", "--", str(HANDOFF))
            continued = self.git("-c", "core.editor=true", "rebase", "--continue", check=False)
            if continued.returncode == 0:
                print("REBASE_HANDOFF_MARKER_ONLY_RESOLVED: upstream nonmarker text preserved", flush=True)
                return

    def write_handoff_receipt(self, remote, reason, changed):
        path = self.repo / HANDOFF
        lines = path.read_text().splitlines(keepends=True)
        positions = [i for i, line in enumerate(lines) if line.startswith(HANDOFF_MARKER)]
        if len(positions) > 1:
            raise RuntimeError("Duplicate CI HANDOFF markers need root reconciliation")
        state = "双 README 差异未审，已打印并停数值步骤" if changed else "双 README 无差异，沿用根已读规则"
        line = (f"{HANDOFF_MARKER} run {self.run_id}/{self.attempt}；实际 pull #{len(self.pulls)} "
                f"至 `{remote}`；{self.pulls[-1]['utc']}；{state}；回执原因 {reason}。\n")
        if positions:
            lines[positions[0]] = line
        else:
            lines.insert(1, line)
        updated = "".join(lines)
        if len(updated.encode()) >= 10_000:
            raise RuntimeError("HANDOFF would exceed its Markdown size limit")
        path.write_text(updated)

    def commit_receipt(self, reason):
        self.save()
        dest = self.repo / self.report
        dest.parent.mkdir(parents=True, exist_ok=True)
        text = self.report_text()
        if len(text.encode()) >= 100_000:
            raise RuntimeError("Scalar Markdown report would exceed 100KB")
        dest.write_text(text)
        self.git("add", "--", str(self.report), str(HANDOFF))
        self.git("commit", "-m", f"visible-flex: {self.request['request_id']} {reason}",
                 "--", str(self.report), str(HANDOFF))

    def sync_rules(self, reason):
        changed = self.pull_rules_once(reason)
        self.commit_receipt(reason)
        while True:
            result = self.git("push", "origin", "HEAD:main", check=False)
            if result.returncode == 0:
                break
            if not concurrent_push_rejection(result.stdout + result.stderr):
                self.publication_failed = True
                raise RuntimeError("Push failed outside the identified concurrent-ref cases; see actual Git output")
            changed = self.pull_rules_once("concurrent-main-ref-retry") or changed
            # Rebase may find our prior commit already on main. Add a normal
            # receipt commit; never amend a possibly already-published HEAD.
            self.commit_receipt("concurrent main ref retry receipt")
        if changed:
            raise RulesChanged(self.failure)

    def save(self):
        payload = {"schema": "6a65-strong-branch-actions-scalar-manifest-v1", "request": self.request,
            "request_sha256": self.request_sha, "run_id": self.run_id, "attempt": self.attempt,
            "source_commit": self.source_commit, "source_inventory_sha256": self.source_digest,
            "source_hashes": self.source_hashes, "node_version": getattr(self, "node_version", None),
            "actual_loaded_controller_sha256": self.controller_sha, "source_epochs": self.source_epochs,
            "same_job_followup_packets": self.followup_packets, "same_job_followup_path": str(self.followup_path),
            "awaiting_same_job_followup": self.awaiting, "stalled_state_retained": self.stall,
            "started_utc": self.started, "updated_utc": utc(), "status": self.status, "failure": self.failure,
            "root_read_rules_commit": self.rules_read, "last_unchanged_rules_check": self.checked_rules,
            "pulls": self.pulls, "steps": self.rows, "transitions": self.transitions,
            "observations": self.observations, "process_receipts": self.receipts,
            "continuous_certificate": False, "strong_target_complete": False, "raw_outputs_published": False}
        self.manifest_path.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n")

    def report_text(self):
        lines = [f"# 强分支同 job 续算：Actions {self.run_id}, attempt {self.attempt}", "",
            "**可信度：启发式/数值证据。** 本记录只报告实际有限目标试步和采样；"
            "不构成连续精确解、全域误差、闭曲面 reach 或课题完成证书。", "",
            f"- [真实 run](https://github.com/{self.repository}/actions/runs/{self.run_id})；状态 {self.status}。"
            "本页状态是最近一次成功发布时的状态；是否仍运行须同时查 Actions 的实际终态。",
            f"- 请求 {self.request['request_id']}；源码提交 {self.source_commit}；Node {self.node_version}；heap {self.heap} MB。",
            f"- 实际已载入 controller SHA-256 {self.controller_sha}。后继数值源码各自按指定公开祖先提交冻结；"
            "后来拉取的 controller 文件不冒充当前 Python 已加载程序。",
            "- 先恢复已见配方：原目标 2 步 → quartic metric 6 步 → gap=1/Δ=.05 新基线 → gap 3 步 "
            "→ 原 42 固定峰点 3 步 → K7→11 零注入 → K11 的 3 步。以上重生不计新研究结果。",
            "- 后续每个阶段显式建立新 objective/discretization 的 baseline、重置本阶段计数，"
            "每次完整 LM 固定其点集并保留全部参数列；其实际末态在 runner 退出前继续密观察及下一阶段。",
            f"- 根会话实际读规则于 {self.rules_read}；最后真实 pull 后双 README 无变化比较到 {self.checked_rules}。"
            "如有差异则打印并标明未审，交由根会话读取，不能自称已理解新规则。",
            "- 每次实际 pull 的提交号同时写入 HANDOFF 唯一 `<!-- 6a65-ci-rules -->` 行，"
            "与本标量报告普通 commit/push；根会话其余 HANDOFF 段不由 CI 改写。",
            f"- 源码清单 SHA-256 {self.source_digest}；请求 SHA-256 {self.request_sha}。"
            "数组、normal、完整 checkpoint 与 stdout 只在 runner/temp，不上传 artifact/Release。",
            f"- 开始 {self.started}；更新 {utc()}。exit 为 Python 等待到的真实 OS 结果。", "",
            "## 实际完整试步", "",
            "| 阶段/步 | 用途 | 接受 | α | R² baseline → end | metric 原网格 / 加点 / max | κ | max abs(y) | held | A / Zc | exit | 秒 |",
            "|---|---|---:|---:|---|---|---:|---:|---:|---|---:|---:|"]
        for r in self.rows:
            lines.append("| " + " | ".join([f"{r['stage']}/{r['iteration']}", r["purpose"],
                "是" if r["accepted"] else "否", number(r.get("alpha")),
                number(r.get("baseline_squared_norm")) + " → " + number(r.get("squared_norm")),
                " / ".join(number(r.get(k)) for k in ("original_grid_metric", "added_peak_metric", "sample_metric")),
                number(r.get("sample_curvature")), number(r.get("sample_max_y")), number(r.get("sample_held")),
                number(r.get("amplitude")) + " / " + number(r.get("actual_cuff_height")),
                str(r["exit_code"]), number(r["wall_seconds"])]) + " |")
        lines += ["", "held 为有限 guide 见证，不是整个闭曲面的 Hausdorff 结论；"
                  "rho 仍为度量设计参数。目标下降也不自动给出峰值或 reach 改善。", "",
                  "## 阶段转换的新基线", "",
                  "| 阶段 | 类型 | 维数 | N / K | 固定点数 | 新 R² | sample metric | sample κ | exit |",
                  "|---|---|---:|---|---:|---:|---:|---:|---:|"]
        for r in self.transitions:
            lines.append("| " + " | ".join([r["label"], r["kind"], str(r["dimension"]),
                f"{r['angles']} / {r['modes']}", str(r.get("peak_rows", 0)), number(r["squared_norm"]),
                number(r["sample_metric"]), number(r["sample_curvature"]), str(r["exit_code"])]) + " |")
        lines += ["", "转换和重评不是优化接受步；各阶段只能和自己的 baseline 比较。", "",
                  "## 同一实际场的额外观察", "",
                  "| 观察 | 点数 | metric | (s,u) | κ | 最小 immersion | exit |",
                  "|---|---:|---:|---|---:|---:|---:|"]
        for r in self.observations:
            lines.append("| " + " | ".join([r["label"], str(r["point_count"]), number(r["metric"]),
                f"({number(r['metric_s'])}, {number(r['metric_u'])})", number(r["curvature"]),
                number(r["minimum_immersion"]), str(r["exit_code"])]) + " |")
        lines += ["", "## 实际临时输出身份", "",
                  "| 阶段 | checkpoint/initial/observation SHA-256 | stdout SHA-256 |",
                  "|---|---|---|"]
        for r in self.rows + self.transitions + self.observations:
            label = f"{r['stage']}/{r['iteration']}" if "stage" in r else r["label"]
            lines.append(f"| {label} | {r.get('output_sha256') or 'none'} | {r['stdout_sha256']} |")
        lines += ["", "转换附带 report 的 SHA-256：", ""]
        for r in self.transitions:
            if r.get("report_sha256"):
                lines.append(f"- {r['label']}：{r['report_sha256']}；输入 {r['input_sha256']}。")
        lines += ["", "## 同 job 后继接收状态", "",
                  f"后继小配方路径为 `{self.followup_path}`，不触发另一个 job。每阶段末尾先真实 observer，"
                  "再保留 raw 等根会话的严格匹配配方；每次轮询只读 fetch 并输出带 UTC 的运行 heartbeat。"
                  "新配方待消费或距上次 pull 达45分钟时，才真实 pull 并把 SHA 写进 HANDOFF 推送。"
                  "静态页面的等待标记不能替代 Actions 实际终态和最新日志。", "",
                  "| 后继 ID | 动作 | 小配方 SHA-256 | 输入 checkpoint SHA-256 | observer SHA-256 |",
                  "|---|---|---|---|---|"]
        for packet in self.followup_packets:
            lines.append("| " + " | ".join([packet["followup_id"], packet["action"], packet["packet_sha256"],
                packet["parent_state_sha256"], packet["parent_observer_sha256"]]) + " |")
        if self.awaiting:
            lines += ["", f"当前留在 runner 内的 checkpoint SHA-256：{self.awaiting['state_sha256']}；"
                      f"observer SHA-256：{self.awaiting['observer_sha256']}。"
                      f"匹配 run_id={self.run_id}、attempt={self.attempt}；等待开始 {self.awaiting['since_utc']}。"]
        lines += ["", "| 数值 source epoch | 指定公开提交 | 全清单 SHA-256 |", "|---|---|---|"]
        for epoch in self.source_epochs:
            lines.append(f"| {epoch['epoch']} | {epoch['commit']} | {epoch['inventory_sha256']} |")
        lines += ["", "## 冻结入口", "", "| 文件 | SHA-256 |", "|---|---|"]
        for path, digest in sorted(self.source_hashes.items()):
            lines.append(f"| {path} | {digest} |")
        if self.failure:
            lines += ["", "## 实际退出原因", "", self.failure]
        return "\n".join(lines) + "\n"

    def publish(self, reason):
        # sync_rules owns a single iterative pull/commit/push transaction.
        self.sync_rules("pre-publish:" + reason)

    def execute(self, label, script, arguments):
        self.sync_rules("pre-process:" + label)
        logfile = self.out / (label + ".log")
        if logfile.exists():
            raise RuntimeError("Refusing to overwrite a prior process receipt")
        entry = self.frozen / SCRIPTS / script
        command = ["node", f"--max-old-space-size={self.heap}", "--max-semi-space-size=4",
                   "--expose-gc", str(entry), *map(str, arguments)]
        child_env = {k: v for k, v in os.environ.items() if k not in ("GH_TOKEN", "GITHUB_TOKEN")}
        start = time.monotonic()
        process = subprocess.Popen(command, cwd=self.frozen, env=child_env,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        assert process.stdout is not None
        selector = selectors.DefaultSelector()
        selector.register(process.stdout, selectors.EVENT_READ)
        try:
            with logfile.open("wb") as log:
                while selector.get_map():
                    for key, _ in selector.select(timeout=1):
                        content = os.read(key.fileobj.fileno(), 65536)
                        if not content:
                            selector.unregister(key.fileobj)
                            continue
                        log.write(content)
                        log.flush()
                        sys.stdout.buffer.write(content)
                        sys.stdout.buffer.flush()
                    if time.monotonic() - self.last_pull >= 45 * 60:
                        self.sync_rules("hourly-during-process")
                code = process.wait()
        except BaseException:
            process.terminate()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
            raise
        finally:
            selector.close()
            process.stdout.close()
        receipt = {"label": label, "exit_code": code, "wall_seconds": time.monotonic() - start,
                   "stdout_sha256": sha(logfile), "script_sha256": sha(entry)}
        self.receipts.append(receipt)
        self.save()
        return receipt

    def require_exit(self, receipt):
        if receipt["exit_code"]:
            self.status = "numeric_process_failed"
            self.failure = f"{receipt['label']}: actual OS exit {receipt['exit_code']}; no later state exists."
            self.save()
            self.publish(receipt["label"] + " actual process failure")
            raise RuntimeError(self.failure)

    @staticmethod
    def state_summary(data):
        options = data["options"]
        J, K = options["radialBasisCount"], options["modes"]
        expected = J * (4 * K + 3) + 2
        if len(data["z"]) != expected or not all(math.isfinite(x) for x in data["z"]):
            raise RuntimeError("Incomplete or nonfinite full parameter state")
        design = data.get("gapLengthDesign", {})
        amplitude_index = design.get("amplitudeIndex", expected - 1)
        cut_index = design.get("cutHeightIndex", J * (2 * K + 1))
        if amplitude_index != expected - 1 or cut_index != J * (2 * K + 1):
            raise RuntimeError("Saved amplitude/cut-height indices disagree with complete layout")
        return {"dimension": expected, "angles": options["angles"], "modes": K,
                "amplitude": data["z"][amplitude_index], "cut_height_coefficient": data["z"][cut_index],
                "actual_cuff_height": design.get("trueCuffHeight"),
                "peak_rows": len(data.get("peakMetricRows", [])),
                "peak_rows_canonical_sha256": json_sha(data.get("peakMetricRows", []))}

    @staticmethod
    def value_summary(value):
        return {"squared_norm": value["squaredNorm"], "sample_metric": value["maxRelativeMetric"],
            "sample_curvature": value["curvature"]["maxCurvature"],
            "original_grid_metric": value.get("originalQuadratureMaxRelativeMetric"),
            "added_peak_metric": value.get("additionalPeakMaximum"),
            "sample_max_y": value["geometry"].get("maxAbsoluteY"),
            "sample_held": value["geometry"].get("minHeldDistance"),
            "geometry_violations": value["geometry"].get("maximumViolations")}

    def lm_step(self, label, iteration, source, script, arguments, output_suffix,
                schema, counter, expected_count, purpose, parent_field="source.inputSHA256", retain_on_stall=False):
        prefix = self.out / f"{label}-{iteration:03d}"
        receipt = self.execute(f"{label}-{iteration:03d}", script, arguments(prefix))
        output = Path(str(prefix) + output_suffix)
        row = {**receipt, "stage": label, "iteration": iteration, "purpose": purpose,
               "accepted": False, "input_sha256": sha(source),
               "output_sha256": sha(output) if output.is_file() else None}
        retained_stall = False
        if output.is_file():
            data = json.loads(output.read_text())
            parent = json.loads(source.read_text())
            if data.get("schema") != schema:
                raise RuntimeError("Actual checkpoint has unexpected stage/objective schema")
            if parent_field and field(data, parent_field) != sha(source):
                raise RuntimeError("Actual checkpoint does not identify its exact input bytes")
            if not parent_field and data.get("parentInput") != str(source):
                raise RuntimeError("Recovered metric checkpoint names a different parent path")
            if data.get("options") != parent.get("options"):
                raise RuntimeError("An LM run changed the frozen finite parameter layout")
            if "peakMetricRows" in parent and data.get("peakMetricRows") != parent["peakMetricRows"]:
                raise RuntimeError("An LM run changed its fixed extra metric rows")
            if schema in ("6a65-R211-original-metric-checkpoint-v1", "6a65-R211-quartic-metric-checkpoint-v1"):
                expected_tau = None if schema == "6a65-R211-original-metric-checkpoint-v1" else .05
                if data.get("metricTau") != expected_tau:
                    raise RuntimeError("Recovered metric checkpoint changed its objective tau")
            accepted = data.get("accepted") is True
            if field(data, counter) != expected_count - (0 if accepted else 1):
                raise RuntimeError("Actual checkpoint did not inherit its phase accepted counter")
            if retain_on_stall and not accepted and data["z"] != parent["z"]:
                raise RuntimeError("An unaccepted retained checkpoint changed its input field")
            retained_stall = bool(retain_on_stall and not accepted and receipt["exit_code"] == 0)
            # A rejected trial's evaluation is not the geometry of the retained z.
            value = data["baseline"] if not accepted else (data.get("evaluation") or data["baseline"])
            row.update(self.state_summary(data))
            row.update(self.value_summary(value))
            row.update({"accepted": accepted, "alpha": data["history"][-1].get("alpha"),
                        "baseline_squared_norm": data["baseline"]["squaredNorm"],
                        "phase_accepted_count": field(data, counter),
                        "gap_length_accepted_count": data.get("gapLengthAcceptedSteps")})
            if accepted and not row["squared_norm"] < row["baseline_squared_norm"]:
                raise RuntimeError("Accepted flag lacks an actual decrease from this normal's baseline")
        self.rows.append(row)
        if receipt["exit_code"] or not row["accepted"]:
            self.status = "numeric_process_stopped"
            self.failure = f"{label}/{iteration}: actual exit {receipt['exit_code']}; accepted={row['accepted']}."
        if retained_stall:
            self.status = "numeric_stall_valid_current_state_retained"
            self.stall = {"stage": label, "iteration": iteration, "checkpoint_sha256": sha(output),
                          "accepted_count": row["phase_accepted_count"], "actual_exit_code": 0}
        self.save()
        self.publish(f"{label} step {iteration} exit {receipt['exit_code']} accepted {row['accepted']}")
        if retained_stall:
            return output
        if receipt["exit_code"] or not row["accepted"]:
            raise RuntimeError(self.failure)
        return output

    def transition(self, label, source, script, arguments, initial_suffix, schema, kind,
                   report_suffix=None, initial_counter=None, parent_field="source.inputSHA256"):
        prefix = self.out / label
        receipt = self.execute(label, script, arguments(prefix))
        self.require_exit(receipt)
        output = Path(str(prefix) + initial_suffix)
        data = json.loads(output.read_text())
        if data.get("schema") != schema or field(data, parent_field) != sha(source):
            raise RuntimeError("Transition did not identify the exact parent and declared new schema")
        if initial_counter and field(data, initial_counter) != 0:
            raise RuntimeError("New objective/discretization counter was not reset to zero")
        if data.get("accepted") is True:
            raise RuntimeError("A transition/value-only result was incorrectly marked as an LM acceptance")
        value = data.get("baseline") or data.get("evaluation")
        if value is None:
            raise RuntimeError("New transition must return its complete fresh baseline")
        record = {**receipt, "kind": kind, "input_sha256": sha(source), "output_sha256": sha(output),
                  "accepted_optimization_step": False, **self.state_summary(data), **self.value_summary(value)}
        if report_suffix:
            report_path = Path(str(prefix) + report_suffix)
            report = json.loads(report_path.read_text())
            if report.get("initialSHA256") is not None and report["initialSHA256"] != sha(output):
                raise RuntimeError("Transition report and initial state have different byte identities")
            record["report_sha256"] = sha(report_path)
        self.transitions.append(record)
        self.save()
        self.publish(label + " actual new baseline")
        return output

    def observe(self, label, source):
        output = self.out / (label + ".json")
        receipt = self.execute(label, OBSERVER,
            [self.frozen / CANDIDATE, source, output, self.observer_radial, self.observer_angles])
        self.require_exit(receipt)
        data = json.loads(output.read_text())
        if data.get("schema") != "6a65-gap-clock-same-field-refined-metric-observation-v1":
            raise RuntimeError("Unexpected saved gap/clock observation schema")
        if field(data, "inputs.inputSHA256") != sha(source) or field(data, "inputs.candidateSHA256") != sha(self.frozen / CANDIDATE):
            raise RuntimeError("Observer did not consume the exact current state and candidate")
        if not all(data.get(key) is True for key in ("fieldCoefficientsUnchanged", "physicalMetricUnchanged", "sourceAngularPrimitiveUnchanged")):
            raise RuntimeError("Observer changed the saved finite field")
        record = {**receipt, "input_sha256": sha(source), "output_sha256": sha(output),
            "point_count": data["pointCount"], "dimension": data["dimension"],
            "metric": data["worstMetric"]["metric"], "metric_s": data["worstMetric"]["s"], "metric_u": data["worstMetric"]["u"],
            "curvature": data["worstCurvature"]["curvature"], "minimum_immersion": data["minImmersion"],
            "continuous_certificate": False}
        self.observations.append(record)
        self.save()
        self.publish(label + " actual same-field observation")
        return output

    def substitute(self, arguments, source, observer, prefix, recipe=None):
        substitutions = {"{candidate}": self.frozen / CANDIDATE, "{source}": source,
                         "{observer}": observer, "{prefix}": prefix,
                         "{recipe}": self.frozen / recipe if recipe else None}
        values = [substitutions.get(x, x) if isinstance(x, str) else x for x in arguments]
        if any(x is None for x in values):
            raise ValueError("Requested argv placeholder has no actual input")
        return values

    def regenerate_observed_input(self):
        candidate, source = self.frozen / CANDIDATE, self.frozen / INITIAL
        for label, count, tau in (("replay-r211", 2, "original"), ("replay-quartic", 6, ".05")):
            schema = "6a65-R211-original-metric-checkpoint-v1" if tau == "original" else "6a65-R211-quartic-metric-checkpoint-v1"
            for i in range(1, count + 1):
                source = self.lm_step(label, i, source, METRIC_RUNNER,
                    lambda prefix: [candidate, source, prefix, tau, "1", "run"], "-1.json",
                    schema, "metricBranchAcceptedSteps", i, "已见输入重生", parent_field="")
        source = self.transition("replay-gap1-delta005", source, GAP_INIT,
            lambda prefix: [candidate, source, prefix, "1", ".05", ".05"], "-seed.json",
            "6a65-gap-length-value-only-seed-v1", "已见新 gap/长度/R215 基线重生",
            report_suffix="-value.json", initial_counter="gapLengthAcceptedSteps")
        for i in range(1, 4):
            source = self.lm_step("replay-gap", i, source, GAP_RUNNER,
                lambda prefix: [candidate, source, prefix], "-state.json", GAP_SCHEMA,
                "gapLengthAcceptedSteps", i, "已见输入重生")
        for i in range(1, 4):
            source = self.lm_step("replay-fixed42", i, source, PEAK_RUNNER,
                lambda prefix: [candidate, source, prefix, "run"], "-state.json", PEAK_SCHEMA,
                "peakMetricAcceptedSteps", i, "已见输入重生")
        source = self.transition("replay-angular-K11", source, ANGULAR_INIT,
            lambda prefix: [candidate, source, "11", prefix], "-initial.json",
            "6a65-fixed-peak-angular-initial-v1", "已见 K7→11 同场零注入重生",
            report_suffix="-report.json", initial_counter="peakMetricAcceptedSteps", parent_field="parent.inputSHA256")
        for i in range(1, 4):
            source = self.lm_step("replay-K11-fixed42", i, source, PEAK_RUNNER,
                lambda prefix: [candidate, source, prefix, "run"], "-state.json", PEAK_SCHEMA,
                "peakMetricAcceptedSteps", i, "已见输入重生")
        return source

    def run_plan(self, source, observed):
        for stage in self.plan:
            label = stage["label"]
            source = self.transition(label + "-initial", source, stage["init_script"],
                lambda prefix: self.substitute(stage["init_arguments"], source, observed, prefix, stage.get("recipe")),
                stage["initial_suffix"], stage["initial_schema"], stage["transition_kind"],
                report_suffix=stage.get("report_suffix"), initial_counter=stage["accepted_counter"],
                parent_field=stage.get("initial_parent_hash_field", "source.inputSHA256"))
            for i in range(1, stage["steps"] + 1):
                purpose = "已见阶段重生" if i <= stage.get("prior_observed_steps", 0) else "本阶段新接受尝试"
                source = self.lm_step(label, i, source, stage["run_script"],
                    lambda prefix: self.substitute(stage["run_arguments"], source, observed, prefix, stage.get("recipe")),
                    stage["checkpoint_suffix"], stage["checkpoint_schema"], stage["accepted_counter"], i, purpose,
                    parent_field=stage.get("checkpoint_parent_hash_field", "source.inputSHA256"), retain_on_stall=True)
                if self.stall is not None:
                    observed = self.observe(label + "-stalled-current-field", source)
                    return source, observed
            observed = self.observe(label + "-current-field", source)
        return source, observed

    def require_public_commit(self, commit):
        if not re.fullmatch(r"[0-9a-f]{40}", str(commit)):
            raise ValueError("Followup source/rules commit must be a full Git SHA")
        if self.git("cat-file", "-e", commit + "^{commit}", check=False, emit=False).returncode:
            self.git("fetch", "--filter=blob:none", "origin", commit)
        while self.git("merge-base", "--is-ancestor", commit, "origin/main", check=False, emit=False).returncode:
            shallow = self.git("rev-parse", "--is-shallow-repository", emit=False).stdout.strip()
            if shallow != "true":
                raise ValueError("Followup commit is not a public main ancestor")
            self.git("fetch", "--filter=blob:none", "--deepen=512", "origin", "main")

    def read_followup(self, source, observed):
        path = self.repo / self.followup_path
        if not path.is_file():
            return None
        published = self.git("rev-parse", f"origin/main:{self.followup_path}", check=False, emit=False)
        if published.returncode:
            return None
        actual_blob = self.git("hash-object", "--", str(self.followup_path), emit=False).stdout.strip()
        if actual_blob != published.stdout.strip():
            raise ValueError("The followup bytes are not the actual published main blob")
        if path.is_symlink() or path.stat().st_size >= 100_000:
            raise ValueError("A followup packet must be a regular file smaller than 100KB")
        packet = json.loads(path.read_text())
        # A stable path may still contain the preceding run's consumed packet.
        # It is not authorized to operate on this run's current raw state.
        if str(packet.get("run_id")) != self.run_id or str(packet.get("attempt")) != self.attempt:
            return None
        identity = packet.get("followup_id", "")
        if identity in self.used_followups:
            return None
        if packet.get("schema") != FOLLOWUP_SCHEMA or not re.fullmatch(r"[A-Za-z0-9_-]{1,80}", identity):
            raise ValueError("Unexpected same-job followup schema/identity")
        if packet.get("parent_state_sha256") != sha(source) or packet.get("parent_observer_sha256") != sha(observed):
            raise ValueError("Followup does not exactly match this current state and observer")
        if packet.get("action") not in ("continue", "release_runner"):
            raise ValueError("Followup action must be continue or explicit release_runner")
        self.require_public_commit(packet.get("rules_read_commit"))
        difference = self.git("diff", packet["rules_read_commit"], "origin/main", "--", *RULES, emit=False).stdout
        if difference.strip():
            raise ValueError("Followup's root-read rules commit does not contain the current README text")
        if packet["action"] == "continue":
            shaped = {**self.request, "request_id": identity, "rules_read_commit": packet["rules_read_commit"],
                      "continuations": packet.get("continuations")}
            plan = parse_plan(shaped)
            if any(s["label"] in self.used_stage_labels for s in plan):
                raise ValueError("Followup stage labels must be new; old paths cannot be overwritten")
            self.require_public_commit(packet.get("source_commit"))
            packet["validated_plan"] = plan
        elif not isinstance(packet.get("reason"), str) or not packet["reason"].strip():
            raise ValueError("Explicit runner release must give the root session's reason")
        packet["packet_sha256"] = sha(path)
        return packet

    def await_followup(self, source, observed):
        self.status = "awaiting_matched_same_job_followup"
        self.awaiting = {"state_sha256": sha(source), "observer_sha256": sha(observed), "since_utc": utc()}
        self.save()
        self.publish("actual final observation retained for same-job successor")
        last_rejection = None
        last_packet_blob = None
        while True:
            self.git("fetch", "--filter=blob:none", "origin", "main")
            found = self.git("rev-parse", f"origin/main:{self.followup_path}", check=False, emit=False)
            current_blob = found.stdout.strip() if not found.returncode else None
            should_read = current_blob is not None and current_blob != last_packet_blob
            if should_read or time.monotonic() - self.last_pull >= 45 * 60:
                self.sync_rules("new-followup-packet" if should_read else "hourly-during-followup-wait")
                refreshed = self.git("rev-parse", f"origin/main:{self.followup_path}", check=False, emit=False)
                refreshed_blob = refreshed.stdout.strip() if not refreshed.returncode else None
                should_read = refreshed_blob is not None and refreshed_blob != last_packet_blob
                last_packet_blob = refreshed_blob
            packet = None
            try:
                if should_read:
                    packet = self.read_followup(source, observed)
                    last_rejection = None
            except (ValueError, RuntimeError) as error:
                message = str(error)
                if message != last_rejection:
                    print(json.dumps({"event": "same_job_followup_rejected", "utc": utc(), "reason": message,
                                      "run_id": self.run_id, "state_sha256": sha(source)}), flush=True)
                last_rejection = message
            if packet is not None:
                self.used_followups.add(packet["followup_id"])
                receipt = {k: packet[k] for k in ("followup_id", "action", "packet_sha256", "parent_state_sha256", "parent_observer_sha256", "rules_read_commit")}
                receipt.update({"received_utc": utc(), "source_commit": packet.get("source_commit"),
                                "reason": packet.get("reason")})
                self.followup_packets.append(receipt)
                self.rules_read = packet["rules_read_commit"]
                if packet["action"] == "release_runner":
                    self.status = "released_by_explicit_matched_followup_not_completion"
                    self.awaiting = None
                    self.save()
                    self.publish("explicit matched runner release")
                    print(json.dumps({"event": "actual_runner_release", "utc": utc(),
                        "followup_id": packet["followup_id"], "checkpoint_sha256": sha(source),
                        "observer_sha256": sha(observed), "strong_target_complete": False}), flush=True)
                    return False
                self.plan = packet["validated_plan"]
                self.used_stage_labels.update(s["label"] for s in self.plan)
                self.freeze_sources(packet["source_commit"])
                self.status, self.awaiting = "running_same_job_followup", None
                self.stall, self.failure = None, None
                self.save()
                self.publish("matched successor sources frozen")
                return True
            self.save()
            print(json.dumps({"event": "actual_same_job_wait_heartbeat", "utc": utc(), "run_id": self.run_id,
                "attempt": self.attempt, "checkpoint_sha256": sha(source), "observer_sha256": sha(observed),
                "latest_checked_rules_commit": self.checked_rules, "next_poll_seconds": self.poll_seconds,
                "strong_target_complete": False}), flush=True)
            # This is an active root-session handoff, not a user confirmation.
            # No deadline silently discards the still-needed raw state.
            time.sleep(self.poll_seconds)

    def run(self):
        source = self.regenerate_observed_input()
        observed = self.observe("replay-K11-current-field", source)
        while True:
            source, observed = self.run_plan(source, observed)
            if not self.await_followup(source, observed):
                return


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    controller = None
    try:
        controller = Controller(args)
        controller.run()
    except BaseException as error:
        if controller is not None:
            already_terminal = controller.status in (
                "numeric_process_failed", "numeric_process_stopped", "unreviewed_readme_change")
            if not already_terminal:
                controller.status = "controller_failed"
            controller.failure = str(error)
            controller.save()
            if not already_terminal and not controller.publication_failed:
                try:
                    controller.publish("actual controller failure")
                except BaseException as publication_error:
                    print(f"TERMINAL_REPORT_NOT_PUBLISHED: {type(publication_error).__name__}: {publication_error}",
                          file=sys.stderr, flush=True)
        print(f"ACTUAL_CONTROLLER_EXIT: {type(error).__name__}: {error}", file=sys.stderr, flush=True)
        raise


if __name__ == "__main__":
    main()
