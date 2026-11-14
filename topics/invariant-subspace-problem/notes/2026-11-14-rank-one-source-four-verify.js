"use strict";
// Exact certificate verifier for the original source s=4 system.
// All large arrays are regenerated from the original six-mode data.
function translateRankOneIntegerSystem(original,s){
 s=BigInt(s);const pow=(a,n)=>{let z=1n;while(n--)z*=a;return z;};
 const bin=(n,k)=>{let z=1n;for(let i=1;i<=k;i++)z=z*BigInt(n-i+1)/BigInt(i);return z;};
 const T=Array.from({length:11},(_,i)=>Array.from({length:11},(_,j)=>j<=i?bin(i,j)*pow(s,i-j):0n));
 const transformed={...original,variableConvention:"m_i=sum_j binomial(i,j) s^(i-j) z_j, s="+s,
  variables:Array.from({length:11},(_,i)=>"z"+i)};
 transformed.equations=original.equations.map(e=>{
  const l=e.linear.map(BigInt),q=e.quadratic.map(BigInt);
  const linear=Array.from({length:11},(_,a)=>l.reduce((z,x,i)=>z+x*T[i][a],0n));
  const quadratic=original.quadraticMonomials.map(([a,b])=>original.quadraticMonomials.reduce((z,[i,j],k)=>
   z+q[k]*(T[i][a]*T[j][b]+(a===b?0n:T[i][b]*T[j][a])),0n));
  return {...e,linear:linear.map(String),quadratic:quadratic.map(String)};
 });
 transformed.LNumerator=original.LNumerator.map(row=>T[0].map((_,j)=>String(row.reduce((a,x,i)=>a+BigInt(x)*T[i][j],0n))));
 return transformed;
}
"use strict";
function rankOneI2Projection(system){
 const columns=[],mult=[];
 for(let n=1;n<=5;n++)for(let b=0;b<=n;b++)columns.push({j:null,a:n-b,b});
 for(let j=2;j<11;j++)for(let n=0;n<=4;n++)for(let b=0;b<=n;b++)columns.push({j,a:n-b,b});
 for(let n=0;n<=3;n++)for(let b=0;b<=n;b++)mult.push({a:n-b,b});
 const key=c=>[c.j===null?"p":c.j,c.a,c.b].join(":"),index=new Map(columns.map((c,i)=>[key(c),i])),matrix=[];
 let nonzeroPureSquare=false;
 function term(q,indices,value,ex){
  if(!value)return;let j=null,a=ex.a,b=ex.b;
  for(const i of indices){if(i===0)a++;else if(i===1)b++;else {if(j!==null)return;j=i;}}
  
  const k=index.get(key({j,a,b}));if(k===undefined)throw Error("Projection column missing.");q[k]+=value;
 }
 for(const e of system.equations){
  for(let i=0;i<2;i++)if(BigInt(e.linear[i]))throw Error("Pure tangent linear term.");
  for(let k=0;k<system.quadraticMonomials.length;k++){
   const [i,j]=system.quadraticMonomials[k],v=BigInt(e.quadratic[k]);
   if(i<2&&j<2&&v){if(i!==1||j!==1)throw Error("Pure tangent term other than d^2.");nonzeroPureSquare=true;}
  }
  for(const ex of mult){
   const r=Array(columns.length).fill(0n);
   for(let i=0;i<11;i++)if(BigInt(e.linear[i]))term(r,[i],BigInt(e.linear[i]),ex);
   for(let k=0;k<system.quadraticMonomials.length;k++)if(BigInt(e.quadratic[k]))term(r,system.quadraticMonomials[k],BigInt(e.quadratic[k]),ex);
   matrix.push(r);
  }
 }
 if(!nonzeroPureSquare)throw Error("This projection requires a nonzero pure d^2 coefficient.");
 for(let j=2;j<11;j++)for(let n=0;n<=2;n++)for(let b=0;b<=n;b++){const r=Array(columns.length).fill(0n);r[index.get(key({j,a:n-b,b:b+2}))]=1n;matrix.push(r);}
 return {columns,multipliers:mult,matrix:matrix.map(r=>r.map(String)),ambient:4367,killed:4212};
}



