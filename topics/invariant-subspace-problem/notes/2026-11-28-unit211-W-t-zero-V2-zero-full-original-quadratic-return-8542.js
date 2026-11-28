/* NEW exact original Gram return on W,t=0,V2=0.
Self-contained rational arithmetic over QQ(u), retaining the ENTIRE
z^2=(2ell-1) algebra and rho^2=1-Q, including both z/rho signs.
Correct jet product v1*w0+v0*w1, no compact-R2 source.
No old determinant/Popov/finite gate is repeated. */
const start=Date.now(); let qops=0, pops=0, rchecks=0;
function igcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;}
function Q(a=0n,b=1n){if(Array.isArray(a)){b=a[1];a=a[0];}else a=BigInt(a);b=BigInt(b);if(!b)throw Error('zero rational denominator');if(!a)return [0n,1n];if(b<0n){a=-a;b=-b;}const g=igcd(a,b);return[a/g,b/g];}
function qa(a,b){qops++;return Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);}
function qn(a){return[-a[0],a[1]];}function qs(a,b){return qa(a,qn(b));}
function qm(a,b){qops++;return Q(a[0]*b[0],a[1]*b[1]);}
function qi(a){if(!a[0])throw Error('zero rational inverse');return Q(a[1],a[0]);}
function qd(a,b){return qm(a,qi(b));}
function qt(a){return a[1]===1n?String(a[0]):String(a[0])+'/'+String(a[1]);}
function trim(a){while(a.length&&!a[a.length-1][0])a.pop();return a;}
function pp(a){return trim(a.map(x=>Q(x)));}
const P0=[],P1=[Q(1)];
function pa(a,b){pops++;const r=[];for(let i=0;i<Math.max(a.length,b.length);i++)r.push(qa(a[i]||Q(),b[i]||Q()));return trim(r);}
function pn(a){return a.map(qn);}function ps(a,b){return pa(a,pn(b));}
function pm(a,b){pops++;if(!a.length||!b.length)return[];const r=Array.from({length:a.length+b.length-1},()=>Q());for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)r[i+j]=qa(r[i+j],qm(a[i],b[j]));return trim(r);}
function pc(a,c){return trim(a.map(x=>qm(x,c)));}
function pdm(a,b){if(!b.length)throw Error('zero polynomial divisor');let r=a.slice();const out=Array.from({length:Math.max(0,a.length-b.length+1)},()=>Q());while(r.length>=b.length){const d=r.length-b.length,c=qd(r[r.length-1],b[b.length-1]);out[d]=qa(out[d],c);for(let j=0;j<b.length;j++)r[d+j]=qs(r[d+j],qm(c,b[j]));trim(r);}return[trim(out),r];}
function peq(a,b){return !ps(a,b).length;}
function pmonic(a){return a.length?pc(a,qi(a[a.length-1])):[];}
function pgcd(a,b){while(b.length){const r=pdm(a,b)[1];a=b;b=r;}return pmonic(a);}
function pexact(a,b){const[q,r]=pdm(a,b);if(r.length)throw Error('inexact polynomial division');if(!peq(pm(q,b),a))throw Error('division multiplication failed');rchecks++;return q;}
function pxgcd(a,b){const aa=a,bb=b;let s0=P1,s1=[],t0=[],t1=P1;while(b.length){const[q,r]=pdm(a,b);[a,b]=[b,r];[s0,s1]=[s1,ps(s0,pm(q,s1))];[t0,t1]=[t1,ps(t0,pm(q,t1))];}if(!a.length)return[[],[],[]];const c=qi(a[a.length-1]);a=pc(a,c);s0=pc(s0,c);t0=pc(t0,c);if(!peq(pa(pm(s0,aa),pm(t0,bb)),a))throw Error('Bezout multiplication failed');rchecks++;return[a,s0,t0];}
function powp(a,n){let r=P1;while(n){if(n&1)r=pm(r,a);a=pm(a,a);n>>=1;}return r;}
class R{
 constructor(n=0,d=null){
  if(n instanceof R){this.n=n.n;this.d=n.d;return;}
  if(!Array.isArray(n))n=pp([n]);if(d===null)d=P1;
  if(!d.length)throw Error('zero function denominator');
  if(!n.length){this.n=[];this.d=P1;return;}
  const g=pgcd(n,d);n=pexact(n,g);d=pexact(d,g);
  const c=qi(d[d.length-1]);this.n=pc(n,c);this.d=pc(d,c);
 }
 add(v){v=new R(v);return new R(pa(pm(this.n,v.d),pm(v.n,this.d)),pm(this.d,v.d));}
 neg(){return new R(pn(this.n),this.d);}
 sub(v){return this.add(new R(v).neg());}
 mul(v){v=new R(v);return new R(pm(this.n,v.n),pm(this.d,v.d));}
 inv(){if(!this.n.length)throw Error('zero rational-function inverse');const out=new R(this.d,this.n);if(!this.mul(out).eq(1))throw Error('inverse product failed');return out;}
 div(v){return this.mul(new R(v).inv());}
 pow(n){if(n<0)return this.inv().pow(-n);let a=this,r=new R(1);while(n){if(n&1)r=r.mul(a);a=a.mul(a);n>>=1;}return r;}
 eq(v){v=new R(v);return peq(pm(this.n,v.d),pm(v.n,this.d));}
 zero(){return !this.n.length;}
}
const U=new R(pp([0,1])),ONE=new R(1),Qweight=U.sub(1).mul(U.sub(2)).mul(2);
const ell=U.div(U.sub(1).mul(U.sub(2))),del=ONE.sub(Qweight),g=ell.mul(2).sub(1);
class Z{
 constructor(a=0,b=0){if(a instanceof Z){this.a=a.a;this.b=a.b;}else{this.a=new R(a);this.b=new R(b);}}
 add(v){v=new Z(v);return new Z(this.a.add(v.a),this.b.add(v.b));}
 neg(){return new Z(this.a.neg(),this.b.neg());}
 sub(v){return this.add(new Z(v).neg());}
 mul(v){v=new Z(v);return new Z(this.a.mul(v.a).add(g.mul(this.b.mul(v.b))),this.a.mul(v.b).add(this.b.mul(v.a)));}
 scale(v){v=new R(v);return new Z(this.a.mul(v),this.b.mul(v));}
 pow(n){let a=this,r=new Z(1);while(n){if(n&1)r=r.mul(a);a=a.mul(a);n>>=1;}return r;}
 eq(v){v=new Z(v);return this.a.eq(v.a)&&this.b.eq(v.b);}
 zero(){return this.a.zero()&&this.b.zero();}
}
class E{
 constructor(a=0,b=0){if(a instanceof E){this.a=a.a;this.b=a.b;}else{this.a=new Z(a);this.b=new Z(b);}}
 add(v){v=new E(v);return new E(this.a.add(v.a),this.b.add(v.b));}
 neg(){return new E(this.a.neg(),this.b.neg());}
 sub(v){return this.add(new E(v).neg());}
 mul(v){v=new E(v);return new E(this.a.mul(v.a).add(this.b.mul(v.b).scale(del)),this.a.mul(v.b).add(this.b.mul(v.a)));}
 pow(n){let a=this,r=new E(1);while(n){if(n&1)r=r.mul(a);a=a.mul(a);n>>=1;}return r;}
 conj(){return new E(this.a,this.b.neg());}
 eq(v){v=new E(v);return this.a.eq(v.a)&&this.b.eq(v.b);}
 zero(){return this.a.zero()&&this.b.zero();}
}
function ck(v,msg){if(!v)throw Error(msg);}
const z=new Z(0,1),p=new E(1,1),q=p.conj();
const b=new E(ell.div(2),U.sub(ell).div(del.mul(2))),c=b.conj(),a=new E(ONE.sub(ell));
const B=z.add(1).scale(new R(1).div(2));
const X=new E(U).add(p.mul(new E(B))),Y=X.conj(),f=U,t=new R(0);
const V2=U.mul(2).sub(ell.mul(Qweight)),T0=V2.sub(U.pow(2).mul(2));
const P02=U.mul(3).neg().add(2).mul(V2).sub(Qweight.mul(U)).add(U.pow(3).mul(2));
const M=ell.mul(V2).sub(U.pow(2)),bc=ell.pow(2).sub(U.sub(ell).pow(2).div(del)).div(4);
ck(V2.zero()&&M.eq(U.pow(2).neg())&&P02.eq(U.mul(U.mul(3).sub(2)).mul(2)),'whole V2-zero weight identities');
ck(b.mul(c).eq(bc)&&b.add(c).eq(ell)&&b.mul(p).add(c.mul(q)).eq(U),'original weight definitions');
const x=new Z(U).add(B),y=B;
const W2=x.scale(V2).add(y.scale(U.mul(2).sub(U.mul(Qweight)).sub(ell.mul(Qweight))));
const lam=W2.sub(new Z(U.mul(T0))).sub(new Z(V2.add(U.pow(2).mul(2)).mul(f))).scale(P02.inv());
const J=U.mul(ONE.sub(U)).mul(2).add(ell.mul(Qweight));
const Phi=T0.add(U.mul(4)).sub(4).add(Qweight),Pf=T0.mul(J.sub(Qweight));
const GG=lam.scale(P02).sub(new Z(ONE.sub(U).mul(T0)));
const T=GG.scale(T0).sub(new Z(Pf.mul(f))).scale(Qweight.mul(P02).inv()).sub(ell);
ck(Phi.mul(J.sub(U.mul(Qweight).mul(2))).sub(Pf).zero(),'whole W original weight equation');
ck(lam.eq(z.add(1).scale(Qweight.neg().div(U.mul(3).sub(2).mul(4)))),'lambda compact restoration');
const r=X.sub(a.mul(p)),s=Y.sub(a.mul(q));
const AA=new E(f.mul(2)).sub(b.mul(X).mul(2)).sub(c.mul(Y).mul(2));
const rows=[[new E(),new E(),p,q],[new E(),AA,r,s],[p,r,new E(),new E()],[q,s,new E(),new E()]];
const unit=[new E(1),new E(),new E(1),new E(1)];
function va(v,w){return v.map((x,i)=>x.add(w[i]));}
function vs(c,v){c=new E(c);return v.map(x=>c.mul(x));}
function vm(v,w){return[v[0].mul(w[0]),v[0].mul(w[1]).add(v[1].mul(w[0])),v[2].mul(w[2]),v[3].mul(w[3])];}
function tau(v){return a.mul(v[0]).add(v[1]).add(b.mul(v[2])).add(c.mul(v[3]));}
function DK(v){return rows.map(row=>tau(vm(row,v)));}
const d=DK(unit),F2=tau(d),Kd=DK(d);
function mean(j){const ee=j===1?tau(vm(rows[0],rows[1])).mul(2):tau(vm(rows[j],rows[j]));return ee.sub(Kd[j].mul(2)).sub(vm(d,d)[j].mul(2)).add(F2.mul(d[j]).mul(2));}
ck(F2.eq(f.mul(2)),'original f return');
for(let j=0;j<4;j++)ck(mean(j).zero(),'whole quadratic original mean '+j);
function N4(v){return tau(vm(d,vm(v,v))).mul(2).sub(F2.mul(tau(vm(v,v)))).sub(tau(v).mul(tau(vm(d,v))).mul(4)).add(F2.mul(tau(v).pow(2)).mul(2)).add(tau(vm(v,DK(v))));}
function P2(v){const vc=va(v,vs(tau(v).neg(),unit));return tau(vm(vm(vc,vc),vc));}
const Nv=N4(va(rows[0],rows[1])).sub(N4(rows[0])).sub(N4(rows[1]));
const vc=va(rows[0],vs(tau(rows[0]).neg(),unit)),zc=va(rows[1],vs(tau(rows[1]).neg(),unit));
const Pj=tau(vm(vm(vc,vc),zc)).mul(3);
ck(N4(rows[0]).eq(lam.scale(P02.mul(2))),'original N0 return');
ck(P2(rows[0]).eq(P02),'original P0 return');
ck(Pj.eq(lam.sub(1).sub(T).scale(P02.mul(3))),'original P1 return');
const A2=lam.pow(2).scale(2).sub(lam.scale(2)).add(1);
const B3=lam.pow(3).scale(4).sub(lam.pow(2).scale(6)).add(lam.scale(3)).sub(1);
const N1=Nv.sub(new E(lam.scale(new R(4).div(3))).mul(Pj));
const NS=b.mul(N4(rows[2])).add(c.mul(N4(rows[3]))).sub(new E(lam.mul(new Z(ell).add(T.scale(2)).add(A2)).scale(P02.mul(2))));
const PS=b.mul(P2(rows[2])).add(c.mul(P2(rows[3]))).sub(new E(new Z(ell).add(T.scale(3)).add(A2.scale(3)).add(B3).scale(P02)));
const original=[N1,NS,PS];for(const v of original)ck(v.b.zero(),'rho-odd original row zero');
const rr=original.map(v=>v.a);
const DP=A2.scale(ell).sub(T.pow(2));
function profileP(a){return{degree:a.length-1,coefficients:a.length<=30?a.map(qt):undefined};}
function profileR(a){return{numerator:profileP(a.n),denominator:profileP(a.d)};}
function profileZ(a){return{constant:profileR(a.a),linear:profileR(a.b)};}
const scalars=[];for(let i=0;i<rr.length;i++)scalars.push(rr[i].a.pow(2).sub(g.mul(rr[i].b.pow(2))));
for(let i=0;i<rr.length;i++)for(let j=i+1;j<rr.length;j++)scalars.push(rr[i].a.mul(rr[j].b).sub(rr[j].a.mul(rr[i].b)));
let cover=[];for(const h of scalars)if(!h.zero())cover=pgcd(cover,h.n);
ck(cover.length,'nonzero scalar necessary cover');
const output={stage:'new_whole_W_t_zero_V2_zero_original_quadratic_return',seconds:(Date.now()-start)/1000,
 qRationalOperations:qops,polynomialOperations:pops,exactDivisionAndBezoutChecks:rchecks,
 weights:'Q=2(u-1)(u-2), ell=u/((u-1)(u-2)), k=2u-4, e=u-1',
 fullQuadratic:'z^2=2ell-1',fullRho:'rho^2=1-Q',allFourOriginalMeansZero:true,
 originalN0P0P1Returned:true,originalRows:rr.map(profileZ),physicalD:profileZ(DP),
 scalarNecessaryProfiles:scalars.map(profileR),entireCover:profileP(cover),claimExcluded:false};
return {output,internals:{Q,qa,qn,qs,qm,qi,qd,qt,pp,pa,pn,ps,pm,pc,pdm,peq,pmonic,pgcd,pexact,pxgcd,powp,R,Z,E,U,Qweight,ell,del,g,V2,T0,P02,M,bc,J,Phi,Pf,x,y,lam,T,A2,B3,rr,DP,scalars,cover,profileP,profileR,profileZ,ck,P1}};
