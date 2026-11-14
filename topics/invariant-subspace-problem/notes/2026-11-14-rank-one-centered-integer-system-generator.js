"use strict";
/*
Input: the already published exact-data JSON containing K, adjugateJ3, detJ3.
No matrix inversion or floating-point arithmetic is used.
*/
function buildRankOneCenteredIntegerSystem(data,meanCoordinates){
 const K=data.K.map(row=>row.map(BigInt)),adj=data.adjugateJ3.map(row=>row.map(BigInt)),
  D=BigInt(data.detJ3),y=meanCoordinates.map(BigInt),n=6;
 const mm=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((z,a,k)=>z+a*B[k][j],0n)));
 const mv=(A,b)=>A.map(row=>row.reduce((z,a,i)=>z+a*b[i],0n));
 const tr=A=>A.reduce((z,row,i)=>z+row[i],0n),dot=(a,b)=>a.reduce((z,x,i)=>z+x*b[i],0n);
 const p=mv(K,y);
 if(dot(y,p)!==0n||y.every(x=>x===0n))throw Error("nonzero physical mean required");
 for(let i=0;i<5;i++)for(let j=0;j<5;j++)
  if(y[i+1]*y[j]!==y[i]*y[j+1])throw Error("mean is not rank one");
 const J2=Array.from({length:11},()=>Array(11).fill(0n));
 for(let i=0;i<6;i++)for(let j=0;j<6;j++)for(let k=0;k<6;k++)for(let l=0;l<6;l++)
  J2[i+k][j+l]+=K[i][j]*K[k][l];
 const B=Array.from({length:16},(_,i)=>Array.from({length:11},(_,j)=>
  i-j>=0&&i-j<=5?p[i-j]:0n));
 const Lnum=mm(mm(adj,B),J2),Bt=B[0].map((_,j)=>B.map(row=>row[j])),
  Anum=mm(Bt,Lnum),Nlinear=mm(J2,Anum).map(row=>row.map(x=>6n*x));
 const evaluateQuadratic=seq=>{
  const M=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>seq[i+j])),
   KM=mm(K,M),MKM=mm(mm(M,K),M),KMK=mm(KM,K),
   Nt=mm(mm(K,MKM),K),tau=tr(mm(KM,KM)),MKMp=mv(MKM,p),
   ell=mv(Lnum,seq),out=Array(17).fill(0n);
  for(let i=0;i<6;i++)for(let j=0;j<6;j++)out[i+j]+=4n*D*Nt[i][j];
  for(let i=0;i<6;i++){
   let contraction=0n;for(let j=0;j<6;j++)for(let k=0;k<6;k++)
    contraction+=ell[i+j+k]*KMK[j][k];
   out[11+i]=2n*D*tau*y[i]+8n*D*MKMp[i]-12n*contraction;
  }return out;
 };
 const basis=Array.from({length:11},(_,i)=>Array.from({length:11},(_,j)=>i===j?1n:0n)),
  diagonal=basis.map(evaluateQuadratic),quadratic=Array.from({length:17},()=>[]),monomials=[];
 for(let i=0;i<11;i++)for(let j=i;j<11;j++){
  monomials.push([i,j]);
  const value=i===j?diagonal[i]:evaluateQuadratic(basis[i].map((x,k)=>x+basis[j][k]))
   .map((x,k)=>x-diagonal[i][k]-diagonal[j][k]);
  value.forEach((x,k)=>quadratic[k].push(x));
 }
 const gcd=(a,b)=>{if(a<0n)a=-a;if(b<0n)b=-b;while(b)[a,b]=[b,a%b];return a;};
 const equations=quadratic.map((q,i)=>{
  const linear=i<11?Nlinear[i]:Array(11).fill(0n),all=linear.concat(q);
  let scale=all.reduce(gcd,0n);if(!scale)throw Error("zero generator");
  if(all.find(x=>x!==0n)<0n)scale=-scale;
  return {name:i<11?"N"+i:"Gamma"+(i-11),scale:String(scale),
   linear:linear.map(x=>String(x/scale)),quadratic:q.map(x=>String(x/scale))};
 });
 return {format:"rank-one-centered-17-original-equations-v1",mean:y.map(String),
  variables:Array.from({length:11},(_,i)=>"m"+i),quadraticMonomials:monomials,
  denominator:String(D),normalization:"D times each original N/Gamma coefficient equals scale times the stored primitive equation.",
  LNumerator:Lnum.map(row=>row.map(String)),equations,
  sourceData:"2026-11-13-six-mode-cubic-bell-third-moment-exact-data.json",
  highest:"H=M+y^2/2; V=(3/2)L_y(M)+y^3/2; T3=6(L_y(M)-yM)",
  scope:"All seventeen original low equations; A_yM need not vanish."};
}
if(typeof module!=="undefined")module.exports={buildRankOneCenteredIntegerSystem};
if(typeof require!=="undefined"&&require.main===module){
 const fs=require("fs"),path=require("path"),input=process.argv[2]||
  path.join(__dirname,"2026-11-13-six-mode-cubic-bell-third-moment-exact-data.json");
 const data=JSON.parse(fs.readFileSync(input,"utf8")),label=process.argv[3]||"zero",
  y=label==="infinity"?[0,0,0,0,0,1]:[1,0,0,0,0,0];
 console.log(JSON.stringify(buildRankOneCenteredIntegerSystem(data,y),null,2));
}
