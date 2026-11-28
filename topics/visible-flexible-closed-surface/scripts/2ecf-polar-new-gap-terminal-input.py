#!/usr/bin/env python3
"""Exact endpoint submaster from a genuine 65-node physical source and its exact ellipse mean."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    a=argparse.ArgumentParser()
    for k in ('scripts','ramp','master-report','prefix'):a.add_argument('--'+k,type=Path,required=True)
    arg=a.parse_args()
    meta=json.loads(arg.master_report.read_text())
    if sha(arg.ramp)!=meta['rampSHA256'] or meta['returnedDenseNodes']!=65:raise ValueError('Verified physical H65 required')
    root=arg.scripts/'6a65-geometry-central-gap-held-budget.py'
    sp=importlib.util.spec_from_file_location('gap_ellipse_bounds',root);budget=importlib.util.module_from_spec(sp);sp.loader.exec_module(budget)
    with np.load(arg.ramp) as v:keys={k:v[k].copy() for k in v.files}
    path=Path(str(arg.prefix)+'-endpoint-submaster.npz')
    with path.open('xb') as f:np.savez_compressed(f,**dict(keys,sx=keys['sx'][::4],coefficients=keys['coefficients'][::4]))
    A,B=[Q(float(keys[k])) for k in ('centralA','centralB')]
    low,high=budget.perimeter_over_pi(A,B,terms=32)
    info=dict(source=dict(masterSHA256=sha(path),physicalMasterSHA256=sha(arg.ramp),physicalReportSHA256=sha(arg.master_report),
              producerSHA256=sha(__file__),ellipseBudgetSHA256=sha(root)),exactEllipticArcRadiusInterval=[str(low/2),str(high/2)],
              useOfSubmaster='Only native traces at indices 0 and 16 needed; these are original H65 indices 0 and 64 exactly.')
    with Path(str(arg.prefix)+'-endpoint-input.json').open('x') as f:json.dump(info,f,indent=2);f.write('\n')
    print(json.dumps(info),flush=True)
if __name__=='__main__':main()
