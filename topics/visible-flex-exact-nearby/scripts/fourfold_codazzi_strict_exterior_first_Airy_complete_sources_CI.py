#!/usr/bin/env python3
"""Run and retain the complete strict-exterior first Airy source consumer."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path

PUBLIC="Rogerhu12/math-research-public"
SCI="topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_strict_exterior_first_Airy_complete_sources.py"
NATIVE="strict-exterior-first-Airy-complete-sources.json.gz"

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix==".gz" else raw)
def save(path,value):
    raw=(json.dumps(value,indent=2,allow_nan=False)+"\n").encode()
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name(path.name+".partial");temp.write_bytes(raw);temp.replace(path)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo","manifest","out-dir","prepared"):p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--resume",type=Path);p.add_argument("--resume-sha")
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new mathematics runs only in the actual public repository Actions")
    if sha(a.manifest)!=a.manifest_sha:raise ValueError("the independently pinned manifest changed")
    manifest=read(a.manifest)
    if manifest["public_repository"]!=PUBLIC:raise ValueError("another repository was supplied")
    a.out_dir.mkdir(parents=True,exist_ok=True)
    process=a.out_dir/"process.json";native=a.out_dir/NATIVE
    if process.exists() or native.exists():raise FileExistsError("preserve every actual result and failure")
    state=dict(kind="actual_public_complete_strict_exterior_first_Airy_source_process",
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
        checked=[]
        for entry in manifest["files"]:
            path=a.repo/entry["path"]
            if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                raise ValueError("a complete fixed scientific input changed: "+entry["path"])
            checked.append(entry)
        state["verified_input_files"]=checked
        state["complete_external_native_receipts"]=[]
        for entry in manifest["external_completed_natives"]:
            path=a.prepared/entry["prepared_path"]
            if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                raise ValueError("an exact complete artifact input changed")
            state["complete_external_native_receipts"].append(entry)
        science=a.repo/SCI
        expected=next(x["sha256"] for x in manifest["files"] if x["path"]==SCI)
        if sha(science)!=expected:raise ValueError("the exact mathematical source differs")
        command=[sys.executable,"-u",str(science),"--repo-root",str(a.repo),
            "--manifest",str(a.manifest),"--prepared",str(a.prepared),"--out",str(native)]
        if a.resume:
            if not a.resume_sha or sha(a.resume)!=a.resume_sha:
                raise ValueError("the separately pinned complete new prefix changed")
            command+=["--resume",str(a.resume)]
            state["original_prefix_sha256"]=a.resume_sha
        state["command"]=command;state["mathematical_source_sha256"]=expected
        save(process,state)
        started=time.monotonic()
        with (a.out_dir/"strict-exterior-first-Airy-complete-sources.stdout.log").open("wb") as stream:
            try:
                child=subprocess.run(command,cwd=a.repo,stdout=stream,stderr=subprocess.STDOUT,timeout=2700)
                state["actual_returncode"]=child.returncode
            except subprocess.TimeoutExpired:
                state["actual_timeout_seconds"]=2700
                state["actual_returncode"]=124
        state["mathematical_wall_seconds"]=time.monotonic()-started
        if native.is_file():
            nd=read(native)
            state.update(native_sha256=sha(native),native_bytes=native.stat().st_size,
                mathematical_complete=nd.get("complete"),mathematical_proved=nd.get("proved"),
                mathematical_failure=nd.get("failure"),mathematical_gates=nd.get("gates",[]))
            if nd.get("source_sha256")!=expected or nd.get("input_manifest_sha256")!=a.manifest_sha:
                raise ValueError("the actual native lost its source or input identity")
            fields=("runtime","original_exterior_run_id","original_exterior_source_sha256",
                "original_exterior_native_sha256","original_exterior_process_sha256","original_exterior_manifest_sha256",
                "original_inner_native_sha256","original_inner_source_sha256",
                "original_complete_root_native_sha256","original_complete_directed_native_sha256",
                "original_complete_moment_native_sha256","original_complete_seam_native_sha256",
                "fixed_intrinsic_parameter","exact_real_delta_radius","exact_complete_inner_radius",
                "input_cutoff","physical_frequency","actual_first_correction_density","source_window",
                "exact_root_interval","exact_physical_inner_interval","exact_cover","fixed_positive_body_cut",
                "original_all1328_coefficient_identities_verified","original_complete_directed_table_payload_sha256",
                "original_complete_derivative_table_payload_sha256",
                "original_target_FFT_intrinsic_coefficient_fold_ray_Taylor_and_derivative_stages_recomputed",
                "original_complete_matrix_words_recomputed","original_exterior_local_sources_recomputed",
                "original_complete_six_analytic_profiles_recomputed","original_physical_seams_recomputed",
                "new_same_order_matrix_conversions","reused_new_same_order_matrix_conversions",
                "reused_inner_same_order_matrix_conversions","new_complete_profiles","reused_complete_profiles",
                "new_complete_source_rows","reused_complete_source_rows",
                "all_fourier_outputs_old_projections_and_independent_mean_retained",
                "artificial_interface_source_introduced","complete_first_corrected_trial_seam_sources_paid",
                "positive_weighted_port_conversion_claimed",
                "full_high_feedback_strong_return_cutoff97_inverse_or_PDE_branch_claimed",
                "last_attempted_matrix_row","last_attempted_profile","last_attempted_source_row",
                "preserved_actual_prefix")
            state.update({k:nd[k] for k in fields if k in nd})
            entries=[]
            if nd.get("coefficient_stage"):entries.append(nd["coefficient_stage"])
            entries.extend(nd.get("case_stages",[]))
            receipts=[]
            for entry in entries:
                relative=Path(entry["file"])
                if relative.is_absolute() or ".." in relative.parts or relative.parts[0] not in ("coefficients","cases"):
                    raise ValueError("a new natural stage leaves its exact output directory")
                path=native.parent/relative
                if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                    raise ValueError("a saved complete new natural stage changed bytes")
                stage=read(path)
                if stage.get("source_sha256")!=expected or stage.get("input_manifest_sha256")!=a.manifest_sha:
                    raise ValueError("a saved new natural stage has different science")
                item=dict(**entry,complete=stage.get("complete",False),accepted_rows=len(stage.get("rows",[])))
                if relative.parts[0]=="cases":
                    profile=stage.get("complete_new_profile")
                    item["complete_new_profile"]=bool(profile and profile.get("complete"))
                    if profile:
                        canonical=json.dumps(profile["payload"],sort_keys=True,separators=(",",":"),allow_nan=False).encode()
                        if hashlib.sha256(canonical).hexdigest()!=profile["payload_sha256"]:
                            raise ValueError("an accepted complete profile payload changed")
                        item["profile_payload_sha256"]=profile["payload_sha256"]
                        item["complete_inverse_phase_Fourier_tail"]=profile["payload"]["complete_fourier_evidence"]
                receipts.append(item)
            state["all_natural_stage_records"]=receipts
            state["all_available_natural_stage_files_verified"]=True
            state["actual_radius_results"]=nd.get("cases",[])
            state["complete_all_other_amplitude_and_operator_details_preserved_in_native"]=True
        passed=(state["actual_returncode"]==0 and state.get("mathematical_complete") is True
            and state.get("mathematical_proved") is True and state.get("mathematical_failure") is None
            and state.get("mathematical_gates") and all(g["passed"] for g in state["mathematical_gates"])
            and len(state.get("actual_radius_results",[]))==6
            and state.get("all_available_natural_stage_files_verified") is True)
        state["complete"]=bool(passed)
        resultcode=0 if passed else 1
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error))
        resultcode=1
    finally:
        raw=(json.dumps(state,indent=2,allow_nan=False)+"\n").encode()
        if len(raw)>60000:
            state["summary_size_failure"]=dict(bytes=len(raw),maximum=60000)
            state["full_process_preserved_in_actual_artifact"]=True
            (a.out_dir/"complete-process-before-summary-size-limit.json").write_bytes(raw)
            state.pop("verified_input_files",None)
            state["verified_input_file_count"]=len(manifest["files"])
            state["verified_input_manifest_sha256"]=a.manifest_sha
            raw=(json.dumps(state,indent=2,allow_nan=False)+"\n").encode()
            if len(raw)>60000:
                state["failure"]=dict(type="ValueError",message="complete readable process still exceeds60000 bytes")
                state["complete"]=False;resultcode=1
                state.pop("actual_radius_results",None)
        save(process,state)
        print(json.dumps(dict(complete=state["complete"],actual_returncode=state.get("actual_returncode"),
            failure=state.get("failure"),process_sha256=sha(process)),allow_nan=False),flush=True)
    raise SystemExit(resultcode)
if __name__=="__main__":main()
