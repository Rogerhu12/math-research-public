#!/usr/bin/env python3
"""Directed actual low-fourfold exterior Robin entries, with mean kept apart.

The input is the complete R74 exterior realization. Its good-tail theorem
supplies the true infinite-mode boundary line. Formula (74.20) is used with
the complete actual entrance intervals; the exponentially small difference
is included for every mode other than the exactly matched fourth mode.
This does not solve the intervening positive body or the central low block.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from flint import arb, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def interval(record):
    return arb(record['lower']).lower().union(arb(record['upper']).upper())


def finite_tail_entries(graft_path, certificate_path, common_path, modes):
    graft, exterior, common = [json.loads(Path(p).read_text())
                              for p in (graft_path, certificate_path, common_path)]
    if not graft.get('complete') or not exterior.get('complete'):
        raise ValueError('the full graft and infinite exterior must be complete')
    if exterior.get('kind') != 'actual_exterior_full_frequency_Robin_and_augmented_positive_domain':
        raise ValueError('wrong actual exterior realization')
    if sha(graft_path) not in exterior['input_sha256'].values():
        raise ValueError('the exterior certificate does not bind this exact graft')
    for key in ('origin_inputs_sha256', 'direction_sha256', 'exact_parameter_interval'):
        if graft[key] != exterior[key]:
            raise ValueError('the finite body and exterior inputs differ')
    outer = list(map(Fraction, exterior['exact_parameter_interval']))
    requested = list(map(Fraction, common['chosen_closed_interval']))
    center, radius = Fraction(common['delta5']), Fraction(common['chosen_radius'])
    if requested != [center-radius, center+radius] or not (
            outer[0] <= requested[0] < requested[1] <= outer[1]):
        raise ValueError('the exact common parameter interval exceeds the exterior input')
    entry = graft['exact_radial_entrance']
    a, z, omega = [interval(entry[name]) for name in ('radius', 'height', 'normalized_omega')]
    if not (a > 0 and z > 0 and omega > arb(7)/5 and omega < arb(3)/2):
        raise ValueError('actual R74 entrance conditions failed')
    A0 = 4*omega+a*a/z
    length = Fraction(exterior['unmodified_length'])
    if length != Fraction(exterior['barrier_length'])-Fraction(25, 8) or length < 64:
        raise ValueError('infinite-tail unmodified length is inconsistent')
    # Monotone m>=4 estimate; retain a convenient exact dyadic cap rather
    # than turning the true exponentially small term into zero.
    full_tail_error = (arb(2)**42*(-8*omega.lower()*exact_arb(length)).exp()).upper()
    if not full_tail_error < arb(2)**(-100):
        raise ValueError('the actual infinite-tail fee is too large')
    rows = []
    for k in range(1, modes+1):
        m = 4*k
        stable = (1+4*m*omega/A0)/(A0+4*omega/m)
        fee = arb(0) if k == 1 else m*arb(2)**(-100)
        true = stable+arb(0, fee.upper())
        if not true > 0:
            raise ValueError('an actual exterior DN entry lost positivity')
        rows.append(dict(normalized_mode=k, physical_frequency=m,
            stable_line=ball_record(stable), true_infinite_tail_fee=ball_record(fee),
            true_Robin=ball_record(true),
            exactly_matched_fourth_mode=(k == 1), negative_mode='same real entry by conjugacy'))
    return dict(kind='directed_true_infinite_exterior_finite_fourfold_Robin_entries',
        complete=True, source_sha256=sha(__file__),
        input_sha256={str(p):sha(p) for p in (graft_path, certificate_path, common_path)},
        origin_inputs_sha256=graft['origin_inputs_sha256'],
        direction_sha256=graft['direction_sha256'],
        exact_parameter_interval=list(map(str, requested)),
        enclosing_exterior_parameter_interval=list(map(str, outer)),
        physical_regular_cut='25/8', physical_angle='theta, period 2*pi',
        fourfold_frequency_convention='m=4*abs(k)',
        entrance={name:ball_record(value) for name, value in
                  dict(a=a, z=z, omega=omega, A0=A0).items()},
        all_nonzero_modes_normalized_true_tail_error=ball_record(full_tail_error),
        regular_mean=dict(form_value='Gamma_H 1 = 0', input='actual regular mean xi',
            output='actual regular mean flux lambda',
            instruction='keep both finite slots; Gamma_H 1=0 does not eliminate the lambda row'),
        entries=rows,
        scope=['Every entry encloses the true infinite exterior, not an imposed stable boundary condition.',
               'The fourth physical mode uses exact matching; all other displayed modes retain the true-tail fee.',
               'Physical-to-shear and canonical boundary changes are separate exact operations.',
               'No positive-body DN or full central low-block inverse is asserted.'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--graft', type=Path, default=Path('notes/2026-11-12-positive-family-natural-graft.json'))
    parser.add_argument('--certificate', type=Path, default=Path('notes/2026-11-12-actual-exterior-robin-certificate.json'))
    parser.add_argument('--common', type=Path, default=Path('notes/2026-11-12-common-core-exterior-parameter-interval.json'))
    parser.add_argument('--modes', type=int, default=8)
    parser.add_argument('--bits', type=int, default=256)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.modes < 1:
        raise ValueError('at least one nonzero fourfold mode required')
    ctx.prec = args.bits
    report = finite_tail_entries(args.graft, args.certificate, args.common, args.modes)
    report['bits'] = args.bits
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(complete=True, modes=args.modes, sha256=sha(args.out),
        gamma4=report['entries'][0]['true_Robin']['ball'],
        gamma_last=report['entries'][-1]['true_Robin']['ball'])), flush=True)


if __name__ == '__main__':
    main()
