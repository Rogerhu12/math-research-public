#!/usr/bin/env node
// Complete run23 parameter text constructor; no scientific evaluation or admission stage.
// All complete original step values remain; two historical objects use exact whole-parent JSON pointers.
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {resolve,dirname} from 'node:path';
import {createHash} from 'node:crypto';

const SPEC={"schema":"complete-fixed-fejer-restoration-continuation-bhalf-parameter-reproduction-spec-v1","prepared_utc":"2026-11-28 01:02:59 UTC","repository":"Rogerhu12/math-research-public","topic":"topics/visible-flex-larger-amplitude","old_namespace":"fixed-fejer-meridian-batched-bhalf-first","namespace":"fixed-fejer-restoration-continuation-bhalf-first","paths":{"science":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-restoration-continuation-bhalf-science-complete-ready.json","pure":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-restoration-continuation-bhalf-pure-complete-ready.json","display":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-restoration-continuation-bhalf-complete-display-correspondence.json","reproducer":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_restoration_continuation_bhalf_parameters.mjs","note":"topics/visible-flex-larger-amplitude/notes/2026-11-28-restoration-continuation-bhalf-complete-parameters.md","manifest":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-restoration-continuation-bhalf-complete-parameter-delivery.json"},"parents":{"binding":{"role":"runtime_binding","name":"fixed-fejer-restoration-continuation-current-runtime-binding.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-restoration-continuation-current-runtime-binding.json","bytes":64341,"sha256":"ad6980f8f1e57ce92eb442a57cc2c7f1584e9bec7c1ea876ce7a952e7ff2277c","git_blob_sha":"2f6776c3c86578152d5dfcf856c3d216da35c725"},"source_manifest":{"role":"manifest","name":"fixed-fejer-restoration-continuation-complete-entry-delivery.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-restoration-continuation-complete-entry-delivery.json","bytes":19448,"sha256":"d1bc3354d5a7aebcaf82abb8832e47b7e9690eacc90fa892f65b17358f57149e","git_blob_sha":"f159d88086202555ad1d71575fc1cea522e59dac"},"source_reproducer":{"role":"reproducer","name":"reproduce_fixed_fejer_restoration_continuation_sources.mjs","path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_restoration_continuation_sources.mjs","bytes":11011,"sha256":"bfd71bab0d94c8a81f2ed22fb67092ce4d01e7b30638d4bbc5cd1a8b6753641b","git_blob_sha":"e19764480d1e0f5e3140befdf19a19d606b6132d"},"source_note":{"role":"note","name":"2026-11-28-complete-restoration-continuation-entry.md","path":"topics/visible-flex-larger-amplitude/notes/2026-11-28-complete-restoration-continuation-entry.md","bytes":19961,"sha256":"d8c5ec7dc4522e87b448ba3bcd013628e373c776a1774d2c416c53c80ef543db","git_blob_sha":"838f962c5453be7a881e81243c2910f5f0a52b71"},"science19":{"role":"science","name":"fixed-fejer-meridian-bhalf-science-complete-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-science-complete-ready.json","bytes":90652,"sha256":"242dd96148ddee96cf829433a4f399e2a2bc052671a92905722c8de8110f2c67","git_blob_sha":"9c4c28ef3c5b189e094c65f51038fafeef48bc48","fixed_publication_commit":"543cfdf281c9bcd0f9b13197721b003a275c5967"},"pure19":{"role":"pure","name":"fixed-fejer-meridian-bhalf-pure-complete-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-pure-complete-ready.json","bytes":80254,"sha256":"8a5f9ff71bc598f77b25c36aeaad833f048dc6b4d218de2df44fda92709e73b7","git_blob_sha":"202b6ca81c72c009c34c04094ef234db2e337328","fixed_publication_commit":"543cfdf281c9bcd0f9b13197721b003a275c5967"},"display19":{"role":"display","name":"fixed-fejer-meridian-bhalf-complete-display-correspondence.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-complete-display-correspondence.json","bytes":25057,"sha256":"cc564e5c273367242aae226913a0dd82ae5b88b3e166fbcbb8da68d6c04edb2d","git_blob_sha":"fac08bdbafbefd0e599687e2b7f0a5c6e71382e7","fixed_publication_commit":"543cfdf281c9bcd0f9b13197721b003a275c5967"}},"policy":{"path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_restoration_damping_continuation.py","bytes":18684,"sha256":"be523c77d488eaaaab9a18f6aa556283362f66bee0916f9d1489cd2b51c1b710","git_blob_sha":"05eb88969c5e83cf2f01fcb3f02e40f4cbea0775"},"policy_design":{"path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-restoration-continuation-complete-integration-design.json","bytes":9970,"sha256":"66cef891231f05135c1202ffe95d64695de0d8b6cb4152c4551e0f0e46e827a5","git_blob_sha":"03d7e0fca68437e64028adf78f3266b50f7f7ed2"},"policy_mathematical_note":{"path":"topics/visible-flex-larger-amplitude/notes/2026-11-28-complete-restoration-continuation-source-design.md","bytes":24517,"sha256":"6f524129b8a595e2991f90624506f52fd5271304493152dc05820681eca127d5","git_blob_sha":"28116820d3b4d0a8e61a5c71fa1d7164da0f601f"},"added_external_peer_records":[{"run_id":"46076669320","run_attempt":1,"run_attempt_key":"46076669320/1","official_url":"https://github.com/Rogerhu12/math-research-public/actions/runs/46076669320","official_workflow_path":".github/workflows/visible-larger-20261127-parallel19.yml","official_head_sha":"543cfdf281c9bcd0f9b13197721b003a275c5967","official_run_started_at":"2026-11-27T22:26:37Z","official_status_at_read":"in_progress","official_conclusion_at_read":null,"official_updated_at":"2026-11-27T22:26:40Z","observed_utc":"2026-11-27 23:21:13 UTC","declared_driver_source_sha256":"10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f","complete_scientific_parameter_record":{"name":"fixed-fejer-meridian-bhalf-science-complete-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-science-complete-ready.json","bytes":90652,"sha256":"242dd96148ddee96cf829433a4f399e2a2bc052671a92905722c8de8110f2c67","git_blob_sha":"9c4c28ef3c5b189e094c65f51038fafeef48bc48","fixed_publication_commit":"543cfdf281c9bcd0f9b13197721b003a275c5967"},"actual_scientific_final_report_sha256":null,"actual_final_checkpoint_sha256":null,"complete_typed_or_accepted_history_available":false,"unknown_history_is_not_empty":true,"not_a_new_typed_transfer_input":true},{"run_id":"46079535427","run_attempt":1,"run_attempt_key":"46079535427/1","official_url":"https://github.com/Rogerhu12/math-research-public/actions/runs/46079535427","official_workflow_path":".github/workflows/visible-larger-20261127-parallel20.yml","official_head_sha":"85cd235221ace28158625a7ced52a24551b509eb","official_run_started_at":"2026-11-27T22:55:41Z","official_status_at_read":"in_progress","official_conclusion_at_read":null,"official_updated_at":"2026-11-27T22:55:44Z","observed_utc":"2026-11-27 23:21:13 UTC","declared_driver_source_sha256":"10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f","complete_scientific_parameter_record":{"name":"fixed-fejer-meridian-bhalf-mu001-science-complete-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-mu001-science-complete-ready.json","sha256":"89b437a4986b3172d281b4928353072d15a15f2cebbb7a1fd8d973880d5166ca","bytes":97019,"git_blob_sha":"598b4cdf62021a66b54c22b71171722027f1c0b5","fixed_publication_commit":"85cd235221ace28158625a7ced52a24551b509eb"},"actual_scientific_final_report_sha256":null,"actual_final_checkpoint_sha256":null,"complete_typed_or_accepted_history_available":false,"unknown_history_is_not_empty":true,"not_a_new_typed_transfer_input":true},{"run_id":"46084442413","run_attempt":1,"run_attempt_key":"46084442413/1","official_url":"https://github.com/Rogerhu12/math-research-public/actions/runs/46084442413","official_workflow_path":".github/workflows/visible-larger-20261127-parallel21.yml","official_head_sha":"95ae5c2399664bed1b9597611b7385cb4e8d6d5e","official_run_started_at":"2026-11-27T23:47:39Z","official_status_at_parent_record":"in_progress","official_conclusion_at_parent_record":null,"status_is_parent_provided_observation_not_a_new_API_poll":true,"declared_driver_source_sha256":"10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f","complete_scientific_parameter_record":{"name":"fixed-fejer-meridian-bfiveeighths-science-complete-ready.json","path":"computations/fixed-fejer-meridian-bfiveeighths-science-complete-ready.json","sha256":"6838b79823f398d930982b2d10fd28baf5a6a2f60eb866403331bfd34eb67d9d","bytes":97307,"git_blob_sha":"6da95445b088f8593ff0f5fb14d76167b26a7a21"},"complete_pure_parameter_record":{"name":"fixed-fejer-meridian-bfiveeighths-pure-complete-ready.json","path":"computations/fixed-fejer-meridian-bfiveeighths-pure-complete-ready.json","sha256":"b750fd865256366a5fcf6b020570a74c053ad853d4b34d0ff983ad3895388822","bytes":86702,"git_blob_sha":"5b2b58e75572b75ce499c8983adf3ba20278211b"},"complete_parameter_delivery_record":{"name":"fixed-fejer-bfiveeighths-complete-parameter-delivery.json","path":"computations/fixed-fejer-bfiveeighths-complete-parameter-delivery.json","sha256":"550ae5ff18b9022bed7ec000c9c63b5958701f632aea100f59f338da249c971e","bytes":52529,"git_blob_sha":"8125f12b1c6df083945afe30bb412577428b5b32"},"actual_scientific_final_report_sha256":null,"actual_final_checkpoint_sha256":null,"complete_typed_or_accepted_history_available":false,"unknown_history_is_not_empty":true,"not_a_new_typed_transfer_input":true},{"run_id":"46090913581","run_attempt":1,"run_attempt_key":"46090913581/1","official_url":"https://github.com/Rogerhu12/math-research-public/actions/runs/46090913581","official_head_sha":"18081452c5181d958bb5432c4045c067bf1d1caa","official_created_at":"2026-11-28T01:00:48Z","official_status_at_parent_record":"in_progress","official_conclusion_at_parent_record":null,"known_job_id":"140811337445","status_is_parent_provided_observation_not_a_new_API_poll":true,"declared_driver_source_sha256":"095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec","complete_scientific_parameter_record":{"path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-bhalf-science-complete-ready.json","role":"science","name":"fixed-fejer-paired-halfwave-bhalf-science-complete-ready.json","bytes":94317,"sha256":"f60ce7bc9c0a6392a84fe73f5a9fcdf347ad294add8066c57233003389a0818d","git_blob_sha":"a8348cd238af32a441ebd5c63bc913cb6157891b"},"complete_source_binding":{"path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-current-complete-runtime-binding.json","bytes":67013,"sha256":"6dd246a030ffaf9e58e750c135e26424b12668b182f0e6a59726c2af006c1638","git_blob_sha":"4f20af6e3663bdf69aca7193bc29624dc706411c"},"physical_seed_mechanism":"paired-halfwave; different from this unchanged full-wave run23 seed","actual_scientific_final_report_sha256":null,"actual_final_checkpoint_sha256":null,"complete_typed_or_accepted_history_available":false,"unknown_history_is_not_empty":true,"not_a_new_typed_transfer_input":true}],"terminal_peer_17":{"run_id":"46053911348","attempt":1,"run_attempt_key":"46053911348/1","official_status":"completed","official_conclusion":"cancelled","official_updated_at":"2026-11-28T00:53:34Z","cancellation_cause":null,"official_status_is_from_whole_published_note_not_a_new_poll":true,"complete_actual_note":{"path":"topics/visible-flex-larger-amplitude/notes/2026-11-27-run17-wide-seed-actual-mathematics.md","bytes":81523,"sha256":"2bdbea9519316f03bd8680d99a381d691810a3f880106f868bfbcc5277b415fc","git_blob_sha":"d3858027922738a6df247eb109ccfd9d45850b80","fixed_publication_commit":"54ac2aa5bc33a4383bc6528f4f5213111daac113"},"two_input_returns_zero":true,"scientific_child_natural_return_observed":false,"scientific_child_exit_code":null,"final_report_sha256":null,"final_checkpoint_sha256":null,"complete_typed_history":null,"last_observed_accepted_direction_count":3,"last_observed_current_point_sha256":"e2c1ad7e37ff214220c2f5e79427dee8e4831a1a3df4aee06c013589c6f73734","last_observed_trial_point_sha256":"52bca852ac42a0ab69521317851e2f5b786df39e93bd53dcc214cf5f1464609b","last_trial_statistics_or_geometry_or_decision":null,"observation_is_not_transferred_as_a_current_field_or_typed_history":true,"unknown_history_is_not_empty":true},"shared_historical_fields":["complete_original_parameter_metadata","pre_repair_current_runtime_source_records"],"serialization":"Compact UTF-8 JSON plus one newline. Every original step field, all numerical arguments, formal/live selectors and budgets are retained. Exactly two historical metadata values are losslessly shared by exact complete parent plus JSON pointer; all replaced current metadata remain recoverable from the whole immediate parent. New whole-file bytes/SHA do not claim to equal the parent."};

const EXPECTED={"display":{"role":"display","name":"fixed-fejer-restoration-continuation-bhalf-complete-display-correspondence.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-restoration-continuation-bhalf-complete-display-correspondence.json","bytes":30357,"sha256":"5e1ab150d09a0c8c893fb8ece293d2e3c6acf5a6077f2bd01cd0c8df5c5edc18","git_blob_sha":"174a0d77589e9cb1742236c5c5cbc5b64f1ceee4"},"science":{"role":"science","name":"fixed-fejer-restoration-continuation-bhalf-science-complete-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-restoration-continuation-bhalf-science-complete-ready.json","bytes":98798,"sha256":"95f7a9337ec20245b4c7f9c35ba74081b718643222a4c4023299532d7562d34f","git_blob_sha":"2fcf6bda73d3fc050fd8e9a9b81e97511031e18d"},"pure":{"role":"pure","name":"fixed-fejer-restoration-continuation-bhalf-pure-complete-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-restoration-continuation-bhalf-pure-complete-ready.json","bytes":88534,"sha256":"536b7ddb2ff5eaa71f7252e96061c1f44547a62618955efc45c4db5db854f686","git_blob_sha":"189138a03de3aff0e2cc5644570b59b7bca49969"}};

function clone(x){return JSON.parse(JSON.stringify(x));}
function exactReference(record,pointer,scope){
 return {schema:"exact-whole-parent-JSON-value-reference-v1",complete_parent_file:clone(record),
  json_pointer:pointer,scope,entire_original_value_retained_in_bound_parent:true,truncated_or_replaced_by_summary:false};
}
function namespaceOnly(value,spec){
 if(typeof value==="string")return value.split(spec.old_namespace).join(spec.namespace);
 if(Array.isArray(value))return value.map(x=>namespaceOnly(x,spec));
 if(value&&typeof value==="object")return Object.fromEntries(Object.entries(value).map(([k,v])=>[k.split(spec.old_namespace).join(spec.namespace),namespaceOnly(v,spec)]));
 return value;
}
function countSelectors(map){return Object.values(map||{}).reduce((n,v)=>n+Object.keys(v).length,0);}
function recoverParentFields(old,out,parent,shared=[]){
 return {whole_parent:clone(parent),shared_original_fields:shared.map(k=>({field:k,json_pointer:"/"+k})),
  replaced_current_fields:Object.keys(old).filter(k=>JSON.stringify(old[k])!==JSON.stringify(out[k]))
   .map(k=>({field:k,json_pointer:"/"+k.replaceAll("~","~0").replaceAll("/","~1")})),
  all_other_original_fields_retained_inline:true,entire_original_value_recovery_is_lossless:true,
  only_new_current_metadata_is_interpreted_as_current:true};
}
function buildDisplay(old,binding,spec){
 const out=clone(old);
 out.schema="complete-fixed-fejer-restoration-continuation-bhalf-display-correspondence-v1";
 out.current_live_mapping=namespaceOnly(old.current_live_mapping,spec);
 out.current_parameter_scope={boundary_total_length:"1/2",profile_delta:"1/32",
  initial_metric_damping:".01",initial_restoration_damping:".01",
  physical_seed_mechanism:"original complete full-wave supported seed, identical mathematical definition to run19; no run22 paired halfwaves",
  algorithm_change:"Only the already-published continuation policy may update the next restoration damping from original completed-direction records after the original update.",
  actual_run_id:null,actual_field_point_sha256:null,actual_model_identity_sha256:null,
  actual_policy_decisions:null,all48_current_scalar_selectors_preserved:true,
  all_historical_mapping_records_retained:true,
  only_live_mapping_file_keys_change_and_all_live_fields_remain_identical:true,
  current_scientific_driver_is_new_and_current_observer_is_original:true};
 out.actual_geometry_producer_source_constant_only=false;
 out.parameter_parent_actual_geometry_producer_source_constant_only=exactReference(spec.parents.display19,
  "/actual_geometry_producer_source_constant_only","Historical producer-pin-only statement retained in the exact parent; the current change is a restoration policy in a complete new driver.");
 out.complete_immediate_display_parent=clone(spec.parents.display19);
 out.complete_current_source_binding=clone(spec.parents.binding);
 out.current_driver=clone(binding.current_complete_runtime_sources.driver);
 out.current_geometry=clone(binding.current_complete_runtime_sources.geometry);
 out.current_normal_operator=clone(binding.current_complete_runtime_sources.endpoint);
 out.current_observer_source_unchanged=true;
 out.current_policy_source=clone(spec.policy);
 out.no_new_live_fields_or_scientific_calls=true;
 out.policy_decisions_are_retained_in_complete_report_and_pure_readout_not_added_to_the48_live_fields=true;
 out.complete_original_parent_field_recovery=recoverParentFields(old,out,spec.parents.display19);
 out.serialization=spec.serialization;
 return out;
}
function buildReady(kind,old,binding,displayRecord,spec){
 const parent=spec.parents[kind+"19"],out=clone(old);
 for(const key of spec.shared_historical_fields)
  out[key]=exactReference(parent,"/"+key,"Entire historical metadata value retained by exact whole immediate parent and JSON pointer; not a summary, truncation or current-source declaration.");
 out.schema="complete-fixed-fejer-restoration-continuation-bhalf-"+kind+"-parameters-v1";
 out.executed=false;
 out.scope="Complete independent fixed-Fejer M160/J923/N2048/32-stage "+kind+
  " with the entire original run19 full-wave b/S=1/2 and delta=1/32 seed, initial metric/restoration damping .01/.01, all original variables, equations, budgets, numerical arguments, accepted/failed direction rules and execution order. The sole mathematical algorithm addition is the published restoration-damping continuation policy after the original update, consuming original returned geometry, row/prediction and accepted-step records for the next restoration direction. No paired-halfwave seed, geometry-first ordering, reduced trial/domain, imported final point or prior certificate is used. All original parameters, sources and unknown historical responsibilities remain bound by whole parents and explicit pointers.";
 out.current_complete_runtime_sources=clone(binding.current_complete_runtime_sources);
 out.current_complete_source_packages=[clone(spec.parents.binding),clone(spec.parents.source_manifest)];
 out.complete_driver_source_role_count=138;
 out.all_original120_source_pairs_retained=true;
 out.all_original137_source_pairs_retained=true;
 out.complete_current_source_role_registry=exactReference(spec.parents.binding,"/complete_current_scientific_registry","All138 complete current scientific source role/name/SHA pairs.");
 out.current_source_role_comparison={original_role_pairs:137,exactly_unchanged_original_pairs:137,replaced_original_pairs:0,
  added_roles:["restoration_damping_policy"],current_role_pairs:138,
  complete_old_registry:exactReference(spec.parents.binding,"/complete_original_scientific_registry","All137 original scientific role pairs, unchanged."),
  complete_current_runtime_sources:19,
  changed_runtime_responsibilities:["driver","reader","launcher"],
  added_runtime_responsibilities:["restoration_damping_policy"],
  scientific_role_count_and_runtime_count_are_distinct:true};
 out.source_constructors=[clone(spec.parents.source_reproducer)];
 out.source_constructors_scope="The current complete source constructor is listed here. The entire prior constructor list and its histories remain in the bound whole immediate parent.";
 out.complete_current_display_correspondence=clone(displayRecord);
 out.complete_parameter_constructor_path=spec.paths.reproducer;
 out.complete_sibling_ready_paths=[spec.paths.science,spec.paths.pure];
 out.all_original_arguments_and_defaults_retained=false;
 out.all_original_numerical_arguments_and_explicit_budget_words_equal_run19=true;
 out.only_current_script_and_output_namespaces_changed_from_wide_parent=false;
 out.complete_current_scientific_source_family_is_identical_to_parent=false;
 out.new_source_patch_or_fixture_or_AST_or_review_gate_added=true;
 out.new_source_patch_scope="True only for the complete new driver/reader/launcher and the explicitly added previously-published policy role. No fixture, AST, replay, review or scientific admission gate is added.";
 out.new_AST_fixture_replay_or_review_gate_added=false;
 out.original_numerical_budgets_not_reduced=true;
 out.complete_parameter_parent=clone(parent);
 out.only_scientific_numerical_argument_change_from_immediate_parent={changed_numerical_argument_words:[],
  seed_boundary_total_length:"1/2",seed_profile_delta:"1/32",initial_metric_damping:".01",
  initial_restoration_damping:".01",next_restoration_damping_may_change_by_complete_source_policy:true};
 out.planned_seed_parameters=clone(old.planned_seed_parameters);
 out.complete_choice_note=clone(spec.policy_mathematical_note);
 out.complete_policy_integration_design=clone(spec.policy_design);
 out.complete_policy_integration_source_note=clone(spec.parents.source_note);
 out.restoration_policy_scope={
  source:clone(spec.policy),initial_metric_damping:".01",initial_restoration_damping:".01",
  original_failure_times4_update_preserved:true,
  original_metric_damping_update_preserved:true,
  original_acceptance_and_line_search_inequalities_preserved:true,
  uses_only_original_returned_direction_values:true,
  no_new_F_J_root_quadrature_geometry_or_KKT_gate:true,
  eligible_literal_full_step_alpha:1,agreement_ratio_threshold:.75,
  decrease_factor:10,restoration_damping_floor:1e-8,
  actual_decisions:null,actual_decrease_count:null,actual_speed_or_improvement:null,
  exact_conditions_and_arithmetic_are_the_whole_bound_policy_not_this_description:true,
  complete_policy_validation_in_new_reader:true};
 for(const key of ["actual_run_id","actual_run_attempt","actual_report_sha256","actual_point_sha256",
  "actual_model_identity_sha256","actual_geometry_or_acceptance_result",
  "future_actual_reference_identity_sha256","future_actual_target_file_sha256",
  "future_actual_model_identity_sha256","future_actual_final_checkpoint_sha256"])out[key]=null;
 out.actual_existing_input_scope={...clone(old.actual_existing_input_scope),run:null,attempt:null,
  two_complete_necessary_inputs_already_returned:false,reference_sha256:null,preparation_sha256:null,
  actual_model_identity_sha256:null,fresh_independent_inputs_required:true,no_cross_runner_raw_migration:true};
 out.new_complete_solver_report_or_point_or_fees_assumed=false;
 out.future_controller_admission_after_actual_natural_return_only=false;
 out.independent_science_requires_only_own_two_complete_reference_inputs=true;
 out.prior_runner_natural_return_required=false;
 const external=clone(old.external_unregistered_peer_obligations);
 for(const record of spec.added_external_peer_records){
  const pair=[record.run_attempt_key,record.declared_driver_source_sha256],previous=external.find(x=>x[0]===pair[0]);
  if(previous&&JSON.stringify(previous)!==JSON.stringify(pair))throw Error("Conflicting external peer source");
  if(!previous)external.push(pair);
 }
 out.external_unregistered_peer_obligations=external;
 out.external_peer_status="The original six external responsibilities and original five supported CLI pairs are unchanged. All known original provenance and unknown final/typed obligations remain. Additional runs19/20/21 retain their actual10fa sources; actual run22 retains its different095bf halfwave source. These are external history declarations, not new PARENT_FAMILIES, not actual typed-transfer inputs, and not current9db3 sources. Dated statuses in parent records remain historical observations; the separately bound full run17 note records its actual official cancellation without manufacturing a natural scientific return or final history.";
 out.additional_external_peer_records=clone(spec.added_external_peer_records);
 out.known_run17_official_terminal_evidence=clone(spec.terminal_peer_17);
 out.supported_original_five_peer_CLI_pairs_unchanged=true;
 out.original_five_pending_CLI_pairs_and_external_obligations_are_distinct=true;
 out.no_unknown_peer_final_or_typed_priority_filled=true;
 out.steps=namespaceOnly(old.steps,spec);
 out.steps[0].id=(kind==="science"?"complete-":"actual-")+spec.namespace+"-20261128";
 out.steps[0].script=binding.current_complete_runtime_sources[kind==="science"?"launcher":"reader"].path;
 out.steps[0].scope="Complete restoration-continuation b/S=1/2, delta=1/32 "+kind+
  "; every original numerical argument, budget, complete domain, variable and row responsibility, output/cleanup contract and formal/live selector is retained from whole run19. Only the current source/namespace and completed-direction adaptive next-mu policy differ. The original full-wave seed and all original acceptance rules remain; no prior accepted point, root, checkpoint or certificate is inherited.";
 out.current_step_delta={
  id_before:old.steps[0].id,id_after:out.steps[0].id,
  script_before:old.steps[0].script,script_after:out.steps[0].script,
  old_namespace:spec.old_namespace,new_namespace:spec.namespace,
  changed_argument_words:old.steps[0].args.flatMap((v,i)=>v===out.steps[0].args[i]?[]:[{index:i,before:v,after:out.steps[0].args[i]}]),
  old_argument_count:old.steps[0].args.length,current_argument_count:out.steps[0].args.length,
  complete_original_formal_selector_count:countSelectors(old.steps[0].summary),
  complete_current_formal_selector_count:countSelectors(out.steps[0].summary),
  complete_current_live_selector_count:countSelectors(out.steps[0].progress_summary),
  all_scientific_numeric_words_and_original_CLI_flags_unchanged:true,
  same_original_output_cleanup_and_reference_cache_retention_policy:true,
  historical_whole_step:exactReference(parent,"/steps/0","Entire original step including all argv, output, selector, cleanup and scope fields.")};
 out.complete_current_source_binding=clone(spec.parents.binding);
 out.current_runtime_role_count=19;
 out.current_new_complete_entry_source_count=3;
 out.current_reused_complete_policy_source_count=1;
 out.intended_independent_runner_label="parallel23";
 out.current_field_or_continuous_certificate_claimed=false;
 out.physical_seed_definition_identical_to_run19_fullwave=true;
 out.run22_halfwave_source_or_seed_not_mixed=true;
 out.geometry_first_ordering_not_added=true;
 out.serialization=spec.serialization;
 out.complete_immediate_parent_metadata_recovery=recoverParentFields(old,out,parent,spec.shared_historical_fields);
 return out;
}


function fail(message){throw new Error(message);}
function same(a,b,label){if(JSON.stringify(a)!==JSON.stringify(b))fail(label);}
function wholeIdentity(bytes){return {bytes:bytes.length,sha256:createHash("sha256").update(bytes).digest("hex")};}
function verifyWhole(bytes,record,label){
 const actual=wholeIdentity(bytes);
 if(actual.bytes!==record.bytes||actual.sha256!==record.sha256)fail(label+" whole bytes or SHA256 differ");
 if(actual.bytes>=100000)fail(label+" exceeds the explicit complete single-file limit");
 return actual;
}
function readWhole(repo,record,label){
 const bytes=readFileSync(resolve(repo,record.path));
 verifyWhole(bytes,record,label);
 return bytes;
}
function readParent(repo,record,label){return JSON.parse(readWhole(repo,record,label).toString("utf8"));}
function materialize(value,record,outdir){
 const bytes=Buffer.from(JSON.stringify(value)+"\n","utf8");
 verifyWhole(bytes,record,record.role+" generated whole parameter");
 const path=resolve(outdir,record.path);
 mkdirSync(dirname(path),{recursive:true});writeFileSync(path,bytes);
 return {...record,generated_path:path};
}
function inspectSourceBinding(binding){
 if(binding.original_scientific_role_count!==137||binding.current_scientific_role_count!==138)
  fail("Exact137-parent/138-current role counts required");
 const old=binding.complete_original_scientific_registry,current=binding.complete_current_scientific_registry;
 if(Object.keys(old).length!==137||Object.keys(current).length!==138)fail("Full registry omitted roles");
 for(const [role,pair] of Object.entries(old))same(current[role],pair,"Changed original role pair: "+role);
 same(Object.keys(current).filter(role=>!(role in old)),["restoration_damping_policy"],"Unexpected added source roles");
 same(current.restoration_damping_policy,[SPEC.policy.path.slice(SPEC.topic.length+1),SPEC.policy.sha256],"Policy source pair");
 same(binding.replaced_original_scientific_roles,[],"The scientific registry changes no existing pair");
 same(binding.added_scientific_roles,["restoration_damping_policy"],"Added policy role");
 if(binding.every_original_source_pair_preserved_exactly!==true)fail("Original complete sources must remain");
 if(binding.current_complete_runtime_source_count!==19||Object.keys(binding.current_complete_runtime_sources).length!==19)
  fail("All19 complete current runtime responsibilities required");
 if(binding.complete_new_file_count!==3||binding.complete_new_files.length!==3)
  fail("Expected exactly three complete new entry source files");
 same(binding.complete_reused_policy_source,SPEC.policy,"The published complete policy changed");
}
function inspectCompleteStep(kind,old,current){
 if(old.steps.length!==1||current.steps.length!==1)fail("One complete step required per ready file");
 const reverse=namespaceOnly(current.steps[0],{old_namespace:SPEC.namespace,namespace:SPEC.old_namespace});
 for(const key of ["id","script","scope"])reverse[key]=old.steps[0][key];
 same(reverse,old.steps[0],"The entire original "+kind+" step was not preserved by its exact mapping");
 if(current.steps[0].args.length!==(kind==="science"?157:7))fail("Complete argument count");
 if(countSelectors(current.steps[0].summary)!==(kind==="science"?458:445))fail("Complete formal selector count");
 if(countSelectors(current.steps[0].progress_summary)!==(kind==="science"?48:0))fail("Complete live mapping");
 for(const key of Object.keys(old))if(!(key in current))fail("Lost original metadata field: "+key);
 for(const key of SPEC.shared_historical_fields){
  const ref=current[key];
  same(ref.complete_parent_file,SPEC.parents[kind+"19"],"Historical whole parent changed");
  if(ref.json_pointer!=="/"+key||ref.truncated_or_replaced_by_summary!==false)
   fail("Shared historical object is not a whole-value reference");
 }
 same(current.external_unregistered_peer_obligations.slice(0,old.external_unregistered_peer_obligations.length),
  old.external_unregistered_peer_obligations,"Original external peer sources changed");
 if(current.external_unregistered_peer_obligations.length!==10)fail("Expected original six plus four known actual external peers");
 for(const record of SPEC.added_external_peer_records)
  same(current.external_unregistered_peer_obligations.find(x=>x[0]===record.run_attempt_key),
   [record.run_attempt_key,record.declared_driver_source_sha256],"External peer source was relabeled");
 if(current.known_run17_official_terminal_evidence.scientific_child_natural_return_observed!==false)
  fail("Official cancellation is not a natural scientific return");
}
function parseArgs(argv){
 const out={};
 for(let i=0;i<argv.length;i++){
  const key=argv[i];
  if(key!=="--repo"&&key!=="--output-directory")fail("Unknown argument: "+key);
  if(out[key]!==undefined||i+1>=argv.length)fail("Missing or duplicate "+key);
  out[key]=argv[++i];
 }
 if(!out["--repo"]||!out["--output-directory"])
  fail("Usage: node reproduce_fixed_fejer_restoration_continuation_bhalf_parameters.mjs --repo <complete-repository> --output-directory <generated-tree>");
 return out;
}
function main(){
 const args=parseArgs(process.argv.slice(2));
 const binding=readParent(args["--repo"],SPEC.parents.binding,"Complete current source binding");
 const science19=readParent(args["--repo"],SPEC.parents.science19,"Complete run19 science");
 const pure19=readParent(args["--repo"],SPEC.parents.pure19,"Complete run19 pure");
 const display19=readParent(args["--repo"],SPEC.parents.display19,"Complete run19 display");
 readWhole(args["--repo"],SPEC.terminal_peer_17.complete_actual_note,"Whole run17 terminal evidence");
 inspectSourceBinding(binding);
 const display=buildDisplay(display19,binding,SPEC);
 const science=buildReady("science",science19,binding,EXPECTED.display,SPEC);
 const pure=buildReady("pure",pure19,binding,EXPECTED.display,SPEC);
 inspectCompleteStep("science",science19,science);
 inspectCompleteStep("pure",pure19,pure);
 same(namespaceOnly(display.current_live_mapping,{old_namespace:SPEC.namespace,namespace:SPEC.old_namespace}),
  display19.current_live_mapping,"The48 live scalar fields changed beyond namespace");
 const outputs=[materialize(display,EXPECTED.display,args["--output-directory"]),
  materialize(science,EXPECTED.science,args["--output-directory"]),
  materialize(pure,EXPECTED.pure,args["--output-directory"])];
 process.stdout.write(JSON.stringify({schema:"complete-restoration-continuation-bhalf-parameter-text-reproduction-v1",
  complete:true,scope:"Complete parameter JSON text construction only; no Python import, AST, scientific stage, test, fixture, approval gate, ref or queue mutation.",
  outputs,science_argument_words:157,pure_argument_words:7,formal_selectors:{science:458,pure:445},
  live_selectors:48,numerical_CLI_word_changes:0,original_scientific_role_pairs_retained:137,
  added_scientific_roles:1,current_scientific_roles:138,current_runtime_sources:19,
  original_supported_peer_CLI_pairs:5,external_obligations:10,
  actual_run_id:null,actual_point_sha256:null,actual_policy_decisions:null,actual_final_report_sha256:null})+"\n");
}
main();
