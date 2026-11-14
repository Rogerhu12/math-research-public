#!/usr/bin/env python3
"""Independent exact flat-cover and separate-endpoint audit of beta reports.

Does not import either collector or any geometry evaluator. It checks
provenance, all exact knot spans, every stored integral and final arithmetic;
the underlying analytic local enclosures require their separate source audit.
"""
from bisect import bisect_right
from fractions import Fraction
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from flint import arb, ctx


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path,digest=None):
    if digest is not None and sha(path)!=digest:raise ValueError('input changed: '+str(path))
    return json.loads(Path(path).read_text())


def endpoint(record,side):
    value=arb(record[side])
    return value.lower() if side=='lower' else value.upper()


def scalar_fraction(value):
    a,b=value.man_exp()
    return str(Fraction(int(a))*Fraction(2)**int(b))


def record_bounds(lo,hi):
    return dict(lower_exact=scalar_fraction(lo.lower()),upper_exact=scalar_fraction(hi.upper()),
                lower_display=str(lo),upper_display=str(hi))


def audit(path):
    report=read(path)
    if not report['complete']:raise ValueError('collector is incomplete')
    object_path=report.get('object_path',report.get('center_object_path'))
    object_sha=report.get('object_sha256',report.get('center_object_sha256'))
    definition=read(object_path,object_sha)
    exact_delta=Fraction(int(definition['delta_fraction']['numerator']),int(definition['delta_fraction']['denominator']))
    if exact_delta!=Fraction(report.get('exact_delta_fraction',report.get('exact_center_parameter'))):
        raise ValueError('object definition and reported exact parameter differ')
    origin=Path(definition['origin_inputs']['path'])
    if not origin.exists():origin=Path('data/phase_ring_continuation')/origin.name
    if sha(origin)!=report['origin_inputs_sha256']:raise ValueError('origin changed')
    direction=Path(definition['direction']['path'])
    if not direction.exists():direction=Path('data/phase_ring_continuation')/direction.name
    if sha(direction)!=report['direction_sha256']:raise ValueError('direction changed')
    waist,cut=Fraction(report['waist_width']),Fraction(report['fixed_cut'])
    with np.load(origin,allow_pickle=False) as values:
        knots={Fraction.from_float(float(x))*sgn for key in values.files if key.endswith('_knots')
               for x in values[key] for sgn in [-1,1]}
    cuts=sorted({waist,cut}|{x for x in knots if waist<x<cut})
    spans=list(zip(cuts,cuts[1:]))
    if len(spans)!=report['exact_original_knot_cells']:raise ValueError('common knot count differs')
    collar_path=report['collar_path'];collar=read(collar_path,report['collar_sha256'])
    if not collar['complete'] or Fraction(collar['fixed_cut'])!=cut:raise ValueError('collar does not join bulk')
    if endpoint(collar['root'],'lower')<=arb(cut.numerator)/cut.denominator:raise ValueError('cut reaches true root')
    identity_keys=['origin_inputs_sha256','direction_sha256']
    identity_keys+=['exact_parameter_interval','exact_center_parameter','exact_parameter_half_width'] if 'exact_parameter_interval' in report else ['exact_delta_fraction']
    leaves=[];waist_record=None;inputs=[{'path':str(path),'sha256':sha(path)},
        {'path':str(origin),'sha256':sha(origin)},{'path':collar_path,'sha256':sha(collar_path)}]
    for spec in report['part_provenance']:
        part=read(spec['path'],spec['sha256']);inputs.append({'path':spec['path'],'sha256':spec['sha256']})
        if part['failed_cells']:raise ValueError('terminal failures remain')
        if Fraction(part['fixed_cut'])!=cut or Fraction(part['waist_width'])!=waist:raise ValueError('different radial cover')
        if part['collar_sha256']!=report['collar_sha256']:raise ValueError('different collar')
        for key in identity_keys:
            if part[key]!=report[key] or collar[key]!=report[key]:raise ValueError('different exact object: '+key)
        if 'waist_integral' in part:
            if waist_record is not None:raise ValueError('duplicate waist integral')
            waist_record=part['waist_integral']
        for cell in part['accepted_cells']:
            a,b=Fraction(cell['left']),Fraction(cell['right'])
            if not a<b:raise ValueError('empty accepted interval')
            index=bisect_right(cuts,a)-1
            if index>=len(spans) or not cuts[index]<=a<b<=cuts[index+1] or index!=cell['index']:
                raise ValueError('accepted interval crosses an exact original knot')
            leaves.append((a,b,index,cell['integral']))
    if waist_record is None:raise ValueError('missing waist')
    leaves.sort(key=lambda item:(item[0],item[1]))
    cursor=waist;seen=set();lo=endpoint(waist_record,'lower');hi=endpoint(waist_record,'upper')
    for a,b,index,ball in leaves:
        if a!=cursor:raise ValueError('gap or overlap in flat exact cover')
        cursor=b;seen.add(index)
        lo+=endpoint(ball,'lower');hi+=endpoint(ball,'upper')
    if cursor!=cut or seen!=set(range(len(spans))):raise ValueError('incomplete cover')
    if len(leaves)!=report['selected_subcells']:raise ValueError('leaf count changed')
    blo=(lo+endpoint(collar['collar_integral'],'lower'))/2
    bhi=(hi+endpoint(collar['collar_integral'],'upper'))/2
    if not endpoint(report['beta'],'lower')<=blo.lower() or not bhi.upper()<=endpoint(report['beta'],'upper'):
        raise ValueError('independent sum leaves saved enclosure')
    scaled_lo=2*arb(5).sqrt()*blo/arb.pi();scaled_hi=2*arb(5).sqrt()*bhi/arb.pi()
    if not (52<scaled_lo and scaled_hi<53):raise ValueError('unexpected odd-grid neighbors')
    gap=(53-scaled_hi).lower();beta_gap=(gap*arb.pi()/(2*arb(5).sqrt())).lower()
    return dict(complete=True,source_files=inputs,exact_spans=len(spans),subcells=len(leaves),
        exact_parameter_interval=report.get('exact_parameter_interval'),exact_delta_fraction=report.get('exact_delta_fraction'),
        bulk=record_bounds(lo,hi),beta=record_bounds(blo,bhi),scaled_beta=record_bounds(scaled_lo,scaled_hi),
        odd_norm_gap_lower=scalar_fraction(gap),beta_lattice_gap_lower=scalar_fraction(beta_gap),
        odd_grid_argument='52<S<53; 53 is the closest odd integer, all Q<=51 or Q>=55 are farther')


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--reports',type=Path,nargs='+',required=True)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args();ctx.prec=224
    results=[audit(path) for path in args.reports]
    output=dict(kind='independent_exact_flat_cover_and_separate_endpoint_sum',complete=True,bits=ctx.prec,
        source_sha256=sha(__file__),results=results,
        limitation='Underlying analytic integration and primitive tails require the separate full source review.')
    args.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps([{'spans':r['exact_spans'],'leaves':r['subcells'],'beta':r['beta']} for r in results],indent=2))


if __name__=='__main__':main()
