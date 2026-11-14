// Genuine interior and endpoint readout from a newly converged fixed-H tail.
// Only RK discretization may differ from the accepted baseline. All endpoints
// are newly evaluated from the new shooting states; none are copied from the
// earlier readout. Native source background and small mean stay separate.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {gunzipSync,gzipSync} from 'node:zlib';
import {pathToFileURL,fileURLToPath} from 'node:url';

const opt={};for(let i=2;i<process.argv.length;i+=2)opt[process.argv[i]]=process.argv[i+1];
for(const key of ['--repo-root','--source-topic','--config','--response','--baseline-config','--baseline-response','--out-dir'])if(!opt[key])throw Error('Missing '+key);
const repo=path.resolve(opt['--repo-root']),source=path.resolve(opt['--source-topic']);
const topic=path.join(repo,'topics/visible-flex-larger-amplitude'),comp=path.join(topic,'computations'),notes=path.join(topic,'notes');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>{const b=fs.readFileSync(p);return JSON.parse((b[0]===31&&b[1]===139?gunzipSync(b):b).toString());};
const equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const write=(p,v)=>fs.writeFileSync(p,JSON.stringify(v)+'\n',{flag:'wx'});
const configPath=path.resolve(opt['--config']),responsePath=path.resolve(opt['--response']);
const baselineConfigPath=path.resolve(opt['--baseline-config']),baselineResponsePath=path.resolve(opt['--baseline-response']);
const config=read(configPath),baselineConfig=read(baselineConfigPath),record=read(responsePath),baselineRecord=read(baselineResponsePath);
const response=record.response??record,baseline=baselineRecord.response??baselineRecord;
const ioKeys=new Set(['initialCheckpoint','traceFile','iterationCheckpointFile','trialDiagnosticFile']);
const allowedKeys=new Set([...ioKeys,'steps','auditSteps']);
const project=o=>Object.fromEntries(Object.entries(o).filter(([k])=>!allowedKeys.has(k)).sort(([a],[b])=>a.localeCompare(b)));
if(!equal(project(config),project(baselineConfig)))throw Error('Physical/source parameters differ from baseline');
if(!response.converged||!(response.residual<config.solveTolerance)||!response.audit||!response.heightJetJacobian)throw Error('Converged shooting, full finite audit and DN Jacobian required');
if(!baseline.converged||!equal(response.checkpoint.cutHeight,baseline.checkpoint.cutHeight))throw Error('All fixed Dirichlet heights must agree exactly');
if(!equal(project(response.checkpoint.parameters),project(baseline.checkpoint.parameters)))throw Error('Checkpoint physical parameters differ');
if(response.checkpoint.parameters.steps!==config.steps||response.checkpoint.parameters.auditSteps!==config.auditSteps)throw Error('Response RK steps differ from config');
const levels=(opt['--levels']??'1,2,4,8').split(',').map(Number),factor=Math.max(...levels),steps=config.steps;
if(!levels.length||levels[0]!==1||levels.some((v,i)=>!Number.isInteger(v)||v<1||factor%v||(i&&v<=levels[i-1]))||!Number.isInteger(steps)||steps%factor)throw Error('Nested increasing levels must divide the actual RK step count');
const ledger=path.join(notes,'2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json');
const stored=path.join(notes,'2026-11-13-strong-m28-recovered-full-audit-r1-ready.json');
Object.assign(process.env,{
  VISIBLE_FLEX_SOURCE_TOPIC:source,VISIBLE_FLEX_SOURCE_ROOT:path.join(source,'repro/source-root'),
  VISIBLE_FLEX_FROZEN_LEDGER_READY:ledger,VISIBLE_FLEX_FROZEN_STORED_READY:stored,
  VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT:'8',
  CLOSING_TAIL_CACHE:path.join(source,'repro/source-root/topics/large-amplitude-twist-flex/scripts')
});
const base=process.env.CLOSING_TAIL_CACHE;
const inputPaths=[configPath,responsePath,baselineConfigPath,baselineResponsePath,ledger,stored];
const inputHashes=Object.fromEntries(inputPaths.map(p=>[p,sha(fs.readFileSync(p))]));
const sourcePaths=[fileURLToPath(import.meta.url),path.join(comp,'tail_frozen_geometry.mjs'),
  path.join(source,'scripts/950f-tail-subdivision.mjs'),path.join(source,'scripts/78718-tail-fourier-root-split-engine.mjs'),
  path.join(base,'f6tail_cusp_grid.mjs'),path.join(base,'f6tail_momentum_physical_jets.mjs'),path.join(base,'f6tail_relative_development.mjs')];
