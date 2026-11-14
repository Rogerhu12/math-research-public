#!/usr/bin/env python3
"""Sharp endpoint certificate for one actual common spline germ.

The radial path is r=t*sin(tau), with t a certified positive fixed root and
the entire time interval strictly inside (-pi/2,pi/2). Sine is increasing
there. Separate directed endpoint bounds avoid the fixed-radius inflation
introduced by first constructing one wide Arb ball for the whole image.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path
import time

from flint import arb, ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_affine import AffineBulkTarget, sha
from fourfold_phase_field_time_germ_union import (
    certified_root, common_knots, reflected_common_domain,
)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT/'data'/'phase_ring_continuation'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--object', type=Path,
        default=DATA/'type_fixed_step02_d5_exact_affine_step5_object.json')
    parser.add_argument('--root-certificate', type=Path,
        default=DATA/'type_fixed_step02_d5_exact_affine_step5_root_tight.json')
    parser.add_argument('--domain-certificate', type=Path,
        default=DATA/'type_fixed_step02_d5_exact_affine_step5_reference419_whole_angle_time_domain.json')
    parser.add_argument('--germ-index', type=int, default=2)
    parser.add_argument('--bits', type=int, default=192)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    ctx.prec, ctx.cap = args.bits, 24
    domain = json.loads(args.domain_certificate.read_text())
    if (not domain.get('complete')
            or domain['target_object_sha256'] != sha(args.object)
            or domain['target_root_sha256'] != sha(args.root_certificate)):
        raise ValueError('completed domain, graph and root identities must agree')
    selected = domain['germs'][args.germ_index]
    cell = tuple(map(Fraction, selected['common_span']))
    times = list(map(Fraction, domain['exact_time_endpoints']))
    left, right = sorted(times)
    if left == right:
        raise ValueError('zero length time interval')
    a, b = exact_arb(left), exact_arb(right)
    if not (a > -arb.pi()/2 and b < arb.pi()/2):
        raise ValueError('the whole exact time interval must be in the sine monotonicity interval')
    target = AffineBulkTarget(args.object, 256, 256,
        exact_arb(Fraction(3,1000)), exact_arb(Fraction(1,400)),
        exact_arb(Fraction(8,25)))
    if Fraction(domain['exact_delta_fraction']) != target.affine_delta:
        raise ValueError('different exact affine parameter')
    root = certified_root(target, args.root_certificate)
    if not root > 0:
        raise ValueError('positive root not certified')
    legal_left, legal_right = reflected_common_domain(target)
    cuts = common_knots(target)
    if (cell not in list(zip(cuts,cuts[1:]))
            or not legal_left <= cell[0] < cell[1] <= legal_right):
        raise ValueError('selected interval is not a valid common physical spline span')
    endpoint_left, endpoint_right = root*a.sin(), root*b.sin()
    radial_lower, radial_upper = endpoint_left.lower(), endpoint_right.upper()
    left_margin = (radial_lower-exact_arb(cell[0])).lower()
    right_margin = (exact_arb(cell[1])-radial_upper).lower()
    cosine_lower = min(a.cos().lower(), b.cos().lower())
    passed = bool(cosine_lower > 0 and left_margin > 0 and right_margin > 0)
    report = dict(kind='sharp_endpoint_certificate_for_one_actual_common_germ',
        proved=passed, source_sha256=sha(__file__),
        object_sha256=sha(args.object), root_certificate_sha256=sha(args.root_certificate),
        domain_certificate_sha256=sha(args.domain_certificate),
        exact_delta_fraction=str(target.affine_delta), bits=args.bits,
        original_oriented_exact_time_endpoints=list(map(str,times)),
        ordered_exact_time_endpoints=list(map(str,(left,right))),
        selected_common_span=list(map(str,cell)), selected_germ_index=args.germ_index,
        certified_positive_root=ball_record(root),
        exact_reflected_common_domain=list(map(str,(legal_left,legal_right))),
        endpoint_radial_enclosures=[ball_record(endpoint_left),ball_record(endpoint_right)],
        sharp_radial_lower_bound=ball_record(radial_lower),
        sharp_radial_upper_bound=ball_record(radial_upper),
        left_strict_margin=ball_record(left_margin),
        right_strict_margin=ball_record(right_margin),
        whole_time_cosine_lower_bound=ball_record(cosine_lower),
        whole_actual_time_interval_in_selected_germ=passed,
        original_coarse_required_spans=domain['required_common_spans'],
        reason='For positive fixed root t, t*sin(tau) is increasing throughout these exact times; '
               'separate endpoint bounds stay strictly inside the selected common span',
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_affine.py','fourfold_phase_field_time_germ_union.py')},
        elapsed_seconds=time.monotonic()-started,
        limitations=['One exact affine point and one exact time interval only',
                     'This certifies actual scalar-germ location, not a new field or flow error',
                     'Other time segments and parameter values require their own endpoint gates'])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({key:report[key] for key in (
        'proved','selected_common_span','left_strict_margin','right_strict_margin',
        'whole_actual_time_interval_in_selected_germ','elapsed_seconds')},indent=2),flush=True)
    if not passed:
        raise SystemExit('sharp endpoint single-germ gate failed')


if __name__ == '__main__':
    main()

