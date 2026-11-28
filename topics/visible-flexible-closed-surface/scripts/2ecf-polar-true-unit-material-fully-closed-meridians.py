#!/usr/bin/env python3
"""Construct actual C2 material meridians with true endpoint two-jets, exact common arclength and three-dimensional endpoint closure."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
import numpy as np
from scipy.special import logsumexp
def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
here=Path(__file__).parent
base=module(here/'2ecf-polar-material-curve-coupled-spherical-design.py','exact_meridian_ports')
def directions():
    return np.array([(x,y,z) for x in range(-2,3) for y in range(-2,3) for z in range(-2,3) if max(abs(x),abs(y),abs(z))==2],float)
class Segment:
    def __init__(self,a,b,k=None,duration=1.,mirror=False):
        self.a=a;self.b=b;self.k=np.zeros(3) if k is None else k
        self.duration=duration;self.mirror=mirror
    def tangent(self,t):
        t=np.asarray(t);q=1-t if self.mirror else t
        blend=q**3*(10+q*(-15+6*q));db=30*q*q*(1-q)**2
        bump=q*(1-q)**3;d_bump=(1-q)**2*(1-4*q)
        raw=self.a+blend[...,None]*(self.b-self.a)+bump[...,None]*self.k
        der=db[...,None]*(self.b-self.a)+d_bump[...,None]*self.k
        norm=np.linalg.norm(raw,axis=-1)[...,None];w=raw/norm
        ws=(der-w*np.sum(w*der,axis=-1,keepdims=True))/norm
        return w,ws*((-1 if self.mirror else 1)/self.duration)
    def displacement(self,t,quadrature):
        x,w=quadrature
        vals=self.tangent(t*x)[0]
        return t*self.duration*(w@vals)

class Catalogue:
    def __init__(self,L,quadrature):
        self.L=L;self.q=quadrature;self.ez=np.array((0.,0.,1.))
        self.d=directions();self.d/=np.linalg.norm(self.d,axis=-1)[:,None]
        self.collar=L/512;self.transitions=L/128
        self.dwell=L-2*self.collar-self.transitions
        self.events=[]
        for i,d in enumerate(self.d):
            via=[np.array((1.,0.,0.))] if d[2]==-1 else []
            seq=[self.ez,*via,d]
            for a,b in zip(seq,seq[1:]):self.events.append(('arc',a,b))
            self.events.append(('dwell',i))
            for a,b in zip(seq[:0:-1],seq[-2::-1]):self.events.append(('arc',a,b))
        count=sum(k[0]=='arc' for k in self.events)
        self.dt=self.transitions/count;self.arc_offset=np.zeros(3);self.prepared=[]
        for event in self.events:
            if event[0]=='arc':
                seg=Segment(*event[1:],duration=self.dt)
                dq=seg.displacement(1.,self.q);self.arc_offset+=dq;self.prepared.append(('arc',seg,dq))
            else:self.prepared.append(event)

    def construct(self,position,velocity,acceleration):
        dl=self.collar
        left=Segment(velocity[0],self.ez,k=dl*acceleration[0],duration=dl)
        right=Segment(velocity[1],self.ez,k=-dl*acceleration[1],duration=dl,mirror=True)
        dlft=left.displacement(1.,self.q);drgt=right.displacement(1.,self.q)
        m=(position[1]-position[0]-dlft-drgt-self.arc_offset)/self.dwell
        lam=np.zeros(3)
        for _ in range(60):
            value=self.d@lam
            prob=np.exp(value-logsumexp(value));mean=prob@self.d
            r=mean-m
            if np.linalg.norm(r)<4e-14:break
            centered=self.d-mean;H=centered.T@(prob[:,None]*centered)
            d=np.linalg.solve(H,r);alpha=1.
            while alpha>1e-10:
                trial=lam-alpha*d;soft=self.d@trial
                rr=np.exp(soft-logsumexp(soft))@self.d-m
                if np.linalg.norm(rr)<np.linalg.norm(r):break
                alpha/=2
            lam-=alpha*d
        else:raise ArithmeticError('Entropy moment did not reach closure')
        segs=[(left,dlft)]
        for e in self.prepared:
            if e[0]=='arc':segs.append((e[1],e[2]))
            else:
                i=e[1];v=self.d[i];h=self.dwell*prob[i]
                segs.append((Segment(v,v,duration=h),h*v))
        segs.append((right,drgt))
        starts=[0.];P=[position[0]]
        for seg,disp in segs:
            starts.append(starts[-1]+seg.duration);P.append(P[-1]+disp)
        def evaluate(s):
            if s<=0:idx=0;t=0.
            elif s>=self.L:idx=len(segs)-1;t=1.
            else:
                idx=int(np.clip(np.searchsorted(starts,s,side='right')-1,0,len(segs)-1))
                t=np.clip((s-starts[idx])/segs[idx][0].duration,0,1)
            seg=segs[idx][0];v,a=seg.tangent(t)
            return P[idx]+seg.displacement(t,self.q),v,a
        stats=dict(mean=float(np.linalg.norm(m)),residual=float(np.linalg.norm(r)),positionClosure=float(np.linalg.norm(P[-1]-position[1])),minimumWeight=float(min(prob)),durationError=float(abs(starts[-1]-self.L)))
        return evaluate,stats

def run(args):
    en=module(here/'2ecf-polar-returning-bend-full-ray-surface.py','explicit_returning_R282')
    ends=en.Ends(args.scripts,args.ramp,args.coast,args.peak,args.terminal,512)
    report=base.read(args.slack)
    from fractions import Fraction as Q
    assert Q(report['maximumRequiredNormalizedMean'])<Q(89,100)
    L=float(Q(report['actualConnectorLength']))
    x,w=np.polynomial.legendre.leggauss(48);cat=Catalogue(L,((x+1)/2,w/2))
    u=2*np.pi*(np.arange(args.angles)+.375)/args.angles
    pair=base.ports(ends,args.peak,args.terminal,u)
    po,ve,ac=[np.stack([base.local(d[k],u) for d in pair],axis=1) for k in ('P','V','A')]
    maxima=dict(unitError=0.,P=0.,V=0.,A=0.,closure=0.,length=0.,mean=0.)
    minweight=1.;a_hash=hashlib.sha256();rad=np.linspace(0,L,args.radials)
    for i in range(len(u)):
        fn,st=cat.construct(po[i],ve[i],ac[i])
        for s in rad:
            p,v,a=fn(s);a_hash.update(np.stack([p,v,a]).astype('<f8').tobytes())
            maxima['unitError']=max(maxima['unitError'],abs(np.linalg.norm(v)-1))
        for j,s in enumerate((0.,L)):
            for k,g,ref in zip(('P','V','A'),fn(s),(po,ve,ac)):
                maxima[k]=max(maxima[k],float(np.linalg.norm(g-ref[i,j])))
        minweight=min(minweight,st['minimumWeight'])
        for k,key in [('closure','positionClosure'),('length','durationError'),('mean','mean')]:maxima[k]=max(maxima[k],st[key])
    assert maxima['P']<1e-11 and maxima['V']<1e-9 and maxima['A']<1e-8 and maxima['unitError']<1e-12
    base.stores(args.output,dict(entrySHA256=base.sha(__file__),rigorousSlackSHA256=base.sha(args.slack),rampSHA256=base.sha(args.ramp),coastSHA256=base.sha(args.coast),portSourceSHA256=base.sha(en.__file__),basisCount=len(cat.d),transitionCount=sum(e[0]=='arc' for e in cat.events),materialAngles=args.angles,physicalRadials=args.radials,geometryDigest=a_hash.hexdigest(),sampledMinimumPositiveWeight=minweight,floatingMaxima=maxima,peak=args.peak,terminal=args.terminal))
    print(maxima,minweight)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','ramp','coast','slack','output'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--angles',type=int,default=128);p.add_argument('--radials',type=int,default=129)
    p.add_argument('--peak',type=float,default=.48);p.add_argument('--terminal',type=float,default=-.2)
    run(p.parse_args())
