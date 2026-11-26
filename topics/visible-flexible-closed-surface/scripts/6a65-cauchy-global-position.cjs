"use strict";
/* Genuine new full-half metric/profile from the Cauchy warm supplier.
 * Complete R201/R205 position columns and R219 caps are rebuilt. There is
 * no transfer of the old B32 clock or an old optimization normal.
 */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const INITIAL="6a65-Cauchy-global-position-initial-v1",CHECKPOINT="6a65-Cauchy-global-position-checkpoint-v1";
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
const emit=x=>process.stdout.write(JSON.stringify(x)+"\n");
const clean=x=>Object.fromEntries(Object.entries(x).filter(([k])=>!["H","g","diagonal","residuals","jvp","z"].includes(k)));
function baseSource(input){
  if(input.baseModel===undefined||input.baseModel==="long-cauchy-v1")return "6a65-geometry-cauchy-warm-base.cjs";
  if(input.baseModel==="short-cauchy-v1")return "6a65-geometry-short-cauchy-base.cjs";
  throw Error("Unknown explicit physical base definition");
}
function build(candidate,input){
  if(!input.options||!input.cauchyDesign)throw Error("Explicit new metric/options required");
  const originalEngine=require("./fd2d-direct-position-tangent-lift-baseline-R187.cjs").createR187();
  const originalBase=originalEngine.candidate(candidate);
  const factory=require("./"+baseSource(input));
  const base=(factory.createShortCauchyWarmBase??factory.createCauchyWarmBase)(originalEngine,originalBase.a0,input.cauchyDesign);
  const engine={...originalEngine,candidate:()=>base};
  const metric=require("./fd2d-nonuniform-metric-provider-R196.cjs").createR196MetricProvider(engine,candidate,input.options);
  metric.definition={...metric.definition,cauchyWarmDesign:base.cauchyWarmDesign,
    radialMetric:"Explicit Cauchy flat-cut polynomial base plus complete rho; design changes g"};
  const originalAlgebra=require("./fd2d-position-curvature-chain-R191.cjs").createR191Algebra();
  let algebra;
  if(input.curvatureModel==="6a65-explicit-tau-quartic-curvature-hinge-v1")
    algebra=require("./6a65-explicit-tau-curvature-hinge.cjs").createExplicitTauCurvatureAlgebra(originalAlgebra,{tau:input.curvatureTau});
  else if(input.curvatureModel===undefined||input.curvatureModel==="R211-fixed-tau-2")
    algebra=require("./fd2d-curvature-quartic-hinge-R211.cjs").createR211AmplifiedCurvatureAlgebra(originalAlgebra,{tau:input.curvatureTau??2});
  else throw Error("Unknown explicit curvature objective definition");
  const referenceFactory=amplitude=>require("./fd2d-bent-annulus-reference-R205.cjs").createR205BentAnnulusReference(engine,base,
    {amplitude,angles:input.options.angles,cacheLimit:0});
  const curvatureOptions={...input.curvatureOptions,sliceReuse:input.runtimeOptions?.sliceReuse??{valueLimit:0,derivativeLimit:0}};
  const position=require("./fd2d-R201-R205-variable-amplitude-lazy-curvature.cjs").createR201R205AmplitudeProvider(
    engine,metric,referenceFactory,curvatureOptions,algebra);
  position.definition={...position.definition,curvaturePenaltyModel:algebra.definition,
    completeSquaredPenaltyEqualsSumPrincipalCurvatureHingesSquared:false,
    baseProvider:{...position.definition.baseProvider,curvaturePenaltyModel:algebra.definition,
      completeSquaredPenaltyEqualsSumPrincipalCurvatureHingesSquared:false}};
  const metricPosition=require("./6a65-quartic-metric-recovered-20261126.cjs").createQuarticMetricProvider(position,engine,input.metricTau??.05);
  const provider=require("./6a65-geometry-low-wide-cap-provider.cjs").createR219WideCapGeometryProvider(metricPosition,input.geometryOptions);
  const cutHeightIndex=metric.definition.stateLayout.cutHeight,amplitudeIndex=position.amplitudeIndex;
  const z=input.z?Array.from(input.z):Array.from(position.initialVector());
  if(!input.z){z[amplitudeIndex]=input.cauchyDesign.amplitude;z[cutHeightIndex]=input.cauchyDesign.cuffHeight-base.height;}
  if(z.length!==provider.dimension||z.some(v=>!Number.isFinite(v)))throw Error("Complete finite parameter vector required");
  return {engine,base,metric,position,metricPosition,provider,referenceFactory,z,cutHeightIndex,amplitudeIndex,
    design:{...base.cauchyWarmDesign,amplitudeIndex,cutHeightIndex,amplitude:z[amplitudeIndex],trueCuffHeight:base.height+z[cutHeightIndex],
      completeCap:"R219",physicalMetricStillADesignVariable:true,continuousCertificate:false,strongTargetComplete:false}};
}
function referenceExport(candidate,input,grid){
  const q=build(candidate,input),ref=q.referenceFactory(q.z[q.amplitudeIndex]),rows=[];
  for(const s of grid.s){
    if(s>q.base.end+1e-13)throw Error("Fit grid must stop at the actual cut");
    const p=q.base.at(Math.min(s,q.base.end)),r=q.metric.radialBasis.physicalJets(s,q.base.centralLength,q.base.end);
    const B=Array(input.options.radialBasisCount).fill(0),Bs=B.slice(),Bss=B.slice();
    for(let k=0;k<r.indices.length;k++){B[r.indices[k]]=r.value[k];Bs[r.indices[k]]=r.first[k];Bss[r.indices[k]]=r.second[k];}
    const t=Math.max(0,Math.min(1,(s-q.base.centralLength)/(q.base.end-q.base.centralLength))),L=q.base.end-q.base.centralLength;
    const chi=t**3*(10+t*(-15+6*t)),chis=30*t*t*(1-t)*(1-t)/L;
    const hc=ref.heightCorrection(s),cut=q.z[q.cutHeightIndex];
    rows.push({s,B,Bs,Bss,f:p.a,fs:p.as,fss:p.ass,meanZ:p.z-hc.value+cut*chi,
      meanZs:p.zs-hc.first+cut*chis,
      angles:grid.u.map(u=>ref.completeReferenceAngles(s,u,q.metric.curve).values.slice(0,4))});
  }
  return {schema:"6a65-Cauchy-R201-explicit-fit-reference-v1",input,zero:Array.from(q.z),design:q.design,
    baseHeight:q.base.height,dimension:q.provider.dimension,cutHeightIndex:q.cutHeightIndex,amplitudeIndex:q.amplitudeIndex,
    legacyDimension:q.metric.dimension,rows,u:grid.u,finiteQuadratureOnly:true};
}
async function runOne(candidate,input){
  if(![INITIAL,CHECKPOINT].includes(input.schema))throw Error("This branch requires its own actual new-metric checkpoint");
  const q=build(candidate,input),release=()=>{q.position.clearSliceReuse?.();if(global.gc)global.gc();};
  const kernel=require("./fd2d_appended_global_schur_R206.cjs").createR206AppendedGlobalKernel(require("./fd2d-R201-R205-band-border-layout.cjs"));
  const lm=require("./fd2d_band_border_lm_adapter_v2_R195.cjs").createBandBorderLM(kernel,q.provider.definition,{halfBandwidthBlocks:4});
  const prior=input.cauchyAcceptedSteps??0;
  if(!Number.isInteger(prior)||prior<0)throw Error("Actual accepted count required");
  const start=Date.now(),normal=q.provider.normal(q.z);release();
  emit({event:"normal",iteration:prior+1,seconds:(Date.now()-start)/1000,R2:normal.squaredNorm,
    metric:normal.maxRelativeMetric,curvature:normal.curvature.maxCurvature,dimension:q.z.length,rowCount:normal.rowCount});
  const out=await lm.lmStep({z:q.z,normal,lambda:input.nextLambda??1e-3,maxDampingAttempts:8,alphas:[1,.5,.25],
    value:z=>{const v=q.provider.value(z);release();return v;},
    onTrial:t=>emit({event:"trial",iteration:prior+1,attempt:t.attempt,alpha:t.alpha,accepted:t.accepted,R2:t.squaredNorm,error:t.error?.message})});
  const z=out.accepted?Array.from(out.z):q.z;
  const record={iteration:prior+1,accepted:out.accepted,status:out.status,alpha:out.alpha??null,baseline:clean(normal),
    evaluation:out.accepted?out.evaluation:clean(normal),trace:out.trace,solveInfo:out.solveInfo??out.lastSolveInfo,seconds:(Date.now()-start)/1000};
  return {...input,schema:CHECKPOINT,z,cauchyAcceptedSteps:prior+(out.accepted?1:0),accepted:out.accepted,
    nextLambda:out.accepted?out.nextLambda:input.nextLambda,status:out.status,baseline:record.baseline,evaluation:record.evaluation,
    cauchyDesign:{...input.cauchyDesign,amplitude:z[q.amplitudeIndex],cuffHeight:q.base.height+z[q.cutHeightIndex]},
    actualDesign:{...q.design,amplitude:z[q.amplitudeIndex],trueCuffHeight:q.base.height+z[q.cutHeightIndex]},
    providerDefinition:q.provider.definition,history:[record],continuousCertificate:false,strongTargetComplete:false};
}
module.exports={build,referenceExport,runOne,INITIAL,CHECKPOINT};
if(require.main===module){
  const [mode,candidateFile,inputFile,outputFile,gridFile]=process.argv.slice(2);
  if(!["reference","value","run"].includes(mode)||!candidateFile||!inputFile||!outputFile||fs.existsSync(outputFile))
    throw Error("reference|value|run candidate input fresh-output [grid] required");
  const candidate=JSON.parse(fs.readFileSync(candidateFile)),input=JSON.parse(fs.readFileSync(inputFile));
  const start=Date.now(),startedUTC=new Date().toISOString();
  (async()=>{
    let output;
    if(mode==="reference")output=referenceExport(candidate,input,JSON.parse(fs.readFileSync(gridFile)));
    else if(mode==="value"){
      const q=build(candidate,input),value=q.provider.value(q.z);q.position.clearSliceReuse?.();if(global.gc)global.gc();
      output={...input,schema:INITIAL,z:q.z,baseline:value,evaluation:value,actualDesign:q.design,
        providerDefinition:q.provider.definition,cauchyAcceptedSteps:0,accepted:false,continuousCertificate:false,strongTargetComplete:false};
    }else output=await runOne(candidate,input);
    output.source={inputSHA256:hash(inputFile),candidateSHA256:hash(candidateFile),entrySHA256:hash(__filename),
      baseSHA256:hash(path.join(__dirname,baseSource(input))),
      curvatureAlgebraSHA256:hash(path.join(__dirname,input.curvatureModel==="6a65-explicit-tau-quartic-curvature-hinge-v1"?
        "6a65-explicit-tau-curvature-hinge.cjs":"fd2d-curvature-quartic-hinge-R211.cjs")),gridSHA256:gridFile?hash(gridFile):null};
    output.execution={startedUTC,endedUTC:new Date().toISOString(),seconds:(Date.now()-start)/1000,node:process.version,
      actualValueBaseline:mode==="value",actualFullNormal:mode==="run",actualAcceptedSteps:mode==="run"&&output.accepted?1:0,
      OSExitCode:null,externalExitReceiptRequired:true};
    fs.mkdirSync(path.dirname(outputFile),{recursive:true});fs.writeFileSync(outputFile,JSON.stringify(output)+"\n");
    const v=output.evaluation;
    emit({event:mode,accepted:output.accepted,count:output.cauchyAcceptedSteps,seconds:output.execution.seconds,
      R2:v?.squaredNorm,metric:v?.maxRelativeMetric,curvature:v?.curvature?.maxCurvature,
      width:v?.geometry?.maxAbsoluteY,held:v?.geometry?.minHeldDistance,A:output.actualDesign?.amplitude,Z:output.actualDesign?.trueCuffHeight,
      dimension:output.dimension??output.z?.length,outputSHA256:hash(outputFile)});
  })().catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
}
