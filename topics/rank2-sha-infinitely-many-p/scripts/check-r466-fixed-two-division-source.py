#!/usr/bin/env python3
"""R466: fixed doubling division-log sources, complete CM7, and the CM19 split.

Exact arithmetic in Q(delta), delta^2=-3.  The CM7 matrix is the complete
23-column matrix reconstructed independently by the R464 fiber certificate.
CM19 is reconstructed on the whole five-dimensional positive mu_6 block:
commutation of the coprime pull/trace operators makes this a closed block.
"""
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
import json
import runpy
import time

BASE = Path(__file__).resolve().parents[1]
H = runpy.run_path(str(BASE / "scripts/check-r464-degree102-cm7-exact.py"))
Q, Mat, Poly = (H[k] for k in ("Q", "Mat", "Poly"))
fq, fa, fn, fs, fm, fi, fp = (H[k] for k in ("fq", "fa", "fn", "fs", "fm", "fi", "fp"))
pa, ps, pm, pd, ptrim = (H[k] for k in ("pa", "ps", "pm", "pd", "ptrim"))
km, ka, ks, kp, kzero, kvec = (H[k] for k in ("km", "ka", "ks", "kp", "kzero", "kvec"))
get_entry, serialize_matrix = (H[k] for k in ("get_entry", "serialize_matrix"))
ZERO, ONE = fq(0), fq(1)


def identity(n):
    return (Mat([[Q(i == j) for j in range(n)] for i in range(n)]), Mat(n, n))


def rank(A):
    R, J = A
    nr, nc = R.nrows(), R.ncols()
    block = Mat([[R[i, j] for j in range(nc)] + [-3 * J[i, j] for j in range(nc)]
                 for i in range(nr)] +
                [[J[i, j] for j in range(nc)] + [R[i, j] for j in range(nc)]
                 for i in range(nr)])
    out = block.rank()
    assert out % 2 == 0
    return out // 2


def cols(vs):
    n = vs[0][0].nrows()
    return tuple(Mat([[v[k][i, 0] for v in vs] for i in range(n)]) for k in (0, 1))


def column(A, j):
    return tuple(Mat([[A[k][i, j]] for i in range(A[k].nrows())]) for k in (0, 1))


def kinv(A):
    n = A[0].nrows()
    assert n == A[0].ncols()
    rows = [[get_entry(A, i, j) for j in range(n)] +
            [fq(i == j) for j in range(n)] for i in range(n)]
    for j in range(n):
        r = next(r for r in range(j, n) if rows[r][j] != ZERO)
        rows[j], rows[r] = rows[r], rows[j]
        scale = fi(rows[j][j])
        rows[j] = [fm(x, scale) for x in rows[j]]
        for i in range(n):
            if i == j:
                continue
            scale = rows[i][j]
            rows[i] = [fs(x, fm(scale, y)) for x, y in zip(rows[i], rows[j])]
    out = tuple(Mat([[rows[i][n + j][k] for j in range(n)]
                     for i in range(n)]) for k in (0, 1))
    assert km(A, out) == identity(n)
    return out


def source_polys():
    X = Poly([0, 1])
    ps0 = [
        [Q(0), Q(10880, 14847), Q(-13504, 14847), Q(6269, 9898),
         Q(-6523, 59388), Q(-37, 33936)],
        [Q(0), Q(923, 1470), Q(107, 5880), Q(11399, 15680),
         Q(-15919, 94080), Q(-37, 53760)],
    ]
    out = []
    for p in ps0:
        w = Poly([0])
        for j in range(1, 6):
            w += p[j] / 2**(6*j) * (X + 1)**(15 - 3*j) * X**(j - 1) * (X - 8)**(3*j - 1)
        w *= 3 * 2**35 * (X + 1) * (X**2 + 20*X - 8)
        assert w.degree() == 21
        out.append(w)
    return out


def eig_project(M, lam, v, period=18):
    out = kzero(v[0].nrows(), v[0].ncols())
    cur = v
    for j in range(period):
        out = ka(out, ks(cur, fp(lam, -j)))
        cur = km(M, cur)
    out = ks(out, fq(Q(1, period)))
    assert km(M, out) == ks(out, lam)
    return out


