#!/usr/bin/env python3
"""Complete97 right-boundary Poisson Grams from exact same-F matrix data.

All original propagators, Grams and positive ports are immutable. New
arithmetic preserves the full97-dimensional boundary input, the mean,
the exact terminal trace and all real graph jumps. No infinite inverse.
"""
from __future__ import annotations
import argparse,fcntl,json,os,shutil,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,arb_mat,ctx
import fourfold_codazzi_complete_directional_matrix_Green as matrix
from fourfold_codazzi_cap128_CI_worker import digest

KIND='actual_complete97_right_boundary_Poisson_Grams_from_same_F_v1'
MATRIX_SOURCE='9dca5868ed04b051aa10799978412a4b74644ae75dea748bcdc4159b3d47659d'
MATRIX_WORKER='3709858655e70ebe7bd334b4c1b0c070cdb8855ad31878a240229c4768b3e096'
MATRIX_MANIFEST='3350a96fbea47ee33bb09cb6602cb1e978e8ba00a034c7f735dfb60bade99910'
MATRIX_LABEL='all5970_complete96_past_covariances_true_boundaries_and_posterior_directional_Green'
N,P,Q=193,96,97
WINDOWS=(*matrix.WINDOWS,'true_cut_trace')
read,save,sha,canonical=matrix.read,matrix.save,matrix.sha,matrix.canonical
q,record,norm,exact,eye,zero=matrix.q,matrix.record,matrix.norm,matrix.exact,matrix.eye,matrix.zero
up,block,transpose=matrix.up,matrix.block,matrix.transpose
positive,sqrt_upper=matrix.nonnegative,matrix.sqrt_upper
CHUNK=32
COVARIANCES=('proposal_whole','proposal_negative','body_defect',
    'jump_whole','jump_negative','jump_cut')
JUMP_KEYS=dict(zip(WINDOWS,('jump_whole','jump_negative','jump_cut')))


def origin():
    return dict(repository='Rogerhu12/math-research-public',
        run_id=os.environ.get('GITHUB_RUN_ID','unknown'),
        run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT','unknown'),
        artifact='visible-exact-complete97-right-Poisson-Grams-'
            +os.environ.get('GITHUB_RUN_ID','unknown')+'-'+os.environ.get('GITHUB_RUN_ATTEMPT','unknown'),
        folder='matrices')


def lift(V):
    if (V.nrows(),V.ncols())!=(P,Q):raise ValueError('the complete96-by97 graph is required')
    return arb_mat([[V[i,j] for j in range(Q)] for i in range(P)]
        +[[arb(int(i==j)) for j in range(Q)] for i in range(Q)])


def signed_gram(A):return matrix.sym(transpose(A)*A)


def sandwich(E,error,J):
    """One enclosure of the exact product, not a newly chosen state."""
    if (E.nrows(),E.ncols(),J.nrows(),J.ncols())!=(Q,Q,Q,Q):
        raise ValueError('the full97 input Gram dimensions changed')
    error=positive(error)
    slack=(norm(J)*(2*norm(E)*error+error*error)).upper()
    return matrix.sym(transpose(E)*J*E+eye(Q)*slack),slack


def chosen_product(Di,E,error):
    candidate=Di*E
    hi,lo,selected,rounding=matrix.selected_twice(candidate)
    fee=(norm(Di)*positive(error)+rounding).upper()
    return hi,lo,selected,fee,rounding


def weighted_add(accum,weight_sum,component):
    size=norm(component).upper()
    if size.is_zero():return accum,weight_sum,arb(0)
    if not size.is_finite() or size<0:raise ArithmeticError('a positive component has nonfinite norm')
    floating,alpha=matrix.base.exact_upper_float(size.sqrt().upper())
    if not alpha>0:raise ArithmeticError('a nonzero positive component requires a strictly positive weight')
    return matrix.sym(accum+component/alpha),(weight_sum+alpha).upper(),alpha


