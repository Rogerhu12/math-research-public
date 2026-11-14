#!/usr/bin/env python3
"""R314: exact dyadic return, full conductor lattice and q=2 transport.

All checks are fixed rational/symbolic identities; no target-prime scan.
"""
import json
from pathlib import Path
import sympy as s

t, X, Y, Z, x, b = s.symbols('t X Y Z x b')
a = 16*t**4-12*t**3+3*t**2-7*t
b0 = 256*t**4+1472*t**3-1200*t**2+200*t+1
c = -128*t**4-832*t**3+1968*t**2-280*t+1
g2 = 8*t*t+20*t-1
delta = t*(t-1)*g2**2
sub = {X:a, Y:b0, Z:c}
checks = []

def check(name, expression):
    assert s.cancel(expression) == 0, name
    checks.append(name)

def mons(n):
    return [X**i*Y**j*Z**(n-i-j)
            for i in range(n+1) for j in range(n-i+1)]

def coefficient_matrix(n):
    ms = mons(n)
    ps = [s.Poly(s.expand(m.subs(sub)), t) for m in ms]
    return ms, s.Matrix([[P.nth(j) for P in ps]
                         for j in range(4*n+1)])

def source_representative(expr, n):
    ms, M = coefficient_matrix(n)
    _, pivot = M.rref()
    v = s.Matrix([s.Poly(expr, t).nth(j) for j in range(4*n+1)])
    coeff = M[:, list(pivot)].gauss_jordan_solve(v)[0]
    P = sum(coeff[j]*ms[pivot[j]] for j in range(len(pivot)))
    check('source representative, degree %s' % n, P.subs(sub)-expr)
    den = s.ilcm(*[q.q for q in coeff])
    return {'polynomial':str(P), 'monomials':[str(ms[j]) for j in pivot],
            'coefficients':list(map(str, coeff)), 'denominator_lcm':str(den),
            'denominator_factors':{str(p):int(e)
                                    for p,e in s.factorint(den).items()}}

C0 = (-1152*X**2+336*X*Y+432*X*Z-3*Y**2+Y*Z+2*Z**2)/7776
C1 = (-1152*X**2+192*X*Y+288*X*Z+3*Y**2+Y*Z-4*Z**2)/31104
C2 = (4608*X**2+672*X*Y+288*X*Z+9*Y**2-4*Y*Z-5*Z**2)/62208
for j, Cj in enumerate((C0,C1,C2)):
    check('conductor conic %s' % j, Cj.subs(sub)-t**j*delta)
extra = {str(j):source_representative(s.expand(delta*t**j),3)
         for j in (5,6)}
assert all(set(v['denominator_factors']) <= {'2','3'} for v in extra.values())
checks.append('extra conductor cubics have only 2,3 denominators')

U = (-48*X+5*Y+4*Z)/9
check('actual linear unit U', U.subs(sub)-(1+8*t)**3)
check('unit mass U', U.subs({X:0,Y:1,Z:1})-1)

tau = 64*t*(1-t)**3/(1+8*t)**3
R2 = (1+8*t)**10*((1+8*t)**3+512*t*(1-t)**3)
check('dyadic tacnode image', tau-1+g2**2/(1+8*t)**3)
check('node carrier factor', R2.subs(t,1)-9**13)
check('node source ratio', b0.subs(t,1)-729)
check('node source ratio Z', c.subs(t,1)-729)

# The physical sigma/coordinate duplication, including the entire carrier.
xx = x*(x**3-8*b)/(4*(x**3+b))
rho2_over_sigma136 = 2**34*(x**3+b)**17*xx**14*(xx**3-8*b)
rho4_over_sigma136 = x**56*(x**3-8*b)**4
check('physical rho duplication',
      rho2_over_sigma136/rho4_over_sigma136-R2.subs(t,-b/x**3))
check('Theta times Theta(2z)^4 equals U',
      x**5*(x**3-8*b)**4-x**14*(x**3-8*b)*(1-8*b/x**3)**3)

