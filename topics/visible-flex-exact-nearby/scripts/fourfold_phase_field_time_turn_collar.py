#!/usr/bin/env python3
"""True time residual at exact +/-pi/2, using certified curvature deflation.

The reference time remains physical tau.  For side=+/-1, eta=pi/2-side*tau,
r=side*t*cos(eta), and r_tau=t*sin(eta).  Exact K(t)=0 defines
D(rho)=-K(t-rho)/rho.  A finite radial Taylor polynomial is composed by Horner
at the nonzero rho time constant; the entire omitted radial tail is paid on
the outer complex time disk before per-time-coefficient Cauchy padding.
The regular field is frame_field(K=-Q, r_tau=t*sin(eta), sign=sign*sin(eta)),
where Q=t*D/(1+cos(eta)).  This includes the true turning endpoint.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import gzip
import io
import json
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, acb_series, ctx

from fourfold_phase_beta_interval import (
    series_constant, array_derivative, series_derivative, vector_dot,
    primitive_fourier_budget, ball_record,
)
from fourfold_phase_beta_bulk_interval import exact_arb, complex_pad
from fourfold_phase_beta_affine import AffineBulkTarget, sha
from fourfold_phase_field_time_taylor import (
    FieldTimeModel, truncate, polynomial, pad_series, phase_evaluation,
    frame_field, record_complex,
)
from fourfold_phase_field_time_germ_union import (
    certified_root, common_knots, reflected_common_domain,
)
from fourfold_phase_reference_time_sample import reference_time_coefficients


@dataclass(frozen=True)
class PiTime:
    """Exact q+p*pi, distinct from a binary64 approximation of an endpoint."""
    q: Fraction = Fraction(0)
    p: Fraction = Fraction(0)

    def __add__(self, other):
        if not isinstance(other, PiTime):
            other = PiTime(Fraction(other))
        return PiTime(self.q+other.q, self.p+other.p)

    __radd__ = __add__

    def __neg__(self):
        return PiTime(-self.q, -self.p)

    def __sub__(self, other):
        return self+(-other if isinstance(other, PiTime) else -Fraction(other))

    def __mul__(self, other):
        coefficient = Fraction(other)
        return PiTime(self.q*coefficient, self.p*coefficient)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return self*(1/Fraction(other))

    def ball(self):
        return exact_arb(self.q)+exact_arb(self.p)*arb.pi()

    def is_zero(self):
        return self.q == 0 and self.p == 0

    def nonnegative(self):
        return self.is_zero() or bool(self.ball() > 0)

    def record(self):
        return dict(rational=str(self.q), pi_coefficient=str(self.p))

    @classmethod
    def from_record(cls, row):
        value = Fraction(int(row['numerator']), int(row['denominator']))
        if row['kind'] == 'rational':
            return cls(value)
        if row['kind'] == 'rational_multiple_of_pi':
            return cls(Fraction(0), value)
        raise ValueError('unsupported exact time object')


def load_reference_segment(path, segment):
    path = Path(path)
    manifest = json.loads(path.read_text())
    if (not manifest.get('complete') or manifest.get('time_basis') != 'bernstein'
            or manifest['time_degree'] != 7 or manifest['fields'] != ['U', 'L']):
        raise ValueError('complete degree-seven U/L Bernstein reference required')
    if not 0 <= segment < manifest['segment_count']:
        raise ValueError('reference segment index outside the branch')
    shard = next(row for row in manifest['shards']
                 if row['start_segment'] <= segment < row['start_segment']+row['segment_count'])
    shard_path = path.parent/shard['path']
    if sha(shard_path) != shard['sha256'] or shard_path.stat().st_size != shard['bytes']:
        raise ValueError('reference shard hash/size mismatch')
    with np.load(io.BytesIO(gzip.decompress(shard_path.read_bytes())), allow_pickle=False) as saved:
        meta = json.loads(str(saved['metadata']))
        real, imag = saved['coefficient_real'].copy(), saved['coefficient_imag'].copy()
    first, count, K = shard['start_segment'], shard['segment_count'], manifest['Fourier_degree']
    if (meta['start_segment'] != first or meta['segment_count'] != count
            or meta['source_sha256'] != manifest['source_sha256']
            or meta['exact_times'] != manifest['exact_time_endpoints'][first:first+count+1]
            or real.shape != (count, 8, 2, K+1) or imag.shape != real.shape
            or not np.all(np.isfinite(real)) or not np.all(np.isfinite(imag))
            or np.any(imag[:, :, :, 0] != 0)):
        raise ValueError('reference shard convention/shape/exact times differ')
    a, b = map(PiTime.from_record, manifest['exact_time_endpoints'][segment:segment+2])
    if manifest['time_orientation'] not in (-1, 1) or not manifest['time_orientation']*(b-a).ball() > 0:
        raise ValueError('nonpositive oriented exact time segment')
    return manifest, shard, shard_path, real[segment-first], imag[segment-first], a, b


class TurnCollarTimeModel(FieldTimeModel):
    """A true positive or negative root collar, with exact physical tau."""
    def __init__(self, object_path, root_certificate, left, right, *, side,
                 nodes=512, order=16, radial_degree=24, outer_radius=8,
                 curvature_radius=Fraction(3, 5000), radial_radius=Fraction(3, 1000),
                 E_radius=Fraction(1, 400), tail_sigma=Fraction(8, 25), branch_sign=1):
        if side not in (-1, 1) or branch_sign not in (-1, 1) or order < 4 or radial_degree < 4:
            raise ValueError('invalid root side, branch sign or Taylor degree')
        self.side, self.sign, self.nodes = side, branch_sign, nodes
        self.order, self.precision = int(order), int(order)+1
        self.work_precision = max(21, self.precision+3)
        self.radial_degree = int(radial_degree)
        self.object_path, self.root_certificate = Path(object_path), Path(root_certificate)
        self.exact_left, self.exact_right = left, right
        self.exact_tau0, self.exact_h = (left+right)/2, (right-left)/2
        self.tau0, self.h = self.exact_tau0.ball(), self.exact_h.ball()
        pi_half = PiTime(Fraction(0), Fraction(1, 2))
        eta_left, eta_right = pi_half-side*left, pi_half-side*right
        if (not eta_left.nonnegative() or not eta_right.nonnegative()
                or not (pi_half-eta_left).ball() > 0 or not (pi_half-eta_right).ball() > 0):
            raise ValueError('the whole real interval must be on the selected inner root side')
        self.endpoint_locations = [v for v, eta in [(-1, eta_left), (1, eta_right)] if eta.is_zero()]
        self.exact_eta0 = pi_half-side*self.exact_tau0
        self.exact_eta1 = -side*self.exact_h
        self.eta0, self.eta1 = self.exact_eta0.ball(), self.exact_eta1.ball()
        self.outer = exact_arb(outer_radius)
        self.RK, self.R0, self.RE, self.sigma = map(exact_arb,
            (curvature_radius, radial_radius, E_radius, tail_sigma))
        if self.h.contains(0) or not self.outer > 1 or not self.R0 > self.RE > self.RK > 0:
            raise ValueError('nonzero time scale and nested analytic radii are required')

        ctx.cap = 4
        positive = AffineBulkTarget(object_path, nodes, nodes, self.R0, self.RE, self.sigma)
        root = certified_root(positive, root_certificate)
        domain_left, domain_right = reflected_common_domain(positive)
        if not exact_arb(domain_left) < root.lower() or not root.upper() < exact_arb(domain_right):
            raise ValueError('the certified root leaves the intersection of actual scalar domains and reflections')
        cuts = common_knots(positive)
        possible = [(a, b) for a, b in zip(cuts, cuts[1:])
                    if exact_arb(a) < root.lower() and root.upper() < exact_arb(b)]
        if len(possible) != 1:
            raise ValueError('the certified positive root is not inside one exact common span')
        self.positive_cell = possible[0]
        positive.set_cell(*self.positive_cell)
        initial_budget = positive.analytic_input_budget(acb(root), self.R0, self.sigma, self.RE)
        self.root, self.root_newton_trace = positive.refine_certified_root(root, self.RK, initial_budget, 3)
        self.root_budget = positive.analytic_input_budget(acb(self.root), self.R0, self.sigma, self.RE)

        # Full radial coefficients about the true root.  Its constant curvature
        # is exactly zero by the existing root certificate, not by floating fit.
        ctx.cap = max(21, self.radial_degree+4)
        root_K = positive.target(self.root, self.RK, self.root_budget)[4]
        if root_K.prec <= self.radial_degree or not root_K[0].real.contains(0):
            raise ValueError('insufficient radial coefficients or inconsistent true root')
        self.deflation_coefficients = [acb((-root_K[j+1]/self.RK).real)
                                       for j in range(self.radial_degree)]

        # A true full-K modulus bound on |r-t| <= RK pays all omitted radial
        # coefficients after division by rho.  Both K denominators are checked.
        ctx.cap = 4
        radial_disk = complex_pad(acb(self.root), self.RK)
        coefficient, Kdisk, _, disk_budget = positive.complete_data(radial_disk)
        first = array_derivative(coefficient)
        Efinite = sum((vector_dot(first[k], first[(-k) % nodes]) for k in range(nodes)), series_constant(0))[0]
        Etrue = complex_pad(Efinite, disk_budget['E_error'])
        radius_disk = positive.scalars(radial_disk, 1)[2][0]
        if (not radius_disk.abs_lower() > 0 or not Etrue.abs_lower() > 0 or not Kdisk.is_finite()):
            raise ValueError('curvature is not certified holomorphic on its full radial disk')
        self.K_bound = abs(Kdisk).upper()
        self.K_domain = dict(radius_modulus_lower=radius_disk.abs_lower(),
                             E_modulus_lower=Etrue.abs_lower(), K_modulus_upper=self.K_bound)

        ctx.cap = self.work_precision
        self.target = (positive if side == 1 else
            AffineBulkTarget(object_path, nodes, nodes, self.R0, self.RE, self.sigma))
        self.cell = self.positive_cell if side == 1 else (-self.positive_cell[1], -self.positive_cell[0])
        self.target.set_cell(*self.cell)
        self.eta = acb_series([acb(self.eta0), acb(self.eta1)])
        self.cos_eta = truncate(self.eta.cos(), self.precision)
        self.sin_eta = truncate(self.eta.sin(), self.precision)
        radial = side*self.root*self.eta.cos()
        self.center = side*self.root*self.eta0.cos()
        self.r_tau = truncate(self.root*self.eta.sin(), self.precision)
        eta_range = self.eta0+arb(0, abs(self.eta1).upper())
        self.real_radial_range = side*self.root*eta_range.cos()
        lo, hi = reflected_common_domain(self.target)
        if (not exact_arb(lo) < self.real_radial_range.lower()
                or not self.real_radial_range.upper() < exact_arb(hi)
                or not exact_arb(self.cell[0]) < self.real_radial_range.lower()
                or not self.real_radial_range.upper() < exact_arb(self.cell[1])):
            raise ValueError('the complete real turning collar leaves its actual common scalar span')
        # The displacement is quadratic near a turn; the linear exp bound used
        # by ordinary spans needlessly loses this vanishing derivative.
        H = abs(self.eta1)*self.outer
        self.radial_image = (abs(self.root)*(abs(self.eta0.cos())*(H.cosh()-1)
                                         +abs(self.eta0.sin())*H.sinh())).upper()
        if not self.radial_image < self.RE:
            raise ValueError('the full outer complex time disk leaves the paid geometric radial disk')
        self.argument = acb_series([0]+[-radial[j]/self.RE for j in range(1, radial.prec)], prec=radial.prec)
        self.budget = self.target.analytic_input_budget(acb(self.center), self.R0, self.sigma, self.RE)
        coefficient, radius, _, _, _ = self.target.target(self.center, self.RE, self.budget)
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

        eta_modulus = (abs(self.eta0)+abs(self.eta1)*self.outer).upper()
        self.cosine_deviation = (eta_modulus.cosh()-1).upper()
        self.rho_outer = (abs(self.root)*self.cosine_deviation).upper()
        if not self.rho_outer < self.RK or not 2-self.cosine_deviation > 0:
            raise ValueError('the full outer time image leaves the paid root-deflation disk')
        ratio = self.rho_outer/self.RK
        self.D_tail = (self.K_bound/self.RK*ratio**self.radial_degree/(1-ratio)).upper()
        self.Q_tail = (abs(self.root)/(2-self.cosine_deviation)*self.D_tail).upper()
        rho = self.root*(1-self.cos_eta)
        normalized_rho = rho/self.RK
        # Known FINITE polynomial: Horner includes every contribution of its
        # nonzero constant.  No truncated analytic series is shifted for free.
        Dpoly = series_constant(self.deflation_coefficients[-1], self.precision)
        for value in self.deflation_coefficients[-2::-1]:
            Dpoly = value+normalized_rho*Dpoly
        Qfinite = self.root*Dpoly/(1+self.cos_eta)
        self.Q = pad_series(Qfinite, self.Q_tail, self.outer, real=True)
        Dfee = sum((abs(value)*ratio**j for j, value in enumerate(self.deflation_coefficients) if j), arb(0))
        self.D_outer = complex_pad(self.deflation_coefficients[0], Dfee+self.D_tail)
        self.Q_outer = self.root*self.D_outer/(2+complex_pad(acb(0), self.cosine_deviation))
        if not self.Q_outer.real > 0 or not self.Q[0].real > 0:
            raise ValueError('true Q does not lie on the positive-real square-root branch')

    def time_field(self, theta_coefficients):
        ctx.cap = self.work_precision
        values, fee, width, Xerror = self.image_and_X_error(theta_coefficients)
        theta = polynomial(values, self.precision)
        X = [series_constant(0, self.precision) for _ in range(3)]
        for k, n in enumerate(self.target.frequency):
            factor = (acb(0, n)*theta).exp()
            for component in range(3):
                X[component] += self.X_coefficient[k, component]*factor
        X = [pad_series(value, Xerror, self.outer, real=all(v.imag == 0 for v in values)) for value in X]
        phases = phase_evaluation(self.beta, self.gamma, self.beta_r, self.gamma_r, theta)
        fields = frame_field(X, self.a, self.ar, *phases, -self.Q,
                             self.r_tau, self.sign*self.sin_eta)
        return fields, dict(theta_image_radius=fee, theta_imaginary_upper=width,
                            X_infinite_error_on_outer_time_disk=Xerror,
                            Q_radial_tail_on_outer_time_disk=self.Q_tail)

    def outer_domain(self, theta_coefficients, state_tube):
        if not exact_arb(state_tube) > 0:
            raise ValueError('strictly positive state-tube radius required')
        old_cap, ctx.cap = ctx.cap, 4
        try:
            values, theta_fee, _, _ = self.image_and_X_error(theta_coefficients)
            theta = complex_pad(values[0], theta_fee+exact_arb(state_tube))
            radial = complex_pad(acb(self.center), self.radial_image)
            coefficient, _, _, budget = self.target.complete_data(radial)
            beta, gamma, a, _ = self.target.scalars(radial, 1)
            phase = phase_evaluation([v[0] for v in beta], [v[0] for v in gamma],
                [v[1] for v in beta], [v[1] for v in gamma], theta)
            angular_width = (4*abs(theta.imag)).upper()
            if not angular_width < self.sigma:
                raise ValueError('the full outer state tube leaves the paid Fourier strip')
            errors, _ = primitive_fourier_budget(self.nodes, self.sigma, angular_width,
                self.R0, budget['radius_bound'], budget['height_bound'], budget['tangent_bound'])
            X = [acb(0) for _ in range(3)]
            for k, n in enumerate(self.target.frequency):
                factor = (acb(0, n)*theta).exp()
                for component in range(3):
                    X[component] += coefficient[k, component][1]*factor
            X = [complex_pad(value, errors[0]/self.R0) for value in X]
            sine = complex_pad(acb(self.eta0), abs(self.eta1)*self.outer).sin()
            f, ft, ftt, rows = frame_field(X, a[0], a[1], *phase, -self.Q_outer,
                                         self.root*sine, self.sign*sine)
            if not rows['D'].abs_lower() > 0 or not all(value.is_finite() for value in (f, ft, ftt)):
                raise ValueError('turning field denominator not separated from zero on the outer disk')
            return dict(f=abs(f).upper(), f_theta=abs(ft).upper(), f_theta2=abs(ftt).upper(),
                        D_modulus_lower=rows['D'].abs_lower(), Q_real_lower=self.Q_outer.real.lower(),
                        theta_imaginary_upper=abs(theta.imag).upper(),
                        X_infinite_error=(errors[0]/self.R0).upper())
        finally:
            ctx.cap = old_cap


def endpoint_residual(model, theta, L, location):
    derivative = lambda values: sum((j*values[j]*location**(j-1) for j in range(1, len(values))), acb(0))/model.h
    # At eta=0 the regular actual field and both angle derivatives vanish
    # identically, irrespective of floating endpoint cosine evaluations.
    return dict(normalized_time_location=location, actual_field_and_angle_derivative_exactly_zero=True,
                e0=record_complex(derivative(theta)), e1=record_complex(derivative(L)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--object', type=Path, required=True)
    parser.add_argument('--root-certificate', type=Path, required=True)
    parser.add_argument('--segment', type=int, required=True)
    parser.add_argument('--side', type=int, choices=(-1, 1), required=True)
    parser.add_argument('--sub-left', default='0')
    parser.add_argument('--sub-right', default='1/8')
    parser.add_argument('--initial-label-real', default='1/2')
    parser.add_argument('--initial-label-imag', default='0')
    parser.add_argument('--quarter-nodes', type=int, default=512)
    parser.add_argument('--jet-order', type=int, default=16)
    parser.add_argument('--radial-degree', type=int, default=24)
    parser.add_argument('--outer-radius', default='8')
    parser.add_argument('--curvature-radius', default='3/5000')
    parser.add_argument('--radial-radius', default='3/1000')
    parser.add_argument('--E-radius', default='1/400')
    parser.add_argument('--tail-sigma', default='8/25')
    parser.add_argument('--state-tube', default='1/65536')
    parser.add_argument('--bits', type=int, default=160)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    ctx.prec, ctx.cap = args.bits, max(21, args.jet_order+4)
    manifest, shard, shard_path, real, imag, a, b = load_reference_segment(args.manifest, args.segment)
    ident = manifest['trace_identity']
    if ident['angular_scale'] != 4 or ident['sign'] not in (-1, 1):
        raise ValueError('physical-angle reference and exact branch sign required')
    if sha(args.object) != ident['source_sha256'] or sha(args.root_certificate) != ident['root_certificate_sha256']:
        raise ValueError('reference and exact graph/root are different objects')
    sub_left, sub_right = Fraction(args.sub_left), Fraction(args.sub_right)
    if not 0 <= sub_left < sub_right <= 1:
        raise ValueError('invalid exact normalized subspan')
    left, right = a+(b-a)*sub_left, a+(b-a)*sub_right
    model = TurnCollarTimeModel(args.object, args.root_certificate, left, right, side=args.side,
        nodes=args.quarter_nodes, order=args.jet_order, radial_degree=args.radial_degree,
        outer_radius=Fraction(args.outer_radius), curvature_radius=Fraction(args.curvature_radius),
        radial_radius=Fraction(args.radial_radius), E_radius=Fraction(args.E_radius),
        tail_sigma=Fraction(args.tail_sigma), branch_sign=int(ident['sign']))
    label_re, label_im = Fraction(args.initial_label_real), Fraction(args.initial_label_imag)
    label = acb(exact_arb(label_re), exact_arb(label_im))
    theta, L = reference_time_coefficients(real, imag, label, sub_left, sub_right)
    result = model.residual_bound(theta, L, Fraction(args.state_tube))
    report = dict(kind='directed_actual_reference_time_residual_with_true_turning_deflation', complete=True,
        source_sha256=sha(__file__), object_sha256=sha(args.object),
        root_certificate_sha256=sha(args.root_certificate), exact_delta_fraction=str(model.target.affine_delta),
        reference_manifest=str(args.manifest), reference_manifest_sha256=sha(args.manifest),
        reference_shard=shard['path'], reference_shard_sha256=sha(shard_path),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in
            ['fourfold_phase_field_time_taylor.py', 'fourfold_phase_field_time_germ_union.py',
             'fourfold_phase_reference_time_sample.py', 'fourfold_phase_beta_interval.py',
             'fourfold_phase_beta_bulk_interval.py', 'fourfold_phase_beta_bulk_box.py',
             'fourfold_phase_beta_affine.py']},
        segment=args.segment, side=args.side, branch_sign=int(ident['sign']),
        exact_time_endpoints=[left.record(), right.record()], normalized_subspan=[str(sub_left), str(sub_right)],
        exact_tau_center=model.exact_tau0.record(), exact_time_halfwidth=model.exact_h.record(),
        exact_eta_center=model.exact_eta0.record(), exact_eta_linear_coefficient=model.exact_eta1.record(),
        included_true_turning_endpoint=bool(model.endpoint_locations),
        physical_time_derivatives='all reference derivatives divide by the exact physical tau halfwidth',
        initial_label=dict(real=str(label_re), imag=str(label_im)),
        root=ball_record(model.root), root_newton_trace=model.root_newton_trace,
        positive_root_common_span=list(map(str, model.positive_cell)), geometry_common_span=list(map(str, model.cell)),
        real_radial_range=ball_record(model.real_radial_range), radial_outer_displacement=ball_record(model.radial_image),
        bits=args.bits, nodes=args.quarter_nodes, retained_time_order=args.jet_order,
        radial_deflation_degree=args.radial_degree, time_outer_radius=args.outer_radius,
        curvature_cauchy_radius=args.curvature_radius, radial_tail_radius=args.radial_radius,
        E_tail_radius=args.E_radius, primitive_tail_normalized_angle_strip=args.tail_sigma,
        state_tube_radius=args.state_tube,
        curvature_holomorphic_disk={key:ball_record(value) for key, value in model.K_domain.items()},
        root_deflation=dict(rho_outer=ball_record(model.rho_outer), D_tail=ball_record(model.D_tail),
            Q_tail=ball_record(model.Q_tail), Q_outer=record_complex(model.Q_outer),
            coefficients_normalized_rho=[record_complex(value) for value in model.deflation_coefficients],
            time_coefficients_Q=[record_complex(model.Q[j]) for j in range(model.precision)],
            exact_root_identity_used=True, finite_radial_polynomial_composed_by_Horner=True,
            entire_omitted_radial_tail_paid_on_outer_time_disk=True),
        reference_theta_coefficients=[record_complex(value) for value in theta],
        reference_L_coefficients=[record_complex(value) for value in L],
        e0_coefficients=[record_complex(result['e0'][j]) for j in range(model.precision)],
        e1_coefficients=[record_complex(result['e1'][j]) for j in range(model.precision)],
        residual_and_time_tail={key:ball_record(result[key]) for key in
                               ('e0_bound', 'e1_bound', 'e0_tail', 'e1_tail')},
        analytic_outer_domain={key:ball_record(value) for key, value in result['domain'].items()},
        reference_outer_image={key:ball_record(value) for key, value in result['image'].items()},
        E_infinite_error_on_geometry_disk=ball_record(model.budget['E_error']),
        E_infinite_error_on_root_disk=ball_record(model.root_budget['E_error']),
        local_zero_initial_error_R60_budgets={key:ball_record(result[key]) for key in
                                             ('qmin', 'qmax', 'A', 'B', 'C', 'denominator', 'R', 'actual_error_upper')},
        hypothetical_matching_left_initial_flow_proved=result['local_matching_initial_flow_proved'],
        exact_endpoint_residuals=[endpoint_residual(model, theta, L, location) for location in model.endpoint_locations],
        elapsed_seconds=time.monotonic()-started,
        limitations=['One exact initial label and one selected saved-reference time subspan',
                     'Negative-root curvature uses the exact explicitly imposed radial symmetry',
                     'Zero left initial error is hypothetical, not the accumulated full-branch error',
                     'No complete initial strip, full return, parameter derivatives or Wiener residual certificate'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key:report[key] for key in
          ['complete', 'side', 'included_true_turning_endpoint', 'residual_and_time_tail',
           'hypothetical_matching_left_initial_flow_proved', 'elapsed_seconds']}, indent=2), flush=True)


if __name__ == '__main__':
    main()
