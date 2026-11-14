"use strict";
/* R201 explicit-block adapter of R195 v2; only radialPermutation is replaced. Explicit integer block width; original three-band source stays frozen.
 * Width defaults to 3. A caller may explicitly choose 4 to preserve measured
 * floating support-edge tails. All off-width entries are still checked.
 * Column-scaled block-band + one-border LM direction.
 * Only the linear algebra changes. H=J^T J, g=J^T r at the same state.
 * Dense input is scanned completely; ANY nonzero outside the declared radial
 * block width is rejected, never dropped. No hidden damping shift.
 * R187/R190 layouts and R191 wrappers are decoded explicitly.
 */
function need(c,m){if(!c)throw Error(m);}
function finite(x,m){need(typeof x==="number"&&Number.isFinite(x),m+" must be finite");return x;}
function copyVector(x,n,name){
  need(x&&typeof x.length==="number"&&(n==null||x.length===n),name+" dimension");
  return Float64Array.from(x,(v)=>finite(Number(v),name));
}
function dot(x,y){
  need(x.length===y.length,"dot dimension");let s=0,c=0;
  for(let i=0;i<x.length;i++){const t=x[i]*y[i],v=s+t;c+=Math.abs(s)>=Math.abs(t)?(s-v)+t:(t-v)+s;s=v;}return s+c;
}
function norm(x){let n=0;for(const v of x)n=Math.hypot(n,v);return n;}
function maximum(x){let a=0;for(const v of x)a=Math.max(a,Math.abs(v));return a;}
function radialPermutation(definition,options={}){
  need(definition&&typeof definition==="object","Explicit R201 definition required");
  need(["fd2d-R201-R205-full-half-developed-tail-curvature-provider-v1","fd2d-R201-R205-half-period-complete-position-geometric-guide-v1"].includes(definition.schema),"Explicit R201 schema required");
  const d=definition.radialBlockLayout,blocks=d&&d.radialBlocks,n=definition.dimension;
  need(d&&d.schema==="fd2d-R201-explicit-radial-blocks-v1"&&Array.isArray(blocks)&&blocks.length>0,"Declared R201 radial blocks required");
  const J=blocks.length,b=blocks[0].length,m=J*b,w=options.halfBandwidthBlocks===undefined?4:Number(options.halfBandwidthBlocks);
  need(Number.isInteger(n)&&n===m+1&&Number.isInteger(w)&&w>=0&&b>0,"Complete equal-width blocks and one border");
  const perm=[];for(const row of blocks){need(Array.isArray(row)&&row.length===b,"Equal width");perm.push(...row);}
  perm.push(d.globalBorder);need(perm.every(x=>Number.isInteger(x)&&x>=0&&x<n)&&new Set(perm).size===n,"Actual complete index bijection");
  const permutation=Int32Array.from(perm),inverse=new Int32Array(n);for(let i=0;i<n;i++)inverse[permutation[i]]=i;
  return {schema:"R201-explicit-radial-block-permutation-v1",n,fieldCount:m,J,K:definition.angularModes,blockSize:b,halfBandwidthBlocks:w,stride:(w+1)*b,
    cutHeightOriginalIndex:d.globalBorder,permutation,inverse,designed:true,providerSchema:definition.schema};
}
function prepareBandBorderNormal(normal,definition,options={}){
  need(normal&&normal.H!=null&&normal.g!=null,"H and g required");
  const layout=radialPermutation(definition,options),{n,fieldCount:m,blockSize:b,stride,permutation,halfBandwidthBlocks:w}=layout;
  const gradient=copyVector(normal.g,n,"g"),R2=finite(Number(normal.squaredNorm),"squaredNorm");
  need(R2>=0,"Negative squaredNorm");
  const H=normal.H,rows=H.length===n&&H[0]!=null&&typeof H[0]!=="number"&&typeof H[0].length==="number";
  need(rows||H.length===n*n,"Flat H must be row-major square");
  if(rows)for(let i=0;i<n;i++)need(H[i].length===n,"H row dimension");
  const get=rows?(i,j)=>Number(H[i][j]):(i,j)=>Number(H[i*n+j]);
  const diagonal=new Float64Array(n),scale=new Float64Array(n),zero=[];
  const given=normal.diagonal==null?null:copyVector(normal.diagonal,n,"diagonal");
  let givenDifference=0,givenRelative=0;
  for(let i=0;i<n;i++){
    const h=finite(get(i,i),"H diagonal");need(h>=0,"A J^T J diagonal cannot be negative");diagonal[i]=h;
    scale[i]=h>0?1/Math.sqrt(h):1;need(Number.isFinite(scale[i]),"Nonfinite exact column scale");
    if(h===0)zero.push(i);
    if(given){const e=Math.abs(h-given[i]);givenDifference=Math.max(givenDifference,e);givenRelative=Math.max(givenRelative,e/Math.max(Number.MIN_VALUE,h,Math.abs(given[i])));}
  }
  const band=new Float64Array(m*stride),originalLower=new Float64Array(m*stride),originalUpper=new Float64Array(m*stride);
  const border=new Float64Array(m),originalFieldToBorder=new Float64Array(m),originalBorderToField=new Float64Array(m);
  let borderDiagonal=0,originalBorderDiagonal=0,symmetryAdjustment=0,scaledSymmetryAdjustment=0,scalingOrderSymmetryAdjustment=0;
  let offBandCount=0,offBandMaximum=0,offBandFirst=null,storedLowerNonzeros=0;
  for(let p=0;p<n;p++){
    const i=permutation[p],si=scale[i];
    for(let q=0;q<=p;q++){
      const j=permutation[q],sj=scale[j],h=finite(get(i,j),"H entry"),ht=finite(get(j,i),"H transpose entry");
      if(p<m&&Math.floor(p/b)-Math.floor(q/b)>w){
        if(h!==0||ht!==0){
          offBandCount++;offBandMaximum=Math.max(offBandMaximum,Math.abs(h),Math.abs(ht));
          if(!offBandFirst)offBandFirst={originalIndices:[i,j],radialBlocks:[Math.floor(p/b),Math.floor(q/b)],entries:[h,ht]};
        }
        continue;
      }
      const s=p===q?h:.5*h+.5*ht;
      const raw=(h*si)*sj,rawT=(ht*sj)*si,low=(s*si)*sj,up=(s*sj)*si;
      need([raw,rawT,low,up].every(Number.isFinite),"Nonfinite scaled normal");
      const work=p===q?low:.5*low+.5*up;
      symmetryAdjustment=Math.max(symmetryAdjustment,Math.abs(s-h),Math.abs(s-ht));
      scaledSymmetryAdjustment=Math.max(scaledSymmetryAdjustment,Math.abs(low-raw),Math.abs(up-rawT));
      scalingOrderSymmetryAdjustment=Math.max(scalingOrderSymmetryAdjustment,Math.abs(low-up));
      if(work!==0)storedLowerNonzeros++;
      if(p<m){const at=p*stride+p-q;band[at]=work;originalLower[at]=raw;originalUpper[at]=rawT;}
      else if(q<m){border[q]=work;originalBorderToField[q]=raw;originalFieldToBorder[q]=rawT;}
      else {borderDiagonal=work;originalBorderDiagonal=raw;}
    }
  }
  if(offBandCount){
    const e=Error("Nonzero H outside the explicitly declared radial block width; no entries were discarded for a solve");
    e.code="NONZERO_OUTSIDE_RADIAL_BAND";e.details={offBandCount,offBandMaximum,offBandFirst};throw e;
  }
  const scaledGradient=new Float64Array(n);
  for(let p=0;p<n;p++){scaledGradient[p]=gradient[permutation[p]]*scale[permutation[p]];need(Number.isFinite(scaledGradient[p]),"Nonfinite scaled gradient");}
  return {schema:"R195-prepared-scaled-band-border-v1",layout,gradient,squaredNorm:R2,diagonal,scale,scaledGradient,
    band,originalLower,originalUpper,border,originalFieldToBorder,originalBorderToField,borderDiagonal,originalBorderDiagonal,
    info:{dimension:n,radialBlocks:layout.J,blockSize:b,halfBandwidthBlocks:w,
      scalarStorageStride:stride,oneGlobalBorderOriginalIndex:layout.cutHeightOriginalIndex,
      offBandNonzeroCount:0,offBandMaximum:0,offBandTolerance:0,storedLowerNonzeros,
      zeroDiagonalColumns:zero,zeroDiagonalScale:1,exactPositiveDiagonalScale:"1/sqrt(Hjj)",
      suppliedDiagonalDifference:givenDifference,suppliedDiagonalRelativeDifference:givenRelative,suppliedDiagonalUsedInsteadOfHjj:false,
      symmetryAdjustment,scaledSymmetryAdjustment,scalingOrderSymmetryAdjustment,
      scaledGradientInfinity:maximum(scaledGradient),
      preparedNumericStorageBytes:band.byteLength+originalLower.byteLength+originalUpper.byteLength+border.byteLength+
        originalFieldToBorder.byteLength+originalBorderToField.byteLength+gradient.byteLength+diagonal.byteLength+scale.byteLength+scaledGradient.byteLength+
        permutation.byteLength+layout.inverse.byteLength,
      fullScaledMatrixAllocated:false,inputArraysModified:false,continuousCertificate:false}};
}
function fieldCholesky(p,lambda){
  const {fieldCount:m,blockSize:b,stride,halfBandwidthBlocks:w}=p.layout,L=new Float64Array(m*stride);
  let minimumPivot=Infinity,maximumPivot=0;
  for(let i=0;i<m;i++){
    const lo=Math.max(0,(Math.floor(i/b)-w)*b),oi=i*stride;
    for(let j=lo;j<=i;j++){
      let s=0,c=0;const oj=j*stride;
      for(let k=lo;k<j;k++){
        const t=L[oi+i-k]*L[oj+j-k],v=s+t;c+=Math.abs(s)>=Math.abs(t)?(s-v)+t:(t-v)+s;s=v;
      }
      const pivot=p.band[oi+i-j]+(i===j?lambda:0)-(s+c);
      if(i===j){
        if(!(Number.isFinite(pivot)&&pivot>0))return {ok:false,phase:"band_cholesky",failedPivot:i,pivot:Number.isFinite(pivot)?pivot:null,lambda};
        minimumPivot=Math.min(minimumPivot,pivot);maximumPivot=Math.max(maximumPivot,pivot);L[oi]=Math.sqrt(pivot);
      }else{
        const v=pivot/L[oj];
        if(!Number.isFinite(v))return {ok:false,phase:"band_cholesky",failedPivot:j,row:i,pivot:null,lambda};
        L[oi+i-j]=v;
      }
    }
  }
  return {ok:true,L,minimumPivot,maximumPivot};
}
function solveTwoFieldRHS(p,L){
  const {fieldCount:m,blockSize:b,stride,halfBandwidthBlocks:w}=p.layout;
  const q0=new Float64Array(m),t0=new Float64Array(m),q=new Float64Array(m),t=new Float64Array(m);
  for(let i=0;i<m;i++){
    const lo=Math.max(0,(Math.floor(i/b)-w)*b),oi=i*stride;let s=0,c=0,v=0,d=0;
    for(let j=lo;j<i;j++){
      const a=L[oi+i-j],x=a*q0[j],y=a*t0[j],sn=s+x,vn=v+y;
      c+=Math.abs(s)>=Math.abs(x)?(s-sn)+x:(x-sn)+s;
      d+=Math.abs(v)>=Math.abs(y)?(v-vn)+y:(y-vn)+v;s=sn;v=vn;
    }
    q0[i]=(-p.scaledGradient[i]-(s+c))/L[oi];t0[i]=(p.border[i]-(v+d))/L[oi];
  }
  for(let i=m-1;i>=0;i--){
    const hi=Math.min(m,(Math.floor(i/b)+w+1)*b);let s=0,c=0,v=0,d=0;
    for(let j=i+1;j<hi;j++){
      const a=L[j*stride+j-i],x=a*q[j],y=a*t[j],sn=s+x,vn=v+y;
      c+=Math.abs(s)>=Math.abs(x)?(s-sn)+x:(x-sn)+s;
      d+=Math.abs(v)>=Math.abs(y)?(v-vn)+y:(y-vn)+v;s=sn;v=vn;
    }
    q[i]=(q0[i]-(s+c))/L[i*stride];t[i]=(t0[i]-(v+d))/L[i*stride];
  }
  return {q,t};
}
function multiplyPrepared(p,q,original=false){
  const {n,fieldCount:m,blockSize:b,stride,halfBandwidthBlocks:w}=p.layout,out=new Float64Array(n);
  const lower=original?p.originalLower:p.band,upper=original?p.originalUpper:p.band;
  const fb=original?p.originalFieldToBorder:p.border,bf=original?p.originalBorderToField:p.border;
  for(let i=0;i<m;i++){
    const lo=Math.max(0,(Math.floor(i/b)-w)*b),hi=Math.min(m,(Math.floor(i/b)+w+1)*b);let s=0,c=0;
    for(let j=lo;j<hi;j++){
      const a=j<=i?lower[i*stride+i-j]:upper[j*stride+j-i],t=a*q[j],v=s+t;
      c+=Math.abs(s)>=Math.abs(t)?(s-v)+t:(t-v)+s;s=v;
    }
    const t=fb[i]*q[m],v=s+t;c+=Math.abs(s)>=Math.abs(t)?(s-v)+t:(t-v)+s;out[i]=v+c;
  }
  let s=0,c=0;
  for(let j=0;j<m;j++){const t=bf[j]*q[j],v=s+t;c+=Math.abs(s)>=Math.abs(t)?(s-v)+t:(t-v)+s;s=v;}
  const t=(original?p.originalBorderDiagonal:p.borderDiagonal)*q[m],v=s+t;
  c+=Math.abs(s)>=Math.abs(t)?(s-v)+t:(t-v)+s;out[m]=v+c;return out;
}
function solvePreparedBandBorder(prepared,lambda){
  const p=prepared;need(p&&p.schema==="R195-prepared-scaled-band-border-v1","Prepared R195 normal required");
  finite(lambda,"lambda");need(lambda>0,"A strictly positive explicit LM damping is required");
  const {n,fieldCount:m,permutation}=p.layout;
  const factor=fieldCholesky(p,lambda);
  if(!factor.ok)return {...factor,preparedInfo:p.info,hiddenDiagonalShift:0};
  const two=solveTwoFieldRHS(p,factor.L);
  if(!Array.from(two.q).every(Number.isFinite)||!Array.from(two.t).every(Number.isFinite))
    return {ok:false,phase:"field_triangular_solve",lambda,preparedInfo:p.info,hiddenDiagonalShift:0};
  const borderContraction=dot(p.border,two.t),schur=p.borderDiagonal+lambda-borderContraction;
  if(!(Number.isFinite(schur)&&schur>0))
    return {ok:false,phase:"border_schur",failedPivot:m,pivot:Number.isFinite(schur)?schur:null,lambda,preparedInfo:p.info,hiddenDiagonalShift:0};
  const rhs=-p.scaledGradient[m]-dot(p.border,two.q),qb=rhs/schur,q=new Float64Array(n);
  q[m]=qb;for(let i=0;i<m;i++)q[i]=two.q[i]-two.t[i]*qb;
  const direction=new Float64Array(n),scaledDirection=new Float64Array(n);
  for(let i=0;i<n;i++){scaledDirection[permutation[i]]=q[i];direction[permutation[i]]=p.scale[permutation[i]]*q[i];}
  if(!Array.from(q).every(Number.isFinite)||!Array.from(direction).every(Number.isFinite))
    return {ok:false,phase:"border_back_substitution",lambda,preparedInfo:p.info,hiddenDiagonalShift:0};
  const hq=multiplyPrepared(p,q),original=multiplyPrepared(p,q,true);
  const aq=new Float64Array(n),residual=new Float64Array(n),originalResidual=new Float64Array(n);
  let unscaledMaximum=0;
  for(let i=0;i<n;i++){
    aq[i]=hq[i]+lambda*q[i];residual[i]=aq[i]+p.scaledGradient[i];
    originalResidual[i]=original[i]+lambda*q[i]+p.scaledGradient[i];
    unscaledMaximum=Math.max(unscaledMaximum,Math.abs(originalResidual[i]/p.scale[permutation[i]]));
  }
  const slope=dot(p.gradient,direction),scaledSlope=dot(p.scaledGradient,q),quadratic=dot(q,hq);
  const predictedSquaredNorm=p.squaredNorm+2*slope+quadratic,denominator=norm(p.scaledGradient)+norm(aq);
  if(![slope,scaledSlope,quadratic,predictedSquaredNorm,unscaledMaximum].every(Number.isFinite))
    return {ok:false,phase:"model_diagnostics",lambda,preparedInfo:p.info,hiddenDiagonalShift:0};
  return {ok:true,lambda,direction,scaledDirection,scale:new Float64Array(p.scale),
    slope,quadratic,predictedSquaredNorm,predictedReduction:-slope-.5*quadratic,
    info:{...p.info,linearSolver:"R195 band Cholesky with two field RHS and scalar Schur border",
      fieldMinimumPivot:factor.minimumPivot,fieldMaximumPivot:factor.maximumPivot,
      borderSchur:schur,borderContraction,
      minimumPivot:Math.min(factor.minimumPivot,schur),maximumPivot:Math.max(factor.maximumPivot,schur),
      scaledSlope,physicalAndScaledSlopeDifference:Math.abs(slope-scaledSlope),
      originalScaledEquationResidualMaximum:maximum(originalResidual),workingScaledEquationResidualMaximum:maximum(residual),
      workingScaledEquationRelativeResidual:denominator>0?norm(residual)/denominator:0,
      originalUnscaledDampedEquationResidualMaximum:unscaledMaximum,
      factorNumericStorageBytes:factor.L.byteLength,diagonalDampingInScaledCoordinates:lambda,hiddenDiagonalShift:0,
      actualTrialEvaluated:false,finiteSpaceLowerBoundClaimed:false,fullDenseFactorAllocated:false}};
}
function solveDampedNormal(normal,options={}){
  need(options.definition,"Explicit provider definition required");
  return solvePreparedBandBorder(prepareBandBorderNormal(normal,options.definition,options),
    options.lambda===undefined?1e-3:Number(options.lambda));
}
module.exports={radialPermutation,prepareBandBorderNormal,solvePreparedBandBorder,solveDampedNormal,multiplyPrepared,dot,norm};
