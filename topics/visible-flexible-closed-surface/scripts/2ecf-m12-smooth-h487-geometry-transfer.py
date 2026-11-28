#!/usr/bin/env python3
"""Exact consequence of R245 for its specified h487 field plus smooth Q.

This inherits the published R245 theorem's explicitly bound saved field;
it does not read or substitute a newly regenerated local h487 field. The
new candidate is the exact mathematical sum Y_R245+Q, not a new Newton
acceptance, and no exact-isometry or refinement-completion claim is made.
"""
from __future__ import annotations
import argparse,hashlib,json,time
from fractions import Fraction as Q
from pathlib import Path

SMOOTHER_SHA='30b1384fed8e7a6018c99ba688b091bb42dfb2451e2df39531c9df0d88aa34b7'
R245_PROOF_SHA='960d606afbeb4b634d7051497b8bd64a46db945aa1b2c545fcc68810d35d27f0'
R245_FIELD_SHA='cdcbbd53c4019d0b4df88043662c13c736b65429575e6276ac44bb482375aa12'
MANIFEST_SHA='cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def packet(x):return {'exact':str(x),'display':float(x)}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--smoothing-report',type=Path,required=True)
    ap.add_argument('--r245-proof',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();began=time.monotonic()
    if args.out.exists():raise FileExistsError('Fresh exact transfer report required')
    if sha(args.r245_proof)!=R245_PROOF_SHA:raise ValueError('Published R245 theorem changed')
    r=json.loads(args.smoothing_report.read_text())
    if r['schema']!='m12-exact-C-infinity-finite-source-seam-regularization-v1':raise ValueError('Unknown exact smoothing report')
    if r['script_sha256']!=SMOOTHER_SHA or r['manifest_sha256']!=MANIFEST_SHA:raise ValueError('Smoothing source changed')
    for k in ('complete_original_finite_tail','same_original_g','every_original_node_zero_two_jets_of_correction',
              'all_derivatives_unchanged_at_window_endpoints','disjoint_windows','all_internal_polynomial_seams_C_infinity'):
        if r[k] is not True:raise ValueError('Missing full-domain source premise: '+k)
    if r['selected_spans']!=18552 or r['internal_seams_smoothed']!=18551 or r['complete_Fourier_modes']!=141:
        raise ValueError('Incomplete original finite tail')
    B={k:Q(v['exact']) for k,v in r['physical_s_u_six_jet_upper'].items()}
    if set(B)!={'Q','Qs','Qu','Qss','Qsu','Quu'} or min(B.values())<0:raise ValueError('Complete nonnegative exact six-jets required')
    rmin=Q(r['selected_inner_exact']);pQ=B['Qs']+B['Qu']/rmin
    cQ=B['Qss']+2*B['Qsu']/rmin+B['Quu']/rmin**2
    # R245 section 4 gives these explicit safe outward decimal endpoints.
    eta0=Q('1.402864e-9');p0=Q('1.794754e-6');cw0=Q('.005437327');cx=Q('4461.108')
    fine_metric0=Q('8.211825e-7')
    eta=eta0+B['Q'];p=p0+pQ;cw=cw0+cQ
    d=Q(257212,10**13);K0=Q(4763997235009095,562949953421312)
    R=Q(2131902881202937,1125899906842624)
    coarse=d+2*(1+d)*p+p*p;fine=fine_metric0+2*(1+fine_metric0)*pQ+pQ*pQ
    normal=(3*p+p*p)/(1-d);diameter=2*(R+eta)
    if coarse>=1:raise ArithmeticError('Cannot prove homotopy immersion')
    K=(K0*(1+d)+normal*cx+cw)/(1-coarse)
    support=Q(737,1000)-Q(19,10)*normal-eta
    reach=1/(K*diameter);held=(Q(19989114,10**8)-2*eta)/diameter
    cap=Q(35426,10**4)/diameter;moment=2400*eta*(1+9*eta)**2
    checks={'exact_C2_and_same_phase_interval_by_theorem':True,'same_target_g':True,
      'central_and_true_cuff_fixed':True,'original_tube_covers_displacement':eta<1/K0,
      'swept_tube_inside_radius_2':R+eta<2,'homotopy_metric_immersion':coarse<1,
      'positive_support_exceeds_inverse_curvature':support>1/K,
      'marker_height_inside_normal_tube':K<2000,'positive_activity_third_moment':moment<Q(44016,10**5),
      'whole_space_whole_phase_metric_below_1e_6':fine<Q(1,10**6),
      'reach_over_diameter_above_0_03':reach>Q(3,100),
      'held_over_diameter_above_0_05':held>Q(5,100),
      'fixed_cap_diameter_above_0_2':cap>Q(1,5)}
    if not all(checks.values()):raise ArithmeticError('At least one full candidate threshold is not proved')
    quantities={'Q_target_differential':pQ,'Q_scaled_coordinate_second_jets':cQ,
      'total_displacement':eta,'total_target_differential':p,'total_scaled_coordinate_second_jets':cw,
      'metric_via_R245_continuous_fine_bound':fine,'metric_coarse_for_curvature_transfer':coarse,
      'normal_change_from_R21':normal,'positive_support':support,'diameter_upper':diameter,
      'principal_curvature_upper':K,'reach_over_diameter_lower':reach,'held_over_diameter_lower':held,
      'fixed_cap_diameter_ratio_lower':cap,'activity_moment_loss_upper':moment}
    out={'schema':'m12-exact-smoothed-R245-h487-all-phase-geometry-transfer-v1','script_sha256':sha(__file__),
      'smoothing_report_sha256':sha(args.smoothing_report),'smoothing_source_sha256':SMOOTHER_SHA,
      'smoothing_divisor':r['divisor'],'smoothing_exact_jump_stream_sha256':r['exact_jump_and_window_stream_sha256'],
      'R245_published_proof_sha256':R245_PROOF_SHA,'R245_inherited_saved_field_sha256':R245_FIELD_SHA,
      'R245_run':45833090043,'R245_source_commit':'a060a8d1cb7bf95d6b8d5087467cf63377e3867e',
      'actual_existing_h487_field_read':False,'newly_regenerated_local_field_substituted':False,
      'candidate':'Exact R245 mathematical field Y plus exact all-original-finite-seam Q from the same manifest and divisor.',
      'inherited_theorems':['R245 exact specified finite h487 field and explicit outward bounds',
        'R21 original continuous geometry','R10 positive support normal tube','R16 D3 fixed-cap moment invariant',
        'R226/R230 physical/material source chart and entire-source bounds'],
      'checks':checks,'quantities':{k:packet(v) for k,v in quantities.items()},
      'new_nonlinear_acceptance':False,'isometry_error_improvement_asserted':False,
      'exact_isometry_proved':False,'README_condition5_proved':False,
      'smoothed_source_polynomial_part_C_infinity_on_finite_tail':True,
      'full_Y_plus_Q_claimed_C_infinity':False,
      'full_Y_plus_Q_regularities':'C2 globally; the inherited W is C4 on its radial interior grid, and the unchanged background/interfaces keep their established regularity.',
      'seconds':time.monotonic()-began}
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'report':str(args.out),'all_checks':True,'quantities_display':{k:float(v) for k,v in quantities.items()},'seconds':out['seconds']},indent=2))

if __name__=='__main__':main()
