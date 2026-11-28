#!/usr/bin/env python3
"""Fresh raised-tail connector with prescribed endpoints, positive radius and oblique height q=z-k*rho."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
for name in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[name]='1'
import numpy as np
from scipy.interpolate import BPoly
from scipy.special import betainc, comb
from numpy.polynomial import Polynomial

def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def get(p):return json.loads(Path(p).read_text())
def write(p,data):
    with Path(p).open('x') as f:json.dump(data,f,indent=2);f.write('\n')
def periodic_spline(x,jets):
    # Data are physical value, first and second angular derivatives, not Taylor coefficients.
    y=np.moveaxis(jets,2,0).swapaxes(1,2);knots=np.r_[x,x[0]+2*np.pi]
    if np.any(np.diff(knots)<=0):raise ArithmeticError("Positive native endpoint clock required")
    return BPoly.from_derivatives(knots,np.concatenate([y,y[:1]]),orders=5)
def higher_raised(warm,raised,A,c,u):
    ports=warm.ports;count=len(u);radius=.8
    U=ports.constant(u,count);U[1]=1;su,cu=ports.sincos(U);y=radius*su
    sign=np.where(y[0]<0,-1.,1.);active=sign*y[0]>c
    x=(y*sign[None,:]-ports.constant(c,count))/(.8-c);x[:,~active]=0
    alpha=A*(126*ports.power(x,5)-420*ports.power(x,6)+540*ports.power(x,7)-315*ports.power(x,8)+70*ports.power(x,9))
    sn,cs=ports.sincos(alpha);hp=sn*sign
    pu=np.stack((-radius*su,ports.mul(cs,radius*cu),ports.mul(hp,radius*cu)),axis=-1)
    v=np.stack((-cu,-ports.mul(cs,su),-ports.mul(hp,su)),axis=-1)
    data=raised.raised_port(warm,A,c,u,radius);data.update(Puuu=2*pu[2],Puuuu=6*pu[3],Vuuu=6*v[3])
    return data
class Ends:
    def __init__(self,scripts,ramp,coast,A,c,M):
        here=Path(__file__).resolve().parent
        self.warm=load(scripts/'6a65-geometry-cauchy-unit-t-warm.py','oblique_warm')
        self.raised=load(here/'2ecf-polar-raised-tail-tall-throat-source.py','oblique_raised')
        self.base=load(scripts/'6a65-geometry-nonfold-polar-connector.py','oblique_traces')
        self.master=self.warm.WarmMaster(ramp,coast,coast_length=.02);self.master._ports=self.warm.ports;self.master._warm=self.warm
        n=np.arange(M)*2*np.pi/M
        self.specs=[];self.clockMin=[]
        for side in (0,1):
            data=(self.base.higher_coast_port(self.master,.02,n) if side==0 else higher_raised(self.warm,self.raised,A,c,n))
            clock=self.base.endpoint_clock(data,n);profile=self.base.polar_profiles(clock)
            clocks=np.stack([clock[k] for k in ('phi','phis','phiss')])
            angle=clocks[0,0].copy()
            self.clockMin.append(float(np.min(clocks[0,1])))
            clocks[0,0]-=n;clocks[0,1]-=1
            self.specs.append((periodic_spline(n,clocks),{k:periodic_spline(angle,v) for k,v in profile.items()}))
    def positions(self,ns,u,b,S):
        L=S-b;t=(ns-b)/L
        mats=np.array([[self.warm.ports.hermite_weights(q,L,j) for j in range(3)] for q in t])
        ends=[]
        for spline,_ in self.specs:
            block=np.stack([spline(u,nu=j).T for j in range(3)],axis=1);block[0,0]+=u;block[0,1]+=1;ends.append(block)
        clock=np.einsum('nka,aju->nkju',mats,np.concatenate(ends))
        theta=clock[:,0,0];blocks=[]
        for _,material in self.specs:
            out={}
            for name,op in material.items():
                angle=(theta-op.x[0])%(2*np.pi)+op.x[0]
                out[name]=np.stack([op(angle,nu=i).transpose(0,2,1) for i in range(3)],axis=2)
            blocks.append(out)
        logs=np.concatenate([p['logrho'] for p in blocks],axis=1)
        q=np.einsum('nka,naju->nkju',mats,logs)
        return t,L,clock,q,blocks
def scoped_eval(t,L,clock,logs,ports,k,amp,n):
    th=clock[:,0,0];cost=np.cos(th);sint=np.sin(th)
    log=logs.copy();poly=64*Polynomial([0,1,-1])**3
    g0=sint**4;g1=4*sint**3*cost;g2=12*sint**2*cost**2-4*sint**4
    for ds in range(3):
        f=amp*poly.deriv(ds)(t)/L**ds
        for dt,g in enumerate((g0,g1,g2)):log[:,ds,dt]+=f[:,None]*g
    r=np.exp(log[:,0,0]);rs=r*log[:,1,0];rt=r*log[:,0,1]
    rss=r*(log[:,2,0]+log[:,1,0]**2);rst=r*(log[:,1,1]+log[:,1,0]*log[:,0,1]);rtt=r*(log[:,0,2]+log[:,0,1]**2)
    left,right=(p['z']-k*p['rho'] for p in ports)
    ctrl=[left[:,1],left[:,1]+L*left[:,2]/n,right[:,1]-L*right[:,2]/n,right[:,1]]
    inner=((n+1)*(right[:,0]-left[:,0])/L-sum(ctrl))/(n-3)
    q=left[:,0].copy()+L*t[:,None,None]*inner;qs=inner.copy();qss=np.zeros_like(qs)
    bern=lambda deg,i:comb(deg,i)*t**i*(1-t)**(deg-i) if 0<=i<=deg else np.zeros_like(t)
    for i,co in zip((0,1,n-1,n),ctrl):
        delta=co-inner
        q+=L*(betainc(i+1,n-i+1,t)/(n+1))[:,None,None]*delta
        qs+=bern(n,i)[:,None,None]*delta
        qss+=(n/L*(bern(n-1,i-1)-bern(n-1,i)))[:,None,None]*delta
    z=q[:,0]+k*r;zs=qs[:,0]+k*rs;zt=q[:,1]+k*rt
    zss=qss[:,0]+k*rss;zst=qs[:,1]+k*rst;ztt=q[:,2]+k*rtt
    es=np.stack([cost,sint,np.zeros_like(th)],axis=-1);et=np.stack([-sint,cost,np.zeros_like(th)],axis=-1)
    def vec(rr,rtan,vz):
        out=rr[...,None]*es+rtan[...,None]*et;out[:,:,2]+=vz;return out
    zero=np.zeros_like(th)
    X=vec(r,zero,z);Xs=vec(rs,zero,zs);Xt=vec(rt,r,zt);Xss=vec(rss,zero,zss);Xst=vec(rst,rs,zst);Xtt=vec(rtt-r,2*rt,ztt)
    ts,tu,tss,tsu,tuu=[clock[:,i,j,:,None] for i,j in ((1,0),(0,1),(2,0),(1,1),(0,2))]
    out=np.stack([X,Xs+Xt*ts,Xt*tu,Xss+2*Xst*ts+Xtt*ts**2+Xt*tss,Xst*tu+Xtt*ts*tu+Xt*tsu,Xtt*tu**2+Xt*tuu],axis=1)
    return out,float(min(v[:,0].min() for v in [inner,*ctrl])),float(qs[:,0].min()),float(tu.min())
def run(a):
    here=Path(__file__).resolve().parent
    base=load(here/'2ecf-polar-new-central-gap-compose.py','oblique_gapprepare')
    saved,de,full,caches,mods,*_=base.validate_prepared(a);ind=get(a.independent)
    basis=load(here/'2ecf-polar-fixed-prefix-position-basis.py','oblique_basis').restrict(full)[0]
    scan=load(here/'2ecf-polar-gap092-true-tail-amplitude-height.py','oblique_pointscan')
    area=load(a.scripts/'6a65-geometry-area-ratio-power-two.py','oblique_area')
    A,c=a.amplitude,a.flat;ep=Ends(a.scripts,a.ramp,a.coast,A,c,a.trace_nodes);stream=mods['stream']
    cfg=ep.raised.tall_config(stream.point.PointConfig)(**dict(de['pointConfig'],true_cuff_height=.415,height_maximum=.113))
    assert de['sourceIdentity']['sourceDefinition']['rampMasterSHA256']==sha(a.ramp) and de['sourceIdentity']['sourceDefinition']['coastMasterSHA256']==sha(a.coast)
    if a.mode=='select':
        groups={key:(obj.nodes,obj.u,obj.jets,obj.radius,saved['caches'][key]['weights']) for key,obj in caches.items()}
        params=[(k,bump,n) for k in (.55,.8) for bump in (0.,.12,.24,-.12) for n in (12,31)]
    else:
        s=get(a.selection);assert s['entrySHA256']==sha(__file__) and s['endParameters']==[A,c]
        params=[tuple(s['selected']['params'])]
        assert all(sha(v)==ind['SHA256'][key] for key,v in ind['files'].items())
        groups={'independent':(np.array(ind['physicalNodes']),np.array(ind['angles']),np.load(ind['files']['jets'],mmap_mode='r'),np.load(ind['files']['radius'],mmap_mode='r'),None)}
    out=dict(schema='new-gap092-true-raised-ends-oblique-height-and-actual-radius-bump-v1',entrySHA256=sha(__file__),preparedSHA256=sha(a.prepared),
        independentSHA256=sha(a.independent),rampSHA256=sha(a.ramp),coastSHA256=sha(a.coast),endParameters=[A,c],mode=a.mode,
        traceNodes=a.trace_nodes,endpointPhiUFiniteMin=ep.clockMin,results={},finiteOnly=True,ownAccepts=0)
    for key,(ns,u,src,rad,w) in groups.items():
        j=src.copy();idx=np.flatnonzero((ns>=basis.c)&(ns<=basis.end))
        for i in np.flatnonzero(ns>basis.end):
            q=ep.raised.raised_port(ep.warm,A,c,u,rad[i,0]);j[i]=np.stack([q[name] for name in ('P','V','Pu','A','Vu','Puu')])
        # The 3 angular jets of the endpoint functions are interpolated together; differentiate that same spline.
        packs=[]
        for start in range(0,len(idx),16):
            ii=idx[start:start+16];packs.append((ii,ep.positions(ns[ii],u,basis.c,basis.end)))
        ops=[]
        for k,bump,n in params:
            ctrl=qs=clock=10.
            for ii,pack in packs:
                new,v,m,d=scoped_eval(*pack,k,bump,int(n));j[ii]=new
                ctrl=min(ctrl,v);qs=min(qs,m);clock=min(clock,d)
            val=scan.evaluate(stream,stream.point,area,j,rad,ns,u,cfg,w)
            val.update(params=[k,bump,n],minimumVelocityControl=ctrl,minimumActualObliqueSpeed=qs,minimumThetaU=clock)
            ops.append(val);print(key,k,bump,n,ctrl,qs,val['metric'],val['curvature'],val['held'],val['R2'],flush=True)
        out['results'][key]=ops
    if a.mode=='select':
        out['rows']=[]
        for x,y in zip(out['results']['training'],out['results']['observer']):
            assert x['params']==y['params'] and x['actualRows']+y['actualRows']==4291840
            out['rows'].append(dict(params=x['params'],R2=x['R2']+y['R2'],metric=max(x['metric'],y['metric']),
                curvature=max(x['curvature'],y['curvature']),held=min(x['held'],y['held']),minControl=min(x['minimumVelocityControl'],y['minimumVelocityControl'])))
        feasible=[v for v in out['rows'] if v['minControl']>0];out['selected']=min(feasible or out['rows'],key=lambda v:v['R2'])
    write(a.output,out)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('prepared','scripts','ramp','coast','independent','selection','output'):p.add_argument('--'+k,type=Path)
    p.add_argument('--mode',choices=['select','observe'],required=True);p.add_argument('--trace-nodes',type=int,default=1024)
    p.add_argument('--amplitude',type=float,default=.4);p.add_argument('--flat',type=float,default=.56);run(p.parse_args())
