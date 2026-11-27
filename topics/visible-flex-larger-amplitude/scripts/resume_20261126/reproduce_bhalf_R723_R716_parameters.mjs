#!/usr/bin/env node
// Complete reversible parameters only: no science, import, AST or fixture.
// Exact original argv, domain, budgets and original selector maps remain recorded.
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
const SPEC={
  "schema": "complete-bhalf-R723-R716-parameter-reproduction-v1",
  "parent": {
    "name": "fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
    "bytes": 80089,
    "sha256": "3b49bd1b12b6b5680fd63a6cd8a5e8c34633626c875044a50ba98b6b1174441a",
    "git_blob_sha": "7d748fcb2ca892ce50c23d0153c198f99fc307db"
  },
  "output": {
    "name": "fixed-fejer-meridian-batched-bhalf-first-R723-complete-R716-moment-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R723-complete-R716-moment-ready.json",
    "bytes": 97718,
    "sha256": "11667d388e2d71d7583891aac274cfe7ea71810b123f9262f4a8ed85e90986c3",
    "git_blob_sha": "a5111bec896c7a83e598a9ea26f1372b80b309dc"
  },
  "operations": [
    {
      "path": [
        "schema"
      ],
      "before_present": true,
      "before": "prepared-fixed-fejer-meridian-bhalf-first-R722-complete-R716-closed-flux-centred-moments-v1",
      "after": "complete-fixed-fejer-bhalf-independent-R723-compatible-R716-moment-ready-v1"
    },
    {
      "path": [
        "complete_source_sha256",
        "fixed_fejer_R723_directional_closed_phase_grip_evidence.py"
      ],
      "before_present": false,
      "after": "1782eebd539ae47367260008c00b6a3912fe1fec26d30c22a8f0a7329a0309dc"
    },
    {
      "path": [
        "complete_source_sha256",
        "fixed_fejer_R723_compatible_r716_centred_volume_moment.py"
      ],
      "before_present": false,
      "after": "3c0d6cfd5280b7cb250b1a8ff2077c849a20f725169d0f667c74eb975c3c294b"
    },
    {
      "path": [
        "steps",
        1,
        "id"
      ],
      "before_present": true,
      "before": "actual-fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-centred-volume-moments-20261127",
      "after": "actual-fixed-fejer-bhalf-R723-compatible-complete-R716-centred-volume-moments-20261127"
    },
    {
      "path": [
        "steps",
        1,
        "script"
      ],
      "before_present": true,
      "before": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_r716_centred_volume_moment.py",
      "after": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_r716_centred_volume_moment.py"
    },
    {
      "path": [
        "steps",
        1,
        "scope"
      ],
      "before_present": true,
      "before": "Read and rebind all complete same-point moment blocks/journals/sources. Replay all12 channels, lower/flat-cap contributions, exact p4 volume/first/mixed moments and the full general R716(2) centred tensors at physical t=0,1/2,1. The simpler B_eff formula requires the actual all32-stage signed half-turn inclusion. Independently consume the FINAL complete producer_R722 closed-phase main report and its exact recorded sidecar; recheck every source/input/output and complete point/model/snapshot/target/normal identity, then replay complete geometry, ports, every support cell, independent unmarked tube and all8 original beta evidence roles. A provisional or incomplete closed report discharges nothing. Only actual full-body interpretation, positive total volume and a separated centred invariant enable the R625/R716 E(3)-quotient lower bound. R722 mean existence and R718 holding distance do not provide volume/noncongruence conclusions. No working F/J/root or accurate field oracle, conditional reach or overall completion claim is added.",
      "after": "Read and rebind every complete same-point moment block, original journal, full source and actual field identity. Retain all twelve raw channels, both half-surfaces and both flat caps, exact p4 volume/first/mixed moments, and the full general R716(2) centred tensors at physical t=0,1/2,1. The simplified B_eff formula remains conditional on the actual full 32-stage signed half-turn inclusion. Consume the exact final R723 closed-phase main report through its complete independent validator: re-read all original geometry streams and directional ranges, complete normal32/radial/circle covers, source-bound C2/phase ports, one common beta, actual full point/model/snapshot/target and original normal binding. The independently rederived UNMARKED flat-cap tube must strictly exceed mark height 1/1000 before any body/additivity interpretation. The old d0fe full eight-role validator is preserved only as an exact separately sourced legacy branch; this R723 route leaves those claims false and does not require the old R650 target to pass. Late-failed or provisional main/sidecar records discharge nothing. Only a full bounded-body interpretation, positive total volume and a separated centred invariant enable the unchanged R625/R716 E(3)-quotient formulas. R722 mean existence and R718 holding distance do not replace those premises. The original 45ca moment producer and its entire 600-second/all-angle budget are retained without modification. No new working F/J/root, accurate field oracle, conditional reach assumption, scientific solver or admission gate is added; no future actual field or fee value is supplied."
    },
    {
      "path": [
        "steps",
        1,
        "args",
        5
      ],
      "before_present": true,
      "before": "{work}/fixed-fejer-meridian-batched-bhalf-first-R722-r716-complete-centred-moments/report.json",
      "after": "{work}/fixed-fejer-meridian-batched-bhalf-first-R723-r716-complete-centred-moments/report.json"
    },
    {
      "path": [
        "steps",
        1,
        "args",
        7
      ],
      "before_present": true,
      "before": "{work}/fixed-fejer-meridian-batched-bhalf-first-R722-complete-closed-phase-grip-v1/report.json",
      "after": "{work}/fixed-fejer-meridian-batched-bhalf-first-R723-directional-closed-phase-grip-v1/report.json"
    },
    {
      "path": [
        "steps",
        1,
        "outputs",
        0
      ],
      "before_present": true,
      "before": "fixed-fejer-meridian-batched-bhalf-first-R722-r716-complete-centred-moments/report.json",
      "after": "fixed-fejer-meridian-batched-bhalf-first-R723-r716-complete-centred-moments/report.json"
    },
    {
      "path": [
        "steps",
        1,
        "summary"
      ],
      "before_present": true,
      "before": {
        "fixed-fejer-meridian-batched-bhalf-first-R722-r716-complete-centred-moments/report.json": {
          "schema": "schema",
          "source": "source_sha256",
          "producer_source": "complete_producer_source_sha256",
          "arithmetic_source": "arithmetic_source_sha256",
          "source_commit": "source_commit",
          "run": "github_run_id",
          "run_attempt": "github_run_attempt",
          "actual_moment_report": "actual_moment_report.sha256",
          "input_available": "actual_complete_moment_input_available",
          "actual_model": "actual_model_identity_sha256",
          "actual_point": "actual_current_full_point_sha256",
          "actual_snapshot": "actual_snapshot_identity_sha256",
          "target": "exact_fixed_target_identity_sha256",
          "complete_binding": "complete_binding_identity_sha256",
          "complete": "complete",
          "integral_complete": "full_domain_integral_input_complete",
          "positive_total_volume": "positive_complete_total_volume_separated_from_zero",
          "completed_circle_blocks": "actual_complete_circle_blocks",
          "expected_circle_blocks": "expected_complete_circle_blocks",
          "selected_half_turn_proved": "actual_half_turn_branch_test_passed",
          "volume_lower": "compact_actual_intervals.unmarked_volume_lower",
          "volume_upper": "compact_actual_intervals.unmarked_volume_upper",
          "A2_real_lower": "compact_actual_intervals.unmarked_A2_real_lower",
          "A2_real_upper": "compact_actual_intervals.unmarked_A2_real_upper",
          "A2_imag_lower": "compact_actual_intervals.unmarked_A2_imag_lower",
          "A2_imag_upper": "compact_actual_intervals.unmarked_A2_imag_upper",
          "A2_absolute_lower": "compact_actual_intervals.unmarked_A2_absolute_lower",
          "total_volume_lower": "compact_actual_intervals.total_volume_lower",
          "total_volume_upper": "compact_actual_intervals.total_volume_upper",
          "Beff_real_lower": "compact_actual_intervals.compensated_B_real_lower",
          "Beff_real_upper": "compact_actual_intervals.compensated_B_real_upper",
          "Beff_imag_lower": "compact_actual_intervals.compensated_B_imag_lower",
          "Beff_imag_upper": "compact_actual_intervals.compensated_B_imag_upper",
          "general_t_half_gap_lower": "compact_actual_intervals.t_half_I_squared_gap_lower",
          "general_t_half_gap_upper": "compact_actual_intervals.t_half_I_squared_gap_upper",
          "general_t_one_gap_lower": "compact_actual_intervals.t_one_I_squared_gap_lower",
          "general_t_one_gap_upper": "compact_actual_intervals.t_one_I_squared_gap_upper",
          "actual_geometry_proved": "complete_closed_image_or_embedding_or_global_outward_orientation_proved",
          "actual_external_tube": "fixed_marker_external_normal_tube_and_disjointness_proved",
          "physical_phase_proof": "same_field_exact_R248_phase_assembly_proof_consumed",
          "noncongruence_certificate": "unconditional_noncongruence_certificate",
          "working_calls": "existing_F_J_normal_root_calls",
          "accurate_field_calls": "accurate_field_oracle_calls",
          "actual_integrals_rechecked": "actual_interval_integral_arithmetic_rechecked",
          "elapsed_hex": "elapsed_seconds_binary64_hex",
          "reason": "reason",
          "problem_completed": "full_metric_reach_refinement_or_problem_completion_claimed",
          "closed_main_report": "closed_phase_evidence.complete_main_report.sha256",
          "closed_main_accepted": "closed_phase_evidence.final_main_report_accepted",
          "closed_sidecar": "closed_phase_evidence.complete_outward_tube_sidecar.sha256",
          "closed_inputs_outputs_rechecked": "closed_phase_evidence.actual_input_and_output_records_rechecked",
          "closed_all_support_rows": "closed_phase_evidence.all_original_geometry_support_cells_rechecked",
          "closed_original_eight_roles": "closed_phase_evidence.all_original_eight_beta_roles_and_radial_extension_rechecked",
          "actual_unmarked_reach": "closed_phase_evidence.actual_unmarked_all_phase_reach_lower",
          "actual_marked_reach": "closed_phase_evidence.actual_marked_all_phase_reach_lower",
          "actual_body_moment_interpretation": "actual_bounded_body_moment_interpretation_certified",
          "actual_delta_E_lower": "unconditional_delta_E_lower",
          "actual_delta_E_positive": "delta_E_positive_certified",
          "all_final_byte_rechecked": "all_bound_input_and_captured_evidence_bytes_rechecked",
          "mathematical_target": "mathematical_target_identity_sha256"
        }
      },
      "after": {
        "fixed-fejer-meridian-batched-bhalf-first-R723-r716-complete-centred-moments/report.json": {
          "schema": "schema",
          "source": "source_sha256",
          "producer_source": "complete_producer_source_sha256",
          "arithmetic_source": "arithmetic_source_sha256",
          "source_commit": "source_commit",
          "run": "github_run_id",
          "run_attempt": "github_run_attempt",
          "actual_moment_report": "actual_moment_report.sha256",
          "input_available": "actual_complete_moment_input_available",
          "actual_model": "actual_model_identity_sha256",
          "actual_point": "actual_current_full_point_sha256",
          "actual_snapshot": "actual_snapshot_identity_sha256",
          "target": "exact_fixed_target_identity_sha256",
          "complete_binding": "complete_binding_identity_sha256",
          "complete": "complete",
          "integral_complete": "full_domain_integral_input_complete",
          "positive_total_volume": "positive_complete_total_volume_separated_from_zero",
          "completed_circle_blocks": "actual_complete_circle_blocks",
          "expected_circle_blocks": "expected_complete_circle_blocks",
          "selected_half_turn_proved": "actual_half_turn_branch_test_passed",
          "volume_lower": "compact_actual_intervals.unmarked_volume_lower",
          "volume_upper": "compact_actual_intervals.unmarked_volume_upper",
          "A2_real_lower": "compact_actual_intervals.unmarked_A2_real_lower",
          "A2_real_upper": "compact_actual_intervals.unmarked_A2_real_upper",
          "A2_imag_lower": "compact_actual_intervals.unmarked_A2_imag_lower",
          "A2_imag_upper": "compact_actual_intervals.unmarked_A2_imag_upper",
          "A2_absolute_lower": "compact_actual_intervals.unmarked_A2_absolute_lower",
          "total_volume_lower": "compact_actual_intervals.total_volume_lower",
          "total_volume_upper": "compact_actual_intervals.total_volume_upper",
          "Beff_real_lower": "compact_actual_intervals.compensated_B_real_lower",
          "Beff_real_upper": "compact_actual_intervals.compensated_B_real_upper",
          "Beff_imag_lower": "compact_actual_intervals.compensated_B_imag_lower",
          "Beff_imag_upper": "compact_actual_intervals.compensated_B_imag_upper",
          "general_t_half_gap_lower": "compact_actual_intervals.t_half_I_squared_gap_lower",
          "general_t_half_gap_upper": "compact_actual_intervals.t_half_I_squared_gap_upper",
          "general_t_one_gap_lower": "compact_actual_intervals.t_one_I_squared_gap_lower",
          "general_t_one_gap_upper": "compact_actual_intervals.t_one_I_squared_gap_upper",
          "actual_geometry_proved": "complete_closed_image_or_embedding_or_global_outward_orientation_proved",
          "actual_external_tube": "fixed_marker_external_normal_tube_and_disjointness_proved",
          "physical_phase_proof": "same_field_exact_R248_phase_assembly_proof_consumed",
          "noncongruence_certificate": "unconditional_noncongruence_certificate",
          "working_calls": "existing_F_J_normal_root_calls",
          "accurate_field_calls": "accurate_field_oracle_calls",
          "actual_integrals_rechecked": "actual_interval_integral_arithmetic_rechecked",
          "elapsed_hex": "elapsed_seconds_binary64_hex",
          "reason": "reason",
          "problem_completed": "full_metric_reach_refinement_or_problem_completion_claimed",
          "closed_main_report": "closed_phase_evidence.complete_main_report.sha256",
          "closed_main_accepted": "closed_phase_evidence.final_main_report_accepted",
          "closed_sidecar": "closed_phase_evidence.complete_outward_tube_sidecar.sha256",
          "closed_inputs_outputs_rechecked": "closed_phase_evidence.actual_input_and_output_records_rechecked",
          "closed_all_support_rows": "closed_phase_evidence.all_original_geometry_support_cells_rechecked",
          "closed_original_eight_roles": "closed_phase_evidence.all_original_eight_beta_roles_and_radial_extension_rechecked",
          "actual_unmarked_reach": "closed_phase_evidence.actual_unmarked_all_phase_reach_lower",
          "actual_marked_reach": "closed_phase_evidence.actual_marked_all_phase_reach_lower",
          "actual_body_moment_interpretation": "actual_bounded_body_moment_interpretation_certified",
          "actual_delta_E_lower": "unconditional_delta_E_lower",
          "actual_delta_E_positive": "delta_E_positive_certified",
          "all_final_byte_rechecked": "all_bound_input_and_captured_evidence_bytes_rechecked",
          "mathematical_target": "mathematical_target_identity_sha256",
          "R723_route": "closed_phase_evidence.independent_directional_R723_route",
          "R723_full_domain_and_roles": "closed_phase_evidence.all_R723_directional_roles_and_original_full_domain_rechecked",
          "R723_old_eight_claims": "closed_phase_evidence.old_eight_role_certificate_claimed",
          "R723_legacy_target_required": "closed_phase_evidence.original_R650_target_pass_required",
          "R723_full_validation": "closed_phase_evidence.complete_R723_reconsumption_validation.all_bound_input_and_generated_output_bytes_rechecked"
        }
      }
    },
    {
      "path": [
        "complete_closed_phase_source_sha256"
      ],
      "before_present": true,
      "before": "002eb1b91c99ea212255d14a4e929e876e09f34c38c78ffb7fc4f806b8799c5f",
      "after": "1782eebd539ae47367260008c00b6a3912fe1fec26d30c22a8f0a7329a0309dc"
    },
    {
      "path": [
        "complete_closed_phase_main_report"
      ],
      "before_present": true,
      "before": "{work}/fixed-fejer-meridian-batched-bhalf-first-R722-complete-closed-phase-grip-v1/report.json",
      "after": "{work}/fixed-fejer-meridian-batched-bhalf-first-R723-directional-closed-phase-grip-v1/report.json"
    },
    {
      "path": [
        "complete_ports_support_unmarked_tube_and_original_beta_evidence_replayed"
      ],
      "before_present": true,
      "before": true,
      "after": false
    },
    {
      "path": [
        "complete_closed_phase_reference"
      ],
      "before_present": true,
      "before": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py",
      "after": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_directional_closed_phase_grip_evidence.py"
    },
    {
      "path": [
        "actual_source_specification"
      ],
      "before_present": true,
      "before": "Reuse the unchanged complete producer-bound source family driver10fa/reader8027/normal76185/packetc750, all137 scientific source roles and18 runtime files. This plan consumes only the genuine bhalf-first field and its own immutable point/fee inputs, never the original run18 input records or mutable observations. All R722 whole-cell validation, twelve moments, full cover and exact final closed-main evidence rules remain unchanged. New run, reference report, working model, point, packet, root, flux and delta_E values are unknown until actual Actions output.",
      "after": "Use all unchanged producer-bound 137 scientific roles and the same complete actual bhalf-first point. The entire original 45ca flux producer and f79c arithmetic are shared. The new complete 3c0d consumer preserves d0fe's exact original legacy validator and adds a separately source-pinned 1782 R723 validator; it never rewrites old eight-role claims. This plan names only future same-point original records, not prior run18 values or mutable progress. Every current original normal report, complete accurate stream, actual target and all twelve moments is re-read by its original full-source validator."
    },
    {
      "path": [
        "complete_parameter_correspondence"
      ],
      "before_present": true,
      "before": [
        {
          "parent_step_id": "actual-fixed-fejer-meridian-batched-producer-R722-complete-R716-whole-closed-flux-integrals-20261127",
          "current_step_id": "actual-fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-whole-closed-flux-integrals-20261127",
          "counts": {
            "argument_words": 10,
            "formal_summary_fields": 34,
            "live_fields": 0,
            "output_count": 1
          },
          "script_unchanged": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_complete_closed_surface_moment_integrals.py",
          "only_runner_namespace_step_id_and_current_scope_changed": true,
          "current_scope_before": "Consume the complete actual producer-bound R722 normal/physical-sixjet report for one genuinely recorded immutable complete-required-angle packet point of driver10fa4e4e, reader8027ec35, normal76185 and packetc750. Rebind all137 scientific source roles, the fixed Fejer target, all six actual input files, the full33-node/32-stage chain, every planned full-circle cell, every original922 radial cell and all actual support/profile/control splits and scalar tail. Re-read complete original R722 posterior source/theorem attribution, all active integral leaves, all three total-equation residuals and the whole-angle posterior root-domain inequalities. Retain the genuine original R709 sufficient-condition flag as true or false. Integrate all12 original interval flux channels and retain each completed atomic block. Missing coverage, mean proof or branch association keeps full-domain moments null. The original600-second budget and maximum-angle-blocks0 remain. Reflection and both flat caps are retained; parametric flux alone does not certify an embedded outward body. No working F/J/root or accurate field oracle is called.",
          "current_scope_after": "Consume the complete actual producer-bound R722 normal/physical-sixjet report for one genuinely recorded immutable complete-required-angle packet point of driver10fa4e4e, reader8027ec35, normal76185 and packetc750. Rebind all137 scientific source roles, the fixed Fejer target, all six actual input files, the full33-node/32-stage chain, every planned full-circle cell, every original922 radial cell and all actual support/profile/control splits and scalar tail. Re-read complete original R722 posterior source/theorem attribution, all active integral leaves, all three total-equation residuals and the whole-angle posterior root-domain inequalities. Retain the genuine original R709 sufficient-condition flag as true or false. Integrate all12 original interval flux channels and retain each completed atomic block. Missing coverage, mean proof or branch association keeps full-domain moments null. The original600-second budget and maximum-angle-blocks0 remain. Reflection and both flat caps are retained; parametric flux alone does not certify an embedded outward body. No working F/J/root or accurate field oracle is called.",
          "all_full_argument_tokens_preserved_except_namespace": true,
          "all_formal_and_live_selector_values_preserved": true
        },
        {
          "parent_step_id": "actual-fixed-fejer-meridian-batched-producer-R722-complete-R716-centred-volume-moments-20261127",
          "current_step_id": "actual-fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-centred-volume-moments-20261127",
          "counts": {
            "argument_words": 8,
            "formal_summary_fields": 60,
            "live_fields": 0,
            "output_count": 1
          },
          "script_unchanged": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_r716_centred_volume_moment.py",
          "only_runner_namespace_step_id_and_current_scope_changed": true,
          "current_scope_before": "Read and rebind all complete same-point moment blocks/journals/sources. Replay all12 channels, lower/flat-cap contributions, exact p4 volume/first/mixed moments and the full general R716(2) centred tensors at physical t=0,1/2,1. The simpler B_eff formula requires the actual all32-stage signed half-turn inclusion. Independently consume the FINAL complete producer_R722 closed-phase main report and its exact recorded sidecar; recheck every source/input/output and complete point/model/snapshot/target/normal identity, then replay complete geometry, ports, every support cell, independent unmarked tube and all8 original beta evidence roles. A provisional or incomplete closed report discharges nothing. Only actual full-body interpretation, positive total volume and a separated centred invariant enable the R625/R716 E(3)-quotient lower bound. R722 mean existence and R718 holding distance do not provide volume/noncongruence conclusions. No working F/J/root or accurate field oracle, conditional reach or overall completion claim is added.",
          "current_scope_after": "Read and rebind all complete same-point moment blocks/journals/sources. Replay all12 channels, lower/flat-cap contributions, exact p4 volume/first/mixed moments and the full general R716(2) centred tensors at physical t=0,1/2,1. The simpler B_eff formula requires the actual all32-stage signed half-turn inclusion. Independently consume the FINAL complete producer_R722 closed-phase main report and its exact recorded sidecar; recheck every source/input/output and complete point/model/snapshot/target/normal identity, then replay complete geometry, ports, every support cell, independent unmarked tube and all8 original beta evidence roles. A provisional or incomplete closed report discharges nothing. Only actual full-body interpretation, positive total volume and a separated centred invariant enable the R625/R716 E(3)-quotient lower bound. R722 mean existence and R718 holding distance do not provide volume/noncongruence conclusions. No working F/J/root or accurate field oracle, conditional reach or overall completion claim is added.",
          "all_full_argument_tokens_preserved_except_namespace": true,
          "all_formal_and_live_selector_values_preserved": true
        }
      ],
      "after": {
        "complete_original_ready": {
          "name": "fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
          "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
          "bytes": 80089,
          "sha256": "3b49bd1b12b6b5680fd63a6cd8a5e8c34633626c875044a50ba98b6b1174441a",
          "git_blob_sha": "7d748fcb2ca892ce50c23d0153c198f99fc307db"
        },
        "producer_entire_step_object_unchanged": true,
        "consumer_original_args": [
          "--repo",
          "{repo}",
          "--moment-report",
          "{work}/fixed-fejer-meridian-batched-bhalf-first-R722-r716-complete-moment-integrals/report.json",
          "--output",
          "{work}/fixed-fejer-meridian-batched-bhalf-first-R722-r716-complete-centred-moments/report.json",
          "--closed-phase-report",
          "{work}/fixed-fejer-meridian-batched-bhalf-first-R722-complete-closed-phase-grip-v1/report.json"
        ],
        "consumer_current_args": [
          "--repo",
          "{repo}",
          "--moment-report",
          "{work}/fixed-fejer-meridian-batched-bhalf-first-R722-r716-complete-moment-integrals/report.json",
          "--output",
          "{work}/fixed-fejer-meridian-batched-bhalf-first-R723-r716-complete-centred-moments/report.json",
          "--closed-phase-report",
          "{work}/fixed-fejer-meridian-batched-bhalf-first-R723-directional-closed-phase-grip-v1/report.json"
        ],
        "only_consumer_argv_changes": [
          {
            "index": 5,
            "purpose": "fresh R723 centred-moment output"
          },
          {
            "index": 7,
            "purpose": "exact optional R723 final closed report"
          }
        ],
        "all_other_flags_values_order_unchanged": true,
        "all_original_summary_maps_retained": true,
        "new_consumer_whole_source": {
          "name": "fixed_fejer_R723_compatible_r716_centred_volume_moment.py",
          "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_r716_centred_volume_moment.py",
          "bytes": 61706,
          "sha256": "3c0d6cfd5280b7cb250b1a8ff2077c849a20f725169d0f667c74eb975c3c294b",
          "git_blob_sha": "3ae6dd08dfcbb00002fa2482ec49cf7e56d86ea4"
        },
        "no_new_scientific_budget_or_gate": true,
        "all_parent_fields_held_either_as_current_unchanged_metadata_or_explicit_full_history": true
      }
    },
    {
      "path": [
        "complete_current_closed_adapter_proof"
      ],
      "before_present": true,
      "before": {
        "role": "closed_note",
        "name": "2026-11-27-producer-R722-closed-phase-grip-r718-source-adapter.md",
        "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-producer-R722-closed-phase-grip-r718-source-adapter.md",
        "bytes": 25302,
        "sha256": "6c96766bd966611895c4a26ef25cf847ad4191873d5685a37644acd02d4793f5",
        "git_blob_sha": "ff5116a3a91ff42e89c945cde02b274f8ac0965b"
      },
      "after": {
        "path": "topics/visible-flex-larger-amplitude/results/R723-directional-normal-flow-support-reach.md",
        "bytes": 21535,
        "sha256": "0edbd1039706186d07412a53c8e5c10411c5966dc36e38a7a504cf923d43e7eb",
        "expected_blob": "2efee88735ae0638062de2e1e1d5706313cac3ea",
        "blob": "2efee88735ae0638062de2e1e1d5706313cac3ea"
      }
    },
    {
      "path": [
        "source_reproducer_path"
      ],
      "before_present": true,
      "before": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_meridian_batched_producer_R722_R716_sources.py",
      "after": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_R723_compatible_R716_source.mjs"
    },
    {
      "path": [
        "current_complete_parameter_counts",
        "consumer_summary_fields"
      ],
      "before_present": true,
      "before": 60,
      "after": 65
    },
    {
      "path": [
        "current_complete_parameter_counts",
        "original_60_consumer_selectors_preserved"
      ],
      "before_present": false,
      "after": true
    },
    {
      "path": [
        "complete_current_closed_runtime"
      ],
      "before_present": true,
      "before": {
        "role": "closed",
        "name": "fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py",
        "bytes": 84576,
        "sha256": "002eb1b91c99ea212255d14a4e929e876e09f34c38c78ffb7fc4f806b8799c5f",
        "git_blob_sha": "5f3b42618cfab77eaa3297073d71657e8df78dac"
      },
      "after": {
        "name": "fixed_fejer_R723_directional_closed_phase_grip_evidence.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_directional_closed_phase_grip_evidence.py",
        "bytes": 87670,
        "sha256": "1782eebd539ae47367260008c00b6a3912fe1fec26d30c22a8f0a7329a0309dc",
        "expected_blob": "94a33898b3b86646d207b3018d26069eaffd8797",
        "git_blob_sha": "94a33898b3b86646d207b3018d26069eaffd8797"
      }
    },
    {
      "path": [
        "complete_closed_source_binding"
      ],
      "before_present": true,
      "before": {
        "runtime": {
          "role": "closed",
          "name": "fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py",
          "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py",
          "bytes": 84576,
          "sha256": "002eb1b91c99ea212255d14a4e929e876e09f34c38c78ffb7fc4f806b8799c5f",
          "git_blob_sha": "5f3b42618cfab77eaa3297073d71657e8df78dac"
        },
        "proof": {
          "role": "closed_note",
          "name": "2026-11-27-producer-R722-closed-phase-grip-r718-source-adapter.md",
          "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-producer-R722-closed-phase-grip-r718-source-adapter.md",
          "bytes": 25302,
          "sha256": "6c96766bd966611895c4a26ef25cf847ad4191873d5685a37644acd02d4793f5",
          "git_blob_sha": "ff5116a3a91ff42e89c945cde02b274f8ac0965b"
        },
        "schema": "actual-fixed-fejer-meridian-batched-bhalf-first-R722-complete-closed-phase-grip-evidence-v1",
        "complete_main_report": "{work}/fixed-fejer-meridian-batched-bhalf-first-R722-complete-closed-phase-grip-v1/report.json",
        "recorded_outward_tube_sidecar": "{work}/fixed-fejer-meridian-batched-bhalf-first-R722-complete-closed-phase-grip-v1/R716-unmarked-outward-tube.json",
        "complete_runtime_source_and_proof_are_the_actual_dependencies": true,
        "separate_closed_packaging_manifest_not_required_for_execution": true,
        "no_actual_geometry_or_tube_result_supplied": true
      },
      "after": {
        "runtime": {
          "name": "fixed_fejer_R723_directional_closed_phase_grip_evidence.py",
          "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_directional_closed_phase_grip_evidence.py",
          "bytes": 87670,
          "sha256": "1782eebd539ae47367260008c00b6a3912fe1fec26d30c22a8f0a7329a0309dc",
          "expected_blob": "94a33898b3b86646d207b3018d26069eaffd8797",
          "git_blob_sha": "94a33898b3b86646d207b3018d26069eaffd8797"
        },
        "theorem": {
          "path": "topics/visible-flex-larger-amplitude/results/R723-directional-normal-flow-support-reach.md",
          "bytes": 21535,
          "sha256": "0edbd1039706186d07412a53c8e5c10411c5966dc36e38a7a504cf923d43e7eb",
          "expected_blob": "2efee88735ae0638062de2e1e1d5706313cac3ea",
          "blob": "2efee88735ae0638062de2e1e1d5706313cac3ea"
        },
        "schema": "actual-fixed-fejer-R723-directional-closed-phase-grip-evidence-v1",
        "complete_main_report": "{work}/fixed-fejer-meridian-batched-bhalf-first-R723-directional-closed-phase-grip-v1/report.json",
        "recorded_outward_tube_sidecar": "{work}/fixed-fejer-meridian-batched-bhalf-first-R723-directional-closed-phase-grip-v1/R716-unmarked-outward-tube.json",
        "complete_runtime_source_and_proof_are_actual_dependencies": true,
        "complete_original_002eb_ports_and_scope_still_verified": true,
        "old_eight_roles_not_claimed_by_new_directional_branch": true,
        "full_original_stream_rereading_and_exact_all_137_scientific_sources_required": true,
        "unmarked_proof_does_not_follow_from_marked_embedding": true,
        "no_actual_geometry_or_tube_result_supplied": true
      }
    },
    {
      "path": [
        "complete_parameter_adapter"
      ],
      "before_present": true,
      "before": {
        "kind": "R716",
        "source_only_parameter_construction": true,
        "runtime_sources_changed": false,
        "exact_runtime_reuse": true,
        "source_reproducer_is_not_a_scientific_admission_gate": true,
        "parent_namespace": "fixed-fejer-meridian-batched-producer-bound",
        "current_namespace": "fixed-fejer-meridian-batched-bhalf-first",
        "parent_complete_metadata_kept_as_historical": true,
        "original_complete_parent_ready": {
          "name": "fixed-fejer-meridian-batched-producer-R722-complete-R716-closed-flux-centred-moments-ready.json",
          "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-producer-R722-complete-R716-closed-flux-centred-moments-ready.json",
          "bytes": 55988,
          "sha256": "93113ca87b4b2c3f921da1fb2934064ed08155d9b5144ab404916a57d302b90d",
          "git_blob_sha": "e1628c1246bf8783055e16abe1053f6ecc0d23c7",
          "fixed_publication_commit": "bf5f7e9708e3438b3c4f0435e1c908b0f95f933a"
        },
        "every_unmodified_parent_top_level_field_preserved": true,
        "all_current_unknown_physical_identities_null": true,
        "original_step_correspondence": [
          {
            "parent_step_id": "actual-fixed-fejer-meridian-batched-producer-R722-complete-R716-whole-closed-flux-integrals-20261127",
            "current_step_id": "actual-fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-whole-closed-flux-integrals-20261127",
            "counts": {
              "argument_words": 10,
              "formal_summary_fields": 34,
              "live_fields": 0,
              "output_count": 1
            },
            "script_unchanged": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_complete_closed_surface_moment_integrals.py",
            "only_runner_namespace_step_id_and_current_scope_changed": true,
            "current_scope_before": "Consume the complete actual producer-bound R722 normal/physical-sixjet report for one genuinely recorded immutable complete-required-angle packet point of driver10fa4e4e, reader8027ec35, normal76185 and packetc750. Rebind all137 scientific source roles, the fixed Fejer target, all six actual input files, the full33-node/32-stage chain, every planned full-circle cell, every original922 radial cell and all actual support/profile/control splits and scalar tail. Re-read complete original R722 posterior source/theorem attribution, all active integral leaves, all three total-equation residuals and the whole-angle posterior root-domain inequalities. Retain the genuine original R709 sufficient-condition flag as true or false. Integrate all12 original interval flux channels and retain each completed atomic block. Missing coverage, mean proof or branch association keeps full-domain moments null. The original600-second budget and maximum-angle-blocks0 remain. Reflection and both flat caps are retained; parametric flux alone does not certify an embedded outward body. No working F/J/root or accurate field oracle is called.",
            "current_scope_after": "Consume the complete actual producer-bound R722 normal/physical-sixjet report for one genuinely recorded immutable complete-required-angle packet point of driver10fa4e4e, reader8027ec35, normal76185 and packetc750. Rebind all137 scientific source roles, the fixed Fejer target, all six actual input files, the full33-node/32-stage chain, every planned full-circle cell, every original922 radial cell and all actual support/profile/control splits and scalar tail. Re-read complete original R722 posterior source/theorem attribution, all active integral leaves, all three total-equation residuals and the whole-angle posterior root-domain inequalities. Retain the genuine original R709 sufficient-condition flag as true or false. Integrate all12 original interval flux channels and retain each completed atomic block. Missing coverage, mean proof or branch association keeps full-domain moments null. The original600-second budget and maximum-angle-blocks0 remain. Reflection and both flat caps are retained; parametric flux alone does not certify an embedded outward body. No working F/J/root or accurate field oracle is called.",
            "all_full_argument_tokens_preserved_except_namespace": true,
            "all_formal_and_live_selector_values_preserved": true
          },
          {
            "parent_step_id": "actual-fixed-fejer-meridian-batched-producer-R722-complete-R716-centred-volume-moments-20261127",
            "current_step_id": "actual-fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-centred-volume-moments-20261127",
            "counts": {
              "argument_words": 8,
              "formal_summary_fields": 60,
              "live_fields": 0,
              "output_count": 1
            },
            "script_unchanged": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_r716_centred_volume_moment.py",
            "only_runner_namespace_step_id_and_current_scope_changed": true,
            "current_scope_before": "Read and rebind all complete same-point moment blocks/journals/sources. Replay all12 channels, lower/flat-cap contributions, exact p4 volume/first/mixed moments and the full general R716(2) centred tensors at physical t=0,1/2,1. The simpler B_eff formula requires the actual all32-stage signed half-turn inclusion. Independently consume the FINAL complete producer_R722 closed-phase main report and its exact recorded sidecar; recheck every source/input/output and complete point/model/snapshot/target/normal identity, then replay complete geometry, ports, every support cell, independent unmarked tube and all8 original beta evidence roles. A provisional or incomplete closed report discharges nothing. Only actual full-body interpretation, positive total volume and a separated centred invariant enable the R625/R716 E(3)-quotient lower bound. R722 mean existence and R718 holding distance do not provide volume/noncongruence conclusions. No working F/J/root or accurate field oracle, conditional reach or overall completion claim is added.",
            "current_scope_after": "Read and rebind all complete same-point moment blocks/journals/sources. Replay all12 channels, lower/flat-cap contributions, exact p4 volume/first/mixed moments and the full general R716(2) centred tensors at physical t=0,1/2,1. The simpler B_eff formula requires the actual all32-stage signed half-turn inclusion. Independently consume the FINAL complete producer_R722 closed-phase main report and its exact recorded sidecar; recheck every source/input/output and complete point/model/snapshot/target/normal identity, then replay complete geometry, ports, every support cell, independent unmarked tube and all8 original beta evidence roles. A provisional or incomplete closed report discharges nothing. Only actual full-body interpretation, positive total volume and a separated centred invariant enable the R625/R716 E(3)-quotient lower bound. R722 mean existence and R718 holding distance do not provide volume/noncongruence conclusions. No working F/J/root or accurate field oracle, conditional reach or overall completion claim is added.",
            "all_full_argument_tokens_preserved_except_namespace": true,
            "all_formal_and_live_selector_values_preserved": true
          }
        ],
        "whole_parent_metadata_is_not_a_current_execution_return": true,
        "parameter_reproducer_path": "scripts/resume_20261126/reproduce_fixed_fejer_bhalf_moment_mesh_parameters.mjs"
      },
      "after": {
        "kind": "independent-R723-complete-consumer-and-whole-parameter-successor",
        "runtime_sources_changed": [
          {
            "name": "fixed_fejer_R723_compatible_r716_centred_volume_moment.py",
            "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_r716_centred_volume_moment.py",
            "bytes": 61706,
            "sha256": "3c0d6cfd5280b7cb250b1a8ff2077c849a20f725169d0f667c74eb975c3c294b",
            "git_blob_sha": "3ae6dd08dfcbb00002fa2482ec49cf7e56d86ea4"
          }
        ],
        "runtime_sources_shared": [
          "45ca full twelve-channel producer",
          "f79c full interval/centred arithmetic",
          "all original 137 scientific roles",
          "6c57 complete geometry and all exact same-point input dependencies"
        ],
        "all_old_legacy_validator_and_numeric_functions_preserved": true,
        "no_source_reproducer_or_validator_added_as_solver_admission_gate": true,
        "complete_original_parent_ready": {
          "name": "fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
          "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
          "bytes": 80089,
          "sha256": "3b49bd1b12b6b5680fd63a6cd8a5e8c34633626c875044a50ba98b6b1174441a",
          "git_blob_sha": "7d748fcb2ca892ce50c23d0153c198f99fc307db"
        },
        "whole_parent_metadata_retained_under_explicit_historical_keys": true,
        "current_consumer_full_source": {
          "name": "fixed_fejer_R723_compatible_r716_centred_volume_moment.py",
          "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_r716_centred_volume_moment.py",
          "bytes": 61706,
          "sha256": "3c0d6cfd5280b7cb250b1a8ff2077c849a20f725169d0f667c74eb975c3c294b",
          "git_blob_sha": "3ae6dd08dfcbb00002fa2482ec49cf7e56d86ea4"
        },
        "parameter_reproducer_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_bhalf_R723_R716_parameters.mjs",
        "current_closed_source": {
          "name": "fixed_fejer_R723_directional_closed_phase_grip_evidence.py",
          "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_directional_closed_phase_grip_evidence.py",
          "bytes": 87670,
          "sha256": "1782eebd539ae47367260008c00b6a3912fe1fec26d30c22a8f0a7329a0309dc",
          "expected_blob": "94a33898b3b86646d207b3018d26069eaffd8797",
          "git_blob_sha": "94a33898b3b86646d207b3018d26069eaffd8797"
        },
        "all_current_unknown_physical_identities_remain_null": true
      }
    },
    {
      "path": [
        "R723_compatible_consumer"
      ],
      "before_present": false,
      "after": {
        "name": "fixed_fejer_R723_compatible_r716_centred_volume_moment.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_r716_centred_volume_moment.py",
        "bytes": 61706,
        "sha256": "3c0d6cfd5280b7cb250b1a8ff2077c849a20f725169d0f667c74eb975c3c294b",
        "git_blob_sha": "3ae6dd08dfcbb00002fa2482ec49cf7e56d86ea4"
      }
    },
    {
      "path": [
        "R723_compatible_consumer_source_reproducer"
      ],
      "before_present": false,
      "after": {
        "name": "reproduce_R723_compatible_R716_source.mjs",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_R723_compatible_R716_source.mjs",
        "bytes": 19477,
        "sha256": "f1e72d72563da39a3ccd29ec43dbdba767f56ec1ce0b6823981721d79ddbac13",
        "git_blob_sha": "176ab5b2b2036b0506fb627690ba92eaa29cb231"
      }
    },
    {
      "path": [
        "R723_complete_closed_ready"
      ],
      "before_present": false,
      "after": {
        "name": "fixed-fejer-meridian-batched-bhalf-first-R723-directional-closed-phase-grip-ready.json",
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R723-directional-closed-phase-grip-ready.json",
        "bytes": 86836,
        "sha256": "5a072e9c1030f146f46084d3b395300f7c79b52bb0c88830a55d0b3188464d9f",
        "git_blob_sha": "80e5cf779dbe6d8bb811561aaf55da036669eca0"
      }
    },
    {
      "path": [
        "R723_parameter_parent"
      ],
      "before_present": false,
      "after": {
        "name": "fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
        "bytes": 80089,
        "sha256": "3b49bd1b12b6b5680fd63a6cd8a5e8c34633626c875044a50ba98b6b1174441a",
        "git_blob_sha": "7d748fcb2ca892ce50c23d0153c198f99fc307db"
      }
    },
    {
      "path": [
        "R723_parameter_reproducer_path"
      ],
      "before_present": false,
      "after": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_bhalf_R723_R716_parameters.mjs"
    },
    {
      "path": [
        "R723_independent_consumption_contract"
      ],
      "before_present": false,
      "after": {
        "complete_old_flux_producer_and_600_seconds_unchanged": true,
        "full_twelve_raw_channels_and_centred_algebra_unchanged": true,
        "all_1024_angle_cells_and_922_radial_cells_plus_accurate_cuts_and_tail_retained": true,
        "full_32_stage_root_uniqueness_glue_and_same_point_held": true,
        "original_signed_half_turn_required_before_simplified_compensation_formula": true,
        "general_full_three_phase_formula_retained_without_half_turn": true,
        "original_R650_legacy_eight_role_branch_preserved_verbatim_under_explicit_legacy_name": true,
        "new_exact_source_schema_dispatch_to_complete_R723_validator": true,
        "R723_not_dependent_on_old_R650_target_or_eight_claims": true,
        "old_eight_role_result_stays_false_on_R723_branch": true,
        "all_actual_point_model_snapshot_target_complete_input_and_source_words_compared": true,
        "final_main_status_and_all_bytes_rechecked_before_sidecar": true,
        "independent_unmarked_support_curvature_reach_and_mark_height_strictly_verified": true,
        "complete_positive_volume_and_nonzero_centred_invariant_still_required": true,
        "actual_reach_may_be_used_only_after_its_complete_R723_proof": true,
        "completion_is_not_the_scientific_goal": true,
        "any_future_actual_fee_or_field_identity": null
      }
    },
    {
      "path": [
        "R723_parameter_parent_consumer_scope"
      ],
      "before_present": false,
      "after": "Read and rebind all complete same-point moment blocks/journals/sources. Replay all12 channels, lower/flat-cap contributions, exact p4 volume/first/mixed moments and the full general R716(2) centred tensors at physical t=0,1/2,1. The simpler B_eff formula requires the actual all32-stage signed half-turn inclusion. Independently consume the FINAL complete producer_R722 closed-phase main report and its exact recorded sidecar; recheck every source/input/output and complete point/model/snapshot/target/normal identity, then replay complete geometry, ports, every support cell, independent unmarked tube and all8 original beta evidence roles. A provisional or incomplete closed report discharges nothing. Only actual full-body interpretation, positive total volume and a separated centred invariant enable the R625/R716 E(3)-quotient lower bound. R722 mean existence and R718 holding distance do not provide volume/noncongruence conclusions. No working F/J/root or accurate field oracle, conditional reach or overall completion claim is added."
    },
    {
      "path": [
        "R723_historical_parent_metadata"
      ],
      "before_present": false,
      "after": {
        "schema": "prepared-fixed-fejer-meridian-bhalf-first-R722-complete-R716-closed-flux-centred-moments-v1",
        "complete_closed_phase_source_sha256": "002eb1b91c99ea212255d14a4e929e876e09f34c38c78ffb7fc4f806b8799c5f",
        "complete_closed_phase_main_report": "{work}/fixed-fejer-meridian-batched-bhalf-first-R722-complete-closed-phase-grip-v1/report.json",
        "complete_ports_support_unmarked_tube_and_original_beta_evidence_replayed": true,
        "complete_closed_phase_reference": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py",
        "complete_current_closed_runtime": {
          "role": "closed",
          "name": "fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py",
          "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py",
          "bytes": 84576,
          "sha256": "002eb1b91c99ea212255d14a4e929e876e09f34c38c78ffb7fc4f806b8799c5f",
          "git_blob_sha": "5f3b42618cfab77eaa3297073d71657e8df78dac"
        },
        "complete_current_closed_adapter_proof": {
          "role": "closed_note",
          "name": "2026-11-27-producer-R722-closed-phase-grip-r718-source-adapter.md",
          "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-producer-R722-closed-phase-grip-r718-source-adapter.md",
          "bytes": 25302,
          "sha256": "6c96766bd966611895c4a26ef25cf847ad4191873d5685a37644acd02d4793f5",
          "git_blob_sha": "ff5116a3a91ff42e89c945cde02b274f8ac0965b"
        },
        "complete_closed_source_binding": {
          "runtime": {
            "role": "closed",
            "name": "fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py",
            "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py",
            "bytes": 84576,
            "sha256": "002eb1b91c99ea212255d14a4e929e876e09f34c38c78ffb7fc4f806b8799c5f",
            "git_blob_sha": "5f3b42618cfab77eaa3297073d71657e8df78dac"
          },
          "proof": {
            "role": "closed_note",
            "name": "2026-11-27-producer-R722-closed-phase-grip-r718-source-adapter.md",
            "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-producer-R722-closed-phase-grip-r718-source-adapter.md",
            "bytes": 25302,
            "sha256": "6c96766bd966611895c4a26ef25cf847ad4191873d5685a37644acd02d4793f5",
            "git_blob_sha": "ff5116a3a91ff42e89c945cde02b274f8ac0965b"
          },
          "schema": "actual-fixed-fejer-meridian-batched-bhalf-first-R722-complete-closed-phase-grip-evidence-v1",
          "complete_main_report": "{work}/fixed-fejer-meridian-batched-bhalf-first-R722-complete-closed-phase-grip-v1/report.json",
          "recorded_outward_tube_sidecar": "{work}/fixed-fejer-meridian-batched-bhalf-first-R722-complete-closed-phase-grip-v1/R716-unmarked-outward-tube.json",
          "complete_runtime_source_and_proof_are_the_actual_dependencies": true,
          "separate_closed_packaging_manifest_not_required_for_execution": true,
          "no_actual_geometry_or_tube_result_supplied": true
        },
        "source_reproducer_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_meridian_batched_producer_R722_R716_sources.py",
        "current_complete_parameter_counts": {
          "producer_arguments": 10,
          "consumer_arguments": 8,
          "producer_summary_fields": 34,
          "consumer_summary_fields": 60,
          "producer_seconds": 600,
          "maximum_angle_blocks": 0
        },
        "complete_parameter_adapter": {
          "kind": "R716",
          "source_only_parameter_construction": true,
          "runtime_sources_changed": false,
          "exact_runtime_reuse": true,
          "source_reproducer_is_not_a_scientific_admission_gate": true,
          "parent_namespace": "fixed-fejer-meridian-batched-producer-bound",
          "current_namespace": "fixed-fejer-meridian-batched-bhalf-first",
          "parent_complete_metadata_kept_as_historical": true,
          "original_complete_parent_ready": {
            "name": "fixed-fejer-meridian-batched-producer-R722-complete-R716-closed-flux-centred-moments-ready.json",
            "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-producer-R722-complete-R716-closed-flux-centred-moments-ready.json",
            "bytes": 55988,
            "sha256": "93113ca87b4b2c3f921da1fb2934064ed08155d9b5144ab404916a57d302b90d",
            "git_blob_sha": "e1628c1246bf8783055e16abe1053f6ecc0d23c7",
            "fixed_publication_commit": "bf5f7e9708e3438b3c4f0435e1c908b0f95f933a"
          },
          "every_unmodified_parent_top_level_field_preserved": true,
          "all_current_unknown_physical_identities_null": true,
          "original_step_correspondence": [
            {
              "parent_step_id": "actual-fixed-fejer-meridian-batched-producer-R722-complete-R716-whole-closed-flux-integrals-20261127",
              "current_step_id": "actual-fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-whole-closed-flux-integrals-20261127",
              "counts": {
                "argument_words": 10,
                "formal_summary_fields": 34,
                "live_fields": 0,
                "output_count": 1
              },
              "script_unchanged": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_complete_closed_surface_moment_integrals.py",
              "only_runner_namespace_step_id_and_current_scope_changed": true,
              "current_scope_before": "Consume the complete actual producer-bound R722 normal/physical-sixjet report for one genuinely recorded immutable complete-required-angle packet point of driver10fa4e4e, reader8027ec35, normal76185 and packetc750. Rebind all137 scientific source roles, the fixed Fejer target, all six actual input files, the full33-node/32-stage chain, every planned full-circle cell, every original922 radial cell and all actual support/profile/control splits and scalar tail. Re-read complete original R722 posterior source/theorem attribution, all active integral leaves, all three total-equation residuals and the whole-angle posterior root-domain inequalities. Retain the genuine original R709 sufficient-condition flag as true or false. Integrate all12 original interval flux channels and retain each completed atomic block. Missing coverage, mean proof or branch association keeps full-domain moments null. The original600-second budget and maximum-angle-blocks0 remain. Reflection and both flat caps are retained; parametric flux alone does not certify an embedded outward body. No working F/J/root or accurate field oracle is called.",
              "current_scope_after": "Consume the complete actual producer-bound R722 normal/physical-sixjet report for one genuinely recorded immutable complete-required-angle packet point of driver10fa4e4e, reader8027ec35, normal76185 and packetc750. Rebind all137 scientific source roles, the fixed Fejer target, all six actual input files, the full33-node/32-stage chain, every planned full-circle cell, every original922 radial cell and all actual support/profile/control splits and scalar tail. Re-read complete original R722 posterior source/theorem attribution, all active integral leaves, all three total-equation residuals and the whole-angle posterior root-domain inequalities. Retain the genuine original R709 sufficient-condition flag as true or false. Integrate all12 original interval flux channels and retain each completed atomic block. Missing coverage, mean proof or branch association keeps full-domain moments null. The original600-second budget and maximum-angle-blocks0 remain. Reflection and both flat caps are retained; parametric flux alone does not certify an embedded outward body. No working F/J/root or accurate field oracle is called.",
              "all_full_argument_tokens_preserved_except_namespace": true,
              "all_formal_and_live_selector_values_preserved": true
            },
            {
              "parent_step_id": "actual-fixed-fejer-meridian-batched-producer-R722-complete-R716-centred-volume-moments-20261127",
              "current_step_id": "actual-fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-centred-volume-moments-20261127",
              "counts": {
                "argument_words": 8,
                "formal_summary_fields": 60,
                "live_fields": 0,
                "output_count": 1
              },
              "script_unchanged": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_r716_centred_volume_moment.py",
              "only_runner_namespace_step_id_and_current_scope_changed": true,
              "current_scope_before": "Read and rebind all complete same-point moment blocks/journals/sources. Replay all12 channels, lower/flat-cap contributions, exact p4 volume/first/mixed moments and the full general R716(2) centred tensors at physical t=0,1/2,1. The simpler B_eff formula requires the actual all32-stage signed half-turn inclusion. Independently consume the FINAL complete producer_R722 closed-phase main report and its exact recorded sidecar; recheck every source/input/output and complete point/model/snapshot/target/normal identity, then replay complete geometry, ports, every support cell, independent unmarked tube and all8 original beta evidence roles. A provisional or incomplete closed report discharges nothing. Only actual full-body interpretation, positive total volume and a separated centred invariant enable the R625/R716 E(3)-quotient lower bound. R722 mean existence and R718 holding distance do not provide volume/noncongruence conclusions. No working F/J/root or accurate field oracle, conditional reach or overall completion claim is added.",
              "current_scope_after": "Read and rebind all complete same-point moment blocks/journals/sources. Replay all12 channels, lower/flat-cap contributions, exact p4 volume/first/mixed moments and the full general R716(2) centred tensors at physical t=0,1/2,1. The simpler B_eff formula requires the actual all32-stage signed half-turn inclusion. Independently consume the FINAL complete producer_R722 closed-phase main report and its exact recorded sidecar; recheck every source/input/output and complete point/model/snapshot/target/normal identity, then replay complete geometry, ports, every support cell, independent unmarked tube and all8 original beta evidence roles. A provisional or incomplete closed report discharges nothing. Only actual full-body interpretation, positive total volume and a separated centred invariant enable the R625/R716 E(3)-quotient lower bound. R722 mean existence and R718 holding distance do not provide volume/noncongruence conclusions. No working F/J/root or accurate field oracle, conditional reach or overall completion claim is added.",
              "all_full_argument_tokens_preserved_except_namespace": true,
              "all_formal_and_live_selector_values_preserved": true
            }
          ],
          "whole_parent_metadata_is_not_a_current_execution_return": true,
          "parameter_reproducer_path": "scripts/resume_20261126/reproduce_fixed_fejer_bhalf_moment_mesh_parameters.mjs"
        },
        "complete_parameter_correspondence": [
          {
            "parent_step_id": "actual-fixed-fejer-meridian-batched-producer-R722-complete-R716-whole-closed-flux-integrals-20261127",
            "current_step_id": "actual-fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-whole-closed-flux-integrals-20261127",
            "counts": {
              "argument_words": 10,
              "formal_summary_fields": 34,
              "live_fields": 0,
              "output_count": 1
            },
            "script_unchanged": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_complete_closed_surface_moment_integrals.py",
            "only_runner_namespace_step_id_and_current_scope_changed": true,
            "current_scope_before": "Consume the complete actual producer-bound R722 normal/physical-sixjet report for one genuinely recorded immutable complete-required-angle packet point of driver10fa4e4e, reader8027ec35, normal76185 and packetc750. Rebind all137 scientific source roles, the fixed Fejer target, all six actual input files, the full33-node/32-stage chain, every planned full-circle cell, every original922 radial cell and all actual support/profile/control splits and scalar tail. Re-read complete original R722 posterior source/theorem attribution, all active integral leaves, all three total-equation residuals and the whole-angle posterior root-domain inequalities. Retain the genuine original R709 sufficient-condition flag as true or false. Integrate all12 original interval flux channels and retain each completed atomic block. Missing coverage, mean proof or branch association keeps full-domain moments null. The original600-second budget and maximum-angle-blocks0 remain. Reflection and both flat caps are retained; parametric flux alone does not certify an embedded outward body. No working F/J/root or accurate field oracle is called.",
            "current_scope_after": "Consume the complete actual producer-bound R722 normal/physical-sixjet report for one genuinely recorded immutable complete-required-angle packet point of driver10fa4e4e, reader8027ec35, normal76185 and packetc750. Rebind all137 scientific source roles, the fixed Fejer target, all six actual input files, the full33-node/32-stage chain, every planned full-circle cell, every original922 radial cell and all actual support/profile/control splits and scalar tail. Re-read complete original R722 posterior source/theorem attribution, all active integral leaves, all three total-equation residuals and the whole-angle posterior root-domain inequalities. Retain the genuine original R709 sufficient-condition flag as true or false. Integrate all12 original interval flux channels and retain each completed atomic block. Missing coverage, mean proof or branch association keeps full-domain moments null. The original600-second budget and maximum-angle-blocks0 remain. Reflection and both flat caps are retained; parametric flux alone does not certify an embedded outward body. No working F/J/root or accurate field oracle is called.",
            "all_full_argument_tokens_preserved_except_namespace": true,
            "all_formal_and_live_selector_values_preserved": true
          },
          {
            "parent_step_id": "actual-fixed-fejer-meridian-batched-producer-R722-complete-R716-centred-volume-moments-20261127",
            "current_step_id": "actual-fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-centred-volume-moments-20261127",
            "counts": {
              "argument_words": 8,
              "formal_summary_fields": 60,
              "live_fields": 0,
              "output_count": 1
            },
            "script_unchanged": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_r716_centred_volume_moment.py",
            "only_runner_namespace_step_id_and_current_scope_changed": true,
            "current_scope_before": "Read and rebind all complete same-point moment blocks/journals/sources. Replay all12 channels, lower/flat-cap contributions, exact p4 volume/first/mixed moments and the full general R716(2) centred tensors at physical t=0,1/2,1. The simpler B_eff formula requires the actual all32-stage signed half-turn inclusion. Independently consume the FINAL complete producer_R722 closed-phase main report and its exact recorded sidecar; recheck every source/input/output and complete point/model/snapshot/target/normal identity, then replay complete geometry, ports, every support cell, independent unmarked tube and all8 original beta evidence roles. A provisional or incomplete closed report discharges nothing. Only actual full-body interpretation, positive total volume and a separated centred invariant enable the R625/R716 E(3)-quotient lower bound. R722 mean existence and R718 holding distance do not provide volume/noncongruence conclusions. No working F/J/root or accurate field oracle, conditional reach or overall completion claim is added.",
            "current_scope_after": "Read and rebind all complete same-point moment blocks/journals/sources. Replay all12 channels, lower/flat-cap contributions, exact p4 volume/first/mixed moments and the full general R716(2) centred tensors at physical t=0,1/2,1. The simpler B_eff formula requires the actual all32-stage signed half-turn inclusion. Independently consume the FINAL complete producer_R722 closed-phase main report and its exact recorded sidecar; recheck every source/input/output and complete point/model/snapshot/target/normal identity, then replay complete geometry, ports, every support cell, independent unmarked tube and all8 original beta evidence roles. A provisional or incomplete closed report discharges nothing. Only actual full-body interpretation, positive total volume and a separated centred invariant enable the R625/R716 E(3)-quotient lower bound. R722 mean existence and R718 holding distance do not provide volume/noncongruence conclusions. No working F/J/root or accurate field oracle, conditional reach or overall completion claim is added.",
            "all_full_argument_tokens_preserved_except_namespace": true,
            "all_formal_and_live_selector_values_preserved": true
          }
        ],
        "actual_source_specification": "Reuse the unchanged complete producer-bound source family driver10fa/reader8027/normal76185/packetc750, all137 scientific source roles and18 runtime files. This plan consumes only the genuine bhalf-first field and its own immutable point/fee inputs, never the original run18 input records or mutable observations. All R722 whole-cell validation, twelve moments, full cover and exact final closed-main evidence rules remain unchanged. New run, reference report, working model, point, packet, root, flux and delta_E values are unknown until actual Actions output."
      }
    },
    {
      "path": [
        "R723_parameter_correspondence"
      ],
      "before_present": false,
      "after": {
        "complete_original_ready": {
          "name": "fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
          "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
          "bytes": 80089,
          "sha256": "3b49bd1b12b6b5680fd63a6cd8a5e8c34633626c875044a50ba98b6b1174441a",
          "git_blob_sha": "7d748fcb2ca892ce50c23d0153c198f99fc307db"
        },
        "producer_entire_step_object_unchanged": true,
        "consumer_original_args": [
          "--repo",
          "{repo}",
          "--moment-report",
          "{work}/fixed-fejer-meridian-batched-bhalf-first-R722-r716-complete-moment-integrals/report.json",
          "--output",
          "{work}/fixed-fejer-meridian-batched-bhalf-first-R722-r716-complete-centred-moments/report.json",
          "--closed-phase-report",
          "{work}/fixed-fejer-meridian-batched-bhalf-first-R722-complete-closed-phase-grip-v1/report.json"
        ],
        "consumer_current_args": [
          "--repo",
          "{repo}",
          "--moment-report",
          "{work}/fixed-fejer-meridian-batched-bhalf-first-R722-r716-complete-moment-integrals/report.json",
          "--output",
          "{work}/fixed-fejer-meridian-batched-bhalf-first-R723-r716-complete-centred-moments/report.json",
          "--closed-phase-report",
          "{work}/fixed-fejer-meridian-batched-bhalf-first-R723-directional-closed-phase-grip-v1/report.json"
        ],
        "only_consumer_argv_changes": [
          {
            "index": 5,
            "purpose": "fresh R723 centred-moment output"
          },
          {
            "index": 7,
            "purpose": "exact optional R723 final closed report"
          }
        ],
        "all_other_flags_values_order_unchanged": true,
        "all_original_summary_maps_retained": true,
        "new_consumer_whole_source": {
          "name": "fixed_fejer_R723_compatible_r716_centred_volume_moment.py",
          "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_r716_centred_volume_moment.py",
          "bytes": 61706,
          "sha256": "3c0d6cfd5280b7cb250b1a8ff2077c849a20f725169d0f667c74eb975c3c294b",
          "git_blob_sha": "3ae6dd08dfcbb00002fa2482ec49cf7e56d86ea4"
        },
        "no_new_scientific_budget_or_gate": true,
        "all_parent_fields_held_either_as_current_unchanged_metadata_or_explicit_full_history": true
      }
    }
  ],
  "parent_whitespace_restoration": []
};
const sha=s=>crypto.createHash("sha256").update(s,"utf8").digest("hex");
const size=s=>Buffer.byteLength(s,"utf8");
const blob=s=>crypto.createHash("sha1").update("blob "+size(s)+"\0").update(s,"utf8").digest("hex");
function check(ok,message){if(!ok)throw new Error(message);}
const equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
function apply(root,operations,inverse=false){
 for(const op of inverse?[...operations].reverse():operations){
  let target=root;for(const key of op.path.slice(0,-1))target=target[key];
  const key=op.path.at(-1);
  if(inverse){
   check(equal(target[key],op.after),"Exact inverse parameter value changed");
   if(op.before_present)target[key]=op.before;else delete target[key];
  }else{
   check(Object.hasOwn(target,key)===op.before_present&&
    (!op.before_present||equal(target[key],op.before)),"Exact original parameter value changed");
   target[key]=op.after;
  }
 }
 return root;
}
const words=process.argv.slice(2),args={};
for(let i=0;i<words.length;i+=2){check(words[i]?.startsWith("--")&&words[i+1],"Complete arguments");
 check(!Object.hasOwn(args,words[i]),"Duplicate option");args[words[i]]=words[i+1];}