const sourceHashes=Object.fromEntries(sourcePaths.map(p=>[p,sha(fs.readFileSync(p))]));
const outDir=path.resolve(opt['--out-dir']);fs.mkdirSync(outDir,{recursive:false});
const nodeDir=path.join(outDir,'nodes');fs.mkdirSync(nodeDir);
write(path.join(outDir,'intent.json'),{schema:'same-H-resolved-tail-readout-intent-v1',started_utc:new Date().toISOString(),
  argv:process.argv.slice(2),source_sha256_at_start:sourceHashes,input_sha256:inputHashes,steps,levels,
  all_physical_parameters_equal:true,all_complete_H_equal:true,accepted_prefix_resolved:false});
const start=performance.now();
const {createStoredPhysical}=await import(pathToFileURL(path.join(comp,'tail_frozen_geometry.mjs')).href);
const {subdividePhysical}=await import(pathToFileURL(path.join(source,'scripts/950f-tail-subdivision.mjs')).href);
const {createFourierRootSplitFluxEngine}=await import(pathToFileURL(path.join(source,'scripts/78718-tail-fourier-root-split-engine.mjs')).href);
const {integrationGrid}=await import(pathToFileURL(path.join(base,'f6tail_cusp_grid.mjs')).href);
const {createMomentumPhysicalJetEvaluator}=await import(pathToFileURL(path.join(base,'f6tail_momentum_physical_jets.mjs')).href);
const {relativeActualDevelopment}=await import(pathToFileURL(path.join(base,'f6tail_relative_development.mjs')).href);
const {physical,factory,manifest}=await createStoredPhysical(config),alpha=physical.stats.alpha;
const stages=subdividePhysical(physical,config.depth,config.shootingParts),S=stages.cells.length;
const M=config.modes,K=2*M,N=config.quadrature,states=response.checkpoint.states;
if(states.length!==S+1||states.some(v=>v.length!==K)||!equal(stages.rawNode,response.checkpoint.rawNode))throw Error('New shooting layout differs from reconstructed physical stages');
if(physical.cells.length!==config.protectCell||manifest.profileFingerprintBefore!==manifest.profileFingerprintAfter)throw Error('Original calibrated background changed');
const rows=Array(factor*S+1),partialMean=new Float64Array(rows.length),meanIncrements=new Float64Array(S),bgRKIncrements=new Float64Array(S);
const diagnostics={maximumEndpointCanonicalDifference:0,maximumEndpointRowRelativeDifference:0,
  maximumSampleMetric:0,maximumFormalCurvature:0,minimumLeading:Infinity,minimumD:Infinity};
