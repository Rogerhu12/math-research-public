#!/usr/bin/env node
/**
 * Complete fixed-Fejer mesh parameter derivation from whole published inputs.
 * Text and JSON only. No field/root/mesh execution or scientific admission gate.
 */
import {readFile,stat,mkdir,writeFile} from "node:fs/promises";
import {resolve,join} from "node:path";
import {createHash} from "node:crypto";
const META={"runtime":{"input":{"role":"input","name":"fixed_fejer_same_field_mesh_input.py","bytes":73133,"sha256":"ad809cb428b7cdd6f3fe082a0057739ff191aefe4abb113e4595fe5e618f0036","git_blob_sha":"9cfe9ac9db4760fe83775b2a51da25965670520c","path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_same_field_mesh_input.py"},"arithmetic":{"role":"arithmetic","name":"fixed_fejer_complete_phase_mesh_arithmetic.py","bytes":39436,"sha256":"80116a4bcfa2752274cece1148420cdce5c489faba3a8a7c0e92c0f6a8d058e4","git_blob_sha":"57c2c563785dab3a1148645225106ca5860e2e2f","path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_phase_mesh_arithmetic.py"},"entry":{"role":"entry","name":"fixed_fejer_complete_same_field_phase_meshes.py","bytes":48348,"sha256":"2acc9b4ee82623603d05f6a0951f01a0a3f92a4a640ca69b9f75814a45e5ab2d","git_blob_sha":"96b9a32372704d5e58e53e72544d4abd40b4c536","path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_same_field_phase_meshes.py"},"reader":{"role":"reader","name":"read_fixed_fejer_same_field_phase_mesh_report.py","bytes":22120,"sha256":"fde5c17f6b0a65f99d05f3ec0973571121899ce8844e93228cc68118975cb9b2","git_blob_sha":"cd9dfc25d025350d9d175570532d4f011a951408","path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_same_field_phase_mesh_report.py"}},"upper_ready":{"name":"fixed-fejer-immutable-point-complete-run12-ready.json","bytes":92380,"sha256":"ab5c00086e21faaa5017ea469c4a63e7d389ecc3019b03a28e46b9daaa129578","git_blob_sha":"13eea0c110a7d98bef3736d1585aa57584402ac3","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-immutable-point-complete-run12-ready.json"},"maker":{"name":"fixed_fejer_r690_reference_inputs.py","path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py","bytes":39375,"sha256":"89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60","git_blob_sha":"7b3e12203c15040e07c7dc9cc4f2c20c12d7d566"},"reference":{"name":"fixed_fejer_axisymmetric_reference.py","path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py","bytes":60335,"sha256":"e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb","git_blob_sha":"8ad0794ebf0daab9a278c5ea1de784e93b64fd8c"},"fixed_input_binding":{"name":"fixed_fejer_reference_input_binding.py","path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_reference_input_binding.py","bytes":25672,"sha256":"3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f","git_blob_sha":"5eab3f96cb8b1bc245f4de33dc2041cf25d22094"},"accurate_input":{"name":"fixed_fejer_normal_packet_accurate_field_input.py","path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_normal_packet_accurate_field_input.py","bytes":32991,"sha256":"1e5101d7bd08a8b3787b6eaa699c915a9e8bd173d365233c7be90f1aee1b3f3f","git_blob_sha":"46ee6fd8157265253259a642844783ea4cd712bb"},"closed_source":{"name":"fixed_fejer_complete_closed_phase_grip_evidence.py","path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_closed_phase_grip_evidence.py","bytes":71420,"sha256":"d606055d1b247d8354ac320bc28a0f40f4b00cbf1ff530a9b6bb2e80dec80bb9","git_blob_sha":"33d9ee5b22c3e8bb5a92262ca7af7b89f20bb78b"},"closed_note":{"name":"2026-11-27-fixed-fejer-closed-phase-grip-source-adapter.md","path":"topics/visible-flex-larger-amplitude/notes/2026-11-27-fixed-fejer-closed-phase-grip-source-adapter.md","bytes":15093,"sha256":"16c15c597359b3017c9e050b5ddef94950d508e88a9c05fa726300cd129b726e","git_blob_sha":"234e60bc7bbf7f286c77ed4e6f78cdf1d935c79c"},"parents":{"final":{"name":"run10-complete-same-field-phase-mesh-final-ready.json","bytes":36220,"sha256":"0cf45a65dee71b08a0a5f53e202aac0382984b6da7193b910023ab642a00a8ae","git_blob_sha":"0ef28c52958ed6bf15b7ecb9611ce71a936e13b8","path":"topics/visible-flex-larger-amplitude/computations/run10-complete-same-field-phase-mesh-final-ready.json"},"packet":{"name":"run10-complete-same-field-phase-mesh-packet-ready.json","bytes":36367,"sha256":"23ef79d18fd9dffcc9d028a869d474abf1a71258216f7d720ceb30481576f136","git_blob_sha":"fd6b1c0f9f29092d906f24e8b4dcf12c182c77a0","path":"topics/visible-flex-larger-amplitude/computations/run10-complete-same-field-phase-mesh-packet-ready.json"}}};
const EXPECTED={"final":{"name":"fixed-fejer-complete-same-field-phase-mesh-final-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-complete-same-field-phase-mesh-final-ready.json","bytes":50869,"sha256":"609e737dd835d7cdb3101f38f2797568e3fb8bbfcd88a1ea513bc6dae7e2aa5a","git_blob_sha":"ea9664dd4b47e92bcda5b053b8975a7096c2fdd8"},"packet":{"name":"fixed-fejer-complete-same-field-phase-mesh-packet-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-complete-same-field-phase-mesh-packet-ready.json","bytes":50836,"sha256":"f3768a3a0ccb3da29045107072a363ef6d7fae761e4596e3de4efb2448e31b25","git_blob_sha":"e96662325c7122a6b298558a8e434b6cce890905"}};
function buildMeshReady(parent,mode,upper,meta,sourceRoles){
 const copy=x=>JSON.parse(JSON.stringify(x));
 const oldOut="run10-same-field-phase-mesh-"+mode+"-v1",newOut="fixed-fejer-same-field-phase-mesh-"+mode+"-v1";
 const oldPoint="run10-detached-closure-values-first",newPoint="fixed-fejer-immutable-point-first";
 const pairs=[[oldOut,newOut],[oldPoint,newPoint],["axisymmetric-R690-reference-v2-first/reference.npz","fixed-fejer-reference/reference.npz"]];
 function relabel(v){
  if(typeof v==="string"){for(const[a,b]of pairs)v=v.split(a).join(b);return v;}
  if(Array.isArray(v))return v.map(relabel);
  if(v&&typeof v==="object")return Object.fromEntries(Object.entries(v).map(([k,x])=>[relabel(k),relabel(x)]));return v;
 }
 const r=copy(parent);
 Object.assign(r,{schema:"complete-fixed-fejer-same-field-closed-phase-mesh-parameters-v1",executed:false,
 actual_original_scientific_run:"46011377225/1",actual_point_sha256:null,
 actual_parent_report_sha256:null,actual_parent_checkpoint_sha256:null,
 actual_mesh_or_refinement_result_available:false,fixed_target_definition_identity_sha256:null,
 actual_current_reference_model_identity_sha256:null,complete_actual_input_binding_sha256:null,
 mathematical_target_recipe_identity_sha256:null,identities_consumed_from_complete_actual_fixed_binding:true,
 prepared_input_or_live_progress_is_a_field_input:false,previous_target_or_current_point_certificates_inherited:false,
 full_scientific_source_role_count:110,full_mesh_source_role_count:117});
 r.source_sha256=Object.fromEntries(Object.values(meta.runtime).map(x=>[x.name,x.sha256]));
 r.complete_runtime_source_records=Object.values(meta.runtime);
 const extraRoles=new Set(["mesh_input","mesh_arithmetic","original_fixed_fejer_driver","original_fixed_fejer_reader","original_fixed_fejer_launcher","complete_accurate_input_scope","optional_closed_phase_source"]);
 const originalRoles=Object.fromEntries(Object.entries(sourceRoles).filter(([key])=>!extraRoles.has(key)));
 if(Object.keys(originalRoles).length!==110)throw new Error("complete110");
 r.complete_original_scientific_parameter_source={...meta.upper_ready,
 original_script:upper.steps[0].script,original_complete_argv:copy(upper.steps[0].args),
 original_complete_source_sha256_by_role:Object.fromEntries(Object.entries(originalRoles).map(([k,v])=>[k,v[1]])),
 actual_runtime_command_is_read_whole_without_argument_elision:true,
 actual_command_required_path:"{work}/"+newPoint+"-command.json",
 original_constructor_body_bytes:8924,
 original_constructor_body_sha256:"d40c3b7e330ea6850997d13891dd17d95b80d3c33e99c9912aa4b5f1da0f3885",
 all_original_pending_source_declarations_preserved_from_actual_command:true,
 actual_input_body_from_published_original_driver:true,same_source_path_not_assumed_across_followups:true,
 complete_original_source_path_records_and_whole_current_copy_equality_required:true};
 r.complete_field_scope={...r.complete_field_scope,predeclared_target_recipe_source:meta.maker,
 immutable_reference_context_source:meta.reference,complete_actual_fixed_input_binder:meta.fixed_input_binding,
 complete_actual_field_input_scope:meta.accurate_input,
 complete_new_reference_and_math_and_target_identities_are_distinct:true,
 no_old_run10_chart_or_model_or_binding_constant_used_as_current:true};
 r.point_source_mode=mode;
 r.scope=mode==="final"?
 "Consume only the actually returned complete fixed Fejer scientific report and its genuine full thirteen-member final checkpoint. Reconstruct all original free words, numerical policies and fixed reference, and use this one point for every complete closed mesh and physical time. A complete existing same-point immutable root snapshot is reused when present; missing final is an input failure and never a reset to initial or progress.":
 "Consume only a genuine complete required-angle immutable point snapshot in captured fixed Fejer scientific report bytes, selected explicitly or as the latest actual complete snapshot. Preserve every point word, every recorded angle and all 32 stage records. It can be a trial/cache point; no acceptance or final success is inferred. Missing snapshot is an input failure, never initial/progress substitution.";
 r.optional_complete_closed_phase_evidence={enabled_by_default:false,required_to_generate_meshes:false,
 source:meta.closed_source,proof_note:meta.closed_note,
 report_path:"{work}/fixed-fejer-complete-closed-phase-grip-v1/report.json",
 actual_report_sha256:null,actual_selected_snapshot_identity_sha256:null,
 argument_if_attaching_the_actual_complete_report:["--closed-phase-report","{work}/fixed-fejer-complete-closed-phase-grip-v1/report.json"],
 optional_expected_report_sha256_flag:"--expected-closed-phase-report-sha256",
 exact_final_main_complete_status_and_all_records_required:true,same_actual_point_model_target_and_snapshot_required:true,
 prior_uncommitted_sidecar_not_accepted:true,original_source_paths_reread_and_only_byte_identical_current_copies_allowed:true,
 absent_evidence_keeps_flags_false_and_mesh_generation_continues:true,accurate_field_claims_do_not_certify_working_mesh_words:true};
 r.steps=relabel(parent.steps);
 r.steps[0].id="complete-fixed-fejer-same-field-phase-mesh-"+mode+"-20261127";
 r.steps[1].id="actual-fixed-fejer-same-field-phase-mesh-"+mode+"-20261127";
 r.steps[0].script=meta.runtime.entry.path;r.steps[1].script=meta.runtime.reader.path;
 r.steps[0].scope=r.scope;
 r.steps[1].scope="Pure stdlib full source/report/point/NPY/PLY-byte reader, including the complete fixed Fejer six-input binding and optional exact same-snapshot final closed proof. It calls no field, root, chart or mesh and retains all incomplete status.";
 const extras=["optional_closed_evidence_provided","optional_closed_same_snapshot_bound","optional_accurate_closed_C2",
 "optional_accurate_all_phase_embedding","optional_accurate_reach_standard","optional_accurate_delta_hold_stronger","optional_evidence_pays_working_mesh_error"];
 for(const[i,path]of[[0,newOut+"/scalar-summary.json"],[1,"postprocess/"+newOut+"-readout.json"]])
  for(const key of extras)r.steps[i].summary[path][key]=key;
 const completeProgress=copy(r.steps[0].progress_summary);
 const live=r.steps[0].progress_summary[newOut+"/scalar-summary.json"];
 if(live.complete!=="complete"||live.meshes!=="actual_mesh_files")throw new Error("exact old progress");
 delete live.complete;delete live.meshes;
 if(Object.values(r.steps[0].progress_summary).reduce((n,v)=>n+Object.keys(v).length,0)!==48)throw new Error("48");
 r.progress_publication_contract={controller_maximum_scalar_selectors:48,
 complete_original_50_selector_mapping_preserved:completeProgress,active_readonly_selectors:48,
 original_complete_and_mesh_count_fields_retained_in_all_full_final_summaries:true,
 active_observer_only_omitted_redundant_final_summary_fields:["complete","actual_mesh_files"],
 numerical_parameters_or_returned_full_records_changed:false,no_progress_value_accepted_as_a_scientific_snapshot:true};
 r.output_boundary={...r.output_boundary,strict_five_megabyte_limit_is_per_complete_rendering_preview:true,
 full_scientific_meshes_not_truncated_to_preview_limit:true};
 r.complete_source_derivation={original_mesh_commit:"91213be817889b7006848b4d251dd06cc77c2a50",
 complete_original_parameter_file:meta.parents[mode],source_only_text_operations:true,
 local_AST_or_compile_or_scientific_execution:false,source_reproducer_is_not_an_admission_gate:true};
 return r;
}

