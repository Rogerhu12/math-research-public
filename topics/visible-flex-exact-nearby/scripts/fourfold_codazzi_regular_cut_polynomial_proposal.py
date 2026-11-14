#!/usr/bin/env python3
"""Complete 193-by-96 cut-to-waist proposal with a nonsingular radial weight.

All numerical rates in this file are diagnostics. The saved complete
binary64 frames are exact finite inputs for a later directed polynomial
projector validator. This file does not certify Gram, differential,
boundary, projector-jump, high-frequency, or nonlinear inverse gates.
The original candidate is never changed. Its distinct exact continuous
repair is reconstructed and identified explicitly, including its mean.
"""
from __future__ import annotations
import argparse, gzip, hashlib, json, math, os, time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[_key]='1'
import numpy as np
import scipy
from scipy.linalg import qr, svdvals, eigvalsh, solve
from flint import ctx
from fourfold_codazzi_final_regular_head_model import FinalHead
from fourfold_codazzi_final_head_trial_model import CANDIDATE, ALPHA, NU
from fourfold_codazzi_final_continuous_value_repair import iter_repair
from fourfold_codazzi_full_body_graft_target_jets import ReciprocalFullTargetJets
from fourfold_codazzi_cap128_CI_worker import digest, read
from fourfold_codazzi_phase_high7_CI_worker import save

KIND='actual_complete_repaired_cut_to_waist_weighted_polynomial_frame_proposal_v1'
REPAIR='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
CUT=Fraction(9,10)


def positive_qr(matrix,full=False):
    q,r=qr(matrix,mode='full' if full else 'economic',check_finite=True)
    signs=np.where(np.diag(r[:96,:96])<0,-1.,1.)
    q[:,:96]*=signs[None,:];r[:96]*=signs[:,None]
    return q,r


def atomic_npz(path,**data):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_suffix(path.suffix+'.partial')
    with temporary.open('wb') as stream:np.savez_compressed(stream,**data)
    temporary.replace(path)


class RepairedHead(FinalHead):
    def __init__(self,*args,repair_report,**kwargs):
        super().__init__(*args,**kwargs)
        report=read(repair_report)
        if not report.get('complete') or report.get('derived_definition_sha256')!=REPAIR:
            raise ValueError('the complete distinct exact continuous repair is required')
        raw=(json.dumps(report['definition'],sort_keys=True,separators=(',',':'))+'\n').encode()
        if hashlib.sha256(raw).hexdigest()!=REPAIR:raise ValueError('the complete repair definition changed')
        exact_hash=hashlib.sha256();offsets=[]
        for piece,physical,jump in iter_repair(self.saved,ALPHA):
            exact_hash.update((json.dumps(dict(piece=piece,physical_offset=list(map(str,physical))),
                sort_keys=True,separators=(',',':'))+'\n').encode())
            offsets.append([float(value/ALPHA) for value in physical])
        if exact_hash.hexdigest()!=report['definition']['offset_sequence_sha256']:
            raise ValueError('one of the exact original physical offsets changed')
        self.normalized_offset_proposals=np.asarray(offsets,dtype=float)
        self.identity.update(derived_continuous_centre_definition_sha256=REPAIR,
            all_exact_physical_offsets_sha256=exact_hash.hexdigest(),
            repair_report_sha256=digest(repair_report),
            original_candidate_not_modified=True,floating_repair_evaluation_is_only_a_proposal=True)

    def background(self,r,pieces=None,derivative=0):
        values=super().background(r,pieces,derivative)
        if derivative==0:
            if pieces is None:pieces=self.piece_indices(r)
            indices=np.broadcast_to(np.atleast_1d(pieces),np.atleast_1d(r).shape)
            offset=self.normalized_offset_proposals[indices]
            values[:32]+=offset[:,:32].T
            values[96:129]+=offset[:,32:].T
        return values


def exact_weight(base,left_rho,right_rho,radius):
    left,right=base
    return left_rho+(right_rho-left_rho)*(radius-left)/(right-left)