check(Object.keys(args).length===2&&args["--parent-ready"]&&args["--output-directory"],
 "Usage: --parent-ready EXACT_WHOLE_PARENT_JSON --output-directory GENERATED_PARAMS_DIR");
const raw=fs.readFileSync(args["--parent-ready"],"utf8");
check(size(raw)===SPEC.parent.bytes&&sha(raw)===SPEC.parent.sha256&&blob(raw)===SPEC.parent.git_blob_sha,
 "The original complete ready bytes/SHA/blob differ");
const original=JSON.parse(raw);
const next=apply(JSON.parse(JSON.stringify(original)),SPEC.operations);
const output=JSON.stringify(next,null,2)+"\n";
check(size(output)===SPEC.output.bytes&&sha(output)===SPEC.output.sha256&&blob(output)===SPEC.output.git_blob_sha,
 "The complete output parameter file differs");
const restored=apply(JSON.parse(JSON.stringify(next)),SPEC.operations,true);
let restoredText=JSON.stringify(restored,null,2)+"\n";
for(const patch of SPEC.parent_whitespace_restoration){
 check(restoredText.split(patch.before).length===2,"Exact original whitespace changed");
 restoredText=restoredText.replace(patch.before,patch.after);
}
check(restoredText===raw,"The entire original parameter file was not restored byte for byte");
fs.mkdirSync(args["--output-directory"],{recursive:true});
const target=path.join(args["--output-directory"],SPEC.output.name);
if(fs.existsSync(target))check(fs.readFileSync(target,"utf8")===output,"Do not replace another parameter file");
else fs.writeFileSync(target,output,"utf8");
process.stdout.write(JSON.stringify({schema:SPEC.schema,parent:SPEC.parent,output:SPEC.output,
 complete_whole_parent_forward_inverse:true,scientific_calls:0,new_admission_gate:false})+"\n");
