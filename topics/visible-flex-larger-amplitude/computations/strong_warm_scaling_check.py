#!/usr/bin/env python3
"""Compare full and radial-batched affine warm scaling on a small real warm.

Pass --check-output PATH and strong_neck_bvp.py arguments. Only warm
construction and this local formula comparison run; there is no BVP solve.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import hashlib,importlib.util,json,sys
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent

def main():
    i=sys.argv.index('--check-output');out=Path(sys.argv[i+1]);del sys.argv[i:i+2]
    hashes={n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in
            ('strong_warm_scaling_check.py','strong_neck_bvp.py','root_dual_core_bvp.py')}
    spec=importlib.util.spec_from_file_location('strong_warm_check_runner',P/'strong_neck_bvp.py')
    runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner);load=runner.module
    def inspect(fun,bc,x,y,p,**kw):
        obj=fun.__self__;obj.select(p);f=obj.flow(p[0]);s,_=obj.chart(x,p[0])
        N=max(512,32*(2*obj.M+1));B,_,_=f.basis(N);ratio=.09/.085
        def extra(ss):
            g=f.geo(ss,N);th=g['theta'];er=np.stack((np.cos(th),np.sin(th),np.zeros_like(th)),axis=-1)
            background=f.profile(ss)[0][:,None,None]*er
            return (ratio-1)*f.project(g['pos']-background,B)/obj.q
        full=ratio*y+extra(s);batched=y.copy()
        for first in range(0,len(s),24):
            sl=slice(first,first+24);batched[:,sl]=ratio*batched[:,sl]+extra(s[sl])
        error=float(np.max(abs(full-batched)))
        result=dict(scope=__doc__,inspection_only=True,nonlinear_solution=False,modes=obj.M,
                    requested_q=obj.q,angular_for_warm=N,warm_nodes=len(x),comparison_ratio=ratio,
                    full_vs_batched_array_equal=bool(np.array_equal(full,batched)),max_abs_error=error,
                    source_sha256=hashes,memory=runner.memory_record())
        out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
        if error>2e-13:raise RuntimeError('Warm batch formula comparison differs unexpectedly')
        raise RuntimeError('Warm scaling inspection complete; no nonlinear solve requested')
    def module(name,path):
        loaded=load(name,path)
        if Path(path).name=='root_dual_core_bvp.py':loaded.solve_bvp=inspect
        return loaded
    runner.module=module;runner.main()

if __name__=='__main__':main()
