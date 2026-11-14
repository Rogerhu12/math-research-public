#!/usr/bin/env python3
"""Floating full-candidate curvature-angle and principal-return diagnostic.

The exact identities are stated separately. All candidate Fourier modes
are read, but target evaluation, ray integration and rotation numbers here
are floating diagnostics only. No turning connection or high inverse is
inferred from this principal return.
"""
from __future__ import annotations
import argparse,gzip,json,time
from functools import lru_cache
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import PPoly,CubicSpline
from scipy.optimize import brentq
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_compact_metric_return_probe import bumps
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_reciprocal_candidate_tools import COORDINATES
from fourfold_phase_metric_defect import sha,save


PERIOD=np.pi/2


def inverse_derivative(values,frequencies):
    coeff=np.fft.fft(values)/len(values);out=np.zeros_like(coeff);nz=frequencies!=0
    out[nz]=coeff[nz]/(1j*frequencies[nz]);return np.fft.ifft(out).real*len(values)


def angular_fields(y,m,N):
    a=np.zeros((2,N),dtype=complex)
    a[0,1:m+1]=-.5j*y[:m];a[0,-m:]=.5j*y[:m][::-1]
    a[1,0]=y[m];a[1,1:m+1]=.5*y[m+1:];a[1,-m:]=.5*y[m+1:][::-1]
    f=4*np.fft.fftfreq(N,1/N)
    return np.fft.ifft(a,axis=1).real*N,np.fft.ifft(a*(1j*f),axis=1).real*N


