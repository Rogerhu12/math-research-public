#!/usr/bin/env node
// Complete run19 -> bhalf-mu001 metadata construction. No scientific imports,
// F/J/root calls, source compilation, fixtures, job dispatch or ref mutation.
// Original runtime sources and full scientific budgets remain unchanged.
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
const TOPIC="topics/visible-flex-larger-amplitude";
const SCIENTIFIC_PARENTS=[
  {
    "name": "fixed-fejer-meridian-bhalf-science-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-science-complete-ready.json",
    "bytes": 90652,
    "sha256": "242dd96148ddee96cf829433a4f399e2a2bc052671a92905722c8de8110f2c67",
    "git_blob_sha": "9c4c28ef3c5b189e094c65f51038fafeef48bc48",
    "published_source_commit": "543cfdf281c9bcd0f9b13197721b003a275c5967",
    "role": "science"
  },
  {
    "name": "fixed-fejer-meridian-bhalf-pure-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-pure-complete-ready.json",
    "bytes": 80254,
    "sha256": "8a5f9ff71bc598f77b25c36aeaad833f048dc6b4d218de2df44fda92709e73b7",
    "git_blob_sha": "202b6ca81c72c009c34c04094ef234db2e337328",
    "published_source_commit": "543cfdf281c9bcd0f9b13197721b003a275c5967",
    "role": "pure"
  }
];
const DISPLAY_PARENT={
  "name": "fixed-fejer-meridian-bhalf-complete-display-correspondence.json",
  "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-complete-display-correspondence.json",
  "bytes": 25057,
  "sha256": "cc564e5c273367242aae226913a0dd82ae5b88b3e166fbcbb8da68d6c04edb2d",
  "git_blob_sha": "fac08bdbafbefd0e599687e2b7f0a5c6e71382e7",
  "fixed_published_commit": "543cfdf281c9bcd0f9b13197721b003a275c5967"
};
const EXPECTED_OUTPUTS=[
  {
    "role": "display",
    "name": "fixed-fejer-meridian-bhalf-mu001-complete-display-correspondence.json",
    "path": "computations/fixed-fejer-meridian-bhalf-mu001-complete-display-correspondence.json",
    "bytes": 32429,
    "sha256": "1fef7603002bdfbac58623b1d7c8b1cd0492d050f42c22acfd1ce11c3597278e",
    "git_blob_sha": "c89b5f4796e3c98a692f2704da6679df29aa39df"
  },
  {
    "role": "science",
    "name": "fixed-fejer-meridian-bhalf-mu001-science-complete-ready.json",
    "path": "computations/fixed-fejer-meridian-bhalf-mu001-science-complete-ready.json",
    "bytes": 97019,
    "sha256": "89b437a4986b3172d281b4928353072d15a15f2cebbb7a1fd8d973880d5166ca",
    "git_blob_sha": "598b4cdf62021a66b54c22b71171722027f1c0b5"
  },
  {
    "role": "pure",
    "name": "fixed-fejer-meridian-bhalf-mu001-pure-complete-ready.json",
    "path": "computations/fixed-fejer-meridian-bhalf-mu001-pure-complete-ready.json",
    "bytes": 86221,
    "sha256": "f627447f7887bdc9d7f257b4d0772173556683501cd5fa9f1e39890ec7ac7f64",
    "git_blob_sha": "53655fce8344040770e02295898a1c4ae9a06ebf"
  }
];


