#!/usr/bin/env python3
"""Publish the complete R734 summary and its handoff marker on this public repo.

The full mathematical workflow is unchanged. The remote topic total comes
from GitHub tree-size metadata, then only the actual note/H byte deltas apply.
"""
from functools import lru_cache
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time
import urllib.error
import urllib.request

REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-larger-amplitude"
HANDOFF = TOPIC + "/HANDOFF.md"
RULES = {
    "README.md": "539f1ea02feb8a63c5aa734ed560ab6ecbf3ff7f570212e46788413bb072f444",
    TOPIC+"/README.md": "3c1c03b358792b6c9937b95fcfea05b80a572a4da2cce615c4c9832fe929057d",
}
MARK = b"<!--r734-publish-->"
LIMIT = 200000000
CREDENTIAL = '!f() { if test "$1" = get; then printf "%s\\n" "username=x-access-token" "password=$GITHUB_TOKEN"; fi; }; f'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(*args, check=True):
    proc = subprocess.run(["git",*args],capture_output=True,
                          env=dict(os.environ,GIT_EDITOR="true",GIT_TERMINAL_PROMPT="0"))
    if check and proc.returncode:
        raise RuntimeError("git "+args[0]+" failed\n"+(proc.stdout+proc.stderr).decode(errors="replace"))
    return proc


def revision(ref):
    return git("rev-parse","--verify",ref).stdout.decode().strip()


def blob_at(commit, path):
    return git("show",commit+":"+path).stdout


def optional_blob(commit, path):
    entry=git("ls-tree","-z",commit,"--",path).stdout
    return blob_at(commit,path) if entry else None


def check_rules(old, base):
    for path,expected in RULES.items():
        if sha(blob_at(base,path)) != expected:
            print(git("diff",old,base,"--",path).stdout.decode(errors="replace"),flush=True)
            raise RuntimeError("Changed README at "+base+": "+path)
    print("R734 actual git pull --rebase origin main; both README hashes checked at "+base,flush=True)


def marked(remote, base, name):
    lines = remote.splitlines(keepends=True)
    if sum(line.startswith(MARK) for line in lines)>1:
        raise RuntimeError("More than one R734 handoff marker")
    other = b"".join(line for line in lines if not line.startswith(MARK))
    if other and not other.endswith(b"\n"):
        other += b"\n"
    stem = Path(name).name
    full = MARK + ("R734 [完整补录](notes/"+stem+")；双README真pull \x60"+base+"\x60。\n").encode()
    short = MARK + ("R734双README真pull \x60"+base+"\x60。\n").encode()
    if len(other)+len(full)<10000:
        return other+full
    if len(other)+len(short)<10000:
        return other+short
    return None


def pull(note=None, body=None):
    old = revision("HEAD")
    result = git("pull","--rebase","origin","main",check=False)
    if result.returncode:
        conflicts = {x.decode() for x in git("diff","--name-only","--diff-filter=U","-z").stdout.split(b"\0") if x}
        if note is None or not conflicts or not conflicts.issubset({HANDOFF,note}):
            raise RuntimeError("Pull/rebase failed\n"+(result.stdout+result.stderr).decode(errors="replace"))
    base = revision("FETCH_HEAD")
    check_rules(old,base)
    if result.returncode:
        # This runner owns one unpublished commit. Begin with the entire new
        # remote handoff. The one R734 line is the only local contribution.
        if HANDOFF in conflicts:
            remote = blob_at(base,HANDOFF)
            resolved = marked(remote,base,note)
            Path(HANDOFF).write_bytes(remote if resolved is None else resolved)
            git("add","--",HANDOFF)
        if note in conflicts:
            if optional_blob(base,note) != body:
                raise RuntimeError("Remote has a different conclusion at the same run/attempt path")
            Path(note).write_bytes(body)
            git("add","--",note)
        clean = git("diff","--cached","--quiet",check=False).returncode
        if clean == 0:
            git("rebase","--skip")
        elif clean == 1:
            git("rebase","--continue")
        else:
            raise RuntimeError("Unable to inspect staged conflict resolution")
    return base


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def tree(oid, recursive):
    url = "https://api.github.com/repos/"+REPOSITORY+"/git/trees/"+oid
    if recursive:
        url += "?recursive=1"
    req = urllib.request.Request(url,headers={
        "Accept":"application/vnd.github+json",
        "Authorization":"Bearer "+os.environ["GITHUB_TOKEN"],
        "X-GitHub-Api-Version":"2022-11-28","User-Agent":"R734-topic-size-metadata"})
    for attempt in range(5):
        try:
            with urllib.request.build_opener(NoRedirect).open(req,timeout=60) as response:
                record=json.load(response)
            break
        except urllib.error.HTTPError as error:
            if attempt==4 or error.code not in (429,500,502,503,504):
                raise
            time.sleep(min(30,2**attempt))
        except urllib.error.URLError:
            if attempt==4:
                raise
            time.sleep(min(30,2**attempt))
    if record.get("sha")!=oid or not isinstance(record.get("tree"),list):
        raise RuntimeError("Unexpected tree metadata identity: "+oid)
    return record


