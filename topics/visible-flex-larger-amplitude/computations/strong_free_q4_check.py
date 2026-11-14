#!/usr/bin/env python3
"""Inspect the actual free-q4 inlet and its derivatives without a BVP solve.

Use --check-output PATH followed by strong_free_q4_bvp.py arguments. The
production adapter is loaded unchanged except for an inspection hook just
before its runner starts. Only warm construction and inlet derivatives run.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import hashlib,json,sys,types
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent

def main():
    i=sys.argv.index('--check-output');out=Path(sys.argv[i+1]);del sys.argv[i:i+2]
    driver=P/'strong_free_q4_bvp.py';source=driver.read_text()
    hashes={name:hashlib.sha256((P/name).read_bytes()).hexdigest() for name in
            ('strong_free_q4_check.py','strong_free_q4_bvp.py','strong_neck_bvp.py','root_dual_core_bvp.py')}
    def install_inspection(runner):
        load=runner.module
        def inspect(fun,bc,x,y,p,**kw):
            obj=fun.__self__;base=obj.initial(p).copy();analytic=obj._initial_jac.copy()
            core=np.asarray(obj._core.coefficients).copy();records=[]
            for index in (2,3):
                steps=[]
                for factor in (1.,.5):
                    h=1e-5*max(1.,abs(p[index]))*factor
                    plus=p.copy();minus=p.copy();plus[index]+=h;minus[index]-=h
                    numeric=(obj.initial(plus).copy()-obj.initial(minus).copy())/(2*h)
                    exact=analytic[:,index]
                    steps.append(dict(step=float(h),max_abs_error=float(np.max(abs(numeric-exact))),
                                      normalized_error=float(np.max(abs(numeric-exact))/max(1.,np.max(abs(exact)))),
                                      analytic_max=float(np.max(abs(exact)))))
                records.append(dict(parameter_index=index,physical_frequency=4 if index==2 else 8,measurements=steps))
            obj.initial(p);np.testing.assert_array_equal(obj._core.coefficients,core)
            recovery={};obj.prepare_recovery_output(recovery)
            result=dict(scope=__doc__,inspection_only=True,nonlinear_solution=False,modes=obj.M,angular=obj.nt,
                        warm_nodes=len(x),reference_coefficients=obj.ref_coeff.tolist(),
                        prescribed_actual_core=dict(q1=obj.q,c6=obj.prescribed_c6),actual_core_coefficients=core.tolist(),
                        free_q4_parameter_value=float(p[2]),free_q4_scale=float(obj.pscale[1]),
                        inlet_warm_residual=float(np.max(abs(y[:,0]-base))),derivative_checks=records,
                        raw_recovery_context=obj.raw_recovery_context,preaudit_output_fields=recovery,
                        source_sha256=hashes,source_transform='Insert inspection loader immediately before runner.main()',
                        memory=runner.memory_record())
            out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
            if not (core[0]==obj.q and core[2]==obj.prescribed_c6 and core[1]==p[2]*obj.pscale[1]):
                raise RuntimeError('Actual prescribed/free inlet layout mismatch')
            if max(z['normalized_error'] for row in records for z in row['measurements'])>=1e-7:
                raise RuntimeError('Free inlet derivative check exceeds tolerance')
            raise RuntimeError('Inlet inspection complete; no nonlinear solve requested')
        def loader(name,path):
            loaded=load(name,path)
            if Path(path).name=='root_dual_core_bvp.py':loaded.solve_bvp=inspect
            return loaded
        runner.module=loader
    old='runner.module=module;runner.main()'
    if source.count(old)!=1:raise ValueError('Production runner entry changed')
    source=source.replace(old,'runner.module=module;_install_inspection(runner);runner.main()')
    module=types.ModuleType('strong_free_inlet_driver');module.__file__=str(driver)
    module.__dict__['_install_inspection']=install_inspection
    exec(compile(source,str(driver),'exec'),module.__dict__);module.main()

if __name__=='__main__':main()
