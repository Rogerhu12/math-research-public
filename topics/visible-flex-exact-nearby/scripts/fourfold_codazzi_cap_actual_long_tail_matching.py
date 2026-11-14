#!/usr/bin/env python3
"""Complete positive-cap / actual long-tail curvature matching budgets.

Consumes the real whole-parameter analytic screening. The nonlinear long
Dirichlet map is inverted in its nonmean C output, retaining the other-end
Dirichlet input and its exponentially small but nonzero reflection. A second
full-Fourier fixed point matches B and both means at the actual r=25/8 cut.
The remote label residual is explicitly not solved here.
"""
from __future__ import annotations
import argparse,gzip,json
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha


def read(p):return json.loads(gzip.decompress(Path(p).read_bytes()))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--screening',type=Path,default=Path('notes/2026-11-13-R133-cap-analytic-screening-r15-mu3halves-native.json.gz'))
    ap.add_argument('--reference',type=Path,default=Path('notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=384
    if args.out.exists():raise FileExistsError('preserve each actual tail-matching calculation')
    screen,ref=read(args.screening),read(args.reference)
    if (screen['kind']!='actual_same_cap_radial_decay_and_growing_full_analytic_width'
        or not screen['complete'] or not screen['curvature_screening_certified']
        or not screen['same_original_branch_identified'] or not screen['weighted_rates_positive']
        or screen['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_cap_radial_analytic_screening.py'))
        or screen['inputs'].get(str(args.reference))!=sha(args.reference)
        or not ref['complete'] or not ref['cap_linear_reference_certified']):
        raise ValueError('the actual full cap screening and reference identities are required')
    for key in ('object_sha256','exact_center_parameter','parameter_half_width'):
        if screen[key]!=ref[key]:raise ValueError('different true target: '+key)
    if not all(screen[k] for k in ('whole_affine_parameter_interval','whole_real_angular_circle','complete_primitive_tail','all_Fourier_modes_retained')):
        raise ValueError('the complete actual scope is missing')
    for p,h in screen['inputs'].items():
        if sha(p)!=h:raise ValueError('screening input changed: '+p)
    if screen['selected_outer_inputs']!=dict(d_nonzero=0,B_mean=0,c_mean=0):
        raise ValueError('the base branch must have exactly the specified zero outer data')
    c={k:box_from_record(v) for k,v in screen['weighted_constants'].items()}
    sb={k:box_from_record(v) for k,v in screen['bounds'].items()}
    cap_radius=box_from_record(screen['weighted_ball']['radius']).lower()
    cap_image=box_from_record(screen['weighted_ball']['image']).upper()
    cap_lip=box_from_record(screen['weighted_ball']['contraction']).upper()
    first=ref['rows'][screen['rows'][0]['native_index']]['coefficients']
    aL=box_from_record(first['a']);entry=ref['true_R74_entrance']
    aR=box_from_record(entry['radius']);omega=box_from_record(entry['normalized_omega'])
    chi=1/(4*omega);w=aR*chi;E=1+w*w
    mu=exact_arb(Fraction(screen['exact_radial_power']));tau=exact_arb(Fraction(screen['exact_width_growth']))
    Wmin=(mu*(aR.lower()/aL.upper()).log()).exp().lower()
    sigma_min=sb['right_analytic_width_lower'].lower()
    sigma_max=(-tau*(aR.lower()/aL.upper()).log()).upper()
    long_B=arb(2)**24-arb(25)/8
    long_L=(omega.lower()*long_B).lower()
    actual_fee=box_from_record(ref['Jacobi']['full_frequency_interval']['complete_true_tail_fee']).upper()
    q_graph_fee=(actual_fee+8*(-8*long_L).exp()).upper()
    reflection=(2*(-6*long_L).exp()).upper()
    rz=arb(1)/10**9;rf=arb(1)/10**8;fB=arb(2)**-60;F=(rf+fB).upper()
    # The proof gives H<=6F; nonmean C, reduced B and mean C remainders
    # have constants 2^12, 2^14 and 2^11, respectively.
    RC=arb(2)**12;RD=arb(2)**14;RM=arb(2)**11
    inverse_norm=arb(9)
    inv_lip=(inverse_norm*4*RC*F).upper()
    inv_image=(inverse_norm*rz+reflection*fB+inverse_norm*RC*F*F).upper()
    derivative_f=(inverse_norm/(1-inv_lip)).upper()
    d_bound=(q_graph_fee*rz+reflection*fB+RD*F*F).upper()
    mean_bound=(RM*F*F).upper()
    d_derivative=(q_graph_fee+4*RD*F*derivative_f).upper()
    mean_derivative=(4*RM*F*derivative_f).upper()
    H_D=c['boundary_D'].upper()
    cap_image_with_tail=(cap_image+(H_D*d_bound+mean_bound)/Wmin).upper()
    base_right=sb['right_analytic_B_plus_c_A0_upper'].upper()
    joint_image=(base_right+(H_D*d_bound+mean_bound)/(1-cap_lip)).upper()
    joint_lip=((H_D*d_derivative+mean_derivative)/(1-cap_lip)).upper()
    # Full raw height/slopes and their independent mean height output.
    H=(6*F).upper()
    K_nonmean=((arb(257)/1020)*rf+reflection*fB+256*H*H).upper()
    K_mean=(256*H*H).upper()
    K_total=(K_nonmean+K_mean).upper()
    height_nonmean=(aR.upper()*w.upper()*rf/16).upper()
    va=(w.upper()*K_total).upper()
    mean_height=(128*aR.upper()*w.upper()*H*H).upper()
    gates=dict(physical_chi_lower=bool(chi.lower()>arb(1)/6),
        physical_chi_sqrtE_upper=bool((chi*E.sqrt()).upper()<arb(1)/5),
        physical_w_upper=bool(w.upper()<arb(1)/800000),true_length=bool(long_L>1),
        doubled_holomorphic_boundary_ball=bool(2*F<arb(2)**-25),
        improved_lift_constant=bool((arb(64)/63)*5<6),
        inner_Green_slope_constant=bool(arb(1)/(1-arb(2)**-8)<2),
        nonmean_C_remainder_constant=bool(64*36<RC),
        reduced_B_remainder_constant=bool(384*36<RD),
        mean_C_remainder_constant=bool(46*36<RM),
        all_mode_C_inverse=bool((arb(1020)/763)*6<inverse_norm),
        nonzero_reflection_retained=bool(reflection>0 and q_graph_fee>0),
        inverse_contraction=bool(inv_lip<1),inverse_strict_ball=bool(inv_image<rf),
        original_cap_contraction=bool(cap_lip<1),cap_with_tail_strict_ball=bool(cap_image_with_tail<cap_radius),
        joint_right_trace_contraction=bool(joint_lip<1),joint_right_trace_strict_ball=bool(joint_image<rz),
        positive_common_analytic_width=bool(sigma_min>arb(1)/64),
        all_true_endpoints_covered=screen['exact_requested_interval']==['3/2','25/8'])
    values=dict(inner_nonzero_C_radius=rz,inner_Dirichlet_radius=rf,remote_Dirichlet_budget=fB,
        total_boundary_radius=F,long_L_lower=long_L,full_true_Jacobi_fee=actual_fee,
        finite_long_reflection_upper=reflection,complete_linear_graph_difference_upper=q_graph_fee,
        C_Dirichlet_inverse_upper=inverse_norm,C_inverse_contraction=inv_lip,C_inverse_image=inv_image,
        C_inverse_image_margin=(rf-inv_image).lower(),C_to_Dirichlet_derivative_upper=derivative_f,
        nonlinear_outer_d_upper=d_bound,nonlinear_outer_c_mean_upper=mean_bound,
        outer_d_derivative_upper=d_derivative,outer_c_mean_derivative_upper=mean_derivative,
        complete_radial_weight_lower=Wmin,analytic_width_lower=sigma_min,analytic_width_upper=sigma_max,
        original_cap_radius=cap_radius,original_cap_contraction=cap_lip,
        cap_image_with_true_tail_ports=cap_image_with_tail,
        cap_image_margin=(cap_radius-cap_image_with_tail).lower(),
        base_true_analytic_C_trace_upper=base_right,joint_right_trace_image=joint_image,
        joint_right_trace_image_margin=(rz-joint_image).lower(),joint_right_trace_contraction=joint_lip,
        joint_contraction_margin=(1-joint_lip).lower(),actual_long_solution_Y_upper=H,
        actual_nonmean_slope_K_upper=K_nonmean,actual_mean_slope_K_upper=K_mean,
        actual_full_slope_K_upper=K_total,physical_nonmean_height_upper=height_nonmean,
        physical_v_a_upper=va,independent_mean_height_difference_upper=mean_height)
    report=dict(kind='actual_full_Fourier_positive_cap_and_long_Dirichlet_tail_joint_curvature_match',
        complete=True,source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.screening,args.reference)},
        object_sha256=ref['object_sha256'],exact_center_parameter=ref['exact_center_parameter'],
        parameter_half_width=ref['parameter_half_width'],whole_affine_parameter_interval=True,
        whole_real_angular_circle=True,complete_primitive_tail=True,all_Fourier_modes_retained=True,
        shared_material_angle='original physical theta; no grounded or return-angle replacement',
        full_periodic_cap_and_long_segment_matched=all(gates.values()),
        exact_cap_interval=['3/2','25/8'],actual_long_coordinate='u=4c0(r-25/8), 0<=u<=2^24-25/8',
        independent_remote_Dirichlet_data_retained=True,remote_data_requirement='real even fourfold fB in homogeneous analytic A2 at the actual endpoint width, norm <=2^-60',
        inner_data_requirement='real even fourfold c_nonzero(3/2) with the actual certified A0 budget; A2 regularity retained for C2 up to that boundary',
        exact_B_mean_by_common_reflection=True,true_C_mean_output_matched=True,
        true_R74_linear_fee_and_finite_long_reflection_retained=True,
        raw_height_and_slope_including_mean_retained=True,independent_mean_height_translation_retained=True,
        gates=gates,bounds={k:record(v) for k,v in values.items()},
        remote_label_residual_matched=False,full_body_matched=False,closed_surface_complete=False,
        held_displacement_certified=False,global_reach_certified=False,
        residual_still_required='F(a,f*)=k_B(a)+C_L f_B(a)-S_L f*-E_D(f_B(a),f*)=0, with the actual label-generated data and mean height.',
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_cap_radial_analytic_screening.py','fourfold_codazzi_rotational_cap_jacobi.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_metric_defect.py')})
    save(args.out,report)
    print(dict(matched=report['full_periodic_cap_and_long_segment_matched'],
        failed=[k for k,v in gates.items() if not v],inverse_lip=inv_lip.str(13),
        cap_image=cap_image_with_tail.str(13),joint_image=joint_image.str(13),
        joint_lip=joint_lip.str(13),raw_height=height_nonmean.str(13)),flush=True)


if __name__=='__main__':main()
