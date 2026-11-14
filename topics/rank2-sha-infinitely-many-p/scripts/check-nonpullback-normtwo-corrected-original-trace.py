#!/usr/bin/env python3
"""R261: actual non-pullback norm-two source, its pole, and full fixed correction.

Exact Q(i) arithmetic; the original trace has a degree-20 numerator over
K_beta. The corrected trace is a degree-16 polynomial. All fixed fibers
and all 16 actual CM5 eigenspace projections are retained.
"""
import importlib.util
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location(
    "r248", HERE/"check-ray17-conjugate-trace-and-yang-projection.py")
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
U, I, dom = m.U, s.I, s.QQ_I
uf = s.Poly(U, U, domain=dom)
beta = 4-I
Q, K, D = m.Qbe, m.Kbe, m.Dbe
checks = {}


def check(k, v):
    checks[k] = bool(v)
    if not v:
        raise AssertionError(k)


def exact_fiber(a, num, den):
    f = uf*m.Qba**4-(m.Kba**4).mul_ground(a)
    Lhat = (num*m.inv(den, f)).rem(f)
    Lcomp = (-1088*uf*K.diff()*m.inv((uf-1)*K, f)).rem(f)
    ratio = m.ipow((m.Pbe*m.inv(m.Pba, f)).rem(f), 17, f)
    mult = (ratio*uf*m.Qba**2*m.inv(m.Kba**2, f)).mul_ground(4*I).rem(f)
    th = s.expand((mult*Lhat*f.diff()).rem(f).nth(16)*a**8*(a-1)**8)
    tc = s.expand((mult*Lcomp*f.diff()).rem(f).nth(16)*a**8*(a-1)**8)
    return th, tc


def enc(v):
    return [str(s.expand(x)) for x in v]


