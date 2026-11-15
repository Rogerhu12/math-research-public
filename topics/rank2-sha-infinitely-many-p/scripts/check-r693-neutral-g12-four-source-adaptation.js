#!/usr/bin/env node
"use strict";
/*
R693: actual neutral G6-power extension of the R679 test.
Run publicly: node check-r693-neutral-g12-four-source-adaptation.js --max-block=5 --taus=2,3
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
  if(a+b+d+e>6||a+b+c+d+e+f>cap||z+t>zcap)continue;
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
 const key=v.join(",")+":"+n;if(linearCache.has(key))return linearCache.get(key);
 const out=[];
 for(let d=0;d<=n;d++)for(let e=0;e<=n-d;e++){
  const g=n-d-e;if(d+e>6)continue;
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
function makePair(i,e,observation="S",zcap=30){
 const a=makeSource(i,e,observation,zcap,CAP,false);
 a.zero=makeSource(i,e,observation,zcap,CAP,true);
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
 return {rank,piv,det,solution:sol,inconsistent:rhs&&A.slice(rank).some(R=>R.at(-1)!==0)};
}
console.error("R693: full native W generator through z^72; original total moment <="+(72+CAP));
const GW=makePair(0,1,"W",MAXZ),native=GW.unweighted;
assert(native[0]===0&&native[1]===ne(6,12),"native W = 6 delta T");

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

function massGen(zero=false){
 const er=zero?E.map(()=>0):E,gr=zero?G.map((v,j)=>md(v-rat*E[j])):G;
 const Lc=zero?[lc[0],0,md(lc[2]-rat*lc[1])]:lc;
 const R=Array.from({length:3},(_,j)=>[D[j],er[j],gr[j]]),cap=CAP-2;
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
const extcols=Array.from({length:MAXBLOCK+1},(_,h)=>dcols.map(P=>shifted(P,6*h))).flat();
const degreeAt=j=>6+6*Math.floor(j/11);
const gen=(source,j,h)=>source["gen"+degreeAt(j)][h];
function build(eta){
 const M=[],old=[],labels=[];
 for(const[i,e]of [[0,0],[1,0],[0,1]])for(let h=0;h<6;h++){
  const src=generators[i+"_"+e];
  M.push(extcols.map((P,j)=>evalRow(P,gen(src,j,h),gen(src.zero,j,h),eta)));
  old.push(evalRow(Pold,src.gen6[h],src.zero.gen6[h],eta));
  labels.push({source:"S",branch:i,endpoint:e,jet:6*h});
 }
 // W mass is already fixed by the same endpoint S mass. Do not count it twice.
 for(let h=1;h<13;h++){
  M.push(extcols.map((P,j)=>evalRow(P,gen(GW,j,h),gen(GW.zero,j,h),eta)));
  old.push(evalRow(Pold,GW.gen6[h],GW.zero.gen6[h],eta));
  labels.push({source:"native 6delta T",jet:6*h});
 }
 M.push(extcols.map((P,j)=>evalRow(der2(P),MG[degreeAt(j)-2],MG0[degreeAt(j)-2],eta)));
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
   md(sum+solution[j]*evalRow(P,gen(GW,j,0),gen(GW.zero,j,0),c.eta)),0));
  assert(W0===0,"native W mass also satisfied exactly");
 }
 return {...c,selected_columns:selected,selected_determinant:selectedDet,
  full_solution:solution,verified_all31:verified,computed_source_rows:sourceRows};
});
const result={
 format:"R693 actual neutral G6-power extension: three S sources, native W=6deltaT, and normalized J2",
 auxiliary:{p:pp,omega:om,tau:TAU,lambda:md((1-TAU)*iv(TAU)),kappa:0,u:0,b:1,Omega:1},
 actual_columns:"eleven original Pi4-zero columns times G^(6h)/(b^h Omega^(6h)), h=0,...,max_block",
 max_block:MAXBLOCK,
 degree_blocks:Array.from({length:MAXBLOCK+1},(_,h)=>6+6*h),column_count:extcols.length,constraint_count:31,
 constraint_order:"frozen S0 six jets; frozen S1 six jets; cd endpoint S six jets; native W jets 6,...,72; normalized J2=1",
 original_kernel_indices:piv,common_selected_columns:common,
 highest_original_total_moment:72+CAP,
 C_factor_coefficients_mod1009:bc,
 C_factor_definition:"-y(s/delta)*sigma(s/delta)^3, all C^(6h) through CAP retained",
 exact_trim:"D+E degree <=6 only after directly generating BOTH full and C-zero sources; G degree and total degree kept through CAP",
 block_ranks:candidates.map(c=>({eta:c.eta,ranks:Array.from({length:MAXBLOCK+1},(_,h)=>elim(c.matrix.map(R=>R.slice(0,11*(h+1)))).rank)})),
 native_W_jets:native,
 source_input_sha256:crypto.createHash("sha256").update(inputCode).digest("hex"),
 certificate:data,
 actual_lift:"Only if a full fixed minor is nonzero: invert the corresponding FULL characteristic-zero 31x31 matrix at actual lambda,kappa,u and eta. The auxiliary solution is not the p-adic test.",
 arithmetic_scope:"All original Pi4 rows remain unchanged. New zero-mass corner claims are not inherited; all higher J_(2+6h) and positive pair masses must be retained. Z-scaled A_T is not identified with native W.",
 outputs_persisted:false
};
return result;
}
const report={
 format:"R693 actual G6-power family at fixed auxiliary tau values",
 max_block:MAXBLOCK, taus:TAUS,
 entries:TAUS.map(t=>{console.error("R693: exact row algebra at tau="+t);return analyze(t);}),
 outputs_persisted:false
};
console.error("R693 completed in "+((Date.now()-start)/1000)+" seconds");
process.stdout.write(JSON.stringify(report)+"\n");
