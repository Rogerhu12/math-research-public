#!/usr/bin/env python3
"""Run the complete old-radial first Airy Taylor algebra and retain all stages."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("repo","manifest","out-dir","prepared"):p.add_argument("--"+key,type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--resume",type=Path);p.add_argument("--resume-sha")
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("actual public repository Actions is required")
    if sha(a.manifest)!=a.manifest_sha:raise ValueError("the separately pinned manifest changed")
    manifest=json.loads(a.manifest.read_text())
    if manifest["public_repository"]!=PUBLIC:raise ValueError("wrong public repository")
    repo,out=a.repo.resolve(),a.out_dir.resolve()
    if out.exists() and any(out.iterdir()):raise FileExistsError("preserve every actual outcome")
    out.mkdir(parents=True,exist_ok=True)
    state=dict(kind="actual_public_complete_old_rho_first_Airy_Taylor_execution",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=a.manifest_sha,
        complete=False,failure=None,actual_returncode=None,
        old_target_FFT_intrinsic_and_auxiliary_stages_recomputed=0,
        old_circle_I_J_or_independent_even_mean_budget_paid=False,
        full_strong_return_or_cutoff97_inverse_claimed=False)
    def checkpoint():
        raw=json.dumps(state,indent=2,allow_nan=False)+"\n"
        if len(raw.encode())>60000:raise ValueError("the full readable process exceeds60000 bytes")
        (out/"process.json").write_text(raw)
    checkpoint()
    try:
        for f in manifest["files"]:
            path=repo/f["path"]
            if not path.is_file() or sha(path)!=f["sha256"] or path.stat().st_size!=f["bytes"]:
                raise ValueError("a pinned original mathematical input changed: "+f["path"])
        state["verified_input_files"]=len(manifest["files"])
        source=repo/TOPIC/"scripts/fourfold_codazzi_old_rho_first_Airy_Taylor.py"
        native=out/"complete-old-rho-first-Airy-Taylor.json.gz"
        command=[sys.executable,"-u",str(source),"--repo-root",str(repo),
            "--manifest",str(a.manifest),"--out",str(native)]
        if a.resume is not None:
            if not a.resume_sha or sha(a.resume)!=a.resume_sha:
                raise ValueError("the original exact finite prefix changed")
            command+=["--resume",str(a.resume)]
            state["actual_original_prefix_sha256"]=a.resume_sha
            state["actual_original_prefix_bytes"]=a.resume.stat().st_size
        state.update(command=command,mathematical_source_sha256=sha(source))
        checkpoint();started=time.monotonic()
        with (out/"complete-old-rho-first-Airy-Taylor.stdout.log").open("wb") as stream:
            child=subprocess.Popen(command,cwd=repo,stdout=stream,stderr=subprocess.STDOUT)
            try:child.wait(timeout=2700)
            except subprocess.TimeoutExpired:
                state["actual_timeout_seconds"]=2700;child.terminate()
                try:child.wait(timeout=10)
                except subprocess.TimeoutExpired:child.kill();child.wait()
        state.update(actual_returncode=child.returncode,mathematical_wall_seconds=time.monotonic()-started)
        if native.is_file():
            state.update(native_sha256=sha(native),native_bytes=native.stat().st_size)
            doc=json.loads(gzip.decompress(native.read_bytes()))
            state.update(mathematical_complete=doc.get("complete"),mathematical_proved=doc.get("proved"),
                mathematical_failure=doc.get("failure"),mathematical_gates=doc.get("gates"))
            for k in ("runtime","algebra_sha256","root_germ_sha256","root_budget_sha256",
                "complete_high_root_native_sha256","complete_high_root_process_sha256",
                "complete_larger_fold_native_sha256","background_definition_sha256",
                "explicit_direction_definition_sha256","actual_intrinsic_parameter",
                "exact_fixed_intrinsic_parameter","exact_complex_delta_radius",
                "exact_root_interval","exact_original_physical_piece_interval",
                "original_completed_point_payload_sha256","old_failed_high_root_source_and_point_retained",
                "leading_Taylor_order","forcing_Taylor_order","first_correction_Taylor_order",
                "complete_non_circular_Fourier_algebra","physical_angle_frequency_multiplier",
                "original_target_FFT_or_high_root_stages_recomputed",
                "original_auxiliary_fold_forcing_or_domain_stages_recomputed",
                "new_cubic_true_root_component_rows","reused_cubic_true_root_component_rows",
                "new_finite_algebra_stages","reused_finite_algebra_stages",
                "branch_epsilon_computed","negative_branch_reused_by_exact_same_complex_parameter_symmetry",
                "complete_branch_identity","complete_Fourier_coefficient_support",
                "old_circle_I_J_or_independent_even_mean_budget_paid",
                "complete_strong_return_or_cutoff97_inverse_claimed",
                "all_original_physical_seams_and_independent_mean_equations_retained",
                "physical_background_outside_original_piece_replaced"):
                state[k]=doc.get(k)
            state["complete_cubic_point_prefix_counts"]={k:len(v) for k,v in doc.get("cubic_point_rows",{}).items()}
            state["accepted_natural_algebra_stages"]=len(doc.get("stages",{}))
            state["complete_natural_stage_files"]={k:dict(bytes=v["bytes"],sha256=v["sha256"])
                for k,v in doc.get("stages",{}).items()}
            def small(v):
                if isinstance(v,list):return [small(x) for x in v]
                if isinstance(v,dict):
                    if "ball" in v:return v["ball"]
                    return {k:small(x) for k,x in v.items()}
                return v
            state["old_product_domain"]=small(doc.get("old_product_domain"))
            reports=[]
            for row in doc.get("first_correction_derivative_budgets",[]):
                table={k:{kind:small(v[kind]) for kind in ("strip_sup","Wiener")}
                    for k,v in row["first_amplitude_budgets"].items()}
                reports.append(dict(
                    exact_output_phi_width=row["exact_output_phi_width"],
                    first_amplitude_budgets=table,
                    complete_normalized_local_L0_w1_sup_bounds=small(row["complete_normalized_local_L0_w1_sup_bounds"]),
                    complete_normalized_local_L0_w1_sup_parts=small(row["complete_normalized_local_L0_w1_sup_parts"]),
                    unnormalized_local_operator_sup_bounds=small(row["unnormalized_local_operator_sup_bounds"]),
                    local_operator_output_space=row["local_operator_output_space"],
                    full_tail_finite_prefix_split_preserved_in_native=True))
            state["old_derivative_budgets"]=reports
            if "original_prefix_audit" in doc:
                old=doc["original_prefix_audit"]
                state["original_prefix_audit"]={k:old.get(k) for k in
                    ("native_sha256","native_bytes","run_id","complete","proved","failure","stage_count")}
            for name,row in doc.get("stages",{}).items():
                path=out/row["file"]
                if not path.is_file() or sha(path)!=row["sha256"] or path.stat().st_size!=row["bytes"]:
                    raise ValueError("a complete natural stage was not preserved: "+name)
            state["all_complete_Fourier_arrays_and_all_natural_prefix_files_verified"]=True
        state["complete"]=(state["actual_returncode"]==0 and native.is_file()
            and state.get("mathematical_complete") is True and state.get("mathematical_proved") is True)
        if state["actual_returncode"]:raise SystemExit(state["actual_returncode"])
        if not state["complete"]:raise RuntimeError("the complete old-radial Taylor calculation did not finish")
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint();print(json.dumps(dict(complete=state["complete"],
            actual_returncode=state["actual_returncode"],failure=state["failure"],
            native_sha256=state.get("native_sha256")),allow_nan=False),flush=True)
if __name__=="__main__":main()
