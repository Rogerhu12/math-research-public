#!/usr/bin/env python3
"""Run and retain the complete same physical-root-piece source consumer."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
SCI="topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_whole_physical_root_piece_first_Airy_sources.py"
NATIVE="whole-physical-root-piece-first-Airy-sources.json.gz"
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix==".gz" else raw)
def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(value,indent=2,allow_nan=False)+"\n").encode()
    if path.suffix==".gz":raw=gzip.compress(raw,mtime=0)
    temp=path.with_name(path.name+".partial");temp.write_bytes(raw);temp.replace(path)
def payload_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def compact_channel(v):
    return {k:v[k] for k in ("complete_rows","complete_first_correction_ordinary_L2_source",
        "complete_squared_source_integral","separate_component_L2_bounds") if k in v}
def compact_case(v):
    result={k:x for k,x in v.items() if k!="source_summary"}
    result["source_summary"]={k:compact_channel(x) for k,x in v["source_summary"].items()}
    return result
def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("repo","manifest","out-dir","prepared"):p.add_argument("--"+key,type=Path,required=True)
    p.add_argument("--manifest-sha",required=True);p.add_argument("--resume",type=Path);p.add_argument("--resume-sha")
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new mathematics requires the actual public repository Actions")
    if sha(a.manifest)!=a.manifest_sha:raise ValueError("the separately pinned input manifest changed")
    m=read(a.manifest)
    if m["public_repository"]!=PUBLIC:raise ValueError("another scientific repository was supplied")
    a.out_dir.mkdir(parents=True,exist_ok=True)
    process=a.out_dir/"process.json";native=a.out_dir/NATIVE
    if process.exists() or native.exists():raise FileExistsError("preserve every actual result and failed prefix")
    state=dict(kind="actual_public_whole_physical_root_piece_first_Airy_sources",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=a.manifest_sha,complete=False,
        failure=None,actual_returncode=None,original_successful_mathematics_recomputed=0,
        complete_strong_return_or_full_inverse_claimed=False)
    code=1
    try:
        for entry in m["files"]:
            path=a.repo/entry["path"]
            if not path.is_file() or path.stat().st_size!=entry["bytes"] or sha(path)!=entry["sha256"]:
                raise ValueError("a fixed scientific input changed: "+entry["path"])
        state["verified_input_file_count"]=len(m["files"])
        state["all_exact_input_pins_preserved_in_manifest"]=True
        for entry in m.get("external_completed_natives",[]):
            path=a.prepared/entry["prepared_path"]
            if not path.is_file() or path.stat().st_size!=entry["bytes"] or sha(path)!=entry["sha256"]:
                raise ValueError("a complete immutable original artifact input changed")
        state["external_complete_original_file_count"]=len(m.get("external_completed_natives",[]))
        science=a.repo/SCI
        expected=next(v["sha256"] for v in m["files"] if v["path"]==SCI)
        if sha(science)!=expected:raise ValueError("the complete mathematical entry point changed")
        command=[sys.executable,"-u",str(science),"--repo-root",str(a.repo),
            "--manifest",str(a.manifest),"--prepared",str(a.prepared),"--out",str(native)]
        if a.resume:
            if not a.resume_sha or sha(a.resume)!=a.resume_sha:raise ValueError("the accepted prefix pin changed")
            command+=["--resume",str(a.resume)]
            state["original_prefix_sha256"]=a.resume_sha
        state["command"]=command;state["mathematical_source_sha256"]=expected
        save(process,state);started=time.monotonic()
        with (a.out_dir/"whole-physical-root-piece-first-Airy-sources.stdout.log").open("wb") as stream:
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
                raise ValueError("the actual mathematical native changed scientific identity")
            fields=("runtime","original_Taylor_native_sha256","original_Nraw_native_sha256",
                "original_bstar_complete_native_sha256","original_auxiliary_native_sha256",
                "original_moment_native_sha256","original_complete_conversion_sha256",
                "fixed_intrinsic_parameter","exact_real_delta_radius","exact_complex_coefficient_delta_radius",
                "exact_root_interval","exact_original_physical_piece_interval","exact_original_scalar_germ",
                "fixed_positive_body_cut","exact_holomorphic_rho_radius","exact_holomorphic_phi_width",
                "input_cutoff","physical_frequency","actual_first_correction_density","source_window",
                "original_targets_FFT_intrinsic_cubics_folds_signed_coefficients_and_saved_norms_recomputed",
                "original_matrix_words_or_same_order_conversions_recomputed",
                "original_exterior_complete_source_rows_recomputed","original_Airy_profiles_recomputed",
                "original_complete_angular_tail_factors_recomputed","new_profile_stages","reused_profile_stages",
                "new_radius_budget_stages","reused_radius_budget_stages","new_complete_source_rows",
                "reused_complete_source_rows","new_case_summaries","new_piece_summary_stages",
                "reused_piece_summary_stages","new_case_summary_stages","reused_case_summary_stages",
                "copied_original_complete_rows",
                "reused_copied_original_complete_rows","new_partial_original_rows","reused_partial_original_rows",
                "recovered_unindexed_complete_stages","original_complete_physical_seams_retained",
                "original_complete_normalized_seam_rows_retained",
                "all_original_failed_large_radius_gates_and_ledgers_retained",
                "actual_local_numerator_is_unnormalized","all_old_circle_and_independent_mean_terms_retained",
                "artificial_interface_source_introduced","complete_first_corrected_trial_seam_sources_paid",
                "positive_weighted_port_conversion_claimed","full_high_feedback_strong_return_or_PDE_branch_claimed",
                "exact_whole_piece_rho_cover","original_complete_holomorphic_product",
                "original_exact_inner_interval","original_complete_seam_native_sha256",
                "original_complete_matrix_row_count","whole_root_piece_row_count","preserved_actual_prefix",
                "exact_atomic_prefix_recovery")
            state["scientific_metadata"]={k:nd[k] for k in fields if k in nd}
            inventory=[];kinds={}
            for name,entry in nd.get("stages",{}).items():
                relative=Path(entry["file"])
                if relative.is_absolute() or ".." in relative.parts or relative.parts[0]!="stages":
                    raise ValueError("a natural scalar stage leaves its scientific directory")
                path=native.parent/relative
                if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                    raise ValueError("an accepted complete new scalar stage changed bytes")
                value=read(path)
                if not (value["stage"]==name and value["complete"]
                    and value["source_sha256"]==expected
                    and value["input_manifest_sha256"]==a.manifest_sha
                    and value["stage_kind"]==entry["stage_kind"]):
                    raise ValueError("a complete new scalar stage changed exact identity")
                kinds[value["stage_kind"]]=kinds.get(value["stage_kind"],0)+1
                inventory.append(dict(name=name,**entry,complete=True,
                    complete_payload_sha256=payload_sha(value["payload"])))
            case_receipts=[];domains=[]
            for entry in nd.get("case_stages",[]):
                relative=Path(entry["file"])
                if relative.is_absolute() or ".." in relative.parts or relative.parts[0]!="cases":
                    raise ValueError("a complete recombined case leaves its output directory")
                path=native.parent/relative
                if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                    raise ValueError("an accepted complete case changed bytes")
                case=read(path)
                if not (case["source_sha256"]==expected and case["input_manifest_sha256"]==a.manifest_sha):
                    raise ValueError("a complete recombination case changed science identity")
                rows=case["rows"];roles=case["row_roles"]
                if len(rows)!=len(roles):raise ValueError("the exact source row-role ledger is incomplete")
                counts={kind:sum(v["kind"]==kind for v in roles) for kind in
                    ("copied_original","partial_original","new_complete_root_piece")}
                case_receipts.append(dict(**entry,complete=case["complete"],accepted_rows=len(rows),
                    accepted_row_kinds=counts,original_complete_case_sha256=case["original_complete_case_sha256"]))
                domains.append(dict(exact_radius=case["exact_radius"],
                    original_path_gates=case["original_bstar_profile"]["domain_gates"],
                    complete_original_seam_ledger_payload_sha256=payload_sha(case["original_normalized_seam_ledger"]),
                    original_normalized_seam_rows=len(case["original_normalized_seam_ledger"]),
                    complete_original_outward_state_payload_sha256=payload_sha(case["original_complete_outward_states"]),
                    original_complete_case_summary_payload_sha256=payload_sha(case["original_complete_case_summary"]),
                    replaced_original_estimator_row_count=len(case["original_rows_wholly_replaced_by_same_solution_estimate"]),
                    actual_original_physical_seams_retained=True))
                if case["complete"] and case["complete_case_summary"] not in nd.get("cases",[]):
                    raise ValueError("an accepted complete case summary is absent from the native index")
            invpath=a.out_dir/"complete-natural-stage-and-original-norm-inventory.json.gz"
            inv=dict(public_repository=PUBLIC,run_id=state["run_id"],mathematical_native_sha256=sha(native),
                original_selected_complete_norm_and_multiplier_receipts=nd.get("original_selected_complete_stage_receipts",[]),
                new_complete_stages=inventory,case_stages=case_receipts)
            save(invpath,inv)
            state["complete_natural_stage_inventory"]=dict(file=invpath.name,
                bytes=invpath.stat().st_size,sha256=sha(invpath),complete_scalar_stage_count=len(inventory),
                accepted_complete_scalar_stage_kinds=kinds,
                original_norm_and_multiplier_stage_count=len(inv["original_selected_complete_norm_and_multiplier_receipts"]))
            state["all_available_natural_stage_files_verified"]=True
            state["complete_case_stage_receipts"]=case_receipts
            state["actual_domain_and_original_seam_reuse"]=domains
            state["actual_whole_root_piece_results"]={k:compact_channel(v)
                for k,v in nd.get("whole_root_piece_source_summary",{}).items()}
            state["actual_radius_results"]=[compact_case(v) for v in nd.get("cases",[])]
            state["complete_full_source_word_and_mean_tables_retained_in_natives"]=True
        passed=(state["actual_returncode"]==0 and state.get("mathematical_complete") is True
            and state.get("mathematical_proved") is True and state.get("mathematical_failure") is None
            and state.get("mathematical_gates") and all(v["passed"] for v in state["mathematical_gates"])
            and len(state.get("actual_radius_results",[]))==6
            and state.get("all_available_natural_stage_files_verified") is True)
        state["complete"]=bool(passed);code=0 if passed else 1
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error));code=1
    finally:
        raw=(json.dumps(state,indent=2,allow_nan=False)+"\n").encode()
        if len(raw)>60000:
            archive=a.out_dir/"complete-process-before-readable-size-guard.json.gz"
            archive.write_bytes(gzip.compress(raw,mtime=0))
            state["complete_unshortened_process_archive"]=dict(file=archive.name,
                bytes=archive.stat().st_size,sha256=sha(archive),uncompressed_bytes=len(raw))
            state["failure"]=dict(type="ValueError",message="readable actual process exceeds60000 bytes")
            state["complete"]=False;code=1
            state.pop("actual_radius_results",None)
        save(process,state)
        print(json.dumps(dict(complete=state["complete"],actual_returncode=state.get("actual_returncode"),
            failure=state.get("failure"),process_sha256=sha(process)),allow_nan=False),flush=True)
    raise SystemExit(code)
if __name__=="__main__":main()
