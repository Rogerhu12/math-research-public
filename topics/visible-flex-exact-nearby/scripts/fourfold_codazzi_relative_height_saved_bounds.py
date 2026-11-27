"""RH: new exact-rational consequences of complete original selected bounds.

No original field, norm, trial, flow or pairing is evaluated.  All bounds
belong to the original Q_delta on [0,9/50], not a new compact centre.
See R147-supplement-relative-height-carriers-and-short-full-frequency-errors.md.
"""
from fractions import Fraction as F
import json


def conclusions():
    checks = []

    def check(name, statement):
        assert statement, name
        checks.append({"name": name, "passed": True})

    b = F(9, 50)
    B, G, curvature = F(211, 1000), F(28, 25), F(21, 20)
    mean, radius, v = F(16, 15), F(239, 125), F(18, 5)
    qmin, qmax, a = F(2669, 5000), F(103, 100), F(9, 8)
    check("complete_selected_mean_gap", F('1.068732504') > mean)
    check("complete_selected_beta", F('.210554393') < B)
    check("complete_selected_gamma", F('1.119697422') < G)
    check("complete_selected_gamma_lower", F('1.037358753') > 1)
    check("complete_selected_curvature", F('1.048658240') < curvature)
    check("complete_selected_pair_radius", F('1.911031809') < radius)
    check("complete_selected_q_lower", F('.533885761') > qmin)
    check("complete_selected_q_upper", F('1.029022746') < qmax)
    check("full_v_bound_from_same_pair_and_q", radius/qmin < v)
    check("short_positive_radius_by_log_derivative",
          B*b < 1 and F('1.068733119')/(1-B*b) < a)
    check("fourfold_primitive_Linfty_kernel", F(22, 7)/8 < F(2, 5))

    d = F(2, 5)*B*radius**2
    J = v/mean
    Cd = B*qmax*radius/2
    Cj = v/mean**2
    Ctau = F(11, 5)
    check("full_tau_state_derivative",
          Ctau-J*Cd > 0 and (Ctau-J*Cd)**2 > G**2+(d*Cj)**2)
    Cp, Ck, Ct = F(15, 32), F(19, 8), F(17, 32)
    check("full_p_state_derivative", B*Ctau < Cp)
    check("full_t_state_derivative", a*(Cd/mean+d/mean**2) < Ct)
    k_margin = Ck/a-radius*Cd/mean
    check("full_k_state_derivative",
          k_margin > 0 and k_margin**2 >
          (d/mean)**2+(G*curvature+d*radius/mean**2)**2)
    CM = Cc = F(5, 2)
    Cbase = F(19, 5)
    check("full_so3_axial_derivative", Cp**2+Ck**2+Ct**2 < CM**2)
    check("full_position_velocity_derivative", a*Ctau < Cc)
    check("complete_base_position_velocity",
          a**2*(G**2+(d*J+G*radius)**2) < Cbase**2)
    position_squared = (Cc**2*b+Cc*CM*Cbase*b**2+
                        (CM*Cbase)**2*b**3/3)
    position, frame, physical = F(36, 25), F(17, 16), F(53, 20)
    check("short_relative_position_L2_receiver", position_squared < position**2)
    check("short_axial_frame_L2_receiver", CM**2*b < frame**2)
    check("same_physical_test_body_receiver", position**2*J < physical**2)
    angle_primitive = F(5, 4)
    check("complete_angle_row_in_primitive_and_mean",
          1/mean**2+v**2/(16*mean**4) < angle_primitive**2)

    E2, Epm = F('6.765672e-6'), F('1.132677e-6')
    check("true_NP_relative_position_error", position*E2 < F('9.742568e-6'))
    check("true_NP_axial_frame_error", frame*E2 < F('7.188527e-6'))
    check("true_NP_fixed_physical_body_error", physical*E2 < F('1.792904e-5'))
    check("true_NP_full_physical_angle_error_coefficient",
          angle_primitive*Epm < F('1.415847e-6'))
    return {"kind": "RH_short_relative_height_exact_rational_consequences_v1",
            "checks": checks,
            "old_scientific_targets_evaluated": 0,
            "same_original_selected_background": True,
            "full_means_and_full_Fourier_error_retained": True,
            "frame_norm_is_axial_or_spectral_not_Frobenius": True,
            "independent_world_anchor_ports_retained": True,
            "actual_world_frame_carrier_claimed": False,
            "new_signed_height_integral_evaluated": False,
            "full_height_or_phase_Schur_closed": False}


if __name__ == '__main__':
    print(json.dumps(conclusions(), sort_keys=True))
