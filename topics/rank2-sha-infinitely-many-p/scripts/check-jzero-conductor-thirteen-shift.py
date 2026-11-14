#!/usr/bin/env python3
"""R328: fixed conductor, canonical multipliers, and complete block transport.

The combinatorial block fixture uses s=20 (so 6s-1 is composite): this is
an integer-lattice identity check, not a target-prime experiment.
"""
import json
import math
from pathlib import Path
import sympy as s

here = Path(__file__).parent
data = json.loads((here/'check-jzero-weighted-conductor-integral.json').read_text())
t, b, ep, ap = s.symbols('t b ep a_p')
N = s.expand(s.Rational(data['scale'])*s.Poly.from_list(
    [s.Integer(v) for v in data['conductor_numerator'][::-1]],t).as_expr())
h7 = 16*t*t+4*t+7
a = t*(t-1)*h7
checks = []


def check(name, expression):
    assert s.cancel(expression) == 0, name
    checks.append(name)


def denominator(n):
    return t**(3*n//4)*(t-1)**(2*n//3)*(1+8*t)**(n//2)*h7**(3*n//4)


def dimension_degree(n):
    return 3*(3*n//4)+2*(n//2)+(2*n//3)


check('actual radial angular carrier',a**40/denominator(40)-
      t**10*(t-1)**14*h7**10/(1+8*t)**20)
assert s.degree(N,t) == 147
assert all(s.Poly(N,t).nth(j) == 0 for j in range(3))
check('actual conductor numerator first coefficient',
      s.Poly(N,t).nth(3)-3**4*7**3*3159421)
check('actual physical first coefficient',
      (-b)**13*7**10*s.Poly(N,t).nth(3)+3**4*7**13*3159421*b**13)
assert all(3159421%d for d in range(2,math.isqrt(3159421)+1))
assert 3159421%6 == 1
checks.append('fixed exceptional integer is prime and ordinary modulo six')

v0 = (t-1)*(1+8*t)*h7
numerators = [s.expand(N*v0),s.cancel(N*v0*(t-1)/t),
              s.cancel(N*v0*(t-1)**2*(1+8*t)*h7/t)]
records = []
for i,pn in enumerate(numerators):
    expected = N*v0*denominator(40+i)/(t**i*denominator(40))
    check('canonical degree %s normalized numerator' % (40+i),pn-expected)
    P = s.Poly(pn,t)
    assert all(q.q == 1 for q in P.all_coeffs())
    assert P.degree() <= dimension_degree(40+i)
    order = min(j for j in range(P.degree()+1) if P.nth(j))
    assert 40+i-3*(40+i)//4+order == 13
    checks.append('canonical degree %s integral degree and origin order' % (40+i))
    records.append({'degree':40+i,'numerator_degree':P.degree(),
                    'numerator_origin_order':order,'physical_origin_order':13})

e2 = lambda x:1+x+x*x/2
check('full charge-forty unit and inverse',
      s.Poly(s.expand(e2(40*ap*ep)*e2(-40*ap*ep)-1),ep).rem(s.Poly(ep**3,ep)).as_expr())
for i in (0,1,2):
    check('consecutive true charge %s' % (40+i),
          s.Poly(s.expand(e2(40*ap*ep)*e2(ap*ep)**i-e2((40+i)*ap*ep)),ep).rem(s.Poly(ep**3,ep)).as_expr())

fixtures = []
for ell in (0,2,6):
    block=20
    L=2*block+ell
    diagonal=[(r+13)//block-r//block for r in range(L)]
    expected=list(range(block-13,block))+list(range(2*block-13,2*block))
    assert [r for r,d in enumerate(diagonal) if d] == expected
    assert sum(diagonal) == 26
    assert all(d in (0,1) for d in diagonal)
    assert all(r+13<L+13 for r in range(L))
    fixtures.append({'block':block,'ell':ell,'input_length':L,
                     'output_length':L+13,'total_index':sum(diagonal),
                     'positive_diagonal_rows':expected})
checks.append('complete thirteen-row transport retains both boundary bands')

out={'status':'PASS','number_of_exact_checks':len(checks),'checks':checks,
     'conductor_degree':40,'physical_shift':13,'total_index':26,
     'physical_first_coefficient':'-3^4*7^13*3159421*b^13',
     'canonical_multipliers':records,'combinatorial_fixtures':fixtures,
     'scope':'All-degree saturation and all-precision lifting are proved in R328. No target-prime scan.'}
dest=Path(__file__).with_suffix('.json')
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('PASS: %s exact checks; %s' % (len(checks),dest.name))
