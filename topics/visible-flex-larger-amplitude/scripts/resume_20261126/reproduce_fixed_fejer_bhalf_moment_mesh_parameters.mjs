#!/usr/bin/env node
/**
 * Complete bhalf-first R716 and final/packet mesh parameter construction.
 * Source-only JSON/text operation; not a scientific solver, replay gate,
 * source preflight, field evaluation, benchmark, or workflow dispatcher.
 * All runtime sources remain the complete published producer-bound family.
 * Read complete hashed parent plans; preserve all original numerical argv,
 * formal/live selectors and historical metadata. Emit the three entire plans.
 */
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

const TOPIC = "topics/visible-flex-larger-amplitude";
const PARENTS = [
  {
    "kind": "R716",
    "path": "computations/fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
    "parent": {
      "name": "fixed-fejer-meridian-batched-producer-R722-complete-R716-closed-flux-centred-moments-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-producer-R722-complete-R716-closed-flux-centred-moments-ready.json",
      "bytes": 55988,
      "sha256": "93113ca87b4b2c3f921da1fb2934064ed08155d9b5144ab404916a57d302b90d",
      "git_blob_sha": "e1628c1246bf8783055e16abe1053f6ecc0d23c7"
    },
    "publication": "bf5f7e9708e3438b3c4f0435e1c908b0f95f933a"
  },
  {
    "kind": "mesh_final",
    "path": "computations/fixed-fejer-meridian-batched-bhalf-first-same-field-phase-mesh-final-ready.json",
    "parent": {
      "name": "fixed-fejer-meridian-producer-bound-same-field-phase-mesh-final-ready.json",
      "path": "computations/fixed-fejer-meridian-producer-bound-same-field-phase-mesh-final-ready.json",
      "bytes": 75629,
      "sha256": "11f5a92dbaf7a74fc5e029c76cac2c459a401bfb1ab70ac3a4064ce243efb152",
      "git_blob_sha": "64e0976a17a9de8373ea1f226029792fd78c1d33"
    },
    "publication": "9356aa12459c861adf4ff9036d97ac5baa45c33e"
  },
  {
    "kind": "mesh_packet",
    "path": "computations/fixed-fejer-meridian-batched-bhalf-first-same-field-phase-mesh-packet-ready.json",
    "parent": {
      "name": "fixed-fejer-meridian-producer-bound-same-field-phase-mesh-packet-ready.json",
      "path": "computations/fixed-fejer-meridian-producer-bound-same-field-phase-mesh-packet-ready.json",
      "bytes": 75602,
      "sha256": "34c65ecad7ee9a2c2923ecbdd05801998b8b06ce27de5f94aba636286f372a50",
      "git_blob_sha": "f0ce1777ab1410e8c7f19dd7ec4629b9e25b55d1"
    },
    "publication": "9356aa12459c861adf4ff9036d97ac5baa45c33e"
  }
];
const SCIENTIFIC_PARAMETERS = [
  {
    "role": "current_complete_science_parameters",
    "path": "computations/fixed-fejer-meridian-bhalf-science-complete-ready.json",
    "bytes": 90652,
    "sha256": "242dd96148ddee96cf829433a4f399e2a2bc052671a92905722c8de8110f2c67",
    "git_blob_sha": "9c4c28ef3c5b189e094c65f51038fafeef48bc48"
  },
  {
    "role": "current_complete_pure_parameters",
    "path": "computations/fixed-fejer-meridian-bhalf-pure-complete-ready.json",
    "bytes": 80254,
    "sha256": "8a5f9ff71bc598f77b25c36aeaad833f048dc6b4d218de2df44fda92709e73b7",
    "git_blob_sha": "202b6ca81c72c009c34c04094ef234db2e337328"
  }
];
const OUTPUTS = [
  {
    "kind": "R716",
    "name": "fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
    "path": "computations/fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
    "bytes": 80089,
    "sha256": "3b49bd1b12b6b5680fd63a6cd8a5e8c34633626c875044a50ba98b6b1174441a",
    "git_blob_sha": "7d748fcb2ca892ce50c23d0153c198f99fc307db"
  },
  {
    "kind": "mesh_final",
    "name": "fixed-fejer-meridian-batched-bhalf-first-same-field-phase-mesh-final-ready.json",
    "path": "computations/fixed-fejer-meridian-batched-bhalf-first-same-field-phase-mesh-final-ready.json",
    "bytes": 91284,
    "sha256": "04456c30ae931cb8d10e2652c8ef51fcd5e6ad5bfe4141e129b7fb98a04bf9c9",
    "git_blob_sha": "aafad01042d2a1412d070c2e302d762b3d0244c8"
  },
  {
    "kind": "mesh_packet",
    "name": "fixed-fejer-meridian-batched-bhalf-first-same-field-phase-mesh-packet-ready.json",
    "path": "computations/fixed-fejer-meridian-batched-bhalf-first-same-field-phase-mesh-packet-ready.json",
    "bytes": 91233,
    "sha256": "eeb88aede82e6d447472c22d884a91a1dec044d4078b15503e25c956e11ba2f4",
    "git_blob_sha": "bb953c7250373eea6e263e19533282136622d5e3"
  }
];
const REPRODUCER_PATH = "scripts/resume_20261126/reproduce_fixed_fejer_bhalf_moment_mesh_parameters.mjs";


