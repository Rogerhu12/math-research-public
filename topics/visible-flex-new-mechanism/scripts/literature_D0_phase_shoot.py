#!/usr/bin/env python3
"""Frozen D=0 Puiseux germ and numerical continuation in public Actions.

The eight coefficient values are abstract.  No closed geometric base or global
two-end profile is claimed.  The same exact coefficient series is evaluated at
both starting deltas; eta is the coefficient of x**(9/2), not boundary data that
changes with delta.  J is initialized from local constants at zero, never from
an asserted right-tail integral.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as F
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import time

import numpy as np
import scipy
from scipy.integrate import solve_ivp


@dataclass(frozen=True)
class G:
    real: F = F(0)
    imag: F = F(0)

    def __add__(self, other):
        other = as_g(other)
        return G(self.real+other.real, self.imag+other.imag)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.real, -self.imag)

    def __sub__(self, other):
        return self+-as_g(other)

    def __rsub__(self, other):
        return as_g(other)+-self

    def __mul__(self, other):
        other = as_g(other)
        return G(self.real*other.real-self.imag*other.imag,
                 self.real*other.imag+self.imag*other.real)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_g(other)
        denominator = other.real**2+other.imag**2
        if not denominator:
            raise ZeroDivisionError
        return G((self.real*other.real+self.imag*other.imag)/denominator,
                 (self.imag*other.real-self.real*other.imag)/denominator)

    def __bool__(self):
        return bool(self.real or self.imag)

    def value(self):
        return complex(float(self.real), float(self.imag))

    def encoded(self):
        return dict(real=str(self.real), imag=str(self.imag))


def as_g(value):
    return value if isinstance(value, G) else G(F(value))


ZERO, ONE = G(), G(F(1))
A, B, C3 = F(128, 261), F(-8192, 43065), F(524288, 5038605)
ELL = -C3/2


def trim(p):
    p = list(p)
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p


def add(*polynomials):
    result = [ZERO]*max(map(len, polynomials))
    for p in polynomials:
        for j, value in enumerate(p):
            result[j] = result[j]+value
    return trim(result)


def scale(p, factor):
    return trim([value*factor for value in p])


def multiply(p, q):
    result = [ZERO]*(len(p)+len(q)-1)
    for j, value in enumerate(p):
        if value:
            for k, other in enumerate(q):
                if other:
                    result[j+k] = result[j+k]+value*other
    return trim(result)


def coefficient(p, n):
    return p[n] if 0 <= n < len(p) else ZERO


def dx(p, order=1):
    """Derivative in x of a polynomial in y=sqrt(x)."""
    result = [ZERO]*max(1, len(p)-2*order)
    for n, value in enumerate(p):
        if not value:
            continue
        factor = F(1)
        for j in range(order):
            factor *= F(n, 2)-j
        if not factor:
            continue
        exponent = n-2*order
        if exponent < 0:
            raise ValueError("unexpected negative Puiseux power")
        result[exponent] = result[exponent]+value*factor
    return trim(result)


C_POLY = [ZERO, ZERO, ONE, ZERO, ONE]
A2_POLY = [G(F(87, 32)), ZERO, G(F(2))]


def L_poly(q):
    return add(scale(q, F(-8, 3)), scale(multiply(A2_POLY, dx(q)), 2),
               scale(multiply(C_POLY, dx(q, 2)), -2))


def Q_poly(q):
    ll, q3 = L_poly(q), dx(q, 3)
    return add(multiply(ll, dx(q, 4)), scale(multiply(dx(ll), q3), 2),
               scale(multiply(C_POLY, multiply(q3, q3)), 2))


def puiseux(eta, degree):
    if degree < 12:
        raise ValueError("half-power degree must be at least 12")
    q = [ZERO]*8
    q[0], q[2], q[4], q[6] = ONE, G(A), G(B/2), G(C3/6)
    denominators = []
    for n in range(8, degree+1):
        old = coefficient(Q_poly(q+[ZERO]), n-4)
        slope = coefficient(Q_poly(q+[ONE]), n-4)-old
        r = F(n, 2)
        expected = ELL*r*(r-1)*(r-F(9, 2))*(r+F(7, 2))
        if slope != G(expected):
            raise ArithmeticError("wrong exact recurrence denominator")
        if n == 9:
            if old or slope:
                raise ArithmeticError("phase resonance was not free")
            q.append(eta)
        else:
            if not slope:
                raise ArithmeticError("unexpected second resonance")
            q.append(-old/slope)
            denominators.append(dict(half_power_degree=n, slope=str(expected)))
    residual = Q_poly(q)
    if any(coefficient(residual, j) for j in range(degree-3)):
        raise ArithmeticError("exact Q coefficients did not cancel")
    if q[8] != G(F(4, 135)*C3) or q[9] != eta:
        raise ArithmeticError("germ normalization changed")
    return q, denominators


def evaluate(p, x):
    if x < 0:
        if any(p[j] for j in range(1, len(p), 2)):
            raise ValueError("non-real half-power series evaluated on negative x")
        values, coordinate = p[::2], x
    else:
        values, coordinate = p, math.sqrt(x)
    answer = 0j
    for value in reversed(values):
        answer = answer*coordinate+value.value()
    return answer


def integral_to(p, x):
    antiderivative = [ZERO, ZERO]+[
        value/(F(n, 2)+1) for n, value in enumerate(p)]
    return evaluate(antiderivative, x)


def local_anchor():
    j0 = F(165, 128)*B**2
    j1 = -F(261, 64)*j0
    j2 = -F(261, 32)*A**2-F(165, 32)*j1
    assert -F(87, 32)*A**2-F(55, 32)*j1-j2/3 == 0
    assert F(87, 32)*j0+F(2, 3)*j1 == 0
    assert -F(55, 32)*B**2+F(4, 3)*j0 == 0
    return [j0, j1, j2]


ANCHOR = local_anchor()


def precompute(q):
    jets = [dx(q, j) for j in range(5)]
    q2square = multiply(jets[2], jets[2])
    q1square = multiply(jets[1], jets[1])
    integrands = [
        q2square,
        [ZERO, ZERO]+q2square,
        add([ZERO]*4+q2square, scale(q1square, 2)),
    ]
    return dict(coefficients=q, jets=jets, L=L_poly(q), Q=Q_poly(q),
                integrands=integrands)


def initial_state(series, x):
    qjets = [evaluate(p, x) for p in series["jets"][:4]]
    js = [complex(float(anchor))-integral_to(p, x)
          for anchor, p in zip(ANCHOR, series["integrands"])]
    return np.asarray(qjets+js, dtype=complex)


def encoded(values):
    return [[float(complex(value).real), float(complex(value).imag)]
            for value in np.asarray(values).ravel()]


def fields(x, q):
    q0, q1, q2, q3 = q
    c = x+x*x
    a2 = 87/32+2*x
    ll = -8/3*q0+2*a2*q1-2*c*q2
    lp = 4/3*q1+55/16*q2-2*c*q3
    scale_l = max(1., abs(8/3*q0)+abs(2*a2*q1)+abs(2*c*q2))
    return c, a2, ll, lp, scale_l


def period_jets(x, state):
    q0, q1, q2, q3, j0, j1, j2 = state
    c, a2, ll, _, _ = fields(x, state[:4])
    b0, b1, b2 = 87/32*x+2/3*x*x, -55/32+2/3*x, -1/3
    op = -8/3*q0*q1+a2*q1*q1+b0*j0+b1*j1+b2*j2
    op1 = -8/3*q0*q2+2*a2*q1*q2-c*q2*q2 \
        +(87/32+4/3*x)*j0+2/3*j1
    op2 = ll*q3+4/3*q1*q2+55/32*q2*q2+4/3*j0
    return np.asarray([op, op1, op2])


def pack(state):
    return np.concatenate([state.real, state.imag])


def unpack(state):
    return state[:7]+1j*state[7:]


def rhs(x, packed):
    state = unpack(packed)
    q0, q1, q2, q3 = state[:4]
    c, _, ll, lp, _ = fields(x, state[:4])
    q4 = -(2*lp*q3+2*c*q3*q3)/ll
    out = np.asarray([q1, q2, q3, q4, -q2*q2, -x*q2*q2,
                      -x*x*q2*q2-2*q1*q1])
    return pack(out)


def integrate(x0, x1, state, args):
    def small_l(x, packed):
        _, _, ll, _, scale_l = fields(x, unpack(packed)[:4])
        return float(abs(ll)/scale_l-args.minimum_l_ratio)

    def large_state(x, packed):
        return float(np.max(abs(unpack(packed)[:4]))-args.maximum_jet)

    small_l.terminal, small_l.direction = True, -1
    large_state.terminal, large_state.direction = True, 1
    initial_ratio = abs(fields(x0, state[:4])[2])/fields(x0, state[:4])[4]
    if initial_ratio <= args.minimum_l_ratio:
        return dict(success=False, reached_target=False,
                    reason="initial L ratio below event threshold",
                    start=float(x0), target=float(x1),
                    initial_l_ratio=float(initial_ratio)), None
    try:
        solution = solve_ivp(rhs, (x0, x1), pack(state), method="DOP853",
                             rtol=args.rtol, atol=args.atol, dense_output=True,
                             max_step=args.max_step, events=[small_l, large_state])
    except (FloatingPointError, OverflowError, ValueError, ZeroDivisionError) as error:
        return dict(success=False, reached_target=False,
                    reason="continuation raised "+type(error).__name__,
                    error=str(error), start=float(x0), target=float(x1),
                    initial_l_ratio=float(initial_ratio)), None
    end = float(solution.t[-1])
    samples = np.linspace(x0, end, args.validation_nodes)
    states = [unpack(solution.sol(x)) for x in samples]
    periods = np.asarray([period_jets(x, y) for x, y in zip(samples, states)])
    ratios = [abs(fields(x, y[:4])[2])/fields(x, y[:4])[4]
              for x, y in zip(samples, states)]
    terminal = unpack(solution.y[:, -1])
    reached = bool(solution.success and abs(end-x1) <= 1e-12*max(1., abs(x1)))
    return dict(
        success=bool(solution.success), reached_target=reached,
        message=str(solution.message), start=float(x0), end=end, target=float(x1),
        nfev=int(solution.nfev), accepted_steps=int(len(solution.t)-1),
        event_times=[list(map(float, ts)) for ts in solution.t_events],
        initial_l_ratio=float(initial_ratio),
        sampled_min_l_ratio=float(min(ratios)),
        terminal_state=encoded(terminal),
        terminal_q_jet_max=float(np.max(abs(terminal[:4]))),
        terminal_local_J_max=float(np.max(abs(terminal[4:]))),
        sampled_period_jet_max=np.max(abs(periods), axis=0).tolist(),
        sampled_imaginary_q_max=float(max(abs(y[0].imag) for y in states)),
        local_J_are_true_global_right_tails=False,
    ), terminal


def local_report(series, x):
    state = initial_state(series, x)
    q4 = evaluate(series["jets"][4], x)
    c, _, ll, lp, scale_l = fields(x, state[:4])
    direct_q = ll*q4+2*lp*state[3]+2*c*state[3]**2
    return dict(
        x=float(x), state=encoded(state), fourth_derivative=encoded([q4])[0],
        direct_Q_absolute=float(abs(direct_q)),
        exact_polynomial_Q_absolute=float(abs(evaluate(series["Q"], x))),
        L_direct=encoded([ll])[0],
        L_exact_polynomial=encoded([evaluate(series["L"], x)])[0],
        L_direct_minus_polynomial=float(abs(ll-evaluate(series["L"], x))),
        relative_L=float(abs(ll)/scale_l),
        period_jet_absolute=list(map(float, abs(period_jets(x, state)))),
    )


def eta_value(label):
    if label == "0":
        return ZERO
    if label == "i":
        return G(F(0), F(1))
    if label == "-i":
        return G(F(0), F(-1))
    real, imag = label.split(",")
    return G(F(real), F(imag))


def developer_check():
    q, _ = puiseux(G(F(0), F(1)), 14)
    plus = precompute(q)
    minus_q, _ = puiseux(G(F(0), F(-1)), 14)
    assert all(u.real == v.real and u.imag == -v.imag
               for u, v in zip(q, minus_q))
    report = dict(
        kind="finite_exact_interface_check",
        exact_Q_zero_through_half_power_degree=10,
        conjugate_coefficient_identity=True,
        local_anchor=list(map(str, ANCHOR)),
        JSON_serialization_valid=True,
        no_ODE_or_geometric_research_executed=True,
    )
    json.dumps(report)
    # A fixed arithmetic interface check; not a solved profile or ODE.
    assert len(initial_state(plus, .001)) == 7
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--developer-check", action="store_true")
    parser.add_argument("--etas", nargs="+", default=["0", "i", "-i"])
    parser.add_argument("--deltas", nargs="+", type=float, default=[.001, .002])
    parser.add_argument("--orders", nargs="+", type=int, default=[24, 32])
    parser.add_argument("--right", type=float, default=.95)
    parser.add_argument("--left", type=float, default=-.95)
    parser.add_argument("--rtol", type=float, default=1e-10)
    parser.add_argument("--atol", type=float, default=1e-12)
    parser.add_argument("--max-step", type=float, default=.01)
    parser.add_argument("--minimum-l-ratio", type=float, default=1e-12)
    parser.add_argument("--maximum-jet", type=float, default=1e4)
    parser.add_argument("--validation-nodes", type=int, default=513)
    args = parser.parse_args()
    if args.developer_check:
        report = developer_check()
    else:
        if os.environ.get("GITHUB_ACTIONS") != "true" or \
                os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
            raise SystemExit("Run research continuation in the public repository Actions.")
        if min(args.deltas) <= 0 or max(args.deltas) >= args.right:
            raise SystemExit("Require 0 < deltas < right.")
        if args.left >= -max(args.deltas):
            raise SystemExit("Require left < -max(deltas).")
        degree = max(args.orders)
        if min(args.orders) < 12:
            raise SystemExit("Puiseux degrees must be at least 12.")
        started = time.time()
        cases, all_terminal = [], {}
        for label in args.etas:
            eta = eta_value(label)
            q, denominators = puiseux(eta, degree)
            series = precompute(q)
            frozen = json.dumps([value.encoded() for value in q], sort_keys=True)
            reference_hash = hashlib.sha256(frozen.encode()).hexdigest()
            starts = []
            for delta in sorted(set(args.deltas)):
                local = local_report(series, delta)
                refinement = []
                reference_state = initial_state(series, delta)
                for order in sorted(set(args.orders)):
                    prefix = precompute(q[:order+1])
                    difference = initial_state(prefix, delta)-reference_state
                    refinement.append(dict(
                        degree=order, fixed_reference_prefix=True,
                        state_max_difference=float(np.max(abs(difference))),
                        q_jet_max_difference=float(np.max(abs(difference[:4])))))
                shot, terminal = integrate(delta, args.right, reference_state, args)
                starts.append(dict(delta=delta, local=local,
                                   series_refinement=refinement, continuation=shot))
                all_terminal[(label, delta)] = terminal if shot.get("reached_target") else None
            d0, d1 = min(args.deltas), max(args.deltas)
            if d0 < d1:
                consistency, matched = integrate(d0, d1, initial_state(series, d0), args)
                if matched is not None and consistency.get("reached_target"):
                    target = initial_state(series, d1)
                    consistency["same_germ_reference_error"] = encoded(matched-target)
                    consistency["same_germ_reference_error_max"] = float(np.max(abs(matched-target)))
            else:
                consistency = dict(skipped="only one delta")
            terminal_values = [all_terminal[(label, d)] for d in sorted(set(args.deltas))]
            agreement = None
            if len(terminal_values) >= 2 and all(v is not None for v in terminal_values):
                agreement = float(max(np.max(abs(v-terminal_values[0]))
                                      for v in terminal_values[1:]))
            case = dict(
                eta_label=label, eta=eta.encoded(),
                eta_definition="coefficient of x^(9/2), identical for all deltas",
                frozen_half_power_degree=degree,
                frozen_series_sha256=reference_hash,
                frozen_coefficients=[value.encoded() for value in q],
                recurrence_denominators=denominators,
                exact_Q_zero_through_half_power_degree=degree-4,
                starts=starts, same_germ_short_flow=consistency,
                reached_target_terminal_agreement=agreement)
            if not eta:
                left_shots = []
                for delta in sorted(set(args.deltas)):
                    left, _ = integrate(-delta, args.left, initial_state(series, -delta), args)
                    left_shots.append(dict(delta=delta, local=local_report(series, -delta),
                                           continuation=left))
                case["real_analytic_left_continuation"] = left_shots
            cases.append(case)
        conjugacy = []
        if "i" in args.etas and "-i" in args.etas:
            for delta in sorted(set(args.deltas)):
                plus, minus = all_terminal[("i", delta)], all_terminal[("-i", delta)]
                conjugacy.append(dict(
                    delta=delta, both_reached_target=bool(plus is not None and minus is not None),
                    terminal_conjugacy_error=None if plus is None or minus is None else
                    float(np.max(abs(plus-np.conjugate(minus))))))
        report = dict(
            schema="literature-D0-Puiseux-phase-shoot-v1",
            source_commit=os.environ.get("GITHUB_SHA", ""),
            source_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            runtime=dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__),
            elapsed_seconds=float(time.time()-started),
            coefficient_order=["p0", "p1", "p2", "r0", "r1", "s0", "s1", "t0", "t1"],
            coefficients=["-8/3", "0", "0", "0", "87/32", "-55/32", "2/3", "-1/3", "0"],
            C=["0", "1", "1"], W=["-55/32"], D="0",
            local_J_anchor=list(map(str, ANCHOR)),
            local_J_are_true_global_right_tails=False,
            settings=dict(orders=args.orders, deltas=args.deltas, etas=args.etas,
                          rtol=args.rtol, atol=args.atol, max_step=args.max_step,
                          minimum_l_ratio=args.minimum_l_ratio, maximum_jet=args.maximum_jet),
            cases=cases, conjugacy_controls=conjugacy,
            global_two_end_profile_constructed=False,
            geometric_base_realized=False, finite_flex_proved=False)
    body = json.dumps(report, indent=2, allow_nan=False)+"\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(body)
    print(body)


if __name__ == "__main__":
    main()
