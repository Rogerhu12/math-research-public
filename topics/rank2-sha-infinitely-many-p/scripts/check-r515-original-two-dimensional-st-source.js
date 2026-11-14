#!/usr/bin/env node
/* R515 exact BigInt rational/CM certificate. */
function certifyR515(){
"use strict";
const ck=(x,m)=>{if(!x)throw Error(m);};
const abs=x=>x<0n?-x:x,gcd=(x,y)=>{x=abs(x);y=abs(y);while(y)[x,y]=[y,x%y];return x;};
const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);ck(d!==0n,"zero denominator");if(d<0n){n=-n;d=-d;}let g=gcd(n,d);return[n/g,d/g];};
const qa=(x,y)=>Q(x[0]*y[1]+y[0]*x[1],x[1]*y[1]),qn=x=>[-x[0],x[1]],
qm=(x,y)=>Q(x[0]*y[0],x[1]*y[1]),qi=x=>Q(x[1],x[0]),
qs=x=>x[1]===1n?String(x[0]):String(x[0])+"/"+x[1];
const E=(a,b=0,d=1)=>[Q(a,d),Q(b,d)], ea=(x,y)=>[qa(x[0],y[0]),qa(x[1],y[1])],
en=x=>[qn(x[0]),qn(x[1])],es=(x,y)=>ea(x,en(y)),
em=(x,y)=>[qa(qm(x[0],y[0]),qn(qm(x[1],y[1]))),
qa(qa(qm(x[0],y[1]),qm(x[1],y[0])),qn(qm(x[1],y[1])))],
ec=x=>[qa(x[0],qn(x[1])),qn(x[1])],
eq=(x,y)=>x[0][0]===y[0][0]&&x[0][1]===y[0][1]&&x[1][0]===y[1][0]&&x[1][1]===y[1][1],
esc=(x,a,b=1)=>em(x,E(a,0,b)),ez=x=>eq(x,E(0)),
ei=x=>{let n=em(x,ec(x));ck(n[1][0]===0n,"norm rational");return[ qm(ec(x)[0],qi(n[0])),qm(ec(x)[1],qi(n[0])) ];},
out=x=>x.map(qs);
const he=(x,y)=>x.reduce((a,t,i)=>ea(a,em(t,ec(y[i]))),E(0));
const va=(x,y)=>x.map((t,i)=>ea(t,y[i])),vs=(x,y)=>x.map((t,i)=>es(t,y[i])),
vm=(x,c)=>x.map(t=>em(t,c));
const mm=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,t,k)=>ea(s,em(t,B[k][j])),E(0))));
const ident=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>E(i===j?1:0)));
function inverse(A){let M=A.map(row=>row.map(x=>x)),B=ident(A.length),det=E(1);
 for(let k=0;k<M.length;k++){let p=k;while(p<M.length&&ez(M[p][k]))p++;ck(p<M.length,"singular");
  if(p!==k){[M[p],M[k]]=[M[k],M[p]];[B[p],B[k]]=[B[k],B[p]];det=en(det);}
  const pivot=M[k][k];det=em(det,pivot);const inv=ei(pivot);M[k]=vm(M[k],inv);B[k]=vm(B[k],inv);
  for(let i=0;i<M.length;i++)if(i!==k&&!ez(M[i][k])){const f=M[i][k];M[i]=vs(M[i],vm(M[k],f));B[i]=vs(B[i],vm(B[k],f));}
 } return {inverse:B,det}; }
const om=E(0,1),om2=E(-1,-1),del=E(1,2),ga=E(3,1),gb=E(2,-1),alpha=E(3,2);
const Z=[del,E(2,4),ga,E(0),E(1),E(2)],
 R=[ga,E(2,4),E(6,3),E(0),E(-1,1),E(4)],
 X=[E(0),E(0),E(0),E(1),E(0),E(0)],
 K=[E(163,83),E(-7,-98),E(-46,107),E(0),E(276,170),E(42,-63)],
 Q1=[E(-6,-9,7),E(1),E(0),E(0),E(4,-1,7),E(11,13,7)],
 Q2=[E(8,5,7),E(0),E(1),E(0),E(0),E(0)];
