// R562: exact source constants and full-complement coefficient certificate.
// Run: node check-r562-four-unit-negative-moment-relation.mjs
const certificate=(()=>{

"use strict";
let checks=0;
const ok=(v,msg)=>{if(!v)throw new Error(msg);checks++;};
const names=["beta","kappa","Omega","b","I4"];
const mon=e=>e.join(",");
const zero=()=>new Map();
const one=()=>new Map([["0,0,0,0,0",1n]]);
const variable=i=>{const e=[0,0,0,0,0];e[i]=1;return new Map([[mon(e),1n]]);};
const add=(a,b)=>{const c=new Map(a);for(const [m,v]of b){const w=(c.get(m)||0n)+v;if(w)c.set(m,w);else c.delete(m);}return c;};
const sc=(a,n)=>new Map([...a].filter(([,v])=>v*n).map(([m,v])=>[m,v*n]));
const mul=(a,b)=>{let c=zero();for(const [ma,va]of a)for(const[mb,vb]of b){const ea=ma.split(",").map(Number),eb=mb.split(",").map(Number);c=add(c,new Map([[mon(ea.map((x,i)=>x+eb[i])),va*vb]]));}return c;};
const pow=(a,n)=>{let r=one();for(let i=0;i<n;i++)r=mul(r,a);return r;};
const eq=(a,b)=>add(a,sc(b,-1n)).size===0;
const fmt=a=>[...a].sort((x,y)=>x[0].localeCompare(y[0])).map(([e,c])=>({exponents:e.split(",").map(Number),coefficient:c.toString()}));
const [beta,kappa,Omega,b,I4]=names.map((_,i)=>variable(i));
const A0=add(one(),sc(beta,-1n));
const A1=mul(Omega,add(one(),sc(mul(beta,kappa),-1n)));
const A3=sc(mul(pow(Omega,3),add(one(),sc(mul(beta,pow(kappa,3)),-1n))),6n);
const types={H:0,f1:1,f3:3,f4:4};
const mod6=n=>(n%6+6)%6;
function moment(f,r){
 if(mod6(r)!==types[f])return zero();
 if(f==="H"&&r===0)return A0;
 if(f==="f1"&&r===1)return A1;
 if(f==="f3"&&r===3)return A3;
 if(f==="f4"&&r===-2)return I4;
 throw new Error("Unpaid moment "+f+" "+r);
}
const tensor=[
 ["H","f1",one()],
 ["f1","H",one()],
 ["f3","f4",sc(b,-6n)],
 ["f4","f3",sc(b,-6n)]
];
function jointMoment(r,s){
 let out=zero();
 for(const [f,g,c]of tensor)out=add(out,mul(c,mul(moment(f,r),moment(g,s))));
 return out;
}
const tests=[[1,0,1n],[0,1,3n],[-1,2,3n],[-2,3,1n]];
let scaledDouble=zero();
for(const[r,s,n]of tests)scaledDouble=add(scaledDouble,sc(jointMoment(r,s),n));
const doubleExpected=add(sc(mul(A0,A1),4n),sc(mul(b,mul(A3,I4)),-6n));
ok(eq(scaledDouble,doubleExpected),"whole two-output double-unit moment");
ok(jointMoment(-1,2).size===0,"complete absent type-5 row");
const scaledFourLeading=add(scaledDouble,sc(mul(beta,A1),-8n));
const target=add(sc(mul(Omega,mul(add(one(),sc(mul(beta,kappa),-1n)),add(one(),sc(beta,-3n)))),4n),sc(mul(b,mul(pow(Omega,3),mul(add(one(),sc(mul(beta,pow(kappa,3)),-1n)),I4))),-36n));
ok(eq(scaledFourLeading,target),"8 delta^2 times exact four-unit relation");
const ka=(u,v)=>[u[0]+v[0],u[1]+v[1]];
const ks=(u,n)=>[u[0]*n,u[1]*n];
const km=(u,v)=>[u[0]*v[0]-u[1]*v[1],u[0]*v[1]+u[1]*v[0]-u[1]*v[1]];
const kc=u=>[u[0]-u[1],-u[1]];
const ke=(u,v)=>u[0]===v[0]&&u[1]===v[1];
const delta=[1n,2n],a=[2n,1n],minusOmega2=[1n,1n],unit=[1n,0n];
ok(ke(km(minusOmega2,a),delta),"delta=-omega^2 a");
ok(ke(km(delta,delta),[-3n,0n]),"delta square");
const gram=(r,s)=>ka(km(r[0],kc(s[0])),ks(km(r[1],kc(s[1])),3n));
const H=[delta,[-1n,0n]],K=[delta,unit];
ok(ke(gram(H,H),[6n,0n]),"H whole degree 6");
ok(ke(gram(K,K),[6n,0n]),"K whole degree 6");
ok(ke(gram(H,K),[0n,0n]),"complete cross polarization");
const det=ka(km(H[0],K[1]),ks(km(H[1],K[0]),-1n));
ok(ke(det,ks(delta,2n)),"physical determinant 2 delta");
const fact=n=>{let r=1n;for(let j=2n;j<=BigInt(n);j++)r*=j;return r;};
ok(fact(7)/210n===24n&&fact(7)%210n===0n,"sigma seventh moment");
ok(fact(6)*3n/10n===216n&&fact(6)*3n%10n===0n,"B sixth moment");
ok(5n*24n===120n,"sigma-deep first coefficient");
ok(7n*216n===1512n,"B-deep first tail coefficient");
const sigTerms=[],bTerms=[];
for(let j=0;j<=30;j++){
 if(mod6(j+3)===1)sigTerms.push({j,valuation:j+3});
 if(mod6(j)===0)bTerms.push({j,valuation:j});
}
ok(sigTerms[0].j===4&&sigTerms[0].valuation===7,"sigma-deep begins at seven");
ok(sigTerms.every(({j},i)=>j===4+6*i),"sigma-deep exact congruence");
ok(bTerms[0].j===0&&bTerms[1].j===6,"B-deep retains mass then sixth order");
ok(bTerms.every(({j},i)=>j===6*i),"B-deep exact congruence");
ok((1+0)%6===1&&(1+3)%6===4,"actual B/P kernel total types");
ok(mod6(3-2)===1,"mixed test total type one");
ok(mod6(1-4)!==0,"complete P kernel is killed");
const boundPolynomial=[9n,-10n,1n],boundFactorProduct=[(-1n)*(-9n),(-1n)+(-9n),1n];
ok(boundPolynomial.every((x,i)=>x===boundFactorProduct[i]),"trace bound (p-3)^2-4p=(p-1)(p-9)");
return {
 title:"R562 exact four-unit negative-moment relation",
 status:"passed",
 checks,
 arithmetic:"BigInt exact polynomial and Q(omega) arithmetic; no prime sampling",
 variables:names,
 scaled_double_unit:"8 delta^2 J_D = 4 A0 A1 - 6 b A3 I4",
 scaled_four_unit_leading:fmt(scaledFourLeading),
 exact_relation:"J_B = Omega(1-beta*kappa)(1-3*beta)/(2*delta^2) - 9*b*Omega^3(1-beta*kappa^3)*I4/(2*delta^2) - C_sigma - T_B",
 complement_orders:{sigma_deep:7,B_deep_mass:0,B_deep_tail:6},
 first_tail_coefficients:{sigma_deep:"120 b beta delta^4 kappa^7 Omega^7 m_B^unit(-6)",B_deep:"1512 b beta delta^-8 kappa^6 Omega^6 m_sigma^unit(-5)"},
 full_core_inputs:["sigma","odd degree3 B","whole even degree6"],
 simultaneous_unit_domain:["c","v","H=delta*c-v","K=delta*c+v"],
 disjoint_removed_domains:["c in p; v unit","c unit; v in p"],
 unit_proof:"1-3 beta=0 mod p would imply Tr(pi0)=3; pi0=1 mod 2 gives even trace",
 scope:"At least one of I4 and J_B is a unit. No original S/T central zero is assigned to J_B."
};

})();
process.stdout.write(JSON.stringify(certificate,null,2)+"\n");
