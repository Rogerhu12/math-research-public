#!/usr/bin/env node
"use strict";
/*
R693: actual neutral G6-power extension of the R679 test.
Run publicly: node check-r693-neutral-g12-four-source-adaptation.js --max-block=4 --taus=2,3 --with-b --free-normalizations
No data files are read or written. The original R594 algorithm is executed
in a child process and its output stays in memory. All requested degree blocks,
all original 31 constraints, the full C_(6*(max_block+1)) term and every actual W coordinate
are computed. Rank and consistency are outputs, not dimension assumptions.
Auxiliary exact arithmetic F1009, omega=374 certifies fixed rational-function
minors only. The actual p-adic test is defined by the full parameter inverse.
*/
const fs=require("fs"),path=require("path"),cp=require("child_process"),crypto=require("crypto");
const assert=(ok,msg)=>{if(!ok)throw Error(msg);};
const start=Date.now();
const inputPath=path.join(__dirname,"check-r594-two-source-six-carry-compensation.js");
const inputCode=fs.readFileSync(inputPath,"utf8");
console.error("R693: recomputing original R594 rows");
const all=JSON.parse(cp.execFileSync(process.execPath,[inputPath],{encoding:"utf8",maxBuffer:16*1024*1024}));
const arg=process.argv.slice(2).find(x=>x.startsWith("--max-block="));
const MAXBLOCK=arg?Number(arg.split("=")[1]):2;
const WITHB=process.argv.includes("--with-b");
const FREE_NORMALIZATIONS=process.argv.includes("--free-normalizations");
const REPORT_FULL=process.argv.includes("--full-matrix");
let DEBOUND=6;
assert(Number.isInteger(MAXBLOCK)&&MAXBLOCK>=2&&MAXBLOCK<=8,"max block must be between 2 and 8");
const argTaus=process.argv.slice(2).find(x=>x.startsWith("--taus="));
const TAUS=(argTaus?argTaus.split("=")[1]:"2").split(",").map(Number);
assert(TAUS.length>=1&&TAUS.length<=3&&TAUS.every(t=>Number.isInteger(t)&&t>1&&t<1009),
 "taus must be one to three integers from 2 to 1008");
const pp=1009,om=374,MAXZ=72,CAP=6*(MAXBLOCK+1),SERIES=Math.ceil((MAXZ+CAP)/6);
const md=x=>((x%pp)+pp)%pp;
const pow=(a,n)=>{let x=1;for(;n;n=Math.floor(n/2),a=md(a*a))if(n%2)x=md(x*a);return x;};
const iv=a=>{a=md(a);assert(a!==0,"zero denominator in exact auxiliary field");return pow(a,pp-2);};
const rf=s=>{let a=String(s).split("/");return md(Number(BigInt(a[0])%BigInt(pp))*iv(Number(BigInt(a[1]||1)%BigInt(pp))));};
const ef=v=>md(rf(v[0])+om*rf(v[1]));
const ne=(a,b=0,d=1)=>md((a+om*b)*iv(d));
const fact=[1];for(let i=1;i<=MAXZ+CAP;i++)fact[i]=md(fact[i-1]*i);
const cb=(n,k)=>md(fact[n]*iv(md(fact[k]*fact[n-k])));
const conv=(a,b,N=SERIES)=>Array.from({length:N+1},(_,n)=>md(a.reduce((s,v,k)=>k<=n?s+v*(b[n-k]||0):s,0)));
const pw=(a,k,N=SERIES)=>{let v=[1];for(let i=0;i<k;i++)v=conv(v,a,N);return v;};
const xx=[1,ne(-1,0,7)];
for(let n=2;n<=SERIES;n++){let sum=0;for(let j=1;j<n;j++)sum=md(sum+xx[j]*xx[n-j]);xx[n]=md(sum*iv((6*n+1)*(n-1)));}
const log=[0,...xx.slice(1).map((a,i)=>md(-a*iv(6*(i+1)*(6*(i+1)-1))))],sig=[1];
for(let n=1;n<=SERIES;n++){let sum=0;for(let j=1;j<=n;j++)sum=md(sum+j*log[j]*sig[n-j]);sig[n]=md(sum*iv(n));}
const my=xx.map((a,i)=>i?md(-(3*i-1)*a):1);
const ss2=pw(sig,2),ss3=pw(sig,3),ss6=pw(sig,6);
const f3=conv(my,ss6),f1=conv(xx,f3),theta=conv(xx,ss2);
const bc=conv(my,ss3).slice(0,MAXBLOCK+2).map((a,i)=>md(a*pow(iv(ne(1,2)),6*i)));
assert(md(om*om+om+1)===0,"omega relation");
assert(bc[1]===rf("-1/90")&&bc[2]===rf("-19/3742200"),"entire C6/C12 retained");