const digest=raw=>createHash("sha256").update(raw).digest("hex");
async function readBound(directory,record){
 const path=join(directory,record.name);
 if((await stat(path)).size!==record.bytes)throw new Error("Whole source/parameter size changed: "+path);
 const raw=await readFile(path);
 if(digest(raw)!==record.sha256)throw new Error("Whole source/parameter SHA changed: "+path);
 return raw.toString("utf8");
}
const words=process.argv.slice(2),options={};
for(let i=0;i<words.length;i+=2){
 if(!words[i].startsWith("--")||!words[i+1]||options[words[i]]!==undefined)throw new Error("Use complete paired arguments");
 options[words[i]]=resolve(words[i+1]);
}
const keys=["--parent-parameter-directory","--current-parameter-directory","--current-source-directory","--output-directory"];
if(Object.keys(options).length!==keys.length||keys.some(k=>!options[k]))throw new Error("Required: "+keys.join(" "));
const output=options["--output-directory"];
if(keys.filter(k=>k!=="--output-directory").some(k=>output===options[k]||options[k].startsWith(output+"/")))throw new Error("Use independent parameter output");
const upper=JSON.parse(await readBound(options["--current-parameter-directory"],META.upper_ready));
const texts={};
for(const [role,record]of Object.entries(META.runtime))texts[role]=await readBound(options["--current-source-directory"],record);
const text=texts.entry,marker="SOURCE_PINS = ",at=text.indexOf(marker),end=text.indexOf("\n\n",at);
if(at<0||end<0)throw new Error("Keep the complete literal source table");
const roles=JSON.parse(text.slice(at+marker.length,end));
if(Object.keys(roles).length!==117)throw new Error("Keep all 117 complete source roles");
const prepared={};
for(const mode of ["final","packet"]){
 const parent=JSON.parse(await readBound(options["--parent-parameter-directory"],META.parents[mode]));
 const document=buildMeshReady(parent,mode,upper,META,roles);
 const raw=Buffer.from(JSON.stringify(document,null,2)+"\n","utf8");
 if(raw.length!==EXPECTED[mode].bytes||digest(raw)!==EXPECTED[mode].sha256)throw new Error("Complete derived parameter identity changed");
 prepared[mode]=raw;
}
await mkdir(output,{recursive:true});
for(const mode of ["final","packet"])await writeFile(join(output,EXPECTED[mode].name),prepared[mode],{flag:"wx"});
console.log(JSON.stringify({schema:"complete-fixed-fejer-mesh-parameter-source-reproduction-v1",
 outputs:EXPECTED,complete_original_numerical_and_mesh_parameters_preserved:true,
 old_formal_summary_selectors_preserved:true,full_old_live_selector_map_preserved:true,
 active_readonly_progress_selector_count:48,scientific_execution:false,
 source_reproducer_is_not_an_admission_gate:true}));
