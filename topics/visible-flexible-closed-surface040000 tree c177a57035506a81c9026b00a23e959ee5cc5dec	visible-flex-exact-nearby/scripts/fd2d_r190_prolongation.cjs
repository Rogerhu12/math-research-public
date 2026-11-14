"use strict";
/* R189 nesting extended to the actual R190 appended radius coefficients.
 * Fixed seed/base/c/S, same complete rho(s), same complete position in real
 * arithmetic. This is initialization in a finer space, not a new metric
 * design step. Binary64 coefficient/function differences are explicit.
 */
function assert(ok,message){if(!ok)throw Error(message);}
function integer(x,name,min){assert(Number.isInteger(x)&&x>=min,name+" is invalid");return x;}
function layout190(J,K){
  const oldDimension=2*J*K+J+1,n=oldDimension+J;
  return {theta:[0,J*K],phi:[J*K,2*J*K],height:[2*J*K,2*J*K+J],
    cutHeight:oldDimension-1,radius:[oldDimension,n]};
}
function binaryDyadic(x){
  assert(Number.isFinite(x),"Nonfinite dyadic input");
  const d=new DataView(new ArrayBuffer(8));d.setFloat64(0,x,false);
  const hi=d.getUint32(0,false),lo=d.getUint32(4,false);
  const exponent=(hi>>>20)&2047,frac=(BigInt(hi&0xfffff)<<32n)|BigInt(lo);
  if(exponent===0&&frac===0n)return {n:0n,e:0};
  let n=exponent===0?frac:(1n<<52n)+frac;
  if(hi>>>31)n=-n;
  return {n,e:exponent===0?-1074:exponent-1023-52};
}
function roundDyadic(n,e){
  if(n===0n)return 0;
  const negative=n<0n;if(negative)n=-n;
  const bits=n.toString(2).length;
  const unit=Math.max(e+bits-53,-1074),shift=unit-e;
  let q;
  if(shift>0){
    const b=BigInt(shift);q=n>>b;
    const remainder=n-(q<<b),half=1n<<(b-1n);
    if(remainder>half||(remainder===half&&(q&1n)!==0n))q+=1n;
  }else q=n<<BigInt(-shift);
  const x=Number(q)*2**unit;
  assert(Number.isFinite(x),"Rounded dyadic overflow");
  return negative?-x:x;
}
function exactMaskEntry(values,numerators){
  const terms=[];let exponent=Infinity;
  for(let i=0;i<values.length;++i){
    const t=binaryDyadic(values[i]);if(t.n===0n||numerators[i]===0)continue;
    const item={n:t.n*BigInt(numerators[i]),e:t.e-3};
    terms.push(item);exponent=Math.min(exponent,item.e);
  }
  if(!terms.length)return 0;
  let n=0n;for(const t of terms)n+=t.n<<BigInt(t.e-exponent);
  return roundDyadic(n,exponent);
}
function refineRadiusCoefficients(values){
  const J=integer(values.length,"radius count",1),nextJ=2*J+3,mask=[1,4,6,4,1];
  const out=new Float64Array(nextJ);
  for(let i=0;i<nextJ;++i){
    const a=[],m=[];
    for(let r=0;r<5;++r){
      if((i-r)%2!==0)continue;
      const j=(i-r)/2;
      if(j>=0&&j<J){assert(Number.isFinite(values[j]),"Nonfinite radius coefficient");a.push(values[j]);m.push(mask[r]);}
    }
    out[i]=exactMaskEntry(a,m);
  }
  return out;
}
function once(z,J,K){
  const nextJ=2*J+3,old=layout190(J,K),next=layout190(nextJ,K);
  const out=new Float64Array(next.radius[1]),mask=[1/8,4/8,6/8,4/8,1/8];
  for(const key of ["theta","phi"])for(let j=0;j<J;++j)for(let k=0;k<K;++k)
    for(let r=0;r<5;++r)out[next[key][0]+(2*j+r)*K+k]+=mask[r]*z[old[key][0]+j*K+k];
  for(let j=0;j<J;++j)for(let r=0;r<5;++r)out[next.height[0]+2*j+r]+=mask[r]*z[old.height[0]+j];
  out[next.cutHeight]=z[old.cutHeight];
  out.set(refineRadiusCoefficients(z.subarray(old.radius[0],old.radius[1])),next.radius[0]);
  return {vector:out,J:nextJ};
}
function pad(z,J,K,nextK){
  const old=layout190(J,K),next=layout190(J,nextK),out=new Float64Array(next.radius[1]);
  for(const key of ["theta","phi"])for(let j=0;j<J;++j)for(let k=0;k<K;++k)
    out[next[key][0]+j*nextK+k]=z[old[key][0]+j*K+k];
  for(let j=0;j<J;++j){out[next.height[0]+j]=z[old.height[0]+j];out[next.radius[0]+j]=z[old.radius[0]+j];}
  out[next.cutHeight]=z[old.cutHeight];return out;
}
function maxRadius(z,L){let m=0;for(let j=L.radius[0];j<L.radius[1];++j)m=Math.max(m,Math.abs(z[j]));return m;}
function prolongR190State(z,definition,options={}){
  assert(definition&&definition.schema==="fd2d-R190-C2-direct-position-designed-radius-finite-provider-v1","Require the actual R190 definition");
  const J=integer(definition.radialBasisCount,"old radial count",1),K=integer(definition.angularModes,"old angular count",1);
  const old=layout190(J,K),oldN=integer(definition.fullEquivalentAngles,"old angular count",16);
  assert(oldN%4===0,"Old angular quadrature is not divisible by four");
  assert(definition.dimension===old.radius[1]&&definition.oldDimension===old.radius[0],"R190 dimension mismatch");
  assert(JSON.stringify(definition.stateLayout)===JSON.stringify(old),"R190 layout mismatch");
  assert(z&&z.length===definition.dimension,"Wrong complete parameter length");
  let vector=new Float64Array(z.length);
  for(let j=0;j<z.length;++j){assert(typeof z[j]==="number"&&Number.isFinite(z[j]),"Nonfinite parameter");vector[j]=z[j];}
  const bound=definition.radiusCoefficientBound;
  assert(Number.isFinite(bound)&&bound>0&&bound<.8,"Invalid R190 radius box");
  const oldMaximum=maxRadius(vector,old);assert(oldMaximum<=bound,"Original state is outside its declared radius box");
  const levels=integer(options.radialRefinements===undefined?1:options.radialRefinements,"radial refinements",0);
  const targetK=integer(options.modes===undefined?K:options.modes,"target angular modes",K);
  const targetN=integer(options.angles===undefined?oldN:options.angles,"target angular quadrature",16);
  assert(targetN%4===0,"Target angular quadrature must be divisible by four");
  let newJ=J;
  for(let l=0;l<levels;++l){const r=once(vector,newJ,K);vector=r.vector;newJ=r.J;}
  if(targetK!==K)vector=pad(vector,newJ,K,targetK);
  const targetLayout=layout190(newJ,targetK),newMaximum=maxRadius(vector,targetLayout);
  assert(newMaximum<=oldMaximum,"The correctly rounded convex radius map violated its exact box bound");
  const targetDefinition={...definition,radialBasisCount:newJ,angularModes:targetK,fullEquivalentAngles:targetN,
    dimension:vector.length,oldDimension:targetLayout.radius[0],stateLayout:targetLayout};
  return {vector,definition:targetDefinition,
    providerOptions:{radialBasisCount:newJ,modes:targetK,angles:targetN,radiusCoefficientBound:bound},
    provenance:{schema:"fd2d-R189-R190-radius-prolongation-v1",oldRadialBasisCount:J,newRadialBasisCount:newJ,
      oldAngularModes:K,newAngularModes:targetK,oldDimension:definition.dimension,newDimension:vector.length,
      radialRefinementLevels:levels,maskNumerators:[1,4,6,4,1],maskDenominator:8,
      oldMaximumRadiusCoefficient:oldMaximum,newMaximumRadiusCoefficient:newMaximum,radiusCoefficientBound:bound,
      radiusMaskExactlyAccumulatedAsDyadicThenNearestEvenRounded:true,radiusCoefficientsClipped:false,
      radiusBoxPreserved:true,oldVectorModified:false,cutHeightCoefficientUnchanged:true,
      exactRealPhysicalMetricAndPositionPreserved:true,binary64BitwiseFieldIdentityClaimed:false,
      changingRadiusAfterInjectionIsNewPhysicalMetricDesign:true,
      radialQuadratureChanged:levels>0,angularPrimitiveQuadratureChanged:targetN!==oldN,
      originalNormalReusable:false,actualNewProviderEvaluated:false,actualNonlinearAcceptedState:false}};
}
function cubic(t){
  const a=Math.abs(t),sg=t<0?-1:1;
  if(a>=2)return [0,0,0];
  if(a<1)return [(4-6*a*a+3*a*a*a)/6,sg*(-12*a+9*a*a)/6,(-12+18*a)/6];
  return [(2-a)**3/6,-sg*(2-a)**2/2,2-a];
}
function radiusCorrectionJets(z,definition,s,c,S){
  const J=definition.radialBasisCount,K=definition.angularModes,L=layout190(J,K),h=(S-c)/(J+3),out=[0,0,0];
  assert(S>c&&z.length===L.radius[1],"Radius evaluation identity mismatch");
  for(let j=0;j<J;++j){const b=cubic((s-(c+(j+2)*h))/h),q=z[L.radius[0]+j];out[0]+=q*b[0];out[1]+=q*b[1]/h;out[2]+=q*b[2]/(h*h);}
  return out;
}
module.exports={prolongR190State,refineRadiusCoefficients,radiusCorrectionJets,layout190,binaryDyadic,roundDyadic};