const enc=(d,e,g,z)=>d+64*e+4096*g+262144*z;
const dec=k=>[k%64,Math.floor(k/64)%64,Math.floor(k/4096)%64,Math.floor(k/262144)];
const clean=P=>Array.from(P,([k,c])=>[...dec(k),c]).filter(x=>x[4]);
function mul(P,R,cap=CAP,zcap=30){
 const Z=new Map();
 for(const[a,b,c,z,v]of P)for(const[d,e,f,t,w]of R){
  if(a+b+d+e>DEBOUND||a+b+c+d+e+f>cap||z+t>zcap)continue;
  const k=enc(a+d,b+e,c+f,z+t);
  Z.set(k,md((Z.get(k)||0)+v*w));
 }
 return clean(Z);
}
const scale=(P,a)=>P.map(([d,e,g,z,c])=>[d,e,g,z,md(c*a)]).filter(v=>v[4]);
function add(P,R){
 const Q=new Map(P.map(([d,e,g,z,c])=>[enc(d,e,g,z),c]));
 for(const[d,e,g,z,c]of R){const k=enc(d,e,g,z);Q.set(k,md((Q.get(k)||0)+c));}
 return clean(Q);
}
const linearCache=new Map();
function linpow(v,n){
 const key=DEBOUND+":"+v.join(",")+":"+n;if(linearCache.has(key))return linearCache.get(key);
 const out=[];
 for(let d=0;d<=n;d++)for(let e=0;e<=n-d;e++){
  const g=n-d-e;if(d+e>DEBOUND)continue;
  const c=md(fact[n]*iv(md(fact[d]*fact[e]*fact[g]))*pow(v[0],d)*pow(v[1],e)*pow(v[2],g));
  if(c)out.push([d,e,g,0,c]);
 }
 linearCache.set(key,out);return out;
}
function factor(base,coeff,row,obs,cap=CAP,zcap=30){
 let out=[];
 for(let h=0;h<coeff.length;h++){
  const n=base+6*h;if(n>cap+zcap)break;
  for(let r=0;r<=Math.min(cap,n);r++){
   const z=n-r;if(z>zcap)continue;
   const scale=md(coeff[h]*cb(n,r)*pow(obs,z));
   for(const[d,e,g,,v]of linpow(row,r)){const c=md(v*scale);if(c)out.push([d,e,g,z,c]);}
  }
 }
 return out;
}
const A=[ne(-2,1,2),ne(4,3,2),ne(2,4)];
const D=[ne(-19,19,174),ne(31,-37,58),ne(-43,-21,29)];
const E=[ne(-133,133,429),ne(217,-259,143),ne(-602,-294,143)];
const G=[ne(-5843,-3715,858),md(ne(-1593,0,286)+ne(0,-123,22)),ne(1324,-266,143)];
const lc=[ne(-1),ne(1596,0,143),ne(-789,526,143)];
const rat=ne(-789,526,1596);
function makeSource(i,endpoint=0,observation="S",zcap=30,cap=CAP,zero=false){
 const ei=i?ne(-170,-291,9135):ne(-170,-117,9135),hh=i?ne(-5,-3):ne(-5,-9);
 const obs=observation==="W"?[...A,ne(3,6),4]:[...A,i?2:1,i?-1:2].map(md);
 let wr=[...D.map((x,j)=>md(x+5*ei*A[j])),md(-87*ei),md(-29*ei)];
 if(endpoint){const v=[...A.map(x=>5*x),i?-24:39,i?97:-92];wr=wr.map((x,j)=>md(x+hh*endpoint*v[j]*iv(315)));}
 const ER=[...E,0,0],GR=[...G,0,0];
 const er=zero?ER.map(()=>0):ER,gr=zero?GR.map((v,j)=>md(v-rat*ER[j])):GR;
 const Lc=zero?[lc[0],0,md(lc[2]-rat*lc[1])]:lc;
 const rows=Array.from({length:5},(_,j)=>[wr[j],er[j],gr[j]]);
 const fac=(base,c,j)=>factor(base,c,rows[j],obs[j],cap,zcap);
 let flat=add(mul(fac(1,f1,0),fac(2,ss2,1),cap,zcap),
  scale(mul(fac(3,f3,0),fac(0,theta,1),cap,zcap),pp-1));
 for(let j=2;j<5;j++)flat=mul(flat,fac(1,sig,j),cap,zcap);
 flat=scale(flat,iv(42));
 let BP=[[0,0,0,0,1]];
 for(let k=1;k<=MAXBLOCK+1;k++)if(6*k<=cap)BP=add(BP,scale(linpow(Lc,6*k),bc[k]));
 const full=mul(flat,BP,cap,zcap);
 const get=(deg,j)=>Object.fromEntries(full.filter(v=>v[0]+v[1]+v[2]===deg&&v[3]===6*j)
  .map(v=>[v.slice(0,3).join(","),md(v[4]*(i?-1:1))]));
 const J=Math.floor(zcap/6)+1;
 return {i,endpoint,observation,zcap,rows,obs,
  ...Object.fromEntries(Array.from({length:MAXBLOCK+1},(_,h)=>[
   "gen"+(6*h+6),Array.from({length:J},(_,j)=>get(6*h+6,j))])),
  unweighted:Array.from({length:J},(_,j)=>(get(0,j)["0,0,0"]||0)),terms:full.length};
}
function makePair(i,e,observation="S",zcap=30,cap=CAP){
 const a=makeSource(i,e,observation,zcap,cap,false);
 a.zero=makeSource(i,e,observation,zcap,cap,true);
 return a;
}
const generators={};
for(const [i,e] of [[0,0],[1,0],[0,1]]){
 console.error("R693: full adaptation generator "+i+"_"+e);
 generators[i+"_"+e]=makePair(i,e);
}
function mm(A,B){return A.map(R=>B[0].map((_,j)=>md(R.reduce((s,c,k)=>md(s+c*B[k][j]),0))));}
function elim(M,rhs=null){
 const A=M.map((R,i)=>rhs?[...R,rhs[i]]:R.slice());let rank=0,piv=[],det=1;
 for(let c=0;c<M[0].length&&rank<M.length;c++){
  let r=rank;while(r<A.length&&!A[r][c])r++;if(r===A.length)continue;
  if(r!==rank){[A[r],A[rank]]=[A[rank],A[r]];det=md(-det);}
  const d=A[rank][c];det=md(det*d);A[rank]=A[rank].map(x=>md(x*iv(d)));
  for(let j=0;j<A.length;j++)if(j!==rank&&A[j][c]){
   const z=A[j][c];A[j]=A[j].map((x,k)=>md(x-z*A[rank][k]));
  }
  piv.push(c);rank++;
 }
 const sol=rhs?Array(M[0].length).fill(0):null;
 if(rhs)for(let j=0;j<rank;j++)sol[piv[j]]=A[j].at(-1);
 return {rank,piv,det,solution:sol,reduced:A,inconsistent:rhs&&A.slice(rank).some(R=>R.at(-1)!==0)};
}
console.error("R693: full native W generator through z^72; original total moment <="+(72+CAP));
const GW=makePair(0,1,"W",MAXZ),native=GW.unweighted;
assert(native[0]===0&&native[1]===ne(6,12),"native W = 6 delta T");


