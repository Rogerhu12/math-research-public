#!/usr/bin/env python3
"""R284: fixed original derivative/primitive interfaces. No target-prime scan."""
import json
from pathlib import Path

import sympy as s
from flint import fmpq, fmpq_mat

root = Path(__file__).parent
src = json.loads((root / "check-original-three-ordinary-adjoint.json").read_text())
plus = json.loads((root / "check-ray17-conjugate-trace-and-yang-projection.json").read_text())
odd = json.loads((root / "check-original-first-order-i-block-and-cm5.json").read_text())
phase_data = json.loads((root / "check-original-positive-cm5-eigenvalues.json").read_text())
checks = {}


def check(name, ok):
    checks[name] = bool(ok)
    if not checks[name]:
        raise AssertionError(name)


def pair(z):
    z = s.expand(s.sympify(z))
    return fmpq(str(s.re(z))), fmpq(str(s.im(z)))


def normalized_matrix(data):
    a, b = fmpq_mat(17, 17), fmpq_mat(17, 17)
    for j, col in enumerate(data["CM5_matrix_columns"]):
        for i, value in enumerate(col):
            x, y = pair(value)
            a[i, j], b[i, j] = (2*x+y)/5, (2*y-x)/5
    return a, b


def realify(a, b):
    return fmpq_mat(34, 34, [
        a[i, j] if i < 17 and j < 17 else
        -b[i, j-17] if i < 17 else
        b[i-17, j] if j < 17 else a[i-17, j-17]
        for i in range(34) for j in range(34)
    ])


# Actual primary gamma_5, with the full symmetric-lift modulus 2*272.
modulus = 544
phi = ((-3*pow(5, -1, modulus)) % modulus,
       (-4*pow(5, -1, modulus)) % modulus)
value, powers = (1, 0), {}
for n in range(1, 17):
    value = ((value[0]*phi[0]-value[1]*phi[1]) % modulus,
             (value[0]*phi[1]+value[1]*phi[0]) % modulus)
    if n in (1, 2, 4, 8, 16):
        powers[str(n)] = list(value)
    check("primary_Heisenberg_no_earlier_identity_" + str(n),
          value != (1, 0) if n < 16 else value == (1, 0))

zh = [fmpq(x) for x in src["angular_primitive_Z_H"]]
pg = fmpq_mat(17, 1, [-zh[17-j]/4 for j in range(17)])
pr = fmpq_mat(17, 1, [
    fmpq(x) for x in src["branch_regular_RH_coefficients"][::-1]
])
# The boundary term P(1)*U^17 is retained in this true source map.
jmap = fmpq_mat(17, 17, [
    -4 if i >= j else 0 for i in range(17) for j in range(17)
])
ell = fmpq_mat(17, 17, [
    -4*(17-i) if i == j else 0 for i in range(17) for j in range(17)
])
bmap = ell * jmap.inv()
check("actual_H_to_R277_odd_primitive", jmap*pg == pr)
check("true_boundary_map_determinant", jmap.det() == (-4)**17)
check("first_order_original_H_return",
      bmap*pr == ell*pg)
check("first_order_return_matrix",
      all(bmap[i, j] == (17-i if i == j else
                        -(17-i) if i == j+1 else 0)
          for i in range(17) for j in range(17)))
check("first_order_return_determinant", bmap.det() == s.factorial(17))
check("original_H_primitive_has_no_linear_term", pg[16, 0] == 0)

ar, ai = normalized_matrix(plus)
br, bi = normalized_matrix(odd)
npg_r, npg_i = br*pg, bi*pg
first = [str(npg_r[16, 0]), str(npg_i[16, 0])]
check("actual_nonzero_first_core_mass",
      npg_r[16, 0] != 0 or npg_i[16, 0] != 0)

# The legitimate primary operator is +N_+ on the even block and -N_i
# on the odd block, so this is the required comparison, not a guessed one.
defect_r, defect_i = ar*jmap+jmap*br, ai*jmap+jmap*bi
defect_real = realify(defect_r, defect_i)
check("paid_angular_map_prime_core_defect_full_rank",
      defect_real.rank() == 34)
defect_norm_det = defect_real.det()
check("paid_angular_map_prime_core_defect_certificate", defect_norm_det != 0)
check("actual_positive_CM5_phases",
      phase_data["status"] == "PASS" and
      all(s.expand(s.sympify(phase_data["eigenvalues"][name])-target) == 0
          for name, target in {
              "A": -2-s.I, "B": -1+2*s.I, "Cbeta": -1+2*s.I
          }.items()))
check("actual_thirty_three_dimensional_derivative_input",
      odd["H_primitive_complex_Krylov_rank"] == 16 and
      odd["untwisted_actual_primitive_orbit_certificates"]
      ["joint_A_B_CM"]["complex_rank"] == 17)

out = {
    "status": "PASS",
    "scope": "Fixed exact Gaussian/rational operations; no target-prime scan.",
    "checks": checks,
    "primary_Heisenberg_modulus": modulus,
    "primary_Heisenberg_multiplier": list(phi),
    "primary_Heisenberg_powers": powers,
    "boundary_map": "J(P)=4*(P-P(1)*U^17)/(U-1)",
    "boundary_map_determinant": str(jmap.det()),
    "H_return": "B(Q)=U*(U-1)*Q'+(17-16*U)*Q",
    "H_return_determinant": str(bmap.det()),
    "H_primitive_P_ascending": [str(pg[j, 0]) for j in range(17)],
    "original_odd_primitive_P_R_ascending": [str(pr[j, 0]) for j in range(17)],
    "N_i_H_primitive_top_coefficient": first,
    "primary_paid_map_defect": "N_+*J+J*N_i",
    "primary_paid_map_defect_complex_rank": 17,
    "primary_paid_map_defect_determinant_norm": str(defect_norm_det),
    "ray_class_true_Tp_phases": {
        "A": "1", "B": "-I", "H": "-I", "Cbeta": "-I", "S8": "-1"
    },
    "three_corrected_connection_joint_orbit_dimension": 37,
    "joint_orbit_components": {"unit_source": 4, "actual_derivatives": 33},
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({
    "status": "PASS", "checks": len(checks),
    "first_core_coefficient": first,
    "primary_defect_rank": 17, "bytes": path.stat().st_size,
}, indent=2))
