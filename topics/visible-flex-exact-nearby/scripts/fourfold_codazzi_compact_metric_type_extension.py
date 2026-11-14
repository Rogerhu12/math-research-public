#!/usr/bin/env python3
"""Pay a larger actual nu range in the compact support; retain the true exterior.

Every changed prefix box is recomputed by the exact E_nu law. The already
certified root and positive exterior are unchanged because the bump is
identically zero there. This supplies a uniform target contract, not an
extension of any candidate-dependent PDE or geometry certificate.
"""
from __future__ import annotations
import argparse,gzip,json,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_compact_metric_type_cover import bump
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import real_interval
from fourfold_phase_metric_defect import record,save,sha


def read(p):return json.loads(gzip.decompress(Path(p).read_bytes()))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--type-cover',type=Path,default=Path('notes/2026-11-13-R133-compact-nu-full-type-cover-native.json.gz'))
    ap.add_argument('--prefix',type=Path,default=Path('notes/2026-11-13-Codazzi-true-target-r02-v1-native.json.gz'))
    ap.add_argument('--nu-left',type=Fraction,default=Fraction(-1,16))
    ap.add_argument('--nu-right',type=Fraction,default=Fraction(-1,40))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320
    if args.out.exists():raise FileExistsError('preserve every larger true-target attempt')
    old=read(args.type_cover);prefix=read(args.prefix)
    if (not old['complete'] or not old['exactly_one_real_K_root'] or not old['root_independent_of_nu']
        or not prefix['complete'] or old['inputs'].get(str(args.prefix))!=sha(args.prefix)
        or prefix['object_sha256']!=old['object_sha256']
        or prefix['parameter_half_width']!=old['parameter_half_width']
        or prefix['exact_center_parameter']!=old['exact_center_parameter']
        or not args.nu_left<=Fraction(old['exact_nu_interval'][0])
        or not Fraction(old['exact_nu_interval'][1])<=args.nu_right<0):
        raise ValueError('a complete same-object smaller true-target interval is required')
    doc={k:v for k,v in old.items() if k not in ('source_sha256','prefix_rows','wall_seconds','subdivisions','failure')}
    doc.update(kind='actual_full_compact_metric_curvature_type_extended',complete=False,
        source_sha256=sha(__file__),exact_nu_interval=[str(args.nu_left),str(args.nu_right)],
        inputs={**old['inputs'],str(args.type_cover):sha(args.type_cover)},
        original_type_source_sha256=old['source_sha256'],original_exact_nu_interval=old['exact_nu_interval'],
        changed_prefix_recomputed_for_entire_larger_nu_interval=True,
        unchanged_root_and_positive_rows_reused_only_after_exact_support_endpoint=True,
        candidate_dependent_Cauchy_geometry_and_inverse_constants_not_transferred=True,
        whole_real_radial_interval=False,prefix_rows=[],subdivisions=[],failure=None)
    nu=real_interval(args.nu_left,args.nu_right);cursor=Fraction(0);gaps=[]
    try:
        for j,row in enumerate(prefix['rows']):
            left,right=map(Fraction,row['interval']);gl,gr=map(Fraction,row['actual_scalar_germ'])
            if left!=cursor or not gl<=left<right<=gr:raise ValueError('the complete original prefix partition changed')
            c={k:box_from_record(row['true_target_coefficients'][k]) for k in ('K','E','beta','a','a1')}
            if not c['E']>0 or not c['a']>0:raise ValueError('true target positivity lost')
            cuts=[left,*[q for q in (Fraction(1,20),Fraction(9,50)) if left<q<right],right]
            for lo,hi in zip(cuts,cuts[1:]):
                h,h1=bump(lo,hi);ex=(nu*h).exp();En=c['E']*ex
                Kn=(c['K']+nu*c['beta']*h1/(2*c['E']))/ex
                gap=En-c['a1']**2
                item=dict(original_row=j,interval=[str(lo),str(hi)],actual_scalar_germ=row['actual_scalar_germ'],
                    K_nu=record(Kn),actual_E_nu=record(En),actual_E_nu_minus_a_prime_squared=record(gap),
                    strict_negative=bool(Kn<0),strict_rotational_chart=bool(gap>0))
                doc['prefix_rows'].append(item)
                if not Kn<0 or not gap>0:raise ValueError('larger true target curvature/chart gate failed at original row '+str(j))
                gaps.append(gap.lower())
            cursor=right
        if cursor!=Fraction(1,5):raise ValueError('the changed true prefix is incomplete')
        # These rows are exact unchanged original-target data, not fresh
        # evaluations at a different nu or a new interpretation of a fail.
        cursor=Fraction(1,5)
        for row in old['new_rows']:
            lo,hi=map(Fraction,row['interval'])
            if lo!=cursor or lo<Fraction(9,50):raise ValueError('the reused root data are inside a changed target region')
            K=box_from_record(row['K']);K1=box_from_record(row['K1'])
            if row['mode']=='negative' and not K<0:raise ValueError('unchanged negative root approach is unresolved')
            if row['mode']=='increasing' and not K1>0:raise ValueError('unchanged root monotonicity is unresolved')
            cursor=hi
        if cursor!=Fraction(old['root_strip'][1]):raise ValueError('unchanged actual root interval is incomplete')
        if not box_from_record(old['root_endpoint_values']['left'])<0 or not box_from_record(old['root_endpoint_values']['right'])>0:
            raise ValueError('unchanged true root endpoint signs are unresolved')
        for row in old['positive_rows']:
            lo,hi=map(Fraction,row['interval'])
            if lo!=cursor or not box_from_record(row['K'])>0:raise ValueError('unchanged positive suffix is incomplete')
            cursor=hi
        if cursor!=Fraction(3,2):raise ValueError('the full larger-nu target interval is incomplete')
        doc.update(complete=True,whole_real_radial_interval=True,
            unchanged_old_root_and_positive_rows_compared=True,
            bounds=dict(changed_prefix_K_upper=record(max(box_from_record(x['K_nu']).upper() for x in doc['prefix_rows']).upper()),
                changed_prefix_rotational_gap_lower=record(min(gaps).lower())))
    except Exception as exc:doc['failure']=dict(type=type(exc).__name__,message=str(exc))
    doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],prefix=len(doc['prefix_rows']),
        nu=doc['exact_nu_interval'],bounds=doc.get('bounds'),wall_seconds=doc['wall_seconds']),flush=True)
    if not doc['complete']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
