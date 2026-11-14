#!/usr/bin/env python3
"""R476: exact full D33-minus Xi bridge and its integral eight-source basis.

All calculations are in Q(delta), delta^2=-3, and in the complete 23-dimensional
principal degree136 theta space.  The full CM19 input is reconstructed by
check-original-degree136-cm19-exact.py using its 23 exact canonical fibers.
This script does not sample the varying ordinary prime.
"""
from pathlib import Path
from math import lcm
import json
import runpy

BASE = Path(__file__).resolve().parents[1]
H = runpy.run_path(str(BASE / "scripts/check-r466-fixed-two-division-source.py"))
Q, Mat = H["Q"], H["Mat"]
fq, fa, fn, fs, fm, fi, fp = (H[k] for k in ("fq", "fa", "fn", "fs", "fm", "fi", "fp"))
km, ka, ks, kp, kzero, kvec = (H[k] for k in ("km", "ka", "ks", "kp", "kzero", "kvec"))
identity, rank, cols, kinv = (H[k] for k in ("identity", "rank", "cols", "kinv"))
entry, serial = H["get_entry"], H["serialize_matrix"]
ZERO, ONE = fq(0), fq(1)
OMEGA = fq(Q(-1, 2), Q(1, 2))


def decode(data):
    return tuple(Mat([[Q(x) for x in row] for row in data[k]]) for k in ("real", "delta"))


def read(relative):
    return json.loads((BASE / relative).read_text())


def subrows(matrix, rows):
    return tuple(Mat([[matrix[k][i, j] for j in range(matrix[k].ncols())]
                      for i in rows]) for k in (0, 1))


