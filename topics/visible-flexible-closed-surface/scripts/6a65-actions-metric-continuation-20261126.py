#!/usr/bin/env python3
"""Run R211 seed regeneration, then one real quartic-metric step per process.

Only scalar observations and SHA-256 identifiers are committed. Arrays remain
in runner/temp. Numerical source is frozen before later pulls update main.
"""
from __future__ import annotations
import argparse
import base64
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import re
import selectors
import shutil
import subprocess
import sys
import time

TOPIC = Path("topics/visible-flexible-closed-surface")
RULES = ["README.md", str(TOPIC / "README.md")]
CANDIDATE = TOPIC / "notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json"
INITIAL = TOPIC / "notes/2026-11-13-fd2d-R211-full-half-01-initial.json"
RUNNER = TOPIC / "scripts/6a65-run-metric-branch-recovered-20261126.cjs"
REQUEST_SCHEMA = "6a65-quartic-metric-actions-request-v1"


def utc():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def number(value):
    if value is None:
        return "—"
    return format(value, ".15g") if isinstance(value, (int, float)) else str(value)


def concurrent_push_rejection(message):
    # GitHub may lose the main compare-and-swap after advertising its ref.
    # Match that concrete race, not unrelated remote permission/hook failures.
    return bool(re.search(
        r"non-fast-forward|fetch first|\[rejected\]|"
        r"cannot lock ref ['\"]refs/heads/main['\"]:\s*is at [0-9a-f]+\s+but expected [0-9a-f]+|"
        r"incorrect old value provided",
        message, re.IGNORECASE))


class RulesChanged(RuntimeError):
    """The controller cannot claim understanding of a new README."""


