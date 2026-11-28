"""First whole selected two-column source carrier and signed polarizations, public Actions."""
from __future__ import annotations
import argparse
import ast
import hashlib
import importlib.util
import json
import multiprocessing as mp
import os
from pathlib import Path
import platform
import queue
import signal
import sys
import time
import traceback
from types import SimpleNamespace


TOPIC = "topics/visible-flex-exact-nearby"
REPOSITORY = "Rogerhu12/math-research-public"
PARENT_MANIFEST = TOPIC+"/notes/2026-11-28-true-root-trial-complete2677-inputs.json"
PARENT_MANIFEST_SHA = "6b82d09170ed4ec780eccd0910cb69df98615390ef2f73237ed324d1e3f2c692"
PARENT_OWNER = TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_vector_trial_owner.py"
PARENT_OWNER_SHA = "2408b84e7aa820ec6942dcd6255b77583cd776072c09fb6f521866930fcb7200"
KIND = "R149_whole_selected_body_signed_Newton_and_nu_source_v1"
MANIFEST_KIND = "R149_whole_selected_body_signed_source_inputs_v1"
TARGETS = ["whole_selected_signed_577_by_2_source_with_true_compact_metric",
           "whole_negative_and_positive_enclosing_windows_signed_source_polarizations"]
RUNTIME = {"python":"3.12.14","packages":{"numpy":"2.3.5","python-flint":"0.9.0"}}
PARAMETERS = {"arithmetic_bits":320,"angular_grid":1024,"quarter_frequencies":288,"rows":577,"columns":2,
    "whole_interval":["0","25/8"],"control":["1/20","9/50"],"negative_window":["0","2383968743003/10000000000000"],
    "positive_enclosing_window":["1191984371497/5000000000000","25/8"],"cubics":6144,"old_rows":7721,
    "maximum_actual_bytes":90000,"maximum_private_bytes":8589934592,"maximum_aggregate_rss":15032385536,
    "maximum_scientific_seconds":19500,"workers":4,"maximum_outstanding":8,"chunk_size":128}
FIELDS = ("kind","identity","parameters","runtime","original_input_identity","source_restoration",
    "plan","complete","proved","stage","failure","actual_returncode","actual_mathematical_wall_seconds",
    "completed_targets","new_complete_signed_cells","chunks","unfinished_chunk","complete_disjoint_cells","new_records",
    "actual_resource_peaks","original_success_targets_recomputed","new_arrays_published","new_artifacts",
    "new_Releases","full_actual_response_or_nonlinear_solution_proved")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def require(ok,message):
    if not ok:
        raise ValueError(message)


def load(path,name):
    spec = importlib.util.spec_from_file_location(name,path)
    require(spec is not None and spec.loader is not None,"one whole module")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def admit(root,raw,digest,rows_index):
    require(sha(raw)==digest and len(raw)<100000,"whole new manifest")
    m=json.loads(raw)
    require(m["kind"]==MANIFEST_KIND and m["scientific_kind"]==KIND and m["parameters"]==PARAMETERS
            and m["repository"]==REPOSITORY and m["target_order"]==TARGETS and m["runtime"]==RUNTIME
            and m["allowed_scientific_fields"]==sorted(FIELDS),"whole signed two-column contract")
    roles = {s["role"]:s for s in m["files"]}
    require(len(roles)==len(m["files"]) and roles["science"]["path"]==TOPIC+"/scripts/"+Path(__file__).name
            and roles["science"]["sha256"]==sha(Path(__file__).read_bytes()),"entire active first owner")
    for s in roles.values():
        p=Path(s["path"])
        require(not p.is_absolute() and ".." not in p.parts and str(p).startswith(TOPIC+"/"),"whole topic input")
        r=(root/p).read_bytes()
        require(len(r)==s["bytes"] and sha(r)==s["sha256"] and hashlib.sha1(
            b"blob "+str(len(r)).encode()+b"\0"+r).hexdigest()==s["git_blob_sha"],"entire "+s["role"])
        if p.suffix==".py":
            ast.parse(r,filename=str(p))
    require(roles["parent_manifest"]["sha256"]==PARENT_MANIFEST_SHA and roles["parent_owner"]["sha256"]==PARENT_OWNER_SHA
            and roles["parent_manifest"]["path"]==PARENT_MANIFEST and roles["parent_owner"]["path"]==PARENT_OWNER,
            "entire original TCXV raw entry")
    parent=json.loads((root/PARENT_MANIFEST).read_bytes())
    specs=parent["files"]+parent["historical_inputs"]
    require(len(parent["files"])==184 and len(parent["historical_inputs"])==32
            and m["whole_original_descriptors"]=={"bytes":len(canonical(specs)),"sha256":sha(canonical(specs))},
            "whole original 184/32 descriptor closure")
    old=load(root/PARENT_OWNER,"_R149_WSS_only_original_raw_inputs")
    original=old.preflight(SimpleNamespace(repo=str(root),input_root=str(root),manifest=str(root/PARENT_MANIFEST),
                    manifest_sha=PARENT_MANIFEST_SHA,rows_index=str(rows_index)))
    require(not any(x in sys.modules for x in ("numpy","flint","scipy")),"metadata before numerical imports")
    return m,roles,original


