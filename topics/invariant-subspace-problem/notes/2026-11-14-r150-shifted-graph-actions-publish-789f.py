"""Publish bounded graph-run receipts and record every successful rule check."""
import base64
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess

secret = os.environ.pop("ISP_ACTIONS_TOKEN")
env = os.environ.copy()
env.update(GIT_TERMINAL_PROMPT="0", GIT_CONFIG_COUNT="2",
           GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
           GIT_CONFIG_KEY_1="credential.helper", GIT_CONFIG_VALUE_1="")
env["GIT_CONFIG_VALUE_0"] = "Authorization: Basic " + base64.b64encode(
    ("x-access-token:" + secret).encode()).decode()
run = str(int(os.environ["GITHUB_RUN_ID"]))
attempt = str(int(os.environ["GITHUB_RUN_ATTEMPT"]))
source = Path(os.environ["ISP_GRAPH_OUT"])
provenance = json.loads((source / "source.json").read_text())
destination = Path("topics/invariant-subspace-problem/notes/r150-shifted-graph-actions-789f") / (run + "-" + attempt)
destination.mkdir(parents=True, exist_ok=True)
for file in source.rglob("*"):
    if file.is_file():
        if file.stat().st_size > 5_000_000:
            raise RuntimeError("Oversized output was not normalized: " + file.name)
        target = destination / file.relative_to(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(file, target)


def git(*args):
    result = subprocess.run(["git", *args], env=env, text=True, capture_output=True)
    for output in (result.stdout, result.stderr):
        if output.strip():
            print(output.replace(secret, "[REDACTED]").rstrip(), flush=True)
    return result


for key, value in (("user.name", "github-actions[bot]"),
                   ("user.email", "41898282+github-actions[bot]@users.noreply.github.com")):
    if git("config", key, value).returncode:
        raise SystemExit(1)

checks = []
committed = False
handoff = Path("topics/invariant-subspace-problem/HANDOFF.md")
label = "- **最近 CI pull 与规则核对：**"
while True:
    if git("pull", "--rebase", "origin", "main").returncode:
        raise SystemExit("Rebase needs the active research session; complete run outputs remain in the artifact.")
    tip = subprocess.check_output(["git", "rev-parse", "origin/main"], text=True).strip()
    current = {path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
               for path in provenance["rules"]}
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    checks.append({"commit": tip, "utc": stamp,
                   "unchanged_rules": current == provenance["rules"]})
    if current != provenance["rules"]:
        (source / "rule-drift.json").write_text(json.dumps(checks, indent=2) + "\n")
        diff = subprocess.check_output(
            ["git", "diff", provenance["source_commit"], tip, "--", *provenance["rules"]], text=True)
        (source / "rule-drift.diff").write_text(diff)
        print(diff, flush=True)
        raise SystemExit("README changed: the active research session must read and apply this difference before publishing.")
    (destination / "git-sync-checks.json").write_text(json.dumps(checks, indent=2) + "\n")
    content = handoff.read_text()
    line = f"{label} `{tip}`（{stamp}，实际 pull/rebase 成功，两 README 与任务源哈希一致）；R150 来源图运行 {run}-{attempt}，真实结果见本次回执。"
    old = next((s for s in content.splitlines() if s.startswith(label)), None)
    if old is None:
        content += "\n## 计算同步\n\n" + line + "\n"
    else:
        content = content.replace(old, line)
    if len(content.encode()) > 10_000:
        raise SystemExit("HANDOFF size needs the active research session; no oversized file will be published.")
    handoff.write_text(content)
    if git("add", "--", str(destination), str(handoff)).returncode:
        raise SystemExit(1)
    if committed:
        result = git("commit", "--amend", "--no-edit")
    else:
        result = git("commit", "-m", f"isp: preserve actual R150 shifted source graph run {run}-{attempt}")
    if result.returncode:
        raise SystemExit(1)
    committed = True
    result = git("push", "origin", "HEAD:main")
    if result.returncode == 0:
        break
    if not any(marker in result.stderr for marker in (
            "non-fast-forward", "fetch first", "[rejected]", "cannot lock ref")):
        raise SystemExit("Push failed outside concurrent-update retry; complete outputs remain in the artifact.")
