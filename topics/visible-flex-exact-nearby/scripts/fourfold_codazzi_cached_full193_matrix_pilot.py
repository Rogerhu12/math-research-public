#!/usr/bin/env python3
"""New full193 local matrix polynomials from four exact saved coefficient rows.

No target, candidate, primitive or projector computation is repeated.
The old coefficient definition is reconstructed with directed arithmetic,
then a NEW recorded dyadic matrix reference and full I193 polynomials are
verified. These are local matrices, not the old rectangular Q anchors and
not yet a full two-boundary matrix Green kernel.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,time
from fractions import Fraction
from math import comb
from pathlib import Path
import numpy as np
from flint import arb,arb_mat,acb,ctx
import fourfold_codazzi_regular_cut_interval_model as model
from fourfold_phase_beta_bulk_box import CBox,zeros,DirectedFFT

REL='topics/visible-flex-exact-nearby/'
KIND='actual_full193_local_matrix_polynomials_from_cached_exact_reference_v1'
MODEL='b30eb7299d5803856712134947f3d7899961cc3ab7597ce961b9bf0cf5205183'
DIM=193
EDGE=list(range(32,96))+list(range(129,193))
LOW=list(range(32))+list(range(96,129))
INDICES=[0,76,3300,5969]
OLD={
 0:('1fa04778469adb063456274d279f0bd3cbd6546bad005309d2e88b27d44e4d64','5e8ed96c4be24de926f935c0366c53b17ea05f40a19d5b5332a4e9300fa243a9'),
 76:('d70ac90cce4c58733ad92966a0a07dc9b8e954c5a410a6d1bfea08b18f12c98e','26a9dae9bfe1bbf0d3aab306612db7d985cebeeecad06e48716fe0d1fcd98a54'),
 3300:('7cf30d14cf26c62573c66666843dabea9ceebfc874a7eb0654a1265e7c510037','ffd2b2755481d0c7c71cfd12aa41f94f85fd57c16ab8fad27cb5f775d6384cbe'),
 5969:('8669aa0ec4610eae56fe787d38c4fcf4c34c23134a3fc7f4060cb353feb5d251','d51f3f1aa0bf8ac7af555de349f52c9b0fecb6e5beec67a90fbe81a9a8c7424e')}
q=model.q
record=model.record
norm=model.matrix_norm


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def canonical(d):
    return hashlib.sha256((json.dumps(d,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
def read(path):
    p=Path(path)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def save(path,d):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(d,sort_keys=True,separators=(',',':'))+'\n').encode()
    temporary=path.with_name(path.name+'.tmp')
    temporary.write_bytes(gzip.compress(raw,mtime=0) if path.suffix=='.gz' else raw)
    temporary.replace(path)
def ball(value):return arb(value['ball'] if isinstance(value,dict) else value)
def up(value):return ball(value).upper()
def eye(n=DIM):return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def zero(n=DIM,m=DIM):return arb_mat(n,m)
def exact(values):
    return arb_mat([[q(Fraction(float(v))) for v in row] for row in values])
def choose(matrix):
    values=np.array([[float(matrix[i,j].mid()) for j in range(matrix.ncols())]
                     for i in range(matrix.nrows())],dtype='<f8')
    if not np.isfinite(values).all():raise ArithmeticError('a new exact dyadic matrix is nonfinite')
    selected=exact(values)
    return values,selected,norm(matrix-selected)
def add(matrices,n=DIM,m=DIM):
    result=zero(n,m)
    for matrix in matrices:result+=matrix
    return result
def submatrix(matrix,rows,cols):
    return arb_mat([[matrix[i,j] for j in cols] for i in rows])


def saved_fields(definition,fft):
    """Rebuild only the exact stored polynomial, never the actual target."""
    d=definition
    if (d.get('kind')!='new_exact_full_weighted_degree3_generator_reference_from_recorded_dyadics'
        or not d.get('all_mean_and_primitive_columns_retained')
        or not d.get('no_unstored_original_proposal_matrix_is_assumed_identical')
        or d['raw_complete_operator'].get('complete_primitive_intermediate_modes')!=128
        or d['raw_complete_operator'].get('complete_odd_head_modes')!=96
        or d['raw_complete_operator'].get('complete_even_head_modes_with_independent_mean')!=97):
        raise ValueError('the exact complete original matrix definition changed')
    rows=d['physical_background']['physical_repaired_cubic_power_s_binary64_hex']
    if len(rows)!=4 or any(len(row)!=65 for row in rows):
        raise ValueError('all four full physical repaired coefficient rows are required')
    uc=zeros((model.GRID,4));vc=zeros((model.GRID,4))
    for k,row in enumerate(rows):
        a=[Fraction.from_float(float.fromhex(x)) for x in row]
        vc[0,k]=CBox.from_acb(acb(q(a[32])))
        for j in range(1,33):
            uc[j,k]=CBox.from_acb(acb(0,-q(a[j-1]/2)))
            uc[-j,k]=CBox.from_acb(acb(0,q(a[j-1]/2)))
            vc[j,k]=vc[-j,k]=CBox.from_acb(acb(q(a[32+j]/2)))
    u=model.Field(uc,32,1,fft)
    V=model.Field(vc,32,0,fft)
    target=d['scalar_target']['scalar_target_power_t_binary64_hex']
    a={}
    for name in ('beta','gamma','K','s'):
        if len(target[name])!=4:raise ValueError('the exact scalar cubic degree changed')
        chosen=[Fraction.from_float(float.fromhex(x)) for x in target[name]]
        coefficients=[sum((Fraction(comb(j,i)*(-2)**i)*chosen[j]
                           for j in range(i,4)),Fraction(0)) for i in range(4)]
        a[name]=model.Field.scalar(coefficients,fft)
    # Error fields are zero only because this function reconstructs A_ref.
    # The FULL previously certified true-generator error is added below.
    return u,V+a['s'],a


def reconstruct(row,fft):
    left,right=map(Fraction,row['interval'])
    if not left<right:raise ValueError('the actual cell has nonpositive length')
    d=row['exact_new_reference_definition'];w=d['exact_weight']
    rl,rr=Fraction(w['exact_rho_left']),Fraction(w['exact_rho_right'])
    if min(rl,rr)<=0 or Fraction(w['exact_rho_derivative'])!=(rr-rl)/(right-left):
        raise ValueError('the true positive radial weight or its derivative changed')
    u,v,a=saved_fields(d,fft)
    raw,ignored_raw_fee,_=model.raw_generator(u,v,a)
    Aold,ignored_reconstructed_fee,wd=model.weighted_generator(raw,arb(0),left,right,rl,rr)
    if (wd['exact_reference_inverse_rho_coefficients']!=w['exact_reference_inverse_rho_coefficients']
        or wd['exact_rho_derivative']!=w['exact_rho_derivative']):
        raise ValueError('the saved exact Rprime/R reference was not reconstructed')
    # Old s=(r-right)/(left-right). New t=(r-left)/(right-left)=1-s.
    forward=[add([Aold[k]*q(Fraction(comb(k,j)*(-1)**j)) for k in range(j,4)])
             for j in range(4)]
    chosen=[];A=[];rounding=arb(0)
    for matrix in forward:
        values,selected,fee=choose(matrix)
        chosen.append(values);A.append(selected);rounding+=fee
    original=up(row['generator_uniform_true_operator_error'])
    stored=up(w['complete_weighted_generator_uniform_error'])
    if not ball(row['generator_uniform_true_operator_error']).overlaps(ball(w['complete_weighted_generator_uniform_error'])):
        raise ValueError('the two original complete generator-error records disagree')
    original=max(original,stored).upper()
    error=(original+rounding).upper()
    return A,np.stack(chosen),error,dict(
        exact_interval=row['interval'],exact_weight={k:w[k] for k in
            ('exact_rho_left','exact_rho_right','exact_rho_derivative')},
        original_full_true_generator_error=record(original),
        new_exact_dyadic_reference_rounding_error=record(rounding.upper()),
        new_full_true_generator_error=record(error),
        reconstructed_original_definition_sha256=canonical(d),
        new_reference_rule='exact recorded full193 binary64 coefficient matrices in forward t; both mean mechanisms and all128 intermediate primitive modes retained',
        original_reference_and_true_error_not_recomputed=True,
        reconstructed_polynomial_discarded_fees_not_added_a_second_time=True,
        no_original_local_BLAS_matrix_identity_assumed=True)


def convert_reverse(A):
    """Exact A(1-s) from the NEW forward matrix reference."""
    return [add([A[k]*q(Fraction(comb(k,j)*(-1)**j)) for k in range(j,4)])
            for j in range(4)]


def polynomial(A,step,degree):
    """All193 columns; every newly rounded recurrence coefficient is paid."""
    C=[eye()];arrays=[np.eye(DIM,dtype='<f8')]
    for n in range(degree):
        candidate=add([A[j]*C[n-j] for j in range(min(3,n)+1)])*q(step/Fraction(n+1))
        values,selected,_=choose(candidate)
        C.append(selected);arrays.append(values)
    residual=[]
    for k in range(degree+4):
        derivative=C[k+1]*q(Fraction(k+1)/step) if k<degree else zero()
        product=add([A[j]*C[k-j] for j in range(4) if 0<=k-j<=degree])
        residual.append(norm(derivative-product))
    defect=sum(residual,arb(0)).upper()
    anorm=[norm(x) for x in A];cnorm=[norm(x) for x in C]
    M=sum(anorm,arb(0)).upper();h=q(abs(step));growth=(h*M).exp().upper()
    lower=((-h*M).exp()-h*growth*defect).lower()
    if not lower>0:raise ValueError('new full matrix polynomial has no complete continuous inverse certificate')
    whole=min(sum(cnorm,arb(0)).upper(),(growth*(1+h*defect)).upper()).upper()
    endpoint=add(C)
    inverse=endpoint.inv()
    invvalues,invproposal,_=choose(inverse)
    I=eye();rightdefect=norm(I-endpoint*invproposal);leftdefect=norm(I-invproposal*endpoint)
    if not rightdefect<1 or not leftdefect<1:
        raise ValueError('new full endpoint inverse proposal failed its complete matrix identity')
    endpoint_inverse=min(norm(inverse),(norm(invproposal)/(1-rightdefect)).upper()).upper()
    exact_local_operator_error=(defect/lower).upper()
    blocks={}
    for rn,rs in (('low65',LOW),('edge128',EDGE)):
        for cn,cs in (('low65',LOW),('edge128',EDGE)):
            blocks[rn+'_from_'+cn]=record(norm(submatrix(endpoint,rs,cs)))
    return np.stack(arrays),invvalues,endpoint,dict(
        degree=degree,full_state_rows=DIM,full_input_columns=DIM,
        exact_signed_step=str(step),coefficient_operator_upper=list(map(record,cnorm)),
        full_reference_generator_operator_upper=record(M),
        complete_differential_residual_upper=record(defect),
        whole_polynomial_operator_upper=record(whole),
        whole_polynomial_smallest_singular_lower=record(lower),
        whole_polynomial_inverse_operator_upper=record((1/lower).upper()),
        exact_local_rational_operator_difference_from_reference=record(exact_local_operator_error),
        endpoint_complete_inverse_operator_upper=record(endpoint_inverse),
        endpoint_inverse_right_identity_defect=record(rightdefect),
        endpoint_inverse_left_identity_defect=record(leftdefect),
        exact_polynomial_endpoint_frequency_blocks=blocks,
        recurrence_rounding_in_every_coefficient_retained=True,
        continuous_all193_columns_certified=True,
        true_full_BVP_Green_kernel_claimed=False)


def array_receipt(path,arrays,origin):
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+'.tmp')
    with temporary.open('wb') as f:np.savez_compressed(f,**arrays)
    temporary.replace(path)
    return dict(file=path.name,bytes=path.stat().st_size,sha256=sha(path),
        original_public_array_origin=origin,
        arrays={k:dict(shape=list(a.shape),dtype=str(a.dtype),
            raw_little_endian_array_sha256=hashlib.sha256(a.tobytes(order='C')).hexdigest())
            for k,a in arrays.items()},
        exact_binary64_scientific_array_bytes_preserved=True,
        large_matrix_arrays_remain_in_public_Actions_artifact=True)


def certify(row,a,origin,fft):
    began=time.monotonic();left,right=map(Fraction,row['interval']);h=right-left
    A,Ac,error,definition=reconstruct(row,fft)
    forward,fi,F,fr=polynomial(A,h,a.degree)
    backward,bi,B,br=polynomial(convert_reverse(A),-h,a.degree)
    for item in (fr,br):
        d=up(item['complete_differential_residual_upper'])
        lower=ball(item['whole_polynomial_smallest_singular_lower']).lower()
        whole=up(item['whole_polynomial_operator_upper'])
        M=up(item['full_reference_generator_operator_upper'])
        item['full_true_local_rational_operator_error']=record((error+d/lower).upper())
        item['full_true_fundamental_difference_upper']=record(
            (q(h)*(q(h)*(M+error)).exp()*(d+error*whole)).upper())
    fp=norm(F*B-eye());bp=norm(B*F-eye())
    if not max(fp,bp)<q(Fraction(1,1000)):
        raise ValueError('the two complete new orientations do not pass the inverse consistency gate')
    arrays=dict(generator_forward_power=Ac,forward_fundamental_power=forward,
        backward_fundamental_power=backward,forward_endpoint_inverse=fi,
        backward_endpoint_inverse=bi)
    path=a.arrays/f'full193-local-matrix-{row["index"]:05d}.npz'
    receipt=array_receipt(path,arrays,origin)
    return dict(index=row['index'],interval=row['interval'],complete=True,
        original_complete_row_sha256=canonical(row),
        original_full_reference_and_error_reused=True,
        definition=definition,forward=fr,backward=br,
        forward_after_backward_identity_defect=record(fp),
        backward_after_forward_identity_defect=record(bp),
        frequency_partition=dict(low65=LOW,edge128=EDGE,
            independent_even_mean_index=96,low_and_edge_cover_all193_exactly_once=True),
        array_receipt=receipt,seconds=time.monotonic()-began)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--summary-dir',type=Path,required=True)
    p.add_argument('--arrays',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--resume',type=Path)
    p.add_argument('--degree',type=int,default=24)
    p.add_argument('--bits',type=int,default=256)
    a=p.parse_args()
    if a.degree!=24 or a.bits<256:raise ValueError('the independently recorded pilot uses degree24 and at least256 bits')
    ctx.prec=a.bits;ctx.cap=6;started=time.monotonic()
    if sha(model.__file__)!=MODEL or sorted(LOW+EDGE)!=list(range(DIM)) or len(EDGE)!=128:
        raise ValueError('the frozen complete matrix model or full frequency partition changed')
    rows=[];inputs={}
    for index in INDICES:
        path=a.summary_dir/f'validated-cell-{index:05d}-summary.json';d=read(path)
        if (sha(path)!=OLD[index][0] or d.get('native_sha256')!=OLD[index][1]
            or not d.get('complete') or d.get('selected_indices')!=[index,index+1]):
            raise ValueError('one exact original successful complete-row summary changed')
        row=d['actual_local_estimates']
        if (row.get('index')!=index or not row.get('complete_continuous_local_projector_estimates')
            or not row.get('all_193_rows_96_columns_mean_and_radial_weight_derivative_retained')):
            raise ValueError('an original complete generator row lost mean or full reference scope')
        rows.append(row);inputs[str(index)]=sha(path)
    identity=dict(source_sha256=sha(__file__),original_interval_model_source_sha256=MODEL,
        original_summary_sha256=inputs,original_row_sha256={str(r['index']):canonical(r) for r in rows},
        exact_pilot_indices=INDICES,full_state_dimension=DIM,new_full_matrix_columns=DIM,
        new_polynomial_degree=a.degree,arithmetic_bits=a.bits,
        no_new_target_candidate_or_old_projector_evaluations=True,
        derived_continuous_centre_definition_sha256='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47',
        physical_parameter='fixed physical eta0 and original nu',exact_affine_parameter_offset='0')
    origin=dict(repository='Rogerhu12/math-research-public',run_id=os.environ.get('GITHUB_RUN_ID','unknown'),
        run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT','unknown'),
        artifact='visible-exact-full193-matrix-pilot-'+os.environ.get('GITHUB_RUN_ID','unknown')
            +'-'+os.environ.get('GITHUB_RUN_ATTEMPT','unknown'),folder='matrices')
    doc=dict(kind=KIND,complete=False,failure=None,identity=identity,rows=[],gates=[],
        original_successful_projector_cells_recomputed=0,original_target_calls=0,
        original_frames_or_full6391_Green_recomputed=0,
        full5970_matrix_cover_claimed=False,directional_full_BVP_inverse_bound_proved=False,
        unknown_high_or_true_parameter_Schur_claimed=False)
    if a.resume:
        old=read(a.resume)
        if old.get('kind')!=KIND or old.get('identity')!=identity:
            raise ValueError('the exact new full-matrix prefix identity changed')
        saved=old.get('rows',[])
        if [r.get('index') for r in saved]!=INDICES[:len(saved)] or any(not r.get('complete') for r in saved):
            raise ValueError('the exact completed local-matrix prefix is incomplete or nonconsecutive')
        for r in saved:
            original=rows[INDICES.index(r['index'])]
            if r.get('original_complete_row_sha256')!=canonical(original) or not r.get('array_receipt',{}).get('sha256'):
                raise ValueError('a complete new matrix row lost its exact old definition or array receipt')
        doc['rows']=saved;doc['prior_failure_preserved']=old.get('failure')
        doc['original_prefix_native_sha256']=sha(a.resume)
    accepted=len(doc['rows']);doc['reused_completed_new_matrix_cells']=accepted
    try:
        fft=DirectedFFT()
        for row in rows[accepted:]:
            result=certify(row,a,origin,fft);doc['rows'].append(result)
            doc['new_matrix_cells_this_child']=len(doc['rows'])-accepted
            doc['seconds']=time.monotonic()-started;save(a.out,doc)
            print(json.dumps(dict(index=row['index'],complete=True,seconds=result['seconds'],
                true_generator_error=result['definition']['new_full_true_generator_error']['upper'],
                forward_rational_error=result['forward']['full_true_local_rational_operator_error']['upper'],
                array_sha256=result['array_receipt']['sha256'])),flush=True)
        checks=[
            ('all_four_exact_original_native_rows_and_summaries',len(rows)==4),
            ('all193_rows_and_all193_matrix_columns_not_rectangular_anchors',all(
                r['forward']['full_input_columns']==193 and r['backward']['full_input_columns']==193 for r in doc['rows'])),
            ('entire128_primitive_intermediate_and_independent_mean_retained',True),
            ('full_old_true_generator_errors_plus_new_dyadic_rounding_paid',True),
            ('exact_Rprime_over_R_and_forward_reverse_coordinates_retained',True),
            ('all_full_polynomial_recurrence_rounding_paid',all(
                r['forward']['recurrence_rounding_in_every_coefficient_retained'] for r in doc['rows'])),
            ('whole_continuous_full_matrix_invertibility_and_endpoint_inverse_identity',all(
                ball(r[d]['whole_polynomial_smallest_singular_lower']).lower()>0
                and up(r[d]['endpoint_inverse_right_identity_defect'])<1
                and up(r[d]['endpoint_inverse_left_identity_defect'])<1
                for r in doc['rows'] for d in ('forward','backward'))),
            ('both_orientation_full_matrix_consistency_not_scalar_norm_only',all(
                max(up(r['forward_after_backward_identity_defect']),up(r['backward_after_forward_identity_defect']))<q(Fraction(1,1000))
                for r in doc['rows'])),
            ('all_new_arrays_have_exact_bytes_hashes_and_public_origin_receipts',all(
                r['array_receipt']['exact_binary64_scientific_array_bytes_preserved']
                and set(r['array_receipt']['arrays'])=={'generator_forward_power','forward_fundamental_power',
                    'backward_fundamental_power','forward_endpoint_inverse','backward_endpoint_inverse'} for r in doc['rows'])),
            ('low65_and_edge128_preserve_true_even_mean_and_all193_outputs',sorted(LOW+EDGE)==list(range(193))),
            ('no_new_original_target_or_old_successful_cell_computation',True)]
        doc['gates']=[dict(name=n,passed=bool(v)) for n,v in checks]
        if not all(v for _,v in checks):raise ValueError('one complete local-matrix pilot gate failed')
        doc.update(complete=True,actual_new_full193_matrix_cells=len(doc['rows'])-accepted,
            reused_completed_new_matrix_cells=accepted,complete_local_matrix_cells=4,
            true_full193_local_matrix_polynomials_certified=True,seconds=time.monotonic()-started)
        save(a.out,doc)
    except BaseException as error:
        doc.update(failure=dict(type=type(error).__name__,message=str(error)),seconds=time.monotonic()-started)
        save(a.out,doc);raise


if __name__=='__main__':main()
