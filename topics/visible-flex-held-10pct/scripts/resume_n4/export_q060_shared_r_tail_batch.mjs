// Batch construction of one common literal-R tail map from a saved response.
// All stages share one assembly and one cumulative original mean chain.
// Canonical boundary values are actually copied, not merely compared closely.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL,fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {gunzipSync,gzipSync} from 'node:zlib';
import {parseArgs} from 'node:util';

const {values}=parseArgs({options:{input:{type:'string'},outdir:{type:'string'},
 stages:{type:'string'},anchors:{type:'string'},degree:{type:'string',default:'192'},
 'difference-step':{type:'string',default:'0.00005'}}});
if(!values.input||!values.outdir||!values.stages)throw Error('--input --outdir --stages required');
if(fs.existsSync(values.outdir))throw Error('Use a fresh batch output directory');
fs.mkdirSync(values.outdir,{recursive:true});
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const read=p=>JSON.parse((p.endsWith('.gz')?gunzipSync(fs.readFileSync(p)):fs.readFileSync(p)).toString());
const checked=ref=>{if(sha(ref.path)!==ref.sha256)throw Error('Bound input changed '+ref.path);return read(ref.path);};
const packet=read(values.input);
if(packet.status!=='all_saved_initial_states_matched_single_mean_chain')throw Error('Unbound cumulative mean chain');
const saved=checked(packet.checkpoint),cp=saved.response.checkpoint,metadata=checked(packet.metadata);
checked(packet.native_record);checked(packet.manifest);
const topic=packet.source_topic,src=path.join(topic,'repro/source-root/topics/large-amplitude-twist-flex/scripts');
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');process.env.CLOSING_TAIL_CACHE=src;
const module=n=>import(pathToFileURL(path.join(src,n)));
const factoryPath=path.join(topic,'scripts/closing_weighted_tail.mjs'),subdivisionPath=path.join(topic,'scripts/950f-tail-subdivision.mjs');
for(const name of ['closing_weighted_tail.mjs','closing_recalibrated_tail.mjs','950f-tail-subdivision.mjs'])
 if(sha(path.join(topic,'scripts',name))!==packet.source_files[name])throw Error('Original source changed '+name);
const {createRecalibrationFactory}=await import(pathToFileURL(factoryPath));
const {subdividePhysical}=await import(pathToFileURL(subdivisionPath));
const {createFastSplitFluxMomentumTailEngine}=await module('f6tail_fast_split_flux_engine.mjs');
const {withCuspAwareRK}=await module('f6tail_cusp_grid.mjs');
const {createRelativeSpatialJetEvaluator}=await module('f6tail_relative_spatial_jets.mjs');
const p=packet.config,scope=packet.finite_scope,M=scope.M,N=scope.quadrature,K=2*M;
const degree=Number(values.degree),dh=Number(values['difference-step']);
if(N!==512||M!==24||scope.spacing!==3||N<2*degree+4)throw Error('Unexpected finite field scope');
const begun=performance.now(),factory=createRecalibrationFactory(p),physical=factory.assemble();
const subdivided=subdividePhysical(physical,p.depth,p.shootingParts),cells=subdivided.cells,S=cells.length;
if(cp.states.length!==S+1||packet.mean_chain.length!==S+1)throw Error('Node count mismatch');
const selected=values.stages==='all'?Array.from({length:S},(_,j)=>j):values.stages.split(',').map(Number);
if(selected.some(j=>!Number.isInteger(j)||j<0||j>=S)||new Set(selected).size!==selected.length)throw Error('Invalid stage selection');
selected.sort((a,b)=>b-a); // Export outward from the inner finite tail.
for(let j=0;j<S;j++)for(const key of ['rawCell','rawSegment','rawLeft','rawRight','portRatio','mu'])
 if(cells[j][key]!==metadata.stages[j][key])throw Error('Native stage identity changed '+j+' '+key);
const modes=[];for(let m=-degree;m<=degree;m++)if((m-1)%3===0)modes.push(m);
const heightModes=Array.from({length:M+1},(_,j)=>3*j),P=modes.length,C=P+M+1;
const trig=modes.map(m=>({cos:Float64Array.from({length:N},(_,n)=>Math.cos(2*Math.PI*n*m/N)),
 sin:Float64Array.from({length:N},(_,n)=>Math.sin(2*Math.PI*n*m/N))}));
