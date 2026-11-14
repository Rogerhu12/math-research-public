// Continue only the two recorded R95 stage35 entry states on one physical
// substage, with the original finite RHS. No shooting/DN/BVP is performed.
import fs from 'node:fs';import path from 'node:path';import zlib from 'node:zlib';import crypto from 'node:crypto';
import {pathToFileURL,fileURLToPath} from 'node:url';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {subdividePhysical} from './950f-tail-subdivision.mjs';
import {createFourierRootSplitFluxEngine} from './78718-tail-fourier-root-split-engine.mjs';
import {prepareGeometricNodeRetraction} from './78718-tail-geometric-newton-retraction-v2.mjs';
const {integrationGrid}=await import(pathToFileURL(path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs')));
const args=process.argv.slice(2),opt={};for(let k=0;k<args.length;k+=2)opt[args[k].replace(/^--/,'')]=args[k+1];
if(!opt.config||!opt.trial||!opt.out||fs.existsSync(opt.out))throw Error('Inputs and fresh output required');
const inputs=[];function read(p){const b=fs.readFileSync(p);inputs.push({path:path.resolve(p),bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});return JSON.parse(p.endsWith('.gz')?zlib.gunzipSync(b):b);}
function identity(p){if(p instanceof URL)p=fileURLToPath(p);const b=fs.readFileSync(p);return {path:path.resolve(p),bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};}
const start=Date.now(),cfg=read(opt.config),trial=read(opt.trial),prior=read(cfg.initialCheckpoint).response.checkpoint,
 physical=createRecalibrationFactory(cfg).assemble(),stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts),
 stage=trial.stage,node=stage+1,cell=stages.cells[stage],profile=cell.profiles[0],M=cfg.modes,K=2*M,N=cfg.quadrature,
 options={modes:M,spacing:cfg.spacing,quadrature:N,mu:cell.mu,orientation:cfg.orientation,projectionFloor:1e-10},
 engine=createFourierRootSplitFluxEngine(options),oldM=prior.parameters.modes,
 oldEngine=createFourierRootSplitFluxEngine({...options,modes:oldM,quadrature:prior.parameters.quadrature}),
 oldState=new Float64Array(2*oldM+2),extended=new Float64Array(K);
oldState.set(prior.states[node]);
const oldRoot=oldEngine.root(oldState,profile,0),raw=oldEngine.toRaw(oldState,profile,0,oldRoot).raw;
for(let j=0;j<oldM;j++){extended[j]=raw[j];extended[M+j]=raw[oldM+j];}
const base=engine.initializeFromRaw(extended,profile,0).state.slice(0,K),lambda=trial.trial.step,
 delta=Float64Array.from(base,(v,j)=>(trial.inputState[j]-v)/lambda),
 prepared=prepareGeometricNodeRetraction({engine,profile,x:0,state:base,delta,spacing:cfg.spacing}),
 retracted=prepared.step(lambda).state;

function requiredCurvature(root){
 const g=root.g,Kg=g.w2*g.dlogwdx/(g.drdx*g.r*g.E*g.E);let max=0;
 for(const v of root.e.rows){const b=g.w*v.U/(g.r*v.sd),c=g.w*v.A/(g.r*Math.sqrt(g.E)*v.sd),
  a=(Kg+b*b)/c,norm=(Math.abs(a+c)+Math.sqrt((a-c)**2+4*b*b))/2;max=Math.max(max,norm);}
 return max;
}
function walk(initial,steps,label){
 let state=new Float64Array(K+2);state.set(initial);const grid=integrationGrid(steps,profile.integrationBreakpoints??[]),
  rows=[],progress={lastCompletedX:0,fields:0,minA:Infinity,minD:Infinity,minS:Infinity,maxGaussRequiredCurvature:0};
 let failed=null;
 function field(y,x,step,phase){
  let root;
  try{root=engine.root(y,profile,x);}catch(error){failed={x,step,phase,error:String(error),state:Array.from(y)};throw error;}
  const curvature=requiredCurvature(root);progress.fields++;
  progress.minA=Math.min(progress.minA,root.e.minA);progress.minD=Math.min(progress.minD,root.e.minD);progress.minS=Math.min(progress.minS,root.e.minS);
  progress.maxGaussRequiredCurvature=Math.max(progress.maxGaussRequiredCurvature,curvature);
  rows.push({x,step,phase,minA:root.e.minA,minD:root.e.minD,minS:root.e.minS,gaussRequiredCurvature:curvature});
  return engine.rhs(y,profile,x,false,root);
 }
 try{
  for(let i=0;i<grid.length-1;i++){
   const x=grid[i],h=grid[i+1]-x,a=field(state,x,i,'a'),t=new Float64Array(K+2);
   for(let j=0;j<K+2;j++)t[j]=state[j]+h*a[j]/2;
   const b=field(t,x+h/2,i,'b');for(let j=0;j<K+2;j++)t[j]=state[j]+h*b[j]/2;
   const c=field(t,x+h/2,i,'c');for(let j=0;j<K+2;j++)t[j]=state[j]+h*c[j];
   const d=field(t,x+h,i,'d');state=Float64Array.from(state,(v,j)=>v+h*(a[j]+2*b[j]+2*c[j]+d[j])/6);
   progress.lastCompletedX=grid[i+1];
  }
  const end=engine.root(state,profile,1);
  return {label,steps,completed:true,...progress,endMinA:end.e.minA,endState:Array.from(state),fields:rows};
 }catch(error){return {label,steps,completed:false,...progress,failure:failed??{error:String(error)},fields:rows};}
}
const rows=[];for(const steps of [32,64])for(const [label,state]of[['original_pi_trial8',trial.inputState],['same_direction_Q_L_retraction',retracted]])rows.push(walk(state,steps,label));
const report={scope:'One finite W22 physical substage from two actual-trial-related entry states; lower floor only for this local exploration, no full DN or whole metric certificate.',
 inputs,script:identity(new URL('78718-tail-retraction-local-stage.mjs',import.meta.url)),helper:identity(new URL('78718-tail-geometric-newton-retraction-v2.mjs',import.meta.url)),
 M,N,stage,node,lambda,localProjectionFloor:1e-10,originalProjectionFloor:.05,rows,
 DN_calls:0,BVP_calls:0,shooting_residual_evaluations:0,production_changed:false,seconds:(Date.now()-start)/1000};
fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({output:identity(opt.out),stage,node,rows:rows.map(v=>({label:v.label,steps:v.steps,completed:v.completed,lastCompletedX:v.lastCompletedX,minA:v.minA,minD:v.minD,maxGaussRequiredCurvature:v.maxGaussRequiredCurvature,failure:v.failure?{x:v.failure.x,step:v.failure.step,phase:v.failure.phase,error:v.failure.error}:null})),seconds:report.seconds}));
