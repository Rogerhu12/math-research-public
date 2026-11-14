#!/usr/bin/env python3
"""Explicit moving-angle warm projection and complete floating diagnostics.

The original physical candidate is read with every retained coefficient.
Any new-chart projection is ONLY a starting guess. Full mean, all interior
3M frequencies, physical residual pullback and sampled boundary tails are
reported after the actual new solve.
"""
from __future__ import annotations
import hashlib,json,os
from pathlib import Path
import numpy as np
from scipy.interpolate import PPoly
from fourfold_codazzi_moving_polynomial_system import MovingPolynomial,COORDINATES
from fourfold_codazzi_reciprocal_candidate_tools import COORDINATES as PHYSICAL_COORDINATES
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_moving_chart_spectrum_probe import measure
from fourfold_phase_local_correction_probe import sha


def load_warm_start(system,path,r,*,object_sha256,allow_projection=False,cache_root=None):
    path=Path(path);saved=load_candidate(path);meta=json.loads(str(saved['metadata']))
    if meta['object_sha256']!=object_sha256 or meta['coordinates'] not in (COORDINATES,PHYSICAL_COORDINATES):
        raise ValueError('same-object complete moving or physical reciprocal input required')
    r=np.asarray(r);pm=int(meta['modes']);M=system.modes
    if r.min()<saved['radial_nodes'][0] or r.max()>saved['radial_nodes'][-1]:raise ValueError('no warm-start radial extrapolation')
    if (meta['coordinates']!=COORDINATES or M<pm) and not allow_projection:
        raise ValueError('a changed-chart or lower-mode guess needs explicit --project-warm-start')
    prior_alpha=float(meta['amplitude']);p=np.array([float(meta['nu'])])
    pp=PPoly(saved['piece_coefficients'],saved['radial_nodes'])
    N=1
    while N<max(2048,16*pm,16*M):N*=2
    identity=dict(source_candidate_sha256=sha(path),source_coordinates=meta['coordinates'],
        object_sha256=object_sha256,source_modes=pm,target_modes=M,conversion_angles=N,
        original_alpha=prior_alpha,new_alpha=float(system.alpha),nu=float(p[0]),
        radial_nodes_sha256=hashlib.sha256(r.tobytes()).hexdigest(),source_sha256=sha(__file__))
    key=hashlib.sha256(json.dumps(identity,sort_keys=True).encode()).hexdigest()
    root=Path(cache_root or '/workspace/scratch/ac0d699811ad/moving_warm_start');root.mkdir(parents=True,exist_ok=True)
    cache=root/(key+'.npz');guess=np.zeros((2*M+1,len(r)));start=0;utail=vtail=meanerror=0.
    if cache.exists():
        with np.load(cache,allow_pickle=False) as old:
            if str(old['identity'])!=json.dumps(identity,sort_keys=True) or not np.array_equal(old['r'],r):raise ValueError('wrong complete warm cache identity')
            start=int(old['completed']);guess=old['guess'].copy()
            if guess.shape!=(2*M+1,len(r)) or not 0<=start<=len(r):raise ValueError('incomplete warm cache shape')
            if hashlib.sha256(guess[:,:start].tobytes()).hexdigest()!=str(old['prefix_sha256']):raise ValueError('warm completed prefix hash mismatch')
            utail,vtail,meanerror=map(float,(old['utail'],old['vtail'],old['meanerror']))
        print(dict(restored_explicit_moving_warm_prefix=start,expected=len(r),identity=key),flush=True)
    def persist(done):
        temporary=cache.with_name(cache.name+'.partial')
        with temporary.open('wb') as stream:
            np.savez_compressed(stream,identity=np.array(json.dumps(identity,sort_keys=True)),r=r,
                guess=guess,completed=np.array(done),prefix_sha256=np.array(hashlib.sha256(guess[:,:done].tobytes()).hexdigest()),
                utail=np.array(utail),vtail=np.array(vtail),meanerror=np.array(meanerror))
        os.replace(temporary,cache)
    targets=system.controlled(r,p[0]);signed=np.abs(np.fft.fftfreq(N,1/N))
    for i in range(start,len(r)):
        y=pp(float(r[i]))
        if meta['coordinates']==COORDINATES:
            k=min(M,pm);guess[:k,i]=y[:k];guess[M:M+k+1,i]=y[pm:pm+k+1]
            utail=max(utail,float(np.sum(abs(y[M:pm]))) if M<pm else 0.)
            vtail=max(vtail,float(np.sum(abs(y[pm+M+1:]))) if M<pm else 0.)
        else:
            s=1/float(targets[5][i]);K=float(targets[3][i])
            report,fu,fv=measure(y[:pm],y[pm:],prior_alpha,s,K,N)
            guess[:M,i]=-2*fu.imag[1:M+1]/prior_alpha
            guess[M,i]=(fv[0].real-s)/prior_alpha
            guess[M+1:,i]=2*fv.real[1:M+1]/prior_alpha
            utail=max(utail,float(np.sum(abs(fu[signed>M]))/prior_alpha))
            vtail=max(vtail,float(np.sum(abs(fv[signed>M]))/prior_alpha))
            meanerror=max(meanerror,abs(report['mean_v_minus_inverse_D']))
        if not np.all(np.isfinite(guess[:,i])):raise ValueError('nonfinite explicit moving warm projection')
        if (i+1)%16==0 or i==len(r)-1:
            persist(i+1);print(dict(explicit_moving_warm_completed=i+1,expected=len(r),
                maximum_sampled_discarded_U_l1=utail,maximum_sampled_discarded_V_l1=vtail),flush=True)
    detail=dict(**identity,target_coordinates=COORDINATES,radial_nodes=len(r),
        original_all_retained_modes_read=True,explicit_projected_warm_start=bool(meta['coordinates']!=COORDINATES or M<pm),
        maximum_sampled_discarded_normalized_U_tail=utail,maximum_sampled_discarded_normalized_V_tail=vtail,
        maximum_sampled_curvature_mean_identity_error=meanerror,
        warm_cache=str(cache),warm_cache_sha256=sha(cache),
        warm_projection_is_not_a_solution_or_a_tail_certificate=True)
    return guess,p,saved,meta,detail


