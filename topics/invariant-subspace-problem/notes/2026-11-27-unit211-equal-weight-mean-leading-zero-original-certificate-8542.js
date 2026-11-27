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
function qparse(v){let a=v.split("/");return new Q(a[0],a[1]||1);}
const uz=()=>new Q(0),uo=()=>new Q(1);
function ut(p){p=p.slice();while(p.length&&!p[p.length-1].n)p.pop();return p;}
function ua(p,q){return ut(Array.from({length:Math.max(p.length,q.length)},(_,i)=>(p[i]||uz()).add(q[i]||uz())));}
function un(p){return p.map(x=>x.neg());}
function us(p,q){return ua(p,un(q));}
function um(p,q){let z=Array.from({length:Math.max(0,p.length+q.length-1)},uz);if(!p.length||!q.length)return [];for(let i=0;i<p.length;i++)for(let j=0;j<q.length;j++)z[i+j]=z[i+j].add(p[i].mul(q[j]));return ut(z);}
function uc(p,c){return ut(p.map(x=>x.mul(c)));}
function ud(p,q){p=ut(p);q=ut(q);if(!q.length)throw Error("zero polynomial divisor");const original=p.slice(),z=Array.from({length:Math.max(0,p.length-q.length+1)},uz);while(p.length>=q.length){const j=p.length-q.length,c=p[p.length-1].div(q[q.length-1]);z[j]=c;p=us(p,Array.from({length:j},uz).concat(uc(q,c)));}if(us(ua(um(z,q),p),original).length)throw Error("division return");return[ut(z),p];}
function ue(p,q){const [z,r]=ud(p,q);if(r.length)throw Error("not exact");return z;}
function ug(p,q){while(q.length){let r=ud(p,q)[1];p=q;q=r;}return p.length?uc(p,uo().div(p[p.length-1])):[];}
function ugx(p,q){let a=[uo()],b=[],c=[],d=[uo()];while(q.length){const[z,r]=ud(p,q);[p,q]=[q,r];[a,c]=[c,us(a,um(z,c))];[b,d]=[d,us(b,um(z,d))];}const sc=uo().div(p[p.length-1]);return[uc(p,sc),uc(a,sc),uc(b,sc)];}
function coeffM(poly){const out=Array.from({length:poly.degrees[1]+1},()=>[]);for(const[e,c]of poly.coefficients){while(out[e[1]].length<=e[0])out[e[1]].push(uz());out[e[1]][e[0]]=qparse(c);}return out.map(ut);}

const input=arguments[0],start=Date.now(),result={stage:"equal_weight_mean_head_zero_complete_univariate_returns",seconds:0,branches:{}};
for(const[name,branch]of Object.entries(input.branches)){
 const polys=Object.fromEntries(["N1","Ns","Ps"].map(k=>[k,branch[k].coefficients.map(qparse)]));
 let g=polys.N1,comb=[[uo()],[],[]],steps=[];
 for(const[name2,index]of [["Ns",1],["Ps",2]]){
  const[ng,a,b]=ugx(g,polys[name2]);if(us(ua(um(a,g),um(b,polys[name2])),ng).length)throw Error("original fiber Bezout");
  comb=comb.map(p=>um(a,p));comb[index]=ua(comb[index],b);g=ng;steps.push({row:name2,gcd:g.map(x=>x.str())});
 }
 if(us(ua(ua(um(comb[0],polys.N1),um(comb[1],polys.Ns)),um(comb[2],polys.Ps)),g).length)throw Error("original fiber combined return");
 result.branches[name]={gcd:g.map(x=>x.str()),steps,coefficientDegrees:comb.map(p=>p.length-1),combinedCoefficients:comb.map(p=>p.map(x=>x.str()))};
}
result.seconds=(Date.now()-start)/1000;return result;