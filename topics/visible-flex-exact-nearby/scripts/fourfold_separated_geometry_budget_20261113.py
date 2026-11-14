#!/usr/bin/env python3
"""Consume the actual complete R78/R79 geometry in independent C0/C1/C2 gates.

This checks a sufficient neighborhood of the already certified reference.
It does not assert that a nonlinear correction in that neighborhood exists.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path

from flint import arb, ctx


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p = Path(p)
    raw = p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix == '.gz' else raw)


def exact(q):
    q = Q(q)
    return arb(q.numerator) / q.denominator


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise ValueError('Use a fresh output path; do not overwrite evidence')
    ctx.prec = 256
    root = Path(__file__).resolve().parent.parent
    paths = [root / 'notes/2026-11-12-actual-closed-reach-certificate.json.gz',
             root / 'notes/2026-11-12-actual-diameter-and-phase-separation.json.gz']
    reach, visible = [read(p) for p in paths]
    if not all(j.get('complete') and not j.get('failed_cells') and
               not j.get('pending') for j in (reach, visible)):
        raise ValueError('A whole completed geometric certificate is required')
    if reach['exact_parameter_interval'] != visible['exact_parameter_interval']:
        raise ValueError('The reach and visible-distance families differ')
    if len(reach['body_cells']) != 1679 or len(reach['graft_cells']) != 64:
        raise ValueError('Unexpected complete R79 cover')
    rg = reach['certified_geometry']
    vg = visible['certified_geometry']
    gates = {}

    def gate(name, condition):
        gates[name] = bool(condition)
        if not gates[name]:
            raise ValueError('Failed actual geometry gate: ' + name)

    sigma, K, D = Q(1, 2), Q(12), Q(2553, 1000)
    distance, holding = Q(13, 100), Q(1932, 1000)
    gate('actual_global_support_above_one_half',
         arb(rg['support_lower']['ball']) > exact(sigma))
    gate('actual_global_curvature_below_twelve',
         arb(rg['principal_curvature_upper']['ball']) < exact(K))
    gate('actual_global_diameter_below_2553_over_1000',
         arb(rg['diameter_upper']['ball']) < exact(D))
    gate('complete_surface_phase_witness_above_13_over_100',
         arb(vg['point_to_complete_surface_distance_lower']['ball']) > exact(distance))
    # R79's far-region support includes both flat caps. On a flat cap it
    # equals its positive height; reflection gives the other cap at -height.
    gate('two_actual_flat_caps_have_diameter_above_1932_over_1000',
         2 * arb(reach['far_geometry']['full_tail_support_lower']['ball']) > exact(holding))
    a, b, c = Q(1, 1000), Q(1, 100), Q(7, 10)
    support = sigma-a-D*b/(1-b)
    inverse_curvature = (1-b)**2/(K+c)
    diameter = D+2*a
    ratio = inverse_curvature/diameter
    held_ratio = (distance-2*a)/diameter
    holding_ratio = (holding-2*a)/diameter
    gate('immersion_margin_positive', 0 <= b < 1)
    gate('support_does_not_limit_reach', support > inverse_curvature > 0)
    gate('reach_over_diameter_above_three_percent', ratio > Q(3, 100))
    gate('visible_motion_above_five_percent', held_ratio > Q(1, 20))
    gate('holding_diameter_above_twenty_percent', holding_ratio > Q(1, 5))
    proof = root / 'results/R123-separated-correction-budgets-and-normal-Hessian.md'
    result = dict(
        kind='actual_reference_separated_geometry_neighborhood', complete=True,
        source_sha256=digest(__file__), proof_sha256=digest(proof),
        input_reports=[dict(path=str(p.relative_to(root)), sha256=digest(p)) for p in paths],
        exact_parameter_interval=reach['exact_parameter_interval'],
        exact_budgets=dict(C0=str(a), intrinsic_C1=str(b),
                           updated_normal_intrinsic_Hessian=str(c)),
        exact_bounds=dict(support_lower=str(support),
                          inverse_curvature_lower=str(inverse_curvature),
                          diameter_upper=str(diameter),
                          reach_over_diameter_lower=str(ratio),
                          held_motion_over_diameter_lower=str(held_ratio),
                          holding_diameter_over_diameter_lower=str(holding_ratio)),
        gates=gates, passed_gate_count=len(gates),
        genuine_material_norms_required=True,
        updated_normal_projection_not_unpaid_old_normal=True,
        actual_nonlinear_correction_produced=False,
        exact_isometric_family_produced=False,
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(complete=True, passed_gate_count=len(gates),
                         exact_bounds=result['exact_bounds']), indent=2))


if __name__ == '__main__':
    main()
