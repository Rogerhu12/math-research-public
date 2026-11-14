#!/usr/bin/env python3
"""Complete same-F directional matrix data from the exact5970 cached rows.

Four successful same-F cells are immutable inputs. The remaining5966
cells use canonical unrounded exact coefficient recurrences, actual
triangular endpoint patches and full signed source/output Grams.
This is matrix data, not yet a two-boundary directional inverse.
"""
from __future__ import annotations
import argparse,hashlib,json,os,time
from collections import OrderedDict
from fractions import Fraction
from math import comb
from pathlib import Path
import numpy as np
from flint import arb,arb_mat,ctx
import fourfold_codazzi_same_F_triangular_source_Gram_pilot as base
import fourfold_codazzi_regular_cut_complete_CI as oldcover
from fourfold_phase_beta_bulk_box import Box,DirectedFFT

REL='topics/visible-flex-exact-nearby/'
KIND='actual_complete_same_F_directional_matrix_data_from_cached5970_v1'
PLAN_KIND='actual_exact5970_same_F_directional_matrix_disjoint_plan_v1'
PILOT_KIND=base.KIND
BASE_SOURCE='2173281e0558cbbabf3a21d506ae3cf9b0253a9406aa2d9d15b8681e8faeaf44'
PILOT_NATIVE='9a46d9fc76499a17a90a0a153a0c4907415eadcedfd9f50f70fd82d08f9dbc7c'
PILOT_WORKER='98ca04e2a5e0691f9e9f319d16700f8884da6eea27f3eb61eb832d3107b19f38'
PILOT_MANIFEST='a24a9a7fec2f39e349e9f547ea4d5c33f72db10d41e3a77ed7030409161e7ad9'
PILOT_REVIEWED_PROCESS='954d803891494df3176641dfc42275566f9eadec3c93b73c87216afaab01840f'
PROFILE='3460a4b5636bf6a3d9c160f6141ab5153fc5fc705ca79000c5f10370a978cb69'
PROFILE_PROCESS='16608b57571d17a427857bcfe0127186589b3f79e93d89a7e423ac48a2740af9'
OLD_COVER_SOURCE='3d4628235a6d48046ac2e17af75cf70ea7bcadf6d5e6856a327426faebfa84fa'
OLD_COVER_MANIFEST='394379df4a2588ad53a85ed91438874a34f30473a746b85cd8db3e83edfcdbf5'
PROPOSAL=base.PROPOSAL
MESH=base.MESH
DIM=base.DIM
P=base.P
Q=base.Q
EDGE=base.EDGE
LOW=base.LOW
INDICES=base.INDICES
PHASE_RIGHT=base.PHASE_RIGHT
q,record,norm,read,save,sha,canonical=base.q,base.record,base.norm,base.read,base.save,base.sha,base.canonical
eye,zero,exact,choose,add,ball,up=base.eye,base.zero,base.exact,base.choose,base.add,base.ball,base.up
transpose,block,trace,raw_sha=base.transpose,base.block,base.trace,base.raw_sha
model=base.model
DEGREES=(8,12,16,20,24,32,40,48,64)
ORIGINAL_RECURRENCE='X_0=Q_right; X_(n+1)=(left-right)/(n+1) sum_(j=0)^min(3,n) A_j X_(n-j)'


def plan_groups():
    result=[]
    for group,first in enumerate(range(0,5970,192)):
        end=min(first+192,5970)
        selected=[i for i in range(first,end) if i not in INDICES]
        result.append(dict(group=group,slice_id=first//384,first=first,end=end,
            exact_new_indices=selected,reused_pilot_indices=[i for i in INDICES if first<=i<end],
            new_cells=len(selected)))
    return result


def check_sources():
    if (sha(base.__file__)!=BASE_SOURCE or sha(base.prior.__file__)!=base.PRIOR_SOURCE
        or sha(model.__file__)!=base.prior.MODEL or sha(oldcover.__file__)!=OLD_COVER_SOURCE):
        raise ValueError('a frozen exact-reference, same-F or original complete-cover source changed')


def profile_input(path,process):
    if sha(path)!=PROFILE or sha(process)!=PROFILE_PROCESS:
        raise ValueError('the exact original5970 profile or original artifact process changed')
    d,p=read(path),read(process)
    if (d.get('kind')!='actual_complete_5970_local_projector_cover_and_all_interfaces_v1'
        or not d.get('complete') or d.get('failure') or d.get('complete_original_cells')!=5970
        or d.get('consumer_source_sha256')!=OLD_COVER_SOURCE
        or str(d.get('actual_public_run_id'))!='43594139132'
        or d.get('original_complete_proposal_sha256')!=PROPOSAL
        or d.get('exact_interval')!=['0','9/10']
        or len(d.get('rows',[]))!=5970
        or p.get('complete_native_sha256')!=PROFILE
        or p.get('worker_source_sha256')!=OLD_COVER_SOURCE
        or p.get('input_manifest_sha256')!=OLD_COVER_MANIFEST
        or str(p.get('run_id'))!='43594139132'
        or p.get('repository')!='Rogerhu12/math-research-public'
        or not p.get('complete_original_5970_cells_claimed')):
        raise ValueError('the original complete cached geometry or proof scope changed')
    edge=Fraction(9,10);previous=None
    for i,r in enumerate(d['rows']):
        left,right=map(Fraction,r['interval']);w=r['exact_weight']
        if (r.get('index')!=i or right!=edge or not left<right
            or not r.get('complete_reference_definition_retained_in_its_original_native')
            or not r.get('complete_original_row_canonical_json_sha256')
            or min(Fraction(w['exact_rho_left']),Fraction(w['exact_rho_right']))<=0):
            raise ValueError('the original5970 exact ordered cover is incomplete')
        if previous and (previous['exact_left_anchor_array_sha256']!=r['exact_right_anchor_array_sha256']
            or previous['exact_weight']['exact_rho_left']!=w['exact_rho_right']):
            raise ValueError('an original shared endpoint lost the same exact Q or physical R')
        edge=left;previous=r
    if edge!=0:raise ValueError('the complete original matrix domain does not reach the waist')
    return d


