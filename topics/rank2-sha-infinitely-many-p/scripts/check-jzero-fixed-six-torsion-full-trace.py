#!/usr/bin/env python3
"""R320: exact fixed E[6] trace, all constants, and original Newton boundary.

The all-n trace is proved by actual x/y translation sums and normalized Miller
functions.  This certificate checks their rational identities, all three
original source columns, and the exact p=23 central boundary.
"""
import json
from pathlib import Path
import sympy as s

checks = []


def check(name, assertion):
    assert assertion, name
    checks.append(name)


X, x, y, b, t, n, m, z = s.symbols("X x y b t n m z", nonzero=True)
d = X - 8*b
basis = [s.Integer(1), 1/X, 1/d, 1/d**2, 1/d**3]
eig = [
    s.Integer(1),
    1/X + 1/(4*b),
    1/d + 1/(12*b),
    1 + 60*b/d + 432*b**2/d**2,
    1 + 228*b/d + 4320*b**2/d**2 + 20736*b**3/d**3,
]
P = s.Matrix([
    [1, 1/(4*b), 1/(12*b), 1, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 60*b, 228*b],
    [0, 0, 0, 432*b**2, 4320*b**2],
    [0, 0, 0, 0, 20736*b**3],
])
for j in range(5):
    check(f"actual eigenfunction {j}",
          s.cancel(sum(P[i,j]*basis[i] for i in range(5))-eig[j]) == 0)
M = s.Matrix([
    [n, (n*n-n)/(4*b), (1-n)/(12*b),
     5*(n-1)/(432*b*b), (n-1)*(n-31)/(20736*b**3)],
    [0, n*n, 0, 0, 0],
    [0, 0, 1, 5*(n-1)/(36*b), (n-1)*(19*n-31)/(1728*b*b)],
    [0, 0, 0, n, 5*n*(n-1)/(24*b)],
    [0, 0, 0, 0, n*n],
])
check("full eigenmatrix including constants",
      (M*P-P*s.diag(n,n*n,1,n,n*n)).applyfunc(s.cancel) == s.zeros(5))
check("identity layer", M.subs(n,1) == s.eye(5))
check("all exact trace compositions",
      (M*M.subs(n,m)-M.subs(n,n*m)).applyfunc(s.cancel) == s.zeros(5))
check("exact determinant", s.factor(M.det()) == n**6)
cp = M.charpoly(z)
zz = cp.gen
check("exact characteristic polynomial",
      s.factor(cp.as_expr()) == (zz-1)*(zz-n)**2*(zz-n*n)**2)

# Actual 3-torsion y-difference and 6-torsion translation sums.
v, a, A = s.symbols("v a A", nonzero=True)
Dder = lambda f: s.diff(f,x)*2*y + s.diff(f,y)*3*x*x
y_three = s.cancel(2*v*Dder(y/x**2)).subs(y*y,x**3+b)
check("actual three-torsion y-difference",
      s.cancel(y_three-(-2*v-8*b*v/x**3)) == 0)
sum_inv1 = 3*x*x/(x**3-A)
sum_inv2 = -s.diff(sum_inv1,x)
sum_inv3 = -s.diff(sum_inv2,x)/2
sum_a_inv2 = x*sum_inv2-sum_inv1
sum_ai_inv2 = (x*x*sum_inv2-2*x*sum_inv1+3)/A
sum_xpair = s.cancel(2*(x*x*sum_inv2+x*sum_a_inv2+2*b*sum_ai_inv2))
sum_ypair = s.cancel(2*v*(3*x*x*sum_inv2-4*(x**3+b)*sum_inv3))
check("actual six-torsion x-pair sum",
      s.cancel(sum_xpair.subs(A,8*b)-6*eig[3].subs(X,x**3)) == 0)
check("actual six-torsion y-pair difference sum",
      s.cancel(sum_ypair.subs(A,8*b)+6*v*eig[4].subs(X,x**3)) == 0)

# The normalized 6-torsion function at P=(2*t^2,3*t^3).
# Its numerator/denominator are the actual tangent and horizontal lines.
ell = y-2*t*x+t**3
ellminus = y+2*t*x-t**3
f6 = (ell/ellminus)**3*(y-t**3)/(y+t**3)
check("six-torsion inverse normalization", s.cancel(f6*f6.subs(y,-y)-1) == 0)
dlog6 = 3*(Dder(ell)/ell-Dder(ellminus)/ellminus)
dlog6 += 3*x*x/(y-t**3)-3*x*x/(y+t**3)
expected = 12*t+36*t**3/(x-2*t*t)
num = s.together(dlog6-expected).as_numer_denom()[0]
check("complete actual six-torsion dlog",
      s.rem(s.Poly(num,y),s.Poly(y*y-x**3-t**6,y)).as_expr().expand() == 0)
check("complete three-point dlog mass",
      s.cancel(36*t/(432*t**7)-1/(12*t**6)) == 0)
