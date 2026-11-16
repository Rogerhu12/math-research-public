// R466: numerical contraction of the complete recorded-factor nominal system.
// This module never evaluates or changes the original primal root. R465 proves
// an exact-real identity for its stated local constant-defect model. The new
// binary64 order is NOT bitwise equivalent to the old differentiated loops;
// no numerical error bound or derivative of IEEE branch/rounding decisions is
// supplied. All 225 literal Gram slots and every direction are retained.
export const RECORDED_FACTOR_CONTRACTION_SCHEMA=
 'original64-recorded-factor-complete-column-contraction-v1';

class NumericalFallback extends Error {
 constructor(reason,detail={}){super(reason);this.reason=reason;this.detail=detail;}
}
const fallback=(reason,detail={})=>{throw new NumericalFallback(reason,detail);};
const finite=(x,phase,index)=>{
 if(!Number.isFinite(x))fallback('contracted-arithmetic-nonfinite',{phase,index});
 return x;
};
const wordBuffer=new ArrayBuffer(8),wordView=new DataView(wordBuffer);
const FRACTION_MASK=(1n<<52n)-1n;

// Decode a finite binary64 word as an exact signed integer times a power of 2.
// This is data representation, not a second scientific root or a shadow gate.
function dyadic(x){
 if(!Number.isFinite(x))fallback('recorded-solve-literal-nonfinite');
 wordView.setFloat64(0,x,true);
 const bits=wordView.getBigUint64(0,true),negative=(bits>>63n)!==0n,
  exponent=Number((bits>>52n)&2047n),fraction=bits&FRACTION_MASK;
 let integer=exponent===0?fraction:(1n<<52n)+fraction;
 if(negative)integer=-integer;
 return {integer,exponent:exponent===0?-1074:exponent-1023-52};
}
function addExact(acc,integer,exponent){
 if(integer===0n)return;
 if(acc.integer===0n){acc.integer=integer;acc.exponent=exponent;return;}
 if(exponent<acc.exponent){
  acc.integer=(acc.integer<<BigInt(acc.exponent-exponent))+integer;
  acc.exponent=exponent;
 }else acc.integer+=integer<<BigInt(exponent-acc.exponent);
}

// One explicit round-to-nearest, ties-to-even projection. The final integer
// has at most 53 significant bits (including a carry). Its multiplication by
// 2**quantum is exact whenever the finite result is representable. Subnormal
// rounding is directly to the binary64 quantum 2**-1074, with no double round.
function projectDyadic(acc){
 if(acc.integer===0n)return {value:0,exact:true,lost:false,overflow:false};
 const negative=acc.integer<0n,
  magnitude=negative?-acc.integer:acc.integer,
  bitLength=magnitude.toString(2).length,
  top=acc.exponent+bitLength-1,quantum=Math.max(top-52,-1074),
  shift=quantum-acc.exponent;
 let rounded,discarded=false;
 if(shift>0){
  const distance=BigInt(shift),truncated=magnitude>>distance,
   remainder=magnitude-(truncated<<distance),half=1n<<(distance-1n);
  rounded=truncated;
  discarded=remainder!==0n;
  if(remainder>half||(remainder===half&&(truncated&1n)!==0n))rounded++;
 }else rounded=magnitude<<BigInt(-shift);
 let value=Number(rounded)*2**quantum;
 if(negative)value=-value;
 return {value,exact:!discarded&&Number.isFinite(value),
  lost:rounded===0n,overflow:!Number.isFinite(value)};
}

// Form b = R^T*s-z from the actual recorded words using exact dyadic sums.
// The mathematical b is not silently set to zero by an ordinary dot product.
// All J entries are accounted before a representability fallback is selected.
function backsolveDefect(R,z,s,J,resourceCheck,stats){
 const sd=Array.from(s,dyadic),zd=Array.from(z,dyadic),b=new Float64Array(J);
 let firstFallback=null,allExactZero=true;
 for(let i=0;i<J;i++){
  resourceCheck();
  const acc={integer:0n,exponent:0};
  for(let j=i;j<J;j++){
   const r=dyadic(R[j*J+i]);
   addExact(acc,r.integer*sd[j].integer,r.exponent+sd[j].exponent);
  }
  addExact(acc,-zd[i].integer,zd[i].exponent);
  const nonzero=acc.integer!==0n,projection=projectDyadic(acc);
  stats.exact_backsolve_defect_components++;
  if(nonzero){stats.exact_nonzero_backsolve_defect_components++;allExactZero=false;}
  if(!projection.exact)stats.backsolve_defect_projection_changed_components++;
  if(projection.lost){
   stats.nonzero_backsolve_defect_projection_lost_components++;
   if(firstFallback===null)firstFallback={reason:'nonzero-backsolve-defect-underflow',index:i};
  }
  if(projection.overflow){
   stats.backsolve_defect_projection_overflow_components++;
   if(firstFallback===null)firstFallback={reason:'backsolve-defect-projection-overflow',index:i};
  }
  b[i]=projection.value;
 }
 if(firstFallback!==null)fallback(firstFallback.reason,{index:firstFallback.index});
 return {b,allExactZero};
}

