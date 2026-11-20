// One saved tail stage -> literal physical-R Fourier two-jet data.
// Local original IVP evaluations only; no shooting solve, no boundary search.
// Planar rr finite differences are explicit parameter choices for a new
// shared-R quintic map, not certified derivatives of an exact PDE solution.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL,fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {parseArgs} from 'node:util';

const {values}=parseArgs({options:{input:{type:'string'},out:{type:'string'},
 degree:{type:'string',default:'192'},'difference-step':{type:'string',default:'0.00005'}}});
if(!values.input||!values.out)throw Error('--input and --out required');
if(fs.existsSync(values.out))throw Error('Refusing to overwrite a previous stage export');
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const packet=JSON.parse(fs.readFileSync(values.input,'utf8'));
if(packet.status!=='existing_native_flow_exact_input_states_matched')throw Error('Unbound stage packet');
const topic=packet.source_topic,src=path.join(topic,'repro/source-root/topics/large-amplitude-twist-flex/scripts');
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');process.env.CLOSING_TAIL_CACHE=src;
const module=n=>import(pathToFileURL(path.join(src,n)));
const factoryPath=path.join(topic,'scripts/closing_weighted_tail.mjs');
const subdivisionPath=path.join(topic,'scripts/950f-tail-subdivision.mjs');
for(const name of ['closing_weighted_tail.mjs','closing_recalibrated_tail.mjs','950f-tail-subdivision.mjs']){
 if(sha(path.join(topic,'scripts',name))!==packet.source_files[name])throw Error('Original source changed: '+name);
}
const {createRecalibrationFactory}=await import(pathToFileURL(factoryPath));
const {subdividePhysical}=await import(pathToFileURL(subdivisionPath));
const {createFastSplitFluxMomentumTailEngine}=await module('f6tail_fast_split_flux_engine.mjs');
const {withCuspAwareRK}=await module('f6tail_cusp_grid.mjs');
const {createRelativeSpatialJetEvaluator}=await module('f6tail_relative_spatial_jets.mjs');
const p=packet.checkpoint.config,scope=packet.finite_scope,M=scope.M,N=scope.quadrature,K=2*M;
const degree=Number(values.degree),dh=Number(values['difference-step']);
if(N<2*degree+4||N!==512||M!==24||scope.spacing!==3)throw Error('Unexpected selected finite scope');
const started=performance.now(),factory=createRecalibrationFactory(p),physical=factory.assemble();
const stages=subdividePhysical(physical,p.depth,p.shootingParts),index=packet.stage.stage;
const cell=stages.cells[index],profile=cell.profiles[0];
for(const key of ['rawCell','rawSegment','rawLeft','rawRight','portRatio','mu']){
 if(cell[key]!==packet.stage[key])throw Error('Stage source coordinate changed: '+key);
}
let engine=createFastSplitFluxMomentumTailEngine({modes:M,spacing:scope.spacing,quadrature:N,
 mu:cell.mu,orientation:scope.orientation,projectionFloor:scope.projectionFloor});
engine=withCuspAwareRK(engine);
const evaluator=createRelativeSpatialJetEvaluator(engine,{spacing:scope.spacing,radialDifferenceStep:dh});
const evaluator2=createRelativeSpatialJetEvaluator(engine,{spacing:scope.spacing,radialDifferenceStep:2*dh});
const modes=[];for(let m=-degree;m<=degree;m++)if((m-1)%3===0)modes.push(m);
const heightModes=Array.from({length:M+1},(_,j)=>3*j),P=modes.length,C=P+M+1;
const trig=modes.map(m=>({cos:Float64Array.from({length:N},(_,n)=>Math.cos(2*Math.PI*n*m/N)),
 sin:Float64Array.from({length:N},(_,n)=>Math.sin(2*Math.PI*n*m/N))}));
