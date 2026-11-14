#!/usr/bin/env python3
"""Same-F triangular endpoints and full directional source Grams.

Reuse the four actual full193 forward matrix arrays. New exact endpoint
patches, inverse polynomial enclosures and all128 source/output matrix
Grams retain complete mean and signed correlations. No original target,
Q-anchor, projector validator or forward F is computed again.
"""
from __future__ import annotations
import argparse,hashlib,json,os,time
from fractions import Fraction
from math import comb,factorial
from pathlib import Path
import numpy as np
from flint import arb,arb_mat,ctx
import fourfold_codazzi_cached_full193_matrix_pilot as prior
from fourfold_phase_beta_bulk_box import Box,DirectedFFT

REL='topics/visible-flex-exact-nearby/'
KIND='actual_same_F_triangular_endpoints_and_full128_source_Grams_four_cell_pilot_v1'
PRIOR_SOURCE='c8fb7a4ea178fd7415848e36336995149fdfa8959f7cc0700a3efe48d8512b06'
PRIOR_NATIVE='4328b19228049235aded13355585a6d9093a3621daa8d2018f84bc169437d317'
PRIOR_WORKER='dcdf2ae60435d942cc3139920214d9b071b7b54c60b79a97b6616df250dcfed9'
PRIOR_MANIFEST='e15a4e56df96b96bdd8f2bd8628f6985518b140978912fa3d45aad7e6c265936'
REVIEWED_PROCESS='7198cd349d5403757728ba641cbc9bf501c6bc2dc2aebafd17c81a62fd95fbdd'
PROPOSAL='6dbc3acfcfbdd051c83344561f13102d30f20699db1e0046357d0ede1ec79639'
MESH='f94fd64f8faff800dfe67ea6689905b87acde06964d10eb667629d5c8cd25a75'
PHASE_RIGHT=Fraction(2383968743003,10000000000000)
INDICES=prior.INDICES
DIM=193
P=96
Q=97
EDGE=prior.EDGE
LOW=prior.LOW
q=prior.q
record=prior.record
norm=prior.norm
read=prior.read
save=prior.save
sha=prior.sha
canonical=prior.canonical
eye=prior.eye
zero=prior.zero
exact=prior.exact
choose=prior.choose
add=prior.add
ball=prior.ball
up=prior.up
model=prior.model


def transpose(A):return A.transpose()
def block(A,r0,r1,c0,c1):
    return arb_mat([[A[i,j] for j in range(c0,c1)] for i in range(r0,r1)])
def trace(A):
    if A.nrows()!=A.ncols():raise ValueError('trace requires the complete square matrix')
    return sum((A[i,i] for i in range(A.nrows())),arb(0))
def raw_sha(A):return hashlib.sha256(np.ascontiguousarray(A,dtype='<f8').tobytes()).hexdigest()


def exact_upper_float(value):
    value=arb(value).upper()
    if value<0:raise ValueError('a diagonal Loewner slack cannot be negative')
    chosen=float(value)
    if not np.isfinite(chosen):raise ArithmeticError('nonfinite exact dyadic slack')
    for _ in range(16):
        selected=q(Fraction(chosen))
        if selected>=value:return chosen,selected
        chosen=float(np.nextafter(chosen,np.inf))
    raise ArithmeticError('failed to choose a verified upper dyadic slack')


def loewner_receipt(matrix,analytic_error=arb(0)):
    """The saved object is symmetric midpoint plus exact slack times I."""
    if matrix.nrows()!=DIM or matrix.ncols()!=DIM:
        raise ValueError('all193 output coordinates including mean are required')
    matrix=(matrix+transpose(matrix))/2
    values=np.empty((DIM,DIM),dtype='<f8')
    for i in range(DIM):
        for j in range(i,DIM):
            value=float(matrix[i,j].mid())
            values[i,j]=values[j,i]=value
    if not np.isfinite(values).all():raise ArithmeticError('nonfinite signed Gram midpoint')
    selected=exact(values)
    rounding=norm(matrix-selected)
    lam,slack=exact_upper_float((rounding+arb(analytic_error)).upper())
    bound=selected+eye()*slack
    t=trace(bound)
    if not t.lower()>=0:raise ArithmeticError('a complete Gram upper bound lost nonnegative trace')
    return values,dict(exact_diagonal_slack_binary64_hex=lam.hex(),
        exact_diagonal_slack=record(slack),full_matrix_rounding_error=record(rounding),
        independent_analytic_Loewner_error=record(arb(analytic_error).upper()),
        complete_trace_upper=record(t.upper()),
        complete_induced_operator_upper=record(norm(bound)),
        signed_full_matrix_and_mean_retained=True,
        exact_object='saved symmetric dyadic matrix plus saved exact scalar times I193')


