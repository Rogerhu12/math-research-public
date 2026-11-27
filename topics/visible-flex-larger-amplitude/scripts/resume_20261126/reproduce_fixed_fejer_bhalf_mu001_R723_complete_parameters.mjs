#!/usr/bin/env node
// Full parameter-only composition from six whole immutable parent documents.
// Parent metadata remains complete in those files; every current step is whole.
// No scientific modules, AST, fixture or new solver admission gate.
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
const SPEC={
  "schema": "complete-bhalf-mu001-R723-split-parameter-reproduction-v1",
  "parents": {
    "closed19": {
      "name": "fixed-fejer-meridian-batched-bhalf-first-R723-directional-closed-phase-grip-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R723-directional-closed-phase-grip-ready.json",
      "bytes": 86836,
      "sha256": "5a072e9c1030f146f46084d3b395300f7c79b52bb0c88830a55d0b3188464d9f",
      "git_blob_sha": "80e5cf779dbe6d8bb811561aaf55da036669eca0"
    },
    "moments19": {
      "name": "fixed-fejer-meridian-batched-bhalf-first-R723-complete-R716-moment-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R723-complete-R716-moment-ready.json",
      "bytes": 97718,
      "sha256": "11667d388e2d71d7583891aac274cfe7ea71810b123f9262f4a8ed85e90986c3",
      "git_blob_sha": "a5111bec896c7a83e598a9ea26f1372b80b309dc"
    },
    "science20": {
      "bytes": 97019,
      "sha256": "89b437a4986b3172d281b4928353072d15a15f2cebbb7a1fd8d973880d5166ca",
      "git_blob_sha": "598b4cdf62021a66b54c22b71171722027f1c0b5",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-mu001-science-complete-ready.json",
      "name": "fixed-fejer-meridian-bhalf-mu001-science-complete-ready.json"
    },
    "params20": {
      "bytes": 50679,
      "sha256": "ce445da032ffedff5e03e40b89e09096cba3e7e147f256968774a6c6e72d21b4",
      "git_blob_sha": "8eee403a87c988cb36fb55f6f82eb3ad0e1988db",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-mu001-complete-parameter-delivery.json",
      "name": "fixed-fejer-bhalf-mu001-complete-parameter-delivery.json"
    },
    "post20": {
      "bytes": 50424,
      "sha256": "d106770d9192c2eeaa24063f52658769a02e327c12c6a3650a71a6eae7894103",
      "git_blob_sha": "797d7803f1b98c138d28215ad4698f015c3628fe",
      "name": "fixed-fejer-bhalf-mu001-complete-moment-mesh-parameter-delivery.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-mu001-complete-moment-mesh-parameter-delivery.json"
    },
    "moments20": {
      "name": "fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
      "bytes": 89824,
      "sha256": "acdff6053f81e252bc82a83b5cdd082d24fb888b03e91905fc3ae6c7d7219e48",
      "git_blob_sha": "e8df07d79e268650ad82ce1bd586d34fa681490e"
    }
  },
  "binding_definition": {
    "schema": "complete-fixed-fejer-bhalf-mu001-R723-parameter-binding-v1",
    "repository": "Rogerhu12/math-research-public",
    "topic": "topics/visible-flex-larger-amplitude",
    "runtime_changes": [],
    "scientific_calls": 0,
    "refs_or_queues_modified": false,
    "known_official_launch": {
      "run_id": 46079535427,
      "attempt": 1,
      "run_started_at": "2026-11-27T22:55:41Z",
      "status": "in_progress",
      "complete_launch_publication_commit": "85cd235221ace28158625a7ced52a24551b509eb",
      "official_head_sha": null,
      "run_id_not_a_scientific_input_model_or_point_identity": true
    },
    "known_launch_is_not_a_field_reference_model_or_fee_identity": true,
    "complete_current_scientific_projection": {
      "complete_scientific_parameter_file": {
        "bytes": 97019,
        "sha256": "89b437a4986b3172d281b4928353072d15a15f2cebbb7a1fd8d973880d5166ca",
        "git_blob_sha": "598b4cdf62021a66b54c22b71171722027f1c0b5",
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-mu001-science-complete-ready.json",
        "name": "fixed-fejer-meridian-bhalf-mu001-science-complete-ready.json"
      },
      "complete_pure_parameter_file": {
        "role": "pure",
        "name": "fixed-fejer-meridian-bhalf-mu001-pure-complete-ready.json",
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-mu001-pure-complete-ready.json",
        "sha256": "f627447f7887bdc9d7f257b4d0772173556683501cd5fa9f1e39890ec7ac7f64",
        "bytes": 86221,
        "git_blob_sha": "53655fce8344040770e02295898a1c4ae9a06ebf"
      },
      "complete_scientific_parameter_delivery": {
        "bytes": 50679,
        "sha256": "ce445da032ffedff5e03e40b89e09096cba3e7e147f256968774a6c6e72d21b4",
        "git_blob_sha": "8eee403a87c988cb36fb55f6f82eb3ad0e1988db",
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-mu001-complete-parameter-delivery.json",
        "name": "fixed-fejer-bhalf-mu001-complete-parameter-delivery.json"
      },
      "current_scientific_script": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_meridian_batched_actions.py",
      "current_complete_scientific_argv": [
        "--repo",
        "{repo}",
        "--reference-bundle",
        "{work}/fixed-fejer-reference/reference.npz",
        "--preparation-report",
        "{work}/fixed-fejer-reference/report.json",
        "--carrier",
        "{work}/fixed-fejer-reference/observations.npz",
        "--node-report",
        "{work}/fixed-fejer-r690-inputs/fixed-affine-nodes.json",
        "--scalar-input",
        "{work}/fixed-fejer-r690-inputs/fixed-scalar-input.json",
        "--angles",
        "2048",
        "--stage-block",
        "64",
        "--angle-block",
        "8",
        "--integration-order",
        "8",
        "--norm-kind",
        "jet-sum",
        "--radial-norm-length",
        ".05",
        "--angular-transition",
        "24",
        "--torch-threads",
        "4",
        "--damping",
        ".01",
        "--directions",
        "1",
        "--maxiter",
        "16",
        "--restoration-directions",
        "4",
        "--restoration-damping",
        ".001",
        "--restoration-maxiter",
        "64",
        "--line-trials",
        "15",
        "--active-rows",
        "192",
        "--qp-atol",
        "0",
        "--qp-rtol",
        "1e-6",
        "--reach-ratio",
        ".03",
        "--reach-safety-factor",
        ".992",
        "--active-band",
        ".025",
        "--marked-diameter-budget",
        "4.2",
        "--witness-lower-budget",
        ".9",
        "--amplitude-height-floor",
        "1.01",
        "--spectral-p",
        "4",
        "--spectral-epsilon",
        ".001",
        "--spectral-scale",
        ".05",
        "--legacy-fraction",
        ".5",
        "--target",
        "1e-9",
        "--outdir",
        "{work}/fixed-fejer-meridian-batched-bhalf-mu001-first",
        "--panels",
        "128",
        "--endpoint-bubble-1-left",
        "1/32",
        "--endpoint-bubble-1-middle",
        "1/4",
        "--endpoint-bubble-1-right",
        "15/32",
        "--endpoint-bubble-2-left",
        "17/32",
        "--endpoint-bubble-2-middle",
        "3/4",
        "--endpoint-bubble-2-right",
        "31/32",
        "--endpoint-root-tolerance",
        "2e-12",
        "--endpoint-root-iterations",
        "24",
        "--endpoint-root-backtracks",
        "18",
        "--endpoint-root-armijo",
        "1e-4",
        "--moment-definition-sha256",
        "05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e",
        "--moment-input",
        "{repo}/topics/visible-flex-larger-amplitude/computations/frozen-zero-moment-Q-actual16-parameters.json",
        "--moment-input-sha256",
        "df11d8a4b36eb9ce113b5961863191c9b58cb2473af9c48e1714026041a42e2c",
        "--endpoint-control-radius",
        "2",
        "--gamma-left",
        "1/16",
        "--gamma-middle",
        "1/8",
        "--gamma-right",
        "3/16",
        "--moment-input-binding",
        "supported-smooth-triangle-reference",
        "--normal-stages",
        "32",
        "--seed-boundary-total-length",
        "1/2",
        "--seed-profile-delta",
        "1/32",
        "--seed-radial-quadrature-order",
        "8",
        "--seed-profile-quadrature-order",
        "16",
        "--seed-mean-maxiter",
        "128",
        "--seed-mean-tolerance",
        "2e-12",
        "--seed-mean-backtracks",
        "24",
        "--seed-mean-armijo",
        "1e-4",
        "--seed-scalar-iterations",
        "64",
        "--manifest",
        "{work}/fixed-fejer-reference/locations.json",
        "--material-envelope-binding",
        "{work}/fixed-fejer-reference/material-envelope-carrier-binding.json",
        "--envelope-near-active-rows",
        "32",
        "--independent-envelope-branch",
        "--pending-parallel-envelope-run",
        "45909290354/1",
        "--pending-parallel-envelope-source",
        "45909290354/1=cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5",
        "--pending-parallel-envelope-run",
        "45929088658/1",
        "--pending-parallel-envelope-source",
        "45929088658/1=95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9",
        "--pending-parallel-envelope-run",
        "45943410994/1",
        "--pending-parallel-envelope-source",
        "45943410994/1=ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5",
        "--pending-parallel-envelope-run",
        "45972294636/1",
        "--pending-parallel-envelope-source",
        "45972294636/1=c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1",
        "--pending-parallel-envelope-run",
        "46011377225/1",
        "--pending-parallel-envelope-source",
        "46011377225/1=477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd"
      ],
      "full_scientific_formal_and_live_maps_location": "The entire original steps[0].summary and steps[0].progress_summary in the exact complete science file above; no map is shortened or rewritten",
      "scientific_argument_words": 157,
      "scientific_formal_fields": 458,
      "pure_argument_words": 7,
      "pure_formal_fields": 445,
      "scientific_live_fields": 48,
      "exact_science_delta_from_complete_run19_parent": {
        "science": {
          "numerical_parameter_change_only": true,
          "original_step_id": "complete-fixed-fejer-meridian-batched-bhalf-first-20261127",
          "current_step_id": "complete-fixed-fejer-meridian-batched-bhalf-mu001-first-20261127",
          "original_scope": "Complete b/S=1/2, delta=1/32 independent same-fixed-g science; all original parameters and domains retained except the documented seed input. Full prior step scopes are preserved separately as parameter provenance.",
          "current_scope": "Complete independent same-fixed-g M160/J923/N2048/32-stage science with b/S=1/2, delta=1/32 and initial restoration damping .001. The complete run19 parent differs only by restoration damping .01 and its output namespace. Metric damping remains .01. Every original free variable, root/QP/restoration/line-search budget, equation, row, domain, acceptance rule and all known or unknown peer obligations remain. This starts from the genuine new runner's two necessary reference inputs and original frozen-reference initial point, without inheriting run19's field or history.",
          "complete_argv_location": "steps[0].args retains every current word; exact_changed_argv_words reverses it to every original parent word, also retained in the whole pinned parent file",
          "exact_changed_argv_words": [
            {
              "index": 37,
              "before": ".01",
              "after": ".001"
            },
            {
              "index": 71,
              "before": "{work}/fixed-fejer-meridian-batched-bhalf-first",
              "after": "{work}/fixed-fejer-meridian-batched-bhalf-mu001-first"
            }
          ],
          "counts": {
            "argv_words": 157,
            "formal_fields": 458,
            "live_fields": 48
          },
          "all_original_non_argument_step_fields_preserved_except_namespace_and_current_scope": true,
          "no_runtime_source_or_algorithm_or_budget_change": true,
          "original_common_slack_and_true_acceptance_rules_preserved": true,
          "same_original_coordinate_norm_and_full_selected_rows": true,
          "exact_QP_only_comparison_scope": "same entire feasible linear constraint set and exact global QP minimizers; nonnegative optimal tau does not increase as mu decreases",
          "finite64_inner_step_or_full_nonlinear_improvement_guarantee": false,
          "actual_cause_of_previous_small_progress_identified": false,
          "actual_prior_step_alpha_QP_status_gradient_norm_or_true_model_ratio_not_invented": true
        },
        "pure": {
          "numerical_parameter_change_only": true,
          "original_step_id": "actual-fixed-fejer-meridian-batched-bhalf-first-20261127",
          "current_step_id": "actual-fixed-fejer-meridian-batched-bhalf-mu001-first-20261127",
          "original_scope": "Complete b/S=1/2, delta=1/32 independent same-fixed-g pure; all original parameters and domains retained except the documented seed input. Full prior step scopes are preserved separately as parameter provenance.",
          "current_scope": "Complete original stdlib reader of the actual bhalf-mu001 scientific report and full source/model/point/geometry/packet bindings. The runtime source and all original selectors are unchanged; missing or partial scientific outputs remain missing or partial, and no F/J/root or scientific acceptance is added.",
          "complete_argv_location": "steps[0].args retains every current word; exact_changed_argv_words reverses it to every original parent word, also retained in the whole pinned parent file",
          "exact_changed_argv_words": [
            {
              "index": 3,
              "before": "{work}/fixed-fejer-meridian-batched-bhalf-first/report.json",
              "after": "{work}/fixed-fejer-meridian-batched-bhalf-mu001-first/report.json"
            },
            {
              "index": 5,
              "before": "{work}/postprocess/fixed-fejer-meridian-batched-bhalf-first-readout.json",
              "after": "{work}/postprocess/fixed-fejer-meridian-batched-bhalf-mu001-first-readout.json"
            }
          ],
          "counts": {
            "argv_words": 7,
            "formal_fields": 445,
            "live_fields": 0
          },
          "all_original_non_argument_step_fields_preserved_except_namespace_and_current_scope": true,
          "no_runtime_source_or_algorithm_or_budget_change": true,
          "original_common_slack_and_true_acceptance_rules_preserved": true,
          "same_original_coordinate_norm_and_full_selected_rows": true,
          "exact_QP_only_comparison_scope": "same entire feasible linear constraint set and exact global QP minimizers; nonnegative optimal tau does not increase as mu decreases",
          "finite64_inner_step_or_full_nonlinear_improvement_guarantee": false,
          "actual_cause_of_previous_small_progress_identified": false,
          "actual_prior_step_alpha_QP_status_gradient_norm_or_true_model_ratio_not_invented": true
        }
      },
      "current_namespace": "fixed-fejer-meridian-batched-bhalf-mu001-first",
      "actual_science_report": "{work}/fixed-fejer-meridian-batched-bhalf-mu001-first/report.json",
      "actual_science_command": "{work}/fixed-fejer-meridian-batched-bhalf-mu001-first-command.json",
      "planned_seed_parameters": {
        "relative_boundary_total_length": "1/2",
        "profile_delta": "1/32",
        "each_of_four_boundary_layers_relative_length": "1/8",
        "combined_central_relative_length": "3/8",
        "each_of_two_central_relative_length": "3/16",
        "input_domain_is_legal": true,
        "actual_mean_root_and_angular_jets_proved": false,
        "metric_or_geometric_improvement_assumed": false
      },
      "planned_initial_restoration_damping": "0.001",
      "planned_metric_damping": "0.01",
      "current_actual_damping_must_be_read_from_true_model_and_report": true,
      "all_original_scientific_variables_rows_domains_norm_thresholds_stopping_rules_and_budgets_retained": true,
      "future_field_result_or_improvement_not_implied": true
    },
    "complete_current_moment_post_delivery": {
      "bytes": 50424,
      "sha256": "d106770d9192c2eeaa24063f52658769a02e327c12c6a3650a71a6eae7894103",
      "git_blob_sha": "797d7803f1b98c138d28215ad4698f015c3628fe",
      "name": "fixed-fejer-bhalf-mu001-complete-moment-mesh-parameter-delivery.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-mu001-complete-moment-mesh-parameter-delivery.json"
    },
    "complete_current_original_R716_ready": {
      "name": "fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
      "bytes": 89824,
      "sha256": "acdff6053f81e252bc82a83b5cdd082d24fb888b03e91905fc3ae6c7d7219e48",
      "git_blob_sha": "e8df07d79e268650ad82ce1bd586d34fa681490e"
    },
    "complete_current_original_R716_producer_step_origin": {
      "whole_ready": {
        "name": "fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
        "bytes": 89824,
        "sha256": "acdff6053f81e252bc82a83b5cdd082d24fb888b03e91905fc3ae6c7d7219e48",
        "git_blob_sha": "e8df07d79e268650ad82ce1bd586d34fa681490e"
      },
      "json_pointer": "/steps/0",
      "step_id": "actual-fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-R716-whole-closed-flux-integrals-20261127",
      "whole_step_object_preserved": true
    },
    "current_geometry_and_normal_paths": {
      "normal": "{work}/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-normal-root-and-sixjet-fees-v1/report.json",
      "geometry": "{work}/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-continuous-gram-curvature-support-v1/report.json",
      "closed": "{work}/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-closed-phase-grip-v1/report.json",
      "closed_sidecar": "{work}/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-closed-phase-grip-v1/R716-unmarked-outward-tube.json",
      "moments": "{work}/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-r716-complete-moment-integrals/report.json",
      "centred": "{work}/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-r716-complete-centred-moments/report.json",
      "mesh_final": "{work}/fixed-fejer-meridian-batched-bhalf-mu001-first-same-field-phase-mesh-final-v1/report.json",
      "mesh_packet": "{work}/fixed-fejer-meridian-batched-bhalf-mu001-first-same-field-phase-mesh-packet-v1/report.json"
    },
    "current_sibling_parameter_records": [
      {
        "role": "normal",
        "path": "computations/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-normal32-full-circle-sixjet-fees-ready.json",
        "bytes": 61812,
        "sha256": "e0b3728a65788157abb245058fccbc477714e181ec34da8e9d1459a555a28d3e",
        "git_blob_sha": "d2dfbda375f6dc896d994de865ccd40017066757"
      },
      {
        "role": "geometry",
        "path": "computations/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-continuous-gram-curvature-support-ready.json",
        "bytes": 59207,
        "sha256": "d971eeb39b6c3b40b1531f68b8f10a039161a441ff1f19255b754305a6ab461a",
        "git_blob_sha": "6f1da76a472d17f54512855e71ad946016b87061"
      },
      {
        "role": "closed",
        "path": "computations/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-closed-phase-grip-r718-ready.json",
        "bytes": 92335,
        "sha256": "a6277fb071145363b2533e59e6aafd86f2ca4ba4b9a40579ed461846fb9964f6",
        "git_blob_sha": "e60b4bbcf83f7b9457b40ae4ba40d46ea6c3e34f"
      }
    ],
    "shared_full_runtime_files": {
      "R723": {
        "name": "fixed_fejer_R723_directional_closed_phase_grip_evidence.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_directional_closed_phase_grip_evidence.py",
        "bytes": 87670,
        "sha256": "1782eebd539ae47367260008c00b6a3912fe1fec26d30c22a8f0a7329a0309dc",
        "expected_blob": "94a33898b3b86646d207b3018d26069eaffd8797",
        "git_blob_sha": "94a33898b3b86646d207b3018d26069eaffd8797"
      },
      "R716_consumer": {
        "name": "fixed_fejer_R723_compatible_r716_centred_volume_moment.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_r716_centred_volume_moment.py",
        "bytes": 61706,
        "sha256": "3c0d6cfd5280b7cb250b1a8ff2077c849a20f725169d0f667c74eb975c3c294b",
        "git_blob_sha": "3ae6dd08dfcbb00002fa2482ec49cf7e56d86ea4"
      },
      "complete_unchanged_source_delivery": {
        "name": "R723-directional-closed-grip-R716-complete-delivery.json",
        "path": "topics/visible-flex-larger-amplitude/computations/R723-directional-closed-grip-R716-complete-delivery.json",
        "bytes": 48223,
        "sha256": "b16346ee6f96d8aedc0f89a2ad6598a53b86af05cb1c3171ec1790e53bb896cc",
        "git_blob_sha": "1929f73367894f35c92e6dfa86198a70889c4da0"
      }
    },
    "complete_original_parameter_history": {
      "R723_closed_parent": {
        "name": "fixed-fejer-meridian-batched-bhalf-first-R723-directional-closed-phase-grip-ready.json",
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R723-directional-closed-phase-grip-ready.json",
        "bytes": 86836,
        "sha256": "5a072e9c1030f146f46084d3b395300f7c79b52bb0c88830a55d0b3188464d9f",
        "git_blob_sha": "80e5cf779dbe6d8bb811561aaf55da036669eca0"
      },
      "R723_R716_parent": {
        "name": "fixed-fejer-meridian-batched-bhalf-first-R723-complete-R716-moment-ready.json",
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R723-complete-R716-moment-ready.json",
        "bytes": 97718,
        "sha256": "11667d388e2d71d7583891aac274cfe7ea71810b123f9262f4a8ed85e90986c3",
        "git_blob_sha": "a5111bec896c7a83e598a9ea26f1372b80b309dc"
      },
      "original_closed_source_and_R716_source_and_parameters_delivery": {
        "name": "R723-directional-closed-grip-R716-complete-delivery.json",
        "path": "topics/visible-flex-larger-amplitude/computations/R723-directional-closed-grip-R716-complete-delivery.json",
        "bytes": 48223,
        "sha256": "b16346ee6f96d8aedc0f89a2ad6598a53b86af05cb1c3171ec1790e53bb896cc",
        "git_blob_sha": "1929f73367894f35c92e6dfa86198a70889c4da0"
      },
      "source": "Each named full original file is preserved without removing any top-level or nested field. Every original parameter/history/provenance object is inherited by exact whole-file reference as history, and remains available byte for byte. Only the new current steps and explicit scientific projection in this package are executable run20 parameters.",
      "all_previous_unknown_peer_and_parent_history_retained": true,
      "old_run19_field_root_or_fee_values_not_current_inputs": true,
      "original_full_137_source_roles_and_all_120_historical_source_pairs_unchanged": true
    },
    "complete_external_unregistered_peer_obligations": [
      [
        "46028002241/1",
        "2ccf1d251e83850428c577fd522eeadbadd53df79c6f234848ad1eb8b94ccae4"
      ],
      [
        "46028184571/1",
        "fff956cc086c8f69c7de87c2d9117792b6b1d5e1de853e59a992fb67e04b4e51"
      ],
      [
        "46031953783/1",
        "97ae6ab8a2a19a07b134efc611b442d9e9113ca0b68c0cd322a45ec175d0f8fd"
      ],
      [
        "46037017666/1",
        "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d"
      ],
      [
        "46053911348/1",
        "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d"
      ],
      [
        "46062343475/1",
        "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f"
      ],
      [
        "46076669320/1",
        "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f"
      ]
    ],
    "complete_external_peer_status": "Original five supported CLI pairs and all historical unknowns remain unchanged. Additional external runs are declarations of provenance and unknown whole scientific history, not typed-transfer inputs or evidence of accepted/final fields. Runs12-15 official cancellations are preserved separately; those terminations do not manufacture missing scientific state. The actual independent run19 is additionally retained as an external unknown whole history; no run19 returned/final/typed state is assumed or inserted into the unchanged original five supported CLI pairs.",
    "supported_original_five_CLI_peer_pairs_unchanged": true,
    "all_existing_history_is_unknown_until_proper_real_source_consumption": true,
    "R723_entire_physical_scope": {
      "exact_phi_over_pi": [
        "0",
        "2"
      ],
      "exact_radial_affine": [
        [
          "0",
          "0"
        ],
        [
          "1",
          "0"
        ]
      ],
      "all_original_normal_stages": 32,
      "current_M": 160,
      "reference_M": 160,
      "current_J": 923,
      "current_full_N": 2048,
      "complete_current_field_fixed": true,
      "all_physical_sixjets_and_raw_closure_lifts": true,
      "all_original_whole_support_rows": true,
      "upper_lower_both_marked_caps": true,
      "physical_t": [
        "0",
        "1"
      ],
      "physical_alpha_over_pi": [
        "0",
        "1/2"
      ],
      "fixed_rh": "9/20",
      "mark_height": "1/1000",
      "cap_recipe": "R661-fixed-p4-outward-cap-graphs-v1",
      "target_reach_ratio": "3/100",
      "relative_Gram_operator_target": "1/1000000",
      "grip_fraction": "1/5",
      "delta_hold_standard_fraction": "1/20",
      "delta_hold_stronger_fraction": "1/5",
      "current_scalar_reconstruction_leaves": 2218,
      "current_full_reference_observation_count": 7377,
      "current_fixed_target_recipe": "predeclared-RN-even-dyadic-Fejer-R690",
      "original_complete_box_distance_retained": true,
      "optional_R718_full_marked_target_flow_distance": true,
      "actual_current_core_coefficients_used_for_ratio": 160,
      "optional_R719_constant_only_with_complete_hypotheses": "7/3",
      "optional_positive_log_terms": 32,
      "optional_positive_exp_terms": 32,
      "optional_exact_downward_binary_bits": 96,
      "optional_bound_changes_solver_or_domain": false,
      "seed_boundary_total_length_relative": "1/2",
      "seed_profile_delta": "1/32",
      "seed_uses_actual_complete_report_definition": true,
      "independent_R723_directional_normal_flow_theorem": true,
      "same_complete_activity_curvature_and_diameter": true,
      "complete_mixed_pair_joint_normal_map_injectivity_from_R723": true,
      "common_beta_affine_leaf_conditions": "w*(a+beta*b)-tau*(Nx^2+Ny^2+beta*Nz^2)>=0",
      "fixed_cap_complete_directional_inequalities": true,
      "all_phase_lower_reflection_and_cap_rows_share_one_beta": true,
      "original_R650_target_no_longer_a_prerequisite": true,
      "actual_R718_support_sigma_is_not_replaced_by_directional_radius": true,
      "independent_unmarked_flat_cap_directional_radius_is_H": true
    },
    "R723_new_output_roles": {
      "distinct_R723_directional_evidence_roles": 5,
      "original_beta_evidence_roles_asserted": 0,
      "all_eight_original_beta_evidence_roles_paid": false,
      "original_beta_read_input_or_consume_executed": false,
      "original_R650_target_pass_required": false,
      "original_R650_interval_and_bound_retained_as_comparison": true,
      "all_original_geometry_streams_reread_and_linked_in_every_complete_cover": true,
      "all_137_scientific_roles_and_original_120_source_pairs_retained": true,
      "exact_all_original_leaf_ranges_and_whole_records_produced": true,
      "range_packaging_count_does_not_omit_any_mathematical_leaf": true,
      "final_complete_main_report_and_exact_sidecars_required": true,
      "marked_R723_ratio_and_actual_R718_sigma_are_distinct": true,
      "unmarked_R716_tube_is_independently_recomputed_from_activity_and_flat_caps": true,
      "optional_R718_only_after_complete_R723_closed_outward_support": true,
      "old_complete_box_distance_retained_and_final_bound_is_maximum": true,
      "no_twelve_moment_integrals_or_delta_E_produced_here": true,
      "late_failed_or_unpaid_outputs_cannot_be_used_as_certificates": true
    },
    "R716_entire_independent_consumption_contract": {
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
    },
    "future_actual": {
      "reference_file_records": null,
      "input_binding_sha256": null,
      "model_identity_sha256": null,
      "full_point_sha256": null,
      "snapshot_record": null,
      "final_checkpoint": null,
      "science_report": null,
      "normal_fee_report": null,
      "geometry_report": null,
      "R723_report": null,
      "moment_report": null,
      "centred_moment_result": null,
      "delta_E_lower": null
    },
    "operation_scope": {
      "all_complete_runtime_sources_shared_without_relabeling_or_rewriting": true,
      "all_current_postprocessing_numeric_parameters_and_budgets_unchanged": true,
      "all_original_complete_8_10_8_argv_and_77_34_65_selector_maps_retained": true,
      "no_run19_moment_producer_step_in_current_plan": true,
      "no_duplicate_of_current_run20_producer_if_already_queued_or_returned": true,
      "actual_original_normal_snapshot_required_not_progress_or_prepared_parameters": true,
      "inherited_full_metadata_is_preserved_in_complete_parent_files_not_discarded": true,
      "new_independent_AST_fixture_reviewer_or_admission_gate": false
    },
    "parameter_reproducer_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_bhalf_mu001_R723_complete_parameters.mjs"
  },
  "closed_metadata": {
    "schema": "complete-fixed-fejer-bhalf-mu001-R723-closed-parameter-ready-v1",
    "scientific_execution_only_in_public_Actions": true,
    "executed": false,
    "admitted": false,
    "complete_current_parameter_binding": {
      "name": "fixed-fejer-bhalf-mu001-R723-complete-parameter-binding.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-mu001-R723-complete-parameter-binding.json",
      "bytes": 27741,
      "sha256": "fe5df0cee988753e710c1971fd7952fd1f8b465a58f004473d7310d228ce090b",
      "git_blob_sha": "cd97924e283d44b3662083c12e2588aef3c3d306"
    },
    "complete_history_is_inherited_from_full_hash_bound_original_files": true,
    "no_parent_metadata_source_or_parameter_field_removed": true,
    "no_runtime_source_rewrite": true,
    "known_current_official_run_id": "46079535427",
    "known_current_official_run_attempt": 1,
    "future_actual_field_model_point_snapshot_and_fee_identities": null,
    "current_scientific_namespace": "fixed-fejer-meridian-batched-bhalf-mu001-first",
    "new_solver_admission_gate": false,
    "full_parameter_reproducer_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_bhalf_mu001_R723_complete_parameters.mjs",
    "complete_immediate_parameter_parent": {
      "name": "fixed-fejer-meridian-batched-bhalf-first-R723-directional-closed-phase-grip-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R723-directional-closed-phase-grip-ready.json",
      "bytes": 86836,
      "sha256": "5a072e9c1030f146f46084d3b395300f7c79b52bb0c88830a55d0b3188464d9f",
      "git_blob_sha": "80e5cf779dbe6d8bb811561aaf55da036669eca0"
    },
    "complete_current_source": {
      "name": "fixed_fejer_R723_directional_closed_phase_grip_evidence.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_directional_closed_phase_grip_evidence.py",
      "bytes": 87670,
      "sha256": "1782eebd539ae47367260008c00b6a3912fe1fec26d30c22a8f0a7329a0309dc",
      "expected_blob": "94a33898b3b86646d207b3018d26069eaffd8797",
      "git_blob_sha": "94a33898b3b86646d207b3018d26069eaffd8797"
    },
    "original_and_current_argv_words": 8,
    "original_66_selector_map_preserved": true,
    "complete_current_scalar_selector_count": 77,
    "entire_original_full_scope_and_output_roles": {
      "name": "fixed-fejer-bhalf-mu001-R723-complete-parameter-binding.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-mu001-R723-complete-parameter-binding.json",
      "bytes": 27741,
      "sha256": "fe5df0cee988753e710c1971fd7952fd1f8b465a58f004473d7310d228ce090b",
      "git_blob_sha": "cd97924e283d44b3662083c12e2588aef3c3d306"
    },
    "all_other_step_fields_preserved_except_namespace_step_id_and_current_scope": true
  },
  "moment_metadata": {
    "schema": "complete-fixed-fejer-bhalf-mu001-R723-R716-parameter-ready-v1",
    "scientific_execution_only_in_public_Actions": true,
    "executed": false,
    "admitted": false,
    "complete_current_parameter_binding": {
      "name": "fixed-fejer-bhalf-mu001-R723-complete-parameter-binding.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-mu001-R723-complete-parameter-binding.json",
      "bytes": 27741,
      "sha256": "fe5df0cee988753e710c1971fd7952fd1f8b465a58f004473d7310d228ce090b",
      "git_blob_sha": "cd97924e283d44b3662083c12e2588aef3c3d306"
    },
    "complete_history_is_inherited_from_full_hash_bound_original_files": true,
    "no_parent_metadata_source_or_parameter_field_removed": true,
    "no_runtime_source_rewrite": true,
    "known_current_official_run_id": "46079535427",
    "known_current_official_run_attempt": 1,
    "future_actual_field_model_point_snapshot_and_fee_identities": null,
    "current_scientific_namespace": "fixed-fejer-meridian-batched-bhalf-mu001-first",
    "new_solver_admission_gate": false,
    "full_parameter_reproducer_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_bhalf_mu001_R723_complete_parameters.mjs",
    "complete_immediate_R723_consumer_parameter_parent": {
      "name": "fixed-fejer-meridian-batched-bhalf-first-R723-complete-R716-moment-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R723-complete-R716-moment-ready.json",
      "bytes": 97718,
      "sha256": "11667d388e2d71d7583891aac274cfe7ea71810b123f9262f4a8ed85e90986c3",
      "git_blob_sha": "a5111bec896c7a83e598a9ea26f1372b80b309dc"
    },
    "complete_actual_run20_original_R716_producer_parameter_parent": {
      "name": "fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
      "bytes": 89824,
      "sha256": "acdff6053f81e252bc82a83b5cdd082d24fb888b03e91905fc3ae6c7d7219e48",
      "git_blob_sha": "e8df07d79e268650ad82ce1bd586d34fa681490e"
    },
    "complete_current_consumer_source": {
      "name": "fixed_fejer_R723_compatible_r716_centred_volume_moment.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R723_compatible_r716_centred_volume_moment.py",
      "bytes": 61706,
      "sha256": "3c0d6cfd5280b7cb250b1a8ff2077c849a20f725169d0f667c74eb975c3c294b",
      "git_blob_sha": "3ae6dd08dfcbb00002fa2482ec49cf7e56d86ea4"
    },
    "complete_original_run20_producer_step_object_preserved": true,
    "no_run19_producer_is_queued": true,
    "original_producer_argv": 10,
    "original_producer_selectors": 34,
    "producer_seconds": 600,
    "maximum_angle_blocks": 0,
    "consumer_argv": 8,
    "original_60_consumer_selectors_preserved": true,
    "complete_consumer_selector_count": 65,
    "if_identical_run20_producer_already_queued_or_returned_use_only_second_step": true
  },
  "output_records": [
    {
      "name": "fixed-fejer-bhalf-mu001-R723-complete-parameter-binding.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-mu001-R723-complete-parameter-binding.json",
      "bytes": 27741,
      "sha256": "fe5df0cee988753e710c1971fd7952fd1f8b465a58f004473d7310d228ce090b",
      "git_blob_sha": "cd97924e283d44b3662083c12e2588aef3c3d306"
    },
    {
      "name": "fixed-fejer-meridian-batched-bhalf-mu001-first-R723-directional-closed-phase-grip-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-mu001-first-R723-directional-closed-phase-grip-ready.json",
      "bytes": 11483,
      "sha256": "b027d255f244b311d6763b316238d93995d8688e9ff5b1f0d6277e22d0094fc5",
      "git_blob_sha": "518ee8bfd7c2142ee187bb4fd37ecbd90cf9f32f"
    },
    {
      "name": "fixed-fejer-meridian-batched-bhalf-mu001-first-R723-complete-R716-moment-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-mu001-first-R723-complete-R716-moment-ready.json",
      "bytes": 15645,
      "sha256": "0ccb05e741eea9d33488e891e532728b9a8cd071e8a43f21b8d16c8fdff0ffa0",
      "git_blob_sha": "8385a3e2abb4ebd1963ebf26ccdd9db4af65209d"
    }
  ],
  "old_namespace": "fixed-fejer-meridian-batched-bhalf-first",
  "current_namespace": "fixed-fejer-meridian-batched-bhalf-mu001-first",
  "closed_step_id": "actual-fixed-fejer-bhalf-mu001-R723-directional-whole-closed-phase-grip-first-20261127",
  "closed_scope": "Read the genuine same-point complete 6c57/c6b07 geometry and all original normal32/root/whole-circle/exact-radial/sixjet records under the exact 137-role 10fa/8027/76185/c750 producer-bound family. Reuse the complete 002eb current-core, C2 lower reflection/Cartesian caps, exact fixed-chart R248 phase, complete all-target image boxes and fixed grip functions. Independently instantiate published R723 from one beta>0 over every original leaf: w*A_beta(F).N-tau*N.A_beta.N>=0, the actual whole-domain curvature bound, and both full p4 cap inequalities. The full joint flow ordering supplies all-phase normal-tube injectivity and mixed-pair reach; it does not remove the curvature condition. Preserve the old R650 parameter intervals and reach as comparisons, without requiring their target to pass and without fabricating any of the original eight exact beta claims. The five new directional roles, all source-linked range records, complete field/cover and sidecar are usable only through the final complete main report and its entire input/output byte recheck. Every original full leaf and stream is consumed, irrespective of packaging into ranges of 4096. Read all actual 160 current core words, distinguish fixed reference M160, and retain all six actual input files, seed/R722 posterior branch, full 32-stage/gluing/domain/periodicity and 137 source obligations. The complete marked support sigma remains separate from the R723 directional radius and supplies the optional unchanged R718 lower bound; preserve the full original box lower and take the maximum. Independently rederive the unmarked flat-cap directional reach using the same actual activity, require the strict 1/1000 outward-tube margin, and retain R716 section6 additivity as separate from its unpaid twelve integrals and centred invariant. No F/J/root/accurate-integrand or new field is evaluated, no old result/progress is accepted as a snapshot, no science source/variable/budget changes. Missing full hypotheses remain null; completion means full consumption rather than satisfaction of the geometric problem. The only new initial field definition is the already-declared run20 same-g supported seed b/S=1/2, delta=1/32; its actual complete report and point have not been supplied. The complete current scientific parameter file is the run20 mu001 branch: the only scientific numerical change from run19 is initial restoration damping .01 to .001; metric damping remains .01. This postprocessing step changes no numerical fee parameter or theorem. The actual run20 full report/model/point/snapshot and accurate geometry are required; neither run19 values nor a known launch record supplies them.",
  "moment_step_id": "actual-fixed-fejer-bhalf-mu001-R723-compatible-complete-R716-centred-volume-moments-20261127",
  "moment_scope": "Read and rebind every complete same-point moment block, original journal, full source and actual field identity. Retain all twelve raw channels, both half-surfaces and both flat caps, exact p4 volume/first/mixed moments, and the full general R716(2) centred tensors at physical t=0,1/2,1. The simplified B_eff formula remains conditional on the actual full 32-stage signed half-turn inclusion. Consume the exact final R723 closed-phase main report through its complete independent validator: re-read all original geometry streams and directional ranges, complete normal32/radial/circle covers, source-bound C2/phase ports, one common beta, actual full point/model/snapshot/target and original normal binding. The independently rederived UNMARKED flat-cap tube must strictly exceed mark height 1/1000 before any body/additivity interpretation. The old d0fe full eight-role validator is preserved only as an exact separately sourced legacy branch; this R723 route leaves those claims false and does not require the old R650 target to pass. Late-failed or provisional main/sidecar records discharge nothing. Only a full bounded-body interpretation, positive total volume and a separated centred invariant enable the unchanged R625/R716 E(3)-quotient formulas. R722 mean existence and R718 holding distance do not replace those premises. The original 45ca moment producer and its entire 600-second/all-angle budget are retained without modification. No new working F/J/root, accurate field oracle, conditional reach assumption, scientific solver or admission gate is added; no future actual field or fee value is supplied. This is the run20 same-source bhalf-mu001 namespace. Its complete scientific parameters have restoration damping .001 and metric damping .01; this changes no moment or evidence formula/budget. All complete field and fee identities must come from the genuine run20 report, not from run19 or mutable progress."
};
const bytes=s=>Buffer.byteLength(s,"utf8");
const sha=s=>crypto.createHash("sha256").update(s,"utf8").digest("hex");
const blob=s=>crypto.createHash("sha1").update("blob "+bytes(s)+"\0").update(s,"utf8").digest("hex");
const copy=x=>JSON.parse(JSON.stringify(x));
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
function assert(ok,message){if(!ok)throw new Error(message);}
function transform(value,from,to){
 if(typeof value==="string")return value.split(from).join(to);
 if(Array.isArray(value))return value.map(x=>transform(x,from,to));
 if(value&&typeof value==="object")return Object.fromEntries(Object.entries(value).map(
  ([key,item])=>[key.split(from).join(to),transform(item,from,to)]));
 return value;
}
const argv=process.argv.slice(2),args={};
for(let i=0;i<argv.length;i+=2){assert(argv[i]?.startsWith("--")&&argv[i+1],"Complete arguments");
 assert(!Object.hasOwn(args,argv[i]),"Duplicate option");args[argv[i]]=argv[i+1];}
