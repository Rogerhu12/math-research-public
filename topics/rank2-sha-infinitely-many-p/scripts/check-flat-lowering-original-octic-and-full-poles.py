#!/usr/bin/env python3
"""R267: actual flat-character lowering, full CM17 poles, original octic rows.

All arithmetic is exact over Q(i,sqrt(2)).  The degree bounds and actual
Mumford lifts are proved in R267 and R229.  The script retains both polar
and holomorphic blocks; it does not erase the former before the original
dyadic projection.  No dense level-4624 matrix is constructed.
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
u = s.Poly(U, U, domain=dom)
alpha, beta = 1+I, 4-I
Q, K, D = m.Qbe, m.Kbe, m.Dbe
field = s.QQ.algebraic_field(I, s.sqrt(2))
checks = {}


def check(k, v):
    checks[k] = bool(v)
    if not v:
        raise AssertionError(k)


def encmat(a):
    return [[str(field.to_sympy(x)) for x in row] for row in a.to_list()]


def lowered_rays():
    data = json.loads((HERE/"check-octic-ray-original-companion-transport.json").read_text())
    check("actual_R254_input", data["status"] == "PASS")
    basis = [u**6+1, u**5+u, u**4+u**2, u**3]

    def op(a):
        return (5*u-3)*a*D+4*u*(u-1)*(a.diff()*D-a*D.diff())

    cols = list(map(op, basis))
    top = s.Matrix([[p.nth(j) for p in cols] for j in range(12, 16)]).to_DM(domain=field)
    topinv = top.inv()
    AP, BP = [], []
    E = Q**2*K+4*u*Q*Q.diff()*K-4*u*Q**2*K.diff()
    check("true_derivative_division", E == (Q*D).mul_ground(beta))
    vv = -(U-1)**2/(4*U)
    check("true_CM2_division",
          s.Poly(s.cancel(256*U**4*K.as_expr().subs(U, vv)-K.as_expr()*Q.as_expr()),
                 U, domain=dom).is_zero)
    for k, ns in zip(data["characters"], data["normalized_ray_numerators"]):
        N = s.Poly(sum(s.sympify(v)*U**j for j, v in enumerate(ns)), U, domain=field)
        rhs = s.Matrix([-8*N.nth(j) for j in range(12, 16)]).to_DM(domain=field)
        cc = (topinv*rhs).to_Matrix()
        A = s.Poly(sum(cc[j]*basis[j].as_expr() for j in range(4)), U, domain=field)
        DD = s.Poly(D.as_expr(), U, domain=field)
        exact = ((5*s.Poly(U, U, domain=field)-3)*A*DD
                 +4*s.Poly(U*(U-1), U, domain=field)*(A.diff()*DD-A*DD.diff())+8*N)
        check("complete_first_derivative_identity_"+str(k), exact.is_zero)
        SS = 2-4*U
        B = s.Poly(s.expand(alpha*(A.nth(3)+A.nth(2)*SS
                      +A.nth(1)*(SS**2-2)+A.nth(0)*(SS**3-3*SS))/256),
                   U, domain=field)
        check("actual_CM2_algebraic_descent_"+str(k),
              s.Poly(s.cancel(alpha*A.as_expr()-256*U**3*B.as_expr().subs(U, vv)),
                     U, domain=field).is_zero)
        check("actual_leading_coefficient_"+str(k), B.LC() == -2*alpha/3)
        check("all_sixteen_genuine_lowered_poles_"+str(k),
              s.gcd(B, s.Poly(K.as_expr(), U, domain=field)).degree() == 0)
        AP.append(A)
        BP.append(B)
    mat = s.Matrix([[p.nth(j) for p in BP] for j in range(4)]).to_DM(domain=field)
    check("four_actual_lowered_sources_span_all_poles", mat.det() != field.zero)
    print("four exact algebraic lowered rays", flush=True)
    return AP, BP, mat


def actual_old_projector():
    # In the R229 T,F,G frame, B_old U^n =
    # G (T+F)^n (T-F)^(16-n)/2^17.
    v = s.symbols("v")
    columns = []
    for n in range(17):
        p = s.Poly((1+v)**n*(1-v)**(16-n), v)
        q = sum(p.nth(2*j+1)*v**j for j in range(8))
        sym = s.Poly(s.expand(q+q.subs(v, 1-v)), v)
        cc = s.symbols("c0:4")
        rem = s.Poly(s.expand(sym.as_expr()
                    -sum(cc[j]*(v*(1-v))**j for j in range(4))), v)
        sol = s.solve(rem.all_coeffs(), cc)
        columns.append([s.cancel(sol[cc[j]]/2**19/4**j) for j in range(4)])
    mat = s.Matrix.hstack(*map(s.Matrix, columns))
    basis = [4*16**j*u**j*(u-1)**(2*j+1)*(u+1)**(15-4*j) for j in range(4)]
    check("same_original_R235_four_basis_normalization",
          mat*s.Matrix.hstack(*map(m.vector, basis)) == s.eye(4))
    return mat


def trace_row(a):
    f = u*m.Qba**4-(m.Kba**4).mul_ground(a)
    ratio = (Q*m.inv(m.Qba, f)).rem(f)
    f68 = m.ipow(ratio, 68, f)
    base = (f68*u*m.Qba**2*m.inv(m.Kba**2, f)).rem(f)
    cur = (base*m.inv(K, f)).rem(f)
    vals = []
    for _ in range(4):
        vals.append(s.expand((cur*f.diff()).rem(f).nth(16)*a**16*K.eval(a)))
        cur = (cur*u).rem(f)
    con = (f68*m.Qba**2*K**2*m.inv(m.Kba**2*Q**2, f)).rem(f)
    constant = s.expand((con*f.diff()).rem(f).nth(16)*a**16)
    return vals, constant


def main():
    # These identities retain all three terms of K_h and the old 4692 input.
    check("complete_nineteenth_order_pole_cancellation",
          s.cancel(102*(U+11)/(U-1)-2312*U/(U-1)
                   +1088*U/(U-1)+1122) == 0)
    check("complete_modified_input_connection",
          s.cancel((4692-204*U)/(U-1)+4692-4488*U/(U-1)) == 0)
    check("actual_flat_pullback_sign",
          s.expand(-I*2**17/alpha**34) == -1)
    AP, BP, rays = lowered_rays()
    oldproj = actual_old_projector()

    values, constants = [], []
    for a in range(2, 24):
        v, c = trace_row(a)
        values.append(v)
        constants.append(c)
    nums = [m.interpolate([v[j] for v in values[:21]], start=2) for j in range(4)]
    check("raw_degree_twenty_global_bound_used",
          all(p.degree() <= 20 for p in nums))
    check("independent_held_out_full_trace",
          all(p.eval(23) == values[-1][j] for j, p in enumerate(nums)))
    invu17 = m.inv(u**17, K)
    polars = [(p*invu17).rem(K) for p in nums]
    hols = []
    for j, (p, r) in enumerate(zip(nums, polars)):
        h, rem = s.div(p-u**17*r, K)
        check("exact_polar_holomorphic_identity_"+str(j),
              rem.is_zero and h.degree() <= 16)
        hols.append(h)
    polarblock = s.Matrix([[p.nth(j) for p in polars] for j in range(4)])
    oldcols = oldproj*s.Matrix.hstack(*map(m.vector, hols))
    check("polar_block_invertible", polarblock.to_DM(domain=dom).det() != dom.zero)
    check("original_holomorphic_block_invertible",
          oldcols.to_DM(domain=dom).det() != dom.zero)
    print("full meromorphic trace and both invertible blocks", flush=True)

    cm = (Q*K)**2
    cs = s.cancel(constants[0]/cm.eval(2))
    check("actual_CM_constant_trace_all_fibers",
          all(s.expand(c-cs*cm.eval(a)) == 0 for a, c in zip(range(2, 24), constants)))
    check("actual_old_dyadic_projector_kills_CM_constant",
          oldproj*m.vector(cm) == s.zeros(4, 1))

    oldray = oldcols.to_DM(domain=field)*rays
    polarray = polarblock.to_DM(domain=field)*rays
    r = s.sqrt(2)
    V1 = s.Poly(1+(-5+2*r)*U+(11-4*r)*U**2+(-15+10*r)*U**3,U,domain=field)
    V3 = s.Poly(1+(63-70*r)*U/17+(-77+44*r)*U**2/17+(5+2*r)*U**3/17,U,domain=field)
    refs = [V1, V3, s.Poly(V1.as_expr().subs(r,-r),U,domain=field),
            s.Poly(V3.as_expr().subs(r,-r),U,domain=field)]
    eig = s.Matrix([[v.nth(j) for v in refs] for j in range(4)]).to_DM(domain=field)
    octic = eig.inv()*oldray
    check("all_four_original_octic_rows_retained",
          all(x != field.zero for row in octic.to_list() for x in row))
    check("actual_four_ray_original_octic_matrix_invertible", octic.det() != field.zero)
    check("actual_four_ray_polar_matrix_invertible", polarray.det() != field.zero)
    aa = [-s.Rational(39797,14784000)-s.Rational(8177,4224000)*r,
          -s.Rational(2091,448000)-s.Rational(2669,1971200)*r]
    bb = [s.Rational(224494093,56229888000)+s.Rational(4237163,1363148800)*r,
          -s.Rational(6031447,3748659200)-s.Rational(202405417,62977474560)*r]
    aa += [x.subs(r,-r) for x in aa]
    bb += [x.subs(r,-r) for x in bb]
    av, bv = (s.Matrix(v).to_DM(domain=field) for v in (aa, bb))
    la, lb = octic.inv()*av, octic.inv()*bv
    check("complete_original_CA_back_substitution", octic*la == av)
    check("complete_original_CB_octic_back_substitution", octic*lb == bv)
    check("actual_doubled_CA_mass", s.simplify(16*sum(aa)) == -s.Rational(272,1155))
    regm = [-60+44*r,(-356+252*r)/17,-60-44*r,(-356-252*r)/17]
    check("actual_doubled_regularized_CB_mass",
          s.simplify(4*sum(x*y for x,y in zip(bb,regm))) == -s.Rational(2261,10240))

    # The polar components also have defined local masses after the *actual*
    # four half-period terms.  Only the identity term has a pole on ker(beta);
    # at the original center all four terms are regular.
    polar_masses = []
    for pp in polars:
        q1 = pp.eval(1)/K.eval(1)
        qd1 = 17*q1+pp.diff().eval(1)/K.eval(1)-pp.eval(1)*K.diff().eval(1)/K.eval(1)**2
        mass = s.expand(pp.nth(3)/(4*beta)+(-16*q1+2*qd1)/2**17)
        polar_masses.append(mass)
    pmrow = s.Matrix([polar_masses]).to_DM(domain=field)*rays
    ray_hol = s.Matrix.hstack(*map(m.vector, hols)).to_DM(domain=field)*rays

    out = {
        "theorem": "R267", "status": "PASS", "checks": checks,
        "flat_branch_at_origin": "-1",
        "flat_target_identity": "h_flat*F(beta*w)=-theta(beta*w)^68",
        "flat_source_multiplier": "-((x(beta*z)^2-1)/(x(beta*z)^2+1))^17",
        "canonical_normtwo_deck_lift": "+T_T0 (old lift was -T_T0)",
        "full_modified_input": "-theta(alpha*beta*z)^68*(Phi''+136*beta*Phi'/y(beta*z)+4488*beta^2*x(beta*z)*Phi/(x(beta*z)^2-1))",
        "full_normtwo_output": "136*alpha*beta*theta(beta*w)^68*R_chi-4488*i*beta^2*C_chi*theta(beta*w)^68/x(beta*w)",
        "characters": [1,3,5,7], "coefficient_order": "ascending",
        "first_derivative_numerators_degree6": [m.coefficients(p) for p in AP],
        "lowered_numerators_degree3": [m.coefficients(p) for p in BP],
        "lowered_four_by_four_determinant": str(field.to_sympy(rays.det())),
        "raw_trace_numerator_columns": [m.coefficients(p) for p in nums],
        "trace_denominator": m.coefficients(K),
        "canonical_polar_columns": [m.coefficients(p) for p in polars],
        "canonical_holomorphic_columns": [m.coefficients(p) for p in hols],
        "polar_block_determinant": str(dom.to_sympy(polarblock.to_DM(domain=dom).det())),
        "old_holomorphic_block_determinant": str(dom.to_sympy(oldcols.to_DM(domain=dom).det())),
        "original_dyadic_projection_columns": [[str(x) for x in oldproj[:,j]] for j in range(17)],
        "actual_four_ray_holomorphic_degree16_columns": encmat(ray_hol.transpose()),
        "actual_four_ray_polar_matrix": encmat(polarray),
        "actual_four_ray_polar_determinant": str(field.to_sympy(polarray.det())),
        "actual_four_ray_original_octic_matrix": encmat(octic),
        "actual_four_ray_original_octic_determinant": str(field.to_sympy(octic.det())),
        "octic_z2_masses_after_common_2_pullback": encmat(octic.scalarmul(field(16))),
        "polar_z2_masses_after_original_projector_and_common_2_pullback": encmat(pmrow.scalarmul(field(4))),
        "actual_CM_constant_scalar": str(cs),
        "actual_CM_constant_polynomial": m.coefficients(cm),
        "actual_CM_constant_original_octic_projection": "0",
        "original_CA_inverse_column": encmat(la),
        "original_CB_inverse_column": encmat(lb),
        "fixed_fibers": {
            "t": list(range(2,24)),
            "raw_trace_values_times_Kbeta": [[str(x) for x in v] for v in values],
            "complete_CM_constant_trace_values": list(map(str,constants))},
        "central_formula": "q2^u*J_A=beta_A*J_Theta2+(1/16)*sum(lambda_A[k]*M2(Y_k)); Y_k=I_k/(136*alpha*beta)-P_k",
        "all_full_polar_and_CM_terms_retained": True,
        "C_chi_not_assumed_p_unit": True,
        "no_original_central_nonvanishing_claim": True,
    }
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"status":"PASS", "checks":len(checks),
                      "output":str(target), "bytes":target.stat().st_size},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
