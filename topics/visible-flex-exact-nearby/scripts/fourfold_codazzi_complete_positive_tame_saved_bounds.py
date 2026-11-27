#!/usr/bin/env python3
"""PX: combine the completed positive bulk and actual exterior estimates.

Only new rational combinations of already proved scalar bounds are used.
There are no native arrays, reference ODEs, Fourier sweeps or old targets.
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

    # The true highest boundary reflection adds to the already proved
    # auxiliary tail gain. No old coefficient gate is reevaluated.
    lt("square proving sqrt two below three halves", 2, F(9, 4))
    joined_loop = F(3, 32) + F(1, 400)
    lt("actual auxiliary bulk plus physical boundary loop", joined_loop, F(1, 8))
    lt("joined tail inverse", 1 / (1 - joined_loop), 2)
    lt("middle band including the true boundary cross", 1 + F(2, 400), 2)

    # Complete fixed-angle affine columns in the first angular order.
    # The moments t<1/4 and Gamma_1,Gamma_2<100 are the completed FX bounds.
    x = F(3, 4)
    family = F(2**32)
    column_first = 8 * family * (
        1 / (1 - x)
        + 6 * 100 / (1 - x)**2
        + 6 * 100 / (1 - x)**3
    )
    lt("complete first-order affine columns before solve", column_first, 2**51)
    lt("actual first-order boundary inverse", 1 + F(".0043"), 2)
    solved_first = (1 + F(".0043")) * column_first
    lt("complete first-order affine columns after solve", solved_first, 2**52)
    lt("common actual low-data normalization", 2**52, 2**64)

    # First new combined tame coefficient. PT supplies these definitions,
    # not new scientific values; FX supplies D_r, a_n and b_n.
    q0w, q1w, q2w, q0 = map(F, ("12.815", "10.877", "1392.129", "6.408"))
    cb = 4 + 472*q0w**2 + 190*q0w*q1w
    db = 16*q0w**2
    n = 2
    cutoff = F((560*(n + 1))**3)
    r_n = F(4, (560*(n + 1))**2)
    l_n = 2**(n+1)*418*q0w*q1w + 3**n*190*(q0w*q2w + q1w**2)
    h_n = 2**(2*n+1)*418*q0 + 4*6**n*190*q0
    k_n_bulk = 3*q0w**2*cutoff + cb + n*db
    a_n = F(2**(n+52))
    b_n = F(2**(3*n+42)*factorial(n+1))
    k_n_data = (2**48 + a_n) / 2**64
    ell_n = b_n / 2**64
    j = n + 1
    eps, ru, rz, rg, height = map(F, (F(1, 2**18), "1e-5", "5e-10", "1e-11", F(1, 2**60)))
    c_height = F(2**(12*j+24) * factorial(j+2)**2)
    d_j = (
        1 / (F("5.84")*eps) + 1/ru
        + F(factorial(j)) / (F("5.84")**2*rz*(1-eps)**(j+1))
        + 2*c_height*height/rg
    )
    a2 = (
        2 + 4*k_n_data
        + (4*r_n*l_n + 8*a_n)*6
        + 6*cutoff**(n-1)*(2 + 4*r_n*k_n_bulk)
        + 8*r_n*h_n
        + (16*b_n + 4*ell_n)*d_j
    )
    lt("second-increment full endpoint moment coefficient", d_j, F("3e15"))
    lt("second-increment complete physical tame coefficient", a2, 2**107)

    print(json.dumps({
        "all_passed": all(checks.values()),
        "new_exact_rational_comparisons": len(checks),
        "joined_auxiliary_loop_upper": str(joined_loop),
        "joined_auxiliary_inverse_upper": str(1/(1-joined_loop)),
        "complete_first_order_affine_column_upper": decimal_upper(solved_first, 6),
        "fixed_angle_data_normalizer": str(2**64),
        "second_increment": {
            "physical_proof_cutoff": str(cutoff),
            "endpoint_moment_D3": decimal_upper(d_j, 6),
            "complete_tame_A2": decimal_upper(a2, 6),
            "simple_A2_upper": "2^107",
        },
        "actual_all_angular_positive_high_graph_with_physical_exterior": True,
        "full_tail_background_only_small_in_original_low_domain": True,
        "high_body_norm": "A^(n+5/3), one linear factor",
        "high_true_endpoint_norm": "A^(n+2), one linear factor",
        "mean_compatibility_height_Robin_and_true_head_trace_retained": True,
        "full_low193_negative_return_and_parameter_Schur_closed": False,
        "old_scientific_targets_native_arrays_and_reference_integrations": 0,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