function inverseLower(R,J,resourceCheck){
 const A=new Float64Array(J*J);
 for(let i=0;i<J;i++){
  resourceCheck();
  const diagonal=R[i*J+i];
  if(!(diagonal>0)&&Number.isFinite(diagonal))
   fallback('recorded-factor-positive-diagonal-unavailable',{index:i});
  A[i*J+i]=finite(1/diagonal,'inverse-lower-diagonal',i);
  for(let j=0;j<i;j++){
   let total=0;
   for(let k=j;k<i;k++)total+=R[i*J+k]*A[k*J+j];
   A[i*J+j]=finite(-total/diagonal,'inverse-lower',i*J+j);
  }
 }
 return A;
}

// S_s is the exact structural action dC*s in the literal beta coordinates.
// The scalar sq2 is the stored original table word. It is not recomputed.
function structuralAction(s,J,B,sq2,resourceCheck){
 const S=new Float64Array(J*B),M=J-1;
 S[0]=s[0];
 for(let j=1;j<=M;j++)S[j]+=sq2*s[j];
 for(let i=1;i<=M;i++){
  resourceCheck();
  const row=i*B;
  S[row+i]+=sq2*s[0];
  for(let j=1;j<=M;j++){
   S[row+Math.abs(i-j)]+=s[j];
   S[row+i+j]+=s[j];
  }
 }
 for(let i=0;i<S.length;i++)finite(S[i],'structured-Gram-action',i);
 return S;
}

// Q_ik = a_i^T T_k v_i, v_i=sum_{j<i} b_j a_j + (b_i/2)*a_i.
// Enumerating every ordered (r,s) preserves the full literal 225-slot Gram;
// the half diagonal belongs to Phi, not an extra factor in the Gram matrix.
function contractedBacksolveAction(A,b,J,B,sq2,resourceCheck){
 const Q=new Float64Array(J*B),prefix=new Float64Array(J),v=new Float64Array(J);
 for(let i=0;i<J;i++){
  resourceCheck();
  const ar=i*J,qr=i*B,half=.5*b[i];
  for(let r=0;r<=i;r++)v[r]=prefix[r]+half*A[ar+r];
  const a0=A[ar],v0=v[0];
  Q[qr]+=a0*v0;
  for(let j=1;j<=i;j++)
   Q[qr+j]+=sq2*(a0*v[j]+A[ar+j]*v0);
  for(let r=1;r<=i;r++)for(let s=1;s<=i;s++){
   const term=A[ar+r]*v[s];
   Q[qr+Math.abs(r-s)]+=term;
   Q[qr+r+s]+=term;
  }
  for(let k=0;k<B;k++)finite(Q[qr+k],'backsolve-defect-contraction',qr+k);
  for(let r=0;r<=i;r++)
   prefix[r]=finite(prefix[r]+b[i]*A[ar+r],'backsolve-defect-prefix',r);
 }
 return Q;
}

function assemble(point,tables,dims,resourceCheck,stats){
 const {J,K}=dims,B=2*(J-1)+1,tape=point.solve,
  R=tape.factor,z=tape.forward,s=tape.solution;
 // Source/tape shape checks are caller responsibilities and are never caught
 // as a numerical fallback. Primal arrays here are read-only.
 stats.preassemblies_started++;
 const defect=backsolveDefect(R,z,s,J,resourceCheck,stats),
  gamma=structuralAction(s,J,B,tables.sq2,resourceCheck);
 if(defect.allExactZero){
  stats.exact_zero_backsolve_defect_updates++;
 }else{
  const A=inverseLower(R,J,resourceCheck),
   Q=contractedBacksolveAction(A,defect.b,J,B,tables.sq2,resourceCheck);
  for(let i=0;i<J;i++){
   resourceCheck();
   const out=i*B;
   for(let j=0;j<=i;j++){
    const r=R[i*J+j],source=j*B;
    for(let k=0;k<B;k++)gamma[out+k]-=r*Q[source+k];
   }
   for(let k=0;k<B;k++)finite(gamma[out+k],'Gamma-assembly',out+k);
  }
 }
 stats.preassemblies_completed++;
 return {R,gamma,J,K,B};
}

