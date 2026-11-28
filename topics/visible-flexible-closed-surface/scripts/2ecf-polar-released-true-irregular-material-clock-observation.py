#!/usr/bin/env python3
"""Direct full six-jet evaluation at every irregular reparametrized point; no spatial interpolation table."""
import argparse
import importlib.util
from pathlib import Path
import sys
import os
for k in ('MKL_NUM_THREADS','OMP_NUM_THREADS','OPENBLAS_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from numpy.polynomial import Polynomial
def module(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m
here=Path(__file__).parent;c=module(here/'2ecf-polar-released-material-physical-two-clock-design.py','accurate_input_clock_design')
ext=c.ext;base=c.base
H=[Polynomial(z) for z in ((1,0,0,-10,15,-6),(0,1,0,-6,8,-3),(0,0,.5,-1.5,1.5,-.5),(0,0,0,10,-15,6),(0,0,0,-4,7,-3),(0,0,0,.5,-1,.5))]
orders=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))
class PhysicalField:
    def __init__(self,a):
        self.ends,self.sol,self.b,self.S,self.T,self.rf,self.g,self.grid=c.source(a)
        z=np.load(a.field);self.co=z['coeff'];self.knots=z['knots'];self.M=np.arange(self.co.shape[2])
        self.active=np.array(self.sol['coefficients']).reshape(3,self.sol['spans']-1,self.sol['modes']+1)
    def evaluate(self,s,u):
        cell=np.clip(np.searchsorted(self.knots,s,side='right')-1,0,len(self.knots)-2);h=self.knots[cell+1]-self.knots[cell];t=(s-self.knots[cell])/h
        M=self.M;ph=np.exp(1j*np.outer(u,M));phase=[ph*(1j*M[None,:])**j for j in range(3)]
        end=self.ends;traces=[]
        for d in (0,1):
            node=cell+d;A=np.empty((len(s),3,3,3))
            for j in range(3):
                cc=self.co[node,j]
                for k in range(3):A[:,j,k]=np.einsum('qmc,qm->qc',cc,phase[k],optimize=False).real
            edge=node==(0 if d==0 else len(self.knots)-1)
            if np.any(edge):
                po=end.base.higher_coast_port(end.master,.02,u[edge]) if d==0 else ext.flat_port(u[edge],float(self.rf))
                for j,keys in enumerate((('P','Pu','Puu'),('V','Vu','Vuu'),('A','Au','Auu'))):
                    for k,key in enumerate(keys):A[edge,j,k]=po[key]
            traces.append(A)
        traces=np.concatenate(traces,axis=1)
        wh=np.ones((len(s),6));wh[:,[1,4]]=h[:,None];wh[:,[2,5]]=h[:,None]**2
        weights=[np.stack([p.deriv(j)(t) for p in H],axis=1)*wh/(h[:,None]**j) for j in range(3)]
        js=np.stack([np.einsum('qi,qic->qc',weights[j],traces[:,:,k]) for j,k in orders],axis=1)
        b=c.spline(s,self.b,self.T,self.sol['spans']);F=[]
        for i in range(3):
            freq=2*np.arange(self.sol['modes']+1)+(i<2);theta=np.outer(u,freq)-(i==1)*np.pi/2
            F.append([np.cos(theta+k*np.pi/2)*freq**k for k in range(3)])
        for z,(r,k) in enumerate(orders):
            for i in range(3):js[:,z,i]+=np.sum((b[r]@self.active[i])*F[i][k],axis=1)
        w=c.move.profile(s,self.b,self.T,*self.sol['transition'])
        for k,d in enumerate([0,1,3]):js[:,d,2]+=self.sol['raisedCuffDelta']*w[k]
        return js
    def compose(self,ns,u,sol):
        clock=c.Clock(ns,u,self.b,self.T,sol['spans'],sol['modes']);z=clock.get(np.array(sol['clockCoefficients']))
        s,v=z[0,0].ravel(),z[1,0].ravel()
        yy=np.concatenate([self.evaluate(s[k:k+512],v[k:k+512]) for k in range(0,len(s),512)]).reshape(len(ns),len(u),6,3).transpose(0,2,1,3)
        res=np.empty_like(yy);res[:,0]=yy[:,0]
        _,A,B,AA,AB,BB=z[0,:,:, :,None];_,C,D,CC,CD,DD=z[1,:,:, :,None]
        res[:,1]=yy[:,1]*A+yy[:,2]*C;res[:,2]=yy[:,1]*B+yy[:,2]*D
        res[:,3]=yy[:,3]*A*A+2*yy[:,4]*A*C+yy[:,5]*C*C+yy[:,1]*AA+yy[:,2]*CC
        res[:,4]=yy[:,3]*A*B+yy[:,4]*(A*D+B*C)+yy[:,5]*C*D+yy[:,1]*AB+yy[:,2]*CD
        res[:,5]=yy[:,3]*B*B+2*yy[:,4]*B*D+yy[:,5]*D*D+yy[:,1]*BB+yy[:,2]*DD
        return res
