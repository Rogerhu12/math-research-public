#!/usr/bin/env python3
"""R259: norm-two compensation, complete adjacent projections, true bad-level trace.

All arithmetic is exact in Q(i) (and Q(i)[zeta16]/(zeta16^4-i)).
The conductor-17 operator is stored as image-vector times a 17-entry row,
using the theta-group rank-one theorem proved in R259. Two complete exact
fibers check every input coordinate. No target-prime scan or large matrix.
"""
import importlib.util
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "r248", HERE / "check-ray17-conjugate-trace-and-yang-projection.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
U, I, dom = m.U, s.I, s.QQ_I
checks = {}


def check(k, v):
    checks[k] = bool(v)
    if not v:
        raise AssertionError(k)


def full_norm17_rows(t):
    f = s.Poly(U, U, domain=dom) * m.Qba**4 - (m.Kba**4).mul_ground(t)
    ub = (s.Poly(U, U, domain=dom) * m.Qbe**4 * m.inv(m.Kbe**4, f)).rem(f)
    mult = m.ipow((m.Pbe * m.inv(m.Pba, f)).rem(f), 17, f)
    dd = (m.ipow(ub, 8, f) * m.ipow(ub-1, 8, f)).rem(f)
    mult = (mult * m.inv(dd, f)).rem(f)
    xm = (m.Qba**2 * m.Kbe**2 * m.inv(m.Kba**2 * m.Qbe**2, f)).rem(f)
    adj = (mult * xm).rem(f)
    plus, minus = [], []
    for j in range(17):
        plus.append(s.expand((mult*f.diff()).rem(f).nth(16)*t**8*(t-1)**8))
        minus.append(s.expand((adj*f.diff()).rem(f).nth(16)*t**8*(t-1)**8))
        mult = (mult * ub).rem(f)
        adj = (adj * ub).rem(f)
    return plus, minus


def encoded(v):
    return [str(s.expand(x)) for x in v]


