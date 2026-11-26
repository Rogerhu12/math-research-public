"use strict";
/* Consume the complete angular zero map on the explicitly saved stretched
 * R215 branch. Keep its clock, gap, height transfer, target and fixed rows. */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const {mapColumns}=require("./6a65-full-half-angular-injection.cjs");
const factory=require("./6a65-geometry-gap-length-value.cjs").createGapLengthState;
const peaks=require("./6a65-geometry-fixed-peak-metric.cjs").createFixedPeakMetricProvider;
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
function inject(candidate,input,K){
 if(input.schema!=="6a65-fixed-peak-metric-R215-checkpoint-v1"||!input.gapLengthDesign||!input.outerLengthDesign||!Array.isArray(input.peakMetricRows))throw Error("Actual complete saved R215 fixed-peak input required");
 const J=input.options.radialBasisCount,N=input.options.angles,m=mapColumns(J,input.options.modes,K);
 if(input.z.length!==m.old.dimension||input.z.some(v=>!Number.isFinite(v))||2*K>=N/2)throw Error("Complete layout and unchanged sub-Nyquist N required");
 const z=new Array(m.next.dimension).fill(0);m.map.forEach((i,j)=>{z[i]=input.z[j];});
 if(m.map.some((i,j)=>!Object.is(z[i],input.z[j])))throw Error("Changed old coefficient");
 const next={schema:"6a65-fixed-peak-angular-initial-v1",options:{...input.options,modes:K},z,
  curvatureOptions:input.curvatureOptions,geometryOptions:input.geometryOptions,centralSeed:input.centralSeed,
  gapLengthDesign:{...input.gapLengthDesign,amplitudeIndex:m.next.A,cutHeightIndex:m.next.cut},
  outerLengthDesign:input.outerLengthDesign,outerLengthFactoryOptions:input.outerLengthFactoryOptions,
  peakMetricRows:input.peakMetricRows,nextLambda:input.nextLambda,metricTau:input.gapLengthDesign.metricTau,
  peakMetricAcceptedSteps:0,gapLengthAcceptedSteps:input.gapLengthAcceptedSteps,accepted:false,
  parent:{schema:input.schema,peakMetricAcceptedSteps:input.peakMetricAcceptedSteps,gapLengthAcceptedSteps:input.gapLengthAcceptedSteps},
  angularInjection:{oldK:m.old.K,newK:K,oldDimension:m.old.dimension,newDimension:m.next.dimension,
   newColumns:m.next.dimension-m.old.dimension,allOldColumnsBitwiseCopied:true,newCoefficientsZero:true,
   physicalClockAndMetricInitiallyUnchanged:true,primitiveAndQuadratureUnchanged:true,
   fixedPeakPointRowsUnchanged:true,acceptedOptimizationStep:false},
  continuousCertificate:false,strongTargetComplete:false};
 const old=factory(candidate,input),now=factory(candidate,next);
 if(old.base.end!==now.base.end||old.base.height!==now.base.height||
  old.design.trueCuffHeight!==now.design.trueCuffHeight||old.design.amplitude!==now.design.amplitude)
  throw Error("Physical background, actual cuff or amplitude changed");
 if(JSON.stringify(old.position.radialCuts)!==JSON.stringify(now.position.radialCuts))throw Error("Radial quadrature changed");
 const keys=["X","Xs","Xu","Xss","Xsu","Xuu"],jet=Object.fromEntries(keys.map(k=>[k,0]));
 let colAbs=0,colRelative=0,count=0;
 const sites=[{s:0,u:0},{s:old.base.centralLength,u:Math.PI/2},{s:.2346108715251372,u:0},
  {s:.4,u:.71},{s:.7,u:Math.PI/2},{s:old.base.end,u:0}];
 for(const {s,u}of sites){
  const a=old.position.slice(s,old.z,true).point(u),b=now.position.slice(s,now.z,true).point(u);
  const cols=new Map(b.indices.map((i,j)=>[i,b.parameterJets[j]]));
  for(const key of keys)for(let k=0;k<3;k++)jet[key]=Math.max(jet[key],Math.abs(a.jets[key][k]-b.jets[key][k]));
  for(let j=0;j<a.indices.length;j++){
   const v=a.parameterJets[j],w=cols.get(m.map[a.indices[j]]);if(!w)throw Error("Missing old active column");
   for(const key of keys)for(let k=0;k<3;k++){
    const d=Math.abs(v[key][k]-w[key][k]);colAbs=Math.max(colAbs,d);colRelative=Math.max(colRelative,d/Math.max(1,Math.abs(v[key][k]),Math.abs(w[key][k])));count++;
   }
  }
  old.position.clearSliceReuse?.();now.position.clearSliceReuse?.();if(global.gc)global.gc();
 }
 const provider=peaks(now.provider,now.metricPosition,next.peakMetricRows),baseline=provider.value(now.z);
 next.z=now.z;next.baseline=baseline;next.providerDefinition=provider.definition;
 return {initial:next,report:{schema:"6a65-R215-fixed-peak-angular-zero-injection-diagnostic-v1",
  oldDimension:m.old.dimension,newDimension:m.next.dimension,newColumns:m.next.dimension-m.old.dimension,
  oldK:m.old.K,newK:K,originalN:N,maxJetDifferences:jet,
  oldColumnProbeDifferences:{absolute:colAbs,relative:colRelative,scalarCount:count},
  actualA:now.design.amplitude,actualZ:now.design.trueCuffHeight,baseline,
  exactSameFiniteFieldByZeroExtension:true,acceptedSteps:0,continuousCertificate:false,strongTargetComplete:false}};
}
module.exports={inject};
if(require.main===module){
 const [candidateFile,inputFile,kText,prefix]=process.argv.slice(2);
 if(!candidateFile||!inputFile||!prefix||fs.existsSync(prefix+"-initial.json"))throw Error("candidate input newK fresh-prefix required");
 const t=Date.now(),r=inject(JSON.parse(fs.readFileSync(candidateFile)),JSON.parse(fs.readFileSync(inputFile)),Number(kText));
 r.initial.parent={...r.initial.parent,inputFile,inputSHA256:hash(inputFile)};
 r.report.source={inputSHA256:hash(inputFile),candidateSHA256:hash(candidateFile),scriptSHA256:hash(__filename),columnMapSHA256:hash(path.join(__dirname,"6a65-full-half-angular-injection.cjs"))};
 r.report.seconds=(Date.now()-t)/1000;
 fs.mkdirSync(path.dirname(prefix),{recursive:true});fs.writeFileSync(prefix+"-initial.json",JSON.stringify(r.initial)+"\n");
 r.report.initialSHA256=hash(prefix+"-initial.json");fs.writeFileSync(prefix+"-report.json",JSON.stringify(r.report,null,2)+"\n");
 process.stdout.write(JSON.stringify({oldDimension:r.report.oldDimension,newDimension:r.report.newDimension,
  newColumns:r.report.newColumns,R2:r.report.baseline.squaredNorm,metric:r.report.baseline.maxRelativeMetric,
  curvature:r.report.baseline.curvature.maxCurvature,jetDifferences:r.report.maxJetDifferences,
  columnDifferences:r.report.oldColumnProbeDifferences,A:r.report.actualA,Z:r.report.actualZ,
  seconds:r.report.seconds,initialSHA256:r.report.initialSHA256,reportSHA256:hash(prefix+"-report.json")})+"\n");
}
