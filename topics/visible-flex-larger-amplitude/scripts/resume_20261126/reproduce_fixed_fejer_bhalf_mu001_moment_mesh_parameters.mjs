#!/usr/bin/env node
/**
 * Complete run19 -> run20 R716 / final-mesh / packet-mesh parameter construction.
 * Metadata only: no scientific imports, field/root/jet/mesh calls, source
 * compilation, fixtures, dispatch, review prerequisites or ref mutations.
 * Every original numerical postprocessing word and selector is retained.
 */
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
const TOPIC="topics/visible-flex-larger-amplitude";
const PARENTS=[
  {
    "role": "R716",
    "name": "fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
    "path": "computations/fixed-fejer-meridian-batched-bhalf-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
    "bytes": 80089,
    "sha256": "3b49bd1b12b6b5680fd63a6cd8a5e8c34633626c875044a50ba98b6b1174441a",
    "git_blob_sha": "7d748fcb2ca892ce50c23d0153c198f99fc307db",
    "fixed_publication_commit": "2e093617aafb8738bb575f90fa2b84a7c5064e95"
  },
  {
    "role": "mesh_final",
    "name": "fixed-fejer-meridian-batched-bhalf-first-same-field-phase-mesh-final-ready.json",
    "path": "computations/fixed-fejer-meridian-batched-bhalf-first-same-field-phase-mesh-final-ready.json",
    "bytes": 91284,
    "sha256": "04456c30ae931cb8d10e2652c8ef51fcd5e6ad5bfe4141e129b7fb98a04bf9c9",
    "git_blob_sha": "aafad01042d2a1412d070c2e302d762b3d0244c8",
    "fixed_publication_commit": "2e093617aafb8738bb575f90fa2b84a7c5064e95"
  },
  {
    "role": "mesh_packet",
    "name": "fixed-fejer-meridian-batched-bhalf-first-same-field-phase-mesh-packet-ready.json",
    "path": "computations/fixed-fejer-meridian-batched-bhalf-first-same-field-phase-mesh-packet-ready.json",
    "bytes": 91233,
    "sha256": "eeb88aede82e6d447472c22d884a91a1dec044d4078b15503e25c956e11ba2f4",
    "git_blob_sha": "bb953c7250373eea6e263e19533282136622d5e3",
    "fixed_publication_commit": "2e093617aafb8738bb575f90fa2b84a7c5064e95"
  }
];
const SCIENTIFIC_PARAMETERS=[
  {
    "role": "current_complete_science_parameters",
    "path": "computations/fixed-fejer-meridian-bhalf-mu001-science-complete-ready.json",
    "bytes": 97019,
    "sha256": "89b437a4986b3172d281b4928353072d15a15f2cebbb7a1fd8d973880d5166ca",
    "git_blob_sha": "598b4cdf62021a66b54c22b71171722027f1c0b5"
  },
  {
    "role": "current_complete_pure_parameters",
    "path": "computations/fixed-fejer-meridian-bhalf-mu001-pure-complete-ready.json",
    "bytes": 86221,
    "sha256": "f627447f7887bdc9d7f257b4d0772173556683501cd5fa9f1e39890ec7ac7f64",
    "git_blob_sha": "53655fce8344040770e02295898a1c4ae9a06ebf"
  }
];
const EXPECTED_OUTPUTS=[
  {
    "role": "R716",
    "name": "fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
    "path": "computations/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-R716-closed-flux-centred-moments-ready.json",
    "sha256": "acdff6053f81e252bc82a83b5cdd082d24fb888b03e91905fc3ae6c7d7219e48",
    "bytes": 89824,
    "git_blob_sha": "e8df07d79e268650ad82ce1bd586d34fa681490e"
  },
  {
    "role": "mesh_final",
    "name": "fixed-fejer-meridian-batched-bhalf-mu001-first-same-field-phase-mesh-final-ready.json",
    "path": "computations/fixed-fejer-meridian-batched-bhalf-mu001-first-same-field-phase-mesh-final-ready.json",
    "sha256": "c971d63d5e1746c60d81d50b40a2e9466019f86b3845c9fec97eeb26b1fa3082",
    "bytes": 94765,
    "git_blob_sha": "3369098b1ad17d7bff86de1ef4bc3b525b204d69"
  },
  {
    "role": "mesh_packet",
    "name": "fixed-fejer-meridian-batched-bhalf-mu001-first-same-field-phase-mesh-packet-ready.json",
    "path": "computations/fixed-fejer-meridian-batched-bhalf-mu001-first-same-field-phase-mesh-packet-ready.json",
    "sha256": "09907572a05e0655da1c9bffb54346baaac73c72ea726604e6a407588f0216db",
    "bytes": 94753,
    "git_blob_sha": "e7ecb98b257b54544b2f41228a95920a56036526"
  }
];
const REPRODUCER_PATH="scripts/resume_20261126/reproduce_fixed_fejer_bhalf_mu001_moment_mesh_parameters.mjs";

