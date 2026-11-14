"use strict";
/* Finite position screen for the R210 cap hypothesis, not a continuous proof.
   Uses one immutable already-saved R201/R205 provider and state. It does not
   change the actual finite quadrature, radius, target, tail amplitude or z.
   Half-period sampling covers the second half by the provider's exact
   (x,y,z)->(-x,-y,z) convention; the lower core is reflected separately. */
function screenR210Protrusion(position,z,configuration={}){
 const {cutHeightIndex,sourceFullAngles,halfIntervals=64,Delta=1/50,farRadius=257/500,onProgress=null}=configuration;
 if(z.length!==position.dimension||!Number.isInteger(cutHeightIndex)||cutHeightIndex<0||cutHeightIndex>=z.length)
  throw Error("Explicit actual state layout required");
 if(!Number.isInteger(sourceFullAngles)||sourceFullAngles<4||sourceFullAngles%2||
    !Number.isInteger(halfIntervals)||halfIntervals<1)throw Error("Explicit angular counts required");
 const Z=position.base.height+z[cutHeightIndex],S=position.base.end,cuts=Array.from(position.radialCuts);
 const byS=new Map();
 function insert(s,kind){if(!byS.has(s))byS.set(s,[]);byS.get(s).push(kind);}
 for(const s of cuts)insert(s,"physical_knot");
 for(let i=1;i<cuts.length;i++){
  const lo=cuts[i-1],h=cuts[i]-lo;
  insert(lo+h*(1-Math.sqrt(1/3))/2,"cell_Gauss2_left");
  insert(lo+h/2,"cell_midpoint");
  insert(lo+h*(1+Math.sqrt(1/3))/2,"cell_Gauss2_right");
 }
 const radial=[...byS].sort((a,b)=>a[0]-b[0]),sourceHalf=sourceFullAngles/2;
 let maxExcess=-Infinity,minRadiusAmongAbove=Infinity,maxSlabViolation=0,maxNearAxisProtrusion=0,
  maxAbsoluteY=0,maxRadius=0,pointCount=0,aboveCount=0,maxCurvature=0,maxRelativeMetric=0,minImmersion=Infinity;
 let heightWitness=null,radialWitness=null,slabWitness=null,nearAxisWitness=null;
 const rowValues=[];
 for(let i=0;i<radial.length;i++){
  const [s,kinds]=radial[i],sl=position.slice(s,z,false);
  let rowMaxExcess=-Infinity,rowMinR=Infinity,rowAbove=0,rowSlab=0,rowNear=0;
  for(let j=0;j<=halfIntervals;j++){
   const u=Math.PI*j/halfIntervals,nodeIndex=j*sourceHalf/halfIntervals;
   const p=Number.isInteger(nodeIndex)?sl.node(nodeIndex):sl.point(u),X=p.jets.X;
   if(X.length!==3||!X.every(Number.isFinite))throw Error("Nonfinite actual position");
   const r=Math.hypot(X[0],X[1]),az=Math.abs(X[2]),excess=az-Z;
   const witness={s,u,X:Array.from(X),radius:r,absoluteHeight:az,heightExcess:excess,radialKinds:kinds};
   pointCount++;rowMaxExcess=Math.max(rowMaxExcess,excess);
   maxAbsoluteY=Math.max(maxAbsoluteY,Math.abs(X[1]));maxRadius=Math.max(maxRadius,Math.hypot(...X));
   maxCurvature=Math.max(maxCurvature,p.curvature);maxRelativeMetric=Math.max(maxRelativeMetric,p.relativeMetric);
   minImmersion=Math.min(minImmersion,p.immersion);
   if(excess>maxExcess){maxExcess=excess;heightWitness=witness;}
   if(excess>0){aboveCount++;rowAbove++;rowMinR=Math.min(rowMinR,r);
    if(r<minRadiusAmongAbove){minRadiusAmongAbove=r;radialWitness=witness;}}
   const sv=Math.max(0,excess-Delta),nv=r<farRadius?Math.max(0,excess):0;
   rowSlab=Math.max(rowSlab,sv);rowNear=Math.max(rowNear,nv);
   if(sv>maxSlabViolation){maxSlabViolation=sv;slabWitness=witness;}
   if(nv>maxNearAxisProtrusion){maxNearAxisProtrusion=nv;nearAxisWitness=witness;}
  }
  rowValues.push([s,kinds.join("|"),rowMaxExcess,rowMinR===Infinity?null:rowMinR,rowAbove,rowSlab,rowNear]);
  if(onProgress&&(i%48===0||i+1===radial.length))onProgress({radialCompleted:i+1,radialTotal:radial.length,maxExcess,minRadiusAmongAbove:minRadiusAmongAbove===Infinity?null:minRadiusAmongAbove,maxSlabViolation,maxNearAxisProtrusion});
 }
 return{schema:"fd2d-R210-complete-prefix-finite-protrusion-screen-v1",Zc:Z,Delta,farRadius,sourceFullAngles,sampleFullEquivalentAngles:2*halfIntervals,
  fieldDimension:position.dimension,tailAmplitude:z[position.amplitudeIndex],radialEnd:S,
  radialPoints:radial.length,pointCount,aboveCount,maxHeightExcess:maxExcess,
  minRadiusAmongAbove:minRadiusAmongAbove===Infinity?null:minRadiusAmongAbove,
  maxSlabViolation,maxNearAxisProtrusion,allSampledR210HeightAndRadiusConditionsSatisfied:maxSlabViolation===0&&maxNearAxisProtrusion===0,
  maxAbsoluteY,maxRadius,maxCurvature,maxRelativeMetric,minImmersion,
  witnesses:{height:heightWitness,smallestAboveRadius:radialWitness,slab:slabWitness,nearAxis:nearAxisWitness},
  radialSummary:{columns:["s","kinds","max_height_excess","min_radius_if_above_Z","above_sample_count","slab_violation","near_axis_height_violation"],values:rowValues},
  actualProviderDefinition:position.definition,
  scope:"Finite physical-knot, midpoint and Gauss2 radial positions, 128 full-equivalent angular samples by default. The source field/quadrature is unchanged.",
  noJacobian:true,noNormal:true,noLM:true,noBVP:true,continuousCertificate:false,wholeCoreReachCertified:false,strongTargetComplete:false};
}
if(typeof module!=="undefined"&&module.exports)module.exports={screenR210Protrusion};
