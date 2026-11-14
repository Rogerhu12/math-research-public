// One saved stage only: original/tight roots and production with/without-J paths.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';
const opt={},args=process.argv.slice(2);
for(let k=0;k<args.length;k+=2){if(!args[k].startsWith('--')||args[k+1]===undefined)throw Error('key/value arguments required');opt[args[k].slice(2)]=args[k+1];}
if(!opt.snapshot||!opt.config||!opt.out||fs.existsSync(opt.out))throw Error('--snapshot --config and fresh --out required');
const here=path.dirname(fileURLToPath(import.meta.url)),sourceRoot=path.resolve(opt['source-root']??process.env.VISIBLE_FLEX_SOURCE_ROOT??path.join(here,'../repro/source-root'));
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import('./closing_weighted_tail.mjs');
const {subdividePhysical}=await import('./950f-tail-subdivision.mjs');
const {createFourierRootSplitFluxEngine}=await import('./78718-tail-fourier-root-split-engine.mjs');
const {createFourierTightRootSplitFluxEngine}=await import('./78718-tail-fourier-root-tight-split-engine.mjs');
const {integrationGrid,splitIntegrationInterval}=await import(pathToFileURL(path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs')));
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
function read(p){const b=fs.readFileSync(p);return {object:JSON.parse(b[0]===31&&b[1]===139?zlib.gunzipSync(b):b),identity:{path:path.resolve(p),bytes:b.length,sha256:sha(b)}};}
const started=Date.now(),input=read(opt.snapshot),config=read(opt.config),snap=input.object,cfg=config.object,cp=snap.checkpoint;
const M=cfg.modes,N=cfg.quadrature,K=2*M,steps=cfg.steps,stage=snap.iteration.worst.stage,component=snap.iteration.worst.component,scale=snap.iteration.worst.scale;
const physical=createRecalibrationFactory(cfg).assemble(),tail=subdividePhysical(physical,cfg.depth,cfg.shootingParts),cell=tail.cells[stage];
if(cp.parameters.modes!==M||cp.parameters.quadrature!==N||cp.states.length!==tail.cells.length+1)throw Error('snapshot/config stage mismatch');
const options={modes:M,quadrature:N,spacing:cfg.spacing,mu:cell.mu,orientation:cfg.orientation,
 projectionFloor:cfg.projectionFloor??.05,cuspAwareFlow:cfg.cuspAwareFlow===true};
const initial=new Float64Array(K+2);initial.set(cp.states[stage+1]);
const cuts=cell.profiles[0].integrationBreakpoints??[],jacGrid=integrationGrid(steps,cuts),plainGrid=[0];
for(let k=0;k<steps;k++){const sub=splitIntegrationInterval(k/steps,(k+1)/steps,cuts);plainGrid.push(...sub.slice(1));}
const results=[],states=new Map();
for(const [precision,factory] of [['original',createFourierRootSplitFluxEngine],['tight',createFourierTightRootSplitFluxEngine]]){
 for(const withJac of [true,false]){
  const engine=factory(options),begin=performance.now(),key=precision+'-'+(withJac?'jac':'plain');
  try{
   let f;
   if(withJac)f=engine.flowStateWithJacobian(initial,cell.profiles,{stepsPerSegment:steps});
   else{
    let state=Float64Array.from(initial);
    for(const profile of cell.profiles)for(let k=0;k<steps;k++)state=engine.rk4(state,profile,k/steps,1/steps);
    f={state};
   }
   const out=Float64Array.from(f.state.slice(0,K),(v,j)=>j<M?v:v/cell.portRatio),residual=Float64Array.from(out,(v,j)=>v-cp.states[stage][j]);
   let worst=0;for(let j=1;j<K;j++)if(Math.abs(residual[j])>Math.abs(residual[worst]))worst=j;
   let tangentMaximum=null,tangentInfinity=null,targetRowL1=null,targetRowMax=null;
   if(withJac){
    tangentMaximum=0;tangentInfinity=0;targetRowL1=0;targetRowMax=0;
    for(let i=0;i<K;i++){
     let rowSum=0;for(let j=0;j<K;j++){
      const value=Math.abs(f.tangent[i*K+j]/(i<M?1:cell.portRatio));
      rowSum+=value;tangentMaximum=Math.max(tangentMaximum,value);
      if(i===component){targetRowL1+=value;targetRowMax=Math.max(targetRowMax,value);}
     }
     tangentInfinity=Math.max(tangentInfinity,rowSum);
    }
   }
   const high=[];for(let j=Math.max(0,M-6);j<M;j++)high.push({frequency:cfg.spacing*(j+1),
    qResidual:residual[j],piResidual:residual[M+j],normalizedPiResidual:Math.abs(residual[M+j])/scale});
   states.set(key,{out,mean:f.state[K]+f.state[K+1]});
   results.push({key,ok:true,precision,withJac,milliseconds:performance.now()-begin,
    minimumLeading:f.minA??null,minimumD:f.minD??null,maximumRootRelative:f.maxRootRelative??null,
    maximumAbsoluteResidual:Math.abs(residual[worst]),normalizedStageResidual:Math.abs(residual[worst])/scale,
    worstComponent:worst,worstFrequency:cfg.spacing*((worst%M)+1),
    savedWorstComponent:component,savedWorstComponentResidual:residual[component],
    savedWorstComponentNormalized:Math.abs(residual[component])/scale,
    savedWorstAbsoluteReplayDifference:Math.abs(residual[component])-snap.iteration.worst.absolute,
    highModes:high,tangentMaximum,tangentInfinity,targetComponentTangentL1:targetRowL1,targetComponentTangentMaximum:targetRowMax});
  }catch(error){results.push({key,ok:false,precision,withJac,milliseconds:performance.now()-begin,error:String(error)});}
 }
}
const comparisons=[];
for(const [a,b] of [['original-jac','original-plain'],['tight-jac','tight-plain'],['original-jac','tight-jac'],['original-plain','tight-plain']]){
 if(!states.has(a)||!states.has(b))continue;
 const left=states.get(a),right=states.get(b);let maximum=0,worst=0,nonzero=0;
 for(let j=0;j<K;j++){
  const d=Math.abs(left.out[j]-right.out[j]);if(d!==0)nonzero++;if(d>maximum){maximum=d;worst=j;}
 }
 comparisons.push({a,b,maximumStateDifference:maximum,normalizedStateDifference:maximum/scale,
  worstComponent:worst,worstFrequency:cfg.spacing*((worst%M)+1),nonzeroComponents:nonzero,
  savedWorstComponentDifference:left.out[component]-right.out[component],
  meanHeightDifference:left.mean-right.mean});
}
const sourceFiles=['78718-tail-fourier-root-momentum.mjs','78718-tail-fourier-root-tight-momentum.mjs',
 '78718-tail-fourier-root-split-engine.mjs','78718-tail-fourier-root-tight-split-engine.mjs',
 '78718-tail-fourier-product-jacobian.mjs','78718-tail-fourier-product-flow.mjs',
 '78718-tail-tangent-core.mjs','950f-tail-subdivision.mjs','closing_weighted_tail.mjs','closing_recalibrated_tail.mjs'];
const report={scope:'Exactly one actual saved stage and its S32 production state-flow branches; no new shooting solve or BVP. Comparison of original/tight roots and withJac=true/false paths. State arrays and tangent matrices are not printed or stored in this scalar report.',
 input:input.identity,config:config.identity,iteration:snap.iteration,stage,rawCell:cell.rawCell,rawSegment:cell.rawSegment,
 part:cell.part,inputNode:stage+1,targetNode:stage,portRatio:cell.portRatio,modes:M,quadrature:N,steps,
 cuspAwareFlow:options.cuspAwareFlow,breakpointCount:cuts.length,
 jacobianGridSHA256:sha(JSON.stringify(jacGrid)),plainGridSHA256:sha(JSON.stringify(plainGrid)),
 gridsExactlyEqual:JSON.stringify(jacGrid)===JSON.stringify(plainGrid),integrationSubsteps:jacGrid.length-1,
 scriptSHA256:sha(fs.readFileSync(fileURLToPath(import.meta.url))),
 sourceSHA256:Object.fromEntries(sourceFiles.map(f=>[f,sha(fs.readFileSync(path.join(here,f)))])),
 cuspSourceSHA256:sha(fs.readFileSync(path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs'))),
 results,comparisons,actualStageFlows:results.length,actualShootingSolves:0,actualBVPCalls:0,seconds:(Date.now()-started)/1000};
fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({out:path.resolve(opt.out),bytes:fs.statSync(opt.out).size,
 flows:results.map(v=>({key:v.key,ok:v.ok,normalizedStageResidual:v.normalizedStageResidual,maxRootRelative:v.maximumRootRelative})),comparisons,seconds:report.seconds}));
