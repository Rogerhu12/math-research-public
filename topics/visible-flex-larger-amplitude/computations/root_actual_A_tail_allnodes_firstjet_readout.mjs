// Fresh numerical readout only: all accepted A shooting nodes, no RK/ODE, shooting/BVP Newton, or variational flow.
// Original point-root Newton and its root-Jacobian solves are evaluated.
// Inputs and original source APIs were inspected at c2efbb20c47a84adbc76fdca62b250c178d0d7fe.
// This file has not itself produced a numerical result until an owned run exits 0.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {gunzipSync,gzipSync} from 'node:zlib';
import {pathToFileURL,fileURLToPath} from 'node:url';

const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const args=process.argv.slice(2),opt={};
for(let i=0;i<args.length;i+=2){
  if(!args[i].startsWith('--')||i+1>=args.length||Object.hasOwn(opt,args[i]))throw Error('Distinct explicit arguments required');
  opt[args[i]]=args[i+1];
}
const keys=['--repo-root','--source-topic','--first-node','--last-node-exclusive','--out-dir'];
if(Object.keys(opt).length!==keys.length||keys.some(k=>!Object.hasOwn(opt,k)))throw Error('Required: '+keys.join(' '));
const repo=path.resolve(opt['--repo-root']),sourceTopic=path.resolve(opt['--source-topic']);
const topic=path.join(repo,'topics/visible-flex-larger-amplitude'),comp=path.join(topic,'computations'),notes=path.join(topic,'notes');
const first=Number(opt['--first-node']),last=Number(opt['--last-node-exclusive']);
if(!Number.isInteger(first)||!Number.isInteger(last)||first<0||last>577||first>=last)throw Error('Range must be a nonempty subset of [0,577)');
const outDir=path.resolve(opt['--out-dir']);
if(fs.existsSync(outDir))throw Error('Fresh absent output directory required');
fs.mkdirSync(outDir,{recursive:true});
const start=process.hrtime.bigint(),hashes={},checks=[];
function check(name,value){if(!value)throw Error('Readout gate: '+name);checks.push(name);}
function readBytes(file,want){
  const b=fs.readFileSync(file),got=sha(b);hashes[file]=got;
  if(want)check('SHA '+path.basename(file),got===want);
  return b;
}
function parseBytes(b){return JSON.parse((b[0]===31&&b[1]===139?gunzipSync(b):b).toString('utf8'));}
function read(file,want){return parseBytes(readBytes(file,want));}
function equal(a,b){
  if(typeof a==='number'||typeof b==='number')return Object.is(a,b);
  if(a===b)return true;
  if(!a||!b||typeof a!=='object'||typeof b!=='object'||Array.isArray(a)!==Array.isArray(b))return false;
  const ak=Object.keys(a).sort(),bk=Object.keys(b).sort();
  return ak.length===bk.length&&ak.every((k,j)=>k===bk[j]&&equal(a[k],b[k]));
}
function finite(x,name){if(!Number.isFinite(x))throw Error('Nonfinite '+name);return x;}
function sidecar(dir,name){
  if(typeof name!=='string'||!name||path.basename(name)!==name)throw Error('Expected local sidecar basename');
  return path.join(dir,name);
}
function typed(t){
  if(!Array.isArray(t))throw Error('Malformed original typed identity');
  if(t[0]==='object')return Object.fromEntries(t[1].map(([k,v])=>[k,typed(v)]));
  if(t[0]==='array')return t[1].map(typed);
  if(t[0]==='f64le'){const b=Buffer.from(t[1],'hex');if(b.length!==8)throw Error('Bad Float64 identity');return finite(b.readDoubleLE(0),'typed identity');}
  if(t[0]==='null')return null;
  if(t[0]==='string'||t[0]==='boolean')return t[1];
  throw Error('Unsupported original typed identity');
}
function saveJSON(file,value){fs.writeFileSync(file,JSON.stringify(value,null,2)+'\n',{flag:'wx'});}
const A='2026-11-13-strong-q126-m32-tail2-actual-r1';
const meanName='2026-11-13-strong-q126-saved-actual-tail-mean-r1';
const primaryPath=path.join(notes,A+'.json.gz');
const primary=read(primaryPath,'917d859e8a73fa663db1839e354909ae4f174bad1895f8717c20705cdd702aaf');
const owned=read(path.join(notes,A+'-resource.json'),'9f02862b2592d5d3d7ab0f7aec0aeecdc6264ae67e4eec3369ed58c3cc86efc6');
const config=read(path.join(notes,A+'-config.json'),'3b0deaaf0cdc65a34a8e4652e0a04d96a840db354ccada71d9cba5e4cd228e23');
const ready=read(path.join(notes,A+'-accepted-ready-extracted.json'),'621b71f00bec98ccf7cb90e465c613b53fdba2adc6a79c9d974797d9d59c6ec0');
const tailPath=path.join(notes,A+'-tail-response_0003.json.gz');
const packet=read(tailPath,'018d19c6ca8c27acc5cc1dde6d396ee783e34ae25e5b525158c5bb37086520d9');
const response=packet.response;
const flowPath=path.join(notes,A+'-tail-response-full-tangent-call0003-manifest.json.gz');
const flow=read(flowPath,'3f63c69738fc171709a4cba47baeaf70c40778876e03f93436db56b302578e1f');
const meanPath=path.join(notes,meanName+'.json.gz');
const means=read(meanPath,'59717e6b83c009671781054b7042624fa30ef39b9f8f9660e9511b1481092e14');
const meanOwned=read(path.join(notes,meanName+'-resource.json'),'87be4d190ccccab57e4731969abefe2fcd446ebc95f88126e61ebb7b0a504802');
check('original A owned exit zero',owned.exitcode===0&&owned.wait4_observed===true);
check('original A whole BVP accepted',primary.solver_success===true&&primary.audit_pending===false&&primary.modes===32&&primary.config.actual_nonlinear_tail===true);
check('original ready object unchanged',equal(ready,primary.actual_tail.ready));
check('original full audited tail response',response.converged===true&&response.residual<config.solveTolerance&&response.audit&&typeof response.audit==='object');
check('original tail source map',equal(packet.source_sha256,primary.actual_tail.source_sha256));
const io=new Set(['traceFile','iterationCheckpointFile','trialDiagnosticFile','initialCheckpoint']);
const nonIO=x=>Object.fromEntries(Object.entries(x).filter(([k])=>!io.has(k)));
check('primary complete physical config',equal(nonIO(config),nonIO(primary.actual_tail.config)));
check('packet complete physical config',equal(nonIO(config),nonIO(packet.config)));
check('fixed original M32 tail settings',config.modes===32&&config.spacing===2&&config.depth===8&&config.shootingParts===8&&config.quadrature===512&&config.orientation===1);
check('complete audited fullflow schema',flow.schema==='full-shooting-flow-tangent-storage-v1'&&flow.complete===true&&flow.baseHadAudit===true&&flow.allStageFlowJacobiansRetained===true&&flow.allBaseStatesAndHeightsRetained===true);
check('fullflow original solve tolerance',flow.convergedBaseResidual<flow.originalSolveTolerance);
check('fullflow final response checksum',response.fullFlowTangentSnapshot.manifestSha256===hashes[flowPath]);
check('fullflow typed identity checksum',sha(Buffer.from(flow.identityCanonical))===flow.identitySha256);
const identity=typed(JSON.parse(flow.identityCanonical));
const {modes:M,stateDimension:K,stages,nodes}=flow.dimensions,N=config.quadrature;
check('all 577 nodes and 576 stages',M===32&&K===64&&stages===576&&nodes===577);
check('original complete checkpoint parameters',equal(nonIO(response.checkpoint.parameters),identity.parameters));
check('original raw-node map',equal(response.checkpoint.rawNode,identity.rawNode)&&equal(identity.rawNode,[0,72,144,216,288,360,432,504,576]));
function binary(record,expected){
  check('sidecar raw dimensions '+record.file,record.rawBytes===expected);
  const compressed=readBytes(sidecar(notes,record.file),record.sha256);
  check('sidecar compressed bytes '+record.file,compressed.length===record.bytes);
  const raw=gunzipSync(compressed,{maxOutputLength:expected});
  check('sidecar raw SHA '+record.file,raw.length===expected&&sha(raw)===record.rawSha256);
  return raw;
}
check('base layout counts',equal(flow.base.counts,{states:nodes*K,physicalH:M,farGraph:M,radius:1,rawNode:identity.rawNode.length}));
const seed=binary(flow.base,(nodes*K+2*M+1+identity.rawNode.length)*8);let at=0;
function take(n){const a=Array(n);for(let j=0;j<n;j++){a[j]=finite(seed.readDoubleLE(at),'base');at+=8;}return a;}
const states=Array.from({length:nodes},()=>take(K)),H=take(M),farGraph=take(M),radius=take(1)[0],rawNode=take(identity.rawNode.length);
check('base fully consumed',at===seed.length);
check('complete H and far graph bits',equal(H,packet.request.height)&&equal(farGraph,identity.farGraph)&&Object.is(radius,identity.radius)&&equal(rawNode,identity.rawNode));
const checkpointText=x=>JSON.stringify({states:x.states.map(v=>Array.from(v)),cutHeight:Array.from(x.cutHeight),rawNode:Array.from(x.rawNode)});
check('binary seed complete original JSON checkpoint binding',sha(Buffer.from(checkpointText({states,cutHeight:H,rawNode})))===flow.checkpointNumericJSONSha256);
check('final complete checkpoint binding',sha(Buffer.from(checkpointText(response.checkpoint)))===flow.checkpointNumericJSONSha256);
check('original finite mean owned zero',meanOwned.exitcode===0&&meanOwned.wait4_observed===true);
check('complete original saved mean identity',means.schema==='accepted-finite-tail-saved-mean-v1'&&means.finished===true&&means.original_fullflow_identity_sha256===flow.identitySha256&&means.every_original_stage_file_reconstructs_bit_for_bit===true&&equal(means.dimensions,flow.dimensions));
check('mean actual input binding',[hashes[primaryPath],hashes[tailPath],hashes[flowPath]].every(h=>Object.values(means.input_sha256).includes(h)));
const compactCompressed=readBytes(sidecar(notes,means.compact_archive.file),'ccd837316e5de3a0a0ca3e3a29a8c1257c2655da3297f6b7d6742605d631a981');
check('mean sidecar declared checksum',sha(compactCompressed)===means.compact_archive.sha256);
const compact=gunzipSync(compactCompressed,{maxOutputLength:stages*(K+3)*8});
check('complete mean sidecar raw identity',compact.length===stages*(K+3)*8&&sha(compact)===means.compact_archive.raw_sha256&&means.rows.length===stages);
const stageMeans=new Float64Array(stages);let forwardMean=0,flowCount=0,flowScalars=0;
for(const chunk of flow.chunks){
  check('complete nonoverlapping fullflow chunks '+flowCount,chunk.firstStage===flowCount&&chunk.stageCount>0&&equal(chunk.shape,[chunk.stageCount,K,K])&&chunk.matrixLayout==='row-major');
  const J=binary(chunk,chunk.stageCount*K*K*8);
  for(let q=0;q<J.length;q+=8){finite(J.readDoubleLE(q),'saved J');flowScalars++;}
  for(let q=0;q<chunk.stageCount;q++){
    const n=flowCount+q,row=means.rows[n],kept=compact.subarray(n*(K+3)*8,(n+1)*(K+3)*8);
    const input=seed.subarray((n+1)*K*8,(n+2)*K*8);
    const headerBytes=Buffer.from(row.header_utf8_base64,'base64'),header=JSON.parse(headerBytes);
    const payload=Buffer.concat([kept.subarray(0,K*8),J.subarray(q*K*K*8,(q+1)*K*K*8),kept.subarray(K*8)]);
    check('original stage input and layout '+n,row.stage===n&&header.stage===n&&header.dimension===K&&header.withJac===true&&header.inputSHA===sha(input)&&header.identitySHA===means.complete_original_cache_identity_sha256&&row.input_sha256===header.inputSHA);
    check('original complete stage payload '+n,sha(payload)===header.payloadSHA256&&header.payloadSHA256===row.payload_sha256);
    const length=Buffer.alloc(4);length.writeUInt32LE(headerBytes.length);
    check('exact original stage reconstruction '+n,sha(Buffer.concat([Buffer.from('VFXJAC01'),length,headerBytes,payload]))===row.cache_file_sha256);
    for(let j=0;j<K+3;j++)finite(kept.readDoubleLE(j*8),'saved stage');
    stageMeans[n]=kept.readDoubleLE(K*8);
    check('original scalar mean bits '+n,Object.is(stageMeans[n],row.mean_height_increment));
    forwardMean+=stageMeans[n];
  }
  flowCount+=chunk.stageCount;
}
check('all original fullflow retained',flowCount===stages&&flowScalars===stages*K*K&&flow.rawFlowBytes===stages*K*K*8);
check('original forward ordered mean sum',Object.is(forwardMean,means.saved_original_meanHeightToCut_forward_sum));
const meanAtNode=new Float64Array(nodes);
for(let i=0;i<nodes;i++){let h=0;for(let n=i;n<stages;n++)h+=stageMeans[n];meanAtNode[i]=finite(h,'node mean');}
check('node zero original sum and inner zero anchor',Object.is(meanAtNode[0],forwardMean)&&Object.is(meanAtNode[stages],0));

