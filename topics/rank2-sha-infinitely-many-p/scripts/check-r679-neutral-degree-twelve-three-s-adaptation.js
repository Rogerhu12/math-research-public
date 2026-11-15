#!/usr/bin/env node
"use strict";
/*
R679 exact finite certificate, 2026-11-15.
Run: node check-r679-neutral-degree-twelve-three-s-adaptation.js [output.json]
Dependencies are the published R594, R674 and R675 JSON files in this directory.
All auxiliary arithmetic is EXACT in F_1009, omega=374. Rational coefficients
are reduced using BigInt. Products using Number are integers <1009^5<2^53.
This proves the characteristic-zero fixed determinants are nonzero. These
auxiliary solution vectors are NOT the actual p-adic test coefficients.
The actual test is defined by the full 19x19 inverse in R679, including
all lambda,kappa,kappa^N terms and the complete C-unit subtraction.
*/
const fs=require("fs"),path=require("path");
const read=name=>JSON.parse(fs.readFileSync(path.join(__dirname,name),"utf8"));
const assert=(ok,msg)=>{if(!ok)throw new Error(msg);};

const pp=1009,om=374,md=x=>((x%pp)+pp)%pp;
const pow=(a,n)=>{let x=1;for(;n;n=Math.floor(n/2),a=md(a*a))if(n%2)x=md(x*a);return x;};
const iv=a=>{a=md(a);if(!a)throw new Error("division by zero in the exact auxiliary field");return pow(a,pp-2);};
const rf=s=>{let a=String(s).split("/");return md(Number(BigInt(a[0])%BigInt(pp))*iv(Number(BigInt(a[1]||1)%BigInt(pp))));};
const ef=v=>md(rf(v[0])+om*rf(v[1]));
const ne=(a,b=0,d=1)=>md((a+om*b)*iv(d));
const fact=[1];for(let i=1;i<=48;i++)fact[i]=md(fact[i-1]*i);
const cb=(n,k)=>md(fact[n]*iv(md(fact[k]*fact[n-k])));
const conv=(a,b,N=7)=>Array.from({length:N+1},(_,n)=>md(a.reduce((s,v,k)=>k<=n?s+v*(b[n-k]||0):s,0)));
const pw=(a,k,N=7)=>{let v=[1];for(let i=0;i<k;i++)v=conv(v,a,N);return v;};
const xx=[1,ne(-1,0,7)];for(let n=2;n<=7;n++){let sum=0;for(let j=1;j<n;j++)sum=md(sum+xx[j]*xx[n-j]);xx[n]=md(sum*iv((6*n+1)*(n-1)));}
const log=[0,...xx.slice(1).map((a,i)=>md(-a*iv(6*(i+1)*(6*(i+1)-1))))],sig=[1];
for(let n=1;n<=7;n++){let sum=0;for(let j=1;j<=n;j++)sum=md(sum+j*log[j]*sig[n-j]);sig[n]=md(sum*iv(n));}
const my=xx.map((a,i)=>i?md(-(3*i-1)*a):1),ss2=pw(sig,2),ss3=pw(sig,3),ss6=pw(sig,6),
 f3=conv(my,ss6),f1=conv(xx,f3),theta=conv(xx,ss2),bc=conv(my,ss3).slice(0,3).map((a,i)=>md(a*pow(iv(ne(1,2)),6*i)));