/* B0 is the integral, genuine Pi4-observable perpendicular to Y,W,C,D,G.
 Its full returning weight is transported before the E-unit inverse.
 At kappa=u=0 its value is Bperp, the first-four projection off A,Dstar. */
const ombar=md(-1-om),pa=(a,b=0,d=1)=>[ne(a,b,d),md((a+ombar*b)*iv(d))];
const padd=(x,y)=>x.map((v,j)=>md(v+y[j])),pneg=x=>x.map(v=>md(-v));
const psub=(x,y)=>padd(x,pneg(y)),pmul=(x,y)=>x.map((v,j)=>md(v*y[j]));
const pdiv=(x,y)=>x.map((v,j)=>md(v*iv(y[j])));
const vadd=(x,y)=>x.map((v,j)=>padd(v,y[j])),vsub=(x,y)=>x.map((v,j)=>psub(v,y[j]));
const vscale=(x,a)=>x.map(v=>pmul(v,a));
const hp=(x,y)=>x.reduce((v,z,j)=>padd(v,[md(z[0]*y[j][1]),md(z[1]*y[j][0])]),pa(0));
const perp=(v,a)=>vsub(v,vscale(a,pdiv(hp(v,a),hp(a,a))));
let Bgeometry=null,Bweight=null,Bweight0=null,Bgenerators=null,BGW=null;
function buildB(){
 const Ar=[pa(1,2),pa(2,4),pa(3,1),pa(2,-1),pa(0),pa(0)];
 const D4=[pa(1),pa(-1,-1),pa(0,-2),pa(0),pa(0),pa(0)];
 const Cr=vscale([pa(1),pa(0),pa(-1),pa(1),pa(0),pa(0)],pdiv(pa(1),pa(1,2)));
 const H1=[pa(-1),pa(2),pa(0,1),pa(1,1),pa(0),pa(0)];
 const c=[pa(0),pa(0),pa(0),pa(0),pa(1),pa(0)];
 const d=[pa(0),pa(0),pa(0),pa(0),pa(0),pa(1)];
 const Dr=vadd(D4,vadd(c,vscale(d,pa(2,3))));
 const Fr=vadd(Dr,Cr),Gr=vadd(vscale(H1,pa(13)),vscale(Fr,pa(3,-2)));
 const Yr=vadd(Ar,vadd(c,vscale(d,pa(2))));
 const Wr=vadd(Ar,vadd(vscale(c,pa(3,6)),vscale(d,pa(4))));
 const Wpr=[pa(4,4),pa(2,4),pa(4,4),pa(0),pa(4,2),pa(4)];
 const Br=[pa(426,263),pa(63),pa(121,342),pa(-305,79),pa(2,-71),pa(217,77)];
 const Bformula=vscale(vsub(vsub(Wpr,vscale(Yr,pa(259,161,263))),vscale(Wr,pa(25,-119,263))),pa(263,0,2));
 assert(Br.every((x,j)=>x.every((v,k)=>v===Bformula[j][k])),"B0 complete Pi4 row");
 for(const [lab,V] of [["Y",Yr],["W",Wr],["C",Cr],["D",Dr],["G",Gr]])
  assert(hp(Br,V).every(x=>x===0),"B0 perpendicular to "+lab);
 assert(hp(Br,Br).every(x=>x===md(397656)),"B0 exact norm");
 const Ds=perp(D4,Ar),Cp=perp(Cr,Ds),H1p=perp(H1,Ds);
 const Er=vscale(Cp,pa(14)),Gp=vadd(vscale(H1p,pa(13)),vscale(Cp,pa(3,-2)));
 const flat=V=>[
 psub(pdiv(psub(V[0],V[2]),pa(6)),pdiv(V[3],pa(3)))[0],
 pdiv(padd(V[0],V[2]),pa(2))[0],V[1][0],
 pmul(pa(1,2,3),padd(psub(V[0],V[2]),V[3]))[0]];
 for(const [lab,row,expected] of [["Dstar",Ds,[...D,lc[0]]],["Eperp",Er,[...E,lc[1]]],["Gperp",Gp,[...G,lc[2]]]])
  assert(flat(row).every((v,j)=>v===expected[j]),"same entire five-input frame for "+lab);
 const Bp=perp(perp([...Br.slice(0,4),pa(0),pa(0)],Ar),Ds);
 let ab=null,selected=null;
 for(let j=0;j<4&&!ab;j++)for(let k=j+1;k<4&&!ab;k++){
  const det=psub(pmul(Er[j],Gp[k]),pmul(Er[k],Gp[j]));
  if(det.some(v=>v===0))continue;
  ab=[pdiv(psub(pmul(Bp[j],Gp[k]),pmul(Bp[k],Gp[j])),det),
      pdiv(psub(pmul(Er[j],Bp[k]),pmul(Er[k],Bp[j])),det)];selected=[j,k];
 }
 assert(ab!==null,"Bperp basis solve");
 const rebuild=vadd(vscale(Er,ab[0]),vscale(Gp,ab[1]));
 assert(Bp.every((x,j)=>x.every((v,k)=>v===rebuild[j][k])),"full first-four Bperp=aEperp+bGperp");
 const ae=ab[0][0],bg=ab[1][0];
 Bweight=Object.fromEntries(Array.from({length:7},(_,j)=>[
  "0,"+j+","+(6-j),md(cb(6,j)*pow(ae,j)*pow(bg,6-j))]).filter(x=>x[1]));
 Bweight0={"0,0,6":pow(bg,6)};
 Bgeometry={norm:397656,integral_row:"(426+263w,63,121+342w,-305+79w,2-71w,217+77w)",
  projection:"Bperp=projection of first four B0 coordinates off A and Dstar",
  residue_coefficients_Eperp_Gperp:ab,selected_basis_coordinates:selected,
  E_inverse_scope:"Only P is mapped to P(D,0,G); Bperp^6 is NOT mapped to its E=0 value in the full branch",
  C_zero_scope:"The C-zero branch separately replaces Bperp by b*G00"};
 DEBOUND=12; Bgenerators={};
 for(const [i,e] of [[0,0],[1,0],[0,1]])Bgenerators[i+"_"+e]=makePair(i,e,"S",30,12);
 BGW=makePair(0,1,"W",MAXZ,12);DEBOUND=6;
}
if(WITHB){console.error("R693: complete independent B0^6 block, including its C and E transposes");buildB();}

