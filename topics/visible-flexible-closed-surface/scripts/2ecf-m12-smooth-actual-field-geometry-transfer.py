#!/usr/bin/env python3
"""Certify the separately identified exact field X+C+Q+W from actual receipts.

The saved W and its original solver receipt remain untouched.  The new map
uses exact R250 Q on the complete finite tail, keeps the original g, and is
not a new Newton acceptance.  The R249/R253/R252 receipts must all belong to
the same actual Q-free field.  A separately identified accurate Q query
source is bound as a runtime interface, not used in place of the global Q
theorem and not promoted to a new solver result.
"""
from __future__ import annotations
import argparse, hashlib, json, time
from fractions import Fraction as F
from pathlib import Path
import numpy as np

PINNED = {
    '2ecf-m12-smooth-source-seams.py': '30b1384fed8e7a6018c99ba688b091bb42dfb2451e2df39531c9df0d88aa34b7',
    '2ecf-m12-smooth-source-query-cache.py': 'c05000bd75fa1fdb98498162a289a7df52844e16ae04e1179006147bacfca191',
    '2ecf-m12-smooth-source-merge-cache.py': '1aee1e34c37c150d0155d07aa268783cc74cf949ccf3558301366bd1ec7bf199',
    '2ecf-m12-local-material-two-jet-budget.py': 'c7e5f4c82616ed43103e234ca774a6e5e95cb46e93dc18c6b2463654911fb632',
    '2ecf-m12-regional-source-normal-geometry.py': '0b62fcd84c7e19155197d6a2719ecd7484ecf515ca5f469fe4d56e52ea921296',
    '2ecf-m12-tail-cross-gram-budget.py': '197a6696eae4f14723ef92a09c9543f102c789fef95d02fe1a751075e9d8e28d',
    '2ecf-m12-tail-cross-gram-local-certificate.py': '138062ba3e48e7aecafdc3e38283c0833a0ffdf9e088832901930de49b393942',
}
DATA_SHA='359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0'
META_SHA='253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2'
BRIDGE_SHA='1389cf1a339b0a0d749beb666b6def24a31e766eff0abf63289217728ceacdaa'
MANIFEST_SHA='cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104'
R226_SHA='81003432a6823b3c86859be226c9a099012ed7fa21e46165ac12091d86727e80'
R230_SHA='b71e1b7bd0c02a19d047793574afcf49e41a2378435f73e7cf56efef65f8a9d3'

def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1<<20),b''):h.update(block)
    return h.hexdigest()
def read(path):return json.loads(Path(path).read_text())
def packet(value,side='upper'):return {side+'_exact':str(value),'display':float(value)}
def require(ok,message):
    if not ok:raise ValueError(message)
def true_fields(record,names):
    for name in names:require(record.get(name) is True,'Missing complete premise: '+name)
