#!/usr/bin/env node
/**
 * Complete text-only reproduction of the run16 same-field mesh sources and plans.
 * Reads each complete pinned parent and emits each full new source and JSON plan.
 * It does not import Python, run scientific modules, evaluate a field or solve.
 * Original all-domain mesh arithmetic and every numerical parameter are retained.
 * This utility is not an admission gate for the solver or the mesh producer.
 */
import { readFile, writeFile, mkdir } from "node:fs/promises";
import { resolve, join, basename, dirname } from "node:path";
import { createHash } from "node:crypto";

const SOURCE_JOBS = [
  {
    "role": "input",
    "parent": {
      "name": "fixed_fejer_same_field_mesh_input.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_same_field_mesh_input.py",
      "bytes": 73133,
      "sha256": "ad809cb428b7cdd6f3fe082a0057739ff191aefe4abb113e4595fe5e618f0036",
      "git_blob_sha": "9cfe9ac9db4760fe83775b2a51da25965670520c"
    },
    "output": {
      "name": "fixed_fejer_stage_observed_same_field_mesh_input.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_same_field_mesh_input.py",
      "bytes": 73265,
      "sha256": "b982e6d3ed8bb4e9615b5232932222bdb9298f95abfc9e3943875794f64a65d7",
      "git_blob_sha": "a1711adb4adbf08f860da5c106c91f23d1b8267d"
    },
    "patches": [
      {
        "label": "SCHEMA",
        "before": "SCHEMA = \"actual-fixed-fejer-same-field-complete-mesh-input-v1\"",
        "after": "SCHEMA = \"actual-fixed-fejer-stage-observed-same-field-complete-mesh-input-v1\"",
        "occurrences": 1
      },
      {
        "label": "DRIVER_NAME",
        "before": "DRIVER_NAME = \"fullclosed_fixed_fejer_immutable_point_so3_qp.py\"",
        "after": "DRIVER_NAME = \"fullclosed_fixed_fejer_stage_point_observed_so3_qp.py\"",
        "occurrences": 1
      },
      {
        "label": "DRIVER_SHA",
        "before": "DRIVER_SHA = \"477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd\"",
        "after": "DRIVER_SHA = \"8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d\"",
        "occurrences": 1
      },
      {
        "label": "READER_NAME",
        "before": "READER_NAME = \"read_fixed_fejer_immutable_point_so3_report.py\"",
        "after": "READER_NAME = \"read_fixed_fejer_stage_point_observed_so3_report.py\"",
        "occurrences": 1
      },
      {
        "label": "READER_SHA",
        "before": "READER_SHA = \"274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b\"",
        "after": "READER_SHA = \"c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f\"",
        "occurrences": 1
      },
      {
        "label": "LAUNCHER_SHA",
        "before": "LAUNCHER_SHA = \"0c1ff0aa2de30fcd490efb4bddd1972613c0f0afb1257d1af0170ac7e60bb5bf\"",
        "after": "LAUNCHER_SHA = \"ed81031fe1eb33684d35585e44022314c8a631821859376a200c874a2aa0e5fa\"",
        "occurrences": 1
      },
      {
        "label": "NORMAL_SHA",
        "before": "NORMAL_SHA = \"1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778\"",
        "after": "NORMAL_SHA = \"42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10\"",
        "occurrences": 1
      },
      {
        "label": "LAUNCHER_NAME",
        "before": "LAUNCHER_NAME = \"launch_fixed_fejer_immutable_point_actions.py\"",
        "after": "LAUNCHER_NAME = \"launch_fixed_fejer_stage_point_observed_actions.py\"",
        "occurrences": 1
      },
      {
        "label": "ACCURATE_INPUT_NAME",
        "before": "ACCURATE_INPUT_NAME = \"fixed_fejer_normal_packet_accurate_field_input.py\"",
        "after": "ACCURATE_INPUT_NAME = \"fixed_fejer_stage_observed_normal_packet_accurate_field_input.py\"",
        "occurrences": 1
      },
      {
        "label": "ACCURATE_INPUT_SHA",
        "before": "ACCURATE_INPUT_SHA = \"1e5101d7bd08a8b3787b6eaa699c915a9e8bd173d365233c7be90f1aee1b3f3f\"",
        "after": "ACCURATE_INPUT_SHA = \"720bbfc1071a3e56598fd096ec420e8cb5a44a60e06b28d33ff0f1c37e3038b3\"",
        "occurrences": 1
      },
      {
        "label": "CLOSED_SOURCE_NAME",
        "before": "CLOSED_SOURCE_NAME = \"fixed_fejer_complete_closed_phase_grip_evidence.py\"",
        "after": "CLOSED_SOURCE_NAME = \"fixed_fejer_stage_observed_closed_phase_grip_evidence.py\"",
        "occurrences": 1
      },
      {
        "label": "CLOSED_SOURCE_SHA",
        "before": "CLOSED_SOURCE_SHA = \"d606055d1b247d8354ac320bc28a0f40f4b00cbf1ff530a9b6bb2e80dec80bb9\"",
        "after": "CLOSED_SOURCE_SHA = \"eddc1fb7d10cc6a24f8245920b93babbf71886e550ceb1b0293b892323548aa9\"",
        "occurrences": 1
      },
      {
        "label": "CLOSED_SCHEMA",
        "before": "CLOSED_SCHEMA = \"actual-fixed-fejer-complete-closed-phase-grip-evidence-v1\"",
        "after": "CLOSED_SCHEMA = \"actual-fixed-fejer-stage-observed-complete-closed-phase-grip-evidence-v1\"",
        "occurrences": 1
      },
      {
        "label": "CLOSED_EVIDENCE_SCHEMA",
        "before": "CLOSED_EVIDENCE_SCHEMA = \"actual-fixed-fejer-same-point-optional-closed-evidence-v1\"",
        "after": "CLOSED_EVIDENCE_SCHEMA = \"actual-fixed-fejer-stage-observed-same-point-optional-closed-evidence-v1\"",
        "occurrences": 1
      },
      {
        "label": "GEOMETRY_SCHEMA",
        "before": "GEOMETRY_SCHEMA = \"actual-fixed-fejer-complete-continuous-gram-curvature-support-v1\"",
        "after": "GEOMETRY_SCHEMA = \"actual-fixed-fejer-stage-observed-complete-continuous-gram-curvature-support-v1\"",
        "occurrences": 1
      },
      {
        "label": "GEOMETRY_SHA",
        "before": "GEOMETRY_SHA = \"fcae1e5926e8e70edbd78a9e3b276f46e3b7b345b1ad2d6ec647905e6c5a4d2b\"",
        "after": "GEOMETRY_SHA = \"3f383d692711d180d0f7fd24e78ce67973c85b8c231e28deb135122664dd3560\"",
        "occurrences": 1
      },
      {
        "label": "complete scientific role count",
        "before": "    if len(value) != 110:",
        "after": "    if len(value) != 120:",
        "occurrences": 1
      },
      {
        "label": "complete role diagnostic",
        "before": "Keep all 110 actual fixed Fejer scientific source roles",
        "after": "Keep all 120 actual stage-observed fixed Fejer scientific source roles",
        "occurrences": 1
      },
      {
        "label": "unchanged constructor provenance",
        "before": "# The following contiguous constructor block is byte-identical to 477499 main.",
        "after": "# The following contiguous constructor block is byte-identical to both 477499 and actual 8dc9 main.",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "entry",
    "parent": {
      "name": "fixed_fejer_complete_same_field_phase_meshes.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_same_field_phase_meshes.py",
      "bytes": 48348,
      "sha256": "2acc9b4ee82623603d05f6a0951f01a0a3f92a4a640ca69b9f75814a45e5ab2d",
      "git_blob_sha": "96b9a32372704d5e58e53e72544d4abd40b4c536"
    },
    "output": {
      "name": "fixed_fejer_stage_observed_complete_same_field_phase_meshes.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_complete_same_field_phase_meshes.py",
      "bytes": 50400,
      "sha256": "3e9a9f8fc63af7fde35442f7c5cf9d4f11c1d851fe4c8659e814e630d952b070",
      "git_blob_sha": "d09a23ae04f618138aa05f3d7bb7846bbf927dc9"
    },
    "patches": [
      {
        "label": "mesh schema",
        "before": "SCHEMA = \"actual-fixed-fejer-complete-same-field-closed-phase-mesh-refinement-v1\"",
        "after": "SCHEMA = \"actual-fixed-fejer-stage-observed-complete-same-field-closed-phase-mesh-refinement-v1\"",
        "occurrences": 1
      },
      {
        "label": "complete 127-role registry",
        "before": "{\n    \"root_packets\": [\n        \"scripts/resume_20261126/fixed_fejer_immutable_normal_root_packets.py\",\n        \"1445b883cbcf3ed76571760923c2dc735ead7c862439d9478684a5a5299de468\"\n    ],\n    \"analytic_parent_stage_matrices\": [\n        \"scripts/resume_20261126/detached_normal_stage_matrix_reuse.py\",\n        \"375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59\"\n    ],\n    \"analytic_parent_adjacent_matrices\": [\n        \"scripts/resume_20261126/adjacent_normal_frame_matrices.py\",\n        \"955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3\"\n    ],\n    \"analytic_parent_driver\": [\n        \"scripts/resume_20261126/fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py\",\n        \"95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9\"\n    ],\n    \"analytic_parent_reader\": [\n        \"scripts/resume_20261126/read_reference_centred_independent_chart_material_envelope_so3_report.py\",\n        \"f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470\"\n    ],\n    \"analytic_J3\": [\n        \"scripts/resume_20261126/fixed_fejer_analytic_stage_jacobian.py\",\n        \"7645268ee3538a43a4a04b73a5aee4fc5483b56962affeb0ba7e7f879d5d4a72\"\n    ],\n    \"analytic_J3_binding\": [\n        \"scripts/resume_20261126/fixed_fejer_complete_source_binding.py\",\n        \"3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88\"\n    ],\n    \"analytic_parent_frame_C1\": [\n        \"scripts/resume_20261126/normal_frame_c1_reuse.py\",\n        \"ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9\"\n    ],\n    \"seed_reference\": [\n        \"scripts/resume_20261126/fixed_fejer_supported_meridian_reference.py\",\n        \"ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a\"\n    ],\n    \"seed_mean\": [\n        \"scripts/resume_20261126/supported_smooth_triangle_seed_mean_jets.py\",\n        \"f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917\"\n    ],\n    \"reference\": [\n        \"scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py\",\n        \"e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb\"\n    ],\n    \"warm_producer\": [\n        \"notes/2026-11-17-parallel-model-fullclosed-hold-warm.py\",\n        \"bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3\"\n    ],\n    \"observed\": [\n        \"scripts/resume_20261120/gauss_observed_closed_gram.py\",\n        \"26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d\"\n    ],\n    \"deep_scalar\": [\n        \"scripts/resume_20261126/deep_valley_tail_input.py\",\n        \"e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2\"\n    ],\n    \"scalar\": [\n        \"notes/2026-11-17-parallel-model-full-hold-oracle.py\",\n        \"a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670\"\n    ],\n    \"integer\": [\n        \"notes/2026-11-17-parallel-inward-integral-enclosure.py\",\n        \"babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0\"\n    ],\n    \"hold\": [\n        \"scripts/parallel_20261117_negative_hold_profile_ivp.py\",\n        \"ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1\"\n    ],\n    \"meridian\": [\n        \"scripts/resume_20261126/fixed_fejer_supported_so3_meridian_operator.py\",\n        \"552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3\"\n    ],\n    \"geometry\": [\n        \"scripts/resume_20261126/so3_fixed_fejer_complete_geometry.py\",\n        \"bab4147bdd2f0d43a372ec1b04225fc66a05db2ccdc2f92968d3f70e2590bf26\"\n    ],\n    \"qp\": [\n        \"scripts/resume_20261120/fullspace_feasible_active_cg_v3.py\",\n        \"fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4\"\n    ],\n    \"spectral\": [\n        \"scripts/resume_20261120/positive_spectral_gram_weights.py\",\n        \"e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91\"\n    ],\n    \"hessian\": [\n        \"scripts/resume_20261120/positive_spectral_gram_hessian.py\",\n        \"29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4\"\n    ],\n    \"centered\": [\n        \"scripts/resume_20261126/centered_spectral_statistics.py\",\n        \"5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01\"\n    ],\n    \"history\": [\n        \"scripts/resume_20261120/launch_refinement_from_full_report.py\",\n        \"4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60\"\n    ],\n    \"pure_geometry\": [\n        \"scripts/resume_20261120_curvature_qp.py\",\n        \"a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854\"\n    ],\n    \"geometry_selector\": [\n        \"scripts/resume_20261120/fullclosed_point_inequalities_v2.py\",\n        \"e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8\"\n    ],\n    \"endpoint\": [\n        \"scripts/resume_20261126/fixed_fejer_normal_lift_operator.py\",\n        \"1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778\"\n    ],\n    \"axisymmetric_seed_driver\": [\n        \"scripts/resume_20261126/fullclosed_axisymmetric_so3_qp.py\",\n        \"606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9\"\n    ],\n    \"frozen_moment_input\": [\n        \"scripts/resume_20261126/frozen_zero_moment_input.py\",\n        \"4dc3e1a8ba8f128e1d05176f4d0f4b18c62d278fed603cc46f7ed686f6e4e611\"\n    ],\n    \"moment_trace_source\": [\n        \"scripts/resume_20261126/trace_zero_initial_endpoint_failure.py\",\n        \"73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54\"\n    ],\n    \"moment_initial_binding\": [\n        \"scripts/resume_20261126/diagnose_zero_initial_chord.py\",\n        \"65787b3e51f80505f5619c35fb05f8ad064e88de111578ff53e8bdad442092c0\"\n    ],\n    \"moment_original_endpoint\": [\n        \"scripts/resume_20261126/so3_zero_closure_endpoint_operator.py\",\n        \"5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46\"\n    ],\n    \"moment_original_driver\": [\n        \"scripts/resume_20261126/fullclosed_zero_closure_so3_qp.py\",\n        \"b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b\"\n    ],\n    \"new_moment_input\": [\n        \"scripts/resume_20261126/fixed_fejer_literal_zero_moment_input.py\",\n        \"ca4fef4066bfb6d6fedbdf9b65349f7f0ba8480376858c84faa8ee3d4d4b97b3\"\n    ],\n    \"reference_calibration\": [\n        \"scripts/resume_20261126/fixed_fejer_reference_calibration.py\",\n        \"fe36240c08ad32c4d4d665a387c70aaf02c0392419a51eef01e072081945e95c\"\n    ],\n    \"frame_C1\": [\n        \"scripts/resume_20261126/fixed_fejer_normal_frame_c1.py\",\n        \"1830c1d8e69e0e12d4b9d8af9f194d234ef3437cba546200738a1592a77aa0ca\"\n    ],\n    \"envelope_memory\": [\n        \"scripts/resume_20261126/complete_material_envelope_memory.py\",\n        \"c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152\"\n    ],\n    \"envelope_rows\": [\n        \"scripts/resume_20261126/complete_material_envelope_rows.py\",\n        \"729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7\"\n    ],\n    \"stage_matrices\": [\n        \"scripts/resume_20261126/fixed_fejer_detached_stage_matrices.py\",\n        \"7aabf3ef5857dbdbbf9832b8bb4ca378faa7e06514a21b48f83649d6df7cb0d7\"\n    ],\n    \"envelope_transfer\": [\n        \"scripts/resume_20261126/transfer_fixed_fejer_material_envelope_memory.py\",\n        \"af35c30e4774987d8f71bc6d05c1942db66a9f7889127c19948b119dee9a1566\"\n    ],\n    \"envelope_parent_reader\": [\n        \"scripts/resume_20261126/read_reference_centred_c1_material_envelope_so3_report.py\",\n        \"104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7\"\n    ],\n    \"envelope_parent_driver\": [\n        \"scripts/resume_20261126/fullclosed_reference_centred_c1_material_envelope_so3_qp.py\",\n        \"cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5\"\n    ],\n    \"envelope_parent_endpoint\": [\n        \"scripts/resume_20261126/so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py\",\n        \"a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd\"\n    ],\n    \"envelope_parent_calibration\": [\n        \"scripts/resume_20261126/reference_centred_c1_smooth_triangle_calibration.py\",\n        \"3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991\"\n    ],\n    \"envelope_parent_geometry\": [\n        \"scripts/resume_20261126/so3_reference_centred_c1_material_envelope_geometry.py\",\n        \"bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f\"\n    ],\n    \"adjacent_matrices\": [\n        \"scripts/resume_20261126/fixed_fejer_adjacent_normal_matrices.py\",\n        \"257e5e44d38dffb82925a410c42e51f084cf7821a398b9928e543088a3f234c0\"\n    ],\n    \"independent_envelope_memory\": [\n        \"scripts/resume_20261126/complete_fixed_fejer_material_envelope_memory.py\",\n        \"9f268e066274eff19ee2635124a8addf9c92eabf6d7177249f4ac4782c88a39a\"\n    ],\n    \"independent_input_projection_producer\": [\n        \"scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py\",\n        \"e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb\"\n    ],\n    \"analytic_frame\": [\n        \"scripts/resume_20261126/fixed_fejer_analytic_normal_frame.py\",\n        \"75db2f20039b66a2784a922bf062e792328c0153fb0458c16acef92e0ab7e38c\"\n    ],\n    \"frame_parent_driver\": [\n        \"scripts/resume_20261126/fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py\",\n        \"0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51\"\n    ],\n    \"frame_parent_reader\": [\n        \"scripts/resume_20261126/read_reference_centred_analytic_j3_material_envelope_so3_report.py\",\n        \"c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e\"\n    ],\n    \"frame_parent_endpoint\": [\n        \"scripts/resume_20261126/so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py\",\n        \"04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e\"\n    ],\n    \"frame_parent_calibration\": [\n        \"scripts/resume_20261126/reference_centred_analytic_j3_smooth_triangle_calibration.py\",\n        \"4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d\"\n    ],\n    \"frame_parent_J3\": [\n        \"scripts/resume_20261126/analytic_normal_stage_jacobian.py\",\n        \"64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d\"\n    ],\n    \"frame_parent_C1\": [\n        \"scripts/resume_20261126/analytic_j3_normal_frame_c1_reuse.py\",\n        \"8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8\"\n    ],\n    \"frame_parent_stage_matrices\": [\n        \"scripts/resume_20261126/analytic_j3_detached_normal_stage_matrix_reuse.py\",\n        \"5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1\"\n    ],\n    \"frame_parent_adjacent_matrices\": [\n        \"scripts/resume_20261126/analytic_j3_adjacent_normal_frame_matrices.py\",\n        \"8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787\"\n    ],\n    \"actual_public_input_binding\": [\n        \"scripts/resume_20261126/fixed_fejer_reference_input_binding.py\",\n        \"3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f\"\n    ],\n    \"closure_values\": [\n        \"scripts/resume_20261126/fixed_fejer_immutable_closure_values.py\",\n        \"01ca74a9f00ac17ef4452173b758d785c0e06869efa98980426f822d4beeb595\"\n    ],\n    \"closure_parent_analytic_J3\": [\n        \"scripts/resume_20261126/analytic_frame_local_stage_jacobian.py\",\n        \"894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866\"\n    ],\n    \"closure_parent_analytic_frame\": [\n        \"scripts/resume_20261126/analytic_normal_frame_jets.py\",\n        \"4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8\"\n    ],\n    \"closure_parent_frame_C1\": [\n        \"scripts/resume_20261126/analytic_frame_c1_reuse.py\",\n        \"f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb\"\n    ],\n    \"closure_parent_stage_matrices\": [\n        \"scripts/resume_20261126/analytic_frame_detached_normal_stage_matrix_reuse.py\",\n        \"fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255\"\n    ],\n    \"closure_parent_adjacent_matrices\": [\n        \"scripts/resume_20261126/analytic_frame_adjacent_normal_matrices.py\",\n        \"3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695\"\n    ],\n    \"closure_parent_reference_calibration\": [\n        \"scripts/resume_20261126/reference_centred_analytic_frame_smooth_triangle_calibration.py\",\n        \"fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0\"\n    ],\n    \"closure_parent_endpoint\": [\n        \"scripts/resume_20261126/so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py\",\n        \"3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc\"\n    ],\n    \"closure_parent_root_packets\": [\n        \"scripts/resume_20261126/immutable_analytic_frame_normal_root_packets.py\",\n        \"094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0\"\n    ],\n    \"closure_parent_analytic_J3_binding\": [\n        \"scripts/resume_20261126/run09_public_reference_analytic_frame_binding.py\",\n        \"15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592\"\n    ],\n    \"closure_parent_geometry\": [\n        \"scripts/resume_20261126/so3_run09_public_reference_analytic_frame_geometry_v2.py\",\n        \"e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13\"\n    ],\n    \"closure_parent_envelope_transfer\": [\n        \"scripts/resume_20261126/transfer_run09_public_reference_analytic_frame_memory.py\",\n        \"6deeeaa1dcbbb0fbfd968d0b31443798909536a55a7ea498f661e08496a27707\"\n    ],\n    \"closure_parent_driver\": [\n        \"scripts/resume_20261126/fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py\",\n        \"ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5\"\n    ],\n    \"closure_parent_reader\": [\n        \"scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py\",\n        \"aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32\"\n    ],\n    \"closure_parent_independent_envelope_memory\": [\n        \"scripts/resume_20261126/complete_material_envelope_memory_public_reference.py\",\n        \"2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb\"\n    ],\n    \"closure_parent_independent_input_projection_producer\": [\n        \"scripts/resume_20261126/freeze_run09_public_reference_and_restore_run05_carrier.py\",\n        \"9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18\"\n    ],\n    \"closure_parent_actual_public_input_binding\": [\n        \"scripts/resume_20261126/actual_public_reference_input_binding.py\",\n        \"306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a\"\n    ],\n    \"immutable_point_parent_closure_values\": [\n        \"scripts/resume_20261126/same_chain_detached_closure_values.py\",\n        \"e1af4fc8cfecbd30ab5cf9f7ded31d6a7a8d11385a8558cc76cbb8a8b1851e9e\"\n    ],\n    \"immutable_point_parent_analytic_J3\": [\n        \"scripts/resume_20261126/analytic_local_stage_jacobian_closure_values.py\",\n        \"9646c1cb1e239f4625dfaa0f13e0d0776dfd9684401789a089326e177c02a5aa\"\n    ],\n    \"immutable_point_parent_analytic_frame\": [\n        \"scripts/resume_20261126/analytic_normal_frame_jets_closure_values.py\",\n        \"8239fc8f3588afd4f93ba10368c599a85652d3b350a088b1397731c196258598\"\n    ],\n    \"immutable_point_parent_frame_C1\": [\n        \"scripts/resume_20261126/normal_frame_c1_closure_values.py\",\n        \"1f80ce726f9cf9424740331eb54a5cafa86a058ca2b048ee5fb6add5fc371caa\"\n    ],\n    \"immutable_point_parent_stage_matrices\": [\n        \"scripts/resume_20261126/detached_stage_matrices_closure_values.py\",\n        \"bf80cc8bbcf442d07d0e9225e1fbf703be4c40b951f10fb20e861e1ec7497c45\"\n    ],\n    \"immutable_point_parent_adjacent_matrices\": [\n        \"scripts/resume_20261126/adjacent_normal_matrices_closure_values.py\",\n        \"6efb1b4de61635bb4121b2cc05daf4b817ecfb772f302568e2a570b7fa16b650\"\n    ],\n    \"immutable_point_parent_reference_calibration\": [\n        \"scripts/resume_20261126/reference_centred_closure_values_calibration.py\",\n        \"b59776d52653f036590b619124579a20400d3bb7a4de8117d3221ca32bec144f\"\n    ],\n    \"immutable_point_parent_endpoint\": [\n        \"scripts/resume_20261126/so3_reference_centred_closure_values_normal_lift_operator.py\",\n        \"6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4\"\n    ],\n    \"immutable_point_parent_root_packets\": [\n        \"scripts/resume_20261126/immutable_closure_values_normal_root_packets.py\",\n        \"31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805\"\n    ],\n    \"immutable_point_parent_binding\": [\n        \"scripts/resume_20261126/run10_detached_closure_value_binding.py\",\n        \"dc3b40645eb47f924392a703eb65e3fda982f43804b1861f89da1c038e9140a1\"\n    ],\n    \"immutable_point_parent_geometry\": [\n        \"scripts/resume_20261126/so3_run10_detached_closure_geometry.py\",\n        \"6c676d4302f4271310ffca899ca8820fe43f2d792ee9a634747f25eecf9f6528\"\n    ],\n    \"immutable_point_parent_envelope_transfer\": [\n        \"scripts/resume_20261126/transfer_run10_detached_closure_memory.py\",\n        \"eca323b12ff941736798f7e40021f78b92e1b23cee8a7edcdcc5e3f6db7508fe\"\n    ],\n    \"immutable_point_parent_driver\": [\n        \"scripts/resume_20261126/fullclosed_run10_detached_closure_so3_qp.py\",\n        \"c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1\"\n    ],\n    \"immutable_point_parent_reader\": [\n        \"scripts/resume_20261126/read_run10_detached_closure_so3_report.py\",\n        \"2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e\"\n    ],\n    \"immutable_point_parent_launcher\": [\n        \"scripts/resume_20261126/launch_run10_detached_closure_actions.py\",\n        \"22069c4bb56a4ca4820b3f608cf720a36b036534e6b1e90b5f467f8eed21e604\"\n    ],\n    \"fixed_fejer_previous_closure_values\": [\n        \"scripts/resume_20261126/immutable_point_detached_closure_values.py\",\n        \"2543ee5db3ff15108fbdb4e340dad84301b94eecb773f757da4126ab86778cfb\"\n    ],\n    \"fixed_fejer_previous_analytic_J3\": [\n        \"scripts/resume_20261126/analytic_local_stage_jacobian_immutable_point.py\",\n        \"21a929c14abfe5e66ca56c232d31b77d8f8e3a5e969d796c4601d1a1e1374024\"\n    ],\n    \"fixed_fejer_previous_analytic_frame\": [\n        \"scripts/resume_20261126/analytic_normal_frame_jets_immutable_point.py\",\n        \"4e9b027b365752878069fa29671f8f549fa4cd9be478487b12ceeb64a908f8fa\"\n    ],\n    \"fixed_fejer_previous_frame_C1\": [\n        \"scripts/resume_20261126/normal_frame_c1_immutable_point.py\",\n        \"53b5bc456cb3f62c6a25d329de54920253d9193168ef3fb761198ff61fa0822d\"\n    ],\n    \"fixed_fejer_previous_stage_matrices\": [\n        \"scripts/resume_20261126/detached_stage_matrices_immutable_point.py\",\n        \"a41872f7563683b28d34cb9da35d7fc3bd0879fb5a8d1d183230a518f6b8f052\"\n    ],\n    \"fixed_fejer_previous_adjacent_matrices\": [\n        \"scripts/resume_20261126/adjacent_normal_matrices_immutable_point.py\",\n        \"ab944e9c9af4b84a65d201a6cc997669a8f274077fc7e1f69ee35b268380bb59\"\n    ],\n    \"fixed_fejer_previous_reference_calibration\": [\n        \"scripts/resume_20261126/reference_centred_immutable_point_calibration.py\",\n        \"794275121ee8d2f79972c5302012a10ba1fd8aa58fa5f67f05399825244fd238\"\n    ],\n    \"fixed_fejer_previous_endpoint\": [\n        \"scripts/resume_20261126/so3_reference_centred_immutable_point_normal_lift_operator.py\",\n        \"9bd394592f95668956c6718387b02d22d47c445b3f981f9101ae0e2c482594d6\"\n    ],\n    \"fixed_fejer_previous_root_packets\": [\n        \"scripts/resume_20261126/immutable_point_normal_root_packets.py\",\n        \"b4c41b2dc8754607441c30cdb3a34199d7e40f8b52fc5e4a8f5d653ea524eac8\"\n    ],\n    \"fixed_fejer_previous_reference\": [\n        \"scripts/resume_20261126/so3_axisymmetric_reference.py\",\n        \"4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3\"\n    ],\n    \"fixed_fejer_previous_seed_reference\": [\n        \"scripts/resume_20261126/supported_smooth_triangle_meridian_reference.py\",\n        \"0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b\"\n    ],\n    \"fixed_fejer_previous_meridian\": [\n        \"scripts/resume_20261126/so3_supported_smooth_triangle_meridian_operator.py\",\n        \"6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865\"\n    ],\n    \"fixed_fejer_previous_new_moment_input\": [\n        \"scripts/resume_20261126/supported_smooth_triangle_literal_zero_moment_input.py\",\n        \"307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7\"\n    ],\n    \"fixed_fejer_previous_analytic_J3_binding\": [\n        \"scripts/resume_20261126/run10_immutable_point_source_binding.py\",\n        \"85f3007a6927968eb253eab168e9379f9a1f732caf5aa43b9f24776f39606d97\"\n    ],\n    \"fixed_fejer_previous_geometry\": [\n        \"scripts/resume_20261126/so3_run10_immutable_point_geometry.py\",\n        \"dbbd4601f4bbc0798759f3c63cd3caae3cfc19f1a62ec9dbd02cc6fbceb896ce\"\n    ],\n    \"fixed_fejer_previous_envelope_transfer\": [\n        \"scripts/resume_20261126/transfer_run10_immutable_point_memory.py\",\n        \"0007abf0b2814b09a3ecc30f621cbd8814a3d94528c753762aa7be5175d08486\"\n    ],\n    \"fixed_fejer_previous_independent_envelope_memory\": [\n        \"scripts/resume_20261126/complete_material_envelope_memory_public_run10.py\",\n        \"f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba\"\n    ],\n    \"fixed_fejer_previous_independent_input_projection_producer\": [\n        \"scripts/resume_20261126/freeze_run10_public_reference_and_restore_run05_carrier.py\",\n        \"fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a\"\n    ],\n    \"fixed_fejer_previous_actual_public_input_binding\": [\n        \"scripts/resume_20261126/actual_public_run10_reference_input_binding.py\",\n        \"9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209\"\n    ],\n    \"fixed_input_producer\": [\n        \"scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py\",\n        \"89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60\"\n    ],\n    \"mesh_input\": [\n        \"scripts/resume_20261126/fixed_fejer_same_field_mesh_input.py\",\n        \"ad809cb428b7cdd6f3fe082a0057739ff191aefe4abb113e4595fe5e618f0036\"\n    ],\n    \"mesh_arithmetic\": [\n        \"scripts/resume_20261126/fixed_fejer_complete_phase_mesh_arithmetic.py\",\n        \"80116a4bcfa2752274cece1148420cdce5c489faba3a8a7c0e92c0f6a8d058e4\"\n    ],\n    \"original_fixed_fejer_driver\": [\n        \"scripts/resume_20261126/fullclosed_fixed_fejer_immutable_point_so3_qp.py\",\n        \"477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd\"\n    ],\n    \"original_fixed_fejer_reader\": [\n        \"scripts/resume_20261126/read_fixed_fejer_immutable_point_so3_report.py\",\n        \"274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b\"\n    ],\n    \"original_fixed_fejer_launcher\": [\n        \"scripts/resume_20261126/launch_fixed_fejer_immutable_point_actions.py\",\n        \"0c1ff0aa2de30fcd490efb4bddd1972613c0f0afb1257d1af0170ac7e60bb5bf\"\n    ],\n    \"complete_accurate_input_scope\": [\n        \"scripts/resume_20261126/fixed_fejer_normal_packet_accurate_field_input.py\",\n        \"1e5101d7bd08a8b3787b6eaa699c915a9e8bd173d365233c7be90f1aee1b3f3f\"\n    ],\n    \"optional_closed_phase_source\": [\n        \"scripts/resume_20261126/fixed_fejer_complete_closed_phase_grip_evidence.py\",\n        \"d606055d1b247d8354ac320bc28a0f40f4b00cbf1ff530a9b6bb2e80dec80bb9\"\n    ]\n}",
        "after": "{\n    \"root_packets\": [\n        \"scripts/resume_20261126/fixed_fejer_stage_point_root_packets.py\",\n        \"140f639656c2a30c59f0ba4c8153e3467d5abddf8189a84fcc38fb6638ee8aaf\"\n    ],\n    \"analytic_parent_stage_matrices\": [\n        \"scripts/resume_20261126/detached_normal_stage_matrix_reuse.py\",\n        \"375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59\"\n    ],\n    \"analytic_parent_adjacent_matrices\": [\n        \"scripts/resume_20261126/adjacent_normal_frame_matrices.py\",\n        \"955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3\"\n    ],\n    \"analytic_parent_driver\": [\n        \"scripts/resume_20261126/fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py\",\n        \"95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9\"\n    ],\n    \"analytic_parent_reader\": [\n        \"scripts/resume_20261126/read_reference_centred_independent_chart_material_envelope_so3_report.py\",\n        \"f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470\"\n    ],\n    \"analytic_J3\": [\n        \"scripts/resume_20261126/fixed_fejer_analytic_stage_jacobian.py\",\n        \"7645268ee3538a43a4a04b73a5aee4fc5483b56962affeb0ba7e7f879d5d4a72\"\n    ],\n    \"analytic_J3_binding\": [\n        \"scripts/resume_20261126/fixed_fejer_stage_point_source_binding.py\",\n        \"9171871fcaaa1d2e65de1c40071cf8bb1acac0d7b0cc1d1da5b9cb36f690076f\"\n    ],\n    \"analytic_parent_frame_C1\": [\n        \"scripts/resume_20261126/normal_frame_c1_reuse.py\",\n        \"ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9\"\n    ],\n    \"seed_reference\": [\n        \"scripts/resume_20261126/fixed_fejer_supported_meridian_reference.py\",\n        \"ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a\"\n    ],\n    \"seed_mean\": [\n        \"scripts/resume_20261126/supported_smooth_triangle_seed_mean_jets.py\",\n        \"f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917\"\n    ],\n    \"reference\": [\n        \"scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py\",\n        \"e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb\"\n    ],\n    \"warm_producer\": [\n        \"notes/2026-11-17-parallel-model-fullclosed-hold-warm.py\",\n        \"bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3\"\n    ],\n    \"observed\": [\n        \"scripts/resume_20261120/gauss_observed_closed_gram.py\",\n        \"26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d\"\n    ],\n    \"deep_scalar\": [\n        \"scripts/resume_20261126/deep_valley_tail_input.py\",\n        \"e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2\"\n    ],\n    \"scalar\": [\n        \"notes/2026-11-17-parallel-model-full-hold-oracle.py\",\n        \"a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670\"\n    ],\n    \"integer\": [\n        \"notes/2026-11-17-parallel-inward-integral-enclosure.py\",\n        \"babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0\"\n    ],\n    \"hold\": [\n        \"scripts/parallel_20261117_negative_hold_profile_ivp.py\",\n        \"ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1\"\n    ],\n    \"meridian\": [\n        \"scripts/resume_20261126/fixed_fejer_supported_so3_meridian_operator.py\",\n        \"552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3\"\n    ],\n    \"geometry\": [\n        \"scripts/resume_20261126/so3_fixed_fejer_stage_point_geometry.py\",\n        \"2ecd2b23eccf6bee564c07daa386fbd232d7ff9f5634b484317d62ab10e56471\"\n    ],\n    \"qp\": [\n        \"scripts/resume_20261120/fullspace_feasible_active_cg_v3.py\",\n        \"fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4\"\n    ],\n    \"spectral\": [\n        \"scripts/resume_20261120/positive_spectral_gram_weights.py\",\n        \"e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91\"\n    ],\n    \"hessian\": [\n        \"scripts/resume_20261120/positive_spectral_gram_hessian.py\",\n        \"29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4\"\n    ],\n    \"centered\": [\n        \"scripts/resume_20261126/centered_spectral_statistics.py\",\n        \"5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01\"\n    ],\n    \"history\": [\n        \"scripts/resume_20261120/launch_refinement_from_full_report.py\",\n        \"4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60\"\n    ],\n    \"pure_geometry\": [\n        \"scripts/resume_20261120_curvature_qp.py\",\n        \"a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854\"\n    ],\n    \"geometry_selector\": [\n        \"scripts/resume_20261120/fullclosed_point_inequalities_v2.py\",\n        \"e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8\"\n    ],\n    \"endpoint\": [\n        \"scripts/resume_20261126/fixed_fejer_stage_point_normal_lift.py\",\n        \"42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10\"\n    ],\n    \"axisymmetric_seed_driver\": [\n        \"scripts/resume_20261126/fullclosed_axisymmetric_so3_qp.py\",\n        \"606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9\"\n    ],\n    \"frozen_moment_input\": [\n        \"scripts/resume_20261126/frozen_zero_moment_input.py\",\n        \"4dc3e1a8ba8f128e1d05176f4d0f4b18c62d278fed603cc46f7ed686f6e4e611\"\n    ],\n    \"moment_trace_source\": [\n        \"scripts/resume_20261126/trace_zero_initial_endpoint_failure.py\",\n        \"73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54\"\n    ],\n    \"moment_initial_binding\": [\n        \"scripts/resume_20261126/diagnose_zero_initial_chord.py\",\n        \"65787b3e51f80505f5619c35fb05f8ad064e88de111578ff53e8bdad442092c0\"\n    ],\n    \"moment_original_endpoint\": [\n        \"scripts/resume_20261126/so3_zero_closure_endpoint_operator.py\",\n        \"5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46\"\n    ],\n    \"moment_original_driver\": [\n        \"scripts/resume_20261126/fullclosed_zero_closure_so3_qp.py\",\n        \"b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b\"\n    ],\n    \"new_moment_input\": [\n        \"scripts/resume_20261126/fixed_fejer_literal_zero_moment_input.py\",\n        \"ca4fef4066bfb6d6fedbdf9b65349f7f0ba8480376858c84faa8ee3d4d4b97b3\"\n    ],\n    \"reference_calibration\": [\n        \"scripts/resume_20261126/fixed_fejer_reference_calibration.py\",\n        \"fe36240c08ad32c4d4d665a387c70aaf02c0392419a51eef01e072081945e95c\"\n    ],\n    \"frame_C1\": [\n        \"scripts/resume_20261126/fixed_fejer_normal_frame_c1.py\",\n        \"1830c1d8e69e0e12d4b9d8af9f194d234ef3437cba546200738a1592a77aa0ca\"\n    ],\n    \"envelope_memory\": [\n        \"scripts/resume_20261126/complete_material_envelope_memory.py\",\n        \"c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152\"\n    ],\n    \"envelope_rows\": [\n        \"scripts/resume_20261126/complete_material_envelope_rows.py\",\n        \"729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7\"\n    ],\n    \"stage_matrices\": [\n        \"scripts/resume_20261126/fixed_fejer_immutable_point_stage_matrices.py\",\n        \"e4d42910f9550a20d0afc16aab8f54b5ea1ceb18ace375128f3a79bfef0e76ce\"\n    ],\n    \"envelope_transfer\": [\n        \"scripts/resume_20261126/transfer_fixed_fejer_stage_point_memory.py\",\n        \"afa2d6397c331b5bf55dd461bbf52a35839ff610d3db0f12a043e8eceef3b6ed\"\n    ],\n    \"envelope_parent_reader\": [\n        \"scripts/resume_20261126/read_reference_centred_c1_material_envelope_so3_report.py\",\n        \"104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7\"\n    ],\n    \"envelope_parent_driver\": [\n        \"scripts/resume_20261126/fullclosed_reference_centred_c1_material_envelope_so3_qp.py\",\n        \"cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5\"\n    ],\n    \"envelope_parent_endpoint\": [\n        \"scripts/resume_20261126/so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py\",\n        \"a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd\"\n    ],\n    \"envelope_parent_calibration\": [\n        \"scripts/resume_20261126/reference_centred_c1_smooth_triangle_calibration.py\",\n        \"3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991\"\n    ],\n    \"envelope_parent_geometry\": [\n        \"scripts/resume_20261126/so3_reference_centred_c1_material_envelope_geometry.py\",\n        \"bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f\"\n    ],\n    \"adjacent_matrices\": [\n        \"scripts/resume_20261126/fixed_fejer_stage_point_adjacent_matrices.py\",\n        \"d04cf80d40a16410a2338f3b4b0c3bbdd0084cfc2ad5270bee21d33ded9449b5\"\n    ],\n    \"independent_envelope_memory\": [\n        \"scripts/resume_20261126/complete_fixed_fejer_material_envelope_memory.py\",\n        \"9f268e066274eff19ee2635124a8addf9c92eabf6d7177249f4ac4782c88a39a\"\n    ],\n    \"independent_input_projection_producer\": [\n        \"scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py\",\n        \"e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb\"\n    ],\n    \"analytic_frame\": [\n        \"scripts/resume_20261126/fixed_fejer_analytic_normal_frame.py\",\n        \"75db2f20039b66a2784a922bf062e792328c0153fb0458c16acef92e0ab7e38c\"\n    ],\n    \"frame_parent_driver\": [\n        \"scripts/resume_20261126/fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py\",\n        \"0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51\"\n    ],\n    \"frame_parent_reader\": [\n        \"scripts/resume_20261126/read_reference_centred_analytic_j3_material_envelope_so3_report.py\",\n        \"c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e\"\n    ],\n    \"frame_parent_endpoint\": [\n        \"scripts/resume_20261126/so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py\",\n        \"04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e\"\n    ],\n    \"frame_parent_calibration\": [\n        \"scripts/resume_20261126/reference_centred_analytic_j3_smooth_triangle_calibration.py\",\n        \"4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d\"\n    ],\n    \"frame_parent_J3\": [\n        \"scripts/resume_20261126/analytic_normal_stage_jacobian.py\",\n        \"64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d\"\n    ],\n    \"frame_parent_C1\": [\n        \"scripts/resume_20261126/analytic_j3_normal_frame_c1_reuse.py\",\n        \"8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8\"\n    ],\n    \"frame_parent_stage_matrices\": [\n        \"scripts/resume_20261126/analytic_j3_detached_normal_stage_matrix_reuse.py\",\n        \"5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1\"\n    ],\n    \"frame_parent_adjacent_matrices\": [\n        \"scripts/resume_20261126/analytic_j3_adjacent_normal_frame_matrices.py\",\n        \"8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787\"\n    ],\n    \"actual_public_input_binding\": [\n        \"scripts/resume_20261126/fixed_fejer_reference_input_binding.py\",\n        \"3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f\"\n    ],\n    \"closure_values\": [\n        \"scripts/resume_20261126/fixed_fejer_immutable_closure_values.py\",\n        \"01ca74a9f00ac17ef4452173b758d785c0e06869efa98980426f822d4beeb595\"\n    ],\n    \"closure_parent_analytic_J3\": [\n        \"scripts/resume_20261126/analytic_frame_local_stage_jacobian.py\",\n        \"894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866\"\n    ],\n    \"closure_parent_analytic_frame\": [\n        \"scripts/resume_20261126/analytic_normal_frame_jets.py\",\n        \"4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8\"\n    ],\n    \"closure_parent_frame_C1\": [\n        \"scripts/resume_20261126/analytic_frame_c1_reuse.py\",\n        \"f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb\"\n    ],\n    \"closure_parent_stage_matrices\": [\n        \"scripts/resume_20261126/analytic_frame_detached_normal_stage_matrix_reuse.py\",\n        \"fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255\"\n    ],\n    \"closure_parent_adjacent_matrices\": [\n        \"scripts/resume_20261126/analytic_frame_adjacent_normal_matrices.py\",\n        \"3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695\"\n    ],\n    \"closure_parent_reference_calibration\": [\n        \"scripts/resume_20261126/reference_centred_analytic_frame_smooth_triangle_calibration.py\",\n        \"fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0\"\n    ],\n    \"closure_parent_endpoint\": [\n        \"scripts/resume_20261126/so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py\",\n        \"3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc\"\n    ],\n    \"closure_parent_root_packets\": [\n        \"scripts/resume_20261126/immutable_analytic_frame_normal_root_packets.py\",\n        \"094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0\"\n    ],\n    \"closure_parent_analytic_J3_binding\": [\n        \"scripts/resume_20261126/run09_public_reference_analytic_frame_binding.py\",\n        \"15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592\"\n    ],\n    \"closure_parent_geometry\": [\n        \"scripts/resume_20261126/so3_run09_public_reference_analytic_frame_geometry_v2.py\",\n        \"e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13\"\n    ],\n    \"closure_parent_envelope_transfer\": [\n        \"scripts/resume_20261126/transfer_run09_public_reference_analytic_frame_memory.py\",\n        \"6deeeaa1dcbbb0fbfd968d0b31443798909536a55a7ea498f661e08496a27707\"\n    ],\n    \"closure_parent_driver\": [\n        \"scripts/resume_20261126/fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py\",\n        \"ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5\"\n    ],\n    \"closure_parent_reader\": [\n        \"scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py\",\n        \"aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32\"\n    ],\n    \"closure_parent_independent_envelope_memory\": [\n        \"scripts/resume_20261126/complete_material_envelope_memory_public_reference.py\",\n        \"2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb\"\n    ],\n    \"closure_parent_independent_input_projection_producer\": [\n        \"scripts/resume_20261126/freeze_run09_public_reference_and_restore_run05_carrier.py\",\n        \"9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18\"\n    ],\n    \"closure_parent_actual_public_input_binding\": [\n        \"scripts/resume_20261126/actual_public_reference_input_binding.py\",\n        \"306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a\"\n    ],\n    \"immutable_point_parent_closure_values\": [\n        \"scripts/resume_20261126/same_chain_detached_closure_values.py\",\n        \"e1af4fc8cfecbd30ab5cf9f7ded31d6a7a8d11385a8558cc76cbb8a8b1851e9e\"\n    ],\n    \"immutable_point_parent_analytic_J3\": [\n        \"scripts/resume_20261126/analytic_local_stage_jacobian_closure_values.py\",\n        \"9646c1cb1e239f4625dfaa0f13e0d0776dfd9684401789a089326e177c02a5aa\"\n    ],\n    \"immutable_point_parent_analytic_frame\": [\n        \"scripts/resume_20261126/analytic_normal_frame_jets_closure_values.py\",\n        \"8239fc8f3588afd4f93ba10368c599a85652d3b350a088b1397731c196258598\"\n    ],\n    \"immutable_point_parent_frame_C1\": [\n        \"scripts/resume_20261126/normal_frame_c1_closure_values.py\",\n        \"1f80ce726f9cf9424740331eb54a5cafa86a058ca2b048ee5fb6add5fc371caa\"\n    ],\n    \"immutable_point_parent_stage_matrices\": [\n        \"scripts/resume_20261126/detached_stage_matrices_closure_values.py\",\n        \"bf80cc8bbcf442d07d0e9225e1fbf703be4c40b951f10fb20e861e1ec7497c45\"\n    ],\n    \"immutable_point_parent_adjacent_matrices\": [\n        \"scripts/resume_20261126/adjacent_normal_matrices_closure_values.py\",\n        \"6efb1b4de61635bb4121b2cc05daf4b817ecfb772f302568e2a570b7fa16b650\"\n    ],\n    \"immutable_point_parent_reference_calibration\": [\n        \"scripts/resume_20261126/reference_centred_closure_values_calibration.py\",\n        \"b59776d52653f036590b619124579a20400d3bb7a4de8117d3221ca32bec144f\"\n    ],\n    \"immutable_point_parent_endpoint\": [\n        \"scripts/resume_20261126/so3_reference_centred_closure_values_normal_lift_operator.py\",\n        \"6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4\"\n    ],\n    \"immutable_point_parent_root_packets\": [\n        \"scripts/resume_20261126/immutable_closure_values_normal_root_packets.py\",\n        \"31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805\"\n    ],\n    \"immutable_point_parent_binding\": [\n        \"scripts/resume_20261126/run10_detached_closure_value_binding.py\",\n        \"dc3b40645eb47f924392a703eb65e3fda982f43804b1861f89da1c038e9140a1\"\n    ],\n    \"immutable_point_parent_geometry\": [\n        \"scripts/resume_20261126/so3_run10_detached_closure_geometry.py\",\n        \"6c676d4302f4271310ffca899ca8820fe43f2d792ee9a634747f25eecf9f6528\"\n    ],\n    \"immutable_point_parent_envelope_transfer\": [\n        \"scripts/resume_20261126/transfer_run10_detached_closure_memory.py\",\n        \"eca323b12ff941736798f7e40021f78b92e1b23cee8a7edcdcc5e3f6db7508fe\"\n    ],\n    \"immutable_point_parent_driver\": [\n        \"scripts/resume_20261126/fullclosed_run10_detached_closure_so3_qp.py\",\n        \"c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1\"\n    ],\n    \"immutable_point_parent_reader\": [\n        \"scripts/resume_20261126/read_run10_detached_closure_so3_report.py\",\n        \"2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e\"\n    ],\n    \"immutable_point_parent_launcher\": [\n        \"scripts/resume_20261126/launch_run10_detached_closure_actions.py\",\n        \"22069c4bb56a4ca4820b3f608cf720a36b036534e6b1e90b5f467f8eed21e604\"\n    ],\n    \"fixed_fejer_previous_closure_values\": [\n        \"scripts/resume_20261126/immutable_point_detached_closure_values.py\",\n        \"2543ee5db3ff15108fbdb4e340dad84301b94eecb773f757da4126ab86778cfb\"\n    ],\n    \"fixed_fejer_previous_analytic_J3\": [\n        \"scripts/resume_20261126/analytic_local_stage_jacobian_immutable_point.py\",\n        \"21a929c14abfe5e66ca56c232d31b77d8f8e3a5e969d796c4601d1a1e1374024\"\n    ],\n    \"fixed_fejer_previous_analytic_frame\": [\n        \"scripts/resume_20261126/analytic_normal_frame_jets_immutable_point.py\",\n        \"4e9b027b365752878069fa29671f8f549fa4cd9be478487b12ceeb64a908f8fa\"\n    ],\n    \"fixed_fejer_previous_frame_C1\": [\n        \"scripts/resume_20261126/normal_frame_c1_immutable_point.py\",\n        \"53b5bc456cb3f62c6a25d329de54920253d9193168ef3fb761198ff61fa0822d\"\n    ],\n    \"fixed_fejer_previous_stage_matrices\": [\n        \"scripts/resume_20261126/detached_stage_matrices_immutable_point.py\",\n        \"a41872f7563683b28d34cb9da35d7fc3bd0879fb5a8d1d183230a518f6b8f052\"\n    ],\n    \"fixed_fejer_previous_adjacent_matrices\": [\n        \"scripts/resume_20261126/adjacent_normal_matrices_immutable_point.py\",\n        \"ab944e9c9af4b84a65d201a6cc997669a8f274077fc7e1f69ee35b268380bb59\"\n    ],\n    \"fixed_fejer_previous_reference_calibration\": [\n        \"scripts/resume_20261126/reference_centred_immutable_point_calibration.py\",\n        \"794275121ee8d2f79972c5302012a10ba1fd8aa58fa5f67f05399825244fd238\"\n    ],\n    \"fixed_fejer_previous_endpoint\": [\n        \"scripts/resume_20261126/so3_reference_centred_immutable_point_normal_lift_operator.py\",\n        \"9bd394592f95668956c6718387b02d22d47c445b3f981f9101ae0e2c482594d6\"\n    ],\n    \"fixed_fejer_previous_root_packets\": [\n        \"scripts/resume_20261126/immutable_point_normal_root_packets.py\",\n        \"b4c41b2dc8754607441c30cdb3a34199d7e40f8b52fc5e4a8f5d653ea524eac8\"\n    ],\n    \"fixed_fejer_previous_reference\": [\n        \"scripts/resume_20261126/so3_axisymmetric_reference.py\",\n        \"4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3\"\n    ],\n    \"fixed_fejer_previous_seed_reference\": [\n        \"scripts/resume_20261126/supported_smooth_triangle_meridian_reference.py\",\n        \"0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b\"\n    ],\n    \"fixed_fejer_previous_meridian\": [\n        \"scripts/resume_20261126/so3_supported_smooth_triangle_meridian_operator.py\",\n        \"6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865\"\n    ],\n    \"fixed_fejer_previous_new_moment_input\": [\n        \"scripts/resume_20261126/supported_smooth_triangle_literal_zero_moment_input.py\",\n        \"307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7\"\n    ],\n    \"fixed_fejer_previous_analytic_J3_binding\": [\n        \"scripts/resume_20261126/run10_immutable_point_source_binding.py\",\n        \"85f3007a6927968eb253eab168e9379f9a1f732caf5aa43b9f24776f39606d97\"\n    ],\n    \"fixed_fejer_previous_geometry\": [\n        \"scripts/resume_20261126/so3_run10_immutable_point_geometry.py\",\n        \"dbbd4601f4bbc0798759f3c63cd3caae3cfc19f1a62ec9dbd02cc6fbceb896ce\"\n    ],\n    \"fixed_fejer_previous_envelope_transfer\": [\n        \"scripts/resume_20261126/transfer_run10_immutable_point_memory.py\",\n        \"0007abf0b2814b09a3ecc30f621cbd8814a3d94528c753762aa7be5175d08486\"\n    ],\n    \"fixed_fejer_previous_independent_envelope_memory\": [\n        \"scripts/resume_20261126/complete_material_envelope_memory_public_run10.py\",\n        \"f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba\"\n    ],\n    \"fixed_fejer_previous_independent_input_projection_producer\": [\n        \"scripts/resume_20261126/freeze_run10_public_reference_and_restore_run05_carrier.py\",\n        \"fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a\"\n    ],\n    \"fixed_fejer_previous_actual_public_input_binding\": [\n        \"scripts/resume_20261126/actual_public_run10_reference_input_binding.py\",\n        \"9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209\"\n    ],\n    \"fixed_input_producer\": [\n        \"scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py\",\n        \"89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60\"\n    ],\n    \"stage_point_parent_root_packets\": [\n        \"scripts/resume_20261126/fixed_fejer_immutable_normal_root_packets.py\",\n        \"1445b883cbcf3ed76571760923c2dc735ead7c862439d9478684a5a5299de468\"\n    ],\n    \"stage_point_parent_stage_matrices\": [\n        \"scripts/resume_20261126/fixed_fejer_detached_stage_matrices.py\",\n        \"7aabf3ef5857dbdbbf9832b8bb4ca378faa7e06514a21b48f83649d6df7cb0d7\"\n    ],\n    \"stage_point_parent_adjacent_matrices\": [\n        \"scripts/resume_20261126/fixed_fejer_adjacent_normal_matrices.py\",\n        \"257e5e44d38dffb82925a410c42e51f084cf7821a398b9928e543088a3f234c0\"\n    ],\n    \"stage_point_parent_endpoint\": [\n        \"scripts/resume_20261126/fixed_fejer_normal_lift_operator.py\",\n        \"1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778\"\n    ],\n    \"stage_point_parent_binding\": [\n        \"scripts/resume_20261126/fixed_fejer_complete_source_binding.py\",\n        \"3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88\"\n    ],\n    \"stage_point_parent_envelope_transfer\": [\n        \"scripts/resume_20261126/transfer_fixed_fejer_material_envelope_memory.py\",\n        \"af35c30e4774987d8f71bc6d05c1942db66a9f7889127c19948b119dee9a1566\"\n    ],\n    \"stage_point_parent_geometry\": [\n        \"scripts/resume_20261126/so3_fixed_fejer_complete_geometry.py\",\n        \"bab4147bdd2f0d43a372ec1b04225fc66a05db2ccdc2f92968d3f70e2590bf26\"\n    ],\n    \"stage_point_parent_driver\": [\n        \"scripts/resume_20261126/fullclosed_fixed_fejer_immutable_point_so3_qp.py\",\n        \"477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd\"\n    ],\n    \"stage_point_parent_reader\": [\n        \"scripts/resume_20261126/read_fixed_fejer_immutable_point_so3_report.py\",\n        \"274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b\"\n    ],\n    \"scalar_progress\": [\n        \"scripts/resume_20261126/fixed_fejer_actual_mathematical_progress.py\",\n        \"bff1e03ae12a08444cb9d9d572e439a9b40cf59e80a201cd500f95539ce9e391\"\n    ],\n    \"mesh_input\": [\n        \"scripts/resume_20261126/fixed_fejer_stage_observed_same_field_mesh_input.py\",\n        \"b982e6d3ed8bb4e9615b5232932222bdb9298f95abfc9e3943875794f64a65d7\"\n    ],\n    \"mesh_arithmetic\": [\n        \"scripts/resume_20261126/fixed_fejer_complete_phase_mesh_arithmetic.py\",\n        \"80116a4bcfa2752274cece1148420cdce5c489faba3a8a7c0e92c0f6a8d058e4\"\n    ],\n    \"original_fixed_fejer_driver\": [\n        \"scripts/resume_20261126/fullclosed_fixed_fejer_stage_point_observed_so3_qp.py\",\n        \"8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d\"\n    ],\n    \"original_fixed_fejer_reader\": [\n        \"scripts/resume_20261126/read_fixed_fejer_stage_point_observed_so3_report.py\",\n        \"c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f\"\n    ],\n    \"original_fixed_fejer_launcher\": [\n        \"scripts/resume_20261126/launch_fixed_fejer_stage_point_observed_actions.py\",\n        \"ed81031fe1eb33684d35585e44022314c8a631821859376a200c874a2aa0e5fa\"\n    ],\n    \"complete_accurate_input_scope\": [\n        \"scripts/resume_20261126/fixed_fejer_stage_observed_normal_packet_accurate_field_input.py\",\n        \"720bbfc1071a3e56598fd096ec420e8cb5a44a60e06b28d33ff0f1c37e3038b3\"\n    ],\n    \"optional_closed_phase_source\": [\n        \"scripts/resume_20261126/fixed_fejer_stage_observed_closed_phase_grip_evidence.py\",\n        \"eddc1fb7d10cc6a24f8245920b93babbf71886e550ceb1b0293b892323548aa9\"\n    ]\n}",
        "occurrences": 1
      }
    ]
  },
  {
    "role": "reader",
    "parent": {
      "name": "read_fixed_fejer_same_field_phase_mesh_report.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_same_field_phase_mesh_report.py",
      "bytes": 22120,
      "sha256": "fde5c17f6b0a65f99d05f3ec0973571121899ce8844e93228cc68118975cb9b2",
      "git_blob_sha": "cd9dfc25d025350d9d175570532d4f011a951408"
    },
    "output": {
      "name": "read_fixed_fejer_stage_observed_same_field_phase_mesh_report.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_stage_observed_same_field_phase_mesh_report.py",
      "bytes": 22150,
      "sha256": "cd33879cc6b0164faac661b3c79f9084db1aa0e70a27c86fe56ecef6d7c4968e",
      "git_blob_sha": "53cafef3831afd17c218b8832ec1f7c568cde330"
    },
    "patches": [
      {
        "label": "mesh report schema",
        "before": "SCHEMA = \"actual-fixed-fejer-complete-same-field-closed-phase-mesh-refinement-v1\"",
        "after": "SCHEMA = \"actual-fixed-fejer-stage-observed-complete-same-field-closed-phase-mesh-refinement-v1\"",
        "occurrences": 1
      },
      {
        "label": "complete main filename",
        "before": "MAIN_NAME = \"fixed_fejer_complete_same_field_phase_meshes.py\"",
        "after": "MAIN_NAME = \"fixed_fejer_stage_observed_complete_same_field_phase_meshes.py\"",
        "occurrences": 1
      },
      {
        "label": "complete main SHA",
        "before": "MAIN_SHA = \"2acc9b4ee82623603d05f6a0951f01a0a3f92a4a640ca69b9f75814a45e5ab2d\"",
        "after": "MAIN_SHA = \"3e9a9f8fc63af7fde35442f7c5cf9d4f11c1d851fe4c8659e814e630d952b070\"",
        "occurrences": 1
      },
      {
        "label": "complete mesh roles",
        "before": "    if len(source_pins)!=117:",
        "after": "    if len(source_pins)!=127:",
        "occurrences": 1
      },
      {
        "label": "complete role diagnostic",
        "before": "Keep all 110 scientific roles and seven mesh/input/evidence source roles",
        "after": "Keep all 120 scientific roles and seven mesh/input/evidence source roles",
        "occurrences": 1
      }
    ]
  }
];
const META = {
  "runtime": [
    {
      "name": "fixed_fejer_stage_observed_same_field_mesh_input.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_same_field_mesh_input.py",
      "bytes": 73265,
      "sha256": "b982e6d3ed8bb4e9615b5232932222bdb9298f95abfc9e3943875794f64a65d7",
      "git_blob_sha": "a1711adb4adbf08f860da5c106c91f23d1b8267d"
    },
    {
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_phase_mesh_arithmetic.py",
      "bytes": 39436,
      "sha256": "80116a4bcfa2752274cece1148420cdce5c489faba3a8a7c0e92c0f6a8d058e4",
      "git_blob_sha": "57c2c563785dab3a1148645225106ca5860e2e2f",
      "name": "fixed_fejer_complete_phase_mesh_arithmetic.py"
    },
    {
      "name": "fixed_fejer_stage_observed_complete_same_field_phase_meshes.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_complete_same_field_phase_meshes.py",
      "bytes": 50400,
      "sha256": "3e9a9f8fc63af7fde35442f7c5cf9d4f11c1d851fe4c8659e814e630d952b070",
      "git_blob_sha": "d09a23ae04f618138aa05f3d7bb7846bbf927dc9"
    },
    {
      "name": "read_fixed_fejer_stage_observed_same_field_phase_mesh_report.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_stage_observed_same_field_phase_mesh_report.py",
      "bytes": 22150,
      "sha256": "cd33879cc6b0164faac661b3c79f9084db1aa0e70a27c86fe56ecef6d7c4968e",
      "git_blob_sha": "53cafef3831afd17c218b8832ec1f7c568cde330"
    }
  ],
  "entry": {
    "name": "fixed_fejer_stage_observed_complete_same_field_phase_meshes.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_complete_same_field_phase_meshes.py",
    "bytes": 50400,
    "sha256": "3e9a9f8fc63af7fde35442f7c5cf9d4f11c1d851fe4c8659e814e630d952b070",
    "git_blob_sha": "d09a23ae04f618138aa05f3d7bb7846bbf927dc9"
  },
  "reader": {
    "name": "read_fixed_fejer_stage_observed_same_field_phase_mesh_report.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_stage_observed_same_field_phase_mesh_report.py",
    "bytes": 22150,
    "sha256": "cd33879cc6b0164faac661b3c79f9084db1aa0e70a27c86fe56ecef6d7c4968e",
    "git_blob_sha": "53cafef3831afd17c218b8832ec1f7c568cde330"
  },
  "current_ready": {
    "name": "fixed-fejer-stage-point-observed-independent-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-point-observed-independent-complete-ready.json",
    "bytes": 97225,
    "sha256": "86d39c01d5a93c5a4d897a02d79bddd23a9b98daa6d6fae6940cc5d348da92f6",
    "git_blob_sha": "03daa9af5617879a6fea591a2a2d6dfe78e78836"
  },
  "current_driver": {
    "name": "fullclosed_fixed_fejer_stage_point_observed_so3_qp.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_stage_point_observed_so3_qp.py",
    "bytes": 95632,
    "sha256": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
    "git_blob_sha": "3a537a58e82f152c78d0408c8b2c5f4403af1106"
  },
  "current_launcher": {
    "name": "launch_fixed_fejer_stage_point_observed_actions.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_stage_point_observed_actions.py",
    "bytes": 21794,
    "sha256": "ed81031fe1eb33684d35585e44022314c8a631821859376a200c874a2aa0e5fa",
    "git_blob_sha": "1848230bd8a4f2dbbb4e4281e84d20d3d33ac531"
  },
  "current_reader": {
    "name": "read_fixed_fejer_stage_point_observed_so3_report.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_stage_point_observed_so3_report.py",
    "bytes": 98763,
    "sha256": "c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f",
    "git_blob_sha": "f37f64e9da226b40cc836c1b5f139eec342db764"
  },
  "accurate_input": {
    "role": "input",
    "name": "fixed_fejer_stage_observed_normal_packet_accurate_field_input.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_normal_packet_accurate_field_input.py",
    "bytes": 33017,
    "sha256": "720bbfc1071a3e56598fd096ec420e8cb5a44a60e06b28d33ff0f1c37e3038b3",
    "git_blob_sha": "eabc6d900dad8b46dc731fd4de9159b4050bb54d"
  },
  "closed_source": {
    "role": "closed_phase_grip",
    "name": "fixed_fejer_stage_observed_closed_phase_grip_evidence.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_closed_phase_grip_evidence.py",
    "bytes": 83826,
    "sha256": "eddc1fb7d10cc6a24f8245920b93babbf71886e550ceb1b0293b892323548aa9",
    "git_blob_sha": "33261dc5dff1eb2514c3497aca597f52abb09b68"
  },
  "closed_note": {
    "role": "implementation_note",
    "name": "2026-11-27-stage-observed-closed-phase-grip-r718-source-adapter.md",
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-stage-observed-closed-phase-grip-r718-source-adapter.md",
    "bytes": 17939,
    "sha256": "1ae4af46df209bff88922a2c620ff8f2baf5e71a4001ecc745d8926c24781c6f",
    "git_blob_sha": "33a2da6f3ef733c8cc48187773c1bb36d5ecb6fd"
  },
  "arithmetic": {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_phase_mesh_arithmetic.py",
    "bytes": 39436,
    "sha256": "80116a4bcfa2752274cece1148420cdce5c489faba3a8a7c0e92c0f6a8d058e4",
    "git_blob_sha": "57c2c563785dab3a1148645225106ca5860e2e2f",
    "name": "fixed_fejer_complete_phase_mesh_arithmetic.py"
  },
  "parents": {
    "final": {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-complete-same-field-phase-mesh-final-ready.json",
      "bytes": 50869,
      "sha256": "609e737dd835d7cdb3101f38f2797568e3fb8bbfcd88a1ea513bc6dae7e2aa5a",
      "git_blob_sha": "ea9664dd4b47e92bcda5b053b8975a7096c2fdd8",
      "name": "fixed-fejer-complete-same-field-phase-mesh-final-ready.json"
    },
    "packet": {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-complete-same-field-phase-mesh-packet-ready.json",
      "bytes": 50836,
      "sha256": "f3768a3a0ccb3da29045107072a363ef6d7fae761e4596e3de4efb2448e31b25",
      "git_blob_sha": "e96662325c7122a6b298558a8e434b6cce890905",
      "name": "fixed-fejer-complete-same-field-phase-mesh-packet-ready.json"
    }
  },
  "reproducer_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_stage_observed_same_field_meshes.mjs",
  "completed_reference_evidence": {
    "complete_returned_source": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46037017666-1-part-001.md",
      "bytes": 16596,
      "sha256": "a17878d025623ae6280d6b1afa42d9be36288f72c93b3802659453d205ed5b17",
      "git_blob_sha": "8d49505495b777f7cc84c73c15fee4247ff76ff9",
      "actual_run_id": "46037017666",
      "actual_attempt": 1,
      "returned_stages": [
        1,
        2
      ],
      "complete_actual_six_input_records_in_ready": true,
      "current_scalar_leaves": 2218,
      "current_accuracy_reached": false,
      "historical2397_leaves_used_as_current": false
    },
    "complete_identity": {
      "run_id": "46037017666",
      "run_attempt": "1",
      "mathematical_target_identity_sha256": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "current_public_reference_model_identity_sha256": "ea64e2fe5e272648195128d53521705cc266d82f7d2636bd7201b90fcf172fac",
      "current_fixed_target_definition_identity_sha256": "50df37b6b832dcdd53d05c54138e62e43df6b14df68d946a7b8a7b8227f58319",
      "current_fixed_target_file": {
        "path": "/home/runner/work/_temp/visible-larger-research-46037017666-1/research/fixed-fejer-reference/fixed-target-definition.json",
        "sha256": "777a69e77b34a8fda152442ca7e326a48c91050edaae69ade0355f5c8b8628df",
        "bytes": 30919
      },
      "current_complete_carrier_target_binding_file": {
        "path": "/home/runner/work/_temp/visible-larger-research-46037017666-1/research/fixed-fejer-reference/material-envelope-carrier-binding.json",
        "sha256": "9edf8a4dd6edec259f615362f1155a811dff79e257de8d1a7579be924fe6a0eb",
        "bytes": 35712
      },
      "current_scalar_profile_definition_identity_sha256": "d492e4ad97245a8474f1a73a8787aac2fc5691b1f928d0b8ea72224cabd55160",
      "current_fixed_chart_sha256": "af8ab672f847163fe02999df70a031cd5e4a495ed89c788ad0dffc8786651103",
      "current_scalar_reference_leaf_count": 2218,
      "current_reference_accuracy_reached": false,
      "historical_scalar_values_used_as_current_reference": false,
      "historical_mathematical_g_equality_claimed": false,
      "full_public_input_evidence_path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46037017666-1-part-001.md",
      "full_public_input_evidence_sha256": "a17878d025623ae6280d6b1afa42d9be36288f72c93b3802659453d205ed5b17",
      "full_public_input_evidence_bytes": 16596,
      "full_public_input_evidence_git_blob_sha": "8d49505495b777f7cc84c73c15fee4247ff76ff9",
      "complete_six_current_input_files": {
        "current_fixed_input_bundle": {
          "path": "/home/runner/work/_temp/visible-larger-research-46037017666-1/research/fixed-fejer-r690-inputs/fixed-reference-input.npz",
          "sha256": "b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98",
          "bytes": 4334
        },
        "current_node_report": {
          "path": "/home/runner/work/_temp/visible-larger-research-46037017666-1/research/fixed-fejer-r690-inputs/fixed-affine-nodes.json",
          "sha256": "1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5",
          "bytes": 144306
        },
        "current_scalar_input": {
          "path": "/home/runner/work/_temp/visible-larger-research-46037017666-1/research/fixed-fejer-r690-inputs/fixed-scalar-input.json",
          "sha256": "2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189",
          "bytes": 40488
        },
        "current_reference_bundle": {
          "path": "/home/runner/work/_temp/visible-larger-research-46037017666-1/research/fixed-fejer-reference/reference.npz",
          "sha256": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb",
          "bytes": 894879
        },
        "current_carrier": {
          "path": "/home/runner/work/_temp/visible-larger-research-46037017666-1/research/fixed-fejer-reference/observations.npz",
          "sha256": "84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e",
          "bytes": 205842
        },
        "current_preparation_report": {
          "path": "/home/runner/work/_temp/visible-larger-research-46037017666-1/research/fixed-fejer-reference/report.json",
          "sha256": "ff41237c4b6caf4eac6fd82f90212ff44c54930ba00c24a923a1ddc8b9cbc373",
          "bytes": 84966
        }
      },
      "side_input_records": {
        "fixed_input_preparation_report": {
          "path": "/home/runner/work/_temp/visible-larger-research-46037017666-1/research/fixed-fejer-r690-inputs/report.json",
          "sha256": "edbf5d6b2a33bd094fed680020e43370e8f7f6af83233cb4078b0154c248a7b4",
          "bytes": 65340
        },
        "new_locations": {
          "path": "/home/runner/work/_temp/visible-larger-research-46037017666-1/research/fixed-fejer-reference/locations.json",
          "sha256": "d1d7eee827a1da2901adbcacf6d277ae89b69c176140e1a1fc311591423000fd",
          "bytes": 106771
        },
        "complete_supplied_location_provenance": {
          "path": "/home/runner/work/_temp/visible-larger-research-46037017666-1/research/fixed-fejer-reference/supplied-location-provenance.json",
          "sha256": "b753b3d416e4f842d2311cb3e296233a8ce77ab5207145a1757eb781fb03a0c6",
          "bytes": 223955
        }
      },
      "actual_maker_source_commit": "5aacee6d6e4aea51c1496926422dc8440a36fb4b",
      "actual_reference_source_commit": "518f48de9f3bef63e2dc7d059dca5af0330f3344",
      "actual_current_field_point_available_not_assumed": true,
      "prepared_input_is_not_a_physical_field": true
    },
    "prepared_reference_is_not_a_field": true
  }
};
const EXPECTED_READY = {
  "final": {
    "name": "fixed-fejer-stage-observed-same-field-phase-mesh-final-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-observed-same-field-phase-mesh-final-ready.json",
    "bytes": 60573,
    "sha256": "f47e183bda69adbef11ceb640ef3f698eed8d9f0f207687b08c23117d2e36dad",
    "git_blob_sha": "c83ad722e8e576dcbfaba78b63f06b1598dc846c"
  },
  "packet": {
    "name": "fixed-fejer-stage-observed-same-field-phase-mesh-packet-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-observed-same-field-phase-mesh-packet-ready.json",
    "bytes": 60542,
    "sha256": "97f5d3fda19c68dec8e0d4d879438088ad6c8b6d4fec021bce3a247ac41a904f",
    "git_blob_sha": "d9469eb9c11c3c41e6d4543b4f4cdc410da76422"
  }
};

function buildMesh16Ready(parent,mode,current,meta,roles) {
 const copy=x=>JSON.parse(JSON.stringify(x));
 const r=copy(parent),oldOut="fixed-fejer-same-field-phase-mesh-"+mode+"-v1",newOut="fixed-fejer-stage-observed-same-field-phase-mesh-"+mode+"-v1";
 const pairs=[[oldOut,newOut],["fixed-fejer-immutable-point-first","fixed-fejer-stage-point-observed-independent"]];
 const replace=s=>pairs.reduce((a,[o,n])=>a.split(o).join(n),s);
 const relabel=v=>typeof v==="string"?replace(v):Array.isArray(v)?v.map(relabel):v&&typeof v==="object"?Object.fromEntries(Object.entries(v).map(([k,a])=>[replace(k),relabel(a)])):v;
 r.schema="complete-fixed-fejer-stage-observed-same-field-closed-phase-mesh-parameters-v1";
 r.actual_original_scientific_run="46037017666/1";
 r.source_sha256=Object.fromEntries(meta.runtime.map(x=>[x.name,x.sha256]));
 r.complete_runtime_source_records=meta.runtime.map(x=>({kind:"complete_runtime_source",...copy(x)}));
 r.complete_original_scientific_parameter_source={
  ...r.complete_original_scientific_parameter_source,...copy(meta.current_ready),
  original_script:current.steps[0].script,original_complete_argv:copy(current.steps[0].args),
  original_complete_source_sha256_by_role:Object.fromEntries(Object.entries(roles).map(([k,v])=>[k,v[1]])),
  actual_command_required_path:"{work}/fixed-fejer-stage-point-observed-independent-command.json"
 };
 r.complete_field_scope.complete_actual_field_input_scope=copy(meta.accurate_input);
 r.full_scientific_source_role_count=120;r.full_mesh_source_role_count=127;
 r.scope=parent.scope+" The actual stage-observed driver/reader/launcher, all120 scientific source roles and the complete run16 command are retained; mathematical live progress is never substituted for a complete immutable snapshot.";
 r.steps=relabel(parent.steps);
 r.steps[0].id="complete-fixed-fejer-stage-observed-same-field-phase-mesh-"+mode+"-20261127";
 r.steps[1].id="actual-fixed-fejer-stage-observed-same-field-phase-mesh-"+mode+"-20261127";
 r.steps[0].script=meta.entry.path;r.steps[1].script=meta.reader.path;
 r.steps[0].scope=r.scope;
 r.steps[1].scope=parent.steps[1].scope+" Actual complete run16 source and input identities are read; no scientific calls are added.";
 const closedPath="{work}/fixed-fejer-stage-observed-complete-closed-phase-grip-v1/report.json";
 r.optional_complete_closed_phase_evidence={
  ...r.optional_complete_closed_phase_evidence,source:copy(meta.closed_source),proof_note:copy(meta.closed_note),
  report_path:closedPath,argument_if_attaching_the_actual_complete_report:["--closed-phase-report",closedPath]
 };
 r.progress_publication_contract=relabel(parent.progress_publication_contract);
 r.complete_source_derivation={
  complete_original_mesh_commit:"244906aebea68c73a74cda79f108df35953c8402",
  complete_original_parameter_file:copy(meta.parents[mode]),
  entire_earlier_derivation:copy(parent.complete_source_derivation),
  source_only_text_operations:true,local_AST_or_compile_or_scientific_execution:false,
  source_reproducer_is_not_an_admission_gate:true,
  complete_reproducer_path:meta.reproducer_path,
  all_original_numerical_parameters_formal_selectors_and_live_mapping_preserved:true,
  original_8924_byte_constructor_remains_whole:true,
  shared_complete_arithmetic_unchanged:copy(meta.arithmetic),
  original_launcher_command_schema_retained_from_actual_source:true
 };
 r.actual_completed_reference_input_evidence=copy(meta.completed_reference_evidence);
 return r;
}

function parseTupleRegistry(raw) {
 let out="",quoted=false,escaped=false;
 for(const c of raw){
  if(quoted){out+=c;if(escaped)escaped=false;else if(c==="\\")escaped=true;else if(c==='"')quoted=false;continue;}
  if(c==='"'){quoted=true;out+=c;}else if(c==="(")out+="[";else if(c===")")out+="]";else out+=c;
 }
 if(quoted||escaped)throw Error("Incomplete quoted source registry");
 return JSON.parse(out);
}

const sha = value => createHash("sha256").update(value).digest("hex");
const bytes = value => Buffer.byteLength(value,"utf8");
const options = {};
const words = process.argv.slice(2);
for(let i=0;i<words.length;i+=2){
 if(!["--repo","--outdir"].includes(words[i]) || !words[i+1] || options[words[i]]) throw Error("Use complete --repo and --outdir pairs");
 options[words[i]]=resolve(words[i+1]);
}
if(Object.keys(options).length!==2)throw Error("Required: --repo REPOSITORY --outdir FRESH_OUTSIDE_REPOSITORY");
const repo=options["--repo"],outdir=options["--outdir"];
if(outdir===repo||outdir.startsWith(repo+"/"))throw Error("Use an independent output directory outside the repository");
async function readBound(record){
 const raw=await readFile(join(repo,record.path));
 if(raw.length!==record.bytes||sha(raw)!==record.sha256)throw Error("Changed whole input "+record.path);
 return raw.toString("utf8");
}
function checkBody(body,record){
 if(bytes(body)!==record.bytes||sha(body)!==record.sha256)throw Error("Derived whole identity differs "+record.name);
}
function replaceCount(body,before,after,count,label){
 if(body.split(before).length-1!==count)throw Error("Changed complete replacement "+label);
 return body.split(before).join(after);
}
const prepared={};
for(const job of SOURCE_JOBS){
 const parent=await readBound(job.parent);
 let body=parent;
 for(const q of job.patches)body=replaceCount(body,q.before,q.after,q.occurrences,q.label);
 checkBody(body,job.output);
 let restored=body;
 for(const q of [...job.patches].reverse())restored=replaceCount(restored,q.after,q.before,q.occurrences,q.label+" reverse");
 if(restored!==parent)throw Error("The complete source parent was not retained "+job.role);
 prepared[job.output.name]=body;
}
for(const r of [META.arithmetic,META.accurate_input,META.closed_source,META.closed_note,META.current_launcher,META.current_reader])await readBound(r);
const driver=await readBound(META.current_driver);
const marker="SOURCE_PINS = ";
const start=driver.indexOf(marker);
const finish=driver.indexOf("\n\n",start);
if(start<0||finish<0)throw Error("Keep the actual complete literal source registry");
const roles=parseTupleRegistry(driver.slice(start+marker.length,finish).trim());
if(Object.keys(roles).length!==120)throw Error("Keep all120 actual scientific source roles");
const current=JSON.parse(await readBound(META.current_ready));
for(const mode of ["final","packet"]){
 const parent=JSON.parse(await readBound(META.parents[mode]));
 const result=buildMesh16Ready(parent,mode,current,META,roles);
 const body=JSON.stringify(result,null,2)+"\n";
 checkBody(body,EXPECTED_READY[mode]);
 prepared[EXPECTED_READY[mode].name]=body;
}
await mkdir(dirname(outdir),{recursive:true});
await mkdir(outdir,{recursive:false});
for(const[name,body]of Object.entries(prepared))await writeFile(join(outdir,name),body,{flag:"wx"});
process.stdout.write(JSON.stringify({
 schema:"complete-fixed-fejer-stage-observed-same-field-mesh-text-reproduction-v1",
 complete_new_sources:SOURCE_JOBS.map(x=>x.output),complete_ready_files:EXPECTED_READY,
 complete_shared_arithmetic:META.arithmetic,scientific_calls:0,
 original_all_domain_numerical_parameters_preserved:true,source_reproducer_is_not_an_admission_gate:true
},null,2)+"\n");
