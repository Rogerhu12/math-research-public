#!/usr/bin/env python3
"""Independent cut-curve/height holonomy audit of saved Fourier-PPoly traces.
No solver or tail construction is called. This is sampled numerical evidence.
"""
import argparse, gzip, hashlib, json, math
from pathlib import Path
import numpy as np
from scipy.interpolate import PPoly
from scipy.optimize import brentq

def load(path):
    with gzip.open(path,'rt') as h:d=json.load(h)
    arrays=[]
    hashes={path.name:hashlib.sha256(path.read_bytes()).hexdigest()}
    for row in d['pp_coefficient_chunks']:
        p=path.parent/row['file']; hashes[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
        if hashes[p.name]!=row['sha256']:raise ValueError('chunk changed')
        with gzip.open(p,'rb') as h:arrays.append(np.load(h,allow_pickle=False))
    c=np.concatenate(arrays,axis=2)
    return d,PPoly.construct_fast(c,np.array(d['mesh']),extrapolate=True,axis=1),hashes

def basis(M,theta):
    er=np.stack([np.cos(theta),np.sin(theta),np.zeros_like(theta)],axis=-1)
    et=np.stack([-np.sin(theta),np.cos(theta),np.zeros_like(theta)],axis=-1)
    ez=np.tile([0.,0.,1.],(len(theta),1))
    B=np.zeros((3*M+1,len(theta),3));D=B.copy();DD=B.copy()
    B[0]=er;D[0]=et;DD[0]=-er
    for j in range(M):
        m=2*j+2;co=np.cos(m*theta)[:,None];si=np.sin(m*theta)[:,None]
        r=j+1;t=M+j+1;z=2*M+j+1
        B[r]=co*er;D[r]=co*et-m*si*er;DD[r]=-(1+m*m)*co*er-2*m*si*et
        B[t]=si*et;D[t]=-si*er+m*co*et;DD[t]=-(1+m*m)*si*et-2*m*co*er
        B[z]=co*ez;D[z]=-m*si*ez;DD[z]=-m*m*co*ez
    return B,D,DD

def run(path,N):
    d,p,hashes=load(path);M=d['config']['modes'];q=d['gauge_amplitude'];end=d['meridian_length']
    cfg=d['frozen_profile'];r=cfg['cut_radius'];w=cfg['cut_slope'];E=1+w*w
    sigma=-1. if r<1 else 1.;ap=sigma/math.sqrt(E);wr=-7*w/r;app=-w*wr/E**2
    th=2*np.pi*np.arange(N)/N;B,D,DD=basis(M,th)
    C=q*p(end);Cp=q*p(end,1);Cpp=q*p(end,2);C[0]+=r;Cp[0]+=ap;Cpp[0]+=app
    F=C@B.reshape(3*M+1,-1);F=F.reshape(N,3)
    dt=np.einsum('j,jkl->kl',C,D);dtt=np.einsum('j,jkl->kl',C,DD)
    lam=np.linalg.norm(dt,axis=1);T=dt/lam[:,None]
    normal_vec=dtt-np.sum(dtt*T,axis=1)[:,None]*T
    nn=np.linalg.norm(normal_vec,axis=1);normal=normal_vec/nn[:,None];kap=nn/lam**2
    alpha=-ap/(r*kap);beta=np.sqrt(1-alpha**2);V=alpha[:,None]*normal+beta[:,None]*np.cross(T,normal)
    mean_s=float(np.mean(V[:,2]));iz=2*M+1
    ut=sigma*dt[:,2];utt=sigma*dtt[:,2]
    nonmean_ur=math.sqrt(E)*np.einsum('j,jkl->kl',Cp,B)[:,2]
    def flux(mean):
        ur=mean+nonmean_ur;S=r*r-ut*ut;Delta=E*S-r*r*ur*ur
        if min(Delta)<=0:raise ValueError('projection domain')
        omega=r*r*(r+ur*utt-ut*ut/r)/(S*np.sqrt(Delta))
        return float(np.mean(omega))
    bracket=[w-.05,w+.05];mr=brentq(lambda m:flux(m)-1,*bracket,xtol=1e-15)
    actual_m=math.sqrt(E)*mean_s
    hv=1e-5
    planar_dt=dt[:,:2];planar_dd=dtt[:,:2]
    winding=np.mean((planar_dt[:,0]*planar_dd[:,1]-planar_dt[:,1]*planar_dd[:,0])/np.sum(planar_dt**2,axis=1))
    return dict(checkpoint=str(path),scope='Independent sampled port geometry; no nonlinear DN or infinite-tail certificate',N=N,M=M,r=r,w=w,sigma=sigma,
        source_sha256=hashes,
        projected_curve_winding=winding,
        angular_metric_error=float(np.max(abs(lam**2/r**2-1))),
        actual_mean_s=mean_s,unperturbed_mean_s=w/math.sqrt(E),actual_mean_correction_s=mean_s-w/math.sqrt(E),
        actual_positive_tail_mean_r=actual_m,flux_at_actual_mean=flux(actual_m),
        flux_root_mean_r=mr,flux_root_mean_correction_r=mr-w,
        flux_root_minus_actual=mr-actual_m,
        flux_derivative_at_root=(flux(mr+hv)-flux(mr-hv))/(2*hv),
        flux_with_zero_mean_correction=flux(w),
        max_tail_nonmean_height=float(np.max(abs(sigma*F[:,2]))),
        max_tail_nonmean_radial_slope=float(np.max(abs(nonmean_ur))),
        prefix_mean_first_jet_if_unreflected_tail=w*ap,
        background_first_jet_mismatch_if_unreflected=mean_s-w*ap,
        terminal_noncircle_modes=C[iz:].tolist())

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('checkpoint',type=Path);p.add_argument('--out',type=Path,required=True);p.add_argument('--angles',type=int,nargs='+',default=[1024,2048]);a=p.parse_args()
    rows=[run(a.checkpoint,N) for N in a.angles]
    a.out.write_text(json.dumps(rows,indent=2)+'\n')
    print(json.dumps([{k:v for k,v in row.items() if k not in ['source_sha256','terminal_noncircle_modes','checkpoint']} for row in rows],indent=2))
