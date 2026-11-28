#!/usr/bin/env node
// Complete literal construction of three independent sources; never imports or executes science.
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {resolve,dirname} from 'node:path';
import {createHash} from 'node:crypto';
const SPEC={"schema":"complete-fixed-fejer-restoration-continuation-source-text-construction-v1","repository":"Rogerhu12/math-research-public","topic":"topics/visible-flex-larger-amplitude","prepared_utc":"2026-11-28 00:54:11 UTC","policy":{"path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_restoration_damping_continuation.py","bytes":18684,"sha256":"be523c77d488eaaaab9a18f6aa556283362f66bee0916f9d1489cd2b51c1b710","git_blob_sha":"05eb88969c5e83cf2f01fcb3f02e40f4cbea0775"},"parents":{"driver":{"path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py","bytes":99313,"sha256":"10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f","git_blob_sha":"8bba3e30bb8e843fd725a2d19f8966b984acc4ae"},"reader":{"path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_meridian_batched_so3_report.py","bytes":99382,"sha256":"8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49","git_blob_sha":"9cd36fd99113d285fc47f17bad929647c8fc6de3"},"launcher":{"name":"launch_fixed_fejer_meridian_batched_actions.py","path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_meridian_batched_actions.py","bytes":22136,"sha256":"f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506","git_blob_sha":"168b1a1d7bc58793985138eb8a02a6e3911d74cc"}},"outputs":{"driver":{"role":"driver","name":"fullclosed_fixed_fejer_restoration_continuation_so3_qp.py","path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_restoration_continuation_so3_qp.py","bytes":99763,"sha256":"9db39cd1b4c2812f5fc1b8fc2619efc4cd30271ba6b43f06bfde65004f131699","git_blob_sha":"1a50449bef3e207cc30797697a07e20437792d9b"},"reader":{"role":"reader","name":"read_fixed_fejer_restoration_continuation_so3_report.py","path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_restoration_continuation_so3_report.py","bytes":99757,"sha256":"14c2dfac957632fc46e2e6ed06a9475bcac5a9dda59692941b4553ada8c322f8","git_blob_sha":"35a93e1063a121f9e2e59594d5b8cb4ff3a666d5"},"launcher":{"role":"launcher","name":"launch_fixed_fejer_restoration_continuation_actions.py","path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_restoration_continuation_actions.py","bytes":22152,"sha256":"f2a9e38f62a3844b5d9ce8df9399f6702f37e6fc96c792d0dcb0bb61a80e1371","git_blob_sha":"e6d7013b4216935c05dad63eb7961f419f39a973"}},"patches":{"driver":[{"kind":"source_registry_addition","old":"SOURCE_PINS = {","replacement":"SOURCE_PINS = {\"restoration_damping_policy\":(\"scripts/resume_20261126/fixed_fejer_restoration_damping_continuation.py\",\"be523c77d488eaaaab9a18f6aa556283362f66bee0916f9d1489cd2b51c1b710\"),"},{"kind":"before_first_F_report_declaration","old":"    scalar_progress_module=load('_actual_fixed_fejer_mathematical_progress',paths['scalar_progress'])","replacement":"    restoration_policy=load('_restoration_policy',paths['restoration_damping_policy'])\n    restoration_policy.initialize_report(report)\n    scalar_progress_module=load('_actual_fixed_fejer_mathematical_progress',paths['scalar_progress'])"},{"kind":"after_unchanged_original_success_failure_block","old":"        record['seconds'] = time.monotonic()-started\n","replacement":"        if phase == 'restoration':\n            restoration_damping=restoration_policy.after_original_update(record,report,restoration_damping)\n        record['seconds'] = time.monotonic()-started\n"},{"kind":"current_report_schema","old":"SCHEMA = \"complete-fixed-fejer-meridian-batched-observed-material-envelope-SO3-QP-v1\"","replacement":"SCHEMA = \"complete-fixed-fejer-restoration-continuation-observed-envelope-SO3-QP-v1\""}],"reader":[{"kind":"append_pure_role_without_replacing_original_three","old":"                          ('batched_geometry_binding','bind_report')):","replacement":"                          ('batched_geometry_binding','bind_report'),\n                          ('restoration_damping_policy','validate_report')):"},{"kind":"dispatch_new_stdlib_validator_after_existing_whole_source_check","old":"        if role=='batched_geometry_binding':\n","replacement":"        if role=='restoration_damping_policy':\n            answer[role]=fn(report,source_sha256=expected)\n            continue\n        if role=='batched_geometry_binding':\n"},{"kind":"retain_complete_new_policy_decision_in_each_direction","old":"        damping=value['actual_damping'], damping_after=value.get('damping_after_direction'),\n","replacement":"        damping=value['actual_damping'], damping_after=value.get('damping_after_direction'),\n        restoration_damping_continuation=value.get('restoration_damping_continuation'),\n"},{"kind":"append_complete_policy_readout","old":"        batched_geometry_binding=extra['batched_geometry_binding'],\n","replacement":"        batched_geometry_binding=extra['batched_geometry_binding'],\n        restoration_damping_continuation=extra['restoration_damping_policy'],\n"},{"kind":"actual_driver_pin","old":"DRIVER_SHA = \"10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f\"","replacement":"DRIVER_SHA = \"9db39cd1b4c2812f5fc1b8fc2619efc4cd30271ba6b43f06bfde65004f131699\""},{"kind":"actual_report_schema","old":"REPORT_SCHEMA = \"complete-fixed-fejer-meridian-batched-observed-material-envelope-SO3-QP-v1\"","replacement":"REPORT_SCHEMA = \"complete-fixed-fejer-restoration-continuation-observed-envelope-SO3-QP-v1\""},{"kind":"actual_driver_path","old":"driver = topic/'scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py'","replacement":"driver = topic/'scripts/resume_20261126/fullclosed_fixed_fejer_restoration_continuation_so3_qp.py'"},{"kind":"current_readout_schema","old":"return dict(schema='actual-fixed-fejer-meridian-batched-observed-envelope-SO3-readout-v1',","replacement":"return dict(schema='actual-fixed-fejer-restoration-continuation-envelope-SO3-readout-v1',"}],"launcher":[{"kind":"actual_driver_pin","old":"DRIVER_SHA = \"10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f\"","replacement":"DRIVER_SHA = \"9db39cd1b4c2812f5fc1b8fc2619efc4cd30271ba6b43f06bfde65004f131699\""},{"kind":"actual_driver_path","old":"'fullclosed_fixed_fejer_meridian_batched_so3_qp.py'","replacement":"'fullclosed_fixed_fejer_restoration_continuation_so3_qp.py'"},{"kind":"current_command_schema","old":"record = dict(schema='public-actions-complete-fixed-fejer-meridian-batched-SO3-command-v1',","replacement":"record = dict(schema='public-actions-complete-fixed-fejer-restoration-continuation-SO3-command-v1',"}]},"source_role_counts":{"parent":137,"current":138,"original_pairs_unchanged":137,"added":["restoration_damping_policy"]},"schemas":{"report":"complete-fixed-fejer-restoration-continuation-observed-envelope-SO3-QP-v1","readout":"actual-fixed-fejer-restoration-continuation-envelope-SO3-readout-v1","command":"public-actions-complete-fixed-fejer-restoration-continuation-SO3-command-v1"},"no_scientific_AST_fixture_replay_or_admission_gate":true};

