#!/usr/bin/env python3
"""Complete real target coefficients on the new genuine root collar.

The already proved type-cover intervals are replayed with the same full
primitive provider to retain all E/a/curvature jets for actual interfaces.
Only the new [.2,.239] rows are saved; the old 493 prefix is not duplicated.
No complex radial domain or turning operator is asserted.
"""
from __future__ import annotations
import argparse,gzip,json,time
from fractions import Fraction
from pathlib import Path
from flint import ctx
from fourfold_phase_codazzi_coefficients import CodazziCoefficientTarget
from fourfold_phase_metric_defect import record,save,sha


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--type-cover',type=Path,default=Path('notes/2026-11-13-R133-compact-nu-full-type-cover-native.json.gz'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320;ctx.cap=4
    if args.out.exists():raise FileExistsError('preserve all genuine collar attempts')
    types=json.loads(gzip.decompress(args.type_cover.read_bytes()))
    if (not types['complete'] or not types['exactly_one_real_K_root'] or types['object_sha256']!=sha(args.object)
        or types['dependencies']['fourfold_phase_codazzi_coefficients.py']!=sha(Path(__file__).with_name('fourfold_phase_codazzi_coefficients.py'))):
        raise ValueError('the same complete true type cover is required')
    target=CodazziCoefficientTarget(args.object,Fraction(types['parameter_half_width']),512,4096)
    doc=dict(kind='actual_complete_real_root_collar_coefficients',complete=False,
        source_sha256=sha(__file__),object_sha256=sha(args.object),inputs={str(p):sha(p) for p in (args.object,args.type_cover)},
        exact_center_parameter=types['exact_center_parameter'],parameter_half_width=types['parameter_half_width'],
        exact_requested_interval=['1/5','239/1000'],whole_affine_parameter_interval=True,
        complete_primitive_tail=True,whole_real_radial_interval=False,whole_real_angular_circle=True,
        compact_nu_identically_absent_on_this_interval=True,complex_radial_domain_not_certified=True,
        root_turning_operator_not_proved=True,rows=[],failure=None,
        coefficient_provider_sha256=sha(Path(__file__).with_name('fourfold_phase_codazzi_coefficients.py')),
        dependencies=types['dependencies'])
    cursor=Fraction(1,5);last=time.monotonic()
    try:
        for index,row in enumerate(types['new_rows']):
            left,right=map(Fraction,row['interval'])
            if left!=cursor:raise ValueError('the entire previous root-neighborhood partition is required')
            c=target.coefficients(left,right)
            if list(map(str,target.cell))!=row['actual_scalar_germ']:raise ValueError('the true scalar germ differs')
            if row['mode']=='negative' and not c['K']<0:raise ValueError('old strict negative collar gate lost')
            if row['mode']=='increasing' and not c['K1']>0:raise ValueError('old root monotonicity gate lost')
            doc['rows'].append(dict(previous_type_row=index,interval=[str(left),str(right)],
                actual_scalar_germ=list(map(str,target.cell)),
                true_target_coefficients={k:record(v) for k,v in c.items()},
                strict_negative_target=bool(c['K']<0),strict_increasing_curvature=bool(c['K1']>0),
                earlier_K_and_K1_records_exactly_equal=bool(record(c['K'])==row['K'] and record(c['K1'])==row['K1'])))
            cursor=right
            if time.monotonic()-last>20:
                doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
                print(dict(rows=len(doc['rows']),right=str(right),seconds=doc['wall_seconds']),flush=True);last=time.monotonic()
        if cursor!=Fraction(239,1000):raise ValueError('the complete collar is not covered')
        doc.update(complete=True,whole_real_radial_interval=True)
    except Exception as exc:doc['failure']=dict(type=type(exc).__name__,message=str(exc))
    doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],rows=len(doc['rows']),seconds=doc['wall_seconds']),flush=True)
    if not doc['complete']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
