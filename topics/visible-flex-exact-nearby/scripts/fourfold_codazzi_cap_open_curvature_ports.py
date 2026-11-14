#!/usr/bin/env python3
"""Actual open full-Fourier curvature trace graph of the corrected driven cap.

This consumes the complete regular residual, exact interface point sources,
and the single verified smaller ball. It keeps both means and all outer ports.
It is not a height DN map or a nonlinear regular-tail matching theorem.
"""
from __future__ import annotations
import argparse,gzip,json
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record,save,sha


def read(p):return json.loads(gzip.decompress(Path(p).read_bytes()))


def exact(q):
    q=Fraction(q);return arb(q.numerator)/q.denominator


def dyadic(x):return Fraction.from_float(float(x))


def trace(saved,r):
    nodes=list(map(dyadic,saved['radial_nodes']));r=Fraction(r)
    j=max(k for k,x in enumerate(nodes[:-1]) if x<=r)
    cc=saved['piece_coefficients'][:,j];h=r-nodes[j]
    alpha=dyadic(json.loads(str(saved['metadata']))['amplitude']);answer=[]
    for k in range(cc.shape[1]):
        z=dyadic(cc[0,k])
        for v in cc[1:,k]:z=z*h+dyadic(v)
        answer.append(alpha*z)
    return answer


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cap',type=Path,default=Path('notes/2026-11-13-R133-centered-cap-r1-v4-jumps-native.json.gz'))
    ap.add_argument('--regularity',type=Path,default=Path('notes/2026-11-13-R133-centered-cap-r1-regularity-native.json.gz'))
    ap.add_argument('--kernels',type=Path,default=Path('notes/2026-11-13-R133-A0-driven-cap-r1-native.json.gz'))
    ap.add_argument('--reference',type=Path,default=Path('notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz'))
    ap.add_argument('--candidate',type=Path,default=Path('notes/2026-11-13-R133-compact-metric-outer-mean-m64-candidate.npz.gz'))
    ap.add_argument('--inner-variation',type=Fraction,default=Fraction(1,100000))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320
    if args.out.exists():raise FileExistsError('preserve every open-port attempt')
    cap,reg,kernel,reference=(read(p) for p in (args.cap,args.regularity,args.kernels,args.reference))
    if (cap['kind']!='actual_complete_nonzero_centred_cap_with_all_exact_interface_jumps'
        or not cap['complete'] or not cap['actual_driven_cap_exists'] or not cap['actual_solution_radially_continuous']
        or reg['kind']!='actual_nonzero_centred_cap_strong_translation_regularization_v1'
        or not reg['complete'] or not reg['all_exact_radial_interface_point_sources_paid']
        or reg['input_sha256']!=sha(args.cap) or reg['kernels_sha256']!=sha(args.kernels)
        or kernel['input_sha256']!=sha(args.reference)):
        raise ValueError('actual completed cap/regularity/Green identities are required')
    for doc,name in ((cap,'fourfold_codazzi_centered_cap_interface_jumps.py'),
                     (reg,'fourfold_codazzi_centered_cap_regularity.py'),
                     (kernel,'fourfold_codazzi_cap_A0_translation_budget.py')):
        if doc['source_sha256']!=sha(Path(__file__).with_name(name)):raise ValueError('completed producer changed')
        for helper,h in doc.get('dependencies',{}).items():
            if sha(Path(__file__).with_name(helper))!=h:raise ValueError('frozen helper changed: '+helper)
        if not all(doc[k] for k in ('whole_affine_parameter_interval','whole_real_angular_circle','complete_primitive_tail')):
            raise ValueError('the true target scope changed')
    for p,h in cap['inputs'].items():
        if sha(p)!=h:raise ValueError('complete cap input changed: '+p)
    if cap['inputs'].get(str(args.candidate))!=sha(args.candidate):raise ValueError('exact centre changed')
    for doc in (reg,kernel):
        for k in ('object_sha256','exact_center_parameter','parameter_half_width','exact_requested_interval'):
            if doc[k]!=cap[k]:raise ValueError('different actual target/interval: '+k)
    c={k:box_from_record(v) for k,v in kernel['constants'].items()}
    b={k:box_from_record(v) for k,v in cap['bounds'].items()}
    rb={k:box_from_record(v) for k,v in reg['bounds'].items()}
    selected=reg['chosen_strict_ball']
    if not selected['passed']:raise ValueError('the one selected complete ball is not strict')
    rho=box_from_record(selected['radius']).upper();lam=box_from_record(selected['contraction']).upper()
    LQ=max(box_from_record(selected[k]).upper() for k in ('full_Q_B_derivative','full_Q_c_derivative')).upper()
    eps=b['fixed_point_residual_upper'].upper();eta=exact(args.inner_variation)
    HD=c['boundary_d_factor'].upper();HC=c['boundary_c_factor'].upper();KD=c['nonlinear_D_kernel'].upper()
    qp=c['q_upper'].upper();qm=box_from_record(kernel['rows'][0]['q_lower']).lower()
    open_image=(eps+HC*eta+lam*rho).upper();open_gate=bool(eta>0 and lam<1 and open_image<rho)
    hfac=dict(inner_c_nonzero=HC,outer_d_nonzero=HD,outer_B_mean=arb(1),outer_c_mean=arb(1))
    solution_columns={k:(v/(1-lam)).upper() for k,v in hfac.items()}
    d_remainder_columns={k:(KD*LQ*v/(1-lam)).upper() for k,v in hfac.items()}
    qpert=d_remainder_columns['inner_c_nonzero'];invertible=bool(qm>qpert)
    inverse=(1/(qm-qpert)).upper() if invertible else None
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']));m=int(meta['modes'])
    left,right=map(Fraction,cap['exact_requested_interval']);inner=trace(saved,left);outer=trace(saved,right)
    if m!=cap['centre_all_modes'] or len(inner)!=2*m+1:raise ValueError('not the complete centre trace')
    entry=reference['true_R74_entrance'];aR=box_from_record(entry['radius']);omega=box_from_record(entry['normalized_omega'])
    fee=box_from_record(reference['Jacobi']['full_frequency_interval']['complete_true_tail_fee']).upper()
    qR=1/(1+(aR/(4*omega))**2).sqrt()+arb(0,fee)
    centre_outer_d=sum((abs(exact(outer[j])+qR*exact(outer[m+1+j])) for j in range(m)),arb(0)).upper()
    eD=exact(cap['outer_nonzero_d_A2_budget']);eB0=exact(cap['outer_B_mean_budget']);eC0=exact(cap['outer_c_mean_budget'])
    first=reference['rows'][kernel['rows'][0]['native_index']]['coefficients']
    last=reference['rows'][kernel['rows'][-1]['native_index']]['coefficients']
    aL=box_from_record(first['a']);CL=box_from_record(first['Cref']);CR=box_from_record(last['Cref'])
    tauB=(aR.upper()/aL.lower())**2
    tauC=(tauB*abs(CR).upper()/abs(CL).lower()).upper();tauB=tauB.upper()
    if not 0<tauB<1 or not 0<tauC<1:raise ValueError('actual complete mean transfer enclosure failed')
    global_error=rb['actual_correction_X0'].upper()
    JB=b['total_B_nonzero_jump_A0'].upper();JC=b['total_c_nonzero_jump_A0'].upper();J0=b['total_c_mean_jump'].upper()
    sd=c['D_rate_per_frequency'].lower()
    base_d_error=(centre_outer_d+eD+(b['full_B_residual_over_frequency_A0'].upper()
        +qp*b['full_C_residual_over_frequency_A0'].upper())/sd+JB+qp*JC+KD*LQ*global_error).upper()
    base_c_mean_error=(tauC*(eC0+abs(exact(outer[m])).upper())
        +c['forced_C_mean_kernel'].upper()*b['full_C_mean_residual'].upper()+J0
        +c['mean_C_nonlinear_kernel'].upper()*LQ*global_error).upper()
    base_b_mean=(tauB*eB0).upper()
    mean_remainder_columns={k:(c['mean_C_nonlinear_kernel'].upper()*LQ*v/(1-lam)).upper() for k,v in hfac.items()}
    report=dict(kind='actual_open_all_Fourier_nonlinear_curvature_cap_port_graph',complete=True,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.cap,args.regularity,args.kernels,args.reference,args.candidate)},
        object_sha256=cap['object_sha256'],exact_center_parameter=cap['exact_center_parameter'],
        parameter_half_width=cap['parameter_half_width'],exact_requested_interval=cap['exact_requested_interval'],
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,complete_primitive_tail=True,
        inner_c_nonzero_variation_A0=str(args.inner_variation),inner_variation_may_have_infinitely_many_modes=True,
        input_regularization='For local C2 immersion and strong two-angle derivatives, the varied inner trace also belongs to A2; its A2 norm need not be small.',
        original_outer_ports=dict(d_nonzero_A2=cap['outer_nonzero_d_A2_budget'],B_mean=cap['outer_B_mean_budget'],c_mean=cap['outer_c_mean_budget']),
        full_open_port_ball_certified=open_gate,nonzero_curvature_trace_derivative_invertible=bool(open_gate and invertible),
        linear_nonzero_inner_graph='b_L=-q_m(L)*c_L+T_m*d_R; b_m=i*sgn(m)*Bhat_m. The nonlinear remainder is the complete D-source integral.',
        mean_rows='B0(L)=(aR/aL)^2 B0(R); c0(L)=aR^2*CrefR/(aL^2*CrefL)*c0(R) plus the full Q0 integral.',
        bounds={k:record(v) for k,v in dict(radius=rho,complete_residual=eps,open_image=open_image,
            open_image_margin=(rho-open_image).lower(),full_contraction=lam,full_Q_derivative=LQ,
            inner_q_lower=qm,inner_q_upper=qp,inner_nonzero_derivative_minus_negative_q=qpert,
            mean_B_linear_transfer_upper=tauB,mean_c_linear_transfer_upper=tauC,
            base_inner_B_nonzero_error_A0=base_d_error,base_inner_c_mean_error=base_c_mean_error,
            base_inner_B_mean_abs=base_b_mean,centre_outer_d_A0=centre_outer_d).items()},
        inverse_nonzero_curvature_trace_derivative_upper=record(inverse) if inverse is not None else None,
        complete_solution_derivative_columns={k:record(v) for k,v in solution_columns.items()},
        nonlinear_d_left_derivative_remainder_columns={k:record(v) for k,v in d_remainder_columns.items()},
        nonlinear_c_mean_left_derivative_remainder_columns={k:record(v) for k,v in mean_remainder_columns.items()},
        exact_finite_centre_inner_trace=dict(B_sine=list(map(str,inner[:m])),c_mean=str(inner[m]),c_cosine=list(map(str,inner[m+1:]))),
        both_means_retained=True,all_Fourier_output_modes_retained=True,
        grounded_flux_or_height_DN_identified=False,nonlinear_regular_tail_matched=False,body_matched=False,
        periodic_frame_holonomy_proved=False,closed_surface_complete=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_centered_cap_interface_jumps.py','fourfold_codazzi_centered_cap_regularity.py',
            'fourfold_codazzi_cap_A0_translation_budget.py','fourfold_codazzi_candidate_shards.py',
            'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_phase_metric_defect.py')})
    save(args.out,report)
    print(dict(open_ball=open_gate,nonzero_derivative_invertible=bool(open_gate and invertible),
        image=open_image.str(15),q_remainder=qpert.str(15),inverse=None if inverse is None else inverse.str(15),
        inner_B_error=base_d_error.str(15),inner_mean_c_error=base_c_mean_error.str(15),mean_B=base_b_mean.str(15)),flush=True)


if __name__=='__main__':main()
