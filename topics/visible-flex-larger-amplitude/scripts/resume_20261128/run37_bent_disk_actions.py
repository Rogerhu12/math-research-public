#!/usr/bin/env python3
"""Replay the full original disk search, then run the finite-amplitude arclength continuation."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time
import traceback

from run36_bent_disk_actions import (
    CREDENTIAL, HANDOFF, LIMIT, REPOSITORY, TOPIC, LiveLog, PUBLIC_TEXT_LIMIT, blob_at,
    checked_pull, collect_fields, complete_tree_bytes, file_info, freeze_source, git, observation,
    optional_blob, revision, sha, timestamp,
)

MARK=b"<!--run37-bent-disk-arclength-->"


def handoff_marker(base,note):
    previous = blob_at(base,HANDOFF)
    lines = previous.splitlines(keepends=True)
    if sum(line.startswith(MARK) for line in lines)>1:
        raise ValueError("Duplicate run37 handoff marker")
    other = b"".join(line for line in lines if not line.startswith(MARK))
    if other and not other.endswith(b"\n"):
        other += b"\n"
    for label in ("37 [实测](notes/"+Path(note).name+") ","37 "):
        new = other+MARK+(label+"双README真pull "+base+"\n").encode()
        if len(new)<10000:
            return previous,new
    return previous,None


def publish(value, note):
    """Ordinary pull/rebase before every write. Replace only this attempt's compact current note."""
    body = (json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+"\n").encode()
    if len(body)>=PUBLIC_TEXT_LIMIT:
        logical=dict(value)
        fields=value.get("whole_runner_field_files")
        if isinstance(fields,dict):
            logical["whole_runner_field_files"]={k:v for k,v in fields.items() if k!="complete_file_records"}
        logical.pop("returned_terminal_log_lines",None)
        body=(json.dumps(logical,ensure_ascii=False,separators=(",",":"),allow_nan=False)+"\n").encode()
        if len(body)>=PUBLIC_TEXT_LIMIT and value.get("scientific_summary") is not None:
            logical["scientific_summary"]=dict(file=value["scientific_summary"]["file"],
                reason="whole result exceeds repository public text limit even with compact encoding")
            body=(json.dumps(logical,ensure_ascii=False,separators=(",",":"),allow_nan=False)+"\n").encode()
    if len(body)>=PUBLIC_TEXT_LIMIT:
        raise ValueError("The complete logical inventory identity does not fit the public text contract")
    while True:
        base=checked_pull(note,body)
        old_h,new_h=handoff_marker(base,note)
        previous=optional_blob(base,note)
        if previous is not None:
            old=json.loads(previous)
            keys=("run","attempt","source_commit","command_identity_sha256")
            if any(old.get(k)!=value.get(k) for k in keys):
                raise RuntimeError("A foreign attempt owns this immutable run path")
            if old.get("terminal") and previous!=body:
                raise RuntimeError("A returned terminal record cannot be replaced by later progress")
        topic_size=complete_tree_bytes(revision(base+":"+TOPIC))
        planned=topic_size+len(body)-len(previous or b"")+(0 if new_h is None else len(new_h)-len(old_h))
        if new_h is None or planned>LIMIT:
            print(json.dumps(dict(publish_deferred=True,actual_topic_bytes=topic_size,
                planned_bytes=planned,readme_commit=base,note=note)),flush=True)
            return False
        local=revision("HEAD")!=base
        if local:
            changed=set(git("diff","--name-only",base,"HEAD").stdout.decode().splitlines())
            if not changed.issubset({HANDOFF,note}) or git("rev-list","--count",base+"..HEAD").stdout.strip()!=b"1":
                raise RuntimeError("Unexpected local change outside this attempt's note and handoff")
        Path(HANDOFF).write_bytes(new_h)
        Path(note).parent.mkdir(parents=True,exist_ok=True)
        Path(note).write_bytes(body)
        git("add","--",HANDOFF,note)
        rc=git("diff","--cached","--quiet",check=False).returncode
        if rc==1:
            if local:
                git("commit","--amend","--no-edit")
            else:
                git("commit","-m","Record run37 arclength continuation "+value["phase"])
        elif rc!=0:
            raise RuntimeError("The run37 publication index is unreadable")
        elif not local:
            return True
        p=git("-c","credential.helper=","-c","credential.helper="+CREDENTIAL,
              "push","origin","HEAD:refs/heads/main",check=False)
        if p.returncode==0:
            print(json.dumps(dict(published=note,bytes=len(body),sha256=sha(body),
                publication_commit=revision("HEAD"),readme_commit=base,topic_bytes=planned)),flush=True)
            return True
        msg=(p.stdout+p.stderr).decode(errors="replace")
        if not any(s in msg for s in ("non-fast-forward","fetch first","cannot lock ref",
                "remote ref updated","failed to update ref","stale info")):
            raise RuntimeError(msg)
        print("Remote main moved, immediately pulling/rebasing before ordinary push",flush=True)


