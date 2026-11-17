// Compare the original and periodic-only algebra on accepted actual stage
// states. This is not a new tail solve or a whole-trajectory speed guarantee.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const [topic,recordFile,outFile]=process.argv.slice(2),source=path.join(topic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=source;
process.env.CLOSING_TAIL_CACHE=path.join(source,'topics/large-amplitude-twist-flex/scripts');
const originalModule=path.join(source,'topics/large-amplitude-twist-flex/scripts/f6tail_fast_split_flux_engine.mjs');
const periodicModule=path.join(topic,'scripts/periodic-quadrature/f6tail_fast_split_flux_engine.mjs');
const {createFastSplitFluxMomentumTailEngine:originalFactory}=await import(pathToFileURL(originalModule));
const {createFastSplitFluxMomentumTailEngine:periodicFactory}=await import(pathToFileURL(periodicModule));
const {withCuspAwareRK}=await import(pathToFileURL(path.join(source,'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs')));
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {subdividePhysical}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-subdivision.mjs')));
const data=JSON.parse(gunzipSync(fs.readFileSync(recordFile))),cfg=data.config,cp=data.response.checkpoint;
if(!data.response.converged||!(data.response.residual<=cfg.solveTolerance))throw Error('Expected an accepted actual input tail');
const physical=createRecalibrationFactory(cfg).assemble(),stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts),
 M=cfg.modes,K=2*M,N=cfg.quadrature,rows=[];
function difference(a,b){let abs=0,scale=0;for(let j=0;j<a.length;j++){abs=Math.max(abs,Math.abs(a[j]-b[j]));scale=Math.max(scale,Math.abs(a[j]),Math.abs(b[j]));}return {linf:abs,scale,relative:abs/Math.max(1e-300,scale)};}
for(const index of [0,40,46,120]){
 const cell=stages.cells[index],p=cell.profiles[0],options={modes:M,spacing:cfg.spacing,quadrature:N,mu:cell.mu,
  orientation:physical.parameters.orientation,projectionFloor:cp.parameters.projectionFloor??.05},
  original=withCuspAwareRK(originalFactory(options)),periodic=withCuspAwareRK(periodicFactory(options));
 if(original.N!==N||periodic.N!==N)throw Error('Public N changed');
 let state=new Float64Array(K+2);state.set(cp.states[index+1]);
 for(const x of [0,.5]){
  if(x===.5)for(let k=0;k<cfg.steps/2;k++)state=original.rk4(state,p,k/cfg.steps,1/cfg.steps);
  const startA=performance.now(),a=original.rhsWithJacobian(state,p,x),msA=performance.now()-startA;
  const startB=performance.now(),b=periodic.rhsWithJacobian(state,p,x),msB=performance.now()-startB;
  if(a.root.e.rows.length!==N||b.root.e.rows.length!==N)throw Error('Full angular rows not retained');
  const independent=periodic.quadratureIndependentNodes,keys=['P','Pt','L','K','U','S','D','A','sd','quad'];
  let periodicCopyError=0,rowDifference=0;
  for(let n=0;n<N;n++)for(const key of keys){
   periodicCopyError=Math.max(periodicCopyError,Math.abs(b.root.e.rows[n][key]-b.root.e.rows[n%independent][key]));
   rowDifference=Math.max(rowDifference,Math.abs(a.root.e.rows[n][key]-b.root.e.rows[n][key]));
  }
  const common=original.evaluateL(b.root.L,state.slice(0,M),a.root.g,true),
   f=physical.parameters.orientation*Math.sqrt(12)*cell.mu/(Math.sqrt(2)*a.root.g.r**4*a.root.g.w2),
   target=Float64Array.from({length:M+1},(_,j)=>j?f*state[M+j-1]:0);
  let originalMomentResidual=0;
  for(let j=0;j<=M;j++)originalMomentResidual=Math.max(originalMomentResidual,Math.abs(common.moments[j]-target[j]));
  const row={stage:index,rawCell:cell.rawCell,rawSegment:cell.rawSegment,x,modes:M,declaredN:N,
   independentRows:independent,multiplicity:periodic.quadraturePeriodMultiplicity,fullRows:b.root.e.rows.length,
   root:difference(a.root.L,b.root.L),rootGram:difference(a.root.e.B,b.root.e.B),
   rhs:difference(a.derivative,b.derivative),jacobian:difference(a.jacobian,b.jacobian),
   originalRootRelativeResidual:a.root.err/a.root.scale,periodicRootRelativeResidual:b.root.err/b.root.scale,
   periodicRootInOriginalMomentRelativeResidual:originalMomentResidual/a.root.scale,
   originalMinA:a.root.e.minA,periodicMinA:b.root.e.minA,originalMinD:a.root.e.minD,periodicMinD:b.root.e.minD,
   periodicCopyError,fullRowsLinfDifference:rowDifference,originalMilliseconds:msA,periodicMilliseconds:msB};
  rows.push(row);console.log(JSON.stringify(row));
 }
}
const bad={modes:M,spacing:cfg.spacing,quadrature:4*M*cfg.spacing,mu:stages.cells[0].mu,orientation:1,projectionFloor:.05};
const guard={};
for(const [name,factory] of [['original',originalFactory],['periodic',periodicFactory]]){
 try{factory(bad);guard[name]='NOT_REJECTED';}catch(error){guard[name]=String(error);}
}
if(guard.original!==guard.periodic||guard.periodic==='NOT_REJECTED')throw Error('Original strict N guard differs');
const output={scope:'Eight local actual-state comparisons, no new solve; mathematically identical periodic quadrature, different floating arithmetic. Timings are local single-call observations only.',
 input_sha256:createHash('sha256').update(fs.readFileSync(recordFile)).digest('hex'),
 source_sha256:createHash('sha256').update(fs.readFileSync(process.argv[1])).digest('hex'),
 inputAcceptedResidual:data.response.residual,guard,rows,
 maxima:{rootRelative:Math.max(...rows.map(r=>r.root.relative)),rhsRelative:Math.max(...rows.map(r=>r.rhs.relative)),
  jacobianRelative:Math.max(...rows.map(r=>r.jacobian.relative)),rootAbsolute:Math.max(...rows.map(r=>r.root.linf)),
  rhsAbsolute:Math.max(...rows.map(r=>r.rhs.linf)),jacobianAbsolute:Math.max(...rows.map(r=>r.jacobian.linf)),
  originalMomentResidualAtPeriodicRoot:Math.max(...rows.map(r=>r.periodicRootInOriginalMomentRelativeResidual))}};
fs.writeFileSync(outFile,JSON.stringify(output,null,2)+'\n');
console.log(JSON.stringify({maxima:output.maxima,guard}));
