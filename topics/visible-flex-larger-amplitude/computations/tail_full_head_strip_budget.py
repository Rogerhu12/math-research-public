#!/usr/bin/env python3
"""Exact constants in R33; no actual full-head closure is asserted.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
No radial integration, Galerkin solve, or Node process is performed.
"""
from fractions import Fraction as Q
import argparse
import hashlib
import json
from pathlib import Path


def record(x):
    return dict(exact=str(x), decimal=float(x))


def ledger():
    T = Q(1,20)
    z = (2*T+Q(5,4)*T*T)/4
    u = 1-z
    checks = {
        "normalized_discriminant_perturbation_below_3over100": z < Q(3,100),
        "square_root_second_remainder_coefficient_below_half": 9 < 16*u**5,
        "square_root_first_difference_coefficient_below_3over5": 25 < 36*u**3,
        "inverse_square_root_below_21over20": 400 < 441*u,
        "inverse_three_halves_below_11over10": 100 < 121*u**3,
        "three_halves_difference_coefficient_below_7over4": 36 < 49*u**5,
        "second_remainder_term": (2+Q(5,4)*T)**2/8 < Q(9,16),
        "mixed_product_term": (Q(1,4)+T/4)/(1-T*T/4) < Q(3,10),
        "last_product_term": (1+T)/(1-T*T/4)*Q(3,5)/4*(2+Q(5,4)*T) < Q(7,20),
        "sum_of_four_quadratic_coefficients": Q(5,8)+Q(9,16)+Q(3,10)+Q(7,20) < 2,
        "mean_derivative_first_term": Q(21,20)/(1-T*T/4) < Q(11,10),
        "mean_derivative_mixed_term": Q(11,10)/4*(1+T)**2/(1-T*T/4) < Q(1,3),
        "mean_derivative_total": Q(43,30)+Q(231,256) < Q(5,2),
    }
    R = Q(1,32)
    total = R+4*R*R
    checks.update(
        mean_root_total_input=total < T,
        mean_root_self_map=2*total**2 < 4*R**2,
        mean_root_contraction=Q(5,2)*total < Q(1,8))
    small = Q(1,64)
    checks.update(
        full_leading_inverse_below_two=Q(5,4)*small+4*small**2 < Q(1,2),
        complete_mean_lift_below_two=1+4*small < 2,
        complete_field_difference_below_two=1+16*small < 2,
        quadratic_source_constant=2*(2+4+Q(6,4)) < 16,
        lipschitz_source_constant=15+120*small < 32)
    count, total_logs, cutoff = 224-12+1, sum(3*n+32 for n in range(12,225)), 4096
    linear_width = 4+Q(7,10)*total_logs/cutoff
    remaining = Q(38)-1-linear_width
    checks.update(
        cell_count=count == 213,
        exact_downward_log_sum=total_logs == 82218,
        displayed_linear_width_upper=linear_width < Q(4513,250),
        displayed_remaining_width_lower=remaining > Q(4737,250))
    assert all(checks.values()), [k for k,v in checks.items() if not v]
    return dict(
        status="Exact constants for the conditional R33 full-frequency theorem",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        checks=checks,
        mean_root=dict(w_upper=record(Q(1,2)), holomorphic_input_radius=record(R),
            working_input_radius=record(small), mean_quadratic_constant=4,
            quadratic_remainder_constant=2, derivative_constant=16,
            maximal_discriminant_perturbation=record(z)),
        full_source=dict(quadratic_constant=16,
            difference_constant=32, density="(1/r+abs(w_r/w))*V(r)^2/w(r)",
            state="(B*p/V,kappa_perp/V), componentwise Fourier radial suprema"),
        deep_head_material=dict(first_cell=12,last_cell=224,cell_count=count,
            frequency_cutoff=cutoff, downward_log_sum_in_units_log2=total_logs,
            angle_loss_upper=4, linear_width_upper=record(linear_width),
            remaining_38_to_1_width_lower=record(remaining),
            assumes_V_non_decreasing_outward=True),
        actual_complete_strong_head_closure_paid=False,
        actual_finite_window_density_Green_paid=False,
        actual_source_profile_envelope_paid=False,
        actual_deep_graph_feedback_paid=False,
        limits=[
            "The high-frequency inequality still requires the chosen B,V,tau and the source-density width integral.",
            "All finite modes below the cutoff and the actual nonlinear deep-graph feedback remain separate inputs.",
            "No M8 or 46-mode scalar-L1 Green result is relabeled as a density-space full-frequency certificate.",
            "The 0..11 outer-head material budget is not included in the 12..224 displayed example."])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    result=ledger()
    result["script_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(dict(output=str(args.out),checks=len(result["checks"]),
        all_passed=True,actual_complete_strong_head_closure_paid=False)))


if __name__=="__main__":
    main()
