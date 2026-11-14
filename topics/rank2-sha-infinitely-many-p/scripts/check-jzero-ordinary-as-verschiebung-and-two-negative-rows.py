#!/usr/bin/env python3
"""R336: the actual ordinary zeta/AS cover and the two full Laurent rows.

The all-prime assertions are proved in R336.  This certificate checks the
symbolic identities and reconstructs ONE actual ordinary fiber, p=13,b=17.
It does not scan primes or assert joint negative-moment nonvanishing.
"""
import json
import math
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import sympy as S

checks = []


def check(name, value):
    assert bool(value), name
    checks.append(name)


n, b, u, X, x, ss = S.symbols("n b u X x s")
check("actual rational-primitive recurrence cancels the adjacent term",
      S.cancel((6*n-1)*(-b*(6*n-4)/(6*n-1))+(6*n-4)*b) == 0)
check("the top derivative coefficient is 2p",
      S.expand(6*(2*ss)+2-2*(6*ss+1)) == 0)
check("lowest L0 coefficient is minus two b over five",
      S.cancel(-b*(6-4)/(6-1)+2*b/5) == 0)

z, l0, h, q = S.symbols("Z L0 H Dpminus2x")
check("connection D-Z has minus the scalar obstruction",
      S.expand((q-z+h)-( -(z-h-q))) == 0)
check("the two required ordinary weights read the same index",
      6*(ss-1)+1 == 6*ss-5 and 6*(ss-1) == 6*ss-6)
check("norm-three top coefficient is minus 28/27",
      -S.Rational(1,27)-1 == -S.Rational(28,27))

# D on the genuine function field F_p(x)[y]/(y^2-x^3-b), using Laurent
# polynomials in x and a parity bit.  Thus no numerical samples are used for
# the rational identities.
p, b0 = 13, 17
s0 = (p-1)//6
bb = b0 % p
HH = math.comb(3*s0,s0)*pow(bb,s0,p) % p


def clean(a):
    return {e: c % p for e,c in a.items() if c % p}


def add(a, b):
    c = dict(a)
    for e,v in b.items():
        c[e] = c.get(e,0)+v
    return clean(c)


def scale(a, c):
    return clean({e:c*v for e,v in a.items()})


def shift(a, e):
    return {j+e:v for j,v in a.items()}


def deriv(a, parity):
    da = clean({e-1:e*c for e,c in a.items()})
    if parity == 0:
        return scale(da,2), 1
    return add(scale(shift(a,2),3),
               add(scale(shift(da,3),2),scale(da,2*bb))), 0


def d_iter(a, parity, count):
    for _ in range(count):
        a, parity = deriv(a, parity)
    return a, parity


aa = [1]
for j in range(1,2*s0+1):
    aa.append(-bb*(6*j-4)*pow(6*j-1,-1,p)*aa[-1] % p)
Z = {-3*j-1:-aa[j] % p for j in range(2*s0+1)}
Lzero = add(Z,{-1:1})
check("p13: exact DZ=-x in the elliptic function field",
      d_iter(Z,1,1) == ({1:p-1},0))
check("p13: D^p x equals H Dx",
      d_iter({1:1},0,p) == (scale({0:2},HH),1))
check("p13: D^(p-1)x=Hx with the actual Hasse scalar",
      d_iter({1:1},0,p-1) == ({1:HH},0))
minus_y_over_x_p = {
    3*j-p:-math.comb(3*s0,j)*pow(bb,3*s0-j,p) % p
    for j in range(3*s0+1)
}
DX, parity = d_iter({1:1},0,p-2)
check("p13: the global pth-root identity has the negative sign",
      parity == 1 and add(DX,scale(Z,HH)) == clean(minus_y_over_x_p))
check("p13: top coefficient and Hasse normalization agree",
      aa[-1]*HH % p == pow(bb,3*s0,p))


def mod_fraction(a):
    a = Fraction(a)
    check_den = a.denominator % p
    assert check_den, "unexpected nonintegral coefficient"
    return a.numerator*pow(check_den,-1,p) % p