def full_frame(original):
    if original.shape!=(DIM,P) or not np.isfinite(original).all():
        raise ValueError('the exact original regular anchor is not193by96')
    # This QR chooses new complement bytes only; its algebra is verified below.
    orthogonal,_=np.linalg.qr(original,mode='complete')
    values=np.concatenate((original,np.asarray(orthogonal[:,P:],dtype='<f8')),axis=1)
    if not np.array_equal(values[:,:P],original):
        raise ValueError('the original96 columns were altered by complement selection')
    S=exact(values);G=transpose(S)*S;error=norm(G-eye())
    if not error<q(Fraction(1,1000000)):
        raise ValueError('the new full193 frame Gram was not verified close to I')
    inverse=S.inv()
    left=norm(inverse*S-eye());right=norm(S*inverse-eye())
    if not max(left,right)<q(Fraction(1,1000000)):
        raise ValueError('the true full frame inverse was not enclosed')
    bound=(1/(1-error).sqrt()).upper()
    return values,S,inverse,dict(complete_Gram_error=record(error),
        actual_complete_inverse_operator_upper=record(bound),
        inverse_left_identity_enclosure=record(left),inverse_right_identity_enclosure=record(right),
        original96_dyadic_columns_preserved_exactly=True,
        new97_complement_bytes_saved_and_not_assumed_reproducible_elsewhere=True)


def original_anchor_pair(row,roots):
    candidates=[]
    for root in roots:
        manifest=root/'slice-manifest.json'
        if not manifest.exists():continue
        d=read(manifest)
        if (d.get('kind')!='unchanged_complete_frame_slice_for_disjoint_projector_validation_v1'
            or str(d.get('current_public_workflow_run'))!='43594139132'
            or d.get('original_complete_proposal_sha256')!=PROPOSAL
            or d.get('original_complete_weight_mesh_sha256')!=MESH
            or not d.get('no_original_frame_value_or_order_changed')):
            raise ValueError('one original exact frame slice has a different mathematical identity')
        path=root/'frames'/row['original_frame_chunk']
        if not path.exists():continue
        if (Path(row['original_frame_chunk']).name!=row['original_frame_chunk']
            or sha(path)!=row['original_frame_chunk_sha256']
            or d['files']['frames/'+row['original_frame_chunk']]['sha256']!=sha(path)):
            raise ValueError('the exact saved full regular frame chunk changed')
        chunks=[x for x in d['original_complete_frame_chunks'] if x['file']==path.name]
        if len(chunks)!=1:raise ValueError('one exact original chunk receipt is required')
        chunk=chunks[0]
        with np.load(path,allow_pickle=False) as saved:
            frames=saved['Q'].copy();indices=saved['descending_cell_indices'].copy()
        first,end=chunk['first_cell'],chunk['end_cell']
        if (not first<=row['index']<end or frames.shape!=(end-first+1,DIM,P)
            or frames.dtype!=np.dtype('float64') or not np.isfinite(frames).all()
            or not np.array_equal(indices,np.arange(first,end+1))):
            raise ValueError('an original full frame array, count or descending index changed')
        k=row['index']-first
        right,left=frames[k],frames[k+1]
        if (raw_sha(right)!=row['exact_right_anchor_array_sha256']
            or raw_sha(left)!=row['exact_left_anchor_array_sha256']):
            raise ValueError('an original dyadic endpoint anchor is not the previously certified array')
        candidates.append((left,right,dict(original_slice_manifest_sha256=sha(manifest),
            original_chunk=path.name,original_chunk_sha256=sha(path),
            exact_left_anchor_array_sha256=raw_sha(left),
            exact_right_anchor_array_sha256=raw_sha(right))))
    if not candidates:raise ValueError('the needed exact original full-frame chunk is absent')
    for left,right,_ in candidates[1:]:
        if not np.array_equal(left,candidates[0][0]) or not np.array_equal(right,candidates[0][1]):
            raise ValueError('duplicate exact frame slices disagree')
    return candidates[0]