function clone(value) { return JSON.parse(JSON.stringify(value)); }
const OLD_NS = "fixed-fejer-meridian-batched-producer-bound";
const NEW_NS = "fixed-fejer-meridian-batched-bhalf-first";
const OLD_R716_ID = "fixed-fejer-meridian-batched-producer-R722";
const NEW_R716_ID = "fixed-fejer-meridian-batched-bhalf-first-R722";
function namespaced(value) {
  if (typeof value === "string") return value.split(OLD_NS).join(NEW_NS).split(OLD_R716_ID).join(NEW_R716_ID);
  if (Array.isArray(value)) return value.map(namespaced);
  if (value && typeof value === "object") return Object.fromEntries(Object.entries(value).map(([k,v])=>[namespaced(k),namespaced(v)]));
  return value;
}
function currentStep(parent) {
  const value=namespaced(parent);
  if (typeof value.scope==="string") {
    value.scope=value.scope.replace("actual run18 command","actual bhalf-first command")
      .replace("Actual complete repaired run18 source and input identities are read",
               "Actual complete bhalf-first source and input identities are read");
  }
  return value;
}
function counts(step) {
  return {argument_words:step.args.length,formal_summary_fields:Object.values(step.summary||{}).reduce((n,v)=>n+Object.keys(v).length,0),live_fields:Object.values(step.progress_summary||{}).reduce((n,v)=>n+Object.keys(v).length,0),output_count:step.outputs.length};
}
function checkStep(parent,child) {
  const p=counts(parent),c=counts(child);
  if(JSON.stringify(p)!==JSON.stringify(c))throw Error("Changed complete parameter/selector count");
  if(parent.script!==child.script || parent.parent_bundle!==child.parent_bundle)throw Error("Changed runtime or reference route");
  if(JSON.stringify(currentStep(parent))!==JSON.stringify(child))throw Error("Unlisted step mutation");
  return {parent_step_id:parent.id,current_step_id:child.id,counts:c,script_unchanged:parent.script,only_runner_namespace_step_id_and_current_scope_changed:true,current_scope_before:parent.scope,current_scope_after:child.scope,all_full_argument_tokens_preserved_except_namespace:true,all_formal_and_live_selector_values_preserved:true};
}
function plannedScience(meshParent,sourceRecords) {
  const p=meshParent.complete_original_scientific_parameter_source;
  const args=clone(p.original_complete_argv);
  if(args.length!==157)throw Error("Keep all 157 original science words");
  const width=args.indexOf("--seed-boundary-total-length"),out=args.indexOf("--outdir"),delta=args.indexOf("--seed-profile-delta");
  if(width<0||args[width+1]!=="1/4"||out<0||args[out+1]!=="{work}/"+OLD_NS||delta<0||args[delta+1]!=="1/32")throw Error("Unexpected complete parent seed/source arguments");
  args[width+1]="1/2";args[out+1]="{work}/"+NEW_NS;
  const differences=args.map((v,i)=>v===p.original_complete_argv[i]?null:{index:i,before:p.original_complete_argv[i],after:v}).filter(Boolean);
  if(differences.length!==2)throw Error("More than explicit width and namespace changed");
  return {
    intended_runner_label:"parallel19",
    actual_run_id:null,actual_run_attempt:null,actual_source_commit:null,
    actual_input_files:null,actual_input_binding_sha256:null,
    actual_report_sha256:null,actual_model_identity_sha256:null,actual_point_sha256:null,
    actual_snapshot_identity_sha256:null,actual_final_checkpoint_sha256:null,
    complete_current_scientific_parameter_files:clone(sourceRecords),
    complete_parent_scientific_parameter_file:{name:p.name,path:p.path,bytes:p.bytes,sha256:p.sha256,git_blob_sha:p.git_blob_sha},
    complete_parent_scientific_source_roles_location:"complete_original_scientific_parameter_source.original_complete_source_sha256_by_role in the whole parent mesh-ready file; all 137 pairs are unchanged",
    current_complete_scientific_script:p.original_script,
    current_complete_scientific_argv:args,scientific_argument_words:157,
    original_complete_argv_difference: differences,
    actual_required_scientific_report:"{work}/"+NEW_NS+"/report.json",
    actual_required_original_command:"{work}/"+NEW_NS+"-command.json",
    actual_command_and_report_are_required_for_runtime_source_model_point_binding:true,
    current_fields_not_inherited_from_parent_run18:true,
    fixed_mathematical_metric_is_the_same_declared_Fejer_recipe:true,
    selected_initial_seed_boundary_total_relative_length:"1/2",
    selected_seed_profile_delta:"1/32",
    unchanged_solver_controls_rows_stages_budgets_and_stopping_rules:true,
    old_scientific_run_or_old_mutable_observation_not_a_current_field_input:true
  };
}
function plannedSeed(parent) {
  return {...clone(parent||{}),
    relative_boundary_total_length:"1/2",profile_delta:"1/32",
    boundary_each_end_relative_length:"1/8",central_combined_relative_length:"3/8",
    each_central_relative_length:"3/16",
    exact_relative_central_intervals:[["5/32","11/32"],["21/32","27/32"]],
    length_scope:"Predeclared exact rational source definitions from the unchanged two-support seed; not evaluated floating-point carriers or an actual field.",
    actual_central_length_carrier_hex:null,actual_mean_branch:null,actual_point_sha256:null,
    actual_complete_posterior_mean_exists_in_this_delivery:null,
    runtime_uses_whole_actual_report_seed_definition:true,
    fixed_mathematical_metric_changed:false,
    old_seed_or_field_or_root_or_fee_identity_inherited:false,
    no_new_R722_mathematical_branch_implemented_in_this_parameter_adapter:true
  };
}
function buildReady(kind,parent,parentRecord,meshParent,scienceRecords,reproducerPath) {
  const out=clone(parent);
  const oldSteps=clone(parent.steps);
  out.steps=oldSteps.map(currentStep);
  const correspondence=oldSteps.map((x,i)=>checkStep(x,out.steps[i]));
  out.executed=false;
  if(Object.prototype.hasOwnProperty.call(out,"admitted"))out.admitted=false;
  out.complete_immediate_parameter_parent=clone(parentRecord);
  out.complete_parameter_adapter={
    kind,source_only_parameter_construction:true,runtime_sources_changed:false,
    exact_runtime_reuse:true,source_reproducer_is_not_a_scientific_admission_gate:true,
    parent_namespace:OLD_NS,current_namespace:NEW_NS,
    parent_complete_metadata_kept_as_historical:true,
    original_complete_parent_ready:clone(parentRecord),
    every_unmodified_parent_top_level_field_preserved:true,
    all_current_unknown_physical_identities_null:true,
    original_step_correspondence:correspondence,
    whole_parent_metadata_is_not_a_current_execution_return:true,
    parameter_reproducer_path:reproducerPath
  };
  out.current_scientific_parameter_binding=plannedScience(meshParent,scienceRecords);
  out.planned_seed_parameters=plannedSeed(parent.planned_seed_parameters);
  out.actual_current_scientific_run=null;
  out.actual_current_complete_reference_inputs=null;
  out.actual_current_input_binding_sha256=null;
  out.actual_current_model_identity_sha256=null;
  out.actual_current_point_sha256=null;
  out.actual_current_snapshot_identity_sha256=null;
  out.actual_current_final_checkpoint_sha256=null;
  out.current_conditional_postprocessing_status="prepared only; no new scientific field, fee, mesh, outward tube, moment, refinement or delta_E returned";
  if(kind==="R716") {
    out.schema="prepared-fixed-fejer-meridian-bhalf-first-R722-complete-R716-closed-flux-centred-moments-v1";
    out.historical_parent_actual_input_evidence=clone(parent.actual_input_evidence);
    out.actual_input_evidence=null;
    out.historical_parent_latest_actual_scientific_boundary=clone(parent.latest_actual_scientific_boundary);
    out.latest_actual_scientific_boundary=null;
    out.historical_parent_complete_parameter_correspondence=clone(parent.complete_parameter_correspondence);
    out.complete_parameter_correspondence=correspondence;
    out.historical_parent_actual_source_specification=parent.actual_source_specification;
    out.actual_source_specification="Reuse the unchanged complete producer-bound source family driver10fa/reader8027/normal76185/packetc750, all137 scientific source roles and18 runtime files. This plan consumes only the genuine bhalf-first field and its own immutable point/fee inputs, never the original run18 input records or mutable observations. All R722 whole-cell validation, twelve moments, full cover and exact final closed-main evidence rules remain unchanged. New run, reference report, working model, point, packet, root, flux and delta_E values are unknown until actual Actions output.";
    out.input_report=namespaced(parent.input_report);
    out.complete_closed_phase_main_report=namespaced(parent.complete_closed_phase_main_report);
    out.new_consumer_arguments=namespaced(parent.new_consumer_arguments);
    out.complete_closed_source_binding=namespaced(parent.complete_closed_source_binding);
    out.historical_run18_unknown_fields={};
    for(const k of Object.keys(parent))if(k.startsWith("current_run18_")){
      out.historical_run18_unknown_fields[k]=clone(parent[k]);
      delete out[k];out[k.replace("current_run18_","current_run19_")]=null;
    }
    out.original_solver_parameters_changed=true;
    out.only_explicit_initial_seed_width_changed=true;
    out.historical_parent_R722_branch_declaration={
      new_R722_mean_branch_added:parent.new_R722_mean_branch_added,
      new_R722_mean_branch_explicit_complete_source_and_theorem_bound:parent.new_R722_mean_branch_explicit_complete_source_and_theorem_bound
    };
    out.new_R722_mean_branch_added=false;
    delete out.new_R722_mean_branch_explicit_complete_source_and_theorem_bound;
    out.existing_R722_mean_branch_explicit_complete_source_and_theorem_bound=true;
    out.solver_numerical_budget_changed=false;
    out.R716_numerical_parameters_changed=false;
    out.current_reference_tail_leaves=null;
    out.complete_closed_source_manifest=parent.complete_closed_source_manifest;
  } else {
    out.schema="complete-fixed-fejer-meridian-bhalf-first-same-field-closed-phase-mesh-parameters-v1";
    out.historical_parent_actual_original_scientific_run=parent.actual_original_scientific_run;
    out.actual_original_scientific_run=null;
    out.historical_parent_completed_reference_input_evidence=clone(parent.actual_completed_reference_input_evidence);
    out.actual_completed_reference_input_evidence=null;
    out.actual_current_scalar_table_leaf_count=null;
    out.configured_complete_reference_tail_leaf_count=2218;
    out.optional_complete_closed_phase_evidence=namespaced(parent.optional_complete_closed_phase_evidence);
    out.historical_parent_scope=parent.scope;
    out.scope=(kind==="mesh_final"
      ?"Consume only the genuine complete bhalf-first scientific report and its full thirteen-member final checkpoint; no initial/progress/other-run substitute."
      :"Consume only a genuine complete required-angle immutable bhalf-first point snapshot from captured scientific report bytes; a trial point is not an accepted or final point.")
      +" Reuse every unchanged runtime source and all137 actual scientific roles. Parse the complete actual new launcher command, rebuild every original parameter, and compare the full model, fixed reference, point and all source/input bytes. Preserve all original mesh/time levels, caps, H, frequencies, budgets and selector mappings.";
    out.point_source_mode=parent.point_source_mode;
    out.source_or_parameter_provenance_field_scope="complete_original_scientific_parameter_source, complete_source_derivation and original_failed_entry_and_method_repair retain original parent provenance. Current bhalf-first parameters and required report/command paths are in current_scientific_parameter_binding and the complete steps.";
  }
  return out;
}