def weighted_matrices(model,radii,piece,base,rhos):
    values=np.asarray([float(x) for x in radii]);pieces=np.full(len(values),piece,dtype=int)
    raw=model.matrix(values,pieces,'response');out=np.empty_like(raw)
    derivative=(rhos[1]-rhos[0])/(base[1]-base[0]);physical=np.sqrt(model.weights)
    for j,radius in enumerate(radii):
        rho=exact_weight(base,*rhos,radius)
        if rho<=0:raise ValueError('the exact continuous piecewise linear weight is not positive')
        weight=physical.copy();weight[96:]*=float(rho)
        out[:,:,j]=raw[:,:,j]*weight[:,None]/weight[None,:]
        out[96:,96:,j]+=float(derivative/rho)*np.eye(97)
    return out


def fundamental_polynomial(matrices,frame,step,order):
    ar,am,al=(matrices[:,:,j] for j in range(3))
    # The following rounded matrices define a proposal, not exact true jets.
    a=[ar,4*am-3*ar-al,2*(al+ar-2*am)]
    x=[frame.copy()]
    for n in range(order):
        total=np.zeros_like(frame)
        for j in range(min(2,n)+1):total+=a[j]@x[n-j]
        x.append((step/(n+1))*total)
    return a,x


def evaluate(coefficients,s,derivative=False):
    value=np.zeros_like(coefficients[0])
    if derivative:
        for k in range(len(coefficients)-1,0,-1):value=value*s+k*coefficients[k]
    else:
        for coefficient in reversed(coefficients):value=value*s+coefficient
    return value


def rates_at_midpoint(matrix,coefficients,step):
    x=evaluate(coefficients,.5);xr=evaluate(coefficients,.5,True)/step
    whole,r=positive_qr(x,True);p=whole[:,:96];q=whole[:,96:]
    sym=(matrix+matrix.T)/2;singular=svdvals(x)
    defect=xr-matrix@x;normal=defect-p@(p.T@defect)
    e=float(np.linalg.norm(normal,ord='fro')/singular[-1])
    cross=float(np.linalg.norm(p.T@sym@q,ord='fro'))
    return dict(sampled_mu=float(eigvalsh(p.T@sym@p,subset_by_index=[95,95])[0]),
        sampled_nu=float(eigvalsh(-q.T@sym@q,subset_by_index=[96,96])[0]),
        sampled_cross_c=2*cross+e,sampled_projector_defect_e=e,
        sampled_frame_minimum_singular_value=float(singular[-1]),
        sampled_frame_maximum_singular_value=float(singular[0]),
        diagnostic_samples_only_not_continuous_bounds=True)


def boundary_diagnostics(frame,boundary):
    full,r=positive_qr(frame,True);p=full[:,:96];q=full[:,96:]
    up=p[:96];uq=q[:96];singular=svdvals(up)
    result=dict(all_96_waist_odd_rows_retained=True,all_97_even_and_mean_states_retained=True,
        sampled_waist_restriction_singular_values=singular.tolist(),
        minimum_waist_singular_value=float(singular[-1]),interval_rank_proved=False)
    if singular[-1]>0:
        result['sampled_left_boundary_inverse_norm']=float(1/singular[-1])
        result['sampled_left_boundary_feedback_D0']=float(np.linalg.norm(solve(up,uq),ord=2))
    return result


