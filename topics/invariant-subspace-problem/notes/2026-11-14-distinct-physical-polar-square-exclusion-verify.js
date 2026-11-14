"use strict";
function verifyDistinctPhysicalPolarSquareExclusion(){
 const K=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],[0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]].map(r=>r.map(BigInt));
 const E=[9600,-25472,-3392,15936,-2888,-936,153,50,5].map(BigInt),prime=103n;
 const data=[
 {name:"plus",P:[-8,32,-25,5],U:[10,64,93,8,75,43,39,56],V:[48,80,47]},
 {name:"minus",P:[864,864,135,5],U:[42,33,59,61,54,92,11,38],V:[77,64,65]}
 ];
 const mod=n=>(n%prime+prime)%prime;
 const mul=(a,b)=>{const c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return c};
 const certificates=[];
 for(const d of data){const P=d.P.map(BigInt),U=d.U.map(BigInt),V=d.V.map(BigInt),a=mul(U,P),b=mul(V,E);const out=Array.from({length:Math.max(a.length,b.length)},(_,i)=>mod((a[i]||0n)+(b[i]||0n)));if(out.some((x,i)=>x!==(i?0n:1n)))throw Error("Bezout "+d.name);if(mod(P[P.length-1])===0n||mod(E[E.length-1])===0n)throw Error("degree loss");certificates.push({...d,identity:"U P + V E8 = 1 mod 103",retained_degrees:[3,8]});}
 function polar(s){const v=Array(6).fill(1n);for(let i=1;i<6;i++)v[i]=v[i-1]*s;return K.map(r=>r.reduce((t,a,i)=>t+a*v[i],0n));}
 const p5=polar(5n),pm1=polar(-1n),p0=polar(0n),pinf=K.map(r=>r[5]);
 if(p5[0]!==0n||p5[1]!==-4000n||pm1[5]!==0n||pm1[4]!==5n)throw Error("exceptional contacts");
 if(p0.some((c,i)=>c!==(i===4?5n:i===5?-1n:0n))||pinf.some((c,i)=>c!==(i===0||i===1?-1n:0n)))throw Error("exceptional value polars");
 return {status:"PASS",arithmetic:"exact BigInt, two retained-degree modular Bezout identities and original-K exceptional polars",prime:"103",certificates,E8:E.map(String),exceptional_checks:{p5_at_zero_order:1,p5_linear_coefficient:String(p5[1]),pminus1_at_infinity_order:1,pminus1_z4_coefficient:String(pm1[4]),p0:p0.map(String),pinfinity:pinf.map(String)}};
}
if(typeof module!=="undefined")module.exports={verifyDistinctPhysicalPolarSquareExclusion};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(verifyDistinctPhysicalPolarSquareExclusion(),null,2)+"\n");
