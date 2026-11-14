#!/usr/bin/env python3
"""Independent flat proof-cover and endpoint sum for true beta-prime transfer.

No collector is imported. Exactly one complete recorded source is selected
per original span, all its leaves are flattened and tiled in exact Fractions,
and only certified upper endpoints enter the absolute integral bound.
"""
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_beta_flat_cover_independent_audit import sha,read,endpoint,scalar_fraction,record_bounds


def main():
    ctx.prec=256
    path=Path('notes/2026-11-12-beta-step3-true-derivative-complete-transfer-h1e5.json')
    report=read(path)
    if not report['complete']:raise ValueError('incomplete purported certificate')
    definition=read(report['center_object_path'],report['center_object_sha256'])
    center=Fraction(int(definition['delta_fraction']['numerator']),int(definition['delta_fraction']['denominator']))
    half=Fraction(report['exact_parameter_half_width']);box=list(map(Fraction,report['exact_parameter_interval']))
    if box!=[center-half,center+half] or center!=Fraction(report['exact_center_parameter']):raise ValueError('parameter identity differs')
    origin=Path(definition['origin_inputs']['path']);direction=Path(definition['direction']['path'])
    if sha(origin)!=report['origin_inputs_sha256'] or sha(direction)!=report['direction_sha256']:raise ValueError('changed raw family')
    waist,cut=Fraction(report['waist_width']),Fraction(report['fixed_cut'])
    with np.load(origin,allow_pickle=False) as z:
        knots={abs(Fraction.from_float(float(x))) for key in z.files if key.endswith('_knots') for x in z[key]}
    if any(0<x<waist for x in knots):raise ValueError('waist crosses a scalar knot')
    cuts=sorted({waist,cut}|{x for x in knots if waist<x<cut})
    spans=list(zip(cuts,cuts[1:]))
    sources={spec['path']:read(spec['path'],spec['sha256']) for spec in report['part_provenance']}
    for part in sources.values():
        for key in ['center_object_sha256','origin_inputs_sha256','direction_sha256',
                    'exact_center_parameter','exact_parameter_half_width','exact_parameter_interval','fixed_cut','waist_width']:
            if part[key]!=report[key]:raise ValueError('different exact bulk object: '+key)
    selected=report['selected_cells']
    if len(selected)!=len(spans) or len(spans)!=report['exact_original_knot_cells']:raise ValueError('incomplete original spans')
    leaves=[];source_counts=Counter()
    for index,((left,right),selection) in enumerate(zip(spans,selected)):
        if selection['index']!=index or Fraction(selection['left'])!=left or Fraction(selection['right'])!=right:
            raise ValueError('selected span differs from exact knot partition')
        source=selection['source_part'];part=sources[source]
        rows=sorted((row for row in part['accepted_cells'] if row['index']==index),key=lambda row:Fraction(row['left']))
        if len(rows)!=selection['subcells']:raise ValueError('selected leaf count differs')
        cursor=left
        for row in rows:
            a,b=Fraction(row['left']),Fraction(row['right'])
            if a!=cursor or not a<b<=right:raise ValueError('gap/overlap within selected complete span')
            cursor=b;leaves.append((a,b,row['derivative_absolute_integral_bound']))
        if cursor!=right:raise ValueError('selected source is only partial')
        source_counts[source]+=1
    leaves.sort(key=lambda x:x[0]);cursor=waist
    bound=endpoint(sources[report['waist_source_path']]['waist_derivative_absolute_integral_bound'],'upper')
    if not bound>=0:raise ValueError('negative waist absolute bound')
    for a,b,value in leaves:
        if a!=cursor:raise ValueError('flat cover gap/overlap')
        cursor=b;z=endpoint(value,'upper')
        if not z>=0:raise ValueError('negative cell absolute bound')
        bound+=z
    if cursor!=cut or len(leaves)!=report['selected_subcells']:raise ValueError('incomplete flat cover')
    collar=read(report['derivative_collar_path'],report['derivative_collar_sha256'])
    if not collar['complete'] or Fraction(collar['fixed_cut'])!=cut or list(map(Fraction,collar['exact_parameter_interval']))!=box:
        raise ValueError('collar object or cover differs')
    cvalue=collar['derivative_collar_integral'];clo,chi=endpoint(cvalue,'lower'),endpoint(cvalue,'upper')
    cbound=max(abs(clo),abs(chi)).upper();B=((bound+cbound)/2).upper()
    if not B<1326:raise ValueError('requested actual derivative bound not proved')
    point=read(report['center_beta_path'],report['center_beta_sha256'])
    movement=B*arb(half.numerator)/half.denominator
    lower=endpoint(point['beta'],'lower')-movement;upper=endpoint(point['beta'],'upper')+movement
    if not endpoint(report['beta'],'lower')<=lower.lower() or not upper.upper()<=endpoint(report['beta'],'upper'):
        raise ValueError('independent parameter transfer leaves saved enclosure')
    slo=2*arb(5).sqrt()*lower/arb.pi();shi=2*arb(5).sqrt()*upper/arb.pi()
    if not (52<slo and shi<53):raise ValueError('odd-grid neighbor changed')
    gap=(53-shi).lower();phase_gap=(gap*arb.pi()/(2*arb(5).sqrt())).lower()
    fourth=read('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_object.json')
    delta4=Fraction(int(fourth['delta_fraction']['numerator']),int(fourth['delta_fraction']['denominator']))
    margin=half-abs(delta4-center)
    if not margin>Fraction(1,2_000_000):raise ValueError('fourth point half-millionth box is not included')
    output=dict(kind='independent_complete_beta_derivative_flat_cover_and_transfer',complete=True,bits=ctx.prec,
        source_sha256=sha(__file__),arithmetic_helper_sha256=sha(Path(__file__).with_name('fourfold_beta_flat_cover_independent_audit.py')),
        original_report_sha256=sha(path),source_provenance=report['part_provenance'],exact_spans=len(spans),leaves=len(leaves),
        complete_spans_by_source=dict(source_counts),bulk_upper=scalar_fraction(bound.upper()),
        finite_part_collar_absolute_upper=scalar_fraction(cbound),beta_derivative_absolute_upper=scalar_fraction(B),
        beta=record_bounds(lower,upper),odd_norm_gap_lower=scalar_fraction(gap),beta_lattice_gap_lower=scalar_fraction(phase_gap),
        delta4_exact=str(delta4),delta4_symmetric_parameter_margin=str(margin),delta4_plus_minus_5e7_inside=True,
        limitation='Arithmetic/coverage audit; underlying analytic box enclosures and finite-part identity have separate source reviews.')
    out=Path('notes/2026-11-12-beta-derivative-independent-cover-and-transfer-audit.json');out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(spans=len(spans),leaves=len(leaves),bulk=str(bound),B=str(B),beta=output['beta'],phase_gap=str(phase_gap),delta4_margin=float(margin)),indent=2))


if __name__=='__main__':main()
