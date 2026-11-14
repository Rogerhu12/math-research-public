#!/usr/bin/env python3
"""Verify closed call15 and ENOSPC provenance; prepare resume03 without a solver."""
import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import numpy as np

EXPECTED = {
    "launch02":"b2e7371a89906a5f1048077eb2040fef8f2c0a58a136ef3812ab6cbc36b5310e",
    "controller":"23f75c9ecc2825e4a8314468775c40b06b6b47439edd0d0ed9a69a9fb5e298a9",
    "client":"cd9b25521427dcefebd5baddcf6a105c58c53f495cf8692fb725d49e4558a564",
    "response":"e6ef3389c839be9f793a11d875d99c616c207acc58b680efc0bda2c005e55c1f",
    "audit":"0bef9b292623e1531f7474c5ed53894638877d13230eaabd4f8eb5d5e2ad3ece",
    "interruption":"5cda4dd0fd47dd002b4c57fc648152a6307de27b9a67d5ae00090c9eab8e496e",
    "interruption_note":"a195c85368e9297ac9ae8d907bc10c60f89538304b1821af18921e871eecabb0",
}
IO = {"initialCheckpoint","traceFile","iterationCheckpointFile",
      "trialDiagnosticFile","trialStatePrefix"}
SOURCES = {
    "db6f-prefix-tail-continuation-client.py",
    "db6f-prefix-tail-trial-worker.mjs",
    "db6f-prefix-tail-trial-core.mjs",
    "db6f-prefix-tail-trial-split.mjs",
    "950f-tail-subdivision.mjs","950f-tail-warm-remesh.mjs",
    "closing_weighted_tail.mjs","closing_recalibrated_tail.mjs",
}


def read(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix==".gz" else raw)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False)


def need(condition,message):
    if not condition:
        raise ValueError(message)


def number(x):
    return type(x) in (int,float) and math.isfinite(x)


def vector(v,n):
    return type(v) is list and len(v)==n and all(number(x) for x in v)