const PREVIOUS_NAMESPACE="fixed-fejer-meridian-batched-bhalf-first";
const CURRENT_NAMESPACE="fixed-fejer-meridian-batched-bhalf-mu001-first";
const PARAMETER_CONSTRUCTOR_PATH="topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_bhalf_mu001_complete_parameters.mjs";
const DISPLAY_PATH="topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-mu001-complete-display-correspondence.json";
const READY_PATHS=["topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-mu001-science-complete-ready.json","topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-mu001-pure-complete-ready.json"];
function copy(v){return JSON.parse(JSON.stringify(v));}
function currentNamespace(v){
  if(typeof v==="string")return v.split(PREVIOUS_NAMESPACE).join(CURRENT_NAMESPACE);
  if(Array.isArray(v))return v.map(currentNamespace);
  if(v&&typeof v==="object")return Object.fromEntries(Object.entries(v).map(([k,x])=>[currentNamespace(k),currentNamespace(x)]));
  return v;
}
function countStep(s){
  return {argv_words:s.args.length,formal_fields:Object.values(s.summary||{}).reduce((a,x)=>a+Object.keys(x).length,0),live_fields:Object.values(s.progress_summary||{}).reduce((a,x)=>a+Object.keys(x).length,0)};
}
function expectedSeed(args){
  for(const [name,expected]of [["--seed-boundary-total-length","1/2"],["--seed-profile-delta","1/32"],["--restoration-damping",".01"],["--damping",".01"],["--restoration-maxiter","64"],["--restoration-directions","4"],["--line-trials","15"]]){
    const i=args.indexOf(name);
    if(i<0||args[i+1]!==expected)throw Error("Complete original parameter changed: "+name);
  }
}
function buildDisplay(parent,parentRecord){
  const result=copy(parent);
  result.mu001_complete_parent_display=copy(parentRecord);
  result.mu001_parent_schema=parent.schema;
  result.mu001_parent_current_live_mapping=copy(parent.current_live_mapping);
  result.mu001_parent_current_parameter_scope=copy(parent.current_parameter_scope);
  result.schema="complete-fixed-fejer-meridian-bhalf-mu001-progress-display-correspondence-v1";
  result.current_live_mapping=currentNamespace(parent.current_live_mapping);
  result.current_parameter_scope={
    boundary_total_length:"1/2",profile_delta:"1/32",initial_metric_damping:".01",
    initial_restoration_damping:".001",previous_restoration_damping:".01",
    actual_run_id:null,actual_field_point_sha256:null,
    all48_current_scalar_selectors_preserved:true,all_historical_mapping_records_retained:true,
    only_current_runner_output_namespace_changed_in_display:true,
    new_observer_or_scientific_evaluation_added:false
  };
  const count=Object.values(result.current_live_mapping).reduce((n,x)=>n+Object.keys(x).length,0);
  if(count!==48||JSON.stringify(result.current_live_mapping)!==JSON.stringify(currentNamespace(parent.current_live_mapping)))throw Error("Keep all48 live mappings");
  return result;
}
function buildReady(parent,kind,parentRecord,displayRecord){
  if(parent.steps.length!==1)throw Error("Use the complete single parent step");
  const value=copy(parent), original=copy(parent.steps[0]);
  const step=currentNamespace(original);
  if(kind==="science"){
    if(step.args.length!==157)throw Error("Keep all157 scientific argv words");
    expectedSeed(original.args);
    const i=step.args.indexOf("--restoration-damping");
    step.args[i+1]=".001";
  }else if(kind!=="pure"||step.args.length!==7)throw Error("Keep the complete pure7");
  const changes=step.args.map((v,i)=>v===original.args[i]?null:{index:i,before:original.args[i],after:v}).filter(Boolean);
  if(kind==="science"){
    const numerical=changes.filter(x=>original.args[x.index-1]==="--restoration-damping");
    if(changes.length!==2||numerical.length!==1||numerical[0].before!==".01"||numerical[0].after!==".001")throw Error("Only restoration damping and namespace may change");
  }else if(JSON.stringify(step.args)!==JSON.stringify(currentNamespace(original.args)))throw Error("Only pure output namespace may change");
  step.scope=(kind==="science"
    ?"Complete independent same-fixed-g M160/J923/N2048/32-stage science with b/S=1/2, delta=1/32 and initial restoration damping .001. The complete run19 parent differs only by restoration damping .01 and its output namespace. Metric damping remains .01. Every original free variable, root/QP/restoration/line-search budget, equation, row, domain, acceptance rule and all known or unknown peer obligations remain. This starts from the genuine new runner's two necessary reference inputs and original frozen-reference initial point, without inheriting run19's field or history."
    :"Complete original stdlib reader of the actual bhalf-mu001 scientific report and full source/model/point/geometry/packet bindings. The runtime source and all original selectors are unchanged; missing or partial scientific outputs remain missing or partial, and no F/J/root or scientific acceptance is added.");
  if(JSON.stringify(countStep(step))!==JSON.stringify(countStep(original)))throw Error("Lost complete parameter or selector count");
  const old={};
  function set(name,v){if(Object.hasOwn(parent,name))old[name]=copy(parent[name]);value[name]=v;}
  set("schema","complete-fixed-fejer-meridian-bhalf-mu001-"+kind+"-parameters-v1");
  set("scope","Single independent restoration-scale parameter branch of the complete run19 bhalf problem. Only --restoration-damping .01 -> .001 changes numerically; b/S=1/2, delta=1/32, metric damping .01, all original budgets, variables, rows, true acceptance rules and all peer history remain. The exact-QP comparison in the source note is not a finite-iteration or nonlinear guarantee.");
  set("complete_current_display_correspondence",copy(displayRecord));
  set("complete_parameter_constructor_path",PARAMETER_CONSTRUCTOR_PATH);
  set("complete_sibling_ready_paths",copy(READY_PATHS));
  set("complete_parameter_parent",copy(parentRecord));
  set("only_scientific_numerical_argument_change_from_immediate_parent",{flag:"--restoration-damping",before:".01",after:".001",unchanged_metric_damping:".01",unchanged_seed_boundary_total_length:"1/2",unchanged_seed_profile_delta:"1/32"});
  set("future_controller_admission_after_actual_natural_return_only",false);
  value.independent_science_requires_only_its_own_two_complete_reference_inputs=true;
  value.prior_runner_natural_scientific_return_is_not_required=true;
  const peers=copy(parent.external_unregistered_peer_obligations||[]);
  const newPair=["46076669320/1","10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f"];
  if(!peers.some(x=>JSON.stringify(x)===JSON.stringify(newPair)))peers.push(newPair);
  set("external_unregistered_peer_obligations",peers);
  set("external_peer_status",parent.external_peer_status+" The actual independent run19 is additionally retained as an external unknown whole history; no run19 returned/final/typed state is assumed or inserted into the unchanged original five supported CLI pairs.");
  set("serialization","Complete compact UTF-8 JSON with trailing newline; every field, full argv and selector preserved.");
  value.steps=[step];
  value.executed=false;
  value.actual_run_id=null;value.actual_run_attempt=null;
  value.actual_report_sha256=null;value.actual_point_sha256=null;
  value.actual_model_identity_sha256=null;value.actual_geometry_or_acceptance_result=null;
  value.mu001_parameter_parent_changed_metadata=old;
  value.mu001_complete_parameter_delta={
    numerical_parameter_change_only:true,original_step_id:original.id,current_step_id:step.id,
    original_scope:original.scope,current_scope:step.scope,
    complete_argv_location:"steps[0].args retains every current word; exact_changed_argv_words reverses it to every original parent word, also retained in the whole pinned parent file",
    exact_changed_argv_words:changes,counts:countStep(step),
    all_original_non_argument_step_fields_preserved_except_namespace_and_current_scope:true,
    no_runtime_source_or_algorithm_or_budget_change:true,
    original_common_slack_and_true_acceptance_rules_preserved:true,
    same_original_coordinate_norm_and_full_selected_rows:true,
    exact_QP_only_comparison_scope:"same entire feasible linear constraint set and exact global QP minimizers; nonnegative optimal tau does not increase as mu decreases",
    finite64_inner_step_or_full_nonlinear_improvement_guarantee:false,
    actual_cause_of_previous_small_progress_identified:false,
    actual_prior_step_alpha_QP_status_gradient_norm_or_true_model_ratio_not_invented:true
  };
  value.restoration_scale_choice_note_path="topics/visible-flex-larger-amplitude/notes/2026-11-27-full-restoration-scale-and-mu001-branch.md";
  value.intended_independent_runner_label="parallel20";
  value.actual_new_initial_damping_read_from_complete_report=null;
  return value;
}


