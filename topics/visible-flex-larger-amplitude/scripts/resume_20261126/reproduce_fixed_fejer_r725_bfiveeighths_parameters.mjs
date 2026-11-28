#!/usr/bin/env node
/* Complete run27 parameter-only derivation from immutable full run26 documents.
 * This program reads JSON/text and writes complete JSON. It imports no scientific
 * source and is not a workflow prerequisite or a numerical admission test.
 * Usage: node reproduce_fixed_fejer_r725_bfiveeighths_parameters.mjs
 *        --parent-directory FULL_PARENT_DIRECTORY --generated-directory OUTPUT
 * The parent directory contains the five entire recorded parent files by basename.
 * An evolving current note is not a substitute for the frozen historical note:
 * recover its exact bytes from the recorded fixed commit/Git blob when necessary.
 */
import {readFileSync,writeFileSync,mkdirSync} from "node:fs";
import {resolve,join,basename} from "node:path";
import {createHash} from "node:crypto";

const DATA={
  "date": "2026-11-28",
  "session": "Astra-larger-e4e2a2bf-20261126",
  "repository": "Rogerhu12/math-research-public",
  "topic": "topics/visible-flex-larger-amplitude",
  "oldNamespace": "fixed-fejer-r725-bhalf-first",
  "newNamespace": "fixed-fejer-r725-bfiveeighths-first",
  "sourcePublicationCommit": "95801769a95b2940b14ad01fe7640581b2c2fb44",
  "parentParameterPublicationCommit": "f44e6c09210e7b616775a966ce89b03ccda25b9d",
  "records": {
    "binding": {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r725-bhalf-complete-parameter-binding.json",
      "name": "fixed-fejer-r725-bhalf-complete-parameter-binding.json",
      "bytes": 47684,
      "sha256": "5abc72b77a2eb51064239e49a5e90fcc9fd230fc4883a925e19461ae701ef7eb",
      "sha": "b81215714615e663d537f7d0d8c7341aadb453c9",
      "git_blob_sha": "b81215714615e663d537f7d0d8c7341aadb453c9",
      "fixed_publication_commit": "f44e6c09210e7b616775a966ce89b03ccda25b9d"
    },
    "science": {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r725-bhalf-science-complete-ready.json",
      "name": "fixed-fejer-r725-bhalf-science-complete-ready.json",
      "bytes": 72545,
      "sha256": "fb33c7620b05193b54e38a39e97f7efc0fa7149bcbc720d04db1c041aeda0d63",
      "sha": "ebde4051043cfbf7524244dee27f2e85589a562c",
      "git_blob_sha": "ebde4051043cfbf7524244dee27f2e85589a562c",
      "fixed_publication_commit": "f44e6c09210e7b616775a966ce89b03ccda25b9d"
    },
    "pure": {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r725-bhalf-pure-complete-ready.json",
      "name": "fixed-fejer-r725-bhalf-pure-complete-ready.json",
      "bytes": 58721,
      "sha256": "29254c1a4a08cbb508266d9ac4c88178a6a7e2b5413428d31461056fe8939ccf",
      "sha": "b3d57832327fccecf3afb4f211006125f331e271",
      "git_blob_sha": "b3d57832327fccecf3afb4f211006125f331e271",
      "fixed_publication_commit": "f44e6c09210e7b616775a966ce89b03ccda25b9d"
    },
    "parent_manifest": {
      "name": "fixed-fejer-r725-bhalf-complete-parameter-delivery.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r725-bhalf-complete-parameter-delivery.json",
      "bytes": 19108,
      "sha256": "a02d1140c3cc83b9e70cde8a264e68707db5ef9da49710826a14a099b6eeb8f5",
      "git_blob_sha": "c5edf0dd581dcba4af3d6c8b8c97483d1d089de6",
      "fixed_publication_commit": "f44e6c09210e7b616775a966ce89b03ccda25b9d"
    },
    "official26": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run26-complete-r725-cutoff-launch-and-continuation.md",
      "name": "2026-11-28-run26-complete-r725-cutoff-launch-and-continuation.md",
      "bytes": 30859,
      "sha256": "27a7d30af5251b30f8a98c254a25f648d4800b1fa1ca38070047a7b553c0976d",
      "git_blob_sha": "ed76ddec90e5d43fe19a513bf7497b372d57f8d0",
      "fixed_publication_commit": "4f80adb37306bd625c5e0ab7e4d1ce02dc4a8c65"
    },
    "accurate_normal_geometry_R723_delivery": {
      "name": "fixed-fejer-r725-complete-accurate-normal-geometry-R723-delivery.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r725-complete-accurate-normal-geometry-R723-delivery.json",
      "bytes": 50664,
      "sha256": "10e51880af1c77a819b1ccd26ddd3212bd65eaa3a6cb230ae2114d866d120b2c",
      "git_blob_sha": "c9479d66f1bddbd7a8aa03f054d606db354ec580",
      "role": "complete_accurate_normal_geometry_R723_delivery"
    },
    "accurate_R716_mesh_delivery": {
      "name": "fixed-fejer-r725-complete-R716-and-phase-mesh-delivery.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r725-complete-R716-and-phase-mesh-delivery.json",
      "bytes": 82506,
      "sha256": "c6e2fb1d278275f6742766c5cfe3e9f74fd0a38bbead028f0f88d4feab257bf2",
      "git_blob_sha": "589d95782627e6d8c72452b4c50089ff3a4a20cc",
      "role": "complete_R716_mesh_delivery"
    }
  },
  "names": {
    "binding": "fixed-fejer-r725-bfiveeighths-complete-parameter-binding.json",
    "science": "fixed-fejer-r725-bfiveeighths-science-complete-ready.json",
    "pure": "fixed-fejer-r725-bfiveeighths-pure-complete-ready.json"
  },
  "external26": {
    "run_id": "46103106086",
    "run_attempt": 1,
    "run_attempt_key": "46103106086/1",
    "job_id": "140849792210",
    "official_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/46103106086",
    "official_head_sha": "a6c9c1011551cb0c84c458e603b6b691f66313f4",
    "official_started_at": "2026-11-28T03:29:40Z",
    "official_status_at_indicated_record": "in_progress",
    "official_conclusion_at_indicated_record": null,
    "declared_driver_source_sha256": "e1d3b06875496ba2555d20e2e1e96bfa92c420c15dc7276788160b44fca337cd",
    "declared_driver_source_is_not_observed_child_source": true,
    "complete_official_launch_and_source_note": {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run26-complete-r725-cutoff-launch-and-continuation.md",
      "name": "2026-11-28-run26-complete-r725-cutoff-launch-and-continuation.md",
      "bytes": 30859,
      "sha256": "27a7d30af5251b30f8a98c254a25f648d4800b1fa1ca38070047a7b553c0976d",
      "git_blob_sha": "ed76ddec90e5d43fe19a513bf7497b372d57f8d0",
      "fixed_publication_commit": "4f80adb37306bd625c5e0ab7e4d1ce02dc4a8c65"
    },
    "complete_scientific_parameter_record": {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r725-bhalf-science-complete-ready.json",
      "name": "fixed-fejer-r725-bhalf-science-complete-ready.json",
      "bytes": 72545,
      "sha256": "fb33c7620b05193b54e38a39e97f7efc0fa7149bcbc720d04db1c041aeda0d63",
      "sha": "ebde4051043cfbf7524244dee27f2e85589a562c",
      "git_blob_sha": "ebde4051043cfbf7524244dee27f2e85589a562c",
      "fixed_publication_commit": "f44e6c09210e7b616775a966ce89b03ccda25b9d"
    },
    "complete_pure_parameter_record": {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r725-bhalf-pure-complete-ready.json",
      "name": "fixed-fejer-r725-bhalf-pure-complete-ready.json",
      "bytes": 58721,
      "sha256": "29254c1a4a08cbb508266d9ac4c88178a6a7e2b5413428d31461056fe8939ccf",
      "sha": "b3d57832327fccecf3afb4f211006125f331e271",
      "git_blob_sha": "b3d57832327fccecf3afb4f211006125f331e271",
      "fixed_publication_commit": "f44e6c09210e7b616775a966ce89b03ccda25b9d"
    },
    "complete_parameter_delivery_record": {
      "name": "fixed-fejer-r725-bhalf-complete-parameter-delivery.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r725-bhalf-complete-parameter-delivery.json",
      "bytes": 19108,
      "sha256": "a02d1140c3cc83b9e70cde8a264e68707db5ef9da49710826a14a099b6eeb8f5",
      "git_blob_sha": "c5edf0dd581dcba4af3d6c8b8c97483d1d089de6",
      "fixed_publication_commit": "f44e6c09210e7b616775a966ce89b03ccda25b9d"
    },
    "actual_scientific_source_commit": null,
    "actual_launcher_source_sha256": null,
    "actual_current_input_file_records": null,
    "actual_model_identity_sha256": null,
    "actual_current_full_point_sha256": null,
    "actual_complete_scientific_report_sha256": null,
    "actual_final_checkpoint_sha256": null,
    "actual_complete_thirteen_member_parent": null,
    "actual_root_packet_sha256": null,
    "actual_snapshot_identity_sha256": null,
    "complete_typed_or_accepted_history_available": false,
    "unknown_history_is_not_empty": true,
    "not_a_typed_transfer_or_restart_input": true,
    "only_external_documented_obligation": true,
    "no_original_five_peer_CLI_pair_added_removed_or_relabelled": true,
    "same_source_code_does_not_imply_same_seed_model_point_or_field": true,
    "no_progress_point_or_reference_input_treated_as_complete_field": true
  }
};
const EXPECTED={
  "binding": {
    "name": "fixed-fejer-r725-bfiveeighths-complete-parameter-binding.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r725-bfiveeighths-complete-parameter-binding.json",
    "bytes": 37316,
    "sha256": "d66e3ed8a8c18908e5d28cecb556308e4bfa9da6ae5fd4687798be5cd45ddd99",
    "git_blob_sha": "959b7b0f7229adccd705163665b5b6220aa2a534",
    "role": "parameter-binding"
  },
  "science": {
    "name": "fixed-fejer-r725-bfiveeighths-science-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r725-bfiveeighths-science-complete-ready.json",
    "bytes": 73010,
    "sha256": "26c61186841194b9bbc151631b6a54027ee0799037d06afdf15ab28d6cea9447",
    "git_blob_sha": "516203d6ec0c43679f5cb04a1fbc7f3da0e52ffc",
    "role": "science-ready"
  },
  "pure": {
    "name": "fixed-fejer-r725-bfiveeighths-pure-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r725-bfiveeighths-pure-complete-ready.json",
    "bytes": 58998,
    "sha256": "66fc1686f905fe36ad6eb5318eaafd30a38232663cb14c72d527ce149f50d213",
    "git_blob_sha": "9605657839339e6ba3fa5fceda09000634ed721b",
    "role": "pure-ready"
  }
};
const digest=(algorithm,content)=>createHash(algorithm).update(content).digest("hex");
const bytes=text=>Buffer.byteLength(text,"utf8");
const record=(name,role,text)=>({
 name,path:DATA.topic+"/computations/"+name,bytes:bytes(text),
 sha256:digest("sha256",text),
 git_blob_sha:digest("sha1",Buffer.concat([Buffer.from("blob "+bytes(text)+"\0","utf8"),Buffer.from(text,"utf8")])),
 role
});
function derive(DATA,PARENTS,record) {

const clone=value=>JSON.parse(JSON.stringify(value));
const pointer=(record,path)=>({complete_file:clone(record),json_pointer:path});
const mapNamespace=value=>{
 if(typeof value==="string")return value.split(DATA.oldNamespace).join(DATA.newNamespace);
 if(Array.isArray(value))return value.map(mapNamespace);
 if(value&&typeof value==="object")return Object.fromEntries(Object.entries(value).map(([k,v])=>[k.split(DATA.oldNamespace).join(DATA.newNamespace),mapNamespace(v)]));
 return value;
};
const pairs=x=>Object.values(x||{}).reduce((sum,row)=>sum+Object.keys(row).length,0);
const pb=PARENTS.binding,ps=PARENTS.science,pp=PARENTS.pure;
if(ps.steps.length!==1||pp.steps.length!==1)throw Error("whole parent step cardinality");
if(ps.steps[0].args.length!==157||pp.steps[0].args.length!==7)throw Error("whole parent argv");
if(ps.steps[0].args[112]!=="--seed-boundary-total-length"||ps.steps[0].args[113]!=="1/2")throw Error("exact original width argument");
if(pairs(ps.steps[0].summary)!==458||pairs(pp.steps[0].summary)!==445||pairs(ps.steps[0].progress_summary)!==64)throw Error("complete parent selectors");
const widthChange={flag:"--seed-boundary-total-length",zero_based_value_index:113,original_value:"1/2",current_value:"5/8"};
const scope=kind=>"Complete R725 epsilon=1/8 paired-halfwave b/S=5/8, delta=1/32 "+kind+" from the entire run26 parameter parent. All137 source-role pairs and all22 complete runtime files are unchanged. Only the existing boundary-total-length numeric argument changes from 1/2 to 5/8, with a fresh namespace; all other157/7 argument words, free coordinates, domains, normal32 stages, budgets, outputs, cleanup and458/445 formal plus64 live selectors are retained subject only to the explicit output namespace mapping. The new physical layer widths, boundary integral B, mean roots, lambda, complete seed/model and reference calibration must be recomputed from this actual run. No prior field, root words, final, accepted/typed history or continuous certificate is inherited.";
const scienceStep=mapNamespace(ps.steps[0]),pureStep=mapNamespace(pp.steps[0]);
scienceStep.args[113]="5/8";scienceStep.scope=scope("science");pureStep.scope=scope("pure");
const undo=value=>{
 if(typeof value==="string")return value.split(DATA.newNamespace).join(DATA.oldNamespace);
 if(Array.isArray(value))return value.map(undo);
 if(value&&typeof value==="object")return Object.fromEntries(Object.entries(value).map(([k,v])=>[k.split(DATA.newNamespace).join(DATA.oldNamespace),undo(v)]));
 return value;
};
const inverseScience=undo(scienceStep),inversePure=undo(pureStep);
inverseScience.args[113]="1/2";inverseScience.scope=ps.steps[0].scope;inversePure.scope=pp.steps[0].scope;
if(JSON.stringify(inverseScience)!==JSON.stringify(ps.steps[0])||JSON.stringify(inversePure)!==JSON.stringify(pp.steps[0]))throw Error("complete inverse parameter object");
const originalPeers=clone(pb.complete_peer_responsibilities.complete_external_obligation_pairs);
if(originalPeers.length!==13||originalPeers.some(x=>x[0]===DATA.external26.run_attempt_key))throw Error("complete original13 peer identity");
const allPeers=originalPeers.concat([[DATA.external26.run_attempt_key,DATA.external26.declared_driver_source_sha256]]);
const sourceRegistry={...clone(pb.current_source_role_registry),unchanged_pairs:137,changed_pairs:0,
 comparison:"run27 versus the complete current run26 source registry",
 historical_run26_source_derivation:pointer(DATA.records.binding,"/current_source_role_registry")};
const runtimeRecords={...clone(pb.current_runtime_records),unchanged_complete_files:22,changed_complete_files:0,
 scope:"All22 exact complete current runtime bodies are shared byte-for-byte with run26. The original nineteen logical slots and seed/base/Q expansion are retained without source aliases or omissions."};
const seedRecipe=clone(pb.explicit_parameter_recipe.current_seed_parameter_recipe);
Object.assign(seedRecipe,{
 relative_boundary_total_length:"5/8",each_of_four_boundary_layers_relative_length:"5/32",
 combined_central_relative_length:"1/4",each_of_two_central_relative_length:"1/8",
 central_intervals_relative:[["3/16","5/16"],["11/16","13/16"]],
 boundary_formula:"Unchanged R725 C_epsilon with exact epsilon1/8 and normalized derivative peak8/7, evaluated on this run's four layers of relative width5/32; all eight exact inner cuts and all twelve boundary pieces follow the full source formulas.",
 current_field_mean_roots_or_working_words_inherited:false,true_mean_root_and_angular_jets_still_require_actual_work:true,
 complete_original_seed_recipe:pointer(DATA.records.binding,"/explicit_parameter_recipe/current_seed_parameter_recipe"),
 scalar_metric_and_frozen_reference_chart_unchanged:true,
 current_complete_seed_model_and_reference_calibration_recomputed:true,
 normalized_boundary_law_or_epsilon_changed:false,
 physical_boundary_layer_lengths_and_piece_locations_changed:true
});
const budgets=clone(pb.original_complete_budgets);budgets.seed_boundary_total_length="5/8";
const display={
 complete_parent_display:pointer(DATA.records.binding,"/complete_display_correspondence"),
 complete_original_display:clone(pb.complete_display_correspondence.complete_original_display),
 current_live_mapping:mapNamespace(pb.complete_display_correspondence.current_live_mapping),
 full_parent48_and_additional16_pairs_preserved:true,all_original64_pairs_unchanged_except_output_namespace:true,
 live_counts:clone(pb.complete_display_correspondence.live_counts),
 formal_counts:clone(pb.complete_display_correspondence.formal_counts),
 formal_pair_values_unchanged:true,location_missing_null_or_original_observation_error_retained:true,
 original_scalar_only_protocol_retained:true,
 compact_public_limit:pb.complete_display_correspondence.compact_public_limit,
 pretty_progress_limit:pb.complete_display_correspondence.pretty_progress_limit,
 queue_and_index_limit:pb.complete_display_correspondence.queue_and_index_limit,
 no_new_F_J_root_or_location_evaluation_added:true
};
const external={
 complete_all13_prior_peer_objects_and_discovery_history:pointer(DATA.records.binding,"/complete_peer_responsibilities"),
 all_original13_pairs_and_all_complete_original_objects_retained_in_original_order:true,
 complete_external_obligation_pairs:allPeers,external_obligation_count:14,
 added_complete_external_peer_record:clone(DATA.external26),
 original_supported_five_CLI_pairs_exactly_preserved:true,supported_CLI_peer_count:5,
 exact_complete_original_CLI_history:pointer(DATA.records.science,"/steps/0/args"),
 current_external_metadata_does_not_enter_typed_memory_or_restart:true,
 unknown_history_is_not_empty:true,source_equality_does_not_make_a_different_width_field_transferable:true,
 original_missing_parent_unknown_typed_obligations_not_discarded:true
};
const recipe={
 complete_parent_science_step:pointer(DATA.records.science,"/steps/0"),
 complete_parent_pure_step:pointer(DATA.records.pure,"/steps/0"),
 old_namespace:DATA.oldNamespace,new_namespace:DATA.newNamespace,
 current_scripts:{science:scienceStep.script,pure:pureStep.script},
 all_runtime_source_bytes_unchanged:true,new_runtime_files:0,new_CLI_words:0,
 all_numerical_argument_words_unchanged_except_one_explicit_existing_width:true,
 numeric_changes:[widthChange],scientific_argv_words:157,pure_argv_words:7,
 full_step_objects_outputs_cleanup_and_all_formal_and_live_values_retained:true,
 permitted_step_changes:["exact namespace substitution in all string keys and values","science args[113]: 1/2 to5/8","current scope prose records the real width change"],
 complete_original_parameter_recipe:pointer(DATA.records.binding,"/explicit_parameter_recipe"),
 current_seed_parameter_recipe:seedRecipe,
 original_actual_guard:{
  canonical_Fraction_argument:true,strict_boundary_range:"0 < b/S < 7/8",
  actual_current_boundary:"5/8",strict_profile_delta_range:"0 < delta < 1/8",
  actual_current_profile_delta:"1/32",source_fixed_epsilon:"1/8",
  actual_supported_intervals:[["1/32","15/32"],["17/32","31/32"]],
  source_checks_equal_positive_central_lengths:true,
  original_driver_seed_constructor_and_model_guards_retained:true,
  no_new_scientific_admission_or_review_gate:true
 }
};
const binding={
 schema:"complete-fixed-fejer-r725-bfiveeighths-parameter-binding-v1",
 prepared_date:DATA.date,session:DATA.session,status:"complete-parameter-only-preparation-not-executed",
 repository:DATA.repository,topic:DATA.topic,namespace:DATA.newNamespace,intended_independent_runner_label:"27",
 complete_parent_documents:{binding:clone(DATA.records.binding),science:clone(DATA.records.science),pure:clone(DATA.records.pure),manifest:clone(DATA.records.parent_manifest),actual26_launch_note:clone(DATA.records.official26)},
 complete_document_sharing:{
  interpretation:"Each complete_file record identifies the entire original bytes. A JSON pointer selects a complete original object; omitted duplicate metadata is inherited in full, not truncated or summarized away.",
  complete_parent_bytes_and_full_original_step_objects_preserved:true,
  no_current_runtime_source_or_scientific_parameter_is_replaced_by_a_stub:true,
  fixed_source_publication_commit:DATA.sourcePublicationCommit,
  fixed_parent_parameter_publication_commit:DATA.parentParameterPublicationCommit
 },
 current_source_role_registry:sourceRegistry,current_runtime_records:runtimeRecords,
 complete_current_source_delivery:clone(pb.complete_current_source_delivery),
 complete_location_transport_delivery:clone(pb.complete_location_transport_delivery),
 current_scientific_source_change:{
  changed_source_roles:[],changed_complete_runtime_files:0,all137_source_pairs_unchanged:true,all22_runtime_bytes_unchanged:true,
  complete_original_run26_source_derivation:pointer(DATA.records.binding,"/current_scientific_source_change"),
  source_fixed_boundary_epsilon:"1/8",normalized_boundary_cutoff_law_unchanged:true,
  physical_boundary_total_length_changed_from:"1/2",physical_boundary_total_length_changed_to:"5/8",
  profile_delta_unchanged:"1/32",new_CLI_words:0,
  all_eight_true_boundary_inner_cuts_and_twelve_boundary_pieces_retained:true,
  original_paired_halfwaves_auxiliary12_bubble_lift_outer_Gauss_and_partial_Lagrange_retained:true,
  new_seed_mean_roots_lambda_and_reference_calibration_actually_required:true,
  old_model_point_mean_root_final_or_certificate_not_inherited:true,
  complete_R725_proof:clone(pb.current_scientific_source_change.complete_R725_proof),
  complete_actual_pure_plan_contract:clone(pb.current_scientific_source_change.complete_actual_pure_plan_contract),
  R726_Slerp_rotation_frame2_restoration_policy_not_added:true
 },
 explicit_parameter_recipe:recipe,original_complete_budgets:budgets,
 fixed_target_scope:{
  accurate_a_rho0_g_reference_chart_and_recipe_unchanged:true,
  all_current_variables_and_three_rotation_channels_retained:true,
  complete_original_target_scope:pointer(DATA.records.binding,"/fixed_target_scope"),
  same_boundary_width_as_run26:false,
  same_boundary_width_as_run24_but_different_R725_cutoff_source:true,
  new_seed_model_depends_on_actual_new_b_and_unchanged_R725_law:true,
  current_mathematical_field_model_point_mean_and_calibration_not_inherited:true,
  own_complete_actual_reference_input_binding_required_by_original_solver:true,
  no_old_runner_raw_inputs_or_root_values_transferred:true,
  no_claim_of_feasibility_Gram_reach_distance_or_whole_image_improvement:true
 },
 complete_peer_responsibilities:external,complete_display_correspondence:display,
 actual_future:clone(pb.actual_future),
 accurate_descendant_scope:{
  complete_run26_accurate_normal_geometry_R723_delivery:clone(DATA.records.accurate_normal_geometry_R723_delivery),
  complete_run26_accurate_R716_and_mesh_delivery:clone(DATA.records.accurate_R716_mesh_delivery),
  actual_current_seed_definition_drives_b_support_central_cuts_and_mean:true,
  R725_accurate_runtime_does_not_hardcode_run26_namespace_or_bhalf:true,
  all_source_model_point_target_snapshot_and_whole_file_guards_preserved:true,
  existing_run26_full_accurate_parameter_plans_are_namespace_specific:true,
  run27_requires_its_own_complete_normal_geometry_R723_P_U_and_mesh_parameter_paths:true,
  run26_report_sha_or_certificate_cannot_be_reused_as_run27:true,
  only_science_and_pure_parameters_are_prepared_in_this_delivery:true,
  actual_run27_accurate_field_report_or_fee_available:false
 },
 scientific_scope:clone(pb.scientific_scope),
 complete_steps_preservation:{
  science:{parent:clone(DATA.records.science),parent_json_pointer:"/steps/0",argv_words:157,formal_fields:458,live_fields:64,numeric_changes:[widthChange]},
  pure:{parent:clone(DATA.records.pure),parent_json_pointer:"/steps/0",argv_words:7,formal_fields:445,live_fields:0,numeric_changes:[]},
  full_inverse_step_object_equals_original_parent:true
 }
};
const json=value=>JSON.stringify(value,null,2)+"\n";
const bindingText=json(binding),bindingRecord=record(DATA.names.binding,"parameter-binding",bindingText);
const ready=(kind,parent,step)=>({
 schema:"complete-fixed-fejer-r725-bfiveeighths-"+kind+"-ready-v1",
 prepared_date:DATA.date,executed:false,scientific_execution_permitted_only_in_public_Actions:true,
 intended_independent_runner_label:"27",namespace:DATA.newNamespace,
 complete_parameter_binding:bindingRecord,
 complete_parent_parameter_file:clone(DATA.records[kind]),
 whole_parent_step:pointer(DATA.records[kind],"/steps/0"),
 all_parent_metadata_preserved_as_historical_full_document:pointer(DATA.records[kind],""),
 complete_current_source_registry:pointer(bindingRecord,"/current_source_role_registry"),
 complete_current_runtime_records:pointer(bindingRecord,"/current_runtime_records"),
 complete_peer_responsibilities:pointer(bindingRecord,"/complete_peer_responsibilities"),
 complete_all64_live_correspondence:pointer(bindingRecord,"/complete_display_correspondence"),
 complete_parameter_recipe:pointer(bindingRecord,"/explicit_parameter_recipe"),
 scientific_numeric_argument_changes:kind==="science"?[widthChange]:[],
 physical_seed_boundary_law_changed:false,physical_boundary_layer_widths_and_seed_model_changed:true,
 source_fixed_cutoff_epsilon:"1/8",
 all_other_numerical_words_budgets_and_original_fields_preserved:true,
 all_original64_live_fields_preserved:true,additional_existing_scalar_live_fields:0,
 complete_runtime_source_bytes_changed:false,new_AST_fixture_replay_scientific_gate_added:false,
 actual_future:clone(pb.actual_future),
 current_argv_word_count:step.args.length,current_formal_selector_count:pairs(step.summary),current_live_selector_count:pairs(step.progress_summary),
 steps:[step]
});
return {
 binding:{value:binding,text:bindingText,record:bindingRecord},
 science:{value:ready("science",ps,scienceStep)},
 pure:{value:ready("pure",pp,pureStep)}
};

}
function parseArguments(argv) {
 const result={};
 for(let i=0;i<argv.length;i+=2) {
  const name=argv[i],value=argv[i+1];
  if(!["--parent-directory","--generated-directory"].includes(name)||!value||result[name])throw Error("Use complete --parent-directory and --generated-directory arguments");
  result[name]=resolve(value);
 }
 if(!result["--parent-directory"]||!result["--generated-directory"])throw Error("Both directory arguments are required");
 return result;
}
function readWhole(parentDirectory,rec) {
 const path=join(parentDirectory,rec.name||basename(rec.path));
 const buffer=readFileSync(path);
 const wholeSha=digest("sha256",buffer);
 const gitSha=digest("sha1",Buffer.concat([Buffer.from("blob "+buffer.length+"\0","utf8"),buffer]));
 if(buffer.length!==rec.bytes||wholeSha!==rec.sha256||gitSha!==rec.git_blob_sha)throw Error("Complete immutable parent identity mismatch: "+rec.path);
 const text=buffer.toString("utf8");
 if(Buffer.compare(Buffer.from(text,"utf8"),buffer)!==0)throw Error("Parent is not whole UTF-8 text: "+rec.path);
 return {path,text};
}
const args=parseArguments(process.argv.slice(2));
const parentDirectory=args["--parent-directory"],outputDirectory=args["--generated-directory"];
const whole={};
for(const role of ["binding","science","pure","parent_manifest","official26"])whole[role]=readWhole(parentDirectory,DATA.records[role]);
const parents={binding:JSON.parse(whole.binding.text),science:JSON.parse(whole.science.text),pure:JSON.parse(whole.pure.text)};
const outputs=derive(DATA,parents,record);
for(const kind of ["science","pure"]) {
 outputs[kind].text=JSON.stringify(outputs[kind].value,null,2)+"\n";
 outputs[kind].record=record(DATA.names[kind],kind+"-ready",outputs[kind].text);
}
for(const [role,entry] of Object.entries(outputs)) {
 const expected=EXPECTED[role];
 if(entry.record.bytes!==expected.bytes||entry.record.sha256!==expected.sha256||entry.record.git_blob_sha!==expected.git_blob_sha)throw Error("Complete generated parameter identity mismatch: "+role);
 if(entry.record.bytes>=100000)throw Error("Complete parameter document must remain below100000 bytes");
}
mkdirSync(outputDirectory,{recursive:true});
for(const [role,entry] of Object.entries(outputs)) {
 writeFileSync(join(outputDirectory,entry.record.name),entry.text,"utf8");
 process.stdout.write(JSON.stringify({role,...entry.record})+"\n");
}
/* The only mutation produced is the three complete parameter files above.
 * Existing source files, original requests, queues, refs, raw arrays, model words,
 * checkpoints, stage roots and all scientific parameters other than declared b
 * are neither loaded as data nor changed by this text reproducer.
 */
