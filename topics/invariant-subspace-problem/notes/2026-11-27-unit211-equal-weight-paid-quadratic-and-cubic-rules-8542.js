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
const U=[m,m.sub(1),J],unames=["m","m_minus_one","J"];
class R{
 constructor(n=0,e=[0,0,0]){if(n instanceof R){this.n=n.n;this.e=n.e.slice();return;}this.n=new P(n);this.e=e.slice();if(!this.n.c.size){this.e=[0,0,0];return;}for(let i=0;i<3;i++)while(this.e[i]>0){const[a,b]=pdiv(this.n,U[i]);if(b.c.size)break;this.n=a;this.e[i]--;}}
 add(o){o=new R(o);const e=this.e.map((a,i)=>Math.max(a,o.e[i]));let a=this.n,b=o.n;for(let i=0;i<3;i++){a=a.mul(U[i].pow(e[i]-this.e[i]));b=b.mul(U[i].pow(e[i]-o.e[i]));}return new R(a.add(b),e);}
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
const names=["E1","EBe","EBo","N1"],original=names.map(n=>fromP(parse(input.rows[n].coefficients)));
function det(a){if(a.length===1)return a[0][0];let s=new P();for(let j=0;j<a.length;j++)s=s.add(a[0][j].mul(det(a.slice(1).map(r=>r.filter((_,k)=>k!==j)))).scale(j%2?-1:1));return s;}
const heads=[[2,0,0],[1,1,0],[1,0,1],[0,0,2]];
let rules,traces;
if(mode==="quadratic"){
 const M=original.map(f=>heads.map(e=>(f.c.get(e.join(","))||new R()).n));
 const delta=det(M),expect=m.pow(2).mul(m.sub(1).pow(2)).mul(J.pow(2)).scale(-16);
 if(!delta.eq(expect))throw Error("quadratic determinant");
 const adj=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>det(M.filter((_,r)=>r!==j).map(row=>row.filter((_,c)=>c!==i))).scale((i+j)%2?-1:1)));
 for(let i=0;i<4;i++)for(let j=0;j<4;j++){let c=new P();for(let k=0;k<4;k++)c=c.add(adj[i][k].mul(M[k][j]));if(!c.eq(i===j?delta:0))throw Error("cofactor inverse return");}
 traces=adj.map(row=>row.map(c=>new A(new R(c.scale(-1,16),[2,2,2]))));
 rules=traces.map(tr=>tr.reduce((s,a,i)=>s.add(a.mul(original[i])),new A()));
 for(let i=0;i<4;i++)for(let j=0;j<4;j++)if(!(rules[i].c.get(heads[j].join(","))||new R()).eq(i===j?1:0))throw Error("monic quadratic "+i+"/"+j);
 return{stage:"original_equal_weight_paid_quadratic_rules",denominatorUnits:unames,originalNames:names,headOrder:heads,determinant:delta.json(),rules:rules.map(a=>a.json()),traces:traces.map(row=>row.map(a=>a.json())),actualCofactorProducts:16,allOriginalCombinations:true,seconds:(Date.now()-start)/1000};
}
rules=prior.rules.map(A.read);traces=prior.traces.map(row=>row.map(A.read));
function reduce(f,tr){let work=new A(f),rem=new A(),steps=0;while(work.c.size){if(++steps>1000)throw Error("quadratic reduction cap");const[e,jc]=work.json()[0],c=R.read(jc);let k=heads.findIndex(g=>g.every((a,i)=>a<=e[i]));if(k<0){const term=A.term(e,c);rem=rem.add(term);work=work.sub(term);continue;}const mon=A.term(e.map((a,i)=>a-heads[k][i]),c);work=work.sub(mon.mul(rules[k]));tr=tr.map((a,i)=>a.sub(mon.mul(traces[k][i])));}
 const back=tr.reduce((s,a,i)=>s.add(a.mul(original[i])),new A());if(!back.eq(rem))throw Error("overlap original return");return{remainder:rem,trace:tr,steps};
}
const ax=A.term([1,0,0]),ay=A.term([0,1,0]),at=A.term([0,0,1]);
const pairs=[[0,ay,1,ax],[0,at,2,ax],[1,at,2,ay],[2,at,3,ax]];
const overlaps=pairs.map(([i,a,j,b])=>reduce(a.mul(rules[i]).sub(b.mul(rules[j])),traces[i].map((z,k)=>a.mul(z).sub(b.mul(traces[j][k])))));
const cubicHeads=[[0,3,0],[0,2,1]],matrix=overlaps.map(z=>cubicHeads.map(e=>z.remainder.c.get(e.join(","))||new R()));
const allUnits=[...U,q,q.sub(1),m.scale(2).add(q.scale(3)).sub(4)],labels=[...unames,"Q","Q_minus_one","P02_other"];
const minors=[];
for(let i=0;i<4;i++)for(let j=i+1;j<4;j++){
 const d=matrix[i][0].mul(matrix[j][1]).sub(matrix[i][1].mul(matrix[j][0]));let f=d.n,paid=[],fac=new P(1);
 for(let k=0;k<allUnits.length;k++){let n=0;while(f.c.size){const[a,b]=pdiv(f,allUnits[k]);if(b.c.size)break;f=a;fac=fac.mul(allUnits[k]);n++;}if(n)paid.push([labels[k],n]);}
 if(!fac.mul(f).eq(d.n))throw Error("cubic minor factor return");
 minors.push({pair:[i,j],zero:!f.c.size,paid,denominatorExponents:d.e,remainingDegrees:[f.degree(0),f.degree(1)],remaining:f.json(),terms:f.c.size,full:d.json()});
}
return{stage:"original_equal_weight_four_cubic_overlap_heads",denominatorUnits:unames,cubicHeads,overlaps:overlaps.map(z=>({remainder:z.remainder.json(),trace:z.trace.map(a=>a.json()),steps:z.steps})),minors,allOriginalOverlapReturns:true,excluded:false,seconds:(Date.now()-start)/1000};
