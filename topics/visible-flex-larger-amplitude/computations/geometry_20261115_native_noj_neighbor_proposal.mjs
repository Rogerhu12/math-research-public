// Request103: bounded real-noJ neighbors; no independent native acceptance.
import crypto from 'node:crypto';
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const raw=v=>Buffer.from(v.buffer,v.byteOffset,v.byteLength);
const rowsHash=rows=>{const h=crypto.createHash('sha256');for(const r of rows)h.update(raw(r));return h.digest('hex');};
function number(value){
 if(typeof value!=='number')return {available:false,javascript_type:typeof value};
 const b=Buffer.alloc(8);b.writeDoubleLE(value);
 return {value:Number.isFinite(value)?value:null,float64le_hex:b.toString('hex'),
  classification:Number.isNaN(value)?'NaN':value===Infinity?'positive-infinity':value===-Infinity?'negative-infinity':Object.is(value,-0)?'negative-zero':'finite'};
}
function failure(error){
 const text=String(error);return {name:error?.name??'Error',message:text.slice(0,1200),
  complete_message_sha256:hash(Buffer.from(text)),printed_message_truncated:text.length>1200};
}
function point(ev,states,target,scales){
 if(ev.flows.length!==576||ev.residuals.length!==576||ev.end.length!==112)
  throw Error('The original full noJ evaluate must return all576 stages and far112.');
 const cut=Float64Array.from(target,(_v,j)=>states[0][j]-target[j]);
 const outputs=ev.flows.map(f=>f.out),all=[cut,...ev.residuals,ev.end];
 if(outputs.some(x=>!(x instanceof Float64Array)||x.length!==224)||
    ev.residuals.some(x=>!(x instanceof Float64Array)||x.length!==224))
  throw Error('The original full224-word stage arrays are required.');
 let maximum=-Infinity,worst=null,nonfinite=0;
 function visit(kind,node,row,value,sigma,globalRow){
  if(!Number.isFinite(value))nonfinite++;
  const scaled=Math.abs(value)/sigma;
  if(scaled>maximum){maximum=scaled;worst={kind,node,row,global_equation_row:globalRow,
   residual:number(value),sigma:number(sigma),scaled_absolute:number(scaled)};}
 }
 // This readout follows the original stage/far/cut visitation order.
 // Its value never replaces ev.norm or becomes a native acceptance test.
 for(let n=0;n<576;n++)for(let j=0;j<224;j++)visit('stage',n,j,ev.residuals[n][j],scales[n],112+n*224+j);
 for(let j=0;j<112;j++)visit('far',576,j,ev.end[j],scales[576],112+576*224+j);
 for(let j=0;j<112;j++)visit('cut',0,j,cut[j],scales[0],j);
 return {original_norm:number(ev.norm),original_minA:number(ev.minA),original_minD:number(ev.minD),
  input_state_sha256:rowsHash(states),stage_out_sha256:rowsHash(outputs),
  stage_residual_sha256:rowsHash(ev.residuals),cut_residual_sha256:hash(raw(cut)),
  far_residual_sha256:hash(raw(ev.end)),all129248_residual_sha256:rowsHash(all),
  row_hash_order:'cut112,stage576x224,far112',full_equation_rows:129248,
  nonfinite_residual_words:nonfinite,maximum_row_readout:worst,
  maximum_row_matches_original_norm:Object.is(maximum,ev.norm),
  stage10:{input_sha256:hash(raw(states[11])),output_sha256:hash(raw(outputs[10])),
   residual_sha256:hash(raw(ev.residuals[10])),mean_height:number(ev.flows[10].meanHeight)},
  stage11:{input_sha256:hash(raw(states[12])),output_sha256:hash(raw(outputs[11])),
   residual_sha256:hash(raw(ev.residuals[11]))}};
}
export function proposeNeighbors(args,meta,emit){
 if(process.env.GITHUB_ACTIONS!=='true'||(process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
  throw Error('Scientific execution belongs only to this public repository Actions.');
 const {ev,states,target,scales,it,M,K,depth,evaluate,cellFlow}=args;
 if(it!==0||M!==112||K!==224||depth!==576||states.length!==577||
    typeof evaluate!=='function'||typeof cellFlow!=='function')
  throw Error('Use the original full first-correction function references and dimensions.');
 const evaluateSHA=hash(Buffer.from(evaluate.toString()));
 if(evaluateSHA!=='9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9')
  throw Error('The original full evaluate source changed.');
 const initialHash=rowsHash(states),targetHash=hash(raw(target)),scalesHash=hash(raw(scales));
 const baseBytes=Buffer.from(raw(states[11]).subarray(75*8,76*8));
 if(baseBytes.toString('hex')!=='6e1cafdb47e9c93c')
  throw Error('The first proposal must use the actual failed73 base Q76 word.');
 const word=baseBytes.readBigUInt64LE(),baseValue=states[11][75];
 const report={schema:'actual-noJ-bounded-neighbor-proposal-v1',...meta,
  initial_state_sha256:initialHash,target_sha256:targetHash,scales_sha256:scalesHash,
  evaluate_source_sha256:evaluateSHA,cellFlow_source_sha256:hash(Buffer.from(cellFlow.toString())),
  coordinate:{node:11,column:75,component:'Q',mode:76,base:number(baseValue)},
  original_current_withJ_norm:number(ev.norm),planned_noJ_full_evaluations_maximum:3,
  original_noJ_full_calls_started:0,original_noJ_full_calls_completed:0,
  independent_J_or_QR_calls:0,complete_original_evaluate_used_for_each_point:true,
  local_residual_reassembly_not_used:true,selection_requires_strict_decrease_from_both_current_withJ_and_actual_noJ_base:true,
  points:[],selected_for_original_trials:false,selected_label:null,
  original_native_acceptance_not_performed:true,original_total32_and_ten_trial_body_unchanged:true,
  finite_neighbors_not_a_convergence_claim:true,native_accepted:false};
 let best=null,bestNorm=ev.norm,baseNorm=null;
 for(const [label,shift] of [['base',0n],['minus-one-ulp',-1n],['plus-one-ulp',1n]]){
  const trial=states.map(row=>Float64Array.from(row));
  const bytes=Buffer.alloc(8);bytes.writeBigUInt64LE(word+shift);
  const desired=bytes.readDoubleLE();trial[11][75]=desired;
  const inputHash=rowsHash(trial),entry={label,word:number(desired),input_state_sha256:inputHash,
   original_noJ_call_started:false,original_noJ_call_completed:false,strictly_below_original_current_norm:false};
  report.points.push(entry);
  try{
   entry.original_noJ_call_started=true;report.original_noJ_full_calls_started++;
   const actual=evaluate(trial,target,false,scales);
   entry.original_noJ_call_completed=true;report.original_noJ_full_calls_completed++;
   if(rowsHash(trial)!==inputHash)throw Error('Original evaluate unexpectedly mutated proposal input states.');
   entry.actual=point(actual,trial,target,scales);
   entry.strictly_below_original_current_norm=Number.isFinite(actual.norm)&&actual.norm<ev.norm;
   if(shift===0n&&Number.isFinite(actual.norm)){
    baseNorm=actual.norm;bestNorm=Math.min(ev.norm,actual.norm);
    report.actual_noJ_base_norm=entry.actual.original_norm;
   }
   entry.strictly_below_actual_noJ_base=baseNorm!==null&&Number.isFinite(actual.norm)&&actual.norm<baseNorm;
   if(shift!==0n&&baseNorm!==null&&Number.isFinite(actual.norm)&&actual.norm<bestNorm){
    bestNorm=actual.norm;best={label,value:desired,states:trial,stateHash:inputHash,entry};
   }
  }catch(error){entry.original_error=failure(error);}
  emit({event:'native103_actual_noJ_proposal_point',...meta,point:entry,
   native_accepted:false,only_direction_proposal:true});
 }
 if(rowsHash(states)!==initialHash||hash(raw(target))!==targetHash||hash(raw(scales))!==scalesHash)
  throw Error('The proposal changed the actual native state, target or scales.');
 let delta=null,negativeZeros=0;
 if(best!==null){
  delta=states.map(row=>Float64Array.from(row,v=>Object.is(v,-0)?-0:0));
  delta[11][75]=best.value-baseValue;
  const unit=states.map((row,n)=>Float64Array.from(row,(v,j)=>v+delta[n][j]));
  if(rowsHash(unit)!==best.stateHash)throw Error('The original unit-step expression does not reproduce the selected neighbor.');
  for(const row of delta)for(const value of row)if(Object.is(value,-0))negativeZeros++;
  report.selected_for_original_trials=true;report.selected_label=best.label;
  report.selected_original_norm=best.entry.actual.original_norm;
  report.delta_sha256=rowsHash(delta);report.delta_shape=[577,224];
  report.proposed_original_unit_state_sha256=best.stateHash;
  report.restored_negative_zero_count=negativeZeros;
  report.original_ten_noJ_trials_still_required=true;
 }else report.fallback='same-fresh-withJ-complete-R273-QR';
 emit({event:'native103_actual_noJ_proposal_finished',...meta,report});
 return {selected:best!==null,delta,report,negative_zero_count:negativeZeros};
}
