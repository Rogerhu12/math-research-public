"use strict";
/* Recovered v2 consumer. This is a new source identity, not a recreation of
 * a lost source hash. Delegate one complete nonlinear step to the actual
 * Cauchy factory; do not substitute a gap-clock provider or drop columns. */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const branch=require("./6a65-cauchy-global-position.cjs");
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
const emit=x=>process.stdout.write(JSON.stringify(x)+"\n");
function assertState(input,candidateSHA256){
  if(![branch.INITIAL,branch.CHECKPOINT].includes(input?.schema)||input.baseModel!=="short-cauchy-v1")
    throw Error("An actual short-Cauchy initial/checkpoint is required");
  if(!Array.isArray(input.z)||!input.z.length||input.z.some(v=>!Number.isFinite(v)))
    throw Error("The complete finite saved coefficient vector is required");
  if(!Number.isInteger(input.cauchyAcceptedSteps)||input.cauchyAcceptedSteps<0)
    throw Error("An explicit nonnegative accepted counter is required");
  const curvature=input.curvatureModel==="6a65-explicit-tau-quartic-curvature-hinge-v1"?
    "6a65-explicit-tau-curvature-hinge.cjs":
    input.curvatureModel===undefined||input.curvatureModel==="R211-fixed-tau-2"?
    "fd2d-curvature-quartic-hinge-R211.cjs":null;
  if(!curvature)throw Error("Unknown explicit curvature model");
  const expected={
    entrySHA256:hash(path.join(__dirname,"6a65-cauchy-global-position.cjs")),
    baseSHA256:hash(path.join(__dirname,"6a65-geometry-short-cauchy-base.cjs")),
    curvatureAlgebraSHA256:hash(path.join(__dirname,curvature))
  };
  for(const [key,value] of Object.entries(expected))
    if(input.source?.[key]!==value)throw Error("Saved Cauchy source identity mismatch: "+key);
  if(candidateSHA256!==undefined&&input.source?.candidateSHA256!==candidateSHA256)
    throw Error("Saved candidate bytes do not match this actual candidate");
  if(!input.options||!input.cauchyDesign)throw Error("Explicit finite layout and physical clock required");
  return expected;
}
async function runOne(candidate,input,options={}){
  const expected=assertState(input,options.candidateSHA256);
  const prior=input.cauchyAcceptedSteps,out=await branch.runOne(candidate,input);
  if(out.schema!==branch.CHECKPOINT||out.z.length!==input.z.length||
      out.providerDefinition?.dimension!==input.z.length)
    throw Error("The complete Cauchy dimension or checkpoint schema changed");
  if(JSON.stringify(out.options)!==JSON.stringify(input.options))
    throw Error("An LM step changed the frozen finite parameter layout");
  if(out.cauchyAcceptedSteps!==prior+(out.accepted===true?1:0))
    throw Error("The actual accepted counter did not inherit its parent");
  if(!out.accepted&&out.z.some((v,i)=>!Object.is(v,input.z[i])))
    throw Error("A rejected step changed the retained coefficient vector");
  if(!Number.isFinite(out.baseline?.squaredNorm)||
      out.accepted&&!(out.evaluation?.squaredNorm<out.baseline.squaredNorm))
    throw Error("An accepted step lacks an actual complete objective decrease");
  if(!Array.isArray(out.history)||out.history.length!==1)
    throw Error("Exactly one actual complete LM attempt record is required");
  out.source={...input.source,...expected,scriptSHA256:hash(__filename),
    ...(options.inputSHA256?{inputSHA256:options.inputSHA256}:{}),
    ...(options.candidateSHA256?{candidateSHA256:options.candidateSHA256}:{})};
  out.physicalMetricStillADesignVariable=true;
  out.continuousCertificate=false;out.wholeClosedReachCertified=false;out.strongTargetComplete=false;
  return out;
}
module.exports={runOne,assertState,INITIAL:branch.INITIAL,CHECKPOINT:branch.CHECKPOINT};
if(require.main===module){
  const [candidateFile,inputFile,prefix,mode="run"]=process.argv.slice(2),output=prefix+"-state.json";
  if(!candidateFile||!inputFile||!prefix||!["run","1"].includes(mode)||fs.existsSync(output))
    throw Error("candidate input fresh-prefix run required; exactly one full attempt");
  const started=Date.now(),startedUTC=new Date().toISOString();
  const candidateSHA256=hash(candidateFile),inputSHA256=hash(inputFile);
  const candidate=JSON.parse(fs.readFileSync(candidateFile)),input=JSON.parse(fs.readFileSync(inputFile));
  (async()=>{
    const out=await runOne(candidate,input,{candidateSHA256,inputSHA256});
    out.parentInput=inputFile;
    out.execution={startedUTC,endedUTC:new Date().toISOString(),seconds:(Date.now()-started)/1000,
      node:process.version,actualFullNormalEvaluations:1,actualAcceptedLMSteps:out.accepted?1:0,
      retainedInputOnNoAcceptance:!out.accepted,OSExitCode:null,externalExitReceiptRequired:true};
    fs.mkdirSync(path.dirname(output),{recursive:true});fs.writeFileSync(output,JSON.stringify(out)+"\n");
    const v=out.accepted?out.evaluation:out.baseline;
    emit({event:"complete",accepted:out.accepted,cauchyAcceptedSteps:out.cauchyAcceptedSteps,
      alpha:out.history[0].alpha,total:v.squaredNorm,metric:v.maxRelativeMetric,
      curvature:v.curvature?.maxCurvature,width:v.geometry?.maxAbsoluteY,held:v.geometry?.minHeldDistance,
      A:out.actualDesign?.amplitude,Z:out.actualDesign?.trueCuffHeight,dimension:out.z.length,
      seconds:out.execution.seconds,outputSHA256:hash(output)});
  })().catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
}
