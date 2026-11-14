// Same saved states and physical endpoints; algebraic roots only, no ODE/DN.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const opt={},args=process.argv.slice(2);
for(let k=0;k<args.length;k+=2){if(!args[k].startsWith('--')||args[k+1]===undefined)throw Error('key/value arguments required');opt[args[k].slice(2)]=args[k+1];}
if(!opt.snapshot||!opt.config||!opt.out||fs.existsSync(opt.out))throw Error('--snapshot --config and fresh --out required');
const here=path.dirname(fileURLToPath(import.meta.url));
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.resolve(opt['source-root']??process.env.VISIBLE_FLEX_SOURCE_ROOT??path.join(here,'../repro/source-root'));
process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import('./closing_weighted_tail.mjs');
const {subdividePhysical}=await import('./950f-tail-subdivision.mjs');
const {createFourierRootMomentumTailEngine}=await import('./78718-tail-fourier-root-momentum.mjs');
const {createFourierTightRootMomentumTailEngine}=await import('./78718-tail-fourier-root-tight-momentum.mjs');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
function read(p){const b=fs.readFileSync(p);return {object:JSON.parse(b[0]===31&&b[1]===139?zlib.gunzipSync(b):b),identity:{path:path.resolve(p),bytes:b.length,sha256:sha(b)}};}
const started=Date.now(),input=read(opt.snapshot),config=read(opt.config),snap=input.object,cfg=config.object,cp=snap.checkpoint;
const M=cfg.modes,N=cfg.quadrature,J=M+1,K=2*M,stage=Number(opt.stage??snap.iteration?.worst?.stage??12);
if(cp.parameters.modes!==M||cp.parameters.quadrature!==N)throw Error('snapshot/config numerical dimensions differ');
const physical=createRecalibrationFactory(cfg).assemble(),tail=subdividePhysical(physical,cfg.depth,cfg.shootingParts),cell=tail.cells[stage];
if(!cell||cp.states.length!==tail.cells.length+1)throw Error('snapshot/stage mismatch');
const options={modes:M,quadrature:N,spacing:cfg.spacing,mu:cell.mu,orientation:cfg.orientation,projectionFloor:cfg.projectionFloor??.05};
const normal=createFourierRootMomentumTailEngine(options),tight=createFourierTightRootMomentumTailEngine(options),profile=cell.profiles[0];

