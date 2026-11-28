#!/usr/bin/env node
// Full JSON/source-identity reproduction only. No Python, AST, fixture or science.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';
const CONFIG={
  "repository": "Rogerhu12/math-research-public",
  "topic": "topics/visible-flex-larger-amplitude",
  "prepared_date": "2026-11-28",
  "session": "Astra-larger-e4e2a2bf-20261126",
  "runner": "29",
  "old_namespace": "fixed-fejer-r725-bhalf-first",
  "namespace": "fixed-fejer-r726-bhalf-first",
  "parent_parameter_publication": "f44e6c09210e7b616775a966ce89b03ccda25b9d",
  "current_source_publication": "7acb89983fe616fbba85cef74811625b357942e4",
  "parameter_binding_name": "fixed-fejer-r726-bhalf-complete-parameter-binding.json",
  "science_name": "fixed-fejer-r726-bhalf-science-complete-ready.json",
  "pure_name": "fixed-fejer-r726-bhalf-pure-complete-ready.json",
  "parents": {
    "science": {
      "name": "fixed-fejer-r725-bhalf-science-complete-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r725-bhalf-science-complete-ready.json",
      "bytes": 72545,
      "sha256": "fb33c7620b05193b54e38a39e97f7efc0fa7149bcbc720d04db1c041aeda0d63",
      "git_blob_sha": "ebde4051043cfbf7524244dee27f2e85589a562c"
    },
    "pure": {
      "name": "fixed-fejer-r725-bhalf-pure-complete-ready.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r725-bhalf-pure-complete-ready.json",
      "bytes": 58721,
      "sha256": "29254c1a4a08cbb508266d9ac4c88178a6a7e2b5413428d31461056fe8939ccf",
      "git_blob_sha": "b3d57832327fccecf3afb4f211006125f331e271"
    },
    "binding": {
      "name": "fixed-fejer-r725-bhalf-complete-parameter-binding.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r725-bhalf-complete-parameter-binding.json",
      "bytes": 47684,
      "sha256": "5abc72b77a2eb51064239e49a5e90fcc9fd230fc4883a925e19461ae701ef7eb",
      "git_blob_sha": "b81215714615e663d537f7d0d8c7341aadb453c9"
    },
    "delivery": {
      "name": "fixed-fejer-r725-bhalf-complete-parameter-delivery.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r725-bhalf-complete-parameter-delivery.json",
      "bytes": 19108,
      "sha256": "a02d1140c3cc83b9e70cde8a264e68707db5ef9da49710826a14a099b6eeb8f5",
      "git_blob_sha": "c5edf0dd581dcba4af3d6c8b8c97483d1d089de6"
    },
    "source_binding": {
      "name": "fixed-fejer-r726-current-complete-runtime-binding.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r726-current-complete-runtime-binding.json",
      "bytes": 55517,
      "sha256": "6e5480838f54ecb50ce8baa085ebabed37504a3ba759d1ed958ec28c6d9df059",
      "git_blob_sha": "159d8c56b1b966cf5de5d19bceec68db3630144b"
    },
    "source_delivery": {
      "name": "fixed-fejer-r726-complete-scientific-source-delivery.json",
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r726-complete-scientific-source-delivery.json",
      "bytes": 24238,
      "sha256": "f3e2e6b31fa9b59af013c4a8fc048e55858eb32279638a4f11368cf2dd2917f9",
      "git_blob_sha": "5200b7728c55e192821f0f4f29578bc5d22f4524"
    },
    "peer26": {
      "name": "2026-11-28-run26-complete-r725-cutoff-launch-and-continuation.md",
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run26-complete-r725-cutoff-launch-and-continuation.md",
      "bytes": 59709,
      "sha256": "9308c531a5208aada7876c8549fb2e2c6f15b28b12ff8be0b3ecabf778c5cc6d",
      "git_blob_sha": "db2e8bfe7b8071577f0193dd3862e1e53ebd6f72"
    },
    "peer27": {
      "name": "2026-11-28-run27-complete-r725-five-eighths-launch-and-continuation.md",
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run27-complete-r725-five-eighths-launch-and-continuation.md",
      "bytes": 31932,
      "sha256": "0aba4962e2c3712d407678da4e64a8f7d38053664e7278bd55a4d68750336bb7",
      "git_blob_sha": "ed1a598ba18f06cd4f663265f52fef60510388ea"
    }
  },
  "expected_binding_record": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r726-bhalf-complete-parameter-binding.json",
    "name": "fixed-fejer-r726-bhalf-complete-parameter-binding.json",
    "bytes": 60792,
    "sha256": "3790d0411f81f755048be6e4ccf047001ca140bcc7700bf24ecd010d49432a9a",
    "git_blob_sha": "faebae8df7750c83d572fdbf9328ea9f2c28de1d"
  }
};
const EXPECTED={
  "binding": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r726-bhalf-complete-parameter-binding.json",
    "name": "fixed-fejer-r726-bhalf-complete-parameter-binding.json",
    "bytes": 60792,
    "sha256": "3790d0411f81f755048be6e4ccf047001ca140bcc7700bf24ecd010d49432a9a",
    "git_blob_sha": "faebae8df7750c83d572fdbf9328ea9f2c28de1d"
  },
  "science": {
    "name": "fixed-fejer-r726-bhalf-science-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r726-bhalf-science-complete-ready.json",
    "bytes": 72547,
    "sha256": "0092bace732ba29a36335f21a59597fe42b109687c35f5ff42d8424f4c252544",
    "git_blob_sha": "370dc3064a8b0040a5e352ae5236ee10cd0c9715"
  },
  "pure": {
    "name": "fixed-fejer-r726-bhalf-pure-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r726-bhalf-pure-complete-ready.json",
    "bytes": 58714,
    "sha256": "0998cec08e7196c1e42f3ac32fb711cf5a74ad29a80c245d45d89ec64c9393d4",
    "git_blob_sha": "5b547cea6640c87bc7d2b2008bc5f15ca01c3ceb"
  }
};
const BUILD=(function(){
function build(config,files) {
 const clone=x=>JSON.parse(JSON.stringify(x));
 const c=config,p=files.binding.value,source=files.source_binding.value;
 const ref=(record,pointer)=>({complete_file:clone(record),json_pointer:pointer,whole_file_required:true});
 const pub=r=>({...clone(r),fixed_publication_commit:c.parent_parameter_publication});
 const sourceRec={...clone(c.parents.source_binding),fixed_publication_commit:c.current_source_publication};
 const sourceDel={...clone(c.parents.source_delivery),fixed_publication_commit:c.current_source_publication};
 function remap(value,oldValue,newValue) {
  if(typeof value==='string')return value.split(oldValue).join(newValue);
  if(Array.isArray(value))return value.map(x=>remap(x,oldValue,newValue));
  if(value!==null&&typeof value==='object')return Object.fromEntries(Object.entries(value).map(([k,v])=>[
   k.split(oldValue).join(newValue),remap(v,oldValue,newValue)]));
  return value;
 }
 function jsonBlocks(text) {
  const marker=String.fromCharCode(96).repeat(3);
  return [...text.matchAll(new RegExp(marker+"json\\s*\\n([\\s\\S]*?)\\n"+marker,"g"))].map(x=>JSON.parse(x[1]));
 }
 const blocks26=jsonBlocks(files.peer26.text),blocks27=jsonBlocks(files.peer27.text);
 const official26=blocks26[0],official27=blocks27[1],run26=official26.official_run,run27=official27.run;
 if(String(run26.id)!=='46103106086'||run26.run_attempt!==1
    ||String(run27.id)!=='46105138690'||run27.run_attempt!==1)
  throw new Error('Complete original R725 peer evidence differs');
 const parentDriver=files.delivery.value.complete_immediate_parent_documents.current_source_binding;
 const parentDriverSha=blocks26[5].observations[c.old_namespace+'/actual-mathematical-progress.json'].math_driver;
 if(parentDriverSha!=='e1d3b06875496ba2555d20e2e1e96bfa92c420c15dc7276788160b44fca337cd')
  throw new Error('Actual R725 peer driver is not the complete declared family');
 const peerRecords=[
  {
   run_attempt_key:'46103106086/1',run_id:'46103106086',run_attempt:1,
   declared_driver_source_sha256:parentDriverSha,
   complete_original_evidence:c.parents.peer26,
   complete_original_evidence_scope:'Whole original note including official run/job, both real inputs, all appended own-point observations, missing values and errors; none is a run29 input or conclusion.',
   official_evidence_json_fence_index:0,all_note_blocks_and_prose_retained:true,
   evidence_body_rewritten:false,
   complete_actual_original_science_parameters:pub(c.parents.science),
   complete_actual_original_pure_parameters:pub(c.parents.pure),
   current_role:'external historical evidence and unknown final/typed responsibility only',
   new_R726_registered_parent_family:false,new_R726_CLI_peer_added:false,
   previous_model_or_mean_root_or_point_or_final_migrated:false,
   no_inference_of_complete_final_or_typed_history_from_progress:true
  },
  {
   run_attempt_key:'46105138690/1',run_id:'46105138690',run_attempt:1,
   declared_driver_source_sha256:parentDriverSha,
   complete_declared_parent_source_binding:clone(parentDriver),
   complete_original_evidence:c.parents.peer27,
   complete_original_evidence_scope:'Whole original R725 five-eighths launch and official run/job record; its different width and actual source remain original.',
   official_evidence_json_fence_index:1,all_note_blocks_and_prose_retained:true,
   evidence_body_rewritten:false,
   complete_original_parameter_records_json_fence_index:0,
   current_role:'external historical evidence and unknown final/typed responsibility only',
   new_R726_registered_parent_family:false,new_R726_CLI_peer_added:false,
   previous_model_or_mean_root_or_point_or_final_migrated:false,
   no_inference_of_complete_final_or_typed_history_from_progress:true
  }
 ];
 const b=clone(p);
 b.schema='complete-fixed-fejer-R726-bhalf-parameter-binding-v1';
 b.prepared_date=c.prepared_date;b.session=c.session;
 b.status='complete prepared R726 spherical parameters; no new scientific run or physical result';
 b.namespace=c.namespace;b.intended_independent_runner_label=c.runner;
 b.complete_parent_documents={
  ...clone(p.complete_parent_documents),
  immediate_R725_science:pub(c.parents.science),immediate_R725_pure:pub(c.parents.pure),
  immediate_R725_parameter_binding:pub(c.parents.binding),immediate_R725_parameter_delivery:pub(c.parents.delivery),
  current_R726_source_binding:sourceRec,current_R726_source_delivery:sourceDel
 };
 b.complete_document_sharing={
  ...clone(p.complete_document_sharing),
  complete_immediate_science_and_pure_metadata:{science:ref(pub(c.parents.science),''),pure:ref(pub(c.parents.pure),'')},
  complete_original_parameter_binding:ref(pub(c.parents.binding),''),
  complete_original_parameter_delivery:ref(pub(c.parents.delivery),''),
  complete_whole_ancestor_documents:ref(pub(c.parents.binding),'/complete_parent_documents'),
  all_original_top_level_metadata_fields:Object.keys(p),
  exact_parent_source_change_metadata:ref(pub(c.parents.binding),'/current_scientific_source_change'),
  exact_parent_all_peer_history:ref(pub(c.parents.binding),'/complete_peer_responsibilities'),
  all_parent_fields_shared_without_truncation:true
 };
 b.current_source_role_registry={...ref(sourceRec,'/complete_source_role_registry'),
  complete_pairs:137,unchanged_pairs:118,changed_pairs:19,
  scope:'Complete actual R726 current registry; nineteen changed current pairs, one hundred eighteen exact R725 pairs retained. Historical registries remain at their own whole sources.'};
 b.current_runtime_records={...ref(sourceRec,'/current_complete_runtime_sources'),
  complete_files:23,new_files:22,shared_files:1,all_current_files_required:true};
 b.complete_current_source_delivery=sourceDel;
 b.current_scientific_source_change={
  complete_current_source_records:ref(sourceRec,'/current_complete_runtime_sources'),
  all_changed_current_source_roles:clone(source.changed_current_source_roles),
  complete_prior_source_change_metadata:ref(pub(c.parents.binding),'/current_scientific_source_change'),
  physical_boundary_Slerp_and_actual_mean_equation_genuinely_changed:true,
  source_fixed_boundary_cutoff_retained:true,source_fixed_boundary_epsilon:'1/8',
  new_CLI_words:0,physical_boundary_total_length_unchanged:'1/2',central_profile_delta_unchanged:'1/32',
  complete_boundary_inner_cuts:8,complete_boundary_polynomial_or_affine_pieces:12,
  original_central_paired_halfwaves_auxiliary12_bubble_and_lift_preserved:true,
  outer_original_whole_cell_Gauss_partial_Lagrange_rule_preserved:true,
  new_seed_mean_roots_and_reference_calibration_actually_required:true,
  old_mean_roots_cached_words_model_point_or_final_not_inherited:true,
  complete_R725_proof:clone(p.current_scientific_source_change.complete_R725_proof),
  complete_R726_definition_and_mean_source:ref(sourceRec,'/actual_field_and_mean'),
  complete_R726_minimal_source_delivery:clone(source.minimal_complete_seed_delivery),
  complete_actual_pure_plan_contract:ref(sourceRec,'/pure_interfaces'),
  curvature_cache_and_original_return_scalar_observer_retained:true,
  restoration_policy_or_demanded_rotation_frame2_not_added:true,
  working_nonantipodal_domain_not_acute_proof_gate:true,
  R709_Euclidean_potential_or_R722_posterior_formula_inherited:false,
  R726_or_R727_accurate_domain_or_existence_claimed:false
 };
 b.explicit_parameter_recipe=clone(p.explicit_parameter_recipe);
 const recipe=b.explicit_parameter_recipe;
 recipe.complete_parent_science_step=ref(pub(c.parents.science),'/steps/0');
 recipe.complete_parent_pure_step=ref(pub(c.parents.pure),'/steps/0');
 recipe.old_namespace=c.old_namespace;recipe.new_namespace=c.namespace;
 recipe.current_scripts={science:source.current_complete_runtime_sources.launcher.path,pure:source.current_complete_runtime_sources.reader.path};
 recipe.complete_original_seed_parameter_recipe=ref(pub(c.parents.binding),'/explicit_parameter_recipe/current_seed_parameter_recipe');
 recipe.current_seed_parameter_recipe=clone(p.explicit_parameter_recipe.current_seed_parameter_recipe);
 const seed=recipe.current_seed_parameter_recipe;
 seed.complete_new_seed_source=clone(source.current_complete_runtime_sources.seed_reference);
 seed.complete_new_mean_source=clone(source.current_complete_runtime_sources.seed_mean);
 seed.complete_physical_boundary_cutoff_source=ref(sourceRec,'/current_complete_runtime_sources/seed_reference');
 seed.boundary_cutoff_formula_retained=seed.boundary_formula;
 seed.boundary_formula='R726 S_chi(N(T0),N(v)) using the original R725 C_epsilon cutoff epsilon1/8 on all four complete boundary layers';
 seed.total_mean_equation='central_length*v + integral_boundary S_chi(N(T0),N(v)) - K = 0';
 seed.amplitude_equation='a_delta(lambda) - norm(v) = 0';
 seed.vector_boundary_mean_equation_changed=true;
 seed.original_complete_scalar_amplitude_and_auxiliary12_formula_retained=true;
 seed.true_mean_root_and_angular_jets_still_require_actual_work=true;
 seed.old_R709_or_R722_boundary_proof_inherited=false;
 seed.R726_or_R727_accurate_mean_existence_claimed=false;
 b.fixed_target_scope={...clone(p.fixed_target_scope),
  same_boundary_width_as_run26:true,
  complete_original_target_scope:ref(pub(c.parents.binding),'/fixed_target_scope'),
  current_field_seed_and_mean_graph_differ_from_R725:true};
 b.complete_peer_responsibilities=clone(p.complete_peer_responsibilities);
 const peers=b.complete_peer_responsibilities;
 peers.complete_previous_peer_binding=pub(c.parents.binding);
 peers.whole_current_prior_peer_objects=ref(pub(c.parents.binding),'/complete_peer_responsibilities');
 peers.complete_R725_external_evidence_records=peerRecords;
 peers.complete_external_obligation_pairs=clone(p.complete_peer_responsibilities.complete_external_obligation_pairs);
 for(const rec of peerRecords){
  if(peers.complete_external_obligation_pairs.some(x=>x[0]===rec.run_attempt_key))
   throw new Error('An R725 peer was already in this exact parent');
  peers.complete_external_obligation_pairs.push([rec.run_attempt_key,rec.declared_driver_source_sha256]);
 }
 peers.external_obligation_count=peers.complete_external_obligation_pairs.length;
 peers.all_original_thirteen_pairs_from_complete_run26_binding_retained=true;
 peers.all_original_thirteen_pair_order_and_complete_old_objects_retained=true;
 peers.current_R726_source_not_assigned_to_any_old_peer=true;
 peers.no_new_peer_CLI_or_PARENT_FAMILIES_entry=true;
 peers.old_unknown_final_or_typed_not_filled_from_new_progress=true;
 peers.R726_seed_change_does_not_admit_old_physical_model_or_final=true;
 b.complete_display_correspondence=clone(p.complete_display_correspondence);
 b.complete_display_correspondence.current_live_mapping=remap(p.complete_display_correspondence.current_live_mapping,c.old_namespace,c.namespace);
 b.complete_display_correspondence.complete_immediate_display=ref(pub(c.parents.binding),'/complete_display_correspondence');
 b.complete_display_correspondence.actual_current_scalar_observer=clone(source.current_complete_runtime_sources.scalar_progress);
 b.complete_display_correspondence.all_original64_pairs_unchanged_except_output_namespace=true;
 b.actual_future=clone(p.actual_future);
 if(Object.values(b.actual_future).some(x=>x!==null))throw new Error('Do not copy an actual run into future29');
 b.scientific_scope={...clone(p.scientific_scope),R726_precise_mean_or_geometry_proof_paid:false,
  no_R727_numeric_gate_added:true,complete_parent_acceptance_and_all_step_order_retained:true};
 b.complete_steps_preservation={
  science:{parent:pub(c.parents.science),parent_json_pointer:'/steps/0',argv_words:157,formal_fields:458,
   original_live_fields:64,additional_live_fields:0,numeric_changes:[]},
  pure:{parent:pub(c.parents.pure),parent_json_pointer:'/steps/0',argv_words:7,formal_fields:445,
   live_fields:0,numeric_changes:[]}
 };
 const steps={};
 for(const kind of ['science','pure']){
  const parent=files[kind].value.steps;
  if(!Array.isArray(parent)||parent.length!==1)throw new Error('The complete parent is not one whole step');
  let step=remap(parent[0],c.old_namespace,c.namespace);
  step.script=recipe.current_scripts[kind];
  step.scope='Complete R726 spherical-boundary paired-halfwave b/S=1/2, delta=1/32 '+kind+
   ' from the entire run26 parameter parent. The actual Slerp boundary, full mean Jacobian/two angular jets, source/model and calibration genuinely change; all original numerical argument words, free variables, domains, 32 normal stages, budget, acceptance rules, complete outputs, cleanup, 458/445 formal selectors and 64 live selectors remain. R725 epsilon1/8 cutoff and paired central halfwaves remain. No old mean/model/point/final or R709/R722 certificate is inherited; no acute-domain numeric gate is added.';
  let reverse=remap(step,c.namespace,c.old_namespace);
  reverse.script=parent[0].script;reverse.scope=parent[0].scope;
  if(JSON.stringify(reverse)!==JSON.stringify(parent[0]))throw new Error('Whole inverse step differs '+kind);
  if(step.args.length!==(kind==='science'?157:7))throw new Error('Whole argv count');
  const formal=Object.values(step.summary).reduce((n,x)=>n+Object.keys(x).length,0);
  const live=Object.values(step.progress_summary||{}).reduce((n,x)=>n+Object.keys(x).length,0);
  if(formal!==(kind==='science'?458:445)||live!==(kind==='science'?64:0))throw new Error('Whole selector count');
  const ready=clone(files[kind].value);
  ready.schema='complete-fixed-fejer-R726-bhalf-'+kind+'-ready-v1';
  ready.prepared_date=c.prepared_date;ready.namespace=c.namespace;ready.intended_independent_runner_label=c.runner;
  ready.executed=false;ready.complete_parameter_binding=clone(c.expected_binding_record);
  ready.complete_parent_parameter_file=pub(c.parents[kind]);
  ready.whole_parent_step=ref(pub(c.parents[kind]),'/steps/0');
  ready.all_parent_metadata_preserved_as_historical_full_document=ref(pub(c.parents[kind]),'');
  ready.complete_current_source_registry=ref(c.expected_binding_record,'/current_source_role_registry');
  ready.complete_current_runtime_records=ref(c.expected_binding_record,'/current_runtime_records');
  ready.complete_peer_responsibilities=ref(c.expected_binding_record,'/complete_peer_responsibilities');
  ready.complete_all64_live_correspondence=ref(c.expected_binding_record,'/complete_display_correspondence');
  ready.explicit_parameter_recipe=ref(c.expected_binding_record,'/explicit_parameter_recipe');
  ready.physical_seed_boundary_law_changed=true;
  ready.source_fixed_cutoff_epsilon='1/8';ready.source_cutoff_unchanged_relative_to_parent=true;
  ready.actual_mean_vector_equation_and_full_derivatives_changed=true;
  ready.old_R709_or_R722_boundary_proof_inherited=false;
  ready.R726_or_R727_accurate_existence_claimed=false;
  ready.actual_future=clone(b.actual_future);
  ready.steps=[step];steps[kind]=ready;
 }
 return {binding:b,...steps};
}
return build;

})();