assert(Object.keys(args).length===2&&args["--parameter-directory"]&&args["--output-directory"],
 "Usage: --parameter-directory COMPLETE_PARENT_JSON_DIRECTORY --output-directory GENERATED_DIRECTORY");
const loaded={},raws={};
for(const [role,record]of Object.entries(SPEC.parents)){
 const raw=fs.readFileSync(path.join(args["--parameter-directory"],record.name),"utf8");
 assert(bytes(raw)===record.bytes&&sha(raw)===record.sha256&&blob(raw)===record.git_blob_sha,
  "Whole original parameter identity differs: "+role);
 loaded[role]=JSON.parse(raw);raws[role]=raw;
}
const binding=copy(SPEC.binding_definition),projection=binding.complete_current_scientific_projection;
assert(same(projection.current_complete_scientific_argv,loaded.science20.steps[0].args),"Every scientific argv word must match");
assert(same(projection.exact_science_delta_from_complete_run19_parent,loaded.params20.exact_parameter_deltas),"Exact science delta");
assert(same(projection.planned_seed_parameters,loaded.params20.planned_seed_parameters),"Complete planned seed definition");
assert(same(binding.known_official_launch,loaded.post20.known_current_official_launch_reported_by_root),"Original actual launch record");
assert(same(binding.complete_external_unregistered_peer_obligations,loaded.science20.external_unregistered_peer_obligations),"Whole peer obligations");
assert(same(binding.complete_external_peer_status,loaded.science20.external_peer_status),"Whole peer status history");
assert(same(binding.current_sibling_parameter_records,loaded.post20.current_sibling_parameter_records_reported_by_owner),"Complete sibling parameters");
assert(same(binding.R723_entire_physical_scope,loaded.closed19.full_scope),"Whole R723 domain");
assert(same(binding.R723_new_output_roles,loaded.closed19.output_roles),"Distinct complete evidence roles");
assert(same(binding.R716_entire_independent_consumption_contract,loaded.moments19.R723_independent_consumption_contract),"Whole R716 contract");
const words=projection.current_complete_scientific_argv;
assert(words.length===157&&words[36]==="--restoration-damping"&&words[37]===".001"&&
 words[words.indexOf("--damping")+1]===".01"&&words[71]==="{work}/"+SPEC.current_namespace,
 "Only the actual run20 complete scientific parameter projection is accepted");
