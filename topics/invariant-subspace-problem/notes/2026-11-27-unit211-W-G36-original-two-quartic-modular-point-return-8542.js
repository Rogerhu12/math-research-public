(function(){
"use strict";
const started=Date.now(),p=1009,k=422,Q=965;
let inverseCount=0;
function md(x){x%=p;return x<0?x+p:x;}
function pw(x,n){let a=1;while(n){if(n&1)a=md(a*x);x=md(x*x);n=Math.floor(n/2);}return a;}
function inv(x){x=md(x);if(!x)throw Error("zero scalar inverse");const y=pw(x,p-2);if(md(x*y)!==1)throw Error("inverse product");inverseCount++;return y;}
const div=(x,y)=>md(x*inv(y)),n=(x)=>md(x);
const e=div(Q,k),u=n(e+1),V=n(u*k+2),ell=div(n(u*(n((k+2)*(k+2))-2*e*k)),n(k*V));
const d=n(1-Q),m=n(u-ell),bc=div(n(ell*ell*d-m*m),4*d),M=n(4*bc*d);
const V2=n(2*u-ell*Q),T0=n(V2-2*u*u),J=n(2*u*(1-u)+ell*Q),Phi=n(T0+4*u-4+Q),Pf=n(T0*(J-Q)),P02=n((2-3*u)*V2-Q*u+2*u*u*u);
const namesPaid={k,nkp1:n(k+1),nkp2:n(k+2),nkp4:n(k+4),e,u,Q,V,d,ell,m,bc,P02,Phi,T0,JminusQ:n(J-Q)};
for(const [label,v] of Object.entries(namesPaid))if(!v)throw Error("paid zero "+label);
class P{
 constructor(v=0){this.a=new Map();if(v instanceof P){this.a=new Map(v.a);return;}if(v instanceof Map){for(const [kk,c] of v){const z=md(c);if(z)this.a.set(kk,z);}return;}if(md(v))this.a.set("0,0,0",md(v));}
 static mon(ex,c=1){return new P(new Map([[ex.join(","),c]]));}
 add(v){v=new P(v);const out=new Map(this.a);for(const [a,c] of v.a)out.set(a,md((out.get(a)||0)+c));return new P(out);}
 neg(){return new P(new Map([...this.a].map(([a,c])=>[a,md(-c)])));}
 sub(v){return this.add(new P(v).neg());}
 mul(v){v=new P(v);const out=new Map();for(const [a,c] of this.a){const aa=a.split(",").map(Number);for(const [b,h] of v.a){const bb=b.split(",").map(Number),key=aa.map((v,i)=>v+bb[i]).join(",");out.set(key,md((out.get(key)||0)+c*h));}}return new P(out);}
 scale(v){return new P(new Map([...this.a].map(([a,c])=>[a,md(c*v)])));}
 pow(j){let o=new P(1),v=this;while(j){if(j&1)o=o.mul(v);v=v.mul(v);j=Math.floor(j/2);}return o;}
 zero(){return this.a.size===0;}
 degree(){return Math.max(-1,...[...this.a.keys()].map(a=>a.split(",").map(Number).reduce((a,b)=>a+b,0)));}
 data(){return [...this.a].map(([a,c])=>[a.split(",").map(Number),c]).sort((a,b)=>a[0].join(",").localeCompare(b[0].join(",")));}
}
class R{
 constructor(a=0,b=0){if(a instanceof R){this.a=a.a;this.b=a.b;return;}this.a=new P(a);this.b=new P(b);}
 add(v){v=new R(v);return new R(this.a.add(v.a),this.b.add(v.b));}
 neg(){return new R(this.a.neg(),this.b.neg());}
 sub(v){return this.add(new R(v).neg());}
 mul(v){v=new R(v);return new R(this.a.mul(v.a).add(this.b.mul(v.b).scale(d)),this.a.mul(v.b).add(this.b.mul(v.a)));}
 scale(v){return new R(this.a.scale(v),this.b.scale(v));}
 pow(j){let o=new R(1),v=this;while(j){if(j&1)o=o.mul(v);v=v.mul(v);j=Math.floor(j/2);}return o;}
}
const X=P.mon([1,0,0]),Y=P.mon([0,1,0]),tt=P.mon([0,0,1]);
const f=X.scale(u).add(Y.scale(u-ell*Q)).sub(div(T0,2)).scale(inv(2*u));
const W2=X.scale(V2).add(Y.scale(2*u-u*Q-ell*Q));
const lam=W2.sub(u*T0).sub(f.scale(V2+2*u*u)).add(tt.scale(bc*Q)).scale(inv(P02));
const G=lam.scale(P02).sub((1-u)*T0);
const T=G.scale(T0).sub(f.scale(Pf)).sub(tt.scale(Phi*bc*Q)).scale(inv(Q*P02)).sub(ell);
const a=n(1-ell),br=div(m,2*d),b=new R(div(ell,2),br),c=new R(div(ell,2),-br),pp=new R(1,1),qq=new R(1,-1);
const XX=new R(X,Y),YY=new R(X,Y.neg()),tr=new R(tt);
const rr=XX.sub(pp.scale(a)).sub(c.mul(tr)),ss=YY.sub(qq.scale(a)).sub(b.mul(tr));
const Ag=new R(f.scale(2)).sub(b.mul(XX).scale(2)).sub(c.mul(YY).scale(2)).add(tr.scale(2*bc));
const rows=[[new R(),new R(),pp,qq],[new R(),Ag,rr,ss],[pp,rr,new R(),tr],[qq,ss,tr,new R()]];
const one=[new R(1),new R(),new R(1),new R(1)];
function vm(v,w){return [v[0].mul(w[0]),v[0].mul(w[1]).add(v[1].mul(w[0])),v[2].mul(w[2]),v[3].mul(w[3])];}
function vs(v,w){return v.map((z,i)=>z.sub(w[i]));}
function va(v,w){return v.map((z,i)=>z.add(w[i]));}
function sc(v,h){return v.map(z=>z.mul(h));}
function tau(v){return v[0].scale(a).add(v[1]).add(b.mul(v[2])).add(c.mul(v[3]));}
function DK(v){return rows.map(rr=>tau(vm(rr,v)));}
const dv=DK(one),F2=tau(dv);
if(!F2.sub(new R(f.scale(2))).a.zero()||!F2.b.zero())throw Error("F2 original");
const DKdv=DK(dv);
function mean(i){const eps=i===1?tau(vm(rows[0],rows[1])).scale(2):tau(vm(rows[i],rows[i]));return eps.sub(DKdv[i].scale(2)).sub(vm(dv,dv)[i].scale(2)).add(F2.mul(dv[i]).scale(2));}
const E0=mean(0);if(!E0.a.zero()||!E0.b.zero())throw Error("E0 reconstruction");
function N4(v){const tv=tau(v),vv=vm(v,v);return tau(vm(dv,vv)).scale(2).sub(F2.mul(tau(vv))).sub(tv.mul(tau(vm(dv,v))).scale(4)).add(F2.mul(tv.pow(2)).scale(2)).add(tau(vm(v,DK(v))));}
function P2(v){const vv=vs(v,sc(one,tau(v)));return tau(vm(vm(vv,vv),vv));}
const centered0=vs(rows[0],sc(one,tau(rows[0]))),centered1=vs(rows[1],sc(one,tau(rows[1])));
const Pj=tau(vm(vm(centered0,centered0),centered1)).scale(3);
const N1=N4(va(rows[0],rows[1])).sub(N4(rows[0])).sub(N4(rows[1])).sub(Pj.mul(new R(lam)).scale(div(4,3)));
const Al=lam.pow(2).scale(2).sub(lam.scale(2)).add(1),Bl=lam.pow(3).scale(4).sub(lam.pow(2).scale(6)).add(lam.scale(3)).sub(1);
const NS=b.mul(N4(rows[2])).add(c.mul(N4(rows[3]))).sub(new R(lam.mul(new P(ell).add(T.scale(2)).add(Al)).scale(2*P02)));
const PS=b.mul(P2(rows[2])).add(c.mul(P2(rows[3]))).sub(new R(new P(ell).add(T.scale(3)).add(Al.scale(3)).add(Bl).scale(P02)));
const E1=mean(1),EB=mean(2);
for(const [label,v] of [["E1",E1],["N1",N1],["NS",NS],["PS",PS]])if(!v.b.zero())throw Error("non scalar "+label);
const D=Al.scale(ell).sub(T.pow(2)),K=Bl.scale(ell*ell).sub(T.mul(Al).scale(3*ell)).add(T.pow(3).scale(2));
const cstar=new P(3).sub(lam.scale(2)),astar=n(4*u*Q-J),Cstar=n(astar*m*m+J*d*ell*ell);
const aD=new P(3).sub(lam.scale(4)).scale(M*ell*ell*Q).add(T.pow(2).scale(M*astar)).add(cstar.mul(T).scale(2*M*u*Q*ell)).add(D.scale(Cstar));
const bD=T.scale(astar).add(cstar.scale(u*Q*ell)).scale(2*M*m);
const R4=aD.pow(2).scale(M).sub(D.mul(bD.pow(2)));
const C4=D.mul(aD).scale(2*m).add(K.mul(bD));
const pols=[E1.a,EB.a,EB.b,N1.a,NS.a,PS.a,R4,C4],names=["E1","EBe","EBo","N1","NS","PS","R4","C4"],ds=[2,2,2,2,3,3,4,4];
const mons=[];for(let i=0;i<=5;i++)for(let j=0;j<=5-i;j++)for(let t=0;t<=5-i-j;t++)mons.push([i,j,t]);
mons.sort((a,b)=>b.reduce((a,b)=>a+b)-a.reduce((a,b)=>a+b)||b[1]-a[1]||b[0]-a[0]||b[2]-a[2]);
if(mons.length!==56||mons[55].join(",")!=="0,0,0")throw Error("monomial basis");
const index=new Map(mons.map((x,i)=>[x.join(","),i])),rawrows=[],labels=[];
for(let ni=0;ni<pols.length;ni++){
 if(pols[ni].degree()>ds[ni])throw Error("original degree "+names[ni]);
 const mult=mons.filter(m=>m.reduce((a,b)=>a+b,0)<=5-ds[ni]);
 for(const mm of mult){const prod=pols[ni].mul(P.mon(mm));const row=Array(56).fill(0);for(const [key,c]of prod.a){const j=index.get(key);if(j===undefined)throw Error("outside columns");row[j]=c;}rawrows.push(row);labels.push([names[ni],mm]);}
}
if(rawrows.length!==108)throw Error("rows");
const bases=[],tags=[],pivots=[];
for(let i=0;i<rawrows.length;i++){
 const row=rawrows[i].slice(),tag=Array(rawrows.length).fill(0);tag[i]=1;
 for(let b=0;b<bases.length;b++){const cf=row[pivots[b]];if(!cf)continue;for(let j=0;j<56;j++)row[j]=md(row[j]-cf*bases[b][j]);for(let j=0;j<tag.length;j++)tag[j]=md(tag[j]-cf*tags[b][j]);}
 const pv=row.findIndex(Boolean);if(pv<0)continue;
 const iv=inv(row[pv]);for(let j=0;j<56;j++)row[j]=md(row[j]*iv);for(let j=0;j<tag.length;j++)tag[j]=md(tag[j]*iv);
 for(let j=0;j<56;j++){let rr=0;for(let r=0;r<rawrows.length;r++)rr=md(rr+tag[r]*rawrows[r][j]);if(rr!==row[j])throw Error("whole basis combination "+j);}
 bases.push(row);tags.push(tag);pivots.push(pv);if(bases.length===56)break;
}
const target=Array(56).fill(0);target[55]=1;const rem=target.slice(),combination=Array(rawrows.length).fill(0);
for(let b=0;b<bases.length;b++){const cf=rem[pivots[b]];if(!cf)continue;for(let j=0;j<56;j++)rem[j]=md(rem[j]-cf*bases[b][j]);for(let j=0;j<combination.length;j++)combination[j]=md(combination[j]+cf*tags[b][j]);}
const unit=!rem.some(Boolean);
if(unit)for(let j=0;j<56;j++){let rr=0;for(let r=0;r<rawrows.length;r++)rr=md(rr+combination[r]*rawrows[r][j]);if(rr!==target[j])throw Error("constant one combination");}
return {prime:p,k,Q,e,u,ell,originalNames:names,originalDegrees:pols.map(z=>z.degree()),originalTerms:pols.map(z=>z.a.size),rows:108,columns:56,rank:bases.length,actualOriginalConstantOneReturned:unit,allBasisFiftySixColumnIdentitiesVerified:true,allUsedInverseProductsOne:true,inverseCount,elapsedMilliseconds:Date.now()-started,certificate:{labels,pivots,combination,remaining:rem},wholeQQHighExcluded:false,onlyPreviouslyUnresolvedModularPoint:true};
})()