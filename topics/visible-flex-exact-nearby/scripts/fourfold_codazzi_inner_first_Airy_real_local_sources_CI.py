#!/usr/bin/env python3
"""Execute only new complete real-angular inner-local source arithmetic."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def short(value):
    if isinstance(value,list):return [short(x) for x in value]
    if isinstance(value,dict):
        if "ball" in value:return value["ball"]
        return {k:short(v) for k,v in value.items()}
    return value
def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ("repo","manifest","out-dir","prepared"):p.add_argument("--"+k,type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--resume",type=Path);p.add_argument("--resume-sha")
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("the authorized public Actions environment is required")
    if sha(a.manifest)!=a.manifest_sha:raise ValueError("the complete new manifest changed")
    m=json.loads(a.manifest.read_text())
    if m["public_repository"]!=PUBLIC:raise ValueError("wrong public repository")
    repo,out=a.repo.resolve(),a.out_dir.resolve()
    if out.exists() and any(out.iterdir()):raise FileExistsError("preserve every actual outcome")
    out.mkdir(parents=True,exist_ok=True)
    state=dict(kind="actual_public_inner_first_Airy_real_local_source_execution",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=a.manifest_sha,complete=False,failure=None,
        actual_returncode=None,old_successful_mathematics_recomputed=False,
        full_strong_return_or_cutoff97_inverse_claimed=False)
    def checkpoint():
        text=json.dumps(state,indent=2,allow_nan=False)+"\n"
        if len(text.encode())>=60000:raise ValueError("complete readable process exceeds60000 bytes")
        t=out/"process.json.partial";t.write_text(text);t.replace(out/"process.json")
    checkpoint()
    try:
        for f in m["files"]:
            path=repo/f["path"]
            if not path.is_file() or sha(path)!=f["sha256"] or path.stat().st_size!=f["bytes"]:
                raise ValueError("an exact original input changed: "+f["path"])
        state["verified_input_files"]=len(m["files"])
        source=repo/TOPIC/"scripts/fourfold_codazzi_inner_first_Airy_real_local_sources.py"
        native=out/"inner-first-Airy-real-local-sources.json.gz"
        command=[sys.executable,"-u",str(source),"--repo-root",str(repo),"--manifest",str(a.manifest),
                 "--out",str(native)]
        if a.resume is not None:
            if not a.resume_sha or sha(a.resume)!=a.resume_sha:raise ValueError("the exact new prefix changed")
            command+=["--resume",str(a.resume)]
            state["original_prefix_native_sha256"]=a.resume_sha
        state.update(command=command,mathematical_source_sha256=sha(source));checkpoint()
        started=time.monotonic()
        with (out/"inner-first-Airy-real-local-sources.stdout.log").open("wb") as stream:
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
            for new,old in (("mathematical_complete","complete"),("mathematical_proved","proved"),
                            ("mathematical_failure","failure"),("mathematical_gates","gates")):
                state[new]=doc.get(old)
            keys=("runtime","original_inner_native_sha256","original_inner_process_sha256",
                "original_Taylor_native_sha256","original_Taylor_process_sha256","original_auxiliary_native_sha256",
                "original_inner_mathematical_source_sha256","original_inner_manifest_sha256",
                "original_complete_stage_payloads","original_complete_matrix_conversions_payload_sha256",
                "original_complete_rows_payload_sha256","exact_real_delta_radius","fixed_intrinsic_parameter",
                "input_cutoff","physical_frequency","actual_first_correction_density","source_window",
                "exact_root_interval","exact_physical_inner_interval","exact_physical_rho_cover",
                "exact_original_physical_piece_interval","new_stages","reused_stages",
                "new_changed_local_integral_rows","reused_changed_local_integral_rows",
                "old_target_FFT_Taylor_profile_matrix_nonlocal_or_mean_recomputations",
                "original_physical_seams_retained","fixed_inner_interval_introduces_no_artificial_source",
                "positive_raw_source_only","positive_weighted_port_conversion_claimed",
                "complete_strong_return_or_cutoff97_inverse_claimed","actual_PDE_branch_claimed",
                "complete_real_raw_local_jets","complete_local_Airy_bounds","complete_inner_source_totals",
                "original_prefix_audit")
            for k in keys:
                if k in doc:state[k]=short(doc[k])
            state["accepted_new_stage_payloads"]={k:dict(complete=v["complete"],payload_sha256=v["payload_sha256"])
                for k,v in doc.get("stages",{}).items()}
            state["actual_accepted_rows"]=len(doc.get("rows",[]))
            state["all_complete_products_profiles_and_source_rows_retained_in_native"]=True
        state["complete"]=(state["actual_returncode"]==0 and native.is_file()
            and state.get("mathematical_complete") is True and state.get("mathematical_proved") is True)
        if state["actual_returncode"]:raise SystemExit(state["actual_returncode"])
        if not state["complete"]:raise RuntimeError("the real local source consumer did not complete")
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint();print(json.dumps(state,allow_nan=False),flush=True)
if __name__=="__main__":main()
