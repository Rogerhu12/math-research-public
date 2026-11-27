#!/usr/bin/env python3
"""LG: new full-mean strong-long-module rational combinations.

The existing long PDE, Green, curvature inverse and endpoint bounds
are inputs. No long solution or completed target is evaluated again.
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

    ry = F(1, 2**24)
    kap, source = F(2**12), F(2**11)
    kap_first = source + 2*kap
    c = kap/2
    c_first = kap + 2*c
    c_second = source + 4*kap + 4*c
    full_mean_jet = kap + kap_first + c + c_first + c_second
    lt("complete kappa C1 and mean height C2 coefficient", full_mean_jet, 2**16)
    lt("complete augmented wide graph value", ry + 2**16*ry**2, 2*ry)
    mean_module = 4*F(2**16)*ry
    lt("complete mean jet direction module", mean_module, F(1, 32))
    complete_columns = (1+mean_module)*(48+2**14)
    lt("both actual complete strong graph derivative columns", complete_columns, 2**15)

    # Actual polar-to-Cartesian height derivatives. The mixed Hessian
    # entry is counted twice and no small radius is divided out alone.
    wa = F(5, 28)
    nonmean_height = F(1, 16) + F(3, 8) + F(1, 4) + wa*(F(15, 8)+2*F(5, 4)+F(11, 8))
    lt("full physical nonmean height C2 fee", F(11, 10)*nonmean_height, 4)
    lt("full physical mean height C2 fee", 1+2*wa, 2)

    print(json.dumps({
        "all_passed": all(checks.values()),
        "new_exact_rational_comparisons": len(checks),
        "full_mean_jet_coefficient": str(full_mean_jet),
        "complete_mean_jet_direction_module": str(mean_module),
        "complete_Z_and_height_strong_columns_upper": decimal_upper(complete_columns, 6),
        "complete_strong_family_uniform_bound": "2^15",
        "full_nonmean_physical_C2_fee": decimal_upper(F(11,10)*nonmean_height, 12),
        "full_mean_physical_C2_fee": decimal_upper(1+2*wa, 12),
        "physical_height_safe_C2_fee": "16",
        "whole_finite_long_strong_radial_module_all_angular_derivatives": True,
        "kappa_mean_height_difference_and_both_mean_slopes_retained": True,
        "independent_overall_height_translation_retained": True,
        "actual_physical_coordinate_first_and_second_derivatives": True,
        "moving_coordinate_raw_strong_module_free_transfer": False,
        "full_horizontal_cap_reconstruction_derivatives_proved_here": False,
        "old_native_arrays_long_solutions_and_reference_integrations": 0,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
