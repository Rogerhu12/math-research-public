#!/usr/bin/env python3
"""Attach actual all-frequency and directed-error budgets to a float q table."""
from __future__ import annotations
import argparse,gzip,json,math
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record,sha


def read(p):
    raw=Path(p).read_bytes()
    return json.loads(gzip.decompress(raw)) if str(p).endswith('.gz') else json.loads(raw)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--floating',type=Path,default=Path('notes/2026-11-13-R133-cap-cut-r15-q256-floating.json'))
    ap.add_argument('--native',type=Path,default=Path('notes/2026-11-13-R133-cap-cut-r15-q256-native.json.gz'))
    ap.add_argument('--screening',type=Path,default=Path('notes/2026-11-13-R133-cap-analytic-screening-r15-mu3halves-native.json.gz'))
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();ctx.prec=320
    if args.out.exists():raise FileExistsError('preserve the original and derived q tables')
    f,n,s=map(read,(args.floating,args.native,args.screening))
    if (not f['success'] or not n['complete'] or not n['entire_finite_vector_certified']
        or n['inputs'].get(str(args.floating))!=sha(args.floating)
        or n['inputs'].get(str(args.screening))!=sha(args.screening)
        or not s['complete'] or not s['curvature_screening_certified']
        or not s['all_Fourier_modes_retained'] or n['modes']!=f['modes']
        or s['exact_requested_interval']!=['3/2','25/8']):raise ValueError('complete same-object q inputs required')
    qmax=box_from_record(s['weighted_constants']['q_upper']).upper()
    if not qmax<arb(53)/50:raise ValueError('the asserted all-mode tail bound does not follow')
    errors=[]
    for frequency,value,e in zip(f['physical_frequencies'],f['q_values'],n['entries']):
        if e['physical_frequency']!=frequency:raise ValueError('full finite q ordering differs')
        lo=box_from_record(e['q_lower']).lower();hi=box_from_record(e['q_upper']).upper();v=arb(value)
        if not lo<v<hi:raise ValueError('actual floating value is outside its directed q enclosure')
        errors.append(max((v-lo).upper(),(hi-v).upper()).upper())
    if len(errors)!=f['modes']:raise ValueError('a finite q entry is missing')
    doc=dict(f)
    doc.update(kind='floating_actual_cap_cut_regular_q_vector_with_complete_true_error_budget',
        derived_source_sha256=sha(__file__),original_floating_sha256=sha(args.floating),
        directed_vector_path=str(args.native),directed_vector_sha256=sha(args.native),
        complete_screening_path=str(args.screening),complete_screening_sha256=sha(args.screening),
        all_nonmean_q_abs_upper=1.06,all_nonmean_q_abs_upper_exact='53/50',
        all_nonmean_q_actual_directed_upper=record(qmax),
        true_q_error_abs_upper=[math.nextafter(float(e),math.inf) for e in errors],
        true_q_error_directed_records=[record(e) for e in errors],
        true_q_error_uniform_upper=record(max(errors).upper()),
        exact_complete_boundary_error_contract='sum_retained err_m |c_m| + ||b_unretained||_A0 + (53/50)||c_unretained||_A0; add the actual nonlinear cap B/mean correction separately.',
        all_frequencies_above_the_table_are_retained=True,
        neither_floating_q_nor_zero_nonlinear_correction_is_claimed_exact=True)
    args.out.write_text(json.dumps(doc,indent=2,allow_nan=False)+'\n')
    print(dict(path=str(args.out),qmax=1.06,maximum_true_q_error=max(errors).str(12),modes=f['modes']),flush=True)


if __name__=='__main__':main()
