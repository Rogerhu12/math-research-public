#!/usr/bin/env python3
"""Uniform curvature-angle rays and floating conjugacy/rotation diagnostic.

This does not certify a circle map, an irrational rotation number, a
parameter derivative, turning scattering, or the infinite body inverse.
It improves the actual principal-map diagnostic without changing the
previous nonuniform physical-angle report.
"""
from __future__ import annotations
import argparse,gzip,json,time
from functools import lru_cache
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline,PPoly
from scipy.optimize import brentq
from fourfold_codazzi_curvature_angle_return_probe import PERIOD,angular_fields,inverse_derivative
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_compact_metric_return_probe import bumps
from fourfold_phase_metric_defect import sha,save


def read(p):return json.loads(gzip.decompress(Path(p).read_bytes()))


def weighted_rotation(spline,count,seeds):
    x=seeds.copy();numerator=np.zeros_like(x);denominator=0.
    for j in range(count):
        t=(j+.5)/count;weight=np.exp(-1/(t*(1-t)))
        move=spline(np.remainder(x,PERIOD));numerator+=weight*move;denominator+=weight;x+=move
    return dict(iterates=count,weighted=(numerator/(PERIOD*denominator)).tolist(),
        ordinary=((x-seeds)/(PERIOD*count)).tolist())


