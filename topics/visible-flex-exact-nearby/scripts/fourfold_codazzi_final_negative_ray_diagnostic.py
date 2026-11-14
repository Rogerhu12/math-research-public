#!/usr/bin/env python3
"""Floating complete-centre negative two-ray return; no certification.

Every centre Fourier coefficient and the full quadratic drift are kept.
The target primitive, radial interpolation, ODE and angular return are
floating diagnostics only.  No Diophantine condition is inferred.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from scipy.integrate import solve_ivp,simpson
from scipy.interpolate import CubicSpline,PPoly
from scipy.optimize import brentq
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_compact_metric_return_probe import bumps
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_moving_polynomial_system import COORDINATES

CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
OBJECT='91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--radial-nodes',type=int,default=4097)
    ap.add_argument('--labels',type=int,default=512)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve all floating ray diagnostics')
    if sha(args.candidate)!=CANDIDATE or sha(args.object)!=OBJECT:
        raise ValueError('the complete actual centre and target are required')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']))
    if meta['coordinates']!=COORDINATES or int(meta['modes'])!=32:
        raise ValueError('wrong complete moving centre')
    alpha=float(Fraction(meta['exact_float_amplitude']));nu=float(Fraction(meta['exact_float_nu']))
    geometry,_=load_exact_object(args.object,512);target=RotationalBodyTarget(geometry)
    def controlled(r):
        r=np.asarray(r,float);base=target.values(r);a,g,b,K,Cr=(base[k] for k in ('a','gamma','beta','K','Cref'))
        w,wp=bumps(r);w,wp=w[0],wp[0]
        G=g*g;D=a*a*G*Cr*Cr;e=np.exp(nu*w);Dn=D+G*np.expm1(nu*w)
        if np.any(Dn<=0):raise ValueError('floating reference denominator failed')
        return g*np.sqrt(e),b,(K+b*nu*wp/(2*a*a*G))/e,1/(Cr*np.sqrt(Dn/(D*e)))
    root=brentq(lambda r:controlled([r])[2][0],.2383968742994,.2383968743003,xtol=5e-16)
    x=np.linspace(np.sqrt(root),0,args.radial_nodes);r=root-x*x;r[0]=0;r[-1]=root
    target_values=[]
    for j in range(0,len(r),32):
        target_values.append(np.asarray(controlled(r[j:j+32])))
    gamma,beta,K,s=np.concatenate(target_values,axis=1)
    y=PPoly(saved['piece_coefficients'],saved['radial_nodes'],extrapolate=False)(r)
    m=s+alpha*y[:,32]
    nfft=256;uf=np.zeros((len(r),nfft),complex);vf=np.zeros_like(uf)
    uf[:,1:33]=-.5j*alpha*y[:,:32];uf[:,-32:]=.5j*alpha*y[:,:32][:,::-1]
    vf[:,0]=m;vf[:,1:33]=.5*alpha*y[:,33:];vf[:,-32:]=.5*alpha*y[:,33:][:,::-1]
    u=np.fft.ifft(uf,axis=1).real*nfft;v=np.fft.ifft(vf,axis=1).real*nfft
    fullS=np.fft.fft(u*u+K[:,None]*v*v,axis=1).real/nfft
    k=4*np.arange(1,65,dtype=float)
    drift=-2*beta[:,None]*fullS[:,1:65]/k
    speed=-gamma*m*np.sqrt(np.maximum(0,-K))
    # The x variable resolves the true square-root endpoint without deleting it.
    reverse=slice(None,None,-1)
    dc=CubicSpline(x[reverse],drift[reverse],axis=0)
    ac=CubicSpline(x[reverse],speed[reverse])
    period=np.pi/2;labels=np.arange(args.labels+1)*period/args.labels
    state=np.r_[labels,labels,np.zeros_like(labels),np.zeros_like(labels)]
    n=len(labels)
    def rhs(t,z):
        d=dc(t);a=float(ac(t));out=[]
        for side,sgn in ((0,1),(1,-1)):
            h=z[side*n:(side+1)*n];phase=k[:,None]*h[None,:]
            drift_at=d@np.sin(phase);derivative=(d*k)@np.cos(phase)
            # H_r=-d+sgn*a; dr/dx=-2x.
            out.append(2*t*(drift_at-sgn*a))
            out.append(2*t*derivative)
        return np.r_[out[0],out[2],out[1],out[3]]
    sol=solve_ivp(rhs,(x[0],0),state,method='DOP853',rtol=2e-11,atol=2e-12,max_step=x[0]/300)
    if not sol.success:raise RuntimeError(sol.message)
    Hplus,Hminus,lp,lm=np.split(sol.y[:,-1],4)
    if np.any(np.diff(Hminus)<=0):raise RuntimeError('sampled inverse ray is not ordered')
    inv=CubicSpline(Hminus,labels)
    periods=np.floor((Hplus-Hminus[0])/period)
    wrapped=Hplus-periods*period
    F=inv(wrapped)+periods*period
    displacement=F-labels
    shift=float(np.mean(displacement[:-1]))
    periodic=displacement-shift;periodic[-1]=periodic[0]
    ret=CubicSpline(labels,periodic,bc_type='periodic')
    q=np.array([0.,period*.173,period*.527]);z=q.copy()
    steps=100000
    for _ in range(steps):z+=shift+ret(np.mod(z,period))
    rot=(z-q)/(steps*period)
    report=dict(kind='floating_actual_final_negative_two_ray_return',certified=False,
        source_sha256=sha(__file__),candidate_sha256=sha(args.candidate),object_sha256=sha(args.object),
        exact_alpha=meta['exact_float_amplitude'],exact_nu=meta['exact_float_nu'],
        radial_nodes=args.radial_nodes,angular_labels=args.labels,
        physical_frequency_factor=4,period=period,floating_root=root,
        full_centre_modes=32,full_quadratic_drift_modes=64,
        target_primitive_nodes=512,ODE_steps=len(sol.t),ODE_rhs_calls=sol.nfev,
        radial_optical_half_integral=float(simpson(2*x[reverse]*speed[reverse],x=x[reverse])),
        return_definition='H_minus(root)^(-1) o H_plus(root); H_s,r=-d+s*(-gamma*m)*sqrt(-K)',
        return_displacement_mean=shift,return_displacement_min=float(displacement.min()),
        return_displacement_max=float(displacement.max()),
        return_nonconstant_half_range=float((displacement.max()-displacement.min())/2),
        sampled_ray_J_min=float(min(np.exp(lp).min(),np.exp(lm).min())),
        sampled_ray_J_max=float(max(np.exp(lp).max(),np.exp(lm).max())),
        numerical_periodicity_error=float(max(abs(Hplus[-1]-Hplus[0]-period),abs(Hminus[-1]-Hminus[0]-period))),
        sampled_orbit_rotation_numbers=rot.tolist(),orbit_iterations=steps,
        return_labels=labels[:-1].tolist(),return_lift=F[:-1].tolist(),
        limitations=['Floating finite primitive, radial interpolation, ODE and angular interpolation.',
          'No root finite part, first phase, true nonlinear branch, rigorous rotation number or Diophantine condition.',
          'Complete quadratic centre drift retained; no replacement by its angular mean.'],
        seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print({k:report[k] for k in ('floating_root','return_displacement_mean','return_nonconstant_half_range',
        'sampled_ray_J_min','sampled_ray_J_max','sampled_orbit_rotation_numbers','seconds')},flush=True)


if __name__=='__main__':main()