const geom=(p,x)=>{const q=p(x),w=Math.exp(q.logw),w2=Math.exp(2*q.logw);return{x,r:q.r,w,w2,E:1+w2,wr:w*q.dlogwdx/q.drdx,drdx:q.drdx,dlogwdx:q.dlogwdx};};
let engine=null,ev=null,rawCell=null,rootCalls=0,rkCalls=0;
function savePoint(node,si,x,input,piMultiplier,kind){
  if(rows[node])throw Error('Duplicate radial node '+node);
  const c=stages.cells[si],p=c.profiles[0],y=new Float64Array(K+2);y.set(input.slice(0,K));
  if(piMultiplier!==1)for(let j=0;j<M;j++)y[M+j]*=piMultiplier;
  const rt=engine.root(y,p,x),jets=ev(y,p,x),g=rt.g;rootCalls+=2;
  const d=relativeActualDevelopment(g,rt.e.rows,jets.perAngle);
  if(!(g.r>0&&g.w>0&&g.drdx>0&&jets.minA>0&&jets.minD>0)||jets.perAngle.length!==N)throw Error('Invalid point domain');
  const raw=Buffer.alloc(N*12*8),file='node-'+String(node).padStart(5,'0')+'.f64le.gz';
  for(let a=0;a<N;a++){
    const v=jets.perAngle[a],values=[d.dx[a],d.dy[a],v.height,d.dxR[a],d.dyR[a],v.ur,d.dxT[a],d.dyT[a],v.ut,v.urr,v.urt,v.utt];
    for(let q=0;q<12;q++){if(!Number.isFinite(values[q]))throw Error('Nonfinite point jet');raw.writeDoubleLE(values[q],(12*a+q)*8);}
  }
  const compressed=gzipSync(raw,{level:6});fs.writeFileSync(path.join(nodeDir,file),compressed,{flag:'wx'});
  rows[node]={node,originalStage:si,rawCell:c.rawCell,rawSegment:c.rawSegment,x,nodePiMultiplier:piMultiplier,
    file,shape:[N,12],sha256:sha(compressed),rawSha256:sha(raw),geometry:geom(p,x),
    meanHeightInnerAnchor:null,meanPerturbationInnerAnchor:null,source:kind,
    sampleMetricRelativeOperatorError:d.actualMetricRelativeOperatorError,formalHeightCurvature:jets.formalHeightCurvature};
  diagnostics.maximumSampleMetric=Math.max(diagnostics.maximumSampleMetric,d.actualMetricRelativeOperatorError);
  diagnostics.maximumFormalCurvature=Math.max(diagnostics.maximumFormalCurvature,jets.formalHeightCurvature);
  diagnostics.minimumLeading=Math.min(diagnostics.minimumLeading,jets.minA);diagnostics.minimumD=Math.min(diagnostics.minimumD,jets.minD);
}
for(let si=0;si<S;si++){
  const c=stages.cells[si],p=c.profiles[0];
  if(c.profiles.length!==1)throw Error('Expected one profile per shooting stage');
  if(rawCell!==c.rawCell){
    engine=createFourierRootSplitFluxEngine({modes:M,spacing:config.spacing,quadrature:N,mu:c.mu,orientation:config.orientation,projectionFloor:config.projectionFloor,cuspAwareFlow:config.cuspAwareFlow});
    ev=createMomentumPhysicalJetEvaluator(engine,{spacing:config.spacing});rawCell=c.rawCell;
  }
  if(si===0)savePoint(0,0,1,states[0],c.portRatio,'new converged shooting outer endpoint');
  savePoint((si+1)*factor,si,0,states[si+1],1,'new converged shooting inner endpoint');
  let y=new Float64Array(K+2);y.set(states[si+1]);
  const cuts=p.integrationBreakpoints??[],grid=cuts.length?integrationGrid(steps,cuts):null,count=grid?grid.length-1:steps,h0=1/steps;
  const got=new Set();
  for(let k=0;k<count;k++){
    const x=grid?grid[k]:k*h0,h=grid?grid[k+1]-grid[k]:h0;
    y=engine.rk4(y,p,x,h);rkCalls++;
    const end=x+h,j=Math.round(end*factor);
    if(j>0&&j<factor&&Math.abs(end-j/factor)<1e-13){
      if(got.has(j))throw Error('Duplicated interior RK point');got.add(j);
      const node=si*factor+factor-j;
      savePoint(node,si,j/factor,y,1,'genuine RK interior from new converged shooting inner state');partialMean[node]=y[K];
    }
  }
  if(got.size!==factor-1)throw Error('Incomplete true RK interior grid');
  meanIncrements[si]=y[K];bgRKIncrements[si]=y[K+1];
  const expected=states[si],scale=Math.max(...expected.map(Math.abs),1e-250);let delta=0;
  for(let j=0;j<K;j++)delta=Math.max(delta,Math.abs(y[j]/(j>=M?c.portRatio:1)-expected[j]));
  diagnostics.maximumEndpointCanonicalDifference=Math.max(diagnostics.maximumEndpointCanonicalDifference,delta);
  diagnostics.maximumEndpointRowRelativeDifference=Math.max(diagnostics.maximumEndpointRowRelativeDifference,delta/scale);
  if((si+1)%48===0){
    const progress={event:'stages',completed:si+1,total:S,seconds:(performance.now()-start)/1000,diagnostics};
    fs.writeFileSync(path.join(outDir,'progress.json'),JSON.stringify(progress)+'\n');console.log(JSON.stringify(progress));
  }
}
if(rows.some(v=>!v))throw Error('Missing regenerated endpoint or interior');
const perturbMean=new Float64Array(S+1);
for(let i=S-1;i>=0;i--)perturbMean[i]=perturbMean[i+1]+meanIncrements[i];
for(let node=0;node<rows.length;node++){
  const si=Math.floor(node/factor),rem=node%factor;
  rows[node].meanPerturbationInnerAnchor=rem===0?perturbMean[si]:perturbMean[si+1]+partialMean[node];
}
const refinementBinding={baseline_config_sha256:inputHashes[baselineConfigPath],baseline_response_sha256:inputHashes[baselineResponsePath],
  config_sha256:inputHashes[configPath],response_sha256:inputHashes[responsePath],all_physical_parameters_equal:true,
  all_complete_H_equal:true,allowed_changed_keys:Array.from(allowedKeys).sort(),baseline_steps:baselineConfig.steps,new_steps:steps,
  actual_newton_converged:true,residual:response.residual,original_tolerance:config.solveTolerance,DN_jacobian_present:true,finite_audit:response.audit,
  original_endpoint_nonmean_jets_reused:false,accepted_prefix_resolved:false};
