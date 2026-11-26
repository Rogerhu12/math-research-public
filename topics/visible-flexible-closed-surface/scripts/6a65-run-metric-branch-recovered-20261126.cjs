"use strict";
/* Recovery version: explicit schemas/counters and invocation-local history.
 * The finite arithmetic is reconstructed from the executed local source.
 * This file has a new identity; old execution hashes are not inherited. */
const fs=require("node:fs"),path=require("node:path");
const {createMemoryBoundR211RunProvider}=require("./6a65-low-memory-r211-provider-recovered-20261126.cjs");
const {createR187}=require("./fd2d-direct-position-tangent-lift-baseline-R187.cjs");
const {createQuarticMetricProvider}=require("./6a65-quartic-metric-recovered-20261126.cjs");
const {createR201R205AmplitudeGeometryProvider}=require("./fd2d-R201-R205-variable-amplitude-geometric-guide.cjs");
const {createR206AppendedGlobalKernel}=require("./fd2d_appended_global_schur_R206.cjs");
const {createBandBorderLM}=require("./fd2d_band_border_lm_adapter_v2_R195.cjs");
const layout=require("./fd2d-R201-R205-band-border-layout.cjs");
const [candidatePath,inputPath,outputPrefix,tauText="0.05",countText="1",mode="run"]=process.argv.slice(2);
if(!candidatePath||!inputPath||!outputPrefix)throw Error("candidate input fresh-output-prefix [tau|original count run|check]");
const input=JSON.parse(fs.readFileSync(inputPath,"utf8")),candidate=JSON.parse(fs.readFileSync(candidatePath,"utf8"));
const tau=tauText==="original"?null:Number(tauText),count=Number(countText);
if(tau!==null&&!(Number.isFinite(tau)&&tau>0))throw Error("Positive finite tau or literal original required");
if(!Number.isInteger(count)||count<1)throw Error("Positive integer iteration count required");
input.curvatureOptions={...input.curvatureOptions,sliceReuse:{valueLimit:0,derivativeLimit:0}};
const original=createMemoryBoundR211RunProvider(candidate,input);
const metricPosition=tau===null?original.position:createQuarticMetricProvider(original.position,createR187(),tau);
const provider=createR201R205AmplitudeGeometryProvider(metricPosition,input.geometryOptions);
const lm=createBandBorderLM(createR206AppendedGlobalKernel(layout),provider.definition,{halfBandwidthBlocks:4});
const write=(name,data)=>{if(fs.existsSync(name))throw Error("Refusing to overwrite output: "+name);fs.mkdirSync(path.dirname(name),{recursive:true});fs.writeFileSync(name,JSON.stringify(data)+"\n");};
const summary=x=>{const out={...x};for(const k of ["H","g","diagonal","residuals","jvp","z"])delete out[k];return out;};
const status=x=>process.stdout.write(JSON.stringify(x)+"\n");
async function main(){
 const start=Date.now(),startedUTC=new Date().toISOString();
 let z=Array.from(input.z),lambda=input.nextLambda??input.lambda??1e-3;
 status({event:"start",mode,tau,dimension:z.length,time:startedUTC});
 if(mode==="check"){
  const d=Float64Array.from({length:z.length},(_,i)=>0.03*Math.sin((i+1)*1.2345));
  d[original.position.amplitudeIndex]=.007;d[original.metric.definition.stateLayout.cutHeight]=.009;
  const a=metricPosition.metric(z,{jacobian:true,direction:d,residuals:true}),eps=1e-6;
  const plus=metricPosition.metric(z.map((v,i)=>v+eps*d[i]),{residuals:true}),minus=metricPosition.metric(z.map((v,i)=>v-eps*d[i]),{residuals:true});
  let fd2=0,j2=0,rd=0,dg=0,dHd=0;
  for(let i=0;i<a.jvp.length;i++){const delta=(plus.residuals[i]-minus.residuals[i])/(2*eps)-a.jvp[i];fd2+=delta*delta;j2+=a.jvp[i]*a.jvp[i];rd+=a.residuals[i]*a.jvp[i];}
  for(let i=0;i<z.length;i++){dg+=d[i]*a.g[i];for(let j=0;j<z.length;j++)dHd+=d[i]*a.H[i*z.length+j]*d[j];}
  const report={schema:"6a65-quartic-metric-complete-chain-check-recovered-v1",dimension:z.length,rowCount:a.rowCount,tau,fdRelativeL2:Math.sqrt(fd2/j2),gradientIdentityRelative:Math.abs(rd-dg)/Math.max(1,Math.abs(rd),Math.abs(dg)),normalIdentityRelative:Math.abs(dHd-j2)/Math.max(1,j2),baseline:summary(a),elapsedSeconds:(Date.now()-start)/1000,continuousCertificate:false};
  write(outputPrefix+"-check.json",report);status(report);return;
 }
 if(mode!=="run")throw Error("mode run or check required");
 const history=[];
 const checkpointSchema=tau===null?"6a65-R211-original-metric-checkpoint-v1":"6a65-R211-quartic-metric-checkpoint-v1";
 const inherited=input.schema===checkpointSchema&&input.metricTau===tau;
 const originAccepted=inherited?(input.metricBranchAcceptedSteps??0):0;
 if(!Number.isInteger(originAccepted)||originAccepted<0)throw Error("Nonnegative inherited accepted count required");
 for(let k=0;k<count;k++){
  const tick=Date.now(),normal=provider.normal(z);
  original.position.clearSliceReuse();if(global.gc)global.gc();
  status({event:"normal",iteration:originAccepted+k+1,seconds:(Date.now()-tick)/1000,R2:normal.squaredNorm,metric:normal.maxRelativeMetric,curvature:normal.curvature.maxCurvature});
  const r=await lm.lmStep({z,normal,value:q=>{const v=provider.value(q);original.position.clearSliceReuse();if(global.gc)global.gc();return v;},lambda,maxDampingAttempts:8,alphas:[1,.5,.25],
    onTrial:t=>status({event:"trial",iteration:originAccepted+k+1,attempt:t.attempt,alpha:t.alpha,accepted:t.accepted,R2:t.squaredNorm,error:t.error?.message})});
  const record={iteration:originAccepted+k+1,accepted:r.accepted,status:r.status,baseline:summary(normal),evaluation:r.evaluation??null,alpha:r.alpha??null,nextLambda:r.nextLambda,trace:r.trace,solveInfo:r.solveInfo??r.lastSolveInfo,elapsedSeconds:(Date.now()-tick)/1000};
  history.push(record);if(r.accepted){z=Array.from(r.z);lambda=r.nextLambda;}
  const accepted=originAccepted+history.filter(v=>v.accepted).length;
  const checkpoint={
    schema:checkpointSchema,parentInput:inputPath,candidate:input.candidate??null,
    options:input.options,curvatureOptions:input.curvatureOptions,geometryOptions:input.geometryOptions,
    centralSeed:input.centralSeed??null,metricTau:tau,metricBranchAcceptedSteps:accepted,
    acceptedSteps:accepted,branchAcceptedSteps:accepted,accepted:r.accepted,status:r.status,
    objectiveTransition:{metric:tau===null?"original R211 quadratic metric objective":inherited?"same saved quartic metric objective":"q to q+q*q/tau^2",oldNormalReused:false,physicalFieldInitiallyUnchanged:true},
    providerDefinition:provider.definition,z,nextLambda:lambda,history,branchHistory:history,
    historyMeaning:"This invocation; earlier accepted states are named by parentInput",
    baseline:record.baseline,evaluation:record.evaluation,
    execution:{runtime:"Node",startedUTC,updatedUTC:new Date().toISOString(),OSExitCode:null,externalProcessExitReceiptRequired:true},
    recoverySourceIdentity:"recovered-20261126; old execution hashes not inherited",
    continuousCertificate:false,strongTargetComplete:false
  };
  write(outputPrefix+"-"+(k+1)+".json",checkpoint);
  status({event:"step",iteration:originAccepted+k+1,accepted:r.accepted,R2:r.squaredNorm,alpha:r.alpha,metric:r.evaluation?.maxRelativeMetric,curvature:r.evaluation?.curvature.maxCurvature,seconds:record.elapsedSeconds,metricBranchAcceptedSteps:accepted});
  if(!r.accepted)break;
 }
 status({event:"complete",acceptedThisInvocation:history.filter(r=>r.accepted).length,metricBranchAcceptedSteps:originAccepted+history.filter(r=>r.accepted).length,seconds:(Date.now()-start)/1000});
}
main().catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});

