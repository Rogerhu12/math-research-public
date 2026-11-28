#!/usr/bin/env python3
"""Run four independent complete R758 physical fits, supervise real pulls and publish their small conclusions."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from publish_r734_exact_conclusion import (
    CREDENTIAL,HANDOFF,LIMIT,REPOSITORY,TOPIC,blob_at,check_rules,complete_tree_bytes,
    git,optional_blob,revision,sha,
)

HERE=TOPIC+"/scripts/resume_20261126/"
NAMES=("r740_rolled_disk_seed.py","r742_tilted_disk_two_jets.py","r744_extruded_closed_two_jets.py",
       "r754_coherent_mirror_bowed_walls_two_jets.py","r756_return_elbows_preloaded_exact_rolls.py",
       "r758_curved_outer_collars_and_fixed_elliptical_crowns.py","solve_r758_curved_crown_middle_annuli.py",
       "publish_r734_exact_conclusion.py","run_r758_all_curved_crown_fits.py")
MARK=b"<!--r758-publish-->"


class NetworkReadError(RuntimeError):
    pass


class RulesChanged(RuntimeError):
    pass


def pull(records=None):
    previous=revision("HEAD");got=git("pull","--rebase","origin","main",check=False)
    base=revision("FETCH_HEAD")
    if got.returncode:
        conflicts={s.decode() for s in git("diff","--name-only","--diff-filter=U","-z").stdout.split(b"\0") if s}
        if not records or not conflicts or not conflicts.issubset({HANDOFF,*records}):
            message=(got.stdout+got.stderr).decode(errors="replace")
            if not conflicts and any(s in message.lower() for s in (
                    "could not resolve host","connection timed out","connection reset","remote end hung up",
                    "couldn't connect","failed to connect","requested url returned error: 5",
                    "http 502","http 503","http 504","tls connection was non-properly terminated")):
                raise NetworkReadError(message)
            raise RuntimeError(message)
    print(git("diff",previous,base,"--","README.md",TOPIC+"/README.md").stdout.decode(errors="replace"),flush=True)
    try:
        check_rules(previous,base)
    except RuntimeError as exc:
        if str(exc).startswith("Changed README at "):
            raise RulesChanged(str(exc)) from exc
        raise
    if got.returncode:
        for name in conflicts:
            body=blob_at(base,HANDOFF) if name==HANDOFF else records[name]
            if name!=HANDOFF and optional_blob(base,name)!=body:
                raise ValueError("different remote run conclusion")
            Path(name).parent.mkdir(exist_ok=True,parents=True);Path(name).write_bytes(body)
            git("add","--",name)
        rc=git("diff","--cached","--quiet",check=False).returncode
        if rc not in (0,1):
            raise RuntimeError("rebased index inspection")
        git("rebase","--continue" if rc else "--skip")
    return base


def checked_small(path):
    data=path.read_bytes()
    if len(data)>=100000:
        raise ValueError("independent branch exceeded small result limit")
    return data


def supervise(tdir):
    base=pull()
    trigger=os.environ["GITHUB_SHA"]
    frozen=tdir/"frozen";frozen.mkdir(exist_ok=True)
    ids={}
    for name in NAMES:
        body=blob_at(trigger,HERE+name);(frozen/name).write_bytes(body)
        ids[name]=[len(body),sha(body)]
    env=dict(os.environ,R758_SOURCE_COMMIT=trigger,R758_RULES_COMMIT=base)
    env.pop("GITHUB_TOKEN",None)
    active={};status={}
    for mode in ("outer_locked","free_end"):
        for side in (-1,1):
            key=mode+("-minus" if side<0 else "-plus")
            cmd=[sys.executable,"-u",str(frozen/"solve_r758_curved_crown_middle_annuli.py"),"--mode",mode,
                 "--side",str(side),"--folder",str(tdir/key),"--report",str(tdir/(key+".json"))]
            proc=subprocess.Popen(cmd,env=env)
            active[key]=proc
            print("R758 frozen source",trigger,"separate rules HEAD",base,"started",key,"PID",proc.pid,flush=True)
    next_pull=time.monotonic()+2700
    while active:
        for key,proc in list(active.items()):
            rc=proc.poll()
            if rc is not None:
                status[key]=rc;active.pop(key);print("R758 natural return",key,rc,flush=True)
        if active and time.monotonic()>=next_pull:
            try:
                pull();next_pull=time.monotonic()+2700
            except NetworkReadError as exc:
                print("R758 transient network read",str(exc),flush=True);next_pull=time.monotonic()+60
            except Exception:
                # A changed rule cannot authorize continuing this older source.
                # Keep existing outputs, identify each still-live PID and propagate the failure.
                for name,proc in active.items():
                    print("R758 stopping old source",name,proc.pid,flush=True);proc.terminate()
                for proc in active.values():
                    proc.wait()
                raise
        if active:
            time.sleep(10)
    (tdir/"branches.json").write_text(json.dumps({"base":trigger,"rules":base,"sources":ids,"status":status},sort_keys=True)+"\n")
    return status


def collect(tdir):
    meta=json.loads((tdir/"branches.json").read_bytes());records={};branches={}
    run,attempt=os.environ["GITHUB_RUN_ID"],os.environ["GITHUB_RUN_ATTEMPT"]
    prefix=TOPIC+"/notes/r758-curved-crown-"+run+"-"+attempt
    for key,rc in sorted(meta["status"].items()):
        if rc:
            branches[key]={"exit":rc};continue
        body=checked_small(tdir/(key+".json"));rep=json.loads(body)
        if (rep["run"],rep["attempt"],rep["source_commit"])!=(run,attempt,meta["base"]):
            raise ValueError("different branch run or source")
        name=prefix+"-"+key+".json";records[name]=body
        print("R758_COMPLETE_BRANCH_BEGIN",key,flush=True)
        print(body.decode(),end="");print("R758_COMPLETE_BRANCH_END",key,flush=True)
        last=rep["rows"][-1]["independent_grid"]
        branches[key]={"exit":rc,"file":Path(name).name,"bytes":len(body),"sha256":sha(body),
            "final_independent_chart_max_metric":max(q[2] for q in last.values()),
            "final_independent_chart_max_abs_principal":max(q[3] for q in last.values()),
            "final_independent_chart_min_support":min(q[4] for q in last.values()),
            "last_tracked_max_chord_minus_initial_path":rep["cap_radial_path_prices"][-1][0][-1]}
    index={"schema":"R758-four-complete-curved-crown-physical-fit-processes-v1","run":run,"attempt":attempt,
        "source_commit":meta["base"],"rules_read_commit":meta["rules"],"trigger_commit":os.environ["GITHUB_SHA"],"sources":meta["sources"],
        "branches":branches,"scope":"Each branch is independently fitted on its complete actual half. The two signed halves of either mode agree on their original central overlap. Raw coefficient words are runner-only and completely regenerated from the listed sources."}
    idxname=prefix+"-index.json";records[idxname]=(json.dumps(index,separators=(",",":"),sort_keys=True)+"\n").encode()
    print("R758_COMPLETE_INDEX",records[idxname].decode(),flush=True)
    return records,idxname


def marker(old,base,name):
    lines=old.splitlines(keepends=True)
    if sum(l.startswith(MARK) for l in lines)>1:
        raise ValueError("duplicate R758 marker")
    retain=b"".join(l for l in lines if not l.startswith(MARK))
    if retain and not retain.endswith(b"\n"):
        retain+=b"\n"
    for label in ("R758 [双弯帽四项实际拟合](notes/"+Path(name).name+") ","R758 "):
        new=retain+MARK+(label+"双README真pull "+base+"\n").encode()
        if len(new)<10000:
            return new
    return None


def publish(records,index):
    git("config","user.name","math-research Actions")
    git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
    while True:
        base=pull(records);remote=blob_at(base,HANDOFF);h=marker(remote,base,index)
        if h is None:
            print("R758 waiting for handoff space",flush=True);time.sleep(15);continue
        total=complete_tree_bytes(revision(base+":"+TOPIC))+len(h)-len(remote)
        for name,body in records.items():
            old=optional_blob(base,name)
            if old not in (None,body):
                raise ValueError("different remote branch at same run")
            total+=len(body)-len(old or b"")
        print("R758 checked remote bytes including four logical fits",total,base,flush=True)
        if total>LIMIT:
            time.sleep(15);continue
        local=revision("HEAD")!=base
        if local:
            changed=set(git("diff","--name-only",base,"HEAD").stdout.decode().splitlines())
            if not changed.issubset({HANDOFF,*records}) or git("rev-list","--count",base+"..HEAD").stdout.strip()!=b"1":
                raise ValueError("unrelated local commits")
        for name,body in {HANDOFF:h,**records}.items():
            Path(name).parent.mkdir(exist_ok=True,parents=True);Path(name).write_bytes(body)
        git("add","--",HANDOFF,*records)
        rc=git("diff","--cached","--quiet",check=False).returncode
        if rc==1:
            if local:
                git("commit","--amend","--no-edit")
            else:
                git("commit","-m","Publish four complete R758 physical fits on the original curved crown metric")
        elif rc:
            raise RuntimeError("index inspection")
        elif not local:
            return
        p=git("-c","credential.helper=","-c","credential.helper="+CREDENTIAL,"push","origin","HEAD:refs/heads/main",check=False)
        if not p.returncode:
            print("R758 published",revision("HEAD"),index,flush=True);return
        msg=(p.stdout+p.stderr).decode(errors="replace")
        if not any(s in msg for s in ("non-fast-forward","fetch first","cannot lock ref","remote ref updated",
                                       "failed to update ref","stale info")):
            raise RuntimeError(msg)
        print("Remote advanced; ordinary rebase and push retry",flush=True)


if __name__=="__main__":
    arg=argparse.ArgumentParser(description=__doc__)
    arg.add_argument("mode",choices=("sync","run","publish"));cmd=arg.parse_args().mode
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise RuntimeError("public project Actions required")
    os.chdir(os.environ["GITHUB_WORKSPACE"]);tmp=Path(os.environ["RUNNER_TEMP"])/"r758-whole-four"
    if cmd=="sync":
        pull()
    elif cmd=="run":
        tmp.mkdir(exist_ok=True);supervise(tmp)
    else:
        rec,idx=collect(tmp);publish(rec,idx)
        if any(json.loads(rec[idx])["branches"][b]["exit"] for b in json.loads(rec[idx])["branches"]):
            sys.exit("at least one original process returned nonzero; all recorded")