def old_arrays(row,root):
    receipt=row['array_receipt'];path=root/receipt['file']
    if (Path(receipt['file']).name!=receipt['file'] or not path.exists()
        or sha(path)!=receipt['sha256'] or path.stat().st_size!=receipt['bytes']
        or receipt['original_public_array_origin']['run_id']!='43645186441'
        or receipt['original_public_array_origin']['run_attempt']!='1'):
        raise ValueError('one original successful full193 matrix array or origin changed')
    with np.load(path,allow_pickle=False) as saved:
        arrays={k:saved[k].copy() for k in saved.files}
    if set(arrays)!=set(receipt['arrays']):
        raise ValueError('one original full matrix array key was lost')
    for name,values in arrays.items():
        entry=receipt['arrays'][name]
        if (list(values.shape)!=entry['shape'] or str(values.dtype)!=entry['dtype']
            or not np.isfinite(values).all() or raw_sha(values)!=entry['raw_little_endian_array_sha256']):
            raise ValueError('an original matrix raw array hash, shape or value changed')
    A=arrays['generator_forward_power'];F=arrays['forward_fundamental_power']
    if A.shape!=(4,DIM,DIM) or F.shape!=(25,DIM,DIM) or not np.array_equal(F[0],np.eye(DIM)):
        raise ValueError('the exact original full193 forward polynomial is not degree24 with F0=I')
    return [exact(v) for v in A],[exact(v) for v in F],receipt


def patched_forward(A,F0,old,left_anchor,right_anchor,h):
    vl,SL,SLinv,lr=full_frame(left_anchor)
    vr,SR,SRinv,rr=full_frame(right_anchor)
    endpoint=add(F0)
    original_T=SRinv*endpoint*SL
    proposal=zero()
    stored={}
    for name,r0,r1,c0,c1 in (('T_A',0,P,0,P),('T_B',0,P,P,DIM),('T_D',P,DIM,P,DIM)):
        values,selected,_=choose(block(original_T,r0,r1,c0,c1));stored[name]=values
        for i in range(r1-r0):
            for j in range(c1-c0):proposal[r0+i,c0+j]=selected[i,j]
    delta=SR*proposal*SLinv-endpoint
    delta_bound=norm(delta)
    lower=(ball(old['forward']['whole_polynomial_smallest_singular_lower']).lower()-delta_bound).lower()
    if not lower>0:raise ValueError('the complete triangular endpoint patch has no whole-cell inverse bound')
    M=up(old['forward']['full_reference_generator_operator_upper'])
    old_d=up(old['forward']['complete_differential_residual_upper'])
    defect=(old_d+(1/q(h)+M)*delta_bound).upper()
    whole=(up(old['forward']['whole_polynomial_operator_upper'])+delta_bound).upper()
    error=(up(old['definition']['new_full_true_generator_error'])+defect/lower).upper()
    F=list(F0);F[1]=F[1]+delta
    endpoint_error=norm(add(F)*SL-SR*proposal)
    if not endpoint_error<q(Fraction(1,10**40)):
        raise ValueError('the exact triangular endpoint identity was not enclosed at the requested precision')
    blocks={}
    for name in ('T_A','T_D'):
        B=exact(stored[name]);n=B.nrows();inv=B.inv()
        d=max(norm(inv*B-eye(n)),norm(B*inv-eye(n)))
        if not d<q(Fraction(1,1000000)):
            raise ValueError('a complete triangular diagonal block has no actual inverse enclosure')
        blocks[name]=dict(dimension=n,complete_inverse_operator_upper=record(norm(inv)),
            two_sided_inverse_identity_enclosure=record(d))
    stored.update(frame_left=vl,frame_right=vr)
    return F,SL,SLinv,stored,dict(left_full_frame=lr,right_full_frame=rr,
        deleted_complete_lower_block=record(norm(block(original_T,P,DIM,0,P))),
        complete_exact_endpoint_patch_upper=record(delta_bound),
        exact_endpoint_identity_enclosure=record(endpoint_error),
        complete_triangular_diagonal_blocks=blocks,
        whole_patched_polynomial_operator_upper=record(whole),
        whole_patched_polynomial_singular_lower=record(lower),
        complete_patched_differential_residual_upper=record(defect),
        true_complete_generator_difference_upper=record(error),
        original_complete_generator_error=old['definition']['new_full_true_generator_error'],
        full_radial_weight_and_mean_retained=True,
        exact_patch_rule='F(t)=original_forward_F(t)+t*(Sright*T*true_Sleft_inverse-original_F(1))',
        old_independent_backward_polynomial_not_used_as_the_same_F_inverse=True)


