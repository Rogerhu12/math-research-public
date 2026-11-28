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
  "parentParameterManifest": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-R729-bhalf-complete-parameter-delivery.json",
    "bytes": 13512,
    "sha256": "38c4d00bc80d96733f3f6aad4388608a49158476ec8c94207c4441c22519f742",
    "git_blob_sha": "739592eac6394174a90863d0fc903f597b40163c"
  },
  "parentBinding": {
    "role": "binding",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-R729-bhalf-complete-parameter-binding.json",
    "bytes": 22016,
    "sha256": "0c8f4e8f15936600d64c55aabc9e1f2aeebdb5a470c86b813f4f45f139594587",
    "git_blob_sha": "8469f30893db495b86f8602c4afddc8b0c7de284"
  },
  "parentScience": {
    "role": "science",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-R729-bhalf-science-complete-ready.json",
    "bytes": 78562,
    "sha256": "4ce7a7e09cd27d7ac7388683da8deb1ca6117c27a99e89debb39efacbbd18815",
    "git_blob_sha": "e37465ec696609b7d0ed87a4bd7819faec3b46c5"
  },
  "parentPure": {
    "role": "pure",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-R729-bhalf-pure-complete-ready.json",
    "bytes": 67817,
    "sha256": "7368155f3a3424d517525a35035f4ed60cad90554919df8e5a26a6916230f70a",
    "git_blob_sha": "63400f463d39cb92f79aa22b2686de33098fc125"
  },
  "parentLaunchManifest": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-R729-run32-complete-launch-delivery.json",
    "bytes": 13656,
    "sha256": "6b8b78ae8252174d513894415b908c4602db06b98bf188c8db50d008420c1bb9",
    "git_blob_sha": "90b5f82413ae08c2e3fa8bf2cc98bb25e4d0a1cc"
  },
  "parallelBinding": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-R729-bhalf-complete-parameter-binding.json",
    "bytes": 30172,
    "sha256": "ca81f91c4e5eb6eed2b36b0e731628b6226ab1730e343ac30d06a52c7167668a",
    "git_blob_sha": "63cff3ff35deba4309a41cf01fe4cae6e2433700"
  }
};
const settings={
  "when": "2026-11-28 09:51:48 UTC",
  "request": "visible-larger-resume-20261128-34",
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
  "sourcePublication": "8fb792e78b0cb67e37177a4a590fd3424e279cb2",
  "peerEvidence": [
    {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46125006601-1-part-001.md",
      "bytes": 16606,
      "sha256": "9093d0d9ba35852e8b5857066ea7a8ca4999e5ae962d5835302ea67b9852ed83",
      "git_blob_sha": "86914149fcfbe442a9dd8f3c6af42fceac10ee85",
      "fixed_commit": "56c35c4ca2d36e03831702cf1a4a1ba9ebb8efeb"
    },
    {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46125006601-1.md",
      "bytes": 55164,
      "sha256": "26dca16a43df1983195c0c8819ad1bdfdea29c4cd85cc5b8dbe70658790c9911",
      "git_blob_sha": "046fe32a8fb426dbc7c497efa2d4627d7e4c6090",
      "fixed_commit": "56c35c4ca2d36e03831702cf1a4a1ba9ebb8efeb"
    },
    {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46130690181-1-part-001.md",
      "bytes": 5756,
      "sha256": "466eff9ea7e6262c86fb827fcfd09c21dcefca91c1e3887470e570eafdbefe18",
      "git_blob_sha": "a9c146a0cbef11f78d0c839e7f93786c84ea2ddc",
      "fixed_commit": "56c35c4ca2d36e03831702cf1a4a1ba9ebb8efeb"
    },
    {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46130690181-1.md",
      "bytes": 49260,
      "sha256": "9b71dd2ce4e34a11d037fb2d30be45815602169f76c9475881d138e88bfedc01",
      "git_blob_sha": "002947e90bbcec8332dd5db5e20238abcefd799a",
      "fixed_commit": "56c35c4ca2d36e03831702cf1a4a1ba9ebb8efeb"
    }
  ],
  "additionalPeerPairs": [],
  "peerContext": {
    "run32": {
      "run": "46125006601/1",
      "complete_launch_delivery": {
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-R729-run32-complete-launch-delivery.json",
        "bytes": 13656,
        "sha256": "6b8b78ae8252174d513894415b908c4602db06b98bf188c8db50d008420c1bb9",
        "git_blob_sha": "90b5f82413ae08c2e3fa8bf2cc98bb25e4d0a1cc"
      },
      "science_source_checkout": "20911541326908882a45a1a1815ec8a05ebb4420",
      "historical_evidence_only": true
    },
    "run33": {
      "run": "46130690181/1",
      "job_id": 140934949073,
      "launch_delivery": {
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-halfwave-R729-run33-complete-launch-delivery.json",
        "bytes": 20866,
        "sha256": "b6ae795cc70a470baf74c5be6fd0ded7ed5abc3c5d7ffdfba41f2493de391452",
        "git_blob_sha": "61b5d57237db921586d23ce11c3a093b06e20790"
      },
      "actual_driver_or_point_inferred_from_planned_source": false
    },
    "current_old_peer_values_as_new_science_input": false
  }
};
const expected={
  "binding": {
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

function buildParameters(input,records,settings,identity) {
  const {source,sourceBinding,parentBinding,parentScience,parentPure,parallelBinding}=input;
  const paths=settings.paths, namespace=sourceBinding.proposed_namespace;
  const io={science:parentScience,pure:parentPure};
  const parent={science:records.parentScience,pure:records.parentPure};
  const immutable=(complete_file,json_pointer='')=>({complete_file,json_pointer,whole_file_required:true});
  const wire=value=>JSON.stringify(value)+'\n';
  const previous=parentScience.namespace;
  const native=source.normal_build_route;
  const seed=sourceBinding.mathematical_problem;
  const budget=parentBinding.complete_original_budgets;
  const legacy={};
  const working={};
  const originalArgs=parentScience.steps[0].args;
  for(const [kind,options] of [['legacy',['boundary-total-length','profile-delta']],['working',['radial-quadrature-order','profile-quadrature-order','mean-maxiter','mean-tolerance','scalar-iterations','mean-backtracks','mean-armijo']]]) {
    for(const option of options) {
      const flag='--seed-'+option;
      (kind==='legacy'?legacy:working)[flag]=originalArgs[originalArgs.indexOf(flag)+1];
    }
  }
  const frozen={...sourceBinding.future_actual,build_receipt_sha256:null,accepted_field:null,certificate:null};
  const contract={
    complete_mathematical_problem:seed,
    complete_physical_proof:source.complete_R730_proof,
    complete_seed_source:sourceBinding.current_complete_runtime_sources.seed_reference,
    complete_length_source:sourceBinding.current_complete_runtime_sources.seed_length_kernel,
    complete_source_interfaces:sourceBinding.interfaces,
    legacy_unused:legacy,
    actual_length_parameters:working,
    length_parameters_constructor_order:['radial_quadrature_order','profile_quadrature_order','mean_maxiter','mean_tolerance','scalar_iterations','mean_backtracks','mean_armijo'],
    fixed_parameters:{eta:'1/32',xi_max:'3/4',k:6,pulse:'(1-(2*t-1)^12)^7',polynomial_degree:84,internal_cuts:[]},
    accurate_curve:'G_xi=((1-xi*psi)*baseline_xy,baseline_z) with the six original R730 Bezier controls at the frozen initial chart/core/height.',
    complete_length_equation:'integral_0^1 |d_t G_xi| dt = S; 0 < xi(phi) < 3/4',
    complete_inverse_equation:'integral_0^t |d_u G_xi(phi)| du = s, F(s,phi)=G_xi(phi)(t(s,phi),phi), T0=F_s',
    complete_working_inverse:'Positive full-mesh-cell prefix table and positive Gauss partial cell; target (s/S)*actual_total_length(phi). Two implicit length and inverse angle jets use the full working rule.',
    complete_immutable_batch_address:'selected complete own-point snapshot -> operator_metadata_snapshot JSON -> base_complete_metadata -> fixed_safe_cone_unit_seed -> length_root_batch_records',
    saved_root_and_inverse_coefficients:source.actual_interface.actual_saved_length_objects,
    old_R728_mean_arrays_inherited:false,old_R727_certificate_inherited:false,same_as_normal_control_inverse:false
  };
  const shared={R730_seed_schema:'safe_cone_seed_definition.schema',R730_seed_identity:'safe_cone_seed_identity_sha256',
    R730_seed_provider_sha256:'safe_cone_seed_binding.source_sha256',R730_length_kernel_sha256:'safe_cone_seed_binding.length_kernel_source_sha256',
    R730_reference_identity:'safe_cone_seed_binding.reference_model_identity_sha256',R730_original_scalar:'safe_cone_seed_binding.fixed_scalar_metric_identity_sha256',
    R730_handle_length:'safe_cone_seed_definition.exact_physical_handle_length',R730_maximum_contraction:'safe_cone_seed_definition.exact_maximum_contraction',
    R730_frozen_core_curvature:'safe_cone_seed_definition.exact_core_radial_curvature',R730_legacy_unused_boundary:'R730_legacy_shape_CLI_unused.boundary',
    R730_legacy_unused_delta:'R730_legacy_shape_CLI_unused.delta'};
  for(const key of ['pulse','pulse_flatness','polynomial_degree','working_order','accurate_length_equation','accurate_inverse_equation','root_tolerance_hex','armijo_hex']) shared['R730_'+key]='safe_cone_seed_definition.complete_safe_cone_definition.'+key;
  for(const key of ['mean_maxiter','scalar_iterations','mean_backtracks']) shared['R730_'+key]='safe_cone_seed_definition.complete_safe_cone_definition.complete_root_budgets.'+key;
  const science={...shared,R730_frozen_seed:'safe_cone_seed_is_frozen_from_original_core_and_height',R730_outer_omega_retained:'safe_cone_seed_does_not_replace_current_outer_omega',R730_inverse_scope:'safe_cone_length_inverse_is_not_a_normal_control_inverse_certificate'};
  const pure={...shared,R730_inverse_scope:'seed_length_inverse_is_not_current_normal_control_inverse_certificate'};
  const rawPrefix='latest_operator_metadata.base_complete_metadata.fixed_safe_cone_unit_seed.';
  for(const key of ['completed_literal_angle_count','all_bound_input_and_source_bytes_rechecked','accurate_length_root_error_or_global_branch_certified','continuous_metric_geometry_or_full_phase_certificate']) science['R730_'+key]=rawPrefix+key;
  for(const key of ['reference_evaluations','requested_points','requested_literal_angles','completed_root_batches','radial_query_batches','angle_cache_hits','new_literal_angles']) {
    science['R730_count_'+key]=rawPrefix+'counts.'+key;
    pure['R730_count_'+key]='seed_diagnostics.actual_counts.'+key;
  }
  for(const key of ['completed_literal_angle_count','completed_root_batch_count','complete_batch_recorded_angle_count','complete_batch_records_match_cached_angle_count','last_seed_failure_phase','last_seed_failure_reason','old_mean_v_d_w_lambda_arrays_or_roots_inherited','seed_root_or_angle_jet_error_enclosed','seed_quadrature_or_normalization_error_enclosed','seed_continuous_metric_or_geometry_certified']) pure['R730_'+key]='seed_diagnostics.'+key;
  const build={};
  for(const key of ['schema','complete','phase','source_commit','workflow_trigger_commit','github_run_id','github_run_attempt','node_version','python_version','original_entry_kind','original_entry_argument_count','generated_sources_complete','builder_returncode','child_started','child_returncode','successful_process_return']) build['R730_build_'+key]=key;
  for(const [name,path] of [['wrapper_source','wrapper_source.sha256'],['source_builder','complete_source_builder.sha256'],['entry_source','actual_original_entry_source.sha256'],['full_materialization','complete_materialization_record.sha256'],['full_file_count','complete_materialization.complete_source_file_count']]) build['R730_build_'+name]=path;
  const scienceScope='Independent global R730 safe-cone reference with full R729 solver. Rebuild the complete current runtime in this source checkout and execute the whole scientific entry. Retain original variables, full domains, 32 normal stages, all original budgets, line trials and original-first QP. Report actual length and inverse data separately from the normal solve.';
  const pureScope='Materialize the same complete R730 scientific sources in this detached checkout and read only the actual same-run R730/R729 report, thirteen-member final and typed history with the full reader. Retain all original diagnostics and their missing-field errors. No solver, root or field evaluation.';
  const steps={}, counts={};
  for(const kind of ['science','pure']){
    const old=io[kind].steps[0];
    const step=JSON.parse(JSON.stringify(old).replaceAll(previous,namespace));
    const [report,selectors]=Object.entries(step.summary)[0];
    const added=kind==='science'?science:pure;
    step.id=(kind==='science'?'complete-':'actual-')+namespace+'-20261128';
    step.script=native.wrapper_entry_script;
    step.scope=kind==='science'?scienceScope:pureScope;
    const prefix=native['wrapper_argument_prefix_'+kind];
    const receipt=prefix[3].replace('{work}/','');
    const orig=step.args;
    step.args=[...prefix,...orig];
    step.outputs.push(receipt,receipt+'.materialization.json');
    step.summary={[report]:{...selectors,...added},[receipt]:build};
    steps[kind]=step;
    counts[kind]={inner_argv:orig.length,wrapper_argv:step.args.length,parent_formal:Object.keys(selectors).length,
       new_R730_formal:Object.keys(added).length,new_build_formal:Object.keys(build).length,
       all_formal:Object.keys(selectors).length+Object.keys(added).length+Object.keys(build).length,
       live:Object.values(step.progress_summary||{}).reduce((n,x)=>n+Object.keys(x).length,0)};
  }
  const peer=parallelBinding.complete_peer_responsibility,known=peer.complete_current_external_pairs.map(x=>[...x]);
  for(const row of parentBinding.complete_peer_responsibility.complete_current_external_pairs) if(!known.some(x=>x[0]===row[0]&&x[1]===row[1])) known.push([...row]);
  for(const row of settings.additionalPeerPairs) if(!known.some(x=>x[0]===row[0]&&x[1]===row[1]))known.push([...row]);
  const binding={
    schema:'complete-fixed-fejer-R730-R729-independent-run34-parameters-v1',repository:source.repository,topic:source.topic,prepared_utc:settings.when,
    intended_runner_label:34,request_id:settings.request,namespace,current_scientific_source_publication_at_preparation:settings.sourcePublication,
    complete_parent_files:records,complete_current_scientific_source_delivery:records.source,complete_current_source_binding:records.sourceBinding,
    complete_runtime_sources:immutable(records.sourceBinding,'/current_complete_runtime_sources'),complete_role_registry:immutable(records.sourceBinding,'/complete_source_role_registry'),
    runtime_files:source.current_runtime_count,scientific_roles:source.current_scientific_role_count,complete_role_comparison:source.current_role_comparison,
    complete_frozen_original_138_source_pairs:immutable(sourceBinding.frozen_history.complete_parent_binding,'/complete_source_role_registry'),
    complete_build_provenance:immutable(records.source,'/normal_build_route'),complete_original_budgets:budget,budget_shape_CLI_semantics:'The two inherited shape words under complete_original_budgets are legacy_unused only.',
    full_original_stage_optimization_and_QP_contract:seed.inherited_exact_optimizer_scope,complete_R730_seed_contract:contract,
    complete_parent_ready_metadata:{science:immutable(parent.science),pure:immutable(parent.pure)},
    current_argument_and_field_counts:counts,complete_R730_selector_maps:{science,pure,build},full_parent_selector_maps:{science:immutable(parent.science,'/steps/0/summary'),pure:immutable(parent.pure,'/steps/0/summary')},
    old_formal_selectors:'All old label/path pairs remain literal, including historical mean-field selectors. Absent old physical fields retain original missing-key errors. No fictitious compatibility data is manufactured.',
    complete_live_selectors:immutable(parent.science,'/steps/0/progress_summary'),complete_R729_display:immutable(records.parentBinding,'/complete_R729_formal_selector_correspondence'),
    complete_peer_responsibility:{whole_run32:immutable(records.parentBinding,'/complete_peer_responsibility'),whole_run33:immutable(records.parallelBinding,'/complete_peer_responsibility'),complete_external_pairs:known,external_pair_count:known.length,extra_peer_source_context:settings.peerContext,fixed_observation_records:settings.peerEvidence,
      five_original_pending_CLI_pairs_remain_unchanged:true,new_cli_or_parent_family_entries:0,previous_failures_and_unknown_histories_preserved:true,previous_final_or_mutable_progress_as_input:false},
    original_scientific_inputs_reconstructed_on_own_runner:true,full_source_and_step_construction:'Complete parent steps, exact namespace substitutions only in inner argv, full source-build prefix and full new source binding. The run34 output directory and pure report paths are independent.',actual_future:frozen
  };
  const bindingText=wire(binding),bindingRecord=identity(paths.binding,bindingText),result={binding:bindingText};
  for(const kind of ['science','pure']){
    result[kind]=wire({schema:'complete-fixed-fejer-R730-R729-independent-run34-ready-v1',prepared_utc:settings.when,kind,executed:false,intended_runner_label:34,request_id:settings.request,namespace,
      complete_parameter_binding:bindingRecord,whole_current_source_delivery:records.source,complete_parent_ready_metadata:immutable(parent[kind]),
      complete_physical_reference:immutable(bindingRecord,'/complete_R730_seed_contract'),complete_current_source_registry:immutable(records.sourceBinding,'/complete_source_role_registry'),
      complete_peer_responsibilities:immutable(bindingRecord,'/complete_peer_responsibility'),complete_formal_scope:immutable(bindingRecord,'/old_formal_selectors'),counts:counts[kind],actual_future:frozen,
      steps:[steps[kind]]});
  }
  return result;
}

const argv=process.argv.slice(2);
if(argv.length!==4||argv[0]!=='--source-repository'||argv[2]!=='--output-repository')
  throw Error('Use --source-repository ROOT --output-repository OUTPUT');
const root=resolve(argv[1]), output=resolve(argv[3]), input={};
for(const [key,record] of Object.entries(records)){
  const source=readWhole(root,record);
  input[key]=record.path.endsWith('.json')?JSON.parse(source):source;
}
const files=buildParameters(input,records,settings,identity);
for(const [key,body] of Object.entries(files)){
  if(!expected[key]||!equal(expected[key],body)) throw Error('Regenerated complete text differs: '+key);
  const path=resolve(output,expected[key].path);
  if(!path.startsWith(output+sep)) throw Error('Expected an output inside the indicated repository');
  mkdirSync(dirname(path),{recursive:true});
  writeFileSync(path,body,{encoding:'utf8'});
}
console.log(JSON.stringify(expected,null,2));
