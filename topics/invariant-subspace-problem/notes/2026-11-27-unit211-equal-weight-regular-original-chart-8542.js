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
 constructor(v=0){this.c=new Map();if(v instanceof P){this.c=new Map(v.c);return;}const q=new Q(v);if(q.n)this.c.set("0,0,0,0",q);}
 static term(e,c=1){const p=new P();const q=new Q(c);if(q.n)p.c.set(e.join(","),q);return p;}
 add(v){v=new P(v);const p=new P(this);for(const[k,a]of v.c){const z=(p.c.get(k)||new Q()).add(a);if(z.n)p.c.set(k,z);else p.c.delete(k);}return p;}
 neg(){const p=new P();for(const[k,a]of this.c)p.c.set(k,a.neg());return p;}
 sub(v){return this.add(new P(v).neg());}
 mul(v){v=new P(v);const p=new P();for(const[k,a]of this.c){const e=k.split(",").map(Number);for(const[j,b]of v.c){const f=j.split(",").map(Number),key=e.map((z,i)=>z+f[i]).join(",");const z=(p.c.get(key)||new Q()).add(a.mul(b));if(z.n)p.c.set(key,z);else p.c.delete(key);}}return p;}
 scale(n,d=1){return this.mul(new Q(n,d));}
 pow(n){let a=this,b=new P(1);while(n){if(n&1)b=b.mul(a);n>>=1;if(n)a=a.mul(a);}return b;}
 eq(v){v=this.sub(v);return !v.c.size;}
 degree(i){return Math.max(-1,...Array.from(this.c.keys(),k=>+k.split(",")[i]));}
 json(){return Array.from(this.c,([k,c])=>[k.split(",").map(Number),c.str()]).sort((a,b)=>{for(let i=0;i<4;i++)if(a[0][i]!=b[0][i])return b[0][i]-a[0][i];return 0;});}
}

const m=P.term([1,0,0,0]),q=P.term([0,1,0,0]),y=P.term([0,0,1,0]),zeta=P.term([0,0,0,1]),ivm=P.term([-1,0,0,0]),one=new P(1),d=one.sub(q),a=one.sub(m);
const x=m.add(y.sub(1).mul(zeta));
const t=one.sub(zeta).scale(2).add(zeta.sub(d).mul(y).scale(2).sub(q).mul(ivm));
class E{
 constructor(a=0,b=0){if(a instanceof E){this.a=a.a;this.b=a.b;}else{this.a=new P(a);this.b=new P(b);}}
 add(v){v=new E(v);return new E(this.a.add(v.a),this.b.add(v.b));}
 neg(){return new E(this.a.neg(),this.b.neg());}
 sub(v){return this.add(new E(v).neg());}
 mul(v){v=new E(v);return new E(this.a.mul(v.a).add(d.mul(this.b).mul(v.b)),this.a.mul(v.b).add(this.b.mul(v.a)));}
 scale(n,dd=1){return this.mul(new E(new Q(n,dd)));}
 pow(n){let a=this,b=new E(1);while(n){if(n&1)b=b.mul(a);n>>=1;if(n)a=a.mul(a);}return b;}
 eq(v){v=new E(v);return this.a.eq(v.a)&&this.b.eq(v.b);}
 conj(){return new E(this.a,this.b.neg());}
}
const b=new E(m.scale(1,2)),c=b,p=new E(1,1),pp=p.conj();
const X=new E(x,y),Y=X.conj(),f=x.add(d.mul(y)).scale(1,2).sub(one.add(d).sub(m.scale(2)).scale(1,4));
const rg=X.sub(new E(a).mul(p)).sub(c.mul(new E(t))),sg=Y.sub(new E(a).mul(pp)).sub(b.mul(new E(t)));
const Ag=new E(f.scale(2)).sub(b.mul(X).scale(2)).sub(c.mul(Y).scale(2)).add(b.mul(c).mul(new E(t)).scale(2));
const rows=[[new E(),new E(),p,pp],[new E(),Ag,rg,sg],[p,rg,new E(),new E(t)],[pp,sg,new E(t),new E()]];
const unit=[new E(1),new E(),new E(1),new E(1)];
const va=(v,w)=>v.map((z,i)=>z.add(w[i]));
const vs=(s,v)=>v.map(z=>new E(s).mul(z));
const vm=(v,w)=>[v[0].mul(w[0]),v[0].mul(w[1]).add(v[1].mul(w[0])),v[2].mul(w[2]),v[3].mul(w[3])];
const tau=v=>new E(a).mul(v[0]).add(v[1]).add(b.mul(v[2])).add(c.mul(v[3]));
const DK=v=>rows.map(row=>tau(vm(row,v)));
const dv=DK(unit),F2=tau(dv),Kd=DK(dv);
if(!F2.eq(new E(f.scale(2))))throw Error("F2");
function mean(j){const ee=j===1?tau(vm(rows[0],rows[1])).scale(2):tau(vm(rows[j],rows[j]));return ee.sub(Kd[j].scale(2)).sub(vm(dv,dv)[j].scale(2)).add(F2.mul(dv[j]).scale(2));}
const E1=mean(1),EB=mean(2),EC=mean(3);
if(!mean(0).eq(0)||!EB.b.eq(0)||!EB.eq(EC)||!E1.b.eq(0))throw Error("same mean identities");
function N4(v){return tau(vm(dv,vm(v,v))).scale(2).sub(F2.mul(tau(vm(v,v)))).sub(tau(v).mul(tau(vm(dv,v))).scale(4)).add(F2.mul(tau(v).pow(2)).scale(2)).add(tau(vm(v,DK(v))));}
function P2(v){const z=va(v,vs(tau(v).neg(),unit));return tau(vm(vm(z,z),z));}
const v=rows[0],z=rows[1],Nv=N4(va(v,z)).sub(N4(v)).sub(N4(z));
const vc=va(v,vs(tau(v).neg(),unit)),zc=va(z,vs(tau(z).neg(),unit)),Jnum=tau(vm(vm(vc,vc),zc));
const P02=m.mul(m.sub(1)).mul(m.scale(2).add(q.scale(3)).sub(4));
if(!P2(rows[0]).eq(new E(P02)))throw Error("P02");
const Lnum=N4(rows[0]).scale(1,2);
if(!Lnum.b.eq(0)||!Nv.b.eq(0)||!Jnum.b.eq(0))throw Error("even N");
const nw=b.mul(N4(rows[2])).add(c.mul(N4(rows[3]))),pw=b.mul(P2(rows[2])).add(c.mul(P2(rows[3])));
if(!nw.b.eq(0)||!pw.b.eq(0))throw Error("even weighted");
const L=Lnum.a,J=Jnum.a,NN=Nv.a;
const N1=P02.mul(NN).sub(L.mul(J).scale(4));
const Ns=P02.pow(2).mul(nw.a).sub(m.sub(1).mul(L).mul(P02.pow(2)).scale(2)).add(L.mul(J).mul(P02).scale(4)).sub(L.pow(3).scale(4));
const Ps=P02.pow(2).mul(pw.a).sub(m.sub(1).mul(P02.pow(3))).add(J.mul(P02.pow(2)).scale(3)).sub(L.pow(3).scale(4));

