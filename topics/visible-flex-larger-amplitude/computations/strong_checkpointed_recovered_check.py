#!/usr/bin/env python3
"""Repeat the observation/atomic-roundtrip check after executor replacement.

This is a new check on an unrelated two-state toy BVP. It does not recreate
the lost original test report or the lost real-prefix NPZ files. The restored
production writer is verified against its original SHA separately.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import json
from pathlib import Path
import platform
import tempfile
import types
import numpy as np
import scipy
from scipy.integrate import _bvp
from strong_checkpointed_tangent_bvp import Recorder,read_bundle

HERE=Path(__file__).resolve().parent


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.out.exists():raise ValueError('Use a fresh check output')
    source_path=HERE/'root_domain_newton.py';source=source_path.read_text()
    hashes={str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in
            (Path(__file__),source_path,HERE/'strong_checkpointed_tangent_bvp.py')}
    modules=[]
    for name in ('plain','observed'):
        mod=types.ModuleType('strong_recovered_check_'+name)
        exec(compile(source,str(source_path),'exec'),mod.__dict__);modules.append(mod)
    plain,observed=modules
    fun_source=source[source.index('def solve_newton('):source.index('\n\ndef install(')]
    for old,new in [
        ('    data = evaluate(y, p)\n','    data = evaluate(y, p)\n    _observe(col_fun,y,p,data,0,"newton-entry",bvp_tol,bc_tol,STATS)\n'),
        ('        y, p, data, step, cost, alpha = accepted\n','        y, p, data, step, cost, alpha = accepted\n        _observe(col_fun,y,p,data,iteration+1,"accepted-newton",bvp_tol,bc_tol,STATS)\n'),
        ('    return y, p, False','    _observe(col_fun,y,p,data,iteration,"newton-return",bvp_tol,bc_tol,STATS)\n    return y, p, False')]:
        assert fun_source.count(old)==1
        fun_source=fun_source.replace(old,new)
    exec(compile(fun_source,str(source_path),'exec'),observed.__dict__)
    x=np.linspace(0.,1.,9);y=np.stack((np.exp(.8*x),np.exp(.8*x)-1));p=np.array([.8])
    def fun(t,Y,P):return np.stack((P[0]*Y[0],Y[0]))
    def jac(t,Y,P):
        J=np.zeros((2,2,len(t)));J[0,0]=P[0];J[1,0]=1.
        Pj=np.zeros((2,1,len(t)));Pj[0,0]=Y[0]
        return J,Pj
    def bc(a,b,P):return np.array([a[0]-1.,a[1],b[0]-np.e])
    def bc_jac(a,b,P):
        return np.array([[1.,0.],[0.,1.],[0.,0.]]),np.array([[0.,0.],[0.,0.],[1.,0.]]),np.zeros((3,1))
    col,jacobian=_bvp.prepare_sys(2,len(x),1,fun,bc,jac,bc_jac,x,np.diff(x))
    call=(2,len(x),np.diff(x),col,bc,jacobian,y.copy(),p.copy(),None,1e-6,1e-7)
    ordinary=plain.solve_newton(*call)
    class Fixture:
        M=1;nt=64;q=.09;fixed=False
        ref_coeff=np.array([0.,0.]);ref_frequencies=[2,4]
        _neck_knots=np.array([0.,1.]);_special_layout='toy validation only'
        raw_recovery_context={'validation_fixture':True}
        cfg={'validation_fixture':True}
        port={'parameters':{'validation_fixture':True},'cut':{'validation_fixture':True}}
        def select(self,P):self.controls=np.asarray(P).copy()
        def flow(self,p0):return types.SimpleNamespace(cfg={'validation_fixture':True,'parameter':float(p0)})
    with tempfile.TemporaryDirectory(prefix='strong-recovered-check-') as directory:
        recorder=Recorder(Path(directory)/'toy',hashes);recorder.obj=Fixture()
        observed._observe=recorder.save
        checked=observed.solve_newton(*call)
        assert np.array_equal(ordinary[0],checked[0]) and np.array_equal(ordinary[1],checked[1])
        assert ordinary[2]==checked[2]
        assert len(recorder.retained)==2
        saved=[]
        for f in recorder.retained:
            meta,arrays=read_bundle(f)
            assert meta['solver_success'] is False and meta['physical_surface'] is False
            assert np.array_equal(arrays['x'],x)
            saved.append(dict(bytes=f.stat().st_size,phase=meta['state_phase']))
        meta,arrays=read_bundle(recorder.retained[-1])
        assert np.array_equal(arrays['y'],checked[0]) and np.array_equal(arrays['p'],checked[1])
        exact_cubic=_bvp.create_spline(checked[0],fun(x,checked[0],checked[1]),x,np.diff(x)).c
        assert np.array_equal(arrays['cubic'],exact_cubic)
        rows=[json.loads(s) for s in recorder.ledger.read_text().splitlines()]
        report=dict(scope=__doc__,finished=True,nonlinear_surface=False,source_sha256=hashes,
            runtime=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
            returned_y_p_bitwise_equal=True,singular_flag_equal=True,cubic_bitwise_equal=True,
            written_bundles=recorder.serial,accepted_step_bundles=sum(r['phase']=='accepted-newton' for r in rows),
            retained_complete_bundles=len(recorder.retained),retained=saved,
            all_saved_states_explicitly_unaccepted=True,temporary_bundles_removed_after_check=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report),flush=True)


if __name__=='__main__':main()