const argv={};
for(let i=2;i<process.argv.length;i+=2){
 const key=process.argv[i],value=process.argv[i+1];
 if(!['--source-root','--output-directory'].includes(key)||!value||argv[key]!==undefined)
  throw new Error('Use exactly --source-root REPOSITORY --output-directory OUTPUT');
 argv[key]=value;
}
if(Object.keys(argv).length!==2)throw new Error('Both source root and output directory are required');
const root=path.resolve(argv['--source-root']),out=path.resolve(argv['--output-directory']);
if(root===out)throw new Error('Use an independent generated directory');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
function agrees(record,data){return data.byteLength===record.bytes&&sha(data)===record.sha256;}
function readWhole(record){
 if(!Number.isSafeInteger(record.bytes)||record.bytes<1||record.bytes>=100000)
  throw new Error('A complete source/metadata input must be below100000 bytes');
 const file=path.join(root,record.path);
 if(fs.existsSync(file)&&fs.statSync(file).size===record.bytes){
  const raw=fs.readFileSync(file);
  if(agrees(record,raw))return raw;
 }
 const blob=record.git_blob_sha;
 if(!/^[0-9a-f]{40}$/.test(blob))throw new Error('Exact original Git blob required');
 const size=spawnSync('git',['cat-file','-s',blob],{cwd:root,encoding:'utf8',maxBuffer:200000});
 if(size.status!==0||Number(size.stdout.trim())!==record.bytes)
  throw new Error('The exact complete historical blob must be present: '+record.path);
 const result=spawnSync('git',['cat-file','blob',blob],{cwd:root,maxBuffer:200000});
 if(result.status!==0||!agrees(record,result.stdout))
  throw new Error('The full original bytes differ: '+record.path);
 return result.stdout;
}
const files={};
for(const [key,record]of Object.entries(CONFIG.parents)){
 const raw=readWhole(record),text=raw.toString('utf8');
 if(!Buffer.from(text,'utf8').equals(raw))throw new Error('Lossless complete UTF-8 required');
 files[key]={text,record,value:key.startsWith('peer')?null:JSON.parse(text)};
}
const built=BUILD(CONFIG,files),results=[];
fs.mkdirSync(out,{recursive:true});
for(const kind of ['binding','science','pure']){
 const record=EXPECTED[kind],text=JSON.stringify(built[kind],null,2)+'\n',raw=Buffer.from(text,'utf8');
 if(!agrees(record,raw))throw new Error('Complete output differs: '+kind);
 if(raw.byteLength>=100000)throw new Error('Complete metadata file limit');
 const dest=path.join(out,record.name);
 if(fs.existsSync(dest)){
  if(!fs.readFileSync(dest).equals(raw))throw new Error('Different existing output; do not overwrite '+dest);
 }else fs.writeFileSync(dest,raw,{flag:'wx'});
 results.push({...record,generated_path:dest,whole_original_step_inverse_equal:true});
}
process.stdout.write(JSON.stringify({
 schema:'complete-R726-run29-parameter-text-reproduction-v1',
 complete:true,scope:'complete JSON parameter construction only; no scientific gate',
 complete_eight_source_metadata_inputs_read:true,outputs:results,
 all_original_157_and_7_argument_words_retained_except_output_namespace:true,
 all_original_458_and_445_formal_and_64_live_pairs_retained:true,
 original_five_supported_CLI_peers_unchanged:true,
 additional_run26_run27_records_only_external_original_evidence:true,
 original_unknown_final_and_typed_responsibilities_retained:true,
 Python_import:false,AST:false,compile:false,fixture:false,scientific_evaluation:false,
 refs_or_queues_changed:false
})+'\n');
