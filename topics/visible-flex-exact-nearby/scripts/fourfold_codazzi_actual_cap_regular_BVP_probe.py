#!/usr/bin/env python3
"""Finite nonlinear body/graft BVP using the genuine regular linear trace.

The whole scalar body and actual natural graft are used to r=25/8.
At that cut the stable-center R74 Codazzi Jacobi condition B_m+q*C_m=0
is imposed for the requested high channels. Its true-tail fee and nonlinear
trace remainder remain explicit unpaid outputs. This is diagnostic only.
"""
from __future__ import annotations
import argparse,inspect,json,time
from pathlib import Path
import numpy as np
import scipy
import scipy.integrate._bvp as bvp
from scipy.integrate import solve_bvp
from flint import ctx
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_two_end_probe import TwoEnded,save_npz_gz
from fourfold_phase_codazzi_feasible_bvp_probe import guarded_newton
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_phase_local_correction_probe import sha


class StableTwoEnded(TwoEnded):
    def __init__(self,geometry,modes,angles,body,graft):
        super().__init__(geometry,modes,angles);self.body=body;self.graft=graft

    def target(self,r):
        r=np.asarray(r);key=r.tobytes()
        if key not in self.cache:
            if len(self.cache)>=5:self.cache.pop(next(iter(self.cache)))
            out=np.zeros((3,len(r)));isbody=r<=3
            ind=np.flatnonzero(isbody)
            for start in range(0,len(ind),32):
                ii=ind[start:start+32];t=self.body.values(r[ii]);out[:,ii]=np.array([t['gamma'],t['beta'],t['K']])
            for i in np.flatnonzero(~isbody):
                t=self.graft.point(float(r[i]));out[:,i]=[t['gamma'],t['beta'],t['K']]
            self.cache[key]=tuple(out)
        return self.cache[key]

    def old_fields(self,r):
        if r<=3:return super().old_fields(r)
        out=np.zeros(2*self.modes+1);out[self.modes]=self.graft.point(r)['Cref'];return out


