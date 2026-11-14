#!/usr/bin/env python3
"""Finite actual positive-cap nonlinear Dirichlet-to-curvature diagnostic.

At r=.239 prescribe the nonmean C coefficients of the actual stored waist
Cauchy endpoint. At the genuine outer cut 25/8 retain every nonmean regular
linear row and the rotational mean row. The inner B and C mean are outputs.
The outer R119 nonlinear response/labels/mean corrections remain unpaid.
This is a floating diagnostic with a genuine, well-labelled boundary model.
"""
from __future__ import annotations
import argparse,inspect,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp
import scipy.integrate._bvp as bvp
from flint import ctx
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_codazzi_actual_cap_regular_BVP_probe import StableTwoEnded,diagnose
from fourfold_phase_codazzi_feasible_bvp_probe import guarded_newton
from fourfold_phase_codazzi_two_end_probe import save_npz_gz
from fourfold_phase_local_correction_probe import sha


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--endpoint',type=Path,default=Path('notes/2026-11-13-codazzi-to-r0239-n1024-endpoint-floating.npz'))
    ap.add_argument('--linear-cap',type=Path,default=Path('notes/2026-11-13-Codazzi-rotational-cap-Jacobi-floating.json'))
    ap.add_argument('--modes',type=int,default=24);ap.add_argument('--angles',type=int,default=384)
    ap.add_argument('--tol',type=float,default=1e-5);ap.add_argument('--max-nodes',type=int,default=3000)
    ap.add_argument('--newton-iterations',type=int,default=18)
    ap.add_argument('--C-floor',type=float,default=.02);ap.add_argument('--field-ceiling',type=float,default=30.)
    ap.add_argument('--initial-step',type=float,default=.125);ap.add_argument('--minimum-step',type=float,default=1/1024)
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--candidate',type=Path,required=True)
    a=ap.parse_args();start=time.monotonic();ctx.prec=192;ctx.cap=6;m=a.modes;n=2*m+1
    if a.out.exists() or a.candidate.exists():raise FileExistsError('refusing to overwrite a cap diagnostic')
    if a.angles<8*m or a.angles%4:raise ValueError('insufficient angular grid')
    data=np.load(a.endpoint,allow_pickle=False);meta=json.loads(str(data['metadata']));left_r=float(data['r'])
    if meta['object_sha256']!=sha(a.object) or left_r!=.239:raise ValueError('unexpected actual endpoint')
    data_state=data['state'];coeff=np.fft.fft(data_state[:,:2],axis=0)/len(data_state)
    prescribed_C=2*coeff[1:m+1,1].real;actual_B=-2*coeff[1:m+1,0].imag;actual_C_mean=float(coeff[0,1].real)
    cap=json.loads(a.linear_cap.read_text())
    if cap['object_sha256']!=sha(a.object) or cap['endpoint_radius']!=left_r:raise ValueError('incompatible linear cap reference')
    qinner=np.ones(m);available=min(m,len(cap['entries']))
    qinner[:available]=[x['q'] for x in cap['entries'][:available]]
    geometry,definition=load_exact_object(a.object,512);body=RotationalBodyTarget(geometry);graft=RotationalGraftTarget(geometry,a.object)
    system=StableTwoEnded(geometry,m,a.angles,body,graft)
    def cref(r):
        r=np.asarray(r);out=np.empty(len(r));ii=np.flatnonzero(r<=3)
        for j in range(0,len(ii),32):out[ii[j:j+32]]=body.values(r[ii[j:j+32]])['Cref']
        for i in np.flatnonzero(r>3):out[i]=graft.point(float(r[i]))['Cref']
        return out
    r=np.unique(np.r_[np.linspace(left_r,.26,85),np.linspace(.26,1.,151),np.linspace(1.,3.,151),np.linspace(3.,3.125,17)])
    qstar=1/np.sqrt(1+(graft.a_endpoint/(4*graft.omega))**2);Cstar=graft.point(3.125)['Cref']
    def bc_jac(left,right):
        jl=np.zeros((n,n));jr=np.zeros((n,n))
        jl[np.arange(m),np.arange(m+1,n)]=1
        jr[np.arange(m,2*m),np.arange(m)]=1;jr[np.arange(m,2*m),np.arange(m+1,n)]=qstar
        jr[-1,m]=1;return jl,jr
    records=[];current=None;current_amplitude=0.;step=a.initial_step;failed_result=None
    original=bvp.solve_newton
    def attempt(amplitude,mesh,guess):
        def bc(left,right):return np.r_[left[m+1:]-amplitude*prescribed_C,
                                        right[:m]+qstar*right[m+1:],right[m]-Cstar]
        log=[];bvp.solve_newton=guarded_newton(system,log,a.C_floor,a.field_ceiling,a.newton_iterations)
        try:
            result=solve_bvp(system.evaluate,bc,mesh,guess,fun_jac=system.jacobian,bc_jac=bc_jac,
                tol=a.tol,bc_tol=a.tol/100,max_nodes=a.max_nodes,verbose=1)
        finally:bvp.solve_newton=original
        finite=bool(np.all(np.isfinite(result.sol.c)));B,C=system.fields(result.y)
        ok=bool(result.success and finite and np.max(C)<-a.C_floor)
        records.append(dict(amplitude=amplitude,success=ok,nodes=len(result.x),solver_status=int(result.status),
            message=result.message,finite_coefficients=finite,guarded_Newton_history=log,
            sampled_C_min=float(np.min(C)),sampled_C_max=float(np.max(C)),
            inner_C_mean=float(result.y[m,0]),inner_B_l1=float(np.sum(abs(result.y[:m,0]))),
            finite_collocation_rms_max=float(np.max(result.rms_residuals))))
        print(dict(amplitude=amplitude,success=ok,nodes=len(result.x),C_range=[float(C.min()),float(C.max())],
                   mean_inner=float(result.y[m,0]),wall=time.monotonic()-start),flush=True)
        return result,ok
    guess=np.zeros((n,len(r)));guess[m]=cref(r)
    current,ok=attempt(0.,r,guess)
    if ok:
        while current_amplitude<1:
            trial=min(1.,current_amplitude+step);mesh=current.x;guess=current.y.copy();reference=cref(mesh)
            if current_amplitude>0:
                scale=trial/current_amplitude;guess[:m]*=scale;guess[m+1:]*=scale
                guess[m]=reference+(guess[m]-reference)*scale*scale
            else:
                decay=np.exp(-system.frequency[:,None]*(mesh-left_r))
                guess[m+1:]=trial*prescribed_C[:,None]*decay
                guess[:m]=-qinner[:,None]*guess[m+1:]
            candidate,ok=attempt(trial,mesh,guess)
            if ok:
                current=candidate;current_amplitude=trial;step=min(.25,step*1.4)
            else:
                failed_result=candidate;step*=.5
                if step<a.minimum_step:break
    else:failed_result=current
    d=diagnose(system,current);state=current.y;inner,outer=state[:,0],state[:,-1]
    actual_B_mismatch=inner[:m]-current_amplitude*actual_B
    actual_C_mean_mismatch=inner[m]-(body.point(left_r)['Cref']+current_amplitude*(actual_C_mean-body.point(left_r)['Cref']))
    f=outer[m+1:]/((1/(4*graft.omega))*np.sqrt(1+(graft.a_endpoint/(4*graft.omega))**2)*(system.frequency**2-system.frequency))
    metadata=dict(kind='floating_actual_positive_cap_nonlinear_Dirichlet_probe',coordinates='B,C',modes=m,
        physical_frequency_factor=4,state_order='B sine k=1..M, C cosine k=0..M',
        source_sha256=sha(__file__),object_sha256=sha(a.object),endpoint_sha256=sha(a.endpoint),
        amplitude=current_amplitude,original_target_fixed=True,actual_natural_graft_used=True,
        inner_boundary='Prescribed nonmean C only; inner B and mean C are outputs.',
        outer_boundary='Every nonmean true R74 regular LINEAR stable-center row, plus rotational C mean; nonlinear tail terms unpaid.')
    save_npz_gz(a.candidate,radial_nodes=current.x,piece_coefficients=current.sol.c,initial_state=inner,
        prescribed_inner_C=prescribed_C,metadata=np.array(json.dumps(metadata)))
    failed_path=None
    if failed_result is not None:
        failed_path=a.candidate.with_name(a.candidate.name.replace('.npz.gz','-last-failed.npz.gz'))
        save_npz_gz(failed_path,radial_nodes=failed_result.x,piece_coefficients=failed_result.sol.c,
            metadata=np.array(json.dumps(dict(metadata,kind='failed_floating_actual_positive_cap_attempt',
                                             amplitude=records[-1]['amplitude']))))
    doc=dict(**metadata,certified=False,reached_full_amplitude=bool(current_amplitude==1),
        finite_BVP_success=bool(current.success and d['valid']),diagnostics=d,attempts=records,
        requested_interval=[left_r,3.125],angular_grid=a.angles,diagnostic_angular_grid=2*a.angles,
        primitive_nodes=512,tol=a.tol,max_nodes=a.max_nodes,
        input_actual_C_mean=actual_C_mean,input_actual_B_coefficients=actual_B.tolist(),
        input_actual_C_nonmean_coefficients=prescribed_C.tolist(),
        inner_B_coefficients=inner[:m].tolist(),inner_C_coefficients=inner[m:].tolist(),
        inner_B_minus_scaled_actual_coefficients=actual_B_mismatch.tolist(),
        inner_B_minus_scaled_actual_l1=float(np.sum(abs(actual_B_mismatch))),
        inner_C_mean_minus_scaled_actual=float(actual_C_mean_mismatch),
        outer_B_coefficients=outer[:m].tolist(),outer_C_coefficients=outer[m:].tolist(),
        outer_regular_linear_residual_l1=float(np.sum(abs(outer[:m]+qstar*outer[m+1:]))),
        outer_C_mean_minus_reference=float(outer[m]-Cstar),
        outer_linear_height_estimate=f.tolist(),outer_linear_height_homogeneous_A2_norm=float(np.sum(system.frequency**2*abs(f))),
        candidate_path=str(a.candidate),candidate_sha256=sha(a.candidate),
        failed_candidate_path=str(failed_path) if failed_path else None,
        failed_candidate_sha256=sha(failed_path) if failed_path else None,
        exact_center_parameter=definition['delta_fraction'],origin_sha256=definition['origin_inputs']['sha256'],
        direction_sha256=definition['direction']['sha256'],linear_cap_input_sha256=sha(a.linear_cap),
        true_R74_tail_fee='<=2^42 exp(-2m omega_lower*(2^24-25/8)) for non-fourth modes; not propagated here.',
        regular_mean_height=None,regular_mean_flux=None,nonlinear_tail_residual=None,
        whole_affine_parameter_interval=False,whole_real_angular_circle=False,whole_radial_domain=False,
        complete_mean_retained=True,scipy_collocation_module_sha256=sha(inspect.getsourcefile(bvp)),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_actual_cap_regular_BVP_probe.py','fourfold_phase_codazzi_two_end_probe.py',
            'fourfold_phase_codazzi_feasible_bvp_probe.py','fourfold_phase_codazzi_rotational_reference_probe.py',
            'fourfold_codazzi_rotational_cap_jacobi_probe.py','fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py')},
        limitations=['Finite Fourier, floating collocation and finite sampled residuals only.',
            'The complete true outer nonlinear Dirichlet/label/bump/mean response is not solved by the displayed boundary approximation.',
            'A zero outer linear height estimate does not justify dropping the true tail or the independent regular mean position.',
            'Inner B and C mean mismatch against the Cauchy endpoint is diagnostic, not an exact obstruction or a global solution.',
            'All unrepresented angular modes, rounding errors and whole-parameter errors remain unpaid.'],
        wall_seconds=time.monotonic()-start)
    a.out.write_text(json.dumps(doc,indent=2,allow_nan=False)+'\n')
    print(dict(amplitude=current_amplitude,finite_BVP_success=doc['finite_BVP_success'],diagnostics=d,
        inner_B_mismatch=doc['inner_B_minus_scaled_actual_l1'],inner_mean_mismatch=doc['inner_C_mean_minus_scaled_actual'],
        outer_height_A2=doc['outer_linear_height_homogeneous_A2_norm'],wall_seconds=doc['wall_seconds']),flush=True)


if __name__=='__main__':main()
