#!/usr/bin/env python3
"""True continuation from a complete union of saved closed-row certificates.

An interrupted original report remains incomplete. Explicitly bound process
evidence permits only its already saved complete rows, whose exact indices
are reconstructed from the full original residual and full weight partition.
The complete union transports one unreset error and true gradient.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
from flint import ctx
from fourfold_codazzi_positive_weight_cubic_C0 import propagate, parameter
from fourfold_codazzi_linear_degeneracy_v2 import read_json, upper, lower
from fourfold_phase_two_jet_newton_source import save, sha


NATIVE_SOURCES={
    'actual_complete_Codazzi_positive_weight_cubic_scalar_comparison_coefficients':
        'fourfold_codazzi_positive_weight_cubic_native.py',
    'actual_complete_Codazzi_positive_weight_cubic_small_batch_comparison_coefficients':
        'fourfold_codazzi_positive_weight_batched_native.py',
}
FLAGS=('whole_affine_parameter_interval','whole_real_angular_circle',
       'initial_weights_exactly_one',
       'all_original_radial_weight_and_actual_germ_joins_retained',
       'full_mean_retained','exact_denominator_clearing',
       'complete_actual_scalar_model_fees',
       'full_nonlinear_error_tube_terms_retained')
IDENTITY=('object_sha256','exact_center_parameter','parameter_half_width',
          'full_BC_candidate_sha256','full_weight_candidate_sha256',
          'actual_initial_error','original_full_native_interval','tubes')


def original_partition(d):
    """Reconstruct every exact original row, including rows never computed."""
    originals=[];weights=[]
    for name in d['inputs']:
        if not (name.endswith('.json') or name.endswith('.json.gz')):continue
        value=read_json(name)
        if value.get('kind')=='actual_complete_Codazzi_cubic_target_cleared_polynomial_residual':
            originals.append((name,value))
        if value.get('kind')=='exact_full_finite_positive_comparison_weight_byte_shards':
            weights.append((name,value))
    if len(originals)!=1 or len(weights)!=1:
        raise ValueError('the unique complete actual residual and full weights are required')
    native_path,native=originals[0];weight_path,weight=weights[0]
    if (not native['complete'] or native['failure'] is not None
        or native['covered_interval']!=native['exact_requested_interval']
        or not native['whole_affine_parameter_interval'] or not native['whole_real_angular_circle']
        or native['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_cubic_cleared_residual.py'))
        or native['object_sha256']!=d['object_sha256']
        or native['exact_center_parameter']!=d['exact_center_parameter']
        or native['parameter_half_width']!=d['parameter_half_width']
        or native['candidate_sha256']!=d['full_BC_candidate_sha256']
        or native['actual_initial_error']!=d['actual_initial_error']
        or native['covered_interval']!=d['original_full_native_interval']):
        raise ValueError('the complete actual residual identity differs')
    meta=weight['original_metadata']
    if (not weight['complete'] or weight['original_sha256']!=d['full_weight_candidate_sha256']
        or weight['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_positive_weight_candidate.py'))
        or meta['object_sha256']!=d['object_sha256']
        or meta['exact_center_parameter']!=d['exact_center_parameter']
        or meta['candidate_original_sha256']!=d['full_BC_candidate_sha256']
        or meta['candidate_manifest_sha256']!=native['candidate_manifest_sha256']
        or not meta['initial_weights_exactly_one'] or not meta['shared_endpoint_continuity_exact']):
        raise ValueError('the full original continuous weights differ')
    for piece in weight['shards']:
        p=str(Path(weight_path).parent/piece['file'])
        if d['inputs'].get(p)!=piece['compressed_sha256']:
            raise ValueError('a complete original weight shard is not bound')
    times=list(map(Fraction,meta['time_nodes_exact_fractions']))
    if times[0]!=0 or any(a>=b for a,b in zip(times,times[1:])):
        raise ValueError('the complete exact weight-node array is invalid')
    subdivide=d['subdivide']
    if not isinstance(subdivide,int) or subdivide<1:
        raise ValueError('the exact radial subdivision is invalid')
    full=[];cursor=Fraction(0)
    for index,item in enumerate(native['rows']):
        lo,hi=map(Fraction,item['interval']);gl,gr=map(Fraction,item['actual_scalar_germ'])
        if lo!=cursor or not gl<=lo<hi<=gr or hi>times[-1]:
            raise ValueError('the complete original residual/germ cover differs')
        cuts=[lo]+[t for t in times if lo<t<hi]+[hi]
        for a,b in zip(cuts,cuts[1:]):
            wpiece=min(len(times)-2,bisect_right(times,a)-1)
            for sub in range(subdivide):
                left=a+(b-a)*sub/subdivide;right=a+(b-a)*(sub+1)/subdivide
                full.append((index,wpiece,left,right,item))
        cursor=hi
    if [str(0),str(cursor)]!=d['original_full_native_interval']:
        raise ValueError('the full original cover endpoint is missing')
    return full,native_path,weight_path


def checked_parts(paths,right,interrupted_audits=()):
    audits={}
    for p in interrupted_audits:
        a=read_json(p);key=str(Path(a['original_report_path']))
        if (a.get('kind')!='observed_external_termination_after_saved_complete_weight_rows'
            or a.get('exit_code')!=137 or a.get('report_original_complete') is not False
            or a.get('report_original_failure') is not None
            or a.get('half_finished_row_consumed') is not False
            or sha(key)!=a['original_report_sha256']
            or sha(a['saved_log_path'])!=a['saved_log_sha256'] or key in audits):
            raise ValueError('an exact unchanged external-termination record is required')
        audits[key]=(str(p),a)
    used_audits=set();producer_hashes={};rows=[];summaries=[]
    reference=None;cursor=Fraction(0);partition=0
    checked_inputs={};checked_dependencies={}
    for path in paths:
        d=read_json(path);producer_name=NATIVE_SOURCES.get(d.get('kind'))
        if producer_name is None:raise ValueError('unrecognized original cubic-weight producer')
        producer_hash=sha(Path(__file__).with_name(producer_name));producer_hashes[producer_name]=producer_hash
        if 'small_batch' in d['kind'] and (d.get('maximum_polynomials_per_angular_batch')!=8
                or not d.get('all_original_columnwise_operations_retained')):
            raise ValueError('the original small-batch contract is missing')
        if (d.get('failure') is not None or d.get('source_sha256')!=producer_hash
            or not all(d.get(key) for key in FLAGS)):
            raise ValueError('the original complete-row producer contract is missing: '+str(path))
        interrupted=not d.get('complete');audit_path=None
        if interrupted:
            if str(path) not in audits:raise ValueError('an interrupted report requires explicit original process evidence')
            audit_path,audit=audits[str(path)];used_audits.add(str(path))
            if (audit['saved_complete_rows']!=len(d['rows'])
                or audit['planned_rows']!=d['planned_boxes']
                or audit['original_partition_first']!=d['original_partition_first']
                or audit['saved_covered_interval']!=d['covered_interval']
                or audit['original_requested_interval']!=d['exact_requested_interval']
                or not 0<len(d['rows'])<d['planned_boxes']):
                raise ValueError('the preserved completed prefix differs from the process record')
        elif str(path) in audits or len(d['rows'])!=d['planned_boxes'] or d['covered_interval']!=d['exact_requested_interval']:
            raise ValueError('a complete original report has an inconsistent full cover')
        if reference is None:reference=d
        elif any(d.get(key)!=reference.get(key) for key in IDENTITY):
            raise ValueError('the true target, full weights or initial conditions differ')
        for name,h in d['inputs'].items():
            if sha(name)!=h:raise ValueError('native input changed: '+name)
            if name in checked_inputs and checked_inputs[name]!=h:raise ValueError('inconsistent input identity')
            checked_inputs[name]=h
        for name,h in d['dependencies'].items():
            if sha(Path(__file__).with_name(name))!=h:raise ValueError('native dependency changed: '+name)
            if name in checked_dependencies and checked_dependencies[name]!=h:raise ValueError('inconsistent dependency identity')
            checked_dependencies[name]=h
        full,native_path,weight_path=original_partition(d)
        first=d['original_partition_first'];planned=d['planned_boxes']
        if not isinstance(first,int) or not isinstance(planned,int) or planned<1 or not 0<=first<first+planned<=len(full):
            raise ValueError('the full planned slice is not the original partition')
        if d['exact_requested_interval']!=list(map(str,(full[first][2],full[first+planned-1][3]))):
            raise ValueError('the original requested interval is not its exact planned slice')
        start,end=map(Fraction,d['covered_interval'])
        if start!=cursor or not start<end<=right or first!=partition or not d['rows']:
            raise ValueError('missing, repeated or noncontiguous original saved rows')
        for item in d['rows']:
            expected=full[partition];native_index,wpiece,lo,hi,original=expected
            if (lo!=cursor or item['partition_row']!=partition
                or item['native_row']!=native_index or item['weight_piece']!=wpiece
                or item['interval']!=list(map(str,(lo,hi)))
                or item['actual_scalar_germ']!=original['actual_scalar_germ']
                or set(item['rates'])!=set(d['tubes'])
                or item['exact_model_degrees']!=dict(k=3,gamma=3,beta=3,kappa=2)
                or not lower(item['weight_lower'])>0
                or not upper(item['weight_upper'])>=lower(item['weight_lower'])):
                raise ValueError('a saved row differs from the full exact partition and closed-box contract')
            for key in ('rho0','Mhat','candidate_gap','k_lower','beta','kappa'):
                if item['original_'+key]!=original['bounds'][key]:
                    raise ValueError('the original full scalar coefficient bound changed: '+key)
            for key in ('k','gamma','beta','kappa'):
                if (key not in item['exact_dyadic_scalar_models']
                    or not upper(item['full_scalar_model_errors'][key])>=0):
                    raise ValueError('the complete exact scalar model or its error is absent')
            if any(not upper(v)>=0 for v in item['rates'].values()):
                raise ValueError('an original tube row is invalid')
            rows.append(item);cursor=hi;partition+=1
        if cursor!=end:raise ValueError('the saved prefix endpoint differs from its last complete row')
        summaries.append(dict(path=str(path),sha256=sha(path),original_kind=d['kind'],
            original_producer=producer_name,original_source_sha256=producer_hash,
            original_complete=d['complete'],original_partition_first=first,planned_boxes=planned,
            consumed_complete_rows=len(d['rows']),exact_requested_interval=d['exact_requested_interval'],
            consumed_covered_interval=d['covered_interval'],full_partition_rows=len(full),
            reconstructed_original_native=native_path,reconstructed_full_weights=weight_path,
            interruption_audit=audit_path,interruption_audit_sha256=sha(audit_path) if audit_path else None,
            bits=d['bits'],angular_grid=d['angular_grid'],product_grid=d['product_grid']))
    if used_audits!=set(audits):raise ValueError('unused or repeated interrupted report evidence')
    if reference is None or cursor!=right:raise ValueError('the exact requested final endpoint is missing')
    original_left,original_right=map(Fraction,reference['original_full_native_interval'])
    if original_left!=0 or not 0<right<=original_right:raise ValueError('the same original actual prefix is required')
    data={key:reference[key] for key in IDENTITY}
    data.update(kind='checked_complete_union_of_original_saved_weight_rows',rows=rows,
        exact_requested_interval=['0',str(right)])
    return data,summaries,checked_inputs,checked_dependencies,producer_hashes


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
    ap.add_argument('--interrupted-audits',type=Path,nargs='*',default=[])
    ap.add_argument('--initial',type=Path,
        default=Path('notes/2026-11-13-R131-C0-only-r005-native.json.gz'))
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits
    if args.out.exists():raise FileExistsError('a fresh complete piece consumer report is required')
    if args.right<=0 or len(set(args.native_parts))!=len(args.native_parts):
        raise ValueError('positive interval and distinct complete native files required')
    data,parts,verified_inputs,verified_deps,producer_hashes=checked_parts(args.native_parts,args.right,args.interrupted_audits)
    waist=actual_initial(args.initial,data)
    initial_gradient=upper(waist['weighted_gradient_upper'])
    results={tube:propagate(data,initial_gradient,tube) for tube in data['tubes']}
    passed=[tube for tube,result in results.items() if result['passed']]
    best=min(passed,key=lambda tube:upper(results[tube]['maximum_actual_C0'])) if passed else None
    dependencies=('fourfold_codazzi_positive_weight_batched_piece_C0.py',
        'fourfold_codazzi_positive_weight_cubic_C0.py',
        'fourfold_codazzi_positive_weight_piece_C0.py','fourfold_codazzi_positive_weight_batched_native.py',
        'fourfold_codazzi_positive_weight_cubic_native.py',
        'fourfold_codazzi_linear_degeneracy_v2.py','fourfold_codazzi_linear_degeneracy.py',
        'fourfold_phase_two_jet_newton_source.py','fourfold_phase_beta_bulk_interval.py')
    out=dict(kind='R131_true_C0_continuation_from_complete_union_of_saved_weight_rows_v4',
        complete=True,continuation_certified=bool(passed),closed_surface_complete=False,
        source_sha256=sha(__file__),bits=args.bits,
        inputs={str(path):sha(path) for path in args.native_parts+[args.initial]+args.interrupted_audits},
        checked_original_piece_producers=producer_hashes,
        original_native_reports_unchanged=True,complete_parts=parts,
        interruption_audits=list(map(str,args.interrupted_audits)),
        interrupted_reports_remain_incomplete=True,
        all_saved_rows_reconstructed_against_full_exact_original_partition=True,
        mixed_original_and_small_batch_saved_closed_rows_explicitly_checked=True,
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
        scope='A complete union of original saved closed-row certificates is checked against the full original exact partition. Explicitly audited interrupted reports remain unchanged and incomplete; no unsaved or half-finished row is used. The same continuous finite weight transports one actual error and the independent true R131 gradient without resets. Passing gives only same-waist Cauchy continuation, not embedding or a closed surface.')
    save(args.out,out)
    print(dict(continuation_certified=bool(passed),parts=len(parts),rows=len(data['rows']),
        passed_tubes=passed,best=best,
        maximum_actual_C0=results[best]['maximum_actual_C0'] if best else None,
        failures={t:r.get('failed_row') for t,r in results.items() if not r['passed']}),flush=True)


if __name__=='__main__':main()
