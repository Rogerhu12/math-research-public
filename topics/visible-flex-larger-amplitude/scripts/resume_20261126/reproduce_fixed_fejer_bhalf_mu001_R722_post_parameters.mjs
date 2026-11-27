#!/usr/bin/env node
// Complete parameter-only source construction. No scientific modules are imported.
// Reads three whole run19 parameter parents and two whole run20 scientific plans.
// All source identities and every non-path post argument/selector remain unchanged.
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { execFileSync } from "node:child_process";

const CONFIG = {
  "schema": "complete-run20-bhalf-mu001-post-text-construction-v1",
  "topic": "topics/visible-flex-larger-amplitude",
  "oldNamespace": "fixed-fejer-meridian-batched-bhalf-first",
  "namespace": "fixed-fejer-meridian-batched-bhalf-mu001-first",
  "parentRestoreCommit": "6167a8bd8fd01c984095e705874e7516ea3fcb6c",
  "parentRecords": {
    "normal": {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R722-complete-normal32-full-circle-sixjet-fees-ready.json",
      "bytes": 49322,
      "sha256": "14e6ac6d8e95721a8fc1ddf983c7d3c67258f9daa41d01fefab955491d74d39a",
      "git_blob_sha": "bae2aeb057b0d1c58d6520038a3467bb4b2548b9",
      "role": "normal_ready"
    },
    "geometry": {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R722-complete-continuous-gram-curvature-support-ready.json",
      "bytes": 48299,
      "sha256": "d43d408cb4612a8998256e4e0d85085bb4041f0abf7e47dc89e5dd6b3e0874cc",
      "git_blob_sha": "bab97b529ea6e68d19fbd92335bd7064ef283202",
      "role": "geometry_ready"
    },
    "closed": {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-first-R722-closed-phase-grip-r718-ready.json",
      "bytes": 74772,
      "sha256": "6ea0e0482697134be32ef6ff080aea7007297116c2ad679a874087e61e3c972f",
      "git_blob_sha": "f5392f425a12a8b219f517f235c368e29e66f7ff",
      "role": "closed_ready"
    }
  },
  "scientificParameterFiles": [
    {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-mu001-science-complete-ready.json",
      "bytes": 97019,
      "sha256": "89b437a4986b3172d281b4928353072d15a15f2cebbb7a1fd8d973880d5166ca",
      "git_blob_sha": "598b4cdf62021a66b54c22b71171722027f1c0b5",
      "role": "science_ready"
    },
    {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-mu001-pure-complete-ready.json",
      "bytes": 86221,
      "sha256": "f627447f7887bdc9d7f257b4d0772173556683501cd5fa9f1e39890ec7ac7f64",
      "git_blob_sha": "53655fce8344040770e02295898a1c4ae9a06ebf",
      "role": "pure_ready"
    }
  ],
  "reproducerPath": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_bhalf_mu001_R722_post_parameters.mjs",
  "counts": {
    "normal": {
      "argv": 38,
      "selectors": 36
    },
    "geometry": {
      "argv": 8,
      "selectors": 48
    },
    "closed": {
      "argv": 8,
      "selectors": 66
    }
  },
  "outputPaths": {
    "normal": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-normal32-full-circle-sixjet-fees-ready.json",
    "geometry": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-continuous-gram-curvature-support-ready.json",
    "closed": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-closed-phase-grip-r718-ready.json"
  }
};
const EXPECTED = {
  "normal": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-normal32-full-circle-sixjet-fees-ready.json",
    "bytes": 61812,
    "sha256": "e0b3728a65788157abb245058fccbc477714e181ec34da8e9d1459a555a28d3e",
    "git_blob_sha": "d2dfbda375f6dc896d994de865ccd40017066757",
    "role": "normal_ready"
  },
  "geometry": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-complete-continuous-gram-curvature-support-ready.json",
    "bytes": 59207,
    "sha256": "d971eeb39b6c3b40b1531f68b8f10a039161a441ff1f19255b754305a6ab461a",
    "git_blob_sha": "6f1da76a472d17f54512855e71ad946016b87061",
    "role": "geometry_ready"
  },
  "closed": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-bhalf-mu001-first-R722-closed-phase-grip-r718-ready.json",
    "bytes": 92335,
    "sha256": "a6277fb071145363b2533e59e6aafd86f2ca4ba4b9a40579ed461846fb9964f6",
    "git_blob_sha": "e60b4bbcf83f7b9457b40ae4ba40d46ea6c3e34f",
    "role": "closed_ready"
  }
};

