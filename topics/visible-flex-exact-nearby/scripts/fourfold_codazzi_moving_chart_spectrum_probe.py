#!/usr/bin/env python3
"""Floating spectra in the exact moving-chart definition, without a tail claim.

The physical candidate keeps every stored mode. A periodic sampled
antiderivative of its full reciprocal C gives the approximate angular
coordinate, and the original finite U,V series is evaluated at every
recovered angle. Two grids diagnose numerical stability only.
"""
from __future__ import annotations
import argparse,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.interpolate import CubicSpline,PPoly
from flint import ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_reciprocal_candidate_tools import COORDINATES
from fourfold_codazzi_reciprocal_polynomial_system import ReciprocalPolynomial
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_phase_local_correction_probe import sha


def nonuniform_fields(U,V,theta,alpha,s):
    modes=4*np.arange(1,len(U)+1);out=np.empty((4,len(theta)))
    for first in range(0,len(theta),256):
        last=min(first+256,len(theta));phase=modes[:,None]*theta[None,first:last]
        sn,cs=np.sin(phase),np.cos(phase)
        out[0,first:last]=alpha*(U@sn)
        out[1,first:last]=s+alpha*(V[0]+V[1:]@cs)
        out[2,first:last]=alpha*((U*modes)@cs)
        out[3,first:last]=-alpha*((V[1:]*modes)@sn)
    return out


