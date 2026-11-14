"use strict";
/* Reproducible R201 actual branch driver. Node only; pure V8 uses the same
 * exported factories and explicitly records its own execution instead.
 * No model or table interpolation replaces complete angular functions.
 */
const fs=require("fs"),path=require("path"),crypto=require("crypto");
const {createR187}=require("./fd2d-direct-position-tangent-lift-baseline-R187.cjs");
const {createR196CubicSplines}=require("./fd2d-cubic-spline-refinement-R196.cjs");
const {createR196MetricProvider}=require("./fd2d-nonuniform-metric-provider-R196.cjs");
const {createR191Algebra}=require("./fd2d-position-curvature-chain-R191.cjs");
const {createR201R196Provider}=require("./fd2d-full-half-phase-position-provider-R201.cjs");
const {createR201GeometryProvider}=require("./fd2d-full-half-position-geometric-guide-R201.cjs");
const kernel=require("./fd2d-full-half-band-border-kernel-R201.cjs");
const {createBandBorderLM}=require("./fd2d_band_border_lm_adapter_v2_R195.cjs");
const sources=["fd2d-direct-position-tangent-lift-baseline-R187.cjs","fd2d-cubic-spline-refinement-R196.cjs","fd2d-nonuniform-metric-provider-R196.cjs","fd2d-position-curvature-chain-R191.cjs","fd2d-full-half-phase-position-provider-R201.cjs","fd2d-full-half-position-geometric-guide-R201.cjs","fd2d-full-half-band-border-kernel-R201.cjs","fd2d_band_border_lm_adapter_v2_R195.cjs","fd2d-run-full-half-position-R201.cjs"];
const hash=s=>crypto.createHash("sha256").update(s).digest("hex");
function identity(file){const b=fs.readFileSync(file);return{path:file,bytes:b.length,sha256:hash(b)};}
function write(file,data){fs.mkdirSync(path.dirname(file),{recursive:true});fs.writeFileSync(file,JSON.stringify(data,null,2)+"\n");}
function args(argv){const a={};for(let i=0;i<argv.length;i+=2){if(!argv[i].startsWith("--")||argv[i+1]===undefined)throw Error("Use --key value");a[argv[i].slice(2)]=argv[i+1];}return a;}
async function run(o){
 if(!o.input||!o.candidate||!o["out-prefix"])throw Error("--input --candidate --out-prefix required");
 const start=Date.now(),input=JSON.parse(fs.readFileSync(o.input,"utf8")),bundle=JSON.parse(fs.readFileSync(o.candidate,"utf8")),
 engine=createR187(),splines=createR196CubicSplines(),algebra=createR191Algebra(),
 met=createR196MetricProvider(engine,bundle,input.options,splines),
 pos=createR201R196Provider(engine,met,input.curvatureOptions||{guide:9.5,weight:.01,nodeShare:.5},algebra),
 geoOptions=input.geometryOptions||{radius:1.59,width:.84,held:.65,weight:10,nodeShare:.5,cutWindow:[.41,.62]},
 provider=createR201GeometryProvider(pos,geoOptions),bindings=Object.fromEntries(sources.map(n=>[n,identity(path.join(__dirname,n))])),
 backend=createBandBorderLM(kernel,provider.definition,{halfBandwidthBlocks:4,kernelSourceSHA256:bindings["fd2d-full-half-band-border-kernel-R201.cjs"].sha256});
 const inherited=input.schema==="fd2d-R201-full-half-actual-checkpoint-v1";
 let z;if(inherited){if(input.z.length!==provider.dimension||JSON.stringify(input.providerDefinition.radialBasisDefinition)!==JSON.stringify(provider.definition.radialBasisDefinition))throw Error("Saved R201 dimension/basis mismatch");z=Float64Array.from(input.z);}
 else z=pos.injectLegacy(input.z);
 let changes=[];if(o["warm-changes"]){changes=JSON.parse(fs.readFileSync(o["warm-changes"],"utf8"));for(const q of changes){if(!Number.isInteger(q.index)||q.index<met.dimension||q.index>=z.length||!Number.isFinite(q.value))throw Error("Explicit appended warm coefficient required");z[q.index]=q.value;}}
 const steps=o.steps===undefined?1:Number(o.steps);if(!Number.isInteger(steps)||steps<0)throw Error("Nonnegative finite steps");
 let lambda=input.nextLambda??input.lambda??1e-3,accepted=0;
 const common={schema:"fd2d-R201-full-half-actual-checkpoint-v1",parent:identity(o.input),candidate:identity(o.candidate),sourceBindings:bindings,options:input.options,
 curvatureOptions:input.curvatureOptions||{guide:9.5,weight:.01,nodeShare:.5},geometryOptions:geoOptions,
 providerDefinition:provider.definition,backendDefinition:backend.backendDefinition,centralSeed:input.centralSeed||null,
 legacyInjection:{performed:!inherited,legacyDimension:met.dimension,newDimension:provider.dimension,completeLegacyPrefixCopied:true},
 warmChanges:changes,continuousCertificate:false,strongTargetComplete:false};
 write(o["out-prefix"]+"-initial.json",{...common,z:Array.from(z),lambda,execution:{kind:"Node",status:"initial-defined",actualAccepted:false}});
 for(let k=0;k<steps;k++){
  const t=Date.now(),normal=provider.normal(z),baseline={...normal};delete baseline.H;delete baseline.g;delete baseline.diagonal;
  const r=await backend.lmStep({z,normal,value:v=>provider.value(v),lambda,maxDampingAttempts:8,alphas:[1,.5,.25],
   onTrial:x=>process.stdout.write(JSON.stringify({iteration:k+1,...x})+"\n")});
  const packet={...common,z:Array.from(r.z),lambda:r.lambda,nextLambda:r.nextLambda,baseline,evaluation:r.evaluation||null,
   trace:r.trace,solveInfo:r.solveInfo||null,status:r.status,accepted:r.accepted,actualValueEvaluations:r.actualValueEvaluations,
   acceptedSteps:accepted+(r.accepted?1:0),execution:{kind:"Node",completed:true,iterationSeconds:(Date.now()-t)/1000,totalSeconds:(Date.now()-start)/1000}};
  write(o["out-prefix"]+"-"+String(k+1).padStart(2,"0")+".json",packet);
  if(!r.accepted)break;z=Float64Array.from(r.z);lambda=r.nextLambda;accepted++;
 }
 return{accepted,dimension:provider.dimension,seconds:(Date.now()-start)/1000};
}
if(require.main===module)run(args(process.argv.slice(2))).then(r=>process.stdout.write(JSON.stringify(r)+"\n")).catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
module.exports={run};
