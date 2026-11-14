/* R205 bounded implementation diagnostic and explicit new baseline.
 * This is finite numerical evidence; it never declares a continuous certificate.
 */
"use strict";
function runR205BentAnnulusCheck(deps,settings={}){
  const {engine,splines,algebra,bundle,parent,referenceFactory,metricFactory,curvatureFactory}=deps;
  const start=Date.now(),amplitude=settings.amplitude===undefined?.25:settings.amplitude,
    angles=settings.angles||128,options={...parent.options,angles,bentAnnulus:{amplitude}},
    curvatureOptions={guide:9.5,weight:.01,nodeShare:.5,...settings.curvatureOptions};
  const metric=metricFactory(engine,bundle,options,splines,referenceFactory),
    provider=curvatureFactory(engine,metric,curvatureOptions,algebra),
    z=Float64Array.from(parent.z),cut=metric.base.end,
    cuffHeight=metric.base.height+z[metric.definition.stateLayout.cutHeight],
    epsilon=2e-6,direction=Float64Array.from(z,(_,i)=>.02*(Math.sin(.23*(i+1))+.3*Math.cos(.71*(i+1)))),
    zp=Float64Array.from(z,(v,i)=>v+epsilon*direction[i]),zm=Float64Array.from(z,(v,i)=>v-epsilon*direction[i]);
  if(z.length!==provider.dimension)throw Error("Complete parent state/layout mismatch");
  const anglesToCheck=[0,.2,.47,Math.PI/3,1.4,Math.PI/2,2,3.8,5.2],cutRows=[];
  for(const u of anglesToCheck){
    const a=provider.point(cut,u,z),b=metric.bentReference.tailPoint(.8,u,cuffHeight);let error=0;
    for(const name of Object.keys(a.jets))for(let j=0;j<3;j++)error=Math.max(error,Math.abs(a.jets[name][j]-b.jets[name][j]));
    cutRows.push({u,error});
  }
  const s=settings.directionPoint?.[0]===undefined?.27:settings.directionPoint[0],
    u=settings.directionPoint?.[1]===undefined?.7:settings.directionPoint[1],
    p=provider.point(s,u,z,{jacobian:true}),pp=provider.point(s,u,zp),pm=provider.point(s,u,zm);
  let jetAbsolute=0,jetScaled=0,hingeAbsolute=0,hingeScaled=0;
  const jetErrors={};
  for(const key of Object.keys(p.jets)){
    let error=0;for(let j=0;j<3;j++){
      let exact=0;for(let h=0;h<p.indices.length;h++)exact+=direction[p.indices[h]]*p.parameterJets[h][key][j];
      const fd=(pp.jets[key][j]-pm.jets[key][j])/(2*epsilon),e=Math.abs(exact-fd);
      error=Math.max(error,e);jetAbsolute=Math.max(jetAbsolute,e);jetScaled=Math.max(jetScaled,e/Math.max(1,Math.abs(exact),Math.abs(fd)));
    }jetErrors[key]=error;
  }
  for(let j=0;j<3;j++){
    let exact=0;for(let h=0;h<p.indices.length;h++)exact+=direction[p.indices[h]]*p.jacobian[j][h];
    const fd=(pp.residual[j]-pm.residual[j])/(2*epsilon),e=Math.abs(exact-fd);
    hingeAbsolute=Math.max(hingeAbsolute,e);hingeScaled=Math.max(hingeScaled,e/Math.max(1,Math.abs(exact),Math.abs(fd)));
  }
  const rowIndex=Math.min(13,angles/4),mr=metric.metricRows(s,z,{jacobian:true})[rowIndex],
    mrp=metric.metricRows(s,zp)[rowIndex],mrm=metric.metricRows(s,zm)[rowIndex];
  let metricJVPError=0;
  for(const [residual,column]of [["rE","e"],["rF","f"]]){
    let exact=0;for(let j=0;j<mr.indices.length;j++)exact+=direction[mr.indices[j]]*mr[column][j];
    metricJVPError=Math.max(metricJVPError,Math.abs((mrp[residual]-mrm[residual])/(2*epsilon)-exact));
  }
  let externalAmplitude=null;
  if(amplitude>epsilon&&amplitude<1.2-epsilon){
    const plus=referenceFactory(engine,metric.base,{amplitude:amplitude+epsilon,angles}),
      minus=referenceFactory(engine,metric.base,{amplitude:amplitude-epsilon,angles}),
      a=metric.bentReference.angular(s,u),ap=plus.angular(s,u),am=minus.angular(s,u);
    let angularError=0,heightError=0,tailError=0;
    for(let j=0;j<8;j++)angularError=Math.max(angularError,Math.abs((ap[j]-am[j])/(2*epsilon)-a[j+8])/Math.max(1,Math.abs(a[j+8])));
    const h=metric.bentReference.heightCorrection(s),hp=plus.heightCorrection(s),hm=minus.heightCorrection(s);
    for(let j=0;j<3;j++){const key=["value","first","second"][j];heightError=Math.max(heightError,Math.abs((hp[key]-hm[key])/(2*epsilon)-h.amplitude[j]));}
    const ta=metric.bentReference.tailPoint(.8,u,cuffHeight),tp=plus.tailPoint(.8,u,cuffHeight),tm=minus.tailPoint(.8,u,cuffHeight);
    for(const key of Object.keys(ta.jets))for(let j=0;j<3;j++)tailError=Math.max(tailError,Math.abs((tp.jets[key][j]-tm.jets[key][j])/(2*epsilon)-ta.amplitudeJets[key][j]));
    externalAmplitude={angularScaledError:angularError,heightAbsoluteError:heightError,tailTwoJetAbsoluteError:tailError,finiteStateContainsAmplitudeColumn:false};
  }
  const value=provider.value(z),execution={runtime:"JavaScript",completed:true,elapsedMilliseconds:Date.now()-start},
    baseline={schema:"fd2d-R205-fixed-bent-annulus-new-baseline-v1",options,curvatureOptions,z:Array.from(z),lambda:.01,
      localAcceptedSteps:0,centralSeed:parent.centralSeed,providerDefinition:provider.definition,
      actualFiniteCuffPlaneHeight:cuffHeight,actualFiniteOuterCutMeanHeight:metric.bentReference.cutSectionMeanJets(cuffHeight).value,
      lastEvaluation:value,execution,newReferenceBaseline:true,parentParameterVectorPreserved:true,parentFieldPreserved:false,
      physicalMetricPreservedAtThisInjection:true,physicalMetricChangesUnderFutureRhoSteps:true,
      R203GeometryRowsIncluded:false,continuousCertificate:false,strongTargetComplete:false};
  const report={schema:"fd2d-R205-complete-cut-and-old-parameter-JVP-check-v1",amplitude,angles,dimension:provider.dimension,
    execution,cutRows,maximumCutTwoJetError:Math.max(...cutRows.map(x=>x.error)),
    directionCheck:{s,u,epsilon,direction:"d_i=.02*(sin(.23*(i+1))+.3*cos(.71*(i+1)))",curvature:p.curvature,
      activeCurvaturePenalty:p.penaltySquared>0,jetAbsolute,jetScaled,hingeAbsolute,hingeScaled,jetErrors,metricJVPError},
    externalAmplitude,innerCuffHeight:cuffHeight,outerCutMeanHeight:baseline.actualFiniteOuterCutMeanHeight,
    actualValue:value,newAcceptedSteps:0,continuousCertificate:false,strongTargetComplete:false};
  return {baseline,report};
}
if(typeof module!=="undefined"&&module.exports)module.exports={runR205BentAnnulusCheck};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module){
  const fs=require("fs"),path=require("path"),crypto=require("crypto"),[candidatePath,parentPath,outputPath,Aarg,Narg]=process.argv.slice(2);
  if(!candidatePath||!parentPath||!outputPath)throw Error("Usage: node CHECK candidate.json parent.json output.json [A=.25] [N=128]");
  function factory(file,name){const src=fs.readFileSync(path.join(__dirname,file),"utf8");return new Function(src+";return "+name+";")();}
  const engine=factory("fd2d-direct-position-tangent-lift-baseline-R187.cjs","createR187")(),
    splines=factory("fd2d-cubic-spline-refinement-R196.cjs","createR196CubicSplines")(),
    algebra=factory("fd2d-position-curvature-chain-R191.cjs","createR191Algebra")(),
    bundle=JSON.parse(fs.readFileSync(candidatePath,"utf8")),parent=JSON.parse(fs.readFileSync(parentPath,"utf8")),
    result=runR205BentAnnulusCheck({engine,splines,algebra,bundle,parent,
      referenceFactory:factory("fd2d-bent-annulus-reference-R205.cjs","createR205BentAnnulusReference"),
      metricFactory:factory("fd2d-direct-position-bent-annulus-metric-R205.cjs","createR205MetricProvider"),
      curvatureFactory:factory("fd2d-direct-position-bent-annulus-curvature-R205.cjs","createR205CurvatureProvider")},
      {amplitude:Aarg===undefined?.25:Number(Aarg),angles:Narg===undefined?128:Number(Narg)});
  result.binding={candidateSHA256:crypto.createHash("sha256").update(fs.readFileSync(candidatePath)).digest("hex"),
    parentSHA256:crypto.createHash("sha256").update(fs.readFileSync(parentPath)).digest("hex")};
  fs.writeFileSync(outputPath,JSON.stringify(result,null,2)+"\n");
}
