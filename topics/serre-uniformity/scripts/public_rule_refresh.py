#!/usr/bin/env python3
"""Read-only public partial clone, actual pull, and bounded rule receipt."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import subprocess

REPOSITORY = "Rogerhu12/math-research-public"
RULES = ("README.md", "topics/serre-uniformity/README.md")


def utc() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def git(args: list[str], cwd: Path | None = None) -> str:
    result = subprocess.run(["git", *args], cwd=cwd, check=True,
                            text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    if result.stderr.strip():
        print(result.stderr.rstrip(), flush=True)
    return result.stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", type=Path, required=True)
    args = parser.parse_args()
    request = json.loads(args.request.read_text(encoding="utf-8"))
    if os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
        raise RuntimeError("This task is restricted to its own public repository")
    if request["repository"] != REPOSITORY:
        raise RuntimeError("Request repository mismatch")
    expected = request["expected_rule_blobs"]
    if set(expected) != set(RULES):
        raise RuntimeError("The request must identify both complete rule files")
    baseline = request["read_baseline_commit"]
    if len(baseline) != 40 or any(c not in "0123456789abcdef" for c in baseline):
        raise RuntimeError("Invalid already-read baseline commit")
    run_id = os.environ["GITHUB_RUN_ID"]
    attempt = os.environ.get("GITHUB_RUN_ATTEMPT", "1")
    temporary = Path(os.environ["RUNNER_TEMP"])
    checkout = temporary / ("serre-rule-refresh-" + run_id + "-" + attempt)
    if checkout.exists():
        raise RuntimeError("Refusing to overwrite an existing refresh checkout")

    git(["-c", "protocol.version=2", "clone", "--quiet",
         "--filter=blob:none", "--no-checkout", "--depth=1",
         "--branch", "main",
         "https://github.com/" + REPOSITORY + ".git", str(checkout)])
    git(["sparse-checkout", "set", "--no-cone",
         "/README.md", "/topics/serre-uniformity/README.md"], checkout)
    git(["checkout", "main"], checkout)
    initial_head = git(["rev-parse", "HEAD"], checkout)
    pull_started = utc()
    pull_stdout = git(["pull", "--rebase", "origin", "main"], checkout)
    pull_completed = utc()
    head = git(["rev-parse", "HEAD"], checkout)
    observed = {path: git(["hash-object", path], checkout) for path in RULES}
    changed = [path for path in RULES if observed[path] != expected[path]]
    difference = ""
    if changed:
        git(["fetch", "--quiet", "--filter=blob:none", "--depth=1",
             "origin", baseline], checkout)
        difference = git(["diff", "--no-ext-diff", baseline, head,
                          "--", *RULES], checkout)
        print("PUBLIC_RULE_DIFF_BEGIN", flush=True)
        print(difference, flush=True)
        print("PUBLIC_RULE_DIFF_END", flush=True)

    receipt = {
        "schema": 1,
        "repository": REPOSITORY,
        "request_nonce": request["nonce"],
        "workflow_source": os.environ["GITHUB_SHA"],
        "run_id": run_id,
        "run_attempt": attempt,
        "read_baseline_commit": baseline,
        "clone_filter": "blob:none",
        "clone_depth": 1,
        "sparse_paths": list(RULES),
        "initial_head": initial_head,
        "actual_pull_command": ["git", "pull", "--rebase", "origin", "main"],
        "pull_started_utc": pull_started,
        "pull_completed_utc": pull_completed,
        "pulled_head": head,
        "pull_stdout": pull_stdout,
        "expected_rule_blobs": expected,
        "observed_rule_blobs": observed,
        "changed_rule_paths": changed,
        "rule_diff": difference,
        "read_only": True,
        "mathematical_computation_performed": False,
    }
    output = temporary / "serre-public-rule-refresh-receipt.json"
    output.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8")
    print("PUBLIC_RULE_REFRESH_RECEIPT=" +
          json.dumps(receipt, ensure_ascii=False, separators=(",", ":")),
          flush=True)


if __name__ == "__main__":
    main()
