"""Save this topic's bounded CI outputs; credentials stay in process environment."""
import base64
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
from datetime import datetime, timezone

secret = os.environ.pop("ISP_ACTIONS_TOKEN")
env = os.environ.copy()
env.update(GIT_TERMINAL_PROMPT="0", GIT_CONFIG_COUNT="2",
           GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
           GIT_CONFIG_KEY_1="credential.helper", GIT_CONFIG_VALUE_1="")
env["GIT_CONFIG_VALUE_0"] = "Authorization: Basic " + base64.b64encode(
    ("x-access-token:" + secret).encode()).decode()
characteristic = int(os.environ["ISP_CHARACTERISTIC"])
run = str(int(os.environ["GITHUB_RUN_ID"]))
attempt = str(int(os.environ["GITHUB_RUN_ATTEMPT"]))
source = Path(os.environ["RUNNER_TEMP"]) / f"isp-r150-module-{characteristic}"
provenance = json.loads((source / "source.json").read_text())
destination = Path("topics/invariant-subspace-problem/notes/r150-module-actions-789f") / (
    run + "-" + attempt) / f"char{characteristic}"
destination.mkdir(parents=True, exist_ok=True)
for file in source.iterdir():
    if file.is_file():
        if file.stat().st_size > 5_000_000:
            raise RuntimeError("Oversized artifact was not normalized: " + file.name)
        shutil.copyfile(file, destination / file.name)

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
while True:
    if git("pull", "--rebase", "origin", "main").returncode:
        raise SystemExit("Rebase requires continuation; artifact remains available.")
    tip = subprocess.check_output(["git", "rev-parse", "origin/main"], text=True).strip()
    current = {path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
               for path in provenance["rules"]}
    checks.append({"commit": tip, "utc": datetime.now(timezone.utc).isoformat(),
                   "unchanged_rules": current == provenance["rules"]})
    if current != provenance["rules"]:
        (source / "rule-drift.json").write_text(json.dumps(checks, indent=2) + "\n")
        raise SystemExit("README changed: preserve artifacts for the active research session to apply the new rules.")
    (destination / "git-sync-checks.json").write_text(json.dumps(checks, indent=2) + "\n")
    if git("add", "--", str(destination)).returncode:
        raise SystemExit(1)
    if committed:
        result = git("commit", "--amend", "--no-edit")
    else:
        result = git("commit", "-m", f"isp: preserve R150 finite parameter module run {run}-{attempt} characteristic {characteristic}")
    if result.returncode:
        raise SystemExit(1)
    committed = True
    result = git("push", "origin", "HEAD:main")
    if result.returncode == 0:
        break
    if not any(marker in result.stderr for marker in (
            "non-fast-forward", "fetch first", "[rejected]", "cannot lock ref")):
        raise SystemExit("Push failed for a reason other than a concurrent update; artifacts remain available.")
