#!/usr/bin/env python3
"""R246: exact original dyadic maps and quarter-period normalization.

Only rational arithmetic in Q[zeta_16]/(zeta_16^8+1) is used.
There is no scan over target primes and no floating-point recognition.
"""
from fractions import Fraction as Q
import json
from pathlib import Path

N = 8

def k(a=0):
    return (Q(a),) + (Q(0),) * 7

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def neg(a):
    return tuple(-x for x in a)

def sub(a, b):
    return add(a, neg(b))

def scale(a, b):
    return tuple(x * Q(b) for x in a)

def mul(a, b):
    out = [Q(0)] * 8
    for j, x in enumerate(a):
        for h, y in enumerate(b):
            out[(j + h) % 8] += (1 if j + h < 8 else -1) * x * y
    return tuple(out)

def zp(a):
    a %= 16
    out = [Q(0)] * 8
    out[a % 8] = Q(1 if a < 8 else -1)
    return tuple(out)

def conj(a):
    out = k()
    for j, x in enumerate(a):
        out = add(out, scale(zp(-j), x))
    return out

Z0, O, I = k(), k(1), zp(4)
checks = {}

def check(label, condition):
    checks[label] = bool(condition)
    if not condition:
        raise AssertionError(label)

def va(a, b):
    return [add(x, y) for x, y in zip(a, b)]

def vs(a, c):
    return [mul(x, c) for x in a]

def vx(v, a=1):
    return [v[(j - a) % 16] for j in range(16)]

def vz(v, a=1):
    return [mul(zp(a * j), v[j]) for j in range(16)]

def inner(a, b):
    out = Z0
    for x, y in zip(a, b):
        out = add(out, mul(conj(x), y))
    return out

zinv = scale(tuple(Q((-1) ** j) for j in range(8)), Q(1, 2))
check('inverse_one_plus_zeta', mul(add(O, zp(1)), zinv) == O)
t = tuple(map(Q, [-1, 1, -1, 1, 0, -1, 1, -1]))
c2 = scale(add(scale(O, 2), add(zp(1), zp(-1))), Q(1, 4))
sec2 = add(O, mul(t, t))
check('cosine_squared_inverse', mul(c2, sec2) == O)
v0 = [O if j % 4 == 0 else Z0 for j in range(16)]
v = [Z0, O, Z0, t, Z0, neg(t), Z0, neg(O),
     Z0, neg(O), Z0, neg(t), Z0, t, Z0, O]
basis = [[O if j == h else Z0 for j in range(16)] for h in range(16)]

def R(w):
    terms = va(vz(vx(w)), vs(vz(vx(w), -1), zp(1)))
    terms = va(terms, vs(vz(vx(w, -1)), zp(1)))
    terms = va(terms, vz(vx(w, -1), -1))
    return vs(terms, zinv)

def Radj(w):
    terms = va(vx(vz(w, -1), -1), vs(vx(vz(w), -1), zp(-1)))
    terms = va(terms, vs(vx(vz(w, -1)), zp(-1)))
    terms = va(terms, vx(vz(w)))
    return vs(terms, conj(zinv))

def pi0(w):
    return vs(v0, scale(inner(v0, w), Q(1, 4)))

def u0(w):
    return R(pi0(w))

def vback0(w):
    return vs(pi0(Radj(w)), c2)

def piv(w):
    return vs(v, mul(scale(c2, Q(1, 4)), inner(v, w)))

def fourier(w):
    out = []
    for a in range(16):
        s = Z0
        for b in range(16):
            s = add(s, mul(zp(-a * b), w[b]))
        out.append(scale(s, Q(1, 4)))
    return out

check('four_term_original_transport', R(v0) == v)
check('new_norm', inner(v, v) == scale(sec2, 4))
check('old_norm', inner(v0, v0) == k(4))
check('backward_on_new_vector', vback0(v) == v0)
check('forward_then_backward_projection', all(vback0(u0(w)) == pi0(w) for w in basis))
check('backward_then_forward_projection', all(u0(vback0(w)) == piv(w) for w in basis))
check('forward_commutes_fourier', all(u0(fourier(w)) == fourier(u0(w)) for w in basis))
check('backward_commutes_fourier', all(vback0(fourier(w)) == fourier(vback0(w)) for w in basis))

# Pullback by alpha_minus=4-i.  The two phases really are opposite.
def xm(w):
    return vs(vz(vx(w, -1), 8), I)

def zm(w):
    return vs(vz(vx(w, 8), -1), neg(I))

def xmi(w):
    return vs(vx(vz(w, 8)), neg(I))

def zmi(w):
    return vs(vx(vz(w), 8), I)

def rm(w):
    terms = va(zm(xm(w)), vs(zmi(xm(w)), zp(1)))
    terms = va(terms, vs(zm(xmi(w)), zp(1)))
    return vs(va(terms, zmi(xmi(w))), zinv)

