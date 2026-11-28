#!/usr/bin/env python3
"""Run four independent complete R787 physical fits, supervise real pulls and publish their small conclusions."""
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
NAMES=(
    "r740_rolled_disk_seed.py",
    "r742_tilted_disk_two_jets.py",
    "r744_extruded_closed_two_jets.py",
    "r754_coherent_mirror_bowed_walls_two_jets.py",
    "r756_return_elbows_preloaded_exact_rolls.py",
    "r758_curved_outer_collars_and_fixed_elliptical_crowns.py",
    "r760_cartesian_curved_crown_and_lower_rate_walls.py",
    "r764_corrugated_pre_roll_and_movable_complete_caps.py",
    "solve_r764_corrugated_whole_sphere.py",
    "r766_positive_boundary_curvature_and_exact_signed_ribbons.py",
    "r769_closed_turn_redistribution_and_complete_rolls.py",
    "r769_full_unit_meridian_shooting.py",
    "solve_r769_complete_meridian_spheres.py",
    "r771_convex_complete_meridian_coordinates.py",
    "r774_common_left_body_and_complete_caps.py",
    "solve_r774_shared_pose_complete_spheres.py",
    "r777_bent_complete_caps_and_true_terminal_collars.py",
    "publish_r734_exact_conclusion.py",
    "r780_exact_bent_caps_and_closed_spatially_shifted_center.py",
    "r780_complete_ring_arclength_and_physical_jets.py",
    "fit_r780_two_remaining_complete_roll_components.py",
    "solve_r780_exact_crowns_and_normalized_whole_rolls.py",
    "r787_long_left_wall_and_complete_initial_disks.py",
    "r787_preloaded_two_complete_caps_and_four_returning_meridians.py",
    "r787_complete_material_graph_paths.py",
    "r787_complete_cartesian_cap_basis_pullback.py",
    "solve_r787_preloaded_long_wall_full_physical_families.py",
    "run_r787_preloaded_long_wall_whole_fits.py",
)
MARK=b"<!--r787-publish-->"


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
        raise ValueError("independent stage exceeded small result limit")
    return data


def supervise(tdir):
    base=publish({},None,"freeze",{})
    trigger=os.environ["GITHUB_SHA"]
    frozen=tdir/"frozen";frozen.mkdir(exist_ok=True)
    ids={}
    for name in NAMES:
        body=blob_at(trigger,HERE+name);(frozen/name).write_bytes(body)
        ids[name]=[len(body),sha(body)]
    env=dict(os.environ,R787_SOURCE_COMMIT=trigger,R787_RULES_COMMIT=base)
    env.pop("GITHUB_TOKEN",None)
    active={};status={}
    for key in ("panels-gram","panels-shape","open-gram","open-shape"):
        program="solve_r787_preloaded_long_wall_full_physical_families.py"
        options=["--mode",key]
        out=tdir/key;out.mkdir(parents=True,exist_ok=True)
        cmd=[sys.executable,"-u",str(frozen/program),*options,"--folder",str(out)]
        proc=subprocess.Popen(cmd,env=env);active[key]=proc
        print("R787 frozen source",trigger,"separate rules HEAD",base,"started",key,"PID",proc.pid,flush=True)
    next_pull=time.monotonic()+2700
    while active:
        for key,proc in list(active.items()):
            rc=proc.poll()
            if rc is not None:
                status[key]=rc;active.pop(key);print("R787 natural return",key,rc,flush=True)
        if active and time.monotonic()>=next_pull:
            try:
                publish({},None,"periodic",{k:p.pid for k,p in active.items()});next_pull=time.monotonic()+2700
            except NetworkReadError as exc:
                print("R787 transient network read",str(exc),flush=True);next_pull=time.monotonic()+60
            except Exception:
                # A changed rule cannot authorize continuing this older source.
                # Keep existing outputs, identify each still-live PID and propagate the failure.
                for name,proc in active.items():
                    print("R787 stopping old source",name,proc.pid,flush=True);proc.terminate()
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
    prefix=TOPIC+"/notes/r787-preloaded-long-wall-fits-"+run+"-"+attempt
    for key,rc in sorted(meta["status"].items()):
        subs={}
        for level in range(3):
            for kind in ("geometry","stage"):
                file=tdir/key/f"{kind}-{level}.json"
                if not file.exists():
                    if not rc:
                        raise ValueError("zero natural return lacked own complete resolution")
                    continue
                body=checked_small(file);rep=json.loads(body)
                if (rep["run"],rep["attempt"],rep["source_commit"],rep["branch"],rep["level"])!=(run,attempt,meta["base"],key,level):
                    raise ValueError("different run, mode or resolution")
                name=prefix+"-"+key+f"-{kind}-{level}.json";records[name]=body
                print("R787_COMPLETE_RESOLUTION_BEGIN",kind,key,level,flush=True);print(body.decode(),end="")
                print("R787_COMPLETE_RESOLUTION_END",kind,key,level,flush=True)
                row=rep["rows"][-1]
                subs[f"{kind}-{level}"]={"file":Path(name).name,"bytes":len(body),"sha256":sha(body),
                    "phase_count":len(rep["rows"]),"last_phase":row["phase"],"last_metric":row["max_metric"],
                    "last_principal":row["max_principal"],"last_min_support":row["min_support"],
                    "last_relative_area":row["min_relative_area"],"last_signed_flux":row["volume"],
                    "last_held_sample":row["initial_witness_sampled_distance"],"last_chords":row["chords"],
                    "last_preband_endpoint_excess":row["maximum_pre_meridian_chord_minus_path"]}
        branches[key]={"exit":rc,"resolutions":subs}
    index={"schema":"R787-four-whole-families-and-all-returned-resolution-identities-v1",
        "run":run,"attempt":attempt,"source_commit":meta["base"],"rules_read_commit":meta["rules"],
        "trigger_commit":os.environ["GITHUB_SHA"],"sources":meta["sources"],"branches":branches,
        "scope":"Each independent stage retains all seven phases and six midpoints, all material charts and both physical ends. Native fit coefficients remain on runner and regenerate from the registered source."}
    idxname=prefix+"-index.json";records[idxname]=(json.dumps(index,separators=(",",":"),sort_keys=True)+"\n").encode()
    print("R787_COMPLETE_INDEX",records[idxname].decode(),flush=True)
    return records,idxname