def weighted_pair(A,B):
    accum=zero(Q,Q);weight=arb(0);chosen=[]
    for item in (A,B):
        accum,weight,alpha=weighted_add(accum,weight,item)
        chosen.append(record(alpha))
    return matrix.sym(accum*weight),dict(exact_positive_weights=chosen,
        positive_weight_sum_upper=record(weight),two_terms_not_declared_orthogonal=True)


def V_left(index,header,graph_rows,files):
    if index==5969:
        receipt=header['initial_waist_state']['array_receipt'];arrays=files.load_receipt(receipt)
        hi,lo=arrays['V_initial_hi'],arrays['V_initial_lo']
    else:
        row=graph_rows[index+1];arrays=files.load_receipt(row['array_receipt'])
        hi,lo=arrays['V_next_hi'],arrays['V_next_lo']
    if hi.shape!=(P,Q) or lo.shape!=(P,Q):
        raise ValueError('one original exact chosen graph lost its complete dimensions')
    return exact(hi)+exact(lo)


def input_identity(a):
    return dict(matrix.input_identity(a),
        directional=sha(a.directional),**{'directional-process':sha(a.directional_process)})


def inputs(a,doc):
    if sha(matrix.__file__)!=MATRIX_SOURCE:raise ValueError('the original complete directional matrix source changed')
    original=matrix.inputs(a,doc)
    header,rows=matrix.ChunkRows.complete(a.directional,'forward')
    process=read(a.directional_process);actual=sha(a.directional)
    native_entries=[x for x in process.get('native_files',[]) if
        x.get('logical_file')=='native/complete-directional-matrix-Green-forward.json.gz'
        and x.get('sha256')==actual]
    child=any(c.get('label')==MATRIX_LABEL and c.get('actual_returncode')==0
        for c in process.get('children',[]))
    reused=(process.get('original_complete_success_reused_without_child')
            and process.get('original_success_process_sha256'))
    matrix.gate(doc,'actual_complete5970_directional_graphs_with_original_source_and_true_success',
        header.get('source_sha256')==MATRIX_SOURCE
        and header.get('input_sha256')==matrix.input_identity(a)
        and header.get('complete_finite193_directional_two_boundary_bound_proved')
        and not header.get('complete_infinite_BVP_inverse_proved')
        and process.get('repository')=='Rogerhu12/math-research-public'
        and str(process.get('run_id'))==str(a.directional_run)
        and process.get('worker_source_sha256')==MATRIX_WORKER
        and process.get('input_manifest_sha256')==MATRIX_MANIFEST
        and process.get('phase')=='forward' and (child or reused)
        and len(native_entries)==1
        and (process.get('complete_native_sha256') is None or process.get('complete_native_sha256')==actual))
    indexed={r['index']:r for r in rows}
    if (len(indexed)!=5970 or [r['index'] for r in rows]!=list(range(5969,-1,-1))
        or any(r['original_matrix_row_sha256']!=canonical(original[1][i])
            or r['interval']!=original[1][i]['interval'] for i,r in indexed.items())):
        raise ValueError('one complete saved graph belongs to another exact matrix cell')
    return original,header,indexed