def run(a):
    m=PhysicalField(a);sol=base.read(a.clock);sp=base.read(a.spatial);old=base.read(a.closed)
    assert sol['spatialSHA256']==base.sha(a.spatial) and sol['previousTargetSHA256']==old['closedTrueTargetSHA256']
    b,S,T=m.b,m.S,m.T;alpha=np.array(sol['targetCoefficients'])
    if np.any(alpha):assert sol['newTargetSHA256']==c.target_hash(sol['previousTargetSHA256'],b,T,sol['metricSpans'],alpha)
    # Independent pointwise-vs-rectangular source comparison, including the actual variable end traces.
    chk_s=np.array([b,b+(T-b)*.002,b+(T-b)*.388,T-(T-b)*.002,T]);chk_u=2*np.pi*(np.arange(13)+.339)/13
    v=m.evaluate(np.repeat(chk_s,len(chk_u)),np.tile(chk_u,len(chk_s))).reshape(len(chk_s),len(chk_u),6,3).transpose(0,2,1,3)
    check=np.max(abs(v-m.grid(chk_s,chk_u)),axis=(0,2,3));assert max(check)<5e-8,check
    p=base.read(a.prepared);ind=base.read(a.independent);stream=module(a.scripts/'6a65-cartesian-complete-stream.py','clock_true_stream')
    ar=module(a.scripts/'6a65-geometry-area-ratio-power-two.py','clock_true_area')
    cfg=c.move.config(stream.point,p['definition']['pointConfig'],sp['raisedCuffDelta'])
    groups={k:(np.asarray(g['nodes']),np.asarray(g['angles']),g['files']['jets'],g['files']['radius'],g['weights']) for k,g in p['caches'].items()}
    groups['independent']=(np.asarray(ind['physicalNodes']),np.asarray(ind['angles']),ind['files']['jets'],ind['files']['radius'],None)
    ns=S+(T-S)*(np.arange(193)+.371)/193;groups['tail193x272']=(ns,2*np.pi*(np.arange(272)+.417)/272,None,None,None)
    rows={}
    for name,(ns,u,jp,rp,w) in groups.items():
        js=np.load(jp,mmap_mode='r') if jp else None;rf=np.load(rp,mmap_mode='r')[:,0] if rp else .8+S-ns
        rad=ext.apply_target(ns,rf,b,S,m.g);B,D,*_=c.spline(ns,b,T,sol['metricSpans']);rv=np.exp(B@alpha[0]);dv=D@alpha[0];rad*=np.exp(B@alpha[1])
        stats=None;area=0.;mins=999.
        for j in range(0,len(ns),6):
            ss=ns[j:j+6];sub=np.array(js[j:j+6],copy=True) if js is not None else np.empty((len(ss),6,len(u),3))
            active=(ss>=b)&(ss<=T)
            if np.any(active):sub[active]=m.compose(ss[active],u,sol)
            for i in np.flatnonzero(ss>T):
                port=ext.flat_port(u,rf[j+i]);sub[i]=np.stack([port[k] for k in ('P','V','Pu','A','Vu','Puu')]);sub[i,0,:,2]+=sp['raisedCuffDelta']
            vv=rv[j:j+6,None,None]
            sub[:,3]=(sub[:,3]-dv[j:j+6,None,None]*sub[:,1])/(vv*vv);sub[:,1]/=vv;sub[:,4]/=vv
            W={k:(np.ones((len(ss),1)) if w is None else .5*np.array(w[k][j:j+6])[:,None])/len(u) for k in ('curvature','metric','geometry')}
            f=rad[j:j+6,None];po=stream.point.PointLinearized(sub.swapaxes(1,2),f,cfg,W)
            block=stream._block_statistics(po,ss,len(u));block['worstMetric']['u']+=float(u[0]);block['worstCurvature']['u']+=float(u[0]);stats=stream._merge_statistics(stats,block)
            ap=ar.AreaPacket(sub,f,W['metric'],.5);area+=ap.stats['squaredNorm'];mins=min(mins,float(ap.stats['minAreaRatio']))
        rows[name]=dict(metric=stats['maxRelativeMetric'],curvature=stats['maxCurvature'],held=stats['minHeldDistance'],R2=stats['squaredNorm']+area if w is not None else None,worstMetric=stats['worstMetric'],worstCurvature=stats['worstCurvature'],area=mins,geometry=stats['geometryMaximumViolations'],actualRows=14*len(ns)*len(u))
        print(name,rows[name]['metric'],rows[name]['curvature'],rows[name]['held'],flush=True)
    base.stores(a.output,dict(entrySHA256=base.sha(__file__),clockSHA256=base.sha(a.clock),fieldSHA256=base.sha(a.field),spatialSHA256=base.sha(a.spatial),trueClosedMetricSHA256=sol['newTargetSHA256'],trueIrregularToOriginalGridCheck=check.tolist(),groups=rows))
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','ramp','coast','prepared','independent','seed-design','donor','donor-field','frozen','state','field','spatial','closed','clock','output'):p.add_argument('--'+k,type=Path,required=True)
    run(p.parse_args())