def conjugacy(spline,rho,N):
    x=PERIOD*np.arange(N)/N;frequency=4*np.fft.fftfreq(N,1/N)
    u=np.zeros(N);history=[];failed=None
    for iteration in range(20):
        coeff=np.fft.fft(u)/N;shift=np.exp(1j*frequency*rho)
        us=np.fft.ifft(coeff*shift).real*N
        derivative=1+np.fft.ifft(1j*frequency*coeff).real*N
        derivative_shift=1+np.fft.ifft(1j*frequency*coeff*shift).real*N
        error=u-us+spline(np.remainder(x+u,PERIOD))-rho
        norm=float(np.max(abs(error)))
        history.append(dict(iteration=iteration,rho_angle=float(rho),rho_turns=float(rho/PERIOD),
            sampled_residual_sup=norm,sampled_derivative_min=float(derivative.min()),
            displacement_sup=float(np.max(abs(u)))))
        if norm<5e-14:break
        if min(derivative.min(),derivative_shift.min())<=.05:
            failed='sampled conjugacy derivative gate';break
        g=error/derivative_shift;drho=float(np.mean(g));gc=np.fft.fft(g)/N
        den=shift-1;nz=frequency!=0
        if np.any(abs(den[nz])<1e-12):failed='floating small divisor unresolved';break
        wc=np.zeros(N,dtype=complex);wc[nz]=gc[nz]/den[nz]
        w=np.fft.ifft(wc).real*N
        # This constant does not affect w(x+rho)-w(x); it preserves mean u.
        w-=np.mean(derivative*w)/np.mean(derivative)
        correction=derivative*w
        accepted=False
        for power in range(9):
            step=2.**(-power);trial=u+step*correction;rr=rho+step*drho
            tc=np.fft.fft(trial)/N
            ts=np.fft.ifft(tc*np.exp(1j*frequency*rr)).real*N
            ee=trial-ts+spline(np.remainder(x+trial,PERIOD))-rr
            if np.max(abs(ee))<norm:accepted=True;u=trial;rho=rr;break
        if not accepted:failed='floating conjugacy residual did not decrease';break
    coeff=np.fft.fft(u)/N
    fine=PERIOD*np.arange(4*N)/(4*N);ff=4*np.fft.fftfreq(4*N,1/(4*N))
    padded=np.zeros(4*N,dtype=complex);idx=np.r_[np.arange(N//2),np.arange(-N//2,0)]
    padded[idx%(4*N)]=coeff
    uf=np.fft.ifft(padded).real*(4*N)
    usf=np.fft.ifft(padded*np.exp(1j*ff*rho)).real*(4*N)
    error=uf-usf+spline(np.remainder(fine+uf,PERIOD))-rho
    return dict(rho_angle=float(rho),rho_turns=float(rho/PERIOD),history=history,
        failure=failed,doubled_twice_sampled_residual_sup=float(np.max(abs(error))),
        grid=N,all_finite_conjugacy_coefficients_real=coeff.real.tolist(),
        all_finite_conjugacy_coefficients_imag=coeff.imag.tolist(),
        no_interval_or_KAM_conclusion=True)


def run(path,prior,geometry,args):
    started=time.monotonic();saved=load_candidate(path);meta=json.loads(str(saved['metadata']))
    entry=next((x for x in prior['entries'] if x['candidate_sha256']==sha(path)),None)
    if entry is None or meta['object_sha256']!=prior['object_sha256']:
        raise ValueError('a complete earlier same-candidate principal diagnostic is required')
    m=int(meta['modes']);alpha=float(meta['amplitude']);nu=float(meta['nu']);turn=float(entry['first_turning_radius'])
    pp=PPoly(saved['piece_coefficients'],saved['radial_nodes']);body=RotationalBodyTarget(geometry)
    @lru_cache(maxsize=32768)
    def target(r):
        z=body.point(r);a,g,b,K,Cr=(z[k] for k in ('a','gamma','beta','K','Cref'))
        h,hp=bumps([r]);h,hp=h[0,0],hp[0,0];exp=np.exp(nu*h)
        D=a*a*g*g*Cr*Cr;Dn=D+g*g*np.expm1(nu*h)
        if Dn<=0:raise ValueError('controlled target denominator failed')
        return g*np.sqrt(exp),(K+b*nu*hp/(2*a*a*g*g))/exp,Cr*np.sqrt(Dn/(D*exp))
    if abs(target(turn)[1])>1e-10:raise ValueError('the old floating turning point changed')
    N=args.waist_grid;angles=PERIOD*np.arange(N)/N;freq=4*np.fft.fftfreq(N,1/N)
    (U,V),_=angular_fields(pp(0.),m,N);s=1/target(0.)[2];C=1/(s+alpha*V)
    if not np.max(C)<0:raise ValueError('sampled negative waist curvature failed')
    D=float(np.mean(C));disp=inverse_derivative(C-D,freq)/D
    phi_disp=CubicSpline(np.r_[angles,PERIOD],np.r_[disp,disp[0]],bc_type='periodic')
    def phi(theta):return theta+phi_disp(np.remainder(theta,PERIOD))
    def phiprime(theta):return 1+phi_disp(np.remainder(theta,PERIOD),1)
    phi_initial=PERIOD*np.arange(args.rays)/args.rays
    theta_initial=np.array([0. if j==0 else brentq(lambda th:phi(th)-q,0.,PERIOD,
        xtol=1e-14,rtol=1e-14) for j,q in enumerate(phi_initial)])
    if np.max(abs(phi(theta_initial)-phi_initial))>1e-12:raise ValueError('floating initial angle inversion failed')
    physical=4*np.arange(1,m+1,dtype=float);calls={'+':0,'-':0};last=time.monotonic()
    def rhs(sign):
        label='+' if sign>0 else '-'
        def value(x,state):
            nonlocal last
            r=float(turn*(2*x-x*x));dr=2*turn*(1-x);theta=state[:args.rays];J=state[args.rays:]
            y=pp(r);g,K,Cr=target(r);k=np.sqrt(max(0.,-K))
            phase=physical[:,None]*np.remainder(theta,PERIOD)[None,:];si=np.sin(phase);co=np.cos(phase)
            u=alpha*(y[:m]@si);ut=alpha*((physical*y[:m])@co)
            v=1/Cr+alpha*(y[m]+y[m+1:]@co);vt=-alpha*((physical*y[m+1:])@si)
            calls[label]+=1
            if time.monotonic()-last>20:
                print(dict(candidate=str(path),branch=label,x=float(x),calls=calls),flush=True);last=time.monotonic()
            return np.r_[-dr*g*(u+sign*v*k),-dr*g*(ut+sign*vt*k)*J]
        return value
    first=solve_ivp(rhs(1),(0.,1.),np.r_[theta_initial,np.ones(args.rays)],method='DOP853',
        rtol=args.rtol,atol=args.atol,max_step=args.maximum_x_step)
    if not first.success:raise ValueError('uniform-curvature initial forward rays failed')
    second=solve_ivp(rhs(-1),(1.,0.),first.y[:,-1],method='DOP853',
        rtol=args.rtol,atol=args.atol,max_step=args.maximum_x_step)
    if not second.success:raise ValueError('uniform-curvature return rays failed')
    theta=second.y[:,-1][:args.rays];J=second.y[:,-1][args.rays:]
    returned=phi(theta);delta=returned-phi_initial
    derivative=phiprime(theta)*J/phiprime(theta_initial)
    spline=CubicSpline(np.r_[phi_initial,PERIOD],np.r_[delta,delta[0]],bc_type='periodic')
    seeds=PERIOD*np.arange(8)/8
    rotations=[weighted_rotation(spline,n,seeds) for n in args.iterates]
    rho=PERIOD*float(np.mean(rotations[-1]['weighted']));conj=conjugacy(spline,rho,args.rays)
    coeff=np.fft.fft(delta)/args.rays;freqindex=np.abs(np.fft.fftfreq(args.rays,1/args.rays))
    result=dict(candidate=str(path),candidate_sha256=sha(path),candidate_metadata=meta,
        actual_amplitude=alpha,actual_nu=nu,turning=turn,rays=args.rays,waist_grid=N,
        complete_uniform_phi_initial=phi_initial.tolist(),complete_physical_initial=theta_initial.tolist(),
        complete_uniform_phi_return=returned.tolist(),complete_uniform_phi_derivative=derivative.tolist(),
        sampled_uniform_phi_displacement_range=[float(delta.min()),float(delta.max())],
        sampled_uniform_phi_derivative_range=[float(derivative.min()),float(derivative.max())],
        complete_return_displacement_fourier_real=coeff.real.tolist(),complete_return_displacement_fourier_imag=coeff.imag.tolist(),
        sampled_return_displacement_high_grid_tail_l1=float(np.sum(abs(coeff[freqindex>=args.rays/4]))),
        weighted_rotation_diagnostics=rotations,floating_conjugacy=conj,
        ray_calls=calls,wall_seconds=time.monotonic()-started)
    print(dict(candidate=str(path),rotation=rotations[-1]['weighted'],conjugacy_rho=conj['rho_turns'],
        conjugacy_residual=conj['doubled_twice_sampled_residual_sup'],conjugacy_failure=conj['failure'],
        high_grid_tail=result['sampled_return_displacement_high_grid_tail_l1'],wall_seconds=result['wall_seconds']),flush=True)
    return result


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--prior',type=Path,default=Path('notes/2026-11-13-R133-curvature-angle-principal-return-alpha070-alpha075-floating.json.gz'))
    ap.add_argument('--candidate',type=Path,nargs='+',required=True)
    ap.add_argument('--waist-grid',type=int,default=8192);ap.add_argument('--rays',type=int,default=512)
    ap.add_argument('--iterates',type=int,nargs='+',default=[10000,40000])
    ap.add_argument('--rtol',type=float,default=5e-12);ap.add_argument('--atol',type=float,default=5e-14)
    ap.add_argument('--maximum-x-step',type=float,default=.0075);ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve each uniform-angle return diagnostic')
    prior=read(args.prior)
    if not prior['complete'] or prior['object_sha256']!=sha(args.object):raise ValueError('complete earlier object identity missing')
    geometry,_=load_exact_object(args.object,512);entries=[];failure=None
    try:
        for path in args.candidate:entries.append(run(path,prior,geometry,args))
    except Exception as exc:failure=dict(type=type(exc).__name__,message=str(exc))
    doc=dict(kind='floating_uniform_curvature_angle_principal_return_and_conjugacy',
        complete=failure is None and len(entries)==len(args.candidate),certified=False,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in [args.object,args.prior,*args.candidate]},
        exact_producer_settings={k:v for k,v in vars(args).items() if not isinstance(v,Path) and k!='candidate'},
        entries=entries,failure=failure,all_original_candidate_modes_retained=True,
        true_turning_scattering_not_paid=True,actual_parameter_twist_not_proved=True,
        KAM_and_Diophantine_certificate_not_claimed=True,full_body_inverse_not_proved=True,
        wall_seconds=time.monotonic()-started)
    save(args.out,doc)
    if failure is not None:raise RuntimeError(str(failure))


if __name__=='__main__':main()
