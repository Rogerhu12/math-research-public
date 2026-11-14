"use strict";
function verifyE8Irreducibility(){
 const p=53,E=[9600,-25472,-3392,15936,-2888,-936,153,50,5],F=[750000000,-398000000,-10600000,9960000,-361000,-23400,765,50,1],md=x=>(x%p+p)%p,trim=a=>{while(a.length>1&&!a[a.length-1])a.pop();return a;};
 const inv=a=>{let z=1;while(a*z%p!==1)z++;return z;},sub=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>md((a[i]||0)-(b[i]||0)))),add=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>md((a[i]||0)+(b[i]||0))));
 const mul=(a,b)=>{let c=Array(a.length+b.length-1).fill(0);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]=(c[i+j]+a[i]*b[j])%p;return trim(c);};
 const div=(a,b)=>{a=trim(a.slice());const q=Array(Math.max(1,a.length-b.length+1)).fill(0),iv=inv(b[b.length-1]);while(a.length>=b.length&&a.some(Boolean)){const j=a.length-b.length,c=a[a.length-1]*iv%p;q[j]=c;for(let i=0;i<b.length;i++)a[j+i]=md(a[j+i]-c*b[i]);trim(a);}return {q:trim(q),r:a};};
 const f=F.map(md),mulmod=(a,b)=>div(mul(a,b),f).r,pow=(a,n)=>{let r=[1];while(n){if(n%2)r=mulmod(r,a);a=mulmod(a,a);n=Math.floor(n/2);}return r;};
 let h=[0,1];const frobenius=[];for(let k=1;k<=8;k++){h=pow(h,p);frobenius.push(h);}
 if(JSON.stringify(h)!==JSON.stringify([0,1]))throw Error("Frobenius degree-eight identity failed");
 const h4minusX=sub(frobenius[3],[0,1]);let r0=f,r1=h4minusX,s0=[1],s1=[0],t0=[0],t1=[1];
 while(r1.some(Boolean)){const {q,r}=div(r0,r1);[r0,r1]=[r1,r];[s0,s1]=[s1,sub(s0,mul(q,s1))];[t0,t1]=[t1,sub(t0,mul(q,t1))];}
 if(r0.length!==1||!r0[0])throw Error("Rabin gcd failed");const a=inv(r0[0]),U=s0.map(x=>x*a%p),V=t0.map(x=>x*a%p),identity=add(mul(U,f),mul(V,h4minusX));if(JSON.stringify(identity)!=="[1]")throw Error("Bezout identity failed");
 for(let i=0;i<8;i++)if(BigInt(E[i])*5n**BigInt(7-i)!==BigInt(F[i]))throw Error("theta polynomial mismatch");
 const evalMod=(coeff,x,prime)=>coeff.reduceRight((v,c)=>((v*x+c)%prime+prime)%prime,0),theta=8,prime=17,derivative=F.slice(1).map((x,i)=>x*(i+1));
 if(evalMod(F,theta,prime)!==0||evalMod(derivative,theta,prime)===0)throw Error("Chosen simple residue root failed");
 return {thetaPolynomial:F,sourcePolynomial:E,irreducibilityPrime:p,reducedThetaPolynomial:f,frobenius,bezout:{U,V,h4minusX,identity},simpleResidueRoot:{prime,source:5,theta,thetaDerivative:evalMod(derivative,theta,prime),sourceDerivative:evalMod(E.slice(1).map((x,i)=>x*(i+1)),5,prime),tangentGram:((-2*5*5*(5-2)*(5+6))%17+17)%17,detJ3Residue:Number(23366320238786911411830138211362846399922176000n%17n)},conclusion:"The monic theta polynomial is irreducible over F53 and Q; theta=8 is a simple root modulo 17."};
}
if(typeof module!=="undefined")module.exports={verifyE8Irreducibility};
if(typeof require!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(verifyE8Irreducibility(),null,2)+"\n");
