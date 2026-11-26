"use strict";
/* Recovered v2 preparation: preserve the original complete R206 solve.
 * This file has a new source identity. It does not claim the hash or exact
 * fixture identity of the source lost in the executor outage.
 * The caller must keep normal.H read-only until the prepared solve finishes.
 */
const {createR206AppendedGlobalKernel}=require("./fd2d_appended_global_schur_R206.cjs");
function createSharedBandR206Kernel(baseKernel){
  const original=createR206AppendedGlobalKernel(baseKernel);
  const need=(v,m)=>{if(!v)throw Error(m);};
  const finite=(v,m)=>{need(Number.isFinite(v),m);return v;};
  function baseRows(H,n,N){
    if(typeof H.subarray==="function")
      return Array.from({length:n},(_,i)=>H.subarray(i*N,i*N+n));
    return Array.from({length:n},(_,i)=>new Proxy({length:n},{
      get(target,key){
        if(key==="length")return n;
        if(typeof key==="string"&&/^(0|[1-9][0-9]*)$/.test(key)){
          const j=Number(key);return j<n?H[i*N+j]:undefined;
        }
        return Reflect.get(target,key);
      }
    }));
  }
  function prepareBandBorderNormal(normal,definition,options={}){
    need(definition?.schema==="fd2d-R206-appended-global-parameter-provider-v1","Explicit R206 provider required");
    const bd=definition.baseProvider,n=bd?.dimension,N=n+1;
    need(Number.isInteger(n)&&n>0&&definition.dimension===N&&definition.globalIndex===n,
      "Explicit appended global layout required");
    need(normal.H?.length===N*N&&normal.g?.length===N,"Complete row-major full normal required");
    // The original clone validates every scalar. Validate the same scalars,
    // in the same order, but borrow the unchanged input rather than copy it.
    const H=normal.H;
    for(let i=0;i<H.length;i++)finite(H[i],"H");
    const g=Float64Array.from(normal.g,x=>finite(x,"g"));
    const H0=baseRows(H,n,N),g0=g.slice(0,n),hbar=new Float64Array(n);
    for(let i=0;i<n;i++)hbar[i]=.5*H[i*N+n]+.5*H[n*N+i];
    const d=H[n*N+n];need(d>=0,"Nonnegative global diagonal required");
    const sA=d>0?1/Math.sqrt(d):1;need(Number.isFinite(sA)&&sA>0,"Finite positive global scale required");
    const R2=finite(normal.squaredNorm,"Squared norm");need(R2>=0,"Nonnegative squared norm required");
    const zdiag=normal.diagonal?Float64Array.from(normal.diagonal).slice(0,n):undefined;
    if(normal.diagonal)need(normal.diagonal.length===N&&normal.diagonal[n]===d,"Complete fresh diagonal required");
    // Unmodified base preparation scans BOTH original orientations, rejects
    // every nonzero off-band entry, and retains all original diagnostics.
    const p=baseKernel.prepareBandBorderNormal({H:H0,g:g0,diagonal:zdiag,squaredNorm:R2},bd,options);
    const b=new Float64Array(n),bTop=new Float64Array(n),bBottom=new Float64Array(n),auxG=new Float64Array(n);
    for(let i=0;i<n;i++){
      b[i]=(hbar[i]*p.scale[i])*sA;
      bTop[i]=(H[i*N+n]*p.scale[i])*sA;
      bBottom[i]=(H[n*N+i]*sA)*p.scale[i];
      auxG[i]=b[i]/p.scale[i];
    }
    // The old second preparation has exactly the same H0, permutation and
    // scale. Only its g and squaredNorm differ. Keep the original division/
    // multiplication roundtrip, rather than replacing the RHS by b directly.
    const auxiliaryGradient=Float64Array.from(auxG,x=>finite(Number(x),"Auxiliary g"));
    const auxiliaryScaledGradient=new Float64Array(n);
    let auxiliaryInfinity=0;
    for(let j=0;j<n;j++){
      const i=p.layout.permutation[j],v=auxiliaryGradient[i]*p.scale[i];
      need(Number.isFinite(v),"Nonfinite scaled auxiliary gradient");
      auxiliaryScaledGradient[j]=v;auxiliaryInfinity=Math.max(auxiliaryInfinity,Math.abs(v));
    }
    const aux={...p,gradient:auxiliaryGradient,scaledGradient:auxiliaryScaledGradient,squaredNorm:0,
      info:{...p.info,suppliedDiagonalDifference:0,suppliedDiagonalRelativeDifference:0,
        scaledGradientInfinity:auxiliaryInfinity}};
    let rhsRounding=0;
    for(let i=0;i<n;i++){
      need(p.scale[i]===aux.scale[i]&&p.layout.permutation[i]===aux.layout.permutation[i],
        "Identical base matrix scaling required");
      rhsRounding=Math.max(rhsRounding,Math.abs(aux.scaledGradient[p.layout.inverse[i]]-b[i]));
    }
    const scaledG=Float64Array.from(g,(v,i)=>v*(i<n?p.scale[i]:sA));
    const sharedNames=["band","originalLower","originalUpper","border","originalFieldToBorder",
      "originalBorderToField","diagonal","scale"];
    const sharedNumericBytes=sharedNames.reduce((sum,key)=>sum+p[key].byteLength,0)+
      p.layout.permutation.byteLength+p.layout.inverse.byteLength;
    const info={...p.info,linearSolver:"R206 appended global Schur on the full R195 cut-border block",
      globalIndex:n,globalName:definition.globalName||"declared_global",originalDimension:n,dimension:N,
      oldNormalColumnsRetained:true,auxiliaryRHSIsLinearAlgebraNotNewResidual:true,
      auxiliaryScaledRHSRoundingMaximum:rhsRounding,
      scaledGradientInfinity:Math.max(...scaledG.map(Math.abs)),hiddenDiagonalShift:0,
      memoryPreparation:{schema:"6a65-R206-shared-band-preparation-recovered-v2",
        fullHReadOnlyBorrowed:true,baseHUsesRowViews:true,completeBasePreparationCalls:1,
        auxiliaryMatrixArraysShared:true,auxiliaryGradientArraysIndependent:true,
        originalAuxiliaryRHSDivisionMultiplicationOrderPreserved:true,
        avoidedFullHCloneBytes:N*N*8,avoidedDenseBaseHCopyBytes:n*n*8,
        avoidedDuplicateAuxiliaryNumericBytes:sharedNumericBytes,
        byteCountsAreAllocationAccountingNotMeasuredRSS:true,
        preparedNumericStorageBytesInBaseInfoCountsLogicalArrays:true}};
    return {schema:"R206-prepared-appended-global-normal-v1",layout:{n:N},n:N,oldN:n,H,g,
      squaredNorm:R2,base:p,aux,b,bTop,bBottom,scaleA:sA,scaledGlobalDiagonal:(d*sA)*sA,scaledG,info};
  }
  return {prepareBandBorderNormal,solvePreparedBandBorder:original.solvePreparedBandBorder,
    implementationDefinition:{...original.implementationDefinition,
      schema:"6a65-R206-shared-band-memory-kernel-recovered-v2",
      preparationOnlyChanged:true,originalSolveFunctionRetained:true,
      completeBasePreparationCalls:1,fullHReadOnlyBorrowed:true,
      auxiliaryMatrixArraysShared:true,auxiliaryBaseFactorizations:2,
      noRowsOrColumnsDropped:true,strictOffBandRejectionPreserved:true}};
}
module.exports={createSharedBandR206Kernel};