def pilot_input(path,process,reviewed,profile):
    if sha(path)!=PILOT_NATIVE or sha(reviewed)!=PILOT_REVIEWED_PROCESS:
        raise ValueError('the exact four successful same-F cells or reviewed process changed')
    d,p,r=read(path),read(process),read(reviewed)
    if (d.get('kind')!=PILOT_KIND or not d.get('complete') or d.get('failure')
        or d.get('identity',{}).get('source_sha256')!=BASE_SOURCE
        or d.get('identity',{}).get('original_indices')!=INDICES
        or not d.get('same_F_local_directional_matrix_Grams_certified')
        or [x.get('index') for x in d.get('rows',[])]!=INDICES
        or len(d.get('gates',[]))!=15 or not all(g['passed'] for g in d['gates'])
        or p.get('repository')!='Rogerhu12/math-research-public'
        or str(p.get('run_id'))!='43648579604' or str(p.get('run_attempt'))!='1'
        or p.get('worker_source_sha256')!=PILOT_WORKER
        or p.get('input_manifest_sha256')!=PILOT_MANIFEST
        or p.get('complete_native_sha256')!=PILOT_NATIVE
        or not any(c.get('label')=='same_forward_F_triangular_endpoints_and_three_complete128_source_Grams'
            and c.get('actual_returncode')==0 for c in p.get('children',[]))):
        raise ValueError('the actual original same-F pilot did not finish scientifically')
    pc,rc=p.get('published_checkpoints',[]),r.get('published_checkpoints',[])
    if ({k:v for k,v in p.items() if k!='published_checkpoints'}
            !={k:v for k,v in r.items() if k!='published_checkpoints'}
        or pc[:min(len(pc),len(rc))]!=rc[:min(len(pc),len(rc))]):
        raise ValueError('the same-F artifact/repository process differs beyond appended receipts')
    for row in d['rows']:
        entry=profile['rows'][row['index']]
        if (row['original_complete_row_sha256']!=entry['complete_original_row_canonical_json_sha256']
            or row['interval']!=entry['interval']):
            raise ValueError('a successful same-F pilot has a different original reference row')
    return d,dict(actual_artifact_process_sha256=sha(process),
        reviewed_repository_process_sha256=sha(reviewed),
        only_appended_publication_checkpoints_accepted=True)


def validate_plan(path,profile):
    d=read(path)
    if (d.get('kind')!=PLAN_KIND or not d.get('complete') or d.get('failure')
        or d.get('source_sha256')!=sha(__file__) or d.get('original_profile_sha256')!=PROFILE
        or d.get('original_pilot_native_sha256')!=PILOT_NATIVE
        or d.get('groups')!=plan_groups() or d.get('new_local_cells')!=5966
        or d.get('reused_complete_pilot_cells')!=4
        or d.get('original_all5970_row_sha256')!=[r['complete_original_row_canonical_json_sha256'] for r in profile['rows']]
        or not d.get('gates') or not all(g['passed'] for g in d['gates'])):
        raise ValueError('the immutable disjoint matrix plan changed or failed')
    return d


def plan_run(a):
    profile=profile_input(a.profile,a.profile_process)
    pilot,receipt=pilot_input(a.pilot,a.pilot_process,a.reviewed_pilot_process,profile)
    groups=plan_groups()
    if sorted([i for g in groups for i in g['exact_new_indices']]+INDICES)!=list(range(5970)):
        raise ValueError('the disjoint full matrix plan lost or repeated an original cell')
    d=dict(kind=PLAN_KIND,complete=True,failure=None,source_sha256=sha(__file__),
        original_profile_sha256=PROFILE,original_profile_process_sha256=sha(a.profile_process),
        original_pilot_native_sha256=PILOT_NATIVE,original_pilot_process_receipt=receipt,
        original_all5970_row_sha256=[r['complete_original_row_canonical_json_sha256'] for r in profile['rows']],
        groups=groups,new_local_cells=5966,reused_complete_pilot_cells=4,
        old_target_validator_Q_and_successful_matrix_recomputations=0,
        exact_domain=['0','9/10'],exact_fixed_phase_right=str(PHASE_RIGHT),
        all_shared_original_Q_and_R_endpoints_verified=True,
        old_successful_pilot_rows=pilot['rows'],
        old_successful_pilot_rows_kept_verbatim=True,
        gates=[dict(name=x,passed=True) for x in (
            'exact_original5970_profile_artifact_process_and_full_ordered_cover',
            'all_shared_original_Q_bytes_and_physical_R_endpoint_weights_are_identical',
            'four_actual_successful_same_F_cells_and15_original_gates_reused_verbatim',
            'only_publication_receipt_append_difference_allowed_in_original_pilot_process',
            'all32_disjoint_groups_cover_exactly5966_missing_cells',
            'original_target_validator_and_four_F_Gram_cells_not_reexecuted',
            'local_matrix_data_do_not_claim_the_full_directional_boundary_inverse')])
    save(a.out,d)


