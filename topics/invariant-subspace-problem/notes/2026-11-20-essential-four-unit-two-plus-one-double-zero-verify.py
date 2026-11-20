#!/usr/bin/env python3
"""Exact original-source check for the rank-four unit (2+1) / double-zero branch.

No finite-field or floating-point calculation is used.  The only final
eliminations are gcds of explicit univariate polynomials over QQ.
"""
import hashlib
import json
import pathlib
import time
import sympy as S

_started = time.perf_counter()

R = S.Rational
rf = S.cancel
theta = S.symbols("theta")
A, B, C, X, Y, Z, b0 = S.symbols("A B C X Y Z b0")
a0 = 1 - b0
delta0 = 1 - 2*b0
coords = (X, Y, Z)
J = S.Matrix([[a0, 1, 0], [1, 0, 0], [0, 0, b0]])
K = S.Matrix([[0, 0, A], [0, C, B], [A, B, 0]])
yv = S.Matrix([a0, 1, b0])
cv = S.Matrix(coords)
H = J/4
mean = (yv.T*cv)[0]
Hform = (cv.T*H*cv)[0]
Vform = (a0*X**3 + 3*X**2*Y + b0*Z**3)/8
P = S.expand(mean**3 - 6*mean*Hform + 4*Vform)
diff = X-Z
assert S.expand(P - (
    Y**3 - 3*b0*diff*Y**2 - R(3,2)*b0*delta0*diff**2*Y
    - R(1,2)*a0*b0*delta0*diff**3
)) == 0
polar = K*yv
F0 = (yv.T*K*yv)[0]/2
Na = S.expand(
    sum(polar[i]*S.diff(P, coords[i]) for i in range(3))/3
    - F0*(mean**2 - 2*Hform)
    + 4*(cv.T*H*K*H*cv)[0]
)

# Reconstruct the active complete mean equations from the Frobenius algebra.
evec = S.Matrix([b0*A**2, 2*b0*A*B, a0*A**2+2*A*B])
dsquare = S.Matrix([polar[0]**2, 2*polar[0]*polar[1], polar[2]**2])
Ederived = evec - 2*K*J*polar - 2*dsquare + 4*F0*polar
E = [
    -b0*delta0**2*A**2 - 2*b0*delta0*A*B + 2*b0*A*C,
    2*b0**2*delta0*A*B - 2*b0*(1+2*b0)*A*C
        - 2*b0*delta0*B**2 + 6*b0*B*C + 2*C**2,
    -a0*delta0**2*A**2 - 2*delta0**2*A*B - 2*b0*A*C
        - 2*delta0*B**2 + 2*B*C,
]
assert all(S.expand(Ederived[i]-E[i]) == 0 for i in range(3))

D = 3*theta**2 + 1
rho = -(theta**2+1)/D
b = (theta**2+1)**3/D**2
a = 1-b
sigma = theta*rho
delta = 1-2*b
U0, U1, U2 = sigma-rho, rho+b, sigma-rho-1
assert rf(2*rho**3-b*(3*rho+1)) == 0
assert rf(sigma**2-(b-rho**2)) == 0
assert rf(U0-U2-1) == 0

nA = 2*b*((1-4*b)*rho**2+(2-6*b)*rho+delta-a*b
           - sigma*(rho+1)*delta)
nB = 2*b*(4*rho**2+3*rho+1-b-sigma*(2*rho+1))
nC = 4*rho**2-b-2*sigma*rho
n = [rf(nA), rf(nB), rf(nC)]
for par, want in zip((A, B, C), n):
    got = 4*Na.coeff(par).subs(b0, b).subs(
        {X: U0, Y: U1, Z: U2}, simultaneous=True
    )
    assert rf(got-want) == 0
target = [
    rf(b-2*rho**2),
    rf(2*rho*(rho+b)),
    rf(b-2*rho**2-2*rho-1),
]

# Eliminate C by the necessary original N value at the double base.
alpha, beta = rf(-n[0]/n[2]), rf(-n[1]/n[2])
matrix = [
    [
        -b*delta**2+2*b*alpha,
        -2*b*delta+2*b*beta,
        S.Integer(0),
    ],
    [
        -2*b*(1+2*b)*alpha+2*alpha**2,
        -2*b*(1+2*b)*beta+2*b**2*delta+6*b*alpha+4*alpha*beta,
        -2*b*delta+6*b*beta+2*beta**2,
    ],
    [
        -a*delta**2-2*b*alpha,
        -2*delta**2-2*b*beta+2*alpha,
        -2*delta+2*beta,
    ],
]
matrix = [[rf(v) for v in row] for row in matrix]
for i in range(3):
    actual = E[i].subs(b0, b).subs(C, alpha*A+beta*B)
    expected = matrix[i][0]*A**2+matrix[i][1]*A*B+matrix[i][2]*B**2
    assert rf(actual-expected) == 0

def determinant(m):
    return rf(
        m[0][0]*m[1][1]*m[2][2]
        +m[0][1]*m[1][2]*m[2][0]
        +m[0][2]*m[1][0]*m[2][1]
        -m[0][2]*m[1][1]*m[2][0]
        -m[0][1]*m[1][0]*m[2][2]
        -m[0][0]*m[1][2]*m[2][1]
    )

