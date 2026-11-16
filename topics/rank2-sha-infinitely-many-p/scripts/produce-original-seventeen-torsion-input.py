#!/usr/bin/env sage-python
"""Produce the original fixed 17-torsion CM input in public Actions only."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("This mathematical producer runs only in the public repository Actions.")
import hashlib
import json
import time
from pathlib import Path
from sage.all import QQ, PolynomialRing, EllipticCurve, NumberField, matrix, vector
from sage.env import SAGE_VERSION

started = time.monotonic()
def progress(stage):
    print("RANK2_17_STAGE " + json.dumps({"stage": stage, "elapsed": time.monotonic()-started}), flush=True)
def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
def digest(obj):
    return hashlib.sha256(canonical(obj).encode()).hexdigest()
def qvec(a, length):
    poly = a.lift()
    return [poly[i] for i in range(length)]
def rational_list(items):
    return [str(QQ(x)) for x in items]

progress("exact division polynomial and H32 orbit")
R = PolynomialRing(QQ, "x")
x = R.gen()
E = EllipticCurve(QQ, [0, 1])
psi = R(E.division_polynomial(17))
assert psi.degree() == 144 and psi.leading_coefficient() == 17
assert psi[0] == -QQ(2)**96
A = R.quotient(psi.monic(), "z")
z = A.gen()
orbit = z
h = A.one()
for i in range(16):
    h *= orbit
    orbit = -(orbit**3 + 4) / (3*orbit**2)
assert orbit == z
h_coeffs = rational_list(qvec(h, 144))
progress("nine dimensional h relation")
powers = [A.one()]
for i in range(9):
    powers.append(powers[-1]*h)
cols = [qvec(v, 144) for v in powers]
mat = matrix(QQ, 144, 10, lambda i,j: cols[j][i])
relations = mat.right_kernel()
assert relations.dimension() == 1
rel = relations.basis()[0]
assert rel[9] != 0
rel = rel / rel[9]
T = PolynomialRing(QQ, "T")
tvar = T.gen()
minpoly = T(list(rel))
assert minpoly.degree() == 9
assert minpoly(h) == 0
assert all(minpoly[i] == 0 for i in (1,2,4,5,7,8))
assert minpoly[0] == QQ(2)**96 / 17
cubic = tvar**3 + minpoly[6]*tvar**2 + minpoly[3]*tvar + minpoly[0]
t = h**3
assert cubic(t) == 0

progress("pure cubic coordinate")
L = NumberField(tvar**3 - 17, "a17")
roots = cubic.roots(L)
assert len(roots) == 1 and roots[0][1] == 1
pure_t = roots[0][0]
pure_coeffs = [pure_t.polynomial()[i] for i in range(3)]

progress("exact norm seven endomorphism and original Frobenius")
K = NumberField(tvar**2 + tvar + 1, "omega")
omega = K.gen()
delta = 1 + 2*omega
alpha = -1 + 2*omega
RK = PolynomialRing(K, "xk")
xk = RK.gen()
Frac = RK.fraction_field()
c7 = (-2 + 6*delta)/7
r7 = Frac((xk**7 + (12-28*c7)*xk**4 + (7*c7**2-24*c7)*xk) /
          (alpha**2*(xk**3+c7)**2))
# The y coordinate is r7'(x)*y/alpha; this identity fixes the CM orientation.
assert (xk**3+1)*r7.derivative()**2/alpha**2 == r7**3+1
AK = RK.quotient(RK(psi.monic()), "zk")
zk = AK.gen()
hK = AK(RK(h.lift()))
tK = hK**3
alpha_x = AK(r7.numerator()) / AK(r7.denominator())
h_sigma = RK(h.lift())(alpha_x)
lambda7 = alpha*hK/h_sigma
t_sigma = h_sigma**3
basis = [AK.one(), tK, tK**2]
bcols = [qvec(v, 144) for v in basis]
bmat = matrix(K, 144, 3, lambda i,j: bcols[j][i])
lambda_coeff = bmat.solve_right(vector(K, qvec(lambda7,144)))
tau_coeff = bmat.solve_right(vector(K, qvec(t_sigma,144)))
assert bmat*lambda_coeff == vector(K, qvec(lambda7,144))
assert bmat*tau_coeff == vector(K, qvec(t_sigma,144))
def eval_basis(coeff, arg):
    return sum((coeff[i]*arg**i for i in range(3)), AK.zero())
t_sigma2 = eval_basis(tau_coeff, t_sigma)
t_sigma3 = eval_basis(tau_coeff, t_sigma2)
assert t_sigma != tK and t_sigma3 == tK
lambda_norm = lambda7*eval_basis(lambda_coeff,t_sigma)*eval_basis(lambda_coeff,t_sigma2)
assert lambda_norm == -1-19*omega
# The quotient alpha*h/h_sigma fixes the original lift, not an arbitrary norm solution.
def kpair(v):
    v = K(v)
    return [str(QQ(v.polynomial()[i])) for i in range(2)]

result = {
    "kind": "rank2_original_seventeen_torsion_input",
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
    "parameters": {"ell":17,"curve":[0,0,0,0,1],"orbit_length":16,
                   "cm_delta":"1+2*omega","frobenius_alpha":"-1+2*omega"},
    "division_polynomial_sha256": digest(rational_list(psi.list())),
    "h_representative_sha256": digest(h_coeffs),
    "h_minpoly_coefficients_ascending": rational_list(minpoly.list()),
    "h_cubed_minpoly_coefficients_ascending": rational_list(cubic.list()),
    "h_cubed_in_Q_cuberoot17_ascending": rational_list(pure_coeffs),
    "tau_on_h_cubed_coefficients_ascending_omega_basis": [kpair(v) for v in tau_coeff],
    "lambda7_coefficients_ascending_omega_basis": [kpair(v) for v in lambda_coeff],
    "lambda7_norm_omega_basis": ["-1","-19"],
    "completed_identities": [
        "division degree, leading coefficient and constant",
        "delta sixteen-fold x orbit closes",
        "h has exact degree nine by the one-dimensional relation kernel",
        "h polynomial and pure cubic coordinate",
        "oriented norm-seven CM rational map preserves E0",
        "original lambda and tau lie in the same cubic field",
        "tau has order three and lambda norm equals -1-19*omega"
    ],
    "elapsed_seconds": time.monotonic()-started
}
payload = canonical(result)
print("RANK2_17_INPUT_RESULT " + payload, flush=True)
print("RANK2_17_INPUT_SHA256 " + hashlib.sha256(payload.encode()).hexdigest(), flush=True)
