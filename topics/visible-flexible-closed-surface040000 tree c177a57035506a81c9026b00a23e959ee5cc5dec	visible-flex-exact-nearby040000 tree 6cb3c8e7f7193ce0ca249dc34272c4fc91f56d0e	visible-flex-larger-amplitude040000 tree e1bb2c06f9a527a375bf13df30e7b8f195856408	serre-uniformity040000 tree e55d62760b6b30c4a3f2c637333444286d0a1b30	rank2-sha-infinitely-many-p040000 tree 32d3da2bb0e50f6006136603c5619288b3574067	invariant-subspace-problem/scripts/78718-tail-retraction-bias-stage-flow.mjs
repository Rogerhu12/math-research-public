// One-stage zero-direction retraction bias: one base Jacobian, one trial flow.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const opt={},args=process.argv.slice(2);
for(let k=0;k<args.length;k+=2){if(!args[k].startsWith('--')||args[k+1]===undefined)throw Error('key/value arguments required');opt[args[k].slice(2)]=args[k+1];}
if(!opt.snapshot||!opt.config||!opt.roundtrip||!opt.out||fs.existsSync(opt.out))throw Error('snapshot, config, roundtrip and fresh out required');
const dataFile=opt.out.replace(/\.json$/,'')+'-base-jacobian.f64.gz';
if(fs.existsSync(dataFile))throw Error('fresh Jacobian data path required');
const here=path.dirname(fileURLToPath(import.meta.url)),sourceRoot=path.resolve(opt['source-root']??process.env.VISIBLE_FLEX_SOURCE_ROOT??path.join(here,'../repro/source-root'));
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import('./closing_weighted_tail.mjs');
const {subdividePhysical}=await import('./950f-tail-subdivision.mjs');
const {createFourierRootSplitFluxEngine}=await import('./78718-tail-fourier-root-split-engine.mjs');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
function read(p){const b=fs.readFileSync(p);return {object:JSON.parse(b[0]===31&&b[1]===139?zlib.gunzipSync(b):b),identity:{path:path.resolve(p),bytes:b.length,sha256:sha(b)}};}
const started=Date.now(),input=read(opt.snapshot),config=read(opt.config),roundtrip=read(opt.roundtrip),snap=input.object,cfg=config.object,cp=snap.checkpoint;
const M=cfg.modes,N=cfg.quadrature,K=2*M,steps=cfg.steps,stage=snap.iteration.worst.stage,component=snap.iteration.worst.component,scale=snap.iteration.worst.scale;
const physical=createRecalibrationFactory(cfg).assemble(),tail=subdividePhysical(physical,cfg.depth,cfg.shootingParts),cell=tail.cells[stage];
if(cp.parameters.modes!==M||cp.parameters.quadrature!==N||cp.states.length!==tail.cells.length+1)throw Error('snapshot/config stage mismatch');
const inputRow=roundtrip.object.rows.find(v=>v.node===stage+1),targetRow=roundtrip.object.rows.find(v=>v.node===stage);
if(!inputRow||!targetRow)throw Error('both stage endpoint roundtrips required');
for(const row of [inputRow,targetRow]){
 if(row.state.length!==K||row.roundtripState.length!==K||row.state.some((v,j)=>!Object.is(v,cp.states[row.node][j])))throw Error('roundtrip belongs to a different saved node');
 if(row.lambda!==1||row.zeroDirectionMaximum!==0)throw Error('zero-direction lambda=1 roundtrip required');
}
const deltaIn=Float64Array.from(inputRow.roundtripState,(v,j)=>v-inputRow.state[j]);
const deltaTarget=Float64Array.from(targetRow.roundtripState,(v,j)=>v-targetRow.state[j]);
const centeredIdentity=[inputRow,targetRow].every(v=>v.centeredState.every((x,j)=>Object.is(x,v.state[j])));
const options={modes:M,quadrature:N,spacing:cfg.spacing,mu:cell.mu,orientation:cfg.orientation,
 projectionFloor:cfg.projectionFloor??.05,cuspAwareFlow:cfg.cuspAwareFlow===true};
