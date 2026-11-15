#!/usr/bin/env node
"use strict";
/*
R690: actual q_N^sharp, complete native W marginal in S72(type 0).
Run publicly: node check-r690-native-w-source-of-adapted-cd-carry.js
No data files are read or written. R594's original standalone algorithm is
executed in a child process and its recomputable output stays in memory.
The full R679 nineteen-column adaptation is recomputed, not embedded.
Auxiliary arithmetic is exact in F1009 with omega=374. This is a fixed
rational-function certificate, never an ordinary-prime sample.
The actual characteristic-zero source uses the full lambda,kappa,kappa^N
matrix and the full C-unit subtraction stated in R679.
*/
const fs=require("fs"),path=require("path"),cp=require("child_process"),crypto=require("crypto");
const assert=(ok,msg)=>{if(!ok)throw Error(msg);};
const start=Date.now();
const inputPath=path.join(__dirname,"check-r594-two-source-six-carry-compensation.js");
const inputCode=fs.readFileSync(inputPath,"utf8");
console.error("R690: recomputing original R594 rows");
const all=JSON.parse(cp.execFileSync(process.execPath,[inputPath],{encoding:"utf8",maxBuffer:16*1024*1024}));
const pp=1009,om=374,MAXZ=72,CAP=12,SERIES=Math.ceil((MAXZ+CAP)/6);
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
const bc=conv(my,ss3).slice(0,3).map((a,i)=>md(a*pow(iv(ne(1,2)),6*i)));
assert(md(om*om+om+1)===0,"omega relation");
assert(bc[1]===rf("-1/90")&&bc[2]===rf("-19/3742200"),"entire C6/C12 retained");

