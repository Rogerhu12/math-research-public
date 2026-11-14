#!/usr/bin/env python3
"""Full moving diagnostics at the supplied actual regular boundary.

All cubic interior frequencies and physical moment tails are reported.
This floating consumer makes no continuous or infinite-tail claim.
"""
import numpy as np
from fourfold_codazzi_moving_candidate_tools import sampled_physical_moments

def diagnostic(system,result):
    if not np.all(np.isfinite(result.sol.c)):return dict(valid=False,reason='nonfinite moving PPoly')
    M=system.modes;al=system.alpha;N=2*system.angular_grid
    fine=type(system)(system.geometry,M,N,system.body,system.graft,
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
