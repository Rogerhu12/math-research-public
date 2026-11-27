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



const input=arguments[0],start=Date.now(),d=P.term([1,0,0,0,0]),z=P.term([0,1,0,0,0]),qn=new P(1).sub(d);
const den=d.mul(z).scale(4),X=z.mul(d.scale(3).sub(d.mul(z).scale(2)).add(z.pow(2))),Y=d.mul(z).scale(2).add(d).add(z.pow(2)),T=z.sub(d).mul(d.add(z.pow(2))).scale(4);
const units=[["d",d],["z",z],["Q",d.sub(1)],["v",d.add(z.pow(2))],["v_minus_one",d.add(z.pow(2)).sub(d.mul(z).scale(2))],["v_plus_one",d.add(z.pow(2)).add(d.mul(z).scale(2))],["mean_m_leading",d.sub(z.pow(2))]];
const output={stage:"whole_equal_half_weight_original_two_parameter_return",parameterNames:["d","z"],m:"1/2",Q:"1-d",xNumerator:X.json(),yNumerator:Y.json(),tNumerator:T.json(),denominator:den.json(),rows:{},excluded:false};
for(const[name,row]of Object.entries(input.rows)){
 const deg=row.xyzTotalDegree;let f=new P();
 for(const[e,c]of row.coefficients){const coef=new Q(...c.split("/")).div(2n**BigInt(e[0]));const term=qn.pow(e[1]).mul(X.pow(e[2])).mul(Y.pow(e[3])).mul(T.pow(e[4])).mul(den.pow(deg-e[2]-e[3]-e[4])).scale(coef);f=f.add(term);}
 const full=f;let factor=new P(1),paid=[];
 for(const[label,u]of units){let n=0;while(f.c.size){const[a,b]=pdiv(f,u);if(b.c.size)break;f=a;factor=factor.mul(u);n++;}if(n)paid.push([label,n]);}
 let dd=1n,nn=0n;for(const c of f.c.values())dd=dd/gcd(dd,c.d)*c.d;for(const c of f.c.values())nn=gcd(nn,c.n*(dd/c.d));const scale=new Q(dd,nn||1n);f=f.scale(scale);factor=factor.scale(new Q(1).div(scale));
 if(!f.mul(factor).eq(full))throw Error("original half-weight substitution/factor "+name);
 output.rows[name]={zero:!f.c.size,degree:[f.degree(0),f.degree(1)],terms:f.c.size,paid,factor:factor.json(),scale:scale.str(),polynomial:f.json(),allOriginalFactorsMultipliedBack:true};
}
output.seconds=(Date.now()-start)/1000;return output;
