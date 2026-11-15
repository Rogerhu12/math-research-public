#!/usr/bin/env node
"use strict";
/*
R715: actual first-Z source of the same R702/R713 cd carry.
Reuses the complete original R702 generator, then differentiates Y+epsilon*Z
with epsilon^2=0. The five type-5 coordinates are read from epsilon*z^(6+6j).
No prior output tables are read. All old sources, C30 terms, E inverses and
the original neutral-difference direction are retained.
Run publicly: node check-r715-native-z-first-moment.js --max-block=4 --taus=2,3 --with-b --b-g-blocks=3 --neutral-degree=12
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
const MAXBLOCK=arg?Number(arg.split("=")[1]):4;
const WITHB=process.argv.includes("--with-b");
const argBG=process.argv.slice(2).find(x=>x.startsWith("--b-g-blocks="));
const BGMAX=argBG?Number(argBG.split("=")[1]):0;
assert(Number.isInteger(BGMAX)&&BGMAX>=0&&BGMAX<MAXBLOCK,"B-G blocks must fit the original total degree");
const FREE_NORMALIZATIONS=process.argv.includes("--free-normalizations");
const argND=process.argv.slice(2).find(x=>x.startsWith("--neutral-degree="));
const NDEG=argND?Number(argND.split("=")[1]):0;
assert(NDEG===0||(NDEG===12&&WITHB),"new complete C-neutral block currently has degree 12 and requires the full D/E generator");
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
 for(const [i,e] of [[0,0],[1,0],[0,1]])Bgenerators[i+"_"+e]=makePair(i,e,"S",30,CAP);
 BGW=makePair(0,1,"W",MAXZ,CAP);DEBOUND=6;
}
if(WITHB){console.error("R693: complete independent B0^6 block, including its C and E transposes");buildB();}

/* Complete first-Z source: derivative of the observation Y+epsilon Z,
   not a derivative of the hidden weight and not a change of unit cut. */
function factorObservationDerivative(base,coeff,row,obs,dr,cap=CAP,zcap=30){
 let out=[];
 for(let h=0;h<coeff.length;h++){
  const n=base+6*h;if(n>cap+zcap)break;
  for(let r=0;r<=Math.min(cap,n);r++){
   const z=n-r;if(z<1||z>zcap)continue;
   const a=md(md(coeff[h]*cb(n,r))*md(z*dr)*pow(obs,z-1));
   for(const[d,e,g,,v]of linpow(row,r)){const c=md(v*a);if(c)out.push([d,e,g,z,c]);}
  }
 }
 return out;
}
function makeFirstZSource(zero=false,cap=CAP){
 const i=0,ei=ne(-170,-117,9135),hh=ne(-5,-9),zcap=30;
 const obs=[...A,1,2].map(md),bY=ne(20,3,17),Wobs=[...A,ne(3,6),4];
 const dr=obs.map((v,j)=>md(Wobs[j]-bY*v));
 let wr=[...D.map((x,j)=>md(x+5*ei*A[j])),md(-87*ei),md(-29*ei)];
 const v=[...A.map(x=>5*x),39,-92];wr=wr.map((x,j)=>md(x+hh*v[j]*iv(315)));
 const ER=[...E,0,0],GR=[...G,0,0];
 const er=zero?ER.map(()=>0):ER,gr=zero?GR.map((v,j)=>md(v-rat*ER[j])):GR;
 const Lc=zero?[lc[0],0,md(lc[2]-rat*lc[1])]:lc;
 const rows=Array.from({length:5},(_,j)=>[wr[j],er[j],gr[j]]);
 const df=(base,c,j)=>[
  factor(base,c,rows[j],obs[j],cap,zcap),
  factorObservationDerivative(base,c,rows[j],obs[j],dr[j],cap,zcap)];
 const dm=(a,b)=>[mul(a[0],b[0],cap,zcap),
  add(mul(a[1],b[0],cap,zcap),mul(a[0],b[1],cap,zcap))];
 const da=(a,b)=>a.map((P,j)=>add(P,b[j]));
 const ds=(a,c)=>a.map(P=>scale(P,c));
 let flat=da(dm(df(1,f1,0),df(2,ss2,1)),ds(dm(df(3,f3,0),df(0,theta,1)),pp-1));
 for(let j=2;j<5;j++)flat=dm(flat,df(1,sig,j));
 flat=ds(flat,iv(42));
 let BP=[[0,0,0,0,1]];
 for(let k=1;6*k<=cap;k++)BP=add(BP,scale(linpow(Lc,6*k),bc[k]));
 const full=mul(flat[1],BP,cap,zcap);
 const get=(deg,j)=>Object.fromEntries(full.filter(v=>v[0]+v[1]+v[2]===deg&&v[3]===6*(j+1))
  .map(v=>[v.slice(0,3).join(","),v[4]]));
 return {rows,obs,dr,
  ...Object.fromEntries(Array.from({length:MAXBLOCK+1},(_,h)=>[
   "gen"+(6*h+6),Array.from({length:5},(_,j)=>get(6*h+6,j))])),
  unweighted:Array.from({length:5},(_,j)=>get(0,j)["0,0,0"]||0),terms:full.length};
}
console.error("R715: same cd source, full first-Z derivative and both C branches");
const ZG=makeFirstZSource();ZG.zero=makeFirstZSource(true);
let ZBG=null;
if(WITHB){DEBOUND=12;ZBG=makeFirstZSource();ZBG.zero=makeFirstZSource(true);DEBOUND=6;}
assert(ZG.unweighted[0]===md(6+ne(3,6)-6*ne(20,3,17)),
 "unweighted first-Z leading coefficient is the full six-sigma directional derivative");
