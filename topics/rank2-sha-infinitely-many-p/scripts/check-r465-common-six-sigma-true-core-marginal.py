#!/usr/bin/env python3
"""R465: original common six-sigma joint, true T-core, and new S marginal.

The quarter calculation is a full polynomial identity in
Q(sqrt(3),delta)[x,w]/(w^2=f^2*(x^3+1)), delta^2=-3.
No interpolation, truncated Taylor identity, or target-prime scan is used.
The canonical quarter constant is R419(10): c_t^8=(e-h)/(12*h^2*f^2).
"""
from pathlib import Path
import json
import runpy
import time
import sympy as sy
from sympy.polys.domains import QQ
from sympy.polys.rings import ring

BASE = Path(__file__).resolve().parents[1]
H = runpy.run_path(str(BASE / "scripts/check-r466-fixed-two-division-source.py"))


def exact_quarter_sum():
    start = time.monotonic()
    field = QQ.algebraic_field(sy.sqrt(3), sy.sqrt(-3))
    ring_x, x = ring("x", field)
    zero, one = ring_x.zero, ring_x.one
    delta = field.from_sympy(sy.sqrt(-3))
    omega = (delta-1)/2
    e = field.from_sympy(-1-sy.sqrt(3))
    h = -field.one
    ebar = 2*h-e
    f2 = e**3+1
    em, en, hm = omega*ebar, omega**2*ebar, omega*h
    k = -3*delta/f2                 # y(m t)=k*y(t), m=2+3 omega
    X, Y = x**3, x**3+1
    R2 = X**2+20*X-8
    ell = 8*Y**2
    xnum = 2*Y*x*(X-8)             # x(2z)=xnum/ell
    tau2 = f2*Y

    def add(a, b):
        return a[0]+b[0], a[1]+b[1]

    def scale(a, c):
        return a[0]*c, a[1]*c

    def mul(a, b):
        return (a[0]*b[0]+a[1]*b[1]*tau2,
                a[0]*b[1]+a[1]*b[0])

    def power(a, n):
        out = one, zero
        while n:
            if n & 1:
                out = mul(out, a)
            a = mul(a, a)
            n //= 2
        return out

    def constant(a):
        return a, zero

    # All factors below are homogeneous numerators after P=[2]z.
    # tau=f*y(z), f*y(2z)=R2*tau/ell.
    u = (f2*ell+3*e*e*(xnum-e*ell)/2, R2)
    nt = (e*xnum*xnum+e*e*xnum*ell+2*ell*ell, -2*R2*ell)
    de, dm = xnum-e*ell, xnum-em*ell
    yt = add((zero, -R2*de**3),
             mul((-f2*ell, R2),
                 add(constant(xnum*de**2), scale(nt, -ell))))
    middle = add(power(nt, 3), constant(-8*de**6))
    p2 = add(add(scale(power(nt, 6), field(7)),
                 scale(power(nt, 3), -4*de**6)), constant(16*de**12))
    um = (k*k*f2*ell+3*em*em*(xnum-em*ell)/2, k*R2)
    nm = (em*xnum*xnum+em*em*xnum*ell+2*ell*ell, -2*k*R2*ell)
    difference = add(constant(en*dm**2), scale(nm, -field.one))
    numerator = power(u, 14)
    for factor in (um, difference, power(nt, 2), yt, middle, p2):
        numerator = mul(numerator, factor)

    c8 = (e-h)/(12*h*h*f2)         # R419 canonical sign, not h-e
    coeff = 3*2**32*c8**7*(7*e**6-4*e**3+16)**2/(k*f2**8)
    root_numerator = x*x-2*hm*x-2*hm*hm
    # Sum over the two signs of f first.
    complete_numerator = numerator[0]*Y**15*R2*root_numerator*coeff*2
    complete_denominator = ell**8*(xnum-h*ell)**7*(xnum-hm*ell)*dm**2*de**25
    quotient, remainder = complete_numerator.div(complete_denominator)
    assert not remainder
    assert quotient.degree() == 67
    four_coeffs = []
    twelve_coeffs = []
    for j in range(69):
        c = field.to_sympy(quotient.get((j,), field.zero))
        # Fix delta=i*sqrt(3) and exchange the two values of e.
        conjugate = c.xreplace({sy.sqrt(3): -sy.sqrt(3), sy.I: -sy.I})
        c = sy.expand(c+conjugate)
        four_coeffs.append(c)
        # sigma^136*x^j has weight 2(j+1) for the mu_3 rotation.
        twelve_coeffs.append(sy.expand(3*c) if j % 3 == 2 else sy.Integer(0))
    print("Complete quarter polynomial division, remainder zero;",
          round(time.monotonic()-start, 2), "s", flush=True)
    return four_coeffs, twelve_coeffs


