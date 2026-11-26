"use strict";
/* Actual R219 caps, N128 evaluation and a frozen union of old/new peak rows.
 * Init is a new complete finite baseline; run performs one full-column LM.
 */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const INITIAL="6a65-R219-expanded-peaks-initial-v1",CHECKPOINT="6a65-R219-expanded-peaks-checkpoint-v1";
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
const emit=x=>process.stdout.write(JSON.stringify(x)+"\n");
const clean=x=>Object.fromEntries(Object.entries(x).filter(([k])=>!["H","g","diagonal","residuals","jvp","z"].includes(k)));
function build(candidate,input){
 const q=require("./6a65-geometry-gap-length-value.cjs").createGapLengthState(candidate,input);
 const caps=require("./6a65-geometry-low-wide-cap-provider.cjs").createR219WideCapGeometryProvider(q.metricPosition,input.geometryOptions);
 const provider=require("./6a65-geometry-fixed-peak-metric.cjs").createFixedPeakMetricProvider(caps,q.metricPosition,input.peakMetricRows);
 q.provider=provider;q.geometryOptions=caps.r219GeometryOptions;
 q.design={...q.design,completeCapSchema:"6a65-R219-low-wide-complete-fixed-caps-v1"};
 return q;
}
function expandedRows(rows){
 if(!Array.isArray(rows)||rows.length!==42)throw Error("Explicit original 42 fixed peak points required for this recorded transition");
 const out=rows.map(p=>({...p})),seen=new Set(out.map(p=>p.s.toPrecision(17)+"/"+p.u.toPrecision(17)));
 const radial=[.11,.12,.13,.13906383994179997,.15,.16,.17],fractions=[0,1/64,1/32,31/32,63/64,1];
 for(const s of radial)for(let j=0;j<fractions.length;j++){
  const f=fractions[j],u=Math.PI*f,key=s.toPrecision(17)+"/"+u.toPrecision(17);
  if(seen.has(key))throw Error("Unexpected duplicate frozen peak point");
  out.push({s,u,anglePiFraction:f,weight:.0005*(j===0||j===fractions.length-1?.5:1)});seen.add(key);
 }
 return out;
}
function initialize(candidate,input){
 if(input.schema!=="6a65-fixed-peak-metric-R215-checkpoint-v1"||input.options.modes!==11||input.options.angles!==64)
  throw Error("This explicit transition requires the actual K11/N64 fixed-peak R215 checkpoint");
 const next={schema:INITIAL,options:{...input.options,angles:128},z:Array.from(input.z),
  curvatureOptions:input.curvatureOptions,geometryOptions:input.geometryOptions,centralSeed:input.centralSeed,
  gapLengthDesign:input.gapLengthDesign,outerLengthDesign:input.outerLengthDesign,outerLengthFactoryOptions:input.outerLengthFactoryOptions,
  metricTau:input.gapLengthDesign.metricTau,peakMetricRows:expandedRows(input.peakMetricRows),
  nextLambda:input.nextLambda,r219AcceptedSteps:0,accepted:false,
  parentCounters:{schema:input.schema,peakMetricAcceptedSteps:input.peakMetricAcceptedSteps,gapLengthAcceptedSteps:input.gapLengthAcceptedSteps},
  lowWideCapDesign:{result:"R219",cornerX:".79",cornerHeight:".86",actualCuffHeightWindow:[".40",".53"],finiteGuideWindow:[.41,.52]},
  objectiveTransition:{actualCompleteCapAndItsMetricChanged:true,prefixExactPhysicalDefinitionInitiallyUnchanged:true,
   allCoefficientsInitiallyUnchanged:true,originalAngles:64,newAngles:128,finitePrimitiveQuadratureChanged:true,
   allOriginal42PeakRowsRetained:true,newFixedPeakRows:42,fixedPeakRowsTotal:84,acceptedOptimizationStep:false},
  continuousCertificate:false,strongTargetComplete:false};
 const old=require("./6a65-geometry-gap-length-value.cjs").createGapLengthState(candidate,input),q=build(candidate,next);
 if(q.z.some((v,i)=>!Object.is(v,input.z[i])))throw Error("Prefix coefficient changed during cap/grid/point transition");
 const keys=["X","Xs","Xu","Xss","Xsu","Xuu"],differences=Object.fromEntries(keys.map(k=>[k,0]));
 const c=q.base.centralLength,S=q.base.end,sites=[{s:0,u:0},{s:c,u:Math.PI/2},{s:.13906383994179997,u:0},{s:.3,u:.4},{s:.65,u:1.3},{s:S,u:.7}];
 for(const {s,u}of sites){
  const a=old.position.slice(s,old.z,false).point(u),b=q.position.slice(s,q.z,false).point(u);
  for(const key of keys)for(let k=0;k<3;k++)differences[key]=Math.max(differences[key],Math.abs(a.jets[key][k]-b.jets[key][k]));
  old.position.clearSliceReuse?.();q.position.clearSliceReuse?.();if(global.gc)global.gc();
 }
 const baseline=q.provider.value(q.z);q.position.clearSliceReuse?.();if(global.gc)global.gc();
 next.z=Array.from(q.z);next.geometryOptions=q.geometryOptions;next.gapLengthDesign=q.design;
 next.providerDefinition=q.provider.definition;next.baseline=baseline;
 next.quadratureTransitionProbe={sites,maxTwoJetDifferences:differences,finiteObservationsOnly:true};
 return {initial:next,q};
}
async function runOne(candidate,input){
 if(![INITIAL,CHECKPOINT].includes(input.schema)||input.options.angles!==128||input.peakMetricRows?.length!==84||input.lowWideCapDesign?.result!=="R219")
  throw Error("Explicit saved R219/N128/84-point branch required");
 const q=build(candidate,input),provider=q.provider;
 const release=()=>{q.position.clearSliceReuse?.();if(global.gc)global.gc();};
 const kernel=require("./fd2d_appended_global_schur_R206.cjs").createR206AppendedGlobalKernel(require("./fd2d-R201-R205-band-border-layout.cjs"));
 const lm=require("./fd2d_band_border_lm_adapter_v2_R195.cjs").createBandBorderLM(kernel,provider.definition,{halfBandwidthBlocks:4});
 const prior=input.r219AcceptedSteps;
 if(!Number.isInteger(prior)||prior<0)throw Error("Actual nonnegative accepted counter required");
 let z=Array.from(q.z),lambda=input.nextLambda??1e-3;const start=Date.now(),normal=provider.normal(z);release();
 emit({event:"normal",iteration:prior+1,seconds:(Date.now()-start)/1000,total:normal.squaredNorm,
  originalObjective:normal.originalObjectiveSquaredNorm,addedPeak:normal.additionalPeakMetricSquaredNorm,
  quadraticMetric:normal.quadraticMetricSquaredNorm,metric:normal.maxRelativeMetric,curvature:normal.curvature.maxCurvature,rowCount:normal.rowCount,dimension:z.length});
 const r=await lm.lmStep({z,normal,lambda,maxDampingAttempts:8,alphas:[1,.5,.25],
  value:v=>{const a=provider.value(v);release();return a;},
  onTrial:t=>emit({event:"trial",iteration:prior+1,attempt:t.attempt,alpha:t.alpha,accepted:t.accepted,R2:t.squaredNorm,error:t.error?.message})});
 if(r.accepted){z=Array.from(r.z);lambda=r.nextLambda;}
 const record={iteration:prior+1,accepted:r.accepted,status:r.status,baseline:clean(normal),evaluation:r.evaluation??null,
  alpha:r.alpha??null,trace:r.trace,solveInfo:r.solveInfo??r.lastSolveInfo,seconds:(Date.now()-start)/1000};
 const checkpoint={schema:CHECKPOINT,options:input.options,z,curvatureOptions:input.curvatureOptions,
  geometryOptions:q.geometryOptions,centralSeed:q.centralSeed,metricTau:q.metricTau,
  gapLengthDesign:{...q.design,amplitude:z[q.design.amplitudeIndex],trueCuffHeight:q.base.height+z[q.cutHeightIndex]},
  outerLengthDesign:q.design.outerLengthDesign,outerLengthFactoryOptions:q.factoryOptions,
  lowWideCapDesign:input.lowWideCapDesign,peakMetricRows:input.peakMetricRows,objectiveTransition:input.objectiveTransition,
  nextLambda:lambda,r219AcceptedSteps:prior+(r.accepted?1:0),accepted:r.accepted,status:r.status,
  parentCounters:input.parentCounters,providerDefinition:provider.definition,baseline:record.baseline,evaluation:record.evaluation,history:[record],
  physicalMetricStillADesignVariable:true,continuousCertificate:false,wholeClosedReachCertified:false,strongTargetComplete:false};
 release();return {checkpoint,record};
}
module.exports={build,expandedRows,initialize,runOne};
if(require.main===module){
 const [candidateFile,inputFile,prefix,mode]=process.argv.slice(2);
 if(!candidateFile||!inputFile||!prefix||!["init","run"].includes(mode))throw Error("candidate input fresh-prefix init|run required");
 const suffix=mode==="init"?"-initial.json":"-state.json",output=prefix+suffix;
 if(fs.existsSync(output))throw Error("Fresh output path required");
 const candidate=JSON.parse(fs.readFileSync(candidateFile)),input=JSON.parse(fs.readFileSync(inputFile)),start=Date.now(),started=new Date().toISOString();
 const source={inputSHA256:hash(inputFile),candidateSHA256:hash(candidateFile),scriptSHA256:hash(__filename),
  capProviderSHA256:hash(path.join(__dirname,"6a65-geometry-low-wide-cap-provider.cjs")),
  peakWrapperSHA256:hash(path.join(__dirname,"6a65-geometry-fixed-peak-metric.cjs"))};
 (async()=>{
  const result=mode==="init"?initialize(candidate,input):await runOne(candidate,input),data=result.initial??result.checkpoint;
  data.source=source;data.parentInput=inputFile;
  data.execution={startedUTC:started,updatedUTC:new Date().toISOString(),seconds:(Date.now()-start)/1000,node:process.version,
   actualFullNormalEvaluations:mode==="run"?1:0,actualAcceptedLMSteps:mode==="run"&&data.accepted?1:0,
   actualInitialValueEvaluations:mode==="init"?1:0,OSExitCode:null,externalExitReceiptRequired:true};
  fs.mkdirSync(path.dirname(output),{recursive:true});fs.writeFileSync(output,JSON.stringify(data)+"\n");
  const v=mode==="init"?data.baseline:data.evaluation;
  emit({event:mode==="init"?"initial":"complete",accepted:data.accepted,r219AcceptedSteps:data.r219AcceptedSteps,
   total:v?.squaredNorm,originalObjective:v?.originalObjectiveSquaredNorm,addedPeak:v?.additionalPeakMetricSquaredNorm,
   quadraticMetric:v?.quadraticMetricSquaredNorm,metric:v?.maxRelativeMetric,curvature:v?.curvature?.maxCurvature,
   width:v?.geometry?.maxAbsoluteY,held:v?.geometry?.minHeldDistance,A:data.gapLengthDesign.amplitude,Z:data.gapLengthDesign.trueCuffHeight,
   alpha:result.record?.alpha,seconds:data.execution.seconds,source,outputSHA256:hash(output)});
 })().catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
}