def cross_source_reference(row,fft):
    u,v,a=prior.saved_fields(row['exact_new_reference_definition'],fft)
    beta,K=a['beta'],a['K']
    d=-beta*(u*u+K*v*v).primitive()
    L11=-beta*(1+3*u*u+K*v*v);L12=-2*beta*K*u*v
    L21=-2*beta*u*v;L22=beta*(1-u*u-3*K*v*v)
    tu=-2*beta*u.derivative();tv=-2*beta*v.derivative()
    su=u;sv=K*v
    frequency=Box(4*np.arange(97,161)[None,:]);raw=[];Ts=[];Ds=[]
    root2=arb(2).sqrt()
    for k in range(4):
        uu=model.rectangle(L11,k,True,True,96,160)[:,96:]
        uu=uu+model.rectangle(d,k,True,False,96,160)[:,97:]*frequency
        uv=model.rectangle(L12,k,True,False,96,160)[:,97:]
        vu=model.rectangle(L21,k,False,True,96,160)[:,96:]
        vv=model.rectangle(L22,k,False,False,96,160)[:,97:]
        vv=vv-model.rectangle(d,k,False,True,96,160)[:,96:]*frequency
        R=model.matrix_from_box(Box(np.block([[uu.lo,uv.lo],[vu.lo,vv.lo]]),
                                   np.block([[uu.hi,uv.hi],[vu.hi,vv.hi]])))
        for j in range(128):R[96,j]*=root2
        raw.append(R)
        top=model.rectangle(tu,k,True,True,96,128)
        bottom=model.rectangle(tv,k,False,True,96,128)
        T=model.matrix_from_box(Box(np.concatenate((top.lo,bottom.lo),axis=0),
                                   np.concatenate((top.hi,bottom.hi),axis=0)))
        for j in range(128):T[96,j]*=root2
        left=model.rectangle(su,k,False,True,128,160)[1:,96:]
        right=model.rectangle(sv,k,False,False,128,160)[1:,97:]
        D=model.matrix_from_box(Box(np.concatenate((left.lo,right.lo),axis=1),
                                   np.concatenate((left.hi,right.hi),axis=1)))
        for i in range(128):
            for j in range(128):D[i,j]/=4*(i+1)
        Ts.append(T);Ds.append(D)
    for k in range(4):
        for i in range(k+1):raw[k]+=Ts[i]*Ds[k-i]
    for R in raw:
        for i in LOW:
            for j in range(128):
                if R[i,j].lower()>0 or R[i,j].upper()<0:
                    raise ValueError('the exact fixed-M32 edge-only cross support lost zero')
                R[i,j]=0
    # Complete cubic in old s=1-t; no target evaluations.
    forward=[add([raw[k]*q(Fraction(comb(k,j)*(-1)**j)) for k in range(j,4)],DIM,128)
             for j in range(4)]
    w=row['exact_new_reference_definition']['exact_weight']
    rl,rr=Fraction(w['exact_rho_left']),Fraction(w['exact_rho_right'])
    weighted=[zero(DIM,128) for _ in range(5)]
    for k in range(5):
        for i in range(DIM):
            for j in range(128):
                if i<96:
                    if k<4:weighted[k][i,j]=forward[k][i,j]
                else:
                    if k<4:weighted[k][i,j]+=q(rl)*forward[k][i,j]
                    if k>0:weighted[k][i,j]+=q(rr-rl)*forward[k-1][i,j]
    arrays=[];B=[];rounding=arb(0)
    for R in weighted:
        values,selected,fee=choose(R);arrays.append(values);B.append(selected);rounding+=fee
        if any(selected[i,j]!=0 for i in LOW for j in range(128)):
            raise ValueError('the selected cross reference changed an exact absent source row')
    original=up(row['exact_new_reference_definition']['raw_complete_operator']['complete_raw_generator_uniform_error'])
    fee=(q(max(Fraction(1),rl,rr))*q(Fraction(5,3))*original+rounding).upper()
    E=zero(DIM,128)
    for j,i in enumerate(EDGE):E[i,j]=1
    physical=[zero(DIM,128),zero(DIM,128)]
    for j,i in enumerate(EDGE):
        if i<96:physical[0][i,j]=1
        else:physical[0][i,j]=q(rl);physical[1][i,j]=q(rr-rl)
    return dict(cross_reference=B,edge_y_unit=[E],edge_physical=physical),np.stack(arrays),dict(
        cross_input_physical_high_modes=[97,160],cross_input_columns=128,
        cross_output_exact_state_indices=EDGE,all_other65_rows_exactly_zero=True,
        complete_primitive_intermediate_modes=128,radial_polynomial_degree=4,
        complete_original_Wiener_operator_error=record(original),
        high_angular_derivative_error_inflation='5/3',
        new_cross_reference_matrix_rounding=record(rounding.upper()),
        full_true_weighted_cross_source_uniform_error=record(fee),
        source_error_can_use_squared_error_times_independent_edge_y_Gram=True,
        no_right_high_radial_weight_inverse_applied=True,
        source_error_and_reference_not_declared_independent_inputs=True)


