#!/usr/bin/env python3
"""Complete scalar mean-error propagation for joint full trial residuals.

Consumes every true closed radial polynomial row exactly once.  Both
original finite trial mean jumps are retained with their actual direction.
The completed full means are continuous; all nonmean jumps remain in the
body contract.  A complete result certifies residuals, never an inverse.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
import json,time
from flint import arb,ctx
from fourfold_codazzi_correlated_head_residual_rows import (
    KIND as ROW_KIND,prepare,attach_full_trials,read,identity)
from fourfold_codazzi_mean_completed_head_body_residual_v3 import flow,jump_row
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha

KIND='actual_complete_correlated_mean_errors_and_full_body_residuals_v1'
NORMS=('L2','H_one_third','H1')


def f(x):return Fraction.from_float(float(x))


def mean_at(t,r,side):
    nodes=t['nodes'];m=t['m']
    from bisect import bisect_left,bisect_right
    j=(bisect_left(nodes,r)-1 if side=='left' else bisect_right(nodes,r)-1)
    j=max(0,min(j,len(nodes)-2));x=r-nodes[j]
    value=Fraction(0)
    for c in t['full_saved']['piece_coefficients'][:,j,m]:value=value*x+f(c)
    return value


def mean_jumps(t):
    return {r:mean_at(t,r,'right')-mean_at(t,r,'left') for r in t['nodes'][1:-1]}


def actual(c,key):return box_from_record(c[key])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('candidate','mean','response','adjoint'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--waist',type=Path,default=Path('notes/2026-11-14-R133-final-waist-mean-adjoint-column-rational.json'))
    p.add_argument('--amp-multiplier',type=Fraction,default=Fraction(-1))
    p.add_argument('--analytic-width',type=Fraction,default=Fraction(1,2048))
    p.add_argument('--radial-subdivisions',type=int,default=1)
    p.add_argument('--parts',type=Path,nargs='+',required=True)
    p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError('preserve every actual mean-flow outcome')
    ctx.prec=320;ctx.cap=6;started=time.monotonic();c,base=prepare(a)
    full=attach_full_trials(c);n=len(c['cuts'])-1;rows=[];reference=None;inputs={}
    for path in a.parts:
        part=read(path);inputs[str(path)]=sha(path)
        if (part.get('kind')!=ROW_KIND or not part.get('selected_cells_complete')
            or part.get('failure') is not None):raise ValueError('every selected true row part must be complete')
        ident=part['identity']
        producer=Path(__file__).with_name('fourfold_codazzi_correlated_head_residual_rows.py')
        if (ident['source_sha256']!=sha(producer) or part['source_sha256']!=ident['source_sha256']
            or any(sha(Path(__file__).with_name(name))!=value for name,value in ident['dependencies'].items())):
            raise ValueError('the complete actual polynomial producer or its algebra changed')
        if reference is None:reference=ident
        if ident!=reference:raise ValueError('all polynomial parts must have the same actual inputs and source')
        if (ident['original_inputs']!=base['inputs'] or ident['full_trials']!=full
            or ident['total_common_cells']!=n or ident['radial_subdivisions']!=a.radial_subdivisions
            or ident['analytic_width']!=str(a.analytic_width)):
            raise ValueError('the real full trial or full original mean cover changed')
        if part['selected_indices']!=[len(rows),len(rows)+len(part['rows'])]:
            raise ValueError('complete original polynomial parts must be consecutive without repetition')
        if (part['actual_outer_response_mean']!=base['outer_response_mean']
            or part['actual_adjoint_initial_mean']!=base['adjoint_initial_mean']):
            raise ValueError('the true independent mean boundary data changed')
        for row in part['rows']:
            i=len(rows);l,r,k,old,indices=identity(c,i)
            if (row['common_row']!=i or row['interval']!=list(map(str,(l,r)))
                or row['source_mean_row']!=k or row['pieces']!=indices
                or row['actual_original_scalar_germ']!=old['actual_scalar_germ']):
                raise ValueError('a true closed polynomial row changed its domain or identity')
            rows.append(row)
    if len(rows)!=n:raise ValueError('the complete [0,25/8] body cover is required before either flow')
    joins={role:mean_jumps(c[role]) for role in ('response','adjoint')}
    doc=dict(kind=KIND,complete=False,failure=None,inputs=inputs,source_sha256=sha(__file__),
        row_identity=reference,candidate_sha256=reference['candidate_sha256'],
        complete_original_common_cells=n,exact_interval=['0','25/8'],
        original_ac1_operator_not_relabelled_as_continuous_repair=True,
        full_trial_mean_jumps={name:[dict(radius=str(r),exact_jump=str(v)) for r,v in js.items()]
                              for name,js in joins.items()},
        adjoint_error_flow=[],response_error_reverse=[],residual_rows=[],
        response_nonmean_jumps=[],adjoint_nonmean_jumps=[],complete_BVP_inverse_proved=False,
        true_nu_Schur_nonzero_proved=False)
    try:
        initial=box_from_record(base['adjoint_initial_mean'])-exact_arb(mean_at(c['adjoint'],Fraction(0),'right'))
        for i,row in enumerate(rows):
            l,r=map(Fraction,row['interval']);cm=actual(row,'scalar_cm')
            end,entire=flow(-cm,actual(row,'adjoint_mean_residual'),initial,r-l)
            jump=joins['adjoint'].get(r,Fraction(0));next_initial=end-exact_arb(jump)
            doc['adjoint_error_flow'].append(dict(common_row=i,interval=row['interval'],
                left=record(initial),right_before_jump=record(end),entire=record(entire),
                exact_mean_jump_subtracted_at_right=str(jump),right_after_jump=record(next_initial)))
            initial=next_initial
        initial=box_from_record(base['outer_response_mean'])-exact_arb(mean_at(c['response'],Fraction(25,8),'left'))
        for i in range(n-1,-1,-1):
            row=rows[i];l,r=map(Fraction,row['interval']);jump=joins['response'].get(r,Fraction(0))
            before=initial+exact_arb(jump);cm=actual(row,'scalar_cm')
            end,entire=flow(-cm,actual(row,'response_mean_residual'),before,r-l)
            doc['response_error_reverse'].append(dict(common_row=i,interval=row['interval'],
                right_after_jump=record(initial),exact_mean_jump_added_before_backward_step=str(jump),
                right_before_jump=record(before),left=record(end),entire=record(entire)))
            initial=end
        sums={role:{norm:arb(0) for norm in NORMS} for role in ('response','adjoint')}
        sup={role:arb(0) for role in sums};asup=dict(sup);aL1=dict(sup);signed=arb(0)
        for i,row in enumerate(rows):
            l,r=map(Fraction,row['interval']);length=exact_arb(r-l)
            ez=actual(doc['response_error_reverse'][n-1-i],'entire')
            emu=actual(doc['adjoint_error_flow'][i],'entire')
            out=dict(common_row=i,interval=row['interval'],response_mean_error=record(ez),adjoint_mean_error=record(emu))
            for role,error,key,col in (
                ('response',ez,'uncorrected_response_nonmean','actual_A_e2_nonmean'),
                ('adjoint',emu,'uncorrected_adjoint_nonmean','actual_Astar_e2_nonmean')):
                e=abs(error).upper();bounds={}
                for norm in NORMS:
                    b=(actual(row[key],norm+'_L2_radial')+e*actual(row[col],norm+'_L2_radial')).upper()
                    bs=(actual(row[key],norm+'_sup')+e*actual(row[col],norm+'_sup')).upper()
                    bounds[norm+'_L2_radial']=record(b);bounds[norm+'_sup']=record(bs)
                    sums[role][norm]+=b*b
                    if norm=='L2':sup[role]=max(sup[role],bs).upper()
                aa=(actual(row[key],'A_sigma_sup')+e*actual(row[col],'A_sigma_sup')).upper()
                bounds['A_sigma_sup']=record(aa);asup[role]=max(asup[role],aa).upper();aL1[role]+=length*aa
                out[role+'_complete_nonmean_residual']=bounds
            piece=actual(row,'signed_full_trial_dual_response_nonmean_integral')-length*actual(row,'signed_adjoint_nonmean_Ae2_range')*ez
            out['signed_complete_dual_response_residual_integral']=record(piece);signed+=piece
            out['exact_response_mean_residual']=0;out['exact_adjoint_mean_residual']=0
            doc['residual_rows'].append(out)
        for role in ('response','adjoint'):
            for j in range(1,len(c[role]['nodes'])-1):doc[role+'_nonmean_jumps'].append(jump_row(c,role,j))
        summary={}
        for role in sums:
            summary[role]={norm+'_L2_radial':record(v.sqrt().upper()) for norm,v in sums[role].items()}
            summary[role].update(L2_sup=record(sup[role]),A_sigma_sup=record(asup[role]),A_sigma_L1_radial=record(aL1[role].upper()))
            allj={norm:arb(0) for norm in ('A0','A_sigma','L2','H_one_third','H1')}
            for row in doc[role+'_nonmean_jumps']:
                for norm in allj:allj[norm]+=box_from_record(row['full_nonmean_jump'][norm]).upper()
            summary[role]['complete_nonmean_jump_l1']={k:record(v.upper()) for k,v in allj.items()}
        mu0=box_from_record(base['adjoint_initial_mean'])
        zR=box_from_record(base['outer_response_mean'])
        z0=actual(doc['response_error_reverse'][-1],'left')+exact_arb(mean_at(c['response'],Fraction(0),'right'))
        muR=actual(doc['adjoint_error_flow'][-1],'right_before_jump')+exact_arb(mean_at(c['adjoint'],Fraction(25,8),'left'))
        doc.update(complete=True,summary=summary,
            signed_body_dual_response_residual_integral=record(signed),
            true_completed_mean_traces={k:record(v) for k,v in dict(response_0=z0,response_R=zR,adjoint_0=mu0,adjoint_R=muR).items()},
            exact_continuous_completed_means=True,
            complete_mean_residuals_exactly_zero=True,
            all_original_nonmean_PPoly_jumps_retained=True,
            actual_complete_body_residual_only=True)
    except Exception as exc:
        doc['failure']=dict(type=type(exc).__name__,message=str(exc));raise
    finally:
        doc['wall_seconds']=time.monotonic()-started;save(a.out,doc)
    print(dict(complete=doc['complete'],rows=n,wall_seconds=doc['wall_seconds']),flush=True)


if __name__=='__main__':main()
