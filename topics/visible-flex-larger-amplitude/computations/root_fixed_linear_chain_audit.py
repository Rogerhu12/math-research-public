#!/usr/bin/env python3
"""Compare actual saved physical two-jets on a fixed finite linear-port metric.

This explicitly rejects nonlinear-tail input. It verifies identical physical
data before comparing the real saved quintics, including their interior jet
lobes. Results are finite samples, not a closed-surface or continuum theorem.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import time
from types import SimpleNamespace

HERE=Path(__file__).resolve().parent

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

def read(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)

def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':')).encode()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--checkpoints',type=Path,nargs='+',required=True)
    p.add_argument('--source-topic',type=Path,required=True)
    p.add_argument('--port',type=Path,required=True)
    p.add_argument('--angular',type=int,default=512)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();started=time.monotonic()
    if len(args.checkpoints)<2:raise ValueError('Require at least two successful physical packages')
    data=[read(path) for path in args.checkpoints]
    keys=('frozen_profile','physical_tail_parameters','physical_tail_cut','angular_chart',
          'chart_reference_coefficients','chart_reference_frequencies','gauge_amplitude','meridian_length')
    for rec in data:
        if not rec.get('solver_success') or rec.get('audit_pending',False) or rec['config'].get('actual_nonlinear_tail'):
            raise ValueError('Require an audited successful finite LINEAR-port physical package')
        for key in keys:
            if canonical(rec[key])!=canonical(data[0][key]):raise ValueError('Changed physical datum: '+key)
    pullback=load('root_fixed_linear_pullback',HERE/'geometric-checkpoint-core-pullback.py')
    utility=load('root_fixed_linear_compare',HERE/'geometric-fixed-dual-prefix.py')
    out=dict(scope=__doc__,fixed_data_sha256={k:hashlib.sha256(canonical(data[0][k])).hexdigest() for k in keys},
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        comparison_helper_sha256=hashlib.sha256((HERE/'geometric-fixed-dual-prefix.py').read_bytes()).hexdigest(),
        checkpoints=[],comparisons=[])
    previous=None
    for path,rec in zip(args.checkpoints,data):
        saved,_=pullback.load_saved(path,args.source_topic,args.port,angular=rec['config']['angular'])
        out['checkpoints'].append(dict(file=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
            modes=rec['config']['modes'],angular=rec['config']['angular'],tol=rec['config']['tol'],nodes=len(rec['mesh']),
            coefficient_chunks=rec['pp_coefficient_chunks']))
        if previous is not None:
            row=utility.compare_shape(previous,SimpleNamespace(flow=lambda:saved.flow),saved.sol,args.angular)
            row.update(previous_file=out['checkpoints'][-2]['file'],current_file=str(path));out['comparisons'].append(row)
            print(json.dumps(dict(event='compared',point=row['maximum_material_point_displacement_sample'],jets=row['physical_material_jet_differences_max_sample'])),flush=True)
        previous=saved
        out['seconds']=time.monotonic()-started
        args.out.write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
