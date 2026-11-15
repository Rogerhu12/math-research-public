#!/usr/bin/env python3
"""Run the complete inner first-correction source consumer and preserve its receipt."""
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
    for k in ("repo","manifest","out-dir","prepared"):p.add_argument("--"+k,type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--resume",type=Path);p.add_argument("--resume-sha")
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("the actual public repository Actions environment is required")
    if sha(a.manifest)!=a.manifest_sha:raise ValueError("the declared complete input manifest changed")
    manifest=json.loads(a.manifest.read_text())
    if manifest["public_repository"]!=PUBLIC:raise ValueError("wrong public repository")
    repo,output=a.repo.resolve(),a.out_dir.resolve()
    if output.exists() and any(output.iterdir()):raise FileExistsError("preserve every actual outcome")
    output.mkdir(parents=True,exist_ok=True)
    state=dict(kind="actual_public_complete_inner_first_Airy_sources_execution",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=a.manifest_sha,complete=False,
        failure=None,actual_returncode=None,original_target_or_matrix_or_Taylor_recomputation=False,
        full_strong_return_or_cutoff97_inverse_claimed=False)
    def checkpoint():
        raw=json.dumps(state,indent=2,allow_nan=False)+"\n"
        if len(raw.encode())>=60000:raise ValueError("complete readable process exceeds60000 bytes")
        temp=output/"process.json.partial";temp.write_text(raw);temp.replace(output/"process.json")
    checkpoint()
    try:
        for f in manifest["files"]:
            path=repo/f["path"]
            if not path.is_file() or sha(path)!=f["sha256"] or path.stat().st_size!=f["bytes"]:
                raise ValueError("an exact original input changed: "+f["path"])
        state["verified_input_files"]=len(manifest["files"])
        state["complete_original_native_receipts"]=[
            dict(name=k,sha256=sha(repo/manifest["input_paths"][k]),
                 bytes=(repo/manifest["input_paths"][k]).stat().st_size)
            for k in ("Taylor_native","Taylor_process","auxiliary_native","auxiliary_process",
                      "exact_fold_native","radial_reference_native","original_norm_native")]
        source=repo/TOPIC/"scripts/fourfold_codazzi_inner_first_Airy_complete_sources.py"
        native=output/"inner-first-Airy-complete-sources.json.gz"
        command=[sys.executable,"-u",str(source),"--repo-root",str(repo),
                 "--manifest",str(a.manifest),"--out",str(native)]
        if a.resume is not None:
            if not a.resume_sha or sha(a.resume)!=a.resume_sha:raise ValueError("an accepted exact prefix changed")
            command+=["--resume",str(a.resume)]
            state["original_prefix_native_sha256"]=a.resume_sha
        state.update(command=command,mathematical_source_sha256=sha(source));checkpoint()
        started=time.monotonic()
        with (output/"inner-first-Airy-complete-sources.stdout.log").open("wb") as stream:
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
            keys=("runtime","original_Taylor_native_sha256","original_Taylor_process_sha256",
                "original_auxiliary_native_sha256","original_exact_fold_native_sha256",
                "original_exact_fold_process_sha256","original_radial_reference_native_sha256",
                "original_completed_norm_native_sha256","exact_real_delta_radius","fixed_intrinsic_parameter",
                "input_cutoff","physical_frequency","actual_first_correction_density","source_window",
                "exact_root_interval","exact_physical_inner_interval","exact_physical_rho_cover",
                "exact_original_physical_piece_interval","original_directed_table_sha256",
                "old_target_FFT_coefficient_flow_fold_and_Taylor_stages_recomputed","old_complete_matrix_words_recomputed",
                "new_stages","reused_stages","new_same_order_matrix_conversions","reused_same_order_matrix_conversions",
                "new_source_integral_rows","reused_source_integral_rows","complete_inner_integral_rows",
                "complete_same_order_converted_rows","all_fourier_outputs_and_old_means_retained",
                "exact_same_complex_parameter_opposite_branch_retained",
                "fixed_inner_interval_introduces_no_artificial_source","original_physical_seams_retained",
                "local_numerator_is_mu_L0_w1","old_density_T_alternative_claimed",
                "leading_nonlocal_contribution_is_separate","positive_raw_source_only",
                "positive_weighted_port_conversion_claimed","complete_strong_return_or_cutoff97_inverse_claimed",
                "actual_PDE_branch_claimed","complete_Airy_source_bounds","complete_inner_source_totals",
                "original_prefix_audit","last_attempted_source_row")
            for k in keys:
                if k in doc:state[k]=short(doc[k])
            state["accepted_stage_payloads"]={k:dict(complete=v["complete"],payload_sha256=v["payload_sha256"])
                for k,v in doc.get("stages",{}).items()}
            stage=doc.get("stages",{}).get("new-inner-Airy-profile-and-exact-PQ-jets")
            if stage:state["complete_inverse_phase_Fourier_tail_evidence"]=short(stage["payload"]["complete_fourier_evidence"])
            state["actual_accepted_rows"]=len(doc.get("rows",[]))
            state["all_complete_original_word_choices_and_new_integrals_preserved_in_native"]=True
        state["complete"]=(state["actual_returncode"]==0 and native.is_file()
            and state.get("mathematical_complete") is True and state.get("mathematical_proved") is True)
        if state["actual_returncode"]:raise SystemExit(state["actual_returncode"])
        if not state["complete"]:raise RuntimeError("complete inner source consumer did not complete")
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint();print(json.dumps(state,allow_nan=False),flush=True)
if __name__=="__main__":main()
