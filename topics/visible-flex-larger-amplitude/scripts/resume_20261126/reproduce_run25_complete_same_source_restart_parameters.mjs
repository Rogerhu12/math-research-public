#!/usr/bin/env node
/**
 * Complete textual parameter reproduction for the genuine run25 same-source restart.
 * This program reads only pinned UTF-8 source/parameter/returned-small-volume files.
 * It never imports the scientific Python modules, opens runner raw arrays, evaluates
 * a field, runs a solver, changes a Git ref, queues a step, or establishes a new
 * scientific admission gate. It is not required before the original solver runs.
 *
 * node reproduce_run25_complete_same_source_restart_parameters.mjs
 *   --repo /absolute/public/repository --output-directory /fresh/output/directory
 *
 * The complete recipe/actual evidence is the published binding below. All large
 * parent report/checkpoint/readout bytes stay on the original Actions runner.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const EXPECTED = {
  "binding": {
    "path": "topics/visible-flex-larger-amplitude/computations/run25-halfwave-dk-cache-complete-same-source-restart-binding.json",
    "bytes": 19128,
    "sha256": "9c9d9b05a5cf81fc5a8cd351f41c449ed29457983787757a0d028c90e92b0a67",
    "git_blob_sha": "055251aace4e5aacd6afbd46b7a0952044c94f00"
  },
  "science": {
    "path": "topics/visible-flex-larger-amplitude/computations/run25-halfwave-dk-cache-same-source-restart-01-science-complete-ready.json",
    "bytes": 63713,
    "sha256": "4fa109c24e9cfcf6061ca9077a6821604ca59ae42b5a3fe9ab1ec52a74076399",
    "git_blob_sha": "d0e0501b3e6e2ef154701262a2cf4c598fe65835"
  },
  "pure": {
    "path": "topics/visible-flex-larger-amplitude/computations/run25-halfwave-dk-cache-same-source-restart-01-pure-complete-ready.json",
    "bytes": 52567,
    "sha256": "eff57600dc91f2572737c69f4215615b7412f3f0a728203175ba29494a8cb108",
    "git_blob_sha": "e37eb7619a23f21b3115f14b787e069552172095"
  }
};
function sha256(text) { return crypto.createHash('sha256').update(text,'utf8').digest('hex'); }
function gitBlob(text) {
  const data=Buffer.from(text,'utf8');
  return crypto.createHash('sha1').update(Buffer.from('blob '+data.length+'\0','utf8')).update(data).digest('hex');
}
function utf8Bytes(text) { return Buffer.byteLength(text,'utf8'); }
function readPinned(repo, record) {
  if (!record || typeof record.path!=='string' || record.bytes>=100000)
    throw new Error('Require a complete pinned small UTF-8 source/parameter record.');
  const file=path.resolve(repo,record.path);
  if (file!==repo && !file.startsWith(repo+path.sep)) throw new Error('Record leaves the repository.');
  const data=fs.readFileSync(file);
  const text=data.toString('utf8');
  if (!Buffer.from(text,'utf8').equals(data) || data.length!==record.bytes ||
      sha256(text)!==record.sha256 || (record.git_blob_sha && gitBlob(text)!==record.git_blob_sha))
    throw new Error('Whole file identity differs: '+record.path);
  return text;
}
function writePinned(directory, record, text) {
  if (utf8Bytes(text)!==record.bytes || sha256(text)!==record.sha256 ||
      gitBlob(text)!==record.git_blob_sha) throw new Error('Complete reconstructed text differs: '+record.path);
  const output=path.join(directory,path.basename(record.path));
  fs.writeFileSync(output,text,{encoding:'utf8',flag:'wx'});
  return {path:output,bytes:record.bytes,sha256:record.sha256,git_blob_sha:record.git_blob_sha};
}

function clone(value) { return JSON.parse(JSON.stringify(value)); }
function need(condition, message) { if (!condition) throw new Error(message); }
function mapNamespace(value, oldName, newName) {
  if (typeof value === "string") return value.split(oldName).join(newName);
  if (Array.isArray(value)) return value.map(x => mapNamespace(x, oldName, newName));
  if (value && typeof value === "object") return Object.fromEntries(Object.entries(value).map(
    ([key, item]) => [key.split(oldName).join(newName), mapNamespace(item, oldName, newName)]));
  return value;
}
function selectorCount(mapping) {
  return Object.values(mapping || {}).reduce((total, fields) => total + Object.keys(fields).length, 0);
}
function buildRestartPlans(configuration, originalScience, originalPure, bindingRecord) {
  const recipe = configuration.recipe;
  need(originalScience.steps.length === 1 && originalPure.steps.length === 1,
       "Both complete immediate parent files must contain their original single step.");
  const oldScience = originalScience.steps[0], oldPure = originalPure.steps[0];
  need(originalScience.namespace === recipe.old_namespace &&
       originalPure.namespace === recipe.old_namespace, "Wrong whole parameter parent namespace.");
  need(oldScience.args.length === 157 && oldPure.args.length === 7, "Wrong original complete argument lists.");
  need(selectorCount(oldScience.summary) === 458 && selectorCount(oldPure.summary) === 445 &&
       selectorCount(oldScience.progress_summary) === 64, "Wrong original complete selector maps.");
  const science = mapNamespace(clone(oldScience), recipe.old_namespace, recipe.new_namespace);
  const pure = mapNamespace(clone(oldPure), recipe.old_namespace, recipe.new_namespace);
  const kept = [], removed = [], peers = [];
  let independentCount = 0, runCount = 0, sourceCount = 0;
  for (let i = 0; i < science.args.length; ++i) {
    const word = science.args[i];
    if (word === recipe.remove_exact_independent_flag) {
      independentCount++; removed.push(word); continue;
    }
    if (recipe.remove_exact_repeated_peer_flags.includes(word)) {
      need(i + 1 < science.args.length, "Missing value after original pending peer flag.");
      const next = science.args[++i]; removed.push(word, next); peers.push([word, next]);
      if (word === "--pending-parallel-envelope-run") runCount++;
      if (word === "--pending-parallel-envelope-source") sourceCount++;
      continue;
    }
    kept.push(word);
  }
  need(independentCount === 1 && runCount === 5 && sourceCount === 5 && removed.length === 21,
       "The exact original independent flag and five complete CLI peer pairs must be retained as history.");
  need(kept.length === 136, "Unexpected original argument removal.");
  need(!kept.includes("--restart-report") && !kept.includes("--restart-checkpoint"), "Parent is already a restart.");
  science.args = kept.concat(clone(recipe.append_restart_arguments));
  science.parent_bundle = recipe.science_parent_bundle;
  science.scope = "Complete same-source continuation on the existing run25 runner from its genuinely returned complete report and whole final13 checkpoint. The actual parent is still finitely infeasible. Restore the full field and complete material/typed history with the original source guards; start a new unchanged 1/16 metric and 4/64 restoration budget, all 15 line trials, explicit metric/restoration .01, all 32 normal stages and full variables/domain. The exact original five CLI peer pairs survive in the complete parent report and whole parameter history; the existing restart parser forbids repeating independent-mode flags. No mutable progress, partial checkpoint, other runner, new scientific source or feasibility claim is used.";
  pure.scope = "Complete unchanged run25 pure reader on the newly returned same-source restart report, with --verify-final-bundle. Preserve all 445 original formal selectors and their original error/null semantics. The original complete parent report, final checkpoint, all typed/material history and all 137 scientific source roles remain required by the existing runtime. A pure success does not assert finite feasibility or a continuous certificate.";
  need(science.args.length === 140 && pure.args.length === 7, "Wrong complete restart argument count.");
  need(science.script === oldScience.script && pure.script === oldPure.script, "Scientific source script changed.");
  need(selectorCount(science.summary) === 458 && selectorCount(pure.summary) === 445 &&
       selectorCount(science.progress_summary) === 64, "A complete original projection was altered.");
  const reverseScience = mapNamespace(clone(science), recipe.new_namespace, recipe.old_namespace);
  const reversePure = mapNamespace(clone(pure), recipe.new_namespace, recipe.old_namespace);
  for (const key of Object.keys(oldScience)) {
    if (["id", "scope", "parent_bundle", "args"].includes(key)) continue;
    need(JSON.stringify(reverseScience[key]) === JSON.stringify(oldScience[key]),
         "Unexpected science step field change: " + key);
  }
  for (const key of Object.keys(oldPure)) {
    if (["id", "scope"].includes(key)) continue;
    need(JSON.stringify(reversePure[key]) === JSON.stringify(oldPure[key]),
         "Unexpected pure step field change: " + key);
  }
  function ready(kind, step, parentRecord) {
    return {
      schema: "actual-run25-complete-same-source-restart-ready-v1",
      prepared_at_utc: configuration.prepared_at_utc,
      status: "prepared-source-and-parameters-only; continuation execution and new result unknown",
      executed: false,
      scientific_execution_permitted_only_in_public_Actions: true,
      namespace: configuration.namespace,
      existing_run_id: configuration.actual_run.run_id,
      existing_run_attempt: configuration.actual_run.run_attempt,
      existing_request_id: configuration.actual_run.active_request_id,
      same_live_runner_required: true,
      complete_parameter_binding: {complete_file: bindingRecord, json_pointer: ""},
      complete_immediate_parent_parameter_file: {complete_file: parentRecord, json_pointer: ""},
      complete_immediate_parent_step: {complete_file: parentRecord, json_pointer: "/steps/0"},
      all_parent_metadata_and_unknown_peer_responsibilities_preserved: {
        complete_file: configuration.original_complete_files.parameter_binding, json_pointer: ""
      },
      complete_current_source_registry: configuration.source_contract.complete_source_registry,
      complete_current_runtime_records: configuration.source_contract.complete_runtime_records,
      original_five_CLI_peers_and_external_history: {
        complete_file: configuration.original_complete_files.parameter_binding,
        json_pointer: "/complete_peer_responsibilities"
      },
      complete_original64_live_correspondence: {
        complete_file: configuration.original_complete_files.science,
        json_pointer: "/complete_all64_live_correspondence"
      },
      parent_actual_final_and_error_records: {complete_file: bindingRecord, json_pointer: "/actual_run"},
      explicit_complete_mode_recipe: {complete_file: bindingRecord, json_pointer: "/recipe"},
      original_parameter_metadata_shared_by_whole_identity_not_truncated: true,
      all_current_step_fields_and_complete_selector_maps_present: true,
      unchanged_scientific_source_role_count: 137,
      unchanged_current_runtime_file_count: 19,
      scientific_runtime_source_bytes_changed: false,
      numerical_argument_word_changes: [],
      new_AST_fixture_preflight_or_scientific_gate_added: false,
      current_argv_word_count: step.args.length,
      current_formal_selector_count: selectorCount(step.summary),
      current_live_selector_count: selectorCount(step.progress_summary),
      actual_future: clone(configuration.future_actual),
      steps: [step]
    };
  }
  return {
    science: ready("science", science, configuration.original_complete_files.science),
    pure: ready("pure", pure, configuration.original_complete_files.pure),
    removed_original_independent_mode_words: removed,
    removed_original_peer_flag_value_pairs: peers,
    complete_new_scientific_argument_words: clone(science.args)
  };
}

function main() {
  const args=process.argv.slice(2);
  if(args.length!==4 || args[0]!=='--repo' || args[2]!=='--output-directory')
    throw new Error('Use --repo ABSOLUTE_REPOSITORY --output-directory FRESH_DIRECTORY');
  const repo=path.resolve(args[1]), directory=path.resolve(args[3]);
  const bindingText=readPinned(repo,EXPECTED.binding), configuration=JSON.parse(bindingText);
  const originalScience=JSON.parse(readPinned(repo,configuration.original_complete_files.science));
  const originalPure=JSON.parse(readPinned(repo,configuration.original_complete_files.pure));
  const originalMetadata=JSON.parse(readPinned(repo,configuration.original_complete_files.parameter_binding));
  const sourceBinding=JSON.parse(readPinned(repo,configuration.original_complete_files.current_runtime_binding));
  need(Object.keys(sourceBinding.complete_source_role_registry).length===137 &&
       Object.keys(sourceBinding.current_complete_runtime_sources).length===19,
       'Require the actual complete run25 source family.');
  need(JSON.stringify(originalMetadata.original_complete_budgets)===
       JSON.stringify(configuration.recipe.original_complete_budgets),
       'Original complete numerical budget object differs.');
  // Whole source reading only; no Python import, AST, compile, numerical evaluation or subprocess.
  for (const record of Object.values(sourceBinding.current_complete_runtime_sources)) readPinned(repo,record);
  readPinned(repo,configuration.actual_run.whole_science_return_volume);
  readPinned(repo,configuration.actual_run.whole_pure_return_volume);
  const plans=buildRestartPlans(configuration,originalScience,originalPure,EXPECTED.binding);
  fs.mkdirSync(directory,{recursive:true});
  const outputs=[
    writePinned(directory,EXPECTED.binding,bindingText),
    writePinned(directory,EXPECTED.science,JSON.stringify(plans.science)+'\n'),
    writePinned(directory,EXPECTED.pure,JSON.stringify(plans.pure)+'\n')
  ];
  process.stdout.write(JSON.stringify({
    schema:'complete-run25-same-source-restart-text-reproduction-v1',
    scope:'complete source-and-parameter text only; no scientific execution or new admission gate',
    scientific_execution_performed:false,source_import_or_AST_performed:false,
    original_scientific_sources_changed:false,outputs,
    scientific_argument_words:plans.science.current_argv_word_count,
    pure_argument_words:plans.pure.current_argv_word_count,
    complete_formal_counts:[plans.science.current_formal_selector_count,plans.pure.current_formal_selector_count],
    complete_live_count:plans.science.current_live_selector_count,
    removed_original_independent_mode_words:plans.removed_original_independent_mode_words,
    all_original_peers_preserved_in_whole_parent_and_restart_branch_origin:true
  },null,2)+'\n');
}
main();
