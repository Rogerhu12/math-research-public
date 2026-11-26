"use strict";
/* Recovered v2: observe the saved short-Cauchy field through its actual
 * factory. Extra sample sites do not change its primitive, coefficients,
 * designed metric, or physical clock. This is not a continuous certificate. */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const branch=require("./6a65-cauchy-global-position.cjs");
const consumer=require("./6a65-run-cauchy-same-job-recovered-v2.cjs");
const SCHEMA="6a65-Cauchy-same-field-refined-metric-observation-v1";
const WIRE_SCHEMA="6a65-gap-clock-same-field-refined-metric-observation-v1";
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
const digest=x=>crypto.createHash("sha256").update(JSON.stringify(x)).digest("hex");
function observe(candidate,input,options={}){
  const source=consumer.assertState(input,options.candidateSHA256);
  const subdivisions=options.subdivisions??4,angularIntervals=options.angularIntervals??256;
  if(!Number.isInteger(subdivisions)||subdivisions<1||subdivisions>32||
      !Number.isInteger(angularIntervals)||angularIntervals<2||angularIntervals>512)
    throw Error("Explicit bounded radial subdivisions and half-period angular intervals required");
  const built=branch.build(candidate,input),p=built.position,z=Array.from(built.z);
  if(z.length!==input.z.length||z.some((v,i)=>!Object.is(v,input.z[i])))
    throw Error("The actual Cauchy observation changed a saved coefficient");
  const md=p.definition.parentMetric,N=md.fullEquivalentAngles,nativeHalf=N/2,centralA=md.centralA;
  if(N!==input.options.angles||!Number.isInteger(nativeHalf)||nativeHalf<1||
      !Number.isFinite(centralA)||centralA<1.4)
    throw Error("The saved angular primitive and actual central support are required");
  const cuts=Array.from(p.radialCuts),end=built.base.end;
  if(cuts[0]!==0||cuts.at(-1)!==end||
      cuts.some((s,i)=>!Number.isFinite(s)||(i>0&&s<=cuts[i-1])))
    throw Error("The actual complete physical half-core cuts are required");
  const set=new Set(),G2=built.engine.gauss(2);
  for(let i=0;i+1<cuts.length;i++){
    const lo=cuts[i],length=cuts[i+1]-lo;
    for(let k=0;k<subdivisions;k++)set.add(lo+length*k/subdivisions);
    for(const x of G2.x)set.add(lo+length*x);
  }
  set.add(end);const samples=Array.from(set).sort((a,b)=>a-b);
  const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
  const topMetricSites=[],topCurvatureSites=[];
  const retain=(list,entry,key)=>{
    if(list.length<24||entry[key]>list.at(-1)[key]){
      list.push(entry);list.sort((a,b)=>b[key]-a[key]);if(list.length>24)list.pop();
    }
  };
  let worstMetric=null,worstCurvature=null,minImmersion=Infinity,minMeanR=Infinity,count=0;
  let maxAbsoluteY=0,maxRadius=0,minHeldDistance=Infinity,minZ=Infinity,maxZ=-Infinity;
  let maximumXNormSite=null,minimumHeldSite=null;
  try{
    for(let si=0;si<samples.length;si++){
      const s=samples[si],sl=p.slice(s,z,false);
      for(let j=0;j<=angularIntervals;j++){
        const u=Math.PI*j/angularIntervals,index=j*nativeHalf/angularIntervals;
        const packet=Number.isInteger(index)?sl.node(index):sl.point(u),X=packet.jets.X;
        const Xs=packet.jets.Xs,Xu=packet.jets.Xu,a=packet.a;
        if(!(Number.isFinite(a)&&a>0)||![...X,...Xs,...Xu,packet.curvature,packet.immersion,packet.phase.R].every(Number.isFinite))
          throw Error("Nonfinite physical jet or observation");
        const e=dot(Xs,Xs)-1,f=dot(Xs,Xu)/a,g=dot(Xu,Xu)/(a*a)-1;
        const center=(e+g)/2,radius=Math.hypot((e-g)/2,f);
        const metric=Math.max(Math.abs(center+radius),Math.abs(center-radius));
        if(!Number.isFinite(metric))throw Error("Nonfinite normalized metric defect");
        const entry={s,u,e,f,g,metric,curvature:packet.curvature,X:Array.from(X)};
        if(!worstMetric||metric>worstMetric.metric)worstMetric=entry;
        if(!worstCurvature||entry.curvature>worstCurvature.curvature)worstCurvature=entry;
        minImmersion=Math.min(minImmersion,packet.immersion);minMeanR=Math.min(minMeanR,packet.phase.R);
        retain(topMetricSites,entry,"metric");retain(topCurvatureSites,entry,"curvature");
        const r=Math.hypot(...X),held=Math.min(
          Math.hypot(X[0],X[1]-centralA,X[2]),Math.hypot(X[0],X[1]+centralA,X[2]));
        if(r>maxRadius){maxRadius=r;maximumXNormSite={s,u,X:Array.from(X),radius:r};}
        if(held<minHeldDistance){minHeldDistance=held;minimumHeldSite={s,u,X:Array.from(X),distance:held};}
        maxAbsoluteY=Math.max(maxAbsoluteY,Math.abs(X[1]));minZ=Math.min(minZ,X[2]);maxZ=Math.max(maxZ,X[2]);
        count++;
      }
      p.clearSliceReuse?.();
      if(options.progress&&si%32===0)
        options.progress({s,count,worstMetric:worstMetric.metric,worstCurvature:worstCurvature.curvature});
      if(global.gc)global.gc();
    }
  }finally{p.clearSliceReuse?.();}
  if(z.some((v,i)=>!Object.is(v,input.z[i]))||built.z.some((v,i)=>!Object.is(v,input.z[i])))
    throw Error("An observation mutated its source coefficients");
  return {schema:SCHEMA,dimension:z.length,fieldFactory:"6a65-cauchy-global-position.cjs:build",
    factorySources:source,implementationSHA256:hash(__filename),
    consumerSHA256:hash(path.join(__dirname,"6a65-run-cauchy-same-job-recovered-v2.cjs")),
    providerDefinitionSHA256:digest(built.provider.definition),sourceStateSchema:input.schema,
    originalAngularRule:N,observationHalfPeriodIntervals:angularIntervals,radialSubdivisions:subdivisions,
    originalMetricRadialGaussNodesIncluded:true,radialPoints:samples.length,pointCount:count,
    physicalDomain:{radialInterval:[0,end],angularInterval:[0,Math.PI],baseModel:input.baseModel,
      wholePhysicalHalfCoreSampled:true,developedTailBeyondCutSampled:false,closedCapsSampled:false},
    actualDesign:built.design,worstMetric,worstCurvature,minImmersion,minMeanR,topMetricSites,topCurvatureSites,
    geometry:{centralSupport:centralA,heldCenters:[[0,centralA,0],[0,-centralA,0]],
      maxAbsoluteY,maxRadius,minHeldDistance,minZ,maxZ,maximumXNormSite,minimumHeldSite,
      sampledCoreGeometryOnly:true,continuousCertificate:false},
    fieldCoefficientsUnchanged:true,physicalMetricUnchanged:true,sourceAngularPrimitiveUnchanged:true,
    physicalClockUnchanged:true,additionalObservationsOnly:true,continuousCertificate:false,
    reachCertified:false,strongTargetComplete:false};
}
function forStrongController(candidate,input,options={}){
  const out=observe(candidate,input,options);
  return {...out,schema:WIRE_SCHEMA,mathematicalObservationSchema:SCHEMA,
    legacyWireCompatibilityOnly:true,legacyGapFactoryUsed:false};
}
module.exports={observe,forStrongController,SCHEMA,WIRE_SCHEMA};
if(require.main===module){
  const [candidateFile,inputFile,outputFile,radial="4",angular="256"]=process.argv.slice(2);
  if(!candidateFile||!inputFile||!outputFile||fs.existsSync(outputFile))
    throw Error("candidate input fresh-output [radial-subdivisions half-angle-intervals]");
  const start=Date.now(),candidateSHA256=hash(candidateFile),inputSHA256=hash(inputFile);
  const out=observe(JSON.parse(fs.readFileSync(candidateFile)),JSON.parse(fs.readFileSync(inputFile)),{
    subdivisions:Number(radial),angularIntervals:Number(angular),candidateSHA256,
    progress:r=>process.stdout.write(JSON.stringify({event:"progress",...r})+"\n")});
  out.inputs={candidateFile,candidateSHA256,inputFile,inputSHA256,scriptSHA256:hash(__filename)};
  out.elapsedSeconds=(Date.now()-start)/1000;
  out.execution={OSExitCode:null,externalExitReceiptRequired:true,actualFiniteObservationReturned:true};
  fs.mkdirSync(path.dirname(outputFile),{recursive:true});fs.writeFileSync(outputFile,JSON.stringify(out,null,2)+"\n");
  process.stdout.write(JSON.stringify({event:"complete",points:out.pointCount,metric:out.worstMetric.metric,
    curvature:out.worstCurvature.curvature,held:out.geometry.minHeldDistance,
    seconds:out.elapsedSeconds,outputSHA256:hash(outputFile)})+"\n");
}