function eigenSummary(matrix,n){
 const a=Float64Array.from(matrix);let lower=Infinity,upper=-Infinity,skew=0;
 for(let i=0;i<n;i++){
  let radius=0;for(let j=0;j<n;j++)if(i!==j){radius+=Math.abs(a[i*n+j]);skew=Math.max(skew,Math.abs(a[i*n+j]-a[j*n+i]));}
  lower=Math.min(lower,a[i*n+i]-radius);upper=Math.max(upper,a[i*n+i]+radius);
 }
 let maxOff=Infinity,iterations=0;
 for(;iterations<50*n*n;iterations++){
  let p=0,q=1;maxOff=0;
  for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)if(Math.abs(a[i*n+j])>maxOff){maxOff=Math.abs(a[i*n+j]);p=i;q=j;}
  let maxDiag=0;for(let i=0;i<n;i++)maxDiag=Math.max(maxDiag,Math.abs(a[i*n+i]));
  if(maxOff<=2e-16*Math.max(1,maxDiag))break;
  const apq=a[p*n+q],tau=(a[q*n+q]-a[p*n+p])/(2*apq),t=(tau>=0?1:-1)/(Math.abs(tau)+Math.hypot(1,tau));
  const c=1/Math.hypot(1,t),s=t*c;
  const app=a[p*n+p],aqq=a[q*n+q];
  for(let k=0;k<n;k++)if(k!==p&&k!==q){
   const ap=a[k*n+p],aq=a[k*n+q],vp=c*ap-s*aq,vq=s*ap+c*aq;
   a[k*n+p]=a[p*n+k]=vp;a[k*n+q]=a[q*n+k]=vq;
  }
  a[p*n+p]=app-t*apq;a[q*n+q]=aqq+t*apq;a[p*n+q]=a[q*n+p]=0;
 }
 const diag=Array.from({length:n},(_,i)=>a[i*n+i]),minimum=Math.min(...diag),maximum=Math.max(...diag);
 return {dimension:n,symmetryGap:skew,gershgorinLower:lower,gershgorinUpper:upper,
  gershgorinConditionUpperEstimate:lower>0?upper/lower:null,
  eigenvalueMinimumApprox:minimum,eigenvalueMaximumApprox:maximum,condition2Approx:maximum/minimum,
  jacobiFinalOffDiagonalMaximum:maxOff,jacobiRotations:iterations,
  scope:'Floating diagnostics of the assembled matrix; no outward eigenvalue certificate.'};
}
function summary(rt,state){
 const f=cfg.orientation*Math.sqrt(12)*cell.mu/(Math.sqrt(2)*rt.g.r**4*rt.g.w2),res=new Float64Array(J);
 for(let j=0;j<J;j++)res[j]=rt.e.moments[j]-(j===0?0:f*state[M+j-1]);
 const high=[];for(let j=Math.max(1,M-5);j<=M;j++)high.push({modeIndex:j,frequency:cfg.spacing*j,
  residual:res[j],relativeToRootScale:Math.abs(res[j])/rt.scale,impliedMomentumResidual:res[j]/f,
  targetMagnitude:Math.abs(f*state[M+j-1])});
 const weights=rt.e.rows.map(v=>v.A/(v.D*Math.sqrt(v.D)));
 return {iterations:rt.iterations,error:rt.err,scale:rt.scale,relativeResidual:rt.err/rt.scale,
  roundoffFallback:rt.roundoffFallback===true,meanResidual:res[0],meanPhysical:rt.g.w*rt.L[0],
  meanRootCoefficient:rt.L[0],minA:rt.e.minA,minD:rt.e.minD,minS:rt.e.minS,
  maximumImpliedMomentumResidual:Math.max(...Array.from(res.slice(1),v=>Math.abs(v/f))),
  highModes:high,gram:eigenSummary(rt.e.B,J),
  gramAngularWeightMinimum:Math.min(...weights),gramAngularWeightMaximum:Math.max(...weights),
  rootPrecision:rt.rootPrecision??null};
}
function change(a,b){
 let maxL=0,nonmeanSlopeL1=0,maxGram=0,maxA=0,maxD=0;
 for(let j=0;j<J;j++){maxL=Math.max(maxL,Math.abs(a.L[j]-b.L[j]));if(j)nonmeanSlopeL1+=Math.sqrt(2)*a.g.w*Math.abs(a.L[j]-b.L[j]);}
 for(let j=0;j<a.e.B.length;j++)maxGram=Math.max(maxGram,Math.abs(a.e.B[j]-b.e.B[j]));
 for(let j=0;j<N;j++){maxA=Math.max(maxA,Math.abs(a.e.rows[j].A-b.e.rows[j].A));maxD=Math.max(maxD,Math.abs(a.e.rows[j].D-b.e.rows[j].D));}
 return {maximumLCoefficientChange:maxL,meanPhysicalChange:a.g.w*(b.L[0]-a.L[0]),
  nonmeanRadialHeightSlopeCoefficientL1Change:nonmeanSlopeL1,maximumGramEntryChange:maxGram,
  maximumLeadingChange:maxA,maximumDChange:maxD};
}
const endpoints=[];
for(const x of [0,1]){
 const node=x===0?stage+1:stage,state=new Float64Array(K+2);state.set(cp.states[node]);
 if(x===1)for(let j=M;j<K;j++)state[j]*=cell.portRatio;
 const a=normal.root(state,profile,x),row={stage,x,node,rawCell:cell.rawCell,rawSegment:cell.rawSegment,
  part:cell.part,portRatio:cell.portRatio,geometry:{r:a.g.r,w:a.g.w,E:a.g.E,drdx:a.g.drdx},normal:summary(a,state)};
 try{const b=tight.root(state,profile,x);row.tight={ok:true,...summary(b,state)};row.tightChange=change(a,b);}
 catch(error){row.tight={ok:false,error:String(error)};}
 try{const b=tight.root(state,profile,x,a.L);row.tightFromNormal={ok:true,...summary(b,state)};row.tightFromNormalChange=change(a,b);}
 catch(error){row.tightFromNormal={ok:false,error:String(error)};}
 endpoints.push(row);
}
const report={scope:'Algebraic roots only at the two endpoints of one actual saved shooting stage. Same Q/pi state and physical profile. This cannot determine accumulation of root errors along an unexecuted flow.',
 input:input.identity,config:config.identity,iteration:snap.iteration,modes:M,quadrature:N,
 scriptSHA256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),
 sourceSHA256:Object.fromEntries(['78718-tail-fourier-root-momentum.mjs','78718-tail-fourier-root-tight-momentum.mjs','closing_weighted_tail.mjs','closing_recalibrated_tail.mjs','950f-tail-subdivision.mjs'].map(f=>[f,sha(fs.readFileSync(path.join(here,f)))])),
 endpointMapping:'x=0 uses checkpoint node stage+1; x=1 uses node stage with pi multiplied by stage.portRatio.',
 endpoints,actualODECalls:0,actualDNCalls:0,actualBVPCalls:0,seconds:(Date.now()-started)/1000};
fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({out:path.resolve(opt.out),bytes:fs.statSync(opt.out).size,
 endpoints:endpoints.map(v=>({node:v.node,x:v.x,normalRelative:v.normal.relativeResidual,tightRelative:v.tight.relativeResidual??null,
  meanChange:v.tightChange?.meanPhysicalChange??null,condition:v.normal.gram.condition2Approx})),seconds:report.seconds}));
