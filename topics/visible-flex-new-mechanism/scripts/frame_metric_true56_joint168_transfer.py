#!/usr/bin/env python3
"""Restore actual56 and its fixed-reference source; import-only, no science replay.

The current56 log supplies current168, original gates, selected pools, and
paid U/T/e/f.  A second original55 COMPLETE supplies the unchanged permanent
reference/height-map constructor data omitted from56's small checkpoint.
Neither old geometry nor any old J/model/optimizer is called.
"""
from __future__ import annotations
import copy
import io
from fractions import Fraction as Q
from pathlib import Path
import time
import numpy as np
import read_original_actions_log as reader
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import RationalRowGrid, array_digest
from frame_direct_reference_geometry159 import DirectReferenceFiveHeightField
from frame_complete_body_extension168 import CompleteBody168Field
import frame_metric_paid_cone_vector_audit as paid
import frame_metric_direct_reference_audit as direct_audit
import frame_metric_curvature_defect_guard_transfer as inherited
import frame_metric_height159_complete_affine_audit as baseline
from frame_metric_true56_joint168_scope import POLICY, Joint168Ledger, require

REPO="Rogerhu12/math-research-public"
PINS={"run_id":"43842056373","job_id":"133212892062",
      "source_commit":"86852956f10ec609ba423990a40327284f081c44",
      "workflow":".github/workflows/visible-true55-nine-fiber.yml",
      "log_bytes":53920117,
      "log_sha256":"53abf31d239449f7a1c4cddb2b3dd788438e403d6358566296afba7e4c84a042"}
RECORDS=[
 {"tag":"COMPLETE","ordinal":1,"JSON_plus_LF_bytes":2228819,
  "JSON_plus_LF_sha256":"05b4501ecb40ae2c725c4c37a361f2833cab09a77f47bc932abe5ca6c0865fd5"},
 {"tag":"CACHE","ordinal":2,"JSON_plus_LF_bytes":29867329,
  "JSON_plus_LF_sha256":"c8ad34a26c6f5ade483d07189bc718bd13c3bec1c24caa0b9ff3aaa949337a4e"},
 {"tag":"FINAL_CLOCK","ordinal":1,"JSON_plus_LF_bytes":41633,
  "JSON_plus_LF_sha256":"94b4a055732cf3214eee935aa817b4ae0aac49ca807d475f4ba6eed145f6a381"}]
SOURCE_REQUEST={"path":"topics/visible-flex-new-mechanism/computations/request-true55-nine-fiber.json",
                "bytes":61536,
                "sha256":"796219c241c4485d12181f035ca7cdd0b2790972334c9afd8efc44628f286d39"}
ANCHOR_PINS={"run_id":"43832870561","job_id":"133182173190",
 "source_commit":"23b37e90cbc1ac33ca6ff8ac1f91fa7a95c903db",
 "workflow":".github/workflows/visible-true54-fresh-model.yml",
 "log_bytes":81300477,
 "log_sha256":"36bfb2269d5a85c52116066e521c9ffdce4f9c99dc35866a11d31e0830928ce2"}
ANCHOR_RECORD={"tag":"COMPLETE","ordinal":1,"JSON_plus_LF_bytes":5388242,
 "JSON_plus_LF_sha256":"a7819f1e04a97c5003e4058fb3c1df17a9841c5b6006790875a98cee27622b4b"}
PHYSICAL_SHA="11c07425846f224c2d05997068b6442fa28a65383b5af5dce3eb2789da0593dd"
STATE_SHA="aa7d8f3fb4d1bfea7aa4a05fef3b23babefbc344c5ea78f7b321b141a2d5181b"
COORDINATE_SHA="c69967fb9b864f3e95da411610b74d5477c58891352895b493aee6e482d960de"
CFG_SHA="1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19"
FIELD_SHA="81e6881cd1f36d87a865cd9cc8c51ee8480d2ac8278241d97fb19666486eba8d"
OBJECTIVE_SHA="812add123c552afc4e7d7cce1c2cd19f9bbbb3e445fc179e73615cafbd122b4f"
CACHE_BINDING="a6465ff91278055caf0c64e374751901f06e23361b760d3414c89c4e87020b60"
ANCESTOR_SECONDS=2233.566394556
ANCESTOR_VALUES=138
SOURCE_STATUS="complete-true55-new9-fiber-original-actual-observation"
GRID_SHAPES={"coarse":(160,384),"fine":(160,768)}

