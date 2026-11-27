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
const m=P.term([1,0,0,0,0]),q=P.term([0,1,0,0,0]),units=[["m",m],["m_minus_one",m.sub(1)],["Q",q],["Q_minus_one",q.sub(1)],["P02_other",m.scale(2).add(q.scale(3)).sub(4)]];
const names=["E1","EBe","EBo","N1"],mons=[[2,0,0],[1,1,0],[1,0,1],[0,2,0],[0,1,1],[0,0,2]];
const rows=names.map(n=>parse(input.rows[n].coefficients));
const mat=rows.map(F=>mons.map(mm=>{let p=new P();for(const[e,c]of F.json())if(e.slice(2).every((v,i)=>v===mm[i]))p=p.add(P.term([e[0],e[1],0,0,0],new Q(...c.split("/"))));return p;}));
function det(a){if(a.length===1)return a[0][0];let s=new P();for(let j=0;j<a.length;j++){const d=det(a.slice(1).map(r=>r.filter((_,k)=>k!==j)));s=s.add(a[0][j].mul(d).scale(j%2?-1:1));}return s;}
const out={stage:"all_original_equal_weight_quadratic_heads",originalRows:names,columns:mons,minors:[],excluded:false};
for(let a=0;a<3;a++)for(let b=a+1;b<4;b++)for(let c=b+1;c<5;c++)for(let d=c+1;d<6;d++){
 const cols=[a,b,c,d],F=det(mat.map(row=>cols.map(i=>row[i])));let f=F,paid=[],factor=new P(1);
 for(const[label,u]of units){let n=0;while(f.c.size){const[p,r]=pdiv(f,u);if(r.c.size)break;f=p;factor=factor.mul(u);n++;}if(n)paid.push([label,n]);}
 if(!factor.mul(f).eq(F))throw Error("head factor return");
 out.minors.push({cols,zero:!F.c.size,paid,fullDegrees:[0,1].map(i=>F.degree(i)),remainingDegrees:[0,1].map(i=>f.degree(i)),terms:f.c.size,remaining:f.json(),full:F.json()});
}
out.seconds=(Date.now()-start)/1000;return out;