async function verifyRankOneSourceFour(data,certificate,buildSystem,rankFunction,report){
 const source=4n,mean=Array.from({length:6},(_,i)=>String(source**BigInt(i)));
 const system=translateRankOneIntegerSystem(buildSystem(data,mean),source),P=rankOneI2Projection(system);
 const {free,kernels}=certificate.smallProjection;
 if(P.matrix.length!==224||P.columns.length!==155||kernels.length!==13||free.length!==13)throw Error("Wrong dimensions");
 let exactZeroChecks=0,independenceChecks=0;
 for(let k=0;k<13;k++){
  const v=kernels[k].map(BigInt);if(v.length!==155)throw Error("Wrong kernel length");
  for(const row of P.matrix){let dot=0n;for(let j=0;j<155;j++)dot+=BigInt(row[j])*v[j];if(dot)throw Error("Nonzero integer kernel dot product");exactZeroChecks++;}
  for(let j=0;j<13;j++){if(k===j?v[free[j]]===0n:v[free[j]]!==0n)throw Error("Free coordinates do not form a nonzero diagonal");independenceChecks++;}
 }
 const K=data.K.map(r=>r.map(BigInt)),y=mean.map(BigInt),u=Array.from({length:6},(_,i)=>i?BigInt(i)*source**BigInt(i-1):0n);
 const pairing=(x,z)=>x.reduce((a,v,i)=>a+v*K[i].reduce((b,k,j)=>b+k*z[j],0n),0n);
 if(pairing(y,y)!==0n||pairing(y,u)!==0n||pairing(u,u)!==-640n)throw Error("Original tangent Gram entries mismatch");
 const result={source:"4",smallProjection:{rows:224,columns:155,independentIntegerKernels:13,exactZeroChecks,independenceChecks,rankUpper:142},fullRationalRankUpper:4354,originalGram:{yy:"0",yu:"0",uu:"-640"}};
 if(rankFunction){
  result.modular=await rankFunction(system,5,report);
  if(result.modular.field!==31||result.modular.rows!==6188||result.modular.columns!==4367||result.modular.rank!==4354)throw Error("Macaulay rank mismatch");
  if(result.modular.coordinateSquareMembership.slice(2).some(x=>!x))throw Error("Transverse square missing");
  result.characteristicZeroConclusion="I_normal^2 in degree at most five is contained in the original ideal; all transverse variables vanish; the nonzero original tangent Gram entry then forces d=0.";
 }
 return result;
}
if(typeof module!=="undefined")module.exports={verifyRankOneSourceFour,translateRankOneIntegerSystem,rankOneI2Projection};
if(typeof require!=="undefined"&&require.main===module){
 const fs=require("fs"),path=require("path");
 const data=JSON.parse(fs.readFileSync(path.join(__dirname,"2026-11-13-six-mode-cubic-bell-third-moment-exact-data.json"),"utf8"));
 const certificate=JSON.parse(fs.readFileSync(path.join(__dirname,"2026-11-14-rank-one-source-four-verification.json"),"utf8"));
 const {buildRankOneCenteredIntegerSystem}=require("./2026-11-14-rank-one-centered-integer-system-generator.js");
 const {rankOneMacaulayF31}=require("./2026-11-14-rank-one-macaulay-f31.js");
 verifyRankOneSourceFour(data,certificate,buildRankOneCenteredIntegerSystem,rankOneMacaulayF31,p=>process.stderr.write(JSON.stringify(p)+"\n")).then(r=>process.stdout.write(JSON.stringify(r,null,2)+"\n")).catch(e=>{console.error(e);process.exitCode=1;});
}
