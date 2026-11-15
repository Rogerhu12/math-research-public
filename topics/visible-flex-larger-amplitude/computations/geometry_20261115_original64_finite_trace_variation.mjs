// Complete local variation of the recorded original binary64 finite root trace.
// Scientific execution belongs to the public Actions owner. No original
// state, root residual, stopping decision, Cholesky factor or RHS is replaced.
// The tangent is a floating numerical linearisation of the forced real trace;
// it is not a derivative of the discontinuous IEEE rounding map.
export const FINITE_TRACE_VARIATION_SCHEMA='original64-literal-finite-root-loop-variation-v1';

const fail=(message,detail={})=>{
 const e=new Error(message);e.finiteTraceVariation=detail;throw e;
};
function finiteArray(a,label){
 for(let k=0;k<a.length;k++)if(!Number.isFinite(a[k]))
  fail('finite-trace-direction-nonfinite',{label,index:k,value:String(a[k])});
 return a;
}
function resourceCheck(){
 const text=process.env.VISIBLE_HEIGHT_PATH_DEADLINE_MONOTONIC;
 if(text!==undefined){
  const deadline=Number(text);
  if(!Number.isFinite(deadline))fail('finite-trace-direction-invalid-deadline');
  // Both clocks are the Linux monotonic clock in the declared Actions runtime.
  if(Number(process.hrtime.bigint())/1e9>=deadline)
   fail('finite-trace-direction-resource-budget',{resource_budget:true});
 }
}

// Three independent angular inputs are P, Pt and Lv. Every operation below
// keeps the scalar expression's parentheses. Its value shadow is not used
// to change the authoritative original root or RHS.
const C=x=>[x,0,0,0];
const X=(x,k)=>{const v=C(x);v[k+1]=1;return v;};
const add=(a,b)=>[a[0]+b[0],a[1]+b[1],a[2]+b[2],a[3]+b[3]];
const neg=a=>[-a[0],-a[1],-a[2],-a[3]];
const sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>[a[0]*b[0],a[1]*b[0]+a[0]*b[1],
 a[2]*b[0]+a[0]*b[2],a[3]*b[0]+a[0]*b[3]];
const div=(a,b)=>{const v=a[0]/b[0];return [v,
 (a[1]-v*b[1])/b[0],(a[2]-v*b[2])/b[0],(a[3]-v*b[3])/b[0]];};
const sqrt=a=>{const v=Math.sqrt(a[0]),d=2*v;return [v,a[1]/d,a[2]/d,a[3]/d];};
const log1p=a=>{const d=1+a[0];return [Math.log1p(a[0]),a[1]/d,a[2]/d,a[3]/d];};
const expm1=a=>{const d=Math.exp(a[0]);return [Math.expm1(a[0]),d*a[1],d*a[2],d*a[3]];};

function angularPartials(v,g,needMatrix){
 const P=X(v.P,0),Pt=X(v.Pt,1),Lv=X(v.L,2),one=C(1),two=C(2),
  w2=C(g.w2),E=C(g.E),K=sub(Lv,Pt),
  KK=mul(K,K),EPP=mul(mul(E,P),P),
  T=add(add(mul(two,K),KK),EPP),u=mul(w2,T),
  D=sub(one,u),S=sub(one,mul(mul(w2,P),P)),sd=sqrt(D),
  plus=add(one,sd),
  fc=div(mul(u,add(two,sd)),mul(mul(mul(two,sd),plus),plus)),
  gc=div(mul(w2,add(mul(P,P),div(mul(S,T),plus))),mul(S,sd)),
  q=add(add(add(mul(C(.5),add(KK,EPP)),mul(K,Pt)),mul(T,fc)),
       mul(mul(add(one,K),Pt),gc)),
  factor=div(add(add(K,div(u,plus)),mul(mul(mul(w2,P),P),sd)),mul(S,sd));
 let bm=null;
 if(needMatrix){
  const am=add(Lv,mul(w2,Pt)),
   power=expm1(mul(C(-1.5),log1p(neg(u))));
  bm=add(am,mul(add(one,am),power));
 }
 return {q,bm,factor};
}

