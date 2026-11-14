// Only the previously identified stage: P8/S32 versus two P16/S16 panels.
// The old RK midpoint is actually integrated, and the old endpoints are kept.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const opt={},args=process.argv.slice(2);
for(let k=0;k<args.length;k+=2){if(!args[k].startsWith('--')||args[k+1]===undefined)throw Error('key/value arguments required');opt[args[k].slice(2)]=args[k+1];}
if(!opt.snapshot||!opt.config||!opt['base-report']||!opt.out||fs.existsSync(opt.out))throw Error('snapshot, config, base-report and fresh out required');
const dataFile=opt.out.replace(/\.json$/,'')+'-half-jacobians.f64.gz';if(fs.existsSync(dataFile))throw Error('fresh Jacobian data required');
const here=path.dirname(fileURLToPath(import.meta.url)),sourceRoot=path.resolve(opt['source-root']??process.env.VISIBLE_FLEX_SOURCE_ROOT??path.join(here,'../repro/source-root'));
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import('./closing_weighted_tail.mjs');
const {subdividePhysical}=await import('./950f-tail-subdivision.mjs');
const {createFourierRootSplitFluxEngine}=await import('./78718-tail-fourier-root-split-engine.mjs');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
function read(p){const b=fs.readFileSync(p);return {object:JSON.parse(b[0]===31&&b[1]===139?zlib.gunzipSync(b):b),identity:{path:path.resolve(p),bytes:b.length,sha256:sha(b)}};}
const started=Date.now(),input=read(opt.snapshot),config=read(opt.config),prior=read(opt['base-report']);
const snap=input.object,cfg=config.object,cp=snap.checkpoint,M=cfg.modes,N=cfg.quadrature,K=2*M,stage=prior.object.stage;
if(prior.object.input.sha256!==input.identity.sha256||prior.object.config.sha256!==config.identity.sha256)throw Error('base and proposed split use different input');
const bytes=fs.readFileSync(prior.object.jacobianData.path);if(sha(bytes)!==prior.object.jacobianData.sha256)throw Error('base Jacobian data hash mismatch');
const raw=zlib.gunzipSync(bytes),baseJ=Float64Array.from({length:K*K},(_,j)=>raw.readDoubleLE(8*j));
const baseOut=Float64Array.from({length:K},(_,j)=>raw.readDoubleLE(8*(K*K+j))),baseMean=raw.readDoubleLE(8*(K*K+K));
const physical=createRecalibrationFactory(cfg).assemble(),oldTail=subdividePhysical(physical,cfg.depth,cfg.shootingParts),old=oldTail.cells[stage];
const fineTail=subdividePhysical(physical,cfg.depth,2*cfg.shootingParts);
const fine=fineTail.cells.map((cell,index)=>({cell,index})).filter(({cell})=>cell.rawCell===old.rawCell&&cell.rawSegment===old.rawSegment&&cell.rawLeft>=old.rawLeft&&cell.rawRight<=old.rawRight).sort((a,b)=>a.cell.rawLeft-b.cell.rawLeft);
if(fine.length!==2||cfg.steps%2)throw Error('this comparison requires two dyadic subpanels');
if(old.portRatio!==1||fine.some(v=>v.cell.portRatio!==1))throw Error('the selected interior stage must use unscaled interface momenta');
const steps=cfg.steps/2,scale=snap.iteration.worst.scale,component=snap.iteration.worst.component;
const engine=createFourierRootSplitFluxEngine({modes:M,quadrature:N,spacing:cfg.spacing,mu:old.mu,
 orientation:cfg.orientation,projectionFloor:cfg.projectionFloor??.05,cuspAwareFlow:cfg.cuspAwareFlow===true});