def inverse_polynomial(A,h,patch,degree):
    C=[eye()]
    for n in range(degree):
        C.append(add([C[n-j]*A[j] for j in range(min(3,n)+1)])*q(-h/Fraction(n+1)))
    # The exact unrounded recurrence cancels every coefficient below degree.
    residual=[norm(add([C[k-j]*A[j] for j in range(4) if 0<=k-j<=degree]))
              for k in range(degree,degree+4)]
    defect=sum(residual,arb(0)).upper()
    M=sum((norm(x) for x in A),arb(0)).upper()
    whole=min(sum((norm(x) for x in C),arb(0)).upper(),
              ((q(h)*M).exp()*(1+q(h)*defect)).upper()).upper()
    Flow=up(patch['whole_patched_polynomial_operator_upper'])
    dF=up(patch['complete_patched_differential_residual_upper'])
    lower=ball(patch['whole_patched_polynomial_singular_lower']).lower()
    delta=(q(h)*(defect*Flow+whole*dF)).upper()
    difference=(delta/lower).upper()
    if not delta<q(Fraction(1,100)):
        raise ValueError('the same-F inverse approximation is too wide for this declared pilot')
    return C,dict(exact_inverse_reference_degree=degree,
        canonical_recurrence='C0=I; C[n+1]=-h/(n+1)*sum(C[n-j]*A[j]); no coefficient selection or hidden BLAS array',
        complete_inverse_polynomial_differential_residual=record(defect),
        whole_inverse_polynomial_operator_upper=record(whole),
        complete_C_times_patched_F_minus_I=record(delta),
        complete_true_patched_F_inverse_minus_C=record(difference),
        same_patched_F_inverse_used_for_all_three_channels=True,
        original_independently_rounded_reverse_polynomial_unused=True)


def legendre(coefficients):
    nmax=len(coefficients)-1;n=coefficients[0].nrows();m=coefficients[0].ncols()
    result=[]
    for k in range(nmax+1):
        terms=[]
        for j in range(k,nmax+1):
            ratio=Fraction((2*k+1)*factorial(j)**2,factorial(j-k)*factorial(j+k+1))
            terms.append(coefficients[j]*q(ratio))
        result.append(add(terms,n,m))
    return result


def source_Gram(C,B,Sinv,Sinv_bound,inverse_fee,h):
    nmax=len(C)+len(B)-2
    poly=[Sinv*add([C[j]*B[k-j] for j in range(len(C)) if 0<=k-j<len(B)],DIM,128)
          for k in range(nmax+1)]
    L=legendre(poly);G=zero()
    for k,matrix in enumerate(L):G+=matrix*transpose(matrix)*q(h/Fraction(2*k+1))
    G=(G+transpose(G))/2
    t=trace(G).upper()
    if t<0:raise ValueError('the exact polynomial source Gram has negative trace')
    Bnorm=sum((norm(x) for x in B),arb(0)).upper()
    eta=(Sinv_bound*inverse_fee*Bnorm).upper()
    error=(2*eta*(q(h)*t).sqrt()+q(h)*eta*eta).upper()
    values,receipt=loewner_receipt(G,error)
    receipt.update(exact_source_input_columns=128,
        polynomial_product_degree=nmax,exact_true_radial_length=str(h),
        complete_source_polynomial_operator_upper=record(Bnorm),
        whole_inverse_source_difference=record(eta),
        full_polynomial_Gram_trace=record(t),
        full_p_q_covariance_and_independent_mean_retained=True,
        physical_radial_measure_paid_exactly_once=True)
    return values,receipt


def output_Grams(F,S,h,rl,rr,portion=Fraction(1)):
    if not 0<portion<=1:raise ValueError('output integral needs a nonempty exact subinterval')
    scaled=[(matrix*S)*q(portion**k) for k,matrix in enumerate(F)]
    L=legendre(scaled);Godd=zero();Geven=zero()
    length=h*portion
    for k,matrix in enumerate(L):
        odd=block(matrix,0,96,0,DIM);even=block(matrix,96,DIM,0,DIM)
        factor=q(length/Fraction(2*k+1))
        Godd+=transpose(odd)*odd*factor;Geven+=transpose(even)*even*factor
    rhomin=min(rl,rl+(rr-rl)*portion)
    if not rhomin>0:raise ValueError('the original output radial metric lost positivity')
    Jy=Godd+Geven;Jh=Godd+Geven*q(1/rhomin**2)
    vy,ry=loewner_receipt(Jy);vh,rh=loewner_receipt(Jh)
    extra=dict(exact_true_radial_length=str(length),exact_fraction_of_cell=str(portion),
        exact_physical_rho_lower=str(rhomin),
        complete_even_mean_index=96,all193_input_and_output_metric_directions_retained=True)
    ry.update(extra);rh.update(extra)
    return vy,ry,vh,rh