def validate(d,m):
    require(sorted(d)==sorted(FIELDS) and d["kind"]==KIND and d["parameters"]==m["parameters"]
            and d["runtime"]==RUNTIME and d["original_success_targets_recomputed"]==0 and
            all(d[k]==0 for k in ("new_arrays_published","new_artifacts","new_Releases"))
            and d["full_actual_response_or_nonlinear_solution_proved"] is False,"whole public signed scope")
    count=len(d["completed_targets"])
    require(d["completed_targets"]==TARGETS[:count] and count<=2 and
            set(d["new_records"])==set(d["completed_targets"]),"complete natural target prefix")
    pieces=d["chunks"]+([d["unfinished_chunk"]] if d["unfinished_chunk"] else [])
    nxt=0
    for item in pieces:
        require(item["first"]==nxt and nxt<item["stop"]<=nxt+PARAMETERS["chunk_size"]
                and len(item["sha256"])==64 and item["whole_file_bytes"]>0,"saved ordered signed source prefix")
        nxt=item["stop"]
    require(nxt==d["new_complete_signed_cells"],"entire accepted prefix represented")
    ahead=d["complete_disjoint_cells"]
    require(len(ahead)<=8 and len({r["index"] for r in ahead})==len(ahead)
            and all(nxt<=r["index"]<nxt+8 and len(r["sha256"])==64 and r["bytes"]>0 for r in ahead),
            "every complete disjoint piece outside the contiguous prefix")
    if count:
        packet=d["new_records"][TARGETS[0]]
        require(not ahead and packet["whole_private_piece_count"]==nxt==d["plan"]["pieces"]
                and packet["complete_domain"]==PARAMETERS["whole_interval"] and packet["physical_source_rows"]==577
                and packet["source_columns"]==["ordinary_Newton_minus_f_delta","ordinary_nu_proposal_defect_s_delta"]
                and packet["new_arrays_published"] is False and len(packet["complete_index_sha256"])==64,
                "complete same-member signed source and original independent mean")
    if count==2:
        result=d["new_records"][TARGETS[1]]
        require(set(result)=={"full","fixed_negative","positive_cover"} and all(
              x["signed_inner_product"]["kind"]=="complete_decimal_ball_v1" and int(x["pieces"])>0
              for x in result.values()),"actual signed polarizations on all three declared intervals")
    if d["complete"]:
        require(count==2 and d["proved"] and d["actual_returncode"]==0 and d["failure"] is None,
                "two whole genuine new conclusions")


