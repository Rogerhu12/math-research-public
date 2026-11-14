// R108 companion: the original Riccati operations and state additions are unchanged.
// Expose the already-computed direction before addition; do not recover it by
// subtracting the rounded predicted state from the base state.
// Warm prediction for the unchanged finite nonlinear multiple-shooting problem.
// All flow Jacobians must belong to this converged solution. No nonlinear
// residual or positivity decision is replaced by this linear calculation.

function multiply(a,b,n){
 const out=new Float64Array(n*n);
 for(let i=0;i<n;i++)for(let k=0;k<n;k++){
  const v=a[i*n+k];for(let j=0;j<n;j++)out[i*n+j]+=v*b[k*n+j];
 }
 return out;
}
function matvec(a,b,n){
 const out=new Float64Array(n);
 for(let i=0;i<n;i++)for(let j=0;j<n;j++)out[i]+=a[i*n+j]*b[j];
 return out;
}
function normInf(a,n){
 let norm=0;
 for(let i=0;i<n;i++){let row=0;for(let j=0;j<n;j++)row+=Math.abs(a[i*n+j]);norm=Math.max(norm,row);}
 return norm;
}
function inverse(a,n){
 // One partial-pivoted LU factorization, followed by n right-hand sides.
 const lu=Float64Array.from(a),permutation=Int32Array.from({length:n},(_,i)=>i);
 for(let k=0;k<n;k++){
  let p=k;for(let i=k+1;i<n;i++)if(Math.abs(lu[i*n+k])>Math.abs(lu[p*n+k]))p=i;
  if(!Number.isFinite(lu[p*n+k])||!(Math.abs(lu[p*n+k])>1e-280))throw Error('Tangent predictor chart singular');
  if(p!==k){
   for(let j=0;j<n;j++){const t=lu[k*n+j];lu[k*n+j]=lu[p*n+j];lu[p*n+j]=t;}
   const t=permutation[k];permutation[k]=permutation[p];permutation[p]=t;
  }
  for(let i=k+1;i<n;i++){
   lu[i*n+k]/=lu[k*n+k];
   for(let j=k+1;j<n;j++)lu[i*n+j]-=lu[i*n+k]*lu[k*n+j];
  }
 }
 const out=new Float64Array(n*n);
 for(let column=0;column<n;column++){
  const x=Float64Array.from(permutation,i=>i===column?1:0);
  for(let i=0;i<n;i++)for(let j=0;j<i;j++)x[i]-=lu[i*n+j]*x[j];
  for(let i=n-1;i>=0;i--){for(let j=i+1;j<n;j++)x[i]-=lu[i*n+j]*x[j];x[i]/=lu[i*n+i];}
  for(let i=0;i<n;i++){if(!Number.isFinite(x[i]))throw Error('Nonfinite tangent predictor inverse');out[i*n+column]=x[i];}
 }
 return out;
}

export function createPhysicalHeightTangentPredictor(solution,farGraph,radius){
 if(solution.converged!==true)throw Error('Tangent predictor needs a converged finite response');
 const states=solution.states,M=states[0].length/2,K=2*M,depth=states.length-1,
  flows=solution.linearizedFlowJacobians;
 if(!Number.isInteger(M)||M<1||!Number.isFinite(radius)||radius<=0
   ||farGraph.length!==M||!flows||flows.length!==depth
   ||states.some(x=>x.length!==K)||flows.some(x=>x.length!==K*K))
  throw Error('Incomplete tangent predictor dimensions');
 const graphs=Array(depth+1),transports=Array(depth);
 graphs[depth]=new Float64Array(M*M);
 for(let j=0;j<M;j++)graphs[depth][j*M+j]=farGraph[j];
 let maxChartCondition=0;
 for(let n=depth-1;n>=0;n--){
  const J=flows[n],A=new Float64Array(M*M),B=new Float64Array(M*M),
   C=new Float64Array(M*M),D=new Float64Array(M*M);
  for(let i=0;i<M;i++)for(let j=0;j<M;j++){
   A[i*M+j]=J[i*K+j];B[i*M+j]=J[i*K+M+j];
   C[i*M+j]=J[(M+i)*K+j];D[i*M+j]=J[(M+i)*K+M+j];
  }
  const BG=multiply(B,graphs[n+1],M),DG=multiply(D,graphs[n+1],M);
  for(let j=0;j<M*M;j++){A[j]+=BG[j];C[j]+=DG[j];}
  transports[n]=inverse(A,M);graphs[n]=multiply(C,transports[n],M);
  maxChartCondition=Math.max(maxChartCondition,normInf(A,M)*normInf(transports[n],M));
 }
 return {
  maxChartCondition,
  predict(height){
   if(height.length!==M||height.some(x=>!Number.isFinite(x)))throw Error('Invalid target height');
   const r4=radius**4,delta=Array(depth+1),out=Array(depth+1);
   let dq=Float64Array.from(height,(h,j)=>h/r4-states[0][j]),maxRelativeCorrection=0;
   for(let n=0;n<=depth;n++){
    const dp=matvec(graphs[n],dq,M);delta[n]=new Float64Array(K);delta[n].set(dq);delta[n].set(dp,M);
    out[n]=Array.from(states[n],(v,j)=>v+delta[n][j]);
    if(out[n].some(x=>!Number.isFinite(x)))throw Error('Nonfinite tangent warm state');
    const scale=Math.max(1e-250,...states[n].map(Math.abs));
    maxRelativeCorrection=Math.max(maxRelativeCorrection,...Array.from(delta[n],v=>Math.abs(v)/scale));
    if(n<depth)dq=matvec(transports[n],dq,M);
   }
   // Preserve the target's directly computed binary Dirichlet values.
   for(let j=0;j<M;j++)out[0][j]=height[j]/r4;
   return {states:out,direction:delta,diagnostics:{kind:'full-nonlinear-shooting-tangent-warm',
    modes:M,stages:depth,maxChartCondition,maxRelativeCorrection,
    scope:'Initial guess only; original nonlinear residual and guards still decide success.'}};
  }
 };
}
