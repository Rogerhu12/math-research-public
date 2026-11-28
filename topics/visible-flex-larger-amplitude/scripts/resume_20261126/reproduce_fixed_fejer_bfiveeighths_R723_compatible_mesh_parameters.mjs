#!/usr/bin/env node
// Complete source/JSON reproduction only. No field, root, mesh or proof is run.
// The whole old plans and shared histories remain immutable inputs.
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

const SPEC = {
  "schema": "fixed-fejer-R723-compatible-complete-mesh-parameter-reproduction-v1",
  "complete_shared_parent_records": [
    {
      "name": "fixed-fejer-bfiveeighths-complete-moment-mesh-parameter-binding.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-moment-mesh-parameter-binding.json",
      "bytes": 71214,
      "sha256": "02589f547c2e9cffb3307e1a675f1a3d616925a694844e1ccbdcd9d18c982e99",
      "git_blob_sha": "fceab004648c04dd5849cf71a125ff6e6db89c55"
    },
    {
      "name": "fixed-fejer-bfiveeighths-complete-normal-closed-parameter-binding.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-normal-closed-parameter-binding.json",
      "bytes": 64060,
      "sha256": "3b6e8e082746a1900b79a60772c0d92d3c9ed608d72951a21ba2175946b846c1",
      "git_blob_sha": "033bc2427bd70d86a639c6c3a38b3314f3ebe5b5"
    },
    {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-moment-mesh-parameter-delivery.json",
      "name": "fixed-fejer-bfiveeighths-complete-moment-mesh-parameter-delivery.json",
      "bytes": 35511,
      "sha256": "00c1746bbeb89de312bf9b59a676dda9339e124b33013354fc742203785b852d",
      "git_blob_sha": "e5e828c6e8a1afe399fe226ec5eb4f57814c095c"
    }
  ],
  "outputs": [
    {
      "parent": {
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bfiveeighths-first-same-field-phase-mesh-final-ready.json",
        "name": "fixed-fejer-meridian-batched-bfiveeighths-first-same-field-phase-mesh-final-ready.json",
        "bytes": 28934,
        "sha256": "4a305e8ae4b90886f88bbcaa18c25645e8145a83bd3def8c2b870e8795852f21",
        "git_blob_sha": "6605aa4784b2ac9d32c639d343068ec916b94cbb"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bfiveeighths-first-R723-compatible-same-field-phase-mesh-final-ready.json",
        "name": "fixed-fejer-meridian-batched-bfiveeighths-first-R723-compatible-same-field-phase-mesh-final-ready.json",
        "bytes": 32488,
        "sha256": "edfeb490f121037ed538dee9ac8732844b9aa0c80fd7ce5dd036ce993f659ea5",
        "git_blob_sha": "e7eade957387f4d3267bd5280e104725f950a7f1"
      },
      "metadata_without_steps": {
        "schema": "fixed-fejer-bfiveeighths-complete-R723-compatible-mesh-final-parameters-v1",
        "prepared_utc": "2026-11-27T23:50:11Z",
        "executed": false,
        "queued": false,
        "scientific_execution_permitted_only_in_public_Actions": true,
        "complete_immediate_parameter_parent": {
          "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bfiveeighths-first-same-field-phase-mesh-final-ready.json",
          "name": "fixed-fejer-meridian-batched-bfiveeighths-first-same-field-phase-mesh-final-ready.json",
          "bytes": 28934,
          "sha256": "4a305e8ae4b90886f88bbcaa18c25645e8145a83bd3def8c2b870e8795852f21",
          "git_blob_sha": "6605aa4784b2ac9d32c639d343068ec916b94cbb"
        },
        "original_complete_parent_ready_and_every_nested_field_retained_by_exact_whole_file": true,
        "parent_metadata_is_historical_and_not_relabelled_as_current_R723_claims": true,
        "complete_current_parameter_binding": {
          "name": "fixed-fejer-bfiveeighths-complete-moment-mesh-parameter-binding.json",
          "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-moment-mesh-parameter-binding.json",
          "bytes": 71214,
          "sha256": "02589f547c2e9cffb3307e1a675f1a3d616925a694844e1ccbdcd9d18c982e99",
          "git_blob_sha": "fceab004648c04dd5849cf71a125ff6e6db89c55"
        },
        "full_current_scientific_normal_closed_binding": {
          "name": "fixed-fejer-bfiveeighths-complete-normal-closed-parameter-binding.json",
          "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-normal-closed-parameter-binding.json",
          "bytes": 64060,
          "sha256": "3b6e8e082746a1900b79a60772c0d92d3c9ed608d72951a21ba2175946b846c1",
          "git_blob_sha": "033bc2427bd70d86a639c6c3a38b3314f3ebe5b5"
        },
        "complete_parent_parameter_delivery": {
          "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-moment-mesh-parameter-delivery.json",
          "name": "fixed-fejer-bfiveeighths-complete-moment-mesh-parameter-delivery.json",
          "bytes": 35511,
          "sha256": "00c1746bbeb89de312bf9b59a676dda9339e124b33013354fc742203785b852d",
          "git_blob_sha": "e5e828c6e8a1afe399fe226ec5eb4f57814c095c"
        },
        "original_parent_steps_json_pointer": "/steps",
        "unchanged_complete_numerical_parameters_json_pointer": "/full_spatial_levels_times_and_time_refinement",
        "current_scientific_namespace": "fixed-fejer-meridian-batched-bfiveeighths-first",
        "current_mesh_namespace": "fixed-fejer-meridian-batched-bfiveeighths-first-R723-compatible-same-field-phase-mesh-final-v1",
        "point_source_mode": "final",
        "source_family": {
          "input": {
            "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_same_field_mesh_input.py",
            "name": "fixed_fejer_R723_compatible_same_field_mesh_input.py",
            "bytes": 95330,
            "sha256": "6c678893db4cff3366a0836ee900e67aabd23b5267768369d6bfa41479197aa8",
            "git_blob_sha": "fe0c0798c6a5ff50c140a0ad00e5e1b5b88e2530"
          },
          "main": {
            "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_same_field_phase_meshes.py",
            "name": "fixed_fejer_R723_compatible_same_field_phase_meshes.py",
            "bytes": 55097,
            "sha256": "f2a46875aaa230f24cfcb92011997aa6b3fa7a7caf985701e02461229e0057f2",
            "git_blob_sha": "be361ed47846be988c252aa049d1a57b68bfec47"
          },
          "reader": {
            "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_R723_compatible_same_field_phase_mesh_report.py",
            "name": "read_fixed_fejer_R723_compatible_same_field_phase_mesh_report.py",
            "bytes": 22349,
            "sha256": "5d47382428fb551a5f6bbaa61fd56191922bc793963a0cbb6af45914c126d813",
            "git_blob_sha": "6fb32e6f51c30796a3e558eca38cf96fd4be7c8f"
          },
          "complete_reused_R723_evidence_source": {
            "name": "fixed_fejer_R723_directional_closed_phase_grip_evidence.py",
            "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_directional_closed_phase_grip_evidence.py",
            "bytes": 87670,
            "sha256": "1782eebd539ae47367260008c00b6a3912fe1fec26d30c22a8f0a7329a0309dc",
            "expected_blob": "94a33898b3b86646d207b3018d26069eaffd8797",
            "git_blob_sha": "94a33898b3b86646d207b3018d26069eaffd8797"
          },
          "source_registry_roles": 146,
          "unchanged_complete_scientific_roles": 137,
          "original_mesh_registry_roles": 144,
          "entire_original_scientific_constructor_bytes": 9077,
          "entire_original_scientific_constructor_sha256": "3980881004d30a0179c7d1229073360491aa179340a16e77a23181dd47999eab",
          "scientific_mesh_main_body_unchanged": true
        },
        "original_complete_32_word_no_evidence_parent_plan_preserved": true,
        "optional_evidence_selection": {
          "requested": true,
          "report_path": "{work}/fixed-fejer-meridian-batched-bfiveeighths-first-R723-directional-closed-phase-grip-v1/report.json",
          "expected_report_sha256": null,
          "report_schema": "actual-fixed-fejer-R723-directional-closed-phase-grip-evidence-v1",
          "no_missing_or_incomplete_supplied_proof_silently_skipped": true,
          "independent_R723_five_roles_never_forge_original_eight_role_claims": true,
          "complete_consumption_does_not_assert_every_geometric_target_paid": true,
          "exact_selected_snapshot_must_match_actual_R723_snapshot": true,
          "physical_mesh_word_error_bound_supplied": false
        },
        "complete_step_derivation": {
          "parent_argv_words": [
            32,
            6
          ],
          "current_argv_words": [
            34,
            6
          ],
          "parent_formal_selector_pairs": [
            110,
            58
          ],
          "current_formal_selector_pairs": [
            118,
            66
          ],
          "original_live_selector_pairs": 48,
          "current_live_selector_pairs": 48,
          "all_parent_argument_words_retained_in_original_order_except_fresh_mesh_output_paths": true,
          "appended_science_argument_words": [
            "--closed-phase-report",
            "{work}/fixed-fejer-meridian-batched-bfiveeighths-first-R723-directional-closed-phase-grip-v1/report.json"
          ],
          "additional_formal_scalar_selectors": [
            "optional_closed_evidence_route",
            "optional_R723_directional_evidence_paid",
            "optional_R723_normal_binding_checked",
            "optional_R723_full_original_domain_reread",
            "optional_R723_reach_lower",
            "optional_R723_marked_sigma",
            "optional_R723_independent_unmarked_tube_paid",
            "optional_R723_old_eight_role_claimed"
          ],
          "scientific_report_and_command_paths_unchanged": true,
          "every_original_step_field_retained_except_explicit_runtime_scope_id_and_output_namespace_changes": true,
          "current_source_paths": [
            "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_same_field_phase_meshes.py",
            "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_R723_compatible_same_field_phase_mesh_report.py"
          ],
          "original_mesh_output_namespace": "fixed-fejer-meridian-batched-bfiveeighths-first-same-field-phase-mesh-final-v1",
          "current_mesh_output_namespace": "fixed-fejer-meridian-batched-bfiveeighths-first-R723-compatible-same-field-phase-mesh-final-v1",
          "no_original_source_parameter_history_field_deleted_from_immutable_parent": true,
          "no_domain_budget_sampling_stage_time_or_export_reduction": true
        },
        "planned_seed_parameters": {
          "relative_boundary_total_length": "5/8",
          "profile_delta": "1/32",
          "each_of_four_boundary_layers_relative_length": "5/32",
          "combined_central_relative_length": "1/4",
          "each_of_two_central_relative_length": "1/8",
          "central_intervals_relative_to_S": [
            [
              "3/16",
              "5/16"
            ],
            [
              "11/16",
              "13/16"
            ]
          ],
          "input_domain_is_legal": true,
          "definition_only_not_actual_floating_carriers": true,
          "actual_mean_root_and_angular_jets_proved": false,
          "metric_or_geometric_improvement_assumed": false
        },
        "planned_initial_damping": {
          "metric": ".01",
          "restoration": ".01",
          "same_as_complete_run19_parent": true,
          "run20_mu001_not_inherited": true
        },
        "original_complete_137_source_and_18_runtime_tables_in_whole_shared_binding": true,
        "complete_original_peers_typed_history_and_pending_responsibilities_in_whole_shared_binding": true,
        "future_actual": {
          "run_id": null,
          "run_attempt": null,
          "actual_complete_reference_inputs": null,
          "reference_report_sha256": null,
          "input_binding_sha256": null,
          "model_identity_sha256": null,
          "full_point_sha256": null,
          "snapshot_identity_sha256": null,
          "final_thirteen_member_checkpoint_sha256": null,
          "scientific_complete_report_sha256": null,
          "complete_normal_fee_report_sha256": null,
          "continuous_geometry_report_sha256": null,
          "legacy_closed_main_report_sha256": null,
          "R723_closed_main_report_sha256": null,
          "unmarked_outward_tube_report_sha256": null,
          "complete_moment_report_sha256": null,
          "centred_invariant_or_delta_E": null,
          "mesh_report_sha256": null,
          "mesh_or_time_refinement_results": null
        },
        "all_raw_complete_points_arrays_root_packets_and_meshes_remain_runner_only": true,
        "selected_packet_is_not_inferred_accepted_or_final": false,
        "final_mode_requires_the_genuine_complete_thirteen_member_checkpoint": true,
        "actual_first_normal_fee_repo_and_returned_snapshot_not_prepopulated": true,
        "fresh_repository_copies_must_match_whole_sources_and_preserve_original_recorded_paths": true,
        "supplied_optional_R723_requires_final_main_before_sidecars": true,
        "no_additional_scientific_step_or_solver_admission_gate_added": true,
        "complete_reproducer_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_bfiveeighths_R723_compatible_mesh_parameters.mjs"
      },
      "old_output_namespace": "fixed-fejer-meridian-batched-bfiveeighths-first-same-field-phase-mesh-final-v1",
      "new_output_namespace": "fixed-fejer-meridian-batched-bfiveeighths-first-R723-compatible-same-field-phase-mesh-final-v1",
      "step_replacements": [
        {
          "id": "complete-fixed-fejer-meridian-batched-bfiveeighths-first-R723-compatible-same-field-phase-mesh-final-20261127",
          "script": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_same_field_phase_meshes.py",
          "scope": "Consume only the actually returned complete fixed Fejer scientific report and its genuine full thirteen-member final checkpoint. Reconstruct all original free words, numerical policies and fixed reference, and use this one point for every complete closed mesh and physical time. A complete existing same-point immutable root snapshot is reused when present; missing final is an input failure and never a reset to initial or progress. The repaired producer-bound meridian-batched driver, reader, launcher and all137 scientific source roles are bound to the entire actual bfiveeighths-first command. The complete selected point, its fixed target and all source and input bytes are retained for every mesh and time; mutable progress is not a mesh input. This independent R723-compatible source retains the entire original numerical mesh algorithm and invokes the complete 1782 evidence validator only for the supplied final R723 report. All original normal32, complete domain, source paths, point, model, target and snapshot relationships are re-read; the new five-role proof is never relabelled as the old eight-role proof. Accurate claims do not bound working mesh word errors."
        },
        {
          "id": "actual-fixed-fejer-meridian-batched-bfiveeighths-first-R723-compatible-same-field-phase-mesh-final-20261127",
          "script": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_R723_compatible_same_field_phase_mesh_report.py",
          "scope": "Complete source/report/point/NPY/PLY-byte reader, including the complete fixed Fejer six-input binding and optional exact same-snapshot final closed proof. It calls no field, root, chart or mesh and retains all incomplete status. Actual complete bfiveeighths-first source and input identities are read; the pure reader performs no field, root or mesh calls. Optional R723 evidence re-consumption includes actual NPZ word reads and full-domain exact rational arithmetic, with no field/root/chart/mesh calls. Every original numerical mesh byte, dimension and count check remains unchanged."
        }
      ],
      "append_science_args": [
        "--closed-phase-report",
        "{work}/fixed-fejer-meridian-batched-bfiveeighths-first-R723-directional-closed-phase-grip-v1/report.json"
      ],
      "additional_selectors": [
        "optional_closed_evidence_route",
        "optional_R723_directional_evidence_paid",
        "optional_R723_normal_binding_checked",
        "optional_R723_full_original_domain_reread",
        "optional_R723_reach_lower",
        "optional_R723_marked_sigma",
        "optional_R723_independent_unmarked_tube_paid",
        "optional_R723_old_eight_role_claimed"
      ]
    },
    {
      "parent": {
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bfiveeighths-first-same-field-phase-mesh-packet-ready.json",
        "name": "fixed-fejer-meridian-batched-bfiveeighths-first-same-field-phase-mesh-packet-ready.json",
        "bytes": 28936,
        "sha256": "2569954a1496af914a29daa1a1d474e46a34d511b6f121197af0bfe6d410d1da",
        "git_blob_sha": "f7f83d236437a2f562e5cc17be631bce9bed5342"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bfiveeighths-first-R723-compatible-same-field-phase-mesh-packet-ready.json",
        "name": "fixed-fejer-meridian-batched-bfiveeighths-first-R723-compatible-same-field-phase-mesh-packet-ready.json",
        "bytes": 32483,
        "sha256": "f126cf24dde8130ab2b35a555069b81d16debc29d6579aaf3b8ea07502861d59",
        "git_blob_sha": "1241189852509af7e6a9c99112aa595b9a67d77d"
      },
      "metadata_without_steps": {
        "schema": "fixed-fejer-bfiveeighths-complete-R723-compatible-mesh-packet-parameters-v1",
        "prepared_utc": "2026-11-27T23:50:11Z",
        "executed": false,
        "queued": false,
        "scientific_execution_permitted_only_in_public_Actions": true,
        "complete_immediate_parameter_parent": {
          "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bfiveeighths-first-same-field-phase-mesh-packet-ready.json",
          "name": "fixed-fejer-meridian-batched-bfiveeighths-first-same-field-phase-mesh-packet-ready.json",
          "bytes": 28936,
          "sha256": "2569954a1496af914a29daa1a1d474e46a34d511b6f121197af0bfe6d410d1da",
          "git_blob_sha": "f7f83d236437a2f562e5cc17be631bce9bed5342"
        },
        "original_complete_parent_ready_and_every_nested_field_retained_by_exact_whole_file": true,
        "parent_metadata_is_historical_and_not_relabelled_as_current_R723_claims": true,
        "complete_current_parameter_binding": {
          "name": "fixed-fejer-bfiveeighths-complete-moment-mesh-parameter-binding.json",
          "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-moment-mesh-parameter-binding.json",
          "bytes": 71214,
          "sha256": "02589f547c2e9cffb3307e1a675f1a3d616925a694844e1ccbdcd9d18c982e99",
          "git_blob_sha": "fceab004648c04dd5849cf71a125ff6e6db89c55"
        },
        "full_current_scientific_normal_closed_binding": {
          "name": "fixed-fejer-bfiveeighths-complete-normal-closed-parameter-binding.json",
          "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-normal-closed-parameter-binding.json",
          "bytes": 64060,
          "sha256": "3b6e8e082746a1900b79a60772c0d92d3c9ed608d72951a21ba2175946b846c1",
          "git_blob_sha": "033bc2427bd70d86a639c6c3a38b3314f3ebe5b5"
        },
        "complete_parent_parameter_delivery": {
          "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-moment-mesh-parameter-delivery.json",
          "name": "fixed-fejer-bfiveeighths-complete-moment-mesh-parameter-delivery.json",
          "bytes": 35511,
          "sha256": "00c1746bbeb89de312bf9b59a676dda9339e124b33013354fc742203785b852d",
          "git_blob_sha": "e5e828c6e8a1afe399fe226ec5eb4f57814c095c"
        },
        "original_parent_steps_json_pointer": "/steps",
        "unchanged_complete_numerical_parameters_json_pointer": "/full_spatial_levels_times_and_time_refinement",
        "current_scientific_namespace": "fixed-fejer-meridian-batched-bfiveeighths-first",
        "current_mesh_namespace": "fixed-fejer-meridian-batched-bfiveeighths-first-R723-compatible-same-field-phase-mesh-packet-v1",
        "point_source_mode": "packet",
        "source_family": {
          "input": {
            "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_same_field_mesh_input.py",
            "name": "fixed_fejer_R723_compatible_same_field_mesh_input.py",
            "bytes": 95330,
            "sha256": "6c678893db4cff3366a0836ee900e67aabd23b5267768369d6bfa41479197aa8",
            "git_blob_sha": "fe0c0798c6a5ff50c140a0ad00e5e1b5b88e2530"
          },
          "main": {
            "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_same_field_phase_meshes.py",
            "name": "fixed_fejer_R723_compatible_same_field_phase_meshes.py",
            "bytes": 55097,
            "sha256": "f2a46875aaa230f24cfcb92011997aa6b3fa7a7caf985701e02461229e0057f2",
            "git_blob_sha": "be361ed47846be988c252aa049d1a57b68bfec47"
          },
          "reader": {
            "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_R723_compatible_same_field_phase_mesh_report.py",
            "name": "read_fixed_fejer_R723_compatible_same_field_phase_mesh_report.py",
            "bytes": 22349,
            "sha256": "5d47382428fb551a5f6bbaa61fd56191922bc793963a0cbb6af45914c126d813",
            "git_blob_sha": "6fb32e6f51c30796a3e558eca38cf96fd4be7c8f"
          },
          "complete_reused_R723_evidence_source": {
            "name": "fixed_fejer_R723_directional_closed_phase_grip_evidence.py",
            "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_directional_closed_phase_grip_evidence.py",
            "bytes": 87670,
            "sha256": "1782eebd539ae47367260008c00b6a3912fe1fec26d30c22a8f0a7329a0309dc",
            "expected_blob": "94a33898b3b86646d207b3018d26069eaffd8797",
            "git_blob_sha": "94a33898b3b86646d207b3018d26069eaffd8797"
          },
          "source_registry_roles": 146,
          "unchanged_complete_scientific_roles": 137,
          "original_mesh_registry_roles": 144,
          "entire_original_scientific_constructor_bytes": 9077,
          "entire_original_scientific_constructor_sha256": "3980881004d30a0179c7d1229073360491aa179340a16e77a23181dd47999eab",
          "scientific_mesh_main_body_unchanged": true
        },
        "original_complete_32_word_no_evidence_parent_plan_preserved": true,
        "optional_evidence_selection": {
          "requested": true,
          "report_path": "{work}/fixed-fejer-meridian-batched-bfiveeighths-first-R723-directional-closed-phase-grip-v1/report.json",
          "expected_report_sha256": null,
          "report_schema": "actual-fixed-fejer-R723-directional-closed-phase-grip-evidence-v1",
          "no_missing_or_incomplete_supplied_proof_silently_skipped": true,
          "independent_R723_five_roles_never_forge_original_eight_role_claims": true,
          "complete_consumption_does_not_assert_every_geometric_target_paid": true,
          "exact_selected_snapshot_must_match_actual_R723_snapshot": true,
          "physical_mesh_word_error_bound_supplied": false
        },
        "complete_step_derivation": {
          "parent_argv_words": [
            32,
            6
          ],
          "current_argv_words": [
            34,
            6
          ],
          "parent_formal_selector_pairs": [
            110,
            58
          ],
          "current_formal_selector_pairs": [
            118,
            66
          ],
          "original_live_selector_pairs": 48,
          "current_live_selector_pairs": 48,
          "all_parent_argument_words_retained_in_original_order_except_fresh_mesh_output_paths": true,
          "appended_science_argument_words": [
            "--closed-phase-report",
            "{work}/fixed-fejer-meridian-batched-bfiveeighths-first-R723-directional-closed-phase-grip-v1/report.json"
          ],
          "additional_formal_scalar_selectors": [
            "optional_closed_evidence_route",
            "optional_R723_directional_evidence_paid",
            "optional_R723_normal_binding_checked",
            "optional_R723_full_original_domain_reread",
            "optional_R723_reach_lower",
            "optional_R723_marked_sigma",
            "optional_R723_independent_unmarked_tube_paid",
            "optional_R723_old_eight_role_claimed"
          ],
          "scientific_report_and_command_paths_unchanged": true,
          "every_original_step_field_retained_except_explicit_runtime_scope_id_and_output_namespace_changes": true,
          "current_source_paths": [
            "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_same_field_phase_meshes.py",
            "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_R723_compatible_same_field_phase_mesh_report.py"
          ],
          "original_mesh_output_namespace": "fixed-fejer-meridian-batched-bfiveeighths-first-same-field-phase-mesh-packet-v1",
          "current_mesh_output_namespace": "fixed-fejer-meridian-batched-bfiveeighths-first-R723-compatible-same-field-phase-mesh-packet-v1",
          "no_original_source_parameter_history_field_deleted_from_immutable_parent": true,
          "no_domain_budget_sampling_stage_time_or_export_reduction": true
        },
        "planned_seed_parameters": {
          "relative_boundary_total_length": "5/8",
          "profile_delta": "1/32",
          "each_of_four_boundary_layers_relative_length": "5/32",
          "combined_central_relative_length": "1/4",
          "each_of_two_central_relative_length": "1/8",
          "central_intervals_relative_to_S": [
            [
              "3/16",
              "5/16"
            ],
            [
              "11/16",
              "13/16"
            ]
          ],
          "input_domain_is_legal": true,
          "definition_only_not_actual_floating_carriers": true,
          "actual_mean_root_and_angular_jets_proved": false,
          "metric_or_geometric_improvement_assumed": false
        },
        "planned_initial_damping": {
          "metric": ".01",
          "restoration": ".01",
          "same_as_complete_run19_parent": true,
          "run20_mu001_not_inherited": true
        },
        "original_complete_137_source_and_18_runtime_tables_in_whole_shared_binding": true,
        "complete_original_peers_typed_history_and_pending_responsibilities_in_whole_shared_binding": true,
        "future_actual": {
          "run_id": null,
          "run_attempt": null,
          "actual_complete_reference_inputs": null,
          "reference_report_sha256": null,
          "input_binding_sha256": null,
          "model_identity_sha256": null,
          "full_point_sha256": null,
          "snapshot_identity_sha256": null,
          "final_thirteen_member_checkpoint_sha256": null,
          "scientific_complete_report_sha256": null,
          "complete_normal_fee_report_sha256": null,
          "continuous_geometry_report_sha256": null,
          "legacy_closed_main_report_sha256": null,
          "R723_closed_main_report_sha256": null,
          "unmarked_outward_tube_report_sha256": null,
          "complete_moment_report_sha256": null,
          "centred_invariant_or_delta_E": null,
          "mesh_report_sha256": null,
          "mesh_or_time_refinement_results": null
        },
        "all_raw_complete_points_arrays_root_packets_and_meshes_remain_runner_only": true,
        "selected_packet_is_not_inferred_accepted_or_final": true,
        "final_mode_requires_the_genuine_complete_thirteen_member_checkpoint": false,
        "actual_first_normal_fee_repo_and_returned_snapshot_not_prepopulated": true,
        "fresh_repository_copies_must_match_whole_sources_and_preserve_original_recorded_paths": true,
        "supplied_optional_R723_requires_final_main_before_sidecars": true,
        "no_additional_scientific_step_or_solver_admission_gate_added": true,
        "complete_reproducer_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_bfiveeighths_R723_compatible_mesh_parameters.mjs"
      },
      "old_output_namespace": "fixed-fejer-meridian-batched-bfiveeighths-first-same-field-phase-mesh-packet-v1",
      "new_output_namespace": "fixed-fejer-meridian-batched-bfiveeighths-first-R723-compatible-same-field-phase-mesh-packet-v1",
      "step_replacements": [
        {
          "id": "complete-fixed-fejer-meridian-batched-bfiveeighths-first-R723-compatible-same-field-phase-mesh-packet-20261127",
          "script": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_same_field_phase_meshes.py",
          "scope": "Consume only a genuine complete required-angle immutable point snapshot in captured fixed Fejer scientific report bytes, selected explicitly or as the latest actual complete snapshot. Preserve every point word, every recorded angle and all 32 stage records. It can be a trial/cache point; no acceptance or final success is inferred. Missing snapshot is an input failure, never initial/progress substitution. The repaired producer-bound meridian-batched driver, reader, launcher and all137 scientific source roles are bound to the entire actual bfiveeighths-first command. The complete selected point, its fixed target and all source and input bytes are retained for every mesh and time; mutable progress is not a mesh input. This independent R723-compatible source retains the entire original numerical mesh algorithm and invokes the complete 1782 evidence validator only for the supplied final R723 report. All original normal32, complete domain, source paths, point, model, target and snapshot relationships are re-read; the new five-role proof is never relabelled as the old eight-role proof. Accurate claims do not bound working mesh word errors."
        },
        {
          "id": "actual-fixed-fejer-meridian-batched-bfiveeighths-first-R723-compatible-same-field-phase-mesh-packet-20261127",
          "script": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_R723_compatible_same_field_phase_mesh_report.py",
          "scope": "Complete source/report/point/NPY/PLY-byte reader, including the complete fixed Fejer six-input binding and optional exact same-snapshot final closed proof. It calls no field, root, chart or mesh and retains all incomplete status. Actual complete bfiveeighths-first source and input identities are read; the pure reader performs no field, root or mesh calls. Optional R723 evidence re-consumption includes actual NPZ word reads and full-domain exact rational arithmetic, with no field/root/chart/mesh calls. Every original numerical mesh byte, dimension and count check remains unchanged."
        }
      ],
      "append_science_args": [
        "--closed-phase-report",
        "{work}/fixed-fejer-meridian-batched-bfiveeighths-first-R723-directional-closed-phase-grip-v1/report.json"
      ],
      "additional_selectors": [
        "optional_closed_evidence_route",
        "optional_R723_directional_evidence_paid",
        "optional_R723_normal_binding_checked",
        "optional_R723_full_original_domain_reread",
        "optional_R723_reach_lower",
        "optional_R723_marked_sigma",
        "optional_R723_independent_unmarked_tube_paid",
        "optional_R723_old_eight_role_claimed"
      ]
    }
  ]
};


