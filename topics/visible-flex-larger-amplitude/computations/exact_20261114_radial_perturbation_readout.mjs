// Actual RK interior states of accepted A on unchanged g and fixed H.
// This refines a C2 reconstruction; it does not resolve a different BVP.
// The background h0'=w is retained separately. The engine's small mean
// coordinate (index 2M) is accumulated directly, without subtracting two
// large integrated heights. Original endpoint nonmean jets are retained.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {gunzipSync,gzipSync} from 'node:zlib';
import {pathToFileURL} from 'node:url';

const opt={};for(let i=2;i<process.argv.length;i+=2)opt[process.argv[i]]=process.argv[i+1];
for(const k of ['--repo-root','--source-topic','--complete','--out-dir'])if(!opt[k])throw Error('Missing '+k);
const repo=path.resolve(opt['--repo-root']),source=path.resolve(opt['--source-topic']);
const topic=path.join(repo,'topics/visible-flex-larger-amplitude'),comp=path.join(topic,'computations'),notes=path.join(topic,'notes');
const outDir=path.resolve(opt['--out-dir']);fs.mkdirSync(outDir,{recursive:false});
const nodeDir=path.join(outDir,'nodes');fs.mkdirSync(nodeDir);
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>{const b=fs.readFileSync(p);return JSON.parse((b[0]===31&&b[1]===139?gunzipSync(b):b).toString());};
const write=(p,v)=>fs.writeFileSync(p,JSON.stringify(v)+'\n',{flag:'wx'});
const start=performance.now(),factor=4,steps=Number(opt['--steps']??12),levels=[1,2,4];
if(!Number.isInteger(steps)||steps<12||steps%factor)throw Error('Steps must be a multiple of 4 at least 12');
const configPath=path.join(notes,'2026-11-13-strong-q126-m32-tail2-actual-r1-config.json');
const tailPath=path.join(notes,'2026-11-13-strong-q126-m32-tail2-actual-r1-tail-response_0003.json.gz');
const oldCompletePath=path.resolve(opt['--complete']),oldComplete=read(oldCompletePath);
const config=read(configPath),packet=read(tailPath),states=packet.response.checkpoint.states;
if(sha(fs.readFileSync(configPath))!=='3b0deaaf0cdc65a34a8e4652e0a04d96a840db354ccada71d9cba5e4cd228e23'||
   sha(fs.readFileSync(tailPath))!=='018d19c6ca8c27acc5cc1dde6d396ee783e34ae25e5b525158c5bb37086520d9')throw Error('Original A inputs changed');
if(!packet.response.converged||oldComplete.completedNodes!==577||states.length!==577)throw Error('Expected complete accepted A');
const ledger=path.join(notes,'2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json');
const stored=path.join(notes,'2026-11-13-strong-m28-recovered-full-audit-r1-ready.json');
Object.assign(process.env,{
  VISIBLE_FLEX_SOURCE_TOPIC:source,VISIBLE_FLEX_SOURCE_ROOT:path.join(source,'repro/source-root'),
  VISIBLE_FLEX_FROZEN_LEDGER_READY:ledger,VISIBLE_FLEX_FROZEN_STORED_READY:stored,
  VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT:'8',
  CLOSING_TAIL_CACHE:path.join(source,'repro/source-root/topics/large-amplitude-twist-flex/scripts')
});
const {createStoredPhysical}=await import(pathToFileURL(path.join(comp,'tail_frozen_geometry.mjs')).href);
const {subdividePhysical}=await import(pathToFileURL(path.join(source,'scripts/950f-tail-subdivision.mjs')).href);
const {createFourierRootSplitFluxEngine}=await import(pathToFileURL(path.join(source,'scripts/78718-tail-fourier-root-split-engine.mjs')).href);
const base=process.env.CLOSING_TAIL_CACHE;
const {integrationGrid}=await import(pathToFileURL(path.join(base,'f6tail_cusp_grid.mjs')).href);
const {createMomentumPhysicalJetEvaluator}=await import(pathToFileURL(path.join(base,'f6tail_momentum_physical_jets.mjs')).href);
const {relativeActualDevelopment}=await import(pathToFileURL(path.join(base,'f6tail_relative_development.mjs')).href);
const {physical,factory,manifest}=await createStoredPhysical(config),alpha=physical.stats.alpha;
const stages=subdividePhysical(physical,8,8),M=config.modes,K=2*M,N=config.quadrature;
const rows=Array(factor*576+1),partialMean=new Float64Array(rows.length),meanIncrements=new Float64Array(576),bgRKIncrements=new Float64Array(576);
const diagnostics={maximumEndpointCanonicalDifference:0,maximumEndpointRowRelativeDifference:0,
  maximumSampleMetric:0,maximumFormalCurvature:0,minimumLeading:Infinity,minimumD:Infinity};
