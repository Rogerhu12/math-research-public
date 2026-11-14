#!/usr/bin/env python3
"""R189: a primitive primal Robert class at the same certified R171 prime.

Python standard library only. R171 supplies its already published ECPP/Pratt
certificate, the global marking, and elementary F_(q^2)/elliptic arithmetic.
Every one of the 1848 new beta-division values is recomputed here. No class
number, floating point, or field-factorization oracle is used.
"""
import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "r171_arithmetic", HERE / "verify_r171_principal_norm_selflocal.py")
r171 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r171)
TARGET = HERE / "r189_primal_robert_generator_certificate.json"
BASE = HERE / "r171_principal_norm_selflocal_certificate.json"


def compute(data):
    base_bytes = BASE.read_bytes()
    base = json.loads(base_bytes)
    p, q = data["p"], base["q"]
    assert p == 43 and q == data["q"]
    assert hashlib.sha256(base_bytes).hexdigest() == data["r171_certificate_sha256"]
    assert r171.verify_ecpp(base["ecpp"], base["pratt_base"]) == q
    assert q % (4*p) == 4*p-1
    field, fp = r171.CertifiedField(q), r171.r161.Fq2(p)
    curve = r171.r161.Curve(field)
    point = tuple(tuple(x) for x in base["expected"]["P"])
    zeta = tuple(base["expected"]["zeta_Weil"])
    assert point is not None and curve.on_curve(point)
    assert point[0][1] == point[1][1] == 0
    assert curve.mul(p, point) is None
    assert r171.pairing(field, curve, point, curve.cm_i(point)) == zeta
    logs, z = {}, field.one
    for j in range(p):
        logs[z] = j
        z = field.mul(z, zeta)
    assert len(logs) == p and z == field.one

    beta, beta_bar = (q-1, 2), (q-1, q-2)
    beta_p, beta_bar_p = (p-1, 2), (p-1, p-2)
    assert fp.mul(beta_p, beta_bar_p) == (5, 0)
    e_beta = fp.sub((5, 0), fp.power(beta_p, 2*p))
    e_beta_bar = fp.sub((5, 0), fp.power(beta_bar_p, 2*p))
    assert e_beta == (8, 39) and e_beta_bar == (8, 4)
    assert fp.mul(e_beta, e_beta_bar) == (80 % p, 0)
    assert fp.sub((121 % p, 0), fp.power((-11 % p, 0), 2*p)) == fp.zero

    point_i = curve.cm_i(point)
    point_2 = (field.i, (1, q-1))
    assert curve.on_curve(point_2)
    assert curve.mul(2, point_2) == (field.zero, field.zero)
    aa, bb = [None], [None]
    for j in range(1, p):
        aa.append(curve.add(aa[-1], point))
        bb.append(curve.add(bb[-1], point_i))
    aa = [curve.add(point_2, t) for t in aa]
    exponent = (q*q-1)//p
    table, values, conjugate_values = {}, {}, {}
    weights = {}
    total, weight_total = fp.zero, fp.zero
    records = bytearray()
    for a in range(p):
        for b in range(p):
            if (a, b) == (0, 0):
                continue
            here = curve.add(aa[a], bb[b])
            assert here is not None and curve.on_curve(here)
            xx = field.mul(here[0], here[0])
            value = field.add(field.mul(beta, xx), field.one)
            conjugate_value = field.add(field.mul(beta_bar, xx), field.one)
            assert value != field.zero and conjugate_value != field.zero
            ell = logs[field.power(value, exponent)]
            table[(a, b)] = ell
            values[(a, b)] = value
            conjugate_values[(a, b)] = conjugate_value
            records.extend((a, b, ell))
            weight = fp.power((a, b), -2*p)
            abar = (a, -b % p)
            assert weight == fp.div(fp.one, fp.mul(abar, abar))
            weights[(a, b)] = weight
            total = fp.add(total, fp.scale(ell, weight))
            weight_total = fp.add(weight_total, weight)
    assert len(table) == 1848 and weight_total == fp.zero

    # This is an exact pointwise identity before taking p-th power symbols.
    # It proves that the conjugate auxiliary's log is -ell_{-i*bar(a)}.
    total_bar = fp.zero
    for a, b in table:
        rotated = (-b % p, -a % p)
        v = values[rotated]
        assert conjugate_values[(a, b)] == (v[0], -v[1] % q)
        ell_bar = -table[rotated] % p
        total_bar = fp.add(total_bar, fp.scale(ell_bar, weights[(a, b)]))
    normalized = fp.div(total, e_beta)
    normalized_bar = fp.div(total_bar, e_beta_bar)
    assert normalized == normalized_bar and normalized[1] == 0

    # v_beta is the inverse of psi_beta, the constant 4 disappears because
    # weight_total=0, 1/(p^2-1)=-1, and restriction to Q_(q^2) multiplies a
    # Q_q unramified class by 2. These give +S_beta/(2e_beta).
    finite = fp.scale(pow(2, -1, p), normalized)
    assert finite == (10, 0)
    u = finite[0]
    # R185 fixed AH coordinates, used with the R168 trace-pairing convention.
    d_robert, d_q = (24, 20), (20, 29)
    determinant = (d_robert[0]*d_q[1]-d_robert[1]*d_q[0]) % p
    assert determinant == 38
    rhs = (-2*u) % p
    pairing_1 = (-d_robert[1]*rhs*pow(determinant, -1, p)) % p
    pairing_45 = (d_robert[0]*rhs*pow(determinant, -1, p)) % p
    assert (pairing_1, pairing_45) == (6, 10)
    assert (24*pairing_1+20*pairing_45) % p == 0
    assert (20*pairing_1+29*pairing_45) % p == rhs
    assert pairing_45 != 0

    return {
        "points": len(table), "beta": list(beta_p),
        "euler_beta": list(e_beta), "euler_conjugate": list(e_beta_bar),
        "sum_weights": list(weight_total),
        "weighted_psi_sum": list(total),
        "weighted_conjugate_psi_sum": list(total_bar),
        "normalized_sum": list(normalized),
        "primal_finite_q": u,
        "p_pairings_with_AH_basis": [pairing_1, pairing_45],
        "log_table_sha256": hashlib.sha256(records).hexdigest(),
        "scope": "actual primal global unit and local pairings; not Omega_2"
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-expected", action="store_true")
    args = parser.parse_args()
    data = json.loads(TARGET.read_text())
    result = compute(data)
    if args.write_expected:
        data["expected"] = result
        TARGET.write_text(json.dumps(data, indent=2, sort_keys=True)+"\n")
    if args.check:
        assert data["expected"] == result
    print("PASS: 1848 beta-Robert values; S=(31,6); primal q value=10; p AH pairings=(6,10)")
    print("certificate_sha256="+hashlib.sha256(TARGET.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