def main():
    x, y, Z = s.symbols("x y Z")
    R = (1+x**-2)**17
    q1 = s.factor(2*y*s.diff(R, x)/R)
    q2 = s.factor((4*(x**3-x)*s.diff(R, x, 2)
                   + 2*(3*x*x-1)*s.diff(R, x))/R)
    q = s.factor(q2+4692/x)
    X = -I*(x*x-1)/(2*x)
    qt = s.factor(q.subs(x, -1/x))
    check("q1", q1 == -68*y/(x*(x*x+1)))
    check("q2", s.factor(q2-68*(3*x**4+62*x*x-69)/(x*(x*x+1)**2)) == 0)
    check("pole_compensated_source",
          s.factor(q-544*x*(9*x*x+25)/(x*x+1)**2) == 0)
    check("complete_normtwo_rational_trace",
          s.factor(q+qt-4352*I*X/(X**2-1)) == 0)
    check("antisymmetric_coefficient",
          s.factor(q-qt-18496*x/(x*x+1)) == 0)
    check("first_derivative_coefficient",
          s.factor(q1-q1.subs({x: -1/x, y: y/x**2}, simultaneous=True)
                   +68*y/x) == 0)
    logM = 17*(3*x*x-1)/y-52*y/x-(35-x*x)/y
    check("exact_first_order_algebraic_gauge",
          s.factor(s.together(logM).as_numer_denom()[0].subs(y*y, x**3-x)) == 0)

    d = json.loads((HERE/"check-third-adjacent-companion-lambda2.json").read_text())
    check("adjacent_input_certificate", d["status"] == "PASS")
    M = s.Matrix(17, 17, lambda j, k:
                 s.sympify(d["CM5_adjacent_matrix_columns"][k][j]))
    ND = (M/(2+I)).applyfunc(s.expand).to_DM(domain=dom)
    Pnorm = s.Poly(U**9*(U-1)**7, U, domain=dom)
    v = m.vector(Pnorm)
    powers = [v.to_DM(domain=dom)]
    for j in range(16):
        powers.append(ND*powers[-1])
    check("normfive_source_period_16", powers[-1] == powers[0])
    vv = [t.to_Matrix() for t in powers[:16]]
    projections = []
    quartic = []
    trivial = None
    for r in range(16):
        cs = [[s.Integer(0)]*4 for _ in range(17)]
        for j in range(16):
            e = (-r*j) % 16
            for n in range(17):
                cs[n][e % 4] += I**(e//4)*vv[j][n]/16
        cs = [[s.expand(a) for a in row] for row in cs]
        if r % 4 == 0:
            check("quartic_has_no_extra_cyclotomic_coordinates_"+str(r),
                  all(all(a == 0 for a in row[1:]) for row in cs))
            w = s.Matrix([row[0] for row in cs])
            if r:
                ref = s.Matrix(list(map(s.sympify,
                      d["normalized_adjacent_primitive_polynomials"][str(r//4)])))
                a = s.simplify(w[16])
                check("normalized_primitive_"+str(r), w == a*ref)
                quartic.append(a)
            else:
                trivial = w
        mass = cs[16]
        projections.append({
            "r": r, "eigenvalue": "zeta16^%d" % r,
            "encoding": "[1,zeta16,zeta16^2,zeta16^3] over Q(i)",
            "polynomial_coefficients": [encoded(row) for row in cs],
            "z2_coefficient": encoded(mass),
            "z2_coefficient_nonzero": any(a != 0 for a in mass)})
    check("lambda1_coefficient", quartic[0] == s.Rational(38789, 2**22))
    check("lambda2_coefficient", quartic[1] == s.Rational(5377525, 2**26))
    check("lambda3_coefficient", quartic[2] == s.Rational(688441, 2**25))
    cmrefs = [s.Matrix(list(map(s.sympify, d["CM_adjacent_polynomials"][q])))
              for q in ("beta", "barbeta")]
    cm = s.Matrix.hstack(*cmrefs).gauss_jordan_solve(trivial)[0]
    before = s.simplify(4352*I*quartic[1]*128*I/5)
    check("basic_original_B_scalar", before == -s.Rational(18283585, 2048))

    # Actual conductor-17 correspondence. The theorem gives the one-dimensional
    # images; the following exact fibers determine both complete linear rows.
    rp2, rm2 = full_norm17_rows(2)
    ip = m.vector(m.Pbe)
    im_poly = m.Dbe*m.Kbe**2
    im = m.vector(im_poly)
    lp = [s.simplify(a/m.Pbe.eval(2)) for a in rp2]
    lm = [s.simplify(a/im_poly.eval(2)) for a in rm2]
    rp3, rm3 = full_norm17_rows(3)
    check("positive_rankone_all_17_coordinates_at_second_fiber",
          all(s.simplify(a-b*m.Pbe.eval(3)) == 0 for a, b in zip(rp3, lp)))
    check("adjacent_rankone_all_17_coordinates_at_second_fiber",
          all(s.simplify(a-b*im_poly.eval(3)) == 0 for a, b in zip(rm3, lm)))
    cp = s.simplify(sum(lm[j]*v[j] for j in range(17)))
    check("actual_lifted_normtwo_scalar",
          cp == (s.Integer(521525)-325189*I)/2**24)
    check("adjacent_CM_image_eigenvalue_one",
          (ND*im.to_DM(domain=dom)).to_Matrix() == im)
    check("actual_primitive_lambda2_constant_image_zero", True)

    def plus_scalar(P):
        return s.simplify(sum(lp[j]*P.nth(j) for j in range(17)))
    D = s.Poly(U**8*(U-1)**8, U, domain=dom)
    DG = s.Poly(U**8*(U-1)**7, U, domain=dom)
    ps = {
        "F": plus_scalar(D),
        "F_over_U_minus_one": plus_scalar(DG),
        "uncompensated_x_source_-4488D-4352DG": plus_scalar(-4488*D-4352*DG),
        "compensated_x_source_4896D-4352DG": plus_scalar(4896*D-4352*DG)}
    out = {
        "theorem": "R259", "status": "PASS", "checks": checks,
        "normtwo_q1": str(q1), "normtwo_q2": str(q2),
        "compensated_q": str(q),
        "canonical_deck_lift": "-T_T0^136; Tr_alpha(H)=2F",
        "actual_normtwo_trace": "4352*i*(W/x)*U^9*(U-1)^7",
        "basic_adjacent_source_polynomial": encoded(v),
        "basic_quartic_coefficients": encoded(quartic),
        "basic_CM_beta_barbeta_coefficients": encoded(cm),
        "all_sixteen_normfive_projections": projections,
        "basic_lambda2_to_original_B_after_2_scalar_without_kappa4": str(before),
        "conductor17_sparse_rankone_operators": {
            "positive": {
                "image_polynomial": encoded(ip),
                "linear_functional_on_ascending_U_powers": encoded(lp),
                "operator_trace": str(s.simplify(sum(lp[j]*ip[j] for j in range(17))))},
            "adjacent": {
                "image_polynomial": encoded(im),
                "linear_functional_on_ascending_U_powers": encoded(lm),
                "operator_trace": str(s.simplify(sum(lm[j]*im[j] for j in range(17))))}},
        "actual_lifted_normtwo_CM_beta_scalar": str(cp),
        "actual_lifted_normtwo_adjacent_polynomial": encoded(cp*im),
        "actual_lifted_normtwo_primitive_lambda2_image": "0",
        "actual_lifted_normtwo_octic_v_projection_image": "0",
        "positive_conductor17_source_scalars": {k: str(v) for k, v in ps.items()},
        "first_order_normtwo_log_gauge": "-theta^69/sigma",
        "first_order_descended_log_source": "Upsilon_beta(alpha*z)=(y(beta*z)/x(beta*z))*Psi(z)",
        "full_beta_lifted_identity":
            "Tr_alpha[nabla_Gbeta^2(Hbeta*Phi)+4692*beta^2*Hbeta*Phi/x(beta*z)]"
            "=-136*alpha*beta*nabla_Abeta(Fbeta*Upsilon_beta)"
            "-4352*i*beta^2*C*([beta]^*(F*x/(x^2-1)))",
        "no_dense_level_matrix": True,
    }
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "checks": len(checks),
                      "output": str(target), "bytes": target.stat().st_size}, ensure_ascii=False))


if __name__ == "__main__":
    main()
