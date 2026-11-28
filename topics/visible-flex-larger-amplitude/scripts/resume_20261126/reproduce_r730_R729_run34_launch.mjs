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
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/public_actions_controller_parallel32_geometry_locations.py",
    "bytes": 21888,
    "sha256": "3b64dc1d2a6e517ac06edf230d4647e7d8f9008ce2e7e664d702f40c3cea6290",
    "git_blob_sha": "cbb8556396d455849430bb642fb25935d270643f"
  },
  "parentWorkflow": {
    "role": "workflow",
    "path": ".github/workflows/visible-larger-20261128-parallel32.yml",
    "bytes": 2211,
    "sha256": "77525a254c23d2ec0e038e4578b908736dada858ae5435fed70b8ed19fe7bbda",
    "git_blob_sha": "925cbdc3edec3db0465c86784d09f55336f504c3"
  },
  "parentQueue": {
    "role": "queue",
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-followups-32.json",
    "bytes": 78678,
    "sha256": "c913ea85839cddfb5cfd5a1fea3ca4cd864c04aff89b29b13f9ed6d4fd4f89b9",
    "git_blob_sha": "294e50f0292b52270f33cb344f43f3c6ef14c425"
  },
  "parentRequest": {
    "role": "request",
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-actions-request-32.json",
    "bytes": 40137,
    "sha256": "1d6ca2d776175ea9f5d79008c5a59317b5c68f85d83ffd3ab6aac3cb8ce94e92",
    "git_blob_sha": "400edd6988db4ac714710a3091adc75d313ef25b"
  },
  "parentLaunchManifest": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-R729-run32-complete-launch-delivery.json",
    "bytes": 13656,
    "sha256": "6b8b78ae8252174d513894415b908c4602db06b98bf188c8db50d008420c1bb9",
    "git_blob_sha": "90b5f82413ae08c2e3fa8bf2cc98bb25e4d0a1cc"
  },
  "source": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r730-R729-complete-source-delivery.json",
    "bytes": 27059,
    "sha256": "7be33312260e6af8e21862a046857330c7b4f704f938b854be97d1cb3d8d74de",
    "git_blob_sha": "1bf08f8a79cfaf971accb7d10985e3289abcc8de"
  },
  "sourceBinding": {
    "role": "complete_runtime_and_source_binding",
    "name": "fixed-fejer-r730-R729-current-runtime-binding.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r730-R729-current-runtime-binding.json",
    "bytes": 61806,
    "sha256": "f7eda4b71048b816288d8dc92a61db84def183861499117f93986258e86d62ce",
    "git_blob_sha": "886a7bb94b171381f6df06890b3d4c745a7f750d"
  },
  "paramManifest": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r730-R729-complete-parameter-delivery.json",
    "bytes": 10643,
    "sha256": "ac63c2fb4ef9fba1867dedd8cc3d42ed0e7ac2ca0856b1164b774bed9e43f528",
    "git_blob_sha": "6d1bf823988ffd202639ea678062252bb8492449"
  },
  "paramBinding": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r730-R729-complete-parameter-binding.json",
    "bytes": 36310,
    "sha256": "b53af2212ab7e574afc7d65f6607594a64c6f32ce6ecbffe2901730cda9b8a91",
    "git_blob_sha": "2bc4198d68ee3f605f9f4bedbafefd8e67d8d510"
  },
  "science": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r730-R729-science-complete-ready.json",
    "bytes": 80179,
    "sha256": "e59560d83da7c287458ac24814b25fa22f3465f1df42c4729d9b283f80c124ca",
    "git_blob_sha": "3521520ffc6ca45a52d21f56b83bd74df423969d"
  },
  "pure": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r730-R729-pure-complete-ready.json",
    "bytes": 69444,
    "sha256": "9cfe04f62d8eb60d808c2ab0c7733f9a2d803a831c6c64de0378c4090dbe139f",
    "git_blob_sha": "39a7df0497e21c90cf93dfe919d280d4e0572446"
  }
};
const settings={
  "when": "2026-11-28 09:56:46 UTC",
  "paths": {
    "binding": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r730-R729-complete-parameter-binding.json",
    "science": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r730-R729-science-complete-ready.json",
    "pure": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r730-R729-pure-complete-ready.json",
    "pgen": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_r730_R729_run34_parameters.mjs",
    "pnote": "topics/visible-flex-larger-amplitude/notes/2026-11-28-R730-R729-run34-complete-parameters.md",
    "pmanifest": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r730-R729-complete-parameter-delivery.json",
    "controller": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/public_actions_controller_parallel34_geometry_locations.py",
    "workflow": ".github/workflows/visible-larger-20261128-parallel34.yml",
    "queue": "topics/visible-flex-larger-amplitude/computations/resume-20261128-followups-34.json",
    "request": "topics/visible-flex-larger-amplitude/computations/resume-20261128-actions-request-34.json",
    "lgen": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_r730_R729_run34_launch.mjs",
    "lnote": "topics/visible-flex-larger-amplitude/notes/2026-11-28-R730-R729-run34-complete-launch.md",
    "lmanifest": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r730-R729-run34-complete-launch-delivery.json"
  },
  "request": "visible-larger-resume-20261128-34",
  "sourcePublication": "8fb792e78b0cb67e37177a4a590fd3424e279cb2",
  "parameterPublication": null,
  "parameterReproducer": {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_r730_R729_run34_parameters.mjs",
    "bytes": 22546,
    "sha256": "8307d555e80b440c837faad328eb569f5cb6223640a64d107a2da5f861662135",
    "git_blob_sha": "7d9399f41a3f1a6c76415631cc5871072828f6ec"
  },
  "rulesReadCommit": "56c35c4ca2d36e03831702cf1a4a1ba9ebb8efeb",
  "ruleRecords": [
    {
      "path": "README.md",
      "bytes": 10649,
      "sha256": "539f1ea02feb8a63c5aa734ed560ab6ecbf3ff7f570212e46788413bb072f444",
      "git_blob_sha": "99c5ad8d06e939e6cfbbab1afdeffa5463f15f18",
      "fixed_commit": "56c35c4ca2d36e03831702cf1a4a1ba9ebb8efeb"
    },
    {
      "path": "topics/visible-flex-larger-amplitude/README.md",
      "bytes": 2664,
      "sha256": "3c1c03b358792b6c9937b95fcfea05b80a572a4da2cce615c4c9832fe929057d",
      "git_blob_sha": "bff8aea253a9e6a7a4fac28d810ac454c5499fec",
      "fixed_commit": "56c35c4ca2d36e03831702cf1a4a1ba9ebb8efeb"
    }
  ],
  "controllerPatches": [
    {
      "from": "visible-larger-parallel-32:start",
      "to": "visible-larger-parallel-34:start",
      "count": 1
    },
    {
      "from": "visible-larger-parallel-32:end",
      "to": "visible-larger-parallel-34:end",
      "count": 1
    },
    {
      "from": "Actions32：",
      "to": "Actions34：",
      "count": 1
    },
    {
      "from": "并行32规则核查",
      "to": "并行34规则核查",
      "count": 1
    }
  ],
  "workflowPatches": [
    {
      "from": "Visible larger amplitude R728 R729 common slack 20261128 32",
      "to": "Visible larger amplitude R730 safe cone R729 common slack 20261128 34",
      "count": 1
    },
    {
      "from": "resume-20261128-actions-request-32.json",
      "to": "resume-20261128-actions-request-34.json",
      "count": 2
    },
    {
      "from": "visible-larger-fixed-input-20261128-32",
      "to": "visible-larger-fixed-input-20261128-34",
      "count": 1
    },
    {
      "from": "Construct the same fixed target and solve complete R728 with R729 common slack",
      "to": "Reconstruct the fixed target and solve complete R730 with R729 common slack",
      "count": 1
    },
    {
      "from": "public_actions_controller_parallel32_geometry_locations.py",
      "to": "public_actions_controller_parallel34_geometry_locations.py",
      "count": 1
    }
  ]
};
const expected={
  "controller": {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/public_actions_controller_parallel34_geometry_locations.py",
    "bytes": 21888,
    "sha256": "fd8eb12916adf8c3ab9b0519e65937b552ac5d8cab2f8b9b44b1877ee1852d64",
    "git_blob_sha": "f37e3871908884474f9d739161246d201580e872"
  },
  "workflow": {
    "path": ".github/workflows/visible-larger-20261128-parallel34.yml",
    "bytes": 2218,
    "sha256": "da4a51ac6feb594b8cf26fb90c63da9c66af2152c12798426a18a403a43b39a9",
    "git_blob_sha": "bd4cec91925246e62d4826da800e6b94322d3642"
  },
  "queue": {
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-followups-34.json",
    "bytes": 83441,
    "sha256": "9020e55bde60fff31c3aee4d56cea1ca17a95402132a31474d9a7bba6e9d1a56",
    "git_blob_sha": "e574ca05b4d5b2b321c60ae52507eeb015e297a6"
  },
  "request": {
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-actions-request-34.json",
    "bytes": 37312,
    "sha256": "2a256463d8a9e2d6b9ae31ded90a27035e83903e274d80849f7cab589a2813b0",
    "git_blob_sha": "9de9b505f266e58fc03e743ceedbdc4b36dbaa0d"
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
  const second={...parentQueue.steps[1],id:parentQueue.steps[1].id.replace(/run32$/,'run34')};
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
  r.scope='Independent R730 global safe-cone reference at fixed input, with the complete original R729 restoration recovery and outer acceptance. Rebuild the full current sources separately for science and pure. Scientific status only comes from this request and its own whole report.';
  const recipe=parent.mathematical_recipe;
  r.mathematical_recipe={};
  for(const key of ['chart_formula','target_coefficients','scalar','mesh','physical_phase','M','K','J','N','P','same_mathematical_g_as_fixed_fejer_run31','demanded_rotation_frame2_used']) r.mathematical_recipe[key]=recipe[key];
  Object.assign(r.mathematical_recipe,{whole_old_mathematical_recipe:immutable(records.parentRequest,'/mathematical_recipe'),whole_current_reference:immutable(records.paramBinding,'/complete_R730_seed_contract'),
    eta:'1/32',xi_max:'3/4',global_polynomial:'(1-(2*t-1)^12)^7',k:6,internal_cuts:[],length_equation:'L(xi,phi)=S',inverse_equation:'ell(t,phi)=s',old_twelve_mean_arrays_or_R727_certificate_inherited:false,old_field_point_or_normal_packet_inherited:false});
  r.source_and_parameter_scope='Published complete R730 source family, 24 runtime files and 139 scientific roles. Relative to all 138 run32 roles, 120 pairs are exact and 18 change, with one new seed_length_kernel. The complete parent vectors are reused with new runner-relative output names and all original numerical words. The complete 17-source build is performed inside each detached source checkout.';
  r.old_history_scope='All original five pending CLI pairs, complete peer objects, failures and unknown typed-history responsibilities remain in their whole parent records. Run32 and run33 compact observations are external evidence. No historical final is admitted as the new field.';
  r.current_refinement={...paramBinding.complete_original_budgets,legacy_unused_shape_words:paramBinding.complete_R730_seed_contract.legacy_unused,remaining_seven_working_length_parameters:paramBinding.complete_R730_seed_contract.actual_length_parameters,
    complete_current_source_registry:immutable(records.sourceBinding,'/complete_source_role_registry'),complete_original_refinement:immutable(records.parentRequest,'/current_refinement'),complete_R729_contract:immutable(records.paramBinding,'/full_original_stage_optimization_and_QP_contract'),source_fixed_R730_global_reference:true,counts:paramBinding.current_argument_and_field_counts,
    actual_future_model_identity_sha256:null,actual_future_field_point_sha256:null};
  r.complete_scientific_parameter_plan={science:records.science,pure:records.pure,whole_steps_separate_without_parameter_omission:true,complete_shared_parameter_binding:records.paramBinding,complete_delivery:records.paramManifest};
  r.queue_capacity_policy=capacity;r.complete_scientific_source_package=records.source;
  r.complete_unchanged_stage_source_package={complete_historical_source_package:immutable(records.parentRequest,'/complete_unchanged_stage_source_package'),current_complete_sources:immutable(records.sourceBinding,'/current_complete_runtime_sources'),current_complete_comparison:immutable(records.sourceBinding,'/current_role_comparison'),normal_stages:32,all_original_equations_and_angular_orders_retained:true};
  r.complete_parameter_reproducer=settings.parameterReproducer;
  const peers=immutable(records.paramBinding,'/complete_peer_responsibility');
  r.external_unregistered_peer_obligations={whole_current:peers,whole_original:immutable(records.parentRequest,'/external_unregistered_peer_obligations')};
  r.external_peer_status={whole_current:peers,whole_parent:immutable(records.parentRequest,'/external_peer_status'),supported_original_CLI_count:5,current_external_pairs:paramBinding.complete_peer_responsibility.external_pair_count,previous_failures_and_unknowns_unchanged:true};
  r.seed_and_mean_contract={whole_old:immutable(records.parentRequest,'/seed_and_mean_contract'),complete_current_R730:immutable(records.paramBinding,'/complete_R730_seed_contract'),complete_current_interfaces:immutable(records.sourceBinding,'/interfaces'),old_mean_input_or_certificate_inherited:false};
  r.complete_display_correspondence={complete_original:immutable(records.parentRequest,'/complete_display_correspondence'),complete_current:immutable(records.paramBinding,'/complete_R730_selector_maps'),complete_counts:paramBinding.current_argument_and_field_counts};
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
  r.transport_window_extension={...parent.transport_window_extension,whole_immediate_parent_extension:immutable(records.parentRequest,'/transport_window_extension'),window_changed_from_actual_parent_run32:false};
  r.current_scientific_source_and_parameter_publications={source:settings.sourcePublication,parameters:settings.parameterPublication,physical_seed_proof_publication:source.complete_R730_proof.publication,previous_publications:immutable(records.parentRequest,'/current_scientific_source_and_parameter_publications')};
  r.original_request_key_count=Object.keys(parent).length;
  r.retry_scope={whole_parent_history:immutable(records.parentRequest,'/retry_scope'),independent_new_physical_reference:true,old_final_used:false,current_run_id:null,current_source_checkout:null,current_model:null,current_point:null,current_report:null};
  r.complete_current_launch_source_and_inputs={whole_current_scientific_delivery:records.source,whole_current_parameter_delivery:records.paramManifest,complete_input_sources:r.complete_input_sources,
    complete_normal_build:immutable(records.source,'/normal_build_route'),complete_scientific_registry:r.complete_source_role_registry,
    wrapper:source.complete_source_reproduction.wrapper,builder:source.complete_source_reproduction.recipe,original_inner_entries:{science:input.sourceBinding.current_complete_runtime_sources.launcher,pure:input.sourceBinding.current_complete_runtime_sources.reader},
    runner_reconstructs_all17_whole_files_before_entry:true,reference_and_physical_report_identity_known_only_after_actual_run:true};
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
