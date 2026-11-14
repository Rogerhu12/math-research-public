"use strict";
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const {createR187}=require("./fd2d-direct-position-tangent-lift-baseline-R187.cjs");
const {createR191Algebra}=require("./fd2d-position-curvature-chain-R191.cjs");
const {createR196CubicSplines}=require("./fd2d-cubic-spline-refinement-R196.cjs");
const {createR196MetricProvider}=require("./fd2d-nonuniform-metric-provider-R196.cjs");
const {createR196CurvatureProvider}=require("./fd2d-nonuniform-curvature-provider-R196.cjs");
const kernel=require("./fd2d_scaled_band_border_lm_v2_R195.cjs");
const {createBandBorderLM}=require("./fd2d_band_border_lm_adapter_v2_R195.cjs");
const sha=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
function atomic(p,v){const q=p+".tmp";fs.writeFileSync(q,JSON.stringify(v,null,2)+"\n");fs.renameSync(q,p);}
async function main(){
 const [input,stem,countText="4"]=process.argv.slice(2),count=Number(countText);
 if(!input||!stem||!Number.isInteger(count)||count<1)throw Error("input output-stem positive-steps required");
 if(fs.existsSync(stem+"-report.json")||fs.existsSync(stem+"-progress.json"))throw Error("Use a fresh output stem");
 const old=JSON.parse(fs.readFileSync(input,"utf8")),guide=old.guide||old.curvatureOptions;
 const candidate=path.join(__dirname,"../notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json");
 const engine=createR187(),core=createR196MetricProvider(engine,JSON.parse(fs.readFileSync(candidate,"utf8")),old.options,createR196CubicSplines());
 const provider=createR196CurvatureProvider(engine,core,guide,createR191Algebra());
 if(old.z.length!==provider.dimension)throw Error("Complete state dimension mismatch");
 const lm=createBandBorderLM(kernel,provider.definition,{halfBandwidthBlocks:4,kernelSourceSHA256:sha(path.join(__dirname,"fd2d_scaled_band_border_lm_v2_R195.cjs"))});
 const names=["fd2d-direct-position-tangent-lift-baseline-R187.cjs","fd2d-position-curvature-chain-R191.cjs","fd2d-cubic-spline-refinement-R196.cjs","fd2d-nonuniform-metric-provider-R196.cjs","fd2d-nonuniform-curvature-provider-R196.cjs","fd2d_scaled_band_border_lm_v2_R195.cjs","fd2d_band_border_lm_adapter_v2_R195.cjs",path.basename(__filename)];
 const identity={inputPath:input,inputSHA256:sha(input),candidateSHA256:sha(candidate),sourceSHA256:Object.fromEntries(names.map(x=>[x,sha(path.join(__dirname,x))]))};
 let z=Array.from(old.z),lambda=old.lambda,iteration=old.iteration??old.localAcceptedSteps??0;
 const start=new Date().toISOString(),tick=process.hrtime.bigint(),history=[];
 fs.mkdirSync(path.dirname(stem),{recursive:true});
 function snapshot(){return {schema:"R196-actual-Node-nonuniform-continuation-v1",execution:{runtime:"Node in actual terminal process",start,updated:new Date().toISOString(),elapsedSeconds:Number(process.hrtime.bigint()-tick)/1e9},identity,options:old.options,guide,centralSeed:old.centralSeed,z,lambda,iteration,parentInitialIteration:old.iteration??old.localAcceptedSteps??0,history,backendDefinition:lm.backendDefinition,actualCutHeight:core.base.height+z[core.definition.stateLayout.cutHeight],completePhysicalMetricFixedDuringDesign:false,continuousCertificate:false,strongTargetComplete:false};}
 for(let j=0;j<count;j++){
  const t=process.hrtime.bigint(),normal=provider.normal(z),normalSeconds=Number(process.hrtime.bigint()-t)/1e9;
  const step=await lm.lmStep({z,normal,value:v=>provider.value(v),lambda,maxDampingAttempts:8,alphas:[1,.5,.25]});
  const rec={iteration:iteration+1,accepted:step.accepted,status:step.status,baselineSquaredNorm:normal.squaredNorm,squaredNorm:step.squaredNorm,lambda:step.lambda,nextLambda:step.nextLambda,alpha:step.alpha??null,evaluation:step.evaluation??null,trace:step.trace,solveInfo:step.solveInfo??step.lastSolveInfo,actualValueEvaluations:step.actualValueEvaluations,normalSeconds,elapsedSeconds:Number(process.hrtime.bigint()-t)/1e9};
  history.push(rec);if(step.accepted){z=Array.from(step.z);lambda=step.nextLambda;iteration++;}
  atomic(stem+"-progress.json",snapshot());
  console.log(JSON.stringify({iteration:rec.iteration,accepted:rec.accepted,R2:rec.squaredNorm,metric:rec.evaluation?.maxRelativeMetric,curvature:rec.evaluation?.curvature?.maxCurvature,lambda:rec.lambda,alpha:rec.alpha,trials:rec.actualValueEvaluations,normalSeconds,elapsedSeconds:rec.elapsedSeconds}));
  if(!step.accepted)break;
 }
 atomic(stem+"-report.json",snapshot());
}
main().catch(e=>{console.error(e.stack||String(e));process.exitCode=1;});