function sha(bytes){return crypto.createHash("sha256").update(bytes).digest("hex");}
function resolveRecord(repo,r){return path.resolve(repo,r.path.startsWith("topics/")?r.path:TOPIC+"/"+r.path);}
function readWhole(repo,r){
  const p=resolveRecord(repo,r),stat=fs.statSync(p);
  if(!stat.isFile()||stat.size!==r.bytes||stat.size>=100000)throw Error("Complete parent size mismatch: "+r.path);
  const bytes=fs.readFileSync(p);
  if(sha(bytes)!==r.sha256)throw Error("Complete parent SHA mismatch: "+r.path);
  return JSON.parse(bytes.toString("utf8"));
}
function cli(args){
  const a={};
  for(let i=0;i<args.length;i+=2){
    if(!["--repo","--output-directory"].includes(args[i])||i+1>=args.length||a[args[i]]!==undefined)
      throw Error("Use --repo REPO --output-directory FRESH_DIRECTORY");
    a[args[i]]=args[i+1];
  }
  if(!a["--repo"]||!a["--output-directory"])throw Error("Both arguments are required");
  return {repo:path.resolve(a["--repo"]),outdir:path.resolve(a["--output-directory"])};
}
function makeArtifact(role,value){
  const expected=EXPECTED_OUTPUTS.find(r=>r.role===role);
  const text=(role==="display"?JSON.stringify(value,null,2):JSON.stringify(value))+"\n";
  const bytes=Buffer.from(text,"utf8");
  if(bytes.length!==expected.bytes||sha(bytes)!==expected.sha256||bytes.length>=100000)
    throw Error("Complete constructed parameter identity mismatch: "+expected.path);
  return {expected,text,value,bytes};
}
function main(){
  const {repo,outdir}=cli(process.argv.slice(2));
  const parentDisplay=readWhole(repo,DISPLAY_PARENT);
  const displayValue=buildDisplay(parentDisplay,DISPLAY_PARENT);
  const display=makeArtifact("display",displayValue);
  const d=display.expected;
  const displayRecord={name:d.name,path:TOPIC+"/"+d.path,bytes:d.bytes,sha256:d.sha256,git_blob_sha:d.git_blob_sha};
  const artifacts=[display];
  for(const kind of ["science","pure"]){
    const parentRecord=SCIENTIFIC_PARENTS.find(r=>r.role===kind);
    const parent=readWhole(repo,parentRecord);
    const exactRecord={...parentRecord};delete exactRecord.role;
    const value=buildReady(parent,kind,exactRecord,displayRecord);
    if(kind==="science"&&JSON.stringify(value.steps[0].progress_summary)!==JSON.stringify(displayValue.current_live_mapping))
      throw Error("Complete48 display mapping must equal the actual complete scientific step");
    artifacts.push(makeArtifact(kind,value));
  }
  fs.mkdirSync(outdir,{recursive:true});
  const outputs=[];
  for(const a of artifacts){
    const dest=path.join(outdir,a.expected.name);
    if(fs.existsSync(dest)){
      const bytes=fs.readFileSync(dest);
      if(bytes.length!==a.bytes.length||sha(bytes)!==a.expected.sha256)throw Error("Refuse to replace different metadata "+dest);
    }else fs.writeFileSync(dest,a.text,{encoding:"utf8",flag:"wx"});
    outputs.push({...a.expected,actual_output:dest});
  }
  process.stdout.write(JSON.stringify({
    schema:"complete-bhalf-mu001-parameter-text-construction-v1",
    complete:true,scientific_execution:false,runtime_source_rewrite:false,
    field_or_fee_or_numerical_result_created:false,
    optional_parameter_constructor_not_an_admission_condition:true,
    source_only_exact_whole_parent_construction:true,
    outputs
  },null,2)+"\n");
}
main();
