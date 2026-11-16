#!/usr/bin/env python3
"""New explicit natural negative-window constants from one complete root97 result.
All saved scientific graphs, the original e/g comparison and old producers are read only.
"""
from __future__ import annotations
import argparse
import ast
import copy
from fractions import Fraction
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import re
import time
import traceback
from flint import arb, ctx

PUBLIC = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby/"
SOURCE = "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_root_natural_negative_window_explicit_constants.py"
WORKER = "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_root_natural_negative_window_explicit_constants_public_worker.py"
KIND = "complete_root_natural_negative_window_explicit_constants_v1"
MANIFEST_KIND = "root_natural_negative_window_explicit_constants_public_inputs_v1"
RUNTIME = {"Python":"3.12.14","python_flint":"0.9.0"}
GATE_COUNT = 16
COMPLETE_SCIENCE_MAX_BYTES = 75000
PIN_SPECS = {"contract":{"path":"topics/visible-flex-exact-nearby/results/R133-supplement-explicit-uniform-natural-negative-window-inverse-constants.md","git_blob":"d6cb8f723584a5f893a01324033d059995d1ee79","bytes":17890,"sha256":"030e434ed31632c0c5330318251486d37424deba78f3fe35bf8b738960425120"},"rni_contract":{"path":"topics/visible-flex-exact-nearby/results/R133-supplement-conditional-cutoff97-faithfulness-and-uniform-natural-window-inverses.md","git_blob":"ce0a46c75360850479333534cf096fd61f412168","bytes":19405,"sha256":"d771cf43faa0d5351851168f9f1567e21f8b7e0be27480b6bd67880a4eb69a81"},"saved_science":{"path":"topics/visible-flex-exact-nearby/notes/root_stable_cutoff97_saved_prefix_recovery_ci/run-43789221154-1/actual-scientific-conclusion.json","git_blob":"577956f3a919360969ac86457c40c40ca752245a","bytes":56630,"sha256":"0c27195fad92a0be1296e533594fae8df46f4f70a6af359e762374141ac770ea"},"saved_execution":{"path":"topics/visible-flex-exact-nearby/notes/root_stable_cutoff97_saved_prefix_recovery_ci/run-43789221154-1/execution.json","git_blob":"493f952207c654744cb807f46bebc7ea00ea0e8f","bytes":11832,"sha256":"a83f20c1b541173c871aee990b6797d9b76ecd9f1c831cbfac719900c18e379f"},"saved_source":{"path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_root_stable_cutoff97_saved_prefix_recovery.py","git_blob":"ce991a307b62f2382127ffa10c9ca92b69a82696","bytes":61957,"sha256":"799b7faa1d2a72374b591561fefeb446099f3d27fe47b2d6ddbd4ae21b6d2534"},"saved_manifest":{"path":"topics/visible-flex-exact-nearby/notes/2026-11-16-R133-root-stable-cutoff97-saved-prefix-recovery-CI-inputs.json","git_blob":"bc6d467c1e9f119d29b117f6985b2efea0074daa","bytes":13656,"sha256":"5d993fefa9cbd2935812d051c4a83a0ff0d4e607d2836ea69d7a93423beb633e"}}
HISTORICAL_INPUTS = []
PARAMETERS = {"arithmetic_bits":320,"expected_actual_gate_count":16,"original_R97R_run":"43789221154/1","exact_real_delta_radius":"1/100000000","fixed_intrinsic_parameter":"eta_0","exact_intrinsic_parameter":"-7789843107295549/4611686018427387904","exact_root_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],"physical_root_piece":2549,"physical_period":"pi/2","normalized_angular_measure":True,"physical_frequency":"n=4|j|","input_cutoff_abs_j":97,"physical_minimum_frequency":388,"natural_negative_windows":["-7/6","-5/2"],"ordered_gain_windows":["-5/2","-11/6","-7/6","-1/2"],"stable_error_gain":"2/3","R0_complete_kernel_bandwidths":[192,384,576,192,384,384,0,576],"weighted_R0_output_cutoffs":[1,97],"complete_primitive_one_gain":"sqrt(17)/4","physical_independent_means":2,"expected_current_inputs":9,"expected_total_inputs":9,"expected_Python_AST_files":3,"expected_historical_inputs":0,"saved_complete_objects":4,"saved_scalar_records":23,"old_target_calls_allowed":0,"old_source_imports_allowed":0,"old_strict_comparisons_reevaluated":0,"full_complex_parameter_square_claimed":False,"uniform_selected_chart_family_claimed":False,"complete_incoming_or_finite_Schur_inverse_claimed":False}
RETAINED_SCOPE = {"scientific_target":"explicit uniform natural negative-window inverse constants for the actual original root97 stable operator","same_real_delta_family_and_fixed_intrinsic_eta0":True,"original_reflection_and_two_carrier_signs_retained":True,"physical_fourier_factor_four_and_normalized_measure_retained":True,"complete_positive_R0_mean_rank_retained":True,"independent_physical_mean_coordinates":2,"full_low_intermediate_primitive_one_quarter_retained":True,"L_and_J_not_assigned_new_finite_bandwidth":True,"original_J1_is_left_angular_derivative":True,"J_negative_windows_use_same_direction_finite_bootstrap":True,"input_frequency_diagonals_kept_in_original_order":True,"old_scalar_upper_bounds_used_only_with_exact_positive_kernel_qualification":True,"saved_positive_strict_margin_read_only":True,"old_R97_graphs_and_comparison_not_recomputed":True,"same_distributional_inverse_in_both_natural_windows":True,"true_Riccati_frame_used_only_through_uniform_bounds_and_strong_realization":True,"Riccati_operator_norm_continuity_claimed":False,"uniform_selected_chart_family_claimed":False,"physical_bulk_Poisson_extension_claimed":False,"complete_incoming_inverse_claimed":False,"finite_Schur_inverse_claimed":False,"nonlinear_background_or_final_surface_claimed":False,"original_low_complement_radial_head_sources_and_all_other_finite_ports_retained":True}
PLANNED_SHAPE = {"saved_actual_receipts":1,"saved_complete_objects":4,"saved_scalar_records":23,"new_L_commutator_bounds":4,"new_complete_J_L2_candidates":2,"new_J_gain_windows":4,"new_weighted_R0_routes":8,"new_weighted_R0_positive_terms":64,"new_amplitude_gain_windows":4,"new_amplitude_gain_positive_terms":8,"new_stable_gain_windows":4,"new_stable_gain_positive_terms":12,"new_natural_inverse_windows":2,"new_finite_inverse_polynomial_terms":8,"new_complete_whole_choices":1,"new_geometric_rational_powers":26,"new_fixed_square_roots":4,"retained_physical_means":2}
COMPLETE_FIELDS = ["kind","complete","proved","actual_returncode","failure","stage","source_sha256","input_manifest_sha256","public_repository","run_id","run_attempt","workflow_event_commit","actual_scientific_checkout_commit","runtime","arithmetic_bits","parameters","input_sha256","verified_original_inputs","accepted_old_inputs","complete_original_objects_read_verbatim","complete_original_objects_sha256","complete_saved_scalar_records_read_verbatim","complete_saved_scalar_records_sha256","complete_geometry_conclusion","complete_L_commutator_conclusion","complete_J_gain_conclusion","complete_weighted_R0_conclusion","complete_amplitude_gain_conclusion","complete_stable_gain_conclusion","complete_natural_inverse_conclusion","retained_scope","planned_shape","actual_progress","gates","actual_mathematical_wall_seconds"]
GATE_NAMES = ["actual public Actions runtime and the frozen new source are exact","nine current small texts and the complete new parameter closure are frozen","all six mathematical primaries have their complete original bytes SHA and Git identity","the original recovery science and execution are matching complete actual identities","the original nine gates strict true result and zero rerun counters are inherited","four original objects and twenty three scalar records are preserved with typed endpoints","four complete commutator Sobolev bounds retain the physical angular normalization","the same direction J bootstrap retains both complete L2 candidates and all four windows","both weighted R0 routes keep every one of the eight original positive terms and the mean rank","all four amplitude gains retain double high projection and original input powers","four complete E gains keep ordered J L and the full low output primitive one quarter","both natural negative inverses use the saved positive gap and separate finite products","all original objects and inputs stay unchanged with zero old comparison evaluation","all complete new ball records and every positive finite formula are retained","new scalar counts and actual completion progress match the complete target","the complete thirty five field schema preserves the same inverse and every retained port"]
INITIAL_ACTUAL_PROGRESS = {"accepted_same_R97R_success":False,"new_commutator_bounds_completed":0,"new_complete_J_candidates_completed":0,"new_same_direction_J_windows_completed":0,"new_weighted_R0_routes_completed":0,"new_amplitude_gain_windows_completed":0,"new_stable_gain_windows_completed":0,"new_natural_inverse_windows_completed":0,"new_complete_whole_choices":0,"new_geometric_rational_powers_completed":0,"new_fixed_sqrt_constants_completed":0,"old_scientific_targets_recomputed":0,"old_R97_root_graphs_recomputed":0,"old_R97_strict_comparisons_reevaluated":0,"historical_inputs_restored":0}
SUCCESS_ACTUAL_PROGRESS = {"accepted_same_R97R_success":True,"new_commutator_bounds_completed":4,"new_complete_J_candidates_completed":2,"new_same_direction_J_windows_completed":4,"new_weighted_R0_routes_completed":8,"new_amplitude_gain_windows_completed":4,"new_stable_gain_windows_completed":4,"new_natural_inverse_windows_completed":2,"new_complete_whole_choices":1,"new_geometric_rational_powers_completed":26,"new_fixed_sqrt_constants_completed":4,"old_scientific_targets_recomputed":0,"old_R97_root_graphs_recomputed":0,"old_R97_strict_comparisons_reevaluated":0,"historical_inputs_restored":0}
OLD = {"kind":"complete_root_stable_cutoff97_saved_prefix_recovery","execution_kind":"actual_public_root_stable_cutoff97_saved_prefix_recovery_execution_v1","manifest_kind":"complete_root_stable_cutoff97_saved_prefix_recovery_public_inputs_v1","run_id":"43789221154","run_attempt":"1","workflow_event_commit":"2600bb87f783eaf1c0b7415f46599ce6f8460c05","actual_scientific_checkout_commit":"2600bb87f783eaf1c0b7415f46599ce6f8460c05","runtime":{"Python":"3.12.14","python_flint":"0.9.0"},"arithmetic_bits":320,"source_sha256":"799b7faa1d2a72374b591561fefeb446099f3d27fe47b2d6ddbd4ae21b6d2534","input_manifest_sha256":"5d993fefa9cbd2935812d051c4a83a0ff0d4e607d2836ea69d7a93423beb633e","science_bytes":56630,"science_sha256":"0c27195fad92a0be1296e533594fae8df46f4f70a6af359e762374141ac770ea","execution_sha256":"a83f20c1b541173c871aee990b6797d9b76ecd9f1c831cbfac719900c18e379f","worker_sha256":"add2b325a391e66a001df0a4f6547a545460188132e51025fbce378935461f04","gate_count":9,"field_count":35,"input_receipt_count":9,"input_receipts_sha256":"629cfb0fd5e0a68df48ec243e350af583117d20711975360fefee96243d57f5b","AST_file_count":3,"AST_inventory_sha256":"0469b173088a5dd6b0161fec9b39cf20da92a17b56bbd3273d7664df0e1c4594","prefix_evidence_sha256":"be0f6546f2e3493b9650cb53800429364b4a1614de805c5f9ebebe4cd37eb32c","complete_objects_sha256":"01cac119904ff63260d1f7d7c3370e49f276b4c88aba2903ce2acae88b7c3313","scalar_records_sha256":"08b04bfb460b3a5c18b85092715d122a65586b1b258a4d1d64ce6928d7f971ed"}
EXPECTED_ACCEPTED_OLD_INPUTS = {"run_id":"43789221154","run_attempt":"1","source_sha256":"799b7faa1d2a72374b591561fefeb446099f3d27fe47b2d6ddbd4ae21b6d2534","input_manifest_sha256":"5d993fefa9cbd2935812d051c4a83a0ff0d4e607d2836ea69d7a93423beb633e","science_sha256":"0c27195fad92a0be1296e533594fae8df46f4f70a6af359e762374141ac770ea","science_bytes":56630,"execution_sha256":"a83f20c1b541173c871aee990b6797d9b76ecd9f1c831cbfac719900c18e379f","workflow_event_commit":"2600bb87f783eaf1c0b7415f46599ce6f8460c05","actual_scientific_checkout_commit":"2600bb87f783eaf1c0b7415f46599ce6f8460c05","runtime":{"Python":"3.12.14","python_flint":"0.9.0"},"arithmetic_bits":320,"complete_old_gates_read_verbatim":[{"name":"complete saved original97 prefix, original source, manifest and execution identity","passed":True},{"name":"complete real moments and neighborhood radial derivatives retain all mean terms","passed":True},{"name":"complete mixed drift derivatives and every D squared p term are finite","passed":True},{"name":"complete rational quotient retains both gaps and all third ordinary derivatives","passed":True},{"name":"complete collected correlations preserve all nine derivative groups and the true mean","passed":True},{"name":"all ordered operator terms and genuine positive diagonal bounds are complete","passed":True},{"name":"the optional strict comparison has its exact narrow ordinary L2 scope","passed":True},{"name":"all original input bytes remain unchanged with zero old target calls","passed":True},{"name":"complete scalar schema retains every conclusion whether the sufficient test passes or fails","passed":True}],"parameters_read_verbatim":{"arithmetic_bits":320,"exact_intrinsic_parameter":"-7789843107295549/4611686018427387904","exact_real_delta_radius":"1/100000000","exact_real_z_interval":["0","1/9409"],"exact_root_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],"expected_Python_AST_files":3,"expected_actual_gate_count":9,"expected_current_inputs":9,"expected_historical_gzip_inputs":0,"expected_total_inputs":9,"fixed_intrinsic_parameter":"eta_0","frequency_relation":"z=j^-2=16*n^-2","full_complex_square_claimed":False,"full_incoming_or_finite_Schur_inverse_claimed":False,"input_cutoff_abs_j":97,"normalized_angular_measure":True,"old_source_imports_allowed":0,"old_target_calls_allowed":0,"physical_frequency":"n=4|j|","physical_minimum_frequency":388,"physical_period":"pi/2","physical_root_piece":2549,"retained_physical_means":2,"strict_failure_is_complete_scalar_result":True},"actual_progress_read_verbatim":{"completed_original_cutoff97_comparisons":1,"historical_gzip_restores":0,"new_correlated_conclusion_completed":1,"new_drift_conclusion_completed":1,"new_quotient_conclusion_completed":1,"new_radial_conclusion_completed":1,"old_successful_targets_recomputed":0,"preserved_gate_count":14,"saved_complete_math_conclusions_reused":2,"saved_mixed_selections_recomputed":0,"saved_prefix_validation_passed":True,"saved_root_domain_recomputed":0},"old_input_receipt_count":9,"old_input_receipts_canonical_sha256":"629cfb0fd5e0a68df48ec243e350af583117d20711975360fefee96243d57f5b","old_AST_file_count":3,"old_AST_inventory_sha256":"0469b173088a5dd6b0161fec9b39cf20da92a17b56bbd3273d7664df0e1c4594","inherited_prefix_evidence_canonical_sha256":"be0f6546f2e3493b9650cb53800429364b4a1614de805c5f9ebebe4cd37eb32c","same_original_strict_true_result_read_without_reevaluation":True,"old_source_is_only_AST_identity_evidence_not_imported":True,"old_scientific_targets_called":0,"historical_natives_restored":0}
RULES = {"role":"rules","path":"topics/visible-flex-exact-nearby/notes/2026-11-15-1133-R133-reviewed-public-CI-rules-cleanup-history.json","git_blob":"5c5d020913d717bb5bc8ce891297e00eaa8944f7","bytes":2461,"sha256":"65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1"}
PUBLICATION_LIMITS = {"complete_science_bytes":75000,"complete_report_bytes":8000,"complete_prepublication_science_report_payload_bytes":90000,"complete_execution_bytes":59000,"pre_science_topic_reserve_bytes":150000,"scientific_file_atomic_and_complete_stdout_before_size_guards":True,"new_artifacts":0,"new_Releases":0}


Q_WINDOWS = ("-5/2", "-11/6", "-7/6", "-1/2")
BANDS = (192, 384, 576, 192, 384, 384, 0, 576)

def ex(value):
    q = Fraction(value)
    return arb(q.numerator) / arb(q.denominator)

def ball(value):
    if isinstance(value, arb):
        return value
    if isinstance(value, dict):
        if set(value) != {"ball"}:
            raise ValueError("unexpected saved ball object")
        value = value["ball"]
    return arb(value)

def up(value):
    value = ball(value)
    if not value.is_finite():
        raise ArithmeticError("nonfinite new positive bound")
    return abs(value).upper()

def upper_sum(values):
    return up(sum((up(v) for v in values), arb(0)))

def rec(value):
    value = ball(value)
    if not value.is_finite():
        raise ArithmeticError("nonfinite record")
    return value.str(75)

def encoded(value):
    if isinstance(value, arb):
        return rec(value)
    if isinstance(value, list):
        return [encoded(v) for v in value]
    if isinstance(value, tuple):
        return [encoded(v) for v in value]
    if isinstance(value, dict):
        return {k: encoded(v) for k, v in value.items()}
    return value

def whole_choice(candidates):
    records = {key: rec(value) for key, value in candidates}
    selected = next(iter(records))
    for key in records:
        if ball(records[key]).upper() < ball(records[selected]).upper():
            selected = key
    return dict(complete_candidate_records=records,
        selected_complete_candidate=selected,
        complete_selected_upper=records[selected],
        comparison_uses_complete_final_record_upper_endpoints=True,
        first_candidate_wins_exact_ties=True,
        all_candidates_bound_the_same_complete_operator_and_window=True)

def start_geometry(doc):
    g = dict(fixed_square_roots={}, positive_geometric_powers={},
        old_frequency_power_is_read_verbatim_not_recomputed=True)
    doc["complete_geometry_conclusion"] = g
    ctx = dict(records=g, values={}, document=doc)
    for number in (2, 3, 17, 67):
        value = up(ex(number).sqrt())
        ctx["values"]["sqrt"+str(number)] = value
        g["fixed_square_roots"]["sqrt"+str(number)] = rec(value)
        doc["actual_progress"]["new_fixed_sqrt_constants_completed"] += 1
    ctx["values"]["CI"] = up(ctx["values"]["sqrt17"]/4)
    g["complete_CI_upper"] = rec(ctx["values"]["CI"])
    return ctx

def geometric_power(geometry, key, base, exponent):
    if key in geometry["values"]:
        return geometry["values"][key]
    base, exponent = Fraction(base), Fraction(exponent)
    if not base > 0 or exponent < 0:
        raise ValueError("positive geometric power qualification")
    x = ex(base)
    if not x.lower() > 0:
        raise ArithmeticError("geometric base lost strict positivity")
    value = up((x.log()*ex(exponent)).exp())
    geometry["values"][key] = value
    geometry["records"]["positive_geometric_powers"][key] = dict(
        base=str(base), exponent=str(exponent), complete_upper=rec(value))
    geometry["document"]["actual_progress"]["new_geometric_rational_powers_completed"] += 1
    return value

def band_weight(geometry, bandwidth, cutoff, exponent):
    exponent = abs(Fraction(exponent))
    if bandwidth == 0 or exponent == 0:
        return ex(1)
    key = str(bandwidth)+"/"+str(cutoff)+"|"+str(exponent)
    return geometric_power(geometry, key, 1+Fraction(bandwidth, cutoff), exponent)

def complete_L_bounds(saved, geometry):
    ell = saved["l"]
    sq = geometry["values"]
    terms = [[ell[0]], [ell[0],ell[1]],
        [ell[0],up(sq["sqrt2"]*ell[1]),ell[2]],
        [ell[0],up(2*ell[1]),up(sq["sqrt3"]*ell[2]),ell[3]]]
    bounds = [upper_sum(row) for row in terms]
    report = dict(integer_orders=[0,1,2,3],
        complete_positive_terms=terms, complete_integer_Sobolev_bounds=bounds,
        ordinary_angular_derivative_has_physical_frequency_four=True,
        same_bounds_for_L_and_its_adjoint=True,
        negative_L_windows_follow_duality_and_interpolation=True,
        no_finite_band_assumption_for_L_or_J=True)
    return bounds, encoded(report)

def complete_J_gains(saved, L, geometry):
    P0 = up(geometry["values"]["CI"]/saved["eta_minus"])
    candidates = [("original_left_derivative",up(saved["eta_plus"]*saved["J1"])),
        ("complete_identity_minus_LJ",up(1+saved["l"][0]*saved["J0"]))]
    choice = whole_choice(candidates)
    BJ = ball(choice["complete_selected_upper"]).upper()
    R1, R2 = up(P0*L[1]), up(P0*L[2])
    brackets = {
        "-5/2":[ex(1),R2,up(R2*R1),up(BJ*R2*R1*R1)],
        "-11/6":[ex(1),R1,up(BJ*R1*R1)],
        "-7/6":[ex(1),R1,up(BJ*R1*R1)],
        "-1/2":[ex(1),up(BJ*R1)]}
    outputs = {"-5/2":["-3/2","-1/2","1/2"],
        "-11/6":["-5/6","1/6"],"-7/6":["-1/6","5/6"],"-1/2":["1/2"]}
    bounds, rows = {}, {}
    for q in Q_WINDOWS:
        bounds[q] = up(P0*upper_sum(brackets[q]))
        rows[q] = dict(input_exponent=q,output_exponent=str(Fraction(q)+1),
            intermediate_R_output_exponents=outputs[q],
            complete_positive_bracket_terms=brackets[q],
            complete_J_one_gain_upper=bounds[q])
    report = dict(complete_P0_upper=P0,complete_BJ_whole_choice=choice,
        complete_R1_upper=R1,complete_R2_upper=R2,windows=rows,
        exact_L2_inverse="(Id+L eta^-1 I)^-1 = eta partial_phi J",
        J_is_same_direction_old_inverse_not_the_adjoint_inverse=True,
        left_derivative_identity_retained=True,
        independent_physical_means_not_in_J_domain=True)
    return bounds, encoded(report)

def complete_weighted_R0(saved, geometry):
    values, rows = {}, {}
    for q in Q_WINDOWS:
        values[q], rows[q] = {}, {}
        for cutoff in (1,97):
            weights = [band_weight(geometry,B,cutoff,Fraction(q)) for B in BANDS]
            terms = [up(w*r) for w,r in zip(weights,saved["R0_terms"])]
            bound = upper_sum(terms)
            values[q][cutoff] = bound
            rows[q][str(cutoff)] = dict(input_exponent=q,output_exponent=q,
                input_cutoff_abs_j=97,output_cutoff_abs_j=cutoff,
                complete_positive_weights=weights,complete_weighted_terms=terms,
                complete_R0_upper=bound,complete_positive_mean_rank=terms[7],
                original_eight_terms_all_retained=True)
    report = dict(complete_kernel_bandwidths=list(BANDS),windows=rows,
        exact_positive_A0_kernel_algorithm_qualification=True,
        internal_mean_rank_has_complete_convolution_majorant=True,
        ordinary_operator_norm_alone_not_used_to_infer_weighted_kernel=True,
        independent_physical_means_retained=True)
    return values, encoded(report)

def complete_amplitude_gains(saved, geometry):
    rho = geometric_power(geometry,"rho97|1/3",1+16*97*97,Fraction(1,3))
    chi = up(rho*saved["n_minus_two_thirds"])
    geometry["values"]["rho"] = rho
    geometry["values"]["chi"] = chi
    geometry["records"]["complete_rho_upper"] = rec(rho)
    geometry["records"]["complete_chi_upper"] = rec(chi)
    values, rows = {}, {}
    for q in Q_WINDOWS:
        target = Fraction(q)+Fraction(2,3)
        weight = band_weight(geometry,384,97,target)
        terms = [up(rho*weight*saved["amplitude_terms"][0]),
                 up(rho*saved["amplitude_terms"][1])]
        values[q] = upper_sum(terms)
        rows[q] = dict(input_exponent=q,output_exponent=str(target),
            complete_high_high_weight_upper=weight,
            complete_positive_gain_terms=terms,complete_amplitude_gain_upper=values[q])
    report = dict(windows=rows,input_and_output_cutoff_abs_j=97,
        old_two_amplitude_terms_are_complete_positive_algorithm_bounds=True,
        input_frequency_powers_retained_on_the_right=True,
        physical_frequency_monotonicity_used_only_for_the_two_saved_powers=True,
        no_unweighted_column_norm_promoted_without_kernel_identity=True)
    return values, encoded(report)

def complete_stable_gains(saved, L, J, R0, amplitude, geometry):
    orders={"-5/2":3,"-11/6":2,"-7/6":2,"-1/2":1}
    values, rows = {}, {}
    for q in Q_WINDOWS:
        primitive = up(R0[q][1]/4)
        input_sum = upper_sum([saved["leading_I"],primitive])
        JL = up(J[q]*L[orders[q]])
        terms = [amplitude[q],
            up(geometry["values"]["chi"]*R0[q][97]/saved["eta_minus"]),
            up(JL*input_sum/saved["eta_minus"])]
        values[q] = upper_sum(terms)
        rows[q] = dict(input_exponent=q,output_exponent=str(Fraction(q)+Fraction(2,3)),
            L_integer_order=orders[q],complete_full_IR0_upper=primitive,
            complete_leading_plus_IR0_upper=input_sum,complete_ordered_JL_upper=JL,
            complete_three_positive_error_terms=terms,complete_error_gain_upper=values[q],
            original_low_intermediate_one_quarter_retained=True)
    report = dict(windows=rows,
        exact_order="P_H E2 - eta^-1 P_H N_out^-2/3 R0 + P_H Z N_out^1/3 J L eta^-1 I R",
        J_and_L_not_given_a_finite_output_band=True,
        all_original_input_diagonals_remain_on_their_original_side=True,
        internal_mean_rank_and_both_physical_means_retained=True,
        final_N_one_third_reads_Hqplus1_to_Hqplus2over3=True)
    return values, encoded(report)

def complete_natural_inverses(saved, gains, geometry):
    Broot = up(1+saved["e_upper"]/saved["margin_lower"])
    a = {q:up(gains[q]/saved["g_minus"]) for q in Q_WINDOWS}
    chains={"-7/6":["-7/6","-1/2"],
        "-5/2":["-5/2","-11/6","-7/6","-1/2"]}
    rows={}
    for target,chain in chains.items():
        terms=[ex(1)]
        product=ex(1)
        for index,q in enumerate(chain):
            product=up(product*a[q])
            if index+1<len(chain):
                terms.append(product)
        terms.append(up(Broot*product))
        B=upper_sum(terms)
        Shat=up(B/saved["g_minus"])
        Snat=up(geometry["values"]["sqrt67"]*Shat)
        rows[target]=dict(input_and_output_exponent=target,
            ordered_gain_windows=chain,terminal_exponent="1/6",
            complete_finite_inverse_polynomial_terms=terms,complete_B_upper=B,
            complete_Shat_inverse_upper=Shat,complete_Snat_inverse_upper=Snat,
            same_distributional_inverse_as_original_L2=True)
    report=dict(complete_Broot_upper=Broot,complete_A_gain_upper=a,windows=rows,
        saved_margin_is_read_directly_no_old_strict_comparison_repeated=True,
        exact_order="(Id+D_g^-1 E)^-1 D_g^-1 M^-1",
        uniform_real_delta_family_only=True,
        two_natural_negative_windows_certified=True,
        selected_common_input_inverse_left_factor_remains_separate=True,
        true_Riccati_operator_norm_continuity_claimed=False,
        uniform_selected_chart_family_claimed=False,
        complete_incoming_inverse_claimed=False,finite_Schur_inverse_claimed=False,
        independent_physical_means_retained=True)
    return encoded(report)


def sha(data):
    return hashlib.sha256(data).hexdigest()

def git_blob(data):
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False)+"\n").encode("utf-8")

def persist(path, doc):
    raw = canonical(doc)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".atomic")
    with temporary.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)
    return raw

