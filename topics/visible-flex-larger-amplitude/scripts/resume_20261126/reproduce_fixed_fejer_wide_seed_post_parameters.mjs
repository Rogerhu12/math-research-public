#!/usr/bin/env node
/*
Parameter-only construction. It imports no scientific modules and changes no
runtime source, Git ref, queue, proof, numerical budget, selector or scientific
data. All output files are complete ready objects, never sliced argument lists.
The six original parameter files and the complete wide-seed science ready are
read whole and strictly SHA256/byte-bound. Every original runtime/schema remains.
No scientific fixture, AST/compile or additional admission gate is introduced.
Forward and reverse modes are standalone text operations.
*/
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import cp from "node:child_process";

const CONFIG = {
  "schema": "complete-wide-seed-post-parameter-reproducer-v1",
  "original_source_commit": "eed2151e7e731c5ba9d15ad73b0ce93de94ff119",
  "science_ready": {
    "name": "fixed-fejer-wide-seed-independent-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-wide-seed-independent-complete-ready.json",
    "bytes": 99205,
    "sha256": "692c8392c6bc2a1b0c66d8fba8ccf3d39f277bf11d24f5cad69548127344b2e7",
    "git_blob_sha": "46b842def03978321dcad3404b441f4891ed920d"
  },
  "parent_parameter_files": [
    {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-observed-complete-normal32-full-circle-sixjet-fees-ready.json",
      "bytes": 10975,
      "sha256": "dc5e88a28167b2a06f0821448c07abbae6cc6ff91d3d5bac8547d03398296d2b",
      "git_blob_sha": "46c3ba9503e7b8e42a93bb6cf7ba5b18566de603",
      "name": "fixed-fejer-stage-observed-complete-normal32-full-circle-sixjet-fees-ready.json"
    },
    {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-observed-complete-continuous-gram-curvature-support-ready.json",
      "bytes": 11490,
      "sha256": "049776de848bb0563d1a0ee6438201d2529b470375adb23dd9eb651ebfe751d6",
      "git_blob_sha": "177b4ca2c3566e84cfacbf0bcdfd10f50b0aa909",
      "name": "fixed-fejer-stage-observed-complete-continuous-gram-curvature-support-ready.json"
    },
    {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-observed-closed-phase-grip-r718-ready.json",
      "bytes": 25638,
      "sha256": "829febbc969106ae7cc6e733d897f58e9ee5f6c3dd2076aef148c6b89560724a",
      "git_blob_sha": "0ce6cc3e657859ad75cc6f8cd812aad1f885c99f",
      "name": "fixed-fejer-stage-observed-closed-phase-grip-r718-ready.json"
    },
    {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-observed-complete-R716-closed-flux-centred-moments-ready.json",
      "bytes": 31162,
      "sha256": "bca7946c9b37096ac65c2236f0792830ef85edf1a313f7f4d998773213f9e027",
      "git_blob_sha": "67881a6498db2504dad50935044cee310d17c673",
      "name": "fixed-fejer-stage-observed-complete-R716-closed-flux-centred-moments-ready.json"
    },
    {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-observed-same-field-phase-mesh-final-ready.json",
      "bytes": 60573,
      "sha256": "f47e183bda69adbef11ceb640ef3f698eed8d9f0f207687b08c23117d2e36dad",
      "git_blob_sha": "c83ad722e8e576dcbfaba78b63f06b1598dc846c",
      "name": "fixed-fejer-stage-observed-same-field-phase-mesh-final-ready.json"
    },
    {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-observed-same-field-phase-mesh-packet-ready.json",
      "bytes": 60542,
      "sha256": "97f5d3fda19c68dec8e0d4d879438088ad6c8b6d4fec021bce3a247ac41a904f",
      "git_blob_sha": "d9469eb9c11c3c41e6d4543b4f4cdc410da76422",
      "name": "fixed-fejer-stage-observed-same-field-phase-mesh-packet-ready.json"
    }
  ],
  "expected_outputs": [
    {
      "name": "fixed-fejer-wide-seed-complete-normal32-full-circle-sixjet-fees-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-wide-seed-complete-normal32-full-circle-sixjet-fees-ready.json",
      "bytes": 28010,
      "sha256": "4c2f85efea4abccd2f6cce708d47f0f5907f04e145e4bb5f7d8a4d291474d8af"
    },
    {
      "name": "fixed-fejer-wide-seed-complete-continuous-gram-curvature-support-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-wide-seed-complete-continuous-gram-curvature-support-ready.json",
      "bytes": 26575,
      "sha256": "313f4f64e8d94eda25c325b75026db3a2a90cc79c714e48b40dbedf43a93244e"
    },
    {
      "name": "fixed-fejer-wide-seed-closed-phase-grip-r718-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-wide-seed-closed-phase-grip-r718-ready.json",
      "bytes": 43614,
      "sha256": "737b4cd6c7095a13d6214d9cb25f7bb72ca9ec589042bb846718425825288d5e"
    },
    {
      "name": "fixed-fejer-wide-seed-complete-R716-closed-flux-centred-moments-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-wide-seed-complete-R716-closed-flux-centred-moments-ready.json",
      "bytes": 57143,
      "sha256": "7e8aa787b9372d1d65a34b16ef5e282c93ac2423fc2208fbf02ebf0da1d70977"
    },
    {
      "name": "fixed-fejer-wide-seed-same-field-phase-mesh-final-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-wide-seed-same-field-phase-mesh-final-ready.json",
      "bytes": 89870,
      "sha256": "a45c277a71543b4183d8ce2008fc6de137de50535683c59c502bb246d16d2f67"
    },
    {
      "name": "fixed-fejer-wide-seed-same-field-phase-mesh-packet-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-wide-seed-same-field-phase-mesh-packet-ready.json",
      "bytes": 89805,
      "sha256": "117d7eb861a2ef3c84e2a20775517a56396d5dcfcfa04e12323e1a2057d028ad"
    }
  ],
  "reproducer_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_wide_seed_post_parameters.mjs"
};

