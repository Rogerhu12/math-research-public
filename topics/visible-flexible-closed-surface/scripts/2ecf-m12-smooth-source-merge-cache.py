#!/usr/bin/env python3
"""Create a separately identified X+C+Q source cache, paying addition error.

Inputs and endpoint traces remain frozen. The output has a NEW schema and
explicit source identity; it is never represented as the original source.
It can be consumed by the existing TailQueries/CommonCutSource readers,
but downstream results must retain its R250 source_regularization field.
Global geometry must include Q's six jets in addition to the new W budget.
"""
from __future__ import annotations
import argparse,hashlib,json,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

QUERY_PRODUCER_SHA='c05000bd75fa1fdb98498162a289a7df52844e16ae04e1179006147bacfca191'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def packet(q):return {'exact':str(q),'display':float(q)}
def aq(x):return Q(*x.as_integer_ratio())

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ('source-report','source-cache','Q-report','Q-cache','smoothing-report','out'):
        ap.add_argument('--'+k,type=Path,required=True)
    args=ap.parse_args();cache=Path(str(args.out)+'.npz');began=time.monotonic()
    if args.out.exists() or cache.exists():raise FileExistsError('A separately identified source is required')
    old=json.loads(args.source_report.read_text());qr=json.loads(args.Q_report.read_text());sm=json.loads(args.smoothing_report.read_text())
    if qr['script_sha256']!=QUERY_PRODUCER_SHA:raise ValueError('Q point-interval producer changed')
    for key,path in [('original_source_report_sha256',args.source_report),('original_source_cache_sha256',args.source_cache),
                     ('cache_sha256',args.Q_cache),('smoothing_report_sha256',args.smoothing_report)]:
        if qr[key]!=sha(path):raise ValueError('Q actual input mismatch '+key)
    if old['endpoint_cache_sha256']!=sha(args.source_cache):raise ValueError('Original source cache changed')
    if old['manifest_sha256']!=qr['manifest_sha256'] or qr['manifest_sha256']!=sm['manifest_sha256']:
        raise ValueError('Original target source manifest differs')
    with np.load(args.source_cache,allow_pickle=False) as z:original={k:z[k].copy() for k in z.files}
    with np.load(args.Q_cache,allow_pickle=False) as z:
        qfraction=z['query_fraction'].copy();qc=z['coefficients'].copy()
        ids=z['original_query_indices'].copy();dids=z['diagnostic_query_indices'].copy()
        if not np.array_equal(z['planar_modes'],original['planar_modes']) or not np.array_equal(z['height_modes'],original['height_modes']):
            raise ValueError('Incomplete original angular channels')
    modes=list(map(int,np.r_[original['planar_modes'],original['height_modes']]))
    addition={(d,j):Q(0) for d in range(3) for j in range(3-d)}
    counts={};unchanged={};merged={k:v.copy() for k,v in original.items()}
    for fraction_key,coefficient_key,mapping in [('query_fraction','coefficients',ids),('diagnostic_fraction','diagnostic_coefficients',dids)]:
        if fraction_key not in original:
            if len(mapping):raise ValueError('Unexpected diagnostic values')
            continue
        if len(mapping)!=len(original[fraction_key]) or any(Q(str(qfraction[k]))!=Q(str(r)) for k,r in zip(mapping,original[fraction_key])):
            raise ValueError('Query mapping differs from the actual original')
        extra=qc[mapping];prior=original[coefficient_key]
        if extra.shape!=prior.shape:raise ValueError('Q coefficient shape mismatch')
        nonzero=extra!=0
        # Preserve every byte of an unchanged coefficient, including signed zero.
        merged[coefficient_key][nonzero]=prior[nonzero]+extra[nonzero]
        row_ids=np.flatnonzero(np.any(nonzero,axis=(1,2)))
        for row in row_ids:
            for d in range(3):
                er=[abs(aq(merged[coefficient_key][row,d,k])-aq(prior[row,d,k])-aq(extra[row,d,k])) if nonzero[row,d,k] else Q(0) for k in range(len(modes))]
                for j in range(3-d):addition[d,j]=max(addition[d,j],sum((e*abs(m)**j for e,m in zip(er,modes)),Q(0)))
        counts[coefficient_key]={'changed_rows':len(row_ids),'changed_nonzero_Q_coefficients':int(np.count_nonzero(nonzero)),
                                 'total_rows':len(prior),'unchanged_coefficients_byte_preserved':True}
    for k,v in original.items():
        if k not in ('coefficients','diagnostic_coefficients'):
            if v.dtype!=merged[k].dtype or v.shape!=merged[k].shape or v.tobytes()!=merged[k].tobytes():
                raise ArithmeticError('Endpoint or query metadata changed: '+k)
            unchanged[k]={'dtype':str(v.dtype),'shape':list(v.shape),'array_bytes_sha256':hashlib.sha256(v.tobytes()).hexdigest()}
    if not counts:raise ValueError('No source coefficient arrays consumed')
    native={k:addition[k]+Q(qr['cache_error_native_r_u_six_jet_upper'][str(k)]['exact']) for k in addition}
    physical={'Q':native[0,0],'Qs':native[1,0],'Qu':native[0,1],
      'Qss':native[2,0]+6*native[1,0],'Qsu':native[1,1],'Quu':native[0,2]}
    np.savez_compressed(cache,**merged)
    identity={'mathematical_source':'Original X plus deterministic central C plus exact R250 Q; a separate source epoch.',
      'original_source_report_sha256':sha(args.source_report),'original_source_cache_sha256':sha(args.source_cache),
      'Q_point_report_sha256':sha(args.Q_report),'Q_point_cache_sha256':sha(args.Q_cache),
      'Q_continuous_report_sha256':sha(args.smoothing_report),'Q_source_sha256':sm['script_sha256'],
      'Q_divisor':sm['divisor'],'Q_exact_jump_stream_sha256':sm['exact_jump_and_window_stream_sha256'],
      'Q_continuous_physical_s_u_six_jet_upper':sm['physical_s_u_six_jet_upper'],
      'same_original_target_metric':True,'same_central_common_cut_and_true_cuff_two_jets':True,
      'not_the_original_unregularized_source':True,
      'required_global_geometry_change':'Keep original X C_X as baseline; add Q eta/p/cw to complete C+W budget before the same R10/R16 transfer.',
      'original_source_evaluator_roundoff_not_recertified':True}
    report={'schema':'m12-R250-regularized-tail-query-source-v1','script_sha256':sha(__file__),
      'source_regularization':identity,'manifest_sha256':old['manifest_sha256'],
      'endpoint_cache_sha256':sha(cache),'query_file_sha256':old['query_file_sha256'],
      'coefficient_arithmetic':'Actual stored original longdouble source plus interval-certified exact Q, with the actual longdouble addition error separately bounded.',
      'source_addition_only_counts':counts,'unchanged_original_arrays':unchanged,
      'additional_error_native_r_u_six_jet_upper':{str(k):packet(v) for k,v in native.items()},
      'additional_error_physical_s_u_six_jet_upper':{k:packet(v) for k,v in physical.items()},
      'actual_addition_only_native_r_u_six_jet_upper':{str(k):packet(v) for k,v in addition.items()},
      'same_query_radii_and_diagnostics':True,'all_global_finite_source_nodes_regularized_by_exact_definition':True,
      'same_original_tail_source':False,'base_original_source_retained_as_lower_layer':True,
      'new_nonlinear_solve_executed':False,'seconds':time.monotonic()-began}
    # Point-selection metadata is unchanged; old source-only bounds are deliberately not copied.
    for key in ('diagnostic_window_exact','diagnostic_windows_exact','disjoint_window_gap_not_claimed_observed',
                'diagnostic_groups','diagnostic_subdivisions','diagnostic_query_count','diagnostic_source_spans',
                'queries','integrated_spans','true_cuff_exact','finite_inner_exact','outer_cut_exact'):
        if key in old:report[key]=old[key]
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'report':str(args.out),'source_regularization_epoch':True,'counts':counts,
      'additional_error_physical_display':{k:float(v) for k,v in physical.items()},'seconds':report['seconds']},indent=2))

if __name__=='__main__':main()
