#!/usr/bin/env python3
"""Validated position-ordered outer11 adjoint functional of the actual source.

Use the already paid real source radii/material boxes and signed N recorder.
The same R65 local Taylor flow is transposed to advance a terminal height
functional backwards. Full partial-flow sign bounds enclose every point
of each source interval. Only the adjoint ODE is integrated: the fixed
background integrals and original candidate are never recomputed/changed.

Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import resource
import tempfile
import time

from flint import arb, ctx, fmpq

from closure_real_head_source_enclosure import exact_q, power2
from closure_real_linear_head_enclosure import PositiveKernels, positive_scale_bounds
from closure_projective_interval_column import ProjectiveColumn
from closure_split_joint_io_v2 import digest, read_field, iter_array
from closure_taylor_cut_slope_v2 import (ball, endpoint, record, point_record,
    intersect, rough_radius, monotone_parts, column_record, restore_column, save,
    EXPECTED_SOURCE, EXPECTED_PROJECTIVE, EXPECTED_PB)
from closure_outer_taylor_shared_flow import taylor_global, root_global, raw_source_identity
from tail_r33_middle_ordered_physical import SourceValues


EXPECTED_OUTER_FLOW_SOURCE = '81d8bd9ad3da434eb8ab98d381a32a09bbe7aca5fa3be8a0bfe493ccd62455b7'
EXPECTED_SOURCE_RECORDER = '544bab2538a33ac32c546d980e08dc0d95fea383d5f25aed894fea9ce27c3d34'
EXPECTED_TAYLOR = '8e150b6fe16c33da98043bc7ebe952abf123e2f7c8da8ebbfb10bfec700fb5ea'


def rational_interval(d):
    def rational(p):
        return arb(fmpq(int(p['numerator']), int(p['denominator'])))
    return rational(d['lower']).union(rational(d['upper']))


def transpose(A):
    return [[A[j][i] for j in range(2)] for i in range(2)]


def functional_v_range(column, A, B):
    """All eta_v(s) on one backwards partial flow with int(a)<=A,int(b)<=B.

