#!/usr/bin/env python3
"""One short-interval linear mixed-boundary diagnostic, never a new BVP.

Fix projected meridional/tangential coordinates and normal modes 0..3 at
the left; free normal modes 4..M.  At the known right curve use a separated
fast real-Schur rowspace of the complete moving-frame finite Jacobian.
"""
import argparse,gzip,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import DOP853
from scipy.linalg import eigvals,solve,svdvals


def main(args):
    helper_path=args.topic/'notes/2026-11-17-parallel-geometry-frenet-schur.py'
    spec=importlib.util.spec_from_file_location('mixed_schur_helper',helper_path)
    h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
    data=json.loads(gzip.decompress(args.field.read_bytes()))
    if not data.get('ivp_reached_end'):raise ValueError('Need a successful local reference field')
    q=h.Frenet(data['M'],data['N']);reader=h.Frenet(q.M,args.read_angles)
    profile=h.profile_from(data)
    x=np.asarray(data['mesh']);ys=np.asarray(data['states']);dy=np.asarray(data['rhs']);ddy=np.asarray(data['d2'])
    fixed=2*q.M+5;free=q.M-3
    def frame(i):
        y=ys[i];F,d,e=q.jet(y);V,dV,_=q.jet(dy[i]);Acc,_,_=q.jet(ddy[i])
        cross=np.cross(V,d);area=np.linalg.norm(cross,axis=1);normal=cross/area[:,None]
        z=dict(d=d,V=V,dV=dV,Acc=Acc,normal=normal,area=area)
        T,Ts=h.moving_frame_map(q,z);a,ap,_=profile(float(x[i]));A=q.jacobian(y,ap/a)
        B=solve(T.T,(T@A+Ts).T).T
        return T,Ts,A,B
    T0,Ts0,A0,B0=frame(0);T1,Ts1,A1,B1=frame(-1)
    ev=eigvals(B1);re=np.sort(ev.real);lo,hi=float(re[-free-1]),float(re[-free])
    out=dict(scope=__doc__,source_sha256=h.sha(__file__),helper_sha256=h.sha(helper_path),
        reference_sha256=h.sha(args.field),M=q.M,N=q.N,start=float(x[0]),end=float(x[-1]),
        fixed_left_count=fixed,free_left_count=free,right_count=free,
        T0_condition=float(np.linalg.cond(T0)),T1_condition=float(np.linalg.cond(T1)),
        right_growth_gap=dict(lower=lo,upper=hi,gap=hi-lo))
    if hi-lo<=1e-8:
        out['status']='No separated real-part threshold at the required count'
        args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out));return
    schur,LB=h.selected_left(B1,lambda re:re>(lo+hi)/2,q.M,None)
    out['right_Schur']={k:v for k,v in schur.items() if k!='modal_energy'}
    if schur['dimension']!=free:raise ValueError('A real Schur block cannot be cut to force the count')
    L=LB@T1
    E=np.eye(q.n)[:,fixed:];U=solve(T0,E)
    out['left_fixed_constraint_residual']=float(np.max(abs((T0@U)[:fixed])))
    coefficients=[]
    for i,width in enumerate(np.diff(x)):
        c0=ys[i];c1=width*dy[i];c2=width*width*ddy[i]/2
        a=ys[i+1]-c0-c1-c2;b=width*dy[i+1]-c1-2*c2;c=width*width*ddy[i+1]-2*c2
        coefficients.append(np.array([c0,c1,c2,10*a-4*b+c/2,-15*a+7*b-c,6*a-3*b+c/2]))
    def reference(s):
        i=min(len(x)-2,max(0,int(np.searchsorted(x,s,side='right')-1)))
        width=x[i+1]-x[i];u=(s-x[i])/width;c=coefficients[i]
        return np.polynomial.polynomial.polyval(u,c),np.polynomial.polynomial.polyval(u,np.arange(1,6)[:,None]*c[1:])/width
    stats=dict(rhs_calls=0,reference_ODE_defect_max=0.)
    started=time.perf_counter()
    print(json.dumps(dict(event='mixed_linear_prepared',**out)),flush=True)
    def variation(s,flat):
        y,v=reference(s);a,ap,_=profile(float(s));k=ap/a
        A=q.jacobian(y,k)
        stats['reference_ODE_defect_max']=max(stats['reference_ODE_defect_max'],float(np.max(abs(v-q.rhs(y,k)))))
        stats['rhs_calls']+=1
        if stats['rhs_calls']%100==0:
            print(json.dumps(dict(event='variational_progress',s=float(s),seconds=time.perf_counter()-started,**stats)),flush=True)
        return (A@flat.reshape(q.n,free)).ravel()
    tau=float(x[-1]-x[0])
    solution=DOP853(variation,x[0],U.ravel(),x[-1],
        rtol=args.rtol,atol=args.atol,first_step=tau/256,max_step=tau/args.max_step_divisor)
    nodes=1;message=None
    while solution.status=='running':
        message=solution.step();nodes+=1
    out['variational_integration']=dict(success=solution.status=='finished',message=message,
        nfev=solution.nfev,nodes=nodes,rtol=args.rtol,atol=args.atol,max_step_divisor=args.max_step_divisor,
        seconds=time.perf_counter()-started,**stats)
    if solution.status!='finished':
        args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out));return
    response=solution.y.reshape(q.n,free)
    K=L@response
    singular=svdvals(K)
    tail=np.zeros(q.n);modes=np.arange(args.target_cutoff+1,q.M+1)
    tail[modes]=ys[-1,modes];tail[q.M+modes]=ys[-1,q.M+modes]
    tail[2*q.M+1+modes]=ys[-1,2*q.M+1+modes]
    target=-L@tail
    eta=solve(K,target);delta=U@eta
    predicted=response@eta
    out['linear_response']=dict(condition_2=float(singular[0]/singular[-1]),
        singular_max=float(singular[0]),singular_min=float(singular[-1]),
        target_max=float(np.max(abs(target))),target_norm=float(np.linalg.norm(target)),
        residual_norm=float(np.linalg.norm(K@eta-target)),
        fixed_left_residual=float(np.max(abs((T0@delta)[:fixed]))),
        free_coeff_max=float(np.max(abs(eta))),initial_coeff_max=float(np.max(abs(delta))),
        initial_delta_F_Fphi_Fphiphi_max=[float(np.max(np.linalg.norm(v,axis=1))) for v in reader.jet(delta)],
        predicted_right_delta_F_Fphi_Fphiphi_max=[float(np.max(np.linalg.norm(v,axis=1))) for v in reader.jet(predicted)],
        target_cutoff=args.target_cutoff,delta_initial_coefficients=delta.tolist())
    a,ap,app=profile(float(x[0]));k=ap/a;kp=app/a-k*k
    first=A0@delta
    eps=1e-24;yc=ys[0]+1j*eps*delta
    second=q.jvp(yc,k,q.rhs(yc,k),dk=kp).imag/eps
    out['initial_linear_radial_jet_changes']=dict(first=float(np.max(np.linalg.norm(reader.jet(first)[0],axis=1))),
        second=float(np.max(np.linalg.norm(reader.jet(second)[0],axis=1))))
    trial=ys[0]+delta
    try:
        velocity=q.rhs(trial,k);acc=q.jvp(trial,k,velocity,dk=kp)
        old_v=np.asarray(data['old_cut_jets']['first']);old_a=np.asarray(data['old_cut_jets']['second'])
        F,d,_=reader.jet(trial);V,_,_=reader.jet(velocity)
        core=np.asarray(data['original_core_coefficients'])
        rho=1+np.cos(reader.angle[:,None]*reader.freq[None,1:])@((1-reader.freq[1:]**2)*core)
        er=np.sum(V*V,axis=1)-1;gr=np.sum(d*d,axis=1)/(a*rho)**2-1;cr=np.sum(V*d,axis=1)/(a*rho)
        error=(abs(er+gr)+np.sqrt((er-gr)**2+4*cr*cr))/2
        local=q.local(trial,k)
        out['nonlinear_trial_initial_point']=dict(domain_H_min=float(local['H'].min()),
            relative_Gram_operator=float(error.max()),
            old_prefix_value_jump=float(np.max(np.linalg.norm(reader.jet(delta)[0],axis=1))),
            old_prefix_first_jump=float(np.max(np.linalg.norm(reader.jet(velocity-old_v)[0],axis=1))),
            old_prefix_second_jump=float(np.max(np.linalg.norm(reader.jet(acc-old_a)[0],axis=1))),
            first_linearization_remainder=float(np.max(abs(velocity-dy[0]-first))),
            second_linearization_remainder=float(np.max(abs(acc-ddy[0]-second))))
    except FloatingPointError as error:
        out['nonlinear_trial_initial_point']=dict(domain_error=str(error))
    displacement=out['linear_response']['initial_delta_F_Fphi_Fphiphi_max'][0]
    out['added_value_only_Hermite_bounds']={str(w):dict(first=15*displacement/(8*w),
        second=10*displacement/(np.sqrt(3)*w*w)) for w in [.0005,.001]}
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    printable={k:v for k,v in out.items() if k!='linear_response'}
    printable['linear_response']={k:v for k,v in out['linear_response'].items() if k!='delta_initial_coefficients'}
    print(json.dumps(printable),flush=True)
    print(json.dumps(dict(output=str(args.out),sha256=h.sha(args.out))),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--topic',type=Path,required=True);p.add_argument('--field',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--target-cutoff',type=int,default=224)
    p.add_argument('--read-angles',type=int,default=8192);p.add_argument('--rtol',type=float,default=1e-8)
    p.add_argument('--atol',type=float,default=1e-11)
    p.add_argument('--max-step-divisor',type=float,default=64)
    main(p.parse_args())
