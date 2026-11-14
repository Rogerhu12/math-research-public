"use strict";
// Exact F_11 row spans using four bit planes and cached scalar multiples.
async function rankOneMacaulayF11(z,D,report){
 const p=11,vars=Array.from({length:11},(_,i)=>8**i),listDeg=d=>{const out=[];const rec=(min,left,key)=>{if(!left){out.push(key);return;}for(let i=min;i<11;i++)rec(i,left-1,key+vars[i]);};rec(0,d,0);return out;};
 const degrees=Array.from({length:D+1},(_,d)=>listDeg(d)),cols=degrees.slice(1).reverse().flat(),index=new Map(cols.map((x,i)=>[x,i])),nw=Math.ceil(cols.length/32);
 const md=x=>Number((BigInt(x)%11n+11n)%11n),rows=z.equations.map(e=>{const a=[];e.quadratic.forEach((x,j)=>{const v=md(x);if(v){const[u,w]=z.quadraticMonomials[j];a.push([vars[u]+vars[w],v]);}});e.linear.forEach((x,j)=>{const v=md(x);if(v)a.push([vars[j],v]);});return a;});
 let rank=0,processed=0,ops=0,last=Date.now();const piv=Array(cols.length),inv=[0,1,6,4,3,9,2,8,7,5,10];
 function add(r,q,w0){
  for(let w=w0;w<nw;w++){
   const a0=r[w],a1=r[nw+w],a2=r[2*nw+w],a3=r[3*nw+w],b0=q[w],b1=q[nw+w],b2=q[2*nw+w],b3=q[3*nw+w];
   const s0=a0^b0;let c=a0&b0;const x1=a1^b1,s1=x1^c;c=(a1&b1)|(x1&c);const x2=a2^b2,s2=x2^c;c=(a2&b2)|(x2&c);const x3=a3^b3,s3=x3^c,s4=(a3&b3)|(x3&c);
   const d0=~s0;let borrow=~s0;const d1=~(s1^borrow);borrow=~s1|borrow;const d2=s2^borrow;borrow=~s2&borrow;const d3=~(s3^borrow);borrow=~s3|borrow;const take=~(~s4&borrow);
   r[w]=s0^(take&(s0^d0));r[nw+w]=s1^(take&(s1^d1));r[2*nw+w]=s2^(take&(s2^d2));r[3*nw+w]=s3^(take&(s3^d3));
  }
 }
 function multiples(r,c,f){
  const all=[r];for(let k=2;k<=10;k++){const q=all[k-2].slice();add(q,r,c>>>5);all.push(q);}
  const normalized=Array.from({length:10},(_,i)=>all[((i+1)*inv[f]%11)-1]);
  for(let i=0;i<10;i++){const q=normalized[i],w=c>>>5,b=c&31,v=((q[w]>>>b)&1)+2*((q[nw+w]>>>b)&1)+4*((q[2*nw+w]>>>b)&1)+8*((q[3*nw+w]>>>b)&1);if(v!==i+1)throw new Error("Noncanonical pivot multiple");}
  return normalized;
 }
 function reduce(r,insert){
  for(let w=0;w<nw;w++){let nz=r[w]|r[nw+w]|r[2*nw+w]|r[3*nw+w];
   while(nz){const bit=31-Math.clz32(nz&-nz),c=32*w+bit;if(c>=cols.length)return -1;
    const f=((r[w]>>>bit)&1)+2*((r[nw+w]>>>bit)&1)+4*((r[2*nw+w]>>>bit)&1)+8*((r[3*nw+w]>>>bit)&1);
    if(f<1||f>10)throw new Error("Noncanonical coefficient");
    if(!piv[c]){if(insert){piv[c]=multiples(r,c,f);rank++;}return c;}
    add(r,piv[c][10-f],w);ops++;nz=r[w]|r[nw+w]|r[2*nw+w]|r[3*nw+w];
   }
  }return -1;
 }
 const make=poly=>{const r=new Int32Array(4*nw);for(const[k,v]of poly){const c=index.get(k),w=c>>>5,b=1<<(c&31);for(let j=0;j<4;j++)if(v&(1<<j))r[j*nw+w]|=b;}return r;};
 // Exhaust every field addition in disjoint bit lanes before row operations.
 for(let a=0;a<11;a++)for(let b=0;b<11;b++){const x=new Int32Array(4*nw),y=new Int32Array(4*nw);for(let j=0;j<4;j++){x[j*nw]=(a>>j)&1;y[j*nw]=(b>>j)&1;}add(x,y,0);let v=0;for(let j=0;j<4;j++)v|=(x[j*nw]&1)<<j;if(v!==(a+b)%11)throw new Error("Field addition identity failed");}
 for(let deg=0;deg<=D-2;deg++)for(let j=0;j<rows.length;j++){
  for(const mult of degrees[deg]){reduce(make(rows[j].map(([k,v])=>[k+mult,v])),true);processed++;}
  if(report&&Date.now()-last>12000){await report({field:11,D,deg,generator:j,processed,rank,ops,elapsed:Date.now()-last});last=Date.now();}
 }
 const member=poly=>reduce(make(poly),false)===-1;
 const squares=Array.from({length:11},(_,i)=>member([[2*vars[i],1]])),linear=vars.map(k=>member([[k,1]]));
 return {field:11,D,rows:processed,columns:cols.length,rank,ops,lowerDegreePivotCounts:degrees.slice(1).map(a=>a.filter(k=>piv[index.get(k)]).length),coordinateLinearMembership:linear,coordinateSquareMembership:squares};
}
if(typeof module!=="undefined")module.exports={rankOneMacaulayF11};
