#!/usr/bin/env python3
"""Publish Run48 science and every scheduled README check on the fetched main."""
from __future__ import annotations
import argparse
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

def handoff_marker(base,note,run_number,mark):
    previous = blob_at(base,HANDOFF)
    lines = previous.splitlines(keepends=True)
    if sum(line.startswith(mark) for line in lines)>1:
        raise ValueError("Duplicate scientific run handoff marker")
    other = b"".join(line for line in lines if not line.startswith(mark))
    if other and not other.endswith(b"\n"):
        other += b"\n"
    for label in (str(run_number)+" [实测](notes/"+Path(note).name+") ",str(run_number)+" "):
        new = other+mark+(label+"双README真pull "+base+"\n").encode()
        if len(new)<10000:
            return previous,new
    return previous,None


def scalar_packet(path):
    with path.open("rb") as handle:
        size=os.fstat(handle.fileno()).st_size
        if size>=PUBLIC_TEXT_LIMIT:
            from hashlib import sha256
            h=sha256()
            for part in iter(lambda:handle.read(1<<20),b""):
                h.update(part)
            return dict(path=str(path),bytes=size,sha256=h.hexdigest()),None
        raw=handle.read()
    stat=dict(path=str(path),bytes=len(raw),sha256=sha(raw))
    obj=json.loads(raw)
    json.dumps(obj,allow_nan=False)
    return stat, raw


def scientific_documents(value, note):
    """Take immutable per-call byte snapshots. A phase mesh or coordinate array never enters git."""
    directory=Path(value["command"][-1])
    documents={}
    records={}
    base_note=note[:-5]
    summary=directory/"summary.json"
    phase_index=directory/"closed-geometry-index.json"
    tube_index=directory/"tube-reference"/"closed-geometry-index.json"
    for name,path in (("summary",summary),("geometry",phase_index),("tube-reference-geometry",tube_index)):
        if not path.is_file():
            continue
        stat,raw=scalar_packet(path)
        records[name]=dict(file=stat)
        if raw is None:
            records[name]["scope"]="immutable whole runner file identity; scientific-source stage documents carry the individual finite returns"
            continue
        git_path=base_note+"-"+name+".json"
        documents[git_path]=raw
        records[name]["public_path"]=git_path
        if name=="summary":
            obj=json.loads(raw)
            records[name]["stage_count"]=len(obj.get("stages",[]))
            records[name]["status"]=obj.get("status")
    for path in sorted(directory.glob("stage-*-return.json")):
        stat,raw=scalar_packet(path)
        key=path.stem
        records[key]=dict(file=stat)
        if raw is not None:
            git_path=base_note+"-"+path.name
            documents[git_path]=raw
            records[key]["public_path"]=git_path
    return records,documents


READ_SINCE_PUBLICATION=[]