def range_rows(a,profile,plan):
    item=plan['groups'][a.group]
    root=a.reference_artifact
    pp=root/'process.json';p=read(pp)
    if (p.get('repository')!='Rogerhu12/math-research-public' or str(p.get('run_id'))!='43594139132'
        or p.get('worker_source_sha256')!=OLD_COVER_SOURCE
        or p.get('input_manifest_sha256')!=OLD_COVER_MANIFEST or p.get('phase')!='range'
        or p.get('slice_id')!=item['slice_id']
        or p.get('disjoint_plan')!=oldcover.plan()[item['slice_id']]
        or not p.get('assigned_original_ranges_complete')
        or not p.get('children') or not all(c.get('actual_returncode')==0 for c in p['children'])):
        raise ValueError('the exact original successful reference range process changed')
    supplied={};receipts=[]
    for first,end in oldcover.plan()[item['slice_id']]['new_ranges']:
        path=root/f'native/validated-cells-{first:05d}-{end:05d}.json.gz'
        original=[r for r in profile['inputs'] if r.get('selected_indices')==[first,end]]
        if len(original)!=1 or sha(path)!=original[0]['sha256']:
            raise ValueError('one original full-reference native differs from the certified complete cover')
        d=oldcover.validated(path,first,end)
        for row in d['rows']:
            r=profile['rows'][row['index']]
            if canonical(row)!=r['complete_original_row_canonical_json_sha256']:
                raise ValueError('one exact193 reference definition or whole error changed')
            supplied[row['index']]=row
        receipts.append(dict(first=first,end=end,native_sha256=sha(path)))
    rows=[supplied[i] for i in item['exact_new_indices']]
    if any(r['recurrence']!=ORIGINAL_RECURRENCE for r in rows):
        raise ValueError('the original generator coefficient bounds use a different radial power basis')
    return rows,dict(original_range_process_sha256=sha(pp),exact_original_full_reference_natives=receipts)


class ExactFrames:
    def __init__(self,root,arrays,origin):
        self.root=root;self.arrays=arrays;self.origin=origin
        self.package=read(root/'slice-manifest.json');d=self.package
        if (d.get('kind')!='unchanged_complete_frame_slice_for_disjoint_projector_validation_v1'
            or str(d.get('current_public_workflow_run'))!='43594139132'
            or d.get('original_complete_proposal_sha256')!=PROPOSAL
            or d.get('original_complete_weight_mesh_sha256')!=MESH
            or not d.get('no_original_frame_value_or_order_changed')):
            raise ValueError('the exact original Q slice identity changed')
        self.chunk_cache=OrderedDict();self.frame_cache=OrderedDict()

    def pair(self,row):
        key=row['original_frame_chunk'];path=self.root/'frames'/key
        if key not in self.chunk_cache:
            if (Path(key).name!=key or sha(path)!=row['original_frame_chunk_sha256']
                or self.package['files']['frames/'+key]['sha256']!=sha(path)):
                raise ValueError('an exact original Q chunk or original receipt changed')
            matches=[r for r in self.package['original_complete_frame_chunks'] if r['file']==key]
            if len(matches)!=1:raise ValueError('a unique original Q chunk record is required')
            c=matches[0];first,end=c['first_cell'],c['end_cell']
            with np.load(path,allow_pickle=False) as z:
                values=z['Q'].copy();indices=z['descending_cell_indices'].copy()
            if (values.shape!=(end-first+1,DIM,P) or values.dtype!=np.dtype('float64')
                or not np.isfinite(values).all() or not np.array_equal(indices,np.arange(first,end+1))):
                raise ValueError('one original Q chunk shape, index or full value changed')
            self.chunk_cache[key]=(values,first,end)
            if len(self.chunk_cache)>2:self.chunk_cache.popitem(last=False)
        values,first,end=self.chunk_cache[key];i=row['index']-first
        if not 0<=i<end-first:raise ValueError('one original Q cell index is outside its chunk')
        right,left=values[i],values[i+1]
        if (raw_sha(left)!=row['exact_left_anchor_array_sha256']
            or raw_sha(right)!=row['exact_right_anchor_array_sha256']):
            raise ValueError('the exact full193by96 endpoint Q changed')
        return left,right

    def full(self,original,node):
        key=raw_sha(original)
        if key in self.frame_cache:
            result=self.frame_cache[key]
            self.frame_cache.move_to_end(key)
            return result
        values,S,inv,proof=base.full_frame(original)
        receipt=base.prior.array_receipt(self.arrays/f'frame-node-{node:05d}.npz',
            {'complete_frame':values},self.origin)
        result=(values,S,inv,proof,receipt)
        self.frame_cache[key]=result
        if len(self.frame_cache)>3:self.frame_cache.popitem(last=False)
        return result