class Controller:
    def __init__(self, args):
        self.repo = Path(__file__).resolve().parents[3]
        self.out = args.out_dir.resolve()
        self.out.mkdir(parents=True, exist_ok=False)
        self.frozen = self.out / "source"
        request_path = (self.repo / args.request).resolve()
        if not request_path.is_relative_to(self.repo / TOPIC / "ci-requests"):
            raise ValueError("Request must be in this topic's ci-requests")
        self.request = json.loads(request_path.read_text())
        self.request_sha = sha(request_path)
        shutil.copyfile(request_path, self.out / "request.json")
        r = self.request
        if r.get("schema") != REQUEST_SCHEMA:
            raise ValueError("Unknown request schema")
        if not re.fullmatch(r"[A-Za-z0-9_-]{1,80}", str(r.get("request_id", ""))):
            raise ValueError("Plain request_id required")
        self.steps, self.tau = r.get("steps", 60), r.get("tau", 0.05)
        self.heap, self.prior_steps = r.get("heap_mb", 512), r.get("prior_observed_quartic_steps", 6)
        if not isinstance(self.steps, int) or not 1 <= self.steps <= 1000:
            raise ValueError("steps must be an integer from 1 through 1000")
        if not isinstance(self.tau, (int, float)) or not math.isfinite(self.tau) or self.tau <= 0:
            raise ValueError("Positive finite tau required")
        if not isinstance(self.heap, int) or not 64 <= self.heap <= 8192:
            raise ValueError("heap_mb must be an integer from 64 through 8192")
        if not isinstance(self.prior_steps, int) or not 0 <= self.prior_steps <= self.steps:
            raise ValueError("Invalid prior observed quartic-step count")
        self.rules_read = r.get("rules_read_commit", "")
        if not re.fullmatch(r"[0-9a-f]{40}", self.rules_read):
            raise ValueError("rules_read_commit must name the root session's actually read commit")
        self.checked_rules, self.last_pull = self.rules_read, 0.0
        self.run_id = os.environ.get("GITHUB_RUN_ID", "")
        self.attempt = os.environ.get("GITHUB_RUN_ATTEMPT", "1")
        self.repository = os.environ.get("GITHUB_REPOSITORY", "")
        if self.repository != "Rogerhu12/math-research-public":
            raise ValueError("Only Rogerhu12/math-research-public is supported")
        if not self.run_id.isdigit() or not self.attempt.isdigit():
            raise ValueError("A real Actions run ID and attempt are required")
        self.report = TOPIC / f"notes/2026-11-26-6a65-actions-metric-{self.run_id}-{self.attempt}.md"
        self.token = os.environ.get("GH_TOKEN", "")
        if not self.token:
            raise ValueError("GH_TOKEN environment credential is required; no credential file is used")
        self.auth = self.git_environment()
        # Rebase creates commits too: identity must cover pull/rebase as well
        # as the explicit report commit. These local settings contain no secret.
        self.git("config", "--local", "user.name", "github-actions[bot]")
        self.git("config", "--local", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
        self.source_commit = self.git("rev-parse", "HEAD", emit=False).stdout.strip()
        self.rows, self.pulls = [], []
        self.status, self.failure, self.started = "running", None, utc()
        self.source_hashes, self.source_digest = {}, None
        self.manifest_path = self.out / "scalar-run-manifest.json"
        self.git("switch", "-c", f"visible-flex-6a65-{self.run_id}-{self.attempt}")
        self.freeze_sources()
        if self.git("cat-file", "-e", self.rules_read + "^{commit}", check=False, emit=False).returncode:
            self.git("fetch", "--filter=blob:none", "--depth=1", "origin", self.rules_read)
        self.sync_rules("startup")
        self.save()

    def git_environment(self):
        env = os.environ.copy()
        env["GIT_TERMINAL_PROMPT"] = "0"
        encoded = base64.b64encode(("x-access-token:" + self.token).encode()).decode()
        count = int(env.get("GIT_CONFIG_COUNT", "0"))
        env["GIT_CONFIG_COUNT"] = str(count + 2)
        env[f"GIT_CONFIG_KEY_{count}"] = "http.https://github.com/.extraheader"
        env[f"GIT_CONFIG_VALUE_{count}"] = "AUTHORIZATION: basic " + encoded
        env[f"GIT_CONFIG_KEY_{count + 1}"] = "credential.helper"
        env[f"GIT_CONFIG_VALUE_{count + 1}"] = ""
        return env

    def git(self, *arguments, check=True, emit=True):
        result = subprocess.run(["git", *arguments], cwd=self.repo, env=self.auth,
                                text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if emit and result.stdout:
            print(result.stdout, end="", flush=True)
        if emit and result.stderr:
            print(result.stderr, end="", file=sys.stderr, flush=True)
        if check and result.returncode:
            raise RuntimeError(f"git {arguments[0]} exited {result.returncode}")
        return result

    def freeze_sources(self):
        tracked = self.git("ls-files", "-z", str(TOPIC / "scripts"), emit=False).stdout.split("\0")
        paths = [Path(p) for p in tracked if p] + [CANDIDATE, INITIAL]
        inventory = []
        for rel in sorted(set(paths)):
            src = self.repo / rel
            if src.is_symlink() or not src.is_file():
                raise ValueError(f"Expected ordinary source file: {rel}")
            dest = self.frozen / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dest)
            inventory.append({"path": rel.as_posix(), "sha256": sha(dest)})
        encoded = json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()
        self.source_digest = hashlib.sha256(encoded).hexdigest()
        (self.out / "frozen-source-inventory.json").write_bytes(encoded + b"\n")
        for rel in [CANDIDATE, INITIAL, RUNNER,
                    TOPIC / "scripts/6a65-quartic-metric-recovered-20261126.cjs",
                    TOPIC / "scripts/6a65-low-memory-r211-provider-recovered-20261126.cjs"]:
            self.source_hashes[str(rel)] = sha(self.frozen / rel)
        self.source_hashes[str(Path(__file__).resolve().relative_to(self.repo))] = sha(Path(__file__))
        self.node_version = subprocess.check_output(["node", "--version"], text=True).strip()

    def sync_rules(self, reason):
        print("RUN git pull --rebase origin main", flush=True)
        self.git("pull", "--rebase", "origin", "main")
        remote = self.git("rev-parse", "origin/main", emit=False).stdout.strip()
        diff = self.git("diff", self.checked_rules, remote, "--", *RULES).stdout
        self.pulls.append({"utc": utc(), "reason": reason, "from": self.checked_rules,
                           "to": remote, "readme_diff_empty": not bool(diff.strip())})
        self.last_pull = time.monotonic()
        if diff.strip():
            (self.out / "UNREVIEWED_README_DIFF.patch").write_text(diff)
            self.status = "unreviewed_readme_change"
            self.failure = "README changed; the root session must read the printed diff and update the request."
            self.save()
            print("UNREVIEWED_README_DIFF: no automatic-compliance claim; this numeric job stops.", flush=True)
            raise RulesChanged(self.failure)
        self.checked_rules = remote

    def save(self):
        payload = {
            "schema": "6a65-actions-metric-scalar-manifest-v1",
            "request": self.request, "request_sha256": self.request_sha,
            "run_id": self.run_id, "attempt": self.attempt,
            "source_commit": self.source_commit, "source_inventory_sha256": self.source_digest,
            "source_hashes": self.source_hashes, "node_version": getattr(self, "node_version", None),
            "started_utc": self.started, "updated_utc": utc(), "status": self.status,
            "failure": self.failure, "root_read_rules_commit": self.rules_read,
            "last_unchanged_rules_check": self.checked_rules, "pulls": self.pulls, "steps": self.rows,
            "continuous_certificate": False, "strong_target_complete": False, "raw_outputs_published": False,
        }
        self.manifest_path.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n")

    def report_text(self):
        run_url = f"https://github.com/{self.repository}/actions/runs/{self.run_id}"
        lines = [
            f"# R211 后的四次 metric 实算：Actions run {self.run_id}, attempt {self.attempt}",
            "",
            "**可信度：启发式/数值证据。** 表中仅为完整有限目标上的真实试步与采样量，"
            "不是全域误差、连续精确解、非局部 reach 或课题完成证书。",
            "",
            f"- 请求 {self.request['request_id']}；[真实 run]({run_url})；状态 {self.status}。",
            f"- 冻结源码提交 {self.source_commit}；Node {self.node_version}；每个 Node 进程 old-space {self.heap} MB。",
            f"- 先重生 R211 原目标两次接受，再运行四次 metric 最多 {self.steps} 次接受。"
            f"前 {self.prior_steps} 个四次步仅恢复先前已见输入，之后才是本分支新续算。",
            f"- 新 metric 残差为 $R=\\sqrt{{1+q/\\tau^2}}(e,\\sqrt2 f)$，"
            f"$q=e^2+2f^2$，$\\tau={self.tau}$；保留 R211 四次曲率及原几何罚项，每步重新计算自己的完整 normal/baseline。",
            "- 全部 1025 列保留。rho 设计参数仍可改变参考度量；这不是最终固定 $g$ 的加密。",
            f"- 根会话实际读规则于 {self.rules_read}；本次最后真实 pull 后双 README 无变化比较到 {self.checked_rules}。"
            "若出现差异，本任务打印差异并标明未审，不自称理解或遵守了新条款。",
            f"- 源码清单 SHA-256 {self.source_digest}。数组、完整 normal、检查点及 stdout 只在 runner 临时目录，不上传 artifact/Release。",
            f"- 起始 {self.started}；更新 {utc()}。退出码来自 Python 等待真实 OS 进程，未从 solver JSON 猜造。",
            "",
            "## 每个实际进程",
            "",
            "| 阶段/步 | 用途 | 接受 | α | R² baseline → end | sample metric | sample κ | max abs(y) | held 采样见证 | exit | 秒 |",
            "|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|",
        ]
        for row in self.rows:
            values = [f"{row['stage']}/{row['iteration']}", row["purpose"],
                      "是" if row["accepted"] else "否", number(row.get("alpha")),
                      number(row.get("baseline_squared_norm")) + " → " + number(row.get("squared_norm")),
                      number(row.get("sample_max_metric")), number(row.get("sample_max_curvature")),
                      number(row.get("sample_max_absolute_y")), number(row.get("sample_min_held_distance")),
                      str(row["exit_code"]), number(row["wall_seconds"])]
            lines.append("| " + " | ".join(values) + " |")
        lines.extend(["", "held 栏是原有限几何 guide 的见证量，不能直接冒充整个闭曲面的 Hausdorff 比例。"
                      "仍须支付全域/全时余项、帽及非局部法球。", "",
                      "## 临时输出的身份", "",
                      "| 阶段/步 | checkpoint SHA-256 | stdout SHA-256 | A | cut-height coefficient |",
                      "|---|---|---|---:|---:|"])
        for row in self.rows:
            lines.append("| " + " | ".join([
                f"{row['stage']}/{row['iteration']}", str(row.get("checkpoint_sha256") or "none"),
                row["stdout_sha256"], number(row.get("amplitude")),
                number(row.get("cut_height_coefficient"))]) + " |")
        lines.extend(["", "## 再生入口与输入", "",
                      "scripts/6a65-actions-metric-continuation-20261126.py 消费本次请求并调用 "
                      "scripts/6a65-run-metric-branch-recovered-20261126.cjs。"
                      "R211 seed 和四次阶段均每进程一个完整 LM 步。"
                      "同目标累计步数由 checkpoint schema/metricTau 验证继承，拒绝时不增加。", "",
                      "| 文件 | SHA-256 |", "|---|---|"])
        for rel, digest in sorted(self.source_hashes.items()):
            lines.append(f"| {rel} | {digest} |")
        if self.failure:
            lines.extend(["", "## 当前退出原因", "", self.failure])
        return "\n".join(lines) + "\n"

    def publish(self, reason):
        self.sync_rules("pre-publish:" + reason)
        self.save()
        dest = self.repo / self.report
        dest.parent.mkdir(parents=True, exist_ok=True)
        text = self.report_text()
        if len(text.encode()) >= 100_000:
            raise RuntimeError("Report would exceed the Markdown limit")
        dest.write_text(text)
        self.git("add", "--", str(self.report))
        self.git("-c", "user.name=github-actions[bot]",
                 "-c", "user.email=41898282+github-actions[bot]@users.noreply.github.com",
                 "commit", "-m", f"visible-flex: {self.request['request_id']} {reason}", "--", str(self.report))
        while True:
            pushed = self.git("push", "origin", "HEAD:main", check=False)
            if pushed.returncode == 0:
                return
            if not concurrent_push_rejection(pushed.stdout + pushed.stderr):
                raise RuntimeError("Push failed for a reason other than non-fast-forward; see actual Git output")
            self.sync_rules("non-fast-forward")
            self.save()
            # This local commit was rejected and has never been published.
            # Refresh its rules-check receipt after the required rebase.
            dest.write_text(self.report_text())
            self.git("add", "--", str(self.report))
            self.git("-c", "user.name=github-actions[bot]",
                     "-c", "user.email=41898282+github-actions[bot]@users.noreply.github.com",
                     "commit", "--amend", "--no-edit", "--", str(self.report))

    def process_step(self, stage, iteration, source, tau_text):
        self.sync_rules(f"pre-solve:{stage}-{iteration}")
        prefix = self.out / f"{stage}-{iteration:04d}"
        logfile = prefix.with_suffix(".log")
        target = Path(str(prefix) + "-1.json")
        command = ["node", f"--max-old-space-size={self.heap}", "--max-semi-space-size=4",
                   "--expose-gc", str(self.frozen / RUNNER), str(self.frozen / CANDIDATE),
                   str(source), str(prefix), tau_text, "1", "run"]
        child_env = {k: v for k, v in os.environ.items() if k not in ("GH_TOKEN", "GITHUB_TOKEN")}
        started = time.monotonic()
        process = subprocess.Popen(command, cwd=self.frozen, env=child_env,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        assert process.stdout is not None
        selector = selectors.DefaultSelector()
        selector.register(process.stdout, selectors.EVENT_READ)
        try:
            with logfile.open("wb") as log:
                while selector.get_map():
                    for key, _ in selector.select(timeout=1):
                        data = os.read(key.fileobj.fileno(), 65536)
                        if not data:
                            selector.unregister(key.fileobj)
                            continue
                        log.write(data)
                        log.flush()
                        sys.stdout.buffer.write(data)
                        sys.stdout.buffer.flush()
                    if time.monotonic() - self.last_pull >= 45 * 60:
                        self.sync_rules("hourly-during-solver")
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
        row = {"stage": stage, "iteration": iteration, "exit_code": code,
               "wall_seconds": time.monotonic() - started,
               "stdout_sha256": sha(logfile), "accepted": False,
               "checkpoint_sha256": sha(target) if target.is_file() else None,
               "purpose": "旧 seed 再生" if stage == "r211" else
                          "旧输入再生" if iteration <= self.prior_steps else "新续算"}
        if target.is_file():
            data = json.loads(target.read_text())
            expected = "6a65-R211-original-metric-checkpoint-v1" if stage == "r211" else "6a65-R211-quartic-metric-checkpoint-v1"
            expected_tau = None if stage == "r211" else self.tau
            if data.get("schema") != expected or data.get("metricTau") != expected_tau:
                raise RuntimeError("Checkpoint objective identity mismatch")
            accepted = data.get("accepted") is True
            if data.get("metricBranchAcceptedSteps") != (iteration if accepted else iteration - 1):
                raise RuntimeError("Checkpoint accepted-count inheritance mismatch")
            value = data.get("evaluation") or data["baseline"]
            row.update({
                "accepted": accepted, "alpha": data["history"][-1].get("alpha"),
                "baseline_squared_norm": data["baseline"]["squaredNorm"],
                "squared_norm": value["squaredNorm"],
                "sample_max_metric": value["maxRelativeMetric"],
                "sample_max_curvature": value["curvature"]["maxCurvature"],
                "sample_max_absolute_y": value["geometry"]["maxAbsoluteY"],
                "sample_min_held_distance": value["geometry"]["minHeldDistance"],
                "geometry_violations": value["geometry"]["maximumViolations"],
                "amplitude": data["z"][1024], "cut_height_coefficient": data["z"][495],
                "branch_accepted_steps": data["metricBranchAcceptedSteps"],
            })
            if accepted and not row["squared_norm"] < row["baseline_squared_norm"]:
                raise RuntimeError("Accepted checkpoint has no actual objective decrease")
        self.rows.append(row)
        if code or not row["accepted"]:
            self.status = "solver_stopped"
            self.failure = f"{stage}/{iteration}: actual exit {code}; accepted={row['accepted']}. No later state was invented."
        elif stage == "quartic" and iteration == self.steps:
            self.status = "requested_numerical_steps_returned"
        self.save()
        self.publish(f"{stage} step {iteration} exit {code} accepted {row['accepted']}")
        if code or not row["accepted"]:
            raise RuntimeError(self.failure)
        return target

    def run(self):
        source = self.frozen / INITIAL
        for iteration in (1, 2):
            source = self.process_step("r211", iteration, source, "original")
        for iteration in range(1, self.steps + 1):
            source = self.process_step("quartic", iteration, source, str(self.tau))
        print(json.dumps({"event": "requested_numerical_steps_returned", "run_id": self.run_id,
                          "quartic_accepted": self.steps, "final_checkpoint_sha256": sha(source),
                          "report": str(self.report), "continuous_certificate": False}), flush=True)


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
            if controller.status == "running":
                controller.status = "controller_stopped"
            controller.failure = str(error)
            controller.save()
        print(f"ACTUAL_CONTROLLER_EXIT: {type(error).__name__}: {error}", file=sys.stderr, flush=True)
        raise


if __name__ == "__main__":
    main()

