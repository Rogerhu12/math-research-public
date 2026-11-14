#!/usr/bin/env python3
"""Consume the complete M128 inner trace in the actual open curvature cap map.

Only exact dyadic endpoint polynomials enter this calculation. The cap is
certified; the finite candidate's body PDE and its nonlinear regular tail are
not thereby certified. Both mean rows remain explicit matching residuals.
"""
from __future__ import annotations
import argparse,json,gzip
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_cap_open_curvature_ports_v2 import trace,exact,dyadic,read
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record,save,sha


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--ports',type=Path,default=Path('notes/2026-11-13-R133-open-curvature-ports-r1-v2-native.json.gz'))
    ap.add_argument('--candidate',type=Path,default=Path('notes/2026-11-13-R133-compact-metric-outer-mean-m128-bounded-v7-b4-candidate.json'))
    ap.add_argument('--floating',type=Path,default=Path('notes/2026-11-13-R133-compact-metric-outer-mean-m128-bounded-v7-b4-floating.json'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320
    if args.out.exists():raise FileExistsError('preserve every complete inner trace attempt')
    ports=read(args.ports);floating=json.loads(args.floating.read_text())
    if (ports['kind']!='actual_open_all_Fourier_nonlinear_curvature_cap_port_graph_v2_inward_radius'
        or not ports['complete'] or not ports['full_open_port_ball_certified']
        or not ports['strictly_inward_parsed_radius']
        or ports['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_cap_open_curvature_ports_v2.py'))):
        raise ValueError('the actual complete open curvature graph is required')
    for p,h in ports['inputs'].items():
        if sha(p)!=h:raise ValueError('a complete graph input changed: '+p)
    for p,h in ports['dependencies'].items():
        if sha(Path(__file__).with_name(p))!=h:raise ValueError('a complete graph dependency changed: '+p)
    if not floating['finite_BVP_success'] or floating['candidate_sha256']!=sha(args.candidate):
        raise ValueError('this consumer names the completed M128 finite candidate, not a failed attempt')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']));m=int(meta['modes'])
    if (meta['object_sha256']!=ports['object_sha256'] or m!=128 or meta['physical_frequency_factor']!=4
        or meta['coordinates']!='B=alpha*b; C=Cref_nu+alpha*c'
        or meta['new_metric_family']!='E_nu=E exp(nu*h); a fixed'
        or meta['exact_bump']!='h=4096 t^6(1-t)^6 for t=(|r|-1/20)/(13/100) in (0,1), zero elsewhere'):
        raise ValueError('the full compact-metric candidate identity changed')
    left,right=map(Fraction,ports['exact_requested_interval'])
    if left<Fraction(18,100):raise ValueError('the cap target is still inside the metric modification')
    new=trace(saved,left);old=ports['exact_finite_centre_inner_trace'];oldb=list(map(Fraction,old['B_sine']));oldc=list(map(Fraction,old['c_cosine']))
    oldb+=([Fraction(0)]*(m-len(oldb)));oldc+=([Fraction(0)]*(m-len(oldc)))
    db=[new[j]-oldb[j] for j in range(m)]
    dc=[new[m+1+j]-oldc[j] for j in range(m)]
    dc0=new[m]-Fraction(old['c_mean']);delta=sum(map(abs,dc),Fraction(0))
    b={k:box_from_record(v) for k,v in ports['bounds'].items()}
    q=b['inner_q_lower'].lower().union(b['inner_q_upper'].upper())
    linear_defect=sum((abs(exact(x)+q*exact(y)) for x,y in zip(db,dc)),arb(0)).upper()
    admissible=delta<Fraction(ports['inner_c_nonzero_variation_A0'])
    error_B=(b['base_inner_B_nonzero_error_A0'].upper()+linear_defect
        +b['inner_nonzero_derivative_minus_negative_q'].upper()*exact(delta)).upper()
    mean_gain=box_from_record(ports['nonlinear_c_mean_left_derivative_remainder_columns']['inner_c_nonzero']).upper()
    error_c0=(b['base_inner_c_mean_error'].upper()+abs(exact(dc0))+mean_gain*exact(delta)).upper()
    report=dict(kind='actual_M128_complete_inner_trace_in_certified_nonlinear_cap_graph',complete=True,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.ports,args.candidate,args.floating)},
        object_sha256=ports['object_sha256'],exact_center_parameter=ports['exact_center_parameter'],
        parameter_half_width=ports['parameter_half_width'],exact_requested_interval=ports['exact_requested_interval'],
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,complete_primitive_tail=True,
        actual_input_modes=m,physical_frequencies=[4,4*m],complete_lossless_candidate_parts_retained=True,
        exact_binary_amplitude=str(dyadic(meta['amplitude'])),exact_binary_nu=str(dyadic(meta['nu'])),
        cap_metric_after_compact_support_exactly_identical=True,
        exact_nonzero_c_input_variation_A0=str(delta),exact_mean_c_candidate_difference=str(dc0),
        exact_B_sine_difference=list(map(str,db)),exact_c_cosine_difference=list(map(str,dc)),
        complete_input_is_inside_open_cap_graph=admissible,actual_driven_cap_for_this_input_exists=admissible,
        bounds={k:record(v) for k,v in dict(inner_c_input_difference_A0=exact(delta),
            finite_body_trace_linear_return_defect_A0=linear_defect,
            true_cap_minus_finite_body_B_nonzero_A0=error_B,
            true_cap_minus_finite_body_c_mean=error_c0,
            true_cap_B_mean_abs=b['base_inner_B_mean_abs'],
            open_input_margin=exact(Fraction(ports['inner_c_nonzero_variation_A0'])-delta)).items()},
        nonzero_C_trace_match_is_exact=True,nonzero_B_trace_and_c_mean_are_unclosed_residuals=True,
        exact_finite_M128_inner_trace=dict(B_sine=list(map(str,new[:m])),c_mean=str(new[m]),c_cosine=list(map(str,new[m+1:]))),
        all_Fourier_cap_output_modes_retained=True,both_means_retained=True,
        nonlinear_regular_tail_matched=False,body_matched=False,full_body_PDE_certified=False,
        periodic_frame_holonomy_proved=False,closed_surface_complete=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_cap_open_curvature_ports_v2.py','fourfold_codazzi_candidate_shards.py',
            'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_phase_metric_defect.py')})
    save(args.out,report)
    print(dict(admissible=admissible,delta_c=exact(delta).str(15),linear_defect=linear_defect.str(15),
        B_matching_residual=error_B.str(15),mean_c_matching_residual=error_c0.str(15)),flush=True)


if __name__=='__main__':main()
