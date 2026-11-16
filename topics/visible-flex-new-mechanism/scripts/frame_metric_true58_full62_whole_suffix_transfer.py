#!/usr/bin/env python3
"""Restore actual58 and the literal paid free36/prefix102 inputs.

Five original public Actions bodies are read, never old optimizers. The free36
MODEL supplies its exact coordinate embedding and RING_SOLUTION its original
backend variables. Prefix102 MODEL supplies the actual q_R scalar fields and
complete paid suffix arrays; no absent whole-grid derived array is invented.
The fifth input is only the closed full51 final account. Its declared compact
records are available, but large scientific arrays have bindings only and are
not reused. The older whole34 missing-array boundary remains. No callback is a
returned candidate. Every ancestor final clock remains.
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
from frame_metric_true58_full62_whole_suffix_scope import POLICY, Suffix58Ledger, require

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

FREE_PINS={
  "run_id": "43884276617",
  "job_id": "133358065602",
  "source_commit": "7ac3c637ec9fb7d151e7b0f7f2ee314dd137533c",
  "workflow": ".github/workflows/visible-true58-free-r1-r2.yml",
  "log_bytes": 38467120,
  "log_sha256": "64d1bd45673f9de4b533008b812acc4300024f34a976edeeb1886fd896076a80"
}
FREE_RECORDS=[
 {"tag":"MODEL","ordinal":1,"JSON_plus_LF_bytes":25755139,"JSON_plus_LF_sha256":"89cc1b6ed0eedaaf18d454206f98831fb3decb8d401212493420bf80deb9ad31"},
  {
    "tag": "RING_SOLUTION",
    "ordinal": 1,
    "JSON_plus_LF_bytes": 148788,
    "JSON_plus_LF_sha256": "752025d1ef9dd9adb557aa7bf0f1c3899fb8a4cd417d00233289c0ff066ab3ae"
  },
  {
    "tag": "COMPLETE",
    "ordinal": 1,
    "JSON_plus_LF_bytes": 344760,
    "JSON_plus_LF_sha256": "396b50f3bfda35ec5131a3fdff61592a4c1dd27d2f69625da2e377965042f381"
  },
  {
    "tag": "FINAL_CLOCK",
    "ordinal": 1,
    "JSON_plus_LF_bytes": 7596,
    "JSON_plus_LF_sha256": "78152b9c0ea685146a3c34c1792660d42ea9f50b99b0dfb24f3d50feffcfa423"
  }
]
FREE_REQUEST={"path":"topics/visible-flex-new-mechanism/computations/request-true58-free-r1-r2.json",
 "bytes":75313,"sha256":"498633426b4bc0928e9397379235ad390dade8b54be2febe87457a74e6cecc6f"}
CLOSED_FREE_SECONDS=2974.589423877
CLOSED_PREFIX_SECONDS=3047.102915103
PREFIX_PINS={"run_id":"43891282963","job_id":"133382836465","source_commit":"30136a383796ea3a255c00e10e482c358b4e822b","workflow":".github/workflows/visible-true58-prefix102.yml","log_bytes":43523873,"log_sha256":"ff12953eb14883ab7cfad649d5476d5676c34b5a2271f9ae22c6b940fff45f5d"}
PREFIX_RECORDS=[{"tag":"MODEL","ordinal":1,"JSON_plus_LF_bytes":42929879,"JSON_plus_LF_sha256":"64d1fdd63d339b102d0ce73f92e1f042110bc2fbe11ce95a92ec59d443663921"},{"tag":"COMPLETE","ordinal":1,"JSON_plus_LF_bytes":165566,"JSON_plus_LF_sha256":"7c2bfcdc76a452a94321caa527d3dc11bf8fe1b8d74a1187b2bf82559e171de5"},{"tag":"FINAL_CLOCK","ordinal":1,"JSON_plus_LF_bytes":5695,"JSON_plus_LF_sha256":"38e876c9ace6a73b8014551b919a40969519e6cfe54f28af5cdb07440878858d"}]
PREFIX_REQUEST={"path":"topics/visible-flex-new-mechanism/computations/request-true58-prefix102.json","bytes":73398,"sha256":"0538456b189cdad619b16d4ee43b12df8be4128cdf0e4e66ee88b307b63b08c9"}
CLOSED_WHOLE_SECONDS=3642.4396103470003
WHOLE_PINS={"run_id":"43910342020","job_id":"133450221925","source_commit":"077d1dbb9c184cf4c6edf3e4c20014880d810283","workflow":".github/workflows/visible-true58-full51-whole-suffix.yml","log_bytes":3681367,"log_sha256":"502518363d74406ba91b61e972ae9c1b8bcd45768f21b2565a84f4e4d4c77135"}
WHOLE_RECORDS=[{"tag":"BODY_SOLUTION","ordinal":1,"JSON_plus_LF_bytes":9017,"JSON_plus_LF_sha256":"ba0f5264acb8b1b65ca14012341c2ab713f55bc944335e220257a05ba43e6232"},{"tag":"COMPLETE","ordinal":1,"JSON_plus_LF_bytes":178885,"JSON_plus_LF_sha256":"532a9c64f2a0133c1de61795426394f9d3f45010fd8c39e793ca7f82049ca263"},{"tag":"FINAL_CLOCK","ordinal":1,"JSON_plus_LF_bytes":6494,"JSON_plus_LF_sha256":"3ff5c74da97137ac5d3a06999fdd4b0982f19dc617276a9d2fb0b94061960a31"}]
WHOLE_REQUEST={"path":"topics/visible-flex-new-mechanism/computations/request-true58-full51-whole-suffix.json","bytes":81390,"sha256":"d6f68629b5d4824e46cec16da1ecd061456d823d0b2ef2b3a2deca7dc08ac172"}
FREE_CANDIDATE_PHYSICAL_SHA="ab59622808faafbb1a1896a2edc670585c13373869665fb95c31b6ca8a1f2773"
FREE_CANDIDATE_ARRAY_SHA="b252055bf59dbdd9e4d22691b2fd1c8ae35f88b2795c7a38f894876cd50c5da7"
FREE_CANDIDATE_BINDING_SHA="5da50ccd367a7d1f5c9f621737c5b2bafcaba2db0eb39e3875adcb3fe6fffbf0"

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
    require(isinstance(ledger,Suffix58Ledger),"one new whole-suffix account required")
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
        # Restore the already constructed, unaccepted ring candidate without
        # calling its ring model, frame/Pi batches, optimizer or body predictor.
        require(request["paid_free_source"]==FREE_PINS
            and request["paid_free_records"]==FREE_RECORDS
            and request["paid_free_request"]==FREE_REQUEST,
            "literal unaccepted free-ring candidate and last closed account required")
        free_request_bytes=Path(FREE_REQUEST["path"]).read_bytes()
        require(len(free_request_bytes)==FREE_REQUEST["bytes"]
            and reader.digest(free_request_bytes)==FREE_REQUEST["sha256"],
            "the original closed free36 request differs")
        free_request=reader.decode_json(free_request_bytes)
        free_records,free_receipts=_read_records(
            api,FREE_PINS,"TRUE58_FREE_R1_R2_",FREE_RECORDS,ledger,progress)
        free_model=free_records[("MODEL",1)]
        ring_solution=free_records[("RING_SOLUTION",1)]
        free_real=free_records[("COMPLETE",1)]
        free_clock=free_records[("FINAL_CLOCK",1)]
        require(free_real["status"]==free_clock["status_at_final_emit"]==
                    "complete-true58-free-r1-r2-observation"
            and not free_clock["scope_exhausted"]
            and free_clock["sampled_after_all_large_cache_and_complete_write_and_flush"] is True
            and free_real["github_sha"]==FREE_PINS["source_commit"]
            and str(free_real["github_run_id"])==FREE_PINS["run_id"]
            and free_real["github_repository"]==REPO
            and free_real["new_acceptances"]==0
            and free_real["selected_two_grid_physical_point"]==point
            and free_real["old_checks_executed"]==free_real["new_development_executed"]==0
            and free_real["source_files_sha256"]==free_request["source_sha256"],
            "the closed free36 task must still name the same accepted58")
        free_final=free_clock["ledger"]
        require(free_final["total_ancestor_plus_new_scientific_seconds"]==CLOSED_FREE_SECONDS
            and free_final["total_source_plus_new_started_values"]==ANCESTOR_VALUES
            and free_final["scientific_seconds"]==72.22285305100002
            and free_final["started_counts"]["free_R1_R2_model_builds"]==1
            and free_final["started_counts"]["free_R1_R2_solver_sessions"]==1
            and free_final["started_counts"]["nonlinear_candidate_predictions"]==1
            and free_final["started_counts"]["actual_trial_pairs"]==0
            and free_final["started_counts"]["actual_grid_values"]==0,
            "the entire closed free36 model, solve, failed body prediction and cost remain")
        require(ring_solution["qualified"] is True
            and ring_solution["status"]=="new-free-ring-candidate-needs-whole-body-validation"
            and free_real["prediction"]["qualified_for_original_actual"] is False,
            "ring qualification must remain distinct from failed wholebody prediction")
        ring_record=ring_solution["candidate_record"]
        saved_candidate=ring_record["rounded_independent168"]
        ring_state=exact_binary64(saved_candidate["exact_binary64"],168)
        require(saved_candidate["shape"]==[168]
            and array_binding(ring_state)["sha256"]==saved_candidate["sha256"]==FREE_CANDIDATE_BINDING_SHA
            and array_digest(ring_state)==FREE_CANDIDATE_ARRAY_SHA
            and np.asarray(saved_candidate["values"],dtype=np.float64).tobytes()==ring_state.tobytes()
            and ring_record["candidate_physical_identity_sha256"]==FREE_CANDIDATE_PHYSICAL_SHA
            and ring_record["original_current_base_physical_identity_sha256"]==PHYSICAL_SHA
            and ring_record["original_actual_box_and_new_explicit_h_pass"] is True
            and ring_record["rounded_exact_box_decision"]["exact_full_box_pass"] is True,
            "the original once-rounded unaccepted168 candidate must be restored literally")
        solution_pin=next(x for x in FREE_RECORDS if x["tag"]=="RING_SOLUTION")
        saved_receipt=free_real["ring_solution_stdout_receipt"]
        require(saved_receipt["JSON_plus_LF_bytes"]==solution_pin["JSON_plus_LF_bytes"]
            and saved_receipt["JSON_plus_LF_sha256"]==solution_pin["JSON_plus_LF_sha256"],
            "COMPLETE must name this exact original ring solution record")
        free_model_pin=next(x for x in FREE_RECORDS if x["tag"]=="MODEL")
        require(free_model["binding_sha256"]==
                    "5fb6c3a80738f6f38b08159a5102dc1d0a88448958816dcf9013902367a4aaf0"
            and ring_record["model_binding_sha256"]==free_model["binding_sha256"]
            and free_real["model_stdout_receipt"]["JSON_plus_LF_bytes"]==
                    free_model_pin["JSON_plus_LF_bytes"]
            and free_real["model_stdout_receipt"]["JSON_plus_LF_sha256"]==
                    free_model_pin["JSON_plus_LF_sha256"],
            "literal paid free36 exact embedding and original ring solution differ")
        require(request["paid_prefix_source"]==PREFIX_PINS
            and request["paid_prefix_records"]==PREFIX_RECORDS
            and request["paid_prefix_request"]==PREFIX_REQUEST,
            "literal completed prefix102 paid input and final account required")
        prefix_request_bytes=Path(PREFIX_REQUEST["path"]).read_bytes()
        require(len(prefix_request_bytes)==PREFIX_REQUEST["bytes"]
            and reader.digest(prefix_request_bytes)==PREFIX_REQUEST["sha256"],
            "the closed prefix102 request differs")
        prefix_request=reader.decode_json(prefix_request_bytes)
        prefix_records,prefix_receipts=_read_records(
            api,PREFIX_PINS,"TRUE58_PREFIX102_",PREFIX_RECORDS,ledger,progress)
        prefix_model=prefix_records[("MODEL",1)]
        prefix_real=prefix_records[("COMPLETE",1)]
        prefix_clock=prefix_records[("FINAL_CLOCK",1)]
        require(prefix_real["status"]==prefix_clock["status_at_final_emit"]==
                    "complete-true58-prefix102-observation"
            and not prefix_clock["scope_exhausted"]
            and prefix_clock["sampled_after_all_large_cache_and_complete_write_and_flush"] is True
            and prefix_real["github_sha"]==PREFIX_PINS["source_commit"]
            and str(prefix_real["github_run_id"])==PREFIX_PINS["run_id"]
            and prefix_real["github_repository"]==REPO
            and prefix_real["new_acceptances"]==0
            and prefix_real["selected_two_grid_physical_point"]==point
            and prefix_real["old_checks_executed"]==prefix_real["new_development_executed"]==0
            and prefix_real["source_files_sha256"]==prefix_request["source_sha256"],
            "closed prefix102 did not change the accepted58 point or source")
        prefix_final=prefix_clock["ledger"]
        require(prefix_final["total_ancestor_plus_new_scientific_seconds"]==CLOSED_PREFIX_SECONDS
            and prefix_final["total_source_plus_new_started_values"]==ANCESTOR_VALUES
            and prefix_final["scientific_seconds"]==72.51349122599999
            and prefix_final["started_counts"]["prefix102_model_builds"]==1
            and prefix_final["started_counts"]["new_body_input_preparations"]==1
            and prefix_final["started_counts"]["fixed_suffix_checks"]==1
            and prefix_final["started_counts"]["prefix102_solver_sessions"]==0
            and prefix_final["started_counts"]["actual_trial_pairs"]==0
            and prefix_final["started_counts"]["actual_grid_values"]==0
            and prefix_model["summary"]["status"]=="fixed-suffix-excludes-this-numerical-fiber"
            and prefix_model["summary"]["full_point_counts"]==
                    {"started":1,"completed":1,"failed":0}
            and prefix_model["summary"]["jacobian_counts"]==
                    {"started":0,"completed":0,"failed":0},
            "all failed-suffix preparation costs and zero solver/J/actual must remain")
        prefix_model_pin=next(x for x in PREFIX_RECORDS if x["tag"]=="MODEL")
        require(prefix_model["binding_sha256"]==
                    "59313c837a22d263a7813b2da0eb43c7b39050594a7a454b49e0bf39684b7272"
            and prefix_real["model_stdout_receipt"]["JSON_plus_LF_bytes"]==
                    prefix_model_pin["JSON_plus_LF_bytes"]
            and prefix_real["model_stdout_receipt"]["JSON_plus_LF_sha256"]==
                    prefix_model_pin["JSON_plus_LF_sha256"]
            and prefix_model["all_initial_global_frame_primitive_and_curvature_arrays_not_duplicated"] is True
            and prefix_model["unsaved_derived_arrays_are_not_future_free_recoverable_inputs"] is True,
            "paid source is the exact saved scalar/suffix input, not absent global derived arrays")
        require(request["closed_full51_source"]==WHOLE_PINS
            and request["closed_full51_records"]==WHOLE_RECORDS
            and request["closed_full51_request"]==WHOLE_REQUEST,
            "literal closed full51 outcome and cost required")
        whole_request_bytes=Path(WHOLE_REQUEST["path"]).read_bytes()
        require(len(whole_request_bytes)==WHOLE_REQUEST["bytes"]
            and reader.digest(whole_request_bytes)==WHOLE_REQUEST["sha256"],
            "closed full51 request identity differs")
        whole_request=reader.decode_json(whole_request_bytes)
        whole_records,whole_receipts=_read_records(
            api,WHOLE_PINS,"TRUE58_FULL51_WHOLE_SUFFIX_",WHOLE_RECORDS,ledger,progress)
        whole_solution=whole_records[("BODY_SOLUTION",1)]
        whole_real=whole_records[("COMPLETE",1)]
        whole_clock=whole_records[("FINAL_CLOCK",1)]
        require(whole_real["status"]==whole_clock["status_at_final_emit"]==
                    "complete-true58-full51-whole-suffix-observation"
            and not whole_clock["scope_exhausted"]
            and whole_clock["sampled_after_all_large_cache_and_complete_write_and_flush"] is True
            and whole_real["github_sha"]==WHOLE_PINS["source_commit"]
            and str(whole_real["github_run_id"])==WHOLE_PINS["run_id"]
            and whole_real["github_repository"]==REPO
            and whole_real["new_acceptances"]==0
            and whole_real["selected_two_grid_physical_point"]==point
            and whole_real["old_checks_executed"]==whole_real["new_development_executed"]==0
            and whole_real["source_files_sha256"]==whole_request["source_sha256"]
            and whole_solution["qualified"] is False
            and whole_solution["status"]=="stopped-at-declared-new-solver-limit"
            and whole_solution["backend_status"] is None
            and whole_solution["backend_success"] is None
            and whole_solution["actual_backend_raw53"] is None,
            "closed full51 did not return a candidate or change accepted58")
        whole_final=whole_clock["ledger"]
        require(whole_final["total_ancestor_plus_new_scientific_seconds"]==CLOSED_WHOLE_SECONDS
            and whole_final["total_source_plus_new_started_values"]==ANCESTOR_VALUES
            and whole_final["scientific_seconds"]==410.626657796
            and whole_final["ancestor_scientific_seconds"]==3231.8129525510003
            and whole_final["started_counts"]["whole_suffix_model_builds"]==1
            and whole_final["started_counts"]["whole_suffix_solver_sessions"]==1
            and whole_final["started_counts"]["nonlinear_candidate_predictions"]==0
            and whole_final["started_counts"]["actual_trial_pairs"]==0
            and whole_final["started_counts"]["actual_grid_values"]==0,
            "closed full51 clock stop and complete input/output costs remain")
        cost={"ancestor_final_original_scientific_seconds":CLOSED_WHOLE_SECONDS,
            "source_global_scientific_seconds":CLOSED_WHOLE_SECONDS,
            "source_original_full_values":ANCESTOR_VALUES,"source_original_values":ANCESTOR_VALUES,
            "source58_final_clock":copy.deepcopy(clock),
            "source_final_clock":copy.deepcopy(whole_clock),
            "prior_prefix102_final_clock":copy.deepcopy(prefix_clock),
            "prior_free36_final_clock":copy.deepcopy(free_clock),
            "all_closed_ring17_reflection_joint_free_prefix_whole34_full51_scopes_not_reopened":True,
            "earlier_checkpoint_samples_not_added_to_final_clock":True}
        source_receipt={"schema":POLICY+"-actual58-and-unaccepted-ring-source","passed":True,
            "source":copy.deepcopy(PINS),"source_records":receipts,
            "fixed_reference_source":copy.deepcopy(ANCHOR_PINS),
            "fixed_reference_records":anchor_receipts,"source_request":copy.deepcopy(SOURCE_REQUEST),
            "accepted_index":58,"physical_state_sha256":PHYSICAL_SHA,
            "independent168_array_sha256":STATE_SHA,"accepted_cache_binding_sha256":CACHE_BINDING,
            "original_log_reads":5,"old_scientific_executions":0,
            "paid_free_source":copy.deepcopy(FREE_PINS),"paid_free_records":free_receipts,
            "last_closed_free_scientific_seconds":CLOSED_FREE_SECONDS,
            "paid_prefix_source":copy.deepcopy(PREFIX_PINS),"paid_prefix_records":prefix_receipts,
            "last_closed_prefix_scientific_seconds":CLOSED_PREFIX_SECONDS,
            "closed_full51_source":copy.deepcopy(WHOLE_PINS),
            "closed_full51_records":whole_receipts,
            "last_closed_full51_scientific_seconds":CLOSED_WHOLE_SECONDS,
            "full51_large_scientific_arrays_have_bindings_only_and_are_not_reused":True,
            "whole34_missing_large_arrays_remain_unavailable":True,
            "full51_unreturned_last_callback_not_reused_as_new_seed":True,
            "paid_prefix_model_binding_sha256":prefix_model["binding_sha256"],
            "paid_free_model_binding_sha256":free_model["binding_sha256"],
            "unaccepted_ring_candidate_physical_sha256":FREE_CANDIDATE_PHYSICAL_SHA,
            "unaccepted_ring_candidate_array_sha256":FREE_CANDIDATE_ARRAY_SHA,
            "unaccepted_candidate_is_not_source_accepted_state":True,
            "missing_wholebody_arrays_are_not_reconstructed_as_paid_inputs":True,
            "second_log_only_supplies_unchanged_reference_constructor_and_original_pool_history":True}
        progress.update(status="complete",accepted_index=58,receipt=source_receipt)
        ledger.check("source58.complete")
        return {"report":real,"reference_report":anchor_real,"checkpoint":cp,
            "point":point,"state168":state,"gates":gates,"accepted_cache":cache,
            "source_stage":real["actual_stage"],"receipt":source_receipt,
            "ancestor_cost_receipt":cost,"source_final_clock":clock,
            "latest_closed_scientific_clock":whole_clock,
            "unaccepted_ring_state168":ring_state,"unaccepted_ring_record":ring_record,
            "paid_free_complete":free_real,"paid_free_solution":ring_solution,
            "paid_free_model":free_model,"paid_prefix_model":prefix_model,
            "paid_prefix_complete":prefix_real,"paid_prefix_clock":prefix_clock,
            "closed_full51_complete":whole_real,"closed_full51_clock":whole_clock}
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
    require(isinstance(ledger,Suffix58Ledger),"one shared whole-suffix ledger required")
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
    ring_state=completed["unaccepted_ring_state168"]
    require(digest(field.identity(ring_state))==FREE_CANDIDATE_PHYSICAL_SHA
        and [str(v) for v in field.full_coefficients(ring_state,exact=True)]==
            completed["unaccepted_ring_record"]["rounded_physical172_exact"],
        "same original field must bind the literal unaccepted free36 physical172")
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
            "closed_ancestor_scientific_seconds":CLOSED_WHOLE_SECONDS,
            "closed_ancestor_ordinary_values":ANCESTOR_VALUES}}
    ledger.check("prepare.complete")
    return {"accepted_cache":completed["accepted_cache"],"source_binding":source_binding,
        "problem":problem,"field168":field,"center168":state,"q168":state,"initial168":state,
        "initial159":old_state,"initial":old_state,"gate":gate,"cfg":cfg,
        "unaccepted_ring_state168":ring_state.copy(),
        "radial":radial,"theta":theta,"fine_theta":fine_theta,"grid":grid,"row_grids":grids,
        "order":order,"lower":gate.coordinate_lower,"upper":gate.coordinate_upper,
        "lower172":lower172,"upper172":upper172,
        "physical_map172x168":matrix,"physical_map_exact172x168":exact_matrix,
        "physical_map_binding":map_binding,"coarse_pool":pools["coarse"],"fine_pool":pools["fine"],
        "bindings":bindings,"replay":replay}
