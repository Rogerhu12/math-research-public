#!/usr/bin/env python3
"""Bind a complete secant geometry screen to its production initial field.

All recorded sample comparisons are diagnostic.  The complete planar core
gap and R7 expression use exact rationals of every saved binary64 mode.
No candidate is promoted to a nonlinear solution or a continuous surface.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path): return json.loads(Path(path).read_text())
def exact(x): return Q(*float(x).as_integer_ratio())
def rec(x): return dict(numerator=str(x.numerator),denominator=str(x.denominator),decimal_display=float(x))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('baseline-screen','candidate-screen','geometry-prepared','production-prepare','out'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--accepted-tail-kappa',type=float,required=True)
    a=ap.parse_args()
    if a.out.exists(): raise FileExistsError(a.out)
    base,cand,geom,prod=[read(p) for p in (a.baseline_screen,a.candidate_screen,a.geometry_prepared,a.production_prepare)]
    original=geom['original_secant']; gates={}
    def check(name,condition):
        if not condition: raise ValueError(name)
        gates[name]=True
    for label,d in (('baseline',base),('candidate',cand)):
        check(label+'_complete_unsolved_geometry',d['finished'] and d['finite_domain_passed'] and
              not d['nonlinear_solution'] and not d['true_new_H_tail_evaluated'] and d['worker_start_attempts']==0)
        g=d['geometry_fields']
        check(label+'_complete_mean',g['complete_mean_height'] and g['all_raw_nodes_and_modes_retained'] and
              g['mean_quadrature']['mean_height_first_second_same_angular_rule'] and
              g['mean_quadrature']['angular']>=g['mean_quadrature']['original_postprocessor_angular'])
        check(label+'_positive_sample_domain',g['minimum_frenet_margin_sample']>0 and g['minimum_tangent_area_sample']>0)
    check('one_complete_common_grid',base['geometry_fields']['grid_sha256']==cand['geometry_fields']['grid_sha256']
          ==geom['common_grid']['grid_sha256'])
    check('preserved_all_raw_nodes',geom['common_grid']['all_raw_nodes_present'] and
          geom['common_grid']['angular']>=768 and geom['common_grid']['angular']%768==0)
    keys=('current_reference_sha256','current_raw_sha256','previous_reference','previous_raw',
          'target_core','external_shifts','scale','geometry_increment','full_direction_shape',
          'full_direction_float64le_sha256','pure_secant_direction_float64le_sha256',
          'initial_complete_height_hold')
    for key in keys: check('same_production_predictor_'+key,original[key]==prod[key])
    check('full_direction_is_pure_secant',original['full_direction_float64le_sha256']==original['pure_secant_direction_float64le_sha256'])
    check('same_target_core',cand['geometry_fields']['actual_core'][:3]==original['target_core'])
    rows=[]
    for label,d in (('baseline',base),('candidate',cand)):
        g=d['geometry_fields'];c=list(map(exact,g['actual_core']))
        gap=2*sum((value for j,value in enumerate(c,1) if j%2),Q(0))
        rho=1-sum(((4*j*j-1)*value*((-1)**j) for j,value in enumerate(c,1)),Q(0))
        k0=exact(g['physical_profile']['start_acceleration']);S=exact(g['twice_radius_max_sample'])
        kappa=exact(g['kappa_abs_max_sample']);tail=exact(a.accepted_tail_kappa)
        check(label+'_positive_complete_core_witness',gap>0 and rho>0)
        rows.append(dict(name=label,complete_core_modes=len(c),complete_core_binary_coefficients=[rec(x) for x in c],
            axial_core_support_gap=rec(gap),short_axis_core_curvature_radius=rec(rho),
            initial_acceleration=rec(k0),R7_initial_witness_product=rec(k0*gap*rho),
            R7_product_below_one=k0*gap*rho<1,
            S_twice_fixed_origin_norm_sample=rec(S),prefix_kappa_sample=rec(kappa),
            prefix_kappa_times_S_sample=rec(kappa*S),
            current_accepted_tail_floor_kappa_times_S_diagnostic=rec(max(kappa,tail)*S),
            finite_sample_budget_below_100_over3=max(kappa,tail)*S<Q(100,3),
            finite_sample_budget_margin=rec(Q(100,3)-max(kappa,tail)*S),
            complete_core_gap_over_S_sample=float(gap/S),
            physical_profile=g['physical_profile'],
            min_Frenet_margin_sample=g['minimum_frenet_margin_sample'],
            min_tangent_area_sample=g['minimum_tangent_area_sample'],
            complete_H_change_max=d['complete_H_change_max']))
    out=dict(schema='actual-secant-complete-geometry-production-identity-budget-v1',scope=__doc__,
        source_sha256=sha(__file__),input_sha256={str(p):sha(p) for p in
          (a.baseline_screen,a.candidate_screen,a.geometry_prepared,a.production_prepare)},
        gates=gates,all_identity_and_domain_gates=True,rows=rows,
        candidate_sample_size_relative_change=float(exact(cand['geometry_fields']['twice_radius_max_sample'])/
                                                   exact(base['geometry_fields']['twice_radius_max_sample'])-1),
        accepted_tail_kappa_sample=a.accepted_tail_kappa,
        target_core=original['target_core'],scale=original['scale'],
        new_candidate_nonlinear_solution=False,new_candidate_true_tail_evaluated=False,
        continuous_kappa_or_reach_proved=False,closed_surface_diameter_proved=False,
        limitations=['S is twice sampled distance from the one fixed origin; it is not a complete closed diameter certificate.',
                     'The accepted old tail floor is a diagnostic and is not a certificate for the new target H.',
                     'The core witness expression is exact for the finite saved coefficients only.',
                     'The unchanged production Newton, full true-H tail, RMS, physical BC, postprocessor and final audit remain mandatory.'])
    a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(out=str(a.out),sha256=sha(a.out),identity_gates=len(gates),
        sample_budget=rows[-1]['finite_sample_budget_below_100_over3'],
        gap_over_S=rows[-1]['complete_core_gap_over_S_sample'],
        R7=rows[-1]['R7_initial_witness_product']['decimal_display'])),flush=True)


if __name__=='__main__':main()
