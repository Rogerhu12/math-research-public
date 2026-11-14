"use strict";

function verifyR601ExactAlgebra(){
 const add=(a,b)=>Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)+(b[i]||0n));
 const sub=(a,b)=>add(a,b.map(v=>-v));
 const mul=(a,b)=>{const c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return c;};
 const sc=(k,a)=>a.map(v=>BigInt(k)*v),der=a=>a.slice(1).map((v,i)=>BigInt(i+1)*v);
 const rem=(a,d)=>{a=a.slice();for(let j=a.length-1;j>=d.length-1;j--){const v=a[j];for(let k=0;k<d.length;k++)a[j-d.length+1+k]-=v*d[k];}return a.slice(0,d.length-1);};
 const D=[-64n,0n,0n,48n,0n,0n,-228n,0n,0n,1n],x=[0n,1n],x2=[0n,0n,1n],s1=[-1n,0n,0n,1n];
 const A=mul(x,mul([-4n,0n,0n,1n],[8n,0n,0n,1n]));
 const F=[-16n,0n,0n,4328n,0n,0n,-19n],N=[0n,0n,-8n,0n,0n,34n,0n,0n,1n];
 const torsionZeta=rem(add(add(mul(mul(mul(x2,F),A),mul(s1,der(D))),sc(288,mul(mul(der(A),s1),der(D)))),add(sc(648,mul(mul(x2,A),der(D))),sc(144,mul(mul(A,s1),der(der(D)))))),D);
 if(torsionZeta.some(v=>v!==0n))throw Error("six-torsion completed-zeta formula");
 const traceE=rem(mul(N,mul(x2,F)),D)[8]||0n;
 const traceEY=rem(N,D)[8]||0n;
 const traceEX=rem(mul(mul(N,x),mul(x2,F)),D)[8]||0n;
 if(traceE!==0n || traceEY!==1n || traceEX!==-5184n)throw Error("weighted residues");
 const ds=[-64n,48n,-228n,1n],ns=[-8n,34n,1n],fs=[5184n,-16n,4328n,-19n];
 const identity=sub(mul(ns,fs),add(mul([0n,-650n,-19n],ds),[-41472n,134784n]));
 if(identity.some(v=>v!==0n))throw Error("short H1 identity");
 const fp=[-8n,-20n,1n],sp=[-1n,1n],sm4=[-4n,1n];
 const psi5=sub(sc(32,mul(mul(sp,sp),fp)),sc(27,[0n,...mul(mul(sm4,sm4),sm4)]));
 const psi6factor=sub(sub(psi5,sc(4,mul(fp,fp))),mul([8n,1n],ds));
 if(psi6factor.some(v=>v!==0n))throw Error("psi6 factorization");
 return{
  scope:"Exact universal rational algebra; no prime scan and no torsion orbit",
  psi6:"6*x*y*(x^3-4)*(x^3+8)*Delta(x)",
  eQ:"y*x^2*(-19*x^6+4328*x^3-16)/5184",
  torsion_zeta_cross_product_remainder:torsionZeta.map(String),
  trace_e_scaled_5184:String(-traceE),
  trace_y:String(-traceEY),
  trace_ex_scaled_5184:String(-traceEX),
  trace_ex_plus_y_scaled_5184:String(-traceEX-5184n*traceEY),
  short_polynomial_identity_zero:identity.every(v=>v===0n),
  psi6_factorization_zero:psi6factor.every(v=>v===0n),
  differential_identity:"partial_E T2=(D T1)/2, verified directly from T1=-(E*x+y), T2=-(E^2*y+2E*x^2+x*y)/2; D^p=B partial_E follows from R574",
  pass:true
 };
}

if (typeof module !== "undefined") {
  module.exports = { verifyR601ExactAlgebra };
  if (require.main === module) process.stdout.write(JSON.stringify(verifyR601ExactAlgebra(), null, 2) + "\n");
}
