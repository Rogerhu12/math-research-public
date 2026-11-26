"use strict";
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const [candidateFile,inputFile,prefix,mode="run"]=process.argv.slice(2);
if(!candidateFile||!inputFile||!prefix||!['run','check'].includes(mode))throw Error("candidate input fresh-prefix [run|check] required");
const candidate=JSON.parse(fs.readFileSync(candidateFile)),input=JSON.parse(fs.readFileSync(inputFile));
const state=require("./6a65-geometry-gap-length-value.cjs").createGapLengthState(candidate,input);
if(state.design.clockFraction!==1)throw Error("This recorded peak branch starts from the actual beta=1 field");
const provider=require("./6a65-geometry-fixed-peak-metric.cjs")
  .createFixedPeakMetricProvider(state.provider,state.metricPosition,input.peakMetricRows);
const release=()=>{state.position.clearSliceReuse?.();if(typeof global.gc==="function")global.gc();};
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
const write=(suffix,data)=>{const p=prefix+suffix;if(fs.existsSync(p))throw Error("Fresh output required: "+p);
  fs.mkdirSync(path.dirname(p),{recursive:true});fs.writeFileSync(p,JSON.stringify(data)+"\n");};
const emit=x=>process.stdout.write(JSON.stringify(x)+"\n");
const summary=x=>Object.fromEntries(Object.entries(x).filter(([k])=>!["H","g","diagonal","residuals","jvp","z"].includes(k)));
async function main(){
  const start=Date.now(),started=new Date().toISOString();
  if(mode==="check"){
    const d=Float64Array.from({length:state.z.length},(_,i)=>.03*Math.sin((i+1)*1.2345));
    d[state.design.amplitudeIndex]=.007;d[state.cutHeightIndex]=.009;
    const a=provider.extraPeakMetric(state.z,{jacobian:true,direction:d,residuals:true}),eps=1e-6;
    release();
    const plus=provider.extraPeakMetric(state.z.map((v,i)=>v+eps*d[i]),{residuals:true});release();
    const minus=provider.extraPeakMetric(state.z.map((v,i)=>v-eps*d[i]),{residuals:true});release();
    let fd2=0,j2=0,rd=0,dg=0,dHd=0;
    for(let i=0;i<a.jvp.length;i++){const err=(plus.residuals[i]-minus.residuals[i])/(2*eps)-a.jvp[i];fd2+=err*err;j2+=a.jvp[i]*a.jvp[i];rd+=a.residuals[i]*a.jvp[i];}
    for(let i=0;i<d.length;i++){dg+=d[i]*a.g[i];for(let j=0;j<d.length;j++)dHd+=d[i]*a.H[i*d.length+j]*d[j];}
    const report={schema:"6a65-fixed-peak-full-parameter-direction-check-v1",dimension:d.length,
      fixedPoints:provider.peakMetricRows,rowCount:a.rowCount,fdRelativeL2:Math.sqrt(fd2/j2),
      gradientIdentityRelative:Math.abs(rd-dg)/Math.max(1,Math.abs(rd),Math.abs(dg)),
      normalIdentityRelative:Math.abs(dHd-j2)/Math.max(1,j2),
      originalRowsUnchangedAndNotRetested:true,sourceParentSHA256:hash(inputFile),
      wrapperSHA256:hash(path.join(__dirname,"6a65-geometry-fixed-peak-metric.cjs")),seconds:(Date.now()-start)/1000};
    write("-check.json",report);emit(report);return;
  }
  const inherited=input.schema==="6a65-fixed-peak-metric-R215-checkpoint-v1",prior=inherited?input.peakMetricAcceptedSteps:0;
  const previousGapSteps=input.gapLengthAcceptedSteps??input.newDesignAcceptedSteps??0;
  const kernel=require("./fd2d_appended_global_schur_R206.cjs")
    .createR206AppendedGlobalKernel(require("./fd2d-R201-R205-band-border-layout.cjs"));
  const lm=require("./fd2d_band_border_lm_adapter_v2_R195.cjs")
    .createBandBorderLM(kernel,provider.definition,{halfBandwidthBlocks:4});
  let z=Array.from(state.z),lambda=input.nextLambda??input.lambda??1e-3;
  const normal=provider.normal(z);release();
  emit({event:"normal",iteration:prior+1,seconds:(Date.now()-start)/1000,
    total:normal.squaredNorm,originalObjective:normal.originalObjectiveSquaredNorm,
    addedPeak:normal.additionalPeakMetricSquaredNorm,originalQuadraticMetric:normal.quadraticMetricSquaredNorm,
    metric:normal.maxRelativeMetric,originalGridMetric:normal.originalQuadratureMaxRelativeMetric,peakMetric:normal.additionalPeakMaximum});
  const r=await lm.lmStep({z,normal,lambda,maxDampingAttempts:8,alphas:[1,.5,.25],
    value:q=>{const v=provider.value(q);release();return v;},
    onTrial:t=>emit({event:"trial",iteration:prior+1,attempt:t.attempt,alpha:t.alpha,accepted:t.accepted,R2:t.squaredNorm,error:t.error?.message})});
  if(r.accepted){z=Array.from(r.z);lambda=r.nextLambda;}
  const record={iteration:prior+1,accepted:r.accepted,status:r.status,baseline:summary(normal),
    evaluation:r.evaluation??null,alpha:r.alpha??null,nextLambda:lambda,trace:r.trace,
    solveInfo:r.solveInfo??r.lastSolveInfo,elapsedSeconds:(Date.now()-start)/1000};
  const checkpoint={schema:"6a65-fixed-peak-metric-R215-checkpoint-v1",parentInput:inputFile,
    source:{candidateSHA256:hash(candidateFile),inputSHA256:hash(inputFile),runnerSHA256:hash(__filename),
      wrapperSHA256:hash(path.join(__dirname,"6a65-geometry-fixed-peak-metric.cjs"))},
    options:input.options,curvatureOptions:input.curvatureOptions,geometryOptions:state.geometryOptions,
    centralSeed:state.centralSeed,z,nextLambda:lambda,
    peakMetricAcceptedSteps:prior+(r.accepted?1:0),peakMetricRows:provider.peakMetricRows,
    gapLengthAcceptedSteps:previousGapSteps+(r.accepted?1:0),accepted:r.accepted,status:r.status,
    gapLengthDesign:{...state.design,amplitude:z[state.design.amplitudeIndex],trueCuffHeight:state.base.height+z[state.cutHeightIndex]},
    outerLengthDesign:state.design.outerLengthDesign,outerLengthFactoryOptions:state.factoryOptions,
    providerDefinition:provider.definition,history:[record],baseline:record.baseline,evaluation:record.evaluation,
    execution:{runtime:"Node.js "+process.version,start:started,updated:new Date().toISOString(),
      actualFullNormalEvaluations:1,actualAcceptedLMSteps:r.accepted?1:0,elapsedSeconds:record.elapsedSeconds,
      OSExitCode:null,externalNaturalExitReceiptRequired:true},
    physicalMetricIsDesignVariable:true,continuousCertificate:false,wholeClosedReachCertified:false,strongTargetComplete:false};
  write("-state.json",checkpoint);release();
  emit({event:"complete",iteration:prior+1,accepted:r.accepted,total:r.evaluation?.squaredNorm,
    originalObjective:r.evaluation?.originalObjectiveSquaredNorm,addedPeak:r.evaluation?.additionalPeakMetricSquaredNorm,
    originalQuadraticMetric:r.evaluation?.quadraticMetricSquaredNorm,metric:r.evaluation?.maxRelativeMetric,
    originalGridMetric:r.evaluation?.originalQuadratureMaxRelativeMetric,peakMetric:r.evaluation?.additionalPeakMaximum,
    curvature:r.evaluation?.curvature?.maxCurvature,geometry:r.evaluation?.geometry,
    A:checkpoint.gapLengthDesign.amplitude,Z:checkpoint.gapLengthDesign.trueCuffHeight,
    alpha:r.alpha,seconds:record.elapsedSeconds,stateSHA256:hash(prefix+"-state.json")});
}
main().catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