angle_X2 = s.cancel(R2*a.subs(t,tau))
num, den = s.fraction(angle_X2)
assert s.Poly(num,t).degree()-s.Poly(den,t).degree() == 18
assert s.Poly(s.gcd(num,den),t).degree() == 0
assert s.Poly(den,t).degree() == 2
check('true finite-pole denominator', s.monic(den,t)-(t+s.Rational(1,8))**2)
checks.append('true pole order eighteen at infinity')

# No degree-one return: the only original linear polynomial of degree <=2.
Mlow = s.Matrix([[P.coeff(t,j) for P in (a,b0,c)] for j in (4,3)])
v = Mlow.nullspace()[0]
low = s.factor(sum(v[j]*[a,b0,c][j] for j in range(3)))
check('unique low-degree linear source',
      low-s.Rational(81,52)*(832*t*t-104*t+1))
assert low.subs(t,-s.Rational(1,8)) != 0
checks.append('degree-one return excluded by actual pole')

returns = {}
for name, angular in [('X2',a), ('ZminusY2',c-b0)]:
    expr = s.cancel((1+8*t)**6*R2*angular.subs(t,tau))
    assert s.denom(expr) == 1
    assert s.Poly(expr,t).degree() <= 24
    assert s.rem(s.Poly(expr,t),s.Poly(delta,t)).is_zero
    checks.append(name+' is in the full degree-six conductor')
    returns[name] = source_representative(s.expand(expr),6)
assert all(set(v['denominator_factors']) <= {'2','3'} for v in returns.values())
checks.append('original degree-six returns have only 2,3 denominators')

# Symbolic all-iterate divisor costs; Q denotes 4^j, Q=1 mod 3.
Q = s.symbols('Q', integer=True, positive=True)
e = 2*(Q-1)/3
D = (5*Q-2)/3
check('tower charge identity', Q+e-D)
check('tower infinity cost', (14*Q-2)/3+3*e-4*D)
check('tower finite-pole surplus', 3*e-(Q-2)-Q)

# The exact q=2 exponential carry is over the same integer target.
ep, ap, pp, dp = s.symbols('epsilon a_p p delta_p')
trunc = lambda f:s.Poly(s.expand(f),ep).rem(s.Poly(ep**3,ep)).as_expr()
E = lambda v:1+v*ep+v*v*ep**2/2
check('whole exponential next-bit cancellation',
      trunc(E(-pp*ap*dp)*E(ap*(4+pp*dp)))-E(4*ap))
check('charge-four target power', trunc(E(ap)**4)-E(4*ap))

# Full Newton multiplication by lambda^u, checked independently by differences.
lam = s.symbols('lambda')
aa = s.symbols('a0:7')
fall = lambda n,j:s.prod(n-i for i in range(j))
for h in range(7):
    differences = sum((-1)**(h-n)*s.binomial(h,n)*lam**n*
                      sum(aa[j]*fall(n,j) for j in range(n+1))
                      for n in range(h+1))/s.factorial(h)
    expected = sum(lam**j*(lam-1)**(h-j)/s.factorial(h-j)*aa[j]
                   for j in range(h+1))
    check('exact Newton transport h=%s' % h, differences-expected)

out = {'status':'PASS','exact_checks':len(checks),'checks':checks,
       'linear_unit_U':str(U),'U_theta_identity':'Theta(z)*Theta(2z)^4',
       'actual_tau':str(tau),'actual_rho_multiplier_R2':str(s.expand(R2)),
       'actual_doubled_X_angle':str(s.factor(angle_X2)),
       'extra_conductor_cubics':extra,'minimal_return_degree':2,
       'returns':returns,'tower_return_power':'2*(4^j-1)/3',
       'tower_source_degree':'(5*4^j-2)/3',
       'mass_nonzero_node_obstruction':'9^m-1',
       'q2_axis_carry':'exp(-a_p*delta_j*w^s), delta_j=(2^(j*(p+1))-4^j)/p'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'exact_checks':len(checks),
                  'return_degrees':[1,6,26,106],
                  'denominators':{k:v['denominator_factors']
                                  for k,v in returns.items()}},indent=2))
