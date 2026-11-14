#!/usr/bin/env python3
"""Run and preserve only the new complete quadratic first-phase arithmetic."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo","manifest","out-dir"):p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--manifest-sha",required=True);a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("run only in the actual public repository Actions")
    if sha(a.manifest)!=a.manifest_sha:raise ValueError("the fixed complete arithmetic manifest changed")
    m=json.loads(a.manifest.read_text());repo=a.repo.resolve();out=a.out_dir.resolve()
    if m["public_repository"]!=PUBLIC:raise ValueError("another repository")
    if out.exists() and any(out.iterdir()):raise FileExistsError("preserve every original outcome")
    out.mkdir(parents=True,exist_ok=True)
    state=dict(kind="actual_public_complete_quadratic_first_phase_arithmetic_execution",
        complete=False,repository=PUBLIC,run_id=os.environ["GITHUB_RUN_ID"],
        run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=a.manifest_sha,
        verified_input_files=0,actual_returncode=None,failure=None,
        original_scalar_phase_finite_part_and_root_recomputed=False,
        actual_full_return_beta_identification_proved=False)
    def save():(out/"process.json").write_text(json.dumps(state,indent=2,allow_nan=False)+"\n")
    save()
    try:
        for entry in m["files"]:
            path=(repo/entry["path"]).resolve()
            if not path.is_relative_to(repo) or not path.is_file() or path.stat().st_size!=entry["bytes"] or sha(path)!=entry["sha256"]:
                raise ValueError("a fixed input changed: "+entry["path"])
            state["verified_input_files"]+=1
        source=repo/TOPIC/"scripts/fourfold_codazzi_first_symbol_quadratic_gap.py"
        native=out/"first-symbol-quadratic-gap.json.gz"
        command=[sys.executable,"-u",str(source),"--topic",str(repo/TOPIC),
            "--coefficient",str(repo/m["input_paths"]["coefficient"]),"--out",str(native)]
        state.update(command=command,mathematical_source_sha256=sha(source));save()
        start=time.monotonic()
        try:
            with (out/"first-symbol-quadratic-gap.stdout.log").open("wb") as stream:
                child=subprocess.run(command,cwd=repo/TOPIC,stdout=stream,stderr=subprocess.STDOUT,
                    timeout=1800,check=False,env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1"))
            state["actual_returncode"]=child.returncode
        except subprocess.TimeoutExpired:
            state["actual_returncode"]=124;state["timeout_seconds"]=1800
        state["mathematical_wall_seconds"]=time.monotonic()-start
        if native.is_file():
            n=json.loads(gzip.decompress(native.read_bytes()))
            state.update(native_sha256=sha(native),mathematical_complete=n.get("complete"),
                mathematical_gates=n.get("gates"),mathematical_failure=n.get("failure"))
            for key in ("coefficient_interval","phase_coefficient_interval","exact_integer_polynomial",
                "limiting_norm_interval","actual_limiting_integer_distance_lower",
                "closest_limiting_integer","complete_finite_candidates","candidate_counts_by_fourth_root",
                "complete_finite_distance_times_abs_n_lower","worst_finite_candidate",
                "complete_common_distance_times_abs_n_lower",
                "exact_uniform_complex_gap_times_abs_n_lower","exact_scalar_inverse_one_derivative_constant",
                "unseparated_candidate"):
                if key in n:state[key]=n[key]
        state["complete"]=state["actual_returncode"]==0 and state.get("mathematical_complete") is True
        save();print(json.dumps(state,ensure_ascii=False),flush=True)
        if not state["complete"]:raise SystemExit(state["actual_returncode"] or 1)
    except Exception as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error));save();raise
if __name__=="__main__":main()
