// Compare the original state-only and state+variational maps at the SAME
// saved failed iterate. This is a finite diagnostic, never an accepted state.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const [topic,input,out]=process.argv.slice(2);
process.env.VISIBLE_FLEX_SOURCE_TOPIC=topic;process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
const rec=JSON.parse(gunzipSync(fs.readFileSync(input))),cp=rec.response.checkpoint,cfg=rec.config;
if(!cp?.states)throw Error('A complete saved iterate is required');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-stage-split.mjs')));
const physical=createRecalibrationFactory(cfg).assemble(),dn=createSplitFluxCompactTailDN({...cfg,tail:physical}),tail=dn.tail;
const states=cp.states.map(x=>Float64Array.from(x)),M=cfg.modes,K=2*M,r=dn.cutJets(new Float64Array(2*M)).radius,target=Float64Array.from(rec.request.height,h=>h/r**4),scales=new Float64Array(states.length);scales[0]=Math.max(1e-250,...target.map(Math.abs));for(let n=0;n<scales.length-1;n++)scales[n+1]=scales[n]/Math.abs(tail.gains[n][0]);
const j=tail.evaluate(states,target,true,scales),v=tail.evaluate(states,target,false,scales),rows=[];
for(let n=0;n<tail.cells.length;n++){
 let diff=0,rj=0,rv=0,JN=0,comp=0;
 for(let k=0;k<K;k++){
  const q=Math.abs(j.flows[n].out[k]-v.flows[n].out[k])/scales[n];if(q>diff){diff=q;comp=k;}
  rj=Math.max(rj,Math.abs(j.residuals[n][k])/scales[n]);rv=Math.max(rv,Math.abs(v.residuals[n][k])/scales[n]);
  let norm=0;for(let m=0;m<K;m++)norm+=Math.abs(j.flows[n].J[k*K+m]);JN=Math.max(JN,norm);
 }
 const c=tail.cells[n];rows.push({stage:n,cell:c.rawCell,segment:c.rawSegment,normalized_map_difference:diff,component:comp,normalized_variational_residual:rj,normalized_state_only_residual:rv,jacobian_infinity_norm:JN});
}
const largest=key=>rows.reduce((a,b)=>a[key]>=b[key]?a:b);
const data={scope:'Finite consistency of the exact split-flux worker maps at the saved failed iterate; no nonlinear acceptance or geometric conclusion.',rhsEvaluation:tail.parameters.rhsEvaluation,input,input_sha256:createHash('sha256').update(fs.readFileSync(input)).digest('hex'),modes:M,quadrature:cfg.quadrature,steps:cfg.steps,shootingParts:cfg.shootingParts,normalized_variational_residual:j.norm,normalized_state_only_residual:v.norm,max_map_difference:largest('normalized_map_difference'),worst_variational_residual:largest('normalized_variational_residual'),worst_state_only_residual:largest('normalized_state_only_residual'),largest_stage_jacobian:largest('jacobian_infinity_norm')};fs.writeFileSync(out,JSON.stringify(data,null,2)+'\n');console.log(JSON.stringify(data));
