#!/usr/bin/env python3
"""True whole-parameter root enclosure and exact common candidate germs.

A floating point is only a proposal. The complete original target and its
infinite primitive remainder provide the curvature and derivative bounds.
The final rational endpoints, signs, and all candidate-node comparisons
are certified. A real common germ is not a complex radial-domain bound.
"""
from __future__ import annotations
import argparse,gzip,json,math,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_codazzi_coefficients import CodazziCoefficientTarget
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_reciprocal_candidate_tools import COORDINATES
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha


def dyadic(x):return Fraction.from_float(float(x))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--type-cover',type=Path,default=Path('notes/2026-11-13-R133-compact-nu-full-type-cover-native.json.gz'))
    ap.add_argument('--candidate',type=Path,action='append',required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320;ctx.cap=4
    if args.out.exists():raise FileExistsError('preserve every genuine root attempt')
    types=json.loads(gzip.decompress(args.type_cover.read_bytes()))
    provider=Path(__file__).with_name('fourfold_phase_codazzi_coefficients.py')
    if (not types['complete'] or not types['exactly_one_real_K_root']
        or not types['root_independent_of_nu'] or types['object_sha256']!=sha(args.object)
        or types['dependencies']['fourfold_phase_codazzi_coefficients.py']!=sha(provider)):
        raise ValueError('a complete same-object unique-root cover is required')
    increasing=[r for r in types['new_rows'] if r['mode']=='increasing']
    left,right=map(Fraction,types['root_strip'])
    if (Fraction(increasing[0]['interval'][0])!=left or Fraction(increasing[-1]['interval'][1])!=right
        or any(a['interval'][1]!=b['interval'][0] for a,b in zip(increasing,increasing[1:]))):
        raise ValueError('the entire unique-root interval needs strict derivative bounds')
    derivative=box_from_record(increasing[0]['K1'])
    for row in increasing[1:]:derivative=derivative.union(box_from_record(row['K1']))
    if not derivative>0:raise ValueError('the complete root derivative does not separate from zero')
    target=CodazziCoefficientTarget(args.object,Fraction(types['parameter_half_width']),512,4096)
    point=Fraction('0.2383968742999')
    if not left<point<right:raise ValueError('the trial point must lie in the already proved root interval')
    coefficients=target.coefficients(point,point);germ=list(map(Fraction,target.cell))
    image=exact_arb(point)-coefficients['K']/derivative
    # These floating roundings select exact rational endpoints only. Strict
    # directed inclusion and true endpoint signs below are the actual gates.
    scale=10**13
    lo=Fraction(math.floor(float(image.lower())*scale)-2,scale)
    hi=Fraction(math.ceil(float(image.upper())*scale)+2,scale)
    if not exact_arb(lo)<image.lower() or not image.upper()<exact_arb(hi):
        raise ValueError('the rational endpoints do not enclose the directed Newton image')
    if not left<lo<hi<right or hi-lo>Fraction(1,10**8):raise ValueError('tight root width gate failed')
    cl=target.coefficients(lo,lo);gl=list(map(Fraction,target.cell))
    cr=target.coefficients(hi,hi);gr=list(map(Fraction,target.cell))
    if gl!=germ or gr!=germ or not cl['K']<0 or not cr['K']>0:
        raise ValueError('whole-parameter root endpoint signs or the common scalar germ are unresolved')
    doc=dict(kind='actual_whole_eta_unique_root_and_common_candidate_germs',complete=False,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.object,args.type_cover,*args.candidate)},
        object_sha256=sha(args.object),exact_center_parameter=types['exact_center_parameter'],
        parameter_half_width=types['parameter_half_width'],exact_nu_interval=types['exact_nu_interval'],
        whole_affine_parameter_interval=True,complete_original_primitive_and_tail=True,
        root_independent_of_compact_metric_nu=True,original_unique_root_interval=types['root_strip'],
        original_complete_positive_root_derivative=record(derivative),trial_point=str(point),
        true_point_coefficients={k:record(v) for k,v in coefficients.items()},
        directed_mean_value_root_image=record(image),exact_root_interval=[str(lo),str(hi)],
        exact_root_width=str(hi-lo),true_left_K=record(cl['K']),true_right_K=record(cr['K']),
        actual_common_scalar_germ=list(map(str,germ)),candidate_germs=[],failure=None,
        complex_radial_denominator_domain_not_certified=True,body_PDE_or_turning_inverse_not_proved=True,
        dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            'fourfold_phase_codazzi_coefficients.py','fourfold_codazzi_candidate_shards.py',
            'fourfold_codazzi_reciprocal_candidate_tools.py','fourfold_codazzi_rotational_cap_jacobi.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_metric_defect.py')})
    common_left,common_right=germ
    for path in args.candidate:
        saved=load_candidate(path);meta=json.loads(str(saved['metadata']))
        if meta['coordinates']!=COORDINATES or meta['object_sha256']!=sha(args.object):
            raise ValueError('a supplied full candidate belongs to a different physical object')
        nu=Fraction(meta['exact_float_nu']);nulo,nuhi=map(Fraction,types['exact_nu_interval'])
        if nu!=dyadic(meta['nu']) or not nulo<=nu<=nuhi:raise ValueError('candidate nu is outside the actual uniform type cover')
        nodes=list(map(dyadic,saved['radial_nodes']));j=bisect_right(nodes,lo)-1
        if not 0<=j<len(nodes)-1 or not nodes[j]<lo<hi<nodes[j+1]:
            raise ValueError('the complete true root box meets a candidate PPoly join')
        common_left=max(common_left,nodes[j]);common_right=min(common_right,nodes[j+1])
        doc['candidate_germs'].append(dict(candidate=str(path),candidate_sha256=sha(path),
            amplitude=str(dyadic(meta['amplitude'])),actual_fixed_nu=str(nu),modes=int(meta['modes']),
            exact_candidate_piece=j,exact_piece_interval=list(map(str,nodes[j:j+2])),
            exact_root_to_left_piece_margin=str(lo-nodes[j]),exact_root_to_right_piece_margin=str(nodes[j+1]-hi),
            metadata=meta,complete_candidate_identity_checked=True))
    if not common_left<lo<hi<common_right:raise ValueError('there is no common real polynomial germ about the entire root box')
    doc.update(complete=True,common_real_analytic_germ=list(map(str,(common_left,common_right))),
        exact_root_to_common_left_margin=str(lo-common_left),exact_root_to_common_right_margin=str(common_right-hi),
        all_candidate_PPoly_joins_outside_entire_root_box=True,wall_seconds=time.monotonic()-started)
    save(args.out,doc)
    print(dict(complete=True,root=doc['exact_root_interval'],width=doc['exact_root_width'],
        common_germ=doc['common_real_analytic_germ'],candidates=len(doc['candidate_germs']),wall_seconds=doc['wall_seconds']),flush=True)


if __name__=='__main__':main()
