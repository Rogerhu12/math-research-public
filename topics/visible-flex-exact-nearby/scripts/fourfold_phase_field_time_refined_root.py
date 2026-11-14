#!/usr/bin/env python3
"""Ordinary/union time germs sharing one certified native root refinement.

The historical binary-endpoint root certificate remains the input identity.
One directed true-infinite interval Newton refinement is cached per exact
object, certificate, precision and Fourier budget.  Explicit common-span time
models then reuse that root ball and all frozen residual/outer-domain methods.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
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
from fourfold_phase_field_time_germ_union import (
    certified_root, common_knots, reflected_common_domain, radial_cover, continuity_gate,
)
from fourfold_phase_reference_time_sample import load_segment, reference_time_coefficients


@dataclass(frozen=True)
class RefinedRoot:
    root: arb
    object_sha256: str
    certificate_sha256: str
    exact_delta: Fraction
    provenance: dict


_ROOT_CACHE = {}


def prepare_refined_root(object_path, root_certificate, *, nodes=512,
                         radial_radius=Fraction(3, 1000), E_radius=Fraction(1, 400),
                         tail_sigma=Fraction(8, 25), scale=Fraction(3, 5000), steps=3):
    """Return a true root enclosure, preserving its original certificate hash."""
    parameters = tuple(map(Fraction, (radial_radius, E_radius, tail_sigma, scale)))
    object_hash, certificate_hash = sha(object_path), sha(root_certificate)
    key = (object_hash, certificate_hash, ctx.prec, int(nodes), parameters, int(steps))
    if key in _ROOT_CACHE:
        return _ROOT_CACHE[key]
    if steps < 1:
        raise ValueError('at least one certified root refinement is required')
    R0, RE, sigma, scale_ball = map(exact_arb, parameters)
    if not R0 > RE > 0 or not scale_ball > 0 or not sigma > 0:
        raise ValueError('invalid native root-refinement radii')
    old_cap, ctx.cap = ctx.cap, 4
    try:
        target = AffineBulkTarget(object_path, nodes, nodes, R0, RE, sigma)
        scalar_continuity = continuity_gate(target)
        original = certified_root(target, root_certificate)
        lo, hi = reflected_common_domain(target)
        if not exact_arb(lo) < original.lower() or not original.upper() < exact_arb(hi):
            raise ValueError('root certificate leaves the common physical scalar domain')
        cuts = common_knots(target)
        cells = [(a, b) for a, b in zip(cuts, cuts[1:])
                 if exact_arb(a) < original.lower() and original.upper() < exact_arb(b)]
        if len(cells) != 1:
            raise ValueError('the certified root is not strictly in one common span')
        target.set_cell(*cells[0])
        budget = target.analytic_input_budget(acb(original), R0, sigma, RE)
        root, trace = target.refine_certified_root(original, scale_ball, budget, int(steps))
        if not original.contains(root) or not root > 0:
            raise ValueError('native refinement escaped the original positive root certificate')
        proof = dict(kind='directed_true_infinite_root_refinement_for_time_fields', proved=True,
            object_sha256=object_hash, root_certificate_sha256=certificate_hash,
            origin_inputs_sha256=target.affine_definition['origin_inputs']['sha256'],
            direction_sha256=target.affine_definition['direction']['sha256'],
            exact_delta_fraction=str(target.affine_delta), source_sha256=sha(__file__),
            bits=ctx.prec, nodes=nodes, radial_radius=str(parameters[0]), E_radius=str(parameters[1]),
            normalized_angle_strip=str(parameters[2]), scale=str(parameters[3]),
            original_root=ball_record(original), refined_root=ball_record(root),
            root_common_span=list(map(str, cells[0])), E_infinite_error=ball_record(budget['E_error']),
            scalar_continuity=scalar_continuity,
            interval_Newton_trace=trace,
            dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in
                ['fourfold_phase_beta_interval.py', 'fourfold_phase_beta_bulk_interval.py',
                 'fourfold_phase_beta_bulk_box.py', 'fourfold_phase_beta_affine.py',
                 'fourfold_phase_field_time_germ_union.py']})
        result = RefinedRoot(root, object_hash, certificate_hash, target.affine_delta, proof)
        _ROOT_CACHE[key] = result
        return result
    finally:
        ctx.cap = old_cap


class RefinedGermTimeModel(FieldTimeModel):
    """The frozen time residual methods with a shared refined-root anchor.

    If cell is omitted, the whole true real time segment must lie in one common
    span.  With an explicit cell, this is the same finite-germ-union contract as
    FixedGermTimeModel: the caller must cover every required actual span.
    """
    def __init__(self, object_path, root_certificate, tau_center, time_halfwidth,
                 *, refined_root=None, cell=None, nodes=512, order=16, outer_radius=8,
                 radial_radius=Fraction(3, 1000), E_radius=Fraction(1, 400),
                 tail_sigma=Fraction(8, 25), branch_sign=1):
        if branch_sign not in (-1, 1) or order < 4:
            raise ValueError('invalid branch sign or time jet order')
        package = refined_root or prepare_refined_root(object_path, root_certificate, nodes=nodes,
            radial_radius=radial_radius, E_radius=E_radius, tail_sigma=tail_sigma)
        if (not isinstance(package, RefinedRoot) or package.object_sha256 != sha(object_path)
                or package.certificate_sha256 != sha(root_certificate)):
            raise ValueError('shared root package and exact object/certificate differ')
        self.root_package, self.root = package, package.root
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
        if self.target.affine_delta != package.exact_delta:
            raise ValueError('shared root has a different exact affine parameter')
        self.radial_range, _, cells, _ = radial_cover(self.target, self.root, tau_center, time_halfwidth)
        if cell is None:
            if len(cells) != 1:
                raise ValueError('ordinary time interval crosses a knot; supply explicit cells for a complete union')
            self.cell = cells[0]
        else:
            self.cell = tuple(map(Fraction, cell))
            if self.cell not in cells:
                raise ValueError('selected germ does not meet the complete true radial image')
        self.required_common_cells = cells
        self.target.set_cell(*self.cell)
        self.tau = acb_series([acb(self.tau0), acb(self.h)])
        radial = self.root*self.tau.sin()
        self.center = self.root*self.tau0.sin()
        self.argument = acb_series([0]+[-radial[j]/self.RE for j in range(1, radial.prec)], prec=radial.prec)
        self.radial_image = (abs(self.root)*((abs(self.h)*self.outer).exp()-1)).upper()
        if not self.radial_image < self.RE:
            raise ValueError('the full outer complex time disk leaves the paid radial disk')
        self.budget = self.target.analytic_input_budget(acb(self.center), self.R0, self.sigma, self.RE)
        coefficient, radius, _, _, K = self.target.target(self.center, self.RE, self.budget)
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
            raise ValueError('negative target curvature is not proved at the time center')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--object', type=Path, required=True)
    parser.add_argument('--root-certificate', type=Path, required=True)
    parser.add_argument('--segment', type=int, default=653)
    parser.add_argument('--sub-left', default='31/64')
    parser.add_argument('--sub-right', default='33/64')
    parser.add_argument('--initial-label-real', default='1/2')
    parser.add_argument('--initial-label-imag', default='0')
    parser.add_argument('--quarter-nodes', type=int, default=512)
    parser.add_argument('--jet-order', type=int, default=16)
    parser.add_argument('--outer-radius', default='8')
    parser.add_argument('--radial-radius', default='3/1000')
    parser.add_argument('--E-radius', default='1/400')
    parser.add_argument('--tail-sigma', default='8/25')
    parser.add_argument('--state-tube', default='1/65536')
    parser.add_argument('--bits', type=int, default=160)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    ctx.prec, ctx.cap = args.bits, max(21, args.jet_order+4)
    manifest, shard, shard_path, real, imag, a, b = load_segment(args.manifest, args.segment)
    ident = manifest['trace_identity']
    if ident['angular_scale'] != 4 or ident['sign'] not in (-1, 1):
        raise ValueError('physical-angle reference and exact branch sign required')
    if sha(args.object) != ident['source_sha256'] or sha(args.root_certificate) != ident['root_certificate_sha256']:
        raise ValueError('reference and exact graph/root are different objects')
    sub_left, sub_right = Fraction(args.sub_left), Fraction(args.sub_right)
    if not 0 <= sub_left < sub_right <= 1:
        raise ValueError('invalid exact normalized subspan')
    left, right = a+(b-a)*sub_left, a+(b-a)*sub_right
    center, halfwidth = (left+right)/2, (right-left)/2
    model = RefinedGermTimeModel(args.object, args.root_certificate, center, halfwidth,
        nodes=args.quarter_nodes, order=args.jet_order, outer_radius=Fraction(args.outer_radius),
        radial_radius=Fraction(args.radial_radius), E_radius=Fraction(args.E_radius),
        tail_sigma=Fraction(args.tail_sigma), branch_sign=int(ident['sign']))
    label_re, label_im = Fraction(args.initial_label_real), Fraction(args.initial_label_imag)
    label = acb(exact_arb(label_re), exact_arb(label_im))
    theta, L = reference_time_coefficients(real, imag, label, sub_left, sub_right)
    result = model.residual_bound(theta, L, Fraction(args.state_tube))
    report = dict(kind='directed_actual_reference_time_residual_with_shared_native_root', complete=True,
        source_sha256=sha(__file__), object_sha256=sha(args.object),
        root_certificate_sha256=sha(args.root_certificate), root_refinement=model.root_package.provenance,
        exact_delta_fraction=str(model.target.affine_delta),
        reference_manifest=str(args.manifest), reference_manifest_sha256=sha(args.manifest),
        reference_shard=shard['path'], reference_shard_sha256=sha(shard_path),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in
            ['fourfold_phase_field_time_taylor.py', 'fourfold_phase_field_time_germ_union.py',
             'fourfold_phase_reference_time_sample.py', 'fourfold_phase_beta_interval.py',
             'fourfold_phase_beta_bulk_interval.py', 'fourfold_phase_beta_bulk_box.py',
             'fourfold_phase_beta_affine.py']},
        segment=args.segment, exact_time_endpoints=list(map(str, (left, right))),
        normalized_subspan=list(map(str, (sub_left, sub_right))), tau_center=str(center), time_halfwidth=str(halfwidth),
        initial_label=dict(real=str(label_re), imag=str(label_im)), branch_sign=int(ident['sign']),
        common_span=list(map(str, model.cell)), whole_true_real_interval_in_one_span=True,
        bits=args.bits, nodes=args.quarter_nodes, retained_time_order=args.jet_order,
        time_outer_radius=args.outer_radius, radial_tail_radius=args.radial_radius,
        E_tail_radius=args.E_radius, primitive_tail_normalized_angle_strip=args.tail_sigma,
        state_tube_radius=args.state_tube,
        reference_theta_coefficients=[record_complex(value) for value in theta],
        reference_L_coefficients=[record_complex(value) for value in L],
        e0_coefficients=[record_complex(result['e0'][j]) for j in range(model.precision)],
        e1_coefficients=[record_complex(result['e1'][j]) for j in range(model.precision)],
        residual_and_time_tail={key:ball_record(result[key]) for key in
                               ('e0_bound', 'e1_bound', 'e0_tail', 'e1_tail')},
        analytic_outer_domain={key:ball_record(value) for key, value in result['domain'].items()},
        reference_outer_image={key:ball_record(value) for key, value in result['image'].items()},
        E_infinite_error_on_radial_disk=ball_record(model.budget['E_error']),
        local_zero_initial_error_R60_budgets={key:ball_record(result[key]) for key in
                                             ('qmin', 'qmax', 'A', 'B', 'C', 'denominator', 'R', 'actual_error_upper')},
        hypothetical_matching_left_initial_flow_proved=result['local_matching_initial_flow_proved'],
        elapsed_seconds=time.monotonic()-started,
        limitations=['Same exact affine root as the historical input certificate, not a changed parameter point',
                     'One fixed initial label and one ordinary saved-reference time subspan',
                     'Matched-left zero initial error is not the accumulated full-branch error',
                     'No complete time/initial-label coverage, parameter derivative or Wiener certificate'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(complete=True, root=model.root.str(40),
        e0=result['e0_bound'].str(22), e1=result['e1_bound'].str(22),
        e0_center_radius=result['e0'][0].real.rad().str(22),
        e1_center_radius=result['e1'][0].real.rad().str(22),
        elapsed_seconds=report['elapsed_seconds']), indent=2), flush=True)


if __name__ == '__main__':
    main()