def main():
    check("actual_sigma_theta_division",
          uf*Q**4-K**4 == (uf-1)*D**2)
    check("kernel_beta_poles_simple", s.gcd(K, K.diff()).degree() == 0)
    check("new_denominator_avoids_kernel_beta",
          s.gcd(K, (uf-1)*D).degree() == 0)
    num = ((12-260*uf)*D**2-544*uf*(uf-1)*D.diff()*D
           +(Q**2*K**2).mul_ground(s.expand(1088*beta**2)))
    den = (uf-1)**2*D**2

    # Verify the original complete h=B0 expression and the fixed pole correction.
    E_num = Q**2*K+4*uf*Q*Q.diff()*K-4*uf*Q**2*K.diff()
    cleared = (K*(12*(uf+1)*D**2
                  +(Q**2*K**2).mul_ground(s.expand(1088*beta**2)))
               -272*uf*Q**2*E_num
               -1088*uf*(uf-1)*K.diff()*D**2-K*num)
    check("complete_ker_beta_pole_correction", cleared.is_zero)
    print("exact pole correction checked", flush=True)

    # Exact degree bounds are proved geometrically in R261.
    # 17 values determine the corrected polynomial; 21 determine the raw
    # numerator. t=23 is held out from both determinations.
    hv, rv = [], []
    for a in range(2, 24):
        th, tc = exact_fiber(a, num, den)
        hv.append(th)
        rv.append(s.expand((th-tc)*K.eval(a)))
    Ph = m.interpolate(hv[:17], start=2)
    Pr = m.interpolate(rv[:21], start=2)
    check("corrected_degree_bound", Ph.degree() <= 16)
    check("original_meromorphic_numerator_bound", Pr.degree() <= 20)
    check("all_corrected_held_out_fibers",
          all(Ph.eval(a) == v for a, v in zip(range(2, 24), hv)))
    check("original_meromorphic_held_out_fiber",
          Pr.eval(23) == rv[-1])
    check("original_trace_has_all_sixteen_genuine_poles",
          s.gcd(Pr, K).degree() == 0)
    Pcomp = Ph*K-Pr

    d = json.loads((HERE/"check-third-adjacent-companion-lambda2.json").read_text())
    check("adjacent_input_certificate", d["status"] == "PASS")
    MM = s.Matrix(17, 17, lambda j, k:
                  s.sympify(d["CM5_adjacent_matrix_columns"][k][j]))
    ND = (MM/(2+I)).applyfunc(s.expand).to_DM(domain=dom)
    v = m.vector(Ph).to_DM(domain=dom)
    powers = [v]
    for j in range(16):
        powers.append(ND*powers[-1])
    check("normalized_normfive_period16", powers[-1] == v)
    vv = [x.to_Matrix() for x in powers[:16]]
    projections, quartic = [], []
    trivial = None
    for r in range(16):
        cs = [[s.Integer(0)]*4 for _ in range(17)]
        for j in range(16):
            e = (-r*j) % 16
            for n in range(17):
                cs[n][e % 4] += I**(e//4)*vv[j][n]/16
        cs = [[s.expand(c) for c in row] for row in cs]
        if r % 4 == 0:
            check("quartic_cyclotomic_reduction_"+str(r),
                  all(all(x == 0 for x in row[1:]) for row in cs))
            w = s.Matrix([row[0] for row in cs])
            if r:
                ref = s.Matrix(list(map(s.sympify,
                    d["normalized_adjacent_primitive_polynomials"][str(r//4)])))
                aa = s.simplify(w[16])
                check("actual_primitive_equality_"+str(r), w == aa*ref)
                quartic.append(aa)
            else:
                trivial = w
        projections.append({
            "r": r, "eigenvalue": "zeta16^%d" % r,
            "encoding": "[1,zeta16,zeta16^2,zeta16^3] over Q(i)",
            "polynomial_coefficients": [enc(row) for row in cs],
            "z2_coefficient": enc(cs[16]),
            "z2_coefficient_nonzero": any(x != 0 for x in cs[16])})
    cmrefs = [s.Matrix(list(map(s.sympify, d["CM_adjacent_polynomials"][q])))
              for q in ("beta", "barbeta")]
    cm = s.Matrix.hstack(*cmrefs).gauss_jordan_solve(trivial)[0]
    expected = (-s.Integer(309664940525)+459681214175*I)/2**23
    check("nonzero_actual_lambda2_coefficient", quartic[1] == expected)
    Bscalar = s.simplify(quartic[1]*128*I/5)
    check("complete_original_B_scalar",
          Bscalar == (-s.Integer(91936242835)-61932988105*I)/2**16)
    check("actual_constant_source_not_pure_beta",
          any(x != 0 for x in (m.vector(Ph)-trivial)))

    out = {
        "theorem": "R261", "status": "PASS", "checks": checks,
        "h": "1/(x(w)^2-1)",
        "division_polynomial_Kbeta": m.coefficients(K),
        "sigma_theta_identity": "U_beta-1=(U-1)*D_beta^2/K_beta^4",
        "original_Kh_has_genuine_kernel_beta_poles": True,
        "original_polar_residue_at_nonzero_T_in_kernel_beta":
            "-272*i*F_beta(T)*h_prime(T)",
        "added_actual_source": "272*i*F_beta*h_prime*dlog(K_beta(x(w)^2))",
        "added_actual_normtwo_input":
            "136*i*h_prime*dlog(K_beta(x(w)^2))*L0",
        "corrected_source_L_numerator": m.coefficients(num),
        "corrected_source_L_denominator": m.coefficients(den),
        "corrected_source_frame": "4*i*F(beta*w)*x(w)",
        "fixed_fibers": {
            "t": list(range(2, 24)),
            "corrected_values": enc(hv),
            "original_values_times_Kbeta": enc(rv)},
        "corrected_trace_polynomial": m.coefficients(Ph),
        "original_trace_numerator_degree20": m.coefficients(Pr),
        "original_trace_denominator": m.coefficients(K),
        "trace_of_full_pole_correction_numerator": m.coefficients(Pcomp),
        "trace_of_full_pole_correction_denominator": m.coefficients(K),
        "complete_trace_identity": "Ph = Pr/K_beta + Pcomp/K_beta",
        "all_sixteen_actual_projections": projections,
        "quartic_H1minus_H2minus_H3minus_coefficients": enc(quartic),
        "CM_beta_barbeta_coefficients": enc(cm),
        "lambda2_original_B_scalar_without_kappa4": str(Bscalar),
        "full_central_identity":
            "Omega_chi,h(u)+136*alpha*beta*Xi_chi,h(u)"
            "=-C_chi*kappa_B*q2^u*J34(u)",
        "C_chi_not_assumed_p_unit": True,
        "single_shift_full_transpose":
            "(d*u+1)*f(u)-d*u*f(u-1)-g(u)+J(error;u)",
        "no_original_central_nonvanishing_claim": True,
    }
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "checks": len(checks),
                     "output": str(target), "bytes": target.stat().st_size},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()