def exact_binary64(values,length):
    require(isinstance(values,list) and len(values)==length
            and all(isinstance(v,str) for v in values),"complete exact binary64 vector required")
    qs=[Q(v) for v in values]
    a=np.asarray([float(v) for v in qs],dtype=np.float64)
    require(np.all(np.isfinite(a)) and all(
        Q.from_float(float(v))==q for v,q in zip(a,qs)),"source binary64 reconstruction differs")
    return a

def _read_records(api,pins,prefix,expected,ledger,progress):
    ledger.check("source.metadata")
    run=api.api_json("/actions/runs/"+pins["run_id"])
    job=api.api_json("/actions/jobs/"+pins["job_id"])
    require(str(run["id"])==str(job["run_id"])==pins["run_id"]
        and str(job["id"])==pins["job_id"]
        and run["head_sha"]==job["head_sha"]==pins["source_commit"]
        and run["status"]==job["status"]=="completed"
        and run["conclusion"]==job["conclusion"]=="success"
        and run["path"]==pins["workflow"],"completed original source identity differs")
    progress["original_logs_requested"]+=1
    raw,redirects=api.job_log(pins["job_id"])
    require(len(raw)==pins["log_bytes"] and reader.digest(raw)==pins["log_sha256"],
            "original research stdout identity changed")
    wanted={(x["tag"],x["ordinal"]):x for x in expected}
    found,counts,receipts={},{},[]
    for line in io.StringIO(raw.decode("utf-8-sig")):
        clean=reader.ANSI.sub("",line.rstrip("\r\n")).lstrip("\ufeff")
        m=reader.TIME_PREFIX.match(clean)
        if m is None: continue
        body=m.group(2).lstrip("\ufeff")
        if not body.startswith(prefix): continue
        tag,sep,payload=body[len(prefix):].partition(" ")
        if not sep: continue
        counts[tag]=counts.get(tag,0)+1
        key=(tag,counts[tag])
        if key not in wanted: continue
        ledger.check("source.decode")
        literal=payload.encode("utf-8")+b"\n"
        pin=wanted[key]
        require(len(literal)==pin["JSON_plus_LF_bytes"]
                and reader.digest(literal)==pin["JSON_plus_LF_sha256"],
                "original source record identity changed: "+str(key))
        found[key]=reader.decode_json(literal)
        receipts.append(copy.deepcopy(pin))
    require(set(found)==set(wanted) and counts.get("COMPLETE")==1,
            "unique complete original source records required")
    progress.setdefault("reads",[]).append({"source":copy.deepcopy(pins),
        "records":receipts,"redirect_count_without_forwarding_authorization":redirects})
    ledger.check("source.decoded")
    return found,receipts