If A*B<1, positive a,b imply T01 in [0,A], T11 in [1-A*B,1]
on every subinterval. Preserve the common signed projective amplitude.
"""
    product=(A*B).upper()
    if not product < arb(1)/4:
        raise ArithmeticError('Subdivide the partial functional-flow bound')
    t01=arb(0).union(A)
    t11=(1-product).lower().union(arb(1))
    z=(t01+column.ratio*t11 if column.pivot==0 else
       column.ratio*t01+t11)
    amp=column.absolute_lower.union(column.absolute_upper)
    lo,hi=positive_scale_bounds((z.lower(),z.upper()),amp)
    if column.sign<0:
        lo,hi=-hi,-lo
    return lo.union(hi)


def actual_panel_bounds(h,segment,left,right,radius,material,mode,mu):
    rr,dr=rough_radius(h,segment,left,right,radius)
    rr=intersect(rr,ball(material['radius']))
    a,b=exact_q(left),exact_q(right)
    source=h.source_point(segment,a.union(b))
    w=intersect(source['w'],ball(material['w']))
    sign=segment['_monotone_sign']
    if sign:
        wl=h.source_point(segment,a)['w']
        wr=h.source_point(segment,b)['w']
        monotone=(wl.lower().union(wr.upper()) if sign>0 else
                  wr.lower().union(wl.upper()))
        w=intersect(w,monotone)
    if not rr>0 or not w>0:
        raise ArithmeticError('The real partial source box must be positive')
    u,nu=mode*mode-4,arb(mode*mode*(mode*mode-1))/12
    A=abs(h.sqrt12*mu*h.rc**(2*u)*dr/(rr**(8+2*u)*w)).upper()
    B=abs(nu*h.sqrt12/(mu*h.rc**(2*u))*rr**(6+2*u)*w*dr).upper()
    if not (A*B).upper()<arb(1)/4:
        raise ArithmeticError('Subdivide actual partial a,b integrals')
    J=(rr/h.rc)**u*rr**4*w*w/(h.sqrt12*mu)
    if not J>0:
        raise ArithmeticError('The fixed-global-gauge source coefficient is not positive')
    return A,B,J


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('ready','flow','source-summary','linear-cancellation','out-prefix'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--precision',type=int,default=256)
    p.add_argument('--order',type=int,default=24)
    p.add_argument('--root-bits',type=int,default=160)
    p.add_argument('--remainder-bits',type=int,default=100)
    p.add_argument('--rss-kib',type=int,default=40960)
    p.add_argument('--resume',type=Path)
    a=p.parse_args()
    if a.precision<a.root_bits+32 or a.order<4:
        raise ValueError('The original rigorous Taylor/root precision is required')
    ctx.prec,ctx.cap,ctx.threads=a.precision,a.order+2,1
    began=time.monotonic()
    output=Path(str(a.out_prefix)+'.json')
    if output.exists():
        raise FileExistsError('Use a fresh complete adjoint-functional prefix')
    expected={'closure_outer_taylor_shared_flow.py':EXPECTED_OUTER_FLOW_SOURCE,
        'closure_outer_candidate_source_record.py':EXPECTED_SOURCE_RECORDER,
        'closure_taylor_cut_slope_v2.py':EXPECTED_TAYLOR,
        'closure_real_head_source_enclosure.py':EXPECTED_SOURCE,
        'closure_projective_interval_column.py':EXPECTED_PROJECTIVE,
        'closure_real_linear_head_enclosure.py':EXPECTED_PB,
        'tail_r33_middle_ordered_physical.py':'ac1bb495b33a37f7f88b6b7258a88a466c205cb452141668b6c454f88386008e'}
    for name,sha in expected.items():
        if digest(Path(__file__).with_name(name))!=sha:
            raise ValueError('A paid mathematical source changed: '+name)
    paths=[getattr(a,k) for k in ('ready','flow','source_summary','linear_cancellation')]
    hashes={str(path):digest(path) for path in paths}
    flow=json.loads(a.flow.read_text())
    sources=json.loads(a.source_summary.read_text())
    cancellation=json.loads(a.linear_cancellation.read_text())
    if (not all(flow['gates'].values()) or not sources['all_gates']
            or not cancellation['all_gates'] or sources['cell']!=11
            or sources['selected_cosine_modes']!=[2,4]
            or sources['panels']!=5545 or sources['tau']!='1/64'):
        raise ValueError('The complete exact same actual source/flow packages are required')
    for doc in (flow,sources):
        if doc['input_hashes'].get(str(a.ready))!=hashes[str(a.ready)]:
            raise ValueError('The actual frozen source changed')
    if cancellation['input_hashes'].get(str(a.flow))!=hashes[str(a.flow)]:
        raise ValueError('The linear cancellation uses another actual background flow')
    for path,sha in sources['input_hashes'].items():
        if path.endswith('response.json.gz') and cancellation['input_hashes'].get(path)!=sha:
            raise ValueError('The candidate outer heights and recorded source differ')
    if sources['entrypoint_sha256']!=EXPECTED_SOURCE_RECORDER:
        raise ValueError('The selected full N source has another executed implementation')
    ready=dict(rationalDeepModel=read_field(a.ready,'rationalDeepModel'),
               shallowSourceParameters=read_field(a.ready,'shallowSourceParameters'))
    identity=raw_source_identity(ready,11)
    h=SourceValues(ready)
    del ready
    kernel=PositiveKernels(h,12,4)
    cell=kernel.source_cell(11)
    h.cells[11]=cell
    actual_cell=next(c for c in flow['cell_rows'] if c['cell']==11)
    R=ball(actual_cell['radius'])
    mu=ball(flow['config']['global_mu_star'])
    modes=[2,4]
    phi={r['mode']:r for r in actual_cell['modes']}
    linear={r['mode']:r for r in cancellation['rows'] if r['endpoint_physical_node']==11}
    groups={g['segment']:g for g in sources['groups']}
    if sorted(groups)!=list(range(9)):
        raise ValueError('All nine complete source groups are required')
    vectors=[ProjectiveColumn([arb(1),arb(0)]) for m in modes]
    integrals=[arb(0),arb(0)]
    absolute_integrals=[arb(0),arb(0)]
    source_L1=[arb(0),arb(0)]
    counts=dict(original_material=0,taylor=0,root_brackets=0,rejected=0)
    worst=arb(0)
    completed=[]
    config=dict(cell=11,modes=modes,precision=a.precision,order=a.order,
        remainder_bits=a.remainder_bits,root_bits=a.root_bits,
        global_mu_star=record(mu),input_hashes=hashes,source_hashes=expected,
        source_only_class_sha256=digest(Path(__file__).with_name('tail_r33_middle_ordered_physical.py')),
        explicit_source_cell_sha256=digest(Path(__file__).with_name('closure_real_linear_head_enclosure.py')),
        entrypoint_sha256=digest(Path(__file__)))
    if a.resume:
        old=json.loads(a.resume.read_text())
        if old['config']!=config:
            raise ValueError('A resume checkpoint has another source or arithmetic configuration')
        vectors=[restore_column(v) for v in old['adjoint_columns']]
        integrals=[ball(v) for v in old['signed_source_integrals']]
        absolute_integrals=[ball(v) for v in old['absolute_source_integrals']]
        source_L1=[ball(v) for v in old['canonical_forcing_L1']]
        counts=old['counts']
        worst=ball(old['greatest_balanced_Taylor_remainder'])
        completed=old['completed_segments']
    def guard():
        rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if rss>a.rss_kib:
            raise MemoryError('The owned adjoint exceeded the observed RSS stop threshold: '+str(rss))
    try:
        for j in range(8,-1,-1):
            if j in completed:
                continue
            group=groups[j]
            path=Path(group['path'])
            if digest(path)!=group['sha256']:
                raise ValueError('A complete position-resolved source group changed')
            segment=cell['segments'][j]
            monotone=monotone_parts(segment,a.root_bits)
            # A private unlinked spool permits reverse streaming without
            # loading an entire decompressed source group into memory.
            with tempfile.TemporaryFile(mode='w+b',dir=a.out_prefix.parent) as spool:
                offsets=[]
                first=last=None
                for g in iter_array(path,'panels'):
                    if g['segment']!=j or g['panel']!=len(offsets):
                        raise ValueError('The full original source-panel ordering changed')
                    if first is None:
                        first=g
                    last=g
                    offsets.append(spool.tell())
                    spool.write(json.dumps(g,separators=(',',':')).encode()+b'\n')
                if len(offsets)!=group['panels']:
                    raise ValueError('The entire original source segment is required')
                segment['physical_inner_radius']=ball(first['radius_left'])
                segment['physical_outer_radius']=ball(last['radius_right'])
                if j==8:
                    intersect(segment['physical_outer_radius'],R)
                first_x=Fraction(first['x_left'])
                last_x=Fraction(last['x_right'])
                if first_x!=0 or last_x!=1:
                    raise ValueError('The full source segment [0,1] is not covered')
                del first,last
                contributions=[arb(0),arb(0)]
                for index in range(len(offsets)-1,-1,-1):
                    spool.seek(offsets[index])
                    g=json.loads(spool.readline())
                    left,right=Fraction(g['x_left']),Fraction(g['x_right'])
                    radius=ball(g['radius_left'])
                    parts=[]
                    for lo,hi,sign in monotone:
                        aa,cc=max(left,lo),min(right,hi)
                        if aa<cc:
                            parts.append((aa,cc,sign))
                    if not parts or parts[0][0]!=left or parts[-1][1]!=right:
                        raise ArithmeticError('The exact monotone/root partition misses source positions')
                    accepted=[]
                    for lo,hi,sign in parts:
                        segment['_monotone_sign']=sign
                        stack=[(lo,hi,0)]
                        while stack:
                            aa,cc,depth=stack.pop()
                            try:
                                T,next_radius,error=(root_global(h,segment,aa,cc,radius,modes,mu)
                                    if sign==0 else taylor_global(h,segment,aa,cc,radius,modes,
                                        a.order,power2(-a.remainder_bits),mu))
                                bounds=[actual_panel_bounds(h,segment,aa,cc,radius,g,m,mu) for m in modes]
                            except (ArithmeticError,ValueError,ZeroDivisionError) as err:
                                if sign==0 or depth>=40:
                                    raise ArithmeticError('Unresolved adjoint source panel '+
                                        str((j,index,aa,cc,sign))+': '+str(err)) from err
                                mid=(aa+cc)/2
                                stack.extend([(mid,cc,depth+1),(aa,mid,depth+1)])
                                counts['rejected']+=1
                                continue
                            accepted.append((aa,cc,T,bounds))
                            radius=next_radius
                            counts['root_brackets' if sign==0 else 'taylor']+=1
                            if sign:
                                worst=max(worst,error)
                            guard()
                    intersect(radius,ball(g['radius_right']))
                    source={row['mode']:ball(row['complete_source_cosine'])
                            for row in g['selected_cosine_sources']}
                    for aa,cc,T,bounds in reversed(accepted):
                        dx=exact_q(cc-aa)
                        for k,m in enumerate(modes):
                            A,B,J=bounds[k]
                            eta=functional_v_range(vectors[k],A,B)
                            value=eta*J*source[m]*dx
                            integrals[k]+=value
                            contributions[k]+=value
                            absolute_integrals[k]+=(abs(eta).upper()*J.upper()*abs(source[m]).upper()*dx).upper()
                            source_L1[k]+=(J.upper()*abs(source[m]).upper()*dx).upper()
                            v=restore_column(column_record(vectors[k]))
                            v.advance(transpose(T[k]))
                            vectors[k]=v
                    counts['original_material']+=1
                    guard()
            completed.append(j)
            checkpoint=dict(status='Complete actual adjoint source segment',config=config,
                completed_segments=completed,adjoint_columns=[column_record(v) for v in vectors],
                signed_source_integrals=[record(v) for v in integrals],
                absolute_source_integrals=[record(v.upper()) for v in absolute_integrals],
                canonical_forcing_L1=[record(v.upper()) for v in source_L1],
                this_segment_signed_integrals=[record(v) for v in contributions],
                counts=counts,greatest_balanced_Taylor_remainder=record(worst),
                elapsed_seconds=time.monotonic()-began,
                peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            cp=Path(str(a.out_prefix)+f'-completed-segment{j}.json')
            if cp.exists():
                raise FileExistsError('A complete adjoint checkpoint would be overwritten')
            save(cp,checkpoint)
            print(json.dumps(dict(event='complete_adjoint_segment',segment=j,counts=counts,
                signed=[str(x) for x in integrals],seconds=time.monotonic()-began,
                peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
        if counts['original_material']!=sources['panels'] or completed!=list(range(8,-1,-1)):
            raise ValueError('The full actual cell11 functional was not covered')
        output_rows=[]
        for k,m in enumerate(modes):
            adj=[]
            for col in range(2):
                lo,hi=vectors[k].component_bounds(col)
                x=lo.union(hi)
                old=ball(phi[m]['global_gauge_fundamental_matrix'][0][col])
                adj.append(record(intersect(x,old)))
            S=ball(phi[m]['S0_true_Q'])
            factor=(R/h.rc)**(m*m-4)/S
            forcing=factor*integrals[k]
            forcing_abs=(abs(factor).upper()*absolute_integrals[k]).upper()
            centre=rational_interval(linear[m]['complete_head_lift_minus_outer_candidate_Q'])+forcing
            axis=rational_interval(linear[m]['canonical_parameter_axis'])
            output_rows.append(dict(mode=m,whole_adjoint_at_node12=adj,
                exact_original_S0_Q=phi[m]['S0_true_Q'],
                signed_global_q_forcing_integral=record(integrals[k]),
                canonical_forcing_L1=record(source_L1[k].upper()),
                signed_canonical_cut_forcing_contribution=record(forcing),
                absolute_canonical_cut_forcing_upper=record(forcing_abs),
                complete_candidate_centre_residual_canonical_Q=record(centre),
                complete_candidate_centre_residual_axis_ratio_upper=record((abs(centre).upper()/axis).upper()),
                canonical_parameter_axis=record(axis),
                unknown_outer_correction_nonlinearity_included=False))
        gates=dict(same_original_candidate_and_fixed_real_g=True,
            no_new_background_source_integrals=True,
            all5545_original_source_positions_and_all_subpositions_paid=True,
            actual_Taylor_remainders_and_critical_root_brackets_paid=True,
            exact_global_mu11_no_rho_repeat=True,
            same_actual_complete_signed_N_with_mean_and_inverse=True,
            final_adjoint_intersects_complete_original_background_first_row=True,
            complete_candidate_linear_source_already_cancelled=True,
            original_R63_R58_cut_feedback_retained=True)
        result=dict(status='Actual whole-cell11 two-mode signed nonlinear source functional and centre residual',
            gates=gates,all_gates=True,cell=11,endpoint_physical_node=11,modes=modes,
            rows=output_rows,config=config,source_identity=identity,counts=counts,
            greatest_balanced_Taylor_remainder=record(worst),
            whole_cell_candidate_centre_residual_paid=True,
            complete_outer_correction_Green_and_Schur_inverse_paid=False,
            full46_or_infinite_frequency_outer_problem_paid=False,
            new_background_integrals=0,source_functional_definition='Integral of eta_v(x)*(r/rc)^u*r^4*w^2/(sqrt12*mu11)*N_cos,m(x) dx, eta(R)=(1,0), then multiply (R/rc)^u/S0.',
            input_hashes=hashes,entrypoint_sha256=digest(Path(__file__)),
            elapsed_seconds=time.monotonic()-began,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save(output,result)
        guard()
        print(json.dumps(dict(event='complete_adjoint_functional',output=str(output),all_gates=True,
            rows=[dict(mode=r['mode'],forcing=str(ball(r['signed_canonical_cut_forcing_contribution'])),
                       centre=str(ball(r['complete_candidate_centre_residual_canonical_Q'])),
                       axis_ratio=str(ball(r['complete_candidate_centre_residual_axis_ratio_upper'])))
                  for r in output_rows],seconds=result['elapsed_seconds'],
            peak_RSS_KiB=result['peak_RSS_KiB'])),flush=True)
    except Exception as error:
        save(Path(str(a.out_prefix)+'-failure.json'),dict(status='Incomplete actual adjoint source functional',
            error=repr(error),config=config,completed_segments=completed,counts=counts,
            elapsed_seconds=time.monotonic()-began,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        raise


if __name__=='__main__':
    main()
