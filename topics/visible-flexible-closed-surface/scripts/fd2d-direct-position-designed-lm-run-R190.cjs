'use strict';
// Actual continuation of a saved state. Every trial uses the complete provider.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const {createR187}=require('./fd2d-direct-position-tangent-lift-baseline-R187.cjs');
const {createR190Provider}=require('./fd2d-direct-position-designed-metric-provider-R190.cjs');
const {lmStep}=require('./fd2d_dense_normal_lm.cjs');
const sha=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const atomic=(p,x)=>{const q=p+'.tmp';fs.writeFileSync(q,JSON.stringify(x,null,2)+'\n');fs.renameSync(q,p);};
async function main(){
 const [input,stem,stepsText='10']=process.argv.slice(2),steps=Number(stepsText);
 if(!input||!stem||!Number.isInteger(steps)||steps<1)throw Error('input-state output-stem positive-step-count');
 if(fs.existsSync(stem+'-report.json')||fs.existsSync(stem+'-progress.json'))throw Error('Use a fresh output stem');
 const old=JSON.parse(fs.readFileSync(input,'utf8'));
 const bundle=path.join(__dirname,'../notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json');
 const engine=createR187(),provider=createR190Provider(engine,JSON.parse(fs.readFileSync(bundle,'utf8')),old.options);
 if(old.z.length!==provider.dimension)throw Error('State layout mismatch');
 const identity={source:sha(__filename),engine:sha(path.join(__dirname,'fd2d-direct-position-tangent-lift-baseline-R187.cjs')),provider:sha(path.join(__dirname,'fd2d-direct-position-designed-metric-provider-R190.cjs')),lm:sha(path.join(__dirname,'fd2d_dense_normal_lm.cjs')),input:sha(input),bundle:sha(bundle)};
 let z=Array.from(old.z),lambda=old.lambda,iteration=old.iteration;
 const history=[],start=new Date().toISOString(),t0=process.hrtime.bigint();
 fs.mkdirSync(path.dirname(stem),{recursive:true});
 for(let j=0;j<steps;j++){
  const tick=process.hrtime.bigint(),normal=provider.normal(z);
  const step=await lmStep({z,normal,value:v=>provider.value(v),lambda,maxDampingAttempts:8,alphas:[1,.5,.25]});
  const r={iteration:iteration+1,accepted:step.accepted,status:step.status,baselineSquaredNorm:normal.squaredNorm,squaredNorm:step.squaredNorm,lambda:step.lambda,nextLambda:step.nextLambda,alpha:step.alpha??null,evaluation:step.evaluation??null,trace:step.trace,solveInfo:step.solveInfo??step.lastSolveInfo,actualValueEvaluations:step.actualValueEvaluations,seconds:Number(process.hrtime.bigint()-tick)/1e9};
  history.push(r);
  if(step.accepted){z=Array.from(step.z);lambda=step.nextLambda;iteration++;}
  atomic(stem+'-progress.json',{kind:'R190-actual-Node-LM-progress-v1',start,identity,options:old.options,z,lambda,iteration,history,continuousCertificate:false,strongTargetComplete:false});
  console.log(JSON.stringify({iteration:r.iteration,accepted:r.accepted,R2:r.squaredNorm,metric:r.evaluation?.maxRelativeMetric,immersion:r.evaluation?.minImmersion,lambda:r.lambda,alpha:r.alpha,trials:r.actualValueEvaluations,cutHeight:provider.base.height+z[provider.definition.stateLayout.cutHeight],seconds:r.seconds}));
  if(!step.accepted)break;
 }
 const report={kind:'R190-actual-Node-LM-checkpoint-v1',start,end:new Date().toISOString(),executionRuntime:'Node actual terminal process',identity,options:old.options,z,lambda,iteration,history,seconds:Number(process.hrtime.bigint()-t0)/1e9,continuousCertificate:false,strongTargetComplete:false};
 atomic(stem+'-report.json',report);
}
main().catch(e=>{console.error(e.stack||String(e));process.exitCode=1;});
