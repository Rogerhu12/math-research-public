#!/usr/bin/env python3
"""Own one complete Pruefer-current-C/R300 full453 BVP process tree and resource scope.

This is transport/resource control, not a mathematical acceptance test.
The fixed original solve's 17 trials/eight outers and native32/10 are untouched.
One live owner must remain alive from first actual-H response through FD,
all original outer calls, and fresh final audit. No intermediate split/restart.
Author: AI, 2026-11-15. Raw remains temporary until complete actual readback.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time

REPO="Rogerhu12/math-research-public"
SCHEMA="current-C-pruefer-R300-full453-owned-process-launch-v1"
RECIPE_SCHEMA="explicit-current-C-pruefer-R300-v3-three-active-complete453-recipe-v1"
DRIVER="geometry_20261115_current_C_pruefer_full453_physical_dn.py"
DRIVER_SHA="0adff5e96cbd773dc78cf22252705f850a49240a88eb4a3df7b6bcb4bb264875"

def actions():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPO:
        raise RuntimeError("Current science and resource control belong to this public repository Actions")

def sha(raw):return hashlib.sha256(raw).hexdigest()

def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()

def receipt(path):
    path=Path(path);h=hashlib.sha256();n=0
    with path.open("rb") as stream:
        while block:=stream.read(1048576):h.update(block);n+=len(block)
    return dict(file=str(path),bytes=n,sha256=h.hexdigest())

def read(path,expected=None):
    raw=Path(path).read_bytes()
    if expected is not None and sha(raw)!=expected:raise ValueError("Actual input bytes differ: "+str(path))
    return json.loads(raw),dict(file=str(path),bytes=len(raw),sha256=sha(raw))

def write(path,value):
    raw=canonical(value)
    with Path(path).open("wb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    return dict(file=Path(path).name,bytes=len(raw),sha256=sha(raw))

def live_group(group):
    """Inspect only this launched Linux process group; zombies do not write."""
    for path in Path("/proc").iterdir():
        if not path.name.isdigit():continue
        try:
            if os.getpgid(int(path.name))!=group:continue
            if (path/"stat").read_text().rsplit(")",1)[1].split()[0]!="Z":return True
        except (ProcessLookupError,FileNotFoundError):continue
    return False

def signal_owned_group(group,kind):
    try:os.killpg(group,kind)
    except ProcessLookupError:pass

def stop_owned_group(process,external_signals=()):
    present=live_group(process.pid)
    if present:
        signal_owned_group(process.pid,signal.SIGTERM)
        until=time.monotonic()+(2 if external_signals else 30)
        while live_group(process.pid) and time.monotonic()<until:
            if external_signals:until=min(until,time.monotonic()+2)
            time.sleep(.1 if external_signals else .2)
        if live_group(process.pid):
            signal_owned_group(process.pid,signal.SIGKILL)
            until=time.monotonic()+(2 if external_signals else 10)
            while live_group(process.pid) and time.monotonic()<until:
                if external_signals:until=min(until,time.monotonic()+2)
                time.sleep(.1 if external_signals else .2)
    if process.poll() is None:
        try:process.wait(timeout=1 if external_signals else 5)
        except subprocess.TimeoutExpired:pass
    return dict(owned_group_shutdown_attempted=True,
        descendants_remained_after_main_wait=present,
        actual_child_exit=process.returncode,
        owned_group_quiescent_before_readback=not live_group(process.pid))

def main(argv=None):
    actions()
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("recipe","accepted","complete-seed","factory-directory","tail-config",
                "tail-source-root","computations","out"):
        p.add_argument("--"+key,type=Path,required=True)
    for key in ("recipe-sha256","accepted-sha256","factory-result-sha256","tail-config-sha256"):
        p.add_argument("--"+key,required=True)
    p.add_argument("--job-deadline",type=Path,required=True)
    args=p.parse_args(argv)
    tmp=Path(os.environ["RUNNER_TEMP"]).resolve();out=args.out.resolve()
    if out==tmp or tmp not in out.parents or out.exists():
        raise ValueError("Use a fresh, exclusive current request directory under actual RUNNER_TEMP")
    for key in ("recipe","accepted","complete_seed","factory_directory","tail_config","tail_source_root","computations"):
        original=getattr(args,key).resolve()
        if original==out or out in original.parents:
            raise ValueError("The launched owned root must not contain any original input/source")
    recipe,recipe_id=read(args.recipe,args.recipe_sha256)
    deadline,deadline_id=read(args.job_deadline)
    if (deadline.get("schema")!="request184-owned-job-science-deadline-v1"
            or deadline.get("repository")!=REPO
            or deadline.get("run_id")!=os.environ["GITHUB_RUN_ID"]
            or deadline.get("source_commit")!=os.environ["GITHUB_SHA"]
            or deadline.get("recipe_sha256")!=args.recipe_sha256):
        raise ValueError("Use the actual same-job deadline and this complete recipe")
    if recipe.get("schema")!=RECIPE_SCHEMA:raise ValueError("Use the explicit new-C full453 recipe")
    execution=recipe.get("execution",{})
    budget=execution.get("complete_BVP_process_budget_seconds")
    if type(budget) not in (int,float) or not math.isfinite(budget) or budget<=0:
        raise ValueError("One explicit complete-process wall resource budget is required")
    for key in ("minimum_free_bytes_at_start","free_bytes_resource_stop","jac_workers","node_heap_mib"):
        if type(execution.get(key)) is not int or execution[key]<=0:
            raise ValueError("Explicit positive integer resource field required: "+key)
    if execution["free_bytes_resource_stop"]>=execution["minimum_free_bytes_at_start"]:
        raise ValueError("Declare a reserve smaller than the startup free-space resource check")
    if receipt(args.computations/DRIVER)["sha256"]!=DRIVER_SHA:
        raise ValueError("Frozen actual full453 driver source differs")
    total=execution.get("maximum_elapsed_science_seconds_from_namespace")
    reserve=execution.get("readback_reserve_seconds")
    if type(total) is not int or total<=0 or type(reserve) is not int or reserve<=0:
        raise ValueError("Keep the explicit whole-job science deadline and readback reserve")
    if (deadline.get("science_seconds_from_namespace")!=total
            or deadline.get("readback_reserve_seconds")!=reserve
            or type(deadline.get("namespace_created_unix_seconds")) not in (int,float)
            or not math.isfinite(deadline["namespace_created_unix_seconds"])):
        raise ValueError("The actual job clock policy differs from the declared recipe")
    wall_deadline=deadline["namespace_created_unix_seconds"]+total
    out.mkdir(parents=True);started=time.monotonic();process=None;exit_code=2
    report=dict(schema=SCHEMA,source_sha256=receipt(__file__)["sha256"],
        driver=dict(file=DRIVER,sha256=DRIVER_SHA),repository=REPO,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        recipe=recipe_id,actual_child_process_started=False,actual_child_exit=None,
        owned_group_quiescent_before_readback=True,
        completed_driver_return=False,current_finite_BVP_accepted=False,
        resource_stop=None,external_interruption=None,error=None,execution=execution,
        actual_job_deadline=deadline_id,
        job_science_deadline_unix_seconds=wall_deadline,
        wall_deadline_is_resource_scope_not_a_scientific_acceptance_gate=True,
        driver_output_directory="full-BVP",band_factor_directory="banded-work",
        exact_target_or_infinite_DN_or_closed_surface_certified=False,
        no_original_iteration_trial_or_tolerance_changed=True,
        algorithmic_protocol_solve_entry_upper_bound=18,
        upper_bound_is_not_a_call_or_scientific_acceptance_gate=True,
        one_call_capacity_not_claimed_to_cover_complete_multi_call_BVP=True,
        every_owned_raw_file_retained_until_actual_readback=True)
    def status():write(out/"result.json",report)
    class LaunchStopped(Exception):
        """Control flow for a retained startup stop or external interruption."""
    received_signals=[]
    previous_handlers={}
    def external_signal(signum,frame):
        # Do not raise from a Python signal handler: a signal may arrive between
        # Popen returning and assignment of process. Retain the event and let
        # the owned launch/stop path finish acquiring and stopping that group.
        nonlocal exit_code
        received_signals.append(dict(signal_number=int(signum),
            signal_name=signal.Signals(signum).name,
            elapsed_seconds=time.monotonic()-started))
        report["external_interruption"]=dict(kind="external-launcher-signal",
            first_signal_number=received_signals[0]["signal_number"],
            received_signals=received_signals,
            not_a_mathematical_or_wall_resource_rejection=True,
            original_scientific_result_not_inferred=True)
        report["completed_driver_return"]=False
        report["current_finite_BVP_accepted"]=False
        exit_code=128+received_signals[0]["signal_number"]
        # The rule owner escalates after 15 seconds. Forward TERM immediately;
        # the ordinary wait/finally path performs bounded escalation and records
        # whether the owned group is actually quiescent.
        if process is not None:
            try:signal_owned_group(process.pid,signal.SIGTERM)
            except OSError as error:report["external_signal_forward_error"]=repr(error)
    for kind in (signal.SIGTERM,signal.SIGINT):
        previous_handlers[kind]=signal.getsignal(kind)
        signal.signal(kind,external_signal)
    try:
        status()
        if received_signals:raise LaunchStopped()
        disk=shutil.disk_usage(tmp)
        report["actual_initial_disk"]=dict(total=disk.total,used=disk.used,free=disk.free)
        if disk.free<execution["minimum_free_bytes_at_start"]:
            report["resource_stop"]=dict(kind="insufficient-startup-free-storage",
                actual_free=disk.free,declared_required=execution["minimum_free_bytes_at_start"],
                scientific_process_not_started=True)
            exit_code=124
            raise LaunchStopped()
        remaining=wall_deadline-time.time()
        report["actual_seconds_remaining_before_job_science_deadline"]=remaining
        if remaining<=0:
            report["resource_stop"]=dict(kind="job-science-deadline-before-BVP",
                scientific_process_not_started=True,readback_reserve_seconds=reserve)
            exit_code=124
            raise LaunchStopped()
        effective_budget=min(budget,remaining)
        report["actual_complete_BVP_process_budget_seconds"]=effective_budget
        command=[sys.executable,"-u",str(args.computations/DRIVER),
            "--recipe",str(args.recipe),"--recipe-sha256",args.recipe_sha256,
            "--accepted",str(args.accepted),"--accepted-sha256",args.accepted_sha256,
            "--complete-seed",str(args.complete_seed),
            "--factory-directory",str(args.factory_directory),
            "--factory-result-sha256",args.factory_result_sha256,
            "--tail-config",str(args.tail_config),"--tail-config-sha256",args.tail_config_sha256,
            "--tail-source-root",str(args.tail_source_root),
            "--tail-client",str(args.computations/"geometry_20261115_current_C_pruefer_tail_client.py"),
            "--jac-workers",str(execution["jac_workers"]),
            "--node-heap",str(execution["node_heap_mib"]),
            "--out",str(out/"full-BVP"),"--work",str(out/"banded-work")]
        report.update(command=command,shell=False,new_process_group=True,
            actual_input_files=dict(recipe=recipe_id,accepted=receipt(args.accepted),
                complete_seed=receipt(args.complete_seed),
                factory_result=receipt(args.factory_directory/"result.json"),
                current_native_config=receipt(args.tail_config)))
        status()
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",PYTHONUNBUFFERED="1")
        for key in ("GITHUB_TOKEN","GH_TOKEN","MR_TOKEN"):env.pop(key,None)
        stdout=out/"full-BVP.stdout.log";stderr=out/"full-BVP.stderr.log"
        with stdout.open("xb") as so,stderr.open("xb") as se:
            if received_signals:raise LaunchStopped()
            process=subprocess.Popen(command,cwd=args.computations,env=env,
                stdout=so,stderr=se,shell=False,start_new_session=True)
            report.update(actual_child_process_started=True,owned_process_group=process.pid,
                owned_group_quiescent_before_readback=False)
            status();child_started=time.monotonic();last_disk=child_started
            try:
                while process.poll() is None:
                    if received_signals:break
                    now=time.monotonic()
                    if now-child_started>=effective_budget:
                        report["resource_stop"]=dict(kind="complete-BVP-wall-resource-budget",
                            elapsed_seconds=now-child_started,declared_process_seconds=budget,
                            actual_process_seconds=effective_budget,
                            job_science_deadline_unix_seconds=wall_deadline,
                            actual_scientific_result_not_inferred_from_resource_stop=True)
                        break
                    if now-last_disk>=5:
                        free=shutil.disk_usage(tmp).free;last_disk=now
                        report["latest_observed_free_bytes"]=free
                        if free<execution["free_bytes_resource_stop"]:
                            report["resource_stop"]=dict(kind="complete-BVP-free-storage-reserve",
                                actual_free=free,declared_reserve=execution["free_bytes_resource_stop"],
                                actual_scientific_result_not_inferred_from_resource_stop=True)
                            break
                    try:process.wait(timeout=min(1,max(.01,effective_budget-(now-child_started))))
                    except subprocess.TimeoutExpired:pass
            finally:
                report.update(stop_owned_group(process,received_signals))
                so.flush();os.fsync(so.fileno());se.flush();os.fsync(se.fileno())
            if received_signals:
                report["stdout_raw_file"]=str(stdout);report["stderr_raw_file"]=str(stderr)
                report["complete_log_identity_deferred_to_original_reader"]=True
                raise LaunchStopped()
            report["stdout"]=receipt(stdout);report["stderr"]=receipt(stderr)
        if received_signals:raise LaunchStopped()
        path=out/"full-BVP"/"adapter-status.json"
        if path.is_file():
            try:
                actual,original=read(path)
                report["actual_adapter_status"]=original
                report["actual_adapter_scope"]={key:actual.get(key) for key in (
                    "schema","source_sha256","phase","success","new_coupled_finite_acceptance",
                    "original_full_DN_phase","original_full_DN_exit_status",
                    "original_boundary_FD_passed","maximum_boundary_FD_relative_error",
                    "exception","native_owner_closed","native_owner_close_exception")}
                report["current_finite_BVP_accepted"]=(
                    actual.get("new_coupled_finite_acceptance") is True
                    and actual.get("success") is True and report["actual_child_exit"]==0
                    and report["resource_stop"] is None
                    and report["external_interruption"] is None
                    and report["owned_group_quiescent_before_readback"] is True)
            except Exception as error:
                report["adapter_status_parse_error"]=dict(type=type(error).__name__,message=str(error),
                    complete_raw_retained_for_reader=True,actual_file=receipt(path))
        report["completed_driver_return"]=(report["actual_child_exit"]==0
            and report["resource_stop"] is None
            and report["external_interruption"] is None
            and report["owned_group_quiescent_before_readback"] is True)
        if received_signals:exit_code=128+received_signals[0]["signal_number"]
        elif report["resource_stop"] is not None:exit_code=124
        elif report["completed_driver_return"]:exit_code=0
        else:exit_code=2
    except LaunchStopped:
        pass
    except Exception as error:
        report["error"]=dict(type=type(error).__name__,message=str(error),
            actual_science_failure_cause_not_inferred=True)
        if process is not None:
            try:report.update(stop_owned_group(process,received_signals))
            except Exception as failure:
                report["owned_group_shutdown_error"]=repr(failure)
                report["owned_group_quiescent_before_readback"]=False
    finally:
        try:
            if received_signals:
                # Also cover interruption after child launch but before the
                # inner wait/finally is entered. Stop only this child's group.
                if (process is not None
                        and report["owned_group_quiescent_before_readback"] is not True
                        and report.get("owned_group_shutdown_attempted") is not True):
                    try:report.update(stop_owned_group(process,received_signals))
                    except Exception as failure:
                        report["owned_group_shutdown_error"]=repr(failure)
                        report["owned_group_quiescent_before_readback"]=False
                report["completed_driver_return"]=False
                report["current_finite_BVP_accepted"]=False
                exit_code=128+received_signals[0]["signal_number"]
            if process is None:report["owned_group_quiescent_before_readback"]=True
            report["elapsed_seconds"]=time.monotonic()-started
            report["cleanup_authorized_only_after_complete_scalar_readback_and_quiescence"]=True
            original=write(out/"result.json",report)
            print(json.dumps(dict(event="current-C-full453-owned-launch-returned",
                original_result=original,actual_child_exit=report["actual_child_exit"],
                completed_driver_return=report["completed_driver_return"],
                current_finite_BVP_accepted=report["current_finite_BVP_accepted"],
                resource_stop=report["resource_stop"],
                external_interruption=report["external_interruption"],
                error=report["error"]),allow_nan=False),flush=True)
        finally:
            for kind,previous in previous_handlers.items():signal.signal(kind,previous)
    return exit_code

if __name__=="__main__":
    raise SystemExit(main())
