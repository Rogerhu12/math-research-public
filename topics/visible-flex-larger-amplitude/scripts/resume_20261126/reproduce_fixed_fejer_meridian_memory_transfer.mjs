#!/usr/bin/env node
/** Complete source-only transfer derivation. No scientific import or evaluation. */
import fs from 'node:fs';
import crypto from 'node:crypto';
const CONFIG={"input":{"name":"transfer_fixed_fejer_stage_point_memory.py","bytes":78863,"sha256":"afa2d6397c331b5bf55dd461bbf52a35839ff610d3db0f12a043e8eceef3b6ed","git_blob_sha":"7f1f3971893d8895d7e1b8cc3612e563a44d3095","path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/transfer_fixed_fejer_stage_point_memory.py"},"output":{"name":"fixed_fejer_meridian_memory_transfer.py","path":"topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_memory_transfer.py","bytes":78920,"sha256":"ae9e5b316e785bf85a223cb210ca812551bf615f0f56b8861f817877b9208021","git_blob_sha":"732698d4f1ba5d4a312ff95701c30b462473dce9"},"patches":[{"old":"complete-fixed-fejer-stage-point-history-and-same-source-continuation-v1","new":"complete-fixed-fejer-meridian-values-history-and-same-source-continuation-v1","count":1},{"old":"9171871fcaaa1d2e65de1c40071cf8bb1acac0d7b0cc1d1da5b9cb36f690076f","new":"15cd8e201db8aeef7139baf0e82d9d18fcf190194cd33dc8b112bebe05a7dffc","count":1},{"old":"fixed_fejer_stage_point_source_binding.py","new":"fixed_fejer_meridian_source_binding.py","count":1},{"old":"only_stage_point_guard_and_recursive_source_policy_changed=True","new":"only_plain_detached_meridian_values_and_recursive_source_policy_changed=True","count":1},{"old":"changed_model_fields='same predeclared Fejer target and full layout; new stage immutable-owner guard and its exact recursive source policies only'","new":"changed_model_fields='same predeclared Fejer target, full layout and all stage equations; optional plain-detached meridian integration values and their exact recursive source policies only'","count":1}]};
const sha=s=>crypto.createHash('sha256').update(s).digest('hex');
const argv=process.argv.slice(2);
if(argv.length!==4||argv[0]!=='--parent-source'||argv[2]!=='--output-source')
  throw Error('Use --parent-source COMPLETE_ORIGINAL.py --output-source COMPLETE_NEW.py');
const raw=fs.readFileSync(argv[1]);
if(raw.length!==CONFIG.input.bytes||sha(raw)!==CONFIG.input.sha256)
  throw Error('The entire actual original transfer source differs');
const original=raw.toString('utf8');
let derived=original;
for(const p of CONFIG.patches){
  if(derived.split(p.old).length-1!==p.count)throw Error('Exact replacement multiplicity differs');
  derived=derived.replace(p.old,p.new);
}
if(Buffer.byteLength(derived)!==CONFIG.output.bytes||sha(derived)!==CONFIG.output.sha256)
  throw Error('The complete independently derived transfer differs');
let back=derived;
for(const p of [...CONFIG.patches].reverse()){
  if(back.split(p.new).length-1!==p.count)throw Error('Exact inverse multiplicity differs');
  back=back.replace(p.new,p.old);
}
if(back!==original)throw Error('The whole unchanged original body did not reverse exactly');
fs.writeFileSync(argv[3],derived,'utf8');
process.stdout.write(JSON.stringify({schema:'complete-meridian-memory-transfer-source-reproduction-v1',
  input:CONFIG.input,output:CONFIG.output,exact_single_replacements:CONFIG.patches.length,
  entire_parent_reverse_equal:true,scientific_evaluations:0,AST_or_compile_executed:false},null,2)+'\n');
