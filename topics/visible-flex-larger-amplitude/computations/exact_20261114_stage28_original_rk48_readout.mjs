// Read six existing RK48 trajectory points in one original shooting stage.
// The accepted states, integrator, 48-step-plus-cusp grid, full H and metric
// are unchanged.  This is a local readout, not a shooting solve or new tail.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {gunzipSync, gzipSync} from 'node:zlib';
import {pathToFileURL, fileURLToPath} from 'node:url';

if(process.env.GITHUB_ACTIONS!=='true'||process.env.GITHUB_REPOSITORY!=='Rogerhu12/math-research-public')
  throw Error('Numerical execution belongs to this public repository Actions');
const opt={};
for(let i=2;i<process.argv.length;i+=2)opt[process.argv[i]]=process.argv[i+1];
for(const key of ['--repo-root','--source-topic','--config','--response','--ledger','--stored','--packet','--anchor','--out-dir'])
  if(!opt[key])throw Error('Missing '+key);
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const read=p=>{const b=fs.readFileSync(p);return JSON.parse((b[0]===31&&b[1]===139?gunzipSync(b):b).toString());};
const write=(p,v)=>fs.writeFileSync(p,JSON.stringify(v)+'\n',{flag:'wx'});
const equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const repo=path.resolve(opt['--repo-root']),source=path.resolve(opt['--source-topic']);
const comp=path.join(repo,'topics/visible-flex-larger-amplitude/computations');
const packet=path.resolve(opt['--packet']),anchorDir=path.resolve(opt['--anchor']);
const packetManifest=read(path.join(packet,'manifest.json')),anchorManifest=read(path.join(anchorDir,'manifest.json'));
if(packetManifest.schema!=='original-GW-cusp-input-byte-extraction-v1'||anchorManifest.schema!=='original-stage28-RK48-anchor-metadata-v1')
  throw Error('Unexpected byte-extraction packet');
const inputHashes={};
for(const key of ['config','response','ledger','stored']){
  const filename=path.resolve(opt['--'+key]),digest=sha(fs.readFileSync(filename));
  if(digest!==anchorManifest.public_assets[key].sha256)throw Error('Changed original public '+key);
  inputHashes[filename]=digest;
}
for(const [name,record]of Object.entries(anchorManifest.files)){
  const filename=path.join(anchorDir,name),bytes=fs.readFileSync(filename);
  if(bytes.length!==record.bytes||sha(bytes)!==record.sha256)throw Error('Changed verbatim anchor '+name);
  inputHashes[filename]=record.sha256;
}
for(const table of ['row_files','node_files'])for(const [name,record]of Object.entries(packetManifest[table])){
  const filename=path.join(packet,name),bytes=fs.readFileSync(filename);
  if(bytes.length!==record.bytes||sha(bytes)!==record.sha256)throw Error('Changed original point packet '+name);
  inputHashes[filename]=record.sha256;
}
for(const directory of [packet,anchorDir])inputHashes[path.join(directory,'manifest.json')]=sha(fs.readFileSync(path.join(directory,'manifest.json')));
const config=read(opt['--config']),record=read(opt['--response']),response=record.response??record;
const anchor=read(path.join(anchorDir,'stage28-inner-anchor.json'));
if(!response.converged||!(response.residual<config.solveTolerance)||!response.audit||!response.heightJetJacobian)
  throw Error('The original full accepted RK48 response is required');
if(config.steps!==48||config.auditSteps!==48||config.modes!==32||config.quadrature!==512||anchor.originalStage!==28||anchor.x!==0)
  throw Error('This local diagnostic is explicitly the original M32/N512 stage28 RK48');