def q19_polynomial():
    """sigma(gamma*z)/(gamma*sigma(z)^19), gamma=4+delta.

    A finite divisor space has basis x^9,x^6,x^3,1, so the first four
    Laurent coefficients determine the entire function.  Compute them
    from x''=6*x^2 and (log sigma)''=-x.
    """
    gamma = fq(4, 1)
    x = [Q(1), Q(-1, 7), Q(1, 637), Q(-1, 84721)]
    logs = [ZERO] + [fm(fq(-x[k] / (6*k*(6*k-1))),
                        fs(fp(gamma, 6*k), fq(19))) for k in range(1, 4)]
    e = [ONE]
    for n in range(1, 4):
        val = ZERO
        for k in range(1, n + 1):
            val = fa(val, fm(fq(k), fm(logs[k], e[n-k])))
        e.append(fm(val, fq(Q(1, n))))
    B = Poly(x)
    c = [ZERO] * 4
    for k in range(4):
        val = e[k]
        for j in range(k):
            val = fs(val, fm(c[j], fq((B**(9-3*j))[k-j])))
        c[k] = val
    q = [ZERO] * 10
    for j in range(4):
        q[9-3*j] = c[j]
    assert q[-1] == ONE
    return gamma, q


def pder(A):
    return ptrim([fm(fq(j), A[j]) for j in range(1, len(A))])


def qmap(q, norm):
    q1, q2 = pder(q), pder(pder(q))
    n = ps(pm([ZERO, ONE], pm(q, q)), fq(norm))
    dlog = pa(pm(q2, q), ps(pm(q1, q1), fq(-1)))
    n = pa(n, ps(pm([ONE, ZERO, ZERO, ONE], dlog), fq(-4)))
    n = pa(n, ps(pm([ZERO, ZERO, ONE], pm(q1, q)), fq(-6)))
    assert n[-1] == ONE and len(n) == norm + 1
    return n


def cm19_fiber(args):
    a, basis = args
    gamma, q = q19_polynomial()
    gb = (gamma[0], -gamma[1])
    qb = [(x[0], -x[1]) for x in q]
    ng = qmap(q, 19)
    nb = [(x[0], -x[1]) for x in ng]
    F = pa(ng, ps(pm(q, q), fm(fq(-a), fp(gamma, 2))))
    assert len(F) == 20 and F[-1] == ONE

    def red(A):
        A = A[:]
        for i in range(len(A) - 1, 18, -1):
            v = A[i]
            if v != ZERO:
                for j in range(19):
                    A[i-19+j] = fs(A[i-19+j], fm(v, F[j]))
        return ptrim(A[:19])

    def rm(A, B):
        return red(pm(A, B))

    def rp(A, n):
        out = [ONE]
        while n:
            if n & 1:
                out = rm(out, A)
            A = rm(A, A)
            n //= 2
        return out

    def ri(A):
        r0, r1, s0, s1 = F, A, [ZERO], [ONE]
        while r1 != [ZERO]:
            quot, r2 = pd(r0, r1)
            s2 = pa(s0, ps(pm(quot, s1), fq(-1)))
            r0, r1, s0, s1 = r1, r2, s1, s2
        assert len(r0) == 1 and r0[0] != ZERO
        ans = red(ps(s0, fi(r0[0])))
        assert rm(A, ans) == [ONE]
        return ans

    T = red(nb)
    V = ps(rp(qb, 2), fp(gb, 2))
    U, W = rp(T, 3), rp(V, 3)
    Up, Wp = [[ONE]], [[ONE]]
    for j in range(22):
        Up.append(rm(Up[-1], U))
        Wp.append(rm(Wp[-1], W))
    # N=136=2*offset+6*22, offset=2.  Divide by gamma and a^2.
    frame = ps(rm(rp(ri(q), 136), rp(T, 2)),
               fm(fp(gamma, -137), fq(Q(1, a*a))))
    traces = [fq(19)]
    for k in range(1, 19):
        val = fm(fq(k), F[19-k])
        for j in range(1, k):
            val = fa(val, fm(F[19-j], traces[k-j]))
        traces.append(fn(val))
    basis_values = []
    for vec in basis:
        polynomial = [ZERO]
        for j, coeff in enumerate(vec):
            if coeff != ZERO:
                polynomial = pa(polynomial, ps(rm(Up[j], Wp[22-j]), coeff))
        polynomial = rm(frame, polynomial)
        val = ZERO
        for j, coeff in enumerate(polynomial):
            val = fa(val, fm(coeff, traces[j]))
        basis_values.append(val)
    return a, basis_values