function applyAllColumns(prepared,dr,dbeta,resourceCheck){
 const {R,gamma,J,K,B}=prepared,right=Float64Array.from(dr),
  forward=new Float64Array(J*K),solution=new Float64Array(J*K);
 for(let i=0;i<J;i++){
  resourceCheck();
  const row=i*K,gr=i*B;
  for(let k=0;k<B;k++){
   const coefficient=gamma[gr+k],br=k*K;
   for(let col=0;col<K;col++)right[row+col]-=coefficient*dbeta[br+col];
  }
  for(let col=0;col<K;col++)finite(right[row+col],'complete-column-right-hand-side',row+col);
 }
 for(let i=0;i<J;i++){
  resourceCheck();
  const row=i*K,diagonal=R[i*J+i];
  for(let col=0;col<K;col++){
   let value=right[row+col];
   for(let j=0;j<i;j++)value-=R[i*J+j]*forward[j*K+col];
   forward[row+col]=finite(value/diagonal,'complete-column-forward-solve',row+col);
  }
 }
 for(let i=J-1;i>=0;i--){
  resourceCheck();
  const row=i*K,diagonal=R[i*J+i];
  for(let col=0;col<K;col++){
   let value=forward[row+col];
   for(let j=i+1;j<J;j++)value-=R[j*J+i]*solution[j*K+col];
   solution[row+col]=finite(value/diagonal,'complete-column-backsolve',row+col);
  }
 }
 return solution;
}

export function newRecordedFactorContractionStatistics(){
 return {schema:RECORDED_FACTOR_CONTRACTION_SCHEMA,
  calls_started:0,calls_completed:0,preassemblies_started:0,preassemblies_completed:0,
  contracted_updates_completed:0,explicit_original_fallbacks_started:0,
  explicit_original_fallbacks_completed:0,complete_direction_columns_returned:0,
  exact_backsolve_defect_components:0,exact_nonzero_backsolve_defect_components:0,
  backsolve_defect_projection_changed_components:0,
  nonzero_backsolve_defect_projection_lost_components:0,
  backsolve_defect_projection_overflow_components:0,exact_zero_backsolve_defect_updates:0,
  fallback_reason_counts:{},last_started_update:null,last_numerical_fallback:null,
  all_literal_Gram_moments_retained:true,actual_recorded_factor_used_for_both_solves:true,
  exact_backsolve_defect_formed_before_explicit_binary64_projection:true,
  local_model:'R465-recorded-constant-defect-nominal-coefficient-system',
  general_variable_defect_derivatives_silently_discarded:false,
  binary64_word_equivalence_to_explicit_factor_loops_claimed:false,
  contraction_roundoff_error_bound_paid:false,original_noJ_primal_modified:false,
  zero_update_root_path_modified:false,numerical_fallback_is_original_195_factor_loop:true};
}

export function contractedRecordedSolve(point,dr,dbeta,tables,dims,
 resourceCheck,originalSolve,stats){
 const {J,K}=dims,B=2*(J-1)+1;
 // A mismatched trace is an existing caller/source contract error, not a
 // reason to invent a numerical replacement or to continue with fewer rows.
 if(dr.length!==J*K||dbeta.length!==B*K)
  throw new Error('contracted-finite-trace-complete-direction-shape-required');
 stats.calls_started++;
 stats.last_started_update={original_iteration:point.iteration,
  original_backtrack:point.backtrack,root_dimension:J,shape_columns:K,Gram_moments:B};
 let solution;
 try{
  resourceCheck();
  solution=applyAllColumns(assemble(point,tables,dims,resourceCheck,stats),
   dr,dbeta,resourceCheck);
  stats.contracted_updates_completed++;
 }catch(error){
  if(!(error instanceof NumericalFallback))throw error;
  stats.explicit_original_fallbacks_started++;
  stats.fallback_reason_counts[error.reason]=(stats.fallback_reason_counts[error.reason]??0)+1;
  stats.last_numerical_fallback={reason:error.reason,detail:error.detail,
   original_iteration:point.iteration,original_backtrack:point.backtrack,
   returned_complete_original_direction:false};
  // No resource stop, binding failure, original root branch, or acceptance
  // decision is caught here. The original explicit solve can itself fail;
  // that actual failure propagates without a second fallback.
  solution=originalSolve(point,dr,dbeta,tables,dims);
  stats.explicit_original_fallbacks_completed++;
  stats.last_numerical_fallback.returned_complete_original_direction=true;
 }
 stats.complete_direction_columns_returned+=K;
 stats.calls_completed++;
 return solution;
}
