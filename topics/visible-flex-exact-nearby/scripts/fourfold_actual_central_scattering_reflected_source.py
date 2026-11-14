#!/usr/bin/env python3
"""Consume exact radial reflection and the two genuine half-core energy rates.

The two-ended source is linear. For each collar use the shorter reflected
orientation; for a core source split only its physical radial support at zero.
Every native cell, mean, original scalar source and exact overlap extension
is retained. No altered full Cauchy or scattering operator is introduced.
"""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import save,sha,stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked


def up(row):return stored(row).upper()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--scattering',type=Path,default=Path('notes/2026-11-13-actual-central-scattering-and-source.json'))
    p.add_argument('--fields',type=Path,default=Path('notes/2026-11-13-R46-native-WKB-full-strict-fields-v2.json.gz'))
    p.add_argument('--scaled',type=Path,default=Path('notes/2026-11-13-R46-215-cell-scaled-strong-operator.json'))
    p.add_argument('--strict',type=Path,default=Path('notes/2026-11-13-R46-windowed-density-strong-budget.json'))
    p.add_argument('--graph',type=Path,default=Path('notes/2026-11-13-negative-root-physical-graph-operator.json'))
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('a fresh output path is required')
    ctx.prec=a.bits;tick=time.monotonic()
    s=checked(a.scattering,'fourfold_actual_central_scattering_and_source.py')
    f=checked(a.fields,'fourfold_strict_actual_wkb_fields.py')
    old=checked(a.scaled,'fourfold_strict_scaled_complete_R46_budget.py')
    c=checked(a.strict,'fourfold_strict_windowed_density_R46.py')
    g=checked(a.graph,'fourfold_negative_root_physical_graph_operator.py')
    if not s['identity']==f['identity']==old['identity']==c['identity']:
        raise ValueError('actual fields/core/scattering identity changed')
    for name,digest in s['input_theorems'].items():
        if sha(Path('results')/name)!=digest:raise ValueError('actual scattering theorem changed: '+name)
    if s['inputs'].get(str(a.graph))!=sha(a.graph) or s['inputs'].get(str(a.strict))!=sha(a.strict):
        raise ValueError('the same complete graph and core are required')
    N=s['scale'];sr=next(x for x in old['rows'] if x['scale']==N)
    cr=next(x for x in c['rows'] if x['scale']==N)
    gr=next(x for x in g['rows'] if x['scale']==N)
    base=next(x for x in cr['complete_amplitude_windows'] if Fraction(x['window'])==0)
    logs=dict(forward=arb(0),backward=arb(0));cursor=Fraction(0);cells=[]
    for cell in f['cells']:
        left,right=Fraction(cell['left']),Fraction(cell['right'])
        if left!=cursor or not left<right:raise ValueError('actual positive-half cover has a gap')
        cursor=right;length=exact_arb(right-left);fee={}
        for direction in logs:
            v=(length*max(arb(0),up(cell['energy']['base_energy_rate_'+direction]))/2).upper()
            logs[direction]+=v;fee[direction]=record(v)
        cells.append(dict(left=str(left),right=str(right),complete_base_energy_log_fee=fee))
    if len(cells)!=215 or str(cursor)!=s['exact_physical_strict_interval'][1]:
        raise ValueError('the actual whole half-core is missing')
    eq=up(sr['energy_equivalence'])
    Ef=(eq*logs['forward'].exp()).upper();Eb=(eq*logs['backward'].exp()).upper()
    # The negative half-index is the flux adjoint of the opposite time
    # direction. Half-way Hilbert interpolation therefore uses sqrt(Ef*Eb).
    Ehalf=(Ef*Eb).sqrt().upper()
    I=up(base['inverse_frame']);Shalf=(I*Ehalf).upper()
    Ki=up(gr['full_actual_physical_cut_to_root'])
    core=(arb(2).sqrt()*Ki*Shalf).upper()
    columns=s['bounds']['full_two_end_scattering_source_columns']
    root=min(up(columns['left_canonical_root']),up(columns['right_canonical_root'])).upper()
    graph=min(up(columns['left_tilted_graph']),up(columns['right_tilted_graph'])).upper()
    direct_sum=(core*core+2*root*root+2*graph*graph).sqrt().upper()
    out=dict(kind='actual_complete_central_scattering_reflected_short_source_budget',
        complete=True,proved=True,bits=a.bits,source_sha256=sha(__file__),
        identity=s['identity'],scale=N,exact_physical_strict_interval=s['exact_physical_strict_interval'],
        inputs={str(x):sha(x) for x in (a.scattering,a.fields,a.scaled,a.strict,a.graph)},
        actual_reflection_theorem_sha256=sha(Path('results/R77-reflection-square-of-principal-return.md')),
        all_215_native_closed_cells_reused=True,native_cells_recomputed=0,
        half_core_cells=cells,
        actual_half_energy_logs={k:record(v.upper()) for k,v in logs.items()},
        complete_half_core_energy_equivalence=record(eq),
        positive_half_index_forward=record(Ef),positive_half_index_backward=record(Eb),
        negative_half_index_is_opposite_orientation_flux_adjoint=True,
        complete_half_core_physical_P0=record(Ehalf),
        unchanged_base_inverse_normal_frame=record(I),
        complete_half_core_L1_HNminus_half_to_amplitude=record(Shalf),
        actual_reflection_used_for_each_source_column_not_for_an_unproved_reference=True,
        exact_source_partition='strict scalar source f=f*1_(r<0)+f*1_(r>=0), as an L1 density; source signs and graph extensions reflect with the complete equation',
        complete_same_two_ended_scattering_operator=True,
        bounds=dict(scattering_and_inverse=record(arb(1)),
            strict_core_source=record(core),either_canonical_root_source=record(root),
            either_tilted_graph_source=record(graph),five_space_direct_sum_source=record(direct_sum)),
        ordinary_source_spaces=s['ordinary_negative_source_spaces'],
        both_means_and_complete_all_frequency_response_retained=True,
        full_returned_Rstar_proved=False,feedback_inverse_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_negative_canonical_cancellation_chart.py')})
    out['seconds']=time.monotonic()-tick
    save(a.out,out)
    print(dict(complete=True,half_P0=Ehalf.str(10),core=core.str(10),
        either_root=root.str(10),either_graph=graph.str(10),
        complete_direct_sum=direct_sum.str(10),out=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()
