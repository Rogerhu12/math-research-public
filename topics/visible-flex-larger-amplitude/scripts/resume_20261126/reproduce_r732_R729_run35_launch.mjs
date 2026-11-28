#!/usr/bin/env node
/** Reproduce complete text inputs from pinned whole Git files. No numerical work. */
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {readFileSync, mkdirSync, writeFileSync} from 'node:fs';
import {resolve, dirname, sep} from 'node:path';

function identity(path, body) {
  const bytes=Buffer.byteLength(body,'utf8');
  const hash=(algorithm,value)=>createHash(algorithm).update(value,'utf8').digest('hex');
  return {path,bytes,sha256:hash('sha256',body),git_blob_sha:hash('sha1','blob '+bytes+'\0'+body)};
}
function equal(record,body) {
  const value=identity(record.path,body);
  return ['bytes','sha256','git_blob_sha'].every(key=>value[key]===record[key]);
}
function readWhole(root,record) {
  let body;
  try { body=readFileSync(resolve(root,record.path),'utf8'); } catch {}
  if(typeof body!=='string'||!equal(record,body))
    body=execFileSync('git',['-C',root,'cat-file','blob',record.git_blob_sha],{encoding:'utf8',maxBuffer:256000});
  if(!equal(record,body)) throw Error('Whole source identity differs: '+record.path);
  return body;
}

