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


const input=arguments[0],start=Date.now(),m=P.term([1,0,0,0,0]),qq=new P(2).sub(m.scale(2));
const units=[["m",m],["m_minus_one",m.sub(1)],["two_m_minus_one",m.scale(2).sub(1)]];
function sub(a){let f=new P();for(const[e,c]of a)f=f.add(P.term([e[0],0,e[2],e[3],e[4]],new Q(...c.split("/"))).mul(qq.pow(e[1])));return f;}
const out={stage:"original_equal_weight_T0_zero_entire_parameter_line",Q:"2-2m",physicalUnits:["m","m-1","2m-1"],rows:{},heads:[],excluded:false};
for(const[name,row]of Object.entries(input.rows)){
 const full=sub(row.coefficients);let f=full,paid=[],factor=new P(1);
 for(const[label,u]of units){let ct=0;while(f.c.size){const[q,r]=pdiv(f,u);if(r.c.size)break;f=q;factor=factor.mul(u);ct++;}if(ct)paid.push([label,ct]);}
 let den=1n,num=0n;for(const c of f.c.values())den=den/gcd(den,c.d)*c.d;for(const c of f.c.values())num=gcd(num,c.n*(den/c.d));const scale=new Q(den,num||1n);f=f.scale(scale);factor=factor.scale(new Q(1).div(scale));if(!factor.mul(f).eq(full))throw Error("original return");
 out.rows[name]={degrees:[0,1,2,3,4].map(i=>f.degree(i)),terms:f.c.size,paid,scale:scale.str(),coefficients:f.json(),factor:factor.json()};
}
function det(a){if(a.length===1)return a[0][0];let s=new P();for(let j=0;j<a.length;j++)s=s.add(a[0][j].mul(det(a.slice(1).map(r=>r.filter((_,k)=>k!==j)))).scale(j%2?-1:1));return s;}
const names=["E1","EBe","EBo","N1"],mons=[[2,0,0],[1,1,0],[1,0,1],[0,2,0],[0,1,1],[0,0,2]];
const mat=names.map(n=>mons.map(mm=>{let p=new P();for(const[e,c]of out.rows[n].coefficients)if(e.slice(2).every((v,i)=>v===mm[i]))p=p.add(P.term([e[0],0,0,0,0],new Q(...c.split("/"))));return p;}));
for(let a=0;a<3;a++)for(let b=a+1;b<4;b++)for(let c=b+1;c<5;c++)for(let d=c+1;d<6;d++){
 const cols=[a,b,c,d],full=det(mat.map(row=>cols.map(j=>row[j])));let f=full,paid=[];
 for(const[label,u]of units){let ct=0;while(f.c.size){const[q,r]=pdiv(f,u);if(r.c.size)break;f=q;ct++;}if(ct)paid.push([label,ct]);}
 out.heads.push({cols,zero:!f.c.size,paid,remaining:f.json(),degree:f.degree(0)});
}
out.seconds=(Date.now()-start)/1000;return out;
