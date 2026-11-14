#!/usr/bin/env python3
"""Run the complete current first-symbol integral in public Actions.

The full imported mathematical sources and inputs are independently
pinned. The wrapper supplies a frozen scientific checkout; this driver
records its actual commit separately from the workflow event commit.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

PUBLIC = "Rogerhu12/math-research-public"
TOPIC = Path("topics/visible-flex-exact-nearby")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--out-dir",type=Path,required=True)
    args=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("the actual public repository Actions environment is required")
    if sha(args.manifest)!=args.manifest_sha:
        raise ValueError("the complete first-symbol input manifest changed")
    manifest=json.loads(args.manifest.read_text())
    if manifest["public_repository"]!=PUBLIC:
        raise ValueError("wrong scientific repository")
    repo,out=args.repo.resolve(),args.out_dir.resolve()
    if out.exists() and any(out.iterdir()):
        raise FileExistsError("preserve every actual first-symbol process and prefix")
    out.mkdir(parents=True,exist_ok=True)
    state=dict(kind="actual_public_current_first_symbol_finite_part_execution",
        repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=args.manifest_sha,
        complete=False,actual_returncode=None,
        original169_scalar_cache_and_all_candidate_shards_reused=True,
        only_common_root_scalar_jets_are_new=True,
        complete_return_beta_and_full_inverse_not_claimed=True)
    def checkpoint():
        (out/"process.json").write_text(json.dumps(state,indent=2,allow_nan=False)+"\n")
    checkpoint()
    for entry in manifest["files"]:
        path=repo/entry["path"]
        if not path.is_file() or sha(path)!=entry["sha256"]:
            raise ValueError("a pinned original source or native differs: "+entry["path"])
    import numpy, scipy, sympy, mpmath, flint
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),numpy=numpy.__version__,
        scipy=scipy.__version__,sympy=sympy.__version__,mpmath=mpmath.__version__,python_flint=flint.__version__)
    if runtime!=manifest["runtime"]:
        raise ValueError("the required exact arithmetic runtime changed: "+json.dumps(runtime))
    state["runtime"]=runtime;state["verified_inputs"]=len(manifest["files"])
    source=repo/TOPIC/"scripts/fourfold_codazzi_current_first_symbol_finite_part.py"
    paths={k:repo/v for k,v in manifest["input_paths"].items()}
    command=[sys.executable,"-u",str(source),"--topic",str(repo/TOPIC)]
    for key,flag in (("candidate","--candidate"),("scalar_cover","--scalar-cover"),
        ("repair","--repair"),("root_germ","--root-germ"),("object","--object")):
        command += [flag,str(paths[key])]
    for key,flag in (("cut_gap","--cut-gap"),("width_goal","--width-goal"),
        ("max_depth","--max-depth"),("bits","--bits"),
        ("exponential_bits","--exponential-bits"),("root_precision_bits","--root-precision-bits")):
        command += [flag,str(manifest["mathematical_parameters"][key])]
    native,partial=out/"first-symbol-finite-part.json.gz",out/"first-symbol-original-prefix.json.gz"
    command += ["--out",str(native),"--partial",str(partial)]
    state.update(command=command,mathematical_source_sha256=sha(source))
    checkpoint();started=time.monotonic()
    with (out/"first-symbol.stdout.log").open("wb") as stream:
        child=subprocess.run(command,cwd=repo/TOPIC,stdout=stream,stderr=subprocess.STDOUT,
            env=dict(os.environ,OPENBLAS_NUM_THREADS="1",OMP_NUM_THREADS="1",PYTHONDONTWRITEBYTECODE="1"),
            timeout=2700,check=False)
    state.update(actual_returncode=child.returncode,mathematical_wall_seconds=time.monotonic()-started)
    for name,path in (("native",native),("partial",partial)):
        if path.is_file():state[name+"_sha256"]=sha(path)
    state["complete"]=child.returncode==0 and native.is_file()
    checkpoint();print(json.dumps(state,ensure_ascii=False),flush=True)
    if child.returncode:raise SystemExit(child.returncode)
    if not native.is_file():raise RuntimeError("the actual child produced no original mathematical native")


if __name__=="__main__":
    main()