const enc=(d,e,g,z)=>d+16*e+256*g+4096*z,dec=k=>[k%16,Math.floor(k/16)%16,Math.floor(k/256)%16,Math.floor(k/4096)];
const clean=P=>Array.from(P,([k,c])=>[...dec(k),c]).filter(x=>x[4]);
function mul(P,R,cap=12,zcap=30){
 const Z=new Map();
 for(const[a,b,c,z,v]of P)for(const[d,e,f,t,w]of R){
  if(a+b+c+d+e+f>cap||z+t>zcap)continue;
  const k=enc(a+d,b+e,c+f,z+t);
  Z.set(k,md((Z.get(k)||0)+v*w));
 }
 return clean(Z);
}
const scale=(P,a)=>P.map(([d,e,g,z,c])=>[d,e,g,z,md(c*a)]).filter(v=>v[4]);
function add(P,R){const Q=new Map(P.map(([d,e,g,z,c])=>[enc(d,e,g,z),c]));for(const[d,e,g,z,c]of R){const k=enc(d,e,g,z);Q.set(k,md((Q.get(k)||0)+c));}return clean(Q);}
function linpow(v,n){const out=[];for(let d=0;d<=n;d++)for(let e=0;e<=n-d;e++){const g=n-d-e;const c=md(fact[n]*iv(md(fact[d]*fact[e]*fact[g]))*pow(v[0],d)*pow(v[1],e)*pow(v[2],g));if(c)out.push([d,e,g,0,c]);}return out;}
function factor(base,coeff,row,obs,cap=12,zcap=30){
 let out=[];for(let h=0;h<coeff.length;h++){const n=base+6*h;if(n>cap+zcap)break;
 for(let r=0;r<=Math.min(cap,n);r++){const z=n-r;if(z>zcap)continue;
 const scale=md(coeff[h]*cb(n,r)*pow(obs,z));
 for(const[d,e,g,,v]of linpow(row,r)){const c=md(v*scale);if(c)out.push([d,e,g,z,c]);}
 }}return out;
}
function makeSource(i,endpoint=0,cap=12){
 // The rows below are the original complete flat-five frame.
 const A=[ne(-1,1,2),ne(4,3,2),ne(2,4)];
 // correct first A=(-2+omega)/2
 A[0]=ne(-2,1,2);
 const D=[ne(-19,19,174),ne(31,-37,58),ne(-43,-21,29)];
 const E=[ne(-133,133,429),ne(217,-259,143),ne(-602,-294,143)];
 const G=[ne(-5843,-3715,858),ne(-1593,0,286)+ne(0,-123,22),ne(1324,-266,143)].map(md);
 const ei=i?ne(-170,-291,9135):ne(-170,-117,9135),hh=i?ne(-5,-3):ne(-5,-9);
 const obs=[...A,i?2:1,i?-1:2].map(md);
 let wr=[...D.map((x,j)=>md(x+5*ei*A[j])),md(-87*ei),md(-29*ei)];
 if(endpoint){const v=[...A.map(x=>5*x),i?-24:39,i?97:-92];wr=wr.map((x,j)=>md(x+hh*endpoint*v[j]*iv(315)));}
 const er=[...E,0,0],gr=[...G,0,0];
 const rows=Array.from({length:5},(_,j)=>[wr[j],er[j],gr[j]]);
 let flat=add(mul(factor(1,f1,rows[0],obs[0],cap),factor(2,ss2,rows[1],obs[1],cap),cap),scale(mul(factor(3,f3,rows[0],obs[0],cap),factor(0,theta,rows[1],obs[1],cap),cap),pp-1));
 for(let j=2;j<5;j++)flat=mul(flat,factor(1,sig,rows[j],obs[j],cap),cap);
 flat=scale(flat,iv(42));
 const lc=[ne(-1),ne(1596,0,143),ne(-789,526,143)];
 let BP=[[0,0,0,0,1]];
 for(let k=1;k<=2;k++)if(6*k<=cap)BP=add(BP,scale(linpow(lc,6*k),bc[k]));
 const full=mul(flat,BP,cap);
 const get=(deg,j)=>Object.fromEntries(full.filter(v=>v[0]+v[1]+v[2]===deg&&v[3]===6*j).map(v=>[v.slice(0,3).join(","),md(v[4]*(i?-1:1))]));
 return {i,endpoint,rows,obs,lc,bc,gen6:Array.from({length:6},(_,j)=>get(6,j)),gen12:Array.from({length:6},(_,j)=>get(12,j)),terms:full.length};
}

const generators={};
for(const i of [0,1])for(const e of [0,1])generators[i+"_"+e]=makeSource(i,e);

