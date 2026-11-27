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
 constructor(v=0){this.c=new Map();if(v instanceof P){this.c=new Map(v.c);return;}const q=new Q(v);if(q.n)this.c.set("0,0,0,0,0",q);}
 static term(e,c=1){const p=new P();const q=new Q(c);if(q.n)p.c.set(e.join(","),q);return p;}
 add(v){v=new P(v);const p=new P(this);for(const[k,a]of v.c){const z=(p.c.get(k)||new Q()).add(a);if(z.n)p.c.set(k,z);else p.c.delete(k);}return p;}
 neg(){const p=new P();for(const[k,a]of this.c)p.c.set(k,a.neg());return p;}
 sub(v){return this.add(new P(v).neg());}
 mul(v){v=new P(v);const p=new P();for(const[k,a]of this.c){const e=k.split(",").map(Number);for(const[j,b]of v.c){const f=j.split(",").map(Number),key=e.map((z,i)=>z+f[i]).join(",");const z=(p.c.get(key)||new Q()).add(a.mul(b));if(z.n)p.c.set(key,z);else p.c.delete(key);}}return p;}
 scale(n,d=1){return this.mul(new Q(n,d));}
 pow(n){let a=this,b=new P(1);while(n){if(n&1)b=b.mul(a);n>>=1;if(n)a=a.mul(a);}return b;}
 eq(v){v=this.sub(v);return !v.c.size;}
 degree(i){return Math.max(-1,...Array.from(this.c.keys(),k=>+k.split(",")[i]));}
 json(){return Array.from(this.c,([k,c])=>[k.split(",").map(Number),c.str()]).sort((a,b)=>{for(let i=0;i<5;i++)if(a[0][i]!=b[0][i])return b[0][i]-a[0][i];return 0;});}
}


function minExp(v,i){return Math.min(...Array.from(v.c.keys(),k=>Number(k.split(",")[i])));}
function ld(v){return v.json()[0];}
function pdiv(v,dv){let work=new P(v),quot=new P(),rem=new P();const [ed,cd]=ld(dv),dc=new Q(...cd.split("/"));let steps=0;while(work.c.size){if(++steps>10000)throw Error("division step cap");const[ew,cw]=ld(work),wc=new Q(...cw.split("/"));if(ew.every((e,i)=>e>=ed[i])){const mon=P.term(ew.map((e,i)=>e-ed[i]),wc.div(dc));quot=quot.add(mon);work=work.sub(mon.mul(dv));}else{const mon=P.term(ew,wc);rem=rem.add(mon);work=work.sub(mon);}}if(!quot.mul(dv).add(rem).eq(v))throw Error("multivariate division return");return[quot,rem];}



const input=arguments[0],start=Date.now();
function parse(a){let p=new P();for(const[e,c]of a)p=p.add(P.term(e,new Q(...c.split("/"))));return p;}
const d=P.term([1,0,0,0,0]),z=P.term([0,1,0,0,0]),E=parse(input.rows.E1.polynomial);
function cf(F,j){let p=new P();for(const[e,c]of F.json())if(e[1]===j)p=p.add(P.term([e[0],0,0,0,0],new Q(...c.split("/"))));return p;}
if(!cf(E,4).eq(1))throw Error("E is not monic z quartic");
const units=[["d",d],["Q",d.sub(1)],["z",z],["v",d.add(z.pow(2))],["v_minus_one",d.add(z.pow(2)).sub(d.mul(z).scale(2))],["v_plus_one",d.add(z.pow(2)).add(d.mul(z).scale(2))],["mean_m_leading",d.sub(z.pow(2))]];
const out={stage:"whole_equal_half_weight_monic_z_quartic_original_remainders",E:E.json(),rows:{},excluded:false};
for(const name of ["N1","Ns","Ps","Dval"]){
 const F=parse(input.rows[name].polynomial);let rem=F,quot=new P();
 while(rem.c.size&&rem.degree(1)>=4){const j=rem.degree(1),term=cf(rem,j).mul(z.pow(j-4));quot=quot.add(term);rem=rem.sub(term.mul(E));}
 if(!quot.mul(E).add(rem).eq(F))throw Error("whole z quartic original remainder "+name);
 const full=rem;let removed=new P(1),paid=[];
 for(const[label,u]of units){let n=0;while(rem.c.size){const[a,b]=pdiv(rem,u);if(b.c.size)break;rem=a;removed=removed.mul(u);n++;}if(n)paid.push([label,n]);}
 let dd=1n,nn=0n;for(const c of rem.c.values())dd=dd/gcd(dd,c.d)*c.d;for(const c of rem.c.values())nn=gcd(nn,c.n*(dd/c.d));const scale=new Q(dd,nn||1n);rem=rem.scale(scale);removed=removed.scale(new Q(1).div(scale));
 if(!removed.mul(rem).eq(full))throw Error("remainder paid factors");
 out.rows[name]={polynomial:rem.json(),quotient:quot.json(),removed:removed.json(),paid,scale:scale.str(),degrees:[rem.degree(0),rem.degree(1)],terms:rem.c.size,originalIdentityMultipliedBack:true};
}
out.seconds=(Date.now()-start)/1000;return out;
