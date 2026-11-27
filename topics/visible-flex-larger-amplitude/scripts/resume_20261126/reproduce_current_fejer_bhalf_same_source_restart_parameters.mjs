#!/usr/bin/env node
// Complete text-only reproduction of the four pinned same-source restart parameter files.
// This program neither imports nor executes a scientific runtime. It is optional
// parameter reconstruction, not a prerequisite or admission gate for a solver.
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
const root=path.resolve(process.argv[2]||".");
const configs=[
  {
    "prepared_utc": "2026-11-27 23:08:52 UTC",
    "current_source_package": {
      "name": "fixed-fejer-meridian-producer-binding-repair-complete-delivery.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-producer-binding-repair-complete-delivery.json",
      "bytes": 52830,
      "sha256": "970b8f8bbb141fc7f1c4e5e42d6048497f0de58731e65918f3c4e4cf6aff008a",
      "git_blob_sha": "45f14a52f824ca947a59bacf73ad123f17fddab9",
      "published_commit": "8c1251a01aa2a1893386b69d13ab1e0a5ae4aa38"
    },
    "full_registry": {
      "complete_file": {
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-mu001-complete-parameter-delivery.json",
        "bytes": 50679,
        "sha256": "ce445da032ffedff5e03e40b89e09096cba3e7e147f256968774a6c6e72d21b4",
        "sha": "8eee403a87c988cb36fb55f6f82eb3ad0e1988db",
        "git_blob_sha": "8eee403a87c988cb36fb55f6f82eb3ad0e1988db"
      },
      "json_field": "current_complete_source_role_registry",
      "role_count": 137,
      "all_original120_pairs_retained": true
    },
    "constructor_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_current_fejer_bhalf_same_source_restart_parameters.mjs",
    "metric_damping": ".01",
    "origin_run_label": "19",
    "origin_run_id": 46076669320,
    "old_namespace": "fixed-fejer-meridian-batched-bhalf-first",
    "new_namespace": "fixed-fejer-meridian-batched-bhalf-restart-01",
    "science_parent": {
      "name": "fixed-fejer-meridian-bhalf-science-complete-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-science-complete-ready.json",
      "bytes": 90652,
      "sha256": "242dd96148ddee96cf829433a4f399e2a2bc052671a92905722c8de8110f2c67",
      "git_blob_sha": "9c4c28ef3c5b189e094c65f51038fafeef48bc48",
      "sha": "9c4c28ef3c5b189e094c65f51038fafeef48bc48",
      "fixed_commit": "543cfdf281c9bcd0f9b13197721b003a275c5967"
    },
    "pure_parent": {
      "name": "fixed-fejer-meridian-bhalf-pure-complete-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-pure-complete-ready.json",
      "bytes": 80254,
      "sha256": "8a5f9ff71bc598f77b25c36aeaad833f048dc6b4d218de2df44fda92709e73b7",
      "git_blob_sha": "202b6ca81c72c009c34c04094ef234db2e337328",
      "sha": "202b6ca81c72c009c34c04094ef234db2e337328",
      "fixed_commit": "543cfdf281c9bcd0f9b13197721b003a275c5967"
    },
    "restoration_damping": ".01",
    "output_science_path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-same-source-restart01-science-ready.json",
    "output_pure_path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-same-source-restart01-pure-ready.json"
  },
  {
    "prepared_utc": "2026-11-27 23:08:52 UTC",
    "current_source_package": {
      "name": "fixed-fejer-meridian-producer-binding-repair-complete-delivery.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-producer-binding-repair-complete-delivery.json",
      "bytes": 52830,
      "sha256": "970b8f8bbb141fc7f1c4e5e42d6048497f0de58731e65918f3c4e4cf6aff008a",
      "git_blob_sha": "45f14a52f824ca947a59bacf73ad123f17fddab9",
      "published_commit": "8c1251a01aa2a1893386b69d13ab1e0a5ae4aa38"
    },
    "full_registry": {
      "complete_file": {
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-mu001-complete-parameter-delivery.json",
        "bytes": 50679,
        "sha256": "ce445da032ffedff5e03e40b89e09096cba3e7e147f256968774a6c6e72d21b4",
        "sha": "8eee403a87c988cb36fb55f6f82eb3ad0e1988db",
        "git_blob_sha": "8eee403a87c988cb36fb55f6f82eb3ad0e1988db"
      },
      "json_field": "current_complete_source_role_registry",
      "role_count": 137,
      "all_original120_pairs_retained": true
    },
    "constructor_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_current_fejer_bhalf_same_source_restart_parameters.mjs",
    "metric_damping": ".01",
    "origin_run_label": "20",
    "origin_run_id": 46079535427,
    "old_namespace": "fixed-fejer-meridian-batched-bhalf-mu001-first",
    "new_namespace": "fixed-fejer-meridian-batched-bhalf-mu001-restart-01",
    "science_parent": {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-mu001-science-complete-ready.json",
      "bytes": 97019,
      "sha256": "89b437a4986b3172d281b4928353072d15a15f2cebbb7a1fd8d973880d5166ca",
      "sha": "598b4cdf62021a66b54c22b71171722027f1c0b5",
      "git_blob_sha": "598b4cdf62021a66b54c22b71171722027f1c0b5",
      "fixed_commit": "85cd235221ace28158625a7ced52a24551b509eb"
    },
    "pure_parent": {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-mu001-pure-complete-ready.json",
      "bytes": 86221,
      "sha256": "f627447f7887bdc9d7f257b4d0772173556683501cd5fa9f1e39890ec7ac7f64",
      "sha": "53655fce8344040770e02295898a1c4ae9a06ebf",
      "git_blob_sha": "53655fce8344040770e02295898a1c4ae9a06ebf",
      "fixed_commit": "85cd235221ace28158625a7ced52a24551b509eb"
    },
    "restoration_damping": ".001",
    "output_science_path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-mu001-same-source-restart01-science-ready.json",
    "output_pure_path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-mu001-same-source-restart01-pure-ready.json"
  }
];
const expected=[
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-same-source-restart01-science-ready.json",
    "bytes": 73350,
    "sha256": "9ad22f878c1da1184e8d8d27fff28a6538bcf6a7bb40a1085e2dcdae8154167d",
    "sha": "17a4606638aa4f13b06c71c18cd4db8e8f1cca9b",
    "git_blob_sha": "17a4606638aa4f13b06c71c18cd4db8e8f1cca9b",
    "role": "run19_science"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-same-source-restart01-pure-ready.json",
    "bytes": 63154,
    "sha256": "fd0127d7461e414777e58f01795ef7250683437b6667c8da02cd7811623f7a22",
    "sha": "b6b77ca1344370ca3cf59585957104def21b33b9",
    "git_blob_sha": "b6b77ca1344370ca3cf59585957104def21b33b9",
    "role": "run19_pure"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-mu001-same-source-restart01-science-ready.json",
    "bytes": 73909,
    "sha256": "34f8ac4b28ae16da4915efabf4717d730249feef3372e3aec210a3723c1bd06a",
    "sha": "98ccc02122c202f056d0641371d4e69640ec9723",
    "git_blob_sha": "98ccc02122c202f056d0641371d4e69640ec9723",
    "role": "run20_science"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-mu001-same-source-restart01-pure-ready.json",
    "bytes": 63676,
    "sha256": "234778da8a578db019d05b7db412d53b167e580e33fae32df87957396d2068d5",
    "sha": "d4b4337428444c717403025446f1909d6e1d1b02",
    "git_blob_sha": "d4b4337428444c717403025446f1909d6e1d1b02",
    "role": "run20_pure"
  }
];
const sha=(b,alg="sha256")=>crypto.createHash(alg).update(b).digest("hex");
const gitblob=b=>sha(Buffer.concat([Buffer.from("blob "+b.length+"\0"),b]),"sha1");
function readWhole(r){
  const b=fs.readFileSync(path.join(root,r.path));
  if(b.length!==r.bytes||sha(b)!==r.sha256||gitblob(b)!==(r.git_blob_sha||r.sha))throw Error("Pinned complete parameter parent differs: "+r.path);
  return JSON.parse(b.toString("utf8"));
}
function buildRestartPair(parentScience,parentPure,config){
  const copy=x=>JSON.parse(JSON.stringify(x));
  const relocate=x=>{
    if(typeof x==="string")return x.split(config.old_namespace).join(config.new_namespace);
    if(Array.isArray(x))return x.map(relocate);
    if(x&&typeof x==="object")return Object.fromEntries(Object.entries(x).map(([k,v])=>[k.split(config.old_namespace).join(config.new_namespace),relocate(v)]));
    return x;
  };
  if(parentScience.steps.length!==1||parentPure.steps.length!==1)throw Error("Both whole immediate parent steps are required");
  const oldScience=parentScience.steps[0],oldPure=parentPure.steps[0];
  if(oldScience.args.length!==157||oldPure.args.length!==7)throw Error("The original complete parent argv changed");
  const science=relocate(copy(oldScience)),pure=relocate(copy(oldPure));
  const kept=[],removed=[],pendingRuns=[],pendingSources=[];
  let independentCount=0;
  for(let i=0;i<oldScience.args.length;i++){
    const word=oldScience.args[i];
    if(word==="--independent-envelope-branch"){removed.push(word);independentCount++;continue;}
    if(word==="--pending-parallel-envelope-run"||word==="--pending-parallel-envelope-source"){
      if(i+1>=oldScience.args.length)throw Error("Incomplete whole pending option");
      const value=oldScience.args[++i];removed.push(word,value);
      (word==="--pending-parallel-envelope-run"?pendingRuns:pendingSources).push(value);
      continue;
    }
    kept.push(relocate(word));
  }
  if(independentCount!==1||pendingRuns.length!==5||pendingSources.length!==5||removed.length!==21||kept.length!==136)throw Error("Only the existing independent invocation mode changes");
  science.args=[...kept,"--restart-report","{work}/"+config.old_namespace+"/report.json","--restart-checkpoint","{work}/"+config.old_namespace+"/final.npz"];
  science.parent_bundle=config.old_namespace+"/final.npz";
  science.scope="Complete same-source continuation of the actual run"+config.origin_run_label+" final field in the same available runner context, through the unchanged10fa/f600 runtime. The parent must really return a complete source/schema/model-bound report and its matching whole13-member final.npz; progress, a trial, accepted-only bundle or packet does not qualify. Restore every free word, all original permanent/typed/protected history, discovery annotations and full inherited unknown peer obligations. Re-evaluate the full baseline with the same original numerical parameters, all32 stages and full original domains/budgets; initial metric/restoration damping remains the declared CLI values, not the prior adapted values. The21 original independent-mode CLI words are represented by the complete inherited parent origin; no numeric budget, source, variable or selector is removed.";
  pure.scope="Read the actual whole same-source restart report, its complete original source closure, every input and inherited parent/history record, all original immutable packet and normal32 metadata and the genuine whole final13 checkpoint. The original8027 complete reader and all445 formal selector pairs remain; no F/J/root computation, inferred final or substitute progress object.";
  const common={
    schema:"complete-current-Fejer-bhalf-same-source-final-continuation-whole-step-v1",
    prepared_utc:config.prepared_utc,executed:false,queued:false,
    scientific_execution_permitted_only_in_public_Actions:true,
    actual_origin_run:{run_id:config.origin_run_id,attempt:1,original_namespace:config.old_namespace},
    current_namespace:config.new_namespace,
    complete_immediate_parameter_parents:{science:config.science_parent,pure:config.pure_parent},
    all_immediate_parent_metadata_preserved_in_complete_files:true,
    full_parent_files_not_a_reduced_or_sampled_history:true,
    complete_current_source_package:config.current_source_package,
    entire_137_role_registry:config.full_registry,
    all18_current_runtime_records:copy(parentScience.current_complete_runtime_sources),
    all_original120_path_SHA_pairs_retained:true,
    scientific_runtime_source_rewrites:[],
    original_whole_source_constructors:copy(parentScience.source_constructors),
    original_complete_display_correspondence:copy(parentScience.complete_current_display_correspondence),
    source_parameter_constructor_path:config.constructor_path,
    complete_original_invocation_mode:{removed_argv_in_original_order:removed,pending_runs:pendingRuns,pending_run_sources:pendingSources,old_science_scope:oldScience.scope,old_pure_scope:oldPure.scope,old_parent_bundle:oldScience.parent_bundle},
    current_parameter_contract:{
      original_science_words:157,current_science_words:140,original_common_words_retained_in_order:136,
      removed_mode_words:21,added_restart_words:4,
      independent_flag_incompatible_with_existing_restart_parser:true,
      old_pending_CLI_is_inherited_as_actual_full_parent_material_envelope_transfer_independent_branch_origin:true,
      all_original_numeric_option_strings_and_order_preserved:true,
      all_original_free_variables_and_32_stages_and_full_domains_and_budgets_preserved:true,
      formal_selector_counts:[458,445],all_original408_and395_formal_pairs_retained:true,
      complete_original_live_map:48,original6_normal_plus42_mathematical_fields_retained:true,
      prior_adaptive_damping_or_QP_or_normal_root_cache_state_automatically_restored:false,
      initial_metric_damping_cli:config.metric_damping,initial_restoration_damping_cli:config.restoration_damping,
      numerical_baseline_is_actually_recomputed:true,
      direction_counters_start_new_original_complete_budget:true,
      stop_at_budget_is_not_research_completion:true
    },
    same_source_contract:{
      driver_schema:"complete-fixed-fejer-meridian-batched-observed-material-envelope-SO3-QP-v1",
      driver_source_sha256:"10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f",
      launcher_source_sha256:"f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506",
      reader_source_sha256:"8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49",
      memory_transfer_source_sha256:"b8af97a4772e5d641c5daea3f2232c65fe52055154d94e45b4c88f661e9778dc",
      parent_report_complete:true,exact_parent_driver_schema_model_representation_scalar_carrier_and_final_bundle_required:true,
      whole_parent_point_and_typed_history_not_new_reference_initialization:true,
      original_all_locations_and_restore_annotations_and_unknown_independent_origin_retained:true,
      same_runner_original_inputs_sources_and_inbound_history_paths_must_remain_available:true,
      complete_parent_source_bound_bytes_and_13_member_final_required:true,
      accepted_only_partial_or_mutable_progress_or_snapshot_is_not_parent:true,
      inherited_old_Phi_feasibility_or_certificates:false,
      platform_or_admission_window_assumed_available:false
    },
    all_original_external_unregistered_peer_obligations:copy(parentScience.external_unregistered_peer_obligations),
    original_external_peer_status:parentScience.external_peer_status,
    complete_original_failed_source_and_parameter_history_location:{whole_science_parent:config.science_parent,whole_pure_parent:config.pure_parent,all_original_nested_history_fields_retained_in_exact_pinned_parents:true},
    future_actual:{complete_parent_report_sha256:null,complete_parent_final_sha256:null,parent_model_identity_sha256:null,parent_point_sha256:null,new_source_commit:null,new_report_sha256:null,new_point_sha256:null,new_accepted_directions:null,new_geometry_or_final:null},
    original_complete_step_values_and_summary_mapping_not_shortened:true,
    new_observation_F_J_root_quadrature_or_acceptance_calls:0,
    separate_fixture_AST_compile_replay_or_approval_gate_added:false,
    raw_scientific_arrays_reports_checkpoint_packets_and_meshes_only_runner_scratch:true,
    constructor_is_optional_complete_text_parameter_reproduction_not_admission:true
  };
  const one=(step,index)=>({...copy(common),whole_parent_step_index:index,current_step_argv_words:step.args.length,current_complete_formal_fields:index===0?458:445,steps:[step]});
  return {science:one(science,0),pure:one(pure,1)};
}
for(const config of configs){
  const pair=buildRestartPair(readWhole(config.science_parent),readWhole(config.pure_parent),config);
  for(const role of ["science","pure"]){
    const r=expected.find(x=>x.path===config["output_"+role+"_path"]);
    const b=Buffer.from(JSON.stringify(pair[role],null,2)+"\n");
    if(!r||b.length!==r.bytes||sha(b)!==r.sha256||gitblob(b)!==r.git_blob_sha)throw Error("Complete generated text identity differs: "+role);
    const dest=path.join(root,r.path);
    fs.mkdirSync(path.dirname(dest),{recursive:true});
    fs.writeFileSync(dest,b);
    process.stdout.write(JSON.stringify({path:r.path,bytes:b.length,sha256:sha(b),git_blob_sha:gitblob(b)})+"\n");
  }
}