const engines=new Map();
function engineFor(index){
 if(engines.has(index))return engines.get(index);
 const cell=cells[index];let engine=createFastSplitFluxMomentumTailEngine({modes:M,spacing:scope.spacing,
  quadrature:N,mu:cell.mu,orientation:scope.orientation,projectionFloor:scope.projectionFloor});
 engine=withCuspAwareRK(engine);
 const result={engine,evaluator:createRelativeSpatialJetEvaluator(engine,{spacing:scope.spacing,radialDifferenceStep:dh})};
 engines.set(index,result);return result;
}
function endpointState(index,inner){
 const node=index+(inner?1:0),state=new Float64Array(K+2),cell=cells[index];
 for(let j=0;j<K;j++)state[j]=cp.states[node][j]*(inner||j<M?1:cell.portRatio);
 state[K]=packet.mean_chain[node][0];state[K+1]=packet.mean_chain[node][1];return state;
}
function pack(a,state){
 const out=Array.from({length:3},()=>Array(C).fill(0));
 for(let d=0;d<3;d++)for(let k=0;k<P;k++){
  let sum=0;for(let n=0;n<N;n++){const v=a.perAngle[n][['V','Vr','Vrr'][d]];sum+=v[0]*trig[k].cos[n]+v[1]*trig[k].sin[n];}
  out[d][k]=sum/N;
 }
 const {g,root,field,heightJets:j}=a,sigma=g.drdx/g.r;
 out[0][P]=state[K];out[1][P]=g.w*root.L[0];out[2][P]=g.w*(j.Ldot[0]+g.dlogwdx*root.L[0])/g.drdx;
 for(let k=0;k<M;k++){
  const m=heightModes[k+1],i=P+k+1;out[0][i]=g.r**4*state[k];
  out[1][i]=m*m*g.r**3*state[k]+Math.sqrt(2)*g.w*root.L[k+1];
  out[2][i]=(m*m*g.r**3*(field[k]+3*sigma*state[k])+Math.sqrt(2)*g.w*(j.Ldot[k+1]+g.dlogwdx*root.L[k+1]))/g.drdx;
 }
 return out;
}
function sample(index,state,xi,kind){
 const cell=cells[index],a=engineFor(index).evaluator.evaluate(state,cell.profiles[0],xi),coefficients=pack(a,state);
 return {kind,xi,sourceX:cell.rawLeft+(cell.rawRight-cell.rawLeft)*xi,sourceStage:index,
  radiusJS:a.g.r,coefficients,backgroundJS:{w:a.g.w,wR:a.g.w*a.g.dlogwdx/a.g.drdx,E:a.g.E},
  sourceMetric:a.development.actualMetricRelativeOperatorError,sourceHeightDarboux:a.heightJets.maxDarboux,
  rootRelativeResidual:a.root.err/a.root.scale,minRootD:a.root.e.minD,minLeading:a.root.e.minA,
  meanPerturbation:state[K],meanBackground:state[K+1],physicalHeight:Array.from(state.slice(0,M),u=>a.g.r**4*u)};
}
const anchorsInput=values.anchors?read(values.anchors):{reuse_stages:{},node_anchors:[]};
const reuse=new Map(),canonical=new Map(),anchors=[];
const mapHash=d=>createHash('sha256').update(JSON.stringify({planarModes:d.planarModes,heightModes:d.heightModes,
 nodes:d.nodes.map(v=>({r:v.radiusJS,c:v.coefficients}))})).digest('hex');
