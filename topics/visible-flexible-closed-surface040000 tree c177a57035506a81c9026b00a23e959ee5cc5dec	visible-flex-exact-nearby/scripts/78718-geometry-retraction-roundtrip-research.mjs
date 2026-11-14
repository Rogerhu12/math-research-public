// R95 floating roundtrip diagnostic, zero direction and lambda=1.
// No ODE, RK, DN, BVP or complete shooting residual is evaluated.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {subdividePhysical} from './950f-tail-subdivision.mjs';
import {createFourierRootSplitFluxEngine} from './78718-tail-fourier-root-split-engine.mjs';
import {prepareGeometricNodeRetraction,initializeFromRawWithMeanGuess} from './78718-tail-geometric-newton-retraction-v2.mjs';

const argv=process.argv.slice(2),args={};
for(let j=0;j<argv.length;j+=2)args[argv[j].replace(/^--/,'')]=argv[j+1];
if(!args.config||!args.checkpoint||!args.out||fs.existsSync(args.out))throw Error('Inputs and a fresh output required');
function identity(p){if(p instanceof URL||String(p).startsWith('file:'))p=fileURLToPath(p);const b=fs.readFileSync(p);return {path:path.resolve(p),bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};}
function read(p){const b=fs.readFileSync(p);return JSON.parse(p.endsWith('.gz')?zlib.gunzipSync(b):b);}
function maximum(v){return Math.max(...Array.from(v,Math.abs));}
function summary(v,M){
 const a=Array.from(v),index=a.reduce((best,x,j)=>Math.abs(x)>Math.abs(a[best])?j:best,0);
 return {maxAbs:maximum(a),maxIndex:index,maxMode:index>=M?(index-M+1)*3:null,
  maxSigned:a[index],qMax:maximum(a.slice(0,M)),piMax:maximum(a.slice(M,2*M)),
  highPiMax:maximum(a.slice(M+Math.floor(M/2),2*M)),l1:a.reduce((s,x)=>s+Math.abs(x),0)};
}
const started=Date.now(),config=read(args.config),packet=read(args.checkpoint),checkpoint=packet.checkpoint,
 physical=createRecalibrationFactory(config).assemble(),stages=subdividePhysical(physical,config.depth,config.shootingParts),
 M=config.modes,K=2*M,spacing=config.spacing,rows=[];
for(const node of (args.nodes??'12,13').split(',').map(Number)){
 const cell=stages.cells[node===0?0:node-1],profile=node===0?cell.profiles.at(-1):cell.profiles[0],
  x=node===0?1:0,portRatio=node===0?cell.portRatio:1,
  engine=createFourierRootSplitFluxEngine({modes:M,spacing,quadrature:config.quadrature,
   mu:cell.mu,orientation:config.orientation,projectionFloor:config.projectionFloor??.05}),
  state=Float64Array.from(checkpoint.states[node]),delta=new Float64Array(state.length),
  y=new Float64Array(K+2);
 for(let j=0;j<M;j++){y[j]=state[j];y[M+j]=state[M+j]*portRatio;}
 const root=engine.root(y,profile,x),prepared=prepareGeometricNodeRetraction({engine,profile,x,
  state,delta,spacing,portRatio,knownRoot:root}),trial=prepared.step(1,{detail:true}),
  bias=Float64Array.from(state,(v,j)=>trial.state[j]-v),
  initialized=initializeFromRawWithMeanGuess(engine,prepared.raw,profile,x,root.L[0]),
  centered=Float64Array.from(state);
 for(let j=0;j<M;j++)centered[M+j]=state[M+j]+(trial.state[M+j]*portRatio-initialized.state[M+j])/portRatio;
 const centeredBias=Float64Array.from(state,(v,j)=>centered[j]-v),
  direct=Float64Array.from(state),factor=engine.orientation*Math.sqrt(2)*root.g.r**4*root.g.w2/(Math.sqrt(12)*engine.mu);
 for(let j=0;j<M;j++)direct[M+j]=factor*root.e.moments[j+1]/portRatio;
 const directBias=Float64Array.from(state,(v,j)=>direct[j]-v),
  rawLGap=Float64Array.from(root.L,(v,j)=>initialized.L[j]-v);
 rows.push({node,x,portRatio,rootRelativeResidual:root.err/root.scale,rootAbsoluteResidual:root.err,
  rootScale:root.scale,minA:root.e.minA,minD:root.e.minD,
  zeroDirectionMaximum:maximum(prepared.rawDirection),meanDirection:prepared.meanLDirection,
  lambda:1,trialDiagnostics:trial.diagnostics,roundtripBias:summary(bias,M),
  centeredBias:summary(centeredBias,M),directMomentBias:summary(directBias,M),
  rawLMaxRoundtripDifference:maximum(rawLGap),rawLMeanDifference:rawLGap[0],
  rawLHighDifference:maximum(rawLGap.slice(1+Math.floor(M/2))),
  state:Array.from(state),roundtripState:Array.from(trial.state),roundtripDifference:Array.from(bias),
  centeredState:Array.from(centered),centeredDifference:Array.from(centeredBias),
  directMomentDifference:Array.from(directBias),rawLDifference:Array.from(rawLGap)});
}
const report={scope:'Actual unconverged fast05 iteration3 node roundtrip, zero Newton direction, lambda=1; pure momentum/mean root evaluation only.',
 inputs:[identity(args.config),identity(args.checkpoint)],script:identity(import.meta.url),
 helper:identity(new URL('./78718-tail-geometric-newton-retraction-v2.mjs',import.meta.url)),
 M,N:config.quadrature,spacing,iteration:packet.iteration,rows,
 ODE_calls:0,DN_calls:0,BVP_calls:0,shooting_residual_evaluations:0,production_changed:false,
 seconds:(Date.now()-started)/1000};
fs.writeFileSync(args.out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({output:identity(args.out),rows:rows.map(v=>({node:v.node,roundtripBias:v.roundtripBias,
 centeredBias:v.centeredBias,directMomentBias:v.directMomentBias,rawLMaxRoundtripDifference:v.rawLMaxRoundtripDifference,
 rawLMeanDifference:v.rawLMeanDifference,rootRelativeResidual:v.rootRelativeResidual})),seconds:report.seconds}));
