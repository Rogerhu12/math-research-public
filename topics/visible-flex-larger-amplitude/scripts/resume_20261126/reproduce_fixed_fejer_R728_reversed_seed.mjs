#!/usr/bin/env node
/**
 * Complete R728 seed source reconstruction, from the complete R726 seed.
 * Text only: no numerical import, AST/compilation or scientific evaluation.
 * All source inputs/outputs remain whole files. No source guard is relaxed.
 *
 * node reproduce_fixed_fejer_R728_reversed_seed.mjs
 *   --source-directory PATH --generated-directory PATH
 */
import {readFile,writeFile,mkdir,access} from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';

const digest = bytes => createHash('sha256').update(bytes).digest('hex');
const same = (a,b) => a.length===b.length && a.equals(b);
const PARENT = {
  "name": "fixed_fejer_R726_spherical_halfwave_meridian_reference.py",
  "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R726_spherical_halfwave_meridian_reference.py",
  "bytes": 52457,
  "sha256": "176484582f7bdd83d0efe300d4ce7efe868df9d50a29310d7fb3aedce9d0f20a",
  "git_blob_sha": "231bad2fba5f80ade672703114fe5bd776512baf"
};
const OUTPUT = {
  "name": "fixed_fejer_R728_reversed_spherical_halfwave_meridian_reference.py",
  "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_R728_reversed_spherical_halfwave_meridian_reference.py",
  "bytes": 53384,
  "sha256": "c6fc04db9223981e1829620613c71de4c0bec93813ec0eeaf5f8ef7770217e86",
  "git_blob_sha": "11143579520b9509d4d95323052743031f317e6b",
  "role": "independent_R728_reversed_spherical_halfwave_seed"
};
const COMPLETE_EDITS = [
  {
    "index": 0,
    "before": "The R711 scalar amplitude, opposite R724 paired\nhalfwaves, and complete fixed-epsilon R725 three-piece C3 cutoff are retained.",
    "after": "The R711 scalar amplitude and complete fixed-epsilon R725 three-piece C3\ncutoff are retained. R728 reverses the complete paired halfwaves to (-,+).\nThe full mean equation and auxiliary amplitude law are unchanged; positions,\nangular fields, current closure calibration and normal roots are not inherited."
  },
  {
    "index": 1,
    "before": "SCHEMA = \"complete-fixed-fejer-R726-spherical-boundary-paired-halfwave-meridian-seed-reference-v1\"",
    "after": "SCHEMA = \"complete-fixed-fejer-R728-reversed-spherical-boundary-paired-halfwave-meridian-seed-reference-v1\"\nPHYSICAL_CENTRAL_POLARITY = -1"
  },
  {
    "index": 2,
    "before": "    \"\"\"Exact complete radial profile; no numerical mean or field evaluation.\"\"\"",
    "after": "    \"\"\"Exact R728 reversed profile; no numerical mean or field evaluation.\"\"\"\n    if type(PHYSICAL_CENTRAL_POLARITY) is not int or PHYSICAL_CENTRAL_POLARITY != -1:\n        raise ValueError(\"This complete source fixes the whole paired-halfwave polarity at -1\")"
  },
  {
    "index": 3,
    "before": "    return dict(schema=\"complete-equal-central-intervals-paired-halfwave-profile-v1\",",
    "after": "    return dict(schema=\"complete-equal-central-intervals-reversed-paired-halfwave-profile-v1\",\n        proof_result=\"R728\", source_fixed_global_polarity=PHYSICAL_CENTRAL_POLARITY,\n        source_parameter_depends_on_angle_mean_direction_or_outer_point=False,"
  },
  {
    "index": 4,
    "before": "        signs_in_radial_discovery_order=[1,-1],",
    "after": "        signs_in_radial_discovery_order=[PHYSICAL_CENTRAL_POLARITY,-PHYSICAL_CENTRAL_POLARITY],"
  },
  {
    "index": 5,
    "before": "            schema=\"R726-spherical-boundary-paired-halfwave-reference-working-definition-v1\",",
    "after": "            schema=\"R728-reversed-spherical-boundary-paired-halfwave-reference-working-definition-v1\",\n            source_fixed_global_central_polarity=PHYSICAL_CENTRAL_POLARITY,\n            old_positive_first_physical_field_or_working_words_inherited=False,"
  },
  {
    "index": 6,
    "before": "            exact_profile_delta=str(profile_delta),\n            exact_boundary_cutoff_epsilon=str(self.boundary_cutoff_epsilon),",
    "after": "            exact_profile_delta=str(profile_delta),\n            source_fixed_global_central_polarity=PHYSICAL_CENTRAL_POLARITY,\n            exact_boundary_cutoff_epsilon=str(self.boundary_cutoff_epsilon),"
  },
  {
    "index": 7,
    "before": "            central_profile=\"paired opposite six-piece C3 halfwaves of the full R711 h_delta; first +h_delta(t/2), second -h_delta(t/2); all exact physical breakpoints retained\",",
    "after": "            central_profile=\"R728 reversed paired six-piece C3 halfwaves of the full R711 h_delta; first -h_delta(t/2), second +h_delta(t/2); all exact physical breakpoints retained\","
  },
  {
    "index": 8,
    "before": "        sign = 1. if index == 0 else -1.",
    "after": "        sign = float(PHYSICAL_CENTRAL_POLARITY if index == 0 else -PHYSICAL_CENTRAL_POLARITY)"
  },
  {
    "index": 9,
    "before": "        record = dict(schema=\"complete-R726-spherical-boundary-paired-halfwave-seed-radial-plan-v1\",",
    "after": "        record = dict(schema=\"complete-R728-reversed-spherical-boundary-paired-halfwave-seed-radial-plan-v1\","
  }
];