def execute(args):
    from fractions import Fraction
    from importlib.metadata import version
    root,manifest,private,output=map(Path,(args.repo,args.manifest,args.private,args.out))
    m,roles,admitted=admit(root,manifest.read_bytes(),args.manifest_sha,args.rows_index)
    if args.preflight_only:
        print(canonical({"kind":"complete_WSS_original_raw_preflight_v1","whole_identity":admitted[-1],
                         "new_targets":TARGETS,"new_scientific_work":0}).decode(),end="")
        return 0
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
        and os.environ.get("GITHUB_RUN_ATTEMPT")=="1" and all(os.environ.get(k)=="1" for k in
        ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS")) and platform.python_version()==RUNTIME["python"]
        and all(version(k)==v for k,v in RUNTIME["packages"].items()),"fixed actual single-thread public runtime")
    import numpy as np
    import flint
    flint.ctx.prec=PARAMETERS["arithmetic_bits"]
    core=load(root/roles["raw_input_helper"]["path"],"_WSS_verified_exact_raw_offsets")
    positive=load(root/roles["positive_signed_source"]["path"],"_WSS_actual_whole_positive_signed_form")
    field=load(root/roles["carrier"]["path"],"_WSS_actual_whole_ordinary_source")
    resources=load(root/roles["resource_carriers"]["path"],"_WSS_aggregate_process_accounting")
    disk=load(root/roles["resource_directory"]["path"],"_WSS_aggregate_native_budget")
    original,old_roles,raws,helper,prior,rows,identity=admitted
    tc=load(root/old_roles["trial_math"]["path"],"_WSS_original_batch_radial_Fourier")
    private.mkdir(parents=True,exist_ok=True)
    require(not output.exists(),"one first outcome")
    start=time.monotonic()
    state={"kind":KIND,"identity":{"manifest_sha256":args.manifest_sha,"source_sha256":roles["science"]["sha256"],
           "run_id":os.environ["GITHUB_RUN_ID"],"run_attempt":"1","actual_scientific_checkout":args.checkout,
           "workflow_event_commit":os.environ["GITHUB_SHA"]},"parameters":PARAMETERS,"runtime":RUNTIME,
           "original_input_identity":identity,"source_restoration":None,"plan":None,"complete":False,"proved":False,
           "stage":"complete_whole_raw_admission","failure":None,"actual_returncode":None,"actual_mathematical_wall_seconds":0.,
           "completed_targets":[],"new_complete_signed_cells":0,"chunks":[],"unfinished_chunk":None,"complete_disjoint_cells":[],"new_records":{},
           "actual_resource_peaks":{"aggregate_rss":0,"private_and_native_bytes":0},"original_success_targets_recomputed":0,
           "new_arrays_published":0,"new_artifacts":0,"new_Releases":0,"full_actual_response_or_nonlinear_solution_proved":False}
    def save():
        state["actual_mathematical_wall_seconds"]=time.monotonic()-start
        validate(state,m)
        raw=canonical(state)
        require(len(raw)<=PARAMETERS["maximum_actual_bytes"],"whole scientific result byte cap")
        core.atomic(output,raw)
    def progress(name,detail):
        print(json.dumps(dict(stage=name,**detail),sort_keys=True),flush=True)
    def terminate_science(signum,frame):
        raise TimeoutError("wall stop requested; retain every completed signed piece")
    signal.signal(signal.SIGTERM,terminate_science)
    processes=[]
    last_disk=0.
    def budget(force=False):
        nonlocal last_disk
        now=time.monotonic()
        peaks=state["actual_resource_peaks"]
        peaks["aggregate_rss"]=max(peaks["aggregate_rss"],resources.aggregate_rss_bytes(processes))
        if force or now-last_disk>20:
            # The original materialized native tree is the immutable input root.
            used=disk.private_bytes((root,private))
            peaks["private_and_native_bytes"]=max(peaks["private_and_native_bytes"],used)
            last_disk=now
        require(peaks["aggregate_rss"]<=PARAMETERS["maximum_aggregate_rss"]
                and peaks["private_and_native_bytes"]<=PARAMETERS["maximum_private_bytes"]
                and now-start<PARAMETERS["maximum_scientific_seconds"],"complete scientific resource cap")
    save()
    try:
        budget(True)
        base,direction,offsets,rows,receipt=core.raw_inputs(np,flint,admitted,root,private,progress)
        state["source_restoration"]=receipt
        backend,br=helper.directed_backend(np,flint,raws[old_roles["box_math"]["path"]],raws[old_roles["fft_math"]["path"]])
        require(br==receipt["directed_backend"],"same whole directed original arithmetic for source and repairs")
        c=tc.DirectedContext(np,flint.arb,backend["Box"],backend["CBox"],backend["zeros"],
                             backend["arb_box"],backend["reduce_box"],backend["DirectedFFT"]())
        read=lambda r:field.historical_ball(flint,r)
        plan=field.partition(helper,rows,base,direction)
        descr=canonical([[j,k,str(a),str(b)] for j,k,a,b in plan])
        require(7721<=len(plan)<20000,"complete declared physical cover")
        state["plan"]={"pieces":len(plan),"bytes":len(descr),"canonical_sha256":sha(descr),
                       "true_compact_signed_derivatives":True,"both_sides_of_true_uncertain_root":True}
        store=field.SignedSourceStore(private/"whole-signed",plan)
        state["stage"]="complete_physical_source_cells"
        save()
        def worker(incoming,outgoing):
            signal.signal(signal.SIGTERM,signal.SIG_DFL)
            while True:
                i=incoming.get()
                if i is None:
                    return
                try:
                    j,k,lo,hi=plan[i]
                    pair=field.signed_pair(c,tc,positive,helper,base,direction,offsets,rows[j],k,lo,hi,read)
                    store.put(i,field.packed_pairs(c,positive,pair),field.endpoint_pair(c,positive,pair))
                    spec=store.records.pop(i)
                    resources.atomic(store.directory/(str(i)+".done"),canonical(spec))
                    outgoing.put((i,spec,None))
                except BaseException as exc:
                    outgoing.put((i,None,type(exc).__name__+": "+str(exc)))
                    return
        context=mp.get_context("fork")
        jobs,finished=context.Queue(8),context.Queue(8)
        pending,buffer={},{}
        nxt=0
        def fill(cursor):
            nonlocal nxt
            # Bound the whole live out-of-order window including already finished cells.
            while nxt<len(plan) and nxt<cursor+8:
                jobs.put(nxt);pending[nxt]=True;nxt+=1
        try:
            for _ in range(4):
                p=context.Process(target=worker,args=(jobs,finished));p.start();processes.append(p)
            chunk=None
            for i in range(len(plan)):
                fill(i)
                while i not in buffer:
                    budget()
                    try:
                        k,s,err=finished.get(timeout=3)
                    except queue.Empty:
                        require(all(p.is_alive() for p in processes),"lost a signed source worker")
                        continue
                    require(k in pending and err is None and s is not None,"whole new signed piece "+str((k,err)))
                    del pending[k]
                    buffer[k]=s
                store.records[i]=buffer.pop(i)
                store.get(i)
                if chunk is None:
                    chunk={"first":i,"stop":i,"whole_file_bytes":0,"sha256":sha(b"WSS-complete-piece-chunk")}
                s=store.records[i]
                chunk.update(stop=i+1,whole_file_bytes=chunk["whole_file_bytes"]+s["bytes"],
                             sha256=sha(bytes.fromhex(chunk["sha256"])+canonical([i,s])))
                state["unfinished_chunk"]=dict(chunk)
                state["new_complete_signed_cells"]=i+1
                if (i+1)%128==0 or i+1==len(plan):
                    state["chunks"].append(chunk);state["unfinished_chunk"]=chunk=None
                if (i+1)%8==0 or i+1==len(plan):
                    save()
                if (i+1)%128==0:
                    progress("whole_signed_prefix",{"complete_cells":i+1})
                budget()
        finally:
            for p in processes:
                if p.is_alive():p.terminate()
            for p in processes:p.join(timeout=5)
            jobs.cancel_join_thread();jobs.close();finished.close()
            for i in range(state["new_complete_signed_cells"],min(nxt,len(plan))):
                path=store.directory/(str(i)+".done")
                if path.is_file():
                    store.records[i]=json.loads(path.read_bytes())
                    store.get(i)
                    state["complete_disjoint_cells"].append({"index":i,**store.records[i]})
        packet=store.receipt()
        state["completed_targets"].append(TARGETS[0]);state["new_records"][TARGETS[0]]=packet
        state["stage"]="whole_signed_source_carrier_completed";save()
        windows={"full":(Fraction(0),helper.OUTER),"fixed_negative":(Fraction(0),helper.ROOT[1]),
                 "positive_cover":(helper.ROOT[0],helper.OUTER)}
        accum={k:[flint.arb(0),0,Fraction(0)] for k in windows}
        import struct
        for i,(j,k,lo,hi) in enumerate(plan):
            _,payload=store.get(i)
            rows_of_pairs=struct.iter_unpack("<dddd",payload)
            total=flint.arb(0)
            for l0,h0,l1,h1 in rows_of_pairs:
                total+=flint.arb(l0).union(flint.arb(h0))*flint.arb(l1).union(flint.arb(h1))
            for name,(left,right) in windows.items():
                if left<=lo<hi<=right:
                    v=accum[name]
                    v[0]+=c.exact(hi-lo)*total;v[1]+=1;v[2]+=hi-lo
            budget()
        result={}
        for name,(left,right) in windows.items():
            v,n,length=accum[name]
            require(length==right-left and n>0,"all pieces in original signed projection window")
            result[name]={"interval":[str(left),str(right)],"pieces":n,"signed_inner_product":resources.scalar(v)}
        state["completed_targets"].append(TARGETS[1]);state["new_records"][TARGETS[1]]=result
        state["stage"]="all_complete_signed_body_targets";state["actual_returncode"]=0
        state["complete"]=state["proved"]=True
    except Exception as exc:
        state["actual_returncode"]=1
        state["failure"]={"type":type(exc).__name__,"message":str(exc),"traceback":traceback.format_exc()}
    save()
    return state["actual_returncode"]


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("repo","manifest","manifest-sha","rows-index","out","private","checkout"):
        parser.add_argument("--"+name,required=True)
    parser.add_argument("--preflight-only",action="store_true")
    raise SystemExit(execute(parser.parse_args()))