def write_new(path,data):
    raw=(json.dumps(data,indent=2,allow_nan=False)+"\n").encode()
    need(len(raw)<1_000_000,"Unexpected large metadata")
    with Path(path).open("xb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    Path(path).chmod(0o444)


def main():
    script=Path(__file__).resolve();topic=script.parent.parent
    repo=script.parents[3];notes=topic/"notes"
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--launch",type=Path,default=notes/"2026-11-09-db6f-prefix-amplitude-resume03-launch.json")
    ap.add_argument("--report",type=Path,default=notes/"2026-11-09-db6f-prefix-amplitude-resume03-source-check.json")
    args=ap.parse_args()
    launch_out=args.launch.resolve();report_out=args.report.resolve()
    out=notes/"2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-03"
    need(not list(notes.glob(out.name+"*")),"Resume03 output stem is already used")
    need(launch_out!=report_out,"Launch and report must differ")
    for p in (launch_out,report_out):
        need(not p.exists(),"Metadata output exists: "+str(p))
        need(not (p.parent==notes and p.name.startswith(out.name)),
             "Preparation metadata must not occupy the controller output stem")
    paths={
        "launch02":notes/"2026-11-09-db6f-prefix-amplitude-resume02-launch.json",
        "controller":script.with_name("db6f-prefix-tail-amplitude-continuation.py"),
        "client":script.with_name("db6f-prefix-tail-continuation-client.py"),
        "response":notes/"2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-02_tail_0015.json.gz",
        "audit":notes/"2026-11-09-db6f-root-continuation02-call015-closed-audit-v2.json",
        "interruption":notes/"2026-11-09-db6f-root-amplitude-resume02-observed-execution.json",
        "interruption_note":notes/"2026-11-09-db6f-root-amplitude-continuation02-enospc.md",
    }
    for key,path in paths.items():
        need(sha(path)==EXPECTED[key],"Frozen identity changed: "+key)
    old=read(paths["launch02"]);audit=read(paths["audit"]);observed=read(paths["interruption"])
    files=set(paths.values())|{script}

    def verify_rows(rows,count):
        need(type(rows) is list and len(rows)==count,"Wrong binding count")
        for item in rows:
            p=Path(item["path"])
            if not p.is_absolute():
                p=repo/p
            need(p.is_file() and sha(p)==item["sha256"],"Binding hash mismatch: "+str(p))
            need(type(item["bytes"]) is int and p.stat().st_size==item["bytes"],
                 "Binding byte count mismatch: "+str(p))
            files.add(p.resolve())

    verify_rows(old["bound_files"],66)
    verify_rows(audit["closed_files"],8)
    verify_rows(observed["files"],9)
    need(audit["status"]=="PASS-closed-converged-finite-DN-provenance-and-request-audit",
         "Call15 closed audit did not pass")
    need(canonical([audit["call"],audit["scale"],audit["source_bindings_verified"],
                    audit["response_source_hashes_matched"]])==canonical([15,31/32,66,8]),
         "Call15 audit identity differs")
    audited_source=repo/audit["script"]["path"]
    need(sha(audited_source)==audit["script"]["sha256"],"Closed auditor source changed")
    files.add(audited_source)
    need(observed["status"]=="observed-process-completed" and
         canonical([observed["actual_exit_code"],observed["tool_session_id"],
                    observed["observer"],observed["tool_receipt"]])==
         canonical([1,17869,"/root","cf4fa6"]),"Wrong actual interruption observation")
    need(observed["controller_child_exit_code_directly_recorded"] is None and
         observed["worker_exit_code_directly_recorded"] is None,
         "Do not invent child/worker exit observations")
    need(observed["complete_call016_response_exists"] is False and
         observed["final_reproduction_exists"] is False and
         observed["target_reached"] is False and observed["target_audited"] is False,
         "Unexpected old completed-target identity")

    command=list(old["command"])
    def value(flag):
        need(command.count(flag)==1,"Wrong argv multiplicity: "+flag)
        return command[command.index(flag)+1]
    need(command[1]==str(paths["controller"]) and old["cwd"]==str(repo),
         "Old controller/cwd differs")
    config_path=Path(value("--config"));target_path=Path(value("--target-prefix"))
    source_root=Path(value("--source-root"))
    need(config_path==notes/"2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-01-config.json",
         "Original configuration path changed")
    need(target_path==notes/"2026-11-09-db6f-prefix-flat-v17v18-m15-affine-cut-predictor-from14q512.json.gz",
         "Original target path changed")
    need(source_root==topic/"repro/source-root","Frozen source-root changed")
    cfg=read(config_path);target=read(target_path);record=read(paths["response"])
    response=record["response"];cp=response["checkpoint"]
    nonio=lambda d:{k:v for k,v in d.items() if k not in IO}
    need(canonical(nonio(cfg))==canonical(nonio(record["config"])),
         "Actual call15 equation/configuration differs by more than five I/O keys")
    want={"modes":15,"spacing":3,"depth":12,"shootingParts":8,"steps":32,
          "quadrature":256,"solveTolerance":2e-9,"maxIterations":36,
          "cuspAwareFlow":True,"actualCuspGrid":True,"sharedEngines":True}
    need(canonical({k:cfg[k] for k in want})==canonical(want),"Original solver controls changed")
    need(canonical(cfg.get("projectionFloor",.05))==canonical(.05),
         "Original positive guard changed")
    need(cfg.get("correctInitialBoundary",True) is True,"Original boundary correction disabled")
    cpwant={"modes":15,"quadrature":256,"physicalDepth":12,"shootingParts":8,
            "steps":32,"projectionFloor":.05}
    need(canonical({k:cp["parameters"][k] for k in cpwant})==canonical(cpwant),
         "Actual checkpoint discretization/guard differs")
    need(target["config"].get("actual_nonlinear_tail") is False and
         type(target["config"]["modes"]) is int and target["config"]["modes"]==15,
         "The frozen target must remain auxiliary, not a fabricated coupled solution")
    for key,expected in target["physical_tail_parameters"].items():
        need(key in cfg and canonical(cfg[key])==canonical(expected),
             "Physical tail parameter changed: "+key)
    need(response.get("converged") is True and not response.get("failed"),
         "Call15 is not an actual converged response")
    residual=response.get("residual")
    need(number(residual) and residual==6.367950627222893e-10 and 0<=residual<cfg["solveTolerance"],
         "Original residual tolerance or closed result changed")
    need(canonical(audit["residual"])==canonical(residual),"Audit residual differs")
    request=record["request"]
    need(set(request)=={"height","jacobian","audit"} and
         request["jacobian"] is False and request["audit"] is False,
         "Call15 request is an unaudited warm request")
    need(response.get("heightJetJacobian") is None and response.get("audit") is None,
         "Do not relabel call15 as the final Jacobian/audit response")
    goal=target["predicted_cut_height"]
    need(vector(goal,15) and vector(request["height"],15) and vector(cp["cutHeight"],15),
         "Invalid physical cut-height vectors")
    expected=np.asarray(goal,dtype=float)*np.float64(31/32)**np.arange(1,16)
    need(np.array_equal(np.asarray(request["height"]),expected) and
         np.array_equal(np.asarray(cp["cutHeight"]),expected),
         "Original NumPy H(31/32) differs")
    need(type(cp["states"]) is list and len(cp["states"])==865 and
         all(vector(v,30) for v in cp["states"]),"Invalid finite shape checkpoint")
    indices=cp["rawNode"]
    need(type(indices) is list and len(indices)==13 and
         all(type(i) is int for i in indices) and indices==[72*k for k in range(13)],
         "Wrong original raw-node layout")
    need(type(cp["rawStates"]) is list and len(cp["rawStates"])==13 and
         all(vector(v,30) for v in cp["rawStates"]) and
         canonical(cp["rawStates"])==canonical([cp["states"][i] for i in indices]),
         "Raw-state mapping differs")
    history=response.get("history")
    need(type(history) is list and len(history)==7 and
         all(type(h.get("iteration")) is int and h["iteration"]==i and
             number(h.get("norm")) for i,h in enumerate(history)),
         "Closed original iteration history differs")
    need(set(record["source_sha256"])==SOURCES,"Wrong actual eight-source set")
    for name,digest in record["source_sha256"].items():
        path=script.parent/name
        need(sha(path)==digest,"Actual response source changed: "+name)
        files.add(path)

    changes={"--out-prefix":str(out),"--initial-step":".015625",
             "--resume-checkpoint":str(paths["response"]),"--resume-scale":".96875"}
    for key,new in changes.items():
        value(key);command[command.index(key)+1]=new
    different=[i for i,(a,b) in enumerate(zip(command,old["command"])) if a!=b]
    need(len(command)==len(old["command"]) and
         different==sorted(command.index(k)+1 for k in changes),"Unexpected argv changes")
    need(value("--initial-scale")==".25" and value("--maximum-step")==".2" and
         value("--minimum-step")==".000244140625" and value("--max-attempts")=="64" and
         value("--node-heap")=="1536","Unchanged continuation controls differ")
    need(min(1.,31/32+1/64)==63/64,"First next target differs")
    files.update([config_path,target_path,source_root/"topics/large-amplitude-twist-flex/scripts/general_root_tail_momentum.mjs"])
    report={
        "status":"PASS_CLOSED_CALL15_RESUME03_SOURCE_INTERFACE_ONLY",
        "resume_response":str(paths["response"]),"resume_response_sha256":sha(paths["response"]),
        "resume_scale":31/32,"next_requested_scale":63/64,"initial_step":1/64,
        "original_tolerance":cfg["solveTolerance"],"original_maxIterations":36,
        "residual":residual,"converged":True,"audited":False,"jacobian_requested":False,
        "checkpoint_shape":[865,30],"raw_checkpoint_shape":[13,30],"history_base_evaluations":7,
        "physical_H_matches_original_NumPy_rule":True,
        "typed_configuration_identical_except_five_IO":True,
        "prior_launch_bindings_verified":66,"closed_call15_bindings_verified":8,
        "interruption_bindings_verified":9,"actual_response_sources_verified":8,
        "interruption_record":str(paths["interruption"]),"interruption_sha256":sha(paths["interruption"]),
        "old_actual_tool_exit_code":1,"old_child_exit_code":None,"old_worker_exit_code":None,
        "call16_numerical_failure_asserted":False,"interrupted_iteration_used_as_warm":False,
        "changed_argv_options":list(changes),"unchanged_controller":True,"unchanged_client":True,
        "future_target_and_final_audit_not_asserted":True,"solver_launches":0,
        "scope":"Only an original converged s=31/32 finite warm is accepted. Resume03 has its own identity. Exact s=1 plus original Jacobian/source audit and real exit must occur later; prefix remains unsolved.",
    }
    need(not list(notes.glob(out.name+"*")),"Resume03 stem became used during preparation")
    write_new(report_out,report);files.add(report_out)
    bound=[{"path":str(p.resolve()),"bytes":p.stat().st_size,"sha256":sha(p)}
           for p in sorted(files)]
    launch={
        "status":"PREPARED_ONLY_NO_RESUME_STARTED_BY_THIS_AGENT",
        "cwd":str(repo),"command":command,"stdout_log":str(out)+"-run.log",
        "stderr":"redirect to stdout_log","out_prefix":str(out),
        "resume_response_sha256":sha(paths["response"]),"resume_scale":31/32,
        "next_requested_scale":63/64,"initial_step":1/64,
        "step_rule":"Choose a smaller boundary-continuation step after infrastructure interruption; unchanged original controller adapts later steps. No claim that ENOSPC is mathematical failure.",
        "bound_files":bound,"required_prelaunch_checks_passed":True,
        "preparation_script_sha256":sha(script),"original_controller_sha256":sha(paths["controller"]),
        "original_client_sha256":sha(paths["client"]),"interruption_record_sha256":sha(paths["interruption"]),
        "source_check_report":str(report_out),"source_check_report_sha256":sha(report_out),
        "scope":"Original controller resumed under continuation03 identity from genuine closed call15. Do not overwrite controller -reproduction.json with the root execution observer.",
    }
    write_new(launch_out,launch)
    print(json.dumps({"verified":True,"launch":str(launch_out),"launch_sha256":sha(launch_out),
                      "report_sha256":sha(report_out),"bindings":len(bound),
                      "first_scale":63/64,"solver_launches":0}),flush=True)


if __name__=="__main__":
    main()
