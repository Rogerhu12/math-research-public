// Actual compact nonlinear finite-depth physical-height DN for the curve BVP.
// Astra curve_transition, AI-assisted 2026-11-08. No infinite-tail assertion.
import {createCompactTailDN} from './f6tail_compact_dn.mjs';
import fs from 'node:fs';
import zlib from 'node:zlib';
import readline from 'node:readline';
const cfg=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
function trace(row){if(cfg.traceFile)fs.appendFileSync(cfg.traceFile,JSON.stringify({time:new Date().toISOString(),...row})+'\n');}
const dn=createCompactTailDN(cfg),M=cfg.modes,zero=dn.cutJets(new Float64Array(2*M));
let last=null,call=0;
if(cfg.initialCheckpoint){
 const raw=fs.readFileSync(cfg.initialCheckpoint),record=JSON.parse((cfg.initialCheckpoint.endsWith('.gz')?zlib.gunzipSync(raw):raw).toString());
 const prior=record.seam?.tail_checkpoint??record;
 if(!prior?.parameters||!prior?.states||!prior?.cutHeight)throw new Error('Initial checkpoint has no complete finite-tail state');
 const old=prior.parameters,now=dn.tail.parameters;
 for(const key of ['rCut','wCut','width','curvatureBound','slopeCap','orientation','prefixR','prefixEnd','prefixReturnStart','protectCell','valleyControls','delta0','R','a','etaPower','etaRatioAtN0','rejoinR20At','rejoinIndexOffset','spacing','depth']){
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
  // A final audit retains the finite-tail shooting state as well as its jets,
  // so the joined surface can be reconstructed without another nonlinear solve.
  const checkpoint=req.audit?{parameters:sol.parameters,states:sol.states,cutHeight:req.height,scope:'Finite Fourier/depth shooting state; the far Robin condition is not an exact rotational collar.'}:null;
  console.log(JSON.stringify({converged:sol.converged,residual:sol.normalizedResidual,jets:sol.jets,heightJetJacobian:sol.heightJetJacobian??null,history:sol.history,audit:sol.audit??null,checkpoint}));
 }catch(e){trace({event:'failure',call,error:String(e)});console.log(JSON.stringify({failed:String(e)}));}
}
process.stdin.destroy();
