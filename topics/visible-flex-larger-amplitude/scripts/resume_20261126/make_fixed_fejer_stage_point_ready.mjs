#!/usr/bin/env node
/** Full stage immutable-point parameter construction from the whole original plan.
 * Both independent and actual full-thirteen-member-parent modes are complete.
 * No Python, numerical fixture, field or solver is invoked.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const INPUT={
  "name": "fixed-fejer-immutable-point-complete-run12-ready.json",
  "bytes": 92380,
  "sha256": "ab5c00086e21faaa5017ea469c4a63e7d389ecc3019b03a28e46b9daaa129578",
  "git_blob_sha": "13eea0c110a7d98bef3736d1585aa57584402ac3",
  "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-immutable-point-complete-run12-ready.json"
};
const RUNTIME={
  "stage_matrices": {
    "name": "fixed_fejer_immutable_point_stage_matrices.py",
    "bytes": 61280,
    "sha256": "e4d42910f9550a20d0afc16aab8f54b5ea1ceb18ace375128f3a79bfef0e76ce",
    "git_blob_sha": "002985b6b754585f08f05b349f305adf03ad2f9e",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_immutable_point_stage_matrices.py"
  },
  "adjacent_matrices": {
    "name": "fixed_fejer_stage_point_adjacent_matrices.py",
    "bytes": 36766,
    "sha256": "d04cf80d40a16410a2338f3b4b0c3bbdd0084cfc2ad5270bee21d33ded9449b5",
    "git_blob_sha": "d5ab132b50b7f5caae92a417f590ee44e77c6ca0",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_point_adjacent_matrices.py"
  },
  "endpoint": {
    "name": "fixed_fejer_stage_point_normal_lift.py",
    "bytes": 98490,
    "sha256": "42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10",
    "git_blob_sha": "ffdaf4a094c7a0363bd6bc3ed316ba1e7e8ec25c",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_point_normal_lift.py"
  },
  "root_packets": {
    "name": "fixed_fejer_stage_point_root_packets.py",
    "bytes": 73070,
    "sha256": "140f639656c2a30c59f0ba4c8153e3467d5abddf8189a84fcc38fb6638ee8aaf",
    "git_blob_sha": "310aa66a367efe0bb6ca26da12b4b4395abd3f08",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_point_root_packets.py"
  },
  "analytic_J3_binding": {
    "name": "fixed_fejer_stage_point_source_binding.py",
    "bytes": 38356,
    "sha256": "9171871fcaaa1d2e65de1c40071cf8bb1acac0d7b0cc1d1da5b9cb36f690076f",
    "git_blob_sha": "fb9dc94fa9b137dd64f602d9cd84b8997d36bdc2",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_point_source_binding.py"
  },
  "envelope_transfer": {
    "name": "transfer_fixed_fejer_stage_point_memory.py",
    "bytes": 78863,
    "sha256": "afa2d6397c331b5bf55dd461bbf52a35839ff610d3db0f12a043e8eceef3b6ed",
    "git_blob_sha": "7f1f3971893d8895d7e1b8cc3612e563a44d3095",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/transfer_fixed_fejer_stage_point_memory.py"
  },
  "geometry": {
    "name": "so3_fixed_fejer_stage_point_geometry.py",
    "bytes": 70709,
    "sha256": "2ecd2b23eccf6bee564c07daa386fbd232d7ff9f5634b484317d62ab10e56471",
    "git_blob_sha": "2677d379e87b359088177b244428894311348996",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_stage_point_geometry.py"
  },
  "driver": {
    "name": "fullclosed_fixed_fejer_stage_point_so3_qp.py",
    "bytes": 93158,
    "sha256": "050a6067fbb2fb4d054a97bf73899cfe5d4629197e42c39f00846a1f6a63b268",
    "git_blob_sha": "b0374f2db88ca38a936c7eadfc97f5377922c146",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_stage_point_so3_qp.py"
  },
  "launcher": {
    "name": "launch_fixed_fejer_stage_point_actions.py",
    "bytes": 21785,
    "sha256": "8fed7b6a7ff6c988ee2240a4193f9440fd91ef158e5ac47d6248868d4e19214c",
    "git_blob_sha": "fed243876328a2933fcfb10288f6f42edda16211",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_stage_point_actions.py"
  },
  "reader": {
    "name": "read_fixed_fejer_stage_point_so3_report.py",
    "bytes": 97975,
    "sha256": "42e198f8d886641048059c3cdd8110b8bc3d000cdf350da1de54ac4bb83014a0",
    "git_blob_sha": "4304a1fdbe907bdb9c6708d7a89f5a18733ce15b",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_stage_point_so3_report.py"
  }
};
const SOURCE_REPRODUCER={
  "name": "reproduce_fixed_fejer_stage_point_sources.mjs",
  "bytes": 54988,
  "sha256": "442a45f849badc2bc054ca4b3d288b627f72a5383821768c9449e3db4e78bfd5",
  "git_blob_sha": "5e5f9010842c03ca406b94a460df4a6d80a964a6",
  "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_stage_point_sources.mjs"
};
const EXPECTED={
  "independent": {
    "name": "fixed-fejer-stage-point-independent-complete-ready.json",
    "bytes": 99934,
    "sha256": "db456635a1811b993398d8ade8276ab753e63a2ac13ea878d27b98d313ef4b39",
    "git_blob_sha": "87b735efa8f879ded64cac07e878b41a6385834f",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-point-independent-complete-ready.json"
  },
  "complete-parent": {
    "name": "fixed-fejer-stage-point-complete-parent-complete-ready.json",
    "bytes": 99478,
    "sha256": "7709e8d96db33d4722ff4128b475a237972932411e51b4705186eaadab1d96df",
    "git_blob_sha": "83631109484a92ef5bcf6efece8a6e741dcaab10",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-point-complete-parent-complete-ready.json"
  }
};
const sha256=s=>crypto.createHash('sha256').update(s,'utf8').digest('hex');
function buildStagePointReady(parent,mode,runtime,sourceReproducer,parentRecord){
 if(!['independent','complete-parent'].includes(mode))throw Error('Use the two complete declared input modes');
 const ready=JSON.parse(JSON.stringify(parent)),oldDir='fixed-fejer-immutable-point-first';
 const newDir='fixed-fejer-stage-point-'+(mode==='independent'?'independent':'complete-parent');
 const move=v=>typeof v==='string'?v.split(oldDir).join(newDir):Array.isArray(v)?v.map(move):
  v&&typeof v==='object'?Object.fromEntries(Object.entries(v).map(([k,x])=>[k.split(oldDir).join(newDir),move(x)])):v;
 ready.steps=move(ready.steps);
 ready.schema='complete-fixed-fejer-stage-point-entry-ready-v1';
 ready.executed=false;
 ready.parameter_mode=mode==='independent'?'independent-original-reference':'actual-complete-Fejer-full13-parent';
 ready.scope=(mode==='independent'
  ?'Independent full solve of the same predeclared Fejer target from its exact frozen reference point; all original peer history obligations and the actual run12 peer are explicit, without inventing any unreturned typed row or parent final.'
  :'Full same-Fejer solve from a genuinely returned complete 477499/274d report and all thirteen final members; the entire inbound, explicit, protected and typed history is reread. A future parent report or checkpoint identity is not filled in.')
  +' All original variables, 32 stages, sixjets and numerical budgets remain. Stage requests use the immutable owner; complete entry and exit point reads and all other guards remain. No measured acceleration is claimed.';
 ready.original_reference_target_declaration=ready.declared_input_delta;delete ready.declared_input_delta;
 ready.declared_stage_point_delta={
  same_complete_Fejer_mathematical_target:true,reference_and_current_M:160,reference_and_current_N:2048,reference_and_current_J:923,
  full_free_size:1333370,current_rotation_angular_size:482,
  stage_point_owner_binding_in_place_of_per_request_complete_point_copy:true,
  original_full_word_and_array_SHA_entry_reads_retained:true,complete_exit_point_words_added:true,
  all_other_original_stage_guards_retained:true,all_original_scientific_matrix_method_bodies_unchanged:true,
  complete_normal_class_method_bodies_unchanged:true,complete_scientific_driver_suffix_unchanged:true,
  complete_parent_required_only_when_consuming_parent_final:true,
  old_Phi_geometry_root_values_or_certificates_inherited:false,
  measured_acceleration_or_completed_field_claimed:false
 };
 ready.original_parameter_lineage={preserved_in_complete_parent_plan_sha256:parentRecord.sha256};
 ready.complete_parameter_origin=JSON.parse(JSON.stringify(parentRecord));
 ready.complete_source_reproducer=JSON.parse(JSON.stringify(sourceReproducer));
 ready.complete_source_sha256={...parent.complete_source_sha256,
  ...Object.fromEntries(Object.values(runtime).map(r=>[r.name,r.sha256]))};
 for(const name of ['fixed_fejer_detached_stage_matrices.py','fixed_fejer_adjacent_normal_matrices.py',
   'fixed_fejer_normal_lift_operator.py','fixed_fejer_immutable_normal_root_packets.py',
   'fixed_fejer_complete_source_binding.py','transfer_fixed_fejer_material_envelope_memory.py',
   'so3_fixed_fejer_complete_geometry.py','fullclosed_fixed_fejer_immutable_point_so3_qp.py',
   'launch_fixed_fejer_immutable_point_actions.py','read_fixed_fejer_immutable_point_so3_report.py'])
  delete ready.complete_source_sha256[name];
 ready.full_runtime_source_role_count=119;
 ready.source_only_status={all_whole_source_hashes_recorded:true,complete_JS_source_forward_and_inverse:true,
  complete_new_runtime_sources:10,original_complete_110_source_pairs_retained:true,
  local_Python_AST_or_compile:false,local_scientific_execution:false,
  source_reproduction_is_not_a_scientific_admission_gate:true};
 ready.actual_parent_report_sha256=null;ready.actual_parent_checkpoint_sha256=null;
 ready.actual_run=null;
 ready.future_result={model_identity_sha256:null,current_point_sha256:null,report_sha256:null,checkpoint_sha256:null,
  accepted_direction_count:null,complete:null};
 ready.progress_publication_contract={
  original_complete_contract:parent.progress_publication_contract,
  all_original_48_scalar_selector_pairs_retained:true,display_selector_changes_in_this_version:false,
  new_stage_owner_counters_are_in_complete_natural_report_and_readout:true,
  no_new_public_progress_selector_added:true,
  progress_is_not_an_accepted_or_final_field:true};
 const science=ready.steps[0],pure=ready.steps[1];
 science.id='complete-fixed-fejer-stage-point-'+mode+'-20261127';
 pure.id='actual-fixed-fejer-stage-point-'+mode+'-20261127';
 science.script='topics/visible-flex-larger-amplitude/scripts/resume_20261126/'+runtime.launcher.name;
 pure.script='topics/visible-flex-larger-amplitude/scripts/resume_20261126/'+runtime.reader.name;
 science.scope=ready.scope;
 pure.scope='Complete pure read of the whole source-bound stage-point report, all original own-point snapshots and complete packet, latest full stage scope counters, actual fixed target and every parent/history/final record. No F/J/root and no inferred future final. The original whole reader and source/model guards remain.';
 const removed=[];
 if(mode==='independent'){
  science.args.push('--pending-parallel-envelope-run','46011377225/1',
   '--pending-parallel-envelope-source','46011377225/1=477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd');
 }else{
  const args=[];
  for(let i=0;i<science.args.length;i++){
   const arg=science.args[i];
   if(arg==='--independent-envelope-branch'){removed.push([arg]);continue;}
   if(['--pending-parallel-envelope-run','--pending-parallel-envelope-source'].includes(arg)){
    removed.push([arg,science.args[++i]]);continue;
   }
   args.push(arg);
  }
  const report='{work}/fixed-fejer-immutable-point-first/report.json';
  args.push('--material-envelope-parent-report',report,'--material-envelope-seed-report',report,
   '--material-envelope-seed-checkpoint','{work}/fixed-fejer-immutable-point-first/final.npz','--manifest',report);
  science.args=args;
  science.parent_bundle='fixed-fejer-immutable-point-first/final.npz';
  pure.parent_bundle='fixed-fejer-immutable-point-first/final.npz';
 }
 const counts=['point_owner_entry_checks','point_owner_entry_failures','point_owner_stage_checks','point_owner_stage_failures',
  'point_owner_exit_checks','point_owner_exit_failures','whole_point_entry_reads','whole_point_entry_read_failures',
  'whole_point_exit_reads','whole_point_exit_read_failures','whole_point_entry_array_sha_checks','whole_point_entry_array_sha_failures'];
 const times=['point_owner_binding_seconds','complete_point_word_read_seconds','complete_point_array_sha_seconds'];
 const scienceSummary=science.summary[newDir+'/report.json'];
 const pureSummary=pure.summary['postprocess/'+newDir+'-readout.json'];
 if(!scienceSummary||!pureSummary)throw Error('Keep the entire actual report and pure summary paths');
 for(const[summary,prefix]of [[scienceSummary,'latest_operator_metadata.detached_stage_matrix_reuse'],
    [pureSummary,'detached_stage_matrix_diagnostics']]){
  for(const key of counts){const name='stage_point_'+key;if(name in summary)throw Error('Existing selector collision');summary[name]=prefix+'.actual_counts.'+key;}
  for(const key of times){const name='stage_point_'+key;if(name in summary)throw Error('Existing selector collision');summary[name]=prefix+'.'+key;}
 }
 ready.complete_unknown_history_responsibility={
  original_whole_independent_mode_tokens_retained_in_independent_plan:true,
  additional_same_target_peer:{run:'46011377225/1',source_sha256:'477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd'},
  parent_mode_consumes_all_actual_nested_transfer_and_inbound_reports:true,
  current_source_complete_restart_supported_by_unchanged_restart_contract:true,
  unknown_parallel_final_and_typed_rows_reconstructed:false,
  all_old_target_material_reinterpretation_declarations_retained:true};
 ready.complete_parameter_correspondence={
  whole_parent_plan:JSON.parse(JSON.stringify(parentRecord)),
  original_science_args:parent.steps[0].args.length,current_science_args:science.args.length,
  original_pure_args:parent.steps[1].args.length,current_pure_args:pure.args.length,
  removed_only_explicit_independent_mode_tokens_count:removed.length,
  removed_tokens_are_complete_in_original_plan_and_delivery_correspondence:true,
  all_other_original_numerical_argv_values_and_order_retained:true,
  original_science_summary_count:Object.keys(Object.values(parent.steps[0].summary)[0]).length,
  original_pure_summary_count:Object.keys(Object.values(parent.steps[1].summary)[0]).length,
  new_stage_owner_and_word_cost_scalar_selectors_per_step:15,
  all_original_48_progress_selector_pairs_exactly_retained:true};
 return ready;
}
function readFull(directory){
 const bytes=fs.readFileSync(path.join(directory,INPUT.name)),text=bytes.toString('utf8');
 if(!Buffer.from(text,'utf8').equals(bytes)||bytes.length!==INPUT.bytes||sha256(text)!==INPUT.sha256)
  throw Error('Keep the entire original fixed Fejer plan');
 return JSON.parse(text);
}
function main(argv){
 const options={};
 for(let i=0;i<argv.length;i+=2){
  if(!['--parameter-directory','--generated-directory'].includes(argv[i])||argv[i+1]===undefined||options[argv[i]])
   throw Error('Supply both complete directory options exactly once');
  options[argv[i]]=path.resolve(argv[i+1]);
 }
 const directory=options['--parameter-directory'],out=options['--generated-directory'];
 if(!directory||!out||directory===out||out.startsWith(directory+path.sep)||fs.existsSync(out))
  throw Error('Keep the original whole plan and choose a separate fresh destination');
 const parent=readFull(directory),items=[];
 for(const[mode,expected]of Object.entries(EXPECTED)){
  const value=buildStagePointReady(parent,mode,RUNTIME,SOURCE_REPRODUCER,INPUT),text=JSON.stringify(value)+'\n';
  if(Buffer.byteLength(text)!==expected.bytes||sha256(text)!==expected.sha256)
   throw Error('Complete parameter reproduction differs: '+mode);
  items.push({name:expected.name,text});
 }
 readFull(directory);fs.mkdirSync(out,{recursive:true});
 for(const item of items)fs.writeFileSync(path.join(out,item.name),item.text,{encoding:'utf8',flag:'wx'});
 console.log(JSON.stringify({complete:true,complete_plans:2,all_original_numerical_argv_values_and_order_retained:true,
  original_summary_selectors_retained:[383,370],new_own_scope_cost_selectors_per_step:15,
  original_progress_selector_pairs_retained:48,scientific_execution:false,
  parameter_reproduction_is_not_a_scientific_admission_gate:true}));
}
if(path.resolve(process.argv[1]||'')===fileURLToPath(import.meta.url))main(process.argv.slice(2));
