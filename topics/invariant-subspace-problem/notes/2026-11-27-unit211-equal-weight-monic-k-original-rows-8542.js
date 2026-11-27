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


const input=arguments[0],report=arguments[1]||(()=>{}),start=Date.now();
function parse(a){let p=new P();for(const[e,c]of a)p=p.add(P.term(e,new Q(...c.split("/"))));return p;}
const k=P.term([1,0,0]),w=P.term([0,1,0]),v=P.term([0,0,1]),A=k.add(w.pow(2)).sub(w.scale(2)),mn=w.sub(1).mul(w.sub(k)),PP=mn.scale(2).sub(A).mul(v.pow(2)).sub(k.mul(A).scale(3)),R=k.pow(2).add(w.sub(1).pow(2).mul(k)).sub(w.pow(2));
const units=[["v",v],["w",w],["k",k],["w_minus_one",w.sub(1)],["w_minus_k",w.sub(k)],["k_minus_one",k.sub(1)],["v_minus_one",v.sub(1)],["v_plus_one",v.add(1)],["A",A],["R",R],["Q",v.pow(2).sub(k)],["P02_other",PP]];
const E=parse(input.E1.coefficients).scale(2);
if(E.json()[0][0].join(",")!=="4,0,0"||E.json()[0][1]!=="1")throw Error("not monic quartic k");
const out={stage:"original_general_equal_weight_monic_k_quartic",E:{degrees:[0,1,2].map(i=>E.degree(i)),terms:E.c.size,coefficients:E.json()},rows:{},excluded:false};
for(const[name,row]of Object.entries(input)){
 if(name==="E1")continue;const F=parse(row.coefficients),[q,r]=pdiv(F,E);let f=r,paid=[],factor=new P(1);
 for(const[label,u]of units){let ct=0;while(f.c.size){const[div,rem]=pdiv(f,u);if(rem.c.size)break;f=div;factor=factor.mul(u);ct++;}if(ct)paid.push([label,ct]);}
 let den=1n,num=0n;for(const c of f.c.values())den=den/gcd(den,c.d)*c.d;for(const c of f.c.values())num=gcd(num,c.n*(den/c.d));const scale=new Q(den,num||1n);f=f.scale(scale);factor=factor.scale(new Q(1).div(scale));
 if(!q.mul(E).add(factor.mul(f)).eq(F))throw Error("full original return "+name);
 const dk=f.degree(0),lc=new P();for(const[e,c]of f.json())if(e[0]===dk)lc.c.set([0,e[1],e[2]].join(","),new Q(...c.split("/")));
 out.rows[name]={originalDegrees:[0,1,2].map(i=>F.degree(i)),paid,scale:scale.str(),degrees:[0,1,2].map(i=>f.degree(i)),terms:f.c.size,coefficients:f.json(),originalQuotient:q.json(),factor:factor.json(),leadingK:lc.json()};
 report({name,seconds:(Date.now()-start)/1000,paid,degrees:out.rows[name].degrees,terms:f.c.size,leadingTerms:lc.c.size});
}
out.seconds=(Date.now()-start)/1000;return out;
