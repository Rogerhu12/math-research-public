#!/usr/bin/env python3
"""R488 exact certificate: fixed mod29 refinement, odd quarter phases,
original shared-A coordinates, and the actual even-depth/W D8 matrices.
The source identities themselves are proved with canonical lifts in R488.
"""
from pathlib import Path
from math import gcd
import json
import sympy as s

BASE = Path(__file__).resolve().parents[1]


def mul(x, y, modulus):
    a, b = x
    c, d = y
    return ((a*c-b*d) % modulus, (a*d+b*c-b*d) % modulus)


def ratio(a, b, modulus):
    norm = (a*a-a*b+b*b) % modulus
    ni = pow(norm, -1, modulus)
    return ((a*a-b*b)*ni % modulus, (2*a*b-b*b)*ni % modulus)


def main():
    old = 2793510720
    a0, b0 = 1428552127, 2161889730
    ca = ((2-a0)*pow(old, -1, 29)) % 29
    cb = (-b0*pow(old, -1, 29)) % 29
    a, b, modulus = a0+old*ca, b0+old*cb, old*29
    assert (a, b, modulus) == (23776637887, 77586679170, 81011810880)
    assert (a % old, b % old) == (a0, b0)
    assert (a % 29, b % 29) == (2, 0)
    norm = (a*a-a*b+b*b) % modulus
    assert norm == 60309924679 and gcd(norm, modulus) == 1
    assert norm % 64 == 7
    expected_ratios = {58: (1, 0), 32: (27, 8), 928: (59, 232), 36: (19, 0)}
    for level, expected in expected_ratios.items():
        assert ratio(a, b, level) == expected
    assert mul(mul((59, 232), (59, 232), 928),
               mul((59, 232), (59, 232), 928), 928) == (465, 0)

    MC = s.Matrix([[1,1,1,1],[4,-1,0,0],[7,7,-15,0],[7,7,7,-22]])
    DC = s.diag(3,12,7,7)
    assert MC.det() == -3190
    assert MC*DC*MC.T == s.diag(29,60,2310,4466)
    assert MC.inv()[:,0] == s.Matrix([s.Rational(3,29),s.Rational(12,29),
                                      s.Rational(7,29),s.Rational(7,29)])
    anchor = s.Matrix([[2,5],[-5,2]])
    assert anchor.det() == 29 and anchor*anchor.T == 29*s.eye(2)

    # Canonical odd quarter phase, N=29 and N=1 have the same class mod4.
    # epsilon=i^(3*Norm(m+n*omega)).  Its argument lies in Z/4, not a chosen sign.
    phases = []
    for m in range(4):
        for n in range(4):
            q = m*m-m*n+n*n
            vm, vn = 7*m-2*n, 2*m+5*n
            E = m*vn-n*vm
            assert E == 2*q
            chi_exponent = (vm+vn+vm*vn) % 2
            assert chi_exponent == q % 2
            eps = 3*q % 4
            for N in (1,29):
                # exp(pi*i*N*E/4)*chi(v) = i^(N*q+2*chi_exponent).
                assert (N*q+2*chi_exponent) % 4 == eps
            mt, nt = 3*m-6*n, 6*m-3*n  # multiplication by 3*delta=3+6omega
            assert (3*(mt*mt-mt*nt+nt*nt)) % 4 == (-eps) % 4
            assert (2*eps) % 4 == (0 if m % 2 == n % 2 == 0 else 2)
            assert (3*((-m)**2-(-m)*(-n)+(-n)**2)) % 4 == eps
            phases.append({"m":m,"n":n,"norm_mod4":q%4,"epsilon_power_of_i":eps,
                           "epsilon_square":1 if m%2==n%2==0 else -1})

    # Flat twists in all three doubled old Y coordinates vanish exactly.
    # delta=1+2omega; list the coefficient of t as a pair in Z[omega].
    flat = {}
    for sign in (1,-1):
        vals = [(58*sign+22,12),(58*sign-174,-348),(58*sign-114,12)]
        assert all(c % 4 == d % 4 == 0 for c,d in vals)
        flat[str(sign)] = [[c,d] for c,d in vals]
    assert flat["1"] == [[80,12],[-116,-348],[-56,12]]
    assert flat["-1"] == [[-36,12],[-232,-348],[-172,12]]

    # R465 (27), the full h=-1 half-period term, followed by its three
    # actual mu3 translates.  Only x exponents congruent to 2 survive.
    x = s.symbols("x")
    X = x**3
    half_poly = ((X+1)*(x+1)**2*(x-2)**2
                 * (-(x-2)**3-8*(x+1)**3)
                 * (7*(x-2)**6+4*(x-2)**3*(x+1)**3+16*(x+1)**6))
    half_principal = s.expand(sum(coef*x**power[0]
                                  for power,coef in s.Poly(half_poly,x).terms()
                                  if power[0] % 3 == 2))
    half_target = -729*x**2*(X+1)*(X-8)*(7*X**2-4*X+16)
    assert s.expand(half_principal-half_target) == 0

    W = s.Matrix([[0,1,-1],[1,0,-1],[0,0,-1]])
    R = s.Matrix([[1,0,0],[0,0,1],[0,1,0]])
    assert W**2 == R**2 == s.eye(3)
    assert (W*R)**4 == s.eye(3) and (W*R)**2 != s.eye(3)
    seen = {tuple(s.eye(3))}
    todo = [s.eye(3)]
    while todo:
        x = todo.pop()
        for g in (W,R):
            y = g*x
            if tuple(y) not in seen:
                seen.add(tuple(y))
                todo.append(y)
    assert len(seen) == 8
    u = s.Matrix([1,s.Rational(1,2),s.Rational(1,2)])
    v = s.Matrix([0,s.Rational(1,2),s.Rational(-1,2)])
    h = s.Matrix([0,1,1])
    assert W*u == v and W*v == u and R*u == u and R*v == -v
    assert W*h == -h and R*h == h

    k = s.symbols("k")
    PA = s.Matrix([[k**2,0],[k**2-1,1]])
    PW = s.Matrix([[1,s.Rational(29,72)*(k-1)],[0,k]])
    assert PA.det() == k**2 and PW.det() == k
    assert (PA*PW).det().factor() == k**3
    delta = s.I*s.sqrt(3)
    CD = s.Matrix([[3*delta,4],[4,3*delta]])
    assert s.simplify(CD.det()) == -43
    assert s.simplify(CD*CD.conjugate().T) == 43*s.eye(2)
    A,Wvar,D = s.symbols("A W D")
    c,d0 = CD.inv()*s.Matrix([Wvar-A,D])
    Ys = s.expand(A+c+2*d0)
    target = ((35+3*delta)*A+(8-3*delta)*Wvar+(4-6*delta)*D)/43
    assert s.simplify(Ys-target) == 0

    report = {
        "old_ray":[a0,b0,old],"new_ray":[a,b,modulus],
        "CRT_corrections":[ca,cb],"norm_residue":norm,
        "whole_core_ratios":{str(n):list(v) for n,v in expected_ratios.items()},
        "odd29_absolute_core":"chi_29,p in {+1,-1}, fixed by the actual normalized trace",
        "C29_output_matrix":[[str(x) for x in MC.row(i)] for i in range(4)],
        "C29_inverse":[[str(x) for x in MC.inv().row(i)] for i in range(4)],
        "C29_Gram":[29,60,2310,4466],"C29_determinant":"-3190",
        "absolute_square_anchor":"sigma(2z-5t)*sigma(5z+2t), degree29 in both axes",
        "quarter_phase_table":phases,
        "old_Y_flat_coefficients_in_Zomega":flat,
        "core_A_four_states":"K_A rho_k=chi rho_(k+1), indices mod4",
        "core_c_four_states":"K_c rho_k=-rho_(k-1), indices mod4",
        "core_d_four_states":"K_d rho_k=-rho_k",
        "core_R_triple":"chi*lambda^3 on the simultaneous three-R deep block",
        "even_state_basis":"e0=rho0, e1=rho1, e2=-(1/4)sum_E4 T_t,W rho0",
        "W_core_matrix":[[int(x) for x in W.row(i)] for i in range(3)],
        "A_two_step_matrix":[[int(x) for x in R.row(i)] for i in range(3)],
        "actual_group_order":len(seen),
        "new_and_reference_first_Y_rows":[0,1,-1],
        "T_first_W_row":[1,1,-1],
        "nonzero_E2_complete_Phi_sum":"-84*delta*S",
        "h_complete_Y_marginal":"-(1+delta)*S(2z)/2",
        "u_complete_Y_marginal":"(3-delta)*S(2z)/4",
        "v_complete_Y_marginal":"Xi(2z)+(1+delta)*S(2z)/4",
        "h_complete_W_marginal":"0",
        "u_and_v_complete_W_marginal":"6*delta*T",
        "common_companion":"D=4c+3delta*d=(Q-3delta*U)/14; R1,R2,R3",
        "A_W_coordinate_determinant":"137170",
        "Y_s_in_A_W_D":"((35+3delta)A+(8-3delta)W+(4-6delta)D)/43",
        "physical_A_two_step":[[str(x) for x in PA.row(i)] for i in range(2)],
        "physical_W_step":[[str(x) for x in PW.row(i)] for i in range(2)],
        "cycle_lattice_identity":"rho|((P_A,2 P_W)^4 Zp^6)=lambda^12*((P_A,2 P_W)^4)_*rho",
        "boundary":"Odd A states need the double W cover; no W closure on those two states is asserted. A deep is not four individual sigma inputs deep."
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2)+"\n")
    print("R488 CRT, odd quarter phases, three-state D8, and exact original coordinates verified.")


if __name__ == "__main__":
    main()
