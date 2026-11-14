#!/usr/bin/env python3
"""R131 true C0 continuation consuming the complete actual cubic residual.

The original producer schema and every input identity are retained. Only the
mathematically identical bound fields are passed to the already proved R131
barrier kernel. A separate original native certificate supplies the actual
initial weighted derivative, never the candidate's derivative error.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_linear_degeneracy_v2 import propagate,read_json,upper
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_two_jet_newton_source import record,save,sha


def parameter(x):
    return (Fraction(int(x['numerator']),int(x['denominator']))
            if isinstance(x,dict) else Fraction(x))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--native',type=Path,required=True)
    ap.add_argument('--initial',type=Path,default=Path('notes/2026-11-13-R131-C0-only-r005-native.json.gz'))
    ap.add_argument('--tube',type=Fraction,default=Fraction(1,16))
    ap.add_argument('--right',type=Fraction)
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();ctx.prec=a.bits
    if a.out.exists():raise FileExistsError('new output path required')
    d=read_json(a.native);initial=read_json(a.initial)
    if (d.get('kind')!='actual_complete_Codazzi_cubic_target_cleared_polynomial_residual'
        or not d.get('complete') or d.get('failure') is not None
        or d['covered_interval']!=d['exact_requested_interval']
        or not d.get('whole_affine_parameter_interval') or not d.get('whole_real_angular_circle')
        or not d.get('exact_denominator_clearing') or not d.get('full_target_cubic_remainder')
        or not d.get('every_exact_candidate_and_scalar_germ_join_retained')):
        raise ValueError('complete actual cleared numerator input required')
    producer=Path(__file__).with_name('fourfold_codazzi_cubic_cleared_residual.py')
    if sha(producer)!=d['source_sha256']:raise ValueError('actual residual producer changed')
    for path,digest in d['inputs'].items():
        if sha(Path(path))!=digest:raise ValueError('actual residual input changed: '+path)
    for name,digest in d['dependencies'].items():
        if sha(Path(__file__).with_name(name))!=digest:raise ValueError('actual residual dependency changed: '+name)
    if (not initial.get('complete') or not initial.get('whole_affine_parameter_interval')
        or not initial.get('whole_real_angular_circle')
        or initial['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_linear_degeneracy.py'))
        or initial['object_sha256']!=d['object_sha256']
        or parameter(initial['exact_center_parameter'])!=parameter(d['exact_center_parameter'])
        or Fraction(initial['parameter_half_width'])!=Fraction(d['parameter_half_width'])):
        raise ValueError('independent actual initial waist identity mismatch')
    for name,digest in initial['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=digest:raise ValueError('actual initial dependency changed: '+name)
    waist=initial['initial_actual_weighted_derivative']
    if not waist['whole_parameter_interval'] or not waist['whole_real_angular_circle']:
        raise ValueError('incomplete actual initial weighted derivative')
    weighted=upper(waist['weighted_gradient_upper'])
    if a.tube<=0 or not weighted.is_finite():raise ValueError('invalid actual C0 barrier data')
    # This local argument dictionary is an explicit schema adapter. It does
    # not rewrite either original report or claim a different producer kind.
    original_right=Fraction(d['exact_requested_interval'][1])
    right=a.right if a.right is not None else original_right
    if not 0<right<=original_right:raise ValueError('requested prefix outside the complete actual native')
    selected=[]
    for item in d['rows']:
        left,end=map(Fraction,item['interval'])
        if left>=right:break
        row=dict(item)
        row['interval']=[str(left),str(min(end,right))]
        selected.append(row)
    kernel_input=dict(initial_error=d['actual_initial_error'],rows=selected,
                      exact_requested_interval=['0',str(right)])
    result=propagate(kernel_input,weighted,exact_arb(a.tube))
    out=dict(kind='R131_true_C0_prefix_from_complete_cubic_cleared_residual',
        complete=True,continuation_certified=result['passed'],closed_surface_complete=False,
        consumer_revision=5,source_sha256=sha(__file__),
        inputs={str(p):sha(p) for p in (a.native,a.initial,producer)},
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,
        object_sha256=d['object_sha256'],candidate_sha256=d['candidate_sha256'],
        exact_center_parameter=d['exact_center_parameter'],parameter_half_width=d['parameter_half_width'],
        exact_requested_interval=['0',str(right)],original_native_interval=d['exact_requested_interval'],
        original_bounds_restricted_to_closed_prefix=True,tube=str(a.tube),bits=a.bits,
        original_native_kind=d['kind'],initial_actual_weighted_derivative=waist,
        actual_initial_dependencies=initial['dependency_sha256'],barrier=result,
        reads_candidate_second_derivative=False,reads_residual_theta_derivative=False,
        reads_R134_Sobolev_error_gate=False,uses_C1_error_Riccati_gate=False,
        dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            'fourfold_codazzi_linear_degeneracy_v2.py','fourfold_codazzi_linear_degeneracy.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_two_jet_newton_source.py')},
        scope='Same actual target and waist; only the passed full interval is certified. R131 uses the independently paid initial weighted derivative. Neither a failed request nor a finite candidate is promoted to a true solution.')
    save(a.out,out)
    print(dict(continuation_certified=result['passed'],covered_interval=result['covered_interval'],
        failed_row=result.get('failed_row'),final_C0=result.get('final_C0_barrier'),
        actual_gap=result.get('actual_gap_lower'),out=str(a.out)),flush=True)


if __name__=='__main__':main()
