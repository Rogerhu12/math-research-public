#!/usr/bin/env python3
"""Replay the whole original Run39, then propagate its selected material fields on their true charts."""
import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback

import numpy as np

import bent_body_killing as parent
from bent_body_flow_field import ClosedAtlas, Field
from bent_body_flow_track import load_field, seeds, process_point


def identity(path):
    path=Path(path)
    return {"name":path.name,"bytes":path.stat().st_size,"sha256":parent.filehash(path)}


def compare(a,b):
    keys=("stage","kind","design","configuration","physical_count","material_count",
          "physical_sha256","material_sha256","point_sha256","npz_bytes","npz_sha256")
    return {k:{"original":a.get(k),"replay":b.get(k)} for k in keys if a.get(k)!=b.get(k)}


def main():
    parser=argparse.ArgumentParser()
    for k in ("params","parent-params","geometry-source","parent-observation","out"):
        parser.add_argument("--"+k,required=True)
    args=parser.parse_args()
    p=json.loads(Path(args.params).read_text());pp=json.loads(Path(args.parent_params).read_text())
    out=Path(args.out);out.mkdir(exist_ok=True,parents=True)
    original_file=identity(args.parent_observation)
    if any(original_file.get(k)!=v for k,v in p["original_observation"].items()
           if k in ("bytes","sha256")):
        raise ValueError("Run39 original terminal public observation identity changed")
    original=json.loads(Path(args.parent_observation).read_text())
    archived=original["scientific_summary"];original_science=archived["complete_small_json"]
    source=Path(args.geometry_source).resolve()
    sys.path.insert(0,str(source.parent));src=importlib.import_module(source.stem)
    start=time.monotonic()
    meta={"schema":"run39b-actual-closed-chart-finite-flow/v1","status":"parent_replay_start",
          "scope":"Three original-source target/candidate fields; complete finite time 0 through pi on named material points, with full two-dimensional variations. Spatial sample and numerical integrations only.",
          "original_run":original["run"],"original_attempt":original["attempt"],"original_child_returncode":original["child_returncode"],
          "original_source_commit":original["source_commit"],"original_observation":original_file,
          "original_runner_summary_identity":archived["file"],"actual_replay":None,"stages":[],
          "full_result":None,"certificate":None}
    def save():
        meta["elapsed_seconds"]=time.monotonic()-start
        parent.dump(out/"summary.json",meta)
    save()
    try:
        directory=out/"parent-full-replay";directory.mkdir()
        cmd=[sys.executable,"-u",str(Path(parent.__file__).resolve()),"--params",str(Path(args.parent_params).resolve()),
             "--geometry-source",str(source),"--out",str(directory)]
        began=time.monotonic();meta["actual_replay"]={"argv":cmd,"returncode":None,"elapsed_seconds":None,
            "scope":"Complete original eleven stages and all budgets; original independent terminal record stays separate."}
        save()
        replay_process=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        meta["actual_replay"]["pid"]=replay_process.pid;save()
        with (directory/"console.log").open("w") as stream:
            for line in replay_process.stdout:
                stream.write(line);stream.flush();print(line,end="",flush=True)
                try: msg=json.loads(line)
                except (TypeError,ValueError):continue
                if msg.get("event")=="stage":
                    meta["actual_replay"]["last_stage_scalar"]=msg;save()
        rc=replay_process.wait()
        replay_info=meta["actual_replay"]
        replay_info.update(returncode=rc,elapsed_seconds=time.monotonic()-began,
                           console=identity(directory/"console.log"))
        returned=directory/"summary.json"
        if returned.exists():
            replay_info["summary"]=identity(returned)
            replay=json.loads(returned.read_text())
            replay_info["status"]=replay.get("status")
            if "exception" in replay:replay_info["exception"]=replay["exception"]
        save()
        if rc or replay_info.get("status")!="completed_whole_closed_body_two_material_refinements":
            raise ValueError("complete parent science did not return its normal eleven-stage result")
        orig=original_science["stages"];new=replay["stages"]
        if len(orig)!=11 or len(new)!=11:
            raise ValueError("the recorded original or replay lacks a whole stage")
        differences={str(i):v for i,(a,b) in enumerate(zip(orig,new)) if (v:=compare(a,b))}
        replay_info.update(stage_by_stage_identity_differences=differences,all_11_exact=not bool(differences),
                           original_frozen=replay_target_id(original_science),replay_frozen=replay_target_id(replay))
        target=replay["frozen_target"];rr=new[target["source_stage"]];zt,_=load_field(directory,rr)
        stage_ids=[rr["stage"]]+[r["stage"] for r in new if r["kind"]=="frozen_metric_actual_shape_and_vector"]
        if len(stage_ids)!=3 or len(set(stage_ids))!=3:
            raise ValueError("one complete selected source and both different fixed refinements are required")
        meta["status"]="integrating_actual_selected_and_both_fixed_fields";save()
        for i in stage_ids:
            r=new[i];z,x=load_field(directory,r)
            if r["design"]!=rr["design"] or (i!=rr["stage"] and
                    r["fixed_target_source_physical_sha256"]!=target["source_physical_sha256"]):
                raise ValueError("replayed fixed candidate and replayed target differ in underlying geometry or chart")
            domain=ClosedAtlas(src,r["design"],pp);f=Field(domain,r,z,x)
            addresses=seeds(f,r,p)
            tied=(replay_info["original_frozen"]==replay_info["replay_frozen"] and
                  str(i) not in differences and str(rr["stage"]) not in differences)
            entry={"stage":i,"point_sha256":r["point_sha256"],"physical_sha256":r["physical_sha256"],
                   "material_sha256":r["material_sha256"],"frozen_target_physical_sha256":target["source_physical_sha256"],
                   "same_exact_original_candidate_and_target":tied,
                   "coordinate_provenance":"original point exactly regenerated" if tied else "independent full replay point",
                   "planned_named_addresses":len(addresses),"points":[],"errors":0}
            meta["stages"].append(entry);save()
            with ProcessPoolExecutor(max_workers=p["parallel_point_workers"]) as pool:
                pending={pool.submit(process_point,(str(source),pp,p,r,z,x,rr,zt,key,seed,str(out))):(key,seed)
                         for key,seed in addresses}
                for future in as_completed(pending):
                    key,seed=pending[future]
                    try:
                        result=future.result()
                    except Exception as exc:
                        result={"seed":key,"address":seed,"errors":[[type(exc).__name__,str(exc)[:320]]]}
                    if "errors" in result:entry["errors"]+=1
                    entry["points"].append(result)
                    # Preserve the specified logical ordering even with four independent workers.
                    entry["points"].sort(key=lambda item:next(j for j,(k,_) in enumerate(addresses) if k==item["seed"]))
                    meta["in_progress"]={"stage":i,"completed_addresses":len(entry["points"]),"last_seed":key}
                    save()
                    print(json.dumps({"event":"true_material_flow","stage":i,"seed":key,"point_sha256":r["point_sha256"],
                                      "peak_error":result.get("peak_error"),"errors":result.get("errors")}),flush=True)
            good=[v for v in entry["points"] if "peak_error" in v]
            if good:
                arg=max(good,key=lambda row:row["peak_error"])
                entry["maximum_observed_relative_gram_error"]=arg["peak_error"]
                entry["maximum_address_label"]=arg["seed"];entry["maximum_phase"]=arg["peak_t"]
            save()
        meta.pop("in_progress",None)
        failures=sum(e["errors"] for e in meta["stages"])
        meta["status"]="all_finite_trajectory_attempts_returned" if not failures else "completed_with_trajectory_failures"
        meta["full_result"]={"source_stages":stage_ids,"named_points_per_stage":[e["planned_named_addresses"] for e in meta["stages"]],
            "failed_addresses":failures,"both_tolerance_families_attempted":True,"spatial_continuum_or_interval_bound":None}
        save()
        return 0 if not failures else 2
    except Exception as exc:
        meta["status"]="runtime_failure"
        meta["exception"]=type(exc).__name__+": "+str(exc)[:1200]
        save();traceback.print_exc();return 1


def replay_target_id(summary):
    r=summary["frozen_target"]
    return {k:r[k] for k in ("source_stage","degree","source_design","source_physical_sha256")}


if __name__=="__main__":
    raise SystemExit(main())
