#!/usr/bin/env node
/** Reproduce the complete R732 parameter binding and both independent Actions steps. */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
const records={
  "old_manifest": {
    "role": "parent_parameters",
    "name": "fixed-fejer-r730-R729-complete-parameter-delivery.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r730-R729-complete-parameter-delivery.json",
    "bytes": 10643,
    "sha256": "ac63c2fb4ef9fba1867dedd8cc3d42ed0e7ac2ca0856b1164b774bed9e43f528",
    "git_blob_sha": "6d1bf823988ffd202639ea678062252bb8492449"
  },
  "old_binding": {
    "role": "binding",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r730-R729-complete-parameter-binding.json",
    "bytes": 36310,
    "sha256": "b53af2212ab7e574afc7d65f6607594a64c6f32ce6ecbffe2901730cda9b8a91",
    "git_blob_sha": "2bc4198d68ee3f605f9f4bedbafefd8e67d8d510"
  },
  "old_science": {
    "role": "science",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r730-R729-science-complete-ready.json",
    "bytes": 80179,
    "sha256": "e59560d83da7c287458ac24814b25fa22f3465f1df42c4729d9b283f80c124ca",
    "git_blob_sha": "3521520ffc6ca45a52d21f56b83bd74df423969d"
  },
  "old_pure": {
    "role": "pure",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r730-R729-pure-complete-ready.json",
    "bytes": 69444,
    "sha256": "9cfe04f62d8eb60d808c2ab0c7733f9a2d803a831c6c64de0378c4090dbe139f",
    "git_blob_sha": "39a7df0497e21c90cf93dfe919d280d4e0572446"
  },
  "new_source": {
    "role": "complete_scientific_source_delivery",
    "name": "fixed-fejer-r732-R729-complete-source-delivery.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r732-R729-complete-source-delivery.json",
    "bytes": 36718,
    "sha256": "7ac0fac5bed253862db708c87892c9908a87ba31a6ceab01460e7a1ce5da3902",
    "git_blob_sha": "069f2d0267355893ac69334d8e845a19c59a0358"
  },
  "new_registry": {
    "role": "complete_runtime_and_source_binding",
    "name": "fixed-fejer-r732-R729-current-runtime-binding.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r732-R729-current-runtime-binding.json",
    "bytes": 66334,
    "sha256": "425a1c0f484de848fdc66396623bc8e434b92bcfaf07216b49149a7324e7a195",
    "git_blob_sha": "ba50a6fa07a086964c2c99c9fb2580c702427915"
  }
};
const settings={
  "prepared_utc": "2026-11-28 10:37:37 UTC",
  "runner": 35,
  "request_id": "visible-larger-resume-20261128-35",
  "source_publication": null,
  "run34": {
    "run_id": 46135301432,
    "attempt": 1,
    "status_at_preparation": "in_progress",
    "source_or_results_inherited": false
  },
  "run33": {
    "run_id": 46133839513,
    "attempt": 1,
    "status_at_preparation": "in_progress",
    "source_or_results_inherited": false
  }
};
function identity(file,body) {
  const b=Buffer.from(body,'utf8');
  const sha=(alg,v)=>crypto.createHash(alg).update(v).digest('hex');
  return {path:file,bytes:b.length,sha256:sha('sha256',b),
    git_blob_sha:sha('sha1',Buffer.concat([Buffer.from('blob '+b.length+'\0'),b]))};
}

