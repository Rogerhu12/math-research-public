"use strict";
/* Actual complete full-half amplitude branch, with explicit objective transition.
 * No old normal is reused. Complete R206 solve and original Armijo policy.
 */
function createFullHalfRunProvider(candidate,input){
 const e=require("./fd2d-direct-position-tangent-lift-baseline-R187.cjs").createR187();
 const spl=require("./fd2d-cubic-spline-refinement-R196.cjs").createR196CubicSplines();
 const m=require("./fd2d-nonuniform-metric-provider-R196.cjs").createR196MetricProvider(e,candidate,input.options,spl);
 const algebra=require("./fd2d-position-curvature-chain-R191.cjs").createR191Algebra();
 const ref=A=>require("./fd2d-bent-annulus-reference-R205.cjs").createR205BentAnnulusReference(e,m.base,{amplitude:A,angles:input.options.angles});
 const position=require("./fd2d-R201-R205-variable-amplitude-slice-reuse.cjs").createR201R205AmplitudeProvider(e,m,ref,input.curvatureOptions,algebra);
 const provider=require("./fd2d-R201-R205-variable-amplitude-geometric-guide.cjs").createR201R205AmplitudeGeometryProvider(position,input.geometryOptions);
 const kernel=require("./fd2d_appended_global_schur_R206.cjs").createR206AppendedGlobalKernel(require("./fd2d-R201-R205-band-border-layout.cjs"));
 const lm=require("./fd2d_band_border_lm_adapter_v2_R195.cjs").createBandBorderLM(kernel,provider.definition,{halfBandwidthBlocks:4});
 if(input.z.length!==provider.dimension)throw Error("Full complete input dimension mismatch");
 if(input.centralSeed&&(input.centralSeed.rawA!==m.curve.A||input.centralSeed.rawB!==m.curve.B))throw Error("Saved central seed changed");
 return {metric:m,position,provider,lm};
}
function finiteSummary(value){
 const out={...value};for(const k of ["H","g","diagonal","residuals","jvp","z"])delete out[k];return out;
}
async function continueFullHalfBranch(candidate,input,count,config={}){
 if(!Number.isInteger(count)||count<1)throw Error("Positive real iteration count required");
 const {metric,position,provider,lm}=createFullHalfRunProvider(candidate,input);
 let z=Array.from(input.z),lambda=input.nextLambda??input.lambda??1e-3,accepted=input.branchAcceptedSteps||0;
 const history=Array.from(input.branchHistory||[]),start=new Date().toISOString(),tick=Date.now();
 function snapshot(record){
  return {...input,schema:"fd2d-R201-R205-variable-amplitude-actual-checkpoint-v1",z,lambda,nextLambda:lambda,
   providerDefinition:provider.definition,backendDefinition:lm.backendDefinition,
   amplitudeIndex:position.amplitudeIndex,cutHeightIndex:metric.definition.stateLayout.cutHeight,
   branchAcceptedSteps:accepted,acceptedSteps:accepted,acceptedCounterMeaning:"Accepted steps in this explicitly named objective branch; parent count is separate",
   branchHistory:history,baseline:record?.baseline,evaluation:record?.evaluation,status:record?.status,accepted:record?.accepted??false,
   trace:record?.trace,solveInfo:record?.solveInfo,actualValueEvaluations:record?.actualValueEvaluations,
   actualAmplitude:z[position.amplitudeIndex],actualFiniteCuffHeight:metric.base.height+z[metric.definition.stateLayout.cutHeight],
   sliceReuseStats:position.sliceReuseStats(),
   execution:{runtime:config.runtime||"caller must supply actual runtime",start,updated:new Date().toISOString(),elapsedSeconds:(Date.now()-tick)/1000,OSExitCode:null},
   physicalMetricIsDesignVariable:true,continuousCertificate:false,wholeClosedReachCertified:false,strongTargetComplete:false};
 }
 for(let k=0;k<count;k++){
  const t=Date.now(),normal=provider.normal(z),normalSeconds=(Date.now()-t)/1000,normalSliceStats=position.sliceReuseStats();
  if(config.onNormal)await config.onNormal({branchIteration:accepted+1,baseline:finiteSummary(normal),normalSeconds,normalSliceStats});
  const r=await lm.lmStep({z,normal,value:q=>provider.value(q),lambda,maxDampingAttempts:8,alphas:[1,.5,.25]});
  const record={branchIteration:accepted+1,accepted:r.accepted,status:r.status,baseline:finiteSummary(normal),baselineSquaredNorm:normal.squaredNorm,
   squaredNorm:r.squaredNorm,lambda:r.lambda,nextLambda:r.nextLambda,alpha:r.alpha??null,evaluation:r.evaluation??null,
   trace:r.trace,solveInfo:r.solveInfo??r.lastSolveInfo,actualValueEvaluations:r.actualValueEvaluations,
   normalSeconds,normalSliceStats,elapsedSeconds:(Date.now()-t)/1000};
  history.push(record);if(r.accepted){z=Array.from(r.z);lambda=r.nextLambda;accepted++;}
  if(config.onStep)await config.onStep(snapshot(record),record);
  if(!r.accepted)break;
 }
 return snapshot(history[history.length-1]);
}
module.exports={createFullHalfRunProvider,continueFullHalfBranch};
if(require.main===module){
 const fs=require("node:fs"),path=require("node:path"),[candidatePath,inputPath,outputPrefix,countText="1"]=process.argv.slice(2);
 if(!candidatePath||!inputPath||!outputPrefix||fs.existsSync(outputPrefix+"-final.json"))throw Error("candidate input fresh-output-prefix [count] required");
 const write=(name,data)=>{fs.mkdirSync(path.dirname(name),{recursive:true});fs.writeFileSync(name,JSON.stringify(data,null,2)+"\n");};
 continueFullHalfBranch(JSON.parse(fs.readFileSync(candidatePath,"utf8")),JSON.parse(fs.readFileSync(inputPath,"utf8")),Number(countText),
 {runtime:"Actual Node invocation; process exit belongs to external receipt",onStep:(s,r)=>{write(outputPrefix+"-"+r.branchIteration+".json",s);process.stdout.write(JSON.stringify({iteration:r.branchIteration,accepted:r.accepted,R2:r.squaredNorm,alpha:r.alpha})+"\n");}})
 .then(s=>write(outputPrefix+"-final.json",s)).catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
}
