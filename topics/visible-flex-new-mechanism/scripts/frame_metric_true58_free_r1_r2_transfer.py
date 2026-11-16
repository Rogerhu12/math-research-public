#!/usr/bin/env python3
"""Restore actual58 and its fixed-reference source; import-only, no science replay.

The current58 log supplies current168, original gates, selected pools, and
paid U/T/e/f.  A second original55 COMPLETE supplies the unchanged permanent
reference/height-map constructor data omitted from58's small checkpoint.
A third original ring17 log supplies its paid circle twojets and closed ledger.
A fourth reflected-R1 stdout supplies paid scalar/frame/V17/primitive17 fields.
A fifth completed joint-alpha/R2 stdout supplies only the latest closed ledger.
Neither old geometry nor any old J/model/optimizer is called.
The source research succeeded; its report-only size stop is not a scientific failure.
Current58 old159 coordinates come from58, not from the55 constructor point.
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
from frame_complete_body_extension168 import CompleteBody168Field, array_binding
import frame_metric_paid_cone_vector_audit as paid
import frame_metric_direct_reference_audit as direct_audit
import frame_metric_curvature_defect_guard_transfer as inherited
import frame_metric_height159_complete_affine_audit as baseline
from frame_metric_true58_free_r1_r2_scope import POLICY, Free58Ledger, require

REPO="Rogerhu12/math-research-public"
PINS={"run_id":"43859882465","job_id":"133273598120",
      "source_commit":"0e6fafbf7bce37cd851dfc972b2de1ff3d0d5881",
      "workflow":".github/workflows/visible-true57-nonlinear168.yml",
      "log_bytes":86358161,
      "log_sha256":"346de3d6027e21e3b3d9dc020b0890c14d65e6dc588c2178ee63eff9f12fca3e"}
RECORDS=[
 {"tag":"COMPLETE","ordinal":1,"JSON_plus_LF_bytes":5606777,
  "JSON_plus_LF_sha256":"e20a2149a50ea86becc177724235b6991d597d541c583fad85df3d1d3a739604"},
 {"tag":"CACHE","ordinal":2,"JSON_plus_LF_bytes":33375405,
  "JSON_plus_LF_sha256":"9bfdb6d35b131d5b4b1514f0e0902c7f38aa735cabc3288502356b1ba03ffbdf"},
 {"tag":"FINAL_CLOCK","ordinal":1,"JSON_plus_LF_bytes":199299,
  "JSON_plus_LF_sha256":"6a8e4724000f16429ed6c72607a92611647159207a18ce8e6a218b97269113de"}]
SOURCE_REQUEST={"path":"topics/visible-flex-new-mechanism/computations/request-true57-nonlinear168.json",
                "bytes":63362,
                "sha256":"543ca3ccccac55e918e3f4c2dd5a08ff3ff853cebbe873367346ae0a175b6c44"}
ANCHOR_PINS={"run_id":"43832870561","job_id":"133182173190",
 "source_commit":"23b37e90cbc1ac33ca6ff8ac1f91fa7a95c903db",
 "workflow":".github/workflows/visible-true54-fresh-model.yml",
 "log_bytes":81300477,
 "log_sha256":"36bfb2269d5a85c52116066e521c9ffdce4f9c99dc35866a11d31e0830928ce2"}
ANCHOR_RECORD={"tag":"COMPLETE","ordinal":1,"JSON_plus_LF_bytes":5388242,
 "JSON_plus_LF_sha256":"a7819f1e04a97c5003e4058fb3c1df17a9841c5b6006790875a98cee27622b4b"}
PHYSICAL_SHA="94950b2bd5d7b5241e14333a4315b073f64840f74849a7909d6de8cb3cc29f54"
STATE_SHA="e2d52f849596a5e7bbf596b66d7805587acc944c1549c5648ee4e115548ed2bf"
COORDINATE_SHA="c69967fb9b864f3e95da411610b74d5477c58891352895b493aee6e482d960de"
CFG_SHA="1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19"
FIELD_SHA="81e6881cd1f36d87a865cd9cc8c51ee8480d2ac8278241d97fb19666486eba8d"
OBJECTIVE_SHA="bbdc448df8f7be0d9f1b506aa7a538c56bc335b69f682bf1cdd6d8ec4978f49d"
CACHE_BINDING="28969794748d9b02fee16b90c775d9b41abba4facdfae0781d95f61e5b9040a1"
ANCESTOR_SECONDS=2830.778901609
ANCESTOR_VALUES=147
SOURCE_STATUS="complete-true57-nonlinear168-original-actual-observation"
GRID_SHAPES={"coarse":(160,384),"fine":(160,768)}

RING_PINS={"run_id":"43865295208","job_id":"133292183126",
 "source_commit":"35438c143eda961a0fa8836d387d0e537fba43b2",
 "workflow":".github/workflows/visible-true58-ring17.yml",
 "log_bytes":1949314,
 "log_sha256":"6b893404c4515ae7bc86252efd79c3f920294242e6f51620b49c5d9c55fbda9a"}
RING_RECORDS=[
 {"tag":"MODEL","ordinal":1,"JSON_plus_LF_bytes":1449765,
  "JSON_plus_LF_sha256":"b56010f023cae1ba6ce63ce33d6fe3728ce72ec096600f466dd377c216aa9fcc"},
 {"tag":"COMPLETE","ordinal":1,"JSON_plus_LF_bytes":157768,
  "JSON_plus_LF_sha256":"7ba6d8e28b0b7ee06d00dd812e7ba614248b7c17e3428ba0f044b70f39765811"},
 {"tag":"FINAL_CLOCK","ordinal":1,"JSON_plus_LF_bytes":4707,
  "JSON_plus_LF_sha256":"1e295d6888a275b4107bc4638d3e940a9efb670be53ecd1e9654c7d2bfce4d4c"}]
RING_REQUEST={"path":"topics/visible-flex-new-mechanism/computations/request-true58-ring17.json",
 "bytes":63988,"sha256":"7826e3b1968cb15f5815d3ac5080869dea7e085d37925141c146af8c045159ab"}
RING_BINDING="a442604e4155a0100e9a203ad94369b38e7968eff365786d5d5627091d190780"
CLOSED_RING_SECONDS=2863.061635735

REFLECTION_PINS={"run_id":"43873254906","job_id":"133319615177",
 "source_commit":"0b8bb24ce9d4a9acb3219c6fe01f35328aba4139",
 "workflow":".github/workflows/visible-true58-reflected-r1.yml",
 "log_bytes":14802012,
 "log_sha256":"b4b8dee48b31995ff27e38d6a4b9bf4c8bb8b8664c5d7f3008956f3dcf47657b"}
REFLECTION_RECORDS=[
 {"tag":"MODEL","ordinal":1,"JSON_plus_LF_bytes":13312899,
  "JSON_plus_LF_sha256":"ca0aec1d95949c467042eb74b94314a4490d6742e5cf76f040eeba060d1b8f3e"},
 {"tag":"COMPLETE","ordinal":1,"JSON_plus_LF_bytes":894576,
  "JSON_plus_LF_sha256":"b87003cdd8566ae41971e3e453f5d69ff0ba41372ef576be50f1f3507d6f9596"},
 {"tag":"FINAL_CLOCK","ordinal":1,"JSON_plus_LF_bytes":7141,
  "JSON_plus_LF_sha256":"c111c84c9116fac9bfab48553466a6bb3a69696fd02a7621cc4827bebc59d9dc"}]
REFLECTION_REQUEST={"path":"topics/visible-flex-new-mechanism/computations/request-true58-reflected-r1.json",
 "bytes":66246,"sha256":"70f7e91d7ecacb1fa24f0834728e2df638412ff1e53b1ccc020ceb027f0fa046"}
CLOSED_REFLECTION_SECONDS=2882.412483226

JOINT_PINS={"run_id":"43880150928","job_id":"133343574077",
 "source_commit":"25c98ff4198cfc10552ddcd0dc9307110a6be8de",
 "workflow":".github/workflows/visible-true58-joint-alpha-r2.yml",
 "log_bytes":6343887,
 "log_sha256":"06dbe91e2fd93053904e27784be35e4856a137bf4d800f8713fbad3f2334541d"}
JOINT_RECORDS=[
 {"tag":"COMPLETE","ordinal":1,"JSON_plus_LF_bytes":182315,
  "JSON_plus_LF_sha256":"293424d38ad60946773491574af45e6bfdc6f4b17d49344fb1442eb231811203"},
 {"tag":"FINAL_CLOCK","ordinal":1,"JSON_plus_LF_bytes":4998,
  "JSON_plus_LF_sha256":"76b7397f0ae2f845dce969c75f1e32f511257b3a895dd299e273b35a0afa3dac"}]
JOINT_REQUEST={"path":"topics/visible-flex-new-mechanism/computations/request-true58-joint-alpha-r2.json",
 "bytes":71258,"sha256":"383d0d45ecd6c617385eae3a4979856db997beb2b1c76029b7e98b7702c037d3"}
CLOSED_JOINT_SECONDS=2902.366570826


def exact_binary64(values,length):
    require(isinstance(values,list) and len(values)==length
            and all(isinstance(v,str) for v in values),"complete exact binary64 vector required")
    qs=[Q(v) for v in values]
    a=np.asarray([float(v) for v in qs],dtype=np.float64)
    require(np.all(np.isfinite(a)) and all(
        Q.from_float(float(v))==q for v,q in zip(a,qs)),"source binary64 reconstruction differs")
    return a

def _pinned_job_log(api,pins):
    """One original source body; its already observed exact size is the cap."""
    cap=int(pins["log_bytes"])
    url=reader.API+"/repos/"+REPO+"/actions/jobs/"+pins["job_id"]+"/logs"
    raw,location=api.get(url,cap,api_auth=True)
    redirects=0
    while location is not None:
        redirects+=1
        require(redirects<=4,"too many original log redirects")
        raw,location=api.get(location,cap,api_auth=False)
    require(raw is not None,"empty original log response")
    return raw,redirects

def _read_records(api,pins,prefix,expected,ledger,progress):
    ledger.check("source.metadata")
    run=api.api_json("/actions/runs/"+pins["run_id"])
    job=api.api_json("/actions/jobs/"+pins["job_id"])
    require(str(run["id"])==str(job["run_id"])==pins["run_id"]
        and str(job["id"])==pins["job_id"]
        and run["head_sha"]==job["head_sha"]==pins["source_commit"]
        and run["status"]==job["status"]=="completed"
        and job["conclusion"]=="success"
        and run["conclusion"] in ("success","failure")
        and run["path"]==pins["workflow"],"completed original source identity differs")
    progress["original_logs_requested"]+=1
    raw,redirects=_pinned_job_log(api,pins)
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
    require(isinstance(ledger,Free58Ledger),"one new free58 account required")
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
            "current58 and its fixed-reference sources must be literal")
        raw_request=Path(SOURCE_REQUEST["path"]).read_bytes()
        require(len(raw_request)==SOURCE_REQUEST["bytes"]
            and reader.digest(raw_request)==SOURCE_REQUEST["sha256"],
            "the complete source58 request differs")
        old_request=reader.decode_json(raw_request)
        require(request["original_input_arguments"]==old_request["original_input_arguments"]
            and len(request["original_input_arguments"])==98
            and request["fixed_complete_metric_sha256"]==old_request["fixed_complete_metric_sha256"]
            and request["fixed_b0_definition_sha256"]==old_request["fixed_b0_definition_sha256"],
            "all24 original inputs and g/b0 must remain")
        api=reader.GitHubReader(REPO)
        rec,receipts=_read_records(api,PINS,"TRUE57_NONLINEAR168_",RECORDS,ledger,progress)
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
            "original actual58 outcome/source differs")
        final=clock["ledger"]
        require(final["total_ancestor_plus_new_scientific_seconds"]==ANCESTOR_SECONDS
            and final["total_source_plus_new_started_values"]==ANCESTOR_VALUES
            and final["scientific_seconds"]==185.978494641
            and final["started_counts"]["actual_trial_pairs"]==1
            and final["started_counts"]["actual_grid_values"]==2,
            "the closed source58 final account differs")
        point=real["selected_two_grid_physical_point"]
        require(point==real["actual_stage"]["selected_two_grid_physical_point"]
            and point["accepted_index"]==58 and point["physical_state_sha256"]==PHYSICAL_SHA
            and point["coordinate_definition_sha256"]==COORDINATE_SHA
            and point["complete_new_field_evaluation_sha256"]==FIELD_SHA
            and point["objective_evaluation_sha256"]==OBJECTIVE_SHA
            and digest(real["configuration"])==CFG_SHA,
            "current complete168 physical/evaluation identity differs")
        state=exact_binary64(point["exact_binary64_independent168_coordinates"],168)
        require(array_digest(state)==STATE_SHA
            and np.asarray(point["independent_coordinates_binary64"],dtype=float).tobytes()==state.tobytes()
            and np.any(state[159:]!=0.),"actual58 has all168 coordinates and nonzero new9")
        gates={}
        for label in GRID_SHAPES:
            d=point[label]
            require(len(d["actual_gate_booleans"])==14
                and all(v is True for v in d["actual_gate_booleans"].values())
                and d["exact_full172_physical_box_pass"] is True,
                "all original actual58 fourteen gates and exact172 box required")
            gates[label]=copy.deepcopy(d)
        trials=[x for x in real["actual_stage"]["trials"] if x.get("accepted_as_next_iterate")]
        require(len(trials)==1 and trials[0]["accepted_index"]==58
            and trials[0]["physical_state_sha256"]==PHYSICAL_SHA
            and trials[0]["state"]["independent168_exact"]==
                point["exact_binary64_independent168_coordinates"],
            "one original accepted58 actual trial must match")
        require(cache["kind"]=="accepted-point-paid-geometry"
            and cache["available"] is True and cache["status"]=="complete"
            and cache["binding_sha256"]==CACHE_BINDING and digest(cache["binding"])==CACHE_BINDING,
            "the current58 CACHE2 identity differs")
        require(cache["first_jet_cache_complete"] is True
            and cache["selected_export_complete"] is True
            and real["accepted_selected_two_jet_export"]["selected_export_complete"] is True,
            "source58 saved first jets and selected exports must remain literal")
        binding=cache["binding"]
        for key,value in {"accepted_index":58,"physical_state_sha256":PHYSICAL_SHA,
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
            and receipt["binding_sha256"]==CACHE_BINDING and receipt["accepted_index"]==58,
            "COMPLETE must point to this exact accepted58 CACHE2")
        # Only the original55 COMPLETE is decoded: it carries permanent reference
        # constructor data absent from the58 checkpoint, not a current derivative.
        anchor_records,anchor_receipts=_read_records(
            api,ANCHOR_PINS,"TRUE54_FRESH_",[ANCHOR_RECORD],ledger,progress)
        anchor_real=anchor_records[("COMPLETE",1)]
        cp=anchor_real["future_fresh54_checkpoint"]
        require(real["future_source_restoration"]["fixed_reference_source"]==ANCHOR_PINS
            and real["future_source_restoration"]["fixed_reference_record"]==ANCHOR_RECORD
            and cp["selected_two_grid_physical_point"]==anchor_real["selected_two_grid_physical_point"]
            and cp["configuration"]==real["configuration"]
            and cp["selected_accepted_index"]==55,
            "the original55 source supplies only the unchanged permanent constructor")
        require(real["fixed_complete_metric_sha256"]==request["fixed_complete_metric_sha256"]
            and real["fixed_b0_definition_sha256"]==request["fixed_b0_definition_sha256"],
            "the current point retained the original fixed g and b0")
        require((len(real["actual_stage"]["coarse_pool"]),len(real["actual_stage"]["fine_pool"]),
            real["actual_stage"]["coarse_pool_version"],real["actual_stage"]["fine_pool_version"])
            ==(4454,4549,15,14),"current58 complete selected pools differ")
        # Read the last closed task exactly once.  Its saved whole-circle
        # arrays are input; its failed R2 solver and coefficient builder are not called.
        require(request["paid_ring_source"]==RING_PINS
            and request["paid_ring_records"]==RING_RECORDS
            and request["paid_ring_request"]==RING_REQUEST,
            "literal paid ring source and closed account required")
        ring_request_bytes=Path(RING_REQUEST["path"]).read_bytes()
        require(len(ring_request_bytes)==RING_REQUEST["bytes"]
            and reader.digest(ring_request_bytes)==RING_REQUEST["sha256"],
            "the original closed ring request differs")
        ring_request=reader.decode_json(ring_request_bytes)
        ring_records,ring_receipts=_read_records(
            api,RING_PINS,"TRUE58_RING17_",RING_RECORDS,ledger,progress)
        ring_model=ring_records[("MODEL",1)]
        ring_real=ring_records[("COMPLETE",1)]
        ring_clock=ring_records[("FINAL_CLOCK",1)]
        require(ring_real["status"]==ring_clock["status_at_final_emit"]==
                    "complete-true58-ring17-observation"
            and not ring_clock["scope_exhausted"]
            and ring_clock["sampled_after_all_large_cache_and_complete_write_and_flush"] is True
            and ring_real["github_sha"]==RING_PINS["source_commit"]
            and str(ring_real["github_run_id"])==RING_PINS["run_id"]
            and ring_real["github_repository"]==REPO
            and ring_real["new_acceptances"]==0
            and ring_real["selected_two_grid_physical_point"]==point
            and ring_real["old_checks_executed"]==ring_real["new_development_executed"]==0
            and ring_real["source_files_sha256"]==ring_request["source_sha256"],
            "the closed ring task must still name the same actual58")
        ring_final=ring_clock["ledger"]
        require(ring_final["total_ancestor_plus_new_scientific_seconds"]==CLOSED_RING_SECONDS
            and ring_final["total_source_plus_new_started_values"]==ANCESTOR_VALUES
            and ring_final["scientific_seconds"]==32.28273412599998
            and ring_final["started_counts"]["finite_ring_LP_calls"]==1
            and ring_final["started_counts"]["nonlinear_candidate_predictions"]==0
            and ring_final["started_counts"]["actual_trial_pairs"]==0
            and ring_final["started_counts"]["actual_grid_values"]==0,
            "the entire last closed science account is retained")
        require(ring_model["binding_sha256"]==RING_BINDING
            and digest(ring_model["binding"])==RING_BINDING
            and ring_model["binding"]["source"]["physical_state_sha256"]==PHYSICAL_SHA
            and np.asarray(ring_model["state168"]["values"],dtype=float).tobytes()==state.tobytes()
            and ring_real["model_stdout_receipt"]["JSON_plus_LF_bytes"]==RING_RECORDS[0]["JSON_plus_LF_bytes"]
            and ring_real["model_stdout_receipt"]["JSON_plus_LF_sha256"]==RING_RECORDS[0]["JSON_plus_LF_sha256"],
            "paid complete ring must bind the same current point and original MODEL1")
        # The fourth completed stdout supplies the already paid ray/V17/Lx/Hxx.
        # Decode its saved arrays; do not call the closed projection or ring LP.
        require(request["paid_reflection_source"]==REFLECTION_PINS
            and request["paid_reflection_records"]==REFLECTION_RECORDS
            and request["paid_reflection_request"]==REFLECTION_REQUEST,
            "literal paid reflection ray and last closed account required")
        reflection_request_bytes=Path(REFLECTION_REQUEST["path"]).read_bytes()
        require(len(reflection_request_bytes)==REFLECTION_REQUEST["bytes"]
            and reader.digest(reflection_request_bytes)==REFLECTION_REQUEST["sha256"],
            "the original closed reflection request differs")
        reflection_request=reader.decode_json(reflection_request_bytes)
        reflected_records,reflected_receipts=_read_records(
            api,REFLECTION_PINS,"TRUE58_REFLECTED_R1_",REFLECTION_RECORDS,ledger,progress)
        reflected_model=reflected_records[("MODEL",1)]
        reflected_real=reflected_records[("COMPLETE",1)]
        reflected_clock=reflected_records[("FINAL_CLOCK",1)]
        require(reflected_real["status"]==reflected_clock["status_at_final_emit"]==
                    "complete-true58-reflected-r1-observation"
            and not reflected_clock["scope_exhausted"]
            and reflected_clock["sampled_after_all_large_cache_and_complete_write_and_flush"] is True
            and reflected_real["github_sha"]==REFLECTION_PINS["source_commit"]
            and str(reflected_real["github_run_id"])==REFLECTION_PINS["run_id"]
            and reflected_real["github_repository"]==REPO
            and reflected_real["new_acceptances"]==0
            and reflected_real["selected_two_grid_physical_point"]==point
            and reflected_real["old_checks_executed"]==reflected_real["new_development_executed"]==0
            and reflected_real["source_files_sha256"]==reflection_request["source_sha256"],
            "the closed reflected R1 task must still name the same actual58")
        reflected_final=reflected_clock["ledger"]
        require(reflected_final["total_ancestor_plus_new_scientific_seconds"]==CLOSED_REFLECTION_SECONDS
            and reflected_final["total_source_plus_new_started_values"]==ANCESTOR_VALUES
            and reflected_final["scientific_seconds"]==19.350847490999968
            and reflected_final["started_counts"]["finite_bounded_R1_least_squares"]==1
            and reflected_final["started_counts"]["finite_ring_LP_calls"]==1
            and reflected_final["started_counts"]["nonlinear_candidate_predictions"]==0
            and reflected_final["started_counts"]["actual_trial_pairs"]==0
            and reflected_final["started_counts"]["actual_grid_values"]==0,
            "the entire closed reflection science account is retained")
        require(reflected_model["source"]["physical_state_sha256"]==PHYSICAL_SHA
            and reflected_model["source"]["paid_ring_model_binding_sha256"]==RING_BINDING
            and reflected_real["model_stdout_receipt"]["JSON_plus_LF_bytes"]==REFLECTION_RECORDS[0]["JSON_plus_LF_bytes"]
            and reflected_real["model_stdout_receipt"]["JSON_plus_LF_sha256"]==REFLECTION_RECORDS[0]["JSON_plus_LF_sha256"],
            "saved full reflection MODEL1 must bind this original58 and paid ring")
        # The fifth stdout is the latest closed task, never a retry or free
        # replacement for its failed local solve.  Only COMPLETE/FINAL are read.
        require(request["paid_joint_source"]==JOINT_PINS
            and request["paid_joint_records"]==JOINT_RECORDS
            and request["paid_joint_request"]==JOINT_REQUEST,
            "literal last closed joint-alpha/R2 account required")
        joint_request_bytes=Path(JOINT_REQUEST["path"]).read_bytes()
        require(len(joint_request_bytes)==JOINT_REQUEST["bytes"]
            and reader.digest(joint_request_bytes)==JOINT_REQUEST["sha256"],
            "the original closed joint-alpha/R2 request differs")
        joint_request=reader.decode_json(joint_request_bytes)
        joint_records,joint_receipts=_read_records(
            api,JOINT_PINS,"TRUE58_JOINT_ALPHA_R2_",JOINT_RECORDS,ledger,progress)
        joint_real=joint_records[("COMPLETE",1)]
        joint_clock=joint_records[("FINAL_CLOCK",1)]
        require(joint_real["status"]==joint_clock["status_at_final_emit"]==
                    "complete-true58-joint-alpha-r2-observation"
            and not joint_clock["scope_exhausted"]
            and joint_clock["sampled_after_all_large_cache_and_complete_write_and_flush"] is True
            and joint_real["github_sha"]==JOINT_PINS["source_commit"]
            and str(joint_real["github_run_id"])==JOINT_PINS["run_id"]
            and joint_real["github_repository"]==REPO
            and joint_real["new_acceptances"]==0
            and joint_real["selected_two_grid_physical_point"]==point
            and joint_real["old_checks_executed"]==joint_real["new_development_executed"]==0
            and joint_real["source_files_sha256"]==joint_request["source_sha256"],
            "the latest closed joint task must still name the same actual58")
        joint_final=joint_clock["ledger"]
        require(joint_final["total_ancestor_plus_new_scientific_seconds"]==CLOSED_JOINT_SECONDS
            and joint_final["total_source_plus_new_started_values"]==ANCESTOR_VALUES
            and joint_final["scientific_seconds"]==19.9540876
            and joint_final["started_counts"]["joint_alpha_R2_model_builds"]==1
            and joint_final["started_counts"]["joint_alpha_R2_solver_sessions"]==1
            and joint_final["started_counts"]["nonlinear_candidate_predictions"]==0
            and joint_final["started_counts"]["actual_trial_pairs"]==0
            and joint_final["started_counts"]["actual_grid_values"]==0,
            "the complete latest failed solve and final science account are retained")
        cost={"ancestor_final_original_scientific_seconds":CLOSED_JOINT_SECONDS,
            "source_global_scientific_seconds":CLOSED_JOINT_SECONDS,
            "source_original_full_values":ANCESTOR_VALUES,"source_original_values":ANCESTOR_VALUES,
            "source58_final_clock":copy.deepcopy(clock),
            "source_final_clock":copy.deepcopy(joint_clock),
            "source_reflection_final_clock":copy.deepcopy(reflected_clock),
            "source_ring_final_clock":copy.deepcopy(ring_clock),
            "closed_joint_alpha_R2_task_not_reopened":True,
            "closed_original_reflected_R1_task_not_reopened":True,
            "closed_original_ring17_task_not_reopened":True,
            "closed_source57_nonlinear168_task_not_reopened":True,
            "earlier_checkpoint_samples_not_added_to_final_clock":True}
        source_receipt={"schema":POLICY+"-actual58-source","passed":True,
            "source":copy.deepcopy(PINS),"source_records":receipts,
            "fixed_reference_source":copy.deepcopy(ANCHOR_PINS),
            "fixed_reference_records":anchor_receipts,"source_request":copy.deepcopy(SOURCE_REQUEST),
            "accepted_index":58,"physical_state_sha256":PHYSICAL_SHA,
            "independent168_array_sha256":STATE_SHA,"accepted_cache_binding_sha256":CACHE_BINDING,
            "original_log_reads":5,"old_scientific_executions":0,
            "paid_joint_source":copy.deepcopy(JOINT_PINS),
            "paid_joint_records":joint_receipts,
            "last_closed_joint_scientific_seconds":CLOSED_JOINT_SECONDS,
            "paid_reflection_source":copy.deepcopy(REFLECTION_PINS),
            "paid_reflection_records":reflected_receipts,
            "last_closed_reflection_scientific_seconds":CLOSED_REFLECTION_SECONDS,
            "paid_ring_source":copy.deepcopy(RING_PINS),"paid_ring_records":ring_receipts,
            "paid_ring_model_binding_sha256":RING_BINDING,
            "last_closed_ring_scientific_seconds":CLOSED_RING_SECONDS,
            "second_log_only_supplies_unchanged_reference_constructor_and_original_pool_history":True}
        source_receipt["paid_ring_metric"]=paid_ring_metric_from_current_cache(cache)
        progress.update(status="complete",accepted_index=58,receipt=source_receipt)
        ledger.check("source58.complete")
        return {"report":real,"reference_report":anchor_real,"checkpoint":cp,
            "point":point,"state168":state,"gates":gates,"accepted_cache":cache,
            "source_stage":real["actual_stage"],"receipt":source_receipt,
            "ancestor_cost_receipt":cost,"source_final_clock":clock,
            "latest_closed_scientific_clock":joint_clock,"paid_ring_model":ring_model,
            "paid_reflected_model":reflected_model,"paid_reflected_complete":reflected_real,
            "paid_ring_complete":ring_real}
    except Exception as error:
        progress.update(status="raised",error={"type":type(error).__name__,"message":str(error)})
        raise
    finally:
        progress["elapsed_source_input_seconds"]=time.monotonic()-started


def paid_ring_metric_from_current_cache(cache):
    """Read saved fixed-g a and a_s; no metric or geometry evaluator is called."""
    candidates=[]
    for label in ("coarse","fine"):
        payload=cache["selected_current168_geometry"][label]
        identity=payload["identity"]
        require(digest(identity)==payload["binding_sha256"]==
            cache["binding"]["selected_current168_geometry"][label]["binding_sha256"],
            "literal actual58 selected payload binding required")
        arrays=payload["arrays"]
        ids_rec,a_rec,as_rec=(arrays[name] for name in ("metric_radial_ids","metric_a","metric_a_s"))
        ids=np.asarray(ids_rec["values"],dtype=np.dtype(ids_rec["dtype"]))
        av=np.asarray(a_rec["values"],dtype=np.dtype(a_rec["dtype"]))
        asv=np.asarray(as_rec["values"],dtype=np.dtype(as_rec["dtype"]))
        require(ids.dtype.kind in "iu" and av.dtype==asv.dtype==np.dtype("float64")
            and ids.ndim==av.ndim==asv.ndim==1 and len(ids)==len(av)==len(asv),
            "paid radial IDs and fixed-g a/a_s shape/type differ")
        for name,rec,arr in (("metric_radial_ids",ids_rec,ids),("metric_a",a_rec,av),("metric_a_s",as_rec,asv)):
            metadata=array_binding(arr)
            require(metadata==identity["arrays"][name]
                and all(rec.get(k)==v for k,v in metadata.items()),
                "literal paid metric payload identity differs: "+label+"/"+name)
        hits=[i for i,value in enumerate(ids.tolist()) if value==141]
        require(len(hits)<=1,"paid selected radial IDs must be unique")
        if hits:
            index=hits[0];value=float(av[index]);slope=float(asv[index])
            require(np.isfinite(value) and value>0. and np.isfinite(slope),
                    "saved original fixed-g a must be positive and a_s finite")
            candidates.append({"a_binary64":value,"a_exact_binary64":str(Q.from_float(value)),
                "a_s_binary64":slope,"a_s_exact_binary64":str(Q.from_float(slope)),
                "source":{"source":copy.deepcopy(PINS),
                    "source_record":copy.deepcopy(next(x for x in RECORDS if x["tag"]=="CACHE")),
                    "accepted_cache_binding_sha256":CACHE_BINDING,"grid":label,
                    "selected_ordinary_binding_sha256":payload["binding_sha256"],
                    "metric_radial_ids":copy.deepcopy(identity["arrays"]["metric_radial_ids"]),
                    "metric_a":copy.deepcopy(identity["arrays"]["metric_a"]),
                    "metric_a_s":copy.deepcopy(identity["arrays"]["metric_a_s"]),
                    "original_radial_index":141,"index_in_saved_selected_metric":index,
                    "new_metric_or_geometry_evaluations":0}})
    require(candidates,"neither paid actual58 selected metric payload contains original ring141")
    require(all((row["a_exact_binary64"],row["a_s_exact_binary64"])==
                (candidates[0]["a_exact_binary64"],candidates[0]["a_s_exact_binary64"])
                for row in candidates), "two saved fixed-g a/a_s values differ")
    answer=copy.deepcopy(candidates[0])
    answer["all_available_original_sources"]=[row["source"] for row in candidates]
    return answer

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
    require(isinstance(ledger,Free58Ledger),"one shared free58 ledger required")
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
    anchor_state = old_state.copy()
    old_state = completed["state168"][:159].copy()
    require(problem.coordinates.physical_exact(old_state)==tuple(
            Q(v) for v in completed["point"]["exact_physical172_coefficients"][:163]),
            "the current original159 physical part differs from the literal current172 point")
    gate,gate_receipt=direct_audit.fresh_adapter_gate(
        gate,problem,old_state,gate.coordinate_lower,gate.coordinate_upper)
    field=CompleteBody168Field(problem)
    state=completed["state168"].copy()
    cfg=copy.deepcopy(real["configuration"])
    require(digest(field.identity(state))==PHYSICAL_SHA
        and field.coordinate_definition_sha256==COORDINATE_SHA
        and digest(field.evaluation_definition())==FIELD_SHA and digest(cfg)==CFG_SHA,
        "restored complete nonzero58 field/coordinates/g/b0/configuration changed")
    radial,theta,grid=baseline.curvature_grid(tenth)
    require(grid==real["full_value_sampling_definition"],"original full sampling definition changed")
    for name,actual in (("radial",radial),("theta",theta)):
        saved=completed["accepted_cache"]["grids"]["coarse"][name]
        require(array_digest(actual)==saved["array_sha256"]
            and np.asarray(saved["values"],dtype=float).tobytes()==actual.tobytes(),
            "the current58 coarse grid binary64 changed")
    fine_theta=np.asarray(completed["accepted_cache"]["grids"]["fine"]["theta"]["values"],dtype=float)
    grids={}
    for label,nt in (("coarse",len(theta)),("fine",len(fine_theta))):
        rg=RationalRowGrid(label,grid["radial_nodes_exact"],nt)
        require(rg.definition_sha256==cp["norm_direction_bank_context"]["original_grids"][label]
            and rg.point_count==cp["norm_direction_bank_context"]["original_point_counts"][label],
            "the original rational row-ID grid changed")
        grids[label]=rg
    stage=completed["source_stage"]
    pools={}
    for label in grids:
        ids=stage[label+"_pool"]
        capacity=int(cfg["max_pool_rows" if label=="coarse" else "max_fine_physical_pool_rows"])
        require(isinstance(ids,list) and all(type(value) is int for value in ids)
            and len(ids)==len(set(ids)) and len(ids)<=capacity
            and all(0<=value<11*grids[label].point_count for value in ids),
            "the literal current pool must be unique/in-range/within original capacity")
        pools[label]=list(ids)  # Actual learning appends IDs; preserve its original order.
    lower172=np.r_[np.asarray(gate.original_lower,float),np.full(9,-.25)]
    upper172=np.r_[np.asarray(gate.original_upper,float),np.full(9,.25)]
    require(field.exact_full_box_decision(state,lower172,upper172)["exact_full_box_pass"],
            "actual58 must be in the unchanged exact physical172 box")
    matrix,exact_matrix,map_binding=exact_physical_map(field)
    bounded=problem.original_problem.base
    order=int(bounded.primitive_order)
    require(order==int(bounded.fixed_primitive.order)==8,"original primitive order changed")
    require(problem.timing_snapshot()["geometry_calls_started"]==0,
            "input construction must not evaluate original geometry")
    source_binding={"source":copy.deepcopy(PINS),"accepted_index":58,
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
            "current58_nonzero_new9_and_exact172_restored":True,
            "ordinary_or_derivative_or_old_optimizer_calls":0,
            "anchor55_state_is_constructor_provenance_not_current58":True,
            "anchor55_independent159_array_sha256":array_digest(anchor_state),
            "original_primitive_order":order,"source_configuration_unchanged":True,
            "closed_ancestor_scientific_seconds":CLOSED_JOINT_SECONDS,
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
        "bindings":bindings,"replay":replay}