def main():
    I = identity(23)
    cm7 = read("notes/2026-11-14-theta-degree136-cm7-exact.json")
    cm19 = read("notes/2026-11-14-theta-degree136-cm19-exact.json")
    M = decode(cm7["matrix"])
    N = decode(cm19["matrix"])
    D = ks(km(N, kp(M, 16, I)), fp(OMEGA, -1))
    assert D == decode(cm19["D33"])
    assert kp(M, 18, I) == I
    assert km(M, N) == km(N, M)
    assert km(D, D) == I
    assert km(D, M) == km(M, D)
    minus = ks(ka(I, ks(D, fq(-1))), fq(Q(1, 2)))
    positive9 = ks(ka(I, kp(M, 9, I)), fq(Q(1, 2)))
    one = H["eig_project"](M, ONE, I)
    reference_projector = km(minus, one)
    seven = km(minus, ka(I, ks(one, fq(-1))))
    assert rank(minus) == 8
    assert km(minus, positive9) == minus
    assert rank(reference_projector) == 1
    assert rank(seven) == 7
    assert km(seven, seven) == seven

    xi = decode(read("scripts/check-r465-common-six-sigma-true-core-marginal.json")["Xi_double"])
    r470 = read("scripts/check-r470-original-negative-source-new-line.json")
    a = decode(r470["A"])
    new = decode(r470["Snew"])
    href = ks(km(reference_projector, a), fq(-120960))
    assert entry(href, 22) == ONE
    assert href[1] == Mat(23, 1)
    assert km(M, href) == href
    assert km(N, href) == ks(href, fn(OMEGA))
    assert km(D, href) == ks(href, fq(-1))
    # Match the already identified k=4 arithmetic line, not k=1/E_{-136}.
    k4 = read("scripts/check-r466-fixed-two-division-source.json")["joint_positive_mu6_sources"][3]
    assert k4["k"] == 4 and k4["curve_D"] == 668168
    k4v = kvec([Q(x) for x in k4["sources"][0]["polynomial_b1"]])
    assert ks(k4v, fi(entry(k4v, 22))) == href

    w13, w15 = [kvec([poly[j] for j in range(23)]) for poly in H["source_polys"]()]
    w = ka(ks(w13, fq(101)), ks(w15, fq(-64)))
    assert km(minus, w) == w
    assert km(one, w) == kzero(23, 1)
    orbit, current = [], w
    for _ in range(7):
        orbit.append(current)
        current = km(M, current)
    B7 = cols(orbit)
    assert rank(B7) == 7
    # The complete minimal polynomial is (t-omega^2)(t^6+t^3+1).
    v = ka(ka(km(kp(M, 6, I), w), km(kp(M, 3, I), w)), w)
    assert km(M, v) == ks(v, fp(OMEGA, 2))
    assert v != kzero(23, 1)
    p = [fq(-4), fq(3, -1), fq(0, -4), fq(-4, 2),
         fq(3, 1), fq(-6, -2), fq(-7, 1)]
    p = [fm(fq(Q(5, 1332)), c) for c in p]
    coeff = tuple(Mat([[c[k]] for c in p]) for k in (0, 1))
    image = km(B7, coeff)
    assert image == km(seven, xi)
    cref = fq(Q(-1, 2016), Q(-1, 2016))
    assert km(reference_projector, xi) == ks(href, cref)
    assert km(minus, xi) == ka(image, ks(href, cref))
    assert entry(image, 22) == fn(cref)
    assert entry(km(minus, xi), 22) == ZERO
    p_omega2 = ZERO
    for j, c in enumerate(p):
        p_omega2 = fa(p_omega2, fm(c, fp(OMEGA, 2*j)))
    assert p_omega2 == fq(Q(-5, 222))
    new_projector = km(minus, H["eig_project"](M, fp(OMEGA, 2), I))
    assert rank(new_projector) == 1
    assert km(new_projector, w) == ks(new, fq(Q(-3848, 5)))
    assert km(new_projector, xi) == ks(new, fq(Q(52, 3)))

    # Integral coefficient extraction on the whole eight-dimensional block.
    B8 = cols([href] + orbit)
    assert rank(B8) == 8
    rows = list(range(22, 14, -1))
    R = subrows(B8, rows)
    Ri = kinv(R)
    selector = (Mat([[Q(i == j) for j in range(23)] for i in rows]), Mat(8, 23))
    dual = km(Ri, selector)
    assert km(dual, B8) == identity(8)
    assert km(km(B8, dual), minus) == minus
    denominator = 1
    for part in Ri:
        for i in range(8):
            for j in range(8):
                denominator = lcm(denominator, int(part[i, j].denom()))
    expected_factors = {2: 22, 3: 11, 5: 2, 7: 1, 13: 1, 19: 1,
                        23: 1, 29: 2, 37: 3, 41: 1, 53: 1, 61: 1}
    expected_denominator = 1
    for prime, exponent in expected_factors.items():
        expected_denominator *= prime**exponent
    assert denominator == expected_denominator
    coords = km(dual, km(minus, xi))
    assert entry(coords, 0) == cref
    assert all(entry(coords, j+1) == p[j] for j in range(7))

    report = {
        "field": "Q(delta), delta^2=-3; omega=(-1+delta)/2",
        "basis": "sigma^136*x^2*X^j, j=0,...,22; b=1",
        "normalization": "N7=M_gamma7/gamma7; N19=M_gamma19/gamma19; same canonical traces as R466",
        "D33": serial(D),
        "D33_minus_dimension": 8,
        "D33_minus_is_inside_N7_ninth_plus": True,
        "eigen_one_D33_minus_dimension": 1,
        "seven_projector": serial(seven),
        "seven_projector_rank": 7,
        "reference_curve_D": 668168,
        "reference_mass_one": serial(href),
        "reference_eigen_N7": ["1", "0"],
        "reference_eigen_N19": ["1/2", "-1/2"],
        "reference_coefficient_in_Xi_b1": [str(x) for x in cref],
        "Wstar": serial(w),
        "Wstar_orbit_rank": 7,
        "Wstar_minimal_polynomial": "(t-omega^2)*(t^6+t^3+1)",
        "bridge_polynomial_coefficients": [[str(x) for x in c] for c in p],
        "bridge_polynomial_at_omega_squared": "-5/222",
        "projected_Xi": serial(image),
        "full_D33_minus_Xi": serial(km(minus, xi)),
        "mass_orbit": [[str(x) for x in entry(v, 22)] for v in orbit],
        "eight_source_basis": serial(B8),
        "coefficient_rows": rows,
        "coefficient_inverse_minor": serial(Ri),
        "coefficient_dual": serial(dual),
        "coefficient_inverse_denominator": str(denominator),
        "coefficient_inverse_denominator_factors": expected_factors,
        "new_projection_coefficient": "52/3",
        "companion_lift_Wstar_scalar": "-111/280",
        "companion_lift_mass": "5824/3",
        "companion_lift_product": "-3848/5",
        "full_tensor_warning": "The eight companion sources are distinct; only their masses are the displayed marginal coefficients.",
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2) + "\n")
    print("R476 full 23-coordinate Xi identity, rank7/8 basis, E668168 reference, and integral dual proved.")
    print("inverse minor denominator", denominator, expected_factors)


if __name__ == "__main__":
    main()
