"use strict";
// Exact F_17/F_19 row spans; the optional target stops after a proved lower bound.
async function rankOneMacaulayF17F19(z,D,p,report,targetRank){
 if(p!==17&&p!==19)throw new Error("Supported primes are 17 and 19");
 const vars=Array.from({length:11},(_,i)=>8**i),listDeg=d=>{const a=[];const rec=(i,k,v)=>{if(!k){a.push(v);return;}for(let j=i;j<11;j++)rec(j,k-1,v+vars[j]);};rec(0,d,0);return a;};
 const degrees=Array.from({length:D+1},(_,d)=>listDeg(d)),cols=degrees.slice(1).reverse().flat(),index=new Map(cols.map((x,i)=>[x,i])),nw=Math.ceil(cols.length/32),bit1one=p===19;
 const md=x=>Number((BigInt(x)%BigInt(p)+BigInt(p))%BigInt(p)),rows=z.equations.map(e=>{const a=[];e.quadratic.forEach((x,j)=>{const v=md(x);if(v){const[i,k]=z.quadraticMonomials[j];a.push([vars[i]+vars[k],v]);}});e.linear.forEach((x,j)=>{const v=md(x);if(v)a.push([vars[j],v]);});return a;});
 const inv=Array(p).fill(0);for(let i=1;i<p;i++){let v=1;while(v*i%p!==1)v++;inv[i]=v;}
 const piv=Array(cols.length);let rank=0,processed=0,ops=0,last=Date.now(),stopped=false;
 function add(r,q,w0){
  for(let w=w0;w<nw;w++){
   const a0=r[w],a1=r[nw+w],a2=r[2*nw+w],a3=r[3*nw+w],a4=r[4*nw+w],b0=q[w],b1=q[nw+w],b2=q[2*nw+w],b3=q[3*nw+w],b4=q[4*nw+w];
   const s0=a0^b0;let c=a0&b0;const x1=a1^b1,s1=x1^c;c=(a1&b1)|(x1&c);const x2=a2^b2,s2=x2^c;c=(a2&b2)|(x2&c);const x3=a3^b3,s3=x3^c;c=(a3&b3)|(x3&c);const x4=a4^b4,s4=x4^c,s5=(a4&b4)|(x4&c);
   const d0=~s0;let b=~s0;const d1=bit1one?~(s1^b):s1^b;b=bit1one?(~s1|b):(~s1&b);const d2=s2^b;b=~s2&b;const d3=s3^b;b=~s3&b;const d4=~(s4^b);b=~s4|b;const take=~(~s5&b);
   r[w]=s0^(take&(s0^d0));r[nw+w]=s1^(take&(s1^d1));r[2*nw+w]=s2^(take&(s2^d2));r[3*nw+w]=s3^(take&(s3^d3));r[4*nw+w]=s4^(take&(s4^d4));
  }
 }
 function multiples(r,c,f){const all=[r];for(let k=2;k<p;k++){const q=all[k-2].slice();add(q,r,c>>>5);all.push(q);}const q=Array.from({length:p-1},(_,i)=>all[((i+1)*inv[f]%p)-1]);for(let i=0;i<p-1;i++){let v=0;for(let j=0;j<5;j++)v|=((q[i][j*nw+(c>>>5)]>>>(c&31))&1)<<j;if(v!==i+1)throw new Error("Bad pivot scalar multiple");}return q;}
 function reduce(r,insert){
  for(let w=0;w<nw;w++){let nz=r[w]|r[nw+w]|r[2*nw+w]|r[3*nw+w]|r[4*nw+w];while(nz){const bit=31-Math.clz32(nz&-nz),c=32*w+bit;if(c>=cols.length)return -1;let f=0;for(let j=0;j<5;j++)f|=((r[j*nw+w]>>>bit)&1)<<j;if(f<1||f>=p)throw new Error("Noncanonical coefficient");if(!piv[c]){if(insert){piv[c]=multiples(r,c,f);rank++;}return c;}add(r,piv[c][p-1-f],w);ops++;nz=r[w]|r[nw+w]|r[2*nw+w]|r[3*nw+w]|r[4*nw+w];}}return -1;
 }
 const make=poly=>{const r=new Int32Array(5*nw);for(const[k,v]of poly){const c=index.get(k),w=c>>>5,b=1<<(c&31);for(let j=0;j<5;j++)if(v&(1<<j))r[j*nw+w]|=b;}return r;};
 for(let a=0;a<p;a++)for(let b=0;b<p;b++){const x=new Int32Array(5*nw),y=new Int32Array(5*nw);for(let j=0;j<5;j++){x[j*nw]=(a>>j)&1;y[j*nw]=(b>>j)&1;}add(x,y,0);let v=0;for(let j=0;j<5;j++)v|=(x[j*nw]&1)<<j;if(v!==(a+b)%p)throw new Error("Field addition identity failed");}
 outer:for(let deg=0;deg<=D-2;deg++)for(let j=0;j<rows.length;j++){
  for(const mult of degrees[deg]){reduce(make(rows[j].map(([k,v])=>[k+mult,v])),true);processed++;if(targetRank&&rank>=targetRank){stopped=true;break outer;}}
  if(report&&Date.now()-last>12000){await report({field:p,D,deg,generator:j,processed,rank,ops,elapsed:Date.now()-last});last=Date.now();}
 }
 return {field:p,D,rowsProcessed:processed,totalRows:rows.length*degrees.slice(0,D-1).reduce((v,x)=>v+x.length,0),columns:cols.length,rankLowerBound:rank,targetReached:stopped,ops,lowerDegreePivotCounts:degrees.slice(1).map(a=>a.filter(k=>piv[index.get(k)]).length)};
}
if(typeof module!=="undefined")module.exports={rankOneMacaulayF17F19};
