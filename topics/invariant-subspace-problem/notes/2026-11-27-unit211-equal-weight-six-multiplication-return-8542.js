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



const input=arguments[0],mode=arguments[1]||"quadratic",prior=arguments[2],start=Date.now();
function parse(a){let p=new P();for(const[e,c]of a)p=p.add(P.term(e,new Q(...c.split("/"))));return p;}
const m=P.term([1,0,0,0,0]),q=P.term([0,1,0,0,0]),J=m.scale(2).add(q).sub(2);
const U=[m,m.sub(1),J,q,q.sub(1)],unames=["m","m_minus_one","J","Q","Q_minus_one"];
class R{
 constructor(n=0,e=[0,0,0,0,0]){if(n instanceof R){this.n=n.n;this.e=n.e.slice();return;}this.n=new P(n);this.e=U.map((_,i)=>e[i]||0);if(!this.n.c.size){this.e=[0,0,0,0,0];return;}for(let i=0;i<U.length;i++)while(this.e[i]>0){const[a,b]=pdiv(this.n,U[i]);if(b.c.size)break;this.n=a;this.e[i]--;}}
 add(o){o=new R(o);const e=this.e.map((a,i)=>Math.max(a,o.e[i]));let a=this.n,b=o.n;for(let i=0;i<U.length;i++){a=a.mul(U[i].pow(e[i]-this.e[i]));b=b.mul(U[i].pow(e[i]-o.e[i]));}return new R(a.add(b),e);}
 neg(){return new R(this.n.neg(),this.e);}
 sub(o){return this.add(new R(o).neg());}
 mul(o){o=new R(o);return new R(this.n.mul(o.n),this.e.map((a,i)=>a+o.e[i]));}
 scale(n,d=1){return new R(this.n.scale(n,d),this.e);}
 eq(o){return !this.sub(o).n.c.size;}
 json(){return{numerator:this.n.json(),denominatorExponents:this.e};}
 static read(v){return new R(parse(v.numerator),v.denominatorExponents);}
}
function cmp(a,b){const ta=a.reduce((s,v)=>s+v,0),tb=b.reduce((s,v)=>s+v,0);return tb-ta||b[0]-a[0]||b[2]-a[2]||b[1]-a[1];}
class A{
 constructor(v=0){this.c=new Map();if(v instanceof A){this.c=new Map(v.c);return;}const c=new R(v);if(c.n.c.size)this.c.set("0,0,0",c);}
 static term(e,c=1){const a=new A();c=new R(c);if(c.n.c.size)a.c.set(e.join(","),c);return a;}
 add(v){v=new A(v);const a=new A(this);for(const[k,c]of v.c){const z=(a.c.get(k)||new R()).add(c);if(z.n.c.size)a.c.set(k,z);else a.c.delete(k);}return a;}
 neg(){const a=new A();for(const[k,c]of this.c)a.c.set(k,c.neg());return a;}
 sub(v){return this.add(new A(v).neg());}
 mul(v){v=new A(v);const a=new A();for(const[k,c]of this.c){const e=k.split(",").map(Number);for(const[j,d]of v.c){const f=j.split(",").map(Number),key=e.map((z,i)=>z+f[i]).join(",");const z=(a.c.get(key)||new R()).add(c.mul(d));if(z.n.c.size)a.c.set(key,z);else a.c.delete(key);}}return a;}
 scale(v){return this.mul(new A(v));}
 eq(v){return !this.sub(v).c.size;}
 json(){return Array.from(this.c,([k,c])=>[k.split(",").map(Number),c.json()]).sort((a,b)=>cmp(a[0],b[0]));}
 static read(v){let a=new A();for(const[e,c]of v)a=a.add(A.term(e,R.read(c)));return a;}
}
function fromP(F){let a=new A();for(const[e,c]of F.json())a=a.add(A.term(e.slice(2),new R(P.term([e[0],e[1],0,0,0],new Q(...c.split("/"))))));return a;}


const six=arguments[2],names=["E1","EBe","EBo","N1","Ns","Ps"],original=names.map(n=>fromP(parse(input.rows[n].coefficients)));
const rules=six.rules.map(A.read),traces=six.traces.map(row=>[...row.map(A.read),new A(),new A()]),heads=six.heads;
const basis=six.generators.map(e=>A.term(e)),axes=[[1,0,0],[0,1,0],[0,0,1]];
function reduce(f){
 let work=new A(f),rem=new A(),trace=Array.from({length:6},()=>new A()),steps=0;
 while(work.c.size){
  if(++steps>1000)throw Error("six-rule reduction cap");
  const[e,jc]=work.json()[0],c=R.read(jc),k=heads.findIndex(g=>g.every((a,i)=>a<=e[i]));
  if(k<0){const term=A.term(e,c);rem=rem.add(term);work=work.sub(term);continue;}
  const mon=A.term(e.map((a,i)=>a-heads[k][i]),c);work=work.sub(mon.mul(rules[k]));trace=trace.map((a,i)=>a.add(mon.mul(traces[k][i])));
 }
 if(!trace.reduce((s,a,i)=>s.add(a.mul(original[i])),new A()).eq(f.sub(rem)))throw Error("complete original reduction identity");
 const row=basis.map((_,i)=>rem.c.get(six.generators[i].join(","))||new R());
 if(!row.reduce((s,c,i)=>s.add(basis[i].scale(c)),new A()).eq(rem))throw Error("six column support");
 return {row,trace,steps};
}
if(mode==="multiplication"){
 const matrices=[],errors=[],stepCounts=[];
 for(let a=0;a<3;a++){
  matrices[a]=[];errors[a]=[];stepCounts[a]=[];
  for(let i=0;i<6;i++){const rr=reduce(A.term(axes[a]).mul(basis[i]));matrices[a][i]=rr.row.map(c=>c.json());errors[a][i]=rr.trace.map(c=>c.json());stepCounts[a][i]=rr.steps;}
 }
 return{stage:"global_equal_weight_original_eighteen_multiplication_identities",denominatorUnits:unames,generators:six.generators,originalNames:names,matrices,errors,stepCounts,allEighteenOriginalProducts:true,freeModuleClaim:false,seconds:(Date.now()-start)/1000};
}
if(mode==="NP"){
 const rows=[];
 for(let n=4;n<6;n++){
  const rr=reduce(original[n]),tr=rr.trace.map(z=>z.neg());tr[n]=tr[n].add(1);
  if(!tr.reduce((s,a,i)=>s.add(a.mul(original[i])),new A()).eq(rr.row.reduce((s,c,i)=>s.add(basis[i].scale(c)),new A())))throw Error("original NP trace return");
  rows.push({name:names[n],row:rr.row.map(c=>c.json()),trace:tr.map(a=>a.json()),steps:rr.steps});
 }
 return{stage:"global_equal_weight_original_NS_PS_six_column_returns",denominatorUnits:unames,generators:six.generators,rows,allOriginalProducts:true,excluded:false,seconds:(Date.now()-start)/1000};
}
throw Error("unknown mode");