const firstZBasis=Array.from({length:5},()=>Array(5).fill(0));
for(let j=0;j<5;j++){
 const cv=conv(conv(pw(sig,34,4),pw(xx,13-3*j,4),4),my.slice(0,5),4);
 for(let k=j;k<5;k++)firstZBasis[k][j]=cv[k-j];
}



/* R702 complete first-2Y quarter source.
   All computations below are performed only by this public Node script.
   A point evaluation uses the entire S136 line bundle, not a sampled claim
   of membership.  The known S136 bound makes 23 distinct X=x^3 values
   an injective exact coordinate map.
   The C average commutes with every W torsion translate.  Its complete
   factor B_C(C) is retained through CAP; the remaining rows are projected
   off C before taking the six raw sigma logarithmic derivatives.
*/
const QCAP=CAP,QBMAX=WITHB?12:6;
const qprod=(...xs)=>xs.reduce((v,x)=>md(v*x),1);
const qAllowed=(a,b,g)=>a+b+g<=CAP&&(a+b<=6||(WITHB&&a+b<=12));
const qGmax=(a,b)=>a+b<=6||(WITHB&&a+b<=12)?CAP-a-b:-1;
const qPairs=[];
for(let n=0;n<=QBMAX;n++)for(let a=0;a<=n;a++)qPairs.push([a,n-a]);
const qkey=(a,b)=>a+","+b;
const quad=(f2)=>{
 const ad=(x,y)=>[md(x[0]+y[0]),md(x[1]+y[1])];
 const ng=x=>[md(-x[0]),md(-x[1])];
 const su=(x,y)=>ad(x,ng(y));
 const sc=(x,a)=>[md(x[0]*a),md(x[1]*a)];
 const mu=(x,y)=>[md(x[0]*y[0]+f2*x[1]*y[1]),md(x[0]*y[1]+x[1]*y[0])];
 const inv=x=>{const d=md(x[0]*x[0]-f2*x[1]*x[1]);return sc([x[0],md(-x[1])],iv(d));};
 const di=(x,y)=>mu(x,inv(y));
 const pw=(x,n)=>{let y=[1,0];for(;n;n=Math.floor(n/2),x=mu(x,x))if(n%2)y=mu(y,x);return y;};
 return {ad,ng,su,sc,mu,inv,di,pw,f2};
};
const bcLog=[0];
for(let n=1;n<=MAXBLOCK+1;n++){
 let v=bc[n]||0;
 for(let k=1;k<n;k++)v=md(v-md(k*bcLog[k]*(bc[n-k]||0))*iv(n));
 bcLog[n]=v;
}
const Araw=[pa(1,2),pa(2,4),pa(3,1),pa(2,-1),pa(0),pa(0)];
const Craw=vscale([pa(1),pa(0),pa(-1),pa(1),pa(0),pa(0)],pdiv(pa(1),pa(1,2)));
const D4raw=[pa(1),pa(-1,-1),pa(0,-2),pa(0),pa(0),pa(0)];
const H1raw=[pa(-1),pa(2),pa(0,1),pa(1,1),pa(0),pa(0)];
const cRaw=[pa(0),pa(0),pa(0),pa(0),pa(1),pa(0)];
const dRaw=[pa(0),pa(0),pa(0),pa(0),pa(0),pa(1)];
const Hraw=vadd(D4raw,vadd(cRaw,vscale(dRaw,pa(2,3))));
const Dsraw=perp(D4raw,Araw),Cpraw=perp(Craw,Dsraw),H1praw=perp(H1raw,Dsraw);
const Erraw=vscale(Cpraw,pa(14)),Grraw=vadd(vscale(H1praw,pa(13)),vscale(Cpraw,pa(3,-2)));
const G00raw=vsub(Grraw,vscale(Erraw,pa(-789,526,1596)));
const Yraw=vadd(Araw,vadd(cRaw,vscale(dRaw,pa(2))));
const Wraw=vadd(Araw,vadd(vscale(cRaw,pa(3,6)),vscale(dRaw,pa(4))));
const Zraw=vsub(Wraw,vscale(Yraw,pa(20,3,17)));
assert(hp(Zraw,Yraw).every(x=>x===0)&&hp(Zraw,Craw).every(x=>x===0),
 "first-Z derivative preserves the true Y bundle and the complete C factor");
assert(hp(Craw,Craw).every(x=>x===1),"C has true norm one");
for(const [lab,r]of [["H",Hraw],["Eperp",Erraw],["Gperp",Grraw],["G00",G00raw]])
 for(const [ax,a]of [["Y",Yraw],["W",Wraw]])
  assert(hp(r,a).every(x=>x===0),lab+" is a complete "+ax+" companion");
