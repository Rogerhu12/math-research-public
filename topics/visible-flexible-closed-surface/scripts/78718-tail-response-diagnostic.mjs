// Floating diagnosis of an actual saved response at its own Fourier order.
// No shooting solve or higher-order padding.  The caller determines whether
// this response is the final original-H target; the request identity is saved.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';

const args=process.argv.slice(2),opt={};
if(args.includes('--help')){
 console.log('node scripts/78718-tail-response-diagnostic.mjs --packet ACTUAL.json.gz --out NEW.json [--cell 0] [--source-root PATH]');
 process.exit(0);
}
for(let k=0;k<args.length;k+=2){
 if(!args[k].startsWith('--')||args[k+1]===undefined)throw Error('key/value arguments required');
 opt[args[k].slice(2)]=args[k+1];
}
if(!opt.packet||!opt.out)throw Error('--packet and --out required');
const out=path.resolve(opt.out),peakFile=out.replace(/\.json$/,'')+'-peak-metric.json.gz';
if(fs.existsSync(out)||fs.existsSync(peakFile))throw Error('fresh output paths required');
const here=path.dirname(fileURLToPath(import.meta.url));
const sourceRoot=path.resolve(opt['source-root']??process.env.VISIBLE_FLEX_SOURCE_ROOT??path.join(here,'../repro/source-root'));
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const src=name=>pathToFileURL(path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts',name));
const {createRecalibrationFactory}=await import('./closing_weighted_tail.mjs');
const {subdividePhysical}=await import('./950f-tail-subdivision.mjs');
const {createFourierRootSplitFluxEngine}=await import('./78718-tail-fourier-root-split-engine.mjs');
const {createMomentumPhysicalJetEvaluator}=await import(src('f6tail_momentum_physical_jets.mjs'));
const {actualMetricFromDarbouxJets}=await import(src('f6tail_actual_metric.mjs'));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const started=Date.now(),bytes=fs.readFileSync(opt.packet);
const packet=JSON.parse(bytes[0]===31&&bytes[1]===139?zlib.gunzipSync(bytes):bytes);
const cfg=packet.config,cp=packet.response?.checkpoint;
if(!cfg||!cp||packet.response.converged!==true)throw Error('a converged saved response with config and checkpoint is required');
const M=cfg.modes,N=cfg.quadrature,K=2*M,steps=Number(opt.steps??cfg.steps),rawCell=Number(opt.cell??0);
if(!Number.isInteger(steps)||steps<1)throw Error('positive integer steps required');
const physical=createRecalibrationFactory(cfg).assemble();
const stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts);
if(cp.states.length!==stages.cells.length+1||cp.states.some(v=>v.length!==K))throw Error('checkpoint stage dimensions do not match its config');
const cache=new Map();
function evaluator(c,n){
 const key=[c.rawCell,n].join(':');if(cache.has(key))return cache.get(key);
 const engine=createFourierRootSplitFluxEngine({modes:M,spacing:cfg.spacing,quadrature:n,mu:c.mu,
  orientation:cfg.orientation,projectionFloor:cfg.projectionFloor??.05,cuspAwareFlow:cfg.cuspAwareFlow===true});
 const result={engine,jets:createMomentumPhysicalJetEvaluator(engine,{spacing:cfg.spacing})};
 cache.set(key,result);return result;
}
function evaluate(stage,x,y,n=N,coordinates=false){
 const c=stages.cells[stage],profile=c.profiles[0],{engine,jets}=evaluator(c,n);
 const g=engine.geometry(profile,x),j=jets(y,profile,x);
 const metric=actualMetricFromDarbouxJets(g,j.perAngle,{returnCoordinates:coordinates});
 return {g,j,metric,row:{stage,rawCell:c.rawCell,rawSegment:c.rawSegment,part:c.part,x,r:g.r,
  modes:M,quadrature:n,metric:metric.actualMetricRelativeOperatorError,
  rr:metric.actualMetricRelativeRR,rt:metric.actualMetricRelativeRT,tt:metric.actualMetricRelativeTT,
  radialCurlCorrection:metric.maximumRadialCurlCorrection,darboux:j.maxDarboux,
  rootRelativeResidual:j.rootRelativeResidual}};
}
function gram(g,fr,ft){
 const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
 return [dot(fr,fr)/g.E-1,dot(fr,ft)/(g.r*Math.sqrt(g.E)),dot(ft,ft)/(g.r*g.r)-1];
}
const perStage=[];let worst=null,worstState=null;
for(let stage=0;stage<stages.cells.length;stage++){
 const c=stages.cells[stage];if(c.rawCell!==rawCell)continue;
 const {engine}=evaluator(c,N),profile=c.profiles[0];
 let y=new Float64Array(K+2),best=null;y.set(cp.states[stage+1]);
 for(let k=0;k<=steps;k++){
  const v=evaluate(stage,k/steps,y);
  if(!best||v.row.metric>best.metric)best=v.row;
  if(!worst||v.row.metric>worst.metric){worst=v.row;worstState=Float64Array.from(y);}
  if(k<steps)y=engine.rk4(y,profile,k/steps,1/steps);
 }
 perStage.push(best);
 if(perStage.length%12===0)console.log(JSON.stringify({phase:'own-mode-cell-scan',stages:perStage.length,maximum:worst.metric,seconds:(Date.now()-started)/1000}));
}
if(!worst)throw Error('no selected stages');
const coarse=evaluate(worst.stage,worst.x,worstState,N,true);
const fine=evaluate(worst.stage,worst.x,worstState,2*N,true);
let sharedJetGap=0,sharedRadialGap=0,sharedGramGap=0;
for(let j=0;j<N;j++){
 const h=2*j;
 for(const key of ['ur','ut','urr','urt','utt'])sharedJetGap=Math.max(sharedJetGap,Math.abs(fine.j.perAngle[h][key]-coarse.j.perAngle[j][key]));
 for(let a=0;a<3;a++)sharedRadialGap=Math.max(sharedRadialGap,Math.abs(fine.metric.radialDerivatives[h][a]-coarse.metric.radialDerivatives[j][a]));
 const a=gram(coarse.g,coarse.metric.radialDerivatives[j],coarse.metric.angularDerivatives[j]);
 const b=gram(fine.g,fine.metric.radialDerivatives[h],fine.metric.angularDerivatives[h]);
 for(let k=0;k<3;k++)sharedGramGap=Math.max(sharedGramGap,Math.abs(a[k]-b[k]));
}
const omega=fine.j.perAngle.map(v=>{
 const S=fine.g.r**2-v.ut**2,delta=fine.g.E*S-fine.g.r**2*v.ur**2;
 if(!(delta>0))throw Error('nonpositive spatial determinant at peak');
 return v.darboux*fine.g.E**2*fine.g.r**4/(delta*Math.sqrt(delta));
});
const cutoff=cfg.spacing*M,maxFrequency=Math.min(N-1,Math.max(180,3*cutoff)),spectrum=[];
for(let f=0;f<=maxFrequency;f++){
 let c=0,s=0;for(let j=0;j<omega.length;j++){
  const theta=2*Math.PI*f*j/omega.length;c+=omega[j]*Math.cos(theta)/omega.length;s+=omega[j]*Math.sin(theta)/omega.length;
 }
 spectrum.push({frequency:f,amplitude:Math.hypot(c,s)*(f?2:1)});
}
const sorted=[...spectrum].sort((a,b)=>b.amplitude-a.amplitude);
const peak={scope:'Floating normalized source metric at common physical radius and equally spaced angles; data for representation comparison, not an interval certificate.',
 packet_sha256:sha(bytes),stage:worst.stage,x:worst.x,geometry:{r:fine.g.r,w:fine.g.w,E:fine.g.E},
 angularNodes:2*N,nativeAngularNodes:N,
 source_metric: fine.metric.radialDerivatives.map((v,j)=>gram(fine.g,v,fine.metric.angularDerivatives[j])),
 source_metric_native:coarse.metric.radialDerivatives.map((v,j)=>gram(coarse.g,v,coarse.metric.angularDerivatives[j]))};