def exact_half_sum_and_original():
    x = sy.symbols("x")
    X, Y = x**3, x**3+1
    delta = sy.sqrt(-3)
    # h=-1: r_{3delta}(t)*c_t^56=delta/6561.
    ph = (4*delta/sy.Integer(729)*(X+1)*(x+1)**2*(x-2)**2
          * (-(x-2)**3-8*(x+1)**3)
          * (7*(x-2)**6+4*(x-2)**3*(x+1)**3+16*(x+1)**6))
    ph = sy.Poly(sy.expand(ph), x)
    half_double = sy.Poly(sy.expand(sum(
        c*2**34*Y**(17-j)*x**j*(X-8)**j/sy.Integer(4)**j
        for (j,), c in ph.terms())), x)
    half_sum = [sy.expand(3*half_double.nth(j)) if j % 3 == 2 else sy.Integer(0)
                for j in range(69)]
    p1 = [sy.Rational(-128, 7), sy.Rational(-80, 7),
          sy.Rational(-12, 7), sy.Rational(-53, 7), sy.Integer(1)]
    original = sy.Poly(sy.expand(
        2**30*x*x*(X-8)**2*sum(
            c*Y**(15-3*j)*X**j*(X-8)**(3*j)/sy.Integer(4)**(3*j)
            for j, c in enumerate(p1))), x)
    return half_sum, [original.nth(j) for j in range(69)]


