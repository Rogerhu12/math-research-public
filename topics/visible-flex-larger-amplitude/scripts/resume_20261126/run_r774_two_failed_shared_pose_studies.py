#!/usr/bin/env python3
"""Retry both R774 whole fits on their complete original budgets; retain the already successful independent studies."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from datetime import datetime,timezone
from publish_r734_exact_conclusion import (
    CREDENTIAL,HANDOFF,LIMIT,REPOSITORY,TOPIC,blob_at,check_rules,complete_tree_bytes,
    git,optional_blob,revision,sha,
)

HERE=TOPIC+"/scripts/resume_20261126/"
NAMES=("r740_rolled_disk_seed.py","r742_tilted_disk_two_jets.py","r744_extruded_closed_two_jets.py",
       "r754_coherent_mirror_bowed_walls_two_jets.py","r756_return_elbows_preloaded_exact_rolls.py",
       "r758_curved_outer_collars_and_fixed_elliptical_crowns.py","r760_cartesian_curved_crown_and_lower_rate_walls.py",
       "r764_corrugated_pre_roll_and_movable_complete_caps.py","solve_r764_corrugated_whole_sphere.py",
       "r766_positive_boundary_curvature_and_exact_signed_ribbons.py","r769_closed_turn_redistribution_and_complete_rolls.py",
       "r769_full_unit_meridian_shooting.py","solve_r769_complete_meridian_spheres.py",
       "r771_convex_complete_meridian_coordinates.py",
       "r774_common_left_body_and_complete_caps.py","solve_r774_shared_pose_complete_spheres_retry.py",
       "publish_r734_exact_conclusion.py","run_r774_two_failed_shared_pose_studies.py")
MARK=b"<!--r774-publish-->"


class NetworkReadError(RuntimeError):
    pass


class RulesChanged(RuntimeError):
    pass


def pull(records,ledger):
    previous=revision("HEAD");got=git("pull","--rebase","origin","main",check=False)
    base=revision("FETCH_HEAD")
    if got.returncode:
        conflicts={s.decode() for s in git("diff","--name-only","--diff-filter=U","-z").stdout.split(b"\0") if s}
        if not conflicts or not conflicts.issubset({HANDOFF,ledger,*records}):
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
            body=(optional_blob(base,name) or b"") if name in (HANDOFF,ledger) else records[name]
            if name not in (HANDOFF,ledger) and optional_blob(base,name)!=body:
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
    base=publish({},None,"freeze",{})
    trigger=os.environ["GITHUB_SHA"]
    frozen=tdir/"frozen";frozen.mkdir(exist_ok=True)
    ids={}
    for name in NAMES:
        body=blob_at(trigger,HERE+name);(frozen/name).write_bytes(body)
        ids[name]=[len(body),sha(body)]
    env=dict(os.environ,R774_SOURCE_COMMIT=trigger,R774_RULES_COMMIT=base)
    env.pop("GITHUB_TOKEN",None)
    active={};status={}
    for key in ("left","common"):
        program="solve_r774_shared_pose_complete_spheres_retry.py";options=["--mode",key]
        out=tdir/key;out.mkdir(parents=True,exist_ok=True)
        cmd=[sys.executable,"-u",str(frozen/program),*options,"--folder",str(out)]
        proc=subprocess.Popen(cmd,env=env);active[key]=proc
        print("R774 frozen source",trigger,"separate rules HEAD",base,"started",key,"PID",proc.pid,flush=True)
    next_pull=time.monotonic()+2700
    while active:
        for key,proc in list(active.items()):
            rc=proc.poll()
            if rc is not None:
                status[key]=rc;active.pop(key);print("R774 natural return",key,rc,flush=True)
        if active and time.monotonic()>=next_pull:
            try:
                publish({},None,"periodic",{k:p.pid for k,p in active.items()});next_pull=time.monotonic()+2700
            except NetworkReadError as exc:
                print("R774 transient network read",str(exc),flush=True);next_pull=time.monotonic()+60
            except Exception:
                # A changed rule cannot authorize continuing this older source.
                # Keep existing outputs, identify each still-live PID and propagate the failure.
                for name,proc in active.items():
                    print("R774 stopping old source",name,proc.pid,flush=True);proc.terminate()
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
    prefix=TOPIC+"/notes/r774-shared-pose-retry-"+run+"-"+attempt
    for key,rc in sorted(meta["status"].items()):
        stages={};geometries={}
        for lev in range(3):
            gi=tdir/key/f"geometry-{lev}.json"
            if gi.exists():
                body=checked_small(gi);g=json.loads(body)
                if (g["run"],g["attempt"],g["source_commit"],g["level"])!=(run,attempt,meta["base"],lev):
                    raise ValueError("different complete construction report")
                name=prefix+"-"+key+f"-level-{lev}-geometry.json";records[name]=body
                print("R774_COMPLETE_GEOMETRY_BEGIN",key,lev,flush=True);print(body.decode(),end="")
                print("R774_COMPLETE_GEOMETRY_END",key,lev,flush=True)
                last=g["rows"][-1];vals=last["all_charts"].values()
                geometries[lev]={"file":Path(name).name,"bytes":len(body),"sha256":sha(body),"phases":len(g["rows"]),
                    "last_metric":max(q[1] for q in vals),"last_principal":max(q[5] for q in vals),
                    "last_rigid_cap_centroid_excess":last["construction"]["general_rigid_cap_centroid"][-1]}
            elif not rc:
                raise ValueError("zero natural return without its geometry experiment")
            file=tdir/key/f"stage-{lev}.json"
            if not file.exists():
                if not rc:
                    raise ValueError("zero physical return without its own resolution")
                continue
            body=checked_small(file);rep=json.loads(body)
            if (rep["run"],rep["attempt"],rep["source_commit"],rep["level"])!=(run,attempt,meta["base"],lev):
                raise ValueError("different resolution run or source")
            name=prefix+"-"+key+f"-level-{lev}.json";records[name]=body
            print("R774_COMPLETE_RESOLUTION_BEGIN",key,lev,flush=True);print(body.decode(),end="")
            print("R774_COMPLETE_RESOLUTION_END",key,lev,flush=True)
            last=rep["fitted"][-1]["independent"];values=last["charts"].values()
            stages[lev]={"file":Path(name).name,"bytes":len(body),"sha256":sha(body),
                "last_phase_max_metric":max(q[2] for q in values),
                "last_phase_max_abs_principal":max(q[3] for q in values),
                "last_phase_min_support":min(q[4] for q in values),
                "last_phase_sampled_held":last["held_witness_min_sample"],
                "last_phase_max_preband_chord_minus_path":last["max_preband_endpoint_chord_minus_initial_path"],
                "last_phase_signed_volumes":rep["fitted"][-1]["volumes"]}
        branches[key]={"exit":rc,"levels":stages,"geometries":geometries}
    index={"schema":"R774-two-complete-fits-retry-and-original-successful-studies-v1","run":run,"attempt":attempt,
        "source_commit":meta["base"],"rules_read_commit":meta["rules"],"trigger_commit":os.environ["GITHUB_SHA"],"sources":meta["sources"],
        "branches":branches,"scope":"Each whole joint signed sphere has one fixed corrugated initial metric, three independently audited resolutions and all registered phases. Coefficients remain on the runner and regenerate from these complete sources."}
    index["original_source"]="30fa2dccd9e30806d4f4b13347dc64aefad2ca02"
    index["original_conclusion_commit"]="1362734f69f11a8eade488e47de0006fe8763823"
    index["original_completed_independent_studies"]=[["r774-shared-pose-whole-46174642286-1-fold.json",45418,"2c9f81f91553755efa7b5f67a0ad879ba440c454757aad6f384041c8fc10df23","5ca1fe833f8a157d75148e2b56c0164bb120f657"],["r774-shared-pose-whole-46174642286-1-interval.json",22171,"b4ac296b6e1d62e94d52a747050721dd0877b34815de40cf7abbe96010129979","649c1e1310568bc4ddceb5d4678e4a6061eb9103"]]
    index["original_two_failed_exits"]={"left":1,"common":1}
    idxname=prefix+"-index.json";records[idxname]=(json.dumps(index,separators=(",",":"),sort_keys=True)+"\n").encode()
    print("R774_COMPLETE_INDEX",records[idxname].decode(),flush=True)
    return records,idxname


def marker(old,base,index,ledger):
    lines=old.splitlines(keepends=True)
    if sum(l.startswith(MARK) for l in lines)>1:
        raise ValueError("duplicate R774 marker")
    retain=b"".join(l for l in lines if not l.startswith(MARK))
    if retain and not retain.endswith(b"\n"):
        retain+=b"\n"
    note=Path(ledger).name
    target=("[全部返回](notes/"+Path(index).name+") ") if index else ""
    for label in (target+"[每次双README真读](notes/"+note+") ","[历次真读](notes/"+note+") "):
        new=retain+MARK+("R774 "+label+base+"\n").encode()
        if len(new)<10000:
            return new
    return None


def publish(final_records,index,stage,pids):
    git("config","user.name","math-research Actions")
    git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
    run=os.environ["GITHUB_RUN_ID"];attempt=os.environ["GITHUB_RUN_ATTEMPT"]
    ledger=TOPIC+"/notes/r774-shared-pose-retry-"+run+"-"+attempt+"-reads.json"
    local_journal=Path(os.environ["RUNNER_TEMP"])/("r774-retry-reads-"+run+"-"+attempt+".jsonl")
    while True:
        base=pull(final_records,ledger)
        entry={"ordinal":0,"commit":base,"utc":datetime.now(timezone.utc).isoformat(),"stage":stage,
               "live_pids":dict(sorted(pids.items())),"rules":"both exact SHA256 and actual git diff read"}
        entries=[json.loads(x) for x in local_journal.read_bytes().splitlines()] if local_journal.exists() else []
        entry["ordinal"]=len(entries)+1
        with local_journal.open("ab") as log:
            log.write((json.dumps(entry,separators=(",",":"))+"\n").encode())
        entries.append(entry)
        oldledger=optional_blob(base,ledger)
        if oldledger:
            pushed=json.loads(oldledger)["checked_pulls"]
            if pushed!=entries[:len(pushed)]:
                raise RuntimeError("different published journal at the same run/attempt")
        journal={"run":run,"attempt":attempt,"source_commit":os.environ["GITHUB_SHA"],
                 "checked_pulls":entries}
        records={**final_records,ledger:(json.dumps(journal,separators=(",",":"))+"\n").encode()}
        if len(records[ledger])>=100000:
            raise ValueError("rules journal exceeds individual report limit")
        remote=blob_at(base,HANDOFF);h=marker(remote,base,index,ledger)
        if h is None:
            print("R774 waiting for handoff space",flush=True);time.sleep(15);continue
        total=complete_tree_bytes(revision(base+":"+TOPIC))+len(h)-len(remote)
        for name,body in records.items():
            old=optional_blob(base,name)
            if name!=ledger and old not in (None,body):
                raise ValueError("different remote branch at same run")
            total+=len(body)-len(old or b"")
        print("R774 checked remote bytes including four logical fits",total,base,flush=True)
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
                git("commit","-m","Record R774 "+stage+" and every actual checked rules pull")
        elif rc:
            raise RuntimeError("index inspection")
        elif not local:
            return base
        p=git("-c","credential.helper=","-c","credential.helper="+CREDENTIAL,"push","origin","HEAD:refs/heads/main",check=False)
        if not p.returncode:
            print("R774 published",revision("HEAD"),index or ledger,flush=True);return base
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
    os.chdir(os.environ["GITHUB_WORKSPACE"]);tmp=Path(os.environ["RUNNER_TEMP"])/"r774-retry-two"
    if cmd=="sync":
        publish({},None,"bootstrap",{})
    elif cmd=="run":
        tmp.mkdir(exist_ok=True);supervise(tmp)
    else:
        rec,idx=collect(tmp);publish(rec,idx,"complete",{})
        if any(json.loads(rec[idx])["branches"][b]["exit"] for b in json.loads(rec[idx])["branches"]):
            sys.exit("at least one original process returned nonzero; all recorded")