def scalar_diagnostics(rows,boundaries,right_error):
    ordered=list(reversed(rows));s=boundaries.get('sampled_left_boundary_feedback_D0')
    if s is None:return dict(available=False,reason='floating left boundary rank failed')
    def factor(rate,length):
        exponential=math.exp(rate*length)
        integral=length if rate==0 else math.expm1(rate*length)/rate
        return exponential,integral
    maximum_s=s;t=right_error;maximum_t=t
    try:
        for row in ordered:
            length=float(Fraction(row['interval'][1])-Fraction(row['interval'][0]))
            ex,integral=factor(row['sampled_mu'],length)
            s=ex*(s+row['floating_QR_projector_join_residual'])+integral*row['sampled_cross_c']
            maximum_s=max(maximum_s,s)
        for row in rows:
            length=float(Fraction(row['interval'][1])-Fraction(row['interval'][0]))
            ex,integral=factor(row['sampled_nu'],length)
            t=ex*t+integral*row['sampled_projector_defect_e']+row['floating_QR_projector_join_residual']
            maximum_t=max(maximum_t,t)
        if not all(math.isfinite(x) for x in (maximum_s,maximum_t,maximum_s*maximum_t)):
            raise OverflowError('the sampled scalar diagnostic exceeded floating range')
        return dict(available=True,sampled_s=maximum_s,sampled_t_without_true_cap_fee=maximum_t,
            sampled_product_without_true_cap_fee=maximum_s*maximum_t,
            full_cap_boundary_error_still_required=True,continuous_gates_proved=False)
    except OverflowError as exc:
        return dict(available=False,reason=str(exc),continuous_gates_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('candidate','object','q-vector','waist-row','repair-report','cut-native'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--work',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--order',type=int,default=24);p.add_argument('--regularization',type=Fraction,default=Fraction(1,64))
    p.add_argument('--growth-target',type=float,default=2.)
    p.add_argument('--max-new-cells',type=int,default=10000000)
    a=p.parse_args();ctx.prec=192;ctx.cap=6;started=time.monotonic()
    if not (16<=a.order<=48 and 0<a.regularization<=1 and 0<a.growth_target<=2 and a.max_new_cells>0):
        raise ValueError('explicit full polynomial order, positive weight and bounded step target required')
    a.work.mkdir(parents=True,exist_ok=True);checkpoint=a.work/'checkpoint.json'
    if a.out.exists():raise FileExistsError('preserve every actual original proposal outcome')
    cut=read(a.cut_native)
    if (not cut.get('complete') or cut.get('candidate_sha256')!=CANDIDATE
        or cut.get('derived_definition_sha256')!=REPAIR or cut.get('exact_cut')!=str(CUT)
        or not cut.get('no_head_or_high_boundary_row_deleted')):
        raise ValueError('the complete original repaired moving cut and mean must be retained')
    model=RepairedHead(a.candidate,a.object,a.q_vector,a.waist_row,
        repair_report=a.repair_report,modes=96,angles=1024,boundary_angles=8192)
    target=ReciprocalFullTargetJets(a.object,Fraction(0),512)
    original_nodes=list(map(lambda x:Fraction(float(x)),model.nodes))
    basecuts=sorted({Fraction(0),CUT}|{r for r in original_nodes if 0<r<CUT}
        |{r for r in target.cuts if 0<r<CUT})
    # A positive binary64 value is an exact dyadic definition of rho at
    # each base node. Its linear interpolation is exact and continuous.
    rhos=[]
    for start in range(0,len(basecuts),128):
        radial=np.array([float(x) for x in basecuts[start:start+128]])
        kval=model.data(radial)['target'][3]
        proposal=(kval*kval+float(a.regularization)**2)**.25
        if not np.isfinite(proposal).all() or not (proposal>0).all():
            raise ValueError('a complete positive radial weight proposal failed')
        rhos.extend(Fraction(float(x)) for x in proposal)
    mesh=dict(exact_base_partition=list(map(str,basecuts)),exact_positive_rho_nodes=list(map(str,rhos)),
        original_candidate_and_scalar_germs_all_retained=True,
        weight='R=diag(I_96,rho I_97) in the complete physical orthonormal moving basis',
        rho='exact continuous piecewise linear interpolation of recorded positive dyadic endpoint values',
        full_even_mean_scaled_with_all_other_even_states=True,
        transformed_generator='R A R^-1 + Rprime R^-1; even diagonal contains rho_prime/rho')
    save(a.work/'exact-weight-and-base-mesh.json',mesh)
    identity=dict(kind=KIND,source_sha256=digest(__file__),complete_background=model.identity,
        input_SHA256={name:digest(getattr(a,name.replace('-','_'))) for name in
            ('candidate','object','q-vector','waist-row','repair-report','cut-native')},
        exact_weight_mesh_sha256=digest(a.work/'exact-weight-and-base-mesh.json'),
        exact_interval=['0','9/10'],regular_dimension=96,state_dimension=193,
        polynomial_order=a.order,step_growth_target=Fraction(a.growth_target).__str__(),
        exact_regularization=str(a.regularization),python_float_object='IEEE binary64 proposals only',
        numpy_version=np.__version__,scipy_version=scipy.__version__,
        finite_head_only=True,complete_infinite_high_and_true_cap_fees_retained_as_unpaid_inputs=True)
    if checkpoint.exists():
        doc=read(checkpoint)
        if doc['identity']!=identity or doc.get('complete'):raise ValueError('the exact proposal checkpoint changed or is complete')
        for chunk in doc['complete_frame_chunks']:
            if digest(a.work/chunk['file'])!=chunk['sha256']:raise ValueError('a complete original saved frame chunk changed')
        if digest(a.work/'current-frame.npz')!=doc['current_frame_sha256']:
            raise ValueError('the complete current frame changed')
        with np.load(a.work/'current-frame.npz',allow_pickle=False) as stored:frame=stored['Q'].copy()
        right=Fraction(doc['current_radius']);base_index=doc['current_base_index']
    else:
        initial=np.array([[float.fromhex(v) for v in row] for row in cut['kernel_proposal']['complete_basis_binary64_hex']])
        if initial.shape!=(193,96):raise ValueError('all original complete kernel columns are required')
        initial[96:]*=float(rhos[-1]);frame,_=positive_qr(initial)
        J=np.array([[float.fromhex(x) for x in row['complete_even_binary64_proposal_hex']] for row in cut['rows']])
        M=np.array([float.fromhex(x) for x in cut['independent_mean_row']['binary64_proposal_hex']])
        boundary=np.zeros((97,193));boundary[:96,:96]=np.eye(96)
        boundary[:96,96:]=J/float(rhos[-1]);boundary[96,96:]=M/float(rhos[-1])
        full,_=positive_qr(frame,True);bq=boundary@full[:,96:];singular=svdvals(bq)
        defect=boundary@frame
        right_diag=dict(complete_97_original_cut_rows=True,original_even_mean_retained=True,
            sampled_complete_cut_kernel_error=float(np.linalg.norm(defect,ord=2)),
            sampled_cut_complement_minimum_singular_value=float(singular[-1]),
            sampled_cut_complement_inverse_norm=float(1/singular[-1]),
            sampled_cut_feedback_without_true_cap_error=float(np.linalg.norm(solve(bq,defect),ord=2)),
            true_cap_Hessian_full_mean_and_high_output_fees_not_yet_consumed=True)
        doc=dict(kind=KIND,identity=identity,complete=False,failure=None,rows=[],complete_frame_chunks=[],
            exact_right_cut_diagnostics=right_diag,current_radius=str(CUT),current_base_index=len(basecuts)-2,
            all_frames_have_193_rows_and_96_columns=True,complete_body_inverse_proved=False,
            continuous_Gram_and_defect_gates_proved=False,true_parameter_Schur_proved=False,
            ordinary_sources_and_all_true_interface_sources_still_required=True)
        right=CUT;base_index=len(basecuts)-2
    accepted=len(doc['rows']);pending_rows=[];pending_frames=[frame.copy()];new=0
    def checkpoint_complete_chunk():
        nonlocal pending_rows,pending_frames
        if not pending_rows:return
        first=len(doc['rows']);end=first+len(pending_rows)
        path=a.work/f'frames-{first:06d}-{end:06d}.npz'
        if path.exists():raise FileExistsError('inspect an unregistered complete saved frame chunk')
        atomic_npz(path,Q=np.stack(pending_frames),descending_cell_indices=np.arange(first,end+1,dtype=np.int64))
        doc['complete_frame_chunks'].append(dict(file=path.name,sha256=digest(path),
            first_cell=first,end_cell=end,complete_frame_count=len(pending_frames),bytes=path.stat().st_size))
        doc['rows'].extend(pending_rows);doc.update(current_radius=str(right),current_base_index=base_index)
        atomic_npz(a.work/'current-frame.npz',Q=frame)
        doc['current_frame_sha256']=digest(a.work/'current-frame.npz');doc['wall_seconds']=time.monotonic()-started
        save(checkpoint,doc);save(a.out,doc);pending_rows=[];pending_frames=[frame.copy()]
    try:
        while right>0 and new<a.max_new_cells:
            base=(basecuts[base_index],basecuts[base_index+1]);base_rhos=(rhos[base_index],rhos[base_index+1])
            if not base[0]<right<=base[1]:raise ValueError('the exact original common base cell changed')
            left=base[0];piece=bisect_right(original_nodes,(left+right)/2)-1
            while True:
                midpoint=(left+right)/2
                matrices=weighted_matrices(model,[right,midpoint,left],piece,base,base_rhos)
                norm=max(math.sqrt(np.linalg.norm(matrices[:,:,j],1)*np.linalg.norm(matrices[:,:,j],np.inf)) for j in range(3))
                if float(right-left)*norm<=a.growth_target:break
                left=(left+right)/2
            step=float(left-right);amodel,coefficients=fundamental_polynomial(matrices,frame,step,a.order)
            endpoint=evaluate(coefficients,1.);next_frame,triangular=positive_qr(endpoint)
            gram=float(np.linalg.norm(next_frame.T@next_frame-np.eye(96),ord=2))
            if not np.isfinite(next_frame).all() or not gram<1e-10:
                raise ValueError('the complete weighted proposal frame lost its floating Gram gate')
            row=rates_at_midpoint(matrices[:,:,1],coefficients,step)
            qr_residual=endpoint-next_frame@triangular
            row.update(index=len(doc['rows'])+len(pending_rows),interval=list(map(str,(left,right))),
                base_cell=base_index,original_candidate_piece=piece,
                exact_rho_left=str(exact_weight(base,*base_rhos,left)),
                exact_rho_right=str(exact_weight(base,*base_rhos,right)),
                exact_rho_derivative=str((base_rhos[1]-base_rhos[0])/(base[1]-base[0])),
                all_original_mean_columns_retained=True,physical_Gram_and_Rprime_over_R_retained=True,
                floating_frame_Gram_residual=gram,
                floating_QR_projector_join_residual=float(np.linalg.norm(qr_residual,ord='fro')/svdvals(endpoint)[-1]),
                sampled_step_matrix_norm=float(right-left)*norm,
                local_floating_operator_model_sha256=hashlib.sha256(np.stack(amodel).tobytes()).hexdigest(),
                high_order_local_polynomial_not_yet_interval_validated=True)
            pending_rows.append(row);pending_frames.append(next_frame.copy());frame=next_frame;right=left;new+=1
            if right==base[0] and right>0:base_index-=1
            if len(pending_rows)>=16:checkpoint_complete_chunk()
            if new%32==0:print(dict(complete_saved_cells=len(doc['rows']),actual_radius=str(right),
                latest_sampled_mu=row['sampled_mu'],latest_sampled_nu=row['sampled_nu'],
                latest_sampled_e=row['sampled_projector_defect_e'],seconds=time.monotonic()-started),flush=True)
        checkpoint_complete_chunk()
        if right==0:
            left_diag=boundary_diagnostics(frame,None)
            doc.update(complete=True,exact_left_waist_diagnostics=left_diag,
                sampled_scalar_feedback=scalar_diagnostics(doc['rows'],left_diag,
                    doc['exact_right_cut_diagnostics']['sampled_cut_feedback_without_true_cap_error']),
                exact_covered_interval=['0','9/10'],all_original_common_cells_covered=True)
        doc.update(new_saved_cells=len(doc['rows'])-accepted,wall_seconds=time.monotonic()-started)
        save(checkpoint,doc);save(a.out,doc)
    except BaseException as error:
        # Only fully written chunks count as completed reusable frames.
        doc.update(failure=dict(type=type(error).__name__,message=str(error)),
            discarded_unpublished_proposal_cells=len(pending_rows),wall_seconds=time.monotonic()-started)
        save(a.out,doc);raise
    print(dict(complete=doc['complete'],complete_saved_cells=len(doc['rows']),radius=doc['current_radius'],
        continuous_inverse_proved=False,seconds=time.monotonic()-started),flush=True)


if __name__=='__main__':main()
