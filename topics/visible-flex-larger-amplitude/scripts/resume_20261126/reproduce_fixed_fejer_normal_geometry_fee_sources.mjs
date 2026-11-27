#!/usr/bin/env node
/**
 * Complete source-only construction of the fixed Fejer normal/geometry fee family.
 * Reads every complete pinned parent and direct new input source.
 * Writes six whole independent Python sources and both whole parameter plans.
 * No scientific module import, Python execution, field/root calculation or fixture.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const PARENTS = {
  "input": {
    "role": "input",
    "name": "run10_normal_packet_accurate_field_input.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_normal_packet_accurate_field_input.py",
    "bytes": 26356,
    "sha256": "852bc97e2990051c776dfbbb5d17de265fd3321758fcfa201fe3d6d2b3adbda8",
    "parent_name": "run09_normal_packet_accurate_field_input.py",
    "parent_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run09_normal_packet_accurate_field_input.py",
    "parent_bytes": 26431,
    "parent_sha256": "f0808c8563679a85969aaf56a3d4fa87de99b58635e5ad72853bc54f30c42f82",
    "git_blob_sha": "41c355a847ce078868f5c945532f016ada27fdb4"
  },
  "radial": {
    "role": "radial",
    "name": "run10_accurate_reference_control_radial_boxes.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_accurate_reference_control_radial_boxes.py",
    "bytes": 45392,
    "sha256": "fdddefd60f89c7d3cea4a59f8a3d1e1bd70764d53095907fbbc09f49f6fb0f3c",
    "parent_name": "run09_accurate_reference_control_radial_boxes.py",
    "parent_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run09_accurate_reference_control_radial_boxes.py",
    "parent_bytes": 45392,
    "parent_sha256": "0587d88cd46ea8379b7e250872ed1b34deb0452ab7d61ae230c284bac126d42b",
    "git_blob_sha": "03f8e7eacd00ade95e5cf2761fa31a40f77ae185"
  },
  "normal": {
    "role": "normal",
    "name": "run10_complete_normal_root_and_sixjet_fees.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_complete_normal_root_and_sixjet_fees.py",
    "bytes": 40280,
    "sha256": "0d6e4c109f75e621ebceb7c660b3f4d5a798c34b15b6d90e4004ef9d97c5ac83",
    "parent_name": "run09_complete_normal_root_and_sixjet_fees.py",
    "parent_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run09_complete_normal_root_and_sixjet_fees.py",
    "parent_bytes": 40268,
    "parent_sha256": "f5ecc7fb67d4c34d5c52cba16ba0cee94b8fb5872f14c67123a190b32c6450c1",
    "git_blob_sha": "01a0febb446e1b3953a021101cd0bc7e99126996"
  },
  "leaf": {
    "role": "leaf",
    "name": "run10_complete_physical_leaf_binding.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_complete_physical_leaf_binding.py",
    "bytes": 44539,
    "sha256": "cf571370b53288048db55dbcc0156a36de481a3fd91c9b3e0b85398905af39a5",
    "parent_name": "run09_complete_physical_leaf_binding.py",
    "parent_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run09_complete_physical_leaf_binding.py",
    "parent_bytes": 44591,
    "parent_sha256": "b71e2e87a910e9461f53a72977263dab0966e55ca1b5800927416343f6d7fb06",
    "git_blob_sha": "170a2ca0027745ba51118cd38c31ed825cf1d020"
  },
  "geometry": {
    "role": "geometry",
    "name": "run10_continuous_gram_curvature_support.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_continuous_gram_curvature_support.py",
    "bytes": 44853,
    "sha256": "e3178af9e5f2313fd3d1e4f649424a0ee9cdaa205964d4b470582572f5be5ed7",
    "parent_name": "run09_continuous_gram_curvature_support.py",
    "parent_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run09_continuous_gram_curvature_support.py",
    "parent_bytes": 44853,
    "parent_sha256": "91843225f698e7f6de945acc353f7a3733ac70719d93995099c2ac3e6186b40a",
    "git_blob_sha": "a8d6e90e58dc52c34ee0fe65cb1a01e0fdf1e158"
  },
  "bridge": {
    "role": "bridge",
    "name": "run10_complete_geometry_support_beta_bridge.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_complete_geometry_support_beta_bridge.py",
    "bytes": 20741,
    "sha256": "96d3467b15130c08948f52f701a80aeaf7a86337ebf3b9f1535b301e5677b8c9",
    "parent_name": "run09_complete_geometry_support_beta_bridge.py",
    "parent_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run09_complete_geometry_support_beta_bridge.py",
    "parent_bytes": 20741,
    "parent_sha256": "f14acf7bd84559b17de4359dc138ccd30b2b59ec26ec292336fd6b4686d99640",
    "git_blob_sha": "ad8173b880c65bf4729f306b697eadeb45a0c716"
  }
};
const INPUTS = {
  "actual_fixed_input_binding": {
    "role": "actual_fixed_input_binding",
    "name": "fixed_fejer_reference_input_binding.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_reference_input_binding.py",
    "bytes": 25672,
    "sha256": "3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f",
    "git_blob_sha": "5eab3f96cb8b1bc245f4de33dc2041cf25d22094"
  },
  "independent_envelope_memory": {
    "role": "independent_envelope_memory",
    "name": "complete_fixed_fejer_material_envelope_memory.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/complete_fixed_fejer_material_envelope_memory.py",
    "bytes": 45988,
    "sha256": "9f268e066274eff19ee2635124a8addf9c92eabf6d7177249f4ac4782c88a39a",
    "git_blob_sha": "d9a09a4e76efa1a4e55831fd566192d150ab67e1"
  },
  "binding": {
    "role": "binding",
    "name": "fixed_fejer_complete_source_binding.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_source_binding.py",
    "bytes": 32487,
    "sha256": "3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88",
    "git_blob_sha": "3073c9490a6bc6ce7dcf323f799ee8075f8bdd78"
  },
  "geometry": {
    "role": "geometry",
    "name": "so3_fixed_fejer_complete_geometry.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_complete_geometry.py",
    "bytes": 70709,
    "sha256": "bab4147bdd2f0d43a372ec1b04225fc66a05db2ccdc2f92968d3f70e2590bf26",
    "git_blob_sha": "f2b28d1bf2f994db9866cb58e74a522ff719358a"
  },
  "transfer": {
    "role": "transfer",
    "name": "transfer_fixed_fejer_material_envelope_memory.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/transfer_fixed_fejer_material_envelope_memory.py",
    "bytes": 66839,
    "sha256": "af35c30e4774987d8f71bc6d05c1942db66a9f7889127c19948b119dee9a1566",
    "git_blob_sha": "597f6529dea5ffeb32e8df43a1442f1f7994d48b"
  },
  "driver": {
    "role": "driver",
    "name": "fullclosed_fixed_fejer_immutable_point_so3_qp.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_immutable_point_so3_qp.py",
    "bytes": 91714,
    "sha256": "477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd",
    "git_blob_sha": "feb49510ddada8fb77d0bf9cf3cd78c1de50079d"
  },
  "launcher": {
    "role": "launcher",
    "name": "launch_fixed_fejer_immutable_point_actions.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_immutable_point_actions.py",
    "bytes": 21789,
    "sha256": "0c1ff0aa2de30fcd490efb4bddd1972613c0f0afb1257d1af0170ac7e60bb5bf",
    "git_blob_sha": "f5d337a07f6b1a0438f33cdaf6fc1845b30f8b84"
  },
  "reader": {
    "role": "reader",
    "name": "read_fixed_fejer_immutable_point_so3_report.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_immutable_point_so3_report.py",
    "bytes": 97987,
    "sha256": "274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b",
    "git_blob_sha": "feae7eaf1b29ea0ae2563c4fc0d8089794602fa3"
  },
  "closure_values": {
    "role": "closure_values",
    "name": "fixed_fejer_immutable_closure_values.py",
    "bytes": 59048,
    "sha256": "01ca74a9f00ac17ef4452173b758d785c0e06869efa98980426f822d4beeb595",
    "git_blob_sha": "f8d32aefb1c11152fd39ad1d5b6d160c60d864ef"
  },
  "analytic_J3": {
    "role": "analytic_J3",
    "name": "fixed_fejer_analytic_stage_jacobian.py",
    "bytes": 25739,
    "sha256": "7645268ee3538a43a4a04b73a5aee4fc5483b56962affeb0ba7e7f879d5d4a72",
    "git_blob_sha": "4fd818ed74a7043b955ef036a0cccccdb3cdc710"
  },
  "analytic_frame": {
    "role": "analytic_frame",
    "name": "fixed_fejer_analytic_normal_frame.py",
    "bytes": 47286,
    "sha256": "75db2f20039b66a2784a922bf062e792328c0153fb0458c16acef92e0ab7e38c",
    "git_blob_sha": "ee0e9799f87301d8a60d6da20cb68731d031cdb0"
  },
  "frame_C1": {
    "role": "frame_C1",
    "name": "fixed_fejer_normal_frame_c1.py",
    "bytes": 37361,
    "sha256": "1830c1d8e69e0e12d4b9d8af9f194d234ef3437cba546200738a1592a77aa0ca",
    "git_blob_sha": "9b3464345766a956159db88d5d6c4326b662ece4"
  },
  "stage_matrices": {
    "role": "stage_matrices",
    "name": "fixed_fejer_detached_stage_matrices.py",
    "bytes": 47791,
    "sha256": "7aabf3ef5857dbdbbf9832b8bb4ca378faa7e06514a21b48f83649d6df7cb0d7",
    "git_blob_sha": "4fad02c03e92b5fcd3aa2b3621c58a49d1631eff"
  },
  "adjacent_matrices": {
    "role": "adjacent_matrices",
    "name": "fixed_fejer_adjacent_normal_matrices.py",
    "bytes": 36766,
    "sha256": "257e5e44d38dffb82925a410c42e51f084cf7821a398b9928e543088a3f234c0",
    "git_blob_sha": "14ad8790e43b2e58f94772aacd98fb61be7826e9"
  },
  "reference_calibration": {
    "role": "reference_calibration",
    "name": "fixed_fejer_reference_calibration.py",
    "bytes": 11914,
    "sha256": "fe36240c08ad32c4d4d665a387c70aaf02c0392419a51eef01e072081945e95c",
    "git_blob_sha": "c174fcf9712b76abe6f3f3ed307d0115598a1d3d"
  },
  "endpoint": {
    "role": "endpoint",
    "name": "fixed_fejer_normal_lift_operator.py",
    "bytes": 98490,
    "sha256": "1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778",
    "git_blob_sha": "fd9b4ba9526a7805c73957ffc75a3261fa785290"
  },
  "root_packets": {
    "role": "root_packets",
    "name": "fixed_fejer_immutable_normal_root_packets.py",
    "bytes": 72375,
    "sha256": "1445b883cbcf3ed76571760923c2dc735ead7c862439d9478684a5a5299de468",
    "git_blob_sha": "12d26c8b663d185907feec930aa09def002af4cb"
  },
  "reference": {
    "role": "reference",
    "name": "fixed_fejer_axisymmetric_reference.py",
    "bytes": 60335,
    "sha256": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
    "git_blob_sha": "8ad0794ebf0daab9a278c5ea1de784e93b64fd8c"
  },
  "meridian": {
    "role": "meridian",
    "name": "fixed_fejer_supported_so3_meridian_operator.py",
    "bytes": 40840,
    "sha256": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
    "git_blob_sha": "1d9e435bb68374b71c3d7361771c28f47838d59e"
  },
  "continuous": {
    "name": "so3_axisymmetric_continuous_integrand.py",
    "sha256": "a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6",
    "bytes": 29047,
    "git_blob_sha": "76d475cc54814b19e1d3aaaab8200a9ba7d7d151"
  },
  "rotation": {
    "name": "accurate_normal_rotation_and_stage_boxes.py",
    "sha256": "29eed317796b18c5f7430535ee2f45ee7ce9cb6546bbbd44d0bc97b9839e3f6b",
    "bytes": 27453,
    "git_blob_sha": "6e007ee79ccd53e3e7e58469164d6c7e34bff40e"
  },
  "seed_math": {
    "role": "seed_math",
    "name": "fixed_fejer_reference_seed_angular_profile_error_bounds.py",
    "bytes": 72182,
    "sha256": "0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b",
    "git_blob_sha": "c0d09245e9e156cb93516945b3eec84e93807bf7"
  },
  "mean": {
    "role": "mean",
    "name": "fixed_fejer_reference_accurate_mean_residuals.py",
    "bytes": 41476,
    "sha256": "ae67ecac9f205cdb2378a7f981d5d60fc723e1caadd5281dff54395d358564a0",
    "git_blob_sha": "fdddb363e724ab45204854a2b3084fcb95cae4bc"
  }
};
const DEPENDENCIES = {
  "actual_fixed_input_binding": {
    "role": "actual_fixed_input_binding",
    "name": "fixed_fejer_reference_input_binding.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_reference_input_binding.py",
    "bytes": 25672,
    "sha256": "3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f",
    "git_blob_sha": "5eab3f96cb8b1bc245f4de33dc2041cf25d22094"
  },
  "independent_envelope_memory": {
    "role": "independent_envelope_memory",
    "name": "complete_fixed_fejer_material_envelope_memory.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/complete_fixed_fejer_material_envelope_memory.py",
    "bytes": 45988,
    "sha256": "9f268e066274eff19ee2635124a8addf9c92eabf6d7177249f4ac4782c88a39a",
    "git_blob_sha": "d9a09a4e76efa1a4e55831fd566192d150ab67e1"
  },
  "binding": {
    "role": "binding",
    "name": "fixed_fejer_complete_source_binding.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_source_binding.py",
    "bytes": 32487,
    "sha256": "3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88",
    "git_blob_sha": "3073c9490a6bc6ce7dcf323f799ee8075f8bdd78"
  },
  "geometry": {
    "role": "geometry",
    "name": "so3_fixed_fejer_complete_geometry.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_complete_geometry.py",
    "bytes": 70709,
    "sha256": "bab4147bdd2f0d43a372ec1b04225fc66a05db2ccdc2f92968d3f70e2590bf26",
    "git_blob_sha": "f2b28d1bf2f994db9866cb58e74a522ff719358a"
  },
  "transfer": {
    "role": "transfer",
    "name": "transfer_fixed_fejer_material_envelope_memory.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/transfer_fixed_fejer_material_envelope_memory.py",
    "bytes": 66839,
    "sha256": "af35c30e4774987d8f71bc6d05c1942db66a9f7889127c19948b119dee9a1566",
    "git_blob_sha": "597f6529dea5ffeb32e8df43a1442f1f7994d48b"
  },
  "driver": {
    "role": "driver",
    "name": "fullclosed_fixed_fejer_immutable_point_so3_qp.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_immutable_point_so3_qp.py",
    "bytes": 91714,
    "sha256": "477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd",
    "git_blob_sha": "feb49510ddada8fb77d0bf9cf3cd78c1de50079d"
  },
  "launcher": {
    "role": "launcher",
    "name": "launch_fixed_fejer_immutable_point_actions.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_immutable_point_actions.py",
    "bytes": 21789,
    "sha256": "0c1ff0aa2de30fcd490efb4bddd1972613c0f0afb1257d1af0170ac7e60bb5bf",
    "git_blob_sha": "f5d337a07f6b1a0438f33cdaf6fc1845b30f8b84"
  },
  "reader": {
    "role": "reader",
    "name": "read_fixed_fejer_immutable_point_so3_report.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_immutable_point_so3_report.py",
    "bytes": 97987,
    "sha256": "274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b",
    "git_blob_sha": "feae7eaf1b29ea0ae2563c4fc0d8089794602fa3"
  },
  "closure_values": {
    "role": "closure_values",
    "name": "fixed_fejer_immutable_closure_values.py",
    "bytes": 59048,
    "sha256": "01ca74a9f00ac17ef4452173b758d785c0e06869efa98980426f822d4beeb595",
    "git_blob_sha": "f8d32aefb1c11152fd39ad1d5b6d160c60d864ef"
  },
  "analytic_J3": {
    "role": "analytic_J3",
    "name": "fixed_fejer_analytic_stage_jacobian.py",
    "bytes": 25739,
    "sha256": "7645268ee3538a43a4a04b73a5aee4fc5483b56962affeb0ba7e7f879d5d4a72",
    "git_blob_sha": "4fd818ed74a7043b955ef036a0cccccdb3cdc710"
  },
  "analytic_frame": {
    "role": "analytic_frame",
    "name": "fixed_fejer_analytic_normal_frame.py",
    "bytes": 47286,
    "sha256": "75db2f20039b66a2784a922bf062e792328c0153fb0458c16acef92e0ab7e38c",
    "git_blob_sha": "ee0e9799f87301d8a60d6da20cb68731d031cdb0"
  },
  "frame_C1": {
    "role": "frame_C1",
    "name": "fixed_fejer_normal_frame_c1.py",
    "bytes": 37361,
    "sha256": "1830c1d8e69e0e12d4b9d8af9f194d234ef3437cba546200738a1592a77aa0ca",
    "git_blob_sha": "9b3464345766a956159db88d5d6c4326b662ece4"
  },
  "stage_matrices": {
    "role": "stage_matrices",
    "name": "fixed_fejer_detached_stage_matrices.py",
    "bytes": 47791,
    "sha256": "7aabf3ef5857dbdbbf9832b8bb4ca378faa7e06514a21b48f83649d6df7cb0d7",
    "git_blob_sha": "4fad02c03e92b5fcd3aa2b3621c58a49d1631eff"
  },
  "adjacent_matrices": {
    "role": "adjacent_matrices",
    "name": "fixed_fejer_adjacent_normal_matrices.py",
    "bytes": 36766,
    "sha256": "257e5e44d38dffb82925a410c42e51f084cf7821a398b9928e543088a3f234c0",
    "git_blob_sha": "14ad8790e43b2e58f94772aacd98fb61be7826e9"
  },
  "reference_calibration": {
    "role": "reference_calibration",
    "name": "fixed_fejer_reference_calibration.py",
    "bytes": 11914,
    "sha256": "fe36240c08ad32c4d4d665a387c70aaf02c0392419a51eef01e072081945e95c",
    "git_blob_sha": "c174fcf9712b76abe6f3f3ed307d0115598a1d3d"
  },
  "endpoint": {
    "role": "endpoint",
    "name": "fixed_fejer_normal_lift_operator.py",
    "bytes": 98490,
    "sha256": "1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778",
    "git_blob_sha": "fd9b4ba9526a7805c73957ffc75a3261fa785290"
  },
  "root_packets": {
    "role": "root_packets",
    "name": "fixed_fejer_immutable_normal_root_packets.py",
    "bytes": 72375,
    "sha256": "1445b883cbcf3ed76571760923c2dc735ead7c862439d9478684a5a5299de468",
    "git_blob_sha": "12d26c8b663d185907feec930aa09def002af4cb"
  },
  "reference": {
    "role": "reference",
    "name": "fixed_fejer_axisymmetric_reference.py",
    "bytes": 60335,
    "sha256": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
    "git_blob_sha": "8ad0794ebf0daab9a278c5ea1de784e93b64fd8c"
  },
  "meridian": {
    "role": "meridian",
    "name": "fixed_fejer_supported_so3_meridian_operator.py",
    "bytes": 40840,
    "sha256": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
    "git_blob_sha": "1d9e435bb68374b71c3d7361771c28f47838d59e"
  },
  "continuous": {
    "name": "so3_axisymmetric_continuous_integrand.py",
    "sha256": "a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6",
    "bytes": 29047,
    "git_blob_sha": "76d475cc54814b19e1d3aaaab8200a9ba7d7d151"
  },
  "rotation": {
    "name": "accurate_normal_rotation_and_stage_boxes.py",
    "sha256": "29eed317796b18c5f7430535ee2f45ee7ce9cb6546bbbd44d0bc97b9839e3f6b",
    "bytes": 27453,
    "git_blob_sha": "6e007ee79ccd53e3e7e58469164d6c7e34bff40e"
  },
  "seed_math": {
    "role": "seed_math",
    "name": "fixed_fejer_reference_seed_angular_profile_error_bounds.py",
    "bytes": 72182,
    "sha256": "0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b",
    "git_blob_sha": "c0d09245e9e156cb93516945b3eec84e93807bf7"
  },
  "mean": {
    "role": "mean",
    "name": "fixed_fejer_reference_accurate_mean_residuals.py",
    "bytes": 41476,
    "sha256": "ae67ecac9f205cdb2378a7f981d5d60fc723e1caadd5281dff54395d358564a0",
    "git_blob_sha": "fdddb363e724ab45204854a2b3084fcb95cae4bc"
  },
  "operator_schema": "complete-fixed-fejer-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1",
  "base_schema": "complete-fixed-fejer-supported-smooth-triangle-so3-meridian-with-core-lift-v1",
  "reference_schema": "R690-fixed-fejer-axisymmetric-SO3-reference-input-v1",
  "source_role_count": 110,
  "parent_seed_math_sha": "91fd1fb0148c7dde3260bdcfed61b057033d308517960bdb86454cc1e96ab3a1",
  "parent_mean_sha": "19fd82f3d746cce4b7de474f42aeb4192e4e1cec8e38c375148bcd4a9ab51a38"
};
const ADDITIONS = {
  "input": "\ndef bind_fixed_reference_inputs(raw, entry, module, used):\n    \"\"\"Re-read the complete declared recipe and actual six-file input closure.\n\n    Mathematical recipe, actual generated reference/model, and actual full\n    target file have separate identities. None is a future numerical point.\n    \"\"\"\n    if (not isinstance(entry, dict)\n            or entry.get(\"schema\") != \"actual-fixed-fejer-complete-input-entry-binding-v1\"\n            or raw.get(\"actual_fixed_reference_input_binding\") != entry\n            or entry.get(\"source_sha256\") != PINS[\"field_binding\"][1]\n            or entry.get(\"actual_pure_input_binding_source_sha256\") != PINS[\"fixed_input_binding\"][1]\n            or entry.get(\"actual_input_producer_source_sha256\") != PINS[\"reference\"][1]\n            or entry.get(\"all_six_current_whole_files_reread\") is not True):\n        raise ValueError(\"Use the complete source-bound fixed Fejer input entry\")\n    record = entry.get(\"actual_binding_file\")\n    path = used.verify(record)\n    payload = used.json(record)\n    rebound, checked = module.read_binding(path,\n        current_files=entry.get(\"complete_current_input_files\"))\n    if (payload != rebound or checked != entry.get(\"complete_input_validation\")\n            or checked.get(\"actual_binding_file\") != record\n            or checked.get(\"complete_generated_fixed_chart_verified\") is not True\n            or checked.get(\"complete_current_six_files_verified\") is not True\n            or checked.get(\"predeclared_deterministic_mathematical_target\") is not True):\n        raise ValueError(\"The actual complete fixed-input validation changed\")\n    target = payload[\"fixed_target_definition\"]\n    reference = raw[\"representation\"][\"base_complete_model\"][\"complete_axisymmetric_reference_model\"]\n    target_identity = canonical(target)\n    reference_identity = canonical(reference)\n    chart_identity = reference.get(\"fixed_chart_core_sha256\")\n    mathematical_identity = canonical(target[\"mathematical_target_recipe\"])\n    if (target != raw.get(\"independent_fixed_target_definition\")\n            or target_identity != raw.get(\"independent_fixed_target_definition_identity_sha256\")\n            or target_identity != entry.get(\"actual_fixed_target_definition_identity_sha256\")\n            or target_identity != checked.get(\"fixed_target_definition_identity_sha256\")\n            or target.get(\"complete_current_reference_model\") != reference\n            or reference.get(\"schema\") != REFERENCE_SCHEMA\n            or reference.get(\"source_sha256\") != PINS[\"reference\"][1]\n            or reference_identity != entry.get(\"actual_reference_model_identity_sha256\")\n            or reference_identity != checked.get(\"actual_current_model_identity_sha256\")\n            or chart_identity != entry.get(\"actual_fixed_chart_core_sha256\")\n            or chart_identity != checked.get(\"current_fixed_chart_core_sha256\")\n            or mathematical_identity != entry.get(\"mathematical_target_identity_sha256\")\n            or mathematical_identity != checked.get(\"mathematical_target_identity_sha256\")\n            or mathematical_identity != reference.get(\"mathematical_target_identity_sha256\")\n            or not all(valid_digest(value) for value in\n                (target_identity, reference_identity, chart_identity, mathematical_identity))):\n        raise ValueError(\"Keep the complete recipe, actual reference and target identities distinct and equal to their own definitions\")\n    files = entry[\"complete_current_input_files\"]\n    required = {\"current_fixed_input_bundle\", \"current_node_report\",\n        \"current_scalar_input\", \"current_reference_bundle\", \"current_carrier\",\n        \"current_preparation_report\"}\n    if (not isinstance(files, dict) or set(files) != required\n            or files != checked.get(\"current_input_records\")):\n        raise ValueError(\"Retain every complete actual fixed-reference input\")\n    for value in files.values():\n        used.verify(value)\n    # These complete records were actually consumed by the fixed-input binder.\n    # Do not silently substitute a current checkout path for an original path.\n    bound_records = [payload[key] for key in (\"fixed_input_preparation_report\",\n        \"fixed_target_definition_file\", \"new_locations\",\n        \"complete_supplied_location_provenance\")]\n    for value in bound_records:\n        used.verify(value)\n    maker_report = used.json(payload[\"fixed_input_preparation_report\"])\n    def retain_declared_records(value):\n        if isinstance(value, dict):\n            if {\"path\", \"bytes\", \"sha256\"} <= set(value):\n                used.verify(value)\n            for item in value.values():\n                retain_declared_records(item)\n        elif isinstance(value, list):\n            for item in value:\n                retain_declared_records(item)\n    retain_declared_records(maker_report)\n    used.verify(record)\n    return dict(entry=copy_json(entry), binding_payload=copy_json(payload),\n        exact_fixed_target_identity_sha256=target_identity,\n        actual_reference_model_identity_sha256=reference_identity,\n        fixed_chart_core_sha256=chart_identity,\n        mathematical_target_identity_sha256=mathematical_identity,\n        complete_current_input_files=copy_json(files))\n\n",
  "leaf": "\ndef bind_fixed_reference_scope(actual, outer, repo, files):\n    \"\"\"Independently re-read the actual new-target closure before consuming leaves.\"\"\"\n    root = Path(repo).resolve()/TOPIC/\"scripts/resume_20261126\"\n    input_name, input_digest = ACTUAL_INPUT_SOURCE_PINS[\"fixed_input_binding\"]\n    actual_input_name, actual_input_digest = ACCURATE_INPUT_SOURCE\n    source = root/actual_input_name\n    if sha(source) != actual_input_digest:\n        raise ValueError(\"The complete accurate-input constructor changed\")\n    files.add(source)\n    spec = importlib.util.spec_from_file_location(\"_fixed_fejer_leaf_actual_input\", source)\n    actual_module = importlib.util.module_from_spec(spec)\n    sys.modules[spec.name] = actual_module\n    spec.loader.exec_module(actual_module)\n    if sha(source) != actual_input_digest:\n        raise ValueError(\"The accurate-input source changed during loading\")\n    module = actual_module.load(\"_fixed_fejer_leaf_input_binding\", root/input_name, input_digest)\n    book = actual_module.VerifiedFiles()\n    state = actual_module.bind_fixed_reference_inputs(outer,\n        actual.get(\"complete_actual_fixed_reference_input_binding\"), module, book)\n    for record in book.used.values():\n        files.verify(record)\n    expected = {\n        \"exact_fixed_target_identity_sha256\": state[\"exact_fixed_target_identity_sha256\"],\n        \"actual_reference_model_identity_sha256\": state[\"actual_reference_model_identity_sha256\"],\n        \"fixed_chart_core_sha256\": state[\"fixed_chart_core_sha256\"],\n        \"mathematical_target_identity_sha256\": state[\"mathematical_target_identity_sha256\"],\n        \"complete_six_actual_inputs\": state[\"complete_current_input_files\"],\n    }\n    if any(actual.get(key) != value for key, value in expected.items()):\n        raise ValueError(\"The complete actual field binding changed its recipe, chart or any actual input\")\n    base = actual[\"complete_model\"][\"base_complete_model\"]\n    reference = base[\"complete_axisymmetric_reference_model\"]\n    if (base.get(\"fixed_chart_core_sha256\") != expected[\"fixed_chart_core_sha256\"]\n            or canonical(reference) != expected[\"actual_reference_model_identity_sha256\"]\n            or reference.get(\"fixed_chart_core_sha256\") != expected[\"fixed_chart_core_sha256\"]):\n        raise ValueError(\"The normal/base/reference chain differs from the actual fixed chart\")\n    return state\n\n",
  "diameter": "\ndef derived_global_bounds(stats,context,k,complete):\n    \"\"\"Complete-cover bounds, including R717's same-leaf three-dimensional norm.\"\"\"\n    def maxval(key):\n        item=stats.maxima.get(key)\n        return None if item is None else item[\"value\"]\n    result=dict(full_upper_cover_bound_scope=complete,\n        relative_Gram_error_operator_norm_upper=None,\n        principal_curvature_absolute_upper=None,\n        normal_norm_lower=None,upper_base_phase_diameter_upper=None,\n        upper_base_phase_position_hull=None,\n        full_upper_normal_positive_from_boxes=False,\n        full_marked_surface_diameter_upper=None,\n        complete_closed_surface_reach_lower=None,\n        formal_reflection_fixed_caps_all_rotation_set_diameter_upper=None,\n        formal_diameter_is_actual_phase_family_certificate=False)\n    if not complete or stats.count==0:\n        return result\n    if stats.gram_missing==0:\n        result[\"relative_Gram_error_operator_norm_upper\"]=maxval(\"relative_Gram_error_operator_norm_upper\")\n    if stats.curvature_missing==0:\n        result[\"principal_curvature_absolute_upper\"]=maxval(\"principal_curvature_absolute_upper\")\n    result[\"normal_norm_lower\"]=stats.minima[\"normal_norm_lower\"][\"value\"]\n    result[\"full_upper_normal_positive_from_boxes\"]=stats.normal_unproved==0\n    result[\"upper_base_phase_position_hull\"]=stats.position\n    d2=sum(((hi-lo)**2 for lo,hi in stats.position),F(0))\n    result[\"upper_base_phase_diameter_upper\"]=k.sqrt_bounds(d2,context[\"bits\"])[1]\n    rho=max(maxval(\"horizontal_position_norm_upper\"),context[\"R\"].hi,F(1,5))\n    z=max(abs(stats.position[2][0]),abs(stats.position[2][1]),\n        abs(k.rational(context[\"geometry\"][\"current_H\"]))+F(1,1000))\n    cylinder_diameter=2*k.sqrt_bounds(rho*rho+z*z,context[\"bits\"])[1]\n    # One leaf's x,y,z boxes bound one physical point simultaneously.\n    # Rotations about the fixed origin and the lower reflection preserve |F|.\n    upper_norm=maxval(\"full_position_norm_upper\")\n    if upper_norm is None or upper_norm<0:\n        raise ValueError(\"The entire cover must retain every same-leaf position norm\")\n    cap_rho=max(context[\"R\"].hi,F(1,5))\n    cap_z=abs(k.rational(context[\"geometry\"][\"current_H\"]))+F(1,1000)\n    cap_norm=k.sqrt_bounds(cap_rho*cap_rho+cap_z*cap_z,context[\"bits\"])[1]\n    complete_set_norm=max(upper_norm,cap_norm)\n    norm_diameter=2*complete_set_norm\n    result[\"formal_reflection_fixed_caps_all_rotation_set_diameter_upper\"]=min(\n        cylinder_diameter,norm_diameter)\n    result[\"formal_diameter_definition\"]=dict(\n        upper_set=\"the complete same-point upper-meridian image\",\n        lower_set=\"formal reflection (x,y,z)->(x,y,-z)\",\n        activity_motion=\"formal rotations about the fixed origin z axis\",\n        cap_set=\"formal disks of the current accurate R at +/-H with the fixed p4 recipe\",\n        cap_mark_height=\"1/1000\",cap_mark_support_radius=\"1/5\",\n        horizontal_radius_upper=str(rho),absolute_z_upper=str(z),\n        radius_support_disks_fit_from_current_R_lower=context[\"R\"].lo>=F(1,5),\n        diameter_method=\"minimum of the complete same-leaf three-dimensional norm bound and the complete coordinate-cylinder bound\",\n        same_leaf_position_norm_upper=str(upper_norm),\n        cap_position_norm_upper=str(cap_norm),\n        complete_rotation_reflection_and_cap_position_norm_upper=str(complete_set_norm),\n        same_leaf_norm_diameter_upper=str(norm_diameter),\n        separate_coordinate_cylinder_diameter_upper=str(cylinder_diameter),\n        all_upper_lower_activity_phase_and_fixed_cap_pairs_in_formal_union=True,\n        same_leaf_position_norms_come_from_all_complete_physical_sixjet_leaves=True,\n        distinct_leaf_coordinate_extrema_not_combined_in_norm_bound=True,\n        proof_reference=\"R717 section 9\",\n        additional_field_root_or_angle_evaluations=0,\n        source_link_to_an_actual_closed_physical_family_proved=False)\n    return result\n\n"
};
const OUTPUTS = {
  "input": {
    "role": "input",
    "name": "fixed_fejer_normal_packet_accurate_field_input.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_normal_packet_accurate_field_input.py",
    "bytes": 32991,
    "sha256": "1e5101d7bd08a8b3787b6eaa699c915a9e8bd173d365233c7be90f1aee1b3f3f"
  },
  "radial": {
    "role": "radial",
    "name": "fixed_fejer_accurate_reference_control_radial_boxes.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_accurate_reference_control_radial_boxes.py",
    "bytes": 45317,
    "sha256": "c52044c5b12000486dc0673f6ddf0a23935239348f5534f103d0f75fb9d585d4"
  },
  "normal": {
    "role": "normal",
    "name": "fixed_fejer_complete_normal_root_and_sixjet_fees.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_normal_root_and_sixjet_fees.py",
    "bytes": 40294,
    "sha256": "1a915b058e7bd9c9edb7905f68d491c597c98b9d69521db97c7eadc2bf8bda35"
  },
  "leaf": {
    "role": "leaf",
    "name": "fixed_fejer_complete_physical_leaf_binding.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_physical_leaf_binding.py",
    "bytes": 47321,
    "sha256": "ee03b17d9c716ef24d76552cec1fc6031b7fa1eb037cf7cb55ddc9980b28721c"
  },
  "geometry": {
    "role": "geometry",
    "name": "fixed_fejer_continuous_gram_curvature_support.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_continuous_gram_curvature_support.py",
    "bytes": 46689,
    "sha256": "fcae1e5926e8e70edbd78a9e3b276f46e3b7b345b1ad2d6ec647905e6c5a4d2b"
  },
  "bridge": {
    "role": "bridge",
    "name": "fixed_fejer_complete_geometry_support_beta_bridge.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_geometry_support_beta_bridge.py",
    "bytes": 20810,
    "sha256": "ff77dd925949bffaed4bffce8249554cfb0d56390da70bc3398cebe1f2202d15"
  }
};
const READY_OUTPUTS = {
  "normal": {
    "role": "normal_ready",
    "name": "fixed-fejer-complete-normal32-full-circle-sixjet-fees-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-complete-normal32-full-circle-sixjet-fees-ready.json",
    "bytes": 9380,
    "sha256": "d38cabbbc9dbc3dd973fe271de7085b9ab5a5f6d5b14df5476c22fba3b91fafa"
  },
  "geometry": {
    "role": "geometry_ready",
    "name": "fixed-fejer-complete-continuous-gram-curvature-support-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-complete-continuous-gram-curvature-support-ready.json",
    "bytes": 9901,
    "sha256": "a2171bdfafd5aa4b3a2c70d53b57bb7c055be4dc17d29138b77fed211323aae4"
  }
};
const READY_SOURCES = {
  "normal": "{\n  \"schema\": \"complete-fixed-fejer-normal-32-stage-and-full-angle-sixjet-fees-ready-v1\",\n  \"executed\": false,\n  \"admitted\": false,\n  \"scientific_execution_only_in_public_Actions\": true,\n  \"complete_source_sha256\": {\n    \"fixed_fejer_normal_packet_accurate_field_input.py\": \"1e5101d7bd08a8b3787b6eaa699c915a9e8bd173d365233c7be90f1aee1b3f3f\",\n    \"fixed_fejer_accurate_reference_control_radial_boxes.py\": \"c52044c5b12000486dc0673f6ddf0a23935239348f5534f103d0f75fb9d585d4\",\n    \"fixed_fejer_complete_normal_root_and_sixjet_fees.py\": \"1a915b058e7bd9c9edb7905f68d491c597c98b9d69521db97c7eadc2bf8bda35\",\n    \"accurate_normal_rotation_and_stage_boxes.py\": \"29eed317796b18c5f7430535ee2f45ee7ce9cb6546bbbd44d0bc97b9839e3f6b\"\n  },\n  \"source_report_expected_path\": \"{work}/fixed-fejer-immutable-point-first/report.json\",\n  \"source_report_sha256_not_yet_assumed\": null,\n  \"actual_snapshot_identity_not_yet_assumed\": null,\n  \"actual_field_report_or_packet_success_not_assumed\": true,\n  \"snapshot_selection\": \"Latest genuine complete required-angle immutable snapshot; every originally cached angle retained; actual accepted outer point not inferred\",\n  \"exact_normal_stage_count\": 32,\n  \"complete_exact_phi_over_pi_domain\": [\n    \"0\",\n    \"2\"\n  ],\n  \"full_angle_closed_cells\": 1024,\n  \"quarter_orbit_symmetry_not_assumed\": true,\n  \"complete_original_radial_affine_domain_retained\": true,\n  \"complete_reference_mean_and_profile_recomputed_as_accurate_whole_angle_boxes\": true,\n  \"previous_literal_only_fees_relabelled_as_uniform\": false,\n  \"working_field_J_or_root_replayed\": false,\n  \"all_raw_proofs_and_physical_streams_only_on_runner\": true,\n  \"solver_admission_prerequisite\": false,\n  \"scientific_solver_parameters_or_sources_changed\": false,\n  \"saved_high_angular_order_not_upgraded\": true,\n  \"complete_physical_working_word_errors_paid\": false,\n  \"lower_reflection_caps_orientation_embedding_physical_phase_reach_separate\": true,\n  \"historical_unknown_peer_obligations_removed\": false,\n  \"partial_budget_return_is_not_certificate_or_solver_failure\": true,\n  \"steps\": [\n    {\n      \"id\": \"actual-fixed-fejer-complete-normal32-full-circle-sixjet-fees-first-20261127\",\n      \"script\": \"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_normal_root_and_sixjet_fees.py\",\n      \"parent_bundle\": \"fixed-fejer-reference/reference.npz\",\n      \"scope\": \"Complete accurate fee execution for the predeclared fixed Fejer target, pending a genuine complete immutable 477499/274d solver report snapshot. Re-read the whole 110-role current source closure, complete actual fixed-input binding, all six actual inputs, full point/model/target and all recorded immutable angular packets. Retain every actual cached/required literal angle and all 32 common normal stages; additionally enclose every one of 1024 closed full-circle cells phi/pi in [0,2]. Independently compute the accurate R709 mean/profile whole-angle boxes, all original exact affine radial pieces and the true exponential/control/frame chains. Use an original stage_XXX_J only as an arbitrary rational preconditioner proposal, preserving its actual order and complete words. Prove local stage root/first/second angular enclosures with every upstream dependency, then emit same-target a_deep/b/c/bs/cs/rho0 whole boxes and all physical sixjets including h/hp/hpp raw-defect terms. Glue only by directed inclusion into a uniqueness domain, including periodic and original-literal association. No working F/J/root replay. A natural 900-second partial return retains complete prefixes and is neither nonexistence nor a complete cover. Lower/cap C2, orientation, embedding, physical phases, mixed-pair reach, working-sixjet-word and external-parameter fees remain separate. No future report, point, snapshot or fee value is prefilled.\",\n      \"args\": [\n        \"--repo\",\n        \"{repo}\",\n        \"--report\",\n        \"{work}/fixed-fejer-immutable-point-first/report.json\",\n        \"--outdir\",\n        \"{work}/fixed-fejer-normal-root-and-sixjet-fees-v1\",\n        \"--seconds\",\n        \"900\",\n        \"--maximum-leaf-evaluations\",\n        \"1000000\",\n        \"--precision-bits\",\n        \"192\",\n        \"--panels\",\n        \"128\",\n        \"--rho-leaf-budget\",\n        \"8192\",\n        \"--inverse-steps\",\n        \"64\",\n        \"--inverse-width\",\n        \"1/1000000000000000000000000\",\n        \"--full-angle-cells\",\n        \"1024\",\n        \"--radial-depth\",\n        \"0\",\n        \"--mean-maximum-splits\",\n        \"8192\",\n        \"--mean-width-goal\",\n        \"1/1000000000\",\n        \"--first-exp-degree\",\n        \"24\",\n        \"--maximum-exp-degree\",\n        \"128\",\n        \"--root-radius\",\n        \"1/100000000\",\n        \"--root-radius\",\n        \"1/1000000\",\n        \"--root-radius\",\n        \"1/10000\"\n      ],\n      \"outputs\": [\n        \"fixed-fejer-normal-root-and-sixjet-fees-v1/report.json\"\n      ],\n      \"summary\": {\n        \"fixed-fejer-normal-root-and-sixjet-fees-v1/report.json\": {\n          \"schema\": \"schema\",\n          \"source\": \"source_sha256\",\n          \"source_commit\": \"source_commit\",\n          \"run\": \"github_run_id\",\n          \"run_attempt\": \"github_run_attempt\",\n          \"actual_report\": \"actual_report.sha256\",\n          \"actual_full_point\": \"actual_current_full_point_sha256\",\n          \"actual_snapshot\": \"actual_snapshot_identity_sha256\",\n          \"actual_driver\": \"actual_scientific_driver_sha256\",\n          \"actual_reader\": \"actual_pure_reader_sha256\",\n          \"input_request\": \"complete_input_and_request_identity_sha256\",\n          \"complete_execution_binding\": \"complete_binding_identity_sha256\",\n          \"geometry_setup\": \"accurate_geometry_setup_complete\",\n          \"complete_all_requested\": \"complete\",\n          \"all_stages_and_streams\": \"all_planned_original_stages_and_sixjet_streams_complete\",\n          \"final_byte_recheck\": \"all_bound_input_and_output_bytes_rechecked_at_final_report\",\n          \"all_recorded_angles\": \"all_original_recorded_angle_count\",\n          \"all_required_angles\": \"all_original_required_angle_count\",\n          \"requested_full_circle_cells\": \"requested_full_circle_cell_count\",\n          \"planned_jobs\": \"planned_job_count\",\n          \"completed_jobs\": \"completed_job_count\",\n          \"whole_continuous_branch\": \"full_same_field_angle_branch.complete_continuous_angle_branch_certified\",\n          \"actual_leaf_evaluations\": \"actual_work_budget.actual_leaf_evaluations\",\n          \"maximum_leaf_evaluations\": \"actual_work_budget.maximum_leaf_evaluations\",\n          \"actual_budget_exhausted\": \"actual_work_budget.exhausted\",\n          \"elapsed_hex\": \"elapsed_seconds_binary64_hex\",\n          \"working_root_field_calls\": \"existing_working_root_and_field_calls\",\n          \"working_J_JT_calls\": \"existing_working_J_or_Jtranspose_calls\",\n          \"actual_words_not_fabricated\": \"comparison_candidates_were_existing_complete_actual_packet_words\",\n          \"actual_second_order_not_invented\": \"working_second_order_words_not_invented\",\n          \"working_physical_word_errors_paid\": \"complete_original_working_physical_sixjet_word_errors_paid\",\n          \"sixjet_scope\": \"physical_sixjet_output_scope\",\n          \"closed_geometry_certified\": \"complete_reflected_closed_surface_C2_or_reach_certificate\",\n          \"external_parameter_fees_paid\": \"external_parameter_J_and_transpose_error_certificate\",\n          \"historical_obligations_removed\": \"unknown_historical_material_role_obligations_removed\",\n          \"problem_completed\": \"mathematical_problem_completion_claimed\"\n        }\n      }\n    }\n  ],\n  \"actual_scientific_source_sha256\": \"477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd\",\n  \"actual_complete_reader_sha256\": \"274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b\",\n  \"actual_fixed_target_definition_identity_sha256\": null,\n  \"actual_reference_model_identity_sha256\": null,\n  \"historical_carrier_used_as_current_reference_values\": false,\n  \"complete_same_target_scalar_a_b_c_jet_boxes_in_every_physical_leaf\": true,\n  \"complete_scientific_runtime_source_role_count\": 110,\n  \"current_normal_source_sha256\": \"1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778\",\n  \"current_immutable_packet_source_sha256\": \"1445b883cbcf3ed76571760923c2dc735ead7c862439d9478684a5a5299de468\",\n  \"complete_reference_mean_source\": {\n    \"name\": \"fixed_fejer_reference_accurate_mean_residuals.py\",\n    \"sha256\": \"ae67ecac9f205cdb2378a7f981d5d60fc723e1caadd5281dff54395d358564a0\"\n  },\n  \"complete_reference_profile_source\": {\n    \"name\": \"fixed_fejer_reference_seed_angular_profile_error_bounds.py\",\n    \"sha256\": \"0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b\"\n  },\n  \"current_report_snapshot_not_progress_json\": true,\n  \"mathematical_target_identity_sha256_not_used_as_actual_target_identity\": true,\n  \"actual_target_and_reference_identities_read_from_complete_fixed_input_binding\": true,\n  \"complete_predeclared_fixed_input_binding_source_sha256\": \"3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f\",\n  \"preexisting_run10_sources_and_parameters_unchanged\": true,\n  \"preexisting_historical_unknown_location_obligations_removed\": false,\n  \"actual_field_point_or_fee_values_assumed\": false,\n  \"predeclared_reference_tail_leaf_count\": 2218,\n  \"historical_2397_carrier_used_as_current_reference_values\": false,\n  \"producer_uses_complete_frozen_dyadic_fejer_chart_and_actual_mesh\": true\n}\n",
  "geometry": "{\n  \"schema\": \"complete-fixed-fejer-continuous-gram-curvature-support-ready-v1\",\n  \"executed\": false,\n  \"admitted\": false,\n  \"scientific_execution_only_in_public_Actions\": true,\n  \"complete_source_sha256\": {\n    \"fixed_fejer_complete_physical_leaf_binding.py\": \"ee03b17d9c716ef24d76552cec1fc6031b7fa1eb037cf7cb55ddc9980b28721c\",\n    \"fixed_fejer_continuous_gram_curvature_support.py\": \"fcae1e5926e8e70edbd78a9e3b276f46e3b7b345b1ad2d6ec647905e6c5a4d2b\",\n    \"fixed_fejer_complete_geometry_support_beta_bridge.py\": \"ff77dd925949bffaed4bffce8249554cfb0d56390da70bc3398cebe1f2202d15\"\n  },\n  \"source_normal_report_expected_path\": \"{work}/fixed-fejer-normal-root-and-sixjet-fees-v1/report.json\",\n  \"future_source_normal_report_sha256\": null,\n  \"future_actual_point_or_snapshot\": null,\n  \"fixed_actual_normal_fee_source_sha256\": \"1a915b058e7bd9c9edb7905f68d491c597c98b9d69521db97c7eadc2bf8bda35\",\n  \"fixed_actual_radial_source_sha256\": \"c52044c5b12000486dc0673f6ddf0a23935239348f5534f103d0f75fb9d585d4\",\n  \"exact_phi_over_pi_domain\": [\n    \"0\",\n    \"2\"\n  ],\n  \"all_original_32_stages_and_literal_associations_checked\": true,\n  \"all_complete_exact_radial_leaves_and_tail_retained\": true,\n  \"relative_Gram_uses_symmetric_operator_norm_not_entry_max\": true,\n  \"complete_physical_sixjets_and_raw_lift_retained\": true,\n  \"same_target_a_deep_and_fixed_rho0_true_enclosures_required\": true,\n  \"output_scope\": \"complete source-bound upper-meridian whole-cell enclosures; closed assembly and all physical phases are separate\",\n  \"original_solver_admission_gate\": false,\n  \"original_scientific_sources_or_parameters_changed\": false,\n  \"raw_support_and_matrix_streams_retained_only_on_runner\": true,\n  \"partial_budget_is_not_geometric_impossibility\": true,\n  \"all_preexisting_pending_queue_objects_must_be_kept_without_modification\": true,\n  \"queue_size_policy\": \"If adding this entire step exceeds95KB, archive only genuinely returned objects or preserve complete non-step history elsewhere with an exact pointer; do not trim pending argv/selectors/domain.\",\n  \"steps\": [\n    {\n      \"id\": \"actual-fixed-fejer-whole-normal-leaf-continuous-gram-curvature-support-first-20261127\",\n      \"script\": \"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_continuous_gram_curvature_support.py\",\n      \"parent_bundle\": \"fixed-fejer-reference/reference.npz\",\n      \"scope\": \"Consume the genuine complete 1a915b fixed-Fejer normal-fee report and every original 32-stage/angular/root journal. Retain all literal associations, all full [0,2] phi/pi cells and every exact radial leaf including the complete tail. Re-read the immutable physical sixjet streams and same-target a_deep/rho0 boxes. Compute complete symmetric 2x2 relative-Gram operator bounds, full-second-form curvature bounds and candidate N=Fphi cross Fs support numerators. Add R717's complete same-leaf three-dimensional position norm, then take the minimum of its formal full-union diameter bound and the original coordinate-cylinder bound. This accounts for all points of the formal rotated/reflected/cap union but does not itself certify the actual closed physical family. No new working F/J/root or accurate integrand evaluation. Incomplete jobs, missing positivity, exhausted budgets and unproved branch glue remain explicit; no missing domain is filled with zero. Only complete global upper-cover numbers are promoted. Lower reflection, closed C2/outward assembly, actual physical phases, all mixed-pair reach and the beta consumer's eight full evidence roles remain separate. Original solver parameters, stages, variables and unknown historical obligations are unchanged.\",\n      \"args\": [\n        \"--repo\",\n        \"{repo}\",\n        \"--normal-report\",\n        \"{work}/fixed-fejer-normal-root-and-sixjet-fees-v1/report.json\",\n        \"--outdir\",\n        \"{work}/fixed-fejer-continuous-gram-curvature-support-v1\",\n        \"--seconds\",\n        \"900\"\n      ],\n      \"outputs\": [\n        \"fixed-fejer-continuous-gram-curvature-support-v1/report.json\"\n      ],\n      \"summary\": {\n        \"fixed-fejer-continuous-gram-curvature-support-v1/report.json\": {\n          \"schema\": \"schema\",\n          \"source\": \"source_sha256\",\n          \"source_commit\": \"source_commit\",\n          \"run\": \"github_run_id\",\n          \"attempt\": \"github_run_attempt\",\n          \"normal_report\": \"normal_report.sha256\",\n          \"geometry_binding\": \"complete_binding_identity_sha256\",\n          \"actual_point\": \"actual_current_full_point_sha256\",\n          \"model\": \"complete_original_model_identity_sha256\",\n          \"snapshot\": \"actual_snapshot_identity_sha256\",\n          \"target\": \"exact_fixed_target_identity_sha256\",\n          \"scalar\": \"fixed_scalar_metric_identity_sha256\",\n          \"setup\": \"geometry_setup_available\",\n          \"complete_upper\": \"complete\",\n          \"whole_angle_jobs\": \"expected_whole_angle_jobs\",\n          \"upstream_whole_jobs\": \"upstream_complete_whole_angle_jobs\",\n          \"processed_whole_jobs\": \"processed_complete_whole_angle_jobs\",\n          \"exact_radial_leaves\": \"expected_radial_leaves_per_angle\",\n          \"expected_all_leaves\": \"expected_complete_geometry_leaves\",\n          \"processed_leaves\": \"processed_geometry_leaves\",\n          \"complete_cover\": \"full_upper_cover_processed\",\n          \"continuous_Gram_complete\": \"continuous_Gram_bound_complete\",\n          \"continuous_K_complete\": \"continuous_curvature_bound_complete\",\n          \"continuous_support_complete\": \"continuous_support_numerator_bounds_complete\",\n          \"positive_upper_immersion_boxes\": \"complete_upper_immersion_lower_from_boxes\",\n          \"original_branch\": \"original_complete_angle_branch.complete\",\n          \"final_all_bytes\": \"all_input_and_output_bytes_rechecked\",\n          \"Gram_operator_upper\": \"accurate_global_bounds.relative_Gram_error_operator_norm_upper\",\n          \"curvature_upper\": \"accurate_global_bounds.principal_curvature_absolute_upper\",\n          \"normal_norm_lower\": \"accurate_global_bounds.normal_norm_lower\",\n          \"upper_only_D\": \"accurate_global_bounds.upper_base_phase_diameter_upper\",\n          \"formal_reflected_rotated_D\": \"accurate_global_bounds.formal_reflection_fixed_caps_all_rotation_set_diameter_upper\",\n          \"formal_D_actual_phase_proved\": \"accurate_global_bounds.formal_diameter_is_actual_phase_family_certificate\",\n          \"full_closed_D\": \"accurate_global_bounds.full_marked_surface_diameter_upper\",\n          \"full_closed_reach\": \"accurate_global_bounds.complete_closed_surface_reach_lower\",\n          \"Gram_unavailable\": \"partial_processed_statistics.relative_Gram_unavailable_leaf_count\",\n          \"K_unavailable\": \"partial_processed_statistics.curvature_unavailable_leaf_count\",\n          \"normal_positive_unproved\": \"partial_processed_statistics.normal_positive_unproved_leaf_count\",\n          \"lower_horizontal_support\": \"partial_processed_statistics.minima_over_processed_leaves.horizontal_support_numerator_lower.value\",\n          \"lower_vertical_support\": \"partial_processed_statistics.minima_over_processed_leaves.vertical_support_numerator_lower.value\",\n          \"new_working_F_J_root\": \"new_working_field_J_or_root_calls\",\n          \"new_accurate_root_integrands\": \"new_accurate_root_or_integrand_calls\",\n          \"closed_geometry\": \"complete_closed_geometry_certified\",\n          \"elapsed_hex\": \"elapsed_seconds_binary64_hex\",\n          \"same_leaf_norm_upper\": \"accurate_global_bounds.formal_diameter_definition.same_leaf_position_norm_upper\",\n          \"fixed_cap_norm_upper\": \"accurate_global_bounds.formal_diameter_definition.cap_position_norm_upper\",\n          \"norm_diameter_upper\": \"accurate_global_bounds.formal_diameter_definition.same_leaf_norm_diameter_upper\",\n          \"coordinate_cylinder_D_upper\": \"accurate_global_bounds.formal_diameter_definition.separate_coordinate_cylinder_diameter_upper\"\n        }\n      }\n    }\n  ],\n  \"optional_beta_bridge\": {\n    \"script\": \"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_geometry_support_beta_bridge.py\",\n    \"scheduled\": false,\n    \"reason\": \"No complete same-field closed/outward/full-phase proof package has returned; no evidence role is synthesized.\",\n    \"full_cli_required_keys\": [\n      \"--repo\",\n      \"--geometry-report\",\n      \"--expected-geometry-report-sha256\",\n      \"--beta-input\",\n      \"--expected-beta-input-sha256\",\n      \"--output\"\n    ],\n    \"requires_all_original_eight_evidence_roles\": true,\n    \"additionally_requires_same_field_lower_reflection_and_all_activity_seams\": true,\n    \"outward_claim_is_external_and_not_inferred_from_an_upper_complete_flag\": true,\n    \"original_beta_source_sha256\": \"e0b44e22fa9e41109ccdeb1c3908aeca60c5c4a18f90dca088f8c9e0243b5991\"\n  },\n  \"actual_scientific_source_sha256\": \"477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd\",\n  \"actual_complete_reader_sha256\": \"274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b\",\n  \"actual_fixed_target_definition_identity_sha256\": null,\n  \"actual_reference_model_identity_sha256\": null,\n  \"complete_scientific_runtime_source_role_count\": 110,\n  \"mathematical_target_identity_sha256_not_used_as_actual_target_identity\": true,\n  \"actual_target_and_reference_identities_read_from_complete_fixed_input_binding\": true,\n  \"complete_predeclared_fixed_input_binding_source_sha256\": \"3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f\",\n  \"preexisting_run10_sources_and_parameters_unchanged\": true,\n  \"preexisting_historical_unknown_location_obligations_removed\": false,\n  \"actual_field_point_or_fee_values_assumed\": false,\n  \"predeclared_reference_tail_leaf_count\": 2218,\n  \"historical_2397_carrier_used_as_current_reference_values\": false,\n  \"producer_uses_complete_frozen_dyadic_fejer_chart_and_actual_mesh\": true,\n  \"R717_same_leaf_full_position_norm_and_complete_formal_union_diameter\": true,\n  \"R717_diameter_is_actual_closed_phase_certificate\": false\n}\n"
};

function buildFixedFejerFees(parents, deps, additions, hash, byteLength) {
  const outputs = {}, patches = [];
  const names = {
    input: "fixed_fejer_normal_packet_accurate_field_input.py",
    radial: "fixed_fejer_accurate_reference_control_radial_boxes.py",
    normal: "fixed_fejer_complete_normal_root_and_sixjet_fees.py",
    leaf: "fixed_fejer_complete_physical_leaf_binding.py",
    geometry: "fixed_fejer_continuous_gram_curvature_support.py",
    bridge: "fixed_fejer_complete_geometry_support_beta_bridge.py"
  };
  const active = {};
  function patch(role, old, value, label, every=false) {
    const s=active[role], count=s.split(old).length-1;
    if(!old || !count || (!every && count!==1)) throw Error(role+" / "+label+" count "+count);
    const positions=[];let from=0;while(true){const i=s.indexOf(old,from);if(i<0)break;positions.push(i);from=i+old.length;}
    active[role]=s.split(old).join(value);
    patches.push({role,label,count,old,new:value,positions,before_sha256:hash(s),after_sha256:hash(active[role])});
  }
  function assign(role,name,value) {
    const re=new RegExp("^"+name+"\\s*=.*$","m");
    const match=active[role].match(re);
    if(!match)throw Error("missing assignment "+role+" "+name);
    patch(role,match[0],name+" = "+value,"constant "+name);
  }
  function removeAssign(role,name) {
    const re=new RegExp("^"+name+"\\s*=.*\\n","m");
    const match=active[role].match(re);
    if(!match)throw Error("missing removal "+role+" "+name);
    patch(role,match[0],"","remove obsolete actual identity "+name);
  }
  function dictionary(role,name,value) {
    const re=new RegExp("^"+name+"\\s*= \\{[\\s\\S]*?^\\}","m");
    let match=active[role].match(re);
    if(!match){
      const re2=new RegExp("^"+name+"=\\{[\\s\\S]*?^\\}","m");
      match=active[role].match(re2);
    }
    if(!match)throw Error("missing dictionary "+role+" "+name);
    const body=name+" = {\n"+Object.entries(value).map(([k,v])=>"    "+JSON.stringify(k)+": ("+JSON.stringify(v[0])+", "+JSON.stringify(v[1])+"),").join("\n")+"\n}";
    patch(role,match[0],body,"complete "+name);
  }
  function done(role) {
    const source=active[role];
    if(byteLength(source)>=100000)throw Error("whole source too large "+role);
    outputs[role]={source,record:{role,name:names[role],path:"topics/visible-flex-larger-amplitude/scripts/resume_20261126/"+names[role],bytes:byteLength(source),sha256:hash(source)}};
  }
  for(const [role,p] of Object.entries(parents)) {
    active[role]=p.source;
    for(const [r,n] of Object.entries(names)) {
      const old=parents[r].record.name;
      if(active[role].includes(old))patch(role,old,n,"new complete basename "+r,true);
    }
    if(active[role].includes("actual-run10"))patch(role,"actual-run10","actual-fixed-fejer","independent actual schema",true);
    if(active[role].includes("_run10_"))patch(role,"_run10_","_fixed_fejer_","independent module names",true);
    if(active[role].includes("run10 "))patch(role,"run10 ","fixed Fejer ","new-target prose",true);
  }
  const inputPins={
    reader:[deps.reader.name,deps.reader.sha256],
    driver:[deps.driver.name,deps.driver.sha256],
    packets:[deps.root_packets.name,deps.root_packets.sha256],
    normal:[deps.endpoint.name,deps.endpoint.sha256],
    base:[deps.meridian.name,deps.meridian.sha256],
    reference:[deps.reference.name,deps.reference.sha256],
    continuous:[deps.continuous.name,deps.continuous.sha256],
    reference_fees:[deps.seed_math.name,deps.seed_math.sha256],
    mean_integrals:[deps.mean.name,deps.mean.sha256],
    fixed_input_binding:[deps.actual_fixed_input_binding.name,deps.actual_fixed_input_binding.sha256],
    field_binding:[deps.binding.name,deps.binding.sha256]
  };
  dictionary("input","PINS",inputPins);
  for(const name of ["ACTUAL_TARGET","ACTUAL_REFERENCE","ACTUAL_CHART"])removeAssign("input",name);
  assign("input","NORMAL_SCHEMA",JSON.stringify(deps.operator_schema));
  assign("input","BASE_SCHEMA",JSON.stringify(deps.base_schema));
  patch("input","\n\ndef require_actions():","\nREFERENCE_SCHEMA = "+JSON.stringify(deps.reference_schema)+"\nACTUAL_SOURCE_ROLE_COUNT = "+deps.source_role_count+"\n\n\ndef require_actions():","explicit fixed reference schema and complete source role count");
  patch("input","\n\nclass ActualNormalPacketPoint:","\n"+additions.input+"\nclass ActualNormalPacketPoint:","complete actual fixed input binder");
  patch("input",'        self.seed_fees = load("_normal_fee_reference_math", self.paths["reference_fees"], PINS["reference_fees"][1])',
    '        self.seed_fees = load("_normal_fee_reference_math", self.paths["reference_fees"], PINS["reference_fees"][1])\n        self.fixed_input_module = load("_normal_fee_fixed_fejer_inputs",\n            self.paths["fixed_input_binding"], PINS["fixed_input_binding"][1])',"load complete fixed input source");
  patch("input","        if len(roles) != 75 or raw.get(","        if len(roles) != ACTUAL_SOURCE_ROLE_COUNT or raw.get(","all current 110 scientific roles");
  patch("input",'        self.model = copy_json(raw["representation"])',
    '        self.fixed_reference_scope = bind_fixed_reference_inputs(raw,\n            pure.get("actual_fixed_reference_input_binding"), self.fixed_input_module, self.used)\n        self.target_identity = self.fixed_reference_scope["exact_fixed_target_identity_sha256"]\n        self.reference_identity = self.fixed_reference_scope["actual_reference_model_identity_sha256"]\n        self.fixed_chart_identity = self.fixed_reference_scope["fixed_chart_core_sha256"]\n        self.mathematical_target_identity = self.fixed_reference_scope["mathematical_target_identity_sha256"]\n        self.model = copy_json(raw["representation"])',"actual dynamic target/model/chart before full model validation");
  patch("input","canonical(self.reference_model) != ACTUAL_REFERENCE","canonical(self.reference_model) != self.reference_identity","actual reference identity");
  patch("input",'self.reference_model.get("fixed_chart_core_sha256") != ACTUAL_CHART','self.reference_model.get("fixed_chart_core_sha256") != self.fixed_chart_identity',"actual fixed chart identity");
  patch("input",'raw.get("independent_fixed_target_definition_identity_sha256") != ACTUAL_TARGET','raw.get("independent_fixed_target_definition_identity_sha256") != self.target_identity',"actual fixed target identity");
  const oldCurrent='        current = pure["actual_public_reference_input_binding"]\n        if (current.get("actual_fixed_target_definition_identity_sha256") != ACTUAL_TARGET\n                or current.get("actual_reference_model_identity_sha256") != ACTUAL_REFERENCE\n                or current.get("actual_fixed_chart_core_sha256") != ACTUAL_CHART):\n            raise ValueError("The actual six-file public-input contract differs")';
  const newCurrent='        current = self.fixed_reference_scope["entry"]\n        if (current.get("actual_fixed_target_definition_identity_sha256") != self.target_identity\n                or current.get("actual_reference_model_identity_sha256") != self.reference_identity\n                or current.get("actual_fixed_chart_core_sha256") != self.fixed_chart_identity):\n            raise ValueError("The actual six-file fixed Fejer input contract differs")';
  patch("input",oldCurrent,newCurrent,"complete current fixed input context");
  patch("input","self.context.identity != ACTUAL_REFERENCE","self.context.identity != self.reference_identity","actual context reference identity");
  patch("input","complete_model=self.model, exact_fixed_target_identity_sha256=ACTUAL_TARGET,\n            actual_reference_model_identity_sha256=ACTUAL_REFERENCE,",
    "complete_model=self.model, exact_fixed_target_identity_sha256=self.target_identity,\n            actual_reference_model_identity_sha256=self.reference_identity,\n            fixed_chart_core_sha256=self.fixed_chart_identity,\n            mathematical_target_identity_sha256=self.mathematical_target_identity,\n            complete_actual_fixed_reference_input_binding=copy_json(current),","actual complete target/input evidence in durable binding");
  patch("input","    def recheck(self):\n        self.used.recheck()",
    '    def recheck(self):\n        rebound = bind_fixed_reference_inputs(self.report,\n            self.fixed_reference_scope["entry"], self.fixed_input_module, self.used)\n        if rebound != self.fixed_reference_scope:\n            raise ValueError("The full fixed-reference input changed during accurate field work")\n        self.used.recheck()',"final whole fixed input recheck");
  done("input");

  assign("radial","INPUT_SHA",JSON.stringify(outputs.input.record.sha256));
  assign("radial","MEAN_SHA",JSON.stringify(deps.mean.sha256));
  assign("radial","SEED_MATH_SHA",JSON.stringify(deps.seed_math.sha256));
  patch("radial",'complete_reference_source_sha256=actual.PINS["reference"][1]\n                if hasattr(actual, "PINS") else "4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3",',
    'complete_reference_source_sha256=actual.reference_model["source_sha256"],',"actual proved reference source; no historical fallback label");
  patch("radial","The parent constructor is deliberately not invoked: it binds one old API",
    "The parent constructor is deliberately not invoked: it binds one literal API","whole-angle adapter constructor scope");
  patch("radial","actual batch/literal angle. This adapter first binds the genuine full run10",
    "actual batch/literal angle. This adapter first binds the genuine full fixed Fejer", "whole-angle new target description");
  done("radial");

  dictionary("normal","PINS",{
    actual_input:[names.input,outputs.input.record.sha256],
    accurate_rotation:[deps.rotation.name,deps.rotation.sha256],
    accurate_radial:[names.radial,outputs.radial.record.sha256]
  });
  assign("normal","ACTUAL_DRIVER",JSON.stringify(deps.driver.sha256));
  assign("normal","ACTUAL_READER",JSON.stringify(deps.reader.sha256));
  patch("normal","fixed Fejer c3dc/2efa detached-closure entry","fixed Fejer immutable-point normal entry","specific actual report CLI");
  done("normal");

  patch("leaf",parents.normal.record.sha256,outputs.normal.record.sha256,"normal fee complete source pin",true);
  assign("leaf","ACTUAL_DRIVER",JSON.stringify(deps.driver.sha256));
  assign("leaf","ACTUAL_READER",JSON.stringify(deps.reader.sha256));
  assign("leaf","ACTUAL_MODEL_SOURCE",JSON.stringify(deps.endpoint.sha256));
  assign("leaf","ACTUAL_BASE",JSON.stringify(deps.meridian.sha256));
  removeAssign("leaf","ACTUAL_TARGET");
  removeAssign("leaf","ACTUAL_CHART");
  dictionary("leaf","ACTUAL_INPUT_SOURCE_PINS",inputPins);
  patch("leaf","\n\ndef require_actions():",
    "\nACCURATE_INPUT_SOURCE = ("+JSON.stringify(names.input)+", "+JSON.stringify(outputs.input.record.sha256)+")\n\n\ndef require_actions():","strict accurate input binding source");
  patch("leaf",parents.input.record.sha256,outputs.input.record.sha256,"accurate input role complete source pin",true);
  patch("leaf",parents.radial.record.sha256,outputs.radial.record.sha256,"accurate radial role complete source pin",true);
  patch("leaf",deps.parent_seed_math_sha, deps.seed_math.sha256,"complete profile arithmetic identity",true);
  patch("leaf",deps.parent_mean_sha, deps.mean.sha256,"complete mean arithmetic identity",true);
  patch("leaf","The complete accurate input's original nine source roles changed",
    "The complete accurate input's eleven source roles changed","accurate role count wording");
  patch("leaf","6a803 literal unpack excludes exactly these complete rows",
    "552f75 literal unpack excludes exactly these complete rows","actual fixed Fejer base layout attribution");
  patch("leaf","\ndef bind_input(report_path,expected_sha,repo,files,k):",
    "\n"+additions.leaf+"\ndef bind_input(report_path,expected_sha,repo,files,k):","independent complete fixed-reference revalidation");
  patch("leaf",'\n            or actual.get("exact_fixed_target_identity_sha256")!=ACTUAL_TARGET',"","remove obsolete previous-target constant");
  patch("leaf",'    for source in actual["full_scientific_runtime_source_records"].values():',
    '    fixed_reference_scope=bind_fixed_reference_scope(actual,outer,repo,files)\n    for source in actual["full_scientific_runtime_source_records"].values():',"actual new-target scope before full leaves");
  patch("leaf",'        binding_identity=identity,actual=actual,actual_identity=actual_id,geometry=geometry,',
    '        binding_identity=identity,actual=actual,actual_identity=actual_id,geometry=geometry,\n        fixed_reference_scope=fixed_reference_scope,',"durable actual target scope");
  done("leaf");

  patch("geometry",parents.leaf.record.sha256,outputs.leaf.record.sha256,"complete leaf source pin",true);
  patch("geometry",'r.ACTUAL_TARGET','context["actual"]["exact_fixed_target_identity_sha256"]',"actual target from complete verified input",true);
  patch("geometry",'r.ACTUAL_CHART','context["actual"]["fixed_chart_core_sha256"]',"actual chart from complete verified input",true);
  patch("geometry",'    radial_xy=square_norm(v["F"][:2],k).sqrt().hi',
    '    radial_xy=square_norm(v["F"][:2],k).sqrt().hi\n    full_position_norm=square_norm(v["F"],k).sqrt().hi',"R717 same-leaf full position norm");
  patch("geometry",'        position_hull=v["F"],horizontal_position_norm_upper=radial_xy,',
    '        position_hull=v["F"],horizontal_position_norm_upper=radial_xy,\n        full_position_norm_upper=full_position_norm,\n        full_position_norm_uses_this_same_complete_leaf=True,',"whole leaf norm output scope");
  patch("geometry",'        self._maximum("horizontal_position_norm_upper",body["horizontal_position_norm_upper"],witness)',
    '        self._maximum("horizontal_position_norm_upper",body["horizontal_position_norm_upper"],witness)\n        self._maximum("full_position_norm_upper",body["full_position_norm_upper"],witness)',"aggregate all same-leaf norm bounds");
  const gdStart=active.geometry.indexOf("def derived_global_bounds(");
  const gdEnd=active.geometry.indexOf("def missing_geometric_responsibilities()",gdStart);
  if(gdStart<0||gdEnd<0)throw Error("global bounds function");
  patch("geometry",active.geometry.slice(gdStart,gdEnd),additions.diameter.trimStart()+"\n\n","R717 complete formal union diameter");
  done("geometry");

  patch("bridge",parents.geometry.record.sha256,outputs.geometry.record.sha256,"complete geometry source pin",true);
  patch("bridge",'"fixed_material_chart_identity_sha256":r.ACTUAL_CHART,',
    '"fixed_material_chart_identity_sha256":a["fixed_chart_core_sha256"],',"actual chart in complete geometry binding");
  patch("bridge",'"fixed_material_chart_identity_sha256":r.ACTUAL_CHART}',
    '"fixed_material_chart_identity_sha256":actual["fixed_chart_core_sha256"]}',"actual chart in beta evidence field");
  done("bridge");
  for(const role of Object.keys(outputs)) {
    let reverse=outputs[role].source;
    for(const p of patches.filter(x=>x.role===role).reverse()) {
      if(hash(reverse)!==p.after_sha256)throw Error("reverse after SHA "+role+" "+p.label);
      for(let i=p.positions.length-1;i>=0;i--) {
        const at=p.positions[i]+i*(p.new.length-p.old.length);
        if(reverse.slice(at,at+p.new.length)!==p.new)throw Error("reverse exact slice "+role+" "+p.label);
        reverse=reverse.slice(0,at)+p.old+reverse.slice(at+p.new.length);
      }
      if(hash(reverse)!==p.before_sha256)throw Error("reverse before SHA "+role+" "+p.label);
    }
    if(reverse!==parents[role].source)throw Error("full parent reverse "+role);
    if(/\bACTUAL_(TARGET|REFERENCE|CHART)\b/.test(outputs[role].source))throw Error("obsolete actual identity token "+role);
    if(outputs[role].source.includes("e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049")
       ||outputs[role].source.includes("90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e"))throw Error("obsolete old target literal "+role);
  }
  return {outputs,patches,names,inputPins};
}

function sha256(s) { return crypto.createHash('sha256').update(s,'utf8').digest('hex'); }
function bytes(s) { return Buffer.byteLength(s,'utf8'); }
function argument(name) {
  const i=process.argv.indexOf(name);
  if(i<0 || i+1>=process.argv.length)throw Error('Required argument '+name);
  return path.resolve(process.argv[i+1]);
}
function readComplete(directory,record) {
  const file=path.join(directory,record.name);
  const st=fs.statSync(file);
  if(!st.isFile() || st.size!==record.bytes || st.size>=100000)
    throw Error('Complete source size/type mismatch: '+record.name);
  const source=fs.readFileSync(file,'utf8');
  if(bytes(source)!==record.bytes || sha256(source)!==record.sha256)
    throw Error('Complete source byte identity mismatch: '+record.name);
  return {source,record};
}
const sourceDirectory=argument('--source-directory');
const generatedDirectory=argument('--generated-directory');
if(generatedDirectory===sourceDirectory ||
   generatedDirectory.startsWith(sourceDirectory+path.sep) ||
   fs.existsSync(generatedDirectory))
  throw Error('Use one fresh separate complete output directory');
const parents=Object.fromEntries(Object.entries(PARENTS).map(([r,v])=>[r,readComplete(sourceDirectory,v)]));
for(const v of Object.values(INPUTS))readComplete(sourceDirectory,v);
const result=buildFixedFejerFees(parents,DEPENDENCIES,ADDITIONS,sha256,bytes);
for(const [role,record] of Object.entries(OUTPUTS)) {
  const actual=result.outputs[role];
  if(!actual || actual.record.name!==record.name ||
     actual.record.bytes!==record.bytes || actual.record.sha256!==record.sha256)
    throw Error('Complete expected source mismatch: '+role);
}
for(const [role,record] of Object.entries(READY_OUTPUTS))
  if(bytes(READY_SOURCES[role])!==record.bytes || sha256(READY_SOURCES[role])!==record.sha256)
    throw Error('Complete expected ready mismatch: '+role);
fs.mkdirSync(generatedDirectory,{recursive:false});
for(const item of Object.values(result.outputs))
  fs.writeFileSync(path.join(generatedDirectory,item.record.name),item.source,{encoding:'utf8',flag:'wx'});
for(const [role,record] of Object.entries(READY_OUTPUTS))
  fs.writeFileSync(path.join(generatedDirectory,record.name),READY_SOURCES[role],{encoding:'utf8',flag:'wx'});
const record={
 schema:'complete-fixed-fejer-normal-geometry-fee-source-only-reconstruction-v1',
 complete:true,source_only:true,scientific_execution_performed:false,
 Python_AST_or_compile_performed:false,
 complete_parent_count:Object.keys(PARENTS).length,
 complete_input_source_count:Object.keys(INPUTS).length,
 complete_runtime_output_count:Object.keys(OUTPUTS).length,
 complete_ready_output_count:Object.keys(READY_OUTPUTS).length,
 complete_forward_and_reverse_source_byte_reconstruction:true,
 outputs:Object.values(OUTPUTS),ready_outputs:Object.values(READY_OUTPUTS),
 declared_patch_count:result.patches.length,
 patches:result.patches.map(({role,label,count,before_sha256,after_sha256})=>
    ({role,label,count,before_sha256,after_sha256})),
 full_exact_patch_reconstruction:'All exact changes and reverse reconstruction are implemented in this complete source; parent and output files are whole-byte pinned.',
 source_only_reproduction_is_not_a_scientific_admission_gate:true
};
fs.writeFileSync(path.join(generatedDirectory,'source-construction-record.json'),
 JSON.stringify(record,null,2)+'\n',{encoding:'utf8',flag:'wx'});
console.log(JSON.stringify({complete:true,source_only:true,scientific_execution_performed:false,
 complete_runtime_output_count:6,complete_ready_output_count:2,complete_forward_and_reverse_source_byte_reconstruction:true}));