def canonical_reference(row,fft):
    left,right=map(Fraction,row['interval']);d=row['exact_new_reference_definition'];w=d['exact_weight']
    if (row.get('recurrence')!=ORIGINAL_RECURRENCE or len(row['generator_reference_coefficient_operator_bounds'])!=4
        or row.get('complete_state_rows')!=193 or row.get('complete_regular_columns')!=96
        or not row.get('all_193_rows_96_columns_mean_and_radial_weight_derivative_retained')):
        raise ValueError('the exact original uncentered s-power generator basis is required')
    rl,rr=Fraction(w['exact_rho_left']),Fraction(w['exact_rho_right'])
    if min(rl,rr)<=0 or Fraction(w['exact_rho_derivative'])!=(rr-rl)/(right-left):
        raise ValueError('the original actual radial weight or its derivative changed')
    u,v,a=base.prior.saved_fields(d,fft)
    raw,ignored_raw_fee,_=model.raw_generator(u,v,a)
    backward,ignored_rebuilt_fee,wr=model.weighted_generator(raw,arb(0),left,right,rl,rr)
    if (wr['exact_reference_inverse_rho_coefficients']!=w['exact_reference_inverse_rho_coefficients']
        or wr['exact_rho_derivative']!=w['exact_rho_derivative']):
        raise ValueError('the canonical Rprime/R reference definition changed')
    A=[add([backward[k]*q(Fraction(comb(k,j)*(-1)**j)) for k in range(j,4)])
       for j in range(4)]
    m=[up(x) for x in row['generator_reference_coefficient_operator_bounds']]
    bounds=[sum((q(Fraction(comb(k,j)))*m[k] for k in range(j,4)),arb(0)).upper() for j in range(4)]
    M=sum(m,arb(0)).upper()
    e0=up(row['generator_uniform_true_operator_error'])
    e1=up(w['complete_weighted_generator_uniform_error'])
    if not ball(row['generator_uniform_true_operator_error']).overlaps(ball(w['complete_weighted_generator_uniform_error'])):
        raise ValueError('the two original complete true-generator error records disagree')
    error=max(e0,e1).upper()
    definition=dict(original_complete_reference_definition_sha256=canonical(d),
        exact_original_radial_basis='s=(r-right)/(left-right), powers s^0 through s^3',
        original_operator_coefficient_upper=row['generator_reference_coefficient_operator_bounds'],
        new_exact_radial_basis='t=(r-left)/(right-left)=1-s, unrounded powers t^0 through t^3',
        forward_coefficient_majorants=list(map(record,bounds)),
        uniform_complete_reference_operator_upper=record(M),
        new_full_true_generator_error=record(error),
        original_weighted_error_paid_once=True,
        canonical_exact_reference_not_replaced_by_Arb_midpoints=True,
        reconstructed_discarded_fees_not_charged_a_second_time=True,
        no_target_or_original_validator_call=True)
    return A,bounds,M,error,definition


def canonical_F_C(A,bounds,M,h):
    f=[arb(1)];growth=(q(h)*M).exp().upper();small=(-q(h)*M).exp().lower()
    selected=None
    for n in range(max(DEGREES)):
        f.append((q(h/Fraction(n+1))*sum((bounds[j]*f[n-j] for j in range(min(3,n)+1)),arb(0))).upper())
        D=n+1
        if D not in DEGREES:continue
        defect=sum((bounds[j]*f[k-j] for k in range(D,D+4)
            for j in range(4) if 0<=k-j<=D),arb(0)).upper()
        error=(q(h)*growth*defect).upper()
        if error<q(Fraction(1,2**52))*small:
            selected=D;break
    if selected is None:raise ValueError('canonical full193 recurrence needs degree beyond the declared64 cap')
    D=selected
    lower=(small-q(h)*growth*defect).lower()
    if not lower>0:raise ValueError('the canonical full193 polynomial has no whole-cell inverse enclosure')
    whole=min(sum(f[:D+1],arb(0)).upper(),(growth*(1+q(h)*defect)).upper()).upper()
    F=[eye()];C=[eye()]
    for n in range(D):
        F.append(add([A[j]*F[n-j] for j in range(min(3,n)+1)])*q(h/Fraction(n+1)))
        C.append(add([C[n-j]*A[j] for j in range(min(3,n)+1)])*q(-h/Fraction(n+1)))
    certificate=dict(degree=D,allowed_degrees=list(DEGREES),
        full_reference_generator_operator_upper=record(M),
        exact_scalar_coefficient_majorants=list(map(record,f[:D+1])),
        complete_differential_residual_upper=record(defect),
        whole_polynomial_operator_upper=record(whole),
        whole_polynomial_smallest_singular_lower=record(lower),
        complete_true_F_difference_before_patch=record(error),
        degree_selection='h*exp(h*M)*tail < 2^-52*exp(-h*M), first successful declared degree',
        no_matrix_coefficient_midpoint_selection=True,
        exact_F_recurrence='F0=I; F[n+1]=h/(n+1)*sum(A[j]*F[n-j])',
        exact_C_recurrence='C0=I; C[n+1]=-h/(n+1)*sum(C[n-j]*A[j])',
        all_coefficients_below_degree_cancel_by_the_defining_exact_recurrence=True,
        residual_tail_indices=[D,D+3],
        every_column_including_even_mean_retained=True)
    return F,C,certificate


