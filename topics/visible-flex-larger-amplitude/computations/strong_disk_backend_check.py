#!/usr/bin/env python3
"""Small synthetic integration check of the disk production shim and hard gate.

No physical prefix, actual metric, true-tail worker or nonlinear BVP is run.
The separate original-vs-disk arithmetic checks belong to the root helper.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse
import hashlib
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import numpy as np
import root_block_collocation as original
from strong_disk_actual_backend import install_disk_backend


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    checks={}
    with tempfile.TemporaryDirectory(prefix='strong-disk-shim-check-') as directory:
        bounded=SimpleNamespace(blocks=original)
        runtime=install_disk_backend(bounded,Path(directory)/'synthetic',
            dict(backward_error_tolerance=5e-11,heartbeat_seconds=20,temporary_parent=directory))
        try:
            assert bounded.blocks.prepare_sys.__defaults__==(24,)
            bounded.blocks.prepare_sys.__defaults__=(3,)
            bounded.blocks.install()
            assert original._bvp.prepare_sys is bounded.blocks.prepare_sys
            checks['original_driver_defaults_and_install_protocol']=True
            x=np.linspace(0.,1.,9);h=np.diff(x)
            y=np.array([.3+.2*x,.5-.1*x],dtype=float);p=np.array([.2])
            def fun(t,z,a):
                return np.array([z[1]+a[0]*np.sin(z[0]),-.7*z[0]+t*a[0]])
            def jac(t,z,a):
                J=np.zeros((2,2,len(t)));J[0,0]=a[0]*np.cos(z[0]);J[0,1]=1;J[1,0]=-.7
                P=np.array([[np.sin(z[0])],[t]])
                return J,P
            def bc(a,b,p):return np.array([a[0]-p[0],a[1]-.5,b[0]-.6])
            def bcj(a,b,p):
                return (np.array([[1.,0.],[0.,1.],[0.,0.]]),
                    np.array([[0.,0.],[0.,0.],[1.,0.]]),np.array([[-1.],[0.],[0.]]))
            col,sys=bounded.blocks.prepare_sys(2,9,1,fun,bc,jac,bcj,x,h)
            residual,middle,f,fm=col(y,p)
            matrix=sys(y,p,middle,f,fm,bc(y[:,0],y[:,-1],p))
            factor=bounded.blocks.DirectBlockQRFactor(matrix,2,9,1)
            exact=np.linspace(-.7,.9,19)
            rhs=matrix.matvec(exact)
            computed=factor.solve(rhs)
            assert np.max(abs(computed-exact))<2e-12
            checks['real_disk_factor_single_rhs_streamed_gate']=True
            exacts=np.column_stack((exact,np.cos(np.arange(19))))
            rhses=np.column_stack([matrix.matvec(exacts[:,i]) for i in range(2)])
            solved=factor.solve(rhses)
            assert np.max(abs(solved-exacts))<2e-12
            checks['multiple_rhs_original_traversal_and_each_column_gate']=True
            observed_valid_error=runtime.stats['maximum_numerical_backward_error']
            proper=factor._audit_matrix
            factor._audit_matrix=SimpleNamespace(matvec=lambda value:proper.matvec(value)+1.)
            try:
                factor.solve(rhs)
            except np.linalg.LinAlgError:
                checks['corrupted_matvec_is_hard_rejected']=True
            else:
                raise AssertionError('A deliberately inconsistent original-system product was accepted')
            finally:
                factor._audit_matrix=proper
            assert runtime.memory()['prefix']['pid']==os.getpid()
            checks['RSS_is_observed_inside_the_owned_process']=True
            stats=dict(runtime.stats)
        finally:
            runtime.finish()
        assert bounded.blocks is original and not Path(runtime.directory).exists()
        checks['backend_restored_and_anonymous_temporary_directory_released']=True
    source=Path(__file__).resolve().parent
    report=dict(scope=__doc__,checks=checks,passed=all(checks.values()),
        original_accepted_linear_backward_error_max=observed_valid_error,
        stats_including_deliberate_rejected_corruption=stats,
        source_sha256={name:hashlib.sha256((source/name).read_bytes()).hexdigest()
            for name in ('strong_disk_backend_check.py','strong_disk_actual_backend.py','root_disk_block_collocation.py')},
        physical_Jacobians=0,physical_tail_workers=0,nonlinear_BVPs=0,
        actual_production_each_solve_still_requires_its_own_streamed_gate=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report),flush=True)


if __name__=='__main__':main()