const peakBytes=zlib.gzipSync(Buffer.from(JSON.stringify(peak)+'\n'),{level:9});
if(peakBytes.length>=5_000_000)throw Error('peak data exceeds file-size limit');
fs.writeFileSync(peakFile,peakBytes);
const height=packet.request?.height;
const report={scope:'Floating diagnosis of one actual saved converged response at its own Fourier order; selected physical cell and one refined peak. Caller must separately establish that this is the final original-H request. No whole-domain or closed-surface certificate.',
 packet:{path:path.resolve(opt.packet),bytes:bytes.length,sha256:sha(bytes)},
 request:{heightCount:Array.isArray(height)?height.length:null,heightJSONSHA256:Array.isArray(height)?sha(JSON.stringify(height)):null,
  heightLInfinity:Array.isArray(height)?Math.max(...height.map(Math.abs)):null},
 program:{path:fileURLToPath(import.meta.url),sha256:sha(fs.readFileSync(fileURLToPath(import.meta.url)))},
 sourceRoot,source_sha256:Object.fromEntries([
  ...['closing_weighted_tail.mjs','closing_recalibrated_tail.mjs','950f-tail-subdivision.mjs',
   '78718-tail-fourier-root-split-engine.mjs','78718-tail-fourier-root-momentum.mjs',
   '78718-tail-fourier-product-flow.mjs','78718-tail-fourier-product-jacobian.mjs'].map(f=>path.join(here,f)),
  ...['f6tail_momentum_physical_jets.mjs','f6tail_actual_metric.mjs','f6tail_momentum_split_flux.mjs','f6tail_cusp_grid.mjs'].map(f=>path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts',f))
 ].map(f=>[f,sha(fs.readFileSync(f))])),
 savedResidual:packet.response.residual,modes:M,quadrature:N,physicalDepth:cfg.depth,shootingParts:cfg.shootingParts,
 rawCell,steps,points:perStage.length*(steps+1),worst,perStage,
 peakAngularComparison:{coarse:coarse.row,refined:fine.row,sharedJetGap,sharedRadialGap,sharedGramGap},
 omegaRetainedMaximum:Math.max(...spectrum.filter(v=>v.frequency<=cutoff).map(v=>v.amplitude)),
 omegaOmittedMaximum:Math.max(...spectrum.filter(v=>v.frequency>cutoff).map(v=>v.amplitude)),
 omegaSpectrumLargest:sorted.slice(0,12),omegaFrequencyCutoff:cutoff,omegaMaximumFrequencyChecked:maxFrequency,
 peakMetricData:{path:peakFile,bytes:peakBytes.length,sha256:sha(peakBytes)},
 actualShootingSolves:0,actualBVPCalls:0,higherModePaddingPerformed:false,
 elapsedSeconds:(Date.now()-started)/1000};
const reportBytes=Buffer.from(JSON.stringify(report,null,2)+'\n');
if(reportBytes.length>=5_000_000)throw Error('diagnostic report exceeds file-size limit');
fs.writeFileSync(out,reportBytes);
console.log(JSON.stringify({output:out,bytes:fs.statSync(out).size,peakDataBytes:peakBytes.length,
 metric:worst.metric,stage:worst.stage,x:worst.x,seconds:report.elapsedSeconds}));