def measure(U,V,alpha,s,K,N):
    period=np.pi/2;theta=period*np.arange(N)/N;M=len(U)
    co=np.zeros(N,dtype=complex);ce=np.zeros(N,dtype=complex)
    co[1:M+1]=-.5j*alpha*U;co[-M:]=.5j*alpha*U[::-1]
    ce[0]=s+alpha*V[0];ce[1:M+1]=.5*alpha*V[1:];ce[-M:]=.5*alpha*V[1:][::-1]
    physical_u=(np.fft.ifft(co)*N).real;physical_v=(np.fft.ifft(ce)*N).real
    if np.any(physical_v>=0):raise ValueError('the sampled physical v chart is not negative')
    C=1/physical_v;D=float(np.mean(C));c=np.fft.fft(C)/N
    frequency=4*np.fft.fftfreq(N,1/N);primitive=np.zeros(N,dtype=complex)
    primitive[1:]=c[1:]/(D*1j*frequency[1:])
    deviation=(np.fft.ifft(primitive)*N).real;deviation-=deviation[0]
    phi=theta+deviation
    if np.any(np.diff(np.r_[phi,period])<=0):raise ValueError('sampled curvature coordinate is not ordered')
    spline=CubicSpline(np.r_[theta,period],np.r_[deviation,deviation[0]],bc_type='periodic')
    target_phi=theta.copy();inverse=np.interp(target_phi,np.r_[phi,period],np.r_[theta,period])
    for _ in range(6):inverse-=(inverse+spline(inverse)-target_phi)/(1+spline(inverse,1))
    u,v,ut,vt=nonuniform_fields(U,V,inverse,alpha,s)
    uq,vq=D*v*ut,D*v*vt
    fu,fv=np.fft.fft(u)/N,np.fft.fft(v)/N
    modes=abs(np.fft.fftfreq(N,1/N));tails=[]
    for cut in (8,16,32,64,128,256,512,1024):
        if cut>=N//2:continue
        tails.append(dict(mode_cut=cut,physical_frequency_cut=4*cut,
            sampled_U_tail_l1=float(np.sum(abs(fu[modes>cut]))),
            sampled_v_tail_l1=float(np.sum(abs(fv[modes>cut])))))
    report=dict(angles=N,quarter_period=period,physical_D=D,inverse_D=1/D,
        moving_mean_u=float(np.mean(u)),moving_mean_v=float(np.mean(v)),
        mean_v_minus_inverse_D=float(np.mean(v)-1/D),
        sampled_v_interval=[float(v.min()),float(v.max())],
        sampled_phi_theta_interval=[float((C/D).min()),float((C/D).max())],
        sampled_coordinate_inverse_residual=float(np.max(abs(inverse+spline(inverse)-target_phi))),
        physical_u_theta_abs=float(np.max(abs(ut))),physical_v_theta_abs=float(np.max(abs(vt))),
        moving_u_phi_abs=float(np.max(abs(uq))),moving_v_phi_abs=float(np.max(abs(vq))),
        sampled_full_U_l1=float(np.sum(abs(fu))),sampled_full_v_l1=float(np.sum(abs(fv))),tails=tails)
    if K<0:
        report.update(sampled_energy_R=float(np.max(np.sqrt(u*u-K*v*v))),
            sampled_energy_L=float(np.max(np.sqrt(uq*uq-K*vq*vq))))
    return report,fu,fv


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--radii',default='0,.05,.1,.15,.2,.2385,.3,1.5')
    ap.add_argument('--angles',type=int,default=8192);ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();tick=time.monotonic();ctx.prec=192;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve every original floating chart diagnostic')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']));M=int(meta['modes'])
    if meta['coordinates']!=COORDINATES or meta['object_sha256']!=sha(args.object):
        raise ValueError('complete same-target reciprocal input required')
    N=args.angles
    if N<8*M or N&(N-1):raise ValueError('invalid diagnostic angular resolution')
    radii=[float(Fraction(x)) for x in args.radii.split(',')]
    if min(radii)<saved['radial_nodes'][0] or max(radii)>saved['radial_nodes'][-1]:
        raise ValueError('no extrapolation of the actual stored candidate')
    geometry,_=load_exact_object(args.object,512);body=RotationalBodyTarget(geometry);graft=RotationalGraftTarget(geometry,args.object)
    system=ReciprocalPolynomial(geometry,M,8*M,body,graft);alpha=float(meta['amplitude']);nu=float(meta['nu'])
    system.alpha=alpha;pp=PPoly(saved['piece_coefficients'],saved['radial_nodes']);rows=[]
    for r in radii:
        y=pp(r);target=system.controlled([r],nu);s=1/float(target[5][0]);K=float(target[3][0]);pair=[];fourier=[]
        for grid in (N,2*N):
            result,fu,fv=measure(y[:M],y[M:],alpha,s,K,grid);pair.append(result);fourier.append((fu,fv))
        cut=min(1024,N//2-1);differences=[]
        for j in range(2):
            aa,bb=fourier[0][j],fourier[1][j]
            differences.append(float(np.sum(abs(aa[:cut+1]-bb[:cut+1]))+np.sum(abs(aa[-cut:]-bb[-cut:]))))
        rows.append(dict(radius=r,target_K=K,target_gamma=float(target[1][0]),target_beta=float(target[2][0]),
            grids=pair,compared_low_mode_cut=cut,complete_low_coefficient_l1_grid_difference=differences))
        print(dict(radius=r,moving_R=pair[-1].get('sampled_energy_R'),moving_L=pair[-1].get('sampled_energy_L'),
            mean_error=pair[-1]['mean_v_minus_inverse_D'],grid_coefficient_difference=differences,
            sampled_tail_64=pair[-1]['tails'][3],wall_seconds=time.monotonic()-tick),flush=True)
    doc=dict(kind='floating_complete_physical_to_moving_curvature_chart_spectrum',certified=False,
        complete_floating_run=True,source_sha256=sha(__file__),candidate_path=str(args.candidate),
        candidate_sha256=sha(args.candidate),object_sha256=sha(args.object),exact_nu=meta['exact_float_nu'],
        exact_alpha=str(Fraction.from_float(alpha)),physical_modes=M,rows=rows,
        all_original_physical_modes_kept=True,infinite_transformed_tail_certified=False,
        coordinate_inverse_method='sampled Fourier primitive, periodic cubic lift and six Newton steps',
        limitations=['Both angular grids are finite floating diagnostics; their difference is not a certified error.',
            'The reciprocal C Fourier tail and coordinate interpolation error are not rigorously enclosed.',
            'No projected moving-chart candidate is saved or called a solution.',
            'These point radii and sampled energy coefficients do not certify continuous Cauchy constants or geometry.'],
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_candidate_shards.py','fourfold_codazzi_reciprocal_candidate_tools.py',
            'fourfold_codazzi_reciprocal_polynomial_system.py','fourfold_phase_symmetric_geometry.py',
            'fourfold_phase_codazzi_rotational_reference_probe.py','fourfold_codazzi_rotational_cap_jacobi_probe.py')},
        wall_seconds=time.monotonic()-tick)
    args.out.write_text(json.dumps(doc,indent=2,allow_nan=False)+'\n')


if __name__=='__main__':main()
