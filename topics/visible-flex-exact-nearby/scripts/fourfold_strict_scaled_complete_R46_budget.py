#!/usr/bin/env python3
"""Reuse all 215 completed strict cells in cutoff-dependent Sobolev norms.

No geometry, primitive, target, ray or closed native box is recomputed.
The saved complete energy map is diagonally rescaled; all fields, full
sources, means, cross-cone outputs and the physical Lambda remain intact.
"""
from __future__ import annotations
import argparse, math, time
from fractions import Fraction
from pathlib import Path
from flint import arb, acb_mat, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import read, save, sha, stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked
from fourfold_strict_high_energy_triangular import positive_matrix_bound, weighted_principal
from fourfold_negative_root_physical_graph_operator import mult, compositions, complete_moment, cross_bound
from fourfold_strict_complete_R46_budget import composition_constants


def up(row):
    return stored(row).upper()


def lo(row):
    return stored(row).lower()


def matrix_record(A):
    return [[record(A[i,j].real) for j in range(A.ncols())] for i in range(A.nrows())]


def inverse_power_sum(N, polynomial_power, denominator_power):
    if denominator_power-polynomial_power <= 1:
        raise ValueError('complete inverse-power series is not summable')
    return sum((arb(math.comb(polynomial_power,j))/arb(N)**j
                *(1+arb(1)/(denominator_power-j-1))
                for j in range(polynomial_power+1)),arb(0)).upper()


