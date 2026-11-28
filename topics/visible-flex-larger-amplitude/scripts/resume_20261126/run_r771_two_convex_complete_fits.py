#!/usr/bin/env python3
"""Run two independent complete R771 physical fits, supervise real pulls and publish their small conclusions."""
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
       "r766_positive_boundary_curvature_and_exact_signed_ribbons.py","r769_closed_turn_redistribution_and_complete_rolls.py",
       "r769_full_unit_meridian_shooting.py","solve_r769_complete_meridian_spheres.py",
       "r771_convex_complete_meridian_coordinates.py","r771_feasible_two_gram_angular_shapes.py","solve_r771_convex_complete_spheres.py",
       "publish_r734_exact_conclusion.py","run_r771_two_convex_complete_fits.py")
MARK=b"<!--r771-publish-->"


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
    env=dict(os.environ,R771_SOURCE_COMMIT=trigger,R771_RULES_COMMIT=base)
    env.pop("GITHUB_TOKEN",None)
    active={};status={}
    for e in (.30,.42):
        key="convex-"+str(round(e*1000))
        cmd=[sys.executable,"-u",str(frozen/"solve_r771_convex_complete_spheres.py"),
             "--response",str(e),"--folder",str(tdir/key)]
        proc=subprocess.Popen(cmd,env=env);active[key]=proc
        print("R771 frozen source",trigger,"separate rules HEAD",base,"started",key,"PID",proc.pid,flush=True)
    next_pull=time.monotonic()+2700
    while active:
        for key,proc in list(active.items()):
            rc=proc.poll()
            if rc is not None:
                status[key]=rc;active.pop(key);print("R771 natural return",key,rc,flush=True)
        if active and time.monotonic()>=next_pull:
            try:
                pull();next_pull=time.monotonic()+2700
            except NetworkReadError as exc:
                print("R771 transient network read",str(exc),flush=True);next_pull=time.monotonic()+60
            except Exception:
                # A changed rule cannot authorize continuing this older source.
                # Keep existing outputs, identify each still-live PID and propagate the failure.
                for name,proc in active.items():
                    print("R771 stopping old source",name,proc.pid,flush=True);proc.terminate()
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
    prefix=TOPIC+"/notes/r771-convex-meridian-"+run+"-"+attempt
    for key,rc in sorted(meta["status"].items()):
        stages={};geometries={};feasible={}
        for lev in range(3):
            fi=tdir/key/f"feasible-{lev}.json"
            if fi.exists():
                body=checked_small(fi);f=json.loads(body)
                if (f["run"],f["attempt"],f["source_commit"],f["level"])!=(run,attempt,meta["base"],lev):
                    raise ValueError("different constrained angular experiment")
                name=prefix+"-"+key+f"-level-{lev}-feasible.json";records[name]=body
                print("R771_COMPLETE_FEASIBLE_BEGIN",key,lev,flush=True);print(body.decode(),end="")
                print("R771_COMPLETE_FEASIBLE_END",key,lev,flush=True)
                feasible[lev]={"file":Path(name).name,"bytes":len(body),"sha256":sha(body),"phases":len(f["rows"]),
                    "last_face_angular_and_shear":f["rows"][-1]["final"]["face_max_abs_11_12"]}
            elif not rc:
                raise ValueError("zero natural return without its endpoint-preserving angular solve")
            gi=tdir/key/f"geometry-{lev}.json"
            if gi.exists():
                body=checked_small(gi);g=json.loads(body)
                if (g["run"],g["attempt"],g["source_commit"],g["level"])!=(run,attempt,meta["base"],lev):
                    raise ValueError("different complete construction report")
                name=prefix+"-"+key+f"-level-{lev}-geometry.json";records[name]=body
                print("R771_COMPLETE_GEOMETRY_BEGIN",key,lev,flush=True);print(body.decode(),end="")
                print("R771_COMPLETE_GEOMETRY_END",key,lev,flush=True)
                last=g["rows"][-1];vals=last["all_charts"].values()
                geometries[lev]={"file":Path(name).name,"bytes":len(body),"sha256":sha(body),"phases":len(g["rows"]),
                    "last_metric":max(q[1] for q in vals),"last_principal":max(q[5] for q in vals),
                    "last_preband_rigid_cap_test":last["construction"]["symmetric_rigid_cap_test"]}
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
            print("R771_COMPLETE_RESOLUTION_BEGIN",key,lev,flush=True);print(body.decode(),end="")
            print("R771_COMPLETE_RESOLUTION_END",key,lev,flush=True)
            last=rep["fitted"][-1]["independent"];values=last["charts"].values()
            stages[lev]={"file":Path(name).name,"bytes":len(body),"sha256":sha(body),
                "last_phase_max_metric":max(q[2] for q in values),
                "last_phase_max_abs_principal":max(q[3] for q in values),
                "last_phase_min_support":min(q[4] for q in values),
                "last_phase_sampled_held":last["held_witness_min_sample"],
                "last_phase_max_preband_chord_minus_path":last["max_preband_endpoint_chord_minus_initial_path"],
                "last_phase_signed_volumes":rep["fitted"][-1]["volumes"]}
        branches[key]={"exit":rc,"levels":stages,"geometries":geometries,"feasible":feasible}
    index={"schema":"R771-two-natural-whole-spheres-and-complete-resolution-stages-v1","run":run,"attempt":attempt,
        "source_commit":meta["base"],"rules_read_commit":meta["rules"],"trigger_commit":os.environ["GITHUB_SHA"],"sources":meta["sources"],
        "branches":branches,"scope":"Each whole joint signed sphere has one fixed corrugated initial metric, three independently audited resolutions and all registered phases. Coefficients remain on the runner and regenerate from these complete sources."}
    idxname=prefix+"-index.json";records[idxname]=(json.dumps(index,separators=(",",":"),sort_keys=True)+"\n").encode()
    print("R771_COMPLETE_INDEX",records[idxname].decode(),flush=True)
    return records,idxname


