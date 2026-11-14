"use strict";
function verifyRankOneOutsideLowVBlocks(){
 let names=[],indices=new Map();
 const Z=()=>new Map(),C=a=>a?new Map([[0n,BigInt(a)]]):Z();
 const X=name=>{if(!indices.has(name)){indices.set(name,names.length);names.push(name);}
  return new Map([[1n<<(6n*BigInt(indices.get(name))),1n]]);};
 const add=(...ps)=>{const r=Z();for(const p of ps)for(const[k,v]of p){const w=(r.get(k)||0n)+v;if(w)r.set(k,w);else r.delete(k);}return r;};
 const sc=(a,c)=>{const r=Z();c=BigInt(c);if(c)for(const[k,v]of a)r.set(k,v*c);return r;};
 const mul=(a,b)=>{const r=Z();for(const[k,v]of a)for(const[l,w]of b){const j=k+l,t=(r.get(j)||0n)+v*w;if(t)r.set(j,t);else r.delete(j);}return r;};
 const sq=a=>mul(a,a),zeroAt=(a,list)=>{const masks=list.map(n=>63n << (6n*BigInt(indices.get(n))));return new Map([...a].filter(([k])=>masks.every(m=>(k&m)===0n)));};
 let checks=0;const eq=(a,b,label)=>{checks++;if(add(a,sc(b,-1)).size)throw Error(label);};
 const mat=f=>Array.from({length:5},(_,i)=>Array.from({length:5},(_,j)=>f(i,j)));
 const mm=(a,b)=>mat((i,j)=>add(...Array.from({length:5},(_,k)=>mul(a[i][k],b[k][j]))));
 const mv=(a,b)=>a.map(row=>add(...row.map((v,j)=>mul(v,b[j]))));
 const tr=a=>add(...a.map((row,i)=>row[i])),dot=(a,b)=>add(...a.map((v,i)=>mul(v,b[i])));
 function build(partition,kind){
  const blocks=[];let next=1;for(const n of partition){blocks.push({start:next,n});next+=n;}
  const K=mat((i,j)=>i===0&&j===0?Z():X("k"+Math.min(i,j)+Math.max(i,j)));
  for(const b of blocks){
   K[b.start][b.start]=Z();
   if(b.n>=2)K[b.start][b.start+1]=K[b.start+1][b.start]=Z();
   if(b.n>=3){const g=X("g"+b.start);K[b.start+1][b.start+1]=sc(g,2);K[b.start][b.start+2]=K[b.start+2][b.start]=sc(g,-1);}
   if(b.n>=4){const a=X("j"+b.start);K[b.start+1][b.start+2]=K[b.start+2][b.start+1]=a;K[b.start][b.start+3]=K[b.start+3][b.start]=sc(a,-1);}
  }
  const H6=mat(()=>Z());H6[0][0]=C(1);
  if(kind==="two_values"){H6[1][1]=sc(X("h"),6);H6[3][3]=sc(X("k"),6);}
  else if(kind==="tangent"){H6[1][1]=sc(X("h0"),6);H6[1][2]=H6[2][1]=sc(X("h1"),6);}
  else H6[1][1]=sc(X("h"),6);
  const V=(i,j,k)=>{if(!i||!j||!k)return Z();for(let b=0;b<blocks.length;b++){
   const q=blocks[b];if([i,j,k].every(i=>i>=q.start&&i<q.start+q.n)){
    const t=i+j+k-3*q.start;return t<q.n?X("v"+b+"_"+t):Z();}}return Z();};
  const p=K.map(row=>row[0]),KH=mm(K,H6),HKH=mm(mm(H6,K),H6),
   KHK=mm(KH,K),b=dot(p,mv(H6,p)),tau=tr(mm(KH,KH)),hp=mv(HKH,p);
  const gamma=Array.from({length:5},(_,i)=>{
   let vp=Z(),vh=Z();for(let j=0;j<5;j++)for(let k=0;k<5;k++){
    vp=add(vp,mul(V(i,j,k),mul(p[j],p[k])));vh=add(vh,mul(V(i,j,k),KHK[j][k]));}
   return add(i===0?add(sc(b,-12),sc(tau,2)):Z(),sc(hp[i],8),sc(vp,144),sc(vh,-48));
  });return {K,gamma};
 }
 const a=build([2,1,1],"one_value");
 eq(a.gamma[2],sc(mul(X("v0_1"),sq(X("k01"))),96),"2+1+1 highest jet");
 const b=build([3,1],"one_value");
 eq(b.gamma[3],sc(mul(X("v0_2"),sq(X("k01"))),96),"3+1 highest jet");
 const c=build([2,2],"two_values"),g=sq(X("k13"));
 eq(c.gamma[0],sc(mul(mul(X("h"),X("k")),g),144),"2+2 mean");
 eq(c.gamma[2],add(sc(mul(X("v0_1"),sq(X("k01"))),96),sc(mul(mul(X("v0_1"),X("k")),g),-288)),"2+2 first highest jet");
 eq(c.gamma[4],add(sc(mul(X("v1_1"),sq(X("k03"))),96),sc(mul(mul(X("v1_1"),X("h")),g),-288)),"2+2 second highest jet");
 const d=build([4],"tangent");
 eq(d.gamma[4],sc(mul(X("v0_3"),sq(X("k01"))),96),"4 highest jet");
 eq(zeroAt(d.gamma[2],["k01"]),sc(mul(X("v0_3"),sq(X("k02"))),96),"4 first jet after value pairing");
 eq(zeroAt(d.gamma[1],["k01","k02"]),sc(mul(mul(X("h1"),X("v0_3")),sq(X("g1"))),1152),"4 remaining value coefficient");
 for(const i of [0,2,3,4])eq(zeroAt(d.gamma[i],["k01","k02"]),Z(),"4 other component "+i);
 return {status:"PASS",arithmetic:"exact sparse multivariate BigInt polynomials",checks,
  scaling:"The verifier computes 36 times the complete original normalized Gamma.",
  coverage:["2+1+1","3+1","2+2","4"],execution:"Executed in code mode; no terminal or Python run is claimed."};
}
if(typeof module!=="undefined")module.exports={verifyRankOneOutsideLowVBlocks};
if(typeof require!=="undefined"&&require.main===module)
 console.log(JSON.stringify(verifyRankOneOutsideLowVBlocks(),null,2));
