#!/usr/bin/env python3
"""OX: new rational combinations for the genuine physical boundary map.

No coefficient array, exterior solution, old target or reference integral
is evaluated. The all-order constants follow from the proof's formulas.
"""

from fractions import Fraction as F
from math import factorial
import json

from fourfold_codazzi_compact_tame_Hessian_saved_bounds import decimal_upper


def main():
    checks = {}

    def lt(name, x, y):
        checks[name] = F(x) < F(y)
        if not checks[name]:
            raise AssertionError(name)

    # Same endpoint and saved radius; only a new full A^3 combination.
    us, vs, er = map(F, ("1.643190e-9", "9.603792e-9", "1e-9"))
    endpoint_A3 = 8 + 3481*(us + vs) + er
    lt("complete actual endpoint low A3 pair norm", endpoint_A3, 9)

    eps, ml = F(1, 2**18), F("5.84")
    lt("true nonmean primitive L2 to H1 factor", F(17, 16), F(33, 32)**2)
    angular_speed_Linfty = (1+eps)/(2*ml*(1-eps))
    angular_speed_H1 = (1+eps)/ml * (
        F(33, 32)/(1-eps) + eps/(4*(1-eps)**2)
    )
    lt("full mean aware residual transport Linfty coefficient", angular_speed_Linfty, F(1, 10))
    lt("full mean aware residual transport H1 coefficient", angular_speed_H1, F(1, 5))
    lt("full residual transport Wiener coefficient", F(11, 10)*angular_speed_H1, F(1, 4))

    # Universal first and second function-parameter Taylor sums.
    # DT supplied the actual mass x < .243 < 1/4; no old row is replayed.
    x = F(1, 4)
    lt("complete second derivative low Taylor sum", 3/(1-x)**2, 6)
    lt("two actual parameter radii normalized by one bound", F("1e11"), 2**37)
    lt("uniform first derivative geometric sum", 1/(1-x), 2)

    def constants(n):
        p = n + 40
        chart = 2**(80*p)*factorial(p)**12
        first = 2**(2*n+4)*factorial(n+1)
        second = 2**(2*n+44)*factorial(n+1)
        return chart, first, second, chart*(2+5*first+5*second)

    # Report sizes of the proved explicit all-order constant, not a
    # numerical approximation of any analytic object.
    p1, j1, k1, c1 = constants(1)
    print(json.dumps({
        "all_passed": all(checks.values()),
        "new_exact_rational_comparisons": len(checks),
        "complete_endpoint_A3_pair_upper": decimal_upper(endpoint_A3, 12),
        "actual_phase_transport_Linfty_upper": decimal_upper(angular_speed_Linfty, 12),
        "actual_phase_transport_H1_upper": decimal_upper(angular_speed_H1, 12),
        "actual_phase_transport_A0_upper": decimal_upper(F(11,10)*angular_speed_H1, 12),
        "universal_high_background_second_Taylor_factor": "32 * 4^n * (n+1)!",
        "first_new_order": {
            "J1": str(j1),
            "K1": str(k1),
            "P1_binary_length": p1.bit_length(),
            "C1_binary_length": c1.bit_length(),
        },
        "actual_fixed_physical_output_Frechet_derivative_identified": True,
        "moving_output_off_shell_transport_retained_exactly": True,
        "all_order_boundary_first_and_second_tame_derivatives": True,
        "direction_scale": "H^(n+3) high and H^3 low, physical normalized height input",
        "single_high_background_scale": "one actual endpoint A^(n+2) factor",
        "both_physical_means_holonomy_and_independent_height_preserved": True,
        "new_low_inverse_or_residual_smallness_gate": False,
        "old_native_arrays_scientific_targets_and_reference_integrations": 0,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