function pack(a,state){
 const out=Array.from({length:3},()=>Array(C).fill(0));
 for(let derivative=0;derivative<3;derivative++){
  const name=['V','Vr','Vrr'][derivative];
  for(let k=0;k<P;k++){
   let sum=0;for(let n=0;n<N;n++)sum+=a.perAngle[n][name][0]*trig[k].cos[n]+a.perAngle[n][name][1]*trig[k].sin[n];
   out[derivative][k]=sum/N;
  }
 }
 const {g,root,field,heightJets:j}=a,sigma=g.drdx/g.r;
 out[0][P]=state[K];out[1][P]=g.w*root.L[0];
 out[2][P]=g.w*(j.Ldot[0]+g.dlogwdx*root.L[0])/g.drdx;
 for(let k=0;k<M;k++){
  const m=heightModes[k+1],i=P+k+1;
  out[0][i]=g.r**4*state[k];
  out[1][i]=m*m*g.r**3*state[k]+Math.sqrt(2)*g.w*root.L[k+1];
  out[2][i]=(m*m*g.r**3*(field[k]+3*sigma*state[k])+
   Math.sqrt(2)*g.w*(j.Ldot[k+1]+g.dlogwdx*root.L[k+1]))/g.drdx;
 }
 return out;
}
function projectionError(a,coeff){
 const error=[0,0,0];
 for(let d=0;d<3;d++)for(let n=0;n<N;n++){
  let x=0,y=0;for(let k=0;k<P;k++){x+=coeff[d][k]*trig[k].cos[n];y+=coeff[d][k]*trig[k].sin[n];}
  const v=a.perAngle[n][['V','Vr','Vrr'][d]];error[d]=Math.max(error[d],Math.hypot(x-v[0],y-v[1]));
 }
 return error;
}
function point(state,x,kind){
 const a=evaluator.evaluate(state,profile,x),coeff=pack(a,state);
 const result={kind,xi:x,sourceX:cell.rawLeft+(cell.rawRight-cell.rawLeft)*x,
  radiusJS:a.g.r,backgroundJS:{w:a.g.w,wR:a.g.w*a.g.dlogwdx/a.g.drdx,E:a.g.E},
  coefficients:coeff,sourceMetric:a.development.actualMetricRelativeOperatorError,
  sourceHeightDarboux:a.heightJets.maxDarboux,projectionError:projectionError(a,coeff),
  rootRelativeResidual:a.root.err/a.root.scale,minRootD:a.root.e.minD,minLeading:a.root.e.minA,
  meanPerturbation:state[K],meanBackground:state[K+1],
  physicalHeight:Array.from(state.slice(0,M),(u)=>a.g.r**4*u)};
 console.log(JSON.stringify({kind,x,r:result.radiusJS,sourceMetric:result.sourceMetric,
  projectionError:result.projectionError,seconds:(performance.now()-started)/1000}));
 return result;
}
const grid=packet.stage.profileGrids[0];
let state=new Float64Array(K+2);state.set(packet.state_inner);state[K]=packet.inner_mean_perturbation_and_background[0];state[K+1]=packet.inner_mean_perturbation_and_background[1];
const states=[Float64Array.from(state)],xs=[0];
for(const step of grid){
 if(Math.abs(step.x-xs.at(-1))>2e-16)throw Error('Noncontiguous original RK grid');
 state=engine.rk4(state,profile,step.x,step.h);states.push(Float64Array.from(state));xs.push(step.x+step.h);
}
const replayEnd=Float64Array.from(state),targetEnd=new Float64Array(K+2);
for(let j=0;j<K;j++)targetEnd[j]=packet.state_outer[j]*(j<M?1:cell.portRatio);
for(let j=0;j<2;j++)targetEnd[K+j]=packet.inner_mean_perturbation_and_background[j]+packet.native_stage_output[K+j];
states[states.length-1]=targetEnd;
const nodes=[],midpoints=[];
for(let i=0;i<xs.length;i++){
 nodes.push(point(states[i],xs[i],'node'));
 if(i<grid.length){const x=(xs[i]+xs[i+1])/2,s=engine.rk4(states[i],profile,xs[i],x-xs[i]);midpoints.push(point(s,x,'midpoint'));}
}
if(nodes.some((v,i)=>i&&!(v.radiusJS>nodes[i-1].radiusJS)))throw Error('Literal radius mesh is not strictly increasing');
const cuspIndex=xs.findIndex(x=>x>0&&x<1&&profile.integrationBreakpoints?.some(t=>Math.abs(t-x)<1e-15));
let secondStepComparison=null;
if(cuspIndex>=0){
 const a=evaluator2.evaluate(states[cuspIndex],profile,xs[cuspIndex]),twice=pack(a,states[cuspIndex]),first=nodes[cuspIndex].coefficients;
 secondStepComparison={node:cuspIndex,xi:xs[cuspIndex],planarRRMaximumCoefficientDifference:
  Math.max(...first[2].slice(0,P).map((v,j)=>Math.abs(v-twice[2][j]))),scope:'FD stability diagnostic only; both sets are possible finite literal choices.'};
}
const names=['f6tail_relative_spatial_jets.mjs','f6tail_relative_development.mjs',
 'f6tail_momentum_physical_jets.mjs','f6tail_fast_split_flux_engine.mjs','f6tail_momentum_split_flux.mjs','f6tail_cusp_grid.mjs'];