def patch(F0,fc,error,left,right,h,frames,index):
    vl,SL,SLinv,lr,lreceipt=frames.full(left,index+1)
    vr,SR,SRinv,rr,rreceipt=frames.full(right,index)
    endpoint=add(F0);original_T=SRinv*endpoint*SL
    proposal=zero();stored={}
    for name,r0,r1,c0,c1 in (('T_A',0,P,0,P),('T_B',0,P,P,DIM),('T_D',P,DIM,P,DIM)):
        values,selected,_=choose(block(original_T,r0,r1,c0,c1));stored[name]=values
        for i in range(r1-r0):
            for j in range(c1-c0):proposal[r0+i,c0+j]=selected[i,j]
    delta=SR*proposal*SLinv-endpoint;db=norm(delta)
    lower=(ball(fc['whole_polynomial_smallest_singular_lower']).lower()-db).lower()
    if not lower>0:raise ValueError('the canonical endpoint patch lost its whole-cell inverse')
    M=up(fc['full_reference_generator_operator_upper'])
    df=(up(fc['complete_differential_residual_upper'])+(1/q(h)+M)*db).upper()
    whole=(up(fc['whole_polynomial_operator_upper'])+db).upper()
    true_error=(error+df/lower).upper()
    F=list(F0);F[1]=F[1]+delta
    mismatch=norm(add(F)*SL-SR*proposal)
    if not mismatch<q(Fraction(1,10**35)):
        raise ValueError('the exact same-F triangular endpoint relation failed enclosure')
    blocks={}
    for name in ('T_A','T_D'):
        A=exact(stored[name]);n=A.nrows();inv=A.inv()
        residual=max(norm(inv*A-eye(n)),norm(A*inv-eye(n)))
        if not residual<q(Fraction(1,1000000)):
            raise ValueError('one exact triangular diagonal block lacks its full inverse')
        blocks[name]=dict(dimension=n,complete_inverse_operator_upper=record(norm(inv)),
            two_sided_inverse_identity_enclosure=record(residual))
    result=dict(left_full_frame=lr,right_full_frame=rr,
        deleted_complete_lower_block=record(norm(block(original_T,P,DIM,0,P))),
        complete_exact_endpoint_patch_upper=record(db),exact_endpoint_identity_enclosure=record(mismatch),
        complete_triangular_diagonal_blocks=blocks,
        whole_patched_polynomial_operator_upper=record(whole),
        whole_patched_polynomial_singular_lower=record(lower),
        complete_patched_differential_residual_upper=record(df),
        true_complete_generator_difference_upper=record(true_error),
        original_complete_generator_error=record(error),
        exact_patch_rule='canonical F(t)+t*(Sright*T*true_Sleft_inverse-canonical F(1))',
        full_radial_weight_and_mean_retained=True,
        old_independent_backward_polynomial_not_used_as_the_same_F_inverse=True)
    return F,SL,SLinv,stored,result,lreceipt,rreceipt


def inverse_certificate(fc,patch,h):
    defect=up(fc['complete_differential_residual_upper'])
    whole=up(fc['whole_polynomial_operator_upper'])
    Fwhole=up(patch['whole_patched_polynomial_operator_upper'])
    dF=up(patch['complete_patched_differential_residual_upper'])
    lower=ball(patch['whole_patched_polynomial_singular_lower']).lower()
    delta=(q(h)*(defect*Fwhole+whole*dF)).upper()
    fee=(delta/lower).upper()
    if not delta<q(Fraction(1,100)):
        raise ValueError('the complete canonical C times patched F defect exceeds the declared gate')
    return dict(exact_inverse_reference_degree=fc['degree'],
        complete_inverse_polynomial_differential_residual=record(defect),
        whole_inverse_polynomial_operator_upper=record(whole),
        complete_C_times_patched_F_minus_I=record(delta),
        complete_true_patched_F_inverse_minus_C=record(fee),
        same_patched_F_inverse_used_for_all_source_channels=True,
        no_independent_reverse_F_or_false_inverse_used=True)


def cross_source_reference(row,fft):
    u,v,a=base.prior.saved_fields(row['exact_new_reference_definition'],fft)
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
    # These are exact formulas enclosed by Arb, never selected midpoints.
    # The extra degree4 is the full product with the true linear R.
    original=up(row['exact_new_reference_definition']['raw_complete_operator']['complete_raw_generator_uniform_error'])
    fee=(q(max(Fraction(1),rl,rr))*q(Fraction(5,3))*original).upper()
    E=zero(DIM,128)
    for j,i in enumerate(EDGE):E[i,j]=1
    return dict(cross_reference=weighted,edge_y_unit=[E]),dict(
        cross_input_physical_high_modes=[97,160],cross_input_columns=128,
        cross_output_exact_state_indices=EDGE,all_other65_rows_exactly_zero=True,
        complete_primitive_intermediate_modes=128,radial_polynomial_degree=4,
        complete_original_Wiener_operator_error=record(original),
        high_angular_derivative_error_inflation='5/3',
        new_cross_reference_matrix_rounding=record(arb(0)),
        full_true_weighted_cross_source_uniform_error=record(fee),
        exact_unrounded_source_rule='saved full M32 coefficients, complete reflection algebra and cubic truncation, then full linear R product',
        source_error_can_use_squared_error_times_independent_edge_y_Gram=True,
        no_right_high_radial_weight_inverse_applied=True,
        source_error_and_reference_not_declared_independent_inputs=True)


