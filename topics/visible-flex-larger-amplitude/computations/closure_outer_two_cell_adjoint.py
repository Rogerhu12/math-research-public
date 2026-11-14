#!/usr/bin/env python3
"""Two true outer cells, both terminal state functionals, and reusable kernels.

The original fixed real g, full signed source, global mu11, Taylor order,
root brackets and every material position are retained. The terminal
node10 q/v rows are advanced backwards through cells10 and11. No metric
integral is recomputed. Per-original-panel signed/absolute geometry
weights are saved with rigorous outward80-bit dyadic endpoints.

Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
import resource
import tempfile
import time

from flint import arb, ctx

from closure_outer_adjoint_source import (
    EXPECTED_OUTER_FLOW_SOURCE, EXPECTED_SOURCE_RECORDER, EXPECTED_TAYLOR,
    EXPECTED_SOURCE, EXPECTED_PROJECTIVE, EXPECTED_PB,
    rational_interval, transpose, functional_v_range, actual_panel_bounds)
from closure_real_head_source_enclosure import exact_q, power2
from closure_real_linear_head_enclosure import PositiveKernels
from closure_projective_interval_column import ProjectiveColumn
from closure_split_joint_io_v2 import digest, read_field, iter_array
from closure_taylor_cut_slope_v2 import (ball, record, intersect, monotone_parts,
    column_record, restore_column, save)
from closure_outer_taylor_shared_flow import taylor_global, root_global, raw_source_identity
from tail_r33_middle_ordered_physical import SourceValues


EXPECTED_ADJOINT = '776dbfd8cabd06247c8ddc38d989e1f833e7be96c44adfc9d4bfad927687eee0'


def compact_endpoint(value, direction, bits=80):
    """A dyadic endpoint rounded toward the specified exterior direction."""
    if not value.is_exact():
        raise ArithmeticError('A compact endpoint must start from an exact dyadic')
    m, e = value.man_exp()
    m, e = int(m), int(e)
    shift = max(0, abs(m).bit_length()-bits)
    if shift:
        base = 1 << shift
        m = m//base if direction < 0 else -((-m)//base)
        e += shift
    return [m, e]


def compact_ball(value):
    return [compact_endpoint(value.lower(), -1), compact_endpoint(value.upper(), 1)]


def compact_upper(value):
    return compact_endpoint(value.upper(), 1)


def matrix_records(values):
    return [[record(v) for v in row] for row in values]


def matrix_balls(values):
    return [[ball(v) for v in row] for row in values]


def zeros():
    return [[arb(0), arb(0)] for unused in range(2)]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('ready','flow','linear-cancellation','out-prefix'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--source-summary',type=Path,action='append',required=True)
    p.add_argument('--precision',type=int,default=256)
    p.add_argument('--order',type=int,default=24)
    p.add_argument('--root-bits',type=int,default=160)
    p.add_argument('--remainder-bits',type=int,default=100)
    p.add_argument('--rss-kib',type=int,default=40960)
    p.add_argument('--resume',type=Path)
    a=p.parse_args()
    if a.precision<a.root_bits+32 or a.order<4:
        raise ValueError('Keep the original Taylor/root precision')
    ctx.prec,ctx.cap,ctx.threads=a.precision,a.order+2,1
    started=time.monotonic()
    output=Path(str(a.out_prefix)+'.json')
    if output.exists():
        raise FileExistsError('Use a fresh complete two-cell functional prefix')
    expected={
        'closure_outer_adjoint_source.py':EXPECTED_ADJOINT,
        'closure_outer_taylor_shared_flow.py':EXPECTED_OUTER_FLOW_SOURCE,
        'closure_outer_candidate_source_record.py':EXPECTED_SOURCE_RECORDER,
        'closure_taylor_cut_slope_v2.py':EXPECTED_TAYLOR,
        'closure_real_head_source_enclosure.py':EXPECTED_SOURCE,
        'closure_projective_interval_column.py':EXPECTED_PROJECTIVE,
        'closure_real_linear_head_enclosure.py':EXPECTED_PB,
        'tail_r33_middle_ordered_physical.py':'ac1bb495b33a37f7f88b6b7258a88a466c205cb452141668b6c454f88386008e'}
    for name,wanted in expected.items():
        if digest(Path(__file__).with_name(name))!=wanted:
            raise ValueError('A frozen mathematical source changed: '+name)
    paths=[a.ready,a.flow,a.linear_cancellation]+a.source_summary
    hashes={str(path):digest(path) for path in paths}
    flow=json.loads(a.flow.read_text())
    cancellation=json.loads(a.linear_cancellation.read_text())
    if not all(flow['gates'].values()) or not cancellation['all_gates']:
        raise ValueError('The completed true two-cell flow and linear cancellation are required')
    if cancellation['input_hashes'].get(str(a.flow))!=hashes[str(a.flow)]:
        raise ValueError('The actual linear centre uses another background flow')
    sources={}
    for path in a.source_summary:
        doc=json.loads(path.read_text())
        n=doc['cell']
        if (n in sources or n not in (10,11) or not doc['all_gates']
                or doc['selected_cosine_modes']!=[2,4] or doc['tau']!='1/64'
                or doc['entrypoint_sha256']!=EXPECTED_SOURCE_RECORDER):
            raise ValueError('Supply the two complete unchanged actual source records')
        if doc['input_hashes'].get(str(a.ready))!=hashes[str(a.ready)]:
            raise ValueError('The recorded source metric differs')
        for dep,sha in doc['input_hashes'].items():
            if dep.endswith('response.json.gz') and cancellation['input_hashes'].get(dep)!=sha:
                raise ValueError('The candidate heights and original complete source differ')
        sources[n]=doc
    if sorted(sources)!=[10,11] or sum(d['panels'] for d in sources.values())!=10793:
        raise ValueError('All10793 original material positions are required')
    ready=dict(rationalDeepModel=read_field(a.ready,'rationalDeepModel'),
        shallowSourceParameters=read_field(a.ready,'shallowSourceParameters'))
    identities=[raw_source_identity(ready,n) for n in (10,11)]
    h=SourceValues(ready)
    del ready
    kernel=PositiveKernels(h,12,4)
    source_cells={n:kernel.source_cell(n) for n in (10,11)}
    h.cells.update(source_cells)
    endpoint_cell=next(c for c in flow['cell_rows'] if c['cell']==10)
    R=ball(endpoint_cell['radius'])
    mu=ball(flow['config']['global_mu_star'])
    modes=[2,4]
    phi={r['mode']:r for r in endpoint_cell['modes']}
    linear={r['mode']:r for r in cancellation['rows'] if r['endpoint_physical_node']==10}
    if sorted(phi)!=modes or sorted(linear)!=modes:
        raise ValueError('Both actual terminal height modes must be present')
    order=[(n,j) for n in (10,11) for j in range(8,-1,-1)]
    groups={(n,g['segment']):g for n,doc in sources.items() for g in doc['groups']}
    if sorted(groups)!=sorted(order):
        raise ValueError('Every source segment of both cells must be retained')
    vectors=[[ProjectiveColumn([arb(1),arb(0)]),ProjectiveColumn([arb(0),arb(1)])]
             for unused in modes]
    integrals,absolute,geometry_absolute,source_L1=zeros(),zeros(),zeros(),[arb(0),arb(0)]
    counts=dict(original_material=0,taylor=0,root_brackets=0,rejected=0)
    completed,kernel_groups=[],[]
    worst=arb(0)
    config=dict(cells=[11,10],reverse_cell_order=[10,11],modes=modes,
        terminal_readouts=['global_q','global_v'],terminal_physical_node=10,
        precision=a.precision,order=a.order,remainder_bits=a.remainder_bits,
        root_bits=a.root_bits,global_mu_star=record(mu),input_hashes=hashes,
        source_hashes=expected,entrypoint_sha256=digest(Path(__file__)),
        geometry_endpoint_bits=80)
    if a.resume:
        old=json.loads(a.resume.read_text())
        if old['config']!=config:
            raise ValueError('The recovery point uses another exact problem/arithmetic')
        vectors=[[restore_column(v) for v in row] for row in old['adjoint_columns']]
        integrals=matrix_balls(old['signed_source_integrals'])
        absolute=matrix_balls(old['absolute_source_integrals'])
        geometry_absolute=matrix_balls(old['absolute_geometry_integrals'])
        source_L1=[ball(v) for v in old['canonical_forcing_L1']]
        counts=old['counts']
        completed=[tuple(x) for x in old['completed_groups']]
        kernel_groups=old['kernel_groups']
        worst=ball(old['greatest_balanced_Taylor_remainder'])
        if completed!=order[:len(completed)]:
            raise ValueError('Recovery order is not the actual radial order')
        for group in kernel_groups:
            if digest(Path(group['path']))!=group['sha256']:
                raise ValueError('A completed geometry group changed')
    def guard():
        rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if rss>a.rss_kib:
            raise MemoryError('The owned two-cell adjoint exceeded its observed RSS gate: '+str(rss))
    active=None
    try:
        for n,j in order:
            if (n,j) in completed:
                continue
            group=groups[(n,j)]
            path=Path(group['path'])
            if digest(path)!=group['sha256']:
                raise ValueError('A position-resolved complete source group changed')
            segment=source_cells[n]['segments'][j]
            monotone=monotone_parts(segment,a.root_bits)
            kernel_path=Path(str(a.out_prefix)+f'-cell{n:03d}-segment{j}-kernels.json.gz')
            partial=kernel_path.with_name(kernel_path.name+'.partial')
            if kernel_path.exists() or partial.exists():
                raise FileExistsError('Use fresh names for an unfinished geometry group')
            active=gzip.open(partial,'wt',compresslevel=9)
            active.write(json.dumps(dict(cell=n,segment=j,terminal_physical_node=10,
                modes=modes,readouts=['global_q','global_v'],
                original_source_group_sha256=group['sha256'],
                compact_geometry_encoding='signed=[[lower_m,lower_e],[upper_m,upper_e]], absolute=[upper_m,upper_e]; all outward80bit dyadics',
                panels_reverse_radial_order=True))[:-1]+',"panels":[\n')
            group_count=0
            contributions=zeros()
            with tempfile.TemporaryFile(mode='w+b',dir=a.out_prefix.parent) as spool:
                offsets=[]
                first=last=None
                for g in iter_array(path,'panels'):
                    if g['segment']!=j or g['panel']!=len(offsets):
                        raise ValueError('The full original source order changed')
                    if first is None:first=g
                    last=g
                    offsets.append(spool.tell())
                    spool.write(json.dumps(g,separators=(',',':')).encode()+b'\n')
                if len(offsets)!=group['panels']:
                    raise ValueError('The whole original source group is required')
                segment['physical_inner_radius']=ball(first['radius_left'])
                segment['physical_outer_radius']=ball(last['radius_right'])
                if (n,j)==(10,8):intersect(segment['physical_outer_radius'],R)
                if Fraction(first['x_left'])!=0 or Fraction(last['x_right'])!=1:
                    raise ValueError('The entire source segment[0,1] must be retained')
                del first,last
                for index in range(len(offsets)-1,-1,-1):
                    spool.seek(offsets[index])
                    g=json.loads(spool.readline())
                    left,right=Fraction(g['x_left']),Fraction(g['x_right'])
                    radius=ball(g['radius_left'])
                    parts=[(max(left,lo),min(right,hi),sgn) for lo,hi,sgn in monotone
                           if max(left,lo)<min(right,hi)]
                    if not parts or parts[0][0]!=left or parts[-1][1]!=right:
                        raise ArithmeticError('The exact root partition misses true source positions')
                    accepted=[]
                    for lo,hi,sgn in parts:
                        segment['_monotone_sign']=sgn
                        stack=[(lo,hi,0)]
                        while stack:
                            aa,cc,depth=stack.pop()
                            try:
                                T,new_radius,error=(root_global(h,segment,aa,cc,radius,modes,mu)
                                    if sgn==0 else taylor_global(h,segment,aa,cc,radius,modes,
                                        a.order,power2(-a.remainder_bits),mu))
                                bounds=[actual_panel_bounds(h,segment,aa,cc,radius,g,m,mu) for m in modes]
                            except (ArithmeticError,ValueError,ZeroDivisionError) as err:
                                if sgn==0 or depth>=40:
                                    raise ArithmeticError('Unresolved true two-cell source panel '+
                                        str((n,j,index,aa,cc,sgn))+': '+str(err)) from err
                                mid=(aa+cc)/2
                                stack.extend([(mid,cc,depth+1),(aa,mid,depth+1)])
                                counts['rejected']+=1
                                continue
                            accepted.append((aa,cc,T,bounds))
                            radius=new_radius
                            counts['root_brackets' if sgn==0 else 'taylor']+=1
                            if sgn:worst=max(worst,error)
                            guard()
                    intersect(radius,ball(g['radius_right']))
                    source={r['mode']:ball(r['complete_source_cosine']) for r in g['selected_cosine_sources']}
                    direct,gs,ga,pa=zeros(),zeros(),zeros(),zeros()
                    for aa,cc,T,bounds in reversed(accepted):
                        dx=exact_q(cc-aa)
                        for k,m in enumerate(modes):
                            A,B,J=bounds[k]
                            source_L1[k]+=(J.upper()*abs(source[m]).upper()*dx).upper()
                            for l in range(2):
                                eta=functional_v_range(vectors[k][l],A,B)
                                weight=eta*J*dx
                                weight_abs=(abs(eta).upper()*J.upper()*dx).upper()
                                gs[k][l]+=weight
                                ga[k][l]+=weight_abs
                                direct[k][l]+=weight*source[m]
                                pa[k][l]+=(weight_abs*abs(source[m]).upper()).upper()
                                v=restore_column(column_record(vectors[k][l]))
                                v.advance(transpose(T[k]))
                                vectors[k][l]=v
                    kernel_rows=[]
                    for k,m in enumerate(modes):
                        centre=source[m].mid()
                        rad=abs(source[m]-centre).upper()
                        for l in range(2):
                            er=(rad*ga[k][l].upper()).upper()
                            recentred=centre*gs[k][l]+(-er).union(er)
                            value=intersect(direct[k][l],recentred)
                            integrals[k][l]+=value
                            contributions[k][l]+=value
                            absolute[k][l]+=pa[k][l]
                            geometry_absolute[k][l]+=ga[k][l]
                            kernel_rows.append(dict(mode=m,readout=l,
                                signed=compact_ball(gs[k][l]),absolute=compact_upper(ga[k][l])))
                    if group_count:active.write(',\n')
                    active.write(json.dumps(dict(panel=index,x_left=g['x_left'],x_right=g['x_right'],
                        weights=kernel_rows),separators=(',',':')))
                    counts['original_material']+=1
                    group_count+=1
                    guard()
            if group_count!=group['panels']:
                raise ValueError('A complete geometry panel range is missing')
            active.write('\n]}\n')
            active.close()
            active=None
            if partial.stat().st_size>5*1024*1024:
                raise ValueError('A complete reusable geometry group exceeds the repository cap')
            partial.rename(kernel_path)
            kernel_groups.append(dict(cell=n,segment=j,path=str(kernel_path),panels=group_count,
                bytes=kernel_path.stat().st_size,sha256=digest(kernel_path),
                source_group_path=str(path),source_group_sha256=group['sha256']))
            completed.append((n,j))
            checkpoint=dict(status='Complete true two-cell adjoint source group',config=config,
                completed_groups=completed,adjoint_columns=[[column_record(v) for v in row] for row in vectors],
                signed_source_integrals=matrix_records(integrals),
                absolute_source_integrals=matrix_records([[v.upper() for v in row] for row in absolute]),
                absolute_geometry_integrals=matrix_records([[v.upper() for v in row] for row in geometry_absolute]),
                canonical_forcing_L1=[record(v.upper()) for v in source_L1],
                this_segment_signed_integrals=matrix_records(contributions),
                kernel_groups=kernel_groups,counts=counts,greatest_balanced_Taylor_remainder=record(worst),
                elapsed_seconds=time.monotonic()-started,
                peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            cp=Path(str(a.out_prefix)+f'-completed-cell{n:03d}-segment{j}.json')
            if cp.exists():raise FileExistsError('A complete checkpoint would be overwritten')
            save(cp,checkpoint)
            print(json.dumps(dict(event='complete_two_cell_adjoint_group',cell=n,segment=j,
                counts=counts,kernel_bytes=kernel_path.stat().st_size,
                seconds=time.monotonic()-started,
                peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
        if completed!=order or counts['original_material']!=10793:
            raise ValueError('The complete two-cell radial range is absent')
        rows=[]
        for k,m in enumerate(modes):
            adj=[]
            for l in range(2):
                sub=[]
                for col in range(2):
                    lo,hi=vectors[k][l].component_bounds(col)
                    sub.append(record(intersect(lo.union(hi),
                        ball(phi[m]['global_gauge_fundamental_matrix'][l][col]))))
                adj.append(sub)
            S=ball(phi[m]['S0_true_Q'])
            factor=(R/h.rc)**(m*m-4)/S
            forcing=factor*integrals[k][0]
            centre=rational_interval(linear[m]['complete_head_lift_minus_outer_candidate_Q'])+forcing
            axis=rational_interval(linear[m]['canonical_parameter_axis'])
            rows.append(dict(mode=m,whole_true_adjoint_matrix_at_node12=adj,
                true_global_qv_forcing_vector=[record(v) for v in integrals[k]],
                absolute_global_qv_forcing_bounds=[record(v.upper()) for v in absolute[k]],
                absolute_global_qv_geometry_bounds=[record(v.upper()) for v in geometry_absolute[k]],
                signed_canonical_cut_forcing_contribution=record(forcing),
                absolute_canonical_cut_forcing_upper=record((abs(factor).upper()*absolute[k][0]).upper()),
                canonical_cut_geometry_factor=record(factor),
                complete_candidate_centre_residual_canonical_Q=record(centre),
                original_canonical_parameter_axis=record(axis),
                original_axis_ratio_upper=record((abs(centre).upper()/axis).upper()),
                unknown_outer_correction_nonlinearity_included=False))
        gates=dict(same_actual_real_g_and_original_two_cell_candidate=True,
            exact_global_mu11_no_interface_rescaling=True,
            all10793_original_panels_and_subpositions_paid=True,
            all_Taylor_remainders_and_real_root_brackets_paid=True,
            both_terminal_state_functionals_retained=True,
            all_four_true_background_matrix_entries_intersect=True,
            signed_source_has_complete_mean_and_inverse=True,
            complete_candidate_linear_forcing_cancelled=True,
            same_original_R63_R58_low_cut_feedback_retained=True,
            reusable_kernel_endpoints_outward80bit=True)
        result=dict(status='Actual two-cell complete source functionals and reusable position kernels',
            gates=gates,all_gates=True,cells=[11,10],endpoint_physical_node=10,modes=modes,
            rows=rows,config=config,source_identity=identities,kernel_groups=kernel_groups,
            counts=counts,greatest_balanced_Taylor_remainder=record(worst),
            source_functional='Each terminal global q/v row eta gives integral eta_v*(r/rc)^(m^2-4)*r^4*w^2/(sqrt12*mu11)*N_cos,m dx. Only q is converted to cut Q by (R/rc)^(m^2-4)/S0.',
            reusable_kernel_rule='For a source box [c-r,c+r] on an original panel, integral belongs to c*K_signed+[-r*K_abs,r*K_abs]. Do not multiply a signed kernel integral by a variable source interval without its absolute kernel.',
            complete_outer_correction_Green_and_Schur_inverse_paid=False,
            full46_or_infinite_frequency_outer_problem_paid=False,
            new_background_integrals=0,input_hashes=hashes,
            entrypoint_sha256=digest(Path(__file__)),elapsed_seconds=time.monotonic()-started,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save(output,result)
        guard()
        print(json.dumps(dict(event='complete_two_cell_functional',output=str(output),all_gates=True,
            rows=[dict(mode=r['mode'],forcing=str(ball(r['signed_canonical_cut_forcing_contribution'])),
                centre=str(ball(r['complete_candidate_centre_residual_canonical_Q']))) for r in rows],
            seconds=result['elapsed_seconds'],peak_RSS_KiB=result['peak_RSS_KiB'])),flush=True)
    except Exception as error:
        if active is not None:active.close()
        save(Path(str(a.out_prefix)+'-failure.json'),dict(status='Incomplete two-cell adjoint, no complete-range claim',
            error=repr(error),config=config,completed_groups=completed,kernel_groups=kernel_groups,
            counts=counts,elapsed_seconds=time.monotonic()-started,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        raise


if __name__=='__main__':main()
