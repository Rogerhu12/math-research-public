// Complete literal source derivation only. This module does not import scientific Python.
import crypto from 'node:crypto';
const identity = text => ({bytes:Buffer.byteLength(text,'utf8'),sha256:crypto.createHash('sha256').update(text,'utf8').digest('hex')});
const same = (a,b) => a.bytes===b.bytes && a.sha256===b.sha256;
export const SPECS = [
 {
  "role": "envelope_transfer",
  "parent": {
   "path": "scripts/resume_20261126/radial_refined_public_reference_history_transfer.py",
   "bytes": 86470,
   "sha256": "2720bd9033391fc3f0a48afe33f50ea5843b2bf225a6596ee5a5b7077819e55c",
   "git_blob_sha": "37ce0c99b2d5aaa5b7f96a6eeac002d18ad8ec6d"
  },
  "output": {
   "name": "transfer_run10_radial_refined_material_memory.py",
   "bytes": 87074,
   "sha256": "8cd8a25830518bc29f80b22dc26e1f611e145566a7cd5fd0bf8e4f758304bb3b"
  },
  "patches": [
   {
    "old": "9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18",
    "new": "fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a",
    "count": 1
   },
   {
    "old": "306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a",
    "new": "9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209",
    "count": 1
   },
   {
    "old": "45943410994",
    "new": "45972294636",
    "count": 1
   },
   {
    "old": "public09",
    "new": "public10",
    "count": 4
   },
   {
    "old": "run09",
    "new": "run10",
    "count": 4
   },
   {
    "old": "PARENT_FAMILIES['ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5'] = {'report_schema': 'complete-run10-public-reference-analytic-frame-material-envelope-SO3-QP-v1', 'reader_sha256': 'aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32', 'reader_relative': 'scripts/resume_20261126/read_run10_public_reference_analytic_frame_so3_report_v2.py', 'operator_sha256': '3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc', 'operator_schema': 'complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1', 'memory_sha256': '2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb'}",
    "new": "PARENT_FAMILIES['ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5'] = {'report_schema': 'complete-run09-public-reference-analytic-frame-material-envelope-SO3-QP-v1', 'reader_sha256': 'aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32', 'reader_relative': 'scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py', 'operator_sha256': '3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc', 'operator_schema': 'complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1', 'memory_sha256': '2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb'}",
    "count": 1
   },
   {
    "old": "ORIGINAL_CURRENT_MEMORY_SOURCE_SHA256 = '2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb'",
    "new": "ORIGINAL_CURRENT_MEMORY_SOURCE_SHA256 = 'f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba'",
    "count": 1
   },
   {
    "old": "5b50b02aea139b81e7e1ed3cbf37c4ad8870d182c63d48bf648fb197e1cf3734",
    "new": "369105f1cdce3eaf4050fabd907a3eff9ab8cf5f0f5b274bdba5f2a37f89cbed",
    "count": 1
   },
   {
    "old": "6d8184f921e93265284c1a5396b9349d3adefd9cfbd7531cf2f4a682b33ad33a",
    "new": "043d451e34890c522de17be687306898f2f18ec8451d1814ab75730eea687071",
    "count": 1
   },
   {
    "old": "6c77349921ccfdfa765e720a330e584abba96d65c4566d9a4286df072428e716",
    "new": "e27e2f333e2a24279af84d6e015835420355b2fb446dbd56b99e99e68d40374b",
    "count": 1
   },
   {
    "old": "radial_material_address_transfer.py",
    "new": "run10_radial_material_address_transfer.py",
    "count": 1
   },
   {
    "old": "radial_refined_public_reference_memory.py",
    "new": "run10_radial_refined_material_memory.py",
    "count": 1
   },
   {
    "old": "radial_refined_public_reference_source_binding.py",
    "new": "run10_radial_source_and_report_binding.py",
    "count": 2
   },
   {
    "old": "complete_material_envelope_memory_public_reference.py",
    "new": "complete_material_envelope_memory_public_run10.py",
    "count": 1
   },
   {
    "old": "2f8de167fb0b66a9328bb7e45c2a31b0fe985678a0af7143fc1c9e965d18ec3d",
    "new": "4ace8184408aa0c7cac7970ba6fc96565c68786a518cd9d280a1a97ef82b50cf",
    "count": 1
   },
   {
    "old": "PARENT_FAMILIES['ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5'] = {'report_schema': 'complete-run09-public-reference-analytic-frame-material-envelope-SO3-QP-v1', 'reader_sha256': 'aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32', 'reader_relative': 'scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py', 'operator_sha256': '3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc', 'operator_schema': 'complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1', 'memory_sha256': '2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb'}",
    "new": "PARENT_FAMILIES['ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5'] = {'report_schema': 'complete-run09-public-reference-analytic-frame-material-envelope-SO3-QP-v1', 'reader_sha256': 'aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32', 'reader_relative': 'scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py', 'operator_sha256': '3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc', 'operator_schema': 'complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1', 'memory_sha256': '2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb'}\nPARENT_FAMILIES['c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1'] = {\"report_schema\":\"complete-run10-detached-closure-value-material-envelope-SO3-QP-v1\",\"reader_sha256\":\"2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e\",\"reader_relative\":\"scripts/resume_20261126/read_run10_detached_closure_so3_report.py\",\"operator_sha256\":\"6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4\",\"operator_schema\":\"complete-R711-reference-centred-detached-closure-values-analytic-frame-J3-normal-layer-v1\",\"memory_sha256\":\"f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba\"}\n",
    "count": 1
   },
   {
    "old": "369105f1cdce3eaf4050fabd907a3eff9ab8cf5f0f5b274bdba5f2a37f89cbed",
    "new": "7536c4b1fb9085fe03a00be5da4073065b7abb98a3b2ee7b3d14833c478af415",
    "count": 1
   }
  ]
 },
 {
  "role": "geometry",
  "parent": {
   "path": "scripts/resume_20261126/so3_radial_refined_public_reference_envelope_geometry.py",
   "bytes": 69975,
   "sha256": "2fe41a0ecc48d1404973b55dcde4cb4591bc4029fb4158740bbf5369aa869877",
   "git_blob_sha": "766c1a0ab227e4d730ce6fb67895f2b41fbbd5e4"
  },
  "output": {
   "name": "so3_run10_radial_refined_envelope_geometry.py",
   "bytes": 71804,
   "sha256": "a55a42c8d577dd4589425680c4a37eeb8e17d80de09a02215b3f424245c7f8e9"
  },
  "patches": [
   {
    "old": "0f4d380773e21c098adf2d6647fb12ba45a620dc4c92592ea22237de821ad6e9",
    "new": "7bbc3384dae0f791992835ceacdbc78ace50101ef9b5291b67d72ea2afd9425b",
    "count": 1
   },
   {
    "old": "bd1f11970897ec217edad05fd4a89eac2e5a4279508f15eb36e3d50959a38d8e",
    "new": "976f638b104c0b95233c9238eec3440baf6b31910f1a943fea99f114f2ccdbe2",
    "count": 1
   },
   {
    "old": "fab35a0c45681b352c5087297c7c47e8156674bce5616680952d0abcc253d387",
    "new": "404ecb970b37b37fd00863c52564ac1ec784c902d7f5123cc5317d77976336c9",
    "count": 1
   },
   {
    "old": "3a156cc80399c3f7c3f59ed8b01a24038e3dcdc1c7d6ac2144c140d526e656d4",
    "new": "7477da02b225834cc1f0dae147d0bca53a3b40398ee04cdf0dfc7f0217483a37",
    "count": 1
   },
   {
    "old": "c4a0160f769c5d97a102785cd8fd64cc527f2e236946901bdf0bc0a58621a178",
    "new": "cb440bfe32830f5a479e466fec8439e9bde88bfbb4160e534f899f999bac573b",
    "count": 1
   },
   {
    "old": "8591b957da548e28efb42d456f55879b5d75fa950a686aab600c2d3b00a887c5",
    "new": "ffbbddc9047b36cd308ed79df7ad4669185f61e71d85caef9a14f37b8292a40c",
    "count": 1
   },
   {
    "old": "6d8184f921e93265284c1a5396b9349d3adefd9cfbd7531cf2f4a682b33ad33a",
    "new": "043d451e34890c522de17be687306898f2f18ec8451d1814ab75730eea687071",
    "count": 1
   },
   {
    "old": "complete-public09-radial-refined-analytic-frame-envelope-world-geometry-v1",
    "new": "complete-run10-radial-refined-closure-values-envelope-world-geometry-v1",
    "count": 1
   },
   {
    "old": "complete-radial-refined-public-reference-analytic-frame-normal-plane-SO3-v1",
    "new": "complete-run10-radial-refined-detached-closure-values-analytic-frame-normal-layer-v1",
    "count": 1
   },
   {
    "old": "KEYS = ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')",
    "new": "CLOSURE_VALUE_SOURCE_SHA256 = '61368668228dc9a90b24c4e88a692c5759214add2b733fe10a882acb2ce8f6eb'\nKEYS = ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')",
    "count": 1
   },
   {
    "old": "        calibration = problem.reference_calibration",
    "new": "        closure=problem.detached_closure_values\n        closure_policy=model.get('detached_closure_value_reuse')\n        if (closure.q is not problem or closure.identity!=problem.identity\n                or closure.operator_source!=ENDPOINT_SOURCE_SHA256\n                or closure_policy!=closure.definition\n                or closure_policy.get('source_sha256')!=CLOSURE_VALUE_SOURCE_SHA256\n                or closure_policy.get('active_parameter_J_and_transpose_use_original') is not True\n                or closure_policy.get('all_32_or_declared_stages_tau_targets_domains_residuals_and_trace_retained') is not True\n                or closure_policy.get('every_stage_final_closure_reread_forces_original') is not True\n                or closure_policy.get('final_endpoint_closure_reread_forces_original') is not True\n                or closure_policy.get('exact_normal_partition_or_root_selection_changed') is not False\n                or closure_policy.get('cache_lifetime_ends_at_the_same_chain_return_or_exception') is not True):\n            raise ValueError('Only complete detached closure values may be reused inside one unchanged chain')\n        for name in ('__init__','value','scope','metadata','progress'):\n            method=getattr(closure,name)\n            if sha(method.__func__.__code__.co_filename)!=CLOSURE_VALUE_SOURCE_SHA256:\n                raise ValueError('The complete closure-value helper method differs: '+name)\n        calibration = problem.reference_calibration",
    "count": 1
   },
   {
    "old": "            operator_source_sha256=self.operator_sha256,\n",
    "new": "            operator_source_sha256=self.operator_sha256,\n            detached_closure_value_source_sha256=CLOSURE_VALUE_SOURCE_SHA256,\n            detached_closure_value_definition=closure_policy,\n            all_stage_final_and_chain_final_closures_reintegrated=True,\n            active_parameter_derivatives_bypass_closure_value_cache=True,\n",
    "count": 1
   }
  ]
 },
 {
  "role": "driver",
  "parent": {
   "path": "scripts/resume_20261126/fullclosed_radial_refined_public_reference_so3_qp.py",
   "bytes": 90333,
   "sha256": "1709eb319dcecfc1310c9c763cfb812aad56599736965b39de3790dec719aa0f",
   "git_blob_sha": "eb27c226ecd4f8c21557004f7d07b7071fe0f590"
  },
  "output": {
   "name": "fullclosed_run10_radial_refined_so3_qp.py",
   "bytes": 93101,
   "sha256": "2693abdb070cb62584abb3ffceeb525854c62d47379c9349d9047a0a365fe4e5"
  },
  "patches": [
   {
    "old": "SOURCE_PINS = {'actual_public_input_binding': ('scripts/resume_20261126/actual_public_reference_input_binding.py',\n                                 '306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a'),\n 'adjacent_matrices': ('scripts/resume_20261126/radial_refined_public_reference_adjacent_matrices.py',\n                       '3a156cc80399c3f7c3f59ed8b01a24038e3dcdc1c7d6ac2144c140d526e656d4'),\n 'analytic_J3': ('scripts/resume_20261126/radial_refined_public_reference_stage_jacobian.py',\n                 '0f4d380773e21c098adf2d6647fb12ba45a620dc4c92592ea22237de821ad6e9'),\n 'analytic_J3_binding': ('scripts/resume_20261126/radial_refined_public_reference_source_binding.py',\n                         '5b50b02aea139b81e7e1ed3cbf37c4ad8870d182c63d48bf648fb197e1cf3734'),\n 'analytic_frame': ('scripts/resume_20261126/radial_refined_public_reference_normal_frame.py',\n                    '8fb0f326356d8e94337d51bfba85068c5872453df8f08e6619f241dfe7f715ce'),\n 'analytic_parent_adjacent_matrices': ('scripts/resume_20261126/adjacent_normal_frame_matrices.py',\n                                       '955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3'),\n 'analytic_parent_driver': ('scripts/resume_20261126/fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py',\n                            '95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9'),\n 'analytic_parent_frame_C1': ('scripts/resume_20261126/normal_frame_c1_reuse.py',\n                              'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9'),\n 'analytic_parent_reader': ('scripts/resume_20261126/read_reference_centred_independent_chart_material_envelope_so3_report.py',\n                            'f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470'),\n 'analytic_parent_stage_matrices': ('scripts/resume_20261126/detached_normal_stage_matrix_reuse.py',\n                                    '375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59'),\n 'axisymmetric_seed_driver': ('scripts/resume_20261126/fullclosed_axisymmetric_so3_qp.py',\n                              '606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9'),\n 'centered': ('scripts/resume_20261126/centered_spectral_statistics.py',\n              '5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01'),\n 'deep_scalar': ('scripts/resume_20261126/deep_valley_tail_input.py',\n                 'e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'),\n 'endpoint': ('scripts/resume_20261126/so3_radial_refined_public_reference_normal_lift.py',\n              '8591b957da548e28efb42d456f55879b5d75fa950a686aab600c2d3b00a887c5'),\n 'envelope_memory': ('scripts/resume_20261126/complete_material_envelope_memory.py',\n                     'c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152'),\n 'envelope_parent_calibration': ('scripts/resume_20261126/reference_centred_c1_smooth_triangle_calibration.py',\n                                 '3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991'),\n 'envelope_parent_driver': ('scripts/resume_20261126/fullclosed_reference_centred_c1_material_envelope_so3_qp.py',\n                            'cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5'),\n 'envelope_parent_endpoint': ('scripts/resume_20261126/so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py',\n                              'a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd'),\n 'envelope_parent_geometry': ('scripts/resume_20261126/so3_reference_centred_c1_material_envelope_geometry.py',\n                              'bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f'),\n 'envelope_parent_reader': ('scripts/resume_20261126/read_reference_centred_c1_material_envelope_so3_report.py',\n                            '104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7'),\n 'envelope_rows': ('scripts/resume_20261126/complete_material_envelope_rows.py',\n                   '729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7'),\n 'envelope_transfer': ('scripts/resume_20261126/radial_refined_public_reference_history_transfer.py',\n                       '2720bd9033391fc3f0a48afe33f50ea5843b2bf225a6596ee5a5b7077819e55c'),\n 'frame_C1': ('scripts/resume_20261126/radial_refined_public_reference_frame_c1.py',\n              'bd1f11970897ec217edad05fd4a89eac2e5a4279508f15eb36e3d50959a38d8e'),\n 'frame_parent_C1': ('scripts/resume_20261126/analytic_j3_normal_frame_c1_reuse.py',\n                     '8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8'),\n 'frame_parent_J3': ('scripts/resume_20261126/analytic_normal_stage_jacobian.py',\n                     '64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d'),\n 'frame_parent_adjacent_matrices': ('scripts/resume_20261126/analytic_j3_adjacent_normal_frame_matrices.py',\n                                    '8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787'),\n 'frame_parent_calibration': ('scripts/resume_20261126/reference_centred_analytic_j3_smooth_triangle_calibration.py',\n                              '4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d'),\n 'frame_parent_driver': ('scripts/resume_20261126/fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py',\n                         '0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51'),\n 'frame_parent_endpoint': ('scripts/resume_20261126/so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py',\n                           '04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e'),\n 'frame_parent_reader': ('scripts/resume_20261126/read_reference_centred_analytic_j3_material_envelope_so3_report.py',\n                         'c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e'),\n 'frame_parent_stage_matrices': ('scripts/resume_20261126/analytic_j3_detached_normal_stage_matrix_reuse.py',\n                                 '5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1'),\n 'frozen_moment_input': ('scripts/resume_20261126/frozen_zero_moment_input.py',\n                         '4dc3e1a8ba8f128e1d05176f4d0f4b18c62d278fed603cc46f7ed686f6e4e611'),\n 'geometry': ('scripts/resume_20261126/so3_radial_refined_public_reference_envelope_geometry.py',\n              '2fe41a0ecc48d1404973b55dcde4cb4591bc4029fb4158740bbf5369aa869877'),\n 'geometry_selector': ('scripts/resume_20261120/fullclosed_point_inequalities_v2.py',\n                       'e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8'),\n 'hessian': ('scripts/resume_20261120/positive_spectral_gram_hessian.py',\n             '29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4'),\n 'history': ('scripts/resume_20261120/launch_refinement_from_full_report.py',\n             '4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'),\n 'hold': ('scripts/parallel_20261117_negative_hold_profile_ivp.py',\n          'ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1'),\n 'independent_envelope_memory': ('scripts/resume_20261126/radial_refined_public_reference_memory.py',\n                                 '6d8184f921e93265284c1a5396b9349d3adefd9cfbd7531cf2f4a682b33ad33a'),\n 'independent_input_projection_producer': ('scripts/resume_20261126/freeze_run09_public_reference_and_restore_run05_carrier.py',\n                                           '9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18'),\n 'integer': ('notes/2026-11-17-parallel-inward-integral-enclosure.py',\n             'babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0'),\n 'meridian': ('scripts/resume_20261126/so3_radial_refined_public_reference_meridian_operator.py',\n              '130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0'),\n 'moment_initial_binding': ('scripts/resume_20261126/diagnose_zero_initial_chord.py',\n                            '65787b3e51f80505f5619c35fb05f8ad064e88de111578ff53e8bdad442092c0'),\n 'moment_original_driver': ('scripts/resume_20261126/fullclosed_zero_closure_so3_qp.py',\n                            'b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b'),\n 'moment_original_endpoint': ('scripts/resume_20261126/so3_zero_closure_endpoint_operator.py',\n                              '5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46'),\n 'moment_trace_source': ('scripts/resume_20261126/trace_zero_initial_endpoint_failure.py',\n                         '73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54'),\n 'new_moment_input': ('scripts/resume_20261126/radial_refined_public_reference_literal_zero_moment_input.py',\n                      '59033328b5cdfd3de96026cd860bcab71d598dee4fce774c08f9c299eea2b652'),\n 'observed': ('scripts/resume_20261120/gauss_observed_closed_gram.py',\n              '26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d'),\n 'pure_geometry': ('scripts/resume_20261120_curvature_qp.py',\n                   'a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854'),\n 'qp': ('scripts/resume_20261120/fullspace_feasible_active_cg_v3.py',\n        'fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4'),\n 'radial_address_transfer': ('scripts/resume_20261126/radial_material_address_transfer.py',\n                             '6c77349921ccfdfa765e720a330e584abba96d65c4566d9a4286df072428e716'),\n 'radial_affine_reference': ('scripts/resume_20261126/exact_affine_supported_reference.py',\n                             '2d1f02119c019b298caf8f7877ab3c9ba9cd0feff85155d095e00bce7394d117'),\n 'radial_layout': ('scripts/resume_20261126/radial_bisection_layout.py',\n                   'cf5bb90fa59ea1e1662095a317260f68d2568e33f941e0d6750e9c490053b744'),\n 'radial_observations': ('scripts/resume_20261126/complete_dyadic_radial_observations.py',\n                         '2e2031901477dad98db1e97d5d5fcf9fd0815e537cf1dba01ad0d18e95d67b74'),\n 'radial_parent_adjacent_matrices': ('scripts/resume_20261126/analytic_frame_adjacent_normal_matrices.py',\n                                     '3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695'),\n 'radial_parent_analytic_J3': ('scripts/resume_20261126/analytic_frame_local_stage_jacobian.py',\n                               '894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866'),\n 'radial_parent_analytic_J3_binding': ('scripts/resume_20261126/run09_public_reference_analytic_frame_binding.py',\n                                       '15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592'),\n 'radial_parent_analytic_frame': ('scripts/resume_20261126/analytic_normal_frame_jets.py',\n                                  '4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8'),\n 'radial_parent_driver': ('scripts/resume_20261126/fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py',\n                          'ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5'),\n 'radial_parent_endpoint': ('scripts/resume_20261126/so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py',\n                            '3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc'),\n 'radial_parent_envelope_transfer': ('scripts/resume_20261126/transfer_run09_public_reference_analytic_frame_memory.py',\n                                     '6deeeaa1dcbbb0fbfd968d0b31443798909536a55a7ea498f661e08496a27707'),\n 'radial_parent_frame_C1': ('scripts/resume_20261126/analytic_frame_c1_reuse.py',\n                            'f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb'),\n 'radial_parent_geometry': ('scripts/resume_20261126/so3_run09_public_reference_analytic_frame_geometry_v2.py',\n                            'e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13'),\n 'radial_parent_memory': ('scripts/resume_20261126/complete_material_envelope_memory_public_reference.py',\n                          '2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb'),\n 'radial_parent_meridian': ('scripts/resume_20261126/so3_supported_smooth_triangle_meridian_operator.py',\n                            '6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865'),\n 'radial_parent_new_moment_input': ('scripts/resume_20261126/supported_smooth_triangle_literal_zero_moment_input.py',\n                                    '307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7'),\n 'radial_parent_reader': ('scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py',\n                          'aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32'),\n 'radial_parent_reference_calibration': ('scripts/resume_20261126/reference_centred_analytic_frame_smooth_triangle_calibration.py',\n                                         'fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0'),\n 'radial_parent_root_packets': ('scripts/resume_20261126/immutable_analytic_frame_normal_root_packets.py',\n                                '094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0'),\n 'radial_parent_stage_matrices': ('scripts/resume_20261126/analytic_frame_detached_normal_stage_matrix_reuse.py',\n                                  'fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255'),\n 'reference': ('scripts/resume_20261126/so3_axisymmetric_reference.py',\n               '4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'),\n 'reference_calibration': ('scripts/resume_20261126/radial_refined_public_reference_calibration.py',\n                           'c4a0160f769c5d97a102785cd8fd64cc527f2e236946901bdf0bc0a58621a178'),\n 'root_packets': ('scripts/resume_20261126/immutable_radial_refined_public_reference_root_packets.py',\n                  '8d2b93dd055cc600aac14183d060d101421a924590c1fe8300625931bc8c0403'),\n 'scalar': ('notes/2026-11-17-parallel-model-full-hold-oracle.py',\n            'a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670'),\n 'seed_mean': ('scripts/resume_20261126/supported_smooth_triangle_seed_mean_jets.py',\n               'f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917'),\n 'seed_reference': ('scripts/resume_20261126/supported_smooth_triangle_meridian_reference.py',\n                    '0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b'),\n 'spectral': ('scripts/resume_20261120/positive_spectral_gram_weights.py',\n              'e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91'),\n 'stage_matrices': ('scripts/resume_20261126/radial_refined_public_reference_stage_matrices.py',\n                    'fab35a0c45681b352c5087297c7c47e8156674bce5616680952d0abcc253d387'),\n 'warm_producer': ('notes/2026-11-17-parallel-model-fullclosed-hold-warm.py',\n                   'bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3')}",
    "new": "SOURCE_PINS = {\n    \"actual_public_input_binding\": (\"scripts/resume_20261126/actual_public_run10_reference_input_binding.py\", \"9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209\"),\n    \"adjacent_matrices\": (\"scripts/resume_20261126/run10_radial_adjacent_normal_matrices.py\", \"7477da02b225834cc1f0dae147d0bca53a3b40398ee04cdf0dfc7f0217483a37\"),\n    \"analytic_frame\": (\"scripts/resume_20261126/run10_radial_analytic_normal_frame.py\", \"945b66100801058d311f215c9453efa35a9cbb3edf031dc1b10da0140f9567f2\"),\n    \"analytic_J3\": (\"scripts/resume_20261126/run10_radial_analytic_stage_jacobian.py\", \"7bbc3384dae0f791992835ceacdbc78ace50101ef9b5291b67d72ea2afd9425b\"),\n    \"analytic_J3_binding\": (\"scripts/resume_20261126/run10_radial_source_and_report_binding.py\", \"369105f1cdce3eaf4050fabd907a3eff9ab8cf5f0f5b274bdba5f2a37f89cbed\"),\n    \"analytic_parent_adjacent_matrices\": (\"scripts/resume_20261126/adjacent_normal_frame_matrices.py\", \"955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3\"),\n    \"analytic_parent_driver\": (\"scripts/resume_20261126/fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py\", \"95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9\"),\n    \"analytic_parent_frame_C1\": (\"scripts/resume_20261126/normal_frame_c1_reuse.py\", \"ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9\"),\n    \"analytic_parent_reader\": (\"scripts/resume_20261126/read_reference_centred_independent_chart_material_envelope_so3_report.py\", \"f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470\"),\n    \"analytic_parent_stage_matrices\": (\"scripts/resume_20261126/detached_normal_stage_matrix_reuse.py\", \"375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59\"),\n    \"axisymmetric_seed_driver\": (\"scripts/resume_20261126/fullclosed_axisymmetric_so3_qp.py\", \"606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9\"),\n    \"centered\": (\"scripts/resume_20261126/centered_spectral_statistics.py\", \"5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01\"),\n    \"closure_values\": (\"scripts/resume_20261126/run10_radial_detached_closure_values.py\", \"61368668228dc9a90b24c4e88a692c5759214add2b733fe10a882acb2ce8f6eb\"),\n    \"deep_scalar\": (\"scripts/resume_20261126/deep_valley_tail_input.py\", \"e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2\"),\n    \"endpoint\": (\"scripts/resume_20261126/so3_run10_radial_refined_closure_normal_lift.py\", \"ffbbddc9047b36cd308ed79df7ad4669185f61e71d85caef9a14f37b8292a40c\"),\n    \"envelope_memory\": (\"scripts/resume_20261126/complete_material_envelope_memory.py\", \"c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152\"),\n    \"envelope_parent_calibration\": (\"scripts/resume_20261126/reference_centred_c1_smooth_triangle_calibration.py\", \"3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991\"),\n    \"envelope_parent_driver\": (\"scripts/resume_20261126/fullclosed_reference_centred_c1_material_envelope_so3_qp.py\", \"cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5\"),\n    \"envelope_parent_endpoint\": (\"scripts/resume_20261126/so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py\", \"a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd\"),\n    \"envelope_parent_geometry\": (\"scripts/resume_20261126/so3_reference_centred_c1_material_envelope_geometry.py\", \"bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f\"),\n    \"envelope_parent_reader\": (\"scripts/resume_20261126/read_reference_centred_c1_material_envelope_so3_report.py\", \"104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7\"),\n    \"envelope_rows\": (\"scripts/resume_20261126/complete_material_envelope_rows.py\", \"729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7\"),\n    \"envelope_transfer\": (\"scripts/resume_20261126/transfer_run10_radial_refined_material_memory.py\", \"d4adb028d64a5b354db7682a25de495c50148713f4713acbc3c7cf917423b7b5\"),\n    \"frame_C1\": (\"scripts/resume_20261126/run10_radial_normal_frame_c1.py\", \"976f638b104c0b95233c9238eec3440baf6b31910f1a943fea99f114f2ccdbe2\"),\n    \"frame_parent_adjacent_matrices\": (\"scripts/resume_20261126/analytic_j3_adjacent_normal_frame_matrices.py\", \"8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787\"),\n    \"frame_parent_C1\": (\"scripts/resume_20261126/analytic_j3_normal_frame_c1_reuse.py\", \"8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8\"),\n    \"frame_parent_calibration\": (\"scripts/resume_20261126/reference_centred_analytic_j3_smooth_triangle_calibration.py\", \"4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d\"),\n    \"frame_parent_driver\": (\"scripts/resume_20261126/fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py\", \"0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51\"),\n    \"frame_parent_endpoint\": (\"scripts/resume_20261126/so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py\", \"04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e\"),\n    \"frame_parent_J3\": (\"scripts/resume_20261126/analytic_normal_stage_jacobian.py\", \"64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d\"),\n    \"frame_parent_reader\": (\"scripts/resume_20261126/read_reference_centred_analytic_j3_material_envelope_so3_report.py\", \"c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e\"),\n    \"frame_parent_stage_matrices\": (\"scripts/resume_20261126/analytic_j3_detached_normal_stage_matrix_reuse.py\", \"5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1\"),\n    \"frozen_moment_input\": (\"scripts/resume_20261126/frozen_zero_moment_input.py\", \"4dc3e1a8ba8f128e1d05176f4d0f4b18c62d278fed603cc46f7ed686f6e4e611\"),\n    \"geometry\": (\"scripts/resume_20261126/so3_run10_radial_refined_envelope_geometry.py\", \"a55a42c8d577dd4589425680c4a37eeb8e17d80de09a02215b3f424245c7f8e9\"),\n    \"geometry_selector\": (\"scripts/resume_20261120/fullclosed_point_inequalities_v2.py\", \"e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8\"),\n    \"hessian\": (\"scripts/resume_20261120/positive_spectral_gram_hessian.py\", \"29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4\"),\n    \"history\": (\"scripts/resume_20261120/launch_refinement_from_full_report.py\", \"4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60\"),\n    \"hold\": (\"scripts/parallel_20261117_negative_hold_profile_ivp.py\", \"ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1\"),\n    \"independent_envelope_memory\": (\"scripts/resume_20261126/run10_radial_refined_material_memory.py\", \"043d451e34890c522de17be687306898f2f18ec8451d1814ab75730eea687071\"),\n    \"independent_input_projection_producer\": (\"scripts/resume_20261126/freeze_run10_public_reference_and_restore_run05_carrier.py\", \"fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a\"),\n    \"integer\": (\"notes/2026-11-17-parallel-inward-integral-enclosure.py\", \"babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0\"),\n    \"meridian\": (\"scripts/resume_20261126/so3_radial_refined_public_reference_meridian_operator.py\", \"130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0\"),\n    \"moment_initial_binding\": (\"scripts/resume_20261126/diagnose_zero_initial_chord.py\", \"65787b3e51f80505f5619c35fb05f8ad064e88de111578ff53e8bdad442092c0\"),\n    \"moment_original_driver\": (\"scripts/resume_20261126/fullclosed_zero_closure_so3_qp.py\", \"b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b\"),\n    \"moment_original_endpoint\": (\"scripts/resume_20261126/so3_zero_closure_endpoint_operator.py\", \"5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46\"),\n    \"moment_trace_source\": (\"scripts/resume_20261126/trace_zero_initial_endpoint_failure.py\", \"73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54\"),\n    \"new_moment_input\": (\"scripts/resume_20261126/radial_refined_public_reference_literal_zero_moment_input.py\", \"59033328b5cdfd3de96026cd860bcab71d598dee4fce774c08f9c299eea2b652\"),\n    \"observed\": (\"scripts/resume_20261120/gauss_observed_closed_gram.py\", \"26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d\"),\n    \"pure_geometry\": (\"scripts/resume_20261120_curvature_qp.py\", \"a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854\"),\n    \"qp\": (\"scripts/resume_20261120/fullspace_feasible_active_cg_v3.py\", \"fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4\"),\n    \"radial_address_transfer\": (\"scripts/resume_20261126/run10_radial_material_address_transfer.py\", \"e27e2f333e2a24279af84d6e015835420355b2fb446dbd56b99e99e68d40374b\"),\n    \"radial_affine_reference\": (\"scripts/resume_20261126/exact_affine_supported_reference.py\", \"2d1f02119c019b298caf8f7877ab3c9ba9cd0feff85155d095e00bce7394d117\"),\n    \"radial_layout\": (\"scripts/resume_20261126/radial_bisection_layout.py\", \"cf5bb90fa59ea1e1662095a317260f68d2568e33f941e0d6750e9c490053b744\"),\n    \"radial_observations\": (\"scripts/resume_20261126/complete_dyadic_radial_observations.py\", \"2e2031901477dad98db1e97d5d5fcf9fd0815e537cf1dba01ad0d18e95d67b74\"),\n    \"radial_parent_adjacent_matrices\": (\"scripts/resume_20261126/analytic_frame_adjacent_normal_matrices.py\", \"3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695\"),\n    \"radial_parent_analytic_frame\": (\"scripts/resume_20261126/analytic_normal_frame_jets.py\", \"4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8\"),\n    \"radial_parent_analytic_J3\": (\"scripts/resume_20261126/analytic_frame_local_stage_jacobian.py\", \"894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866\"),\n    \"radial_parent_analytic_J3_binding\": (\"scripts/resume_20261126/run09_public_reference_analytic_frame_binding.py\", \"15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592\"),\n    \"radial_parent_driver\": (\"scripts/resume_20261126/fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py\", \"ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5\"),\n    \"radial_parent_endpoint\": (\"scripts/resume_20261126/so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py\", \"3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc\"),\n    \"radial_parent_envelope_transfer\": (\"scripts/resume_20261126/transfer_run09_public_reference_analytic_frame_memory.py\", \"6deeeaa1dcbbb0fbfd968d0b31443798909536a55a7ea498f661e08496a27707\"),\n    \"radial_parent_frame_C1\": (\"scripts/resume_20261126/analytic_frame_c1_reuse.py\", \"f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb\"),\n    \"radial_parent_geometry\": (\"scripts/resume_20261126/so3_run09_public_reference_analytic_frame_geometry_v2.py\", \"e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13\"),\n    \"radial_parent_memory\": (\"scripts/resume_20261126/complete_material_envelope_memory_public_reference.py\", \"2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb\"),\n    \"radial_parent_meridian\": (\"scripts/resume_20261126/so3_supported_smooth_triangle_meridian_operator.py\", \"6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865\"),\n    \"radial_parent_new_moment_input\": (\"scripts/resume_20261126/supported_smooth_triangle_literal_zero_moment_input.py\", \"307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7\"),\n    \"radial_parent_reader\": (\"scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py\", \"aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32\"),\n    \"radial_parent_reference_calibration\": (\"scripts/resume_20261126/reference_centred_analytic_frame_smooth_triangle_calibration.py\", \"fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0\"),\n    \"radial_parent_root_packets\": (\"scripts/resume_20261126/immutable_analytic_frame_normal_root_packets.py\", \"094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0\"),\n    \"radial_parent_stage_matrices\": (\"scripts/resume_20261126/analytic_frame_detached_normal_stage_matrix_reuse.py\", \"fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255\"),\n    \"reference\": (\"scripts/resume_20261126/so3_axisymmetric_reference.py\", \"4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3\"),\n    \"reference_calibration\": (\"scripts/resume_20261126/run10_radial_reference_calibration.py\", \"cb440bfe32830f5a479e466fec8439e9bde88bfbb4160e534f899f999bac573b\"),\n    \"root_packets\": (\"scripts/resume_20261126/immutable_run10_radial_normal_root_packets.py\", \"fa9f50d318af9ec268ce391b6ba16d8eb971d88ad519ae79c8ba3c661806f528\"),\n    \"run10_parent_adjacent_matrices\": (\"scripts/resume_20261126/adjacent_normal_matrices_closure_values.py\", \"6efb1b4de61635bb4121b2cc05daf4b817ecfb772f302568e2a570b7fa16b650\"),\n    \"run10_parent_analytic_frame\": (\"scripts/resume_20261126/analytic_normal_frame_jets_closure_values.py\", \"8239fc8f3588afd4f93ba10368c599a85652d3b350a088b1397731c196258598\"),\n    \"run10_parent_analytic_J3\": (\"scripts/resume_20261126/analytic_local_stage_jacobian_closure_values.py\", \"9646c1cb1e239f4625dfaa0f13e0d0776dfd9684401789a089326e177c02a5aa\"),\n    \"run10_parent_analytic_J3_binding\": (\"scripts/resume_20261126/run10_detached_closure_value_binding.py\", \"dc3b40645eb47f924392a703eb65e3fda982f43804b1861f89da1c038e9140a1\"),\n    \"run10_parent_closure_parent_actual_public_input_binding\": (\"scripts/resume_20261126/actual_public_reference_input_binding.py\", \"306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a\"),\n    \"run10_parent_closure_parent_independent_input_projection_producer\": (\"scripts/resume_20261126/freeze_run09_public_reference_and_restore_run05_carrier.py\", \"9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18\"),\n    \"run10_parent_closure_values\": (\"scripts/resume_20261126/same_chain_detached_closure_values.py\", \"e1af4fc8cfecbd30ab5cf9f7ded31d6a7a8d11385a8558cc76cbb8a8b1851e9e\"),\n    \"run10_parent_driver\": (\"scripts/resume_20261126/fullclosed_run10_detached_closure_so3_qp.py\", \"c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1\"),\n    \"run10_parent_endpoint\": (\"scripts/resume_20261126/so3_reference_centred_closure_values_normal_lift_operator.py\", \"6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4\"),\n    \"run10_parent_envelope_transfer\": (\"scripts/resume_20261126/transfer_run10_detached_closure_memory.py\", \"eca323b12ff941736798f7e40021f78b92e1b23cee8a7edcdcc5e3f6db7508fe\"),\n    \"run10_parent_frame_C1\": (\"scripts/resume_20261126/normal_frame_c1_closure_values.py\", \"1f80ce726f9cf9424740331eb54a5cafa86a058ca2b048ee5fb6add5fc371caa\"),\n    \"run10_parent_geometry\": (\"scripts/resume_20261126/so3_run10_detached_closure_geometry.py\", \"6c676d4302f4271310ffca899ca8820fe43f2d792ee9a634747f25eecf9f6528\"),\n    \"run10_parent_independent_envelope_memory\": (\"scripts/resume_20261126/complete_material_envelope_memory_public_run10.py\", \"f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba\"),\n    \"run10_parent_reader\": (\"scripts/resume_20261126/read_run10_detached_closure_so3_report.py\", \"2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e\"),\n    \"run10_parent_reference_calibration\": (\"scripts/resume_20261126/reference_centred_closure_values_calibration.py\", \"b59776d52653f036590b619124579a20400d3bb7a4de8117d3221ca32bec144f\"),\n    \"run10_parent_root_packets\": (\"scripts/resume_20261126/immutable_closure_values_normal_root_packets.py\", \"31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805\"),\n    \"run10_parent_stage_matrices\": (\"scripts/resume_20261126/detached_stage_matrices_closure_values.py\", \"bf80cc8bbcf442d07d0e9225e1fbf703be4c40b951f10fb20e861e1ec7497c45\"),\n    \"scalar\": (\"notes/2026-11-17-parallel-model-full-hold-oracle.py\", \"a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670\"),\n    \"seed_mean\": (\"scripts/resume_20261126/supported_smooth_triangle_seed_mean_jets.py\", \"f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917\"),\n    \"seed_reference\": (\"scripts/resume_20261126/supported_smooth_triangle_meridian_reference.py\", \"0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b\"),\n    \"spectral\": (\"scripts/resume_20261120/positive_spectral_gram_weights.py\", \"e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91\"),\n    \"stage_matrices\": (\"scripts/resume_20261126/run10_radial_detached_stage_matrices.py\", \"404ecb970b37b37fd00863c52564ac1ec784c902d7f5123cc5317d77976336c9\"),\n    \"warm_producer\": (\"notes/2026-11-17-parallel-model-fullclosed-hold-warm.py\", \"bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3\"),\n}",
    "count": 1
   },
   {
    "old": "complete-public09-J1845-analytic-frame-material-envelope-SO3-QP-v1",
    "new": "complete-run10-J1845-detached-closure-values-material-envelope-SO3-QP-v1",
    "count": 1
   },
   {
    "old": "actual-radial-refined-public-reference-analytic-frame-snapshot-v1",
    "new": "actual-run10-radial-refined-closure-values-normal-snapshot-v1",
    "count": 1
   },
   {
    "old": "ROOT_SNAPSHOT_KEYS = ('current_full_point_sha256', 'endpoint_root_policy', 'normal_stage_count', 'exact_normal_step_nodes', 'actual_normal_step_carriers_binary64_hex', 'common_partition_for_all_angles_and_free_points', 'per_angle_adaptive_normal_partition', 'current_cached_angle_roots', 'current_all_grid_angle_roots_available', 'current_all_grid_second_angular_jets_available', 'current_maximum_endpoint_residual', 'current_maximum_dimensionless_control_norm', 'current_maximum_physical_z_norm', 'current_maximum_gamma_axis_norm', 'current_maximum_first_angular_endpoint_residual', 'current_maximum_second_angular_endpoint_residual', 'endpoint_counts', 'actual_normal_counts', 'last_root_failure', 'normal_lift_last_summary', 'numerical_Newton_iterations_differentiated', 'complete_uniform_IFT_conditions_verified', 'complete_continuous_root_branch_certified', 'endpoint_root_error_enclosed', 'stationary_KKT_selection_used', 'continuous_horizontal_ODE_solution_claimed', 'final_implicit_J_uses_all_normal_stage_equations', 'previous_normal_frame_full_parameter_chain_retained', 'original_zero_control_target_full_parameter_chain_retained', 'implicit_control_dimension', 'normal_increment_dimension', 'implicit_dimension_per_stage', 'complete_first_angular_implicit_dimension', 'complete_second_angular_implicit_dimension', 'current_reference_calibration', 'analytic_stage_jacobian', 'analytic_normal_frame')",
    "new": "ROOT_SNAPSHOT_KEYS = ('current_full_point_sha256', 'endpoint_root_policy', 'normal_stage_count', 'exact_normal_step_nodes', 'actual_normal_step_carriers_binary64_hex', 'common_partition_for_all_angles_and_free_points', 'per_angle_adaptive_normal_partition', 'current_cached_angle_roots', 'current_all_grid_angle_roots_available', 'current_all_grid_second_angular_jets_available', 'current_maximum_endpoint_residual', 'current_maximum_dimensionless_control_norm', 'current_maximum_physical_z_norm', 'current_maximum_gamma_axis_norm', 'current_maximum_first_angular_endpoint_residual', 'current_maximum_second_angular_endpoint_residual', 'endpoint_counts', 'actual_normal_counts', 'last_root_failure', 'normal_lift_last_summary', 'numerical_Newton_iterations_differentiated', 'complete_uniform_IFT_conditions_verified', 'complete_continuous_root_branch_certified', 'endpoint_root_error_enclosed', 'stationary_KKT_selection_used', 'continuous_horizontal_ODE_solution_claimed', 'final_implicit_J_uses_all_normal_stage_equations', 'previous_normal_frame_full_parameter_chain_retained', 'original_zero_control_target_full_parameter_chain_retained', 'implicit_control_dimension', 'normal_increment_dimension', 'implicit_dimension_per_stage', 'complete_first_angular_implicit_dimension', 'complete_second_angular_implicit_dimension', 'current_reference_calibration', 'analytic_stage_jacobian', 'analytic_normal_frame', 'detached_closure_value_reuse')",
    "count": 1
   },
   {
    "old": "_actual_run09_public_reference_scope",
    "new": "_actual_run10_public_reference_scope",
    "count": 1
   },
   {
    "old": "run09_input_binding",
    "new": "run10_input_binding",
    "count": 2
   },
   {
    "old": "bind_actual_run09_input",
    "new": "bind_actual_run10_input",
    "count": 1
   },
   {
    "old": "The whole actually returned run09 input binding is required",
    "new": "The whole actually returned run10 input binding is required",
    "count": 1
   },
   {
    "old": "# Every current run09 path",
    "new": "# Every current run10 path",
    "count": 1
   },
   {
    "old": "    stage_matrices = load('_actual_complete_detached_stage_matrices',paths['stage_matrices'])",
    "new": "    closure_values = load('_actual_complete_same_chain_closure_values',paths['closure_values'])\n    stage_matrices = load('_actual_complete_detached_stage_matrices',paths['stage_matrices'])",
    "count": 1
   },
   {
    "old": "        analytic_frame_module=analytic_frame)\n",
    "new": "        analytic_frame_module=analytic_frame,closure_value_module=closure_values,\n        evaluation_progress_path=args.outdir/'actual-normal-evaluation-progress.json')\n",
    "count": 1
   },
   {
    "old": "        adjacent_matrix_rounding_is_independent=",
    "new": "        detached_closure_value_reuse_definition=q.detached_closure_values.definition,\n        detached_closure_value_source=file_record(paths['closure_values']),\n        closure_value_all_final_original_equation_checks_retained=True,\n        closure_value_active_J_and_transpose_use_original=True,\n        closure_value_speedup_rounding_or_root_certificate=False,\n        actual_evaluation_progress_path=str(args.outdir/'actual-normal-evaluation-progress.json'),\n        evaluation_progress_is_mutable_observation_not_scientific_input=True,\n        adjacent_matrix_rounding_is_independent=",
    "count": 1
   },
   {
    "old": "    try:\n        native = q.residual(x)\n        current = statistics(x, native)\n        geometry = scan(x)\n",
    "new": "    try:\n        q.detached_closure_values.progress('initial-complete-residual-start',force=True)\n        native = q.residual(x)\n        q.detached_closure_values.progress('initial-complete-residual-returned',force=True)\n        q.detached_closure_values.progress('initial-complete-statistics-start',force=True)\n        current = statistics(x, native)\n        q.detached_closure_values.progress('initial-complete-statistics-returned',force=True)\n        q.detached_closure_values.progress('initial-complete-geometry-start',force=True)\n        geometry = scan(x)\n        q.detached_closure_values.progress('initial-complete-geometry-returned',force=True)\n",
    "count": 1
   },
   {
    "old": "369105f1cdce3eaf4050fabd907a3eff9ab8cf5f0f5b274bdba5f2a37f89cbed",
    "new": "7536c4b1fb9085fe03a00be5da4073065b7abb98a3b2ee7b3d14833c478af415",
    "count": 1
   },
   {
    "old": "d4adb028d64a5b354db7682a25de495c50148713f4713acbc3c7cf917423b7b5",
    "new": "8cd8a25830518bc29f80b22dc26e1f611e145566a7cd5fd0bf8e4f758304bb3b",
    "count": 1
   }
  ]
 },
 {
  "role": "launcher",
  "parent": {
   "path": "scripts/resume_20261126/launch_radial_refined_public_reference_so3_actions.py",
   "bytes": 22323,
   "sha256": "2658b074a61afa32305703def009e71c8aa99836036a6b756508e6305a7770ec",
   "git_blob_sha": "c7ca4d4ae12868383c7cfef0e06404b485149a04"
  },
  "output": {
   "name": "launch_run10_radial_refined_actions.py",
   "bytes": 22614,
   "sha256": "b71588c0323c96970abedbe1b495429295f4bd44de01b921486123b6cfbf861e"
  },
  "patches": [
   {
    "old": "1709eb319dcecfc1310c9c763cfb812aad56599736965b39de3790dec719aa0f",
    "new": "2693abdb070cb62584abb3ffceeb525854c62d47379c9349d9047a0a365fe4e5",
    "count": 1
   },
   {
    "old": "fullclosed_radial_refined_public_reference_so3_qp.py",
    "new": "fullclosed_run10_radial_refined_so3_qp.py",
    "count": 1
   },
   {
    "old": "public-actions-complete-public09-J1845-SO3-command-v1",
    "new": "public-actions-complete-run10-J1845-closure-values-SO3-command-v1",
    "count": 1
   },
   {
    "old": "        measured_cache_hit_rate_or_speedup_claimed=False,\n",
    "new": "        measured_cache_hit_rate_or_speedup_claimed=False,\n        detached_closure_value_source_sha256=records['closure_values']['sha256'],\n        all_stage_and_chain_final_equations_reread_by_original_formula=True,\n        active_J_and_transpose_bypass_closure_value_cache=True,\n        mutable_progress_file_is_not_immutable_root_evidence=True,\n",
    "count": 1
   }
  ]
 },
 {
  "role": "reader",
  "parent": {
   "path": "scripts/resume_20261126/read_radial_refined_public_reference_so3_report.py",
   "bytes": 97634,
   "sha256": "c344478b6dbb0df0dfa80e924b6ef6a739d79460ab3094a16f23b8b33bdb2695",
   "git_blob_sha": "0a9cc0cd223ea00f46cfbff775a739616fe9c990"
  },
  "output": {
   "name": "read_run10_radial_refined_so3_report.py",
   "bytes": 97943,
   "sha256": "64e92ed8b48f753e9988221c2c1f91513ed2e468e6fff3ce9cc83096c4bad8e4"
  },
  "patches": [
   {
    "old": "import sys\n",
    "new": "import sys\nimport textwrap\n",
    "count": 1
   },
   {
    "old": "def read_frame_reuse_policy(path):\n    \"\"\"Evaluate only three explicitly selected stdlib policy/shape functions.\"\"\"\n    tree = ast.parse(Path(path).read_text())\n    names = {'SCHEMA','ORIGINAL_CENTERED_SOURCE','METHOD_AST','ANALYTIC_STAGE_SOURCE_SHA256'}\n    functions = {'sha','definition','_new_counts'}\n    body = []\n    seen_names,seen_functions = set(),set()\n    for node in tree.body:\n        if isinstance(node,ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0],ast.Name):\n            name = node.targets[0].id\n            if name in names:\n                ast.literal_eval(node.value)\n                body.append(node)\n                seen_names.add(name)\n        if isinstance(node,ast.FunctionDef) and node.name in functions:\n            body.append(node)\n            seen_functions.add(node.name)\n    if seen_names != names or seen_functions != functions:\n        raise ValueError('The complete source-bound C1 policy is not independently readable')\n    namespace = {'Path':Path,'hashlib':hashlib,'__file__':str(path)}\n    exec(compile(ast.Module(body=body,type_ignores=[]),'<bound pure C1 policy>','exec'),namespace)\n    return namespace['definition'](),set(namespace['_new_counts']())\n\n",
    "new": "def read_frame_reuse_policy(path):\n    \"\"\"Evaluate the complete explicitly source-bound pure C1 policy and AST overrides.\"\"\"\n    tree = ast.parse(Path(path).read_text())\n    names = {'SCHEMA','ORIGINAL_CENTERED_SOURCE','METHOD_AST','ANALYTIC_STAGE_SOURCE_SHA256',\n        'METHOD_SOURCE_OVERRIDES','CLOSURE_VALUE_SOURCE_SHA256'}\n    functions = {'sha','definition','_new_counts','canonical','_ast_value','complete_method_ast'}\n    body = []\n    seen_names,seen_functions = set(),set()\n    for node in tree.body:\n        if isinstance(node,ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0],ast.Name):\n            name = node.targets[0].id\n            if name in names:\n                ast.literal_eval(node.value)\n                body.append(node)\n                seen_names.add(name)\n        if isinstance(node,ast.FunctionDef) and node.name in functions:\n            body.append(node)\n            seen_functions.add(node.name)\n    if seen_names != names or seen_functions != functions:\n        raise ValueError('The complete source-bound C1 policy is not independently readable')\n    namespace = dict(Path=Path,hashlib=hashlib,json=json,math=math,ast=ast,textwrap=textwrap,__file__=str(path))\n    exec(compile(ast.Module(body=body,type_ignores=[]),'<bound pure C1 policy>','exec'),namespace)\n    return namespace['definition'](),set(namespace['_new_counts']())\n\n",
    "count": 1
   },
   {
    "old": "1709eb319dcecfc1310c9c763cfb812aad56599736965b39de3790dec719aa0f",
    "new": "2693abdb070cb62584abb3ffceeb525854c62d47379c9349d9047a0a365fe4e5",
    "count": 1
   },
   {
    "old": "fullclosed_radial_refined_public_reference_so3_qp.py",
    "new": "fullclosed_run10_radial_refined_so3_qp.py",
    "count": 1
   },
   {
    "old": "complete-public09-J1845-analytic-frame-material-envelope-SO3-QP-v1",
    "new": "complete-run10-J1845-detached-closure-values-material-envelope-SO3-QP-v1",
    "count": 1
   },
   {
    "old": "complete-radial-refined-public-reference-analytic-frame-normal-plane-SO3-v1",
    "new": "complete-run10-radial-refined-detached-closure-values-analytic-frame-normal-layer-v1",
    "count": 1
   },
   {
    "old": "actual-radial-refined-public-reference-analytic-frame-snapshot-v1",
    "new": "actual-run10-radial-refined-closure-values-normal-snapshot-v1",
    "count": 1
   },
   {
    "old": "ROOT_SNAPSHOT_KEYS = ('current_full_point_sha256', 'endpoint_root_policy', 'normal_stage_count', 'exact_normal_step_nodes', 'actual_normal_step_carriers_binary64_hex', 'common_partition_for_all_angles_and_free_points', 'per_angle_adaptive_normal_partition', 'current_cached_angle_roots', 'current_all_grid_angle_roots_available', 'current_all_grid_second_angular_jets_available', 'current_maximum_endpoint_residual', 'current_maximum_dimensionless_control_norm', 'current_maximum_physical_z_norm', 'current_maximum_gamma_axis_norm', 'current_maximum_first_angular_endpoint_residual', 'current_maximum_second_angular_endpoint_residual', 'endpoint_counts', 'actual_normal_counts', 'last_root_failure', 'normal_lift_last_summary', 'numerical_Newton_iterations_differentiated', 'complete_uniform_IFT_conditions_verified', 'complete_continuous_root_branch_certified', 'endpoint_root_error_enclosed', 'stationary_KKT_selection_used', 'continuous_horizontal_ODE_solution_claimed', 'final_implicit_J_uses_all_normal_stage_equations', 'previous_normal_frame_full_parameter_chain_retained', 'original_zero_control_target_full_parameter_chain_retained', 'implicit_control_dimension', 'normal_increment_dimension', 'implicit_dimension_per_stage', 'complete_first_angular_implicit_dimension', 'complete_second_angular_implicit_dimension', 'current_reference_calibration', 'analytic_stage_jacobian', 'analytic_normal_frame')",
    "new": "ROOT_SNAPSHOT_KEYS = ('current_full_point_sha256', 'endpoint_root_policy', 'normal_stage_count', 'exact_normal_step_nodes', 'actual_normal_step_carriers_binary64_hex', 'common_partition_for_all_angles_and_free_points', 'per_angle_adaptive_normal_partition', 'current_cached_angle_roots', 'current_all_grid_angle_roots_available', 'current_all_grid_second_angular_jets_available', 'current_maximum_endpoint_residual', 'current_maximum_dimensionless_control_norm', 'current_maximum_physical_z_norm', 'current_maximum_gamma_axis_norm', 'current_maximum_first_angular_endpoint_residual', 'current_maximum_second_angular_endpoint_residual', 'endpoint_counts', 'actual_normal_counts', 'last_root_failure', 'normal_lift_last_summary', 'numerical_Newton_iterations_differentiated', 'complete_uniform_IFT_conditions_verified', 'complete_continuous_root_branch_certified', 'endpoint_root_error_enclosed', 'stationary_KKT_selection_used', 'continuous_horizontal_ODE_solution_claimed', 'final_implicit_J_uses_all_normal_stage_equations', 'previous_normal_frame_full_parameter_chain_retained', 'original_zero_control_target_full_parameter_chain_retained', 'implicit_control_dimension', 'normal_increment_dimension', 'implicit_dimension_per_stage', 'complete_first_angular_implicit_dimension', 'complete_second_angular_implicit_dimension', 'current_reference_calibration', 'analytic_stage_jacobian', 'analytic_normal_frame', 'detached_closure_value_reuse')",
    "count": 1
   },
   {
    "old": "actual-public09-J1845-analytic-frame-packet-envelope-SO3-readout-v1",
    "new": "actual-run10-J1845-closure-values-packet-envelope-SO3-readout-v1",
    "count": 1
   },
   {
    "old": "        analytic_normal_frame=extra['analytic_J3_binding']['analytic_normal_frame'],\n",
    "new": "        analytic_normal_frame=extra['analytic_J3_binding']['analytic_normal_frame'],\n        detached_closure_value_reuse=extra['analytic_J3_binding']['detached_closure_value_reuse'],\n",
    "count": 1
   }
  ]
 }
];

export function build(read) {
  const output=new Map();
  for(const spec of SPECS) {
    const parent=read(spec.parent.path);
    if(typeof parent!=='string'||!same(identity(parent),spec.parent))throw new Error('Whole construction parent differs: '+spec.parent.path);
    let value=parent;
    for(const patch of spec.patches) {
      const count=value.split(patch.old).length-1;
      if(count!==patch.count)throw new Error('Exact patch count differs: '+spec.output.name+' '+count+' != '+patch.count);
      value=value.split(patch.old).join(patch.new);
    }
    if(!same(identity(value),spec.output))throw new Error('Whole derived source differs: '+spec.output.name);
    if(spec.output.bytes>=100000)throw new Error('Complete source exceeds the integration ceiling');
    output.set(spec.output.name,value);
  }
  return output;
}
