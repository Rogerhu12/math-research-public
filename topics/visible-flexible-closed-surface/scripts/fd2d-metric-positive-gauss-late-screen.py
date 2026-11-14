#!/usr/bin/env python3
"""Only one saved late node and its two adjacent P1 cells.

The full-circle grid and its Fourier split are finite diagnostics. Exact
rational P1 coefficient signs and conservative all-angle n/l enclosures
are kept separate. No BVP, Jacobian, body ODE or new field projection.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path
import resource
import time
import numpy as np
from fd2d_gc_archive_arrays import identity, save_npz
from fd2d_gc_bump_coast_native_field import window
from fd2d_gc_positive_gauss_l_native_field import PositiveGaussLNativeField


def maximum(value):
    return float(np.max(np.abs(value), initial=0.))


def scalar_json(value):
    if isinstance(value,np.ndarray):return value.tolist()
    if isinstance(value,np.integer):return int(value)
    if isinstance(value,np.floating):return float(value)
    raise TypeError(type(value).__name__)


def write_json(path,value):
    path.write_text(json.dumps(value,indent=2,allow_nan=False,default=scalar_json)+'\n')


def rational(value):
    return Fraction.from_float(float(value))


def fraction_record(value):
    return dict(exact_rational=str(value), display=float(value), sign=int(value>0)-int(value<0))


def exact_coefficients(reader,s):
    i=int(np.clip(np.searchsorted(reader.nodes,s,side='right')-1,0,len(reader.nodes)-2))
    t=(rational(s)-rational(reader.nodes[i]))/(rational(reader.nodes[i+1])-rational(reader.nodes[i]))
    return [rational(a)+t*(rational(b)-rational(a))
            for a,b in zip(reader.values[i],reader.values[i+1])]


def exact_angle_facts(reader,s,kappa_upper):
    coef=exact_coefficients(reader,s)
    parts=dict(n=coef[:reader.e],l=coef[reader.d:])
    cycles={
        'zero':(Fraction(1),),
        'pi_over_6':(Fraction(1),Fraction(1,2),Fraction(-1,2),Fraction(-1),Fraction(-1,2),Fraction(1,2)),
        'pi_over_4':(Fraction(1),Fraction(0),Fraction(-1),Fraction(0)),
        'pi_over_3':(Fraction(1),Fraction(-1,2),Fraction(-1,2)),
        'pi_over_2':(Fraction(1),Fraction(-1))}
    out={}
    for name,c in parts.items():
        center=c[0];radius=sum(abs(q) for q in c[1:])
        angles={label:sum(value*cycle[j%len(cycle)] for j,value in enumerate(c))
                for label,cycle in cycles.items()}
        out[name]=dict(all_angle_lower=fraction_record(center-radius),
            all_angle_upper=fraction_record(center+radius+kappa_upper),
            correction_special_angles={key:fraction_record(value) for key,value in angles.items()},
            exact_complete_value_at_zero=fraction_record(angles['zero']),
            positive_complete_value_proved_at=[key for key,value in angles.items() if value>0],
            nonnegative_tail_used=True)
        if name=='n':
            out[name]['exact_complete_value_at_pi_over_2']=fraction_record(angles['pi_over_2'])
            negative=angles['zero']<0 or angles['pi_over_2']<0
            positive=any(value>0 for value in angles.values())
            out[name]['both_signs_and_angular_zero_proved']=bool(negative and positive)
    out['scope']=('Exact P1 binary-node Fourier coefficients at this exact binary s; '
        'nonnegative full tail and 0<=S5 weight<=1; no radial evaluation or Fourier truncation needed. '
        'Only zero-angle n/l and pi/2 n are complete exact values; the other correction values '
        'are lower bounds on the full n/l. Ranges are conservative full-circle enclosures.')
    return out


def spectrum(values,retained_mode,theta):
    W=len(values);F=np.fft.rfft(values)/W
    frequencies=2*np.arange(retained_mode+1)
    coeff=np.r_[F[0].real,2*F[frequencies[1:]].real]
    low=np.cos(theta[:,None]*frequencies)@coeff
    high=values-low
    total=float(np.mean(values*values));low_energy=float(np.mean(low*low))
    high_energy=float(np.mean(high*high))
    top=np.argsort(abs(F[1:]))[-8:][::-1]+1
    summary=dict(full_maximum=maximum(values),retained_maximum=maximum(low),omitted_maximum=maximum(high),
        full_rms=float(np.sqrt(total)),retained_rms=float(np.sqrt(low_energy)),
        omitted_rms=float(np.sqrt(high_energy)),
        retained_energy_fraction=low_energy/max(total,1e-300),
        omitted_energy_fraction=high_energy/max(total,1e-300),
        discrete_orthogonality_error=abs(total-low_energy-high_energy),
        D2_reflection_error=maximum(values-values[np.mod(-np.arange(W),W)]),
        D2_half_period_error=maximum(values-np.roll(values,W//2)),
        top_nonconstant_frequencies=[dict(frequency=int(k),cosine=2*float(F[k].real),
            sine=-2*float(F[k].imag)) for k in top],
        angular_truncation_applied_to_actual_field=False,
        continuous_Fourier_or_alias_certificate=False)
    return summary,low,high,coeff


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('field','source-report','candidate','inlet','cache','out-prefix'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--node',type=int,default=118)
    ap.add_argument('--angular',type=int,default=1024)
    args=ap.parse_args();start=time.monotonic();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use a fresh late-screen prefix')
    if args.angular<256 or args.angular%256:raise ValueError('Retain the original 256 point grid as a subset')
    original=identity(args.field);source_report=json.loads(args.source_report.read_text())
    r=PositiveGaussLNativeField(args.field,args.candidate,reference_inlet=args.inlet,reference_cache=args.cache)
    if not 1<=args.node<len(r.nodes)-1:raise ValueError('Requested node must have both adjacent cells')
    tail_controls=[rational(x) for x in r.tail.coefficients]
    if min(tail_controls)<0:raise ValueError('The exact nonnegative-tail bound requires actual nonnegative controls')
    width_lower=min(rational(r.tail.width),Fraction(23,50))
    kappa_upper=max(tail_controls)*Fraction(315,128)/width_lower
    queries=[('left_node',float(r.nodes[args.node-1])),('peak_node',float(r.nodes[args.node])),
             ('right_node',float(r.nodes[args.node+1]))]
    for cell in (args.node-1,args.node):
        left,right=r.nodes[cell:cell+2]
        queries.extend((f'cell{cell}_fraction{int(4*t)}',float(left+t*(right-left))) for t in (.25,.5,.75))
    queries.sort(key=lambda item:item[1])
    theta=2*np.pi*np.arange(args.angular)/args.angular
    rows=[];arrays=dict(theta=theta);retained=[];old_subset_difference=None
    for index,(label,s) in enumerate(queries):
        if s<max(r.angular_atlas.exit_stop,r.blend_interval[1]):
            raise ValueError('This late exact-angle consumer requires the actual material chart U=xi')
        w,ws=window(s,r.coast_reference.entry_s,r.coast_reference.length,r.reference_rim_fraction)
        if w!=0. or ws!=0. or s<r.seed_weight_definition['end']:
            raise ValueError('The requested local span is not outside the coast and seed lifting windows')
        q=r.evaluate_angular_native(s,theta)
        if maximum(q['u']-theta)!=0. or maximum(q['U_xi']-1)!=0.:
            raise ArithmeticError('The actual saved chart is not the claimed material angle')
        n,m,l=(q[k] for k in ('n','m','l'));K=-q['a_ss']/q['a']
        G=n*l-m*m-K;summary,low,high,coeff=spectrum(G,r.K,theta)
        retained.append(coeff)
        j=int(np.argmax(abs(G)));actualfields={}
        for name,values in (('n',n),('m',m),('l',l)):
            imin,imax=int(np.argmin(values)),int(np.argmax(values))
            actualfields[name]=dict(minimum=float(values[imin]),minimum_xi=float(theta[imin]),
                maximum=float(values[imax]),maximum_xi=float(theta[imax]),
                minimum_absolute=float(np.min(abs(values))),
                negative_samples=int(np.count_nonzero(values<0.)),
                positive_samples=int(np.count_nonzero(values>0.)),
                near_zero_1e_minus8=int(np.count_nonzero(abs(values)<1e-8)))
        piece_index=int(np.clip(np.searchsorted(r.profile.base.breaks,s,side='right')-1,
                               0,len(r.profile.base.segments)-1))
        piece=r.profile.base.segments[piece_index]
        base_piece={key:piece[key] for key in ('kind','label','s0','s1','p0','p1','ps0','ps1','L') if key in piece}
        bump_max=[maximum(r.profile.basis([s],order)) for order in (0,1,2)]
        row=dict(label=label,physical_s=s,sampled_field=actualfields,
            actual_K=float(K[0]),actual_a=float(q['a'][0]),actual_a_s=float(q['a_s'][0]),
            actual_a_ss=float(q['a_ss'][0]),base_piece_index=piece_index,base_piece=base_piece,
            actual_bump_value_first_second_basis_maxima=bump_max,
            coast_window=float(w),material_chart_exact=True,
            gauss_spectrum=summary,exact_angle_facts=exact_angle_facts(r,s,kappa_upper),
            determinant_nl_minus_m2_sample_range=[float(np.min(n*l-m*m)),float(np.max(n*l-m*m))],
            sampled_indefinite_points=int(np.count_nonzero(n*l-m*m<0.)),
            peak=dict(xi=float(theta[j]),signed_G=float(G[j]),n=float(n[j]),m=float(m[j]),l=float(l[j]),
                n_times_l=float(n[j]*l[j]),m_squared=float(m[j]*m[j]),K=float(K[j]),
                retained_G=float(low[j]),omitted_G=float(high[j])))
        if label=='peak_node':
            peak=source_report['final_locations']['full_gauss']
            if peak['node']!=args.node or peak['s']!=s:raise ValueError('Source report names a different peak')
            oldidx=int(peak['angular_index'])*(args.angular//256)
            old_subset_difference=abs(float(G[oldidx])-float(peak['signed_value']))
            row['original_256_grid_peak_reproduction_error']=old_subset_difference
            row['original_256_grid_maximum']=maximum(G[::args.angular//256])
        rows.append(row)
        for key,value in (('n',n),('m',m),('l',l),('G',G),('G_low',low),('G_high',high)):
            arrays[f'point_{index}_{key}']=np.asarray(value,float)
    arrays.update(physical_s=np.array([q[1] for q in queries]),retained_G_coefficients=np.array(retained))
    samples=save_npz(stem.with_name(stem.name+'-samples.npz'),**arrays)
    definition=stem.with_name(stem.name+'-definition.json');write_json(definition,r.definition())
    here=Path(__file__).resolve().parent
    sources=[identity(here/name) for name in ('fd2d-metric-positive-gauss-late-screen.py',
        'fd2d_gc_positive_gauss_l_native_field.py','fd2d_positive_flat_developable_family.py')]
    peakrow=next(row for row in rows if row['label']=='peak_node')
    report=dict(schema='fd2d-actual-R153-late-two-cell-diagnostic-v1',actual_execution=True,
        input=original,source_report=identity(args.source_report),candidate=identity(args.candidate),sources=sources,
        node=args.node,adjacent_cells=[args.node-1,args.node],angular_grid=args.angular,
        finite_angular_samples_not_continuous_residual_certificate=True,
        exact_angle_coefficient_arithmetic='Fraction of saved binary64 values and actual binary s; exact P1 ratio',
        exact_nonnegative_tail=True,tail_parameter_minimum=float(min(tail_controls)),
        tail_parameter_maximum=float(max(tail_controls)),
        tail_kappa_global_upper=fraction_record(kappa_upper),
        tail_width_lower=fraction_record(width_lower),
        protected_bump_free_final_interval=[float(r.profile.supports[:,1].max()),float(r.profile.end)],
        no_unknown_n_divided_in_this_span=True,point_queries=rows,
        peak_node_summary=peakrow,original_256_peak_reproduction_error=old_subset_difference,
        actual_original_input_unchanged=identity(args.field)==original,
        definition=identity(definition),samples=samples,
        BVP_run=False,body_run=False,Jacobian_assembled=False,
        actual_field_projection_or_parameters_changed=False,
        continuous_residual_certificate=False,closed_surface_certificate=False,
        seconds=time.monotonic()-start,maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    report['passed_execution_checks']=bool(report['actual_original_input_unchanged'] and old_subset_difference<1e-9)
    out=stem.with_name(stem.name+'-report.json');write_json(out,report)
    print(json.dumps(dict(report=identity(out),actual_execution_checks=report['passed_execution_checks'],
        seconds=report['seconds'],maximum_rss_kib=report['maximum_rss_kib'],
        peak_spectrum=peakrow['gauss_spectrum'],peak_n=peakrow['sampled_field']['n'],
        exact_n_axis=peakrow['exact_angle_facts']['n']),allow_nan=False),flush=True)
    raise SystemExit(0 if report['passed_execution_checks'] else 1)


if __name__=='__main__':main()
