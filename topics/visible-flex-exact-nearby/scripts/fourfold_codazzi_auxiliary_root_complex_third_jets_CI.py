#!/usr/bin/env python3
"""Execute only new auxiliary root-piece domains and complete complex third jets."""
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
    state=dict(kind="actual_public_auxiliary_root_complex_third_jets_execution",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=a.manifest_sha,
        complete=False,failure=None,actual_returncode=None,
        original_completed_small_domain_results_recomputed=0,
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
        source=repo/TOPIC/"scripts/fourfold_codazzi_auxiliary_root_complex_third_jets.py"
        native=output/"auxiliary-root-complex-third-jets.json.gz"
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
            with (output/"auxiliary-root-complex-third-jets.stdout.log").open("wb") as stream:
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
                "object_sha256","root_germ_sha256","original_root_budget_sha256",
                "exact_complex_delta_radius","actual_intrinsic_parameter","exact_root_interval",
                "original_scalar_germ","original_polynomial_piece","exact_original_piece_interval",
                "exact_physical_candidate_amplitude","exact_intrinsic_affine_center",
                "exact_intrinsic_affine_half_width","original_completed_small_domain_results_recomputed",
                "new_intrinsic_domains","reused_intrinsic_domains",
                "new_original_cubic_component_jet_rows","reused_original_cubic_component_jet_rows",
                "auxiliary_extension_only","physical_background_identity_outside_original_piece_claimed",
                "every_original_global_seam_and_full_mean_retained",
                "enlarged_fold_or_first_amplitude_budget_paid",
                "full_strong_return_or_cutoff97_inverse_claimed",
                "all_requested_domains_attempted","successful_auxiliary_domains","failed_auxiliary_domains"):
                state[key]=doc.get(key)
            def short(v):
                if isinstance(v,dict):
                    if "ball" in v:return v["ball"]
                    return {k:short(w) for k,w in v.items()}
                if isinstance(v,list):return [short(w) for w in v]
                return v
            cases=[]
            for c in doc.get("cases",[]):
                row={k:c.get(k) for k in ("exact_auxiliary_radius","exact_complex_rectangle",
                    "complete","proved","failure","intrinsic_evaluation_complete",
                    "intrinsic_domain_failure","exact_identity_with_original_family_only_on_original_germ_intersection",
                    "auxiliary_continuation_does_not_replace_neighboring_physical_pieces")}
                row["accepted_original_cubic_components"]={
                    k:len(v) for k,v in c.get("polynomial_component_jets",{}).items()}
                evidence=c.get("complete_complex_intrinsic_evidence",{})
                row["complete_intrinsic"]={k:short(evidence.get(k)) for k in (
                    "original_scalar_polynomial_degree_at_most",
                    "exact_bilinear_zero_convolution_without_conjugation",
                    "original_complete_primitive_nodes","full_primitive_tail",
                    "complete_primitive_radial_errors","denominator_gaps",
                    "root_slope_real_lower",
                    "minus_rotational_real_lower","gamma_real_lower")}
                row["complete_intrinsic"]["ordinary_jet_modulus_upper"]={
                    k:[short(v["modulus_upper"]) for v in jets]
                    for k,jets in evidence.get("ordinary_intrinsic_jets",{}).items()}
                budget=c.get("complete_family_budget",{})
                row["complete_family"]={k:short(budget.get(k)) for k in (
                    "complex_divided_curvature_enclosure","complex_root_characteristic_enclosure",
                    "root_characteristic_real_lower","divided_curvature_radial_derivative_bounds")}
                for name in ("complete_mean_ordinary_jets","complete_eta_ordinary_jets"):
                    row["complete_family"][name+"_modulus_upper"]=[short(v["modulus_upper"])
                        for v in budget.get(name,[])]
                row["full_family_norm_summary"]={}
                for width,table in budget.get("strips",{}).items():
                    selected={k:short(table[k]) for k in (
                        "full_drift_angular_bounds","scalar_mean_abs_upper","nonmean_S_bound")}
                    for name in ("U","V"):
                        jets=table["full_family_"+name+"_ordinary_radial_angular_jets"]
                        selected[name+"_angular_orders0to4"]=short(jets[0])
                        if width=="1/32":
                            selected[name+"_ordinary_radial_orders0to3"]=short([v[0] for v in jets])
                    row["full_family_norm_summary"][width]=selected
                cases.append(row)
            state["cases"]=cases
            state["all_full_component_jet_arrays_and_mixed_norms_preserved_in_native"]=True
            state["mathematical_proved"]=doc.get("proved") is True
        state["complete"]=(state["actual_returncode"]==0 and native.is_file() and state.get("mathematical_complete") is True and state.get("mathematical_proved") is True)
        if state["actual_returncode"]:raise SystemExit(state["actual_returncode"])
        if not state["complete"]:raise RuntimeError("the actual auxiliary-domain audit did not prove every requested new domain")
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint();print(json.dumps(state,allow_nan=False),flush=True)
if __name__=="__main__":main()
