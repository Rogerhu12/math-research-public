#!/usr/bin/env python3
"""True R131 continuation from complete positive-weight comparison boxes.

The bootstrap is tested in the unweighted error, max(Wp,Wq)*z<T, and
retains the actual gap and the independent true initial weighted gradient.
Every attempted tube, including a failed row, is preserved separately.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_linear_degeneracy_v2 import read_json,upper,lower
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_two_jet_newton_source import record,save,sha


def parameter(value):
    return Fraction(int(value['numerator']),int(value['denominator'])) if isinstance(value,dict) else Fraction(value)


def propagate(native,initial_gradient,tube):
    T=exact_arb(Fraction(tube));tiny=arb(2)**-180;inflate=1+arb(2)**-40
    z=(2*upper(native['actual_initial_error']['epsilon0'])+tiny).upper()
    gradient=(initial_gradient+tiny).upper();cursor=Fraction(0);rows=[]
    min_gap=None;min_k=None;max_error=arb(0);max_C1=arb(0);integrated=arb(0)
    for i,item in enumerate(native['rows']):
        left,right=map(Fraction,item['interval']);gl,gr=map(Fraction,item['actual_scalar_germ'])
        if left!=cursor or not gl<=left<right<=gr:raise ValueError('noncontiguous complete actual weight cover')
        wl,wu=lower(item['weight_lower']),upper(item['weight_upper'])
        rate=upper(item['rates'][tube]);rho=upper(item['original_rho0']);h=exact_arb(right-left)
        if not (wl>0 and wu>=wl and rate>=0 and rho>=0):raise ValueError('invalid complete positive comparison data')
        forcing=(rho/wl).upper();den=(1-h*rate).lower()
        if not den>0:
            rows.append(dict(native_row=i,interval=item['interval'],positive_affine_denominator=False,
                             denominator=record(den),rate=record(rate)))
            return dict(passed=False,failed_row=i,reason='positive_affine_denominator',
                        covered_interval=['0',str(cursor)],rows=rows)
        end=((z+h*forcing)/den*inflate+tiny).upper()
        margin=(end-z-h*(rate*end+forcing)).lower()
        error=(wu*end).upper();gap=(lower(item['original_candidate_gap'])-2*error).lower()
        k=lower(item['original_k_lower']);M=(upper(item['original_Mhat'])+error).upper()
        beta,kappa=upper(item['original_beta']),upper(item['original_kappa'])
        G=(beta*(2+4*M*M)+4*kappa).upper();newgrad=(gradient*(h*G).exp()).upper()
        gates=dict(positive_weights=bool(wl>0),positive_k=bool(k>0),
            weighted_affine_margin=bool(margin>0),unweighted_error_inside_tube=bool(error<T),
            strict_actual_gap=bool(gap>0),finite_true_weighted_gradient=bool(newgrad.is_finite()))
        C1=(newgrad/gap).upper() if all(gates.values()) else None
        rows.append(dict(native_row=i,interval=item['interval'],weight_lower=record(wl),weight_upper=record(wu),
            weighted_initial=record(z),weighted_final=record(end),weighted_rate=record(rate),
            weighted_source=record(forcing),weighted_affine_margin=record(margin),
            actual_unweighted_C0=record(error),actual_gap_lower=record(gap),actual_M=record(M),
            actual_weighted_gradient_initial=record(gradient),actual_weighted_gradient_final=record(newgrad),
            actual_first_angular_derivative_upper=record(C1) if C1 is not None else None,gates=gates))
        if not all(gates.values()):
            return dict(passed=False,failed_row=i,reason='actual_bootstrap_gate',
                        covered_interval=['0',str(cursor)],rows=rows)
        cursor=right;z=end;gradient=newgrad;integrated=(integrated+h*G).upper()
        min_gap=gap if min_gap is None else min(min_gap,gap).lower()
        min_k=k if min_k is None else min(min_k,k).lower()
        max_error=max(max_error,error).upper();max_C1=max(max_C1,C1).upper()
    if ['0',str(cursor)]!=native['exact_requested_interval']:raise ValueError('the full requested endpoint is missing')
    return dict(passed=True,covered_interval=['0',str(cursor)],rows=rows,
        final_weighted_C0=record(z),maximum_actual_C0=record(max_error),actual_gap_lower=record(min_gap),
        target_k_lower=record(min_k),final_actual_weighted_gradient=record(gradient),
        maximum_actual_first_angular_derivative=record(max_C1),
        integrated_actual_weighted_gradient_rate=record(integrated))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--native',type=Path,required=True)
    ap.add_argument('--initial',type=Path,default=Path('notes/2026-11-13-R131-C0-only-r005-native.json.gz'))
    ap.add_argument('--bits',type=int,default=256);ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();ctx.prec=a.bits
    if a.out.exists():raise FileExistsError('new true continuation report required')
    d=read_json(a.native);initial=read_json(a.initial)
    if (d.get('kind')!='actual_complete_Codazzi_positive_weight_cubic_scalar_comparison_coefficients'
        or not d.get('complete') or d.get('failure') is not None
        or d['covered_interval']!=d['exact_requested_interval'] or d['exact_requested_interval'][0]!='0'
        or not all(d.get(k) for k in ('whole_affine_parameter_interval','whole_real_angular_circle',
            'initial_weights_exactly_one','all_original_radial_weight_and_actual_germ_joins_retained',
            'full_mean_retained','exact_denominator_clearing','complete_actual_scalar_model_fees',
            'full_nonlinear_error_tube_terms_retained'))):
        raise ValueError('a complete true positive-weight comparison from the original waist is required')
    producer=Path(__file__).with_name('fourfold_codazzi_positive_weight_cubic_native.py')
    if sha(producer)!=d['source_sha256']:raise ValueError('native positive-weight producer changed')
    for p,h in d['inputs'].items():
        if sha(p)!=h:raise ValueError('native positive-weight input changed: '+p)
    for p,h in d['dependencies'].items():
        if sha(Path(__file__).with_name(p))!=h:raise ValueError('native positive-weight dependency changed: '+p)
    if (not initial.get('complete') or not initial.get('whole_affine_parameter_interval')
        or not initial.get('whole_real_angular_circle') or initial['object_sha256']!=d['object_sha256']
        or initial['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_linear_degeneracy.py'))
        or parameter(initial['exact_center_parameter'])!=parameter(d['exact_center_parameter'])
        or Fraction(initial['parameter_half_width'])!=Fraction(d['parameter_half_width'])):
        raise ValueError('independent actual waist identity mismatch')
    for p,h in initial['dependency_sha256'].items():
        if sha(Path(__file__).with_name(p))!=h:raise ValueError('actual initial derivative dependency changed: '+p)
    waist=initial['initial_actual_weighted_derivative']
    if not waist['whole_parameter_interval'] or not waist['whole_real_angular_circle']:
        raise ValueError('independent true initial weighted gradient is incomplete')
    initial_gradient=upper(waist['weighted_gradient_upper'])
    results={tube:propagate(d,initial_gradient,tube) for tube in d['tubes']}
    passed=[tube for tube,result in results.items() if result['passed']]
    best=min(passed,key=lambda tube:upper(results[tube]['maximum_actual_C0'])) if passed else None
    out=dict(kind='R131_true_C0_continuation_from_complete_cubic_scalar_positive_weights',
        complete=True,continuation_certified=bool(passed),closed_surface_complete=False,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (a.native,a.initial,producer)},
        object_sha256=d['object_sha256'],exact_center_parameter=d['exact_center_parameter'],
        parameter_half_width=d['parameter_half_width'],whole_affine_parameter_interval=True,
        whole_real_angular_circle=True,exact_requested_interval=d['exact_requested_interval'],
        full_BC_candidate_sha256=d['full_BC_candidate_sha256'],full_weight_candidate_sha256=d['full_weight_candidate_sha256'],
        initial_actual_weighted_derivative=waist,all_attempted_tubes_preserved=True,
        tube_results=results,passed_tubes=passed,best_certified_tube=best,
        final_bootstrap_is_unweighted=True,uses_candidate_C1_error_barrier=False,
        dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            'fourfold_codazzi_linear_degeneracy_v2.py','fourfold_codazzi_linear_degeneracy.py',
            'fourfold_phase_two_jet_newton_source.py','fourfold_phase_beta_bulk_interval.py')},
        scope='Same actual target and initial waist. A passed full positive-weight maximum comparison plus the true R131 weighted-gradient transport certifies only the stated Cauchy interval, not its geometric embedding, cap closure or a final common-metric closed family.')
    save(a.out,out)
    print(dict(continuation_certified=bool(passed),passed_tubes=passed,best=best,
        maximum_actual_C0=results[best]['maximum_actual_C0'] if best is not None else None,
        failures={t:r.get('failed_row') for t,r in results.items() if not r['passed']}),flush=True)


if __name__=='__main__':main()
