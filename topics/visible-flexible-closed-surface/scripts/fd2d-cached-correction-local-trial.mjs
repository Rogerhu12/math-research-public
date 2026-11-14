// Diagnose the actual slow Newton step from its retained complete stage maps.
// Reconstruct the original Riccati algebra without rerunning any full-J map;
// compare only the previously observed worst stage's two candidate trial curves.
// This is local evidence, never a new complete DN or an acceptance decision.
import fs from 'node:fs';
import path from 'node:path';
import v8 from 'node:v8';
import zlib from 'node:zlib';
import {createHash} from 'node:crypto';
import {pathToFileURL} from 'node:url';

const args={};
for(let i=2;i<process.argv.length;i+=2){
 if(!process.argv[i].startsWith('--')||process.argv[i+1]===undefined)throw Error('Key/value arguments required');
 args[process.argv[i].slice(2)]=process.argv[i+1];
}
for(const name of ['topic','config','warm','context','cache-root','out'])
 if(!args[name])throw Error('Missing --'+name);
if(fs.existsSync(args.out))throw Error('Choose an unused output path');
const topic=path.resolve(args.topic),scripts=path.join(topic,'scripts'),
 sourceRoot=path.join(topic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const digest=b=>createHash('sha256').update(b).digest('hex');
const read=file=>{
 const bytes=fs.readFileSync(file);
 return JSON.parse(bytes[0]===31&&bytes[1]===139?zlib.gunzipSync(bytes):bytes);
};
const load=name=>import(pathToFileURL(path.join(scripts,name)));
const {createRecalibrationFactory}=await load('closing_weighted_tail.mjs');
const {createSplitFluxCompactTailDN}=await load('fd2d-bounded-tail-stage-split.mjs');
const {createFourierRootSplitFluxEngine}=await load('78718-tail-fourier-root-split-engine.mjs');
const {prepareGeometricNodeRetraction}=await load('78718-tail-geometric-newton-retraction-centered-v3.mjs');
const {serialStageFlow}=await load('fd2d-cached-tail-stage-pool.mjs');
const cfg=read(args.config),record=read(args.warm),cp=record.checkpoint??record.response?.checkpoint;
if(!cp?.states||!cp.cutHeight)throw Error('Complete actual warm state required');
const M=cfg.modes,K=2*M,count=cp.states.length-1,
 input=new Float64Array(count*K);
for(let n=0;n<count;n++)input.set(cp.states[n+1],n*K);
const inputHash=digest(Buffer.from(input.buffer)),key=digest(args.context+'|'+inputHash+'|true'),
 directory=path.join(args['cache-root'],key),manifest=read(path.join(args['cache-root'],args.context+'-context.json'));
if(manifest.context!==args.context||manifest.count!==count||manifest.K!==K||
 manifest.stepsPerSegment!==cfg.steps||manifest.options.modes!==M||
 manifest.options.quadrature!==cfg.quadrature)throw Error('Cache configuration differs');
const flows=Array(count),blocks=[];
for(let start=0;start<count;start+=manifest.blockSize){
 const file=path.join(directory,'block-'+String(start).padStart(5,'0')+'.v8.gz'),bytes=fs.readFileSync(file),
  row=v8.deserialize(zlib.gunzipSync(bytes)),end=Math.min(count,start+manifest.blockSize);
 if(row.key!==key||row.start!==start||row.end!==end||!row.withJac||
  row.output.length!==(end-start)*K||row.jacobian.length!==(end-start)*K*K)
  throw Error('Actual retained block identity/dimensions differ');
 for(let n=start;n<end;n++){
  const j=n-start;
  flows[n]={out:row.output.subarray(j*K,(j+1)*K),J:row.jacobian.subarray(j*K*K,(j+1)*K*K),
   meanHeight:row.scalar[3*j],minA:row.scalar[3*j+1],minD:row.scalar[3*j+2]};
 }
 blocks.push({start,end,file,sha256:digest(bytes)});
}
console.log(JSON.stringify({event:'loaded-complete-actual-J',stages:count,blocks:blocks.length,inputHash,key}));
const physical=createRecalibrationFactory(cfg).assemble();
const dn=createSplitFluxCompactTailDN({...cfg,tail:physical,stageBatchEvaluator:()=>flows});
const replaced=new Set();
for(const cell of dn.tail.cells){
 if(replaced.has(cell.engine))continue;
 replaced.add(cell.engine);
 Object.assign(cell.engine,createFourierRootSplitFluxEngine({modes:M,spacing:cfg.spacing,
  quadrature:cfg.quadrature,mu:cell.mu,orientation:dn.tail.parameters.orientation,
  projectionFloor:dn.tail.parameters.projectionFloor,cuspAwareFlow:cfg.cuspAwareFlow===true}));
}
const states=cp.states.map(row=>Float64Array.from(row));
const radius=dn.tail.cells[0].profiles.at(-1)(1).r,
 target=Float64Array.from(cp.cutHeight,v=>v/radius**4),scales=new Float64Array(count+1);
scales[0]=Math.max(1e-250,...target.map(Math.abs));
for(let n=0;n<count;n++)scales[n+1]=scales[n]/Math.abs(dn.tail.gains[n][0]);
const ev=dn.tail.evaluate(states,target,true,scales);
// Exact source text, with the same helpers and lexical variables as the solver.
const core=path.join(scripts,'fd2d-bounded-tail-stage-core.mjs'),coreText=fs.readFileSync(core,'utf8'),
 helpers=coreText.slice(coreText.indexOf('function denseSolve('),coreText.indexOf('export function createCompactTailShooting(')),
 begin=coreText.indexOf(' function correction('),end=coreText.indexOf('\n function solve(',begin);
if(begin<0||end<0)throw Error('Original correction definition missing');
const correction=new Function('M','K','depth','graphs',helpers+coreText.slice(begin,end)+'\nreturn correction;')(
 M,K,count,dn.tail.graphs),cor=correction(ev,states,target),stage=Number(args.stage??ev.worst.stage);
console.log(JSON.stringify({event:'original-correction',norm:ev.norm,worst:ev.worst,
 maxChartCondition:cor.maxChartCondition,stage}));
function localNode(i){
 const cell=dn.tail.cells[i===0?0:i-1],profile=i===0?cell.profiles.at(-1):cell.profiles[0];
 return prepareGeometricNodeRetraction({engine:cell.engine,profile,x:i===0?1:0,
  state:states[i],delta:cor.delta[i],spacing:cfg.spacing,portRatio:i===0?cell.portRatio:1});
}
const geometry=[localNode(stage),localNode(stage+1)],curves=[];
let actualStageFlowCalls=0,completedStageFlowCalls=0;
for(const lambda of [1,.5,.125,.01]){
 const linear=[stage,stage+1].map(i=>Float64Array.from(states[i],(v,j)=>v+lambda*cor.delta[i][j]));
 let geometric,constructionFailure=null;
 try{geometric=geometry.map(node=>node.step(lambda,{detail:true}));}
 catch(error){constructionFailure=String(error);}
 const info={lambda,constructionFailure};
 if(geometric){
  info.maxCanonicalDifference=geometric.map((row,i)=>Math.max(...row.state.map((v,j)=>Math.abs(v-linear[i][j]))));
  info.nodeDiagnostics=geometric.map(row=>row.diagnostics);
 }
 // Only lambda=1 needs actual flow work to assess the observed slow full step.
 if(lambda===1){
  for(const [name,pair] of [['canonical',linear],['geometric',geometric?.map(row=>row.state)]]){
   if(!pair)continue;
   try{
    actualStageFlowCalls++;
    const began=performance.now(),f=serialStageFlow(dn.tail.cells[stage],pair[1],
     {withJac:false,stepsPerSegment:cfg.steps}),residual=Float64Array.from(f.out,(v,j)=>v-pair[0][j]),
     max=Math.max(...residual.map(Math.abs));
    let worst=0;for(let j=1;j<K;j++)if(Math.abs(residual[j])>Math.abs(residual[worst]))worst=j;
    completedStageFlowCalls++;
    info[name]={milliseconds:performance.now()-began,normalizedStageResidual:max/scales[stage],
     worstComponent:worst,absolute:residual[worst],scale:scales[stage],
     actualInput:Array.from(pair[1]),actualOutput:Array.from(f.out),actualNextNode:Array.from(pair[0])};
   }catch(error){info[name]={failed:String(error)};}
  }
 }
 curves.push(info);
}
const predicted=new Float64Array(K),f=flows[stage];
for(let i=0;i<K;i++){
 let sum=ev.residuals[stage][i]-cor.delta[stage][i];
 for(let j=0;j<K;j++)sum+=f.J[i*K+j]*cor.delta[stage+1][j];
 predicted[i]=sum;
}
const report={scope:'Actual cached Newton correction and two local stage flows only; no complete trial residual, DN response, BVP or metric claim',
 config:path.resolve(args.config),warm:path.resolve(args.warm),warmSHA256:digest(fs.readFileSync(args.warm)),
 core:{path:core,sha256:digest(fs.readFileSync(core))},context:args.context,inputHash,key,blocks,
 base:{norm:ev.norm,minA:ev.minA,minD:ev.minD,worst:ev.worst,maxChartCondition:cor.maxChartCondition},
 stage,normalizedLinearizedResidual:Math.max(...predicted.map(Math.abs))/scales[stage],
 deltaRows:[stage,stage+1].map(i=>({node:i,delta:Array.from(cor.delta[i])})),curves,
 actualStageFlowCalls,completedStageFlowCalls,actualNewFullJacobianFlows:0};
const output=Buffer.from(JSON.stringify(report,null,2)+'\n');
if(output.length>=1_000_000)throw Error('Unexpected report size');
fs.writeFileSync(args.out,output,{flag:'wx'});
console.log(JSON.stringify({event:'local-comparison-complete',out:args.out,bytes:output.length,sha256:digest(output),
 base:report.base,normalizedLinearizedResidual:report.normalizedLinearizedResidual,
 curves:curves.map(row=>({lambda:row.lambda,maxCanonicalDifference:row.maxCanonicalDifference,
 canonical:row.canonical?{normalizedStageResidual:row.canonical.normalizedStageResidual,failed:row.canonical.failed}:null,
 geometric:row.geometric?{normalizedStageResidual:row.geometric.normalizedStageResidual,failed:row.geometric.failed}:null}))}));
