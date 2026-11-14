#!/usr/bin/env python3
"""Exact finite checks of R182 from the original sigma/theta coefficients.

The two sparse ranges are the already used R177 calibrations: p=7, t<=8
and p=11, t<=3.  The script does not generate any coefficient from the
claimed carry formula.  It also tests the actual next central row and
checks that the two proposed low-range confluent prefixes have zero
kernel; those cases are not reported as arithmetic gains.
"""
import importlib.util
import json
from math import comb, factorial
from pathlib import Path

from flint import ctx, fmpq, fmpq_series as Series

spec = importlib.util.spec_from_file_location(
    "actual_plane", Path(__file__).with_name("check-theta-plane-saturated-jets.py"))
plane = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plane)


def mod(value, modulus):
    denominator = int(value.denominator) % modulus
    return int(value.numerator) % modulus * pow(denominator, -1, modulus) % modulus


def actual_series(prime, sparse_maximum):
    r = (prime+1)//4
    period_index = r*(prime-1)
    precision = max(r+period_index*sparse_maximum+3, r*prime+3)
    ctx.cap = precision
    s = Series([0, 1], prec=precision)
    logarithm = [fmpq(0)]*precision
    coefficient = fmpq(1, 3)
    for n in range(1, precision):
        logarithm[n] = coefficient/n
        coefficient *= fmpq(4*n+1, 4*n+3)
    a_s = Series(logarithm, prec=precision).exp()
    period = Series([fmpq(comb(2*n, n), 4**n*(4*n+1))
                     for n in range(precision)], prec=precision)
    s_w = (s*period**4).reversion()
    a_w = a_s(s_w)
    b_w = s_w*a_w
    u_w = Series([(a_w[k]-b_w[k]/3)
                  if k and (k-r) % period_index == 0 else 0
                  for k in range(precision)], prec=precision)
    v_w = Series([b_w[k] if k and (k-1) % period_index == 0 else 0
                  for k in range(precision)], prec=precision)
    u_v = u_w(v_w.reversion())

    h1 = 1+4*s+70*s**2+4*s**3+s**4
    h2 = 1+20*s-26*s**2+20*s**3+s**4
    q8 = 1+364*s**2-1088*s**3+1190*s**4-1088*s**5+364*s**6+s**8
    polynomial = (s*(1-s)**2*(1+s)*(1-2*s+5*s**2)
                  *(5-2*s+s**2)*h1*h2/5)
    ratio = (1+s)*q8/((1-s)*h1*h2)
    first = (polynomial*a_s**17)(s_w)
    second = (ratio*polynomial*a_s**17)(s_w)
    return r, period_index, u_w, v_w, u_v, first, second


def check(prime, sparse_maximum):
    r, period_index, u_w, v_w, u_v, first, second = actual_series(
        prime, sparse_maximum)
    raw = [prime**(1+prime*t)*u_w[r+period_index*t]
           for t in range(sparse_maximum+1)]
    output = [prime**(prime*t)*v_w[1+period_index*t]
              for t in range(sparse_maximum+1)]
    transformed = [prime**(1+prime*t)*u_v[r+period_index*t]
                   for t in range(sparse_maximum+1)]
    g0 = raw[0]
    tau = mod(g0, prime)
    assert tau

    # The actual degree-17 source is combined to satisfy its first
    # central congruence; the next-row identity is then checked directly.
    if mod(first[r], prime):
        multiplier = mod(second[r]/first[r], prime)
        source = second-multiplier*first
        label = f"B-{multiplier}A2"
    else:
        source, label = first, "A2"
    central = source[r]
    assert plane.vp(central, prime) >= 1
    next_axis = source[2*r]-17*u_w[r]*central
    assert plane.vp(next_axis, prime) >= 0
    lhs = prime**(prime-2)*source[r*prime]
    rhs = -central/prime+next_axis/(17*g0)
    assert plane.vp(lhs, prime) >= 0
    assert mod(lhs-rhs, prime) == 0

    ctx.cap = sparse_maximum+1
    variable = Series([0, 1], prec=sparse_maximum+1)
    raw_g = Series(raw, prec=sparse_maximum+1)
    raw_v = Series(output, prec=sparse_maximum+1)
    g = Series(transformed, prec=sparse_maximum+1)
    universal = Series([
        fmpq(prime**t, factorial(1+(prime-1)*t))*g0**(1+(prime-1)*t)
        for t in range(sparse_maximum+1)], prec=sparse_maximum+1)
    universal_v = Series([
        fmpq(prime**t, factorial((prime-1)*t))*g0**((prime-1)*t)
        for t in range(sparse_maximum+1)], prec=sparse_maximum+1)
    for t in range(sparse_maximum+1):
        assert mod(raw_g[t]-universal[t], prime**2) == 0
        assert mod(raw_v[t]-universal_v[t], prime**2) == 0
    assert all(mod(raw_v[t], prime) == (1 if t == 0 else 0)
               for t in range(sparse_maximum+1))

    correction = (raw_v-1)/prime
    raw_defect = (raw_g+variable*raw_g**prime-g0)/prime
    defect = (g+variable*g**prime-g0)/prime
    wilson = ((factorial(prime-1)+1)//prime) % prime
    predicted_raw = -wilson*variable*g**prime
    predicted_output = -variable*g**(prime-1)
    predicted = predicted_raw+r*tau*variable*g**(prime-1)
    for t in range(sparse_maximum+1):
        assert mod(raw_defect[t]-predicted_raw[t], prime) == 0
        assert mod(correction[t]-predicted_output[t], prime) == 0
        assert mod(defect[t]-predicted[t], prime) == 0

    # Independently transform the actual inverse G to the common q
    # parameter.  Every mod-p^3 core basis has degree at most two there.
    inverse_parameter = (variable*g**(prime-1)).reversion()
    reciprocal = 1/g(inverse_parameter)
    core_basis = [Series([1]), prime*reciprocal, prime*variable,
                  prime**2*reciprocal**2,
                  prime**2*variable*reciprocal, prime**2*variable**2]
    for value in core_basis:
        for n in range(3, sparse_maximum+1):
            assert plane.vp(value[n], prime) >= 3
    print(json.dumps({
        "p": prime, "sparse_maximum": sparse_maximum,
        "Wilson_mod_p": wilson,
        "raw_defect_mod_p": [mod(raw_defect[t], prime)
                             for t in range(sparse_maximum+1)],
        "Cartan_defect_mod_p": [mod(defect[t], prime)
                                for t in range(sparse_maximum+1)],
        "actual_next_central_source": label,
        "next_central_row_mod_p": mod(lhs, prime),
        "universal_mod_p2": True, "third_common_layer": True,
        "verified": True
    }), flush=True)


def check_empty_prefix(prime, degree):
    columns, rows = plane.actual_rows(degree)
    target = 2*((prime+1)//4)*degree
    assert target <= len(rows)
    pivots, remaining = plane.saturated_orders(rows[:target], prime)
    assert not remaining
    print(json.dumps({"p": prime, "D": degree, "target_k": target,
                      "source_dimension": len(columns),
                      "prefix_rank": len(pivots), "kernel_rank": 0,
                      "last_nonzero_row": pivots[-1][0],
                      "not_an_arithmetic_gain": True}), flush=True)


if __name__ == "__main__":
    for pair in ((7, 8), (11, 3)):
        check(*pair)
    for pair in ((7, 3), (11, 5)):
        check_empty_prefix(*pair)
