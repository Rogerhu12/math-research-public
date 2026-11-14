#!/usr/bin/env python3
"""Executed full small moving-chart derivatives and physical-moment checks.

These are floating implementation checks, not a continuous certificate.
Every finite column, the parameter, mean feedback and degree-2M intermediate
are exercised. Complete physical moments are compared to an independently
inverted uniform physical-angle grid.
"""
from __future__ import annotations
import argparse,json,time
from pathlib import Path
import numpy as np
from flint import ctx
from fourfold_codazzi_moving_polynomial_system import MovingPolynomial
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_phase_local_correction_probe import sha


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--q-vector',type=Path,default=Path('notes/2026-11-13-R133-cap-cut-r15-q256-with-tail.json'))
    args=ap.parse_args();tick=time.monotonic();ctx.prec=192;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve every actual operator audit')
    geo,_=load_exact_object(args.object,512);body=RotationalBodyTarget(geo);graft=RotationalGraftTarget(geo,args.object)
    M=7;N=64;n=2*M+1
    system=MovingPolynomial(geo,M,N,body,graft,q_path=args.q_vector);system.alpha=.75
    r=np.array([0.,.1,.145,.2383968743,.3,1.5]);p=np.array([-.035]);rng=np.random.default_rng(20261113)
    y=.09*rng.standard_normal((n,len(r)))
    y[:M]/=np.arange(1,M+1)[:,None]**2
    y[M:]/=(1+np.arange(M+1))[:,None]**2
    J,Jp=system.jacobian(r,y,p);action=system.full_action(r,y,p)
    action_errors=[];derivative_errors=[];step=2.**-19
    for j in range(n):
        d=np.zeros_like(y);d[j]=1
        action_errors.append(float(np.max(abs(action(d,0.)-J[:,j]))))
        fd=(system.evaluate(r,y+step*d,p)-system.evaluate(r,y-step*d,p))/(2*step)
        derivative_errors.append(float(np.max(abs(fd-J[:,j]))))
    action_errors.append(float(np.max(abs(action(np.zeros_like(y),1.)-Jp[:,0]))))
    fp=(system.evaluate(r,y,p+step)-system.evaluate(r,y,p-step))/(2*step)
    derivative_errors.append(float(np.max(abs(fp-Jp[:,0]))))
    fu,fv,z=system.moving_rhs(r,y,p);beta=z['target'][2];K=z['target'][3]
    sr=beta*z['s']*(1-K*z['s']**2)
    mean_error=float(np.max(abs(sr+system.alpha*np.mean(fv,axis=0)-beta*z['mean']*(1-np.mean(z['S'],axis=0)))))
    tails=system.rhs_tail(r,y,p);boundary=[]
    for radius,column in ((0.,0),(.1,1),(1.5,5)):
        yy=y[:,column];b,c,jb,jc,pb,pc=system.boundary_jet(radius,yy,p)
        jac=np.vstack((jb,jc));jp=np.r_[pb,pc];errors=[]
        for j in range(n):
            d=np.zeros(n);d[j]=step
            up=system.boundary_jet(radius,yy+d,p);down=system.boundary_jet(radius,yy-d,p)
            fd=(np.r_[up[0],up[1]]-np.r_[down[0],down[1]])/(2*step)
            errors.append(float(np.max(abs(fd-jac[:,j]))))
        up=system.boundary_jet(radius,yy,p+step);down=system.boundary_jet(radius,yy,p-step)
        errors.append(float(np.max(abs((np.r_[up[0],up[1]]-np.r_[down[0],down[1]])/(2*step)-jp))))
        target=system.controlled([radius],p[0]);Cr=float(target[5][0]);s=1/Cr;al=system.alpha;m=s+al*yy[M]
        assert s+al*np.sum(abs(yy[M:]))<0
        NN=16384;theta=(np.pi/2)*np.arange(NN)/NN;k=4*np.arange(1,M+1)[:,None]
        inverse=theta.copy()
        for _ in range(6):
            sn,cs=np.sin(k*inverse),np.cos(k*inverse)
            IV=(yy[M+1:,None]*sn/k).sum(axis=0);V=yy[M]+yy[M+1:]@cs
            inverse-=(inverse+al*IV/m-theta)/((s+al*V)/m)
        sn,cs=np.sin(k*inverse),np.cos(k*inverse)
        U=yy[:M]@sn;v=s+al*(yy[M]+yy[M+1:]@cs)
        bf=np.fft.fft(U/v)/NN;cf=np.fft.fft((1/v-Cr)/al)/NN
        direct=np.r_[-2*bf.imag[1:M+1],cf.real[0],2*cf.real[1:M+1]]
        boundary.append(dict(radius=radius,all_state_and_parameter_columns_tested=n+1,
            maximum_central_difference_error=max(errors),physical_direct_grid=NN,
            complete_retained_moment_difference=float(np.max(abs(direct-np.r_[b,c]))),
            mean_C_identity_error=float(abs(np.mean(1/v)-1/m)),
            mean_B_value=float(abs(np.mean(al*U/v)))))
    gates=dict(full_all_column_FFT_action=max(action_errors)<2e-12,
        complete_interior_state_and_parameter_derivatives=max(derivative_errors)<3e-7,
        true_mean_feedback_identity=mean_error<2e-13,
        exact_cubic_support=tails['roundoff_beyond_exact_cubic_support_l1']<2e-13,
        full_boundary_state_and_parameter_columns=max(x['maximum_central_difference_error'] for x in boundary)<3e-8,
        independent_physical_moments=max(x['complete_retained_moment_difference'] for x in boundary)<3e-11)
    report=dict(kind='executed_complete_small_moving_operator_audit',certified=False,complete=True,
        source_sha256=sha(__file__),system_sha256=sha(Path(__file__).with_name('fourfold_codazzi_moving_polynomial_system.py')),
        object_sha256=sha(args.object),q_vector_sha256=sha(args.q_vector),modes=M,angles=N,
        radii=r.tolist(),seed=20261113,alpha=.75,nu=float(p[0]),central_difference_step=step,
        all_columns_including_mean_and_parameter=True,
        full_action_max_absolute_error=max(action_errors),interior_derivative_max_error=max(derivative_errors),
        mean_feedback_max_error=mean_error,complete_interior_tail=tails,physical_boundary_checks=boundary,
        gates=gates,all_gates_pass=all(gates.values()),wall_seconds=time.monotonic()-tick,
        scope='Floating implementation evidence only; no complete BVP, infinite PDE or geometric certificate.')
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n');print(json.dumps(report,indent=2),flush=True)
    if not all(gates.values()):raise SystemExit(2)


if __name__=='__main__':main()
