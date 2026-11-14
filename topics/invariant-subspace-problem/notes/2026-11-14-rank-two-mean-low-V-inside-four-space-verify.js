"use strict";
function verifyLowVE4Blocks(){
 const names=["c","F","l1","l2","n1","n2","g","h","k","v"],d=names.length,Z="0".repeat(d);
 const zero=()=>new Map(),one=n=>n?new Map([[Z,BigInt(n)]]):zero(),varp=i=>new Map([[Array.from({length:d},(_,j)=>i===j?"1":"0").join(""),1n]]);
 const add=(...ps)=>{const q=zero();for(const p of ps)for(const [m,a]of p)q.set(m,(q.get(m)||0n)+a);for(const[m,a]of q)if(a===0n)q.delete(m);return q};
 const sc=(p,a)=>new Map([...p].map(([m,c])=>[m,c*BigInt(a)]).filter(([m,c])=>c!==0n));
 const mul=(p,q)=>{const r=zero();for(const[m,a]of p)for(const[n,b]of q){const k=[...m].map((t,i)=>(parseInt(t,36)+parseInt(n[i],36)).toString(36)).join("");r.set(k,(r.get(k)||0n)+a*b)}for(const[m,a]of r)if(a===0n)r.delete(m);return r};
 const prod=(...ps)=>ps.reduce(mul,one(1)),sq=p=>mul(p,p),dot=(a,b)=>add(...a.map((p,i)=>mul(p,b[i]))),mm=(a,b)=>a.map(r=>b[0].map((_,j)=>dot(r,b.map(r=>r[j]))));
 const [c,F,l,m,n,o,g,h,k,v]=names.map((_,i)=>varp(i)),checks=[];
 const check=(name,a,b)=>{if(add(a,sc(b,-1)).size)throw new Error(name);checks.push(name)};
 for(const mode of ["reduced","double"]){
  const red=mode==="reduced",kap=red?add(one(1),sc(c,-2)):one(1),K=[[sc(F,2),zero(),l,m],[zero(),red?sc(F,-2):zero(),n,o],[l,n,zero(),g],[m,o,g,zero()]],Y=[one(1),zero(),zero(),zero()];
  const A=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>i===j?(red?[sc(c,2),sc(c,2),sc(h,4),sc(k,4)]:[zero(),sc(c,4),sc(h,4),sc(k,4)])[i]:zero()));
  const B=Array.from({length:4},()=>Array.from({length:4},()=>Array.from({length:4},zero)));
  if(red)B[0][0][0]=c;
  B[0][1][1]=B[1][0][1]=B[1][1][0]=sc(c,red?1:2);B[2][2][2]=sc(v,4);
  const p=K.map(r=>dot(r,Y)),Ap=A.map(r=>dot(r,p)),KA=mm(K,A),AKA=mm(A,KA),KAK=mm(KA,K),AKAp=AKA.map(r=>dot(r,p));
  const Q8=add(sc(sq(F),8),sc(dot(p,Ap),-4),add(...mm(KA,KA).map((r,i)=>r[i])));
  const G8=Array.from({length:4},(_,i)=>{let bpp=zero(),bk=zero();for(let j=0;j<4;j++)for(let r=0;r<4;r++){bpp=add(bpp,prod(B[i][j][r],p[j],p[r]));bk=add(bk,mul(B[i][j][r],KAK[j][r]));}return add(mul(Q8,Y[i]),sc(prod(F,Ap[i]),-8),sc(AKAp[i],4),sc(bpp,8),sc(bk,-4));});
  const Ttwice=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>Array.from({length:4},(_,r)=>add(sc(prod(Y[i],Y[j],Y[r]),2),sc(mul(Y[i],A[j][r]),-1),sc(mul(Y[j],A[i][r]),-1),sc(mul(Y[r],A[i][j]),-1),sc(B[i][j][r],2)))));
  const N4=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>add(sc(dot(Ttwice[i][j],p),2),sc(prod(F,Y[i],Y[j]),-4),sc(mul(F,A[i][j]),2),AKA[i][j])));
  const bR=add(prod(h,l,l),prod(k,m,m));
  const wantG=[add(prod(kap,kap,F,F),sc(mul(kap,bR),-2),sc(prod(h,k,g,g),4)),zero(),add(sc(prod(kap,F,h,l),-4),sc(prod(h,k,g,m),8),sc(prod(red?add(one(1),sc(c,-1)):one(1),v,l,l),4),sc(prod(c,v,n,n),red?-4:-8),sc(prod(v,k,g,g),-8)),add(sc(prod(kap,F,k,m),-4),sc(prod(h,k,g,l),8))];
  const N=Array.from({length:4},()=>Array.from({length:4},zero));
  N[0][0]=red?prod(kap,add(one(1),sc(c,-1)),F):F;N[1][1]=red?prod(c,kap,F):sc(prod(c,F),2);
  N[0][2]=N[2][0]=sc(prod(red?add(one(1),sc(c,-1)):one(1),h,l),-2);
  N[0][3]=N[3][0]=sc(prod(red?add(one(1),sc(c,-1)):one(1),k,m),-2);
  N[1][2]=N[2][1]=sc(prod(c,h,n),red?2:4);N[1][3]=N[3][1]=sc(prod(c,k,o),red?2:4);
  N[2][2]=add(sc(prod(F,h),-2),sc(prod(v,l),4));N[3][3]=sc(prod(F,k),-2);N[2][3]=N[3][2]=sc(prod(h,k,g),4);
  for(let i=0;i<4;i++){check(mode+" G "+i,G8[i],sc(wantG[i],8));for(let j=0;j<4;j++)check(mode+" N "+i+","+j,N4[i][j],sc(N[i][j],4));}
  const qX=add(prod(kap,l,l),sc(prod(k,g,g),-6)),qZ=add(prod(kap,m,m),sc(prod(h,g,g),-6));
  check(mode+" conic 20 identity",add(wantG[0],sc(mul(h,qX),2),sc(mul(k,qZ),2)),add(prod(kap,kap,F,F),sc(prod(h,k,g,g),-20)));
 }
 return {status:"PASS",arithmetic:"exact BigInt polynomial ring over Z; original H and V stored as 4H and 4V",checks:checks.length,identities:checks};
}
if(typeof module!=="undefined")module.exports={verifyLowVE4Blocks};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(verifyLowVE4Blocks(),null,2)+"\n");
