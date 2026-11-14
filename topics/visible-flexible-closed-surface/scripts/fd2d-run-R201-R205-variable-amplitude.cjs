"use strict";
/* R201/R205/R206 actual two-global half-period LM replay.
 * Same frozen finite functions and complete rows; no continuous certificate.
 */
const fs=require("fs"),path=require("path"),crypto=require("crypto");
const {createR187}=require("./fd2d-direct-position-tangent-lift-baseline-R187.cjs");
const {createR196CubicSplines}=require("./fd2d-cubic-spline-refinement-R196.cjs");
const {createR196MetricProvider}=require("./fd2d-nonuniform-metric-provider-R196.cjs");
const {createR191Algebra}=require("./fd2d-position-curvature-chain-R191.cjs");
const {createR205BentAnnulusReference}=require("./fd2d-bent-annulus-reference-R205.cjs");
const {createR201R205AmplitudeProvider}=require("./fd2d-R201-R205-variable-amplitude-provider.cjs");
const {createR201R205AmplitudeGeometryProvider}=require("./fd2d-R201-R205-variable-amplitude-geometric-guide.cjs");
const baseKernel=require("./fd2d-R201-R205-band-border-layout.cjs");
const {createR206AppendedGlobalKernel}=require("./fd2d_appended_global_schur_R206.cjs");
const {createBandBorderLM}=require("./fd2d_band_border_lm_adapter_v2_R195.cjs");
const sourceNames=["fd2d-direct-position-tangent-lift-baseline-R187.cjs","fd2d-cubic-spline-refinement-R196.cjs",
"fd2d-nonuniform-metric-provider-R196.cjs","fd2d-position-curvature-chain-R191.cjs","fd2d-bent-annulus-reference-R205.cjs",
"fd2d-R201-R205-variable-amplitude-provider.cjs","fd2d-R201-R205-variable-amplitude-geometric-guide.cjs",
"fd2d-R201-R205-band-border-layout.cjs","fd2d_appended_global_schur_R206.cjs","fd2d_band_border_lm_adapter_v2_R195.cjs",
"fd2d-run-R201-R205-variable-amplitude.cjs"];
function args(v){const o={};for(let i=0;i<v.length;i+=2){if(!v[i].startsWith("--")||v[i+1]===undefined)throw Error("Use --key value");o[v[i].slice(2)]=v[i+1];}return o;}
function identity(p){const b=fs.readFileSync(p);return {path:p,bytes:b.length,sha256:crypto.createHash("sha256").update(b).digest("hex")};}
function write(p,x){fs.mkdirSync(path.dirname(p),{recursive:true});fs.writeFileSync(p,JSON.stringify(x,null,2)+"\n");}
function summary(n){const r={...n};for(const k of["H","g","diagonal","z","residuals","jvp"])delete r[k];return r;}
async function run(o){
 if(!o.input||!o.candidate||!o["out-prefix"])throw Error("--input --candidate --out-prefix required");
 const t=Date.now(),input=JSON.parse(fs.readFileSync(o.input,"utf8")),bundle=JSON.parse(fs.readFileSync(o.candidate,"utf8"));
 const engine=createR187(),splines=createR196CubicSplines(),metric=createR196MetricProvider(engine,bundle,input.options,splines),
 algebra=createR191Algebra(),curvatureOptions=input.curvatureOptions||{guide:9.5,weight:.01,nodeShare:.5},
 geometryOptions=input.geometryOptions||{radius:1.59,width:.84,held:.65,weight:10,nodeShare:.5,cutWindow:[.41,.62]},
 referenceFactory=A=>createR205BentAnnulusReference(engine,metric.base,{amplitude:A,angles:input.options.angles}),
 position=createR201R205AmplitudeProvider(engine,metric,referenceFactory,curvatureOptions,algebra),
 provider=createR201R205AmplitudeGeometryProvider(position,geometryOptions),
 kernel=createR206AppendedGlobalKernel(baseKernel),
 lm=createBandBorderLM(kernel,provider.definition,{halfBandwidthBlocks:4});
 if(input.centralSeed&&(input.centralSeed.rawA!==metric.curve.A||input.centralSeed.rawB!==metric.curve.B))
   throw Error("Saved finite central axes do not match this complete frozen provider");
 const inherited=input.schema==="fd2d-R201-R205-variable-amplitude-actual-checkpoint-v1";
 let z,transition;
 if(inherited){
  if(!Array.isArray(input.z)||input.z.length!==provider.dimension)throw Error("Explicit R201/R205/R206 saved layout mismatch");
  if(JSON.stringify(input.providerDefinition.radialBasisDefinition)!==JSON.stringify(provider.definition.radialBasisDefinition))
    throw Error("Saved actual radial basis mismatch");
  z=Float64Array.from(input.z);transition={inheritedActualField:true,amplitudeFromSavedVector:true};
 }else{
  if(o.amplitude===undefined)throw Error("An explicit --amplitude is required for a new reference baseline");
  const A=Number(o.amplitude);
  if(input.schema==="fd2d-R201-full-half-actual-checkpoint-v1")z=position.appendAmplitude(input.z,A);
  else if(Array.isArray(input.z)&&input.z.length===metric.dimension)z=position.injectLegacy(input.z,A);
  else throw Error("Only an explicit full R201 checkpoint or complete legacy coefficient vector can be injected");
  transition={inheritedActualField:false,newDevelopedReferenceBaseline:true,allParentCoefficientsCopied:true,
    newUnknownAmplitude:A,positionsClaimedEqualToFlatParent:false,acceptedBeforeActualTrial:false};
 }
 const steps=o.steps===undefined?1:Number(o.steps);if(!Number.isInteger(steps)||steps<0)throw Error("Nonnegative integer steps required");
 const sources=Object.fromEntries(sourceNames.map(n=>[n,identity(path.join(__dirname,n))]));
 const common={schema:"fd2d-R201-R205-variable-amplitude-actual-checkpoint-v1",parent:identity(o.input),candidate:identity(o.candidate),
  sourceBindings:sources,options:input.options,curvatureOptions,geometryOptions,centralSeed:input.centralSeed||null,
  providerDefinition:provider.definition,backendDefinition:lm.backendDefinition,referenceTransition:transition,
  amplitudeIndex:position.amplitudeIndex,cutHeightIndex:metric.definition.stateLayout.cutHeight,
  heightMeaning:"Zc at the inner flat cuff; developed outer section mean is Zc minus R205 mean height",
  continuousCertificate:false,strongTargetComplete:false};
 let lambda=input.nextLambda??input.lambda??1e-3,accepted=0;
 write(o["out-prefix"]+"-initial.json",{...common,z:Array.from(z),lambda,execution:{kind:"Node",status:"initial-defined",actualAccepted:false}});
 for(let it=0;it<steps;it++){
  const t0=Date.now(),normal=provider.normal(z),normalSeconds=(Date.now()-t0)/1000;
  const r=await lm.lmStep({z,normal,lambda,maxDampingAttempts:8,alphas:[1,.5,.25],value:q=>provider.value(q),
    onTrial:q=>process.stdout.write(JSON.stringify({iteration:it+1,...q})+"\n")});
  const result={...common,z:Array.from(r.z),lambda:r.lambda,nextLambda:r.nextLambda,baseline:summary(normal),
   evaluation:r.evaluation||null,status:r.status,accepted:r.accepted,acceptedSteps:accepted+(r.accepted?1:0),
   trace:r.trace,solveInfo:r.solveInfo||null,actualValueEvaluations:r.actualValueEvaluations,
   execution:{kind:"Node",completed:true,normalSeconds,iterationSeconds:(Date.now()-t0)/1000,totalSeconds:(Date.now()-t)/1000}};
  write(o["out-prefix"]+"-"+String(it+1).padStart(2,"0")+".json",result);
  if(!r.accepted)break;z=Float64Array.from(r.z);lambda=r.nextLambda;accepted++;
 }
 return {accepted,dimension:provider.dimension,amplitude:z[position.amplitudeIndex],seconds:(Date.now()-t)/1000};
}
if(require.main===module)run(args(process.argv.slice(2))).then(r=>process.stdout.write(JSON.stringify(r)+"\n")).catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
module.exports={run};