function mm(A,B){return A.map(R=>B[0].map((_,j)=>md(R.reduce((s,c,k)=>md(s+c*B[k][j]),0))));}
function elim(M,rhs=null){const A=M.map((R,i)=>rhs?[...R,rhs[i]]:R.slice());let rank=0,piv=[],det=1;
 for(let c=0;c<M[0].length&&rank<M.length;c++){let r=rank;while(r<A.length&&!A[r][c])r++;if(r===A.length)continue;if(r!==rank){[A[r],A[rank]]=[A[rank],A[r]];det=md(-det);}const d=A[rank][c];det=md(det*d);A[rank]=A[rank].map(x=>md(x*iv(d)));
 for(let j=0;j<A.length;j++)if(j!==rank&&A[j][c]){const z=A[j][c];A[j]=A[j].map((x,k)=>md(x-z*A[rank][k]));}
 piv.push(c);rank++;
 }
 const sol=rhs?Array(M[0].length).fill(0):null;if(rhs)for(let j=0;j<rank;j++)sol[piv[j]]=A[j].at(-1);
 return {rank,piv,det,A,solution:sol,inconsistent:rhs&&A.slice(rank).some(R=>R.at(-1)!==0)};
}
const all=read("check-r594-two-source-six-carry-compensation.json"),m674=read("check-r674-double-s-arithmetic-adaptation.json");
const AP=all.matrix.Aplus.map(R=>R.map(ef)),AZ=all.matrix.Azero.map(R=>R.map(ef)),BM=all.polynomial_right_inverse.B.map(M=>M.map(R=>R.map(ef))),
A2=AP.map((R,i)=>R.map((x,j)=>md(x+2*AZ[i][j]))),B2=BM[0].map((R,i)=>R.map((x,j)=>md(x+2*BM[1][i][j]))),BA=mm(B2,A2),PI=BA.map((R,i)=>R.map((x,j)=>md((i===j?1:0)-x)));
const piv=m674.pivots,cols=all.matrix.polys.map(P=>Object.fromEntries(Object.entries(P).map(([k,v])=>[k,ef(v)]))),base=Object.fromEntries(Object.entries(all.matrix.base).map(([k,v])=>[k,ef(v)]));
const readP=P=>P;
const e0=P=>Object.fromEntries(Object.entries(P).filter(([k,v])=>+k.split(",")[1]===0));
const shifted=(P,n)=>Object.fromEntries(Object.entries(P).map(([k,v])=>{let a=k.split(",").map(Number);a[2]+=n;return[a.join(","),v];}));
const der2=P=>Object.fromEntries(Object.entries(P).filter(([k,v])=>+k.split(",")[0]>=2).map(([k,v])=>{let a=k.split(",").map(Number),c=md(v*a[0]*(a[0]-1));a[0]-=2;return[a.join(","),c];}));
const moment=(P,G)=>Object.entries(P).reduce((s,[k,c])=>{const a=k.split(",").map(Number);return md(s+c*(G[k]||0)*md(fact[a[0]]*fact[a[1]]*fact[a[2]]));},0);
const rat=ne(-789,526,1596);
const flatten=G=>{const T={};for(const[k,c]of Object.entries(G)){const a=k.split(",").map(Number),j=[a[0],0,a[1]+a[2]].join(",");T[j]=md((T[j]||0)+c*pow(md(-rat),a[1]));}return T;};
const evalRow=(P,G,eta)=>md(moment(P,G)+moment(e0(P),G)+eta*moment(e0(P),flatten(G)));
function massGen(){
 const D=[ne(-19,19,174),ne(31,-37,58),ne(-43,-21,29)];
 const E=[ne(-133,133,429),ne(217,-259,143),ne(-602,-294,143)];
 const G=[ne(-5843,-3715,858),md(ne(-1593,0,286)+ne(0,-123,22)),ne(1324,-266,143)];
 const R=Array.from({length:3},(_,j)=>[D[j],E[j],G[j]]);
 let P=add(mul(factor(1,f1,R[0],0,10,0),factor(2,ss2,R[1],0,10,0),10,0),
 scale(mul(factor(3,f3,R[0],0,10,0),factor(0,theta,R[1],0,10,0),10,0),pp-1));
 P=scale(mul(P,factor(1,sig,R[2],0,10,0),10,0),iv(42));
 const BP=add([[0,0,0,0,1]],scale(linpow([ne(-1),ne(1596,0,143),ne(-789,526,143)],6),bc[1]));
 const T=mul(P,BP,10,0);
 return Object.fromEntries([4,10].map(d=>[d,Object.fromEntries(T.filter(v=>v[0]+v[1]+v[2]===d).map(v=>[v.slice(0,3).join(","),v[4]]))]));
}
const MG=massGen(),sjet=m674.S_jets.map(ef),
bp=all.matrix.target.map((x,i)=>md(ef(x)-ef(all.matrix.basePlus[i])-2*ef(all.matrix.baseZero[i]))),
xp=mm(B2,bp.map(x=>[x])).map(R=>R[0]);
const addPoly=(P,R,c=1)=>{const T={...P};for(const[k,v]of Object.entries(R))T[k]=md((T[k]||0)+c*v);return Object.fromEntries(Object.entries(T).filter(([k,v])=>v));};
let Pold={...base};cols.forEach((P,j)=>{Pold=addPoly(Pold,P,xp[j]);});
const dcols=piv.map(j=>cols.reduce((P,C,i)=>addPoly(P,C,PI[i][j]),{}));
const build=eta=>{
 const mat=[],old=[],rowlabels=[];
 for(const [e,i]of [[0,0],[0,1],[1,0]])for(let h=0;h<6;h++){
  const src=generators[i+"_"+e],g6=src.gen6[h],g12=src.gen12[h];
  mat.push([...dcols.map(P=>evalRow(P,g6,eta)),...dcols.map(P=>evalRow(shifted(P,6),g12,eta))]);
  old.push(evalRow(Pold,g6,eta));rowlabels.push([e,i,h]);
 }
 mat.push([...dcols.map(P=>evalRow(der2(P),MG[4],eta)),...dcols.map(P=>evalRow(der2(shifted(P,6)),MG[10],eta))]);
 old.push(evalRow(der2(Pold),MG[4],eta));rowlabels.push("normalized J2");
 const target=[...sjet,...sjet,...sjet,1],rhs=target.map((x,i)=>md(x-old[i]));
 const sol=elim(mat,rhs),sub=sol.piv.length===19?mat.map(R=>sol.piv.map(j=>R[j])):null;
 const det=sub?elim(sub).det:null;
 const checks=sol.solution?mm(mat,sol.solution.map(x=>[x])).every((R,i)=>R[0]===rhs[i]):false;
 return {eta,rowlabels,rank:sol.rank,pivots:sol.piv,det,consistent:!sol.inconsistent,solution:sol.solution,verified:checks,matrix:mat,rhs,target,old};
};

