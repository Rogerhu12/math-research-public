#!/usr/bin/env python3
"""UNSOLVED warm predictor: fixed-g prefix with a lifted affine slope port.

The low-mode block is a previously converged actual DN and its stored
Jacobian. Added modes use the frozen linear slope port; cross blocks vanish.
This changes only the auxiliary initial-guess problem, not the intended
actual nonlinear coupled problem. Original-DN correction is mandatory.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import gzip
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp

HERE=Path(__file__).resolve().parent


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class LiftedAffineSlope:
    def __init__(self,actual,linear,M):
        self.M=M;self.oldM=len(actual['request']['height'])
        if M<=self.oldM:
            raise ValueError('This predictor must add at least one Fourier mode')
        if not actual['response']['converged']:
            raise ValueError('The low-mode DN anchor must actually be converged')
        self.H0=np.zeros(M);self.H0[:self.oldM]=actual['request']['height']
        self.S0=np.zeros(M);self.S0[:self.oldM]=actual['response']['jets']['slope']
        self.J=np.zeros((M,M))
        self.J[:self.oldM,:self.oldM]=np.asarray(actual['response']['heightJetJacobian']).reshape(3*self.oldM+2,self.oldM)[:self.oldM]
        for j in range(self.oldM,M):self.J[j,j]=linear[j]
        # TailMixin only consumes these first M slope-Jacobian rows. The
        # remaining rows are placeholders, not second-jet or mean predictions.
        complete=np.zeros((3*M+2,M));complete[:M]=self.J
        self.matrix=complete.ravel().tolist()

    def solve(self,height,jacobian=True,audit=False):
        if audit:raise RuntimeError('UNSOLVED affine predictor cannot provide an actual tail audit')
        slope=self.S0+self.J@(np.asarray(height)-self.H0)
        return dict(jets=dict(slope=slope.tolist()),heightJetJacobian=self.matrix,
                    scope='UNSOLVED lifted affine slope port for an initial guess only')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-root',type=Path,required=True)
    ap.add_argument('--checkpoint',type=Path,required=True)
    ap.add_argument('--linear-port',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--modes',type=int,required=True)
    ap.add_argument('--angular',type=int,default=512)
    ap.add_argument('--max-nodes',type=int,default=4500)
    a=ap.parse_args();start=time.monotonic()
    if any(p.name!=a.out_prefix.name+'-run.log' for p in a.out_prefix.parent.glob(a.out_prefix.name+'*')):
        raise FileExistsError('Output prefix already used')
    runner=module('affine_lift_runner',HERE/'db6f-prefix-flat-coupled.py').m
    runner.adaptive.old.install_source(a.source_root)
    from curve_stable_prefix_bvp import load_checkpoint,save_checkpoint
    from f6curve_domain_newton import install,STATS
    rec=load_checkpoint(a.checkpoint)
    assert rec['solver_success'] and rec['config']['actual_nonlinear_tail']
    tailpath=a.checkpoint.parent/rec['tail_seam']['tail_record']
    actual=json.load(gzip.open(tailpath,'rt'))
    port=json.loads(a.linear_port.read_text());port['_sha256']=sha(a.linear_port)
    if rec['physical_port_sha256']!=port['_sha256']:
        raise ValueError('Frozen physical linear-port input changed')
    cfg=dict(rec['config'],modes=a.modes,angular=a.angular)
    _,Base=runner.adaptive.build_classes(rec['chart'])
    class BVP(runner.TailMixin,Base):pass
    obj=BVP(rec['frozen_profile'],port,rec['gauge_amplitude'],a.modes,a.angular,True,rec['warp_reference_q'])
    obj.bcweights=np.full(obj.M,cfg['physical_bc_tol']/cfg['bc_tol'])
    initializer=module('affine_lift_initializer',HERE/'db6f-prefix-preserve-restart.py')
    x,y,par,restart=initializer.restart(obj,a.checkpoint,rec['chart'])
    anchor=LiftedAffineSlope(actual,port['linearSlope'],obj.M);obj.tail=anchor
    startheight=obj.bridge.sigma*obj.q*y[obj.iz:,-1]
    initial_error=float(np.max(abs(obj.bc(y[:,0],y[:,-1],par))))
    manifest=dict(scope=__doc__,status='UNSOLVED initial-guess construction',
        command=[sys.executable,str(Path(__file__).resolve()),*sys.argv[1:]],
        checkpoint=str(a.checkpoint),checkpoint_sha256=sha(a.checkpoint),
        frozen_actual_tail=str(tailpath),frozen_actual_tail_sha256=sha(tailpath),
        linear_port=str(a.linear_port),linear_port_sha256=sha(a.linear_port),
        script_sha256=sha(__file__),source_sha256={name:sha(HERE/name) for name in
          ['db6f-prefix-flat-coupled.py','db6f-prefix-coupled.py','db6f-prefix-preserve-restart.py']},
        original_modes=anchor.oldM,modes=obj.M,angular=obj.nt,tolerance=cfg['tol'],
        bc_tolerance=cfg['bc_tol'],physical_bc_tolerance=cfg['physical_bc_tol'],
        maximum_nodes=a.max_nodes,initial_nodes=len(x),initial_affine_bc=initial_error,
        initial_cut_height=startheight.tolist(),anchor_height=anchor.H0.tolist(),
        added_linear_slopes=[float(anchor.J[j,j]) for j in range(anchor.oldM,obj.M)],
        cross_blocks='zero by definition of this surrogate only',restart=restart,
        actual_nonlinear_tail=False,original_projection_floor=actual['response']['checkpoint']['parameters']['projectionFloor'])
    a.out_prefix.with_name(a.out_prefix.name+'-input-bindings.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(dict(event='start_UNSOLVED_affine_lift',oldM=anchor.oldM,M=obj.M,
                         nodes=len(x),tol=cfg['tol'],initial_affine_bc=initial_error)),flush=True)
    install()
    try:
        sol=solve_bvp(obj.fun,obj.bc,x,y,par,tol=cfg['tol'],bc_tol=cfg['bc_tol'],
                      max_nodes=a.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=2)
        flow=obj.flow(sol.p[0]);obj.initial(sol.p)
        physical=SimpleNamespace(x=obj.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p)
        physical.sol=flow.c2_interpolant(physical)
        out={key:rec[key] for key in ('angular_chart','chart','warp_reference_q','frozen_profile',
                  'gauge_amplitude','physical_port_sha256','physical_tail_parameters','physical_tail_cut')}
        out.update(scope=__doc__,status='UNSOLVED relative to the actual nonlinear DN',
            config=dict(cfg,actual_nonlinear_tail=False,frozen_affine_dn=True),
            actual_primary_amplitude=obj.support_amplitude,meridian_length=flow.end,
            parameters=sol.p.tolist(),central_correction_scales=obj.pscale.tolist(),
            nodes=len(sol.x),solver_success=bool(sol.success),message=sol.message,
            max_rms_collocation_residual=float(np.max(sol.rms_residuals)),
            newton_domain_audit=dict(STATS),mesh=physical.x.tolist(),pp_coefficients=physical.sol.c,
            restart_mesh_diagnostics=restart,frozen_actual_tail=str(tailpath),
            frozen_actual_tail_sha256=sha(tailpath))
        save_checkpoint(a.out_prefix.with_suffix('.json.gz'),out)
        cutheight=obj.bridge.sigma*obj.q*sol.y[obj.iz:,-1]
        out['predicted_cut_height']=cutheight.tolist()
        out['predicted_slope_from_surrogate']=anchor.solve(cutheight)['jets']['slope']
        out['summary']=runner.adaptive.audit(obj,physical,max(1024,64*obj.M))
        out['summary']['scope']='Sampled prefix of an UNSOLVED affine initial guess; no actual tail or whole-surface result.'
        out['seconds']=time.monotonic()-start
        save_checkpoint(a.out_prefix.with_suffix('.json.gz'),out)
        summary={key:value for key,value in out.items() if key not in ('mesh','pp_coefficients')}
        manifest.update(affine_solver_success=bool(sol.success),nodes=len(sol.x),
            rms=out['max_rms_collocation_residual'],prefix_metric=out['summary']['metric_l1'],
            predicted_cut_height=cutheight.tolist(),cut_change_linf=float(np.max(abs(cutheight-startheight))),
            new_mode_cut_height_linf=float(np.max(abs(cutheight[anchor.oldM:]))),
            actual_amplitude=obj.support_amplitude)
        print(json.dumps(dict(event='UNSOLVED_affine_lift_result',**{key:manifest[key] for key in
             ['affine_solver_success','nodes','rms','prefix_metric','cut_change_linf','new_mode_cut_height_linf','actual_amplitude']})),flush=True)
    except Exception as exc:
        manifest.update(affine_solver_success=False,error=repr(exc));summary=dict(manifest)
        print(json.dumps(dict(event='affine_lift_failure',error=repr(exc))),flush=True)
    manifest['seconds']=time.monotonic()-start
    a.out_prefix.with_name(a.out_prefix.name+'-reproduction.json').write_text(json.dumps(manifest,indent=2)+'\n')
    a.out_prefix.with_name(a.out_prefix.name+'-summary.json').write_text(json.dumps(summary,indent=2)+'\n')


if __name__=='__main__':main()
