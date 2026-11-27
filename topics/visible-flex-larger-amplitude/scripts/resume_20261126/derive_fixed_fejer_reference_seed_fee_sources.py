#!/usr/bin/env python3
"""Reproduce three complete fixed Fejer fee sources; standard-library source text only.

All original files remain unchanged. Every replacement has its full old and
new text, occurrence count and exact character offsets. Reverse application
checks those offsets after each inverse operation and restores each complete
parent byte string. No field, scalar, interval, profile, array or root code is
imported or executed by this reproducer.
"""
import argparse
import hashlib
import json
from pathlib import Path

SCHEMA = "complete-fixed-fejer-reference-fees-source-reproduction-v1"
TOPIC = "topics/visible-flex-larger-amplitude"
DATA = json.loads(r"""[
 {
  "role": "consumer",
  "parent": {
   "path": "scripts/resume_20261126/run10_reference_seed_angular_profile_error_bounds.py",
   "name": "run10_reference_seed_angular_profile_error_bounds.py",
   "sha256": "91fd1fb0148c7dde3260bdcfed61b057033d308517960bdb86454cc1e96ab3a1",
   "bytes": 64800,
   "blob": "96912a916f530f02d00801404e150893b3c0d567"
  },
  "target": {
   "name": "fixed_fejer_reference_seed_angular_profile_error_bounds.py",
   "path": "scripts/resume_20261126/fixed_fejer_reference_seed_angular_profile_error_bounds.py",
   "sha256": "0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b",
   "bytes": 72182,
   "blob": "c0d09245e9e156cb93516945b3eec84e93807bf7"
  },
  "operations": [
   {
    "label": "complete_new_source_contracts",
    "old": "SCHEMA = 'complete-run10-reference-actual-seed-angular-profile-node-fees-v1'\nREQUEST_SCHEMA = 'actual-run10-reference-seed-accurate-fee-request-v1'\nPROVIDER_SHA = \"0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b\"\nKERNEL_SHA = \"f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917\"\nREADER_SHA = '2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e'\nDRIVER_SHA = 'c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1'\nADAPTER_SOURCE_CONTRACT = {'stem': 'run10_reference',\n 'report_schema': 'complete-run10-detached-closure-value-material-envelope-SO3-QP-v1',\n 'driver_name': 'fullclosed_run10_detached_closure_so3_qp.py',\n 'driver_sha256': 'c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1',\n 'reader_name': 'read_run10_detached_closure_so3_report.py',\n 'reader_sha256': '2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e',\n 'field_schema': 'complete-R711-reference-centred-detached-closure-values-analytic-frame-J3-normal-layer-v1',\n 'field_name': 'so3_reference_centred_closure_values_normal_lift_operator.py',\n 'field_sha256': '6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4',\n 'calibration_name': 'reference_centred_closure_values_calibration.py',\n 'calibration_sha256': 'b59776d52653f036590b619124579a20400d3bb7a4de8117d3221ca32bec144f',\n 'C1_role': 'frame_C1',\n 'C1_sha256': '1f80ce726f9cf9424740331eb54a5cafa86a058ca2b048ee5fb6add5fc371caa'}\nDERIVED_FROM_COMPLETE_R713_SOURCE_SHA256 = '82e6f1a714c241b1e445304017613cc0fab8874520ef7d6904acf3ae62904f76'\nDERIVED_FROM_COMPLETE_CACHED_CONSUMER_SHA256 = 'a7f1862362d729f29fba2b41ad040a5961b8cedb5eb729d8d6bbdc5bc36120c9'\nMATERIAL_ENVELOPE_SOURCE_CONTRACT = {'memory_role': 'independent_envelope_memory',\n 'memory_name': 'complete_material_envelope_memory_public_run10.py',\n 'memory_sha256': 'f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba',\n 'rows_name': 'complete_material_envelope_rows.py',\n 'rows_sha256': '729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7',\n 'geometry_name': 'so3_run10_detached_closure_geometry.py',\n 'geometry_sha256': '6c676d4302f4271310ffca899ca8820fe43f2d792ee9a634747f25eecf9f6528',\n 'memory_schema': 'complete-actual-public-run10-material-envelope-memory-and-typed-policy-v1',\n 'policy_schema': 'literal-old-current-grid-actual-public-run10-working-policy-v1',\n 'complete_reader_validates_every_recorded_scan_and_row_scope': True,\n 'protected_history_roles_or_order_reconstructed': False,\n 'fixed_seed_fees_pay_material_envelope_geometry': False}\nDERIVED_FROM_COMPLETE_MATERIAL_ENVELOPE_CONSUMER_SHA256 = '2859943d522cd764b686112acd0acdb065dc6a893625f4a8e237641caf041d36'\nACTUAL_PUBLIC_REFERENCE_CONTRACT = {'run_id': '45972294636',\n 'run_attempt': '1',\n 'target_schema': 'independently-frozen-actual-public-run10-scalar-and-material-chart-v1',\n 'target_identity_sha256': 'e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049',\n 'reference_model_identity_sha256': '081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5',\n 'reference_bundle_sha256': '512f13149c54b0cce9ca7b1d27fd4139493a480efcc824fe2e083d192d3a222b',\n 'preparation_report_sha256': '35fdae489de9a7ee205b4f03f805b30107cec382abbdd242ece43f87d857d286',\n 'fixed_chart_core_sha256': '90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e',\n 'returned_input_binding_sha256': '4ace8184408aa0c7cac7970ba6fc96565c68786a518cd9d280a1a97ef82b50cf',\n 'returned_input_binding_bytes': 430908,\n 'entry_binding_source_sha256': 'dc3b40645eb47f924392a703eb65e3fda982f43804b1861f89da1c038e9140a1',\n 'public_input_source_sha256': '9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209',\n 'input_producer_source_sha256': 'fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a',\n 'reference_source_sha256': '4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3',\n 'historical_carrier_restoration_leaves_declared_by_bound_producer': 2397,\n 'old_carrier_is_not_current_reference_value_input': True}\nDERIVED_FROM_COMPLETE_RUN09_CONSUMER_SHA256 = '7666e726f424e2d95c53b4d57e28a195923cb344a5fd34487fee9d00950677b1'\n",
    "new": "SCHEMA = 'complete-fixed-fejer-reference-actual-seed-angular-profile-node-fees-v1'\nREQUEST_SCHEMA = 'actual-fixed-fejer-reference-seed-accurate-fee-request-v1'\nPROVIDER_SHA = \"ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a\"\nKERNEL_SHA = \"f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917\"\nREADER_SHA = \"274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b\"\nDRIVER_SHA = \"477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd\"\nADAPTER_SOURCE_CONTRACT = {\"stem\": \"fixed_fejer_reference\",\n \"report_schema\": \"complete-fixed-fejer-immutable-point-material-envelope-SO3-QP-v1\",\n \"driver_name\": \"fullclosed_fixed_fejer_immutable_point_so3_qp.py\",\n \"driver_sha256\": \"477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd\",\n \"reader_name\": \"read_fixed_fejer_immutable_point_so3_report.py\",\n \"reader_sha256\": \"274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b\",\n \"field_schema\": \"complete-fixed-fejer-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1\",\n \"field_name\": \"fixed_fejer_normal_lift_operator.py\",\n \"field_sha256\": \"1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778\",\n \"calibration_name\": \"fixed_fejer_reference_calibration.py\",\n \"calibration_sha256\": \"fe36240c08ad32c4d4d665a387c70aaf02c0392419a51eef01e072081945e95c\",\n \"C1_role\": \"frame_C1\",\n \"C1_sha256\": \"1830c1d8e69e0e12d4b9d8af9f194d234ef3437cba546200738a1592a77aa0ca\"}\nMATERIAL_ENVELOPE_SOURCE_CONTRACT = {\"memory_role\": \"independent_envelope_memory\",\n \"memory_name\": \"complete_fixed_fejer_material_envelope_memory.py\",\n \"memory_sha256\": \"9f268e066274eff19ee2635124a8addf9c92eabf6d7177249f4ac4782c88a39a\",\n \"rows_name\": \"complete_material_envelope_rows.py\",\n \"rows_sha256\": \"729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7\",\n \"geometry_name\": \"so3_fixed_fejer_complete_geometry.py\",\n \"geometry_sha256\": \"bab4147bdd2f0d43a372ec1b04225fc66a05db2ccdc2f92968d3f70e2590bf26\",\n \"memory_schema\": \"complete-fixed-fejer-new-target-material-envelope-memory-v1\",\n \"policy_schema\": \"literal-reinterpreted-history-fixed-fejer-complete-grid-policy-v1\",\n \"complete_reader_validates_every_recorded_scan_and_row_scope\": True,\n \"protected_history_roles_or_order_reconstructed\": False,\n \"fixed_seed_fees_pay_material_envelope_geometry\": False,\n \"historical_literals_reinterpreted_not_same_physical_points\": True}\nFIXED_REFERENCE_SOURCE_CONTRACT = {\"target_schema\": \"complete-fixed-fejer-reference-definition-v1\",\n \"preparation_schema\": \"R690-fixed-fejer-axisymmetric-SO3-preparation-v1\",\n \"reference_schema\": \"R690-fixed-fejer-axisymmetric-SO3-reference-input-v1\",\n \"entry_binding_source_sha256\": \"3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88\",\n \"pure_input_binding_source_sha256\": \"3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f\",\n \"input_maker_source_sha256\": \"89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60\",\n \"reference_source_sha256\": \"e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb\",\n \"scalar_parameters_identity_sha256\": \"e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa\",\n \"working_scalar_integral_leaf_target\": 2218,\n \"mathematical_target_source_schema\": \"fixed-rn64-fejer-R690-mathematical-target-v1\",\n \"actual_reference_model_or_file_identity_prefilled\": False,\n \"old_carrier_is_not_current_reference_value_input\": True}\nDERIVED_FROM_COMPLETE_R713_SOURCE_SHA256 = '82e6f1a714c241b1e445304017613cc0fab8874520ef7d6904acf3ae62904f76'\nDERIVED_FROM_COMPLETE_CACHED_CONSUMER_SHA256 = 'a7f1862362d729f29fba2b41ad040a5961b8cedb5eb729d8d6bbdc5bc36120c9'\nDERIVED_FROM_COMPLETE_MATERIAL_ENVELOPE_CONSUMER_SHA256 = '2859943d522cd764b686112acd0acdb065dc6a893625f4a8e237641caf041d36'\nDERIVED_FROM_COMPLETE_RUN09_CONSUMER_SHA256 = '7666e726f424e2d95c53b4d57e28a195923cb344a5fd34487fee9d00950677b1'\nDERIVED_FROM_COMPLETE_RUN10_CONSUMER_SHA256 = '91fd1fb0148c7dde3260bdcfed61b057033d308517960bdb86454cc1e96ab3a1'\n",
    "count": 1,
    "positions": [
     754
    ]
   },
   {
    "label": "complete_actual_fixed_recipe_attribution",
    "old": "def recheck_run10_reference_attribution(value):\n    \"\"\"Keep every actually read input byte; no numerical value is generated.\"\"\"\n    for record in value[\"complete_snapshot_input_records\"]:\n        path = Path(record[\"path\"]).resolve()\n        if path.stat().st_size != record[\"bytes\"] or sha(path) != record[\"sha256\"]:\n            raise ValueError(\"The complete current run10 reference input changed: \"+str(path))\n\n\ndef bind_run10_reference_attribution(raw, pure):\n    \"\"\"Cross-bind the actual run10 field, whole returned target and six true inputs.\"\"\"\n    expected = ACTUAL_PUBLIC_REFERENCE_CONTRACT\n    roles = raw.get(\"source_sha256_by_role\", {})\n    target = raw.get(\"independent_fixed_target_definition\")\n    identity = raw.get(\"independent_fixed_target_definition_identity_sha256\")\n    checked = pure.get(\"independent_fixed_target_binding\")\n    actual = pure.get(\"actual_public_reference_input_binding\")\n    base = raw[\"representation\"][\"base_complete_model\"]\n    reference = base[\"complete_axisymmetric_reference_model\"]\n    seed = raw[\"supported_unit_seed_definition\"]\n    path_binding = raw[\"material_envelope\"][\"historical_address_binding\"][\"actual_path_binding\"]\n    if (raw.get(\"github_run_id\") != expected[\"run_id\"]\n            or roles.get(\"analytic_J3_binding\") != expected[\"entry_binding_source_sha256\"]\n            or roles.get(\"actual_public_input_binding\") != expected[\"public_input_source_sha256\"]\n            or roles.get(\"independent_input_projection_producer\") != expected[\"input_producer_source_sha256\"]\n            or roles.get(\"reference\") != expected[\"reference_source_sha256\"]\n            or not isinstance(target, dict) or not isinstance(checked, dict)\n            or not isinstance(actual, dict)\n            or target.get(\"schema\") != expected[\"target_schema\"]\n            or identity != expected[\"target_identity_sha256\"] or canonical(target) != identity\n            or target != path_binding.get(\"fixed_target_definition\")\n            or path_binding.get(\"fixed_target_definition_identity_sha256\") != identity\n            or checked.get(\"definition_identity_sha256\") != identity\n            or checked.get(\"actual_returned_public_input_binding\") != actual\n            or raw.get(\"actual_public_reference_input_binding\") != actual\n            or checked.get(\"complete_target_and_actual_report_reference_equal\") is not True\n            or checked.get(\"actual_full_chart_words_verified\") is not True\n            or checked.get(\"same_original_fixed_chart\") is not True\n            or checked.get(\"same_mathematical_g_claimed\") is not False\n            or checked.get(\"old_values_or_certificates_inherited\") is not False\n            or target.get(\"same_original_fixed_chart\") is not True\n            or target.get(\"same_mathematical_g_claimed\") is not False):\n        raise ValueError(\"Retain the complete actually returned run10 target, not another same-chart report\")\n    if (target.get(\"complete_current_reference_model\") != reference\n            or canonical(reference) != expected[\"reference_model_identity_sha256\"]\n            or seed.get(\"complete_axisymmetric_reference_model\") != reference\n            or target.get(\"current_reference_model_identity_sha256\") != canonical(reference)\n            or checked.get(\"actual_reference_model_identity_sha256\") != canonical(reference)\n            or target.get(\"complete_current_reference_bundle_sha256\") != expected[\"reference_bundle_sha256\"]\n            or raw.get(\"bundle_sha256\") != expected[\"reference_bundle_sha256\"]\n            or base.get(\"initial_reference_bundle_sha256\") != raw[\"bundle_sha256\"]\n            or seed.get(\"initial_reference_bundle_sha256\") != raw[\"bundle_sha256\"]\n            or checked.get(\"actual_reference_bundle_sha256\") != raw[\"bundle_sha256\"]\n            or target.get(\"fixed_chart_core_array_record\", {}).get(\"sha256\") != expected[\"fixed_chart_core_sha256\"]\n            or reference.get(\"fixed_chart_core_sha256\") != expected[\"fixed_chart_core_sha256\"]\n            or base.get(\"fixed_chart_core_sha256\") != expected[\"fixed_chart_core_sha256\"]\n            or seed.get(\"fixed_chart_core_sha256\") != expected[\"fixed_chart_core_sha256\"]\n            or checked.get(\"actual_fixed_chart_core_sha256\") != expected[\"fixed_chart_core_sha256\"]):\n        raise ValueError(\"Use the current whole reference/model/chart and its exact seed values\")\n    evidence = target.get(\"complete_public_input_evidence\", {})\n    files = actual.get(\"complete_current_input_files\")\n    file_roles = {\"current_warm_bundle\", \"current_node_report\", \"current_scalar_input\",\n        \"current_carrier\", \"current_preparation_report\", \"current_reference_bundle\"}\n    input_record = actual.get(\"actual_binding_file\", {})\n    if (actual.get(\"source_sha256\") != expected[\"entry_binding_source_sha256\"]\n            or actual.get(\"actual_run_id\") != expected[\"run_id\"]\n            or actual.get(\"actual_run_attempt\") != expected[\"run_attempt\"]\n            or actual.get(\"actual_fixed_target_definition_identity_sha256\") != identity\n            or actual.get(\"all_six_current_whole_files_reread\") is not True\n            or actual.get(\"physical_values_roots_or_certificates_inherited\") is not False\n            or input_record != path_binding.get(\"binding_file\")\n            or input_record.get(\"sha256\") != expected[\"returned_input_binding_sha256\"]\n            or input_record.get(\"bytes\") != expected[\"returned_input_binding_bytes\"]\n            or not isinstance(files, dict) or set(files) != file_roles\n            or evidence.get(\"current_files\") != files\n            or evidence.get(\"actual_run_id\") != expected[\"run_id\"]\n            or evidence.get(\"actual_run_attempt\") != expected[\"run_attempt\"]\n            or canonical(evidence) != target.get(\"complete_public_input_evidence_identity_sha256\")):\n        raise ValueError(\"The six actual current files and immutable returned input binding are required\")\n    expected_files = dict(current_reference_bundle=raw[\"bundle_sha256\"],\n        current_carrier=raw[\"observation_carrier_sha256\"],\n        current_node_report=raw[\"exact_tail_node_report_sha256\"],\n        current_scalar_input=raw[\"exact_tail_scalar_input_sha256\"],\n        current_preparation_report=raw[\"independent_preparation_report\"][\"sha256\"])\n    if any(files[key][\"sha256\"] != value for key, value in expected_files.items()):\n        raise ValueError(\"The current scientific input arguments cannot be replaced by the historical carrier\")\n    snapshot = dict(complete_snapshot_input_records=[input_record]+[files[key] for key in sorted(file_roles)])\n    recheck_run10_reference_attribution(snapshot)\n    preparation_bytes = Path(files[\"current_preparation_report\"][\"path\"]).read_bytes()\n    if (hashlib.sha256(preparation_bytes).hexdigest() != expected[\"preparation_report_sha256\"]\n            or len(preparation_bytes) != files[\"current_preparation_report\"][\"bytes\"]\n            or files[\"current_preparation_report\"][\"sha256\"] != expected[\"preparation_report_sha256\"]):\n        raise ValueError(\"Read the actual current preparation report before interpreting its integral metadata\")\n    preparation = json.loads(preparation_bytes)\n    scalar = preparation.get(\"true_scalar\", {})\n    leaves = scalar.get(\"integral_leaves\")\n    if (preparation.get(\"schema\") != \"R690-independent-axisymmetric-SO3-preparation-v1\"\n            or preparation.get(\"source_sha256\") != expected[\"reference_source_sha256\"]\n            or preparation.get(\"complete\") is not True\n            or preparation.get(\"reference_definition\") != reference\n            or preparation.get(\"reference_model_identity_sha256\") != canonical(reference)\n            or preparation.get(\"complete_scalar_tail_included\") is not True\n            or scalar.get(\"all_tail_domain_included\") is not True\n            or scalar.get(\"unresolved_oscillations_dropped\") is not False\n            or scalar.get(\"definition\") != reference[\"fixed_scalar_profile_definition\"]\n            or type(leaves) is not int or leaves < 1):\n        raise ValueError(\"The complete current radius/scalar enclosure and its real tail metadata are required\")\n    result = dict(\n        actual_run_id=expected[\"run_id\"], actual_run_attempt=expected[\"run_attempt\"],\n        fixed_target_definition_identity_sha256=identity,\n        actual_reference_model_identity_sha256=canonical(reference),\n        actual_reference_bundle_sha256=raw[\"bundle_sha256\"],\n        actual_current_carrier_sha256=raw[\"observation_carrier_sha256\"],\n        actual_fixed_chart_core_sha256=reference[\"fixed_chart_core_sha256\"],\n        actual_current_preparation_report=files[\"current_preparation_report\"],\n        actual_returned_input_binding=input_record,\n        actual_public_input_binding=actual,\n        complete_snapshot_input_records=snapshot[\"complete_snapshot_input_records\"],\n        current_reference_tail_integral_leaves=leaves,\n        current_reference_tail_requested_accuracy_reached=scalar[\"requested_integral_accuracy_reached\"],\n        current_reference_tail_integral_width_exact=scalar[\"integral_enclosure_width_exact\"],\n        current_radius_complete_enclosure=reference[\"radius_complete_enclosure\"],\n        actual_seed_initial_height_hex=seed[\"initial_height_hex\"],\n        historical_carrier_restoration_leaves_declared_by_bound_producer=\n            expected[\"historical_carrier_restoration_leaves_declared_by_bound_producer\"],\n        historical_carrier_used_as_current_reference_value_input=False,\n        current_reference_values_or_paid_fees_inherited_from_old_batch=False,\n        same_original_fixed_chart=True, same_mathematical_g_claimed=False,\n        actual_outer_analytic_frame_and_J3_are_source_attribution_only=True,\n        original_complete_R709_R713_formulas_retained=True,\n        continuous_angle_or_current_normal_or_field_fees_paid=False)\n    recheck_run10_reference_attribution(result)\n    return result\n\n\n",
    "new": "def recheck_fixed_fejer_reference_attribution(value):\n    \"\"\"Recheck every actually captured source/input byte without new values.\"\"\"\n    for record in value[\"complete_snapshot_input_records\"]:\n        path = Path(record[\"path\"]).resolve()\n        if path.stat().st_size != record[\"bytes\"] or sha(path) != record[\"sha256\"]:\n            raise ValueError(\"A complete fixed-Fejer source or actual reference input changed: \"+str(path))\n\n\ndef bind_fixed_fejer_reference_attribution(raw, pure):\n    \"\"\"Bind the declared recipe and the actually returned reference; no future identities.\"\"\"\n    expected = FIXED_REFERENCE_SOURCE_CONTRACT\n    roles = raw.get(\"source_sha256_by_role\", {})\n    target = raw.get(\"independent_fixed_target_definition\")\n    identity = raw.get(\"independent_fixed_target_definition_identity_sha256\")\n    checked = pure.get(\"independent_fixed_target_binding\")\n    actual = pure.get(\"actual_fixed_reference_input_binding\")\n    base = raw[\"representation\"][\"base_complete_model\"]\n    reference = base[\"complete_axisymmetric_reference_model\"]\n    seed = raw[\"supported_unit_seed_definition\"]\n    path_binding = raw[\"material_envelope\"][\"historical_address_binding\"][\"actual_path_binding\"]\n    if (roles.get(\"analytic_J3_binding\") != expected[\"entry_binding_source_sha256\"]\n            or roles.get(\"actual_public_input_binding\") != expected[\"pure_input_binding_source_sha256\"]\n            or roles.get(\"independent_input_projection_producer\") != expected[\"reference_source_sha256\"]\n            or roles.get(\"reference\") != expected[\"reference_source_sha256\"]\n            or roles.get(\"fixed_input_producer\") != expected[\"input_maker_source_sha256\"]\n            or not isinstance(target, dict) or not isinstance(checked, dict)\n            or not isinstance(actual, dict)\n            or target.get(\"schema\") != expected[\"target_schema\"]\n            or canonical(target) != identity\n            or target != path_binding.get(\"fixed_target_definition\")\n            or path_binding.get(\"fixed_target_definition_identity_sha256\") != identity\n            or checked.get(\"definition_identity_sha256\") != identity\n            or checked.get(\"actual_fixed_recipe_input_binding\") != actual\n            or raw.get(\"actual_fixed_reference_input_binding\") != actual\n            or checked.get(\"complete_target_and_actual_report_reference_equal\") is not True\n            or checked.get(\"actual_full_chart_words_verified\") is not True\n            or checked.get(\"predeclared_new_target\") is not True\n            or checked.get(\"same_original_fixed_chart\") is not False\n            or checked.get(\"same_mathematical_g_claimed\") is not False\n            or checked.get(\"old_values_or_certificates_inherited\") is not False\n            or target.get(\"declared_new_target\") is not True\n            or target.get(\"same_previous_mathematical_g_claimed\") is not False\n            or target.get(\"previous_target_fields_roots_or_certificates_inherited\") is not False):\n        raise ValueError(\"Retain the actual complete declared Fejer target and its own input family\")\n    mathematical = target.get(\"mathematical_target_recipe\")\n    math_identity = target.get(\"mathematical_target_identity_sha256\")\n    if (not isinstance(mathematical, dict)\n            or mathematical.get(\"schema\") != expected[\"mathematical_target_source_schema\"]\n            or canonical(mathematical) != math_identity\n            or mathematical.get(\"complete_scalar_parameters_identity_sha256\") != expected[\"scalar_parameters_identity_sha256\"]\n            or reference.get(\"mathematical_target_recipe\") != mathematical\n            or reference.get(\"mathematical_target_identity_sha256\") != math_identity\n            or checked.get(\"mathematical_target_identity_sha256\") != math_identity\n            or actual.get(\"mathematical_target_identity_sha256\") != math_identity\n            or pure.get(\"predeclared_mathematical_target_identity_sha256\") != math_identity\n            or pure.get(\"historical_literal_requests_reinterpreted_not_same_physical_points\") is not True\n            or pure.get(\"previous_target_completion_or_unknown_typed_history_reconstructed\") is not False):\n        raise ValueError(\"The entire exact-dyadic chart/scalar recipe and history scope must agree\")\n    if (reference.get(\"schema\") != expected[\"reference_schema\"]\n            or reference.get(\"source_sha256\") != expected[\"reference_source_sha256\"]\n            or target.get(\"complete_current_reference_model\") != reference\n            or seed.get(\"complete_axisymmetric_reference_model\") != reference\n            or target.get(\"current_reference_model_identity_sha256\") != canonical(reference)\n            or checked.get(\"actual_reference_model_identity_sha256\") != canonical(reference)\n            or target.get(\"complete_current_reference_bundle_sha256\") != raw[\"bundle_sha256\"]\n            or base.get(\"initial_reference_bundle_sha256\") != raw[\"bundle_sha256\"]\n            or seed.get(\"initial_reference_bundle_sha256\") != raw[\"bundle_sha256\"]\n            or checked.get(\"actual_reference_bundle_sha256\") != raw[\"bundle_sha256\"]\n            or target.get(\"fixed_chart_core_array_record\", {}).get(\"sha256\") != reference[\"fixed_chart_core_sha256\"]\n            or base.get(\"fixed_chart_core_sha256\") != reference[\"fixed_chart_core_sha256\"]\n            or seed.get(\"fixed_chart_core_sha256\") != reference[\"fixed_chart_core_sha256\"]\n            or checked.get(\"actual_fixed_chart_core_sha256\") != reference[\"fixed_chart_core_sha256\"]\n            or reference.get(\"warm_or_BVP_core_consumed\") is not False\n            or reference.get(\"same_previous_target_claimed\") is not False\n            or reference.get(\"predeclared_fixed_chart_from_rational_recipe\") is not True):\n        raise ValueError(\"Keep the complete generated reference, rounded chart and fixed seed\")\n    files = actual.get(\"complete_current_input_files\")\n    file_roles = {\"current_fixed_input_bundle\", \"current_node_report\", \"current_scalar_input\",\n        \"current_carrier\", \"current_preparation_report\", \"current_reference_bundle\"}\n    validation = actual.get(\"complete_input_validation\")\n    input_record = actual.get(\"actual_binding_file\")\n    if (actual.get(\"source_sha256\") != expected[\"entry_binding_source_sha256\"]\n            or actual.get(\"actual_input_producer_source_sha256\") != expected[\"reference_source_sha256\"]\n            or actual.get(\"actual_pure_input_binding_source_sha256\") != expected[\"pure_input_binding_source_sha256\"]\n            or actual.get(\"actual_fixed_input_maker_source_sha256\") != expected[\"input_maker_source_sha256\"]\n            or actual.get(\"actual_reference_model_identity_sha256\") != canonical(reference)\n            or actual.get(\"actual_fixed_target_definition_identity_sha256\") != identity\n            or actual.get(\"all_six_current_whole_files_reread\") is not True\n            or actual.get(\"predeclared_new_target\") is not True\n            or actual.get(\"same_original_fixed_chart\") is not False\n            or actual.get(\"same_mathematical_g_claimed\") is not False\n            or actual.get(\"physical_values_roots_or_certificates_inherited\") is not False\n            or not isinstance(validation, dict)\n            or validation != raw.get(\"independent_fixed_target_validation\")\n            or validation.get(\"source_sha256\") != expected[\"pure_input_binding_source_sha256\"]\n            or validation.get(\"complete_current_six_files_verified\") is not True\n            or validation.get(\"complete_generated_fixed_chart_verified\") is not True\n            or validation.get(\"historical_literal_addresses_are_reinterpreted_not_same_physical_points\") is not True\n            or validation.get(\"unknown_previous_target_history_reconstructed\") is not False\n            or validation.get(\"fixed_target_definition_identity_sha256\") != identity\n            or validation.get(\"mathematical_target_identity_sha256\") != math_identity\n            or validation.get(\"actual_current_model_identity_sha256\") != canonical(reference)\n            or validation.get(\"current_input_records\") != files\n            or validation.get(\"actual_binding_file\") != input_record\n            or input_record != path_binding.get(\"binding_file\")\n            or not isinstance(files, dict) or set(files) != file_roles):\n        raise ValueError(\"All six actual files and the complete source-bound input validation are required\")\n    required_files = dict(current_fixed_input_bundle=reference[\"fixed_input_bundle_sha256\"],\n        current_reference_bundle=raw[\"bundle_sha256\"],\n        current_carrier=raw[\"observation_carrier_sha256\"],\n        current_node_report=raw[\"exact_tail_node_report_sha256\"],\n        current_scalar_input=raw[\"exact_tail_scalar_input_sha256\"],\n        current_preparation_report=raw[\"independent_preparation_report\"][\"sha256\"])\n    if any(files[key][\"sha256\"] != digest for key, digest in required_files.items()):\n        raise ValueError(\"Current scientific inputs cannot be replaced by older target/carrier values\")\n    records = [input_record]+[files[key] for key in sorted(file_roles)]\n    snapshot = dict(complete_snapshot_input_records=records)\n    recheck_fixed_fejer_reference_attribution(snapshot)\n\n    def captured_record(record, name):\n        path = Path(record[\"path\"]).resolve()\n        data = path.read_bytes()\n        if len(data) != record[\"bytes\"] or hashlib.sha256(data).hexdigest() != record[\"sha256\"]:\n            raise ValueError(\"Captured complete bytes changed: \"+name)\n        return json.loads(data)\n\n    payload = captured_record(input_record, \"fixed input binding\")\n    preparation = captured_record(files[\"current_preparation_report\"], \"complete reference preparation\")\n    if (payload.get(\"fixed_target_definition\") != target\n            or payload.get(\"fixed_target_definition_identity_sha256\") != identity\n            or payload.get(\"mathematical_target_identity_sha256\") != math_identity\n            or payload.get(\"current_files\") != files\n            or payload.get(\"all_current_six_files_are_actual\") is not True\n            or preparation.get(\"schema\") != expected[\"preparation_schema\"]\n            or preparation.get(\"source_sha256\") != expected[\"reference_source_sha256\"]\n            or preparation.get(\"complete\") is not True\n            or preparation.get(\"reference_definition\") != reference\n            or preparation.get(\"reference_model_identity_sha256\") != canonical(reference)\n            or preparation.get(\"fixed_target_definition\") != target\n            or preparation.get(\"fixed_target_definition_identity_sha256\") != identity\n            or preparation.get(\"mathematical_target_identity_sha256\") != math_identity\n            or preparation.get(\"fixed_input_definition\") != target[\"working_input_definition\"]\n            or preparation.get(\"fixed_input_definition_identity_sha256\") != target[\"working_input_definition_identity_sha256\"]\n            or preparation.get(\"fixed_input_bundle\") != files[\"current_fixed_input_bundle\"]\n            or preparation.get(\"no_warm_BVP_or_optimized_old_chart_required\") is not True\n            or preparation.get(\"complete_scalar_tail_included\") is not True):\n        raise ValueError(\"The captured preparation, whole recipe and six files differ\")\n    execution = preparation.get(\"execution\", {})\n    if (execution != payload.get(\"producer\", {}).get(\"execution\")\n            or str(execution.get(\"run_id\")) != actual.get(\"actual_run_id\")\n            or str(execution.get(\"run_attempt\")) != actual.get(\"actual_run_attempt\")\n            or execution.get(\"repository\") != \"Rogerhu12/math-research-public\"):\n        raise ValueError(\"Retain actual reference execution separately from the field's own report\")\n    scalar = preparation.get(\"true_scalar\", {})\n    leaves = scalar.get(\"integral_leaves\")\n    if (scalar.get(\"all_tail_domain_included\") is not True\n            or scalar.get(\"unresolved_oscillations_dropped\") is not False\n            or scalar.get(\"definition\") != reference[\"fixed_scalar_profile_definition\"]\n            or scalar.get(\"model_identity_sha256\") != reference[\"fixed_scalar_metric_identity_sha256\"]\n            or leaves != expected[\"working_scalar_integral_leaf_target\"]\n            or type(leaves) is not int\n            or type(scalar.get(\"requested_integral_accuracy_reached\")) is not bool\n            or preparation.get(\"deterministic_scalar_work\") != dict(\n                leaf_target=leaves, actual_leaves=leaves, wall_clock_decides_leaf_count=False,\n                all_original_integer_leaf_operations_retained=True)):\n        raise ValueError(\"Read the complete fixed-work scalar table and its real accuracy status\")\n    maker_record = payload[\"fixed_input_preparation_report\"]\n    if preparation.get(\"fixed_input_preparation_report\") != maker_record:\n        raise ValueError(\"The actual fixed input construction report changed\")\n    maker = captured_record(maker_record, \"complete deterministic input construction\")\n    maker_outputs = {key:files[role] for key,role in (\n        (\"fixed_input\",\"current_fixed_input_bundle\"),(\"node_report\",\"current_node_report\"),\n        (\"scalar_input\",\"current_scalar_input\"))}\n    if (maker.get(\"source_sha256\") != expected[\"input_maker_source_sha256\"]\n            or maker.get(\"complete\") is not True or maker.get(\"status\") != \"complete\"\n            or maker.get(\"all_input_and_source_output_records_rechecked\") is not True\n            or maker.get(\"outputs\") != maker_outputs\n            or maker.get(\"mathematical_target_recipe\") != mathematical\n            or maker.get(\"mathematical_target_identity_sha256\") != math_identity\n            or maker.get(\"definition\") != target[\"working_input_definition\"]\n            or maker.get(\"definition_identity_sha256\") != target[\"working_input_definition_identity_sha256\"]\n            or maker.get(\"complete_scalar_parameters_identity_sha256\") != expected[\"scalar_parameters_identity_sha256\"]):\n        raise ValueError(\"No solved warm/core or another mathematical input can replace the fixed recipe\")\n    records.append(maker_record)\n    records.extend(maker[\"source_records\"].values())\n    records.extend(maker[\"input_records\"].values())\n    records.extend(payload[name] for name in (\n        \"fixed_target_definition_file\", \"new_locations\", \"complete_supplied_location_provenance\"))\n    for role,path in preparation[\"source_paths\"].items():\n        expected_sha = preparation[\"source_sha256_by_role\"][role]\n        if roles.get(role) != expected_sha:\n            raise ValueError(\"The actual reference source closure differs from the full field: \"+role)\n        actual_path = Path(path).resolve()\n        records.append(dict(path=str(actual_path),bytes=actual_path.stat().st_size,sha256=expected_sha))\n    result = dict(\n        actual_run_id=actual[\"actual_run_id\"], actual_run_attempt=actual[\"actual_run_attempt\"],\n        actual_field_run_id=raw.get(\"github_run_id\"),\n        fixed_target_definition_identity_sha256=identity,\n        mathematical_target_identity_sha256=math_identity,\n        complete_mathematical_target_recipe=mathematical,\n        actual_reference_model_identity_sha256=canonical(reference),\n        actual_reference_bundle_sha256=raw[\"bundle_sha256\"],\n        actual_current_carrier_sha256=raw[\"observation_carrier_sha256\"],\n        actual_fixed_chart_core_sha256=reference[\"fixed_chart_core_sha256\"],\n        actual_current_preparation_report=files[\"current_preparation_report\"],\n        actual_returned_input_binding=input_record,\n        actual_fixed_input_maker_report=maker_record,\n        actual_fixed_reference_input_binding=actual,\n        complete_snapshot_input_records=records,\n        current_reference_tail_integral_leaves=leaves,\n        current_reference_tail_requested_accuracy_reached=scalar[\"requested_integral_accuracy_reached\"],\n        current_reference_tail_integral_width_exact=scalar[\"integral_enclosure_width_exact\"],\n        current_radius_complete_enclosure=reference[\"radius_complete_enclosure\"],\n        actual_seed_initial_height_hex=seed[\"initial_height_hex\"],\n        historical_carrier_restoration_leaves_declared_by_bound_producer=None,\n        historical_carrier_used_as_current_reference_value_input=False,\n        current_reference_values_or_paid_fees_inherited_from_old_batch=False,\n        same_original_fixed_chart=False, same_mathematical_g_claimed=False,\n        exact_current_mathematical_recipe_and_generated_binary_chart_verified=True,\n        ideal_unrounded_Fejer_coefficients_used_as_actual_chart=False,\n        old_literals_reinterpreted_not_same_physical_points=True,\n        unknown_previous_target_history_reconstructed=False,\n        actual_outer_analytic_frame_J3_and_cache_are_source_attribution_only=True,\n        original_complete_R709_R713_formulas_retained=True,\n        continuous_angle_or_current_normal_or_field_fees_paid=False)\n    recheck_fixed_fejer_reference_attribution(result)\n    return result\n\n\n",
    "count": 1,
    "positions": [
     36791
    ]
   },
   {
    "label": "new_provider_schema_only",
    "old": "complete-supported-smooth-triangle-meridian-seed-reference-v1",
    "new": "complete-fixed-fejer-supported-smooth-triangle-meridian-seed-reference-v1",
    "count": 1,
    "positions": [
     17408
    ]
   },
   {
    "label": "actual_new_complete_base_source",
    "old": "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865",
    "new": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
    "count": 1,
    "positions": [
     58041
    ]
   },
   {
    "label": "actual_complete_reader_basename",
    "old": "read_run10_detached_closure_so3_report.py",
    "new": "read_fixed_fejer_immutable_point_so3_report.py",
    "count": 1,
    "positions": [
     62317
    ]
   },
   {
    "label": "new_recheck_calls",
    "old": "recheck_run10_reference_attribution",
    "new": "recheck_fixed_fejer_reference_attribution",
    "count": 1,
    "positions": [
     66584
    ]
   },
   {
    "label": "new_attribution_call",
    "old": "bind_run10_reference_attribution",
    "new": "bind_fixed_fejer_reference_attribution",
    "count": 1,
    "positions": [
     61739
    ]
   },
   {
    "label": "new_report_attribution_key",
    "old": "actual_run10_reference_attribution",
    "new": "actual_fixed_fejer_reference_attribution",
    "count": 2,
    "positions": [
     61704,
     66639
    ]
   },
   {
    "label": "final complete snapshot recheck before paid completion",
    "old": "    report[\"complete\"] = True\n    report[\"scope\"] = \"Complete conditional arithmetic for the bound actual batch and supplied nodes; external accurate fees remain explicit\"\n",
    "new": "    recheck_fixed_fejer_reference_attribution(\n        binding[\"complete_outer_attribution\"][\"actual_fixed_fejer_reference_attribution\"])\n    if (sha(args.report) != binding[\"report_sha256\"]\n            or sha(binding[\"actual_raw_batch_path\"]) != binding[\"actual_raw_batch_sha256\"]\n            or sha(args.fees) != fee_digest):\n        raise ValueError(\"The complete captured report, raw batch or accurate-fee request changed\")\n    report[\"all_actual_input_and_fee_request_records_rechecked\"] = True\n    report[\"complete\"] = True\n    report[\"scope\"] = \"Complete conditional arithmetic for the bound actual batch and supplied nodes; external accurate fees remain explicit\"\n",
    "count": 1,
    "positions": [
     71434
    ]
   }
  ]
 },
 {
  "role": "mean",
  "parent": {
   "path": "scripts/resume_20261126/run10_reference_accurate_mean_residuals.py",
   "name": "run10_reference_accurate_mean_residuals.py",
   "sha256": "19fd82f3d746cce4b7de474f42aeb4192e4e1cec8e38c375148bcd4a9ab51a38",
   "bytes": 40898,
   "blob": "0bd61da1dd500d62b6006a590f49a14b6fc2cc35"
  },
  "target": {
   "name": "fixed_fejer_reference_accurate_mean_residuals.py",
   "path": "scripts/resume_20261126/fixed_fejer_reference_accurate_mean_residuals.py",
   "sha256": "ae67ecac9f205cdb2378a7f981d5d60fc723e1caadd5281dff54395d358564a0",
   "bytes": 41476,
   "blob": "fdddb363e724ab45204854a2b3084fcb95cae4bc"
  },
  "operations": [
   {
    "label": "producer schema",
    "old": "complete-run10-reference-accurate-total-mean-residuals-v1",
    "new": "complete-fixed-fejer-reference-accurate-total-mean-residuals-v1",
    "count": 1,
    "positions": [
     759
    ]
   },
   {
    "label": "actual journal source-specific schema",
    "old": "same-run10-reference-actual-batch-complete-integral-journal-v1",
    "new": "same-fixed-fejer-reference-actual-batch-complete-integral-journal-v1",
    "count": 1,
    "positions": [
     842
    ]
   },
   {
    "label": "complete direct source dependencies",
    "old": "PINS = {'fees': ('scripts/resume_20261126/run10_reference_seed_angular_profile_error_bounds.py',\n          '91fd1fb0148c7dde3260bdcfed61b057033d308517960bdb86454cc1e96ab3a1'),\n 'reference': ('scripts/resume_20261126/so3_axisymmetric_reference.py',\n               '4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'),\n 'whole_scalar': ('scripts/resume_20261126/so3_axisymmetric_continuous_integrand.py',\n                  'a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6')}\n",
    "new": "PINS = {\"fees\": [\"scripts/resume_20261126/fixed_fejer_reference_seed_angular_profile_error_bounds.py\", \"0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b\"],\n \"reference\": [\"scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py\", \"e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb\"],\n \"whole_scalar\": [\"scripts/resume_20261126/so3_axisymmetric_continuous_integrand.py\", \"a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6\"]}\n",
    "count": 1,
    "positions": [
     959
    ]
   },
   {
    "label": "complete source ancestry",
    "old": "REFERENCE_UNIT_LAW = ",
    "new": "DERIVED_FROM_COMPLETE_RUN10_PRODUCER_SHA256 = '19fd82f3d746cce4b7de474f42aeb4192e4e1cec8e38c375148bcd4a9ab51a38'\nREFERENCE_UNIT_LAW = ",
    "count": 1,
    "positions": [
     1899
    ]
   },
   {
    "label": "accurate fixed recipe scope",
    "old": "SOURCE_SCOPE = ('Complete accurate fixed-seed candidate mean residuals for the full actually returned run10 detached-closure reference '\n 'and every angle in this actual batch. Current reference radius/core/H and scalar input are taken from the '\n 'actual current model, not from the 2397-leaf historical carrier reconstruction. Original R709/R713 '\n 'mathematical formulas and the full radial journal are unchanged. No whole-angle, raw calibration, current '\n 'normal-chain, sixjet, metric or geometry error is paid by this fixed-reference component.')",
    "new": "SOURCE_SCOPE = ('Complete accurate fixed-seed candidate mean residuals for the actual Fejer reference '\n 'generated from the declared deterministic input recipe and every angle in this actual batch. '\n 'The complete reference, exact binary64 chart, scalar definition, working H and all six actual files '\n 'are reread from the actual source-bound input records; no older reference value or fee is inherited. '\n 'The ideal unrounded Fejer polynomial is not substituted for the exact generated chart. '\n 'Original R709/R713 mathematical formulas, complete radial pieces and journal remain unchanged. '\n 'No whole-angle, raw calibration, current normal-chain, sixjet, metric or geometry error is paid here.')",
    "count": 1,
    "positions": [
     2104
    ]
   },
   {
    "label": "complete source snapshot after reference construction",
    "old": "        self.scalar = self.modules['whole_scalar'].ScalarWholeInterval(\n",
    "new": "        self.k.recheck_fixed_fejer_reference_attribution(\n            self.actual_binding['complete_outer_attribution']['actual_fixed_fejer_reference_attribution'])\n        self.scalar = self.modules['whole_scalar'].ScalarWholeInterval(\n",
    "count": 1,
    "positions": [
     8451
    ]
   },
   {
    "label": "every complete snapshot recheck",
    "old": "    def recheck_actual_bytes(self):\n",
    "new": "    def recheck_actual_bytes(self):\n        self.k.recheck_fixed_fejer_reference_attribution(\n            self.actual_binding['complete_outer_attribution']['actual_fixed_fejer_reference_attribution'])\n",
    "count": 1,
    "positions": [
     13341
    ]
   }
  ]
 },
 {
  "role": "scheduler",
  "parent": {
   "path": "scripts/resume_20261126/run10_all_recorded_reference_seed_fees.py",
   "name": "run10_all_recorded_reference_seed_fees.py",
   "sha256": "42624b7f7fb4be694ff1253baf456b8526269a0f20099a40af737b5ffc096cb5",
   "bytes": 29234,
   "blob": "190d7b7298a782443b9837c6da740b7a600f7942"
  },
  "target": {
   "name": "fixed_fejer_all_recorded_reference_seed_fees.py",
   "path": "scripts/resume_20261126/fixed_fejer_all_recorded_reference_seed_fees.py",
   "sha256": "ff21999e226953efd095f403f413c08fc244e36c05122485f97b128d699b5bba",
   "bytes": 29348,
   "blob": "b622b6cf83c52ad7498aca3c7635a45fe4251fe8"
  },
  "operations": [
   {
    "label": "actual fixed recipe scheduler description",
    "old": "Full recorded-batch fixed-seed fee schedule for the complete actual run10 detached-closure reference.",
    "new": "Full recorded-batch fixed-seed fee schedule for the actual deterministic Fejer reference.",
    "count": 1,
    "positions": [
     26
    ]
   },
   {
    "label": "scheduler schema",
    "old": "complete-run10-all-recorded-reference-seed-fee-schedule-v1",
    "new": "complete-fixed-fejer-all-recorded-reference-seed-fee-schedule-v1",
    "count": 1,
    "positions": [
     728
    ]
   },
   {
    "label": "complete current reader and fee source closure",
    "old": "PINS = {'reader': ('read_run10_detached_closure_so3_report.py',\n            '2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e'),\n 'producer': ('run10_reference_accurate_mean_residuals.py',\n              '19fd82f3d746cce4b7de474f42aeb4192e4e1cec8e38c375148bcd4a9ab51a38'),\n 'consumer': ('run10_reference_seed_angular_profile_error_bounds.py',\n              '91fd1fb0148c7dde3260bdcfed61b057033d308517960bdb86454cc1e96ab3a1')}\nDRIVER_SHA = 'c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1'\nREPORT_SCHEMA = 'complete-run10-detached-closure-value-material-envelope-SO3-QP-v1'\n",
    "new": "PINS = {\"reader\": [\"read_fixed_fejer_immutable_point_so3_report.py\", \"274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b\"],\n \"producer\": [\"fixed_fejer_reference_accurate_mean_residuals.py\", \"ae67ecac9f205cdb2378a7f981d5d60fc723e1caadd5281dff54395d358564a0\"],\n \"consumer\": [\"fixed_fejer_reference_seed_angular_profile_error_bounds.py\", \"0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b\"]}\nDRIVER_SHA = '477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd'\nREPORT_SCHEMA = 'complete-fixed-fejer-immutable-point-material-envelope-SO3-QP-v1'\n",
    "count": 1,
    "positions": [
     841
    ]
   },
   {
    "label": "whole source ancestry",
    "old": "INPUTS = (\"reference_bundle\", \"carrier\", \"node_report\", \"scalar_input\", \"preparation_report\")",
    "new": "DERIVED_FROM_COMPLETE_RUN10_SCHEDULER_SHA256 = '42624b7f7fb4be694ff1253baf456b8526269a0f20099a40af737b5ffc096cb5'\nINPUTS = (\"reference_bundle\", \"carrier\", \"node_report\", \"scalar_input\", \"preparation_report\")",
    "count": 1,
    "positions": [
     1662
    ]
   },
   {
    "label": "current attribution module name",
    "old": "\"_run10_reference_fee_attribution_\"",
    "new": "\"_fixed_fejer_reference_fee_attribution_\"",
    "count": 1,
    "positions": [
     4265
    ]
   },
   {
    "label": "same complete current attribution callback",
    "old": "module.bind_run10_reference_attribution",
    "new": "module.bind_fixed_fejer_reference_attribution",
    "count": 1,
    "positions": [
     4560
    ]
   },
   {
    "label": "actual fixed recipe attribution record key",
    "old": "actual_run10_reference_attribution",
    "new": "actual_fixed_fejer_reference_attribution",
    "count": 3,
    "positions": [
     4840,
     10369,
     11910
    ]
   }
  ]
 }
]""")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def checked(raw, record, role):
    if len(raw) != record["bytes"] or digest(raw) != record["sha256"]:
        raise ValueError("The complete source identity changed: "+role)
    return raw.decode("utf-8")


