// Read-only localization of finite state defects, including explicitly failed
// Newton checkpoints. Build one state engine per stage; no Jacobian or solve.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const [topic,recordFile,outFile]=process.argv.slice(2);
const source=path.join(topic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=source;
process.env.CLOSING_TAIL_CACHE=path.join(source,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {subdividePhysical,buildStableStageGraphs}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-subdivision.mjs')));
const {createSplitFluxMomentumTailEngine}=await import(pathToFileURL(path.join(source,'topics/large-amplitude-twist-flex/scripts/f6tail_momentum_split_flux.mjs')));
const {integrationGrid}=await import(pathToFileURL(path.join(source,'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs')));
const record=JSON.parse(gunzipSync(fs.readFileSync(recordFile))),cfg=record.config,checkpoint=record.response?.checkpoint;
if(!checkpoint?.states)throw Error('No saved actual trial state');
const physical=createRecalibrationFactory(cfg).assemble(),stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts),
 M=cfg.modes,K=2*M,size=K+2,states=checkpoint.states,
 linear=buildStableStageGraphs(physical,stages,{modes:M,spacing:cfg.spacing,linearFar:cfg.linearFar,linearSteps:cfg.linearSteps});
if(states.length!==stages.cells.length+1)throw Error('Stage count differs');
const r=stages.cells[0].profiles.at(-1)(1).r,target=checkpoint.cutHeight.map(x=>x/r**4),scales=[Math.max(1e-250,...target.map(Math.abs))];
for(let n=0;n<stages.cells.length;n++)scales.push(scales[n]/Math.abs(linear.gains[n][0]));
const rows=[];
for(let n=0;n<stages.cells.length;n++){
 const cell=stages.cells[n],engine=createSplitFluxMomentumTailEngine({modes:M,spacing:cfg.spacing,quadrature:cfg.quadrature,
  mu:cell.mu,orientation:physical.parameters.orientation,projectionFloor:checkpoint.parameters.projectionFloor??.05});
 let state=new Float64Array(size);state.set(states[n+1]);
 let minA=Infinity,minD=Infinity,minS=Infinity,maxRootRelative=0,where=null,error=null;
 function rhs(s,p,x){
  const rt=engine.root(s,p,x);
  if(rt.e.minA<minA){minA=rt.e.minA;where={x,r:rt.g.r,w:rt.g.w};}
  minD=Math.min(minD,rt.e.minD);minS=Math.min(minS,rt.e.minS);maxRootRelative=Math.max(maxRootRelative,rt.err/rt.scale);
  return engine.rhs(s,p,x,false,rt);
 }
 try{
  for(const p of cell.profiles){
   const grid=integrationGrid(cfg.steps,cfg.cuspAwareFlow?(p.integrationBreakpoints??[]):[]);
   for(let k=0;k<grid.length-1;k++){
    const x=grid[k],h=grid[k+1]-x,a=rhs(state,p,x),
     b=rhs(Float64Array.from(state,(v,j)=>v+h*a[j]/2),p,x+h/2),
     c=rhs(Float64Array.from(state,(v,j)=>v+h*b[j]/2),p,x+h/2),
     d=rhs(Float64Array.from(state,(v,j)=>v+h*c[j]),p,x+h);
    state=Float64Array.from(state,(v,j)=>v+h*(a[j]+2*b[j]+2*c[j]+d[j])/6);
   }
  }
 }catch(e){error=String(e);}
 let normalizedResidual=0,component=-1;
 if(!error)for(let j=0;j<K;j++){
  const v=Math.abs(state[j]/(j<M?1:cell.portRatio)-states[n][j])/scales[n];
  if(v>normalizedResidual){normalizedResidual=v;component=j;}
 }
 rows.push({stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,rawLeft:cell.rawLeft,rawRight:cell.rawRight,
  minA,minD,minS,maxRootRelative,where,error,normalizedResidual:error?null:normalizedResidual,component,
  stateLinf:Math.max(...states[n].map(Math.abs)),normalizationScale:scales[n]});
}
const result={scope:'Read-only finite RK and local-root stage diagnostic. The input may be an explicitly failed global trial; this is neither a new solve nor acceptance.',
 inputAccepted:record.response.converged===true&&record.response.residual<=cfg.solveTolerance,
 inputFailure:record.response.failed??null,source_sha256:createHash('sha256').update(fs.readFileSync(process.argv[1])).digest('hex'),
 input_sha256:createHash('sha256').update(fs.readFileSync(recordFile)).digest('hex'),stages:rows.length,
 failedStages:rows.filter(x=>x.error),lowestA:rows.toSorted((a,b)=>a.minA-b.minA).slice(0,8),
 largestResidual:rows.filter(x=>!x.error).toSorted((a,b)=>b.normalizedResidual-a.normalizedResidual).slice(0,8),
 largestRootResidual:rows.toSorted((a,b)=>b.maxRootRelative-a.maxRootRelative).slice(0,8)};
fs.writeFileSync(outFile,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result));
