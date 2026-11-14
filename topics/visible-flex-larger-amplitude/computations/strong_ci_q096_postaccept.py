#!/usr/bin/env python3
"""Verify the accepted q096 design as a fixed view, then compute its true response.

This driver never reruns the q096 BVP or starts a tail worker. It requires the
byte-verified original Actions artifact restoration report and the accepted
M+3 actual endpoint. The first numerical stage is the genuine M+3 -> M
fixed-view RMS/full-H/physical-BC verification. Only then may the unchanged
full-field actual Jacobian be differentiated in delta/LB/vp, the two
explicit first-piece controls, and the existing vd/vu/descending-K directions. No nonlinear continuation or closure result
is asserted by this derivative calculation.
"""
from __future__ import annotations
import argparse
import datetime
import gzip
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
TOPIC = Path("topics/visible-flex-larger-amplitude")
ORIGINAL_PREFIX = "notes/2026-11-12-strong-actual-q096-ci-actions-43302113873-1-strong"
ZIP_SHA = "27c0e11f6ab2c0fc45338dd186c0fdd36cfe7f2f962f1b849f509708054331fb"
RECOVERY_SOURCE_SHA = "2cd1010a2e5ea315a9b899490029ecc5957ae070911b514f0d41235ee31fe6f4"
SOURCE_RESTORE_SHA = "12a0bf27f1ed1288b77d0f55ead1d72954422f89f78b3dbafd16b226ac450e33"
SOURCE_HASHES = {
    "strong_initial_laws_freeze_design_view.py":
        "785442ffad4a72f9671aef285dae4a4bfc11f410b2cec54027cd913a09a61ab3",
    "strong_initial_laws_disk_control_response.py":
        "42db431d26f8cc87b56f3e8baf38b7afba38816f701d185efd1955028afe9750",
    "strong_monotone_initial_speed.py":
        "12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7",
    "strong_monotone_initial_speed_check.py":
        "d2b5a0a28b79658c8b83a21fcc8c53323792182e221ec9d203aff8f12af3646a",
    "strong_pulse_freeze_design_view.py":
        "18ff9e44b4f69e52017c5a7d20998e1a7d06c77fd3930bd7b21b767d984f4e7e",
    "strong_pulse_disk_control_response.py":
        "7b74a86e2e7f8e88d1280985dce7bcae85aa273a174f00f9511f3a4d14099f7f",
    "strong_disk_actual_fixed_control_response.py":
        "e20e9724b82130848562142ac23cec3c65959949e5470436a643358b664ba0bf",
    "root_actual_freeze_design_view.py":
        "4209f87b8cae531f8899c5fa9af48a13666411c340981ae759daa9034315628b",
    "strong_foreground_resource_run.py":
        "e683fbbeb1eb579d07799acbdd08b2254917e49209566c28a85628eb9cb72bc6",
}
SELF_SHA = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
THREADS = {name:"1" for name in (
    "OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS")}


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def digest(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(1024*1024),b""):
            value.update(block)
    return value.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open(path,"rt") if path.suffix == ".gz" else path.open()) as stream:
        return json.load(stream)


def write(path, data):
    path = Path(path)
    payload = (json.dumps(data,indent=2,allow_nan=False)+"\n").encode()
    if len(payload) >= 5_000_000:
        raise ValueError("Oversized orchestration record")
    temporary = path.with_name(path.name+".tmp-"+str(os.getpid()))
    with temporary.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    try:
        os.link(temporary,path)
    finally:
        temporary.unlink()


def local(topic, value):
    relative = Path(value)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("An original relative notes path is required")
    result = topic/relative
    result.resolve().relative_to((topic/"notes").resolve())
    return result


def check(path, expected=None):
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError("Required accepted input/source missing: "+str(path))
    actual = digest(path)
    if expected is not None and expected != actual:
        raise ValueError("Accepted input/source hash differs: "+str(path))
    return dict(path=str(path),bytes=path.stat().st_size,sha256=actual)


