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



const input=arguments[0],started=Date.now();
const m=P.term([1,0,0,0,0]),x=P.term([0,0,1,0,0]),y=P.term([0,0,0,1,0]),t=P.term([0,0,0,0,1]),a=x.sub(y),d=m.scale(2).sub(1);
function parse(row){let p=new P();for(const[e,c]of row.coefficients)p=p.add(P.term(e,new Q(...c.split("/"))));return p;}
const EB=parse(input.rows.EBe),N=parse(input.rows.N1),f1=m.mul(t).sub(a.scale(2)),f2=m.mul(t).sub(d.mul(a).scale(2));
if(!N.eq(f1.mul(f2)))throw Error("original factor");
for(const [r,remainder]of [[new P(1),m.sub(1).mul(a).mul(m.mul(y.scale(2).add(1)).sub(a)).scale(4)],[d,d.mul(m.sub(1)).mul(a).mul(a.add(m)).scale(4)]]){
 const linear=m.mul(t).sub(r.mul(a).scale(2)),quotient=m.mul(t).add(r.mul(a).scale(2)).add(m.mul(m.sub(1).sub(x)).scale(2));
 if(!m.mul(EB).sub(linear.mul(quotient)).eq(remainder))throw Error("original singleton mean trace");
}
return{stage:"T0zero_original_N_and_mean_factor_trace",seconds:(Date.now()-started)/1000,N1FactorVerified:true,bothFullOriginalMeanIdentitiesVerified:true,cover:["x=y,t=0","x-y=m(1+2y),t=2(1+2y)","x-y=-m,t=-2(2m-1)"]};
