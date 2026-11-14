#!/usr/bin/env python3
"""Consume actual R111 full-cap comparison in the paid R105 retained block.

This proves only the six-dimensional retained model with its finite angular
core and the complete cap response. The omitted core channels and the full
infinite feedback Schur complement are not certified by this program.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

from flint import arb, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    p = Path(path)
    raw = p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix == '.gz' else raw)


def verify_reference(entry):
    if sha(entry['path']) != entry['sha256']:
        raise ValueError('Changed full input: ' + entry['path'])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--retained', type=Path, required=True)
    ap.add_argument('--cap-comparison', type=Path, required=True)
    ap.add_argument('--bits', type=int, default=256)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    ctx.prec = args.bits
    low, cap = read(args.retained), read(args.cap_comparison)
    scripts = Path(__file__).parent

    if (low.get('kind') != 'actual_even_retained_core_cap_block_with_center_cap_scope'
            or not low.get('complete')
            or not low.get('actual_center_retained_block_inverse_certified')
            or not low.get('uniform_family_with_cap_frozen_at_center_certified')
            or low.get('source_sha256') != sha(scripts/'fourfold_phase_even_low_paid_core.py')):
        raise ValueError('Need the completed actually paid six-dimensional block')
    for entry in low['input_reports'] + low['input_arrays'] + [low['arrays']]:
        verify_reference(entry)
    for name, digest in low['dependency_sha256'].items():
        if sha(scripts/name) != digest:
            raise ValueError('Changed retained-model dependency: ' + name)
    if not (low['paired_angular_mean_retained'] and
            low['paired_regular_trace_and_flux_retained'] and low['dimension'] == 6):
        raise ValueError('The actual mean or regular port has been lost')

    if (not cap.get('complete') or not cap.get('cap_form_comparison_complete')
            or cap.get('collector_sha256') != sha(scripts/'fourfold_phase_cap_parameter_collect.py')
            or cap.get('source_sha256') != sha(scripts/'fourfold_phase_cap_parameter_comparison.py')
            or cap.get('exact_body_interval') != ['1/4', '3']
            or cap.get('exact_graft_interval') != ['3', '25/8']):
        raise ValueError('Need the full executed R111 collector, not a receipt or prefix')
    for entry in cap['body_input_manifests']:
        verify_reference(entry)
    if sha(cap['paid_graft_path']) != cap['paid_graft_sha256']:
        raise ValueError('Changed paid graft input')
    for name, digest in cap['dependency_sha256'].items():
        if sha(scripts/name) != digest:
            raise ValueError('Changed cap dependency: ' + name)

    if (low['object_sha256'] != cap['object_sha256']
            or Fraction(low['exact_center_parameter']) != Fraction(cap['exact_center'])
            or list(map(Fraction, low['exact_parameter_interval'])) !=
               list(map(Fraction, cap['exact_parameter_interval']))):
        raise ValueError('The retained model and full cap are not the same exact family')
    eps = exact_arb(Fraction(cap['uniform_relative_form_bound']))
    if not 0 <= arb(cap['maximum_relative_form_error']['ball']) <= eps < 1:
        raise ValueError('Unpaid or invalid whole-cap relative form error')
    inv = arb(low['actual_center_retained_block_inverse_upper']['ball']).upper()
    cap_norm = arb(low['true_center_cap_cosine_norm_upper']['ball']).upper()
    if not inv > 0 or not cap_norm >= 0:
        raise ValueError('Invalid retained inverse or complete cap norm')

    # The old cap uncertainty is already paid in inv. R111 adds only this
    # new form-change fee, in the exact isometric grounded paired-cap basis.
    added_fee = (eps * cap_norm).upper()
    product = (inv * added_fee).upper()
    if not product < 1:
        raise ValueError('The actual whole-cap variation exhausts the remaining inverse margin')
    final = (inv / (1 - product)).upper()
    remaining = (1/inv - added_fee).lower()
    report = dict(
        kind='actual_complete_parameter_six_dimensional_retained_model',
        complete=True, source_sha256=sha(__file__), bits=args.bits,
        exact_center_parameter=low['exact_center_parameter'],
        exact_parameter_interval=low['exact_parameter_interval'],
        object_sha256=low['object_sha256'], dimension=6, physical_cut='1/4',
        input_reports=[dict(path=str(p), sha256=sha(p))
                       for p in (args.retained, args.cap_comparison)],
        uniform_cap_relative_form_bound=ball_record(eps),
        complete_cap_norm_upper=ball_record(cap_norm),
        previously_paid_inverse_upper=ball_record(inv),
        added_true_cap_parameter_fee=ball_record(added_fee),
        new_Banach_product=ball_record(product),
        entire_actual_parameter_family_retained_model_certified=True,
        retained_model_inverse_upper=ball_record(final),
        remaining_absolute_retained_error_allowance=ball_record(remaining),
        original_cap_radius_not_paid_twice=True,
        grounded_paired_cap_injection_is_exact_isometry=True,
        paired_angular_mean_retained=True,
        paired_regular_trace_and_flux_retained=True,
        full_cap_response_in_retained_inputs=True,
        omitted_core_height_channels_paid=False,
        infinite_high_feedback_paid=False,
        rigorous_full_Schur_inverse=False,
        nonlinear_family_complete=False,
        scope='Exact coefficients and the whole real parameter interval in the '
              'six-dimensional retained model. The core is the certified finite '
              'angular ODE; its omitted-channel residuals and the full infinite '
              'feedback are separate obligations. The complete positive cap '
              'response and genuine Robin/regular ports are retained.',
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps({k:report[k] for k in ('complete',
        'added_true_cap_parameter_fee', 'new_Banach_product',
        'retained_model_inverse_upper', 'rigorous_full_Schur_inverse')},indent=2))


if __name__ == '__main__':
    main()
