#!/usr/bin/env python3
"""New exact combinations for the actual cap-to-world anchor theorem.

Consumes only rational outward constants already proved in M, RA, RB,
C0 geometry, ACT, WRA and the completed WMR run 45942597362/1.
No old numerical producer, ODE, Fourier contraction, residual, or target
is called.  Every comparison below is a new cap-to-world combination.
"""
from fractions import Fraction as F


def main():
    checks = []

    def lt(name, value, upper):
        value, upper = F(value), F(upper)
        if not value < upper:
            raise AssertionError((name, value, upper))
        checks.append((name, str(value), str(upper)))

    rho = F(3, 10**6)
    repair = F(5, 10**18)
    e = F(71, 500000)
    d = F(1, 10**10)
    omega_state = F("15.736315")
    omega_nu = F("0.304809")
    position_state = F("30.196406")
    position_nu = F("0.105999")
    path = F("1.950540")
    r_frame = F(1, 10**12)
    r_height = F(6, 10**21)
    frame_l = F("0.002234557")
    height_l = F("0.004287890")

    lt("complete_cap_moving_C0_with_repair", 47*rho+repair, e)
    lt("actual_cap_mean_gap", F(3)+e+repair, F("3.1914104290"))
    lt("cap_L_vertical_frame", r_frame+omega_state*e, frame_l)
    lt("cap_L_height_mod_one_constant",
       r_height+path*r_frame+position_state*e, height_l)
    lt("whole_cap_anchored_b_frame_with_compact_metric",
       r_frame+omega_state*e+omega_nu*d, F("0.002235"))
    lt("whole_cap_anchored_b_height_mod_one_constant",
       r_height+path*r_frame+position_state*e+position_nu*d,
       F("0.004288"))

    defect_q = F("0.00000003127699")
    defect_f = F("0.00000004956566")
    raw_omega = F("2.157")
    raw_fphi = F("4.001")
    intrinsic_beta_gamma = F("2.227")
    intrinsic_radius = F("4.131")
    lt("raw_angular_connection_from_paid_defect",
       F("2.156")+defect_q, raw_omega)
    lt("raw_angular_velocity_from_paid_defect", F(4)+defect_f, raw_fphi)
    lt("intrinsic_beta_over_gamma_from_same_angle",
       F(32,31)*raw_omega, intrinsic_beta_gamma)
    lt("intrinsic_radius_from_same_angle",
       F(32,31)*raw_fphi, intrinsic_radius)
    lt("complete_cap_angular_connection_difference_factor",
       intrinsic_beta_gamma+intrinsic_radius*F(67,150), F("4.073"))

    frame_l_1 = F("0.005399")
    height_l_1 = F("0.009528")
    lt("actual_cap_L_frame_C1",
       raw_omega*frame_l+F("4.073")*e+defect_q, frame_l_1)
    lt("actual_cap_L_height_C1",
       raw_fphi*frame_l+intrinsic_radius*e+defect_f, height_l_1)

    b0, bq1, bf1 = F("0.002235"), F("0.015072"), F("0.04748")
    lt("ACT_actual_b_frame_C0", frame_l+F("0.00000003148"), b0)
    lt("ACT_actual_b_frame_C1",
       frame_l_1+F("4.312")*frame_l+F("0.000036461"), bq1)
    lt("ACT_actual_b_height_C1",
       height_l_1+F("1.950541")*frame_l_1
       +F("12.205365")*frame_l+F("0.000141"), bf1)

    lt("actual_root_weak_height_receiver",
       F(94000)+86061*b0+12531*bq1+4590*bf1, F(94600))
    lt("actual_root_source_weak_height_receiver",
       F(6650)+6086*b0+887*bq1+325*bf1, F(6693))
    lt("actual_strict_source_weak_height_receiver",
       F(3000)+2919*b0+441*bq1+210*bf1, F(3024))
    lt("actual_strict_jump_weak_height_receiver",
       F(8850)+8098*b0+1180*bq1+432*bf1, F(8907))

    uk, gs = F("0.031082487"), F("0.006877446")
    height_error = uk*b0+gs*F("0.004288")
    lt("complete_particular_actual_anchor_error", height_error, F("0.000099"))
    lt("actual_particular_negative_upper",
       -F("0.0252298")+F("0.000099"), -F("0.02513"))
    lt("actual_particular_negative_lower",
       -F("0.02547"), -F("0.0253702")-F("0.000099"))
    lt("actual_particular_scalar_inverse", F(1,1)/F("0.02513"), F(40))
    print("All %d new exact cap/world combinations passed." % len(checks))
    for name, value, upper in checks:
        print(name + ": " + value + " < " + upper)


if __name__ == "__main__":
    main()
