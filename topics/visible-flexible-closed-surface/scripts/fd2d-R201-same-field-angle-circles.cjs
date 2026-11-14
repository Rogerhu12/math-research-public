"use strict";
/* Same saved finite field, different angular observation grids only.
   sourceFullAngles stays fixed when the provider is instantiated.
   Cartesian derivatives are from complete R201/R205 formulas, not a DFT. */
function nestedAngleCircles(position,z,radialPoints,{sourceFullAngles=64,levels=[64,128,256,512]}={}){
 if(z.length!==position.dimension||levels.some(N=>N<sourceFullAngles||N%sourceFullAngles||N%2))throw Error("Invalid explicit nested grid");
 const finest=Math.max(...levels),half=finest/2,sourceHalf=sourceFullAngles/2,rows=[];
 if(levels.some(N=>finest%N))throw Error("All observation grids must be nested");
 const dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0);
 for(const input of radialPoints){
  const s=input.s,sl=position.slice(s,z,false),samples=[];
  for(let j=0;j<=half;j++){
   const u=Math.PI*j/half,oldIndex=j*sourceHalf/half,p=Number.isInteger(oldIndex)?sl.node(oldIndex):sl.point(u);
   const E=dot(p.jets.Xs,p.jets.Xs),F=dot(p.jets.Xs,p.jets.Xu)/p.a,G=dot(p.jets.Xu,p.jets.Xu)/(p.a*p.a);
   const v={s,u,rE:E-1,rF:F,rG:G-1,relativeMetric:p.relativeMetric,curvature:p.curvature,
    principalCurvatures:Array.from(p.principalCurvatures),immersion:p.immersion,X:Array.from(p.jets.X)};
   if(![v.rE,v.rF,v.rG,v.relativeMetric,v.curvature,v.immersion].every(Number.isFinite))throw Error("Nonfinite actual twojet sample");
   samples.push(v);
  }
  const summaries=[];
  for(const N of levels){
   const stride=finest/N,n=N/2;let meanE=0,meanF=0,meanMetricSquared=0,maxAbsG=0;
   let maxMetric=null,maxCurvature=null,maxAbsE=null,maxAbsF=null,minImmersion=null;
   for(let j=0;j<=n;j++){
    const p=samples[j*stride],w=((j===0||j===n)?0.5:1)/n;
    meanE+=w*p.rE;meanF+=w*p.rF;meanMetricSquared+=w*(p.rE*p.rE+2*p.rF*p.rF);maxAbsG=Math.max(maxAbsG,Math.abs(p.rG));
    if(!maxMetric||p.relativeMetric>maxMetric.relativeMetric)maxMetric=p;
    if(!maxCurvature||p.curvature>maxCurvature.curvature)maxCurvature=p;
    if(!maxAbsE||Math.abs(p.rE)>Math.abs(maxAbsE.rE))maxAbsE=p;
    if(!maxAbsF||Math.abs(p.rF)>Math.abs(maxAbsF.rF))maxAbsF=p;
    if(!minImmersion||p.immersion<minImmersion.immersion)minImmersion=p;
   }
   summaries.push({fullEquivalentAngles:N,halfSamples:n+1,meanResidualE:meanE,meanResidualF:meanF,
    meanMetricSquared,maxAbsResidualG:maxAbsG,maxMetric,maxCurvature,maxAbsE,maxAbsF,minImmersion});
  }
  rows.push({s,selectionReason:input.reason,levels:summaries,finestSampleCount:samples.length});
 }
 return {schema:"fd2d-R201-R205-same-field-nested-angle-circles-v1",fieldDimension:position.dimension,
  sourceFullAngles,levels,radialPoints:radialPoints.map(x=>({...x})),rows,
  scope:"Only observation angles change. The original provider state, radial basis, primitive quadrature, reference, radius, target and tail parameters are unchanged.",
  angularDerivativesByDFT:false,newTargetMetric:false,noJacobian:true,noNormal:true,noLM:true,
  continuousCertificate:false,globalMaximaCertificate:false,strongTargetComplete:false};
}
if(typeof module!=="undefined"&&module.exports)module.exports={nestedAngleCircles};
