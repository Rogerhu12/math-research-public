#!/usr/bin/env python3
"""Local strict-span time Taylor model of the true exact-affine R37 field.

The geometry is an exact R57 affine point, with a certified root.  The time
coordinate is tau=tau0+h*u, r=troot*sin(tau); theta and L are explicitly chosen
finite polynomials in u.  Infinite primitive and mean-E errors are inserted
before forming the residual jets.  A larger complex u disk bounds the actual
field and pays the entire time Taylor tail by Cauchy.  This module does not
certify a complete initial-circle reference, a turning collar, or parameter
derivatives.  Its CLI constructs and verifies one local reference model.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
import json
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, acb_series, ctx

from fourfold_phase_beta_interval import (
    series_constant, array_derivative, series_derivative, series_real,
    primitive_fourier_budget, ball_record,
)
from fourfold_phase_beta_bulk_interval import exact_arb, complex_pad
from fourfold_phase_beta_affine import AffineBulkTarget, sha


def exact_complex(value):
    return value if isinstance(value, acb) else acb(exact_arb(value))


def polynomial(coefficients, precision=None):
    return acb_series([exact_complex(v) for v in coefficients],
                      prec=ctx.cap if precision is None else precision)


def truncate(series, precision):
    if series.prec < precision:
        raise ValueError('insufficient computed Taylor coefficients')
    return acb_series([series[j] for j in range(precision)], prec=precision)


def polynomial_bound(coefficients, radius, first=0):
    return sum((abs(exact_complex(v))*radius**j for j, v in enumerate(coefficients)
                if j >= first), arb(0)).upper()


def pad_series(series, error, outer_radius, real=False):
    values = []
    for j in range(series.prec):
        fee = (error/outer_radius**j).upper()
        values.append(acb(series[j].real+arb(0, fee)) if real
                      else complex_pad(series[j], fee))
    return acb_series(values, prec=series.prec)


def frame_field(X, a, ar, beta, gamma, beta_r, gamma_r,
                beta_t, gamma_t, beta_tt, gamma_tt,
                beta_ttt, gamma_ttt, beta_rt, gamma_rt,
                beta_rtt, gamma_rtt, K, r_tau, branch_sign):
    """Field and first two state-angle derivatives; scalar or series inputs.

    Saved sign convention is exactly that of fourfold_phase_exact_affine_nodes:
      f = r_tau*(-m/n + sign*(G/n)*sqrt(-K)).
    With n=-a^2 D, m=-a^2 M, G=a^2 W, this is -r_tau*(M+sign*kappa*W)/D.
    X_theta is the true a_r*T+a*T_r, never a derivative of a truncated primitive.
    """
    sb, cb, s, c = beta.sin(), beta.cos(), gamma.sin(), gamma.cos()
    h = -sb*X[0]+cb*X[1]
    v = -cb*X[0]-sb*X[1]
    z = X[2]
    Q, R = c*z-s*h, c*h+s*z
    P, u, p, q = 1+beta_t, gamma_t, beta_r, gamma_r
    P1, P2, u1, u2 = beta_tt, beta_ttt, gamma_tt, gamma_ttt
    p1, p2, q1, q2 = beta_rt, beta_rtt, gamma_rt, gamma_rtt
    Q1 = a*q-P*s*v-u*R
    R1 = ar+P*c*v+u*Q
    v1 = a*c*p-P*h
    h1 = ar*c-a*s*q+P*v
    Q2 = a*q1-P1*s*v-P*c*u*v-P*s*v1-u1*R-u*R1
    v2 = a*(-s*u*p+c*p1)-P1*h-P*h1
    D = P*c*Q-u*v
    M = p*c*Q-q*v
    W = Q*Q+v*v
    D1 = P1*c*Q-P*s*u*Q+P*c*Q1-u1*v-u*v1
    M1 = p1*c*Q-p*s*u*Q+p*c*Q1-q1*v-q*v1
    W1 = 2*(Q*Q1+v*v1)
    D2 = (P2*c*Q+2*P1*(-s*u*Q+c*Q1)
          +P*((-c*u*u-s*u1)*Q-2*s*u*Q1+c*Q2)
          -u2*v-2*u1*v1-u*v2)
    M2 = (p2*c*Q+2*p1*(-s*u*Q+c*Q1)
          +p*((-c*u*u-s*u1)*Q-2*s*u*Q1+c*Q2)
          -q2*v-2*q1*v1-q*v2)
    W2 = 2*(Q1*Q1+Q*Q2+v1*v1+v*v2)
    kappa = (-K).sqrt()
    A, A1, A2 = -M-branch_sign*kappa*W, -M1-branch_sign*kappa*W1, -M2-branch_sign*kappa*W2
    f = r_tau*A/D
    ft = r_tau*(A1/D-A*D1/D**2)
    ftt = r_tau*(A2/D-(2*A1*D1+A*D2)/D**2+2*A*D1*D1/D**3)
    return f, ft, ftt, dict(D=D, M=M, W=W, Q=Q, v=v)


def phase_evaluation(beta, gamma, beta_r, gamma_r, theta):
    """Finite physical phases with exact Fourier theta differentiation."""
    values = [[0, 0] for _ in range(4)]
    radial = [[0, 0] for _ in range(3)]
    for k, (b, g, br, gr) in enumerate(zip(beta, gamma, beta_r, gamma_r), 1):
        n = 4*k
        sine, cosine = (n*theta).sin(), (n*theta).cos()
        factors = (sine, n*cosine, -n*n*sine, -n*n*n*cosine)
        for j in range(4):
            values[j][0] += b*factors[j]
            values[j][1] += g*factors[j]
        for j in range(3):
            radial[j][0] += br*factors[j]
            radial[j][1] += gr*factors[j]
    return [*values[0], *radial[0], *values[1], *values[2],
            *values[3], *radial[1], *radial[2]]


def field_algebra_check():
    """Independent axisymmetric model: X=(2,0,3), K=-1, r_tau=1."""
    zero = acb(0)
    f, ft, ftt, _ = frame_field([acb(2), zero, acb(3)], acb(1), acb(2),
        *([zero]*14), acb(-1), acb(1), 1)
    if not f.contains(-acb(13)/3) or ft != 0 or ftt != 0:
        raise AssertionError('axisymmetric field/sign/angle-derivative check failed')


class FieldTimeModel:
    """One accurate local branch; all constructor numerics define coefficients."""
    def __init__(self, object_path, root_certificate, tau_center, time_halfwidth,
                 *, nodes=256, order=16, outer_radius=8,
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
        self.sign = branch_sign
        if self.h.contains(0) or not self.outer > 1 or not self.R0 > self.RE > 0:
            raise ValueError('invalid nonzero time scale or analytic radii')
        if not abs(self.tau0)+abs(self.h) < arb.pi()/2:
            raise ValueError('this interface only handles strict interior time segments')
        self.target = AffineBulkTarget(object_path, nodes, nodes, self.R0, self.RE, self.sigma)
        self.nodes = nodes
        certificate = json.loads(Path(root_certificate).read_text())
        if (not certificate.get('proved')
                or certificate['origin_inputs_sha256'] != self.target.affine_definition['origin_inputs']['sha256']
                or certificate['frozen_direction_sha256'] != self.target.affine_definition['direction']['sha256']
                or Fraction(certificate['exact_delta_fraction']) != self.target.affine_delta):
            raise ValueError('root certificate and exact affine graph differ')
        self.root = arb(float(certificate['root_interval'][0])).union(arb(float(certificate['root_interval'][1])))
        self.tau = acb_series([acb(self.tau0), acb(self.h)])
        radial = self.root*self.tau.sin()
        self.center = self.root*self.tau0.sin()
        real_radial_range = self.root*(self.tau0+arb(0, abs(self.h).upper())).sin()
        cuts = sorted({Fraction.from_float(float(v))*sign for key, values in self.target.frozen.items()
                       if key.endswith('_knots') for v in values for sign in (-1, 1)})
        index = bisect_right(cuts, Fraction.from_float(float(self.center.mid())))-1
        if index < 0 or index+1 >= len(cuts):
            raise ValueError('the time center lies outside the actual radial input domain')
        left, right = cuts[index:index+2]
        if not (real_radial_range.lower() >= exact_arb(left)
                and real_radial_range.upper() <= exact_arb(right)):
            raise ValueError('the complete true real time segment crosses a scalar knot')
        self.cell = left, right
        self.target.set_cell(left, right)
        # r0 is DEFINED by the same root*sin(tau0) as radial[0].  This is an
        # exact identity, not subtraction of two independent root approximations.
        self.argument = acb_series([0]+[-radial[j]/self.RE for j in range(1, radial.prec)], prec=radial.prec)
        self.radial_image = (abs(self.root)*((abs(self.h)*self.outer).exp()-1)).upper()
        if not self.radial_image < self.RE:
            raise ValueError('the entire outer complex time disk leaves the paid radial disk')
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
            raise ValueError('actual negative target curvature not proved at the time center')

    def image_and_X_error(self, theta_coefficients):
        values = [exact_complex(v) for v in theta_coefficients]
        if not values:
            raise ValueError('a nonempty finite angle reference is required')
        fee = polynomial_bound(values, self.outer, first=1)
        width = (abs(values[0].imag)+fee).upper()
        normalized_width = (4*width).upper()
        if not normalized_width < self.sigma:
            raise ValueError('reference image leaves the paid Fourier strip')
        errors, _ = primitive_fourier_budget(self.nodes, self.sigma, normalized_width,
            self.R0, self.budget['radius_bound'], self.budget['height_bound'], self.budget['tangent_bound'])
        Xerror = (errors[0]/(self.R0-self.RE)).upper()
        return values, fee, width, Xerror

    def time_field(self, theta_coefficients):
        ctx.cap = self.work_precision
        values, fee, width, Xerror = self.image_and_X_error(theta_coefficients)
        theta = polynomial(values, self.precision)
        X = [series_constant(0, self.precision) for _ in range(3)]
        for k, n in enumerate(self.target.frequency):
            factor = (acb(0, n)*theta).exp()
            for component in range(3):
                X[component] += self.X_coefficient[k, component]*factor
        real = all(v.imag == 0 for v in values)
        X = [pad_series(value, Xerror, self.outer, real=real) for value in X]
        phases = phase_evaluation(self.beta, self.gamma, self.beta_r, self.gamma_r, theta)
        fields = frame_field(X, self.a, self.ar, *phases, self.K, self.r_tau, self.sign)
        return fields, dict(theta_image_radius=fee, theta_imaginary_upper=width,
                            X_infinite_error_on_outer_time_disk=Xerror)

    def outer_domain(self, theta_coefficients, state_tube):
        """Coarse actual analytic field bounds on the larger complex time disk.

        This uses direct wide boxes ONLY for a Cauchy bound / denominator gate.
        The residual itself is formed from the retained time series elsewhere.
        The fixed scalar polynomial germs extend analytically beyond their real
        spans; the actual real trajectory is separately proved to stay in them.
        """
        if not exact_arb(state_tube) > 0:
            raise ValueError('a strictly positive state-tube radius is required')
        old_cap, ctx.cap = ctx.cap, 4
        try:
            values, theta_fee, _, _ = self.image_and_X_error(theta_coefficients)
            theta = complex_pad(values[0], theta_fee+exact_arb(state_tube))
            radial = complex_pad(acb(self.center), self.radial_image)
            coefficient, K, _, budget = self.target.complete_data(radial)
            if not (-K).real > 0:
                raise ValueError('sqrt(-K) is not on the right-half-plane branch in the outer disk')
            beta, gamma, a, _ = self.target.scalars(radial, 1)
            phase = phase_evaluation([v[0] for v in beta], [v[0] for v in gamma],
                [v[1] for v in beta], [v[1] for v in gamma], theta)
            angular_width = (4*abs(theta.imag)).upper()
            if not angular_width < self.sigma:
                raise ValueError('the full outer state tube leaves the Fourier budget strip')
            errors, _ = primitive_fourier_budget(self.nodes, self.sigma, angular_width,
                self.R0, budget['radius_bound'], budget['height_bound'], budget['tangent_bound'])
            X = [acb(0) for _ in range(3)]
            for k, n in enumerate(self.target.frequency):
                factor = (acb(0, n)*theta).exp()
                for component in range(3):
                    X[component] += coefficient[k, component][1]*factor
            X = [complex_pad(value, errors[0]/self.R0) for value in X]
            tau = complex_pad(acb(self.tau0), abs(self.h)*self.outer)
            r_tau = self.root*tau.cos()
            f, ft, ftt, rows = frame_field(X, a[0], a[1], *phase, K, r_tau, self.sign)
            if not rows['D'].abs_lower() > 0 or not all(v.is_finite() for v in (f, ft, ftt)):
                raise ValueError('true field denominator not separated from zero on the outer disk')
            return dict(f=abs(f).upper(), f_theta=abs(ft).upper(), f_theta2=abs(ftt).upper(),
                        D_modulus_lower=rows['D'].abs_lower(), minus_K_real_lower=(-K).real.lower(),
                        theta_imaginary_upper=abs(theta.imag).upper(),
                        X_infinite_error=(errors[0]/self.R0).upper())
        finally:
            ctx.cap = old_cap

    def residual_bound(self, theta_coefficients, L_coefficients, state_tube):
        if (not theta_coefficients or not L_coefficients
                or len(theta_coefficients) > self.precision or len(L_coefficients) > self.precision):
            raise ValueError('reference degree exceeds retained residual degree')
        (f, ft, _, _), trace = self.time_field(theta_coefficients)
        # Differentiation of a known finite polynomial has no unknown high tail.
        # Rebuild its zero coefficient at the highest retained order explicitly.
        derivative0 = polynomial([(j+1)*exact_complex(theta_coefficients[j+1])/self.h
                                  for j in range(len(theta_coefficients)-1)], self.precision)
        derivative1 = polynomial([(j+1)*exact_complex(L_coefficients[j+1])/self.h
                                  for j in range(len(L_coefficients)-1)], self.precision)
        e0, e1 = derivative0-f, derivative1-ft
        domain = self.outer_domain(theta_coefficients, state_tube)
        qratio = 1/self.outer
        tails = [domain[name]*qratio**self.precision/(1-qratio) for name in ('f', 'f_theta')]
        errors = [sum((abs(value[j]) for j in range(self.precision)), arb(0)).upper()+tail
                  for value, tail in zip((e0, e1), tails)]
        Lvalues = [exact_complex(v) for v in L_coefficients]
        Lfee = polynomial_bound(Lvalues, arb(1), first=1)
        qmin = (Lvalues[0].real-Lfee).exp().lower()
        qmax = (Lvalues[0].real+Lfee).exp().upper()
        length = 2*abs(self.h)
        A, B, C = length*errors[0]/qmin, length*errors[1], length*domain['f_theta2']*qmax/2
        denominator = 1-B.exp()*C*A
        R = B.exp()*A/denominator
        accepted = bool(denominator > 0 and qmax*R < exact_arb(state_tube))
        return dict(e0=e0, e1=e1, e0_bound=errors[0].upper(), e1_bound=errors[1].upper(),
                    e0_tail=tails[0].upper(), e1_tail=tails[1].upper(), domain=domain, image=trace,
                    qmin=qmin, qmax=qmax, A=A, B=B, C=C, denominator=denominator,
                    R=R, actual_error_upper=(qmax*R).upper(), local_matching_initial_flow_proved=accepted)


def record_complex(value):
    return dict(real=ball_record(value.real), imag=ball_record(value.imag))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--object', type=Path, required=True)
    parser.add_argument('--root-certificate', type=Path, required=True)
    parser.add_argument('--tau-center', default='1/2')
    parser.add_argument('--time-halfwidth', default='1/16384')
    parser.add_argument('--theta0', default='3/10')
    parser.add_argument('--branch-sign', type=int, default=1)
    parser.add_argument('--reference-degree', type=int, default=7)
    parser.add_argument('--jet-order', type=int, default=16)
    parser.add_argument('--outer-radius', default='8')
    parser.add_argument('--radial-radius', default='3/1000')
    parser.add_argument('--E-radius', default='1/400')
    parser.add_argument('--tail-sigma', default='8/25')
    parser.add_argument('--state-tube', default='1/65536')
    parser.add_argument('--quarter-nodes', type=int, default=256)
    parser.add_argument('--bits', type=int, default=160)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    started = time.monotonic()
    field_algebra_check()
    if not 1 <= args.reference_degree <= args.jet_order:
        raise ValueError('invalid local polynomial degree')
    model = FieldTimeModel(args.object, args.root_certificate, Fraction(args.tau_center),
        Fraction(args.time_halfwidth), nodes=args.quarter_nodes, order=args.jet_order,
        outer_radius=Fraction(args.outer_radius), radial_radius=Fraction(args.radial_radius),
        E_radius=Fraction(args.E_radius), tail_sigma=Fraction(args.tail_sigma), branch_sign=args.branch_sign)
    print(json.dumps(dict(stage='strict time germ', cell=list(map(str, model.cell)),
                          elapsed=time.monotonic()-started)), flush=True)
    theta = [Fraction(args.theta0)]
    for j in range(args.reference_degree):
        (f, _, _, _), _ = model.time_field(theta)
        # This midpoint is only a constructor choice. The chosen dyadic
        # coefficient itself defines the final reference and is verified below.
        theta.append(Fraction.from_float(float((model.h*f[j]/(j+1)).real.mid())))
    (_, ft, _, _), _ = model.time_field(theta)
    L = [Fraction(0)]+[Fraction.from_float(float((model.h*ft[j]/(j+1)).real.mid()))
                       for j in range(args.reference_degree)]
    result = model.residual_bound(theta, L, Fraction(args.state_tube))
    dependencies = ['fourfold_phase_beta_interval.py', 'fourfold_phase_beta_bulk_interval.py',
                    'fourfold_phase_beta_bulk_box.py', 'fourfold_phase_beta_affine.py']
    report = dict(kind='verified_local_strict_time_Taylor_model_for_exact_affine_R37_field',
        complete=True, source_sha256=sha(__file__),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in dependencies},
        object_sha256=sha(args.object), root_certificate_sha256=sha(args.root_certificate),
        origin_inputs_sha256=model.target.affine_definition['origin_inputs']['sha256'],
        frozen_direction_sha256=model.target.affine_definition['direction']['sha256'],
        exact_delta_fraction=str(model.target.affine_delta), bits=args.bits, nodes=args.quarter_nodes,
        tau_center=str(Fraction(args.tau_center)), time_halfwidth=str(Fraction(args.time_halfwidth)),
        exact_radial_common_cell=list(map(str, model.cell)),
        root=ball_record(model.root), radial_center=ball_record(model.center),
        complete_outer_time_radial_image_upper=ball_record(model.radial_image),
        time_outer_radius=str(Fraction(args.outer_radius)),
        radial_tail_radius=str(Fraction(args.radial_radius)), E_tail_radius=str(Fraction(args.E_radius)),
        primitive_tail_normalized_angle_strip=str(Fraction(args.tail_sigma)),
        state_tube_radius=str(Fraction(args.state_tube)),
        branch_sign=args.branch_sign,
        branch_convention='f=troot*cos(tau)*(-m/n+sign*G/n*sqrt(-K0)), matching saved exact-affine DOP853 sign',
        reference_theta_coefficients=[str(v) for v in theta], reference_L_coefficients=[str(v) for v in L],
        reference_definition='theta(u),L(u) are the exact rational power polynomials listed; '
                             'tau=tau_center+time_halfwidth*u, |u|<=1; q=exp(L)',
        matching_initial_theta_fraction=str(sum(((-1)**j*v for j, v in enumerate(theta)), Fraction(0))),
        retained_residual_order=args.jet_order,
        e0_coefficients=[record_complex(result['e0'][j]) for j in range(model.precision)],
        e1_coefficients=[record_complex(result['e1'][j]) for j in range(model.precision)],
        residual_and_time_tail={key:ball_record(result[key]) for key in
                               ('e0_bound', 'e1_bound', 'e0_tail', 'e1_tail')},
        analytic_outer_domain={key:ball_record(value) for key, value in result['domain'].items()},
        reference_outer_image={key:ball_record(value) for key, value in result['image'].items()},
        E_infinite_error_on_radial_disk=ball_record(model.budget['E_error']),
        local_R60_budgets={key:ball_record(result[key]) for key in
                           ('qmin', 'qmax', 'A', 'B', 'C', 'denominator', 'R', 'actual_error_upper')},
        local_matching_initial_flow_proved=result['local_matching_initial_flow_proved'],
        elapsed_seconds=time.monotonic()-started,
        limitations=['One local strict common-span reference only; no entire initial circle or complete leg',
                     'The initial value for the local flow is defined to equal this reference at u=-1',
                     'No parameter first/second derivatives, root collar, global Wiener residual or PDE conclusion',
                     'Polynomial germs provide an analytic extension outside their real spans; '
                     'the whole actual real time segment is separately checked to remain in the selected span'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key:report[key] for key in
          ('local_matching_initial_flow_proved', 'residual_and_time_tail', 'local_R60_budgets', 'elapsed_seconds')}, indent=2), flush=True)
    if not result['local_matching_initial_flow_proved']:
        raise SystemExit('local flow tube did not pass; retained report is a diagnostic')


if __name__ == '__main__':
    main()
