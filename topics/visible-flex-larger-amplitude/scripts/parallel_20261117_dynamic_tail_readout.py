#!/usr/bin/env python3
"""Read actual interpolant derivatives and retract its sampled mean once.

The retracted field is a new readout candidate.  Its P and nonzero K modes
are the accepted interpolant's actual values and derivatives.  Only the
zero-mode value is solved here, then its derivative follows literal implicit
differentiation.  This is not a replacement of derivatives by the ODE RHS.
"""
import argparse,gzip,hashlib,json
from pathlib import Path
import numpy as np
from scipy.interpolate import CubicHermiteSpline
from parallel_20261117_dynamic_tail import Background,DynamicMean


def retract_jet(q,y,dy,s,ell,z):
    v=y.copy();iterations=0
    for iterations in range(6):
        _,d=q.evaluate(v,s,ell,z,True)
        correction=d['mean']/d['mu'];v[-1]-=correction
        if np.max(abs(correction))<2e-17:break
    P,T,K,_=q.fields(v);E=1+z;A=2*K+K*K+E*P*P;S=1-z*P*P;D=1-z*A
    Q=np.sqrt(D);yy=1+K;L=yy+E*T;N=1+z*yy*T/S
    BP=E*P*N/Q**3+2*z*yy*T*P/(S*S*Q)
    Bz=P*P/(Q*(1+Q))+A*(A+z*P*P)*(1+2*Q)/(2*Q**3*(1+Q)**2)+yy*T*((A+z*P*P)/(2*S*Q**3)+P*P/(S*S*Q))
    C3=(1+Q+Q*Q)/(Q**3*(1+Q));BK1=K+E*T+z*L*A*C3
    BT1=K+z*yy*(A/(1+Q)+P*P*Q)/(S*Q)
    mu=1+v[-1]+z*np.mean(L*A*C3,axis=0)
    px=q.S@dy[:q.M];tx=q.C@(q.freq[:,None]*dy[:q.M]);kx=q.C@dy[q.M:2*q.M]
    vv=dy.copy();vv[-1]=-(2*ell*z*np.mean(Bz,axis=0)+np.mean(BP*px+BK1*kx+BT1*tx,axis=0))/mu
    return v,vv,iterations+1


def main(a):
    raw=a.input.read_bytes();d=json.loads(gzip.decompress(raw))
    if not d['success']:raise ValueError('Need accepted finite field')
    bg=Background(a.background,d.get('coordinate','physical-r'))
    if bg.sha256!=d['background_sha256']:raise ValueError('Background changed')
    q=DynamicMean(d['M'],a.angles or d['N']);x=np.array(d['mesh'])
    state=CubicHermiteSpline(x,np.array(d['states']).T,np.array(d['rhs']).T,axis=1)
    extrema={k:0. for k in ('original_mean','retracted_mean','delta_c','delta_c_radial_derivative',
       'original_full_P_radial_residual','original_full_K_radial_residual',
       'retracted_full_P_radial_residual','retracted_full_K_radial_residual',
       'original_relative_coefficient_radial_residual','retracted_relative_coefficient_radial_residual')}
    points=0;root_iterations=0
    fractions=np.linspace(0,1,a.subdivisions+1)
    for begin in range(0,len(x)-1,32):
        left=x[begin:min(begin+32,len(x)-1)];right=x[begin+1:min(begin+32,len(x)-1)+1]
        xx=np.ravel(left[:,None]+(right-left)[:,None]*fractions)
        yy=state(xx);dy=state(xx,1);s,ell,z=bg(xx);_,rx=bg.radial(xx)
        vy,vd,niter=retract_jet(q,yy,dy,s,ell,z);root_iterations=max(root_iterations,niter)
        extrema['delta_c']=max(extrema['delta_c'],float(np.max(abs(vy[-1]-yy[-1]))))
        extrema['delta_c_radial_derivative']=max(extrema['delta_c_radial_derivative'],float(np.max(abs((vd[-1]-dy[-1])/rx))))
        for label,y,yp in [('original',yy,dy),('retracted',vy,vd)]:
            rhs,info=q.evaluate(y,s,ell,z,True)
            rawp=q.S@rhs[:q.M]-info['pde_p_residual']
            pk=(q.C@yp[q.M:2*q.M]+yp[-1]-info['raw_k'])/rx
            pp=(q.S@yp[:q.M]-rawp)/rx
            values={label+'_mean':np.max(abs(info['mean'])),label+'_full_P_radial_residual':np.max(abs(pp)),
                    label+'_full_K_radial_residual':np.max(abs(pk)),
                    label+'_relative_coefficient_radial_residual':np.max(abs((yp-rhs)/rx)/(1+abs(rhs/rx)))}
            for name,value in values.items():extrema[name]=max(extrema[name],float(value))
        points+=len(xx)*q.N
    result=dict(scope=__doc__,input_sha256=hashlib.sha256(raw).hexdigest(),background_sha256=bg.sha256,
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),M=q.M,N=q.N,
                subdivisions=a.subdivisions,sampled_angle_radial_points=points,max_root_iterations=root_iterations,
                extrema=extrema)
    a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path,required=True)
    p.add_argument('--background',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--angles',type=int);p.add_argument('--subdivisions',type=int,default=4)
    main(p.parse_args())
