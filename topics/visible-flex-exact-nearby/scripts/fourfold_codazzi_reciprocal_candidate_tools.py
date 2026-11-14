#!/usr/bin/env python3
"""Explicit coordinate conversion and full physical diagnostics for U,V.

No solver or repository state is changed. A converted projection is only a
warm start. The diagnostics retain the complete polynomial interior tail,
the rational physical boundary tail, both means and the metric parameter.
"""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.interpolate import PPoly
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_reciprocal_polynomial_system import ReciprocalPolynomial
from fourfold_phase_local_correction_probe import sha


COORDINATES='B=alpha*U/v; C=1/v; v=1/Cref_nu+alpha*V'
OLD_COORDINATES='B=alpha*b; C=Cref_nu+alpha*c'


def finite_fields(y,m,N):
    """Independent complete old sine/cosine synthesis at the chosen grid."""
    fo=np.zeros((N,y.shape[1]),dtype=complex);fe=np.zeros_like(fo)
    fo[1:m+1]=-.5j*y[:m];fo[-m:]=.5j*y[:m][::-1]
    fe[0]=y[m];fe[1:m+1]=.5*y[m+1:];fe[-m:]=.5*y[m+1:][::-1]
    return np.fft.ifft(fo,axis=0).real*N,np.fft.ifft(fe,axis=0).real*N


def load_warm_start(system,path,r,*,object_sha256,batch=32):
    path=Path(path);saved=load_candidate(path);meta=json.loads(str(saved['metadata']))
    if (meta['object_sha256']!=object_sha256 or meta['coordinates'] not in (COORDINATES,OLD_COORDINATES)
        or meta['physical_frequency_factor']!=4):raise ValueError('incompatible actual reciprocal warm start')
    pm=int(meta['modes']);m=system.modes
    if m<pm:raise ValueError('this warm-start interface never silently drops old retained modes')
    r=np.asarray(r,dtype=float)
    if np.min(r)<saved['radial_nodes'][0] or np.max(r)>saved['radial_nodes'][-1]:
        raise ValueError('no radial extrapolation of the complete old candidate')
    pp=PPoly(saved['piece_coefficients'],saved['radial_nodes']);p=np.array([float(meta['nu'])])
    prior_alpha=float(meta['amplitude']);guess=np.zeros((2*m+1,len(r)));b_error=0.;c_error=0.
    for start in range(0,len(r),batch):
        rr=r[start:start+batch];y=pp(rr).T
        if meta['coordinates']==COORDINATES:
            guess[:pm,start:start+len(rr)]=y[:pm]
            guess[m:m+pm+1,start:start+len(rr)]=y[pm:]
            continue
        b,c=finite_fields(y,pm,system.angular_grid);Cr=system.controlled(rr,p[0])[5]
        C=Cr+prior_alpha*c
        if np.any(C==0):raise ZeroDivisionError('old complete candidate leaves the physical C chart')
        U=b/C;V=-c/(Cr*C);yn=system.project(U,V);guess[:,start:start+len(rr)]=yn
        up,vp=system.fields(yn);v=1/Cr+prior_alpha*vp
        if np.any(v==0):raise ZeroDivisionError('projected reciprocal warm start leaves its chart')
        b_error=max(b_error,float(np.max(abs(prior_alpha*up/v-prior_alpha*b))))
        c_error=max(c_error,float(np.max(abs(1/v-C))))
    detail=dict(source_candidate=str(path),source_candidate_sha256=sha(path),source_coordinates=meta['coordinates'],
        target_coordinates=COORDINATES,source_modes=pm,target_modes=m,full_original_modes_read=True,
        radial_nodes=len(r),old_amplitude=prior_alpha,new_amplitude=float(system.alpha),
        exact_old_nu=str(Fraction.from_float(float(meta['nu']))),
        same_old_alpha_projection_physical_B_error=b_error,same_old_alpha_projection_physical_C_error=c_error,
        conversion_is_only_a_floating_warm_start=True,conversion_does_not_solve_boundary_or_PDE=True)
    return guess,p,saved,meta,detail


