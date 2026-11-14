// Complete original evaluate miss/hit comparison; this is not a DN solve.
// The same warmed full state, target, scaling and every original output field
// are compared. No residual or final acceptance gate is replaced by this check.
import crypto from 'node:crypto';

const hash=bytes=>crypto.createHash('sha256').update(bytes).digest('hex');
function numberBytes(value){const b=Buffer.allocUnsafe(8);b.writeDoubleLE(value);return b;}
function vectorBytes(value){
 const b=Buffer.allocUnsafe(value.length*8);
 for(let j=0;j<value.length;j++)b.writeDoubleLE(value[j],8*j);
 return b;
}
function recordBytes(value,hasher,counter){
 if(typeof value==='number'){
  hasher.update('number:');hasher.update(numberBytes(value));counter.numbers++;return;
 }
 if(value instanceof Float64Array){
  hasher.update('Float64Array:'+value.length+':');hasher.update(vectorBytes(value));
  counter.numbers+=value.length;return;
 }
 if(Array.isArray(value)){
  hasher.update('Array:'+value.length+':');for(const item of value)recordBytes(item,hasher,counter);return;
 }
 if(value&&Object.getPrototypeOf(value)===Object.prototype){
  const keys=Object.keys(value).sort();hasher.update('Object:'+JSON.stringify(keys)+':');
  for(const key of keys)recordBytes(value[key],hasher,counter);return;
 }
 throw Error('Unrecorded evaluate output type: '+String(value));
}
function fingerprint(value){
 const hasher=crypto.createHash('sha256'),counter={numbers:0};recordBytes(value,hasher,counter);
 return {sha256:hasher.digest('hex'),numberCount:counter.numbers};
}
function equalBits(a,b,where='root'){
 if(typeof a==='number'||typeof b==='number'){
  if(typeof a!=='number'||typeof b!=='number'||!numberBytes(a).equals(numberBytes(b)))
   throw Error('Scalar bit mismatch at '+where);return;
 }
 if(a instanceof Float64Array||b instanceof Float64Array){
  if(!(a instanceof Float64Array)||!(b instanceof Float64Array)||a.length!==b.length||
    !vectorBytes(a).equals(vectorBytes(b)))throw Error('Array bit mismatch at '+where);return;
 }
 if(Array.isArray(a)||Array.isArray(b)){
  if(!Array.isArray(a)||!Array.isArray(b)||a.length!==b.length)throw Error('Array shape mismatch at '+where);
  for(let j=0;j<a.length;j++)equalBits(a[j],b[j],where+'['+j+']');return;
 }
 const ak=Object.keys(a).sort(),bk=Object.keys(b).sort();
 if(JSON.stringify(ak)!==JSON.stringify(bk))throw Error('Output key mismatch at '+where);
 for(const key of ak)equalBits(a[key],b[key],where+'.'+key);
}

export function compareCompleteStageEvaluation(dn,states,height,event=()=>{}){
 const shooting=dn.tail,{modes:M,depth}=shooting.parameters,K=2*M;
 if(!shooting.exactStagePersistence||!shooting.exactStageDiagnostic)
  throw Error('The explicit original complete-stage cache is not installed');
 if(!states||states.length!==depth+1||states.some(row=>row.length!==K)||height.length!==M)
  throw Error('Full actual warmed shooting dimensions differ');
 const zero=dn.cutJets(new Float64Array(K)),r4=zero.radius**4;
 const target=Float64Array.from(height,v=>v/r4),scales=new Float64Array(depth+1);
 scales[0]=Math.max(1e-250,...Array.from(target,Math.abs));
 for(let j=0;j<depth;j++)scales[j+1]=scales[j]/Math.abs(shooting.gains[j][0]);
 const originalStates=states.map(row=>Float64Array.from(row));
 const stateBefore=fingerprint(originalStates),statisticsBefore={...shooting.exactStagePersistence.stats};
 const stages=[0,depth-1],samples=[];
 for(const stage of stages){
  const input=originalStates[stage+1];
  const uncached=shooting.exactStageDiagnostic.uncachedCellFlow(stage,input,true);
  const stored=shooting.exactStageDiagnostic.cellFlow(stage,input,true);
  equalBits(uncached,stored,'stage'+stage);
  const row={stage,allFiveFieldsBitwiseEqual:true,uncached:fingerprint(uncached),stored:fingerprint(stored)};
  samples.push(row);event({event:'actual_stage_uncached_vs_stored_passed',...row});
 }
 event({event:'actual_complete_stage_evaluate_begin',depth,modes:M,
  stats:{...shooting.exactStagePersistence.stats}});
 const first=shooting.evaluate(originalStates,target,true,scales);
 const firstHash=fingerprint(first),afterFirst={...shooting.exactStagePersistence.stats};
 event({event:'actual_complete_stage_first_evaluate_finished',...firstHash,
  norm:first.norm,minA:first.minA,minD:first.minD,stats:afterFirst});
 const second=shooting.evaluate(originalStates,target,true,scales);
 equalBits(first,second,'complete-original-evaluate');
 const secondHash=fingerprint(second),afterSecond={...shooting.exactStagePersistence.stats};
 if(secondHash.sha256!==firstHash.sha256||afterSecond.hits-afterFirst.hits!==depth||
   afterSecond.misses!==afterFirst.misses)throw Error('Complete repeat was not all exact stage hits');
 const stateAfter=fingerprint(originalStates);
 if(stateBefore.sha256!==stateAfter.sha256)throw Error('Original evaluate mutated the supplied full state');
 const result={scope:'Actual complete original variational evaluate equivalence, including full residuals and all local Jacobians. Diagnostic only; no Newton, DN convergence or geometric audit acceptance.',
  passed:true,nonlinearSolution:false,nonlinearSolves:0,finalAudits:0,modes:M,depth,
  stagesCompared:depth,componentFields:['flows.out','flows.J','flows.meanHeight','flows.minA','flows.minD',
   'residuals','end','norm','minA','minD'],
  literalEveryOutputFloat64ByteCompared:true,first:firstHash,second:secondHash,
  statisticsBefore,afterFirst,afterSecond,samples,completeStateUnchanged:true,
  stateFloat64TreeSHA256:stateBefore.sha256,targetFloat64LESHA256:hash(vectorBytes(target)),
  scalesFloat64LESHA256:hash(vectorBytes(scales)),cacheIdentitySHA:shooting.exactStagePersistence.identitySHA,
  cacheRoot:shooting.exactStagePersistence.root,initialResidual:first.norm,
  originalFullSolveAndAuditStillRequired:true};
 event({event:'actual_complete_stage_evaluate_check_passed',...result});
 return result;
}