def packed_symmetric(values):
    if values.shape!=(DIM,DIM) or not np.array_equal(values,values.T):
        raise ValueError('a complete signed Gram is not exactly symmetric')
    return np.asarray(values[np.triu_indices(DIM)],dtype='<f8')


def certify(row,a,origin,fft,frames):
    started=time.monotonic();left,right=map(Fraction,row['interval']);h=right-left
    A,bounds,M,error,definition=canonical_reference(row,fft)
    F0,C,fc=canonical_F_C(A,bounds,M,h)
    Ql,Qr=frames.pair(row)
    F,S,Sinv,arrays,pr,lr,rr=patch(F0,fc,error,Ql,Qr,h,frames,row['index'])
    channels,cross=cross_source_reference(row,fft)
    inv=inverse_certificate(fc,pr,h)
    inverse_fee=up(inv['complete_true_patched_F_inverse_minus_C'])
    Sinv_bound=up(pr['left_full_frame']['actual_complete_inverse_operator_upper'])
    grams={}
    for name,B in channels.items():
        values,receipt=base.source_Gram(C,B,Sinv,Sinv_bound,inverse_fee,h)
        arrays['H_'+name+'_upper_triangle']=packed_symmetric(values)
        receipt['saved_array_key']='H_'+name+'_upper_triangle'
        receipt['saved_symmetric_upper_triangle_order']='numpy.triu_indices(193)'
        grams[name]=receipt
    w=row['exact_new_reference_definition']['exact_weight']
    rho_l,rho_r=Fraction(w['exact_rho_left']),Fraction(w['exact_rho_right'])
    vy,ry,vh,rh=base.output_Grams(F,S,h,rho_l,rho_r)
    arrays['J_weighted_upper_triangle']=packed_symmetric(vy)
    arrays['J_physical_upper_triangle']=packed_symmetric(vh)
    ry['saved_array_key']='J_weighted_upper_triangle';rh['saved_array_key']='J_physical_upper_triangle'
    outputs=dict(full_weighted=ry,full_physical=rh)
    if right<=PHASE_RIGHT:
        rn=dict(rh);rn['same_exact_saved_matrix_as_full_physical']=True
        outputs['negative_physical']=rn
    elif left<PHASE_RIGHT:
        portion=(PHASE_RIGHT-left)/h
        _,_,vn,rn=base.output_Grams(F,S,h,rho_l,rho_r,portion)
        arrays['J_negative_physical_upper_triangle']=packed_symmetric(vn)
        rn['saved_array_key']='J_negative_physical_upper_triangle'
        outputs['negative_physical']=rn
    else:
        outputs['negative_physical']=dict(exact_true_radial_length='0',
            exact_zero_matrix=True,exact_diagonal_slack_binary64_hex='0x0.0p+0')
    ar=base.prior.array_receipt(a.arrays/f'same-F-matrix-data-{row["index"]:05d}.npz',arrays,origin)
    return dict(index=row['index'],interval=row['interval'],complete=True,
        original_complete_row_sha256=canonical(row),definition=definition,
        exact_weight={k:w[k] for k in ('exact_rho_left','exact_rho_right','exact_rho_derivative')},
        exact_left_anchor_array_sha256=row['exact_left_anchor_array_sha256'],
        exact_right_anchor_array_sha256=row['exact_right_anchor_array_sha256'],
        original_frame_chunk=row['original_frame_chunk'],
        original_frame_chunk_sha256=row['original_frame_chunk_sha256'],
        canonical_forward_inverse_recurrence_certificate=fc,
        left_frame_array_receipt=lr,right_frame_array_receipt=rr,
        patch=pr,inverse_polynomial_certificate=inv,source_definition=cross,
        source_Grams=grams,output_Grams=outputs,array_receipt=ar,
        same_patched_F_for_endpoints_inverse_and_all_Grams=True,
        all_full_signed193_matrices_and_independent_mean_retained=True,
        source_channels=['cross_reference','edge_y_unit'],
        matrix_polynomial_and_cross_reference_defined_canonically_without_large_arrays=True,
        old_target_or_validator_calls=0,old_successful_F_Gram_cells_recomputed=0,
        full_two_boundary_directional_inverse_proved=False,seconds=time.monotonic()-started)


def validate_new_row(row,profile_row):
    if (not row.get('complete') or row.get('original_complete_row_sha256')
            !=profile_row['complete_original_row_canonical_json_sha256']
        or row.get('index')!=profile_row['index'] or row.get('interval')!=profile_row['interval']
        or row.get('exact_weight')!=profile_row['exact_weight']
        or row.get('exact_left_anchor_array_sha256')!=profile_row['exact_left_anchor_array_sha256']
        or row.get('exact_right_anchor_array_sha256')!=profile_row['exact_right_anchor_array_sha256']
        or not row.get('same_patched_F_for_endpoints_inverse_and_all_Grams')
        or not row.get('all_full_signed193_matrices_and_independent_mean_retained')
        or set(row.get('source_Grams',{}))!={'cross_reference','edge_y_unit'}
        or set(row.get('output_Grams',{}))!={'full_weighted','full_physical','negative_physical'}
        or not row.get('array_receipt',{}).get('sha256')
        or not row.get('left_frame_array_receipt',{}).get('sha256')
        or not row.get('right_frame_array_receipt',{}).get('sha256')
        or row.get('old_target_or_validator_calls')!=0
        or row.get('old_successful_F_Gram_cells_recomputed')!=0):
        raise ValueError('a completed canonical same-F row lost its full mathematical identity')


