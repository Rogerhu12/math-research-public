#!/usr/bin/env python3
"""Time and compare the two Jacobian assemblies on an actual saved curve.

No BVP, true DN, or curve evolution is run. Only scalar errors and timings
are saved. This assesses a numerical Jacobian backend, not surface accuracy.
"""
import os
for task_key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[task_key]='1'
import argparse
import importlib.util
import json
import hashlib
from pathlib import Path
import time
import numpy as np

HERE=Path(__file__).resolve().parent
TOPIC=HERE.parent

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec);spec.loader.exec_module(value)
    return value

def ident(path):
    path=Path(path).resolve();data=path.read_bytes()
    return dict(path=str(path),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())

def lift(y,old,new):
    result=np.zeros((3*new+1,y.shape[1]));result[0]=y[0]
    for k in range(3):result[k*new+1:k*new+old+1]=y[k*old+1:(k+1)*old+1]
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.out.exists():raise ValueError('Use a fresh report')
    loader=module('fourier_jac_loader',HERE/'db6f-prefix-flat-geometry-source.py')
    fast=module('fourier_jac_backend',HERE/'78718-prefix-fourier-jacobian.py')
    rec,obj,unused,sol=loader.source(args.checkpoint,
        TOPIC/'notes/2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json',TOPIC/'repro/source-root')
    positions=np.linspace(0,unused.end,32)
    source=sol.sol(positions)
    rows=[]
    for M,N in [(15,512),(22,1024)]:
        if M<obj.M:continue
        flow=obj.Flow(obj.cfg,obj.port,M,obj.q,N,obj.base_mode,obj.bridge)
        y=lift(source,obj.M,M)
        begin=time.perf_counter();old,old_p=flow.fun_jac(positions,y,np.zeros(M));old_seconds=time.perf_counter()-begin
        begin=time.perf_counter();tables=fast.build_tables(flow);flow._fourier_jacobian_tables=tables;build_seconds=time.perf_counter()-begin
        begin=time.perf_counter();new,new_p=fast.adapt_fun_jac(flow,positions,y,np.zeros(M));new_seconds=time.perf_counter()-begin
        difference=new-old
        matrix_max=float(np.max(np.abs(old)))
        row=dict(M=M,N=N,radial_points=len(positions),
            original_seconds=old_seconds,table_build_seconds=build_seconds,new_seconds=new_seconds,
            speedup_excluding_one_time_tables=old_seconds/new_seconds,
            maximum_original_entry=matrix_max,
            maximum_absolute_entry_difference=float(np.max(np.abs(difference))),
            relative_maximum_entry_difference=float(np.max(np.abs(difference))/matrix_max),
            relative_frobenius_difference=float(np.linalg.norm(difference.ravel())/np.linalg.norm(old.ravel())),
            parameter_derivatives_equal=bool(np.array_equal(old_p,new_p)),
            projected_imaginary_roundoff_max=tables['imaginary_max'],
            first_assembly_nonzeros=int(tables['first'].nnz),second_assembly_nonzeros=int(tables['second'].nnz))
        # One centred directional difference checks the unchanged actual RHS.
        rng=np.random.default_rng(78718+M)
        direction=rng.normal(size=y.shape)/(1+np.arange(flow.n))[:,None]
        delta=1e-6
        observed=(flow.fun(positions,y+delta*direction,np.zeros(M))-flow.fun(positions,y-delta*direction,np.zeros(M)))/(2*delta)
        expected=np.einsum('ijk,jk->ik',new,direction)
        row['centred_RHS_direction_difference_relative']=float(np.linalg.norm(observed-expected)/np.linalg.norm(expected))
        rows.append(row)
    report=dict(scope=__doc__,script=ident(__file__),backend=ident(HERE/'78718-prefix-fourier-jacobian.py'),
        checkpoint=ident(args.checkpoint),source_modes=obj.M,
        saved_curve_was_successful=rec.get('solver_success') is True,diagnostics=rows,
        BVP_calls=0,DN_calls=0,new_surface_created=False)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=ident(args.out),diagnostics=rows,BVP_calls=0,DN_calls=0)))

if __name__=='__main__':main()
