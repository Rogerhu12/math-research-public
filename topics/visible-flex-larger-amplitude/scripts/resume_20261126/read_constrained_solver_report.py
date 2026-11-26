#!/usr/bin/env python3
"""Compact actual all-row SOC / v5 attribution; JSON and source text only.

No scientific array, field, Jacobian or new fixture is read or evaluated.
The actual complete driver body is validated by the explicit source binder.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

SCALAR_SHA='9124229786200659f1c9dc73620eecd75dda6493990f684149471d7003263b9d'
OLD_READER_SHA='adc90f41cb7cb1dd4b5842e547d2381432094e8e0565c63c5859e5bcfc1d06dd'
DERIVERS={False:('derive_full_phi_all_rows_soc.py','94ea77107305c058425877a3ff93cf7e8b58575e982f5ca6c1040a32279a0f73'),
          True:('derive_full_phi_face_pcg.py','7b3e7911b35beab8a5979e91cecdd1d35f467bc39dddb57e1035d327896067ed')}

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load(name,path,digest):
    if sha(path)!=digest:raise ValueError('Actual small source changed: '+str(path))
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod

def selected(d,keys):return {k:d.get(k) for k in keys}
def stats(d):
    return dict(max_relative_gram=d.get('max_relative_gram'),
        legacy_max_relative_gram=d.get('legacy_max_relative_gram'),
        radial_weighted_mean_sse=d.get('radial_weighted_mean_sse'),
        spectral=selected(d.get('spectral',{}),('p','epsilon','scale','phi_normalized','phi_zero','max_gram')))
def trial(t):
    return dict(**selected(t,('index','alpha','kind','merit','finite','feasible','descent','curvature_feasible',
        'half_objective_slope','quadratic_predicted_actual_change','actual_to_same_corrected_step_predicted_decrease')),
        statistics=stats(t.get('statistics',{})),curvature_filter=t.get('curvature_filter'),
        curvature=selected(t.get('curvature_points') or {},('complete','maximum_absolute_principal_curvature',
            'closed_body_diameter_point_lower','worst','maximum_radius_point')))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True);p.add_argument('--report',type=Path,required=True)
    p.add_argument('--driver',type=Path);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError('Use a new attribution output')
    r=json.loads(a.report.read_text());source=a.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120'
    here=Path(__file__).resolve().parent
    is_v5='face_pcg_derivation' in r;name,digest=DERIVERS[is_v5]
    deriver=load('actual_constrained_report_binder',here/name,digest)
    driver=a.driver or Path(r['diameter_diagnostic_source'])
    binding=deriver.bind_soc_parent(r,driver,source,source/'launch_fixed_g_refinement_qp.py')
    scalar=load('actual_constrained_scalar_reader',source/'full_phi_qp_scalar_diagnostics.py',SCALAR_SHA)
    old=load('actual_constrained_original_ray_view',source/'full_phi_pcg_soc_report.py',OLD_READER_SHA)
    parent=r.get('initial',{});directions=[]
    for j,d in enumerate(r.get('directions',[])):
        view,view_scope=old.original_ray_view(d)
        qp=d.get('qp',{});soc=d.get('soc') or {};proposal=soc.get('proposal') or {}
        projection=proposal.get('constrained_projection') or {}
        metric=qp.get('fixed_preconditioner',{}).get('face_metric') or {}
        item=dict(**selected(d,('index','accepted','accepted_alpha','accepted_update_kind','accepted_bundle_sha256',
            'old_merit','new_merit','damping','damping_after_direction','seconds')),
            QP=selected(qp,('schema','status','advances','maxiter','seconds','initial_gradient_norm',
                'gradient_tolerance','final_face_projected_gradient_norm','maximum_linear_violation',
                'maximum_complementarity_residual','longest_same_face_advances','operator_products')),
            original_ray_model_scope=view_scope,
            original_QP_scalars=scalar.analyze_direction(view,parent,r),
            original_trials=[trial(t) for t in d.get('trials',[])],
            SOC=dict(**selected(soc,('attempted','accepted','seconds','additional_cost')),
                proposal=selected(proposal,('schema','complete','attempted','proposal_available','reason','tau',
                    'correction_norm','correction_over_original_norm','corrected_coordinate_norm',
                    'corrected_maximum_linear_violation','all_fixed_parent_nonlinear_target_maximum_violation')),
                projection=selected(projection,('schema','status','numerical_feasible','minimum_norm_convergence_claimed',
                    'rows','sweeps','max_sweeps','actual_maximum_violation','direct_projected_dual_gradient_inf',
                    'floating_primal_dual_gap','complementarity_max_abs','preparation_seconds','seconds','infeasibility_proved')),
                corrected_actual_trial=trial(soc['trial']) if soc.get('trial') is not None else None),
            face_preconditioner=selected(metric,('schema','current_mode','applications','global_B_applications',
                'global_B_seconds','preparation_seconds','maximum_cached_vectors','maximum_cached_vector_bytes',
                'maximum_observed_Schur_skew','fallback_faces','preparation_history')))
        directions.append(item)
        if d.get('accepted'):
            if d.get('accepted_update_kind')=='parent_row_soc':parent=soc['trial']['statistics']
            else:
                candidates=[t for t in d.get('trials',[]) if t.get('alpha')==d.get('accepted_alpha')]
                if len(candidates)!=1:raise ValueError('Accepted actual ray is not uniquely identified')
                parent=candidates[0]['statistics']
    result=scalar.sanitize(dict(schema='actual-constrained-SOC-v5-compact-attribution-v1',
        source_sha256=sha(__file__),report=str(a.report.resolve()),report_sha256=sha(a.report),
        actual_driver=binding,report_complete=r.get('complete'),
        input_bundle_sha256=r.get('bundle_sha256'),final_bundle_sha256=r.get('final_bundle_sha256'),
        initial=stats(r.get('initial',{})),final=stats(r.get('current',r.get('initial',{}))),
        initial_damping=r.get('initial_damping'),final_damping=r.get('final_damping'),
        final_known_point_filter=r.get('final_curvature_filter'),sample_target=r.get('sample_target'),
        directions=directions,scientific_arrays_read=0,field_evaluations=0,J_calls=0,Jtranspose_calls=0,
        new_fixtures=0,strict_arithmetic=False,continuous_metric_or_reach_claimed=False,
        interpretation='Actual returned scalars only. A finite feasible SOC proposal, minimum-norm convergence, inner-QP stationarity, true Phi acceptance and continuous geometry are separate.'))
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(result,separators=(',',':'),allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(a.out.resolve()),sha256=sha(a.out),bytes=a.out.stat().st_size,
        directions=len(directions),final=result['final'],final_filter=result['final_known_point_filter'],
        SOC=[d['SOC'] for d in directions],QP=[d['QP'] for d in directions]),separators=(',',':')),flush=True)
if __name__=='__main__':main()
