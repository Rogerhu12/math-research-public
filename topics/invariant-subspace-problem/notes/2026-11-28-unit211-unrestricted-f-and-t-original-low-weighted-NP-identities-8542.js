"use strict";
// NEW full free-f and free-t original low weighted N/P dependence.
// Eight free variables b,c,p,q,X,Y,t,eta with f=u+eta. True dual product.
// Compact two scalar consequences below are used only after p+q=2 and original value equalities.
const began=Date.now(),D=8,ZKEY="0,0,0,0,0,0,0,0";let products=0;
function C(n=0n){return n===0n?new Map():new Map([[ZKEY,n]])}
function V(i){const a=Array(D).fill(0);a[i]=1;return new Map([[a.join(","),1n]])}
function add(a,b){const c=new Map(a);for(const[k,v]of b){let x=(c.get(k)||0n)+v;if(x)c.set(k,x);else c.delete(k)}return c}
function neg(a){return new Map([...a].map(([k,v])=>[k,-v]))}
function sub(a,b){return add(a,neg(b))}
function mul(a,b){if(Date.now()-began>120000)throw Error("new original bipartite jet identity 120 second budget");products++;const c=new Map();for(const[ka,va]of a){const ea=ka.split(",").map(Number);for(const[kb,vb]of b){const eb=kb.split(",").map(Number),k=ea.map((x,i)=>x+eb[i]).join(","),x=(c.get(k)||0n)+va*vb;if(x)c.set(k,x);else c.delete(k)}}return c}
function sc(a,n){return mul(a,C(BigInt(n)))}
function sq(a){return mul(a,a)}
function sum(xs){return xs.reduce(add,C())}
function prod(xs){return xs.reduce(mul,C(1n))}

const [b,c,p,q,X,Y,t,eta]=Array.from({length:D},(_,i)=>V(i));
const one=C(1n),zero=C(),ell=add(b,c),a=sub(one,ell);
const uu=add(mul(b,p),mul(c,q)),scalarV0=add(mul(b,X),mul(c,Y));
const r=sub(sub(X,mul(a,p)),mul(c,t)),s=sub(sub(Y,mul(a,q)),mul(b,t));
const A1=add(sub(sc(add(uu,eta),2),sc(scalarV0,2)),sc(prod([b,c,t]),2));
const rows=[[zero,zero,p,q],[zero,A1,r,s],
            [p,r,zero,t],[q,s,t,zero]];
const unit=[one,zero,one,one];
function vm(v,w){return[mul(v[0],w[0]),add(mul(v[0],w[1]),mul(v[1],w[0])),
                         mul(v[2],w[2]),mul(v[3],w[3])]}
function va(v,w){return v.map((x,i)=>add(x,w[i]))}
function vs(x,v){return v.map(t=>mul(x,t))}
function tau(v){return sum([mul(a,v[0]),v[1],mul(b,v[2]),mul(c,v[3])])}
function DK(v){return rows.map(row=>tau(vm(row,v)))}
const dv=DK(unit),F2=tau(dv),Kd=DK(dv),dd=vm(dv,dv);
const checks=[];
function check(name,P){if(P.size)throw Error(name+": "+P.size+" nonzero terms");
 checks.push({name,fullIntegerPolynomialDifferenceZero:true});}
const u=tau(rows[0]),d1=tau(rows[1]);
const scalarV=add(mul(b,dv[2]),mul(c,dv[3]));
check("same_full_Gram_free_f",sub(F2,sc(add(u,eta),2)));
function mean(j){
 const e=j===1?sc(tau(vm(rows[0],rows[1])),2):tau(vm(rows[j],rows[j]));
 return sum([e,sc(Kd[j],-2),sc(dd[j],-2),sc(mul(F2,dv[j]),2)]);
}
function centered(v){return va(v,vs(neg(tau(v)),unit))}
function P2(v){const vc=centered(v);return tau(vm(vm(vc,vc),vc))}
function N4(v){
 const tv=tau(v),vv=vm(v,v);
 return sum([sc(tau(vm(dv,vv)),2),neg(mul(F2,tau(vv))),
             sc(mul(tv,tau(vm(dv,v))),-4),
             sc(mul(F2,sq(tv)),2),tau(vm(v,DK(v)))]);
}
const v=rows[0],w=rows[1],vc=centered(v),wc=centered(w);
const Nzero=N4(v),Pzero=P2(v);
const Nj=sub(sub(N4(va(v,w)),N4(v)),N4(w));
const Pj=sc(tau(vm(vm(vc,vc),wc)),3);
const E0=mean(0),E1=mean(1),EB=mean(2),EC=mean(3);
const Ep=add(prod([b,p,EB]),prod([c,q,EC]));

const V2=add(mul(b,sq(p)),mul(c,sq(q))),T0=sub(V2,sc(sq(u),2));
const NW=add(mul(b,N4(rows[2])),mul(c,N4(rows[3])));
const PW=add(mul(b,P2(rows[2])),mul(c,P2(rows[3])));
const EW2=add(prod([b,sub(sub(sc(p,2),u),dv[2]),EB]),
              prod([c,sub(sub(sc(q,2),u),dv[3]),EC]));


