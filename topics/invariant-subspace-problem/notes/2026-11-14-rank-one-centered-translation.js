"use strict";
function translateRankOneCenteredSystem(original,sValue){
 const s=BigInt(sValue),n=11,choose=(a,b)=>{let v=1n;for(let j=1;j<=b;j++)v=v*BigInt(a-j+1)/BigInt(j);return v;},gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
 const B=Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>j>i?0n:choose(i,j)*s**BigInt(i-j)));
 const mon=original.quadraticMonomials,index=new Map(mon.map((m,i)=>[m.join(","),i]));
 const equations=original.equations.map(e=>{
  const lin=Array(n).fill(0n),quad=Array(mon.length).fill(0n);
  for(let i=0;i<n;i++)for(let j=0;j<=i;j++)lin[j]+=BigInt(e.linear[i])*B[i][j];
  mon.forEach(([i,j],k)=>{const q=BigInt(e.quadratic[k]);if(!q)return;for(let a=0;a<=i;a++)for(let b=0;b<=j;b++)quad[index.get([Math.min(a,b),Math.max(a,b)].join(","))]+=q*B[i][a]*B[j][b];});
  let g=0n;for(const v of [...lin,...quad])g=gcd(g,v);if(!g)g=1n;const first=[...lin,...quad].find(v=>v!==0n);if(first<0n)g=-g;
  return {name:e.name,scale:String(BigInt(e.scale)*g),linear:lin.map(v=>String(v/g)),quadratic:quad.map(v=>String(v/g))};
 });
 const LNumerator=original.LNumerator.map(row=>Array.from({length:n},(_,j)=>String(row.reduce((v,x,i)=>v+BigInt(x)*B[i][j],0n))));
 return {...original,variables:Array.from({length:n},(_,i)=>"n"+i),equations,LNumerator,coordinateChange:{physicalParameter:String(s),formula:"m_k=sum_{j=0}^k binomial(k,j)*s^(k-j)*n_j; n_j=sum_{k=0}^j binomial(j,k)*(-s)^(j-k)*m_k",tangentVariables:["n0","n1"],normalVariables:Array.from({length:9},(_,i)=>"n"+(i+2)),originalMean:original.mean}};
}
if(typeof module!=="undefined")module.exports={translateRankOneCenteredSystem};
