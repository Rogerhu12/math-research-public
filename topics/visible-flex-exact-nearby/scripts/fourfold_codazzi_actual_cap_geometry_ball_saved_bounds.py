#!/usr/bin/env python3
"""New rational consequences of the already solved actual M cap.

This does not rerun a contraction, Green integral, physical coefficient
calculation, or geometry target.  It sharpens the proved fixed-point
radius and converts it to a complete real moving C0 bound.
"""
from fractions import Fraction as F


def main():
    comparisons = []

    def lt(name, value, upper):
        value, upper = F(value), F(upper)
        assert value < upper, (name, value, upper)
        comparisons.append((name, value, upper))

    rho = F(3, 10**6)
    forcing = F("0.000000323") + F(1, 2**80)
    gap = F(1) - F("0.879") - 208*rho
    new_radius = F("0.000002684")
    lt("same_actual_fixed_point_radius", forcing/gap, new_radius)
    lt("known_physical_readout_first_derivative", F(32,31)*F(11,24), F(1,2))
    lt("full_mean_aware_inverse_angle_factor", F(33,32)*F(7,4), F(2))

    v = F("5.954")
    u = F(1,50)
    denominator = F(1)-v*rho
    lt("direct_physical_B_difference_factor", v/denominator, F(6))
    lt("direct_physical_C_difference_factor", v*(u+v)/denominator, F(36))
    lt("complete_moving_cap_error_with_repair",
       37*new_radius+F(5,10**18), F("0.000099309"))
    lt("actual_cap_in_final_geometry_state_ball", F("0.000099309"), F(1,10000))

    print("All %d new actual-cap geometry-ball combinations passed." % len(comparisons))
    for name, value, upper in comparisons:
        print(name + ": " + str(value) + " < " + str(upper))


if __name__ == "__main__":
    main()