def print_complete_document(doc):
    print("BEGIN_COMPLETE_ROOT_NATURAL_NEGATIVE_WINDOW_SCIENCE_JSON",flush=True)
    print(canonical(doc).decode("utf-8"),end="",flush=True)
    print("END_COMPLETE_ROOT_NATURAL_NEGATIVE_WINDOW_SCIENCE_JSON",flush=True)

def gate(doc, index, condition):
    passed = bool(condition)
    doc["gates"].append(dict(name=GATE_NAMES[index],passed=passed))
    if not passed:
        raise ValueError("failed RNE structural gate: "+GATE_NAMES[index])

def require(condition, message):
    if not condition:
        raise ValueError(message)

def literal_old_constants(text):
    wanted={"KIND","RUNTIME","PARAMETERS","RETAINED_SCOPE","COUNTS",
        "COMPLETE_FIELDS","GATE_NAMES","SUCCESS_ACTUAL_PROGRESS","PIN_SPECS",
        "PRESERVED_PREFIX_EVIDENCE","PRESERVED_OBJECT_HASHES"}
    result={}
    for node in ast.parse(text).body:
        if isinstance(node,ast.Assign) and len(node.targets)==1:
            target=node.targets[0]
            if isinstance(target,ast.Name) and target.id in wanted:
                result[target.id]=ast.literal_eval(node.value)
    require(set(result)==wanted,"old source literal identity is incomplete")
    return result