def scaled_ibp_cross(N, B24, rmax, gain, same_order):
    direct=(B24*inverse_power_sum(N,rmax+gain,24)).upper()
    split=(same_order+B24/arb(N)**gain
           *inverse_power_sum(N,rmax,24-gain)).upper()
    return min(direct,split).upper()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--strict',type=Path,default=Path(
        'notes/2026-11-13-R46-complete-actual-strict-operator.json'))
    ap.add_argument('--fields',type=Path,default=Path(
        'notes/2026-11-13-R46-native-WKB-full-strict-fields-v2.json.gz'))
    ap.add_argument('--graph',type=Path,default=Path(
        'notes/2026-11-13-negative-root-physical-graph-operator.json'))
    ap.add_argument('--scales',type=int,nargs='+',default=[1,4096,16384,65536,1048576])
    ap.add_argument('--bits',type=int,default=320)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists() or any(N<1 for N in a.scales):
        raise ValueError('new output and positive scales required')
    ctx.prec=a.bits;tick=time.monotonic()
    d=checked(a.strict,'fourfold_strict_complete_R46_budget.py')
    f=checked(a.fields,'fourfold_strict_actual_wkb_fields.py')
    g=checked(a.graph,'fourfold_negative_root_physical_graph_operator.py')
    if (d['kind']!='actual_full_strict_R46_complete_strong_operator_budget'
        or d['inputs'].get(str(a.fields))!=sha(a.fields)
        or f['kind']!='actual_strict_R46_complete_WKB_and_energy_fields'):
        raise ValueError('the complete original 215-cell strict certificate is required')
    if f['object_sha256']!=sha(f['object_path']):
        raise ValueError('actual fixed-type object changed')
    if f['identity']!=d['identity'] or len(f['cells'])!=215 or d['positive_cells']!=215:
        raise ValueError('the same complete native field cover is required')
    si,gi=d['identity'],g['identity']
    if si['object_sha256']!=gi['center_object_sha256']:
        raise ValueError('root graph uses a different actual operator')
    for key in ('origin_inputs_sha256','direction_sha256','exact_center_parameter',
                'exact_parameter_half_width','exact_parameter_interval'):
        if si[key]!=gi[key]:raise ValueError('actual parameter family differs: '+key)
    if d['exact_physical_interval'][1]!=g['physical_cut']:
        raise ValueError('actual root graph and strict physical cuts differ')
    lattice='physical frequencies 4*n; scaled norm uses 1+(4*n)^2/(4*N)^2=1+n^2/N^2'
    A=acb_mat([[up(v) for v in row] for row in d['whole_both_direction_energy_map']])
    if A.nrows()!=11 or A.ncols()!=11:
        raise ValueError('complete ten-derivative energy map is missing')
    if any(A[i,j]!=0 for i in range(11) for j in range(i+1,11)):
        raise ValueError('saved complete energy map is not lower triangular')
    ranges={key:[] for key in ('alpha','gamma','lambda')}
    Ms=[];mumin=[];mup=[];mp=[];tp=[]
    logdiag=[arb(0) for _ in range(11)]
    base_integral=arb(0);char_integral=arb(0)
    cursor=Fraction(0)
    for row in f['cells']:
        left,right=Fraction(row['left']),Fraction(row['right'])
        if left!=cursor or not left<right:raise ValueError('actual strict cover has a gap')
        cursor=right;length=exact_arb(right-left)
        for key in ranges:ranges[key].append(row['energy']['positive_ranges'][key])
        M={name:up(v) for name,v in row['complete_complex_field_moduli'].items()}
        Ms.append(M)
        mumin.append(lo(row['geometry']['mu_modulus_lower']))
        mup.append(M['mu']);tp.append(M['T'])
        mp.append(up(row['geometry']['m_modulus_upper']))
        for side in ('forward','backward'):
            b=up(row['energy']['base_energy_rate_'+side])/2
            c=up(row['energy']['first_characteristic_rate_'+side])
            base_integral+=length*max(arb(0),b)
            char_integral+=length*c
            for j in range(11):
                logdiag[j]+=length*max(arb(0),b+j*c)
    if str(cursor)!=g['physical_cut']:
        raise ValueError('full actual strict endpoint is missing')
    rr={key:(min(lo(v[0]) for v in rows).lower(),
             max(up(v[1]) for v in rows).upper()) for key,rows in ranges.items()}
    if not min(v[0] for v in rr.values())>0:
        raise ValueError('true energy weights lack a positive global lower bound')
    flow=d['actual_relative_flow']
    CJ=up(flow['relative_derivative_modulus'])
    delta_theta=lo(flow['full_physical_angle_strip'])
    flow_width=4*delta_theta
    field_width=4*exact_arb(Fraction(f['physical_angle_strip']))
    H=up(d['full_strict_phase_modulus'])
    RP=up(d['full_both_sides_Pmh_integral'])
    # Existing proof supplies all 24 derivatives and their actual reciprocal
    # phase denominator. Its formulas are now applied to x=4*theta.
    oldcross=composition_constants(CJ,flow_width)
    B24=oldcross['cross_constant'](arb(1),constant=True)
    Bh24=oldcross['cross_constant'](H)
    # Real H'>=1/CJ and full complex |H'|<=CJ on flow_width imply
    # Re H'>=1/(2*CJ) on this genuine smaller strip. Cauchy pays H''.
    cross_strip=(flow_width/(4*CJ**2)).lower()
    cross_real_derivative=(1/(2*CJ)).lower()
    endpoint=Ms[-1];epmu=mumin[-1];epm=mp[-1]
    initfield=epm*endpoint['Fcal']*endpoint['a']/(2*epmu)
    momfield=CJ*endpoint['Fcal']*endpoint['a']/(2*epmu**2)
    out=dict(kind='actual_complete_215_cell_strict_scaled_strong_operator',
        complete=False,proved=False,source_sha256=sha(__file__),bits=a.bits,
        inputs={str(p):sha(p) for p in (a.strict,a.fields,a.graph)},identity=si,
        exact_physical_interval=d['exact_physical_interval'],
        actual_full_fourier_lattice=lattice,
        exact_physical_momentum='p=a*u_r+b*u_theta, unchanged',
        exact_physical_Lambda='Lambda_n=max(1,4*abs(n)); its mean is one',
        native_cells_recomputed=0,all_215_original_closed_cells_reused=True,
        true_full_550_segment_ray_certificate_reused=True,
        same_actual_graph_cut_operator_and_parameter_box=True,
        true_energy_ranges={k:[record(x),record(y)] for k,(x,y) in rr.items()},
        original_complete_energy_map=matrix_record(A),
        comparison_diagonal=[record(A[j,j].real) for j in range(11)],
        diagonal_log_integrals=[record(v.upper()) for v in logdiag],
        full_base_diagonal_log_upper=record(base_integral.upper()),
        full_first_characteristic_log_upper=record(char_integral.upper()),
        zeroth_diagonal_comparison_exponential=record(base_integral.exp().upper()),
        tenth_diagonal_comparison_exponential=record(logdiag[-1].exp().upper()),
        comparison_diagonal_is_not_a_lower_bound_on_true_PDE=True,
        norm_scale_cannot_remove_the_diagonal_comparison_exponent=True,
        full_phase=record(H),full_Pmh_integral=record(RP),
        normalized_flow_strip=record(flow_width),normalized_field_strip=record(field_width),
        true_relative_flow_derivative_and_inverse=record(CJ),
        full_twenty_four_IBP_constant=record(B24),full_h_twenty_four_IBP_constant=record(Bh24),
        true_positive_real_derivative_cross_strip=record(cross_strip),
        true_complex_cross_derivative_real_lower=record(cross_real_derivative),
        rows=[],full_mean_full_sources_and_all_intermediate_head_paths_retained=True,
        physical_source='L1(dr;H_N^(s-1/2)) of the unchanged ordinary physical source',
        exact_strong_model='the same full actual R46 W0 with S_sigma,h_sigma and original physical Lambda',
        full_returned_Rstar_proved=False,effective_R104_feedback_cutoff_proved=False,
        dependencies={n:sha(Path(__file__).with_name(n)) for n in (
            'fourfold_negative_root_physical_graph_operator.py',
            'fourfold_strict_complete_R46_budget.py',
            'fourfold_strict_high_energy_triangular.py',
            'fourfold_negative_canonical_cancellation_chart.py',
            'fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py')})
    for N in a.scales:
        scale=arb(4*N)
        scaled=acb_mat([[A[i,j]/scale**(i-j) if j<=i else 0
                        for j in range(11)] for i in range(11)])
        diagonal=acb_mat([[scaled[i,j] if i==j else 0 for j in range(11)] for i in range(11)])
        off=scaled-diagonal
        hmin=min(rr['lambda'][0],scale**2*rr['gamma'][0],rr['alpha'][0]).lower()
        hmax=max(rr['lambda'][1],scale**2*rr['gamma'][1],rr['alpha'][1]).upper()
        eq=(hmax/hmin).sqrt().upper()
        energy=[];diagbounds=[];offbounds=[]
        for k in range(11):
            energy.append((eq*positive_matrix_bound(weighted_principal(scaled,k))).upper())
            diagbounds.append((eq*positive_matrix_bound(weighted_principal(diagonal,k))).upper())
            offbounds.append((eq*positive_matrix_bound(weighted_principal(off,k))).upper())
        E=max(energy).upper()
        comp=compositions(N,CJ,flow_width)
        Nc=comp['uniform']
        Mm=mult(N,Fraction(21,2),max(mp),field_width)
        Mr=mult(N,Fraction(21,2),max(mup).sqrt(),field_width)
        Mt=mult(N,Fraction(21,2),max(tp),field_width)
        u=arb(2)**(arb(1)/4)*Mm
        frame=(u*u+(Mt*u+scale.sqrt()*Mr)**2).sqrt().upper()
        iframe=(scale*Mr*Mr+arb(2).sqrt()*Mm*Mm*(1+Mt*Mt)).sqrt().upper()
        defect=(arb(2)**(arb(3)/4)*mult(N,Fraction(19,2),initfield,field_width)).upper()
        residual=(4*arb(2)**(arb(1)/4)*Nc*mult(N,Fraction(19,2),RP,flow_width)).upper()
        Cerr=(iframe*E*(defect+residual+frame)+1).upper()
        X1ibp=scaled_ibp_cross(N,B24,9,2,Nc)
        Xhibp=scaled_ibp_cross(N,Bh24,10,1,mult(N,10,H,flow_width)*Nc)
        X1analytic=cross_bound(N,cross_strip,cross_real_derivative,arb(1),9,2,Nc)
        Xhanalytic=cross_bound(N,cross_strip,cross_real_derivative,H,10,1,
                              mult(N,10,H,flow_width)*Nc)
        X1=min(X1ibp,X1analytic);Xh=min(Xhibp,Xhanalytic)
        X=(scale.sqrt()*(arb(2)**(arb(1)/4)*X1+arb(2)**(arb(3)/4)*Xh)).upper()
        Lmom=(2*mult(N,Fraction(19,2),momfield,flow_width)*Nc).upper()
        # Physical lag is 4*l. The safe complete Peetre fee is 2*4=8.
        ordering=(8*H*complete_moment(N,flow_width,10,1)).upper()
        Qbound=(arb(2)**(arb(1)/4)*scale.sqrt()*Nc).upper()
        R2=(Cerr+4*(2*X+Lmom+Qbound*ordering)).upper()
        Cfull=(iframe*E*frame).upper()
        Sfull=(iframe*E).upper()
        W0=max(arb(1),Qbound*(1+mult(N,11,H,flow_width))).upper()
        row=dict(scale=N,physical_derivative_scale=4*N,
            complete_scaled_energy_map=matrix_record(scaled),
            energy_equivalence=record(eq),energy_weights=[record(hmin),record(hmax)],
            half_integer_full_Cauchy={str(Fraction(2*k+1,2)):record(v) for k,v in enumerate(energy)},
            half_integer_diagonal_comparison_only={str(Fraction(2*k+1,2)):record(v) for k,v in enumerate(diagbounds)},
            half_integer_off_diagonal_comparison_only={str(Fraction(2*k+1,2)):record(v) for k,v in enumerate(offbounds)},
            full_Cauchy_window=['-21/2','21/2'],full_Cauchy=record(E),
            composition_integer_positive=[record(v) for v in comp['positive']],
            composition_integer_negative=[record(v) for v in comp['negative']],
            complete_scaled_composition_matrix=matrix_record(comp['matrix']),
            full_normal_frame=record(frame),full_inverse_normal_frame=record(iframe),
            full_initial_momentum_defect=record(defect),full_ordinary_residual_budget=record(residual),
            full_source_and_mean_correction=record(Cerr),full_cross_and_mean_output=record(X),
            independent_cross_bounds={key:record(value) for key,value in dict(
                unit_IBP=X1ibp,h_IBP=Xhibp,unit_analytic=X1analytic,h_analytic=Xhanalytic).items()},
            full_remaining_momentum_term=record(Lmom),full_ordering_fee=record(ordering),
            full_amplitude_and_inverse=record(Cfull),full_W0_bound=record(W0),
            full_ordinary_physical_source=record(Sfull),full_strong_R2=record(R2),
            strong_window=[-8,8],amplitude_window=[-10,10],proved=True)
        out['rows'].append(row)
        print(dict(N=N,Cauchy=E.str(9),diagonal=diagbounds[-1].str(9),
            off_diagonal=offbounds[-1].str(9),R2=R2.str(9)),flush=True)
    out.update(complete=True,proved=True,seconds=time.monotonic()-tick,
        scope='Full actual strict R46 propagation, physical ordinary source and strong two-derivative remainder at complete norm scales, reusing every original native cell. The diagonal characteristic-supremum growth is displayed and is not removed by scaling. It is a comparison-bound limitation, not a true-solution lower bound.')
    save(a.out,out)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),seconds=out['seconds']),flush=True)


if __name__=='__main__':
    main()