function loadStage(name){
 const d=read(name),originalPacket=read(d.input);
 if(originalPacket.checkpoint.sha256!==packet.checkpoint.sha256||JSON.stringify(d.planarModes)!==JSON.stringify(modes)
  ||JSON.stringify(d.heightModes)!==JSON.stringify(heightModes))throw Error('Prior stage map belongs to a different field '+name);
 return d;
}
function setAnchor(node,value,definition){
 if(value.meanPerturbation!==packet.mean_chain[node][0]||value.meanBackground!==packet.mean_chain[node][1])
  throw Error('An anchor has a different cumulative mean at node '+node);
 if(canonical.has(node)){
  const other=canonical.get(node).value;
  if(other.radiusJS!==value.radiusJS||JSON.stringify(other.coefficients)!==JSON.stringify(value.coefficients))throw Error('Conflicting explicit canonical anchors');
 }
 canonical.set(node,{value,definition});anchors.push({node,...definition});
}
for(const [key,ref]of Object.entries(anchorsInput.reuse_stages??{})){
 const index=Number(key),d=loadStage(ref.path);if(d.stage!==index)throw Error('Reuse stage index differs');
 reuse.set(index,{data:d,path:ref.path,preserve:!!ref.preserve,sha256:sha(ref.path)});
 if(ref.preserve){
  setAnchor(index,d.nodes.at(-1),{kind:'previously_certified_stage_endpoint',stage:index,endpoint:'outer',path:ref.path,sha256:sha(ref.path)});
  setAnchor(index+1,d.nodes[0],{kind:'previously_certified_stage_endpoint',stage:index,endpoint:'inner',path:ref.path,sha256:sha(ref.path)});
 }
}
for(const ref of anchorsInput.node_anchors??[]){
 const d=loadStage(ref.path),v=ref.endpoint==='inner'?d.nodes[0]:d.nodes.at(-1);
 setAnchor(ref.node,v,{kind:'explicit_existing_component_anchor',stage:d.stage,endpoint:ref.endpoint,path:ref.path,sha256:sha(ref.path)});
}
function canonicalNode(node){
 if(canonical.has(node))return canonical.get(node);
 const index=node===0?0:node-1,inner=node!==0;
 const value=sample(index,endpointState(index,inner),inner?0:1,'canonical_boundary');
 const definition={kind:'outer_stage_inner_endpoint',stage:index,endpoint:inner?'inner':'outer'};
 const result={value,definition};canonical.set(node,result);return result;
}
const outdir=path.resolve(values.outdir),manifestPath=path.join(outdir,'manifest.json');
const sourceNames=['f6tail_relative_spatial_jets.mjs','f6tail_relative_development.mjs','f6tail_momentum_physical_jets.mjs',
 'f6tail_fast_split_flux_engine.mjs','f6tail_momentum_split_flux.mjs','f6tail_cusp_grid.mjs'];
const manifest={status:'running',input:{path:path.resolve(values.input),sha256:sha(values.input)},
 sourceSHA256:Object.fromEntries([fileURLToPath(import.meta.url),factoryPath,subdivisionPath,...sourceNames.map(n=>path.join(src,n))].map(p=>[p,sha(p)])),
 existingCheckpoint:packet.checkpoint,selectedStages:selected,finiteScope:scope,degree,planarModes:modes,heightModes,
 physicalParameters:physical.parameters,physicalStats:physical.stats,
 canonicalRule:'At internal node k use outer stage k-1 inner physical-R jet, except the declared previously certified anchors. Node0 is the original cut outer jet; the deepest node uses its explicit collar anchor if supplied. Copy all Cartesian/Fourier value and first/second jets and the radius exactly.',
 meanContract:packet.mean_contract,explicitAnchors:anchors,files:[],interfaceRepairs:[],
 originalBvpSolvesExecuted:0,shootingIterationsExecuted:0,assemblies:1,globalContinuousMetricCertified:false};
