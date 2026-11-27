#!/usr/bin/env node
// Whole published run19 -> independent bfiveeighths parameter construction.
// Only seed width1/2->5/8 and current runner namespace change; all runtime
// sources, scientific budgets, formal/live mappings and history remain.
// This is text/JSON construction only, not a scientific execution gate.
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
const TOPIC="topics/visible-flex-larger-amplitude";
const COMPLETE_PARENTS=[
  {
    "role": "science",
    "name": "fixed-fejer-meridian-bhalf-science-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-science-complete-ready.json",
    "bytes": 90652,
    "sha256": "242dd96148ddee96cf829433a4f399e2a2bc052671a92905722c8de8110f2c67",
    "git_blob_sha": "9c4c28ef3c5b189e094c65f51038fafeef48bc48",
    "fixed_publication_commit": "543cfdf281c9bcd0f9b13197721b003a275c5967"
  },
  {
    "role": "pure",
    "name": "fixed-fejer-meridian-bhalf-pure-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-pure-complete-ready.json",
    "bytes": 80254,
    "sha256": "8a5f9ff71bc598f77b25c36aeaad833f048dc6b4d218de2df44fda92709e73b7",
    "git_blob_sha": "202b6ca81c72c009c34c04094ef234db2e337328",
    "fixed_publication_commit": "543cfdf281c9bcd0f9b13197721b003a275c5967"
  },
  {
    "role": "display",
    "name": "fixed-fejer-meridian-bhalf-complete-display-correspondence.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-complete-display-correspondence.json",
    "bytes": 25057,
    "sha256": "cc564e5c273367242aae226913a0dd82ae5b88b3e166fbcbb8da68d6c04edb2d",
    "git_blob_sha": "fac08bdbafbefd0e599687e2b7f0a5c6e71382e7",
    "fixed_publication_commit": "543cfdf281c9bcd0f9b13197721b003a275c5967"
  }
];
const CHOICE_NOTE={
  "name": "2026-11-27-supported-seed-five-eighths-three-quarters-and-existing-geometry-observations.md",
  "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-supported-seed-five-eighths-three-quarters-and-existing-geometry-observations.md",
  "sha256": "26b8f9ccce6f208f8ac5e09f13a12a543d6be5b258ad061efb8ed11ddcb5950f",
  "bytes": 20086,
  "git_blob_sha": "18bd23b13cf2cee74fca29cf5b774cbd6adc16e1",
  "fixed_publication_commit": "a02b2766d2ec89852a4ac8f584b3f5fe772426f5"
};
const ADDITIONAL_KNOWN_PEERS=[
  {
    "run_id": "46076669320",
    "run_attempt": 1,
    "run_attempt_key": "46076669320/1",
    "official_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/46076669320",
    "official_workflow_path": ".github/workflows/visible-larger-20261127-parallel19.yml",
    "official_head_sha": "543cfdf281c9bcd0f9b13197721b003a275c5967",
    "official_run_started_at": "2026-11-27T22:26:37Z",
    "official_status_at_read": "in_progress",
    "official_conclusion_at_read": null,
    "official_updated_at": "2026-11-27T22:26:40Z",
    "observed_utc": "2026-11-27 23:21:13 UTC",
    "declared_driver_source_sha256": "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f",
    "complete_scientific_parameter_record": {
      "name": "fixed-fejer-meridian-bhalf-science-complete-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-science-complete-ready.json",
      "bytes": 90652,
      "sha256": "242dd96148ddee96cf829433a4f399e2a2bc052671a92905722c8de8110f2c67",
      "git_blob_sha": "9c4c28ef3c5b189e094c65f51038fafeef48bc48",
      "fixed_publication_commit": "543cfdf281c9bcd0f9b13197721b003a275c5967"
    },
    "actual_scientific_final_report_sha256": null,
    "actual_final_checkpoint_sha256": null,
    "complete_typed_or_accepted_history_available": false,
    "unknown_history_is_not_empty": true,
    "not_a_new_typed_transfer_input": true
  },
  {
    "run_id": "46079535427",
    "run_attempt": 1,
    "run_attempt_key": "46079535427/1",
    "official_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/46079535427",
    "official_workflow_path": ".github/workflows/visible-larger-20261127-parallel20.yml",
    "official_head_sha": "85cd235221ace28158625a7ced52a24551b509eb",
    "official_run_started_at": "2026-11-27T22:55:41Z",
    "official_status_at_read": "in_progress",
    "official_conclusion_at_read": null,
    "official_updated_at": "2026-11-27T22:55:44Z",
    "observed_utc": "2026-11-27 23:21:13 UTC",
    "declared_driver_source_sha256": "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f",
    "complete_scientific_parameter_record": {
      "name": "fixed-fejer-meridian-bhalf-mu001-science-complete-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-mu001-science-complete-ready.json",
      "sha256": "89b437a4986b3172d281b4928353072d15a15f2cebbb7a1fd8d973880d5166ca",
      "bytes": 97019,
      "git_blob_sha": "598b4cdf62021a66b54c22b71171722027f1c0b5",
      "fixed_publication_commit": "85cd235221ace28158625a7ced52a24551b509eb"
    },
    "actual_scientific_final_report_sha256": null,
    "actual_final_checkpoint_sha256": null,
    "complete_typed_or_accepted_history_available": false,
    "unknown_history_is_not_empty": true,
    "not_a_new_typed_transfer_input": true
  }
];
const EXPECTED_OUTPUTS=[
  {
    "role": "display",
    "name": "fixed-fejer-meridian-bfiveeighths-complete-display-correspondence.json",
    "path": "computations/fixed-fejer-meridian-bfiveeighths-complete-display-correspondence.json",
    "sha256": "ef7739227cd03e9a09329d32d144f8fd57235105c02ba470ce6da5ba51619040",
    "bytes": 29575,
    "git_blob_sha": "5a183254da8fcd3d5c523bd6d767440712ef1d61"
  },
  {
    "role": "science",
    "name": "fixed-fejer-meridian-bfiveeighths-science-complete-ready.json",
    "path": "computations/fixed-fejer-meridian-bfiveeighths-science-complete-ready.json",
    "sha256": "6838b79823f398d930982b2d10fd28baf5a6a2f60eb866403331bfd34eb67d9d",
    "bytes": 97307,
    "git_blob_sha": "6da95445b088f8593ff0f5fb14d76167b26a7a21"
  },
  {
    "role": "pure",
    "name": "fixed-fejer-meridian-bfiveeighths-pure-complete-ready.json",
    "path": "computations/fixed-fejer-meridian-bfiveeighths-pure-complete-ready.json",
    "sha256": "b750fd865256366a5fcf6b020570a74c053ad853d4b34d0ff983ad3895388822",
    "bytes": 86702,
    "git_blob_sha": "5b2b58e75572b75ce499c8983adf3ba20278211b"
  }
];

