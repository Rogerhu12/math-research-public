#!/usr/bin/env python3
"""Validate complete local rectangular projectors and every saved-frame jump.

Each original full 193x96 endpoint is an exact dyadic anchor. A new exact
local polynomial is defined by the recorded reference generator and its
exact recurrence. Old unstored floating local generators are not reused.
All complete mean/Gram/error terms and the true Rprime/R are retained.
A complete selected range still is not a global Green or infinite inverse.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[_name]='1'
import numpy as np
from scipy.linalg import qr,eigh
from flint import arb,arb_mat,ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_final_continuous_value_repair import iter_repair
from fourfold_codazzi_full_body_graft_target_jets import ReciprocalFullTargetJets
from fourfold_codazzi_regular_cut_interval_model import (
    q,ab,record,matrix_norm,complete_cell_model,DirectedFFT,DIM,MODES,ORDER)

KIND='actual_complete_weighted_cut_local_projector_validation_v1'
CANDIDATE='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
OBJECT='91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848'
REPAIR='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
ALPHA=Fraction(6890507429876859,9007199254740992)
NU=Fraction(-2572625729470897,72057594037927936)


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)
def save(path,document):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(document,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    if path.suffix=='.gz':raw=gzip.compress(raw,mtime=0)
    temporary=path.with_suffix(path.suffix+'.partial');temporary.write_bytes(raw);temporary.replace(path)
def identity(n):return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def exact_matrix(values):
    if not np.isfinite(values).all():raise ValueError('a complete exact dyadic frame is nonfinite')
    return arb_mat([[arb(float(x)) for x in row] for row in values])
def midpoint_matrix(matrix):
    return np.array([[float(matrix[i,j].mid()) for j in range(matrix.ncols())]
                     for i in range(matrix.nrows())],dtype=float)
def transpose(matrix):return matrix.transpose()
def zero(rows=DIM,columns=MODES):return arb_mat(rows,columns)
def sym(matrix):return (matrix+transpose(matrix))/2
def add_matrices(matrices):
    result=arb_mat(matrices[0].nrows(),matrices[0].ncols())
    for matrix in matrices:result+=matrix
    return result


def gram(frame):
    G=transpose(frame)*frame;delta=matrix_norm(G-identity(G.nrows()))
    if not delta<1:raise ValueError('the entire exact frame Gram gate failed')
    return G,G.inv(),(1-delta).lower(),(1+delta).upper(),delta


def symmetric_largest_upper(matrix):
    """A selected float eigenbasis is checked as exact dyadics in Arb."""
    mid=midpoint_matrix(matrix);_,proposal=eigh((mid+mid.T)/2,check_finite=True)
    U=exact_matrix(proposal);G=transpose(U)*U;delta=matrix_norm(G-identity(G.nrows()))
    if not delta<1:raise ValueError('the complete auxiliary spectral basis lost rank')
    T=transpose(U)*matrix*U;bounds=[]
    for i in range(T.nrows()):
        bound=T[i,i].upper()+sum((ab(T[i,j]) for j in range(T.ncols()) if j!=i),arb(0))
        bounds.append(bound.upper())
    b=max(bounds).upper();answer=(b/(1-delta) if b>=0 else b/(1+delta)).upper()
    return answer,dict(auxiliary_full_dyadic_basis_Gram_error=record(delta),
        complete_congruence_Gershgorin_upper=record(b),spectral_upper=record(answer),
        auxiliary_basis_was_verified_in_this_run_not_assumed_bit_identical_elsewhere=True)


def compressed_rate(frame,H,lower,upper):
    b,evidence=symmetric_largest_upper(transpose(frame)*H*frame)
    answer=(b/lower if b>=0 else b/upper).upper()
    return answer,evidence


def polynomial_frame(A,anchor,step,degree,A_norms,anchor_norm):
    X=[anchor];bounds=[anchor_norm]
    for n in range(degree):
        total=zero();bound=arb(0)
        for j in range(min(ORDER,n)+1):
            total+=A[j]*X[n-j];bound+=A_norms[j]*bounds[n-j]
        X.append(total*q(step/Fraction(n+1)))
        bounds.append((q(abs(step)/Fraction(n+1))*bound).upper())
    # Coefficients below degree vanish exactly by the defining recurrence.
    # No interval subtraction of two correlated low coefficients is used.
    defect=arb(0)
    for k in range(degree,degree+ORDER+1):
        for j in range(ORDER+1):
            if 0<=k-j<=degree:defect+=A_norms[j]*bounds[k-j]
    return X,bounds,defect.upper()


def validate_cell(A,error,Qright,Qleft,left,right,degree):
    step=left-right;h=q(right-left);Q=exact_matrix(Qright);QL=exact_matrix(Qleft)
    G,Ginv,g0,gg0,gram_error=gram(Q);QT=transpose(Q)
    P=Q*Ginv*QT;N=identity(DIM)-P
    whole,_=qr(Qright,mode='full',check_finite=True)
    V=N*exact_matrix(whole[:,MODES:]);VG,VGinv,vg,vgg,vdelta=gram(V)
    norms=[matrix_norm(a) for a in A];M=sum(norms,arb(0)).upper()
    X,xbounds,dpoly=polynomial_frame(A,Q,step,degree,norms,gg0.sqrt().upper())
    growth=(h*M).exp().upper()
    xwhole=min(sum(xbounds,arb(0)).upper(),(growth*(gg0.sqrt()+h*dpoly)).upper()).upper()
    lower=(g0.sqrt()*(-h*M).exp()-h*growth*dpoly).lower()
    if not lower>0:raise ValueError('the exact complete local polynomial Gram needs a finer cell')
    dtrue=(dpoly+error*xwhole).upper()
    H=sym(add_matrices([A[j]*q(Fraction(1,2)**j) for j in range(ORDER+1)]))
    Hnorm=matrix_norm(H)
    variation=(error+sum((matrix_norm(sym(A[j]))*q(1-Fraction(1,2)**j)
                        for j in range(1,ORDER+1)),arb(0))).upper()
    mu0,mu_evidence=compressed_rate(Q,H,g0,gg0)
    nu0,nu_evidence=compressed_rate(V,-H,vg,vgg)
    cross0=(matrix_norm(QT*H*V)/(g0*vg).sqrt()).upper()
    # A recurrence for exact normal coefficients avoids charging the large
    # motion internal to the regular span as a projector rotation.
    normal_generator=[(matrix_norm(N*(a*Q))/g0.sqrt()).upper() for a in A]
    ybounds=[arb(0)]
    for n in range(degree):
        total=arb(0)
        for j in range(min(ORDER,n)+1):
            total+=normal_generator[j]*xbounds[n-j]+norms[j]*ybounds[n-j]
        ybounds.append((h*total/(n+1)).upper())
    normal_uniform=sum(ybounds,arb(0)).upper();bootstrap=[]
    for _ in range(3):
        delta=min(arb(1),(normal_uniform/lower).upper()).upper()
        mu=(mu0+variation+2*Hnorm*delta).upper()
        exponential=(-mu*h).exp()
        better=(g0.sqrt()*min(arb(1),exponential.lower())
                -h*dtrue*max(arb(1),exponential.upper())).lower()
        bootstrap.append(dict(whole_frame_singular_lower=record(lower),
            whole_projector_distance_from_exact_anchor=record(delta),forward_signed_rate_upper=record(mu)))
        if better>lower:lower=better
    delta=min(arb(1),(normal_uniform/lower).upper()).upper()
    e=(dtrue/lower).upper()
    mu=(mu0+variation+2*Hnorm*delta).upper()
    nu=(nu0+variation+2*Hnorm*delta).upper()
    cross=(cross0+variation+2*Hnorm*delta).upper()
    c=(2*cross+e).upper()
    # The next cell starts from the original saved full dyadic endpoint.
    # Its projector jump is included even if it is numerically tiny.
    GL,GLinv,gl,ggl,left_gram_error=gram(QL);PL=QL*GLinv*transpose(QL)
    endpoint=add_matrices(X);normal_endpoint=(identity(DIM)-PL)*endpoint
    jump=min(arb(1),(matrix_norm(normal_endpoint)/lower).upper()).upper()
    if not all(value.is_finite() for value in (error,lower,e,mu,nu,c,jump)):
        raise ValueError('a complete signed rate or full matrix error is nonfinite')
    return dict(exact_polynomial_degree=degree,
        recurrence='X_0=Q_right; X_(n+1)=(left-right)/(n+1) sum_(j=0)^min(3,n) A_j X_(n-j)',
        complete_state_rows=DIM,complete_regular_columns=MODES,
        anchor_full_Gram_error=record(gram_error),left_anchor_full_Gram_error=record(left_gram_error),
        exact_auxiliary_complement_Gram_error=record(vdelta),
        generator_uniform_true_operator_error=record(error),
        generator_reference_coefficient_operator_bounds=list(map(record,norms)),
        exact_polynomial_differential_residual_upper=record(dpoly),
        whole_polynomial_operator_upper=record(xwhole),
        whole_polynomial_smallest_singular_lower=record(lower),
        whole_polynomial_Gram_lower=record((lower*lower).lower()),
        full_true_differential_residual_upper=record(dtrue),
        full_normal_projector_defect_e=record(e),
        complete_forward_signed_rate_mu=record(mu),complete_backward_signed_rate_nu=record(nu),
        complete_cross_c=record(c),whole_projector_variation_from_exact_anchor=record(delta),
        complete_left_interface_projector_jump=record(jump),
        exact_anchor_normal_generator_coefficient_bounds=list(map(record,normal_generator)),
        complete_symmetric_generator_variation=record(variation),
        exact_anchor_symmetric_generator_operator_bound=record(Hnorm),
        exact_anchor_cross_symmetric_operator_bound=record(cross0),
        forward_auxiliary_spectral_verification=mu_evidence,
        backward_auxiliary_spectral_verification=nu_evidence,Gram_bootstrap=bootstrap,
        all_193_rows_96_columns_mean_and_radial_weight_derivative_retained=True,
        every_endpoint_projector_jump_paid=True,
        original_unstored_local_floating_generator_not_used=True,
        complete_continuous_local_projector_estimates=True)


class Frames:
    def __init__(self,path,proposal):
        self.path=Path(path);self.chunks=proposal['complete_frame_chunks']
        self.starts=[row['first_cell'] for row in self.chunks];self.current=None;self.array=None
        next_cell=0
        for row in self.chunks:
            if row['first_cell']!=next_cell or row['end_cell']<=next_cell:
                raise ValueError('original full-frame chunk partition changed')
            next_cell=row['end_cell']
        if next_cell!=len(proposal['rows']):raise ValueError('original frame coverage changed')

    def pair(self,index):
        chunk_index=bisect_right(self.starts,index)-1;row=self.chunks[chunk_index]
        if not row['first_cell']<=index<row['end_cell']:raise ValueError('missing original complete frame cell')
        if self.current!=chunk_index:
            path=self.path/row['file']
            if Path(row['file']).name!=row['file'] or sha(path)!=row['sha256']:
                raise ValueError('an original exact complete frame chunk changed')
            with np.load(path,allow_pickle=False) as saved:
                frames=saved['Q'].copy();indices=saved['descending_cell_indices'].copy()
            count=row['end_cell']-row['first_cell']+1
            if (frames.shape!=(count,DIM,MODES) or frames.dtype!=np.dtype('float64')
                or not np.array_equal(indices,np.arange(row['first_cell'],row['end_cell']+1))
                or not np.isfinite(frames).all()):
                raise ValueError('the complete original frame array or indexing changed')
            if self.current is not None and chunk_index==self.current+1:
                if self.array[-1].tobytes()!=frames[0].tobytes():
                    raise ValueError('two complete original frame chunks disagree at their interface')
            self.current=chunk_index;self.array=frames
        local=index-row['first_cell']
        return self.array[local],self.array[local+1],row


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('candidate','object','repair-report','proposal','frames','out'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--first',type=int,required=True);p.add_argument('--end',type=int,required=True)
    p.add_argument('--degree',type=int,default=24);p.add_argument('--bits',type=int,default=256)
    p.add_argument('--max-new-cells',type=int,default=10000000);a=p.parse_args()
    if not 16<=a.degree<=48 or a.bits<192 or a.max_new_cells<1:
        raise ValueError('full polynomial degree, directed precision and a positive real range required')
    ctx.prec=a.bits;ctx.cap=6;started=time.monotonic()
    if sha(a.candidate)!=CANDIDATE:raise ValueError('the complete original background changed')
    saved=load_candidate(a.candidate);meta=json.loads(str(saved['metadata']))
    if (saved['piece_coefficients'].shape!=(4,6144,65) or len(saved['radial_nodes'])!=6145
        or sha(a.object)!=OBJECT or meta['object_sha256']!=OBJECT
        or Fraction(meta['exact_float_amplitude'])!=ALPHA or Fraction(meta['exact_float_nu'])!=NU):
        raise ValueError('the complete original physical state or exact parameters changed')
    repair=read(a.repair_report)
    if not repair.get('complete') or repair.get('derived_definition_sha256')!=REPAIR:
        raise ValueError('the distinct exact complete continuous repair is required')
    raw=(json.dumps(repair['definition'],sort_keys=True,separators=(',',':'))+'\n').encode()
    if hashlib.sha256(raw).hexdigest()!=REPAIR:raise ValueError('the exact repair definition changed')
    offsets=[];offset_hash=hashlib.sha256()
    for piece,offset,jump in iter_repair(saved,ALPHA):
        offsets.append(offset)
        offset_hash.update((json.dumps(dict(piece=piece,physical_offset=list(map(str,offset))),
            sort_keys=True,separators=(',',':'))+'\n').encode())
    if offset_hash.hexdigest()!=repair['definition']['offset_sequence_sha256']:
        raise ValueError('an original exact physical repair offset changed')
    proposal=read(a.proposal);original=proposal['identity'];rows=proposal['rows']
    if (proposal.get('kind')!='actual_complete_repaired_cut_to_waist_weighted_polynomial_frame_proposal_v1'
        or original['complete_background']['candidate_sha256']!=CANDIDATE
        or original['complete_background']['derived_continuous_centre_definition_sha256']!=REPAIR
        or not proposal.get('all_frames_have_193_rows_and_96_columns')
        or not 0<=a.first<a.end<=len(rows)):
        raise ValueError('the requested original complete frame domain changed')
    for name in ('candidate','object','repair-report'):
        if original['input_SHA256'][name]!=sha(getattr(a,name.replace('-','_'))):
            raise ValueError('an original complete frame scientific input changed')
    if rows[0]['interval'][1]!='9/10':raise ValueError('the real complete cap cut changed')
    for previous,current in zip(rows,rows[1:]):
        if Fraction(previous['interval'][0])!=Fraction(current['interval'][1]):
            raise ValueError('the original full frame radial partition has a gap or overlap')
    if proposal.get('complete') and Fraction(rows[-1]['interval'][0])!=0:
        raise ValueError('the complete original frame proposal did not reach the waist')
    mesh_path=a.frames/'exact-weight-and-base-mesh.json';mesh=read(mesh_path)
    if sha(mesh_path)!=original['exact_weight_mesh_sha256']:raise ValueError('the exact continuous radial weight changed')
    mesh_nodes=list(map(Fraction,mesh['exact_base_partition']));rho_nodes=list(map(Fraction,mesh['exact_positive_rho_nodes']))
    if (len(mesh_nodes)!=len(rho_nodes) or any(x<=0 for x in rho_nodes)
        or any(x>=y for x,y in zip(mesh_nodes,mesh_nodes[1:]))):
        raise ValueError('the entire positive exact continuous radial weight changed')
    nodes=list(map(lambda value:Fraction(float(value)),saved['radial_nodes']))
    ident=dict(kind=KIND,source_sha256=sha(__file__),interval_model_source_sha256=sha(Path(__file__).with_name('fourfold_codazzi_regular_cut_interval_model.py')),
        input_sha256={name:sha(getattr(a,name.replace('-','_'))) for name in ('candidate','object','repair-report','proposal')},
        original_exact_frame_identity=original,exact_weight_mesh_sha256=sha(mesh_path),
        selected_indices=[a.first,a.end],complete_original_proposal_cells=len(rows),
        exact_original_complete_offset_sequence_sha256=offset_hash.hexdigest(),
        exact_alpha=str(ALPHA),exact_nu=str(NU),parameter_offset='0',
        full_state_dimension=DIM,regular_dimension=MODES,polynomial_degree=a.degree,arithmetic_bits=a.bits)
    if a.out.exists():
        document=read(a.out)
        if document.get('identity')!=ident or document.get('selected_cells_complete'):
            raise ValueError('the complete original projector checkpoint changed or already finished')
        if [row['index'] for row in document['rows']]!=list(range(a.first,a.first+len(document['rows']))):
            raise ValueError('the exact prior projector prefix has a missing or duplicated row')
        document['previous_actual_failure']=document.get('failure');document['failure']=None
    else:
        document=dict(kind=KIND,identity=ident,selected_cells_complete=False,failure=None,rows=[],
            global_continuous_Green_criterion_proved=False,complete_infinite_inverse_proved=False,
            true_boundary_and_independent_source_Green_fees_still_required=True)
    target=ReciprocalFullTargetJets(a.object,Fraction(0),512);fft=DirectedFFT();frames=Frames(a.frames,proposal)
    accepted=len(document['rows']);new=0;current=a.first+accepted
    try:
        while current<a.end and new<a.max_new_cells:
            row=rows[current];left,right=map(Fraction,row['interval']);piece=row['original_candidate_piece'];base=row['base_cell']
            if row['index']!=current or not nodes[piece]<=left<right<=nodes[piece+1]:
                raise ValueError('an exact original candidate-piece cell changed')
            bl,br=mesh_nodes[base:base+2];rl,rr=rho_nodes[base:base+2]
            if not bl<=left<right<=br:raise ValueError('an exact weight base cell changed')
            rho_l=rl+(rr-rl)*(left-bl)/(br-bl);rho_r=rl+(rr-rl)*(right-bl)/(br-bl)
            if (str(rho_l)!=row['exact_rho_left'] or str(rho_r)!=row['exact_rho_right']
                or (rho_l-rho_r)/(left-right)!=Fraction(row['exact_rho_derivative'])):
                raise ValueError('the full exact radial weight or its derivative changed')
            Qright,Qleft,chunk=frames.pair(current);began=time.monotonic()
            A,error,definition=complete_cell_model(saved['piece_coefficients'][:,piece,:],nodes[piece],
                left,right,ALPHA,NU,offsets[piece],target,rho_l,rho_r,fft)
            result=validate_cell(A,error,Qright,Qleft,left,right,a.degree)
            result.update(index=current,interval=row['interval'],original_candidate_piece=piece,
                original_frame_chunk=chunk['file'],original_frame_chunk_sha256=chunk['sha256'],
                exact_right_anchor_array_sha256=hashlib.sha256(Qright.tobytes()).hexdigest(),
                exact_left_anchor_array_sha256=hashlib.sha256(Qleft.tobytes()).hexdigest(),
                exact_new_reference_definition=definition,actual_seconds=time.monotonic()-began)
            document['rows'].append(result);current+=1;new+=1
            document['wall_seconds']=time.monotonic()-started;save(a.out,document)
            print(json.dumps(dict(completed=current-a.first,requested=a.end-a.first,original_cell=current-1,
                exact_interval=row['interval'],mu=result['complete_forward_signed_rate_mu']['upper'],
                nu=result['complete_backward_signed_rate_nu']['upper'],e=result['full_normal_projector_defect_e']['upper'],
                jump=result['complete_left_interface_projector_jump']['upper'],seconds=result['actual_seconds'])),flush=True)
        document.update(selected_cells_complete=current==a.end,completed_indices=[a.first,current],
            exact_covered_interval=[rows[current-1]['interval'][0],rows[a.first]['interval'][1]],
            every_selected_original_cell_and_complete_interface_once=True,new_completed_cells=new)
    except BaseException as error:
        document['failure']=dict(type=type(error).__name__,message=str(error),original_cell=current);raise
    finally:
        document['wall_seconds']=time.monotonic()-started;save(a.out,document)
    print(json.dumps(dict(complete=document['selected_cells_complete'],completed=len(document['rows']),
        global_continuous_inverse_proved=False,seconds=document['wall_seconds'])),flush=True)


if __name__=='__main__':main()
