"use strict";
/* R206: append one genuine global parameter to a complete R195-compatible
 * provider (whose original cut height is already a border). No columns,
 * normal entries, domain conditions or actual Armijo values are discarded.
 */
function createR206AppendedGlobalKernel(baseKernel){
 const need=(v,m)=>{if(!v)throw Error(m);};
 const finite=(v,m)=>{need(Number.isFinite(v),m);return v;};
 const dot=baseKernel.dot||((a,b)=>a.reduce((s,v,i)=>s+v*b[i],0));
 const norm=baseKernel.norm||(a=>Math.hypot(...a));
 function prepareBandBorderNormal(normal,definition,options={}){
  need(definition?.schema==="fd2d-R206-appended-global-parameter-provider-v1","Explicit R206 provider required");
  const bd=definition.baseProvider,n=bd?.dimension,N=n+1;
  need(Number.isInteger(n)&&n>0&&definition.dimension===N&&definition.globalIndex===n,"Explicit appended global layout required");
  need(normal.H?.length===N*N&&normal.g?.length===N,"Complete row-major full normal required");
  const H=Float64Array.from(normal.H,x=>finite(x,"H")),g=Float64Array.from(normal.g,x=>finite(x,"g"));
  const H0=new Float64Array(n*n),g0=g.slice(0,n),hbar=new Float64Array(n);
  for(let i=0;i<n;i++){
   for(let j=0;j<n;j++)H0[i*n+j]=H[i*N+j];
   hbar[i]=.5*H[i*N+n]+.5*H[n*N+i];
  }
  const d=H[n*N+n];need(d>=0,"Nonnegative global diagonal required");
  const sA=d>0?1/Math.sqrt(d):1;need(Number.isFinite(sA)&&sA>0,"Finite positive global scale required");
  const R2=finite(normal.squaredNorm,"Squared norm");need(R2>=0,"Nonnegative squared norm required");
  const zdiag=normal.diagonal?Float64Array.from(normal.diagonal).slice(0,n):undefined;
  if(normal.diagonal)need(normal.diagonal.length===N&&normal.diagonal[n]===d,"Complete fresh diagonal required");
  const p=baseKernel.prepareBandBorderNormal({H:H0,g:g0,diagonal:zdiag,squaredNorm:R2},bd,options);
  const b=new Float64Array(n),bTop=new Float64Array(n),bBottom=new Float64Array(n),auxG=new Float64Array(n);
  for(let i=0;i<n;i++){
   b[i]=(hbar[i]*p.scale[i])*sA;
   bTop[i]=(H[i*N+n]*p.scale[i])*sA;
   bBottom[i]=(H[n*N+i]*sA)*p.scale[i];
   auxG[i]=b[i]/p.scale[i];
  }
  const aux=baseKernel.prepareBandBorderNormal({H:H0,g:auxG,squaredNorm:0},bd,options);
  let rhsRounding=0;
  for(let i=0;i<n;i++){
   need(p.scale[i]===aux.scale[i]&&p.layout.permutation[i]===aux.layout.permutation[i],"Identical base matrix scaling required");
   rhsRounding=Math.max(rhsRounding,Math.abs(aux.scaledGradient[p.layout.inverse[i]]-b[i]));
  }
  const scaledG=Float64Array.from(g,(v,i)=>v*(i<n?p.scale[i]:sA));
  const info={...p.info,linearSolver:"R206 appended global Schur on the full R195 cut-border block",
   globalIndex:n,globalName:definition.globalName||"declared_global",originalDimension:n,dimension:N,
   oldNormalColumnsRetained:true,auxiliaryRHSIsLinearAlgebraNotNewResidual:true,
   auxiliaryScaledRHSRoundingMaximum:rhsRounding,
   scaledGradientInfinity:Math.max(...scaledG.map(Math.abs)),hiddenDiagonalShift:0};
  return {schema:"R206-prepared-appended-global-normal-v1",layout:{n:N},n:N,oldN:n,H,g,
   squaredNorm:R2,base:p,aux,b,bTop,bBottom,scaleA:sA,scaledGlobalDiagonal:(d*sA)*sA,scaledG,info};
 }
 function solvePreparedBandBorder(p,lambda){
  need(p?.schema==="R206-prepared-appended-global-normal-v1","Prepared R206 normal required");
  need(Number.isFinite(lambda)&&lambda>0,"Explicit positive LM damping required");
  const x=baseKernel.solvePreparedBandBorder(p.base,lambda);
  if(!x.ok)return {...x,phase:"R206_base_"+x.phase};
  const w=baseKernel.solvePreparedBandBorder(p.aux,lambda);
  if(!w.ok)return {...w,phase:"R206_aux_"+w.phase};
  const n=p.oldN,N=n+1,contraction=dot(p.b,w.scaledDirection);
  const schur=p.scaledGlobalDiagonal+lambda+contraction;
  if(!(Number.isFinite(schur)&&schur>0))return {ok:false,phase:"R206_global_schur",failedPivot:n,pivot:Number.isFinite(schur)?schur:null,lambda,hiddenDiagonalShift:0};
  const va=(-p.scaledG[n]-dot(p.b,x.scaledDirection))/schur;
  const scaledDirection=new Float64Array(N),direction=new Float64Array(N),scale=new Float64Array(N);
  for(let i=0;i<n;i++){scale[i]=p.base.scale[i];scaledDirection[i]=x.scaledDirection[i]+w.scaledDirection[i]*va;direction[i]=scale[i]*scaledDirection[i];}
  scale[n]=p.scaleA;scaledDirection[n]=va;direction[n]=p.scaleA*va;
  if(!Array.from(direction).every(Number.isFinite))return {ok:false,phase:"R206_global_back_substitution",lambda,hiddenDiagonalShift:0};
  const q=Float64Array.from(p.base.layout.permutation,i=>scaledDirection[i]);
  const hv=baseKernel.multiplyPrepared(p.base,q),original=baseKernel.multiplyPrepared(p.base,q,true);
  const work=new Float64Array(N),orig=new Float64Array(N),aq=new Float64Array(N),oa=new Float64Array(N),res=new Float64Array(N),ores=new Float64Array(N);
  for(let j=0;j<n;j++){
   const i=p.base.layout.permutation[j];
   work[i]=hv[j]+p.b[i]*va;orig[i]=original[j]+p.bTop[i]*va;
  }
  work[n]=dot(p.b,scaledDirection.subarray(0,n))+p.scaledGlobalDiagonal*va;
  orig[n]=dot(p.bBottom,scaledDirection.subarray(0,n))+p.scaledGlobalDiagonal*va;
  for(let i=0;i<N;i++){
   aq[i]=work[i]+lambda*scaledDirection[i];oa[i]=orig[i]+lambda*scaledDirection[i];
   res[i]=aq[i]+p.scaledG[i];ores[i]=oa[i]+p.scaledG[i];
  }
  const slope=dot(p.g,direction),quadratic=dot(scaledDirection,work),scaledSlope=dot(p.scaledG,scaledDirection);
  const denom=norm(p.scaledG)+norm(aq),oden=norm(p.scaledG)+norm(oa);
  if(![slope,quadratic,scaledSlope].every(Number.isFinite))return {ok:false,phase:"R206_model_diagnostics",lambda,hiddenDiagonalShift:0};
  return {ok:true,lambda,direction,scaledDirection,scale,slope,quadratic,
   predictedSquaredNorm:p.squaredNorm+2*slope+quadratic,predictedReduction:-slope-.5*quadratic,
   info:{...p.info,baseSolver:x.info,auxiliarySolver:w.info,globalSchur:schur,globalContraction:contraction,
    scaledSlope,physicalAndScaledSlopeDifference:Math.abs(slope-scaledSlope),
    workingScaledEquationResidualMaximum:Math.max(...res.map(Math.abs)),
    originalScaledEquationResidualMaximum:Math.max(...ores.map(Math.abs)),
    workingScaledEquationRelativeResidual:denom>0?norm(res)/denom:0,
    originalScaledEquationRelativeResidual:oden>0?norm(ores)/oden:0,
    hiddenDiagonalShift:0,actualTrialEvaluated:false,fullDenseFactorAllocated:false}};
 }
 return {prepareBandBorderNormal,solvePreparedBandBorder,
  implementationDefinition:{schema:"R206-appended-global-Schur-v1",originalCutBorderRetained:true,
   explicitNewGlobalColumns:1,fullNormalRequired:true,auxiliaryBaseFactorizations:2,hiddenDiagonalShift:0}};
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR206AppendedGlobalKernel};
