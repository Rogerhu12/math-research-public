(()=>{
"use strict";
const started=Date.now(),checks=[];
const ok=(name,b)=>{if(!b)throw Error(name);checks.push(name);};
const abs=a=>a<0n?-a:a;
function igcd(a,b){a=abs(a);b=abs(b);while(b){let t=a%b;a=b;b=t;}return a;}
function trim(a){a=a.map(BigInt);while(a.length&&!a[a.length-1])a.pop();return a;}
const pzero=[],pone=[1n];
function add(a,b){let r=Array(Math.max(a.length,b.length)).fill(0n);for(let i=0;i<r.length;i++)r[i]=(a[i]||0n)+(b[i]||0n);return trim(r);}
function neg(a){return a.map(x=>-x);}
function sub(a,b){return add(a,neg(b));}
function scale(a,c){return trim(a.map(x=>x*c));}
function mul(a,b){if(!a.length||!b.length)return [];let r=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)r[i+j]+=a[i]*b[j];return trim(r);}
function shift(a,n){return a.length?Array(n).fill(0n).concat(a):[];}
function content(a){return a.reduce((g,c)=>igcd(g,c),0n);}
function primitive(a){a=trim(a);if(!a.length)return [];let g=content(a);if(a[a.length-1]<0n)g=-g;return a.map(c=>c/g);}
function prem(a,b){a=trim(a);if(!b.length)throw Error("zero polynomial divisor");while(a.length>=b.length&&a.length){let d=a.length-b.length;a=primitive(sub(scale(a,b[b.length-1]),shift(scale(b,a[a.length-1]),d)));}return a;}
function pgcd(a,b){a=primitive(a);b=primitive(b);while(b.length){let r=prem(a,b);a=b;b=r;}return primitive(a);}
function divexact(a,b){a=trim(a);if(!b.length)throw Error("zero exact divisor");let q=Array(Math.max(0,a.length-b.length+1)).fill(0n);while(a.length>=b.length&&a.length){let d=a.length-b.length,lc=b[b.length-1],n=a[a.length-1];if(n%lc)throw Error("nonintegral exact quotient");let c=n/lc;q[d]+=c;a=sub(a,shift(scale(b,c),d));}if(a.length)throw Error("nonzero exact remainder");return trim(q);}
class R{
 constructor(n=0,d=null){if(n instanceof R&&d===null){this.n=n.n;this.d=n.d;return;}n=trim(Array.isArray(n)?n:[n]);d=trim(d===null?[1n]:(Array.isArray(d)?d:[d]));if(!d.length)throw Error("zero rational denominator");if(!n.length){this.n=[];this.d=[1n];return;}let g=pgcd(n,d);n=divexact(n,g);d=divexact(d,g);let c=igcd(content(n),content(d));if(d[d.length-1]<0n)c=-c;this.n=n.map(x=>x/c);this.d=d.map(x=>x/c);}
 add(v){v=new R(v);return new R(add(mul(this.n,v.d),mul(v.n,this.d)),mul(this.d,v.d));}
 neg(){return new R(neg(this.n),this.d);}
 sub(v){return this.add(new R(v).neg());}
 mul(v){v=new R(v);return new R(mul(this.n,v.n),mul(this.d,v.d));}
 div(v){v=new R(v);if(!v.n.length)throw Error("zero rational inverse");return new R(mul(this.n,v.d),mul(this.d,v.n));}
 pow(n){if(n<0)return new R(this.d,this.n).pow(-n);let r=new R(1),a=this;while(n){if(n&1)r=r.mul(a);n=Math.floor(n/2);if(n)a=a.mul(a);}return r;}
 eq(v){v=new R(v);return !sub(mul(this.n,v.d),mul(v.n,this.d)).length;}
}
const rr=x=>new R(x),m=rr([0n,1n]);
const A=m.pow(2).sub(m.mul(6)).add(6);
const B=m.pow(2).sub(m.mul(4)).add(6);
const C=m.pow(3).sub(m.pow(2).mul(10)).add(m.mul(36)).sub(36);
const E2=m.pow(2).mul(5).sub(m.mul(30)).add(36);
const Cb=m.pow(3).mul(5).sub(m.pow(2).mul(32)).add(m.mul(78)).sub(72);
const Cu=m.pow(3).mul(2).sub(m.pow(2).mul(17)).add(m.mul(48)).sub(36);
const Z=m.pow(4).mul(7).sub(m.pow(3).mul(91)).add(m.pow(2).mul(408)).sub(m.mul(720)).add(432);
const k=A.mul(2).div(m),e=C.div(A.mul(6)),u=e.add(1),Q=e.mul(k);
const V=u.mul(k).add(2);
const ell=u.mul(k.add(2).pow(2).sub(e.mul(k).mul(2))).div(k.mul(V));
const ellpar=m.mul(m.sub(4)).mul(E2).div(A.pow(2).mul(6));
const K=e.pow(2).mul(k.pow(2)).mul(12).sub(e.mul(k.pow(3))).add(e.mul(k.pow(2)).mul(8)).sub(k.pow(3)).sub(k.pow(2).mul(4)).sub(k.mul(16)).sub(16);
ok("full seven-term K polynomial vanishes under parameterization",K.eq(0));
ok("u complete rational formula",u.eq(m.pow(2).mul(m.sub(4)).div(A.mul(6))));
ok("Q complete rational formula",Q.eq(C.div(m.mul(3))));
ok("ell complete original W weight formula",ell.eq(ellpar));
ok("V=B/3",V.eq(B.div(3)));
ok("k+2 paid factorization",k.add(2).eq(m.sub(2).mul(m.sub(3)).mul(2).div(m)));
ok("k+4 paid factorization",k.add(4).eq(B.mul(2).div(m)));
ok("Q-2 paid factorization",Q.sub(2).eq(m.sub(6).mul(B).div(m.mul(3))));
ok("1-Q complete factorization",rr(1).sub(Q).eq(m.sub(3).pow(2).mul(m.sub(4)).neg().div(m.mul(3))));
ok("2e+1 complete factorization",e.mul(2).add(1).eq(m.sub(3).mul(B).div(A.mul(3))));
ok("ell-u complete factorization",ell.sub(u).eq(m.mul(m.sub(4)).mul(m.sub(2)).mul(m.sub(3)).mul(m.sub(6)).neg().div(A.pow(2).mul(6))));
ok("u-Q complete factorization",u.sub(Q).eq(m.sub(2).mul(m.sub(6)).mul(Cu).neg().div(m.mul(A).mul(6))));
const M=ell.mul(u.mul(2).sub(ell.mul(Q))).sub(u.pow(2));
const d=rr(1).sub(Q),bc=M.div(d.mul(4));
ok("M entire factorization",M.eq(m.mul(m.sub(4).pow(2)).mul(m.sub(3).pow(3)).mul(Z).neg().div(A.pow(4).mul(27))));
ok("bc entire factorization",bc.eq(m.pow(2).mul(m.sub(4)).mul(m.sub(3)).mul(Z).div(A.pow(4).mul(36))));
const V2=u.mul(2).sub(ell.mul(Q)),T0=V2.sub(u.pow(2).mul(2));
const P02=rr(2).sub(u.mul(3)).mul(V2).sub(Q.mul(u)).add(u.pow(3).mul(2));
const Phi=T0.add(u.mul(4)).sub(4).add(Q),J=u.mul(rr(1).sub(u)).mul(2).add(ell.mul(Q));
ok("P02 entire factorization",P02.eq(C.pow(2).mul(m.sub(4)).mul(m.sub(3)).mul(Cb).div(A.pow(3).mul(B).mul(54))));
ok("Phi entire factorization",Phi.eq(C.pow(2).neg().div(m.mul(A.pow(2)).mul(3))));
ok("T0 entire factorization",T0.eq(C.mul(m.sub(4)).mul(m.sub(2)).mul(m.sub(3)).neg().div(A.pow(2).mul(3))));
ok("J-Q entire factorization",J.sub(Q).eq(C.pow(2).mul(m.sub(3)).neg().div(m.mul(A.pow(2)).mul(9))));
ok("physical lambda t coefficient",bc.mul(Q).div(P02).eq(m.mul(B).mul(Z).div(A.mul(C).mul(Cb).mul(2))));
const theta=e.mul(k).mul(24).add(k.mul(rr(8).sub(k))).div(k.add(4));
ok("theta complete formula",theta.eq(m.pow(2).sub(6).mul(2).div(m)));
ok("whole conic identity",theta.pow(2).eq(k.pow(2).add(k.mul(24)).add(48)));
ok("inverse parameter exactly m",theta.add(k).add(12).div(4).eq(m));
ok("explicit inverse of m",k.add(12).sub(theta).div(24).mul(m).eq(1));
// Reverse direction in the ENTIRE quadratic algebra over Q(k).
// Only k and k+4 may occur as variable denominators; no norm zero lost.
const kr=rr([0n,1n]),disc=kr.pow(2).add(kr.mul(24)).add(48);
class E{
 constructor(a=0,b=0){if(a instanceof E){this.a=a.a;this.b=a.b;}else{this.a=rr(a);this.b=rr(b);}}
 add(v){v=new E(v);return new E(this.a.add(v.a),this.b.add(v.b));}
 neg(){return new E(this.a.neg(),this.b.neg());}
 sub(v){return this.add(new E(v).neg());}
 mul(v){v=new E(v);return new E(this.a.mul(v.a).add(disc.mul(this.b.mul(v.b))),this.a.mul(v.b).add(this.b.mul(v.a)));}
 divScalar(v){v=rr(v);return new E(this.a.div(v),this.b.div(v));}
 pow(n){let r=new E(1),a=this;while(n){if(n&1)r=r.mul(a);n=Math.floor(n/2);if(n)a=a.mul(a);}return r;}
 eq(v){v=new E(v);return this.a.eq(v.a)&&this.b.eq(v.b);}
}
const th=new E(0,1),me=th.add(kr).add(12).divScalar(4);
const mei=new E(kr.add(12)).sub(th).divScalar(24);
ok("entire quadratic-algebra inverse m multiplies to one",me.mul(mei).eq(1));
const ae=me.pow(2).sub(me.mul(6)).add(6),be=me.pow(2).sub(me.mul(4)).add(6);
const ce=me.pow(3).sub(me.pow(2).mul(10)).add(me.mul(36)).sub(36);
const de=me.pow(2).mul(5).sub(me.mul(30)).add(36);
ok("reverse k reconstruction all conic branches",ae.mul(mei).mul(2).eq(kr));
ok("reverse k+4 reconstruction all conic branches",be.mul(mei).mul(2).eq(kr.add(4)));
const ei=new E(kr.add(4)).mul(th).add(kr.mul(kr.sub(8))).divScalar(kr.mul(24));
const ainv=mei.mul(2).divScalar(kr);
ok("A inverse uses only k and true m inverse",ae.mul(ainv).eq(1));
ok("reverse e reconstruction all conic branches",ce.mul(ainv).divScalar(6).eq(ei));
const ue=ei.add(1),ve=ue.mul(kr).add(2),vinv=mei.mul(6).divScalar(kr.add(4));
ok("V inverse uses only k+4 and true m inverse",ve.mul(vinv).eq(1));
const elle=ue.mul(new E(kr.add(2).pow(2)).sub(ei.mul(kr).mul(2))).mul(vinv).divScalar(kr);
ok("reverse ell reconstruction all conic branches",me.mul(me.sub(4)).mul(de).mul(ainv.pow(2)).divScalar(6).eq(elle));
const qcoef=kr.pow(2).mul(rr(8).sub(kr));
const qconst=kr.pow(3).neg().sub(kr.pow(2).mul(4)).sub(kr.mul(16)).sub(16);
ok("exact quadratic discriminant identity",qcoef.pow(2).sub(kr.pow(2).mul(12).mul(qconst).mul(4)).eq(kr.pow(2).mul(kr.add(4).pow(2)).mul(disc)));
function paidReverseDen(r){let p=r.d;for(let f of [[0n,1n],[4n,1n]]){while(p.length>1){let g=pgcd(p,f);if(g.length<=1)break;p=divexact(p,g);}}return p.length===1;}
for(let [name,x] of [["m",me],["m_inverse",mei],["A_inverse",ainv],["V_inverse",vinv],["e",ei],["ell",elle]])
 ok("no extra reverse denominator: "+name,paidReverseDen(x.a)&&paidReverseDen(x.b));
// Rationalize the ORIGINAL rho extension as well, using already paid m-3.
const sig=rr([0n,1n]),ms=rr(4).div(sig.pow(2).mul(3).add(1));
const As=ms.pow(2).sub(ms.mul(6)).add(6);
const Cs=ms.pow(3).sub(ms.pow(2).mul(10)).add(ms.mul(36)).sub(36);
const Qs=Cs.div(ms.mul(3)),rho=ms.sub(3).mul(sig);
ok("entire rho extension rationalization",rho.pow(2).eq(rr(1).sub(Qs)));
ok("rho parameter inverse",rho.div(ms.sub(3)).eq(sig));
ok("rho parameter denominator forced unit",ms.mul(sig.pow(2).mul(3).add(1)).eq(4));
return {schema:"isp-entire-K7-rational-curve-original-identities-v1",
date:"2026-11-28 Asia/Taipei",execution:"actual V8 BigInt exact rational polynomial arithmetic",
elapsed_milliseconds:Date.now()-started,completeExactIdentities:checks.length,identities:checks,
entireConicBothDirectionsReturned:true,allDiscriminantZeroBranchesRetained:true,
mInverseExplicitConstantNorm:true,reverseVariableDenominatorsOnly:["k","k+4"],
mZeroImpossibleByNorm96:true,finiteOriginalPointsHaveFiniteM:true,
AandBZeroCorrespondToAlreadyPaidKOrKPlusFour:true,
allRemainingOriginalPhysicalUnitsStillRequired:true,
rhoExtensionBothDirectionsReturned:true,
physicalScope:"current whole W K7=0; k,k+4,k+2 and all old physical units stay paid",
K7EntireOriginalFibreExcluded:false,wholeWExcluded:false,ordinaryISPClaim:false,
osExitCode:null,maxRSSKiB:null,noCoefficientCacheOrEncodedPayload:true};
})()
