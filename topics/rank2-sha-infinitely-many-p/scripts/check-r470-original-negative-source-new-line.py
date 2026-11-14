#!/usr/bin/env python3
"""R470: the original R414 negative source and the explicit new CM line.

All equalities are exact, over Q(delta), delta^2=-3.  This consumes the
complete 23-column CM7 matrix and the complete five-dimensional CM19
block, already reconstructed from their actual finite isogeny fibers.
It does not use target-prime sampling or infer arithmetic rank from mass.
"""
from pathlib import Path
import json
import runpy

BASE = Path(__file__).resolve().parents[1]
H = runpy.run_path(str(BASE / "scripts/check-r466-fixed-two-division-source.py"))
Q, Mat, Poly = (H[k] for k in ("Q", "Mat", "Poly"))
fq, fm, fp = (H[k] for k in ("fq", "fm", "fp"))
km, ka, ks, kp, kvec, kzero = (H[k] for k in ("km", "ka", "ks", "kp", "kvec", "kzero"))
cols, rank, identity, kinv = (H[k] for k in ("cols", "rank", "identity", "kinv"))
get_entry, serialize_matrix, eig_project = (
    H[k] for k in ("get_entry", "serialize_matrix", "eig_project"))


def decode(data):
    return tuple(Mat([[Q(x) for x in row] for row in data[part]])
                 for part in ("real", "delta"))


def sub(a, b):
    return ka(a, ks(b, fq(-1)))


def evaluate_five(a):
    """The same five full polynomial evaluations as the CM19 certificate."""
    return tuple(Mat([[sum(a[k][j, i] * Q(t)**(3*j)
                           for j in range(a[k].nrows()))
                       for i in range(a[k].ncols())] for t in range(1, 6)])
                 for k in (0, 1))


def field_json(a):
    return [str(x) for x in a]