assert(md(om*om+om+1)===0,"omega relation");
assert(bc[1]===rf("-1/90")&&bc[2]===rf("-19/3742200"),"complete C moments");
const expectedDet={"1":770,"-1":888};
const expectedSolution={
 "1":[497,449,924,374,55,273,492,763,276,626,9,297,511,462,321,222,124,82,716],
 "-1":[137,910,330,579,327,32,750,348,389,148,463,383,894,413,247,538,83,292,692]
};
let oldMatrixChecks=0,newEquations=0;
const certificate=[1,-1].map(eta=>{
 const z=build(eta),square=z.matrix.map(R=>R.slice(0,19)),s=elim(square,z.rhs);
 assert(s.rank===19&&!s.inconsistent,"actual selected auxiliary square is invertible");
 assert(s.det===expectedDet[String(eta)],"nineteen determinant");
 assert(s.solution.every((v,j)=>v===expectedSolution[String(eta)][j]),"exact solution");
 assert(mm(square,s.solution.map(v=>[v])).every((R,j)=>R[0]===z.rhs[j]),"all nineteen equations");
 newEquations+=19;
 const old=m674.auxiliary.eta[String(eta)].matrix;
 for(let r=0;r<12;r++)for(let j=0;j<11;j++){
  assert(square[r][j]===Number(old[r][j]),"original frozen source matrix");
  oldMatrixChecks++;
 }
 for(let j=0;j<11;j++){
  assert(square[18][j]===Number(old[12][j]),"original normalized J2 row");
  oldMatrixChecks++;
 }
 return {eta,rowlabels:z.rowlabels,matrix:square,det:s.det,rank:s.rank,
   target:z.target,old:z.old,rhs:z.rhs,solution:s.solution,
   verified_equations:19};
});
const oldEndpoint=read("check-r675-original-cd-endpoint-six-source.json");
let endpointChecks=0;
for(let i=0;i<2;i++)for(let h=0;h<6;h++){
 const actual=generators[i+"_1"].gen6[h],expected=oldEndpoint.generators.full.sources[i].gen[h];
 for(const k of new Set([...Object.keys(actual),...Object.keys(expected)])){
  const v=expected[k]?md((i?-1:1)*ef(expected[k])):0;
  assert((actual[k]||0)===v,"original complete endpoint generator");
  endpointChecks++;
 }
}
const result={
 format:"R679 exact nineteen-column neutral degree-twelve adaptation",
 date:"2026-11-15",
 original_dependencies:[
 "check-r594-two-source-six-carry-compensation.json",
 "check-r674-double-s-arithmetic-adaptation.json",
 "check-r675-original-cd-endpoint-six-source.json"
 ],
 auxiliary:{p:pp,omega:om,tau:2,lambda:md(-iv(2)),kappa:0,u:0,b:1,Omega:1},
 columns:{old_kernel_indices:piv,old_kernel_count:11,
  G6_kernel_indices:piv.slice(0,8),G6_kernel_count:8,
  G6_multiplier:"physical G^6/(b*Omega^6)"},
 C_factor_coefficients:{constant:"1",degree6:"-b/90",degree12:"-19*b^2/3742200"},
 S_target_jets:sjet,
 complete_source_generators:generators,
 normalized_J2_generators:MG,
 certificate,
 checks:{original_matrix_entries:oldMatrixChecks,original_endpoint_entries:endpointChecks,new_equations:newEquations},
 actual_lift:{
 matrix:"The FULL characteristic-zero moment map in R679, not this residue matrix.",
 right_hand_side:"(S,S,S,1) minus the FULL old-test rows.",
 solution:"M_sharp(N,p)^(-1) times that full right-hand side.",
 good_primes:"Fixed CM polynomial-unit density lemma; both eta determinants nonzero; uniform all N in 4Z.",
 preservation:"Entire original pi4 pushforward; not all old local degree-six mass constraints.",
 retained:"Both C6/C12; new J8; degree<=12 depth terms; all actual T shallow/exterior and Mellin mass."
 }
};
const output=JSON.stringify(result,null,2)+"\n";
if(process.argv[2])fs.writeFileSync(process.argv[2],output);else process.stdout.write(output);