function deriveReady(parent, parentRecord, science, scienceRecord, options = {}) {
  const clone = x => JSON.parse(JSON.stringify(x));
  const out = clone(parent);
  const changes = [];
  const oldOrder = Object.keys(parent);
  const oldScopes = parent.steps.map(s => s.scope);
  const oldStem = "fixed-fejer-stage-point-observed-independent";
  const newStem = "fixed-fejer-wide-seed-first";
  const oldPost = "fixed-fejer-stage-observed-";
  const newPost = "fixed-fejer-wide-seed-";
  const translate = s => typeof s === "string"
    ? s.split(oldStem).join(newStem).split(oldPost).join(newPost) : s;
  function set(keys, value) {
    let target = out;
    for (const key of keys.slice(0, -1)) target = target[key];
    const key = keys[keys.length - 1];
    const exists = Object.prototype.hasOwnProperty.call(target, key);
    if (exists && JSON.stringify(target[key]) === JSON.stringify(value)) return;
    changes.push({path: keys, original_exists: exists,
                  original_value: exists ? clone(target[key]) : null});
    target[key] = clone(value);
  }
  function setTop(key, value) { if (Object.prototype.hasOwnProperty.call(out, key)) set([key], value); }
  function keyed(value) {
    return Object.fromEntries(Object.entries(value).map(([key, val]) => [translate(key), clone(val)]));
  }
  function scopeText(value) {
    return value.replaceAll("complete run16 command", "complete actual wide-seed command")
      .replaceAll("Complete run16 observed", "Complete same-source wide-seed observed")
      .replaceAll("Actual complete run16 source and input identities", "Actual complete wide-seed source and input identities")
      .replaceAll("source family is run16 stage-point-observed", "source family remains stage-point-observed for this wide-seed field")
      + " Parameter-only wide-seed use: the actual command must contain boundary-total-length 1/4 and profile-delta 1/32, with every other original numerical word retained. The immutable fixed target and reference are unchanged mathematical objects; this new seed, mean/root branch, complete field model and physical field are not inherited from run16. All new report/point/packet/fee identities remain unfilled until genuine complete inputs are read.";
  }
  out.steps = out.steps.map(step => {
    const result = clone(step);
    result.id = translate(step.id);
    result.scope = scopeText(step.scope);
    result.args = step.args.map(translate);
    result.outputs = step.outputs.map(translate);
    result.summary = keyed(step.summary);
    if (step.progress_summary) result.progress_summary = keyed(step.progress_summary);
    if (step.cleanup_generated_patterns) result.cleanup_generated_patterns = step.cleanup_generated_patterns.map(translate);
    return result;
  });
  for (const key of ["source_report_expected_path", "source_normal_report_expected_path",
                     "source_geometry_expected_path", "input_report", "complete_closed_phase_main_report"]) {
    if (typeof out[key] === "string") setTop(key, translate(out[key]));
  }
  for (const key of ["intended_actual_run_id", "intended_actual_run_attempt", "actual_original_scientific_run",
                     "exact_fixed_target_identity_sha256", "fixed_target_identity_sha256",
                     "fixed_target_definition_identity_sha256", "fixed_material_chart_identity_sha256",
                     "fixed_chart_core_sha256", "reference_model_identity_sha256",
                     "actual_current_reference_model_identity_sha256",
                     "actual_fixed_target_definition_identity_sha256",
                     "actual_reference_model_identity_sha256",
                     "actual_returned_input_identity", "actual_input_evidence",
                     "actual_completed_reference_input_evidence"]) setTop(key, null);
  for (const key of ["scientific_solver_parameters_or_sources_changed",
                     "original_scientific_sources_or_parameters_changed", "original_solver_parameters_changed"]) {
    setTop(key, true);
  }
  setTop("scope", scopeText(parent.scope || ""));
  if (typeof parent.actual_source_specification === "string") setTop("actual_source_specification", scopeText(parent.actual_source_specification));
  if (Array.isArray(out.new_consumer_arguments)) setTop("new_consumer_arguments", out.new_consumer_arguments.map(translate));
  if (out.optional_complete_closed_phase_evidence) {
    set(["optional_complete_closed_phase_evidence", "report_path"],
        translate(out.optional_complete_closed_phase_evidence.report_path));
    set(["optional_complete_closed_phase_evidence", "argument_if_attaching_the_actual_complete_report"],
        out.optional_complete_closed_phase_evidence.argument_if_attaching_the_actual_complete_report.map(translate));
  }
  if (out.progress_publication_contract && out.progress_publication_contract.complete_original_50_selector_mapping_preserved) {
    set(["progress_publication_contract", "complete_original_50_selector_mapping_preserved"],
        keyed(out.progress_publication_contract.complete_original_50_selector_mapping_preserved));
  }
  if (out.complete_original_scientific_parameter_source) {
    const key = "complete_original_scientific_parameter_source";
    for (const name of ["name", "path", "bytes", "sha256", "git_blob_sha"]) {
      set([key, name], scienceRecord[name]);
    }
    set([key, "original_complete_argv"], science.steps[0].args);
    set([key, "actual_command_required_path"], "{work}/fixed-fejer-wide-seed-first-command.json");
  }
  if (out.source_only_validation) {
    setTop("source_only_validation", {
      complete_original_runtime_source_and_all_original_parameters_retained: true,
      parameter_text_forward_and_inverse_preserve_whole_parent_JSON: true,
      new_runtime_source_or_guard_changes: false,
      Python_AST_or_compile_executed: false,
      scientific_module_import_or_math_evaluation: false,
      parameter_text_and_source_interface_reading_only: true,
      no_new_admission_gate: true
    });
  }
  const correspondence = parent.steps.map((step, index) => ({
    step: index + 1,
    unchanged_script: step.script,
    original_full_argv: clone(step.args),
    current_full_argv: clone(out.steps[index].args),
    original_output_paths: clone(step.outputs),
    current_output_paths: clone(out.steps[index].outputs),
    summary_field_counts: Object.values(step.summary).map(value => Object.keys(value).length),
    progress_field_counts: Object.values(step.progress_summary || {}).map(value => Object.keys(value).length),
    all_selector_names_and_JSON_paths_retained: true,
    all_numeric_parameters_and_order_retained: true,
    only_input_and_output_paths_changed_in_postprocess_argv: true
  }));
  setTop("complete_parameter_correspondence", correspondence);
  out.wide_seed_parameter_variant = {
    schema: "same-source-wide-seed-complete-postprocessing-parameters-v1",
    intended_plan_number: 17,
    admitted: false,
    executed: false,
    new_runtime_source_count: 0,
    complete_scientific_source_role_count: 120,
    science_ready: clone(scienceRecord),
    unchanged_driver: clone(science.complete_new_runtime_sources.driver),
    unchanged_launcher: clone(science.complete_new_runtime_sources.launcher),
    unchanged_reader: clone(science.complete_new_runtime_sources.reader),
    scientific_command_expected_path: "{work}/fixed-fejer-wide-seed-first-command.json",
    scientific_report_expected_path: "{work}/fixed-fejer-wide-seed-first/report.json",
    science_argv_word_count: science.steps[0].args.length,
    pure_argv_word_count: science.steps[1].args.length,
    science_and_pure_selector_counts: science.steps.map(s => Object.values(s.summary).map(v => Object.keys(v).length)),
    exact_seed_parameter_changes: clone(science.parameter_contract.exact_seed_parameter_changes),
    all_other_original_science_numeric_words_and_order_retained: true,
    all_original_postprocess_numeric_words_selectors_and_sources_retained: true,
    seed_boundary_total_length_over_S: "1/4",
    supported_total_length_over_S: "7/8",
    central_total_length_over_S: "5/8",
    central_profile: "R711 twelve-piece smooth triangle",
    profile_delta: "1/32",
    new_mean_or_root_existence_or_better_cost_or_geometry_assumed: false,
    R709_full_angle_conditions_and_all_actual_mean_profile_errors_must_be_repaid: true,
    all_original_32_normal_stages_and_full_physical_sixjets_retained: true,
    previous_seed_batches_root_packets_fields_or_certificates_inherited: false,
    same_fixed_g_is_not_same_seed_or_same_complete_field_model: true,
    current_M: 160, current_J: 923, current_full_N: 2048,
    reference_M: 160, reference_J: 923, reference_full_N: 2048,
    actual_new_run_id: null,
    actual_new_run_attempt: null,
    actual_new_input_binding_record: null,
    actual_new_six_input_file_records: null,
    actual_new_scientific_report_record: null,
    actual_new_command_record: null,
    actual_new_full_point_sha256: null,
    actual_new_normal_model_identity_sha256: null,
    actual_new_seed_identity_sha256: null,
    actual_new_snapshot_identity_sha256: null,
    actual_new_normal_fee_report_record: null,
    actual_new_geometry_report_record: null,
    actual_new_closed_report_record: null,
    actual_new_moment_report_record: null,
    actual_new_mesh_report_record: null,
    actual_new_result_or_certificate: null,
    fixed_definition_expectations: {
      attribution: "Predeclared mathematical object identities from the unchanged recipe/reference source; these are not asserted new-run file SHA256 values or returned field identities.",
      mathematical_recipe_identity_sha256: "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      fixed_target_definition_identity_sha256: "50df37b6b832dcdd53d05c54138e62e43df6b14df68d946a7b8a7b8227f58319",
      reference_model_identity_sha256: "ea64e2fe5e272648195128d53521705cc266d82f7d2636bd7201b90fcf172fac",
      fixed_chart_identity_sha256: "af8ab672f847163fe02999df70a031cd5e4a495ed89c788ad0dffc8786651103",
      fixed_scalar_profile_identity_sha256: "d492e4ad97245a8474f1a73a8787aac2fc5691b1f928d0b8ea72224cabd55160",
      fixed_recipe_source_sha256: "89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60",
      complete_reference_source_sha256: "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
      complete_actual_six_input_validator_sha256: "3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f",
      current_scalar_leaf_recipe: 2218,
      actual_file_bytes_and_all_definition_objects_must_be_read_again: true,
      actual_scalar_accuracy_flag_not_assumed_true: true,
      seed_configuration_is_not_part_of_fixed_recipe_or_fixed_reference_definition: true
    },
    historical_peer_scope: {
      original_five_supported_pending_CLI_pairs_unchanged: true,
      complete_original_science_CLI_is_in_science_ready: true,
      external_unregistered_peer_run_source_pairs: clone(science.parameter_contract.external_unregistered_peer_run_source_pairs),
      newer_peer_typed_memory_consumed_or_declared_empty: false,
      source_family_registry_relaxed: false,
      unknown_old_branches_removed: false
    },
    report_and_snapshot_selection_boundary: "Read a genuine complete report and the selected actual immutable snapshot or full thirteen-member final according to the unchanged consumer. Prepared input, progress, a ready, a failed incomplete snapshot or another field is never substituted. Mesh packet mode does not imply accepted/final; mesh final mode never resets to reference.",
    runtime_sources_or_scientific_queue_modified_here: false
  };
  out.wide_seed_parameter_derivation = {
    complete_direct_parameter_parent: clone(parentRecord),
    complete_original_parent_metadata_is_preserved_without_relabelling: true,
    original_top_level_key_order: oldOrder,
    original_step_scopes: oldScopes,
    changed_original_values: changes,
    original_run16_evidence_scope: "All original run16 records retained in changed_original_values or unchanged source/provenance fields are historical parameter provenance. Their old actual paths/SHA256/run IDs are not new-run evidence or inherited field certificates.",
    complete_current_step_correspondence: correspondence,
    reproducer_path: options.reproducer_path,
    forward_and_inverse_operations: "Whole source-pinned JSON, exact namespace substitutions only in operational paths/step IDs, explicit provenance changes, and complete inverse restoration using the original key order and saved values.",
    local_AST_compile_science_or_fixture: false,
    no_new_execution_admission_gate: true
  };
  return out;
}