const quarterRows={};
for(const zero of [false,true]){
 const rs=[Hraw,zero?Erraw.map(()=>pa(0)):Erraw,zero?G00raw:Grraw];
 const ls=rs.map(r=>hp(r,Craw)[0]);
 const prs=rs.map(r=>perp(r,Craw));
 const rows=Array.from({length:6},(_,i)=>prs.map(r=>r[i][0]));
 const weights=[];
 for(const[a,b]of qPairs)for(let g=0;g<=qGmax(a,b);g++){
  const n=a+b+g;if(!n)continue;
  const multi=md(fact[n]*iv(md(fact[a]*fact[b]*fact[g])));
  weights.push({a,b,g,n,coeff:rows.map(r=>md(multi*pow(r[0],a)*pow(r[1],b)*pow(r[2],g))),
   bc:n%6?0:md(multi*(bcLog[n/6]||0)*pow(ls[0],a)*pow(ls[1],b)*pow(ls[2],g))});
 }
 quarterRows[String(zero)]={rows,ls,weights};
}
function qPointAdd(P,Q,F){
 if(!P)return Q;if(!Q)return P;
 const {ad,su,mu,di,sc}=F;
 const eq=(x,y)=>x[0]===y[0]&&x[1]===y[1];
 let slope;
 if(eq(P.x,Q.x)){
  assert(eq(P.y,Q.y)&&P.a===Q.a&&eq(P.z,Q.z),"point pole in public interpolation candidate");
  slope=di(sc(mu(P.x,P.x),3),sc(P.y,2));
 }else slope=di(su(P.y,Q.y),su(P.x,Q.x));
 const xr=su(su(mu(slope,slope),P.x),Q.x);
 const yr=su(mu(slope,su(P.x,xr)),P.y);
 return{x:xr,y:yr,z:ad(ad(P.z,Q.z),slope),a:md((P.a||0)+(Q.a||0))};
}
function qPointNeg(P,F){return{x:P.x,y:F.ng(P.y),z:F.ng(P.z),a:md(-(P.a||0))};}
function qPointTimes(P,n,F){
 if(n<0)return qPointTimes(qPointNeg(P,F),-n,F);
 let R=null;for(;n;n=Math.floor(n/2),P=qPointAdd(P,P,F))if(n%2)R=qPointAdd(R,P,F);
 return R;
}
function qCmPoints(x,y,F){
 const P={x:[x,0],y:[y,0],z:[0,0],a:1};
 const O={x:[md(om*x),0],y:[y,0],z:[0,0],a:md(om*om)};
 const labels=[[2,4],[4,8],[6,2],[4,-2],[2,0],[4,0]];
 return labels.map(([a,b],j)=>{
  const R=qPointAdd(qPointTimes(P,a,F),qPointTimes(O,b,F),F);
  assert(R.a===md(2*Yraw[j][1]),"complete CM zeta coefficient");
  return R;
 });
}
function qQuarterTorsion(e,F){
 const f2=F.f2,h=md(-1);
 const ht=[0,md(-3*e*e*iv(4*f2))];
 const T={x:[e,0],y:[0,1],z:ht,a:0};
 const OT={x:[md(om*e),0],y:[0,1],z:F.sc(ht,md(om*om)),a:0};
 const H={x:[h,0],y:[0,0],z:[0,0],a:0};
 const OH={x:[md(om*h),0],y:[0,0],z:[0,0],a:0};
 const Dt=qPointAdd(T,OH,F),Ga=qPointAdd(qPointNeg(T,F),OT,F);
 const Gb=qPointAdd(H,qPointNeg(OT,F),F);
 return[Dt,H,Ga,Gb,qPointNeg(Dt,F),null];
}
function qHalfTorsion(F){
 const h=md(-1),p=x=>({x:[x,0],y:[0,0],z:[0,0],a:0});
 return[p(h),null,p(md(om*om*h)),p(md(om*h)),p(h),null];
}
function qLogs(points,F){
 const {ad,mu,sc}=F;
 return points.map(P=>{
  const x=[P.x,sc(P.y,2)];
  for(let n=0;n+2<=QCAP-2;n++){
   let s=[0,0];for(let j=0;j<=n;j++)s=ad(s,mu(x[j],x[n-j]));
   x[n+2]=sc(s,md(6*iv((n+2)*(n+1))));
  }
  const L=Array(QCAP+1).fill(null);L[0]=[0,0];L[1]=P.z;
  for(let n=2;n<=QCAP;n++)L[n]=sc(x[n-2],md(-iv(n*(n-1))));
  return L;
 });
}
function qExpHidden(logs,zero,F){
 const {ad,sc,mu}=F,R=quarterRows[String(zero)];
 const L={};
 for(const[a,b]of qPairs)L[qkey(a,b)]=Array.from({length:qGmax(a,b)+1},()=>[0,0]);
 for(const w of R.weights){
  let s=[w.bc,0];
  for(let i=0;i<6;i++)if(w.coeff[i])s=ad(s,sc(logs[i][w.n],w.coeff[i]));
  L[qkey(w.a,w.b)][w.g]=s;
 }
 const U={},u0=[[1,0]],l0=L["0,0"];
 for(let n=1;n<=QCAP;n++){
  let s=[0,0];for(let j=1;j<=n;j++)s=ad(s,sc(mu(l0[j],u0[n-j]),j));
  u0[n]=sc(s,iv(n));
 }
 U["0,0"]=u0;
 for(const[a,b]of qPairs){
  const n=a+b;if(!n)continue;
  const gm=qGmax(a,b),out=Array.from({length:gm+1},()=>[0,0]);
  for(let c=0;c<=a;c++)for(let d=0;d<=b;d++){
   if(!c&&!d)continue;
   const l=L[qkey(c,d)],v=U[qkey(a-c,b-d)];if(!l||!v)continue;
   for(let g=0;g<=gm;g++){
    let s=[0,0];
    for(let j=0;j<=g&&j<l.length;j++)if(g-j<v.length)
      s=ad(s,mu(l[j],v[g-j]));
    out[g]=ad(out[g],sc(s,c+d));
   }
  }
  U[qkey(a,b)]=out.map(v=>sc(v,iv(n)));
 }
 const out={};
 for(const[a,b]of qPairs)for(let g=0;g<U[qkey(a,b)].length;g++)
  if((a+b+g)%6===0)out[[a,b,g].join(",")]=U[qkey(a,b)][g];
 return out;
}
const qPolynomial=(co,x)=>co.reduce((s,c)=>md(s*x+c),0);
function qSdouble(x){
 const X=pow(x,3),Y=md(X+1),xm=md(X-8),p=[rf("-128/7"),rf("-80/7"),rf("-12/7"),rf("-53/7"),1];
 let s=0;
 for(let j=0;j<=4;j++)s=md(s+p[j]*pow(Y,15-3*j)*pow(X,j)*pow(xm,3*j)*pow(iv(4),3*j));
 return qprod(pow(2,30),x,x,xm,xm,s);
}
function qNew(x){
 const X=pow(x,3);
 const blocks=[[1,1],[1,20,-8],[7,-4,16],[1,40,2112,3136,1792],
 [13,52,1536,1024,256],[1,1232,-58688,-49408,-439040,-2111488,-1949696,-851968,-32768]];
 return md(x*x*iv(91)*blocks.reduce((v,p)=>md(v*qPolynomial(p,X)),1));
}
function qXi(x){
 const X=pow(x,3),delta=ne(1,2);
 const H=md((X+1)*qPolynomial([1,20,-8],X)*qPolynomial([7,-4,16],X)*qPolynomial([1,40,2112,3136,1792],X));
 const ar=qPolynomial([17,-38136,-2117568,23348480,248235264,868082688,-518148096,2393505792,8501723136,6635651072,2686451712,591396864,-16777216],X);
 const ai=qPolynomial([31,-27000,-359904,9361408,-218937600,-1178698752,-3474518016,-2798419968,1462763520,2889613312,962592768,213909504,16777216],X);
 return md(-x*x*H*iv(7)*md(ar+delta*ai));
}
function qQuarterValue(x,y,e,F){
 const {ad,su,sc,mu,pw}=F,f2=F.f2,delta=ne(1,2),h=md(-1);
 const X=pow(x,3),Y=md(X+1),R2=md(X*X+20*X-8),ell=md(8*Y*Y);
 const xn=md(2*Y*x*(X-8)),eb=md(2*h-e),em=md(om*eb),en=md(om*om*eb),hm=md(om*h);
 const k=md(-3*delta*iv(f2)),de=md(xn-e*ell),dm=md(xn-em*ell);
 const u=[md(f2*ell+ne(3,0,2)*e*e*de),md(R2*y)];
 const nt=[md(e*xn*xn+e*e*xn*ell+2*ell*ell),md(-2*R2*ell*y)];
 const yt=ad([0,md(-R2*pow(de,3)*y)],
  mu([md(-f2*ell),md(R2*y)],su([md(xn*de*de),0],sc(nt,ell))));
 const mid=su(pw(nt,3),[md(8*pow(de,6)),0]);
 const p2=ad(su(sc(pw(nt,6),7),sc(pw(nt,3),md(4*pow(de,6)))),[md(16*pow(de,12)),0]);
 const um=[md(k*k*f2*ell+ne(3,0,2)*em*em*dm),md(k*R2*y)];
 const nm=[md(em*xn*xn+em*em*xn*ell+2*ell*ell),md(-2*k*R2*ell*y)];
 const difference=su([md(en*dm*dm),0],nm);
 let num=pw(u,14);
 for(const a of [um,difference,pw(nt,2),yt,mid,p2])num=mu(num,a);
 const c8=md((e-h)*iv(md(12*h*h*f2))),pe=md(7*pow(e,6)-4*pow(e,3)+16);
 const co=qprod(3,pow(2,32),pow(c8,7),pe,pe,iv(md(k*pow(f2,8))));
 const root=md(x*x-2*hm*x-2*hm*hm);
 const den=qprod(pow(ell,8),pow(md(xn-h*ell),7),md(xn-hm*ell),dm,dm,pow(de,25));
 return sc(num,md(pow(Y,15)*R2*root*co*iv(den)));
}
function qHalfValue(x){
 const X=pow(x,3),Y=md(X+1),x2=md(x*(X-8)*iv(md(4*Y))),t=md(x2+1),v=md(x2-2);
 const ph=qprod(ne(4,8,729),md(pow(x2,3)+1),t,t,v,v,
  md(-pow(v,3)-8*pow(t,3)),md(7*pow(v,6)+4*pow(v,3)*pow(t,3)+16*pow(t,6)));
 return md(pow(2,34)*pow(Y,17)*ph);
}
const qS34basis=Array.from({length:6},()=>Array(6).fill(0));
for(let j=0;j<6;j++){
 const t=conv(pw(sig,34,5),pw(xx,17-3*j,5),5);
 for(let k=j;k<6;k++)qS34basis[k][j]=t[k-j];
}
const qExpectedRaw={};
for(const zero of [false,true]){
 const src=zero?generators["0_1"].zero:generators["0_1"],bSrc=WITHB?(zero?Bgenerators["0_1"].zero:Bgenerators["0_1"]):null;
 const table={};
 for(let h=0;h<=MAXBLOCK;h++){
  const n=6*(h+1),g=src["gen"+n];
  const keys=new Set(g.flatMap(v=>Object.keys(v)));
  if(n>=12&&WITHB)for(const v of bSrc["gen"+n])for(const k of Object.keys(v))keys.add(k);
  for(const key of keys){
   const a=key.split(",").map(Number);
   const qg=a[0]+a[1]>6&&bSrc?bSrc["gen"+n]:g;
   const rhs=qg.map(v=>v[key]||0),s=elim(qS34basis,rhs);
   assert(s.rank===6&&!s.inconsistent,"old S34 exact triangular source");
   table[key]=s.solution;
  }
 }
 qExpectedRaw[String(zero)]=table;
}
function qCheckRaw(x,raw,zero){
 const X=pow(x,3),Y=md(X+1),x2=md(x*(X-8)*iv(md(4*Y))),pref=pow(2,34)*pow(Y,17);
 const basis=Array.from({length:6},(_,j)=>md(pref*pow(x2,17-3*j)));
 const table=qExpectedRaw[String(zero)];
 for(const[key,c]of Object.entries(table)){
  const target=md(-84*c.reduce((s,v,j)=>md(s+v*basis[j]),0));
  assert((raw[key]||0)===target,"raw C-factor/complete original endpoint mismatch "+key+" at x="+x);
 }
}
function qAtPoint(x,y,needJets=true){
 const tot=[{},{}],raw0=[{},{}];
 const accumulate=(target,P,Q,F,scalar)=>{
  for(const[k,v]of Object.entries(P))target[k]=md((target[k]||0)+scalar*F.mu(Q,v)[0]);
 };
 const F0=quad(1),P0=qCmPoints(x,y,F0),L0=needJets?qLogs(P0,F0):null;
 const val0=md(-84*qSdouble(x));
 for(const zero of [false,true]){
  const P=needJets?qExpHidden(L0,zero,F0):{"0,0,0":[1,0]};
  accumulate(raw0[Number(zero)],P,[val0,0],F0,1);
  accumulate(tot[Number(zero)],P,[val0,0],F0,iv(336));
  if(needJets)qCheckRaw(x,raw0[Number(zero)],zero);
 }
 for(let j=0;j<3;j++){
  const xj=md(pow(om,j)*x),rot=pow(om,j);
  const hpts=qCmPoints(xj,y,F0).map((P,i)=>qPointAdd(P,qHalfTorsion(F0)[i],F0));
  const hv=qHalfValue(xj),hl=needJets?qLogs(hpts,F0):null;
  for(const zero of [false,true]){
   const P=needJets?qExpHidden(hl,zero,F0):{"0,0,0":[1,0]};
   accumulate(tot[Number(zero)],P,[hv,0],F0,md(rot*iv(336)));
  }
  for(const e of quarterRoots){
   const F=quad(md(pow(e,3)+1)),ts=qQuarterTorsion(e,F);
   const ps=qCmPoints(xj,y,F).map((P,i)=>qPointAdd(P,ts[i],F));
   const Q=qQuarterValue(xj,y,e,F),l=needJets?qLogs(ps,F):null;
   for(const zero of [false,true]){
    const P=needJets?qExpHidden(l,zero,F):{"0,0,0":[1,0]};
    accumulate(tot[Number(zero)],P,Q,F,md(-2*rot*iv(336)));
   }
  }
 }
 assert(tot[0]["0,0,0"]===qXi(x)&&tot[1]["0,0,0"]===qXi(x),"whole unweighted R465 quarter identity at x="+x);
 return {main:tot[0],zero:tot[1]};
}
const sq3=Array.from({length:pp},(_,i)=>i).find(i=>md(i*i)===3);
assert(sq3!==undefined,"sqrt(3) in the auxiliary field");
const quarterRoots=[md(-1-sq3),md(-1+sq3)];
const pointList=[],Xused=new Set();
for(let x=1;x<pp&&pointList.length<23;x++){
 const X=pow(x,3);if(!X||Xused.has(X))continue;
 const y=Array.from({length:pp},(_,i)=>i).find(i=>md(i*i)===md(X+1));
 if(y===undefined||y===0)continue;
 try{qAtPoint(x,y,false);}catch(e){if(/point pole|zero denominator/.test(e.message))continue;throw e;}
 pointList.push({x,y,X});Xused.add(X);
}
assert(pointList.length===23,"twenty-three regular complete S136 coordinates");
console.error("R702: complete quarter source on 23 regular elliptic coordinates, total hidden degree "+CAP);
const pointData=[];
for(let i=0;i<pointList.length;i++){
 const P=pointList[i];console.error("R702: exact complete point "+(i+1)+"/23, x="+P.x);
 pointData.push(qAtPoint(P.x,P.y,true));
}
function makeQuarterGenerator(zero){
 const out={unweighted:pointList.map(P=>qXi(P.x))};
 for(let h=0;h<=MAXBLOCK;h++){
  const n=6+6*h;
  out["gen"+n]=pointData.map(P=>Object.fromEntries(Object.entries(P[zero?"zero":"main"])
   .filter(([k])=>k.split(",").map(Number).reduce((a,b)=>a+b,0)===n)));
 }
 return out;
}
const QY=makeQuarterGenerator(false);QY.zero=makeQuarterGenerator(true);
const S2values=pointList.map(P=>qSdouble(P.x)),newValues=pointList.map(P=>qNew(P.x));
const V136=pointList.map(P=>Array.from({length:23},(_,j)=>md(P.x*P.x*pow(P.X,j))));
assert(elim(V136).rank===23,"full 23-coordinate Vandermonde is nonsingular");

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
if(WITHB){DEBOUND=12;MGB=massGen(false,CAP-2);MGB0=massGen(true,CAP-2);DEBOUND=6;}
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
if(WITHB)for(let h=0;h<=BGMAX;h++)extcols.push(...dcols.map(P=>shifted(P,6*h)));
const highStart=extcols.length,highLabels=[];
if(NDEG){
 for(let i=1;i<=5;i++)for(let j=0;j<=NDEG-i;j++){
  const P={},g=NDEG-i-j,den=pow(iv(14),i+j);
  for(let a=0;a<=i;a++)for(let bb=0;bb<=j;bb++){
   const k=[a+bb,i+j-a-bb,g].join(",");
   const co=qprod(cb(i,a),pow(md(-1),a),cb(j,bb),pow(13,bb),den);
   P[k]=md((P[k]||0)+co);
  }
  extcols.push(Object.fromEntries(Object.entries(P).filter(v=>v[1])));
  highLabels.push({C:i,F:j,G:g,total_degree:NDEG});
 }
}
const degreeAt=j=>6+6*Math.floor(j/11);
const bDegreeAt=j=>12+6*Math.floor((j-gcount)/11);
const gen=(source,j,h)=>source["gen"+degreeAt(j)][h];
const readRow=(P,j,src,bsrc,h,eta)=>j<gcount
 ?evalRow(P,gen(src,j,h),gen(src.zero,j,h),eta)
 :j<highStart?evalB(P,bsrc["gen"+bDegreeAt(j)][h],bsrc.zero["gen"+bDegreeAt(j)][h],eta)
 :evalRow(P,bsrc["gen"+NDEG][h],bsrc.zero["gen"+NDEG][h],eta);

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
 M.push(extcols.map((P,j)=>j<gcount?evalRow(der2(P),MG[degreeAt(j)-2],MG0[degreeAt(j)-2],eta):j<highStart?evalB(der2(P),MGB[bDegreeAt(j)-2],MGB0[bDegreeAt(j)-2],eta):evalRow(der2(P),MGB[NDEG-2],MGB0[NDEG-2],eta)));
 old.push(evalRow(der2(Pold),MG[4],MG0[4],eta));labels.push({source:"normalized J2"});
 const target=[...Sjet,...Sjet,...Sjet,...native.slice(1),1];
 const rhs=target.map((x,i)=>md(x-old[i])),full=elim(M,rhs);
 const old19=[...Array.from({length:18},(_,i)=>i),30].map(i=>M[i].slice(0,19));
 if(TAU===2)assert(elim(old19).det===(eta===1?770:888),"same original nineteen actual columns");
 return {eta,matrix:M,old,target,rhs,labels,rank:full.rank,pivots:full.piv,consistent:!full.inconsistent,free_solution:full.solution};
}
const candidates=[1,-1].map(build);