const depFile=path.join(comp,'source-dependencies.json');
const deps=read(depFile,'7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941');
check('original source manifest revision',deps.source_revision==='869436630c99aa5a68afb55bd8877c826034d117'&&deps.files.length===91);
const prefix='topics/visible-flexible-closed-surface/';
for(const f of deps.files){
  check('pinned source within exact topic '+f.path,f.path.startsWith(prefix)&&!f.path.slice(prefix.length).split('/').includes('..'));
  const bytes=readBytes(path.join(sourceTopic,f.path.slice(prefix.length)),f.sha256);
  check('pinned source byte count '+f.path,bytes.length===f.bytes);
}
const pins={
  'tail_frozen_geometry.mjs':'db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3',
  'strong_frozen_calibration_factory.mjs':'77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247',
  'closure_bounded_point_cache.mjs':'35289a4de44ec409bc211f82c7a1bee81a10c6bc1c5fb31e4ca9a8634cc09043'
};
for(const [file,want] of Object.entries(pins))readBytes(path.join(comp,file),want);
const ledger=path.join(notes,'2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json');
const stored=path.join(notes,'2026-11-13-strong-m28-recovered-full-audit-r1-ready.json');
readBytes(ledger,identity.physicalIdentity.calibrationLedgerSHA256);
readBytes(stored,identity.physicalIdentity.storedReferenceReadySHA256);
process.env.VISIBLE_FLEX_SOURCE_TOPIC=sourceTopic;
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(sourceTopic,'repro/source-root');
process.env.VISIBLE_FLEX_FROZEN_LEDGER_READY=ledger;
process.env.VISIBLE_FLEX_FROZEN_STORED_READY=stored;
process.env.VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT='8';
process.env.CLOSING_TAIL_CACHE=path.join(sourceTopic,'repro/source-root/topics/large-amplitude-twist-flex/scripts');
const {createStoredPhysical}=await import(pathToFileURL(path.join(comp,'tail_frozen_geometry.mjs')).href);
const {physical,manifest:geometry}=await createStoredPhysical(config);
const old=ready.storedMetricAdapter;
check('same complete physical geometry',physical.cells.length===160&&geometry.cellCount===160&&geometry.profileFingerprintBefore===old.profileFingerprintBefore&&geometry.profileFingerprintAfter===old.profileFingerprintAfter&&geometry.profileFingerprintBefore===geometry.profileFingerprintAfter);
check('same global warp alpha',Object.is(physical.stats.alpha,old.frozenWarpAlpha)&&Object.is(physical.stats.alpha,identity.physicalIdentity.frozenWarpAlpha));
check('same complete physical parameters',equal(nonIO(geometry.physicalParameters),nonIO(old.physicalParameters))&&equal(nonIO(geometry.physicalParameters),identity.physicalIdentity.parameters));
check('same fingerprint bound to fullflow',geometry.profileFingerprintAfter===identity.physicalIdentity.profileFingerprintAfter&&geometry.profileFingerprintBefore===identity.physicalIdentity.profileFingerprintBefore&&equal(geometry.fingerprintFields,identity.physicalIdentity.fingerprintFields)&&equal(geometry.fingerprintFractions,identity.physicalIdentity.fingerprintFractions));
const {subdividePhysical}=await import(pathToFileURL(path.join(sourceTopic,'scripts/950f-tail-subdivision.mjs')).href);
const {createFourierRootSplitFluxEngine}=await import(pathToFileURL(path.join(sourceTopic,'scripts/78718-tail-fourier-root-split-engine.mjs')).href);
const baseScripts=path.join(sourceTopic,'repro/source-root/topics/large-amplitude-twist-flex/scripts');
const {createMomentumPhysicalJetEvaluator}=await import(pathToFileURL(path.join(baseScripts,'f6tail_momentum_physical_jets.mjs')).href);
const {relativeActualDevelopment}=await import(pathToFileURL(path.join(baseScripts,'f6tail_relative_development.mjs')).href);
const stagesNow=subdividePhysical(physical,config.depth,config.shootingParts);
check('same complete shooting subdivision',stagesNow.cells.length===stages&&equal(stagesNow.rawNode,identity.rawNode));
const layoutKeys=['rawCell','rawSegment','rawLeft','rawRight','part','parts','portRatio','mu'];
for(let n=0;n<stages;n++){
  const cell=stagesNow.cells[n],row={stage:n};
  for(const key of layoutKeys)row[key]=cell[key];
  row.profileIntegrationBreakpoints=cell.profiles.map(p=>Array.from(p.integrationBreakpoints??[]));
  check('full original stage layout '+n,equal(row,identity.stageLayout[n]));
}
const preflight={schema:'accepted-A-tail-node-readout-preflight-v1',finished:true,input_sha256:hashes,
  source_sha256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),range:[first,last],
  original_fullflow_identity_sha256:flow.identitySha256,checks,geometry,
  complete_saved_J_scalars_verified:flowScalars,no_new_ODE_RK_shooting_or_BVP_Newton_or_variational_flow:true};