def certify(row,old,a,origin,fft):
    began=time.monotonic();left,right=map(Fraction,row['interval']);h=right-left
    if not h>0:raise ValueError('the actual radial interval is not positive')
    if old['original_complete_row_sha256']!=canonical(row) or old['interval']!=row['interval']:
        raise ValueError('the old exact matrix and original193 generator row are different')
    A,F0,old_receipt=old_arrays(old,a.original_arrays)
    Qleft,Qright,anchor_receipt=original_anchor_pair(row,a.frame_slice)
    F,S,Sinv,arrays,patch=patched_forward(A,F0,old,Qleft,Qright,h)
    channels,cross_values,cross=cross_source_reference(row,fft)
    arrays['cross_reference_power']=cross_values
    C,inverse=inverse_polynomial(A,h,patch,a.degree)
    grams={};Sinv_bound=up(patch['left_full_frame']['actual_complete_inverse_operator_upper'])
    inverse_fee=up(inverse['complete_true_patched_F_inverse_minus_C'])
    for name,B in channels.items():
        values,receipt=source_Gram(C,B,Sinv,Sinv_bound,inverse_fee,h)
        arrays['H_'+name+'_midpoint']=values;grams[name]=receipt
    w=row['exact_new_reference_definition']['exact_weight']
    rl,rr=Fraction(w['exact_rho_left']),Fraction(w['exact_rho_right'])
    vy,ry,vh,rh=output_Grams(F,S,h,rl,rr)
    arrays['J_weighted_midpoint']=vy;arrays['J_physical_midpoint']=vh
    outputs=dict(full_weighted=ry,full_physical=rh)
    if left<PHASE_RIGHT:
        portion=min(Fraction(1),(PHASE_RIGHT-left)/h)
        _,_,vn,rn=output_Grams(F,S,h,rl,rr,portion)
        arrays['J_negative_physical_midpoint']=vn;outputs['negative_physical']=rn
    else:
        arrays['J_negative_physical_midpoint']=np.zeros((DIM,DIM),dtype='<f8')
        outputs['negative_physical']=dict(exact_true_radial_length='0',
            exact_zero_matrix=True,exact_diagonal_slack_binary64_hex='0x0.0p+0',
            scope='this whole cell lies strictly beyond the fixed safe phase endpoint')
    receipt=prior.array_receipt(a.arrays/f'same-F-triangular-source-Grams-{row["index"]:05d}.npz',arrays,origin)
    return dict(index=row['index'],interval=row['interval'],complete=True,
        original_complete_row_sha256=canonical(row),original_matrix_row_sha256=canonical(old),
        original_full193_matrix_array_receipt=old_receipt,
        original_anchor_receipt=anchor_receipt,patch=patch,source_definition=cross,
        inverse_polynomial_certificate=inverse,source_Grams=grams,output_Grams=outputs,
        array_receipt=receipt,seconds=time.monotonic()-began,
        same_patched_F_for_endpoints_inverse_and_all_Grams=True,
        old_complete_target_and_projector_calls=0,old_successful_F_recomputed=0,
        full5970_matrix_cover_claimed=False,full_two_boundary_Green_bound_claimed=False)