function argumentsOf(argv) {
  const result={};
  for(let i=0;i<argv.length;i+=2) {
    if(!['--source-directory','--generated-directory'].includes(argv[i])
        || argv[i+1]===undefined || argv[i+1].startsWith('--')
        || Object.hasOwn(result,argv[i])) {
      throw new Error('Use each complete directory option exactly once');
    }
    result[argv[i]]=path.resolve(argv[i+1]);
  }
  if(Object.keys(result).length!==2) throw new Error('Both complete directories are required');
  return result;
}
function whole(bytes,record,label) {
  if(bytes.length!==record.bytes || digest(bytes)!==record.sha256)
    throw new Error(label+' whole byte identity differs');
}
function exactlyOnce(source,from,to,label) {
  const first=source.indexOf(from);
  if(first<0 || source.indexOf(from,first+from.length)>=0)
    throw new Error(label+' must match exactly once');
  return source.slice(0,first)+to+source.slice(first+from.length);
}
const args=argumentsOf(process.argv.slice(2));
const sourcePath=path.join(args['--source-directory'],PARENT.name);
const outputPath=path.join(args['--generated-directory'],OUTPUT.name);
if(sourcePath===outputPath) throw new Error('The full parent cannot be overwritten');
const original=await readFile(sourcePath);
whole(original,PARENT,'parent');
const originalText=original.toString('utf8');
if(!same(Buffer.from(originalText,'utf8'),original))
  throw new Error('The complete parent must be lossless UTF-8');
let current=originalText;
for(const entry of COMPLETE_EDITS)
  current=exactlyOnce(current,entry.before,entry.after,'forward '+entry.index);
const generated=Buffer.from(current,'utf8');
whole(generated,OUTPUT,'new complete source');
let inverse=current;
for(const entry of [...COMPLETE_EDITS].reverse())
  inverse=exactlyOnce(inverse,entry.after,entry.before,'reverse '+entry.index);
if(!same(Buffer.from(inverse,'utf8'),original))
  throw new Error('The complete reverse reconstruction does not recover the original bytes');
whole(await readFile(sourcePath),PARENT,'parent after construction');
await mkdir(args['--generated-directory'],{recursive:true});
try {
  await access(outputPath);
  if(!same(await readFile(outputPath),generated))
    throw new Error('Refusing to replace a different existing whole source');
} catch(error) {
  if(error.code!=='ENOENT') throw error;
}
await writeFile(outputPath,generated);
whole(await readFile(outputPath),OUTPUT,'written complete source');
console.log(JSON.stringify({
  schema:'complete-R728-reversed-halfwave-source-reconstruction-v1',
  complete:true,
  parent:{...PARENT,actual_path:sourcePath},
  output:{...OUTPUT,actual_path:outputPath},
  complete_edit_count:COMPLETE_EDITS.length,
  entire_parent_recovered_by_reverse_text_edits:true,
  all_parent_and_output_bytes_rechecked:true,
  scientific_evaluation_performed:false,
  AST_or_compilation_performed:false,
  source_ref_or_queue_updated:false
},null,2));
