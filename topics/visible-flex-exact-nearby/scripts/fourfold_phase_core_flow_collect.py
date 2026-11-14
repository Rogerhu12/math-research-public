#!/usr/bin/env python3
"""Assemble the complete parameter-uniform finite physical core transfer.

All original common spans and all accepted subdivisions are required. The
true local errors are propagated through exact finite reference prefixes,
then exact radial reflection gives both physical Cauchy channels. Only the
finite angular DN conversion is tested; no infinite-core DN or high Schur
inverse is assumed.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import time
import traceback
import numpy as np
from flint import arb,acb,acb_mat,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_core_cell_flow import exact_matrix,identity,real_midpoint,ball_record
from fourfold_phase_low_feedback_paid_inputs import norm as matrix_norm,adjoint

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    def reject(value):raise ValueError('nonfinite JSON constant '+value)
    return json.loads(Path(path).read_text(),parse_constant=reject)
def write(path,value):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
def norm(value):
    answer=matrix_norm(value)
    if not answer.is_finite():raise ValueError('nonfinite certified matrix norm')
    return answer
def sub(value,r0,r1,c0,c1):
    return acb_mat([[value[i,j] for j in range(c0,c1)] for i in range(r0,r1)])
def join(a,b,c,d):
    n=a.nrows();out=acb_mat(2*n,2*n)
    for i in range(n):
        for j in range(n):
            out[i,j],out[i,n+j]=a[i,j],b[i,j]
            out[n+i,j],out[n+i,n+j]=c[i,j],d[i,j]
    return out
def product_bound(sequence,dimension,label):
    """P_j^-1 (T_j_true-T_j) P_{j-1} pays every ordered factor."""
    prefix=identity(dimension);previous_norm=arb(1);action=arb(0);rows=[]
    largest_condition=arb(0)
    for index,(center,error,metadata) in enumerate(sequence):
        prefix=center*prefix
        pinv=prefix.inv()
        pn,qn=norm(prefix),norm(pinv)
        beta=(qn*error*previous_norm).upper()
        action+=beta
        largest_condition=max(largest_condition,(pn*qn).upper())
        rows.append(dict(step=index,source=metadata,prefix_norm=ball_record(pn),
            inverse_prefix_norm=ball_record(qn),local_transfer_error=ball_record(error),
            ordered_relative_increment=ball_record(beta)))
        previous_norm=pn
    error=(previous_norm*(action.exp()-1)).upper()
    return prefix,error,dict(label=label,steps=len(sequence),
        total_ordered_relative_action=ball_record(action.upper()),
        final_reference_norm=ball_record(previous_norm),
        largest_reference_prefix_condition=ball_record(largest_condition),
        true_transfer_error=ball_record(error)),rows

def validate(manifests):
    pieces=[];identity0=None
    for path in manifests:
        doc=read(path)
        if not doc.get('complete') or doc.get('terminal_failures'):
            raise ValueError('incomplete core piece: '+str(path))
        if doc.get('kind')!='complete_piece_of_true_uniform_core_flow':
            raise ValueError('unexpected core piece schema')
        ident=doc['identity']
        if identity0 is None:identity0=ident
        elif ident!=identity0:raise ValueError('different core family or source identities')
        pieces.append((doc['first_span'],doc,path))
    pieces.sort()
    expected=0;original=[];leaves=[];manifest_records=[]
    for first,doc,path in pieces:
        if first!=expected or not first<doc['last_span_exclusive']:
            raise ValueError('common-span pieces have a gap or overlap')
        expected=doc['last_span_exclusive']
        original+=doc['original_spans'];leaves+=doc['complete_leaves']
        manifest_records.append(dict(path=str(path),sha256=sha(path)))
    if expected!=identity0.get('total_original_common_spans',pieces[0][1]['total_original_common_spans']):
        raise ValueError('the complete original common-span count was not supplied')
    if any(doc['total_original_common_spans']!=expected for _,doc,_ in pieces):
        raise ValueError('different declared original common-span counts')
    if [row['index'] for row in original]!=list(range(expected)):
        raise ValueError('not exactly all original common spans are present')
    cursor=Fraction(0)
    for row in original:
        a,b=map(Fraction,row['exact_interval'])
        if a!=cursor or not a<b:raise ValueError('original common cells have a gap')
        cursor=b
    if cursor!=Fraction(1,4):raise ValueError('the complete core half does not end at 1/4')
    here=Path(__file__).parent
    for name,digest in identity0['dependency_sha256'].items():
        if sha(here/name)!=digest:raise ValueError('core producer dependency changed: '+name)
    if sha(here/'fourfold_phase_core_flow_cover.py')!=identity0['worker_source_sha256']:
        raise ValueError('core worker changed')
    if sha(identity0['object_path'])!=identity0['object_sha256']:
        raise ValueError('central exact affine object changed')
    if not identity0.get('uniform_in_the_entire_real_parameter_interval'):
        raise ValueError('a center-only result is not a whole-family certificate')
    leaves.sort(key=lambda row:Fraction(row['exact_interval'][0]))
    cursor=Fraction(0);loaded=[];leaf_records=[]
    n=2*(2*identity0['modes']+1)
    for leaf in leaves:
        a,b=map(Fraction,leaf['exact_interval'])
        if a!=cursor or not a<b:raise ValueError('accepted real intervals have a gap or overlap')
        cursor=b;path=Path(leaf['path'])
        if sha(path)!=leaf['sha256']:raise ValueError('leaf report changed: '+str(path))
        doc=read(path)
        if not doc.get('complete') or doc.get('stage')!='actual_local_transfer_complete':
            raise ValueError('an accepted leaf is not a completed true local flow')
        expected_identity=dict(**identity0,common_span_index=leaf['index'],
            exact_common_span=original[leaf['index']]['exact_interval'],
            exact_real_interval=leaf['exact_interval'])
        if doc['cover_identity']!=expected_identity:
            raise ValueError('leaf identity differs from its exact cover')
        if doc['arrays']!=leaf['arrays']:raise ValueError('leaf arrays identity differs')
        ap=Path(doc['arrays']['path'])
        if sha(ap)!=doc['arrays']['sha256']:raise ValueError('leaf array changed')
        with np.load(ap,allow_pickle=False) as data:
            transfer=np.array(data['exact_dyadic_local_transfer_center'],copy=True)
            gen=data['exact_dyadic_generator_coefficients']
            if transfer.shape!=(n,n) or gen.shape!=(identity0['time_terms'],n,n):
                raise ValueError('local state dimensions differ')
            if np.any(~np.isfinite(transfer)) or np.any(~np.isfinite(gen)):
                raise ValueError('local arrays contain a nonfinite coefficient')
        eps=arb(doc['true_scaled_local_transfer_operator_error']['ball']).upper()
        if not eps.is_finite() or eps<0:raise ValueError('invalid true local error')
        if doc['true_scaled_local_transfer_operator_error']!=leaf['transfer_error']:
            raise ValueError('manifest local error differs')
        loaded.append((exact_matrix(transfer),eps,dict(path=str(path),
            index=leaf['index'],word=leaf['word'])))
        leaf_records.append(dict(path=str(path),sha256=sha(path),arrays=doc['arrays'],
            exact_interval=leaf['exact_interval'],transfer_error=ball_record(eps)))
    if cursor!=Fraction(1,4):raise ValueError('accepted intervals miss the quarter cut')
    return identity0,loaded,manifest_records,leaf_records

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cover-root',type=Path,required=True)
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--old-core',type=Path,default=Path('notes/2026-11-12-actual-core-low-block-M4.json'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits
    wall,cpu=time.monotonic(),time.process_time()
    report=dict(kind='complete_uniform_finite_physical_core_transfer_and_DN',
        complete=False,source_sha256=sha(__file__),bits=args.bits,
        rigorous_infinite_core_DN_inverse=False,rigorous_full_Schur_inverse=False)
    traces=[]
    try:
        manifests=sorted(args.cover_root.glob('block_*/manifest.json'))
        if not manifests:raise ValueError('no complete core pieces')
        ident,positive,inputs,leaves=validate(manifests)
        report.update(identity=ident,input_manifests=inputs,
            original_common_spans=sum(len(read(p)['original_spans']) for p in manifests),
            accepted_real_leaves=len(positive),exact_physical_cuts=['-1/4','1/4'],
            full_Cauchy_channels_retained=True,angular_mean_retained=True)
        n=2*ident['modes']+1;d=2*n
        scale=exact_arb(Fraction(ident['momentum_scale']))
        J=identity(d)
        for k in range(n,d):J[k,k]=-1
        P,eperp,half,trace=product_bound(positive,d,'positive half')
        traces+=trace;report['positive_half']=half
        p,q=norm(P),norm(P.inv())
        if not q*eperp<1:
            raise ValueError('true half inverse perturbation not paid')
        full_center=P*J*P.inv()*J
        reflection_error=(eperp*q*(1+p*q)/(1-q*eperp)).upper()
        negative=[]
        for center,error,meta in reversed(positive):
            inverse=center.inv();bound=norm(inverse)
            if not bound*error<1:
                raise ValueError('true local inverse perturbation not paid')
            fee=(bound*bound*error/(1-bound*error)).upper()
            negative.append((J*inverse*J,fee,dict(**meta,reflected_inverse=True)))
        full2,eordered,whole,trace=product_bound(negative+positive,d,'full ordered reflection')
        traces+=trace
        # Both full_center and full2 enclose the same exact rational expression.
        mismatch=norm(full_center-full2)
        full_error=min(reflection_error,eordered+mismatch).upper()
        report.update(reflection_formula='P J P^{-1} J, J=diag(I,-I) in the state (w,p/scale)',
            full_ordered=whole,half_to_full_reflection_error=ball_record(reflection_error),
            same_exact_reference_enclosure_comparison=ball_record(mismatch),
            true_full_scaled_transfer_error=ball_record(full_error))
        A,B,C,D=sub(full_center,0,n,0,n),sub(full_center,0,n,n,d),sub(full_center,n,d,0,n),sub(full_center,n,d,n,d)
        Q=B.inv();qa=norm(Q);an,dn=norm(A),norm(D)
        if not qa*full_error<1:
            raise ValueError('finite DN B-block inverse perturbation not below one')
        qt=(qa/(1-qa*full_error)).upper()
        dq=(qa*qa*full_error/(1-qa*full_error)).upper()
        e11=(dq*an+qt*full_error).upper()
        e12=dq
        e22=(dn*dq+full_error*qt).upper()
        e21=(full_error+full_error*qt*(an+full_error)+dn*e11).upper()
        dn_error=(scale*(e11*e11+e12*e12+e21*e21+e22*e22).sqrt()).upper()
        DN=scale*join(Q*A,-Q,C-D*Q*A,D*Q)
        # The true finite DN is Hermitian. Hermitian projection contracts the
        # operator error; it does not assume the rational reference is exact.
        sym=(DN+adjoint(DN))/2
        saved=real_midpoint(sym)
        saved=(saved+saved.T)/2
        # This last binary average is separately included in the selection fee.
        selection=norm(sym-exact_matrix(saved))
        total=(dn_error+selection).upper()
        report.update(finite_projected_DN_certified=True,
            finite_B_inverse_norm=ball_record(qa),finite_B_inverse_perturbation_product=ball_record(qa*full_error),
            actual_finite_core_DN_error=ball_record(total),
            DN_before_binary_choice_error=ball_record(dn_error),
            exact_Hermitian_projection_selection_error=ball_record(selection),
            reference_DN_antisymmetric_norm=ball_record(norm(DN-adjoint(DN))/2),
            raw_DN_port_order='left outward -p, right outward +p; all 4k retained heights, including both means',
            physical_momentum_scale=str(Fraction(ident['momentum_scale'])))
        arrays=args.out.with_suffix('.npz')
        arrays.parent.mkdir(parents=True,exist_ok=True)
        np.savez_compressed(arrays,core_DN=saved,
            exact_dyadic_positive_half_center=real_midpoint(P),
            exact_dyadic_full_scaled_transfer_center=real_midpoint(full_center))
        report['arrays']=dict(path=str(arrays),sha256=sha(arrays),bytes=arrays.stat().st_size,
            definition='The core_DN array is an exact dyadic Hermitian center with the stated complete operator radius. The two transfer arrays are diagnostic rounded centers; their additional selection errors are recorded below.')
        report['positive_half_saved_selection_error']=ball_record(norm(P-exact_matrix(real_midpoint(P))))
        report['full_transfer_saved_selection_error']=ball_record(norm(full_center-exact_matrix(real_midpoint(full_center))))
        if args.old_core.exists():
            old=read(args.old_core);record=old['arrays']
            if old['object_sha256']!=ident['object_sha256'] or sha(record['path'])!=record['sha256']:
                raise ValueError('old floating comparison belongs to different inputs')
            with np.load(record['path'],allow_pickle=False) as data:
                old_center=exact_matrix(data['core_DN'])
            comparison=norm(exact_matrix(saved)-old_center)
            report['old_floating_core_comparison']=dict(path=str(args.old_core),sha256=sha(args.old_core),
                chosen_center_difference=ball_record(comparison),
                true_uniform_DN_minus_old_raw_center_upper=ball_record((comparison+total).upper()),
                old_result_scope='Only a floating diagnostic; the new uniform proof does not assume it exact.')
        report['complete']=True
        report['scope']=[
            'Every real point of [-1/4,1/4] and every parameter in the explicit eta interval is covered for the actual finite projected generator.',
            'The complete finite DN conversion is proved at the two physical quarter cuts, with both angular means retained.',
            'This does not assert the full infinite core Dirichlet problem is invertible. High-channel body residuals and complete high Schur feedback remain separate.']
    except Exception as exc:
        report.update(failure=repr(exc),traceback=traceback.format_exc())
    report.update(CPU_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-wall,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_core_cell_flow.py','fourfold_phase_core_flow_cover.py',
            'fourfold_phase_low_feedback_paid_inputs.py','fourfold_phase_cap_energy_collect.py')})
    if traces:
        tp=args.out.with_suffix('.prefix-trace.json.gz')
        tp.parent.mkdir(parents=True,exist_ok=True)
        with gzip.GzipFile(filename=str(tp),mode='wb',mtime=0) as f:
            f.write((json.dumps(traces,sort_keys=True,allow_nan=False)+'\n').encode())
        report['complete_ordered_prefix_trace']=dict(path=str(tp),sha256=sha(tp),bytes=tp.stat().st_size)
    write(args.out,report)
    print(json.dumps({key:report.get(key) for key in ('complete','original_common_spans',
        'accepted_real_leaves','true_full_scaled_transfer_error','actual_finite_core_DN_error',
        'old_floating_core_comparison','failure','CPU_seconds','wall_seconds')},indent=2,allow_nan=False),flush=True)
    if not report['complete']:raise SystemExit(1)
if __name__=='__main__':main()
