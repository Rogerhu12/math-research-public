#!/usr/bin/env python3
"""Run the strict exterior consumer and preserve every complete natural prefix."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(gzip.decompress(p.read_bytes()) if p.suffix==".gz" else p.read_bytes())
def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("repo","manifest","out-dir","prepared"):p.add_argument("--"+key,type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--resume",type=Path);p.add_argument("--resume-sha")
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("actual public repository Actions is required")
    if sha(a.manifest)!=a.manifest_sha:raise ValueError("the separately pinned exact manifest changed")
    manifest=json.loads(a.manifest.read_text())
    if manifest["public_repository"]!=PUBLIC:raise ValueError("wrong authorized repository")
    repo,out=a.repo.resolve(),a.out_dir.resolve()
    if out.exists() and any(out.iterdir()):raise FileExistsError("preserve every actual outcome")
    out.mkdir(parents=True,exist_ok=True)
    state=dict(kind="actual_public_strict_exterior_first_Airy_local_source_execution",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=a.manifest_sha,
        complete=False,failure=None,actual_returncode=None,
        old_successful_target_coefficient_amplitude_Fourier_seam_stages_recomputed=0,
        full_nonlocal_mean_return_or_cutoff97_inverse_claimed=False)
    def checkpoint():
        raw=json.dumps(state,indent=2,allow_nan=False)+"\n"
        if len(raw.encode())>60000:raise ValueError("the complete readable process exceeds60000 bytes")
        q=out/"process.json.partial";q.write_text(raw);q.replace(out/"process.json")
    checkpoint()
    try:
        for entry in manifest["files"]:
            path=repo/entry["path"]
            if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                raise ValueError("a pinned complete original input changed: "+entry["path"])
        state["verified_input_files"]=len(manifest["files"])
        source=repo/TOPIC/"scripts/fourfold_codazzi_strict_exterior_first_Airy_local_sources.py"
        native=out/"strict-exterior-first-Airy-local-sources.json.gz"
        command=[sys.executable,"-u",str(source),"--repo-root",str(repo),"--manifest",str(a.manifest),
            "--prepared",str(a.prepared),"--out",str(native)]
        if a.resume:
            if not a.resume_sha or sha(a.resume)!=a.resume_sha:raise ValueError("an exact original exterior prefix changed")
            command+=["--resume",str(a.resume)]
            state.update(actual_original_prefix_sha256=a.resume_sha,actual_original_prefix_bytes=a.resume.stat().st_size)
        state.update(command=command,mathematical_source_sha256=sha(source))
        checkpoint();started=time.monotonic()
        with (out/"strict-exterior-first-Airy-local-sources.stdout.log").open("wb") as stream:
            child=subprocess.Popen(command,cwd=repo,stdout=stream,stderr=subprocess.STDOUT)
            try:child.wait(timeout=2700)
            except subprocess.TimeoutExpired:
                state["actual_timeout_seconds"]=2700;child.terminate()
                try:child.wait(timeout=10)
                except subprocess.TimeoutExpired:child.kill();child.wait()
        state.update(actual_returncode=child.returncode,mathematical_wall_seconds=time.monotonic()-started)
        if native.is_file():
            state.update(native_sha256=sha(native),native_bytes=native.stat().st_size)
            doc=read(native)
            state.update(mathematical_complete=doc.get("complete"),mathematical_proved=doc.get("proved"),
                mathematical_failure=doc.get("failure"),mathematical_gates=doc.get("gates"))
            for key in ("runtime","root_native_sha256","first_forcing_native_sha256","first_seam_native_sha256",
                "complete_cancelled_fold_native_sha256","complete_old_rho_Taylor_native_sha256",
                "background_definition_sha256","explicit_direction_definition_sha256","actual_intrinsic_parameter",
                "exact_real_delta_radius","exact_root_interval","exact_cover","exact_physical_inner_interval",
                "fixed_positive_body_cut","exact_original_leading_strip","exact_new_leading_third_strip",
                "exact_local_numerator_strip","exact_amplitude_output_strip","true_local_source","source_window",
                "new_coefficient_derivative_rows","reused_coefficient_derivative_rows",
                "new_strict_exterior_rows","reused_strict_exterior_rows",
                "old_target_FFT_intrinsic_cubic_point_and_ray_stages_recomputed",
                "old_complete_forcing_coefficient_rows_recomputed","old_complete_amplitude_cases_recomputed",
                "old_complete_Taylor_algebra_stages_recomputed","old_complete_physical_seam_operators_recomputed",
                "old_circle_nonlocal_and_independent_even_mean_budget_paid",
                "all_original_physical_seams_and_mean_equations_retained","artificial_interface_source_introduced",
                "complete_strong_return_norm_or_cutoff97_inverse_claimed"):
                state[key]=doc.get(key)
            records=[]
            if doc.get("coefficient_stage"):records.append(doc["coefficient_stage"])
            records+=doc.get("case_stages",[])
            actual=[]
            for entry in records:
                relative=Path(entry["file"])
                if relative.is_absolute() or ".." in relative.parts or relative.parts[0] not in ("coefficients","cases"):
                    raise ValueError("a natural scientific stage leaves its output directory")
                path=out/relative
                if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                    raise ValueError("an actual complete natural stage changed its exact bytes")
                stage=read(path)
                if stage["source_sha256"]!=sha(source) or stage["input_manifest_sha256"]!=a.manifest_sha:
                    raise ValueError("an actual natural stage changed scientific identity")
                actual.append(dict(**entry,complete=stage.get("complete"),accepted_rows=len(stage.get("rows",[]))))
            state["all_natural_stage_records"]=actual
            state["all_available_natural_stage_files_verified"]=True
            state["actual_radius_results"]=[]
            for case in doc.get("cases",[]):
                row={key:case[key] for key in ("exact_radius","exact_cover","complete","complete_exterior_rows",
                    "complete_Fourier_factor","Fourier_tail_first_lag",
                    "negative_local_component_Hminus4over3_to_primitive_L2","positive_collar_local_source_L2",
                    "positive_body_local_source_L2","new_radial_weight_rows","reused_original_radial_weight_rows")}
                row["sides"]={}
                for side,values in case["source_summary"].items():
                    part={key:values[key] for key in ("complete_exterior_rows","complete_first_row_local_L2_source",
                        "ordinary_unnormalized_amplitude_L2_bounds","exact_enclosing_interval")}
                    part["selected_actual_w1_derivatives"]={
                        name:{norm:{key:table[key] for key in ("0,0","1,0","2,0")}
                            for norm,table in norms.items()}
                        for name,norms in values["complete_w1_exterior_derivative_suprema"].items()}
                    row["sides"][side]=part
                state["actual_radius_results"].append(row)
            for key in ("last_attempted_coefficient_row","last_attempted_exterior_row"):
                if key in doc:state[key]=doc[key]
            state["complete_full_native_and_all_other_derivative_tables_preserved"]=True
        state["complete"]=bool(child.returncode==0 and state.get("mathematical_complete")
            and state.get("mathematical_proved") and state.get("mathematical_failure") is None
            and state.get("all_available_natural_stage_files_verified"))
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error))
    finally:checkpoint()
    print(json.dumps(dict(complete=state["complete"],actual_returncode=state["actual_returncode"],
        failure=state["failure"],actual_complete_radii=len(state.get("actual_radius_results",[])),
        mathematical_failure=state.get("mathematical_failure")),allow_nan=False),flush=True)
    if not state["complete"]:raise SystemExit(1)
if __name__=="__main__":main()