const save=()=>fs.writeFileSync(manifestPath,JSON.stringify(manifest,null,2)+'\n');save();
let active=null;
try{
 for(const index of selected){
  active=index;const cell=cells[index],old=reuse.get(index);let d;
  if(old)d=structuredClone(old.data);
  else{
   const grid=metadata.stages[index].profileGrids[0],{engine}=engineFor(index),profile=cell.profiles[0];
   const states=[endpointState(index,true)],xs=[0];
   for(const step of grid){states.push(engine.rk4(states.at(-1),profile,step.x,step.h));xs.push(step.x+step.h);}
   const replay=states.at(-1);states[states.length-1]=endpointState(index,false);
   const nodes=[],midpoints=[];
   for(let i=0;i<xs.length;i++){
    nodes.push(sample(index,states[i],xs[i],'node'));
    if(i<grid.length){const x=(xs[i]+xs[i+1])/2,s=engine.rk4(states[i],profile,xs[i],x-xs[i]);midpoints.push(sample(index,s,x,'midpoint'));}
   }
   d={status:'literal_R_stage_before_common_boundary_selection',stage:index,rawCell:cell.rawCell,rawSegment:cell.rawSegment,
    rawLeft:cell.rawLeft,rawRight:cell.rawRight,finiteScope:scope,degree,planarModes:modes,heightModes,
    nodes,midpoints,physicalParameters:physical.parameters,
    originalReplayEndVsNative:{first48MaximumAbsoluteDifference:Math.max(...Array.from(replay.slice(0,K),(v,j)=>Math.abs(v-packet.native_stage_outputs[index][j]))),
     meanIncrementDifferences:Array.from({length:2},(_,j)=>replay[K+j]-packet.mean_chain[index+1][j]-packet.native_stage_outputs[index][K+j])},
    sourceSHA256:manifest.sourceSHA256};
  }
  const beforeHash=mapHash(d),repairs=[];
  for(const [node,local]of [[index+1,0],[index,d.nodes.length-1]]){
   const original=d.nodes[local],chosen=canonicalNode(node),target=chosen.value;
   const maximumJetDifferences=Array.from({length:3},(_,j)=>Math.max(...original.coefficients[j].map((v,k)=>Math.abs(v-target.coefficients[j][k]))));
   const repair={node,receivingStage:index,endpoint:local===0?'inner':'outer',canonical:chosen.definition,
    originalRadius:original.radiusJS,canonicalRadius:target.radiusJS,radiusDifference:target.radiusJS-original.radiusJS,
    maximumJetDifferences,meanDifference:target.meanPerturbation-original.meanPerturbation,
    physicalHeightMaximumDifference:Math.max(...original.physicalHeight.map((v,j)=>Math.abs(v-target.physicalHeight[j])))};
   repairs.push(repair);manifest.interfaceRepairs.push(repair);
   d.nodes[local]={...structuredClone(target),kind:'shared_canonical_node',xi:local===0?0:1,
    canonicalNode:node,canonicalDefinition:chosen.definition,
    receiverOriginalSource:{radiusJS:original.radiusJS,sourceStage:index,sourceX:original.sourceX,xi:original.xi}};
  }
  if(d.nodes.some((v,j)=>j&&!(v.radiusJS>d.nodes[j-1].radiusJS)))throw Error('Canonical R endpoint destroys positive span at '+index);
  const afterHash=mapHash(d);
  if(old?.preserve&&beforeHash!==afterHash)throw Error('A previously certified map would change at stage '+index);
  d.status='literal_R_stage_with_exact_common_boundary_two_jets';d.boundInput=manifest.input;
  d.coordinateDefinition='All radiusJS values are declared exact binary-real R knots. Endpoint values come from the explicitly recorded canonical node, possibly another adjacent source profile; they are not true-R interval midpoints.';
  d.meanDefinition=packet.mean_contract;d.sharing={repairs,mapHash:afterHash,previousMapHash:beforeHash,
   previouslyCertifiedMapPreserved:old?.preserve??false,reusedData:old?{path:old.path,sha256:old.sha256}:null};
  const name=path.join(outdir,'stage-'+String(index).padStart(4,'0')+'.json.gz');
  fs.writeFileSync(name,gzipSync(JSON.stringify(d),{level:6}));
  manifest.files.push({stage:index,path:name,sha256:sha(name),bytes:fs.statSync(name).size,mapHash:afterHash,
   nodes:d.nodes.length,midpoints:d.midpoints.length,previouslyCertifiedMapPreserved:old?.preserve??false});
  manifest.seconds=(performance.now()-begun)/1000;save();
  console.log(JSON.stringify({stage:index,nodes:d.nodes.length,reused:!!old,preserved:old?.preserve??false,
   repairs:repairs.map(r=>({node:r.node,radius:r.radiusDifference,jets:r.maximumJetDifferences})),seconds:manifest.seconds}));
  engines.delete(index);
 }
 const byStage=new Map(manifest.files.map(v=>[v.stage,v]));
 manifest.exactAdjacentCommonNodeChecks=[];
 for(const index of selected)if(byStage.has(index+1)){
  const outer=read(byStage.get(index).path).nodes[0],inner=read(byStage.get(index+1).path).nodes.at(-1);
  const same=outer.radiusJS===inner.radiusJS&&JSON.stringify(outer.coefficients)===JSON.stringify(inner.coefficients);
  if(!same)throw Error('Adjacent output stages do not share the exact same node');
  manifest.exactAdjacentCommonNodeChecks.push({outerStage:index,innerStage:index+1,node:index+1,exactSharedRadiusAndCartesianTwoJets:true});
 }
 manifest.status='selected_stages_share_one_literal_R_C2_definition';manifest.seconds=(performance.now()-begun)/1000;save();
 console.log(JSON.stringify({status:manifest.status,stages:manifest.files.length,sharedInterfaces:manifest.exactAdjacentCommonNodeChecks.length,
  seconds:manifest.seconds,manifestSHA256:sha(manifestPath)}));
}catch(error){manifest.status='failed';manifest.failedStage=active;manifest.error=String(error);manifest.seconds=(performance.now()-begun)/1000;save();throw error;}
