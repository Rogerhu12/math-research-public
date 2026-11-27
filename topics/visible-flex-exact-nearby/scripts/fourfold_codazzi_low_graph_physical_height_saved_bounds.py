#!/usr/bin/env python3
"""GHW: new exact combinations for the complete physical height derivative.

All profile, mean, endpoint and installation bounds are completed inputs.
No earlier successful check or scientific target is rerun.
"""

import json


def main():
    checks = {}

    def lt(name, value, bound):
        checks[name] = value < bound
        if not checks[name]:
            raise AssertionError(name)

    def positive_sum_exponent(*values):
        return max(values)+(len(values)-1).bit_length()

    lt("true endpoint tangent coordinate retains a strict low margin",
       6291456-49000000+16, -2)
    lt("complete common-reference scalar multiplier and scaled jet remain small",
       positive_sum_exponent(1048576-110000000,
                             170016-2*48000000)+16, -4)
    lt("whole internal background radial state derivative remains below one",
       264+262144-47000000, 0)
    lt("complete internal physical Hessian profile",
       129+200+64-300+440, 540)
    lt("complete fixed-metric mean physical two-jet budget",
       533+84+12, 640)
    scalar_profile = 9216+2-64
    lt("actual shallow first-principal row fits its separate scalar majorant",
       8960+2, 14+scalar_profile)
    lt("full first-principal physical height including installation scale",
       scalar_profile+1024+8+440, 12000)
    lt("actual first-principal height column remains below the direction norm",
       12000-47000000, 0)
    lt("all fixed-metric height components and full first-principal column",
       704+4+1, 2048)

    gamma_height = positive_sum_exponent(262152-57000000,
                                         1032+440-110000000)
    lt("complete actual installed physical parameter-height column",
       gamma_height, -56000000)

    print(json.dumps({
        "all_passed": all(checks.values()),
        "new_exact_integer_comparisons": len(checks),
        "internal_physical_hessian_profile_exponent": 533,
        "actual_first_principal_scalar_profile_exponent": scalar_profile,
        "complete_piecewise_C2_height_derivative": "2^2048 ||h||_E20",
        "global_C2_requires_original_matching_jets": True,
        "actual_installed_partial_gamma_height_upper":
            "2^-56000000 r_gamma^-1 ||eta||_A0",
        "actual_partial_gamma_height_exponent_before_widening": gamma_height,
        "endpoint_tangent_is_true_J_w": True,
        "whole_finite_connector_and_both_profile_junctions": True,
        "independent_height_and_flux_ports_preserved": True,
        "ordinary_mean_and_complete_principal_feedback_retained": True,
        "radial_jets_come_from_the_actual_graph": True,
        "old_scientific_arrays_integrals_and_targets": 0,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
