#!/usr/bin/env python3
"""Find a floating-point joint linear-resonance/cubic-obstruction zero."""
import argparse
import importlib.util
import json
from pathlib import Path
from scipy.optimize import brentq

path=Path(__file__).with_name('78718-geometry-cubic-cap-scan.py')
spec=importlib.util.spec_from_file_location('cap_scan',path)
cap=importlib.util.module_from_spec(spec)
spec.loader.exec_module(cap)

ap=argparse.ArgumentParser()
ap.add_argument('--rtol',type=float,default=1e-10)
ap.add_argument('--bvp-tol',type=float,default=1e-7)
ap.add_argument('--output',type=Path,required=True)
args=ap.parse_args()
trace=[]
cache={}
def evaluate(bump):
    if bump in cache:return cache[bump]
    f=lambda join:cap.first_order(cap.Profile(join,bump),4,args.rtol)[0]
    join=brentq(f,1.8,2.05,xtol=max(1e-12,args.rtol*.1),rtol=1e-13)
    result=cap.cubic(cap.Profile(join,bump),4,args.rtol,args.bvp_tol)
    trace.append(result)
    cache[bump]=result
    print(json.dumps({k:result[k] for k in ['bump','join','cubic_total',
                     'doubled_resonance_residual','second_bvp_nodes']}),flush=True)
    return result
root=brentq(lambda b:evaluate(b)['cubic_total'],-.006,-.005,xtol=1e-11,rtol=1e-12)
result=evaluate(root)
doc=dict(status='floating-point simultaneous zero only; not an exact isometric family',
         result=result,evaluations=trace)
args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(json.dumps(doc,indent=2)+'\n')
print('SAVED',args.output.name,flush=True)
