#!/usr/bin/env node
/** Complete M320 parameter reproduction, with both original input modes.
 * Reads the whole original Fejer M160 plan; preserves every numerical budget,
 * original scalar selector and all 48 progress selectors. No solver is called.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const INPUT={
  "bytes": 92380,
  "sha256": "ab5c00086e21faaa5017ea469c4a63e7d389ecc3019b03a28e46b9daaa129578",
  "git_blob_sha": "13eea0c110a7d98bef3736d1585aa57584402ac3",
  "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-immutable-point-complete-run12-ready.json",
  "name": "fixed-fejer-immutable-point-complete-run12-ready.json"
};
const RUNTIME={
  "frequency_layout": {
    "name": "fixed_fejer_frequency_layout.py",
    "bytes": 13582,
    "sha256": "67c5503e8df036aa1468a3df2f395f5a33c91c4309520fbb8862b39c2495a251",
    "git_blob_sha": "6fff72221e35c9835bdedfa7dd5089f05e200937"
  },
  "meridian": {
    "name": "fixed_fejer_frequency_meridian_operator.py",
    "bytes": 43041,
    "sha256": "f7058f9c9d3f02292b738b360b116062b60bcf07907286acb42346eb431bdf9a",
    "git_blob_sha": "fdcb0339b20957a8cccfef0000b90da69067ac17"
  },
  "new_moment_input": {
    "name": "fixed_fejer_frequency_literal_moment_input.py",
    "bytes": 31477,
    "sha256": "4bf9e5b96884e26750f6f08cffcc338965d94969e7516c3d2ed493d037697849",
    "git_blob_sha": "464fa397a7fa322e8739531213551d4811175f43"
  },
  "closure_values": {
    "name": "fixed_fejer_frequency_closure_values.py",
    "bytes": 59771,
    "sha256": "6949ca97c49d338761ef2bc5e748ed9a55e20682a6e6225a7fc2bc63ead2bc88",
    "git_blob_sha": "46a10d1e9a03319e92784b8d6f514e46c15938d0"
  },
  "analytic_J3": {
    "name": "fixed_fejer_frequency_stage_jacobian.py",
    "bytes": 25706,
    "sha256": "740d3b39fcbdbb766962d26d3ec960b8883810418af83f13bd7b55c11776dbc3",
    "git_blob_sha": "c2315e13e8ba8c87855294f3dc8e47754e95cb56"
  },
  "analytic_frame": {
    "name": "fixed_fejer_frequency_normal_frame.py",
    "bytes": 47253,
    "sha256": "e165dda2543dd4175fa1f7187dfd28cad84ac08ec95a24f27a5e6addcaa2fc34",
    "git_blob_sha": "0dffec85d09398ec68095d2a7fc2c1ffd99eb46d"
  },
  "frame_C1": {
    "name": "fixed_fejer_frequency_frame_c1.py",
    "bytes": 37361,
    "sha256": "9d001b492aa49058b545e05eb67c6eb2413fa512580393243955f8a706015fdd",
    "git_blob_sha": "67d2ac4cfa8e31339343adbe47ca5c8b4b214a93"
  },
  "stage_matrices": {
    "name": "fixed_fejer_frequency_stage_matrices.py",
    "bytes": 47791,
    "sha256": "f30eac74cfb436cd40fa3413d4ca4c037ef1fe79ac05b442738de07eef522642",
    "git_blob_sha": "f368ec12a52edb995bb0c0d65a2017cb74687701"
  },
  "adjacent_matrices": {
    "name": "fixed_fejer_frequency_adjacent_matrices.py",
    "bytes": 36766,
    "sha256": "59e9089bc991136ff9e1e2fd4a37663d7f91c03837eac9bd49c8d49c206ce015",
    "git_blob_sha": "fb4374b147c33084df41df2aed826ca0ab6e29bf"
  },
  "reference_calibration": {
    "name": "fixed_fejer_frequency_calibration.py",
    "bytes": 12329,
    "sha256": "90a8c8eae8d67d5d09fc09ad0593872e40037256779cb94e5eab5fbbff25b11e",
    "git_blob_sha": "0d7d9ca5d2a81d108acf237eca96bc12029ed2dd"
  },
  "endpoint": {
    "name": "fixed_fejer_frequency_normal_lift.py",
    "bytes": 98459,
    "sha256": "60769d4999af17f6dc904400e414e3f34ec1000bd84529ad168dca67f6889b5f",
    "git_blob_sha": "2fca2cd110ea329788e8cfe1d18984a5c8717cfc"
  },
  "root_packets": {
    "name": "fixed_fejer_frequency_root_packets.py",
    "bytes": 73037,
    "sha256": "767be252b02b0f92ee1a7229881cfa693a2d4e73f48f6a703fe0c21340c59b78",
    "git_blob_sha": "b4dbba342bc412cf91241ce909b0329dc53e1052"
  },
  "analytic_J3_binding": {
    "name": "fixed_fejer_frequency_source_binding.py",
    "bytes": 35685,
    "sha256": "caf16fbc87ef618ddae5ba42616d9bbe136beac6d32487224073ac6958c4d3c0",
    "git_blob_sha": "8a25d59f8a2fa2c818af8d3d17875d1ca5ae8a33"
  },
  "envelope_transfer": {
    "name": "transfer_fixed_fejer_frequency_memory.py",
    "bytes": 84194,
    "sha256": "1d35b2e7231ed5609e066e602f0f4722bb931b89bb9b3acea132cb45cc510bb8",
    "git_blob_sha": "66571893cb9f27a6b830b831e83052d5950059c0"
  },
  "geometry": {
    "name": "so3_fixed_fejer_frequency_geometry.py",
    "bytes": 70658,
    "sha256": "70c083a3cb8925b5e38ace61f646c87ec0204f22743acf3bcb22fcdab9aabe77",
    "git_blob_sha": "877460a2fc4bf5dd4aa3943a46027e606ab7fde4"
  },
  "driver": {
    "name": "fullclosed_fixed_fejer_frequency_so3_qp.py",
    "bytes": 96268,
    "sha256": "fff956cc086c8f69c7de87c2d9117792b6b1d5e1de853e59a992fb67e04b4e51",
    "git_blob_sha": "557e4823a9dd5892699767a55515339ac02c88a1"
  },
  "launcher": {
    "name": "launch_fixed_fejer_frequency_actions.py",
    "bytes": 22336,
    "sha256": "596e137f6e381a2fdbc882a559a30b664c6e985095867535f3b32d7fa61c417c",
    "git_blob_sha": "a2055fd88befd873367c8ea835e30cde41d11820"
  },
  "reader": {
    "name": "read_fixed_fejer_frequency_so3_report.py",
    "bytes": 98354,
    "sha256": "b79c352d11b41de5384016f103c07db7abc2a41bf438ef92fe20b8a9b43e75bb",
    "git_blob_sha": "a84b93ef25817001ef99ec4ee953bf78e4d45658"
  }
};
const SOURCE_REPRODUCER={
  "name": "reproduce_fixed_fejer_frequency_sources.mjs",
  "bytes": 64491,
  "sha256": "4ad186519e8f70303ad1d4d9800edaadf1335f4f420da8605cb3023a3a9f00c8",
  "git_blob_sha": "752f0f98f2394c47373dd89bd842ae6722f3faac",
  "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_frequency_sources.mjs"
};
const OUTPUTS={
  "independent": {
    "name": "fixed-fejer-frequency-M320-independent-complete-ready.json",
    "bytes": 99028,
    "sha256": "1dfa646e1adec414acd8d5ea86f05ec28187831e684ccfb30460a590a2b7fc7b",
    "git_blob_sha": "4d01ce7f102c66b5e8f5284bd633865ad557a31d",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-frequency-M320-independent-complete-ready.json"
  },
  "complete-parent": {
    "name": "fixed-fejer-frequency-M320-complete-parent-complete-ready.json",
    "bytes": 99180,
    "sha256": "6ae70d6f1236255fda6028e1b7edb8db5e900258b5248890fc07970d47707f35",
    "git_blob_sha": "cf27437b77e32fac3c3ed1b7bdc736cff8ffb261",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-frequency-M320-complete-parent-complete-ready.json"
  }
};
const sha256=s=>crypto.createHash('sha256').update(s,'utf8').digest('hex');
function buildReady(parent,mode,runtime,sourceReproducer,parentRecord){
 if(!['independent','complete-parent'].includes(mode))throw Error('Two explicit input modes only');
 const ready=JSON.parse(JSON.stringify(parent)),oldDir='fixed-fejer-immutable-point-first';
 const newDir='fixed-fejer-frequency-M320-'+(mode==='independent'?'independent':'parent')+'-first';
 const replace=v=>typeof v==='string'?v.split(oldDir).join(newDir):Array.isArray(v)?v.map(replace):
  v&&typeof v==='object'?Object.fromEntries(Object.entries(v).map(([k,x])=>[k.split(oldDir).join(newDir),replace(x)])):v;
 ready.steps=replace(ready.steps);
 ready.schema='complete-fixed-fejer-M320-immutable-point-entry-ready-v1';
 ready.executed=false;
 ready.parameter_mode=mode==='independent'?'independent-reference-zero-inclusion':'actual-Fejer-M160-full13-final-zero-inclusion';
 ready.scope=(mode==='independent'
  ?'Complete M160-to-M320 inclusion of the same predeclared fixed Fejer metric from its original reference core/H and all-zero outer rotation. The current run12 M160 peer and all earlier unreturned histories remain explicit obligations; no future final or typed list is invented.'
  :'Complete M160-to-M320 inclusion from a genuinely returned complete 477499/274d Fejer M160 field. Its whole report, all 13 final checkpoint members and complete typed/protected/address history are consumed. No future parent/output identity is filled in.')
  +' The fixed reference remains M160/N2048/J923; all original variables, every new mode, full 32-stage equations, all rows, original numerical budgets and immutable-point closure reuse remain. Current roots, geometry, norm and residuals are read anew. No old computed value or certificate is inherited.';
 ready.original_fixed_target_input_declaration=ready.declared_input_delta;
 delete ready.declared_input_delta;
 ready.declared_frequency_delta={
  same_predeclared_Fejer_mathematical_target:true,reference_M:160,current_M:320,
  reference_N:2048,current_N:2048,reference_J:923,current_J:923,
  all_original_numeric_parameters_except_explicit_current_M_retained_in_order:true,
  full_actual_reference_scalar_chart_seed_Q_gamma_and_tau_retained:true,
  full_current_norm_identity_changes_with_current_layout:true,
  old_saved_Phi_roots_norm_or_certificate_inherited:false,
  all_original_pending_history_responsibilities_retained:true,
  completed_parent_required_only_for_complete_parent_mode:true
 };
 ready.original_parameter_lineage=ready.complete_parameter_origin;
 ready.complete_parameter_origin=JSON.parse(JSON.stringify(parentRecord));
 ready.complete_source_reproducer=JSON.parse(JSON.stringify(sourceReproducer));
 ready.complete_source_sha256=Object.fromEntries(Object.values(runtime).map(r=>[r.name,r.sha256]));
 for(const name of ['fixed_fejer_r690_reference_inputs.py','fixed_fejer_axisymmetric_reference.py',
  'fixed_fejer_supported_meridian_reference.py','fixed_fejer_reference_input_binding.py',
  'complete_fixed_fejer_material_envelope_memory.py']){
  const digest=parent.complete_source_sha256[name];if(!digest)throw Error('Missing whole shared source '+name);
  ready.complete_source_sha256[name]=digest;
 }
 ready.full_runtime_source_role_count=128;
 ready.source_only_status={all_whole_source_hashes_recorded:true,complete_JS_source_forward_and_inverse:true,
  complete_new_runtime_sources:18,original_Fejer_source_role_pairs_retained:110,
  local_Python_AST_or_compile:false,local_scientific_execution:false,
  source_reproduction_is_not_a_scientific_admission_gate:true};
 ready.frequency_inclusion={
  reference_M:160,current_M:320,reference_N:2048,current_N:2048,reference_J:923,current_J:923,
  original_free_size:1333370,current_free_size:2661210,
  original_rotation_angular_size:482,current_rotation_angular_size:962,
  exact_component_slices:[
   {component:'x_odd_sin',original:[0,161],current:[0,161]},
   {component:'y_odd_cos',original:[161,322],current:[321,482]},
   {component:'z_even_sin',original:[322,482],current:[642,802]}],
  original_core_160_and_height_words_retained:true,
  new_current_core_and_rotation_slots_zero_at_inclusion_and_free_afterwards:true,
  fixed_reference_chart_not_extended_or_redefined:true,
  accurate_selected_field_inclusion_requires_compatible_implicit_branch:true,
  floating_field_values_and_working_norm_require_complete_reread:true,
  output_model_identity_sha256:null,output_point_sha256:null,output_final_sha256:null
 };
 ready.complete_unknown_history_responsibility={
  original_explicit_peers:[
   {run:'45909290354/1',source:'cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5'},
   {run:'45929088658/1',source:'95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9'},
   {run:'45943410994/1',source:'ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5'},
   {run:'45972294636/1',source:'c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1'}],
  current_Fejer_peer:{run:'46011377225/1',source:'477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd'},
  mode:mode==='independent'?'all five peers explicitly declared; no unread final or typed rows assumed empty':
   'actual Fejer parent whole history, inherited prior independent origin and all typed rows reread; no separate pending CLI flag in strict mode',
  previous_non_Fejer_material_labels_reinterpreted_as_declared_not_same_physical_s:true,
  future_parent_report_sha256:null,future_parent_final_sha256:null
 };
 const science=ready.steps[0],pure=ready.steps[1];
 science.id='complete-fixed-fejer-frequency-M320-'+(mode==='independent'?'independent':'parent')+'-first-20261127';
 pure.id='actual-fixed-fejer-frequency-M320-'+(mode==='independent'?'independent':'parent')+'-first-20261127';
 science.script='topics/visible-flex-larger-amplitude/scripts/resume_20261126/'+runtime.launcher.name;
 pure.script='topics/visible-flex-larger-amplitude/scripts/resume_20261126/'+runtime.reader.name;
 science.scope=ready.scope;
 pure.scope='Complete pure source/model/layout and actual same-Fejer input attribution; preserve every original snapshot, derivative/cache policy, immutable packet and complete typed/protected history. No F/J/root computation and no future identity is synthesized.';
 const i=science.args.indexOf('--angles');
 if(i<0||science.args[i+1]!=='2048'||science.args.includes('--current-modes'))throw Error('Complete fixed N2048 inputs');
 science.args.splice(i+2,0,'--current-modes','320');
 const removed=[];
 if(mode==='independent'){
  science.args.push('--pending-parallel-envelope-run','46011377225/1',
   '--pending-parallel-envelope-source','46011377225/1=477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd');
 }else{
  const next=[];
  for(let j=0;j<science.args.length;j++){
   const token=science.args[j];
   if(token==='--independent-envelope-branch'){removed.push([token]);continue;}
   if(['--pending-parallel-envelope-run','--pending-parallel-envelope-source'].includes(token)){
    if(j+1>=science.args.length)throw Error('Missing original peer value');
    removed.push([token,science.args[++j]]);continue;
   }
   next.push(token);
  }
  science.args=next;
  const report='{work}/fixed-fejer-immutable-point-first/report.json';
  science.args.push('--material-envelope-parent-report',report,
   '--material-envelope-seed-report',report,
   '--material-envelope-seed-checkpoint','{work}/fixed-fejer-immutable-point-first/final.npz',
   '--manifest',report);
 }
 ready.input_mode_parameter_correspondence={
  whole_original_ready:JSON.parse(JSON.stringify(parentRecord)),
  whole_original_science_argv_count:parent.steps[0].args.length,
  whole_current_science_argv_count:science.args.length,
  whole_original_pure_argv_count:parent.steps[1].args.length,
  whole_current_pure_argv_count:pure.args.length,
  removed_only_explicit_independent_mode_tokens:removed,
  no_numeric_budget_flag_removed_or_changed:true,
  complete_original_summary_and_all_48_progress_selectors_retained:true
 };
 const sciencePath=newDir+'/report.json',purePath='postprocess/'+newDir+'-readout.json';
 if(Object.keys(science.summary).length!==1||!science.summary[sciencePath]||
    Object.keys(pure.summary).length!==1||!pure.summary[purePath])throw Error('Complete summary destination');
 const common={
  M_reference:'reference_M',M_current:'current_M',M_layout:'frequency_layout_identity_sha256',
  M_input_mode:'frequency_refinement.mode',
  M_current_initial_point:'frequency_refinement.current_full_point_sha256',
  M_original_frozen_point:'frequency_refinement.frozen_original_point_relation.original_full_point_sha256',
  M_current_frozen_point:'frequency_refinement.frozen_original_point_relation.current_full_point_sha256',
  M_old_values_inherited:'frequency_refinement.old_values_roots_norm_or_certificates_inherited',
  M_all_original_variables:'frequency_refinement.all_original_free_variables_retained',
  M_all_new_modes_explicit:'frequency_refinement.all_new_mode_initialization_explicit'
 };
 for(const summary of [science.summary[sciencePath],pure.summary[purePath]]){
  for(const[k,v]of Object.entries(common)){if(k in summary)throw Error('Selector collision '+k);summary[k]=v;}
 }
 Object.assign(science.summary[sciencePath],{
  M_current_variable_count:'original_variables',
  M_original_variable_count:'frequency_layout_definition.original_free_size',
  M_current_layout_variable_count:'frequency_layout_definition.current_free_size',
  M_current_norm_identity:'coordinate_norm.norm_identity_sha256'});
 Object.assign(pure.summary[purePath],{
  M_current_variable_count:'frequency_refinement_binding.layout.current_free_size',
  M_original_variable_count:'frequency_refinement_binding.layout.original_free_size',
  M_current_norm_identity:'coordinate_norm.norm_identity_sha256',
  M_exact_inclusion_branch_responsibility:'frequency_refinement_binding.exact_selected_field_inclusion_requires_compatible_implicit_branch'});
 return ready;
}
function readFull(directory){
 const raw=fs.readFileSync(path.join(directory,INPUT.name)),text=raw.toString('utf8');
 if(!Buffer.from(text,'utf8').equals(raw)||raw.length!==INPUT.bytes||sha256(text)!==INPUT.sha256)
  throw Error('The entire original Fejer plan changed');
 return JSON.parse(text);
}
function main(argv){
 const options={};
 for(let i=0;i<argv.length;i+=2){
  if(!['--parameter-directory','--generated-directory'].includes(argv[i])||argv[i+1]===undefined||options[argv[i]])
   throw Error('Use both complete directory options exactly once');
  options[argv[i]]=path.resolve(argv[i+1]);
 }
 const directory=options['--parameter-directory'],out=options['--generated-directory'];
 if(!directory||!out||directory===out||out.startsWith(directory+path.sep)||fs.existsSync(out))
  throw Error('Keep the original parameters and choose a separate fresh output directory');
 const parent=readFull(directory),items=[];
 for(const[mode,wanted]of Object.entries(OUTPUTS)){
  const value=buildReady(parent,mode,RUNTIME,SOURCE_REPRODUCER,INPUT),text=JSON.stringify(value)+'\n';
  if(Buffer.byteLength(text)!==wanted.bytes||sha256(text)!==wanted.sha256)
   throw Error('Complete reproduced plan differs: '+mode);
  items.push({name:wanted.name,text});
 }
 readFull(directory);
 fs.mkdirSync(out,{recursive:true});
 for(const item of items)fs.writeFileSync(path.join(out,item.name),item.text,{encoding:'utf8',flag:'wx'});
 console.log(JSON.stringify({complete:true,complete_plans:2,all_original_numerical_budgets_retained:true,
  independent_reference_and_actual_full13_parent_modes_distinct:true,
  scientific_execution:false,scientific_admission_gate:false}));
}
if(path.resolve(process.argv[1]||'')===fileURLToPath(import.meta.url))main(process.argv.slice(2));
