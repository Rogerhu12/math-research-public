#!/usr/bin/env python3
"""Remove reproducible Serre data from main under root README rule 15.

No mathematics is executed and no data is uploaded to a Release or artifact.
The deleted bytes remain in the recorded Git history; metadata records SHA-256.
"""
import base64
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

REPO = Path(__file__).resolve().parents[3]
TOPIC = "topics/serre-uniformity"
RULES = ["README.md", TOPIC+"/README.md"]
MANIFEST = TOPIC+"/notes/2026-11-15-reproducible-data-removal-manifest.json.gz"
SUMMARY = TOPIC+"/notes/2026-11-15-reproducible-data-removal-summary.json"


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            h.update(block)
    return h.hexdigest()


def git(*args, check=True):
    env = os.environ.copy()
    token = env["SERRE_ACTIONS_TOKEN"]
    header = base64.b64encode(("x-access-token:"+token).encode()).decode()
    env.update(GIT_CONFIG_COUNT="2",
               GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
               GIT_CONFIG_VALUE_0="Authorization: Basic "+header,
               GIT_CONFIG_KEY_1="credential.helper", GIT_CONFIG_VALUE_1="")
    return subprocess.run(["git", *args], cwd=REPO, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=check)


def selected(path, size):
    if path.startswith(TOPIC+"/scripts/data/"):
        return True
    return (path.startswith(TOPIC+"/computations/") and size >= 100000
            and path.endswith((".gz", ".jsonl", ".csv", ".txt", ".log")))


def main():
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    source = git("rev-parse", "HEAD").stdout.strip()
    git("fetch", "--no-tags", "--filter=blob:none", "origin", "main")
    delta = git("diff", source, "origin/main", "--", *RULES).stdout
    if delta.strip():
        print("RULES_CHANGED_BEFORE_REMOVAL\n"+delta)
        return 3
    git("checkout", "-B", "serre-data-prune-"+os.environ["GITHUB_RUN_ID"], "origin/main")
    before = git("rev-parse", "HEAD").stdout.strip()
    inventory = []
    total = 0
    for line in git("ls-tree", "-r", "-l", "HEAD", "--", TOPIC).stdout.splitlines():
        meta, path = line.split("\t", 1)
        mode, kind, oid, raw_size = meta.split()
        if kind != "blob":
            continue
        size = int(raw_size)
        total += size
        if selected(path, size):
            local = REPO/path
            assert local.is_file() and not local.is_symlink()
            assert local.stat().st_size == size
            inventory.append({"path": path, "bytes": size, "git_blob_sha": oid,
                              "sha256": digest(local)})
    assert inventory, "No matching current data; inspect existing cleanup receipt instead of rerunning"
    removed = sum(row["bytes"] for row in inventory)
    assert total-removed < 190_000_000, "Selection does not satisfy current topic size limit"
    for offset in range(0, len(inventory), 100):
        git("rm", "--sparse", "--", *[r["path"] for r in inventory[offset:offset+100]])
    manifest = {
        "source_commit_before_removal": before,
        "workflow_source_commit": source,
        "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "selection": {
            "all_under": TOPIC+"/scripts/data/",
            "large_under": TOPIC+"/computations/",
            "minimum_large_bytes": 100000,
            "large_extensions": [".gz", ".jsonl", ".csv", ".txt", ".log"]},
        "files": inventory,
        "mathematics_recomputed": False,
        "removed_data_remain_in_git_history": True}
    manifest_path = REPO/MANIFEST
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    encoded = (json.dumps(manifest, sort_keys=True, separators=(",", ":"))+"\n").encode()
    manifest_path.write_bytes(gzip.compress(encoded, compresslevel=9, mtime=0))
    assert manifest_path.stat().st_size < 5_000_000
    summary = {
        "source_commit_before_removal": before, "workflow_source_commit": source,
        "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "workflow_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/"+os.environ["GITHUB_RUN_ID"],
        "script": TOPIC+"/scripts/prune_reproducible_data.py",
        "script_sha256": digest(Path(__file__)),
        "root_readme_sha256": digest(REPO/"README.md"),
        "topic_readme_sha256": digest(REPO/(TOPIC+"/README.md")),
        "removed_file_count": len(inventory), "removed_bytes": removed,
        "topic_bytes_before_removal": total,
        "topic_bytes_after_removal_before_metadata": total-removed,
        "manifest": MANIFEST, "manifest_sha256": digest(manifest_path),
        "manifest_bytes": manifest_path.stat().st_size,
        "history_restore_command": "git show "+before+":<exact path from manifest>",
        "mathematics_recomputed": False, "data_uploaded_to_release_or_artifact": False}
    (REPO/SUMMARY).write_text(json.dumps(summary, indent=2)+"\n")
    after = sum(p.stat().st_size for p in (REPO/TOPIC).rglob("*")
                if p.is_file() and not p.is_symlink())
    assert after < 200_000_000
    summary["actual_materialized_topic_bytes_after_removal"] = after
    (REPO/SUMMARY).write_text(json.dumps(summary, indent=2)+"\n")
    git("add", "--sparse", MANIFEST, SUMMARY)
    git("config", "user.name", "github-actions[bot]")
    git("config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
    git("commit", "-m", "serre: remove reproducible historical data under root rule 15")
    while True:
        git("pull", "--rebase", "origin", "main")
        delta = git("diff", source, "origin/main", "--", *RULES).stdout
        if delta.strip():
            print("RULES_CHANGED_DURING_PUBLICATION\n"+delta)
            return 3
        pushed = git("push", "origin", "HEAD:main", check=False)
        if pushed.returncode == 0:
            print(json.dumps(summary, indent=2))
            print("PUBLICATION_COMMIT="+git("rev-parse", "HEAD").stdout.strip())
            return 0
        if not any(w in pushed.stdout for w in ("fetch first", "non-fast-forward", "but expected")):
            print(pushed.stdout)
            return pushed.returncode


if __name__ == "__main__":
    sys.exit(main())
