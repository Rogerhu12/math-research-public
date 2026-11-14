// Memory sharing worker; full solve and response protocol are unchanged.
// 950f continuation: frozen weighted metric, own worker; archived constructors unchanged.
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
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
const sourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
if(!sourceRoot)throw Error('VISIBLE_FLEX_SOURCE_ROOT is required');
import {createSplitFluxCompactTailDN as createCompactTailDN} from './db6f-prefix-tail-shared-split.mjs';
import {remeshCheckpoint} from './950f-tail-warm-remesh.mjs';
const {createFastSplitFluxMomentumTailEngine}=await import(pathToFileURL(path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_fast_split_flux_engine.mjs')));
import fs from 'node:fs';
import zlib from 'node:zlib';
import readline from 'node:readline';
const cfg=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
function trace(row){if(cfg.traceFile)fs.appendFileSync(cfg.traceFile,JSON.stringify({time:new Date().toISOString(),...row})+'\n');}
const physical=createRecalibrationFactory(cfg).assemble();
// The weighted factory already finds zeros of the ACTUAL capped/restored slope.
// The inherited DN factory installs raw-source zeros, so retain both lists.
const actualBreakpoints=physical.cells.map(c=>c.profiles.map(p=>[...(p.integrationBreakpoints??[])]));
const dn=createCompactTailDN({...cfg,tail:physical}),M=cfg.modes,zero=dn.cutJets(new Float64Array(2*M));
// The cut restoration can create extra zeros of the actual logarithmic slope.
// Add those zeros to the inherited raw-source cusp grid without changing the
// physical profile. This affects integration only, not any metric parameter.

let last=null,call=0,progressStates=null,progressRow=null,currentHeight=null;
// Optional recovery record: this does not change any numerical operation.
// Its state may be unconverged and is only an initial guess for another solve.
if(cfg.iterationCheckpointFile&&fs.existsSync(cfg.iterationCheckpointFile))
 throw new Error('Iteration checkpoint path already exists');
function retainIteration(row,states){
 if(!cfg.iterationCheckpointFile)return;
 const checkpoint={parameters:dn.tail.parameters,states,rawNode:dn.tail.rawNode,
  rawStates:dn.tail.rawNode.map(n=>states[n]),cutHeight:currentHeight,
  scope:'UNCONVERGED iteration checkpoint for recovery only; not a solved DN response or geometric certificate.'};
 const data=zlib.gzipSync(JSON.stringify({status:'iteration-recovery-only',call,
  iteration:row,checkpoint})+'\n');
 if(data.length>=5_000_000)throw new Error('Iteration checkpoint exceeds repository file limit');
 const tmp=cfg.iterationCheckpointFile+'.tmp';fs.writeFileSync(tmp,data);
 fs.renameSync(tmp,cfg.iterationCheckpointFile);
}
if(cfg.initialCheckpoint){
 const raw=fs.readFileSync(cfg.initialCheckpoint),record=JSON.parse((cfg.initialCheckpoint.endsWith('.gz')?zlib.gunzipSync(raw):raw).toString());
 const prior=record.response?.checkpoint??record.seam?.tail_checkpoint??record.checkpoint??record;
 if(!prior?.parameters||!prior?.states||!prior?.cutHeight)throw new Error('Initial checkpoint has no complete finite-tail state');
 const old=prior.parameters,now=dn.tail.parameters;
 for(const key of ['pulseCaps','valleyCaps','flatOuterThroughCell','flatOuterStartSegment','flatSlope','capMode','rCut','wCut','width','curvatureBound','slopeCap','capTransition','calibrationSteps','warpSteps','quadratureTolerance','cuspAwareQuadrature','orientation','prefixR','prefixEnd','prefixReturnStart','protectCell','warpWeightLevels','constructor','valleyControls','delta0','R','a','etaPower','etaRatioAtN0','rejoinR20At','rejoinIndexOffset','spacing']){
  if(JSON.stringify(old[key]??null)!==JSON.stringify(now[key]??null))throw new Error('Warm tail geometry mismatch: '+key);
 }
 if((old.physicalDepth??old.depth)>cfg.depth)throw new Error('Warm remesh cannot shorten physical depth');

 const oldM=old.modes,keep=Math.min(oldM,M);
 const states=remeshCheckpoint(prior,dn,createFastSplitFluxMomentumTailEngine);
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
  const req=JSON.parse(line);if(req.stop)break;currentHeight=req.height;progressStates=null;progressRow=null;
  call++;const start=Date.now();trace({event:'request',call,height:req.height,jacobian:!!req.jacobian,audit:!!req.audit});
  let initial;
  if(last){
   const prev=last.jets.height[0],ratio=req.height[0]/prev;
   if(Number.isFinite(ratio)&&ratio>.25&&ratio<4)initial=last.states.map(row=>row.map((v,j)=>v*(cfg.harmonicAmplitudePredictor===true && req.height.slice(1).every(x=>x===0)?ratio**(j%M+1):ratio)));
  }
  // Warm starts must satisfy the NEW Dirichlet height, including higher modes.
  // Add the exact finite linear response of the height difference; this is only
  // an initial guess. The full nonlinear root/ODE/residual still decides success.
  if(initial&&cfg.correctInitialBoundary!==false){
   const r4=zero.radius**4,delta=Float64Array.from(req.height,(v,j)=>v/r4-initial[0][j]),add=dn.tail.initial(delta);
   initial=initial.map((row,n)=>row.map((v,j)=>v+add[n][j]));
  }
  const sol=dn.solve(req.height,{maxIterations:cfg.maxIterations??24,tolerance:cfg.solveTolerance??2e-10,initial,jacobian:!!req.jacobian,audit:!!req.audit,auditSteps:cfg.auditSteps??cfg.steps,progress:(row,states)=>{if(states){progressStates=states;progressRow=row;retainIteration(row,states);}trace({event:'iteration',call,elapsed_ms:Date.now()-start,...row});}});
  if(sol.converged)last=sol;
  trace({event:'response',call,elapsed_ms:Date.now()-start,converged:sol.converged,residual:sol.normalizedResidual,maxChartCondition:Math.max(...sol.history.map(x=>x.chartCondition??0))});
  // Every actual response retains the shooting state. Audit execution itself
  // is still controlled by req.audit and has not been weakened or bypassed.
  const checkpoint={parameters:sol.parameters,states:sol.states,rawNode:dn.tail.rawNode,rawStates:dn.tail.rawNode.map(n=>sol.states[n]),cutHeight:req.height,scope:'Finite Fourier/depth shooting state; the far Robin condition is not an exact rotational collar. Retained for every actual response; an unaudited response is not a final geometric audit.'};
  console.log(JSON.stringify({converged:sol.converged,residual:sol.normalizedResidual,jets:sol.jets,heightJetJacobian:sol.heightJetJacobian??null,history:sol.history,audit:sol.audit??null,checkpoint}));
 }catch(e){trace({event:'failure',call,error:String(e)});console.log(JSON.stringify({failed:String(e),lastIteration:progressRow,checkpoint:progressStates?{parameters:dn.tail.parameters,states:progressStates,rawNode:dn.tail.rawNode,rawStates:dn.tail.rawNode.map(n=>progressStates[n]),cutHeight:currentHeight,scope:'FAILED Newton state; retained only for diagnosis and possible initial guesses.'}:null}));}
}
process.stdin.destroy();
