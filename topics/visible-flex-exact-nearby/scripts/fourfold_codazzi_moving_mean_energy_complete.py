#!/usr/bin/env python3
"""Consume actual saved rows plus complete parts without resetting the mean.

The original failed/incomplete reports stay unchanged. Every input row is
identified against the complete original target/candidate partition. Only
the complete union is propagated and called a full energy certificate.
"""
from __future__ import annotations
import argparse,time
from pathlib import Path
from flint import arb,arb_mat,ctx
from fourfold_codazzi_moving_mean_energy_rows import arguments,prepare,identify
from fourfold_codazzi_moving_mean_energy_prefix_v2 import (
    read,dyadic,target_bounds,polynomial_ranges,moving_jump,comparison_matrix,
    mat_upper,matrix_record,exact_arb,record,save,sha)
from fourfold_codazzi_rotational_cap_jacobi import box_from_record


def main():
    ap=arguments(argparse.ArgumentParser(description=__doc__))
    ap.add_argument('--saved-prefix',type=Path,required=True)
    ap.add_argument('--part',type=Path,action='append',required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320
    if args.out.exists():raise FileExistsError('preserve every full moving-energy consumer attempt')
    context=prepare(args);header=context['header'];old=read(args.saved_prefix)
    source=Path(__file__).with_name('fourfold_codazzi_moving_mean_energy_prefix_v2.py')
    rows_source=Path(__file__).with_name('fourfold_codazzi_moving_mean_energy_rows.py')
    direct_source=Path(__file__).with_name('fourfold_codazzi_moving_mean_energy_direct_rows.py')
    if (old['kind']!='actual_full_Fourier_moving_curvature_angle_mean_energy_v2'
        or old['source_sha256']!=sha(source) or old['complete'] or old['failure'] is not None):
        raise ValueError('the original native complete-row prefix is not the stated unchanged input')
    def same_identity(doc):
        for key in ('object_sha256','candidate_metadata','actual_fixed_nu','exact_amplitude','exact_interval',
                    'parameter_half_width','whole_affine_parameter_interval','complete_primitive_tail',
                    'closed_angular_cells','all_Fourier_variations_retained','independent_allowed_mean_retained'):
            if doc[key]!=header[key]:raise ValueError('a true-target/candidate/mean identity changed: '+key)
        for key,value in header['inputs'].items():
            if doc['inputs'].get(key)!=value:raise ValueError('a complete primary input changed: '+key)
    same_identity(old);parts=[]
    for path in args.part:
        part=read(path);same_identity(part)
        accepted={'actual_moving_mean_energy_complete_row_part':sha(rows_source),
                  'actual_moving_mean_energy_direct_complete_row_part':sha(direct_source)}
        if (part['kind'] not in accepted or not part['complete']
            or part['failure'] is not None or part['source_sha256']!=accepted[part['kind']]
            or part['coefficient_formula_source_sha256']!=sha(source)
            or part['total_common_partition_rows']!=header['total_common_partition_rows']):
            raise ValueError('a named part has not completed the same genuine row contract')
        parts.append((part['first_common_row'],path,part))
    parts.sort(key=lambda p:p[0]);rows=list(old['rows']);cursor=len(rows)
    origins=[dict(input=str(args.saved_prefix),first=0,last=cursor,original_complete=False,
        actual_process_observation='tool session 7649 was unavailable; no exit code or cause is inferred')]
    for first,path,part in parts:
        if first!=cursor or len(part['rows'])!=part['last_common_row_exclusive']-first:
            raise ValueError('the complete saved-row union has a gap, overlap, or missing row')
        if part['exact_requested_subinterval']!=list(map(str,(context['cuts'][first],context['cuts'][part['last_common_row_exclusive']]))):
            raise ValueError('a complete part names a different true radial subinterval')
        for index,row in enumerate(part['rows'],first):
            if row['common_row']!=index:raise ValueError('a completed part changed its original common row number')
            rows.append({k:v for k,v in row.items() if k!='common_row'})
        cursor=part['last_common_row_exclusive'];origins.append(dict(input=str(path),first=first,last=cursor,original_complete=True))
    if cursor!=header['total_common_partition_rows']:
        raise ValueError('the complete actual interval has not yet been certified')
    calculated=[]
    for index,row in enumerate(rows):
        left,right,j,k,actual=identify(context,index)
        if (row['interval']!=list(map(str,(left,right))) or row['candidate_piece']!=j or row['native_row']!=k
            or row['actual_scalar_germ']!=actual['actual_scalar_germ']):
            raise ValueError('a saved completed row belongs to a different actual common partition')
        a=target_bounds(actual,left,right,context['nu'])
        if row['actual_target']!={name:record(a[name]) for name in ('gamma','beta','K','K1')}:
            raise ValueError('a saved row changed its true-target coefficients')
        c={name:box_from_record(value) for name,value in row['bounds'].items()}
        if (not all(v.is_finite() for v in c.values()) or not c['v']<0 or not c['v_abs_lower']>0
            or not c['actual_D']<0 or not c['actual_m']<0 or not c['q']>0
            or not c['actual_R_upper']>=0 or not c['actual_L_upper']>=0):
            raise ValueError('a saved complete moving-energy coefficient gate was lost')
        # Exact identity <v^2>_phi=<v>_theta/D retains the full actual mean.
        y,_=polynomial_ranges(context['saved'],context['nodes'],j,left,right)
        vmean=a['s']+context['alpha']*y[context['m']]
        v2=vmean/c['actual_D']
        if not v2>0:raise ValueError('the complete actual moving L2 v norm is unresolved')
        c['actual_v_L2_phi_upper']=v2.sqrt().upper()
        row['actual_v_L2_phi_upper']=record(c['actual_v_L2_phi_upper'])
        calculated.append(c)
    doc=dict(header,kind='actual_complete_moving_mean_energy_from_saved_rows_and_parts',complete=False,
        source_sha256=sha(__file__),inputs={**header['inputs'],**{str(p):sha(p) for p in (args.saved_prefix,*args.part)}},
        rows=rows,row_origins=origins,jumps=[],failure=None,
        original_reports_preserved_without_changing_completion=True,
        all_exact_common_rows_identified=True,original_finite_BVP_outcome_not_changed=True,
        actual_centre_continuous_PDE_residual_not_certified_here=True,full_body_BVP_inverse_not_proved=True,
        dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            'fourfold_codazzi_moving_mean_energy_prefix_v2.py','fourfold_codazzi_moving_mean_energy_rows.py',
            'fourfold_codazzi_moving_mean_energy_direct_rows.py','fourfold_codazzi_rotational_cap_jacobi.py')})
    try:
        jump_at={};nodes=context['nodes'];cuts=context['cuts']
        for i in range(1,len(calculated)):
            if rows[i-1]['candidate_piece']==rows[i]['candidate_piece']:continue
            j=rows[i]['candidate_piece']
            if nodes[j]!=cuts[i]:raise ValueError('an actual candidate join is missing')
            entry,amount=moving_jump(context['saved'],nodes,j,context['alpha'],context['m'],calculated[i-1],calculated[i])
            doc['jumps'].append(entry);jump_at[i]=arb_mat([[amount[0]],[amount[1]]])
        matrices={};jump_results={}
        for reverse in (False,True):
            exact=arb_mat([[1,0],[0,1]]);uniform=arb_mat([[1,0],[0,1]]);jump=arb_mat([[0],[0]])
            order=range(len(calculated)-1,-1,-1) if reverse else range(len(calculated))
            for i in order:
                entry=jump_at.get(i+1 if reverse else i)
                if entry is not None:jump=mat_upper(jump+entry)
                length=exact_arb(cuts[i+1]-cuts[i]);c=calculated[i]
                flow=mat_upper((comparison_matrix(c,reverse)*length).exp())
                positive_flow=mat_upper((comparison_matrix(c,reverse,True)*length).exp())
                exact=mat_upper(flow*exact);uniform=mat_upper(positive_flow*uniform);jump=mat_upper(flow*jump)
            name='backward' if reverse else 'forward';matrices[name]=(exact,uniform);jump_results[name]=jump
        qmin=min(c['q'].lower() for c in calculated).lower()
        qleft=calculated[0]['q'].lower();qright=calculated[-1]['q'].lower()
        jump_sum=arb_mat([[sum((j[0,0] for j in jump_at.values()),arb(0)).upper()],
                          [sum((j[1,0] for j in jump_at.values()),arb(0)).upper()]])
        bounds={}
        for name,(exact,uniform) in matrices.items():
            qi=qright if name=='backward' else qleft
            bounds[name]=dict(endpoint_matrix=matrix_record(exact),all_subinterval_positive_majorant=matrix_record(uniform),
                complete_initial_energy_endpoint_gain=record((exact[0,0]+exact[0,1]/qi).upper()),
                complete_initial_energy_uniform_gain=record((uniform[0,0]+uniform[0,1]/qi).upper()),
                initial_zero_mean_energy_endpoint_gain=record(exact[0,0].upper()),
                initial_zero_mean_energy_uniform_gain=record(uniform[0,0].upper()),
                full_ordinary_L1_energy_source_uniform_gain=record((uniform[0,0]+uniform[0,1]/qmin).upper()),
                actual_moving_jump_endpoint_energy=record(jump_results[name][0,0]),
                actual_moving_jump_uniform_energy=record((uniform*jump_sum)[0,0].upper()))
        doc.update(complete=True,all_closed_radial_and_angular_boxes_passed=True,
            all_exact_PPoly_moving_jumps_paid=True,bounds=bounds,
            global_bounds={name:record(value) for name,value in dict(q_abs_lower=qmin,
                minimum_actual_v_abs=min(c['v_abs_lower'] for c in calculated).lower(),
                maximum_actual_R=max(c['actual_R_upper'] for c in calculated).upper(),
                maximum_actual_L=max(c['actual_L_upper'] for c in calculated).upper(),
                maximum_actual_v_L2_phi=max(c['actual_v_L2_phi_upper'] for c in calculated).upper(),
                total_actual_moving_energy_jumps=jump_sum[0,0],total_actual_moving_mean_jumps=jump_sum[1,0]).items()})
    except Exception as exc:doc['failure']=dict(type=type(exc).__name__,message=str(exc))
    doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],rows=len(rows),jumps=len(doc['jumps']),
        bounds=doc.get('bounds'),wall_seconds=doc['wall_seconds']),flush=True)
    if not doc['complete']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