function minExp(v,i){return Math.min(...Array.from(v.c.keys(),k=>Number(k.split(",")[i])));}
function ld(v){return v.json()[0];}
function pdiv(v,dv){let work=new P(v),quot=new P(),rem=new P();const [ed,cd]=ld(dv),dc=new Q(...cd.split("/"));let steps=0;while(work.c.size){if(++steps>10000)throw Error("division step cap");const[ew,cw]=ld(work),wc=new Q(...cw.split("/"));if(ew.every((e,i)=>e>=ed[i])){const mon=P.term(ew.map((e,i)=>e-ed[i]),wc.div(dc));quot=quot.add(mon);work=work.sub(mon.mul(dv));}else{const mon=P.term(ew,wc);rem=rem.add(mon);work=work.sub(mon);}}if(!quot.mul(dv).add(rem).eq(v))throw Error("multivariate division return");return[quot,rem];}
const units=[["m",m],["m_minus_one",m.sub(1)],["Q",q],["Q_minus_one",q.sub(1)],["P02_other",m.scale(2).add(q.scale(3)).sub(4)],["y_minus_one",y.sub(1)]];
const output={stage:"equal_weight_y_not_one_regular_original_chart",seconds:0,originalE0N0MeanAndWeightedIdentities:true,EBoExactlyZero:true,chartInverse:"z=(x-m)/(y-1)",onlyNewlyUsedUnit:"y-1, proved by complete original exclusion",tFormula:"2(1-z)+(2(z-(1-Q))y-Q)/m",excluded:false,rows:{}};
for(const [name,p0]of [["E1",E1.a],["EBe",EB.a],["N1",N1],["Ns",Ns],["Ps",Ps]]){
 const min=minExp(p0,0),clear=Math.max(0,-min);let p=p0.mul(m.pow(clear)),paid=[];for(const[label,atom]of units){let count=0;while(p.c.size){const[qu,rem]=pdiv(p,atom);if(rem.c.size)break;p=qu;count++;}if(count)paid.push([label,count]);}
 output.rows[name]={clearM:clear,paid,degrees:[0,1,2,3].map(i=>p.degree(i)),terms:p.c.size,coefficients:p.json()};
}
output.seconds=(Date.now()-t0)/1000;return output;