def blob_bytes(entries):
    size=0
    for item in entries:
        if item["type"]=="blob":
            n=item.get("size")
            if type(n) is not int or n<0:
                raise ValueError("Missing GitHub blob.size for "+item["path"])
            size+=n
    return size


@lru_cache(maxsize=None)
def complete_tree_bytes(oid):
    record=tree(oid,True)
    if record.get("truncated") is False:
        return blob_bytes(record["tree"])
    direct=tree(oid,False)
    if direct.get("truncated") is not False:
        raise RuntimeError("Incomplete direct tree listing: "+oid)
    entries=direct["tree"]
    return blob_bytes(entries)+sum(complete_tree_bytes(x["sha"]) for x in entries if x["type"]=="tree")


def publish(summary):
    run=os.environ["GITHUB_RUN_ID"]
    attempt=os.environ["GITHUB_RUN_ATTEMPT"]
    note=TOPIC+"/notes/r734-actual-Hermite-"+run+"-"+attempt+".json"
    body=summary.read_bytes()
    report=json.loads(body)
    if (str(report["run"]),str(report["attempt"]))!=(run,attempt):
        raise RuntimeError("The summary's execution identity differs from this run/attempt")
    git("config","user.name","math-research Actions")
    git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
    while True:
        base=pull(note,body)
        # Always account against the actual fetched remote commit, never a
        # local unpublished tree. Its tree OID needs no file-size lookups.
        base_h=blob_at(base,HANDOFF)
        base_note=optional_blob(base,note)
        if base_note is not None and base_note!=body:
            raise RuntimeError("Do not replace a different public result for this run/attempt")
        next_h=marked(base_h,base,note)
        if next_h is None:
            print("No handoff room for even the short R734 marker; retrying an actual pull",flush=True)
            time.sleep(15)
            continue
        topic_tree=revision(base+":"+TOPIC)
        remote_bytes=complete_tree_bytes(topic_tree)
        delta=len(next_h)-len(base_h)+len(body)-len(base_note or b"")
        planned=remote_bytes+delta
        print(f"R734 topic {base} tree {topic_tree}: remote {remote_bytes} bytes, "
              f"handoff {len(base_h)}->{len(next_h)}, note {len(base_note or b'')}->{len(body)}, total {planned}",
              flush=True)
        if planned>LIMIT:
            print("Waiting for actual topic capacity; complete summary remains in this job log",flush=True)
            time.sleep(15)
            continue
        local = revision("HEAD")!=base
        if local:
            changed = set(git("diff","--name-only",base,"HEAD").stdout.decode().splitlines())
            if (git("rev-list","--count",base+"..HEAD").stdout.strip()!=b"1"
                    or not changed.issubset({HANDOFF,note})):
                raise RuntimeError("Unexpected unpublished commits outside this result")
        Path(HANDOFF).write_bytes(next_h)
        Path(note).parent.mkdir(parents=True,exist_ok=True)
        Path(note).write_bytes(body)
        git("add","--",HANDOFF,note)
        changed=git("diff","--cached","--quiet",check=False).returncode
        if changed==1:
            if local:
                git("commit","--amend","--no-edit")
            else:
                git("commit","-m","Publish complete R734 fixed Hermite conclusion and checked handoff")
        elif changed!=0:
            raise RuntimeError("Could not inspect the staged result")
        elif not local:
            print("Complete result and handoff already at remote "+base,flush=True)
            return
        push=git("-c","credential.helper=","-c","credential.helper="+CREDENTIAL,
                 "push","origin","HEAD:refs/heads/main",check=False)
        if push.returncode==0:
            print(json.dumps({"published":note,"bytes":len(body),"sha256":sha(body),
                              "commit":revision("HEAD"),"rules_checked_remote_commit":base,
                              "complete_topic_bytes":planned}),flush=True)
            return
        message=(push.stdout+push.stderr).decode(errors="replace")
        if not any(s in message for s in ("non-fast-forward","fetch first","cannot lock ref",
                "remote ref updated","failed to update ref","stale info")):
            raise RuntimeError("Ordinary push failed\n"+message)
        print("Remote main moved; immediately pulling/rebasing the complete result",flush=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("mode",choices=["sync","publish"])
    p.add_argument("--summary",type=Path)
    args=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise RuntimeError("This publisher belongs to the public project runner")
    os.chdir(os.environ["GITHUB_WORKSPACE"])
    if args.mode=="sync":
        base=pull()
        with open(os.environ["GITHUB_ENV"],"a",encoding="utf-8") as stream:
            stream.write("R734_RULES_COMMIT="+base+"\n")
    else:
        if args.summary is None:
            p.error("publish requires --summary")
        publish(args.summary.resolve())


if __name__=="__main__":
    main()