function make(inputs,docs,settings,identity) {
  const old=docs.old_binding, source=docs.new_registry, delivery=docs.new_source;
  const ns='fixed-fejer-r732-R729-first', before='fixed-fejer-r730-R729-first';
  const currentPath=name=>source.topic+'/computations/fixed-fejer-r732-R729-'+name+'.json';
  const whole=(complete_file,json_pointer='')=>({complete_file,json_pointer,whole_file_required:true});
  const now=settings.prepared_utc, id=settings.request_id;
  const frozen=docs.old_manifest;
  const readies={},argsByKind={},maps={},counts={};
  const endKeys=['beta_law_source_sha256','beta_width_exact','beta_kappa_exact','physical_S_hex',
    'central_length_hex','A_hex','constant_end_hex','uf_hex','xf_hex','hf_hex','L_hex','Rv_hex','Z_hex',
    'order','mathematical_formula_cuts_are_preserved','working_end_integral_and_infinite_tail_rounding_enclosed'];
  for(const kind of ['science','pure']) {
    const parent=docs['old_'+kind],numeric=kind==='science',oldStep=parent.steps[0];
    const replacePath=v=>v.replaceAll(before,ns).replaceAll('r730-'+kind+'-source-build','r732-'+kind+'-source-build')
      .replaceAll('build_and_launch_r730_R729_actions','build_and_launch_r732_R729_actions');
    const step={...oldStep,id:replacePath(oldStep.id),script:source.source_materialization.wrapper.path,
      scope:numeric?'R732 full rounded-end and S-L central seed in the complete 139-role R729 SO3 optimizer. Original core, H and rotation variables and every original budget retained.':
      'Complete own R732/R729 report and final bundle with the original pure entry. Current reference input is bound independently to the explicitly selected immutable normal snapshot.',
      args:oldStep.args.map(replacePath),outputs:oldStep.outputs.map(replacePath)};
    if(step.id===oldStep.id)step.id=step.id.replaceAll('r730','r732').replaceAll('R730','R732');
    step.parent_bundle=replacePath(oldStep.parent_bundle);
    step.outputs.push('r732-'+kind+'-source-build.json.materialization.json.r730-materialization.json');
    if(oldStep.cleanup_generated_patterns)
      step.cleanup_generated_patterns=oldStep.cleanup_generated_patterns.map(replacePath);
    if(oldStep.progress_summary)
      step.progress_summary=Object.fromEntries(Object.entries(oldStep.progress_summary)
        .map(([file,selector])=>[replacePath(file),selector]));
    step.summary=Object.fromEntries(Object.entries(oldStep.summary).map(
      ([file,selectors])=>[replacePath(file),{...selectors}]));
    const key=step.outputs[0],record='r732-'+kind+'-source-build.json';
    const inherited=Object.values(step.summary).reduce((n,v)=>n+Object.keys(v).length,0);
    const current={};
    for(const [label,selector] of Object.entries(old.complete_R730_selector_maps[kind])) {
      current[label.replace('R730','R732')]=selector.replace('R730_legacy_shape_CLI_unused','R732_legacy_shape_CLI_unused');
    }
    const end=numeric?'safe_cone_seed_definition.working_definition.rounded_end.':
      'selected_immutable_R732_reference.rounded_end.definition.';
    for(const field of endKeys)current['R732_end_'+field]=end+field;
    const fees=numeric?'latest_operator_metadata.base_complete_metadata.fixed_safe_cone_unit_seed.rounded_end.':
      'selected_immutable_R732_reference.rounded_end.';
    for(const field of ['actual_integrals','actual_beta_queries','nonzero_argument_beta_rounded_to_zero'])
      current['R732_end_'+field]=fees+field;
    if(!numeric)for(const field of ['point_sha256','normal_model_identity_sha256','seed_model_identity_sha256',
      'snapshot_identity_sha256','capture_ordinal','snapshot_file.sha256','operator_metadata_snapshot.sha256',
      'mutable_progress_or_other_snapshot_used','continuous_certificate'])
      current['R732_selected_'+field.replaceAll('.','_')]='selected_immutable_R732_reference.'+field;
    const build=Object.fromEntries(Object.entries(old.complete_R730_selector_maps.build)
      .map(([label,selector])=>[label.replace('R730','R732'),selector]));
    for(const [label,selector] of Object.entries({parent_sha256:'sha256',parent_bytes:'bytes',
      pinned_parent_builder:'recipe.sha256',parent_source_count:'receipt.complete_source_file_count',
      parent_complete:'receipt.complete'}))build['R732_build_'+label]='complete_materialization.parent_build.'+selector;
    Object.assign(step.summary[key],current);
    Object.assign(step.summary[record],build);
    maps[kind]={working:current,build};
    const live=Object.values(step.progress_summary||{}).reduce((n,v)=>n+Object.keys(v).length,0);
    counts[kind]={inner_argv:step.args.length-5,wrapper_argv:step.args.length,parent_formal:inherited,
      new_R732_formal:Object.keys(current).length,new_build_formal:Object.keys(build).length,
      all_formal:Object.values(step.summary).reduce((n,v)=>n+Object.keys(v).length,0),live};
    argsByKind[kind]=step.args;
    readies[kind]={schema:'complete-fixed-fejer-R732-R729-independent-run'+settings.runner+'-ready-v1',
      prepared_utc:now,kind,executed:false,intended_runner_label:settings.runner,request_id:id,namespace:ns,
      whole_current_source_delivery:inputs.new_source,complete_parent_ready_metadata:whole(inputs['old_'+kind]),
      complete_current_source_registry:whole(inputs.new_registry,'/complete_source_role_registry'),
      counts:counts[kind],actual_future:{...parent.actual_future,selected_snapshot:null,terminal_work:null},steps:[step]};
  }
  const p={schema:'complete-fixed-fejer-R732-R729-full-parameter-binding-v1',repository:source.repository,
    topic:source.topic,prepared_utc:now,intended_runner_label:settings.runner,request_id:id,namespace:ns,
    current_scientific_source_publication_at_preparation:settings.source_publication,
    complete_parent_files:inputs,historical_full_source_and_parameter_inputs:old.complete_parent_files,
    complete_current_scientific_source_delivery:inputs.new_source,complete_current_source_binding:inputs.new_registry,
    complete_runtime_sources:whole(inputs.new_registry,'/current_complete_runtime_sources'),
    complete_role_registry:whole(inputs.new_registry,'/complete_source_role_registry'),runtime_files:24,scientific_roles:139,
    complete_role_comparison:source.current_role_comparison,complete_frozen_original_139_source_pairs:
      whole(old.complete_current_source_binding,'/complete_source_role_registry'),
    complete_build_provenance:whole(inputs.new_source,'/normal_build_route'),complete_original_budgets:old.complete_original_budgets,
    full_original_stage_optimization_and_QP_contract:old.full_original_stage_optimization_and_QP_contract,
    budget_shape_CLI_semantics:old.budget_shape_CLI_semantics,
    complete_R732_seed_contract:{complete_math:source.mathematical_problem,complete_proof:source.complete_mathematical_proof,
      complete_physical_deliveries:source.complete_physical_source_deliveries,
      complete_interfaces:source.interfaces,legacy_unused:old.complete_R730_seed_contract.legacy_unused,
      actual_length_parameters:old.complete_R730_seed_contract.actual_length_parameters,
      selected_snapshot:'explicit report-save hook -> exact snapshot_file -> operator_metadata_snapshot -> base_complete_metadata.fixed_safe_cone_unit_seed. Unavailable when the hook failed or cache and outer point differ.'},
    complete_parent_ready_metadata:{science:whole(inputs.old_science),pure:whole(inputs.old_pure)},
    complete_R732_selector_maps:maps,current_argument_and_field_counts:counts,
    full_parent_selector_maps:{science:whole(inputs.old_science,'/steps/0/summary'),pure:whole(inputs.old_pure,'/steps/0/summary')},
    old_formal_selectors:'All 632/625 R730 parent label/address pairs retained exactly as parent reporting addresses. Each returns the current emitted data or its genuine missing-key error. Prefixes on historical labels identify the stored query lineage, not a R730 execution. The R732-specific fields identify the new end, cut, integration and immutable selected snapshot explicitly.',
    complete_live_selectors:whole(inputs.old_science,'/steps/0/progress_summary'),
    complete_R729_display:old.complete_R729_display,complete_peer_responsibility:{...old.complete_peer_responsibility,
      parent_34_source:old.complete_current_scientific_source_delivery,parent_34_parameters:inputs.old_manifest,
      peer_34_run_observed:settings.run34,peer_33_retry_observed:settings.run33,
      previous_final_or_mutable_progress_as_input:false},original_scientific_inputs_reconstructed_on_own_runner:true,
    original_workflow_inputs:'Both original input preparation steps immediately precede the new independent science and are reproduced by the launch package. Complete pure is a follow-up to natural science return.',
    full_inner_and_outer_arguments:argsByKind,full_source_and_step_construction:'Every detached worktree builds 17 published R730 parents and 17 R732 files. The separate complete working source manifests identify all five R732 physical files.',
    actual_future:{...old.actual_future,terminal_integral:null,selected_snapshot:null}};
  const path=currentPath('complete-parameter-binding'), binding=JSON.stringify(p)+'\n';
  const pin=identity(path,binding),files=[{role:'binding',path,body:binding}];
  for(const kind of ['science','pure']) {
    const ready=readies[kind];ready.complete_parameter_binding=pin;
    ready.complete_physical_reference=whole(pin,'/complete_R732_seed_contract');
    ready.complete_peer_responsibilities=whole(pin,'/complete_peer_responsibility');
    ready.complete_formal_scope=whole(pin,'/old_formal_selectors');
    files.push({role:kind,path:currentPath(kind+'-complete-ready'),body:JSON.stringify(ready)+'\n'});
  }
  return {files,counts};
}
if(process.argv.length!==4) throw Error('Use node reproduce_r732_R729_run35_parameters.mjs REPOSITORY OUTPUT_REPOSITORY');
const root=path.resolve(process.argv[2]),dest=path.resolve(process.argv[3]);
const docs={};
for(const [key,record] of Object.entries(records)) {
  const raw=fs.readFileSync(path.join(root,record.path),'utf8'),got=identity(record.path,raw);
  if(['bytes','sha256','git_blob_sha'].some(k=>got[k]!==record[k]))throw Error('Changed whole parameter parent: '+key);
  docs[key]=JSON.parse(raw);
}
const {files}=make(records,docs,settings,identity);
for(const file of files) {
  const full=path.join(dest,file.path);
  fs.mkdirSync(path.dirname(full),{recursive:true});
  if(fs.existsSync(full)) {
    if(fs.readFileSync(full,'utf8')!==file.body)throw Error('Different existing complete file: '+full);
  } else fs.writeFileSync(full,file.body,{flag:'wx'});
  process.stdout.write(JSON.stringify(identity(file.path,file.body))+'\n');
}
