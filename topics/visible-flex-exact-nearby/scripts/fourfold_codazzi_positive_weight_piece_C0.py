#!/usr/bin/env python3
"""True C0 continuation from separately completed positive-weight pieces.

Every piece remains an original immutable native report.  This consumer
checks identities and the exact contiguous partition, then carries the
same weighted error across the common weight function.  It never rewrites
an incomplete report as a completed report or impersonates its producer.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
from flint import ctx
from fourfold_codazzi_positive_weight_cubic_C0 import propagate, parameter
from fourfold_codazzi_linear_degeneracy_v2 import read_json, upper
from fourfold_phase_two_jet_newton_source import save, sha


NATIVE_KIND='actual_complete_Codazzi_positive_weight_cubic_scalar_comparison_coefficients'
FLAGS=('whole_affine_parameter_interval','whole_real_angular_circle',
       'initial_weights_exactly_one',
       'all_original_radial_weight_and_actual_germ_joins_retained',
       'full_mean_retained','exact_denominator_clearing',
       'complete_actual_scalar_model_fees',
       'full_nonlinear_error_tube_terms_retained')
IDENTITY=('object_sha256','exact_center_parameter','parameter_half_width',
          'full_BC_candidate_sha256','full_weight_candidate_sha256',
          'actual_initial_error','original_full_native_interval','tubes')


def checked_parts(paths,right):
    producer=Path(__file__).with_name('fourfold_codazzi_positive_weight_cubic_native.py')
    producer_hash=sha(producer)
    rows=[];summaries=[];reference=None;cursor=Fraction(0);partition=0
    checked_inputs={};checked_dependencies={}
    for path in paths:
        d=read_json(path)
        if (d.get('kind')!=NATIVE_KIND or not d.get('complete')
            or d.get('failure') is not None
            or d.get('source_sha256')!=producer_hash
            or d.get('covered_interval')!=d.get('exact_requested_interval')
            or not all(d.get(key) for key in FLAGS)):
            raise ValueError('a complete original cubic-weight piece is required: '+str(path))
        if reference is None:
            reference=d
        elif any(d.get(key)!=reference.get(key) for key in IDENTITY):
            raise ValueError('the true target, full weights or initial conditions differ between pieces')
        for name,h in d['inputs'].items():
            if sha(name)!=h:raise ValueError('native input changed: '+name)
            if name in checked_inputs and checked_inputs[name]!=h:
                raise ValueError('inconsistent input byte identities')
            checked_inputs[name]=h
        for name,h in d['dependencies'].items():
            if sha(Path(__file__).with_name(name))!=h:
                raise ValueError('native dependency changed: '+name)
            if name in checked_dependencies and checked_dependencies[name]!=h:
                raise ValueError('inconsistent dependency byte identities')
            checked_dependencies[name]=h
        start,end=map(Fraction,d['exact_requested_interval'])
        if (start!=cursor or not start<end<=right
            or d['original_partition_first']!=partition
            or len(d['rows'])!=d['planned_boxes'] or not d['rows']):
            raise ValueError('missing, repeated or noncontiguous complete native piece')
        for item in d['rows']:
            lo,hi=map(Fraction,item['interval'])
            gl,gr=map(Fraction,item['actual_scalar_germ'])
            if (lo!=cursor or not gl<=lo<hi<=gr
                or item['partition_row']!=partition
                or set(item['rates'])!=set(d['tubes'])):
                raise ValueError('actual row/germ/tube partition is incomplete')
            rows.append(item);cursor=hi;partition+=1
        if cursor!=end:raise ValueError('piece endpoint is not its actual completed endpoint')
        summaries.append(dict(path=str(path),sha256=sha(path),
            original_partition_first=d['original_partition_first'],
            planned_boxes=d['planned_boxes'],exact_requested_interval=d['exact_requested_interval'],
            bits=d['bits'],angular_grid=d['angular_grid'],product_grid=d['product_grid']))
    if reference is None or cursor!=right:
        raise ValueError('the exact requested final endpoint is missing')
    original_left,original_right=map(Fraction,reference['original_full_native_interval'])
    if original_left!=0 or not 0<right<=original_right:
        raise ValueError('requested interval is not a prefix of the same original complete residual')
    # Only an internal row view is assembled.  Its source is this checker;
    # the original producer identity is retained separately in the output.
    data={key:reference[key] for key in IDENTITY}
    data.update(kind='checked_contiguous_original_weight_rows',rows=rows,
        exact_requested_interval=['0',str(right)])
    return data,summaries,checked_inputs,checked_dependencies,producer_hash


def actual_initial(path,data):
    initial=read_json(path)
    if (not initial.get('complete')
        or not initial.get('whole_affine_parameter_interval')
        or not initial.get('whole_real_angular_circle')
        or initial['object_sha256']!=data['object_sha256']
        or initial['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_linear_degeneracy.py'))
        or parameter(initial['exact_center_parameter'])!=parameter(data['exact_center_parameter'])
        or Fraction(initial['parameter_half_width'])!=Fraction(data['parameter_half_width'])):
        raise ValueError('independent actual initial waist identity mismatch')
    for name,h in initial['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=h:
            raise ValueError('actual initial derivative dependency changed: '+name)
    waist=initial['initial_actual_weighted_derivative']
    if not waist['whole_parameter_interval'] or not waist['whole_real_angular_circle']:
        raise ValueError('incomplete actual initial weighted gradient')
    return waist


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--native-parts',type=Path,nargs='+',required=True)
    ap.add_argument('--right',type=Fraction,default=Fraction(1,5))
    ap.add_argument('--initial',type=Path,
        default=Path('notes/2026-11-13-R131-C0-only-r005-native.json.gz'))
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits
    if args.out.exists():raise FileExistsError('a fresh complete piece consumer report is required')
    if args.right<=0 or len(set(args.native_parts))!=len(args.native_parts):
        raise ValueError('positive interval and distinct complete native files required')
    data,parts,verified_inputs,verified_deps,producer_hash=checked_parts(args.native_parts,args.right)
    waist=actual_initial(args.initial,data)
    initial_gradient=upper(waist['weighted_gradient_upper'])
    results={tube:propagate(data,initial_gradient,tube) for tube in data['tubes']}
    passed=[tube for tube,result in results.items() if result['passed']]
    best=min(passed,key=lambda tube:upper(results[tube]['maximum_actual_C0'])) if passed else None
    dependencies=('fourfold_codazzi_positive_weight_cubic_C0.py',
        'fourfold_codazzi_positive_weight_cubic_native.py',
        'fourfold_codazzi_linear_degeneracy_v2.py','fourfold_codazzi_linear_degeneracy.py',
        'fourfold_phase_two_jet_newton_source.py','fourfold_phase_beta_bulk_interval.py')
    out=dict(kind='R131_true_C0_continuation_from_checked_complete_positive_weight_pieces',
        complete=True,continuation_certified=bool(passed),closed_surface_complete=False,
        source_sha256=sha(__file__),bits=args.bits,
        inputs={str(path):sha(path) for path in args.native_parts+[args.initial]},
        checked_original_piece_producer_sha256=producer_hash,
        original_native_reports_unchanged=True,complete_parts=parts,
        verified_native_inputs=verified_inputs,verified_native_dependencies=verified_deps,
        exact_requested_interval=['0',str(args.right)],
        complete_rows=len(data['rows']),exact_contiguous_row_and_scalar_germ_cover=True,
        same_complete_weight_candidate_at_all_joins=True,
        object_sha256=data['object_sha256'],exact_center_parameter=data['exact_center_parameter'],
        parameter_half_width=data['parameter_half_width'],
        full_BC_candidate_sha256=data['full_BC_candidate_sha256'],
        full_weight_candidate_sha256=data['full_weight_candidate_sha256'],
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,
        initial_actual_weighted_derivative=waist,all_attempted_tubes_preserved=True,
        tube_results=results,passed_tubes=passed,best_certified_tube=best,
        final_bootstrap_is_unweighted=True,uses_candidate_C1_error_barrier=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in dependencies},
        scope='The original complete native pieces are checked separately and concatenate exactly. The same continuous finite weight transports one actual error and the independent true R131 gradient. A passed requested interval is a same-waist Cauchy continuation only; no geometric embedding or closed-surface conclusion is implied.')
    save(args.out,out)
    print(dict(continuation_certified=bool(passed),parts=len(parts),rows=len(data['rows']),
        passed_tubes=passed,best=best,
        maximum_actual_C0=results[best]['maximum_actual_C0'] if best else None,
        failures={t:r.get('failed_row') for t,r in results.items() if not r['passed']}),flush=True)


if __name__=='__main__':main()