def positions(text, value):
    result = []
    p = 0
    while True:
        i = text.find(value, p)
        if i < 0:
            return result
        result.append(i)
        p = i+len(value)


def forward(source, operations):
    value = source
    for operation in operations:
        where = positions(value, operation["old"])
        if where != operation["positions"] or len(where) != operation["count"]:
            raise ValueError("The exact old source section changed: "+operation["label"])
        for p in reversed(where):
            value = value[:p]+operation["new"]+value[p+len(operation["old"]):]
    return value


def reverse(target, operations):
    value = target
    for operation in reversed(operations):
        difference = len(operation["new"])-len(operation["old"])
        where = [p+i*difference for i,p in enumerate(operation["positions"])]
        for p in reversed(where):
            if value[p:p+len(operation["new"])] != operation["new"]:
                raise ValueError("The exact replacement section changed: "+operation["label"])
            value = value[:p]+operation["old"]+value[p+len(operation["new"]):]
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    parser.add_argument("--verify-existing", action="store_true")
    args = parser.parse_args()
    repo, out = args.repo.resolve(), args.outdir.resolve()
    if repo == out or repo in out.parents:
        parser.error("Keep generated source-only replay outside the repository")
    if not args.verify_existing:
        out.mkdir(parents=True, exist_ok=True)
    rows = []
    for item in DATA:
        parent_path = repo/TOPIC/item["parent"]["path"]
        raw = parent_path.read_bytes()
        parent = checked(raw, item["parent"], item["role"]+" parent")
        target = forward(parent, item["operations"])
        generated = target.encode("utf-8")
        checked(generated, item["target"], item["role"]+" target")
        restored = reverse(target, item["operations"]).encode("utf-8")
        checked(restored, item["parent"], item["role"]+" reverse")
        if restored != raw:
            raise ValueError("Reverse replay did not restore every complete parent byte")
        path = out/item["target"]["name"]
        if args.verify_existing:
            if path.read_bytes() != generated:
                raise ValueError("The complete independently generated target differs: "+str(path))
        else:
            if path.exists() and path.read_bytes() != generated:
                raise FileExistsError("Do not overwrite different source bytes: "+str(path))
            path.write_bytes(generated)
        rows.append(dict(role=item["role"], path=str(path),
            bytes=len(generated), sha256=digest(generated),
            original_complete_parent_sha256=digest(raw),
            exact_forward_and_reverse_complete=True))
    print(json.dumps(dict(schema=SCHEMA, source_sha256=digest(Path(__file__).read_bytes()),
        complete=True, generated_sources=rows,
        imported_scientific_module=False, scientific_calculations_executed=False,
        AST_or_compile_claimed=False), sort_keys=True))


if __name__ == "__main__":
    main()
