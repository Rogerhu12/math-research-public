#!/usr/bin/env python3
"""Publish this session's prepared text through real partial-clone git operations."""
import datetime as dt
import json
import os
from pathlib import Path
import re
import subprocess
import sys

REPO = "Rogerhu12/math-research-public"
SESSION = "Astra-serre-24b8836b-20261126"
TOPIC = "topics/serre-uniformity/"
H = TOPIC + "HANDOFF.md"
LOG = TOPIC + "log.md"
REQUEST = TOPIC + "notes/astra24-publication-request.json"
RULES = ("README.md", TOPIC + "README.md")

def git(*args, check=True, binary=False):
    env = os.environ.copy()
    token = env.get("GH_TOKEN")
    if token:
        import base64
        env["GIT_CONFIG_COUNT"] = "1"
        env["GIT_CONFIG_KEY_0"] = "http.https://github.com/.extraheader"
        env["GIT_CONFIG_VALUE_0"] = "AUTHORIZATION: basic " + base64.b64encode(("x-access-token:" + token).encode()).decode()
    result = subprocess.run(["git", "-c", "user.name=" + SESSION,
        "-c", "user.email=astra-serre@users.noreply.github.com", *args],
        capture_output=True, text=not binary, env=env)
    if check and result.returncode:
        out = result.stdout + result.stderr
        sys.stdout.buffer.write(out if binary else out.encode())
        raise SystemExit(result.returncode)
    return result

def safe(name):
    path = Path(name)
    assert not path.is_absolute() and ".." not in path.parts
    assert name.startswith(TOPIC) or name == ".github/workflows/serre-astra24-publication.yml"
    assert path.suffix in (".md", ".py", ".json", ".yml")
    return path

def blob(ref, name):
    result = git("rev-parse", "--verify", ref + ":" + name, check=False)
    return result.stdout.strip() if result.returncode == 0 else None

def refresh(request):
    git("pull", "--rebase", "origin", "main")
    head = git("rev-parse", "FETCH_HEAD").stdout.strip()
    stamp = dt.datetime.now(dt.timezone.utc).isoformat()
    actual = {path: blob(head, path) for path in RULES}
    old = request["last_read_rules_commit"]
    if git("cat-file", "-e", old + "^{commit}", check=False).returncode:
        git("fetch", "--filter=blob:none", "--depth=1", "origin", old)
    diff = git("diff", "--no-ext-diff", old, head, "--", *RULES).stdout
    print("SERRE_ACTUAL_PULL " + json.dumps({
        "session": SESSION, "head": head, "utc": stamp,
        "last_read_rules_commit": old, "rules_git_blobs": actual,
        "readme_diff_empty": not diff,
        "partial_clone_filter": git("config", "remote.origin.partialclonefilter").stdout.strip()
    }, ensure_ascii=False), flush=True)
    if diff or actual != request["rules_git_blobs"]:
        print(diff, flush=True)
        raise SystemExit("README changed: read this exact diff and update the prepared text.")
    return head, stamp

def update_record(head, stamp):
    path = Path(H)
    text = path.read_text()
    replacement = "**公开两README已读提交：" + head + "**（" + stamp + "；本公开Actions真实git pull --rebase，两README差异为空）"
    text, count = re.subn(r"\*\*公开两README已读提交：[0-9a-f]{40}\*\*（[^\n]*?）", replacement, text, count=1)
    assert count == 1 and len(text.encode()) < 10000
    path.write_text(text)
    path = Path(LOG)
    lines = path.read_text().splitlines()
    for index in range(len(lines) - 1, -1, -1):
        if lines[index].startswith("- 本push规则："):
            lines[index] = "- 本push规则：公开Actions真实pull至 " + head + "（" + stamp + "），两README diff为空；本次真实git推送，主目标OPEN。"
            break
    else:
        raise AssertionError("Missing current log rule record")
    path.write_text("\n".join(lines) + "\n")

def main():
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == REPO
    source = git("rev-parse", "HEAD").stdout.strip()
    assert source == os.environ["GITHUB_SHA"]
    request_bytes = Path(REQUEST).read_bytes()
    request = json.loads(request_bytes)
    assert request["session"] == SESSION and request["schema"] == 1
    assert request["source_branch"] == os.environ["GITHUB_REF_NAME"]
    prepared = {}
    expected = {}
    for row in request["files"]:
        name = row["path"]
        path = safe(name)
        data = path.read_bytes()
        assert len(data) < 100000
        if name == H:
            assert len(data) < 10000
        if name == TOPIC + "open.md":
            assert len(data) < 30000
        prepared[name] = data
        expected[name] = row["previous_git_blob"]
    prepared[REQUEST] = request_bytes
    expected[REQUEST] = request["previous_request_git_blob"]
    assert H in prepared and LOG in prepared
    git("fetch", "--filter=blob:none", "--depth=2", "origin", "refs/heads/main:refs/remotes/origin/main")
    git("checkout", "-B", "serre-astra24-publication-work", "origin/main")
    head, stamp = refresh(request)
    if Path(REQUEST).exists() and Path(REQUEST).read_bytes() == request_bytes:
        for name, data in prepared.items():
            if name not in (H, LOG):
                assert Path(name).read_bytes() == data, name
        print("SERRE_ALREADY_PUBLISHED " + json.dumps({"request": request["request_id"], "head": head}), flush=True)
        return
    for name, data in prepared.items():
        assert blob("HEAD", name) == expected[name], "Concurrent content change: " + name
        path = safe(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    update_record(head, stamp)
    git("add", "--", *prepared)
    git("commit", "-m", request["message"])
    attempt = 0
    while True:
        attempt += 1
        head, stamp = refresh(request)
        update_record(head, stamp)
        git("add", "--", H, LOG)
        git("commit", "--amend", "--no-edit")
        result = git("push", "origin", "HEAD:refs/heads/main", check=False)
        print(result.stdout + result.stderr, flush=True)
        if result.returncode == 0:
            print("SERRE_PUBLISHED " + json.dumps({
                "request": request["request_id"], "source_commit": source,
                "main_commit": git("rev-parse", "HEAD").stdout.strip(),
                "rules_read_commit": head, "pull_utc": stamp, "attempt": attempt
            }), flush=True)
            return
        if not any(x in result.stdout + result.stderr for x in
                   ("non-fast-forward", "fetch first", "[rejected]", "[remote rejected]", "cannot lock ref")):
            raise SystemExit(result.returncode)
        print("Push rejected: immediately pull --rebase and retry.", flush=True)

if __name__ == "__main__":
    main()
