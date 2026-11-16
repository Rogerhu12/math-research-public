#!/usr/bin/env python3
"""Request221: real original112 full-DN with one live128 same-H response owner.

Only this public Actions job may restore inputs or execute the unchanged
original full-DN consumer. There is one 19200-second scientific clock.
Every numerical file stays in the one temporary namespace until complete
necessary readback and independently observed process quiescence.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import signal
import subprocess
import sys
import time
import traceback
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
REPO = "Rogerhu12/math-research-public"
SCHEMA = "R508-live128-scoped-original-full112-owned-procedure-v1"
REQUEST_SCHEMA = "public-live128-scoped-original-full112-FD-fullDN-request-v1"
NAMESPACE = "visible-live128-scoped-original-fullDN221"
CLOCK_SCHEMA = "R493-original-full112-live128-job-deadline-v1"
RUN_KEYS = ("GITHUB_REPOSITORY","GITHUB_RUN_ID","GITHUB_RUN_ATTEMPT","GITHUB_SHA")
PROCESS = "geometry_20261116_live128_owned_process.py"
PROCESS_SHA = "1516306f3ead5a5e8b54f389da172ef9544298b13ccf659c390cb874d26ed6a7"
ENTRY = "geometry_20261116_live128_original_full_dn.py"
ENTRY_SHA = "63bbbefcfda8ae5761be314da743afc5291ad1a83749cf6d554003d429f5508e"
RULES = "root_20261114_current576_rules_runner.py"
RULES_SHA = "3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde"
RESUME = "exact_20261114_public_resume.py"
RESUME_SHA = "11399783f01b145ee3f23d88213af368daee9c16dfb858b40dd7316870b300a5"
FETCH = "root_20261115_fetch_native_word_parent91.py"
FETCH_SHA = "98e9044fa23d76484fa864b5b769fc0a38a2f18ef95ca91bf97d88bff3940fb8"
SEED = "geometry_20261116_live128_actual91_seed.py"
SEED_SHA = "219f5f8b26af05c17e596a1534e1fe5390c72ecb895de3b5606505525b8e429a"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True,
                      separators=(",",":"), allow_nan=False).encode("ascii")+b"\n"


def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(1<<20),b""):
            h.update(block)
    return h.hexdigest()


def receipt(path):
    path=Path(path).resolve(strict=True)
    return dict(file=str(path),bytes=path.stat().st_size,sha256=sha(path))


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw)


def write(path,value,*,replace=False):
    path=Path(path)
    if replace:
        temporary=path.with_name(path.name+".tmp")
        temporary.write_bytes(canonical(value))
        temporary.replace(path)
    else:
        with path.open("xb") as stream:
            stream.write(canonical(value))


def run_identity():
    return {key:os.environ.get(key) for key in RUN_KEYS}


def require_actions():
    require(os.environ.get("GITHUB_ACTIONS")=="true"
            and os.environ.get("GITHUB_REPOSITORY")==REPO,
            "This source executes only in the declared public Actions repository")


def checked_source(name,digest):
    path=HERE/name
    require(Path(name).name==name and path.is_file() and not path.is_symlink()
            and sha(path)==digest,"The exact declared source is required: "+name)
    return path


def load_source(name,digest,role):
    path=checked_source(name,digest)
    spec=importlib.util.spec_from_file_location("_R508_"+role,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    return module


def base_path(value,*,exists=True):
    runner=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    supplied=Path(value)
    require(supplied.is_absolute() and ".." not in supplied.parts
            and not supplied.is_symlink(),"Actual absolute temporary namespace")
    base=supplied.resolve(strict=exists)
    require(base.parent==runner and base.name==NAMESPACE,
            "Only this exact request221 namespace is owned")
    return base


def bind(request_path,request_sha,namespace,*,prepared=False):
    require_actions()
    request_path=Path(request_path).resolve(strict=True)
    request=read(request_path)
    require(sha(request_path)==request_sha and request["schema"]==REQUEST_SCHEMA
            and request["request_number"]==221 and request["repository"]==REPO,
            "The actual complete request221 bytes and schema")
    base=base_path(namespace)
    marker=read(base/"ownership.json")
    require(marker["schema"]==SCHEMA and marker["run"]==run_identity()
            and marker["request"]["sha256"]==request_sha
            and marker["namespace"]==str(base),"The one actual owned namespace")
    if prepared:
        preparation=read(base/"preparation.json")
        require(preparation["complete"] is True and preparation["request"]==receipt(request_path),
                "The actual source and original-input preparation must have returned")
    return request,base


def exact_git_input(repo,row,destination,transport_log):
    relative=PurePosixPath(row["path"])
    require(not relative.is_absolute() and ".." not in relative.parts
            and str(relative).startswith("topics/visible-flex-larger-amplitude/"),
            "Explicit existing historical public-topic input path")
    revision=row["commit"]
    require(len(revision)==40 and all(c in "0123456789abcdef" for c in revision),
            "An actual complete historical public commit")
    got=subprocess.run(["git","-C",str(repo),"cat-file","-e",revision+"^{commit}"],
                       stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    if got.returncode:
        with transport_log.open("ab") as log:
            subprocess.run(["git","-C",str(repo),"fetch","--no-tags","--depth=1",
                "--filter=blob:none","origin",revision],stdout=log,stderr=log,check=True)
    actual_blob=subprocess.check_output(
        ["git","-C",str(repo),"rev-parse",revision+":"+str(relative)],text=True).strip()
    require(actual_blob==row["git_blob"],"Actual historical input path/blob identity")
    raw=subprocess.check_output(["git","-C",str(repo),"show",revision+":"+str(relative)])
    require(len(raw)==row["bytes"] and hashlib.sha256(raw).hexdigest()==row["sha256"],
            "Original input bytes and SHA are unchanged: "+relative.name)
    with destination.open("xb") as stream:
        stream.write(raw)
    return dict(declared=row,actual=receipt(destination),no_scientific_recomputation=True)


def prepare(request_path,request_sha,namespace):
    require_actions()
    base=base_path(namespace,exists=False)
    require(not base.exists(),"Use a fresh actual request221 namespace")
    base.mkdir(mode=0o700)
    request_path=Path(request_path).resolve(strict=True)
    request=read(request_path)
    require(sha(request_path)==request_sha and request["schema"]==REQUEST_SCHEMA
            and request["request_number"]==221 and request["repository"]==REPO,
            "The actual independent request221")
    write(base/"ownership.json",dict(schema=SCHEMA,namespace=str(base),
          run=run_identity(),request=receipt(request_path),source=receipt(__file__),
          science_started=False,all_original_raw_temporary=True))
    report=dict(schema=SCHEMA+"-preparation",run=run_identity(),source=receipt(__file__),
        request=receipt(request_path),complete=False,phase="source-binding",error=None,
        verified_sources=[],original_inputs={},children=[],science_evaluated=False)
    write(base/"preparation.json",report)
    try:
        repo=Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
        head=subprocess.check_output(["git","-C",str(repo),"rev-parse","HEAD"],text=True).strip()
        require(head==os.environ["GITHUB_SHA"],"Science checkout retains its actual source head")
        for name,digest in request["source_sha256"].items():
            path=checked_source(name,digest)
            report["verified_sources"].append(dict(file=name,bytes=path.stat().st_size,sha256=digest))
        report["actual_readme_blobs"]={}
        for relative,expected in request["reviewed_README_blobs"].items():
            actual=subprocess.check_output(
                ["git","-C",str(repo),"rev-parse","HEAD:"+relative],text=True).strip()
            require(actual==expected,"Actual source checkout README identity")
            report["actual_readme_blobs"][relative]=actual
        inputs=base/"original-inputs";inputs.mkdir()
        transport=base/"input-restore.log"
        for key,row in request["original_inputs"].items():
            target=inputs/row["runtime_basename"]
            report["original_inputs"][key]=exact_git_input(repo,row,target,transport)
        status_transport=inputs/request["original_inputs"]["warm_status"]["runtime_basename"]
        stored=status_transport.read_bytes()
        status_raw=gzip.decompress(stored) if stored[:2]==b"\x1f\x8b" else stored
        expected=request["actual63"]["decoded_status"]
        require(len(status_raw)==expected["bytes"]
                and hashlib.sha256(status_raw).hexdigest()==expected["sha256"],
                "Actual63 original decoded status bytes, without reserialization")
        status=inputs/"actual63-driver-status.json"
        with status.open("xb") as stream:
            stream.write(status_raw)
        warm_path=inputs/request["original_inputs"]["warm"]["runtime_basename"]
        warm=read(warm_path)
        producer=warm["optimization_warm"]["source_sha256"]
        require(isinstance(producer,dict) and producer,"Actual63 complete producer source ledger")
        report["actual63_producer_sources"]={}
        for name,digest in producer.items():
            require(request["source_sha256"].get(name)==digest,
                    "Actual63 producer is explicitly in the new source closure: "+name)
            checked_source(name,digest)
            report["actual63_producer_sources"][name]=digest
        # This is an explicitly new transport file containing the actual saved
        # warm's complete original port object. It is not an old port-file SHA.
        port=inputs/"actual63-original-port-object.json"
        write(port,warm["complete_scalar_profile"]["complete_original_port"])
        report["original_port_object"]=dict(actual=receipt(port),source=receipt(warm_path),
            source_JSON_pointer="/complete_scalar_profile/complete_original_port",
            complete_JSON_object_preserved=True,original_port_file_bytes_claimed=False)
        report["decoded_status"]=dict(actual=receipt(status),transport=receipt(status_transport),
            original_JSON_reserialized=False)
        report["phase"]="restore-public78-source"
        write(base/"preparation.json",report,replace=True)
        restoration=base/"original-source-restoration";restoration.mkdir()
        resume=load_source(RESUME,RESUME_SHA,"public_source_restoration")
        topic=resume.prepare_public_source(repo,restoration,restoration)
        source_root=topic/"repro"/"source-root"
        require(source_root.is_dir() and source_root.parent.parent==topic,
                "The original client consumes topic/repro/source-root")
        report["original_source_topic"]=str(topic)
        report["original_source_root"]=str(source_root)
        report["original_public_source_preparation"]=receipt(restoration/"public-source-preparation.json")
        report["phase"]="fetch-original91-whole-artifact"
        write(base/"preparation.json",report,replace=True)
        fetch=checked_source(FETCH,FETCH_SHA)
        argv=[sys.executable,"-u",str(fetch)]
        for key in ("run_id","artifact_id","artifact_name","expected_size","expected_sha256"):
            argv+=["--"+key.replace("_","-"),str(request["actual91_artifact"][key])]
        actual91=base/"actual91";argv+=["--out",str(actual91)]
        for label,command in (
            ("actual91-transport",argv),
            ("actual91-seed-binding",[sys.executable,"-u",str(checked_source(SEED,SEED_SHA)),
                 "--actual91-directory",str(actual91),"--out",str(base/"actual91-initial-guess")])):
            record=dict(label=label,command=command,returned=False,actual_exit=None)
            report["children"].append(record)
            write(base/"preparation.json",report,replace=True)
            with (base/(label+".stdout.log")).open("xb") as stdout, (base/(label+".stderr.log")).open("xb") as stderr:
                completed=subprocess.run(command,stdout=stdout,stderr=stderr,check=False)
            record.update(returned=True,actual_exit=completed.returncode,
                stdout=receipt(base/(label+".stdout.log")),stderr=receipt(base/(label+".stderr.log")))
            require(completed.returncode==0,"Actual original-input child failed: "+label)
        seed=base/"actual91-initial-guess"/"seed.json"
        report.update(seed=receipt(seed),phase="complete",complete=True,
            exact_prefix_inputs=dict(accepted=receipt(inputs/request["original_inputs"]["accepted"]["runtime_basename"]),
                warm=receipt(warm_path),warm_status=receipt(status),port=receipt(port),
                tail_config=receipt(inputs/request["original_inputs"]["tail_config"]["runtime_basename"])),
            actual91_is_only_initial_tail_guess=True,actual63_is_only_initial_prefix_warm=True,
            no_completed61_parent_or_old_native_cache=True)
        env_file=os.environ.get("GITHUB_ENV")
        if env_file:
            with open(env_file,"a") as stream:
                stream.write("VISIBLE_FLEX_SOURCE_TOPIC="+str(topic)+"\n")
                stream.write("VISIBLE_FLEX_SOURCE_ROOT="+str(source_root)+"\n")
                stream.write("VISIBLE_SOURCE_TOPIC="+str(topic)+"\n")
                for key,row in request["original_inputs"].items():
                    if row.get("environment"):
                        stream.write(row["environment"]+"="+str(inputs/row["runtime_basename"])+"\n")
        return 0
    except Exception as error:
        report.update(error=dict(type=type(error).__name__,message=str(error),
                                 traceback=traceback.format_exc()))
        return 2
    finally:
        write(base/"preparation.json",report,replace=True)
        print(json.dumps(dict(event="request221_preparation_return",complete=report["complete"],
            phase=report["phase"],error=report["error"],actual=receipt(base/"preparation.json")),
            ensure_ascii=True,allow_nan=False),flush=True)


def registry_paths(base):
    # Only the two explicit original-rule/science registries and actual Node
    # session registries produced by the independently pinned client.
    values=[base/"rules-process.json",base/"science-process.json"]
    values.extend((base/"science"/"full-dn").glob("true-tail_live128/worker-process.json"))
    return [p for p in values if p.is_file()]


def quiet_registries(base, owner):
    records, errors = [], []
    for path in registry_paths(base):
        try:
            actual=path.resolve(strict=True)
            require(actual.is_relative_to(base) and not path.is_symlink(),
                    "Actual registry stays in this namespace")
            record=read(actual)
            target=Path(record["namespace"]).resolve(strict=True)
            wanted=record["worker"]
            require(record["schema"]==owner.SCHEMA and record["run"]==run_identity()
                    and record["source"]["sha256"]==PROCESS_SHA,
                    "Original process source and same-run actual registry")
            require(target.is_relative_to(base) and actual.is_relative_to(target)
                    and wanted["uid"]==os.getuid()
                    and wanted["pid"]==wanted["pgid"]==wanted["sid"]
                    and isinstance(wanted["start_ticks"],int) and wanted["start_ticks"]>=0,
                    "Registered pid/start-time/uid/session/group/namespace")
            records.append(dict(path=actual,record=record,identity=receipt(actual)))
        except Exception as error:
            errors.append(dict(registry=str(path),actual_error_type=type(error).__name__,
                               reason=str(error)))
    return records,errors


def namespace_argument(raw, base):
    prefix=os.fsencode(str(base))
    for argument in raw.split(b"\0"):
        value=argument.split(b"=",1)[-1]
        if value==prefix or value.startswith(prefix+b"/"):
            return True
    return False


def scoped_process_observation(base, owner, registries, seen):
    """A permission boundary: unrelated same-uid processes are not our workers."""
    infos,failures={},{}
    wanted=[row["record"]["worker"] for row in registries]
    registered={row["pid"]:row for row in wanted}
    for path in Path("/proc").iterdir():
        if not path.name.isdecimal() or int(path.name)==os.getpid():
            continue
        pid=int(path.name)
        try:
            info=owner.proc_info(pid)
            if info is None:
                continue
            # Keep stat identities across uid boundaries so a real descendant
            # or registered group cannot disappear merely by changing uid.
            infos[pid]=info
        except FileNotFoundError:
            continue
        except (OSError,ValueError) as error:
            failures[pid]=dict(actual_error_type=type(error).__name__,reason=str(error))
    # Only exact live identities anchor ancestry. A reused numeric pid does not.
    linked={pid for pid,info in infos.items()
            if ((pid in registered and info["start_ticks"]==registered[pid]["start_ticks"])
                or seen.get(pid)==info["start_ticks"])}
    ancestry=set()
    changed=True
    while changed:
        changed=False
        for pid,info in infos.items():
            parent=infos.get(info["ppid"])
            if pid not in linked and parent is not None and parent["pid"] in linked \
                    and parent["start_ticks"]<=info["start_ticks"]:
                linked.add(pid);ancestry.add(pid);changed=True
    live,unknown,zombies,outside=[],[],[],[]
    for pid in sorted(set(infos)|set(failures)):
        info=infos.get(pid)
        path=Path("/proc",str(pid))
        reasons=[]
        if pid in registered:
            reasons.append("registered-pid")
        if pid in seen:
            reasons.append("previously-observed-namespace-or-owned-identity")
        if pid in ancestry:
            reasons.append("actual-observed-descendant")
        group_rows=[]
        if info is not None:
            group_rows=[row for row in registries
                        if info["pgid"]==row["record"]["worker"]["pgid"]
                        or info["sid"]==row["record"]["worker"]["sid"]]
            if group_rows:
                reasons.append("registered-group-or-session")
            if info["state"]=="Z":
                if reasons:
                    zombies.append(dict(actual=info,evidence=reasons,zombie_nonwriting=True))
                continue
            if info["uid"]!=os.getuid() and not reasons:
                continue
        errors=[]
        command_matches=False
        try:
            command_matches=namespace_argument((path/"cmdline").read_bytes(),base)
        except FileNotFoundError:
            continue
        except OSError as error:
            errors.append(dict(member="cmdline",type=type(error).__name__,error=str(error)))
        if command_matches:
            reasons.append("readable-namespace-command-argument")
        environment=None
        try:
            values=(path/"environ").read_bytes().split(b"\0")
            key=(owner.ENV_NAMESPACE+"=").encode()
            environment=[item[len(key):] for item in values if item.startswith(key)]
        except FileNotFoundError:
            continue
        except OSError as error:
            errors.append(dict(member="environ",type=type(error).__name__,error=str(error)))
        prefix=os.fsencode(str(base))
        namespace_matches=environment is not None and any(
            item==prefix or item.startswith(prefix+b"/") for item in environment)
        if namespace_matches:
            reasons.append("readable-owned-namespace-environment")
        if not reasons:
            if errors or pid in failures:
                outside.append(dict(pid=pid,reason="outside-established-ownership-scope",
                    permission_errors=errors,stat_error=failures.get(pid),
                    not_claimed_owned_or_signalled=True,
                    not_a_claim_every_same_uid_process_was_readable=True))
            continue
        if info is None:
            unknown.append(dict(pid=pid,evidence=reasons,stat_error=failures.get(pid),
                                permission_errors=errors,reason="possible-owned-identity-unreadable"))
            continue
        try:
            after=owner.proc_info(pid)
        except (OSError,ValueError) as error:
            unknown.append(dict(actual=info,evidence=reasons,
                reason="possible-owned-identity-recheck-failed",actual_error_type=type(error).__name__,
                error=str(error),permission_errors=errors))
            continue
        if after is None:
            continue
        if any(after[key]!=info[key] for key in ("pid","ppid","pgid","sid","start_ticks","uid")):
            unknown.append(dict(actual=after,previous=info,evidence=reasons,
                                reason="identity-changed-during-observation"))
            continue
        seen[pid]=info["start_ticks"]
        if info["uid"]!=os.getuid() or (pid in registered and
                info["start_ticks"]!=registered[pid]["start_ticks"]):
            unknown.append(dict(actual=info,evidence=reasons,reason="registered-identity-not-the-original"))
            continue
        if errors:
            unknown.append(dict(actual=info,evidence=reasons,permission_errors=errors,
                                reason="actual-or-suspected-owned-process-unreadable"))
            continue
        bound=[]
        for row in group_rows:
            record=row["record"];w=record["worker"]
            if (info["pgid"]==w["pgid"] and info["sid"]==w["sid"]
                    and info["uid"]==w["uid"] and info["start_ticks"]>=w["start_ticks"]
                    and (info["pid"]!=w["pid"] or info["start_ticks"]==w["start_ticks"])
                    and os.fsencode(record["namespace"]) in environment):
                bound.append(w["pgid"])
        live.append(dict(actual=info,evidence=reasons,signalable_registered_groups=bound))
        if not bound:
            unknown.append(dict(actual=info,evidence=reasons,
                                reason="namespace-or-descendant-not-bound-to-a-registered-session"))
    return dict(remaining_owned_processes=live,unknown=unknown,zombie_nonwriting=zombies,
                outside_scope_unreadable=outside)


def quiet(base):
    require_actions();base=base_path(base)
    owner=load_source(PROCESS,PROCESS_SHA,"process_owner")
    outputs=[];seen={};attempted=set();registry_errors=[]
    # Original registration source is unchanged. This outer observation replaces
    # the old unrestricted same-uid-environ rule; it never reads numerical arrays.
    while True:
        registries,errors=quiet_registries(base,owner)
        registry_errors=errors
        pending=[row for row in registries if str(row["path"]) not in attempted]
        if errors or not pending:
            break
        row=pending[0];attempted.add(str(row["path"]))
        wanted=row["record"]["worker"];pgid=wanted["pgid"]
        report=dict(registry=row["identity"],original_worker=wanted,signals=[],
                    observed_before=None,observed_after=None,unknown=[],quiescent=False)
        for sig,grace in ((signal.SIGTERM,15.0),(signal.SIGKILL,15.0)):
            registries,errors=quiet_registries(base,owner)
            observation=scoped_process_observation(base,owner,registries,seen)
            if report["observed_before"] is None:
                report["observed_before"]=observation
            if errors or observation["unknown"]:
                report["unknown"]=errors+observation["unknown"]
                report["reason"]="owned-or-suspected-ownership-unproved-no-signal"
                break
            members=[item for item in observation["remaining_owned_processes"]
                     if item["actual"]["pgid"]==pgid]
            if not members:
                break
            require(all(pgid in item["signalable_registered_groups"] for item in members),
                    "Only the actual original registered group may receive a signal")
            try:
                os.killpg(pgid,sig)
                report["signals"].append(dict(signal=int(sig),members=members))
            except ProcessLookupError:
                pass
            until=time.monotonic()+grace
            while time.monotonic()<until:
                current=scoped_process_observation(base,owner,registries,seen)
                if current["unknown"] or not any(
                        item["actual"]["pgid"]==pgid for item in current["remaining_owned_processes"]):
                    break
                time.sleep(0.1)
        current=scoped_process_observation(base,owner,registries,seen)
        report["observed_after"]=current
        report["unknown"]=registry_errors+current["unknown"]
        report["quiescent"]=not report["unknown"] and not any(
            item["actual"]["pgid"]==pgid for item in current["remaining_owned_processes"])
        outputs.append(report)
    registries,registry_errors=quiet_registries(base,owner)
    current=scoped_process_observation(base,owner,registries,seen)
    unknown=registry_errors+current["unknown"]
    record=dict(schema=SCHEMA+"-quiet",run=run_identity(),namespace=str(base),
        source=receipt(__file__),registries=[row["identity"] for row in registries],
        groups=outputs,remaining_owned_processes=current["remaining_owned_processes"],
        unknown=unknown,zombie_nonwriting=current["zombie_nonwriting"],
        outside_scope_unreadable=current["outside_scope_unreadable"],
        scope="registered-original-identities-groups-sessions-observed-descendants-and-readable-namespace",
        same_uid_alone_does_not_establish_ownership=True,
        unreadable_actual_or_suspected_owned_process_blocks_read_and_delete=True,
        all_same_uid_processes_readable_or_quiescent_not_claimed=True,
        quiescent=not current["remaining_owned_processes"] and not unknown
                  and all(row.get("quiescent") is True for row in outputs),
        no_scientific_acceptance_inferred=True)
    write(base/"quiescence.json",record,replace=True)
    return record

def science(request_path,request_sha,namespace):
    request,base=bind(request_path,request_sha,namespace,prepared=True)
    preparation=read(base/"preparation.json")
    clock=base/"job-deadline.json";deadline=read(clock)
    require(deadline["schema"]==CLOCK_SCHEMA and deadline["run"]==run_identity(),
            "The actual original320-minute clock is already running")
    require(deadline["absolute_monotonic_deadline_ns"]>time.monotonic_ns(),
            "Original scientific clock has remaining time")
    owner=load_source(PROCESS,PROCESS_SHA,"science_process_owner")
    os.environ[owner.ENV_NAMESPACE]=str(base)
    policy=dict(schema="R493-current-H-live128-client-policy-v1",namespace=str(base),
        initial_guess=preparation["seed"],job_deadline=receipt(clock),
        expected_input_config_sha256=request["original_inputs"]["tail_config"]["sha256"],
        factor_parameters=dict(eta_cli_text=request["runtime"]["native_eta"],
            exact_workers=request["runtime"]["native_exact_workers"],
            max_factor_bytes=request["runtime"]["native_max_factor_bytes"]),
        resources=request["live_call_resources"],retain_optional_tangent_predictor=True)
    policy_file=base/"live128-policy.json";write(policy_file,policy)
    command=[sys.executable,"-u",str(checked_source(ENTRY,ENTRY_SHA))]
    for key in ("accepted","warm","warm_status","port","tail_config"):
        command+=["--"+key.replace("_","-"),preparation["exact_prefix_inputs"][key]["file"]]
    for key in ("warm","warm_status"):
        command+=["--"+key.replace("_","-")+"-sha256",preparation["exact_prefix_inputs"][key]["sha256"]]
    command+=["--tail-source-root",preparation["original_source_root"],
        "--live128-policy",str(policy_file),"--live128-policy-sha256",sha(policy_file),
        "--out",str(base/"science"),"--work",str(base/"prefix-work")]
    for key,value in request["runtime"].items():
        command+=["--"+key.replace("_","-"),str(value)]
    # The original rule runner starts this command in a new session. exec
    # preserves this actual pid/start-time/group/environment for the full-DN.
    owner.register(SimpleNamespace(pid=os.getpid()),base,base/"science-process.json",
                   command,receipt(clock))
    write(base/"science-command.json",dict(schema=SCHEMA+"-actual-command",
        command=command,original_rule_runner_started_this_session=True,
        registered_before_same_pid_exec=True,deadline=receipt(clock),
        entry=receipt(HERE/ENTRY),policy=receipt(policy_file)))
    os.execv(sys.executable,command)


def rules(request_path,request_sha,namespace):
    request,base=bind(request_path,request_sha,namespace,prepared=True)
    module=load_source(RULES,RULES_SHA,"original_rules_runner")
    repo=Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
    baselines={}
    for name,expected in request["reviewed_README_blobs"].items():
        raw=(repo/name).read_bytes()
        actual=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
        require(actual==expected,"Actual reviewed README words before original rule runner")
        baselines[name]=dict(blob=actual,text=raw.decode("utf-8"))
    old={name:value["blob"] for name,value in module.BASELINES.items()}
    module.BASELINES=baselines
    write(base/"rules-baseline-update.json",dict(
        schema=SCHEMA+"-explicit-reviewed-rules-baseline",source=receipt(HERE/RULES),
        old_embedded_blobs=old,reviewed_current_blobs=request["reviewed_README_blobs"],
        period_seconds=module.PERIOD_SECONDS,
        original_pull_rebase_rule_change_stop_and_science_command_retained=True))
    command=[sys.executable,"-u",str(Path(__file__).resolve()),"science",
        "--request",str(Path(request_path).resolve()),"--request-sha256",request_sha,
        "--namespace",str(base)]
    sys.argv=[str(HERE/RULES),"--out",str(base/"rules"),"--command",*command]
    return module.main()


def run(request_path,request_sha,namespace):
    request,base=bind(request_path,request_sha,namespace,prepared=True)
    require(not (base/"job-deadline.json").exists(),"No new clock replaces an existing science clock")
    started=time.monotonic_ns()
    deadline=dict(schema=CLOCK_SCHEMA,run=run_identity(),source=receipt(__file__),
        total_seconds=19200,started_monotonic_ns=started,
        absolute_monotonic_deadline_ns=started+19200*10**9,
        readback_cleanup_reserve_seconds=request["resources"]["readback_cleanup_reserve_seconds"],
        original_science_step_minutes=320,original_workflow_job_minutes=350,
        every_H_and_original_FD_fullDN_share_this_clock=True,
        initial_source_input_restoration_finished_before_clock=True)
    write(base/"job-deadline.json",deadline)
    command=[sys.executable,"-u",str(Path(__file__).resolve()),
        "rules","--request",str(Path(request_path).resolve()),"--request-sha256",request_sha,
        "--namespace",str(base)]
    state=dict(schema=SCHEMA+"-execution",run=run_identity(),source=receipt(__file__),
        request=receipt(request_path),deadline=receipt(base/"job-deadline.json"),
        command=command,returned=False,science_returncode=None,rules_returncode=None,
        resource_stop=None,external_signal=None,error=None,all_raw_retained=True)
    write(base/"execution.json",state)
    owner=load_source(PROCESS,PROCESS_SHA,"launcher_process_owner")
    signals=[]
    previous={sig:signal.getsignal(sig) for sig in (signal.SIGTERM,signal.SIGINT)}
    def on_signal(signum,unused_frame):
        signals.append(signum)
    for sig in previous:signal.signal(sig,on_signal)
    child=None
    code=2
    until=deadline["absolute_monotonic_deadline_ns"]-deadline["readback_cleanup_reserve_seconds"]*10**9
    env=os.environ.copy();env[owner.ENV_NAMESPACE]=str(base)
    try:
        with (base/"science.stdout.log").open("xb") as stdout, (base/"science.stderr.log").open("xb") as stderr:
            child=subprocess.Popen(command,stdout=stdout,stderr=stderr,env=env,start_new_session=True)
            owner.register(child,base,base/"rules-process.json",command,receipt(base/"job-deadline.json"))
            state["actual_rules_process"]=read(base/"rules-process.json")["worker"]
            write(base/"execution.json",state,replace=True)
            while child.poll() is None:
                if signals:
                    state["external_signal"]=signals[0];code=128+signals[0];break
                if time.monotonic_ns()>=until:
                    state["resource_stop"]="original320-minute-science-deadline-final-reserve"
                    code=75;break
                if shutil.disk_usage(base).free<request["resources"]["free_bytes_resource_stop"]:
                    state["resource_stop"]="declared-temporary-storage-reserve"
                    code=75;break
                time.sleep(0.25)
            if child.poll() is not None:
                code=child.returncode if child.returncode>=0 else 128-child.returncode
            state["rules_returncode"]=child.poll()
    except Exception as error:
        state["error"]=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
        code=2
    finally:
        for sig,handler in previous.items():signal.signal(sig,handler)
        try:
            observation=quiet(base)
            state["quiescence"]=receipt(base/"quiescence.json")
            state["owned_processes_quiescent"]=observation["quiescent"]
        except Exception as error:
            state["owned_processes_quiescent"]=False
            state["quiet_error"]=dict(type=type(error).__name__,message=str(error))
        if child is not None:
            try:
                child.wait(timeout=15)
            except subprocess.TimeoutExpired:
                state["original_rules_child_reaped"]=False
            else:
                state["original_rules_child_reaped"]=True
                state["rules_returncode"]=child.returncode
        runner_result=base/"rules"/"runner-result.json"
        if runner_result.is_file():
            state["original_rules_result"]=receipt(runner_result)
            state["science_returncode"]=read(runner_result).get("science_returncode")
        state.update(returned=True,actual_exit_code=code,
            elapsed_seconds=(time.monotonic_ns()-started)/1e9,
            disk_at_end=dict(zip(("total","used","free"),shutil.disk_usage(base))))
        write(base/"execution.json",state,replace=True)
        print(json.dumps(dict(event="request221_actual_science_return",actual_exit_code=code,
            rules_returncode=state["rules_returncode"],science_returncode=state["science_returncode"],
            resource_stop=state["resource_stop"],external_signal=state["external_signal"],
            owned_processes_quiescent=state["owned_processes_quiescent"],
            execution=receipt(base/"execution.json")),ensure_ascii=True),flush=True)
    return code


def cleanup(request_path,request_sha,namespace,summary_path):
    request,base=bind(request_path,request_sha,namespace)
    summary_path=Path(summary_path).resolve(strict=True)
    require(summary_path.parent==Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
            and summary_path.name==NAMESPACE+"-necessary.json","Exact independent necessary summary path")
    raw=summary_path.read_bytes();summary=json.loads(raw)
    require(len(raw)<=90000 and summary.get("schema")=="R508-live128-scoped-original-full112-necessary-v1"
            and summary.get("necessary_readback_complete") is True
            and summary.get("request",{}).get("sha256")==request_sha
            and summary.get("run")==run_identity(),"Actual single complete necessary readback")
    observation=quiet(base)
    if observation["quiescent"] is not True:
        print(json.dumps(dict(event="request221_cleanup",removed=False,
              reason="actual-owned-process-quiescence-not-proved")),flush=True)
        return 3
    marker=read(base/"ownership.json")
    require(marker["run"]==run_identity(),"Same actual namespace immediately before deletion")
    identity_before=receipt(base/"ownership.json")
    summary_identity=receipt(summary_path)
    # Read-only fetched input directories are exclusively under this namespace.
    for directory,unused_dirs,unused_files in os.walk(base,followlinks=False):
        os.chmod(directory,0o700)
    shutil.rmtree(base)
    record=dict(event="request221_cleanup",removed=True,namespace=str(base),
        ownership=identity_before,necessary_summary=summary_identity,
        actual_owned_processes_quiescent=True,scientific_success_not_required=True,
        only_owned_temporary_namespace_removed=True)
    print(json.dumps(record,ensure_ascii=True),flush=True)
    return 0


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=("prepare","run","rules","science","quiet","cleanup"))
    parser.add_argument("--request",type=Path,required=True)
    parser.add_argument("--request-sha256",required=True)
    parser.add_argument("--namespace",type=Path,required=True)
    parser.add_argument("--summary",type=Path)
    args=parser.parse_args()
    if args.mode=="prepare":return prepare(args.request,args.request_sha256,args.namespace)
    if args.mode=="run":return run(args.request,args.request_sha256,args.namespace)
    if args.mode=="rules":return rules(args.request,args.request_sha256,args.namespace)
    if args.mode=="science":return science(args.request,args.request_sha256,args.namespace)
    if args.mode=="quiet":
        bind(args.request,args.request_sha256,args.namespace)
        result=quiet(args.namespace)
        print(json.dumps(dict(event="request221_quiet",quiescent=result["quiescent"],
              registry_count=len(result["registries"]),unknown=result["unknown"],
              receipt=receipt(Path(args.namespace)/"quiescence.json")),ensure_ascii=True),flush=True)
        return 0 if result["quiescent"] else 3
    require(args.summary is not None,"Actual necessary summary is required for cleanup")
    return cleanup(args.request,args.request_sha256,args.namespace,args.summary)


if __name__=="__main__":
    raise SystemExit(main())
