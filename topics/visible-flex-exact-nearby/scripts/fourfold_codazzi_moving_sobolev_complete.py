#!/usr/bin/env python3
"""Complete H1 and H^(1/6) moving Cauchy/source, including mean and jumps.

The first two comparison rows are the completed actual zero-order theorem.
The third row pays every derivative commutator. Full H0/H1 operator bounds
are interpolated in the same weighted Fourier scale, without deleting mean.
"""
from __future__ import annotations
import argparse,time
from pathlib import Path
from flint import arb,arb_mat,ctx
from fourfold_codazzi_moving_mean_energy_rows import arguments,prepare,identify
from fourfold_codazzi_moving_mean_energy_prefix_v2 import (
    read,actual_jump,comparison_matrix,mat_upper,matrix_record,exact_arb,record,save,sha)
from fourfold_codazzi_rotational_cap_jacobi import box_from_record


def three_matrix(base,strong,reverse=False,positive=False):
    low=comparison_matrix(base,reverse,positive)
    g=strong['backward_derivative_rate' if reverse else 'forward_derivative_rate']
    if positive:g=max(arb(0),g).upper()
    return arb_mat([[low[0,0],low[0,1],0],[low[1,0],low[1,1],0],
                    [strong['coupling_E0_to_E1'],strong['coupling_mean_to_E1'],g]])


def norm_gains(U,qinitial,zero_mean=False):
    # A full H1 vector has norm sqrt(E0^2+E1^2); M<=E0/qinitial.
    a=U[0,0] if zero_mean else U[0,0]+U[0,1]/qinitial
    b=U[0,2]
    c=U[2,0] if zero_mean else U[2,0]+U[2,1]/qinitial
    d=U[2,2]
    C0=a.upper();C1=(a*a+b*b+c*c+d*d).sqrt().upper()
    Ct=((5*C0.log()+C1.log())/6).exp().upper()
    return dict(H0=C0,H1=C1,H_one_sixth=Ct)


def derivative_jump(context,j,left,right,sl,sr,old):
    delta=actual_jump(context['saved'],context['nodes'],j);m=context['m'];alpha=context['alpha']
    du1=(abs(alpha)*sum((4*(k+1)*abs(exact_arb(z)) for k,z in enumerate(delta[:m])),arb(0))).upper()
    dv1=(abs(alpha)*sum((4*k*abs(exact_arb(z)) for k,z in enumerate(delta[m:])),arb(0))).upper()
    dv=box_from_record(old['exact_physical_v_jump_A0']).upper()
    deltaD=box_from_record(old['mean_C_difference_upper']).upper()
    deltaTheta=box_from_record(old['inverse_angle_difference_upper']).upper()
    D=max(abs(left['actual_D']),abs(right['actual_D'])).upper()
    V=max(left['v_abs_upper'],right['v_abs_upper']).upper()
    Ut=max(left['full_u_theta_absolute'],right['full_u_theta_absolute']).upper()
    Vt=max(left['full_v_theta_absolute'],right['full_v_theta_absolute']).upper()
    Utt=max(sl['full_u_theta_theta_absolute'],sr['full_u_theta_theta_absolute']).upper()
    Vtt=max(sl['full_v_theta_theta_absolute'],sr['full_v_theta_theta_absolute']).upper()
    ju=(deltaD*V*Ut+D*dv*Ut+D*V*du1+D*(Vt*Ut+V*Utt)*deltaTheta).upper()
    jv=(deltaD*V*Vt+D*dv*Vt+D*V*dv1+D*(Vt*Vt+V*Vtt)*deltaTheta).upper()
    q=max(left['q'].upper(),right['q'].upper()).upper();energy=(ju*ju+q*q*jv*jv).sqrt().upper()
    result=dict(radius=old['radius'],candidate_join=j,exact_physical_u_theta_jump_A0=record(du1),
        exact_physical_v_theta_jump_A0=record(dv1),moving_u_phi_jump_absolute=record(ju),
        moving_v_phi_jump_absolute=record(jv),moving_first_derivative_energy_jump=record(energy),
        actual_angular_derivative_mean_exactly_zero=True)
    return result,energy


