#!/usr/bin/env python3
"""Ordinarily merge a verified owned cache into current main, then pull/verify.

Use only after publish_topic_object_batches_v2.py completed the exact source.
No force update, credential file, repository-wide index or primary-data deletion.
GITHUB_TOKEN and Git authentication are supplied only in the caller's ephemeral
CLI environment. Every pull immediately checks the two READMEs; a changed rule
or independently changed topic is returned for reconciliation, never overwritten.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.error
import urllib.request

from publish_topic_checkpoint import update_read_marker


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ("active", "publish", "cache-state", "state"):
        ap.add_argument("--"+name, type=Path, required=True)
    ap.add_argument("--read", required=True)
    ap.add_argument("--message", required=True)
    a = ap.parse_args()
    active, pub = a.active.resolve(), a.publish.resolve()
    if active == pub:
        raise ValueError("Use the independent clean publisher")
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise ValueError("An ephemeral CLI GITHUB_TOKEN is required")
    cache = json.loads(a.cache_state.read_text())
    if not cache.get("complete_cache") or not cache.get("complete_source_topic_identity_checked"):
        raise ValueError("The immutable source must be completely cached first")
    topic, source, base = cache["topic"], cache["source"], cache["base"]
    branch, tip = cache["branch"], cache["batches"][-1]["commit"]
    if topic != "topics/visible-flex-larger-amplitude" or branch != "agent-visible-larger-cache-"+source[:20]:
        raise ValueError("The owned topic/cache identity differs")
    if a.state.exists():
        raise FileExistsError("Use a fresh publication state; do not overwrite history")
    env = {k:v for k,v in os.environ.items() if not k.startswith("GIT_TRACE") and k != "GIT_CURL_VERBOSE"}

    def git(*args, data=None, check=True):
        p = subprocess.run(["git", "-c", "gc.auto=0", *args], cwd=pub, env=env,
            input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if check and p.returncode:
            raise RuntimeError("git "+args[0]+" failed: "+p.stderr.decode()[-1500:])
        return p

    def value(*args):
        return git(*args).stdout.decode().strip()

    if value("status", "--porcelain=v1", "--untracked-files=all"):
        raise ValueError("The dedicated publisher must be clean")
    # Only the two rule files need a working copy; all research is in the
    # active checkout and immutable Git objects. This is reversible sparse IO.
    git("sparse-checkout", "set", "--no-cone", "--stdin",
        data=("/README.md\n/"+topic+"/README.md\n").encode())
    source_tree = value("rev-parse", source+":"+topic)
    if value("rev-parse", tip+":"+topic) != source_tree:
        raise ValueError("The complete cache topic is not the source topic")
    changed = value("diff", "--name-only", base, tip).splitlines()
    if any(not p.startswith(topic+"/") for p in changed):
        raise ValueError("The cache changes another topic or root file")
    state = dict(source=source, base=base, topic=topic, cache_ref=branch, cache_tip=tip,
        source_topic_tree=source_tree, changed_files=len(changed), read=a.read,
        published=None, force=False, synchronizations=[], merge_attempts=[],
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())

    def save():
        state["updated_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        temp = a.state.with_suffix(a.state.suffix+".tmp")
        temp.write_text(json.dumps(state,indent=2,ensure_ascii=False)+"\n")
        temp.replace(a.state)

    def pull():
        git("pull", "--quiet", "--rebase", "origin", "main")
        head = value("rev-parse", "HEAD")
        diff = git("diff", state["read"], head, "--", "README.md", topic+"/README.md").stdout
        sync = dict(operation="pull --rebase", head=head, readme_changed=bool(diff),
            utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
        state["synchronizations"].append(sync)
        if diff:
            state["blocked"] = "Read the changed README diff and apply it immediately"
            save(); print(diff.decode(),flush=True); raise SystemExit(50)
        state["read"] = head
        handoff = active/topic/"HANDOFF.md"
        temporary = handoff.with_suffix(".md.merge-marker.tmp")
        temporary.write_text(update_read_marker(handoff.read_text(),head));temporary.replace(handoff)
        save()
        print(json.dumps(sync),flush=True)
        return head

    head = pull()
    while True:
        upstream_tree = value("rev-parse", head+":"+topic)
        if upstream_tree == source_tree:
            state["published"] = head
            state["already_contains_exact_source_topic"] = True
            break
        if upstream_tree != value("rev-parse", base+":"+topic):
            state["blocked"] = "Upstream topic changed independently; reconcile before merging"
            save();raise SystemExit(51)
        remote = value("ls-remote", "origin", "refs/heads/"+branch).split()
        if not remote or remote[0] != tip:
            raise ValueError("The verified owned remote cache tip changed")
        body = dict(base="main",head=tip,commit_message=a.message)
        request = urllib.request.Request(
            "https://api.github.com/repos/Rogerhu12/math-research/merges",
            data=json.dumps(body).encode(),method="POST",headers={
                "Authorization":"Bearer "+token,"Accept":"application/vnd.github+json",
                "X-GitHub-Api-Version":"2022-11-28","User-Agent":"math-research-authorized-checkpoint"})
        attempt = dict(index=len(state["merge_attempts"])+1, after_pull=head,
            utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
        try:
            with urllib.request.urlopen(request,timeout=50) as response:
                raw=response.read(); data=json.loads(raw) if raw else {}
                attempt.update(http_status=response.status,merge_sha=data.get("sha"),
                    parents=[p["sha"] for p in data.get("parents",[])])
        except urllib.error.HTTPError as error:
            attempt["http_status"] = error.code
        state["merge_attempts"].append(attempt)
        if attempt["http_status"] == 201:
            state["published"] = attempt["merge_sha"]
            save();head=pull();break
        if attempt["http_status"] == 204:
            save();head=pull();state["published"]=head;break
        save()
        if attempt["http_status"] == 409:
            # A normal merge conflict/race never skips the new root rule.
            head=pull();continue
        raise RuntimeError("Ordinary merge HTTP status "+str(attempt["http_status"]))
    published = state["published"]
    if (git("merge-base", "--is-ancestor", published, head, check=False).returncode
            or value("rev-parse", published+":"+topic) != source_tree):
        state["blocked"]="Post-pull publication identity differs; reconcile without overwriting"
        save();raise SystemExit(52)
    state["main_ancestry_and_exact_source_topic_verified"] = True
    remote = value("ls-remote", "origin", "refs/heads/"+branch).split()
    if remote and remote[0] == tip:
        deleted = git("push", "origin", ":refs/heads/"+branch, check=False)
        state["owned_cache_deletion_exitcode"] = deleted.returncode
        state["owned_cache_deleted"] = deleted.returncode == 0
    elif not remote:
        state["owned_cache_already_absent"] = True
    else:
        state["owned_cache_retained_because_tip_changed"] = True
    save()
    print(json.dumps(dict(published=published,source=source,read=state["read"],
        source_topic_tree=source_tree,files=len(changed),
        owned_cache_deleted=state.get("owned_cache_deleted",False))),flush=True)


if __name__ == "__main__":
    main()