const oldClosed=loaded.closed19.steps[0],oldMoment=loaded.moments19.steps[1];
const closedStep=transform(oldClosed,SPEC.old_namespace,SPEC.current_namespace);
closedStep.id=SPEC.closed_step_id;closedStep.scope=SPEC.closed_scope;
const momentStep=transform(oldMoment,SPEC.old_namespace,SPEC.current_namespace);
momentStep.id=SPEC.moment_step_id;momentStep.scope=SPEC.moment_scope;
const producer=copy(loaded.moments20.steps[0]);
assert(producer.args.length===10&&producer.args[7]==="600"&&producer.args[9]==="0"&&
 producer.args[3].includes(SPEC.current_namespace)&&producer.args[5].includes(SPEC.current_namespace),
 "Use the entire current run20 producer, never the run19 step");
function selectorMap(step){const all=Object.values(step.summary);assert(all.length===1,"Complete single report selector map");return all[0];}
assert(closedStep.args.length===8&&Object.keys(selectorMap(closedStep)).length===77,"Closed complete count");
assert(momentStep.args.length===8&&Object.keys(selectorMap(momentStep)).length===65,"Consumer complete count");
assert(Object.keys(selectorMap(producer)).length===34,"Producer complete count");
assert(same(selectorMap(closedStep),selectorMap(oldClosed))&&same(selectorMap(momentStep),selectorMap(oldMoment)),
 "No original selector may be omitted or altered");
