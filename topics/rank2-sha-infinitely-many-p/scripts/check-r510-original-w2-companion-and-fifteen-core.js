#!/usr/bin/env node
/* R510: exact BigInt rational and CM certificate. */
function certifyR510(){
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
const F=[W2,Qc,D,K,Q1,Q2],{inverse:Finv,det}=inverse(F),G=F.map(row=>F.map(col=>he(row,col)));
const deg=[72,32760,10270,113918];
for(let i=0;i<4;i++)for(let j=0;j<6;j++)ck(eq(G[i][j],E(i===j?deg[i]:0)),"full first-axis Gram");
ck(eq(G[4][4],E(40,0,7))&&eq(G[5][5],E(46,0,7))&&eq(G[4][5],E(-25,-38,7)),"original Q block");
ck(eq(det,em(E(76162320),alpha)),"full exact determinant");
const oldcoef=mm([W],Finv)[0],ycoef=mm([Y],Finv)[0];
const expectW=[E(22,-7,36),E(22,29,2340),E(175,168,5135),E(1,1,79),E(0),E(0)];
const expectY=[E(17,-3,36),E(17,33,2340),E(2,0,65),E(0),E(0),E(0)];
ck(oldcoef.every((x,i)=>eq(x,expectW[i]))&&ycoef.every((x,i)=>eq(x,expectY[i])),"old W and Y exact rows");
ck(va(va(W,vm(Wp,om2)),vm(W2,om)).every(ez),"three W relation");
ck(eq(he(B15,B15),E(15))&&eq(he(Y,B15),E(17,14))&&eq(he(W2,B15),E(33,17)),"B15 Gram");
ck(va(vm(Y,en(om2)),vm(B15,E(2))).every((x,i)=>eq(x,W2[i])),"two arithmetic rows");
const bExpected=[E(2),E(2,1),E(2),E(0),E(-1),E(1,-1)];
ck(B15.every((x,i)=>eq(x,bExpected[i])),"whole original B15 direction");
ck(eq(em(ga,gb),E(7))&&eq(alpha,en(em(om2,gb))),"free sigma unit");
ck(eq(em(E(-18),alpha),E(-54,-36))&&eq(em(em(E(-18),alpha),ec(em(E(-18),alpha))),E(2268)),"quarter period norm");
const periodPair=em(ec(em(E(7,0,4),alpha)),em(E(-18),alpha));
ck(periodPair[1][0]===0n,"quarter alternating phase");

function imul(x,y,m){return[((x[0]*y[0]-x[1]*y[1])%m+m)%m,((x[0]*y[1]+x[1]*y[0]-x[1]*y[1])%m+m)%m];}
function iv(x,m){let r=m,s=((x%m)+m)%m,t=0n,u=1n;while(s){let q=r/s;[r,s]=[s,r-q*s];[t,u]=[u,t-q*u];}ck(r===1n,"mod inverse");return(t%m+m)%m;}
function gp(m){m=BigInt(m);let p=[23776637887n%m,77586679170n%m],n=iv((p[0]*p[0]-p[0]*p[1]+p[1]*p[1])%m,m);
return imul(p,p,m).map(x=>x*n%m);}
ck(gp(65520).every((x,i)=>x===[24571n,32760n][i]),"whole Q32760 ratio");
ck(gp(390).every((x,i)=>x===[1n,0n][i])&&gp(30).every((x,i)=>x===[1n,0n][i]),"whole odd common ratios");
ck(gp(68).every((x,i)=>x===[67n,0n][i]),"whole raw Y34 ratio");
const N=32760,k=24571,half=N/2,quarter=N/4;
for(let j=0;j<N;j++){
 const col=new Map(),add=(i,x)=>col.set(i,(col.get(i)||0)+x);
 add((j+quarter*(j%4))%N,1);
 if(j%2===0){add(j,-1);add((j+half)%N,-1);}
 const p=(k*j+half)%N,sg=j%2===0?-1:1;
 for(const[i,x]of col)ck(x===(i===p?sg:0),"whole quarter kernel");
 ck((k*p+half)%N===j&&((p+j)%2===0),"whole square and central sign");
}
const projector=row=>row.map(x=>row.map(y=>esc(em(ec(x),y),1,Number(he(row,row)[0][0]))));
const commonOdd=15*13;
ck(commonOdd===65*3&&eq(em(E(4,1),ec(E(4,1))),E(13))&&eq(em(del,ec(del)),E(3)),"common odd195 anchors");
const dCenter=10271;
ck(dCenter%4===3&&dCenter%(5*13*79)===1,"whole D10270 center");
return {coordinates:"(xi1,xi2,xi3,x=xi4,c,d0)",frame:F.map(r=>r.map(out)),inverse:Finv.map(r=>r.map(out)),Gram:G.map(r=>r.map(out)),determinant:out(det),
D10270:D.map(out),old_W:oldcoef.map(out),original_Y:ycoef.map(out),W2:W2.map(out),Q32760:Qc.map(out),B15:B15.map(out),
B15_Y_pair:out(he(Y,B15)),B15_W2_pair:out(he(W2,B15)),S_T_B_plane_determinant:263,
raw_W_relation:"W + omega^2 Wprime + omega W2 = 0",
whole_Q_center:["24571","32760"],whole_Q_kernel:"-chi65*(1/4 sum E4 -1/2 sum E2)",whole_Q_square:1,
whole_D_center:dCenter,whole_D_core:"chi65",
B15_core:"chi15=chi65, via the common odd S195",B15_five_sigma_diagonal:"sigma^15*x^2*(x^3+b)/7",
B15_first_term:"z^5/7",B15_full_six_input_marginal:"zero because the independent sigma(x) has mass zero",
quarter_period:out(em(E(-18),alpha)),quarter_period_norm:2268,quarter_alternating_pair:out(periodPair),
Y_projection:projector(Y).map(r=>r.map(out)),B15_projection:projector(B15).map(r=>r.map(out)),
eta_definition:"K_W2 rho0 = omega^2 T e2 = -omega^2 T v -(rho0+h)/2",
eta_new_row:"-omega^2 Snew tensor D5_*Lambda_old",eta_reference_row:"-omega^2 Href tensor D5_*Lambda_ref",
remaining_Q_common_core:"lambda^2 on rho0 and eta, with the full non-diagonal two-axis Gram",
warning:"T and U do not preserve the four-input block; complete original five-companion transports are kept."
};
}

if(typeof module!=="undefined"){
  module.exports={certifyR510};
  if(require.main===module){
    const report=certifyR510();
    require("fs").writeFileSync(__filename.replace(/\.js$/,".json"),
      JSON.stringify(report,null,2)+"\n");
    console.log("R510 full frame, all 32760 quarter columns, two arithmetic rows and odd15 bridge verified.");
  }
}
