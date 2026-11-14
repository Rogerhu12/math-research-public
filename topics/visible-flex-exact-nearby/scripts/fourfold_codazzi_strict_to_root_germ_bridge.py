#!/usr/bin/env python3
"""Actual strict moving bridge to the common root germ and physical ports.

Only the exterior [0.238, common-root-germ left endpoint] is treated. The
last actual PPoly jump into the root piece is retained. All H0/H1 and mean
rows are paid; the root-germ turning analysis is a separate same-candidate
operator. No curved Airy port is identified with a fixed radial circle.
"""
from __future__ import annotations
import argparse,json,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
from flint import arb,arb_mat,ctx
from fourfold_phase_codazzi_coefficients import CodazziCoefficientTarget
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_reciprocal_candidate_tools import COORDINATES
from fourfold_codazzi_moving_mean_energy_prefix_v2 import (
    read,dyadic,polynomial_ranges,row_coefficients,moving_jump,mat_upper,matrix_record,
    exact_arb,record,save,sha)
from fourfold_codazzi_moving_sobolev_rows import StrongDirectSums,derivative_budget
from fourfold_codazzi_moving_sobolev_complete import three_matrix,norm_gains,derivative_jump


def physical_inverse_port(c):
    q=c['q'].lower();g=c['v_abs_lower'];V=c['v_abs_upper']
    mlo=abs(c['actual_m']).lower();mhi=abs(c['actual_m']).upper()
    V2=c['actual_v_L2_phi_upper'];L=c['actual_L_upper'];L2=c['actual_Q_phi_phi_energy_upper']
    Vp=c['actual_v_phi_absolute'];a=1/(4*g*q);b=V2/(4*g*mlo)
    c0=(V/mlo).sqrt().upper();c1=(mhi/g).sqrt().upper()
    W=L2+L*Vp/g
    P=arb_mat([[c0*(1+L*a),c0*L*b,0],
               [c1*(L/(g*q)+W*a),c1*(L/mlo+W*b),c1]])
    return mat_upper(P)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--root',type=Path,default=Path('notes/2026-11-13-R133-actual-root-and-three-common-germs-native.json.gz'))
    ap.add_argument('--energy',type=Path,default=Path('notes/2026-11-13-R133-moving-mean-energy-alpha075-r0238-complete-native.json.gz'))
    ap.add_argument('--angles',type=int,default=4096);ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320;ctx.cap=4
    if args.out.exists():raise FileExistsError('preserve the actual strict exterior bridge')
    root=read(args.root);energy=read(args.energy);saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']))
    if (not root['complete'] or not energy['complete'] or meta['coordinates']!=COORDINATES
        or meta['object_sha256']!=sha(args.object) or energy['candidate_metadata']!=meta
        or energy['inputs'].get(str(args.candidate))!=sha(args.candidate)
        or root['parameter_half_width']!=energy['parameter_half_width']
        or not any(r['candidate_sha256']==sha(args.candidate) for r in root['candidate_germs'])):
        raise ValueError('the complete prefix and true root must use this exact actual candidate')
    left=Fraction(119,500);right=Fraction(root['common_real_analytic_germ'][0])
    if energy['exact_interval']!=['0',str(left)] or not left<right<Fraction(root['exact_root_interval'][0]):
        raise ValueError('the bridge must end strictly before the same true root')
    nodes=list(map(dyadic,saved['radial_nodes']));m=int(meta['modes']);alpha=exact_arb(dyadic(meta['amplitude']))
    target=CodazziCoefficientTarget(args.object,Fraction(root['parameter_half_width']),512,4096)
    sampler=StrongDirectSums(m,args.angles)
    cuts=sorted({left,right}|{r for r in nodes if left<r<right})
    context=dict(saved=saved,nodes=nodes,m=m,alpha=alpha)
    doc=dict(kind='actual_strict_moving_H1_bridge_to_common_root_germ',complete=False,source_sha256=sha(__file__),
        inputs={str(p):sha(p) for p in (args.candidate,args.object,args.root,args.energy)},
        object_sha256=sha(args.object),candidate_metadata=meta,exact_interval=list(map(str,(left,right))),
        parameter_half_width=root['parameter_half_width'],whole_affine_parameter_interval=True,
        complete_primitive_tail=True,closed_angular_cells=args.angles,all_Fourier_variations_and_mean_retained=True,
        no_extrapolation_into_root_common_germ=True,curved_Airy_port_not_treated_as_fixed_r=True,
        rows=[],terminal_right_side=None,jumps=[],failure=None,
        dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            'fourfold_phase_codazzi_coefficients.py','fourfold_codazzi_candidate_shards.py',
            'fourfold_codazzi_moving_mean_energy_prefix_v2.py','fourfold_codazzi_moving_mean_energy_direct_rows.py',
            'fourfold_codazzi_moving_sobolev_rows.py','fourfold_codazzi_moving_sobolev_complete.py')})
    def evaluate(lo,hi,piece):
        c=target.coefficients(lo,hi);gap=c['E']-c['a1']**2
        if not c['K']<0 or not gap>0:raise ValueError('the entire real strict bridge target/chart gate is unresolved')
        a=dict(gamma=c['gamma'],beta=c['beta'],K=c['K'],K1=c['K1'],s=-c['a']*(c['E']/gap).sqrt())
        y,_=polynomial_ranges(saved,nodes,piece,lo,hi);fields,node_fields=sampler.fields(y,alpha,a['s'])
        b=row_coefficients(fields[:5],node_fields[:5],a,args.angles)
        b.update(derivative_budget(fields,a,b));b['actual_v_L2_phi_upper']=((a['s']+alpha*y[m])/b['actual_D']).sqrt().upper()
        return b,dict(interval=list(map(str,(lo,hi))),candidate_piece=piece,
            actual_scalar_germ=list(map(str,target.cell)),true_target_coefficients={k:record(v) for k,v in c.items()},
            bounds={k:record(v) for k,v in b.items()})
    calculated=[]
    try:
        for lo,hi in zip(cuts,cuts[1:]):
            piece=min(bisect_right(nodes,lo)-1,len(nodes)-2)
            if not nodes[piece]<=lo<hi<=nodes[piece+1]:raise ValueError('the strict bridge crosses a candidate polynomial germ')
            b,row=evaluate(lo,hi,piece);calculated.append(b);doc['rows'].append(row)
        endpoint_piece=bisect_right(nodes,right)-1
        endpoint,terminal=evaluate(right,right,endpoint_piece);doc['terminal_right_side']=terminal
        # Include the genuine final jump into the right-hand root PPoly germ.
        all_bounds=calculated+[endpoint];all_pieces=[r['candidate_piece'] for r in doc['rows']]+[endpoint_piece]
        jump_at={}
        for i in range(1,len(all_bounds)):
            if all_pieces[i-1]==all_pieces[i]:continue
            j=all_pieces[i]
            if nodes[j]!=(right if i==len(calculated) else cuts[i]):raise ValueError('an exact strict bridge interface is missing')
            entry,amount=moving_jump(saved,nodes,j,alpha,m,all_bounds[i-1],all_bounds[i])
            stronger,J1=derivative_jump(context,j,all_bounds[i-1],all_bounds[i],all_bounds[i-1],all_bounds[i],entry)
            entry.update(stronger);doc['jumps'].append(entry);jump_at[i]=arb_mat([[amount[0]],[amount[1]],[J1]])
        results={};qmin=min(b['q'].lower() for b in all_bounds).lower()
        total=arb_mat([[sum((v[j,0] for v in jump_at.values()),arb(0)).upper()] for j in range(3)])
        for reverse in (False,True):
            end=arb_mat([[1,0,0],[0,1,0],[0,0,1]]);U=arb_mat([[1,0,0],[0,1,0],[0,0,1]])
            J=arb_mat([[0],[0],[0]]);order=range(len(calculated)-1,-1,-1) if reverse else range(len(calculated))
            for i in order:
                extra=jump_at.get(i+1 if reverse else i)
                if extra is not None:J=mat_upper(J+extra)
                length=exact_arb(cuts[i+1]-cuts[i]);b=calculated[i]
                flow=mat_upper((three_matrix(b,b,reverse)*length).exp())
                upflow=mat_upper((three_matrix(b,b,reverse,True)*length).exp())
                end=mat_upper(flow*end);U=mat_upper(upflow*U);J=mat_upper(flow*J)
            if not reverse and len(calculated) in jump_at:J=mat_upper(J+jump_at[len(calculated)])
            qi=endpoint['q'].lower() if reverse else calculated[0]['q'].lower()
            jump=mat_upper(U*total)
            results['backward' if reverse else 'forward']=dict(endpoint_matrix=matrix_record(end),
                all_subinterval_positive_majorant=matrix_record(U),
                complete_initial_uniform_gains={k:record(v) for k,v in norm_gains(U,qi).items()},
                complete_ordinary_L1_source_gains={k:record(v) for k,v in norm_gains(U,qmin).items()},
                actual_moving_jump_uniform_H0=record(jump[0,0]),
                actual_moving_jump_uniform_H1=record((jump[0,0]**2+jump[2,0]**2).sqrt().upper()),
                actual_moving_jump_endpoint_vector=matrix_record(J))
        port=physical_inverse_port(endpoint)
        doc.update(complete=True,bounds=results,terminal_moving_to_physical_H0_H1_port_matrix=matrix_record(port),
            terminal_port_input_order=['E0','absolute_mean','E1'],terminal_port_output_order=['physical_theta_E0','physical_theta_E1'],
            terminal_physical_source_and_target_identity_preserved=True,
            terminal_candidate_piece=endpoint_piece,terminal_exact_root_germ=list(map(str,nodes[endpoint_piece:endpoint_piece+2])),
            all_actual_terminal_PPoly_jumps_paid=True)
    except Exception as exc:doc['failure']=dict(type=type(exc).__name__,message=str(exc))
    doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],rows=len(doc['rows']),jumps=len(doc['jumps']),
        interval=doc['exact_interval'],bounds=doc.get('bounds'),wall_seconds=doc['wall_seconds']),flush=True)
    if not doc['complete']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
