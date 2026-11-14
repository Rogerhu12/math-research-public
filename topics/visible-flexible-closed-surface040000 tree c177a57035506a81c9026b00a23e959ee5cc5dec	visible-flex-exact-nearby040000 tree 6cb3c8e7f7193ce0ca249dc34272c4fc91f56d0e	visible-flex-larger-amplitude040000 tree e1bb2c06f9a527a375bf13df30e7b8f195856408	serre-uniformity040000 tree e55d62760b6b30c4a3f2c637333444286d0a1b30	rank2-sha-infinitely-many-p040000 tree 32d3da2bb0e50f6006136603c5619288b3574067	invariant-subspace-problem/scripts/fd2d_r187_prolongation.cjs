"use strict";
/* Exact real-function nesting for the frozen R187 centered cardinal cubic
 * radial basis and sin(2*k*u) angular corrections. Arithmetic cache uses
 * binary64 and is not represented as an exact bitwise field identity.
 * No physical profile, seed, boundary amplitude, or provider is modified.
 */
function requireCondition(ok, message) { if (!ok) throw new Error(message); }
function integer(x, name, minimum) {
  requireCondition(Number.isInteger(x) && x >= minimum, name + " is invalid");
  return x;
}
function layout(J,K) {
  const JK=J*K, n=2*JK+J+1;
  return {theta:[0,JK],phi:[JK,2*JK],height:[2*JK,2*JK+J],cutHeight:n-1};
}
function copyFinite(z,n) {
  requireCondition(z && z.length===n,"Parameter vector has the wrong dimension");
  const out=new Float64Array(n);
  for(let i=0;i<n;++i) {
    requireCondition(typeof z[i]==="number" && Number.isFinite(z[i]),"Nonfinite parameter");
    out[i]=z[i];
  }
  return out;
}
function cardinalCubic(t) {
  const a=Math.abs(t),sg=t<0?-1:1;
  if(a>=2)return [0,0,0];
  if(a<1)return [(4-6*a*a+3*a*a*a)/6,sg*(-12*a+9*a*a)/6,(-12+18*a)/6];
  return [(2-a)**3/6,-sg*(2-a)**2/2,2-a];
}
function refineOnce(z,J,K) {
  const nextJ=2*J+3,old=layout(J,K),next=layout(nextJ,K);
  const out=new Float64Array(2*nextJ*K+nextJ+1),mask=[1/8,4/8,6/8,4/8,1/8];
  for(const name of ["theta","phi"])
    for(let j=0;j<J;++j)for(let k=0;k<K;++k) {
      const c=z[old[name][0]+j*K+k];
      for(let r=0;r<5;++r)out[next[name][0]+(2*j+r)*K+k]+=mask[r]*c;
    }
  for(let j=0;j<J;++j)for(let r=0;r<5;++r)
    out[next.height[0]+2*j+r]+=mask[r]*z[old.height[0]+j];
  out[next.cutHeight]=z[old.cutHeight];
  return {vector:out,J:nextJ};
}
function padAngular(z,J,K,nextK) {
  const old=layout(J,K),next=layout(J,nextK),out=new Float64Array(2*J*nextK+J+1);
  for(const name of ["theta","phi"])
    for(let j=0;j<J;++j)for(let k=0;k<K;++k)
      out[next[name][0]+j*nextK+k]=z[old[name][0]+j*K+k];
  for(let j=0;j<J;++j)out[next.height[0]+j]=z[old.height[0]+j];
  out[next.cutHeight]=z[old.cutHeight];
  return out;
}

