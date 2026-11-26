"use strict";
/* Consume an actual same-state observer on the R219 stretched physical span.
 * R208 prolongs EVERY radial channel with exact rational Boehm weights.
 * The complete new value is rebuilt; new quadrature is not an accepted step.
 */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const {build}=require("./6a65-run-low-wide-expanded-peaks.cjs");
const {prolongR201R205State}=require("./fd2d-R201-R205-complete-radial-prolongation.cjs");
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
function gcd(a,b){while(b){const r=a%b;a=b;b=r;}return a<0n?-a:a;}
function midpoint(a,b){
 const n=BigInt(a[0])*BigInt(b[1])+BigInt(b[0])*BigInt(a[1]),d=2n*BigInt(a[1])*BigInt(b[1]),g=gcd(n,d);
 return [(n/g).toString(),(d/g).toString()];
}
function select(candidate,input,observation,target="both"){
 if(!["metric","curvature","both"].includes(target))throw Error("metric, curvature or both target required");
 if(input.schema!=="6a65-R219-expanded-peaks-checkpoint-v1"||input.options.angles!==128||input.peakMetricRows?.length!==84||input.lowWideCapDesign?.result!=="R219")
  throw Error("Complete actual R219 checkpoint required");
 if(observation.schema!=="6a65-gap-clock-same-field-refined-metric-observation-v1"||
  observation.dimension!==input.z.length||observation.originalAngularRule!==input.options.angles||
  !observation.fieldCoefficientsUnchanged||!observation.physicalMetricUnchanged||!observation.sourceAngularPrimitiveUnchanged)
  throw Error("Same-state explicit stretched-clock observer required");
 const old=build(candidate,input),c=old.base.centralLength,S=old.base.end,L=S-c;
 const knots=input.options.radialKnots,x=knots.map(v=>Number(v[0])/Number(v[1])),selected=new Map(),decisions=[];
 for(const key of target==="both"?["worstMetric","worstCurvature"]:[target==="metric"?"worstMetric":"worstCurvature"]){
  const peak=observation[key];if(!peak||!Number.isFinite(peak.s)||!Number.isFinite(peak.u))throw Error("Finite observed peak required");
  const q=(peak.s-c)/L,spans=[];
  if(!(q>0&&q<1)){decisions.push({source:key,s:peak.s,u:peak.u,q,action:"Outside open flexible span; no radial insertion"});continue;}
  const at=x.findIndex(t=>Math.abs(t-q)<=1e-12);
  if(at>0&&at<x.length-1){
   if(x[at]-x[at-1]>0)spans.push(at-1);
   if(x[at+1]-x[at]>0)spans.push(at);
  }else{
   const i=x.findIndex((t,i)=>i+1<x.length&&q>=t&&q<x[i+1]);
   if(i<0)throw Error("Observed peak in no declared radial knot span");spans.push(i);
  }
  const inserted=spans.map(i=>midpoint(knots[i],knots[i+1]));
  for(const k of inserted)selected.set(k.join("/"),k);
  decisions.push({source:key,s:peak.s,u:peak.u,q,oldSpans:spans.map(i=>[knots[i],knots[i+1]]),insertedKnots:inserted,
   action:at>0?"Adjacent span midpoint(s) at an observed knot":"Containing span midpoint"});
 }
 const insertedKnots=Array.from(selected.values()).sort((a,b)=>Number(a[0])/Number(a[1])-Number(b[0])/Number(b[1]));
 if(!insertedKnots.length)throw Error("No interior observed peak selected");
 return {old,selection:{insertedKnots,decisions,physicalSpan:{c,S,L},selectionIsFiniteNumerical:true,continuousPeakLocalizationClaimed:false}};
}
function initialize(candidate,input,observation,target="both"){
 const start=Date.now(),{old,selection}=select(candidate,input,observation,target);
 const J=input.options.radialBasisCount,K=input.options.modes,cut=J*(2*K+1),A=J*(4*K+3)+1;
 if(old.cutHeightIndex!==cut||old.position.amplitudeIndex!==A||input.z.length!==A+1)throw Error("Actual complete stretched factory layout mismatch");
 const mapped=prolongR201R205State({schema:"fd2d-R201-R205-variable-amplitude-actual-checkpoint-v1",
  options:input.options,z:input.z,cutHeightIndex:cut,amplitudeIndex:A,curvatureOptions:input.curvatureOptions,
  geometryOptions:input.geometryOptions,centralSeed:input.centralSeed,nextLambda:input.nextLambda},selection.insertedKnots);
 const next={schema:"6a65-R219-expanded-peaks-initial-v1",options:mapped.options,z:mapped.z,
  curvatureOptions:input.curvatureOptions,geometryOptions:input.geometryOptions,centralSeed:input.centralSeed,
  metricTau:input.metricTau,gapLengthDesign:{...input.gapLengthDesign,amplitudeIndex:mapped.amplitudeIndex,cutHeightIndex:mapped.cutHeightIndex},
  outerLengthDesign:input.outerLengthDesign,outerLengthFactoryOptions:input.outerLengthFactoryOptions,
  lowWideCapDesign:input.lowWideCapDesign,peakMetricRows:input.peakMetricRows,
  nextLambda:input.nextLambda,r219AcceptedSteps:0,accepted:false,
  parentCounters:{schema:input.schema,r219AcceptedSteps:input.r219AcceptedSteps},
  objectiveTransition:{actualCapAndPhysicalClockUnchanged:true,primitiveAndAngularRuleUnchanged:true,
   fixed84PeakRowsUnchanged:true,radialQuadratureChanged:true,acceptedOptimizationStep:false},
  radialRefinement:{method:"R208 exact rational all-channel Boehm insertion with one final binary64 rounding",
   selection,insertedKnots:mapped.insertedKnots,oldDimension:mapped.oldDimension,newDimension:mapped.newDimension,
   oldRadialCount:mapped.oldRadialCount,newRadialCount:mapped.newRadialCount,
   exactRealAllChannelFieldPreserved:true,finiteStoredFieldClaimedBitwiseEqual:false,
   globalCutAndAmplitudeCopiedByObjectIs:true,storedSplineRoundoffBounds:mapped.storedSplineRoundoffBounds,
   nonlinearRoundoffPropagationAndBasisEvaluationNotCertified:true,
   newRadialQuadratureRequiresFreshBaseline:true},continuousCertificate:false,strongTargetComplete:false};
 const now=build(candidate,next);
 if(old.base.end!==now.base.end||old.base.height!==now.base.height||old.base.centralLength!==now.base.centralLength||
    old.design.trueCuffHeight!==now.design.trueCuffHeight||old.design.amplitude!==now.design.amplitude)
  throw Error("Changed physical interval, background, actual cut height or amplitude");
 const keys=["X","Xs","Xu","Xss","Xsu","Xuu"],diff=Object.fromEntries(keys.map(k=>[k,0]));
 const c=old.base.centralLength,S=old.base.end,sites=[{s:0,u:0},{s:c,u:Math.PI/2},
  {s:observation.worstMetric.s,u:observation.worstMetric.u},{s:observation.worstCurvature.s,u:observation.worstCurvature.u},
  {s:c+(S-c)*.5,u:.7},{s:S,u:.31}];
 for(const {s,u}of sites){
  const a=old.position.slice(s,old.z,false).point(u),b=now.position.slice(s,now.z,false).point(u);
  for(const key of keys)for(let j=0;j<3;j++)diff[key]=Math.max(diff[key],Math.abs(a.jets[key][j]-b.jets[key][j]));
  old.position.clearSliceReuse?.();now.position.clearSliceReuse?.();if(global.gc)global.gc();
 }
 const baseline=now.provider.value(now.z);now.position.clearSliceReuse?.();if(global.gc)global.gc();
 next.z=Array.from(now.z);next.baseline=baseline;next.gapLengthDesign=now.design;next.geometryOptions=now.geometryOptions;
 next.providerDefinition=now.provider.definition;
 return {initial:next,report:{schema:"6a65-R219-observed-peak-radial-insertion-v1",selection,
  oldDimension:mapped.oldDimension,newDimension:mapped.newDimension,oldRadialCount:J,newRadialCount:mapped.newRadialCount,
  allChannelRoundoffBounds:mapped.storedSplineRoundoffBounds,completeTwoJetProbeMaxDifferences:diff,probeSites:sites,
  freshCompleteBaseline:baseline,acceptedOptimizationStep:false,seconds:(Date.now()-start)/1000,
  continuousCertificate:false,strongTargetComplete:false}};
}
module.exports={select,initialize};
if(require.main===module){
 const[candidateFile,stateFile,observerFile,prefix,target="both"]=process.argv.slice(2);
 if(!candidateFile||!stateFile||!observerFile||!prefix||fs.existsSync(prefix+"-initial.json")||fs.existsSync(prefix+"-report.json"))
  throw Error("candidate actual-R219-state same-state-observer fresh-prefix [metric|curvature|both]");
 const input=JSON.parse(fs.readFileSync(stateFile)),observer=JSON.parse(fs.readFileSync(observerFile));
 if(observer.inputs?.inputSHA256!==hash(stateFile)||observer.inputs?.candidateSHA256!==hash(candidateFile))
  throw Error("Observer does not identify these exact source bytes");
 const r=initialize(JSON.parse(fs.readFileSync(candidateFile)),input,observer,target);
 r.initial.source={inputSHA256:hash(stateFile),observerSHA256:hash(observerFile),candidateSHA256:hash(candidateFile),
  scriptSHA256:hash(__filename),prolongationSHA256:hash(path.join(__dirname,"fd2d-R201-R205-complete-radial-prolongation.cjs"))};
 r.report.source=r.initial.source;
 fs.mkdirSync(path.dirname(prefix),{recursive:true});fs.writeFileSync(prefix+"-initial.json",JSON.stringify(r.initial)+"\n");
 r.report.initialSHA256=hash(prefix+"-initial.json");fs.writeFileSync(prefix+"-report.json",JSON.stringify(r.report,null,2)+"\n");
 process.stdout.write(JSON.stringify({event:"initial",oldDimension:r.report.oldDimension,newDimension:r.report.newDimension,
  selectedKnots:r.report.selection.insertedKnots,twoJetDifferences:r.report.completeTwoJetProbeMaxDifferences,
  total:r.initial.baseline.squaredNorm,metric:r.initial.baseline.maxRelativeMetric,
  curvature:r.initial.baseline.curvature.maxCurvature,seconds:r.report.seconds,
  initialSHA256:r.report.initialSHA256,reportSHA256:hash(prefix+"-report.json"),accepted:false})+"\n");
}
