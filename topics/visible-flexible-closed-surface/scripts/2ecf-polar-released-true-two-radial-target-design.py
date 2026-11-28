#!/usr/bin/env python3
"""Joint physical shape and radial target, or its genuinely frozen target with enriched position basis."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.optimize import minimize

def module(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
here=Path(__file__).parent
cart=module(here/'2ecf-polar-released-actual-cartesian-guarded-design.py','released_metric_position')
base=cart.base;ext=cart.ext
def metric_basis(ns,b,T,spans):
    from scipy.interpolate import BSpline
    t=(ns-b)/(T-b);kn=np.r_[np.zeros(6),np.arange(1,spans)/spans,np.ones(6)]
    spline=BSpline(kn,np.eye(len(kn)-6),5);mask=(t>0)&(t<1)
    return [spline(np.clip(t,0,1),nu=k)[:,3:-3]*mask[:,None]/(T-b)**k for k in (0,1)]
def target_id(a,alpha,b,T,old):
    d=dict(previousTargetSHA256=old,b=float(b).hex(),T=float(T).hex(),basis='open degree-5 uniform, remove three end coefficients both sides',spans=a.metric_spans,radialSpeedAndHoopLogHex=[[float(v).hex() for v in row] for row in alpha])
    return hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def warp(raw,logv,der):
    vel=np.exp(-logv)[:,None,None];ans=raw.copy()
    ans[:,1]=vel*raw[:,1];ans[:,4]=vel*raw[:,4];ans[:,3]=vel**2*(raw[:,3]-der[:,None,None]*raw[:,1])
    return ans,vel
def run(a):
    ends,ref,b,S,T,rf,g=ext.setup(a);st=base.read(a.state);warm=base.read(a.warm)
    assert st['fieldSHA256']==base.sha(a.field) and st['targetSHA256']==g['targetSHA256'] and warm['sourceFieldSHA256']==base.sha(a.field)
    if a.mode=='observe':
        sol=base.read(a.solution);alpha=np.array(sol['logPhysicalMetricCoefficients']);a.metric_spans=sol['metricSpans']
        assert sol['entrySHA256']==base.sha(__file__) and target_id(a,alpha,b,T,g['targetSHA256'])==sol['newTargetSHA256']
        groups,evaluate,*_=cart.lift.load_groups(a,('training','observer','independent','tail193x272'));result={}
        for name,(ns,u,j,r,w) in groups.items():
            bas=cart.Basis(ns,u,b,T,sol['spans'],sol['modes']);br,dr=metric_basis(ns,b,T,a.metric_spans)
            act,unused=warp(j+bas.apply(np.asarray(sol['positionCoefficients'])),br@alpha[0],dr@alpha[0]);target=r.copy();target[:,0]*=np.exp(br@alpha[1])
            result[name]=evaluate(ns,u,act,target,w);v=result[name];print(name,v['metric'],v['curvature'],v['held'],v['R2'],flush=True)
        base.stores(a.output,dict(entrySHA256=base.sha(__file__),solutionSHA256=base.sha(a.solution),newTargetSHA256=sol['newTargetSHA256'],observations=result));return
    ns=np.linspace(b,T,a.radials);u=2*np.pi*np.arange(a.angles)/a.angles
    basis=cart.Basis(ns,u,b,T,a.spans,a.modes);br,dr=metric_basis(ns,b,T,a.metric_spans);npv=int(np.prod(basis.shape));na=br.shape[1]
    field=base.MaterialField(a.field,ends);j=np.concatenate([field.position(ns[k:k+12],u) for k in range(0,len(ns),12)])
    pre=base.read(a.prepared);c=pre['caches']['training'];p=Path(c['files']['radius']);assert base.sha(p)==c['SHA256']['radius']
    ix=np.argsort(c['nodes']);f=np.interp(ns,np.array(c['nodes'])[ix],np.load(p)[:,0][ix]);f[ns>=S]=.8+S-ns[ns>=S];f=ext.apply_target(ns,f,b,S,g)[:,None]
    old=cart.Basis(ns,u,b,T,warm['spans'],warm['modes'])
    xx=np.asarray(warm.get('positionCoefficients',warm.get('coefficients'))).reshape(old.shape)
    xi=[]
    for k in range(3):
        c1=np.linalg.lstsq(basis.B[0],(old.B[0]@xx[k])@old.F[k][0].T,rcond=1e-13)[0]
        xi.append(np.linalg.lstsq(basis.F[k][0],c1.T,rcond=1e-13)[0].T.ravel())
    shape=np.concatenate(xi);alpha0=np.asarray(warm.get('logPhysicalMetricCoefficients',np.zeros((2,na))))
    assert alpha0.shape==(2,na)
    if a.fixed_metric:assert warm['newTargetSHA256']==target_id(a,alpha0,b,T,g['targetSHA256'])
    x0=shape if a.fixed_metric else np.r_[shape,alpha0.ravel()]
    point=module(a.scripts/'6a65-cartesian-complete-stream.py','two_radial_physical_rows').point
    area=module(a.scripts/'6a65-geometry-area-ratio-power-two.py','two_radial_area')
    cfg=ends.raised.tall_config(point.PointConfig)(**dict(pre['definition']['pointConfig'],true_cuff_height=.415,height_maximum=.113))
    w=np.ones((len(ns),1));w[[0,-1]]=.5;w/=w.sum()*len(u);weights=dict(metric=w,geometry=w*a.geometry,curvature=w*a.curvature)
    centers=[np.array([0,sign*ends.master.A,0]) for sign in (-1,1)]
    def value(x,gradient=True):
        alpha=alpha0 if a.fixed_metric else x[npv:].reshape(2,na)
        logv=br@alpha[0];der=dr@alpha[0];logf=br@alpha[1]
        source=j+basis.apply(x[:npv]);js,v=warp(source,logv,der);fr=f*np.exp(logf)[:,None]
        pt=point.PointLinearized(js.swapaxes(1,2),fr,cfg,weights);ar=area.AreaPacket(js,fr,w,.5)
        loss=np.sum(pt.residual**2)+np.sum(ar.residual**2);ds=[]
        for center in centers:
            dd=source[:,0]-center;length=np.linalg.norm(dd,axis=-1);gap=np.maximum(0,a.held-length)
            loss+=a.guard*np.sum(w*gap**2);ds.append((dd,length,gap))
        if not gradient:return dict(loss=float(loss),metric=float(np.max(np.abs(pt.metric/np.array([1.,np.sqrt(2.),1.])))),kappa=float(np.max(abs(pt.curvature['eigenvalues']))),held=float(min(np.min(d[1]) for d in ds)),logVelocityRange=[float(min(logv)),float(max(logv))],logHoopRange=[float(min(logf)),float(max(logf))])
        adj=2*pt.vjp(pt.residual).swapaxes(1,2);gs,gu=ar.vjp(2*ar.residual);adj[:,1]+=gs;adj[:,2]+=gu
        adj[:,1]=v*adj[:,1]-v*v*der[:,None,None]*adj[:,3];adj[:,3]*=v**2;adj[:,4]*=v
        for dd,length,gap in ds:adj[:,0]-=(2*a.guard*w*gap/length)[...,None]*dd
        gx=basis.transpose(adj)
        if a.fixed_metric:return float(loss),gx
        cr,ca=ext.radius.radius_op.radius_columns(pt,ar,w,1.,.5)
        area_der=2*np.sum(ca*ar.residual,axis=1)
        g1=2*np.sum(cr*pt.residual,axis=(1,2))+area_der
        raw=np.zeros_like(pt.metric);raw[...,0]=-2*(pt.metric[...,0]+1);raw[...,1]=-pt.metric[...,1]
        cv=pt.sqrt_weights['metric'][...,None]*pt.metric_apply(raw)
        g0=2*np.sum(cv*pt.residual[...,:3],axis=(1,2))+area_der
        return float(loss),np.r_[gx,br.T@g0,br.T@g1]
    loss,grad=value(x0);rng=np.random.default_rng(11690);d=rng.normal(size=len(x0));d/=np.linalg.norm(d);h=2e-7
    fd=(value(x0+h*d,False)['loss']-value(x0-h*d,False)['loss'])/(2*h)
    err=abs(fd-grad@d)/max(1.,abs(fd),abs(grad@d));assert err<5e-5,(err,fd,grad@d)
    hist=[]
    def cb(z):
        hist.append(value(z,False))
        if len(hist)%100==0:print(len(hist),hist[-1],flush=True)
    opt=minimize(value,x0,jac=True,method='L-BFGS-B',callback=cb,options=dict(maxiter=a.iterations,gtol=2e-8,ftol=1e-15,maxls=45,maxcor=26))
    aa=alpha0 if a.fixed_metric else opt.x[npv:].reshape(2,na)
    base.stores(a.output,dict(entrySHA256=base.sha(__file__),sourceFieldSHA256=base.sha(a.field),sourceStateSHA256=base.sha(a.state),warmSHA256=base.sha(a.warm),oldTargetSHA256=g['targetSHA256'],newTargetSHA256=target_id(a,aa,b,T,g['targetSHA256']),fixedCurrentMetric=a.fixed_metric,physicalDomain=[b,T],metricSpans=a.metric_spans,spans=a.spans,modes=a.modes,logPhysicalMetricCoefficients=aa.tolist(),positionCoefficients=opt.x[:npv].tolist(),angularGrid=a.angles,radialGrid=a.radials,actualOwn=opt.nit,controls=len(x0),gradientCheck=err,starting=value(x0,False),final=value(opt.x,False),history=hist))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=('design','observe'),required=True);p.add_argument('--fixed-metric',action='store_true')
    for k in ('scripts','ramp','coast','prepared','independent','seed-design','donor','donor-field','frozen','state','field','warm','solution','output'):p.add_argument('--'+k,type=Path)
    for k,v in [('radials',129),('angles',88),('spans',15),('modes',6),('metric-spans',14),('iterations',900)]:p.add_argument('--'+k,type=int,default=v)
    for k,v in [('curvature',3.),('geometry',40.),('guard',350000.),('held',.6547)]:p.add_argument('--'+k,type=float,default=v)
    run(p.parse_args())
