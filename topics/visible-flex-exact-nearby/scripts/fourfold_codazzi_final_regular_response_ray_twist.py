#!/usr/bin/env python3
"""Floating full-regular response -> actual two-ray phase-twist proposal.

The input response is physical unnormalized h=(du,dv), with its genuine
even mean, for D h=+partial_nu F.  Direct metric, state drift, mean speed,
both characteristic legs, and both physical waist angle terms are kept.
This is explicitly a proposal: no interval flow, actual branch, circle
conjugacy or Diophantine condition follows from its floating output.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import time
for _ray_thread_variable in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[_ray_thread_variable] = '1'
import numpy as np
from scipy.integrate import solve_ivp, simpson
from scipy.interpolate import CubicSpline, PPoly
from scipy.optimize import brentq
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_compact_metric_return_probe import bumps
from fourfold_codazzi_final_continuous_value_repair import iter_repair
from fourfold_codazzi_final_head_trial_model import FULL_COORDINATES
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_moving_polynomial_system import COORDINATES

CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
OBJECT='91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848'
REPAIR='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def fourier_pairs(real_sine, real_cosine, mean, nfft):
    n=len(real_sine); modes=real_sine.shape[1]
    a=np.zeros((n,nfft),complex); b=np.zeros_like(a)
    a[:,1:modes+1]=-.5j*real_sine
    a[:,-modes:]=.5j*real_sine[:,::-1]
    b[:,0]=mean
    b[:,1:modes+1]=.5*real_cosine
    b[:,-modes:]=.5*real_cosine[:,::-1]
    return a,b


def inverse_conjugacy_proposal(labels, F, period, modes):
    x=labels[:-1];y=F[:-1];k=4*np.arange(1,modes+1,dtype=float)
    C=np.cos(x[:,None]*k);S=np.sin(x[:,None]*k)
    CY=np.cos(y[:,None]*k);SY=np.sin(y[:,None]*k)
    A=np.column_stack((np.ones_like(x),-(SY-S),-(CY-C)))
    sol,_,rank,singular=np.linalg.lstsq(A,y-x,rcond=None)
    omega=float(sol[0]);a,b=sol[1:modes+1],sol[modes+1:]
    def lift(t):
        t=np.asarray(t,float)
        return t+np.sin(t[...,None]*k)@a+np.cos(t[...,None]*k)@b
    def derivative(t):
        t=np.asarray(t,float)
        return 1+np.cos(t[...,None]*k)@(k*a)-np.sin(t[...,None]*k)@(k*b)
    residual=lift(y)-lift(x)-omega
    return lift,derivative,dict(modes=modes,omega=omega,normalized_rotation=omega/period,
        sine_coefficients=a.tolist(),cosine_coefficients=b.tolist(),rank=int(rank),
        smallest_singular=float(singular[-1]),sampled_conjugacy_residual=float(np.max(abs(residual))),
        sampled_derivative_min=float(np.min(derivative(x))),
        sampled_derivative_max=float(np.max(derivative(x))),certified=False)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--response',type=Path,required=True)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--radial-nodes',type=int,default=1025)
    ap.add_argument('--labels',type=int,default=128)
    ap.add_argument('--conjugacy-modes',type=int,default=24)
    ap.add_argument('--minimum-steps',type=int,default=300)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve every complete phase proposal')
    if sha(args.candidate)!=CANDIDATE or sha(args.object)!=OBJECT:
        raise ValueError('the same complete final candidate and intrinsic target are required')
    if args.labels<2*args.conjugacy_modes+8 or args.radial_nodes<513 or args.minimum_steps<200:
        raise ValueError('invalid declared full ray proposal resolution')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']))
    trial=load_candidate(args.response);tm=json.loads(str(trial['metadata']))
    if meta['coordinates']!=COORDINATES or int(meta['modes'])!=32:
        raise ValueError('the centre must use the true moving coordinates')
    if (tm.get('kind')!='actual_final_full_finite_head_trial_v1' or tm.get('role')!='response_full'
        or tm.get('coordinates')!=FULL_COORDINATES or tm.get('background_candidate_sha256')!=CANDIDATE
        or tm.get('Schur_complement')!='full_regular_waist_amplitude_output'
        or not tm.get('original_fourth_Robin_row_retained') or tm.get('modes')!=96):
        raise ValueError('a full-regular physical response including its mean is required')
    alpha=Fraction(meta['exact_float_amplitude']);nu=Fraction(meta['exact_float_nu'])
    if tm['background_exact_alpha']!=str(alpha) or tm['background_exact_nu']!=str(nu):
        raise ValueError('the response parameter units differ from the actual centre')
    geometry,_=load_exact_object(args.object,512);target=RotationalBodyTarget(geometry)
    def controlled(r):
        r=np.asarray(r,float);base=target.values(r)
        a,g,b,K,Cr=(base[k] for k in ('a','gamma','beta','K','Cref'))
        w,wp=bumps(r);w,wp=w[0],wp[0]
        E=(a*g)**2;en=np.exp(float(nu)*w)
        D=a*a*g*g*Cr*Cr
        Dn=D+(g*g)*np.expm1(float(nu)*w)
        if np.any(Dn<=0):raise ValueError('floating complete rotational reference failed')
        gamma=g*np.sqrt(en);curvature=(K+b*float(nu)*wp/(2*E))/en
        scalar_s=1/(Cr*np.sqrt(Dn/(D*en)))
        return gamma,b,curvature,scalar_s,b/(2*E*en),w,wp
    root=brentq(lambda r:controlled([r])[2][0],.2383968742994,.2383968743003,xtol=5e-16)
    xgrid=np.linspace(np.sqrt(root),0,args.radial_nodes);r=root-xgrid*xgrid
    r[0]=0;r[-1]=root
    fields=np.concatenate([np.asarray(controlled(r[j:j+32])) for j in range(0,len(r),32)],axis=1)
    gamma,beta,K,s,T,w,wp=fields
    centre=PPoly(saved['piece_coefficients'],saved['radial_nodes'],extrapolate=False)(r)
    response=PPoly(trial['piece_coefficients'],trial['radial_nodes'],extrapolate=False)(r)
    pieces=np.searchsorted(saved['radial_nodes'],r,side='right')-1
    last=int(pieces.max());repair=np.zeros((last+1,65))
    for piece,offset,_ in iter_repair(saved,alpha):
        if piece>last:break
        repair[piece]=[float(z) for z in offset]
    u_s=float(alpha)*centre[:,:32]+repair[pieces,:32]
    v_c=float(alpha)*centre[:,33:]+repair[pieces,33:]
    mean=s+float(alpha)*centre[:,32]+repair[pieces,32]
    nfft=512
    uf,vf=fourier_pairs(u_s,v_c,mean,nfft)
    hf,kf=fourier_pairs(response[:,:96],response[:,97:],response[:,96],nfft)
    u=np.fft.ifft(uf,axis=1).real*nfft;v=np.fft.ifft(vf,axis=1).real*nfft
    hu=np.fft.ifft(hf,axis=1).real*nfft;hv=np.fft.ifft(kf,axis=1).real*nfft
    S=np.fft.fft(u*u+K[:,None]*v*v,axis=1).real/nfft
    Knu=-w*K+T*wp
    direct=np.fft.fft(Knu[:,None]*v*v,axis=1).real/nfft
    state=np.fft.fft(2*u*hu+2*K[:,None]*v*hv,axis=1).real/nfft
    k0=4*np.arange(1,65,dtype=float);k1=4*np.arange(1,129,dtype=float)
    # F_sigma = beta I(S) + sigma c.  The real sine amplitude of I
    # a real even polynomial with positive Fourier entry f_j is 2 f_j/(4j).
    drift=2*beta[:,None]*S[:,1:65]/k0
    ddirect=2*beta[:,None]*direct[:,1:129]/k1
    dstate=2*beta[:,None]*state[:,1:129]/k1
    q=np.sqrt(np.maximum(0,-K));speed=-gamma*mean*q
    cmetric=np.zeros_like(q);support=(wp!=0)
    cmetric[support]=gamma[support]*mean[support]*T[support]*wp[support]/(2*q[support])
    cmean=-gamma*q*response[:,96]
    rev=slice(None,None,-1)
    splines=[CubicSpline(xgrid[rev],z[rev],axis=0) for z in (drift,speed,ddirect,dstate,cmetric,cmean)]
    period=np.pi/2;labels=np.linspace(0,period,args.labels+1);n=len(labels)
    # Per side: actual angle, log Jacobian, metric variation, state-drift
    # variation, and the complete even-mean speed variation.
    initial=np.zeros((2,5,n));initial[:,0,:]=labels
    def rhs(x,z):
        z=z.reshape(2,5,n);out=np.empty_like(z)
        d,c,dd,ds,cm,cz=(sp(x) for sp in splines)
        for side,sgn in enumerate((1,-1)):
            H=z[side,0];p0=k0[:,None]*H;p1=k1[:,None]*H
            sine0=np.sin(p0);sine1=np.sin(p1)
            D=d@sine0;D1=(d*k0)@np.cos(p0)
            out[side,0]=-2*x*(D+sgn*c)
            out[side,1]=-2*x*D1
            forcing=(dd@sine1+sgn*cm,ds@sine1,np.full(n,sgn*cz))
            for j,forcing_j in enumerate(forcing,2):
                out[side,j]=-2*x*(D1*z[side,j]+forcing_j)
        return out.ravel()
    sol=solve_ivp(rhs,(xgrid[0],0),initial.ravel(),method='DOP853',
        rtol=3e-11,atol=3e-12,max_step=xgrid[0]/args.minimum_steps)
    if not sol.success:raise RuntimeError(sol.message)
    end=sol.y[:,-1].reshape(2,5,n);hp,hm=end[:,0];lp,lm=end[:,1]
    if np.any(np.diff(hm)<=0):raise RuntimeError('the sampled full backward ray is not invertible')
    wind=np.floor((hp-hm[0])/period);wrapped=hp-wind*period
    inverse=CubicSpline(hm,labels);F=inverse(wrapped)+wind*period
    Jm=np.exp(CubicSpline(hm,lm)(wrapped));Jp=np.exp(lp);Fp=Jp/Jm
    variations=[]
    for j in range(2,5):
        ym=CubicSpline(hm,end[1,j])(wrapped)
        variations.append((end[0,j]-ym)/Jm)
    total=sum(variations)
    # Full parameter-dependent waist coordinate; the root coordinate
    # cancels exactly between the two legs of their physical composition.
    v0=centre[0,33:]*float(alpha)+repair[0,33:]
    h0=response[0,97:];m0=mean[0];z0=response[0,96]
    kw=4*np.arange(1,97,dtype=float)
    vpad=np.r_[v0,np.zeros(64)]
    psi=vpad/(m0*kw)
    psidot=(h0-z0*vpad/m0)/(m0*kw)
    def theta(t):return t+np.sin(np.asarray(t)[...,None]*kw)@psi
    def theta1(t):return 1+np.cos(np.asarray(t)[...,None]*kw)@(kw*psi)
    def theta_dot(t):return np.sin(np.asarray(t)[...,None]*kw)@psidot
    physical_derivative=theta1(F)*Fp/theta1(labels)
    chart_term=theta_dot(F)-physical_derivative*theta_dot(labels)
    physical_total=theta1(F)*total+chart_term
    lift,derivative,conjugacy=inverse_conjugacy_proposal(labels,F,period,args.conjugacy_modes)
    weight=derivative(F[:-1])*derivative(labels[:-1])
    split=[float(np.mean(weight*z[:-1])) for z in variations]
    twist=float(sum(split))
    physical_weight=derivative(F[:-1])/theta1(F[:-1])*derivative(labels[:-1])
    physical_twist=float(np.mean(physical_weight*physical_total[:-1]))
    chart_average=float(np.mean(physical_weight*chart_term[:-1]))
    periodic_error=max(abs(hp[-1]-hp[0]-period),abs(hm[-1]-hm[0]-period))
    report=dict(kind='floating_actual_full_regular_response_two_ray_twist',certified=False,
        source_sha256=sha(__file__),candidate_sha256=sha(args.candidate),object_sha256=sha(args.object),
        derived_continuous_centre_definition_sha256=REPAIR,response_sha256=sha(args.response),
        response_metadata=tm,physical_unnormalized_response=True,complete_even_mean_retained=True,
        parameter_source_sign='D h = + partial_nu F',direct_gamma_sign='+w gamma/2',
        no_extra_reference_s_nu_column_added=True,root_independent_of_nu=True,
        exact_alpha=str(alpha),exact_nu=str(nu),floating_root=root,
        radial_nodes=args.radial_nodes,labels=args.labels,ODE_steps=len(sol.t),ODE_rhs_calls=sol.nfev,
        background_modes=32,response_modes=96,full_variation_drift_modes=128,convolution_grid=nfft,
        floating_optical_half_integral=float(simpson(2*xgrid[rev]*speed[rev],x=xgrid[rev])),
        inverse_conjugacy_proposal=conjugacy,mean_return_displacement=float(np.mean((F-labels)[:-1])),
        weighted_rotation_lift_derivative_proposal=twist,
        normalized_rotation_derivative_proposal=twist/period,
        split_weighted_lift_derivatives=dict(direct_metric=split[0],full_state_drift=split[1],true_mean_speed=split[2]),
        physical_waist_chart_mean_term=chart_average,
        physical_chart_weighted_rotation_derivative=physical_twist,
        full_return_derivative_min=float(np.min(total)),full_return_derivative_max=float(np.max(total)),
        full_physical_return_derivative_min=float(np.min(physical_total)),full_physical_return_derivative_max=float(np.max(physical_total)),
        ray_J_min=float(min(np.exp(lp).min(),np.exp(lm).min())),
        ray_J_max=float(max(np.exp(lp).max(),np.exp(lm).max())),periodicity_error=float(periodic_error),
        labels_moving=labels[:-1].tolist(),return_moving=F[:-1].tolist(),return_moving_derivative=Fp[:-1].tolist(),
        parameter_return_metric=variations[0][:-1].tolist(),parameter_return_state_drift=variations[1][:-1].tolist(),
        parameter_return_mean_speed=variations[2][:-1].tolist(),parameter_return_total=total[:-1].tolist(),
        physical_labels=theta(labels[:-1]).tolist(),physical_return=theta(F[:-1]).tolist(),
        physical_parameter_return=physical_total[:-1].tolist(),
        no_true_nonlinear_solution_branch_or_phase_twist_proved=True,
        no_interval_ODE_or_actual_conjugacy_proved=True,no_Diophantine_condition_proved=True,
        no_complete_high_return_or_global_inverse_proved=True,
        limitations=['Finite full-regular response is a proposal; its actual mean must be completed and continuous defects paid.',
          'Target evaluation, radial interpolation, ODE, inverse ray and conjugacy are floating.',
          'Mean speed, direct target and the physical waist conjugation are retained, not set to zero.',
          'Choosing one nearby final nu is not permission to vary the metric within the isometric flex family.'],
        seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print({k:report[k] for k in ('floating_root','weighted_rotation_lift_derivative_proposal',
        'normalized_rotation_derivative_proposal','split_weighted_lift_derivatives',
        'full_return_derivative_min','full_return_derivative_max','physical_waist_chart_mean_term','seconds')},flush=True)


if __name__=='__main__':main()
