// Exact BigInt certificate for R271, three exceptional weights, full birth-one and birth-two Gram bounds.
// Variables: z1,z2,z3,k,l. No sampled parameters and no floating eigenvalues.
// Run: node this-file.mjs. It prints one PASS report or throws.
// All products check each base-64 exponent before encoding can carry.
"use strict";

const PB=64, PP=[1,64,4096,262144,16777216];
const BOUNDS=new WeakMap();
function pbound(p){let b=BOUNDS.get(p);if(b)return b;b=[0,0,0,0,0];for(const[k,v]of p){if(!Number.isSafeInteger(k)||k<0||k>=PB**5)throw Error("unsafe exponent code");for(let i=0;i<5;i++)b[i]=Math.max(b[i],Math.floor(k/PP[i])%PB)}BOUNDS.set(p,b);return b}
function pc(c){return new Map(c?[[0,BigInt(c)]]:[])}
function pv(i){return new Map([[PP[i],1n]])}
function padd(...ps){const o=new Map;for(const p of ps)for(const [k,v]of p){const w=(o.get(k)||0n)+v;if(w)o.set(k,w);else o.delete(k)}return o}
function pneg(p){return new Map([...p].map(([k,v])=>[k,-v]))}
function psub(a,b){return padd(a,pneg(b))}
function pmul(a,b){const ba=pbound(a),bb=pbound(b);for(let i=0;i<5;i++)if(ba[i]+bb[i]>=PB)throw Error("exponent overflow");const o=new Map;for(const[k,v]of a)for(const[l,w]of b){const t=k+l,z=(o.get(t)||0n)+v*w;if(z)o.set(t,z);else o.delete(t)}return o}
function pscale(p,c){return new Map([...p].map(([k,v])=>[k,v*BigInt(c)]).filter(([k,v])=>v))}
function ppow(p,n){let r=pc(1);for(let i=0;i<n;i++)r=pmul(r,p);return r}
function pdivmon(p,es){let shift=es.reduce((s,e,i)=>s+e*PP[i],0),o=new Map;for(const[k,v]of p){for(let i=0;i<es.length;i++)if(Math.floor(k/PP[i])%PB<es[i])throw Error("not monomial divisible "+es+" "+k);o.set(k-shift,v)}return o}
function psubstshift(p,dk,dl){const k=padd(pv(3),pc(dk)),l=padd(pv(4),pc(dl)),cache=[[],[]];cache[0][0]=cache[1][0]=pc(1);function power(j,n){const v=j?l:k;for(let t=cache[j].length;t<=n;t++)cache[j][t]=pmul(cache[j][t-1],v);return cache[j][n]}let r=pc(0);for(const[mon,c]of p){const ek=Math.floor(mon/PP[3])%PB,el=Math.floor(mon/PP[4])%PB,base=mon-ek*PP[3]-el*PP[4];const term=pmul(power(0,ek),power(1,el));for(const[q,b]of term){const key=q+base,z=(r.get(key)||0n)+b*c;if(z)r.set(key,z);else r.delete(key)}}return r}
function pminors(A,i,j){return A.filter((_,r)=>r!==i).map(row=>row.filter((_,c)=>c!==j))}
function pdet(A){if(A.length===0)return pc(1);if(A.length===1)return A[0][0];let r=pc(0);for(let j=0;j<A.length;j++)r=padd(r,pscale(pmul(A[0][j],pdet(pminors(A,0,j))),j%2?-1:1));return r}
function padj(A){return A.map((_,i)=>A.map((_,j)=>pscale(pdet(pminors(A,j,i)),(i+j)%2?-1:1)))}
function pmm(A,B){return A.map(row=>B[0].map((_,j)=>row.reduce((s,a,k)=>padd(s,pmul(a,B[k][j])),pc(0))))}
function pmat_scale(A,p){return A.map(row=>row.map(a=>pmul(a,p)))}
function pmat_sub(A,B){return A.map((row,i)=>row.map((a,j)=>psub(a,B[i][j])))}
function pserial(p){return [...p].map(([k,v])=>[k,v.toString()])}
function punserial(p){return new Map(p.map(([k,v])=>[k,BigInt(v)]))}
function pstats(p){const deg=[0,0,0,0,0];let neg=0;for(const[k,v]of p){if(v<0n)neg++;for(let i=0;i<5;i++)deg[i]=Math.max(deg[i],Math.floor(k/PP[i])%PB)}return {terms:p.size,negative:neg,degrees:deg}}
function model3(){
 const a=[pv(0),pv(1),pv(2)],k=pv(3),l=pv(4);
 const w=[pmul(l,pmul(psub(l,pc(1)),psub(l,pc(2)))),pmul(k,pmul(l,psub(l,pc(1)))),pmul(pmul(k,psub(k,pc(1))),l),pmul(k,pmul(psub(k,pc(1)),psub(k,pc(2))))];
 const E=Array.from({length:4},()=>Array.from({length:4},()=>pc(0)));
 for(let mask=0;mask<8;mask++){const u=[1,...a.map((_,i)=>(mask>>i)&1)],r=u.slice(1).reduce((x,y)=>x+y,0);let ww=w[r];for(let i=0;i<3;i++)if(u[i+1])ww=pmul(ww,a[i]);for(let i=0;i<4;i++)for(let j=0;j<4;j++)if(u[i]*u[j])E[i][j]=padd(E[i][j],ww);}
 const Z=E[0][0],T=pdivmon(pdet(E),[0,0,0,3,3]),N=Array.from({length:3},(_,i)=>Array.from({length:3},(_,j)=>pdivmon(pscale(pdet(pminors(E,j+1,i+1)),(i+j)%2?-1:1),[0,0,0,2,2]))),M=Array.from({length:3},(_,i)=>Array.from({length:3},(_,j)=>pdivmon(psub(pmul(Z,E[i+1][j+1]),pmul(E[i+1][0],E[0][j+1])),[0,0,0,1,1])));
 return {Z,T,N,M,E};
}