def main():
    four, quarter = exact_quarter_sum()
    half, original = exact_half_sum_and_original()
    # rho=-1/84 times the raw six-sigma product; K72 coefficients
    # are 1/4 on E[4]\E[2] and -1/4 on E[2].
    xi_x = [sy.expand((-quarter[j]+half[j]-84*original[j])/336)
            for j in range(69)]
    assert all(v == 0 for j, v in enumerate(xi_x) if j % 3 != 2)
    xi = [xi_x[j] for j in range(2, 69, 3)]

    Q, Mat = H["Q"], H["Mat"]
    km, ka, ks, kp = (H[k] for k in ("km", "ka", "ks", "kp"))
    identity, eig_project = H["identity"], H["eig_project"]
    omega = H["fq"](Q(-1, 2), Q(1, 2))
    omega2 = H["fp"](omega, 2)

    def decode(data):
        return tuple(Mat([[Q(x) for x in row] for row in data[part]])
                     for part in ("real", "delta"))

    def vector(values):
        return (Mat([[Q(str(sy.simplify(sy.re(c))))] for c in values]),
                Mat([[Q(str(sy.simplify(sy.im(c)/sy.sqrt(3))))] for c in values]))

    def evaluate(a):
        return tuple(Mat([[sum(a[k][j, i]*Q(t)**(3*j)
                               for j in range(a[k].nrows()))
                           for i in range(a[k].ncols())] for t in range(1, 6)])
                     for k in (0, 1))

    data = json.loads((BASE / "notes/2026-11-14-theta-degree136-cm7-exact.json").read_text())
    m = decode(data["matrix"])
    data19 = json.loads((BASE / "scripts/check-r466-fixed-two-division-source.json").read_text())
    b = decode(data19["positive_mu6_basis"])
    m19 = decode(data19["positive_mu6_N19"])
    bi = H["kinv"](evaluate(b))
    i = identity(23)
    v = vector(xi)
    s2 = vector([original[j] for j in range(2, 69, 3)])
    assert H["get_entry"](s2, 21) == H["fq"](64)
    negative = ks(ka(v, ks(km(kp(m, 9, i), v), H["fq"](-1))), H["fq"](Q(1, 2)))
    assert negative == ks(s2, H["fq"](Q(-1, 4), Q(-1, 4)))

    selected = eig_project(m, omega2, v)
    coordinates = km(bi, evaluate(selected))
    assert km(b, coordinates) == selected
    projected = ks(ka(selected, ks(km(b, km(m19, coordinates)), H["fn"](omega))),
                   H["fq"](Q(1, 2)))
    new_data = json.loads((BASE / "scripts/check-r470-original-negative-source-new-line.json").read_text())
    new = decode(new_data["Snew"])
    assert projected == ks(new, H["fq"](Q(52, 3)))
    assert H["get_entry"](projected, 22) == H["fq"](0)
    eig_matrix = eig_project(m, omega2, i)
    eig_coordinates = km(bi, evaluate(eig_matrix))
    assert km(b, eig_coordinates) == eig_matrix
    full_projector = ks(ka(eig_matrix,
                         ks(km(b, km(m19, eig_coordinates)), H["fn"](omega))),
                        H["fq"](Q(1, 2)))
    assert km(full_projector, full_projector) == full_projector
    assert H["rank"](full_projector) == 1
    orbit, cur = [], v
    for _ in range(18):
        orbit.append(cur)
        cur = km(m, cur)
    assert H["rank"](H["cols"](orbit)) == 10

    # The actual six independent physical inputs and all companions.
    delta = sy.sqrt(-3)
    physical = sy.Matrix([
        [1, 1, 1, 1, 3*delta, 4],
        [3*delta, 3*delta, 3*delta, 3*delta, 29, 0],
        [1, 1, 1, 1, 3*delta, -14],
        [4, -1, 0, 0, 0, 0],
        [7, 7, -15, 0, 0, 0],
        [7, 7, 7, -22, 0, 0],
    ])
    gram = sy.simplify(physical*sy.diag(3, 12, 7, 7, 1, 1)*sy.conjugate(physical.T))
    expected_gram = [72, 1624, 252, 60, 2310, 4466]
    assert gram == sy.diag(*expected_gram)
    determinant = sy.simplify(physical.det())
    assert abs(determinant) == 1008*3190
    old_y_cover = sy.Matrix([
        [2, 2, 2, 2, 2, 4],
        [2, 2, 2, 2, -58, 0],
        [2, 2, 2, 2, 2, -30],
        [4, -1, 0, 0, 0, 0],
        [7, 7, -15, 0, 0, 0],
        [7, 7, 7, -22, 0, 0],
    ])
    d = sy.diag(3, 12, 7, 7, 1, 1)
    cover_gram = sy.simplify(old_y_cover*d*sy.conjugate(old_y_cover.T))
    assert cover_gram == sy.diag(136, 3480, 1020, 60, 2310, 4466)
    cross = sy.simplify(old_y_cover*d*physical[0, :].T)
    assert cross[3, 0] == cross[4, 0] == cross[5, 0] == 0
    # Each quarter flat twist disappears on this fixed cover.
    for entry in cross[:3, 0]:
        a = sy.simplify(sy.re(entry)/4+sy.im(entry)/(4*sy.sqrt(3)))
        bomega = sy.simplify(sy.im(entry)/(2*sy.sqrt(3)))
        assert a.is_Integer and bomega.is_Integer

    X = sy.symbols("X")
    real_poly = sy.Poly(sum(sy.re(c)*X**j for j, c in enumerate(xi)), X)
    delta_poly = sy.Poly(sum(sy.im(c)/sy.sqrt(3)*X**j for j, c in enumerate(xi)), X)
    common = ((X+1)*(X**2+20*X-8)*(7*X**2-4*X+16)
              * (X**4+40*X**3+2112*X**2+3136*X+1792))
    ar, rr = sy.div(-7*real_poly.as_expr(), common, X)
    ai, ri = sy.div(-7*delta_poly.as_expr(), common, X)
    assert rr == 0 and ri == 0
    report = {
        "field": "Q(delta), delta^2=-3; quarter calculation also adjoins sqrt(3)",
        "normalization": "rho=-1/84*C29(A)*sigma(c)*sigma(d); S=x2Q4sigma34, W marginal=6delta*T",
        "basis": "sigma^136*x^2*X^j, j=0,...,22",
        "canonical_quarter_constant": "c_t^8=(e-h)/(12*h^2*f^2)",
        "quarter_remainder_zero": True,
        "quarter_four_point_coefficients_x": H["serialize_matrix"](vector(four)),
        "quarter_twelve_point_coefficients_x": H["serialize_matrix"](vector(quarter)),
        "half_three_point_coefficients_x": H["serialize_matrix"](vector(half)),
        "Xi_double": H["serialize_matrix"](v),
        "S_double": H["serialize_matrix"](s2),
        "negative_block": H["serialize_matrix"](negative),
        "new_projection": H["serialize_matrix"](projected),
        "new_projection_coefficient": "52/3",
        "first_axis_projector_rank": 1,
        "negative_block_coefficient": ["-1/4", "-1/4"],
        "Xi_common_polynomial_factor": str(common),
        "Xi_degree12_real_factor": [str(sy.Poly(ar, X).nth(j)) for j in range(13)],
        "Xi_degree12_delta_factor": [str(sy.Poly(ai, X).nth(j)) for j in range(13)],
        "Xi_cyclic_dimension": 10,
        "full_physical_matrix": [[str(x) for x in row] for row in physical.tolist()],
        "full_Gram": expected_gram, "full_determinant": str(determinant),
        "old_Y_fixed_cover": [[str(x) for x in row] for row in old_y_cover.tolist()],
        "old_Y_fixed_cover_Gram": [136, 3480, 1020, 60, 2310, 4466],
        "old_Y_fixed_cover_determinant": str(old_y_cover.det()),
        "old_Y_fixed_cover_cross_W": [str(x) for x in cross],
        "boundary": "The first core state's full S marginal is Xi, not a known central zero; only the displayed complete CM projection is Snew."
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2)+"\n")
    print("Exact true-core marginal: Q Xi(2z)=(52/3) Snew")
    print("Exact negative block: -(1+delta)/4 * S(2z)")
    print("Full six-input Gram", expected_gram, "det", determinant)


if __name__ == "__main__":
    main()