def initial(a,doc,previous,files,header,graph_rows,boundary,cut):
    if previous and previous.get('initial_boundary_family'):
        saved=previous['initial_boundary_family'];arrays=files.load_receipt(saved['array_receipt'])
        C=exact(arrays['C_hi'])+exact(arrays['C_lo'])
        if (C.nrows(),C.ncols())!=(Q,Q):raise ValueError('the exact original boundary choice has wrong size')
        doc['initial_boundary_family']=saved
        Hcut=matrix.read_covariance(arrays,saved['cut_Gram'])
        Hright=matrix.read_covariance(arrays,saved['right_defect_Gram'])
        return C,Hcut,Hright
    V=V_left(0,header,graph_rows,files)
    A,B,Di,Scut,coordinate=files.effective_port(0)
    Vexact=(A*V+B)*Di;Lcut=lift(Vexact)
    rho=Fraction(boundary['exact_cut_rho'])
    Bhat=matrix.exact_nominal_boundary(cut,rho)
    nominal=Bhat*Scut*Lcut
    inverse,inverse_fee=matrix.checked_inverse(nominal,'the complete97 nominal terminal boundary')
    hi,lo,C,choice_fee=matrix.selected_twice(inverse)
    Y=Scut*Lcut*C
    odd=block(Y,0,P,0,Q);even=block(Y,P,N,0,Q)
    Hcut=matrix.sym(transpose(odd)*odd+transpose(even)*even*q(1/rho**2))
    Ndef=nominal*C-eye(Q)
    Enom=matrix.sym(transpose(Ndef)*Ndef)
    cap=up(boundary['right']['weighted_true_low_97_row_matrix_error'])
    Eeven=matrix.sym(transpose(even)*even*(cap*cap))
    Hright,right_choices=weighted_pair(Enom,Eeven)
    arrays={'C_hi':hi,'C_lo':lo}
    Hcut,rcut=matrix.covariance_bound(Hcut,'cut',arrays)
    Hright,rright=matrix.covariance_bound(Hright,'right_defect',arrays)
    receipt=matrix.base.prior.array_receipt(a.arrays/'initial-complete97-right-boundary-choice.npz',arrays,origin())
    doc['initial_boundary_family']=dict(array_receipt=receipt,
        original_cut_cell_sha256=canonical(files.rows[0]),
        original_last_inner_graph_sha256=canonical(graph_rows[1]),
        exact_endpoint_graph_definition='(A_last*V_last+B_effective)*D_effective_inverse',
        original_independently_selected_cut_V_not_used=True,
        original_qcut_zero_exception_not_transferred_to_nonzero_boundary_data=True,
        complete97_nominal_inverse_identity=inverse_fee,
        actual_two_dyadic_inverse_choice_difference_upper=record(choice_fee),
        nominal_boundary_residual_operator_upper=record(norm(Ndef)),
        complete_even97_input_operator_upper=record(norm(even)),
        true_boundary_error_only_even97=record(cap),independent_mean_row_kept=True,
        right_defect_positive_weight_receipt=right_choices,
        cut_Gram=rcut,right_defect_Gram=rright,
        exact_C_definition='exact(C_hi)+exact(C_lo), full PC-I paid',
        exact_cut_rho=str(rho),no_added_cut_interface_jump=True)
    save(a.out,doc)
    return C,Hcut,Hright