def run_one(path,geometry,args):
    started=time.monotonic();saved=load_candidate(path);meta=json.loads(str(saved['metadata']))
    if meta['coordinates']!=COORDINATES or meta['object_sha256']!=sha(args.object):
        raise ValueError('a complete same-object reciprocal candidate is required')
    m=int(meta['modes']);alpha=float(meta['amplitude']);nu=float(meta['nu'])
    pp=PPoly(saved['piece_coefficients'],saved['radial_nodes']);body=RotationalBodyTarget(geometry)
    @lru_cache(maxsize=32768)
    def target(r):
        t=body.point(float(r));a,g,b,K,Cr=(t[k] for k in ('a','gamma','beta','K','Cref'))
        h,hp=bumps([r]);h,hp=h[0,0],hp[0,0];exp=np.exp(nu*h)
        G=g*g;D=a*a*G*Cr*Cr;Dn=D+G*np.expm1(nu*h)
        if Dn<=0:raise ValueError('controlled rotational denominator failed')
        return a,g*np.sqrt(exp),b,(K+b*nu*hp/(2*a*a*G))/exp,Cr*np.sqrt(Dn/(D*exp))
    mesh=np.linspace(0,.26,521);K=np.array([target(float(r))[3] for r in mesh])
    brackets=[(mesh[j],mesh[j+1]) for j in range(len(mesh)-1) if K[j]*K[j+1]<0]
    if not K[0]<0 or not brackets:raise ValueError('no first negative-to-positive turning bracket')
    turning=brentq(lambda r:target(float(r))[3],*brackets[0],xtol=5e-15,rtol=1e-14)
    if np.any(K[mesh<turning]>0):raise ValueError('the sampled waist band is not entirely negative')
    N=args.angular_grid;frequency=4*np.fft.fftfreq(N,1/N)
    samples=[];waist_phi_coeff=None;waist_D=None
    for radial in np.linspace(0,turning,args.radial_samples):
        r=float(radial);a,g,b,K,Cr=target(r);s=1/Cr;sr=b*s*(1-K*s*s)
        (U,V),(Ut,Vt)=angular_fields(pp(r),m,N);(Ur,Vr),_=angular_fields(pp(r,1),m,N)
        u=alpha*U;v=s+alpha*V;ut=alpha*Ut;vt=alpha*Vt;vr=sr+alpha*Vr
        if not np.max(v)<0:raise ValueError('sampled physical reciprocal chart changed sign')
        B=u/v;C=1/v;A=(u*u+K*v*v)/v
        Br=alpha*Ur/v-u*vr/(v*v);Ct=-vt/(v*v);Bt=ut/v-u*vt/(v*v);Crad=-vr/(v*v)
        At=2*B*Bt/C-A*Ct/C
        RB=Br-g*At+2*b*B;RC=Crad-g*Bt-b*(A-C)
        D=float(np.mean(C));Dr=float(np.mean(Crad));Am=float(np.mean(A));Rm=float(np.mean(RC))
        P=inverse_derivative(C-D,frequency);Pr=inverse_derivative(Crad-Dr,frequency)
        phi_t=C/D;phi_r=Pr/D-P*Dr/(D*D)
        drift=g*B/D-phi_r
        d_formula=g*np.mean(B)/D-b/D*inverse_derivative(A-Am*C/D,frequency)
        d_residual=-inverse_derivative(RC-Rm*C/D,frequency)/D
        dphi_formula=b*(Am/D-A/C)+Rm/D-RC/C
        dtheta=np.fft.ifft(1j*frequency*np.fft.fft(drift)).real
        omega=-g*np.sqrt(max(0.,-K))/D
        identity=max(float(np.max(abs(drift-d_formula-d_residual))),
            float(np.max(abs(dtheta/phi_t-dphi_formula))))
        samples.append(dict(r=r,K=float(K),D=D,phi_theta_min=float(np.min(phi_t)),
            phi_theta_max=float(np.max(phi_t)),omega=float(omega),
            sampled_drift_sup=float(np.max(abs(drift))),sampled_drift_phi_derivative_sup=float(np.max(abs(dphi_formula))),
            sampled_residual_drift_sup=float(np.max(abs(d_residual))),
            full_candidate_B_residual_sup=float(np.max(abs(RB))),full_candidate_C_residual_sup=float(np.max(abs(RC))),
            sampled_algebra_identity_error=identity))
        if r==0:
            waist_phi_coeff=np.fft.fft(P/D)/N;waist_D=D
    physical=4*np.arange(1,m+1,dtype=float)
    def field_at(r,theta):
        y=pp(float(r));a,g,b,K,Cr=target(float(r));s=1/Cr
        ang=physical[:,None]*np.remainder(theta,PERIOD)[None,:]
        si=np.sin(ang);co=np.cos(ang)
        U=y[:m]@si;Ut=(physical*y[:m])@co
        V=y[m]+y[m+1:]@co;Vt=-(physical*y[m+1:])@si
        return alpha*U,s+alpha*V,alpha*Ut,alpha*Vt,g,np.sqrt(max(0.,-K))
    progress=time.monotonic();counts={'+':0,'-':0}
    def ray_rhs(sign):
        label='+' if sign>0 else '-'
        def rhs(x,y):
            nonlocal progress
            counts[label]+=1;r=turning*(2*x-x*x);dr=2*turning*(1-x)
            theta,J=y[:args.rays],y[args.rays:]
            u,v,ut,vt,g,k=field_at(float(r),theta)
            speed=-dr*g*(u+sign*v*k);gradient=-dr*g*(ut+sign*vt*k)
            if time.monotonic()-progress>20:
                print(dict(stage='principal_rays',candidate=str(path),branch=label,x=float(x),calls=counts),flush=True)
                progress=time.monotonic()
            return np.r_[speed,gradient*J]
        return rhs
    angles=PERIOD*np.arange(args.rays)/args.rays
    first=solve_ivp(ray_rhs(1),(0.,1.),np.r_[angles,np.ones(args.rays)],method='DOP853',
        rtol=args.rtol,atol=args.atol,max_step=args.maximum_x_step)
    if not first.success:raise ValueError('forward principal ray solve failed')
    second=solve_ivp(ray_rhs(-1),(1.,0.),first.y[:,-1],method='DOP853',
        rtol=args.rtol,atol=args.atol,max_step=args.maximum_x_step)
    if not second.success:raise ValueError('backward principal ray solve failed')
    returned,J=second.y[:,-1][:args.rays],second.y[:,-1][args.rays:]
    if np.min(J)<=0:raise ValueError('sampled principal return is not orientation preserving')
    def waist_phi(theta):
        wrapped=np.remainder(theta,PERIOD)
        # Finite floating interpolation of the complete sampled inverse;
        # used only for this diagnostic coordinate report, never a proof.
        displacement=np.fft.ifft(waist_phi_coeff).real*N
        spline=CubicSpline(np.r_[PERIOD*np.arange(N)/N,PERIOD],np.r_[displacement,displacement[0]],bc_type='periodic')
        return theta+spline(wrapped)
    displacement=returned-angles
    flat_displacement=waist_phi(returned)-waist_phi(angles)
    spline=CubicSpline(np.r_[angles,PERIOD],np.r_[displacement,displacement[0]],bc_type='periodic')
    # This is an empirical rotation estimate from the interpolated return,
    # not a certified irrationality/Diophantine or KAM assertion.
    seeds=PERIOD*np.arange(8)/8;theta=seeds.copy();history={}
    for j in range(1,args.iterates+1):
        theta+=spline(np.remainder(theta,PERIOD))
        if j in {args.iterates//2,args.iterates}:
            history[str(j)]=((theta-seeds)/(PERIOD*j)).tolist()
    output=dict(candidate=str(path),candidate_sha256=sha(path),candidate_metadata=meta,
        first_turning_radius=float(turning),sampled_turning_brackets=[list(map(float,b)) for b in brackets],
        target_grid_K_range=[float(K) for K in (np.min([x['K'] for x in samples]),np.max([x['K'] for x in samples]))],
        actual_candidate_modes=m,actual_amplitude=alpha,actual_nu=nu,
        radial_samples=samples,rays=args.rays,angular_grid=N,ray_calls=counts,
        sampled_return_displacement_range=[float(displacement.min()),float(displacement.max())],
        sampled_curvature_angle_return_displacement_range=[float(flat_displacement.min()),float(flat_displacement.max())],
        sampled_return_derivative_range=[float(J.min()),float(J.max())],
        sampled_curvature_angle_half_roundtrip_phase=float(sum((samples[j+1]['r']-samples[j]['r'])*
            (samples[j+1]['omega']+samples[j]['omega'])/2 for j in range(len(samples)-1))),
        rotation_number_from_interpolated_principal_map=history,
        complete_sampled_return=dict(initial_angle=angles.tolist(),returned_angle=returned.tolist(),
            returned_derivative=J.tolist(),curvature_angle_displacement=flat_displacement.tolist()),
        waist_mean_C=waist_D,wall_seconds=time.monotonic()-started)
    print(dict(candidate=str(path),turning=turning,flat_return_range=output['sampled_curvature_angle_return_displacement_range'],
        rotation=history[str(args.iterates)],wall_seconds=output['wall_seconds']),flush=True)
    return output


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--candidate',type=Path,nargs='+',required=True)
    ap.add_argument('--angular-grid',type=int,default=4096);ap.add_argument('--radial-samples',type=int,default=65)
    ap.add_argument('--rays',type=int,default=256);ap.add_argument('--iterates',type=int,default=10000)
    ap.add_argument('--rtol',type=float,default=2e-10);ap.add_argument('--atol',type=float,default=2e-12)
    ap.add_argument('--maximum-x-step',type=float,default=.01);ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve each principal return diagnostic')
    geometry,definition=load_exact_object(args.object,512);entries=[];failure=None
    try:
        for path in args.candidate:entries.append(run_one(path,geometry,args))
    except Exception as exc:failure=dict(type=type(exc).__name__,message=str(exc))
    doc=dict(kind='floating_complete_candidate_curvature_angle_and_principal_return',
        complete=failure is None and len(entries)==len(args.candidate),certified=False,
        source_sha256=sha(__file__),object_sha256=sha(args.object),exact_center_parameter=definition['delta_fraction'],
        inputs={str(p):sha(p) for p in args.candidate},entries=entries,failure=failure,
        all_candidate_Fourier_modes_read=True,principal_return_only=True,
        true_turning_connection_not_supplied=True,small_divisor_bound_not_proved=True,
        whole_radial_angular_rounding_not_paid=True,new_metric_nu_not_old_type_fixed_object=True,
        wall_seconds=time.monotonic()-started,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_symmetric_geometry.py','fourfold_phase_codazzi_rotational_reference_probe.py',
            'fourfold_codazzi_compact_metric_return_probe.py','fourfold_codazzi_candidate_shards.py',
            'fourfold_codazzi_reciprocal_candidate_tools.py')})
    save(args.out,doc)
    if failure is not None:raise RuntimeError(str(failure))


if __name__=='__main__':main()
