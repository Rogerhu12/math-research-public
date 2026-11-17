"""Create an explicitly experimental finite momentum chart with pivoted LU.

The equations, D/S domain and nonlinear residual tests are unchanged. The
pointwise A>floor and positive-definite-matrix chart restrictions are replaced
by full nonsingular finite-Gram solves. No infinite-mode conclusion follows.
The archived source is never overwritten. Warm root selection is explicit.
"""
import argparse,hashlib,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
s=a.source.read_text();source_sha=hashlib.sha256(a.source.read_bytes()).hexdigest()
assert source_sha=='182847f2ff1b27ff211364729c2969e4b417973efe0bba5977b2ef26e500528c', 'Unexpected archived momentum source'
assert a.out.resolve()!=a.source.resolve()
old='if(!(D>floor&&S>floor&&A>floor))throw new Error("momentum branch D/S/A rejected");'
new='if(!(D>floor&&S>floor))throw new Error("experimental full-Gram chart D/S rejected");'
assert s.count(old)==1;s=s.replace(old,new)
start=s.index(' function solveSPD(B,b){');end=s.index(' function root(state,profile,x,guess){',start)
lu=r''' // Explicit finite nonsingular chart; no positive-Gram assertion.
 let lastRootGuess=null;
 let solveDiagnostics={calls:0,minRelativePivot:Infinity,maxRelativeResidual:0};
 function solveSPD(B,b){
  const A=Float64Array.from(B),rhs=Float64Array.from(b),out=new Float64Array(J);
  let norm=0;for(let i=0;i<J;i++){let row=0;for(let j=0;j<J;j++)row+=Math.abs(B[i*J+j]);norm=Math.max(norm,row);}
  if(!(norm>0&&Number.isFinite(norm)))throw Error('invalid full Gram matrix');
  let minPivot=Infinity;
  for(let k=0;k<J;k++){
   let pivot=k;for(let i=k+1;i<J;i++)if(Math.abs(A[i*J+k])>Math.abs(A[pivot*J+k]))pivot=i;
   const pv=Math.abs(A[pivot*J+k]);minPivot=Math.min(minPivot,pv/norm);
   if(!(pv>64*Number.EPSILON*norm))throw Error('finite Gram pivot unresolved');
   if(pivot!==k){for(let j=0;j<J;j++){const t=A[k*J+j];A[k*J+j]=A[pivot*J+j];A[pivot*J+j]=t;}const t=rhs[k];rhs[k]=rhs[pivot];rhs[pivot]=t;}
   for(let i=k+1;i<J;i++){const factor=A[i*J+k]/A[k*J+k];A[i*J+k]=0;for(let j=k+1;j<J;j++)A[i*J+j]-=factor*A[k*J+j];rhs[i]-=factor*rhs[k];}
  }
  for(let i=J-1;i>=0;i--){let v=rhs[i];for(let j=i+1;j<J;j++)v-=A[i*J+j]*out[j];out[i]=v/A[i*J+i];}
  let err=0,bnorm=0,xnorm=0;for(let i=0;i<J;i++){let v=-b[i];for(let j=0;j<J;j++)v+=B[i*J+j]*out[j];err=Math.max(err,Math.abs(v));bnorm=Math.max(bnorm,Math.abs(b[i]));xnorm=Math.max(xnorm,Math.abs(out[i]));}
  const relative=err/Math.max(Number.MIN_VALUE,bnorm+norm*xnorm);
  if(!(relative<=2e-12&&Array.from(out).every(Number.isFinite)))throw Error('finite Gram linear solve residual');
  solveDiagnostics.calls++;solveDiagnostics.minRelativePivot=Math.min(solveDiagnostics.minRelativePivot,minPivot);solveDiagnostics.maxRelativeResidual=Math.max(solveDiagnostics.maxRelativeResidual,relative);
  return out;
 }
'''
s=s[:start]+lu+s[end:]
old='let L=guess?Float64Array.from(guess):Float64Array.from(target);'
new='let L=Float64Array.from(guess??lastRootGuess??target);'
assert s.count(old)==1;s=s.replace(old,new)
old='if(err<=8e-14*scale)return last;';new='if(err<=8e-14*scale){lastRootGuess=Float64Array.from(L);return last;}'
assert s.count(old)==1;s=s.replace(old,new)
old='if(err<=5e-12*scale)return {...last,roundoffFallback:true};';new='if(err<=5e-12*scale){lastRootGuess=Float64Array.from(L);return {...last,roundoffFallback:true};}'
assert s.count(old)==1;s=s.replace(old,new)
old='return {state,L,meanPhysical:g.w*L[0],normalizedMeanResidual:e.moments[0]};';new='lastRootGuess=Float64Array.from(L);return {state,L,meanPhysical:g.w*L[0],normalizedMeanResidual:e.moments[0]};'
assert s.count(old)==1;s=s.replace(old,new)
old='return {M,N,size,mu,orientation,root,evaluateL,geometry,initializeFromRaw,toRaw,rhs,rhsWithJacobian,rk4,flowRawCell,flowStateWithJacobian};'
new='return {M,N,size,mu,orientation,root,evaluateL,geometry,initializeFromRaw,toRaw,rhs,rhsWithJacobian,rk4,flowRawCell,flowStateWithJacobian,seedRootGuess:L=>{lastRootGuess=Float64Array.from(L);},solveDiagnostics};'
assert s.count(old)==1;s=s.replace(old,new)
s='// HELD10 EXPERIMENT: finite full-Gram chart; not the original positive-A solver.\n'+s
a.out.write_text(s)
print(json.dumps({'source_sha256':source_sha,'output_sha256':hashlib.sha256(a.out.read_bytes()).hexdigest(),'changes':['D/S only in evaluateL; A recorded','pivoted LU with pivot and residual checks','explicit warm root guess'],'unchanged':'all equations, Fourier projections, D/S bounds, nonlinear root residual tolerance'}))