saveJSON(path.join(outDir,'preflight.json'),preflight);
console.log(JSON.stringify({event:'preflight_complete',nodesRequested:last-first,checks:checks.length,meanHeightToCut:forwardMean}));

let roots=0,rhs=0,engineRawCell=null,engine=null,evaluate=null;
const rows=[],summary={sampleMetric:0,formalHeightCurvature:0,rootRelativeResidual:0,darboux:0,translationPeriod:0,angularHolonomyResidual:0,minA:Infinity,minD:Infinity};
const columns=['delta_X_round','delta_Y_round','height_oscillatory','delta_X_r_round','delta_Y_r_round','height_r','delta_X_theta_round','delta_Y_theta_round','height_theta','height_rr','height_rtheta','height_thetatheta'];
for(let node=first;node<last;node++){
  const sn=node===0?0:node-1,cell=stagesNow.cells[sn],profile=node===0?cell.profiles.at(-1):cell.profiles[0],x=node===0?1:0;
  if(engineRawCell!==cell.rawCell){
    engine=createFourierRootSplitFluxEngine({modes:M,spacing:config.spacing,quadrature:N,mu:cell.mu,orientation:config.orientation,projectionFloor:config.projectionFloor,cuspAwareFlow:config.cuspAwareFlow});
    const r=engine.root.bind(engine),f=engine.rhs.bind(engine);
    engine.root=(...a)=>{roots++;return r(...a);};
    engine.rhs=(...a)=>{rhs++;return f(...a);};
    const forbidden=()=>{throw Error('No RK, ODE, or flow evaluation belongs to this node-only readout');};
    for(const key of ['rk4','flowRawCell','flowStateWithJacobian','flow','integrate'])if(typeof engine[key]==='function')engine[key]=forbidden;
    evaluate=createMomentumPhysicalJetEvaluator(engine,{spacing:config.spacing});
    engineRawCell=cell.rawCell;
  }
  const y=new Float64Array(K+2);y.set(states[node]);
  const piMultiplier=node===0?cell.portRatio:1;
  if(node===0)for(let j=0;j<M;j++)y[M+j]*=piMultiplier;
  const root=engine.root(y,profile,x),jets=evaluate(y,profile,x),g=root.g;
  const rel=relativeActualDevelopment(g,root.e.rows,jets.perAngle);
  check('node point domain '+node,g.r>0&&g.w>0&&g.drdx>0&&root.e.minA>0&&root.e.minD>0&&jets.minA>0&&jets.minD>0);
  check('complete point angular rows '+node,root.e.rows.length===N&&jets.perAngle.length===N&&rel.dx.length===N);
  const bytes=Buffer.alloc(N*columns.length*8);
  for(let j=0;j<N;j++){
    const v=jets.perAngle[j];
    const values=[rel.dx[j],rel.dy[j],v.height,rel.dxR[j],rel.dyR[j],v.ur,rel.dxT[j],rel.dyT[j],v.ut,v.urr,v.urt,v.utt];
    for(let k=0;k<values.length;k++)bytes.writeDoubleLE(finite(values[k],'node '+node+' angular '+j+' column '+k),(j*values.length+k)*8);
  }
  const file='node-'+String(node).padStart(4,'0')+'.f64le.gz';
  fs.writeFileSync(path.join(outDir,file),gzipSync(bytes,{level:6}),{flag:'wx'});
  const record={node,stage:sn,rawCell:cell.rawCell,rawSegment:cell.rawSegment,x,
    nodePiMultiplier:piMultiplier,mu:cell.mu,geometry:{r:g.r,w:g.w,w2:g.w2,E:g.E,drdx:g.drdx,dlogwdx:g.dlogwdx,logw:g.logw},
    meanHeightInnerAnchor:meanAtNode[node],
    meanSumConvention:'stages node,...,575 in original increasing-stage addition order; node576=0',
    inputStateRawSha256:sha(seed.subarray(node*K*8,(node+1)*K*8)),
    file,shape:[N,columns.length],rawBytes:bytes.length,rawSha256:sha(bytes),
    bytes:fs.statSync(path.join(outDir,file)).size,sha256:sha(fs.readFileSync(path.join(outDir,file))),
    sampleMetricRelativeOperatorError:finite(rel.actualMetricRelativeOperatorError,'point metric'),
    formalHeightCurvature:finite(jets.formalHeightCurvature,'height curvature'),
    maxDarboux:finite(jets.maxDarboux,'Darboux'),
    rootRelativeResidual:finite(jets.rootRelativeResidual,'root residual'),
    minA:jets.minA,minD:jets.minD,
    translationPeriod:finite(rel.translationPeriod,'period'),angularHolonomyResidual:finite(rel.angularHolonomyResidual,'holonomy'),
    angularPhaseMeanDerivative:finite(rel.angularPhaseMeanDerivative,'phase derivative')};
  saveJSON(path.join(outDir,'node-'+String(node).padStart(4,'0')+'-record.json'),record);
  rows.push(record);
  summary.sampleMetric=Math.max(summary.sampleMetric,record.sampleMetricRelativeOperatorError);
  summary.formalHeightCurvature=Math.max(summary.formalHeightCurvature,record.formalHeightCurvature);
  summary.rootRelativeResidual=Math.max(summary.rootRelativeResidual,record.rootRelativeResidual);
  summary.darboux=Math.max(summary.darboux,record.maxDarboux);
  summary.translationPeriod=Math.max(summary.translationPeriod,record.translationPeriod);
  summary.angularHolonomyResidual=Math.max(summary.angularHolonomyResidual,record.angularHolonomyResidual);
  summary.minA=Math.min(summary.minA,record.minA);summary.minD=Math.min(summary.minD,record.minD);
  console.log(JSON.stringify({event:'node_complete',node,file,sha256:record.sha256,metric:record.sampleMetricRelativeOperatorError}));
  if(typeof globalThis.gc==='function')globalThis.gc();
}
const result={schema:'accepted-A-all-shooting-node-Cartesian-first-jet-readout-v1',finished:true,
  source_sha256:preflight.source_sha256,input_inventory_commit:'c2efbb20c47a84adbc76fdca62b250c178d0d7fe',
  input_sha256:hashes,original_fullflow_identity_sha256:flow.identitySha256,
  original_A_primary_sha256:hashes[primaryPath],original_final_tail_sha256:hashes[tailPath],
  original_mean_primary_sha256:hashes[meanPath],range:[first,last],requestedNodes:last-first,completedNodes:rows.length,
  whole_577_node_readout_complete:first===0&&last===577,angular:N,columns,layout:'node files: angle-major Float64LE, no omitted angles',
  angular_rule:'theta_j=2*Math.PI*j/512, j=0,...,511, exactly the original point evaluator grid',
  reconstruction:{position:['r*cos(theta)+delta_X_round','r*sin(theta)+delta_Y_round','meanHeightInnerAnchor+height_oscillatory'],
    radial:['cos(theta)+delta_X_r_round','sin(theta)+delta_Y_r_round','height_r'],
    angular:['-r*sin(theta)+delta_X_theta_round','r*cos(theta)+delta_Y_theta_round','height_theta']},
  vertical_second_jets_only:true,horizontal_rr_not_computed:true,
  height_anchor:'The deepest shooting node576 has mean height zero. A separate actual prefix-cut height/rigid frame matching is required.',
  original_meanHeightToCut_forward_sum:forwardMean,checks,summary,rows,
  evaluations:{pointRoots:roots,pointRHS:rhs,RKSteps:0,ODEFlows:0,shootingOrBVPNewtonSolves:0,pointRootNewton:'permitted inside original point roots; iterations not counted here',newVariationalFlows:0},
  limitations:['Finite accepted M32/depth8/steps12 state readout at 577 possible radial nodes and 512 original angular nodes only.',
    'Point roots and actual vertical two-jets are newly evaluated by the pinned original formulas; no interval or continuous radial error bound.',
    'Horizontal development uses the pinned original centered-round and zero-mean-phase gauge; no fitted rigid transformation.',
    'Saved stage mean is a finite original integral. It is not replaced by the rotational background and is not a rigorous integral remainder bound.',
    'Horizontal rr jets, continuous Hermite/tail agreement, flat closure, all-t fixed-g refinement, complete diameter, reach and Hausdorff amplitudes remain separate obligations.',
    'No new physical solution, changed acceptance gate, or successful CI/owned status is inferred from source preparation.'],
  seconds:Number(process.hrtime.bigint()-start)/1e9};
saveJSON(path.join(outDir,'complete.json'),result);
console.log(JSON.stringify({event:'complete',file:path.join(outDir,'complete.json'),nodes:rows.length,roots,rhs,summary,seconds:result.seconds}));