def publish_live(value,note):
    try:
        return publish(value,note)
    except Exception as error:
        if "Changed README at " in str(error):
            raise
        value["last_live_publication_error"]=dict(utc=timestamp(),type=type(error).__name__,message=str(error))
        print(json.dumps(value["last_live_publication_error"],ensure_ascii=False),flush=True)
        return False


def reproduce_parent(request, frozen, work, env, value, note):
    """Recover the two actual immutable input checkpoints and original summary, preserving replay attribution."""
    import numpy as np
    files=request["scientific_inputs"]
    terminal_path=frozen/files["parent_terminal"]["path"]
    terminal=json.loads(terminal_path.read_bytes())
    parent=request["original_parent"]
    original=terminal["scientific_summary"]
    if (terminal.get("terminal") is not True or terminal.get("child_returncode")!=0
            or terminal.get("run")!=parent["run_id"] or terminal.get("attempt")!=parent["attempt"]
            or terminal.get("source_commit")!=parent["source_commit"] or not isinstance(original["complete_small_json"],dict)):
        raise ValueError("The complete public parent terminal does not describe the original returned field")
    state=original["complete_small_json"]
    exact=(json.dumps(state,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()
    if (len(exact)!=original["file"]["bytes"] or sha(exact)!=original["file"]["sha256"]
            or sha(exact)!=parent["scientific_summary_sha256"]
            or state["source_sha256"]!=files["parent_script"]["sha256"]
            or state["params_sha256"]!=files["parent_parameters"]["sha256"]):
        raise ValueError("The whole original 36 scientific JSON cannot be restored byte for byte")
    selected=work/"original-36-inputs"
    selected.mkdir()
    (selected/"summary.json").write_bytes(exact)
    out=work/"full-36-replay"
    out.mkdir()
    command=[sys.executable,"-u",str(frozen/files["parent_script"]["path"]),
        "--params",str(frozen/files["parent_parameters"]["path"]),"--out",str(out)]
    history=dict(original_scientific_terminal=file_info(terminal_path),
        original_summary_reconstructed_byte_for_byte=file_info(selected/"summary.json"),
        original_summary_serialization="all original nested JSON values, sorted compact keys and LF, compared with original recorded SHA-256",
        replay_command=command,started_utc=timestamp(),child_returncode=None,
        required_original_points_reproduced=False,stage_reproduction=[],complete_original_budget_and_domain=True)
    value.update(phase="reproducing-complete-36-input",parent_reproduction=history)
    publish_live(value,note)
    child=subprocess.Popen(command,cwd=frozen,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    live=LiveLog(child.stdout,work/"complete-parent-replay-stdout-stderr.log")
    live.thread.start()
    try:
        last_sync=last=time.monotonic()
        while child.poll() is None:
            time.sleep(request["observe_period_seconds"])
            if time.monotonic()-last_sync>=request["readme_pull_period_seconds"]:
                value["latest_periodic_readme_checked_commit"]=checked_pull()
                last_sync=time.monotonic()
            if time.monotonic()-last>=request["live_scalar_publish_period_seconds"]:
                count,line,_=live.sample()
                history.update(actual_scalar_events=count,last_scalar_event=line,
                    current_original_replay_progress=observation(out/"summary.json"))
                publish_live(value,note)
                last=time.monotonic()
    finally:
        if child.poll() is None:
            child.terminate()
            try: child.wait(timeout=15)
            except subprocess.TimeoutExpired:
                child.kill()
                child.wait()
        live.thread.join()
        child.stdout.close()
    if live.error:
        history["replay_stdout_capture_error"]=live.error
    history.pop("current_original_replay_progress",None)
    history.update(child_returncode=child.returncode,returned_utc=timestamp(),
        replay_log=file_info(live.path),whole_replay_summary=file_info(out/"summary.json") if (out/"summary.json").is_file() else None)
    if child.returncode:
        _,_,tail=live.sample()
        history["returned_terminal_log_lines"]=tail
        raise RuntimeError("The complete original 36 source replay returned "+str(child.returncode))
    replay=json.loads((out/"summary.json").read_bytes())
    history["replay_observation"]=dict(status=replay.get("status"),elapsed_seconds=replay.get("elapsed_seconds"),
        selected_design=replay.get("selected_design"),selected_coarse_stage=replay.get("selected_coarse_stage"),
        last_stage=replay.get("last_stage"),stages=[{k:s.get(k) for k in ("stage","design","nfev","njev",
            "x_shape","x_sha256","fixed_angular_target_sha256")} for s in replay.get("stages",[])])
    if replay.get("status")!="completed_finite_design_and_two_fixed_target_resolutions" or len(replay["stages"])!=len(state["stages"]):
        raise ValueError("The parent replay did not finish its full original program")
    inventory=terminal["whole_runner_field_files"]["complete_file_records"]
    artifacts=[]
    for stage in parent["required_stages"]:
        index=stage["ordinal"]
        name="stage-%02d.npz"%index
        saved=state["stages"][index]
        matches=[f for f in inventory if Path(f["path"]).name==name]
        if (len(matches)!=1 or matches[0]["sha256"]!=stage["npz_sha256"]
                or matches[0]["bytes"]!=stage["npz_bytes"] or saved["stage"]!=index
                or saved["x_sha256"]!=stage["x_sha256"] or saved["x_shape"]!=stage["shape"]):
            raise ValueError("The original whole return disagrees on the required seed "+name)
        source=out/name
        actual=file_info(source)
        with np.load(source,allow_pickle=False) as words:
            if set(words.files)!={"coefficients","target_nodes"}:
                raise ValueError("The original two-member checkpoint layout changed for "+name)
            coefficients=words["coefficients"]
            digest=sha(np.ascontiguousarray(coefficients,dtype="<f8").tobytes(order="C"))
            shape=list(coefficients.shape)
            dtype=str(coefficients.dtype)
        actual_stage=replay["stages"][index]
        equal=(digest==stage["x_sha256"] and shape==stage["shape"] and dtype=="float64"
            and actual["bytes"]==stage["npz_bytes"] and actual["sha256"]==stage["npz_sha256"]
            and actual_stage["x_sha256"]==digest and actual_stage["design"]==saved["design"]
            and actual_stage["configuration"]==saved["configuration"])
        history["stage_reproduction"].append(dict(ordinal=index,complete_original_file=matches[0],
            complete_replayed_file=actual,original_x_sha256=stage["x_sha256"],actual_x_sha256=digest,
            actual_shape=shape,actual_dtype=dtype,original_nfev=saved["nfev"],replayed_nfev=actual_stage["nfev"],
            actual_complete_file_and_coefficient_words_match=equal))
        artifacts.append((name,source,equal))
    differing=[name for name,source,equal in artifacts if not equal]
    if differing:
        raise ValueError("The complete public replay differs on actual original inputs: "+", ".join(differing))
    for name,source,equal in artifacts:
        os.link(source,selected/name)
    history["required_original_points_reproduced"]=True
    value["phase"]="complete-original-inputs-returned"
    publish_live(value,note)
    return selected


def supervise(request_path,setup_conclusion):
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise RuntimeError("This scientific entry runs on the designated public GitHub Actions repository")
    repo=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    os.chdir(repo)
    trigger=os.environ["GITHUB_SHA"]
    revision(trigger+"^{commit}")
    request_relative=str(request_path.resolve().relative_to(repo))
    request_raw=blob_at(trigger,request_relative)
    request=json.loads(request_raw)
    run,attempt=os.environ["GITHUB_RUN_ID"],os.environ["GITHUB_RUN_ATTEMPT"]
    note=TOPIC+"/notes/run37-bent-disk-arclength-"+run+"-"+attempt+".json"
    work=Path(os.environ["RUNNER_TEMP"])/("run37-bent-disk-arclength-"+run+"-"+attempt)
    work.mkdir()
    frozen=work/"source"
    out=work/"field"
    script=frozen/request["scientific_inputs"]["script"]["path"]
    params=frozen/request["scientific_inputs"]["parameters"]["path"]
    parent_parameters=frozen/request["scientific_inputs"]["parent_parameters"]["path"]
    ellipse_source=frozen/request["scientific_inputs"]["ellipse_source"]["path"]
    command=[sys.executable,"-u",str(script),"--params",str(params),
        "--parent-params",str(parent_parameters),"--parent-dir",str(work/"original-36-inputs"),
        "--ellipse-source",str(ellipse_source),"--out",str(out)]
    contract=json.dumps(dict(commit=trigger,inputs=request["scientific_inputs"],original_parent=request["original_parent"],argv=command),
        sort_keys=True,separators=(",",":"),allow_nan=False).encode()
    git("config","user.name","math-research Actions")
    git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
    base=checked_pull()
    value=dict(schema="visible-larger-run37-actual-arclength-continuation-v1",
        run=run,attempt=attempt,source_commit=trigger,initial_readme_checked_commit=base,
        command_identity_sha256=sha(contract),request=dict(path=request_relative,bytes=len(request_raw),sha256=sha(request_raw)),
        scientific_inputs=request["scientific_inputs"],actual_frozen_inputs=None,
        command=command,runner_scope="public ubuntu-latest 4 vCPU 16 GB",python=sys.version,
        machine=platform.machine(),system=platform.platform(),actual_logical_cpu_count=os.cpu_count(),
        actual_cpu_affinity=(sorted(os.sched_getaffinity(0)) if hasattr(os,"sched_getaffinity") else None),
        setup_python_step=setup_conclusion,
        run_started_utc=timestamp(),phase="initialization",terminal=False,child_started=False,
        parent_reproduction=None,child_pid=None,child_returncode=None,latest_observed_scalar_line=None,scientific_summary=None,
        whole_runner_field_files=None,scientific_sampled_success_inferred_by_launcher=False,
        exact_metric_or_global_geometry_inferred_by_launcher=False)
    process=None
    stdout=None
    last_summary=None
    completed_stages=0
    last_status=None
    observed=0
    last_publish=0.
    last_sync=time.monotonic()
    try:
        value["actual_frozen_inputs"]=freeze_source(trigger,frozen,request["scientific_inputs"])
        if setup_conclusion!="success":
            raise RuntimeError("The pinned Python setup returned "+setup_conclusion)
        env=dict(os.environ)
        for key in ("GITHUB_TOKEN","GH_TOKEN","ACTIONS_RUNTIME_TOKEN","ACTIONS_ID_TOKEN_REQUEST_TOKEN"):
            env.pop(key,None)
        env.update(request["scientific_environment"])
        env["GITHUB_WORKSPACE"]=str(frozen)
        install=[sys.executable,"-m","pip","install","--disable-pip-version-check","--no-input",
            "--only-binary=:all:",*request["dependencies"]]
        value.update(phase="installing-declared-numerical-dependencies",dependency_command=install)
        publish_live(value,note)
        dependency=subprocess.run(install,cwd=frozen,env=env,check=False)
        value["dependency_returncode"]=dependency.returncode
        if dependency.returncode:
            raise RuntimeError("Pinned numerical dependency install returned "+str(dependency.returncode))
        from importlib.metadata import version
        value["actual_numeric_versions"]={name:version(name) for name in ("numpy","scipy")}
        reproduce_parent(request,frozen,work,env,value,note)
        out.mkdir()
        value["scientific_environment"] = dict(request["scientific_environment"])
        value["phase"]="scientific-entry"
        process=subprocess.Popen(command,cwd=frozen,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        stdout=LiveLog(process.stdout,work/"complete-scientific-stdout-stderr.log")
        stdout.thread.start()
        value.update(child_started=True,child_pid=process.pid,child_started_utc=timestamp())
        publish_live(value,note)
        last_publish=time.monotonic()
        while process.poll() is None:
            time.sleep(request["observe_period_seconds"])
            now=time.monotonic()
            snap=observation(out/"summary.json")
            digest=snap["file"]["sha256"] if snap else None
            count,line,_=stdout.sample()
            scientific=snap.get("complete_small_json") if snap else None
            stages=scientific.get("stages",[]) if isinstance(scientific,dict) else []
            status=scientific.get("status") if isinstance(scientific,dict) else None
            stage_changed=(digest is not None and digest!=last_summary
                and (len(stages)!=completed_stages or status!=last_status))
            scalar_due=(count!=observed or digest!=last_summary) and now-last_publish>=request["live_scalar_publish_period_seconds"]
            if (stage_changed or scalar_due) and now-last_publish>=request["minimum_publish_retry_seconds"]:
                value.update(phase="candidate-return" if stage_changed else "live-scalar",
                    observed_utc=timestamp(),latest_observed_scalar_line=line,
                    original_scalar_line_count=count,scientific_summary=snap)
                last_publish=now
                if publish_live(value,note):
                    observed,last_summary=count,digest
                    completed_stages,last_status=len(stages),status
                    last_sync=now
            elif now-last_sync>=request["readme_pull_period_seconds"]:
                value["latest_periodic_readme_checked_commit"]=checked_pull()
                last_sync=now
        stdout.thread.join()
        process.stdout.close()
        count,line,tail=stdout.sample()
        value.update(child_returncode=process.returncode,child_returned_utc=timestamp(),
            phase="scientific-return",latest_observed_scalar_line=line,original_scalar_line_count=count,
            scientific_summary=observation(out/"summary.json"),stdout_stderr=file_info(stdout.path),
            whole_runner_field_files=collect_fields(out,work),
            complete_scientific_stdout_and_runner_field_retained=True)
        if process.returncode:
            value["returned_terminal_log_lines"]=tail
        if stdout.error:
            value["stdout_capture_error"]=stdout.error
        if value["scientific_summary"] is None:
            value["scientific_summary_unavailable"]="the child returned without its summary.json"
    except BaseException as error:
        if process is not None and process.poll() is None:
            process.terminate()
            try:process.wait(timeout=15)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
        if stdout is not None:
            stdout.thread.join(timeout=30)
            if stdout.path.exists():value["stdout_stderr"]=file_info(stdout.path)
        value.update(phase="runner-or-entry-error",returned_utc=timestamp(),
            exception=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc()),
            child_returncode=None if process is None else process.returncode,
            scientific_summary=observation(out/"summary.json"),whole_runner_field_files=collect_fields(out,work) if out.exists() else [])
    value["terminal"]=True
    value["final_observed_utc"]=timestamp()
    final_body=(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+"\n").encode()
    (work/"complete-runner-conclusion.json").write_bytes(final_body)
    if len(final_body)<PUBLIC_TEXT_LIMIT:
        print(final_body.decode(),flush=True)
    else:
        print(json.dumps(file_info(work/"complete-runner-conclusion.json")),flush=True)
    while True:
        try:
            if publish(value,note):
                break
        except Exception as error:
            message=str(error)
            if any(reason in message for reason in ("Changed README at ","foreign attempt owns",
                    "terminal record cannot be replaced","Duplicate run37","Unexpected local change")):
                raise
            print(json.dumps(dict(terminal_publication_retry=message,utc=timestamp())),flush=True)
        time.sleep(20)
    rc=value["child_returncode"]
    if rc is not None and rc!=0:
        return rc if rc>=0 else 128-rc
    if value["phase"]=="runner-or-entry-error" or value["scientific_summary"] is None:
        return 1
    return 0


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request",required=True,type=Path)
    parser.add_argument("--setup-conclusion",required=True)
    args=parser.parse_args()
    raise SystemExit(supervise(args.request,args.setup_conclusion))
