#!/usr/bin/env python3
"""Compare unchanged serial and isolated-thread RHS at an actual saved field."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,gzip,hashlib,importlib.util,json,resource,sys,time,types
from pathlib import Path
import numpy as np
import root_radial_batching as original
import root_20261114_radial_threads as parallel
from strong_frontload_anchor_loader_adapter import build
HERE=Path(__file__).resolve().parent

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj;spec.loader.exec_module(obj);return obj

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for n in ('input','source-topic','port','out'):p.add_argument('--'+n,type=Path,required=True)
    p.add_argument('--batch',type=int,default=24);p.add_argument('--workers',type=int,default=4)
    p.add_argument('--angular',type=int,default=None,
                   help='Explicit diagnostic override; default is the saved production config.angular.')
    a=p.parse_args()
    if a.out.exists():raise FileExistsError(a.out)
    ns,provenance=build('audit',HERE/'strong_anchor_interior_fullmean_audit.py')
    obs=dict(provider_loads=0,saved_fields=[])
    pb=ns['install_audit_loader'](module,obs)('thread_actual_saved_loader',HERE/'geometric-checkpoint-core-pullback.py')
    opener=gzip.open if a.input.suffix=='.gz' else open
    with opener(a.input,'rt') as source_file:source_record=json.load(source_file)
    source_angular=int(source_record['config']['angular'])
    requested_angular=source_angular if a.angular is None else a.angular
    saved,loader=pb.load_saved(a.input,a.source_topic,a.port,angular=requested_angular)
    f=saved.flow;s=saved.sol.x;y=saved.sol.y;params=saved.sol.p
    # Include the already-built Fourier derivative table carried by actual
    # post-J response flows; the adapter must copy this state correctly too.
    jac=loader.source_module('thread_original_fourier_jacobian',a.source_topic/'scripts/78718-prefix-fourier-jacobian.py')
    f.fun_jac=types.MethodType(jac.adapt_fun_jac,f)
    f.fun_jac(s[:a.batch],y[:,:a.batch],params)
    begin=time.perf_counter();expected=original.value(f,s,y,params,a.batch);serial_seconds=time.perf_counter()-begin
    before=f.calls;parallel.configure(a.workers)
    begin=time.perf_counter();actual=parallel.value(f,s,y,params,a.batch);parallel_seconds=time.perf_counter()-begin
    parallel.close()
    same=bool(np.array_equal(expected,actual));difference=float(np.max(abs(expected-actual)))
    count=(len(s)+a.batch-1)//a.batch;calls=f.calls-before
    if not same or calls!=count:raise AssertionError((difference,calls,count))
    result=dict(input=str(a.input),input_sha256=hashlib.sha256(a.input.read_bytes()).hexdigest(),
        source_sha256={Path(v).name:hashlib.sha256(Path(v).read_bytes()).hexdigest() for v in
        (__file__,original.__file__,parallel.__file__)},modes=f.M,angular=f.nt,physical_nodes=len(s),
        source_config_angular=source_angular,requested_angular=requested_angular,
        production_angular_retained=(requested_angular==source_angular and f.nt==source_angular),
        state_dimension=len(y),output_values=int(actual.size),batch=a.batch,workers=a.workers,
        original_profile=obs,loader_provenance=provenance,serial_seconds=serial_seconds,
        parallel_seconds=parallel_seconds,speedup=serial_seconds/parallel_seconds,
        bitwise_equal=same,max_abs_difference=difference,callback_calls=calls,
        expected_callback_calls=count,parallel_stats=parallel.STATS,
        populated_Fourier_jacobian_table_retained=True,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        fixed_state_RHS_comparison=True,new_nonlinear_solution=False)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('bitwise_equal','output_values','serial_seconds','parallel_seconds','speedup','peak_rss_kib')}),flush=True)

if __name__=='__main__':main()
