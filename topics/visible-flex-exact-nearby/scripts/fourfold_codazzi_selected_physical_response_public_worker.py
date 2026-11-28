"""Public job for the signed physical response, with original WSS and GG numerical runtimes."""
import argparse
import ast
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import traceback

TOPIC="topics/visible-flex-exact-nearby"
REPO="Rogerhu12/math-research-public"


def require(ok,msg):
    if not ok:
        raise ValueError(msg)


def encode(v):
    return (json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(",",":"),allow_nan=False)+"\n").encode()


def sha(b):
    return sha256(b).hexdigest()


def module(root,s):
    p=(root/s["path"]).resolve()
    b=p.read_bytes()
    require(p.is_relative_to(root) and len(b)==s["bytes"] and sha(b)==s["sha256"],"the entire "+s["role"])
    spec=importlib.util.spec_from_file_location("_R149_transport_"+s["sha256"][:22],p)
    obj=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def bootstrap(root,files):
    wm=json.loads((root/files["wss_manifest"]["path"]).read_bytes())
    wr={s["role"]:s for s in wm["files"]}
    worker=module(root,wr["worker"])
    old=sys.argv[:]
    try:
        sys.argv=[worker.PARENT_WORKER,"--repo",str(root),"--manifest",str(root/worker.PARENT_MANIFEST),
                  "--manifest-sha",worker.PARENT_MANIFEST_SHA]
        return worker.original_input_prefix(root,files["operational_review"])()
    finally:
        sys.argv=old


def gg_restore(gg,root,shared,target):
    """Use exactly the original worker's 21-object native restoration, with no old scientific entry."""
    g={s["role"]:s for s in gg["files"]}
    worker=module(root,g["worker"])
    tree=ast.parse((root/g["worker"]["path"]).read_bytes())
    main=next(v for v in tree.body if isinstance(v,ast.FunctionDef) and v.name=="main")
    defs=[v for v in main.body if isinstance(v,ast.FunctionDef) and v.name=="restore"]
    require(len(defs)==1,"one frozen whole original 21-object restoration")
    namespace=dict(worker.__dict__,manifest=gg,root=root,temporary=target,state={},
                   git=shared["git"],fetch_commit=shared["fetch_commit"])
    fragment=ast.Module(body=defs,type_ignores=[])
    exec(compile(fragment,"<entire original GG 21-object restoration only>","exec"),namespace)
    target.mkdir()
    args=namespace["restore"]()
    result=namespace["state"]["historical_restoration"]
    require(len(args)==12 and result["historical_input_count"]==21 and result["old_producers_executed"]==0,
            "entire old original native and repair arguments")
    return args,result


