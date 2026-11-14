#!/usr/bin/env python3
"""Execute the directed matrix norm refinement on completed original rows."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo","manifest","out-dir","prepared"):p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--resume",type=Path);p.add_argument("--resume-sha")
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("the actual public repository Actions is required")
    if sha(a.manifest)!=a.manifest_sha:raise ValueError("the exact old-circle manifest changed")
    manifest=json.loads(a.manifest.read_text())
    if manifest["public_repository"]!=PUBLIC:raise ValueError("wrong scientific repository")
    repo,output=a.repo.resolve(),a.out_dir.resolve()
    if output.exists() and any(output.iterdir()):raise FileExistsError("preserve all real outcomes")
    output.mkdir(parents=True,exist_ok=True)
    state=dict(kind="actual_public_directed_matrix_old_circle_sources_execution",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=a.manifest_sha,
        complete=False,failure=None,actual_returncode=None,
        original_target_coefficient_ray_and_amplitude_solves_recomputed=0,
        complete_strong_norm_CE_Cs_and_cutoff97_not_claimed=True)
    def checkpoint():
        raw=json.dumps(state,indent=2,allow_nan=False)+"\n"
        if len(raw.encode())>60000:raise ValueError("the complete readable process exceeds60000 bytes")
        (output/"process.json").write_text(raw)
    checkpoint()
    try:
        for entry in manifest["files"]:
            path=repo/entry["path"]
            if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                raise ValueError("a complete fixed original input changed: "+entry["path"])
        state["verified_input_files"]=len(manifest["files"])
        originals={}
        for spec in manifest["external_completed_natives"]:
            path=a.prepared/spec["prepared_path"]
            if not path.is_file() or sha(path)!=spec["sha256"] or path.stat().st_size!=spec["bytes"]:
                raise ValueError("an original completed artifact differs: "+spec["name"])
            originals[spec["name"]]=path
        seam=repo/manifest["input_paths"]["first_seam_native"]
        old_native=repo/manifest["input_paths"]["original_norm_native"]
        state["original_native_receipts"]=[
            dict(name=spec["name"],run_id=spec["run_id"],sha256=sha(originals[spec["name"]]),
                 bytes=originals[spec["name"]].stat().st_size)
            for spec in manifest["external_completed_natives"]]
        state["original_native_receipts"].append(dict(name="first_seams",run_id="43625828234",
            sha256=sha(seam),bytes=seam.stat().st_size))
        state["original_native_receipts"].append(dict(name="original_complete_moment_norms",run_id="43629465215",
            sha256=sha(old_native),bytes=old_native.stat().st_size))
        source=repo/TOPIC/"scripts/fourfold_codazzi_directed_matrix_old_circle_sources.py"
        native=output/"directed-matrix-old-circle-sources.json.gz"
        command=[sys.executable,"-u",str(source),"--repo-root",str(repo),
            "--manifest",str(a.manifest),"--root-native",str(originals["root"]),
            "--forcing-native",str(originals["forcing"]),"--seam-native",str(seam),
            "--old-native",str(old_native),"--out",str(native)]
        if a.resume is not None:
            if not a.resume_sha or sha(a.resume)!=a.resume_sha:raise ValueError("the exact saved prefix changed")
            command+=["--resume",str(a.resume)]
            state["actual_original_prefix_sha256"]=a.resume_sha
            state["actual_original_prefix_bytes"]=a.resume.stat().st_size
        state.update(command=command,mathematical_source_sha256=sha(source));checkpoint()
        started=time.monotonic()
        try:
            with (output/"directed-matrix-old-circle-sources.stdout.log").open("wb") as stream:
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
            state["complete_coefficient_norm_rows"]=len(doc.get("coefficient_rows",[]))
            state["complete_radius_cases"]=sum(bool(c.get("complete")) for c in doc.get("cases",[]))
            for key in ("exact_cover","exact_root_interval","exact_real_delta_radius","input_cutoff",
                "physical_frequency","source_window","density_input_normalization",
                "root_native_sha256","first_forcing_native_sha256","first_seam_native_sha256",
                "actual_negative_Cauchy_native_sha256","fixed_positive_body_cut","positive_cut_receipt_sha256",
                "coefficient_rows_reused","new_coefficient_norm_rows",
                "original_completed_norm_native_sha256","original_completed_norm_rows_reused",
                "old_completed_moment_rows_recomputed",
                "last_attempted_coefficient_row","last_attempted_source_row",
                "old_mean_and_all_Fourier_outputs_retained","higher_radial_intrinsic_jets_invented_or_recomputed",
                "local_L0_w1_paid","positive_source_to_root_conversion_claimed",
                "complete_strong_return_norm_evaluated","numerical_cutoff97_inverse_claimed",
                "actual_PDE_branch_claimed"):
                state[key]=doc.get(key)
            state["cases"]=[]
            keys=("exact_radius","exact_cover","complete","complete_original_rows","original_norm_rows_reused",
                "constant_matrix_derivative_evidence","complete_case_operator_cost_maxima",
                "complete_original_matrix_widths","original_complete_source_bounds_not_overwritten",
                "separate_first_row_term_L2_source_bounds","negative_complete_ordinary_L2_source",
                "positive_complete_ordinary_L2_source","positive_collar_complete_ordinary_L2_source",
                "positive_body_complete_ordinary_L2_source",
                "positive_split_retains_independent_mean_and_is_not_a_full_low_high_inverse",
                "actual_negative_source_to_primitive_L2_gain",
                "negative_leading_nonlocal_and_mean_component_Hminus4over3_to_primitive_L2",
                "positive_source_to_root_conversion_claimed")
            for case in doc.get("cases",[]):
                summary={k:case.get(k) for k in keys}
                summary["actual_accepted_integral_rows"]=len(case.get("rows",[]))
                state["cases"].append(summary)
        state["complete"]=(state["actual_returncode"]==0 and native.is_file()
                           and state.get("mathematical_complete") is True)
        if state["actual_returncode"]:raise SystemExit(state["actual_returncode"])
        if not state["complete"]:raise RuntimeError("the actual old-circle source budget did not complete")
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint();print(json.dumps(state,allow_nan=False),flush=True)
if __name__=="__main__":main()