function identity(bytes){return {bytes:bytes.length,sha256:createHash('sha256').update(bytes).digest('hex')};}
function requireWhole(bytes,record){
 const actual=identity(bytes);
 if(actual.bytes!==record.bytes||actual.sha256!==record.sha256)
  throw new Error('Whole source identity changed: '+record.path);
 return actual;
}
function readBound(repo,record){
 const bytes=readFileSync(resolve(repo,record.path));requireWhole(bytes,record);
 return bytes.toString('utf8');
}
function once(text,oldValue,newValue,label){
 if(text.split(oldValue).length!==2)throw new Error('Unique complete literal required: '+label);
 return text.replace(oldValue,newValue);
}
function sourcePairs(text){
 const lines=text.split('\n').filter(s=>s.startsWith('SOURCE_PINS = '));
 if(lines.length!==1)throw new Error('Exactly one whole literal SOURCE_PINS assignment required');
 const list=[...lines[0].matchAll(/["']([^"']+)["']:\(["']([^"']+)["'],["']([0-9a-f]{64})["']\)/g)]
  .map(m=>[m[1],[m[2],m[3]]]);
 if(new Set(list.map(x=>x[0])).size!==list.length)throw new Error('Duplicate source role');
 return list;
}
function args(argv){
 const a={};
 for(let i=0;i<argv.length;i++){
  const k=argv[i];
  if(!['--repo','--output-directory'].includes(k)||a[k]!==undefined||i+1>=argv.length)
   throw new Error('Use --repo <complete-repository> --output-directory <generated-tree>');
  a[k]=argv[++i];
 }
 if(!a['--repo']||!a['--output-directory'])throw new Error('Both explicit source and generated roots are required');
 return a;
}
function main(){
 const a=args(process.argv.slice(2));readBound(a['--repo'],SPEC.policy);
 const generated={},parents={};
 for(const role of ['driver','reader','launcher']){
  const parent=readBound(a['--repo'],SPEC.parents[role]);parents[role]=parent;
  let text=parent;
  for(const patch of SPEC.patches[role])text=once(text,patch.old,patch.replacement,role+':'+patch.kind);
  let reverse=text;
  for(const patch of [...SPEC.patches[role]].reverse())
   reverse=once(reverse,patch.replacement,patch.old,'inverse '+role+':'+patch.kind);
  if(reverse!==parent)throw new Error('The complete inverse source differs: '+role);
  const bytes=Buffer.from(text,'utf8');requireWhole(bytes,SPEC.outputs[role]);
  if(bytes.length>=100000)throw new Error('Complete new source exceeds declared single-file bound');
  generated[role]={text,bytes};
 }
 const before=sourcePairs(parents.driver),after=sourcePairs(generated.driver.text);
 if(before.length!==137||after.length!==138)throw new Error('Actual complete role count differs');
 const extra=after.filter(([role])=>role==='restoration_damping_policy');
 if(extra.length!==1||extra[0][1][1]!==SPEC.policy.sha256)throw new Error('Actual whole policy role missing');
 if(JSON.stringify(after.filter(([role])=>role!=='restoration_damping_policy'))!==JSON.stringify(before))
  throw new Error('An original scientific source pair changed');
 const outputs=[];
 for(const role of ['driver','reader','launcher']){
  const record=SPEC.outputs[role],path=resolve(a['--output-directory'],record.path);
  mkdirSync(dirname(path),{recursive:true});writeFileSync(path,generated[role].bytes);
  outputs.push({...record,generated_path:path});
 }
 process.stdout.write(JSON.stringify({schema:SPEC.schema,complete:true,outputs,
  original_scientific_roles:137,current_scientific_roles:138,
  original_all137_pairs_unchanged:true,complete_source_inverse_equal:true,
  actual_field_or_policy_decision_or_speed_result:null,
  science_AST_fixture_or_ref_operations:0,
  scope:'Complete source-text construction only; not a scientific stage or admission requirement.'})+'\n');
}
main();
