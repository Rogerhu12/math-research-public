#!/usr/bin/env python3
"""Explicit approximate stable-cap extension for a complete moving guess.

No saved spline is extrapolated. All original body coefficients remain;
only the missing positive cap is initialized from the complete retained
physical moments and the actual target's linear regular graph. This warm
extension is not an equation, a solution, or an infinite-tail certificate.
"""
from pathlib import Path
import hashlib,json
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import PPoly
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_moving_polynomial_system import COORDINATES
from fourfold_codazzi_moving_candidate_tools import load_warm_start as body_load,sampled_physical_moments
from fourfold_phase_local_correction_probe import sha

def load_warm_start(system,path,r,*,object_sha256,allow_projection=False,cache_root=None,allow_extension=False):
    saved=load_candidate(path);meta=json.loads(str(saved['metadata']));right=float(saved['radial_nodes'][-1])
    if right>=system.right_boundary:
        return body_load(system,path,r,object_sha256=object_sha256,allow_projection=allow_projection,cache_root=cache_root)
    if not allow_extension or right!=1.5 or system.right_boundary!=3.125 or meta['coordinates']!=COORDINATES:
        raise ValueError('a missing cap needs the explicit complete 3/2 to 25/8 warm extension')
    r=np.asarray(r);inside=r<=right
    body,p,saved,meta,detail=body_load(system,path,r[inside],object_sha256=object_sha256,
        allow_projection=allow_projection,cache_root=cache_root)
    M=system.modes;al=system.alpha;nu=float(p[0]);freq=4*np.arange(1,M+1)
    if int(meta['modes'])!=M:raise ValueError('the cap extension must retain every original moving mode')
    identity=dict(source_candidate_sha256=sha(path),source_sha256=sha(__file__),object_sha256=object_sha256,
        q_sha256=sha(system.q_path),alpha=al,nu=nu,radial_nodes_sha256=hashlib.sha256(r.tobytes()).hexdigest(),
        source_coordinates=COORDINATES,all_body_modes_retained=True,no_spline_extrapolation=True)
    root=Path(cache_root or '/workspace/scratch/ac0d699811ad/moving_warm_start');root.mkdir(parents=True,exist_ok=True)
    key=hashlib.sha256(json.dumps(identity,sort_keys=True).encode()).hexdigest();cache=root/(key+'-regular-cap.npz')
    if cache.exists():
        with np.load(cache,allow_pickle=False) as old:
            if str(old['identity'])!=json.dumps(identity,sort_keys=True) or not np.array_equal(old['r'],r):raise ValueError('wrong complete cap warm cache')
            guess=old['guess'].copy();extra=json.loads(str(old['detail']))
        if guess.shape!=(2*M+1,len(r)) or not np.all(np.isfinite(guess)):raise ValueError('incomplete cap warm cache')
        detail.update(extra);detail.update(regular_cap_warm_cache=str(cache),regular_cap_warm_cache_sha256=sha(cache))
        return guess,p,saved,meta,detail
    # The vector follows the actual body/graft reference, not an extrapolated
    # cubic nor the false mode-dependent square-root formula.
    def target(x):
        z=system.body.point(float(x)) if x<=3 else system.graft.point(float(x))
        return z['gamma'],z['beta'],z['lambda_ref'],z['Cref']
    def qrhs(x,q):
        gamma,beta,lam,_=target(x)
        return freq*gamma*(q*q-lam)+beta*(lam-1)*q
    qsol=solve_ivp(qrhs,(system.right_boundary,right),system.q_vector.copy(),method='DOP853',
        rtol=2e-11,atol=2e-13,max_step=.004,dense_output=True)
    if not qsol.success:raise ValueError('actual linear q warm extension failed: '+qsol.message)
    def logr(x,z):
        gamma,beta,lam,_=target(x)
        return -freq*gamma*qsol.sol(x)-beta*(1+lam)
    lsol=solve_ivp(logr,(right,system.right_boundary),np.zeros(M),method='DOP853',
        rtol=2e-11,atol=2e-13,max_step=.004,dense_output=True)
    if not lsol.success:raise ValueError('actual linear amplitude warm extension failed: '+lsol.message)
    pp=PPoly(saved['piece_coefficients'],saved['radial_nodes'])
    # Same-alpha body_load keeps the normalized coefficient state. If alpha
    # changes, the new solve still receives only an explicit approximate guess.
    bcut,ccut,cmean=sampled_physical_moments(system,right,body[:,-1],p,M)
    N=max(2048,16*M);phi=(np.pi/2)*np.arange(N)/N;indices=abs(np.fft.fftfreq(N,1/N))
    guess=np.zeros((2*M+1,len(r)));guess[:,inside]=body
    maximum_inverse_error=maximum_sampled_tail=0.;cut_row=None
    for j,x in enumerate(r):
        if x<right:continue
        _,_,_,Cr=target(x);q=qsol.sol(x);c=ccut*np.exp(lsol.sol(x));theta=phi.copy()
        for iteration in range(16):
            phase=freq[:,None]*theta;ss=np.sin(phase);cc=np.cos(phase)
            C=Cr+al*(c@cc);lift=theta+(al/Cr)*((c/freq)@ss);err=lift-phi
            if np.max(abs(err))<2e-13:break
            if np.any(C/Cr<=0):raise ValueError('the approximate cap warm lift is not monotone')
            theta-=err/(C/Cr)
        else:raise ValueError('cap warm angle inversion failed')
        B=-al*((q*c)@ss);u=B/C;v=1/C;fu=np.fft.fft(u)/N;fv=np.fft.fft(v)/N
        row=np.r_[-2*fu.imag[1:M+1]/al,(fv[0].real-1/Cr)/al,2*fv.real[1:M+1]/al]
        if x==right:cut_row=row
        else:guess[:,j]=row
        maximum_inverse_error=max(maximum_inverse_error,float(np.max(abs(err))))
        maximum_sampled_tail=max(maximum_sampled_tail,float(np.sum(abs(fu[indices>M]))+np.sum(abs(fv[indices>M]))))
    if cut_row is None:raise ValueError('the original cap cut must remain a mesh node')
    extra=dict(actual_positive_cap_warm_extension=True,complete_original_body_preserved=True,
        source_cap_cut=right,actual_regular_endpoint=system.right_boundary,
        cap_extension_is_only_a_starting_guess=True,cap_extension_uses_true_body_and_natural_graft=True,
        cap_extension_q_source_sha256=sha(system.q_path),all_cap_q_columns=M,
        cap_q_solver_success=bool(qsol.success),cap_amplitude_solver_success=bool(lsol.success),
        cap_extension_Robin_mismatch_at_original_cut=float(np.sum(abs(bcut+qsol.sol(right)*ccut))),
        cap_extension_mean_at_original_cut=float(cmean),
        cap_extension_state_join_difference=float(np.max(abs(cut_row-body[:,-1]))),
        cap_extension_inverse_angle_sampled_residual=maximum_inverse_error,
        cap_extension_sampled_projection_tail=maximum_sampled_tail,
        no_spline_extrapolation=True,all_infinite_tails_and_quadrature_errors_unpaid=True)
    temporary=cache.with_name(cache.name+'.partial')
    with temporary.open('wb') as out:np.savez_compressed(out,identity=np.array(json.dumps(identity,sort_keys=True)),r=r,guess=guess,detail=np.array(json.dumps(extra)))
    temporary.replace(cache);detail.update(extra)
    detail.update(regular_cap_warm_cache=str(cache),regular_cap_warm_cache_sha256=sha(cache))
    print(dict(complete_actual_cap_warm_extension=extra),flush=True)
    return guess,p,saved,meta,detail