def read_source(request,ledger,*,capture=None):
    require(isinstance(ledger,Joint168Ledger),"one new joint168 account required")
    progress={} if capture is None else capture
    require(not progress,"fresh input capture required")
    started=time.monotonic()
    progress.update(status="started",original_logs_requested=0,
        ordinary_geometry_calls=0,old_J_model_optimizer_or_development_calls=0)
    try:
        require(request["source"]==PINS and request["source_records"]==RECORDS
            and request["source_request"]==SOURCE_REQUEST
            and request["fixed_reference_source"]==ANCHOR_PINS
            and request["fixed_reference_record"]==ANCHOR_RECORD,
            "current56 and its fixed-reference sources must be literal")
        raw_request=Path(SOURCE_REQUEST["path"]).read_bytes()
        require(len(raw_request)==SOURCE_REQUEST["bytes"]
            and reader.digest(raw_request)==SOURCE_REQUEST["sha256"],
            "the complete source56 request differs")
        old_request=reader.decode_json(raw_request)
        require(request["original_input_arguments"]==old_request["original_input_arguments"]
            and len(request["original_input_arguments"])==98
            and request["fixed_complete_metric_sha256"]==old_request["fixed_complete_metric_sha256"]
            and request["fixed_b0_definition_sha256"]==old_request["fixed_b0_definition_sha256"],
            "all24 original inputs and g/b0 must remain")
        api=reader.GitHubReader(REPO)
        rec,receipts=_read_records(api,PINS,"TRUE55_NINE_",RECORDS,ledger,progress)
        real,cache,clock=rec[("COMPLETE",1)],rec[("CACHE",2)],rec[("FINAL_CLOCK",1)]
        require(real["status"]==clock["status_at_final_emit"]==SOURCE_STATUS
            and not clock["scope_exhausted"]
            and clock["sampled_after_all_large_cache_and_complete_write_and_flush"] is True
            and real["github_sha"]==PINS["source_commit"]
            and str(real["github_run_id"])==PINS["run_id"]
            and real["github_repository"]==REPO
            and real["new_acceptances"]==1
            and real["old_checks_executed"]==real["new_development_executed"]==0
            and real["source_files_sha256"]==old_request["source_sha256"],
            "original actual56 outcome/source differs")
        final=clock["ledger"]
        require(final["total_ancestor_plus_new_scientific_seconds"]==ANCESTOR_SECONDS
            and final["total_source_plus_new_started_values"]==ANCESTOR_VALUES
            and final["scientific_seconds"]==160.00398343599997
            and final["started_counts"]["actual_trial_pairs"]==1
            and final["started_counts"]["actual_grid_values"]==2,
            "the closed source56 final account differs")
        point=real["selected_two_grid_physical_point"]
        require(point==real["actual_stage"]["selected_two_grid_physical_point"]
            and point["accepted_index"]==56 and point["physical_state_sha256"]==PHYSICAL_SHA
            and point["coordinate_definition_sha256"]==COORDINATE_SHA
            and point["complete_new_field_evaluation_sha256"]==FIELD_SHA
            and point["objective_evaluation_sha256"]==OBJECTIVE_SHA
            and digest(real["configuration"])==CFG_SHA,
            "current complete168 physical/evaluation identity differs")
        state=exact_binary64(point["exact_binary64_independent168_coordinates"],168)
        require(array_digest(state)==STATE_SHA
            and np.asarray(point["independent_coordinates_binary64"],dtype=float).tobytes()==state.tobytes()
            and np.any(state[159:]!=0.),"actual56 has all168 coordinates and nonzero new9")
        gates={}
        for label in GRID_SHAPES:
            d=point[label]
            require(len(d["actual_gate_booleans"])==14
                and all(v is True for v in d["actual_gate_booleans"].values())
                and d["exact_full172_physical_box_pass"] is True,
                "all original actual56 fourteen gates and exact172 box required")
            gates[label]=copy.deepcopy(d)
        trials=[x for x in real["actual_stage"]["trials"] if x.get("accepted_as_next_iterate")]
        require(len(trials)==1 and trials[0]["accepted_index"]==56
            and trials[0]["physical_state_sha256"]==PHYSICAL_SHA
            and trials[0]["state"]["independent168_exact"]==
                point["exact_binary64_independent168_coordinates"],
            "one original accepted56 actual trial must match")
        require(cache["kind"]=="accepted-point-paid-geometry"
            and cache["available"] is True and cache["status"]=="complete"
            and cache["binding_sha256"]==CACHE_BINDING and digest(cache["binding"])==CACHE_BINDING,
            "the current56 CACHE2 identity differs")
        binding=cache["binding"]
        for key,value in {"accepted_index":56,"physical_state_sha256":PHYSICAL_SHA,
                "independent168_array_sha256":STATE_SHA,"coordinate_definition_sha256":COORDINATE_SHA,
                "field_evaluation_sha256":FIELD_SHA,"objective_evaluation_sha256":OBJECTIVE_SHA,
                "original_cfg_sha256":CFG_SHA}.items():
            require(binding[key]==value,"accepted cache binding differs: "+key)
        saved=cache["accepted_independent168"]
        require(saved["shape"]==[168] and saved["dtype"]=="float64"
            and saved["array_sha256"]==STATE_SHA
            and np.asarray(saved["values"],dtype=float).tobytes()==state.tobytes(),
            "the current cache state differs")
        for label,(nr,nt) in GRID_SHAPES.items():
            rows=cache["grids"][label]
            shapes={"U":[nr,nt,3],"T":[nr,nt,3],"e":[nr*nt],"f":[nr*nt],
                    "radial":[nr],"theta":[nt]}
            require(set(rows)==set(shapes),"original accepted first-jet arrays changed")
            for key,shape in shapes.items():
                require(rows[key]["shape"]==shape and rows[key]["dtype"]=="float64"
                    and rows[key]["array_sha256"]==binding["grid_array_sha256"][label][key],
                    "current first-jet metadata changed")
        receipt=real["accepted_cache_stdout_receipt"]
        cache_pin=next(x for x in RECORDS if x["tag"]=="CACHE")
        require(receipt["JSON_plus_LF_bytes"]==cache_pin["JSON_plus_LF_bytes"]
            and receipt["JSON_plus_LF_sha256"]==cache_pin["JSON_plus_LF_sha256"]
            and receipt["binding_sha256"]==CACHE_BINDING and receipt["accepted_index"]==56,
            "COMPLETE must point to this exact accepted56 CACHE2")
        # Only the original55 COMPLETE is decoded: it carries permanent reference
        # constructor data absent from the56 checkpoint, not a current derivative.
        anchor_records,anchor_receipts=_read_records(
            api,ANCHOR_PINS,"TRUE54_FRESH_",[ANCHOR_RECORD],ledger,progress)
        anchor_real=anchor_records[("COMPLETE",1)]
        cp=anchor_real["future_fresh54_checkpoint"]
        require(real["future_source_restoration"]["original55_source"]==ANCHOR_PINS
            and real["source55_actual_point"]==anchor_real["selected_two_grid_physical_point"]
            and cp["selected_two_grid_physical_point"]==real["source55_actual_point"]
            and cp["configuration"]==real["configuration"]
            and exact_binary64(cp["selected_final159_binary64_exact"],159).tobytes()==state[:159].tobytes()
            and cp["selected_accepted_index"]==55,
            "the fixed-reference source must be the exact retained old159 part")
        require((len(real["actual_stage"]["coarse_pool"]),len(real["actual_stage"]["fine_pool"]),
            real["actual_stage"]["coarse_pool_version"],real["actual_stage"]["fine_pool_version"])
            ==(4453,4549,14,14),"current56 complete selected pools differ")
        cost={"ancestor_final_original_scientific_seconds":ANCESTOR_SECONDS,
            "source_global_scientific_seconds":ANCESTOR_SECONDS,
            "source_original_full_values":ANCESTOR_VALUES,"source_original_values":ANCESTOR_VALUES,
            "source_final_clock":copy.deepcopy(clock),
            "closed_source55_nine_fiber_task_not_reopened":True,
            "earlier_checkpoint_samples_not_added_to_final_clock":True}
        source_receipt={"schema":POLICY+"-actual56-source","passed":True,
            "source":copy.deepcopy(PINS),"source_records":receipts,
            "fixed_reference_source":copy.deepcopy(ANCHOR_PINS),
            "fixed_reference_records":anchor_receipts,"source_request":copy.deepcopy(SOURCE_REQUEST),
            "accepted_index":56,"physical_state_sha256":PHYSICAL_SHA,
            "independent168_array_sha256":STATE_SHA,"accepted_cache_binding_sha256":CACHE_BINDING,
            "original_log_reads":2,"old_scientific_executions":0,
            "second_log_only_supplies_unchanged_reference_constructor_and_original_pool_history":True}
        progress.update(status="complete",accepted_index=56,receipt=source_receipt)
        ledger.check("source56.complete")
        return {"report":real,"reference_report":anchor_real,"checkpoint":cp,
            "point":point,"state168":state,"gates":gates,"accepted_cache":cache,
            "source_stage":real["actual_stage"],"receipt":source_receipt,
            "ancestor_cost_receipt":cost,"source_final_clock":clock}
    except Exception as error:
        progress.update(status="raised",error={"type":type(error).__name__,"message":str(error)})
        raise
    finally:
        progress["elapsed_source_input_seconds"]=time.monotonic()-started

