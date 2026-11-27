#!/usr/bin/env node
/** Complete parameter-only reproduction. No scientific module or command is run.
 * The two whole original plans are retained as immutable construction inputs.
 * Every argument and original selector survives; only declared M/layout/source,
 * fresh output names and explicit additional M summaries are changed.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const INPUTS={
  "independent": {
    "name": "run10-immutable-point-independent-complete-ready.json",
    "bytes": 91753,
    "sha256": "9948e5db970cea85d7b176a14ec1dd8397c80a3b2bc90069f76ac14f1e938f0c",
    "git_blob_sha": "cc25cd7dc39c14deb69e1e0b399ef160b7df51d4"
  },
  "complete-parent": {
    "name": "run10-immutable-point-complete-parent-complete-ready.json",
    "bytes": 92231,
    "sha256": "8cb06ff176d7bd06818bb4d0892bbf10769a9c7f2deacac5f9d2cbfec695b4e1",
    "git_blob_sha": "12419ff99a2677056da9ea11efe024b18e6237fb"
  }
};
const OUTPUTS={
  "independent": {
    "name": "run10-frequency-M320-immutable-independent-complete-ready.json",
    "bytes": 96766,
    "sha256": "8e1e4fe0daf726e67a7f1e198ed3c5d83b0e1c6b12624b9f5d0f26336e87f54d"
  },
  "complete-parent": {
    "name": "run10-frequency-M320-immutable-complete-parent-complete-ready.json",
    "bytes": 97235,
    "sha256": "9cf8e590d679ed57e21bf3282e6060a264e7d772584d16094b21b7edd1243504"
  }
};
const RUNTIME={
  "closure_values": {
    "name": "run10_frequency_immutable_point_closure_values.py",
    "sha256": "e87044f0b0a51c9552f3f4028617a433c661e73b6a4507a6edb5ddbab7a877fb",
    "bytes": 59808
  },
  "analytic_J3": {
    "name": "run10_frequency_immutable_point_stage_jacobian.py",
    "sha256": "3f351c6b0aa80ff025e5714f8dcbf67cba870e5e9c45b9ad80b61198e5fa00ed",
    "bytes": 25743
  },
  "analytic_frame": {
    "name": "run10_frequency_immutable_point_normal_frame.py",
    "sha256": "83f864898f1ed0ebd45f02aafa354b084978e9e623816d1b6c52777964b149c4",
    "bytes": 47290
  },
  "frame_C1": {
    "name": "run10_frequency_immutable_point_frame_c1.py",
    "sha256": "fbe2f08578c6ea21c1e481e8f37b9ff973838e841329e20d87fa53753def96aa",
    "bytes": 37361
  },
  "stage_matrices": {
    "name": "run10_frequency_immutable_point_stage_matrices.py",
    "sha256": "93944b0a344e9d155477b874dc215cc104e616e74bcee536609484e1cddc8168",
    "bytes": 47791
  },
  "adjacent_matrices": {
    "name": "run10_frequency_immutable_point_adjacent_matrices.py",
    "sha256": "2331d3a43188b39eeb3522094af1351ca8df46fe0820cf65597cb04b8d19c40c",
    "bytes": 36766
  },
  "reference_calibration": {
    "name": "run10_frequency_immutable_point_calibration.py",
    "sha256": "61ad9a9e782c0fd67bf83887d8414968946e8543baac773dcc628419f0248992",
    "bytes": 12374
  },
  "endpoint": {
    "name": "so3_run10_frequency_immutable_point_normal_lift.py",
    "sha256": "a53b2ad03c1c5ba81a0392c6fe7bd08076f6e8f3f11e64f7e997f8319bedc8aa",
    "bytes": 98516
  },
  "root_packets": {
    "name": "immutable_run10_frequency_root_packets.py",
    "sha256": "bdc6e3c714f919deb27ac72400a2d3391cd288a3d089d5baaaaa6eac17759b2f",
    "bytes": 72379
  },
  "analytic_J3_binding": {
    "name": "run10_frequency_immutable_point_source_binding.py",
    "sha256": "1cf73abf9170964d194b1963c0fb54839c9326bb509510eee04303746f6fa1f8",
    "bytes": 38000
  },
  "envelope_transfer": {
    "name": "transfer_run10_frequency_immutable_point_memory.py",
    "sha256": "952790e603606e1efeff10c89580383567e7e645524a4601b68dde1bbe09207b",
    "bytes": 82837
  },
  "geometry": {
    "name": "so3_run10_frequency_immutable_point_geometry.py",
    "sha256": "eac5997e6bc27d4b510a2933e0d2c3c4bc73d37c9316a77bcf257df9f45e9aa5",
    "bytes": 70768
  },
  "driver": {
    "name": "fullclosed_run10_frequency_immutable_point_so3_qp.py",
    "sha256": "1ea2b362cb714a37daa44d8eec9a67eba355b9cb555f07fb465c1cb056f794bb",
    "bytes": 91975
  },
  "launcher": {
    "name": "launch_run10_frequency_immutable_point_actions.py",
    "sha256": "6894d7d1b057d13daa8d38d82522bfb8e36626b0372d64c067290fdbfdb3b326",
    "bytes": 22348
  },
  "reader": {
    "name": "read_run10_frequency_immutable_point_so3_report.py",
    "sha256": "24939deed9a2b24732608a182d039751f8259f16f4d7f20acac40115f218c08b",
    "bytes": 98133
  },
  "meridian": {
    "name": "so3_frequency_refined_smooth_triangle_meridian_operator.py",
    "sha256": "41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2",
    "bytes": 42982
  },
  "new_moment_input": {
    "name": "frequency_refined_smooth_triangle_literal_zero_moment_input.py",
    "sha256": "bde3fd4cab72c6296472928cd9760ad88063462ac5872c2c88addd75958d2971",
    "bytes": 31068
  },
  "frequency_layout": {
    "name": "so3_frequency_refinement_layout.py",
    "sha256": "ce188ae4bdf1ccecfbf9549897284e8dc44f4722e04e974c7a0cd045c78a3a27",
    "bytes": 13582
  }
};
const SOURCE_REPRODUCER={
  "name": "reproduce_run10_frequency_immutable_point_sources.mjs",
  "bytes": 34080,
  "sha256": "f5fbdd81ab53a234aaa930978236c29eafddfd5ddbd90982674146ce8bf03944",
  "git_blob_sha": "69fb8191323f4d1bde297a2ecf3cf8a34ce9cc3a"
};
const hash=s=>crypto.createHash('sha256').update(s,'utf8').digest('hex');

function buildM10Ready(parent,mode,runtime,sourceReproducer) {
 const ready=JSON.parse(JSON.stringify(parent));
 const oldDir=mode==="independent"?"run10-immutable-point-independent-first":"run10-immutable-point-parent-first";
 const newDir=mode==="independent"?"run10-frequency-M320-immutable-independent-first":"run10-frequency-M320-immutable-parent-first";
 const replace=v=>typeof v==="string"?v.split(oldDir).join(newDir):Array.isArray(v)?v.map(replace):v&&typeof v==="object"?Object.fromEntries(Object.entries(v).map(([k,x])=>[k.split(oldDir).join(newDir),replace(x)])):v;
 ready.steps=replace(ready.steps);
 ready.schema="complete-run10-M320-immutable-point-entry-ready-v1";
 ready.executed=false;
 ready.parameter_mode=mode==="independent"?"independent-reference-zero-inclusion":"actual-c3dc-full13-final-zero-inclusion";
 ready.scope=(mode==="independent"
  ?"Complete M160-to-M320 inclusion at the same actually frozen run10 target, from its original reference core/H and all-zero outer rotation. Every old free coordinate remains, and every newly added current core and rotation coordinate is free. The original c3dc peer and all older unknown histories remain explicit obligations."
  :"Complete M160-to-M320 inclusion from the genuinely returned c3dc/2efa M160 complete final. The original full report, all 13 checkpoint members, complete typed/protected history and exact old/new model relationship are consumed. Future report/checkpoint/point identities remain null until that actual complete input exists.")
  +" The fixed reference stays M160/N2048/J923, with all original rows, norms and numerical budgets, full 32-stage equations, packet capture and immutable-point value reuse. No prior physical values, roots, norm statistics, accepted Phi or certificate are inherited.";
 ready.source_sha256=Object.fromEntries(Object.values(runtime).map(r=>[r.name,r.sha256]));
 ready.source_sha256["complete_material_envelope_memory_public_run10.py"]="f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba";
 ready.original_immutable_point_ready={name:mode==="independent"?"run10-immutable-point-independent-complete-ready.json":"run10-immutable-point-complete-parent-complete-ready.json",
  sha256:mode==="independent"?"9948e5db970cea85d7b176a14ec1dd8397c80a3b2bc90069f76ac14f1e938f0c":"8cb06ff176d7bd06818bb4d0892bbf10769a9c7f2deacac5f9d2cbfec695b4e1",
  bytes:mode==="independent"?91753:92231,git_blob_sha:mode==="independent"?"cc25cd7dc39c14deb69e1e0b399ef160b7df51d4":"12419ff99a2677056da9ea11efe024b18e6237fb"};
 ready.complete_source_reproducer={name:sourceReproducer.name,bytes:sourceReproducer.bytes,sha256:sourceReproducer.sha256,git_blob_sha:sourceReproducer.git_blob_sha};
 ready.source_only_checks={whole_sources_constructed_and_SHA256_checked:true,
  all_output_sources_below_100000_bytes:true,complete_runtime_sources:18,
  independent_new_runtime_sources:15,whole_shared_original_runtime_sources:3,
  complete_source_role_count:107,all_original_75_current_run10_roles_retained:true,
  all_90_immutable_point_family_source_pairs_retained:true,
  complete_JS_text_forward_all18_and_inverse_all15:true,
  local_AST_or_compile_performed:false,scientific_imports_or_F_J_roots_or_fixtures_executed:false,
  reproducibility_utility_is_not_a_scientific_admission_gate:true};
 ready.frequency_inclusion={reference_M:160,current_M:320,reference_N:2048,current_N:2048,
  reference_J:923,current_J:923,old_free_size:1333370,current_free_size:2661210,
  old_rotation_angular_size:482,current_rotation_angular_size:962,
  exact_component_slices:[{component:"x_odd_sin",old:[0,161],current:[0,161]},
   {component:"y_odd_cos",old:[161,322],current:[321,482]},
   {component:"z_even_sin",old:[322,482],current:[642,802]}],
  new_slots_are_zero_only_at_inclusion:true,all_new_slots_are_free_in_current_solves:true,
  complete_reference_seed_metric_chart_radial_and_angular_observer_retained:true,
  current_full_norm_identity_and_initial_physics_require_actual_reread:true,
  accurate_selected_field_inclusion_requires_compatible_implicit_branch:true,
  original_computed_values_roots_geometry_or_certificate_inherited:false,
  M320_output_current_model_identity_sha256:null,M320_output_point_sha256:null,M320_output_final_sha256:null};
 ready.same_complete_run10_frozen_target_retained=true;
 ready.predecessor_target_source_and_model_are_not_changed_by_point_storage=true;
 ready.input_mode_delta={original_immutable_point_mode_delta:ready.input_mode_delta,
  additional_explicit_current_modes_tokens:["--current-modes","320"],
  all_original_numeric_parameters_other_than_current_M_retained_in_order:true,
  complete_original_pending_or_inherited_unknown_histories_retained:true,
  old_same_reference_norm_parameters_retained_but_current_norm_identity_is_new:true};
 const science=ready.steps[0],pure=ready.steps[1];
 science.id="complete-run10-frequency-M320-immutable-"+(mode==="independent"?"independent":"parent")+"-first-20261127";
 pure.id="actual-run10-frequency-M320-immutable-"+(mode==="independent"?"independent":"parent")+"-first-20261127";
 science.script="topics/visible-flex-larger-amplitude/scripts/resume_20261126/"+runtime.launcher.name;
 pure.script="topics/visible-flex-larger-amplitude/scripts/resume_20261126/"+runtime.reader.name;
 science.scope=ready.scope;
 pure.scope="Complete pure source/model/layout and actual c3dc inclusion attribution. Retain every original current-point diagnostic, six cache/derivative policies, all immutable packets and complete typed/permanent history. Read actual final bytes only when present; no F/J/root/array algebra or future identity is synthesized.";
 const i=science.args.indexOf("--angles");if(i<0||science.args[i+1]!=="2048")throw new Error("complete N2048 input");
 science.args.splice(i+2,0,"--current-modes","320");
 const sciencePath=newDir+"/report.json",purePath="postprocess/"+newDir+"-readout.json";
 if(Object.keys(science.summary).length!==1||!science.summary[sciencePath])throw new Error("scientific summary path");
 if(Object.keys(pure.summary).length!==1||!pure.summary[purePath])throw new Error("pure summary path");
 const common={
  M_reference:"reference_M",M_current:"current_M",M_layout:"frequency_layout_identity_sha256",
  M_input_mode:"frequency_refinement.mode",
  M_current_initial_point:"frequency_refinement.current_full_point_sha256",
  M_original_frozen_point:"frequency_refinement.frozen_original_point_relation.original_full_point_sha256",
  M_current_frozen_point:"frequency_refinement.frozen_original_point_relation.current_full_point_sha256",
  M_old_values_inherited:"frequency_refinement.old_values_roots_norm_or_certificates_inherited",
  M_all_original_variables:"frequency_refinement.all_original_free_variables_retained",
  M_all_new_modes_explicit:"frequency_refinement.all_new_mode_initialization_explicit"
 };
 for(const summary of [science.summary[sciencePath],pure.summary[purePath]]){
  for(const[k,v]of Object.entries(common)){if(k in summary)throw new Error("selector collision");summary[k]=v;}
 }
 Object.assign(science.summary[sciencePath],{
  M_current_variable_count:"original_variables",
  M_original_variable_count:"frequency_layout_definition.original_free_size",
  M_current_layout_variable_count:"frequency_layout_definition.current_free_size",
  M_current_norm_identity:"coordinate_norm.norm_identity_sha256"});
 Object.assign(pure.summary[purePath],{
  M_current_variable_count:"frequency_refinement_binding.layout.current_free_size",
  M_original_variable_count:"frequency_refinement_binding.layout.original_free_size",
  M_current_norm_identity:"coordinate_norm.norm_identity_sha256",
  M_exact_inclusion_branch_responsibility:"frequency_refinement_binding.exact_selected_field_inclusion_requires_compatible_implicit_branch"});
 return ready;
}

function readFull(directory,record){
 const raw=fs.readFileSync(path.join(directory,record.name));
 const source=raw.toString('utf8');
 if(!Buffer.from(source,'utf8').equals(raw)||raw.length!==record.bytes||hash(source)!==record.sha256)
  throw new Error('The complete original plan changed: '+record.name);
 return {source,document:JSON.parse(source)};
}
function main(argv){
 const opts={};
 for(let i=0;i<argv.length;i+=2){
  if(!['--parameter-directory','--generated-directory'].includes(argv[i])||argv[i+1]===undefined||opts[argv[i]])
   throw new Error('Use both declared directory options once');
  opts[argv[i]]=path.resolve(argv[i+1]);
 }
 const input=opts['--parameter-directory'],out=opts['--generated-directory'];
 if(!input||!out||out===input||out.startsWith(input+path.sep)||fs.existsSync(out))
  throw new Error('Keep both complete original parameter files and choose a separate fresh output directory');
 const generated=[];
 for(const[mode,rec]of Object.entries(INPUTS)){
  const parent=readFull(input,rec).document,ready=buildM10Ready(parent,mode,RUNTIME,SOURCE_REPRODUCER);
  const source=JSON.stringify(ready)+'\n',expected=OUTPUTS[mode];
  if(Buffer.byteLength(source)!==expected.bytes||hash(source)!==expected.sha256)
   throw new Error('The complete reproduced plan differs: '+mode);
  generated.push({name:expected.name,source,mode});
 }
 fs.mkdirSync(out,{recursive:true});
 for(const item of generated)fs.writeFileSync(path.join(out,item.name),item.source,{encoding:'utf8',flag:'wx'});
 for(const rec of Object.values(INPUTS))readFull(input,rec);
 console.log(JSON.stringify({complete:true,complete_plans:2,scientific_execution:false,
   all_original_numeric_parameters_retained_except_explicit_current_M:true,
   source_or_parameter_reproduction_is_not_a_scientific_admission_gate:true}));
}
if(path.resolve(process.argv[1]||'')===fileURLToPath(import.meta.url))main(process.argv.slice(2));
