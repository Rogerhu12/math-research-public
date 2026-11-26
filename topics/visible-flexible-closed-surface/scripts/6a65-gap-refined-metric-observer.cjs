"use strict";
/* Explicit gap/clock factory: additional observations of the SAME finite field: retain the input angular
 * primitive, coefficients, physical metric and all interfaces. Sample maxima
 * are not continuous error/reach certificates or a new solved refinement. */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
function observe(candidate,input,options={}) {
  if(["6a65-Cauchy-global-position-initial-v1","6a65-Cauchy-global-position-checkpoint-v1"].includes(input?.schema))
    return require("./6a65-cauchy-same-field-observer-recovered-v2.cjs").forStrongController(candidate,input,options);
  const subdivisions=options.subdivisions??4,angularIntervals=options.angularIntervals??128;
  if(!Number.isInteger(subdivisions)||subdivisions<1||!Number.isInteger(angularIntervals)||angularIntervals<2)
    throw Error("Positive integer radial subdivisions and half-period angular intervals required");
  if(!input.gapLengthDesign||!input.outerLengthDesign)throw Error("Explicit saved gap/clock input required");
  const built=require("./6a65-geometry-gap-length-value.cjs").createGapLengthState(candidate,input);
  if(built.z.some((v,i)=>!Object.is(v,input.z[i])))throw Error("Same-clock observation changed a coefficient");
  const p=built.position,z=Array.from(built.z),cuts=p.radialCuts,nativeHalf=p.definition.parentMetric.fullEquivalentAngles/2;
  const set=new Set(),G2=built.engine.gauss(2);
  for(let i=0;i+1<cuts.length;i++) {
    const lo=cuts[i],length=cuts[i+1]-lo;
    for(let k=0;k<subdivisions;k++)set.add(lo+length*k/subdivisions);
    for(const x of G2.x)set.add(lo+length*x);
  }
  set.add(cuts.at(-1));const samples=Array.from(set).sort((a,b)=>a-b);
  const dot=(v,w)=>v[0]*w[0]+v[1]*w[1]+v[2]*w[2];
  let worstMetric=null,worstCurvature=null,minImmersion=Infinity,minMeanR=Infinity,count=0;
  const top=[];
  for(let si=0;si<samples.length;si++) {
    const s=samples[si],sl=p.slice(s,z,false);
    for(let j=0;j<=angularIntervals;j++) {
      const u=Math.PI*j/angularIntervals,nativeIndex=j*nativeHalf/angularIntervals;
      const packet=Number.isInteger(nativeIndex)?sl.node(nativeIndex):sl.point(u);
      const Xs=packet.jets.Xs,Xu=packet.jets.Xu,a=packet.a;
      const e=dot(Xs,Xs)-1,f=dot(Xs,Xu)/a,g=dot(Xu,Xu)/(a*a)-1;
      const center=(e+g)/2,radius=Math.hypot((e-g)/2,f);
      const defect=Math.max(Math.abs(center+radius),Math.abs(center-radius));
      if(!Number.isFinite(defect)||!Number.isFinite(packet.curvature))throw Error("Nonfinite observation");
      const entry={s,u,e,f,g,metric:defect,curvature:packet.curvature,X:packet.jets.X};
      if(!worstMetric||entry.metric>worstMetric.metric)worstMetric=entry;
      if(!worstCurvature||entry.curvature>worstCurvature.curvature)worstCurvature=entry;
      minImmersion=Math.min(minImmersion,packet.immersion);minMeanR=Math.min(minMeanR,packet.phase.R);
      if(top.length<24||entry.metric>top.at(-1).metric) {
        top.push(entry);top.sort((a,b)=>b.metric-a.metric);if(top.length>24)top.pop();
      }
      count++;
    }
    p.clearSliceReuse?.();
    if(options.progress&&si%32===0)options.progress({s,count,worstMetric:worstMetric.metric,worstCurvature:worstCurvature.curvature});
    if(global.gc)global.gc();
  }
  return {schema:"6a65-gap-clock-same-field-refined-metric-observation-v1",dimension:z.length,
    originalAngularRule:p.definition.parentMetric.fullEquivalentAngles,observationHalfPeriodIntervals:angularIntervals,
    radialSubdivisions:subdivisions,originalMetricRadialGaussNodesIncluded:true,radialPoints:samples.length,pointCount:count,
    worstMetric,worstCurvature,minImmersion,minMeanR,topMetricSites:top,
    fieldCoefficientsUnchanged:true,physicalMetricUnchanged:true,sourceAngularPrimitiveUnchanged:true,
    additionalObservationsOnly:true,continuousCertificate:false,reachCertified:false,strongTargetComplete:false};
}
module.exports={observe};
if(require.main===module) {
  const [candidateFile,inputFile,outputFile,radial="4",angular="128"]=process.argv.slice(2);
  if(!candidateFile||!inputFile||!outputFile||fs.existsSync(outputFile))throw Error("candidate input fresh-output [radial-subdivisions half-angle-intervals]");
  const start=Date.now(),hash=f=>crypto.createHash("sha256").update(fs.readFileSync(f)).digest("hex");
  const out=observe(JSON.parse(fs.readFileSync(candidateFile)),JSON.parse(fs.readFileSync(inputFile)),{
    subdivisions:Number(radial),angularIntervals:Number(angular),
    progress:r=>process.stdout.write(JSON.stringify({event:"progress",...r})+"\n")});
  out.inputs={candidateFile,candidateSHA256:hash(candidateFile),inputFile,inputSHA256:hash(inputFile),scriptSHA256:hash(__filename)};
  out.elapsedSeconds=(Date.now()-start)/1000;
  fs.mkdirSync(path.dirname(outputFile),{recursive:true});fs.writeFileSync(outputFile,JSON.stringify(out,null,2)+"\n");
  process.stdout.write(JSON.stringify({event:"complete",points:out.pointCount,metric:out.worstMetric.metric,curvature:out.worstCurvature.curvature,seconds:out.elapsedSeconds})+"\n");
}