function digest(bytes) {
  return crypto.createHash("sha256").update(bytes).digest("hex");
}
function topicPath(relative) {
  return relative.startsWith("topics/") ? relative : TOPIC + "/" + relative;
}
function readWhole(repo, record) {
  const filename=path.resolve(repo,topicPath(record.path));
  const stat=fs.statSync(filename);
  if(!stat.isFile()||stat.size!==record.bytes||stat.size>=100000)
    throw new Error("Complete metadata source size mismatch: "+record.path);
  const bytes=fs.readFileSync(filename);
  if(digest(bytes)!==record.sha256)
    throw new Error("Complete metadata source SHA mismatch: "+record.path);
  return JSON.parse(bytes.toString("utf8"));
}
function argumentsOf(argv) {
  const result={};
  for(let i=0;i<argv.length;i+=2) {
    if(!["--repo","--output-directory"].includes(argv[i])||i+1>=argv.length||result[argv[i]]!==undefined)
      throw new Error("Usage: node "+REPRODUCER_PATH+" --repo REPO --output-directory FRESH_DIRECTORY");
    result[argv[i]]=argv[i+1];
  }
  if(!result["--repo"]||!result["--output-directory"])
    throw new Error("Both --repo and --output-directory are required.");
  return {repo:path.resolve(result["--repo"]),outdir:path.resolve(result["--output-directory"])};
}
function main() {
  const {repo,outdir}=argumentsOf(process.argv.slice(2));
  const parents=PARENTS.map(r=>readWhole(repo,r.parent));
  const science=SCIENTIFIC_PARAMETERS.map(r=>readWhole(repo,r));
  const meshParent=parents[PARENTS.findIndex(r=>r.kind==="mesh_final")];
  const sciencePlan=plannedScience(meshParent,SCIENTIFIC_PARAMETERS);
  const realScience=science[0].steps[0];
  if(JSON.stringify(sciencePlan.current_complete_scientific_argv)!==JSON.stringify(realScience.args)||
     sciencePlan.current_complete_scientific_script!==realScience.script||
     science[0].steps.length!==1||science[1].steps.length!==1||
     science[1].steps[0].args.length!==7)
    throw new Error("Whole current scientific/pure parameter source disagreement.");
  const constructed=PARENTS.map((spec,i)=>{
    const parentRecord={...spec.parent,fixed_publication_commit:spec.publication};
    const value=buildReady(spec.kind,parents[i],parentRecord,meshParent,SCIENTIFIC_PARAMETERS,REPRODUCER_PATH);
    const text=JSON.stringify(value,null,2)+"\n";
    const bytes=Buffer.from(text,"utf8");
    const expected=OUTPUTS.find(x=>x.kind===spec.kind);
    if(bytes.length!==expected.bytes||digest(bytes)!==expected.sha256||bytes.length>=100000)
      throw new Error("Complete output identity mismatch: "+expected.path);
    return {expected,value,text,bytes};
  });
  fs.mkdirSync(outdir,{recursive:true});
  const records=[];
  for(const item of constructed) {
    const destination=path.join(outdir,item.expected.name);
    if(fs.existsSync(destination)) {
      const bytes=fs.readFileSync(destination);
      if(bytes.length!==item.bytes.length||digest(bytes)!==item.expected.sha256)
        throw new Error("Refuse to replace a different existing file: "+destination);
    } else fs.writeFileSync(destination,item.text,{encoding:"utf8",flag:"wx"});
    records.push({...item.expected,actual_output:destination,
      complete_steps:item.value.steps.map(s=>({id:s.id,...counts(s)}))});
  }
  process.stdout.write(JSON.stringify({
    schema:"complete-fixed-fejer-bhalf-moment-mesh-parameter-source-construction-v1",
    complete_parameter_construction:true,
    scientific_execution_performed:false,
    field_or_fee_or_mesh_result_created:false,
    refs_queues_or_running_jobs_modified:false,
    runtime_source_changes:0,
    whole_current_scientific_argument_words:157,
    only_current_scientific_argument_differences:sciencePlan.original_complete_argv_difference,
    records
  },null,2)+"\n");
}
main();