def exact(record,key):
    value=F(record[key]['upper_exact']);require(value>=0,'Negative bound: '+key);return value

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    names=('scripts','data','field','grid','result','query-report','query-cache',
           'source-bounds','correction-bounds','two-jet-report','regional-report',
           'continuous-metric','smoothing-report','regularized-base-report',
           'regularized-base-cache','Q-query-report','Q-query-cache',
           'regularized-report','regularized-cache','out')
    for name in names:ap.add_argument('--'+name,type=Path,required=True)
    args=ap.parse_args();began=time.monotonic()
    require(not args.out.exists(),'Fresh regularized field output required')
    inputs={name.replace('-','_'):getattr(args,name.replace('-','_')) for name in names if name not in ('scripts','out')}
    hashes={k:sha(p) for k,p in inputs.items()}
    for name,wanted in PINNED.items():require(sha(args.scripts/name)==wanted,'Published producer changed: '+name)
    notes=args.scripts.parent/'notes'
    for name,wanted in (
        ('2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json',META_SHA),
        ('2026-11-09-db6f-root-exact-bridge-m12.json',BRIDGE_SHA),
        ('2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json',MANIFEST_SHA)):
        require(sha(notes/name)==wanted,'Original source definition changed: '+name)
    require(hashes['data']==DATA_SHA,'Original exact prefix data changed')
    result=read(args.result);grid=read(args.grid);original=read(args.query_report)
    source=read(args.source_bounds);change=read(args.correction_bounds)
    two=read(args.two_jet_report);regional=read(args.regional_report);metric=read(args.continuous_metric)
    smooth=read(args.smoothing_report);base=read(args.regularized_base_report)
    qr=read(args.Q_query_report);regular=read(args.regularized_report)
    require(result['field_sha256']==hashes['field'] and result['grid_sha256']==hashes['grid'],'Actual solver field/grid mismatch')
    require(result['query_report_sha256']==hashes['query_report'] and result['query_cache_sha256']==hashes['query_cache'],'Original solver query identity differs')
    require(not result.get('source_regularization') and not result['source'].get('source_regularization'),'Input solver must retain its original Q-free identity')
    require(result['source']['data_sha256']==DATA_SHA and result['source']['common_meta_sha256']==META_SHA and result['source']['bridge_sha256']==BRIDGE_SHA,'Original common-cut source differs')
    require(result['original_exact_metric_unchanged'] is True,'Original fixed target required')
    for record,producer in ((two,'2ecf-m12-local-material-two-jet-budget.py'),(regional,'2ecf-m12-regional-source-normal-geometry.py')):
        require(record['script_sha256']==PINNED[producer],'Continuous geometry producer mismatch')
        for key,argument in (('field_sha256','field'),('grid_sha256','grid'),('solver_result_sha256','result'),
                             ('correction_receipt_sha256','correction_bounds'),('source_receipt_sha256','source_bounds')):
            require(record[key]==hashes[argument],'Geometry actual input differs: '+key)
    require(regional['actual_two_jet_report_sha256']==hashes['two_jet_report'],'Regional receipt used another full two-jet bound')
    true_fields(two,('same_original_metric','same_actual_field','all_original_spans_and_all_angles','central_correction_included'))
    true_fields(regional,('same_original_Q_free_source_and_g','same_actual_saved_field_no_refit',
        'all_prefix_spans_and_all_angles_continuously_covered','prefix_boundary_uncertainty_included_by_superset',
        'tail_uses_complete_inherited_global_p','entire_phase_interval_by_original_orbit_structure'))
    require(metric['script_sha256'] in (PINNED['2ecf-m12-tail-cross-gram-budget.py'],PINNED['2ecf-m12-tail-cross-gram-local-certificate.py']),'Unknown continuous cross-Gram producer')
    for key,argument in (('field_sha256','field'),('grid_sha256','grid'),('solver_result_sha256','result'),
                         ('correction_bounds_sha256','correction_bounds'),('query_report_sha256','query_report')):
        require(metric[key]==hashes[argument],'Continuous metric actual input differs: '+key)
    true_fields(metric,('original_target_metric_retained','original_source_X_plus_C_retained',
        'all_angles_and_all_points_in_listed_intervals','full_surface_certificate',
        'covers_complete_moving_half_and_fixed_cuffs_caps_by_original_identity'))
    require(metric['Q_source_regularization_included'] is False,'The input metric already includes Q')
    require(change['script_sha256']==R226_SHA and source['script_sha256']==R230_SHA,'Original continuous source/change producer changed')
    require(change['field_sha256']==hashes['field'] and change['grid_sha256']==hashes['grid'],'Continuous correction belongs to another field')
    require(change['exact_zero_endpoint_jets']==[True,True,True],'Complete zero endpoint two jets required')
    true_fields(change,('continuous_all_knots_and_all_angles','central_reference_change_included'))
    true_fields(source,('continuous_all_spans_and_all_angles','exact_common_cut_change_included'))
    require(source['tail_report_sha256']==hashes['query_report'] and source['tail_cache_sha256']==hashes['query_cache'],'Complete source bound used another original query identity')
    for record in (source,change):
        require(record['data_sha256']==DATA_SHA and record['common_meta_sha256']==META_SHA and record['bridge_sha256']==BRIDGE_SHA and record['tail_manifest_sha256']==MANIFEST_SHA,'Original complete source definition differs')
    with np.load(args.field,allow_pickle=False) as f:
        knots=f['unit_knots'];coeff=f['coefficients'];pm=f['planar_modes'];zm=f['vertical_modes']
        require(coeff.dtype==np.float64 and np.all(np.isfinite(coeff)) and np.all(np.isfinite(knots)),'Actual finite saved coefficients required')
        require(np.array_equal(pm,np.arange(-grid['order'],grid['order']+1)*3+1) and np.array_equal(zm,np.arange(grid['order']+1)*3),'Incomplete actual D3 modes')
        require(np.all(knots[1:]>=knots[:-1]) and np.all(knots[:6]==0) and np.all(knots[-6:]==1),'Quintic clamped field required')
        require(coeff.shape==(len(knots)-12,len(pm)+len(zm)),'Complete free coefficient array required')
        unique,multiplicity=np.unique(knots,return_counts=True)
        require(np.all(multiplicity[(unique>0)&(unique<1)]<=3),'Saved W lacks global C2 continuity')
        field_shape=list(coeff.shape)
    require(smooth['script_sha256']==PINNED['2ecf-m12-smooth-source-seams.py'] and smooth['manifest_sha256']==MANIFEST_SHA,'Exact Q definition changed')
    true_fields(smooth,('complete_original_finite_tail','same_original_g','every_original_node_zero_two_jets_of_correction',
        'all_derivatives_unchanged_at_window_endpoints','disjoint_windows','all_internal_polynomial_seams_C_infinity'))
    require(smooth['selected_spans']==18552 and smooth['internal_seams_smoothed']==18551 and smooth['complete_Fourier_modes']==141,'Incomplete Q source')
    require(regular['script_sha256']==PINNED['2ecf-m12-smooth-source-merge-cache.py'] and qr['script_sha256']==PINNED['2ecf-m12-smooth-source-query-cache.py'],'Accurate query source producer changed')
    require(regular['schema']=='m12-R250-regularized-tail-query-source-v1' and regular['same_original_tail_source'] is False,'Separate regularized source epoch required')
    identity=regular['source_regularization']
    for record,key,argument in (
        (original,'endpoint_cache_sha256','query_cache'),(base,'endpoint_cache_sha256','regularized_base_cache'),
        (qr,'original_source_report_sha256','regularized_base_report'),(qr,'original_source_cache_sha256','regularized_base_cache'),
        (qr,'cache_sha256','Q_query_cache'),(qr,'smoothing_report_sha256','smoothing_report'),
        (regular,'endpoint_cache_sha256','regularized_cache'),
        (identity,'original_source_report_sha256','regularized_base_report'),(identity,'original_source_cache_sha256','regularized_base_cache'),
        (identity,'Q_point_report_sha256','Q_query_report'),(identity,'Q_point_cache_sha256','Q_query_cache'),
        (identity,'Q_continuous_report_sha256','smoothing_report')):
        require(record[key]==hashes[argument],'Regularized source input differs: '+key)
    for record in (original,base,qr,regular):require(record['manifest_sha256']==MANIFEST_SHA,'Query source has another manifest')
    require(identity['Q_divisor']==smooth['divisor'] and identity['Q_exact_jump_stream_sha256']==smooth['exact_jump_and_window_stream_sha256'],'Different Q windows or jumps')
    require(identity['Q_continuous_physical_s_u_six_jet_upper']==smooth['physical_s_u_six_jet_upper'],'Regularized source carries another global Q bound')
    true_fields(identity,('same_original_target_metric','same_central_common_cut_and_true_cuff_two_jets','not_the_original_unregularized_source'))
    require(regular['query_file_sha256']==base['query_file_sha256'],'Runtime query recipe changed during source merge')
    endpoint_keys=('endpoint_numerator','endpoint_denominator','first','second','planar_modes','height_modes')
    with np.load(args.query_cache,allow_pickle=False) as old,np.load(args.regularized_base_cache,allow_pickle=False) as new,np.load(args.regularized_cache,allow_pickle=False) as merged:
        for key in endpoint_keys:
            require(np.array_equal(old[key],new[key]) and np.array_equal(new[key],merged[key]),'Original endpoint or complete mode data changed: '+key)
        require(np.array_equal(new['query_fraction'],merged['query_fraction']),'Runtime exact query radii changed')
    for key in ('finite_inner_exact','outer_cut_exact','true_cuff_exact'):
        require(F(original[key])==F(base[key])==F(regular[key]),'Physical endpoint changed: '+key)
    require(F(smooth['selected_inner_exact'])==F(original['finite_inner_exact']) and F(smooth['outer_exact'])==F(original['outer_cut_exact']),'Q does not use the same exact finite tail')

    B={k:F(v['exact']) for k,v in smooth['physical_s_u_six_jet_upper'].items()}
    require(set(B)=={'Q','Qs','Qu','Qss','Qsu','Quu'} and min(B.values())>=0,'Complete exact nonnegative Q six jets required')
    rmin=F(smooth['selected_inner_exact']);pQ=B['Qs']+B['Qu']/rmin
    cQ=B['Qss']+2*B['Qsu']/rmin+B['Quu']/rmin**2
    old=two['rational_quantities'];reg=regional['rational_quantities']
    eta0=exact(old,'displacement');p0=exact(old,'target_differential');cw0=exact(old,'change_scaled_second_jets')
    pp=exact(reg,'prefix_differential');require(pp<=p0,'Invalid prefix norm cap')
    require(exact(reg,'tail_differential')==p0,'Regional tail did not use actual full differential')
    cxp=F(source['prefix_original_C_X']['upper_exact']);cxt=F(source['tail_original_C_X']['upper_exact'])
    require(exact(reg,'prefix_source_CX')==cxp and exact(reg,'tail_source_CX')==cxt,'Regional original source CX differs')
    eta=eta0+B['Q'];p=p0+pQ;cw=cw0+cQ
    d0=F(257212,10**13);K0=F(4763997235009095,562949953421312);R=F(2131902881202937,1125899906842624)
    eps0=exact(metric,'relative_metric_upper');fine=eps0+2*(1+eps0)*pQ+pQ*pQ
    coarse=d0+2*(1+d0)*p+p*p
    require(coarse<1,'No uniform homotopy immersion from these inputs')
    nu=lambda v:(3*v+v*v)/(1-d0)
    # Q is identically zero throughout the complete prefix, central seam,
    # deep collar, true cuff and caps. Only the tail Hessian budget grows.
    kp=(K0*(1+d0)+nu(pp)*cxp+cw0)/(1-coarse)
    kt=(K0*(1+d0)+nu(p)*cxt+cw)/(1-coarse)
    K=max(K0,kp,kt);D=2*(R+eta);support=F(737,1000)-F(19,10)*nu(p)-eta
    reach=1/(K*D);held=(F(19989114,10**8)-2*eta)/D
    cap=F(35426,10**4)/D;moment=2400*eta*(1+9*eta)**2
    checks={'same_original_target_g_and_material_parameters':True,'globally_C2_and_C2_continuous_in_original_phase':True,
        'complete_original_phase_interval':True,'central_and_true_cuff_zero_two_jets_preserved':True,
        'fixed_cap_holding_region_unchanged':True,'homotopy_immersion':coarse<1,
        'displacement_inside_original_normal_tube':eta<1/K0,'swept_surface_inside_radius_two':R+eta<2,
        'positive_support_exceeds_inverse_curvature':support>1/K,'fixed_marker_height_inside_new_normal_tube':K<2000,
        'activity_third_moment_still_positive':moment<F(44016,10**5),'full_space_and_phase_metric_below_1e_6':fine<F(1,10**6),
        'full_space_and_phase_reach_over_D_above_003':reach>F(3,100),'held_over_D_above_005':held>F(5,100),
        'fixed_cap_diameter_over_D_above_02':cap>F(1,5)}
    geometry=all(checks[k] for k in ('homotopy_immersion','displacement_inside_original_normal_tube','swept_surface_inside_radius_two',
        'positive_support_exceeds_inverse_curvature','fixed_marker_height_inside_new_normal_tube','activity_third_moment_still_positive'))
    candidate={'definition':'Exact Y=X+C+Q+W, with the actual saved W unchanged and exact complete R250 Q added to the mathematical source.',
        'original_prefix_data_sha256':DATA_SHA,'original_common_meta_sha256':META_SHA,'original_bridge_sha256':BRIDGE_SHA,
        'original_tail_manifest_sha256':MANIFEST_SHA,'unchanged_saved_W_sha256':hashes['field'],'unchanged_saved_W_grid_sha256':hashes['grid'],
        'Q_producer_sha256':smooth['script_sha256'],'Q_divisor':smooth['divisor'],
        'Q_exact_jump_stream_sha256':smooth['exact_jump_and_window_stream_sha256'],
        'phase':'Original R234/R250 ambient orbit and fixed-cap family; same complete phase interval.'}
    candidate_hash=hashlib.sha256(json.dumps(candidate,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    quantities={'Q_displacement':B['Q'],'Q_target_differential':pQ,'Q_scaled_coordinate_second_jets':cQ,
        'total_displacement':eta,'prefix_differential_unchanged':pp,'tail_and_global_differential':p,
        'prefix_scaled_second_jets_unchanged':cw0,'tail_scaled_second_jets':cw,
        'complete_metric':fine,'homotopy_metric_triangle':coarse,'global_normal_change':nu(p),
        'prefix_curvature':kp,'tail_curvature':kt,'whole_curvature':K,'diameter':D,
        'support':support,'reach_over_D':reach,'held_over_D':held,'fixed_cap_diameter_over_D':cap,'activity_moment_loss':moment}
    lower={'support','reach_over_D','held_over_D','fixed_cap_diameter_over_D'}
    out={'schema':'2ecf-M12-exact-Q-plus-actual-field-all-phase-geometry-v1','script_sha256':sha(__file__),
        'input_sha256':hashes,'published_producer_sha256':PINNED,
        'new_mathematical_candidate':candidate,'new_mathematical_candidate_identity_sha256':candidate_hash,
        'original_solver_result_retained_as_Q_free':True,'saved_coefficient_array_unchanged':True,
        'physical_source_and_map_changed_by_exact_Q':True,'actual_saved_field_shape':field_shape,
        'runtime_regularized_source_identity':identity,
        'runtime_query_cache_is_finite_evaluation_interface_not_definition':True,
        'runtime_query_base_may_differ_from_original_solver_recipe_without_changing_X':True,
        'runtime_Q_query_evaluation_error':qr['cache_error_physical_s_u_six_jet_upper'],
        'runtime_additional_Q_merge_error':regular['additional_error_physical_s_u_six_jet_upper'],
        'runtime_old_source_evaluation_and_angular_roundoff_not_recertified':True,
        'Q_continuous_physical_s_u_six_jet_upper':smooth['physical_s_u_six_jet_upper'],
        'rational_quantities':{k:packet(v,'lower' if k in lower else 'upper') for k,v in quantities.items()},
        'checks':checks,'all_reported_thresholds_proved':all(checks.values()),
        'full_space_all_phase_embedding_and_reach':geometry,'strict_noncongruence_including_reflections':geometry,
        'noncongruence_basis':'R16 unchanged fixed-cap markers, preserved D3/reflection orbit and positive activity third moment after the displayed loss.',
        'new_nonlinear_solve_or_acceptance':False,'old_solver_residual_relabelled_as_regularized':False,
        'isometry_error_improvement_asserted':False,'exact_isometry_proved':False,'README_condition5_proved':False,
        'regularized_closed_meshes_generated_in_this_consumer':False,
        'regularity_scope':'Global C2 only. The finite-tail polynomial source is smooth internally; saved W may have C2 triple knots.',
        'seconds':time.monotonic()-began}
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'report':str(args.out),'report_sha256':sha(args.out),'candidate_identity':candidate_hash,
        'all_thresholds':all(checks.values()),'quantities_display':{k:float(v) for k,v in quantities.items()},'seconds':out['seconds']},indent=2),flush=True)

if __name__=='__main__':main()
