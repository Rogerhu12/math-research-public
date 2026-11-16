#!/usr/bin/env python3
"""R450: same-job complete far-family reuse and fresh complete native sampling.

The complete original R380/R357 family, every candidate/error record, the
physical far radius, the original far point sample and its actual mu word
are retained. Only the new grid's other point enclosures and numerical
representatives are produced. No old response, Jacobian, native state,
factorization, acceptance or continuous-field certificate is reused.

The independent worker/client identify this producer honestly. Frozen R441
and R448 callers require an explicit new source registration; this module
does not modify them or their globals. All science runs only in public
Actions. ``readback`` is standard-library metadata reading, not science.
Author: geometry agent (AI), 2026-11-16.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import shutil
import signal
import struct
import sys
import time

ENTRY=Path(__file__).name
SCHEMA="R450-current-C-same-complete-far-family-fresh-radial-sampling-v1"
READBACK_SCHEMA="R450-same-far-fresh-grid-one-necessary-readback-v1"
MODEL="R286-original-stored-continuous-model-convention-C-v1"
REPOSITORY="Rogerhu12/math-research-public"
M,K,DEPTH=112,224,576
MODES=list(range(2,225,2))
SOURCES={
 "positive":dict(name="geometry_20261115_current_C_pruefer_positive_radial_sampling.py",
  sha256="965c277c5aad5a3b5c8c817600d4c435186d9ce1b267b0b59f6e7a8fa69de390",
  schema="current-C-pruefer-positive-endpoint-physical-radial-samples-and-general-far-v1"),
 "joint":dict(name="geometry_20261115_current_C_pruefer_joint_radial_sampling.py",
  sha256="32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4",
  schema="current-C-pruefer-joint-nominal-row-physical-radial-samples-and-general-far-v1")}
ORIGINS=(
 dict(schema="current-C-continuous-ten-full453-frozen450-owned-process-launch-v1",
  sha256="6ff21118040ad4006ae8170923996ee11e34163ce38fc460dd6aa23f972fcd66",
  deadline_schema="request193-owned-job-science-deadline-v1"),
 dict(schema="current-C-continuous-ten-joint-full453-frozen450-owned-process-launch-v1",
  sha256="cb05724bbedf71951524d187d242c1783d244bc729241ec91a91e0a9cf8f02d7",
  deadline_schema="request203-owned-job-science-deadline-v1"))
WORKER="geometry_20261116_current_C_same_far_native_worker.mjs"
CLIENT="geometry_20261116_current_C_same_far_tail_client.py"
NATIVE_PINS={
 WORKER:"bbbca0cb031ff5f2ca33f675d2c0d3e8135866a33962649e2d551e1d683b7c03",
 CLIENT:"4328caeb0c2dde4e0d7df70058e793a042ee8202dd47eca376d441071d6d81de",
 "geometry_20261115_current_C_general_robin_native.mjs":"fae2cb0fface7eadcc955fe09a07e9b59a7df8cd692bccc6cdf826c691eb8349",
 "geometry_20261115_current_C_synchronous_linear_bridge.mjs":"67e3b23c9e5306764db3d6b8e0392eb8f59d4b63bfb671a0703fe33b2146c286",
 "exact_20261115_current_C_general_robin_chain.py":"946251656306a6cbe137513e12bac305c7758e5ec7306995a63314bd0f400bb5",
 "exact_20261114_tail_capacity_loader.mjs":"07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395",
 "geometry_20261115_pruefer_joint_row_representative.py":"24c7681c75d5615bcfbfa7b14cdf0155a858bf09578f856433313408b6a16e97"}
REUSED_LEDGER_NAMES=("far-all-mode-rows","far-complete-tubes","far-inverse-leaf-coverage",
 "far-panel-commits","far-accepted-panels","coefficient-boxes","sample-inverse-leaves")

def require_actions():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise RuntimeError("R450 belongs only to the named public repository Actions")

def require(value,message):
    if not value:raise ValueError(message)

def canonical(value):
    return (json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()

def same_payload(a,b):
    return isinstance(a,dict) and isinstance(b,dict) and all(a.get(k)==b.get(k) for k in ("bytes","sha256"))

def actual_identity(value):
    require(value.get("repository")==REPOSITORY and str(value.get("run_id"))==os.environ["GITHUB_RUN_ID"]
        and value.get("source_commit")==os.environ["GITHUB_SHA"],"Use the actual same-job/source object")

def contained(directory,name):
    root=Path(directory).resolve(strict=True)
    require(isinstance(name,str) and not Path(name).is_absolute(),"Use a relative original member path")
    p=(root/name).resolve(strict=True)
    require(p!=root and root in p.parents,"Original member escaped its bound directory")
    q=root/Path(name)
    while q!=root:
        require(not q.is_symlink(),"No member symlinks")
        q=q.parent
    return p

def temporary(path,exists=True):
    root=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    p=Path(path).resolve(strict=exists)
    require(p!=root and root in p.parents,"All actual data must remain under RUNNER_TEMP")
    return p

def receipt(path,budget=None):
    p=Path(path);digest=hashlib.sha256();size=0
    with p.open("rb") as stream:
        while raw:=stream.read(1<<20):
            if budget is not None:budget.check()
            digest.update(raw);size+=len(raw)
    return dict(file=p.name,bytes=size,sha256=digest.hexdigest())

def read_json(path,expected=None,budget=None):
    p=Path(path);raw=p.read_bytes()
    if budget is not None:budget.check()
    ident=dict(file=p.name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
    if isinstance(expected,str):require(ident["sha256"]==expected,"Actual JSON SHA differs: "+str(p))
    elif expected is not None:require(same_payload(ident,expected),"Actual member bytes/SHA differ: "+str(p))
    return json.loads(raw),ident

def member(directory,desc,budget=None):
    require(isinstance(desc,dict),"Original member descriptor required")
    return read_json(contained(directory,desc["file"]),desc,budget)

def write_json(path,value):
    p=Path(path);raw=canonical(value)
    with p.open("xb") as handle:
        handle.write(raw);handle.flush();os.fsync(handle.fileno())
    return dict(file=p.name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())

def word(value):
    x=float(value)
    require(math.isfinite(x),"Actual finite binary64 word required")
    return dict(value=x,f64le=struct.pack("<d",x).hex(),
        classification="negative-zero" if x==0 and math.copysign(1,x)<0 else "finite")

def from_word(value):
    require(isinstance(value,dict) and isinstance(value.get("f64le"),str),"Complete original word record required")
    raw=bytes.fromhex(value["f64le"])
    require(len(raw)==8,"One exact binary64 word required")
    x=struct.unpack("<d",raw)[0]
    require(math.isfinite(x) and struct.pack("<d",float(value["value"]))==raw,
        "Original decimal/word representations disagree")
    return x

class ResourceStop(RuntimeError):
    """Declared clock/storage/interruption, never a scientific rejection."""

class Budget:
    """Cooperative whole-call clock; the external OwnedChild remains the hard owner."""
    def __init__(self,args,deadline,started):
        self.started=started;self.seconds=args.budget_seconds;self.deadline=deadline
        self.limit=args.sample_max_nodes;self.out=args.out;self.reserve=args.free_bytes_reserve
        self.attempts=0;self.checks=0;self.stop=None;self.signals=[];self.finished=None
        self.last_disk=None;self.last_disk_time=0;self.handlers={}
    def signal(self,number,frame):
        self.signals.append(dict(number=number,name=signal.Signals(number).name,
            elapsed_seconds=time.monotonic()-self.started))
    def install(self):
        for number in (signal.SIGTERM,signal.SIGINT):self.handlers[number]=signal.signal(number,self.signal)
    def restore(self):
        for number,handler in self.handlers.items():signal.signal(number,handler)
    def halt(self,kind,**facts):
        if self.stop is None:self.stop=dict(kind=kind,actual_work_units=self.attempts,
            elapsed_seconds=time.monotonic()-self.started,**facts)
        raise ResourceStop(kind)
    def check(self):
        self.checks+=1;now=time.monotonic()
        if self.signals:self.halt("actual_external_interruption",signals=self.signals)
        if time.time()>=self.deadline:self.halt("original_absolute_science_deadline_reached")
        if now-self.started>=self.seconds:self.halt("explicit_whole_call_budget_reached")
        if self.last_disk is None or now-self.last_disk_time>=1 or self.checks%256==0:
            disk=shutil.disk_usage(self.out);self.last_disk=dict(total=disk.total,used=disk.used,free=disk.free)
            self.last_disk_time=now
            if disk.free<self.reserve:self.halt("owned_output_free_reserve_reached",actual_storage=self.last_disk)
    def attempt(self):
        self.check()
        if self.attempts>=self.limit:self.halt("explicit_fresh_sampling_work_unit_limit_reached")
        self.attempts+=1
    def finish(self):
        if self.finished is None:self.finished=time.monotonic()
    def record(self):
        return dict(declared_whole_call_seconds=self.seconds,absolute_original_deadline=self.deadline,
            elapsed_seconds=(self.finished or time.monotonic())-self.started,
            source_binding_and_runtime_setup_included=True,declared_fresh_point_work_units=self.limit,
            actual_fresh_point_work_units=self.attempts,actual_checks=self.checks,
            last_storage=self.last_disk,free_bytes_reserve=self.reserve,stop=self.stop,signals=self.signals,
            cooperative_checks_not_an_independent_asynchronous_kill=True,
            external_owned_child_and_original_job_limits_still_required=True)

def bind_clock(args):
    origin,oid=read_json(temporary(args.origin_launch_directory)/"result.json",args.origin_launch_result_sha256)
    actual_identity(origin)
    matches=[r for r in ORIGINS if origin.get("schema")==r["schema"] and origin.get("source_sha256")==r["sha256"]]
    require(len(matches)==1,"Only the actual original193 or joint203 clock source is registered")
    deadline,did=read_json(temporary(args.job_deadline),args.job_deadline_sha256)
    actual_identity(deadline)
    require(same_payload(did,origin.get("actual_job_deadline")),"The actual original launch consumed another clock")
    require(deadline.get("schema")==matches[0]["deadline_schema"]
        and deadline.get("recipe_sha256")==origin.get("recipe",{}).get("sha256")
        and deadline.get("science_seconds_from_namespace")==18900
        and deadline.get("readback_reserve_seconds")==2700,"Original clock/recipe/reserve changed")
    t0=deadline.get("namespace_created_unix_seconds")
    require(type(t0) in (int,float) and math.isfinite(t0) and t0>0,"Actual original creation time required")
    return t0+18900,dict(actual_origin_launch=oid,actual_job_deadline=did,original_clock=deadline,
        BVP_acceptance_not_required_or_inferred_by_far_reuse=True)

def load_sampler(comp,family,args):
    spec=SOURCES[family];path=Path(comp)/spec["name"]
    require(receipt(path)["sha256"]==spec["sha256"],"Original sampling method source differs")
    module_spec=importlib.util.spec_from_file_location("_R450_original_"+family,path)
    module=importlib.util.module_from_spec(module_spec);sys.modules[module_spec.name]=module
    try:module_spec.loader.exec_module(module)
    except BaseException:sys.modules.pop(module_spec.name,None);raise
    runtime,sources,proof=module.load_runtime(args)
    return module,runtime,sources,proof

def bound_stream(directory,desc,budget,selected=None,visit=None,progress=None):
    """Read every original byte once; only designated scientific rows are parsed."""
    p=contained(directory,desc["file"]);h=hashlib.sha256();size=count=0;chosen=[]
    with p.open("rb") as handle:
        for raw in handle:
            budget.check();h.update(raw);size+=len(raw)
            require(raw.endswith(b"\n"),"A completed original ledger has an unfinished physical line")
            if selected is None or selected(count):
                value=json.loads(raw)
                if visit is not None:visit(count,value)
                else:chosen.append(value)
            count+=1
            if progress is not None:progress.update(bytes_read=size,physical_lines_read=count)
    require((size,count,h.hexdigest())==(desc["bytes"],desc["rows"],desc["sha256"]),
        "Complete original ledger bytes/rows/SHA differ: "+desc["file"])
    return chosen,dict(directory=str(Path(directory).resolve()),descriptor=copy.deepcopy(desc),
        actual_full_bytes_read=size,actual_full_rows_read=count,actual_sha256=h.hexdigest())

def bind_original_far(args,report,budget,S,data):
    directory=temporary(args.original_sampling_directory)
    previous,pid=read_json(directory/"result.json",args.original_sampling_result_sha256,budget)
    actual_identity(previous)
    matching=[k for k,r in SOURCES.items() if previous.get("schema")==r["schema"]
        and previous.get("source_sha256")==r["sha256"]]
    require(matching==[args.original_family],"The actual prior source family differs")
    require(previous.get("target_model_schema")==MODEL and previous.get("completed") is True
        and previous.get("native_geometry_ready") is True and previous.get("error") is None
        and previous.get("old_graphs_or_gains_used") is False
        and previous.get("exact_global_C_realization_of_numeric_representatives_certified") is False,
        "This thin consumer requires the actual completed original geometry, with its honest finite scope")
    require(previous.get("actual_original_input_binding")==data["binding"],
        "The complete C, exact root family, deep rows, cut query or full original streams changed")
    require(same_payload(previous.get("actual_R380_proof"),report["actual_R380_proof"])
        and same_payload(previous.get("actual_R357_proof"),report["actual_R357_proof"]),
        "The original propagation and oriented-unit proofs changed")
    require(previous.get("actual_far_modes_completed")==MODES
        and previous.get("complete_factorized_far_modes")==MODES
        and previous.get("complete_unit_far_row_modes")==MODES
        and previous.get("actual_not_started_far_modes")==[],"Every original physical mode must actually be complete")
    geometry,gid=member(directory,previous["geometry"],budget)
    require(geometry.get("schema")==S.GEOMETRY_SCHEMA and geometry.get("model_schema")==MODEL
        and (geometry.get("modes"),geometry.get("spacing"),geometry.get("stage_count"))==(112,2,576)
        and geometry.get("original_C_input_binding")==data["binding"],"The original full geometry/model identity differs")
    far=float(geometry["finite_far_radius"]);cut=float(geometry["cut_radius"])
    require(math.isfinite(far) and 0<far<cut and Q(cut)==data["cut"],"Actual finite endpoints changed")
    far_sample=previous["far_point_sample"];mu=from_word(previous["actual_far_coordinate_mu_word"])
    require(mu>0 and from_word(far_sample["physical_radius_word"])==far
        and far_sample.get("point_index")==0 and far_sample.get("complete_closed_point_inclusion") is True
        and far_sample.get("old_finite_inverse_selector_used") is False,
        "The original complete physical far anchor is unavailable")
    for name in ("w","w_r","logw","dlogwdr"):
        rec=far_sample["numerical_word_receipts"][name]
        x=from_word(rec["actual_word"])
        require(struct.pack("<d",x)==struct.pack("<d",float(far_sample["numerical"][name])),
            "The retained far representative and its actual word differ")
        S.F.record_bounds(rec["exact_real_enclosure"])
        S.F.record_bounds(rec["difference_exact_quantity_minus_numeric_word"])
    require(struct.pack("<d",from_word(geometry["far_identity"]["physical_radius_word"]))==struct.pack("<d",far),
        "The original far identity used another radius word")
    rowdesc=geometry["far_identity"]["general_rows"]
    rows_doc,rid=member(directory,rowdesc,budget)
    require(rows_doc.get("schema")==previous["schema"]+"-all112-general-far-rows"
        and rows_doc.get("old_graph_or_height_division_used") is False
        and rows_doc.get("exact_unit_row_orientation_and_all_candidate_dependencies_retained") is True
        and struct.pack("<d",from_word(rows_doc["physical_radius_word"]))==struct.pack("<d",far),
        "The actual complete candidate-oriented row document differs")
    rows=rows_doc.get("complete_rows")
    require(isinstance(rows,list) and len(rows)==112,"All112 actual complete far rows required")
    report["reuse_binding_progress"]=dict(original_sampling_result=pid,original_geometry=gid,
        original_rows=rid,current_ledger=None,complete_ledger_identities=[],remaining_ledgers=[])
    ledger=previous["detailed_ledgers"]
    names=list(REUSED_LEDGER_NAMES)
    if args.original_family=="joint":names.append("numeric-far-row-selection")
    progress=report["reuse_binding_progress"]
    progress["remaining_ledgers"]=list(names)
    modes=[];anchor_leaves=[];all_ids={}
    anchor_span=far_sample["all_closed_inverse_leaves"]
    require(type(anchor_span.get("first")) is int and type(anchor_span.get("stop")) is int
        and 0<=anchor_span["first"]<anchor_span["stop"]<=ledger["sample-inverse-leaves"]["rows"],
        "The original complete far inverse span is absent")
    for pos,name in enumerate(names):
        progress["current_ledger"]=dict(name=name,bytes_read=0,physical_lines_read=0)
        progress["remaining_ledgers"]=names[pos:]
        selected=(None if name=="far-all-mode-rows" else
            (lambda i:anchor_span["first"]<=i<anchor_span["stop"]) if name=="sample-inverse-leaves" else
            (lambda i:False))
        chosen,ident=bound_stream(directory,ledger[name],budget,selected=selected,
            progress=progress["current_ledger"])
        all_ids[name]=ident;progress["complete_ledger_identities"].append(ident)
        if name=="far-all-mode-rows":modes=chosen
        if name=="sample-inverse-leaves":anchor_leaves=chosen
    progress["current_ledger"]=None;progress["remaining_ledgers"]=[]
    require(len(modes)==112 and len(anchor_leaves)==anchor_span["stop"]-anchor_span["first"],
        "Complete mode/anchor span was not retained")
    for leaf in anchor_leaves:
        require(leaf.get("point_index")==0 and from_word(leaf["radius_word"])==far
            and leaf.get("entire_possible_inverse_fragment_retained") is True
            and leaf.get("every_original_exact_root_choice_included") is True,
            "An actual far inverse candidate was not complete")
    span_keys={"complete_step_rows":"far-accepted-panels","complete_far_tube_rows":"far-complete-tubes",
        "complete_panel_commit_rows":"far-panel-commits","complete_far_leaf_coverage_rows":"far-inverse-leaf-coverage"}
    next_row={key:0 for key in span_keys}
    compact=[];matrix_values=[]
    for i,(mode,row) in enumerate(zip(modes,rows)):
        budget.check();m=MODES[i]
        require(mode.get("schema")==previous["schema"]+"-complete-physical-far-mode"
            and mode.get("mode_index")==i and mode.get("physical_frequency")==m
            and row.get("physical_frequency")==m,"Actual complete mode order differs")
        require(all(mode.get(k) is True for k in ("complete","complete_required_far_propagation",
            "complete_unit_row_family_enclosed","all_original_root_choices_included"))
            and mode.get("error") is None and mode.get("complete_pending_scope") is None
            and mode.get("uncommitted_transaction") is None and mode.get("row_norm_unproved_count")==0
            and mode.get("candidate_count")==mode.get("complete_unit_row_count")
            and type(mode.get("candidate_count")) is int and mode["candidate_count"]>0
            and mode.get("required_leaf_count")==mode.get("completed_leaf_count")
            and mode["required_leaf_count"]==len(anchor_leaves),
            "An original all-mode/candidate responsibility remains partial")
        require(row.get("every_candidate_amplitude_nonzero_and_sign_proved") is True
            and row.get("every_candidate_Robin_row_norm_strictly_positive_proved") is True
            and row.get("candidate_count")==mode["candidate_count"]
            and row.get("division_by_far_physical_height") is False
            and row.get("simultaneous_global_C_realization_of_numeric_rows_certified") is False,
            "The original oriented unit family or its finite scope differs")
        for value,key in ((mode,"physical_far_word"),(row,"physical_radius_word")):
            require(struct.pack("<d",from_word(value[key]))==struct.pack("<d",far)
                and struct.pack("<d",from_word(value["mu_word"]))==struct.pack("<d",mu),
                "A row used another physical far or momentum-coordinate word")
        require(row["complete_original_QF_one_unit_row"]==mode["whole_candidate_unit_row_hull"],
            "Numeric row errors belong to another complete unit family")
        for key,lname in span_keys.items():
            span=mode[key]
            require(type(span.get("first")) is int and type(span.get("stop")) is int
                and span["first"]==next_row[key] and span["stop"]>=span["first"],
                "A complete original mode ledger span was omitted")
            next_row[key]=span["stop"]
            if key in ("complete_far_tube_rows","complete_far_leaf_coverage_rows"):
                require(row[key]==span,"Numeric row refers to a different candidate/leaf span")
            require(span["stop"]<=ledger[lname]["rows"],"Original span exceeds its complete ledger")
        for key in ("uncommitted_written_step_span","uncommitted_written_far_span"):
            require(mode[key]["first"]==mode[key]["stop"],"An original uncommitted span remains")
        coefficients=[]
        for j,key in enumerate(("complete_Q_coefficient","complete_Pi_coefficient")):
            coeff=row[key];x=from_word(coeff["actual_word"])
            require(coeff["exact_real_enclosure"]==row["complete_original_QF_one_unit_row"][j],
                "Original coefficient enclosure and complete family differ")
            S.F.record_bounds(coeff["difference_exact_quantity_minus_numeric_word"])
            coefficients.append(x)
        require(coefficients[0]!=0 or coefficients[1]!=0,"No original numerical zero boundary may be manufactured")
        values=[0.0]*224;values[i]=coefficients[0];values[112+i]=coefficients[1];matrix_values.extend(values)
        compact.append(dict(physical_frequency=m,candidate_count=mode["candidate_count"],
            Q_word=row["complete_Q_coefficient"]["actual_word"]["f64le"],
            Pi_word=row["complete_Pi_coefficient"]["actual_word"]["f64le"],
            complete_far_tube_rows=mode["complete_far_tube_rows"],
            complete_far_leaf_coverage_rows=mode["complete_far_leaf_coverage_rows"]))
    for key,lname in span_keys.items():
        require(next_row[key]==ledger[lname]["rows"],"A complete original ledger suffix was not attributed")
    matrix_desc=geometry["arrays"]["far_matrix"]
    require(matrix_desc.get("completed") is True and matrix_desc.get("dtype")=="<f8"
        and matrix_desc.get("order")=="C" and matrix_desc.get("shape")==[112,224],
        "The complete original binary matrix layout differs")
    matrix_path=contained(directory,matrix_desc["file"]);matrix_raw=matrix_path.read_bytes()
    require(same_payload(dict(bytes=len(matrix_raw),sha256=hashlib.sha256(matrix_raw).hexdigest()),matrix_desc)
        and matrix_raw==b"".join(struct.pack("<d",x) for x in matrix_values),
        "The original numerical matrix differs from all112 original coefficient words")
    node_mu_desc=geometry["arrays"]["node_mu"]
    require(node_mu_desc.get("shape")==[577] and node_mu_desc.get("dtype")=="<f8"
        and node_mu_desc.get("completed") is True,"Original complete node-mu layout differs")
    node_mu_path=contained(directory,node_mu_desc["file"])
    require(same_payload(receipt(node_mu_path,budget),node_mu_desc),"Original node-mu byte identity differs")
    with node_mu_path.open("rb") as h:h.seek(576*8);last=h.read(8)
    require(node_mu_desc["bytes"]==577*8 and last==struct.pack("<d",mu),
        "The original far rows and actual numerical endpoint use different mu")
    prefix,prefix_id=member(directory,previous["finite_far_required_prefix"],budget)
    require(from_word(prefix["actual_physical_radius"])==far and prefix.get("all_possible_inverse_leaves_included") is True,
        "The original complete finite prefix identity differs")
    reuse=dict(complete=True,original_family=args.original_family,original_directory=str(directory),
        original_result=pid,original_geometry=gid,original_row_document=rid,
        original_far_matrix=copy.deepcopy(matrix_desc),original_node_mu=copy.deepcopy(node_mu_desc),
        original_required_prefix=prefix_id,original_ledger_identities=all_ids,
        original_far_inverse_span=copy.deepcopy(anchor_span),original_far_sample=copy.deepcopy(far_sample),
        physical_far_word=word(far),mu_word=word(mu),frozen_far_sample_and_mu_words=True,
        numeric_matrix_word_copy_complete=True,original_modes=MODES,complete_mode_summary=compact,
        all_candidate_errors_retained_at_original_same_job_paths=True,
        complete_original_factor_coefficient_streams_hashed_not_numerically_reproved=True,
        full_root_family_not_narrowed=True,M_changed=False,native_response_J_state_factors_reused=False)
    report["same_original_far_family_reuse"]=reuse
    return dict(previous=previous,geometry=geometry,rows=rows_doc,row_descriptor=rowdesc,
        far_sample=far_sample,far=far,cut=cut,mu=mu,matrix_raw=matrix_raw,reuse=reuse,
        family=args.original_family,original_directory=directory)

def raw_copy(path,raw,shape):
    require(len(raw)==math.prod(shape)*8,"Raw word copy shape differs")
    with Path(path).open("xb") as h:h.write(raw);h.flush();os.fsync(h.fileno())
    return dict(file="large-arrays/"+Path(path).name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),
        dtype="<f8",order="C",shape=shape,completed=True)

def fresh_grid(args,report,budget,S,data,old,journals):
    F,B=S.F,S.B;cb=data["core"]
    head=B.ContinuousHead(cb["physical_parameters"],cb["original_shallow_rows"],cb["original_frozen_warp_alpha"],cb)
    geom=F.GeometryCache(head,data["panels"],args,journals["coefficient-boxes"],budget)
    sampler=S.InverseSampler(head,data,args,geom,journals["sample-inverse-leaves"],
        journals["complete-unpaid-scope"],budget)
    anchor=copy.deepcopy(old["far_sample"])
    anchor["point_enclosure_origin"]=dict(kind="retained-original-same-job-far-anchor",
        original_directory=str(old["original_directory"]),original_result=old["reuse"]["original_result"],
        original_inverse_ledger=old["reuse"]["original_ledger_identities"]["sample-inverse-leaves"],
        all_closed_inverse_leaves=copy.deepcopy(anchor["all_closed_inverse_leaves"]),
        interval_error_and_numeric_words_unchanged=True)
    sampler.cache[word(old["far"])["f64le"]]=anchor;sampler.point_count=1
    report["far_point_sample"]=anchor;report["actual_far_coordinate_mu_word"]=word(old["mu"])
    nodes,grid,grid_identity=S.radial_grid(old["far"],old["cut"],args.steps)
    # The original helper owns this grid formula. Its schema remains a truthful
    # callee identity; the enclosing result/geometry identity is independently R450.
    plan=write_json(args.out/"actual-radial-field-plan.json",dict(schema=SCHEMA+"-complete-field-plan",
        original_grid_helper_source=SOURCES[args.original_family],grid_identity=grid_identity,
        nodes=[word(x) for x in nodes],stages=grid))
    report.update(grid_identity=grid_identity,actual_field_plan=plan,
        original_grid_helper_schema_not_relabelled=True,
        native_plan_address=dict(phase="nodes",next_node=0,node_stop=577,
            next_stage=0,stage_stop=576,next_field=0,all_fields_required=True,field_plan=plan))
    progress=report["native_plan_address"];mu=[];field_count=0
    try:
        for n,r in enumerate(nodes):
            progress.update(phase="nodes",next_node=n)
            s=sampler.sample(r,"R450-actual-node-"+str(n))
            value=(old["mu"] if word(r)["f64le"]==word(old["far"])["f64le"]
                else math.exp(7*math.log(r)+s["numerical"]["logw"]))
            require(math.isfinite(value) and value>0,"Actual numerical node mu is unavailable")
            mu.append(value);progress["next_node"]=n+1
        require(struct.pack("<d",mu[-1])==struct.pack("<d",old["mu"]),"Original boundary coordinate was changed")
        stage_packets=[];field_words=[];field_width=None
        for n,stage in enumerate(grid):
            progress.update(phase="fields",next_stage=n,next_field=0,field_stop=len(stage["fields"]))
            budget.check()
            ratio=mu[n]/mu[n+1]
            require(math.isfinite(ratio) and ratio>0,"Actual momentum-coordinate port is unavailable")
            packet=dict(stage=n,rawCell=stage["rawCell"],rawSegment=stage["rawSegment"],
                shootingSubsegment=stage["shootingSubsegment"],fields=[],mu_word=word(mu[n+1]),
                output_node_mu_word=word(mu[n]),port_ratio_word=word(ratio))
            for j,entry in enumerate(stage["fields"]):
                progress["next_field"]=j
                sample=sampler.sample(entry["r_word"]["value"],"R450-stage-"+str(n)+"-field")
                logw=sample["numerical"]["logw"]
                dlog=entry["drdx_word"]["value"]*sample["numerical"]["dlogwdr"]
                require(math.isfinite(dlog),"Actual finite dlogwdx overflow")
                true_dlogwdx=B.exact(Q(entry["drdx_word"]["value"]))*F.as_ball(
                    sample["numerical_word_receipts"]["dlogwdr"]["exact_real_enclosure"])
                record=dict(stage=n,field_index=j,x_word=entry["x_word"],r_word=entry["r_word"],
                    drdx_word=entry["drdx_word"],logw_word=word(logw),dlogwdx_word=word(dlog),
                    same_C_sample=sample,complete_target_dlogwdx=B.record(true_dlogwdx),
                    target_dlogwdx_minus_actual_numeric_word=B.record(true_dlogwdx-B.exact(Q(dlog))),
                    finite_derived_dlogwdx_rounding_not_an_exact_derivative_identity=True)
                journals["numeric-point-values-and-errors"].add(record)
                packet["fields"].append(dict(x_word=entry["x_word"],point_index=sample["point_index"]))
                field_words.extend([entry["x_word"]["value"],entry["r_word"]["value"],
                    entry["drdx_word"]["value"],logw,dlog])
                field_count+=1;progress["next_field"]=j+1
                report["complete_native_field_occurrences"]=field_count
            if field_width is None:field_width=len(stage["fields"])
            require(field_width==len(stage["fields"]),"The original full stage width changed")
            stage_packets.append(packet);progress["next_stage"]=n+1;progress["next_field"]=0
        progress["phase"]="array_materialization"
        budget.check();large=args.out/"large-arrays"
        arrays=dict(node_radii=S.raw_array(large/"node-radii.f64le",nodes,[577]),
            node_mu=S.raw_array(large/"node-mu.f64le",mu,[577]),
            field_geometry=S.raw_array(large/"full-stage-field-geometry.f64le",field_words,[576,field_width,5]),
            far_matrix=raw_copy(large/"complete-general-far-matrix.f64le",old["matrix_raw"],[112,224]))
        require(arrays["far_matrix"]["sha256"]==old["reuse"]["original_far_matrix"]["sha256"],
            "The retained original finite boundary matrix changed words")
        row_raw=contained(old["original_directory"],old["row_descriptor"]["file"]).read_bytes()
        row_path=args.out/"retained-general-far-row-intervals-and-representatives.json"
        with row_path.open("xb") as h:h.write(row_raw);h.flush();os.fsync(h.fileno())
        row_receipt=receipt(row_path,budget)
        require(same_payload(row_receipt,old["reuse"]["original_row_document"]),
            "The retained row document changed while being used")
        geometry_identity=dict(schema=SCHEMA+"-numeric-geometry-identity",
            sampler_source_sha256=report["source_sha256"],actual_source_binding=data["binding"],
            original_C_model=MODEL,actual_radial_field_plan=plan,
            all_point_enclosures_and_representative_errors=journals["numeric-point-values-and-errors"].finish(),
            general_far_row_enclosures_and_representatives=row_receipt,
            reused_far_family=old["reuse"],complete_native_arrays=arrays,
            exact_global_C_realization_of_numeric_representatives_certified=False,
            finite_evaluator_error_not_paid_by_native_residual=True,
            every_actual_C_point_and_far_row_is_interval_enclosed=True,
            actual_original_engine_exp_and_exp_twice_logw_rounding_error_certified=False,
            original_engine_must_record_its_actual_w_w2_E_words=True)
        far_identity=copy.deepcopy(old["geometry"]["far_identity"])
        far_identity.update(general_rows=row_receipt,complete_all112_general_matrix=arrays["far_matrix"],
            R450_actual_original_far_identity_retained=True,reuse_receipt=old["reuse"])
        geometry=dict(schema=S.GEOMETRY_SCHEMA,model_schema=MODEL,modes=112,spacing=2,orientation=1,
            stage_count=576,rawNode=[72*i for i in range(9)],cut_radius=old["cut"],finite_far_radius=old["far"],
            native_old_graphs_or_gains_used=False,original_C_input_binding=data["binding"],
            numeric_geometry_identity=geometry_identity,arrays=arrays,stage_packets=stage_packets,
            field_columns=["x","r","drdx","logw","dlogwdx"],steps_per_stage=args.steps,
            field_count_per_stage=field_width,
            coordinate_mu_rule="original far mu word retained; all other nodes use actual binary64 exp(7 log(r)+fresh logw)",
            finite_far_rows_are_nondividing_approximations_with_bound_error=True,
            exact_global_same_C_and_infinite_nonlinear_DN_not_certified=True,far_identity=far_identity)
        budget.check()
        report.update(geometry=write_json(args.out/"geometry.json",geometry),
            completed=True,native_geometry_ready=True,complete_unique_sample_points=sampler.point_count,
            freshly_computed_unique_points=sampler.point_count-1,
            numerical_sample_work_resolution_complete=all(x["work_resolution_complete"] for x in sampler.cache.values()))
        progress.update(phase="complete",next_stage=576,next_field=0)
    finally:
        report.update(actual_point_count=sampler.point_count,actual_fresh_point_count=sampler.point_count-1,
            actual_inverse_range_count=sampler.range_count,actual_fresh_coarse_valid_point_leaves=sampler.coarse_count)

def sample(args):
    require_actions();started=time.monotonic();args.out=temporary(args.out,False)
    require(not args.out.exists(),"Fresh exclusively owned R450 output required")
    for key in ("steps","sample_max_nodes","max_geometry_cache_records"):
        require(type(getattr(args,key)) is int and getattr(args,key)>0,"Positive finite original sampling capacity required")
    require(type(args.precision_bits) is int and 64<=args.precision_bits<=4096
        and 0<=args.sample_inverse_depth<=60 and 0<=args.sample_value_bits<=1024
        and args.free_bytes_reserve>=0 and math.isfinite(args.budget_seconds) and args.budget_seconds>0,
        "Explicit valid work resources required")
    args.code_directory=args.code_directory.resolve(strict=True)
    for key in ("cover_directory","far_directory","original_sampling_directory"):
        setattr(args,key,temporary(getattr(args,key)))
    inputs=[getattr(args,k) for k in ("cover_directory","far_directory","original_sampling_directory")]
    require(all(args.out!=p and args.out not in p.parents and p not in args.out.parents for p in inputs),
        "Owned output must not overlap any actual input")
    args.out.mkdir(parents=True);(args.out/"large-arrays").mkdir()
    report=dict(schema=SCHEMA,source_sha256=receipt(__file__)["sha256"],target_model_schema=MODEL,
        repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        completed=False,native_geometry_ready=False,error=None,old_graphs_or_gains_used=False,
        no_height_division_in_far_rows=True,exact_global_C_realization_of_numeric_representatives_certified=False,
        nonlinear_solve_or_DN_computed=False,closed_field_or_BVP_accepted=False,
        old_native_response_J_or_factor_reused=False,same_original_far_family_reuse=None,
        complete_native_field_occurrences=0,actual_far_modes_attempted=[],actual_far_modes_completed=[],
        native_plan_address=dict(phase="source_binding",all577_nodes_and_all576_stages_unstarted=True,
            requested_steps=args.steps,complete_new_field_plan_not_yet_formed=True),
        declared_fresh_sampling=dict(precision_bits=args.precision_bits,steps=args.steps,
            sample_max_nodes=args.sample_max_nodes,sample_inverse_depth=args.sample_inverse_depth,
            sample_value_bits=args.sample_value_bits,max_geometry_cache_records=args.max_geometry_cache_records),
        no_linear_far_propagation_performed_in_this_call=True,
        no_native_response_or_acceptance_implied=True,raw_cleanup_performed=False)
    journals={};budget=None;code=2
    try:
        absolute,clock=bind_clock(args);report.update(clock)
        budget=Budget(args,absolute,started);budget.install();budget.check()
        S,runtime,sources,proof=load_sampler(args.code_directory,args.original_family,args)
        budget.check();data=S.F.bind_inputs(args);budget.check()
        report.update(runtime=runtime,frozen_sources=sources,original_sampling_helper=SOURCES[args.original_family],
            actual_R380_proof=proof["Pruefer_propagation"],actual_R357_proof=proof["oriented_unit_Robin_rows"],
            actual_original_input_binding=data["binding"],actual_original_scope_conditions=data["facts"])
        for name in ("coefficient-boxes","sample-inverse-leaves","numeric-point-values-and-errors","complete-unpaid-scope"):
            journals[name]=S.B.Journal(args.out/"large-arrays"/(name+".jsonl"),args.out)
        if not data["ready"]:
            journals["complete-unpaid-scope"].add(dict(kind="original-full-C-or-deep-scope-not-complete",
                all_required_modes=MODES,actual_original_scope_conditions=data["facts"],
                all_native_stages_unstarted=[0,576],no_coverage_or_root_condition_assumed=True))
        else:
            old=bind_original_far(args,report,budget,S,data)
            report["reused_complete_far_modes"]=MODES
            fresh_grid(args,report,budget,S,data,old,journals)
            code=0
    except Exception as failure:
        code=75 if isinstance(failure,ResourceStop) else 2
        report["error"]=dict(type=type(failure).__name__,message=str(failure),
            resource_partial=isinstance(failure,ResourceStop),mathematical_refutation_not_inferred=True)
        if "complete-unpaid-scope" in journals:
            journals["complete-unpaid-scope"].add(dict(kind="R450-complete-fresh-grid-unfinished",
                error=report["error"],complete_native_plan_address=report["native_plan_address"],
                complete_original_reuse_binding_progress=report.get("reuse_binding_progress"),
                exact_current_inverse_stack_if_started_is_in_same_original_unpaid_ledger=True))
    finally:
        if budget is not None:budget.finish();budget.restore()
        report.update(detailed_ledgers={name:j.finish() for name,j in journals.items()},
            resource_receipt=None if budget is None else budget.record(),elapsed_seconds=time.monotonic()-started,
            internal_exit_code=code,raw_owned_temporary_only=True,new_nonlinear_acceptance_gate=False)
        rid=write_json(args.out/"result.json",report)
        print(json.dumps(dict(event="R450-same-far-fresh-grid-returned",result=rid,
            completed=report["completed"],native_geometry_ready=report["native_geometry_ready"],
            fresh_far_modes_attempted=[],reused_modes=report.get("reused_complete_far_modes",[]),
            internal_exit_code=code,error=report["error"])),flush=True)
    return code

def configure(args):
    """Make an independently sourced finite-native config; no native call is made."""
    require_actions();directory=temporary(args.directory);out=temporary(args.out,False)
    require(not out.exists(),"Fresh native configuration output required")
    result,rid=read_json(directory/"result.json",args.result_sha256);actual_identity(result)
    require(result.get("schema")==SCHEMA and result.get("source_sha256")==receipt(__file__)["sha256"]
        and result.get("completed") is True and result.get("native_geometry_ready") is True,
        "Use this actual completed R450 result")
    cfg,cid=read_json(temporary(args.original_config),args.original_config_sha256)
    require(cfg.get("schema")=="current-C-complete112-client-config-v1"
        and cfg.get("model_schema")==MODEL and cfg.get("repository")==REPOSITORY,
        "Actual original current-C native configuration required")
    original,pid=read_json(temporary(cfg["geometry_directory"])/"result.json",cfg["geometry_result_sha256"])
    actual_identity(original)
    require(same_payload(pid,result["same_original_far_family_reuse"]["original_result"]),
        "The configuration does not belong to the retained original far geometry")
    comp=args.computations.resolve(strict=True)
    require(comp==Path(cfg["computations"]).resolve(strict=True),"Actual computation source directory changed")
    for name,digest in cfg["source_sha256"].items():
        require(Path(name).name==name and receipt(comp/name)["sha256"]==digest,"Original native source differs: "+name)
    require(type(args.quadrature) is int and args.quadrature>896 and args.quadrature%2==0,
        "Use the original full-angle native quadrature condition")
    new=copy.deepcopy(cfg)
    for name,digest in NATIVE_PINS.items():
        require(receipt(comp/name)["sha256"]==digest,"Independent native source differs: "+name)
        new["source_sha256"][name]=digest
    require(receipt(comp/ENTRY)["sha256"]==result["source_sha256"],"Actual R450 sampler source differs")
    new["source_sha256"][ENTRY]=result["source_sha256"]
    geometry,_=member(directory,result["geometry"])
    new.update(geometry_directory=str(directory),geometry_result_sha256=rid["sha256"],
        quadrature=args.quadrature,steps=geometry["steps_per_stage"],
        R450_same_far_fresh_grid_origin=dict(original_config=cid,original_sampling_result=pid,
            actual_R450_result=rid,independent_client=dict(file=CLIENT,sha256=NATIVE_PINS[CLIENT]),
            original_native_owner_bridge_QR_and_runtime_unchanged=True,
            old_native_states_responses_J_and_factors_not_reused=True,
            frozen_R441_R448_caller_registration_not_performed=True))
    out.parent.mkdir(parents=True,exist_ok=True)
    ident=write_json(out,new)
    print(json.dumps(dict(event="R450-explicit-native-configuration-created",configuration=ident,
        client=CLIENT,no_native_call_performed=True)),flush=True)
    return 0

def readback(args):
    """One necessary metadata document. Original large candidate bodies stay in Actions."""
    require_actions();directory=temporary(args.directory);out=temporary(args.out,False)
    require(not out.exists(),"Fresh necessary-readback directory required");out.mkdir(parents=True)
    result,rid=read_json(directory/"result.json",args.result_sha256);actual_identity(result)
    require(result.get("schema")==SCHEMA and result.get("source_sha256")==receipt(__file__)["sha256"],
        "Use the actual independent R450 producer")
    selected_keys=("target_model_schema","repository","run_id","source_commit","source_sha256",
        "completed","native_geometry_ready","error","internal_exit_code","elapsed_seconds",
        "declared_fresh_sampling","actual_origin_launch","actual_job_deadline","original_clock",
        "actual_original_scope_conditions","resource_receipt","native_plan_address",
        "complete_native_field_occurrences","complete_unique_sample_points","freshly_computed_unique_points",
        "numerical_sample_work_resolution_complete","actual_point_count","actual_fresh_point_count",
        "actual_inverse_range_count","actual_fresh_coarse_valid_point_leaves",
        "old_native_response_J_or_factor_reused","no_native_response_or_acceptance_implied",
        "actual_far_modes_attempted","actual_far_modes_completed","reused_complete_far_modes",
        "no_linear_far_propagation_performed_in_this_call","raw_cleanup_performed")
    necessary={k:result[k] for k in selected_keys if k in result}
    reuse=result.get("same_original_far_family_reuse")
    if reuse is not None:
        keys=("complete","original_family","original_result","original_geometry","original_row_document",
            "original_far_matrix","original_node_mu","original_required_prefix","original_far_inverse_span",
            "physical_far_word","mu_word","frozen_far_sample_and_mu_words","numeric_matrix_word_copy_complete",
            "original_modes","complete_mode_summary","full_root_family_not_narrowed","M_changed")
        necessary["same_original_far_family_reuse"]={k:reuse[k] for k in keys if k in reuse}
        necessary["original_reused_ledger_identities"]={k:v["descriptor"] for k,v in reuse["original_ledger_identities"].items()}
        necessary["original_far_sample_identity"]={"bytes":len(canonical(reuse["original_far_sample"])),
            "sha256":hashlib.sha256(canonical(reuse["original_far_sample"])).hexdigest(),
            "identity_scope":"canonical original result member, not a separate producer file"}
    if result.get("reuse_binding_progress") and reuse is None:
        necessary["reuse_binding_progress"]=result["reuse_binding_progress"]
    ledger_identities={};unpaid=[]
    for name,desc in result["detailed_ledgers"].items():
        path=contained(directory,desc["file"]);h=hashlib.sha256();size=rows=0
        with path.open("rb") as stream:
            for raw in stream:
                h.update(raw);size+=len(raw);rows+=1
                require(raw.endswith(b"\n"),"Unfinished actual generated ledger")
                if name=="complete-unpaid-scope":unpaid.append(json.loads(raw))
        require((size,rows,h.hexdigest())==(desc["bytes"],desc["rows"],desc["sha256"]),
            "Actual complete generated ledger identity differs")
        ledger_identities[name]=desc
    necessary["complete_unpaid_records"]=unpaid
    necessary["complete_generated_ledger_identities"]=ledger_identities
    if "geometry" in result:
        geometry,gid=member(directory,result["geometry"])
        for desc in geometry["arrays"].values():
            require(same_payload(receipt(contained(directory,desc["file"])),desc),"Complete generated array identity differs")
        necessary["actual_complete_geometry"]=dict(identity=gid,arrays=geometry["arrays"],
            steps_per_stage=geometry["steps_per_stage"],field_count_per_stage=geometry["field_count_per_stage"],
            numeric_point_and_candidate_bodies_not_returned=True,
            every_large_payload_byte_hashed_not_independently_numerically_recomputed=True)
    summary=dict(schema=READBACK_SCHEMA,producer_result=rid,original=necessary,
        selected_original_keys=list(necessary),missing_keys_not_filled=True,
        original_large_far_candidate_and_factor_streams_remain_temporary=True,
        no_raw_cleanup_performed=True,no_new_scientific_gate=True)
    raw=canonical(summary);ident=write_json(out/"summary.json",summary)
    if len(raw)>90000:
        print(json.dumps(dict(event="R450-necessary-readback-over-budget",bytes=len(raw),
            sha256=hashlib.sha256(raw).hexdigest(),complete_readback_transported=False,
            no_partial_body_disguised_as_complete=True)),flush=True)
        return 70
    print("BEGIN_R450_SAME_FAR_FRESH_GRID_NECESSARY",flush=True)
    print(raw.decode(),end="",flush=True)
    print("END_R450_SAME_FAR_FRESH_GRID_NECESSARY",flush=True)
    print(json.dumps(dict(event="R450-necessary-summary-identity",summary=ident)),flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"],"a") as stream:
            stream.write("same_far_summary_bytes="+str(ident["bytes"])+"\n")
            stream.write("same_far_summary_sha256="+ident["sha256"]+"\n")
    return 0

def parser():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest="command",required=True)
    run=sub.add_parser("sample")
    for key in ("cover-directory","far-directory","original-sampling-directory","code-directory",
                "proof","unit-row-proof","origin-launch-directory","job-deadline","out"):
        run.add_argument("--"+key,type=Path,required=True)
    for key in ("cover-result-sha256","far-result-sha256","original-sampling-result-sha256",
                "origin-launch-result-sha256","job-deadline-sha256"):
        run.add_argument("--"+key,required=True)
    run.add_argument("--original-family",choices=tuple(SOURCES),required=True)
    for key in ("steps","precision-bits","sample-max-nodes","sample-inverse-depth",
                "sample-value-bits","max-geometry-cache-records","free-bytes-reserve"):
        run.add_argument("--"+key,type=int,required=True)
    run.add_argument("--budget-seconds",type=float,required=True)
    cfg=sub.add_parser("configure")
    for key in ("directory","original-config","computations","out"):cfg.add_argument("--"+key,type=Path,required=True)
    for key in ("result-sha256","original-config-sha256"):cfg.add_argument("--"+key,required=True)
    cfg.add_argument("--quadrature",type=int,required=True)
    rb=sub.add_parser("readback")
    for key in ("directory","out"):rb.add_argument("--"+key,type=Path,required=True)
    rb.add_argument("--result-sha256",required=True)
    return p

def main(argv=None):
    args=parser().parse_args(argv)
    return {"sample":sample,"configure":configure,"readback":readback}[args.command](args)

if __name__=="__main__":
    raise SystemExit(main())
