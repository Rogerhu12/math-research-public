#!/usr/bin/env python3
"""Execute and retain complete root-subtracted first Airy source merging."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
SCI="topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_root_subtracted_first_Airy_complete_sources.py"
NATIVE="root-subtracted-first-Airy-complete-sources.json.gz"
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix==".gz" else raw)
def save(path,value):
    raw=(json.dumps(value,indent=2,allow_nan=False)+"\n").encode()
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name(path.name+".partial");temp.write_bytes(raw);temp.replace(path)
def payload_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo","manifest","out-dir","prepared"):p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--resume",type=Path);p.add_argument("--resume-sha")
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new mathematics requires the actual public repository Actions")
    if sha(a.manifest)!=a.manifest_sha:raise ValueError("the separately pinned manifest changed")
    m=read(a.manifest)
    if m["public_repository"]!=PUBLIC:raise ValueError("another public repository was supplied")
    a.out_dir.mkdir(parents=True,exist_ok=True)
    process=a.out_dir/"process.json";native=a.out_dir/NATIVE
    if process.exists() or native.exists():raise FileExistsError("preserve every actual result and failure")
    state=dict(kind="actual_public_complete_root_subtracted_first_Airy_source_process",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=a.manifest_sha,
        complete=False,failure=None,actual_returncode=None,
        old_target_matrix_coefficient_derivative_profile_or_seam_recomputation=0,
        final_strong_return_or_cutoff97_inverse_claimed=False)
    resultcode=1
    try:
        for entry in m["files"]:
            path=a.repo/entry["path"]
            if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                raise ValueError("a complete fixed input changed: "+entry["path"])
        state["verified_input_file_count"]=len(m["files"])
        state["verified_input_manifest_sha256"]=a.manifest_sha
        state["complete_external_native_receipts"]=[]
        for entry in m["external_completed_natives"]:
            path=a.prepared/entry["prepared_path"]
            if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                raise ValueError("an exact complete original artifact input changed")
            state["complete_external_native_receipts"].append(entry)
        science=a.repo/SCI
        expected=next(v["sha256"] for v in m["files"] if v["path"]==SCI)
        if sha(science)!=expected:raise ValueError("the exact mathematical source differs")
        command=[sys.executable,"-u",str(science),"--repo-root",str(a.repo),
            "--manifest",str(a.manifest),"--prepared",str(a.prepared),"--out",str(native)]
        if a.resume:
            if not a.resume_sha or sha(a.resume)!=a.resume_sha:
                raise ValueError("the separately pinned accepted source prefix changed")
            command+=["--resume",str(a.resume)]
            state["original_prefix_sha256"]=a.resume_sha
        state["command"]=command;state["mathematical_source_sha256"]=expected
        save(process,state);started=time.monotonic()
        with (a.out_dir/"root-subtracted-first-Airy-complete-sources.stdout.log").open("wb") as stream:
            try:
                child=subprocess.run(command,cwd=a.repo,stdout=stream,stderr=subprocess.STDOUT,timeout=2700)
                state["actual_returncode"]=child.returncode
            except subprocess.TimeoutExpired:
                state["actual_timeout_seconds"]=2700;state["actual_returncode"]=124
        state["mathematical_wall_seconds"]=time.monotonic()-started
        if native.is_file():
            nd=read(native)
            state.update(native_sha256=sha(native),native_bytes=native.stat().st_size,
                mathematical_complete=nd.get("complete"),mathematical_proved=nd.get("proved"),
                mathematical_failure=nd.get("failure"),mathematical_gates=nd.get("gates",[]))
            if nd.get("source_sha256")!=expected or nd.get("input_manifest_sha256")!=a.manifest_sha:
                raise ValueError("the actual native lost its complete source or input identity")
            fields=("runtime","original_complete_exterior_native_sha256","original_complete_exterior_source_sha256",
                "original_complete_exterior_manifest_sha256","original_complete_exterior_process_sha256",
                "original_bstar_native_sha256","original_bstar_source_sha256","original_bstar_manifest_sha256",
                "original_bstar_process_sha256","original_exterior_local_native_sha256",
                "original_complete_moment_native_sha256","original_complete_directed_native_sha256",
                "original_complete_root_native_sha256","original_complete_seam_native_sha256",
                "fixed_intrinsic_parameter","exact_real_delta_radius","exact_complete_inner_radius",
                "input_cutoff","physical_frequency","actual_first_correction_density",
                "exact_amplitude_output_phi_width","source_window","exact_root_interval",
                "exact_physical_inner_interval","exact_cover","fixed_positive_body_cut",
                "original_target_FFT_intrinsic_fold_Taylor_coefficient_or_derivative_stages_recomputed",
                "original_complete_matrix_words_recomputed","original_same_order_matrix_conversions_recomputed",
                "original_Airy_phase_profiles_recomputed","original_local_source_integrals_recomputed",
                "original_root_norms_or_divided_forcing_or_seam_normalizations_recomputed",
                "new_complete_operator_rows","reused_new_complete_operator_rows",
                "copied_original_complete_source_rows","reused_copied_original_complete_source_rows",
                "new_complete_source_integrals","new_radius_source_summaries",
                "reused_complete_same_order_matrix_rows","original_complete_physical_seams_retained",
                "original_complete_normalized_seam_rows_retained",
                "original_failed_path_gates_and_every_physical_seam_retained",
                "all_fourier_outputs_old_projections_and_independent_mean_retained",
                "artificial_interface_source_introduced","complete_first_corrected_trial_seam_sources_paid",
                "positive_weighted_port_conversion_claimed",
                "full_high_feedback_strong_return_cutoff97_inverse_or_PDE_branch_claimed",
                "last_attempted_row","preserved_actual_prefix")
            state.update({k:nd[k] for k in fields if k in nd})
            receipts=[];diagnostics=[];domains=[]
            for entry in nd.get("case_stages",[]):
                relative=Path(entry["file"])
                if relative.is_absolute() or ".." in relative.parts or relative.parts[0]!="cases":
                    raise ValueError("a complete natural case leaves the output directory")
                path=native.parent/relative
                if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                    raise ValueError("an accepted complete natural case changed bytes")
                stage=read(path)
                if stage.get("source_sha256")!=expected or stage.get("input_manifest_sha256")!=a.manifest_sha:
                    raise ValueError("a new case changed its exact mathematics")
                rows=stage.get("rows",[]);consumed=stage.get("row_consumption",[])
                if len(rows)!=len(consumed):raise ValueError("an accepted row ledger is incomplete")
                profile=stage["complete_new_profile"]
                if not profile["complete"] or profile["payload_sha256"]!=payload_sha(profile["payload"]):
                    raise ValueError("an unchanged original complete Airy profile changed payload")
                item=dict(**entry,complete=stage.get("complete",False),accepted_rows=len(rows),
                    accepted_new_operator_rows=sum(v["new_complete_source_operator_evaluation"] for v in consumed),
                    original_full_rows_copied=sum(not v["new_complete_source_operator_evaluation"] for v in consumed),
                    original_complete_case_sha256=stage["original_complete_case_sha256"],
                    original_bstar_case_sha256=stage["original_bstar_case_sha256"],
                    original_complete_profile_payload_sha256=profile["payload_sha256"],
                    original_complete_profile_recomputed=stage["original_complete_profile_recomputed"])
                receipts.append(item)
                domains.append(dict(exact_radius=stage["exact_radius"],
                    actual_domain_gates=stage["original_bstar_profile"]["domain_gates"],
                    original_normalized_seam_rows=len(stage["original_normalized_seam_ledger"]),
                    complete_original_seam_ledger_payload_sha256=payload_sha(stage["original_normalized_seam_ledger"]),
                    original_complete_outward_states_payload_sha256=payload_sha(stage["original_complete_outward_states"]),
                    all_true_physical_seams_retained=True))
                if stage.get("complete"):
                    if stage["complete_case_summary"] not in nd.get("cases",[]):
                        raise ValueError("a completed case summary is absent from its native index")
                    diagnostics.append(dict(exact_radius=stage["exact_radius"],
                        actual_new_derivative_rows=stage["accepted_new_derivative_rows"],
                        complete_source_rows_copied_verbatim=stage["original_complete_source_rows_copied_verbatim"],
                        original_complete_summary_reused_verbatim=stage["original_complete_summary_reused_verbatim"],
                        dominant_rows=stage["complete_dominant_accepted_row_diagnostics"]))
            state["all_natural_stage_records"]=receipts
            state["all_available_natural_stage_files_verified"]=True
            state["actual_radius_results"]=nd.get("cases",[])
            state["actual_domain_and_seam_reuse"]=domains
            diagnostic_path=a.out_dir/"complete-source-dominant-row-diagnostics.json"
            diagnostic_doc=dict(public_repository=PUBLIC,run_id=state["run_id"],
                complete=bool(nd.get("complete")),mathematical_native_sha256=sha(native),
                cases=diagnostics,only_diagnostics_of_accepted_bounds=True)
            save(diagnostic_path,diagnostic_doc)
            state["complete_dominant_row_diagnostics"]=dict(file=diagnostic_path.name,
                bytes=diagnostic_path.stat().st_size,sha256=sha(diagnostic_path))
            state["all_original_and_new_term_evidence_preserved_in_complete_natives"]=True
        passed=(state["actual_returncode"]==0 and state.get("mathematical_complete") is True
            and state.get("mathematical_proved") is True and state.get("mathematical_failure") is None
            and state.get("mathematical_gates") and all(v["passed"] for v in state["mathematical_gates"])
            and len(state.get("actual_radius_results",[]))==6
            and state.get("all_available_natural_stage_files_verified") is True)
        state["complete"]=bool(passed);resultcode=0 if passed else 1
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error));resultcode=1
    finally:
        raw=(json.dumps(state,indent=2,allow_nan=False)+"\n").encode()
        if len(raw)>60000:
            fullpath=a.out_dir/"complete-process-before-summary-size-limit.json.gz"
            fullpath.write_bytes(gzip.compress(raw,mtime=0))
            state["full_process_preserved_before_summary_compaction"]=dict(
                file=fullpath.name,bytes=fullpath.stat().st_size,sha256=sha(fullpath),
                uncompressed_bytes=len(raw))
            # Manifest and complete native retain the exact same source words.
            state["complete_external_native_receipt_count"]=len(state.get("complete_external_native_receipts",[]))
            state.pop("complete_external_native_receipts",None)
            for case in state.get("actual_radius_results",[]):
                for side in case.get("source_summary",{}).values():
                    side.pop("individual_first_row_nonlocal_L2_bounds",None)
            raw=(json.dumps(state,indent=2,allow_nan=False)+"\n").encode()
            if len(raw)>60000:
                state["failure"]=dict(type="ValueError",message="readable complete process still exceeds60000 bytes")
                state["complete"]=False;resultcode=1
                state.pop("actual_radius_results",None)
        save(process,state)
        print(json.dumps(dict(complete=state["complete"],actual_returncode=state.get("actual_returncode"),
            failure=state.get("failure"),process_sha256=sha(process)),allow_nan=False),flush=True)
    raise SystemExit(resultcode)
if __name__=="__main__":main()
