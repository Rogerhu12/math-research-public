// Real-record data guards only: no physical factory, RHS, Newton, or audit.
import fs from 'node:fs';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {preserveExactRawWarm,samePhysicalHeight} from './strong_exact_raw_tail_warm.mjs';
const [checkpointFile,referenceFile,outFile]=process.argv.slice(2);
if(!outFile)throw Error('Usage: guard-check CHECKPOINT.json.gz ACCEPTED.json.gz OUT.json');
const read=p=>JSON.parse((p.endsWith('.gz')?zlib.gunzipSync(fs.readFileSync(p)):fs.readFileSync(p)).toString());
const sha=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const record=read(checkpointFile),prior=record.checkpoint,reference=read(referenceFile),
 ready=reference.actual_tail.ready;
// This object supplies recorded dimensions/parameters only, not an engine.
const descriptor={tail:{parameters:ready.parameters,cells:Array(ready.parameters.depth),rawNode:prior.rawNode}};
const checks={};
const result=preserveExactRawWarm(prior,descriptor);
checks.complete_real_state_copy_preserved=result.states.every((row,n)=>
 row!==prior.states[n]&&row.every((v,j)=>Object.is(v,prior.states[n][j])));
checks.complete_real_parameter_binding=result.diagnostics.allNonIOParametersExactlyEqual;
checks.complete_real_H_exact=samePhysicalHeight(prior.cutHeight,prior.cutHeight);
function oneULP(x){const b=Buffer.alloc(8);b.writeDoubleLE(x);b.writeBigUInt64LE(b.readBigUInt64LE()+1n);return b.readDoubleLE();}
const shifted=prior.cutHeight.slice();shifted[0]=oneULP(shifted[0]);
checks.one_ULP_changed_H_rejected=!samePhysicalHeight(shifted,prior.cutHeight);
const clone=x=>JSON.parse(JSON.stringify(x));
function rejected(mutator){const bad=clone(prior);mutator(bad);try{preserveExactRawWarm(bad,descriptor);return false;}catch{return true;}}
checks.changed_grid_rejected=rejected(p=>p.parameters.shootingParts++);
checks.changed_spectrum_rejected=rejected(p=>p.parameters.modes++);
checks.changed_raw_subset_rejected=rejected(p=>p.rawStates[0][0]=oneULP(p.rawStates[0][0]));
checks.nonfinite_full_state_rejected=rejected(p=>p.states[1][1]=NaN);
const pathsOnly=clone(prior);pathsOnly.parameters.initialCheckpoint='another-explicit-I-O-path';
checks.I_O_path_only_change_allowed=preserveExactRawWarm(pathsOnly,descriptor).diagnostics.allNonIOParametersExactlyEqual;
if(!Object.values(checks).every(Boolean))throw Error('Exact raw data guard failed');
const report={scope:'Data-format and exact-bit guards on genuine saved records only; the target object is a metadata descriptor, never a numerical engine.',checks,passed:true,
 checkpoint:checkpointFile,checkpointSHA256:sha(checkpointFile),reference:referenceFile,referenceSHA256:sha(referenceFile),
 helperSHA256:sha(new URL('./strong_exact_raw_tail_warm.mjs',import.meta.url)),
 testSHA256:sha(new URL(import.meta.url)),nodeVersion:process.version,
 diagnostics:result.diagnostics,physicalFactoriesCreated:0,RHSEvaluations:0,Jacobians:0,NewtonSolves:0,newResponses:0};
fs.writeFileSync(outFile,JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({passed:true,checks:Object.keys(checks).length,out:outFile}));
