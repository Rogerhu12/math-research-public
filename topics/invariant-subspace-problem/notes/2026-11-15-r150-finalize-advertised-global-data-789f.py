#!/usr/bin/env python3
"""Finalize already advertised exact data, one actual main commit at a time."""
import base64
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
sys.dont_write_bytecode = True
REPO = "Rogerhu12/math-research-public"
PREFIX = "topics/invariant-subspace-problem/notes/r150-saturated-third-global-actions-789f/43674463008-1"
STAGES = [
"f6c2932c3e53126ebb2f38eb8f604689ee4f0360",
"bfcb0734a8359cad1084ea4501a3574dbe0d9dd2",
"b6a0366ad7957214178721278503de888ba82cbe",
"d7e13156e774d1587716fd8118e2745a9da2f52f",
"070feb488031cefd810bc9befb665f10f14bb93d",
"29e0b9a0a3a29dfd3b603736bac75c1cc9463c84"]
RULES = {"README.md": "8fec34716cd4464b55ef546022bd4eb06ea8f50b2040f4025b7383d043db99f2",
"topics/invariant-subspace-problem/README.md": "40a65616e7a2cdcdc9916585c048b3f66547e71f0627b4abf58e5d3487ce1929"}
OUT = Path(os.environ["RUNNER_TEMP"]) / "isp-r150-finalize-advertised-data"
OUT.mkdir(exist_ok=True)
assert os.environ["GITHUB_REPOSITORY"] == REPO
token = os.environ["GH_TOKEN"]
auth = base64.b64encode(("x-access-token:" + token).encode()).decode()
env = dict(os.environ)
env.update(GIT_CONFIG_COUNT="5",
GIT_CONFIG_KEY_0="http.https://github.com/.extraheader", GIT_CONFIG_VALUE_0="AUTHORIZATION: basic " + auth,
GIT_CONFIG_KEY_1="credential.helper", GIT_CONFIG_VALUE_1="",
GIT_CONFIG_KEY_2="pack.window", GIT_CONFIG_VALUE_2="0",
GIT_CONFIG_KEY_3="pack.depth", GIT_CONFIG_VALUE_3="0",
GIT_CONFIG_KEY_4="push.negotiate", GIT_CONFIG_VALUE_4="true")
state = {"format": "r150-finalize-exact-advertised-global-data-v1", "status": "starting",
"originatingRun": "43674463008", "verifiedRecoveryRun": "43676091547",
"sourceCommit": "88be0c86d8924b4874e16b51c26732588696a5e3",
"executionRun": os.environ["GITHUB_RUN_ID"], "executionSource": os.environ["GITHUB_SHA"],
"publicationReranMathematics": False, "downloadedArtifactsAgain": False,
"forcePushUsed": False, "originalDataStageCommits": STAGES,
"maximumNewDataBytesPerMainCommit": 400000000, "pulls": [], "pushes": []}
def save():
    (OUT / "publication-receipt.json").write_text(json.dumps(state, indent=2) + "\n")
def git(*args, check=True):
    timeout = 900 if args and args[0] in ("fetch", "push", "pull") else 180
    r = subprocess.run(["git", *args], env=env, cwd=os.environ["GITHUB_WORKSPACE"],
        text=True, capture_output=True, timeout=timeout)
    stdout = r.stdout.replace(token, "***").replace(auth, "***")
    stderr = r.stderr.replace(token, "***").replace(auth, "***")
    with (OUT / "terminal-git.log").open("a") as f:
        f.write("$ git " + " ".join(args) + "\n" + stdout + stderr + "\nexit=" + str(r.returncode) + "\n")
    if check and r.returncode:
        raise RuntimeError("git failed: " + " ".join(args[:3]))
    return r.returncode, stdout, stderr
def tree(commit):
    out = git("ls-tree", "-r", "-z", commit, "--", PREFIX)[1]
    entries = {}
    for record in out.split("\0"):
        if not record:
            continue
        meta, path = record.split("\t", 1)
        mode, kind, sha = meta.split()
        assert kind == "blob" and mode == "100644" and path.startswith(PREFIX + "/")
        entries[path] = sha
    return entries
