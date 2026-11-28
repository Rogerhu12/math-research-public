#!/usr/bin/env python3
"""Publish one R742 result plus its handoff marker, with real pull/rebase."""
import argparse
import json
import os
from pathlib import Path
import time

from publish_r734_exact_conclusion import (
    CREDENTIAL, HANDOFF, LIMIT, REPOSITORY, TOPIC, blob_at, check_rules,
    complete_tree_bytes, git, optional_blob, revision, sha,
)


MARK=b"<!--r742-publish-->"


def checked_pull(note=None, report=None):
    old=revision("HEAD")
    p=git("pull","--rebase","origin","main",check=False)
    base=revision("FETCH_HEAD")
    if p.returncode:
        conflicts={s.decode() for s in git("diff","--name-only","--diff-filter=U","-z").stdout.split(b"\0") if s}
        if not note or not conflicts or not conflicts.issubset({HANDOFF,note}):
            raise RuntimeError((p.stdout+p.stderr).decode(errors="replace"))
    check_rules(old,base)
    if p.returncode:
        # Retain the whole remote H now. The publishing loop adds exactly our
        # one marker after rebase, calculating capacity on this same base.
        if HANDOFF in conflicts:
            Path(HANDOFF).write_bytes(blob_at(base,HANDOFF))
            git("add","--",HANDOFF)
        if note in conflicts:
            if optional_blob(base,note)!=report:
                raise ValueError("different result already present at this run path")
            Path(note).write_bytes(report)
            git("add","--",note)
        rc=git("diff","--cached","--quiet",check=False).returncode
        if rc not in (0,1):
            raise RuntimeError("cannot inspect rebase index")
        git("rebase","--continue" if rc else "--skip")
    return base


def handoff(old, base, note):
    lines=old.splitlines(keepends=True)
    if sum(x.startswith(MARK) for x in lines)>1:
        raise ValueError("duplicate R742 markers")
    other=b"".join(x for x in lines if not x.startswith(MARK))
    if other and not other.endswith(b"\n"):
        other+=b"\n"
    description="R742 [13设计全六jet](notes/"+Path(note).name+") "
    for label in (description,"R742 "):
        next_h=other+MARK+(label+"双README真pull "+base+"\n").encode()
        if len(next_h)<10000:
            return next_h
    return None


def publish(summary):
    run,attempt=os.environ["GITHUB_RUN_ID"],os.environ["GITHUB_RUN_ATTEMPT"]
    note=TOPIC+"/notes/r742-actual-two-jet-"+run+"-"+attempt+".json"
    report=summary.read_bytes()
    meta=json.loads(report)
    if (len(report)>=100000 or (meta["run"],meta["attempt"])!=(run,attempt)):
        raise ValueError("result size or run identity differs")
    git("config","user.name","math-research Actions")
    git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
    while True:
        base=checked_pull(note,report)
        remote=blob_at(base,HANDOFF)
        old_report=optional_blob(base,note)
        if old_report not in (None,report):
            raise ValueError("different published result at same run and attempt")
        new_h=handoff(remote,base,note)
        if new_h is None:
            print("H presently has insufficient bytes for the short marker; retrying",flush=True)
            time.sleep(15)
            continue
        tree=revision(base+":"+TOPIC)
        old_total=complete_tree_bytes(tree)
        planned=old_total+len(new_h)-len(remote)+len(report)-len(old_report or b"")
        print(f"R742 {base} tree {tree} {old_total} H {len(remote)}->{len(new_h)}, "
              f"note {len(old_report or b'')}->{len(report)}, planned {planned}",flush=True)
        if planned>LIMIT:
            time.sleep(15)
            continue
        local=revision("HEAD")!=base
        if local:
            paths=set(git("diff","--name-only",base,"HEAD").stdout.decode().splitlines())
            if not paths.issubset({HANDOFF,note}) or git("rev-list","--count",base+"..HEAD").stdout.strip()!=b"1":
                raise ValueError("unrelated local commits or files")
        Path(HANDOFF).write_bytes(new_h)
        Path(note).parent.mkdir(parents=True,exist_ok=True)
        Path(note).write_bytes(report)
        git("add","--",HANDOFF,note)
        rc=git("diff","--cached","--quiet",check=False).returncode
        if rc==1:
            if local:
                git("commit","--amend","--no-edit")
            else:
                git("commit","-m","Publish original R742 all-piece comparison and handoff")
        elif rc!=0:
            raise RuntimeError("cannot inspect publish index")
        elif not local:
            return
        p=git("-c","credential.helper=","-c","credential.helper="+CREDENTIAL,
              "push","origin","HEAD:refs/heads/main",check=False)
        if p.returncode==0:
            print(json.dumps({"note":note,"bytes":len(report),"sha256":sha(report),"base":base,
                              "published_commit":revision("HEAD"),"topic_bytes":planned}),flush=True)
            return
        msg=(p.stdout+p.stderr).decode(errors="replace")
        if not any(s in msg for s in ("non-fast-forward","fetch first","cannot lock ref",
                "remote ref updated","failed to update ref","stale info")):
            raise RuntimeError(msg)
        print("Remote moved; retrying immediate ordinary pull/rebase",flush=True)


if __name__=="__main__":
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument("mode",choices=("sync","publish"))
    cli.add_argument("--summary",type=Path)
    args=cli.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise RuntimeError("public project Actions required")
    os.chdir(os.environ["GITHUB_WORKSPACE"])
    if args.mode=="sync":
        base=checked_pull()
        with open(os.environ["GITHUB_ENV"],"a",encoding="utf-8") as f:
            f.write("R742_RULES_COMMIT="+base+"\n")
    elif args.summary:
        publish(args.summary.resolve())
    else:
        cli.error("publish requires --summary")
