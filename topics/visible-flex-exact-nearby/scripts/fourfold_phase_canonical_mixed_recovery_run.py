#!/usr/bin/env python3
"""Fresh-process execution of actual recovered mixed Taylor batches."""
from __future__ import annotations
import argparse,json,os,subprocess,sys
from pathlib import Path


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--batch-cells",type=int,default=4)
    args,rest=ap.parse_known_args()
    if args.batch_cells<1:raise ValueError("positive actual batch required")
    child=Path(__file__).with_name("fourfold_phase_canonical_collar_bivariate_recovery.py")
    env=os.environ.copy()
    env["MALLOC_ARENA_MAX"]="2";env["MALLOC_TRIM_THRESHOLD_"]="0"
    while True:
        result=subprocess.run([sys.executable,"-u",str(child),
            "--batch-cells",str(args.batch_cells),*rest],env=env)
        if result.returncode==0:return
        if result.returncode!=75:raise SystemExit(result.returncode)
        if "--resume" not in rest:rest.append("--resume")
        print(json.dumps({"saved_actual_batch":True,"continuing_exact_prefix":True}),flush=True)


if __name__=="__main__":main()