function analyze(TAU){
const AP=all.matrix.Aplus.map(R=>R.map(ef)),AZ=all.matrix.Azero.map(R=>R.map(ef));
const BM=all.polynomial_right_inverse.B.map(M=>M.map(R=>R.map(ef)));
const A2=AP.map((R,i)=>R.map((x,j)=>md(x+TAU*AZ[i][j])));
const B2=BM[0].map((R,i)=>R.map((x,j)=>md((x+TAU*BM[1][i][j])*iv(TAU-1))));
assert(mm(A2,B2).every((R,i)=>R.every((x,j)=>x===(i===j?1:0))),"original nine-row exact right inverse at this tau");
const BA=mm(B2,A2),PI=BA.map((R,i)=>R.map((x,j)=>md((i===j?1:0)-x)));
const piv=[0,1,2,3,4,13,15,16,17,18,19];
const cols=all.matrix.polys.map(P=>Object.fromEntries(Object.entries(P).map(([k,v])=>[k,ef(v)])));
const base=Object.fromEntries(Object.entries(all.matrix.base).map(([k,v])=>[k,ef(v)]));
const e0=P=>Object.fromEntries(Object.entries(P).filter(([k])=>+k.split(",")[1]===0));
const shifted=(P,n)=>Object.fromEntries(Object.entries(P).map(([k,v])=>{let a=k.split(",").map(Number);a[2]+=n;return[a.join(","),v];}));
const der2=P=>Object.fromEntries(Object.entries(P).filter(([k])=>+k.split(",")[0]>=2)
 .map(([k,v])=>{let a=k.split(",").map(Number),c=md(v*a[0]*(a[0]-1));a[0]-=2;return[a.join(","),c];}));
const moment=(P,H)=>Object.entries(P).reduce((s,[k,c])=>{
 const a=k.split(",").map(Number);return md(s+c*(H[k]||0)*md(fact[a[0]]*fact[a[1]]*fact[a[2]]));
},0);
// Directly precompose the C-unit core G -> G-rat*E BEFORE truncation.
// Otherwise D+E<=6 trimming would lose high E terms that become G powers.
const evalRow=(P,H,H0,eta)=>md(moment(P,H)+(TAU-1)*(moment(e0(P),H)+eta*moment(e0(P),H0)));

function massGen(zero=false,requestedCap=CAP-2){
 const er=zero?E.map(()=>0):E,gr=zero?G.map((v,j)=>md(v-rat*E[j])):G;
 const Lc=zero?[lc[0],0,md(lc[2]-rat*lc[1])]:lc;
 const R=Array.from({length:3},(_,j)=>[D[j],er[j],gr[j]]),cap=requestedCap;
 let P=add(mul(factor(1,f1,R[0],0,cap,0),factor(2,ss2,R[1],0,cap,0),cap,0),
  scale(mul(factor(3,f3,R[0],0,cap,0),factor(0,theta,R[1],0,cap,0),cap,0),pp-1));
 P=scale(mul(P,factor(1,sig,R[2],0,cap,0),cap,0),iv(42));
 let BP=[[0,0,0,0,1]];
 for(let k=1;6*k<=cap;k++)BP=add(BP,scale(linpow(Lc,6*k),bc[k]));
 const T=mul(P,BP,cap,0);
 return Object.fromEntries(Array.from({length:MAXBLOCK+1},(_,h)=>4+6*h).map(d=>[
  d,Object.fromEntries(T.filter(v=>v[0]+v[1]+v[2]===d).map(v=>[v.slice(0,3).join(","),v[4]]))]));
}
const MG=massGen(),MG0=massGen(true);
let MGB=null,MGB0=null;
if(WITHB){DEBOUND=12;MGB=massGen(false,10);MGB0=massGen(true,10);DEBOUND=6;}
const polyMul=(P,Q)=>{
 const out={};for(const[k,v]of Object.entries(P))for(const[l,w]of Object.entries(Q)){
  const a=k.split(",").map(Number),b=l.split(",").map(Number),key=a.map((x,j)=>x+b[j]).join(",");
  out[key]=md((out[key]||0)+v*w);
 }return Object.fromEntries(Object.entries(out).filter(x=>x[1]));
};
const evalB=(P,H,H0,eta)=>md(moment(polyMul(P,Bweight),H)
 +(TAU-1)*moment(polyMul(e0(P),Bweight),H)
 +eta*(TAU-1)*moment(polyMul(e0(P),Bweight0),H0));

const makeBasis=(N,J)=>{
 const sp=pw(sig,N,J),T=Array.from({length:J+1},()=>Array(J+1).fill(0));
 for(let j=0;j<=J;j++){
  const a=N/2-3*j,cv=conv(sp,pw(xx,a,J),J);
  for(let r=j;r<=J;r++)T[r][j]=cv[r-j];
 }
 return T;
};
const basis34=makeBasis(34,5),Scoords=[0,1,ne(-53,0,7),ne(-12,0,7),ne(-80,0,7),ne(-128,0,7)];
const Sjet=mm(basis34,Scoords.map(x=>[x])).map(x=>x[0]);
const bp=all.matrix.target.map((x,i)=>md(ef(x)-ef(all.matrix.basePlus[i])-TAU*ef(all.matrix.baseZero[i])));
const xp=mm(B2,bp.map(x=>[x])).map(R=>R[0]);
const addPoly=(P,R,c=1)=>{
 const T={...P};for(const[k,v]of Object.entries(R))T[k]=md((T[k]||0)+c*v);
 return Object.fromEntries(Object.entries(T).filter(([k,v])=>v));
};
let Pold={...base};cols.forEach((P,j)=>{Pold=addPoly(Pold,P,xp[j]);});
const dcols=piv.map(j=>cols.reduce((P,C,i)=>addPoly(P,C,PI[i][j]),{}));
const gcount=11*(MAXBLOCK+1);
const extcols=Array.from({length:MAXBLOCK+1},(_,h)=>dcols.map(P=>shifted(P,6*h))).flat();
if(WITHB)extcols.push(...dcols);
const degreeAt=j=>6+6*Math.floor(j/11);
const gen=(source,j,h)=>source["gen"+degreeAt(j)][h];
const readRow=(P,j,src,bsrc,h,eta)=>j<gcount
 ?evalRow(P,gen(src,j,h),gen(src.zero,j,h),eta)
 :evalB(P,bsrc.gen12[h],bsrc.zero.gen12[h],eta);

function build(eta){
 const M=[],old=[],labels=[];
 for(const[i,e]of [[0,0],[1,0],[0,1]])for(let h=0;h<6;h++){
  const src=generators[i+"_"+e];
  M.push(extcols.map((P,j)=>readRow(P,j,src,WITHB?Bgenerators[i+"_"+e]:null,h,eta)));
  old.push(evalRow(Pold,src.gen6[h],src.zero.gen6[h],eta));
  labels.push({source:"S",branch:i,endpoint:e,jet:6*h});
 }
 // W mass is already fixed by the same endpoint S mass. Do not count it twice.
 for(let h=1;h<13;h++){
  M.push(extcols.map((P,j)=>readRow(P,j,GW,BGW,h,eta)));
  old.push(evalRow(Pold,GW.gen6[h],GW.zero.gen6[h],eta));
  labels.push({source:"native 6delta T",jet:6*h});
 }
 M.push(extcols.map((P,j)=>j<gcount?evalRow(der2(P),MG[degreeAt(j)-2],MG0[degreeAt(j)-2],eta):evalB(der2(P),MGB[10],MGB0[10],eta)));
 old.push(evalRow(der2(Pold),MG[4],MG0[4],eta));labels.push({source:"normalized J2"});
 const target=[...Sjet,...Sjet,...Sjet,...native.slice(1),1];
 const rhs=target.map((x,i)=>md(x-old[i])),full=elim(M,rhs);
 const old19=[...Array.from({length:18},(_,i)=>i),30].map(i=>M[i].slice(0,19));
 if(TAU===2)assert(elim(old19).det===(eta===1?770:888),"same original nineteen actual columns");
 return {eta,matrix:M,old,target,rhs,labels,rank:full.rank,pivots:full.piv,consistent:!full.inconsistent,free_solution:full.solution};
}
const candidates=[1,-1].map(build);
let common=null;
if(candidates.every(c=>c.rank===31&&c.consistent)){
 for(const indices of candidates.map(c=>c.pivots)){
  if(candidates.every(c=>elim(c.matrix.map(R=>indices.map(j=>R[j]))).rank===31)){
   common=indices;break;
  }
 }
}

const data=candidates.map(c=>{
 const selected=common||(c.rank===31?c.pivots:null);
 let selectedDet=null,solution=null,verified=false,sourceRows=null;
 if(selected){
  const M=c.matrix.map(R=>selected.map(j=>R[j])),v=elim(M,c.rhs);
  assert(v.rank===31&&!v.inconsistent,"selected actual full system");
  selectedDet=v.det;solution=Array(extcols.length).fill(0);
  selected.forEach((col,j)=>{solution[col]=v.solution[j];});
  verified=mm(c.matrix,solution.map(x=>[x])).every((R,j)=>R[0]===c.rhs[j]);
  assert(verified,"all thirty-one actual equations");
  sourceRows=mm(c.matrix,solution.map(x=>[x])).map((R,j)=>md(R[0]+c.old[j]));
  const W0=md(evalRow(Pold,GW.gen6[0],GW.zero.gen6[0],c.eta)+extcols.reduce((sum,P,j)=>
   md(sum+solution[j]*readRow(P,j,GW,BGW,0,c.eta)),0));
  assert(W0===0,"native W mass also satisfied exactly");
 }
 return {...c,selected_columns:selected,selected_determinant:selectedDet,
  full_solution:solution,verified_all31:verified,computed_source_rows:sourceRows};
});

const freeResults=[];
if(FREE_NORMALIZATIONS){
 const ncol=extcols.length;
 const targets=Array.from({length:4},()=>Array(31).fill(0));
 for(let b=0;b<3;b++)for(let j=0;j<6;j++)targets[b][6*b+j]=Sjet[j];
 for(let j=1;j<13;j++)targets[3][17+j]=native[j];
 const pairs=[[0,1],[0,3],[1,3],[2,3],[0,2],[1,2]];
 for(const c of candidates){
  const rows=[];
  for(const free of pairs){
   const A=c.matrix.map((row,i)=>[...row,...free.map(j=>md(-targets[j][i]))]);
   const rhs=c.target.map((v,i)=>md(v-c.old[i]-free.reduce((a,j)=>a+targets[j][i],0)));
   const e=elim(A,rhs);let chosen=null,chosenRows=null,det=null,values=null,solution=null,verified=false;
   if(e.rank>=30&&!e.inconsistent){
    chosen=e.piv;
    const colMatrix=A.map(row=>chosen.map(j=>row[j]));
    chosenRows=elim(chosen.map((_,j)=>colMatrix.map(R=>R[j]))).piv;
    const m=chosenRows.map(i=>colMatrix[i]),x=elim(m,chosenRows.map(i=>rhs[i]));
    det=x.det;solution=Array(A[0].length).fill(0);
    chosen.forEach((j,k)=>{solution[j]=x.solution[k];});
    values=[1,1,1,1];free.forEach((j,k)=>{values[j]=solution[ncol+k];});
    verified=mm(A,solution.map(v=>[v])).every((r,i)=>r[0]===rhs[i]);
    assert(verified,"all actual equations with free source normalizations");
    const W0=md(evalRow(Pold,GW.gen6[0],GW.zero.gen6[0],c.eta)+extcols.reduce((sum,P,j)=>
     md(sum+solution[j]*readRow(P,j,GW,BGW,0,c.eta)),0));
    assert(W0===0,"whole W mass preserved in proportional target");
   }
   rows.push({free_source_indices:free,rank:e.rank,consistent:!e.inconsistent,
    determinant:det,source_scalars:values,selected_columns:chosen,selected_rows:chosenRows,verified});
  }
  freeResults.push({eta:c.eta,choices:rows});
 }
 const preferred=pairs.find(pair=>freeResults.every(c=>c.choices.some(q=>
  q.free_source_indices.join(",")===pair.join(",")&&q.rank>=30&&q.consistent)));
 for(const c of freeResults){
  c.preferred_free_indices=preferred||null;
  if(preferred){
   const original=candidates.find(q=>q.eta===c.eta),choice=c.choices.find(q=>q.free_source_indices.join(",")===preferred.join(","));
   const A=original.matrix.map((row,i)=>[...row,...preferred.map(j=>md(-targets[j][i]))]);
   const rhs=original.target.map((v,i)=>md(v-original.old[i]-preferred.reduce((a,j)=>a+targets[j][i],0)));
   const x=elim(choice.selected_rows.map(i=>choice.selected_columns.map(j=>A[i][j])),choice.selected_rows.map(i=>rhs[i]));
   const sol=Array(A[0].length).fill(0);choice.selected_columns.forEach((j,k)=>sol[j]=x.solution[k]);
   c.preferred_full_solution=sol;
   c.preferred_source_rows=mm(original.matrix,sol.slice(0,ncol).map(v=>[v])).map((r,i)=>md(r[0]+original.old[i]));
   c.preferred_is_only_auxiliary_if_rank30=choice.rank===30;
   const fullA=original.matrix.map((row,i)=>[...row,...targets.map(T=>md(-T[i]))]);
   const tr=fullA[0].map((_,j)=>fullA.map(R=>R[j])),rr=elim(tr),pivset=new Set(rr.piv);
   c.all_four_target_rank=rr.rank;
   c.all_four_target_left_relations=[];
   for(let f=0;f<31;f++)if(!pivset.has(f)){
    const v=Array(31).fill(0);v[f]=1;
    rr.piv.forEach((j,k)=>{v[j]=md(-rr.reduced[k][f]);});
    assert(tr.every(row=>md(row.reduce((sum,x,j)=>sum+x*v[j],0))===0),"entire auxiliary left relation");
    c.all_four_target_left_relations.push({row:v,nonzero_support:v.map((x,j)=>x?[j,x]:null).filter(Boolean),
     old_affine_value:md(v.reduce((sum,x,j)=>sum+x*original.old[j],0)),
     j2_coefficient:v[30]});
   }
  }
  c.choices=c.choices.map(q=>q.free_source_indices.join(",")===(preferred||[]).join(",")?q:{...q,selected_columns:undefined,selected_rows:undefined});
 }
}
const result={
 format:"R693 actual neutral G6-power extension: three S sources, native W=6deltaT, and normalized J2",
 auxiliary:{p:pp,omega:om,tau:TAU,lambda:md((1-TAU)*iv(TAU)),kappa:0,u:0,b:1,Omega:1},
 actual_columns:"eleven original Pi4-zero columns times G^(6h)/(b^h Omega^(6h)), h=0,...,max_block; with --with-b append the eleven ORIGINAL columns times B0^6/(b Omega^6)",
 max_block:MAXBLOCK,with_B:WITHB,B_geometry:Bgeometry,free_normalizations:FREE_NORMALIZATIONS,proportional_adaptation:freeResults,source_scalar_order:["frozen S0","frozen S1","cd S","native 6delta T"],
 degree_blocks:Array.from({length:MAXBLOCK+1},(_,h)=>6+6*h),column_count:extcols.length,constraint_count:31,
 constraint_order:"frozen S0 six jets; frozen S1 six jets; cd endpoint S six jets; native W jets 6,...,72; normalized J2=1",
 original_kernel_indices:piv,common_selected_columns:common,
 highest_original_total_moment:72+CAP,
 C_factor_coefficients_mod1009:bc,
 C_factor_definition:"-y(s/delta)*sigma(s/delta)^3, all C^(6h) through CAP retained",
 exact_trim:"G blocks: D+E<=6 only after separately precomposing both full and C-zero sources. B0 block: its own full degree12 generators with D+E<=12; E-zero acts only on the original P, and the C-zero multiplier is separately (b G00)^6.",
 block_ranks:candidates.map(c=>({eta:c.eta,ranks:Array.from({length:MAXBLOCK+1},(_,h)=>elim(c.matrix.map(R=>R.slice(0,11*(h+1)))).rank),rank_with_B:c.rank})),
 native_W_jets:native,
 source_input_sha256:crypto.createHash("sha256").update(inputCode).digest("hex"),
 certificate:data.map(c=>REPORT_FULL?c:{...c,matrix:undefined}),
 full_matrix_omitted:!REPORT_FULL,
 actual_lift:"A nonzero full31 minor proves an actual full inverse. A rank30 auxiliary solution and its left relation do NOT by themselves establish an actual solution: the complete characteristic-zero relation or saturated higher-parameter Schur correction remains required. No auxiliary solution is substituted into the p-adic test.",
 arithmetic_scope:"All original Pi4 rows remain unchanged. New zero-mass corner claims are not inherited; all higher J_(2+6h) and positive pair masses must be retained. Z-scaled A_T is not identified with native W.",
 outputs_persisted:false
};
return result;
}
const report={
 format:"R693 actual G6-power family at fixed auxiliary tau values",
 max_block:MAXBLOCK, taus:TAUS,with_B:WITHB,free_normalizations:FREE_NORMALIZATIONS,
 entries:TAUS.map(t=>{console.error("R693: exact row algebra at tau="+t);return analyze(t);}),
 outputs_persisted:false
};
console.error("R693 completed in "+((Date.now()-start)/1000)+" seconds");
process.stdout.write(JSON.stringify(report)+"\n");