const enc=(d,e,g,z)=>d+16*e+256*g+4096*z;
const dec=k=>[k%16,Math.floor(k/16)%16,Math.floor(k/256)%16,Math.floor(k/4096)];
const clean=P=>Array.from(P,([k,c])=>[...dec(k),c]).filter(x=>x[4]);
function mul(P,R,cap=CAP,zcap=30){
 const Z=new Map();
 for(const[a,b,c,z,v]of P)for(const[d,e,f,t,w]of R){
  if(a+b+c+d+e+f>cap||z+t>zcap)continue;
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
  const g=n-d-e;
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
function makeSource(i,endpoint=0,observation="S",zcap=30,cap=CAP){
 const ei=i?ne(-170,-291,9135):ne(-170,-117,9135),hh=i?ne(-5,-3):ne(-5,-9);
 const obs=observation==="W"?[...A,ne(3,6),4]:[...A,i?2:1,i?-1:2].map(md);
 let wr=[...D.map((x,j)=>md(x+5*ei*A[j])),md(-87*ei),md(-29*ei)];
 if(endpoint){const v=[...A.map(x=>5*x),i?-24:39,i?97:-92];wr=wr.map((x,j)=>md(x+hh*endpoint*v[j]*iv(315)));}
 const er=[...E,0,0],gr=[...G,0,0];
 const rows=Array.from({length:5},(_,j)=>[wr[j],er[j],gr[j]]);
 const fac=(base,c,j)=>factor(base,c,rows[j],obs[j],cap,zcap);
 let flat=add(mul(fac(1,f1,0),fac(2,ss2,1),cap,zcap),
  scale(mul(fac(3,f3,0),fac(0,theta,1),cap,zcap),pp-1));
 for(let j=2;j<5;j++)flat=mul(flat,fac(1,sig,j),cap,zcap);
 flat=scale(flat,iv(42));
 let BP=[[0,0,0,0,1]];
 for(let k=1;k<=2;k++)if(6*k<=cap)BP=add(BP,scale(linpow(lc,6*k),bc[k]));
 const full=mul(flat,BP,cap,zcap);
 const get=(deg,j)=>Object.fromEntries(full.filter(v=>v[0]+v[1]+v[2]===deg&&v[3]===6*j)
  .map(v=>[v.slice(0,3).join(","),md(v[4]*(i?-1:1))]));
 const J=Math.floor(zcap/6)+1;
 return {i,endpoint,observation,zcap,rows,obs,
  gen6:Array.from({length:J},(_,j)=>get(6,j)),
  gen12:Array.from({length:J},(_,j)=>get(12,j)),
  unweighted:Array.from({length:J},(_,j)=>(get(0,j)["0,0,0"]||0)),terms:full.length};
}
const generators={};
for(const [i,e] of [[0,0],[1,0],[0,1]]){
 console.error("R690: full adaptation generator "+i+"_"+e);
 generators[i+"_"+e]=makeSource(i,e);
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
const AP=all.matrix.Aplus.map(R=>R.map(ef)),AZ=all.matrix.Azero.map(R=>R.map(ef));
const BM=all.polynomial_right_inverse.B.map(M=>M.map(R=>R.map(ef)));
const A2=AP.map((R,i)=>R.map((x,j)=>md(x+2*AZ[i][j])));
const B2=BM[0].map((R,i)=>R.map((x,j)=>md(x+2*BM[1][i][j])));
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
const rat=ne(-789,526,1596);
const flatten=H=>{
 const T={};for(const[k,c]of Object.entries(H)){
  const a=k.split(",").map(Number),j=[a[0],0,a[1]+a[2]].join(",");
  T[j]=md((T[j]||0)+c*pow(md(-rat),a[1]));
 }return T;
};
const evalRow=(P,H,eta)=>md(moment(P,H)+moment(e0(P),H)+eta*moment(e0(P),flatten(H)));
function massGen(){
 const R=Array.from({length:3},(_,j)=>[D[j],E[j],G[j]]);
 let P=add(mul(factor(1,f1,R[0],0,10,0),factor(2,ss2,R[1],0,10,0),10,0),
  scale(mul(factor(3,f3,R[0],0,10,0),factor(0,theta,R[1],0,10,0),10,0),pp-1));
 P=scale(mul(P,factor(1,sig,R[2],0,10,0),10,0),iv(42));
 const BP=add([[0,0,0,0,1]],scale(linpow(lc,6),bc[1])),T=mul(P,BP,10,0);
 return Object.fromEntries([4,10].map(d=>[d,Object.fromEntries(T.filter(v=>v[0]+v[1]+v[2]===d).map(v=>[v.slice(0,3).join(","),v[4]]))]));
}
const MG=massGen();
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
const bp=all.matrix.target.map((x,i)=>md(ef(x)-ef(all.matrix.basePlus[i])-2*ef(all.matrix.baseZero[i])));
const xp=mm(B2,bp.map(x=>[x])).map(R=>R[0]);
const addPoly=(P,R,c=1)=>{
 const T={...P};for(const[k,v]of Object.entries(R))T[k]=md((T[k]||0)+c*v);
 return Object.fromEntries(Object.entries(T).filter(([k,v])=>v));
};
let Pold={...base};cols.forEach((P,j)=>{Pold=addPoly(Pold,P,xp[j]);});
const dcols=piv.map(j=>cols.reduce((P,C,i)=>addPoly(P,C,PI[i][j]),{}));
const extcols=[...dcols,...dcols.slice(0,8).map(P=>shifted(P,6))];
function build(eta){
 const M=[],old=[];
 for(const[i,e]of [[0,0],[1,0],[0,1]])for(let h=0;h<6;h++){
  const src=generators[i+"_"+e];
  M.push(extcols.map((P,j)=>evalRow(P,(j<11?src.gen6:src.gen12)[h],eta)));
  old.push(evalRow(Pold,src.gen6[h],eta));
 }
 M.push(extcols.map((P,j)=>evalRow(der2(P),MG[j<11?4:10],eta)));
 old.push(evalRow(der2(Pold),MG[4],eta));
 const target=[...Sjet,...Sjet,...Sjet,1],rhs=target.map((x,i)=>md(x-old[i]));
 const sol=elim(M,rhs);
 assert(sol.rank===19&&!sol.inconsistent,"actual nineteen adapted columns");
 assert(sol.det===(eta===1?770:888),"original R679 full nineteen determinant");
 assert(mm(M,sol.solution.map(x=>[x])).every((R,j)=>R[0]===rhs[j]),"all original nineteen equations");
 return {eta,matrix:M,old,target,rhs,solution:sol.solution,det:sol.det};
}
const adapted=[1,-1].map(build);
console.error("R690: native W generator through z^72, original total moment <=84");
const GW=makeSource(0,1,"W",MAXZ);
const basis72=makeBasis(72,12);
const thetaCoordinates=jet=>{
 const v=Array(jet.length).fill(0);
 for(let r=0;r<jet.length;r++)v[r]=md(jet[r]-v.slice(0,r).reduce((s,c,j)=>md(s+basis72[r][j]*c),0));
 return v;
};
const native=GW.unweighted;
assert(native[0]===0&&native[1]===ne(6,12),"native unweighted W = 6 delta T normalization");
const nativeCoords=thetaCoordinates(native);
const data=adapted.map(ad=>{
 const Wrows=[],oldW=[],jet=[];
 for(let h=0;h<13;h++){
  const row=extcols.map((P,j)=>evalRow(P,(j<11?GW.gen6:GW.gen12)[h],ad.eta));
  const old=evalRow(Pold,GW.gen6[h],ad.eta);
  Wrows.push(row);oldW.push(old);
  jet.push(md(old+row.reduce((s,c,j)=>md(s+c*ad.solution[j]),0)));
 }
 assert(jet[0]===0,"entire W mass equals the paid endpoint S mass");
 const coords=thetaCoordinates(jet),ratio=md(jet[1]*iv(native[1]));
 const residual=jet.map((x,j)=>md(x-ratio*native[j]));
 const first=residual.findIndex(x=>x!==0);
 const minors=jet.map((x,j)=>md(native[1]*x-jet[1]*native[j]));
 return {eta:ad.eta,adaptation_determinant:ad.det,
  adaptation_solution:ad.solution,
  actual_W_residue_jet:jet,actual_W_residue_theta_coordinates:coords,
  native_T_ratio_from_first_jet:ratio,all_native_T_minors:minors,
  first_off_line_jet_index:first,
  native_T_line:first<0,W_generator_rows:Wrows,W_old_affine_row:oldW,
  W_coefficients_general_b:"coordinate j is b^(j-1) times the displayed normalized rational-function coordinate; this auxiliary reduction is b=Omega=1"};
});
const result={
 format:"R690 native W marginal of the same actual degree-twelve adapted cd carry",
 auxiliary:{p:pp,omega:om,tau:2,lambda:md(-iv(2)),kappa:0,u:0,b:1,Omega:1},
 source:"q_cd from R671 j=N, with the full R679 actual nineteen inverse; native W, not the Z-scaled A_T",
 basis:"sigma_b^72 x_b^(36-3j), j=0,...,12; leading z^(6j)",
 max_original_total_moment:84,
 C_factor:{degree6:"-b/90",degree12:"-19b^2/3742200"},
 source_input_sha256:crypto.createHash("sha256").update(inputCode).digest("hex"),
 recomputation_input:"original standalone R594 algorithm, executed without writing its output",
 native_W_jets:native,native_W_theta_coordinates:nativeCoords,
 native_W_normalization:"6 delta T72",
 basis72,certificate:data,
 actual_lift:"Full characteristic-zero orthogonal moment generator followed by the SAME R679 full inverse. The auxiliary solution is not substituted into the actual p-adic test.",
 scope:"A nonzero native-T minor proves a fixed rational function is nonzero; apply only the already paid fixed-CM unit-density lemma. No central value is assigned to the other W components."
};
console.error("R690 completed in "+((Date.now()-start)/1000)+" seconds");
process.stdout.write(JSON.stringify(result,null,2)+"\n");
