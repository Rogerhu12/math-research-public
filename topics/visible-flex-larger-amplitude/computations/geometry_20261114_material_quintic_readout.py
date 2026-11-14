#!/usr/bin/env python3
"""Read an actual C2 physical quintic prefix in the accepted material angle.

Endpoint position, first derivative and finite-ODE second derivative define
the unique quintic on every physical radial interval. The exact mathematical
definition treats saved binary64 nodal data as rationals; evaluation uses
extended precision for polynomial coefficients. Angular pullback uses the
actual accepted complete core, including its high modes. These are sampled
readouts, not continuous reach/embedding or closed-surface certificates.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import gzip
import hashlib
import importlib.util
import json
import time
from fractions import Fraction
from pathlib import Path
import numpy as np

P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('material_quintic_base',P/'geometry_20261114_r225_free_core_bvp.py')
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)


def material_angles(coefficients,count):
    frequency=2*np.arange(1,len(coefficients)+1)
    density=(1-frequency**2)*coefficients
    theta=2*np.pi*np.arange(count)/count
    phi=theta.copy();low=np.zeros(count);high=np.full(count,2*np.pi)
    for iteration in range(80):
        argument=frequency[:,None]*phi
        value=phi+(density/frequency)@np.sin(argument)
        rho=1+density@np.cos(argument);error=value-theta
        active=abs(error)>2e-14
        if not np.any(active):
            break
        low=np.where(active&(error<0),phi,low);high=np.where(active&(error>0),phi,high)
        candidate=phi-error/rho
        bad=(candidate<=low)|(candidate>=high)|(~np.isfinite(candidate))
        candidate=np.where(bad,(low+high)/2,candidate)
        phi=np.where(active,candidate,phi)
    else:
        raise RuntimeError('Material angle inversion did not converge')
    argument=frequency[:,None]*phi
    rho=1+density@np.cos(argument)
    rhop=-(frequency*density)@np.sin(argument)
    return phi,rho,rhop,dict(iterations=iteration+1,max_angle_residual=float(abs(error).max()),
                            rho_sample_min=float(rho.min()),rho_sample_max=float(rho.max()))


def angular_jet(values,M,phi):
    freq=2*np.arange(M+1)
    C=np.cos(freq[:,None]*phi);S=np.sin(freq[:,None]*phi)
    C1=-freq[:,None]*S;S1=freq[:,None]*C
    C2=-freq[:,None]**2*C;S2=-freq[:,None]**2*S
    def evaluate(y):
        r=y[:,:M+1];t=y[:,M+1:2*M+1];z=y[:,2*M+1:]
        R=r@C;T=t@S[1:];Z=z@C
        Rp=r@C1;Tp=t@S1[1:];Zp=z@C1
        Rpp=r@C2;Tpp=t@S2[1:];Zpp=z@C2
        F=np.stack([R,T,Z],axis=2)
        first=np.stack([Rp-T,Tp+R,Zp],axis=2)
        second=np.stack([Rpp-2*Tp-R,Tpp+2*Rp-T,Zpp],axis=2)
        return F,first,second
    return evaluate


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--angles',type=int,nargs='+',default=[1024,2048])
    p.add_argument('--radial-subdivisions',type=int,nargs='+',default=[2,4])
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    if len(args.angles)!=len(args.radial_subdivisions):
        raise ValueError('Provide one angular and radial count per level')
    data=base.fixed.read(args.input)
    if data['success']is not True:
        raise ValueError('An accepted full BVP is required')
    M,N=data['M'],data['N'];law=data['original_metric_identity']['law']
    c=np.array(data['core']['coefficients']);q=base.native.outward.FullCoreProbe(c,M,N,law['velocity'],law['length'],law['k0'])
    q.profile=base.fixed.FixedProfile(data['fixed_scalar_profile']['geometry']).profile;base.fixed.fft.enable_fft(q)
    x=np.array(data['mesh']);Y=np.array(data['states']);DY=np.array(data['rhs']);DDY=[]
    epsilon=1e-25;node_rhs_gap=0.
    for s,y,yp in zip(x,Y,DY):
        fr=q.frame(float(s),y);local=q.project(fr['V']);node_rhs_gap=max(node_rhs_gap,float(abs(local-yp).max()))
        state=q.project(q.frame(float(s),y.astype(complex)+1j*epsilon*yp,strict=False)['V']).imag/epsilon
        da=-fr['app']/(fr['a']*fr['kap'])+fr['ap']**2/(fr['a']**2*fr['kap']);db=-fr['al']*da/fr['be']
        DDY.append(state+q.project(da[:,None]*fr['N']+db[:,None]*fr['B']))
    DDY=np.array(DDY);h=np.diff(x.astype(np.longdouble))
    y=Y.astype(np.longdouble);dy=DY.astype(np.longdouble);ddy=DDY.astype(np.longdouble)
    c0=y[:-1];c1=h[:,None]*dy[:-1];c2=h[:,None]**2*ddy[:-1]/2
    A=y[1:]-c0-c1-c2;B=h[:,None]*dy[1:]-c1-2*c2;C=h[:,None]**2*ddy[1:]-2*c2
    coefficients=np.stack([c0,c1,c2,10*A-4*B+C/2,-15*A+7*B-C,6*A-3*B+C/2],axis=1)
    rho_coefficients=[str(Fraction(float(v)))for v in c]
    major=1+float(c.sum());minor=1+float(np.sum(c*(-1.)**np.arange(1,M+1)));gap=major-minor
    begin=time.time();levels=[]
    for ntheta,subdivision in zip(args.angles,args.radial_subdivisions):
        if subdivision<1:
            raise ValueError('Use positive radial subdivisions')
        phi,rho,rhop,angle_info=material_angles(c,ntheta)
        evaluate=angular_jet(None,M,phi);cos=np.cos(phi);sin=np.sin(phi)
        metric_max=kappa_max=0.;min_determinant=np.inf;witness_min=np.inf;twice_norm=0.;worst=None;rows=[]
        for j in range(len(x)-1):
            maxima=dict(interval=j,s_left=float(x[j]),s_right=float(x[j+1]),metric=0.,kappa=0.)
            for i in range(subdivision+1):
                if j and i==0:
                    continue
                u=np.longdouble(i)/subdivision;pol=coefficients[j]
                y0=np.polynomial.polynomial.polyval(u,pol)
                y1=np.polynomial.polynomial.polyval(u,np.arange(1,6)[:,None]*pol[1:])/h[j]
                y2=np.polynomial.polynomial.polyval(u,(np.arange(2,6)*np.arange(1,5))[:,None]*pol[2:])/(h[j]*h[j])
                s=float(np.longdouble(x[j])+u*h[j]);a,ap,app=q.profile(s)
                value,first,second=evaluate(np.array([y0,y1,y2],dtype=float))
                F,Fs,Fss=value
                Ft=first[0]/rho[:,None];Fst=first[1]/rho[:,None]
                Ftt=second[0]/rho[:,None]**2-first[0]*(rhop/rho**3)[:,None]
                E=np.einsum('ij,ij->i',Fs,Fs);mixed=np.einsum('ij,ij->i',Fs,Ft);G=np.einsum('ij,ij->i',Ft,Ft)
                errors=np.maximum.reduce([abs(E-1),abs(mixed)/a,abs(G/a**2-1)])
                metric=float(errors.max());at=int(np.argmax(errors))
                normal=np.cross(Fs,Ft);normal/=np.linalg.norm(normal,axis=1)[:,None]
                e=np.einsum('ij,ij->i',Fss,normal);f=np.einsum('ij,ij->i',Fst,normal);g=np.einsum('ij,ij->i',Ftt,normal)
                determinant=E*G-mixed*mixed;trace=(e*G+g*E-2*f*mixed)/determinant
                kg=(e*g-f*f)/determinant;disc=np.maximum(0.,trace*trace-4*kg)
                kappa=float(np.max((abs(trace)+np.sqrt(disc))/2))
                xyz=np.stack([cos*F[:,0]-sin*F[:,1],sin*F[:,0]+cos*F[:,1],F[:,2]],axis=1)
                distance=np.linalg.norm(xyz-np.array([0.,major,0.]),axis=1)
                witness_min=min(witness_min,float(distance.min()));twice_norm=max(twice_norm,2*float(np.linalg.norm(xyz,axis=1).max()))
                min_determinant=min(min_determinant,float(determinant.min()))
                if metric>metric_max:
                    metric_max=metric;worst=dict(s=s,interval=j,u=float(u),theta=float(2*np.pi*at/ntheta),phi=float(phi[at]),error=metric)
                kappa_max=max(kappa_max,kappa);maxima['metric']=max(maxima['metric'],metric);maxima['kappa']=max(maxima['kappa'],kappa)
            rows.append(maxima)
            if (j+1)%100==0:
                print(json.dumps(dict(event='material_quintic',angles=ntheta,radial_subdivisions=subdivision,
                                      intervals=j+1,metric=metric_max,kappa=kappa_max,seconds=time.time()-begin)),flush=True)
        levels.append(dict(angles=ntheta,radial_subdivisions=subdivision,radial_sample_count=(len(x)-1)*subdivision+1,
                           metric_sample=metric_max,kappa_sample=kappa_max,minimum_metric_determinant=min_determinant,
                           minimum_witness_distance=witness_min,reflected_prefix_D_sample=twice_norm,
                           worst_metric=worst,angle_inversion=angle_info,interval_rows=rows))
        print(json.dumps({k:v for k,v in levels[-1].items()if k!='interval_rows'}),flush=True)
    report=dict(scope=__doc__,M=M,base_angular=N,node_count=len(x),core_gap=gap,
                actual_core_coefficients_rational=rho_coefficients,
                material_map='theta=phi+sum_m (1-4m^2)c_m sin(2m phi)/(2m); phi_s=0, phi_theta=1/rho, phi_thetatheta=-rho_phi/rho^3.',
                metric='ds^2+a(s)^2 dtheta^2, with the unchanged fixed scalar profile in the accepted BVP.',
                node_saved_vs_local_rhs_gap=node_rhs_gap,levels=levels,seconds=time.time()-begin,
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),
                field_definition='Unique physical quintic matching accepted binary64 y, saved RHS and computed finite-ODE second derivative at every radial node; exact binary rationals define C2 seams.',
                continuous_metric_certificate=False,closed_surface=False)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':
    main()
