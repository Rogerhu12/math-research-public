#!/usr/bin/env python3
"""Actually consume the free BVP inlet, reverse exact coast, and both C2 seams.

The BVP inlet is explicitly projected to a NEW finite Cartesian Fourier
curve, with exact-arclength normalization to the same old f. All seam traces
are entire analytic functions; their angular derivatives use the same map.
The signed coast's n,m derivatives are transported by exact identities, not
independently Fourier fitted. Full Gram is observed on both adjacent ramps.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import importlib.util
import json
import math
from pathlib import Path
import time
import numpy as np
from scipy.interpolate import BSpline

HERE=Path(__file__).resolve().parent
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);out=importlib.util.module_from_spec(spec);spec.loader.exec_module(out);return out
bvp=module('signed_bvp_source',HERE/'6a65-m12-positive-ramp-position-bvp.py')
signed=module('signed_coast_source',HERE/'6a65-r137-signed-coast.py')
glue=bvp.glue;ramp=glue.ramp;ad=ramp.ad;LD=np.longdouble


def inlet_third(curve,u,v):
    """One-curve inlet plus the two third shape derivatives used in transport."""
    sup=ad.supplier;u=np.asarray(u);theta=curve.theta(u)
    gamma=np.stack([curve.derivative(theta,j)/math.factorial(j) for j in range(sup.ORDER+1)])
    gp=sup.diff(gamma);speed=sup.sqrt(sup.dot(gp,gp));recip=sup.inv(speed)
    T=sup.scale(recip,gp);lam=curve.a*recip
    def Du(field):return sup.scale(lam,sup.diff(field)) if field.ndim==3 else sup.mul(lam,sup.diff(field))
    Tu=Du(T);norm=sup.sqrt(sup.dot(Tu,Tu));inv=sup.inv(norm)
    U=sup.scale(inv,Tu);V=sup.cross(T,U);ratio=v*inv;one=np.zeros_like(ratio);one[0]=1
    rad=one-sup.mul(ratio,ratio)
    if np.any(rad[0]<=0):raise ValueError('BVP-projected curve has |T_u|<=v')
    d=-sup.scale(ratio,U)+sup.scale(sup.sqrt(rad),V);N=sup.cross(d,T)
    du=Du(d);duu=Du(du);Tuu=Du(Tu);Nu=Du(N)
    n=sup.dot(Tu,N)/curve.a;m=sup.dot(du,N)/curve.a
    nu,mu=Du(n),Du(m);nuu,muu=Du(nu),Du(mu);nuuu,muuu=Du(nuu),Du(muu)
    return dict(u=u,theta=theta,X=gamma[0],X_u=curve.a*T[0],X_uu=curve.a*Tu[0],
                e1=d[0],e1_u=du[0],e1_uu=duu[0],e2=T[0],e2_u=Tu[0],e2_uu=Tuu[0],
                N=N[0],N_u=Nu[0],n=n[0],m=m[0],n_u=nu[0],m_u=mu[0],n_uu=nuu[0],m_uu=muu[0],
                n_uuu=nuuu[0],m_uuu=muuu[0])


def multiply(a,b):
    out=np.zeros(np.broadcast_shapes(a.shape,b.shape))
    for j in range(3):
        for k in range(j+1):out[j]+=a[k]*b[j-k]
    return out


def inverse(a):
    out=np.zeros_like(a);out[0]=1/a[0]
    for j in range(1,3):out[j]=-sum(a[k]*out[j-k] for k in range(1,j+1))/a[0]
    return out


def cartesian_coeff(c):
    M=(len(c)-2)//3;degree=3*M+1;z=np.zeros((2*degree+1,3),complex)
    def xy(k,a):
        z[degree+k,0]+=a/2;z[degree-k,0]+=a/2
        z[degree+k,1]-=1j*a/2;z[degree-k,1]+=1j*a/2
    xy(1,c[0])
    for j in range(1,M+1):
        xy(1+3*j,(c[j]+c[M+j])/2);xy(1-3*j,(c[j]-c[M+j])/2)
        z[degree+3*j,2]=z[degree-3*j,2]=c[2*M+j]/2
    z[degree,2]=c[-1]
    return np.arange(-degree,degree+1),z


def old_port_traces(src,s,u,rho0,rho0p,lam):
    """Own old X, Xs, Xss and two theta derivatives, by analytic chain rule."""
    s=LD(s);e,ep=src.chart(s)
    j=min(np.searchsorted(src.sx,s/src.end,side='right')-1,len(src.sc)-1)
    xx=s/src.end-src.sx[j]
    epp=src.warp*(2*src.sc[j,2]+6*src.sc[j,3]*xx)/(src.end*src.end)
    psi=np.asarray(u,dtype=LD).copy()
    for unused in range(20):
        r=psi-e*np.sin(3*psi)/3-u;psi-=r/(1-e*np.cos(3*psi))
        if np.max(abs(r))<LD('1e-18'):break
    cell=max(0,min(len(src.mesh)-2,np.searchsorted(src.mesh,s,side='right')-1))
    c,d=src.coefficients(cell,s);t=(s-src.mesh[cell])/src.h[cell];p=src.power[cell]
    dd=20*p[5]
    for k in range(4,1,-1):dd=dd*t+k*(k-1)*p[k]
    dd/=src.h[cell]**2
    native=[]
    for row in (c,d,dd):
        modes,coeff=cartesian_coeff(np.asarray(row,float))
        ex=np.exp(1j*np.asarray(psi,float)[:,None]*modes)
        native.append([(ex@(coeff*(1j*modes[:,None])**k)).real for k in range(5)])
    sn,cs=np.sin(3*np.asarray(psi,float)),np.cos(3*np.asarray(psi,float))
    S=np.stack((sn,3*cs,-4.5*sn));C=np.stack((cs,-3*sn,-4.5*cs))
    rho=-float(e)*C;rho[0]+=1;rec=inverse(rho)
    ps=float(ep)/3*multiply(S,rec)
    pss=multiply(float(epp)/3*S+2*float(ep)*multiply(C,ps)-3*float(e)*multiply(S,multiply(ps,ps)),rec)
    def series(j,order):return np.stack((native[j][order],native[j][order+1],native[j][order+2]/2))
    def scale(a,z):return multiply(a[...,None],z)
    jets=[series(0,0),float(lam)*(series(1,0)+scale(ps,series(0,1))),
          float(lam)**2*(series(2,0)+2*scale(ps,series(1,1))+scale(multiply(ps,ps),series(0,2))+scale(pss,series(0,1)))]
    pt=rho0/rho[0];ptt=(rho0p-3*float(e)*sn*pt*pt)/rho[0]
    return np.stack([np.stack((z[0],z[1]*pt[:,None],2*z[2]*pt[:,None]**2+z[1]*ptt[:,None])) for z in jets])


def bvp_trace(basis,coeff,s,N):
    values=[basis.spline([s],nu=j)@coeff for j in range(3)]
    return np.stack([np.stack([basis.angular(values[j],N,k)[0] for k in range(3)]) for j in range(3)])


def observed_positive(src,candidate,central,basis,coeff,delta,N,lam,elements,gauss):
    mesh,s,weights=bvp.radial_grid(candidate,elements,gauss)
    p,bb=bvp.background(src,candidate,central,s,N,lam)
    op=bvp.Linearized(basis,s,weights,p,bb,N,precondition=False)
    p+=op.packet(coeff)
    left=float(candidate.left);h=float(candidate.R*candidate.etaq)
    poly=np.array([[1,0,0,-10,15,-6],[0,h,0,-6*h,8*h,-3*h],[0,0,h*h/2,-1.5*h*h,1.5*h*h,-.5*h*h]])
    pd=poly[:,1:]*np.arange(1,6)/h;pdd=pd[:,1:]*np.arange(1,5)/h
    for j,value in enumerate(s):
        if value>left+h:continue
        z=(value-left)/h;v=np.polynomial.polynomial.polyval(z,poly.T)
        dv=np.polynomial.polynomial.polyval(z,pd.T);ddv=np.polynomial.polynomial.polyval(z,pdd.T)
        p[j,0]+=np.einsum('a,and->nd',v,delta[:,0]);p[j,1]+=np.einsum('a,and->nd',dv,delta[:,0])
        p[j,2]+=np.einsum('a,and->nd',v,delta[:,1]);p[j,3]+=np.einsum('a,and->nd',ddv,delta[:,0])
        p[j,4]+=np.einsum('a,and->nd',dv,delta[:,1]);p[j,5]+=np.einsum('a,and->nd',v,delta[:,2])
    return bvp.statistics(p,bb,weights)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--data',type=Path,required=True);ap.add_argument('--bvp-report',type=Path,required=True)
    ap.add_argument('--bvp-field',type=Path,required=True);ap.add_argument('--ramp-field',type=Path,required=True)
    ap.add_argument('--ramp-report',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--angular',type=int,default=768);ap.add_argument('--degree',type=int,default=191)
    ap.add_argument('--gauss',type=int,default=10)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh output required')
    start=time.monotonic();br=json.loads(args.bvp_report.read_text());rr=json.loads(args.ramp_report.read_text())
    if ad.sha(args.bvp_field)!=br['field_sha256'] or ad.sha(args.ramp_field)!=rr['field_sha256']:raise ValueError('Source field identity mismatch')
    with np.load(args.bvp_field,allow_pickle=False) as d:
        coeff=d['coefficients'].copy();knots=d['knots'].copy();pm=d['planar_modes'].copy();zm=d['vertical_modes'].copy()
        central_c=[Q(int(a),int(b)) for a,b in zip(d['central_c_numerator'],d['central_c_denominator'])]
    with np.load(args.ramp_field,allow_pickle=False) as d:
        rampcoeff=d['coefficients'].copy();mesh=[Q(int(a),int(b)) for a,b in zip(d['mesh_numerator'],d['mesh_denominator'])]
    basis=bvp.Basis(np.r_[knots[0],knots[6:-6],knots[-1]],br['order'])
    if not np.array_equal(knots,basis.knots) or not np.array_equal(pm,basis.pm) or not np.array_equal(zm,basis.zm):raise ValueError('BVP basis mismatch')
    src=ad.base.Source(args.data,HERE.parent/'notes'/ad.base.META_NAME)
    candidate=bvp.PositiveRamp(src.meta);first=ramp.OriginalRamp(src.meta)
    central=ad.NativeCurve(central_c,512,32);N=args.angular
    if 2*args.degree>=N:raise ValueError('Need strict Fourier truncation')
    u,rho,rhop=bvp.central_chart(central,N)
    bridge=json.loads((HERE.parent/'notes/2026-11-09-db6f-root-exact-bridge-m12.json').read_text())['arclength_rescale']
    lam=ad.base.ld((Q(bridge['lo'])+Q(bridge['hi']))/2)
    old=old_port_traces(src,lam*ad.base.ld(candidate.left),u,rho,rhop,lam)
    old+=bvp_trace(basis,coeff,float(candidate.left),N)
    half=ramp.symmetric_fourier(old[0,0])
    raw=glue.EndpointCurve(half,args.degree)
    f1=1+candidate.delta-candidate.vq*candidate.R/2;v=float(candidate.vq)
    curve=ad.FixedRadiusCurve(raw,float(f1))
    leftparts=[];backparts=[];coast=[]
    length=candidate.Tu*(1-2*candidate.eps)
    for j in range(0,N,64):
        uj=u[j:j+64]
        leftparts.append(inlet_third(curve,uj,v))
        backparts.append(signed.at_material_inlet(float(f1),v,-float(length),uj,lambda t:inlet_third(curve,t,v)))
    left={k:np.concatenate([p[k] for p in leftparts]) for k in leftparts[0]}
    back={k:np.concatenate([p[k] for p in backparts]) for k in backparts[0] if isinstance(backparts[0][k],np.ndarray)}
    delta_positive=glue.correction_traces(left,LD(float(f1)),rho,rhop,old)
    oldramp=np.stack([np.stack([ramp.evaluate_coeff(rampcoeff[-1,j],N,k) for k in range(3)]) for j in range(3)])
    f0=1+candidate.vq*candidate.R/2
    delta_first=glue.correction_traces(back,LD(float(f0)),rho,rhop,oldramp)
    first_observation=glue.observe(mesh,rampcoeff,delta_first,rho,first,N,args.gauss,ad.base.ld(first.breaks[-2]))
    positive_observation=observed_positive(src,candidate,central,basis,coeff,delta_positive,N,lam,br['elements'],args.gauss)
    for q in (Q(0),Q(1,2),Q(1)):
        parts=[signed.at_material(float(f1),v,-float(length*q),u[j:j+64],lambda t:inlet_third(curve,t,v)) for j in range(0,N,64)]
        coast.append({'backward_fraction':str(q),'metric':float(max(np.max(p['metric']) for p in parts)),
                      'curvature':float(max(np.max(p['actual_curvature']) for p in parts)),
                      'minimum_D':float(min(np.min(p['D']) for p in parts)),
                      'minimum_Ut':float(min(np.min(p['U_t']) for p in parts)),
                      'n_transport_error':float(max(np.max(abs(p['n']-p['ideal_n'])) for p in parts)),
                      'ratio_transport_error':float(max(np.max(abs(p['m']/p['n']-p['ideal_ratio'])) for p in parts))})
    np.savez_compressed(str(args.out)+'.coast-definition.npz',positive_cartesian_coefficients=half[:args.degree+1])
    out={'schema':'6a65-M12-free-BVP-signed-exact-coast-and-both-true-C2-seams-v1','script_sha256':ad.sha(__file__),
         'signed_consumer_sha256':ad.sha(HERE/'6a65-r137-signed-coast.py'),'bvp_report_sha256':ad.sha(args.bvp_report),
         'bvp_field_sha256':ad.sha(args.bvp_field),'ramp_field_sha256':ad.sha(args.ramp_field),
         'coast_definition_sha256':ad.sha(str(args.out)+'.coast-definition.npz'),'degree':args.degree,'angles':N,
         'original_metric_unchanged':True,'signed_radius_exact':str(f1),'signed_length_exact':str(-length),'slope_exact':str(candidate.vq),
         'raw_arc_radius_numerical':raw.a,'projection_value_error':float(np.max(np.linalg.norm(raw.derivative(np.arange(N)*2*np.pi/N)-old[0,0],axis=-1))),
         'first_ramp_trace_norms':[[float(np.max(np.linalg.norm(delta_first[j,k],axis=-1))) for k in range(3)] for j in range(3)],
         'positive_ramp_trace_norms':[[float(np.max(np.linalg.norm(delta_positive[j,k],axis=-1))) for k in range(3)] for j in range(3)],
         'first_ramp_after_actual_seam':first_observation,'positive_ramp_after_actual_seam':positive_observation,'signed_coast_observations':coast,
         'C2_gluing_exact_function_identity':True,'continuous_domain_for_new_signed_curve_certified':False,
         'positive_right_port_not_yet_connected':True,'whole_closed_surface_constructed':False,'seconds':time.monotonic()-start}
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps(out,indent=2,allow_nan=False))


if __name__=='__main__':main()
