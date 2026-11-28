#!/usr/bin/env node
// Complete run22 parameter text constructor. This is not a scientific stage or an admission requirement.
// All original step values are retained; exactly two historical metadata objects are shared by whole parent + JSON pointer.
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {resolve,dirname} from 'node:path';
import {createHash} from 'node:crypto';

const SPEC={"schema":"complete-fixed-fejer-paired-halfwave-bhalf-parameter-reproduction-spec-v1","prepared_utc":"2026-11-28 00:32:24 UTC","repository":"Rogerhu12/math-research-public","topic":"topics/visible-flex-larger-amplitude","old_namespace":"fixed-fejer-meridian-batched-bhalf-first","namespace":"fixed-fejer-paired-halfwave-bhalf-first","paths":{"science":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-bhalf-science-complete-ready.json","pure":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-bhalf-pure-complete-ready.json","display":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-bhalf-complete-display-correspondence.json","reproducer":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_paired_halfwave_bhalf_parameters.mjs","note":"topics/visible-flex-larger-amplitude/notes/2026-11-28-paired-halfwave-bhalf-complete-parameters.md","manifest":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-bhalf-complete-parameter-delivery.json"},"parents":{"binding":{"path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-current-complete-runtime-binding.json","bytes":67013,"sha256":"6dd246a030ffaf9e58e750c135e26424b12668b182f0e6a59726c2af006c1638","git_blob_sha":"4f20af6e3663bdf69aca7193bc29624dc706411c"},"science19":{"role":"science","name":"fixed-fejer-meridian-bhalf-science-complete-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-science-complete-ready.json","bytes":90652,"sha256":"242dd96148ddee96cf829433a4f399e2a2bc052671a92905722c8de8110f2c67","git_blob_sha":"9c4c28ef3c5b189e094c65f51038fafeef48bc48","fixed_publication_commit":"543cfdf281c9bcd0f9b13197721b003a275c5967"},"pure19":{"role":"pure","name":"fixed-fejer-meridian-bhalf-pure-complete-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-pure-complete-ready.json","bytes":80254,"sha256":"8a5f9ff71bc598f77b25c36aeaad833f048dc6b4d218de2df44fda92709e73b7","git_blob_sha":"202b6ca81c72c009c34c04094ef234db2e337328","fixed_publication_commit":"543cfdf281c9bcd0f9b13197721b003a275c5967"},"display19":{"role":"display","name":"fixed-fejer-meridian-bhalf-complete-display-correspondence.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-complete-display-correspondence.json","bytes":25057,"sha256":"cc564e5c273367242aae226913a0dd82ae5b88b3e166fbcbb8da68d6c04edb2d","git_blob_sha":"fac08bdbafbefd0e599687e2b7f0a5c6e71382e7","fixed_publication_commit":"543cfdf281c9bcd0f9b13197721b003a275c5967"}},"proof":{"path":"topics/visible-flex-larger-amplitude/results/R724-paired-halfwave-central-seed-and-complete-source-identity.md","bytes":25314,"sha256":"fea22bde71c3780bead8b7448c5fc057e64f8e6429f97c1b3155e1d13e32f878","git_blob_sha":"e2dbf61239c0092025ef8a5c0f6cac80b4e87d83","fixed_publication_commit":"21bb485ad77530cf7623f9ef5c01b77294bc4ca3"},"changed_source_roles":["root_packets","analytic_J3","analytic_J3_binding","seed_reference","meridian","geometry","endpoint","new_moment_input","reference_calibration","frame_C1","stage_matrices","envelope_transfer","adjacent_matrices","analytic_frame","closure_values","detached_meridian_values","batched_geometry_binding"],"added_external_peer_records":[{"run_id":"46076669320","run_attempt":1,"run_attempt_key":"46076669320/1","official_url":"https://github.com/Rogerhu12/math-research-public/actions/runs/46076669320","official_workflow_path":".github/workflows/visible-larger-20261127-parallel19.yml","official_head_sha":"543cfdf281c9bcd0f9b13197721b003a275c5967","official_run_started_at":"2026-11-27T22:26:37Z","official_status_at_read":"in_progress","official_conclusion_at_read":null,"official_updated_at":"2026-11-27T22:26:40Z","observed_utc":"2026-11-27 23:21:13 UTC","declared_driver_source_sha256":"10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f","complete_scientific_parameter_record":{"name":"fixed-fejer-meridian-bhalf-science-complete-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-science-complete-ready.json","bytes":90652,"sha256":"242dd96148ddee96cf829433a4f399e2a2bc052671a92905722c8de8110f2c67","git_blob_sha":"9c4c28ef3c5b189e094c65f51038fafeef48bc48","fixed_publication_commit":"543cfdf281c9bcd0f9b13197721b003a275c5967"},"actual_scientific_final_report_sha256":null,"actual_final_checkpoint_sha256":null,"complete_typed_or_accepted_history_available":false,"unknown_history_is_not_empty":true,"not_a_new_typed_transfer_input":true},{"run_id":"46079535427","run_attempt":1,"run_attempt_key":"46079535427/1","official_url":"https://github.com/Rogerhu12/math-research-public/actions/runs/46079535427","official_workflow_path":".github/workflows/visible-larger-20261127-parallel20.yml","official_head_sha":"85cd235221ace28158625a7ced52a24551b509eb","official_run_started_at":"2026-11-27T22:55:41Z","official_status_at_read":"in_progress","official_conclusion_at_read":null,"official_updated_at":"2026-11-27T22:55:44Z","observed_utc":"2026-11-27 23:21:13 UTC","declared_driver_source_sha256":"10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f","complete_scientific_parameter_record":{"name":"fixed-fejer-meridian-bhalf-mu001-science-complete-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-mu001-science-complete-ready.json","sha256":"89b437a4986b3172d281b4928353072d15a15f2cebbb7a1fd8d973880d5166ca","bytes":97019,"git_blob_sha":"598b4cdf62021a66b54c22b71171722027f1c0b5","fixed_publication_commit":"85cd235221ace28158625a7ced52a24551b509eb"},"actual_scientific_final_report_sha256":null,"actual_final_checkpoint_sha256":null,"complete_typed_or_accepted_history_available":false,"unknown_history_is_not_empty":true,"not_a_new_typed_transfer_input":true},{"run_id":"46084442413","run_attempt":1,"run_attempt_key":"46084442413/1","official_url":"https://github.com/Rogerhu12/math-research-public/actions/runs/46084442413","official_workflow_path":".github/workflows/visible-larger-20261127-parallel21.yml","official_head_sha":"95ae5c2399664bed1b9597611b7385cb4e8d6d5e","official_run_started_at":"2026-11-27T23:47:39Z","official_status_at_parent_record":"in_progress","official_conclusion_at_parent_record":null,"status_is_parent_provided_observation_not_a_new_API_poll":true,"declared_driver_source_sha256":"10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f","complete_scientific_parameter_record":{"name":"fixed-fejer-meridian-bfiveeighths-science-complete-ready.json","path":"computations/fixed-fejer-meridian-bfiveeighths-science-complete-ready.json","sha256":"6838b79823f398d930982b2d10fd28baf5a6a2f60eb866403331bfd34eb67d9d","bytes":97307,"git_blob_sha":"6da95445b088f8593ff0f5fb14d76167b26a7a21"},"complete_pure_parameter_record":{"name":"fixed-fejer-meridian-bfiveeighths-pure-complete-ready.json","path":"computations/fixed-fejer-meridian-bfiveeighths-pure-complete-ready.json","sha256":"b750fd865256366a5fcf6b020570a74c053ad853d4b34d0ff983ad3895388822","bytes":86702,"git_blob_sha":"5b2b58e75572b75ce499c8983adf3ba20278211b"},"complete_parameter_delivery_record":{"name":"fixed-fejer-bfiveeighths-complete-parameter-delivery.json","path":"computations/fixed-fejer-bfiveeighths-complete-parameter-delivery.json","sha256":"550ae5ff18b9022bed7ec000c9c63b5958701f632aea100f59f338da249c971e","bytes":52529,"git_blob_sha":"8125f12b1c6df083945afe30bb412577428b5b32"},"actual_scientific_final_report_sha256":null,"actual_final_checkpoint_sha256":null,"complete_typed_or_accepted_history_available":false,"unknown_history_is_not_empty":true,"not_a_new_typed_transfer_input":true}],"shared_historical_fields":["complete_original_parameter_metadata","pre_repair_current_runtime_source_records"],"serialization":"Compact UTF-8 JSON plus one newline. All complete step values, numerical arguments, selectors and budgets are retained. Two historical objects are losslessly shared through their complete whole parent and JSON pointer; every replaced current metadata value remains recoverable from the complete immediate parent."};

const EXPECTED={"display":{"role":"display","name":"fixed-fejer-paired-halfwave-bhalf-complete-display-correspondence.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-bhalf-complete-display-correspondence.json","bytes":30196,"sha256":"472e385c78f39a2b3bb582a162b642e2e349696708aa8b3d130e0a1fa2c8403c","git_blob_sha":"4d15d836b40ba5547542e7468dfe0aff52d07934"},"science":{"role":"science","name":"fixed-fejer-paired-halfwave-bhalf-science-complete-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-bhalf-science-complete-ready.json","bytes":94317,"sha256":"f60ce7bc9c0a6392a84fe73f5a9fcdf347ad294add8066c57233003389a0818d","git_blob_sha":"a8348cd238af32a441ebd5c63bc913cb6157891b"},"pure":{"role":"pure","name":"fixed-fejer-paired-halfwave-bhalf-pure-complete-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-bhalf-pure-complete-ready.json","bytes":84075,"sha256":"1a7649f702c005eadd7b0c9d8b4a064f0ed70be37dabc449bbc1e9afcf3b8cc9","git_blob_sha":"76e73edb425a30cda39c94275ee193914a319fb4"}};

function clone(x){return JSON.parse(JSON.stringify(x));}

function exactReference(record,pointer,description){
 return {schema:"exact-whole-parent-JSON-value-reference-v1",complete_parent_file:clone(record),
  json_pointer:pointer,scope:description,entire_original_value_retained_in_bound_parent:true,
  truncated_or_replaced_by_summary:false};
}

function namespaceOnly(value,spec){
 if(typeof value==="string")return value.split(spec.old_namespace).join(spec.namespace);
 if(Array.isArray(value))return value.map(x=>namespaceOnly(x,spec));
 if(value&&typeof value==="object")return Object.fromEntries(Object.entries(value).map(([k,v])=>[k.split(spec.old_namespace).join(spec.namespace),namespaceOnly(v,spec)]));
 return value;
}

function countSelectors(map){return Object.values(map||{}).reduce((n,v)=>n+Object.keys(v).length,0);}

function buildDisplay(old,binding,spec){
 const out=clone(old);
 out.schema="complete-fixed-fejer-paired-halfwave-bhalf-display-correspondence-v1";
 out.current_live_mapping=namespaceOnly(old.current_live_mapping,spec);
 out.current_parameter_scope={boundary_total_length:"1/2",profile_delta:"1/32",
  physical_seed_mechanism:"paired halfwaves +lambda*h_delta(t/2), -lambda*h_delta(t/2) on the two equal central intervals",
  actual_run_id:null,actual_field_point_sha256:null,actual_model_identity_sha256:null,
  all48_current_scalar_selectors_preserved:true,all_historical_mapping_records_retained:true,
  only_current_runner_output_namespace_changed:false,
  only_live_mapping_file_keys_change_and_all_live_fields_remain_identical:true,
  current_source_family_is_new_and_not_the_original_19_family:true};
 out.actual_geometry_producer_source_constant_only=false;
 out.parameter_parent_actual_geometry_producer_source_constant_only=exactReference(spec.parents.display19,
  "/actual_geometry_producer_source_constant_only","Historical producer-pin-only statement; it does not describe the current halfwave seed mechanism.");
 out.complete_immediate_display_parent=clone(spec.parents.display19);
 out.halfwave_parent_current_live_mapping=exactReference(spec.parents.display19,"/current_live_mapping",
  "Entire immediate run19 live mapping; every scalar name, selector and order is preserved with new current file keys.");
 out.complete_current_source_binding=clone(spec.parents.binding);
 out.current_driver=clone(binding.current_complete_runtime_sources.driver);
 out.current_geometry=clone(binding.current_complete_runtime_sources.geometry);
 out.current_normal_operator=clone(binding.current_complete_runtime_sources.endpoint);
 out.current_observer_source_unchanged=true;
 out.no_new_live_fields_or_scientific_calls=true;
 out.current_run_and_input_model_hashes_not_inferred=true;
 out.complete_original_parent_field_recovery={whole_parent:clone(spec.parents.display19),
  replaced_current_fields:Object.keys(old).filter(k=>JSON.stringify(old[k])!==JSON.stringify(out[k]))
   .map(k=>({field:k,json_pointer:"/"+k.replaceAll("~","~0").replaceAll("/","~1")})),
  all_other_original_fields_retained_inline:true};
 out.serialization=spec.serialization;
 return out;
}

function buildReady(kind,old,binding,displayRecord,spec){
 const parent=spec.parents[kind+"19"];
 const out=clone(old);
 for(const key of spec.shared_historical_fields){
  out[key]=exactReference(parent,"/"+key,
   "The entire historical object is shared losslessly from its exact complete immediate parent; this is not a truncation or current-source declaration.");
 }
 out.schema="complete-fixed-fejer-paired-halfwave-bhalf-"+kind+"-parameters-v1";
 out.executed=false;
 out.scope="Complete independent fixed-Fejer M160/J923/N2048/32-stage "+kind+
  " using the paired-halfwave physical seed against the entire run19 b/S=1/2, delta=1/32, metric damping .01 and restoration damping .01 baseline. Every numerical argument, variable, budget, domain, original formal/live selector and original five pending CLI pairs is retained. This is a new scientific source family and physical seed mechanism, not a namespace-only relabeling or a transferred accepted field. Current fields and all future actual identities are unknown until the two necessary inputs and this complete new family really return. Original parameter/source history is retained in exact whole parents and explicit pointers.";
 out.current_complete_runtime_sources=clone(binding.current_complete_runtime_sources);
 out.current_complete_source_packages=[{...clone(spec.parents.binding),
  scope:"Actual complete current halfwave source binding: all137 scientific roles, 18 runtime responsibilities and all20 new complete sources."}];
 out.complete_driver_source_role_count=137;
 out.all_original120_source_pairs_retained=false;
 out.complete_current_source_role_registry=exactReference(spec.parents.binding,"/complete_source_role_registry",
  "All137 actual current source role/name/SHA pairs; not a selected subset.");
 out.current_source_role_comparison={complete_parent_registry_scope:"Complete immediate run19 scientific family",
  same_role_names:137,exactly_unchanged_pairs:120,changed_current_pairs:17,
  changed_roles:clone(spec.changed_source_roles),
  complete_old_and_new_records:exactReference(spec.parents.binding,"/complete_changed_source_parent_records",
   "Every changed full source, its full parent and actual current full record; driver/launcher/reader changes are also retained."),
  original_source_files_retained_at_original_paths:true,
  unchanged_original120_historical_subset_claimed:false};
 out.source_constructors_scope="The original source_constructors array is historical parent provenance, unchanged. It does not claim to generate the new halfwave family; actual current complete sources are bound by the new complete runtime binding.";
 out.complete_current_display_correspondence=clone(displayRecord);
 out.complete_parameter_constructor_path=spec.paths.reproducer;
 out.complete_sibling_ready_paths=[spec.paths.science,spec.paths.pure];
 out.all_original_arguments_and_defaults_retained=false;
 out.all_original_numerical_arguments_and_explicit_budget_words_equal_run19=true;
 out.only_current_script_and_output_namespaces_changed_from_wide_parent=false;
 out.complete_current_scientific_source_family_is_identical_to_parent=false;
 out.new_source_patch_or_fixture_or_AST_or_review_gate_added=true;
 out.new_source_patch_scope="True only because the physical paired-halfwave mechanism has a new complete20-source implementation; no fixture, AST, replay, review or scientific admission gate is added.";
 out.new_AST_fixture_replay_or_review_gate_added=false;
 out.original_numerical_budgets_not_reduced=true;
 out.complete_parameter_parent=clone(parent);
 out.only_scientific_numerical_argument_change_from_immediate_parent={
  changed_numerical_argument_words:[],seed_boundary_total_length:"1/2",
  seed_profile_delta:"1/32",metric_damping:".01",restoration_damping:".01",
  mechanism_changed_by_explicit_complete_source:true};
 out.planned_seed_parameters={...clone(old.planned_seed_parameters),
  physical_profile_mechanism:"paired-halfwave",
  first_central_profile:"+lambda*h_delta(t/2)",
  second_central_profile:"-lambda*h_delta(t/2)",
  local_material_t_range:"[0,1]",
  exactly_two_equal_central_intervals_required:true,
  central_intervals_relative:[["5/32","11/32"],["21/32","27/32"]],
  scalar_mean_equation_and_auxiliary_twelve_piece_kernel_preserved_as_mathematical_objects:true,
  current_field_mean_roots_or_working_words_inherited:false,
  complete_new_seed_source:clone(binding.new_complete_sources.find(x=>x.name==="fixed_fejer_paired_halfwave_meridian_reference.py")),
  full_R724_definition_and_scope:clone(spec.proof)};
 out.complete_choice_note=clone(spec.proof);
 for(const key of ["actual_run_id","actual_run_attempt","actual_report_sha256","actual_point_sha256",
  "actual_model_identity_sha256","actual_geometry_or_acceptance_result",
  "future_actual_reference_identity_sha256","future_actual_target_file_sha256",
  "future_actual_model_identity_sha256","future_actual_final_checkpoint_sha256"])out[key]=null;
 out.actual_existing_input_scope={...clone(old.actual_existing_input_scope),
  run:null,attempt:null,two_complete_necessary_inputs_already_returned:false,
  reference_sha256:null,preparation_sha256:null,actual_model_identity_sha256:null,
  fresh_independent_inputs_required:true,no_cross_runner_raw_migration:true};
 out.new_complete_solver_report_or_point_or_fees_assumed=false;
 out.future_controller_admission_after_actual_natural_return_only=false;
 out.independent_science_requires_only_own_two_complete_reference_inputs=true;
 out.prior_runner_natural_return_required=false;
 const external=clone(old.external_unregistered_peer_obligations);
 for(const record of spec.added_external_peer_records){
  const pair=[record.run_attempt_key,record.declared_driver_source_sha256];
  const oldPair=external.find(x=>x[0]===pair[0]);
  if(oldPair&&JSON.stringify(oldPair)!==JSON.stringify(pair))throw Error("peer source conflict");
  if(!oldPair)external.push(pair);
 }
 out.external_unregistered_peer_obligations=external;
 out.external_peer_status="All original six external obligations, all five original supported CLI pairs and complete historical unknowns are retained. Runs19/20/21 are additionally recorded with their true complete10fa source family and complete actual known parameter/start provenance. They are not relabeled as current095bf sources and are not inserted into PARENT_FAMILIES or used as actual typed/final inputs. Published partial observations do not supply their unknown complete final/typed histories.";
 out.halfwave_added_external_peer_records=clone(spec.added_external_peer_records);
 out.supported_original_five_peer_CLI_pairs_unchanged=true;
 out.halfwave_original_five_pending_CLI_pairs_and_external_obligations_are_distinct=true;
 out.halfwave_no_unknown_peer_final_or_typed_priority_filled=true;
 out.steps=namespaceOnly(old.steps,spec);
 out.steps[0].script=binding.current_complete_runtime_sources[kind==="science"?"launcher":"reader"].path;
 out.steps[0].scope="Complete paired-halfwave b/S=1/2, delta=1/32 "+kind+
  "; all original numerical arguments, complete budget, variable/domain/row responsibilities and selector values are retained from the bound whole run19 parent. The current source family and physical profile are explicit new objects; no old accepted state, field value or certificate is inherited.";
 out.halfwave_current_step_delta={
  script_before:old.steps[0].script,script_after:out.steps[0].script,
  old_namespace:spec.old_namespace,new_namespace:spec.namespace,
  changed_argument_words:old.steps[0].args.flatMap((v,i)=>v===out.steps[0].args[i]?[]:[{index:i,before:v,after:out.steps[0].args[i]}]),
  old_argument_count:old.steps[0].args.length,current_argument_count:out.steps[0].args.length,
  complete_original_formal_selector_count:countSelectors(old.steps[0].summary),
  complete_current_formal_selector_count:countSelectors(out.steps[0].summary),
  complete_current_live_selector_count:countSelectors(out.steps[0].progress_summary),
  all_scientific_numeric_words_and_original_CLI_flags_unchanged:true,
  same_original_output_cleanup_and_reference_cache_retention_policy:true,
  historical_whole_step:exactReference(parent,"/steps/0","Every original step field, original source/script, entire argument vector, output, selector, cleanup and scope.")
 };
 out.complete_immediate_parent_metadata_recovery={
  whole_parent:clone(parent),
  shared_original_fields:spec.shared_historical_fields.map(k=>({field:k,json_pointer:"/"+k})),
  replaced_current_fields:Object.keys(old).filter(k=>JSON.stringify(old[k])!==JSON.stringify(out[k]))
   .map(k=>({field:k,json_pointer:"/"+k.replaceAll("~","~0").replaceAll("/","~1")})),
  all_other_original_fields_retained_inline:true,
  entire_original_value_recovery_is_lossless:true,
  only_new_current_metadata_is_interpreted_as_current:true};
 out.complete_current_source_binding=clone(spec.parents.binding);
 out.current_runtime_role_count=18;
 out.current_new_complete_source_count=20;
 out.intended_independent_runner_label="parallel22";
 out.current_mean_or_field_or_continuous_certificate_claimed=false;
 out.physical_seed_model_differs_from_parent_even_when_free_initial_words_match=true;
 out.serialization=spec.serialization;
 return out;
}


function fail(message){throw new Error(message);}
function wholeIdentity(bytes){return {bytes:bytes.length,sha256:createHash("sha256").update(bytes).digest("hex")};}
function verifyWhole(bytes,record,label){
 const actual=wholeIdentity(bytes);
 if(actual.bytes!==record.bytes||actual.sha256!==record.sha256)
  fail(label+" complete bytes or SHA256 differ from the bound parent/output");
 if(actual.bytes>=100000)fail(label+" violates this parameter artifact's explicit single-file bound");
 return actual;
}
function readParent(repo,record,label){
 const path=resolve(repo,record.path);
 const bytes=readFileSync(path);
 verifyWhole(bytes,record,label);
 return JSON.parse(bytes.toString("utf8"));
}
function materialize(value,record,outdir){
 const bytes=Buffer.from(JSON.stringify(value)+"\n","utf8");
 verifyWhole(bytes,record,record.role+" generated parameter");
 const path=resolve(outdir,record.path);
 mkdirSync(dirname(path),{recursive:true});
 writeFileSync(path,bytes);
 return {...record,generated_path:path};
}
function same(a,b,label){if(JSON.stringify(a)!==JSON.stringify(b))fail(label);}
function inspectCompleteStep(kind,old,current){
 if(old.steps.length!==1||current.steps.length!==1)fail("Expected one complete "+kind+" step");
 const reverse=namespaceOnly(current.steps[0],{old_namespace:SPEC.namespace,namespace:SPEC.old_namespace});
 reverse.script=old.steps[0].script;reverse.scope=old.steps[0].scope;
 same(reverse,old.steps[0],kind+" original whole step is not preserved by the declared three-field mapping");
 if(current.steps[0].args.length!==(kind==="science"?157:7))fail(kind+" argument count");
 if(countSelectors(current.steps[0].summary)!==(kind==="science"?458:445))fail(kind+" complete formal selector count");
 if(countSelectors(current.steps[0].progress_summary)!==(kind==="science"?48:0))fail(kind+" complete live selector count");
 for(const key of Object.keys(old))if(!(key in current))fail("Original top-level metadata field missing: "+key);
 for(const key of SPEC.shared_historical_fields){
  const r=current[key];
  same(r.complete_parent_file,SPEC.parents[kind+"19"],"Shared historical parent differs");
  if(r.json_pointer!=="/"+key||r.truncated_or_replaced_by_summary!==false)
   fail("Shared historical value was not losslessly referenced");
 }
 const prior=old.external_unregistered_peer_obligations;
 same(current.external_unregistered_peer_obligations.slice(0,prior.length),prior,"Original six external obligations changed");
 if(current.external_unregistered_peer_obligations.length!==9)fail("Expected nine distinct external obligations");
 for(const record of SPEC.added_external_peer_records){
  const pair=current.external_unregistered_peer_obligations.find(x=>x[0]===record.run_attempt_key);
  same(pair,[record.run_attempt_key,record.declared_driver_source_sha256],"Actual historical peer source was relabeled");
 }
}
function inspectSourceBinding(binding){
 if(binding.complete_source_role_count!==137||Object.keys(binding.complete_source_role_registry).length!==137)
  fail("The actual current complete scientific registry must have 137 roles");
 if(binding.current_complete_runtime_source_count!==18||Object.keys(binding.current_complete_runtime_sources).length!==18)
  fail("Expected 18 complete current runtime responsibilities");
 if(binding.new_source_count!==20||binding.new_complete_sources.length!==20)
  fail("Expected all 20 complete new source files");
 if(binding.unchanged_source_roles.length!==120)fail("Expected exactly 120 unchanged role pairs");
 const changed=binding.complete_changed_source_parent_records.filter(x=>x.role in binding.complete_source_role_registry).map(x=>x.role);
 same([...changed].sort(),[...SPEC.changed_source_roles].sort(),"The 17 changed actual scientific roles differ");
 for(const role of SPEC.changed_source_roles)if(binding.unchanged_source_roles.includes(role))fail("Changed role also claimed unchanged");
 if(binding.current_runtime_source_registry_unchanged_from_parent!==false)fail("New family must not be claimed identical to old family");
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
  fail("Usage: node reproduce_fixed_fejer_paired_halfwave_bhalf_parameters.mjs --repo <complete-repository> --output-directory <generated-tree>");
 return out;
}
function main(){
 const args=parseArgs(process.argv.slice(2));
 const binding=readParent(args["--repo"],SPEC.parents.binding,"current complete runtime binding");
 const science19=readParent(args["--repo"],SPEC.parents.science19,"whole run19 science parent");
 const pure19=readParent(args["--repo"],SPEC.parents.pure19,"whole run19 pure parent");
 const display19=readParent(args["--repo"],SPEC.parents.display19,"whole run19 display parent");
 inspectSourceBinding(binding);
 const display=buildDisplay(display19,binding,SPEC);
 const science=buildReady("science",science19,binding,EXPECTED.display,SPEC);
 const pure=buildReady("pure",pure19,binding,EXPECTED.display,SPEC);
 inspectCompleteStep("science",science19,science);
 inspectCompleteStep("pure",pure19,pure);
 same(namespaceOnly(display.current_live_mapping,{old_namespace:SPEC.namespace,namespace:SPEC.old_namespace}),
      display19.current_live_mapping,"Full 48 live field mapping changed beyond file names");
 const outputs=[materialize(display,EXPECTED.display,args["--output-directory"]),
  materialize(science,EXPECTED.science,args["--output-directory"]),
  materialize(pure,EXPECTED.pure,args["--output-directory"])];
 process.stdout.write(JSON.stringify({schema:"complete-fixed-fejer-paired-halfwave-bhalf-parameter-text-reproduction-v1",
  complete:true,scope:"Only complete source/parameter text reproduction; no scientific execution, AST, fixture, admission gate, ref or queue change.",
  outputs,numeric_science_argument_changes:0,science_argument_words:157,pure_argument_words:7,
  formal_selectors:{science:458,pure:445},live_selectors:48,
  scientific_source_roles:137,current_runtime_sources:18,new_complete_sources:20,
  unchanged_source_role_pairs:120,changed_source_role_pairs:17,
  original_supported_peer_CLI_pairs:5,external_obligations:9,
  actual_run_id:null,actual_report_sha256:null,actual_final_checkpoint_sha256:null})+"\n");
}
main();
