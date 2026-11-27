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


const input=arguments[0],udata=arguments[1],report=arguments[2]||(()=>{}),started=Date.now();
function fromJSON(a){let p=new P();for(const[e,c]of a)p=p.add(P.term(e,new Q(...c.split("/"))));return p;}
const k=P.term([1,0,0]),w=P.term([0,1,0]),v=P.term([0,0,1]);
const alpha=fromJSON(udata.alpha),beta=fromJSON(udata.beta),E=alpha.mul(v.pow(2)).add(beta);
const A=k.add(w.pow(2)).sub(w.scale(2)),R=k.pow(2).add(w.sub(1).pow(2).mul(k)).sub(w.pow(2)),mn=w.sub(1).mul(w.sub(k));
const physicalPure=[["k",k],["w",w],["w_minus_one",w.sub(1)],["w_minus_k",w.sub(k)],["k_minus_one",k.sub(1)],["A",A],["R",R],["beta",beta],["Q_norm",beta.add(k.mul(alpha))],["P02_norm",mn.scale(2).sub(A).mul(beta).add(k.mul(A).mul(alpha).scale(3))]];
const output={stage:"original_equal_weight_same_v_linear_remainder",exactOriginalTrace:true,allLeadingZeroFibresPreserved:true,excluded:false,rows:{}};
for(const[name,row]of Object.entries(input.rows)){
 const F=fromJSON(row.coefficients),n=F.degree(2),L=Math.floor(n/2),ap=[new P(1)],bp=[new P(1)];
 for(let i=1;i<=L;i++){ap.push(ap[i-1].mul(alpha));bp.push(bp[i-1].mul(beta.neg()));}
 let C=Array.from({length:n+1},()=>new P());for(const[e,c]of F.json())C[e[2]]=C[e[2]].add(P.term([e[0],e[1],0],new Q(...c.split("/"))));
 let a0=new P(),a1=new P(),trace=new P();
 for(let j=0;j<=n;j++){
  const q=Math.floor(j/2),par=j%2,term=C[j].mul(bp[q]).mul(ap[L-q]);
  if(par)a1=a1.add(term);else a0=a0.add(term);
  if(q){let s=new P();for(let i=0;i<q;i++)s=s.add(ap[q-1-i].mul(v.pow(2*(q-1-i))).mul(bp[i]));
   trace=trace.add(C[j].mul(ap[L-q]).mul(v.pow(par)).mul(s));}
 }
 if(!ap[L].mul(F).sub(a0.add(a1.mul(v))).eq(E.mul(trace)))throw Error("original trace "+name);
 report({stage:"trace_returned",name,seconds:(Date.now()-started)/1000,terms:[a0.c.size,a1.c.size]});
 let factor=new P(1),paid=[];
 for(const[label,atom]of physicalPure){let c=0;while(a0.c.size||a1.c.size){
  const[q0,r0]=pdiv(a0,atom);if(r0.c.size)break;const[q1,r1]=pdiv(a1,atom);if(r1.c.size)break;
  a0=q0;a1=q1;factor=factor.mul(atom);c++;
 }if(c)paid.push([label,c]);}
 let den=1n,num=0n;for(const a of[a0,a1])for(const c of a.c.values()){den=den/gcd(den,c.d)*c.d;}for(const a of[a0,a1])for(const c of a.c.values()){num=gcd(num,c.n*(den/c.d));}
 const scale=new Q(den,num||1n);a0=a0.scale(scale);a1=a1.scale(scale);factor=factor.scale(scale.div(1).div(scale.mul(scale)));
 if(!ap[L].mul(F).sub(factor.mul(a0.add(a1.mul(v)))).eq(E.mul(trace)))throw Error("stripped trace "+name);
 output.rows[name]={degreeV:n,alphaPower:L,paid,scale:scale.str(),degrees0:[0,1].map(i=>a0.degree(i)),degrees1:[0,1].map(i=>a1.degree(i)),terms0:a0.c.size,terms1:a1.c.size,atVOneIdenticallyZero:a0.add(a1).eq(0),atVMinusOneIdenticallyZero:a0.sub(a1).eq(0),a0:a0.json(),a1:a1.json(),factor:factor.json(),trace:trace.json()};
 report({stage:"row_returned",name,seconds:(Date.now()-started)/1000,paid,terms:[a0.c.size,a1.c.size]});
}
output.seconds=(Date.now()-started)/1000;return output;