function clone(x) { return JSON.parse(JSON.stringify(x)); }
const OLD_NS="fixed-fejer-meridian-batched-bhalf-first";
const NEW_NS="fixed-fejer-meridian-batched-bhalf-mu001-first";
function mapped(x) {
 if(typeof x==="string") return x.split(OLD_NS).join(NEW_NS);
 if(Array.isArray(x)) return x.map(mapped);
 if(x&&typeof x==="object") return Object.fromEntries(Object.entries(x).map(([k,v])=>[mapped(k),mapped(v)]));
 return x;
}
function stepCount(s) {
 return {argument_words:s.args.length,formal_summary_fields:Object.values(s.summary||{}).reduce((n,v)=>n+Object.keys(v).length,0),live_fields:Object.values(s.progress_summary||{}).reduce((n,v)=>n+Object.keys(v).length,0),output_count:s.outputs.length};
}
function currentStep(parent) {
 const out=mapped(parent);
 if(typeof out.scope==="string") out.scope=out.scope.split("bhalf-first").join("bhalf-mu001-first");
 return out;
}
function parameterProjection(parent,science,pure,scienceRecords) {
 const p=parent.current_scientific_parameter_binding;
 const oldArgs=p.current_complete_scientific_argv;
 const step=science.steps[0];
 if(oldArgs.length!==157||step.args.length!==157||pure.steps[0].args.length!==7)throw Error("Complete scientific argv counts");
 if(p.current_complete_scientific_script!==step.script)throw Error("Runtime must be unchanged");
 const expected=oldArgs.map(x=>typeof x==="string"?x.split(OLD_NS).join(NEW_NS):x);
 const index=expected.indexOf("--restoration-damping");
 if(index<0||expected[index+1]!==".01")throw Error("Actual complete parent damping");
 expected[index+1]=".001";
 if(JSON.stringify(expected)!==JSON.stringify(step.args))throw Error("Unlisted complete scientific parameter change");
 const value=clone(p);
 value.intended_runner_label="parallel20";
 value.complete_current_scientific_parameter_files=clone(scienceRecords);
 value.complete_parent_scientific_parameter_file=clone(p.complete_current_scientific_parameter_files[0]);
 value.current_complete_scientific_script=step.script;
 value.current_complete_scientific_argv=clone(step.args);
 value.original_complete_argv_difference=step.args.map((x,i)=>x===oldArgs[i]?null:{index:i,before:oldArgs[i],after:x}).filter(Boolean);
 value.actual_required_scientific_report="{work}/"+NEW_NS+"/report.json";
 value.actual_required_original_command="{work}/"+NEW_NS+"-command.json";
 value.current_fields_not_inherited_from_parent_run18=true;
 value.current_fields_not_inherited_from_parent_run19=true;
 value.selected_initial_restoration_damping="0.001";
 value.selected_metric_damping="0.01";
 value.same_bhalf_initial_seed_and_all_numerical_budgets_as_complete_parent=true;
 value.unchanged_solver_controls_rows_stages_budgets_and_stopping_rules=false;
 value.only_initial_restoration_damping_differs_from_immediate_parent=true;
 value.all_other_solver_controls_rows_stages_budgets_and_stopping_rules_unchanged=true;
 for(const k of ["actual_run_id","actual_run_attempt","actual_source_commit","actual_input_files","actual_input_binding_sha256","actual_report_sha256","actual_model_identity_sha256","actual_point_sha256","actual_snapshot_identity_sha256","actual_final_checkpoint_sha256"])value[k]=null;
 return value;
}
function buildPost(kind,parent,parentRecord,science,pure,scienceRecords,reproducerPath) {
 const out=clone(parent),history={};
 function put(k,v) {
  if(Object.prototype.hasOwnProperty.call(parent,k)&&k!=="steps")history[k]=clone(parent[k]);
  out[k]=clone(v);
 }
 const steps=parent.steps.map(currentStep);
 const correspondence=steps.map((s,i)=>{
  const p=parent.steps[i],a=stepCount(p),b=stepCount(s);
  if(JSON.stringify(a)!==JSON.stringify(b)||p.script!==s.script||p.parent_bundle!==s.parent_bundle)throw Error("Changed postprocessing source, argument, domain or selector count");
  return {parent_step_id:p.id,current_step_id:s.id,counts:b,script_unchanged:s.script,exact_argument_differences:s.args.map((v,j)=>v===p.args[j]?null:{index:j,before:p.args[j],after:v}).filter(Boolean),only_namespace_step_id_and_scope_changed:true,all_formal_and_live_selector_values_retained:true};
 });
 put("steps",steps);
 put("schema",kind==="R716"?"prepared-fixed-fejer-meridian-bhalf-mu001-R722-complete-R716-closed-flux-centred-moments-v1":"complete-fixed-fejer-meridian-bhalf-mu001-same-field-closed-phase-mesh-parameters-v1");
 put("executed",false);
 if(Object.prototype.hasOwnProperty.call(parent,"admitted"))put("admitted",false);
 put("complete_immediate_parameter_parent",parentRecord);
 put("complete_parameter_adapter",{kind,source_only_parameter_construction:true,runtime_sources_changed:false,exact_runtime_reuse:true,source_reproducer_is_not_a_scientific_admission_gate:true,parent_namespace:OLD_NS,current_namespace:NEW_NS,parent_complete_metadata_kept_as_historical:true,original_complete_parent_ready:parentRecord,every_unmodified_parent_top_level_field_preserved:true,all_current_unknown_physical_identities_null:true,original_step_correspondence:correspondence,whole_parent_metadata_is_not_a_current_execution_return:true,parameter_reproducer_path:reproducerPath,only_postprocessing_namespace_changed:true,scientific_parent_damping_change:{"--restoration-damping":{"before":".01","after":".001"}}});
 put("current_scientific_parameter_binding",parameterProjection(parent,science,pure,scienceRecords));
 put("external_unregistered_peer_obligations",science.external_unregistered_peer_obligations);
 if(Object.prototype.hasOwnProperty.call(parent,"external_peer_status"))put("external_peer_status","All original obligations, including the separate run19 branch, remain. A terminal public workflow does not supply an empty typed history or a complete parent point.");
 put("planned_seed_parameters",{...clone(parent.planned_seed_parameters),same_seed_as_complete_run19_parameter_parent:true,initial_restoration_damping:"0.001",metric_damping:"0.01",initial_damping_scope:"Planned exact CLI parameters; actual command and report must be read. No convergence or larger accepted step is inferred."});
 for(const k of ["actual_current_scientific_run","actual_current_complete_reference_inputs","actual_current_input_binding_sha256","actual_current_model_identity_sha256","actual_current_point_sha256","actual_current_snapshot_identity_sha256","actual_current_final_checkpoint_sha256"])put(k,null);
 put("current_conditional_postprocessing_status","Prepared only for this independent bhalf-mu001 field. No complete report, checkpoint, required-angle packet, continuous fee, outward tube, moment, mesh refinement or delta_E has been supplied.");
 if(kind==="R716") {
  for(const k of ["input_report","complete_closed_phase_main_report","new_consumer_arguments","complete_closed_source_binding"])if(k in parent)put(k,mapped(parent[k]));
  put("complete_parameter_correspondence",correspondence);
  put("actual_source_specification","Use exactly the published producer-bound source family driver10fa/reader8027/normal76185/packetc750 and all137 scientific roles. Consume only the genuine bhalf-mu001 field, its own immutable complete-required-angle point and matching whole normal/closed reports. The full actual scientific command differs from run19 only in initial restoration damping .01 to .001 and output namespace. No parent19 field or numerical result is inherited; all R722, twelve-channel, full-cover and closed-main validation bodies remain unchanged.");
  put("only_explicit_initial_seed_width_changed",false);
  put("original_solver_parameters_changed",true);
  put("only_explicit_initial_restoration_damping_changed",true);
  put("solver_numerical_budget_changed",false);
  put("R716_numerical_parameters_changed",false);
  const previous={};
  for(const k of Object.keys(parent))if(k.startsWith("current_run19_")){previous[k]=clone(parent[k]);delete out[k];out[k.replace("current_run19_","current_run20_")]=null;}
  out.mu001_historical_run19_unknown_fields=previous;
 } else {
  put("scope",(kind==="mesh_final"?"Consume only the genuine complete bhalf-mu001 scientific report and its full thirteen-member final checkpoint; no initial/progress/other-run substitute.":"Consume only a genuine complete required-angle immutable bhalf-mu001 point snapshot from captured scientific report bytes; a trial point is not an accepted or final point.")+" Reuse every unchanged runtime source and all137 actual scientific roles. Parse the full actual current launcher command, including restoration damping .001, reconstruct all original parameters and free words, and bind the complete model, fixed reference, point and source/input bytes. All original mesh/time levels, caps, H, frequencies, budgets and selectors remain.");
  put("optional_complete_closed_phase_evidence",mapped(parent.optional_complete_closed_phase_evidence));
  put("source_or_parameter_provenance_field_scope","All complete original source and parent parameter records remain historical. Current run20 parameters, actual report/command paths and .001 restoration damping are in current_scientific_parameter_binding and the complete steps. Full overwritten run19 metadata is retained in mu001_parent_metadata; its actual unknown state is not converted to a new result.");
 }
 out.mu001_parent_metadata=history;
 out.mu001_parent_complete_steps={whole_parent_ready:clone(parentRecord),json_path:"steps",entire_original_steps_recoverable_from_whole_fixed_Git_file:true,inverse_namespace_from:NEW_NS,inverse_namespace_to:OLD_NS,scope_strings_are_also_in_the_complete_original_file:true,no_parent_argument_selector_cleanup_or_history_removed_from_its_source:true};
 out.mu001_same_runtime_no_new_mathematics_or_scientific_admission_gate=true;
 out.mu001_all_parent_history_and_actual_unknowns_preserved=true;
 return out;
}

