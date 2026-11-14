#!/usr/bin/env python3
"""Finite Codazzi BVP continuation from the rotational solution.

The positive nonmean-C boundary is scaled from zero to its original chosen
value. This remains an artificial finite boundary condition, not a cap DN.
The metric stays fixed; the waist curve is allowed to change.
"""
from __future__ import annotations
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_local_correction_probe import sha,scalar_target
from fourfold_phase_codazzi_two_end_probe import TwoEnded,save_npz_gz,load_candidate


class ChunkedTwoEnded(TwoEnded):
    def target(self,r):
        r=np.asarray(r);key=r.tobytes()
        if key not in self.cache:
            if len(self.cache)>=5:self.cache.pop(next(iter(self.cache)))
            pieces=[]
            for j in range(0,len(r),128):
                t=self.geometry.radial_target_metric(r[j:j+128])
                pieces.append(np.array([np.sqrt(t['E'])/t['a'],t['a_x']/t['a'],t['K']]))
            values=np.concatenate(pieces,axis=1)
            self.cache[key]=tuple(values)
        return self.cache[key]


def diagnostics(system,solution):
    m=system.modes;points=np.unique(np.concatenate([solution.x,(solution.x[:-1]+solution.x[1:])/2]))
    fine=ChunkedTwoEnded(system.geometry,m,2*system.angular_grid)
    maxima=dict(finite_PDE_residual=0.,A_projection_defect=0.,A_theta_projection_defect=0.,
        full_sampled_B_residual=0.,full_sampled_C_residual=0.,C_abs_min=np.inf,C_min=np.inf,C_max=-np.inf)
    for start in range(0,len(points),128):
        r=points[start:start+128];values=solution.sol(r);radial=solution.sol(r,1)
        gamma,beta,K=fine.target(r);B,C=fine.fields(values)
        A=(K[None,:]+B*B)/C;ac=fine.proj@A;projection=fine.cos.T@ac
        diff=A-projection
        Bt=fine.cos[1:].T@(fine.frequency[:,None]*values[:m])
        Ct=-fine.sin.T@(fine.frequency[:,None]*values[m+1:])
        # Exact rational chain rule at the samples, not a truncated-A derivative.
        At=2*B*Bt/C-(K[None,:]+B*B)*Ct/(C*C)
        projection_t=-fine.sin.T@(fine.frequency[:,None]*ac[1:])
        dt=At-projection_t
        Br=fine.sin.T@radial[:m];Cr=fine.cos.T@radial[m:]
        RB=Br-gamma*At+2*beta*B;RC=Cr-gamma*Bt-beta*(A-C)
        finite=radial-system.evaluate(r,values)
        frB=system.sin.T@finite[:m];frC=system.cos.T@finite[m:]
        maxima['finite_PDE_residual']=max(maxima['finite_PDE_residual'],float(np.max(abs(frB))),float(np.max(abs(frC))))
        for key,value in [('A_projection_defect',diff),('A_theta_projection_defect',dt),
                          ('full_sampled_B_residual',RB),('full_sampled_C_residual',RC)]:
            maxima[key]=max(maxima[key],float(np.max(abs(value))))
        maxima['C_abs_min']=min(maxima['C_abs_min'],float(np.min(abs(C))))
        maxima['C_min']=min(maxima['C_min'],float(np.min(C)))
        maxima['C_max']=max(maxima['C_max'],float(np.max(C)))
    return maxima


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--modes',type=int,default=12);p.add_argument('--angles',type=int,default=256)
    p.add_argument('--right',type=float,default=.25);p.add_argument('--radial-nodes',type=int,default=251)
    p.add_argument('--tol',type=float,default=1e-5);p.add_argument('--max-nodes',type=int,default=3000)
    p.add_argument('--first-step',type=float,default=.1);p.add_argument('--min-step',type=float,default=1/512)
    p.add_argument('--maximum-attempts',type=int,default=25)
    p.add_argument('--guess',type=Path);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--candidate',type=Path,required=True);p.add_argument('--failed-candidate',type=Path,required=True)
    args=p.parse_args();start=time.monotonic()
    if args.angles<8*args.modes or args.angles%4:raise ValueError('insufficient angular grid')
    geometry,definition=load_exact_object(args.object,512)
    system=ChunkedTwoEnded(geometry,args.modes,args.angles);m=args.modes;n=2*m+1
    t0=scalar_target(geometry,0.);a0=t0['a'];right_old=system.old_fields(args.right)[m+1:]
    r=np.linspace(0.,args.right,args.radial_nodes);guess=np.zeros((n,len(r)))
    for j in range(0,len(r),128):
        t=geometry.radial_target_metric(r[j:j+128]);speed=t['a_x']/np.sqrt(t['E'])
        if np.max(abs(speed))>=1:raise ValueError('rotational reference is not a real immersion')
        guess[m,j:j+128]=-np.sqrt(1-speed*speed)/t['a']
    amplitude=0.;step=args.first_step;solution=None;last_failed=None;last_failed_amplitude=None;attempts=[]
    if args.guess:
        saved=load_candidate(args.guess);meta=json.loads(str(saved['metadata']))
        if meta['object_sha256']!=sha(args.object):raise ValueError('different metric target in guess')
        pm=int(meta['modes']);old=PPoly(saved['piece_coefficients'],saved['radial_nodes'])(r).T
        count=min(m,pm);guess[:count]=old[:count];guess[m:m+count+1]=old[pm:pm+count+1]
        amplitude=float(meta.get('boundary_amplitude',1.))
    def bc_jac(left,right):
        jl=np.zeros((n,n));jr=np.zeros((n,n))
        jl[np.arange(m+1),np.arange(m+1)]=1
        jr[np.arange(m+1,n),np.arange(m+1,n)]=1
        return jl,jr
    wanted=amplitude
    for attempt in range(args.maximum_attempts):
        def bc(left,right):return np.concatenate([left[:m],[left[m]+1/a0],right[m+1:]-wanted*right_old])
        print(dict(attempt=attempt,boundary_amplitude=wanted,previous_amplitude=amplitude,step=step),flush=True)
        result=solve_bvp(system.evaluate,bc,r,guess,fun_jac=system.jacobian,bc_jac=bc_jac,
            tol=args.tol,bc_tol=args.tol/100,max_nodes=args.max_nodes,verbose=1)
        B,C=system.fields(result.y);ok=bool(result.success and np.max(C)<-.02)
        row=dict(attempt=attempt,boundary_amplitude=wanted,success=ok,solver_success=bool(result.success),
            solver_status=int(result.status),message=result.message,radial_nodes=len(result.x),iterations=int(result.niter),
            max_collocation_rms_residual=float(np.max(result.rms_residuals)),
            boundary_residual=float(np.max(abs(bc(result.y[:,0],result.y[:,-1])))),
            sampled_C_range=[float(np.min(C)),float(np.max(C))],elapsed=time.monotonic()-start)
        attempts.append(row);print(row,flush=True)
        if ok:
            solution=result;amplitude=wanted;r=result.x;guess=result.y
            if amplitude>=1:break
            step=min(step*1.35,.2);wanted=min(1.,amplitude+step)
        else:
            last_failed=result;last_failed_amplitude=wanted
            if solution is None:break
            step*=.5
            if step<args.min_step:break
            wanted=min(1.,amplitude+step);r=solution.x;guess=solution.y
    if solution is None:
        final=result;final_amplitude=wanted
    else:final=solution;final_amplitude=amplitude
    metadata=dict(kind='floating_homotopy_two_ended_Codazzi_candidate',object_sha256=sha(args.object),
        source_sha256=sha(__file__),modes=m,physical_frequency_factor=4,boundary_amplitude=final_amplitude,
        state_order='B sine k=1..M, C cosine k=0..M',original_target_fixed=True,initial_waist_curve_changed=True,
        right_boundary='scaled old actual nonmean angular normal curvature only; NOT cap DN')
    save_npz_gz(args.candidate,radial_nodes=final.x,piece_coefficients=final.sol.c,
        initial_state=final.y[:,0],right_boundary_C_nonmean=final_amplitude*right_old,
        metadata=np.array(json.dumps(metadata)))
    failed_info=None
    if last_failed is not None:
        failed_metadata=dict(metadata,boundary_amplitude=last_failed_amplitude,successful=False)
        save_npz_gz(args.failed_candidate,radial_nodes=last_failed.x,piece_coefficients=last_failed.sol.c,
            initial_state=last_failed.y[:,0],right_boundary_C_nonmean=last_failed_amplitude*right_old,
            metadata=np.array(json.dumps(failed_metadata)))
        failed_info=dict(path=str(args.failed_candidate),sha256=sha(args.failed_candidate))
    diagnostic=diagnostics(system,final)
    old_initial=system.old_fields(0.)
    doc=dict(**metadata,certified=False,success=bool(solution is not None and final_amplitude>=1),
        reached_boundary_amplitude=final_amplitude,requested_boundary_amplitude=1.,attempts=attempts,
        primitive_nodes=512,angular_grid=args.angles,diagnostic_angular_grid=2*args.angles,
        exact_center_parameter=definition['delta_fraction'],origin_sha256=definition['origin_inputs']['sha256'],
        direction_sha256=definition['direction']['sha256'],right=args.right,tol=args.tol,max_nodes=args.max_nodes,
        initial_radial_nodes=args.radial_nodes,initial_step=args.first_step,minimum_step=args.min_step,
        maximum_attempts=args.maximum_attempts,guess_path=str(args.guess) if args.guess else None,
        guess_sha256=sha(args.guess) if args.guess else None,
        candidate_path=str(args.candidate),candidate_sha256=sha(args.candidate),last_failed_candidate=failed_info,
        diagnostics=diagnostic,initial_C_coefficients=final.y[m:,0].tolist(),
        old_initial_C_coefficients=old_initial[m:].tolist(),
        initial_C_coefficient_difference_l1=float(np.sum(abs(final.y[m:,0]-old_initial[m:]))),
        complete_mean_retained=True,whole_parameter_interval=False,whole_radial_domain=False,whole_real_angular_circle=False,
        dependency_sha256={s:sha(Path(__file__).with_name(s)) for s in
            ('fourfold_phase_codazzi_two_end_probe.py','fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py',
             'fourfold_phase_core_low_block.py','fourfold_phase_local_correction_probe.py')},
        rhs_calls=system.calls,jac_calls=system.jac_calls,wall_seconds=time.monotonic()-start,
        limitations=['Finite Fourier and floating collocation with an artificial nonmean-C outer boundary only.',
            'This changes the initial waist curve and is not the frozen R127 exact branch.',
            'No full tail/roundoff/continuous residual validation, true cap DN, regular-port matching or closed surface.',
            'The retained mean is constrained at the waist by exact total tangent turning; it is not deleted.'])
    args.out.write_text(json.dumps(doc,indent=2)+'\n')
    print(dict(success=doc['success'],amplitude=final_amplitude,diagnostics=diagnostic,
        initial_curve_difference=doc['initial_C_coefficient_difference_l1'],wall_seconds=doc['wall_seconds']),flush=True)


if __name__=='__main__':main()