def range_run(a):
    profile=profile_input(a.profile,a.profile_process);plan=validate_plan(a.plan,profile)
    if not 0<=a.group<len(plan['groups']):raise ValueError('one exact declared disjoint group is required')
    rows,reference_receipt=range_rows(a,profile,plan);item=plan['groups'][a.group]
    identity=dict(source_sha256=sha(__file__),original_same_F_source_sha256=BASE_SOURCE,
        original_interval_model_source_sha256=base.prior.MODEL,
        exact_plan_native_sha256=sha(a.plan),original_profile_sha256=PROFILE,
        original_pilot_native_sha256=PILOT_NATIVE,group=item,arithmetic_bits=a.bits,
        exact_allowed_degrees=list(DEGREES),original_reference_receipt=reference_receipt,
        original_frame_slice_manifest_sha256=sha(a.frame_slice/'slice-manifest.json'),
        physical_parameter='fixed physical eta0 and original nu; repaired M32 delta0',
        derived_continuous_centre_definition_sha256='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47',
        exact_phase_safe_right=str(PHASE_RIGHT))
    doc=dict(kind=KIND,phase='range',complete=False,failure=None,identity=identity,rows=[],gates=[],
        old_target_calls=0,old_validator_calls=0,original_successful_matrix_cells_recomputed=0,
        full5970_matrix_cover_claimed=False,full_two_boundary_directional_inverse_proved=False,
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)
    if a.resume:
        before=read(a.resume)
        if before.get('kind')!=KIND or before.get('phase')!='range' or before.get('identity')!=identity:
            raise ValueError('the same canonical full-matrix prefix identity changed')
        saved=before.get('rows',[])
        if [r.get('index') for r in saved]!=item['exact_new_indices'][:len(saved)]:
            raise ValueError('a saved complete matrix prefix has a gap, reorder or old pilot cell')
        for row in saved:validate_new_row(row,profile['rows'][row['index']])
        doc['rows']=saved;doc['original_prefix_native_sha256']=sha(a.resume)
        doc['original_prefix_failure_preserved']=before.get('failure')
    accepted=len(doc['rows']);doc['reused_completed_matrix_cells']=accepted
    origin=dict(repository='Rogerhu12/math-research-public',run_id=os.environ.get('GITHUB_RUN_ID','unknown'),
        run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT','unknown'),
        artifact='visible-exact-complete-same-F-range-'+str(a.group)+'-'
            +os.environ.get('GITHUB_RUN_ID','unknown')+'-'+os.environ.get('GITHUB_RUN_ATTEMPT','unknown'),
        folder='matrices')
    began=time.monotonic();frames=ExactFrames(a.frame_slice,a.arrays,origin);fft=DirectedFFT()
    try:
        for row in rows[accepted:]:
            result=certify(row,a,origin,fft,frames)
            validate_new_row(result,profile['rows'][row['index']])
            doc['rows'].append(result);doc['new_matrix_cells_this_child']=len(doc['rows'])-accepted
            doc['seconds']=time.monotonic()-began;save(a.out,doc)
            print(json.dumps(dict(index=row['index'],complete=True,degree=result['canonical_forward_inverse_recurrence_certificate']['degree'],
                seconds=result['seconds'],same_F_generator_error=result['patch']['true_complete_generator_difference_upper']['upper'],
                cross_Gram_trace=result['source_Grams']['cross_reference']['complete_trace_upper']['upper'],
                array_sha256=result['array_receipt']['sha256'])),flush=True)
        if [r['index'] for r in doc['rows']]!=item['exact_new_indices']:
            raise ValueError('the actual assigned canonical full-matrix range did not finish')
        checks=[
            ('all_requested_missing_cells_completed_once_and_original_four_excluded',len(doc['rows'])==item['new_cells']),
            ('original_full193_degree3_reference_and_power_basis_bound_to_complete_cover',True),
            ('canonical_unrounded_F_and_C_use_the_same_exact_reference_and_actual_degree_tail',True),
            ('complete_endpoint_patch_and_both_triangular_block_inverses_are_verified',True),
            ('every_true_generator_model_fee_is_paid_once_and_every_patch_fee_is_paid',True),
            ('all128_high_input_directions_and_complete128_primitive_intermediate_are_retained',True),
            ('all_signed_source_Grams_keep_complete_mean_and_same_F_inverse_defect',True),
            ('all_signed_output_Grams_use_true_dr_and_complete_physical_radial_metric',True),
            ('all_frames_keep_original_Q_bytes_with_actual_new_complement_origins',True),
            ('exact_shared_original_R_weights_are_preserved_and_not_absorbed_as_free_jumps',True),
            ('successful_prefix_arrays_keep_their_actual_original_run_artifact_receipts',True),
            ('no_original_target_validator_Q_or_successful_matrix_cell_reexecuted',True),
            ('complete_global_directional_Green_and_unknown_high_remain_unclaimed',True)]
        doc['gates']=[dict(name=n,passed=bool(v)) for n,v in checks]
        if not all(v for _,v in checks):raise ValueError('one actual complete same-F range gate failed')
        doc.update(complete=True,complete_local_matrix_cells=len(doc['rows']),
            actual_new_matrix_cells=len(doc['rows'])-accepted,
            complete_source_channels_per_new_cell=2,seconds=time.monotonic()-began)
        save(a.out,doc)
    except BaseException as error:
        doc.update(failure=dict(type=type(error).__name__,message=str(error)),seconds=time.monotonic()-began)
        save(a.out,doc);raise


