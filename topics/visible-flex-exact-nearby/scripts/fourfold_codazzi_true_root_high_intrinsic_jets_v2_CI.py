#!/usr/bin/env python3
"""Resume the complete original high-root point with an exact Nyquist consumption view."""
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
        raise RuntimeError("the actual public repository Actions environment is required")
    if sha(a.manifest)!=a.manifest_sha:raise ValueError("the exact reviewed scientific manifest changed")
    manifest=json.loads(a.manifest.read_text())
    if manifest["public_repository"]!=PUBLIC:raise ValueError("wrong public repository")
    repo,output=a.repo.resolve(),a.out_dir.resolve()
    if output.exists() and any(output.iterdir()):raise FileExistsError("preserve every actual outcome")
    output.mkdir(parents=True,exist_ok=True)
    state=dict(kind="actual_public_true_root_high_intrinsic_jets_exact_Nyquist_v2_execution",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=a.manifest_sha,
        complete=False,failure=None,actual_returncode=None,
        original_completed_auxiliary_domains_recomputed=0,
        original_infinite_tail_evaluations_recomputed=0,
        first_correction_root_Taylor_coefficients_paid=False,
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
        source=repo/TOPIC/"scripts/fourfold_codazzi_true_root_high_intrinsic_jets_v2.py"
        native=output/"true-root-high-intrinsic-jets-v2.json.gz"
        command=[sys.executable,"-u",str(source),"--repo-root",str(repo),
                 "--manifest",str(a.manifest),"--out",str(native)]
        if a.resume is not None:
            if not a.resume_sha or sha(a.resume)!=a.resume_sha:raise ValueError("the accepted exact prefix changed")
            command+=["--resume",str(a.resume)]
            state["actual_original_prefix_sha256"]=a.resume_sha
            state["actual_original_prefix_bytes"]=a.resume.stat().st_size
        state.update(command=command,mathematical_source_sha256=sha(source))
        checkpoint();started=time.monotonic()
        with (output/"true-root-high-intrinsic-jets-v2.stdout.log").open("wb") as stream:
            child=subprocess.Popen(command,cwd=repo,stdout=stream,stderr=subprocess.STDOUT)
            try:
                child.wait(timeout=2700)
            except subprocess.TimeoutExpired:
                state["actual_timeout_seconds"]=2700
                child.terminate()
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
                "runtime","object_sha256","root_germ_sha256","auxiliary_native_sha256","auxiliary_process_sha256",
                "actual_intrinsic_parameter","other_intrinsic_parameters_given_the_same_true_root",
                "complete_intrinsic_delta_independence_only_on_original_bump_zero_germ",
                "exact_root_interval","original_scalar_germ","exact_original_physical_piece_interval",
                "exact_fixed_intrinsic_parameter","original_parameter_half_width_used_for_outward_enclosure",
                "consumed_complete_auxiliary_radii","original_auxiliary_failed_cases_preserved",
                "original_auxiliary_process_returncode",
                "original_completed_auxiliary_domains_recomputed","original_infinite_tail_evaluations_recomputed",
                "original_65_or_193_cubic_domains_recomputed",
                "new_true_root_finite_evaluations","reused_true_root_finite_evaluations",
                "new_complete_error_orders","reused_complete_error_orders","new_mean_products","reused_mean_products",
                "new_energy_orders","reused_energy_orders","new_intrinsic_series_stages","reused_intrinsic_series_stages",
                "finite_primitive_derivative_count","energy_derivative_count","ordinary_intrinsic_derivative_count",
                "all_original_physical_seams_and_independent_means_retained",
                "first_correction_root_Taylor_coefficients_paid",
                "old_circle_I_J_or_independent_even_mean_on_first_correction_paid",
                "full_strong_return_or_cutoff97_inverse_claimed"):
                state[key]=doc.get(key)
            def small(value):
                if isinstance(value,list):return [small(x) for x in value]
                if isinstance(value,dict):
                    if "ball" in value:return value["ball"]
                    return {k:small(v) for k,v in value.items()}
                return value
            point=doc.get("finite_root_stage",{})
            state["strict_original_source_migration"]=small(doc.get("strict_original_source_migration"))
            state["original_finite_point_payload_sha256"]=doc.get("original_finite_point_payload_sha256")
            state["exact_Nyquist_consumption"]=small(doc.get("exact_Nyquist_consumption"))
            state["finite_point_stage"]={k:point.get(k) for k in (
                "complete","exact_evaluation_interval","original_scalar_germ","nodes","modes",
                "ordinary_radial_derivatives_not_factorial_normalized",
                "original_infinite_tail_evaluator_called","original_auxiliary_domain_evaluator_called")}
            state["complete_primitive_error_orders"]=[dict(order=row["order"],
                chosen_candidate=row["selected_candidate_index"],
                candidate_count=len(row["complete_candidates"]),upper=small(row["complete_error_upper"]))
                for row in doc.get("complete_errors",[])]
            state["finite_component_Wiener_bounds"]=[dict(order=row["order"],value=small(row["value"]))
                for row in doc.get("finite_component_norms",[])]
            state["physical_radius_ordinary_jets"]=small(doc.get("physical_radius_ordinary_jets"))
            state["energy_ordinary_jets"]=small(doc.get("energy_jets"))
            state["accepted_complete_mean_products"]=len(doc.get("mean_products",{}))
            state["denominator_gaps"]=small(doc.get("denominator_gaps"))
            state["intrinsic_stage"]=small(doc.get("intrinsic_stage"))
            state["at_the_certified_true_root"]=small(doc.get("at_the_certified_true_root"))
            state["original_low_order_identity_checks"]=doc.get("original_low_order_identity_checks")
            state["full_finite_arrays_all_error_candidates_and_accepted_means_preserved_in_native"]=True
            if "original_prefix_audit" in doc:
                old=doc["original_prefix_audit"]
                state["original_prefix_audit"]={k:old.get(k) for k in (
                    "native_sha256","native_bytes","run_id","complete","proved","failure")}
        state["complete"]=(state["actual_returncode"]==0 and native.is_file()
            and state.get("mathematical_complete") is True and state.get("mathematical_proved") is True)
        if state["actual_returncode"]:raise SystemExit(state["actual_returncode"])
        if not state["complete"]:raise RuntimeError("new true-root high intrinsic jets did not complete")
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint();print(json.dumps(state,allow_nan=False),flush=True)
if __name__=="__main__":main()
