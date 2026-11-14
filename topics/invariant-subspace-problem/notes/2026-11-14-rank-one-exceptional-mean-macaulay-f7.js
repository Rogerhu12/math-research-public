"use strict";
// Exact row spans over F_7. A search aid, not a characteristic-zero certificate.
async function rankOneMacaulayF7(z,D,report){
 const vars=Array.from({length:11},(_,i)=>8**i), listDeg=d=>{const out=[];const rec=(min,left,key)=>{if(!left){out.push(key);return;}for(let i=min;i<11;i++)rec(i,left-1,key+vars[i]);};rec(0,d,0);return out;};
 const degrees=Array.from({length:D+1},(_,d)=>listDeg(d)),cols=degrees.slice(1).reverse().flat(),index=new Map(cols.map((x,i)=>[x,i])),nw=Math.ceil(cols.length/32);
 const md=x=>Number((BigInt(x)%7n+7n)%7n);
 const rows=z.equations.map(e=>{const a=[];e.quadratic.forEach((x,j)=>{const v=md(x);if(v){const[u,w]=z.quadraticMonomials[j];a.push([vars[u]+vars[w],v]);}});e.linear.forEach((x,j)=>{const v=md(x);if(v)a.push([vars[j],v]);});return a;});
 const piv=Array(cols.length);let rank=0,processed=0,ops=0,lastTime=Date.now();
 function norm(r,c,f){
  if(f===1)return;
  const iv=[0,1,4,5,2,3,6][f],cycle=iv===1||iv===6?0:iv===2||iv===5?1:2,neg=iv>=3&&iv!==4;
  for(let w=c>>>5;w<nw;w++){
   const a=r[w],b=r[nw+w],d=r[2*nw+w];let x=cycle===0?a:cycle===1?d:b,y=cycle===0?b:cycle===1?a:d,t=cycle===0?d:cycle===1?b:a;
   if(neg){const u=x|y|t;x=u^x;y=u^y;t=u^t;}
   r[w]=x;r[nw+w]=y;r[2*nw+w]=t;
  }
 }
 function sub(r,q,c,f){
  const factor=7-f,cycle=factor===1||factor===6?0:factor===2||factor===5?1:2,neg=factor>=3&&factor!==4;
  const j0=cycle===0?0:cycle===1?2*nw:nw,j1=cycle===0?nw:cycle===1?0:2*nw,j2=cycle===0?2*nw:cycle===1?nw:0,mask=neg?-1:0;
  for(let w=c>>>5;w<nw;w++){
   const a0=r[w],a1=r[nw+w],a2=r[2*nw+w],b0=q[j0+w]^mask,b1=q[j1+w]^mask,b2=q[j2+w]^mask;
   let s0=a0^b0,carry=a0&b0;const x1=a1^b1;let s1=x1^carry;carry=(a1&b1)|(x1&carry);const x2=a2^b2;let s2=x2^carry;carry=(a2&b2)|(x2&carry);
   const t0=s0^carry;carry&=s0;s0=t0;const t1=s1^carry;carry&=s1;s1=t1;s2^=carry;const keep=~(s0&s1&s2);
   r[w]=s0&keep;r[nw+w]=s1&keep;r[2*nw+w]=s2&keep;
  }
  ops++;
 }
 function reduce(r,insert){
  for(let w=0;w<nw;w++){
   let nz=r[w]|r[nw+w]|r[2*nw+w];
   while(nz){
    const bit=31-Math.clz32(nz&-nz),c=32*w+bit;if(c>=cols.length)return -1;
    const f=((r[w]>>>bit)&1)+2*((r[nw+w]>>>bit)&1)+4*((r[2*nw+w]>>>bit)&1);
    if(!piv[c]){if(insert){norm(r,c,f);piv[c]=r;rank++;}return c;}
    sub(r,piv[c],c,f);nz=r[w]|r[nw+w]|r[2*nw+w];
   }
  }
  return -1;
 }
 const make=poly=>{const r=new Int32Array(3*nw);for(const[k,v]of poly){const c=index.get(k),w=c>>>5,b=1<<(c&31);if(v&1)r[w]|=b;if(v&2)r[nw+w]|=b;if(v&4)r[2*nw+w]|=b;}return r;};
 for(let deg=0;deg<=D-2;deg++)for(let j=0;j<rows.length;j++){
  for(const mult of degrees[deg]){reduce(make(rows[j].map(([k,v])=>[k+mult,v])),true);processed++;}
  if(report&&Date.now()-lastTime>12000){await report({D,deg,generator:j,processed,rank,ops,elapsed:Date.now()-lastTime});lastTime=Date.now();}
 }
 const member=poly=>reduce(make(poly),false)===-1;
 const squares=Array.from({length:11},(_,i)=>member([[2*vars[i],1]])),linear=vars.map(k=>member([[k,1]]));
 const counts=degrees.slice(1).map(a=>a.filter(k=>piv[index.get(k)]).length);
 return {field:7,D,rows:processed,columns:cols.length,rank,ops,lowerDegreePivotCounts:counts,coordinateLinearMembership:linear,coordinateSquareMembership:squares};
}
if(typeof module!=="undefined")module.exports={rankOneMacaulayF7};