def marker(old,base,index,ledger):
    lines=old.splitlines(keepends=True)
    if sum(l.startswith(MARK) for l in lines)>1:
        raise ValueError("duplicate R787 marker")
    retain=b"".join(l for l in lines if not l.startswith(MARK))
    if retain and not retain.endswith(b"\n"):
        retain+=b"\n"
    note=Path(ledger).name
    target=("[全部返回](notes/"+Path(index).name+") ") if index else ""
    for label in (target+"[每次双README真读](notes/"+note+") ","[历次真读](notes/"+note+") "):
        new=retain+MARK+("R787 "+label+base+"\n").encode()
        if len(new)<10000:
            return new
    return None


def publish(final_records,index,stage,pids):
    git("config","user.name","math-research Actions")
    git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
    run=os.environ["GITHUB_RUN_ID"];attempt=os.environ["GITHUB_RUN_ATTEMPT"]
    ledger=TOPIC+"/notes/r787-preloaded-long-wall-fits-"+run+"-"+attempt+"-reads.json"
    local_journal=Path(os.environ["RUNNER_TEMP"])/("r787-reads-"+run+"-"+attempt+".jsonl")
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
            print("R787 waiting for handoff space",flush=True);time.sleep(15);continue
        total=complete_tree_bytes(revision(base+":"+TOPIC))+len(h)-len(remote)
        for name,body in records.items():
            old=optional_blob(base,name)
            if name!=ledger and old not in (None,body):
                raise ValueError("different remote branch at same run")
            total+=len(body)-len(old or b"")
        print("R787 checked remote bytes including four logical fits",total,base,flush=True)
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
                git("commit","-m","Record R787 "+stage+" and every actual checked rules pull")
        elif rc:
            raise RuntimeError("index inspection")
        elif not local:
            return base
        p=git("-c","credential.helper=","-c","credential.helper="+CREDENTIAL,"push","origin","HEAD:refs/heads/main",check=False)
        if not p.returncode:
            print("R787 published",revision("HEAD"),index or ledger,flush=True);return base
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
    os.chdir(os.environ["GITHUB_WORKSPACE"]);tmp=Path(os.environ["RUNNER_TEMP"])/"r787-whole-four"
    if cmd=="sync":
        publish({},None,"bootstrap",{})
    elif cmd=="run":
        tmp.mkdir(exist_ok=True);supervise(tmp)
    else:
        rec,idx=collect(tmp);publish(rec,idx,"complete",{})
        if any(json.loads(rec[idx])["branches"][b]["exit"] for b in json.loads(rec[idx])["branches"]):
            sys.exit("at least one original process returned nonzero; all recorded")
