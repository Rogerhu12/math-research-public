// Own wrapper for the frozen physically optimized tail; no metric change on reload.
// Actual custom cut-preserving geometry; recording protocol copied from reviewed split-flux worker.
// Explicit split-flux variant of the reviewed recording worker.
// The complete optional factory has its own algebra and call-path review.
// Optional recording worker. Only checkpoint retention changes relative to
// f6curve_compact_tail_port.mjs SHA256 81834ad36f6cc9767cc4cef850ad0fb6762b8206f54f5f81cff25b76a37fa233.
// Actual compact nonlinear finite-depth physical-height DN for the curve BVP.
// Astra curve_transition, AI-assisted 2026-11-08. No infinite-tail assertion.
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {createRecalibrationFactory} from './closing_recalibrated_tail.mjs';
const sourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
if(!sourceRoot)throw Error('VISIBLE_FLEX_SOURCE_ROOT is required');
const {createSplitFluxCompactTailDN:createCompactTailDN}=await import(pathToFileURL(path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_compact_dn_split_flux.mjs')));
import fs from 'node:fs';
import zlib from 'node:zlib';
import readline from 'node:readline';
const cfg=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
function trace(row){if(cfg.traceFile)fs.appendFileSync(cfg.traceFile,JSON.stringify({time:new Date().toISOString(),...row})+'\n');}
const dn=createCompactTailDN({...cfg,tail:createRecalibrationFactory(cfg).assemble()}),M=cfg.modes,zero=dn.cutJets(new Float64Array(2*M));
// The cut restoration can create extra zeros of the actual logarithmic slope.
// Add those zeros to the inherited raw-source cusp grid without changing the
// physical profile. This affects integration only, not any metric parameter.
if(cfg.actualCuspGrid===true)for(const cell of dn.tail.cells)for(const profile of cell.profiles){
 const roots=[...(profile.integrationBreakpoints??[])];let a=0,fa=profile(0).dlogwdx;
 for(let k=1;k<=128;k++){
  const b=k/128,fb=profile(b).dlogwdx;
  if(fa*fb<0){let lo=a,hi=b,flo=fa;for(let n=0;n<48;n++){
   const mid=(lo+hi)/2,fm=profile(mid).dlogwdx;
   if(flo*fm<=0)hi=mid;else{lo=mid;flo=fm;}}
   roots.push((lo+hi)/2);}
  a=b;fa=fb;
 }
 profile.integrationBreakpoints=[...new Set(roots)].sort((a,b)=>a-b);
}
let last=null,call=0;
if(cfg.initialCheckpoint){
 const raw=fs.readFileSync(cfg.initialCheckpoint),record=JSON.parse((cfg.initialCheckpoint.endsWith('.gz')?zlib.gunzipSync(raw):raw).toString());
 const prior=record.seam?.tail_checkpoint??record.checkpoint??record;
 if(!prior?.parameters||!prior?.states||!prior?.cutHeight)throw new Error('Initial checkpoint has no complete finite-tail state');
 const old=prior.parameters,now=dn.tail.parameters;
 for(const key of ['pulseCaps','valleyCaps','flatOuterThroughCell','flatOuterStartSegment','flatSlope','capMode','rCut','wCut','width','curvatureBound','slopeCap','capTransition','calibrationSteps','warpSteps','quadratureTolerance','cuspAwareQuadrature','orientation','prefixR','prefixEnd','prefixReturnStart','protectCell','valleyControls','delta0','R','a','etaPower','etaRatioAtN0','rejoinR20At','rejoinIndexOffset','spacing','depth']){
  if(JSON.stringify(old[key]??null)!==JSON.stringify(now[key]??null))throw new Error('Warm tail geometry mismatch: '+key);
 }
 if(prior.states.length!==cfg.depth+1)throw new Error('Warm tail depth mismatch');
 const oldM=old.modes,keep=Math.min(oldM,M);
 const states=prior.states.map(row=>{
  if(row.length!==2*oldM)throw new Error('Warm tail state dimension mismatch');
  const v=Array(2*M).fill(0);for(let j=0;j<keep;j++){v[j]=row[j];v[M+j]=row[oldM+j];}return v;
 });
 const height=Array(M).fill(0);for(let j=0;j<keep;j++)height[j]=prior.cutHeight[j];
 last={states,jets:{height}};trace({event:'warm_initial_state',source:cfg.initialCheckpoint,sourceModes:oldM,targetModes:M,depth:cfg.depth});
}
const D=[];
for(let j=0;j<M;j++){
 const node=new Float64Array(2*M),q=1e-18;node[j]=q;node[M+j]=q*dn.tail.graphs[0][j];
 const jets=dn.cutJets(node);D.push(jets.slope[j]/jets.height[j]);
}
console.log(JSON.stringify({event:'ready',parameters:dn.tail.parameters,cut:zero,linearSlope:D}));
for await(const line of readline.createInterface({input:process.stdin,terminal:false})){
 try{
  const req=JSON.parse(line);if(req.stop)break;
  call++;const start=Date.now();trace({event:'request',call,height:req.height,jacobian:!!req.jacobian,audit:!!req.audit});
  let initial;
  if(last){
   const prev=last.jets.height[0],ratio=req.height[0]/prev;
   if(Number.isFinite(ratio)&&ratio>.25&&ratio<4)initial=last.states.map(row=>row.map(v=>v*ratio));
  }
  const sol=dn.solve(req.height,{maxIterations:18,tolerance:cfg.solveTolerance??2e-10,initial,jacobian:!!req.jacobian,audit:!!req.audit,auditSteps:cfg.auditSteps??cfg.steps,progress:row=>trace({event:'iteration',call,elapsed_ms:Date.now()-start,...row})});
  if(sol.converged)last=sol;
  trace({event:'response',call,elapsed_ms:Date.now()-start,converged:sol.converged,residual:sol.normalizedResidual,maxChartCondition:Math.max(...sol.history.map(x=>x.chartCondition??0))});
  // Every actual response retains the shooting state. Audit execution itself
  // is still controlled by req.audit and has not been weakened or bypassed.
  const checkpoint={parameters:sol.parameters,states:sol.states,cutHeight:req.height,scope:'Finite Fourier/depth shooting state; the far Robin condition is not an exact rotational collar. Retained for every actual response; an unaudited response is not a final geometric audit.'};
  console.log(JSON.stringify({converged:sol.converged,residual:sol.normalizedResidual,jets:sol.jets,heightJetJacobian:sol.heightJetJacobian??null,history:sol.history,audit:sol.audit??null,checkpoint}));
 }catch(e){trace({event:'failure',call,error:String(e)});console.log(JSON.stringify({failed:String(e)}));}
}
process.stdin.destroy();