def marker(old,base,name):
    lines=old.splitlines(keepends=True)
    if sum(l.startswith(MARK) for l in lines)>1:
        raise ValueError("duplicate R771 marker")
    retain=b"".join(l for l in lines if not l.startswith(MARK))
    if retain and not retain.endswith(b"\n"):
        retain+=b"\n"
    for label in ("R771 [全子午凸坐标两整球六层实际](notes/"+Path(name).name+") ","R771 "):
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
            print("R771 waiting for handoff space",flush=True);time.sleep(15);continue
        total=complete_tree_bytes(revision(base+":"+TOPIC))+len(h)-len(remote)
        for name,body in records.items():
            old=optional_blob(base,name)
            if old not in (None,body):
                raise ValueError("different remote branch at same run")
            total+=len(body)-len(old or b"")
        print("R771 checked remote bytes including two logical fits",total,base,flush=True)
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
                git("commit","-m","Publish all R771 whole surface resolution stages on the corrugated initial metric")
        elif rc:
            raise RuntimeError("index inspection")
        elif not local:
            return
        p=git("-c","credential.helper=","-c","credential.helper="+CREDENTIAL,"push","origin","HEAD:refs/heads/main",check=False)
        if not p.returncode:
            print("R771 published",revision("HEAD"),index,flush=True);return
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
    os.chdir(os.environ["GITHUB_WORKSPACE"]);tmp=Path(os.environ["RUNNER_TEMP"])/"r771-whole-two"
    if cmd=="sync":
        pull()
    elif cmd=="run":
        tmp.mkdir(exist_ok=True);supervise(tmp)
    else:
        rec,idx=collect(tmp);publish(rec,idx)
        if any(json.loads(rec[idx])["branches"][b]["exit"] for b in json.loads(rec[idx])["branches"]):
            sys.exit("at least one original process returned nonzero; all recorded")
