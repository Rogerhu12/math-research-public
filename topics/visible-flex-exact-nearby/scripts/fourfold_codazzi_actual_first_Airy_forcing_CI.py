#!/usr/bin/env python3
"""Run only the new complete real-piecewise root consumer in public Actions."""
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
    if sha(a.manifest)!=a.manifest_sha:raise ValueError("the exact first-forcing manifest changed")
    manifest=json.loads(a.manifest.read_text())
    if manifest["public_repository"]!=PUBLIC:raise ValueError("wrong public scientific repository")
    repo,output=a.repo.resolve(),a.out_dir.resolve()
    if output.exists() and any(output.iterdir()):
        raise FileExistsError("preserve every actual first-forcing result and failed prefix")
    output.mkdir(parents=True,exist_ok=True)
    state=dict(kind="actual_public_actual_first_Airy_forcing_execution",complete=False,failure=None,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=a.manifest_sha,
        original_target_root_rows_candidate_or_response_solves_recomputed=0,
        complete_strong_norm_CE_Cs_and_cutoff97_not_claimed=True,actual_returncode=None)
    def checkpoint():
        raw=json.dumps(state,indent=2,allow_nan=False)+"\n"
        if len(raw.encode())>60000:
            raise ValueError("the actual human-readable summary must remain at most60000 bytes")
        (output/"process.json").write_text(raw)
    checkpoint()
    try:
        for entry in manifest["files"]:
            path=repo/entry["path"]
            if not path.is_file() or sha(path)!=entry["sha256"] or path.stat().st_size!=entry["bytes"]:
                raise ValueError("a full original input or exact source changed: "+entry["path"])
        state["verified_input_files"]=len(manifest["files"])
        source=repo/TOPIC/"scripts/fourfold_codazzi_actual_first_Airy_forcing.py"
        native=output/"actual-first-Airy-forcing.json.gz"
        command=[sys.executable,"-u",str(source),"--repo-root",str(repo),
                 "--manifest",str(a.manifest),"--prepared",str(a.prepared),"--out",str(native)]
        if a.resume is not None:
            if not a.resume_sha or sha(a.resume)!=a.resume_sha:
                raise ValueError("the actual original first-forcing prefix bytes changed")
            command+=["--resume",str(a.resume)]
            state["actual_original_prefix_sha256"]=a.resume_sha
            state["actual_original_prefix_bytes"]=a.resume.stat().st_size
        state.update(command=command,mathematical_source_sha256=sha(source));checkpoint()
        started=time.monotonic()
        try:
            with (output/"actual-first-Airy-forcing.stdout.log").open("wb") as stream:
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
            state["complete_original_native_reused"]=bool(a.resume is not None and sha(native)==a.resume_sha)
            state["actual_new_closed_rows_in_this_child"]=0 if state["complete_original_native_reused"] else doc.get("new_closed_rows")
            state["mathematical_complete"]=doc.get("complete") is True
            state["mathematical_failure"]=doc.get("failure")
            state["mathematical_gates"]=doc.get("gates",[])
            for key in ("actual_forcing","global_coefficient_and_inverse_bounds",
                "exact_cover","exact_root_interval","accepted_closed_rows",
                "original_complete_root_rows","original_complete_seams","original_selected_intrinsic_rows",
                "root_native_sha256","original_root_native_bytes","original_root_native_public_run_id",
                "original_part_receipts","full_original_193_direction_and_even_mean_retained",
                "exact_real_delta_radius","original_closed_rows_reused","new_closed_rows",
                "original_completed_prefix_sha256","original_completed_prefix_run_id",
                "prefix_global_accepted_rows","explicit_historical_prefix_reused",
                "last_attempted_common_cell","last_accepted_common_cell","complete_strong_return_norm_evaluated",
                "numerical_cutoff97_return_inverse_claimed","actual_PDE_branch_claimed"):
                state[key]=doc.get(key)
            if doc.get("rows"):
                state["actual_completed_prefix_interval"]=[
                    doc["rows"][0]["interval"][0],doc["rows"][-1]["interval"][1]]
        state["complete"]=(state["actual_returncode"]==0 and native.is_file()
                           and state.get("mathematical_complete") is True)
        if state["actual_returncode"]:raise SystemExit(state["actual_returncode"])
        if not state["complete"]:raise RuntimeError("the true first-forcing gates did not complete")
    except BaseException as error:
        state["failure"]={"type":type(error).__name__,"message":str(error)};raise
    finally:
        checkpoint()
        print(json.dumps(state,ensure_ascii=False,allow_nan=False),flush=True)
if __name__=="__main__":main()
