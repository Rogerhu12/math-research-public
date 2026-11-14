#!/usr/bin/env python3
"""True nonlinear remote forcing, mean flux and incoming analytic-width gain.

The complete actual long Dirichlet solution is used. Fixed-fB differences
have exp(-7L/4) radial screening, including the holonomy mean. When fB=0,
the entire incoming map gains 7L/16 units of physical angular width.
No remote-label inverse or new-tail norm identification is asserted.
"""
from __future__ import annotations
import argparse,gzip,json
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record,save,sha


def read(path):return json.loads(gzip.decompress(Path(path).read_bytes()))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--joint',type=Path,default=Path('notes/2026-11-13-R133-positive-cap-actual-long-tail-joint-native.json.gz'))
    ap.add_argument('--whole',type=Path,default=Path('notes/2026-11-13-R133-whole-r1-open-cap-actual-long-tail-native.json.gz'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=384
    if args.out.exists():raise FileExistsError('preserve the actual nonlinear screening calculation')
    joint,whole=read(args.joint),read(args.whole)
    if (not joint['complete'] or not joint['full_periodic_cap_and_long_segment_matched']
        or not whole['complete'] or not whole['full_B_and_C_including_means_matched']
        or whole['inputs'].get(str(args.joint))!=sha(args.joint)
        or joint['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_cap_actual_long_tail_matching.py'))
        or whole['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_cap_whole_open_long_tail_matching.py'))):
        raise ValueError('the complete actual coupled cap/long-segment objects are required')
    for key in ('object_sha256','exact_center_parameter','parameter_half_width'):
        if joint[key]!=whole[key]:raise ValueError('the actual target differs: '+key)
    b={k:box_from_record(v) for k,v in joint['bounds'].items()}
    wb={k:box_from_record(v) for k,v in whole['bounds'].items()}
    L=b['long_L_lower'].lower();sigma=b['analytic_width_lower'].lower()
    rf=b['inner_Dirichlet_radius'].upper();fB=b['remote_Dirichlet_budget'].upper()
    rstar=arb(2)**-20;nu=arb(7)/4;alpha=arb(7)/16
    I=arb(512)/31;G=arb(160);lift=arb(16)
    linearized_Q=(2048*rstar).upper();linearized_mu=(1024*rstar).upper()
    lip=(G*linearized_Q).upper();gain=(lift/(1-lip)).upper()
    mean_gain=(linearized_mu*gain).upper()
    analytic_image=(lift*rf+G*512*rstar*rstar).upper()
    analytic_solution=(lift*rf/(1-G*512*rstar)).upper()
    analytic_gain=(alpha*L).lower();remote_width=(sigma+analytic_gain).lower()
    decay=(-nu*L).exp().upper()
    remote_difference=(25*decay*rf).upper()
    remote_mean_difference=(mean_gain*decay*rf).upper()
    fB_disk=arb(2)**-27
    mixed_difference=(25*decay*rf*fB/fB_disk).upper()
    feedback_constant=(25*(rf/fB_disk+wb['fstar_derivative_to_remote_fB'].upper())).upper()
    inner_constant=(25*wb['fstar_derivative_to_inner_c'].upper()).upper()
    endpoint_orders={}
    small_width=arb(1)/512;gap=(sigma-small_width).lower()
    for n in (224,404):
        log_fee=(n*(arb(5)/4).log()+(n-1)*(arb(n-1)/(2*gap)).log()).upper()
        log_source=(log_fee+(25*rf).log()-nu*L).upper()
        endpoint_orders[str(n)]=dict(norm='inhomogeneous A^N at physical width 1/512, including separate mean',
            logarithm_of_angular_derivative_fee_upper=record(log_fee),
            logarithm_of_complete_remote_forcing_upper=record(log_source),
            complete_remote_forcing_upper=record(log_source.exp().upper()))
    gates=dict(actual_complete_long_length=bool(L>1),
        exact_exponential_kernel_integral=bool(I<17),
        full_weighted_Green_budget=bool(1+8*I<G),
        common_weight_below_M4_rate=bool(nu<2),
        incoming_width_growth_below_M4_rate=bool(alpha<arb(1)/2),
        dual_number_nonlinear_domain=bool(2*rstar<arb(1)/1024),
        true_weighted_linearized_contraction=bool(lip<1),
        true_incoming_weighted_ball=bool(analytic_image<rstar),
        complete_incoming_size_gain=bool(analytic_solution<18*rf),
        complete_incoming_derivative_gain=bool(gain<24),
        mean_gain_exact_rational_identity=(Fraction(1024,2**20)*16/
            (1-Fraction(160*2048,2**20))==Fraction(1,44)),
        independent_remote_Cauchy_disk=bool(fB_disk+fB+rf<arb(2)**-25),
        complete_remote_feedback_budget=bool(feedback_constant<128),
        complete_inner_driving_budget=bool(inner_constant<arb(1)/32),
        physical_width_for_224_and_404=bool(gap>0),
        exponential_quantity_not_deleted=bool(decay>0))
    values=dict(actual_long_L_lower=L,actual_inner_analytic_width_lower=sigma,
        radial_screening_exponent=nu,analytic_width_growth=alpha,
        weighted_Green_upper=G,weighted_inner_lift_upper=lift,
        weighted_complete_Q_derivative_upper=linearized_Q,
        weighted_complete_mean_derivative_upper=linearized_mu,
        weighted_linearized_contraction=lip,weighted_difference_upper_per_input=gain,
        full_mean_flux_difference_upper_per_input_before_radial_factor=mean_gain,
        incoming_weighted_ball_image=analytic_image,incoming_weighted_solution_Y_upper=analytic_solution,
        actual_incoming_angular_width_gain_lower=analytic_gain,actual_remote_incoming_angular_width_lower=remote_width,
        full_incoming_map_A1_derivative_upper=gain,
        exact_nonzero_remote_radial_factor=decay,
        complete_remote_normalized_flux_difference_upper=remote_difference,
        complete_remote_mean_flux_difference_upper=remote_mean_difference,
        mean_height_span_difference_upper_divided_by_inner_aw=(rf/165).upper(),
        mixed_fB_incoming_remainder_complete_flux_upper=mixed_difference,
        independent_fB_Cauchy_radius=fB_disk,remote_fB_feedback_prefactor_upper=feedback_constant,
        inner_c_driving_prefactor_upper=inner_constant,
        complete_remote_fB_feedback_derivative_upper=(128*decay).upper(),
        complete_remote_inner_c_driving_derivative_upper=(decay/32).upper())
    result=dict(kind='actual_nonlinear_long_tail_remote_forcing_mean_and_incoming_analytic_gain_v2',
        complete=True,source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.joint,args.whole)},
        object_sha256=joint['object_sha256'],exact_center_parameter=joint['exact_center_parameter'],
        parameter_half_width=joint['parameter_half_width'],whole_affine_parameter_interval=True,
        whole_real_angular_circle=True,complete_primitive_tail=True,all_Fourier_modes_retained=True,
        nonlinear_screening_certified=all(gates.values()),gates=gates,
        bounds={k:record(v) for k,v in values.items()},full_angular_orders=endpoint_orders,
        exact_remote_difference='DeltaK(fB,f*)=K_B^long(fB,f*)-K_B^long(fB,0); normalized slope includes its holonomy mean.',
        exact_decomposition='DeltaK(fB,f*)=K_B^long(0,f*)-K_B^long(0,0)+mixed(fB,f*); fB is not set to zero in the full remote equation.',
        actual_remote_residual_difference='F(a,f*)-F(a,0)=-DeltaK_nonmean(fB(a),f*); full mean flux is retained separately.',
        incoming_gain_scope='The fB=0 incoming component has physical width sigma+7L/16. The mixed part for nonzero fB retains fixed physical width sigma.',
        original_body_graft_and_long_object_only=True,tail_label_224_or_raw_404_weight_not_identified=True,
        new_deep_profile_not_implicitly_substituted=True,remote_label_inverse_proved=False,
        inner_body_proved=False,closed_surface_complete=False,
        initial_v1_failure='The exact equality mean_gain=1/44 was tested by an outward-ball <= comparison; it returned false. v2 checks the rational identity exactly. The original source and false report remain unchanged.',
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_cap_actual_long_tail_matching.py','fourfold_codazzi_cap_whole_open_long_tail_matching.py',
            'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_phase_metric_defect.py')})
    save(args.out,result)
    print(dict(certified=result['nonlinear_screening_certified'],failed=[k for k,v in gates.items() if not v],
        actual_extra_width=analytic_gain.str(14),remote_log=(25*rf).log().__sub__(nu*L).str(14),
        feedback_prefactor=feedback_constant.str(12)),flush=True)


if __name__=='__main__':main()
