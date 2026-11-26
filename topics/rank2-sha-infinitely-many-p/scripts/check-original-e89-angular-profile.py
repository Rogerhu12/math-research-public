#!/usr/bin/env python3
"""Exact angular profile of the freshly rebuilt original E89 source.

Run only in this public repository's Actions.  Rebuilds the complete CM7/CM13
matrices and their common mass kernel in the same job.  No coefficient table,
matrix, polynomial gcd witness or other generated output is written to disk.
The proof of normalization and conductor is separate from this finite reader.
"""
from __future__ import annotations
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
import os
import pathlib
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
START = time.time()
MATRIX_SHA = "6ee0222d90db6add172d6d6e650a2f8186b1776072661594a242b4e65c78d665"
PRODUCER_SHA = "b5c2e3f6781e1a788e2d3fd749f10e2ecab9e6c58e2950aecc9acf727f237e67"

def trim(p):
    p = [Q(x) for x in p]
    while p and not p[-1]:
        p.pop()
    return p

def add(a, b):
    out = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)

def scale(a, c):
    return trim([c*x for x in a])

def mul(a, b):
    if not a or not b:
        return []
    out = [Q(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)

def product(factors, den=1):
    out = [Q(1)]
    for f in factors:
        out = mul(out, f)
    return scale(out, Q(1, den))

def divrem(a, b):
    a, b = trim(a), trim(b)
    assert b
    out = [Q(0)] * max(0, len(a)-len(b)+1)
    while a and len(a) >= len(b):
        i, c = len(a)-len(b), a[-1]/b[-1]
        out[i] += c
        for j, x in enumerate(b):
            a[i+j] -= c*x
        a = trim(a)
    return trim(out), a

def exact_div(a, b):
    q, r = divrem(a, b)
    assert not r
    assert mul(q, b) == trim(a)
    return q

def gcd_bezout(a, b):
    aa, bb = trim(a), trim(b)
    r0, r1, u0, u1, v0, v1 = aa, bb, [Q(1)], [], [], [Q(1)]
    while r1:
        q, r = divrem(r0, r1)
        r0, r1 = r1, r
        u0, u1 = u1, add(u0, scale(mul(q, u1), -1))
        v0, v1 = v1, add(v0, scale(mul(q, v1), -1))
    assert r0
    c = 1/r0[-1]
    g, u, v = scale(r0, c), scale(u0, c), scale(v0, c)
    assert add(mul(u, aa), mul(v, bb)) == g
    assert not divrem(aa, g)[1] and not divrem(bb, g)[1]
    return g, u, v

def resultant(a, b):
    a, b = trim(a), trim(b)
    assert a and b
    value = Q(1)
    while len(b) > 1:
        m, n = len(a)-1, len(b)-1
        if m < n:
            value *= (-1)**(m*n)
            a, b = b, a
            continue
        _, r = divrem(a, b)
        if not r:
            return Q(0)
        value *= (-1)**(m*n) * b[-1]**(m-(len(r)-1))
        a, b = b, r
    return value * b[0]**(len(a)-1)

def multiplicity(f, factor):
    f, factor = trim(f), trim(factor)
    assert f and len(factor) > 1
    n = 0
    while len(f) >= len(factor):
        q, r = divrem(f, factor)
        if r:
            break
        f, n = q, n+1
    return n

def evaluate(f, x):
    out = Q(0)
    for c in reversed(f):
        out = out*x+c
    return out

def canonical(value):
    return json.dumps(value, separators=(",", ":"), sort_keys=True).encode()

def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()

def rational_summary(x):
    x = Q(x)
    return {
        "nonzero": bool(x),
        "numerator_bits": abs(x.numerator).bit_length(),
        "denominator_bits": x.denominator.bit_length(),
        "exact_rational_sha256": hashlib.sha256(str(x).encode()).hexdigest()
    }

def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("Mathematical execution is authorized only in the named public Actions repository")
    producer = HERE / "check-r943-degree178-full-cm-source.py"
    producer_sha = hashlib.sha256(producer.read_bytes()).hexdigest()
    assert producer_sha == PRODUCER_SHA
    # Preserve the unchanged original producer, including all complete fibers
    # and its JSON certification.  Capture its actual matrices in memory so
    # the six-sigma reader consumes this same rebuild, not saved tables.
    helper_path = HERE / "check-original-e89-six-sigma-projection.py"
    spec = importlib.util.spec_from_file_location("r958_six_sigma", helper_path)
    helper = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = helper
    spec.loader.exec_module(helper)
    report, six_sigma = helper.rebuild_and_check(producer)
    assert report["status"] == "PASS"
    assert report["canonical_matrix_sha256"] == MATRIX_SHA
    assert report["joint_mass_kernel_dimension"] == 1
    line = report["joint_mass_kernel"][0]
    assert line["origin_order"] == 6
    cs = line["polynomial_X_ascending"]
    assert len(cs) == 30 and cs[29] == ["0", "0"] and cs[28] == ["1", "0"]
    assert all(x[1] == "0" for x in cs)
    coeffs = [Q(x[0]) for x in cs[:29]]
    assert all(91 % x.denominator == 0 for x in coeffs)
    fw = [Q(0)] * 30
    for j, c in enumerate(coeffs):
        fw[29-j] += (-1)**(29-j)*c
    fw = trim(fw)
    assert len(fw) == 30 and fw[1] == -1
    t, tm1, h7, d = [0, 1], [-1, 1], [7, 4, 16], [1, 8]
    a = product([t, tm1, h7])
    h = product([
        [-1, 20, 8],
        [13, -52, 1536, -1024, 256],
        [1, -40, 2112, -3136, 1792],
        [-1, 1232, 58688, -49408, 439040, -2111488, 1949696, -851968, 32768]])
    assert len(h) == 19 and h[0] == 13
    f = product([a, d], 7)
    fu = product([a, h], 91)
    assert len(f) == 6 and len(fu) == 23
    g = exact_div(fw, a)
    sw_quotient = exact_div(fw, f)
    assert len(g) == 26 and len(sw_quotient) == 25
    orders = {name: multiplicity(fw, p) for name, p in (
        ("t", t), ("t_minus_1", tm1), ("h7_both_roots", h7), ("d", d))}
    common, u, v = gcd_bezout(h, g)
    old_common, _, _ = gcd_bezout(product([a, d]), h)
    assert len(old_common) == 1
    rs = resultant(h, g)
    assert bool(rs) == (len(common) == 1)
    simple_a = all(orders[key] == 1 for key in ("t", "t_minus_1", "h7_both_roots"))
    pencil = simple_a and len(common) == 1
    assert evaluate(a, Q(-1, 4)) == Q(35, 16)
    witness = {
        "H": [str(x) for x in h],
        "G": [str(x) for x in g],
        "gcd": [str(x) for x in common],
        "bezout_H": [str(x) for x in u],
        "bezout_G": [str(x) for x in v]}
    out = {
        "status": "PASS",
        "source_commit": os.environ["GITHUB_SHA"],
        "run_id": int(os.environ["GITHUB_RUN_ID"]),
        "source_charge": 89,
        "source_cm_matrix_sha256": MATRIX_SHA,
        "source_producer_sha256": producer_sha,
        "source_cm_dependency_sha256": report["dependency_sha256"],
        "source_coefficients_regenerated_in_same_job": True,
        "polynomial_X_ascending_sha256": hashlib.sha256(
            json.dumps([str(x) for x in coeffs], separators=(",", ":")).encode()).hexdigest(),
        "angular_fW_sha256": digest([str(x) for x in fw]),
        "angular_degrees": {"fW": len(fw)-1, "fW_over_a": len(g)-1,
                            "fW_over_fS": len(sw_quotient)-1},
        "multiplicities": orders,
        "gcd_H18_fW_over_a_degree": len(common)-1,
        "whole_bezout_identity_checked": True,
        "whole_bezout_witness_sha256": digest(witness),
        "resultant_H18_fW_over_a": rational_summary(rs),
        "resultant_a_fW_over_a": rational_summary(resultant(a, g)),
        "leading_coefficient_fW": rational_summary(fw[-1]),
        "new_four_point_bounds_all_1_over_89": simple_a,
        "U89_W68_basepointfree_pencil_eligible": pencil,
        "pencil_and_primitive_degree_checks": None,
        "output_files": False,
        "scope": "Exact fixed angular multiplicities and full polynomial gcds for the original regenerated E89 source; not a central nonvanishing or infinite-prime claim."
    }
    # The original U,W pencil may have a genuine common finite factor.
    # Shear within exactly the same source ring: U_c = U + c*S^4.
    # H_c = H/91 + c*a^3*d^4/7^4, so its values at a*d=0 and its
    # degree-18 leading term agree with H/91.  At each root of G
    # at most one c is forbidden, and deg(G)=25.
    out["sheared_parameter"] = None
    out["sheared_pencil_and_primitive_degree_checks"] = None
    if simple_a:
        a3d4 = product([a, a, a, d, d, d, d])
        trials = []
        chosen = None
        for c in range(26):
            hc = add(scale(h, Q(1, 91)), scale(a3d4, Q(c, 7**4)))
            assert len(hc) == 19 and hc[-1] == h[-1]/91
            hc_ad, _, _ = gcd_bezout(hc, product([a, d]))
            assert len(hc_ad) == 1
            gc, uc, vc = gcd_bezout(hc, g)
            trials.append({"c": c, "gcd_degree": len(gc)-1})
            if len(gc) == 1:
                chosen = c
                break
        assert chosen is not None
        assert len(mul(a, hc)) == 23
        resc = resultant(hc, g)
        assert resc
        sheared_witness = {
            "Hc": [str(x) for x in hc],
            "G": [str(x) for x in g],
            "bezout_Hc": [str(x) for x in uc],
            "bezout_G": [str(x) for x in vc]}
        out["sheared_parameter"] = {
            "c": chosen,
            "formula": "U_c = U + c*S^4; H_c = H/91 + c*a^3*d^4/7^4",
            "trials": trials,
            "gcd_Hc_G_degree": 0,
            "gcd_Hc_a_times_d_degree": 0,
            "Hc_degree": len(hc)-1,
            "f_Uc_degree": len(mul(a, hc))-1,
            "whole_bezout_identity_checked": True,
            "whole_bezout_witness_sha256": digest(sheared_witness),
            "resultant_Hc_G": rational_summary(resc),
            "same_source_ring": "R[S,U_c,W] = R[S,U,W]",
            "central_zero_inherited": False}
        L = 68*89
        degree_A = max(22*89, 29*68)-4*68
        degree_C = max(5+22*22, 29*17)-4*17-1
        assert degree_A == 1700 and degree_C == 424
        assert math.gcd(degree_A, degree_C) == 4
        assert 89*13-68*17 == 1 and 17+68*22-89*17 == 0
        generators = []
        for r in range(L):
            q = 29*r//89 - 4*((r+88)//89)
            last_n = 2 if q <= -2 else 1
            generators.append(L*last_n+r)
        assert max(generators) == 12113
        conductor_weight = 17*(degree_A-1)
        assert conductor_weight == 28883
        out["sheared_pencil_and_primitive_degree_checks"] = {
            "common_pencil_weight": L,
            "projective_pencil_degree": degree_A,
            "rational_map_A_degree": degree_A,
            "rational_map_C_degree": degree_C,
            "common_map_degree_divides": math.gcd(degree_A, degree_C),
            "quadratic_involution_test_a_at_minus_one_quarter": "35/16",
            "normalization_finite_module_generator_max_weight": max(generators),
            "candidate_different_weight": conductor_weight,
            "parameter_shear_c": chosen,
            "candidate_different_origin_angular_order_range": [
                (conductor_weight+88)//89, 29*conductor_weight//89]}
    out["six_sigma_projection"] = six_sigma
    out["reader_sha256"] = hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    out["elapsed_seconds"] = time.time()-START
    print(json.dumps(out, separators=(",", ":")))

if __name__ == "__main__":
    main()
