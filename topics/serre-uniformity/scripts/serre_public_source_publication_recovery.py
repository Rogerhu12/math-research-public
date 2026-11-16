#!/usr/bin/env python3
"""Publish reviewed source text through the authorized public repository Actions."""
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import urllib.request
import urllib.error
import time

REPO = "Rogerhu12/math-research-public"
REQUEST = "topics/serre-uniformity/notes/serre-source-publication-recovery-request.json"
H = "topics/serre-uniformity/HANDOFF.md"
LOG = "topics/serre-uniformity/log.md"
RULES = ("README.md", "topics/serre-uniformity/README.md")
SESSION = "serre-public-astra-20261115"

def sha(data):
    return hashlib.sha256(data).hexdigest()

def git(*args, check=True):
    p = subprocess.run(["git", "-c", "user.name="+SESSION, "-c", "user.email=research-agent@users.noreply.github.com", *args], capture_output=True, text=True)
    if check and p.returncode:
        print(p.stdout, end="")
        print(p.stderr, end="", file=sys.stderr)
        raise SystemExit(p.returncode)
    return p

def safe(path):
    p = Path(path)
    assert not p.is_absolute() and ".." not in p.parts
    assert path.startswith("topics/serre-uniformity/") or re.fullmatch(r"\.github/workflows/serre-[A-Za-z0-9_-]+\.yml", path)
    assert p.suffix in (".md", ".py", ".json", ".yml")
    return p

def refresh_rules(request):
    before = git("rev-parse", "HEAD").stdout.strip()
    git("pull", "--rebase", "origin", "main")
    head = git("rev-parse", "origin/main").stdout.strip()
    actual = {name: sha(Path(name).read_bytes()) for name in RULES}
    stamp = dt.datetime.now(dt.timezone.utc).isoformat()
    print("ACTUAL_RULES_PULL=" + json.dumps({"head": head, "UTC": stamp, "readme_sha256": actual}), flush=True)
    if actual != request["readme_sha256"]:
        old = request["rules_last_read_commit"]
        git("fetch", "--filter=blob:none", "--depth=1", "origin", old)
        print(git("diff", old, head, "--", *RULES).stdout, flush=True)
        raise SystemExit("README changed: root must read this actual diff before continuing.")
    return head, stamp

def update_record(head, stamp):
    p = Path(H)
    text, count = re.subn(r"\*\*已读规则提交：[0-9a-f]+\*\*（[^）]*）",
        "**已读规则提交：" + head + "**（" + stamp + "；公开Actions真实git pull --rebase origin main，两README SHA无变化）",
        p.read_text(), count=1)
    assert count == 1 and len(text.encode()) < 10000
    p.write_text(text)
    p = Path(LOG)
    lines = p.read_text().splitlines()
    header = None
    for i in range(len(lines)-1, -1, -1):
        if lines[i].startswith("### ") and SESSION in lines[i]:
            header = i
            lines[i] = "### " + dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M") + " Asia/Taipei — " + SESSION
            break
    assert header is not None
    for i in range(len(lines)-1, header, -1):
        if lines[i].startswith("- 本push规则："):
            lines[i] = "- 本push规则：公开Actions真实pull至" + head + "（" + stamp + "），两README SHA6979d793/35f82f3d无diff；本仓库Actions执行恢复发布，主目标OPEN。"
            break
    else:
        raise AssertionError("missing final rules entry")
    p.write_text("\n".join(lines) + "\n")

def commit(message, amend=False):
    git("add", "--", H, LOG)
    args = ["-c", "user.name="+SESSION, "-c", "user.email=research-agent@users.noreply.github.com", "commit"]
    args += ["--amend", "--no-edit"] if amend else ["-m", message]
    git(*args)