for(const level of levels){
  const bgRows=[],nativeNode=new Float64Array(level*S+1),selected=[];
  for(let si=0;si<S;si++){
    const c=stages.cells[si],p=c.profiles[0],entry=factory.getEntries(c.rawCell,config.valleyControls?.[c.rawCell]??0).entries[c.rawSegment];
    for(let sub=level-1;sub>=0;sub--){
      const pa=sub/level,pb=(sub+1)/level,a=c.rawLeft+(c.rawRight-c.rawLeft)*pa,b=c.rawLeft+(c.rawRight-c.rawLeft)*pb;
      const primitive=entry.integrate(a,b),stage=si*level+(level-1-sub);
      bgRows.push({stage,originalStage:si,subdivision:level,sourceProfileLeft:pa,sourceProfileRight:pb,
        nativeHeightIncrement:primitive[4]+alpha*primitive[5],points:Array.from({length:17},(_,j)=>({...geom(p,pa+(pb-pa)*j/16),x:j/16}))});
    }
  }
  for(let i=nativeNode.length-2;i>=0;i--)nativeNode[i]=nativeNode[i+1]+bgRows[i].nativeHeightIncrement;
  for(let i=0;i<nativeNode.length;i++){
    const row=rows[i*factor/level];selected.push({...row,node:i,file:path.join('nodes',row.file),meanHeightInnerAnchor:nativeNode[i]+row.meanPerturbationInnerAnchor});
  }
  const complete={schema:'same-H-resolved-tail-Cartesian-radial-readout-v1',finished:true,completedNodes:selected.length,
    angular:N,refinement:level,steps,rows:selected,source_sha256_at_start:sourceHashes,input_sha256:inputHashes,
    original_profile_fingerprint:manifest.profileFingerprintAfter,same_original_endpoint_nonmean_jets:false,refinement_binding:refinementBinding,
    mean_definition:'Direct engine small mean from newly solved states, accumulated from one fixed inner anchor; native source background added separately.',diagnostics,
    limitations:['Finite re-solved shooting solution at the same full H and physical metric; original prefix is not re-solved or accepted again.',
      'All endpoint jets and true RK interior states are newly evaluated; no old endpoint nonmean data are copied.',
      'No interval error enclosure, infinite nonlinear solution, or complete-task assertion.']};
  write(path.join(outDir,'complete-'+level+'.json'),complete);
  write(path.join(outDir,'background-'+level+'.json'),{schema:'accepted-A-refined-source-background-v1',finished:true,
    original_profile_fingerprint:manifest.profileFingerprintAfter,stages:bgRows.length,samples_per_stage:17,nodeHeightInnerAnchor:Array.from(nativeNode),rows:bgRows});
}
const report={schema:'same-H-resolved-tail-actual-radial-readout-v1',finished:true,steps,levels,originalStages:S,finestNodes:rows.length,
  source_sha256_at_start:sourceHashes,input_sha256:inputHashes,original_profile_fingerprint:manifest.profileFingerprintAfter,
  refinement_binding:refinementBinding,smallMeanIncrements:Array.from(meanIncrements),backgroundRKIncrements:Array.from(bgRKIncrements),
  perturbationMeanAtCut:perturbMean[0],diagnostics,nodeRootCalls:rootCalls,RKCalls:rkCalls,seconds:(performance.now()-start)/1000};
write(path.join(outDir,'result.json'),report);
console.log(JSON.stringify({event:'complete',outDir,steps,levels,seconds:report.seconds,diagnostics}));
