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

const input=arguments[0],start=Date.now();
function cq(s){const a=s.split("/");return new Q(a[0],a[1]||1);}
const k=P.term([1,0,0]),w=P.term([0,1,0]),v=P.term([0,0,1]),one=new P(1);
const mn=w.sub(1).mul(w.sub(k)),md=w.pow(2).sub(w.scale(2)).add(k),qn=v.pow(2).sub(k);
const pp=mn.scale(2).sub(md).mul(v.pow(2)).sub(k.mul(md).scale(3));
const units=[["v",v],["w",w],["k",k],["w_minus_one",w.sub(1)],["w_minus_k",w.sub(k)],["k_minus_one",k.sub(1)],["v_minus_one",v.sub(1)],["A_m_denominator",md],["Q",qn],["P02_other",pp]];
const output={stage:"equal_weight_original_three_parameter_chart",parameters:["k=d*v^2","w=z*v","v=2y-1"],m:"(w-1)(w-k)/(w^2-2w+k)",originalUnitChart:true,excluded:false,rows:{},seconds:0};
for(const name of ["E1","EBe","N1"]){
 const row=input.rows[name],M=row.degrees[0],Dq=row.degrees[1],Dz=row.degrees[3];let out=new P();
 for(const[e,c]of row.coefficients){
  let z=new P(cq(c));z=z.mul(mn.pow(e[0])).mul(md.pow(M-e[0])).mul(qn.pow(e[1])).mul(v.pow(2*(Dq-e[1])+Dz-e[3])).mul(v.add(1).pow(e[2])).scale(1,2**e[2]).mul(w.pow(e[3]));out=out.add(z);
 }
 const full=out;let paid=[];for(const[label,atom]of units){let ct=0;while(out.c.size){const[qq,rr]=pdiv(out,atom);if(rr.c.size)break;out=qq;ct++;}if(ct)paid.push([label,ct]);}
 output.rows[name]={clearing:{mDenPower:M,vPower:2*Dq+Dz},fullDegrees:[0,1,2].map(i=>full.degree(i)),fullTerms:full.c.size,paid,degrees:[0,1,2].map(i=>out.degree(i)),terms:out.c.size,coefficients:out.json()};
}
output.seconds=(Date.now()-start)/1000;return output;