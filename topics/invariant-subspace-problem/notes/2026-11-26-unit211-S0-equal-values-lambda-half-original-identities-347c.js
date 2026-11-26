(()=>{
"use strict";
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let r=a%b;a=b;b=r}return a}
class Q{
 constructor(n,d=1n){if(n instanceof Q){this.n=n.n;this.d=n.d;return}n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero rational denominator");if(d<0n){n=-n;d=-d}const g=gcd(n,d);this.n=n/g;this.d=d/g}
 add(v){v=new Q(v);return new Q(this.n*v.d+v.n*this.d,this.d*v.d)}
 neg(){return new Q(-this.n,this.d)}
 sub(v){return this.add(new Q(v).neg())}
 mul(v){v=new Q(v);return new Q(this.n*v.n,this.d*v.d)}
 eq(v){v=new Q(v);return this.n===v.n&&this.d===v.d}
 str(){return this.n.toString()+"/"+this.d.toString()}
}
let products=0,identities=0;
class P{
 constructor(v=0){if(v instanceof P){this.m=new Map(v.m);return}this.m=new Map();let q=new Q(v);if(q.n)this.m.set("0,0,0",q)}
 static mono(e,v=1){let p=new P();let q=new Q(v);if(q.n)p.m.set(e.join(","),q);return p}
 add(v){v=new P(v);let p=new P(this);for(const[k,q]of v.m){let z=(p.m.get(k)||new Q(0)).add(q);if(z.n)p.m.set(k,z);else p.m.delete(k)}return p}
 neg(){let p=new P();for(const[k,q]of this.m)p.m.set(k,q.neg());return p}
 sub(v){return this.add(new P(v).neg())}
 mul(v){v=new P(v);let p=new P();products++;for(const[k,q]of this.m)for(const[j,r]of v.m){let a=k.split(",").map(Number),b=j.split(",").map(Number),key=a.map((x,i)=>x+b[i]).join(",");let z=(p.m.get(key)||new Q(0)).add(q.mul(r));if(z.n)p.m.set(key,z);else p.m.delete(key)}return p}
 pow(n){let p=new P(1);for(let i=0;i<n;i++)p=p.mul(this);return p}
 eq(v){return this.sub(v).m.size===0}
 serial(){return [...this.m].sort((a,b)=>a[0].localeCompare(b[0])).map(([m,q])=>m+":"+q.str()).join(";")}
}
function check(a,b,label){identities++;if(!new P(a).eq(b))throw Error("original identity failed: "+label)}
const b=P.mono([1,0,0]),q=P.mono([0,1,0]),t=P.mono([0,0,1]);
const H=new P(new Q(1,2)),c=H.sub(b),delta=q.sub(1),sigma=q.add(1),u=b.add(c.mul(q)),W=c.add(b.mul(q)).mul(2);
const zero=new P(),one=new P(1);
const rows=[
 [zero,zero,delta,delta.mul(q)],
 [zero,zero,c.mul(t),b.mul(q).mul(t).neg()],
 [delta,c.mul(t),zero,delta.mul(t)],
 [delta.mul(q),b.mul(q).mul(t).neg(),delta.mul(t),zero]];
function add(v,z){return v.map((x,i)=>x.add(z[i]))}
function scale(a,v){a=new P(a);return v.map(x=>a.mul(x))}
function mul(v,z){return [v[0].mul(z[0]),v[0].mul(z[1]).add(v[1].mul(z[0])),v[2].mul(z[2]),v[3].mul(z[3])]}
function tau(v){return H.mul(v[0]).add(v[1]).add(b.mul(v[2])).add(c.mul(v[3]))}
const unit=[one,zero,one,one];
function DK(v){return rows.map(r=>tau(mul(r,v)))}
const d=DK(unit),F2=tau(d),Dd=DK(d),d2=mul(d,d);
check(F2,delta.mul(u),"the original half-mean graph");
function mean(j){let e=j===1?tau(mul(rows[0],rows[1])).mul(2):tau(mul(rows[j],rows[j]));return e.sub(Dd[j].mul(2)).sub(d2[j].mul(2)).add(F2.mul(d[j]).mul(2))}
function center(v){return add(v,scale(tau(v).neg(),unit))}
function P2(v){let x=center(v);return tau(mul(mul(x,x),x))}
function Pjet2(v,z){let x=center(v),y=center(z);return tau(mul(mul(x,x),y)).mul(3)}
function N4(v){return tau(mul(d,mul(v,v))).mul(2).sub(F2.mul(tau(mul(v,v)))).sub(tau(v).mul(tau(mul(d,v))).mul(4)).add(F2.mul(tau(v).pow(2)).mul(2)).add(tau(mul(v,DK(v))))}
const V=[one,zero,zero,zero],V2=b.add(c.mul(q.pow(2))),P02=b.add(c.mul(q.pow(3))).sub(u.mul(V2).mul(3)).add(u.pow(3).mul(2));
check(mean(0),zero,"original E0");
check(P2(rows[0]),delta.pow(3).mul(P02),"original P0");
check(N4(rows[0]),delta.pow(3).mul(P02),"original N0=P0/2");
check(P2(V),zero,"original P(V)");
check(N4(V),zero,"original N(V)");
const EBcoef=delta.pow(2).add(b.mul(delta).mul(2)).sub(c.mul(q.pow(2)).mul(2));
const ECcoef=delta.pow(2).sub(c.mul(q).mul(delta).mul(2)).sub(b.mul(2));
const E1=mean(1),EB=mean(2),EC=mean(3),PJ=Pjet2(rows[0],rows[1]);
check(E1,b.mul(c).mul(t).mul(delta.pow(2).mul(u.mul(2).sub(sigma)).sub(q.mul(t))),"original first jet mean");
check(EB,c.mul(t).mul(delta.pow(2).mul(c.mul(2).add(b.mul(q))).mul(-2).add(t.mul(EBcoef))),"original B mean");
check(EC,b.mul(t).mul(delta.pow(2).mul(c.add(b.mul(q).mul(2))).mul(-2).add(t.mul(ECcoef))),"original C mean");
const g=W.pow(2).add(sigma.mul(W)).sub(q);
check(PJ,delta.pow(3).mul(b).mul(c).mul(t).mul(g).mul(new Q(-3,2)),"original P1");
check(u.mul(2).sub(sigma),W.neg(),"E1 solves q*t=-delta^2*W");
const AB=W.pow(2).mul(q.pow(2).add(q).sub(1)).sub(q.pow(2).mul(W).mul(2)).add(q.pow(2));
const AC=W.pow(2).mul(q.pow(2).sub(q).sub(1)).add(q.mul(W).mul(2)).sub(q.pow(2));
check(delta.mul(q.mul(c.mul(2).add(b.mul(q))).mul(2).add(W.mul(EBcoef))),AB,"B mean after E1");
check(delta.mul(q.mul(c.add(b.mul(q).mul(2))).mul(2).add(W.mul(ECcoef))),AC,"C mean after E1");
check(AB.sub(AC),q.mul(W.pow(2).sub(sigma.mul(W)).add(q)).mul(2),"paired original means");
check(g.add(W.pow(2).sub(sigma.mul(W)).add(q)),W.pow(2).mul(2),"W squared is zero");
return {status:"all_exact_original_half_collision_identities_verified",rationalPolynomialIdentities:identities,polynomialProducts:products,variables:["b","q","t"],paidUnits:["b","c=1/2-b","q","q-1"],tZeroRequiresOriginalFullFiveColumnGramRank:true,tNonzeroContradiction:"g=0 and AB-AC=0 imply W^2=0, then q=0",fullGramAtTzero:"[[0,0,1,q,U0],[0,0,0,0,0],[1,0,0,0,0],[q,0,0,0,0],[U0,0,0,0,0]]",physicalRank:2,physicalRequiredMinimumRank:4,claimOriginalHalfCollisionExcluded:true,claimWholeS0LayerEmpty:false,originalInput:[E1.serial(),EB.serial(),EC.serial(),PJ.serial()]};
})()
