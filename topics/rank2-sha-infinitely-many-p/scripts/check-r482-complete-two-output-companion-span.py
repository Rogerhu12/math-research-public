#!/usr/bin/env python3
"""Exact companion span of the original degree136 by degree9792 source.

This is one fixed characteristic-zero theta calculation, not a prime scan.
Every coefficient is a whole first-axis theta polynomial.  The six classes
are checked separately. The two complete quarter/half-torsion constraints
give an upper bound of 51 in the whole first theta space.
"""
from pathlib import Path
from math import factorial
import json
from flint import fmpq as Q, fmpq_poly as Poly, fmpq_mat as Mat

BASE = Path(__file__).resolve().parents[1]
x = Poly([0, 1])
Y = x**3+1
zero = (Poly([0]), Poly([0]))
one = (Poly([1]), Poly([0]))


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def scale(a, c):
    return a[0]*c, a[1]*c


def mul(a, b):
    return a[0]*b[0]+Y*a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def deriv(a):
    return 3*x*x*a[1]+2*Y*a[1].derivative(), 2*a[0].derivative()


def conv(a, b, n):
    out = []
    for j in range(n+1):
        v = zero
        for k in range(j+1):
            v = add(v, mul(a[k], b[j-k]))
        out.append(v)
        if j and j % 24 == 0:
            print("convolution through", j, flush=True)
    return out


def from_X(cs):
    ans = Poly([0])
    for j, c in enumerate(cs):
        ans += Q(c)*x**(3*j)
    return ans


def main():
    data = json.loads((BASE/"scripts/check-r471-original-six-sigma-normtwo-factor.json").read_text())
    f = from_X(data["six_sigma_in_sigma72_frame"])
    u = x*x*from_X(data["theta4_in_sigma32_x_frame"])**2
    nmax = 101
    df, du = (f, Poly([0])), (u, Poly([0]))
    fs, us = [], []
    for j in range(nmax+1):
        fs.append(scale(df, Q(8**j, factorial(j))))
        us.append(scale(du, Q((-9)**j, factorial(j))))
        df, du = deriv(df), deriv(du)
    logs = [zero for _ in range(nmax+1)]
    dx = (x, Poly([0]))
    for j in range(2, nmax+1):
        logs[j] = scale(dx, Q(-(72*8**j+64*(-9)**j), factorial(j)))
        dx = deriv(dx)
    sig = [one]
    for j in range(1, nmax+1):
        v = zero
        for k in range(1, j+1):
            v = add(v, scale(mul(logs[k], sig[j-k]), Q(k, j)))
        sig.append(v)
    print("all exact input and Gaussian coefficients ready", flush=True)
    coeffs = conv(conv(fs, us, nmax), sig, nmax)
    out = {
        "source": "F72(w+8q)*Theta(4w-36q)^2, b=1",
        "whole_theta_degree": 136,
        "companion_degree": 9792,
        "classes": {},
    }
    total = 0
    for residue in range(6):
        js = list(range(residue, nmax+1, 6))
        assert len(js) == 17
        parity = residue % 2
        r = ((4+residue)//2 if parity == 0 else (1+residue)//2) % 3
        max_i = 68 if parity == 0 else 66
        inds = list(range(r, max_i+1, 3))
        cols = []
        for j in js:
            poly = coeffs[j][parity]
            assert not coeffs[j][1-parity]
            assert poly.degree() <= max_i
            assert all(poly[k] == 0 for k in range(poly.degree()+1)
                       if k % 3 != r)
            cols.append([poly[i] for i in inds])
        mat = Mat([[cols[j][i] for j in range(len(js))]
                   for i in range(len(inds))])
        rank = mat.rank()
        total += rank
        record = {"q_degrees": js, "basis_y_parity": parity,
                  "basis_x_exponents": inds, "rank": rank,
                  "whole_coordinate_matrix": [[str(mat[i, j]) for j in range(mat.ncols())]
                                               for i in range(mat.nrows())]}
        rr, rr_rank = mat.rref()
        assert rr_rank == rank
        chosen_cols = [next(j for j in range(rr.ncols()) if rr[i, j])
                       for i in range(rank)]
        selected = Mat([[mat[i, j] for j in chosen_cols]
                        for i in range(mat.nrows())])
        rr, rr_rank = selected.transpose().rref()
        assert rr_rank == rank
        pivots = [next(j for j in range(rr.ncols()) if rr[i, j])
                  for i in range(rank)]
        minor = Mat([[selected[i, j] for j in range(rank)] for i in pivots])
        determinant = minor.det()
        assert determinant
        record["selected_q_degrees"] = [js[j] for j in chosen_cols]
        record["pivot_coordinate_indices"] = pivots
        record["minor_determinant"] = str(determinant)
        out["classes"][str(residue)] = record
        print("mu6 class", residue, "rank", rank, flush=True)
    out["total_rank"] = total
    def b2(j):
        return (69*j+68) % 136, (-1)**j
    def k4(j):
        return (35*j+68) % 136, -(-1)**j
    def compose(f, g, j):
        k, c = g(j)
        l, d = f(k)
        return l, c*d
    def trace(f):
        return sum(c for j in range(136) for k, c in [f(j)] if k == j)
    for j in range(136):
        assert compose(b2, b2, j) == (j, 1)
        assert compose(k4, k4, j) == (j, 1)
        assert compose(b2, k4, j) == compose(k4, b2, j)
    traces = [trace(b2), trace(k4), trace(lambda j: compose(b2, k4, j))]
    assert traces == [-68, -34, -34]
    joint_dimension = (136-traces[0]-traces[1]+traces[2])//4
    assert joint_dimension == 51 and total == 51
    assert [out["classes"][str(r)]["rank"] for r in range(6)] == [8, 9, 8, 9, 8, 9]
    out["half_quarter_product_traces"] = traces
    out["expected_E2_trace_zero_dimension"] = 102
    out["complete_joint_minus_dimension"] = joint_dimension
    out["full_joint_rank_attained"] = total == joint_dimension
    rendered = json.dumps(out, indent=2)+"\n"
    dest = Path(__file__).with_suffix(".json")
    if len(rendered.encode()) > 1_000_000:
        import gzip
        dest = Path(str(dest)+".gz")
        with gzip.open(dest, "wt") as f:
            f.write(rendered)
    else:
        dest.write_text(rendered)
    print("total rank", total, "saved bytes", dest.stat().st_size,
          "in", dest.name, flush=True)


if __name__ == "__main__":
    main()
