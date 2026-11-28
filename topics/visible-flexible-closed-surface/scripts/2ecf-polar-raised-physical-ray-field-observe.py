#!/usr/bin/env python3
"""Compose a full radial-Hermite/cosine ray surface with its endpoint clock and measure actual Cartesian jets."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np

def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
class PhysicalRays:
    def __init__(self,field,ends):
        a=np.load(field);self.coeff=a['coeff'];self.knots=a['knots'];self.modes=a['modes']
        self.ends=ends
    def clock(self,ns,u):
        b,S=self.knots[[0,-1]];L=S-b
        mats=np.array([[self.ends.warm.ports.hermite_weights((s-b)/L,L,j) for j in range(3)] for s in ns])
        rows=[]
        for op,_ in self.ends.specs:
            q=np.stack([op(u,nu=j).T for j in range(3)],axis=1)
            q[0,0]+=u;q[0,1]+=1;rows.append(q)
        return np.einsum('nka,aju->nkju',mats,np.concatenate(rows))
    def position(self,ns,u):
        ck=self.clock(ns,u);th=ck[:,0,0];ce=np.cos(th);sn=np.sin(th);M=self.modes
        cell=np.clip(np.searchsorted(self.knots,ns,side='right')-1,0,len(self.knots)-2)
        h=self.knots[cell+1]-self.knots[cell];t=(ns-self.knots[cell])/h
        mats=np.array([[self.ends.warm.ports.hermite_weights(x,hh,j) for j in range(3)] for x,hh in zip(t,h)])
        edge=[]
        for side in (0,1):
            node=cell+side;arr=np.empty((len(ns),3,3,len(u),2))
            coeff=self.coeff[:,node,:,:].transpose(1,0,2,3)
            for j in range(3):
                angular=np.cos(th[:,:,None]*M[None,None,:]+j*np.pi/2)*M**j
                arr[:,:,j,:,:]=np.einsum('num,nmcv->ncuv',angular,coeff)
            ii=np.flatnonzero(node==(0 if side==0 else len(self.knots)-1))
            for i in ii:
                for zz,key in enumerate(('logrho','z')):
                    f=self.ends.specs[side][1][key];a=(th[i]-f.x[0])%(2*np.pi)+f.x[0]
                    for j in range(3):arr[i,:,j,:,zz]=f(a,nu=j).T
            edge.append(arr)
        jets=np.einsum('nka,najuv->nkjuv',mats,np.concatenate(edge,axis=1))
        g=jets[:,:,:,:,0];v=jets[:,:,:,:,1];r=np.exp(g[:,0,0])
        rs=r*g[:,1,0];rt=r*g[:,0,1]
        rss=r*(g[:,2,0]+g[:,1,0]**2);rst=r*(g[:,1,1]+g[:,1,0]*g[:,0,1]);rtt=r*(g[:,0,2]+g[:,0,1]**2)
        def vec(rad,tan,z):return np.stack([rad*ce-tan*sn,rad*sn+tan*ce,z],axis=-1)
        zero=np.zeros_like(r)
        X=vec(r,zero,v[:,0,0]);Xs=vec(rs,zero,v[:,1,0]);Xt=vec(rt,r,v[:,0,1])
        Xss=vec(rss,zero,v[:,2,0]);Xst=vec(rst,rs,v[:,1,1]);Xtt=vec(rtt-r,2*rt,v[:,0,2])
        ts,tu,tss,tsu,tuu=[ck[:,i,j,:,None] for i,j in ((1,0),(0,1),(2,0),(1,1),(0,2))]
        return np.stack([X,Xs+Xt*ts,Xt*tu,Xss+2*Xst*ts+Xtt*ts**2+Xt*tss,Xst*tu+Xtt*ts*tu+Xt*tsu,Xtt*tu**2+Xt*tuu],axis=1)
def run(a):
    here=Path(__file__).parent
    ob=load(here/'2ecf-polar-raised-monotone-oblique-connector.py','actual_ray_endpoints')
    src=load(here/'2ecf-polar-new-central-gap-compose.py','actual_ray_original')
    saved,de,full,caches,mods,*_=src.validate_prepared(a)
    ind=read(a.independent);r=read(a.design)
    assert r['fieldSHA256']==sha(a.field) and r['rampSHA256']==sha(a.ramp) and r['coastSHA256']==sha(a.coast)
    ends=ob.Ends(a.scripts,a.ramp,a.coast,r['amp'],r['flat'],a.trace_nodes);ray=PhysicalRays(a.field,ends)
    scan=load(here/'2ecf-polar-gap092-true-tail-amplitude-height.py','actual_ray_scan')
    area=load(a.scripts/'6a65-geometry-area-ratio-power-two.py','actual_ray_area')
    stream=mods['stream'];cfg=ends.raised.tall_config(stream.point.PointConfig)(**dict(de['pointConfig'],true_cuff_height=.415,height_maximum=.113))
    b,S=ray.knots[[0,-1]];basis=load(here/'2ecf-polar-fixed-prefix-position-basis.py','actual_ray_basis').restrict(full)[0]
    assert b==basis.c and S==basis.end
    groups={k:(c.nodes,c.u,c.jets,c.radius,saved['caches'][k]['weights']) for k,c in caches.items()}
    assert all(sha(v)==ind['SHA256'][k] for k,v in ind['files'].items())
    groups['independent']=(np.array(ind['physicalNodes']),np.array(ind['angles']),np.load(ind['files']['jets'],mmap_mode='r'),np.load(ind['files']['radius'],mmap_mode='r'),None)
    result={}
    for k,(ns,u,source,rad,w) in groups.items():
        j=source.copy();ii=np.flatnonzero((ns>=b)&(ns<=S))
        for jj in range(0,len(ii),12):
            ids=ii[jj:jj+12];j[ids]=ray.position(ns[ids],u)
        for i in np.flatnonzero(ns>S):
            port=ends.raised.raised_port(ends.warm,r['amp'],r['flat'],u,rad[i,0])
            j[i]=np.stack([port[k] for k in ('P','V','Pu','A','Vu','Puu')])
        tail=ends.raised.raised_port(ends.warm,r['amp'],r['flat'],u,.8)
        # Compare against the original endpoint providers, including angular and mixed derivatives.
        exactL=ends.base.higher_coast_port(ends.master,.02,u)
        ports=np.stack([np.stack([port[k] for k in ('P','V','Pu','A','Vu','Puu')]) for port in (exactL,tail)])
        endpointErr=np.abs(ray.position(np.array([b,S]),u)-ports).max(axis=(2,3))
        val=scan.evaluate(stream,stream.point,area,j,rad,ns,u,cfg,w);val['endpointSixJetMaxErrors']=endpointErr.tolist()
        result[k]=val;print(k,val['metric'],val['curvature'],val['held'],val['R2'],endpointErr.max(),flush=True)
    report=dict(schema='R273-fixed-speed-physical-ray-complete-Cartesian-observations-v1',entrySHA256=sha(__file__),
        fieldSHA256=sha(a.field),designSHA256=sha(a.design),preparedSHA256=sha(a.prepared),independentSHA256=sha(a.independent),
        traceNodes=a.trace_nodes,results=result,ownAccepts=0,completeG10R2=result['training']['R2']+result['observer']['R2'],finiteOnly=True)
    assert result['training']['actualRows']+result['observer']['actualRows']==4291840
    with a.output.open('x') as f:json.dump(report,f,indent=2);f.write('\n')
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','ramp','coast','field','design','prepared','independent','output'):p.add_argument('--'+k,required=True,type=Path)
    p.add_argument('--trace-nodes',type=int,default=2048);run(p.parse_args())