check('CM_minus_X_phase_i', (-15 * 8) % 32 == 8)
check('CM_minus_Z_phase_minus_i', (-(-8) * 15) % 32 == 24)
check('CM_minus_inverse_X', all(xmi(xm(w)) == w for w in basis))
check('CM_minus_inverse_Z', all(zmi(zm(w)) == w for w in basis))
check('CM_minus_commutator', all(zm(xm(w)) == vs(xm(zm(w)), zp(1)) for w in basis))
check('CM_minus_transport_has_negative_sign', rm(v0) == vs(v, k(-1)))

# Exact local expansion at -T, T=(1-i) Omega_0/4, x(T)=i,y(T)=1-i.
ORDER = 4

def smul(a, b):
    out = [Z0] * (ORDER + 1)
    for j, x in enumerate(a):
        for h, y in enumerate(b):
            if j + h <= ORDER:
                out[j + h] = add(out[j + h], mul(x, y))
    return out

def sexp(a):
    out = [O] + [Z0] * ORDER
    for n in range(1, ORDER + 1):
        ss = Z0
        for j in range(1, n + 1):
            ss = add(ss, scale(mul(a[j], out[n - j]), j))
        out[n] = scale(ss, Q(1, n))
    return out

def sinv(a, a0inv):
    out = [a0inv] + [Z0] * ORDER
    for n in range(1, ORDER + 1):
        ss = Z0
        for j in range(1, n + 1):
            ss = add(ss, mul(a[j], out[n - j]))
        out[n] = neg(mul(a0inv, ss))
    return out

def spoly(coeffs, s):
    out = [Z0] * (ORDER + 1)
    for a in reversed(coeffs):
        out = smul(out, s)
        out[0] = add(out[0], k(a))
    return out

x = [I, scale(sub(O, I), -2), k(-4), scale(add(O, I), -4), scale(I, -8)]
x2 = smul(x, x)
check('quarter_point_ODE', all(scale(x[j + 2], (j + 1) * (j + 2)) ==
      sub(scale(x2[j], 6), k(2) if j == 0 else Z0) for j in range(3)))
xi = sinv(x, neg(I))
s = smul(xi, xi)
log_theta = [Z0, scale(add(O, I), Q(1, 2)), scale(I, Q(-1, 2)),
             scale(sub(O, I), Q(-1, 3)), k(Q(1, 3))]
g17 = sexp([scale(a, 17) for a in log_theta])
P1 = [0, 1, Q(3, 5), Q(-1, 5), Q(1, 5)]
P2 = [1, 0, -18, 16, 1]
P3 = [1, -7, 21, -5, -2]
a1 = smul(g17, spoly(P1, s))
expected = [Z0, scale(add(O, I), Q(-32, 5)), scale(I, Q(-32, 5)),
            scale(sub(O, I), Q(56, 5)), k(-88)]
check('fourth_jet_exact', a1 == expected)
check('lambda2_quarter_value', spoly(P2, s)[0] == k(-32))
check('lambda3_quarter_value', spoly(P3, s)[0] == k(32))
# The common factor is 2 i * 2^(-51/8) sec(pi/16).
# Divide by rho=2^(5/8) sec(pi/16), then account for 4^4/2^4.
check('lambda1_normalized_transport_minus_22_i', scale(mul(I, a1[4]), Q(1, 4)) == scale(I, -22))
check('lambda2_normalized_transport_minus_i_over_2', scale(mul(I, spoly(P2, s)[0]), Q(1, 64)) == scale(I, Q(-1, 2)))
check('lambda3_normalized_transport_i_over_2', scale(mul(I, spoly(P3, s)[0]), Q(1, 64)) == scale(I, Q(1, 2)))

def show(a):
    return [str(x) for x in a]

out = {
    'theorem': 'R246', 'status': 'PASS',
    'field': 'Q[zeta_16]/(zeta_16^8+1)',
    'rho': '2^(5/8)/cos(pi/16)',
    'forward_map': 'rho^-1 R Pi_0',
    'backward_map': 'rho cos(pi/16)^2 Pi_0 R^*',
    'CM_minus_lifts': ['i Z^8 X^-1', '-i Z^-1 X^8'],
    'old_to_new_constants': {
        'CM_plus': '1', 'CM_minus': '-1', 'E17_to_E136': '-22 i',
        'E289_to_E2312': '-i/2', 'E4913_to_E39304': 'i/2'},
    'new_to_vplus_constants': {
        'E136_to_E68': '-i 2^(-1/4)/110',
        'E2312_to_E34': '-640 i 2^(-1/4)',
        'E39304_to_E19652': '2 i 2^(-1/4)'},
    'quarter_normalized_jet': [show(a) for a in a1],
    'checks': checks,
}
target = Path(__file__).with_suffix('.json')
target.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'checks': len(checks), 'output': str(target)}, ensure_ascii=False))