const out=path.resolve(opt['--out-dir']);fs.mkdirSync(out,{recursive:false});
fs.mkdirSync(path.join(out,'nodes'));
Object.assign(process.env,{
  VISIBLE_FLEX_SOURCE_TOPIC:source,VISIBLE_FLEX_SOURCE_ROOT:path.join(source,'repro/source-root'),
  VISIBLE_FLEX_FROZEN_LEDGER_READY:path.resolve(opt['--ledger']),VISIBLE_FLEX_FROZEN_STORED_READY:path.resolve(opt['--stored']),
  VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT:'8',
  CLOSING_TAIL_CACHE:path.join(source,'repro/source-root/topics/large-amplitude-twist-flex/scripts')
});
const scripts=process.env.CLOSING_TAIL_CACHE;
const sourcePaths=[fileURLToPath(import.meta.url),path.join(comp,'tail_frozen_geometry.mjs'),
  path.join(comp,'strong_frozen_calibration_factory.mjs'),path.join(comp,'closure_bounded_point_cache.mjs'),
  path.join(source,'scripts/950f-tail-subdivision.mjs'),path.join(source,'scripts/78718-tail-fourier-root-split-engine.mjs'),
  path.join(scripts,'f6tail_cusp_grid.mjs'),path.join(scripts,'f6tail_momentum_physical_jets.mjs'),
  path.join(scripts,'f6tail_relative_development.mjs')];
const sourceHashes=Object.fromEntries(sourcePaths.map(p=>[p,sha(fs.readFileSync(p))]));
write(path.join(out,'intent.json'),{schema:'stage28-original-RK48-local-readout-intent-v1',
  argv:process.argv.slice(2),started_utc:new Date().toISOString(),input_sha256:inputHashes,
  source_sha256_at_start:sourceHashes,source_repository:process.env.GITHUB_REPOSITORY,source_commit:process.env.GITHUB_SHA,
  original_integration_grid_required:true,no_shooting_solve:true,complete_tail_readout:false});
const start=performance.now();
const {createStoredPhysical}=await import(pathToFileURL(path.join(comp,'tail_frozen_geometry.mjs')));
const {subdividePhysical}=await import(pathToFileURL(path.join(source,'scripts/950f-tail-subdivision.mjs')));
const {createFourierRootSplitFluxEngine}=await import(pathToFileURL(path.join(source,'scripts/78718-tail-fourier-root-split-engine.mjs')));
const {integrationGrid}=await import(pathToFileURL(path.join(scripts,'f6tail_cusp_grid.mjs')));
const {createMomentumPhysicalJetEvaluator}=await import(pathToFileURL(path.join(scripts,'f6tail_momentum_physical_jets.mjs')));
const {relativeActualDevelopment}=await import(pathToFileURL(path.join(scripts,'f6tail_relative_development.mjs')));
const {physical,manifest}=await createStoredPhysical(config);
const stages=subdividePhysical(physical,config.depth,config.shootingParts),states=response.checkpoint.states;
const M=config.modes,K=2*M,N=config.quadrature,si=28,c=stages.cells[si],p=c.profiles[0];
if(stages.cells.length+1!==states.length||states.some(y=>y.length!==K)||!equal(stages.rawNode,response.checkpoint.rawNode))
  throw Error('Original physical stage layout changed');
if(c.profiles.length!==1||c.rawCell!==anchor.rawCell||c.rawSegment!==anchor.rawSegment||
   manifest.profileFingerprintBefore!==anchorManifest.original_profile_fingerprint||
   manifest.profileFingerprintAfter!==anchorManifest.original_profile_fingerprint||
   manifest.profileFingerprintAfter!==packetManifest.original_profile_fingerprint)
  throw Error('Original calibrated source geometry changed');
const originalRows=new Map();
for(const label of ['coarse','fine'])for(const entry of packetManifest.layers[label].rows){
  const row=read(path.join(packet,entry.row_file));
  if(row.originalStage!==si)throw Error('Unexpected original stage');
  const previous=originalRows.get(row.x);
  if(previous&&(previous.rawSha256!==row.rawSha256||previous.meanPerturbationInnerAnchor!==row.meanPerturbationInnerAnchor))
    throw Error('The shared original cusp is not the same saved point');
  originalRows.set(row.x,row);
}
const cusp=Math.max(...originalRows.keys()),requested=[42/48,43/48,44/48,45/48,46/48,cusp];
if(originalRows.size!==3||!originalRows.has(42/48)||!originalRows.has(45/48)||cusp!==.9769532415364806)
  throw Error('Unexpected legacy A/B/C local window');
