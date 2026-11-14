#!/usr/bin/env python3
"""Run the complete first-Airy seam consumer on two completed public natives."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--out-dir",type=Path,required=True)
    p.add_argument("--prepared",type=Path,required=True)
    p.add_argument("--resume",type=Path)
    p.add_argument("--resume-sha")
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("this computation requires the actual public repository Actions")
    if sha(a.manifest)!=a.manifest_sha:raise ValueError("the exact seam manifest changed")
    manifest=json.loads(a.manifest.read_text())
    if manifest["public_repository"]!=PUBLIC:raise ValueError("wrong public scientific repository")
    repo,output=a.repo.resolve(),a.out_dir.resolve()
    if output.exists() and any(output.iterdir()):
        raise FileExistsError("preserve every actual seam result and failed prefix")
    output.mkdir(parents=True,exist_ok=True)
    state=dict(kind="actual_public_first_Airy_seam_operators_execution",complete=False,failure=None,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=a.manifest_sha,
        original_target_coefficient_ray_and_amplitude_solves_recomputed=0,
        complete_strong_norm_CE_Cs_and_cutoff97_not_claimed=True,actual_returncode=None)
    def checkpoint():
        raw=json.dumps(state,indent=2,allow_nan=False)+"\n"
        if len(raw.encode())>60000:
            raise ValueError("the complete human-readable process must remain at most60000 bytes")
        (output/"process.json").write_text(raw)
    checkpoint()
    try:
        for entry in manifest["files"]:
            path=repo/entry["path"]
            if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                raise ValueError("an actual original receipt or exact source changed: "+entry["path"])
        state["verified_input_files"]=len(manifest["files"])
        originals={}
        for spec in manifest["external_completed_natives"]:
            path=a.prepared/spec["prepared_path"]
            if not path.is_file() or sha(path)!=spec["sha256"] or path.stat().st_size!=spec["bytes"]:
                raise ValueError("a completed original native differs: "+spec["name"])
            originals[spec["name"]]=path
        state["original_native_receipts"]=[
            dict(name=spec["name"],run_id=spec["run_id"],sha256=sha(originals[spec["name"]]),
                 bytes=originals[spec["name"]].stat().st_size)
            for spec in manifest["external_completed_natives"]]
        source=repo/TOPIC/"scripts/fourfold_codazzi_actual_first_Airy_seam_operators.py"
        native=output/"actual-first-Airy-seam-operators.json.gz"
        command=[sys.executable,"-u",str(source),"--repo-root",str(repo),
            "--manifest",str(a.manifest),"--root-native",str(originals["root"]),
            "--forcing-native",str(originals["forcing"]),"--out",str(native)]
        if a.resume is not None:
            if not a.resume_sha or sha(a.resume)!=a.resume_sha:
                raise ValueError("the exact original seam prefix bytes changed")
            command+=["--resume",str(a.resume)]
            state["actual_original_prefix_sha256"]=a.resume_sha
            state["actual_original_prefix_bytes"]=a.resume.stat().st_size
        state.update(command=command,mathematical_source_sha256=sha(source));checkpoint()
        started=time.monotonic()
        try:
            with (output/"actual-first-Airy-seam-operators.stdout.log").open("wb") as stream:
                result=subprocess.run(command,cwd=repo/TOPIC,stdout=stream,stderr=subprocess.STDOUT,
                    timeout=2700,check=False,env=dict(os.environ,OPENBLAS_NUM_THREADS="1",
                    OMP_NUM_THREADS="1",PYTHONDONTWRITEBYTECODE="1"))
            state["actual_returncode"]=result.returncode
        except subprocess.TimeoutExpired:
            state["actual_returncode"]=124;state["timeout_seconds"]=2700
        finally:
            state["mathematical_wall_seconds"]=time.monotonic()-started
        if native.is_file():
            state["native_sha256"]=sha(native);state["native_bytes"]=native.stat().st_size
            doc=json.loads(gzip.decompress(native.read_bytes()))
            state["mathematical_complete"]=doc.get("complete") is True
            state["mathematical_failure"]=doc.get("failure")
            state["mathematical_gates"]=doc.get("gates",[])
            state["complete_actual_seams"]=len(doc.get("seams",[]))
            for key in ("exact_cover","exact_root_interval","exact_real_delta_radius","input_cutoff",
                "physical_frequency","source_window","density_input_normalization",
                "root_native_sha256","first_forcing_native_sha256","first_forcing_process_sha256",
                "actual_negative_Cauchy_native_sha256","completed_seams_reused","new_seams_evaluated",
                "last_attempted_seam","negative_seam_count","positive_seam_count",
                "complete_unpropagated_seam_operator_sums","actual_negative_first_seam_contributions",
                "negative_first_seam_component_has_complete_strong_4over3_window",
                "old_mean_full_output_and_head_rows_retained",
                "positive_weighted_affine_port_conversion_claimed",
                "complete_strong_return_norm_evaluated","numerical_cutoff97_inverse_claimed",
                "actual_PDE_branch_claimed"):
                state[key]=doc.get(key)
            state["refined_forcing_radius_cases"]=[]
            keep=("coefficient_strip","leading_strip","forcing_strip","output_strip","bound_type",
                "complete_actual_L0_v0_pair_sup","complete_actual_L0_v0_pair_first_angular_sup",
                "actual_first_a_amplitude_sup","actual_first_b_amplitude_sup",
                "actual_original_mean_first_derivative_jump_sum",
                "actual_a_first_derivative_jump_sum","A_second_radial_seam_fee",
                "A_second_radial_first_angular_seam_fee",
                "actual_minimum_seam_root_distance","common_next_root_trace",
                "full_branch_factors_retained")
            for case in doc.get("refined_forcing_radius_cases",[]):
                state["refined_forcing_radius_cases"].append(dict(
                    exact_radius=case["exact_radius"],exact_cover=case["exact_cover"],
                    complete_original_forcing_rows=case["complete_original_forcing_rows"],
                    complete_original_seams=case["complete_original_seams"],passed=case["passed"],
                    actual_forcing={k:case["actual_forcing"].get(k) for k in keep}))
            if doc.get("seams"):
                state["actual_completed_seam_prefix"]=[
                    doc["seams"][0]["radial"],doc["seams"][-1]["radial"]]
        state["complete"]=(state["actual_returncode"]==0 and native.is_file()
                           and state.get("mathematical_complete") is True)
        if state["actual_returncode"]:raise SystemExit(state["actual_returncode"])
        if not state["complete"]:raise RuntimeError("the complete actual seam gates did not finish")
    except BaseException as error:
        state["failure"]={"type":type(error).__name__,"message":str(error)};raise
    finally:
        checkpoint()
        print(json.dumps(state,ensure_ascii=False,allow_nan=False),flush=True)
if __name__=="__main__":main()
