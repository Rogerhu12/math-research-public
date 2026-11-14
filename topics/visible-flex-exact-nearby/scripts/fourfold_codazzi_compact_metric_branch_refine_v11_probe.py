#!/usr/bin/env python3
"""Refine the compact-metric branch with fast Fourier multiplication and chunked approximate Newton matrices and lossless cubic shards.

The normalized mean and every retained mode are present.  The opposite mean
boundary, true nonlinear regular tail, and continuous full-spectrum PDE
validation remain explicit outputs.  This is a floating diagnostic.
"""
from __future__ import annotations
import argparse,inspect,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np
import scipy
import scipy.integrate._bvp as bvp
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly
from flint import ctx
from fourfold_codazzi_compact_metric_branch_probe import CompactNormalized,diagnostic,jacobian_audit
from fourfold_codazzi_guarded_Newton_krylov_v3 import guarded_parameter_newton_krylov_v3
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_codazzi_candidate_shards import load_candidate,save_candidate
from fourfold_codazzi_matrix_free_fft_collocation_v3 import make_prepare_sys
from fourfold_phase_local_correction_probe import sha

from fourfold_codazzi_compact_metric_fast_jacobian import FastCompactNormalized

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--guess',type=Path,required=True);ap.add_argument('--modes',type=int,required=True)
    ap.add_argument('--angles',type=int,required=True);ap.add_argument('--amplitude',type=float)
    ap.add_argument('--mean-boundary',choices=['waist','outer'],default='outer')
    ap.add_argument('--mesh-stride',type=int,default=2);ap.add_argument('--tol',type=float,default=2e-6)
    ap.add_argument('--max-nodes',type=int,default=3500);ap.add_argument('--newton-iterations',type=int,default=24)
    ap.add_argument('--jac-band',type=int,default=4);ap.add_argument('--jac-drop',type=float,default=1e-13)
    ap.add_argument('--jac-chunk',type=int,default=8)
    ap.add_argument('--max-nu',type=float,default=.2);ap.add_argument('--C-floor',type=float,default=.02)
    ap.add_argument('--field-ceiling',type=float,default=30.)
    ap.add_argument('--checkpoint-dir',type=Path,default=Path('/workspace/scratch/ac0d699811ad/codazzi_newton_checkpoints'))
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--candidate',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic();ctx.prec=192;ctx.cap=6
    if args.out.exists() or args.candidate.exists():raise FileExistsError('refusing to overwrite a refinement or real failure')
    if args.angles<8*args.modes or args.mesh_stride<1:raise ValueError('invalid finite resolution')
    if args.candidate.suffix!='.json':raise ValueError('use a .json index for the lossless complete polynomial shards')
    if args.guess.suffix=='.npz':
        with np.load(args.guess,allow_pickle=False) as z:saved={k:z[k].copy() for k in z.files}
        if 'state' not in saved or 'radial_derivative' not in saved:raise ValueError('not a complete accepted Newton checkpoint')
        saved['piece_coefficients']=bvp.create_spline(saved['state'],saved['radial_derivative'],saved['radial_nodes'],np.diff(saved['radial_nodes'])).c
        saved['initial_state']=saved['state'][:,0]
    else:saved=load_candidate(args.guess)
    meta=json.loads(str(saved['metadata']));pm=int(meta['modes'])
    if meta['object_sha256']!=sha(args.object) or meta['coordinates']!='B=alpha*b; C=Cref_nu+alpha*c':
        raise ValueError('incompatible normalized candidate identity')
    if not np.all(np.isfinite(saved['piece_coefficients'])):raise ValueError('nonfinite warm start')
    alpha=float(meta['amplitude']) if args.amplitude is None else args.amplitude
    if alpha<0:raise ValueError('negative amplitude is not part of this diagnostic')
    geometry,definition=load_exact_object(args.object,512);body=RotationalBodyTarget(geometry);graft=RotationalGraftTarget(geometry,args.object)
    system=FastCompactNormalized(geometry,args.modes,args.angles,body,graft);m=args.modes;n=2*m+1
    audit=jacobian_audit(system);system.alpha=alpha
    r=np.unique(np.r_[saved['radial_nodes'][::args.mesh_stride],saved['radial_nodes'][-1]])
    values=PPoly(saved['piece_coefficients'],saved['radial_nodes'])(r).T;guess=np.zeros((n,len(r)));common=min(m,pm)
    guess[:common]=values[:common];guess[m:m+common+1]=values[pm:pm+common+1];nu=np.array([float(meta['nu'])])
    qstar=1/np.sqrt(1+(graft.a_endpoint/(4*graft.omega))**2)
    def bc(left,right,p):
        mean=left[m] if args.mean_boundary=='waist' else right[m]
        return np.r_[left[:m],mean,left[m+1]+1,right[:m]+qstar*right[m+1:]]
    def bc_jac(left,right,p):
        jl=np.zeros((n+1,n));jr=np.zeros_like(jl);jp=np.zeros((n+1,1))
        jl[np.arange(m),np.arange(m)]=1
        if args.mean_boundary=='waist':jl[m,m]=1
        else:jr[m,m]=1
        jl[m+1,m+1]=1;jr[np.arange(m+2,n+1),np.arange(m)]=1
        jr[np.arange(m+2,n+1),np.arange(m+1,n)]=qstar
        return jl,jr,jp
    checkpoint_paths=[];checkpoint_root=args.checkpoint_dir/args.out.stem
    checkpoint_root.mkdir(parents=True,exist_ok=False)
    def checkpoint(y,p,derivative,step):
        path=checkpoint_root/f'accepted-{len(checkpoint_paths):03d}.npz'
        metadata=dict(meta,kind='complete_accepted_Newton_nodal_checkpoint',modes=m,
            amplitude=alpha,nu=float(p[0]),exact_float_nu=str(Fraction(float(p[0]))),
            exact_float_amplitude=str(Fraction(float(alpha))),mean_boundary=args.mean_boundary,
            source_sha256=sha(__file__),
            finite_BVP_success=False,mathematical_certificate=False)
        np.savez_compressed(path,radial_nodes=system.current_mesh_x,state=y,
            radial_derivative=derivative,metadata=np.array(json.dumps(metadata)))
        checkpoint_paths.append(dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size,
            nodes=len(system.current_mesh_x),step=dict(step)))
        print(dict(accepted_complete_checkpoint=checkpoint_paths[-1]),flush=True)
    system.accepted_checkpoint=checkpoint
    history=[];linear_history=[];old=bvp.solve_newton;old_prepare=bvp.prepare_sys
    bvp.prepare_sys=make_prepare_sys(np.r_[np.arange(1,m+1),np.arange(m+1)],system=system,band=args.jac_band,drop=args.jac_drop,chunk=args.jac_chunk,history=linear_history)
    bvp.solve_newton=guarded_parameter_newton_krylov_v3(system,history,args.C_floor,args.field_ceiling,args.max_nu,args.newton_iterations)
    try:result=solve_bvp(system.evaluate,bc,r,guess,p=nu,fun_jac=system.jacobian,bc_jac=bc_jac,
        tol=args.tol,bc_tol=args.tol/100,max_nodes=args.max_nodes,verbose=1)
    finally:bvp.solve_newton=old;bvp.prepare_sys=old_prepare
    dd=diagnostic(system,result);left,right=result.y[:,0],result.y[:,-1]
    a0=system.base([0.])[0,0];Cr0=system.controlled([0.],result.p[0])[5][0];CrR=system.controlled([3.125],result.p[0])[5][0]
    waistC=alpha*left[m:].copy();waistC[0]+=Cr0;outerC=alpha*right[m:].copy();outerC[0]+=CrR
    metadata=dict(kind='floating_refined_compact_metric_normalized_Codazzi_branch_v11_full_FFT_matrix_free_preconditioned_Newton',coordinates=meta['coordinates'],
        normalized_state_order=meta['normalized_state_order'],modes=m,physical_frequency_factor=4,
        amplitude=alpha,nu=float(result.p[0]),exact_float_nu=str(Fraction(float(result.p[0]))),
        source_sha256=sha(__file__),object_sha256=sha(args.object),new_metric_family=meta['new_metric_family'],
        exact_bump=meta['exact_bump'],mean_boundary=args.mean_boundary,original_target_fixed=False,
        old_waist_branch_reused=False,waist_nonmean_complement_allowed_to_change=True,outer_boundary=meta['outer_boundary'])
    save_candidate(args.candidate,radial_nodes=result.x,piece_coefficients=result.sol.c,initial_state=left,metadata=np.array(json.dumps(metadata)))
    f_est=alpha*right[m+1:]/((1/(4*graft.omega))*np.sqrt(1+(graft.a_endpoint/(4*graft.omega))**2)*(system.frequency**2-system.frequency))
    report=dict(**metadata,certified=False,finite_BVP_success=bool(result.success and dd['valid']),
        solver_status=int(result.status),solver_message=result.message,diagnostics=dd,guarded_Newton_history=history,
        approximate_linear_solver_history=linear_history,nonlinear_system_unmodified=True,
        target_coefficient_cache_entries=len(system.all_base_cache),
        complete_linearized_operator_used=True,accepted_complete_checkpoints=checkpoint_paths,
        requested_interval=['0','25/8'],initial_radial_nodes=len(r),radial_nodes=len(result.x),
        angular_grid=args.angles,diagnostic_angular_grid=2*args.angles,primitive_nodes=512,tol=args.tol,
        analytic_Jacobian_audit=audit,waist_mean_C=float(waistC[0]),waist_mean_closure_gap=float(waistC[0]+1/a0),
        waist_turn_number=float(-a0*waistC[0]),waist_total_turn=float(-2*np.pi*a0*waistC[0]),
        waist_B_coefficients=(alpha*left[:m]).tolist(),waist_C_coefficients=waistC.tolist(),
        outer_B_coefficients=(alpha*right[:m]).tolist(),outer_C_coefficients=outerC.tolist(),
        outer_C_mean_minus_reference=float(alpha*right[m]),
        normalized_outer_regular_linear_residual_l1=float(np.sum(abs(right[:m]+qstar*right[m+1:]))),
        maximum_boundary_residual=float(np.max(abs(bc(left,right,result.p)))),
        outer_linear_height_estimate=f_est.tolist(),outer_linear_height_homogeneous_A2_norm=float(np.sum(system.frequency**2*abs(f_est))),
        guess_path=str(args.guess),guess_sha256=sha(args.guess),candidate_path=str(args.candidate),candidate_sha256=sha(args.candidate),
        exact_center_parameter=definition['delta_fraction'],origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        mean_retained=True,regular_mean_height=None,regular_mean_flux=None,nonlinear_regular_tail=None,
        whole_affine_parameter_interval=False,whole_real_angular_circle=False,whole_radial_interval=False,
        scipy_version=scipy.__version__,scipy_collocation_module_sha256=sha(inspect.getsourcefile(bvp)),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_compact_metric_branch_probe.py','fourfold_codazzi_compact_metric_return_probe.py',
            'fourfold_codazzi_candidate_shards.py','fourfold_codazzi_chunked_collocation.py',
            'fourfold_codazzi_compact_metric_fast_jacobian.py','fourfold_codazzi_guarded_Newton_krylov_v3.py','fourfold_codazzi_matrix_free_fft_collocation_v3.py',
            'fourfold_phase_codazzi_two_end_probe.py','fourfold_phase_codazzi_rotational_reference_probe.py',
            'fourfold_codazzi_rotational_cap_jacobi_probe.py','fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py')},
        limitations=['Only the LU preconditioner is sparsified; GMRES uses the full untruncated finite Jacobian action and checks its residual. The full nonlinear system and diagnostics are unchanged.',
            'Finite floating complement refinement; convergence of increasing mode counts is not a continuous certificate.',
            'The actual normalized full nonlinear source is measured on an independent doubled grid and radial quarter points.',
            'The opposite mean boundary is printed, not silently set to zero.',
            'True nonlinear regular tail, non-fourth-mode fee, mean height and flux remain unclosed.',
            'The target changes on .05<|r|<.18 and the waist curve also changes; no old g0/old-waist proof is transferred.'],
        wall_seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(dict(success=report['finite_BVP_success'],alpha=alpha,nu=float(result.p[0]),diagnostics=dd,
        waist_mean_gap=report['waist_mean_closure_gap'],outer_A2=report['outer_linear_height_homogeneous_A2_norm'],
        wall_seconds=report['wall_seconds']),flush=True)


if __name__=='__main__':main()
