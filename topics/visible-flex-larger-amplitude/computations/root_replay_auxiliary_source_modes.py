#!/usr/bin/env python3
"""Serial, separately recoverable single-mode executions of a frozen source plan.

No mathematical formula is changed. Each child has its own original wait4
resource record, immutable plan, console transcript and compressed primary.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda:f.read(1<<18), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--plan",type=Path,required=True)
    ap.add_argument("--state",type=Path,required=True)
    a = ap.parse_args()
    plan = json.loads(a.plan.read_text())
    if a.state.exists():
        raise FileExistsError("Use a fresh run state; successful mode outputs are immutable")
    state = dict(status="running", plan=str(a.plan),plan_sha256=digest(a.plan),
                 source_sha256=digest(__file__),completed=[])

    def save():
        state["utc"] = datetime.now(timezone.utc).isoformat()
        temp = a.state.with_suffix(a.state.suffix+".tmp")
        temp.write_text(json.dumps(state,indent=2)+"\n")
        temp.replace(a.state)

    save()
    for mode in plan["run_modes"]:
        if digest(plan["frozen_source"]) != plan["frozen_source_sha256"]:
            raise ValueError("The mathematical source changed during this serial batch")
        prefix = plan["output_prefix_pattern"].format(mode=mode)
        paths = {"plan":Path(prefix+"-plan.json"),
                 "resource":Path(prefix+"-resource.json"),
                 "console":Path(prefix+"-console.log"),
                 "primary":Path(prefix+".json.gz")}
        if any(p.exists() for p in paths.values()):
            raise FileExistsError("A mode output already exists: "+prefix)
        command = plan["command_base"]+["--mode",str(mode),"--out",str(paths["primary"])]
        prepared = dict(status="Prepared, not yet executed",mode=mode,command=command,
            source_sha256=plan["frozen_source_sha256"],parent_plan_sha256=state["plan_sha256"],
            owned_RSS_MiB=40,estimated_seconds=4,new_ODE=0,new_source_integrals=0,
            utc=datetime.now(timezone.utc).isoformat())
        paths["plan"].write_text(json.dumps(prepared,indent=2)+"\n")
        run = [plan["python"],"computations/strong_resource_run.py",
               "--out",str(paths["resource"]),"--"]+command
        p = subprocess.run(run,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        paths["console"].write_bytes(p.stdout)
        resource = json.loads(paths["resource"].read_text()) if paths["resource"].exists() else {}
        record = dict(mode=mode,wrapper_exit=p.returncode,wait4_exit=resource.get("exitcode"),
                      wall_seconds=resource.get("wall_seconds"),peak_rss_kib=resource.get("peak_rss_kib"))
        events=[]
        for line in p.stdout.decode(errors="replace").splitlines():
            if line.startswith("{"):
                try: events.append(json.loads(line))
                except json.JSONDecodeError: pass
        done = [e for e in events if e.get("event")=="done"]
        success = (p.returncode==0 and resource.get("exitcode")==0 and len(done)==1
                   and done[0].get("all_gates") and done[0].get("modes")==[mode]
                   and paths["primary"].exists()
                   and digest(paths["primary"])==done[0].get("sha256"))
        record["verified_success"] = bool(success)
        record["files"] = [dict(path=str(path),bytes=path.stat().st_size,sha256=digest(path))
                           for path in paths.values() if path.exists()]
        state["completed"].append(record)
        if not success:
            state["status"]="stopped at a preserved unsuccessful mode"
            save();print(json.dumps(record),flush=True);raise SystemExit(1)
        save();print(json.dumps({k:v for k,v in record.items() if k!="files"}),flush=True)
    state["status"]="all planned modes formally completed"
    state["all_planned_modes_complete"]=(
        [r["mode"] for r in state["completed"]]==plan["run_modes"]
        and all(r["verified_success"] for r in state["completed"]))
    save()
    print(json.dumps(dict(event="batch_done",modes=len(state["completed"]),
                         all_complete=state["all_planned_modes_complete"],state_sha256=digest(a.state))),flush=True)


if __name__ == "__main__":
    main()
