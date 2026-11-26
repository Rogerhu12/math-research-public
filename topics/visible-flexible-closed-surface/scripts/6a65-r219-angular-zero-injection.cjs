"use strict";
/* Same R219 cap, gap, clock, all radial channels and N128 quadrature.
 * Only the complete angular space grows; every old coefficient is copied.
 */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const {build}=require("./6a65-run-low-wide-expanded-peaks.cjs");
const {mapColumns}=require("./6a65-full-half-angular-injection.cjs");
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
function initialize(candidate,input,K){
 const start=Date.now();
 if(input.schema!=="6a65-R219-expanded-peaks-checkpoint-v1"||input.options.angles!==128||input.peakMetricRows?.length!==84||input.lowWideCapDesign?.result!=="R219")
  throw Error("Actual complete R219/N128/84-point checkpoint required");
 const J=input.options.radialBasisCount,N=input.options.angles,m=mapColumns(J,input.options.modes,K);
 if(input.z.length!==m.old.dimension||input.z.some(v=>!Number.isFinite(v))||2*K>=N/2)throw Error("Finite complete vector and sub-Nyquist new angular order required");
 const z=new Array(m.next.dimension).fill(0);m.map.forEach((i,j)=>{z[i]=input.z[j];});
 if(m.map.some((i,j)=>!Object.is(z[i],input.z[j])))throw Error("Old coefficient bit pattern changed");
 const next={schema:"6a65-R219-expanded-peaks-initial-v1",options:{...input.options,modes:K},z,
  curvatureOptions:input.curvatureOptions,geometryOptions:input.geometryOptions,centralSeed:input.centralSeed,
  metricTau:input.metricTau,gapLengthDesign:{...input.gapLengthDesign,amplitudeIndex:m.next.A,cutHeightIndex:m.next.cut},
  outerLengthDesign:input.outerLengthDesign,outerLengthFactoryOptions:input.outerLengthFactoryOptions,
  lowWideCapDesign:input.lowWideCapDesign,peakMetricRows:input.peakMetricRows,
  nextLambda:input.nextLambda,r219AcceptedSteps:0,accepted:false,
  parentCounters:{schema:input.schema,r219AcceptedSteps:input.r219AcceptedSteps},
  objectiveTransition:{actualCapAndPhysicalClockUnchanged:true,primitiveAndQuadratureUnchanged:true,
   fixed84PeakRowsUnchanged:true,acceptedOptimizationStep:false},
  angularInjection:{oldK:m.old.K,newK:K,oldDimension:m.old.dimension,newDimension:m.next.dimension,
   newColumns:m.next.dimension-m.old.dimension,allOldCoefficientsBitwiseCopied:true,newCoefficientsZero:true,
   exactRealAllChannelFieldAndOldColumnsPreserved:true,finiteStoredFieldClaimedBitwiseEqual:false},
  continuousCertificate:false,strongTargetComplete:false};
 const old=build(candidate,input),now=build(candidate,next);
 if(old.base.end!==now.base.end||old.base.height!==now.base.height||old.design.trueCuffHeight!==now.design.trueCuffHeight||
  old.design.amplitude!==now.design.amplitude||JSON.stringify(old.position.radialCuts)!==JSON.stringify(now.position.radialCuts))
  throw Error("Same-field zero extension changed physical or radial data");
 const keys=["X","Xs","Xu","Xss","Xsu","Xuu"],diff=Object.fromEntries(keys.map(k=>[k,0]));
 let colAbs=0,count=0;
 const sites=[{s:0,u:0},{s:old.base.centralLength,u:Math.PI/2},{s:.13995229881993795,u:0},
  {s:.4491089374465381,u:1.5953400194010667},{s:.7,u:.31},{s:old.base.end,u:.7}];
 for(const {s,u}of sites){
  const a=old.position.slice(s,old.z,true).point(u),b=now.position.slice(s,now.z,true).point(u);
  for(const key of keys)for(let j=0;j<3;j++)diff[key]=Math.max(diff[key],Math.abs(a.jets[key][j]-b.jets[key][j]));
  const cols=new Map(b.indices.map((idx,j)=>[idx,b.parameterJets[j]]));
  for(let j=0;j<a.indices.length;j++){
   const av=a.parameterJets[j],bv=cols.get(m.map[a.indices[j]]);if(!bv)throw Error("Missing old active column");
   for(const key of keys)for(let k=0;k<3;k++){colAbs=Math.max(colAbs,Math.abs(av[key][k]-bv[key][k]));count++;}
  }
  old.position.clearSliceReuse?.();now.position.clearSliceReuse?.();if(global.gc)global.gc();
 }
 const baseline=now.provider.value(now.z);now.position.clearSliceReuse?.();if(global.gc)global.gc();
 next.z=Array.from(now.z);next.baseline=baseline;next.providerDefinition=now.provider.definition;
 next.gapLengthDesign=now.design;next.geometryOptions=now.geometryOptions;
 return {initial:next,report:{schema:"6a65-R219-complete-angular-zero-injection-v1",oldDimension:m.old.dimension,newDimension:m.next.dimension,
  oldK:m.old.K,newK:K,newColumns:m.next.dimension-m.old.dimension,unchangedN:N,
  completeTwoJetProbeMaxDifferences:diff,oldColumnProbe:{maximumAbsolute:colAbs,scalarCount:count},probeSites:sites,
  freshCompleteBaseline:baseline,acceptedOptimizationStep:false,seconds:(Date.now()-start)/1000,
  continuousCertificate:false,strongTargetComplete:false}};
}
module.exports={initialize};
if(require.main===module){
 const[candidateFile,stateFile,kText,prefix]=process.argv.slice(2);
 if(!candidateFile||!stateFile||!kText||!prefix||fs.existsSync(prefix+"-initial.json")||fs.existsSync(prefix+"-report.json"))
  throw Error("candidate actual-R219-state new-K fresh-prefix");
 const r=initialize(JSON.parse(fs.readFileSync(candidateFile)),JSON.parse(fs.readFileSync(stateFile)),Number(kText));
 r.initial.source={inputSHA256:hash(stateFile),candidateSHA256:hash(candidateFile),scriptSHA256:hash(__filename),
  columnMapSHA256:hash(path.join(__dirname,"6a65-full-half-angular-injection.cjs"))};r.report.source=r.initial.source;
 fs.mkdirSync(path.dirname(prefix),{recursive:true});fs.writeFileSync(prefix+"-initial.json",JSON.stringify(r.initial)+"\n");
 r.report.initialSHA256=hash(prefix+"-initial.json");fs.writeFileSync(prefix+"-report.json",JSON.stringify(r.report,null,2)+"\n");
 process.stdout.write(JSON.stringify({event:"initial",oldDimension:r.report.oldDimension,newDimension:r.report.newDimension,
  newColumns:r.report.newColumns,oldK:r.report.oldK,newK:r.report.newK,twoJetDifferences:r.report.completeTwoJetProbeMaxDifferences,
  oldColumnProbe:r.report.oldColumnProbe,total:r.initial.baseline.squaredNorm,metric:r.initial.baseline.maxRelativeMetric,
  curvature:r.initial.baseline.curvature.maxCurvature,seconds:r.report.seconds,
  initialSHA256:r.report.initialSHA256,reportSHA256:hash(prefix+"-report.json"),accepted:false})+"\n");
}