function dimensions(rt,state,options,tables){
 const M=options.modes,N=options.quadrature,J=M+1,K=2*M,size=K+2;
 if(!Number.isInteger(M)||M<1||!Number.isInteger(N)||state.length!==size||
    tables.cs.length!==N||tables.sn.length!==N||tables.gramCos.length!==N||
    tables.freq.length!==M||rt.L.length!==J||rt.e.rows.length!==N)
  fail('finite-trace-complete-shape-binding');
 if(rt.finiteTrace?.schema!=='original64-root-primal-tape-v1'||
    rt.finiteTrace.shape_dimension!==K||rt.finiteTrace.root_dimension!==J||
    rt.finiteTrace.primal_word_mutation!==false)
  fail('finite-trace-authoritative-primal-tape-required');
 return {M,N,J,K,size};
}

function initialDirection(trace,J,K,M){
 const dL=new Float64Array(J*K);
 if(trace.initial_guess_supplied)
  fail('finite-trace-explicit-guess-direction-not-specified');
 for(let j=0;j<M;j++)dL[(j+1)*K+M+j]=trace.target_factor;
 return dL;
}

function residualAndGramDirection(point,dL,trace,options,tables,dims,statistics){
 const {M,N,J,K}=dims,g=trace.geometry,
  dr=Float64Array.from(dL),dbeta=new Float64Array((2*M+1)*K),
  dlv=new Float64Array(K),dq=new Float64Array(K),db=new Float64Array(K),
  pCoefficient=Float64Array.from(tables.freq,m=>-m*g.r**3/(tables.sq2*g.w));
 for(let j=0;j<M;j++)dr[(j+1)*K+M+j]-=trace.target_factor;
 for(let n=0;n<N;n++){
  if((n&31)===0)resourceCheck();
  const cs=tables.cs[n],sn=tables.sn[n],gc=tables.gramCos[n],
   v=point.e.rows[n],a=angularPartials(v,g,true);
  dlv.fill(0);
  for(let i=0;i<J;i++){
   const c=cs[i],offset=i*K;
   for(let col=0;col<K;col++)dlv[col]+=dL[offset+col]*c;
  }
  for(let col=0;col<K;col++){
   const p=col<M?pCoefficient[col]*sn[col]:0,
    pt=col<M?tables.freq[col]*pCoefficient[col]*cs[col+1]:0;
   dq[col]=a.q[1]*p+a.q[2]*pt+a.q[3]*dlv[col];
   db[col]=a.bm[1]*p+a.bm[2]*pt+a.bm[3]*dlv[col];
  }
  for(let i=0;i<J;i++){
   const c=cs[i],offset=i*K;
   for(let col=0;col<K;col++)dr[offset+col]+=dq[col]*c/N;
  }
  for(let k=0;k<=2*M;k++){
   const c=gc[k],offset=k*K;
   for(let col=0;col<K;col++)dbeta[offset+col]+=db[col]*c/N;
  }
 }
 return {dr,dbeta};
}