function pevalvar(p,index,val){const o=new Map;for(const[k,v]of p){const e=Math.floor(k/PP[index])%64,key=k-e*PP[index],vv=v*BigInt(val)**BigInt(e),z=(o.get(key)||0n)+vv;if(z)o.set(key,z);else o.delete(key)}return o}

function pshiftvar(p,index,val){const o=new Map,cache=[pc(1)],v=padd(pv(index),pc(val));for(const[k,c]of p){const e=Math.floor(k/PP[index])%64,base=k-e*PP[index];for(let j=cache.length;j<=e;j++)cache[j]=pmul(cache[j-1],v);for(const[q,b]of cache[e]){const key=q+base,z=(o.get(key)||0n)+b*c;if(z)o.set(key,z);else o.delete(key)}}return o}

function must(b,msg){if(!b)throw Error(msg)}
function zero(p,msg){must(p.size===0,msg)}
function coefficient(p,es){return p.get(es.reduce((s,e,i)=>s+e*PP[i],0))||0n}
function positiveCheck(p,terms,es,value,name){
 must(p.size===terms,name+": term count");
 for(const v of p.values())must(v>0n,name+": nonpositive coefficient");
 must(coefficient(p,es)===BigInt(value),name+": explicit coefficient");
 return {name,terms,explicitCoefficient:String(value)};
}
function traceprod(A,B){let r=pc(0);for(let i=0;i<3;i++)for(let j=0;j<3;j++)r=padd(r,pmul(A[i][j],B[j][i]));return r}
function runCertificate(){
 const {Z,T,N,M}=model3();
 const NM=pmm(N,M),ZT=pmul(Z,T);
 for(let i=0;i<3;i++)for(let j=0;j<3;j++){zero(psub(NM[i][j],i===j?ZT:pc(0)),"NM=ZT I");zero(psub(N[i][j],N[j][i]),"N symmetric");zero(psub(M[i][j],M[j][i]),"M symmetric")}
 zero(psub(pdet(N),pmul(Z,ppow(T,2))),"det N");
 zero(psub(pdet(M),pmul(ppow(Z,2),T)),"det M");
 const Tp=psubstshift(T,-1,1),Tn=psubstshift(T,1,-1),Zp=psubstshift(Z,-1,1),Zn=psubstshift(Z,1,-1);
 const Np=N.map(row=>row.map(p=>psubstshift(p,-1,1))),Nn=N.map(row=>row.map(p=>psubstshift(p,1,-1)));
 const Mp=M.map(row=>row.map(p=>psubstshift(p,-1,1))),Mn=M.map(row=>row.map(p=>psubstshift(p,1,-1)));
 const alpha=pmul(pv(3),pv(4)),beta=pmul(psub(pv(3),pc(1)),psub(pv(4),pc(1)));
 const A=pmm(pmm(M,Np),M),C=pmm(pmm(N,Mp),N);
 const Delta11=psub(pmul(pmul(alpha,Zn),A[0][0]),pmul(pmul(beta,pmul(ppow(Z,2),Tp)),Mn[0][0]));
 const P1=pdivmon(Delta11,[1,1,1,0,0]);
 const mix=padd(pmul(A[1][1],Mn[2][2]),pmul(A[2][2],Mn[1][1]),pscale(pmul(A[1][2],Mn[1][2]),-2));
 const R=padd(pmul(pmul(ppow(alpha,2),Zn),C[0][0]),pneg(pmul(pmul(alpha,beta),mix)),pmul(pmul(ppow(beta,2),pmul(ppow(Z,2),Tp)),Nn[0][0]));
 const P2=pdivmon(R,[1,2,2,0,0]);
 const tr1=traceprod(pmm(N,Mp),pmm(N,Mn)),tr2=traceprod(pmm(Nn,M),pmm(Np,M));
 const F=padd(
  pmul(ppow(alpha,3),pmul(Zn,pmul(ppow(T,2),Zp))),
  pneg(pmul(pmul(ppow(alpha,2),beta),tr1)),
  pmul(pmul(alpha,ppow(beta,2)),tr2),
  pneg(pmul(ppow(beta,3),pmul(ppow(Z,2),pmul(Tp,Tn))))
 );
 const P3=pdivmon(F,[2,2,2,0,0]),polys=[P1,P2,P3],report=[];
 const interior=polys.map(p=>psubstshift(p,3,3));
 const ic=[21735,33977,51785],ie=[[2,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]],iv=["2239488","11943936","143327232"];
 for(let i=0;i<3;i++)report.push(positiveCheck(interior[i],ic[i],ie[i],iv[i],"interior P"+(i+1)));
 const edge=polys.map(p=>psubstshift(pevalvar(p,3,2),0,3));
 const ec=[1184,2163,3571],ev=["1119744","5038848","40310784"];
 for(let i=0;i<3;i++)report.push(positiveCheck(edge[i],ec[i],ie[i],ev[i],"edge P"+(i+1)));
 const corner=polys.map(p=>{let r=pevalvar(pevalvar(p,3,2),4,2);for(let j=0;j<3;j++)r=pshiftvar(r,j,1);return r});
 const cc=[127,160,245],cv=["2985984","11943936","35831808"];
 for(let i=0;i<3;i++)report.push(positiveCheck(corner[i],cc[i],[0,0,0,0,0],cv[i],"four-site corner P"+(i+1)));
 // Birth two: these are minus P_i(-1-x,-1-y), an exact finite polynomial substitution.
 const reflected=polys.map(p=>{
  const flipped=new Map([...p].map(([key,value])=>{
   const parity=(Math.floor(key/PP[3])%PB+Math.floor(key/PP[4])%PB)%2;
   return [key,parity?value:-value];
  }));
  return psubstshift(flipped,1,1);
 });
 const rc=[21251,33584,51515],re=[[1,1,1,0,0],[0,1,1,0,0],[0,1,1,0,0]],rv=["248832","1327104","15925248"];
 for(let i=0;i<3;i++)report.push(positiveCheck(reflected[i],rc[i],re[i],rv[i],"birth-two reflected P"+(i+1)));
 return {status:"PASS",identities:["NM=ZT I","det N=ZT^2","det M=Z^2T","all exact monomial divisions"],certificate:report};
}
const report=runCertificate();
if(typeof console!=="undefined")console.log(JSON.stringify(report));