const sourcePaths=[fileURLToPath(import.meta.url),factoryPath,subdivisionPath,...names.map(n=>path.join(src,n))];
const result={status:'existing_stage_literal_R_two_jet_data_exported',input:path.resolve(values.input),inputSHA256:sha(values.input),
 sourceSHA256:Object.fromEntries(sourcePaths.map(p=>[p,sha(p)])),stage:index,rawCell:cell.rawCell,rawSegment:cell.rawSegment,
 rawLeft:cell.rawLeft,rawRight:cell.rawRight,finiteScope:scope,degree,planarModes:modes,heightModes,
 physicalParameters:physical.parameters,physicalStats:physical.stats,
 coordinateDefinition:'Each radiusJS number is an explicitly chosen exact binary-real knot of the new R-quintic map, not the midpoint of a true-R interval. Source x and xi are retained only as data provenance.',
 coefficientDefinition:'Coefficients are exact binary-real nodal values, physical-R first and second derivatives. Standard shared quintic Hermite interpolation in R will define the new finite C2 perturbation. Planar rr data use the recorded FD formula; this is not an exact PDE-derivative claim.',
 meanDefinition:'Perturbation mean at the inner endpoint is the original saved native increment sum. The outer endpoint uses the same saved stage increment. Interior values are the original RK replay. The target background primitive must be supplied separately; do not add the background mean slot to the perturbation twice.',
 heightDefinition:'Nonzero physical H is r_JS^4 u at each source datum, not true_R^4 u.',
 nodes,midpoints,secondStepComparison,
 originalReplayEndVsNative:{first48MaximumAbsoluteDifference:Math.max(...Array.from(replayEnd.slice(0,K),(v,j)=>Math.abs(v-packet.native_stage_output[j]))),
  meanIncrementDifferences:Array.from({length:2},(_,j)=>replayEnd[K+j]-packet.inner_mean_perturbation_and_background[j]-packet.native_stage_output[K+j])},
 maximumSourceMetric:Math.max(...nodes.concat(midpoints).map(v=>v.sourceMetric)),
 maximumPlanarProjectionErrors:Array.from({length:3},(_,j)=>Math.max(...nodes.concat(midpoints).map(v=>v.projectionError[j]))),
 bvpSolvesExecuted:0,shootingIterationsExecuted:0,localExistingIVPReplayed:true,
 seconds:(performance.now()-started)/1000};
fs.writeFileSync(values.out,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.status,nodes:nodes.length,midpoints:midpoints.length,
 maximumSourceMetric:result.maximumSourceMetric,maximumPlanarProjectionErrors:result.maximumPlanarProjectionErrors,
 secondStepComparison,seconds:result.seconds,outputSHA256:sha(values.out)}));