const PREVIOUS_NAMESPACE="fixed-fejer-meridian-batched-bhalf-first";
const CURRENT_NAMESPACE="fixed-fejer-meridian-batched-bfiveeighths-first";
const PARAMETER_CONSTRUCTOR_PATH="topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_bfiveeighths_complete_parameters.mjs";
const DISPLAY_PATH="topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bfiveeighths-complete-display-correspondence.json";
const READY_PATHS=["topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bfiveeighths-science-complete-ready.json","topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bfiveeighths-pure-complete-ready.json"];
function copy(v){return JSON.parse(JSON.stringify(v));}
function currentNamespace(v){
 if(typeof v==="string")return v.split(PREVIOUS_NAMESPACE).join(CURRENT_NAMESPACE);
 if(Array.isArray(v))return v.map(currentNamespace);
 if(v&&typeof v==="object")return Object.fromEntries(Object.entries(v).map(([k,x])=>[currentNamespace(k),currentNamespace(x)]));
 return v;
}
function counts(s){return {argv_words:s.args.length,formal_fields:Object.values(s.summary||{}).reduce((n,x)=>n+Object.keys(x).length,0),live_fields:Object.values(s.progress_summary||{}).reduce((n,x)=>n+Object.keys(x).length,0)};}
function requireFlag(args,name,expected){
 const indices=args.map((v,i)=>v===name?i:-1).filter(i=>i>=0);
 if(indices.length!==1||args[indices[0]+1]!==expected)throw Error("Complete original argument mismatch: "+name);
 return indices[0];
}
function requireOriginalScience(s){
 if(s.args.length!==157)throw Error("Keep all original157 scientific argument words");
 for(const [name,value]of [["--seed-boundary-total-length","1/2"],["--seed-profile-delta","1/32"],["--restoration-damping",".01"],["--damping",".01"],["--directions","1"],["--maxiter","16"],["--restoration-directions","4"],["--restoration-maxiter","64"],["--line-trials","15"],["--normal-stages","32"],["--angles","2048"],["--active-rows","192"],["--seed-mean-maxiter","128"],["--seed-scalar-iterations","64"]])requireFlag(s.args,name,value);
 if(s.args.filter(v=>v==="--independent-envelope-branch").length!==1||s.args.includes("--restart-checkpoint")||s.args.includes("--restart-report"))throw Error("Keep the actual independent fresh mode");
 if(s.args.filter(v=>v==="--pending-parallel-envelope-run").length!==5||s.args.filter(v=>v==="--pending-parallel-envelope-source").length!==5)throw Error("Keep all five original supported peer CLI pairs");
 const c=counts(s);
 if(c.formal_fields!==458||c.live_fields!==48)throw Error("Keep all458 formal and48 live mappings");
}
function buildDisplay(parent,parentRecord){
 const v=copy(parent);
 v.schema="complete-fixed-fejer-meridian-bfiveeighths-progress-display-correspondence-v1";
 v.current_live_mapping=currentNamespace(parent.current_live_mapping);
 v.current_parameter_scope={boundary_total_length:"5/8",profile_delta:"1/32",initial_metric_damping:".01",initial_restoration_damping:".01",actual_run_id:null,actual_field_point_sha256:null,all48_current_scalar_selectors_preserved:true,all_historical_mapping_records_retained:true,only_current_runner_output_namespace_changed_in_display:true,new_observer_or_scientific_evaluation_added:false};
 v.bfiveeighths_complete_parent_display=copy(parentRecord);
 v.bfiveeighths_parent_current_metadata_recovery={complete_parent_file:copy(parentRecord),exact_parent_JSON_keys:["schema","current_live_mapping","current_parameter_scope"],all_parent_nested_history_objects_retained_verbatim:true,full_old_current_mapping_remains_in_the_exact_pinned_parent_file:true};
 if(Object.values(v.current_live_mapping).reduce((n,x)=>n+Object.keys(x).length,0)!==48)throw Error("Do not remove any original live selector");
 return v;
}
function buildReady(parent,kind,parentRecord,displayRecord,choiceRecord,additionalPeers){
 if(!Array.isArray(parent.steps)||parent.steps.length!==1)throw Error("Use the complete single published parent step");
 const value=copy(parent),original=copy(parent.steps[0]),step=currentNamespace(original);
 if(kind==="science"){
  requireOriginalScience(original);
  step.args[requireFlag(original.args,"--seed-boundary-total-length","1/2")+1]="5/8";
 }else if(kind!=="pure"||original.args.length!==7||counts(original).formal_fields!==445)throw Error("Keep the original full pure7/445");
 const changes=step.args.map((v,i)=>v===original.args[i]?null:{index:i,before:original.args[i],after:v}).filter(Boolean);
 if(kind==="science"){
  const i=original.args.indexOf("--seed-boundary-total-length")+1;
  if(changes.length!==2||step.args[i]!=="5/8"||changes.find(x=>x.index===i)?.before!=="1/2")throw Error("Only seed width and output namespace may change");
  for(const f of ["--damping","--restoration-damping"])requireFlag(step.args,f,".01");
 }else if(JSON.stringify(step.args)!==JSON.stringify(currentNamespace(original.args)))throw Error("Only the complete pure report/readout namespace changes");
 if(JSON.stringify(counts(step))!==JSON.stringify(counts(original)))throw Error("Do not shorten any complete step");
 step.scope=kind==="science"
  ?"Complete independent same-fixed-g M160/J923/N2048,32-stage solve with supported seed boundary total length b/S=5/8 and profile delta1/32. Relative to the complete run19 bhalf parameter parent, only seed width1/2->5/8 changes numerically; metric and restoration damping remain .01. Every original variable, source, root/metric/restoration/QP/line-search budget, complete geometry domain, true acceptance rule and all declared or unknown peer responsibilities remain. Its two complete fixed-reference inputs must be produced in this new runner. No earlier field, accepted state, root, typed list or final is fabricated as its input."
  :"Complete original stdlib reader of the actual bfiveeighths report, all137 scientific roles, complete model/point/packet/history/geometry bindings, and all445 original scalar selectors. No F/J/root or numerical acceptance call is added. Missing or partial scientific data remain missing or partial.";
 const changed=[];
 function set(k,v){if(Object.hasOwn(parent,k))changed.push(k);value[k]=v;}
 set("schema","complete-fixed-fejer-meridian-bfiveeighths-"+kind+"-parameters-v1");
 set("scope","Independent width-only input selection from the complete run19 b/S=1/2 parent. Set b/S=5/8; keep profile delta1/32, metric damping .01, restoration damping .01, all original variables, equations, domains, algorithms, budgets and true acceptance rules. Explicit boundary-slope and central-length tradeoffs are not an actual geometry/root/mean improvement guarantee. All historical sources, full parameters and unknown peer obligations remain.");
 set("complete_current_display_correspondence",copy(displayRecord));
 set("complete_parameter_constructor_path",PARAMETER_CONSTRUCTOR_PATH);
 set("complete_sibling_ready_paths",copy(READY_PATHS));
 set("complete_parameter_parent",copy(parentRecord));
 set("complete_choice_note",copy(choiceRecord));
 set("only_scientific_numerical_argument_change_from_immediate_parent",{flag:"--seed-boundary-total-length",before:"1/2",after:"5/8",unchanged_profile_delta:"1/32",unchanged_metric_damping:".01",unchanged_restoration_damping:".01"});
 set("planned_seed_parameters",{relative_boundary_total_length:"5/8",profile_delta:"1/32",each_of_four_boundary_layers_relative_length:"5/32",combined_central_relative_length:"1/4",each_of_two_central_relative_length:"1/8",central_intervals_relative_to_S:[["3/16","5/16"],["11/16","13/16"]],input_domain_is_legal:true,definition_only_not_actual_floating_carriers:true,actual_mean_root_and_angular_jets_proved:false,metric_or_geometric_improvement_assumed:false});
 set("future_controller_admission_after_actual_natural_return_only",false);
 const peers=copy(parent.external_unregistered_peer_obligations||[]);
 for(const p of additionalPeers){const pair=[p.run_attempt_key,p.declared_driver_source_sha256];if(!peers.some(x=>JSON.stringify(x)===JSON.stringify(pair)))peers.push(pair);}
 set("external_unregistered_peer_obligations",peers);
 set("external_peer_status","All original five supported CLI pairs, six external run/source pairs and their complete historical metadata remain; the actually launched run19 and run20 are additionally kept as external unknown whole-history obligations. None of these additional peers is aliased into the old supported PARENT_FAMILIES or passed as a typed/final transfer input. Official termination or absent public records never means an empty scientific history. Their complete declared parameter files and known official launch identities are recorded separately.");
 set("serialization","Complete compact UTF-8 JSON plus trailing newline. Every current scientific argument and formal/live selector is retained; overwritten parent metadata is exactly recoverable at its original JSON keys in the whole fixed parent file.");
 value.steps=[step];
 value.executed=false;
 value.actual_run_id=null;value.actual_run_attempt=null;
 value.actual_report_sha256=null;value.actual_point_sha256=null;
 value.actual_model_identity_sha256=null;value.actual_geometry_or_acceptance_result=null;
 value.future_actual_reference_identity_sha256=null;value.future_actual_target_file_sha256=null;
 value.future_actual_model_identity_sha256=null;value.future_actual_final_checkpoint_sha256=null;
 value.intended_independent_runner_label="parallel21";
 value.independent_science_requires_only_its_own_two_complete_reference_inputs=true;
 value.prior_runner_natural_scientific_return_is_not_required=true;
 value.bfiveeighths_complete_parameter_delta={original_step_id:original.id,current_step_id:step.id,complete_changed_argument_words:changes,counts:counts(step),complete_original_parent_file:copy(parentRecord),original_current_step_fields_in_parent:"steps[0]",all_original_step_fields_unchanged_except_exact_width_word_current_namespace_and_scope:true,all_source_pairs_and_runtime_files_unchanged:true,all_original_numerical_budgets_and_tolerances_unchanged:true,original_five_supported_pending_CLI_pairs_preserved:true,complete_fixed_input_and_reference_CLI_do_not_have_a_seed_width_parameter:true,fixed_mathematical_target_recipe_unchanged:true,seed_model_and_physical_initial_field_change:true,new_mean_root_normal_branch_and_geometry_are_unknown:true,boundary_and_central_scale_comparison_is_not_nonlinear_improvement_guarantee:true};
 value.bfiveeighths_parent_current_metadata_recovery={complete_parent_file:copy(parentRecord),overwritten_current_metadata_JSON_keys:changed,all_original_top_level_keys_retained:true,all_historical_nested_objects_retained_verbatim:true,all_replaced_values_recoverable_at_identical_keys_in_pinned_complete_parent:true,no_scientific_argument_or_selector_replaced_by_a_reference:true};
 value.bfiveeighths_added_external_peer_records=copy(additionalPeers);
 value.actual_new_initial_damping_read_from_complete_report=null;
 return value;
}

