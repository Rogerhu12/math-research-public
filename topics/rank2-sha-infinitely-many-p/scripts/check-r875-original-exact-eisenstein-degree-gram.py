#!/usr/bin/env sage-python
"""Exact original 17-torsion Eisenstein degree Gram; public Actions only."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical producer only in the public repository Actions.")
import hashlib
import json
import time
from pathlib import Path
from sage.all import QQ, PolynomialRing, EllipticCurve, NumberField, matrix, vector
from sage.env import SAGE_VERSION

started = time.monotonic()
def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
def digest(obj):
    return hashlib.sha256(canonical(obj).encode()).hexdigest()
def stage(label):
    print("RANK2_EXACT_GRAM_STAGE " + canonical({
        "stage": label, "elapsed_seconds": time.monotonic()-started}), flush=True)
def qvec(t, length):
    p = t.lift()
    return [p[i] for i in range(length)]
def qstrings(v):
    return [str(QQ(t)) for t in v]
def qmatrix(M):
    return [qstrings(row) for row in M.rows()]

stage("original division polynomial, product and sum on the same H32 orbit")
RX = PolynomialRing(QQ, "x")
x = RX.gen()
E0 = EllipticCurve(QQ, [0, 1])
psi = RX(E0.division_polynomial(17))
assert psi.degree() == 144 and psi.leading_coefficient() == 17
assert psi[0] == -QQ(2)**96
A = RX.quotient(psi.monic(), "xp")
xp = A.gen()
point = xp
h = A.one()
T0 = A.zero()
for k in range(16):
    h *= point
    T0 += point
    point = -(point**3 + 4)/(3*point**2)
assert point == xp
vA = h**3 / QQ(2)**32
assert vA**3 + 367395*vA**2 + 147*vA + QQ(1)/17 == 0
# T0/h lies in Q(v): solve and verify the entire 144-coordinate identity.
basis = [h, h*vA, h*vA**2]
columns = [qvec(t, 144) for t in basis]
B = matrix(QQ, 144, 3, lambda i,j: columns[j][i])
assert B.rank() == 3
trace_coeff = B.solve_right(vector(QQ, qvec(T0, 144)))
assert B*trace_coeff == vector(QQ, qvec(T0, 144))
def trace_poly(t):
    return sum((trace_coeff[i]*t**i for i in range(3)), t.parent().zero())

stage("original oriented norm-seven automorphism and cubic cocycle")
RK = PolynomialRing(QQ, "w")
w = RK.gen()
K = NumberField(w**2+w+1, "omega")
omega = K.gen()
delta = 1+2*omega
alpha = -1+2*omega
cc = -1-19*omega
assert alpha**3*omega**2 == cc
PV = PolynomialRing(K, "V")
V = PV.gen()
L = PV.quotient(V**3+367395*V**2+147*V+QQ(1)/17, "v")
v = L.gen()
def ell(t):
    return ((21905009-23122022*omega) +
            (112353990182+54575060764*omega)*t +
            (305813+148546*omega)*t**2)/25505280
tau_v = alpha**3*v/ell(v)**3
tau2_v = alpha**3*tau_v/ell(tau_v)**3
tau3_v = alpha**3*tau2_v/ell(tau2_v)**3
assert tau3_v == v and tau_v != v
assert ell(v)*ell(tau_v)*ell(tau2_v) == cc
u1 = ell(tau2_v)
u2 = cc/ell(v)
t0 = trace_poly(v)
t1 = (alpha/ell(v))*trace_poly(tau_v)
t2 = (alpha**2/(ell(v)*ell(tau_v)))*trace_poly(tau2_v)
# sigma^3 h = omega*h, so all nine coset sums follow from these three.
assert alpha**3/cc == omega

# Verify that the algebraic sigma is the original [alpha], not the inverse lift.
PK = PolynomialRing(K, "xk")
xk = PK.gen()
Rat = PK.fraction_field()
c7 = (-2+6*delta)/7
r7 = Rat((xk**7+(12-28*c7)*xk**4+(7*c7**2-24*c7)*xk) /
         (alpha**2*(xk**3+c7)**2))
assert (xk**3+1)*r7.derivative()**2/alpha**2 == r7**3+1
AK = PK.quotient(PK(psi.monic()), "xpk")
xpk = AK.gen()
alpha_x = AK(r7.numerator())/AK(r7.denominator())
hK = AK(PK(h.lift()))
vK = hK**3/QQ(2)**32
hsigma = PK(h.lift())(alpha_x)
assert hsigma == alpha*hK/ell(vK)
T0sigma = PK(T0.lift())(alpha_x)
assert T0sigma == hsigma*trace_poly(hsigma**3/QQ(2)**32)

stage("three-root Fourier trace and exact rational degree Gram")
# Work in L[zeta]/(zeta^3-omega^2), represented by three coefficients.
# Its trace over L is 3 times the constant coefficient.
zero = L.zero()
one = L.one()
def cmul(a, b):
    out = [zero, zero, zero]
    for i in range(3):
        for j in range(3):
            n = i+j
            factor = one
            if n >= 3:
                n -= 3
                factor = L(omega**2)
            out[n] += factor*a[i]*b[j]
    return tuple(out)
def cscale(a, s):
    return tuple(s*t for t in a)
G = (one, L(omega)*u2/alpha**2, L(omega)*u1/alpha)
Tf = (t0, L(omega)*t1, L(omega**2)*t2)
W = cscale(cmul(cmul(G, G), Tf), -QQ(8192)/51*v)
eb = [
    (one, zero, zero),
    (zero, one, L(omega)),
    (zero, L(omega), one)
]
def rational_constant(t):
    p = L(t).lift()
    assert p.degree() <= 0, "Gram entry did not descend from the original cubic field"
    k = K(p[0])
    coeff = k.list()
    coeff += [QQ(0)]*(2-len(coeff))
    assert coeff[1] == 0, "Gram entry did not descend from K to Q"
    return QQ(coeff[0])
Q = matrix(QQ, 3, 3, lambda i,j:
           rational_constant(3*cmul(W, cmul(eb[i], eb[j]))[0]))
assert Q == Q.transpose()
assert all(Q[:i,:i].determinant() > 0 for i in (1,2,3))

stage("original cusp-ideal generator and exact polarized return")
PE = PolynomialRing(QQ, "theta_var")
theta_var = PE.gen()
EF = NumberField(theta_var**3-3*theta_var+1, "theta")
theta = EF.gen()
eps2 = theta**2-2
u = (915+1097*theta+2962*eps2)/55569
ret = 106+59*theta+185*eps2
assert u*ret == 17
assert u.norm() == -QQ(17)/55569
basis_E = [EF.one(), theta, eps2]
def ecoords(t):
    p = EF(t).list()
    p += [QQ(0)]*(3-len(p))
    return vector(QQ, [p[0]+2*p[2], p[1], p[2]])
cols_U = [ecoords(u*t) for t in basis_E]
U = matrix(QQ, 3, 3, lambda i,j: cols_U[j][i])
QI = U.transpose()*Q*U
assert QI == QI.transpose()
assert QI.det() == u.norm()**2*Q.det()
candidate_degree = QI[0,0]
return_degree = (vector(QQ,[106,59,185])*QI*
                 vector(QQ,[106,59,185]).column())[0]
assert return_degree == 17**2*Q[0,0]

# Prove the same candidate is in the complete original q-integral ideal.
PA = PolynomialRing(QQ, "a_var")
a_var = PA.gen()
F = NumberField(a_var**3-17, "a17")
a17 = F.gen()
lambda_basis = [F.one(), -497+237*a17-17*a17**2,
                609-44*a17-75*a17**2]
def lam(t):
    cs = ecoords(t)
    return sum((cs[i]*lambda_basis[i] for i in range(3)), F.zero())
def ofcoords(t):
    p = F(t).list()
    p += [QQ(0)]*(3-len(p))
    return [p[0]-p[2], p[1]+p[2], 3*p[2]]
candidate_qcoords = [ofcoords(lam(u*t)/a17) for t in basis_E]
assert all(QQ(z).denominator() == 1 for row in candidate_qcoords for z in row)
assert lam(u) == (68+7*a17-13*a17**2)/3

result = {
    "kind": "rank2_original_exact_17_torsion_eisenstein_degree_gram",
    "status": "exact",
    "source": os.environ.get("RANK2_SOURCE_SHA"),
    "run_id": os.environ.get("RANK2_RUN_ID"),
    "run_attempt": os.environ.get("RANK2_RUN_ATTEMPT"),
    "sage_version": SAGE_VERSION,
    "image": os.environ.get("RANK2_IMAGE"),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "readme_blobs": {
        "README.md": os.environ.get("RANK2_ROOT_README_SHA"),
        "topics/rank2-sha-infinitely-many-p/README.md": os.environ.get("RANK2_TOPIC_README_SHA")
    },
    "parameters": {"torsion_prime":17, "orbit_length":16,
                   "curve":[0,0,0,0,1], "alpha":"-1+2*omega",
                   "gram_basis":["1","theta","theta^2-2"],
                   "theta_polynomial":"theta^3-3*theta+1"},
    "division_polynomial_sha256": digest(qstrings(psi.list())),
    "h_representative_sha256": digest(qstrings(qvec(h,144))),
    "T0_representative_sha256": digest(qstrings(qvec(T0,144))),
    "T0_over_h_in_v_basis": qstrings(trace_coeff),
    "degree_gram": qmatrix(Q),
    "degree_gram_determinant": str(Q.det()),
    "Xi0_quasi_degree": str(Q[0,0]),
    "candidate_u_coordinates": ["915/55569","1097/55569","2962/55569"],
    "candidate_norm": str(u.norm()),
    "candidate_ideal_basis_matrix": qmatrix(U),
    "candidate_ideal_degree_gram": qmatrix(QI),
    "candidate_ideal_gram_determinant": str(QI.det()),
    "candidate_ideal_gram_integral":
        all(t.denominator() == 1 for t in QI.list()),
    "candidate_q_integrality_matrix": [qstrings(row) for row in candidate_qcoords],
    "candidate_exact_quasi_degree": str(candidate_degree),
    "candidate_degree_equals_376": bool(candidate_degree == 376),
    "candidate_degree_at_most_408": bool(candidate_degree <= 408),
    "candidate_degree_at_most_527": bool(candidate_degree <= 527),
    "integer_return_multiplier":17,
    "integer_return_hecke_coordinates":["106","59","185"],
    "completed_identities":[
        "original H32 product and sum in the full 144-dimensional division algebra",
        "T0/h in Q(v), verified in all 144 coordinates",
        "original oriented norm-seven CM map and original cocycle",
        "sigma cubed acts by omega on h and the coset trace",
        "three-root Fourier trace, with the original period and minus sign",
        "all six degree Gram entries are exact rational constants",
        "positive definite Gram, original candidate q-integrality and norm",
        "exact integer Hecke return u*(106+59theta+185(theta^2-2))=17"
    ],
    "not_claimed":[
        "cusp q-integrality implies an actual integral Hom",
        "the candidate elliptic coordinates have already been reconstructed",
        "an exact integral quasi-degree proves an integral Hom",
        "the original endpoint Frobenius shadow is nonzero"
    ],
    "elapsed_seconds":time.monotonic()-started
}
payload = canonical(result)
print("RANK2_EXACT_GRAM_RESULT " + payload, flush=True)
print("RANK2_EXACT_GRAM_SHA256 " + hashlib.sha256(payload.encode()).hexdigest(), flush=True)
