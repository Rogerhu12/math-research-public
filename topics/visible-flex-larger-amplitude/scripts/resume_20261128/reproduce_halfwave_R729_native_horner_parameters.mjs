#!/usr/bin/env node
import {createHash} from 'node:crypto';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {resolve,dirname} from 'node:path';
import {execFileSync} from 'node:child_process';

const spec = {
  "oldNamespace": "fixed-fejer-halfwave-R729-bhalf-first",
  "newNamespace": "fixed-fejer-halfwave-R729-native-horner-first",
  "oldReady": {
    "science": {
      "role": "science",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-R729-bhalf-science-complete-ready.json",
      "bytes": 80928,
      "sha256": "d35579f13e07cf004a333905af411c0a47f2147f42c574b9b0c65af7b02b1798",
      "git_blob_sha": "8631722f6367d98f4515adce383f49226f69c3cd"
    },
    "pure": {
      "role": "pure",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-R729-bhalf-pure-complete-ready.json",
      "bytes": 70074,
      "sha256": "19e226f138e2076dc2834f7b3a2449eef633961c4a80159e5933c7f0fa0e290a",
      "git_blob_sha": "86116e5b0605b3fc5d24cf8b998695bf65939401"
    }
  },
  "source": {
    "role": "complete science, pure and normal-build source roles",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-R729-native-horner-complete-source-delivery.json",
    "name": "fixed-fejer-halfwave-R729-native-horner-complete-source-delivery.json",
    "bytes": 53774,
    "sha256": "5744c3e748ac9877a42f9f8b173df1fa3f0a8123391768ebd795968e6c63bb9f",
    "git_blob_sha": "d44d4bfda00b5aaeb61b5ebbe0cbfae139092434"
  },
  "wrapper": {
    "role": "complete scientific and pure entry",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/build_and_launch_halfwave_R729_native_horner_actions.py",
    "name": "build_and_launch_halfwave_R729_native_horner_actions.py",
    "bytes": 7679,
    "sha256": "e04d5b367e817ddee6f67cdd134f8612a31e73648315cf55c0e8e0649cc78457",
    "git_blob_sha": "ab73ebf7dec07cd7bb2d4a7c4d87c5d4dbf39d5c"
  },
  "nativeSelectors": {
    "native_state": "strict_native_horner.state",
    "native_c_source_sha256": "strict_native_horner.c_source_sha256",
    "native_binding_python_sha256": "strict_native_horner.binding_python_sha256",
    "native_native_coefficient_buffer_sha256": "strict_native_horner.native_coefficient_buffer_sha256",
    "native_compiler": "strict_native_horner.compiler",
    "native_compiler_sha256": "strict_native_horner.compiler_sha256",
    "native_compiler_version": "strict_native_horner.compiler_version",
    "native_compiler_target": "strict_native_horner.compiler_target",
    "native_binary_bytes": "strict_native_horner.binary_bytes",
    "native_binary_sha256": "strict_native_horner.binary_sha256",
    "native_initial_rounding_code": "strict_native_horner.initial_rounding_code",
    "native_initial_mxcsr": "strict_native_horner.initial_mxcsr",
    "native_last_rounding_code": "strict_native_horner.last_rounding_code",
    "native_last_mxcsr": "strict_native_horner.last_mxcsr",
    "native_native_calls": "strict_native_horner.native_calls",
    "native_native_radial_elements": "strict_native_horner.native_radial_elements",
    "native_element_Horner_updates": "strict_native_horner.element_Horner_updates",
    "native_whole_original_fallback_calls": "strict_native_horner.whole_original_fallback_calls",
    "native_compile_error": "strict_native_horner.compile_error",
    "native_scientific_speedup_measured": "strict_native_horner.scientific_speedup_measured"
  },
  "buildSelectors": {
    "native_build_schema": "schema",
    "native_build_complete": "complete",
    "native_build_phase": "phase",
    "native_build_source_commit": "source_commit",
    "native_build_workflow_trigger_commit": "workflow_trigger_commit",
    "native_build_github_run_id": "github_run_id",
    "native_build_github_run_attempt": "github_run_attempt",
    "native_build_node_version": "node_version",
    "native_build_python_version": "python_version",
    "native_build_original_entry_kind": "original_entry_kind",
    "native_build_original_entry_argument_count": "original_entry_argument_count",
    "native_build_generated_sources_complete": "generated_sources_complete",
    "native_build_builder_returncode": "builder_returncode",
    "native_build_child_started": "child_started",
    "native_build_child_returncode": "child_returncode",
    "native_build_successful_process_return": "successful_process_return",
    "native_build_wrapper_source": "wrapper_source.sha256",
    "native_build_source_builder": "complete_source_builder.sha256",
    "native_build_entry_source": "actual_original_entry_source.sha256",
    "native_build_full_materialization": "complete_materialization_record.sha256",
    "native_build_full_file_count": "complete_materialization.complete_source_file_count",
    "native_build_scientific_role_count": "scientific_role_count",
    "native_build_current_complete_runtime_source_count": "current_complete_runtime_source_count",
    "native_build_all_original_method_guards_retained": "all_original_method_guards_retained",
    "native_build_explicit_complete_method_replacements": "explicit_complete_method_replacements",
    "native_build_extra_scientific_preflight_or_fixture": "extra_scientific_preflight_or_fixture"
  },
  "prepared": "2026-11-28 16:59 UTC",
  "targetPaths": {
    "science": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-R729-native-horner-science-complete-ready.json",
    "pure": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-R729-native-horner-pure-complete-ready.json"
  }
};
const outputs = {
  "science": {
    "role": "science",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-R729-native-horner-science-complete-ready.json",
    "name": "fixed-fejer-halfwave-R729-native-horner-science-complete-ready.json",
    "bytes": 93038,
    "sha256": "bb28cba94271c8cee91886338979dd28852de30d8df2d8f46d8934a5ef48a69d",
    "git_blob_sha": "efbfd82b3bb379bc49f1dc24a314e63b2ba8060a"
  },
  "pure": {
    "role": "pure",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-R729-native-horner-pure-complete-ready.json",
    "name": "fixed-fejer-halfwave-R729-native-horner-pure-complete-ready.json",
    "bytes": 77713,
    "sha256": "4fcec48ed389cb41964333a2642054f02360be9bc4b9f69f97ed6f4095d4f174",
    "git_blob_sha": "53e38d2d064afcd16bad52ce7c9df255f6cf5150"
  }
};
const historicalCommit = '43914b1da832b13ffc65f9f3074446217fc065b9';
function makeReady(parent, kind, spec) {
    const oldStep = parent.steps[0];
    const step = JSON.parse(JSON.stringify(oldStep).replaceAll(spec.oldNamespace, spec.newNamespace));
    const oldArguments = step.args.slice();
    const buildPath = 'native-horner-' + kind + '-source-build.json';
    step.id = 'complete-fixed-fejer-native-horner-' + kind + '-20261128';
    step.script = spec.wrapper.path;
    step.scope += ' Build all seventeen source files on the selected trigger commit. Use the strict binary64 native Horner operator only in eligible ordinary detached value paths. Preserve every original phase, forced reread and differentiation path. Public comparison to original checkpoints requires their actual full-point SHA256.';
    step.args = ['--entry', kind, '--build-record', '{work}/' + buildPath, '--', ...oldArguments];
    step.outputs.push(buildPath, buildPath + '.materialization.json');
    step.summary[buildPath] = spec.buildSelectors;
    if (kind === 'science') {
        const progress = spec.newNamespace + '/actual-normal-evaluation-progress.json';
        Object.assign(step.progress_summary[progress], spec.nativeSelectors);
        step.summary[progress] = spec.nativeSelectors;
    }
    const count = mapping => Object.values(mapping || {}).reduce((total, group) => total + Object.keys(group).length, 0);
    const pointer = key => ({complete_file: spec.source, json_pointer: '/' + key, whole_file_required: true});
    return {
        schema: 'complete-halfwave-R729-native-horner-run47-' + kind + '-v1',
        prepared_utc: spec.prepared, intended_independent_runner_label: 47,
        status: 'Complete reproducible prepared configuration. No future run, binary or field is asserted.',
        executed: false, namespace: spec.newNamespace, current_source_publication_at_preparation: null,
        original_whole_ready_document: spec.oldReady[kind], complete_original_parent_binding: parent.complete_parameter_binding,
        all_complete_original_parent_metadata: parent.all_complete_original_parent_metadata,
        original_complete_parent_step: parent.original_complete_parent_step,
        complete_original_peer_history: parent.complete_original_peer_history,
        complete_current_peer_responsibilities: parent.complete_current_peer_responsibilities,
        complete_current_source_delivery: spec.source,
        current_complete_source_registry: pointer('complete_source_role_registry'),
        current_complete_runtime_records: pointer('current_complete_runtime_sources'),
        current_complete_source_roles: 140, current_complete_runtime_files: 23,
        original_scientific_role_count: 138, original_runtime_count: 21,
        required_pure_frame_validator: parent.complete_pure_frame_validator_helper,
        pure_frame_helper_is_scientific_source_role: false,
        full_original_scientific_budget: parent.full_original_scientific_budget,
        complete_current_physical_seed_recipe: parent.complete_current_physical_seed_recipe,
        full_current_algorithm_contract: parent.full_current_algorithm_contract,
        full_R729_scalar_correspondence: parent.full_R729_scalar_correspondence,
        complete_original64_live_correspondence: parent.complete_original64_live_correspondence,
        old_original_report_objects_and_legacy_QP_meanings_preserved: true,
        new_AST_fixture_benchmark_preflight_or_scientific_gate: false,
        numerical_argument_word_changes: [], original_scientific_argument_word_count: oldArguments.length,
        outer_build_argv_word_count: step.args.length, original_formal_selector_count: count(oldStep.summary),
        current_formal_selector_count: count(step.summary), original_live_selector_count: count(oldStep.progress_summary),
        current_live_selector_count: count(step.progress_summary),
        namespace_changes: 'Only the complete run-local output namespace changes in the original scientific argument list. All numerical flags and peer words are preserved.',
        actual_future: {run:null,model:null,point:null,compiled_binary:null,accepted_directions:null,
            numerical_speedup:null,complete_field:null,pure_readout:null,strict_certificate:null},
        kind, steps: [step]
    };
}

