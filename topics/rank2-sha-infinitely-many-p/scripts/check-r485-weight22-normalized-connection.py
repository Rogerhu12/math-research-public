#!/usr/bin/env python3
"""Fixed exact certificates for the weight-22 pure angular connection.

All 68 floor/ceiling classes are checked.  One exact characteristic-p
boundary checks the sharp cumulative saturation threshold; no prime scan.
"""

import json
import sympy as sp

t, K = sp.symbols("t K")
h7 = 16*t*t + 4*t + 7
a = sp.expand(t*(t-1)*h7)
b = sp.cancel(a*a/t).expand()
assert b == t*(t-1)**2*h7**2 or sp.expand(b-t*(t-1)**2*h7**2) == 0
assert sp.degree(b, t) == 7
assert b.coeff(t, 1) == 49


def cm(m):
    return (m+67)//68


def fm(m):
    return 11*m//34


def em(m):
    return fm(m)-4*cm(m)


rows = []
for residue in range(68):
    # Add one period so every input piece is nonempty.
    m = 68+residue
    jump = cm(m+22)-cm(m)
    degree_step = fm(m+22)-fm(m)
    polynomial_raise = 7-4*jump
    slack = em(m+22)-em(m)-polynomial_raise
    assert jump in (0, 1) and degree_step in (7, 8) and slack in (0, 1)
    assert em(m+22)-em(m) >= polynomial_raise
    rows.append([residue, jump, degree_step, slack])
    # The coefficient formula is exact for every polynomial degree j.
    for j in (0, em(m)):
        f = t**j
        left = sp.expand(b*t*sp.diff(a**cm(m)*f, t))
        right = sp.expand(a**(cm(m)+1)*(cm(m)*sp.diff(a, t)*f+a*sp.diff(f, t)))
        assert left == right

# For every smaller positive weight, the single input m=69-c forces
# divisibility by a^2/t (degree seven), beyond the allowed degree.
for c in range(1, 22):
    m = 69-c
    assert cm(m) == 1 and cm(m+c) == 2 and em(m) >= 0
    assert fm(c) < 7
assert fm(22) == 7 and cm(22) == 1


def kernel_dimension(m, p):
    exponent = p*((cm(m)+p-1)//p)
    return max(0, 1+(fm(m)-4*exponent)//p)


p = 101
threshold = (136*p+10)//11
assert threshold == 1249
assert fm(threshold) == 4*p and cm(threshold) <= p
assert sum(kernel_dimension(m, p) for m in range(threshold)) == 1
assert kernel_dimension(threshold, p) == 1
assert sum(kernel_dimension(m, p) for m in range(threshold+1)) == 2
assert 4*(p-cm(threshold)) == em(threshold)
# theta^threshold * a^p is an actual source element; its angular derivative
# has all exponents divisible by p and hence vanishes modulo p.
frobenius_coefficients = {p*j: int(a.coeff(t, j)) % p for j in range(1, 5)}
assert all(exponent*coefficient % p == 0
           for exponent, coefficient in frobenius_coefficients.items())

print(json.dumps({
    "result": "passed",
    "a_coefficients": [int(a.coeff(t, j)) for j in range(5)],
    "weight22_multiplier_coefficients": [int(b.coeff(t, j)) for j in range(8)],
    "all_68_classes_checked": True,
    "degree_step_8_residues": [r for r, _, d, _ in rows if d == 8],
    "ceil_jump_residues": [r for r, j, _, _ in rows if j],
    "pure_delta_minimum_weight": 22,
    "sharp_boundary": {
        "prime": p, "first_extra_kernel_weight": threshold,
        "angular_degree": fm(threshold),
        "canonical_a_exponent": cm(threshold),
        "remaining_polynomial_degree": em(threshold),
        "extra_kernel": "Theta^1249 * a(t)^101",
        "kernel_dimension_below": 1, "kernel_dimension_at": 2,
    },
    "physical_image_saturation_claimed": False,
    "new_central_zero_claimed": False,
}, indent=2))
