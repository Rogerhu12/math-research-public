#!/usr/bin/env python3
"""Check the same-chart triple adapter locally, without a nonlinear solve.

Only a small warm mesh, three radial Jacobian points, and inlet derivatives
are used. The diagnostic checks actual prescribed coefficients separately
from the unchanged numerical reference chart and the third physical control.
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
    path=P/'strong_triple_same_chart_bvp.py';source=path.read_text()
    hashes={name:hashlib.sha256((P/name).read_bytes()).hexdigest() for name in
            ('strong_triple_same_chart_bvp.py','strong_triple_same_chart_check.py','root_triple_core_bvp.py','strong_neck_bvp.py','strong_flow_lru.py')}
    def install(runner):
        load=runner.module
        def inspect(fun,bc,x,y,p,**kw):
            obj=fun.__self__;obj.initial(p);core=obj._core.coefficients.copy();f=obj.flow(p[0])
            np.testing.assert_array_equal(f.general_core_chart.coefficients,obj.ref_coeff)
            np.testing.assert_array_equal(f.general_core_chart.frequencies,[2,4])
            indices=np.unique(np.round(np.linspace(0,len(x)-1,5)[1:-1]).astype(int))
            t=x[indices];state=y[:,indices];J,PJ=kw['fun_jac'](t,state,p)
            controls=[]
            for j,name in enumerate(obj.control_names):
                rows=[]
                for factor in (1.,.5):
                    h=3e-6*max(.1,abs(obj.cfg[name]+p[j]))*factor
                    plus=p.copy();minus=p.copy();plus[j]+=h;minus[j]-=h
                    numeric=(fun(t,state,plus)-fun(t,state,minus))/(2*h)
                    error=float(np.max(abs(numeric-PJ[:,j])))
                    rows.append(dict(step=h,max_abs_error=error,normalized_error=error/max(1.,np.max(abs(PJ[:,j])))))
                controls.append(dict(parameter_index=j,physical_control=name,measurements=rows))
            obj.initial(p);analytic=obj._initial_jac[:,3].copy();rows=[]
            for factor in (1.,.5):
                h=1e-5*max(1.,abs(p[3]))*factor
                plus=p.copy();minus=p.copy();plus[3]+=h;minus[3]-=h
                numeric=(obj.initial(plus).copy()-obj.initial(minus).copy())/(2*h)
                rows.append(dict(step=h,max_abs_error=float(np.max(abs(numeric-analytic)))))
            obj.initial(p);record={};obj.prepare_recovery_output(record)
            result=dict(scope=__doc__,inspection_only=True,nonlinear_solution=False,modes=obj.M,angular=obj.nt,warm_nodes=len(x),
                reference_coefficients=obj.ref_coeff.tolist(),reference_frequencies=obj.ref_frequencies,
                actual_prescribed_coefficients=obj.prescribed.tolist(),actual_core_coefficients=core.tolist(),
                inlet_warm_residual=float(np.max(abs(y[:,0]-obj.initial(p)))),control_parameter_checks=controls,
                first_free_core_derivative=dict(parameter_index=3,physical_frequency=8,measurements=rows),
                raw_recovery_context=obj.raw_recovery_context,preaudit_output_fields=record,
                source_sha256=hashes,memory=runner.memory_record())
            out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
            np.testing.assert_array_equal(core[:3],obj.prescribed)
            if max(v['normalized_error'] for row in controls for v in row['measurements'])>2e-6:
                raise RuntimeError('Three physical derivative diagnostic exceeds tolerance')
            if max(row['max_abs_error'] for row in rows)>1e-7:raise RuntimeError('Free core inlet derivative mismatch')
            raise RuntimeError('Same-chart triple inspection complete; no nonlinear solve requested')
        def module(name,path):
            loaded=load(name,path)
            if Path(path).name=='root_dual_core_bvp.py':loaded.solve_bvp=inspect
            return loaded
        runner.module=module
    old='runner.module=module;runner.main()'
    if source.count(old)!=1:raise ValueError('Production entry changed')
    source=source.replace(old,'runner.module=module;_install_inspection(runner);runner.main()')
    module=types.ModuleType('strong_local_triple_check');module.__file__=str(path)
    module.__dict__['_install_inspection']=install
    exec(compile(source,str(path),'exec'),module.__dict__);module.main()

if __name__=='__main__':main()