const records={
  "parentController": {
    "role": "controller",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/public_actions_controller_parallel34_geometry_locations.py",
    "bytes": 21888,
    "sha256": "fd8eb12916adf8c3ab9b0519e65937b552ac5d8cab2f8b9b44b1877ee1852d64",
    "git_blob_sha": "f37e3871908884474f9d739161246d201580e872"
  },
  "parentWorkflow": {
    "role": "workflow",
    "path": ".github/workflows/visible-larger-20261128-parallel34.yml",
    "bytes": 2218,
    "sha256": "da4a51ac6feb594b8cf26fb90c63da9c66af2152c12798426a18a403a43b39a9",
    "git_blob_sha": "bd4cec91925246e62d4826da800e6b94322d3642"
  },
  "parentQueue": {
    "role": "queue",
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-followups-34.json",
    "bytes": 83441,
    "sha256": "9020e55bde60fff31c3aee4d56cea1ca17a95402132a31474d9a7bba6e9d1a56",
    "git_blob_sha": "e574ca05b4d5b2b321c60ae52507eeb015e297a6"
  },
  "parentRequest": {
    "role": "request",
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-actions-request-34.json",
    "bytes": 37312,
    "sha256": "2a256463d8a9e2d6b9ae31ded90a27035e83903e274d80849f7cab589a2813b0",
    "git_blob_sha": "9de9b505f266e58fc03e743ceedbdc4b36dbaa0d"
  },
  "parentManifest": {
    "role": "parent_launch_manifest",
    "name": "fixed-fejer-r730-R729-run34-complete-launch-delivery.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r730-R729-run34-complete-launch-delivery.json",
    "bytes": 30531,
    "sha256": "e1541fa2b1b5165b9f56a81cc874b53ba07d1d19d85f4e9706ed10877e996d1a",
    "git_blob_sha": "d663234935ba4eb3205beda75a904d131ef9d1df"
  },
  "paramBinding": {
    "role": "binding",
    "name": "fixed-fejer-r732-R729-complete-parameter-binding.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r732-R729-complete-parameter-binding.json",
    "bytes": 55504,
    "sha256": "18818dc9d8ca565c8b06921210b3c237465174255f55aaa27bc91a8968540959",
    "git_blob_sha": "90863cf813f8e83e54a812302269fe30623b4402"
  },
  "paramManifest": {
    "role": "pmanifest",
    "name": "fixed-fejer-r732-R729-complete-parameter-delivery.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r732-R729-complete-parameter-delivery.json",
    "bytes": 21423,
    "sha256": "356527e358a425882a0578e94a891d96f188d672160fc1dbec3004669569109a",
    "git_blob_sha": "c57da600dcd07950c045d9224c16987cef64d87c"
  },
  "source": {
    "role": "complete_scientific_source_delivery",
    "name": "fixed-fejer-r732-R729-complete-source-delivery.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r732-R729-complete-source-delivery.json",
    "bytes": 36718,
    "sha256": "7ac0fac5bed253862db708c87892c9908a87ba31a6ceab01460e7a1ce5da3902",
    "git_blob_sha": "069f2d0267355893ac69334d8e845a19c59a0358"
  },
  "sourceBinding": {
    "role": "complete_runtime_and_source_binding",
    "name": "fixed-fejer-r732-R729-current-runtime-binding.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r732-R729-current-runtime-binding.json",
    "bytes": 66334,
    "sha256": "425a1c0f484de848fdc66396623bc8e434b92bcfaf07216b49149a7324e7a195",
    "git_blob_sha": "ba50a6fa07a086964c2c99c9fb2580c702427915"
  },
  "science": {
    "role": "science",
    "name": "fixed-fejer-r732-R729-science-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r732-R729-science-complete-ready.json",
    "bytes": 87692,
    "sha256": "ebc8d4a0ed161a43ef3a50628b55600e67dec0855aacfc118d9b5fb20335695d",
    "git_blob_sha": "a8c5b8abdf2a6de3da4738403bad883060a024c0"
  },
  "pure": {
    "role": "pure",
    "name": "fixed-fejer-r732-R729-pure-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r732-R729-pure-complete-ready.json",
    "bytes": 77632,
    "sha256": "e7c82c216e2da8c84327b6b23df302ccf26fd1ccbe775d76b8abac317d1318e0",
    "git_blob_sha": "0438f0d75e83445aad50b83ffdd878b0bd22659f"
  }
};
const settings={
  "when": "2026-11-28 10:43:28 UTC",
  "request": "visible-larger-resume-20261128-35",
  "paths": {
    "controller": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/public_actions_controller_parallel35_geometry_locations.py",
    "workflow": ".github/workflows/visible-larger-20261128-parallel35.yml",
    "queue": "topics/visible-flex-larger-amplitude/computations/resume-20261128-followups-35.json",
    "request": "topics/visible-flex-larger-amplitude/computations/resume-20261128-actions-request-35.json"
  },
  "parameterReproducer": {
    "role": "pgen",
    "name": "reproduce_r732_R729_run35_parameters.mjs",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_r732_R729_run35_parameters.mjs",
    "bytes": 13829,
    "sha256": "cf7332753aace071fdd7b97976d9be6bca4ea414630cd7ce74a371055a859ef5",
    "git_blob_sha": "36a116016d175a97d678ed2b82afd18cc1d98769"
  },
  "sourcePublication": null,
  "parameterPublication": null,
  "rulesReadCommit": "e6b5997e2c01c7c39fbdd3762c27240b29182c3d",
  "ruleRecords": [
    {
      "path": "README.md",
      "bytes": 10649,
      "sha256": "539f1ea02feb8a63c5aa734ed560ab6ecbf3ff7f570212e46788413bb072f444",
      "git_blob_sha": "99c5ad8d06e939e6cfbbab1afdeffa5463f15f18",
      "fixed_commit": "e6b5997e2c01c7c39fbdd3762c27240b29182c3d"
    },
    {
      "path": "topics/visible-flex-larger-amplitude/README.md",
      "bytes": 2664,
      "sha256": "3c1c03b358792b6c9937b95fcfea05b80a572a4da2cce615c4c9832fe929057d",
      "git_blob_sha": "bff8aea253a9e6a7a4fac28d810ac454c5499fec",
      "fixed_commit": "e6b5997e2c01c7c39fbdd3762c27240b29182c3d"
    }
  ],
  "controllerPatches": [
    {
      "from": "visible-larger-parallel-34:start",
      "to": "visible-larger-parallel-35:start",
      "count": 1
    },
    {
      "from": "visible-larger-parallel-34:end",
      "to": "visible-larger-parallel-35:end",
      "count": 1
    },
    {
      "from": "Actions34：",
      "to": "Actions35：",
      "count": 1
    },
    {
      "from": "并行34规则核查",
      "to": "并行35规则核查",
      "count": 1
    }
  ],
  "workflowPatches": [
    {
      "from": "Visible larger amplitude R730 safe cone R729 common slack 20261128 34",
      "to": "Visible larger amplitude R732 rounded end R729 common slack 20261128 35",
      "count": 1
    },
    {
      "from": "resume-20261128-actions-request-34.json",
      "to": "resume-20261128-actions-request-35.json",
      "count": 2
    },
    {
      "from": "visible-larger-fixed-input-20261128-34",
      "to": "visible-larger-fixed-input-20261128-35",
      "count": 1
    },
    {
      "from": "Reconstruct the fixed target and solve complete R730 with R729 common slack",
      "to": "Reconstruct the fixed target and solve complete R732 with R729 common slack",
      "count": 1
    },
    {
      "from": "public_actions_controller_parallel34_geometry_locations.py",
      "to": "public_actions_controller_parallel35_geometry_locations.py",
      "count": 1
    }
  ]
};
const expected={
  "controller": {
    "role": "controller",
    "name": "public_actions_controller_parallel35_geometry_locations.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/public_actions_controller_parallel35_geometry_locations.py",
    "bytes": 21888,
    "sha256": "e3c0c644bb206b051120cd7c02f5928553e7337f40635fb876b2357d18ec5274",
    "git_blob_sha": "8bddfed0548deb3d2e707e0e91f1c063e408204d"
  },
  "workflow": {
    "role": "workflow",
    "name": "visible-larger-20261128-parallel35.yml",
    "path": ".github/workflows/visible-larger-20261128-parallel35.yml",
    "bytes": 2220,
    "sha256": "7db7fefe0a5c4afe97161e94df0e623df5dad040d05d6a27c08775f4ce82b4e2",
    "git_blob_sha": "b8f0e883ee26b6381e8043ba9048bfdd37b95bd6"
  },
  "queue": {
    "role": "queue",
    "name": "resume-20261128-followups-35.json",
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-followups-35.json",
    "bytes": 90808,
    "sha256": "fb1205fa6fb22d09c497be930a082492cc6c52e3f08b5209a13eb2fa5710a1f9",
    "git_blob_sha": "ac58f4a4f870fba462823777bab1962d5d55718c"
  },
  "request": {
    "role": "request",
    "name": "resume-20261128-actions-request-35.json",
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-actions-request-35.json",
    "bytes": 39785,
    "sha256": "f7697461e65cf9233e2c06375d255f688b17496552d321dfac211f6572d0f64f",
    "git_blob_sha": "a1f65bdd734208d129abebc595210a32c71f6863"
  }
};
function buildLaunch(input,records,settings,identity) {
  const {parentRequest,parentQueue,paramBinding,source,science,pure}=input;
  const paths=settings.paths;
  const immutable=(complete_file,json_pointer='')=>({complete_file,json_pointer,whole_file_required:true});
  const wire=value=>JSON.stringify(value)+'\n';
  const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
  const requestID=settings.request;
  function replaceText(body,patches) {
    for(const patch of patches){
      const pieces=body.split(patch.from);
      if(pieces.length-1!==patch.count)throw Error('Whole parent text does not have the pinned transport label: '+patch.from);
      body=pieces.join(patch.to);
    }
    return body;
  }
  const controller=replaceText(input.parentController,settings.controllerPatches);
  const workflow=replaceText(input.parentWorkflow,settings.workflowPatches);
  const controllerId=identity(paths.controller,controller);
  const workflowId=identity(paths.workflow,workflow);
  const first=parentQueue.steps[0];
  const second={...parentQueue.steps[1],id:parentQueue.steps[1].id.replace(/run34$/,'run35')};
  if(second.id===parentQueue.steps[1].id) throw Error('Expected the second original input label');
  const sc=science.steps[0],rd=pure.steps[0];
  const queueOf=steps=>({parent_request_id:requestID,finish_when_done:false,steps});
  const queue=wire(queueOf([first,second,sc]));
  const queueId=identity(paths.queue,queue);
  const late=wire(queueOf([rd]));
  const capacity={
    initial_steps:[first.id,second.id,sc.id],initial_queue:queueId,initial_step_count:3,
    initial_queue_bytes:queueId.bytes,pure_only_queue_bytes:identity(paths.queue,late).bytes,
    pure_only_queue_sha256:identity(paths.queue,late).sha256,pure_only_queue_git_blob:identity(paths.queue,late).git_blob_sha,
    all_four_step_queue_bytes:identity(paths.queue,wire(queueOf([first,second,sc,rd]))).bytes,
    science_plus_pure_two_step_queue_bytes:identity(paths.queue,wire(queueOf([sc,rd]))).bytes,
    active_queue_limit_bytes:95000,deferred_complete_pure_step_ready:records.pure,
    after_actual_science_natural_return:'Replace the active request queue with the whole /steps/0 of the current pure-ready file under this same parent_request_id. Keep finish_when_done false for accurate postprocessing.',
    finish_when_done:false,numerical_parameters_or_original_summary_selectors_removed:false,complete_parent_capacity:immutable(records.parentRequest,'/queue_capacity_policy')};
  const parent=parentRequest;
  const r={...parent};
  r.request_id=requestID;r.created_utc=settings.when;r.rules_read_commit=settings.rulesReadCommit;
  r.rules_sha256=Object.fromEntries(settings.ruleRecords.map(x=>[x.path,x.sha256]));
  r.complete_launch_rules_records=settings.ruleRecords;
  r.rules_read_method='Both complete README files were read through the fixed Git blobs at the stated commit, including the 2026-11-28 root Section 16. The inherited controller compares both whole files on its real pulls.';
  r.followup_file=paths.queue;r.controller=controllerId;r.followups=parent.followups;
  r.scope='Independent R732 central S-L contraction and rounded deep-tail end at fixed input, with the complete original R729 restoration recovery and outer acceptance. Rebuild the full current sources separately for science and pure. Scientific status only comes from this request and its own whole report.';
  const recipe=parent.mathematical_recipe;
  r.mathematical_recipe={};
  for(const key of ['chart_formula','target_coefficients','scalar','mesh','physical_phase','M','K','J','N','P','same_mathematical_g_as_fixed_fejer_run31','demanded_rotation_frame2_used']) r.mathematical_recipe[key]=recipe[key];
  Object.assign(r.mathematical_recipe,{whole_old_mathematical_recipe:immutable(records.parentRequest,'/mathematical_recipe'),whole_current_reference:immutable(records.paramBinding,'/complete_R732_seed_contract'),
    eta:'1/512',xi_max:'3/4',global_polynomial:'(1-(2*t-1)^12)^7',k:6,b:'1/1000',d:'7/50',h_T:'13/50',internal_cuts:['s=S-L','u=uf','u=uc','u=2b','u=b'],length_equation:'central L(xi,phi)=S-L_terminal',inverse_equation:'central ell(t,phi)=s; terminal u=S-s',noncircular_core_acceleration:'k0*rho*n',outer_collar_frozen:false,old_twelve_mean_arrays_or_R727_certificate_inherited:false,old_field_point_or_normal_packet_inherited:false});
  r.source_and_parameter_scope='Complete R732 source family, 24 runtime files and 139 scientific roles. Relative to the 139 run34 roles, 120 pairs are exact and 19 current physical or downstream pairs change. The complete parent vectors are reused with new runner-relative output names and all original numerical words. Each detached source checkout first builds all 17 whole R730 parents, then all 17 R732 files from those parents.';
  r.old_history_scope='All original five pending CLI pairs, complete peer objects, failures and unknown typed-history responsibilities remain in their whole parent records. The run32 and run33 histories, the run33 retry and run34 are separate from this field. No historical final is admitted as the new field.';
  r.current_refinement={...paramBinding.complete_original_budgets,legacy_unused_shape_words:paramBinding.complete_R732_seed_contract.legacy_unused,remaining_seven_working_length_parameters:paramBinding.complete_R732_seed_contract.actual_length_parameters,
    complete_current_source_registry:immutable(records.sourceBinding,'/complete_source_role_registry'),complete_original_refinement:immutable(records.parentRequest,'/current_refinement'),complete_R729_contract:immutable(records.paramBinding,'/full_original_stage_optimization_and_QP_contract'),source_fixed_R732_global_reference:true,counts:paramBinding.current_argument_and_field_counts,
    actual_future_model_identity_sha256:null,actual_future_field_point_sha256:null};
  r.complete_scientific_parameter_plan={science:records.science,pure:records.pure,whole_steps_separate_without_parameter_omission:true,complete_shared_parameter_binding:records.paramBinding,complete_delivery:records.paramManifest};
  r.queue_capacity_policy=capacity;r.complete_scientific_source_package=records.source;
  r.complete_unchanged_stage_source_package={complete_historical_source_package:immutable(records.parentRequest,'/complete_unchanged_stage_source_package'),current_complete_sources:immutable(records.sourceBinding,'/current_complete_runtime_sources'),current_complete_comparison:immutable(records.sourceBinding,'/current_role_comparison'),normal_stages:32,all_original_equations_and_angular_orders_retained:true};
  r.complete_parameter_reproducer=settings.parameterReproducer;
  const peers=immutable(records.paramBinding,'/complete_peer_responsibility');
  r.external_unregistered_peer_obligations={whole_current:peers,whole_original:immutable(records.parentRequest,'/external_unregistered_peer_obligations')};
  r.external_peer_status={whole_current:peers,whole_parent:immutable(records.parentRequest,'/external_peer_status'),supported_original_CLI_count:5,current_external_pairs:paramBinding.complete_peer_responsibility.external_pair_count,previous_failures_and_unknowns_unchanged:true};
  r.seed_and_mean_contract={whole_old:immutable(records.parentRequest,'/seed_and_mean_contract'),complete_current_R732:immutable(records.paramBinding,'/complete_R732_seed_contract'),complete_current_interfaces:immutable(records.sourceBinding,'/interfaces'),old_mean_input_or_certificate_inherited:false};
  r.complete_display_correspondence={complete_original:immutable(records.parentRequest,'/complete_display_correspondence'),complete_current:immutable(records.paramBinding,'/complete_R732_selector_maps'),complete_counts:paramBinding.current_argument_and_field_counts};
  r.original_complete_launch_request=immutable(records.parentRequest);r.all_original_launch_request_metadata_preserved_in_full={...immutable(records.parentRequest),every_original_key_value_retained_as_historical_metadata:true};
  r.controller_source_identity_derivation={complete_parent:records.parentController,complete_text_replacements:settings.controllerPatches,current:controllerId};r.workflow_identity_derivation={complete_parent:records.parentWorkflow,complete_text_replacements:settings.workflowPatches,current:workflowId};
  r.complete_initial_input_step_origin={whole_parent_queue:records.parentQueue,complete_json_pointers:['/steps/0','/steps/1'],only_changed_word:{pointer:'/steps/1/id',from:parentQueue.steps[1].id,to:second.id},both_original_input_steps_execute_in_this_runner:true};
  r.complete_current_parameter_delivery=records.paramManifest;r.complete_current_source_binding=records.sourceBinding;
  r.complete_source_role_registry={...immutable(records.sourceBinding,'/complete_source_role_registry'),complete_pairs:139};
  r.complete_current_runtime_registry={...immutable(records.sourceBinding,'/current_complete_runtime_sources'),complete_files:24};
  r.complete_current_parameter_binding=records.paramBinding;
  r.complete_current_peer_responsibilities={current:peers,whole_previous:immutable(records.parentRequest,'/complete_current_peer_responsibilities')};
  r.complete_original_terminal_and_failure_histories={whole_previous:immutable(records.parentRequest,'/complete_original_terminal_and_failure_histories'),whole_current_peer_and_parallel_history:peers,original_run29_failure:immutable(records.parentRequest,'/complete_current_original_run29_failure'),other_family_terminal_state_inferred:false};
  r.current_transport_contract={...parent.current_transport_contract,complete_publication_capacity_wait:{...parent.current_transport_contract.complete_publication_capacity_wait,complete_current_controller:controllerId,complete_parent_controller:records.parentController,complete_original_derivation:immutable(records.parentRequest,'/current_transport_contract/complete_publication_capacity_wait')}};
  r.transport_window_extension={...parent.transport_window_extension,whole_immediate_parent_extension:immutable(records.parentRequest,'/transport_window_extension'),window_changed_from_actual_parent_run34:false};
  r.current_scientific_source_and_parameter_publications={source:settings.sourcePublication,parameters:settings.parameterPublication,physical_seed_proof_publication:source.complete_R732_proof.publication,previous_publications:immutable(records.parentRequest,'/current_scientific_source_and_parameter_publications')};
  r.original_request_key_count=Object.keys(parent).length;
  r.retry_scope={whole_parent_history:immutable(records.parentRequest,'/retry_scope'),independent_new_physical_reference:true,old_final_used:false,current_run_id:null,current_source_checkout:null,current_model:null,current_point:null,current_report:null};
  r.complete_current_launch_source_and_inputs={whole_current_scientific_delivery:records.source,whole_current_parameter_delivery:records.paramManifest,complete_input_sources:r.complete_input_sources,
    complete_normal_build:immutable(records.source,'/normal_build_route'),complete_scientific_registry:r.complete_source_role_registry,
    wrapper:source.complete_source_reproduction.wrapper,builder:source.complete_source_reproduction.recipe,original_inner_entries:{science:input.sourceBinding.current_complete_runtime_sources.launcher,pure:input.sourceBinding.current_complete_runtime_sources.reader},
    runner_reconstructs_all17_whole_files_before_entry:true,reference_and_physical_report_identity_known_only_after_actual_run:true};
  r.complete_R732_selected_reference_input=immutable(records.paramBinding,'/complete_R732_seed_contract/selected_snapshot');
  r.actual_future=paramBinding.actual_future;r.current_complete_request_key_count=Object.keys(r).length;
  if(!same(r.complete_input_sources,parent.complete_input_sources)) throw Error('Full input sources must be inherited');
  return {controller,workflow,queue,request:wire(r)};
}

const argv=process.argv.slice(2);
if(argv.length!==4||argv[0]!=='--source-repository'||argv[2]!=='--output-repository')
  throw Error('Use --source-repository ROOT --output-repository OUTPUT');
const root=resolve(argv[1]), output=resolve(argv[3]), input={};
for(const [key,record] of Object.entries(records)){
  const source=readWhole(root,record);
  input[key]=record.path.endsWith('.json')?JSON.parse(source):source;
}
const files=buildLaunch(input,records,settings,identity);
for(const [key,body] of Object.entries(files)){
  if(!expected[key]||!equal(expected[key],body)) throw Error('Regenerated complete text differs: '+key);
  const path=resolve(output,expected[key].path);
  if(!path.startsWith(output+sep)) throw Error('Expected an output inside the indicated repository');
  mkdirSync(dirname(path),{recursive:true});
  writeFileSync(path,body,{encoding:'utf8'});
}
console.log(JSON.stringify(expected,null,2));
