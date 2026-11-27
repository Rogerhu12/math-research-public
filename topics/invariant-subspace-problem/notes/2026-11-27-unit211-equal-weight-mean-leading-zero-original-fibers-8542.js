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


const input=arguments[0],start=Date.now();
function cq(s){const a=s.split("/");return new Q(a[0],a[1]||1);}
function from(cs){let p=new P();for(const[e,c]of cs)p=p.add(P.term(e,cq(c)));return p;}
const m=P.term([1,0,0,0]),Qv=P.term([0,1,0,0]),y=P.term([0,0,1,0]),z=P.term([0,0,0,1]),one=new P(1),dd=one.sub(Qv),v=y.scale(2).sub(1);
const F=z.mul(dd).mul(v.pow(2)).add(m.sub(1).mul(dd.add(z.pow(2))).mul(v)).sub(z.mul(m.scale(2).sub(1)));
if(!from(input.rows.E1.coefficients).sub(from(input.rows.EBe.coefficients)).eq(m.sub(1).mul(F).scale(-2)))throw Error("original mean difference");
const aVar=P.term([1,0,0,0]),iv=P.term([-1,0,0,0]);
const branches={
 zero_z:[aVar,one.sub(iv),new P(new Q(1,2)),new P()],
 nonzero_z:[one.add(iv.pow(2)).scale(1,2),one.sub(aVar.pow(2)),one.add(iv).scale(1,2),aVar]
};
function evaluate(cs,values){let p=new P();for(const[e,c]of cs){let q=new P(cq(c));for(let i=0;i<4;i++)q=q.mul(values[i].pow(e[i]));p=p.add(q);}return p;}
function normalizedUnivariate(p){if(!p.c.size)return {clear:0,coefficients:[]};let min=Math.min(...Array.from(p.c.keys(),k=>+k.split(",")[0]));if(min<0)p=p.mul(aVar.pow(-min));const arr=Array.from({length:p.degree(0)+1},()=>new Q());for(const[e,c]of p.json()){if(e.slice(1).some(Boolean))throw Error("not univariate");arr[e[0]]=cq(c);}return {clear:Math.max(0,-min),coefficients:arr.map(c=>c.str())};}
const out={stage:"equal_weight_mean_difference_leading_zero_original_fibers",seconds:0,originalDifferenceIdentity:true,F:"z*d*v^2+(m-1)*(d+z^2)*v-z*(2m-1)",leadingInM:"(d+z^2)*v-2z",branches:{},excluded:false};
for(const[name,vals]of Object.entries(branches)){out.branches[name]={};for(const [row,r]of Object.entries(input.rows))out.branches[name][row]=normalizedUnivariate(evaluate(r.coefficients,vals));}
out.seconds=(Date.now()-start)/1000;return out;