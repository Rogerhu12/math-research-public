#!/usr/bin/env node
// Complete source/parameter text reproduction only; not a scientific entry or gate.
import {readFileSync,writeFileSync,mkdirSync,existsSync} from 'node:fs';
import {resolve,dirname} from 'node:path';
import {createHash} from 'node:crypto';
const parents=[{"role":"science","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-producer-bound-science-complete-ready.json","bytes":97806,"sha256":"75fef2a2d4505cc0e35941f5b7d6b33c8565af7a925171c2f5f61fa203478018"},{"role":"pure","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-producer-bound-pure-complete-ready.json","bytes":85234,"sha256":"74b548fe85faa89b4f0109e8b10fe4c70d524ebade97698245a8c26efc85f0c8"},{"role":"display","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-producer-bound-progress-display-correspondence.json","bytes":24461,"sha256":"255b0926e53556f53089d5371b5a9ef2631e1b6f9ea9374cf19ccedb69eb4be4"}];
const expected=[{"name":"fixed-fejer-meridian-bhalf-complete-display-correspondence.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-complete-display-correspondence.json","bytes":25057,"sha256":"cc564e5c273367242aae226913a0dd82ae5b88b3e166fbcbb8da68d6c04edb2d","git_blob_sha":"fac08bdbafbefd0e599687e2b7f0a5c6e71382e7","sha":"fac08bdbafbefd0e599687e2b7f0a5c6e71382e7"},{"name":"fixed-fejer-meridian-bhalf-science-complete-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-science-complete-ready.json","bytes":90652,"sha256":"242dd96148ddee96cf829433a4f399e2a2bc052671a92905722c8de8110f2c67","git_blob_sha":"9c4c28ef3c5b189e094c65f51038fafeef48bc48","sha":"9c4c28ef3c5b189e094c65f51038fafeef48bc48"},{"name":"fixed-fejer-meridian-bhalf-pure-complete-ready.json","path":"topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-pure-complete-ready.json","bytes":80254,"sha256":"8a5f9ff71bc598f77b25c36aeaad833f048dc6b4d218de2df44fda92709e73b7","git_blob_sha":"202b6ca81c72c009c34c04094ef234db2e337328","sha":"202b6ca81c72c009c34c04094ef234db2e337328"}];
function mapNamespace(v){
 const oldName="fixed-fejer-meridian-batched-producer-bound",newName="fixed-fejer-meridian-batched-bhalf-first";
 if(typeof v==="string")return v.split(oldName).join(newName);
 if(Array.isArray(v))return v.map(mapNamespace);
 if(v&&typeof v==="object")return Object.fromEntries(Object.entries(v).map(([k,x])=>[k.split(oldName).join(newName),mapNamespace(x)]));
 return v;
}
function makeDisplay(parent){
 const d=JSON.parse(JSON.stringify(parent));
 d.parameter_parent_schema=d.schema;d.schema="complete-fixed-fejer-meridian-bhalf-progress-display-correspondence-v1";
 d.parameter_parent_current_live_mapping=JSON.parse(JSON.stringify(d.current_live_mapping));
 d.current_live_mapping=mapNamespace(d.current_live_mapping);
 d.actual_current_scientific_result_inferred=false;
 d.current_parameter_scope={boundary_total_length:"1/2",profile_delta:"1/32",actual_run_id:null,actual_field_point_sha256:null,all48_current_scalar_selectors_preserved:true,all_historical_mapping_records_retained:true,only_current_runner_output_namespace_changed:true};
 return d;
}
function makeReady(parent,mode,displayRecord){
 const d=JSON.parse(JSON.stringify(parent)),p="topics/visible-flex-larger-amplitude/";
 for(const key of ["schema","scope","complete_current_display_correspondence","complete_parameter_constructor_path","complete_sibling_ready_paths","actual_run_id","actual_run_attempt","actual_prior_failed_entry","actual_existing_input_scope","all_original_arguments_and_defaults_retained","only_current_script_and_output_namespaces_changed_from_wide_parent"])if(Object.prototype.hasOwnProperty.call(d,key))d["parameter_parent_"+key]=d[key];
 d.schema="complete-fixed-fejer-meridian-bhalf-"+mode+"-parameters-v1";
 d.scope="Complete independent same-fixed-g M160/J923/N2048/32-stage science with b/S=1/2 and delta=1/32. The only changed scientific numerical input from the complete producer-bound parent is the supported seed boundary total length 1/4 -> 1/2. All free variables, original numerical budgets, root iterations, QP and restoration directions, line trials, complete geometry domains, original formal/live selectors and all unknown history obligations remain. Two necessary inputs must be freshly built in this independent public runner; no old run's field, mean roots, input-file hashes, accepted state, checkpoint or fees are inherited. Parent initialization failures and all parameter/source metadata remain historical provenance.";
 d.complete_current_display_correspondence=displayRecord;
 d.complete_parameter_constructor_path=p+"scripts/resume_20261126/reproduce_fixed_fejer_bhalf_complete_parameters.mjs";
 d.complete_sibling_ready_paths=[p+"computations/fixed-fejer-meridian-bhalf-science-complete-ready.json",p+"computations/fixed-fejer-meridian-bhalf-pure-complete-ready.json"];
 d.actual_run_id=null;d.actual_run_attempt=null;
 delete d.actual_prior_failed_entry;
 d.actual_existing_input_scope={run:null,attempt:null,two_complete_necessary_inputs_already_returned:false,reference_sha256:null,preparation_sha256:null,actual_model_identity_sha256:null,fresh_independent_inputs_required:true,no_cross_runner_raw_migration:true};
 d.all_original_arguments_and_defaults_retained=false;
 d.all_original_argument_positions_and_numerical_budgets_retained_except_explicit_seed_input=true;
 d.only_current_script_and_output_namespaces_changed_from_wide_parent=false;
 d.only_scientific_numerical_argument_change_from_immediate_parent={flag:"--seed-boundary-total-length",before:"1/4",after:"1/2",delta_flag:"--seed-profile-delta",unchanged_delta:"1/32"};
 d.complete_parameter_parent={path:p+"computations/fixed-fejer-meridian-producer-bound-"+mode+"-complete-ready.json",bytes:mode==="science"?97806:85234,sha256:mode==="science"?"75fef2a2d4505cc0e35941f5b7d6b33c8565af7a925171c2f5f61fa203478018":"74b548fe85faa89b4f0109e8b10fe4c70d524ebade97698245a8c26efc85f0c8",git_blob_sha:mode==="science"?"432a30604fd104dbfcb318c0fd57846010b1dfef":"41fdc59bf7d7d1cefaec2653ecef853c4b5db670",published_source_commit:"8c1251a01aa2a1893386b69d13ab1e0a5ae4aa38"};
 d.parameter_parent_complete_step_scopes=d.steps.map(x=>({id:x.id,scope:x.scope}));
 d.steps=d.steps.map(mapNamespace);
 for(const s of d.steps)s.scope="Complete b/S=1/2, delta=1/32 independent same-fixed-g "+mode+"; all original parameters and domains retained except the documented seed input. Full prior step scopes are preserved separately as parameter provenance.";
 if(mode==="science"){const a=d.steps[0].args,at=a.indexOf("--seed-boundary-total-length");if(at<0||a[at+1]!=="1/4")throw Error("complete seed parent mismatch");a[at+1]="1/2";}
 d.planned_seed_parameters={relative_boundary_total_length:"1/2",profile_delta:"1/32",each_of_four_boundary_layers_relative_length:"1/8",combined_central_relative_length:"3/8",each_of_two_central_relative_length:"3/16",input_domain_is_legal:true,actual_mean_root_and_angular_jets_proved:false,metric_or_geometric_improvement_assumed:false};
 d.complete_choice_note={path:p+"notes/2026-11-27-actual18-six-constraints-and-bhalf-seed-choice.md",bytes:11002,sha256:"045921b3670fb7fd33f8fcafd033ffeab1a87b6314b06984a0bcb0e65f734778",git_blob_sha:"9869a8b031ed5371b79d0c4dfe6a052f4991416a"};
 d.external_unregistered_peer_obligations=[...d.external_unregistered_peer_obligations,["46062343475/1","10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f"]];
 d.external_peer_status="Original five supported CLI pairs and all historical unknowns remain unchanged. Additional external runs are declarations of provenance and unknown whole scientific history, not typed-transfer inputs or evidence of accepted/final fields. Runs12-15 official cancellations are preserved separately; those terminations do not manufacture missing scientific state.";
 d.original_numerical_budgets_not_reduced=true;
 d.complete_current_scientific_source_family_is_identical_to_parent=true;
 d.new_source_patch_or_fixture_or_AST_or_review_gate_added=false;
 d.future_actual_reference_identity_sha256=null;d.future_actual_target_file_sha256=null;d.future_actual_model_identity_sha256=null;d.future_actual_final_checkpoint_sha256=null;
 d.serialization="Compact UTF-8 JSON plus newline; all original fields, full steps, source/parameter histories and selector maps retained.";
 return d;
}
function digest(body,algorithm='sha256'){return createHash(algorithm).update(body).digest('hex');}
function record(path,body){const bytes=Buffer.byteLength(body),sha=digest(Buffer.concat([Buffer.from('blob '+bytes+'\0'),Buffer.from(body)]),'sha1');return {name:path.split('/').pop(),path,bytes,sha256:digest(body),git_blob_sha:sha,sha};}
const argv=process.argv.slice(2);
function option(name){const at=argv.indexOf(name);if(at<0||!argv[at+1])throw Error('Required '+name);return argv[at+1];}
const repo=resolve(option('--repo')),out=resolve(option('--out')),loaded={};
for(const r of parents){const body=readFileSync(resolve(repo,r.path),'utf8');if(Buffer.byteLength(body)!==r.bytes||digest(body)!==r.sha256)throw Error('Whole parent mismatch '+r.path);loaded[r.role]=JSON.parse(body);}
const displayPath='topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-complete-display-correspondence.json';
const displayBody=JSON.stringify(makeDisplay(loaded.display))+'\n',displayRecord=record(displayPath,displayBody);
const bodies=new Map([[displayPath,displayBody]]);
for(const mode of ['science','pure'])bodies.set('topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-bhalf-'+mode+'-complete-ready.json',JSON.stringify(makeReady(loaded[mode],mode,displayRecord))+'\n');
for(const r of expected){const body=bodies.get(r.path),actual=record(r.path,body);if(actual.bytes!==r.bytes||actual.sha256!==r.sha256||actual.git_blob_sha!==r.git_blob_sha)throw Error('Complete output mismatch '+r.path);const dest=resolve(out,r.path);mkdirSync(dirname(dest),{recursive:true});if(existsSync(dest)&&readFileSync(dest,'utf8')!==body)throw Error('Refuse different existing output '+r.path);writeFileSync(dest,body);}
for(const r of parents){const body=readFileSync(resolve(repo,r.path),'utf8');if(Buffer.byteLength(body)!==r.bytes||digest(body)!==r.sha256)throw Error('Parent changed '+r.path);}
process.stdout.write(JSON.stringify({scope:'Complete text-only reproduction; no scientific execution, AST, compile, fixture or admission gate',outputs:expected})+'\n');
