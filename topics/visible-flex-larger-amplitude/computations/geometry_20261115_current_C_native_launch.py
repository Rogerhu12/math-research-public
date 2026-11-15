#!/usr/bin/env python3
"""Bind one actual current-C geometry result to explicit full112 native requests.

No scientific value is reconstructed from a prior response. Request153 uses
one explicitly defined +0 physical-height vector and requests its actual full
eta=0 endpoint sensitivity and finite audit. Other complete H inputs remain
possible only through an explicit separately bound recipe.
Author: geometry agent (AI), 2026-11-15.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import os
import signal
from pathlib import Path
import struct
import subprocess
import sys
import time

SCHEMA="current-C-complete112-native-launch-result-v1"
RECIPE="current-C-complete112-native-execution-recipe-v1"
MODEL="R286-original-stored-continuous-model-convention-C-v1"
SAMPLER="geometry_20261115_current_C_radial_sampling.py"
CLIENT="geometry_20261115_current_C_tail_client.py"
REPO="Rogerhu12/math-research-public"


def actions():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPO:
        raise RuntimeError("Current-C scientific execution only in this public repository Actions")


def sha(raw):return hashlib.sha256(raw).hexdigest()


def read(path,expected=None):
    raw=Path(path).read_bytes()
    if expected is not None and sha(raw)!=expected:raise ValueError("Actual original input differs: "+str(path))
    return json.loads(raw),dict(file=Path(path).name,bytes=len(raw),sha256=sha(raw))


def file_receipt(path):
    h=hashlib.sha256();count=0
    with Path(path).open("rb") as stream:
        while block:=stream.read(1048576):h.update(block);count+=len(block)
    return dict(file=Path(path).name,bytes=count,sha256=h.hexdigest())


def emit(path,value):
    raw=(json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()
    with Path(path).open("xb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    return dict(file=Path(path).name,bytes=len(raw),sha256=sha(raw))


def main(argv=None):
    actions();p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--geometry-directory",type=Path,required=True)
    p.add_argument("--geometry-result-sha256",required=True)
    p.add_argument("--recipe",type=Path,required=True)
    p.add_argument("--recipe-sha256",required=True)
    p.add_argument("--computations",type=Path,required=True)
    p.add_argument("--source-topic",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args(argv)
    root=Path(os.environ["RUNNER_TEMP"]).resolve();out=args.out.resolve()
    if out==root or root not in out.parents or out.exists():
        raise ValueError("Use a new explicitly owned native launch directory")
    for source in (args.geometry_directory,args.recipe,args.computations,args.source_topic):
        if Path(source).resolve()==out or out in Path(source).resolve().parents:
            raise ValueError("Owned output cannot contain a source or original input")
    out.mkdir(parents=True)
    report=dict(schema=SCHEMA,repository=REPO,run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"],source_sha256=sha(Path(__file__).read_bytes()),
        completed=False,actual_client_process_started=False,actual_client_exit=None,error=None,
        no_historical_height_or_state_or_response_relabelled=True,
        infinite_C_nonlinear_DN_certified=False,full_BVP_or_closed_surface_accepted=False)
    exit_code=2;started=time.monotonic()
    try:
        recipe,rr=read(args.recipe,args.recipe_sha256)
        if recipe.get("schema")!=RECIPE or recipe.get("model_schema")!=MODEL:
            raise ValueError("Explicit independent current-C execution recipe required")
        if (recipe["modes"]!=112 or recipe["stage_count"]!=576 or recipe["node_count"]!=577
                or recipe["max_iterations"]!=32 or recipe["line_search_trials"]!=10
                or recipe["nonlinear_tolerance"]!=2e-9 or recipe["sensitivity_eta"]!=0):
            raise ValueError("Complete current native dimensions or declared nonlinear policy changed")
        if not isinstance(recipe.get("requests"),list) or not recipe["requests"]:
            raise ValueError("At least one explicit complete original physical-height request is required")
        if recipe["protocol_request_count"]!=len(recipe["requests"]):
            raise ValueError("The complete protocol-call count differs")
        records={}
        for name,expected in recipe["source_sha256"].items():
            if Path(name).name!=name:raise ValueError("Source closure uses exact computation basenames")
            actual=file_receipt(args.computations/name)
            if actual["sha256"]!=expected:raise ValueError("Pinned current source differs: "+name)
            records[name]=actual
        if file_receipt(__file__)!=records[Path(__file__).name]:
            raise ValueError("The actual launcher was not included in the source closure")
        geom,gr=read(args.geometry_directory/"result.json",args.geometry_result_sha256)
        if (geom.get("schema")!="current-C-physical-radial-samples-and-general-far-v1"
                or geom.get("source_sha256")!=recipe["source_sha256"][SAMPLER]
                or geom.get("target_model_schema")!=MODEL
                or geom.get("repository")!=REPO
                or geom.get("run_id")!=os.environ["GITHUB_RUN_ID"]
                or geom.get("source_commit")!=os.environ["GITHUB_SHA"]):
            raise ValueError("The native sampler is not the actual same-job/source geometry")
        report.update(original_recipe=rr,actual_geometry_result=gr,actual_source_closure=records,
            actual_geometry_completed=geom.get("completed"),
            actual_geometry_ready=geom.get("native_geometry_ready"),
            actual_sampler_error=geom.get("error"),
            explicit_protocol_request_count=len(recipe["requests"]),
            source_initial_height_origins=[r["origin"] for r in recipe["requests"]])
        if geom.get("completed") is not True or geom.get("native_geometry_ready") is not True:
            report.update(error=dict(type="CurrentCGeometryUnpaid",
                message="Actual geometry source remains partial; no native data was fabricated"),
                complete_unstarted_native_request_indices=list(range(len(recipe["requests"]))))
        else:
            requests=[]
            for index,item in enumerate(recipe["requests"]):
                if not isinstance(item["origin"],dict) or not item["origin"]:
                    raise ValueError("Every current physical height needs an explicit origin")
                H=[float(v) for v in item["height"]]
                if len(H)!=112 or not all(math.isfinite(v) for v in H):
                    raise ValueError("Keep all 112 actual finite physical height coefficients")
                zero=item.get("height_negative_zero_columns",[])
                if not isinstance(zero,list) or zero!=sorted(set(zero)):
                    raise ValueError("Negative-zero sidecar must be an exact ordered index list")
                for j in zero:
                    if not isinstance(j,int) or not 0<=j<112 or H[j]!=0:
                        raise ValueError("Explicit negative-zero sidecar differs")
                    H[j]=-0.0
                raw=b"".join(struct.pack("<d",v) for v in H)
                if sha(raw)!=item["height_sha256"]:
                    raise ValueError("Explicit requested height words differ")
                requests.append(dict(height=H,height_negative_zero_columns=zero,height_sha256=sha(raw),
                    jacobian=item["jacobian"],audit=item["audit"],origin=item["origin"]))
            plan=emit(out/"complete-physical-height-requests.json",dict(
                schema="current-C-explicit-full112-native-requests-v1",requests=requests,
                original_execution_recipe=rr,no_old_response_or_J_used_as_a_new_source=True))
            cfg={k:recipe[k] for k in ("source_sha256","original_runtime_sha256","eta","sensitivity_eta",
                "reference_floor","projection_floor","quadrature","steps","linear_budget_seconds",
                "maximum_factor_bytes","max_iterations","line_search_trials","nonlinear_tolerance")}
            cfg.update(schema="current-C-complete112-client-config-v1",model_schema=MODEL,repository=REPO,
                computations=str(args.computations.resolve()),source_topic=str(args.source_topic.resolve()),
                geometry_directory=str(args.geometry_directory.resolve()),geometry_result_sha256=gr["sha256"],
                original_execution_recipe=rr,original_actual_geometry_result=gr)
            config=emit(out/"current-C-client-config.json",cfg)
            command=[sys.executable,"-u",str(args.computations/CLIENT),
                "--config",str(out/config["file"]),"--source-topic",str(args.source_topic),
                "--requests",str(out/plan["file"]),"--requests-sha256",plan["sha256"],
                "--node-heap",str(recipe["node_heap_mib"]),"--out",str(out/"live-client")]
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",PYTHONUNBUFFERED="1")
            for key in ("GITHUB_TOKEN","GH_TOKEN","MR_TOKEN"):env.pop(key,None)
            report.update(actual_runtime_config=config,actual_complete_requests=plan,
                command=command,shell=False,
                explicit_resource_budget_seconds=recipe["native_process_budget_seconds"],
                complete_algorithm_iterations_not_truncated_by_source=True)
            emit(out/"native-client-launch.json",dict(schema=SCHEMA+"-launch",**{
                k:report[k] for k in ("command","shell","actual_runtime_config","actual_complete_requests",
                "explicit_resource_budget_seconds","source_initial_height_origins")}))
            stdout=out/"native-client.stdout.log";stderr=out/"native-client.stderr.log"
            with stdout.open("xb") as so,stderr.open("xb") as se:
                report["actual_client_process_started"]=True
                process=subprocess.Popen(command,cwd=args.computations,env=env,stdout=so,stderr=se,
                    shell=False,start_new_session=True)
                report["owned_client_process_group"]=process.pid
                try:
                    report["actual_client_exit"]=process.wait(timeout=recipe["native_process_budget_seconds"])
                except subprocess.TimeoutExpired as error:
                    report["error"]=dict(type="NativeResourceTimeout",message=str(error),
                        actual_native_or_endpoint_acceptance_not_inferred=True)
                finally:
                    # The Node worker and its synchronous QR children inherit this
                    # new, exclusively owned process group. No original input or
                    # unrelated process is in it. Stop remaining descendants before
                    # any scalar readback or later owned-directory cleanup.
                    def group_exists():
                        # Linux runner: a zombie has no live code or open writing
                        # thread. Ignore only that explicit state, not missing
                        # metadata or a stopped live process.
                        for candidate in Path("/proc").iterdir():
                            if not candidate.name.isdigit():continue
                            try:
                                if os.getpgid(int(candidate.name))!=process.pid:continue
                                state=(candidate/"stat").read_text().rsplit(")",1)[1].split()[0]
                                if state!="Z":return True
                            except ProcessLookupError:continue
                            except FileNotFoundError:continue
                        return False
                    remaining=group_exists()
                    report["owned_descendants_remained_after_client_wait"]=remaining
                    if remaining:
                        os.killpg(process.pid,signal.SIGTERM)
                        until=time.monotonic()+30
                        while group_exists() and time.monotonic()<until:time.sleep(0.2)
                        if group_exists():
                            os.killpg(process.pid,signal.SIGKILL)
                            until=time.monotonic()+10
                            while group_exists() and time.monotonic()<until:time.sleep(0.2)
                    if process.poll() is None:process.wait()
                    report["actual_client_exit"]=process.returncode
                    report["owned_process_group_shutdown_before_readback"]=not group_exists()
                    if not report["owned_process_group_shutdown_before_readback"]:
                        raise RuntimeError("Owned native descendant remains live; report partial and do not clean its directory")
                    so.flush();os.fsync(so.fileno());se.flush();os.fsync(se.fileno())
            report["actual_client_stdout"]=file_receipt(stdout)
            report["actual_client_stderr"]=file_receipt(stderr)
            final=out/"live-client"/"explicit-request-result.json"
            if final.is_file():
                returned,identity=read(final)
                report["actual_client_result"]=identity
                report["actual_client_completed_request_count"]=len(returned["actual_completed_readbacks"])
                report["actual_client_reported_error"]=returned["error"]
                if report["actual_client_exit"]==0 and returned["error"] is None:
                    report["completed"]=True;exit_code=0
            if report["actual_client_exit"] not in (None,0) and report["error"] is None:
                report["error"]=dict(type="ActualNativeClientFailure",
                    message="Actual child exit "+str(report["actual_client_exit"]),
                    no_root_or_line_search_failure_cause_inferred_without_original_packets=True)
    except Exception as error:
        report["error"]=dict(type=type(error).__name__,message=str(error))
    finally:
        report["elapsed_seconds"]=time.monotonic()-started
        result=emit(out/"result.json",report)
        print(json.dumps(dict(event="current-C-native-launch-result",result=result,
            completed=report["completed"],actual_client_exit=report["actual_client_exit"],
            error=report["error"]),allow_nan=False),flush=True)
    return exit_code


if __name__=="__main__":
    raise SystemExit(main())