function sha(bytes){return crypto.createHash("sha256").update(bytes).digest("hex");}
function sourcePath(repo,r){return path.resolve(repo,r.path.startsWith("topics/")?r.path:TOPIC+"/"+r.path);}
function readWhole(repo,r){
 const p=sourcePath(repo,r),stat=fs.statSync(p);
 if(!stat.isFile()||stat.size!==r.bytes||stat.size>=100000)throw Error("Complete parent size mismatch: "+r.path);
 const bytes=fs.readFileSync(p);
 if(sha(bytes)!==r.sha256)throw Error("Complete parent wholeSHA mismatch: "+r.path);
 return JSON.parse(bytes.toString("utf8"));
}
function parseArgs(args){
 const result={};
 for(let i=0;i<args.length;i+=2){
  if(!["--repo","--output-directory"].includes(args[i])||i+1>=args.length||Object.hasOwn(result,args[i]))throw Error("Use --repo REPO --output-directory OUTPUT_DIRECTORY");
  result[args[i]]=args[i+1];
 }
 if(!result["--repo"]||!result["--output-directory"])throw Error("Both arguments are required");
 return {repo:path.resolve(result["--repo"]),outdir:path.resolve(result["--output-directory"])};
}
function identity(role,value){
 const expected=EXPECTED_OUTPUTS.find(r=>r.role===role);
 const text=(role==="display"?JSON.stringify(value,null,2):JSON.stringify(value))+"\n",bytes=Buffer.from(text,"utf8");
 if(bytes.length>=100000||bytes.length!==expected.bytes||sha(bytes)!==expected.sha256)throw Error("Complete output identity differs: "+expected.path);
 return {expected,text,bytes,value};
}
function restoreOriginalStep(current,parent,kind){
 const backward=function(v){
  if(typeof v==="string")return v.split(CURRENT_NAMESPACE).join(PREVIOUS_NAMESPACE);
  if(Array.isArray(v))return v.map(backward);
  if(v&&typeof v==="object")return Object.fromEntries(Object.entries(v).map(([k,x])=>[backward(k),backward(x)]));
  return v;
 };
 const s=backward(current);
 if(kind==="science")s.args[requireFlag(s.args,"--seed-boundary-total-length","5/8")+1]="1/2";
 s.scope=parent.scope;
 if(JSON.stringify(s)!==JSON.stringify(parent))throw Error("Full step cannot be reversed to its exact original");
}
function main(){
 const {repo,outdir}=parseArgs(process.argv.slice(2));
 const dparent=COMPLETE_PARENTS.find(r=>r.role==="display");
 const d=readWhole(repo,dparent),dr={...dparent};delete dr.role;
 const displayValue=buildDisplay(d,dr);
 const display=identity("display",displayValue);
 const displayRecord={name:display.expected.name,path:TOPIC+"/"+display.expected.path,sha256:display.expected.sha256,bytes:display.expected.bytes,git_blob_sha:display.expected.git_blob_sha};
 const artifacts=[display];
 for(const kind of ["science","pure"]){
  const p=COMPLETE_PARENTS.find(r=>r.role===kind),original=readWhole(repo,p),pr={...p};delete pr.role;
  const value=buildReady(original,kind,pr,displayRecord,CHOICE_NOTE,ADDITIONAL_KNOWN_PEERS);
  restoreOriginalStep(value.steps[0],original.steps[0],kind);
  if(kind==="science"&&JSON.stringify(value.steps[0].progress_summary)!==JSON.stringify(displayValue.current_live_mapping))throw Error("Complete48 live mapping differs");
  artifacts.push(identity(kind,value));
 }
 fs.mkdirSync(outdir,{recursive:true});
 const records=[];
 for(const a of artifacts){
  const dest=path.join(outdir,a.expected.name);
  if(fs.existsSync(dest)){
   const actual=fs.readFileSync(dest);
   if(actual.length!==a.bytes.length||sha(actual)!==a.expected.sha256)throw Error("Refuse to replace different parameter bytes: "+dest);
  }else fs.writeFileSync(dest,a.bytes,{flag:"wx"});
  records.push({...a.expected,actual_output_path:dest});
 }
 process.stdout.write(JSON.stringify({schema:"complete-fixed-fejer-bfiveeighths-parameter-text-construction-v1",complete:true,scientific_execution:false,runtime_source_rewrite:false,new_field_or_root_or_fee_or_certificate_created:false,complete_parent_files_and_all_arguments_selectors_and_peer_history_preserved:true,optional_metadata_constructor_is_not_a_scientific_admission_gate:true,outputs:records},null,2)+"\n");
}
main();