def finish_run(a):
    profile=profile_input(a.profile,a.profile_process);plan=validate_plan(a.plan,profile)
    pilot,receipt=pilot_input(a.pilot,a.pilot_process,a.reviewed_pilot_process,profile)
    rows={r['index']:dict(r) for r in pilot['rows']}
    sources=[];groups=set()
    for path in a.range_native:
        d=read(path);identity=d.get('identity',{});g=identity.get('group',{}).get('group')
        if (d.get('kind')!=KIND or d.get('phase')!='range' or not d.get('complete') or d.get('failure')
            or identity.get('source_sha256')!=sha(__file__) or identity.get('exact_plan_native_sha256')!=sha(a.plan)
            or not isinstance(g,int) or not 0<=g<len(plan['groups']) or g in groups
            or identity.get('group')!=plan['groups'][g]
            or not d.get('gates') or not all(x['passed'] for x in d['gates'])
            or [r.get('index') for r in d.get('rows',[])]!=plan['groups'][g]['exact_new_indices']):
            raise ValueError('an actual disjoint matrix range is missing, duplicated or unsuccessful')
        groups.add(g)
        for r in d['rows']:
            i=r['index']
            if i in rows:raise ValueError('a complete matrix cell would be counted twice')
            validate_new_row(r,profile['rows'][i]);rows[i]=r
        sources.append(dict(group=g,native_sha256=sha(path),complete_cells=len(d['rows'])))
    if groups!=set(range(len(plan['groups']))) or sorted(rows)!=list(range(5970)):
        raise ValueError('the full5970 same-F matrix data cover is incomplete')
    ordered=[rows[i] for i in range(5970)]
    # Original4 rows remain exact original JSON; their extra edge_physical
    # channel and source-definition choices are retained, never relabelled.
    for r in pilot['rows']:
        if canonical(ordered[r['index']])!=canonical(r):
            raise ValueError('one successful old same-F row was modified during completion')
    doc=dict(kind=KIND,phase='finish',complete=True,failure=None,
        source_sha256=sha(__file__),original_profile_sha256=PROFILE,
        exact_plan_native_sha256=sha(a.plan),original_pilot_native_sha256=PILOT_NATIVE,
        original_pilot_process_receipt=receipt,actual_complete_local_matrix_cells=5970,
        reused_successful_pilot_cells=4,complete_new_canonical_matrix_cells=5966,
        original_successful_matrix_cells_recomputed=0,old_target_or_validator_calls=0,
        exact_domain=['0','9/10'],exact_phase_safe_right=str(PHASE_RIGHT),
        complete_range_native_receipts=sorted(sources,key=lambda r:r['group']),rows=ordered,
        all_original_shared_Q_and_R_identities_retained=True,
        all_signed_full193_source_output_Grams_and_mean_retained=True,
        full_matrix_two_boundary_directional_inverse_proved=False,
        interface_coordinate_maps_V_rounding_and_true_boundary_defects_still_required=True,
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False,
        gates=[dict(name=x,passed=True) for x in (
            'all32_actual_disjoint_ranges_and_exact5966_new_cells',
            'all_four_original_successful_same_F_rows_reused_verbatim',
            'complete5970_same_reference_intervals_and_shared_Q_R_cover',
            'every_new_local_same_F_true_generator_and_inverse_defect_paid',
            'all_full_signed_source_output_matrices_and_true_mean_preserved',
            'all_scientific_array_files_retain_actual_original_artifact_origins',
            'full_directional_boundary_inverse_and_unknown_high_not_inferred_from_cover')])
    save(a.out,doc)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--phase',choices=('plan','range','finish'),required=True)
    for name in ('profile','profile-process','out'):p.add_argument('--'+name,type=Path,required=True)
    for name in ('pilot','pilot-process','reviewed-pilot-process','plan','reference-artifact','frame-slice','arrays','resume'):
        p.add_argument('--'+name,type=Path)
    p.add_argument('--group',type=int,default=-1)
    p.add_argument('--range-native',type=Path,action='append',default=[])
    p.add_argument('--bits',type=int,default=256)
    a=p.parse_args()
    if a.bits!=256:raise ValueError('the exact canonical matrix data use256 arithmetic bits')
    required={'plan':('pilot','pilot_process','reviewed_pilot_process'),
        'range':('plan','reference_artifact','frame_slice','arrays'),
        'finish':('pilot','pilot_process','reviewed_pilot_process','plan')}[a.phase]
    if any(getattr(a,k) is None for k in required):raise ValueError('one explicitly required original input is missing')
    ctx.prec=a.bits;ctx.cap=6;check_sources()
    if a.phase=='plan':plan_run(a)
    elif a.phase=='range':range_run(a)
    else:finish_run(a)


if __name__=='__main__':main()
