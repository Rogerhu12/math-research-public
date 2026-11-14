#!/usr/bin/env python3
"""Complete mean and H1 Cauchy/source energy for the actual moving centre.

The centre is finite in moving phi, not physical theta.  Every original
target box and the exact chosen nu are retained.  Direct whole-cell angular
sums enclose R,L,L2; the exact finite phi mean replaces inverse-angle
quadrature.  Infinite Fourier variations and the independent mean evolve
in a full four-state comparison.  PPoly jumps are paid in this same phi
coordinate.  Physical variation/port conversion is a separate contract.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
import json
from pathlib import Path
import time

from flint import arb, arb_mat, ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_curvature_angle_energy_prefix import (
    read, dyadic, target_bounds, polynomial_ranges, actual_jump)
from fourfold_codazzi_moving_actual_R_boundary import COORDINATES
from fourfold_codazzi_moving_sobolev_rows import StrongDirectSums
from fourfold_codazzi_moving_mean_energy_prefix_v2 import (
    upper, lower, maxabs, interval, arb_box, square_box,
    mat_upper, matrix_record, comparison_matrix)
from fourfold_codazzi_moving_sobolev_complete import three_matrix, norm_gains
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha


KIND = 'actual_final_moving_centre_full_mean_H1_Y2_strict_energy'


def direct_coefficients(y, fields, a, alpha, modes):
    u,v,up,vp,vpp,upp = fields
    if not upper(v) < 0:
        raise ValueError('the complete moving centre lost its negative-v chart')
    K, beta = arb_box(a['K']), arb_box(a['beta'])
    mean = a['s']+alpha*y[modes]
    if not mean < 0:
        raise ValueError('the actual moving mean is not strictly negative')
    # Complete orthogonality in phi, including the actual V0 and all modes.
    mean_u2 = alpha**2*sum((z*z for z in y[:modes]),arb(0))/2
    mean_v2 = mean**2+alpha**2*sum((z*z for z in y[modes+1:]),arb(0))/2
    Smean = mean_u2+a['K']*mean_v2
    Smean = Smean.intersection(interval(square_box(u)+K*square_box(v)))
    dphi = beta*(arb_box(Smean)-square_box(u)-K*square_box(v))
    R = upper(square_box(u)-K*square_box(v)).sqrt().upper()
    L = upper(square_box(up)-K*square_box(vp)).sqrt().upper()
    L2 = upper(square_box(upp)-K*square_box(vpp)).sqrt().upper()
    up_abs, vp_abs = maxabs(up), maxabs(vp)
    angle_J = v/arb_box(mean)
    if not lower(angle_J)>0:raise ValueError('the complete physical angle Jacobian is not positive')
    diagonal1 = -beta*(1+3*square_box(u)+K*square_box(v))
    diagonal2 = beta*(1-square_box(u)-3*K*square_box(v))+arb_box(a['K1']/(2*a['K']))
    G01, G02 = diagonal1-dphi/2, diagonal2-dphi/2
    G11, G12 = diagonal1+dphi/2, diagonal2+dphi/2
    primitive_fee = (abs(a['beta'])*R*L/2).upper()
    q = (-a['K']).sqrt()
    base = dict(actual_m=mean, actual_D=1/mean,
                actual_S_mean=Smean, actual_v_L2=mean_v2.sqrt(),
                actual_R_upper=R, actual_L_upper=L,
                full_u_phi_absolute=up_abs, full_v_phi_absolute=vp_abs,
                physical_angle_J_lower=lower(angle_J), physical_angle_J_upper=upper(angle_J),
                actual_d_phi=interval(dphi), q=q,
                actual_v=interval(v), v_abs_lower=(-upper(v)).lower(),
                v_abs_upper=(-lower(v)).upper(),
                forward_rate=(max(upper(G01),upper(G02))+primitive_fee).upper(),
                backward_rate=(max(-lower(G01),-lower(G02))+primitive_fee).upper(),
                coupling_mean_to_energy=(a['gamma']*q*L).upper(),
                coupling_energy_to_mean=(2*abs(a['beta']*mean)*R).upper(),
                forward_mean_rate=(a['beta']*(1-Smean)).upper(),
                backward_mean_rate=(-a['beta']*(1-Smean)).upper(),
                nonlocal_primitive_energy_fee=primitive_fee,
                forward_diagonal_1=interval(G01), forward_diagonal_2=interval(G02))
    strong = dict(actual_Q_phi_phi_energy_upper=L2,
                  forward_derivative_rate=max(upper(G11),upper(G12)).upper(),
                  backward_derivative_rate=max(-lower(G11),-lower(G12)).upper(),
                  coupling_E0_to_E1=(abs(a['beta'])*R*(10*L+L2/2)).upper(),
                  coupling_mean_to_E1=(a['gamma']*q*L2).upper(),
                  coupling_E0_to_Y2=(2*abs(a['beta'])*maxabs(u*v)+abs(a['beta'])*R*vp_abs/2).upper(),
                  coupling_mean_to_Y2=(a['gamma']*up_abs).upper(),
                  coupling_E1_to_Y2=abs(a['gamma']*mean).upper(),
                  forward_Y2_rate=upper(beta*(1-square_box(u)-3*K*square_box(v))-dphi/2),
                  backward_Y2_rate=(-lower(beta*(1-square_box(u)-3*K*square_box(v))-dphi/2)).upper())
    return base, strong


def four_matrix(base,strong,reverse=False,positive=False):
    core=three_matrix(base,strong,reverse,positive)
    g=strong['backward_Y2_rate' if reverse else 'forward_Y2_rate']
    if positive:g=max(arb(0),g).upper()
    rows=[[core[i,j] for j in range(3)]+[arb(0)] for i in range(3)]
    rows.append([strong['coupling_E0_to_Y2'],strong['coupling_mean_to_Y2'],
                 strong['coupling_E1_to_Y2'],g])
    return arb_mat(rows)


def ordinary_three_channel_gain(U,q_upper):
    # Full ordinary H1 input/source, without division by the turning weight.
    w=max(arb(1),q_upper).upper()
    injection=arb_mat([[w,0],[1,0],[0,w],[1,0]])
    product=mat_upper(U*injection)
    return sum((product[i,j]**2 for i in (0,2,3) for j in range(2)),arb(0)).sqrt().upper()


def physical_port_matrices(base,strong):
    # Input/output are (weighted E0, weighted E1, ordinary second-component L2).
    # The independent moving mean is the second column of the four-state vector.
    g=base['v_abs_lower'].lower()
    mg=(-base['actual_m']).lower();ma=abs(base['actual_m']).upper()
    V2=base['actual_v_L2'].upper();V1=base['full_v_phi_absolute'].upper()
    L=base['actual_L_upper'].upper();L2=strong['actual_Q_phi_phi_energy_upper'].upper()
    jlo=base['physical_angle_J_lower'].lower();jhi=base['physical_angle_J_upper'].upper()
    if not g>0 or not mg>0 or not jlo>0:raise ValueError('an actual complete physical port gap is unresolved')
    ay=(1/(4*g)).upper();am=(V2/(4*g*mg)).upper()
    by=(1/g+V1*ay/g).upper();bm=(1/mg+V1*am/g).upper()
    rootj=jhi.sqrt().upper();irootj=(1/jlo.sqrt()).upper()
    to_phys=arb_mat([
        [rootj,rootj*L*am,0,rootj*L*ay],
        [0,irootj*(L2*am+L*bm),irootj,irootj*(L2*ay+L*by)],
        [0,rootj*V1*am,0,rootj*(1+V1*ay)]])
    to_mov=arb_mat([
        [irootj,0,irootj*L/(4*g)],
        [0,0,irootj*ma/g],
        [0,rootj,irootj*(L2/(4*g)+L/g)],
        [0,0,irootj*(1+V1/(4*g))]])
    return dict(moving_to_physical_three_channels=matrix_record(mat_upper(to_phys)),
                physical_to_moving_four_channels=matrix_record(mat_upper(to_mov)),
                physical_angle_J_lower=record(jlo),physical_angle_J_upper=record(jhi),
                no_inverse_turning_weight_used=True,
                exact_reflection_gauge_and_complete_mean_required=True)


def prepare(args):
    saved=load_candidate(args.candidate)
    meta=json.loads(str(saved['metadata']))
    original=read(args.target);types=read(args.type_cover)
    if (meta['coordinates']!=COORDINATES
            or meta['object_sha256']!=original['object_sha256']
            or not original['complete'] or not types['complete']
            or not types['exactly_one_real_K_root']
            or types['inputs'].get(str(args.target))!=sha(args.target)):
        raise ValueError('the same complete original target and moving candidate are required')
    nuq=Fraction(meta['exact_float_nu'])
    nulo,nuhi=map(Fraction,types['exact_nu_interval'])
    if nuq!=dyadic(meta['nu']) or not nulo<=nuq<=nuhi:
        raise ValueError('the actual fixed nu lies outside the original proved type cover')
    if not 0<args.right<=Fraction(119,500):
        raise ValueError('this complete base cover ends at the genuinely strict r=.238')
    rows=list(original['rows']);inputs=[args.candidate,args.target,args.type_cover]
    if args.right>Fraction(1,5):
        collar=read(args.collar);inputs.append(args.collar)
        if (not collar['complete'] or not collar['whole_real_radial_interval']
                or collar['object_sha256']!=original['object_sha256']
                or collar['parameter_half_width']!=original['parameter_half_width']
                or collar['inputs'].get(str(args.type_cover))!=sha(args.type_cover)):
            raise ValueError('the whole genuine original root-collar target is required')
        rows.extend(collar['rows'])
    if any(Fraction(a['interval'][1])!=Fraction(b['interval'][0]) for a,b in zip(rows,rows[1:])):
        raise ValueError('the original true closed target boxes have a gap')
    nodes=list(map(dyadic,saved['radial_nodes']))
    if nodes[0]!=0 or nodes[-1]<args.right:
        raise ValueError('the exact moving candidate does not cover the whole requested interval')
    tn=[Fraction(r['interval'][0]) for r in rows]+[Fraction(rows[-1]['interval'][1])]
    cuts=sorted({Fraction(0),args.right}|{x for x in (Fraction(1,20),Fraction(9,50)) if x<args.right}
                |{x for x in nodes if 0<x<args.right}|{x for x in tn if 0<x<args.right})
    m=int(meta['modes']);angles=args.angles
    if angles<=2*m or angles&(angles-1):
        raise ValueError('a full closed angular partition with power-of-two count is required')
    alphaq=Fraction(meta['exact_float_amplitude'])
    if alphaq!=dyadic(meta['amplitude']):raise ValueError('the exact amplitude changed')
    context=dict(saved=saved,meta=meta,rows=rows,nodes=nodes,tn=tn,cuts=cuts,
                 modes=m,angles=angles,alpha=exact_arb(alphaq),nu=exact_arb(nuq))
    doc=dict(kind=KIND,source_sha256=sha(__file__),complete=False,failure=None,
             inputs={str(p):sha(p) for p in inputs},candidate_metadata=meta,
             object_sha256=meta['object_sha256'],exact_nu=str(nuq),exact_amplitude=str(alphaq),
             exact_requested_interval=['0',str(args.right)],total_closed_radial_cells=len(cuts)-1,
             closed_angular_cells=angles,original_parameter_half_width=original['parameter_half_width'],
             original_exact_center_parameter=original['exact_center_parameter'],
             whole_affine_parameter_interval=True,complete_original_intrinsic_tail=True,
             complete_finite_moving_centre=True,all_Fourier_variations_and_mean_retained=True,
             angle='the candidate moving phi; no physical-angle Fourier truncation is inferred',
             norm='sum_(k in 4Z) (1+k^2)^t (|h1_k|^2+(-K)|h2_k|^2), plus ordinary ||h2||2; mean retained',
             comparison_channels=['E0','abs(mean(h2))','E1','ordinary_second_component_L2'],
             source_channels=['weighted_R_L2','abs(mean(R2))','weighted_R_phi_L2','ordinary_R2_L2'],
             rows=[],jumps=[],resume_history=[],
             dependencies={n:sha(Path(__file__).with_name(n)) for n in (
                 'fourfold_codazzi_candidate_shards.py','fourfold_codazzi_curvature_angle_energy_prefix.py',
                 'fourfold_codazzi_moving_actual_R_boundary.py','fourfold_codazzi_moving_sobolev_rows.py',
                 'fourfold_codazzi_moving_mean_energy_direct_rows.py','fourfold_codazzi_moving_mean_energy_prefix_v2.py',
                 'fourfold_codazzi_moving_sobolev_complete.py','fourfold_phase_beta_bulk_box.py',
                 'fourfold_codazzi_rotational_cap_jacobi.py')},
             body_BVP_inverse_proved=False,physical_variation_port_conversion_paid_here=False,
             full_candidate_residual_certified_here=False)
    return context,doc


def identity(c,index):
    left,right=c['cuts'][index:index+2]
    j=min(bisect_right(c['nodes'],left)-1,len(c['nodes'])-2)
    k=bisect_right(c['tn'],left)-1;row=c['rows'][k]
    a,b=map(Fraction,row['interval'])
    if not (c['nodes'][j]<=left<right<=c['nodes'][j+1] and a<=left<right<=b):
        raise ValueError('incomplete common moving-candidate/true-target refinement')
    return left,right,j,k,row


def coefficient_row(c,index,sampler):
    left,right,j,k,row=identity(c,index)
    a=target_bounds(row,left,right,c['nu'])
    y,_=polynomial_ranges(c['saved'],c['nodes'],j,left,right)
    fields,_=sampler.fields(y,c['alpha'],a['s'])
    base,strong=direct_coefficients(y,fields,a,c['alpha'],c['modes'])
    return dict(common_row=index,interval=[str(left),str(right)],candidate_piece=j,
                original_target_row=k,actual_scalar_germ=row['actual_scalar_germ'],
                actual_target={name:record(a[name]) for name in ('gamma','beta','K','K1','s')},
                base={name:record(v) for name,v in base.items()},
                strong={name:record(v) for name,v in strong.items()})


def complete_comparison(c,doc):
    rows=doc['rows'];n=len(rows)
    if n!=len(c['cuts'])-1:
        raise ValueError('a partial coefficient cover cannot be called a complete propagation')
    base=[{k:box_from_record(v) for k,v in r['base'].items()} for r in rows]
    strong=[{k:box_from_record(v) for k,v in r['strong'].items()} for r in rows]
    jumps={};m=c['modes'];al=c['alpha']
    for i in range(1,n):
        if rows[i-1]['candidate_piece']==rows[i]['candidate_piece']:continue
        j=rows[i]['candidate_piece']
        if c['nodes'][j]!=c['cuts'][i]:raise ValueError('a true moving polynomial join was lost')
        exact=actual_jump(c['saved'],c['nodes'],j)
        du=(abs(al)*sum((abs(exact_arb(z)) for z in exact[:m]),arb(0))).upper()
        dv=(abs(al)*sum((abs(exact_arb(z)) for z in exact[m:]),arb(0))).upper()
        du1=(abs(al)*sum((4*(j+1)*abs(exact_arb(z)) for j,z in enumerate(exact[:m])),arb(0))).upper()
        dv1=(abs(al)*sum((4*j*abs(exact_arb(z)) for j,z in enumerate(exact[m:])),arb(0))).upper()
        jm=abs(al*exact_arb(exact[m])).upper()
        q=max(base[i-1]['q'].upper(),base[i]['q'].upper()).upper()
        j0=(du*du+q*q*dv*dv).sqrt().upper()
        j1=(du1*du1+q*q*dv1*dv1).sqrt().upper()
        jumps[i]=arb_mat([[j0],[jm],[j1],[dv]])
        doc['jumps'].append(dict(common_row=i,candidate_join=j,radius=str(c['nodes'][j]),
            exact_moving_u_jump_A0=record(du),exact_moving_v_jump_A0=record(dv),
            exact_moving_u_phi_jump_A0=record(du1),exact_moving_v_phi_jump_A0=record(dv1),
            full_energy_jump=record(j0),exact_mean_jump=record(jm),full_H1_derivative_jump=record(j1),
            full_ordinary_second_component_jump=record(dv)))
    qmin=min(b['q'].lower() for b in base).lower()
    jump_sum=arb_mat([[sum((v[j,0] for v in jumps.values()),arb(0)).upper()] for j in range(4)])
    result={}
    for reverse in (False,True):
        U=arb_mat([[int(i==j) for j in range(4)] for i in range(4)])
        P=arb_mat([[int(i==j) for j in range(4)] for i in range(4)])
        propagated_jumps=arb_mat([[0],[0],[0],[0]])
        order=range(n-1,-1,-1) if reverse else range(n)
        for i in order:
            length=exact_arb(c['cuts'][i+1]-c['cuts'][i])
            current=jumps.get(i+1 if reverse else i)
            if current is not None:propagated_jumps=mat_upper(propagated_jumps+current)
            flow=mat_upper((four_matrix(base[i],strong[i],reverse)*length).exp())
            upflow=mat_upper((four_matrix(base[i],strong[i],reverse,True)*length).exp())
            U=mat_upper(flow*U);P=mat_upper(upflow*P)
            propagated_jumps=mat_upper(flow*propagated_jumps)
        qi=base[-1 if reverse else 0]['q'].lower()
        full=norm_gains(P,qi);zero=norm_gains(P,qi,True);source=norm_gains(P,qmin)
        def extra_fractional(g):
            return {**g,'H_one_third':((2*g['H0'].log()+g['H1'].log())/3).exp().upper()}
        full,zero,source=map(extra_fractional,(full,zero,source))
        jbound=mat_upper(P*jump_sum)
        jH0=jbound[0,0].upper();jH1=(jbound[0,0]**2+jbound[2,0]**2).sqrt().upper()
        result['backward' if reverse else 'forward']=dict(
            endpoint_matrix=matrix_record(U),all_subinterval_positive_majorant=matrix_record(P),
            full_initial_gains={k:record(v) for k,v in full.items()},
            conditional_initial_zero_mean_gains={k:record(v) for k,v in zero.items()},
            full_L1_source_gains={k:record(v) for k,v in source.items()},
            full_ordinary_H1_to_three_channel_initial_gain=record(ordinary_three_channel_gain(P,base[-1 if reverse else 0]['q'].upper())),
            full_L1_ordinary_H1_source_to_three_channel_gain=record(ordinary_three_channel_gain(P,max(b['q'].upper() for b in base))),
            actual_moving_jump_endpoint=matrix_record(propagated_jumps),
            actual_moving_jump_H0_uniform=record(jH0),actual_moving_jump_H1_uniform=record(jH1),
            actual_moving_jump_Y2_uniform=record(jbound[3,0].upper()))
    doc.update(complete=True,whole_requested_radial_interval=True,
        whole_closed_angular_circle=True,all_exact_moving_PPoly_jumps_paid=True,
        full_four_state_propagation=True,bounds=result,
        physical_ports=dict(left=physical_port_matrices(base[0],strong[0]),
                            right=physical_port_matrices(base[-1],strong[-1])),
        global_bounds={k:record(v) for k,v in dict(
            q_absolute_lower=qmin,actual_negative_v_gap=min(b['v_abs_lower'] for b in base).lower(),
            actual_mean_absolute_lower=min((-b['actual_m']).lower() for b in base).lower(),
            R_upper=max(b['actual_R_upper'] for b in base).upper(),
            L_upper=max(b['actual_L_upper'] for b in base).upper(),
            L2_upper=max(b['actual_Q_phi_phi_energy_upper'] for b in strong).upper(),
            total_actual_moving_energy_jump=jump_sum[0,0],total_actual_moving_mean_jump=jump_sum[1,0],
            total_actual_moving_derivative_jump=jump_sum[2,0],
            total_actual_moving_ordinary_second_component_jump=jump_sum[3,0]).items()})


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--target',type=Path,default=Path('notes/2026-11-13-Codazzi-true-target-r02-v1-native.json.gz'))
    ap.add_argument('--collar',type=Path,default=Path('notes/2026-11-13-R133-actual-root-collar-complete-coefficients-v2-native.json.gz'))
    ap.add_argument('--type-cover',type=Path,default=Path('notes/2026-11-13-R133-compact-nu-full-type-cover-native.json.gz'))
    ap.add_argument('--right',type=Fraction,default=Fraction(119,500))
    ap.add_argument('--angles',type=int,default=1024)
    ap.add_argument('--resume',type=Path)
    ap.add_argument('--max-new-rows',type=int)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve the original checkpoint and every actual run')
    c,doc=prepare(args)
    if args.resume:
        previous=read(args.resume)
        for k in ('kind','source_sha256','inputs','candidate_metadata','exact_nu','exact_amplitude',
                  'exact_requested_interval','total_closed_radial_cells','closed_angular_cells','dependencies'):
            if previous[k]!=doc[k]:raise ValueError('a saved moving-energy input changed: '+k)
        if previous['failure'] is not None or previous['complete']:
            raise ValueError('resume only the stated successful saved row prefix')
        for index,row in enumerate(previous['rows']):
            left,right,j,k,actual=identity(c,index)
            if (row['common_row']!=index or row['interval']!=list(map(str,(left,right)))
                or row['candidate_piece']!=j or row['original_target_row']!=k
                or row['actual_scalar_germ']!=actual['actual_scalar_germ']):
                raise ValueError('a complete saved row changed its original mathematical interval')
        doc['rows']=previous['rows'];doc['resume_history']=previous['resume_history']+[
            dict(path=str(args.resume),sha256=sha(args.resume),complete=False,
                 saved_complete_rows=len(previous['rows']),
                 observation='explicit prefix consumed; no missing process exit status is inferred')]
    sampler=StrongDirectSums(c['modes'],args.angles)
    first=len(doc['rows']);last=len(c['cuts'])-1
    if args.max_new_rows is not None:
        if args.max_new_rows<=0:raise ValueError('positive explicit new-row count required')
        last=min(last,first+args.max_new_rows)
    checkpoint=time.monotonic()
    try:
        for index in range(first,last):
            row=coefficient_row(c,index,sampler);doc['rows'].append(row)
            if time.monotonic()-checkpoint>15:
                doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
                print(dict(rows=len(doc['rows']),total=len(c['cuts'])-1,
                           right=row['interval'][1],L=row['base']['actual_L_upper']['mid_float']),flush=True)
                checkpoint=time.monotonic()
        if len(doc['rows'])==len(c['cuts'])-1:complete_comparison(c,doc)
        else:doc['explicit_saved_prefix_only']=True
    except Exception as exc:
        doc['failure']=dict(type=type(exc).__name__,message=str(exc))
        raise
    finally:
        doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],rows=len(doc['rows']),
               total=len(c['cuts'])-1,wall_seconds=doc['wall_seconds'],out=str(args.out)),flush=True)
    if doc['complete']:
        print({name:{k:g['mid_float'] for k,g in row['full_initial_gains'].items()}
               for name,row in doc['bounds'].items()},flush=True)


if __name__=='__main__':
    main()
