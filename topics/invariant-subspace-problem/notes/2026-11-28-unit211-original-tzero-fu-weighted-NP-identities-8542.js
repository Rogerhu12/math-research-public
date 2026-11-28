"use strict";
// NEW original unit211 t=0,f=u weighted N/P sources; A1 remains the exact Gram value.
// No Phi, W, lambda normalization, scalar mean inverses or old head input.
const began=Date.now(),D=6,ZKEY="0,0,0,0,0,0";let products=0;
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

const [b,c,p,q,r,s]=Array.from({length:D},(_,i)=>V(i));
const one=C(1n),zero=C(),ell=add(b,c),a=sub(one,ell);
const uu=add(mul(b,p),mul(c,q)),Rzero=add(mul(b,r),mul(c,s));
const A1=sub(sc(mul(ell,uu),2),sc(Rzero,2));
const rows=[[zero,zero,p,q],[zero,A1,r,s],
            [p,r,zero,zero],[q,s,zero,zero]];
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
check("same_full_Gram_f_equals_u",sub(F2,sc(u,2)));
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
check("whole_weighted_N_on_actual_tzero_fu",
 sub(NW,sum([mul(A1,T0),sc(prod([ell,u,u,u]),-4),sc(mul(d1,E0),2)])));
check("whole_weighted_P_on_actual_tzero_fu",
 sub(sc(PW,2),sum([mul(sub(one,sc(ell,2)),Nzero),sc(mul(A1,T0),3),
                  sc(prod([ell,u,u,u]),-8),
                  sc(mul(add(sc(mul(ell,u),2),d1),E0),2),sc(EW2,2)])));
check("whole_free_A1_first_jet_on_actual_tzero_fu",
 sum([sc(Pj,2),sc(Nzero,-3),sc(mul(a,Pzero),6),sc(mul(A1,T0),3)]));
check("whole_second_jet_on_actual_tzero_fu",
 sum([Nj,sc(mul(ell,Nzero),-2),sc(mul(a,Pzero),2),sc(Ep,2),
 sc(mul(u,E1),-2),sc(prod([a,u,E0]),-2),
 neg(mul(A1,sub(E0,T0)))]));
return {schema:"isp-original-tzero-fu-weighted-NP-v1",
 variables:["b","c","p","q","r","s"],elapsed_milliseconds:Date.now()-began,
 integerPolynomialProducts:products,checks,
 trueGramA1:"2*ell*u-2*(b*r+c*s)",trueDualGermSquare:true,
 actualF2Equals2u:true,wholeWeightedNAndP:true,
 noPhiAssumption:true,noWAuxiliaryAssumption:true,noUnpaidDivision:true,
 consequenceAfterAllOriginalValueAndJetEqualities:
 "(2*lambda-1)*w=0 and lambda*(2*ell-1)=0",
 ordinaryISPClaim:false};
