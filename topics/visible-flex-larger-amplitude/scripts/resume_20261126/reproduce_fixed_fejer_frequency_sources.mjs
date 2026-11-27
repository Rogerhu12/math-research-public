#!/usr/bin/env node
/** Reproduce the complete independent Fejer M160-to-M320 source family.
 * Uses complete immutable source files, source text transformations and SHA256 only.
 * Does not import or run Python, NumPy, Torch, F, J, roots, fixtures or solvers.
 * This archival construction utility is not an additional scientific admission gate.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const INPUTS={
  "oldM": {
    "frequency_layout": {
      "name": "so3_frequency_refinement_layout.py",
      "bytes": 13582,
      "sha256": "ce188ae4bdf1ccecfbf9549897284e8dc44f4722e04e974c7a0cd045c78a3a27",
      "git_blob_sha": "8d459b9b1dc3defda44b58bc36c306fe586c484e"
    },
    "meridian": {
      "name": "so3_frequency_refined_smooth_triangle_meridian_operator.py",
      "bytes": 42982,
      "sha256": "41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2",
      "git_blob_sha": "20b4707c1ea7628d7bd922d24ba0226da276c2d1"
    },
    "reference_calibration": {
      "name": "run10_frequency_immutable_point_calibration.py",
      "bytes": 12374,
      "sha256": "61ad9a9e782c0fd67bf83887d8414968946e8543baac773dcc628419f0248992",
      "git_blob_sha": "715f78e4e1b6245c68e1229a3e936ceebf7f6e36"
    },
    "analytic_J3_binding": {
      "name": "run10_frequency_immutable_point_source_binding.py",
      "bytes": 38000,
      "sha256": "1cf73abf9170964d194b1963c0fb54839c9326bb509510eee04303746f6fa1f8",
      "git_blob_sha": "9a547b35fef277520dea5bb2f1e058d2e412c3bb"
    },
    "envelope_transfer": {
      "name": "transfer_run10_frequency_immutable_point_memory.py",
      "bytes": 82837,
      "sha256": "952790e603606e1efeff10c89580383567e7e645524a4601b68dde1bbe09207b",
      "git_blob_sha": "85dce5cb7466baf038ab00616c9b7b17e1e51195"
    }
  },
  "fixed": {
    "reference": {
      "name": "fixed_fejer_axisymmetric_reference.py",
      "bytes": 60335,
      "sha256": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
      "git_blob_sha": "8ad0794ebf0daab9a278c5ea1de784e93b64fd8c"
    },
    "seed_reference": {
      "name": "fixed_fejer_supported_meridian_reference.py",
      "bytes": 39771,
      "sha256": "ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a",
      "git_blob_sha": "ad7f2d9ea2e63df16d900cf12885d611fef5d823"
    },
    "meridian": {
      "name": "fixed_fejer_supported_so3_meridian_operator.py",
      "bytes": 40840,
      "sha256": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
      "git_blob_sha": "1d9e435bb68374b71c3d7361771c28f47838d59e"
    },
    "new_moment_input": {
      "name": "fixed_fejer_literal_zero_moment_input.py",
      "bytes": 31409,
      "sha256": "ca4fef4066bfb6d6fedbdf9b65349f7f0ba8480376858c84faa8ee3d4d4b97b3",
      "git_blob_sha": "172d2b82eca6496058d2c73560de86bada50f12d"
    }
  },
  "lower": {
    "closure_values": {
      "name": "fixed_fejer_immutable_closure_values.py",
      "bytes": 59048,
      "sha256": "01ca74a9f00ac17ef4452173b758d785c0e06869efa98980426f822d4beeb595",
      "git_blob_sha": "f8d32aefb1c11152fd39ad1d5b6d160c60d864ef"
    },
    "analytic_J3": {
      "name": "fixed_fejer_analytic_stage_jacobian.py",
      "bytes": 25739,
      "sha256": "7645268ee3538a43a4a04b73a5aee4fc5483b56962affeb0ba7e7f879d5d4a72",
      "git_blob_sha": "4fd818ed74a7043b955ef036a0cccccdb3cdc710"
    },
    "analytic_frame": {
      "name": "fixed_fejer_analytic_normal_frame.py",
      "bytes": 47286,
      "sha256": "75db2f20039b66a2784a922bf062e792328c0153fb0458c16acef92e0ab7e38c",
      "git_blob_sha": "ee0e9799f87301d8a60d6da20cb68731d031cdb0"
    },
    "frame_C1": {
      "name": "fixed_fejer_normal_frame_c1.py",
      "bytes": 37361,
      "sha256": "1830c1d8e69e0e12d4b9d8af9f194d234ef3437cba546200738a1592a77aa0ca",
      "git_blob_sha": "9b3464345766a956159db88d5d6c4326b662ece4"
    },
    "stage_matrices": {
      "name": "fixed_fejer_detached_stage_matrices.py",
      "bytes": 47791,
      "sha256": "7aabf3ef5857dbdbbf9832b8bb4ca378faa7e06514a21b48f83649d6df7cb0d7",
      "git_blob_sha": "4fad02c03e92b5fcd3aa2b3621c58a49d1631eff"
    },
    "adjacent_matrices": {
      "name": "fixed_fejer_adjacent_normal_matrices.py",
      "bytes": 36766,
      "sha256": "257e5e44d38dffb82925a410c42e51f084cf7821a398b9928e543088a3f234c0",
      "git_blob_sha": "14ad8790e43b2e58f94772aacd98fb61be7826e9"
    },
    "reference_calibration": {
      "name": "fixed_fejer_reference_calibration.py",
      "bytes": 11914,
      "sha256": "fe36240c08ad32c4d4d665a387c70aaf02c0392419a51eef01e072081945e95c",
      "git_blob_sha": "c174fcf9712b76abe6f3f3ed307d0115598a1d3d"
    },
    "endpoint": {
      "name": "fixed_fejer_normal_lift_operator.py",
      "bytes": 98490,
      "sha256": "1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778",
      "git_blob_sha": "fd9b4ba9526a7805c73957ffc75a3261fa785290"
    },
    "root_packets": {
      "name": "fixed_fejer_immutable_normal_root_packets.py",
      "bytes": 72375,
      "sha256": "1445b883cbcf3ed76571760923c2dc735ead7c862439d9478684a5a5299de468",
      "git_blob_sha": "12d26c8b663d185907feec930aa09def002af4cb"
    }
  },
  "upper": {
    "binding": {
      "name": "fixed_fejer_complete_source_binding.py",
      "bytes": 32487,
      "sha256": "3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88",
      "git_blob_sha": "3073c9490a6bc6ce7dcf323f799ee8075f8bdd78"
    },
    "transfer": {
      "name": "transfer_fixed_fejer_material_envelope_memory.py",
      "bytes": 66839,
      "sha256": "af35c30e4774987d8f71bc6d05c1942db66a9f7889127c19948b119dee9a1566",
      "git_blob_sha": "597f6529dea5ffeb32e8df43a1442f1f7994d48b"
    },
    "geometry": {
      "name": "so3_fixed_fejer_complete_geometry.py",
      "bytes": 70709,
      "sha256": "bab4147bdd2f0d43a372ec1b04225fc66a05db2ccdc2f92968d3f70e2590bf26",
      "git_blob_sha": "f2b28d1bf2f994db9866cb58e74a522ff719358a"
    },
    "driver": {
      "name": "fullclosed_fixed_fejer_immutable_point_so3_qp.py",
      "bytes": 91714,
      "sha256": "477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd",
      "git_blob_sha": "feb49510ddada8fb77d0bf9cf3cd78c1de50079d"
    },
    "launcher": {
      "name": "launch_fixed_fejer_immutable_point_actions.py",
      "bytes": 21789,
      "sha256": "0c1ff0aa2de30fcd490efb4bddd1972613c0f0afb1257d1af0170ac7e60bb5bf",
      "git_blob_sha": "f5d337a07f6b1a0438f33cdaf6fc1845b30f8b84"
    },
    "reader": {
      "name": "read_fixed_fejer_immutable_point_so3_report.py",
      "bytes": 97987,
      "sha256": "274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b",
      "git_blob_sha": "feae7eaf1b29ea0ae2563c4fc0d8089794602fa3"
    }
  }
};
const EXPECTED={
  "frequency_layout": {
    "name": "fixed_fejer_frequency_layout.py",
    "bytes": 13582,
    "sha256": "67c5503e8df036aa1468a3df2f395f5a33c91c4309520fbb8862b39c2495a251",
    "git_blob_sha": "6fff72221e35c9835bdedfa7dd5089f05e200937"
  },
  "meridian": {
    "name": "fixed_fejer_frequency_meridian_operator.py",
    "bytes": 43041,
    "sha256": "f7058f9c9d3f02292b738b360b116062b60bcf07907286acb42346eb431bdf9a",
    "git_blob_sha": "fdcb0339b20957a8cccfef0000b90da69067ac17"
  },
  "new_moment_input": {
    "name": "fixed_fejer_frequency_literal_moment_input.py",
    "bytes": 31477,
    "sha256": "4bf9e5b96884e26750f6f08cffcc338965d94969e7516c3d2ed493d037697849",
    "git_blob_sha": "464fa397a7fa322e8739531213551d4811175f43"
  },
  "closure_values": {
    "name": "fixed_fejer_frequency_closure_values.py",
    "bytes": 59771,
    "sha256": "6949ca97c49d338761ef2bc5e748ed9a55e20682a6e6225a7fc2bc63ead2bc88",
    "git_blob_sha": "46a10d1e9a03319e92784b8d6f514e46c15938d0"
  },
  "analytic_J3": {
    "name": "fixed_fejer_frequency_stage_jacobian.py",
    "bytes": 25706,
    "sha256": "740d3b39fcbdbb766962d26d3ec960b8883810418af83f13bd7b55c11776dbc3",
    "git_blob_sha": "c2315e13e8ba8c87855294f3dc8e47754e95cb56"
  },
  "analytic_frame": {
    "name": "fixed_fejer_frequency_normal_frame.py",
    "bytes": 47253,
    "sha256": "e165dda2543dd4175fa1f7187dfd28cad84ac08ec95a24f27a5e6addcaa2fc34",
    "git_blob_sha": "0dffec85d09398ec68095d2a7fc2c1ffd99eb46d"
  },
  "frame_C1": {
    "name": "fixed_fejer_frequency_frame_c1.py",
    "bytes": 37361,
    "sha256": "9d001b492aa49058b545e05eb67c6eb2413fa512580393243955f8a706015fdd",
    "git_blob_sha": "67d2ac4cfa8e31339343adbe47ca5c8b4b214a93"
  },
  "stage_matrices": {
    "name": "fixed_fejer_frequency_stage_matrices.py",
    "bytes": 47791,
    "sha256": "f30eac74cfb436cd40fa3413d4ca4c037ef1fe79ac05b442738de07eef522642",
    "git_blob_sha": "f368ec12a52edb995bb0c0d65a2017cb74687701"
  },
  "adjacent_matrices": {
    "name": "fixed_fejer_frequency_adjacent_matrices.py",
    "bytes": 36766,
    "sha256": "59e9089bc991136ff9e1e2fd4a37663d7f91c03837eac9bd49c8d49c206ce015",
    "git_blob_sha": "fb4374b147c33084df41df2aed826ca0ab6e29bf"
  },
  "reference_calibration": {
    "name": "fixed_fejer_frequency_calibration.py",
    "bytes": 12329,
    "sha256": "90a8c8eae8d67d5d09fc09ad0593872e40037256779cb94e5eab5fbbff25b11e",
    "git_blob_sha": "0d7d9ca5d2a81d108acf237eca96bc12029ed2dd"
  },
  "endpoint": {
    "name": "fixed_fejer_frequency_normal_lift.py",
    "bytes": 98459,
    "sha256": "60769d4999af17f6dc904400e414e3f34ec1000bd84529ad168dca67f6889b5f",
    "git_blob_sha": "2fca2cd110ea329788e8cfe1d18984a5c8717cfc"
  },
  "root_packets": {
    "name": "fixed_fejer_frequency_root_packets.py",
    "bytes": 73037,
    "sha256": "767be252b02b0f92ee1a7229881cfa693a2d4e73f48f6a703fe0c21340c59b78",
    "git_blob_sha": "b4dbba342bc412cf91241ce909b0329dc53e1052"
  },
  "analytic_J3_binding": {
    "name": "fixed_fejer_frequency_source_binding.py",
    "bytes": 35685,
    "sha256": "caf16fbc87ef618ddae5ba42616d9bbe136beac6d32487224073ac6958c4d3c0",
    "git_blob_sha": "8a25d59f8a2fa2c818af8d3d17875d1ca5ae8a33"
  },
  "envelope_transfer": {
    "name": "transfer_fixed_fejer_frequency_memory.py",
    "bytes": 84194,
    "sha256": "1d35b2e7231ed5609e066e602f0f4722bb931b89bb9b3acea132cb45cc510bb8",
    "git_blob_sha": "66571893cb9f27a6b830b831e83052d5950059c0"
  },
  "geometry": {
    "name": "so3_fixed_fejer_frequency_geometry.py",
    "bytes": 70658,
    "sha256": "70c083a3cb8925b5e38ace61f646c87ec0204f22743acf3bcb22fcdab9aabe77",
    "git_blob_sha": "877460a2fc4bf5dd4aa3943a46027e606ab7fde4"
  },
  "driver": {
    "name": "fullclosed_fixed_fejer_frequency_so3_qp.py",
    "bytes": 96268,
    "sha256": "fff956cc086c8f69c7de87c2d9117792b6b1d5e1de853e59a992fb67e04b4e51",
    "git_blob_sha": "557e4823a9dd5892699767a55515339ac02c88a1"
  },
  "launcher": {
    "name": "launch_fixed_fejer_frequency_actions.py",
    "bytes": 22336,
    "sha256": "596e137f6e381a2fdbc882a559a30b664c6e985095867535f3b32d7fa61c417c",
    "git_blob_sha": "a2055fd88befd873367c8ea835e30cde41d11820"
  },
  "reader": {
    "name": "read_fixed_fejer_frequency_so3_report.py",
    "bytes": 98354,
    "sha256": "b79c352d11b41de5384016f103c07db7abc2a41bf438ef92fe20b8a9b43e75bb",
    "git_blob_sha": "a84b93ef25817001ef99ec4ee953bf78e4d45658"
  }
};
const NAMES={
  "frequency_layout": "fixed_fejer_frequency_layout.py",
  "meridian": "fixed_fejer_frequency_meridian_operator.py",
  "new_moment_input": "fixed_fejer_frequency_literal_moment_input.py",
  "closure_values": "fixed_fejer_frequency_closure_values.py",
  "analytic_J3": "fixed_fejer_frequency_stage_jacobian.py",
  "analytic_frame": "fixed_fejer_frequency_normal_frame.py",
  "frame_C1": "fixed_fejer_frequency_frame_c1.py",
  "stage_matrices": "fixed_fejer_frequency_stage_matrices.py",
  "adjacent_matrices": "fixed_fejer_frequency_adjacent_matrices.py",
  "reference_calibration": "fixed_fejer_frequency_calibration.py",
  "endpoint": "fixed_fejer_frequency_normal_lift.py",
  "root_packets": "fixed_fejer_frequency_root_packets.py",
  "analytic_J3_binding": "fixed_fejer_frequency_source_binding.py",
  "envelope_transfer": "transfer_fixed_fejer_frequency_memory.py",
  "geometry": "so3_fixed_fejer_frequency_geometry.py",
  "driver": "fullclosed_fixed_fejer_frequency_so3_qp.py",
  "launcher": "launch_fixed_fejer_frequency_actions.py",
  "reader": "read_fixed_fejer_frequency_so3_report.py"
};
const SCHEMAS={
  "layout": "complete-fixed-fejer-M160-to-M320-frequency-inclusion-v1",
  "base": "complete-fixed-fejer-frequency-refined-frozen-reference-so3-meridian-v1",
  "Q": "fixed-fejer-frequency-refined-literal-zero-endpoint-Q-input-v1",
  "Qdefinition": "fixed-fejer-frequency-refined-literal-two-bubble-endpoint-Q-v1",
  "endpoint": "complete-fixed-fejer-frequency-refined-immutable-point-normal-layer-v1",
  "binding": "complete-fixed-fejer-frequency-refined-source-model-binding-v1",
  "snapshot": "actual-fixed-fejer-frequency-refined-current-point-snapshot-v1",
  "transfer": "complete-fixed-fejer-M160-to-M320-history-transfer-v1",
  "driver": "complete-fixed-fejer-frequency-refined-immutable-point-SO3-QP-v1",
  "reader": "actual-fixed-fejer-frequency-refined-immutable-point-SO3-readout-v1"
};
const ORIGINAL_SOURCE_ROLES={
  "root_packets": [
    "scripts/resume_20261126/fixed_fejer_immutable_normal_root_packets.py",
    "1445b883cbcf3ed76571760923c2dc735ead7c862439d9478684a5a5299de468"
  ],
  "analytic_parent_stage_matrices": [
    "scripts/resume_20261126/detached_normal_stage_matrix_reuse.py",
    "375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59"
  ],
  "analytic_parent_adjacent_matrices": [
    "scripts/resume_20261126/adjacent_normal_frame_matrices.py",
    "955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3"
  ],
  "analytic_parent_driver": [
    "scripts/resume_20261126/fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py",
    "95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9"
  ],
  "analytic_parent_reader": [
    "scripts/resume_20261126/read_reference_centred_independent_chart_material_envelope_so3_report.py",
    "f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470"
  ],
  "analytic_J3": [
    "scripts/resume_20261126/fixed_fejer_analytic_stage_jacobian.py",
    "7645268ee3538a43a4a04b73a5aee4fc5483b56962affeb0ba7e7f879d5d4a72"
  ],
  "analytic_J3_binding": [
    "scripts/resume_20261126/fixed_fejer_complete_source_binding.py",
    "3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88"
  ],
  "analytic_parent_frame_C1": [
    "scripts/resume_20261126/normal_frame_c1_reuse.py",
    "ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9"
  ],
  "seed_reference": [
    "scripts/resume_20261126/fixed_fejer_supported_meridian_reference.py",
    "ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a"
  ],
  "seed_mean": [
    "scripts/resume_20261126/supported_smooth_triangle_seed_mean_jets.py",
    "f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917"
  ],
  "reference": [
    "scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py",
    "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"
  ],
  "warm_producer": [
    "notes/2026-11-17-parallel-model-fullclosed-hold-warm.py",
    "bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3"
  ],
  "observed": [
    "scripts/resume_20261120/gauss_observed_closed_gram.py",
    "26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d"
  ],
  "deep_scalar": [
    "scripts/resume_20261126/deep_valley_tail_input.py",
    "e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2"
  ],
  "scalar": [
    "notes/2026-11-17-parallel-model-full-hold-oracle.py",
    "a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670"
  ],
  "integer": [
    "notes/2026-11-17-parallel-inward-integral-enclosure.py",
    "babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0"
  ],
  "hold": [
    "scripts/parallel_20261117_negative_hold_profile_ivp.py",
    "ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1"
  ],
  "meridian": [
    "scripts/resume_20261126/fixed_fejer_supported_so3_meridian_operator.py",
    "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3"
  ],
  "geometry": [
    "scripts/resume_20261126/so3_fixed_fejer_complete_geometry.py",
    "bab4147bdd2f0d43a372ec1b04225fc66a05db2ccdc2f92968d3f70e2590bf26"
  ],
  "qp": [
    "scripts/resume_20261120/fullspace_feasible_active_cg_v3.py",
    "fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4"
  ],
  "spectral": [
    "scripts/resume_20261120/positive_spectral_gram_weights.py",
    "e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91"
  ],
  "hessian": [
    "scripts/resume_20261120/positive_spectral_gram_hessian.py",
    "29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4"
  ],
  "centered": [
    "scripts/resume_20261126/centered_spectral_statistics.py",
    "5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01"
  ],
  "history": [
    "scripts/resume_20261120/launch_refinement_from_full_report.py",
    "4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60"
  ],
  "pure_geometry": [
    "scripts/resume_20261120_curvature_qp.py",
    "a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854"
  ],
  "geometry_selector": [
    "scripts/resume_20261120/fullclosed_point_inequalities_v2.py",
    "e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8"
  ],
  "endpoint": [
    "scripts/resume_20261126/fixed_fejer_normal_lift_operator.py",
    "1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778"
  ],
  "axisymmetric_seed_driver": [
    "scripts/resume_20261126/fullclosed_axisymmetric_so3_qp.py",
    "606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9"
  ],
  "frozen_moment_input": [
    "scripts/resume_20261126/frozen_zero_moment_input.py",
    "4dc3e1a8ba8f128e1d05176f4d0f4b18c62d278fed603cc46f7ed686f6e4e611"
  ],
  "moment_trace_source": [
    "scripts/resume_20261126/trace_zero_initial_endpoint_failure.py",
    "73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54"
  ],
  "moment_initial_binding": [
    "scripts/resume_20261126/diagnose_zero_initial_chord.py",
    "65787b3e51f80505f5619c35fb05f8ad064e88de111578ff53e8bdad442092c0"
  ],
  "moment_original_endpoint": [
    "scripts/resume_20261126/so3_zero_closure_endpoint_operator.py",
    "5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46"
  ],
  "moment_original_driver": [
    "scripts/resume_20261126/fullclosed_zero_closure_so3_qp.py",
    "b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b"
  ],
  "new_moment_input": [
    "scripts/resume_20261126/fixed_fejer_literal_zero_moment_input.py",
    "ca4fef4066bfb6d6fedbdf9b65349f7f0ba8480376858c84faa8ee3d4d4b97b3"
  ],
  "reference_calibration": [
    "scripts/resume_20261126/fixed_fejer_reference_calibration.py",
    "fe36240c08ad32c4d4d665a387c70aaf02c0392419a51eef01e072081945e95c"
  ],
  "frame_C1": [
    "scripts/resume_20261126/fixed_fejer_normal_frame_c1.py",
    "1830c1d8e69e0e12d4b9d8af9f194d234ef3437cba546200738a1592a77aa0ca"
  ],
  "envelope_memory": [
    "scripts/resume_20261126/complete_material_envelope_memory.py",
    "c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152"
  ],
  "envelope_rows": [
    "scripts/resume_20261126/complete_material_envelope_rows.py",
    "729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7"
  ],
  "stage_matrices": [
    "scripts/resume_20261126/fixed_fejer_detached_stage_matrices.py",
    "7aabf3ef5857dbdbbf9832b8bb4ca378faa7e06514a21b48f83649d6df7cb0d7"
  ],
  "envelope_transfer": [
    "scripts/resume_20261126/transfer_fixed_fejer_material_envelope_memory.py",
    "af35c30e4774987d8f71bc6d05c1942db66a9f7889127c19948b119dee9a1566"
  ],
  "envelope_parent_reader": [
    "scripts/resume_20261126/read_reference_centred_c1_material_envelope_so3_report.py",
    "104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7"
  ],
  "envelope_parent_driver": [
    "scripts/resume_20261126/fullclosed_reference_centred_c1_material_envelope_so3_qp.py",
    "cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5"
  ],
  "envelope_parent_endpoint": [
    "scripts/resume_20261126/so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py",
    "a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd"
  ],
  "envelope_parent_calibration": [
    "scripts/resume_20261126/reference_centred_c1_smooth_triangle_calibration.py",
    "3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991"
  ],
  "envelope_parent_geometry": [
    "scripts/resume_20261126/so3_reference_centred_c1_material_envelope_geometry.py",
    "bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f"
  ],
  "adjacent_matrices": [
    "scripts/resume_20261126/fixed_fejer_adjacent_normal_matrices.py",
    "257e5e44d38dffb82925a410c42e51f084cf7821a398b9928e543088a3f234c0"
  ],
  "independent_envelope_memory": [
    "scripts/resume_20261126/complete_fixed_fejer_material_envelope_memory.py",
    "9f268e066274eff19ee2635124a8addf9c92eabf6d7177249f4ac4782c88a39a"
  ],
  "independent_input_projection_producer": [
    "scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py",
    "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"
  ],
  "analytic_frame": [
    "scripts/resume_20261126/fixed_fejer_analytic_normal_frame.py",
    "75db2f20039b66a2784a922bf062e792328c0153fb0458c16acef92e0ab7e38c"
  ],
  "frame_parent_driver": [
    "scripts/resume_20261126/fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py",
    "0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51"
  ],
  "frame_parent_reader": [
    "scripts/resume_20261126/read_reference_centred_analytic_j3_material_envelope_so3_report.py",
    "c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e"
  ],
  "frame_parent_endpoint": [
    "scripts/resume_20261126/so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py",
    "04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e"
  ],
  "frame_parent_calibration": [
    "scripts/resume_20261126/reference_centred_analytic_j3_smooth_triangle_calibration.py",
    "4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d"
  ],
  "frame_parent_J3": [
    "scripts/resume_20261126/analytic_normal_stage_jacobian.py",
    "64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d"
  ],
  "frame_parent_C1": [
    "scripts/resume_20261126/analytic_j3_normal_frame_c1_reuse.py",
    "8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8"
  ],
  "frame_parent_stage_matrices": [
    "scripts/resume_20261126/analytic_j3_detached_normal_stage_matrix_reuse.py",
    "5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1"
  ],
  "frame_parent_adjacent_matrices": [
    "scripts/resume_20261126/analytic_j3_adjacent_normal_frame_matrices.py",
    "8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787"
  ],
  "actual_public_input_binding": [
    "scripts/resume_20261126/fixed_fejer_reference_input_binding.py",
    "3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f"
  ],
  "closure_values": [
    "scripts/resume_20261126/fixed_fejer_immutable_closure_values.py",
    "01ca74a9f00ac17ef4452173b758d785c0e06869efa98980426f822d4beeb595"
  ],
  "closure_parent_analytic_J3": [
    "scripts/resume_20261126/analytic_frame_local_stage_jacobian.py",
    "894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866"
  ],
  "closure_parent_analytic_frame": [
    "scripts/resume_20261126/analytic_normal_frame_jets.py",
    "4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8"
  ],
  "closure_parent_frame_C1": [
    "scripts/resume_20261126/analytic_frame_c1_reuse.py",
    "f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb"
  ],
  "closure_parent_stage_matrices": [
    "scripts/resume_20261126/analytic_frame_detached_normal_stage_matrix_reuse.py",
    "fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255"
  ],
  "closure_parent_adjacent_matrices": [
    "scripts/resume_20261126/analytic_frame_adjacent_normal_matrices.py",
    "3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695"
  ],
  "closure_parent_reference_calibration": [
    "scripts/resume_20261126/reference_centred_analytic_frame_smooth_triangle_calibration.py",
    "fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0"
  ],
  "closure_parent_endpoint": [
    "scripts/resume_20261126/so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py",
    "3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc"
  ],
  "closure_parent_root_packets": [
    "scripts/resume_20261126/immutable_analytic_frame_normal_root_packets.py",
    "094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0"
  ],
  "closure_parent_analytic_J3_binding": [
    "scripts/resume_20261126/run09_public_reference_analytic_frame_binding.py",
    "15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592"
  ],
  "closure_parent_geometry": [
    "scripts/resume_20261126/so3_run09_public_reference_analytic_frame_geometry_v2.py",
    "e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13"
  ],
  "closure_parent_envelope_transfer": [
    "scripts/resume_20261126/transfer_run09_public_reference_analytic_frame_memory.py",
    "6deeeaa1dcbbb0fbfd968d0b31443798909536a55a7ea498f661e08496a27707"
  ],
  "closure_parent_driver": [
    "scripts/resume_20261126/fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py",
    "ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5"
  ],
  "closure_parent_reader": [
    "scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py",
    "aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32"
  ],
  "closure_parent_independent_envelope_memory": [
    "scripts/resume_20261126/complete_material_envelope_memory_public_reference.py",
    "2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb"
  ],
  "closure_parent_independent_input_projection_producer": [
    "scripts/resume_20261126/freeze_run09_public_reference_and_restore_run05_carrier.py",
    "9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18"
  ],
  "closure_parent_actual_public_input_binding": [
    "scripts/resume_20261126/actual_public_reference_input_binding.py",
    "306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a"
  ],
  "immutable_point_parent_closure_values": [
    "scripts/resume_20261126/same_chain_detached_closure_values.py",
    "e1af4fc8cfecbd30ab5cf9f7ded31d6a7a8d11385a8558cc76cbb8a8b1851e9e"
  ],
  "immutable_point_parent_analytic_J3": [
    "scripts/resume_20261126/analytic_local_stage_jacobian_closure_values.py",
    "9646c1cb1e239f4625dfaa0f13e0d0776dfd9684401789a089326e177c02a5aa"
  ],
  "immutable_point_parent_analytic_frame": [
    "scripts/resume_20261126/analytic_normal_frame_jets_closure_values.py",
    "8239fc8f3588afd4f93ba10368c599a85652d3b350a088b1397731c196258598"
  ],
  "immutable_point_parent_frame_C1": [
    "scripts/resume_20261126/normal_frame_c1_closure_values.py",
    "1f80ce726f9cf9424740331eb54a5cafa86a058ca2b048ee5fb6add5fc371caa"
  ],
  "immutable_point_parent_stage_matrices": [
    "scripts/resume_20261126/detached_stage_matrices_closure_values.py",
    "bf80cc8bbcf442d07d0e9225e1fbf703be4c40b951f10fb20e861e1ec7497c45"
  ],
  "immutable_point_parent_adjacent_matrices": [
    "scripts/resume_20261126/adjacent_normal_matrices_closure_values.py",
    "6efb1b4de61635bb4121b2cc05daf4b817ecfb772f302568e2a570b7fa16b650"
  ],
  "immutable_point_parent_reference_calibration": [
    "scripts/resume_20261126/reference_centred_closure_values_calibration.py",
    "b59776d52653f036590b619124579a20400d3bb7a4de8117d3221ca32bec144f"
  ],
  "immutable_point_parent_endpoint": [
    "scripts/resume_20261126/so3_reference_centred_closure_values_normal_lift_operator.py",
    "6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4"
  ],
  "immutable_point_parent_root_packets": [
    "scripts/resume_20261126/immutable_closure_values_normal_root_packets.py",
    "31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805"
  ],
  "immutable_point_parent_binding": [
    "scripts/resume_20261126/run10_detached_closure_value_binding.py",
    "dc3b40645eb47f924392a703eb65e3fda982f43804b1861f89da1c038e9140a1"
  ],
  "immutable_point_parent_geometry": [
    "scripts/resume_20261126/so3_run10_detached_closure_geometry.py",
    "6c676d4302f4271310ffca899ca8820fe43f2d792ee9a634747f25eecf9f6528"
  ],
  "immutable_point_parent_envelope_transfer": [
    "scripts/resume_20261126/transfer_run10_detached_closure_memory.py",
    "eca323b12ff941736798f7e40021f78b92e1b23cee8a7edcdcc5e3f6db7508fe"
  ],
  "immutable_point_parent_driver": [
    "scripts/resume_20261126/fullclosed_run10_detached_closure_so3_qp.py",
    "c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1"
  ],
  "immutable_point_parent_reader": [
    "scripts/resume_20261126/read_run10_detached_closure_so3_report.py",
    "2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e"
  ],
  "immutable_point_parent_launcher": [
    "scripts/resume_20261126/launch_run10_detached_closure_actions.py",
    "22069c4bb56a4ca4820b3f608cf720a36b036534e6b1e90b5f467f8eed21e604"
  ],
  "fixed_fejer_previous_closure_values": [
    "scripts/resume_20261126/immutable_point_detached_closure_values.py",
    "2543ee5db3ff15108fbdb4e340dad84301b94eecb773f757da4126ab86778cfb"
  ],
  "fixed_fejer_previous_analytic_J3": [
    "scripts/resume_20261126/analytic_local_stage_jacobian_immutable_point.py",
    "21a929c14abfe5e66ca56c232d31b77d8f8e3a5e969d796c4601d1a1e1374024"
  ],
  "fixed_fejer_previous_analytic_frame": [
    "scripts/resume_20261126/analytic_normal_frame_jets_immutable_point.py",
    "4e9b027b365752878069fa29671f8f549fa4cd9be478487b12ceeb64a908f8fa"
  ],
  "fixed_fejer_previous_frame_C1": [
    "scripts/resume_20261126/normal_frame_c1_immutable_point.py",
    "53b5bc456cb3f62c6a25d329de54920253d9193168ef3fb761198ff61fa0822d"
  ],
  "fixed_fejer_previous_stage_matrices": [
    "scripts/resume_20261126/detached_stage_matrices_immutable_point.py",
    "a41872f7563683b28d34cb9da35d7fc3bd0879fb5a8d1d183230a518f6b8f052"
  ],
  "fixed_fejer_previous_adjacent_matrices": [
    "scripts/resume_20261126/adjacent_normal_matrices_immutable_point.py",
    "ab944e9c9af4b84a65d201a6cc997669a8f274077fc7e1f69ee35b268380bb59"
  ],
  "fixed_fejer_previous_reference_calibration": [
    "scripts/resume_20261126/reference_centred_immutable_point_calibration.py",
    "794275121ee8d2f79972c5302012a10ba1fd8aa58fa5f67f05399825244fd238"
  ],
  "fixed_fejer_previous_endpoint": [
    "scripts/resume_20261126/so3_reference_centred_immutable_point_normal_lift_operator.py",
    "9bd394592f95668956c6718387b02d22d47c445b3f981f9101ae0e2c482594d6"
  ],
  "fixed_fejer_previous_root_packets": [
    "scripts/resume_20261126/immutable_point_normal_root_packets.py",
    "b4c41b2dc8754607441c30cdb3a34199d7e40f8b52fc5e4a8f5d653ea524eac8"
  ],
  "fixed_fejer_previous_reference": [
    "scripts/resume_20261126/so3_axisymmetric_reference.py",
    "4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3"
  ],
  "fixed_fejer_previous_seed_reference": [
    "scripts/resume_20261126/supported_smooth_triangle_meridian_reference.py",
    "0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b"
  ],
  "fixed_fejer_previous_meridian": [
    "scripts/resume_20261126/so3_supported_smooth_triangle_meridian_operator.py",
    "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865"
  ],
  "fixed_fejer_previous_new_moment_input": [
    "scripts/resume_20261126/supported_smooth_triangle_literal_zero_moment_input.py",
    "307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7"
  ],
  "fixed_fejer_previous_analytic_J3_binding": [
    "scripts/resume_20261126/run10_immutable_point_source_binding.py",
    "85f3007a6927968eb253eab168e9379f9a1f732caf5aa43b9f24776f39606d97"
  ],
  "fixed_fejer_previous_geometry": [
    "scripts/resume_20261126/so3_run10_immutable_point_geometry.py",
    "dbbd4601f4bbc0798759f3c63cd3caae3cfc19f1a62ec9dbd02cc6fbceb896ce"
  ],
  "fixed_fejer_previous_envelope_transfer": [
    "scripts/resume_20261126/transfer_run10_immutable_point_memory.py",
    "0007abf0b2814b09a3ecc30f621cbd8814a3d94528c753762aa7be5175d08486"
  ],
  "fixed_fejer_previous_independent_envelope_memory": [
    "scripts/resume_20261126/complete_material_envelope_memory_public_run10.py",
    "f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba"
  ],
  "fixed_fejer_previous_independent_input_projection_producer": [
    "scripts/resume_20261126/freeze_run10_public_reference_and_restore_run05_carrier.py",
    "fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a"
  ],
  "fixed_fejer_previous_actual_public_input_binding": [
    "scripts/resume_20261126/actual_public_run10_reference_input_binding.py",
    "9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209"
  ],
  "fixed_input_producer": [
    "scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py",
    "89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60"
  ]
};
const sha256=s=>crypto.createHash('sha256').update(s,'utf8').digest('hex');
const utf8=s=>Buffer.from(s,'utf8');
const hash=s=>({sha256:sha256(s),bytes:utf8(s).length});
function ex(t,n){const a=t.indexOf("def "+n+"(");if(a<0)throw Error("function absent "+n);let b=t.length;for(const mark of ["\ndef ","\nclass ","\nif __name__"]) {const p=t.indexOf(mark,a+4);if(p>=0)b=Math.min(b,p+1);}return t.slice(a,b);}
function buildCore(oldM,fixed,names,schemas,hash) {
 const outputs={};
 const begin=(p,r)=>({role:r,name:names[r],parent:{name:p.name,sha256:p.sha256,bytes:p.bytes,git_blob_sha:p.git_blob_sha},text:p.text,patches:[]});
 function patch(r,a,b,count){const n=r.text.split(a).length-1;if(n!==count)throw Error(r.name+" expected "+count+" found "+n+" "+a.slice(0,90));r.text=r.text.split(a).join(b);r.patches.push({old:a,new:b,count:n});}
 function done(r){Object.assign(r,hash(r.text));if(r.bytes>=100000)throw Error("source size");outputs[r.role]=r;return r;}
 const l=begin(oldM.frequency_layout,"frequency_layout");
 patch(l,"complete-SO3-M160-to-M320-frequency-inclusion-v1",schemas.layout,1);
 patch(l,"complete-R711-frequency-refined-frozen-reference-so3-meridian-with-core-lift-v1",schemas.base,1);done(l);
 const b=begin(oldM.meridian,"meridian");
 patch(b,"complete-R711-frequency-refined-frozen-reference-so3-meridian-with-core-lift-v1",schemas.base,1);
 patch(b,oldM.frequency_layout.sha256,l.sha256,1);
 patch(b,"0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b",fixed.seed_reference.sha256,1);
 patch(b,"4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3",fixed.reference.sha256,1);
 patch(b,"complete-supported-smooth-triangle-meridian-seed-reference-v1","complete-fixed-fejer-supported-smooth-triangle-meridian-seed-reference-v1",1);
 patch(b,"theta0(phi)=Theta_initial_warm_core(phi)","theta0(phi)=Theta_cbar(phi); predeclared RN-even64 Fejer B=1/4,n=7, not an optimized warm chart",1);done(b);
 const q=begin(fixed.new_moment_input,"new_moment_input");
 patch(q,"fixed-fejer-supported-reference-literal-zero-endpoint-Q-input-v1",schemas.Q,1);
 patch(q,"fixed-fejer-supported-reference-literal-two-bubble-endpoint-Q-v1",schemas.Qdefinition,1);
 patch(q,"complete-fixed-fejer-supported-smooth-triangle-so3-meridian-with-core-lift-v1",schemas.base,1);
 patch(q,fixed.meridian.sha256,b.sha256,1);
 patch(q,"if (base.get('M') != 160 or base.get('J') != 923","if (base.get('M') != 320 or base.get('current_M') != 320\n            or base.get('reference_M') != 160 or base.get('J') != 923",1);done(q);
 return outputs;
}

function buildFejerMLower(parents,m09,sha256,utf8,names,schema,base,baseschema,qsource,oldbase) {
 const out={},ops={},inputs={};
 const oldschema="complete-fixed-fejer-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1";
 const oldbaseschema="complete-fixed-fejer-supported-smooth-triangle-so3-meridian-with-core-lift-v1";
 function one(role,s,a,b) {
   const n=s.split(a).length-1;if(n!==1)throw Error(role+" expected one occurrence "+a.slice(0,100)+" got "+n);
   (ops[role]??=[]).push({kind:"replace",old:a,new:b,count:1});
   return s.replace(a,b);
 }
 function all(role,s,a,b){
   const n=s.split(a).length-1;if(n<1)throw Error(role+" missing "+a);
   (ops[role]??=[]).push({kind:"replace",old:a,new:b,count:n});
   return s.split(a).join(b);
 }
 function begin(role,source,key=role){
   inputs[role]={key,sha256:sha256(source),bytes:utf8(source).length};ops[role]=[];return source;
 }
 function save(role,s){if(utf8(s).length>=100000)throw Error("oversize "+role);out[role]={name:names[role],source:s,sha256:sha256(s),bytes:utf8(s).length};}
 const chart0=parents.endpoint.source.match(/    def _chart\(self, phi\):\n[\s\S]*?(?=\n    def )/)[0];
 const chart=chart0.replace("tensor(self.freq)","tensor(self.reference_freq)");
 if(chart===chart0)throw Error("missing reference/current chart split");
 let s=begin("closure_values",parents.closure_values.source);
 s=all("closure_values",s,oldschema,schema);s=all("closure_values",s,oldbase,base);
 let line=s.split("\n").find(x=>x.startsWith("DERIVED_METHOD_SOURCES = json.loads("));
 const arg=line.slice("DERIVED_METHOD_SOURCES = json.loads(".length,-1);
 const methods=JSON.parse(JSON.parse(arg)); if(methods._chart)throw Error("unexpected old chart override");
 methods._chart=chart.trimEnd()+"\n";
 s=one("closure_values",s,line,"DERIVED_METHOD_SOURCES = json.loads("+JSON.stringify(JSON.stringify(methods))+")");
 s=one("closure_values",s,"        base_source_sha256=BASE_SOURCE_SHA256,torch_version=TORCH_VERSION,",
 "        base_source_sha256=BASE_SOURCE_SHA256,torch_version=TORCH_VERSION,\n        frozen_reference_M=160,current_M=320,\n        material_chart_uses_frozen_reference_frequencies=True,");
 save("closure_values",s);
 for(const role of ["analytic_J3","analytic_frame","frame_C1","stage_matrices","adjacent_matrices"]){
   s=begin(role,parents[role].source);
   if(s.includes(oldschema))s=all(role,s,oldschema,schema);
   s=all(role,s,oldbase,base);
   for(const dep of ["closure_values","analytic_J3","analytic_frame","frame_C1","stage_matrices"]){
     if(out[dep]&&s.includes(parents[dep].record.sha256))s=all(role,s,parents[dep].record.sha256,out[dep].sha256);
   }
   save(role,s);
 }
 s=begin("reference_calibration",m09.reference_calibration.source,"M10:run10_frequency_immutable_point_calibration.py");
 s=one("reference_calibration",s,s.match(/^ENDPOINT_SCHEMA = .+$/m)[0],"ENDPOINT_SCHEMA = '"+schema+"'");
 s=one("reference_calibration",s,"41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2",base);
 s=one("reference_calibration",s,"complete-R711-frequency-refined-frozen-reference-so3-meridian-with-core-lift-v1",baseschema);
 s=one("reference_calibration",s,"0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b","ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a");
 save("reference_calibration",s);
 s=begin("endpoint",parents.endpoint.source);
 s=all("endpoint",s,oldschema,schema);s=all("endpoint",s,oldbase,base);
 s=all("endpoint",s,oldbaseschema,baseschema);
 s=all("endpoint",s,"ca4fef4066bfb6d6fedbdf9b65349f7f0ba8480376858c84faa8ee3d4d4b97b3",qsource);
 for(const [a,b] of [
 ["fixed-fejer-supported-reference-literal-zero-endpoint-Q-input-v1","fixed-fejer-frequency-refined-literal-zero-endpoint-Q-input-v1"],
 ["fixed-fejer-supported-reference-literal-two-bubble-endpoint-Q-v1","fixed-fejer-frequency-refined-literal-two-bubble-endpoint-Q-v1"]])
 {if(s.includes(a))s=all("endpoint",s,a,b);}
 for(const dep of ["closure_values","analytic_J3","analytic_frame","frame_C1","stage_matrices","adjacent_matrices","reference_calibration"]){
   s=all("endpoint",s,parents[dep].record.sha256,out[dep].sha256);
 }
 s=one("endpoint",s,chart0,chart);save("endpoint",s);
 s=begin("root_packets",parents.root_packets.source);
 const spec="    '"+out.endpoint.sha256+"': dict(schema='"+schema+"',\n"+
 "        base='"+base+"',\n"+
 "        adjacent='"+out.adjacent_matrices.sha256+"',calibration='"+out.reference_calibration.sha256+"',\n"+
 "        analytic='"+out.analytic_J3.sha256+"',analytic_frame='"+out.analytic_frame.sha256+"',\n"+
 "        closure_values='"+out.closure_values.sha256+"'),\n";
 s=one("root_packets",s,"NORMALS = {\n","NORMALS = {\n"+spec);save("root_packets",s);
 return {schema,base_schema:baseschema,outputs:out,patches:ops,inputs};
}




function buildBinding(parent,oldM,outputs,names,schemas,hash,ex){
 const r={role:"analytic_J3_binding",name:names.analytic_J3_binding,parent:{name:parent.name,sha256:parent.sha256,bytes:parent.bytes,git_blob_sha:parent.git_blob_sha},text:parent.text,patches:[]};
 function patch(a,b,count=1){const n=r.text.split(a).length-1;if(n!==count)throw Error("binding expected "+count+" found "+n+" "+a.slice(0,100));r.text=r.text.split(a).join(b);r.patches.push({old:a,new:b,count:n});}
 function line(n,value){const a=r.text.split("\n").find(s=>s.startsWith(n+" = "));if(!a)throw Error("missing "+n);patch(a,n+" = "+JSON.stringify(value));}
 line("SCHEMA",schemas.binding);line("OPERATOR_SCHEMA",schemas.endpoint);line("ROOT_SNAPSHOT_SCHEMA",schemas.snapshot);
 line("BASE_SOURCE_SHA256",outputs.meridian.sha256);
 const roles=JSON.parse(r.text.split("\n").find(x=>x.startsWith("SOURCE_BINDINGS = ")).slice(18));
 for(const role of Object.keys(roles))roles[role]=[outputs[role].name,outputs[role].sha256];
 line("SOURCE_BINDINGS",roles);
 patch("    policies=_policies(directory)\n","    _layout(directory).validate_base_model(model['base_complete_model'],expected_base_source_sha256=BASE_SOURCE_SHA256)\n    policies=_policies(directory)\n");
 let block=oldM.text.slice(oldM.text.indexOf("IMMUTABLE_POINT_PARENT_DRIVER ="),oldM.text.indexOf("def read_actual("));
 const substitutions=[
 ["fullclosed_run10_detached_closure_so3_qp.py","fullclosed_fixed_fejer_immutable_point_so3_qp.py"],
 ["c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1","477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd"],
 ["run10_detached_closure_value_binding.py","fixed_fejer_complete_source_binding.py"],
 ["dc3b40645eb47f924392a703eb65e3fda982f43804b1861f89da1c038e9140a1","3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88"],
 ["6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4","1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778"],
 ["complete-R711-reference-centred-detached-closure-values-analytic-frame-J3-normal-layer-v1","complete-fixed-fejer-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1"],
 ["immutable_point_parent_driver","frequency_parent_driver"],
 ["immutable_point_parent_binding","frequency_parent_binding"],
 ["len(old_pins)!=75","len(old_pins)!=110"],
 ["all 75 complete source roles of the original run10 parent","all 110 complete source roles of the actual Fejer M160 parent"],
 ["actual c3dc run10 M160 source-bound field","actual 477499 Fejer M160 source-bound field"],
 ["actual original run10 driver","actual original Fejer M160 driver"],
 ["original complete run10 model validator","original complete Fejer M160 model validator"],
 ["so3_frequency_refinement_layout.py",outputs.frequency_layout.name],
 ["ce188ae4bdf1ccecfbf9549897284e8dc44f4722e04e974c7a0cd045c78a3a27",outputs.frequency_layout.sha256],
 ["supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1","fixed-fejer-supported-reference-literal-two-bubble-endpoint-Q-v1"],
 ["frequency-refined-fixed-fejer-supported-reference-literal-two-bubble-endpoint-Q-v1",schemas.Qdefinition],
 ["actual-actual_run10-M320-complete-refinement-binding-v1","actual-fixed-fejer-M320-complete-refinement-binding-v1"],
 ["_actual_run10_frequency_binding_","_actual_fixed_fejer_frequency_binding_"]
 ];
 for(const [a,b]of substitutions){if(!block.includes(a))throw Error("frequency block missing "+a);block=block.split(a).join(b);}
 const start=r.text.indexOf("IMMUTABLE_POINT_PARENT_DRIVER ="),end=r.text.indexOf("def read_actual(");
 patch(r.text.slice(start,end),block);
 patch("        analytic_normal_frame=frame,detached_closure_value_reuse=closure,\n","        analytic_normal_frame=frame,detached_closure_value_reuse=closure,\n        frequency_refinement=frequency_refinement_binding(report,roles=roles,source_directory=source_directory),\n");
 Object.assign(r,hash(r.text));if(r.bytes>=100000)throw Error("binding size");
 return r;
}

function buildTransfer(oldM,current,outputs,names,schemas,hash,ex){
 const r={role:"envelope_transfer",name:names.envelope_transfer,parent:{name:oldM.name,sha256:oldM.sha256,bytes:oldM.bytes,git_blob_sha:oldM.git_blob_sha},text:oldM.text,patches:[]};
 function patch(a,b,count=1){const n=r.text.split(a).length-1;if(n!==count)throw Error("transfer expected "+count+" found "+n+" "+a.slice(0,95));r.text=r.text.split(a).join(b);r.patches.push({old:a,new:b,count:n});}
 function all(a,b){const n=r.text.split(a).length-1;if(!n)throw Error("transfer missing "+a);patch(a,b,n);}
 function line(n,v){const a=r.text.split("\n").find(x=>x.startsWith(n+" = "));if(!a)throw Error(n);patch(a,n+" = "+JSON.stringify(v));}
 line("SCHEMA",schemas.transfer);
 line("ANALYTIC_BINDING_SOURCE_SHA256",outputs.analytic_J3_binding.sha256);
 line("CURRENT_MEMORY_SOURCE_SHA256","9f268e066274eff19ee2635124a8addf9c92eabf6d7177249f4ac4782c88a39a");
 line("LAYOUT_SOURCE_SHA256",outputs.frequency_layout.sha256);
 const first=r.text.indexOf("PARENT_FAMILIES ="),end=r.text.indexOf("def _parent_family(");
 let families=current.text.slice(current.text.indexOf("PARENT_FAMILIES ="),current.text.indexOf("def _parent_family("));
 families+="PARENT_FAMILIES['477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd'] = dict(\n"+
 "    report_schema='complete-fixed-fejer-immutable-point-material-envelope-SO3-QP-v1',\n"+
 "    reader_sha256='274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b',\n"+
 "    reader_relative='scripts/resume_20261126/read_fixed_fejer_immutable_point_so3_report.py',\n"+
 "    operator_sha256='1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778',\n"+
 "    operator_schema='complete-fixed-fejer-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1',\n"+
 "    memory_sha256=CURRENT_MEMORY_SOURCE_SHA256)\n\n";
 patch(r.text.slice(first,end),families);
 let def=ex(current.text,"definition");
 def=def.replace("        historical_parent_families_are_provenance_not_current_target_parents=True,",
 "        pre_fejer_parent_families_are_provenance_not_current_target_parents=True,\n"+
 "        complete_actual_fejer_M160_parent_and_all_thirteen_final_members_supported=True,\n"+
 "        frequency_layout_source_sha256=LAYOUT_SOURCE_SHA256,reference_M=160,current_M=320,J=923,full_N=2048,\n"+
 "        complete_fixed_fejer_target_reference_seed_mesh_observer_Q_gamma_partition_retained=True,\n"+
 "        three_unequal_rotation_blocks_copied_with_explicit_new_zero_modes=True,\n"+
 "        full_actual_fixed_input_target_and_mathematical_recipe_validation_retained=True,");
 def=def.replace("changed_model_fields='new declared mathematical chart and deterministic mesh; no previous-target model or field equivalence asserted'",
 "changed_model_fields='only current M160-to-M320 layout, explicit frozen-point coordinate identities and whole bound source policies; same complete fixed Fejer target and unchanged radial/angular observer'");
 def=def.replace("        explicit_old_complete_final_free_variable_words_supported=False,",
 "        explicit_old_pre_fejer_complete_final_free_variable_words_supported=False,\n"+
 "        explicit_same_target_fejer_M160_complete_final_free_variable_words_supported=True,");
 patch(ex(r.text,"definition"),def);
 all("run10_frequency_immutable_point_source_binding.py",names.analytic_J3_binding);
 all("so3_frequency_refinement_layout.py",names.frequency_layout);
 all("complete_material_envelope_memory_public_run10.py","complete_fixed_fejer_material_envelope_memory.py");
 all("R690-independent-axisymmetric-SO3-preparation-v1","R690-fixed-fejer-axisymmetric-SO3-preparation-v1");
 all("actual-run10-M320-input-point-and-fixed-reference-v1","actual-fixed-fejer-M320-input-point-and-fixed-reference-v1");
 const oldLoad=ex(r.text,"load_memory"),currentLoad=ex(current.text,"load_memory");
 let newBranch=currentLoad.slice(currentLoad.indexOf("    if independent:\n        target="),currentLoad.indexOf("    initial_rows ="));
 newBranch=newBranch.replace("explicit-new-fixed-fejer-complete-material-envelope-origin-v1","explicit-fixed-fejer-frequency-inclusion-origin-v1")
  .replace("            mathematical_target_identity_sha256=target['mathematical_target_identity_sha256'],",
 "            mathematical_target_identity_sha256=target['mathematical_target_identity_sha256'],\n"+
 "            same_declared_fejer_mathematical_target=True,\n"+
 "            current_frequency_refinement_changes_fixed_target=False,\n"+
 "            historical_sameg_false_flags_refer_to_pre_fejer_targets=True,");
 const oldBranch=oldLoad.slice(oldLoad.indexOf("    if independent:\n        target="),oldLoad.indexOf("    initial_rows ="));
 patch(oldBranch,newBranch);
 const oldValid=ex(r.text,"validate_metadata"),currentValid=ex(current.text,"validate_metadata");
 let validation=currentValid.slice(currentValid.indexOf("    if branch is not None:"),currentValid.indexOf("    elif not parents"));
 validation=validation.replace("explicit-new-fixed-fejer-complete-material-envelope-origin-v1","explicit-fixed-fejer-frequency-inclusion-origin-v1")
  .replace("                or branch.get('mathematical_target_identity_sha256')!=target['mathematical_target_identity_sha256']",
 "                or branch.get('mathematical_target_identity_sha256')!=target['mathematical_target_identity_sha256']\n"+
 "                or branch.get('same_declared_fejer_mathematical_target') is not True\n"+
 "                or branch.get('current_frequency_refinement_changes_fixed_target') is not False\n"+
 "                or branch.get('historical_sameg_false_flags_refer_to_pre_fejer_targets') is not True");
 const oldValidation=oldValid.slice(oldValid.indexOf("    if branch is not None:"),oldValid.indexOf("    elif not parents"));
 patch(oldValidation,validation);
 const doc=r.text.slice(0,r.text.indexOf("import ast"));
 patch(doc,'#!/usr/bin/env python3\n"""Complete same-Fejer M160 to M320 words, addresses and typed-history transfer.\n\nOnly an actually returned complete 477499/274d Fejer parent can supply its\nthirteen-member final and complete typed/protected discoveries. Independent\nreference-zero inclusion and same-source restart are distinct explicit modes.\nThe older pre-Fejer targets remain source-bound unresolved provenance only.\nNo old field values, selected roots, norm, acceptance or certificate transfer.\nAll original history/role inputs are reread; no ancestry or typed row is capped.\n"""\n');
 Object.assign(r,hash(r.text));if(r.bytes>=100000)throw Error("transfer source size");
 return r;
}

function buildFejerMUpper(parents,sourceRoles,lower,binding,transfer,shared,sha256,utf8,names,schemas) {
 const outputs={},ops={};
 const roles={...lower.outputs,analytic_J3_binding:binding,envelope_transfer:transfer,...shared};
 const baseSchema=lower.base_schema;
 const oldschema="complete-fixed-fejer-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1";
 const snapshot=schemas.snapshot;
 const driverSchema=schemas.driver;
 function one(r,s,a,b){const n=s.split(a).length-1;if(n!==1)throw Error(r+" "+n+" "+a.slice(0,100));(ops[r]??=[]).push({kind:"replace",old:a,new:b,count:n});return s.replace(a,b);}
 function all(r,s,a,b){const n=s.split(a).length-1;if(n<1)throw Error(r+" missing "+a);(ops[r]??=[]).push({kind:"replace",old:a,new:b,count:n});return s.split(a).join(b);}
 function assign(r,s,k,v){const m=s.match(new RegExp("^"+k+" = .+$","m"));if(!m)throw Error(k);return one(r,s,m[0],k+" = '"+v+"'");}
 function save(role,name,source){if(utf8(source).length>=100000)throw Error("oversize "+role);outputs[role]={name,source,bytes:utf8(source).length,sha256:sha256(source)};}
 const common=[
 [oldschema,lower.schema],
 ["complete-fixed-fejer-supported-smooth-triangle-so3-meridian-with-core-lift-v1",baseSchema],
 ["fixed-fejer-supported-reference-literal-zero-endpoint-Q-input-v1",schemas.Q],
 ["fixed-fejer-supported-reference-literal-two-bubble-endpoint-Q-v1",schemas.Qdefinition],
 ["actual-fixed-fejer-immutable-point-current-point-snapshot-v1",snapshot]
 ];
 for(const[r,v]of Object.entries(roles)){
    if(sourceRoles[r])common.push([sourceRoles[r][1],v.sha256],[sourceRoles[r][0].split("/").pop(),v.name]);
 }
 function replaceKnown(role,s){for(const[a,b]of common)if(s.includes(a)&&a!==b)s=all(role,s,a,b);return s;}
 let geo=replaceKnown("geometry",parents.geometry.source);
 geo=assign("geometry",geo,"SCHEMA","complete-fixed-fejer-frequency-envelope-world-geometry-v1");
 save("geometry",names.geometry,geo);roles.geometry=outputs.geometry;
 common.push([sourceRoles.geometry[1],outputs.geometry.sha256],[sourceRoles.geometry[0].split("/").pop(),outputs.geometry.name]);
 const pins=JSON.parse(JSON.stringify(sourceRoles));
 for(const[r,v]of Object.entries(roles)){
   if(sourceRoles[r]){
     if(pins["frequency_parent_"+r])throw Error("alias collision "+r);
     pins["frequency_parent_"+r]=sourceRoles[r];
   }
   pins[r]=["scripts/resume_20261126/"+v.name,v.sha256];
 }
 pins.frequency_parent_driver=["scripts/resume_20261126/"+parents.driver.record.name,parents.driver.record.sha256];
 pins.frequency_parent_reader=["scripts/resume_20261126/"+parents.reader.record.name,parents.reader.record.sha256];
 pins.frequency_parent_binding=["scripts/resume_20261126/"+parents.binding.record.name,parents.binding.record.sha256];
 const pretty=ps=>"{"+Object.entries(ps).map(([k,v])=>JSON.stringify(k)+": ("+JSON.stringify(v[0])+", "+JSON.stringify(v[1])+")").join(", ")+"}";
 let d=parents.driver.source;ops.driver=[];
 const tableStart=d.indexOf("SOURCE_PINS = "),tableEnd=d.indexOf("\n\nROOT_SNAPSHOT_SCHEMA",tableStart);
 if(tableStart<0||tableEnd<tableStart)throw Error("table boundary");
 // Preserve every old record before substituting current source roles.
 const placeholder="SOURCE_PINS = __COMPLETE_SOURCE_TABLE_PENDING__";
 d=one("driver",d,d.slice(tableStart,tableEnd),placeholder);
 d=replaceKnown("driver",d);
 d=one("driver",d,placeholder,"SOURCE_PINS = "+pretty(pins));
 d=assign("driver",d,"SCHEMA",driverSchema);
 const addArg="    p.add_argument('--angles', type=int, default=2048)";
 const newArg=addArg+"\n    p.add_argument('--current-modes', type=int, default=320)";
 const check="    if (a.material_envelope_binding is None or a.normal_stages!=32 or a.integration_order!=8\n            or a.current_modes!=320 or a.angles!=2048):\n        raise ValueError('M-only inclusion retains the complete actual target, all 32 stages, N2048 and eight radial Gauss nodes')\n";
 d=one("driver",d,addArg,newArg);
 d=one("driver",d,"    a.manifest = [path.resolve() for path in a.manifest]",check+"    a.manifest = [path.resolve() for path in a.manifest]");
 d=one("driver",d,"    independent_envelope_memory = load('_so3_complete_current_restorer_envelope_memory',paths['independent_envelope_memory'])",
 "    independent_envelope_memory = load('_so3_complete_current_restorer_envelope_memory',paths['independent_envelope_memory'])\n    frequency_layout = load('_complete_actual_frequency_layout',paths['frequency_layout'])");
 d=one("driver",d,"seed_parameters=seed_parameters, seed_mean_kernel_module=seed_mean)",
 "seed_parameters=seed_parameters, seed_mean_kernel_module=seed_mean,\n        current_modes=args.current_modes,frequency_layout_module=frequency_layout)");
 d=one("driver",d,"    if prior_final_point is not None:\n        x = prior_final_point\n",
 "    if prior_final_point is not None:\n        x = prior_final_point\n    frequency_record=envelope_transfer.frequency_initial_record(args,q,x,\n        transfer_record=envelope_transfer_record,seed_record=prior_final_seed)\n");
 d=one("driver",d,"        representation=q.model, coordinate_norm=coordinates.record,",
 "        representation=q.model, coordinate_norm=coordinates.record,\n        frequency_refinement=frequency_record,reference_M=160,current_M=320,\n        frequency_layout_definition=base.frequency_layout_definition,\n        frequency_layout_identity_sha256=base.model['frequency_layout_identity_sha256'],\n        frequency_layout_source=file_record(paths['frequency_layout']),\n        radial_observation_refinement_performed=False,angular_observation_refinement_performed=False,\n        full_fixed_reference_target_unchanged=True,saved_parent_Phi_used_as_current_baseline=False,");
 const marker="    def save_report():";
 if(d.slice(d.indexOf(marker))!==parents.driver.source.slice(parents.driver.source.indexOf(marker)))throw Error("changed scientific suffix");
 save("driver",names.driver,d);
 let l=replaceKnown("launcher",parents.launcher.source);
 l=assign("launcher",l,"DRIVER_SHA",outputs.driver.sha256);
 l=all("launcher",l,parents.driver.record.name,outputs.driver.name);
 l=one("launcher",l,addArg,newArg);
 l=one("launcher",l,"    a.manifest = [path.resolve() for path in a.manifest]",check+"    a.manifest = [path.resolve() for path in a.manifest]");
 l=one("launcher",l,"        fixed_supported_unit_seed=True,",
 "        fixed_supported_unit_seed=True,reference_M=160,current_M=args.current_modes,\n        every_original_free_word_retained_with_correct_three_block_zero_inclusion=True,\n        original_reference_M160_chart_and_N2048_radial_observer_retained=True,");
 save("launcher",names.launcher,l);
 let r=replaceKnown("reader",parents.reader.source);
 r=assign("reader",r,"DRIVER_SHA",outputs.driver.sha256);
 r=assign("reader",r,"REPORT_SCHEMA",driverSchema);
 r=all("reader",r,parents.driver.record.name,outputs.driver.name);
 r=one("reader",r,"                    'all_original_outer_free_variables_and_norm_layout_unchanged'))",
 "                    'all_original_outer_free_variables_retained_and_new_modes_added',\n                    'frozen_reference_layout_unchanged','current_norm_layout_changed'))");
 r=one("reader",r,"schema='actual-fixed-fejer-immutable-point-envelope-SO3-readout-v1'",
 "schema='"+schemas.reader+"'");
 r=one("reader",r,"        material_envelope_transfer=transfer_binding,\n",
 "        material_envelope_transfer=transfer_binding,\n        frequency_refinement=report['frequency_refinement'],\n        frequency_refinement_binding=extra['analytic_J3_binding']['frequency_refinement'],\n        reference_M=report['reference_M'],current_M=report['current_M'],\n        frequency_layout_identity_sha256=report['frequency_layout_identity_sha256'],\n");
 save("reader",names.reader,r);
 return {outputs,patches:ops,pins,driverSchema,snapshot,scientific_suffix_sha256:sha256(d.slice(d.indexOf(marker))),scientific_suffix_bytes:utf8(d.slice(d.indexOf(marker))).length};
}



function reproduceAll(inputs,names,schemas,sourceRoles,sha256,utf8,hash,ex){
 const core=buildCore(inputs.oldM,inputs.fixed,names,schemas,hash);
 const adapt=group=>Object.fromEntries(Object.entries(group).map(([k,r])=>[k,{source:r.text,record:r}]));
 const lower=buildFejerMLower(adapt(inputs.lower),adapt(inputs.oldM),sha256,utf8,names,schemas.endpoint,
   core.meridian.sha256,schemas.base,core.new_moment_input.sha256,inputs.fixed.meridian.sha256);
 const all={...core};
 for(const[role,r]of Object.entries(lower.outputs))all[role]={...r,text:r.source,role,
   parent:role==='reference_calibration'?inputs.oldM.reference_calibration:inputs.lower[role],patches:lower.patches[role]};
 const binding=buildBinding(inputs.upper.binding,inputs.oldM.analytic_J3_binding,all,names,schemas,hash,ex);
 all.analytic_J3_binding=binding;
 const transfer=buildTransfer(inputs.oldM.envelope_transfer,inputs.upper.transfer,all,names,schemas,hash,ex);
 all.envelope_transfer=transfer;
 const upper=buildFejerMUpper(adapt(inputs.upper),sourceRoles,lower,binding,transfer,{meridian:core.meridian,new_moment_input:core.new_moment_input,frequency_layout:core.frequency_layout},sha256,utf8,names,schemas);
 for(const[role,r]of Object.entries(upper.outputs))all[role]={...r,text:r.source,role,parent:inputs.upper[role],patches:upper.patches[role]};
 if(Object.keys(all).length!==18||Object.keys(upper.pins).length!==128)throw Error('Complete eighteen sources / 128 role table required');
 for(const pair of Object.values(sourceRoles)){
  if(!Object.values(upper.pins).some(x=>JSON.stringify(x)===JSON.stringify(pair)))
   throw Error('Lost original full parent source record '+pair[0]);
 }
 for(const r of Object.values(all)){
  if(r.bytes!==utf8(r.text).length||r.sha256!==sha256(r.text)||r.bytes>=100000)throw Error('Whole output identity '+r.name);
 }
 return {outputs:all,pins:upper.pins,scientific_suffix_bytes:upper.scientific_suffix_bytes,
  scientific_suffix_sha256:upper.scientific_suffix_sha256};
}
function readFull(directory,record){
 const file=path.join(directory,record.name),raw=fs.readFileSync(file),text=raw.toString('utf8');
 if(!Buffer.from(text,'utf8').equals(raw)||raw.length!==record.bytes||sha256(text)!==record.sha256)
  throw Error('Complete original source differs: '+record.name);
 return {...record,text};
}
function inverseAll(inputs,result){
 const parents={frequency_layout:inputs.oldM.frequency_layout,meridian:inputs.oldM.meridian,
  new_moment_input:inputs.fixed.new_moment_input,...inputs.lower,
  reference_calibration:inputs.oldM.reference_calibration,analytic_J3_binding:inputs.upper.binding,
  envelope_transfer:inputs.oldM.envelope_transfer,geometry:inputs.upper.geometry,driver:inputs.upper.driver,
  launcher:inputs.upper.launcher,reader:inputs.upper.reader};
 for(const[role,r]of Object.entries(result.outputs)){
  let text=r.text;
  for(const change of r.patches.slice().reverse()){
   const count=text.split(change.new).length-1;
   if(count!==change.count)throw Error('Inverse source occurrence differs: '+role);
   text=text.split(change.new).join(change.old);
  }
  if(text!==parents[role].text)throw Error('Complete inverse source differs: '+role);
 }
}
function main(argv){
 const options={};
 for(let i=0;i<argv.length;i+=2){
  const key=argv[i];
  if(!['--source-directory','--generated-directory'].includes(key)||argv[i+1]===undefined||options[key])
   throw Error('Use each declared directory argument exactly once');
  options[key]=path.resolve(argv[i+1]);
 }
 const directory=options['--source-directory'],out=options['--generated-directory'];
 if(!directory||!out||out===directory||out.startsWith(directory+path.sep)||fs.existsSync(out))
  throw Error('Preserve the original sources and choose a separate fresh output directory');
 const inputs=Object.fromEntries(Object.entries(INPUTS).map(([group,records])=>[group,
  Object.fromEntries(Object.entries(records).map(([role,record])=>[role,readFull(directory,record)]))]));
 const result=reproduceAll(inputs,NAMES,SCHEMAS,ORIGINAL_SOURCE_ROLES,sha256,utf8,hash,ex);
 inverseAll(inputs,result);
 for(const[role,r]of Object.entries(result.outputs)){
  const wanted=EXPECTED[role];
  if(r.name!==wanted.name||r.bytes!==wanted.bytes||r.sha256!==wanted.sha256)
   throw Error('Complete generated source differs: '+role);
 }
 for(const records of Object.values(INPUTS))for(const record of Object.values(records))readFull(directory,record);
 fs.mkdirSync(out,{recursive:true});
 for(const r of Object.values(result.outputs))fs.writeFileSync(path.join(out,r.name),r.text,{encoding:'utf8',flag:'wx'});
 console.log(JSON.stringify({complete:true,complete_sources:18,complete_source_roles:128,
  original_Fejer_parent_source_roles_retained:110,all_whole_forward_and_inverse_texts_matched:true,
  scientific_suffix_bytes:result.scientific_suffix_bytes,scientific_suffix_sha256:result.scientific_suffix_sha256,
  scientific_execution:false,Python_AST_or_compile:false,scientific_admission_gate:false}));
}
if(path.resolve(process.argv[1]||'')===fileURLToPath(import.meta.url))main(process.argv.slice(2));
