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
const m=P.term([1,0,0,0,0]),q=P.term([0,1,0,0,0]),J=m.scale(2).add(q).sub(2);
const U=[m,m.sub(1),J,q,q.sub(1),m.scale(2).add(q.scale(3)).sub(4)],labels=["m","m_minus_one","J","Q","Q_minus_one","P02_other"];
const rows=[];
for(const obj of input){
 const exp=U.map((_,i)=>Math.max(...obj.row.map(c=>c.denominatorExponents[i]||0)));
 let denominator=new P(1);for(let i=0;i<U.length;i++)denominator=denominator.mul(U[i].pow(exp[i]));
 const cleared=obj.row.map(c=>{let f=parse(c.numerator);for(let i=0;i<U.length;i++)f=f.mul(U[i].pow(exp[i]-(c.denominatorExponents[i]||0)));return f;});
 let polys=cleared,removed=new P(1),paid=[];
 for(let i=0;i<U.length;i++){
  let n=0;
  while(polys.some(p=>p.c.size)){
   const ds=polys.map(p=>pdiv(p,U[i]));if(ds.some(([a,b])=>b.c.size))break;
   polys=ds.map(d=>d[0]);removed=removed.mul(U[i]);n++;
  }
  if(n)paid.push([labels[i],n]);
 }
 let den=1n,num=0n;for(const p of polys)for(const c of p.c.values())den=den/gcd(den,c.d)*c.d;
 for(const p of polys)for(const c of p.c.values())num=gcd(num,c.n*(den/c.d));
 const scale=new Q(den,num||1n);polys=polys.map(p=>p.scale(scale));removed=removed.scale(new Q(1).div(scale));
 for(let i=0;i<6;i++)if(!polys[i].mul(removed).eq(cleared[i]))throw Error("primitive six-row return");
 rows.push({name:obj.name,polynomials:polys.map(p=>p.json()),commonDenominatorExponents:exp,paidRemoved:paid,removedPolynomial:removed.json(),contentScale:scale.str(),degrees:[0,1].map(i=>Math.max(...polys.map(p=>p.degree(i)))),terms:polys.map(p=>p.c.size),allColumnProducts:true});
}
return{stage:"original_equal_weight_primitive_six_column_rows",rows,seconds:(Date.now()-start)/1000};
