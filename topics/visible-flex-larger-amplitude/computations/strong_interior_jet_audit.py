#!/usr/bin/env python3
"""Audit the actual saved C2 polynomial at nodes, midpoints and both jet lobes.

Every reported quantity is a finite spatial sample, not a continuous bound.
The saved polynomial's actual second derivatives are authoritative; pointwise
PDE derivatives are compared, never substituted. No metric or map is changed.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for n in ('input','source-topic','port','out'):p.add_argument('--'+n,type=Path,required=True)
    p.add_argument('--angular',type=int,default=512)
    p.add_argument('--batch',type=int,default=16)
    p.add_argument('--radial',type=int,default=801)
    a=p.parse_args();start=time.time();source_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    input_hash=hashlib.sha256(a.input.read_bytes()).hexdigest()
    pb=load('strong_audit_pullback',P/'geometric-checkpoint-core-pullback.py')
    cv=load('strong_audit_curvature',P/'alternative-neck-curvature-map.py')
    saved,_=pb.load_saved(a.input,a.source_topic,a.port,angular=a.angular)
    if not saved.rec.get('solver_success'):raise ValueError('Successful saved prefix required')
    f=saved.flow;N=a.angular;B,B1,B2=f.basis(N);x=saved.sol.x
    xi=np.array([.5,(3-np.sqrt(3))/6,(3+np.sqrt(3))/6])
    ss=np.unique(np.r_[x,(x[:-1,None]+np.diff(x)[:,None]*xi).ravel(),f.breaks,np.linspace(0,f.end,a.radial)])
    top={};rows=[]
    segments=[];pre=f._alternative_neck
    for i,seg in enumerate(pre.segments):segments.append(dict(index=i,label=cv.label(seg,pre.loop_begin),lo=seg['s0'],hi=seg['s1']))
    for i,seg in enumerate(f.bridge.segments):segments.append(dict(index=len(pre.segments)+i,label=cv.label(seg,pre.loop_begin,True),lo=pre.end+seg['s0'],hi=pre.end+seg['s1']))
    def record(name,values,s):
        flat=int(np.argmax(values));row,col=np.unravel_index(flat,values.shape)
        val=float(values[row,col])
        if name not in top or val>top[name]['value']:
            si=float(s[row]);idx=min(len(x)-2,max(0,int(np.searchsorted(x,si,side='right')-1)))
            seg=next((v for v in segments if v['lo']-1e-12<=si<=v['hi']+1e-12),segments[-1])
            top[name]=dict(value=val,s=si,psi=float(col*2*np.pi/N),segment=seg['label'],interval=idx,interval_width=float(x[idx+1]-x[idx]),normalized_interval_position=float((si-x[idx])/(x[idx+1]-x[idx])))
    for first in range(0,len(ss),a.batch):
        s=ss[first:first+a.batch];Y=saved.sol.sol(s);Yp=saved.sol.sol(s,1);Ypp=saved.sol.sol(s,2)
        aa,ap,app=f.profile(s);fr,Fsp,dW=f.velocity_s(s,Y,Yp,B1,B2);g=fr['geo'];rho=g['rho'];v=g['v']
        Fsc=g['s1']+saved.q*f.values(Yp,B);Fsc[:,:,2]+=np.mean(fr['V'][:,:,2],axis=1)[:,None]
        Fssc=g['s2']+saved.q*f.values(Ypp,B);Fssc[:,:,2]+=np.mean(dW[:,:,2],axis=1)[:,None]
        Fs=Fsc-v[:,:,None]*fr['d'];Ft=fr['d']/rho[:,:,None]
        Ftt=fr['dd']/rho[:,:,None]**2-fr['d']*g['rhop'][:,:,None]/rho[:,:,None]**3
        Fst=(Fsp-g['vp'][:,:,None]*fr['d']-v[:,:,None]*fr['dd'])/rho[:,:,None]
        Fss=Fssc-2*v[:,:,None]*Fsp+v[:,:,None]**2*fr['dd']+(v*g['vp']-g['vs'])[:,:,None]*fr['d']
        E=np.sum(Fs*Fs,axis=2);F=np.sum(Fs*Ft,axis=2);G=np.sum(Ft*Ft,axis=2)
        errors=np.stack((E-1,F/aa[:,None],G/aa[:,None]**2-1),axis=2)
        metric=np.max(abs(errors),axis=2);kap=cv.principal(Fs,Ft,Fss,Fst,Ftt)[0]
        Hst=(Fst-ap[:,None,None]/aa[:,None,None]*Ft)/aa[:,None,None]
        Htt=(Ftt+(aa*ap)[:,None,None]*Fs)/aa[:,None,None]**2
        gram=np.eye(3)[None,None,:,:]-Fs[:,:,:,None]*Fs[:,:,None,:]-(Ft/aa[:,None,None])[:,:,:,None]*(Ft/aa[:,None,None])[:,:,None,:]
        tensor=.5*(Fss[:,:,:,None]*Htt[:,:,None,:]+Htt[:,:,:,None]*Fss[:,:,None,:])-Hst[:,:,:,None]*Hst[:,:,None,:]+(app/aa)[:,None,None,None]*gram
        darboux=np.linalg.norm(tensor,axis=(2,3));flow=np.linalg.norm(Fs-fr['Vnormal'],axis=2)
        projected=f.project(dW-g['s2'],B)/saved.q
        second_diff=saved.q*f.values(Ypp-projected,B)
        second=np.linalg.norm(second_diff,axis=2)
        for name,values in [('metric_component_max',metric),('kappa',kap),('darboux_frobenius',darboux),('flow_defect',flow),('actual_vs_PDE_second',second)]:record(name,values,s)
        metric_l1=np.max(np.sum(abs(np.fft.fft(errors,axis=1)/N),axis=1),axis=1)
        ft=np.fft.fft(tensor,axis=1)/N;dar_l1=np.sum(np.linalg.norm(ft,axis=(2,3)),axis=1)
        for name,values in [('metric_fourier_l1',metric_l1),('darboux_fourier_l1',dar_l1)]:
            idx=int(np.argmax(values));val=float(values[idx])
            if name not in top or val>top[name]['value']:top[name]=dict(value=val,s=float(s[idx]))
    out=dict(scope=__doc__,input=str(a.input),input_sha256=input_hash,source_sha256=source_hash,config=dict(angular=N,radial=a.radial,batch=a.batch,interior_fractions=xi.tolist()),sample_count=len(ss),modes=saved.M,q=saved.q,physical_metric_sha256=hashlib.sha256(json.dumps(saved.rec['frozen_profile'],sort_keys=True).encode()).hexdigest(),top=top,seconds=time.time()-start)
    a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
