#!/usr/bin/env python3
"""R99 exact rational field-to-physical-jet bridge for R95.

The input field-difference caps are hypotheses supplied by a separate true
solution proof. This consumer never certifies existence or those caps. The
complete candidate mean and its nonzero actual J residual are retained.
Only standard-library Fraction arithmetic controls the output.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from fractions import Fraction as Q
import argparse
import hashlib
import json
from pathlib import Path

INPUTS = ("Kbar", "P", "P_theta", "Kbar_theta")
OUTPUTS = ("h_r", "h_theta", "h_rr", "h_rtheta", "h_thetatheta")


def fraction(value):
    if isinstance(value, Q):
        return value
    if isinstance(value, bool):
        raise TypeError("A Boolean is not a numerical cap")
    if isinstance(value, int):
        return Q(value)
    if isinstance(value, str):
        return Q(value)
    if isinstance(value, dict) and set(("numerator", "denominator")) <= set(value):
        return Q(int(value["numerator"]), int(value["denominator"]))
    raise TypeError("Use exact integers, rational strings or numerator/denominator records")


def record(value):
    value = fraction(value)
    return dict(numerator=str(value.numerator), denominator=str(value.denominator))


def nonnegative(value, name):
    value = fraction(value)
    if value < 0:
        raise ValueError(name + " is negative")
    return value


def positive(value, name):
    value = fraction(value)
    if value <= 0:
        raise ValueError(name + " is not strictly positive")
    return value


def multiply(matrix, vector):
    return [sum((coefficient*value for coefficient, value in zip(row, vector)), Q(0))
            for row in matrix]


def complete_field_bridge(data):
    """Conditional real-angle sup bounds from actual Fourier A0 differences.

    Every joint cap holds for BOTH complete mean roots on the same real g.
    A/D positivity along the state line follows by concavity; L is affine.
    Intermediate states need not solve the mean equation. No complex-strip
    inverse is inferred from the real positive lower bounds.
    """
    if data["schema"] != "complete-mean-field-to-physical-jets-input-v1":
        raise ValueError("A typed complete-mean field difference input is required")
    assumptions = data["required_hypotheses"]
    required = (
        "same_true_metric_and_physical_radius",
        "candidate_is_one_compatible_height_with_actual_derivatives",
        "candidate_complete_mean_root_and_actual_mean_derivative",
        "comparison_is_a_true_full_unprojected_Darboux_height",
        "comparison_uses_the_same_complete_mean_branch",
        "joint_real_A_D_L_caps_cover_both_complete_roots",
        "differences_are_A0_Fourier_mass_bounds",
        "both_nonmean_fields_have_zero_mean_and_minimum_mode_two",
        "candidate_J_uses_all_frequencies_and_complete_mean",
    )
    if any(assumptions.get(key) is not True for key in required):
        raise ValueError("A required conditional hypothesis was not explicitly stated")
    b, box = data["background_bounds"], data["joint_field_bounds"]
    rlo = positive(b["r_lower"], "r_lower")
    rhi = positive(b["r_upper"], "r_upper")
    wlo = positive(b["w_lower"], "w_lower")
    w = positive(b["w_upper"], "w_upper")
    rxlo = positive(b["r_x_lower"], "r_x_lower")
    wr = nonnegative(b["abs_w_r_upper"], "abs_w_r_upper")
    if rlo > rhi or wlo > w:
        raise ValueError("A common true background interval is reversed")
    z, E = w*w, 1+w*w
    p = nonnegative(box["P_A0_upper"], "P_A0_upper")
    k = nonnegative(box["complete_K_A0_upper"], "complete_K_A0_upper")
    t = nonnegative(box["P_theta_A0_upper"], "P_theta_A0_upper")
    U = nonnegative(box["K_theta_minus_P_A0_upper"], "K_theta_minus_P_A0_upper")
    a = min(Q(1), positive(box["real_A_lower"], "real_A_lower"))
    d = min(Q(1), positive(box["real_D_lower"], "real_D_lower"))
    ell = positive(box["real_L_lower"], "real_L_lower")

    # M.14: the complete mean derivative is >= L_min/E_max^2.
    u = z*(2*k+k*k+E*p*p)
    CK = (k+E*t)/(d*d) + Q(3, 2)*u/(d*d*d)
    CT = (k+z*p*p)/(a*d) + u/(2*d*d)
    CP = E*p*(1+z*(1+k)*t/a)/(d*d) + 2*z*p*(1+k)*t/(a*a*d)
    mean_coefficients = [E*E*CK/ell, E*E*CP/ell, E*E*CT/ell, Q(0)]
    # The numerator below is an absolute bound, not its signed midpoint.
    numerator = wr*(1+z*((1+k)*t+p*p)) + E*w*U*U/rlo
    FK = wr*z*t/ell + numerator/(ell*ell)
    FP = 2*wr*z*p/ell + 2*E*w*U/(rlo*ell)
    FT = wr*z*(1+k)/ell + E*numerator/(ell*ell)
    Ftheta = 2*E*w*U/(rlo*ell)
    aK, aP, aT, unused = mean_coefficients

    # Order: Kbar, P, P_theta, Kbar_theta.
    matrix = [
        [w*(1+aK), w*aP, w*aT, Q(0)],
        [Q(0), rhi*w, Q(0), Q(0)],
        [FK*(1+aK), FP+FK*aP, FT+FK*aT, Ftheta],
        [Q(0), Q(0), Q(0), w],
        [Q(0), Q(0), rhi*w, Q(0)],
    ]
    J = nonnegative(data["candidate_residual"]["complete_J_A0_upper"], "complete_J_A0_upper")
    residual = w*J/(rxlo*ell)
    residual_options = {"complete_J": residual}
    if "complete_physical_Darboux_upper" in data["candidate_residual"]:
        D = nonnegative(data["candidate_residual"]["complete_physical_Darboux_upper"],
                        "complete_physical_Darboux_upper")
        residual_options["same_candidate_physical_Darboux"] = rhi*E*E*D/(wlo*ell)
        residual = min(residual_options.values())
    if "complete_physical_RK_upper" in data["candidate_residual"]:
        R = nonnegative(data["candidate_residual"]["complete_physical_RK_upper"],
                        "complete_physical_RK_upper")
        residual_options["same_candidate_complete_RK"] = R
        residual = min(residual_options.values())
    e = [nonnegative(data["field_difference_A0_upper"][name], name) for name in INPUTS]
    jets = multiply(matrix, e)
    jets[2] += residual
    # A same-location candidate-to-candidate bridge is added only when given.
    earlier = data.get("reference_to_candidate_physical_jet_upper",
                       {name: "0" for name in OUTPUTS})
    jets = [value+nonnegative(earlier[name], "reference_to_candidate."+name)
            for name, value in zip(OUTPUTS, jets)]
    mean_difference = sum((a*x for a, x in zip(mean_coefficients, e)), Q(0))
    combined_strong_coefficients = multiply(matrix, [Q(1,3),Q(1,3),Q(1),Q(1)])
    result = dict(
        schema="conditional-complete-mean-field-to-physical-jets-v1",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        input_hypotheses_copied=assumptions,
        input_order=list(INPUTS), output_order=list(OUTPUTS),
        complete_mean_difference_coefficients=[record(x) for x in mean_coefficients],
        positive_5_by_4_matrix=[[record(x) for x in row] for row in matrix],
        complete_mean_difference_upper=record(mean_difference),
        candidate_physical_second_defect_upper=record(residual),
        candidate_residual_options={key:record(x) for key,x in residual_options.items()},
        total_reference_to_true_physical_jet_upper={
            name:record(value) for name,value in zip(OUTPUTS,jets)},
        coefficient_for_a_joint_A_tau_1_field_difference=[
            record(x) for x in combined_strong_coefficients],
        candidate_and_reference_terms_not_removed_when_field_error_zero=True,
        complete_mean_zero_mode_not_dropped=True,
        all_true_nonmean_modes_included_in_stated_error=True,
        radial_derivative_obtained_only_from_true_equation_with_candidate_residual=True,
        output_hrr_is_a_real_angle_sup_bound_not_a_free_A_tau_bound=True,
        new_ODE_Node_or_source_integration=False,
        true_solution_or_input_error_bounds_certified_here=False,
        final_geometric_gate_paid_here=False,
    )
    if "r95_uniform_physical_gate" in data:
        gate = positive(data["r95_uniform_physical_gate"], "r95_uniform_physical_gate")
        result["conditional_r95_componentwise_gate"] = dict(
            threshold=record(gate), passed=all(x <= gate for x in jets),
            components={name:value <= gate for name,value in zip(OUTPUTS,jets)},
            existence_and_stated_input_errors_remain_external_obligations=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a fresh conditional jet-bridge output")
    raw = args.input.read_bytes()
    data = json.loads(raw)
    result = complete_field_bridge(data)
    result["input_file"] = str(args.input)
    result["input_sha256"] = hashlib.sha256(raw).hexdigest()
    result["producer_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.out.with_name(args.out.name+".tmp")
    with temporary.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write("\n")
    temporary.replace(args.out)


if __name__ == "__main__":
    main()