def main():
    cm7 = json.loads((BASE / "notes/2026-11-14-theta-degree136-cm7-exact.json").read_text())
    cm19 = json.loads((BASE / "scripts/check-r466-fixed-two-division-source.json").read_text())
    m = decode(cm7["matrix"])
    b = decode(cm19["positive_mu6_basis"])
    m7b = decode(cm19["positive_mu6_N7"])
    m19b = decode(cm19["positive_mu6_N19"])
    i, ib = identity(23), identity(5)
    omega = fq(Q(-1, 2), Q(1, 2))
    omega2 = fp(omega, 2)
    assert kp(m, 18, i) == i
    assert km(m, b) == km(b, m7b)
    assert kp(m7b, 3, ib) == ib
    assert km(m7b, m19b) == km(m19b, m7b)
    # On N7^3=1, N7^-2=N7.  This keeps the absolute CM19 normalization.
    d33 = ks(km(m19b, m7b), omega2)
    assert km(d33, d33) == ib
    assert km(d33, m7b) == km(m7b, d33)
    bi = kinv(evaluate_five(b))

    x = Poly([0, 1])
    r = x**2 + 20*x - 8
    p4 = x*(x-8)**3 - 512*(x+1)**3
    p8 = 7*x**2*(x-8)**6 - 256*x*(x-8)**3*(x+1)**3 + 65536*(x+1)**6
    ell = 10*x**3 - 24*x**2 + 192*x + 64
    pa = (x+1)**2*(x-8)**2*r*p4*p8*ell / 70
    av = kvec([pa[j] for j in range(23)])
    assert pa.degree() == 21 and pa[21] == 1 and pa[22] == 0
    assert km(kp(m, 9, i), av) == av

    ws = [kvec([w[j] for j in range(23)]) for w in H["source_polys"]()]
    positive = ks(ka(ka(i, kp(m, 3, i)), kp(m, 6, i)), fq(Q(1, 3)))
    new = ks(km(positive, sub(ks(ws[0], fq(101)), ks(ws[1], fq(64)))), fq(Q(-5, 3848)))
    f4a = x**4 + 40*x**3 + 2112*x**2 + 3136*x + 1792
    f4b = 13*x**4 + 52*x**3 + 1536*x**2 + 1024*x + 256
    f8 = (x**8 + 1232*x**7 - 58688*x**6 - 49408*x**5 - 439040*x**4
          - 2111488*x**3 - 1949696*x**2 - 851968*x - 32768)
    pn = (x+1)*r*(7*x**2-4*x+16)*f4a*f4b*f8 / 91
    assert new == kvec([pn[j] for j in range(23)])
    assert pn.degree() == 21 and pn[21] == 1
    assert km(m, new) == ks(new, omega2)
    newb = km(bi, evaluate_five(new))
    assert km(b, newb) == new
    assert km(m19b, newb) == ks(newb, fq(Q(1, 2), Q(1, 2)))  # -omega^2
    assert km(d33, newb) == ks(newb, fq(-1))

    positive_parts = []
    projected = None
    for lam in (fq(1), omega, omega2):
        v = eig_project(m, lam, av)
        vb = km(bi, evaluate_five(v))
        assert km(b, vb) == v
        dv = km(b, km(d33, vb))
        for sign in (1, -1):
            part = ks(ka(v, ks(dv, fq(sign))), fq(Q(1, 2)))
            positive_parts.append({
                "N7_eigenvalue": field_json(lam), "D33_eigenvalue": sign,
                "mass": field_json(get_entry(part, 22)),
                "degree21_coefficient": field_json(get_entry(part, 21)),
                "Taylor_z6": field_json(H["fs"](get_entry(part, 21),
                                          fm(fq(Q(136, 15)), get_entry(part, 22)))),
                "vector": serialize_matrix(part)})
            if lam == omega2 and sign == -1:
                projected = part
    assert projected == ks(new, fq(Q(13, 90)))
    assert get_entry(projected, 22) == fq(0)
    # Full-source verification of the explicit polynomial projector.
    e = kzero(23, 1)
    cur = av
    for j in range(18):
        e = ka(e, ks(cur, fp(omega, j)))
        cur = km(m, cur)
    eb = km(bi, evaluate_five(e))
    assert km(b, eb) == e
    qav = ks(sub(e, ks(km(b, km(m19b, eb)), omega)), fq(Q(1, 36)))
    assert qav == projected

    orbits = []
    for w in ws:
        assert km(kp(m, 9, i), w) == w
        for _ in range(9):
            orbits.append(w)
            w = km(m, w)
    aorbit = []
    cur = av
    for _ in range(9):
        aorbit.append(cur)
        cur = km(m, cur)
    assert rank(cols(orbits)) == 16
    assert rank(cols(orbits + [av])) == 17
    assert rank(cols(aorbit)) == 9
    assert rank(sub(kp(m, 9, i), i)) == 6
    out = {
        "field": "Q(delta), delta^2=-3", "curve_b": 1,
        "basis": "sigma^136*x^2*X^j, j=0,...,22; X=x^3",
        "normalization": "N7=M_gamma7/gamma7; N19=M_gamma19/gamma19; gamma19=4+delta",
        "projector": "Q=(I-omega*N19)/36 * sum_{j=0}^17 omega^j*N7^j; equivalently nine terms /18 on N7^9=1",
        "A": serialize_matrix(av), "Snew": serialize_matrix(new),
        "projected_A": serialize_matrix(projected),
        "A_remainder": serialize_matrix(sub(av, projected)),
        "A_to_Snew": "13/90", "D33_positive_block": serialize_matrix(d33),
        "positive_mu3_parts_of_A": positive_parts,
        "ranks": {"N7_ninth_positive_whole_block": 17, "W13_W15_cyclic_sum": 16,
                  "W13_W15_plus_A": 17, "A_cyclic": 9},
        "mixed_coefficient": "9152*delta/81",
        "arithmetic_boundary": "No elliptic-curve identity or central zero is inferred from this certificate."
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
    print("Exact 23-coordinate identity: Q A136 = (13/90) Snew")
    print("Complete mixed coefficient: (7040 delta/9)*(13/90)=9152 delta/81")
    print("Whole positive block / W pair / W pair plus A ranks: 17 / 16 / 17")


if __name__ == "__main__":
    main()