const engine=createFourierRootSplitFluxEngine(options),initial=new Float64Array(K+2);initial.set(inputRow.state);
const base=engine.flowStateWithJacobian(initial,cell.profiles,{stepsPerSegment:steps});
const baseOut=Float64Array.from(base.state.slice(0,K),(v,j)=>j<M?v:v/cell.portRatio);
const J=Float64Array.from({length:K*K},(_,ij)=>base.tangent[ij]/(Math.floor(ij/K)<M?1:cell.portRatio));
if(!Array.from(J).every(Number.isFinite))throw Error('nonfinite stage Jacobian');
const stored=Buffer.alloc(8*(K*K+K+1));
for(let j=0;j<K*K;j++)stored.writeDoubleLE(J[j],8*j);
for(let j=0;j<K;j++)stored.writeDoubleLE(baseOut[j],8*(K*K+j));
stored.writeDoubleLE(base.state[K]+base.state[K+1],8*(K*K+K));
const compressed=zlib.gzipSync(stored,{level:9});if(compressed.length>=5_000_000)throw Error('Jacobian data exceeds file limit');
fs.writeFileSync(dataFile,compressed);
let trial=new Float64Array(K+2);trial.set(inputRow.roundtripState);
for(const profile of cell.profiles)for(let k=0;k<steps;k++)trial=engine.rk4(trial,profile,k/steps,1/steps);
const trialOut=Float64Array.from(trial.slice(0,K),(v,j)=>j<M?v:v/cell.portRatio);
function dotRow(row,lo,hi){
 let sum=0,correction=0;
 for(let j=lo;j<hi;j++){const x=J[row*K+j]*deltaIn[j],next=sum+x;
  correction+=Math.abs(sum)>=Math.abs(x)?(sum-next)+x:(x-next)+sum;sum=next;}
 return sum+correction;
}
const prediction=new Float64Array(K),actualChange=new Float64Array(K),baseResidual=new Float64Array(K),trialResidual=new Float64Array(K);
for(let i=0;i<K;i++){
 prediction[i]=dotRow(i,0,K)-deltaTarget[i];
 actualChange[i]=(trialOut[i]-baseOut[i])-deltaTarget[i];
 baseResidual[i]=baseOut[i]-targetRow.state[i];trialResidual[i]=trialOut[i]-targetRow.roundtripState[i];
}
const maximum=v=>Math.max(...Array.from(v,Math.abs));
function block(rs,cs){let maxEntry=0,maxRowSum=0;for(let i=rs;i<rs+M;i++){let sum=0;for(let j=cs;j<cs+M;j++){const x=Math.abs(J[i*K+j]);maxEntry=Math.max(maxEntry,x);sum+=x;}maxRowSum=Math.max(maxRowSum,sum);}return {maximumEntry:maxEntry,maximumRowSum:maxRowSum};}
const mode=(component%M),high=[];
for(let j=Math.max(0,M-6);j<M;j++){const i=M+j;high.push({frequency:cfg.spacing*(j+1),baseResidual:baseResidual[i],trialResidual:trialResidual[i],
 predictedResidualChange:prediction[i],actualResidualChange:actualChange[i],linearPredictionError:actualChange[i]-prediction[i],
 inputPiRoundtrip:deltaIn[i],targetPiRoundtrip:deltaTarget[i],sameFrequencyPiFromPi:J[i*K+i],sameFrequencyPiFromQ:J[i*K+j]});}
const report={scope:'One-stage test of the actual zero-direction geometric roundtrip. One original base variational flow and one original plain flow at the roundtripped input. The full base Jacobian and output are retained as a small binary file. No full-tail shooting or BVP is run.',
 input:input.identity,config:config.identity,roundtrip:roundtrip.identity,iteration:snap.iteration,
 stage,rawCell:cell.rawCell,rawSegment:cell.rawSegment,part:cell.part,inputNode:stage+1,targetNode:stage,
 modes:M,quadrature:N,steps,portRatio:cell.portRatio,normalizingScale:scale,
 scriptSHA256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),
 sourceSHA256:Object.fromEntries(['78718-tail-fourier-root-split-engine.mjs','78718-tail-fourier-root-momentum.mjs',
  '78718-tail-fourier-product-flow.mjs','78718-tail-fourier-product-jacobian.mjs','950f-tail-subdivision.mjs',
  'closing_weighted_tail.mjs','closing_recalibrated_tail.mjs'].map(f=>[f,sha(fs.readFileSync(path.join(here,f)))])),
 jacobianData:{path:path.resolve(dataFile),bytes:compressed.length,sha256:sha(compressed),dtype:'little-endian float64',
  rows:K,columns:K,layout:'First K*K row-major port-normalized state Jacobian, then K base output coordinates, then mean-height scalar.'},
 blocks:{QQ:block(0,0),QPi:block(0,M),PiQ:block(M,0),PiPi:block(M,M)},
 inputMaximumQBias:maximum(deltaIn.slice(0,M)),inputMaximumPiBias:maximum(deltaIn.slice(M)),
 targetMaximumQBias:maximum(deltaTarget.slice(0,M)),targetMaximumPiBias:maximum(deltaTarget.slice(M)),
 centeredStatesBitwiseEqualBase:centeredIdentity,
 baseNormalizedStageResidual:maximum(baseResidual)/scale,trialNormalizedStageResidual:maximum(trialResidual)/scale,
 savedWorstAbsoluteReplayDifference:Math.abs(baseResidual[component])-snap.iteration.worst.absolute,
 predictedChangeNormalized:maximum(prediction)/scale,actualChangeNormalized:maximum(actualChange)/scale,
 predictionErrorNormalized:maximum(Float64Array.from(actualChange,(v,j)=>v-prediction[j]))/scale,
 savedWorst:{component,frequency:cfg.spacing*(mode+1),baseResidual:baseResidual[component],trialResidual:trialResidual[component],
  predictedChange:prediction[component],actualChange:actualChange[component],
  fromInputQ:dotRow(component,0,M),fromInputPi:dotRow(component,M,K),minusTarget:-deltaTarget[component],
  sameFrequencyPiFromQ:J[component*K+mode],sameFrequencyPiFromPi:J[component*K+M+mode]},
 highModes:high,baseMinimumLeading:base.minA,baseMinimumD:base.minD,baseMaximumRootRelative:base.maxRootRelative,
 actualStageFlows:2,actualShootingSolves:0,actualBVPCalls:0,seconds:(Date.now()-started)/1000};
fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({out:path.resolve(opt.out),bytes:fs.statSync(opt.out).size,jacobianDataBytes:compressed.length,
 baseNorm:report.baseNormalizedStageResidual,trialNorm:report.trialNormalizedStageResidual,
 predictedChange:report.predictedChangeNormalized,actualChange:report.actualChangeNormalized,
 predictionError:report.predictionErrorNormalized,savedWorst:report.savedWorst,seconds:report.seconds}));