// Explicit differentiation of the ACTUAL stored lower Cholesky factor and
// its two ACTUAL substitution vectors. No C inverse shortcut and no dropped
// factor/forward/backsolve residual derivative is asserted.
function differentiatedOriginalSolve(point,dr,dbeta,tables,dims){
 const {J,K}=dims,tape=point.solve;
 if(!tape||tape.factor.length!==J*J||tape.forward.length!==J||
    tape.solution.length!==J)
  fail('finite-trace-original-factor-and-substitution-values-required');
 const R=tape.factor,z=tape.forward,s=tape.solution,
  dR=new Float64Array(J*J*K),dz=new Float64Array(J*K),ds=new Float64Array(J*K),
  dv=new Float64Array(K);
 for(let i=0;i<J;i++){
  resourceCheck();
  for(let j=0;j<=i;j++){
   if(j===0){
    const factor=i===0?1:tables.sq2,offset=i*K;
    for(let col=0;col<K;col++)dv[col]=factor*dbeta[offset+col];
   }else{
    const left=(i-j)*K,right=(i+j)*K;
    for(let col=0;col<K;col++)dv[col]=dbeta[left+col]+dbeta[right+col];
   }
   for(let k=0;k<j;k++){
    const aik=R[i*J+k],ajk=R[j*J+k],ik=(i*J+k)*K,jk=(j*J+k)*K;
    for(let col=0;col<K;col++)dv[col]-=dR[ik+col]*ajk+aik*dR[jk+col];
   }
   const ij=(i*J+j)*K;
   if(i===j){
    const denominator=2*R[i*J+i];
    for(let col=0;col<K;col++)dR[ij+col]=dv[col]/denominator;
   }else{
    const jj=(j*J+j)*K,diagonal=R[j*J+j],actual=R[i*J+j];
    for(let col=0;col<K;col++)dR[ij+col]=(dv[col]-actual*dR[jj+col])/diagonal;
   }
  }
 }
 for(let i=0;i<J;i++){
  resourceCheck();
  const offset=i*K,diagonal=R[i*J+i],ii=(i*J+i)*K;
  for(let col=0;col<K;col++)dv[col]=dr[offset+col];
  for(let j=0;j<i;j++){
   const r=R[i*J+j],ij=(i*J+j)*K,jo=j*K;
   for(let col=0;col<K;col++)dv[col]-=dR[ij+col]*z[j]+r*dz[jo+col];
  }
  for(let col=0;col<K;col++)dz[offset+col]=(dv[col]-z[i]*dR[ii+col])/diagonal;
 }
 for(let i=J-1;i>=0;i--){
  resourceCheck();
  const offset=i*K,diagonal=R[i*J+i],ii=(i*J+i)*K;
  for(let col=0;col<K;col++)dv[col]=dz[offset+col];
  for(let j=i+1;j<J;j++){
   const r=R[j*J+i],ji=(j*J+i)*K,jo=j*K;
   for(let col=0;col<K;col++)dv[col]-=dR[ji+col]*s[j]+r*ds[jo+col];
  }
  for(let col=0;col<K;col++)ds[offset+col]=(dv[col]-s[i]*dR[ii+col])/diagonal;
 }
 return finiteArray(ds,'original-solve-direction');
}

function finiteRootDirection(rt,state,options,tables,dims,statistics){
 const {M,J,K}=dims,trace=rt.finiteTrace;
 let dL=initialDirection(trace,J,K,M);
 if(trace.accepted_updates.length!==trace.iterations||
    !['normal-stop','original-roundoff-fallback'].includes(trace.return_reason))
  fail('finite-trace-successful-return-branch-required');
 statistics.root_returns++;
 statistics.zero_update_returns+=trace.accepted_updates.length===0?1:0;
 statistics.normal_returns+=trace.return_reason==='normal-stop'?1:0;
 statistics.fallback_returns+=trace.return_reason==='original-roundoff-fallback'?1:0;
 statistics.original_root_evaluations+=trace.root_evaluations;
 statistics.original_line_trials+=trace.line_trials;
 statistics.return_iteration_histogram[trace.iterations]++;
 for(const point of trace.accepted_updates){
  resourceCheck();
  if(!(Number.isInteger(point.backtrack)&&point.backtrack>=0&&point.backtrack<20)||
     point.alpha!==2**(-point.backtrack))
   fail('finite-trace-original-selected-backtrack-required');
  const formed=residualAndGramDirection(point,dL,trace,options,tables,dims,statistics),
   ds=differentiatedOriginalSolve(point,formed.dr,formed.dbeta,tables,dims),
   next=new Float64Array(dL.length);
  for(let j=0;j<next.length;j++)next[j]=dL[j]-point.alpha*ds[j];
  dL=finiteArray(next,'finite-root-update-direction');
  statistics.differentiated_accepted_updates++;
 }
 return dL;
}