det = determinant(matrix)
f = 2*theta**3+2*theta**2+theta-1
g = 7*theta**4+4*theta**3+11*theta**2+2
F7 = 15*theta**7+15*theta**6+54*theta**5+14*theta**4 \
    +47*theta**3-17*theta**2+12*theta-12
det_want = 16*(theta-1)**4*(theta+1)**6*(theta**2+1)**6 \
    *(2*theta**2+1)*f/((theta+3)**3*D**8)
assert rf(det-det_want) == 0
monomials = []
for col in range(3):
    repl = [[target[i] if j == col else matrix[i][j]
             for j in range(3)] for i in range(3)]
    monomials.append(rf(determinant(repl)/det))
A2, AB, B2 = monomials
A2_want = -D**2*g/(2*(theta+1)*(theta**2+1)**2*(2*theta**2+1)*f)
assert rf(A2-A2_want) == 0
rankone = rf(AB**2-A2*B2)
rankone_want = theta**2*(theta+3)**2*D**2*F7 / (
    16*(theta+1)*(theta**2+1)**4*(2*theta**2+1)*f**2
)
assert rf(rankone-rankone_want) == 0

def pgcd(p, q):
    return S.gcd(S.Poly(p, theta, domain=S.QQ),
                 S.Poly(q, theta, domain=S.QQ)).monic()

# These are the complete determinant and A=0 exceptional obstructions.
assert pgcd(f, g).degree() == 0
assert pgcd(F7, g).degree() == 0

# Original highest equations at all three active jets determine V/A.
lam = A2
q = rf(AB/A2)  # B/A
h = rf(alpha+beta*q)  # C/A
p0 = a*b*delta/2
p1 = 3*b*delta*(a*q-h)/2
p2 = q**3-3*b*q**2-3*b*delta*q/2-a*b*delta/2
pquot = [
    p0/U0**2,
    p1/U0**2-2*U1*p0/U0**3,
    p2/U2**2,
]
dbar = [b, h+b*q, a+q]
Vbar = [rf(dbar[i]-2*lam*pquot[i]/3) for i in range(3)]
tauV = rf(a*Vbar[0]+Vbar[1]+b*Vbar[2])
Fbar = rf(a*b+b*q+h/2)
nbase = rf(b*delta*(a*(a+q)-h/2)/2)

# Independently check this coefficient from the original active N tensor.
assert rf(Na.subs({X: 0, Y: 0, Z: 1}, simultaneous=True)
          .subs({A: 1, B: q, C: h, b0: b}, simultaneous=True)-nbase) == 0

source = rf(
    lam*nbase + sigma*U0*(Vbar[0]-b)
    +(tauV-Fbar)*U0**2/2 + b*U2*U0/2
)
source_num, source_den = S.fraction(source)
source_poly = S.Poly(source_num, theta, domain=S.QQ).clear_denoms()[1].primitive()[1]
if source_poly.LC() < 0:
    source_poly = -source_poly
assert source_poly.degree() == 28
expected_den = (theta+1)**3*(2*theta**2+1)*D**4*f*g**2
assert not rf(source_den/expected_den).has(theta)
assert pgcd(F7, source_poly.as_expr()).degree() == 0

# The sole non-half root where nC=0 is theta=-3; do not divide there.
at = {theta: S.Integer(-3)}
ka = rf((-n[0]/n[1]).subs(at))
assert ka == R(117,98)
alt = [
    [
        -b*delta**2-2*b*delta*ka,
        2*b,
        S.Integer(0),
    ],
    [
        2*b**2*delta*ka-2*b*delta*ka**2,
        -2*b*(1+2*b)+6*b*ka,
        S.Integer(2),
    ],
    [
        -a*delta**2-2*delta**2*ka-2*delta*ka**2,
        -2*b+2*ka,
        S.Integer(0),
    ],
]
alt = [[rf(v.subs(at)) for v in row] for row in alt]
alt_target = [rf(v.subs(at)) for v in target]
alt_det = determinant(alt)
assert alt_det == R(-47500,16807)
alt_ans = []
for col in range(3):
    repl = [[alt_target[i] if j == col else alt[i][j]
             for j in range(3)] for i in range(3)]
    alt_ans.append(rf(determinant(repl)/alt_det))
assert alt_ans == [R(-686,475), R(234,175), R(-11070,16807)]
bad = rf(alt_ans[1]**2-alt_ans[0]*alt_ans[2])
assert bad == R(9936,11875)

print(json.dumps({
    "status": "PASS",
    "source_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
    "sympy_version": S.__version__,
    "elapsed_seconds": time.perf_counter()-_started,
    "field": "QQ",
    "original_active_mean_coefficients": 3,
    "original_active_N_coefficients": 3,
    "determinant_factorization": True,
    "rankone_factorization": True,
    "gcd_f_g_degree": 0,
    "gcd_F7_g_degree": 0,
    "highest_then_original_N_source_degree": source_poly.degree(),
    "gcd_F7_N_source_degree": 0,
    "theta_minus3_incompatibility": str(bad),
}, sort_keys=True))
