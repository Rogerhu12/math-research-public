#!/usr/bin/env python3
"""Exercise the real bounded/fixed/actual loader without a tail or BVP.

Uses the successful physical warm trajectory. A synthetic affine tail map
is used only to verify the fixed-g terminal parameter derivative. No actual
nonlinear D-N result is produced by this inspection.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
import root_actual_bounded_neck as bounded


def main():
    i=sys.argv.index('--check-output');out=Path(sys.argv[i+1]);del sys.argv[i:i+2]
    original=bounded.adapter.module;counts=dict(inspections=0,tail_start_attempts=0)

    def guard(self):
        counts['tail_start_attempts']+=1
        raise AssertionError('Tail worker is forbidden in this inspection')

    def inspect(self,fun,bc,x,y,p,**kw):
        counts['inspections']+=1
        assert self.fixed and self.tail is None
        flow=self.flow();cfg=json.dumps(flow.cfg,sort_keys=True)
        indices=np.unique(np.linspace(1,len(x)-2,3).astype(int));t=x[indices];state=y[:,indices]
        f0=fun(t,state,p)
        # This local diagnostic uses only a supplied linear map; the
        # production actual tail boundary method is not modified on disk.
        matrix=np.diag(np.linspace(1.,2.,self.M))
        self.tail_boundary=lambda value:(matrix@self.tail_height(value),matrix)
        A,B,P=self.bc_jac(y[:,0],y[:,-1],p)
        checks=[]
        for j in sorted(set([0,1,2,self.M-1])):
            h=2e-6*max(1.,abs(p[j]));plus=p.copy();minus=p.copy();plus[j]+=h;minus[j]-=h
            fp=fun(t,state,plus);fm=fun(t,state,minus)
            estimate=(bc(y[:,0],y[:,-1],plus)-bc(y[:,0],y[:,-1],minus))/(2*h)
            denominator=max(1.,float(np.max(abs(P[:,j]))))
            error=float(np.max(abs(estimate-P[:,j])))/denominator
            assert np.array_equal(f0,fp) and np.array_equal(f0,fm)
            assert self.flow() is flow and json.dumps(flow.cfg,sort_keys=True)==cfg
            assert error<2e-7,(j,error)
            assert np.array_equal(P[self.n:,j],np.zeros(self.M))
            checks.append(dict(column=j,normalized_boundary_derivative_error=error,
                               interior_rhs_bitwise_parameter_independent=True,
                               actual_same_flow_object=True,terminal_parameter_column_exactly_zero=True))
        self.select(p);assert counts['tail_start_attempts']==0
        record=dict(scope=__doc__,fixed_metric=True,nonlinear_BVP_run=False,tail_worker_started=False,
            warm_nodes=len(x),modes=self.M,angular=self.nt,checks=checks,
            fixed_metric_provenance=self.fixed_metric_provenance,actual_context=self.raw_recovery_context,
            counts=counts,memory=bounded.adapter.memory_record(),
            script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
        out.write_text(json.dumps(record,indent=2)+'\n')
        print(json.dumps(dict(event='actual_fixed_loader_inspection_passed',checks=checks,memory=record['memory'])),flush=True)
        raise RuntimeError('Fixed actual loader inspection complete; no BVP or worker requested')

    def module(name,path):
        loaded=original(name,path)
        if Path(path).name=='root_dual_core_bvp.py':
            source_main=loaded.main
            def entry():
                factory=loaded.make_dual
                def instrument(*args,**kwargs):
                    cls=factory(*args,**kwargs);cls.ensure_tail=guard;cls.solve_coupled=inspect;return cls
                loaded.make_dual=instrument
                return source_main()
            loaded.main=entry
        return loaded

    bounded.adapter.module=module;bounded.main()
    if counts!={'inspections':1,'tail_start_attempts':0} or not out.is_file():
        raise RuntimeError('The intended fixed actual loading chain was not inspected')


if __name__=='__main__':main()