function topSpans(text) {
  let i=0; const white=()=>{while(/\s/.test(text[i]||"") && i<text.length)i++;};
  const str=()=>{const start=i;if(text[i++]!=='"')throw Error("Expected JSON string");while(i<text.length){const c=text[i++];if(c==="\\"){i++;continue;}if(c==='"')return {start,end:i};}throw Error("Unclosed string");};
  const value=()=>{const start=i,c=text[i];if(c==='"'){str();return {start,end:i};}if(c==="{"||c==="["){const stack=[c==="{"?"}":"]"];i++;while(stack.length&&i<text.length){if(text[i]==='"'){str();continue;}const d=text[i++];if(d==="{")stack.push("}");else if(d==="[")stack.push("]");else if(d==="}"||d==="]"){if(stack.pop()!==d)throw Error("JSON nesting");}}if(stack.length)throw Error("JSON nesting EOF");return{start,end:i};}while(i<text.length&&!/[,\}\]\s]/.test(text[i]))i++;return{start,end:i};};
  white();if(text[i++]!=="{")throw Error("Expected object");
  const entries=[];white();while(text[i]!=="}"){const key=str();const name=JSON.parse(text.slice(key.start,key.end));white();if(text[i++]!==":")throw Error("JSON colon");white();const v=value();entries.push({name,keyStart:key.start,keyEnd:key.end,start:v.start,end:v.end});white();if(text[i]===","){i++;white();}else if(text[i]!=="}")throw Error("JSON separator");}
  return{entries,close:i};
}
function editText(parent, edits) {
  const sorted=[...edits].sort((a,b)=>a.start-b.start);
  let end=0,delta=0;for(const e of sorted){if(e.start<end||parent.slice(e.start,e.end)!==e.before)throw Error("Edit overlap or old bytes");e.newStart=e.start+delta;e.newEnd=e.newStart+e.after.length;delta+=e.after.length-(e.end-e.start);end=e.end;}
  let output=parent;for(const e of [...sorted].reverse())output=output.slice(0,e.start)+e.after+output.slice(e.end);
  let restored=output;for(const e of [...sorted].reverse()){if(restored.slice(e.newStart,e.newEnd)!==e.after)throw Error("Reverse bytes");restored=restored.slice(0,e.newStart)+e.before+restored.slice(e.newEnd);}
  if(restored!==parent)throw Error("Full parent byte reversal failed");
  return{output,edits:sorted};
}
function makeReady(kind, parent, config, currentFeeRecords) {
  const old=JSON.parse(parent), spans=topSpans(parent), entries=new Map(spans.entries.map(x=>[x.name,x]));
  const edits=[], renamed={};const replaceValue=(key,newValue)=>{const p=entries.get(key);if(!p)throw Error("Missing "+key);edits.push({start:p.start,end:p.end,before:parent.slice(p.start,p.end),after:JSON.stringify(newValue,null,2).replace(/\n/g,"\n  ")});};
  const rename=(key,next)=>{const p=entries.get(key);if(!p||entries.has(next))throw Error("Historical key collision "+key);renamed[key]=next;edits.push({start:p.keyStart,end:p.keyEnd,before:parent.slice(p.keyStart,p.keyEnd),after:JSON.stringify(next)});};
  const map=s=>s.split(config.oldNamespace).join(config.namespace);
  replaceValue("schema",map(old.schema));
  const expectedKey={normal:"source_report_expected_path",geometry:"source_normal_report_expected_path",closed:"source_geometry_expected_path"}[kind];
  replaceValue(expectedKey,map(old[expectedKey]));
  const p=entries.get("steps");let stepText=parent.slice(p.start,p.end);const oldScope=map(old.steps[0].scope);
  const newScope=oldScope.replace(/\brun19\b/g,"run20")+" The upstream run20 scientific command changes only initial --restoration-damping from literal .01 to literal .001 relative to run19; ordinary --damping remains literal .01. This does not change the fixed metric, prescribed b/S=1/2 and delta=1/32 seed definitions, any full variable/domain/budget, or these fee algorithms. Every actual field, packet and accuracy result must nevertheless be read from this run20 namespace; no finite-iteration, nonlinear-improvement or fee-success claim follows from the smaller restoration parameter.";
  stepText=map(stepText);if(stepText.split(JSON.stringify(oldScope)).length!==2)throw Error("Scope bytes not unique");
  stepText=stepText.replace(JSON.stringify(oldScope),JSON.stringify(newScope));
  edits.push({start:p.start,end:p.end,before:parent.slice(p.start,p.end),after:stepText});
  for(const key of ["run19_complete_parameter_contract","run19_complete_parameter_parent","run19_current_post_plan"])rename(key,"parameter_parent_"+key);
  if(kind==="closed")for(const key of ["complete_parameter_correspondence","complete_current_fee_ready_files","complete_current_scientific_parameter_files","current_scientific_parameter_file_source_scope","current_reproduction_source_path"])rename(key,"parameter_parent_run19_"+key);
  const step=JSON.parse(stepText)[0];
  const selectors=Object.values(step.summary)[0], oldSelectors=Object.values(old.steps[0].summary)[0];
  const changed=[];step.args.forEach((a,i)=>{if(a!==old.steps[0].args[i])changed.push({index:i,before:old.steps[0].args[i],after:a});});
  if(JSON.stringify(changed.map(x=>x.index))!=="[3,5]"||step.args.length!==config.counts[kind].argv||Object.keys(selectors).length!==config.counts[kind].selectors||JSON.stringify(selectors)!==JSON.stringify(oldSelectors))throw Error("Complete parameter preservation failed");
  const contract={
    schema:"complete-same-source-bhalf-mu001-R722-post-parameter-successor-v1",
    new_scientific_run_label:"20",
    actual_run_id:null,actual_run_attempt:null,actual_launch_record:null,
    science_namespace:config.namespace,current_science_report:"{work}/"+config.namespace+"/report.json",
    complete_current_science_and_pure_parameter_files:config.scientificParameterFiles,
    actual_current_input_file_records:null,actual_complete_report_file_record:null,
    actual_normal_model_identity_sha256:null,actual_full_point_sha256:null,
    actual_seed_model_identity_sha256:null,actual_immutable_snapshot_record:null,
    accurate_fee_or_closed_result:null,
    exact_upstream_scientific_parameter_delta:{
      flag:"--restoration-damping",argv_value_index_zero_based:37,parent_literal:".01",current_literal:".001",
      metric_damping_flag:"--damping",metric_damping_literal_unchanged:".01",
      scientific_argv_words:157,pure_argv_words:7,scientific_formal_selectors:458,
      no_other_scientific_numeric_argument_or_budget_change:true,
      full_parent_and_current_scientific_argv_in_pinned_whole_files:true,
      smaller_mu_guarantees_finite_iteration_or_nonlinear_improvement:false
    },
    prescribed_seed:old.run19_complete_parameter_contract.prescribed_seed,
    fixed_metric_recipe_identity_sha256:old.run19_complete_parameter_contract.fixed_metric_recipe_identity_sha256,
    same_fixed_metric_and_prescribed_seed_basis:"Initial restoration damping is an outer QP/restoration search parameter. The original Fejer RN-even chart, R690 scalar definition, frozen reference M160/J923/N2048, b/S=1/2 and profile delta=1/32 formulas and all mathematical field equations are unchanged. Actual runner inputs, candidate words, model and point identities are still read and validated in full; no old actual bytes or numerical values are inferred.",
    old_seed_point_root_values_or_certificates_inherited:false,
    runtime_or_scientific_source_modified_by_this_parameter_package:false,
    runtime_source_family_role_count:137,original_120_source_pairs_retained:true,
    all_scientific_solver_budgets_and_variables_retained:true,
    all_normal32_full_circle1024_radial922_plus_exact_cuts_and_sixjets_retained:true,
    all_current_and_parent_parameter_fields_preserved:true,
    parent_run19_and_older_facts_are_historical_parameter_provenance_not_current_inputs:true,
    all_original_supported_peers_and_external_unknown_history_preserved:true,
    new_solver_admission_gate_or_reproducer_step:false,
    raw_arrays_and_all_reports_stay_on_public_Actions_runner:true,
    complete_parent_ready_files:config.parentRecords,
    exact_parent_restore_commit:config.parentRestoreCommit,
    current_reproduction_source_path:config.reproducerPath
  };
  const extra={
    run20_complete_parameter_contract:contract,
    run20_complete_parameter_parent:{
      complete_parameter_parent_file:config.parentRecords[kind],
      original_current_metadata_preserved_under_exact_keys:renamed,
      parent_all_argv_and_selectors_available_in_full_pinned_file:true,
      complete_parent_step_scope:old.steps[0].scope,
      parent_and_current_runtime_source_sha256_maps_exactly_equal:true,
      original_run19_actual_values_not_used_as_current:false
    },
    run20_current_post_plan:{
      schema:"complete-bhalf-mu001-post-step-correspondence-v1",
      all_original_argv_flags_numbers_and_order_preserved:true,
      exact_changed_argv_words:changed,
      original_args:old.steps[0].args,current_args:step.args,
      source_script_unchanged:step.script,parent_bundle_unchanged:step.parent_bundle,
      original_scalar_selector_count:Object.keys(oldSelectors).length,
      current_scalar_selector_count:Object.keys(selectors).length,
      entire_selector_name_and_expression_maps_unchanged:true,
      output_roles_and_full_source_records_unchanged:true,
      steps_not_yet_executed:true
    }
  };
  extra.run20_complete_parameter_parent.original_run19_actual_values_not_used_as_current=true;
  if(kind==="closed"){
    extra.complete_parameter_correspondence={complete_direct_parent_ready:config.parentRecords.closed,original_args:old.steps[0].args,current_args:step.args,all_original_summary_selectors_retained:true,original_scalar_selector_count:66,current_scalar_selector_count:66,support_chunk_rows_unchanged:"4096",full_mathematical_domains_and_all_source_obligations_retained:true,complete_historical_correspondence_key:renamed.complete_parameter_correspondence};
    extra.complete_current_fee_ready_files=[currentFeeRecords.normal,currentFeeRecords.geometry];
    extra.complete_current_scientific_parameter_files=config.scientificParameterFiles;
    extra.current_scientific_parameter_file_source_scope="The two pinned complete run20 science/pure parameter files specify exactly --restoration-damping .001 and unchanged --damping .01, b/S=1/2 and profile delta=1/32, with the same complete 137-source family. Parameter readiness is not a returned field or certificate; every new actual input/report/point/model/packet remains unassumed.";
    extra.current_reproduction_source_path=config.reproducerPath;
  }
  const insertion=JSON.stringify(extra,null,2).slice(1,-1).trimEnd();
  const insertAt=spans.entries[spans.entries.length-1].end;
  edits.push({start:insertAt,end:insertAt,before:"",after:","+insertion});
  const result=editText(parent,edits);const current=JSON.parse(result.output);
  for(const [key,value] of Object.entries(old)){
    if(key==="schema"||key===expectedKey||key==="steps")continue;
    const target=renamed[key]||key;
    if(JSON.stringify(value)!==JSON.stringify(current[target]))throw Error("Lost parent field "+key);
  }
  if(JSON.stringify(old.complete_source_sha256)!==JSON.stringify(current.complete_source_sha256))throw Error("Source map changed");
  return{...result,kind,current,renamed,counts:{argv:step.args.length,selectors:Object.keys(selectors).length},changed};
}

