"use strict";
// NEW original f=u,u=2 centered branch: exact low-N/P unit combination.
// Only the displayed original identities are evaluated; no old matrix,
// cofactor, Groebner, or whole Gram computation is replayed.
const started=Date.now();let products=0,checks=[];
function trim(a){while(a.length&&!a[a.length-1])a.pop();return a;}
const P=n=>n===0?[]:[BigInt(n)];
const Q=[0n,1n];
function add(a,b){return trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)+(b[i]||0n)));}
const neg=a=>a.map(x=>-x),sub=(a,b)=>add(a,neg(b));
function mul(a,b){products++;const c=Array(Math.max(0,a.length+b.length-1)).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return trim(c);}
const sc=(a,n)=>trim(a.map(v=>v*BigInt(n)));
const eq=(a,b)=>!sub(a,b).length;
class R{
 constructor(n=0,d=1){if(n instanceof R){this.n=n.n;this.d=n.d;return;}this.n=Array.isArray(n)?trim([...n]):P(n);this.d=Array.isArray(d)?trim([...d]):P(d);if(!this.d.length)throw Error("zero denominator");}
 add(z){z=new R(z);return new R(add(mul(this.n,z.d),mul(z.n,this.d)),mul(this.d,z.d));}
 neg(){return new R(neg(this.n),this.d);}
 sub(z){return this.add(new R(z).neg());}
 mul(z){z=new R(z);return new R(mul(this.n,z.n),mul(this.d,z.d));}
 div(z){z=new R(z);if(!z.n.length)throw Error("formal zero inverse");return new R(mul(this.n,z.d),mul(this.d,z.n));}
}
const r=x=>new R(x),sum=(...xs)=>xs.reduce((a,b)=>a.add(b),r(0));
const sq=x=>r(x).mul(x);
function check(name,a){if(r(a).n.length)throw Error(name);checks.push(name);}
const q=r(Q),delta=r(1).sub(q),h=q.sub(2);
const u=r(2),ell=r(1),t=r(4),x=r(3),y=q.div(h.mul(2));
const Sx=x.mul(2),Px=Sx.add(delta.mul(y).mul(2));
const XY=sq(x).sub(delta.mul(sq(y))),W=r(6).sub(q.div(2));
const A1=r(4).sub(Sx.add(y.mul(2))).sub(q.div(delta).mul(2));
const lam=A1.sub(r(8).div(q)).add(2).div(4);
const Psi=sum(q.mul(q).mul(q),sq(q).mul(-7),q.mul(16),-16);
const EBe=sum(r(3).div(2),q.div(2).neg(),r(-2).div(h),delta.mul(-2).div(sq(h)));
check("true_even_mean_is_minus_Psi_over_two_h_squared",
 EBe.add(Psi.div(sq(h).mul(2))));
check("N0_recovered_lambda_exact_Psi_error",
 lam.sub(r(1).div(delta)).add(Psi.div(q.mul(delta).mul(h).mul(4))));
const Kl=sum(
 sq(t),u.mul(3).sub(Sx).sub(2).mul(t).mul(2),
 XY.mul(2),Px.mul(3),r(2).sub(u.mul(2)).mul(Sx),W.mul(-2),
 sq(u).mul(4),u.mul(-16),4,ell.mul(q)).mul(2);
check("whole_original_Klambda_compact",
 Kl.sub(q.mul(4).add(delta.mul(q).mul(q.mul(5).sub(12)).div(sq(h)))));
const bc=q.neg().div(delta.mul(4)),P02=q.mul(2);
const Lowl=P02.mul(lam).mul(2).sub(bc.mul(t).mul(Kl));
check("full_original_low_and_even_mean_unit",
 Lowl.add(EBe.mul(4)).add(sq(q).mul(2).div(delta.mul(h))));
return {schema:"isp-true-Phi-fu-u-two-original-low-unit-v1",
 elapsed_milliseconds:Date.now()-started,integerPolynomialProducts:products,
 exactRationalPolynomialIdentities:checks,
 fullGramReplayed:false,oldMatrixReplayed:false,
 assumptions:"correct Phi f=u; Q,1-Q,theta=2-Q,t are previously paid; odd mean forces t=4",
 returnedOriginalIdentity:"Lowl+4*EBe=-2*Q^2/((1-Q)*(Q-2))",
 wholeFuUTwoExcluded:true,wholeFuExcluded:false,wholePhiExcluded:false,ordinaryISPClaim:false};