const root = resolve(process.argv[2] || '.');
const destination = resolve(process.argv[3] || root);
function identify(bytes) {
    const hash = (kind, data) => createHash(kind).update(data).digest('hex');
    return {bytes: bytes.length, sha256: hash('sha256',bytes),
        git_blob_sha:hash('sha1',Buffer.concat([Buffer.from('blob ' + bytes.length + '\0'),bytes]))};
}
function same(bytes, row) {
    const actual = identify(bytes);
    return ['bytes','sha256','git_blob_sha'].every(key => actual[key] === row[key]);
}
async function readParent(row) {
    let bytes;
    try { bytes = await readFile(resolve(root, row.path)); } catch (error) {
        if (error.code !== 'ENOENT') throw error;
    }
    if (!bytes || !same(bytes, row)) {
        bytes = execFileSync('git',['-C',root,'show',historicalCommit+':'+row.path],{maxBuffer:1000000});
    }
    if (!same(bytes,row)) throw Error('Complete original ready document differs: ' + row.path);
    return JSON.parse(bytes.toString('utf8'));
}
for(const kind of ['science','pure']) {
    const parent = await readParent(spec.oldReady[kind]);
    const value = makeReady(parent,kind,spec);
    const bytes = Buffer.from(JSON.stringify(value,null,1)+'\n');
    if (!same(bytes,outputs[kind])) throw Error('Complete run47 parameter identity differs: ' + kind);
    const path=resolve(destination,outputs[kind].path);
    await mkdir(dirname(path),{recursive:true});
    await writeFile(path,bytes);
    process.stdout.write(JSON.stringify({kind,path,...identify(bytes)})+'\n');
}