def main():
    ap=arguments(argparse.ArgumentParser(description=__doc__))
    ap.add_argument('--energy',type=Path,default=Path('notes/2026-11-13-R133-moving-mean-energy-alpha075-r0238-complete-native.json.gz'))
    ap.add_argument('--part',type=Path,action='append',required=True);ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320
    if args.out.exists():raise FileExistsError('preserve every actual strong consumer result')
    context=prepare(args);original=read(args.energy);header=context['header']
    if (not original['complete'] or original['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_moving_mean_energy_complete.py'))
        or any(original['inputs'].get(k)!=v for k,v in header['inputs'].items())):
        raise ValueError('the same completed full zero-order theorem is required')
    parts=[]
    for path in args.part:
        doc=read(path)
        if (not doc['complete'] or doc['failure'] is not None
            or doc['kind']!='actual_complete_moving_H1_coefficient_row_part'
            or doc['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_moving_sobolev_rows.py'))
            or doc['inputs'].get(str(args.energy))!=sha(args.energy)
            or any(doc['inputs'].get(k)!=v for k,v in header['inputs'].items())
            or doc['total_common_partition_rows']!=header['total_common_partition_rows']):
            raise ValueError('a complete same-object strong coefficient part is missing')
        parts.append((doc['first_common_row'],path,doc))
    parts.sort(key=lambda item:item[0]);rows=[];cursor=0
    for first,path,doc in parts:
        if first!=cursor or len(doc['rows'])!=doc['last_common_row_exclusive']-first:
            raise ValueError('strong rows have a gap, overlap, or missing index')
        if doc['exact_requested_subinterval']!=list(map(str,(context['cuts'][first],context['cuts'][doc['last_common_row_exclusive']]))):
            raise ValueError('the actual strong radial partition changed')
        rows.extend(doc['rows']);cursor=doc['last_common_row_exclusive']
    if cursor!=header['total_common_partition_rows'] or len(original['rows'])!=cursor:
        raise ValueError('the strong actual coefficient interval is incomplete')
    base=[];strong=[]
    for index,row in enumerate(rows):
        left,right,j,k,actual=identify(context,index)
        if (row['common_row']!=index or row['interval']!=list(map(str,(left,right)))
            or row['candidate_piece']!=j or row['native_row']!=k):
            raise ValueError('an actual strong common-row identity changed')
        b={name:box_from_record(value) for name,value in original['rows'][index]['bounds'].items()}
        s={name:box_from_record(value) for name,value in row['bounds'].items()}
        if not all(z.is_finite() for z in s.values()) or not s['actual_Q_phi_phi_energy_upper']>=0:
            raise ValueError('the complete true second angular derivative is unresolved')
        base.append(b);strong.append(s)
    doc=dict(header,kind='actual_full_moving_H1_and_fractional_Cauchy_source',complete=False,
        source_sha256=sha(__file__),inputs={**header['inputs'],**{str(p):sha(p) for p in (args.energy,*args.part)}},
        rows=rows,jumps=[],failure=None,all_Fourier_variations_and_mean_retained=True,
        exact_fractional_order='1/6',norm='sum_m (1+m^2)^s (|h1_m|^2+(-K)|h2_m|^2), physical m in 4Z',
        actual_centre_PDE_residual_not_certified_here=True,body_BVP_inverse_not_proved=True,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_moving_mean_energy_prefix_v2.py','fourfold_codazzi_moving_mean_energy_rows.py',
            'fourfold_codazzi_moving_sobolev_rows.py','fourfold_codazzi_rotational_cap_jacobi.py')})
    try:
        oldj={r['candidate_join']:r for r in original['jumps']};jump_at={};cuts=context['cuts']
        for i in range(1,len(rows)):
            if rows[i-1]['candidate_piece']==rows[i]['candidate_piece']:continue
            j=rows[i]['candidate_piece']
            if j not in oldj:raise ValueError('a genuine zero-order interface is missing')
            entry,J1=derivative_jump(context,j,base[i-1],base[i],strong[i-1],strong[i],oldj[j]);doc['jumps'].append(entry)
            jump_at[i]=arb_mat([[box_from_record(oldj[j]['moving_energy_jump']).upper()],
                [box_from_record(oldj[j]['moving_mean_jump']).upper()],[J1]])
        results={};qmin=min(r['q'].lower() for r in base).lower()
        jump_sum=arb_mat([[sum((v[j,0] for v in jump_at.values()),arb(0)).upper()] for j in range(3)])
        for reverse in (False,True):
            end=arb_mat([[1,0,0],[0,1,0],[0,0,1]]);uniform=arb_mat([[1,0,0],[0,1,0],[0,0,1]])
            J=arb_mat([[0],[0],[0]]);order=range(len(rows)-1,-1,-1) if reverse else range(len(rows))
            for i in order:
                extra=jump_at.get(i+1 if reverse else i)
                if extra is not None:J=mat_upper(J+extra)
                length=exact_arb(cuts[i+1]-cuts[i])
                flow=mat_upper((three_matrix(base[i],strong[i],reverse)*length).exp())
                upflow=mat_upper((three_matrix(base[i],strong[i],reverse,True)*length).exp())
                end=mat_upper(flow*end);uniform=mat_upper(upflow*uniform);J=mat_upper(flow*J)
            qi=base[-1 if reverse else 0]['q'].lower()
            ordinary=norm_gains(uniform,qmin);initial=norm_gains(uniform,qi);zero=norm_gains(uniform,qi,True)
            jump_bound=mat_upper(uniform*jump_sum)
            J0=jump_bound[0,0].upper();JH1=(jump_bound[0,0]**2+jump_bound[2,0]**2).sqrt().upper()
            Jfrac=((5*J0.log()+JH1.log())/6).exp().upper() if J0>0 else arb(0)
            results['backward' if reverse else 'forward']=dict(endpoint_matrix=matrix_record(end),
                all_subinterval_positive_majorant=matrix_record(uniform),
                complete_initial_energy_uniform_gains={k:record(v) for k,v in initial.items()},
                initial_zero_mean_uniform_gains={k:record(v) for k,v in zero.items()},
                ordinary_L1_source_uniform_gains={k:record(v) for k,v in ordinary.items()},
                actual_moving_jump_uniform_bounds={k:record(v) for k,v in dict(H0=J0,H1=JH1,H_one_sixth=Jfrac).items()},
                actual_moving_jump_endpoint_H1=record((J[0,0]**2+J[2,0]**2).sqrt().upper()))
        doc.update(complete=True,bounds=results,all_closed_rows_and_all_interfaces_paid=True,
            maximum_actual_Q_phi_phi_energy=record(max(s['actual_Q_phi_phi_energy_upper'].upper() for s in strong)),
            full_H1_mean_preserving_Cauchy_theorem=True,full_H_one_sixth_by_same_scale_interpolation=True)
    except Exception as exc:doc['failure']=dict(type=type(exc).__name__,message=str(exc))
    doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],rows=len(rows),jumps=len(doc['jumps']),
        bounds=doc.get('bounds'),wall_seconds=doc['wall_seconds']),flush=True)
    if not doc['complete']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
