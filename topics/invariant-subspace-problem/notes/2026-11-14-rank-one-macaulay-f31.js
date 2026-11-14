"use strict";
// Deterministic exact row spans over F_31, using five bitplanes.
// No characteristic-zero conclusion is made by this helper alone.
async function rankOneMacaulayF31(z,D,report){
 const prime=31,vars=Array.from({length:11},(_,i)=>8**i),listDeg=d=>{const out=[];const rec=(min,left,key)=>{if(!left){out.push(key);return;}for(let i=min;i<11;i++)rec(i,left-1,key+vars[i]);};rec(0,d,0);return out;};
 const degrees=Array.from({length:D+1},(_,d)=>listDeg(d)),cols=degrees.slice(1).reverse().flat(),index=new Map(cols.map((x,i)=>[x,i])),nw=Math.ceil(cols.length/32);
 const md=x=>Number((BigInt(x)%31n+31n)%31n);
 const rows=z.equations.map(e=>{const a=[];e.quadratic.forEach((x,j)=>{const v=md(x);if(v){const[u,w]=z.quadraticMonomials[j];a.push([vars[u]+vars[w],v]);}});e.linear.forEach((x,j)=>{const v=md(x);if(v)a.push([vars[j],v]);});return a;});
 const rep=Array(31),iv=Array(31);
 for(let c=0;c<3;c++)for(let rot=0;rot<5;rot++)for(let neg=0;neg<2;neg++){const v=([1,3,5][c]*2**rot*(neg?-1:1)%31+31)%31;rep[v]={c,rot,neg};}
 for(let a=1;a<31;a++){let x=1;while(a*x%31!==1)x++;iv[a]=x;}
 const piv=Array(cols.length);let rank=0,processed=0,ops=0,lastTime=Date.now();
 function addRot(r,q,start,rot,neg){
  const j0=((5-rot)%5)*nw,j1=((6-rot)%5)*nw,j2=((7-rot)%5)*nw,j3=((8-rot)%5)*nw,j4=((9-rot)%5)*nw,mask=neg?-1:0;
  for(let w=start;w<nw;w++){
   const a0=r[w],a1=r[nw+w],a2=r[2*nw+w],a3=r[3*nw+w],a4=r[4*nw+w],b0=q[j0+w]^mask,b1=q[j1+w]^mask,b2=q[j2+w]^mask,b3=q[j3+w]^mask,b4=q[j4+w]^mask;
   let s0=a0^b0,carry=a0&b0;
   const x1=a1^b1;let s1=x1^carry;carry=(a1&b1)|(x1&carry);
   const x2=a2^b2;let s2=x2^carry;carry=(a2&b2)|(x2&carry);
   const x3=a3^b3;let s3=x3^carry;carry=(a3&b3)|(x3&carry);
   const x4=a4^b4;let s4=x4^carry;carry=(a4&b4)|(x4&carry);
   const t0=s0^carry;carry&=s0;s0=t0;const t1=s1^carry;carry&=s1;s1=t1;const t2=s2^carry;carry&=s2;s2=t2;const t3=s3^carry;carry&=s3;s3=t3;s4^=carry;
   const keep=~(s0&s1&s2&s3&s4);
   r[w]=s0&keep;r[nw+w]=s1&keep;r[2*nw+w]=s2&keep;r[3*nw+w]=s3&keep;r[4*nw+w]=s4&keep;
  }
 }
 function norm(r,c,f){
  if(f===1)return;const R=rep[iv[f]],start=c>>>5;
  if(R.c)addRot(r,r.slice(),start,R.c===1?1:2,0);
  const j0=((5-R.rot)%5)*nw,j1=((6-R.rot)%5)*nw,j2=((7-R.rot)%5)*nw,j3=((8-R.rot)%5)*nw,j4=((9-R.rot)%5)*nw;
  for(let w=start;w<nw;w++){let a=r[j0+w],b=r[j1+w],d=r[j2+w],e=r[j3+w],f=r[j4+w];if(R.neg){const u=a|b|d|e|f;a^=u;b^=u;d^=u;e^=u;f^=u;}r[w]=a;r[nw+w]=b;r[2*nw+w]=d;r[3*nw+w]=e;r[4*nw+w]=f;}
 }
 function insert(r,c,f){
  norm(r,c,f);const a=r.slice(),b=r.slice();addRot(a,r,c>>>5,1,0);addRot(b,r,c>>>5,2,0);piv[c]=[r,a,b];rank++;
 }
 function reduce(r,doInsert){
  for(let w=0;w<nw;w++){
   let nz=r[w]|r[nw+w]|r[2*nw+w]|r[3*nw+w]|r[4*nw+w];
   while(nz){
    const bit=31-Math.clz32(nz&-nz),c=32*w+bit;if(c>=cols.length)return -1;
    const f=((r[w]>>>bit)&1)+2*((r[nw+w]>>>bit)&1)+4*((r[2*nw+w]>>>bit)&1)+8*((r[3*nw+w]>>>bit)&1)+16*((r[4*nw+w]>>>bit)&1);
    if(!piv[c]){if(doInsert)insert(r,c,f);return c;}
    const R=rep[31-f];addRot(r,piv[c][R.c],w,R.rot,R.neg);ops++;
    nz=r[w]|r[nw+w]|r[2*nw+w]|r[3*nw+w]|r[4*nw+w];
   }
  }
  return -1;
 }
 const make=poly=>{const r=new Int32Array(5*nw);for(const[k,v]of poly){const c=index.get(k),w=c>>>5,b=1<<(c&31);if(v&1)r[w]|=b;if(v&2)r[nw+w]|=b;if(v&4)r[2*nw+w]|=b;if(v&8)r[3*nw+w]|=b;if(v&16)r[4*nw+w]|=b;}return r;};
 for(let deg=0;deg<=D-2;deg++)for(let j=0;j<rows.length;j++){
  for(const mult of degrees[deg]){reduce(make(rows[j].map(([k,v])=>[k+mult,v])),true);processed++;}
  if(report&&Date.now()-lastTime>10000){await report({D,deg,generator:j,processed,rank,ops,elapsed:Date.now()-lastTime});lastTime=Date.now();}
 }
 const member=poly=>reduce(make(poly),false)===-1;
 const squares=Array.from({length:11},(_,i)=>member([[2*vars[i],1]])),linear=vars.map(k=>member([[k,1]]));
 const counts=degrees.slice(1).map(a=>a.filter(k=>piv[index.get(k)]).length);
 return {field:31,D,rows:processed,columns:cols.length,rank,ops,lowerDegreePivotCounts:counts,coordinateLinearMembership:linear,coordinateSquareMembership:squares};
}
if(typeof module!=="undefined")module.exports={rankOneMacaulayF31};