def docker(root,temporary,command,name,authenticated=False):
    run=["docker","run","--rm","--name",name,"--user",str(os.getuid())+":"+str(os.getgid()),
         "-v",str(root)+":"+str(root),"-v",str(temporary)+":"+str(temporary),"-w",str(root)]
    if not authenticated:
        run+=["--network","none"]
    env=["GITHUB_ACTIONS","GITHUB_REPOSITORY","GITHUB_RUN_ID","GITHUB_RUN_ATTEMPT","GITHUB_SHA",
         "GITHUB_WORKSPACE","RUNNER_TEMP","GSA_JOB_MONOTONIC_START"]
    if authenticated:
        env+=["GITHUB_TOKEN","GITHUB_API_URL","GITHUB_SERVER_URL"]
    for key in env:
        if key in os.environ:
            run+=["-e",key]
    for v in ("OPENBLAS_CORETYPE=Haswell","OPENBLAS_NUM_THREADS=1","OMP_NUM_THREADS=1","MKL_NUM_THREADS=1",
              "BLIS_NUM_THREADS=1","VECLIB_MAXIMUM_THREADS=1","NUMEXPR_NUM_THREADS=1","PYTHONDONTWRITEBYTECODE=1"):
        run+=["-e",v]
    return run+["r149-original-wss:job","python"]+list(map(str,command))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ("repo","manifest"):
        ap.add_argument("--"+k,type=Path,required=True)
    ap.add_argument("--manifest-sha",required=True)
    ap.add_argument("--original-raw-route",type=Path)
    a=ap.parse_args()
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT")=="1","first event in the original public repository")
    root=a.repo.resolve()
    mpath=(root/a.manifest).resolve()
    raw=mpath.read_bytes()
    require(mpath.is_relative_to(root) and len(raw)<100000 and sha(raw)==a.manifest_sha,"whole joint manifest")
    m=json.loads(raw)
    files={s["role"]:s for s in m["files"]}
    owner=module(root,files["science"])
    require(sha(Path(__file__).read_bytes())==files["worker"]["sha256"] and m["reviewed_rules"]==files["operational_review"],
            "actual worker and reviewed operational rules")
    owner.metadata(root,m)
    shared=bootstrap(root,files)
    if a.original_raw_route is not None:
        route=a.original_raw_route.resolve()
        require(route.is_relative_to(Path(os.environ["RUNNER_TEMP"]).resolve()) and not route.exists()
                and os.environ.get("OPENBLAS_CORETYPE")=="Haswell","one private original raw input phase")
        head=shared["prepare_original"]()
        result=dict(head=head,inputs=str(shared["inputs"]),temporary=str(shared["temporary"]),
                    rows_index=str(shared["rows_index"]),original_state=shared["state"])
        shared["atomic"](route,encode(result))
        return
    op=m["operation"]
    marker=op["consumed_marker"]
    shared["configure_publication"](marker,op)
    git=shared["git"]
    head=shared["pull"]()
    if git("cat-file","-e",head+":"+marker,check_return=False).returncode==0:
        print("Previously reserved complete physical response; original terminal outcome remains authoritative.",flush=True)
        return
    temp=Path(shared["temporary"])
    tmp_root=Path(os.environ["RUNNER_TEMP"]).resolve()
    require(temp.is_relative_to(tmp_root),"one public job-private filesystem")
    run=os.environ["GITHUB_RUN_ID"]
    outdir=op["output_base"]+"/run-"+run+"-1"
    output=temp/"selected-physical-response.json"
    state=shared["state"]
    state.update(kind="R149_selected_physical_response_execution_v1",problem_id=m["problem_id"],
        manifest_sha256=a.manifest_sha,run_id=run,run_attempt="1",entry_commit=os.environ["GITHUB_SHA"],
        complete=False,scientific_complete=False,positive_physical_gate_passed=False,actual_child_returncode=None,
        science_children=0,science_targets=m["target_order"],completed_natural_targets=[],scientific_files=[],
        failure=None,old_completed_targets_recomputed=0,new_artifacts=0,new_Releases=0,new_arrays_published=0)
    gg,wm=(json.loads((root/files[k]["path"]).read_bytes()) for k in ("gg_manifest","wss_manifest"))
    current={}
    for s in list(files.values())+gg["files"]+wm["files"]:
        if s["path"] in current:
            require(all(current[s["path"]][k]==s[k] for k in ("bytes","sha256","git_blob_sha")),"overlapping unchanged input")
        current[s["path"]]=s
    require(len(current)==m["whole_distinct_current_files"],"every nested current source")
    inputs=None
    actual=None
    staged={}
    def bind(h):
        require(sha(git("show",h+":"+str(mpath.relative_to(root)),binary=True).stdout)==a.manifest_sha,
                "frozen metadata after every reviewed pull")
        for path,s in current.items():
            b,_=shared["checked_bytes"](s,h)
            if inputs is not None:
                p=inputs/path
                if p.exists():
                    require(p.read_bytes()==b,"same original staged source")
                else:
                    shared["atomic"](p,b)
    def collect():
        nonlocal actual
        if not output.is_file():
            return
        b=output.read_bytes()
        require(len(b)<=owner.PARAMETERS["maximum_actual_bytes"],"complete small scientific output")
        d=owner.validate(json.loads(b),m)
        require(d["identity"]["run_id"]==run and d["identity"]["run_attempt"]=="1"
                and d["identity"]["source_sha256"]==files["science"]["sha256"]
                and d["identity"]["manifest_sha256"]==a.manifest_sha and d["identity"]["actual_checkout"]==state["actual_scientific_checkout"],
                "current full natural result bound to actual child and checkout")
        require(actual is None or d["completed_targets"][:len(actual["completed_targets"])]==actual["completed_targets"],
                "whole natural prefix never overwritten by an earlier prefix")
        actual=d
        name=outdir+"/selected-physical-response.json"
        staged[name]=b
        state["scientific_files"]=[dict(path=name,bytes=len(b),sha256=sha(b))]
        state["completed_natural_targets"]=d["completed_targets"]
    def outcome():
        collect()
        b=encode(state)
        require(len(b)<100000,"entire public execution remains small")
        report=("# Actual selected physical response\n\nRun "+run+"/1 preserved "+
            str(len(state["completed_natural_targets"]))+" natural targets. The two signed sources, the physical mean, "
            "both terminal blocks and the complete ordinary negative window use the original coordinates. "
            "The scientific file records the actual sufficient-gate outcome and distinguishes affine inputs from matched global data.\n").encode()
        return {**staged,outdir+"/execution.json":b,outdir+"/report.md":report}
    began=time.monotonic()
    os.environ["GSA_JOB_MONOTONIC_START"]=str(began)
    next_pull=began+1800
    published=0
    child=None
    container=None
    def monitored(command,label,env=None,container_name=None):
        nonlocal child,container,next_pull,published
        container=container_name
        child=subprocess.Popen(command,cwd=root,env=env,start_new_session=True)
        while child.poll() is None:
            try:
                child.wait(timeout=5)
            except subprocess.TimeoutExpired:
                pass
            now=time.monotonic()
            require(now-began<=op["child_timeout_seconds"],"joint wall budget including all preparation and arrays")
            if now>=next_pull:
                bind(shared["pull"]())
                next_pull=now+1800
            if output.is_file():
                collect()
                n=len(actual["completed_targets"])
                if n>published:
                    state["last_natural_publication"]=shared["publish"](outcome,"visible-exact: retain whole physical response prefix")
                    published=n
        ret=child.wait()
        child,container=None,None
        state["children"].append(dict(label=label,returncode=ret))
        return ret
    state["children"]=[]
    try:
        bind(head)
        cap,_=shared["capacity"](head)
        require(cap["topic_blob_bytes"]+op["maximum_total_publication_bytes"]+op["reserve_bytes"]<=op["topic_maximum_bytes"],
                "full reserved publication fits the topic")
        state["pre_execution_capacity"]=cap
        markerdata=dict(kind="first_actual_selected_physical_response_reservation_v1",problem_id=m["problem_id"],
            run_id=run,run_attempt="1",manifest_sha256=a.manifest_sha,prepared_utc=shared["utc"](),
            output_directory=outdir,automatic_scientific_retry=False,old_completed_targets_may_be_recomputed=False,
            original_GG_actual=files["gg_actual"]["sha256"],original_WSS_actual=files["wss_actual"]["sha256"],
            target_order=owner.TARGETS)
        state["consumed_marker_publication"]=shared["publish"](lambda:{marker:encode(markerdata)},
             "visible-exact: reserve full actual selected physical response",True)
        route=temp/"raw-route.json"
        native_cmd=[Path(__file__).resolve(),"--repo",root,"--manifest",mpath,"--manifest-sha",a.manifest_sha,
                    "--original-raw-route",route]
        name="gsa-wss-native-"+run
        require(monitored(docker(root,tmp_root,native_cmd,name,True),"original_WSS_native_184_plus_32",
               container_name=name)==0 and route.is_file(),"original native route with all physical source bytes")
        native_route=json.loads(route.read_bytes())
        inputs=Path(native_route["inputs"])
        rows=Path(native_route["rows_index"])
        require(inputs.is_relative_to(tmp_root) and rows.is_relative_to(inputs),"original WSS private native path")
        original_state=native_route["original_state"]
        native_state_bytes=encode(original_state)
        state["original_WSS_native_state"]=dict(bytes=len(native_state_bytes),sha256=sha(native_state_bytes))
        head=shared["pull"]()
        bind(head)
        args,restoration=gg_restore(gg,inputs,shared,temp/"gg-native")
        state["original_GG_native_receipt"]=dict(bytes=len(encode(restoration)),sha256=sha(encode(restoration)),
                                                original_objects=restoration["historical_input_count"])
        immutable=temp/"joint-manifest.json"
        shared["atomic"](immutable,raw)
        base=[inputs/files["science"]["path"],"--repo",inputs,"--manifest",immutable,"--manifest-sha",a.manifest_sha,
              "--rows-index",rows,"--out",output,"--private",temp/"joint-private","--checkout",head,*args]
        env=dict(os.environ)
        for k in ("GITHUB_TOKEN","GIT_CONFIG_COUNT","GIT_CONFIG_KEY_0","GIT_CONFIG_VALUE_0","OPENBLAS_CORETYPE"):
            env.pop(k,None)
        env.update(OPENBLAS_NUM_THREADS="1",OMP_NUM_THREADS="1",MKL_NUM_THREADS="1",PYTHONDONTWRITEBYTECODE="1")
        require(monitored([sys.executable,*base,"--preflight-only"],"whole_GG_WSS_metadata_native_admission",env)==0,
                "actual joint predecessor preflight before recovering either mathematical carrier")
        state["actual_scientific_checkout"]=head
        name="gsa-wss-source-"+run
        require(monitored(docker(root,tmp_root,[*base,"--source-only"],name),"original_WSS_signed_carrier_320",
                          container_name=name)==0,"entire original signed source in original WSS runtime")
        state["science_children"]=1
        state["scientific_started_utc"]=shared["utc"]()
        ret=monitored([sys.executable,*base],"GG_restore_and_actual_full_response_384",env)
        state["actual_child_returncode"]=ret
        state["scientific_ended_utc"]=shared["utc"]()
        collect()
        require(actual is not None,"genuine signed response actual outcome")
        state["scientific_complete"]=actual["complete"]
        if len(actual["completed_targets"])>=4:
            state["positive_physical_gate_passed"]=actual["conclusions"][owner.TARGETS[3]]["physical_gate_passed"]
        require(ret==0 and actual["complete"] and actual["failure"] is None,"whole actual physical branch")
        state["complete"]=True
    except BaseException as exc:
        state["failure"]=dict(type=type(exc).__name__,message=str(exc)[:1500],traceback=traceback.format_exc()[-6000:])
        print(traceback.format_exc(),flush=True)
    finally:
        if child is not None and child.poll() is None:
            if container is not None:
                subprocess.run(["docker","kill",container],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            try:
                os.killpg(child.pid,signal.SIGTERM)
                child.wait(timeout=20)
            except (ProcessLookupError,subprocess.TimeoutExpired):
                if child.poll() is None:
                    os.killpg(child.pid,signal.SIGKILL)
                    child.wait()
        state["finished_utc"]=shared["utc"]()
        state["total_wall_seconds"]=time.monotonic()-began
        whole=outcome()
        print("RECOVERABLE WHOLE GSA OUTCOME BEFORE GIT "+encode({k:v.decode() for k,v in whole.items()}).decode(),flush=True)
        state["final_publication"]=shared["publish"](outcome,"visible-exact: publish entire actual physical response outcome")
    require(state["complete"],"terminal failure/prefix preserved without automatic scientific replay")


if __name__=="__main__":
    main()
