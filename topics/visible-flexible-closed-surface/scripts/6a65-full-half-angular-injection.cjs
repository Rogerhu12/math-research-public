"use strict";
/* Zero-extend every R201 angular channel, including both cosine families.
 * Retain the original radial basis, all physical scalars, N-angle primitive,
 * quadrature and interfaces. No coefficient rounding or old column deletion.
 * The subsequent solver still changes rho as a design variable. */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const make=require("./6a65-low-memory-r211-provider-recovered-20261126.cjs").createMemoryBoundR211RunProvider;
const quartic=require("./6a65-quartic-metric-recovered-20261126.cjs").createQuarticMetricProvider;
const guide=require("./fd2d-R201-R205-variable-amplitude-geometric-guide.cjs").createR201R205AmplitudeGeometryProvider;
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
function completeLayout(J,K){
 if(!Number.isInteger(J)||J<1||!Number.isInteger(K)||K<1)throw Error("Positive integer J,K required");
 const height=2*J*K,cut=height+J,radius=cut+1,extra=radius+J,A=J*(4*K+3)+1;
 return {J,K,height,cut,radius,extra,A,dimension:A+1};
}
function mapColumns(J,K,KK){
 if(!Number.isInteger(KK)||KK<=K)throw Error("Strict angular enlargement required");
 const a=completeLayout(J,K),b=completeLayout(J,KK),map=new Array(a.dimension).fill(-1);
 for(let j=0;j<J;j++){
  for(let k=0;k<K;k++){
   map[j*K+k]=j*KK+k;
   map[J*K+j*K+k]=J*KK+j*KK+k;
   map[a.extra+j*(2*K+1)+1+k]=b.extra+j*(2*KK+1)+1+k;
   map[a.extra+j*(2*K+1)+1+K+k]=b.extra+j*(2*KK+1)+1+KK+k;
  }
  map[a.height+j]=b.height+j;map[a.radius+j]=b.radius+j;
  map[a.extra+j*(2*K+1)]=b.extra+j*(2*KK+1);
 }
 map[a.cut]=b.cut;map[a.A]=b.A;
 if(map.some(i=>i<0)||new Set(map).size!==map.length)throw Error("Incomplete/noninjective complete old-column map");
 return {old:a,next:b,map};
}
function inject(input,KK){
 const allowed=new Set(["6a65-R211-quartic-metric-checkpoint-v1","6a65-R211-radial-refinement-initial-v1","6a65-R211-angular-injection-initial-v1"]);
 if(!allowed.has(input.schema)||input.outerLengthDesign||input.gapLengthDesign)throw Error("Original unextended recovered quartic representation required");
 const o=input.options,m=mapColumns(o?.radialBasisCount,o?.modes,KK);
 if(!Array.isArray(input.z)||input.z.length!==m.old.dimension||input.z.some(x=>!Number.isFinite(x)))throw Error("Complete finite input vector required");
 if(!Number.isInteger(o.angles)||o.angles%4||2*KK>=o.angles/2)throw Error("Keep original primitive and modes strictly below its nodal Nyquist frequency");
 const z=new Array(m.next.dimension).fill(0);m.map.forEach((i,j)=>{z[i]=input.z[j];});
 if(m.map.some((i,j)=>!Object.is(z[i],input.z[j])))throw Error("Old coefficient bit pattern changed");
 const next={schema:"6a65-R211-angular-injection-initial-v1",options:{...o,modes:KK},z,
  curvatureOptions:input.curvatureOptions,geometryOptions:input.geometryOptions,centralSeed:input.centralSeed??null,
  metricTau:input.metricTau,nextLambda:input.nextLambda??input.lambda??1e-3,
  amplitudeIndex:m.next.A,cutHeightIndex:m.next.cut,
  metricBranchAcceptedSteps:0,acceptedSteps:0,accepted:false,
  parent:{schema:input.schema,acceptedSteps:input.metricBranchAcceptedSteps??null},
  angularInjection:{oldK:m.old.K,newK:KK,oldDimension:m.old.dimension,newDimension:m.next.dimension,
   newColumns:4*m.old.J*(KK-m.old.K),allOldColumnsMapped:true,oldCoefficientsBitwiseCopied:true,
   newColumnsZero:true,radialBasisUnchanged:true,physicalMetricInitiallyUnchanged:true,
   sourceAngularPrimitiveUnchanged:true,quadratureUnchanged:true,acceptedOptimizationStep:false,
   sameExactFiniteField:true,floatingPointFieldBitwiseEqualityNotAssumed:true},
  continuousCertificate:false,strongTargetComplete:false};
 return {...m,initial:next};
}
function diagnose(candidate,input,KK){
 const start=Date.now(),m=inject(input,KK),old=make(candidate,input),now=make(candidate,m.initial),keys=["X","Xs","Xu","Xss","Xsu","Xuu"];
 if(old.position.amplitudeIndex!==m.old.A||now.position.amplitudeIndex!==m.next.A||
   old.metric.definition.stateLayout.cutHeight!==m.old.cut||now.metric.definition.stateLayout.cutHeight!==m.next.cut)
  throw Error("Actual factories disagree with complete column map");
 if(JSON.stringify(old.metric.radialCuts)!==JSON.stringify(now.metric.radialCuts))throw Error("Radial quadrature changed");
 const c=old.metric.base.centralLength,S=old.metric.base.end,L=S-c;
 const sites=[{s:0,u:0},{s:c,u:Math.PI/2},{s:.1359375,u:Math.PI},
  {s:c+L*.25,u:.78},{s:c+L*.6,u:1.24},{s:c+L*.9,u:Math.PI*37/64},{s:S,u:0}];
 const jets=Object.fromEntries(keys.map(k=>[k,0])),columns={absolute:0,relative:0,count:0};
 for(const {s,u}of sites){
  const a=old.position.slice(s,input.z,true).point(u),b=now.position.slice(s,m.initial.z,true).point(u);
  for(const key of keys)for(let i=0;i<3;i++)jets[key]=Math.max(jets[key],Math.abs(a.jets[key][i]-b.jets[key][i]));
  const newColumns=new Map(b.indices.map((idx,j)=>[idx,b.parameterJets[j]]));
  for(let j=0;j<a.indices.length;j++){
   const av=a.parameterJets[j],bv=newColumns.get(m.map[a.indices[j]]);
   if(!bv)throw Error("Lost an old active parameter column");
   for(const key of keys)for(let i=0;i<3;i++){
    const d=Math.abs(av[key][i]-bv[key][i]);columns.absolute=Math.max(columns.absolute,d);
    columns.relative=Math.max(columns.relative,d/Math.max(1,Math.abs(av[key][i]),Math.abs(bv[key][i])));columns.count++;
   }
  }
  old.position.clearSliceReuse();now.position.clearSliceReuse();if(global.gc)global.gc();
 }
 const p=quartic(now.position,now.engine,input.metricTau),provider=guide(p,input.geometryOptions),baseline=provider.value(m.initial.z);
 m.initial.providerDefinition=provider.definition;m.initial.baseline=baseline;
 return {initial:m.initial,report:{schema:"6a65-complete-angular-zero-injection-diagnostic-v1",
  oldDimension:m.old.dimension,newDimension:m.next.dimension,newColumns:m.next.dimension-m.old.dimension,
  oldK:m.old.K,newK:KK,originalN:input.options.angles,quadratureUnchanged:true,
  physicalSpan:{c,S},maxJetDifferences:jets,allOldColumnProbeDifferences:columns,probeCount:sites.length,
  exactZeroInjectionDoesNotNeedCoefficientRounding:true,freshCompleteBaseline:baseline,
  acceptanceCount:0,seconds:(Date.now()-start)/1000,continuousCertificate:false,strongTargetComplete:false}};
}
module.exports={completeLayout,mapColumns,inject,diagnose};
if(require.main===module){
 const [candidateFile,inputFile,kText,prefix]=process.argv.slice(2);
 if(!candidateFile||!inputFile||!kText||!prefix||fs.existsSync(prefix+"-initial.json")||fs.existsSync(prefix+"-report.json"))throw Error("candidate input newK fresh-prefix required");
 const input=JSON.parse(fs.readFileSync(inputFile)),r=diagnose(JSON.parse(fs.readFileSync(candidateFile)),input,Number(kText));
 r.initial.parent={...r.initial.parent,inputFile,inputSHA256:hash(inputFile)};
 r.report.source={inputSHA256:hash(inputFile),candidateSHA256:hash(candidateFile),scriptSHA256:hash(__filename)};
 fs.mkdirSync(path.dirname(prefix),{recursive:true});fs.writeFileSync(prefix+"-initial.json",JSON.stringify(r.initial)+"\n");
 r.report.initialSHA256=hash(prefix+"-initial.json");fs.writeFileSync(prefix+"-report.json",JSON.stringify(r.report,null,2)+"\n");
 process.stdout.write(JSON.stringify({dimension:r.initial.z.length,newColumns:r.report.newColumns,
  R2:r.report.freshCompleteBaseline.squaredNorm,metric:r.report.freshCompleteBaseline.maxRelativeMetric,
  curvature:r.report.freshCompleteBaseline.curvature.maxCurvature,maxJetDifferences:r.report.maxJetDifferences,
  oldColumnDifferences:r.report.allOldColumnProbeDifferences,seconds:r.report.seconds,
  initialSHA256:r.report.initialSHA256,reportSHA256:hash(prefix+"-report.json"),accepted:false})+"\n");
}
