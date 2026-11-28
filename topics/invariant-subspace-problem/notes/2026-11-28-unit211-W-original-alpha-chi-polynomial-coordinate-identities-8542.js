(()=>{
"use strict";
// NEW exact, denominator-cleared polynomial-coordinate identities.
// The original R identity is the corrected true-dual-germ identity,
// not the retracted compact Rbad. No old Gram/determinant gate is run.
const began=Date.now(),names=["u","ell","Q","f","t","A1","e","k","alpha","chi"],n=names.length;
const key0=Array(n).fill(0).join(",");let products=0;
function c(v=0n){v=BigInt(v);return v?new Map([[key0,v]]):new Map()}
function vr(i){let a=Array(n).fill(0);a[i]=1;return new Map([[a.join(","),1n]])}
function add(a,b){let p=new Map(a);for(const[k,v]of b){let w=(p.get(k)||0n)+v;if(w)p.set(k,w);else p.delete(k)}return p}
function neg(a){return new Map([...a].map(([k,v])=>[k,-v]))}
function sub(a,b){return add(a,neg(b))}
function mul(a,b){
 if(Date.now()-began>30000)throw Error("new coordinate identity 30 second bound");
 products++;let p=new Map();
 for(const[ka,va]of a){const ea=ka.split(",").map(Number);
  for(const[kb,vb]of b){const eb=kb.split(",").map(Number),key=ea.map((x,j)=>x+eb[j]).join(","),z=(p.get(key)||0n)+va*vb;
   if(z)p.set(key,z);else p.delete(key)}}
 return p;
}
function sc(a,v){return mul(a,c(v))}
function sq(a){return mul(a,a)}
function sum(a){return a.reduce(add,c())}
function pr(a){return a.reduce(mul,c(1))}
function degree(p,j){return Math.max(-1,...[...p.keys()].map(k=>Number(k.split(",")[j])))}
const one=c(1),[u,l,Q,f,t,A1,e,k,al,chi]=names.map((_,i)=>vr(i));
const delta=sub(one,Q),m=sub(u,l),a=sub(one,l),eta=sub(f,u);
const Uhat=sub(u,mul(l,Q)),V2=sub(sc(u,2),mul(l,Q));
const T0=sub(V2,sc(sq(u),2)),M=sub(mul(l,V2),sq(u));
const Z=add(mul(u,sub(u,one)),pr([l,a,Q]));
const C=add(sub(u,one),mul(a,Q));
const Rw=sum([sc(mul(u,sub(one,u)),2),neg(mul(u,Q)),pr([sub(sc(u,2),one),l,Q])]);
const alpha=sub(sc(mul(delta,eta),4),mul(Uhat,t));
const checks=[];
function check(name,p){if(p.size)throw Error(name+" has "+p.size+" nonzero coefficients");checks.push({name,fullIntegerPolynomialDifferenceZero:true})}
check("weight_identity_UhatZ_minus_MC",add(sub(mul(Uhat,Z),mul(M,C)),mul(m,Rw)));
check("weight_identity_2uZ_plus_mT0",sum([sc(mul(u,Z),2),mul(m,T0),mul(l,Rw)]));
// V=f+bc*t-A1/2, bc=M/(4delta): Vnum=4delta*V.
const Vnum=sum([sc(mul(delta,f),4),mul(M,t),sc(mul(delta,A1),-2)]);
// Rclear=8delta^2*R, with the complete original R after E0.
const Rclear=sum([
 sc(pr([delta,eta,sub(mul(M,t),sc(mul(delta,A1),2))]),8),
 sc(pr([delta,M,sq(t)]),2),
 sc(pr([delta,M,u,t]),8),
 sc(pr([delta,l,Vnum,t]),-2),
 sc(pr([delta,m,add(T0,sc(mul(u,f),4)),t]),4),
 sc(pr([m,Vnum,t]),-2)
]);
check("full_original_R_A1_linear_identity",
 sub(add(Rclear,sc(pr([delta,alpha,A1]),4)),
 mul(t,sum([sc(pr([delta,Z,f]),8),sc(pr([M,C,t]),-2),sc(pr([delta,m,T0]),4)]))));
// The same original R is linear in f,t after r=A1/t.
const r2num=add(chi,Z); // r=(chi+Z)/(2delta).
const den=mul(m,Rw);
const Nt=neg(add(mul(al,chi),sc(pr([delta,l,Rw]),2))); // den*t.
const Nf=sum([sc(pr([delta,u,den]),4),mul(al,den),mul(Uhat,Nt)]); // 4delta*den*f.
const NV=add(Nf,mul(sub(sub(M,Z),chi),Nt)); // 4delta*den*V.
const NA=mul(r2num,Nt); // 2delta*den*A1.
check("A1_from_original_Gram_after_new_map",sub(add(sub(Nf,NV),mul(M,Nt)),NA));
check("same_alpha_recovered",sub(sub(sub(Nf,sc(pr([delta,u,den]),4)),mul(Uhat,Nt)),mul(al,den)));
check("same_chi_recovered_without_dividing_t",sub(sub(NA,mul(Z,Nt)),mul(chi,Nt)));
check("full_original_R_return_after_new_map",
 sub(pr([al,NA,den]),mul(Nt,sum([mul(Z,Nf),neg(pr([M,C,Nt])),sc(pr([delta,den,m,T0]),2)]))));
// W1=(T0+4u*f)/2, denominator 8delta*den.
const NW=add(sc(pr([delta,den,T0]),4),sc(mul(u,Nf),4));
const NX=sub(sc(mul(Uhat,NV),2),mul(m,NW));
const NY=sub(mul(l,NW),sc(mul(u,NV),2));
check("original_weighted_V_reconstruction",sub(add(mul(l,NX),mul(m,NY)),sc(mul(M,NV),2)));
check("original_weighted_W1_reconstruction",sub(add(mul(u,NX),mul(Uhat,NY)),mul(M,NW)));
check("original_f_from_E0_reconstruction",
 sub(sub(add(mul(u,NX),mul(Uhat,NY)),sc(pr([delta,den,M,T0]),4)),sc(pr([u,M,Nf]),4)));
// Current W specialization pays Rw by the already proved entire H_old theorem.
const uw=add(e,one),Vbar=add(mul(uw,k),c(2));
const H=sum([sc(mul(e,k),4),neg(sq(k)),sc(k,-4),c(-8)]);
const Lnum=mul(uw,sub(sq(add(k,c(2))),sc(mul(e,k),2)));
const Lden=mul(k,Vbar),Qw=mul(e,k);
check("entire_W_Rw_equals_minus_u_e2_H_over_Vbar",
 sum([mul(Lden,sub(sc(mul(uw,sub(one,uw)),2),mul(uw,Qw))),
 pr([sub(sc(uw,2),one),Lnum,Qw]),pr([uw,sq(e),H,k])]));
return {
 schema:"isp-W-original-alpha-chi-polynomial-coordinate-identities-v1",
 variables:names,
 elapsed_milliseconds:Date.now()-began,
 integerPolynomialProducts:products,checks,
 numeratorAlphaDegrees:{t:degree(Nt,8),f:degree(Nf,8),V:degree(NV,8),A1:degree(NA,8),x:degree(NX,8),y:degree(NY,8)},
 numeratorChiDegrees:{t:degree(Nt,9),f:degree(Nf,9),V:degree(NV,9),A1:degree(NA,9),x:degree(NX,9),y:degree(NY,9)},
 coordinateDenominators:"only rational constants and delta*m*Rw*M; Rw=-u*e^2*H_old/Vbar on W",
 inverseMapRequiresOnlyPreviouslyPaidT:true,
 alphaZeroKeptByPolynomialIdentities:true,
 noGammaOrNewParameterHeadInverted:true,
 allOriginalValuesStillRequired:true,
 noNewExclusionClaim:true,ordinaryISPClaim:false,
 actualExecution:"pure V8 BigInt exact integer polynomial arithmetic"
};
})()
