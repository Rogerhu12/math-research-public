"use strict";
/* R200: explicit fixed cut-height coordinate; complete objective unchanged.
 * Fresh full normal is assembled before an exact coordinate restriction.
 * No trial clipping, no discarded residual rows, no change to frozen providers.
 */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const sha=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
function bits(x){const b=Buffer.alloc(8);b.writeDoubleBE(x);return b.toString("hex");}
function need(c,m){if(!c)throw Error(m);}
function atomic(p,v){fs.mkdirSync(path.dirname(p),{recursive:true});const t=p+".tmp";fs.writeFileSync(t,JSON.stringify(v,null,2)+"\n");fs.renameSync(t,p);}
function loadFactories(dir){
 const engine=require(path.join(dir,"fd2d-direct-position-tangent-lift-baseline-R187.cjs")).createR187();
 const algebra=require(path.join(dir,"fd2d-position-curvature-chain-R191.cjs")).createR191Algebra();
 const splines=require(path.join(dir,"fd2d-cubic-spline-refinement-R196.cjs")).createR196CubicSplines();
 const metric=require(path.join(dir,"fd2d-nonuniform-metric-provider-R196.cjs")).createR196MetricProvider;
 const curvature=require(path.join(dir,"fd2d-nonuniform-curvature-provider-R196.cjs")).createR196CurvatureProvider;
 const kernel=require(path.join(dir,"fd2d_scaled_band_border_lm_v2_R195.cjs"));
 const bandLM=require(path.join(dir,"fd2d_band_border_lm_adapter_v2_R195.cjs")).createBandBorderLM;
 const candidate=path.join(dir,"../notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json");
 const bundle=JSON.parse(fs.readFileSync(candidate,"utf8"));
 const names=["fd2d-direct-position-tangent-lift-baseline-R187.cjs","fd2d-position-curvature-chain-R191.cjs","fd2d-cubic-spline-refinement-R196.cjs","fd2d-nonuniform-metric-provider-R196.cjs","fd2d-nonuniform-curvature-provider-R196.cjs","fd2d_scaled_band_border_lm_v2_R195.cjs","fd2d_band_border_lm_adapter_v2_R195.cjs"];
 const sourceSHA256=Object.fromEntries(names.map(n=>[n,sha(path.join(dir,n))]));
 return {candidate,sourceSHA256,make(options,guide){
   const core=metric(engine,bundle,options,splines),provider=curvature(engine,core,guide,algebra);
   const lm=bandLM(kernel,provider.definition,{halfBandwidthBlocks:4,kernelSourceSHA256:sourceSHA256["fd2d_scaled_band_border_lm_v2_R195.cjs"]});
   return {core,provider,lm};
 }};
}
function embedAngular(z,J,K,L){
 need(Number.isInteger(J)&&J>0&&Number.isInteger(K)&&K>0&&Number.isInteger(L)&&L>=K,"Explicit nested angular orders required");
 need(z.length===2*J*K+2*J+1,"Full designed-radius layout required");
 const out=new Float64Array(2*J*L+2*J+1),oldCut=2*J*K+J,newCut=2*J*L+J;
 for(let j=0;j<J;j++){
   for(let k=0;k<K;k++){out[j*L+k]=z[j*K+k];out[J*L+j*L+k]=z[J*K+j*K+k];}
   out[2*J*L+j]=z[2*J*K+j];out[newCut+1+j]=z[oldCut+1+j];
 }
 out[newCut]=z[oldCut];
 return out;
}
function guardFixed(z,c){
 need(z.length>c.index,"Fixed coordinate index outside state");
 need(bits(z[c.index])===c.coefficientBinary64,"Fixed cut-height coefficient changed; no projection is applied");
}
function restrictNormal(normal,index){
 const n=normal.g.length;
 need(normal.H.length===n*n&&normal.diagonal&&normal.diagonal.length===n,"Fresh complete flat full normal required");
 need(index>=0&&index<n&&Number.isInteger(index),"Fixed coordinate index");
 const original={gradient:normal.g[index],diagonal:normal.H[index*n+index],columnMaximum:0};
 for(let j=0;j<n;j++)original.columnMaximum=Math.max(original.columnMaximum,Math.abs(normal.H[j*n+index]),Math.abs(normal.H[index*n+j]));
 for(let j=0;j<n;j++){normal.H[j*n+index]=0;normal.H[index*n+j]=0;}
 normal.g[index]=0;normal.diagonal[index]=0;
 normal.coordinateRestriction={schema:"R200-one-fixed-coordinate-normal-restriction-v1",fixedIndex:index,originalCoordinate:original,residualRowsRemoved:0,objectiveValueChanged:false,fullNormalAssembledBeforeRestriction:true};
 return normal;
}
function identity(input,f){return {inputPath:input,inputSHA256:sha(input),candidateSHA256:sha(f.candidate),sourceSHA256:{...f.sourceSHA256,[path.basename(__filename)]:sha(__filename)}};}
function initialize(dir,input,stem,newK=15,target=5/8){
 need(!fs.existsSync(stem+"-input.json")&&!fs.existsSync(stem+"-baseline.json"),"Use a fresh initialization stem");
 const f=loadFactories(dir),old=JSON.parse(fs.readFileSync(input,"utf8")),guide=old.guide||old.curvatureOptions;
 const J=old.options.radialBasisCount,K=old.options.modes;
 need(old.options.angles===128,"Assigned initial same-field comparison uses N128");
 const options={...old.options,modes:newK},op=f.make(old.options,guide),np=f.make(options,guide);
 const embedded=embedAngular(old.z,J,K,newK),common=[];
 const sites=[[.28452183830339467,.37],[.35198514973081013,.2945243112740431],[np.core.base.end,.73]];
 for(const [s,u]of sites){
   const a=op.provider.point(s,u,old.z),b=np.provider.point(s,u,embedded);let maximum=0,scaled=0;
   for(const key of ["X","Xs","Xu","Xss","Xsu","Xuu"])for(let i=0;i<3;i++){
     const d=Math.abs(a.jets[key][i]-b.jets[key][i]);maximum=Math.max(maximum,d);scaled=Math.max(scaled,d/(1+Math.abs(a.jets[key][i])));
   }
   common.push({s,u,maximumAbsoluteTwoJetDifference:maximum,maximumScaledTwoJetDifference:scaled});
 }
 const sameFieldValue=np.provider.value(embedded),cut=np.core.definition.stateLayout.cutHeight;
 const z=Array.from(embedded),oldCoefficient=z[cut],fixed=target-np.core.base.height;
 need(Number.isFinite(target)&&np.core.base.height+fixed===target,"Finite target height is not exactly achieved by this subtraction");
 z[cut]=fixed;
 const c={schema:"R200-fixed-finite-cut-height-coordinate-v1",index:cut,targetFiniteHeight:target,targetBinary64:bits(target),baseFiniteHeight:np.core.base.height,baseHeightBinary64:bits(np.core.base.height),coefficient:fixed,coefficientBinary64:bits(fixed),accuratePhysicalCutHeightCertified:false,initializationChangesField:true,trialProjection:false};
 guardFixed(z,c);
 const baseline=np.provider.value(z),tick=new Date().toISOString();
 const out={schema:"R200-explicit-fixed-height-nonuniform-initial-state-v1",execution:{runtime:"Node actual process",completedInitialization:true,updated:tick},identity:identity(input,f),options,guide,centralSeed:old.centralSeed,z,lambda:old.lambda,iteration:0,parentInitialIteration:old.iteration??old.localAcceptedSteps??null,parentOldDimension:old.z.length,
 fixedHeightConstraint:c,
 angularInjection:{schema:"R196-exact-angular-zero-injection-v1",oldK:K,newK,oldDimension:old.z.length,newDimension:z.length,angularSamplingUnchanged:128,explicitRadialKnotsUnchanged:true,centralSeedUnchanged:true,completeFieldPreservedBeforeHeightChangeInRealArithmetic:true,storedOldCoefficientsCopiedWithoutRounding:true,commonPointTwoJetComparison:common,sameFieldFiniteValue:sameFieldValue},
 initialization:{newBaselineNotAcceptedStep:true,parentActualFiniteHeight:np.core.base.height+oldCoefficient,previousCoefficient:oldCoefficient,previousCoefficientBinary64:bits(oldCoefficient),coefficientChange:fixed-oldCoefficient,newActualFiniteHeight:np.core.base.height+z[cut]},
 initialBaseline:baseline,lastEvaluation:baseline,history:[],providerDefinition:np.provider.definition,backendDefinition:np.lm.backendDefinition,physicalMetricIsDesignVariable:true,continuousCertificate:false,strongTargetComplete:false};
 atomic(stem+"-input.json",out);
 atomic(stem+"-baseline.json",{schema:"R200-fixed-height-baseline-summary-v1",identity:out.identity,angularInjection:out.angularInjection,fixedHeightConstraint:c,initialization:out.initialization,baseline,continuousCertificate:false,strongTargetComplete:false});
 console.log(JSON.stringify({input:stem+"-input.json",newDimension:z.length,sameFieldR2:sameFieldValue.squaredNorm,newBaselineR2:baseline.squaredNorm,metric:baseline.maxRelativeMetric,curvature:baseline.curvature.maxCurvature,minImmersion:baseline.curvature.minImmersion,fixedCut:target,coefficient:fixed,bits:c.coefficientBinary64,common}));
 return out;
}
async function run(dir,input,stem,count){
 need(Number.isInteger(count)&&count>0,"Positive integer step count");
 need(!fs.existsSync(stem+"-report.json")&&!fs.existsSync(stem+"-progress.json"),"Use fresh run stem");
 const f=loadFactories(dir),old=JSON.parse(fs.readFileSync(input,"utf8")),guide=old.guide||old.curvatureOptions;
 const p=f.make(old.options,guide),c=old.fixedHeightConstraint;
 need(c&&c.schema==="R200-fixed-finite-cut-height-coordinate-v1","Explicit fixed-height constraint required");
 need(c.index===p.core.definition.stateLayout.cutHeight&&bits(p.core.base.height)===c.baseHeightBinary64,"Different actual cut layout or background height");
 need(p.core.base.height+c.coefficient===c.targetFiniteHeight,"Inconsistent finite height identity");
 let z=Array.from(old.z),lambda=old.lambda,iteration=old.iteration??0;guardFixed(z,c);
 const history=[],start=new Date().toISOString(),tick=process.hrtime.bigint();
 const binding=identity(input,f);
 function snapshot(){return {schema:"R200-actual-fixed-height-nonuniform-continuation-v1",execution:{runtime:"Node actual terminal process",start,updated:new Date().toISOString(),elapsedSeconds:Number(process.hrtime.bigint()-tick)/1e9},identity:binding,options:old.options,guide,centralSeed:old.centralSeed,z,lambda,iteration,parentInitialIteration:old.iteration??0,history,fixedHeightConstraint:c,actualFiniteCutHeight:p.core.base.height+z[c.index],backendDefinition:p.lm.backendDefinition,physicalMetricIsDesignVariable:true,continuousCertificate:false,strongTargetComplete:false};}
 const value=v=>{guardFixed(v,c);return p.provider.value(v);};
 for(let j=0;j<count;j++){
   guardFixed(z,c);const t=process.hrtime.bigint(),normal=restrictNormal(p.provider.normal(z),c.index),normalSeconds=Number(process.hrtime.bigint()-t)/1e9;
   normal.z=Array.from(z);
   const step=await p.lm.lmStep({z,normal,value,lambda,maxDampingAttempts:8,alphas:[1,.5,.25]});
   if(step.accepted){need(step.direction[c.index]===0,"Fixed-coordinate direction was nonzero");guardFixed(step.z,c);}
   const rec={iteration:iteration+1,accepted:step.accepted,status:step.status,baselineSquaredNorm:normal.squaredNorm,squaredNorm:step.squaredNorm,lambda:step.lambda,nextLambda:step.nextLambda,alpha:step.alpha??null,evaluation:step.evaluation??null,trace:step.trace,solveInfo:step.solveInfo??step.lastSolveInfo,actualValueEvaluations:step.actualValueEvaluations,normalSeconds,elapsedSeconds:Number(process.hrtime.bigint()-t)/1e9,coordinateRestriction:normal.coordinateRestriction,acceptedFixedCoordinateBits:step.accepted?bits(step.z[c.index]):null};
   history.push(rec);
   if(step.accepted){z=Array.from(step.z);lambda=step.nextLambda;iteration++;}
   atomic(stem+"-progress.json",snapshot());
   console.log(JSON.stringify({iteration:rec.iteration,accepted:rec.accepted,R2:rec.squaredNorm,metric:rec.evaluation?.maxRelativeMetric,curvature:rec.evaluation?.curvature?.maxCurvature,alpha:rec.alpha,lambda:rec.lambda,actualFiniteCutHeight:p.core.base.height+z[c.index],normalSeconds,elapsedSeconds:rec.elapsedSeconds}));
   if(!step.accepted)break;
 }
 atomic(stem+"-report.json",snapshot());
}
module.exports={embedAngular,restrictNormal,guardFixed,initialize,run};
if(require.main===module){
 const [mode,dir,input,stem,arg,extra]=process.argv.slice(2);
 if(mode==="init")Promise.resolve().then(()=>initialize(path.resolve(dir),path.resolve(input),path.resolve(stem),arg===undefined?15:Number(arg),extra===undefined?5/8:Number(extra))).catch(e=>{console.error(e.stack||String(e));process.exitCode=1;});
 else if(mode==="run")run(path.resolve(dir),path.resolve(input),path.resolve(stem),Number(arg)).catch(e=>{console.error(e.stack||String(e));process.exitCode=1;});
 else throw Error("Usage: init SHARED_SCRIPTS INPUT STEM [K HEIGHT] | run SHARED_SCRIPTS INPUT STEM COUNT");
}
