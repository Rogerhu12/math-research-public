#!/usr/bin/env python3
"""Actual-reference time residuals across knots by a finite germ union.

Every common scalar span meeting the certified true radial image is listed.
Its exact polynomial germ is extended to the entire time subspan, where the
frozen time engine proves the full residual and its analytic Cauchy tail.
Taking maxima covers the actual piecewise field without solving any knot
preimage.  No germ extension is asserted to be the actual field off its span.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, acb_series, ctx

from fourfold_phase_beta_interval import array_derivative, series_derivative, ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_affine import AffineBulkTarget, sha
from fourfold_phase_field_time_taylor import FieldTimeModel, truncate, record_complex
from fourfold_phase_reference_time_sample import load_segment, reference_time_coefficients


def common_knots(target):
    return sorted({Fraction.from_float(float(value))*side
                   for key, values in target.frozen.items() if key.endswith('_knots')
                   for value in values for side in (-1, 1)})


def certified_root(target, path):
    certificate = json.loads(Path(path).read_text())
    if (not certificate.get('proved')
            or certificate['origin_inputs_sha256'] != target.affine_definition['origin_inputs']['sha256']
            or certificate['frozen_direction_sha256'] != target.affine_definition['direction']['sha256']
            or Fraction(certificate['exact_delta_fraction']) != target.affine_delta):
        raise ValueError('root certificate and exact affine graph differ')
    root = arb(float(certificate['root_interval'][0])).union(arb(float(certificate['root_interval'][1])))
    if not root > 0:
        raise ValueError('the positive target root is required')
    return root


def physical_splines(target):
    splines = [('base', target.base), ('raw', target.raw), ('shift', target.shift)]
    splines += [(f'mean{j}', sp) for j, sp in enumerate(target.means)]
    splines += [(f'height{j}_primitive', sp) for j, sp in enumerate(target.height_integrals)]
    return splines


def reflected_common_domain(target):
    """Intersection of each actual B-spline domain and its exact reflection."""
    left, right = [], []
    for _, spline in physical_splines(target):
        knots = [Fraction.from_float(float(value)) for value in spline.knots_float]
        degree = int(spline.degree)
        lo, hi = knots[degree], knots[-degree-1]
        left.extend([lo, -hi])
        right.extend([hi, -lo])
    result = max(left), min(right)
    if not result[0] < result[1]:
        raise ValueError('actual scalar domains and their reflections have empty intersection')
    return result


def continuity_gate(target):
    """C2 scalar gluing is enough for continuity of this characteristic field."""
    result = []
    for name, spline in physical_splines(target):
        knots = [Fraction.from_float(float(value)) for value in spline.knots_float]
        multiplicities = Counter(knots)
        degree = int(spline.degree)
        lo, hi = knots[degree], knots[-degree-1]
        interior = [multiplicity for value, multiplicity in multiplicities.items() if lo < value < hi]
        minimum = degree-max(interior, default=0)
        if minimum < 2:
            raise ValueError(f'{name} does not have the required C2 interior gluing')
        result.append(dict(name=name, degree=degree, minimum_interior_continuity=minimum))
    return result


def radial_cover(target, root, tau0, halfwidth):
    tau0, halfwidth = exact_arb(tau0), abs(exact_arb(halfwidth))
    if halfwidth.contains(0) or not abs(tau0)+halfwidth < arb.pi()/2:
        raise ValueError('a strict interior nonzero time interval is required')
    radial = root*(tau0+arb(0, halfwidth.upper())).sin()
    left = Fraction(str(radial.lower().fmpq()))
    right = Fraction(str(radial.upper().fmpq()))
    domain_left, domain_right = reflected_common_domain(target)
    if not domain_left < left < right < domain_right:
        raise ValueError('radial image leaves the intersection of actual scalar domains and reflections')
    cuts = common_knots(target)
    if not cuts[0] < left < right < cuts[-1]:
        raise ValueError('radial image leaves the common scalar domain')
    cells = [(a, b) for a, b in zip(cuts, cuts[1:]) if a <= right and b >= left]
    if (not cells or not cells[0][0] <= left <= right <= cells[-1][1]
            or any(a[1] != b[0] for a, b in zip(cells, cells[1:]))):
        raise ValueError('finite germ list does not cover the whole certified radial image')
    radial_left, radial_right = root*(tau0-halfwidth).sin(), root*(tau0+halfwidth).sin()
    crossed = [knot for knot in cuts if radial_left.upper() < exact_arb(knot) < radial_right.lower()]
    return radial, (left, right), cells, crossed


class FixedGermTimeModel(FieldTimeModel):
    """Frozen field methods, with an explicitly selected analytic scalar germ.

    Unlike FieldTimeModel, the selected span need only meet the true radial
    image.  The mathematical object computed outside it is explicitly the
    polynomial extension, used only as a bound for the portion inside it.
    """
    def __init__(self, object_path, root_certificate, tau_center, time_halfwidth,
                 cell, *, nodes=512, order=16, outer_radius=8,
                 radial_radius=Fraction(3, 1000), E_radius=Fraction(1, 400),
                 tail_sigma=Fraction(8, 25), branch_sign=1):
        if branch_sign not in (-1, 1) or order < 4:
            raise ValueError('invalid branch sign or time jet order')
        self.order, self.precision = int(order), int(order)+1
        self.work_precision = max(21, self.precision+3)
        ctx.cap = self.work_precision
        self.object_path, self.root_certificate = Path(object_path), Path(root_certificate)
        self.tau0, self.h = exact_arb(tau_center), exact_arb(time_halfwidth)
        self.outer = exact_arb(outer_radius)
        self.R0, self.RE, self.sigma = map(exact_arb, (radial_radius, E_radius, tail_sigma))
        self.sign, self.nodes = branch_sign, nodes
        if self.h.contains(0) or not self.outer > 1 or not self.R0 > self.RE > 0:
            raise ValueError('invalid nonzero time scale or analytic radii')
        self.target = AffineBulkTarget(object_path, nodes, nodes, self.R0, self.RE, self.sigma)
        self.root = certified_root(self.target, root_certificate)
        self.radial_range, _, cells, _ = radial_cover(self.target, self.root, tau_center, time_halfwidth)
        self.cell = tuple(map(Fraction, cell))
        if self.cell not in cells:
            raise ValueError('the explicit germ is not one of the required common spans')
        self.target.set_cell(*self.cell)
        self.tau = acb_series([acb(self.tau0), acb(self.h)])
        radial = self.root*self.tau.sin()
        self.center = self.root*self.tau0.sin()
        # This zero constant uses the identical definition r0=root*sin(tau0).
        self.argument = acb_series([0]+[-radial[j]/self.RE for j in range(1, radial.prec)], prec=radial.prec)
        self.radial_image = (abs(self.root)*((abs(self.h)*self.outer).exp()-1)).upper()
        if not self.radial_image < self.RE:
            raise ValueError('the full outer complex time disk leaves the paid radial disk')
        self.budget = self.target.analytic_input_budget(acb(self.center), self.R0, self.sigma, self.RE)
        coefficient, radius, E, C, K = self.target.target(self.center, self.RE, self.budget)
        beta, gamma, _, _ = self.target.scalars(self.center, -self.RE)
        first = array_derivative(coefficient, -self.RE)
        self.X_coefficient = np.empty(first.shape, object)
        for key in np.ndindex(first.shape):
            self.X_coefficient[key] = truncate(first[key](self.argument), self.precision)
        self.beta = [truncate(value(self.argument), self.precision) for value in beta]
        self.gamma = [truncate(value(self.argument), self.precision) for value in gamma]
        self.beta_r = [truncate(series_derivative(value, -self.RE)(self.argument), self.precision) for value in beta]
        self.gamma_r = [truncate(series_derivative(value, -self.RE)(self.argument), self.precision) for value in gamma]
        self.a = truncate(radius(self.argument), self.precision)
        self.ar = truncate(series_derivative(radius, -self.RE)(self.argument), self.precision)
        self.K = truncate(K(self.argument), self.precision)
        self.r_tau = truncate(self.root*self.tau.cos(), self.precision)
        if not (-self.K[0]).real > 0:
            raise ValueError('negative curvature of the selected germ is not proved at the center')


def aggregate_reference_bounds(results, halfwidth, state_tube):
    """Uniform maxima, then one R60 comparison for the entire piecewise field."""
    e0 = max(row['e0_bound'].upper() for row in results)
    e1 = max(row['e1_bound'].upper() for row in results)
    qmin = min(row['qmin'].lower() for row in results)
    qmax = max(row['qmax'].upper() for row in results)
    second = max(row['domain']['f_theta2'].upper() for row in results)
    length = 2*abs(exact_arb(halfwidth))
    A, B, C = length*e0/qmin, length*e1, length*second*qmax/2
    denominator = 1-B.exp()*C*A
    R = B.exp()*A/denominator
    accepted = bool(denominator > 0 and qmax*R < exact_arb(state_tube))
    return dict(e0_bound=e0, e1_bound=e1, qmin=qmin, qmax=qmax,
                f_theta2_bound=second, A=A, B=B, C=C, denominator=denominator,
                R=R, actual_error_upper=(qmax*R).upper()), accepted


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--object', type=Path, required=True)
    parser.add_argument('--root-certificate', type=Path, required=True)
    parser.add_argument('--segment', type=int, required=True)
    parser.add_argument('--initial-label-real', default='1/2')
    parser.add_argument('--initial-label-imag', default='0')
    parser.add_argument('--sub-left', default='5/8')
    parser.add_argument('--sub-right', default='7/8')
    parser.add_argument('--quarter-nodes', type=int, default=512)
    parser.add_argument('--jet-order', type=int, default=16)
    parser.add_argument('--outer-radius', default='8')
    parser.add_argument('--radial-radius', default='3/1000')
    parser.add_argument('--E-radius', default='1/400')
    parser.add_argument('--tail-sigma', default='8/25')
    parser.add_argument('--state-tube', default='1/65536')
    parser.add_argument('--max-germs', type=int, default=16)
    parser.add_argument('--bits', type=int, default=160)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    ctx.prec, ctx.cap = args.bits, max(21, args.jet_order+4)
    manifest, shard, shard_path, real, imag, a, b = load_segment(args.manifest, args.segment)
    ident = manifest['trace_identity']
    if ident['angular_scale'] != 4 or ident['sign'] not in (-1, 1):
        raise ValueError('physical-angle Y=x/4+U and an exact branch sign are required')
    if sha(args.object) != ident['source_sha256'] or sha(args.root_certificate) != ident['root_certificate_sha256']:
        raise ValueError('reference and exact graph/root are different objects')
    sub_left, sub_right = Fraction(args.sub_left), Fraction(args.sub_right)
    if not 0 <= sub_left < sub_right <= 1:
        raise ValueError('invalid exact normalized subspan')
    left, right = a+(b-a)*sub_left, a+(b-a)*sub_right
    tau0, halfwidth = (left+right)/2, (right-left)/2
    R0, RE, sigma = map(Fraction, (args.radial_radius, args.E_radius, args.tail_sigma))
    target = AffineBulkTarget(args.object, args.quarter_nodes, args.quarter_nodes,
                              *map(exact_arb, (R0, RE, sigma)))
    root = certified_root(target, args.root_certificate)
    continuity = continuity_gate(target)
    radial, cover, cells, crossed = radial_cover(target, root, tau0, halfwidth)
    if not cells or len(cells) > args.max_germs:
        raise ValueError('required germ count is outside the configured budget; no cells were omitted')
    label_re, label_im = Fraction(args.initial_label_real), Fraction(args.initial_label_imag)
    label = acb(exact_arb(label_re), exact_arb(label_im))
    theta, L = reference_time_coefficients(real, imag, label, sub_left, sub_right)
    report = dict(kind='directed_actual_reference_residual_finite_common_germ_union', complete=False,
        source_sha256=sha(__file__), object_sha256=sha(args.object),
        root_certificate_sha256=sha(args.root_certificate), exact_delta_fraction=str(target.affine_delta),
        reference_manifest=str(args.manifest), reference_manifest_sha256=sha(args.manifest),
        reference_shard=shard['path'], reference_shard_sha256=sha(shard_path),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in
            ['fourfold_phase_field_time_taylor.py', 'fourfold_phase_reference_time_sample.py',
             'fourfold_phase_beta_interval.py', 'fourfold_phase_beta_bulk_interval.py',
             'fourfold_phase_beta_bulk_box.py', 'fourfold_phase_beta_affine.py']},
        segment=args.segment, original_exact_time_endpoints=[str(a), str(b)],
        normalized_subspan=[str(sub_left), str(sub_right)], exact_time_endpoints=[str(left), str(right)],
        tau_center=str(tau0), time_halfwidth=str(halfwidth),
        initial_label=dict(real=str(label_re), imag=str(label_im)), branch_sign=int(ident['sign']),
        state_coordinate='physical theta=Y=x/4+U; reference Fourier label x has period 2*pi',
        true_radial_range=ball_record(radial), exact_outward_radial_enclosure=list(map(str, cover)),
        exact_reflected_common_scalar_domain=list(map(str, reflected_common_domain(target))),
        required_common_spans=[list(map(str, cell)) for cell in cells],
        guaranteed_crossed_knots=list(map(str, crossed)), scalar_continuity=continuity,
        exact_common_span_coverage=True, bits=args.bits, nodes=args.quarter_nodes,
        retained_time_order=args.jet_order, time_outer_radius=args.outer_radius,
        radial_tail_radius=args.radial_radius, E_tail_radius=args.E_radius,
        primitive_tail_normalized_angle_strip=args.tail_sigma, state_tube_radius=args.state_tube,
        reference_theta_coefficients=[record_complex(value) for value in theta],
        reference_L_coefficients=[record_complex(value) for value in L], accepted_germs=[],
        limitations=['Each selected polynomial germ is only the actual field on its own scalar span',
                     'The bounds are for one exact initial label and the saved finite reference subspan',
                     'Matched-left zero initial error is hypothetical and not the global accumulated error',
                     'No full initial strip, turning collar, parameter variation or Wiener residual certificate'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    def save():
        report['elapsed_seconds'] = time.monotonic()-started
        args.out.write_text(json.dumps(report, indent=2)+'\n')
    save()
    results = []
    for index, cell in enumerate(cells):
        model = FixedGermTimeModel(args.object, args.root_certificate, tau0, halfwidth, cell,
            nodes=args.quarter_nodes, order=args.jet_order, outer_radius=Fraction(args.outer_radius),
            radial_radius=R0, E_radius=RE, tail_sigma=sigma, branch_sign=int(ident['sign']))
        result = model.residual_bound(theta, L, Fraction(args.state_tube))
        results.append(result)
        row = dict(index=index, common_span=list(map(str, cell)),
            whole_true_radial_image_inside_this_span=bool(radial.lower() >= exact_arb(cell[0])
                                                        and radial.upper() <= exact_arb(cell[1])),
            residual_and_time_tail={key:ball_record(result[key]) for key in
                                   ('e0_bound', 'e1_bound', 'e0_tail', 'e1_tail')},
            analytic_outer_domain={key:ball_record(value) for key, value in result['domain'].items()},
            reference_outer_image={key:ball_record(value) for key, value in result['image'].items()},
            E_infinite_error_on_radial_disk=ball_record(model.budget['E_error']),
            e0_coefficients=[record_complex(result['e0'][j]) for j in range(model.precision)],
            e1_coefficients=[record_complex(result['e1'][j]) for j in range(model.precision)])
        report['accepted_germs'].append(row)
        save()
        print(json.dumps(dict(stage='accepted full-time germ', index=index, span=row['common_span'],
                              e0=result['e0_bound'].str(16), e1=result['e1_bound'].str(16))), flush=True)
    aggregate, accepted = aggregate_reference_bounds(results, halfwidth, Fraction(args.state_tube))
    report['uniform_piecewise_field_bounds'] = {key:ball_record(value) for key, value in aggregate.items()}
    report['hypothetical_matching_left_initial_flow_proved'] = accepted
    report['complete'] = len(report['accepted_germs']) == len(cells)
    save()
    print(json.dumps(dict(complete=report['complete'], germs=len(cells),
                          guaranteed_crossed_knots=report['guaranteed_crossed_knots'],
                          e0=aggregate['e0_bound'].str(16), e1=aggregate['e1_bound'].str(16),
                          matched_left_flow=accepted, actual_error=aggregate['actual_error_upper'].str(16))), flush=True)


if __name__ == '__main__':
    main()
