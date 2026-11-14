// Readonly original residual/Newton-direction probe; no trial is accepted.
import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {gzipSync,gunzipSync} from 'node:zlib';
import {parseArgs} from 'node:util';
import {pathToFileURL,fileURLToPath} from 'node:url';
const {values:v}=parseArgs({options:{'source-root':{type:'string'},config:{type:'string'},
 checkpoint:{type:'string'},out:{type:'string'},direction:{type:'string'},lambdas:{type:'string'}}});
for(const k of ['source-root','config','checkpoint','out'])if(!v[k])throw Error('Missing '+k);
if(fs.existsSync(v.out))throw Error('Output exists');
const here=path.dirname(fileURLToPath(import.meta.url));
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.resolve(v['source-root']);
const source=name=>pathToFileURL(path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts',name));
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(here,'closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(here,'db6f-prefix-tail-direction-split.mjs')));
const {createFastSplitFluxMomentumTailEngine}=await import(source('f6tail_fast_split_flux_engine.mjs'));
const {remeshCheckpoint}=await import(pathToFileURL(path.join(here,'950f-tail-warm-remesh.mjs')));
const read=p=>JSON.parse((p.endsWith('.gz')?gunzipSync(fs.readFileSync(p)):fs.readFileSync(p)).toString());
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const cfg=read(v.config),record=read(v.checkpoint),cp=record.response?.checkpoint??record.checkpoint??record;
const physical=createRecalibrationFactory(cfg).assemble(),dn=createSplitFluxCompactTailDN({...cfg,tail:physical}),tail=dn.tail;
const M=cfg.modes,K=2*M,zero=dn.cutJets(new Float64Array(K)),r4=zero.radius**4;
let states=remeshCheckpoint(cp,dn,createFastSplitFluxMomentumTailEngine);
// Exactly the same boundary-corrected warm initialization as the worker,
// at identical cutHeight (ratio=1, so the harmonic predictor is immaterial).
states=states.map(row=>Float64Array.from(row));
const target=Float64Array.from(cp.cutHeight,x=>x/r4);
if(cfg.correctInitialBoundary!==false){
 const delta=Float64Array.from(target,(x,j)=>x-states[0][j]),add=tail.initial(delta);
 states=states.map((row,n)=>Float64Array.from(row,(x,j)=>x+add[n][j]));
}
const scales=tail.scaleFor(target),depth=tail.cells.length;
const summary={scope:'Readonly actual finite residual and Newton direction; no trial acceptance, no coupled solution claim.',
 scriptSHA256:sha(fileURLToPath(import.meta.url)),config:v.config,configSHA256:sha(v.config),
 checkpoint:v.checkpoint,checkpointSHA256:sha(v.checkpoint),sourceMapSHA256:sha(path.join(here,'../notes/2026-11-09-db6f-prefix-tail-direction-source-map.json')),
 parameters:tail.parameters,stages:depth,rows:[]};
function save(){const bytes=Buffer.from(JSON.stringify(summary,null,2)+'\n');if(bytes.length>=5_000_000)throw Error('Report too large');fs.writeFileSync(v.out,bytes);}
function details(ev){
 const stageNorm=ev.residuals.map((r,n)=>Math.max(...Array.from(r,x=>Math.abs(x)/scales[n])));
 const order=stageNorm.map((norm,n)=>({stage:n,norm,rawCell:tail.cells[n].rawCell,rawSegment:tail.cells[n].rawSegment})).sort((a,b)=>b.norm-a.norm);
 return {norm:ev.norm,stageNorm,worst:order.slice(0,5),endNorm:Math.max(...Array.from(ev.end,x=>Math.abs(x)/scales[depth]))};
}
let direction;
if(v.direction){
 const old=read(v.direction);if(old.checkpointSHA256!==summary.checkpointSHA256||old.configSHA256!==summary.configSHA256)throw Error('Direction input mismatch');
 direction=old.delta.map(row=>Float64Array.from(row));summary.direction=v.direction;summary.directionSHA256=sha(v.direction);
}else{
 const plain=tail.evaluate(states,target,false,scales);summary.stateOnly=details(plain);save();
 console.log(JSON.stringify({event:'stateOnly',norm:plain.norm,worst:summary.stateOnly.worst[0]}));
 const variational=tail.evaluate(states,target,true,scales);summary.variational=details(variational);
 summary.stageResidualDifference=plain.residuals.map((r,n)=>Math.max(...Array.from(r,(x,j)=>Math.abs(x-variational.residuals[n][j])/scales[n])));
 summary.maximumNormalizedResidualDifference=Math.max(...summary.stageResidualDifference);
 const cor=tail.correction(variational,states,target);direction=cor.delta;summary.chartCondition=cor.maxChartCondition;
 let linear=0;const linearByStage=[];
 for(let n=0;n<depth;n++){
  const r=variational.residuals[n],J=variational.flows[n].J;let local=0;
  for(let i=0;i<K;i++){
   let value=r[i]-direction[n][i];for(let j=0;j<K;j++)value+=J[i*K+j]*direction[n+1][j];
   local=Math.max(local,Math.abs(value)/scales[n]);
  }
  linearByStage.push(local);linear=Math.max(linear,local);
 }
 for(let j=0;j<M;j++){
  linear=Math.max(linear,Math.abs(variational.end[j]+direction[depth][M+j]-tail.graphs[depth][j]*direction[depth][j])/scales[depth]);
  linear=Math.max(linear,Math.abs(states[0][j]-target[j]+direction[0][j])/scales[0]);
 }
 summary.linearizedResidualMaximum=linear;summary.linearizedResidualByStage=linearByStage;
 const outputDirection=v.out.replace(/\.json$/, '')+'-direction.json.gz';if(fs.existsSync(outputDirection))throw Error('Direction output exists');
 const bytes=gzipSync(JSON.stringify({scope:'UNSOLVED original Newton direction only; no accepted trial.',checkpointSHA256:summary.checkpointSHA256,configSHA256:summary.configSHA256,delta:direction.map(x=>Array.from(x))})+'\n');
 if(bytes.length>=5_000_000)throw Error('Direction too large');fs.writeFileSync(outputDirection,bytes,{flag:'wx'});
 summary.direction=outputDirection;summary.directionSHA256=sha(outputDirection);save();
 console.log(JSON.stringify({event:'baseComparison',stateOnly:plain.norm,variational:variational.norm,maximumNormalizedResidualDifference:summary.maximumNormalizedResidualDifference,linearizedResidualMaximum:linear,chartCondition:cor.maxChartCondition}));
}
for(const lambda of (v.lambdas??'').split(',').filter(Boolean).map(Number)){
 const trial=states.map((row,n)=>Float64Array.from(row,(x,j)=>x+lambda*direction[n][j]));
 try{const ev=tail.evaluate(trial,target,false,scales),d=details(ev);summary.rows.push({lambda,...d});console.log(JSON.stringify({event:'trial',lambda,norm:ev.norm,worst:d.worst[0]}));}
 catch(e){const row={lambda,error:String(e),stage:e.tailStage,rawCell:e.tailRawCell,rawSegment:e.tailRawSegment};summary.rows.push(row);console.log(JSON.stringify(row));}
 save();
}
save();
