#!/usr/bin/env python3
"""Refine the SAME five true R48 moments on the original material panels.

The raw source identity is certified for cells10/11 before using R65's
analytic source jets.  Critical points of w are bracketed; only those
tiny strips use a nonnegative range-times-length enclosure.  Taylor
coefficients at an interval of base points rigorously bound the integral
remainder.  No radius/ODE trajectory or candidate coefficient is changed.

Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
import resource
import time

from flint import arb, arb_series, ctx

from closure_split_joint_io_v2 import read, iter_array, digest
from closure_real_head_source_enclosure import exact_q, power2
from closure_real_linear_head_enclosure import PositiveKernels
from tail_r33_middle_ordered_physical import SourceValues
from closure_taylor_cut_slope_v2 import (source_series, monotone_parts, ball,
    record, intersect, add_error)
from closure_outer_taylor_shared_flow import raw_source_identity
from tail_outer_weighted_compatible import MOMENT_KEYS
from tail_outer_candidate_domain import nonnegative_integral


EXPECTED = {
 'closure_taylor_cut_slope_v2.py': '8e150b6fe16c33da98043bc7ebe952abf123e2f7c8da8ebbfb10bfec700fb5ea',
 'closure_outer_taylor_shared_flow.py': '81d8bd9ad3da434eb8ab98d381a32a09bbe7aca5fa3be8a0bfe493ccd62455b7',
 'closure_real_head_source_enclosure.py': '97ff78a171b284cd8d5acc8dc233bcfe1f0b7c428ce2fbbd5b7104bd0ecb8c47',
 'closure_real_linear_head_enclosure.py': '1b8023b53eeca7a0ef28816a99b1b7d4a43f025c2482afae9e88db572e174b8e',
 'tail_r33_middle_ordered_physical.py': 'ac1bb495b33a37f7f88b6b7258a88a466c205cb452141668b6c454f88386008e',
 'tail_outer_weighted_compatible.py': '03c88b010447c78e4fb6bb26f0d3704fafd23510d16cc00084f315daa07f3d1b',
 'tail_outer_candidate_domain.py': '17d6b7d85be80f8f40b3eec411ae49a73c51c6b624d030df57b94202a7d08690',
}


def finite(x):
    if not x.is_finite():
        raise ArithmeticError('The true moment enclosure is nonfinite')
    return x


def basis(u):
    # Products rather than generic real powers also work for signed Arb
    # interval arguments.  Mathematically these five functions are >=0
    # on the exact normalized source domain 0<=u<=1.
    v = 1-u
    return dict(zip(MOMENT_KEYS,
        (v*v*(1+2*u), u*v*v, u*u*(3-2*u), u*u*v, u*u*v*v)))


def moment_series(head, segment, before, total, base, span, order, sign):
    w, g = source_series(head, segment, base, span, order, sign)
    x = arb_series([base, span], prec=order+2)
    u = (before+segment['length']*x)/total
    ph = basis(u)
    return {'width': g, **{key:w*g*ph[key] for key in MOMENT_KEYS}}


def taylor_integrals(head, segment, before, total, left, right,
                     order, sign, tolerance):
    x0, span = exact_q(left), exact_q(right-left)
    xx = x0.union(exact_q(right))
    pc = moment_series(head, segment, before, total, x0, span, order, sign)
    dc = moment_series(head, segment, before, total, xx, span, order, sign)
    result, relative_remainder = {}, arb(0)
    for key in ('width',)+MOMENT_KEYS:
        value = sum((pc[key][k]/(k+1) for k in range(order)), arb(0))
        error = finite(abs(dc[key][order]).upper()/(order+1))
        enclosed = finite(add_error(value,error))
        if not enclosed > 0 or not error < tolerance*enclosed.lower():
            raise ArithmeticError('Subdivide the true positive-moment Taylor remainder')
        result[key] = enclosed
        relative_remainder = max(relative_remainder,(error/enclosed.lower()).upper())
    return result, relative_remainder


def root_integrals(head, segment, before, total, left, right):
    xx = exact_q(left).union(exact_q(right))
    source = head.source_point(segment,xx)
    w, ell = source['w'], source['log_w_x']
    E = 1+w*w
    gx = abs(w*ell)/(8*E*E.sqrt())+head.alpha*source['ro_x']/E
    if not w > 0 or not E > 0:
        raise ArithmeticError('The exact source on a critical-root bracket is not finite positive')
    u = (before+segment['length']*xx)/total
    ph = basis(u)
    span = exact_q(right-left)
    caps = {'width': finite(abs(gx).upper()*span),
            **{key:finite(abs(w*gx*ph[key]).upper()*span) for key in MOMENT_KEYS}}
    # Exact integral positivity, rather than the rounded lower endpoint of
    # a ball union, supplies this domain restriction.
    return {key: nonnegative_integral(record(arb(0).union(value.upper())))
            for key,value in caps.items()}


def save(path,data):
    path=Path(path)
    raw=(json.dumps(data,separators=(',',':'))+'\n').encode()
    if len(raw)>1_000_000:
        raise ValueError('Use a separate compressed group for large derived records')
    temporary=Path(str(path)+'.partial')
    temporary.write_bytes(raw)
    temporary.replace(path)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--ready',type=Path,required=True)
    p.add_argument('--cell-manifest',type=Path,required=True)
    p.add_argument('--out-prefix',type=Path,required=True)
    p.add_argument('--order',type=int,default=16)
    p.add_argument('--precision',type=int,default=224)
    p.add_argument('--remainder-bits',type=int,default=48)
    p.add_argument('--root-bits',type=int,default=160)
    p.add_argument('--rss-kib',type=int,default=40960)
    a=p.parse_args()
    if a.order<8 or a.precision<a.root_bits+32 or a.remainder_bits<24:
        raise ValueError('The actual Taylor/root precision safeguards were not retained')
    ctx.prec,ctx.cap,ctx.threads=a.precision,a.order+2,1
    began=time.monotonic()
    out=Path(str(a.out_prefix)+'-summary.json')
    if out.exists() or Path(str(a.out_prefix)+'-integrals-segment0.json.gz').exists():
        raise FileExistsError('Use a fresh complete true-moment prefix')
    for name,expected in EXPECTED.items():
        if digest(Path(__file__).with_name(name))!=expected:
            raise ValueError('A previously executed mathematical source changed: '+name)
    inputs={str(a.ready):digest(a.ready),str(a.cell_manifest):digest(a.cell_manifest)}
    old=read(a.cell_manifest);ready=read(a.ready)
    n=old['cell'];meta=old['original_metadata']
    if not all(old['checks'].values()) or inputs[str(a.ready)] not in meta['input_hashes'].values():
        raise ValueError('The same complete real source and positive-moment package are required')
    identity=raw_source_identity(ready,n)
    h=SourceValues(ready)
    source=PositiveKernels(h,225,92).source_cell(n)
    del ready
    segments=source['segments'];lengths=[s['length'] for s in segments]
    total_length=sum(lengths,arb(0))
    before=[sum(lengths[:j],arb(0)) for j in range(9)]
    tolerance=power2(-a.remainder_bits)
    counts=dict(original_panels=0,taylor=0,root_brackets=0,rejected=0)
    groups=[];active=None
    total={key:arb(0) for key in ('width',)+MOMENT_KEYS}
    worst_remainder=arb(0)
    cfg=dict(cell=n,order=a.order,precision=a.precision,remainder_bits=a.remainder_bits,
             root_bits=a.root_bits,source_coordinate='one normalized sum of the nine unequal original source lengths')
    def guard():
        peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak>a.rss_kib:
            raise MemoryError('Observed owned RSS exceeded its stop threshold: '+str(peak))
    def recovery(error=None):
        save(Path(str(a.out_prefix)+'-recovery.json'),dict(
            status='Completed original-panel integral groups; no incomplete full-cell claim',
            config=cfg,completed_groups=groups,counts=counts,input_hashes=inputs,
            entrypoint_sha256=digest(__file__),error=error,
            elapsed_seconds=time.monotonic()-began))
    try:
        old_groups=sorted(old['groups'],key=lambda g:g['source_segment'])
        if [g['source_segment'] for g in old_groups]!=list(range(9)):
            raise ValueError('All nine original source segments are required')
        for group in old_groups:
            j=group['source_segment'];segment=segments[j]
            path=Path(group['path'])
            if digest(path)!=group['sha256']:
                raise ValueError('An original complete positive-moment group changed')
            inputs[str(path)]=group['sha256']
            pieces=monotone_parts(segment,a.root_bits)
            target=Path(str(a.out_prefix)+f'-integrals-segment{j}.json.gz')
            if target.exists():
                raise FileExistsError('A completed original-panel integral group would be overwritten')
            active=gzip.open(target,'wt',compresslevel=9)
            active.write('{"cell":'+str(n)+',"segment":'+str(j)+
                ',"original_group_sha256":'+json.dumps(group['sha256'])+',"panels":[\n')
            subtotal={key:arb(0) for key in total}
            prior=Fraction(0);seen=0
            for i,row in enumerate(iter_array(path,'panels')):
                left,right=Fraction(row['x_left']),Fraction(row['x_right'])
                if row['segment']!=j or left!=prior or not left<right or row['possible_branches']!=['raw']:
                    raise ValueError('The original raw real panels do not form the same ordered complete cover')
                u=(before[j]+segment['length']*exact_q(left).union(exact_q(right)))/total_length
                intersect(u,ball(row['u']))
                intersect(segment['length']/total_length,ball(row['u_x']))
                values={key:arb(0) for key in total}
                for pl,pr,sign in pieces:
                    l,r=max(left,pl),min(right,pr)
                    if not l<r:
                        continue
                    stack=[(l,r,0)]
                    while stack:
                        ll,rr,depth=stack.pop()
                        if sign==0:
                            val=root_integrals(h,segment,before[j],total_length,ll,rr)
                            counts['root_brackets']+=1
                        else:
                            try:
                                val,error=taylor_integrals(h,segment,before[j],total_length,ll,rr,
                                    a.order,sign,tolerance)
                                worst_remainder=max(worst_remainder,error)
                                counts['taylor']+=1
                            except ArithmeticError:
                                if depth>=36:
                                    raise ArithmeticError('The same true moment panel exceeded its subdivision budget')
                                middle=(ll+rr)/2
                                stack.append((middle,rr,depth+1));stack.append((ll,middle,depth+1))
                                counts['rejected']+=1
                                continue
                        for key in values:
                            values[key]+=val[key]
                values['width']=intersect(finite(values['width']),ball(row['width']))
                for key in MOMENT_KEYS:
                    values[key]=intersect(finite(values[key]),ball(row['moments'][key]))
                if any(not value>0 for value in values.values()):
                    raise ArithmeticError('An entire positive original panel did not obtain a strict lower bound')
                for key in subtotal:
                    subtotal[key]+=values[key]
                rec=dict(panel=i,x_left=row['x_left'],x_right=row['x_right'],
                    original_parent=row['original_parent'],width=record(values['width']),
                    moments={key:record(values[key]) for key in MOMENT_KEYS})
                if seen:
                    active.write(',\n')
                active.write(json.dumps(rec,separators=(',',':')))
                seen+=1;counts['original_panels']+=1;prior=right
                if seen%64==0:
                    guard()
            active.write('\n]}\n');active.close();active=None
            if prior!=1 or seen!=group['panels']:
                raise ValueError('An original complete source segment was not covered')
            if target.stat().st_size>=5*1024*1024:
                raise ValueError('The complete original-panel integral group exceeds the file limit')
            for key in total:
                total[key]+=subtotal[key]
            item=dict(source_segment=j,panels=seen,path=str(target),bytes=target.stat().st_size,
                sha256=digest(target),original_group_path=str(path),original_group_sha256=group['sha256'],
                summed_width=record(subtotal['width']),
                summed_moments={key:record(subtotal[key]) for key in MOMENT_KEYS},
                monotone_parts=[dict(left=str(l),right=str(r),sign=s) for l,r,s in pieces])
            groups.append(item);recovery();guard()
            print(json.dumps(dict(event='complete_true_moment_segment',cell=n,segment=j,panels=seen,
                counts=counts,seconds=time.monotonic()-began,
                peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
        if counts['original_panels']!=old['panels']:
            raise ValueError('Every original real material panel is required')
        refined={key:intersect(total[key],ball(meta['total_positive_moments'][key])) for key in MOMENT_KEYS}
        physical_width=intersect(total['width'],ball(meta['outer_radius'])-ball(meta['inner_radius']))
        if any(not v>0 for v in refined.values()) or not physical_width>0:
            raise ArithmeticError('A complete true positive moment failed its original enclosure')
        gates=dict(all_original_true_material_panels_complete=True,
            whole_cell_cap_valley_weight_identity_explicitly_paid=True,
            same_original_source_coordinate_and_five_integrands=True,
            all_panel_and_total_integrals_intersect_original_enclosures=True,
            Taylor_derivative_remainder_paid_before_acceptance=True,
            all_critical_root_brackets_retained_as_nonnegative_integrals=True,
            fixed_candidate_coefficients_not_redefined=True,
            no_ODE_or_recalibration=True)
        result=dict(status='Sharper enclosures of the same five true weighted moments',
            config=cfg,cell=n,panels=counts['original_panels'],groups=groups,counts=counts,
            total_positive_moments={key:record(v) for key,v in refined.items()},
            physical_width=record(physical_width),worst_relative_Taylor_remainder=record(worst_remainder),
            source_identity=identity,gates=gates,all_gates=all(gates.values()),
            mathematical_definition='I_j=integral w(r)*phi_j(u(r)) dr for the fixed true source; boxes only enclose these constants',
            integral_remainder='At order p, coefficients at every panel base point enclose f^(p)/p!. Integral remainder <= max|coefficient_p|/(p+1), with scaled source span already in g.',
            original_material_manifest=str(a.cell_manifest),input_hashes=inputs,source_hashes=EXPECTED,
            entrypoint_sha256=digest(__file__),elapsed_seconds=time.monotonic()-began,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save(out,result)
        print(json.dumps(dict(event='complete_same_true_moments',summary=str(out),all_gates=True,
            counts=counts,total_b=str(refined['b']),peak_RSS_KiB=result['peak_RSS_KiB'])),flush=True)
    except Exception as error:
        if active is not None:
            active.close()
        recovery(repr(error))
        raise


if __name__=='__main__':
    main()
