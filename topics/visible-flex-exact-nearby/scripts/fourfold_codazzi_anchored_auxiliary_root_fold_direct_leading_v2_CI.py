#!/usr/bin/env python3
"""Consume completed auxiliary jets for anchored folds and direct leading derivatives."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo","manifest","out-dir","prepared"):p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--resume",type=Path);p.add_argument("--resume-sha")
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("the genuine public repository Actions environment is required")
    if sha(a.manifest)!=a.manifest_sha:raise ValueError("the exact reviewed scientific manifest changed")
    manifest=json.loads(a.manifest.read_text())
    if manifest["public_repository"]!=PUBLIC:raise ValueError("wrong public repository")
    repo,output=a.repo.resolve(),a.out_dir.resolve()
    if output.exists() and any(output.iterdir()):raise FileExistsError("retain every actual outcome")
    output.mkdir(parents=True,exist_ok=True)
    state=dict(kind="actual_public_anchored_auxiliary_root_fold_direct_leading_v2_execution",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=a.manifest_sha,
        complete=False,failure=None,actual_returncode=None,
        original_targets_primitives_cubics_and_completed_domain_jets_recomputed=0,
        auxiliary_extension_only=True,physical_background_identity_outside_original_piece_claimed=False,
        full_strong_return_or_cutoff97_inverse_claimed=False)
    def checkpoint():
        raw=json.dumps(state,indent=2,allow_nan=False)+"\n"
        if len(raw.encode())>60000:raise ValueError("the complete readable process exceeds60000 bytes")
        (output/"process.json").write_text(raw)
    checkpoint()
    try:
        for f in manifest["files"]:
            path=repo/f["path"]
            if not path.is_file() or sha(path)!=f["sha256"] or path.stat().st_size!=f["bytes"]:
                raise ValueError("an original exact input changed: "+f["path"])
        state["verified_input_files"]=len(manifest["files"])
        source=repo/TOPIC/"scripts/fourfold_codazzi_anchored_auxiliary_root_fold_direct_leading_v2.py"
        native=output/"anchored-auxiliary-root-fold-direct-leading-v2.json.gz"
        command=[sys.executable,"-u",str(source),"--repo-root",str(repo),
            "--manifest",str(a.manifest),"--out",str(native)]
        if a.resume is not None:
            if not a.resume_sha or sha(a.resume)!=a.resume_sha:raise ValueError("the accepted exact prefix changed")
            command+=["--resume",str(a.resume)]
            state["actual_original_prefix_sha256"]=a.resume_sha
            state["actual_original_prefix_bytes"]=a.resume.stat().st_size
        state.update(command=command,mathematical_source_sha256=sha(source));checkpoint()
        started=time.monotonic()
        try:
            with (output/"anchored-auxiliary-root-fold-direct-leading-v2.stdout.log").open("wb") as stream:
                child=subprocess.run(command,cwd=repo/TOPIC,stdout=stream,stderr=subprocess.STDOUT,
                    timeout=2700,check=False,env=dict(os.environ,OPENBLAS_NUM_THREADS="1",
                    OMP_NUM_THREADS="1",PYTHONDONTWRITEBYTECODE="1"))
            state["actual_returncode"]=child.returncode
        except subprocess.TimeoutExpired:
            state["actual_returncode"]=124;state["timeout_seconds"]=2700
        finally:state["mathematical_wall_seconds"]=time.monotonic()-started
        if native.is_file():
            state["native_sha256"]=sha(native);state["native_bytes"]=native.stat().st_size
            doc=json.loads(gzip.decompress(native.read_bytes()))
            state["mathematical_complete"]=doc.get("complete") is True
            state["mathematical_failure"]=doc.get("failure")
            state["mathematical_gates"]=doc.get("gates",[])
            for key in ("background_definition_sha256","explicit_direction_definition_sha256",
                "actual_intrinsic_parameter","exact_complex_delta_radius","root_germ_sha256",
                "root_budget_sha256","auxiliary_native_sha256","exact_root_interval",
                "exact_original_piece_interval","exact_original_scalar_germ",
                "original_targets_primitives_cubics_and_completed_domain_jets_recomputed",
                "true_root_anchor_and_complete_parameter_mean_retained",
                "physical_background_outside_original_piece_changed",
                "original_physical_seam_and_source_equations_retained",
                "old_circle_I_J_and_independent_mean_source_on_w1_paid",
                "complete_strong_return_or_cutoff97_inverse_claimed",
                "original_auxiliary_audit_global_proved_false_retained","original_anchor_reused",
                "new_coefficient_cases","reused_coefficient_cases","new_fold_cases","reused_fold_cases",
                "new_direct_leading_cases","reused_direct_leading_cases",
                "new_first_forcing_cases","reused_first_forcing_cases",
                "original_prefix_run","original_prefix_native_sha256","original_prefix_source_sha256",
                "original_prefix_manifest_sha256","original_prefix_actual_returncode",
                "original_prefix_global_proved_false_retained","complete_old_smaller_case_recomputed",
                "original_complete_coefficient_stages_recomputed","new_characteristic_refinements",
                "reused_characteristic_refinements","original_smaller_case_payload_sha256",
                "original_larger_coefficient_payload_sha256","complete_smaller_case_payload_unchanged",
                "complete_larger_coefficient_payload_unchanged"):
                state[key]=doc.get(key)
            def short(v):
                if isinstance(v,dict):
                    if "ball" in v:return v["ball"]
                    return {k:short(w) for k,w in v.items()}
                if isinstance(v,list):return [short(w) for w in v]
                return v
            state["complete_original_root_anchor"]=short(doc.get("complete_original_root_anchor"))
            prior=doc.get("original_larger_failed_case_audit",{})
            state["original_larger_failed_case_audit"]={k:prior.get(k) for k in (
                "exact_input_auxiliary_radius","exact_fold_radius","complete","proved",
                "attempt_complete","failure","gates")}
            cases=[]
            for c in doc.get("cases",[]):
                row={k:c.get(k) for k in ("exact_input_auxiliary_radius","exact_fold_radius",
                    "exact_coefficient_width","exact_old_leading_width",
                    "complete","proved","attempt_complete","failure","gates")}
                ce=c.get("coefficient_evidence",{})
                row["anchored_complete_boxes"]={k:short(ce.get(k)) for k in (
                    "complete_subdomain_k","complete_subdomain_eta",
                    "complete_current_Kr","complete_characteristic_a")}
                re=c.get("characteristic_refinement_evidence",{})
                row["characteristic_refinement_evidence"]={k:short(re.get(k)) for k in (
                    "exact_refinement_identity","exact_fold_radius","complete_old_characteristic_box",
                    "complete_root_integral_box","complete_new_characteristic_box",
                    "saved_original_radial_derivative_bound","independent_modulus_bound",
                    "original_complete_coefficient_constructor_called")} if re else None
                if re:row["anchored_complete_boxes"]["complete_characteristic_a"]=short(re["complete_new_characteristic_box"])
                cm=re.get("complete_refined_coefficient_majorants",ce.get("complete_coefficient_majorants",{}))
                row["complete_coefficient_bounds"]={k:short(cm.get(k)) for k in (
                    "km","kp","em","ep","am","ap","k1","k2","a1","a2","D","Dr",
                    "beta","beta_r","K","Kr","T0","V0","vartheta","rQ","ell",
                    "b0","eta_log_r","log_EG_r","log_EG_rr")}
                row["fold_evidence"]=short(c.get("fold_evidence"))
                le=c.get("direct_leading_evidence",{})
                row["direct_leading_evidence"]={k:short(le.get(k)) for k in (
                    "auxiliary_seam_fee_exactly_zero_only_for_the_analytic_extension",
                    "actual_global_physical_seams_retained","radial_Cauchy_used_for_leading_second_derivatives",
                    "A_mixed_derivatives","G_mixed_derivatives",
                    "direct_a0_ordinary_derivatives","direct_b0_ordinary_derivatives","full_direct_fold_chain")}
                row["first_forcing_evidence"]=short(c.get("first_forcing_evidence"))
                cases.append(row)
            state["cases"]=cases
            state["all_full_scientific_stages_and_prefixes_preserved_in_native"]=True
            state["mathematical_proved"]=doc.get("proved") is True
        state["complete"]=(state["actual_returncode"]==0 and native.is_file() and state.get("mathematical_complete") is True and state.get("mathematical_proved") is True)
        if state["actual_returncode"]:raise SystemExit(state["actual_returncode"])
        if not state["complete"]:raise RuntimeError("the actual anchored auxiliary fold and forcing budget did not finish")
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint();print(json.dumps(state,allow_nan=False),flush=True)
if __name__=="__main__":main()
