"use strict";
// NEW original unit211 A1=t=0 Gram identities.
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
const rows=[[zero,zero,p,q],[zero,zero,r,s],
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
check("same_full_Gram_F2_equals_twoV",sub(F2,sc(scalarV,2)));
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
check("full_original_Pjet_N0_identity",
 sum([sc(Pj,2),sc(Nzero,-3),sc(mul(a,Pzero),6)]));
check("full_original_Njet_means_N0_identity",
 sum([Nj,sc(mul(ell,Nzero),-2),sc(mul(a,Pzero),2),
      sc(Ep,2),sc(mul(u,E1),-2),sc(prod([a,u,E0]),-2)]));
return {schema:"isp-original-bipartite-unit211-jets-v1",
 variables:["b","c","p","q","r","s"],
 elapsed_milliseconds:Date.now()-began,integerPolynomialProducts:products,checks,
 originalGramRows:["0,0,p,q","0,0,r,s","p,r,0,0","q,s,0,0"],
 trueDualGermSquare:true,allSixParametersIndependent:true,
 noPhiAssumption:true,noWAuxiliaryAssumption:true,noUnpaidDivision:true,
 noOldQuadraticHeadUsed:true,
 consequenceUsingOriginalN0P1N1AndMeans:"P02 != 0 forces T=-ell and A2=ell, hence D=0",
 originalISPClaim:false};
