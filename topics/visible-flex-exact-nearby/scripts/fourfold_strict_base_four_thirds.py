#!/usr/bin/env python3
"""The same complete strict WKB error at the two actual base 4/3 windows.

Pay the physical Cauchy correction at its output index t=s+4/3,
not at s+2. All four source/momentum branches, the full mean and all
cross-cone frequencies remain. The complete existing R2 theorem supplies
the exact residual identity, not a silently projected error.
"""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_root_fourier_fit import save,sha,stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked
from fourfold_negative_root_physical_graph_operator import mult,complete_moment
from fourfold_strict_windowed_density_R46 import real_refined_compositions,true_cross,ceiling
from fourfold_strict_complete_R46_budget import composition_constants
from fourfold_strict_scaled_complete_R46_budget import scaled_ibp_cross,matrix_record


def up(row):return stored(row).upper()
def lo(row):return stored(row).lower()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--windowed',type=Path,default=Path('notes/2026-11-13-R46-windowed-density-strong-budget.json'))
    p.add_argument('--fields',type=Path,default=Path('notes/2026-11-13-R46-native-WKB-full-strict-fields-v2.json.gz'))
    p.add_argument('--scale',type=int,default=1048576)
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('a new report path is required')
    ctx.prec=a.bits;tick=time.monotonic()
    d=checked(a.windowed,'fourfold_strict_windowed_density_R46.py')
    f=checked(a.fields,'fourfold_strict_actual_wkb_fields.py')
    if d['identity']!=f['identity'] or d['inputs'].get(str(a.fields))!=sha(a.fields):
        raise ValueError('the same complete original 215 fields are required')
    if len(f['cells'])!=215 or not d['all_215_original_cells_reused']:
        raise ValueError('the complete actual cover is missing')
    N=a.scale;row=next(x for x in d['rows'] if x['scale']==N)
    amplitudes={Fraction(x['window']):x for x in row['complete_amplitude_windows']}
    Cr=up(d['real_relative_derivative']);Cc=up(d['unchanged_complex_relative_derivative'])
    X=lo(d['unchanged_normalized_complex_flow_strip']);Xf=lo(d['normalized_field_strip'])
    ac=lo(d['complete_positive_real_cross_strip'])
    cc=lo(d['complete_cross_complex_derivative_real_lower'])
    H=up(d['actual_full_phase_modulus']);RP=up(d['actual_full_Pmh_integral'])
    ep=f['cells'][-1];M={k:up(v) for k,v in ep['complete_complex_field_moduli'].items()}
    m=up(ep['geometry']['m_modulus_upper']);mu=lo(ep['geometry']['mu_modulus_lower'])
    defect_field=m*M['Fcal']*M['a']/(2*mu)
    momentum_field=Cc*M['Fcal']*M['a']/(2*mu**2)
    oldcross=composition_constants(Cc,X)
    B24=oldcross['cross_constant'](arb(1),constant=True)
    Bh24=oldcross['cross_constant'](H)
    out=dict(kind='complete_actual_strict_two_base_four_thirds_windows',
        complete=False,proved=False,source_sha256=sha(__file__),bits=a.bits,
        identity=d['identity'],scale=N,inputs={str(x):sha(x) for x in (a.windowed,a.fields)},
        exact_physical_interval=d['exact_physical_interval'],native_cells_recomputed=0,
        unchanged_original_four_branch_model=True,complete_mean_and_all_frequency_crossings=True,
        unchanged_ordinary_physical_scalar_source=True,rows=[],
        physical_frequency='Lambda_n=max(1,4*abs(n)), with full mean one',
        gain='4/3',
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_root_fourier_fit.py','fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_negative_canonical_cancellation_chart.py','fourfold_negative_root_physical_graph_operator.py',
            'fourfold_strict_windowed_density_R46.py','fourfold_strict_complete_R46_budget.py',
            'fourfold_strict_scaled_complete_R46_budget.py')})
    for s in (Fraction(0),Fraction(-4,3)):
        t=s+Fraction(4,3);erow=amplitudes[abs(t)]
        E=up(erow['Cauchy']);I=up(erow['inverse_frame']);F=up(erow['frame'])
        source_order=t-Fraction(1,2)
        degree=ceiling(max(abs(t+Fraction(1,2)),abs(source_order),
                           abs(s+Fraction(1,2)),abs(s+Fraction(3,2))))
        comp=real_refined_compositions(N,Cr,Cc,X,degree);Nc=comp['uniform']
        defect=(arb(2)**(arb(3)/4)*mult(N,abs(source_order),defect_field,Xf)).upper()
        residual=(4*arb(2)**(arb(1)/4)*Nc*mult(N,abs(source_order),RP,X)).upper()
        corr=(I*E*(defect+residual+F)+1).upper()
        p1=ceiling(abs(s+Fraction(1,2)));ph=ceiling(abs(s+Fraction(3,2)))
        X1a=true_cross(N,ac,cc,arb(1),p1,2,Nc)
        Xha=true_cross(N,ac,cc,H,ph,1,mult(N,ph,H,X)*Nc)
        X1b=scaled_ibp_cross(N,B24,p1,2,Nc)
        Xhb=scaled_ibp_cross(N,Bh24,ph,1,mult(N,ph,H,X)*Nc)
        cross=(arb(4*N).sqrt()*(arb(2)**(arb(1)/4)*min(X1a,X1b)
               +arb(2)**(arb(3)/4)*min(Xha,Xhb))).upper()
        momentum=(2*mult(N,abs(source_order),momentum_field,X)*Nc).upper()
        order=(8*H*complete_moment(N,X,ceiling(abs(t)),1)).upper()
        Q=(arb(2)**(arb(1)/4)*arb(4*N).sqrt()*Nc).upper()
        bound=(corr+4*(2*cross+momentum+Q*order)).upper()
        out['rows'].append(dict(input_order=str(s),output_order=str(t),
            physical_Cauchy_output_index=str(t),
            physical_ordinary_source_output_order=str(source_order),
            Cauchy=record(E),frame=record(F),inverse_frame=record(I),
            complete_composition_degree=degree,composition=record(Nc),
            full_composition_matrix=matrix_record(comp['matrix']),
            full_inverse_Jacobian_matrix=matrix_record(comp['inverse_Jacobian_matrix']),
            complete_initial_defect=record(defect),complete_residual=record(residual),
            complete_source_and_mean_correction=record(corr),
            cross_unit_analytic=record(X1a),cross_h_analytic=record(Xha),
            cross_unit_IBP=record(X1b),cross_h_IBP=record(Xhb),
            full_cross_cone_and_mean_output=record(cross),
            full_remaining_momentum=record(momentum),full_ordering=record(order),full_Q=record(Q),
            full_strict_four_thirds=record(bound),proved=True))
        print(dict(input=str(s),output=str(t),Cauchy=E.str(10),R=bound.str(10)),flush=True)
    out.update(complete=True,proved=True,seconds=time.monotonic()-tick,
        scope='The original complete strict C-W0 at 0->4/3 and -4/3->0, with all physical scalar sources, means and four branches. No whole-return, finite Schur or weighted inverse is inferred.')
    save(a.out,out)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()