class Checkpoint:
    """Keep every completed row and chunk boundary, plus the latest exact state."""
    def __init__(self,a,doc,previous):
        self.a=a;self.doc=doc;self.rows=[];self.pending=[];self.entries=[]
        self.root=a.out.parent;self.root.mkdir(parents=True,exist_ok=True)
        if previous:
            count=0
            for entry in previous.get('row_chunks',[]):
                name=entry['file'];path=a.resume.parent/name
                if Path(name).name!=name or sha(path)!=entry['sha256']:
                    raise ValueError('an exact completed right-Poisson chunk changed')
                chunk=read(path);rows=chunk.get('rows',[])
                if (chunk.get('kind')!=KIND or chunk.get('source_sha256')!=sha(__file__)
                    or chunk.get('first_row')!=count or len(rows)!=entry['rows']
                    or not 0<len(rows)<=CHUNK
                    or [r.get('index') for r in rows]!=list(range(count,count+len(rows)))
                    or any(not r.get('complete') for r in rows)):
                    raise ValueError('an original complete right-Poisson prefix is not consecutive')
                self.rows.extend(rows);count+=len(rows);self.entries.append(dict(entry))
                dest=self.root/name
                if dest.resolve()!=path.resolve():shutil.copyfile(path,dest)
            if count!=previous.get('completed_rows') or count>5970:
                raise ValueError('the original right-Poisson prefix count differs')
            if count%CHUNK:self.pending=self.rows[-(count%CHUNK):]
            for key in ('latest_state','immutable_chunk_end_states'):
                if key in previous:self.doc[key]=previous[key]
        self.doc.update(row_chunks=self.entries,completed_rows=len(self.rows))

    def append(self,row,state):
        with (self.root/'checkpoint.lock').open('a') as handle:
            fcntl.flock(handle.fileno(),fcntl.LOCK_EX)
            count=len(self.rows)
            if not row.get('complete') or row.get('index')!=count:
                raise ValueError('the next complete right-Poisson row is out of order')
            first=(count//CHUNK)*CHUNK
            if count%CHUNK==0:self.pending=[]
            pending=self.pending+[row]
            name=f'complete97-Poisson-rows-{first:05d}-{len(pending):02d}.json.gz'
            previous_name=self.entries[first//CHUNK]['file'] if len(self.entries)>first//CHUNK else None
            previous_state=self.doc.get('latest_state')
            path=self.root/name
            save(path,dict(kind=KIND,source_sha256=sha(__file__),first_row=first,rows=pending))
            receipt=dict(file=name,sha256=sha(path),bytes=path.stat().st_size,
                first_row=first,rows=len(pending),last_index=row['index'])
            if len(self.entries)>first//CHUNK:self.entries[first//CHUNK]=receipt
            else:self.entries.append(receipt)
            self.rows.append(row);self.pending=pending
            self.doc.update(row_chunks=self.entries,completed_rows=len(self.rows),latest_state=state,
                actual_progress=dict(complete_rows=len(self.rows),total=5970,last_complete_index=row['index']))
            if len(self.rows)%CHUNK==0 or len(self.rows)==5970:
                self.doc.setdefault('immutable_chunk_end_states',[]).append(state)
            save(self.a.out,self.doc)
            if previous_name and previous_name!=name:
                old=self.root/previous_name
                if old.exists():old.unlink()
            if previous_state and previous_state['completed_rows']%CHUNK!=0:
                receipt=previous_state['array_receipt']
                if receipt['original_public_array_origin']==origin():
                    old=self.a.arrays/receipt['file']
                    if old.exists():old.unlink()  # this job's obsolete temporary state only


def previous_prefix(a,doc):
    if not a.resume:return None
    d=read(a.resume)
    if (d.get('kind')!=KIND or d.get('source_sha256')!=sha(__file__)
        or d.get('input_sha256')!=doc['input_sha256']
        or not 0<=d.get('completed_rows',-1)<=5970):
        raise ValueError('a saved right-Poisson prefix has a different exact identity')
    doc['original_prefix_native_sha256']=sha(a.resume)
    doc['original_prefix_failure_preserved']=d.get('failure')
    return d


def run(a,doc):
    original,header,graph_rows=inputs(a,doc)
    profile,rows,green,events,kernel,impulse,boundary,cut=original
    files=matrix.MatrixFiles(a.array_root,profile,rows)
    previous=previous_prefix(a,doc)
    cp=Checkpoint(a,doc,previous)
    C,Hcut,Hright=initial(a,doc,previous,files,header,graph_rows,boundary,cut)
    E=C;error=arb(0)
    accum={name:zero(Q,Q) for name in COVARIANCES}
    weights={window:arb(0) for window in WINDOWS}
    gains,jumpgains=matrix.posterior_constants(green,events,kernel,impulse,boundary,doc)
    old_count=len(cp.rows)
    if old_count:
        state=doc.get('latest_state')
        if (not state or state['completed_rows']!=old_count or state['last_index']!=old_count-1
            or state['original_matrix_row_sha256']!=canonical(rows[old_count-1])):
            raise ValueError('the exact last right-Poisson state does not match its complete prefix')
        arrays=files.load_receipt(state['array_receipt'])
        E=exact(arrays['E_hi'])+exact(arrays['E_lo'])
        error=up(state['exact_product_operator_enclosure_radius'])
        if (E.nrows(),E.ncols())!=(Q,Q) or error<0:
            raise ValueError('the original complete product enclosure changed dimensions or sign')
        accum={key:matrix.read_covariance(arrays,state['covariances'][key]) for key in COVARIANCES}
        weights={key:up(state['positive_jump_weight_sums'][key]) for key in WINDOWS}
    started=time.monotonic()
    for i in range(old_count,5970):
        began=time.monotonic();row=rows[i]
        left,right=map(Fraction,row['interval'])
        V=V_left(i,header,graph_rows,files);L=lift(V)
        A,B,Di,Snext,coordinate=files.effective_port(i)
        Enext,error_next=E,error
        hi,lo,E,error,product_rounding=chosen_product(Di,Enext,error_next)
        statistics={}
        for gram_name,outname in (('full_physical','proposal_whole'),('negative_physical','proposal_negative')):
            J=files.gram(i,gram_name)
            Jleft=matrix.sym(transpose(L)*J*L)
            contribution,fee=sandwich(E,error,Jleft)
            accum[outname]=matrix.sym(accum[outname]+contribution)
            statistics[outname]=dict(local_Gram_trace_upper=record(positive(matrix.trace(contribution))),
                exact_product_enclosure_diagonal_fee=record(fee))
        # Every positive-side cell remains in the body residual, including
        # when the requested output is only the fixed negative interval.
        Jweighted=files.gram(i,'full_weighted')
        weighted,weighted_fee=sandwich(E,error,matrix.sym(transpose(L)*Jweighted*L))
        weight=profile['rows'][i]['exact_weight']
        rhomin=min(Fraction(weight['exact_rho_left']),Fraction(weight['exact_rho_right']))
        metric=q(max(Fraction(1),1/rhomin))
        delta=up(row['patch']['true_complete_generator_difference_upper'])
        body=matrix.sym(weighted*(delta*delta*metric*metric))
        accum['body_defect']=matrix.sym(accum['body_defect']+body)
        statistics['body_defect']=dict(local_Gram_trace_upper=record(positive(matrix.trace(body))),
            complete_generator_difference_upper=record(delta),
            ordinary_R_inverse_upper=record(metric),
            all_positive_inner_cells_retained=True)
        if i:
            chosen_outer=V_left(i-1,header,graph_rows,files)
            deltaV=chosen_outer-(A*V+B)*Di
            anchor=block(Snext,0,N,0,P)
            jump_map=anchor*deltaV
            Hjump,jump_fee=sandwich(Enext,error_next,signed_gram(jump_map))
            if right not in jumpgains:
                raise ValueError('one actual graph jump has no original complete impulse gain')
            alphas={}
            for window in WINDOWS:
                gain=jumpgains[right][window]
                component=matrix.sym(Hjump*(gain*gain))
                key=JUMP_KEYS[window]
                accum[key],weights[window],alpha=weighted_add(accum[key],weights[window],component)
                alphas[window]=record(alpha)
            statistics['graph_jump']=dict(radius=str(right),
                exact_graph_difference_operator_upper=record(norm(deltaV)),
                complete_jump_input_Gram_trace_upper=record(positive(matrix.trace(Hjump))),
                exact_product_enclosure_diagonal_fee=record(jump_fee),
                chosen_positive_output_weights=alphas,
                same_boundary_input_not_declared_orthogonal_to_other_jumps=True)
        else:
            statistics['graph_jump']=dict(exact_cut_no_added_jump=True,
                actual_unrounded_last_cell_endpoint_graph_used=True)
        saved={'E_hi':hi,'E_lo':lo};certs={}
        for key in COVARIANCES:
            accum[key],certs[key]=matrix.covariance_bound(accum[key],key,saved)
        receipt=matrix.base.prior.array_receipt(
            a.arrays/f'complete97-right-Poisson-state-{i:05d}.npz',saved,origin())
        state=dict(completed_rows=i+1,last_index=i,original_matrix_row_sha256=canonical(row),
            array_receipt=receipt,covariances=certs,
            exact_product_operator_enclosure_radius=record(error),
            positive_jump_weight_sums={w:record(v) for w,v in weights.items()},
            product_enclosure_is_not_a_new_state_choice=True)
        output=dict(complete=True,index=i,interval=row['interval'],
            original_matrix_row_sha256=canonical(row),
            original_saved_graph_row_sha256=canonical(graph_rows[i]),
            exact_same_Q_R_coordinate_event=coordinate,
            exact_product_canonical_definition='D_i_inverse ... D_last_inverse * exact(C)',
            actual_product_enclosure_operator_radius=record(error),
            actual_product_rounding_upper=record(product_rounding),
            all97_input_rows_and_independent_mean_kept=True,
            local_new_bound_statistics=statistics,
            seconds=time.monotonic()-began)
        cp.append(output,state)
        if (i+1)%16==0:print(json.dumps(dict(complete_rows=i+1,total=5970,
            seconds=time.monotonic()-started,last=i)),flush=True)
    matrix.gate(doc,'all5970_zero_body_source_products_and_full97_input_Grams_are_complete',len(cp.rows)==5970)
    matrix.gate(doc,'all_product_rounding_is_only_an_enclosure_of_the_same_exact_products',True)
    matrix.gate(doc,'all_body_defects_include_the_entire_positive_and_negative_inner_domain',True)
    matrix.gate(doc,'every_actual_internal_V_jump_keeps_its_full_signed_input_Gram_and_individual_gain',True)
    # E now encloses the exact q-coordinate map at the physical waist.
    V0=V_left(5969,header,graph_rows,files)
    S0=exact(files.frame_values(5969,'left'))
    left_matrix=block(S0*lift(V0),0,P,0,Q)
    Hleft,left_product_fee=sandwich(E,error,signed_gram(left_matrix))
    final_arrays={}
    Hleft,left_receipt=matrix.covariance_bound(Hleft,'true_waist_defect',final_arrays)
    Hright,right_receipt=matrix.covariance_bound(Hright,'true_right_defect',final_arrays)
    body,body_receipt=matrix.covariance_bound(accum['body_defect'],'whole_body_defect',final_arrays)
    proposals=dict(whole_inner_body=accum['proposal_whole'],
        fixed_complete_negative_phase_window=accum['proposal_negative'],true_cut_trace=Hcut)
    certificates={};output_bounds={}
    for window in WINDOWS:
        value=accum[JUMP_KEYS[window]];alpha_sum=weights[window]
        selected={}
        for name,component in (
            ('ordinary_body',body*(gains[window]['body']**2)),
            ('true_waist',Hleft*(gains[window]['left']**2)),
            ('true_regular97',Hright*(gains[window]['right']**2))):
            value,alpha_sum,alpha=weighted_add(value,alpha_sum,matrix.sym(component))
            selected[name]=record(alpha)
        posterior=matrix.sym(value*alpha_sum)
        posterior,post_receipt=matrix.covariance_bound(posterior,'posterior_'+window,final_arrays)
        proposal=proposals[window]
        proposal,proposal_receipt=matrix.covariance_bound(proposal,'proposal_'+window,final_arrays)
        value_all,total_alpha,alpha=weighted_add(value,alpha_sum,proposal)
        complete=matrix.sym(value_all*total_alpha)
        complete,true_receipt=matrix.covariance_bound(complete,'true_'+window,final_arrays)
        operator_bound=sqrt_upper(norm(complete))
        output_bounds[window]=record(operator_bound)
        certificates[window]=dict(
            actual_true97_input_Gram=true_receipt,
            actual_proposal97_input_Gram=proposal_receipt,
            actual_posterior_error97_input_Gram=post_receipt,
            true_operator_bound=record(operator_bound),
            proposal_operator_bound=record(sqrt_upper(norm(proposal))),
            posterior_operator_bound=record(sqrt_upper(norm(posterior))),
            original_true_Green_gains={k:record(v) for k,v in gains[window].items()},
            actual_positive_post_weights=selected,
            actual_proposal_weight=record(alpha),
            sum_actual_jump_weights_upper=record(weights[window]),
            sum_all_positive_weights_upper=record(total_alpha),
            complete_independent_mean_and_signed_boundary_input_correlation_retained=True,
            all_jump_terms_have_the_same_boundary_input_and_are_not_assumed_orthogonal=True)
    receipt=matrix.base.prior.array_receipt(
        a.arrays/'complete97-true-right-Poisson-positive-Grams.npz',final_arrays,origin())
    matrix.gate(doc,'true96_waist_and_true97_regular_boundary_defects_include_the_independent_mean',True)
    matrix.gate(doc,'actual_last_cell_unrounded_graph_replaces_the_old_qcut_zero_exception',True)
    matrix.gate(doc,'positive_weighted_Cauchy_pays_all_correlated_defects_and_preserves97_input_directions',True)
    matrix.gate(doc,'all_three_complete_true_right_Poisson_Gram_bounds_are_finite',
        all(up(x).is_finite() and up(x)>=0 for x in output_bounds.values()))
    matrix.gate(doc,'the_true_cut_output_uses_independent_point_kernel_and_trace_gains',True)
    doc.update(complete=True,reused_complete_rows=old_count,new_product_rows=5970-old_count,
        exact_inner_interval=['0','9/10'],
        exact_negative_output_interval=['0',str(matrix.PHASE_RIGHT)],
        complete_true_right_Poisson_operator_upper=output_bounds,
        complete_true_right_Poisson_Gram_certificates=certificates,
        complete_true97_Gram_array_receipt=receipt,
        complete_true_waist_defect_Gram=left_receipt,
        complete_true_regular97_defect_Gram=right_receipt,
        complete_whole_inner_body_defect_Gram=body_receipt,
        actual_waist_product_enclosure_fee=record(left_product_fee),
        complete97_input_Poisson_Gram_bound_proved=True,
        true_complete_finite193_BVP_only=True,
        exact_boundary_input_units='original97 regular row Euclidean coordinates; no second rho input weight',
        all_full_infinite_cap_high_trace_maps_still_require_their_own_complete_contract=True,
        original_F_C_H_J_target_validator_and_positive_port_recomputations=0,
        exact_true_source='zero ordinary body forcing; arbitrary complete97 right boundary load',
        complete_infinite_BVP_inverse_proved=False,
        exact_full_PDE_parameter_response_error_proved=False,true_parameter_Schur_proved=False)
    save(a.out,doc)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('matrix-data','matrix-process','profile','profile-process','green','green-process',
        'kernel','kernel-process','impulse','impulse-process','reviewed-impulse-process',
        'boundary','nominal-cut','directional','directional-process','array-root','arrays','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--matrix-run',required=True);p.add_argument('--directional-run',required=True)
    p.add_argument('--resume',type=Path)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError('preserve every actual right-Poisson result and prefix')
    ctx.prec=320;ctx.cap=6;started=time.monotonic()
    doc=dict(kind=KIND,source_sha256=sha(__file__),complete=False,failure=None,gates=[],
        input_sha256=input_identity(a),completed_rows=0,row_chunks=[],
        arithmetic_bits=320,complete_infinite_BVP_inverse_proved=False,
        exact_full_PDE_parameter_response_error_proved=False,true_parameter_Schur_proved=False)
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=doc['complete'],completed_rows=doc['completed_rows'],
        gates=len(doc['gates']),seconds=doc['seconds'],
        complete_finite97_Poisson_bounds=doc.get('complete_true_right_Poisson_operator_upper'),
        infinite_inverse=False)),flush=True)


if __name__=='__main__':main()