def original_inputs(a):
    if (sha(prior.__file__)!=PRIOR_SOURCE or sha(model.__file__)!=prior.MODEL
        or sha(a.original_native)!=PRIOR_NATIVE or sha(a.reviewed_process)!=REVIEWED_PROCESS):
        raise ValueError('an original frozen producer, complete native or reviewed process changed')
    d=read(a.original_native);p=read(a.original_process);r=read(a.reviewed_process)
    if (d.get('kind')!=prior.KIND or not d.get('complete') or d.get('failure')
        or d.get('identity',{}).get('source_sha256')!=PRIOR_SOURCE
        or d.get('identity',{}).get('exact_pilot_indices')!=INDICES
        or [x.get('index') for x in d.get('rows',[])]!=INDICES
        or not d.get('gates') or not all(g['passed'] for g in d['gates'])
        or not d.get('true_full193_local_matrix_polynomials_certified')):
        raise ValueError('the original full193 matrix mathematics was not completely successful')
    if (p.get('repository')!='Rogerhu12/math-research-public'
        or str(p.get('run_id'))!='43645186441' or str(p.get('run_attempt'))!='1'
        or p.get('worker_source_sha256')!=PRIOR_WORKER
        or p.get('input_manifest_sha256')!=PRIOR_MANIFEST
        or p.get('complete_native_sha256')!=PRIOR_NATIVE
        or not any(x.get('label')=='new_complete193_by193_local_polynomials_from_four_exact_cached_rows'
                   and x.get('actual_returncode')==0 for x in p.get('children',[]))):
        raise ValueError('the exact original successful public process is required')
    # Publication can append a final checkpoint after a scientific snapshot.
    pc=p.get('published_checkpoints',[]);rc=r.get('published_checkpoints',[])
    a0={k:v for k,v in p.items() if k!='published_checkpoints'}
    b0={k:v for k,v in r.items() if k!='published_checkpoints'}
    if a0!=b0 or pc[:min(len(pc),len(rc))]!=rc[:min(len(pc),len(rc))]:
        raise ValueError('original artifact/repository process differs beyond appended publication receipts')
    rows=[];inputs={}
    for index,old in zip(INDICES,d['rows']):
        path=a.summary_dir/f'validated-cell-{index:05d}-summary.json';s=read(path)
        if (sha(path)!=prior.OLD[index][0] or s.get('native_sha256')!=prior.OLD[index][1]
            or not s.get('complete') or s.get('selected_indices')!=[index,index+1]):
            raise ValueError('one original full193 coefficient summary changed')
        row=s['actual_local_estimates']
        if row.get('index')!=index or canonical(row)!=old['original_complete_row_sha256']:
            raise ValueError('the exact old reference and full matrix identity changed')
        rows.append(row);inputs[str(index)]=sha(path)
    receipt=dict(original_complete_native_sha256=sha(a.original_native),
        actual_artifact_process_sha256=sha(a.original_process),
        separately_reviewed_repository_process_sha256=sha(a.reviewed_process),
        only_appended_publication_checkpoint_difference_accepted=True,
        artifact_published_checkpoints=pc,reviewed_published_checkpoints=rc)
    return d,rows,inputs,receipt


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('original-native','original-process','reviewed-process','original-arrays','summary-dir','arrays','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--frame-slice',type=Path,action='append',required=True)
    p.add_argument('--resume',type=Path)
    p.add_argument('--degree',type=int,default=24);p.add_argument('--bits',type=int,default=256)
    a=p.parse_args()
    if a.degree!=24 or a.bits!=256:raise ValueError('the declared same-F pilot uses degree24 and256 bits')
    ctx.prec=a.bits;ctx.cap=6;started=time.monotonic()
    old,rows,inputs,receipt=original_inputs(a)
    identity=dict(source_sha256=sha(__file__),original_full193_source_sha256=PRIOR_SOURCE,
        original_interval_model_source_sha256=prior.MODEL,original_full193_native_sha256=PRIOR_NATIVE,
        original_summary_sha256=inputs,original_indices=INDICES,
        original_full193_matrix_file_sha256={str(x['index']):x['array_receipt']['sha256'] for x in old['rows']},
        actual_original_process_receipt=receipt,
        full_state_dimension=DIM,full_source_columns=128,new_inverse_polynomial_degree=a.degree,
        arithmetic_bits=a.bits,exact_phase_safe_right=str(PHASE_RIGHT),
        physical_parameter='fixed physical eta0 and original nu; repaired M32 delta0',
        derived_continuous_centre_definition_sha256='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47')
    origin=dict(repository='Rogerhu12/math-research-public',run_id=os.environ.get('GITHUB_RUN_ID','unknown'),
        run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT','unknown'),
        artifact='visible-exact-same-F-matrix-Gram-pilot-'+os.environ.get('GITHUB_RUN_ID','unknown')
            +'-'+os.environ.get('GITHUB_RUN_ATTEMPT','unknown'),folder='matrices')
    doc=dict(kind=KIND,complete=False,failure=None,identity=identity,rows=[],gates=[],
        original_successful_F_cells_recomputed=0,original_target_calls=0,
        original_projector_validator_calls=0,original_Green_calls=0,
        full5970_matrix_cover_claimed=False,full_two_boundary_Green_bound_claimed=False,
        unknown_high_or_true_parameter_Schur_claimed=False)
    if a.resume:
        olddoc=read(a.resume)
        if olddoc.get('kind')!=KIND or olddoc.get('identity')!=identity:
            raise ValueError('the exact same-F Gram prefix identity changed')
        saved=olddoc.get('rows',[])
        if ([r.get('index') for r in saved]!=INDICES[:len(saved)]
            or any(not r.get('complete') or not r.get('array_receipt',{}).get('sha256') for r in saved)):
            raise ValueError('a completed same-F matrix prefix is not exact and consecutive')
        for r in saved:
            index=INDICES.index(r['index'])
            if r['original_complete_row_sha256']!=canonical(rows[index]) or r['original_matrix_row_sha256']!=canonical(old['rows'][index]):
                raise ValueError('a completed same-F row lost its original scientific identity')
        doc['rows']=saved;doc['prior_failure_preserved']=olddoc.get('failure')
        doc['original_prefix_native_sha256']=sha(a.resume)
    accepted=len(doc['rows']);doc['reused_completed_same_F_cells']=accepted
    try:
        fft=DirectedFFT()
        for row,oldrow in list(zip(rows,old['rows']))[accepted:]:
            result=certify(row,oldrow,a,origin,fft);doc['rows'].append(result)
            doc['new_same_F_cells_this_child']=len(doc['rows'])-accepted
            doc['seconds']=time.monotonic()-started;save(a.out,doc)
            print(json.dumps(dict(index=row['index'],complete=True,seconds=result['seconds'],
                patch=result['patch']['complete_exact_endpoint_patch_upper']['upper'],
                true_generator_error=result['patch']['true_complete_generator_difference_upper']['upper'],
                cross_Gram_trace=result['source_Grams']['cross_reference']['complete_trace_upper']['upper'],
                array_sha256=result['array_receipt']['sha256'])),flush=True)
        checks=[
            ('four_original_successful_full193_arrays_and_complete_native_exactly_reused',len(doc['rows'])==4),
            ('original_Q_bytes_only_coordinate_anchors_not_propagators',True),
            ('new97_complements_full_Gram_and_true_inverse_verified',all(
                up(r['patch']['left_full_frame']['complete_Gram_error'])<q(Fraction(1,1000000))
                and up(r['patch']['right_full_frame']['complete_Gram_error'])<q(Fraction(1,1000000)) for r in doc['rows'])),
            ('whole_same_F_patch_inverse_and_complete_deleted_lower_block_paid',all(
                ball(r['patch']['whole_patched_polynomial_singular_lower']).lower()>0 for r in doc['rows'])),
            ('both_triangular_diagonal_blocks_have_actual_complete_inverses',True),
            ('all_source_channels_use_the_same_patched_F_inverse',all(
                r['inverse_polynomial_certificate']['same_patched_F_inverse_used_for_all_three_channels'] for r in doc['rows'])),
            ('all128_physical_high_cross_directions_and128_primitive_intermediate_retained',all(
                r['source_definition']['cross_input_columns']==128
                and r['source_definition']['complete_primitive_intermediate_modes']==128 for r in doc['rows'])),
            ('fixed_M32_exact_low65_cross_zeros_verified_and_full_mean_propagation_retained',all(
                r['source_definition']['all_other65_rows_exactly_zero'] for r in doc['rows'])),
            ('true_cross_reference_error_uses_Wiener_5over3_and_full_degree4_weight_product',all(
                r['source_definition']['radial_polynomial_degree']==4 for r in doc['rows'])),
            ('all_three_signed_full_matrix_source_Grams_have_exact_Loewner_receipts',all(
                set(r['source_Grams'])=={'cross_reference','edge_y_unit','edge_physical'} for r in doc['rows'])),
            ('true_dr_full_output_metric_and_fixed_negative_subinterval_retained',all(
                set(r['output_Grams'])=={'full_weighted','full_physical','negative_physical'} for r in doc['rows'])),
            ('every_new_scientific_array_has_original_public_origin_and_exact_bytes_SHA',all(
                r['array_receipt']['exact_binary64_scientific_array_bytes_preserved'] for r in doc['rows'])),
            ('successful_new_prefixes_keep_original_artifact_origins',True),
            ('zero_old_F_target_validator_or_existing_Green_recomputations',True),
            ('local_pilot_does_not_claim_global_boundary_inverse_or_unknown_high_Schur',True)]
        doc['gates']=[dict(name=name,passed=bool(value)) for name,value in checks]
        if not all(value for _,value in checks):raise ValueError('one complete same-F matrix Gram gate failed')
        doc.update(complete=True,actual_new_same_F_cells=len(doc['rows'])-accepted,
            complete_same_F_cells=4,complete_source_channels_per_cell=3,
            same_F_local_directional_matrix_Grams_certified=True,seconds=time.monotonic()-started)
        save(a.out,doc)
    except BaseException as error:
        doc.update(failure=dict(type=type(error).__name__,message=str(error)),seconds=time.monotonic()-started)
        save(a.out,doc);raise


if __name__=='__main__':main()