const digest=x=>crypto.createHash("sha256").update(x).digest("hex");
function readWhole(repo,r){
  const file=path.resolve(repo,r.path);
  if(!file.startsWith(repo+path.sep))throw Error("Keep the complete immutable parent path");
  const raw=fs.readFileSync(file);
  if(raw.length!==r.bytes||digest(raw)!==r.sha256)
    throw Error("The complete parent bytes differ: "+r.path);
  return JSON.parse(raw.toString("utf8"));
}
function mapNamespace(x,from,to){
  if(typeof x==="string")return x.split(from).join(to);
  if(Array.isArray(x))return x.map(v=>mapNamespace(v,from,to));
  if(x!==null&&typeof x==="object")
    return Object.fromEntries(Object.entries(x).map(([k,v])=>
      [mapNamespace(k,from,to),mapNamespace(v,from,to)]));
  return x;
}
function counts(step){
  return {argv_words:step.args.length,
    formal_selector_pairs:Object.values(step.summary).reduce((n,v)=>n+Object.keys(v).length,0),
    live_selector_pairs:Object.values(step.progress_summary||{}).reduce((n,v)=>n+Object.keys(v).length,0)};
}
function construct(parent,item){
  if(!Array.isArray(parent.steps)||parent.steps.length!==2)
    throw Error("Keep both complete original mesh steps");
  if(parent.steps[0].args.length!==32||parent.steps[1].args.length!==6)
    throw Error("The original complete 32/6 parameter scope changed");
  if(parent.steps[0].args.includes("--closed-phase-report"))
    throw Error("This exact parent already contains a different optional evidence selection");
  const steps=mapNamespace(parent.steps,item.old_output_namespace,item.new_output_namespace);
  for(let i=0;i<2;i++)Object.assign(steps[i],item.step_replacements[i]);
  steps[0].args.push(...item.append_science_args);
  const first=steps[0].summary[item.new_output_namespace+"/scalar-summary.json"];
  const second=Object.values(steps[1].summary)[0];
  if(!first||!second)throw Error("Keep the exact full original public readout objects");
  for(const key of item.additional_selectors){
    if(key in first||key in second)throw Error("Do not overwrite an existing formal selector");
    first[key]=key;second[key]=key;
  }
  const c=steps.map(counts);
  if(c[0].argv_words!==34||c[0].formal_selector_pairs!==118||c[0].live_selector_pairs!==48
      ||c[1].argv_words!==6||c[1].formal_selector_pairs!==66||c[1].live_selector_pairs!==0)
    throw Error("The complete formal/live/parameter scope changed");
  const inverse=structuredClone(steps);
  inverse[0].args.splice(-item.append_science_args.length);
  for(const key of item.additional_selectors){
    delete inverse[0].summary[item.new_output_namespace+"/scalar-summary.json"][key];
    delete Object.values(inverse[1].summary)[0][key];
  }
  for(let i=0;i<2;i++)
    for(const key of ["id","script","scope"])inverse[i][key]=parent.steps[i][key];
  if(JSON.stringify(mapNamespace(inverse,item.new_output_namespace,item.old_output_namespace))
      !==JSON.stringify(parent.steps))
    throw Error("The entire original step objects must be inversely recoverable");
  const value={...item.metadata_without_steps,steps};
  const raw=Buffer.from(JSON.stringify(value,null,2)+"\n","utf8");
  if(raw.length!==item.output.bytes||digest(raw)!==item.output.sha256)
    throw Error("The complete new parameter file differs: "+item.output.name);
  return raw;
}
function main(){
  const args=process.argv.slice(2);
  if(args.length!==4||args[0]!=="--repo"||args[2]!=="--output-directory")
    throw Error("Use --repo <complete checkout> --output-directory <fresh source/parameter directory>");
  const repo=path.resolve(args[1]),out=path.resolve(args[3]);
  if(out===repo||out.startsWith(repo+path.sep))
    throw Error("Use a construction directory outside the repository");
  for(const r of SPEC.complete_shared_parent_records)readWhole(repo,r);
  const prepared=SPEC.outputs.map(item=>{
    const raw=construct(readWhole(repo,item.parent),item);
    const target=path.resolve(out,item.output.name);
    if(path.dirname(target)!==out)throw Error("Keep the complete output basename");
    if(fs.existsSync(target)&&!fs.readFileSync(target).equals(raw))
      throw Error("Preserve an existing different complete parameter file: "+target);
    return {item,raw,target};
  });
  fs.mkdirSync(out,{recursive:true});
  for(const {raw,target} of prepared)if(!fs.existsSync(target))fs.writeFileSync(target,raw);
  process.stdout.write(JSON.stringify({schema:SPEC.schema,
    complete_outputs:prepared.map(x=>x.item.output),source_text_only:true,
    whole_original_plans_and_shared_histories_retained:true,
    numerical_or_scientific_execution:false,source_compilation_or_AST_execution:false,
    new_admission_gate:false},null,2)+"\n");
}
main();