const keep=[...Array.from({length:29},(_,i)=>i),30],newRows=[];
const target0=Sjet.map(x=>x),r693cols=[...Array.from({length:23},(_,j)=>j),25,26,36,37,47,48];
const output=[];
for(const c of candidates){
 const Qmatrix=pointList.map((_,k)=>extcols.map((P,j)=>readRow(P,j,QY,QY,k,c.eta)));
 const Qold=pointList.map((_,k)=>evalRow(Pold,QY.gen6[k],QY.zero.gen6[k],c.eta));
 const oldM=keep.map(i=>c.matrix[i]),oldRhs=keep.map(i=>md((i>=12?c.target[i]:0)-c.old[i]));
 // Whole-period identities fix the negative first-2Y block to omega^2 S2/2.
 // Prescribe all three source scalars, leaving only actual neutral-test columns.
 const fixedScalars=[1,md(om*om*iv(2)),1];
 const M=[...oldM,...Qmatrix];
 const rhs=[...oldRhs.map((v,k)=>md(v+(k<6?Sjet[k]:0))),
  ...Qold.map((v,k)=>md(fixedScalars[1]*S2values[k]+newValues[k]-v))];
 const ee=elim(M,rhs);
 let selectedCols=ee.piv,selectedRows=null,det=null,solution=null,scalars=null,verified=false,E1coords=null;
 if(!ee.inconsistent){
  const chosen=M.map(R=>selectedCols.map(j=>R[j]));
  selectedRows=elim(selectedCols.map((_,j)=>chosen.map(R=>R[j]))).piv;
  const B=selectedRows.map(i=>chosen[i]),rr=elim(B,selectedRows.map(i=>rhs[i]));
  det=rr.det;solution=Array(M[0].length).fill(0);
  selectedCols.forEach((j,k)=>{solution[j]=rr.solution[k];});
  verified=mm(M,solution.map(x=>[x])).every((R,j)=>R[0]===rhs[j]);
  assert(verified,"all original source/J2 rows and complete new quarter source");
  assert(ee.rank===45,"whole old thirty-source image plus fifteen new E2-trace-zero E4-vanishing coordinates");
  assert(selectedCols.every(j=>j<extcols.length),"the selected minor consists only of actual neutral test columns");
  const actualQ=mm(Qmatrix,solution.slice(0,extcols.length).map(x=>[x])).map((r,j)=>md(r[0]+Qold[j]));
  E1coords=elim(V136,actualQ).solution;scalars=fixedScalars;
  const wlast=md(c.old[29]+c.matrix[29].reduce((v,x,j)=>md(v+x*solution[j]),0));
  assert(wlast===c.target[29],"R693 complete halfperiod supplies the omitted W row");
  const wmass=md(evalRow(Pold,GW.gen6[0],GW.zero.gen6[0],c.eta)+extcols.reduce((v,P,j)=>
   md(v+solution[j]*readRow(P,j,GW,BGW,0,c.eta)),0));
  assert(wmass===0,"same endpoint and W mass exactly zero");
 }

 assert(!ee.inconsistent&&ee.rank===45,"paid R702 square is available");
 const Zmatrix=Array.from({length:5},(_,k)=>extcols.map((P,j)=>readRow(P,j,ZG,ZBG,k,c.eta)));
 const Zold=Array.from({length:5},(_,k)=>evalRow(Pold,ZG.gen6[k],ZG.zero.gen6[k],c.eta));
 const solvePaid=(target)=>{
  const chosen=selectedRows.map(i=>selectedCols.map(j=>M[i][j]));
  const e=elim(chosen,selectedRows.map(i=>target[i]));
  assert(e.rank===45&&!e.inconsistent,"same actual 45-column right inverse");
  const x=Array(extcols.length).fill(0);selectedCols.forEach((j,k)=>{x[j]=e.solution[k];});
  assert(mm(M,x.map(z=>[z])).every((v,i)=>v[0]===target[i]),"all 53 rows under changed exact target");
  return x;
 };
 const symRhs=rhs.map((x,i)=>md(x+(i>=6&&i<12?Sjet[i-6]:0)));
 const symSol=solvePaid(symRhs);
 const neutralRhs=Array(M.length).fill(0);neutralRhs[29]=1;
 const neutralSol=solvePaid(neutralRhs);
 const sourceOf=(x,affine)=>{
  const jets=mm(Zmatrix,x.map(v=>[v])).map((r,j)=>md(r[0]+(affine?Zold[j]:0)));
  const ec=elim(firstZBasis,jets);
  assert(ec.rank===5&&!ec.inconsistent,"complete first-Z type-five triangular source");
  return {jets_z5_11_17_23_29:jets,theta_coordinates:ec.solution,
   basis:"-sigma^34*x^(13-3j)*y, j=0,...,4; coefficient b^j",
   is_zero:jets.every(v=>v===0)};
 };
 const augmented=M.concat(Zmatrix),augSymRhs=symRhs.concat(Zold.map(v=>md(-v))),
  augNeutralRhs=neutralRhs.concat(Array(5).fill(0));
 const as=elim(augmented,augSymRhs),an=elim(augmented,augNeutralRhs);
 const moreCols=as.piv,moreChosen=augmented.map(r=>moreCols.map(j=>r[j]));
 const moreRows=elim(moreCols.map((_,j)=>moreChosen.map(r=>r[j]))).piv;
 const minor=elim(moreRows.map(i=>moreChosen[i]));
 const zLeftE=elim(augmented[0].map((_,j)=>augmented.map(R=>R[j]))),zLeft=[];
 const zPiv=new Set(zLeftE.piv);
 for(let f=0;f<augmented.length;f++)if(!zPiv.has(f)){
  const v=Array(augmented.length).fill(0);v[f]=1;
  zLeftE.piv.forEach((j,k)=>{v[j]=md(-zLeftE.reduced[k][f]);});
  assert(augmented[0].every((_,j)=>md(augmented.reduce((a,r,i)=>md(a+r[j]*v[i]),0))===0),
    "complete auxiliary augmented left relation");
  const pair=t=>md(t.reduce((a,x,i)=>md(a+x*v[i]),0));
  zLeft.push({row:v,symmetric_rhs:pair(augSymRhs),neutral_J_rhs:pair(augNeutralRhs)});
 }
 const firstZAnalysis={
  type5_dimension:5,original_rank:ee.rank,augmented_rank:as.rank,
  original_R702_source:sourceOf(solution,true),
  symmetric_three_S_source:sourceOf(symSol,true),
  neutral_J2_one_source:sourceOf(neutralSol,false),
  symmetric_selected_solution:selectedCols.map(j=>symSol[j]),
  neutral_selected_solution:selectedCols.map(j=>neutralSol[j]),
  zero_first_Z_while_preserving_all_sources:{symmetric_consistent:!as.inconsistent,
   neutral_J2_one_consistent:!an.inconsistent,selected_rows:moreRows,selected_columns:moreCols,
   selected_determinant:minor.det,auxiliary_left_relations:zLeft},
  scope:"All five coordinates are actual first-Z source rows. Auxiliary vanishing or incompatibility alone is not a characteristic-zero conclusion."};

 const tr=M[0].map((_,j)=>M.map(R=>R[j])),leftE=elim(tr),left=[];
 const leftSet=new Set(leftE.piv);
 for(let f=0;f<M.length;f++)if(!leftSet.has(f)){
  const v=Array(M.length).fill(0);v[f]=1;
  leftE.piv.forEach((j,k)=>{v[j]=md(-leftE.reduced[k][f]);});
  assert(tr.every(R=>md(R.reduce((s,x,j)=>s+x*v[j],0))===0),"entire auxiliary left relation");
  left.push({row:v,rhs_pairing:md(v.reduce((s,x,j)=>s+x*rhs[j],0))});
 }
 const rM=oldM.map((R,k)=>[...r693cols.map(j=>R[j]),k<6?md(-Sjet[k]):0]);
 const rsol=elim(rM,oldRhs);
 assert(rsol.rank===30&&!rsol.inconsistent,"same R693 thirty actual equations");
 const rx=Array(extcols.length).fill(0);r693cols.forEach((j,k)=>{rx[j]=rsol.solution[k];});
 const rq=mm(Qmatrix,rx.map(x=>[x])).map((r,j)=>md(r[0]+Qold[j]));
 const baseCoords=elim(V136,rq).solution;
 const baseLine=elim(pointList.map((_,j)=>[S2values[j],newValues[j]]),rq);
 output.push({eta:c.eta,rank:ee.rank,row_count:M.length,column_count:M[0].length,
  consistent:!ee.inconsistent,selected_rows:selectedRows,selected_columns:selectedCols,
  selected_determinant:det,verified_all_rows:verified,source_scalars:scalars,
  scalar_order:["frozen S0","e1-Y coefficient S(2z)","e1-Y coefficient Snew"],
  selected_solution:solution?selectedCols.map(j=>solution[j]):null,E1_polynomial_coordinates:E1coords,
  auxiliary_left_relations:left,
  original_R693:{determinant:rsol.det,frozen_c0:rsol.solution.at(-1),
    E1_polynomial_coordinates:baseCoords,already_in_two_arithmetic_lines:!baseLine.inconsistent},
  complete_source_verified:!!verified,first_Z_analysis:firstZAnalysis,
  scope:"the actual 45-column minor is an auxiliary nonvanishing certificate; the full 53-row lifting uses the independent complete half-period and E4-divisor proof"});
}
return {
 format:"R702 fixed complete first-2Y target omega^2 S2/2+Snew and all original R693 constraints",
 auxiliary:{p:pp,omega:om,tau:TAU,lambda:md((1-TAU)*iv(TAU)),kappa:0,u:0,b:1,Omega:1},
 max_block:MAXBLOCK,with_B:WITHB,B_G_blocks:BGMAX,complete_C_neutral_degree:NDEG,new_C_neutral_columns:highLabels,degree_blocks:Array.from({length:MAXBLOCK+1},(_,h)=>6+6*h),
 source_input_sha256:crypto.createHash("sha256").update(inputCode).digest("hex"),
 quarter_method:"R465 canonical full four-torsion formula; complete C-factor; 23 injective S136 evaluations",
 original_raw_endpoint_checked:true,unweighted_R465_identity_checked:true,
 coordinate_basis:"sigma^136*x^2*X^j, j=0,...,22",
 points:pointList,highest_original_total_moment:132+CAP,
 C_factor_coefficients_mod1009:bc,
 preservation:"same actual Pi4-zero G/B-G blocks plus, if requested, every C^i F^j G^(d-i-j), 1<=i<=5, d=12; all entire C moments and complete E inverses retained",
 entries:output,outputs_persisted:false
};
}
const report={
 format:"R715 complete first-Z source and detection of the actual neutral J2 direction",
 entries:TAUS.map(t=>{console.error("R702: full exact source algebra at tau="+t);return analyze(t);}),
 outputs_persisted:false
};
console.error("R702 completed in "+((Date.now()-start)/1000)+" seconds");
process.stdout.write(JSON.stringify(report)+"\n");
