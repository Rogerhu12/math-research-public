#!/usr/bin/env python3
"""True R=25/8 regular q proposal and complete nonlinear long-end ports.

The nominal vector is the same exact leading q_* at every physical mode.
It is not labelled as the exact infinite-tail multiplier. The directed
report retains every nonzero tail fee, the full parameter interval, both
nonlinear curvature ports, the independent far Dirichlet data and height.
"""
from __future__ import annotations
import argparse,gzip,json,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha


def read(path):return json.loads(gzip.decompress(Path(path).read_bytes()))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--reference',type=Path,default=Path('notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz'))
    ap.add_argument('--long-proof',type=Path,default=Path('results/R133-supplement-actual-positive-cap-and-periodic-long-tail-matching.md'))
    ap.add_argument('--tail-proof',type=Path,default=Path('results/R119-supplement-stronger-tail-raw-labels-sources-and-regular-boundary.md'))
    ap.add_argument('--modes',type=int,default=256)
    ap.add_argument('--C-radius',type=Fraction,default=Fraction(1,10**10))
    ap.add_argument('--far-Dirichlet-radius',type=Fraction,default=Fraction(1,2**60))
    ap.add_argument('--angular-width',type=Fraction,default=Fraction(0))
    ap.add_argument('--floating',type=Path,required=True);ap.add_argument('--native',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320;ctx.cap=6
    if args.floating.exists() or args.native.exists():raise FileExistsError('preserve each actual endpoint report')
    if (args.modes<1 or not 0<args.C_radius<=Fraction(1,10**9)
        or not 0<=args.far_Dirichlet_radius<=Fraction(1,2**60)
        or not 0<=args.angular_width<=Fraction(1,8)):
        raise ValueError('outside the proved complete periodic-long domains')
    ref=read(args.reference)
    if (not ref['complete'] or not ref['cap_linear_reference_certified']
        or not ref['whole_affine_parameter_interval'] or not ref['complete_primitive_tail']
        or ref['object_sha256']!=sha(args.object)
        or ref['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_rotational_cap_jacobi_v2.py'))):
        raise ValueError('the actual complete intrinsic endpoint reference is required')
    entry=ref['true_R74_entrance']
    if entry['physical_cut']!='25/8':raise ValueError('wrong physical endpoint')
    radius=box_from_record(entry['radius']);omega=box_from_record(entry['normalized_omega'])
    if not (radius>0 and radius<arb(7)/10**6 and omega>arb(7)/5 and omega<arb(3)/2):
        raise ValueError('the true endpoint is outside the proved regular regime')
    w=radius/(4*omega);Ea=1+w*w;chi=1/(4*omega);base=1/Ea.sqrt()
    length=omega*exact_arb(Fraction(2**24)-Fraction(25,8));Lmin=length.lower()
    # The fourth mode is exact. All other allowed frequencies have M>=8.
    common_fee=(arb(2)**42*(-16*Lmin).exp()).upper()
    lower=(base.lower()-common_fee).lower();upper=(base.upper()+common_fee).upper()
    if not 0<lower<=upper<1:raise ValueError('the actual all-mode interval (0,1) is unresolved')
    proposed=float(base.mid());proposal=arb(proposed)
    model_fee=abs(base-proposal).upper();frequencies=[4*j for j in range(1,args.modes+1)]
    modes=[]
    for M in frequencies:
        tail_fee=arb(0) if M==4 else (arb(2)**42*(-2*M*Lmin).exp()).upper()
        if M!=4 and not tail_fee>0:raise ValueError('the true nonzero tail fee was lost')
        modes.append(dict(physical_frequency=M,nominal_dyadic_q=proposed,
            true_q_lower=record((base.lower()-tail_fee).lower()),
            true_q_upper=record((base.upper()+tail_fee).upper()),
            whole_parameter_nominal_q_error=record((model_fee+tail_fee).upper()),
            true_nonzero_regular_tail_fee=record(tail_fee),fourth_mode_tail_fee_exactly_zero=M==4))
    rZ=exact_arb(args.C_radius);rB=exact_arb(args.far_Dirichlet_radius)
    rf=(10*(rZ+rB)).upper();F=(rf+rB).upper();H=(6*F).upper()
    reflection=(2*(-6*Lmin).exp()).upper()
    finite_ratio=(8*(-8*Lmin).exp()).upper();epsilon_q=(common_fee+finite_ratio).upper()
    Cimage=(9*rZ+reflection*rB+9*arb(2)**12*F*F).upper()
    Clip=(9*4*arb(2)**12*F).upper()
    if not (2*F<arb(2)**-25 and H<arb(2)**-20 and Cimage<rf and Clip<1):
        raise ValueError('the actual nonlinear C-to-Dirichlet contraction is unresolved')
    Jf=(9/(1-Clip)).upper()
    d=(epsilon_q*rZ+reflection*rB+arb(2)**14*F*F).upper()
    d_nominal=(d+(model_fee+common_fee)*rZ).upper()
    mean=(arb(2)**11*F*F).upper()
    Ld=(epsilon_q+4*arb(2)**14*F*Jf).upper()
    Lmean=(4*arb(2)**11*F*Jf).upper()
    mu=(256*H*H).upper()
    Kne=(arb(257)/1020*rf+reflection*rB+256*H*H).upper()
    Kfull=(Kne+mu).upper()
    raw_height=(radius*w*rf/16).upper();raw_a_slope=(w*Kfull).upper()
    raw_mean_difference=(radius*w*mu/2).upper()
    bounds=dict(actual_aR=radius,actual_omega=omega,actual_w=w,actual_E_in_a_coordinate=Ea,
        actual_C_reference=-chi/Ea.sqrt(),actual_qstar=base,long_L=length,
        all_nonmean_true_q_lower=lower,all_nonmean_true_q_upper=upper,
        all_nonmean_true_q_abs_upper=arb(1),nominal_dyadic_q_error_full_parameter=model_fee,
        all_m_greater_than_four_true_tail_fee=common_fee,
        complete_finite_long_q_ratio_difference=finite_ratio,
        complete_true_q_to_periodic_long_linear_difference=epsilon_q,
        far_Dirichlet_reflection=reflection,physical_C_nonmean_radius=rZ,
        independent_far_Dirichlet_radius=rB,actual_inner_Dirichlet_radius=rf,
        total_boundary_radius=F,long_solution_Y_upper=H,
        C_to_Dirichlet_image=Cimage,C_to_Dirichlet_image_margin=(rf-Cimage).lower(),
        C_to_Dirichlet_contraction=Clip,C_to_Dirichlet_derivative=Jf,
        exact_regular_q_nonlinear_nonmean_d_upper=d,
        nominal_q_vector_complete_nonmean_d_upper=d_nominal,
        true_C_mean_output_upper=mean,true_B_mean_output=arb(0),
        true_nonmean_d_derivative=Ld,true_C_mean_derivative=Lmean,
        full_holonomy_mean_mu_upper=mu,full_slope_K_upper=Kfull,
        raw_nonmean_height_upper=raw_height,raw_a_derivative_upper=raw_a_slope,
        independent_mean_height_difference_upper=raw_mean_difference)
    inputs={str(p):sha(p) for p in (args.object,args.reference,args.long_proof,args.tail_proof)}
    floating=dict(kind='floating_actual_R74_regular_endpoint_q_vector',complete=True,success=True,
        certified=False,source_sha256=sha(__file__),object_sha256=sha(args.object),
        reference_sha256=sha(args.reference),left='25/8',right='25/8',right_boundary='25/8',
        modes=args.modes,physical_frequencies=frequencies,q_values=[proposed]*args.modes,
        all_nonmean_q_abs_upper=1.0,actual_omega_center=float(omega.mid()),actual_aR_center=float(radius.mid()),
        exact_center_parameter=ref['exact_center_parameter'],parameter_half_width=ref['parameter_half_width'],
        physical_material_angle='theta',nominal_vector_is_not_exact_true_tail_multiplier=True,
        qstar_formula='(1+(a_R/(4*omega))^2)^(-1/2), no extra frequency in this denominator',
        actual_frequency_dependence_retained_by_separate_nonzero_native_tail_fees=True,
        full_native_report=str(args.native),old_r15_cut_vector_not_reused=True)
    args.floating.write_text(json.dumps(floating,indent=2,allow_nan=False)+'\n')
    doc=dict(kind='actual_R25over8_regular_vector_and_complete_nonlinear_long_ports',complete=True,
        source_sha256=sha(__file__),inputs={**inputs,str(args.floating):sha(args.floating)},
        object_sha256=sha(args.object),exact_center_parameter=ref['exact_center_parameter'],
        parameter_half_width=ref['parameter_half_width'],whole_affine_parameter_interval=True,
        whole_real_angular_circle=True,complete_primitive_tail=True,all_Fourier_modes_and_mean_retained=True,
        physical_cut='25/8',physical_material_angle='theta',angular_width=str(args.angular_width),
        input_C_norm='complete nonmean A0_sigma; no finite-mode truncation',
        input_Dirichlet_norm='complete nonmean dot A2_sigma with weight |m|^2; mean handled separately',
        exact_tail_identity='R119 stronger-tail raw-label/source/regular-boundary V.8-V.12: fixed Gamma, newly selected full good bump parameter, freshly stopped fourth connector',
        latest_second_negative_band_bump_not_instantiated_here=True,
        original_R74_identity_also_covered=True,compact_E_nu_support_ends_at_r018=True,
        q_identity='q_M=-lambda_M/(M*omega*sqrt(1+w_R^2)); lambda_4=-4*omega exactly',
        modes=modes,bounds={k:record(v) for k,v in bounds.items()},
        gates=dict(actual_endpoint=True,all_q_strictly_between_zero_and_one=True,
            all_nonfourth_regular_fees_strictly_positive=True,full_C_to_Dirichlet_contraction=True,
            full_periodic_long_solution=True,exact_B_mean_by_reflection=True,true_C_mean_output_retained=True,
            independent_far_Dirichlet_retained=True,independent_mean_height_retained=True,
            complete_finite_long_reflection_retained=True),
        no_candidate_C_radius_verified_by_this_script=True,
        complete_body_or_boundary_inverse_not_claimed=True,full_regular_label_residual_solved=False,
        required_far_equation='k_B(a)+C_L f_B(a)-S_L f_star-E_D(f_B(a),f_star)=0',
        raw_height='v_perp(R)=a_R*w_R*f_star; Z=Zref-v; mean height translation independent',
        raw_radial_derivative='v_r(R)=-4*c0*omega*a_R*w_R*(mu+2*f_star+h_t(L))',
        normalized_body_rows='if b,c were divided by amplitude alpha, divide these physical port remainder bounds by |alpha|',
        dependencies={'fourfold_codazzi_rotational_cap_jacobi.py':sha(Path(__file__).with_name('fourfold_codazzi_rotational_cap_jacobi.py'))},
        wall_seconds=time.monotonic()-started)
    save(args.native,doc)
    print(dict(complete=True,modes=args.modes,qstar=base.str(30),nominal_full_parameter_error=model_fee.str(20),
        nonlinear_d=d.str(20),nonlinear_Cmean=mean.str(20),C_inverse_contraction=Clip.str(20),
        files=[str(args.floating),str(args.native)],wall_seconds=doc['wall_seconds']),flush=True)


if __name__=='__main__':main()