def exact_physical_map(field):
    old=field.original_field.coordinates
    matrix=[[Q(0) for _ in range(168)] for _ in range(172)]
    for i in range(154): matrix[i][i]=Q(1)
    for i in range(9):
        for j in range(5): matrix[154+i][154+j]=old.basis.H[i][j]
    for j in range(9): matrix[163+j][159+j]=Q(1)
    exact=[[str(x) for x in row] for row in matrix]
    floating=np.asarray([[float(x) for x in row] for row in matrix],dtype=float)
    binding={"schema":POLICY+"-exact-affine-physical172-map",
        "coordinate_definition_sha256":field.coordinate_definition_sha256,
        "old_null_basis_definition_sha256":digest(old.basis.identity),
        "exact_matrix_sha256":digest(exact),"float_matrix_sha256":array_digest(floating),
        "shape":[172,168],"norm_definition":"4*||M172x168 delta168||_infinity",
        "physical_values_remain_exact_affine_rationals":True}
    return floating,exact,binding

def prepare(request,output,completed,ledger,*,process_started):
    require(isinstance(ledger,Joint168Ledger),"one shared joint168 ledger required")
    ledger.check("prepare.start")
    cp,real=completed["checkpoint"],completed["report"]
    args=inherited.previous.old_input_namespace(request,output)
    restored,bindings,tenth,_,_,_=baseline.growth.prepare_run(
        args,process_started=process_started)
    ledger.check("prepare.original-inputs")
    original,_,original_gate,lower,upper,historical_cfg,_=restored
    coordinate_sha=digest(cp["coordinate_definition"])
    require(coordinate_sha==paid.COORDINATE_SHA,"original permanent159 coordinate map differs")
    field_request={"source":{"coordinate_definition_sha256":coordinate_sha},
        "fixed_complete_metric_sha256":request["fixed_complete_metric_sha256"],
        "fixed_b0_definition_sha256":request["fixed_b0_definition_sha256"]}
    old_field,old_state,gate,field_receipt=inherited.reconstruct_checkpoint_field(
        original,original_gate,lower,upper,cp,field_request)
    problem=DirectReferenceFiveHeightField(old_field)
    require(np.array_equal(old_state,completed["state168"][:159]),
            "the old physical part of actual56 differs from the reference construction source")
    gate,gate_receipt=direct_audit.fresh_adapter_gate(
        gate,problem,old_state,gate.coordinate_lower,gate.coordinate_upper)
    field=CompleteBody168Field(problem)
    state=completed["state168"].copy()
    cfg=copy.deepcopy(real["configuration"])
    require(digest(field.identity(state))==PHYSICAL_SHA
        and field.coordinate_definition_sha256==COORDINATE_SHA
        and digest(field.evaluation_definition())==FIELD_SHA and digest(cfg)==CFG_SHA,
        "restored complete nonzero56 field/coordinates/g/b0/configuration changed")
    radial,theta,grid=baseline.curvature_grid(tenth)
    require(grid==real["full_value_sampling_definition"],"original full sampling definition changed")
    for name,actual in (("radial",radial),("theta",theta)):
        saved=completed["accepted_cache"]["grids"]["coarse"][name]
        require(array_digest(actual)==saved["array_sha256"]
            and np.asarray(saved["values"],dtype=float).tobytes()==actual.tobytes(),
            "the current56 coarse grid binary64 changed")
    fine_theta=np.asarray(completed["accepted_cache"]["grids"]["fine"]["theta"]["values"],dtype=float)
    grids={}
    for label,nt in (("coarse",len(theta)),("fine",len(fine_theta))):
        rg=RationalRowGrid(label,grid["radial_nodes_exact"],nt)
        require(rg.definition_sha256==cp["norm_direction_bank_context"]["original_grids"][label]
            and rg.point_count==cp["norm_direction_bank_context"]["original_point_counts"][label],
            "the original rational row-ID grid changed")
        grids[label]=rg
    stage=completed["source_stage"]
    pools={label:inherited.checked_pool(stage[label+"_pool"],grids[label].point_count,
           cfg["max_pool_rows" if label=="coarse" else "max_fine_physical_pool_rows"],label)
           for label in grids}
    lower172=np.r_[np.asarray(gate.original_lower,float),np.full(9,-.25)]
    upper172=np.r_[np.asarray(gate.original_upper,float),np.full(9,.25)]
    require(field.exact_full_box_decision(state,lower172,upper172)["exact_full_box_pass"],
            "actual56 must be in the unchanged exact physical172 box")
    matrix,exact_matrix,map_binding=exact_physical_map(field)
    bounded=problem.original_problem.base
    order=int(bounded.primitive_order)
    require(order==int(bounded.fixed_primitive.order)==8,"original primitive order changed")
    require(problem.timing_snapshot()["geometry_calls_started"]==0,
            "input construction must not evaluate original geometry")
    source_binding={"source":copy.deepcopy(PINS),"accepted_index":56,
        "physical_state_sha256":PHYSICAL_SHA,"independent168_array_sha256":STATE_SHA,
        "coordinate_definition_sha256":COORDINATE_SHA,
        "source_original_cfg_sha256":CFG_SHA,"source_original_field_sha256":FIELD_SHA,
        "source_original_objective_sha256":OBJECTIVE_SHA}
    replay={"source_checkpoint":{key:copy.deepcopy(stage[key]) for key in (
            "coarse_pool","fine_pool","coarse_pool_version","fine_pool_version")},
        "source_current_point":copy.deepcopy(completed["point"]),
        "source_final_gate_receipts":copy.deepcopy(completed["gates"]),
        "source_paid_receipt":copy.deepcopy(completed["receipt"]),
        "ancestor_cost_receipt":copy.deepcopy(completed["ancestor_cost_receipt"]),
        "source_input_restoration":{"all24_original_inputs_loaded_once":True,
            "field_transfer":field_receipt,"fresh_adapter_gate":gate_receipt,
            "historical24_configuration_sha256":digest(historical_cfg),
            "current56_nonzero_new9_and_exact172_restored":True,
            "ordinary_or_derivative_or_old_optimizer_calls":0,
            "original_primitive_order":order,"source_configuration_unchanged":True,
            "closed_ancestor_scientific_seconds":ANCESTOR_SECONDS,
            "closed_ancestor_ordinary_values":ANCESTOR_VALUES}}
    ledger.check("prepare.complete")
    return {"accepted_cache":completed["accepted_cache"],"source_binding":source_binding,
        "problem":problem,"field168":field,"center168":state,"q168":state,"initial168":state,
        "initial159":old_state,"initial":old_state,"gate":gate,"cfg":cfg,
        "radial":radial,"theta":theta,"fine_theta":fine_theta,"grid":grid,"row_grids":grids,
        "order":order,"lower":gate.coordinate_lower,"upper":gate.coordinate_upper,
        "lower172":lower172,"upper172":upper172,
        "physical_map172x168":matrix,"physical_map_exact172x168":exact_matrix,
        "physical_map_binding":map_binding,"coarse_pool":pools["coarse"],"fine_pool":pools["fine"],
        "bindings":bindings,"replay":replay,"seed_metric_tags":[]}
