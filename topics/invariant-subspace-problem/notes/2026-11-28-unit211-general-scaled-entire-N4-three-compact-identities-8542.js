"use strict";
// NEW three full N4 coefficients of polynomial ell-scaled value vectors.
// Nine independent raw Gram/value variables; no equations or inverses.
const began=Date.now(),D=9,ZKEY="0,0,0,0,0,0,0,0,0";let products=0;
function C(n=0n){return n===0n?new Map():new Map([[ZKEY,n]])}
function V(i){const a=Array(D).fill(0);a[i]=1;return new Map([[a.join(","),1n]])}
function add(a,b){const c=new Map(a);for(const[k,v]of b){let x=(c.get(k)||0n)+v;if(x)c.set(k,x);else c.delete(k)}return c}
function neg(a){return new Map([...a].map(([k,v])=>[k,-v]))}
function sub(a,b){return add(a,neg(b))}
function mul(a,b){if(Date.now()-began>120000)throw Error("new complete scaled N4 identity 120 second budget");products++;const c=new Map();for(const[ka,va]of a){const ea=ka.split(",").map(Number);for(const[kb,vb]of b){const eb=kb.split(",").map(Number),k=ea.map((x,i)=>x+eb[i]).join(","),x=(c.get(k)||0n)+va*vb;if(x)c.set(k,x);else c.delete(k)}}return c}
function sc(a,n){return mul(a,C(BigInt(n)))}
function sq(a){return mul(a,a)}
function sum(xs){return xs.reduce(add,C())}
function prod(xs){return xs.reduce(mul,C(1n))}


const [b,c,rho,A1,r,s,t,lam,T]=Array.from({length:D},(_,i)=>V(i));
const one=C(1n),zero=C(),ell=add(b,c),a=sub(one,ell);
const p=add(one,rho),q=sub(one,rho),Q=sub(one,sq(rho)),delta=sq(rho);
const rows=[[zero,zero,p,q],[zero,A1,r,s],[p,r,zero,t],[q,s,t,zero]];
const unit=[one,zero,one,one];
function vm(v,w){return[mul(v[0],w[0]),add(mul(v[0],w[1]),mul(v[1],w[0])),
                       mul(v[2],w[2]),mul(v[3],w[3])]}
function va(v,w){return v.map((x,i)=>add(x,w[i]))}
function tau(v){return sum([mul(a,v[0]),v[1],mul(b,v[2]),mul(c,v[3])])}
function DK(v){return rows.map(row=>tau(vm(row,v)))}
const dv=DK(unit),F2=tau(dv),u=dv[0],X=dv[2],Y=dv[3];
const scalarV=add(mul(b,X),mul(c,Y)),W1=add(prod([b,p,X]),prod([c,q,Y]));
const m=sub(u,ell),M=sc(prod([b,c,delta]),4),w=sub(sub(lam,one),T);
const Al=sum([sc(sq(lam),2),sc(lam,-2),one]);
const Dval=sub(mul(ell,Al),sq(T));
const checks=[];
function check(name,P){if(P.size)throw Error(name+": "+P.size+" nonzero terms");
 checks.push({name,fullIntegerPolynomialDifferenceZero:true})}
check("same_original_normalized_u",sub(u,add(ell,mul(rho,sub(b,c)))));
check("same_original_M",sub(M,sub(mul(sq(ell),delta),sq(m))));
function N4(v){
 const tv=tau(v),vv=vm(v,v);
 return sum([sc(tau(vm(dv,vv)),2),neg(mul(F2,tau(vv))),
             sc(mul(tv,tau(vm(dv,v))),-4),
             sc(mul(F2,sq(tv)),2),tau(vm(v,DK(v)))]);
}
const V0=[ell,mul(ell,w),add(ell,T),add(ell,T)];
const V1=[zero,zero,sub(m,mul(ell,rho)),add(m,mul(ell,rho))];
check("scaled_value_zero_trace",sub(tau(V0),mul(ell,lam)));
check("scaled_value_one_trace",tau(V1));
check("scaled_value_one_B_is_minus_2c_rho",add(V1[2],sc(mul(c,rho),2)));
check("scaled_value_one_C_is_2b_rho",sub(V1[3],sc(mul(b,rho),2)));
const Z0=N4(V0),Z2=N4(V1),Z1=sub(sub(N4(va(V0,V1)),Z0),Z2);
const cval=sub(C(3n),sc(lam,2));
const short0=sum([
 mul(sq(ell),A1),
 sc(prod([sq(ell),sub(one,sc(lam,2)),F2]),2),
 prod([ell,F2,Dval]),
 sc(prod([ell,u,w,add(mul(ell,cval),T)]),2),
 sc(mul(scalarV,sum([sq(ell),prod([ell,cval,T]),sq(T)])),2),
 sc(prod([b,c,t,sub(sq(T),sq(ell))]),2)
]);
const short1=sum([
 sc(mul(add(mul(ell,cval),sc(T,2)),sub(mul(u,scalarV),mul(ell,W1))),2),
 sc(prod([ell,M,w]),-2),
 sc(prod([b,c,m,T,t]),4)
]);
const short2=sum([
 sc(mul(sub(sq(u),mul(sq(ell),Q)),scalarV),2),
 sc(prod([m,ell,W1]),-4),
 neg(prod([ell,M,F2])),
 sc(prod([b,c,M,t]),-2)
]);
check("full_original_scaled_N4V0_compact",sub(Z0,short0));
check("full_original_scaled_N4polar_compact",sub(Z1,short1));
check("full_original_scaled_N4V1_compact",sub(Z2,short2));
return {schema:"isp-nine-free-variable-scaled-entire-N4-three-coefficients-v1",
 variables:["b","c","rho","A1","r","s","t","lambda","T"],
 normalizedOnly:"a=1-b-c, p=1+rho, q=1-rho",
 elapsed_milliseconds:Date.now()-began,integerPolynomialProducts:products,
 checks,originalTermCounts:[Z0.size,Z1.size,Z2.size],
 noOriginalMeanEquationAssumed:true,noWOrPhiWeightRelationAssumed:true,
 noDOrEllOrGeometryInverse:true,noOldCofactorOrOriginalValueGateRepeated:true,
 wholeWExcluded:false,ordinaryISPClaim:false};