function prolongR187State(z,definition,options={}) {
  requireCondition(definition && definition.schema==="fd2d-R187-C2-direct-position-two-angle-finite-provider-v1",
    "Require the actual R187 provider definition");
  const J=integer(definition.radialBasisCount,"old radial count",1),K=integer(definition.angularModes,"old angular count",1);
  const oldN=integer(definition.fullEquivalentAngles,"old angular quadrature count",16);
  requireCondition(oldN%4===0,"Old angular quadrature must be divisible by four");
  const levels=integer(options.radialRefinements===undefined?1:options.radialRefinements,"radial refinement levels",0);
  const nextK=integer(options.modes===undefined?K:options.modes,"target angular modes",K);
  const nextN=integer(options.angles===undefined?oldN:options.angles,"target angular quadrature count",16);
  requireCondition(nextN%4===0,"Target angular quadrature must be divisible by four");
  const oldDimension=2*J*K+J+1;
  requireCondition(definition.dimension===oldDimension,"Definition dimension mismatch");
  if(definition.stateLayout)requireCondition(JSON.stringify(definition.stateLayout)===JSON.stringify(layout(J,K)),"Unexpected R187 state layout");
  let vector=copyFinite(z,oldDimension),newJ=J;
  for(let l=0;l<levels;++l) {const r=refineOnce(vector,newJ,K);vector=r.vector;newJ=r.J;}
  if(nextK!==K)vector=padAngular(vector,newJ,K,nextK);
  const targetDefinition={...definition,radialBasisCount:newJ,angularModes:nextK,
    fullEquivalentAngles:nextN,dimension:vector.length,stateLayout:layout(newJ,nextK)};
  const provenance={schema:"fd2d-R189-cardinal-cubic-and-angular-prolongation-v1",
    oldRadialBasisCount:J,newRadialBasisCount:newJ,oldAngularModes:K,newAngularModes:nextK,
    radialRefinementLevels:levels,stepRatio:2**levels,
    oldDimension,newDimension:vector.length,oldEquivalentAngles:oldN,newEquivalentAngles:nextN,
    radialMaskNumerators:[1,4,6,4,1],radialMaskDenominator:8,
    newIndicesForOldIndex:"2*j + r, r=0,...,4, independently for each old angular mode and height",
    highAngularCoefficients:"exact zero padding",cutHeightCoefficientUnchanged:true,
    originalVectorModified:false,exactRealFunctionIdentity:true,binary64BitwiseFieldIdentityClaimed:false,
    physicalMetricMustBeIdentical:true,seedAndBoundaryDataMustBeIdentical:true,
    mathematicalFullPrimitiveAndPositionTwoJetsPreserved:true,
    angularPrimitiveQuadratureChanged:nextN!==oldN,
    radialQuadratureChanged:levels>0,oldNormalReusable:false,
    actualNewProviderEvaluated:false,actualNonlinearAcceptance:false};
  return {vector,definition:targetDefinition,
    providerOptions:{radialBasisCount:newJ,modes:nextK,angles:nextN},provenance};
}

/* Pure corrections, useful for common-point identity checks. Rows are
 * [value, s, ss, u, su, uu]. The seed and physical profile are external.
 */
function correctionJets(z,definition,s,u,c,S) {
  const J=definition.radialBasisCount,K=definition.angularModes,L=layout(J,K);
  requireCondition(Number.isFinite(c)&&Number.isFinite(S)&&S>c,"Invalid fixed physical interval");
  requireCondition(z.length===2*J*K+J+1,"Wrong correction vector");
  const step=(S-c)/(J+3),theta=new Float64Array(6),phi=new Float64Array(6),height=new Float64Array(3);
  for(let j=0;j<J;++j) {
    const q=cardinalCubic((s-(c+(j+2)*step))/step),b=q[0],bs=q[1]/step,bss=q[2]/(step*step);
    for(let k=0;k<K;++k) {
      const omega=2*(k+1),f=Math.sin(omega*u),fu=omega*Math.cos(omega*u),fuu=-omega*omega*f;
      const jet=[b*f,bs*f,bss*f,b*fu,bs*fu,b*fuu];
      for(const pair of [[theta,L.theta[0]],[phi,L.phi[0]]]) {
        const coefficient=z[pair[1]+j*K+k];
        for(let d=0;d<6;++d)pair[0][d]+=coefficient*jet[d];
      }
    }
    const a=z[L.height[0]+j];height[0]+=a*b;height[1]+=a*bs;height[2]+=a*bss;
  }
  let shape=[0,0,0];
  if(s>=S)shape=[1,0,0];
  else if(s>c) {const t=(s-c)/(S-c),h=S-c;shape=[t*t*t*(10+t*(-15+6*t)),30*t*t*(1-t)*(1-t)/h,60*t*(1-t)*(1-2*t)/(h*h)];}
  for(let d=0;d<3;++d)height[d]+=z[L.cutHeight]*shape[d];
  return {theta,phi,height};
}
module.exports={prolongR187State,correctionJets,cardinalCubic,layout};
