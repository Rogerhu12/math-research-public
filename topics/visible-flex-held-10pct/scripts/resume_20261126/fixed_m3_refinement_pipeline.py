#!/usr/bin/env python3
"""Three finite fixed-g solves with honest gates and same-chart C2 diagnostics.

This pipeline stops at its first rejected solve, missing return, or failed
comparison. Successful completion means the declared finite calculations
returned and passed their finite gates. Three stages, including only one
change of M, never prove a C2 limit or any closed-surface completion goal.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--source-run", type=Path, required=True)
    parser.add_argument("--port32", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    parser.add_argument("--q-branch", type=float, nargs=2, default=[.055, .065])
    parser.add_argument("--max-nodes", type=int, default=6000)
    parser.add_argument("--jac-batch", type=int, default=8)
    parser.add_argument("--compare-angular", type=int, nargs="+", default=[512, 1024, 2048])
    args = parser.parse_args()
    initial = json.loads(args.source_run.read_text())
    if initial.get("modes") != 24 or not initial.get("solver_success") or not initial.get("physical_sha256"):
        raise ValueError("Start from an actual converged M24 return and its physical C2 export")
    if not args.port32.is_file():
        raise ValueError("Provide the original metric's M32 port")
    if args.max_nodes < 1 or args.jac_batch < 1:
        raise ValueError("Positive original solve budget and Jacobian batch required")
    args.outdir.mkdir(parents=True, exist_ok=False)
    start = time.monotonic()
    installed = args.repo.resolve()/"topics/visible-flex-held-10pct/scripts/resume_20261126"
    driver = installed/"fixed_m3_branch_refinement.py"
    compare = installed/"fixed_m3_compare_c2.py"
    definitions = [
        dict(name="m24-fixed",modes=24,angular=768,refine=1,
             tol=1e-6,bc_tol=1e-7,physical_bc_tol=2e-9,audit=[512,1024]),
        dict(name="m24-refined",modes=24,angular=1536,refine=2,
             tol=1e-8,bc_tol=1e-9,physical_bc_tol=2e-11,audit=[1024,2048]),
        dict(name="m32-refined",modes=32,angular=2048,refine=1,
             tol=1e-9,bc_tol=1e-10,physical_bc_tol=2e-12,audit=[1024,2048]),
    ]
    record = dict(scope=__doc__,command=[sys.executable,*sys.argv],status="initialized",
        source_run=str(args.source_run.resolve()),source_run_sha256=sha(args.source_run),
        port32=str(args.port32.resolve()),port32_sha256=sha(args.port32),
        source_hashes={p.name:sha(p) for p in (Path(__file__),driver,compare,installed/"fixed_m3_branch_model.py")},
        definitions=definitions,mean_nodes=1168,q_branch=args.q_branch,
        original_bc_normalization=.02,stages=[],comparisons=[],
        complete_surface=False,C2_convergence_proven=False,
        one_modal_increment_only=True,continuous_time_family_provided=False)

    def save():
        record["elapsed"] = time.monotonic()-start
        (args.outdir/"pipeline.json").write_text(json.dumps(record,indent=2,allow_nan=False)+"\n")
        summary=dict(status=record["status"],stages=record["stages"],
            progress=dict(accepted_stages=sum(bool(s.get("accepted")) for s in record["stages"]),
                expected_stages=3,comparisons_evaluated=sum(c.get("status")=="evaluated" for c in record["comparisons"]),
                elapsed=record["elapsed"]),
            result=dict(last_run=record.get("last_run"),comparisons=record["comparisons"],
                all_finite_stages_passed=record["status"]=="three_finite_stages_evaluated",
                C2_convergence_proven=False,one_modal_increment_only=True,complete_surface=False),
            error=record.get("error"),scope=__doc__)
        (args.outdir/"summary.json").write_text(json.dumps(summary,indent=2,allow_nan=False)+"\n")

    def event(kind,**fields):
        row=dict(event=kind,elapsed=time.monotonic()-start,**fields)
        with (args.outdir/"events.jsonl").open("a") as stream:
            stream.write(json.dumps(row,allow_nan=False)+"\n")
        print(json.dumps(row,allow_nan=False),flush=True)

    environment=dict(os.environ,OPENBLAS_NUM_THREADS="1",OMP_NUM_THREADS="1",MKL_NUM_THREADS="1")
    current=args.source_run.resolve()
    fixed_runs=[]
    save()
    for index,definition in enumerate(definitions):
        output=args.outdir/definition["name"]
        command=[sys.executable,"-u",str(driver),"--source-run",str(current),
            "--outdir",str(output),"--modes",str(definition["modes"]),
            "--angular",str(definition["angular"]),"--refine",str(definition["refine"]),
            "--mean-nodes","1168","--q-branch",*[str(q) for q in args.q_branch],
            "--bc-normalization","0.02",
            "--jac-batch",str(args.jac_batch),"--max-nodes",str(args.max_nodes),
            "--tol",str(definition["tol"]),"--bc-tol",str(definition["bc_tol"]),
            "--physical-bc-tol",str(definition["physical_bc_tol"]),
            "--audit-angular",*[str(n) for n in definition["audit"]]]
        if definition["modes"]==32:
            command += ["--port",str(args.port32.resolve())]
        stage=dict(definition=definition,command=command,status="running",accepted=False)
        record["stages"].append(stage);record["status"]="running";save()
        event("stage_start",index=index,name=definition["name"])
        with (args.outdir/(definition["name"]+".log")).open("w") as stream:
            result=subprocess.run(command,stdout=stream,stderr=subprocess.STDOUT,env=environment)
        stage["returncode"]=result.returncode
        returned=output/"run.json"
        candidate=None
        if returned.is_file():
            candidate=json.loads(returned.read_text())
            stage.update(run=str(returned.resolve()),run_sha256=sha(returned),
                solver_success=bool(candidate.get("solver_success")),
                finite_linear_candidate_pass=bool(candidate.get("finite_linear_candidate_pass")),
                status=candidate.get("status"),actual_q=candidate.get("actual_q"),
                physical_bc=candidate.get("linear_dn_physical_bc_max"),
                raw_return=candidate.get("raw_return"),error=candidate.get("error"))
            stage["accepted"]=bool(result.returncode==0 and candidate.get("solver_success") and
                candidate.get("finite_linear_candidate_pass") and candidate.get("physical_sha256"))
        if not stage["accepted"]:
            record["status"]="stopped_on_rejected_stage"
            record["error"]=stage.get("error") or "Stage did not return an actual solver/finite-metric/physical-BC accepted field"
            save()
            event("stage_rejected",index=index,name=definition["name"],returncode=result.returncode,
                  actual_status=stage.get("status"),error=stage.get("error"))
            return 2
        current=returned.resolve();fixed_runs.append(current)
        event("stage_accepted",index=index,name=definition["name"],run=str(current))
        save()
        if index:
            comparison_path=args.outdir/(definitions[index-1]["name"]+"-to-"+definition["name"]+"-c2.json")
            comparison_command=[sys.executable,"-u",str(compare),"--first-run",str(fixed_runs[-2]),
                "--second-run",str(fixed_runs[-1]),"--out",str(comparison_path),
                "--mean-nodes","1168","--angular",*[str(n) for n in args.compare_angular]]
            item=dict(command=comparison_command,status="running",
                refinement_kind="same-M numerical refinement" if index==1 else "first modal increment")
            record["comparisons"].append(item);save()
            with comparison_path.with_suffix(".log").open("w") as stream:
                comparison_return=subprocess.run(comparison_command,stdout=stream,
                    stderr=subprocess.STDOUT,env=environment)
            item["returncode"]=comparison_return.returncode
            if comparison_return.returncode or not comparison_path.is_file():
                item["status"]="error";record["status"]="stopped_on_comparison_error"
                record["error"]="C2 comparison did not return an evaluated diagnostic"
                save()
                event("comparison_error",index=index,returncode=comparison_return.returncode)
                return 3
            comparison=json.loads(comparison_path.read_text())
            item.update(status="evaluated",file=str(comparison_path.resolve()),sha256=sha(comparison_path),
                finite_candidate_pass=comparison["finite_candidate_pass"],
                core_literal_coefficient_distances=comparison["core_literal_coefficient_distances"],
                rows=comparison["rows"],
                observed_height_quadrature_change=comparison["observed_height_quadrature_change"],
                continuous_C2_bound_certified=False,same_limit_core_proven=False)
            event("comparison_evaluated",index=index,file=str(comparison_path.resolve()))
            save()
    record["status"]="three_finite_stages_evaluated"
    record["last_run"]=str(current)
    save()
    event("finite_pipeline_return",last_run=str(current),C2_convergence_proven=False)
    return 0


if __name__=="__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        if "--outdir" in sys.argv:
            directory=Path(sys.argv[sys.argv.index("--outdir")+1])
            directory.mkdir(parents=True,exist_ok=True)
            destination=directory/"summary.json"
            if not destination.exists():
                destination.write_text(json.dumps(dict(status="error",stages=[],progress={},
                    result=dict(C2_convergence_proven=False,complete_surface=False),error=repr(exc)),indent=2)+"\n")
        raise
