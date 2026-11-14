#!/usr/bin/env python3
"""Finite full-body BVP with the complete regular boundary model, mean included.

At the waist impose B=0. At the true regular cut impose all nonmean R74
linear rows and the rotational mean C row. The waist mean/total turning
and every waist nonmean coefficient are outputs, never silently normalized.
"""
from __future__ import annotations
import argparse,inspect,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly
import scipy.integrate._bvp as bvp
from flint import ctx
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_codazzi_actual_cap_regular_BVP_probe import StableTwoEnded
from fourfold_codazzi_positive_cap_nonlinear_probe_v2 import diagnose
from fourfold_phase_codazzi_feasible_bvp_probe import guarded_newton
from fourfold_phase_codazzi_two_end_probe import load_candidate,save_npz_gz
from fourfold_phase_local_correction_probe import sha


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--cap-guess',type=Path,default=Path('notes/2026-11-13-Codazzi-positive-cap-nonlinear-m64-candidate.npz.gz'))
    ap.add_argument('--modes',type=int,default=24);ap.add_argument('--angles',type=int,default=384)
    ap.add_argument('--tol',type=float,default=1e-5);ap.add_argument('--max-nodes',type=int,default=3000)
    ap.add_argument('--newton-iterations',type=int,default=32)
    ap.add_argument('--C-floor',type=float,default=.02);ap.add_argument('--field-ceiling',type=float,default=30.)
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--candidate',type=Path,required=True)
    a=ap.parse_args();started=time.monotonic();ctx.prec=192;ctx.cap=6;m=a.modes;n=2*m+1
    if a.out.exists() or a.candidate.exists():raise FileExistsError('refusing to overwrite a finite full-boundary result')
    if a.angles<8*m or a.angles%4:raise ValueError('insufficient angular grid')
    geometry,definition=load_exact_object(a.object,512);body=RotationalBodyTarget(geometry);graft=RotationalGraftTarget(geometry,a.object)
    system=StableTwoEnded(geometry,m,a.angles,body,graft)
    saved=load_candidate(a.cap_guess);meta=json.loads(str(saved['metadata']));pm=int(meta['modes'])
    if meta['object_sha256']!=sha(a.object) or meta['coordinates']!='B,C' or meta['amplitude']!=1:
        raise ValueError('incompatible positive-cap candidate')
    if not np.all(np.isfinite(saved['piece_coefficients'])):raise ValueError('nonfinite cap warm start')
    cut=float(saved['radial_nodes'][0]);r=np.unique(np.r_[np.linspace(0.,cut,241),saved['radial_nodes']])
    guess=np.zeros((n,len(r)));inner=r<cut
    guess[:,inner]=np.column_stack([system.old_fields(float(x)) for x in r[inner]])
    values=PPoly(saved['piece_coefficients'],saved['radial_nodes'])(r[~inner]).T;common=min(m,pm)
    guess[:common,~inner]=values[:common];guess[m:m+common+1,~inner]=values[pm:pm+common+1]
    old0=system.old_fields(0.);a0=body.point(0.)['a']
    qstar=1/np.sqrt(1+(graft.a_endpoint/(4*graft.omega))**2);Cstar=graft.point(3.125)['Cref']
    def bc(left,right):return np.r_[left[:m],right[:m]+qstar*right[m+1:],right[m]-Cstar]
    def bc_jac(left,right):
        jl=np.zeros((n,n));jr=np.zeros((n,n));jl[np.arange(m),np.arange(m)]=1
        jr[np.arange(m,2*m),np.arange(m)]=1;jr[np.arange(m,2*m),np.arange(m+1,n)]=qstar;jr[-1,m]=1
        return jl,jr
    log=[];original=bvp.solve_newton
    bvp.solve_newton=guarded_newton(system,log,a.C_floor,a.field_ceiling,a.newton_iterations)
    try:
        result=solve_bvp(system.evaluate,bc,r,guess,fun_jac=system.jacobian,bc_jac=bc_jac,
            tol=a.tol,bc_tol=a.tol/100,max_nodes=a.max_nodes,verbose=1)
    finally:bvp.solve_newton=original
    d=diagnose(system,result);left,right=result.y[:,0],result.y[:,-1]
    metadata=dict(kind='floating_full_body_Codazzi_with_regular_mean_boundary_model',coordinates='B,C',
        modes=m,source_sha256=sha(__file__),object_sha256=sha(a.object),original_target_fixed=True,
        state_order='B sine k=1..M, C cosine k=0..M',physical_frequency_factor=4,
        waist_boundary='B=0; C mean and all nonmean coefficients are outputs.',
        outer_boundary='All true R74 regular LINEAR stable-center rows plus rotational mean C; nonlinear terms unpaid.')
    save_npz_gz(a.candidate,radial_nodes=result.x,piece_coefficients=result.sol.c,initial_state=left,metadata=np.array(json.dumps(metadata)))
    report=dict(**metadata,certified=False,finite_BVP_success=bool(result.success and d['valid']),
        solver_message=result.message,solver_status=int(result.status),guarded_Newton_history=log,diagnostics=d,
        initial_radial_nodes=len(r),radial_nodes=len(result.x),angular_grid=a.angles,diagnostic_angular_grid=2*a.angles,
        requested_interval=['0','25/8'],tol=a.tol,primitive_nodes=512,
        cap_guess_path=str(a.cap_guess),cap_guess_sha256=sha(a.cap_guess),
        waist_B_l1=float(np.sum(abs(left[:m]))),waist_mean_C=float(left[m]),waist_mean_closure_gap=float(left[m]+1/a0),
        waist_turn_number=float(-a0*left[m]),waist_total_turn=float(-2*np.pi*a0*left[m]),
        waist_C_coefficients=left[m:].tolist(),old_waist_C_coefficients=old0[m:].tolist(),
        waist_nonmean_change_l1=float(np.sum(abs(left[m+1:]-old0[m+1:]))),
        waist_nonmean_remaining_l1=float(np.sum(abs(left[m+1:]))),
        outer_regular_linear_residual_l1=float(np.sum(abs(right[:m]+qstar*right[m+1:]))),
        outer_mean_C_gap=float(right[m]-Cstar),outer_B_coefficients=right[:m].tolist(),outer_C_coefficients=right[m:].tolist(),
        exact_center_parameter=definition['delta_fraction'],origin_sha256=definition['origin_inputs']['sha256'],
        direction_sha256=definition['direction']['sha256'],candidate_path=str(a.candidate),candidate_sha256=sha(a.candidate),
        scipy_collocation_module_sha256=sha(inspect.getsourcefile(bvp)),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_actual_cap_regular_BVP_probe.py','fourfold_codazzi_positive_cap_nonlinear_probe_v2.py',
            'fourfold_phase_codazzi_feasible_bvp_probe.py','fourfold_phase_codazzi_two_end_probe.py',
            'fourfold_phase_codazzi_rotational_reference_probe.py','fourfold_codazzi_rotational_cap_jacobi_probe.py')},
        mean_retained=True,waist_closed_curve_certified=False,whole_radial_interval=False,whole_affine_parameter_interval=False,
        whole_real_angular_circle=False,regular_mean_height=None,regular_mean_flux=None,nonlinear_regular_tail=None,
        limitations=['Finite floating projection/collocation only, with node/quarter/mid/three-quarter residual diagnostics.',
            'The actual waist total turning is an output and is not normalized to one.',
            'All outer nonmean rows and the mean row are boundary-model equations; true nonlinear tail matching is still unpaid.',
            'No visible-amplitude condition is imposed; a near-rotational solution would not establish the requested flex.',
            'No mathematical singularity or nonexistence is inferred from the domain-preserving Newton stop flag.'],
        wall_seconds=time.monotonic()-started)
    a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(dict(success=report['finite_BVP_success'],diagnostics=d,waist_mean_gap=report['waist_mean_closure_gap'],
        waist_nonmean_l1=report['waist_nonmean_remaining_l1'],waist_low4=report['waist_C_coefficients'][1:5],
        wall_seconds=report['wall_seconds']),flush=True)


if __name__=='__main__':main()
