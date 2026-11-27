#!/usr/bin/env node
/** Full two-mode mathematical scalar observation parameters.
 * Reads complete original plans and the entire explicit display correspondence.
 * No numerical work or independent admission gate is performed.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const INPUTS={
  "runtime": {
    "scalar_progress": {
      "name": "fixed_fejer_actual_mathematical_progress.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_actual_mathematical_progress.py",
      "bytes": 26595,
      "sha256": "bff1e03ae12a08444cb9d9d572e439a9b40cf59e80a201cd500f95539ce9e391",
      "git_blob_sha": "509d502e13511c3746ba4647a6be32fce165bb61"
    },
    "driver": {
      "name": "fullclosed_fixed_fejer_stage_point_observed_so3_qp.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_stage_point_observed_so3_qp.py",
      "bytes": 95632,
      "sha256": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
      "git_blob_sha": "3a537a58e82f152c78d0408c8b2c5f4403af1106"
    },
    "launcher": {
      "name": "launch_fixed_fejer_stage_point_observed_actions.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_stage_point_observed_actions.py",
      "bytes": 21794,
      "sha256": "ed81031fe1eb33684d35585e44022314c8a631821859376a200c874a2aa0e5fa",
      "git_blob_sha": "1848230bd8a4f2dbbb4e4281e84d20d3d33ac531"
    },
    "reader": {
      "name": "read_fixed_fejer_stage_point_observed_so3_report.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_stage_point_observed_so3_report.py",
      "bytes": 98763,
      "sha256": "c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f",
      "git_blob_sha": "f37f64e9da226b40cc836c1b5f139eec342db764"
    }
  },
  "source_reproducer": {
    "name": "reproduce_fixed_fejer_mathematical_progress_entry.mjs",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_mathematical_progress_entry.mjs",
    "bytes": 12957,
    "sha256": "f6b30c44180f417d589a8a07fafe04980b18172c5cd4eb8e3815ffc0d8aa9d11",
    "git_blob_sha": "07de5c3e4414b9d2c064fe19991f253cb2d5f3b7"
  },
  "display": {
    "name": "fixed-fejer-mathematical-progress-display-correspondence.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-mathematical-progress-display-correspondence.json",
    "bytes": 14376,
    "sha256": "f649da05f8b74e6ed27cf92ab825ca2cabbdeae77c2c78e603f6f1f09c558372",
    "git_blob_sha": "141e5866eace9a96220b8160a3409217d784d8b9"
  },
  "hot_manifest": {
    "name": "fixed-fejer-stage-point-complete-delivery.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-point-complete-delivery.json",
    "bytes": 74078,
    "sha256": "f0497fee9a867ea1b6aee90f7d15ccd86415e7bcd3aee64e597e18afc7424d04",
    "git_blob_sha": "7392fb1e01864e2f13bfc7d4ebae04465db229fa"
  },
  "parent_records": {
    "independent": {
      "name": "fixed-fejer-stage-point-independent-complete-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-point-independent-complete-ready.json",
      "bytes": 99934,
      "sha256": "db456635a1811b993398d8ade8276ab753e63a2ac13ea878d27b98d313ef4b39",
      "git_blob_sha": "87b735efa8f879ded64cac07e878b41a6385834f"
    },
    "complete-parent": {
      "name": "fixed-fejer-stage-point-complete-parent-complete-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-point-complete-parent-complete-ready.json",
      "bytes": 99478,
      "sha256": "7709e8d96db33d4722ff4128b475a237972932411e51b4705186eaadab1d96df",
      "git_blob_sha": "83631109484a92ef5bcf6efece8a6e741dcaab10"
    }
  }
};
const EXPECTED={
  "independent": {
    "name": "fixed-fejer-stage-point-observed-independent-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-point-observed-independent-complete-ready.json",
    "bytes": 97225,
    "sha256": "86d39c01d5a93c5a4d897a02d79bddd23a9b98daa6d6fae6940cc5d348da92f6",
    "git_blob_sha": "03daa9af5617879a6fea591a2a2d6dfe78e78836"
  },
  "complete-parent": {
    "name": "fixed-fejer-stage-point-observed-complete-parent-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-point-observed-complete-parent-complete-ready.json",
    "bytes": 96781,
    "sha256": "a9e2d82e85d1cd9af9255f98fe4b2303666949185040fcfe9cef409b49b49088",
    "git_blob_sha": "e7c038e4d61133e1af6ddf5d0fd85dd5cc3408d3"
  }
};
const sha256=s=>crypto.createHash('sha256').update(s,'utf8').digest('hex');
function buildObservedReady(parent,mode,parentRecord,runtime,sourceReproducer,display,hotManifest){
 const oldDir='fixed-fejer-stage-point-'+mode,newDir='fixed-fejer-stage-point-observed-'+mode;
 const move=v=>typeof v==='string'?v.split(oldDir).join(newDir):Array.isArray(v)?v.map(move):
  v&&typeof v==='object'?Object.fromEntries(Object.entries(v).map(([k,x])=>[k.split(oldDir).join(newDir),move(x)])):v;
 const steps=move(parent.steps),science=steps[0],pure=steps[1];
 science.id='complete-fixed-fejer-stage-point-observed-'+mode+'-20261127';
 pure.id='actual-fixed-fejer-stage-point-observed-'+mode+'-20261127';
 science.script='topics/visible-flex-larger-amplitude/scripts/resume_20261126/'+runtime.launcher.name;
 pure.script='topics/visible-flex-larger-amplitude/scripts/resume_20261126/'+runtime.reader.name;
 science.scope=parent.scope+' Existing statistics/geometry/decision scalar observations are published at their own actual points without new F/J/root calls.';
 pure.scope=parent.steps[1].scope+' The complete scalar observer snapshot and captured original normal progress are read from the actual full report.';
 science.progress_summary={
  [newDir+'/actual-normal-evaluation-progress.json']:display.value.selected_original_live_mapping,
  [newDir+'/actual-mathematical-progress.json']:display.value.new_mathematical_live_mapping};
 const additions={math_initial_point:'initial_statistics.point_sha256',math_current_point:'current_statistics.point_sha256',
  math_current_Phi:'current_statistics.Phi',math_current_Gram:'current_statistics.max_relative_gram',
  math_geometry_point:'current_geometry.point_sha256',math_positive_physical_g:'current_geometry.positive_physical_g',
  math_accepted_direction_count:'accepted_direction_count',math_original_report_complete:'report_complete',
  math_observation_failures:'actual_counts.observation_failures',
  math_original_complete_normal_progress_captured:'original_normal_progress_snapshot.available'};
 for(const[summary,prefix]of [[Object.values(science.summary)[0],'actual_mathematical_observation'],
   [Object.values(pure.summary)[0],'mathematical_observation']]){
  for(const[k,v]of Object.entries(additions)){if(k in summary)throw Error('Duplicate scalar selector');summary[k]=prefix+'.'+v;}
 }
 const record=v=>({name:v.name,path:v.path,bytes:v.bytes,sha256:v.sha256,git_blob_sha:v.git_blob_sha});
 return {schema:'complete-fixed-fejer-stage-point-observed-ready-v1',executed:false,
  scientific_execution_permitted_only_in_public_Actions:true,
  parameter_mode:parent.parameter_mode,scope:science.scope,
  complete_parent_parameter_file:record(parentRecord),
  complete_unchanged_scientific_source_closure:record(hotManifest),
  complete_new_runtime_sources:Object.fromEntries(Object.entries(runtime).map(([k,v])=>[k,record(v)])),
  source_reproducer:record(sourceReproducer),complete_display_correspondence:record(display),
  all_complete_source_role_count:120,
  actual_run_id:null,actual_parent_report_sha256:null,actual_parent_checkpoint_sha256:null,
  actual_model_identity_sha256:null,actual_current_point_sha256:null,actual_accepted_or_complete_result:null,
  parameter_contract:{original_complete_science_and_pure_argv_values_and_order_retained:true,
   only_script_output_paths_and_scalar_observation_sources_changed:true,
   original_398_and385_scalar_selector_pairs_retained:true,new_observer_summary_scalars_per_step:10,
   original_48_progress_mapping_preserved_in_complete_correspondence:true,
   original_48_live_mapping_unchanged_claimed:false,
   current_live_original_normal_fields:18,current_live_mathematical_fields:30,current_total_live_fields:48,
   all_original_normal_progress_scalar_values_captured_in_full_report_and_readout:true,
   actual_unknown_parent_and_history_responsibilities_retained:true,
   no_F_J_or_root_computation_added:true,no_numerical_budget_or_acceptance_change:true},
  source_only_status:{complete_text_forward_and_inverse:true,local_Python_AST_or_compile:false,local_scientific_execution:false,no_new_admission_gate:true},
  steps};
}
function readFull(directory,record){
 const raw=fs.readFileSync(path.join(directory,record.name)),text=raw.toString('utf8');
 if(!Buffer.from(text,'utf8').equals(raw)||raw.length!==record.bytes||sha256(text)!==record.sha256)
  throw Error('Keep the complete original parameters '+record.name);
 return {...record,value:JSON.parse(text)};
}
function main(argv){
 const options={};
 for(let i=0;i<argv.length;i+=2){
  if(!['--parameter-directory','--generated-directory'].includes(argv[i])||argv[i+1]===undefined||options[argv[i]])
   throw Error('Supply both complete directory options once');
  options[argv[i]]=path.resolve(argv[i+1]);
 }
 const directory=options['--parameter-directory'],out=options['--generated-directory'];
 if(!directory||!out||directory===out||out.startsWith(directory+path.sep)||fs.existsSync(out))
  throw Error('Keep the original full plans and choose a separate fresh output directory');
 const display=readFull(directory,INPUTS.display),items=[];
 for(const[mode,parentRecord]of Object.entries(INPUTS.parent_records)){
  const parent=readFull(directory,parentRecord);
  const value=buildObservedReady(parent.value,mode,parentRecord,INPUTS.runtime,INPUTS.source_reproducer,
    display,INPUTS.hot_manifest),text=JSON.stringify(value)+'\n',wanted=EXPECTED[mode];
  if(Buffer.byteLength(text)!==wanted.bytes||sha256(text)!==wanted.sha256)
   throw Error('Complete observed plan differs: '+mode);
  items.push({name:wanted.name,text});
 }
 readFull(directory,INPUTS.display);
 for(const record of Object.values(INPUTS.parent_records))readFull(directory,record);
 fs.mkdirSync(out,{recursive:true});
 for(const item of items)fs.writeFileSync(path.join(out,item.name),item.text,{encoding:'utf8',flag:'wx'});
 console.log(JSON.stringify({complete:true,complete_plans:2,full_numerical_argv_unchanged:true,
  all_previous_summary_pairs_retained:[398,385],new_observer_summary_pairs_per_step:10,
  current_live_display:{original_normal_fields:18,mathematical_fields:30,total:48},
  original_complete_48_mapping_and_full_formal_capture_retained:true,
  scientific_execution:false,parameter_reproduction_is_not_a_scientific_admission_gate:true}));
}
if(path.resolve(process.argv[1]||'')===fileURLToPath(import.meta.url))main(process.argv.slice(2));
