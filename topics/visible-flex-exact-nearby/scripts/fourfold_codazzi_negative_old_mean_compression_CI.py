#!/usr/bin/env python3
"""Execute and retain new negative old-mean compression in public Actions."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def short(v):
    if isinstance(v,list):return [short(x) for x in v]
    if isinstance(v,dict):
        if "upper" in v and "ball" in v:return v["upper"]
        if "ball" in v:return v["ball"]
        return {k:short(x) for k,x in v.items()}
    return v
def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("repo","manifest","out-dir","prepared"):p.add_argument("--"+key,type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--resume",type=Path);p.add_argument("--resume-sha")
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("the actual public repository Actions environment is required")
    if sha(a.manifest)!=a.manifest_sha:raise ValueError("the exact reviewed scientific manifest changed")
    manifest=json.loads(a.manifest.read_text())
    if manifest["public_repository"]!=PUBLIC:raise ValueError("wrong public repository")
    repo,output=a.repo.resolve(),a.out_dir.resolve()
    if output.exists() and any(output.iterdir()):raise FileExistsError("preserve every actual outcome")
    output.mkdir(parents=True,exist_ok=True)
    state=dict(kind="actual_public_negative_old_mean_compression_execution",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=a.manifest_sha,complete=False,
        failure=None,actual_returncode=None,
        original_target_coefficient_ray_and_amplitude_solves_recomputed=0,
        first_correction_nonlocal_sources_paid=False,
        complete_strong_norm_CE_Cs_and_cutoff97_not_claimed=True)
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
        state["original_native_receipts"]=[]
        for name in ("exact_fold_native","exact_fold_process","radial_reference_native","original_norm_native"):
            path=repo/manifest["input_paths"][name]
            state["original_native_receipts"].append(dict(name=name,sha256=sha(path),bytes=path.stat().st_size))
        source=repo/TOPIC/"scripts/fourfold_codazzi_negative_old_mean_compression.py"
        native=output/"negative-old-mean-compression.json.gz"
        command=[sys.executable,"-u",str(source),"--repo-root",str(repo),
                 "--manifest",str(a.manifest),"--out",str(native)]
        if a.resume is not None:
            if not a.resume_sha or sha(a.resume)!=a.resume_sha:raise ValueError("the accepted exact prefix changed")
            command+=["--resume",str(a.resume)]
            state["actual_original_prefix_sha256"]=a.resume_sha
            state["actual_original_prefix_bytes"]=a.resume.stat().st_size
        state.update(command=command,mathematical_source_sha256=sha(source));checkpoint()
        started=time.monotonic()
        with (output/"negative-old-mean-compression.stdout.log").open("wb") as stream:
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
            state["mathematical_complete"]=doc.get("complete")
            state["mathematical_proved"]=doc.get("proved")
            state["mathematical_failure"]=doc.get("failure")
            state["mathematical_gates"]=doc.get("gates")
            for key in (
                "runtime","original_exact_fold_native_sha256","original_exact_fold_process_sha256",
                "original_radial_reference_native_sha256","original_completed_norm_native_sha256",
                "exact_real_delta_radius","input_cutoff","physical_frequency","density_input_normalization",
                "source_window","exact_cover","exact_root_interval","fixed_positive_body_cut",
                "positive_cut_receipt_sha256","actual_negative_Cauchy_native_sha256",
                "original_directed_table_sha256","original_completed_norm_rows_reused",
                "original_completed_directed_rows_reused","original_completed_scalar_jet_cases_reused",
                "original_completed_analytic_amplitude_cases_reused","original_completed_Airy_profile_cases_reused",
                "original_target_coefficient_ray_and_amplitude_solves_recomputed",
                "old_completed_moment_rows_recomputed","old_completed_directed_rows_recomputed",
                "old_completed_analytic_amplitude_cases_recomputed","old_completed_Airy_profiles_recomputed",
                "old_completed_scalar_jet_cases_recomputed","original_radial_weights_or_split_integrals_recomputed",
                "original_eight_other_source_terms_recomputed","original_independent_even_mean_rows_recomputed",
                "original_positive_source_rows_recomputed","actual_new_mean_compression_rows",
                "actual_new_negative_integral_rows","source_integral_rows_reused",
                "source_integral_rows_copied_without_new_math","old_mean_and_all_Fourier_outputs_retained",
                "original_global_seam_equations_and_fees_retained","exact_negative_mean_identity_only",
                "first_correction_nonlocal_sources_paid","local_L0_w1_paid",
                "positive_source_to_root_conversion_claimed","complete_strong_return_norm_evaluated",
                "numerical_cutoff97_inverse_claimed","actual_PDE_branch_claimed","last_attempted_source_row"):
                state[key]=doc.get(key)
            state["complete_radius_cases"]=sum(bool(c.get("complete")) for c in doc.get("cases",[]))
            state["cases"]=[]
            keys=("exact_radius","exact_cover","complete","complete_original_rows","new_negative_rows",
                "original_complete_case_payload_sha256","original_positive_rows_and_split_integrals_copied",
                "all_original_scalar_jets_and_amplitude_tensors_copied",
                "negative_complete_ordinary_L2_source","positive_complete_ordinary_L2_source",
                "positive_collar_complete_ordinary_L2_source","positive_body_complete_ordinary_L2_source",
                "negative_leading_nonlocal_and_mean_component_Hminus4over3_to_primitive_L2",
                "actual_negative_source_to_primitive_L2_gain","original_complete_negative_source_bound",
                "original_complete_negative_primitive_bound","separate_first_row_term_L2_source_bounds")
            for case in doc.get("cases",[]):
                summary={k:short(case.get(k)) for k in keys}
                summary["actual_accepted_integral_rows"]=len(case.get("rows",[]))
                summary["accepted_negative_mean_rows"]=sum(
                    bool(row.get("negative",{}).get("exact_old_mean_compression")) for row in case.get("rows",[]))
                state["cases"].append(summary)
            if "original_prefix_audit" in doc:
                state["original_prefix_audit"]={k:doc["original_prefix_audit"].get(k)
                    for k in ("native_sha256","native_bytes","complete","proved","failure")}
            state["all_original_and_new_mean_rows_with_exact_case_identities_preserved_in_native"]=True
        state["complete"]=(state["actual_returncode"]==0 and native.is_file()
            and state.get("mathematical_complete") is True and state.get("mathematical_proved") is True)
        if state["actual_returncode"]:raise SystemExit(state["actual_returncode"])
        if not state["complete"]:raise RuntimeError("new negative old-mean compression did not complete")
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint();print(json.dumps(state,allow_nan=False),flush=True)
if __name__=="__main__":main()