const sigma=add(p,q),Sx=add(X,Y),Qpq=mul(p,q),W=add(prod([b,p,X]),prod([c,q,Y]));
const Px=add(mul(p,X),mul(q,Y));
const PhiGen=sum([neg(sq(sigma)),Qpq,sc(V2,3),sc(mul(ell,Qpq),2),sc(sq(u),-2)]);
const CN=sum([sc(mul(t,sub(Sx,sc(u,4))),2),sc(mul(X,Y),-8),
 sc(add(mul(q,X),mul(p,Y)),4),sc(mul(u,Sx),4),sc(sq(u),4),sc(mul(a,Qpq),-4)]);
const CP=sum([sc(sq(t),4),sc(mul(t,sub(sub(u,Sx),sigma)),4),
 sc(mul(X,Y),-8),sc(mul(sigma,Sx),8),sc(sub(sq(sigma),sc(Qpq,3)),2),
 sc(V2,-18),sc(mul(ell,Qpq),-8),sc(sq(u),20)]);
const CJ=sum([sc(mul(sub(sigma,u),t),2),sc(W,4),sc(mul(sigma,Sx),-2),
 sc(Px,-2),sc(sq(sigma),-4),sc(Qpq,4),sc(V2,16),sc(mul(ell,Qpq),12),sc(sq(u),-8)]);
const Kw=sc(sum([sq(t),mul(sub(sub(sc(u,5),sc(Sx,2)),sigma),t),
 sc(mul(X,Y),2),sc(Px,2),sc(mul(u,Sx),-2),sc(sq(u),2),
 sc(mul(sigma,u),-3),Qpq]),2);
const Kl=sc(sum([sq(t),sc(mul(sub(sub(sc(u,3),Sx),sigma),t),2),
 sc(mul(X,Y),2),sc(Px,3),mul(sub(sigma,sc(u,2)),Sx),sc(W,-2),
 sc(sq(u),4),sc(mul(sigma,u),-8),sq(sigma),mul(ell,Qpq)]),2);

function monomialDivide(P,variable,power,coefficient){
 const q=new Map();
 for(const [key,v] of P){
  const ex=key.split(",").map(Number);
  if(ex[variable]<power||v%coefficient)throw Error("nonexact original eta division");
  ex[variable]-=power;q.set(ex.join(","),v/coefficient);
 }
 const atom=Array(D).fill(0);atom[variable]=power;
 check("whole_original_eta_quotient_return",sub(P,mul(q,new Map([[atom.join(","),coefficient]]))));
 return q;
}
const first=sum([sc(NW,3),sc(PW,-3),neg(Pj),sc(mul(a,sub(Nzero,Pzero)),3),
 sc(mul(sub(d1,sc(mul(ell,u),2)),E0),-3),sc(EW2,3),sc(prod([b,c,t,Kw]),3)]);
const second=sum([NW,neg(PW),Nj,neg(Pj),mul(sub(C(2n),sc(ell,3)),Nzero),
 mul(sub(ell,one),Pzero),EW2,sc(Ep,2),sc(mul(u,E1),-2),
 neg(mul(sum([d1,A1,sc(mul(u,sub(one,sc(ell,2))),2)]),E0)),prod([b,c,t,Kl])]);
const Rw=monomialDivide(first,7,1,3n),Rl=monomialDivide(second,7,1,1n);
check("free_f_first_jet_original_identity",sub(sum([sc(Pj,2),sc(Nzero,-3),
 sc(mul(a,Pzero),6),sc(mul(A1,T0),3)]),sc(prod([b,c,t,PhiGen]),6)));
const secondJetResidual=sub(sum([Nj,sc(mul(ell,Nzero),-2),sc(mul(a,Pzero),2),
 sc(Ep,2),sc(mul(u,E1),-2),sc(prod([a,u,E0]),-2),
 neg(mul(A1,sub(E0,T0)))]),prod([b,c,t,CJ]));
const Jeta=monomialDivide(secondJetResidual,7,1,1n);
check("free_f_second_jet_eta_compact_formula",
 sub(Jeta,add(sc(mul(u,A1),-4),sc(prod([b,c,sigma,t]),4))));
function canonical(P){return [...P].map(([key,c])=>[key.split(",").map(Number),String(c)])
 .sort((a,b)=>{for(let i=0;i<D;i++)if(a[0][i]!==b[0][i])return a[0][i]-b[0][i];return 0;});}
return {schema:"isp-eight-free-variables-original-weighted-NP-f-dependence-v1",
 variables:["b","c","p","q","X","Y","t","eta"],f:"u+eta",
 elapsed_milliseconds:Date.now()-began,integerPolynomialProducts:products,checks,
 originalFullFirstJetReturned:true,originalFullSecondJetEtaReturned:true,
 firstLowResidualEquals:"3*eta*Rw",secondLowResidualEquals:"eta*Rl",
 Rw:canonical(Rw),Rl:canonical(Rl),
 firstLowCount:Rw.size,secondLowCount:Rl.size,
 noDivisionByEtaInOriginalConclusion:true,ordinaryISPClaim:false};
