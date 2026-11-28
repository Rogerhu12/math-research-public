#!/usr/bin/env python3
"""Pay the true full-tail premises of the existing third-activity flux bound.

Both reflected tails, their actual deep collars, and plain disks are included.
The fixed marker is excluded. The bound is for the unshifted activity A3(0),
to be combined with the same prefix flux and the R67 increment ell*m3.
No numerical moment, geometric polynomial, or background integral is rerun.
"""
import argparse
from fractions import Fraction as Q
from pathlib import Path

import tail_metric_complete_supplement_v2 as supplement
from qr_coupled_prefix_continuous import CoupledContext, SOURCE_KIND

REVIEWED_FLUX = Path(__file__).with_name("tail_third_activity_flux_bound.py")
REVIEWED_FLUX_SHA = "2dcaf9cfde8a6923c0ac0e32a81ae7f5356d12025239b467c7ad7ab3a94767f7"

original = supplement.original
ref, write, checked_plain = supplement.ref, supplement.write, supplement.checked_plain


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--placement-report',type=Path,required=True)
    p.add_argument('--complete-original-certificate',type=Path,required=True)
    p.add_argument('--outdir',type=Path,required=True)
    p.add_argument('--coupling-summary',type=Path,required=True)
    args=p.parse_args()
    if ref(REVIEWED_FLUX)['sha256']!=REVIEWED_FLUX_SHA:
        raise ValueError('The unchanged complete-tail flux proof source changed')
    out=args.outdir.resolve();out.mkdir(parents=True,exist_ok=False)
    placement=checked_plain(ref(args.placement_report))
    if (placement['status']!='same_actual_tail_absolute_placement_and_global_curvature_certified'
            or placement['cylinder_half_length_exact']!='0'
            or placement['marker_amplitude_exact']!='0'
            or not placement['complete_deep_collar_and_plain_disks_included']):
        raise ValueError('A same actual complete unshifted/unmarked tail placement is required')
    if ref(placement['source']['path'])!=placement['source']:
        raise ValueError('The actual placement proof source changed')
    height=checked_plain(placement['absolute_height'])
    context=CoupledContext(args.coupling_summary,'complete-tail-third-activity-bound')
    actual,physical,binding=context.accept(height['prefix_source_run']['path'])
    del actual,physical
    if (placement.get('actual_source_kind')!=SOURCE_KIND
            or placement['source']!=ref(Path(__file__).with_name('qr_tail_actual_placement.py'))
            or height.get('actual_coupled_gate_provenance')!=context.payload['actual_coupled_gate_provenance']
            or height.get('final_physical_height_binding')!=context.payload['full_height_binding']
            or height['accepted_packet']!=binding['packet']
            or height.get('raw_candidate_used_as_final_height') is not False):
        raise ValueError('The same actual QR physical-height placement is required')
    for key in ('geometry_bundle','constants','normalization','physical_R_identity','entire_mean','accepted_packet'):
        if ref(height[key]['path'])!=height[key]:
            raise ValueError('A complete actual height/background input changed: '+key)
    bundle=checked_plain(height['geometry_bundle'])
    spectrum=checked_plain(bundle['spectrum_contract'])
    index=checked_plain(bundle['canonical_node_index'])
    radius=checked_plain(height['physical_R_identity'])
    complete_ref=ref(args.complete_original_certificate)
    complete=checked_plain(complete_ref)
    if (complete['geometry_bundle']!=height['geometry_bundle']
            or complete['accepted_packet']!=height['accepted_packet']
            or complete['original_mean_chain']!=height['entire_mean']
            or complete['constants']!=height['constants']
            or complete['normalization']!=height['normalization']
            or not complete['all_finite_stages_audited']
            or not complete['complete_tail_disk_planar_projection_injective']
            or not complete['finite_tail_to_its_own_deep_disk_C2']
            or complete['component_certificate_summaries']!=placement['original_geometric_summaries']
            or ref(complete['source']['path'])!=complete['source']):
        raise ValueError('The actual same complete projected disk and C2 collar are not proved')
    if (radius['geometry_bundle']!=height['geometry_bundle']
            or not radius['radius_chart_identity_proved']
            or Q(radius['reparameterization_delta_exact'])!=0):
        raise ValueError('Only the proved same physical-R identity is accepted')
    rows=checked_plain(placement['component_bounds'])
    stages=[row['component']['stage'] for row in rows if isinstance(row['component'],dict)]
    S=index['finite_stage_count']
    if (sorted(stages)!=list(range(S)) or len(rows)!=S+2
            or placement['finite_stage_count']!=S
            or not all(Q(row['first_jet_upper_exact'])<1 for row in rows)):
        raise ValueError('The entire finite tail, actual collar and inner disk are required')
    labels={row['component'] for row in rows if isinstance(row['component'],str)}
    if labels!={'same_actual_zero_jet_deep_collar','unchanged_rotational_cuff_and_plain_disks'}:
        raise ValueError('The actual deep component inventory changed')
    constants=checked_plain(height['constants'])
    Rc=Q.from_float(constants['parameters']['rCut'])
    if Q(radius['physical_cut_radius_exact'])!=Rc:
        raise ValueError('Another physical cut radius was substituted')
    perturbation=max(Q(row['position_upper_exact']) for row in rows)
    pole_low,pole_high=map(Q,height['exact_upper_plain_disk_height_interval'])
    if perturbation<0 or not 0<pole_low<=pole_high:
        raise ValueError('The actual positive height and full perturbation bounds are missing')
    rstar=Rc+perturbation
    Z=pole_high+perturbation
    pi_upper=Q(22,7)
    bound=4*pi_upper*Z*rstar**5/5
    moment_source=Path(__file__).resolve().parents[1]/'analytic/cartesian_third_activity_moment.py'
    report=dict(
        status='actual_complete_tail_and_deep_disk_third_activity_flux_bounded',
        source=ref(__file__),placement=ref(args.placement_report),
        actual_source_kind=SOURCE_KIND,actual_coupled_source_verified=True,
        coupling_summary=context.payload['coupling_summary'],
        final_physical_height_binding=context.payload['full_height_binding'],
        actual_coupled_gate_provenance=context.payload['actual_coupled_gate_provenance'],
        raw_candidate_used_as_final_height=False,reviewed_original_flux_source=ref(REVIEWED_FLUX),
        absolute_height=placement['absolute_height'],
        complete_original_projection_certificate=complete_ref,
        complete_component_bounds=placement['component_bounds'],
        existing_conditional_formula_source=ref(moment_source),
        geometry_bundle=height['geometry_bundle'],prefix_source_run=height['prefix_source_run'],
        actual_cut_certificate=height['cut_certificate'],
        cut_width_exact=height['cut_width_exact'],
        spectrum_contract=bundle['spectrum_contract'],finite_scope=spectrum['finite_scope'],
        accepted_packet=height['accepted_packet'],entire_mean=height['entire_mean'],
        physical_R_identity=height['physical_R_identity'],
        true_background_constants=height['constants'],true_background_normalization=height['normalization'],
        finite_stage_count=S,literal_span_count=placement['original_literal_span_count'],
        actual_deep_collar_and_plain_disks_included=True,
        complete_injective_planar_projection=True,
        physical_R_exact_identity=True,
        perturbation_position_upper=original.upper_row(perturbation),
        horizontal_radius_upper=original.upper_row(rstar),
        absolute_height_upper=original.upper_row(Z),
        pi_upper_exact=str(pi_upper),
        two_reflected_tail_complex_third_flux_absolute_upper=original.upper_row(bound),
        two_reflected_tail_real_third_flux_interval=[original.lower(-bound),original.upper(bound)],
        bound_formula='4*pi_upper*Z*r_star^5/5',
        proof='The complete projected upper tail is injective and lies in |w|<=r_star; both reflected tail fluxes have absolute value <=2*Z*integral_projection |w|^3 dA <=2*Z*integral_disk |w|^3 dA=4*pi*Z*r_star^5/5.',
        prefix_density_compatibility='2*z*Re(w^3)*(Xpsi_x*Xs_y-Xpsi_y*Xs_x); the factor two already includes the reflected lower piece.',
        activity_combination='A3(ell)=A3_prefix(0)+A3_tail(0)+ell*m3; use this unshifted tail bound with the same actual prefix/core output.',
        fixed_marker_contribution_excluded=True,
        original_integral_or_geometry_recomputed=False,
        tail_metric_gate_assumed=False,
        actual_cylinder_length_selected=False,
        whole_activity_nonzero_claimed=False,
        euclidean_noncongruence_claimed=False,
        whole_surface_metric_claimed=False)
    path=out/'summary.json';write(path,report)
    import json
    print(json.dumps(dict(status=report['status'],summary=ref(path),
                          r_star_upper=report['horizontal_radius_upper']['upper'],
                          Z_upper=report['absolute_height_upper']['upper'],
                          absolute_tail_third_flux_upper=report['two_reflected_tail_complex_third_flux_absolute_upper']['upper'])),flush=True)


if __name__=='__main__':main()