function identity(text) {
  const b=Buffer.from(text,"utf8");
  return{bytes:b.length,sha256:crypto.createHash("sha256").update(b).digest("hex"),
    git_blob_sha:crypto.createHash("sha1").update(Buffer.from("blob "+b.length+"\0")).update(b).digest("hex")};
}
function check(text, record, label) {
  const a=identity(text);
  for(const key of ["bytes","sha256","git_blob_sha"])if(a[key]!==record[key])throw Error(label+" whole "+key+" differs");
  if(a.bytes>=100000)throw Error(label+" is not a complete under-100KB text artifact");
  JSON.parse(text);return a;
}
function parseArgs(argv) {
  const o={repo:".",out:"reproduced-run20-bhalf-mu001-post",restoreParent:false,checkExisting:false};
  for(let i=0;i<argv.length;i++){
    const x=argv[i];
    if(x==="--repo"||x==="--out"){if(i+1===argv.length)throw Error("Missing "+x);o[x.slice(2)]=argv[++i];}
    else if(x==="--restore-parent")o.restoreParent=true;
    else if(x==="--check-existing")o.checkExisting=true;
    else if(x==="--help"){console.log("node reproduce_fixed_fejer_bhalf_mu001_R722_post_parameters.mjs --repo REPO --out OUTPUT [--restore-parent] [--check-existing]\n--restore-parent reads exactly the complete run19 parents at commit "+CONFIG.parentRestoreCommit+" by git show; it does not change a ref.\n--check-existing compares the three whole outputs at OUTPUT instead of writing them.\nThis is optional source/parameter text reproduction, never a scientific or controller admission step.");process.exit(0);}
    else throw Error("Unknown argument "+x);
  }
  o.repo=path.resolve(o.repo);o.out=path.resolve(o.out);return o;
}
function readParent(o, record) {
  const text=o.restoreParent?execFileSync("git",["-C",o.repo,"show",CONFIG.parentRestoreCommit+":"+record.path],{encoding:"utf8",maxBuffer:2000000}):fs.readFileSync(path.join(o.repo,record.path),"utf8");
  check(text,record,"run19 "+record.role);return text;
}
function validateScientificParameterFiles(o) {
  const values={};
  for(const record of CONFIG.scientificParameterFiles){
    const text=fs.readFileSync(path.join(o.repo,record.path),"utf8");
    check(text,record,"run20 "+record.role);values[record.role]=JSON.parse(text);
  }
  const science=values.science_ready,pure=values.pure_ready;
  const a=science.steps[0].args, p=pure.steps[0].args;
  const take=flag=>{const i=a.indexOf(flag);if(i<0||i+1>=a.length)throw Error("Missing scientific "+flag);return a[i+1];};
  if(a.length!==157||p.length!==7||a[36]!=="--restoration-damping"||a[37]!==".001"||
     take("--damping")!==".01"||take("--seed-boundary-total-length")!=="1/2"||
     take("--seed-profile-delta")!=="1/32"||science.complete_driver_source_role_count!==137)
    throw Error("The complete current scientific parameter contract differs");
  if(Object.values(science.steps[0].summary).reduce((n,x)=>n+Object.keys(x).length,0)!==458)
    throw Error("The complete scientific formal selector map differs");
  return values;
}
function main() {
  const o=parseArgs(process.argv.slice(2));
  validateScientificParameterFiles(o);
  const outputs=[],records={};
  for(const kind of ["normal","geometry","closed"]){
    const parent=readParent(o,CONFIG.parentRecords[kind]);
    const made=makeReady(kind,parent,CONFIG,records);
    const a=check(made.output,EXPECTED[kind],"run20 "+kind);
    records[kind]={path:CONFIG.outputPaths[kind],bytes:a.bytes,sha256:a.sha256,git_blob_sha:a.git_blob_sha,role:kind+"_ready"};
    outputs.push({kind,text:made.output,record:records[kind],counts:made.counts,edit_count:made.edits.length});
  }
  for(const item of outputs){
    const filename=path.join(o.out,item.record.path);
    if(o.checkExisting){if(fs.readFileSync(filename,"utf8")!==item.text)throw Error("Full existing output differs: "+filename);}
    else{fs.mkdirSync(path.dirname(filename),{recursive:true});fs.writeFileSync(filename,item.text,"utf8");}
  }
  console.log(JSON.stringify({complete:true,source_and_parameter_text_only:true,
    scientific_execution:false,no_ref_mutation:true,no_controller_or_solver_gate:true,
    exact_parent_restore_commit:CONFIG.parentRestoreCommit,
    every_original_parent_byte_recovered_by_inverse_edits:true,
    runtime_source_and_all_post_numerical_parameters_unchanged:true,
    complete_records:outputs.map(x=>({kind:x.kind,...x.record,counts:x.counts,edit_count:x.edit_count}))},null,2));
}
main();
