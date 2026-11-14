#!/usr/bin/env python3
"""Exact Weil-pairing and normalization certificate for R78.

Uses only Python's standard library and the existing R70 arithmetic module.
The pairing convention is Miller (2004), Proposition 8:
    e_n(P,Q) = (-1)^n f_(n,P)(Q) / f_(n,Q)(P).
This is the inverse of Sutherland's 2025 Lecture 23 convention.

R70's two base projections are recomputed, while R73's complete certificate
is read and its 860 weights/sums are checked.  To recompute R73's isogenies
as well, use its separate C++ verifier.  No p-adic correction is evaluated.
"""

import hashlib
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True

from verify_r70_elliptic_unit_residues import Fq2, Curve, certificate


def line_quotient(curve, left, right, at):
    """Evaluate a chord/tangent divided by the vertical through its sum."""
    f = curve.f
    if left is None or right is None:
        return f.one
    x, y = left
    xx, yy = right
    z, w = at
    if x == xx and f.add(y, yy) == f.zero:
        value = f.sub(z, x)
        assert value != f.zero
        return value
    if left == right:
        slope = f.div(f.sub(f.scale(3, f.mul(x, x)), f.one),
                      f.scale(2, y))
    else:
        slope = f.div(f.sub(yy, y), f.sub(xx, x))
    summed = curve.add(left, right)
    assert summed is not None
    numerator = f.sub(f.sub(w, y), f.mul(slope, f.sub(z, x)))
    denominator = f.sub(z, summed[0])
    assert numerator != f.zero and denominator != f.zero
    return f.div(numerator, denominator)


def miller(curve, n, point, at):
    """Double-and-add evaluation of f_(n,point) with its full denominator."""
    assert n > 0 and point is not None and at is not None
    f = curve.f
    value, current = f.one, point
    for digit in bin(n)[3:]:
        value = f.mul(f.mul(value, value),
                      line_quotient(curve, current, current, at))
        current = curve.add(current, current)
        if digit == "1":
            value = f.mul(value, line_quotient(curve, current, point, at))
            current = curve.add(current, point)
    assert current == curve.mul(n, point)
    return value


def weil_direct(curve, p, point, other):
    assert curve.mul(p, point) is None
    assert curve.mul(p, other) is None
    f = curve.f
    value = f.div(miller(curve, p, point, other),
                  miller(curve, p, other, point))
    return f.neg(value) if p % 2 else value


def weil_shifted(curve, p, point, other):
    """Miller (2004), formula (10), with T=(0,0)=-T."""
    f = curve.f
    shift = (f.zero, f.zero)
    assert curve.on_curve(shift) and curve.mul(2, shift) is None
    a = f.div(miller(curve, p, point, curve.add(other, shift)),
              miller(curve, p, point, shift))
    b = f.div(miller(curve, p, other, curve.add(point, shift)),
              miller(curve, p, other, shift))
    return f.div(a, b)


def discrete_log(field, root, value, p):
    assert field.power(root, p) == field.one and root != field.one
    table, power = {}, field.one
    for j in range(p):
        assert power not in table
        table[power] = j
        power = field.mul(power, root)
    assert power == field.one and value in table
    return table[value]


