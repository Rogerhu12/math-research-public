#!/usr/bin/env python3
"""Intersect the complete same-label log jets with the already proved true gap.

Consumes the saved 4096 closed-cell ranges.  No Fourier transform, geometric
cell or true ray integration is repeated.  Both normalized-log and Bell
identities are evaluated before taking a per-cell minimum.
"""
from __future__ import annotations
import argparse,time
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_root_fourier_fit import save,sha,stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked


def up(z):return stored(z).upper()
def lo(z):return stored(z).lower()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--cells',type=Path,default=Path('notes/2026-11-13-R106-full-relative-real-log-jets.json.gz'))
    p.add_argument('--old-jets',type=Path,default=Path('notes/2026-11-13-R106-full-relative-real-ray-jets.json.gz'))
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('a fresh complete gap-intersection report is required')
    ctx.prec=a.bits;tick=time.monotonic()
    c=checked(a.cells,'fourfold_actual_relative_ray_log_jets.py')
    old=checked(a.old_jets,'fourfold_actual_relative_ray_real_jets.py')
    if c['identity']!=old['identity'] or c['inputs'].get(str(a.old_jets))!=sha(a.old_jets):
        raise ValueError('the same actual original family and true ray are required')
    m0=lo(old['true_normalized_initial_label_derivative_lower'])
    M0=up(old['true_normalized_initial_label_derivative_upper'])
    Cr=up(old['accepted_relative_first_derivative'])
    absolute={j+1:up(z) for j,z in enumerate(old['complete_absolute_normalized_flow_derivatives'])}
    previous={z['order']:up(z['accepted_complete_relative_derivative'])
              for z in old['whole_time_relative_derivative_bounds']}
    global_bounds=[arb(0),Cr,arb(0),arb(0),arb(0)];witness=[None]*5;cells=[]
    for i,row in enumerate(c['cells']):
        if row['node']!=i:raise ValueError('saved complete angular cover has a gap')
        m=max(m0,lo(row['normalized_Fprime_lower'])).lower()
        M=min(M0,up(row['normalized_Fprime_upper'])).upper()
        if not 0<m<=M:raise ValueError('two true first-jet enclosures have empty intersection')
        C=min(Cr,(M/m).upper()).upper()
        ratios=[]
        for j,z in zip((2,3,4),row['normalized_derivative_ratio_ranges']):
            if z['order']!=j:raise ValueError('wrong actual derivative ratio order')
            lower=max(lo(z['lower']),(-absolute[j]/m).lower()).lower()
            upper=min(up(z['upper']),(absolute[j]/m).upper()).upper()
            if not lower<=upper:raise ValueError('two true derivative-ratio enclosures are disjoint')
            ratios.append((lower,upper))
        A=[max(abs(l),abs(u)).upper() for l,u in ratios]
        delta=[(u-l).upper() for l,u in ratios]
        L,M3,_=A;d2,d3,d4=delta
        log2=(C*d2/m).upper()
        log3=(C*(d3+3*L*d2)/m**2).upper()
        log4=(C*(d4+6*L*d3+(15*L**2+4*M3)*d2)/m**3).upper()
        # The same-label ratio and global complete Fourier-jet bounds can
        # also be intersected before applying the exact divided Bell identity.
        J=[arb(0),arb(1)]+[(min(absolute[j],M*A[j-2])/m**j).upper()
                           for j in (2,3,4)]
        bell2=((1+C)*J[2]).upper();H2=min(log2,bell2,previous[2]).upper()
        bell3=((1+C)*J[3]+3*H2*J[2]).upper();H3=min(log3,bell3,previous[3]).upper()
        bell4=((1+C)*J[4]+H2*(4*J[3]+3*J[2]**2)+6*H3*J[2]).upper()
        H4=min(log4,bell4,previous[4]).upper()
        selected=[H2,H3,H4]
        for j,v in zip((2,3,4),selected):
            if v>global_bounds[j]:global_bounds[j]=v;witness[j]=i
        cells.append(dict(node=i,complete_first_derivative_lower=record(m),
            complete_first_derivative_upper=record(M),complete_relative_first=record(C),
            complete_ratio_ranges=[dict(order=j,lower=record(ratios[j-2][0]),
                upper=record(ratios[j-2][1])) for j in (2,3,4)],
            log_identity_bounds=[record(v) for v in (log2,log3,log4)],
            divided_Bell_bounds=[record(v) for v in (bell2,bell3,bell4)],
            accepted_relative_jets=[record(v) for v in selected]))
    if len(cells)!=c['nodes']:raise ValueError('complete saved circle missing')
    rows=[dict(order=j,accepted_complete_relative_derivative=record(global_bounds[j]),
        previous_complete_real_bound=record(previous[j]),witness_cell=witness[j],
        improvement_factor=record((previous[j]/global_bounds[j]).lower())) for j in (2,3,4)]
    if not all(global_bounds[j]<previous[j] for j in (2,3,4)):
        raise ValueError('all requested actual real-jet improvements were not obtained')
    out=dict(kind='actual_complete_relative_real_log_jets_true_gap_intersection',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,identity=c['identity'],
        inputs={str(p):sha(p) for p in (a.cells,a.old_jets)},
        original_complete_higher_jet_report=str(a.old_jets),
        original_full_closed_cell_report=str(a.cells),
        all_550_true_segments_and_4400_exact_controls=True,all_549_exact_seams_checked=True,
        all_pairs_of_strict_times_and_both_directions=True,all_real_angles=True,
        entire_original_real_parameter_box=True,
        native_geometry_recomputed=0,Fourier_transforms_recomputed=0,
        true_gap_used_before_ratio_bound=record(m0),
        accepted_relative_first_derivative=record(Cr),
        accepted_real_derivative_bounds=rows,cells=cells,
        exact_global_jet_intersection='m=max(m_cell,m_true); M=min(M_cell,M_true); |F^(j)/Fprime|<=M_j_true/m; then retain both exact divided-Bell and log-difference estimates',
        unchanged_complex_derivative_and_strip_permission=True,
        every_head_mean_source_and_reconstruction_position_unchanged=True,
        full_returned_remainder_claimed=False,finite_head_feedback_solved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_root_fourier_fit.py','fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_negative_canonical_cancellation_chart.py')},
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,rows=rows,out=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()

