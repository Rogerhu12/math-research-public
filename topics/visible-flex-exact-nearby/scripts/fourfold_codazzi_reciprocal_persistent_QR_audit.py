#!/usr/bin/env python3
"""Check an actual persisted substitution pause and both full solves against independent LU.

The small projection here is exclusively a finite linear algebra test.
It is not a continuation candidate and does not certify the source BVP.
"""
from __future__ import annotations
import argparse,json,time,tempfile
from pathlib import Path
import numpy as np
import scipy.integrate._bvp as bvp
from scipy.interpolate import PPoly
from scipy.sparse.linalg import splu
from flint import ctx
from fourfold_codazzi_reciprocal_batched_system import ReciprocalCapCutBatched as ReciprocalCapCut
from fourfold_codazzi_full_action_qr_collocation_persistent import make_prepare_sys
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_phase_local_correction_probe import sha


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--guess',type=Path,default=Path('notes/2026-11-13-R133-compact-metric-m128-alpha070-v14-full-QR-candidate.json'))
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--q-vector',type=Path,default=Path('notes/2026-11-13-R133-cap-cut-r15-q256-with-tail.json'))
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();tick=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve actual linear-test outcomes')
    ctx.prec=192;geometry,_=load_exact_object(args.object,512)
    body=RotationalBodyTarget(geometry);graft=RotationalGraftTarget(geometry,args.object)
    saved=load_candidate(args.guess);meta=json.loads(str(saved['metadata']));pm=int(meta['modes'])
    m,N=8,2048;n=2*m+1
    system=ReciprocalCapCut(geometry,m,128,body,graft,q_path=args.q_vector);system.alpha=float(meta['amplitude'])
    system.factor_checkpoint_identity=json.dumps(dict(object=sha(args.object),q_vector=sha(args.q_vector),source=sha(args.guess)),sort_keys=True)
    p=np.array([float(meta['nu'])])
    available=saved['radial_nodes'][saved['radial_nodes']<1.5]
    r=np.unique(np.r_[available[::40],1.5])
    values=PPoly(saved['piece_coefficients'],saved['radial_nodes'])(r).T
    co=np.zeros((N,len(r)),dtype=complex);ce=np.zeros_like(co)
    co[1:pm+1]=-.5j*values[:pm];co[-pm:]=.5j*values[:pm][::-1]
    ce[0]=values[pm];ce[1:pm+1]=.5*values[pm+1:];ce[-pm:]=.5*values[pm+1:][::-1]
    b=np.fft.ifft(co,axis=0).real*N;c=np.fft.ifft(ce,axis=0).real*N
    Cr=system.controlled(r,p[0])[5];C=Cr+system.alpha*c
    U=b/C;V=-c/(Cr*C);fu=np.fft.fft(U,axis=0)/N;fv=np.fft.fft(V,axis=0)/N
    y=np.r_[-2*fu.imag[1:m+1],2*fv.real[:m+1]];y[m]*=.5
    old_col,old_jac=bvp.prepare_sys(n,len(r),1,system.evaluate,system.boundary,
        system.jacobian,system.boundary_jac,r,np.diff(r))
    col,mid,f,fm=old_col(y,p);boundary=system.boundary(y[:,0],y[:,-1],p)
    original=old_jac(y,p,mid,f,fm,boundary);reference=splu(original)
    rng=np.random.default_rng(2026111318);reports=[]
    rhs_list=[np.r_[col.ravel(order='F'),boundary],rng.normal(size=original.shape[0])]
    with tempfile.TemporaryDirectory(prefix='codazzi-persistent-QR-audit-',dir='/workspace/scratch/ac0d699811ad') as scratch:
        history=[];prepare=make_prepare_sys(system=system,chunk=3,history=history,
            storage='checkpoint',scratch=scratch,span=6)
        _,jac=prepare(n,len(r),1,system.evaluate,system.boundary,system.jacobian,
            system.boundary_jac,r,np.diff(r))
        factor=jac(y,p,mid,f,fm,boundary);tests=[];interruption=None
        class ExpectedCheckpointPause(Exception):pass
        def pause(stage,index):
            if stage=='forward' and index==6:raise ExpectedCheckpointPause('saved forward block six')
        factor.factor.checkpoint_hook=pause
        try:factor.solve(rhs_list[0])
        except ExpectedCheckpointPause as error:
            interruption=dict(stage='forward',next_index=6,actual_exception=str(error))
        if interruption is None:raise RuntimeError('the actual mid-substitution pause did not happen')
        del factor
        factor=jac(y,p,mid,f,fm,boundary)
        for round_name in ('resume_actual_forward_checkpoint','reload_complete_solutions'):
            if round_name=='reload_complete_solutions':
                del factor;factor=jac(y,p,mid,f,fm,boundary)
            for rhs in rhs_list:
                answer=factor.solve(rhs);target=reference.solve(rhs);probe=rng.normal(size=original.shape[0])
                tests.append(dict(round=round_name,measurements=dict(
                    full_QR_residual_against_original_SciPy=float(np.linalg.norm(original@answer-rhs)/np.linalg.norm(rhs)),
                    difference_from_independent_full_LU=float(np.linalg.norm(answer-target)/np.linalg.norm(target)),
                    full_FFT_action_against_original_SciPy=float(np.linalg.norm(factor.operator@probe-original@probe)/np.linalg.norm(original@probe)))))
        reports.append(dict(storage='persistent_complete_checkpoint',history=history,
            actual_mid_substitution_pause=interruption,tests=tests))
        del factor
    passed=all(max(test['measurements'].values())<5e-8 for row in reports for test in row['tests'])
    result=dict(kind='persistent_complete_reciprocal_cap_cut_QR_actual_resume_test',
        all_original_backward_gates_passed=passed,finite_linear_algorithm_only=True,
        source_input_sha256=sha(args.guess),object_sha256=sha(args.object),q_vector_sha256=sha(args.q_vector),modes=m,angles=128,
        full_source_projection_angles=N,radial_nodes=len(r),complete_dimension=original.shape[0],
        all_nonlinear_boundary_rows_and_parameter_retained=True,tests=reports,
        source_sha256=sha(__file__),dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_reciprocal_batched_system.py','fourfold_codazzi_reciprocal_cap_cut_system.py','fourfold_codazzi_full_action_qr_collocation_persistent.py',
            'fourfold_codazzi_block_qr_collocation.py','fourfold_codazzi_block_qr_checkpointed.py','fourfold_codazzi_block_qr_persistent.py')},
        wall_seconds=time.monotonic()-tick)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(dict(all_original_backward_gates_passed=passed,tests=[row['tests'] for row in reports],wall_seconds=result['wall_seconds']),flush=True)
    if not passed:raise SystemExit(2)


if __name__=='__main__':main()
