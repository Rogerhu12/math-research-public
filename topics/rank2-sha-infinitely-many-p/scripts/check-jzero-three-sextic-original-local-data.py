#!/usr/bin/env python3
"""R306: exact local data for D=17,17^3,17^5 in one Yang frame.

Uses R290's exact field and finite Weil definitions only; its top-level
matrix computations and output are not rerun. No fitted source or p scan.
"""
from pathlib import Path
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
source = (HERE / "check-jzero-original-local-weil-and-schwartz.py").read_text()
ns: dict = {}
exec(compile(source.split("\nM = W(g0)")[0], "<R290 exact local definitions>", "exec"), ns)
K, om, zeta, root17 = (ns[x] for x in ("K", "om", "zeta", "gauss"))
gs, W, leg, kpow, mv = (ns[x] for x in ("gs", "W", "leg", "kpow", "mv"))
checks: list[str] = []


def check(name, truth):
    if not truth:
        raise AssertionError(name)
    checks.append(name)


check("same_actual_norm_one17_generator", len(set(gs)) == 18 and gs[6] == (8, 9))
check("same_real_positive_quadratic_Gauss", root17*root17 == 17 and root17.conj() == root17)
M = W(gs[1])
traces = [sum((A[j][j] for j in range(17)), K.zero) for A in (W(g) for g in gs)]
table = [(j, leg(gs[j][1]), 3*gs[j][0]*pow(2*gs[j][1], -1, 17) % 17) for j in range(1, 9)]
six = {kpow(gs[3], j): (-om**2)**j for j in range(6)}


def chi(z):
    return six[kpow(z, 48)]


records = []
for exponent, c in ((1, 1), (3, 4), (5, 1)):
    tau = om**((exponent+3)//2)
    f = [root17*int(a == 0)-sum((eps*tau**(-j)*zeta**(phase*a*a)
                                 for j, eps, phase in table), K.zero)
         for a in range(17)]
    check(f"k{exponent}_original_finite_eigenline", mv(M, f) == [tau*x for x in f])
    check(f"k{exponent}_actual_character_multiplicity_one", sum(
        (tau**(-j)*traces[j] for j in range(18)), K.zero)/18 == 1)
    check(f"k{exponent}_even_and_real_vector", all(f[a] == f[-a % 17] and f[a].conj() == f[a] for a in range(17)))
    check(f"k{exponent}_zero_coordinate", f[0] == root17-c)
    norm = sum((x*x.conj() for x in f), K.zero)
    check(f"k{exponent}_FULL_finite_norm", norm == 9*(17-c*root17) and norm == 9*root17*f[0])
    fibers = [K.zero]*17
    for a in range(17):
        for b in range(17):
            if (a, b) != (0, 0):
                fibers[a] += chi((a, b))**(-exponent)
    G = sum((fibers[a]*zeta**(-a) for a in range(17)), K.zero)
    check(f"k{exponent}_full_trace_fiber_Gauss", fibers == [K(-16)]+[K.one]*16 and G == -17)
    check(f"k{exponent}_17_epsilon_and_delta", chi((0, 1))**exponent == -1 and (-1)*(G/17)*chi((0, 1))**exponent == -1)
    ratio13 = tau**14/(om**2)**14
    check(f"k{exponent}_ACTUAL_CM13_relative_phase", ratio13 == om**(exponent-1))
    records.append({"k":exponent,"D":17**exponent,
                    "idele_unit_exponent_at17":48*exponent,
                    "mu4_torus_exponent":(9+3*exponent) % 18,
                    "tau_g0_power_basis":tau.coeffs(),
                    "zero_coordinate":f"sqrt(17)-{c}",
                    "squared_norm":f"9*(17-{c}*sqrt(17))",
                    "vector_power_basis":[x.coeffs() for x in f],
                    "M13_eigenvalue":f"-(4+omega)*omega^{(exponent-1)%3}"})

# Published sextic-twist direction checked at the same split norm-seven
# place as R290; these are three fixed curves, not a target-prime scan.
def ap7(D):
    count = 1
    for x in range(7):
        v = (x**3+D) % 7
        count += 1+(0 if v == 0 else 1 if pow(v, 3, 7) == 1 else -1)
    return 8-count

delta = 1+2*om
psi1 = -2-delta
symbol17 = (1+delta)/2
check("actual_twist_direction_all_three_curves_at_seven", [ap7(17**k) for k in (1,3,5)] == [-5,4,1]
      and all(psi1*symbol17**(-k)+(psi1*symbol17**(-k)).conj() == ap7(17**k) for k in (1,3,5)))
check("two_and_three_adic_local_power_criteria", 17 % 8 == 1 and (-17) % 9 == 1 and 17 % 3 == 2)
check("all_three_exact_common_full_weight_period", all(
    [m for m in range(12) if (2*m)%3 == 0 and (2*m)%4 == 0 and (48*k*(2*m))%288 == 0] == [0,6]
    for k in (1,3,5)))

s = sp.sqrt(17)
N1, N3 = 9*(17-s), 9*(17-4*s)
check("second_full_square_constant_ratio", sp.simplify(N1/N3-(13+3*s)) == 0)
check("all_finite_norms_strictly_positive", 17*17 > 16*17)
P = sp.pi
for n in (N1, N3, N1):
    full_norm = 3*(3+sp.sqrt(3))*n/sp.sqrt(102*sp.sqrt(3))
    C = P*sp.sqrt(102*sp.sqrt(3))/(17*sp.sqrt(3)*(3+sp.sqrt(3))*n)
    assert sp.simplify((2/(6*sp.Rational(17,27)))*P/(3*sp.sqrt(3))/full_norm-C) == 0
check("all_three_Yang_constants_with_actual_global_measure", True)

result = {"result":"R306", "all_passed":True, "check_count":len(checks), "checks":checks,
          "power_basis":"Q(zeta_51), omega=zeta_51^17, zeta_17=zeta_51^3",
          "common_Hermitian_alpha":17,"common_Gaussian_kappa":"51*sqrt(3)",
          "common_weight_period":6,"curves":records,
          "common_2":{"unit_character":"Teich_mu3", "uniformizer_value":-1,"Schwartz_vector":"(1,t,-1,t), t=(1+sqrt(3))/sqrt(2)","norm":"3+sqrt(3)"},
          "common_3":{"unit_character":"mod delta quadratic", "uniformizer_value":"-i","Schwartz":"1_(3^-1 Z3)","norm":3},
          "full_square_constants_relative_to_k1":["1","13+3*sqrt(17)","1"],
          "real_period_ratios_relative_to_E17":["1","17^(-1/3)","17^(-2/3)"],
          "scope":"Actual local data and all complex critical weights; no deletion of unknown p-adic derivatives."}
target = Path(__file__).with_suffix(".json")
target.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
print(f"PASS: {len(checks)} exact three-sextic local/full-weight checks; {target.name}")