const initial=new Float64Array(K+2);initial.set(cp.states[stage+1]);
let midpoint=Float64Array.from(initial);
for(let k=0;k<cfg.steps/2;k++)midpoint=engine.rk4(midpoint,old.profiles[0],k/cfg.steps,1/cfg.steps);
const canonicalMid=midpoint.slice(0,K),halfFlows=[],halfMatrices=[],halfOutputs=[];
const maximum=v=>Math.max(...Array.from(v,Math.abs));
function difference(a,b){return maximum(Float64Array.from(a,(v,j)=>v-b[j]));}
function blocks(J){
 const result={};
 for(const [name,rs,cs] of [['QQ',0,0],['QPi',0,M],['PiQ',M,0],['PiPi',M,M]]){
  let maxEntry=0,maxRowSum=0;for(let i=rs;i<rs+M;i++){let sum=0;for(let j=cs;j<cs+M;j++){const x=Math.abs(J[i*K+j]);maxEntry=Math.max(maxEntry,x);sum+=x;}maxRowSum=Math.max(maxRowSum,sum);}
  result[name]={maximumEntry:maxEntry,maximumRowSum:maxRowSum};
 }
 return result;
}
for(let h=0;h<2;h++){
 const {cell,index}=fine[h],seed=new Float64Array(K+2);seed.set(h===0?cp.states[stage+1]:canonicalMid);
 const begin=performance.now(),flow=engine.flowStateWithJacobian(seed,cell.profiles,{stepsPerSegment:steps});
 const J=Float64Array.from(flow.tangent.slice(0,K*K)),out=flow.state.slice(0,K),target=h===0?canonicalMid:cp.states[stage];
 halfMatrices.push(J);halfOutputs.push(out);
 let piRow=0;for(let j=M;j<K;j++)piRow+=Math.abs(J[component*K+j]);
 halfFlows.push({half:h,direction:'increasing original-stage x',fineStage:index,part:cell.part,
  rawLeft:cell.rawLeft,rawRight:cell.rawRight,steps,breakpointCount:cell.profiles[0].integrationBreakpoints?.length??0,
  milliseconds:performance.now()-begin,blocks:blocks(J),sameFrequencyPiFromPi:J[component*K+component],
  sameFrequencyPiFromQ:J[component*K+component-M],pi63RowPiBlockL1:piRow,
  maximumStateDifferenceToRetainedTarget:difference(out,target),
  residualUsingOldStageReferenceScale:difference(out,target)/scale,
  minimumLeading:flow.minA,minimumD:flow.minD,maximumRootRelative:flow.maxRootRelative,
  meanHeight:flow.state[K]+flow.state[K+1]});
}
const composed=new Float64Array(K*K);
for(let i=0;i<K;i++)for(let j=0;j<K;j++){
 let sum=0,c=0;for(let k=0;k<K;k++){
  const v=halfMatrices[1][i*K+k]*halfMatrices[0][k*K+j],next=sum+v;
  c+=Math.abs(sum)>=Math.abs(v)?(sum-next)+v:(v-next)+sum;sum=next;
 }composed[i*K+j]=sum+c;
}
let maxJDiff=0,maxJScaled=0;for(let i=0;i<K*K;i++){const d=Math.abs(composed[i]-baseJ[i]);maxJDiff=Math.max(maxJDiff,d);maxJScaled=Math.max(maxJScaled,d/Math.max(1,Math.abs(baseJ[i])));}
const flat=[...canonicalMid];for(let h=0;h<2;h++)flat.push(...halfMatrices[h],...halfOutputs[h],halfFlows[h].meanHeight);
const binary=Buffer.alloc(8*flat.length);for(let j=0;j<flat.length;j++)binary.writeDoubleLE(flat[j],8*j);
const compressed=zlib.gzipSync(binary,{level:9});if(compressed.length>=5_000_000)throw Error('half data exceeds size limit');fs.writeFileSync(dataFile,compressed);
const report={scope:'One old stage only. An actual original-RK midpoint, then two P16/S16 variational flows at the same physical RK density. Old endpoints retained. Old full-stage J/output are read from the saved earlier experiment. No full-tail DN or BVP; old normalization scale is only a local comparison reference.',
 input:input.identity,config:config.identity,baseReport:prior.identity,stage,rawCell:old.rawCell,rawSegment:old.rawSegment,
 originalParts:cfg.shootingParts,newParts:2*cfg.shootingParts,originalSteps:cfg.steps,newSteps:steps,
 originalLinearSteps:cfg.linearSteps,referenceScale:scale,modes:M,quadrature:N,
 originalInputNode:stage+1,originalTargetNode:stage,oldRKStepsUsedToObtainMidpoint:cfg.steps/2,
 midpointMatchesFirstFineFlowBitwise:halfOutputs[0].every((v,j)=>Object.is(v,canonicalMid[j])),
 midpointShapeDifference:difference(halfOutputs[0],canonicalMid),
 composedShapeDifferenceToOriginalFullFlow:difference(halfOutputs[1],baseOut),
 composedMeanHeightDifferenceToOriginal:halfFlows[0].meanHeight+halfFlows[1].meanHeight-baseMean,
 composedJacobianMaximumDifference:maxJDiff,composedJacobianMaximumScaledDifference:maxJScaled,
 originalBlocks:blocks(baseJ),halfFlows,
 data:{path:path.resolve(dataFile),bytes:compressed.length,sha256:sha(compressed),dtype:'little-endian float64',
  layout:'First K original midpoint shape coordinates, then for each of two physical halves: K*K row-major J, K output coordinates, one mean-height scalar.',K},
 scriptSHA256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),
 sourceSHA256:Object.fromEntries(['78718-tail-fourier-root-split-engine.mjs','78718-tail-fourier-root-momentum.mjs',
  '78718-tail-fourier-product-flow.mjs','78718-tail-fourier-product-jacobian.mjs','950f-tail-subdivision.mjs',
  'closing_weighted_tail.mjs','closing_recalibrated_tail.mjs'].map(f=>[f,sha(fs.readFileSync(path.join(here,f)))])),
 actualFullStageReruns:0,actualOriginalHalfStateFlows:1,actualFineHalfVariationalFlows:2,
 actualShootingSolves:0,actualBVPCalls:0,seconds:(Date.now()-started)/1000};
fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({out:path.resolve(opt.out),bytes:fs.statSync(opt.out).size,
 halfPiPiMax:halfFlows.map(v=>v.blocks.PiPi.maximumEntry),halfPi63Gain:halfFlows.map(v=>v.sameFrequencyPiFromPi),
 midpointShapeDifference:report.midpointShapeDifference,composedShapeDifference:report.composedShapeDifferenceToOriginalFullFlow,
 composedJRelativeDifference:maxJScaled,seconds:report.seconds}));
