#!/usr/bin/env python3
"""Integrate completed R80 local source bounds against physical time.

The whole fixed reference has q=Y_x != 0 on a proved complex label strip.
Each radial leaf supplies f_p/f_pp for its entire possible s=r/t(p) range.
The arcsin time envelopes may overlap; counting overlaps increases the bound.
No sign or nonzero mean parameter twist is inferred.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
import time
from flint import arb, ctx

from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_saved_circle_field_multidomain_budget import read, upper
from fourfold_forward_density_pipeline import save, lower


def integrate(source, qsummary, descriptor):
    if not (source.get('complete') and source.get('complete_real_core_parameter_source_proved')
            and source.get('negative_half_and_both_branch_signs_included_by_exact_reflection')
            and source.get('all_closed_bulk_cells_exactly_covered')):
        raise ValueError('completed full actual parameter-source coverage required')
    if not (qsummary.get('complete') and qsummary.get('all_550_segments_passed')
            and qsummary['identity']['leg'] == 'forward'):
        raise ValueError('completed full forward q certificate required')
    if (source['center_object_sha256'] != descriptor['target_object']['sha256']
            or source['exact_center_parameter'] != descriptor['target_exact_delta_fraction']):
        raise ValueError('parameter source and fixed reference use different actual centers')
    constants = qsummary['verified_simple_constants']
    S, qmin, qmax = map(Fraction, (constants['label_strip'], constants['real_part_lower'],
                                  constants['modulus_upper']))
    if not qmin > 0 or not qmax > 0 or not qmax*S < Fraction(source['physical_theta_strip']):
        raise ValueError('reference image or denominator is outside the paid parameter source')
    s0 = Fraction(source['fixed_s_turn_split'])
    if not 0 < s0 < 1 or source['turn']['fixed_s_interval'] != [str(s0), '1']:
        raise ValueError('the complete true turn collar has another normalized range')
    radial = [tuple(map(Fraction,row['exact_radial_interval'])) for row in source['rows']]
    expected = tuple(map(Fraction, source['exact_positive_bulk_radial_cover']))
    if (not radial or radial[0][0] != expected[0] or radial[-1][1] != expected[1]
            or any(a >= b for a,b in radial)
            or any(a[1] != b[0] for a,b in zip(radial,radial[1:]))):
        raise ValueError('actual closed radial leaves do not form the stated exact cover')
    keys = ('physical_field_parameter_first_upper', 'physical_field_parameter_second_upper')
    total = [arb(0), arb(0)]
    time_cover, ledger = arb(0), []
    for index,row in enumerate(source['rows']):
        # Clipping uses the independently known physical 0 <= s <= s0.
        lo = max(Fraction(0), Fraction(str(lower(row['fixed_s_interval']).fmpq())))
        hi = min(s0, Fraction(str(upper(row['fixed_s_interval']).fmpq())))
        if not 0 <= lo <= hi <= s0:
            raise ValueError('invalid ordinary actual normalized-time envelope')
        length = (exact_arb(hi).asin()-exact_arb(lo).asin()).upper()
        contributions = [(2*length*upper(row[key])).upper() for key in keys]
        total = [a+b for a,b in zip(total,contributions)]
        time_cover += 2*length
        ledger.append(dict(index=index,exact_radial_interval=row['exact_radial_interval'],
            positive_time_length_upper=ball_record(length),
            both_halves_source_integrals=list(map(ball_record,contributions))))
    turn_length = (arb.pi()/2-exact_arb(s0).asin()).upper()
    turn = [(2*turn_length*upper(source['turn'][key])).upper() for key in keys]
    total = [(a+b).upper() for a,b in zip(total,turn)]
    time_cover = (time_cover+2*turn_length).upper()
    B = [(v/exact_arb(qmin)).upper() for v in total]
    global_only = [(arb.pi()*upper(source['global_bounds'][key])/exact_arb(qmin)).upper()
                   for key in keys]
    return dict(
        proved_integrated_actual_parameter_density_moduli=True,
        exact_parameter_interval=source['exact_parameter_interval'],
        exact_center_parameter=source['exact_center_parameter'],
        label_strip=str(S),reference_q_real_lower=str(qmin),
        reference_q_modulus_upper=str(qmax),
        reference_physical_image_upper=str(qmax*S),
        actual_source_physical_strip=source['physical_theta_strip'],
        formula='B_i <= sum_leaf 2*(asin(s_hi)-asin(s_lo))*sup|f_(p^i)| / qmin; turn included',
        physical_time_cover_length_upper=ball_record(time_cover),
        true_integrated_physical_source_moduli=list(map(ball_record,total)),
        true_integrated_reference_density_moduli=dict(B1=ball_record(B[0]),B2=ball_record(B[1])),
        global_max_only_comparison=dict(B1=ball_record(global_only[0]),B2=ball_record(global_only[1])),
        ordinary_leaf_count=len(ledger),ordinary_leaves=ledger,
        turn=dict(positive_time_length_upper=ball_record(turn_length),
                  both_halves_source_integrals=list(map(ball_record,turn))),
        limitations=['Upper moduli only: these numbers do not provide a signed mean or twist.',
            'Reference Y and q are fixed throughout the actual parameter interval.',
            'No extra factor 4: g_i=h*f_(p^i)/q is the normalized-label coordinate velocity.',
            'The current g0 residual A and all finite forcing errors E_i remain separate inputs.'])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    base=Path('data/phase_ring_continuation')
    parser.add_argument('--source',type=Path,
        default=base/'type_fixed_step02_d5_step5_fixed_tau_parameter_source_full.json.gz')
    parser.add_argument('--q-summary',type=Path,
        default=Path('notes/2026-11-12-step5-forward-reference-derivative-complete-summary.json'))
    parser.add_argument('--descriptor',type=Path,default=base/'step5_retargeted_reference/descriptor.json')
    parser.add_argument('--bits',type=int,default=192)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();ctx.prec=args.bits
    tic,cpu=time.monotonic(),time.process_time()
    source,qsummary,descriptor=map(read,(args.source,args.q_summary,args.descriptor))
    if (sha(qsummary['report']) != qsummary['report_sha256']
            or sha(args.descriptor) != qsummary['identity']['retarget_descriptor_sha256']):
        raise ValueError('fixed reference q report or descriptor identity changed')
    result=integrate(source,qsummary,descriptor)
    result.update(kind='R82_full_forward_integrated_actual_parameter_source_budget',complete=True,
        source_sha256=sha(__file__),bits=args.bits,
        R80_report_sha256=sha(args.source),q_summary_sha256=sha(args.q_summary),
        q_report_sha256=qsummary['report_sha256'],descriptor_sha256=sha(args.descriptor),
        cpu_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-tic)
    save(args.out,result)
    print({k:result[k] for k in ('true_integrated_reference_density_moduli',
        'global_max_only_comparison','physical_time_cover_length_upper')},flush=True)


if __name__=='__main__':main()