const geom=(p,x)=>{const q=p(x),w=Math.exp(q.logw),w2=Math.exp(2*q.logw);return{x,r:q.r,w,w2,E:1+w2,wr:w*q.dlogwdx/q.drdx,drdx:q.drdx,dlogwdx:q.dlogwdx};};
function copyOriginal(i){
  const row=oldComplete.rows[i],file='node-'+String(i*factor).padStart(5,'0')+'.f64le.gz';
  const b=fs.readFileSync(path.join(path.dirname(oldCompletePath),row.file));
  if(sha(b)!==row.sha256)throw Error('Changed original node');
  fs.writeFileSync(path.join(nodeDir,file),b,{flag:'wx'});
  rows[i*factor]={...row,node:i*factor,originalNode:i,file,source:'original accepted node nonmean jets'};
}
for(let i=0;i<=576;i++)copyOriginal(i);
let engine=null,ev=null,rawCell=null,rootCalls=0,rkCalls=0;
for(let si=0;si<576;si++){
  const c=stages.cells[si],p=c.profiles[0];
  if(rawCell!==c.rawCell){
    engine=createFourierRootSplitFluxEngine({modes:M,spacing:config.spacing,quadrature:N,mu:c.mu,orientation:config.orientation,projectionFloor:config.projectionFloor,cuspAwareFlow:config.cuspAwareFlow});
    ev=createMomentumPhysicalJetEvaluator(engine,{spacing:config.spacing});rawCell=c.rawCell;
  }
  let y=new Float64Array(K+2);y.set(states[si+1]);
  const cuts=p.integrationBreakpoints??[],grid=cuts.length?integrationGrid(steps,cuts):null,count=grid?grid.length-1:steps,h0=1/steps;
  const got=new Set();
  for(let k=0;k<count;k++){
    const x=grid?grid[k]:k*h0,h=grid?grid[k+1]-grid[k]:h0;
    y=engine.rk4(y,p,x,h);rkCalls++;
    const end=x+h,j=Math.round(end*factor);
    if(j>0&&j<factor&&Math.abs(end-j/factor)<1e-13){
      if(got.has(j))throw Error('Duplicated refined node');got.add(j);
      const pointState=Float64Array.from(y);pointState[K]=pointState[K+1]=0;
      const rt=engine.root(pointState,p,j/factor),jets=ev(pointState,p,j/factor),g=rt.g;
      rootCalls+=2;const d=relativeActualDevelopment(g,rt.e.rows,jets.perAngle);
      const node=si*factor+factor-j,file='node-'+String(node).padStart(5,'0')+'.f64le.gz';
      const raw=Buffer.alloc(N*12*8);
      for(let a=0;a<N;a++){
        const v=jets.perAngle[a],values=[d.dx[a],d.dy[a],v.height,d.dxR[a],d.dyR[a],v.ur,d.dxT[a],d.dyT[a],v.ut,v.urr,v.urt,v.utt];
        for(let q=0;q<12;q++){if(!Number.isFinite(values[q]))throw Error('Nonfinite jet');raw.writeDoubleLE(values[q],(12*a+q)*8);}
      }
      const compressed=gzipSync(raw,{level:6});fs.writeFileSync(path.join(nodeDir,file),compressed,{flag:'wx'});
      rows[node]={node,originalStage:si,x:j/factor,file,shape:[N,12],sha256:sha(compressed),rawSha256:sha(raw),
        geometry:geom(p,j/factor),meanHeightInnerAnchor:null,meanPerturbationInnerAnchor:null,
        source:'actual original RK stage interior, fixed accepted inner state',
        sampleMetricRelativeOperatorError:d.actualMetricRelativeOperatorError,formalHeightCurvature:jets.formalHeightCurvature};
      partialMean[node]=y[K];
      diagnostics.maximumSampleMetric=Math.max(diagnostics.maximumSampleMetric,d.actualMetricRelativeOperatorError);
      diagnostics.maximumFormalCurvature=Math.max(diagnostics.maximumFormalCurvature,jets.formalHeightCurvature);
      diagnostics.minimumLeading=Math.min(diagnostics.minimumLeading,jets.minA);diagnostics.minimumD=Math.min(diagnostics.minimumD,jets.minD);
    }
  }
  if(got.size!==3)throw Error('Refined RK sample grid incomplete');
  meanIncrements[si]=y[K];bgRKIncrements[si]=y[K+1];
  const old=states[si],scale=Math.max(...old.map(Math.abs),1e-250);let delta=0;
  for(let j=0;j<K;j++)delta=Math.max(delta,Math.abs(y[j]/(j>=M?c.portRatio:1)-old[j]));
  diagnostics.maximumEndpointCanonicalDifference=Math.max(diagnostics.maximumEndpointCanonicalDifference,delta);
  diagnostics.maximumEndpointRowRelativeDifference=Math.max(diagnostics.maximumEndpointRowRelativeDifference,delta/scale);
  if((si+1)%48===0)console.log(JSON.stringify({event:'stages',completed:si+1,seconds:(performance.now()-start)/1000,diagnostics}));
}
const perturbMean=new Float64Array(577);
for(let i=575;i>=0;i--)perturbMean[i]=perturbMean[i+1]+meanIncrements[i];
for(let node=0;node<rows.length;node++){
  const si=Math.floor(node/factor),rem=node%factor;
  rows[node].meanPerturbationInnerAnchor=rem===0?perturbMean[si]:perturbMean[si+1]+partialMean[node];
}
const sourceInputs=Object.fromEntries([configPath,tailPath,oldCompletePath,ledger,stored].map(p=>[p,sha(fs.readFileSync(p))]));
for(const level of levels){
  const bgRows=[],nativeNode=new Float64Array(level*576+1),selected=[];
  for(let si=0;si<576;si++){
    const c=stages.cells[si],p=c.profiles[0],entry=factory.getEntries(c.rawCell,config.valleyControls?.[c.rawCell]??0).entries[c.rawSegment];
    for(let sub=level-1;sub>=0;sub--){
      const pa=sub/level,pb=(sub+1)/level,a=c.rawLeft+(c.rawRight-c.rawLeft)*pa,b=c.rawLeft+(c.rawRight-c.rawLeft)*pb;
      const primitive=entry.integrate(a,b),stage=si*level+(level-1-sub);
      bgRows.push({stage,originalStage:si,subdivision:level,sourceProfileLeft:pa,sourceProfileRight:pb,
        nativeHeightIncrement:primitive[4]+alpha*primitive[5],
        points:Array.from({length:17},(_,j)=>({...geom(p,pa+(pb-pa)*j/16),x:j/16}))});
    }
  }
  for(let i=nativeNode.length-2;i>=0;i--)nativeNode[i]=nativeNode[i+1]+bgRows[i].nativeHeightIncrement;
  for(let i=0;i<nativeNode.length;i++){
    const original=rows[i*factor/level];
    selected.push({...original,node:i,file:path.join('nodes',original.file),
      meanHeightInnerAnchor:nativeNode[i]+original.meanPerturbationInnerAnchor});
  }
  const complete={schema:'accepted-A-RK-interior-Cartesian-refinement-v1',finished:true,completedNodes:selected.length,
    angular:N,refinement:level,steps,rows:selected,source_sha256:sha(fs.readFileSync(new URL(import.meta.url))),
    input_sha256:sourceInputs,original_profile_fingerprint:manifest.profileFingerprintAfter,
    same_original_endpoint_nonmean_jets:true,mean_definition:'Direct engine small mean, summed with one inner anchor; source background primitive added separately.',
    diagnostics,limitations:['Finite RK12/24 readout from fixed accepted shooting states; not a new shooting solution.',
      'New interior states are actual RK evolution, not resampling the old quintic.',
      'Original endpoint mismatch is recorded; common Hermite endpoint jets define a C2 finite field.']};
  write(path.join(outDir,'complete-'+level+'.json'),complete);
  write(path.join(outDir,'background-'+level+'.json'),{schema:'accepted-A-refined-source-background-v1',finished:true,
    original_profile_fingerprint:manifest.profileFingerprintAfter,stages:bgRows.length,samples_per_stage:17,
    nodeHeightInnerAnchor:Array.from(nativeNode),rows:bgRows});
}
const report={schema:'accepted-A-actual-radial-refinement-readout-v1',finished:true,steps,levels,
  originalStages:576,finestNodes:rows.length,originalCompleteSha256:sha(fs.readFileSync(oldCompletePath)),
  source_sha256:sha(fs.readFileSync(new URL(import.meta.url))),input_sha256:sourceInputs,
  original_profile_fingerprint:manifest.profileFingerprintAfter,smallMeanIncrements:Array.from(meanIncrements),
  backgroundRKIncrements:Array.from(bgRKIncrements),perturbationMeanAtCut:perturbMean[0],diagnostics,
  nodeRootCalls:rootCalls,RKCalls:rkCalls,seconds:(performance.now()-start)/1000,
  scope:'Actual ODE interior readout and nested radial C2 reconstruction data at fixed g/H; not a new BVP, infinite solution or closed surface.'};
write(path.join(outDir,'result.json'),report);
console.log(JSON.stringify({event:'complete',outDir,steps,seconds:report.seconds,diagnostics}));
