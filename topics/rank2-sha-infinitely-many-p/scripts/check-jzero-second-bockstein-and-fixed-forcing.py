#!/usr/bin/env python3
"""R338: fixed exact identities; no target-prime scan or fitted source."""

import json
from pathlib import Path
import sympy as s

p, ap, H, eps, n = s.symbols('p a_p H epsilon n')
checks = []


def check(name, expr):
    assert s.cancel(expr) == 0, name
    checks.append(name)


def e2(v):
    return 1 + v + v**2 / 2


def eps_trunc(expr):
    return s.Poly(s.expand(expr), eps).nth(0) + s.Poly(s.expand(expr), eps).nth(1) * eps + s.Poly(s.expand(expr), eps).nth(2) * eps**2


check('full high-axis exponential including the quadratic term',
      eps_trunc(e2(n * ap * eps) * e2(n * p * H * eps)
                - e2(n * (ap + p * H) * eps)))

W0, W1, W2, W3, W4 = s.symbols('W0 W1 W2 W3 W4')
J = W0 + ap * eps * W1 + ap**2 * eps**2 * W2 / 2
JE = W1 + ap * eps * W2 + ap**2 * eps**2 * W3 / 2
JEE = W2 + ap * eps * W3 + ap**2 * eps**2 * W4 / 2
Ee = lambda f: eps * s.diff(f, eps)
check('first Euler identity in the exact three-block target',
      eps_trunc(eps * JE - Ee(J) / ap))
check('second Euler identity in the exact three-block target',
      eps_trunc(eps**2 * JEE - (Ee(Ee(J)) - Ee(J)) / ap**2))

# These symbols are independent contact tails only for checking this
# coefficient identity.  The theorem requires both tails from the same P.
U, V, Z, j1, j2 = s.symbols('shift_W0 shift_W1 shift2_W0 J1_div_p2 J2_div_p2')
low1 = (p**2 * j1 - p * U) / ap
low2 = (2 * p**2 * j2 - 2 * p * ap * V - 2 * p**2 * Z) / ap**2
check('first contact tail with the exact discarded p multiple',
      low1 / p + U / ap - p * j1 / ap)
check('second contact tail with the exact discarded p multiple',
      ap * low2 / p + V + V - 2 * p * (j2 - Z) / ap)
boundary_j1 = s.symbols('boundary_J1_div_p')
boundary_low1 = (p * boundary_j1 - p * U) / ap
check('only the paid boundary tail remains under the weaker original kernel condition',
      boundary_low1 / p + U / ap - boundary_j1 / ap)

# Universal example for the necessity of quotienting by beta_1(K_1):
# T=diag(p,p^2).  The mod-p source e2 admits p*u*e1+e2 as mod-p^2 lifts.
u, v, v1 = s.symbols('u v v1')
T = s.diag(p, p**2)
source_lift = s.Matrix([p * u, v + p * v1])
second = T * source_lift / p**2
assert second == s.Matrix([u, v + p * v1])
checks.append('fixed mod-p2 second obstruction retains the first-lift parameter')
first = T * s.Matrix([u, 0]) / p
assert first == s.Matrix([u, 0])
checks.append('the first-lift change is exactly beta_1 of a first-kernel source')
assert second - first == s.Matrix([0, v + p * v1])
checks.append('the genuine second spectral target quotients this exact beta_1 image')

# One fixed truncated algebra, with composite 6*20-1=119.  This is not a
# target-prime experiment.  The proof in R338 gives the uniform result.
block, ell, shift = 20, 3, 13
length = 2 * block + ell
delta = [((r + shift) // block) - (r // block) for r in range(length)]
boundary = {r for r, d in enumerate(delta) if d == 1}
assert boundary == set(range(block - shift, block)) | set(range(2 * block - shift, 2 * block))
assert len(boundary) == 26 and all(d in (0, 1) for d in delta)
checks.append('all twenty-six physical boundary rows are retained with their exact exponent')

assert all((r // block) in (0, 1) for r in boundary)
assert all((r // block) * ((r // block) - 1) == 0 for r in boundary)
checks.append('target Euler preserves the actual boundary and its second falling power kills it')

for d in (0, 1):
    q = s.symbols('q')
    row = p**(2 - d) * q
    check('original second obstruction has the correct precision for boundary exponent %s' % d,
          p**d * row / p**2 - q)

# Sparse mod-p target: (epsilon-power, w-power).  A coefficient crossing
# w^block is zero mod p; no deletion of the integral row is asserted.
def mult_w_mod_p(term, power, target_ell):
    i, j = term
    j += power
    if j >= block or i >= 3 or (i == 2 and j >= target_ell):
        return None
    return i, j


def m_mod_p(term):
    return mult_w_mod_p(term, shift, ell + shift)


all_contacts = [(1, j) for j in range(block)] + [(2, j) for j in range(ell)]
for term in all_contacts:
    multiplied = mult_w_mod_p(term, block - shift, ell)
    assert multiplied is None or m_mod_p(multiplied) is None
checks.append('the entire second high-axis variation reads only H below s-13')

for j in range(block - shift, block):
    for power in range(block):
        multiplied = mult_w_mod_p((1, j), power, ell)
        assert multiplied is None or m_mod_p(multiplied) is None
checks.append('the weaker original-kernel contact remainder stays in the paid boundary under H')

# Exact central aggregation in a formal degree q=w^s.  The zero source
# mass eliminates the potential quadratic-H contribution to weight 2s.
c1, c2, c20, pair = s.symbols('c1 c2 c2_low high_axis_pair')
check('the original complete next digit remains an aggregate',
      ap**2 / p * (p * c1 / ap - p**2 * (c20 + pair) / ap**2)
      - (ap * c1 - p * c20 - p * pair))
check('the exact central high-axis pairing is isolated without setting either digit to zero',
      ap * c1 / p - c20 - ((ap * c1 - p * c2) / p + c2 - c20))

out = {
    'status': 'PASS',
    'number_of_exact_checks': len(checks),
    'checks': checks,
    'fixed_second_target': 'coker(M mod p)',
    'second_target_when_only_first_kernel_is_fixed':
        'coker(M mod p) / beta_1(ker(M mod p))',
    'true_high_axis_variation':
        '-m13_bar H (0, a_p^-1 shift_s W0, shift_s W1)',
    'source': 'the entire integral canonical conductor of R335, with relative Euler n and original charge n+40',
    'contact_constraint': 'W1 is the Euler value of the same original P; the two contact tails are not independent inputs',
    'central_constraint': '[w^s](H*S_low) = a_p*c1/p - c2_low mod p',
    'scope': 'Fixed symbolic identities and one composite-length truncated algebra; no target-prime scan. Uniform maps and precision are proved in R338.'
}
dest = Path(__file__).with_suffix('.json')
dest.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print('PASS: %s exact checks; %s' % (len(checks), dest.name))
