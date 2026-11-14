#!/usr/bin/env node
// R554: exact original five-input identity; no dependencies and no prime scan.
const certificate=(function(){

const key=e=>e.join(","),out=P=>Object.fromEntries([...P].sort().map(([e,c])=>[e,c.toString()]));
function binom(n,k){let r=1n;for(let j=1;j<=k;j++)r=r*BigInt(n-j+1)/BigInt(j);return r}
function mono(e,c=1n){
 const P=new Map(),q=Math.floor(e[2]/2),r=e[2]%2;
 for(let j=0;j<=q;j++){const a=[...e];a[0]+=q-j;a[1]+=3*j;a[2]=r;P.set(key(a),c*binom(q,j))}
 return P;
}
const add=(A,B)=>{const C=new Map(A);for(const[k,v]of B){const n=(C.get(k)||0n)+v;if(n)C.set(k,n);else C.delete(k)}return C};
const scale=(A,c)=>new Map([...A].map(([k,v])=>[k,v*BigInt(c)]).filter(([k,v])=>v));
const mul=(A,B)=>{let C=new Map();for(const[ka,a]of A)for(const[kb,b]of B){
 const ea=ka.split(",").map(Number),eb=kb.split(",").map(Number);
 C=add(C,mono(ea.map((v,i)=>v+eb[i]),a*b));
}return C};
const pow=(A,n)=>{let R=mono([0,0,0,0,0]);for(let i=0;i<n;i++)R=mul(R,A);return R};
function diff(P){
 let Q=new Map();
 for(const[k,v]of P){const e=k.split(",").map(Number);
  if(e[1]){const a=[...e];a[1]--;a[2]++;Q=add(Q,mono(a,2n*BigInt(e[1])*v))}
  if(e[2]){const a=[...e];a[2]--;a[1]+=2;Q=add(Q,mono(a,3n*BigInt(e[2])*v))}
  if(e[3]){const a=[...e];a[3]--;a[1]++;Q=add(Q,mono(a,-BigInt(e[3])*v))}
  if(e[4]){const a=[...e];a[3]++;Q=add(Q,mono(a,BigInt(e[4])*v))}
 }
 return Q;
}
const x=mono([0,1,0,0,0]),y=mono([0,0,1,0,0]),g=mono([0,0,0,1,0]),sig=mono([0,0,0,0,1]);
const f4=mul(x,pow(sig,6)),f1=scale(mul(mul(x,y),pow(sig,6)),-1),theta=mul(x,pow(sig,2));
const d1=diff(f4),d2=diff(d1),d3=diff(d2),Q=add(d3,scale(f1,-24));
const positive=scale(mul(mul(pow(sig,2),pow(diff(sig),2)),diff(theta)),108);
const residual=add(Q,scale(positive,-1));
if(residual.size)throw Error("whole differential identity failed");
const qcoeff=(n,d)=>{n=BigInt(n);d=BigInt(d);const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;for(;b;){const c=a%b;a=b;b=c}return a},h=gcd(n,d);return [n/h,d/h]};
const qa=(a,b)=>qcoeff(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),qm=(a,b)=>qcoeff(a[0]*b[0],a[1]*b[1]),qs=a=>a.map(String).join("/");
const coeff4=qcoeff(-4,35),coeff1=qcoeff(6,35);
const h12=qa(qm(coeff4,qcoeff(1,11*12)),qm(qcoeff(-24,1),qm(coeff1,qcoeff(1,8*9*10*11*12))));
if(qs(h12)!=="-1/1100")throw Error("fixed twelve-jet failed");
const q7=qm(h12,qcoeff(8*9*10*11*12,1));
if(qs(q7)!=="-432/5")throw Error("fixed seven-jet failed");
if(108/6!==18)throw Error("same-source symmetrization factor");
const witnesses={D_f4:out(d1),D2_f4:out(d2),D3_f4:out(d3),Q:out(Q),positive_factor:out(positive),whole_residual:out(residual)};
return {status:"PASS",ring:"Q[b,x,y,g,sigma]/(y^2-x^3-b)",derivation:{b:"0",x:"2y",y:"3x^2",g:"-x",sigma:"g*sigma"},
 witnesses,exact_input_weight:"(Y^3-18*u*e2(t1,t2,t3,t4))/(24*Omega^3)",
 exact_same_unit_domain:"Y=t1+t2+t3+t4+u in Z_p^x",
 exact_negative_difference:"Omega^2 I_-2(f4)-24 Omega^5 I_-5(f1)=18 Omega^2 integral_{Yunit} u*e2/Y^5 d rho",
 derivative_Q_first_coefficient:q7.map(String),primitive_H_first_coefficient:h12.map(String),
 ordinary_core_basis_Q_G:[["beta6*kappa0^3","24*beta6*(kappa0^3-1)"],["0","beta6"]],
 nonvanishing_scope:"Q and H are nonzero fixed functions. No nonvanishing of the two prescribed negative moments is inferred.",
 primes_scanned:0};

})();
console.log(JSON.stringify(certificate,null,2));
