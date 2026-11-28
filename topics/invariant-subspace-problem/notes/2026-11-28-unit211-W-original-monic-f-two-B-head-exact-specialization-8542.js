// New exact characteristic-zero exploratory B-coefficient determinant.
// This is NOT a physical-point or empty-fiber test. The original I4
// degrees in f and (lambda,T) prove the coefficient interpolation used.
// Parameter definition: e=1,k=3; lambda,T=(0,0),(1,0),(0,1),(2,3).
// All operations exact rational arithmetic, rho^2=1-Q; no norm inverse.
(function(){
let ops=0; const start=Date.now();
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;}
class R{
constructor(n=0n,d=1n){if(n instanceof R){this.n=n.n;this.d=n.d;return;}n=BigInt(n);d=BigInt(d);if(!d)throw Error('zero denominator');let g=gcd(n,d);if(d<0n)g=-g;this.n=n/g;this.d=d/g;}
add(o){o=new R(o);ops++;return new R(this.n*o.d+o.n*this.d,this.d*o.d);}
neg(){return new R(-this.n,this.d);}
sub(o){return this.add(new R(o).neg());}
mul(o){o=new R(o);ops++;return new R(this.n*o.n,this.d*o.d);}
div(o){o=new R(o);return this.mul(new R(o.d,o.n));}
pow(n){let a=new R(1n),b=this;while(n){if(n&1)a=a.mul(b);n>>=1;if(n)b=b.mul(b);}return a;}
eq(o){o=new R(o);return this.n===o.n&&this.d===o.d;}
str(){return this.d===1n?String(this.n):this.n+'/'+this.d;}
}
const r=x=>new R(x),sum=xs=>xs.reduce((a,b)=>a.add(b),r(0));
const e=r(1),k=r(3),u=e.add(1),Q=e.mul(k),Vbar=u.mul(k).add(2),delta=r(1).sub(Q),
 ell=u.mul(k.add(2).pow(2).sub(e.mul(k).mul(2))).div(k.mul(Vbar)),m=u.sub(ell),
 theta=u.sub(ell.mul(Q)),V2=u.mul(2).sub(ell.mul(Q)),M=ell.mul(V2).sub(u.pow(2)),
 bc=M.div(delta.mul(4)),T0=V2.sub(u.pow(2).mul(2)),J=u.mul(r(1).sub(u)).mul(2).add(ell.mul(Q)),
 Phi=T0.add(u.mul(4)).sub(4).add(Q),Pf=T0.mul(J.sub(Q)),
 P02=r(2).sub(u.mul(3)).mul(V2).sub(Q.mul(u)).add(u.pow(3).mul(2)),
 beta=u.mul(2).sub(J.div(Q)),cf=bc.div(u.mul(u.sub(beta)).mul(2));
class E{
constructor(a=0,b=0){if(a instanceof E){this.a=a.a;this.b=a.b;return;}this.a=r(a);this.b=r(b);}
add(o){o=new E(o);return new E(this.a.add(o.a),this.b.add(o.b));}
neg(){return new E(this.a.neg(),this.b.neg());}
sub(o){return this.add(new E(o).neg());}
mul(o){o=new E(o);return new E(this.a.mul(o.a).add(delta.mul(this.b).mul(o.b)),this.a.mul(o.b).add(this.b.mul(o.a)));}
pow(n){let a=new E(1);while(n--)a=a.mul(this);return a;}
eq(o){o=new E(o);return this.a.eq(o.a)&&this.b.eq(o.b);}
conj(){return new E(this.a,this.b.neg());}
}
const E0=x=>new E(x),esm=xs=>xs.reduce((a,b)=>a.add(b),new E());
const b=new E(ell.div(2),m.div(delta.mul(2))),c=b.conj(),a=E0(r(1).sub(ell)),p=new E(1,1),q=p.conj();
function raw(lam,T,f){
 lam=r(lam);T=r(T);f=r(f);
 const G=lam.mul(P02).sub(r(1).sub(u).mul(T0)),Pc=Q.mul(P02).mul(ell.add(T)).sub(G.mul(T0)),
 t=Pf.mul(f).add(Pc).neg().div(bc.mul(Q).mul(Phi)),V=J.mul(f).sub(G).add(bc.mul(Q).mul(t)).div(Q),
 W=T0.div(2).add(u.mul(f).mul(2)),x=theta.mul(V).sub(m.mul(W)).div(M),y=ell.mul(W).sub(u.mul(V)).div(M),
 A1=f.mul(2).sub(V.mul(2)).add(bc.mul(t).mul(2)),X=new E(x,y),Y=X.conj(),
 rr=X.sub(a.mul(p)).sub(c.mul(t)),ss=Y.sub(a.mul(q)).sub(b.mul(t)),
 rows=[[new E(),new E(),p,q],[new E(),E0(A1),rr,ss],[p,rr,new E(),E0(t)],[q,ss,E0(t),new E()]],
 one=[new E(1),new E(),new E(1),new E(1)];
 const va=(v,w)=>v.map((x,i)=>x.add(w[i])),vs=(h,v)=>v.map(x=>h.mul(x)),
 vm=(v,w)=>[v[0].mul(w[0]),v[0].mul(w[1]).add(v[1].mul(w[0])),v[2].mul(w[2]),v[3].mul(w[3])],
 tau=v=>a.mul(v[0]).add(v[1]).add(b.mul(v[2])).add(c.mul(v[3])),
 DK=v=>rows.map(rr=>tau(vm(rr,v))),d=DK(one),F2=tau(d),Kd=DK(d);
 function mean(j){
 const sq=j===1?tau(vm(rows[0],rows[1])).mul(2):tau(vm(rows[j],rows[j]));
 return sq.sub(Kd[j].mul(2)).sub(vm(d,d)[j].mul(2)).add(F2.mul(d[j]).mul(2));
 }
 if(!mean(0).eq(0)||!F2.eq(f.mul(2)))throw Error('original mean recovery');
 function N4(v){
 return esm([tau(vm(d,vm(v,v))).mul(2),F2.mul(tau(vm(v,v))).neg(),
  tau(v).mul(tau(vm(d,v))).mul(-4),F2.mul(tau(v).pow(2)).mul(2),tau(vm(v,DK(v)))]);
 }
 const pol=N4(va(rows[0],rows[1])).sub(N4(rows[0])).sub(N4(rows[1])),
 N1=pol.sub(lam.mul(lam.sub(1).sub(T)).mul(P02).mul(4)),
 e1=mean(1),eb=mean(2);
 if(!e1.b.eq(0)||!N1.b.eq(0)||!mean(3).eq(eb.conj()))throw Error('descent');
 if(!N4(rows[0]).eq(lam.mul(P02).mul(2)))throw Error('N0');
 return [e1.a,eb.a,eb.b,N1.a];
}
function rowBs(l,T){
 const fm=raw(l,T,-1),f0=raw(l,T,0),fp=raw(l,T,1);
 const h=fm.map((x,i)=>x.add(fp[i]).sub(f0[i].mul(2)).div(2)),
 lin=fm.map((x,i)=>fp[i].sub(x).div(2));
 const q1=cf.mul(lin[1].add(ell.mul(delta).div(m).mul(lin[2])));
 const q2=cf.mul(h[1].add(ell.mul(delta).div(m).mul(h[2])));
 if(!q2.eq(1))throw Error('monic f2');
 return [0,2,3].map(i=>lin[i].sub(h[i].mul(q1)));
}
const z=rowBs(0,0),l=rowBs(1,0),t=rowBs(0,1),v=rowBs(2,3);
const B=z.map((x,i)=>[x,l[i].sub(x),t[i].sub(x)]);
for(let i=0;i<3;i++)if(!B[i][0].add(B[i][1].mul(2)).add(B[i][2].mul(3)).eq(v[i]))throw Error('affine coefficient');
const det=B[0][0].mul(B[1][1].mul(B[2][2]).sub(B[1][2].mul(B[2][1])))
 .sub(B[0][1].mul(B[1][0].mul(B[2][2]).sub(B[1][2].mul(B[2][0]))))
 .add(B[0][2].mul(B[1][0].mul(B[2][1]).sub(B[1][1].mul(B[2][0]))));
return {parameters:{e:"1",k:"3"},exactDeterminant:det.str(),zero:det.eq(0),
 coefficientRowNames:["E1","EBo","N1"],affineCoefficientColumns:["1","lambda","T"],
 exactOriginalDualArithmetic:true,degreeBoundUsed:"published total degree at most two",nonemptyOrEmptyPhysicalFiberClaim:false,
 arithmeticOperations:ops,milliseconds:Date.now()-start};
})()