def diagnostic(system,result):
    if not np.all(np.isfinite(result.sol.c)):return dict(valid=False,reason='nonfinite reciprocal collocation polynomial')
    m=system.modes;al=system.alpha
    fine=ReciprocalPolynomial(system.geometry,m,2*system.angular_grid,system.body,system.graft,
        mean_boundary=system.mean_boundary,right=system.right_boundary)
    fine.alpha=al;fine.all_base_cache=system.all_base_cache
    rr=np.unique(np.r_[result.x,*[result.x[:-1]+z*np.diff(result.x) for z in (.25,.5,.75)]])
    names=('normalized_finite_residual','normalized_full_U_residual','normalized_full_V_residual',
        'complete_U_residual_Fourier_l1','complete_V_residual_Fourier_l1',
        'actual_full_B_residual','actual_full_C_residual','independent_physical_residual_identity_error',
        'polynomial_residual_beyond_3M_roundoff_l1','U_rhs_projection_defect','V_rhs_projection_defect')
    out={k:0. for k in names};out.update(C_min=np.inf,C_max=-np.inf,B_abs_max=0.,v_min=np.inf,v_max=-np.inf)
    N=fine.angular_grid;kk=np.abs(np.fft.fftfreq(N,1/N))
    for start in range(0,len(rr),16):
        r=rr[start:start+16];y=result.sol(r);yr=result.sol(r,1)
        fu,fv,z=fine.physical_rhs(r,y,result.p)
        a,g,beta,K,ell,Cr,*_=z['target'];s=z['s'];v=z['v'];u=al*z['U']
        if np.any(v==0) or not np.all(np.isfinite(v)):
            return dict(valid=False,reason='sampled reciprocal chart v vanishes or is nonfinite')
        Ur,Vr=fine.fields(yr);Ru=Ur-fu;Rv=Vr-fv
        B=u/v;C=1/v;A=(K+B*B)/C
        RB=al*(Ru/v-u*Rv/(v*v));RC=-al*Rv/(v*v)
        # Independent physical-coordinate residual: no use of the residual
        # transformation in this branch of the diagnostic.
        sr=beta*s*(1-K*s*s);ur=al*Ur;vr=sr+al*Vr;ut=al*z['Ut'];vt=al*z['Vt']
        Br=ur/v-u*vr/(v*v);Crad=-vr/(v*v)
        Bt=ut/v-u*vt/(v*v);Ct=-vt/(v*v);At=2*B*Bt/C-A*Ct/C
        RBdirect=Br-g*At+2*beta*B;RCdirect=Crad-g*Bt-beta*(A-C)
        finite=yr-system.evaluate(r,y,result.p);feU,feV=fine.fields(finite)
        fftu=np.fft.fft(Ru,axis=0)/N;fftv=np.fft.fft(Rv,axis=0)/N
        proj=fine.project(fu,fv);projU,projV=fine.fields(proj)
        vals=dict(normalized_finite_residual=max(float(np.max(abs(feU))),float(np.max(abs(feV)))),
            normalized_full_U_residual=float(np.max(abs(Ru))),normalized_full_V_residual=float(np.max(abs(Rv))),
            complete_U_residual_Fourier_l1=float(np.max(np.sum(abs(fftu),axis=0))),
            complete_V_residual_Fourier_l1=float(np.max(np.sum(abs(fftv),axis=0))),
            actual_full_B_residual=float(np.max(abs(RB))),actual_full_C_residual=float(np.max(abs(RC))),
            independent_physical_residual_identity_error=max(float(np.max(abs(RB-RBdirect))),float(np.max(abs(RC-RCdirect)))),
            polynomial_residual_beyond_3M_roundoff_l1=max(float(np.max(np.sum(abs(fftu[kk>3*m]),axis=0))),
                float(np.max(np.sum(abs(fftv[kk>3*m]),axis=0)))),
            U_rhs_projection_defect=float(np.max(abs(fu-projU))),V_rhs_projection_defect=float(np.max(abs(fv-projV))))
        if not all(np.isfinite(x) for x in vals.values()):return dict(valid=False,reason='nonfinite full reciprocal diagnostic')
        for k,value in vals.items():out[k]=max(out[k],value)
        out['C_min']=min(out['C_min'],float(np.min(C)));out['C_max']=max(out['C_max'],float(np.max(C)))
        out['B_abs_max']=max(out['B_abs_max'],float(np.max(abs(B))))
        out['v_min']=min(out['v_min'],float(np.min(v)));out['v_max']=max(out['v_max'],float(np.max(v)))
    left=result.sol(result.x[0]);right=result.sol(result.x[-1]);p=result.p
    bl,cl=fine.physical_normalized_fields([0.],left,p);br,cr=fine.physical_normalized_fields([system.right_boundary],right,p)
    flb=np.fft.fft(bl[:,0])/N;flc=np.fft.fft(cl[:,0])/N
    frb=np.fft.fft(br[:,0])/N;frc=np.fft.fft(cr[:,0])/N
    signs=np.sign(np.fft.fftfreq(N,1/N));robin=1j*signs*frb+system.qstar*frc;robin[0]=0
    a0=fine.base([0.])[0,0];Cr0=fine.controlled([0.],p[0])[5][0]
    out.update(full_physical_boundary=dict(
        actual_waist_B_sup=float(abs(al)*np.max(abs(bl))),
        normalized_waist_c_fourth_plus_one_abs=float(abs(2*flc[1].real+1)),
        actual_waist_mean_C_plus_inverse_a=float(Cr0+al*flc[0].real+1/a0),
        actual_outer_C_mean_minus_reference=float(al*frc[0].real),
        normalized_all_sampled_nonmean_Robin_l1=float(np.sum(abs(robin))),
        normalized_retained_Robin_l1=float(np.sum(abs(robin[(kk>0)&(kk<=m)]))),
        normalized_unretained_Robin_tail_l1=float(np.sum(abs(robin[kk>m]))),
        normalized_Robin_high_grid_tail_l1=float(np.sum(abs(robin[kk>=N/4]))),
        right_Robin_remains_the_stated_linear_reference=True,
        true_nonlinear_regular_relation_not_claimed=True),
        radial_samples='all nodes and quarter/mid/three-quarter points',radial_sample_count=len(rr),
        actual_angular_grid=N,full_interior_polynomial_support=3*m,
        valid=bool(out['C_max']<0 and np.isfinite(out['C_min'])),
        mathematical_certificate=False,complete_continuous_rounding_error_not_paid=True)
    return out
