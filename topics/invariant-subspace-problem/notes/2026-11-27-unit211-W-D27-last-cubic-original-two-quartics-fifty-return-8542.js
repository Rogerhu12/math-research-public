/* Last D27/F782 residue: exact original 50x35 over F_1009[k]/(k^3+7k^2+14k+12).
 * e=-1-758k-757k^2 is the already retained e-linear branch.
 * Rebuild the original Gram, actual double-point algebra, original value moments,
 * original Delta line and both new quartic original combinations.
 * No earlier successful residue is rerun; no physical D inverse is used.
 */
(() => {
const begin=Date.now(),p=1009;
let inverseCount=0;
const mod=x=>{x%=p;return x<0?x+p:x;};
class F{
 constructor(v=0){if(v instanceof F){this.a=v.a.slice();return;}
 this.a=Array.isArray(v)?[mod(v[0]||0),mod(v[1]||0),mod(v[2]||0)]:[mod(v),0,0];}
 add(v){v=new F(v);return new F(this.a.map((c,j)=>mod(c+v.a[j])));}
 neg(){return new F(this.a.map(c=>mod(-c)));}
 sub(v){return this.add(new F(v).neg());}
 mul(v){v=new F(v);const c=Array(5).fill(0);for(let i=0;i<3;i++)for(let j=0;j<3;j++)c[i+j]=mod(c[i+j]+this.a[i]*v.a[j]);
 for(let j=4;j>=3;j--){const a=c[j];c[j]=0;c[j-1]=mod(c[j-1]-7*a);c[j-2]=mod(c[j-2]-14*a);c[j-3]=mod(c[j-3]-12*a);}
 return new F(c);}
 pow(n){let a=this,r=new F(1);for(;n;n=Math.floor(n/2)){if(n%2)r=r.mul(a);if(n>1)a=a.mul(a);}return r;}
 zero(){return this.a.every(c=>c===0);}
 eq(v){return this.sub(v).zero();}
 inv(){if(this.zero())throw Error("zero scalar inverse");const r=this.pow(p*p*p-2);if(!this.mul(r).eq(1))throw Error("nonunit scalar, cannot discard");inverseCount++;return r;}
 div(v){return this.mul(new F(v).inv());}
}
const ZERO="0,0,0,0";
class P{
 constructor(v=0){this.t=new Map();if(v instanceof P){this.t=new Map(v.t);return;}
 v=new F(v);if(!v.zero())this.t.set(ZERO,v);}
 static variable(j){const r=new P(),m=[0,0,0,0];m[j]=1;r.t.set(m.join(","),new F(1));return r;}
 add(v){v=new P(v);const r=new P(this);for(const [m,c]of v.t){const z=(r.t.get(m)||new F()).add(c);if(z.zero())r.t.delete(m);else r.t.set(m,z);}return r;}
 neg(){const r=new P();for(const [m,c]of this.t)r.t.set(m,c.neg());return r;}
 sub(v){return this.add(new P(v).neg());}
 mul(v){v=new P(v);const r=new P();for(const [ma,ca]of this.t){const a=ma.split(",").map(Number);for(const [mb,cb]of v.t){const b=mb.split(",").map(Number),key=a.map((x,j)=>x+b[j]).join(","),z=(r.t.get(key)||new F()).add(ca.mul(cb));if(z.zero())r.t.delete(key);else r.t.set(key,z);}}return r;}
 scale(v){v=new F(v);const r=new P();if(v.zero())return r;for(const [m,c]of this.t){const z=c.mul(v);if(!z.zero())r.t.set(m,z);}return r;}
 pow(n){let r=new P(1);for(let j=0;j<n;j++)r=r.mul(this);return r;}
 eq(v){return this.sub(v).t.size===0;}
 zero(){return this.t.size===0;}
 degree(){return Math.max(-1,...[...this.t.keys()].map(m=>m.split(",").reduce((s,x)=>s+Number(x),0)));}
 data(){return [...this.t].sort((a,b)=>a[0].localeCompare(b[0])).map(([m,c])=>[m.split(",").map(Number),c.a]);}
}
const k=new F([0,1,0]),e=new F([1008,251,252]),u=e.add(1),Q=e.mul(k),V=u.mul(k).add(2);
const f3=k.pow(3).add(k.pow(2).mul(7)).add(k.mul(14)).add(12);
if(!f3.zero())throw Error("k cover not returned");
const kp=k.pow(p),frobeniusInverse=kp.sub(k).inv();
if(!k.pow(p*p*p).eq(k)||!kp.sub(k).mul(frobeniusInverse).eq(1))throw Error("complete degree-three finite-field criterion failed");
const ell=u.mul(k.add(2).pow(2).sub(e.mul(k).mul(2))).div(k.mul(V));
const d=new F(1).sub(Q),bc=ell.pow(2).sub(u.sub(ell).pow(2).div(d)).div(4);
const V2=u.mul(2).sub(ell.mul(Q)),T0=V2.sub(u.pow(2).mul(2));
const P02=new F(2).sub(u.mul(3)).mul(V2).sub(Q.mul(u)).add(u.pow(3).mul(2));
const J=u.mul(new F(1).sub(u)).mul(2).add(ell.mul(Q)),Phi=T0.add(u.mul(4)).sub(4).add(Q);
const Pf=T0.mul(J.sub(Q)),M=ell.mul(V2).sub(u.pow(2));
const Hp=e.mul(k).mul(4).sub(k.pow(2)).sub(k.mul(4)).sub(8);
const C9=e.pow(2).mul(k.pow(2)).mul(4).sub(e.mul(k.pow(4).add(k.pow(3).mul(9)).add(k.pow(2).mul(20)).add(k.mul(16))))
 .add(k.pow(3)).add(k.pow(2).mul(10)).add(k.mul(24)).add(16);
const J19=e.pow(4).mul(k.pow(3)).mul(16)
 .add(e.pow(3).mul(k.pow(4).mul(-8).sub(k.pow(3).mul(16)).sub(k.pow(2).mul(96))))
 .add(e.pow(2).mul(k.pow(5).neg().sub(k.pow(4).mul(8)).add(k.pow(3).mul(24)).add(k.pow(2).mul(64)).add(k.mul(192))))
 .add(e.mul(k.pow(5).mul(-2).sub(k.pow(4).mul(14)).sub(k.pow(3).mul(12)).sub(128)))
 .sub(k.pow(5)).sub(k.pow(4).mul(10)).sub(k.pow(3).mul(40)).sub(k.pow(2).mul(104)).sub(k.mul(160)).sub(128);
const Fco=[
 k.pow(6).neg().sub(k.pow(5).mul(18)).sub(k.pow(4).mul(120)).sub(k.pow(3).mul(440)).sub(k.pow(2).mul(1008)).sub(k.mul(1344)).sub(768),
 k.pow(5).mul(-10).sub(k.pow(4).mul(28)).add(k.pow(3).mul(48)).add(k.pow(2).mul(64)).sub(k.mul(512)).sub(768),
 k.pow(6).mul(3).add(k.pow(5).mul(8)).add(k.pow(4).mul(60)).add(k.pow(3).mul(384)).add(k.pow(2).mul(1088)).add(k.mul(1024)),
 k.pow(6).mul(2).sub(k.pow(5).mul(12)).sub(k.pow(4).mul(96)).sub(k.pow(3).mul(384)).sub(k.pow(2).mul(384)),
 k.pow(5).mul(-4).add(k.pow(4).mul(32)),k.pow(4).mul(16)];
let jf=new F();for(let i=0;i<Fco.length;i++)jf=jf.add(Fco[i].mul(e.pow(i)));
if(!jf.zero()||!M.eq(bc.mul(d).mul(4))||!Phi.mul(J.sub(u.mul(Q).mul(2))).eq(Pf))throw Error("original weight identities failed");
const paid=[["k",k],["k+1",k.add(1)],["k+2",k.add(2)],["k+4",k.add(4)],["e",e],["u",u],["Q",Q],["V",V],["d",d],["bc",bc],["P02",P02],["Phi",Phi],["ell",ell],["ell-u",ell.sub(u)],["Q-2",Q.sub(2)],["u-Q",u.sub(Q)],["H",Hp],["C9",C9],["2e+1",e.mul(2).add(1)],["T0",T0],["J-Q",J.sub(Q)],["J19",J19],["M",M]];
for(const [name,val]of paid){if(val.zero()||!val.mul(val.inv()).eq(1))throw Error("unpaid zero fiber "+name);}
class E{
 constructor(a=0,b=0){if(a instanceof E){this.a=new P(a.a);this.b=new P(a.b);}else{this.a=new P(a);this.b=new P(b);}}
 add(v){v=new E(v);return new E(this.a.add(v.a),this.b.add(v.b));}
 neg(){return new E(this.a.neg(),this.b.neg());}
 sub(v){return this.add(new E(v).neg());}
 mul(v){v=new E(v);return new E(this.a.mul(v.a).add(this.b.mul(v.b).scale(d)),this.a.mul(v.b).add(this.b.mul(v.a)));}
 scale(v){return new E(this.a.scale(v),this.b.scale(v));}
 pow(n){let r=new E(1);for(let i=0;i<n;i++)r=r.mul(this);return r;}
 conj(){return new E(this.a,this.b.neg());}
 eq(v){v=new E(v);return this.a.eq(v.a)&&this.b.eq(v.b);}
}
const B=new E(ell.div(2),u.sub(ell).div(d.mul(2))),C=B.conj();
const pp=new E(1,1),qq=pp.conj(),aw=new F(1).sub(ell);
if(!B.mul(C).eq(new E(bc))||!B.mul(pp).add(C.mul(qq)).eq(new E(u)))throw Error("quadratic spectral algebra identities failed");
const [x,y,t,s]=[0,1,2,3].map(j=>P.variable(j)),X=new E(x,y),Y=X.conj();
const f=x.scale(u).add(y.scale(u.sub(ell.mul(Q)))).sub(new P(T0.div(2))).scale(u.mul(2).inv());
const lam=x.scale(V2).add(y.scale(u.mul(2).sub(u.mul(Q)).sub(ell.mul(Q)))).sub(new P(u.mul(T0)))
 .sub(f.scale(V2.add(u.pow(2).mul(2)))).add(t.scale(bc.mul(Q))).scale(P02.inv());
const G=lam.scale(P02).sub(new P(new F(1).sub(u).mul(T0)));
const T=G.scale(T0).sub(f.scale(Pf)).sub(t.scale(Phi.mul(bc).mul(Q))).scale(Q.mul(P02).inv()).sub(new P(ell));
const rg=X.sub(pp.scale(aw)).sub(C.mul(new E(t))),sg=Y.sub(qq.scale(aw)).sub(B.mul(new E(t)));
const ag=new E(f.scale(2)).sub(B.mul(X).scale(2)).sub(C.mul(Y).scale(2)).add(new E(t.scale(bc.mul(2))));
const gram=[[new E(),new E(),pp,qq],[new E(),ag,rg,sg],[pp,rg,new E(),new E(t)],[qq,sg,new E(t),new E()]];
const unit=[new E(1),new E(),new E(1),new E(1)];
const va=(v,z)=>v.map((a,i)=>a.add(z[i])),vs=(a,v)=>v.map(b=>new E(a).mul(b));
const vm=(v,z)=>[v[0].mul(z[0]),v[0].mul(z[1]).add(v[1].mul(z[0])),v[2].mul(z[2]),v[3].mul(z[3])];
const tau=v=>v[0].scale(aw).add(v[1]).add(B.mul(v[2])).add(C.mul(v[3]));
const DK=v=>gram.map(row=>tau(vm(row,v)));
const dv=DK(unit),F2=tau(dv),Kd=DK(dv),dv2=vm(dv,dv);
if(!F2.eq(new E(f.scale(2))))throw Error("original f return failed");
function mean(j){const first=j===1?tau(vm(gram[0],gram[1])).scale(2):tau(vm(gram[j],gram[j]));
 return first.sub(Kd[j].scale(2)).sub(dv2[j].scale(2)).add(F2.mul(dv[j]).scale(2));}
function N4(v){return tau(vm(dv,vm(v,v))).scale(2).sub(F2.mul(tau(vm(v,v))))
 .sub(tau(v).mul(tau(vm(dv,v))).scale(4)).add(F2.mul(tau(v).pow(2)).scale(2)).add(tau(vm(v,DK(v))));}
function P2(v){const centered=va(v,vs(tau(v).neg(),unit));return tau(vm(vm(centered,centered),centered));}
if(!mean(0).eq(0))throw Error("original E0 return failed");
const vc=va(gram[0],vs(tau(gram[0]).neg(),unit)),zc=va(gram[1],vs(tau(gram[1]).neg(),unit));
const Pj=tau(vm(vm(vc,vc),zc)).scale(3);
if(!N4(gram[0]).eq(new E(lam.scale(P02.mul(2))))||!Pj.eq(new E(lam.sub(1).sub(T).scale(P02.mul(3))))||!P2(gram[0]).eq(new E(P02)))throw Error("original N0/P1 return failed");
const N1=N4(va(gram[0],gram[1])).sub(N4(gram[0])).sub(N4(gram[1])).sub(new E(lam.scale(new F(4).div(3))).mul(Pj));
const Al=lam.pow(2).scale(2).sub(lam.scale(2)).add(1),Bl=lam.pow(3).scale(4).sub(lam.pow(2).scale(6)).add(lam.scale(3)).sub(1);
const NS=B.mul(N4(gram[2])).add(C.mul(N4(gram[3]))).sub(new E(lam.mul(new P(ell).add(T.scale(2)).add(Al)).scale(P02.mul(2))));
const PS=B.mul(P2(gram[2])).add(C.mul(P2(gram[3]))).sub(new E(new P(ell).add(T.scale(3)).add(Al.scale(3)).add(Bl).scale(P02)));
const E1=mean(1),EB=mean(2);
if(!E1.b.zero()||!EB.conj().eq(mean(3))||!N1.b.zero()||!NS.b.zero()||!PS.b.zero())throw Error("original spectral cancellation failed");
const m=u.sub(ell),D=Al.scale(ell).sub(T.pow(2)),K=Bl.scale(ell.pow(2)).sub(T.mul(Al).scale(ell.mul(3))).add(T.pow(3).scale(2));
const v0=T.add(s.scale(m)).scale(ell.inv()),v1=s.neg(),zeta=T.add(s.scale(u)).scale(ell.inv());
const h=new E(v0.add(1),v1),ku=h.conj(),wval=lam.sub(1).sub(T),Vval=[new E(1),new E(wval),h,ku];
const E2=tau(vm(Vval,Vval)).sub(new E(lam.pow(2).scale(2)));
const E3=tau(vm(vm(Vval,Vval),Vval)).sub(new E(lam.pow(3).scale(4)));
const q=s.pow(2).scale(M).sub(D),H=K.sub(D.mul(s).scale(m.mul(2)));
if(!tau(Vval).eq(new E(lam))||!E2.b.zero()||!E3.b.zero()||!E2.a.scale(ell).eq(q))throw Error("original value first/second moments failed");
if(!s.scale(m.mul(2)).add(new P(ell.mul(3))).add(T.scale(3)).mul(E2.a).scale(ell).sub(E3.a.scale(ell.pow(2))).eq(H))throw Error("original third moment identity failed");
const zv=h.sub(1).mul(ku.sub(1));if(!zv.b.zero())throw Error("z value parity failed");
const S=v0.scale(2).add(3).sub(lam.scale(2));
const Nf=new P(3).sub(lam.scale(4)).scale(Q).sub(zv.a.scale(J))
 .add(S.mul(v1.scale(u.mul(Q).mul(2)).add(zeta.scale(J))));
const Nt=S.mul(zeta).scale(bc.mul(Q));
const R1=new P(3).sub(lam.scale(2)).add(v0).add(v1).scale(u).sub(v1.scale(ell.mul(Q)));
const Nc=G.mul(zv.a.sub(S.mul(zeta))).add(S.mul(v1).scale(Q.mul(T0).div(2))).add(wval.mul(R1).scale(Q));
const Pc=new P(ell).add(T).scale(Q.mul(P02)).sub(G.scale(T0));
if(!f.scale(Pf).add(t.scale(bc.mul(Q).mul(Phi))).add(Pc).zero())throw Error("full original P1 failed");
const Nv=N4(Vval);
if(!Nv.b.zero()||!Nv.a.scale(Q.div(2)).eq(Nf.mul(f).add(Nt.mul(t)).add(Nc).sub(f.mul(E2.a).scale(Q))))throw Error("full original N4(V) correction failed");
const Edelta=Nf.scale(Phi).sub(S.mul(zeta).scale(Pf));
const simplified=new P(3).sub(lam.scale(4)).scale(Q).sub(zv.a.scale(J)).add(S.mul(v0).scale(u.mul(Q).mul(2)));
if(!Edelta.eq(simplified.scale(Phi)))throw Error("whole W original Delta identity failed");
const c=new P(3).sub(lam.scale(2)),astar=u.mul(Q).mul(4).sub(J),cstar=astar.mul(m.pow(2)).add(J.mul(d).mul(ell.pow(2)));
const ad=new P(3).sub(lam.scale(4)).scale(M.mul(ell.pow(2)).mul(Q)).add(T.pow(2).scale(M.mul(astar)))
 .add(c.mul(T).scale(M.mul(u).mul(Q).mul(ell).mul(2))).add(D.scale(cstar));
const bd=T.scale(astar).add(c.scale(u.mul(Q).mul(ell))).scale(M.mul(m).mul(2));
const R4=ad.pow(2).scale(M).sub(D.mul(bd.pow(2))),C4=D.mul(ad).scale(m.mul(2)).add(K.mul(bd));
const Zdelta=Edelta.scale(ell.pow(2).div(Phi));
if(!Zdelta.scale(M).sub(q.scale(cstar)).eq(ad.add(bd.mul(s))))throw Error("same-s original linear identity failed");
const minus=ad.sub(bd.mul(s));
if(!R4.scale(Phi).eq(minus.mul(Edelta).scale(M.pow(2).mul(ell.pow(2))).add(bd.pow(2).sub(minus.scale(M.mul(cstar))).mul(q).scale(Phi))))throw Error("R4 original combination failed");
if(!C4.scale(Phi).eq(D.mul(Edelta).scale(m.mul(M).mul(ell.pow(2)).mul(2)).sub(D.mul(q).scale(m.mul(cstar).mul(Phi).mul(2))).add(bd.mul(H).scale(Phi))))throw Error("C4 original combination failed");
const originals=[E1.a,EB.a,EB.b,N1.a,NS.a,PS.a,R4,C4],names=["E1","EBe","EBo","N1","NS","PS","Delta_second_moment_R4","Delta_third_moment_C4"];
for(let i=0;i<originals.length;i++)for(const [mm]of originals[i].t){const a=mm.split(",").map(Number);if(a[3]!==0||a[0]+a[1]+a[2]>(i<4?2:i<6?3:4))throw Error("original geometric degree failed");}
const mons=[];for(let i=0;i<=4;i++)for(let j=0;j<=4-i;j++)for(let h=0;h<=4-i-j;h++)mons.push([i,j,h,0]);
mons.sort((a,b)=>{const sa=a[0]+a[1]+a[2],sb=b[0]+b[1]+b[2];return sb-sa||b[1]-a[1]||b[0]-a[0]||b[2]-a[2];});
if(mons.length!==35||mons[34].join(",")!==ZERO)throw Error("complete original columns failed");
const mi=new Map(mons.map((m,i)=>[m.join(","),i])),rows=[],labels=[];
for(let i=0;i<originals.length;i++){
 const deg=i<4?2:i<6?3:4;
 const multipliers=mons.filter(m=>m[0]+m[1]+m[2]<=4-deg);
 for(const mm of multipliers){const row=mons.map(()=>new F());
 for(const [mon,cf]of originals[i].t){const m=mon.split(",").map(Number),key=m.map((x,j)=>x+mm[j]).join(","),col=mi.get(key);if(col===undefined)throw Error("omitted original column");row[col]=row[col].add(cf);}
 rows.push(row);labels.push([names[i],mm]);}
}
if(rows.length!==50)throw Error("complete original fifty rows failed");
const basis=[],pivots=[],tags=[];
function accumulate(tag,ii,v){const c=(tag.get(ii)||new F()).add(v);if(c.zero())tag.delete(ii);else tag.set(ii,c);}
for(let ri=0;ri<rows.length;ri++){
 let row=rows[ri].map(v=>new F(v)),tag=new Map([[ri,new F(1)]]);
 for(let bi=0;bi<basis.length;bi++){const c=row[pivots[bi]];if(c.zero())continue;
 row=row.map((v,j)=>v.sub(c.mul(basis[bi][j])));for(const [ii,v]of tags[bi])accumulate(tag,ii,c.mul(v).neg());}
 const pv=row.findIndex(v=>!v.zero());if(pv<0)continue;
 const inv=row[pv].inv();row=row.map(v=>v.mul(inv));tag=new Map([...tag].map(([j,v])=>[j,v.mul(inv)]));
 if(!row[pv].eq(1)||pivots.some(j=>!row[j].zero()))throw Error("original pivot inverse failed");
 for(let j=0;j<35;j++){let actual=new F();for(const [ii,v]of tag)actual=actual.add(v.mul(rows[ii][j]));if(!actual.eq(row[j]))throw Error("basis original column product failed");}
 basis.push(row);pivots.push(pv);tags.push(tag);if(basis.length===35)break;
}
let rem=mons.map((_,j)=>new F(j===34?1:0)),unitTag=new Map();
for(let bi=0;bi<basis.length;bi++){const c=rem[pivots[bi]];if(c.zero())continue;rem=rem.map((v,j)=>v.sub(c.mul(basis[bi][j])));for(const [ii,v]of tags[bi])accumulate(unitTag,ii,c.mul(v));}
const unitReturned=rem.every(v=>v.zero());
for(let j=0;j<35;j++){let actual=rem[j];for(const [ii,v]of unitTag)actual=actual.add(v.mul(rows[ii][j]));if(!actual.eq(j===34?1:0))throw Error("original full target product failed");}
const encodeTag=tag=>[...tag].sort((a,b)=>a[0]-b[0]).map(([i,v])=>[i,v.a]);
const certificate={prime:p,kModulus:[12,14,7,1],e:[1008,251,252],allOriginalRows:originals.map(po=>po.data()),columns:mons,labels,pivots,allBasisOriginalCombinationTags:tags.map(encodeTag),originalConstantOneTag:encodeTag(unitTag),targetRemainder:rem.map(v=>v.a)};
return {receipt:{schema:"isp-D27-last-Fq3-original-two-quartics-fifty-by-thirty-five-v1",
 prime:p,kFactorIndex:11,kDegree:3,eDegree:1,kModulus:[12,14,7,1],eCoefficients:[1008,251,252],
 completeOriginalThreeDimensionalConstantField:true,finiteFieldFrobeniusAndInverseActuallyVerified:true,
 D27FiveTermAndLeadingTermAllActuallyReturned:true,allPaidOriginalWeightInverseProductsOne:true,
 originalE0N0P1AndDoublePointGramActuallyRebuilt:true,originalSixGramRowsActuallyReturned:true,
 fullOriginalN4VSecondMomentCorrectionActuallyReturned:true,originalDeltaIdentityActuallyReturned:true,
 originalFirstSecondThirdMomentsActuallyReturned:true,
 bothNewQuarticOriginalCombinationIdentitiesActuallyReturned:true,
 originalRows:50,originalColumns:35,rank:basis.length,pivots,
 everyBasisRowAllThirtyFiveOriginalColumnProductsActuallyVerified:true,
 constantOneActuallyAttempted:true,constantOneActuallyReturned:unitReturned,
 targetAllThirtyFiveOriginalColumnProductsActuallyVerified:true,
 allActualScalarInversesMultipliedBackToOne:true,actualInverseCount:inverseCount,
 noPhysicalDOrNormInverse:true,oldSuccessfulFibersNotRerun:true,
 onlyThisPreviouslyUnreturnedModularFiberConsidered:true,
 fullQQD27ExclusionNotIndependentlyClaimed:true,claimExcluded:false,
 originalRowsProfiles:originals.map((po,j)=>({name:names[j],degree:po.degree(),terms:po.t.size})),
 elapsedMilliseconds:Date.now()-begin},
 certificate};
})()
