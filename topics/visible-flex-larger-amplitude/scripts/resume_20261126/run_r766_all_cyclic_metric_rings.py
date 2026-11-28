#!/usr/bin/env python3
"""Run four independent complete R766 physical fits, supervise real pulls and publish their small conclusions."""
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
       "r758_curved_outer_collars_and_fixed_elliptical_crowns.py","r760_cartesian_curved_crown_and_lower_rate_walls.py",
       "r764_corrugated_pre_roll_and_movable_complete_caps.py","solve_r764_corrugated_whole_sphere.py",
       "r766_positive_boundary_curvature_and_exact_signed_ribbons.py","solve_r766_cyclic_pre_rolls_and_closed_caps.py",
       "publish_r734_exact_conclusion.py","run_r766_all_cyclic_metric_rings.py")
MARK=b"<!--r766-publish-->"


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
    env=dict(os.environ,R766_SOURCE_COMMIT=trigger,R766_RULES_COMMIT=base)
    env.pop("GITHUB_TOKEN",None)
    active={};status={}
    for mode in ("forward","alternating"):
        for e in (.13,.14):
            key=mode+("-130" if e==.13 else "-140")
            cmd=[sys.executable,"-u",str(frozen/"solve_r766_cyclic_pre_rolls_and_closed_caps.py"),"--pattern",mode,
                 "--retreat",str(e),"--folder",str(tdir/key)]
            proc=subprocess.Popen(cmd,env=env)
            active[key]=proc
            print("R766 frozen source",trigger,"separate rules HEAD",base,"started",key,"PID",proc.pid,flush=True)
    next_pull=time.monotonic()+2700
    while active:
        for key,proc in list(active.items()):
            rc=proc.poll()
            if rc is not None:
                status[key]=rc;active.pop(key);print("R766 natural return",key,rc,flush=True)
        if active and time.monotonic()>=next_pull:
            try:
                pull();next_pull=time.monotonic()+2700
            except NetworkReadError as exc:
                print("R766 transient network read",str(exc),flush=True);next_pull=time.monotonic()+60
            except Exception:
                # A changed rule cannot authorize continuing this older source.
                # Keep existing outputs, identify each still-live PID and propagate the failure.
                for name,proc in active.items():
                    print("R766 stopping old source",name,proc.pid,flush=True);proc.terminate()
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
    prefix=TOPIC+"/notes/r766-cyclic-ring-"+run+"-"+attempt
    for key,rc in sorted(meta["status"].items()):
        stages={}
        for lev in range(3):
            pair={}
            for label in ("rings","surface"):
                file=tdir/key/f"stage-{lev}-{label}.json"
                if not file.exists():
                    if not rc:
                        raise ValueError("zero physical return without its scientific resolution stage")
                    continue
                body=checked_small(file);rep=json.loads(body)
                if (rep["run"],rep["attempt"],rep["source_commit"],rep["level"],rep["experiment"])!=(run,attempt,meta["base"],lev,label):
                    raise ValueError("different resolution run or source")
                name=prefix+"-"+key+f"-level-{lev}-{label}.json";records[name]=body
                print("R766_COMPLETE_EXPERIMENT_BEGIN",key,lev,label,flush=True);print(body.decode(),end="")
                print("R766_COMPLETE_EXPERIMENT_END",key,lev,label,flush=True)
                info={"file":Path(name).name,"bytes":len(body),"sha256":sha(body),"phases":len(rep["rows"])}
                last=rep["rows"][-1][-1]
                if label=="rings":
                    info["last_max_three_edge_prices"]={k:r["maximum_squared_edge_prices"] for k,r in last.items()}
                    info["last_cartesian_fallback"]={k:r["cartesian_fallback"] for k,r in last.items()}
                else:
                    vals=last["charts"].values()
                    info.update(last_metric=max(x[1] for x in vals),last_abs_principal=max(x[5] for x in vals),
                        last_min_support=min(x[6] for x in vals),last_sampled_held=last["minimum_sampled_held_witness"])
                pair[label]=info
            stages[lev]=pair
        branches[key]={"exit":rc,"levels":stages}
    index={"schema":"R766-four-natural-whole-spheres-and-complete-resolution-stages-v1","run":run,"attempt":attempt,
        "source_commit":meta["base"],"rules_read_commit":meta["rules"],"trigger_commit":os.environ["GITHUB_SHA"],"sources":meta["sources"],
        "branches":branches,"scope":"Each whole joint signed sphere has one fixed corrugated initial metric, three independently audited resolutions and all registered phases. Coefficients remain on the runner and regenerate from these complete sources."}
    idxname=prefix+"-index.json";records[idxname]=(json.dumps(index,separators=(",",":"),sort_keys=True)+"\n").encode()
    print("R766_COMPLETE_INDEX",records[idxname].decode(),flush=True)
    return records,idxname


def marker(old,base,name):
    lines=old.splitlines(keepends=True)
    if sum(l.startswith(MARK) for l in lines)>1:
        raise ValueError("duplicate R766 marker")
    retain=b"".join(l for l in lines if not l.startswith(MARK))
    if retain and not retain.endswith(b"\n"):
        retain+=b"\n"
    for label in ("R766 [双卷整周保边与整壳实际](notes/"+Path(name).name+") ","R766 "):
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
            print("R766 waiting for handoff space",flush=True);time.sleep(15);continue
        total=complete_tree_bytes(revision(base+":"+TOPIC))+len(h)-len(remote)
        for name,body in records.items():
            old=optional_blob(base,name)
            if old not in (None,body):
                raise ValueError("different remote branch at same run")
            total+=len(body)-len(old or b"")
        print("R766 checked remote bytes including four logical fits",total,base,flush=True)
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
                git("commit","-m","Publish all R766 whole surface resolution stages with full cyclic edge constraints and a continuous closed audit")
        elif rc:
            raise RuntimeError("index inspection")
        elif not local:
            return
        p=git("-c","credential.helper=","-c","credential.helper="+CREDENTIAL,"push","origin","HEAD:refs/heads/main",check=False)
        if not p.returncode:
            print("R766 published",revision("HEAD"),index,flush=True);return
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
    os.chdir(os.environ["GITHUB_WORKSPACE"]);tmp=Path(os.environ["RUNNER_TEMP"])/"r766-whole-four"
    if cmd=="sync":
        pull()
    elif cmd=="run":
        tmp.mkdir(exist_ok=True);supervise(tmp)
    else:
        rec,idx=collect(tmp);publish(rec,idx)
        if any(json.loads(rec[idx])["branches"][b]["exit"] for b in json.loads(rec[idx])["branches"]):
            sys.exit("at least one original process returned nonzero; all recorded")
