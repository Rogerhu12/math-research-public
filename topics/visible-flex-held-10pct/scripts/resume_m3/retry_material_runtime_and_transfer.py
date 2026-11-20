#!/usr/bin/env python3
"""Retry two observed startup failures without removing any numerical guard.

The native retry has an empty dynamic-loader override environment and first
checks that the same Python/NumPy/SciPy runtime works in that environment.
The M12 transfer uses the original engine's required angular quadrature.
Previous failed outputs are retained in their original directories.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--workdir",type=Path,required=True)
    args=parser.parse_args()
    repo,work=args.repo.resolve(),args.workdir.resolve()
    scripts=repo/"topics/visible-flex-held-10pct/scripts/resume_m3"
    summary=work/"material-runtime-retry-status.json"
    if summary.exists():
        raise FileExistsError("Keep the previous runtime retry")
    clean=dict(os.environ)
    removed={name:bool(clean.pop(name,None)) for name in ("LD_PRELOAD","LD_LIBRARY_PATH")}
    for name in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
        clean[name]="1"
    check=subprocess.run([sys.executable,"-c",
        "import json,numpy,scipy;print(json.dumps(dict(numpy=numpy.__version__,scipy=scipy.__version__)))"],
        env=clean,capture_output=True,text=True,check=False)
    state=dict(status="runtime_checked",stages=[],complete_surface=False,
        diagnostics=dict(loader_override_presence_before=removed,
            loader_overrides_present_after=False,native_guard_unchanged=True,
            clean_python_returncode=check.returncode,
            clean_python_stdout=check.stdout[-1000:],clean_python_stderr=check.stderr[-2000:]))
    def save():
        summary.write_text(json.dumps(state,indent=2)+"\n")
    save()
    if check.returncode:
        state["status"]="clean_python_runtime_failed";save();return 2
    retry=work/"material-runtime-retry01"
    retry.mkdir(exist_ok=False)
    shutil.copyfile(work/"bootstrap.json",retry/"bootstrap.json")
    shutil.copytree(work/"inputs",retry/"inputs")
    jobs=[
        ("true_dn_clean_loader",[sys.executable,"-u",scripts/"correct_projected_material_seed.py",
            "--repo",repo,"--workdir",retry,"--prefix-dir",work/"material-lam002-linear",
            "--core-config",scripts/"material_support_lam002.json","--workers","2"]),
        ("m12_valid_quadrature",[sys.executable,"-u",scripts/"prepare_lifted_mode_restart.py",
            "--source-run",work/"material-lam002-linear/run.json","--modes","12",
            "--tail-config",work/"inputs/q060-tail.json",
            "--outdir",work/"material-lam002-m12-transfer-v2"]),
    ]
    def run(name,command):
        log=work/("material-runtime-retry-"+name+".log")
        with log.open("x") as stream:
            result=subprocess.run(list(map(str,command)),cwd=repo,env=clean,
                                  stdout=stream,stderr=subprocess.STDOUT,check=False)
        return result.returncode,log
    state["stages"]=[dict(name=name,status="running",returncode=None,
                           argv=list(map(str,command))) for name,command in jobs]
    state["status"]="running";save()
    with ThreadPoolExecutor(max_workers=2) as pool:
        pending={pool.submit(run,name,command):name for name,command in jobs}
        for future in as_completed(pending):
            name=pending[future]
            code,log=future.result()
            row=next(row for row in state["stages"] if row["name"]==name)
            row.update(status="finished",returncode=code)
            if code:
                lines=log.read_text(errors="replace").splitlines()
                row["error_lines"]=[line[:900] for line in lines if
                    any(token in line for token in ("Error","Traceback","failed"))][-15:]
            stderr=retry/"corrector-actual-00/tail_worker_stderr.log"
            if name=="true_dn_clean_loader" and stderr.exists():
                state["diagnostics"]["native_stderr_last_lines"]=[
                    line[:800] for line in stderr.read_text(errors="replace").splitlines()[-18:]]
            save()
    state["status"]="finished";save()
    return 0 if all(row["returncode"]==0 for row in state["stages"]) else 2


if __name__=="__main__":
    sys.exit(main())