function restoreParent(derived) {
  const clone = x => JSON.parse(JSON.stringify(x));
  const d = clone(derived);
  const info = d.wide_seed_parameter_derivation;
  if (!info || !Array.isArray(info.original_top_level_key_order)) throw new Error("Missing complete inverse provenance");
  const back = s => typeof s === "string"
    ? s.split("fixed-fejer-wide-seed-first").join("fixed-fejer-stage-point-observed-independent")
       .split("fixed-fejer-wide-seed-").join("fixed-fejer-stage-observed-") : s;
  const keyed = x => Object.fromEntries(Object.entries(x).map(([k,v])=>[back(k), clone(v)]));
  d.steps = d.steps.map((step,index) => {
    const s = clone(step);
    s.id = back(step.id);
    s.scope = info.original_step_scopes[index];
    s.args = step.args.map(back);
    s.outputs = step.outputs.map(back);
    s.summary = keyed(step.summary);
    if (step.progress_summary) s.progress_summary = keyed(step.progress_summary);
    if (step.cleanup_generated_patterns) s.cleanup_generated_patterns = step.cleanup_generated_patterns.map(back);
    return s;
  });
  for (const entry of [...info.changed_original_values].reverse()) {
    let target = d;
    for (const key of entry.path.slice(0,-1)) target = target[key];
    const key = entry.path[entry.path.length-1];
    if (entry.original_exists) target[key] = clone(entry.original_value);
    else delete target[key];
  }
  return Object.fromEntries(info.original_top_level_key_order.map(key=>[key,d[key]]));
}

