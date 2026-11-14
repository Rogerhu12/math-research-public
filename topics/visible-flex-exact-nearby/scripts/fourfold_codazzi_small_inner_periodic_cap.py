#!/usr/bin/env python3
"""Actual small-input open periodic cap at r=3/2, with true long-tail ports.

The input ball is independent of any old finite centre. Exact finite boundary
traces may be selected from successful or failed body diagnostics; their
finite status is preserved and never used as a PDE certificate.
"""
from __future__ import annotations
import argparse,gzip,json
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_cap_open_curvature_ports_v2 import trace,exact,dyadic
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record,save,sha


def read(path):return json.loads(gzip.decompress(Path(path).read_bytes()))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--screening',type=Path,default=Path('notes/2026-11-13-R133-cap-analytic-screening-r15-mu3halves-native.json.gz'))
    ap.add_argument('--joint',type=Path,default=Path('notes/2026-11-13-R133-positive-cap-actual-long-tail-joint-native.json.gz'))
    ap.add_argument('--candidate',type=Path,action='append',default=[])
    ap.add_argument('--floating',type=Path,action='append',default=[])
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=384
    if args.out.exists():raise FileExistsError('preserve each actual small-input cap calculation')
    if len(args.candidate)!=len(args.floating):raise ValueError('pair every finite candidate with its original diagnostic status')
    screen,joint=read(args.screening),read(args.joint)
    if (not screen['complete'] or not screen['curvature_screening_certified']
        or not screen['weighted_rates_positive'] or not joint['complete']
        or not joint['full_periodic_cap_and_long_segment_matched']
        or joint['inputs'].get(str(args.screening))!=sha(args.screening)
        or screen['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_cap_radial_analytic_screening.py'))
        or joint['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_cap_actual_long_tail_matching.py'))
        or screen['exact_requested_interval']!=['3/2','25/8']
        or screen['exact_radial_power']!='3/2' or screen['exact_width_growth']!='1/128'):
        raise ValueError('the same complete real cap kernels and long object are required')
    for key in ('object_sha256','exact_center_parameter','parameter_half_width'):
        if screen[key]!=joint[key]:raise ValueError('the true target differs: '+key)
    c={k:box_from_record(v) for k,v in screen['weighted_constants'].items()}
    s={k:box_from_record(v) for k,v in screen['bounds'].items()}
    j={k:box_from_record(v) for k,v in joint['bounds'].items()}
    HC=c['boundary_C'].upper();HD=c['boundary_D'].upper();KG=c['complete_pair_nonlinear_kernel'].upper()
    KD=c['nonlinear_D_kernel'].upper();Km=c['mean_nonlinear_kernel'].upper()
    Cstar=c['Cref_abs_lower'].lower();Lam=c['ell_upper'].upper()
    Wmin=j['complete_radial_weight_lower'].lower();Wmax=s['right_common_radial_weight_upper'].upper()
    epsilon=arb(1)/50000;rho=arb(1)/10000;rz=arb(1)/5000000000;rf=arb(1)/500000000
    fB=j['remote_Dirichlet_budget'].upper();F=(rf+fB).upper()
    RC=arb(2)**12;RD=arb(2)**14;RM=arb(2)**11
    fee=j['complete_linear_graph_difference_upper'].upper();reflection=j['finite_long_reflection_upper'].upper()
    lam_f=(9*4*RC*F).upper();image_f=(9*rz+reflection*fB+9*RC*F*F).upper()
    Jf=(9/(1-lam_f)).upper()
    ed=(fee*rz+reflection*fB+RD*F*F).upper();e0=(RM*F*F).upper()
    Ld=(fee+4*RD*F*Jf).upper();L0=(4*RM*F*Jf).upper()
    def qbound(r):return (Lam*r*r/(Cstar-r)).upper()
    def dqbound(r):return (Lam*(2*r/(Cstar-r)+r*r/(Cstar-r)**2)).upper()
    Qrho=qbound(rho);DQrho=dqbound(rho);lam_rho=(KG*DQrho).upper()
    Hboundary=(HC*epsilon+(HD*ed+e0)/Wmin).upper()
    cap_image=(Hboundary+KG*Qrho).upper()
    # One explicit a posteriori estimate, not a search over ball radii.
    Hbar=(Hboundary/(1-lam_rho)).upper()
    Qbar=qbound(Hbar);DQbar=dqbound(Hbar);lam=(KG*DQbar).upper()
    image_Z=(Wmax*Hbar).upper();lam_Z=((HD*Ld+L0)/(1-lam)).upper()
    GZ=(Wmax*HC/((1-lam)*(1-lam_Z))).upper()
    gd=(Ld*GZ).upper();g0=(L0*GZ).upper()
    complete_solution_column=((HC+(HD*gd+g0)/Wmin)/(1-lam)).upper()
    graph_remainder=(gd+KD*DQbar*complete_solution_column).upper()
    mean_column=(g0+Km*DQbar*complete_solution_column).upper()
    qmin=box_from_record(screen['rows'][0]['weighted']['q_lower']).lower()
    qmax=c['q_upper'].upper();qinterval=qmin.union(qmax)
    inverse=(1/(qmin-graph_remainder)).upper() if qmin>graph_remainder else None
    Dleft=(ed+KD*Qbar).upper();mean_left=(e0+Km*Qbar).upper()
    gates=dict(all_663_continuous_boxes=screen['selected_closed_boxes']==663,
        positive_complete_denominator=bool(Cstar>rho),
        doubled_actual_long_boundary_domain=bool(2*F<arb(2)**-25),
        full_C_to_Dirichlet_inverse_contraction=bool(lam_f<1),
        full_C_to_Dirichlet_inverse_strict_ball=bool(image_f<rf),
        complete_cap_contraction=bool(lam_rho<1),complete_cap_strict_ball=bool(cap_image<rho),
        single_posterior_estimate_inside_ball=bool(Hbar<rho),
        full_right_trace_strict_ball=bool(image_Z<rz),full_right_trace_contraction=bool(lam_Z<1),
        complete_inner_B_graph_invertible=bool(qmin>graph_remainder),
        nonzero_actual_reflection_retained=bool(fee>0 and reflection>0))
    inputs={str(p):sha(p) for p in (args.screening,args.joint)}
    finite=[]
    for path,fp in zip(args.candidate,args.floating):
        fd=json.loads(fp.read_text());data=load_candidate(path);meta=json.loads(str(data['metadata']))
        if (fd['candidate_sha256']!=sha(path) or meta['object_sha256']!=joint['object_sha256']
            or meta['physical_frequency_factor']!=4 or meta['coordinates']!='B=alpha*b; C=Cref_nu+alpha*c'
            or meta['new_metric_family']!='E_nu=E exp(nu*h); a fixed'
            or meta['exact_bump']!='h=4096 t^6(1-t)^6 for t=(|r|-1/20)/(13/100) in (0,1), zero elsewhere'):
            raise ValueError('the exact selected boundary datum or compact target changed')
        m=int(meta['modes']);z=trace(data,Fraction(3,2))
        if len(z)!=2*m+1:raise ValueError('incomplete finite boundary trace')
        n=sum(map(abs,z[m+1:]),Fraction(0))
        n2=sum((abs(v)*(1+4*(k+1))**2 for k,v in enumerate(z[m+1:])),Fraction(0))
        defect=sum((abs(exact(z[k])+qinterval*exact(z[m+1+k])) for k in range(m)),arb(0)).upper()
        inside=n<Fraction(1,50000)
        finite.append(dict(candidate=str(path),floating=str(fp),original_finite_BVP_success=bool(fd['finite_BVP_success']),
            modes=m,radial_nodes=len(data['radial_nodes']),exact_binary_amplitude=str(dyadic(meta['amplitude'])),
            exact_binary_nu=str(dyadic(meta['nu'])),exact_nonmean_c_input_A0=str(n),exact_nonmean_c_input_A2=str(n2),
            exact_finite_c_mean=str(z[m]),inside_universal_input_ball=inside,
            actual_periodic_cap_exists_for_this_exact_boundary_datum=bool(inside and all(gates.values())),
            bounds=dict(nonzero_c_A0=record(exact(n)),finite_linear_return_defect_A0=record(defect),
                true_cap_minus_finite_B_A0=record((defect+Dleft).upper()),
                true_cap_minus_finite_c_mean=record((abs(exact(z[m]))+mean_left).upper())),
            only_boundary_data_selected=True,body_PDE_proved=False,full_trace_matching_proved=False))
        inputs[str(path)]=sha(path);inputs[str(fp)]=sha(fp)
    values=dict(inner_nonzero_c_A0_radius=epsilon,weighted_cap_radius=rho,nonzero_C_R_radius=rz,
        inner_long_Dirichlet_radius=rf,remote_Dirichlet_budget=fB,complete_denominator_lower=(Cstar-rho).lower(),
        long_C_inverse_contraction=lam_f,long_C_inverse_image=image_f,C_to_fstar_derivative=Jf,
        actual_outer_d_upper=ed,actual_outer_c_mean_upper=e0,actual_outer_d_Z_derivative=Ld,
        actual_outer_c_mean_Z_derivative=L0,cap_full_Q_bound_at_radius=Qrho,cap_full_DQ_bound_at_radius=DQrho,
        cap_full_contraction_at_radius=lam_rho,cap_image=cap_image,cap_image_margin=(rho-cap_image).lower(),
        one_explicit_complete_solution_upper=Hbar,complete_Q_bound_at_actual_solution=Qbar,
        complete_DQ_bound_at_actual_solution=DQbar,actual_solution_cap_derivative_contraction=lam,
        full_joint_right_trace_image=image_Z,full_joint_right_trace_contraction=lam_Z,
        inner_c_to_C_R_derivative=GZ,inner_c_to_d_R_derivative=gd,inner_c_to_c_mean_R_derivative=g0,
        inner_c_to_complete_cap_solution_derivative=complete_solution_column,
        inner_B_derivative_minus_negative_q=graph_remainder,inner_c_mean_derivative=mean_column,
        inner_c_to_fstar_derivative=(Jf*GZ).upper(),full_inner_B_inverse_upper=inverse,
        actual_inner_B_plus_q_c_A0_upper=Dleft,actual_inner_c_mean_abs_upper=mean_left,
        inner_q_lower=qmin,inner_q_upper=qmax,actual_right_analytic_width_lower=j['analytic_width_lower'],
        actual_complete_long_L_lower=j['long_L_lower'],nonzero_actual_R74_and_reflection_fee=fee)
    result=dict(kind='actual_universal_small_inner_periodic_cap_and_long_segment_r15',complete=True,
        source_sha256=sha(__file__),inputs=inputs,object_sha256=joint['object_sha256'],
        exact_center_parameter=joint['exact_center_parameter'],parameter_half_width=joint['parameter_half_width'],
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,complete_primitive_tail=True,
        all_Fourier_modes_retained=True,exact_cap_interval=['3/2','25/8'],exact_weight=['3/2','1/128'],
        actual_open_periodic_cap_graph_certified=all(gates.values()),gates=gates,
        bounds={k:None if v is None else record(v) for k,v in values.items()},selected_exact_finite_boundary_data=finite,
        inner_data='All real even fourfold nonmean c(3/2) in the A0 ball 1/50000, additionally A2 for C2 up to the inner boundary.',
        both_means_retained=True,actual_B_mean_identically_zero_by_common_reflection=True,
        full_B_and_C_match_actual_periodic_long_segment=True,remote_fB_is_independent=True,
        original_body_graft_and_long_object_only=True,independent_of_old_alpha065_centre=True,
        remote_label_equation_proved=False,body_PDE_proved=False,closed_surface_complete=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_cap_radial_analytic_screening.py','fourfold_codazzi_cap_actual_long_tail_matching.py',
            'fourfold_codazzi_cap_open_curvature_ports_v2.py','fourfold_codazzi_candidate_shards.py',
            'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_phase_metric_defect.py')})
    save(args.out,result)
    print(dict(certified=result['actual_open_periodic_cap_graph_certified'],failed=[k for k,v in gates.items() if not v],
        posterior=Hbar.str(12),joint_contraction=lam_Z.str(12),graph_remainder=graph_remainder.str(12),
        nonlinear_B=Dleft.str(12),mean=mean_left.str(12),selected=[dict(alpha=v['exact_binary_amplitude'],
        inside=v['inside_universal_input_ball'],finite=v['original_finite_BVP_success']) for v in finite]),flush=True)


if __name__=='__main__':main()