for(const [current,original]of [[closedStep,oldClosed],[momentStep,oldMoment]]){
 const reverse=transform(current,SPEC.current_namespace,SPEC.old_namespace);
 reverse.id=original.id;reverse.scope=original.scope;
 assert(same(reverse,original),"Entire original step must be restored");
}
const closed={...copy(SPEC.closed_metadata),steps:[closedStep]};
const moments={...copy(SPEC.moment_metadata),steps:[producer,momentStep]};
const outputs=[binding,closed,moments];
for(let i=0;i<outputs.length;i++){
 const raw=JSON.stringify(outputs[i],null,2)+"\n",record=SPEC.output_records[i];
 assert(bytes(raw)===record.bytes&&sha(raw)===record.sha256&&blob(raw)===record.git_blob_sha,"Complete output bytes differ");
 fs.mkdirSync(args["--output-directory"],{recursive:true});
 const target=path.join(args["--output-directory"],record.name);
 if(fs.existsSync(target))assert(fs.readFileSync(target,"utf8")===raw,"Do not overwrite another parameter artifact");
 else fs.writeFileSync(target,raw,"utf8");
}
// All full original metadata remains the exact original bytes; only references
// are shared, not projections in place of the source documents.
for(const [role,record]of Object.entries(SPEC.parents)){
 assert(sha(raws[role])===record.sha256&&blob(raws[role])===record.git_blob_sha,
  "A complete retained history parent changed");
}
process.stdout.write(JSON.stringify({schema:SPEC.schema,parents:SPEC.parents,outputs:SPEC.output_records,
 entire_current_producer_step_preserved:true,entire_closed_and_consumer_step_inverse:true,
 all_full_history_parent_bytes_preserved:true,runtime_sources_changed:0,scientific_calls:0,
 new_solver_admission_gate:false})+"\n");