def main():
    start = time.monotonic()
    data = json.loads((BASE / "notes/2026-11-14-theta-degree136-cm7-exact.json").read_text())
    M = tuple(Mat([[Q(x) for x in row] for row in data["matrix"][part]])
              for part in ("real", "delta"))
    I = identity(23)
    assert kp(M, 18, I) == I
    polys = source_polys()
    vectors = [kvec([w[j] for j in range(23)]) for w in polys]
    omega = fq(Q(-1, 2), Q(1, 2))
    six_roots = [ONE, omega, fp(omega, 2), fq(-1),
                 fm(fq(-1), omega), fm(fq(-1), fp(omega, 2))]
    out = {
        "normalization": "b=1; N7=M_gamma7/gamma7; W=R_2(z)*C(2z), without division by 2",
        "basis": "sigma^136*x^2*X^j, j=0,...,22",
        "source_polynomials": [[str(w[j]) for j in range(23)] for w in polys],
        "six_mu6_projections": [],
    }
    positive = kzero(23, 23)
    for lam in six_roots:
        P = eig_project(M, lam, I)
        if fp(lam, 3) == ONE:
            positive = ka(positive, P)
        row = {"eigenvalue": [str(x) for x in lam], "full_dimension": rank(P), "sources": []}
        for v in vectors:
            w = km(P, v)
            row["sources"].append({"zero": w == kzero(23, 1),
                                   "mass": [str(x) for x in get_entry(w, 22)],
                                   "vector": serialize_matrix(w)})
        out["six_mu6_projections"].append(row)
        print("mu6", row["eigenvalue"], "dimension", row["full_dimension"],
              "zero", [x["zero"] for x in row["sources"]], flush=True)
    assert rank(positive) == 5
    for v in vectors:
        assert km(kp(M, 9, I), v) == v
        orbit, cur = [], v
        for _ in range(9):
            orbit.append(cur)
            cur = km(M, cur)
        assert rank(cols(orbit)) == 9
    chosen, pivot_columns = [], []
    for j in range(23):
        v = column(positive, j)
        if rank(cols(chosen + [v])) > len(chosen):
            chosen.append(v)
            pivot_columns.append(j)
        if len(chosen) == 5:
            break
    B = cols(chosen)
    basis = [[get_entry(B, j, i) for j in range(23)] for i in range(5)]
    targets = list(range(1, 6))
    E = tuple(Mat([[sum(B[k][j, i] * a**(3*j) for j in range(23))
                   for i in range(5)] for a in targets]) for k in (0, 1))
    Ei = kinv(E)
    rows = {}
    with ProcessPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(cm19_fiber, (a, basis)) for a in targets]
        for future in as_completed(futures):
            a, values = future.result()
            rows[a] = values
            print("CM19 exact fiber", a, "elapsed", round(time.monotonic()-start, 2), flush=True)
    F = tuple(Mat([[rows[a][i][k] for i in range(5)] for a in targets]) for k in (0, 1))
    M19 = km(Ei, F)
    # Coordinates of N7 on the same block use five evaluations of the known full matrix.
    MB = km(M, B)
    F7 = tuple(Mat([[sum(MB[k][j, i] * a**(3*j) for j in range(23))
                    for i in range(5)] for a in targets]) for k in (0, 1))
    M7b = km(Ei, F7)
    assert km(M7b, M19) == km(M19, M7b)
    assert kp(M19, 6, identity(5)) == identity(5)
    # The independent 17-local reflection, with its full absolute scalar.
    D33 = ks(km(M19, kp(M7b, 4, identity(5))), fp(omega, -1))
    assert km(D33, D33) == identity(5)
    assert rank(ka(identity(5), D33)) == 3
    assert rank(ka(identity(5), ks(D33, fq(-1)))) == 2
    coord_sources = []
    for v in vectors:
        v = km(positive, v)
        ev = tuple(Mat([[sum(v[k][j, 0]*a**(3*j) for j in range(23))]
                        for a in targets]) for k in (0, 1))
        coord_sources.append(km(Ei, ev))
    joints = []
    for k in range(1, 6):
        lam7 = fp(omega, 2*k-2)
        lam19 = fm(fq((-1)**(k+1)), fp(omega, k))
        P = km(eig_project(M7b, lam7, identity(5)),
               eig_project(M19, lam19, identity(5)))
        assert rank(P) == 1
        row = {"k": k, "curve_D": 8*(-17)**k,
               "N7": [str(x) for x in lam7], "N19": [str(x) for x in lam19],
               "sources": []}
        for v in coord_sources:
            w = km(B, km(P, v))
            assert w != kzero(23, 1)
            assert w[1] == Mat(23, 1)
            row["sources"].append({"mass": str(w[0][22, 0]),
                                   "polynomial_b1": [str(w[0][j, 0]) for j in range(23)]})
        joints.append(row)
    out["joint_positive_mu6_sources"] = joints

    # The actual integral combination isolates the new k=2 source.
    combined = ka(ks(vectors[0], fq(101)), ks(vectors[1], fq(-64)))
    Pplus = ks(ka(ka(I, kp(M, 3, I)), kp(M, 6, I)), fq(Q(1, 3)))
    new = ks(km(Pplus, combined), fq(Q(-5, 3848)))
    X = Poly([0, 1])
    factored = ((X+1)*(X**2+20*X-8)*(7*X**2-4*X+16) *
                (X**4+40*X**3+2112*X**2+3136*X+1792) *
                (13*X**4+52*X**3+1536*X**2+1024*X+256) *
                (X**8+1232*X**7-58688*X**6-49408*X**5-439040*X**4 -
                 2111488*X**3-1949696*X**2-851968*X-32768))/91
    assert factored.degree() == 21 and factored[21] == 1
    assert new == kvec([factored[j] for j in range(23)])
    assert km(M, new) == ks(new, fp(omega, 2))
    for k in (1, 3, 4, 5):
        v13 = [Q(x) for x in joints[k-1]["sources"][0]["polynomial_b1"]]
        v15 = [Q(x) for x in joints[k-1]["sources"][1]["polynomial_b1"]]
        assert all(101*a == 64*b for a, b in zip(v13, v15))
    residual = ka(combined, ks(km(Pplus, combined), fq(-1)))
    assert residual[0][22, 0] == 0 and residual[1][22, 0] == 0
    orbit, cur = [], residual
    for _ in range(9):
        orbit.append(cur)
        cur = km(M, cur)
    assert rank(cols(orbit)) == 6
    out["new_source_b1_polynomial"] = [str(factored[j]) for j in range(23)]
    out["new_source_z6"] = "1"
    out["unprojected_combination_external_cyclic_dimension"] = 6
    out["new_source_coefficients_in_W13_W15"] = [
        joints[1]["sources"][i]["polynomial_b1"][21] for i in (0, 1)]
    print("five complete arithmetic candidate lines and isolated k=2 source verified", flush=True)
    out["positive_mu6_basis_columns"] = pivot_columns
    out["positive_mu6_basis"] = serialize_matrix(B)
    out["positive_mu6_N7"] = serialize_matrix(M7b)
    out["positive_mu6_N19"] = serialize_matrix(M19)
    out["positive_mu6_D33"] = serialize_matrix(D33)
    out["sigma19_division_polynomial"] = [[str(x) for x in a] for a in q19_polynomial()[1]]
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
    print("CM19 block ready", round(time.monotonic()-start, 2), flush=True)


if __name__ == "__main__":
    main()
