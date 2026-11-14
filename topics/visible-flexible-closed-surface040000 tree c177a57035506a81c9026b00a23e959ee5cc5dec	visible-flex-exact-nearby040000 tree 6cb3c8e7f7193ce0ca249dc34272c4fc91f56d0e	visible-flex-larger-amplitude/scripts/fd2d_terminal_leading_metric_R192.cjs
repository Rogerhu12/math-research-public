"use strict";
/* R192. Optional coordinates for the exact finite analytic last-span
 * necessary conditions. Nothing here changes an active provider or LM.
 * The asymptotic statement assumes the exact B32 endpoint semantics.
 */
function assert(b,message){if(!b)throw Error(message);}
function describe(definition){
  const kinds=["fd2d-R187-C2-direct-position-two-angle-finite-provider-v1","fd2d-R190-C2-direct-position-designed-radius-finite-provider-v1"];
  assert(definition&&kinds.includes(definition.schema),"Require the explicit R187 or R190 definition");
  const J=definition.radialBasisCount,K=definition.angularModes;
  assert(Number.isInteger(J)&&J>0&&Number.isInteger(K)&&K>0,"Invalid dimensions");
  const isRadius=definition.schema===kinds[1],expected=2*J*K+J+1+(isRadius?J:0);
  assert(definition.dimension===expected,"Wrong actual dimension");
  const layout=definition.stateLayout;
  assert(layout&&layout.theta[0]===0&&layout.theta[1]===J*K,"Wrong theta layout");
  if(isRadius)assert(layout.radius[0]===2*J*K+J+1&&layout.radius[1]===expected,"Wrong radius layout");
  const thetaIndices=Array.from({length:K},(_,k)=>(J-1)*K+k);
  const radiusIndex=isRadius?layout.radius[1]-1:null;
  return {J,K,n:expected,thetaIndices,radiusIndex};
}
function copy(z,n){
  assert(z&&z.length===n,"Wrong complete vector length");
  const out=new Float64Array(n);
  for(let i=0;i<n;++i){assert(typeof z[i]==="number"&&Number.isFinite(z[i]),"Nonfinite parameter");out[i]=z[i];}
  return out;
}
function terminalLeadingMetric(z,definition,base){
  const d=describe(definition);copy(z,d.n);
  assert(base&&Array.isArray(base.segments)&&base.segments.length>0,"Require the actual base profile");
  const last=base.segments.at(-1),c=base.centralLength,S=base.end;
  assert(last.kind==="phase_bridge"&&last.exact_endpoint_phase==="-pi/2"&&last.ps1===0,"Require the declared quadratic flat brake");
  assert(Number.isFinite(c)&&Number.isFinite(S)&&S>c&&last.L>0,"Invalid interval");
  const ac=base.at(S).a,h=(S-c)/(d.J+3),h3=h*h*h;
  const rho=d.radiusIndex===null?0:z[d.radiusIndex];
  const meanE=rho/h3,cosineE=new Float64Array(d.K),sineF=new Float64Array(d.K);
  let energy=meanE*meanE;
  for(let j=0;j<d.K;++j){
    const k=j+1,t=z[d.thetaIndices[j]],den=4*k*k-1;
    cosineE[j]=ac*(2*k)*t/(h3*den);
    sineF[j]=ac*t/(2*h3*den);
    energy+=.5*cosineE[j]*cosineE[j]+sineF[j]*sineF[j];
  }
  return {definition:{schema:"fd2d-R192-last-span-leading-metric-v1",oldFieldSchema:definition.schema,
      radialBasisCount:d.J,angularModes:d.K,centralLength:c,end:S,cutRadius:ac,step:h,
      validAsymptoticNeighborhood:Math.min(h,last.L),
      exactProfileAssumption:"a_base_s=-1+O(tau^4), z_base_s=O(tau^2) at the same exact S",
      expansion:"rE=tau^2*(meanE+sum cosineE[k-1]*cos(2ku))+O(tau^3); rF=tau^2*sum sineF[k-1]*sin(2ku)+O(tau^3)",
      remainderUniformInAngleForThisFixedFiniteField:true,remainderUniformInResolutionClaimed:false,
      necessaryConditionOnlyForExactFiniteAnalyticIsometry:true,arbitraryC2ObstructionClaimed:false},
    thetaIndices:d.thetaIndices,radiusIndex:d.radiusIndex,meanE,cosineE,sineF,
    weightedAngularMeanSquaredLeadingCoefficient:energy,
    evaluate:u=>{let E=meanE,F=0;for(let k=1;k<=d.K;++k){E+=cosineE[k-1]*Math.cos(2*k*u);F+=sineF[k-1]*Math.sin(2*k*u);}return {rEOverTauSquared:E,rFOverTauSquared:F};}};
}
function createTerminalRestriction(definition){
  const d=describe(definition),removed=[...d.thetaIndices,...(d.radiusIndex===null?[]:[d.radiusIndex])];
  const removedSet=new Set(removed),keep=Array.from({length:d.n},(_,i)=>i).filter(i=>!removedSet.has(i));
  const description={schema:"fd2d-R192-optional-zero-terminal-leading-coordinates-v1",
    originalFieldSchema:definition.schema,fullDimension:d.n,freeDimension:keep.length,
    removedThetaIndices:d.thetaIndices,removedRadiusIndex:d.radiusIndex,keptIndices:keep,
    activeSolverModified:false,fullOriginalProviderMustEvaluateExpandedVector:true,
    exactFiniteAnalyticNecessarySubspace:true,newBaselineRequiredIfZeroCopyChangesField:true,
    dyadicProlongationPreservesSubspace:true};
  function expand(free){const q=copy(free,keep.length),full=new Float64Array(d.n);for(let i=0;i<keep.length;++i)full[keep[i]]=q[i];return full;}
  function reduce(full){
    const z=copy(full,d.n);for(const j of removed)assert(z[j]===0,"Nonzero removed coefficient: use explicit zeroCopy and evaluate a new baseline");
    return Float64Array.from(keep,j=>z[j]);
  }
  function zeroCopy(full){
    const vector=copy(full,d.n),changes=[];
    for(const j of removed){if(vector[j]!==0)changes.push({index:j,oldValue:vector[j],newValue:0});vector[j]=0;}
    return {vector,definition:description,metadata:{schema:"fd2d-R192-explicit-new-warm-zeroing-v1",changes,
      originalVectorModified:false,actualSameField:changes.length===0,
      physicalMetricChanged:changes.some(x=>x.index===d.radiusIndex),
      originalBoundaryTwoJetsPreserved:true,
      newActualBaselineRequired:changes.length>0,actualNewBaselineEvaluated:false,
      actualNonlinearAcceptedState:false}};
  }
  function selectNormal(normal,currentFullVector){
    const free=reduce(currentFullVector);
    assert(normal&&normal.g&&normal.g.length===d.n&&Number.isFinite(normal.squaredNorm)&&normal.squaredNorm>=0,"Invalid full normal");
    if(normal.z)assert(normal.z.length===d.n&&normal.z.every((v,i)=>v===currentFullVector[i]),"Normal is bound to another parameter vector");
    const rows=normal.H.length===d.n&&normal.H[0]&&typeof normal.H[0]!=="number";
    assert(rows||normal.H.length===d.n*d.n,"Wrong full H");
    const n=keep.length,H=new Float64Array(n*n),g=new Float64Array(n),diagonal=new Float64Array(n);
    for(let i=0;i<n;++i){
      g[i]=normal.g[keep[i]];
      for(let j=0;j<n;++j)H[i*n+j]=rows?normal.H[keep[i]][keep[j]]:normal.H[keep[i]*d.n+keep[j]];
      diagonal[i]=H[i*n+i];
    }
    return {...normal,H,g,diagonal,z:free,restriction:description};
  }
  return {definition:description,expand,reduce,zeroCopy,selectNormal};
}
module.exports={terminalLeadingMetric,createTerminalRestriction};
