"use strict";
const t0=Date.now();
function abs(x){return x<0n?-x:x;}
function gcd(a,b){a=abs(a);b=abs(b);while(b){let z=a%b;a=b;b=z;}return a;}
class Q {
 constructor(n=0n,d=1n){if(n instanceof Q){this.n=n.n;this.d=n.d;return;}n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
 add(o){o=new Q(o);return new Q(this.n*o.d+o.n*this.d,this.d*o.d);}
 neg(){return new Q(-this.n,this.d);}
 sub(o){return this.add(new Q(o).neg());}
 mul(o){o=new Q(o);return new Q(this.n*o.n,this.d*o.d);}
 div(o){o=new Q(o);return new Q(this.n*o.d,this.d*o.n);}
 eq(o){o=new Q(o);return this.n===o.n&&this.d===o.d;}
 str(){return this.d===1n?""+this.n:this.n+"/"+this.d;}
}
class P {
 constructor(v=0){this.c=new Map();if(v instanceof P){this.c=new Map(v.c);return;}const q=new Q(v);if(q.n)this.c.set("0,0,0",q);}
 static term(e,c=1){const p=new P();const q=new Q(c);if(q.n)p.c.set(e.join(","),q);return p;}
 add(v){v=new P(v);const p=new P(this);for(const[k,a]of v.c){const z=(p.c.get(k)||new Q()).add(a);if(z.n)p.c.set(k,z);else p.c.delete(k);}return p;}
 neg(){const p=new P();for(const[k,a]of this.c)p.c.set(k,a.neg());return p;}
 sub(v){return this.add(new P(v).neg());}
 mul(v){v=new P(v);const p=new P();for(const[k,a]of this.c){const e=k.split(",").map(Number);for(const[j,b]of v.c){const f=j.split(",").map(Number),key=e.map((z,i)=>z+f[i]).join(",");const z=(p.c.get(key)||new Q()).add(a.mul(b));if(z.n)p.c.set(key,z);else p.c.delete(key);}}return p;}
 scale(n,d=1){return this.mul(new Q(n,d));}
 pow(n){let a=this,b=new P(1);while(n){if(n&1)b=b.mul(a);n>>=1;if(n)a=a.mul(a);}return b;}
 eq(v){v=this.sub(v);return !v.c.size;}
 degree(i){return Math.max(-1,...Array.from(this.c.keys(),k=>+k.split(",")[i]));}
 json(){return Array.from(this.c,([k,c])=>[k.split(",").map(Number),c.str()]).sort((a,b)=>{for(let i=0;i<3;i++)if(a[0][i]!=b[0][i])return b[0][i]-a[0][i];return 0;});}
}
function minExp(v,i){return Math.min(...Array.from(v.c.keys(),k=>Number(k.split(",")[i])));}
function ld(v){return v.json()[0];}
function pdiv(v,dv){let work=new P(v),quot=new P(),rem=new P();const [ed,cd]=ld(dv),dc=new Q(...cd.split("/"));let steps=0;while(work.c.size){if(++steps>10000)throw Error("division step cap");const[ew,cw]=ld(work),wc=new Q(...cw.split("/"));if(ew.every((e,i)=>e>=ed[i])){const mon=P.term(ew.map((e,i)=>e-ed[i]),wc.div(dc));quot=quot.add(mon);work=work.sub(mon.mul(dv));}else{const mon=P.term(ew,wc);rem=rem.add(mon);work=work.sub(mon);}}if(!quot.mul(dv).add(rem).eq(v))throw Error("multivariate division return");return[quot,rem];}


const row=arguments[0],start=Date.now();
function cq(s){const a=s.split("/");return new Q(a[0],a[1]||1);}
const k=P.term([1,0,0]),w=P.term([0,1,0]),one=new P(1),md=k.add(w.pow(2)).sub(w.scale(2));
let alpha=new P(),beta=new P();for(const[e,c]of row.coefficients){if(e[2]===2)alpha=alpha.add(P.term([e[0],e[1],0],cq(c)));else if(e[2]===0)beta=beta.add(P.term(e,cq(c)));else throw Error("not even quadratic");}
const R=k.pow(2).add(w.sub(1).pow(2).mul(k)).sub(w.pow(2));
if(!alpha.scale(2).eq(w.sub(1).mul(md).mul(R)))throw Error("leading factor");
const [quot,rem]=pdiv(beta.scale(2),R);
let reduced=rem,paid=[];for(const[label,atom]of [["k",k],["w",w],["w_minus_one",w.sub(1)],["k_minus_one",k.sub(1)],["w_minus_k",w.sub(k)],["Abar",md]]){let n=0;while(reduced.c.size){const[q,r]=pdiv(reduced,atom);if(r.c.size)break;reduced=q;n++;}if(n)paid.push([label,n]);}

const B=w.pow(4).sub(w.pow(3).scale(2)).add(w.pow(2).scale(4)).sub(w.scale(2)).add(1),C=w.pow(2).mul(w.pow(2).add(1)),L=k.mul(B).sub(C);
if(!beta.scale(2).eq(quot.mul(R).sub(w.mul(L).scale(4))))throw Error("full beta return");
const J=k.mul(B).add(C).add(w.sub(1).pow(2).mul(B)),U=w.pow(4).mul(w.sub(1).pow(4));
if(!B.pow(2).mul(R).add(U).eq(L.mul(J)))throw Error("whole resultant unit identity");
const vv=P.term([0,0,1]),Ebar=alpha.mul(vv.pow(2)).add(beta);
const coeffR=quot.mul(J).sub(w.mul(B.pow(2)).scale(4)).add(J.mul(w.sub(1)).mul(md).mul(vv.pow(2))),coeffE=J.scale(-2);
if(!coeffR.mul(R).add(coeffE.mul(Ebar)).eq(w.mul(U).scale(4)))throw Error("actual mean ideal unit identity");
return {stage:"equal_weight_original_monic_value_quadratic",seconds:(Date.now()-start)/1000,originalMeanIdentityVerified:true,alphaFactor:"2alpha=(w-1)Abar R",R:"k^2+(w-1)^2*k-w^2",originalBetaReductionVerified:true,wholeWeightLeadingZeroBranchExcluded:true,unitIdentity:"coeffR*R-2J*Ebar=4*w^5*(w-1)^4",allUnitIdentityProductsMultipliedBack:true,monicValueQuadratic:"v^2=-beta/alpha",sameValueV:true,wholeEqualWeightExcluded:false,alpha:alpha.json(),beta:beta.json(),quotient:quot.json(),B:B.json(),C:C.json(),J:J.json(),coeffR:coeffR.json(),coeffE:coeffE.json()};
