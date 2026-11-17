#!/usr/bin/env python3
"""Read an actual accepted prefix cut in canonical material angle.

This converts the full physical-angle Fourier state and saved radial velocity,
not an ellipse surrogate, to the height/P/K interface of the tail equations.
All reported extrema, omitted spectra and means are numerical diagnostics.
The raw trace output belongs outside the repository.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np
from parallel_20261117_profile import Profile


def main(args):
    raw=args.input.read_bytes(); data=json.loads(gzip.decompress(raw))
    if not data.get('success'):raise ValueError('Need an accepted prefix')
    M=data['M']; freq=2*np.arange(1,M+1,dtype=float)
    y=np.asarray(data['states'][-1]); ys=np.asarray(data['rhs'][-1])
    core=np.asarray(data['core']['coefficients'])
    rc=(1-freq**2)*core
    N=args.angles
    if N%2 or N<4*max(M,args.modes)+4:raise ValueError('Insufficient even angular grid')
    theta=2*np.pi*np.arange(N)/N
    lo=np.zeros(N);hi=np.full(N,2*np.pi);phi=theta.copy()
    for iteration in range(50):
        phase=phi[:,None]*freq;sn=np.sin(phase);cs=np.cos(phase)
        residual=phi+sn@(rc/freq)-theta;rho=1+cs@rc
        if np.min(rho)<=0:raise ValueError('Sampled material map is not monotone')
        if np.max(abs(residual))<32*np.finfo(float).eps:break
        pos=residual>0;hi=np.where(pos,phi,hi);lo=np.where(pos,lo,phi)
        trial=phi-residual/rho
        phi=np.where((trial>=lo)&(trial<=hi),trial,(lo+hi)/2)
    else:raise RuntimeError('Material angle inversion did not converge')
    s=float(data['mesh'][-1])
    geometry=data.get('fixed_scalar_profile',data.get('inherited_profile'))['geometry']
    origin=float(data.get('analytic_extension_origin',data.get('extension_scalar',{}).get('start',s)))
    profile=Profile(geometry,origin);r,ap,app=profile(s)
    if not 0<ap<1:raise ValueError('This trace convention requires 0<a_prime<1')
    n=np.sqrt(1-ap*ap);w=n/ap;wr=-app/(ap**3*n)
    phase=phi[:,None]*freq;sn=np.sin(phase);cs=np.cos(phase)
    rho=1+cs@rc;rho_phi=-sn@(freq*rc)
    z=y[2*M+1:];zs=ys[2*M+1:]
    height=z[0]+cs@z[1:]
    hphi=-sn@(freq*z[1:]);hpp=-cs@(freq**2*z[1:])
    hs=zs[0]+cs@zs[1:];hsphi=-sn@(freq*zs[1:])
    P=hphi/(rho*r*w);K=hs/n-1
    T=(hpp*rho-hphi*rho_phi)/(rho**3*r*w)
    U=hsphi/(n*rho)-P
    zeta=w*w;E=1+zeta;A=2*K+K*K+E*P*P
    S=1-zeta*P*P;D=1-zeta*A;L=1+K+E*T
    branch_N=1+zeta*(1+K)*T/S
    if min(S.min(),D.min())>0:
        q=np.sqrt(D);B=A/(q*(1+q))+(1+K)*T/(S*q)
        mean=float(np.mean(B))
    else:mean=None
    phat=np.fft.rfft(P)/N;khat=np.fft.rfft(K)/N;hhat=np.fft.rfft(height)/N
    modes=2*np.arange(1,args.modes+1)
    pc=-2*phat[modes].imag;kc=2*khat[modes].real;hc=2*hhat[modes].real
    def omitted(spec):
        keep=np.zeros_like(spec,dtype=bool);keep[0]=True;keep[modes]=True
        return float(2*np.sum(abs(spec[~keep])))
    pp=np.sin(theta[:,None]*modes)@pc
    kk=float(khat[0].real)+np.cos(theta[:,None]*modes)@kc
    tt=np.cos(theta[:,None]*modes)@(modes*pc)
    AA=2*kk+kk*kk+E*pp*pp;SS=1-zeta*pp*pp;DD=1-zeta*AA;LL=1+kk+E*tt
    qq=np.sqrt(DD)
    bm=AA/(qq*(1+qq))+(1+kk)*tt/(SS*qq)
    report=dict(scope=__doc__,input_sha256=hashlib.sha256(raw).hexdigest(),
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                s=s,angles=N,modes=args.modes,physical_modes=M,
                r=float(r),a_prime=float(ap),a_second=float(app),w=float(w),w_r=float(wr),
                material_angle_residual_max=float(np.max(abs(phi+np.sin(phi[:,None]*freq)@(rc/freq)-theta))),
                height_mean=float(hhat[0].real),height_cos_coefficients=hc.tolist(),
                P_sin_coefficients=pc.tolist(),K_mean=float(khat[0].real),K_cos_coefficients=kc.tolist(),
                full_sampled=dict(P_max=float(np.max(abs(P))),K_max=float(np.max(abs(K))),
                                  T_max=float(np.max(abs(T))),U_max=float(np.max(abs(U))),
                                  S_min=float(S.min()),D_min=float(D.min()),L_min=float(L.min()),
                                  y_min=float((1+K).min()),N_min=float(branch_N.min()),mean=mean),
                projected_sampled=dict(P_max=float(np.max(abs(pp))),K_max=float(np.max(abs(kk))),
                                       S_min=float(SS.min()),D_min=float(DD.min()),L_min=float(LL.min()),
                                       mean=float(np.mean(bm))),
                omitted_discrete_l1=dict(P=omitted(phat),K=omitted(khat),height=omitted(hhat)))
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if not k.endswith('coefficients')},indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--modes',type=int,default=112);p.add_argument('--angles',type=int,default=8192)
    main(p.parse_args())