function splitRhsDirection(rt,state,dL,options,tables,dims,statistics){
 const {M,N,J,K,size}=dims,g=rt.g,frequency=tables.freq,
  sigma=g.drdx/g.r,
  pref=(options.orientation??1)*tables.sq2*g.r**3*g.drdx*g.w2/(tables.sq12*options.mu),
  pCoefficient=Float64Array.from(frequency,m=>-m*g.r**3/(tables.sq2*g.w)),
  dFlux=new Float64Array(M*K),dlv=new Float64Array(K),duv=new Float64Array(K),
  df=new Float64Array(K),result=new Float64Array(size*K);
 for(let n=0;n<N;n++){
  if((n&31)===0)resourceCheck();
  const cs=tables.cs[n],sn=tables.sn[n],v=rt.e.rows[n],a=angularPartials(v,g,false);
  for(let col=0;col<K;col++){dlv[col]=dL[col];duv[col]=0;}
  for(let j=0;j<M;j++){
   const c=cs[j+1],sine=sn[j],m=frequency[j],offset=(j+1)*K;
   for(let col=0;col<K;col++){
    dlv[col]+=dL[offset+col]*c;
    duv[col]+=(-m*dL[offset+col]+(col===j?(m*m-1)*pCoefficient[j]:0))*sine;
   }
  }
  for(let col=0;col<K;col++){
   const p=col<M?pCoefficient[col]*sn[col]:0,
    pt=col<M?frequency[col]*pCoefficient[col]*cs[col+1]:0,
    dFactor=a.factor[1]*p+a.factor[2]*pt+a.factor[3]*dlv[col];
   df[col]=duv[col]*a.factor[0]+v.U*dFactor;
  }
  for(let j=0;j<M;j++){
   const sine=sn[j],offset=j*K;
   for(let col=0;col<K;col++)dFlux[offset+col]+=df[col]*sine/N;
  }
 }
 for(let j=0;j<M;j++)for(let col=0;col<K;col++){
  const m=frequency[j],L1=dL[(j+1)*K+col],
   p1=col===j?pCoefficient[j]:0,
   linear=-m*L1+(m*m-1)*p1;
  result[j*K+col]=sigma*((col===j?m*m-4:0)+tables.sq2*g.w*L1/g.r**3);
  result[(M+j)*K+col]=(col===M+j?4*sigma:0)+pref*m*(linear+dFlux[j*K+col]);
 }
 for(let col=0;col<K;col++)result[K*K+col]=g.drdx*g.w*dL[col];
 // The second mean component has g.r_x*g.w as its primal RHS and zero shape
 // derivative. It is retained as a complete row, never removed.
 return finiteArray(result,'complete-226-by-224-local-field-direction');
}

export function newFiniteTraceStatistics(){
 return {schema:FINITE_TRACE_VARIATION_SCHEMA,root_returns:0,zero_update_returns:0,
  normal_returns:0,fallback_returns:0,original_root_evaluations:0,original_line_trials:0,
  differentiated_accepted_updates:0,
  // Successful normal/fallback returns have 0..29 accepted updates. The
  // 30th accepted update exits the original loop with iteration-limit failure.
  return_iteration_histogram:Array(30).fill(0),
  complete_local_jacobians:0,
  no_rounding_map_derivative_claim:true,no_implicit_root_equation_substitution:true,
  original_primal_state_or_RHS_modified:false,
  numerical_tangent_roundoff_bound_paid:false,
  forced_trace_branch_neighbourhood_proved:false};
}

export function completeFiniteRootTraceJacobian(rt,state,options,tables,statistics){
 resourceCheck();
 const dims=dimensions(rt,state,options,tables),
  dL=finiteRootDirection(rt,state,options,tables,dims,statistics),
  result=splitRhsDirection(rt,state,dL,options,tables,dims,statistics);
 statistics.complete_local_jacobians++;
 return result;
}
