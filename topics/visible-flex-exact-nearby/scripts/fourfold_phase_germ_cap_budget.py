#!/usr/bin/env python3
"""Conditional exact cap budgets from a completed true-germ domain cover.

The actual crossing geometry and field-modulus fees are computed with Arb.
The remaining hypotheses are an identical analytic reference Y whose complex
image stays in the listed domain, and a lower bound for Y_x only on each real
cap and the full complex label strip.  Neither is claimed by this report.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

from flint import arb,ctx
from fourfold_phase_domain_cover_verify import Closure,Time,ball,decode,digest


def record(x):
    return dict(ball=str(x),lower=str(x.lower()),upper=str(x.upper()),
                upper_float=float(x.upper()))


def nonnegative_upper(x):
    v=x.upper()
    return v if v>0 else arb(0)


def leaf_budget(doc,root):
    ta,tb=map(Time.parse,doc['exact_time_endpoints'])
    c,h=(ta+tb).scale(Fraction(1,2)),(tb-ta).scale(Fraction(1,2))
    cb,hb=c.value(),h.value()
    if hb>0:direction=1
    elif hb<0:direction=-1
    else:raise ValueError('physical time orientation is not separated')
    R=ball(Fraction(doc['time_radius']));theta_strip=Fraction(doc['physical_theta_strip'])
    source_rows=doc['germs'];cells=[tuple(map(Fraction,row['common_span']))for row in source_rows]
    center=root*cb.sin();primary=None
    for i,(a,b)in enumerate(cells):
        if ball(a)<=center.lower() and center.upper()<=ball(b):
            primary=i;break
    if primary is None:raise ValueError('the actual center cannot be assigned to a certified main germ')
    order=list(range(len(cells)))
    if direction<0:order.reverse()
    primary_position=order.index(primary)
    pairs=[];total=arb(0);supremum=arb(0)
    for pos,(ia,ib)in enumerate(zip(order,order[1:])):
        ka=cells[ia][1]if direction>0 else cells[ia][0]
        kb=cells[ib][0]if direction>0 else cells[ib][1]
        if ka!=kb:raise ValueError('adjacent chronological germs have different actual knots')
        ratio=ball(ka)/root
        if not ratio.lower()>-1 or not ratio.upper()<1:
            raise ValueError('cap is at or beyond the actual turn; ordinary matching cannot be used')
        tau=ratio.asin();cross=(tau-cb)/hb
        left=pos<primary_position
        cap=nonnegative_upper(cross+1 if left else 1-cross)
        rho=(R-abs(cross).upper()).lower()
        if not rho>0 or not cap<rho:
            raise ValueError('centered crossing disk does not cover the possible actual cap')
        m=(abs(arb(source_rows[ia]['true_field_moduli']['f']['ball'])).upper()
           +abs(arb(source_rows[ib]['true_field_moduli']['f']['ball'])).upper()).upper()
        half=abs(hb).upper()
        fee=(half*m*cap**4/(4*rho**3)).upper()
        amplitude=(half*m*cap**3/rho**3).upper()
        total=(total+fee).upper();supremum=(supremum+amplitude).upper()
        pairs.append(dict(first_germ_index=ia,second_germ_index=ib,
            exact_shared_radial_knot=str(ka),actual_crossing_tau=record(tau),
            actual_crossing_u=record(cross),active_side='left_of_crossing'if left else'right_of_crossing',
            possible_cap_length_upper=record(cap),centered_analytic_radius_lower=record(rho),
            sum_physical_field_moduli_upper=record(m),absolute_time_halfwidth_upper=record(half),
            integrated_h_times_physical_field_difference_upper=record(fee),
            uniform_h_times_physical_field_difference_upper=record(amplitude),
            matching_order=2,first_possible_nonzero_order=3))
    return dict(leg=doc['leg'],segment=doc['segment'],normalized_subspan=doc['normalized_subspan'],
        exact_time_endpoints=doc['exact_time_endpoints'],actual_center_radial_value=record(center),
        main_germ_index=primary,main_germ_common_span=list(map(str,cells[primary])),
        chronological_germ_indices=order,common_time_radius=str(Fraction(doc['time_radius'])),
        physical_theta_strip=str(theta_strip),pairs=pairs,
        integrated_h_times_physical_field_difference_upper=record(total),
        uniform_h_times_physical_field_difference_upper=record(supremum),
        interpretation='Divide the integrated fee by a proved uniform real-cap |Y_x| lower bound; the fee already includes |h|',
        required_reference_domain='One identical Y analytic on this local |u|<R and the full label strip, with its entire complex image inside the listed physical theta strip',
        true_small_field_error_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--index',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--bits',type=int,default=192)
    p.add_argument('--matching-proof',type=Path,default=Path('notes/2026-11-12-exact-germ-matching-and-cubic-caps.md'))
    args=p.parse_args();ctx.prec=args.bits
    raw=args.index.read_bytes();index=decode(args.index,raw)
    package=index['refined_root']
    if (not package.get('proved')or package['object_sha256']!=index['target_object_sha256']
        or package['root_certificate_sha256']!=index['target_root_sha256']):
        raise ValueError('the exact same-object refined true root is required')
    continuity={row['name']:row for row in package['scalar_continuity']}
    ordinary=['base','raw','shift','mean0','mean1','mean2']
    height=['height'+str(i)+'_primitive'for i in range(4)]
    if (any(name not in continuity or continuity[name]['minimum_interior_continuity']<4 for name in ordinary)
        or any(name not in continuity or continuity[name]['minimum_interior_continuity']<5 for name in height)):
        raise ValueError('the actual common scalar splines do not have the required matching jets')
    proof_sha=digest(args.matching_proof.read_bytes())
    root=arb(package['refined_root']['ball'])
    if not root.lower()>0:raise ValueError('positive true root enclosure required')
    closure=Closure(Path.cwd(),index['target_object_sha256'],index['target_root_sha256'])
    rows=[];total=arb(0);maximum=arb(0)
    for case in index['cases']:
        if not case.get('proved'):raise ValueError('only complete covered cases can supply cap domains')
        for leaf in case['leaves']:
            doc=closure.domain(leaf['path'],leaf['sha256'])
            row=leaf_budget(doc,root)
            row.update(domain_certificate_path=leaf['path'],domain_certificate_sha256=leaf['sha256'])
            rows.append(row)
            total=(total+arb(row['integrated_h_times_physical_field_difference_upper']['ball'])).upper()
            value=arb(row['uniform_h_times_physical_field_difference_upper']['ball']).upper()
            if value>maximum:maximum=value
    report=dict(kind='actual_crossing_geometry_and_conditional_cubic_cap_fees',status='complete',
        source_sha256=digest(Path(__file__).read_bytes()),cover_index_path=str(args.index),cover_index_sha256=digest(raw),
        target_object_sha256=index['target_object_sha256'],target_root_sha256=index['target_root_sha256'],
        exact_delta_fraction=index['exact_delta_fraction'],true_root_used=record(root),bits=args.bits,
        exact_scalar_continuity=package['scalar_continuity'],
        matching_proof_path=str(args.matching_proof),matching_proof_sha256=proof_sha,
        covered_cases=len(index['cases']),covered_leaves=len(rows),
        ordinary_crossing_pairs=sum(len(row['pairs'])for row in rows),
        source_whole_both_branches=bool(index.get('whole_both_branches')),
        integrated_h_times_physical_field_difference_upper=record(total),
        maximum_single_leaf_uniform_h_times_physical_field_difference_upper=record(maximum),
        rows=rows,domain_dependency_files=sorted(closure.files.values(),key=lambda r:r['path']),
        dependency_sha256={'fourfold_phase_domain_cover_verify.py':digest(Path(__file__).with_name('fourfold_phase_domain_cover_verify.py').read_bytes())},
        limitations=['The reference complex image condition has not been proved by this calculation',
            'No real-cap Y_x lower bound has been inserted; this is not an actual total R72 E',
            'Only completed listed domain leaves are covered; no missing time case is supplied',
            'The true small-field common M/A must also include this cap error',
            'Adjacent matching is used only at nonturn knots; no root germ is extrapolated for free'])
    data=(json.dumps(report,indent=2)+'\n').encode()
    if len(data)>1000000 and args.out.suffix!='.gz':raise ValueError('data above 1MB requires gzip')
    data=gzip.compress(data,mtime=0)if args.out.suffix=='.gz'else data
    if len(data)>5000000:raise ValueError('split the report under 5MB')
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_bytes(data)
    print(json.dumps(dict(leaves=len(rows),pairs=report['ordinary_crossing_pairs'],
        integrated_field_fee_before_q=record(total),sha256=digest(data))),flush=True)


if __name__=='__main__':main()

