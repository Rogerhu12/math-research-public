#!/usr/bin/env python3
"""Pull the genuine periodic long-tail match back to the whole open r=1 cap.

The moving r=3/2 inner trace is paid, not silently held fixed. Full physical
outer B/C means, analytic-to-A2 data and the new inner derivative columns are
retained. The remote nonlinear label residual and inner body remain open.
"""
from __future__ import annotations
import argparse,gzip,json
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record,save,sha


def read(p):return json.loads(gzip.decompress(Path(p).read_bytes()))


def vals(d):return {k:box_from_record(v) for k,v in d.items()}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--matched',type=Path,default=Path('notes/2026-11-13-R133-positive-cap-actual-long-tail-joint-native.json.gz'))
    ap.add_argument('--screening',type=Path,default=Path('notes/2026-11-13-R133-cap-analytic-screening-r15-mu3halves-native.json.gz'))
    ap.add_argument('--ports',type=Path,default=Path('notes/2026-11-13-R133-open-curvature-ports-r1-v2-native.json.gz'))
    ap.add_argument('--M128',type=Path,default=Path('notes/2026-11-13-R133-M128-actual-inner-cap-trace-native.json.gz'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=384
    matched,screen,ports,m128=(read(p) for p in (args.matched,args.screening,args.ports,args.M128))
    if args.out.exists():raise FileExistsError('preserve each whole-cap matching result')
    if (not matched['complete'] or not matched['full_periodic_cap_and_long_segment_matched']
        or matched['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_cap_actual_long_tail_matching.py'))
        or matched['inputs'].get(str(args.screening))!=sha(args.screening)
        or not screen['curvature_screening_certified'] or not screen['same_original_branch_identified']
        or not ports['complete'] or not ports['full_open_port_ball_certified']
        or not ports['nonzero_curvature_trace_derivative_invertible']
        or ports['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_cap_open_curvature_ports_v2.py'))
        or ports['exact_requested_interval']!=['1','25/8']):
        raise ValueError('the same true matched long segment and open whole cap are required')
    for doc in (screen,ports,m128):
        for key in ('object_sha256','exact_center_parameter','parameter_half_width'):
            if doc[key]!=matched[key]:raise ValueError('a true target identity differs: '+key)
    for name,h in ports['inputs'].items():
        if sha(name)!=h:raise ValueError('actual open-cap input changed: '+name)
        if name in screen['inputs'] and screen['inputs'][name]!=h:
            raise ValueError('the suffix is not from the same complete cap')
    if (not m128['complete_input_is_inside_open_cap_graph']
        or m128['inputs'].get(str(args.ports))!=sha(args.ports)
        or m128['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_cap_M128_inner_trace.py'))):
        raise ValueError('the full actual M128 trace identity changed')
    b=vals(matched['bounds']);s=vals(screen['bounds']);wc=vals(screen['weighted_constants'])
    op=vals(ports['bounds']);sol=vals(ports['complete_solution_derivative_columns'])
    bn=vals(ports['nonlinear_d_left_derivative_remainder_columns'])
    mn=vals(ports['nonlinear_c_mean_left_derivative_remainder_columns'])
    rho_w=b['original_cap_radius'].lower();lw=b['original_cap_contraction'].upper()
    Wmax=s['right_common_radial_weight_upper'].upper();Wmin=b['complete_radial_weight_lower'].lower()
    HD=wc['boundary_D'].upper();HC=wc['boundary_C'].upper()
    cap_rho=op['radius'].upper();old_e=s['original_proved_correction_X0'].upper()
    extra_inner=max(arb(0),cap_rho-old_e).upper()
    new_inner=(s['actual_inner_c_A0'].upper()+extra_inner).upper()
    base_image=(box_from_record(screen['weighted_ball']['image']).upper()+HC*extra_inner).upper()
    ed=b['nonlinear_outer_d_upper'].upper();e0=b['nonlinear_outer_c_mean_upper'].upper()
    Ld=b['outer_d_derivative_upper'].upper();L0=b['outer_c_mean_derivative_upper'].upper()
    SD=sol['outer_d_nonzero'].upper();SM=sol['outer_c_mean'].upper();SC=sol['inner_c_nonzero'].upper()
    source_d=(HD+Wmax*HC*SD).upper();source_mean=(1+Wmax*HC*SM).upper()
    joint_image=(b['base_true_analytic_C_trace_upper'].upper()+(source_d*ed+source_mean*e0)/(1-lw)).upper()
    joint_lip=((source_d*Ld+source_mean*L0)/(1-lw)).upper()
    image_with_tail=(base_image+(HD*ed+e0)/Wmin).upper()
    GZ_inner=(Wmax*HC*SC/((1-lw)*(1-joint_lip))).upper()
    d_inner=(Ld*GZ_inner).upper();mean_inner=(L0*GZ_inner).upper()
    extra_B=((1+bn['outer_d_nonzero'].upper())*d_inner+bn['outer_c_mean'].upper()*mean_inner).upper()
    extra_mean=(mn['outer_d_nonzero'].upper()*d_inner+
        (op['mean_c_linear_transfer_upper'].upper()+mn['outer_c_mean'].upper())*mean_inner).upper()
    complete_B=(op['inner_nonzero_derivative_minus_negative_q'].upper()+extra_B).upper()
    qm=op['inner_q_lower'].lower()
    inverse=(1/(qm-complete_B)).upper() if qm>complete_B else None
    complete_mean=(mn['inner_c_nonzero'].upper()+extra_mean).upper()
    # Explicit remote-input columns, still in the original physical angle.
    F=b['total_boundary_radius'].upper();lf=b['C_inverse_contraction'].upper()
    refl=b['finite_long_reflection_upper'].upper();Jf=b['C_to_Dirichlet_derivative_upper'].upper()
    f_remote_direct=((refl+9*4*(arb(2)**12)*F)/(1-lf)).upper()
    d_remote_direct=(refl+4*(arb(2)**14)*F*(1+f_remote_direct)).upper()
    mean_remote_direct=(4*(arb(2)**11)*F*(1+f_remote_direct)).upper()
    Z_remote=((source_d*d_remote_direct+source_mean*mean_remote_direct)/((1-lw)*(1-joint_lip))).upper()
    d_remote=(d_remote_direct+Ld*Z_remote).upper()
    mean_remote=(mean_remote_direct+L0*Z_remote).upper()
    B_remote=((1+bn['outer_d_nonzero'].upper())*d_remote+bn['outer_c_mean'].upper()*mean_remote).upper()
    cmean_remote=(mn['outer_d_nonzero'].upper()*d_remote+
        (op['mean_c_linear_transfer_upper'].upper()+mn['outer_c_mean'].upper())*mean_remote).upper()
    dA2=(1600*ed).upper()
    gates=dict(original_open_port_radius=bool(op['open_image_margin'].lower()>0),
        actual_width_for_full_inhomogeneous_A2=bool(b['analytic_width_lower'].lower()>arb(1)/16),
        true_outer_d_in_old_complete_A2_budget=bool(dA2<arb(1)/10**8),
        true_outer_mean_in_old_budget=bool(e0<arb(1)/10**8),
        modified_suffix_strict_ball=bool(image_with_tail<rho_w),
        whole_cap_joint_strict_ball=bool(joint_image<b['inner_nonzero_C_radius'].lower()),
        whole_cap_joint_contraction=bool(joint_lip<1),
        complete_inner_trace_derivative_invertible=bool(qm>complete_B),
        complete_M128_trace_already_inside_original_open_graph=m128['complete_input_is_inside_open_cap_graph'])
    values=dict(whole_cap_radius=cap_rho,additional_true_suffix_inner_budget=extra_inner,
        complete_actual_suffix_inner_budget=new_inner,modified_suffix_base_image=base_image,
        modified_suffix_image_with_true_tail=image_with_tail,
        modified_suffix_image_margin=(rho_w-image_with_tail).lower(),
        true_outer_d_inhomogeneous_A2_upper=dA2,
        complete_outer_d_to_right_trace_source=source_d,
        complete_outer_mean_to_right_trace_source=source_mean,
        whole_joint_right_trace_image=joint_image,whole_joint_right_trace_contraction=joint_lip,
        right_trace_derivative_to_inner_c=GZ_inner,
        actual_outer_d_derivative_to_inner_c=d_inner,actual_outer_cmean_derivative_to_inner_c=mean_inner,
        additional_inner_B_derivative_from_true_tail=extra_B,
        additional_inner_cmean_derivative_from_true_tail=extra_mean,
        complete_inner_B_derivative_minus_negative_q=complete_B,
        complete_inner_cmean_derivative=complete_mean,
        fstar_derivative_to_inner_c=(Jf*GZ_inner).upper(),
        right_trace_derivative_to_remote_fB=Z_remote,
        fstar_derivative_to_remote_fB=(f_remote_direct+Jf*Z_remote).upper(),
        inner_B_derivative_to_remote_fB=B_remote,inner_cmean_derivative_to_remote_fB=cmean_remote)
    report=dict(kind='actual_whole_open_r1_cap_matched_to_periodic_nonlinear_long_tail',complete=True,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.matched,args.screening,args.ports,args.M128)},
        object_sha256=matched['object_sha256'],exact_center_parameter=matched['exact_center_parameter'],
        parameter_half_width=matched['parameter_half_width'],whole_affine_parameter_interval=True,
        whole_real_angular_circle=True,complete_primitive_tail=True,all_Fourier_modes_retained=True,
        exact_positive_cap_interval=['1','25/8'],entire_original_open_inner_c_A0_neighborhood=ports['inner_c_nonzero_variation_A0'],
        actual_suffix_inner_trace_dependence_paid=True,full_B_and_C_including_means_matched=all(gates.values()),
        periodic_frame_obtained_from_actual_tail=True,reflection_keeps_B_mean_exactly_zero=True,
        gates=gates,bounds={k:record(v) for k,v in values.items()},
        complete_inner_nonzero_B_trace_inverse=record(inverse) if inverse is not None else None,
        complete_M128_input_consumed=True,M128_boundaries=m128['bounds'],
        original_M128_B_and_mean_matching_residuals_remain_bounds_for_this_true_periodic_cap=True,
        remote_fB_parameter_retained=True,remote_label_equation_solved=False,inner_body_solved=False,
        closed_surface_complete=False,global_embedding_or_reach_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_cap_actual_long_tail_matching.py','fourfold_codazzi_cap_radial_analytic_screening.py',
            'fourfold_codazzi_cap_open_curvature_ports_v2.py','fourfold_codazzi_cap_M128_inner_trace.py',
            'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_phase_metric_defect.py')})
    save(args.out,report)
    print(dict(matched=report['full_B_and_C_including_means_matched'],failed=[k for k,v in gates.items() if not v],
        suffix_image=image_with_tail.str(13),joint_lip=joint_lip.str(13),
        added_B_derivative=extra_B.str(13),complete_q_remainder=complete_B.str(13),
        inverse=None if inverse is None else inverse.str(13)),flush=True)


if __name__=='__main__':main()