def pairing_record(base):
    p, s = base["p"], base["q"]
    f, curve = Fq2(s), Curve(Fq2(s))
    point = tuple(tuple(x) for x in base["p_point"])
    other = curve.cm_i(point)
    root = tuple(base["zeta"])
    assert point[0][1] == point[1][1] == 0
    assert curve.on_curve(point) and curve.on_curve(other)
    assert curve.mul(p, point) is None and point is not None
    assert curve.mul(p, other) is None and other is not None
    assert root == f.power((2, 1), (s*s-1)//p)
    fpq = miller(curve, p, point, other)
    fqp = miller(curve, p, other, point)
    direct = weil_direct(curve, p, point, other)
    shifted = weil_shifted(curve, p, point, other)
    assert direct == shifted
    assert direct != f.one and f.power(direct, p) == f.one
    assert weil_direct(curve, p, other, point) == f.inv(direct)
    assert weil_direct(curve, p, curve.mul(2, point), other) == f.power(direct, 2)
    assert weil_direct(curve, p, point, curve.mul(3, other)) == f.power(direct, 3)
    assert f.power(direct, s) == f.inv(direct)
    return {"s": s, "p_point": point, "i_p_point": other,
            "zeta_s": root, "f_P_at_iP": fpq, "f_iP_at_P": fqp,
            "weil_direct": direct, "weil_shifted": shifted,
            "k_s": discrete_log(f, root, direct, p),
            "base_projection": base["u1_projection"],
            "base_log_table_sha256": base["log_table_sha256"]}


def main():
    here = Path(__file__).resolve().parent
    r70_path = here / "r70_elliptic_unit_residue_certificates.json"
    r73_path = here / "r73_derivative_residue_certificate.json"
    r70 = json.loads(r70_path.read_text())
    r73 = json.loads(r73_path.read_text())
    saved = {row["q"]: row for row in r70["certificates"]}
    p, q, r = r73["p"], r73["q"], r73["r"]
    assert (p, q, r) == (43, 49019, 859) and r73["complete"]

    pairings = []
    for s in (r, q):
        rebuilt = certificate(s, p)
        assert json.loads(json.dumps(rebuilt)) == saved[s]
        pairings.append(pairing_record(saved[s]))
    by_s = {row["s"]: row for row in pairings}
    assert by_s[r]["k_s"] == 40 and by_s[q]["k_s"] == 29

    fr = Fq2(r)
    zeta_r = tuple(r73["zeta_r"])
    assert list(zeta_r) == saved[r]["zeta"]
    assert r73["zeta_q"] == saved[q]["zeta"]
    counts, weighted, unweighted = [0]*p, [0, 0], [0, 0]
    lines = r73["lines"]
    assert len(lines) == r+1
    for index, row in enumerate(lines):
        slope, j, x, y = row
        assert slope == index and all(0 <= t < p for t in (j, x, y))
        generator = (1, slope) if slope < r else fr.i
        residue = fr.power(generator, (r*r-1)//p)
        assert discrete_log(fr, zeta_r, residue, p) == j
        counts[j] += 1
        for k, value in enumerate((x, y)):
            weighted[k] = (weighted[k]+j*value) % p
            unweighted[k] = (unweighted[k]+value) % p
    assert counts == [20]*p
    assert weighted == r73["Z"] == [31, 12]
    assert unweighted == r73["unweighted_sum"] == [0, 0]
    euler7 = 8*pow(7, -1, p) % p
    raw = [euler7*x % p for x in weighted]
    assert raw == r73["R65_raw_derivative_coordinate"] == [17, 26]
    assert saved[q]["u1_projection"] == [0, 0]

    # With D=sum(j*sigma^j) and sigma(Pi)/Pi=zeta_s, Hilbert 90 gives
    # valuation = -log_(zeta_s).  See Rubin 1991, Proposition 2.3, and R78.
    singular_r = -saved[r]["u1_projection"][1] % p
    singular_q = -raw[1] % p
    # In V coordinates, an unramified log is divided by k_q; restriction
    # Q_q -> K_q then multiplies the real Frobenius coordinate by 2.
    q_unramified_K = raw[0]*pow(by_s[q]["k_s"], -1, p) % p
    q_unramified_Q = q_unramified_K*pow(2, -1, p) % p
    m_qr = q_unramified_Q*pow(singular_r, -1, p) % p
    m_rq = -m_qr % p  # Proven by global reciprocity, not a second raw run.
    matrix = [[0, m_rq], [m_qr, 0]]
    determinant = -m_qr*m_rq % p
    assert (singular_r, singular_q, q_unramified_K, q_unramified_Q) == (28, 17, 8, 4)
    assert matrix == [[0, 6], [37, 0]] and determinant == 36

    result = {
        "p": p, "r": r, "q": q,
        "pairing_convention": "Miller 2004 Proposition 8: (-1)^p f_P(Q)/f_Q(P)",
        "pairings": pairings,
        "r73_certificate_sha256": hashlib.sha256(r73_path.read_bytes()).hexdigest(),
        "r73_line_count": len(lines), "r73_weight_counts": counts,
        "r73_weighted_sum": weighted, "r73_unweighted_sum": unweighted,
        "euler_7_factor": euler7, "raw_kappa_r_at_q": raw,
        "q_unramified_K_real_coordinate": q_unramified_K,
        "q_unramified_Q_coordinate": q_unramified_Q,
        "lambda_r": singular_r, "lambda_r_inverse": pow(singular_r, -1, p),
        "lambda_q_second_order": singular_q,
        "lambda_q_inverse": pow(singular_q, -1, p),
        "matrix_order": [r, q], "matrix": matrix, "determinant": determinant,
        "reverse_entry_source": "global reciprocity; not a separately evaluated derivative",
        "p_local_corrections_computed": False,
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