function sha(bytes) { return crypto.createHash("sha256").update(bytes).digest("hex"); }
function topicPath(p) { return p.startsWith("topics/")?p:TOPIC+"/"+p; }
function readWhole(repo,record) {
 const file=path.resolve(repo,topicPath(record.path));
 const st=fs.statSync(file);
 if(!st.isFile()||st.size!==record.bytes||st.size>=100000)throw Error("Complete metadata size: "+record.path);
 const raw=fs.readFileSync(file);
 if(sha(raw)!==record.sha256)throw Error("Complete metadata SHA: "+record.path);
 return JSON.parse(raw.toString("utf8"));
}
function cli(args) {
 const out={};
 for(let i=0;i<args.length;i+=2) {
  if(!["--repo","--output-directory"].includes(args[i])||i+1>=args.length||args[i] in out)throw Error("Usage: --repo REPO --output-directory FRESH_DIRECTORY");
  out[args[i]]=args[i+1];
 }
 if(!out["--repo"]||!out["--output-directory"])throw Error("Both arguments are required");
 return {repo:path.resolve(out["--repo"]),outdir:path.resolve(out["--output-directory"])};
}
function main() {
 const {repo,outdir}=cli(process.argv.slice(2));
 const srec=SCIENTIFIC_PARAMETERS.find(x=>x.role==="current_complete_science_parameters");
 const prec=SCIENTIFIC_PARAMETERS.find(x=>x.role==="current_complete_pure_parameters");
 const science=readWhole(repo,srec),pure=readWhole(repo,prec);
 const artifacts=[];
 for(const parentRecord of PARENTS) {
  const parent=readWhole(repo,parentRecord),kind=parentRecord.role;
  const value=buildPost(kind,parent,parentRecord,science,pure,SCIENTIFIC_PARAMETERS,REPRODUCER_PATH);
  const text=JSON.stringify(value)+"\n";
  const bytes=Buffer.from(text,"utf8"),expected=EXPECTED_OUTPUTS.find(r=>r.role===kind);
  if(!expected||bytes.length!==expected.bytes||bytes.length>=100000||sha(bytes)!==expected.sha256)throw Error("Complete constructed metadata mismatch: "+kind);
  artifacts.push({expected,text,bytes});
 }
 fs.mkdirSync(outdir,{recursive:true});
 const results=[];
 for(const a of artifacts) {
  const dest=path.join(outdir,a.expected.name);
  if(fs.existsSync(dest)) {
   const b=fs.readFileSync(dest);
   if(b.length!==a.bytes.length||sha(b)!==a.expected.sha256)throw Error("Refuse different existing metadata: "+dest);
  } else fs.writeFileSync(dest,a.text,{encoding:"utf8",flag:"wx"});
  results.push({...a.expected,actual_output:dest});
 }
 process.stdout.write(JSON.stringify({
  schema:"complete-bhalf-mu001-moment-mesh-parameter-construction-v1",
  complete:true,scientific_execution:false,runtime_source_rewritten:false,
  full_report_point_mesh_or_fee_result_created:false,
  optional_metadata_constructor_not_an_admission_condition:true,
  complete_parent_inputs_and_output_bytes_verified:true,outputs:results
 },null,2)+"\n");
}
main();