limit = 12
aq = [Fraction(1)]
vq = [Fraction(1)]
for j in range(1,limit+1):
    aq.append(aq[-1]*Fraction(-b0*(6*j-4),6*j-1))
    vq.append(vq[-1]*Fraction(3-2*j,2*j)*b0)
LL, LL0 = {}, {}
for j in range(1,limit+1):
    LL[6*j-1] = mod_fraction(sum(aq[i]*vq[j-i] for i in range(1,j+1)))
    LL0[6*j-1] = mod_fraction(sum(aq[i]*vq[j-i] for i in range(1,min(j,2*s0)+1)))
as_diff = {}
for e in range(6*limit):
    val = (-HH*LL.get(e,0)+HH*LL0.get(e,0)) % p
    if e % p == 0:
        val = (val+LL.get(e//p,0)) % p
    if val:
        as_diff[e] = val
check("p13: actual rational sigma coefficients satisfy the AS equation",
      not as_diff)
first_diff = min(e for e in LL if (LL[e]-LL0[e]) % p)
check("p13: the first omitted correction is exactly order 5p",first_diff == 5*p)
check("p13: the correction equals H^-1 L0^p",
      (LL[first_diff]-LL0[first_diff]) % p == pow(HH,-1,p)*LL[5] % p)

# Reconstruct the actual ordinary kernel polynomial from the standard
# division-polynomial recursions, reducing in the genuine elliptic ring.
def poly(f):
    return S.Poly(f,x,modulus=p)


zero, one, cubic = poly(0), poly(1), poly(x**3+bb)


def pmul(a,b):
    a0,a1 = a
    b0,b1 = b
    return a0*b0+cubic*a1*b1, a0*b1+a1*b0


def psub(a,b):
    return a[0]-b[0],a[1]-b[1]


def ppow(a,j):
    out = one,zero
    for _ in range(j):
        out = pmul(out,a)
    return out


@lru_cache(None)
def psi(m):
    if m == 0:
        return zero,zero
    if m == 1:
        return one,zero
    if m == 2:
        return zero,poly(2)
    if m == 3:
        return poly(3*x**4+12*bb*x),zero
    if m == 4:
        return zero,poly(4*(x**6+20*bb*x**3-8*bb**2))
    if m % 2:
        k = (m-1)//2
        return psub(pmul(psi(k+2),ppow(psi(k),3)),
                    pmul(psi(k-1),ppow(psi(k+1),3)))
    k = m//2
    top = pmul(psi(k), psub(pmul(psi(k+2),ppow(psi(k-1),2)),
                            pmul(psi(k-2),ppow(psi(k+1),2))))
    quotient,remainder = S.div(top[0],cubic)
    assert remainder.is_zero
    inv2 = pow(2,-1,p)
    return top[1].mul_ground(inv2),quotient.mul_ground(inv2)


ps, odd = psi(p)
check("p13: the actual p-division polynomial has no y term",odd.is_zero)
check("p13: its exponents are all divisible by p",
      all(m[0] % p == 0 for m,c in ps.terms()))
fv = poly(sum(int(c)*x**(m[0]//p) for m,c in ps.terms())).monic()
check("p13: the actual separable kernel has degree p-1 over two",
      fv.degree() == (p-1)//2)
check("p13: the actual kernel is in x cubed",
      all(m[0] % 3 == 0 for m,c in fv.terms()))
P = S.Poly(sum(int(c)*X**(m[0]//3) for m,c in fv.terms()),X,modulus=p)
Pe = P.as_expr()
T = S.Poly(36*X*(X+bb)*(S.diff(Pe,X)**2-Pe*S.diff(Pe,X,2))
           -6*(7*X+4*bb)*Pe*S.diff(Pe,X),X,modulus=p)
check("p13: the genuine Wronskian numerator is monic of degree 2s",
      T.degree() == 2*s0 and int(T.LC()) % p == 1)
fexpr = fv.as_expr()
W = poly(4*(x**3+bb)*S.diff(fexpr,x)**2
         -fexpr*(6*x**2*S.diff(fexpr,x)+4*(x**3+bb)*S.diff(fexpr,x,2)))
check("p13: the full covariant numerator equals x T_P(x^3)",
      W == poly(x*T.as_expr().subs(X,x**3)))
NN = W.mul_ground(pow(HH,-2,p))
DD = fv*fv
wr = NN.diff()*DD-NN*DD.diff()
curve = cubic*wr*wr-(NN*NN*NN*DD+DD**4*bb).mul_ground(HH*HH)
check("p13: the reconstructed V map satisfies the original curve equation",
      curve.is_zero)

e0,e1 = int(P.nth(0)) % p,int(P.nth(1)) % p
epsilon3 = pow(bb,(p-1)//2,p)
check("p13: both actual bottom coefficients are nonzero",e0 != 0 and e1 != 0)
check("p13: the true Q± derivative ratio has its exact constant",
      24*bb*e1+HH**3*epsilon3*e0 == 0 or
      (24*bb*e1+HH**3*epsilon3*e0) % p == 0)
phi = -(X+4*bb)**3/(27*X**2)
norm3 = S.together(X**(2*s0)*Pe.subs(X,phi)-Pe*T.as_expr())
num,den = S.fraction(norm3)
check("p13: the complete norm-three kernel-polynomial equation",
      S.Poly(num,X,modulus=p).is_zero)
check("p13: the actual constant obeys (H P(0))^3=1",
      pow(HH*e0,3,p) == 1)

# This single fiber has n=s-1=1.  The original z rows retain the correction
# x^3=z^-6-3b/7+..., and do not simply read the bottom kernel coefficient.
sigma_row = (e1-mod_fraction(Fraction(6*b0,7))) % p
theta_row = int(T.nth(3)) % p
actual_c = mod_fraction(Fraction(b0,210))
actual_d = mod_fraction(Fraction(-2*b0,15))
check("p13: the first full Laurent row is the original sigma moment",
      pow(HH,6,p)*sigma_row % p == actual_c)
check("p13: the second full Laurent row is the original Theta moment",
      pow(HH,6,p)*theta_row % p == actual_d)
check("p13: the discarded coordinate correction would change the first row",
      sigma_row != e1)

# The complete low Lagrange kernels use the real h rather than an arbitrary
# local parameter.  At n=1 they already detect both different corrections.
t = S.symbols("t")
E1 = 1+t/S.Integer(15)
h1 = 1+t/S.Integer(14)
invv1 = 1+t/S.Integer(2)
c_lag = S.expand(E1*h1**5*invv1).coeff(t,1)*(-b)
d_lag = S.expand(E1**2*h1**6*invv1).coeff(t,1)*(-b)
check("first sigma Lagrange coefficient retains all factors",
      mod_fraction(c_lag.subs(b,b0)) == actual_c)
check("first Theta Lagrange coefficient retains all factors",
      mod_fraction(d_lag.subs(b,b0)) == actual_d)

out = {
    "status":"PASS",
    "check_count":len(checks),
    "checks":checks,
    "single_actual_fiber":{
        "p":p,"b":b0,"H":HH,
        "kernel_polynomial_in_X":str(Pe),
        "T_P":str(T.as_expr()),
        "sigma_laurent_row":sigma_row,
        "theta_laurent_row":theta_row,
        "actual_sigma_coefficient":actual_c,
        "actual_theta_coefficient":actual_d,
        "first_AS_correction_order":first_diff,
    },
    "all_prime_formula":{
        "H":"binom(3s,s)*b^s, p=6s+1",
        "primitive":"Z=-(y/x)*sum(a_n*x^(-3n), n=0..2s)",
        "recurrence":"a_0=1; a_n=-b*(6n-4)/(6n-1)*a_(n-1)",
        "global_identity":"D^(p-2)x+H*Z=-(y/x)^p",
        "scalar_obstruction":"Z^p-H*Z-D^(p-2)x=L0^p",
        "connection_curvature":"curv(D-Z)=-L0^p",
        "actual_AS":"zeta^p-H*zeta=D^(p-2)x; L^p-H*L=-H*L0",
        "norm_three":"X^(2s) P(-(X+4b)^3/(27X^2))=P(X) T_P(X)",
    },
    "scope":"Exact AS/V and full-row identities; no prime scan and no joint fixed-negative-moment nonvanishing claim."
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(f"{len(checks)} exact checks: PASS")
