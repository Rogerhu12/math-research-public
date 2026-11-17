#!/usr/bin/env python3
"""Explicit replay of the original cut0 weak-height curvature experiment.

No intermediate optimizer template is needed. The old parameter values, zero
start, feasibility LP, diagonal scaling and L-BFGS-B options are written here.
The frozen AcceptedBase supplies the same height definition, with coupling
explicitly true. Its later prepare_initial and Armijo paths are not called.
The original polynomial evaluation of cap w is retained, rather than the
algebraically equivalent factored evaluation used by the frozen reader.
"""
from pathlib import Path
import argparse,hashlib,importlib.util,json,time
import numpy as np
from scipy.optimize import minimize

HERE=Path(__file__).parent
spec=importlib.util.spec_from_file_location('cut0_frozen_definition',HERE/'2026-11-17-parallel-model-direct-height-accepted-base.py')
model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)

class ReplayBase(model.AcceptedBase):
    def reference_metric(self,r):
        r=np.asarray(r);inner=np.minimum(r,self.deep_r)
        w=np.exp(self.bg.spline(inner));wr=w*self.bg.spline(inner,1)
        outside=r>self.deep_r
        if np.any(outside):
            u=(r[outside]-self.deep_r)/self.cap_width
            w[outside]=np.polynomial.polynomial.polyval(u,self.wpolynomial)
            wr[outside]=np.polynomial.polynomial.polyval(u,np.polynomial.polynomial.polyder(self.wpolynomial))/self.cap_width
        return w,wr

def main(a):
    p=argparse.Namespace(trace=a.trace,background=a.background,out=a.out,input=None,
        accepted_state=a.state,accepted_mean_anchor=.9196724087226285,accepted_scale=.0014,
        cuff_radius=1.767318285443017,cap_lift=.048856939517352364,cut_fraction=0.,
        modes=32,angles=512,gauss=8,metric_stride=64,panel_refinement=1,height_knots='segments',
        metric_knots='[0.005,0.015,0.04,0.08,0.15,0.25,0.4]',angular_basis='physical',
        decay_length=.08,coefficient_scale=.1,join_width=.01,branch_floor=1e-4,
        branch_margin=1e-3,branch_weight=100.,curvature_limit=6.8,curvature_weight=10.,
        height_limit=1.21,height_weight=10.,actual_curvature_weight=.1,actual_curvature_limit=6.8,
        amplitude=1.,metric_modes=5,metric_bound=4.,end_weight=1.,max_nfev=300,tolerance=1e-9,
        log_every=20,method='lbfgs',operator_scale=.1,linear_iterations=40,no_positive_start=False,
        no_diagonal_scale=False,freeze_metric=False,scaling='heuristic',rescale_input=False,
        cap_metric_modes=False,cap_length_weight=0.,metric_height_coupling=True,function_tolerance=1e-14)
    q=ReplayBase(p);q.source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    x=np.zeros(q.n);old_n,old_ng=q.n,q.ng;q.n=q.nheight;q.ng=0
    x[:q.nheight]=model.direct.base.DirectHeight.positive_mean_start(q,x[:q.nheight]);q.n=old_n;q.ng=old_ng
    initial_norm=float(abs(x).max());q.objective(x)
    weight=(q.width[:,None]*q.gw/q.L).ravel();scale=np.ones(q.n)
    for j,m in enumerate(np.r_[0,q.freq]):
        norm=q.height_scale*np.sqrt(np.sum(weight[:,None]*(q.B[1]**2+(1+m*m)**2*q.B[0]**2),axis=0))
        scale[j*q.nf:(j+1)*q.nf]=1/np.maximum(norm,1e-3)
    scale[q.nheight-1]=1/max(q.height_scale*np.sqrt(np.sum(weight*q.Bend[1]**2)),1e-3)
    scale[q.nheight:]=min(300.,10/max(np.sqrt(p.amplitude),.01))
    def objective(v):
        value,gradient=q.objective(v*scale);return value,gradient*scale
    bounds=[(None,None)]*q.nheight+[(-p.metric_bound/scale[j],p.metric_bound/scale[j]) for j in range(q.nheight,q.n)]
    sol=minimize(objective,x/scale,jac=True,method='L-BFGS-B',bounds=bounds,
        options=dict(maxiter=300,maxfun=1200,maxls=30,ftol=1e-14,gtol=1e-9,maxcor=30))
    final=sol.x*scale;z=q.reconstruct(final);q.last_info=q.diagnostics(z)
    q.last_info.update(sampled_reference_curvature=float(z['reference_curvature'].max()),sampled_actual_curvature=float(z['actual_curvature'].max()))
    cost=float(np.sum(np.asarray(q.ad_residual(final))**2)/2)
    status=dict(success=bool(sol.success),message=str(sol.message),nfev=int(sol.nfev),nit=int(sol.nit),variable_scale=scale.tolist())
    q.save_design(final,cost,True,status);report=json.loads(a.out.read_text())
    report['legacy_replay']=dict(scope=__doc__,source_sha256=q.source_sha,zero_initializer_maximum=initial_norm,
        frozen_definition_sha256=hashlib.sha256((HERE/'2026-11-17-parallel-model-direct-height-accepted-base.py').read_bytes()).hexdigest(),
        coefficient_binary_sha256=hashlib.sha256(np.asarray(final,dtype='<f8').tobytes()).hexdigest(),
        no_template_dependency=True,original_candidate_sha256='8fed32f53f5d839d10056c04645919e335034cf559be4e09b74efecff827eeae')
    if a.compare:
        old=np.array(json.loads(a.compare.read_text())['coefficients']);diff=final-old
        report['legacy_replay']['comparison']=dict(reference_sha256=hashlib.sha256(a.compare.read_bytes()).hexdigest(),
            coefficient_binary_equal=bool(np.array_equal(final,old)),maximum_coefficient_difference=float(abs(diff).max()),
            old_coefficient_binary_sha256=hashlib.sha256(np.asarray(old,dtype='<f8').tobytes()).hexdigest())
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(event='replay-done',cost=cost,nfev=int(sol.nfev),nit=int(sol.nit),diagnostics=q.last_info,legacy_replay=report['legacy_replay'])),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--trace',type=Path,required=True)
    p.add_argument('--state',type=Path,required=True);p.add_argument('--background',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--compare',type=Path)
    main(p.parse_args())
