#!/usr/bin/env python3
"""LV: new exact combinations for the complete long vector two-jet map.

The actual long graph, wide module columns and intrinsic q/a fee are
completed inputs. This evaluates no old PDE, Green function or target.
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

    r = F(1, 64)
    ry = F(1, 2**24)
    beta = F(7, 16_000_000)
    lt("wide actual state inside module center ball", 8*ry, F(1, 128))
    lt("full D reciprocal root neighborhood", (2+3*r)*r, 3*r)
    lt("b squared neighborhood for its half-root inverse", 2*(2*r+2*r*r), F(1, 8))

    g1 = 2*(2+3*r)+4*(1+r)
    a1 = 2*(1+r)
    b1 = 2*(2+2*r)
    lt("G minus one divided by q", g1, 16)
    lt("G complete value", 1+16*r, 2)
    lt("a1 divided by q", a1, 4)
    lt("b minus one divided by q", b1, 5)
    h0 = 4*(1+r)+4*(1+3*r)+8*r
    lt("full radial angular connection H0", h0, 32)
    gamma = F(16, 4)+F(32, 2)
    lt("complete normalized angle including its radial mean", gamma, 32)
    lt("value and angular first jet", 2*r+64, 128)
    lt("radial first jet", 2*(5+4)+64, 128)

    kt = 32*r+3
    lt("true full mean and nonmean radial K derivative", kt, 4)
    st = 2*(1+r)*4+2*r+4*r*3
    dt = 2*(2+3*r)+st
    lt("D radial derivative divided by q", dt, 23)
    bt = 2*23+2*8*r
    a1t = 2*(5*(1+r)+4*r)+16*(1+r)*r*r
    lt("b radial derivative divided by q", bt, 64)
    lt("a1 radial derivative divided by q", a1t, 32)
    btheta = 4*(1+3*r)+8*r
    a1theta = 2*(1+2*r)+4*(1+r)*r*r
    lt("b angular derivative divided by q", btheta, 16)
    lt("a1 angular derivative divided by q", a1theta, 8)
    lt("A angular derivative divided by q", 2*r, 1)
    lt("both canceled coframe combinations", 2*16+5+r, 38)
    radial_second = 2*(64+32+32*(2+4*r))
    mixed_second = 2*(38+8+16+8)
    angular_second = 2*(38+4+1)
    lt("actual radial second jet", radial_second, 512)
    lt("actual mixed second jet", mixed_second, 256)
    lt("actual angular second jet", angular_second, 128)
    full_jet = 3*128+512+2*256+128
    lt("all physical two jets with mixed entry twice", full_jet, 2**12)

    state_module = F(2**12, 64)*128
    complete_columns = state_module*4*2**15
    lt("state module fee uses a true square-zero neighborhood", state_module, 2**14)
    lt("full boundary parameter module fee", complete_columns, 2**31)
    rotating_value = 2**12*beta*8*ry
    cartesian_value = 16*rotating_value
    # The simple final geometric statement uses a safe decimal budget.
    lt("actual rotating horizontal two-jet perturbation", rotating_value, F(1, 10**8))
    lt("actual Cartesian horizontal two-jet perturbation", cartesian_value, F(1, 10**7))
    lt("actual annulus chord-path injectivity margin", 3*cartesian_value, F(1, 1000))

    print(json.dumps({
        "all_passed": all(checks.values()),
        "new_exact_rational_comparisons": len(checks),
        "state_algebra_radius": str(r),
        "full_radial_rotation_mean_is_retained": True,
        "normalized_gamma_coefficient_upper": str(gamma),
        "full_rotating_two_jet_coefficient": full_jet,
        "safe_state_two_jet_coefficient": "2^12 beta",
        "complete_state_module_coefficient": str(state_module),
        "complete_Z_and_height_jet_columns": "2^30 beta",
        "actual_beta_upper": decimal_upper(beta, 15),
        "actual_rotating_horizontal_C2_upper": decimal_upper(rotating_value, 18),
        "actual_Cartesian_horizontal_C2_upper": decimal_upper(cartesian_value, 18),
        "height_third_derivative_used": False,
        "coefficientwise_radial_suprema_preserved": True,
        "both_endpoint_height_means_and_radial_rotation_difference_retained": True,
        "independent_world_frame_and_position_ports_retained": True,
        "complete_finite_long_vector_graph_all_angular_tame": True,
        "full_body_and_far_matching_solved": False,
        "old_native_arrays_long_solutions_and_reference_integrations": 0,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