def positive_new_records(value):
    if isinstance(value,dict):
        return all(positive_new_records(v) for v in value.values())
    if isinstance(value,(list,tuple)):
        return all(positive_new_records(v) for v in value)
    if isinstance(value,str):
        numeric=re.fullmatch(r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?",value)
        if value.startswith("[") or numeric:
            v=ball(value)
            return bool(v.is_finite() and v.lower()>=0)
        if value.lower() in ("nan","inf","+inf","-inf","indeterminate"):
            return False
    return True

def checked_inputs(args, doc):
    runtime={"Python":platform.python_version(),
             "python_flint":importlib.metadata.version("python-flint")}
    doc["runtime"]=runtime
    gate(doc,0,os.environ.get("GITHUB_ACTIONS")=="true"
        and os.environ.get("GITHUB_REPOSITORY")==PUBLIC
        and runtime==RUNTIME and args.bits==ctx.prec==PARAMETERS["arithmetic_bits"]
        and re.fullmatch(r"[0-9a-f]{40}",doc["actual_scientific_checkout_commit"] or "") is not None
        and doc["input_manifest_sha256"]==args.manifest_sha)
    manifest=json.loads(args.manifest.read_bytes())
    expected_paths={"source":SOURCE,"worker":WORKER,"rules":RULES["path"]}
    expected_paths.update({key:entry["path"] for key,entry in PIN_SPECS.items()})
    entries=manifest.get("files",[])
    by_role={entry.get("role"):entry for entry in entries}
    gate(doc,1,manifest.get("kind")==MANIFEST_KIND
        and manifest.get("public_repository")==PUBLIC
        and manifest.get("source_path")==SOURCE
        and manifest.get("source_sha256")==doc["source_sha256"]
        and manifest.get("parameters")==PARAMETERS
        and manifest.get("scope")==RETAINED_SCOPE
        and manifest.get("publication_limits")==PUBLICATION_LIMITS
        and manifest.get("expected_actual_gate_count")==GATE_COUNT
        and manifest.get("expected_immutable_AST_files")==3
        and manifest.get("expected_current_input_count")==9
        and manifest.get("expected_input_count")==9
        and len(entries)==len(by_role)==9 and set(by_role)==set(expected_paths)
        and manifest.get("input_paths")==expected_paths
        and manifest.get("current_text_input_roles")==list(expected_paths)
        and manifest.get("current_input_paths")==list(expected_paths.values())
        and manifest.get("all_inputs_are_current_small_texts") is True
        and manifest.get("historical_inputs")==[]
        and manifest.get("legacy_artifact_inputs")==[]
        and manifest.get("old_successful_scientific_calls_allowed") is False
        and manifest.get("new_native_arrays_or_artifact_persistence_allowed") is False)
    paths={role:args.repo/Path(path) for role,path in expected_paths.items()}
    verified={}
    for role,path in paths.items():
        entry=by_role[role]
        data=path.read_bytes()
        require(entry["path"]==expected_paths[role],"current path changed")
        require(0<len(data)<100000 and path.suffix in (".py",".json",".md"),
                "current small text qualification")
        data.decode("utf-8")
        require(not data.startswith(b"\x1f\x8b"),"no gzip input in RNE")
        require(len(data)==entry["bytes"] and sha(data)==entry["sha256"]
            and git_blob(data)==entry["git_blob"],"complete current identity mismatch: "+role)
        if role in PIN_SPECS:
            require({k:entry[k] for k in ("path","git_blob","bytes","sha256")}==PIN_SPECS[role],
                    "mathematical pin changed: "+role)
            verified[role]={"bytes":len(data),"sha256":sha(data)}
        if role=="rules":
            require(all(entry[k]==RULES[k] for k in ("path","git_blob","bytes","sha256")),
                    "reviewed rules identity changed")
    input_sha={role:entry["sha256"] for role,entry in PIN_SPECS.items()}
    input_sha["manifest"]=doc["input_manifest_sha256"]
    doc["input_sha256"]=input_sha
    doc["verified_original_inputs"]=verified
    contract=paths["contract"].read_text()
    rni=paths["rni_contract"].read_text()
    gate(doc,2,len(verified)==6
        and manifest.get("complete_input_bytes")==sum(entry["bytes"] for entry in entries)
        and manifest.get("file_sha256")=={entry["path"]:entry["sha256"] for entry in entries}
        and manifest.get("mathematical_input_sha256")=={k:v["sha256"] for k,v in PIN_SPECS.items()}
        and all(tag in contract for tag in (r"\tag{RNE.6}",r"\tag{RNE.17}",r"\tag{RNE.22}",r"\tag{RNE.26}"))
        and all(tag in rni for tag in (r"\tag{RNI.9}",r"\tag{RNI.14}",r"\tag{RNI.15}"))
        and by_role["source"]["sha256"]==sha(Path(__file__).read_bytes()))
    return manifest,paths

def accepted_R97R(paths, doc):
    raw=paths["saved_science"].read_bytes()
    science=json.loads(raw)
    execution=json.loads(paths["saved_execution"].read_bytes())
    manifest=json.loads(paths["saved_manifest"].read_bytes())
    original=literal_old_constants(paths["saved_source"].read_text())
    wanted_scientific_conclusion=dict(actual_gate_count=9,actual_passed_gate_count=9,
        actual_returncode=0,bytes=OLD["science_bytes"],complete=True,
        file="actual-scientific-conclusion.json",
        original_result_printed_before_any_format_gate=True,sha256=OLD["science_sha256"])
    gate(doc,3,len(raw)==OLD["science_bytes"] and sha(raw)==OLD["science_sha256"]
        and canonical(science)==raw
        and science.get("kind")==original["KIND"]==OLD["kind"]
        and execution.get("kind")==OLD["execution_kind"]
        and manifest.get("kind")==OLD["manifest_kind"]
        and science.get("run_id")==execution.get("run_id")==OLD["run_id"]
        and science.get("run_attempt")==execution.get("run_attempt")==OLD["run_attempt"]
        and science.get("workflow_event_commit")==execution.get("workflow_commit")==OLD["workflow_event_commit"]
        and science.get("actual_scientific_checkout_commit")
            ==execution.get("actual_scientific_checkout_commit")==OLD["actual_scientific_checkout_commit"]
        and science.get("source_sha256")==execution.get("source_sha256")==manifest.get("source_sha256")==OLD["source_sha256"]
        and science.get("input_manifest_sha256")==execution.get("input_manifest_sha256")==OLD["input_manifest_sha256"]
        and execution.get("worker_source_sha256")==OLD["worker_sha256"]
        and science.get("runtime")==execution.get("actual_scientific_runtime")==original["RUNTIME"]==OLD["runtime"]
        and science.get("arithmetic_bits")==320
        and execution.get("complete") is True and execution.get("actual_returncode")==0
        and execution.get("actual_failure") is None
        and execution.get("actual_new_scientific_processes")==1
        and execution.get("scientific_conclusion")==wanted_scientific_conclusion
        and any(row.get("file")=="actual-scientific-conclusion.json"
            and row.get("bytes")==OLD["science_bytes"] and row.get("sha256")==OLD["science_sha256"]
            for row in execution.get("output_hashes",[])))
    old_files=manifest["files"]
    old_receipts=[dict(role=row["role"],path=row["path"],bytes=row["bytes"],sha256=row["sha256"],
        origin="exact_current_small_text") for row in old_files]
    old_map={k:v["sha256"] for k,v in original["PIN_SPECS"].items()}
    old_verified={k:{"bytes":v["bytes"],"sha256":v["sha256"]} for k,v in original["PIN_SPECS"].items()}
    op=science["complete_ordered_operator_conclusion"]
    gate(doc,4,science.get("complete") is True and science.get("proved") is True
        and science.get("actual_returncode")==0 and science.get("failure") is None and science.get("stage")=="complete"
        and set(science)==set(original["COMPLETE_FIELDS"]) and len(science)==35
        and science.get("parameters")==original["PARAMETERS"]==manifest["parameters"]
        and science.get("retained_scope")==original["RETAINED_SCOPE"]==manifest["scope"]
        and science.get("counts")==original["COUNTS"]
        and science.get("gates")==[dict(name=label,passed=True) for label in original["GATE_NAMES"]]
        and len(science["gates"])==9
        and science.get("actual_progress")==original["SUCCESS_ACTUAL_PROGRESS"]
        and science["actual_progress"]["completed_original_cutoff97_comparisons"]==1
        and science["original_cutoff97_sufficient_gate_passed"] is True
        and op["original_cutoff97_sufficient_gate_passed"] is True
        and op["root_stable_injectivity_certified"] is True
        and op["same_window_onto_only_with_original_SE_identity"] is True
        and op["strict_comparison_uses_retained_75_digit_ball_endpoints"] is True
        and op["negative_window_numerical_inverse_claimed"] is False
        and op["complete_incoming_inverse_claimed"] is False
        and op["finite_Schur_inverse_claimed"] is False
        and op["physical_independent_means_retained"] is True
        and op["full_IR0_norm_is_not_high_cut"] is True
        and science.get("input_sha256")==dict(manifest=OLD["input_manifest_sha256"],**old_map)
        and science.get("verified_original_inputs")==old_verified
        and manifest["mathematical_input_sha256"]==execution["mathematical_input_sha256"]==old_map
        and execution["actual_original_Git_input_receipts"]==old_receipts
        and sha(canonical(old_receipts))==execution["actual_verified_Git_input_receipts_sha256"]==OLD["input_receipts_sha256"]
        and execution["actual_verified_Git_input_count"]==OLD["input_receipt_count"]==9
        and execution["complete_immutable_Python_AST_closure_passed"] is True
        and execution["complete_immutable_Python_AST_file_count"]==OLD["AST_file_count"]==3
        and execution["complete_immutable_Python_AST_inventory_sha256"]==OLD["AST_inventory_sha256"]
        and sha(canonical(science["preserved_prefix_evidence"]))==OLD["prefix_evidence_sha256"]
        and science["preserved_prefix_evidence"]==original["PRESERVED_PREFIX_EVIDENCE"]
        and all(sha(canonical(science[k]))==v for k,v in original["PRESERVED_OBJECT_HASHES"].items())
        and all(execution.get(k)==0 for k in ("old_artifacts_downloaded","old_binary_parts_restored",
            "old_flow_root_mean_or_Airy_recomputations","old_numerical_enclosures_recomputed",
            "old_producers_or_integrals_reexecuted","saved_mixed_selections_recomputed","saved_root_domain_recomputed"))
        and execution.get("complete_original_input_array_recomputation") is False
        and execution.get("complete_mathematical_receipt_available") is True
        and execution.get("complete_atomic_scientific_result_reprinted") is True)
    domain=science["complete_root_domain_conclusion"]
    inverse=science["copied_old_inputs"]["root_inverse"]
    copied=dict(root_domain=domain,root_inverse=inverse,ordered_operator=op,
        original_scope=science["retained_scope"])
    records=dict(eta_minus=domain["eta_low"],eta_plus=domain["eta"][0],J0=domain["J0"],J1=domain["J1"],
        l=inverse["L_derivative_commutator_bounds"],amplitude_terms=op["amplitude_two_terms"],
        R0_terms=op["R0_eight_complete_terms"],leading_I=op["high_leading_primitive_upper"],
        n_minus_two_thirds=op["right_input_powers"]["-2/3"],g_minus=op["genuine_diagonal_lower"],
        e_upper=op["complete_stable_error_upper"],margin_lower=op["strict_margin"])
    require(len(records["l"])==4 and all(isinstance(x,dict) and set(x)=={"ball"} for x in records["l"]),
        "four original commutator ball objects must remain complete")
    require(len(records["amplitude_terms"])==2 and len(records["R0_terms"])==8,
        "complete original positive term arrays")
    saved={}
    lower_keys={"eta_minus","g_minus","margin_lower"}
    for key,value in records.items():
        if key in ("l","amplitude_terms","R0_terms"):
            saved[key]=[up(x) for x in value]
        elif key in lower_keys:
            v=ball(value)
            require(v.is_finite() and v.lower()>0,"missing saved strict positive lower: "+key)
            saved[key]=v.lower()
        else:
            saved[key]=up(value)
    accepted=copy.deepcopy(EXPECTED_ACCEPTED_OLD_INPUTS)
    require(accepted["parameters_read_verbatim"]==science["parameters"]
        and accepted["complete_old_gates_read_verbatim"]==science["gates"]
        and accepted["actual_progress_read_verbatim"]==science["actual_progress"],
        "accepted original summary is not the exact saved metadata")
    doc["accepted_old_inputs"]=accepted
    doc["complete_original_objects_read_verbatim"]=copy.deepcopy(copied)
    doc["complete_original_objects_sha256"]=sha(canonical(copied))
    doc["complete_saved_scalar_records_read_verbatim"]=copy.deepcopy(records)
    doc["complete_saved_scalar_records_sha256"]=sha(canonical(records))
    gate(doc,5,len(copied)==4 and len(records)==12
        and doc["complete_original_objects_sha256"]==OLD["complete_objects_sha256"]
        and doc["complete_saved_scalar_records_sha256"]==OLD["scalar_records_sha256"]
        and all(ball(x).is_finite() and ball(x).lower()>=0
            for v in records.values() for x in (v if isinstance(v,list) else [v]))
        and sum(len(v) if isinstance(v,list) else 1 for v in records.values())==23
        and op["complete_positive_mean_rank"]==op["R0_eight_complete_terms"][7]
        and op["E2_upper"]==op["complete_unprojected_amplitude_upper"])
    doc["actual_progress"]["accepted_same_R97R_success"]=True
    return saved


NEW_GRAPH_FIELDS = (
    "complete_geometry_conclusion","complete_L_commutator_conclusion",
    "complete_J_gain_conclusion","complete_weighted_R0_conclusion",
    "complete_amplitude_gain_conclusion","complete_stable_gain_conclusion",
    "complete_natural_inverse_conclusion")

def complete_shape_counts(doc):
    L=doc["complete_L_commutator_conclusion"]
    J=doc["complete_J_gain_conclusion"]
    R=doc["complete_weighted_R0_conclusion"]
    A=doc["complete_amplitude_gain_conclusion"]
    E=doc["complete_stable_gain_conclusion"]
    N=doc["complete_natural_inverse_conclusion"]
    G=doc["complete_geometry_conclusion"]
    return (
        len(L["complete_integer_Sobolev_bounds"])==4
        and len(J["complete_BJ_whole_choice"]["complete_candidate_records"])==2
        and set(J["windows"])==set(R["windows"])==set(A["windows"])==set(E["windows"])==set(Q_WINDOWS)
        and all(set(R["windows"][q])=={"1","97"} for q in Q_WINDOWS)
        and sum(len(row["complete_weighted_terms"]) for q in Q_WINDOWS
            for row in R["windows"][q].values())==64
        and sum(len(row["complete_positive_gain_terms"]) for row in A["windows"].values())==8
        and sum(len(row["complete_three_positive_error_terms"]) for row in E["windows"].values())==12
        and set(N["windows"])=={"-7/6","-5/2"}
        and sum(len(row["complete_finite_inverse_polynomial_terms"]) for row in N["windows"].values())==8
        and len(G["fixed_square_roots"])==4
        and len(G["positive_geometric_powers"])==26)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--manifest",type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True)
    parser.add_argument("--bits",type=int,default=320)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    if args.out.exists():
        raise FileExistsError("refusing to overwrite an existing complete or partial scientific result")
    ctx.prec=args.bits
    doc={key:None for key in COMPLETE_FIELDS}
    doc.update(kind=KIND,complete=False,proved=False,actual_returncode=None,failure=None,
        stage="initial_current_input_admission",source_sha256=sha(Path(__file__).read_bytes()),
        input_manifest_sha256=sha(args.manifest.read_bytes()),public_repository=PUBLIC,
        run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        runtime={},arithmetic_bits=args.bits,parameters=copy.deepcopy(PARAMETERS),
        input_sha256={},verified_original_inputs={},accepted_old_inputs={},
        complete_original_objects_read_verbatim={},complete_original_objects_sha256=None,
        complete_saved_scalar_records_read_verbatim={},complete_saved_scalar_records_sha256=None,
        retained_scope=copy.deepcopy(RETAINED_SCOPE),planned_shape=copy.deepcopy(PLANNED_SHAPE),
        actual_progress=copy.deepcopy(INITIAL_ACTUAL_PROGRESS),gates=[],
        actual_mathematical_wall_seconds=0)
    began=time.monotonic()
    try:
        manifest,paths=checked_inputs(args,doc)
        doc["stage"]="complete_saved_R97R_admission"
        saved=accepted_R97R(paths,doc)
        persist(args.out,doc)

        doc["stage"]="complete_new_L_commutator_conclusion"
        geometry=start_geometry(doc)
        L,report=complete_L_bounds(saved,geometry)
        doc["complete_L_commutator_conclusion"]=report
        doc["actual_progress"]["new_commutator_bounds_completed"]=4
        gate(doc,6,report["integer_orders"]==[0,1,2,3]
            and len(report["complete_integer_Sobolev_bounds"])==4
            and [len(row) for row in report["complete_positive_terms"]]==[1,2,3,4]
            and positive_new_records(report))
        persist(args.out,doc)

        doc["stage"]="complete_new_J_gain_conclusion"
        J,report=complete_J_gains(saved,L,geometry)
        doc["complete_J_gain_conclusion"]=report
        doc["actual_progress"]["new_complete_J_candidates_completed"]=2
        doc["actual_progress"]["new_same_direction_J_windows_completed"]=4
        doc["actual_progress"]["new_complete_whole_choices"]=1
        choice=report["complete_BJ_whole_choice"]
        gate(doc,7,set(report["windows"])==set(Q_WINDOWS)
            and len(choice["complete_candidate_records"])==2
            and choice["complete_selected_upper"]==choice["complete_candidate_records"][choice["selected_complete_candidate"]]
            and [len(report["windows"][q]["complete_positive_bracket_terms"]) for q in Q_WINDOWS]==[4,3,3,2]
            and report["J_is_same_direction_old_inverse_not_the_adjoint_inverse"] is True
            and positive_new_records(report))
        persist(args.out,doc)

        doc["stage"]="complete_new_weighted_R0_conclusion"
        R0,report=complete_weighted_R0(saved,geometry)
        doc["complete_weighted_R0_conclusion"]=report
        doc["actual_progress"]["new_weighted_R0_routes_completed"]=8
        gate(doc,8,report["complete_kernel_bandwidths"]==list(BANDS)
            and set(report["windows"])==set(Q_WINDOWS)
            and all(set(report["windows"][q])=={"1","97"} for q in Q_WINDOWS)
            and all(len(row["complete_weighted_terms"])==len(row["complete_positive_weights"])==8
                and row["complete_positive_mean_rank"]==row["complete_weighted_terms"][7]
                and row["original_eight_terms_all_retained"] is True
                for q in Q_WINDOWS for row in report["windows"][q].values())
            and positive_new_records(report))
        persist(args.out,doc)

        doc["stage"]="complete_new_amplitude_gain_conclusion"
        amplitude,report=complete_amplitude_gains(saved,geometry)
        doc["complete_amplitude_gain_conclusion"]=report
        doc["actual_progress"]["new_amplitude_gain_windows_completed"]=4
        gate(doc,9,set(report["windows"])==set(Q_WINDOWS)
            and all(len(row["complete_positive_gain_terms"])==2 for row in report["windows"].values())
            and report["input_and_output_cutoff_abs_j"]==97
            and report["input_frequency_powers_retained_on_the_right"] is True
            and positive_new_records(report))
        persist(args.out,doc)

        doc["stage"]="complete_new_stable_gain_conclusion"
        gains,report=complete_stable_gains(saved,L,J,R0,amplitude,geometry)
        doc["complete_stable_gain_conclusion"]=report
        doc["actual_progress"]["new_stable_gain_windows_completed"]=4
        gate(doc,10,set(report["windows"])==set(Q_WINDOWS)
            and all(len(report["windows"][q]["complete_three_positive_error_terms"])==3
                and report["windows"][q]["complete_three_positive_error_terms"][0]
                    ==doc["complete_amplitude_gain_conclusion"]["windows"][q]["complete_amplitude_gain_upper"]
                and report["windows"][q]["original_low_intermediate_one_quarter_retained"] is True
                for q in Q_WINDOWS)
            and report["J_and_L_not_given_a_finite_output_band"] is True
            and report["internal_mean_rank_and_both_physical_means_retained"] is True
            and positive_new_records(report))
        persist(args.out,doc)

        doc["stage"]="complete_new_natural_inverse_conclusion"
        report=complete_natural_inverses(saved,gains,geometry)
        doc["complete_natural_inverse_conclusion"]=report
        doc["actual_progress"]["new_natural_inverse_windows_completed"]=2
        gate(doc,11,set(report["windows"])=={"-7/6","-5/2"}
            and [len(report["windows"][q]["complete_finite_inverse_polynomial_terms"])
                for q in ("-7/6","-5/2")]==[3,5]
            and report["saved_margin_is_read_directly_no_old_strict_comparison_repeated"] is True
            and report["independent_physical_means_retained"] is True
            and report["selected_common_input_inverse_left_factor_remains_separate"] is True
            and positive_new_records(report))
        persist(args.out,doc)

        doc["stage"]="complete_final_readonly_and_schema_checks"
        gate(doc,12,all(sha(paths[row["role"]].read_bytes())==row["sha256"] for row in manifest["files"])
            and sha(args.manifest.read_bytes())==doc["input_manifest_sha256"]==args.manifest_sha
            and sha(canonical(doc["complete_original_objects_read_verbatim"]))==OLD["complete_objects_sha256"]
            and sha(canonical(doc["complete_saved_scalar_records_read_verbatim"]))==OLD["scalar_records_sha256"]
            and all(doc["actual_progress"][key]==0 for key in
                ("old_scientific_targets_recomputed","old_R97_root_graphs_recomputed",
                 "old_R97_strict_comparisons_reevaluated","historical_inputs_restored")))
        gate(doc,13,all(isinstance(doc[key],dict) and positive_new_records(doc[key]) for key in NEW_GRAPH_FIELDS))
        gate(doc,14,doc["planned_shape"]==PLANNED_SHAPE
            and doc["actual_progress"]==SUCCESS_ACTUAL_PROGRESS
            and complete_shape_counts(doc))
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-began
        gate(doc,15,set(doc)==set(COMPLETE_FIELDS) and len(doc)==35
            and doc["retained_scope"]==RETAINED_SCOPE
            and len(doc["gates"])==15
            and [row["name"] for row in doc["gates"]]==GATE_NAMES[:15]
            and all(row["passed"] is True for row in doc["gates"])
            and doc["parameters"]==PARAMETERS)
        doc.update(complete=True,proved=True,actual_returncode=0,failure=None,stage="complete")
    except BaseException as error:
        doc.update(complete=False,proved=False,actual_returncode=1,
            failure={"type":type(error).__name__,"message":str(error),"traceback":traceback.format_exc()},
            actual_mathematical_wall_seconds=time.monotonic()-began)
        doc["failed_new_stage_diagnostic"]={
            "stage":doc["stage"],
            "complete_saved_admission_passed":doc["actual_progress"]["accepted_same_R97R_success"],
            "returned_graph_fields_available":[key for key in NEW_GRAPH_FIELDS if isinstance(doc.get(key),dict)],
            "old_targets_not_recomputed":True,
            "old_root97_comparison_not_reevaluated":True,
            "new_negative_window_conclusion_authorized":False}
        persist(args.out,doc)
        print_complete_document(doc)
        raise
    raw=persist(args.out,doc)
    print_complete_document(doc)
    if len(raw)>COMPLETE_SCIENCE_MAX_BYTES:
        raise ValueError("complete scientific result saved and printed; publication byte budget exceeded")

if __name__=="__main__":
    main()