def diagnose(system,result):
    if not np.all(np.isfinite(result.sol.c)):
        return dict(valid=False,reason='nonfinite collocation polynomial; no residual bound exists')
    fine=StableTwoEnded(system.geometry,system.modes,2*system.angular_grid,system.body,system.graft)
    m=system.modes;points=np.unique(np.r_[result.x,(result.x[:-1]+result.x[1:])/2])
    out=dict(finite_PDE_residual=0.,full_sampled_B_residual=0.,full_sampled_C_residual=0.,
        A_projection_defect=0.,C_min=np.inf,C_max=-np.inf,C_abs_min=np.inf)
    for start in range(0,len(points),32):
        r=points[start:start+32];y=result.sol(r);yr=result.sol(r,1);gamma,beta,K=fine.target(r)
        B,C=fine.fields(y)
        if np.any(C==0) or not all(np.all(np.isfinite(x)) for x in (y,yr,B,C)):
            return dict(valid=False,reason='nonfinite or zero C diagnostic sample; no residual bound exists')
        A=(K+B*B)/C;ac=fine.proj@A
        Bt=fine.cos[1:].T@(fine.frequency[:,None]*y[:m]);Ct=-fine.sin.T@(fine.frequency[:,None]*y[m+1:])
        At=2*B*Bt/C-(K+B*B)*Ct/(C*C)
        RB=fine.sin.T@yr[:m]-gamma*At+2*beta*B
        RC=fine.cos.T@yr[m:]-gamma*Bt-beta*(A-C)
        finite=yr-system.evaluate(r,y)
        values=dict(finite_PDE_residual=max(float(np.max(abs(system.sin.T@finite[:m]))),float(np.max(abs(system.cos.T@finite[m:])))),
            full_sampled_B_residual=float(np.max(abs(RB))),full_sampled_C_residual=float(np.max(abs(RC))),
            A_projection_defect=float(np.max(abs(A-fine.cos.T@ac))))
        if not all(np.isfinite(v) for v in values.values()):
            return dict(valid=False,reason='nonfinite rational residual; no residual bound exists')
        for name,value in values.items():out[name]=max(out[name],value)
        out['C_min']=min(out['C_min'],float(np.min(C)));out['C_max']=max(out['C_max'],float(np.max(C)))
        out['C_abs_min']=min(out['C_abs_min'],float(np.min(abs(C))))
    out['valid']=bool(out['C_max']<0 and out['C_abs_min']>0);return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--modes',type=int,default=24);p.add_argument('--angles',type=int,default=384)
    p.add_argument('--waist-low',type=int,default=4);p.add_argument('--tol',type=float,default=1e-5)
    p.add_argument('--max-nodes',type=int,default=3000);p.add_argument('--newton-iterations',type=int,default=16)
    p.add_argument('--C-floor',type=float,default=.02);p.add_argument('--field-ceiling',type=float,default=30.)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--candidate',type=Path,required=True)
    a=p.parse_args();ctx.prec=192;ctx.cap=6;started=time.monotonic();m,L=a.modes,a.waist_low;n=2*m+1
    if a.out.exists() or a.candidate.exists():raise FileExistsError('refusing to overwrite a candidate')
    if not 0<=L<m or a.angles<8*m or a.angles%4:raise ValueError('invalid angular/retained dimensions')
    geometry,definition=load_exact_object(a.object,512);body=RotationalBodyTarget(geometry);graft=RotationalGraftTarget(geometry,a.object)
    system=StableTwoEnded(geometry,m,a.angles,body,graft)
    r=np.unique(np.r_[np.linspace(0,.25,251),np.linspace(.25,1.,151),np.linspace(1.,3.,101),np.linspace(3.,3.125,17)])
    guess=np.column_stack([system.old_fields(float(x)) for x in r]);old0=system.old_fields(0.)
    a0=body.point(0.)['a'];endref=graft.point(3.125)
    wstar=graft.a_endpoint/(4*graft.omega);qstar=1/np.sqrt(1+wstar*wstar)
    def bc(left,right):return np.r_[left[:m],left[m]+1/a0,left[m+1:m+L+1]-old0[m+1:m+L+1],
        right[L:m]+qstar*right[m+L+1:]]
    def bc_jac(left,right):
        jl=np.zeros((n,n));jr=np.zeros((n,n));split=m+L+1
        jl[np.arange(split),np.arange(split)]=1
        rr=np.arange(split,n);jr[rr,np.arange(L,m)]=1;jr[rr,np.arange(m+L+1,n)]=qstar
        return jl,jr
    history=[];original=bvp.solve_newton
    bvp.solve_newton=guarded_newton(system,history,a.C_floor,a.field_ceiling,a.newton_iterations)
    try:
        result=solve_bvp(system.evaluate,bc,r,guess,fun_jac=system.jacobian,bc_jac=bc_jac,
            tol=a.tol,bc_tol=a.tol/100,max_nodes=a.max_nodes,verbose=1)
    finally:bvp.solve_newton=original
    d=diagnose(system,result);left,right=result.y[:,0],result.y[:,-1]
    outer_residual=right[:m]+qstar*right[m+1:]
    metadata=dict(kind='floating_actual_body_graft_regular_linear_high_Codazzi_BVP',modes=m,coordinates='B,C',
        source_sha256=sha(__file__),object_sha256=sha(a.object),physical_frequency_factor=4,
        state_order='B sine k=1..M, C cosine k=0..M',original_target_fixed=True,initial_waist_curve_changed=True,
        fixed_waist_C_modes=list(range(L+1)),matched_regular_linear_modes=list(range(L+1,m+1)),
        unmatched_regular_linear_modes=list(range(1,L+1)),actual_natural_graft_used=True,
        boundary_identity='At actual r=25/8 use the stable-center representative of the true R74 Codazzi Jacobi line; actual tail fee and nonlinear regular response remain unpaid.')
    save_npz_gz(a.candidate,radial_nodes=result.x,piece_coefficients=result.sol.c,initial_state=left,
        right_boundary_C_nonmean=right[m+1:],metadata=np.array(json.dumps(metadata)))
    f_est=right[m+1:]/((1/(4*graft.omega))*np.sqrt(1+wstar*wstar)*(system.frequency**2-system.frequency))
    doc=dict(**metadata,certified=False,success=bool(result.success and d['valid']),solver_message=result.message,
        solver_status=int(result.status),guarded_Newton_history=history,diagnostics=d,
        finite_coefficients=bool(np.all(np.isfinite(result.sol.c))),radial_nodes=len(result.x),initial_radial_nodes=len(r),
        requested_interval=['0','25/8'],angular_grid=a.angles,diagnostic_angular_grid=2*a.angles,tol=a.tol,max_nodes=a.max_nodes,
        C_search_floor=a.C_floor,field_search_ceiling=a.field_ceiling,initial_B_l1=float(np.sum(abs(left[:m]))),
        initial_mean_C=float(left[m]),initial_mean_gap=float(left[m]+1/a0),initial_turn_number=float(-a0*left[m]),
        fixed_low_waist_C_difference_l1=float(np.sum(abs(left[m+1:m+L+1]-old0[m+1:m+L+1]))),
        initial_nonmean_C_difference_from_old_l1=float(np.sum(abs(left[m+1:]-old0[m+1:]))),
        initial_C_coefficients=left[m:].tolist(),old_initial_C_coefficients=old0[m:].tolist(),
        regular_linear_residual_coefficients=outer_residual.tolist(),
        matched_regular_linear_residual_l1=float(np.sum(abs(outer_residual[L:]))),
        unmatched_low_regular_linear_residual_l1=float(np.sum(abs(outer_residual[:L]))),
        outer_B_coefficients=right[:m].tolist(),outer_C_coefficients=right[m:].tolist(),
        outer_C_mean_minus_rotational_reference=float(right[m]-endref['Cref']),
        outer_linear_height_Dirichlet_estimate=f_est.tolist(),
        outer_linear_height_homogeneous_A2_norm=float(np.sum(system.frequency**2*abs(f_est))),
        regular_mean_height=None,regular_mean_flux=None,nonlinear_tail_residual=None,
        true_R74_linear_tail_fee='m=4 exactly zero; remaining m: <=2^42 exp(-2m omega_lower*(2^24-25/8)), unpropagated in this floating solve',
        nonlinear_tail_contract='R119 complete mean/Dirichlet/bump/label equations still must be solved; the displayed linear height estimate is not their nonlinear solution.',
        whole_parameter_interval=False,whole_real_angular_circle=False,whole_radial_domain=False,
        candidate_path=str(a.candidate),candidate_sha256=sha(a.candidate),
        exact_center_parameter=definition['delta_fraction'],origin_sha256=definition['origin_inputs']['sha256'],
        direction_sha256=definition['direction']['sha256'],scipy_version=scipy.__version__,
        scipy_collocation_module_sha256=sha(inspect.getsourcefile(bvp)),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_codazzi_two_end_probe.py','fourfold_phase_codazzi_feasible_bvp_probe.py',
            'fourfold_phase_codazzi_rotational_reference_probe.py','fourfold_codazzi_rotational_cap_jacobi_probe.py',
            'fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py')},
        wall_seconds=time.monotonic()-started,
        limitations=['Finite Fourier and floating radial collocation, with no complete residual/rounding/parameter certificate.',
            'The imposed outer rows are the genuine regular LINEAR trace representative at 25/8, not the nonlinear cap DN.',
            'The true exponentially small non-fourth-mode fee and every nonlinear regular-tail term remain explicit unpaid items.',
            'All omitted low regular rows and both mean position/flux slots remain unmatched outputs.',
            'The Newton stop flag can denote no admissible decreasing step; it is not a nonexistence or exact singularity claim.'])
    a.out.write_text(json.dumps(doc,indent=2,allow_nan=False)+'\n')
    print(dict(success=doc['success'],diagnostics=d,low_regular=doc['unmatched_low_regular_linear_residual_l1'],
        mean_C=doc['outer_C_mean_minus_rotational_reference'],outer_A2=doc['outer_linear_height_homogeneous_A2_norm'],
        wall_seconds=doc['wall_seconds']),flush=True)


if __name__=='__main__':main()