def sampled_physical_moments(system,r,y,p,maximum_mode):
    z=system.moving_data([r],np.asarray(y)[:,None],p);N=system.angular_grid;al=system.alpha
    U=z['U'][:,0];V=z['V'][:,0];m=float(z['mean'][0]);Cr=float(z['target'][5][0])
    phi=(np.pi/2)*np.arange(N)/N;theta=phi+al*system.primitive(V)/m
    k=4*np.arange(1,maximum_mode+1)[:,None]
    b=2*np.mean(np.sin(k*theta)*U,axis=1)/m
    c=2*np.mean(np.cos(k*theta),axis=1)/(al*m)
    return b,c,-Cr*float(y[system.modes])/m


def diagnostic(system,result):
    if not np.all(np.isfinite(result.sol.c)):return dict(valid=False,reason='nonfinite moving PPoly')
    M=system.modes;al=system.alpha;N=2*system.angular_grid
    fine=MovingPolynomial(system.geometry,M,N,system.body,system.graft,
        q_path=system.q_path,mean_boundary=system.mean_boundary)
    fine.alpha=al;fine.all_base_cache=system.all_base_cache
    r=np.unique(np.r_[result.x,*[result.x[:-1]+f*np.diff(result.x) for f in (.25,.5,.75)]])
    keys=('normalized_finite_residual','normalized_full_U_residual','normalized_full_V_residual',
        'complete_U_residual_Fourier_l1','complete_V_residual_Fourier_l1',
        'actual_full_physical_B_residual','actual_full_physical_C_residual',
        'independent_physical_residual_identity_error','polynomial_residual_beyond_3M_roundoff_l1')
    out={k:0. for k in keys};out.update(C_min=np.inf,C_max=-np.inf,B_abs_max=0.,v_min=np.inf,v_max=-np.inf)
    modes=abs(np.fft.fftfreq(N,1/N))
    for start in range(0,len(r),16):
        rr=r[start:start+16];y=result.sol(rr);yr=result.sol(rr,1)
        fu,fv,z=fine.moving_rhs(rr,y,result.p);U,V,Ut,Vt,v,m=(z[k] for k in ('U','V','Ut','Vt','v','mean'))
        g=z['target'][1];beta=z['target'][2];K=z['target'][3];s=z['s']
        if np.any(v>=0) or not np.all(np.isfinite(v)):return dict(valid=False,reason='sampled moving v is not negative')
        Ur,Vr=fine.fields(yr);Ru=Ur-fu;Rv=Vr-fv;u=al*U;up=al*Ut;vp=al*Vt
        # Exact inverse coordinate differential on the FULL nonlinear residual.
        ru=al*Ru;rv=al*Rv
        displacement=fine.primitive(rv-v*np.mean(rv,axis=0)/m)/v
        physical_ru=ru-up*displacement;physical_rv=rv-vp*displacement
        RB=physical_ru/v-u*physical_rv/(v*v);RC=-physical_rv/(v*v)
        # Independent fixed-theta differentiation of the actual inverse lift.
        sr=beta*s*(1-K*s*s);ur=al*Ur;vr=sr+al*Vr;mr=sr+al*yr[M]
        theta_r=fine.primitive(vr-v*mr/m)/m
        urtheta=ur-(m/v)*theta_r*up;vrtheta=vr-(m/v)*theta_r*vp
        ut=(m/v)*up;vt=(m/v)*vp
        direct_u=urtheta-g*(u*ut+K*v*vt)+beta*u*(1+u*u+K*v*v)
        direct_v=vrtheta-g*(u*vt-v*ut)-beta*v*(1-u*u-K*v*v)
        B=u/v;C=1/v
        RBdirect=direct_u/v-u*direct_v/(v*v);RCdirect=-direct_v/(v*v)
        finite=yr-system.evaluate(rr,y,result.p);rU,rV=fine.fields(finite)
        ff=np.fft.fft(np.stack((Ru,Rv)),axis=1)/N
        values=dict(normalized_finite_residual=max(float(np.max(abs(rU))),float(np.max(abs(rV)))),
            normalized_full_U_residual=float(np.max(abs(Ru))),normalized_full_V_residual=float(np.max(abs(Rv))),
            complete_U_residual_Fourier_l1=float(np.max(np.sum(abs(ff[0]),axis=0))),
            complete_V_residual_Fourier_l1=float(np.max(np.sum(abs(ff[1]),axis=0))),
            actual_full_physical_B_residual=float(np.max(abs(RB))),actual_full_physical_C_residual=float(np.max(abs(RC))),
            independent_physical_residual_identity_error=max(float(np.max(abs(RB-RBdirect))),float(np.max(abs(RC-RCdirect)))),
            polynomial_residual_beyond_3M_roundoff_l1=float(np.max(np.sum(abs(ff[:,modes>3*M]),axis=1))))
        if not all(np.isfinite(z) for z in values.values()):return dict(valid=False,reason='nonfinite full moving diagnostic')
        for key,value in values.items():out[key]=max(out[key],value)
        out['C_min']=min(out['C_min'],float(np.min(C)));out['C_max']=max(out['C_max'],float(np.max(C)))
        out['B_abs_max']=max(out['B_abs_max'],float(np.max(abs(B))))
        out['v_min']=min(out['v_min'],float(np.min(v)));out['v_max']=max(out['v_max'],float(np.max(v)))
    maxmode=min(4*M,N//8);left=result.sol(result.x[0]);right=result.sol(result.x[-1]);p=result.p
    lb,lc,lmean=sampled_physical_moments(fine,0.,left,p,maxmode)
    rb,rc,rmean=sampled_physical_moments(fine,system.right_boundary,right,p,maxmode)
    b0,c0,*_=system.boundary_jet(system.right_boundary,right,p)
    q=system.q_vector;Q=system.q_tail_bound
    a0=float(fine.base([0.])[0,0]);Cr0=float(fine.controlled([0.],p[0])[5][0])
    out.update(full_physical_boundary=dict(actual_waist_B_sampled_moment_l1=float(al*np.sum(abs(lb))),
        normalized_waist_physical_fourth_plus_one_abs=float(abs(lc[0]+1)),
        actual_waist_mean_C_plus_inverse_a=Cr0+al*lmean+1/a0,
        actual_outer_mean_C_minus_reference=float(al*rmean),
        normalized_retained_Robin_l1=float(np.sum(abs(rb[:M]+q*rc[:M]))),
        sampled_unretained_physical_b_moment_tail=float(np.sum(abs(rb[M:]))),
        sampled_unretained_physical_c_moment_tail=float(np.sum(abs(rc[M:]))),
        sampled_unretained_Robin_tail_upper=None if Q is None else float(np.sum(abs(rb[M:]))+Q*np.sum(abs(rc[M:]))),
        retained_moment_quadrature_grid_difference_l1=float(np.sum(abs(b0-rb[:M]))+np.sum(abs(c0[1:]-rc[:M]))),
        maximum_sampled_physical_mode=maxmode,all_infinite_boundary_tails_and_quadrature_error_unpaid=True,
        true_nonlinear_cap_remainder_and_mean_correction_unpaid=True),
        radial_samples='all nodes and quarter/mid/three-quarter points',radial_sample_count=len(r),
        moving_angular_grid=N,full_interior_polynomial_support=3*M,
        valid=bool(out['C_max']<0 and np.isfinite(out['C_min'])),mathematical_certificate=False,
        complete_continuous_rounding_error_not_paid=True)
    return out