def accepted_inputs(topic, recovery_path):
    report = read(recovery_path)
    if (report.get("entry_sha256") != RECOVERY_SOURCE_SHA
            or report.get("artifact_id") != 13983440730
            or report.get("status") != "complete-byte-verified-original-artifact-restoration"
            or report.get("download",{}).get("sha256") != ZIP_SHA
            or report.get("formal_original_solver_success") is not True
            or report.get("formal_original_audit_pending") is not False
            or report.get("original_stable_manifest",{}).get("all_original_recorded_hashes_equal") is not True):
        raise ValueError("The original complete accepted CI artifact has not been established")
    stable_path = topic/(ORIGINAL_PREFIX+"-ci-stable-files.json")
    check(stable_path,report["original_stable_manifest"]["sha256"])
    stable = read(stable_path)
    if stable.get("original_solver_success_and_audit_complete") is not True:
        raise ValueError("Original numerical CI output did not record audited acceptance")
    records = {}
    for item in stable["files"]:
        relative = Path(item["path"])
        if (relative.is_absolute() or ".." in relative.parts
                or not relative.as_posix().startswith(ORIGINAL_PREFIX)):
            raise ValueError("Unexpected original stable input path")
        if item["path"] in records:
            raise ValueError("Duplicate original stable entry")
        records[item["path"]] = item

    checked = [check(recovery_path),check(stable_path)]
    def original_file(relative):
        if relative not in records:
            raise ValueError("Required mathematics input is absent from original stable snapshot: "+relative)
        item = records[relative]
        path = local(topic,relative)
        row = check(path,item["sha256"])
        if row["bytes"] != item["bytes"]:
            raise ValueError("Original accepted input byte count differs")
        checked.append(row)
        return path

    primary_rel = ORIGINAL_PREFIX+".json.gz"
    raw_rel = ORIGINAL_PREFIX+"-raw-collocation.json.gz"
    config_rel = ORIGINAL_PREFIX+"-config.json"
    primary,raw_path,config = map(original_file,(primary_rel,raw_rel,config_rel))
    saved,raw = read(primary),read(raw_path)
    if (saved.get("solver_success") is not True or saved.get("audit_pending",True)
            or saved.get("error") or not saved["config"].get("actual_nonlinear_tail")
            or saved["config"].get("fixed_metric") or not raw.get("solver_success")
            or raw["identity"].get("fixed") or raw["arrays"]["p"]["shape"] != [27]
            or int(saved["modes"]) != 24 or int(saved["config"]["angular"]) != 768
            or saved["config"]["tol"] != 1e-7 or saved["gauge_amplitude"] != .09):
        raise ValueError("Expected the original accepted M24/N768/tol7 augmented actual endpoint")
    if saved["raw_collocation_checkpoint"]["sha256"] != digest(raw_path):
        raise ValueError("Accepted physical primary links a different raw state")
    if digest(config) != raw["identity"]["coupling_context"]["tail_config_sha256"]:
        raise ValueError("The original generated actual configuration changed")
    tail_rel = saved["actual_tail"]["final_response"]
    tail = original_file(tail_rel)
    for value in raw["arrays"].values():
        for chunk in value["chunks"]:
            if Path(chunk["file"]).name != chunk["file"]:
                raise ValueError("Original raw chunk path is not a basename")
            file = original_file("notes/"+chunk["file"])
            if digest(file) != chunk["sha256"]:
                raise ValueError("Raw-linked chunk differs from the original stable snapshot")
    for chunk in saved["pp_coefficient_chunks"]:
        if Path(chunk["file"]).name != chunk["file"]:
            raise ValueError("Original physical quintic chunk path is not a basename")
        file = original_file("notes/"+chunk["file"])
        if digest(file) != chunk["sha256"]:
            raise ValueError("Physical quintic chunk differs")
    # The real fixed-view utility below additionally reconstructs the whole
    # field and checks exact full H, original RMS and all physical BCs.
    unique = {row["path"]:row for row in checked}
    return dict(primary=primary_rel,raw=raw_rel,tail=tail_rel,config=config_rel,
        modes=24,angular=768,gauge=.09,parameters=len(raw["parameter_state"]),
        nodes=raw["arrays"]["x"]["shape"][0],
        actual_primary_amplitude=saved["actual_primary_amplitude"],
        final_physical_profile=saved["frozen_profile"],
        original_metric_audit=saved.get("summary"),
        source_records=list(unique.values()))


