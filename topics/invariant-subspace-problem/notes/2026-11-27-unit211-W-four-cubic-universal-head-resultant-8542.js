return (function(){
"use strict";
const began=Date.now(),n=9;
const key=v=>v.join(","),zero=()=>new Map(),one=()=>new Map([[key(Array(n).fill(0)),1n]]);
function v(j){const a=Array(n).fill(0);a[j]=1;return new Map([[key(a),1n]])}
function add(p,q){const r=new Map(p);for(const[k,c]of q){const z=(r.get(k)||0n)+c;if(z)r.set(k,z);else r.delete(k)}return r}
function neg(p){return new Map([...p].map(([k,c])=>[k,-c]))}
function sub(p,q){return add(p,neg(q))}
function mul(p,q){const r=zero();for(const[ka,a]of p)for(const[kb,b]of q){const x=ka.split(",").map(Number),y=kb.split(",").map(Number);const k=key(x.map((c,i)=>c+y[i]));const z=(r.get(k)||0n)+a*b;if(z)r.set(k,z);else r.delete(k)}return r}
function det(A){if(!A.length)return one();if(A.length===1)return A[0][0];let r=zero();for(let j=0;j<A.length;j++){const minor=A.slice(1).map(row=>row.filter((_,k)=>k!==j));const t=mul(A[0][j],det(minor));r=add(r,j%2?neg(t):t)}return r}
const[a,b,c,d,e,f,g,h,i]=Array.from({length:n},(_,j)=>v(j)),z=zero;
const M=[
[a,b,c,z()],
[z(),a,b,c],
[g,sub(h,d),sub(i,e),neg(f)],
[mul(a,d),add(add(mul(a,e),mul(b,d)),mul(c,g)),add(add(mul(a,f),mul(b,e)),mul(c,h)),add(mul(b,f),mul(c,i))]
];
const Syl=[
[a,b,c,z(),z()],
[z(),a,b,c,z()],
[z(),z(),a,b,c],
[g,sub(h,d),sub(i,e),neg(f),z()],
[z(),g,sub(h,d),sub(i,e),neg(f)]
];
const D=det(M),R=det(Syl),diff=sub(D,R);
if(diff.size)throw Error("universal determinant identity failed");
const canonical=[...D].sort(([a],[b])=>a.localeCompare(b)).map(([m,c])=>[m,c.toString()]);
return {stage:"W_four_cubic_universal_head_resultant_identity",
coefficientVariables:["a","b","c","d","e","f","g","h","i"],
identity:"det(binary cubic head)=Res(aF^2+bFlambda+clambda^2, F*(gF^2+hFlambda+ilambda^2)-lambda*(dF^2+eFlambda+flambda^2))",
exactIntegerPolynomialComparison:true,nonzeroTermCount:D.size,
totalCoefficientDegree:Math.max(...[...D.keys()].map(k=>k.split(",").reduce((s,x)=>s+Number(x),0))),
noCoefficientInverted:true,noGenericityAssumption:true,
canonicalPolynomial:canonical,elapsedMilliseconds:Date.now()-began,
OSExitCode:"not applicable: functions.exec V8",RSS:"not exposed",
finitePointExclusionClaim:false};
})();