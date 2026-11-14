#!/usr/bin/env python3
"""Execute the complete complex inner-root forcing budget from exact old inputs."""
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
    state=dict(kind="actual_public_complex_inner_root_first_Airy_forcing_execution",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=a.manifest_sha,
        complete=False,failure=None,actual_returncode=None,
        original_target_fold_ray_and_leading_amplitude_solves_recomputed=0,
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
        source=repo/TOPIC/"scripts/fourfold_codazzi_complex_inner_root_first_Airy_forcing.py"
        native=output/"complex-inner-root-first-Airy-forcing.json.gz"
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
            with (output/"complex-inner-root-first-Airy-forcing.stdout.log").open("wb") as stream:
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
                "exact_complex_parameter_radius","actual_intrinsic_parameter","root_germ_sha256",
                "root_budget_native_sha256","original_fold_native_sha256","original_leading_native_sha256",
                "original_target_fold_ray_and_leading_amplitude_solves_recomputed",
                "original_completed_zeroth_order_coefficient_values_recomputed",
                "new_original_cubic_derivative_components","reused_original_cubic_derivative_components",
                "new_coefficient_budget_cases","new_forcing_cases","reused_forcing_cases",
                "all65_base_and193_direction_components_retained","independent_even_mean_retained",
                "independent_even_mean_operator_budget_paid","complete_old_circle_remainder_on_w1_paid",
                "real_only_intrinsic_jets_used_for_complex_derivatives",
                "artificial_root_interface_or_background_analytic_extension_inserted",
                "complete_full_frequency_strong_return_norm_paid",
                "numerical_cutoff97_inverse_or_true_PDE_branch_claimed","exact_root_interval",
                "exact_original_complex_radial_rectangle","exact_original_root_piece_interval",
                "constant_background_and_direction_repairs_have_zero_piece_derivative",
                "complete_old_product_leading_constants_reused","complete_coefficient_budget",
                "complete_coefficient_budget_numeric"):
                state[key]=doc.get(key)
            state["accepted_derivative_components"]={
                name:len(rows) for name,rows in doc.get("polynomial_derivatives",{}).items()}
            state["cases"]=doc.get("cases",[])
            state["complete_forcing_cases"]=sum(bool(c.get("complete")) for c in state["cases"])
        state["complete"]=(state["actual_returncode"]==0 and native.is_file() and state.get("mathematical_complete") is True)
        if state["actual_returncode"]:raise SystemExit(state["actual_returncode"])
        if not state["complete"]:raise RuntimeError("the actual complete inner forcing budget did not finish")
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint();print(json.dumps(state,allow_nan=False),flush=True)
if __name__=="__main__":main()
