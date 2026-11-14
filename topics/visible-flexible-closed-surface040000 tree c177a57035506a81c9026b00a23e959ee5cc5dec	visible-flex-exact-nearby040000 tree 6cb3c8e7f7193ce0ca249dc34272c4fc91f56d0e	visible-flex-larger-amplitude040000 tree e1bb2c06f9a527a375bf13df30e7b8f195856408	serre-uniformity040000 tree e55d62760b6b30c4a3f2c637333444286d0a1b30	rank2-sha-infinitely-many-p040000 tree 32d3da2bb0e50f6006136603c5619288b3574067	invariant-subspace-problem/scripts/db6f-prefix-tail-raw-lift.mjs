// A warm guess only: preserve the old raw height/slope Fourier data when
// raising M, then recompute nonlinear momentum coefficients in the larger
// basis. The unchanged shooting residual must subsequently be solved.
import fs from 'node:fs';
import zlib from 'node:zlib';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {subdividePhysical,buildStableStageGraphs} from './950f-tail-subdivision.mjs';
import {remeshCheckpoint} from './950f-tail-warm-remesh.mjs';
const args=process.argv.slice(2),get=(name,def)=>{const k=args.indexOf(name);return k<0?def:args[k+1];};
const input=get('--checkpoint'),config=get('--config'),output=get('--out');
if(!input||!config||!output)throw Error('Required: --checkpoint saved.json.gz --config target.json --out warm.json.gz');
const sourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;if(!sourceRoot)throw Error('VISIBLE_FLEX_SOURCE_ROOT required');
const sourceURL=name=>pathToFileURL(path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts',name));
const {createFastSplitFluxMomentumTailEngine}=await import(sourceURL('f6tail_fast_split_flux_engine.mjs'));
const bytes=fs.readFileSync(input),record=JSON.parse((input.endsWith('.gz')?zlib.gunzipSync(bytes):bytes).toString());
const prior=record.response?.checkpoint??record.checkpoint??record,cfg=JSON.parse(fs.readFileSync(config,'utf8'));
const old=prior.parameters,oldM=old.modes,M=cfg.modes;
if(!(M>=oldM))throw Error('This lift only raises the Fourier order');
const physical=createRecalibrationFactory(cfg).assemble(),stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts),
  graph=buildStableStageGraphs(physical,stages,{modes:M,spacing:cfg.spacing,linearFar:cfg.linearFar,linearSteps:cfg.linearSteps}),
  parameters={...old,...physical.parameters,modes:M,spacing:cfg.spacing,depth:stages.cells.length,
    physicalDepth:cfg.depth,shootingParts:stages.parts,steps:cfg.steps,quadrature:cfg.quadrature,
    linearFar:cfg.linearFar,linearSteps:cfg.linearSteps,projectionFloor:cfg.projectionFloor??.05},
  pseudoDN={tail:{...stages,graphs:graph.graphs,gains:graph.gains,physical,parameters}},
  states=remeshCheckpoint(prior,pseudoDN,createFastSplitFluxMomentumTailEngine),
  oldCache=new Map(),newCache=new Map();
function engine(cache,modes,quadrature,mu){
  if(!cache.has(mu))cache.set(mu,createFastSplitFluxMomentumTailEngine({modes,spacing:cfg.spacing,quadrature,mu,
    orientation:physical.parameters.orientation,projectionFloor:cfg.projectionFloor??.05}));
  return cache.get(mu);
}
let maxLowHeightChange=0,maxRawSlopeChange=0,maxMeanSlopeChange=0,maxAddedMomentum=0,minRawLeading=Infinity;
for(let i=0;i<states.length;i++){
  // Node i is the input (x=0) of stage i-1. Node0 is the output
  // (x=1) of stage0 and has the documented cross-cell normalization.
  const cell=stages.cells[i===0?0:i-1],profile=cell.profiles[0],x=i===0?1:0,
    factor=i===0?cell.portRatio:1,
    oldEngine=engine(oldCache,oldM,old.quadrature,cell.mu),
    newEngine=engine(newCache,M,cfg.quadrature,cell.mu),small=new Float64Array(2*oldM+2);
  for(let j=0;j<oldM;j++){small[j]=states[i][j];small[oldM+j]=factor*states[i][M+j];}
  const oldRaw=oldEngine.toRaw(small,profile,x),raw=oldRaw.raw,largeRaw=new Float64Array(2*M);
  for(let j=0;j<oldM;j++){largeRaw[j]=raw[j];largeRaw[M+j]=raw[oldM+j];}
  const lifted=newEngine.initializeFromRaw(largeRaw,profile,x),check=newEngine.toRaw(lifted.state,profile,x,lifted.root);
  minRawLeading=Math.min(minRawLeading,check.root.e.minA);
  maxMeanSlopeChange=Math.max(maxMeanSlopeChange,Math.abs(check.meanPhysical-oldRaw.meanPhysical));
  for(let j=0;j<oldM;j++){
    maxLowHeightChange=Math.max(maxLowHeightChange,Math.abs(check.raw[j]-raw[j]));
    maxRawSlopeChange=Math.max(maxRawSlopeChange,Math.abs(check.raw[M+j]-raw[oldM+j]));
  }
  for(let j=oldM;j<M;j++)maxAddedMomentum=Math.max(maxAddedMomentum,Math.abs(lifted.state[M+j]/factor));
  states[i]=Array.from(lifted.state.slice(0,2*M));for(let j=0;j<M;j++)states[i][M+j]/=factor;
}
const height=Array(M).fill(0);for(let j=0;j<oldM;j++)height[j]=prior.cutHeight[j];
const checkpoint={parameters,states,rawNode:stages.rawNode,rawStates:stages.rawNode.map(n=>states[n]),cutHeight:height,
  scope:'UNSOLVED warm guess from raw Fourier lift; no shooting, metric, or geometric claim.'};
const result={scope:'A nonlinear coordinate conversion used only for initialization.',source:input,config,
  oldModes:oldM,newModes:M,maxLowHeightChange,maxRawSlopeChange,maxMeanSlopeChange,maxAddedMomentum,minRawLeading,checkpoint};
const text=JSON.stringify(result);fs.writeFileSync(output,output.endsWith('.gz')?zlib.gzipSync(text):text+'\n');
console.log(JSON.stringify({output,oldModes:oldM,newModes:M,stages:stages.cells.length,
  maxLowHeightChange,maxRawSlopeChange,maxMeanSlopeChange,maxAddedMomentum,minRawLeading,scope:checkpoint.scope}));