const grid=integrationGrid(config.steps,p.integrationBreakpoints??[]);
if(requested.some(x=>!grid.includes(x)))throw Error('A requested readout would change the original integration grid');
const engine=createFourierRootSplitFluxEngine({modes:M,spacing:config.spacing,quadrature:N,mu:c.mu,
  orientation:config.orientation,projectionFloor:config.projectionFloor,cuspAwareFlow:config.cuspAwareFlow});
const evaluate=createMomentumPhysicalJetEvaluator(engine,{spacing:config.spacing});
let y=new Float64Array(K+2);y.set(states[si+1]);
const snapshots=new Map();
// No readout-dependent subdivisions, additional RK steps or numerical solves.
for(let k=0;k<grid.length-1;k++){
  y=engine.rk4(y,p,grid[k],grid[k+1]-grid[k]);
  if(requested.includes(grid[k+1]))snapshots.set(grid[k+1],Float64Array.from(y));
}
if(snapshots.size!==requested.length)throw Error('Missing original trajectory snapshot');
let canonicalEndpointDifference=0;
for(let j=0;j<K;j++)canonicalEndpointDifference=Math.max(canonicalEndpointDifference,Math.abs(y[j]/(j>=M?c.portRatio:1)-states[si][j]));
function geometry(x){
  const q=p(x),w=Math.exp(q.logw),w2=Math.exp(2*q.logw);
  return {x,r:q.r,w,w2,E:1+w2,wr:w*q.dlogwdx/q.drdx,drdx:q.drdx,dlogwdx:q.dlogwdx};
}
const rows=[],identity=[];
for(const x of requested){
  const snapshot=snapshots.get(x),point=new Float64Array(K+2);point.set(snapshot.slice(0,K));
  const root=engine.root(point,p,x),jets=evaluate(point,p,x),g=root.g;
  const d=relativeActualDevelopment(g,root.e.rows,jets.perAngle);
  if(!(g.r>0&&g.w>0&&g.drdx>0&&jets.minA>0&&jets.minD>0)||jets.perAngle.length!==N)
    throw Error('Invalid original point domain');
  const raw=Buffer.alloc(N*12*8);
  for(let j=0;j<N;j++){
    const v=jets.perAngle[j],values=[d.dx[j],d.dy[j],v.height,d.dxR[j],d.dyR[j],v.ur,d.dxT[j],d.dyT[j],v.ut,v.urr,v.urt,v.utt];
    for(let q=0;q<12;q++){if(!Number.isFinite(values[q]))throw Error('Nonfinite original point jet');raw.writeDoubleLE(values[q],8*(12*j+q));}
  }
  const file='nodes/original-rk48-stage28-point-'+String(rows.length).padStart(2,'0')+'.f64le.gz';
  const compressed=gzipSync(raw,{level:6});fs.writeFileSync(path.join(out,file),compressed,{flag:'wx'});
  const row={node:rows.length,originalStage:si,rawCell:c.rawCell,rawSegment:c.rawSegment,x,nodePiMultiplier:1,
    file,shape:[N,12],sha256:sha(compressed),rawSha256:sha(raw),geometry:geometry(x),
    meanPerturbationInnerAnchor:anchor.meanPerturbationInnerAnchor+snapshot[K],
    source:'Existing original RK48 trajectory point, evaluated without changing any RK step',
    original_RK_grid_index:grid.indexOf(x),sampleMetricRelativeOperatorError:d.actualMetricRelativeOperatorError,
    formalHeightCurvature:jets.formalHeightCurvature,minimumLeading:jets.minA,minimumD:jets.minD};
  rows.push(row);
  if(originalRows.has(x)){
    const old=originalRows.get(x),keys=['r','w','w2','E','drdx','dlogwdx'];
    identity.push({x,original_node:old.node,old_raw_sha256:old.rawSha256,new_raw_sha256:row.rawSha256,
      raw_bytes_equal:old.rawSha256===row.rawSha256,
      small_mean_exactly_equal:old.meanPerturbationInnerAnchor===row.meanPerturbationInnerAnchor,
      old_small_mean:old.meanPerturbationInnerAnchor,new_small_mean:row.meanPerturbationInnerAnchor,
      geometry_exactly_equal:keys.every(k=>old.geometry[k]===row.geometry[k]),
      geometry_differences:Object.fromEntries(keys.map(k=>[k,row.geometry[k]-old.geometry[k]]))});
  }
}
const identityPassed=identity.length===3&&identity.every(r=>r.raw_bytes_equal&&r.small_mean_exactly_equal&&r.geometry_exactly_equal);
write(path.join(out,'legacy-point-replay-identity.json'),{passed:identityPassed,points:identity,
  interpretation:'Strict original A/B/C raw bytes, mean and geometry check; compression bytes may differ across runtime versions.'});