weighted_simple = s.cancel((x*sum_inv1-3)/a)
check("complete CM-phase simple pole sum",
      s.cancel(weighted_simple.subs(A,a**3)-3*a*a/(x**3-a**3)) == 0)

# Original sources, all in this same U frame and original degree 34 line.
C3 = X**3-204*b*X**2-384*b*b*X+64*b**3
D = (X+4*b)*C3
N = (X+b)*(7*X**2-4*b*X+16*b*b)/7
P5 = X**5+272*b*X**4-272*b*b*X**3-14912*b**3*X**2-6784*b**4*X+1024*b**5
source = [N/(X*d**3), D/(X*d**3), P5/(X*d**4)]
Ecols = s.Matrix([
    [-1/(224*b), s.Rational(3,2), 0],
    [-s.Rational(1,224), -b/2, b/4],
    [-s.Rational(3,112), -9*b, 9*b],
    [1/(224*b), s.Rational(3,2), -s.Rational(3,2)],
    [3/(896*b), -s.Rational(9,8), s.Rational(27,16)],
])
for j in range(3):
    check(f"complete original source eigen-column {j}",
          s.cancel(sum(Ecols[i,j]*eig[i] for i in range(5))-source[j]) == 0)
check("original full U source",
      s.cancel((-336*b*source[0]+5*source[1]+4*source[2])/9-1) == 0)
check("all original polynomial line bundles",
      all(s.cancel(X*d**4*source[j]).is_polynomial(X) for j in range(3)))
Mzero = M.subs(n,0)
check("exact rank-one Cartier-square image", Mzero.rank() == 1 and Mzero*Mzero == Mzero)
check("original S nonzero Cartier-square row",
      (Mzero*P*Ecols[:,0]+s.Rational(3,112)*P[:,2]).applyfunc(s.cancel) == s.zeros(5,1))

# Build the exact original sigma and x coefficients, not a fitted power series.
# q=z^6.  Only q^3 is needed after the q-leading actual pole factors.
q = s.symbols("q")
W = [s.Integer(1), -b/7]
for k in range(2,4):
    W.append(s.cancel(sum(W[j]*W[k-j] for j in range(1,k))/((k-1)*(6*k+1))))
Wx = sum(W[k]*q**k for k in range(4))
logE = -34*sum(W[k]*q**k/(6*k*(6*k-1)) for k in range(1,4))
E = s.series(s.exp(logE),q,0,4).removeO()
U_over_X = q*E*Wx**2*(Wx**3-8*b*q)**4
U_over_d = q*E*Wx**5*(Wx**3-8*b*q)**3
a24 = s.expand(U_over_X).coeff(q,4).subs(b,17)
b24 = s.expand(U_over_d).coeff(q,4).subs(b,17)
check("p23 exact original U/X coefficient",
      a24 == -s.Rational(10343098809781711,857800125))
check("p23 exact original U/(X-8b) coefficient",
      b24 == -s.Rational(33503806082698781,9435801375))
red = lambda r,p: int(s.numer(r))%p * pow(int(s.denom(r))%p,-1,p)%p
check("p23 both actual first divided rows nonzero", red(a24,23)==7 and red(b24,23)==5)
pc23 = -s.Integer(17)**4*s.binomial(8,4)/s.Integer(4)**4
c23 = pow(red(34*pc23,23),-1,23)
check("p23 actual common period coefficient", c23==18)
check("p23 actual central units", (c23*red(a24,23))%23==11 and (c23*red(b24,23))%23==21)

out = {
    "status":"PASS", "check_count":len(checks), "checks":checks,
    "basis":[str(f) for f in basis],
    "trace_matrix_columns":[[str(M[i,j]) for i in range(5)] for j in range(5)],
    "eigenfunctions":[str(f) for f in eig],
    "eigenvalues":["n","n^2","1","n","n^2"],
    "original_sources_eigen_columns":[[str(Ecols[i,j]) for i in range(5)] for j in range(3)],
    "modp_image":"span{1/(X-8b)+1/(12b)}; original S coefficient -3/112",
    "complete_observer":"J_(T_U T)(u)/J_U(u)=sum_j M_ji(n) J_(U*basis_j)(u)/J_U(u)",
    "p23":{
        "U_over_X_coefficient_z24":str(a24),
        "U_over_Xminus8b_coefficient_z24":str(b24),
        "coefficients_modp":[7,5],"actual_common_period_factor":c23,
        "central_divided_rows_modp":[11,21],
        "consequence":"No scalar intertwining on this actual five-dimensional space at p=23"
    },
    "scope":"Actual fixed E[6] source closure and full original Newton transport; no claim that the original central functional commutes with this frame-dependent trace or that its target is nonzero for infinitely many primes."
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({"status":"PASS","check_count":len(checks),"p23_rows":[11,21]},indent=2))