def publish(value, note):
    """Publish the original small scientific documents and the parent observation on one current base."""
    logical=dict(value)
    records,documents=scientific_documents(value,note)
    logical["scientific_documents"]=records
    if logical.get("scientific_summary") is not None:
        logical["scientific_summary"]=(records.get("summary") or
                                        {"file":logical["scientific_summary"]["file"]})
    owned=set(documents)|{HANDOFF,note}
    body=None
    while True:
        base=checked_pull(note,body)
        READ_SINCE_PUBLICATION.append([timestamp(),base])
        logical["readme_pulls_this_publication"]=list(READ_SINCE_PUBLICATION)
        logical["latest_checked_readme_commit"]=base
        if value["phase"]=="readme-maintenance":
            value["latest_periodic_readme_checked_commit"]=base
            logical["latest_periodic_readme_checked_commit"]=base
        body=(json.dumps(logical,ensure_ascii=False,separators=(",",":"),allow_nan=False)+"\n").encode()
        if len(body)>=PUBLIC_TEXT_LIMIT:
            fields=logical.get("whole_runner_field_files")
            if isinstance(fields,dict):
                logical["whole_runner_field_files"]={k:v for k,v in fields.items() if k!="complete_file_records"}
            body=(json.dumps(logical,ensure_ascii=False,separators=(",",":"),allow_nan=False)+"\n").encode()
        if len(body)>=PUBLIC_TEXT_LIMIT:
            raise ValueError("Scientific attempt observation exceeds the small-file ceiling")
        documents[note]=body
        old_h,new_h=handoff_marker(base,note,value["run_number"],value["handoff_marker"].encode("ascii"))
        previous={p:optional_blob(base,p) for p in documents}
        if previous[note] is not None:
            old=json.loads(previous[note])
            keys=("run","attempt","source_commit","command_identity_sha256")
            if any(old.get(k)!=value.get(k) for k in keys):
                raise RuntimeError("A foreign attempt owns this immutable run path")
            if old.get("terminal"):
                prior={k:v for k,v in old.items() if k not in ("readme_pulls_this_publication","latest_checked_readme_commit")}
                current={k:v for k,v in logical.items() if k not in ("readme_pulls_this_publication","latest_checked_readme_commit")}
                if prior==current:
                    READ_SINCE_PUBLICATION.clear()
                    return True
                raise RuntimeError("A returned terminal record cannot be replaced by later progress")
        for p,data in documents.items():
            if p not in (note,note[:-5]+"-summary.json") and previous[p] not in (data,None):
                raise ValueError("Independent stage or extracted terminal index changed at "+p)
        topic_size=complete_tree_bytes(revision(base+":"+TOPIC))
        planned=topic_size+sum(len(data)-len(previous[p] or b"") for p,data in documents.items())
        planned+=0 if new_h is None else len(new_h)-len(old_h)
        if new_h is None or planned>LIMIT:
            print(json.dumps(dict(publish_deferred=True,actual_topic_bytes=topic_size,
                planned_bytes=planned,readme_commit=base,note=note)),flush=True)
            return False
        local=revision("HEAD")!=base
        if local:
            changed=set(git("diff","--name-only",base,"HEAD").stdout.decode().splitlines())
            if not changed.issubset(owned) or git("rev-list","--count",base+"..HEAD").stdout.strip()!=b"1":
                raise RuntimeError("Unexpected local change outside this attempt's scientific documents")
        Path(HANDOFF).write_bytes(new_h)
        for p,data in documents.items():
            Path(p).parent.mkdir(parents=True,exist_ok=True)
            Path(p).write_bytes(data)
        git("add","--",HANDOFF,*documents)
        rc=git("diff","--cached","--quiet",check=False).returncode
        if rc==1:
            if local:
                git("commit","--amend","--no-edit")
            else:
                git("commit","-m","Record run"+str(value["run_number"])+" "+value["phase"])
        elif rc!=0:
            raise RuntimeError("The scientific publication index is unreadable")
        elif not local:
            READ_SINCE_PUBLICATION.clear()
            return True
        p=git("-c","credential.helper=","-c","credential.helper="+CREDENTIAL,
              "push","origin","HEAD:refs/heads/main",check=False)
        if p.returncode==0:
            READ_SINCE_PUBLICATION.clear()
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
    prefix=request["attempt_note_prefix"]
    note=TOPIC+"/notes/"+prefix+"-"+run+"-"+attempt+".json"
    work=Path(os.environ["RUNNER_TEMP"])/(prefix+"-"+run+"-"+attempt)
    work.mkdir()
    frozen=work/"source"
    out=work/"field"
    script=frozen/request["scientific_inputs"]["script"]["path"]
    params=frozen/request["scientific_inputs"]["parameters"]["path"]
    command=[sys.executable,"-u",str(script),"--params",str(params)]
    for flag,role in request["scientific_path_arguments"]:
        command.extend([flag,str(frozen/request["scientific_inputs"][role]["path"])])
    command.extend(["--out",str(out)])
    contract=json.dumps(dict(commit=trigger,inputs=request["scientific_inputs"],argv=command),
        sort_keys=True,separators=(",",":"),allow_nan=False).encode()
    git("config","user.name","math-research Actions")
    git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
    base=checked_pull()
    READ_SINCE_PUBLICATION.append([timestamp(),base])
    value=dict(schema=request["actual_observation_schema"],run_number=request["run_number"],
        handoff_marker=request["handoff_marker"],
        run=run,attempt=attempt,source_commit=trigger,initial_readme_checked_commit=base,
        command_identity_sha256=sha(contract),request=dict(path=request_relative,bytes=len(request_raw),sha256=sha(request_raw)),
        scientific_inputs=request["scientific_inputs"],actual_frozen_inputs=None,
        command=command,runner_scope="public ubuntu-latest 4 vCPU 16 GB",python=sys.version,
        machine=platform.machine(),system=platform.platform(),actual_logical_cpu_count=os.cpu_count(),
        actual_cpu_affinity=(sorted(os.sched_getaffinity(0)) if hasattr(os,"sched_getaffinity") else None),
        setup_python_step=setup_conclusion,
        run_started_utc=timestamp(),phase="initialization",terminal=False,child_started=False,
        child_pid=None,child_returncode=None,latest_observed_scalar_line=None,scientific_summary=None,
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
        package_names=[spec.split("==",1)[0] for spec in request["dependencies"]]
        value["actual_numeric_versions"]={name:version(name) for name in package_names}
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
            if now-last_sync>=request["readme_pull_period_seconds"]:
                value.update(phase="readme-maintenance",observed_utc=timestamp())
                if publish_live(value,note):
                    last_sync=time.monotonic()
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
                    "terminal record cannot be replaced","Duplicate scientific run","Unexpected local change")):
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