if(!identityPassed)throw Error('Local replay did not reproduce all three original point data exactly; no refinement comparison authorized');
rows.reverse();for(let i=0;i<rows.length;i++)rows[i].node=i;
write(path.join(out,'complete-local.json'),{schema:'stage28-six-existing-RK48-points-local-view-v1',finished:true,
  angular:N,rows,original_profile_fingerprint:manifest.profileFingerprintAfter,
  refinement_binding:anchorManifest.original_refinement_binding,complete_tail:false,
  scope:'Only stage28 x in [42/48, original cusp]. Three original nodes reproduced exactly and three additional existing RK48 nodes retained.'});
// Retain every old common-stage 450/451 sample and add 17 source samples per
// new local span. These evaluations do not alter the trajectory or its grid.
const sampleMap=new Map();
function retain(q,origin){
  const key=q.r.toString();
  if(!sampleMap.has(key))sampleMap.set(key,{...q,origins:[]});
  sampleMap.get(key).origins.push(origin);
}
const oldBackground=[read(path.join(packet,packetManifest.background_row_file)),
  read(path.join(anchorDir,'original-background-stage-00451.json'))];
for(const bg of oldBackground){
  if(bg.originalStage!==si)throw Error('Changed original background stage');
  for(const q of bg.points){
    const actualX=bg.sourceProfileLeft+(bg.sourceProfileRight-bg.sourceProfileLeft)*q.x;
    retain({...q,source_profile_x:actualX},{kind:'original-common-grid',common_stage:bg.stage,x:q.x});
  }
}
for(let span=0;span<requested.length-1;span++)for(let j=0;j<=16;j++){
  const x=requested[span]+(requested[span+1]-requested[span])*j/16;
  retain({...geometry(x),source_profile_x:x},{kind:'local-existing-grid-subspan',span,x:j/16});
}
const samples=Array.from(sampleMap.values()).sort((a,b)=>a.r-b.r);
write(path.join(out,'background-local.json'),{schema:'stage28-original-background-common-local-samples-v1',
  original_profile_fingerprint:manifest.profileFingerprintAfter,points:samples,
  scope:'Original source background values only; every old stage450/451 sample retained.'});
const result={finished:true,stage:si,originalStages:stages.cells.length,M,N,steps:config.steps,
  original_integration_grid:grid,unchanged_RK_calls:grid.length-1,requested_source_x:requested,
  canonicalEndpointDifference,legacy_point_identity_passed:identityPassed,
  source_sha256_at_start:sourceHashes,input_sha256:inputHashes,original_profile_fingerprint:manifest.profileFingerprintAfter,
  seconds:(performance.now()-start)/1000,complete_tail:false,new_shooting_solve:false,
  original_scalar_metric_changed:false,complete_task:false};
write(path.join(out,'result.json'),result);
console.log(JSON.stringify({event:'stage28-original-RK48-local-readout-complete',...result}));
