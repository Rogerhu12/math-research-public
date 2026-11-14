#!/usr/bin/env python3
"""Solve the complete reciprocal body at the true r=3/2 cap cut with full QR.

This is a floating BVP producer, not an infinite-dimensional certificate.
The nonlinear physical boundary quotients, mean row, fourth-mode amplitude
and metric parameter are retained. Every final cubic coefficient is saved;
all polynomial interior tails and rational boundary tails are diagnosed.
"""
from __future__ import annotations
import argparse,inspect,json,time
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace
import numpy as np
import scipy
import scipy.integrate._bvp as bvp
from scipy.integrate import solve_bvp
from flint import ctx
from fourfold_codazzi_reciprocal_cap_cut_system import ReciprocalCapCut,diagnostic
from fourfold_codazzi_reciprocal_candidate_tools import COORDINATES,load_warm_start
from fourfold_codazzi_full_action_qr_collocation import make_prepare_sys
from fourfold_codazzi_guarded_Newton_krylov_v3 import guarded_parameter_newton_krylov_v3
from fourfold_codazzi_candidate_shards import load_candidate,save_candidate
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_phase_local_correction_probe import sha


class AcceptedCheckpointPause(Exception):
    def __init__(self,x,y,p,derivative):
        self.x=x.copy();self.y=y.copy();self.p=p.copy();self.derivative=derivative.copy()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--q-vector',type=Path,required=True)
    ap.add_argument('--guess',type=Path,required=True);ap.add_argument('--modes',type=int,required=True)
    ap.add_argument('--angles',type=int,required=True);ap.add_argument('--amplitude',type=float)
    ap.add_argument('--mean-boundary',choices=['outer','waist'],default='outer')
    ap.add_argument('--mesh-stride',type=int,default=1);ap.add_argument('--tol',type=float,default=2e-6)
    ap.add_argument('--max-nodes',type=int,default=2500);ap.add_argument('--newton-iterations',type=int,default=24)
    ap.add_argument('--pause-after-accepted',type=int,default=1)
    ap.add_argument('--jac-chunk',type=int,default=4);ap.add_argument('--qr-span',type=int,default=32)
    ap.add_argument('--qr-storage',choices=['memory','file','checkpoint'],default='checkpoint')
    ap.add_argument('--qr-scratch',type=Path,default=Path('/workspace/scratch/ac0d699811ad'))
    ap.add_argument('--max-nu',type=float,default=.2);ap.add_argument('--C-floor',type=float,default=.02)
    ap.add_argument('--field-ceiling',type=float,default=30.)
    ap.add_argument('--checkpoint-dir',type=Path,default=Path('/workspace/scratch/ac0d699811ad/codazzi_newton_checkpoints'))
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--candidate',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic();ctx.prec=192;ctx.cap=6
    if args.out.exists() or args.candidate.exists():raise FileExistsError('preserve every real solver outcome')
    if args.angles<8*args.modes or args.mesh_stride<1 or args.candidate.suffix!='.json' or args.pause_after_accepted<0:
        raise ValueError('complete cubic angular support and lossless indexed output are required')
    source=load_candidate(args.guess);oldmeta=json.loads(str(source['metadata']))
    alpha=float(oldmeta['amplitude']) if args.amplitude is None else args.amplitude
    if alpha<0:raise ValueError('negative amplitudes are outside this branch diagnostic')
    geometry,definition=load_exact_object(args.object,512)
    body=RotationalBodyTarget(geometry);graft=RotationalGraftTarget(geometry,args.object)
    system=ReciprocalCapCut(geometry,args.modes,args.angles,body,graft,q_path=args.q_vector,mean_boundary=args.mean_boundary)
    system.alpha=alpha;m=args.modes
    available=source['radial_nodes'][source['radial_nodes']<=1.5]
    if not len(available) or source['radial_nodes'][-1]<1.5:raise ValueError('complete old candidate does not cover the cap cut')
    r=np.unique(np.r_[available[::args.mesh_stride],1.5])
    guess,nu,source,oldmeta,warm=load_warm_start(system,args.guess,r,object_sha256=sha(args.object))
    print(dict(actual_warm_start=warm),flush=True)
    metadata=dict(kind='floating_complete_reciprocal_polynomial_Codazzi_true_cap_cut_branch_with_saved_step_pause',coordinates=COORDINATES,
        normalized_state_order='U sine modes 1..M; V cosine modes 0..M, physical frequency 4m',
        modes=m,physical_frequency_factor=4,amplitude=alpha,exact_float_amplitude=str(Fraction(float(alpha))),
        source_sha256=sha(__file__),object_sha256=sha(args.object),
        new_metric_family=oldmeta['new_metric_family'],exact_bump=oldmeta['exact_bump'],
        mean_boundary=args.mean_boundary,original_target_fixed=False,old_waist_branch_reused=False,
        waist_nonmean_complement_allowed_to_change=True,outer_boundary='r=3/2 actual mode-dependent propagated linear cap graph; nonlinear and mean remainders unpaid',
        exact_cap_cut='3/2',q_vector_path=str(args.q_vector),q_vector_sha256=sha(args.q_vector),
        exact_float_q_values=[str(Fraction(float(q))) for q in system.q_vector],
        mathematical_certificate=False)
    checkpoint_paths=[];checkpoint_root=args.checkpoint_dir/args.out.stem
    checkpoint_root.mkdir(parents=True,exist_ok=False)
    def checkpoint(y,p,derivative,step):
        path=checkpoint_root/f'accepted-{len(checkpoint_paths):03d}.npz'
        checkpoint_meta=dict(metadata,kind='complete_accepted_reciprocal_Newton_nodal_checkpoint',
            nu=float(p[0]),exact_float_nu=str(Fraction(float(p[0]))),finite_BVP_success=False)
        np.savez_compressed(path,radial_nodes=system.current_mesh_x,state=y,
            radial_derivative=derivative,metadata=np.array(json.dumps(checkpoint_meta)))
        checkpoint_paths.append(dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size,
            nodes=len(system.current_mesh_x),step=dict(step)))
        print(dict(accepted_complete_checkpoint=checkpoint_paths[-1]),flush=True)
        if args.pause_after_accepted and len(checkpoint_paths)>=args.pause_after_accepted:
            raise AcceptedCheckpointPause(system.current_mesh_x,y,p,derivative)
    system.accepted_checkpoint=checkpoint
    history=[];linear_history=[];old_newton=bvp.solve_newton;old_prepare=bvp.prepare_sys
    bvp.prepare_sys=make_prepare_sys(system=system,chunk=args.jac_chunk,history=linear_history,
        storage=args.qr_storage,scratch=args.qr_scratch,span=args.qr_span)
    bvp.solve_newton=guarded_parameter_newton_krylov_v3(system,history,args.C_floor,args.field_ceiling,
        args.max_nu,args.newton_iterations)
    try:
        result=solve_bvp(system.evaluate,system.boundary,r,guess,p=nu,
            fun_jac=system.jacobian,bc_jac=system.boundary_jac,tol=args.tol,bc_tol=args.tol/100,
            max_nodes=args.max_nodes,verbose=1)
    except AcceptedCheckpointPause as saved_step:
        x,y,p,f=saved_step.x,saved_step.y,saved_step.p,saved_step.derivative
        h=np.diff(x);sol=bvp.create_spline(y,f,x,h);mid=x[:-1]+h/2
        fm=system.evaluate(mid,sol(mid),p);rm=sol(mid,1)-fm
        rms=bvp.estimate_rms_residuals(system.evaluate,sol,x,h,p,rm,fm)
        result=SimpleNamespace(x=x,y=y,p=p,sol=sol,success=False,status=4,
            message='Intentional pause after a completely accepted saved Newton step; no final BVP convergence claim',
            rms_residuals=rms)
        print(dict(intentional_complete_step_pause=True,accepted_steps=len(checkpoint_paths),
            full_saved_nodes=len(x),maximum_original_RMS_gate_value=float(np.max(rms))),flush=True)
    finally:
        bvp.solve_newton=old_newton;bvp.prepare_sys=old_prepare
    dd=diagnostic(system,result)
    finite_success=bool(result.success and dd['valid'])
    metadata.update(nu=float(result.p[0]),exact_float_nu=str(Fraction(float(result.p[0]))),
        finite_BVP_success=finite_success,solver_status=int(result.status),solver_message=result.message)
    save_candidate(args.candidate,radial_nodes=result.x,piece_coefficients=result.sol.c,
        initial_state=result.y[:,0],metadata=np.array(json.dumps(metadata)))
    report=dict(**metadata,certified=False,diagnostics=dd,warm_start=warm,
        guarded_Newton_history=history,complete_linear_solver_history=linear_history,
        accepted_complete_checkpoints=checkpoint_paths,complete_linearized_operator_used=True,
        all_finite_modes_and_nonlinear_physical_boundary_rows_retained=True,
        original_linear_backward_residual_gate=5e-8,finite_BVP_is_in_new_reciprocal_coordinates=True,
        requested_interval=['0','3/2'],initial_radial_nodes=len(r),radial_nodes=len(result.x),
        pause_after_accepted=args.pause_after_accepted,intentional_saved_step_pause=result.status==4,
        a_pause_is_not_a_failed_mathematical_gate=True,
        angular_grid=args.angles,diagnostic_angular_grid=2*args.angles,
        exact_interior_polynomial_support_index=3*m,tol=args.tol,
        maximum_estimated_relative_radial_residual=float(np.max(result.rms_residuals)),
        maximum_finite_boundary_residual=float(np.max(abs(system.boundary(result.y[:,0],result.y[:,-1],result.p)))),
        candidate_path=str(args.candidate),candidate_sha256=sha(args.candidate),
        exact_center_parameter=definition['delta_fraction'],
        origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        mean_retained=True,true_nonlinear_regular_tail=None,
        whole_affine_parameter_interval=False,whole_real_angular_circle=False,whole_radial_interval=False,
        scipy_version=scipy.__version__,scipy_collocation_module_sha256=sha(inspect.getsourcefile(bvp)),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_reciprocal_cap_cut_system.py','fourfold_codazzi_reciprocal_polynomial_system.py','fourfold_codazzi_reciprocal_candidate_tools.py',
            'fourfold_codazzi_full_action_qr_collocation.py','fourfold_codazzi_block_qr_collocation.py',
            'fourfold_codazzi_block_qr_checkpointed.py','fourfold_codazzi_guarded_Newton_krylov_v3.py',
            'fourfold_codazzi_candidate_shards.py','fourfold_codazzi_compact_metric_branch_probe.py')},
        wall_seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(finite_BVP_success=finite_success,nu=float(result.p[0]),
        radial_nodes=len(result.x),diagnostics=dd,maximum_relative_radial_residual=report['maximum_estimated_relative_radial_residual'],
        wall_seconds=report['wall_seconds']),indent=2),flush=True)


if __name__=='__main__':main()