function encoded(value) { return JSON.stringify(value, null, 2) + "\n"; }
function digest(text) {
  return {bytes: Buffer.byteLength(text,"utf8"), sha256: crypto.createHash("sha256").update(text,"utf8").digest("hex")};
}
function must(condition, message) { if (!condition) throw new Error(message); }
function matches(text, record) {
  const value = digest(text);
  return value.bytes === record.bytes && value.sha256 === record.sha256;
}
function readPinned(repo, record) {
  const file = path.resolve(repo, record.path);
  let text = null;
  if (fs.existsSync(file)) {
    const bytes = fs.readFileSync(file);
    must(bytes.length < 100000, "Refuse oversized parameter source: " + record.path);
    const candidate = bytes.toString("utf8");
    if (matches(candidate, record)) text = candidate;
  }
  if (text === null) {
    // Fixed complete Git blob recovery, not a different version or a network run.
    const got = cp.spawnSync("git", ["show", record.git_blob_sha], {
      cwd: repo, encoding: "utf8", maxBuffer: 100000
    });
    must(got.status === 0 && typeof got.stdout === "string",
         "Complete pinned parameter unavailable: " + record.path);
    text = got.stdout;
  }
  must(matches(text, record), "Whole source mismatch: " + record.path);
  must(encoded(JSON.parse(text)) === text, "Parent canonical formatting changed: " + record.path);
  return text;
}
function originalValuesUnchanged(parent, derived) {
  must(parent.steps.length === derived.steps.length, "Step count changed");
  for (let i=0; i<parent.steps.length; ++i) {
    const a=parent.steps[i], b=derived.steps[i];
    must(a.script === b.script && a.parent_bundle === b.parent_bundle, "Runtime source or parent bundle changed");
    must(a.args.length === b.args.length, "Argument count changed");
    for (let j=0; j<a.args.length; ++j) {
      if (a.args[j] !== b.args[j]) {
        must(typeof a.args[j] === "string" && a.args[j].startsWith("{work}/"),
             "Unexpected numerical/option change at argument " + j);
      }
    }
    must(JSON.stringify(Object.values(a.summary)) === JSON.stringify(Object.values(b.summary)),
         "Formal selector mapping changed");
    must(JSON.stringify(Object.values(a.progress_summary || {})) === JSON.stringify(Object.values(b.progress_summary || {})),
         "Live selector mapping changed");
  }
  for (const key of ["complete_source_sha256","source_sha256","complete_runtime_source_records"]) {
    must(JSON.stringify(parent[key]) === JSON.stringify(derived[key]), "Runtime source table changed");
  }
  must(encoded(restoreParent(derived)) === encoded(parent), "Incomplete inverse provenance");
}
function parse(argv) {
  const result = {repo:".", output_dir:null, reverse:null};
  const names = {"--repo":"repo","--output-dir":"output_dir","--reverse":"reverse"};
  for (let i=0; i<argv.length; ++i) {
    const key = names[argv[i]];
    must(key && i+1<argv.length, "Usage: --repo REPO --output-dir DIR [--reverse READY_DIR]");
    result[key] = argv[++i];
  }
  must(result.output_dir, "--output-dir is required");
  return result;
}
function writeOne(directory, name, text, expected) {
  must(matches(text, expected), "Constructed whole file differs: " + name);
  must(digest(text).bytes < 100000, "Each complete deliverable must be below100000 bytes");
  fs.mkdirSync(directory, {recursive:true});
  const file = path.join(directory,name);
  if (fs.existsSync(file)) {
    must(fs.readFileSync(file,"utf8") === text, "Refuse to replace different bytes: " + file);
  } else fs.writeFileSync(file,text,"utf8");
  return {path:file,...digest(text)};
}
function main() {
  const args=parse(process.argv.slice(2)), results=[];
  if (args.reverse !== null) {
    for (let i=0; i<CONFIG.expected_outputs.length; ++i) {
      const expected=CONFIG.expected_outputs[i], parent=CONFIG.parent_parameter_files[i];
      const text=fs.readFileSync(path.join(args.reverse,expected.name),"utf8");
      must(matches(text,expected), "Reverse input does not match complete derived ready");
      const restored=encoded(restoreParent(JSON.parse(text)));
      results.push(writeOne(args.output_dir,parent.name,restored,parent));
    }
  } else {
    const science=JSON.parse(readPinned(args.repo,CONFIG.science_ready));
    must(science.steps[0].args.length===157 && science.steps[1].args.length===7,
         "Complete science/pure word count changed");
    must(science.steps[0].args[science.steps[0].args.indexOf("--seed-boundary-total-length")+1]==="1/4",
         "Wide seed boundary does not match");
    must(science.steps[0].args[science.steps[0].args.indexOf("--seed-profile-delta")+1]==="1/32",
         "Wide seed profile does not match");
    for (let i=0; i<CONFIG.parent_parameter_files.length; ++i) {
      const record=CONFIG.parent_parameter_files[i], expected=CONFIG.expected_outputs[i];
      const parentText=readPinned(args.repo,record), parent=JSON.parse(parentText);
      const derived=deriveReady(parent,record,science,CONFIG.science_ready,{reproducer_path:CONFIG.reproducer_path});
      originalValuesUnchanged(parent,derived);
      must(encoded(restoreParent(derived))===parentText, "Whole-byte inverse changed original ready");
      results.push(writeOne(args.output_dir,expected.name,encoded(derived),expected));
    }
  }
  process.stdout.write(encoded({
    scope:"complete parameter text only",
    scientific_calls:0, runtime_sources_changed:0, refs_or_queue_written:false,
    reverse:args.reverse!==null, files:results
  }));
}
main();
