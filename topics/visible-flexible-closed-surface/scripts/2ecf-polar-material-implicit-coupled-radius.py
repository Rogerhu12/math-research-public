#!/usr/bin/env python3
"""Joint radial log-metric and implicit unit-material directions, or a genuine fixed-g continuation."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import os
for name in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):
    os.environ[name]='1'
import numpy as np
from scipy.interpolate import BSpline
here=Path(__file__).parent
def module(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
impl=module(here/'2ecf-polar-material-coupled-implicit-design-and-observe.py','radius_spherical_closure')
base=impl.old
radius_op=module(here/'2ecf-polar-log-radius-operator.py','radius_consumer')
def radius_basis(t,spans):
    knots=np.r_[np.zeros(6),np.arange(1,spans)/spans,np.ones(6)]
    B=BSpline(knots,np.eye(len(knots)-6),5)(np.clip(t,0,1))[:,3:-3]
    B[(t<=0)|(t>=1)]=0
    return B
def target_hash(spans,alpha,b,S):
    desc=dict(spans=int(spans),alphaHex=[float(v).hex() for v in alpha],bHex=float(b).hex(),endHex=float(S).hex(),degree=5,support='b<S; full quintic positive exponential; original equal on both outer portions')
    return hashlib.sha256(json.dumps(desc,sort_keys=True,separators=(',',':')).encode()).hexdigest()
class Designed(impl.Implicit):
    def __init__(self,args,ends,initial,nr,nu):
        super().__init__(args,ends,initial,nr,nu)
        self.BR=radius_basis(self.t,args.radius_spans)
        self.npos=sum(self.counts)
        self.alpha0=np.zeros(self.BR.shape[1])
        if args.frozen is not None:
            q=base.read(args.frozen)
            assert q['radiusSpans']==args.radius_spans and q['preparedSHA256']==base.sha(args.prepared)
            self.alpha0=np.array(q['logRadiusCoefficients'])
    def starting(self):
        state=base.read(self.args.start)
        if 'positionCoefficients' in state:
            from scipy.interpolate import BSpline
            cfg=state['spans'];m=state['modes'];x=np.asarray(state['positionCoefficients'])
            kn=np.r_[np.zeros(4),np.arange(1,cfg)/cfg,np.ones(4)]
            B=BSpline(kn,np.eye(len(kn)-4),3)(self.t)[:,2:-2]
            n=B.shape[1]*(m+1)
            parts=[]
            for i,(v,F) in enumerate(zip((x[:n].reshape(B.shape[1],-1),x[n:].reshape(B.shape[1],-1)),self.F)):
                f=np.cos(self.u[:,None]*2*np.arange(m+1)) if i==0 else np.sin(self.u[:,None]*2*np.arange(1,m+1))
                coeff=np.linalg.lstsq(self.B,B@v@f.T,rcond=1e-12)[0]
                parts.append(np.linalg.lstsq(F,coeff.T,rcond=1e-12)[0].T.ravel())
            x=np.concatenate(parts)
            assert state['seedFieldSHA256']==base.sha(self.args.seed_field)
        else:x=super().starting()
        return x if self.args.frozen else np.r_[x,self.alpha0]
    def field(self,x):
        return super().field(x[:self.npos])
    def value(self,x,with_gradient=True):
        if not hasattr(self,'referenceRadius'):
            self.referenceRadius=self.rad.copy()
            point=self.point.PointLinearized;area=self.area.AreaPacket
            def current_point(*args):
                self.lastPoint=point(*args);return self.lastPoint
            def current_area(*args):
                self.lastArea=area(*args);return self.lastArea
            self.point=SimpleNamespace(PointLinearized=current_point)
            self.area=SimpleNamespace(AreaPacket=current_area)
        alpha=self.alpha0 if self.args.frozen else x[self.npos:]
        self.rad=self.referenceRadius*np.exp(self.BR@alpha)[:,None]
        result=super().value(x[:self.npos],with_gradient)
        if not with_gradient:
            result['maxLogRadiusChange']=float(np.max(np.abs(self.BR@alpha)))
            return result
        loss,g=result
        if self.args.frozen:return loss,g
        cr,ca=radius_op.radius_columns(self.lastPoint,self.lastArea,self.weights['metric'],1.,.5)
        scalar=2*np.sum(cr*self.lastPoint.residual,axis=(1,2))+2*np.sum(ca*self.lastArea.residual,axis=1)
        return loss,np.r_[g,self.BR.T@scalar]

def design(args):
    dest=args.output
    if dest.exists():raise FileExistsError(dest)
    base.Model=Designed
    with TemporaryDirectory(dir=dest.parent) as temp:
        intermediate=Path(temp)/'design.json'
        args.output=intermediate;base.design(args);q=base.read(intermediate)
    x=np.array(q.pop('coefficients'))
    count=(args.spans-1)*(2*args.modes+1)
    # Remove the ambiguous concatenated vector: position and metric have separate identities.
    pos=x[:count]
    alpha=np.array(base.read(args.frozen)['logRadiusCoefficients']) if args.frozen else x[count:]
    assert len(alpha)==args.radius_spans-1
    flat=np.load(args.field);b,S=flat['knots'][[0,-1]]
    q.update(schema='explicit-new-diagonal-material-radius-and-spherical-3D-physical-port-closure-v1',jointEntrySHA256=base.sha(__file__),implicitEntrySHA256=base.sha(impl.__file__),positionCoefficients=pos.tolist(),logRadiusCoefficients=alpha.tolist(),radiusSpans=args.radius_spans,positionControls=len(pos),radiusDesignControls=0 if args.frozen else len(alpha),fixedDesignedTarget=bool(args.frozen),targetSHA256=target_hash(args.radius_spans,alpha,b,S),startSHA256=base.sha(args.start),frozenStateSHA256=(base.sha(args.frozen) if args.frozen else None))
    if args.frozen:assert q['targetSHA256']==base.read(args.frozen)['targetSHA256']
    base.stores(dest,q)

def observe(args):
    d=base.read(args.design);seed=base.read(args.seed_design)
    assert d['jointEntrySHA256']==base.sha(__file__) and d['fieldSHA256']==base.sha(args.field) and d['seedDesignSHA256']==base.sha(args.seed_design)
    ends_module=base.end_module(here,seed)
    eng=base.load(here/'2ecf-polar-raised-physical-ray-field-observe.py','rad_full_obs')
    loader=eng.load;eng.PhysicalRays=base.MaterialField
    cache=np.load(args.field);b,S=cache['knots'][[0,-1]]
    alpha=np.asarray(d['logRadiusCoefficients'])
    assert target_hash(d['radiusSpans'],alpha,b,S)==d['targetSHA256']
    def supply(path,name):
        if Path(path).name=='2ecf-polar-raised-monotone-oblique-connector.py':return ends_module
        m=loader(path,name)
        if Path(path).name=='2ecf-polar-gap092-true-tail-amplitude-height.py':
            scan=m.evaluate
            def evaluate(stats,pt,area,packet,rad,ns,u,cfg,weights):
                radius=rad.copy()
                radius[:,0]*=np.exp(radius_basis((ns-b)/(S-b),d['radiusSpans'])@alpha)
                return scan(stats,pt,area,packet,radius,ns,u,cfg,weights)
            m.evaluate=evaluate
        return m
    eng.load=supply;dest=args.output
    with TemporaryDirectory(dir=dest.parent) as temp:
        p=Path(temp)/'full.json';args.output=p;eng.run(args);q=base.read(p)
    q.update(actualJointRadiusEntrySHA256=base.sha(__file__),targetSHA256=d['targetSHA256'],frozenMetric=d['fixedDesignedTarget'])
    base.stores(dest,q)

if __name__=='__main__':
    a=argparse.ArgumentParser()
    a.add_argument('--mode',choices=('design','observe'),required=True)
    for k in ('scripts','ramp','coast','prepared','field','output','seed-field','seed-design','design','independent','start','frozen'):
        a.add_argument('--'+k,type=Path)
    for k,v in [('angles',128),('radials',121),('spans',24),('modes',12),('iterations',250),('fine-radials',769),('fine-angles',320),('cells',96),('stored-modes',100),('trace-nodes',2048),('radius-spans',12)]:
        a.add_argument('--'+k,type=int,default=v)
    for k,v in [('closure',0.),('curvature',2.),('geometry',180.)]:
        a.add_argument('--'+k,type=float,default=v)
    args=a.parse_args();(design if args.mode=='design' else observe)(args)
