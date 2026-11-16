#!/usr/bin/env sage -python
"""Exact original cusp-integral Hecke lattice and certified degree bounds.

Public Actions only. Needs the adjacent committed R873 producer, no data file:
  sage -python check-r874-original-cusp-integral-hecke-lattice.py \
    --M 1024 --bits 384 --radius 2 --top 12
No map or shadow is declared constructed by this lattice computation.
"""
import os
import time
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Mathematical execution is restricted to the public repository Actions.")
STARTED = time.monotonic()
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
from sage.all import QQ, ZZ, PolynomialRing, NumberField, RealBallField
from sage.all import ComplexBallField, matrix, vector, identity_matrix, diagonal_matrix
from sage.env import SAGE_VERSION


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--M', type=int, default=1024)
    ap.add_argument('--bits', type=int, default=384)
    ap.add_argument('--radius', type=int, default=2)
    ap.add_argument('--top', type=int, default=12)
    args = ap.parse_args()
    assert args.M >= 17 and args.bits >= 192
    assert 1 <= args.radius <= 6 and 1 <= args.top <= 30
    producer_path = Path(__file__).with_name('check-r873-original-cm-petersson-degree.py')
    assert producer_path.is_file(), "the exact committed R873 producer is required"
    spec = importlib.util.spec_from_file_location("r873_original", str(producer_path))
    r873 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r873)

    Qx = PolynomialRing(QQ, 'x')
    x = Qx.gen()
    F = NumberField(x**3-17, 'a')
    a = F.gen()
    Fy = PolynomialRing(F, 'y')
    y = Fy.gen()
    L = F.extension(y**2+y+1, 'om')
    om = L.gen()
    alpha = -1+2*om
    cc = -1-19*om
    v = F(-122465)-47628*a-(QQ(314892)/17)*a*a
    assert v**3+367395*v*v+147*v+QQ(1)/17 == 0

    def ell(t):
        return ((21905009-23122022*om)
                +(112353990182+54575060764*om)*t
                +(305813+148546*om)*t*t)/25505280

    ell0 = ell(L(v))
    tv = alpha**3*v/ell0**3
    ell1 = ell(tv)
    ttv = alpha**3*tv/ell1**3
    ell2 = ell(ttv)
    assert alpha**3*ttv/ell2**3 == L(v)
    assert ell0*ell1*ell2 == cc
    u1, u2 = ell2, cc/ell0

    def descend(z):
        p = z.polynomial()
        assert p[1] == 0
        return F(p[0])

    c1 = descend(u1/alpha+(alpha/cc)*u2)
    c2 = descend((alpha*alpha/cc)*u1+u2/(alpha*alpha))
    lambdas = [F(1), c1, c2]
    OFbasis = [F(1), a, (a*a-a+1)/3]
    assert OFbasis[2]**3-OFbasis[2]**2+6*OFbasis[2]-12 == 0
    assert F.discriminant() == -867

    def coords_F(z):
        p = F(z).polynomial()
        return vector(QQ, [p[0]-p[2], p[1]+p[2], 3*p[2]])

    def poly_F(z):
        p = F(z).polynomial()
        return [str(p[i]) for i in range(3)]

    def all_integral(mat):
        return all(QQ(t).denominator() == 1 for t in mat.list())

    M0 = identity_matrix(QQ, 3)
    M1 = matrix(QQ, [[0, 2, -1], [1, 0, 1], [0, 1, 0]])
    M2 = matrix(QQ, [[0, -1, 2], [0, 1, -1], [1, 0, -1]])
    blocks = []
    for Mk in [M0, M1, M2]:
        columns = []
        for j in range(3):
            val = sum(lambdas[i]*Mk[i,j] for i in range(3))/a
            columns.append(coords_F(val))
        blocks.append(matrix(QQ, columns).transpose())
    B = blocks[0].stack(blocks[1]).stack(blocks[2])
    B0 = blocks[0]
    assert B0.det() != 0
    lower = blocks[1].stack(blocks[2])*B0.inverse()
    denominator = ZZ(1)
    for t in lower.list():
        denominator = denominator.lcm(ZZ(t.denominator()))
    M = matrix(ZZ, denominator*lower)
    S, left, right = M.smith_form()
    assert left*M*right == S
    assert abs(left.det()) == 1 and abs(right.det()) == 1
    scales = [denominator // denominator.gcd(abs(ZZ(S[i,i]))) for i in range(3)]
    z_basis = right*diagonal_matrix(ZZ, scales)
    lattice_basis = B0.inverse()*z_basis
    common = ZZ(1)
    for t in lattice_basis.list():
        common = common.lcm(ZZ(t.denominator()))
    integral_columns = matrix(ZZ, common*lattice_basis)
    canonical = integral_columns.transpose().hermite_form().transpose()
    lattice_basis = matrix(QQ, canonical)/common
    assert all_integral(B*lattice_basis)
    ideal_norm = abs(lattice_basis.det())
    assert ideal_norm > 0
    assert all_integral(lattice_basis.inverse()*M1*lattice_basis)
    assert all_integral(lattice_basis.inverse()*M2*lattice_basis)

    E = NumberField(x**3-3*x+1, 'th')
    th = E.gen()
    assert E.discriminant() == 81
    Ebasis = [E(1), th, th*th-2]

    def field_u(col):
        return sum(Ebasis[i]*col[i] for i in range(3))

    def u_coordinates(u):
        p = E(u).polynomial()
        return vector(QQ, [p[0]+2*p[2], p[1], p[2]])

    exact_basis = [field_u(lattice_basis.column(i)) for i in range(3)]
    for eu in exact_basis:
        assert abs(QQ(eu.norm())/ideal_norm).denominator() == 1

    seed = vector(QQ, [3, 0, 1])  # th^2+1, norm 17, actual bad-17 direction
    seed_eval = B*seed
    assert field_u(seed).norm() == 17

    # Recompute the rigorous norms, not by importing a rounded prior output.
    R = RealBallField(args.bits)
    C = ComplexBallField(args.bits)
    pi = R.pi()
    z = (2*pi*C(0,1)/9).exp()
    omc = z**3
    alphac = -1+2*omc
    bvals = [alphac*z**(2+3*j) for j in range(3)]
    theta_values = [(z**(2+3*j)+z**(-2-3*j)).real() for j in range(3)]
    roots = [z**e for e in [1,7,4]]
    aa = (R(17).log()/3).exp()

    def eval_F(t):
        p = F(t).polynomial()
        return R(p[0])+R(p[1])*aa+R(p[2])*aa*aa

    def eval_L(t):
        p = L(t).polynomial()
        return C(eval_F(p[0]))+C(eval_F(p[1]))*omc

    def real(zv):
        zv = C(zv)
        assert zv.imag().contains_zero()
        return zv.real()

    u1c, u2c = eval_L(u1), eval_L(u2)
    G = [1+u1c/bb+u2c/(bb*bb) for bb in bvals]
    K, ac, Ac, ideals, coeff_hash = r873.exact_coefficients(args.M)

    def eval_K9(t, zz):
        ans = C(0)
        for q in reversed(list(t.polynomial())):
            ans = ans*zz+C(q)
        return ans

    Q = R(867).sqrt()/(2*pi)
    rr = (-1/Q).exp()
    mmax = args.M
    tail = rr**(mmax+1)*(1/(1-rr)+(2/Q)*((mmax+1)/(1-rr)+rr/(1-rr)**2))
    Lvalues = []
    for j in range(3):
        vv = R(0)
        for m in range(1, mmax+1):
            am = real(eval_K9(Ac[m], roots[j]))
            vv += am*(-R(m)/Q).exp()*(R(1)/(m*m)+2/(Q*m))
        vv = vv.add_error(tail)
        assert vv > 0
        Lvalues.append(vv)
    area0 = R(QQ(1)/3).gamma()**2*R(QQ(1)/6).gamma()**2/(4*pi*R(3).sqrt())
    vreal = eval_F(v)
    area = area0/(((-vreal/2).log()*R(2)/3).exp())
    weights = [136*real(G[j]*G[j].conjugate())*Lvalues[j]/(R(3).sqrt()*area)
               for j in range(3)]
    assert all(w > 0 for w in weights)
    geomean = ((weights[0]*weights[1]*weights[2]).log()/3).exp()
    global_lower = 3*geomean*(R(ideal_norm).log()*R(2)/3).exp()

    def embeddings(col):
        return [R(col[0])+R(col[1])*t+R(col[2])*(t*t-2) for t in theta_values]

    def degree(col):
        vals = embeddings(col)
        return sum(weights[j]*vals[j]*vals[j] for j in range(3))

    # Integer LLL is used only to choose candidates.  Every displayed degree
    # is independently enclosed by the original positive quadratic form.
    denom_scale = ZZ(2)**128
    rounded_rows = []
    for i in range(3):
        vals = embeddings(lattice_basis.column(i))
        rounded_rows.append([ZZ((vals[j]*weights[j].sqrt()*denom_scale).mid().round())
                             for j in range(3)])
    rounded = matrix(ZZ, rounded_rows)
    assert rounded.det() != 0
    reduced, transform = rounded.LLL(transformation=True)
    assert transform*rounded == reduced and abs(transform.det()) == 1
    reduced_basis = lattice_basis*matrix(QQ, transform.transpose())
    assert all_integral(B*reduced_basis)

    candidates = []
    seen = set()
    for zz in itertools.product(range(-args.radius,args.radius+1), repeat=3):
        if zz == (0,0,0):
            continue
        if next(t for t in zz if t) < 0:
            continue
        col = reduced_basis*vector(ZZ, zz)
        key = tuple(str(t) for t in col)
        if key in seen:
            continue
        seen.add(key)
        u = field_u(col)
        assert u != 0 and all_integral(matrix(QQ, 9, 1, list(B*col)))
        inverse = u_coordinates(1/u)
        multiplier = ZZ(1)
        for t in inverse:
            multiplier = multiplier.lcm(ZZ(t.denominator()))
        return_polynomial = vector(ZZ, [multiplier*t for t in inverse])
        assert u*field_u(return_polynomial) == multiplier
        # Necessary by the original bad-17 Neron argument, now a useful check.
        assert multiplier % 17 == 0
        dg = degree(col)
        assert dg > 0
        leading = sum(lambdas[i]*col[i] for i in range(3))
        assert leading != 0
        norm_ratio = abs(QQ(u.norm()))/ideal_norm
        assert norm_ratio.denominator() == 1
        candidates.append((float(dg.mid()), {
            "coordinates_1_th_eps2": list(key),
            "exact_norm": str(u.norm()),
            "norm_index_in_cusp_ideal": str(norm_ratio),
            "leading_coefficient_in_1_a_a2": poly_F(leading),
            "quasidegree": str(dg),
            "return_integer_m": str(multiplier),
            "return_hecke_polynomial_1_th_eps2": [str(t) for t in return_polynomial],
            "would_exceed_weight_caps": {str(k): bool(dg > 102*k) for k in [2,4,6,8]}
        }))
    candidates.sort(key=lambda x:(x[0],x[1]["coordinates_1_th_eps2"]))

    def serial(mat):
        return [[str(mat[i,j]) for j in range(mat.ncols())] for i in range(mat.nrows())]

    lattice_report = {
        "lambda_1_th_eps2": [poly_F(t) for t in lambdas],
        "OF_basis": ["1", "a", "(a^2-a+1)/3"],
        "constraint_matrix_9_by_3": serial(B),
        "cusp_ideal_column_basis": serial(lattice_basis),
        "cusp_ideal_norm": str(ideal_norm),
        "smith_denominator": str(denominator),
        "smith_diagonal": [str(S[i,i]) for i in range(3)],
        "smith_scales": [str(t) for t in scales],
        "OE_stable": True,
        "seed_th_squared_plus_1": {
            "norm": "17",
            "global_cusp_integral": all(t.denominator()==1 for t in seed_eval),
            "nine_constraints": [str(t) for t in seed_eval]
        }
    }
    report_hash = hashlib.sha256(json.dumps(lattice_report,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    result = {
        "status": "PASS",
        "sage_version": SAGE_VERSION,
        "parameters": vars(args),
        "R873_dependency_sha256": hashlib.sha256(producer_path.read_bytes()).hexdigest(),
        "coefficient_sha256": coeff_hash,
        "lattice_sha256": report_hash,
        "exact_lattice": lattice_report,
        "norms": {
            "L_beta_squared_at_2": [str(t) for t in Lvalues],
            "uniform_absolute_tail": str(tail),
            "original_positive_weights": [str(t) for t in weights],
            "global_cusp_integral_packet_degree_lower": str(global_lower),
            "all_true_packet_maps_exceed_caps": {str(k): bool(global_lower>102*k) for k in [2,4,6,8]}
        },
        "LLL_column_basis": serial(reduced_basis),
        "candidate_count": len(candidates),
        "best_candidates": [r for _,r in candidates[:args.top]],
        "scope": {
            "cusp_integral_implies_actual_hom": False,
            "candidate_is_global_shortest": False,
            "original_coordinate_certificate_passed": False,
            "original_shadow_nonzero": False
        }
    }
    result["run"] = {
        "source": os.environ.get("RANK2_SOURCE_SHA"),
        "run_id": os.environ.get("RANK2_RUN_ID"),
        "run_attempt": os.environ.get("RANK2_RUN_ATTEMPT"),
        "image": os.environ.get("RANK2_IMAGE"),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "readme_blobs": {"README.md": os.environ.get("RANK2_ROOT_README_SHA"),
            "topics/rank2-sha-infinitely-many-p/README.md": os.environ.get("RANK2_TOPIC_README_SHA")},
        "elapsed_seconds": time.monotonic()-STARTED
    }
    payload = json.dumps(result,sort_keys=True,separators=(',',':'))
    print("RANK2_CUSP_LATTICE_RESULT "+payload,flush=True)
    print("RANK2_CUSP_LATTICE_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(),flush=True)


if __name__ == '__main__':
    main()