Q2[4]=E(4,6,7);Q2[5]=E(-10,6,7);
const D=vm(vs(vm(Z,E(65)),vm(R,E(34,1))),E(1,0,2)),
 W2=va(R,vm(X,alpha)),Qc=vs(vm(R,E(7)),vm(X,em(E(65),alpha))),
 Y=va(Z,vm(X,gb)),B15=vm(va(R,vm(Z,om2)),E(1,0,2)),
 W=[del,E(2,4),ga,gb,E(3,6),E(4)],
 Wp=[E(4,4),E(2,4),E(4,4),E(0),E(4,2),E(4)];

const cc=E(17,14),cW=E(17,-3),vW=E(33,17);
const Aodd=vs(vm(Y,E(15)),vm(B15,cc)),
 Eaxis=vs(vm(X,E(263)),vm(Aodd,ga)),
 P=vs(Aodd,vm(X,em(E(15),gb))),
 L=vs(vm(Y,E(36)),vm(W2,cW));
const F=[W2,L,Eaxis,K,Q1,Q2],{inverse:Finv,det}=inverse(F),G=F.map(row=>F.map(col=>he(row,col)));
for(let i=0;i<4;i++)for(let j=0;j<6;j++)ck(eq(G[i][j],E(i===j?[72,18936,41554,113918][i]:0)),"complete four-axis Gram");
ck(eq(det,E(308164464)),"full six-input determinant");
ck(eq(he(B15,B15),E(15))&&eq(he(Aodd,Aodd),E(3945))&&eq(he(Eaxis,Eaxis),E(41554)),"new three-axis norms");
ck(eq(he(B15,Aodd),E(0))&&eq(he(B15,Eaxis),E(0))&&eq(he(Aodd,Eaxis),E(0)),"new three-axis cross terms");
ck(eq(he(P,P),E(2370))&&eq(he(P,B15),E(0)),"intermediate two-dimensional five-sigma frame");
ck(va(vm(B15,cc),Aodd).every((x,i)=>eq(x,esc(Y[i],15))),"Y plane expression");
ck(vs(vm(B15,vW),vm(Aodd,om2)).every((x,i)=>eq(x,esc(W2[i],15))),"T plane expression");
const old=mm([W],Finv)[0],ys=mm([Y],Finv)[0],b=mm([B15],Finv)[0];
const expectOld=[E(22,-7,36),E(259,161,9468),E(-233,-209,20777),E(1,1,79),E(0),E(0)];
ck(old.every((x,i)=>eq(x,expectOld[i])),"old W with both omitted coordinates retained");
ck(ys.every((x,i)=>eq(x,[E(17,-3,36),E(1,0,36),E(0),E(0),E(0),E(0)][i])),"Y in the true plane");
ck(b.every((x,i)=>eq(x,[E(16,-17,72),E(-1,-1,72),E(0),E(0),E(0),E(0)][i])),"B in the true plane");
const ly=vs(vm(B15,E(34)),vm(Y,ec(cc)));
ck(eq(he(ly,ly),E(8942))&&eq(he(ly,Y),E(0)),"Y companion degree 8942");
const a1=E(54),a2=em(del,em(ga,em(ga,ga)));
ck(eq(ea(em(a1,ec(a1)),em(a2,ec(a2))),E(3945)),"odd3945 absolute square anchor");
ck(eq(em(a2,ec(a2)),E(1029)),"second anchor norm");
const permN=18936,kN=1+3*permN/4,half=permN/2,quarter=permN/4;
for(let j=0;j<permN;j++){
 const col=new Map(),add=(i,x)=>col.set(i,(col.get(i)||0)+x);
 add((j+quarter*(j%4))%permN,1);
 if(j%2===0){add(j,-1);add((j+half)%permN,-1);}
 const p=(kN*j+half)%permN,sg=j%2===0?-1:1;
 for(const[i,x]of col)ck(x===(i===p?sg:0),"whole 18936 quarter kernel");
 ck((kN*p+half)%permN===j&&(p+j)%2===0,"whole 18936 square");
}
ck(kN===14203&&kN%16===11&&permN%16===8,"complete dyadic ratio");
ck(kN%9===1&&permN%9===0&&kN%263===1&&permN%263===0,"complete odd ratio");
const Ldiff=va(L,vm(W2,cW));
ck(Ldiff.every((x,i)=>eq(x,esc(Y[i],36))),"quarter-period row");
const periods=vm(Y,E(9)),periodNorm=he(periods,periods),refQuarter=vm(W2,esc(en(cW),1,4)),alternating=he(periods,refQuarter);
ck(eq(periodNorm,E(2754))&&alternating[1][0]===0n,"complete absolute 18936 phase");
const ptoA=[[E(1),em(E(15),gb)],[en(ga),E(158)]];
ck(eq(es(em(ptoA[0][0],ptoA[1][1]),em(ptoA[0][1],ptoA[1][0])),E(263)),"full P/x change");
const u=em(ec(cc),E(1,0,27)),ZJtoBP=[[u,E(1,0,27)],[E(158,0,27),en(esc(cc,1,27))]];
ck(eq(es(em(ZJtoBP[0][0],ZJtoBP[1][1]),em(ZJtoBP[0][1],ZJtoBP[1][0])),E(-5,0,9)),"full Z/J change");
const Tc=vs(vm(Z,ga),vm(X,E(27))),tc=mm([Tc],Finv)[0];
ck(tc.every((x,i)=>eq(x,[E(37,45,36),E(-605,-876,9468),E(-34,0,263),E(0),E(0),E(0)][i])),"original positive companion keeps its E term");
return {
 Tc_original:tc.map(out),
 coordinates:"(xi1,xi2,xi3,x,c,d0)",B15:B15.map(out),P2370:P.map(out),A3945:Aodd.map(out),E41554:Eaxis.map(out),
 W2:W2.map(out),L18936:L.map(out),Y_companion_8942:ly.map(out),
 frame:F.map(row=>row.map(out)),inverse:Finv.map(row=>row.map(out)),Gram:G.map(row=>row.map(out)),determinant:out(det),
 old_W:old.map(out),Y:ys.map(out),B:b.map(out),
 odd3945_anchor:[out(a1),out(a2)],anchor_norms:[2916,1029],psi_square:1,
 whole_P_core:"chi65",whole_A_core:"psi",whole_E_core:"epsilon=-chi65*psi",
 whole_L_center:[kN,permN],whole_L_core:"chi65*psi*(1/4 sum E4 -1/2 sum E2)",whole_L_square:1,
 quarter_period_row:periods.map(out),quarter_period_norm:out(periodNorm),quarter_alternating_pair:out(alternating),
 two_state_rectangle:"(-1)^(c+e)*(chi65*psi)^(b+c)*lambda^(a+b+c+e+2t); state i+a+b mod2",
 four_companion_common_core:"(chi65*psi)^n lambda^(4n)",
 common_2D_source:"-1/84 product_{j=1}^6 sigma(B_j b + A_j a)",
 residual_5_source_degrees:[15,2370],independent_sigma_factor:"sigma(15*bar(gamma)*a)",
 two_arithmetic_rows:{Y:"(A+(17+14omega)B)/15",W2:"((33+17omega)B-omega^2 A)/15"},
 primitive_carry:"P,c unit and A=P+c deep iff A deep,E unit; normalized A/kap carry =lambda*(psi+chi65*lambda) times the same two-dimensional source",
 warning:"Old W has nonzero E and K coefficients. Neither its tube nor the T/U geometry is silently pushed to the two-dimensional source."
 };
}

if(typeof module!=="undefined"){
 module.exports={certifyR515};
 if(require.main===module){
  const report=certifyR515();
  require("fs").writeFileSync(__filename.replace(/\.js$/,".json"),
   JSON.stringify(report,null,2)+"\n");
  console.log("R515 full six-input frame, whole 18936 kernel, two-dimensional source and retained boundary data verified.");
 }
}
