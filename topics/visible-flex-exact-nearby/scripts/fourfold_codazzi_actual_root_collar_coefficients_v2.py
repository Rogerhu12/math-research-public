#!/usr/bin/env python3
"""Finish the actual real root collar from a verified complete-row prefix.

The original incomplete report is immutable. Its saved rows were appended
only after the full native coefficient calculation returned. This consumer
checks their source, object, partition, germ, and strict gates, then performs
the missing rows. Only the union is called a complete collar certificate.
"""
from __future__ import annotations
import argparse,gzip,json,time
from fractions import Fraction
from pathlib import Path
from flint import ctx
from fourfold_phase_codazzi_coefficients import CodazziCoefficientTarget
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record,save,sha


def read(p):return json.loads(gzip.decompress(Path(p).read_bytes()))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--type-cover',type=Path,default=Path('notes/2026-11-13-R133-compact-nu-full-type-cover-native.json.gz'))
    ap.add_argument('--prefix',type=Path,default=Path('notes/2026-11-13-R133-actual-root-collar-complete-coefficients-native.json.gz'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320;ctx.cap=4
    if args.out.exists():raise FileExistsError('preserve every original and resumed attempt')
    types=read(args.type_cover);old=read(args.prefix)
    provider=Path(__file__).with_name('fourfold_phase_codazzi_coefficients.py')
    original=Path(__file__).with_name('fourfold_codazzi_actual_root_collar_coefficients.py')
    if (not types['complete'] or not types['exactly_one_real_K_root'] or old['complete']
        or old['failure'] is not None or old['source_sha256']!=sha(original)
        or old['object_sha256']!=sha(args.object) or types['object_sha256']!=sha(args.object)
        or old['coefficient_provider_sha256']!=sha(provider)
        or types['dependencies']['fourfold_phase_codazzi_coefficients.py']!=sha(provider)
        or old['inputs'].get(str(args.type_cover))!=sha(args.type_cover)
        or old['inputs'].get(str(args.object))!=sha(args.object)
        or old['parameter_half_width']!=types['parameter_half_width']
        or old['exact_center_parameter']!=types['exact_center_parameter']):
        raise ValueError('the original saved complete-row prefix has a different identity')
    fields={'a','a1','a2','a3','E','E1','E2','K','K1','gamma','gamma1','gamma2','beta','primitive_tail'}
    cursor=Fraction(1,5)
    for index,row in enumerate(old['rows']):
        source=types['new_rows'][index];left,right=map(Fraction,row['interval'])
        if (row['previous_type_row']!=index or left!=cursor or row['interval']!=source['interval']
            or row['actual_scalar_germ']!=source['actual_scalar_germ']
            or not fields<=set(row['true_target_coefficients'])
            or not row['earlier_K_and_K1_records_exactly_equal']
            or any(row['true_target_coefficients'][k]!=source[k] for k in ('K','K1','primitive_tail'))):
            raise ValueError('an original complete saved row is missing or has changed')
        K=box_from_record(row['true_target_coefficients']['K'])
        K1=box_from_record(row['true_target_coefficients']['K1'])
        if source['mode']=='negative' and not K<0:raise ValueError('saved strict negative gate lost')
        if source['mode']=='increasing' and not K1>0:raise ValueError('saved root monotonicity gate lost')
        if row['strict_negative_target']!=bool(K<0) or row['strict_increasing_curvature']!=bool(K1>0):
            raise ValueError('saved strict flags do not describe the actual bounds')
        cursor=right
    count=len(old['rows'])
    if not 0<count<len(types['new_rows']):raise ValueError('the input must be a proper nonempty saved prefix')
    doc={k:v for k,v in old.items() if k not in ('source_sha256','wall_seconds','rows','failure')}
    doc.update(kind='actual_complete_real_root_collar_coefficients_resumed_v2',complete=False,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.object,args.type_cover,args.prefix)},
        original_saved_prefix_rows=count,original_planned_rows=len(types['new_rows']),
        original_report_complete=False,original_report_failure=None,
        observed_original_process_status='the previous tool session 57704 was unavailable when polled; no exit code or cause is inferred',
        complete_saved_rows_consumed_without_changing_original=True,
        original_complete_row_source_sha256=sha(original),rows=list(old['rows']),failure=None)
    target=CodazziCoefficientTarget(args.object,Fraction(types['parameter_half_width']),512,4096)
    last=time.monotonic()
    try:
        for index in range(count,len(types['new_rows'])):
            source=types['new_rows'][index];left,right=map(Fraction,source['interval'])
            if left!=cursor:raise ValueError('the saved and new closed boxes are not contiguous')
            c=target.coefficients(left,right)
            if list(map(str,target.cell))!=source['actual_scalar_germ']:raise ValueError('actual scalar germ changed')
            if source['mode']=='negative' and not c['K']<0:raise ValueError('strict negative gate unresolved')
            if source['mode']=='increasing' and not c['K1']>0:raise ValueError('root monotonicity gate unresolved')
            equal=all(record(c[k])==source[k] for k in ('K','K1','primitive_tail'))
            if not equal:raise ValueError('full native replay differs from the previous actual type bounds')
            doc['rows'].append(dict(previous_type_row=index,interval=[str(left),str(right)],
                actual_scalar_germ=list(map(str,target.cell)),
                true_target_coefficients={k:record(v) for k,v in c.items()},
                strict_negative_target=bool(c['K']<0),strict_increasing_curvature=bool(c['K1']>0),
                earlier_K_and_K1_records_exactly_equal=True))
            cursor=right
            if time.monotonic()-last>20:
                doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
                print(dict(rows=len(doc['rows']),right=str(right),seconds=doc['wall_seconds']),flush=True)
                last=time.monotonic()
        if cursor!=Fraction(239,1000):raise ValueError('the entire collar is not covered')
        doc.update(complete=True,whole_real_radial_interval=True,new_native_rows=len(doc['rows'])-count)
    except Exception as exc:doc['failure']=dict(type=type(exc).__name__,message=str(exc))
    doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],rows=len(doc['rows']),seconds=doc['wall_seconds']),flush=True)
    if not doc['complete']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