def replace_only_unstarted_run(dispatch, token):
    run_id = dispatch.get("replace_unstarted_run_id")
    if run_id is None:
        return True
    assert isinstance(run_id, int) and run_id > 0
    expected = dispatch["replace_expected_head_sha"]
    assert re.fullmatch(r"[0-9a-f]{40}", expected)
    base = "https://api.github.com/repos/" + REPO + "/actions/runs/" + str(run_id)
    headers = {"Authorization": "Bearer "+token, "Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28"}
    def get(url):
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as response:
            return json.load(response)
    run = get(base)
    assert run["head_sha"] == expected
    assert run["path"] == ".github/workflows/" + dispatch["workflow"]
    assert run["event"] == "workflow_dispatch"
    jobs = get(base + "/jobs?per_page=100")
    if run["status"] != "queued" or jobs["total_count"] != 0:
        print("UNSTARTED_REPLACEMENT_SKIPPED=" + json.dumps({"run_id": run_id,
              "status": run["status"], "job_count": jobs["total_count"],
              "reason": "Original request has started or is already complete; no duplicate dispatch."}), flush=True)
        return False
    if dispatch.get("requeue_unstarted_same_concurrency") is True:
        workflow = Path(".github/workflows") / dispatch["workflow"]
        workflow_bytes = workflow.read_bytes()
        assert sha(workflow_bytes) == dispatch["expected_workflow_sha256"]
        group = dispatch["expected_concurrency_group"]
        assert re.fullmatch(r"serre-[A-Za-z0-9_-]+-\$\{\{ github\.ref \}\}", group)
        exact = "concurrency:\n  group: " + group + "\n  cancel-in-progress: false\n"
        assert exact in workflow_bytes.decode()
        print("UNSTARTED_SAME_CONCURRENCY_REQUEUE=" + json.dumps({"run_id": run_id,
              "head_sha": expected, "job_count": 0, "workflow": dispatch["workflow"],
              "concurrency_group": group,
              "reason": "Previously observed standard and force cancellation conflicts; requeue the same source under the unchanged single-running concurrency group."}), flush=True)
        return True
    req = urllib.request.Request(base + "/cancel", data=b"", method="POST", headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            assert response.status == 202
    except urllib.error.HTTPError as error:
        if error.code != 409:
            raise
        run = get(base)
        jobs = get(base + "/jobs?per_page=100")
        if run["head_sha"] != expected or run["path"] != ".github/workflows/" + dispatch["workflow"] or run["event"] != "workflow_dispatch" or run["status"] != "queued" or jobs["total_count"] != 0:
            print("UNSTARTED_REPLACEMENT_SKIPPED=" + json.dumps({"run_id": run_id,
                  "status": run["status"], "job_count": jobs["total_count"],
                  "reason": "Run state changed after standard cancellation conflict; no duplicate dispatch."}), flush=True)
            return False
        print("UNSTARTED_STANDARD_CANCEL_CONFLICT=" + json.dumps({"run_id": run_id,
              "head_sha": expected, "job_count": 0,
              "reason": "Same original request remains queued with zero jobs; try documented force-cancel."}), flush=True)
        force_req = urllib.request.Request(base + "/force-cancel", data=b"", method="POST", headers=headers)
        try:
            with urllib.request.urlopen(force_req, timeout=60) as response:
                assert response.status == 202
        except urllib.error.HTTPError as force_error:
            if force_error.code != 409:
                raise
            print("UNSTARTED_REPLACEMENT_SKIPPED=" + json.dumps({"run_id": run_id,
                  "reason": "Both standard and force cancellation returned conflict; original remains unstarted, no duplicate dispatch."}), flush=True)
            return False
    for attempt in range(13):
        run = get(base)
        if run["status"] == "completed":
            break
        if attempt < 12:
            time.sleep(5)
    jobs = get(base + "/jobs?per_page=100")
    if run["status"] != "completed" or run["conclusion"] != "cancelled" or jobs["total_count"] != 0:
        print("UNSTARTED_REPLACEMENT_SKIPPED=" + json.dumps({"run_id": run_id,
              "status": run["status"], "conclusion": run["conclusion"],
              "job_count": jobs["total_count"],
              "reason": "Cancellation did not certify zero started jobs; no duplicate dispatch."}), flush=True)
        return False
    print("UNSTARTED_RUN_CANCELLED=" + json.dumps({"run_id": run_id, "head_sha": expected,
          "job_count": 0, "no_mathematical_job_started": True}), flush=True)
    return True

def main():
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == REPO
    source = git("rev-parse", "HEAD").stdout.strip()
    assert source == os.environ["GITHUB_SHA"]
    request_bytes = Path(REQUEST).read_bytes()
    request = json.loads(request_bytes)
    assert request["schema"] == 1 and request["session"] == SESSION
    assert request["source_branch"] == os.environ["GITHUB_REF_NAME"]
    payload = {}
    expected = {}
    for row in request["files"]:
        name = row["path"]
        path = safe(name)
        data = path.read_bytes()
        assert len(data) < 100000 and sha(data) == row["sha256"]
        if name == H:
            assert len(data) < 10000
        if name.endswith("/open.md"):
            assert len(data) < 30000
        payload[name] = data
        expected[name] = row["expected_previous_sha256"]
    payload[REQUEST] = request_bytes
    expected[REQUEST] = request["expected_previous_request_sha256"]
    assert H in payload and LOG in payload
    git("fetch", "--filter=blob:none", "--depth=1", "origin", "refs/heads/main:refs/remotes/origin/main")
    git("checkout", "-B", "serre-source-publication-work", "origin/main")
    head, stamp = refresh_rules(request)
    if Path(REQUEST).exists() and Path(REQUEST).read_bytes() == request_bytes:
        for name, data in payload.items():
            if name not in (H, LOG):
                assert Path(name).read_bytes() == data, name
        print("ALREADY_PUBLISHED=" + json.dumps({"request_id": request["request_id"], "head": head}), flush=True)
        return
    for name, data in payload.items():
        path = safe(name)
        actual = sha(path.read_bytes()) if path.exists() else None
        assert actual == expected[name], (name, actual, expected[name])
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    update_record(head, stamp)
    git("add", "--", *payload)
    commit(request["commit_message"])
    attempt = 0
    while True:
        attempt += 1
        head, stamp = refresh_rules(request)
        update_record(head, stamp)
        commit(request["commit_message"], amend=True)
        result = git("push", "origin", "HEAD:refs/heads/main", check=False)
        print(result.stdout + result.stderr, flush=True)
        if result.returncode == 0:
            published = git("rev-parse", "HEAD").stdout.strip()
            print("PUBLISHED=" + json.dumps({"request_id": request["request_id"], "source_commit": source, "main_commit": published, "attempt": attempt}), flush=True)
            break
        message = result.stdout + result.stderr
        if not any(x in message for x in ("non-fast-forward", "fetch first", "[rejected]", "[remote rejected]", "cannot lock ref")):
            raise SystemExit(result.returncode)
        print("Push rejected: immediately pulling with rebase again.", flush=True)
    token = os.environ["GH_TOKEN"]
    for dispatch in request.get("dispatch_workflows", []):
        assert re.fullmatch(r"serre-[A-Za-z0-9_-]+\.yml", dispatch["workflow"])
        assert dispatch["request_path"].startswith("topics/serre-uniformity/notes/")
        assert safe(dispatch["request_path"]).suffix == ".json"
        assert sha(Path(dispatch["request_path"]).read_bytes()) == dispatch["request_sha256"]
        if not replace_only_unstarted_run(dispatch, token):
            continue
        url = "https://api.github.com/repos/" + REPO + "/actions/workflows/" + dispatch["workflow"] + "/dispatches"
        body = json.dumps({"ref": "main"}).encode()
        req = urllib.request.Request(url, data=body, method="POST", headers={"Authorization": "Bearer "+token, "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"})
        for dispatch_attempt in range(1, 13):
            try:
                with urllib.request.urlopen(req, timeout=60) as response:
                    assert response.status == 204
                break
            except urllib.error.HTTPError as error:
                detail = error.read().decode("utf-8", errors="replace")
                print("WORKFLOW_DISPATCH_HTTP_ERROR=" + json.dumps({"workflow": dispatch["workflow"], "attempt": dispatch_attempt, "status": error.code, "body": detail[:4096]}), flush=True)
                if error.code not in (404, 422) or dispatch_attempt == 12:
                    raise
                time.sleep(5)
        print("WORKFLOW_DISPATCH_ACCEPTED=" + json.dumps({"workflow": dispatch["workflow"], "published_commit": published, "request_sha256": dispatch["request_sha256"]}), flush=True)

if __name__ == "__main__":
    main()
