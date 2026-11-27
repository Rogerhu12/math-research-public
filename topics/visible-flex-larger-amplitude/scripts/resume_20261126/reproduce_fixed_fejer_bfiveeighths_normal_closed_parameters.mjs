#!/usr/bin/env node
// Complete JSON-only parameter reconstruction. No scientific runtime is imported.
// This optional reproducer is not a solver prerequisite or validation gate.
import fs from "node:fs"; import path from "node:path"; import crypto from "node:crypto";
const root=path.resolve(process.argv[2]||".");
const cfg={
  "prepared_utc": "2026-11-27 23:35:50 UTC",
  "old_namespace": "fixed-fejer-meridian-batched-bhalf-first",
  "new_namespace": "fixed-fejer-meridian-batched-bfiveeighths-first",
  "whole_parent_records": [
    {
      "role": "normal_ready",
      "name": "fixed-fejer-meridian-batched-bhalf-first-R722-complete-normal32-full-circle-sixjet-fees-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R722-complete-normal32-full-circle-sixjet-fees-ready.json",
      "bytes": 49322,
      "sha256": "14e6ac6d8e95721a8fc1ddf983c7d3c67258f9daa41d01fefab955491d74d39a",
      "git_blob_sha": "bae2aeb057b0d1c58d6520038a3467bb4b2548b9",
      "fixed_commit": "6167a8bd8fd01c984095e705874e7516ea3fcb6c"
    },
    {
      "role": "geometry_ready",
      "name": "fixed-fejer-meridian-batched-bhalf-first-R722-complete-continuous-gram-curvature-support-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R722-complete-continuous-gram-curvature-support-ready.json",
      "bytes": 48299,
      "sha256": "d43d408cb4612a8998256e4e0d85085bb4041f0abf7e47dc89e5dd6b3e0874cc",
      "git_blob_sha": "bab97b529ea6e68d19fbd92335bd7064ef283202",
      "fixed_commit": "6167a8bd8fd01c984095e705874e7516ea3fcb6c"
    },
    {
      "role": "closed_ready",
      "name": "fixed-fejer-meridian-batched-bhalf-first-R722-closed-phase-grip-r718-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R722-closed-phase-grip-r718-ready.json",
      "bytes": 74772,
      "sha256": "6ea0e0482697134be32ef6ff080aea7007297116c2ad679a874087e61e3c972f",
      "git_blob_sha": "f5392f425a12a8b219f517f235c368e29e66f7ff",
      "fixed_commit": "6167a8bd8fd01c984095e705874e7516ea3fcb6c"
    },
    {
      "name": "fixed-fejer-meridian-batched-bhalf-first-R723-directional-closed-phase-grip-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R723-directional-closed-phase-grip-ready.json",
      "bytes": 86836,
      "sha256": "5a072e9c1030f146f46084d3b395300f7c79b52bb0c88830a55d0b3188464d9f",
      "git_blob_sha": "80e5cf779dbe6d8bb811561aaf55da036669eca0",
      "role": "complete_bhalf_R723_closed_parameters",
      "fixed_commit": "52decf9d255faf5d569a3dac00a93d55d2c5f9dd"
    }
  ],
  "current_science_record": {
    "role": "science",
    "name": "fixed-fejer-meridian-bfiveeighths-science-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bfiveeighths-science-complete-ready.json",
    "sha256": "6838b79823f398d930982b2d10fd28baf5a6a2f60eb866403331bfd34eb67d9d",
    "bytes": 97307,
    "git_blob_sha": "6da95445b088f8593ff0f5fb14d76167b26a7a21",
    "sha": "6da95445b088f8593ff0f5fb14d76167b26a7a21",
    "published_commit": "dd02e95f7ee748618e0657ac42c8e69d056a3587"
  },
  "current_pure_record": {
    "role": "pure",
    "name": "fixed-fejer-meridian-bfiveeighths-pure-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bfiveeighths-pure-complete-ready.json",
    "sha256": "b750fd865256366a5fcf6b020570a74c053ad853d4b34d0ff983ad3895388822",
    "bytes": 86702,
    "git_blob_sha": "5b2b58e75572b75ce499c8983adf3ba20278211b",
    "sha": "5b2b58e75572b75ce499c8983adf3ba20278211b",
    "published_commit": "dd02e95f7ee748618e0657ac42c8e69d056a3587"
  },
  "current_parameter_manifest_record": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-parameter-delivery.json",
    "bytes": 52529,
    "sha256": "550ae5ff18b9022bed7ec000c9c63b5958701f632aea100f59f338da249c971e",
    "sha": "8125f12b1c6df083945afe30bb412577428b5b32",
    "git_blob_sha": "8125f12b1c6df083945afe30bb412577428b5b32",
    "published_commit": "dd02e95f7ee748618e0657ac42c8e69d056a3587"
  },
  "full_ordinary_post_source_manifest": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bhalf-R722-complete-post-parameter-delivery.json",
    "bytes": 44101,
    "sha256": "fc0c9d2eecced80287bdff4d21bd775a4cb8338b7622e4397d421a060321a812",
    "git_blob_sha": "7a0378cc3ae91d59cebd8747be5ccd1d0b4b0382",
    "published_commit": "6167a8bd8fd01c984095e705874e7516ea3fcb6c"
  },
  "full_R723_source_manifest": {
    "path": "topics/visible-flex-larger-amplitude/computations/R723-directional-closed-grip-R716-complete-delivery.json",
    "bytes": 48223,
    "sha256": "b16346ee6f96d8aedc0f89a2ad6598a53b86af05cb1c3171ec1790e53bb896cc",
    "git_blob_sha": "1929f73367894f35c92e6dfa86198a70889c4da0",
    "published_commit": "52decf9d255faf5d569a3dac00a93d55d2c5f9dd"
  },
  "binding_path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-normal-closed-parameter-binding.json",
  "constructor_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_bfiveeighths_normal_closed_parameters.mjs",
  "output_paths": [
    "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bfiveeighths-first-R722-complete-normal32-full-circle-sixjet-fees-ready.json",
    "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bfiveeighths-first-R722-complete-continuous-gram-curvature-support-ready.json",
    "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bfiveeighths-first-R722-closed-phase-grip-r718-ready.json",
    "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bfiveeighths-first-R723-directional-closed-phase-grip-ready.json"
  ]
};
const expected=[
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-bfiveeighths-complete-normal-closed-parameter-binding.json",
    "bytes": 64060,
    "sha256": "3b6e8e082746a1900b79a60772c0d92d3c9ed608d72951a21ba2175946b846c1",
    "sha": "033bc2427bd70d86a639c6c3a38b3314f3ebe5b5",
    "git_blob_sha": "033bc2427bd70d86a639c6c3a38b3314f3ebe5b5"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bfiveeighths-first-R722-complete-normal32-full-circle-sixjet-fees-ready.json",
    "bytes": 8764,
    "sha256": "335bafdb6fb143ff4c57ef417aafb9f611d01e42c3fa9b5ebbbfd4c17cf350db",
    "sha": "dc1cbfe46c88f03b94c04363b343e21c82356b64",
    "git_blob_sha": "dc1cbfe46c88f03b94c04363b343e21c82356b64"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bfiveeighths-first-R722-complete-continuous-gram-curvature-support-ready.json",
    "bytes": 8907,
    "sha256": "f16f2d4d07a17892bc7c3c6bf33e8fc221e85d4dea26aec37d227e8be21792c2",
    "sha": "f451bcd1bcdb87c70e86429e4b69b53574ecfa78",
    "git_blob_sha": "f451bcd1bcdb87c70e86429e4b69b53574ecfa78"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bfiveeighths-first-R722-closed-phase-grip-r718-ready.json",
    "bytes": 11677,
    "sha256": "c6efd5a221411c0be120452618bed2b489a6fa71910f20f6e2730ca643859da3",
    "sha": "e97921b8d74dc79b0e20f659becae35ffb720d0d",
    "git_blob_sha": "e97921b8d74dc79b0e20f659becae35ffb720d0d"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bfiveeighths-first-R723-directional-closed-phase-grip-ready.json",
    "bytes": 10742,
    "sha256": "28907d75504593294e6957536245c442dba6f48a46a417c41f866c8f66893af6",
    "sha": "c11b75128bb501a2b772c1103c2aef72b0e8eb9e",
    "git_blob_sha": "c11b75128bb501a2b772c1103c2aef72b0e8eb9e"
  }
];
const sha=(b,a="sha256")=>crypto.createHash(a).update(b).digest("hex");
const blob=b=>sha(Buffer.concat([Buffer.from("blob "+b.length+"\0"),b]),"sha1");
function record(pathname,text){const b=Buffer.from(text);return {path:pathname,bytes:b.length,sha256:sha(b),sha:blob(b),git_blob_sha:blob(b)};}
function read(r){const b=fs.readFileSync(path.join(root,r.path));if(b.length!==r.bytes||sha(b)!==r.sha256||blob(b)!==(r.git_blob_sha||r.sha))throw Error("Complete parameter parent differs: "+r.path);return JSON.parse(b.toString("utf8"));}
function buildCompleteNormalClosed(parents,currentScience,currentParams,cfg,makeRecord){
 const copy=x=>JSON.parse(JSON.stringify(x)),relocate=x=>typeof x==="string"?x.split(cfg.old_namespace).join(cfg.new_namespace):Array.isArray(x)?x.map(relocate):x&&typeof x==="object"?Object.fromEntries(Object.entries(x).map(([k,v])=>[relocate(k),relocate(v)])):x;
 const binding={
 schema:"complete-bfiveeighths-normal-R722-closed-R723-parameter-binding-v1",
 prepared_utc:cfg.prepared_utc,executed:false,queued:false,
 current_namespace:cfg.new_namespace,
 complete_current_science_parameter_file:cfg.current_science_record,
 complete_current_pure_parameter_file:cfg.current_pure_record,
 complete_current_parameter_delivery:cfg.current_parameter_manifest_record,
 all_137_complete_current_source_roles:copy(currentParams.current_complete_source_role_registry),
 all_18_current_runtime_records:copy(currentParams.current_complete_runtime_sources),
 all_original120_source_pairs_preserved:true,
 current_complete_scientific_argv:copy(currentScience.steps[0].args),
 current_complete_scientific_parameter_delta:copy(currentScience.bfiveeighths_complete_parameter_delta),
 original_science_formal445_and458_and_live48_location:{science:cfg.current_science_record,pure:cfg.current_pure_record,science_formal:458,pure_formal:445,science_live:48,whole_steps_not_shortened:true},
 complete_parameter_history_sources:copy(cfg.whole_parent_records),
 all_original_parent_top_level_and_nested_metadata_retained_in_exact_whole_files:true,
 original_parent_metadata_not_replaced_by_this_binding:true,
 original_step_scopes:parents.map(x=>x.steps[0].scope),
 current_seed_parameters:copy(currentParams.planned_seed_parameters),
 current_initial_damping:copy(currentParams.planned_initial_damping),
 entire_external_peer_obligations:copy(currentScience.external_unregistered_peer_obligations),
 full_external_peer_status:currentScience.external_peer_status,
 full_original_supported_five_pending_CLI_pairs_in_current_complete_argv:true,
 new_verified_external_peer_records:copy(currentParams.new_known_external_peer_records),
 full_ordinary_post_source_manifest:cfg.full_ordinary_post_source_manifest,
 full_R723_source_manifest:cfg.full_R723_source_manifest,
 scientific_or_postprocessing_runtime_rewrites:[],
 entire_original_normal32_fullcircle1024_radial922_all_exact_cuts_sixjets_tail_domains_retained:true,
 all_source_specific_R722_posterior_R709_actual_bool_and_R710_R711_contracts_retained:true,
 complete_downstream_normal_geometry_closed_R718_R716_source_and_main_sidecar_contracts_retained:true,
 original_all_scalar_formal_selector_pairs_and_numerical_budgets_preserved:true,
 binding_and_continuation_contract:{
   normal_first_full_step_uses_its_actual_repo_and_scientific_report_snapshot_inputs:true,
   normal_repeated_complete_pass_uses_same_actual_repo_absolute_path_and_exact_input_binding:true,
   normal_repeat_new_controller_step_id_allowed_if_original_data_and_repo_binding_unchanged:true,
   new_repo_with_same_source_bytes_does_not_preserve_normal_absolute_source_path_identity:true,
   actual_repo_and_source_worktree_paths_not_known_until_real_return:true,
   geometry_after_complete_stable_whole_normal_report:true,
   geometry_reuse_preserves_its_first_actual_source_paths_and_whole_normal_report_record:true,
   fresh_whole_normal_report_sha_requires_fresh_geometry_outdir_if_prior_binding_exists:true,
   R723_requires_new_fresh_outdir_for_every_new_invocation:true,
   every_original_partial_output_preserved_before_new_parameters:true,
   source_binding_is_original_contract_not_new_numerical_admission_gate:true
 },
 physical_scope:{
   same_fixed_g_new_seed_not_same_field:true,
   complete_required_angle_immutable_snapshot_distinct_from_partial_mutable_progress_and_final13:true,
   normal_complete_does_not_prove_continuous_normal_branch:true,
   complete_geometry_must_pay_exact_source_declared_full_domains_and_accuracy:true,
   original_002eb_R722_old_eight_roles_are_not_R723_roles:true,
   R723_all_original_signed_leaves_common_beta_curvature_caps_mixed_pairs_and_joint_flow:true,
   marked_actual_sigma_for_R718_not_directional_radius:true,
   R716_independent_unmarked_outward_tube_positive_volume_and_nonzero_invariant_still_required:true,
   current_delta_hold_pointtwoD_not_paid_by_standard_pointzeroFiveD:true,
   raw_reports_arrays_snapshots_fees_meshes_only_public_runner_scratch:true
 },
 future_actual:{run_id:null,source_commits:null,reference_records:null,model:null,point:null,snapshot:null,scientific_report:null,normal_first_repo_path:null,normal_report:null,geometry_report:null,closed_R722:null,closed_R723:null,fees_or_completion:null},
 full_parameter_reproducer:cfg.constructor_path,
 no_local_scientific_AST_fixture_or_benchmark_or_new_admission:true
 };
 const bbody=JSON.stringify(binding,null,2)+"\n",brec=makeRecord(cfg.binding_path,bbody);
 const all=parents.map((parent,i)=>{
  if(parent.steps.length!==1)throw Error("Whole original one-step parent required");
  const old=parent.steps[0],step=relocate(copy(old));
  step.scope=step.scope.replaceAll("run19","run21").replaceAll("b/S=1/2","b/S=5/8").replaceAll("boundary measure 1/2","boundary measure 5/8").replaceAll("boundary total length 1/2","boundary total length 5/8");
  if(i===3)step.id=step.id.replace("fixed-fejer-bhalf-R723","fixed-fejer-bfiveeighths-R723");
  const changed=step.args.map((v,j)=>v===old.args[j]?null:{index:j,before:old.args[j],after:v}).filter(Boolean);
  const out={schema:"whole-step-bfiveeighths-normal-geometry-closed-parameter-v1",prepared_utc:cfg.prepared_utc,executed:false,queued:false,complete_current_binding:brec,complete_parent_parameter_file:cfg.whole_parent_records[i],all_original_parent_metadata_retained_by_exact_whole_file:true,all_original_step_fields_preserved_except_explicit_namespace_scope_and_id:true,original_step_id:old.id,current_step_id:step.id,original_scope_in_full_binding_and_parent:true,complete_argument_differences:changed,argument_count:step.args.length,formal_selector_count:Object.values(step.summary??{}).reduce((n,v)=>n+Object.keys(v).length,0),all_original_numeric_parameters_domains_budgets_and_selector_pairs_unchanged:true,no_runtime_source_changed:true,parameter_stage:["complete_normal_fees","complete_continuous_geometry","original_R722_closed_grip_R718","independent_R723_closed_grip_R718"][i],downstream_execution_is_not_automatically_queued_with_partial_predecessors:true,future_actual:null,steps:[step]};
  return out;
 });
 return {binding,binding_record:brec,readies:all};
}
const out=buildCompleteNormalClosed(cfg.whole_parent_records.map(read),read(cfg.current_science_record),read(cfg.current_parameter_manifest_record),cfg,record);
const outputs=[out.binding,...out.readies];
for(let i=0;i<outputs.length;i++){
 const r=expected[i],text=JSON.stringify(outputs[i],null,2)+"\n",actual=record(r.path,text);
 if(actual.bytes!==r.bytes||actual.sha256!==r.sha256||actual.sha!==r.git_blob_sha)throw Error("Complete generated parameter identity differs: "+r.path);
 const dest=path.join(root,r.path);fs.mkdirSync(path.dirname(dest),{recursive:true});
 if(fs.existsSync(dest)&&!fs.readFileSync(dest).equals(Buffer.from(text)))throw Error("Different output already exists: "+r.path);
 fs.writeFileSync(dest,text);process.stdout.write(JSON.stringify(actual)+"\n");
}
