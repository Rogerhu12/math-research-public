#!/usr/bin/env python3
"""Run the exact root-value-subtracted first Airy scalar consumer."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path

PUBLIC="Rogerhu12/math-research-public"
SCI="topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_root_subtracted_first_Airy_sources.py"
NATIVE="root-subtracted-first-Airy-sources.json.gz"

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
    state=dict(kind="actual_public_root_subtracted_first_Airy_source_process",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=a.manifest_sha,
        complete=False,failure=None,actual_returncode=None,
        old_target_FFT_Taylor_coefficient_derivative_profile_or_seam_recomputation=0,
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
        with (a.out_dir/"root-subtracted-first-Airy-sources.stdout.log").open("wb") as stream:
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
            fields=("runtime","algebra_sha256","original_exterior_native_sha256","original_exterior_source_sha256",
                "original_complete_Taylor_native_sha256","original_complete_Taylor_source_sha256",
                "original_complete_auxiliary_native_sha256","original_complete_root_native_sha256",
                "original_complete_seam_native_sha256","fixed_intrinsic_parameter","exact_real_delta_radius",
                "physical_frequency","actual_first_correction_density","input_cutoff","source_window",
                "exact_root_interval","exact_cover","exact_physical_inner_interval","fixed_positive_body_cut",
                "original_complete_physical_seams_reused","original_complete_exterior_rows_reused",
                "original_complete_coefficient_rows_reused","original_complete_Taylor_finite_stages_recomputed",
                "original_target_FFT_Taylor_coefficient_derivative_seam_and_profile_stages_recomputed",
                "new_root_coefficient_norm_rows","reused_root_coefficient_norm_rows",
                "new_root_tail_stages","reused_root_tail_stages","new_case_profiles","reused_case_profiles",
                "new_seam_normalizations","reused_seam_normalizations",
                "new_divided_forcing_rows","reused_divided_forcing_rows",
                "new_refined_derivative_rows","reused_refined_derivative_rows","new_local_source_rows",
                "original_fallback_rows","reused_original_fallback_rows",
                "exact_root_mean_and_all_old_fourier_outputs_retained","true_physical_seam_sources_unchanged",
                "no_artificial_inner_interface_source","new_tables_full_old_circle_and_independent_mean_integrals_claimed",
                "positive_weighted_port_or_full_high_inverse_or_strong_cutoff97_claimed",
                "last_attempted_row","preserved_actual_prefix")
            state.update({k:nd[k] for k in fields if k in nd})
            entries=[]
            if nd.get("root_stage"):entries.append(nd["root_stage"])
            entries.extend(nd.get("case_stages",[]))
            receipts=[]
            for entry in entries:
                relative=Path(entry["file"])
                if relative.is_absolute() or ".." in relative.parts or relative.parts[0] not in ("root","cases"):
                    raise ValueError("a new natural stage leaves its exact output directory")
                path=native.parent/relative
                if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                    raise ValueError("a saved complete new natural stage changed bytes")
                stage=read(path)
                if stage.get("source_sha256")!=expected or stage.get("input_manifest_sha256")!=a.manifest_sha:
                    raise ValueError("a saved new natural stage has different science")
                item=dict(**entry,complete=stage.get("complete",False),accepted_rows=len(stage.get("rows",[])))
                if relative.parts[0]=="root":
                    item["accepted_root_coefficient_norm_rows"]=len(stage.get("coefficient_rows",[]))
                    tail=stage.get("whole_product_tail")
                    item["complete_root_tail"]=bool(tail)
                    if tail:
                        state["actual_complete_root_forcing_norms"]=tail
                else:
                    item["complete_new_profile"]=bool(stage.get("profile"))
                    item["accepted_true_seam_normalizations"]=len(stage.get("seam_normalizations",[]))
                    item["accepted_refined_derivative_rows"]=sum(bool(r.get("new_root_subtracted_derivatives"))
                        for r in stage.get("rows",[]))
                    item["accepted_original_fallback_rows"]=len(stage.get("rows",[]))-item["accepted_refined_derivative_rows"]
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
                # The original complete process above retains every derivative
                # table. Only the readable receipt omits these repeated tables.
                for case in state.get("actual_radius_results",[]):
                    for side in case.get("source_summary",{}).values():
                        side.pop("complete_w1_exterior_derivative_suprema",None)
                state["complete_derivative_tables_preserved_in_original_process_and_natives"]=True
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