def stage(topic,prefix,name,command,env):
    part = Path(str(prefix)+"-"+name)
    relative = str(part.relative_to(topic))
    supervisor = [sys.executable,"-u","computations/strong_foreground_resource_run.py",
        "--out",relative+"-resource.json","--heartbeat",relative+"-heartbeat.json",
        "--ownership",relative+"-ownership.json","--task-prefix",relative,
        "--",*command]
    plan = dict(stage=name,created_utc=utc(),command=command,supervisor=supervisor,
        cwd=str(topic),Node_workers=0,new_BVP=False,
        environment={key:env[key] for key in (*THREADS,"TMPDIR","PYTHONUNBUFFERED")},
        full_environment_never_serialized=True)
    write(Path(str(part)+"-command.json"),plan)
    result = None
    with Path(str(part)+".log").open("xb") as output:
        process = subprocess.Popen(supervisor,cwd=topic,env=env,
            stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for block in iter(process.stdout.readline,b""):
            output.write(block)
            output.flush()
            sys.stdout.buffer.write(block)
            sys.stdout.buffer.flush()
        result = process.wait()
    resource_path = Path(str(part)+"-resource.json")
    owned = read(resource_path) if resource_path.is_file() else None
    terminal = dict(stage=name,finished_utc=utc(),supervisor_returncode=result,
        owned_wait4_resource=owned,new_nonlinear_solution=False)
    write(Path(str(part)+"-terminal.json"),terminal)
    if result or owned is None or owned.get("exitcode") != 0:
        raise RuntimeError("Required genuine postaccept stage did not formally finish: "+name)
    return terminal


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--work-root",type=Path,required=True)
    parser.add_argument("--run-id",required=True)
    parser.add_argument("--recovery-report",type=Path,required=True)
    parser.add_argument("--prepare-only",action="store_true")
    parser.add_argument("--phase",choices=("all","freeze","response"),default="all")
    parser.add_argument("--existing-fixed-view-prefix",type=Path)
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,79}",args.run_id):
        raise ValueError("Use a fresh simple CI run ID")
    if (args.phase=="response") != bool(args.existing_fixed_view_prefix):
        raise ValueError("Response-only recovery requires its completed fixed-view prefix")
    repo=args.repo.resolve();topic=repo/TOPIC
    prefix=topic/"notes"/("2026-11-12-strong-q096-postaccept-"+args.run_id)
    if any(prefix.parent.glob(prefix.name+"*")):
        raise FileExistsError("Use a fresh output identity")
    recovery_path = local(topic,args.recovery_report)
    inputs=accepted_inputs(topic,recovery_path)
    hashes={str(HERE/name):check(HERE/name,expected)["sha256"]
        for name,expected in SOURCE_HASHES.items()}
    check(HERE/"strong_ci_q096_recovery.py",SOURCE_RESTORE_SHA)
    import strong_ci_q096_recovery as recovery
    work=args.work_root.resolve()/("strong-q096-postaccept-"+args.run_id)
    work.mkdir(parents=True,exist_ok=False)
    temporary=work/"arenas";temporary.mkdir()
    if shutil.disk_usage(temporary).free<1_000_000_000:
        raise OSError("Use an owned disk with enough room for original full-Jacobian/QR arenas")
    env=dict(os.environ);env.update(THREADS)
    source_topic,source_origin=recovery.restore_source(repo,topic,work/"source",env)
    env=recovery.numerical_environment(env)
    for key in tuple(os.environ):
        if key not in recovery.numerical_environment({key:os.environ[key]}):
            os.environ.pop(key,None)
    env.update(PYTHONUNBUFFERED="1",TMPDIR=str(temporary))
    for key,value in THREADS.items():os.environ[key]=value
    import numpy
    import scipy
    if (platform.python_version()!="3.12.14" or numpy.__version__!="2.3.5"
            or scipy.__version__!="1.17.0"):
        raise ValueError("Use the original declared Python/NumPy/SciPy versions")
    fixed=(args.existing_fixed_view_prefix if args.existing_fixed_view_prefix
        else Path(str(prefix.relative_to(topic))+"-fixed"))
    fixed_path=local(topic,fixed)
    if args.phase=="response":
        fixed_report=read(Path(str(fixed_path)+"-report.json"))
        if (fixed_report.get("original_parameter_count")!=27
                or fixed_report.get("fixed_parameter_count")!=24
                or fixed_report.get("counters")!=dict(raw_restorations=1,residual_checks=1,tail_start_attempts=0)
                or not fixed_report.get("complete_H_bitwise_equal")):
            raise ValueError("Response-only mode requires the actual completed 27-to24 check")
    common=["--source-topic",str(source_topic),
        "--port","computations/alternative-neck-provider-smallcut30-port32-r2048.json",
        "--tail-config",inputs["config"],"--defer-tail-start"]
    relative=str(prefix.relative_to(topic))
    commands={
        "provider-fixture":[sys.executable,"-u","computations/strong_monotone_initial_speed_check.py",
            "--out",relative+"-provider-fixture.json"],
        "fixed-source":[sys.executable,"-u","computations/strong_initial_laws_freeze_design_view.py",
            "--prepare-source-record",relative+"-fixed-source.json"],
        "response-source":[sys.executable,"-u","computations/strong_initial_laws_disk_control_response.py",
            "--prepare-source-record",relative+"-response-source.json"],
        "fixed-view":[sys.executable,"-u","computations/strong_initial_laws_freeze_design_view.py",
            "--design-checkpoint",inputs["primary"],"--design-raw",inputs["raw"],
            "--design-tail",inputs["tail"],"--fixed-view-prefix",str(fixed),
            "--radial-batch-size","8",*common],
        "actual-response":[sys.executable,"-u","computations/strong_initial_laws_disk_control_response.py",
            "--response-checkpoint",str(fixed)+".json.gz",
            "--response-raw",str(fixed)+"-raw-collocation.json.gz",
            "--response-tail",inputs["tail"],"--response-out-prefix",relative+"-response",
            "--response-fields","delta,boost_length,boost_speed,initial_speed_pulse,initial_speed_frontload,vd,vu,descending_turn_curvature",
            "--radial-batch-size","8","--collocation-batch-size","12",
            "--disk-backward-error-tol","5e-11","--disk-heartbeat-seconds","20",
            "--disk-temporary-parent",str(temporary),*common],
    }
    ordered=["provider-fixture","fixed-source","response-source"]
    if args.phase in ("all","freeze"):ordered.append("fixed-view")
    if args.phase in ("all","response"):ordered.append("actual-response")
    metadata=dict(scope=__doc__,entry_sha256=SELF_SHA,status="prepared-not-executed",
        created_utc=utc(),phase=args.phase,inputs=inputs,source_origin=source_origin,
        source_sha256=hashes,commands={name:commands[name] for name in ordered},
        numerical_environment={**THREADS,"TMPDIR":str(temporary),"PYTHONUNBUFFERED":"1"},
        authentication_removed_before_any_numeric_child=True,all_MJS_unchanged=True,
        Node_workers_started=0,q096_BVP_rerun=False,new_nonlinear_solution=False,
        runtime=dict(python=platform.python_version(),numpy=numpy.__version__,scipy=scipy.__version__))
    write(Path(str(prefix)+"-plan.json"),metadata)
    print(json.dumps(dict(event="q096_postaccept_prepared",prefix=relative,
        phase=args.phase,stages=ordered,new_BVP=False,Node_workers=0)),flush=True)
    if args.prepare_only:return
    results=[];failure=None
    try:
        for name in ordered:
            results.append(stage(topic,prefix,name,commands[name],env))
        if args.phase in ("all","freeze"):
            result=read(Path(str(fixed_path)+"-report.json"))
            if (result.get("original_parameter_count")!=27 or result.get("fixed_parameter_count")!=24
                    or result.get("counters")!=dict(raw_restorations=1,residual_checks=1,tail_start_attempts=0)):
                raise ValueError("The real fixed-view verification did not record the intended layout change")
        if args.phase in ("all","response"):
            response_path=Path(str(prefix)+"-response.json")
            result=read(response_path)
            if not result.get("finished"):
                raise ValueError("The original complete fixed-response finish marker is absent")
            # Preserve the full original derivative record; this small view
            # makes the actual scientific decision fields readable without
            # transferring large source-transform dictionaries through an API.
            brief_keys=(
                "schema","finished","inspection_only","new_solution","tail_worker_started",
                "fields","baseline","modes","angular","nodes","external_responses",
                "physical_core_parameter_scales","low_three_core_by_physical_control",
                "control_order","half_step_low_three_core_by_physical_control",
                "low_exchange_condition","prescribed_low_core_responses",
                "additional_core_held_directions","tangent_arrays",
                "radial_batch_size","collocation_batch_size",
                "jacobian_seconds","factor_seconds","seconds","peak_rss_kib","counters",
                "field_parameter_layout","limitations")
            brief={key:result[key] for key in brief_keys if key in result}
            brief["original_response"]=check(response_path)
            brief["scope"]="Exact selected terminal fields from the completed original full-field derivative. No new computation or nonlinear acceptance."
            brief["original_response_not_rewritten"]=True
            brief["disk_backward_checks"]=result.get("disk_block_storage",{}).get("stats")
            if len((json.dumps(brief,indent=2,allow_nan=False)+"\n").encode())>=100000:
                raise ValueError("Selected actual response brief exceeded100KB")
            write(Path(str(prefix)+"-response-brief.json"),brief)
    except BaseException as error:
        failure=dict(type=type(error).__name__,message=str(error))
        raise
    finally:
        terminal=dict(scope=__doc__,finished_utc=utc(),phase=args.phase,stages=results,
            failure=failure,postaccept_stages_complete=failure is None,
            new_nonlinear_solution=False,complete_topic_acceptance=False)
        write(Path(str(prefix)+"-terminal.json"),terminal)
        files=[]
        for path in sorted(prefix.parent.glob(prefix.name+"*")):
            if path.is_file() and ".tmp-" not in path.name:
                row=check(path);row["path"]=str(path.relative_to(topic));files.append(row)
        write(Path(str(prefix)+"-stable-files.json"),dict(scope=__doc__,files=files,
            mathematical_status="representation check and derivative only",
            complete_topic_acceptance=False))


if __name__=="__main__":
    main()