last_read = os.environ["GITHUB_SHA"]
def pull():
    global last_read
    rc, out, err = git("pull", "--rebase", "origin", "main", check=False)
    main = git("rev-parse", "origin/main")[1].strip()
    change = git("diff", last_read, main, "--", *RULES)[1]
    actual = {}
    for path in RULES:
        raw = subprocess.run(["git", "show", main + ":" + path], env=env,
            cwd=os.environ["GITHUB_WORKSPACE"], capture_output=True, check=True).stdout
        actual[path] = hashlib.sha256(raw).hexdigest()
    item = {"utc": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "beforeReadCommit": last_read, "originMainAfterPull": main,
        "exitCode": rc, "rulesSHA256": actual,
        "rulesDiffer": bool(change) or actual != RULES}
    state["pulls"].append(item)
    state["lastRulesReadCommit"] = main
    last_read = main
    (OUT / ("readme-diff-after-pull-" + str(len(state["pulls"])) + ".patch")).write_text(change)
    save()
    print("ISP_DATA_PULL " + json.dumps(item), flush=True)
    if item["rulesDiffer"]:
        raise RuntimeError("README changed: root must read this actual diff and apply it")
    if rc:
        raise RuntimeError("actual pull rebase failed")
save()
try:
    assert not git("status", "--porcelain")[1].strip()
    if git("rev-parse", "--is-shallow-repository")[1].strip() == "true":
        git("fetch", "--no-tags", "--unshallow", "--filter=blob:none", "origin", "main")
    git("fetch", "--no-tags", "--filter=blob:none", "origin", STAGES[-1])
    expected = tree(STAGES[-1])
    assert len(expected) == 1047, "complete exact data tree has 1047 stored files"
    for i, c in enumerate(STAGES):
        if i:
            assert git("rev-parse", c + "^")[1].strip() == STAGES[i - 1]
        changed = git("diff-tree", "--no-commit-id", "--name-only", "-r", "-z", c)[1].split("\0")
        assert all(not p or p.startswith(PREFIX + "/") for p in changed)
    state["allAdvertisedSourceCommitsRestrictedToExactDirectory"] = True
    state["storedFileCount"] = len(expected)
    state["expectedDataTreeSHA256"] = hashlib.sha256(json.dumps(expected, sort_keys=True).encode()).hexdigest()
    save()
    git("config", "user.name", "github-actions[bot]")
    git("config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
    git("switch", "-c", "isp-finalize-global-" + os.environ["GITHUB_RUN_ID"], STAGES[-1])
    while True:
        pull()
        assert tree("HEAD") == expected, "rebasing must preserve every exact original data blob"
        pending = git("rev-list", "--reverse", "origin/main..HEAD")[1].split()
        if not pending:
            assert tree("origin/main") == expected
            state.update(status="pushed", publishedCommit=git("rev-parse", "origin/main")[1].strip(),
                publishedResultDirectory=PREFIX)
            save()
            break
        commit = pending[0]
        names = git("diff-tree", "--no-commit-id", "--name-only", "-r", "-z", commit)[1].split("\0")
        assert all(not p or p.startswith(PREFIX + "/") for p in names)
        rc, out, err = git("push", "--progress", "origin", commit + ":refs/heads/main", check=False)
        state["pushes"].append({"commit": commit, "exitCode": rc,
            "pendingDataCommitsBeforePush": len(pending)})
        save()
        if rc == 0:
            print("ISP_DATA_MAIN_BATCH " + json.dumps(state["pushes"][-1]), flush=True)
            continue
        rejection = (out + err).lower()
        nff = (any(x in rejection for x in ("non-fast-forward", "fetch first", "[rejected]"))
            or ("cannot lock ref" in rejection and " is at " in rejection and " expected " in rejection)
            or ("[remote rejected]" in rejection and "failed to update ref" in rejection))
        if not nff:
            raise RuntimeError("bounded single-commit main push failed; advertised data remain intact")
        # The next operation is the required real pull/rebase and README comparison.
except Exception as e:
    state.update(status="publication-incomplete", errorType=type(e).__name__, error=str(e))
    save()
finally:
    print("ISP_GLOBAL_DATA_FINAL " + json.dumps(state), flush=True)
if state["status"] != "pushed":
    raise SystemExit(1)
