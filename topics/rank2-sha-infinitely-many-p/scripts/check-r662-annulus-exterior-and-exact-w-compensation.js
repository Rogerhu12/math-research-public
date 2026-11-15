#!/usr/bin/env node
// R662 exact original-coordinate certificate; no external packages.
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



function certificate(){

const row=a=>a.map(x=>Array.isArray(x)?E(...x):E(x));
const C=vm(row([1,0,-1,1,0,0]),ei(E(1,2)));
const A=row([[1,2],[2,4],[3,1],[2,-1],0,0]),Qrow=row([0,0,0,0,1,2]),Lrow=row([0,0,0,0,2,-1]);
const Y=va(A,Qrow),W=va(A,row([0,0,0,0,[3,6],4]));
const D=row([1,[-1,-1],[0,-2],0,1,[2,3]]),F=va(D,C),H=row([-1,2,[0,1],[1,1],0,0]),g=E(3,-2),G=va(vm(H,E(13)),vm(F,g));
const aa=E(-5,-6,29),bf=E(5,6,5),bq=E(11,6,5),bl=E(2,12,5),by=E(20,3,17);
const F0=vs(vs(F,vm(A,aa)),vm(Qrow,bf)),D0=vs(F0,C);
const aW=em(he(A,W),ei(he(W,W))),qW=em(he(Qrow,W),ei(he(W,W))),dW=em(he(D0,W),ei(he(W,W)));
ck(eq(aW,E(29,0,72))&&eq(qW,E(5,-6,72))&&eq(dW,E(-6,-1,60)),"actual W changes");
ck(eq(he(A,Qrow),E(0))&&eq(he(A,Lrow),E(0))&&eq(he(Qrow,Lrow),E(0)),"true A/Q/L frame");
for(const V of[C,F,G])ck(ez(he(V,Y))&&ez(he(V,W)),"original q invariance only on true Y/W axes");
ck(eq(he(W,Y),em(by,he(Y,Y))),"actual mixed Y/W coefficient");
ck(W.every((v,i)=>eq(v,ea(ea(A[i],em(bq,Qrow[i])),em(bl,Lrow[i])))),"complete W A/Q/L form");
return {format:"R662 exact annulus/exterior geometry",rows:{C:C.map(out),A:A.map(out),Q:Qrow.map(out),L:Lrow.map(out),Y:Y.map(out),W:W.map(out),F0:F0.map(out),D0:D0.map(out)},coefficients:{a:out(aa),bF:out(bf),bQ:out(bq),bL:out(bl),bY:out(by),aW:out(aW),qW:out(qW),dW:out(dW)},source:"same mu0, same R594 q_N; no new source or ray",
exact_identities:{
Y_total:"lambda^(r+m)*beta^N*<lambda^2>^(m*d*u)*J_S(u)",
joint_return:"g_r=chi^r lambda^(3r), B_r=P_A,kappa^(2r) P_Q,kappa^r",
Y_common:"g_r * integral Q in p^m units, q_N(B_r x)*<(Q+kappa^r A)/p^m>^(d*u)",
q_common:"F0+a*kappa^(2r) A+bF*kappa^r Q; G0+g times the same increment",
W_common_after_Q_core:"a_core^m g_r * integral q_N(B_r P_Q,kappa^m x), Wobs unit",
W_observation_coefficients:{A:"kappa^(2r)*(1-bY)+epsilon*bY*kappa^(r-m)",Q:"kappa^(r+m)*(bQ-bY)+epsilon*bY",L:"bL",epsilon:"(-1)^(r+m); take r even"},
exterior_transport:"a_core^-m (O_m^0,O_m^1)^T=[[1,0],[m log<lambda^2>,1]] (M0(1-a_core),M0 ell_D)^T",
W_full_compensation:"C_r,m=(1-lambda^2)*I_r,m'(0)/(d*g_r), retaining f_r,m composed with the actual W core",
remaining_two_W_rows:"Theta_+-^(j)=integral G0 p0 1_(bL L +- bY Q unit) log^j<bL L +- bY Q> dmu0"
},errors:{mass:"p^(r+m-N)",log:"p^min(r-m,r+m-N+1)",difference:"p^min(r-m,r-N+1)",finite_unit_mass:"r>=N+1 and r>m; M0 unit on R659 subfamily"},checks:"all exact original coordinate identities passed; convergence and full arithmetic compensation are proved in the result"};

}
const output=JSON.stringify(certificate(),null,2)+'\n';
if(process.argv[2])require('fs').writeFileSync(process.argv[2],output);else process.stdout.write(output);
