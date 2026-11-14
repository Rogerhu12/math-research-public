"use strict";
function createR203RunProvider(candidate,input){
 const {createR187}=require("./fd2d-direct-position-tangent-lift-baseline-R187.cjs");
 const {createR196CubicSplines}=require("./fd2d-cubic-spline-refinement-R196.cjs");
 const {createR196MetricProvider}=require("./fd2d-nonuniform-metric-provider-R196.cjs");
 const {createR196CurvatureProvider}=require("./fd2d-nonuniform-curvature-provider-R196.cjs");
 const {createR191Algebra}=require("./fd2d-position-curvature-chain-R191.cjs");
 const {createR203GeometryProvider}=require("./fd2d-complete-position-geometric-guide-R203.cjs");
 const e=createR187(),core=createR196MetricProvider(e,candidate,input.options,createR196CubicSplines());
 const curv=createR196CurvatureProvider(e,core,input.guide||input.curvatureOptions,createR191Algebra());
 const provider=createR203GeometryProvider(curv,input.geometryGuide);
 const lm=require("./fd2d_band_border_lm_adapter_v2_R195.cjs").createBandBorderLM(require("./fd2d_scaled_band_border_lm_v2_R195.cjs"),provider.definition,{halfBandwidthBlocks:4});
 return {core,curv,provider,lm};
}
async function continueR203(candidate,input,count,config={}){
 if(!Number.isInteger(count)||count<1)throw Error("Positive number of actual steps required");
 const {core,provider,lm}=createR203RunProvider(candidate,input);
 let z=Array.from(input.z),lambda=input.lambda,iteration=input.iteration||0;
 const history=Array.from(input.history||[]),started=new Date().toISOString(),tick=Date.now();
 function snapshot(){return {...input,schema:"R203-actual-complete-geometry-continuation-v1",z,lambda,iteration,history,
  actualFiniteCutHeight:core.base.height+z[core.definition.stateLayout.cutHeight],
  execution:{runtime:config.runtime||"unspecified caller",start:started,updated:new Date().toISOString(),elapsedSeconds:(Date.now()-tick)/1000},
  physicalMetricIsDesignVariable:true,continuousCertificate:false,strongTargetComplete:false};}
 for(let k=0;k<count;k++){
  const t=Date.now(),normal=provider.normal(z),normalSeconds=(Date.now()-t)/1000;
  const step=await lm.lmStep({z,normal,value:v=>provider.value(v),lambda,maxDampingAttempts:8,alphas:[1,.5,.25]});
  const r={iteration:iteration+1,accepted:step.accepted,status:step.status,baselineSquaredNorm:normal.squaredNorm,
   squaredNorm:step.squaredNorm,lambda:step.lambda,nextLambda:step.nextLambda,alpha:step.alpha??null,
   evaluation:step.evaluation??null,trace:step.trace,solveInfo:step.solveInfo??step.lastSolveInfo,
   actualValueEvaluations:step.actualValueEvaluations,normalSeconds,elapsedSeconds:(Date.now()-t)/1000};
  history.push(r);if(step.accepted){z=Array.from(step.z);lambda=step.nextLambda;iteration++;}
  if(config.onStep)await config.onStep(snapshot(),r);
  if(!step.accepted)break;
 }
 return snapshot();
}
module.exports={createR203RunProvider,continueR203};
if(require.main===module){
 const fs=require("node:fs"),path=require("node:path"),[inputPath,candidatePath,stem,countText="4"]=process.argv.slice(2);
 if(!inputPath||!candidatePath||!stem)throw Error("Usage: input.json candidate.json fresh-output-stem count");
 if(fs.existsSync(stem+"-report.json")||fs.existsSync(stem+"-progress.json"))throw Error("Fresh output stem required");
 const input=JSON.parse(fs.readFileSync(inputPath)),candidate=JSON.parse(fs.readFileSync(candidatePath));
 const atomic=(p,x)=>{fs.mkdirSync(path.dirname(p),{recursive:true});fs.writeFileSync(p+".tmp",JSON.stringify(x,null,2)+"\n");fs.renameSync(p+".tmp",p);};
 continueR203(candidate,input,Number(countText),{runtime:"Node actual terminal child; actual exit belongs to external receipt",onStep:(s,r)=>{atomic(stem+"-progress.json",s);console.log(JSON.stringify({iteration:r.iteration,accepted:r.accepted,R2:r.squaredNorm,metric:r.evaluation?.maxRelativeMetric,curvature:r.evaluation?.curvature?.maxCurvature,geometry:r.evaluation?.geometryPenaltySquaredNorm,cut:s.actualFiniteCutHeight}));}}).then(r=>atomic(stem+"-report.json",r)).catch(e=>{console.error(e.stack||e);process.exitCode=1;});
}
