#!/usr/bin/env python3
"""Complete M96 regular-subspace proposal for a continuous head inverse.

All arithmetic here is floating diagnostic arithmetic.  The exact dyadic
saved Hermite frame is a later interval-validation input, never an already
proved continuous invariant subspace.  No Fourier entry, mean, or outer
Robin row is omitted.  Each complete Magnus/QR segment is saved before its
checkpoint advances.  It is not a raw unstable fundamental matrix.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import time
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[_name]='1'
import numpy as np
import scipy
from scipy.linalg import expm, qr, solve
from flint import ctx
from fourfold_codazzi_final_regular_head_model import FinalHead
from fourfold_codazzi_final_head_trial_model import CANDIDATE, ALPHA, NU, RIGHT

KIND='actual_final_M96_continuous_regular_subspace_Magnus_QR_proposal'

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def exact(x):return str(Fraction(float(x)))

def atomic_json(path,data):
    path=Path(path);tmp=path.with_suffix(path.suffix+'.partial')
    tmp.write_text(json.dumps(data,indent=2,allow_nan=False)+'\n');os.replace(tmp,path)

def atomic_npz(path,**data):
    path=Path(path);tmp=path.with_suffix(path.suffix+'.partial')
    with tmp.open('wb') as f:np.savez_compressed(f,**data)
    os.replace(tmp,path)

def positive_qr(X):
    Q,R=qr(X,mode='economic',check_finite=False)
    signs=np.where(np.diag(R)<0.,-1.,1.)
    Q=Q*signs[None,:];R=signs[:,None]*R
    return Q,R

def frame_derivative(A,Q):
    """Continuous QR gauge; P=QQ^T has (I-P)(P'-AP)=0 for an exact flow."""
    AQ=A@Q;B=Q.T@AQ
    R=np.triu(B+B.T,1)+np.diag(np.diag(B))
    return AQ-Q@R

def transformed(model,r,pieces):
    raw=model.matrix(np.atleast_1d(r),np.atleast_1d(pieces),'response')
    weight=np.sqrt(model.weights)
    return raw*weight[:,None,None]/weight[None,:,None]

def initial_frame(model):
    U,BR,amplitude,description=model.regular_rows()
    n,m=model.n,model.m;weight=np.sqrt(model.weights)
    # BR has 97 rows (true model mean + every j=1..96 Robin row).
    # Its even block is square.  Every u amplitude is an independent port.
    even=BR[:,m:]
    if even.shape!=(m+1,m+1):raise ValueError('the complete mean/even right block changed')
    v=solve(even,-BR[:,:m],assume_a='gen',check_finite=True)
    physical=np.vstack((np.eye(m),v))
    Q,R=positive_qr(weight[:,None]*physical)
    residual=BR@(Q/weight[:,None])
    gram=Q.T@Q-np.eye(m)
    error=float(np.linalg.norm(residual,ord=2))
    if not error<1e-9 or not np.linalg.norm(gram,ord=2)<1e-11:
        raise ValueError('the complete right regular kernel proposal failed its original floating check')
    return Q,dict(state_dimension=n,regular_dimension=m,right_rows=m+1,
        original_m4_and_full_mean_retained=True,
        even_block_condition_2=float(np.linalg.cond(even)),
        all_row_model_kernel_residual_2=error,
        full_Gram_error_2=float(np.linalg.norm(gram,ord=2)),
        complete_L2_Gram=model.weights.tolist(),
        physical_boundary_description=description)

def prepare(a):
    model=FinalHead(a.candidate,a.object,a.q_vector,a.waist_row,
        modes=96,angles=1024,boundary_angles=8192)
    identity=dict(kind=KIND,source_sha256=sha(__file__),model=model.identity,
        candidate_sha256=CANDIDATE,exact_alpha=str(ALPHA),exact_nu=str(NU),
        n=193,regular_dimension=96,complement_dimension=97,
        parameter_unknown_in_this_proposal=False,
        radial_method='fourth-order two-Gauss Magnus exponential then complete positive-diagonal QR',
        growth_target=exact(a.growth_target),left_cut=exact(a.left),
        scipy_version=scipy.__version__,numpy_version=np.__version__,
        source_coordinates='z=sqrt(W)h, physical unnormalized moving h',
        angular_frequency_factor=4,finite_angular_projection=96,
        whole_frequency_inverse_claimed=False,continuous_invariance_certified=False)
    a.work.mkdir(parents=True,exist_ok=True)
    cp=a.work/'checkpoint.json';qp=a.work/'current-frame.npz'
    if cp.exists():
        doc=json.loads(cp.read_text())
        if doc['identity']!=identity:raise ValueError('the original complete proposal identity changed')
        if doc['complete']:raise FileExistsError('preserve the complete proposal')
        if sha(qp)!=doc['current_frame_sha256']:raise ValueError('incomplete saved full current frame')
        with np.load(qp,allow_pickle=False) as x:Q=x['Q'].copy()
    else:
        Q,initial=initial_frame(model)
        atomic_npz(qp,Q=Q)
        doc=dict(kind=KIND,identity=identity,complete=False,initial_right_kernel=initial,
            radius=exact(RIGHT),next_candidate_piece=len(model.nodes)-2,
            current_frame_sha256=sha(qp),segments=[],runs=[],maximum_Gram_error=0.,
            largest_observed_model_step_norm=0.,failure=None,
            complete_body_BVP_inverse_proved=False,actual_nu_Schur_nonzero_proved=False)
        atomic_json(cp,doc)
    return model,Q,doc

def complete_endpoint(model,Q,doc):
    U,BR,amplitude,_=model.regular_rows();w=np.sqrt(model.weights)
    C=U@(Q/w[:,None]);singular=np.linalg.svd(C,compute_uv=False)
    doc['left_model_kernel_match']=dict(
        radius=doc['radius'],all_waist_u_rows=96,regular_dimension=96,
        singular_values=singular.tolist(),minimum_singular_value=float(singular[-1]),
        condition_2=float(singular[0]/singular[-1]),
        actual_physical_waist_amplitude_row_on_regular_basis=(amplitude@(Q/w[:,None])).tolist(),
        diagnostic_only=True,interval_rank_not_proved=True)
    doc['complete']=True

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate',type=Path,required=True)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--q-vector',type=Path,default=Path('notes/2026-11-13-R133-regular-r25over8-q256-floating.json'))
    p.add_argument('--waist-row',type=Path,default=Path('notes/2026-11-14-R133-final-waist-complete-96-amplitude-row-rational.json'))
    p.add_argument('--left',type=float,default=0.)
    p.add_argument('--growth-target',type=float,default=4.)
    p.add_argument('--max-new-segments',type=int,default=64)
    p.add_argument('--work',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();ctx.prec=192;ctx.cap=6;start=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every previous diagnostic result')
    if not (0<=a.left<float(RIGHT) and 0<a.growth_target<=4 and a.max_new_segments>0):
        raise ValueError('explicit positive growth/work budget and actual interval required')
    run=dict(kind=KIND,source_sha256=sha(__file__),complete=False,mathematical_certificate=False,
        complete_body_BVP_inverse_proved=False,actual_nu_Schur_nonzero_proved=False,failure=None)
    try:
        model,Q,doc=prepare(a);count=0
        if Q.shape!=(193,96):raise ValueError('the full regular subspace must retain all columns')
        first=len(doc['segments']);sqrt3=math.sqrt(3.);weight=np.sqrt(model.weights)
        while count<a.max_new_segments and Fraction(doc['radius'])>Fraction(a.left):
            right=float(Fraction(doc['radius']));piece=int(doc['next_candidate_piece'])
            if not model.nodes[piece]<=right<=model.nodes[piece+1]:
                raise ValueError('the proposal left its actual original background germ')
            bound=max(float(model.nodes[piece]),a.left)
            remaining=right-bound
            if remaining<=0:raise ValueError('a completed background piece was not advanced')
            # A floating step-selection diagnostic, not a continuous upper bound.
            amid=transformed(model,[right-remaining/2],[piece])[:,:,0]
            norm=math.sqrt(np.linalg.norm(amid,1)*np.linalg.norm(amid,np.inf))
            pieces=max(1,math.ceil(remaining*norm/a.growth_target))
            left=bound if pieces==1 else right-remaining/pieces
            h=left-right
            gauss=np.array([right+h*(.5-sqrt3/6),right+h*(.5+sqrt3/6)])
            AA=transformed(model,gauss,[piece,piece]);A1,A2=AA[:,:,0],AA[:,:,1]
            Omega=h*(A1+A2)/2-sqrt3*h*h*(A1@A2-A2@A1)/12
            propagated=expm(Omega)@Q
            Qleft,R=positive_qr(propagated)
            gram=float(np.linalg.norm(Qleft.T@Qleft-np.eye(96),ord=2))
            if not np.isfinite(Qleft).all() or not gram<1e-10:
                raise ValueError('the full floating Gram or exponential became invalid')
            endpoints=transformed(model,[left,right],[piece,piece])
            dleft=frame_derivative(endpoints[:,:,0],Qleft)
            dright=frame_derivative(endpoints[:,:,1],Q)
            number=len(doc['segments']);segment=a.work/('segment-%06d.npz'%number)
            if segment.exists():raise FileExistsError('an unregistered complete segment must be inspected')
            atomic_npz(segment,left=np.array(left),right=np.array(right),Q_left=Qleft,Q_right=Q,
                Qr_left=dleft,Qr_right=dright,original_candidate_piece=np.array(piece))
            row=dict(number=number,interval=[exact(left),exact(right)],original_candidate_piece=piece,
                path=segment.name,sha256=sha(segment),complete_regular_columns=96,
                full_Gram_error_2=gram,observed_midpoint_matrix_norm=float(norm),
                observed_step_norm=float(remaining*norm/pieces),
                minimum_QR_diagonal=float(np.min(np.diag(R))),
                maximum_QR_diagonal=float(np.max(np.diag(R))))
            doc['segments'].append(row);Q=Qleft;count+=1
            doc['radius']=exact(left)
            if left==bound and left>a.left:doc['next_candidate_piece']=piece-1
            doc['maximum_Gram_error']=max(doc['maximum_Gram_error'],gram)
            doc['largest_observed_model_step_norm']=max(doc['largest_observed_model_step_norm'],row['observed_step_norm'])
            atomic_npz(a.work/'current-frame.npz',Q=Q)
            doc['current_frame_sha256']=sha(a.work/'current-frame.npz')
            atomic_json(a.work/'checkpoint.json',doc)
            if count%8==0:print(dict(complete_segment=number,left=left,piece=piece,Gram_error=gram),flush=True)
        if Fraction(doc['radius'])==Fraction(a.left):complete_endpoint(model,Q,doc)
        run.update(complete=doc['complete'],identity=doc['identity'],new_complete_segments=count,
            first_segment=first,final_segment=len(doc['segments'])-1,covered_interval=[doc['radius'],str(RIGHT)],
            checkpoint=str(a.work/'checkpoint.json'),maximum_Gram_error=doc['maximum_Gram_error'],
            current_full_frame=str(a.work/'current-frame.npz'),
            initial_right_kernel=doc['initial_right_kernel'],
            left_model_kernel_match=doc.get('left_model_kernel_match'),
            interval_defects_and_true_DN_not_yet_paid=True)
        doc['runs'].append(dict(out=str(a.out),new_complete_segments=count,wall_seconds=time.monotonic()-start))
        atomic_json(a.work/'checkpoint.json',doc)
        run['checkpoint_sha256']=sha(a.work/'checkpoint.json')
    except Exception as exc:
        run['failure']=dict(type=type(exc).__name__,message=str(exc));raise
    finally:
        run['wall_seconds']=time.monotonic()-start;a.out.parent.mkdir(parents=True,exist_ok=True)
        atomic_json(a.out,run)
    print(dict(complete=run['complete'],new_segments=run.get('new_complete_segments'),out=str(a.out)),flush=True)

if __name__=='__main__':main()
