#!/usr/bin/env node
/**
 * Complete text-only reproduction of prepared run31 R728 reversed-demanded parameters.
 * The complete original run30 files remain unchanged and are read by whole identity.
 * All 157/7 argument words, 458/445 formal selectors, 64 live selectors, original
 * five pending CLI pairs and seventeen external peer-source pairs are retained.
 * Only actual output namespace/script/scope and the separately pinned current
 * source/physical mechanism change. Run31 source publication and actuals are null
 * at preparation; a later true publication belongs in a separate dated record.
 * No scientific module import, Python, AST, fixture, benchmark, field/root call,
 * controller/queue/ref change, or additional scientific execution gate.
 * Usage: node reproduce_fixed_fejer_R728_demanded_run31_parameters.mjs
 *        --repo ABSOLUTE_REPOSITORY --output-directory FRESH_DIRECTORY
 * Restore any un-published parent document by its exact complete Git blob first;
 * those documents are whole source/parameter artifacts, never encoded raw data.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
const EXPECTED={
  "binding": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-demanded-bhalf-complete-parameter-binding.json",
    "bytes": 35050,
    "sha256": "8790f2cc535346118f7733ac3fb8577b599f2c9c2374efffd06dae7d1ccf9154",
    "git_blob_sha": "fc704611d7a95003ff9dc31157801bbd88be6ea6"
  },
  "science": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-demanded-bhalf-science-complete-ready.json",
    "bytes": 65507,
    "sha256": "efb605cc5451bea73cd25c660201f346c0e7de644f4a4cfa29102db2a69c3444",
    "git_blob_sha": "21f5eb7d1b53244b4695809955a0fae8e5fa59f0"
  },
  "pure": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-demanded-bhalf-pure-complete-ready.json",
    "bytes": 53783,
    "sha256": "ef6e6bf414d4d1665bc6b7c1706a3d8668fce398cfc33d6b2d11201294376fb8",
    "git_blob_sha": "1c854be4fde79088727f8e8590bc7cd8a856bb67"
  }
};
function sha256(text){ return crypto.createHash('sha256').update(text,'utf8').digest('hex'); }
function gitBlob(text){
 const body=Buffer.from(text,'utf8');
 return crypto.createHash('sha1').update(Buffer.from('blob '+body.length+'\0','utf8')).update(body).digest('hex');
}
function readComplete(repo,record){
 if(!record || typeof record.path!=='string' || record.bytes>=100000)
  throw new Error('A complete pinned small source/parameter file is required.');
 const file=path.resolve(repo,record.path);
 if(!file.startsWith(repo+path.sep))throw new Error('Path leaves repository.');
 const bytes=fs.readFileSync(file),text=bytes.toString('utf8');
 if(!Buffer.from(text,'utf8').equals(bytes)||bytes.length!==record.bytes||
    sha256(text)!==record.sha256||(record.git_blob_sha&&gitBlob(text)!==record.git_blob_sha))
  throw new Error('Whole text identity changed: '+record.path);
 return text;
}
function writeComplete(dir,record,text){
 if(Buffer.byteLength(text,'utf8')!==record.bytes||sha256(text)!==record.sha256||gitBlob(text)!==record.git_blob_sha)
  throw new Error('Complete reconstructed object differs: '+record.path);
 const target=path.join(dir,path.basename(record.path));
 fs.writeFileSync(target,text,{encoding:'utf8',flag:'wx'});
 return {...record,local_output:target};
}
function copy(value) { return JSON.parse(JSON.stringify(value)); }
function requireText(condition,message) { if(!condition) throw new Error(message); }
function remapNamespace(value,oldName,newName) {
  if(typeof value==='string') return value.split(oldName).join(newName);
  if(Array.isArray(value)) return value.map(x=>remapNamespace(x,oldName,newName));
  if(value && typeof value==='object') return Object.fromEntries(Object.entries(value).map(
    ([key,item])=>[key.split(oldName).join(newName),remapNamespace(item,oldName,newName)]));
  return value;
}
function countSelectors(value) {
  return Object.values(value||{}).reduce((n,x)=>n+Object.keys(x).length,0);
}
function buildRun31Parameters(recipe,parentScience,parentPure,parentBinding,currentSourceBinding,bindingRecord) {
  requireText(parentScience.steps.length===1 && parentPure.steps.length===1,'Read both complete original run30 steps.');
  requireText(parentScience.namespace===recipe.parent_namespace &&
              parentPure.namespace===recipe.parent_namespace,'Wrong original parameter namespace.');
  requireText(Object.keys(currentSourceBinding.complete_source_role_registry).length===137 &&
              Object.keys(currentSourceBinding.current_complete_runtime_sources).length===23,'Wrong complete current source registry.');
  requireText(currentSourceBinding.changed_current_scientific_role_count===18 &&
              currentSourceBinding.unchanged_current_scientific_role_count===119,'Wrong declared current source relationship.');
  const oldScience=parentScience.steps[0],oldPure=parentPure.steps[0];
  requireText(oldScience.args.length===157 && oldPure.args.length===7,'Preserve the full original argv.');
  requireText(countSelectors(oldScience.summary)===458 && countSelectors(oldPure.summary)===445 &&
              countSelectors(oldScience.progress_summary)===64,'Preserve all formal and live selectors.');
  requireText(JSON.stringify(parentBinding.complete_original_budgets)===JSON.stringify(recipe.complete_original_budgets),
              'The full original numerical budget object differs.');
  requireText(JSON.stringify(parentBinding.external_actual_evidence.complete_current_external_pairs)===
              JSON.stringify(recipe.external_actual_evidence.complete_current_external_pairs),'Do not relabel the complete original external peer sources.');
  const science=remapNamespace(copy(oldScience),recipe.parent_namespace,recipe.namespace);
  const pure=remapNamespace(copy(oldPure),recipe.parent_namespace,recipe.namespace);
  science.script=recipe.declared_runtime_scripts.science;
  pure.script=recipe.declared_runtime_scripts.pure;
  science.scope='Complete independent R728 reversed-polarity spherical-boundary paired-halfwave field with b/S=1/2, profile delta=1/32 and the complete demanded detached rotation/frame2 implementation. The source-fixed central signs are (-,+); the R726 complete mean equation and both angular jets remain, while the physical field and current source/model identity are new. Preserve every original variable, 32 stages, all 157 argument words, budgets, call order, acceptance rules and original pending CLI/history responsibilities. Actual finite-data eligibility and all original analytic/AD fallbacks remain. No inherited physical field, root packet, old certificate, actual feasibility, current input identity or measured speedup is asserted.';
  pure.scope='Complete current R728 reversed-demanded pure reader for the actual newly returned own-source report, with all original 445 formal selectors, source/model checks, own-point snapshots and --verify-final-bundle. Full diagnostics remain in the readout. The current independent seed is source-fixed (-,+), never a relabelled R726 physical field. A complete finite return or pure success does not certify continuous roots, metric, reach, phase bounds or old/new physical field equality.';
  for(const [kind,oldStep,newStep] of [['science',oldScience,science],['pure',oldPure,pure]]) {
    const back=remapNamespace(copy(newStep),recipe.namespace,recipe.parent_namespace);
    for(const key of Object.keys(oldStep)) {
      if(['script','scope'].includes(key)) continue;
      requireText(JSON.stringify(back[key])===JSON.stringify(oldStep[key]),'Unexpected complete '+kind+' step change: '+key);
    }
    requireText(Object.keys(oldStep).length===Object.keys(newStep).length,'Step field was dropped or added.');
  }
  const base={
    schema:'complete-R728-reversed-demanded-independent-run31-ready-v1',
    prepared_utc:recipe.prepared_utc,
    status:'prepared-complete-source-and-parameters; no run31 scientific execution or result claimed',
    executed:false,scientific_execution_permitted_only_in_public_Actions:true,
    intended_independent_runner_label:31,namespace:recipe.namespace,
    current_source_publication_at_preparation:recipe.current_source_publication,
    complete_parameter_binding:{complete_file:bindingRecord,json_pointer:'',whole_file_required:true},
    all_complete_frozen_parent_metadata:{complete_file:recipe.parents.binding30,json_pointer:'',whole_file_required:true},
    full_original_peer_history:copy(recipe.complete_frozen_metadata.all_original_peer_history),
    complete_external_actual_updates:{complete_file:bindingRecord,json_pointer:'/external_actual_evidence',whole_file_required:true},
    current_complete_source_registry:recipe.complete_source_scope.registry,
    current_complete_runtime_records:recipe.complete_source_scope.runtime,
    complete_current_source_delivery:recipe.parents.source31,
    full_current_source_and_fallback_contract:{complete_file:bindingRecord,json_pointer:'/complete_source_scope',whole_file_required:true},
    complete_current_source_roles:137,complete_current_runtime_files:23,
    actual_current_role_replacements:18,actual_unchanged_role_pairs:119,
    current_role_comparison_parent:'complete protected run30 current registry; never an executed run30 field',
    full_current_parameter_recipe:{complete_file:bindingRecord,json_pointer:'/exact_step_recipe',whole_file_required:true},
    full_original_scientific_budget:{complete_file:bindingRecord,json_pointer:'/complete_original_budgets',whole_file_required:true},
    complete_current_physical_seed_recipe:{complete_file:bindingRecord,json_pointer:'/complete_current_seed_mechanism',whole_file_required:true},
    whole_metadata_references_preserve_all_original_fields:true,
    complete_R726_mean_equation_and_two_angular_jets_unchanged:true,
    physical_central_polarity_changes_from_positive_first_to_source_fixed_negative_first:true,
    previous_physical_field_or_actual_model_root_word_identity_inherited:false,
    existing_R726_zero_angle_working_definition_and_unpaid_accurate_error_scope_preserved:true,
    old_R709_or_R722_boundary_proof_inherited:false,
    R726_R727_or_R728_accurate_existence_or_geometric_certificate_claimed:false,
    original_call_order_or_acceptance_rules_changed:false,
    adaptive_restoration_or_geometry_first_mixed:false,
    numerical_argument_word_changes:[],
    all_original64_live_fields_preserved:true,
    new_AST_fixture_benchmark_preflight_or_scientific_gate:false,
    actual_future:copy(recipe.actual_future)
  };
  function ready(kind,step,parentRecord) {
    return {...copy(base),kind,
      complete_immediate_parent_parameter_file:{complete_file:parentRecord,json_pointer:'',whole_file_required:true},
      original_complete_parent_step:{complete_file:parentRecord,json_pointer:'/steps/0',whole_file_required:true},
      current_argv_word_count:step.args.length,
      current_formal_selector_count:countSelectors(step.summary),
      current_live_selector_count:countSelectors(step.progress_summary),
      steps:[step]};
  }
  return {science:ready('science',science,recipe.parents.science30),pure:ready('pure',pure,recipe.parents.pure30),
    display:remapNamespace(copy(oldScience.progress_summary),recipe.parent_namespace,recipe.namespace)};
}
function main(){
 const args=process.argv.slice(2);
 if(args.length!==4||args[0]!=='--repo'||args[2]!=='--output-directory')
  throw new Error('Use --repo ABSOLUTE_REPOSITORY --output-directory FRESH_DIRECTORY');
 const repo=path.resolve(args[1]),outdir=path.resolve(args[3]);
 const text=readComplete(repo,EXPECTED.binding),recipe=JSON.parse(text);
 const parentScience=JSON.parse(readComplete(repo,recipe.parents.science30));
 const parentPure=JSON.parse(readComplete(repo,recipe.parents.pure30));
 const parentBinding=JSON.parse(readComplete(repo,recipe.parents.binding30));
 const source=JSON.parse(readComplete(repo,recipe.parents.binding31));
 readComplete(repo,recipe.parents.params30);
 readComplete(repo,recipe.parents.source31);
 readComplete(repo,recipe.parents.source_proof31);
 requireText(recipe.current_source_publication===null,'The frozen prepared binding cannot invent its later publication.');
 // Complete source text identities only. No source body is imported or evaluated.
 for(const record of Object.values(source.current_complete_runtime_sources))readComplete(repo,record);
 for(const observation of recipe.external_actual_evidence.appended_complete_observations)
  readComplete(repo,observation.complete_evidence);
 const made=buildRun31Parameters(recipe,parentScience,parentPure,parentBinding,source,EXPECTED.binding);
 requireText(JSON.stringify(made.display)===JSON.stringify(recipe.complete_display_correspondence.current_live_mapping),
             'The complete original 64 live selectors must agree.');
 fs.mkdirSync(outdir,{recursive:true});
 const outputs=[
  writeComplete(outdir,EXPECTED.binding,text),
  writeComplete(outdir,EXPECTED.science,JSON.stringify(made.science)+'\n'),
  writeComplete(outdir,EXPECTED.pure,JSON.stringify(made.pure)+'\n')
 ];
 process.stdout.write(JSON.stringify({
  schema:'complete-run31-R728-reversed-demanded-text-reproduction-v1',
  scope:'whole source and parameter text only; not a scientific admission or execution step',
  outputs,
  original_numerical_argument_words_changed:false,
  complete_argument_counts:[made.science.current_argv_word_count,made.pure.current_argv_word_count],
  complete_formal_counts:[made.science.current_formal_selector_count,made.pure.current_formal_selector_count],
  complete_live_count:made.science.current_live_selector_count,
  complete_current_source_role_count:137,complete_current_runtime_file_count:23,
  current_role_changes_relative_to_complete_run30:18,unchanged_current_role_pairs:119,
  source_fixed_global_central_polarity:-1,
  inherited_actual_model_point_roots_or_geometric_values:false,
  prior_whole_metadata_preserved:true,
  original_pending_CLI_pairs_preserved:true,
  complete_external_peer_pairs:recipe.external_actual_evidence.current_pair_count,
  raw_scientific_data_read:false,
  scientific_import_AST_fixture_benchmark_or_execution_performed:false,
  refs_or_queues_changed:false
 },null,2)+'\n');
}
main();
