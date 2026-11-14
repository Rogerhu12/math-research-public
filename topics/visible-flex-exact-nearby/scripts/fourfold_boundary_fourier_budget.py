#!/usr/bin/env python3
"""Directed error budgets for Fourier reconstruction from two complex boundaries.

This module supplies arithmetic, not an analytic-domain certificate. Callers
must first prove the stated strip bound for the actual function. Widths are
physical theta widths; theta has period 2*pi/frequency_scale (default 4).
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


def positive(x, name):
    if not x > 0:
        raise ValueError(name + ' must be strictly positive')


def geometric_moment(r, first, derivative):
    """Sum_{k=first}^infty k^derivative r^k, for derivatives 0,1,2."""
    if derivative not in (0, 1, 2) or first < 1 or not (r > 0 and r < 1):
        raise ValueError('invalid geometric moment')
    d = 1-r
    values = [1/d, first/d+r/d**2,
              first**2/d+2*first*r/d**2+r*(1+r)/d**3]
    return r**first*values[derivative]


def coefficient_error(k, nodes, sample_width, outer_width, modulus, node_error,
                      frequency_scale=4):
    """Error of a sign-selected DFT coefficient, including all aliases.

    Positive k uses the lower boundary and negative k the upper boundary.
    k=0 may use either boundary. node_error bounds the mean absolute sample
    error on each boundary (the maximum also suffices).
    """
    k = abs(k)
    if not (nodes > 1 and 0 <= k < nodes/2 and frequency_scale > 0):
        raise ValueError('frequency must be strictly below the Nyquist mode')
    if not (sample_width >= 0 and outer_width > sample_width and
            modulus >= 0 and node_error >= 0):
        raise ValueError('invalid strip or nonnegative bound')
    q = frequency_scale
    noise = node_error*(-q*k*sample_width).exp()
    aliases = modulus*((-q*k*outer_width).exp()/
                       ((q*nodes*(outer_width-sample_width)).exp()-1)
                       +(q*k*outer_width).exp()/
                       ((q*nodes*(outer_width+sample_width)).exp()-1))
    return noise, aliases


def reconstruction_budget(nodes, degree, sample_width, outer_width, inner_width,
                          modulus, node_error, derivative=0, frequency_scale=4):
    """A_inner norm error, hence a uniform derivative error on the inner strip."""
    if not (0 <= degree < nodes/2 and 0 <= inner_width < outer_width):
        raise ValueError('invalid degree or inner strip')
    if derivative not in (0, 1, 2):
        raise ValueError('only derivative orders 0, 1 and 2 are implemented')
    q = frequency_scale
    noise = arb(0)
    alias = arb(0)
    for k in range(degree+1):
        nk, ak = coefficient_error(k, nodes, sample_width, outer_width,
                                   modulus, node_error, q)
        weight = (1 if k == 0 else 2)*(q*k)**derivative*(q*k*inner_width).exp()
        noise += weight*nk
        alias += weight*ak
    r = (-q*(outer_width-inner_width)).exp()
    tail = 2*modulus*q**derivative*geometric_moment(r, degree+1, derivative)
    return dict(node_error=noise.upper(), alias=alias.upper(),
                fourier_tail=tail.upper(), total=(noise+alias+tail).upper())


def full_fourier_factor(outer_width, inner_width, derivative=0, frequency_scale=4):
    """Sum_{k in Z} (q|k|)^j exp[-q|k|(outer-inner)]."""
    positive(outer_width-inner_width, 'outer minus inner width')
    q = frequency_scale
    r = (-q*(outer_width-inner_width)).exp()
    return (1 if derivative == 0 else 0)+2*q**derivative*geometric_moment(r, 1, derivative)


def time_fourier_budget(nodes, degree, sample_width, outer_width, inner_width,
                        modulus, time_outer_radius, time_inner_radius,
                        coefficient_node_errors, derivative=0, frequency_scale=4):
    """Finite time-polynomial reconstruction, paying the full omitted time tail.

    modulus bounds |f(u,theta)| on |u|<=time_outer_radius, |Im theta|<=outer_width.
    Each supplied error concerns the true corresponding time coefficient at
    the actual sampled boundary. The full rectangular complement is included.
    """
    if not (0 <= time_inner_radius < time_outer_radius and coefficient_node_errors):
        raise ValueError('invalid time radii or missing coefficient errors')
    total = dict(node_error=arb(0), alias=arb(0), fourier_tail=arb(0))
    for i, error in enumerate(coefficient_node_errors):
        b = reconstruction_budget(nodes, degree, sample_width, outer_width, inner_width,
                                  modulus/time_outer_radius**i, error, derivative,
                                  frequency_scale)
        for key in total:
            total[key] += time_inner_radius**i*b[key]
    ratio = time_inner_radius/time_outer_radius
    total['time_tail'] = (modulus*full_fourier_factor(outer_width, inner_width, derivative,
                                                    frequency_scale)*
                          ratio**len(coefficient_node_errors)/(1-ratio))
    total['total'] = sum(total.values(), arb(0))
    return {k: v.upper() for k, v in total.items()}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--nodes', type=int, default=4096)
    p.add_argument('--degree', type=int, default=1800)
    p.add_argument('--sample-width', default='1/100')
    p.add_argument('--outer-width', default='1/64')
    p.add_argument('--inner-width', default='81/10000')
    p.add_argument('--modulus', default='1')
    p.add_argument('--node-error', default='1/1000000000000000000000000')
    p.add_argument('--bits', type=int, default=256)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    ctx.prec = args.bits
    values = [exact_arb(Fraction(getattr(args, name))) for name in
              ['sample_width', 'outer_width', 'inner_width', 'modulus', 'node_error']]
    result = {str(j): {k: ball_record(v) for k, v in
              reconstruction_budget(args.nodes, args.degree, *values, derivative=j).items()}
              for j in range(3)}
    report = dict(kind='conditional_two_boundary_fourier_reconstruction_budget',
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  parameters={k: str(v) if isinstance(v, Path) else v for k, v in vars(args).items()},
                  derivative_budgets=result,
                  actual_field_domain_proved=False,
                  limitation='Arithmetic for explicitly assumed strip/modulus/noise inputs; not an actual return certificate.')
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({j: v['total']['ball'] for j, v in result.items()}, indent=2))


if __name__ == '__main__':
    main()
