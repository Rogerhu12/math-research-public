#!/usr/bin/env node
// R556 exact original carry intersections, odd37 axes and actual Mellin cuts.
function certifyR556(){
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


const w=E(0,1),w2=em(w,w),delta=E(1,2),gamma=E(3,1),gb=ec(gamma);
const zeta=[E(1),w2,w];
const c=[0,0,0,0,1,0].map(x=>E(x)),dr=[0,0,0,0,0,1].map(x=>E(x));
const C=vm([1,0,-1,1,0,0].map(x=>E(x)),ei(delta));
const D4=[E(1),w2,E(0,-2),E(0),E(0),E(0)];
const H1=[E(-1),E(2),w,E(1,1),E(0),E(0)];
const M=va(c,vm(dr,E(2,3))),F=va(va(D4,C),M);
const G=va(vm(H1,E(13)),vm(F,E(3,-2)));
const A=[delta,esc(delta,2),gamma,gb,E(0),E(0)],Y=va(va(A,c),vm(dr,E(2))),W=va(va(A,vm(c,esc(delta,3))),vm(dr,E(4)));
const Rc=ident(6);Rc[4][4]=E(-1);
const H=ident(6),pair=[[E(-1,-1,2),E(-1,-2,2)],[E(2,1,2),E(-1,-1,2)]];
for(let i=0;i<2;i++)for(let j=0;j<2;j++)H[4+i][4+j]=pair[i][j];
const u=[E(0),E(0),E(0),E(0),esc(w,1,2),esc(es(E(1),w),1,2)];
const L=va(vm(c,E(1,3)),dr),Yc=mm([Y],Rc)[0],Wc=mm([W],Rc)[0],Fp=mm([F],Rc)[0],Gp=mm([G],Rc)[0];
ck(Fp.every((x,i)=>eq(x,vs(F,vm(c,E(2)))[i])),"F reflection");
const taus=[w,w2],axes=[];
for(const tau of taus){
 const J=vs(vm(F,es(E(1),tau)),vm(c,E(2))),JH=mm([J],H)[0];
 ck(eq(he(J,J),E(37)),"degree37");ck(ez(he(J,C)),"C fixed");
 ck(J.every(x=>x.every(q=>q[1]===1n))&&JH.every(x=>x.every(q=>q[1]===1n)),"integral original and H rows");
 ck(eq(he(Y,J),E(-2))&&eq(he(W,J),esc(delta,-6)),"mixed native rows");
 ck(eq(he(Yc,J),esc(ec(tau),2))&&eq(he(Wc,J),em(esc(delta,6),ec(tau))),"reflected rows");
 const halfCount=row=>row.filter(x=>x.some(q=>(q[0]%2n+2n)%2n===1n)).length;
 const jh=halfCount(JH),jo=halfCount(J);ck(jo%2===1&&jh%2===1,"odd half-character");
 const Jr=mm([J],Rc)[0],Jother=vs(vm(F,es(E(1),ec(tau))),vm(c,E(2)));
 ck(Jr.every((x,i)=>eq(x,em(en(tau),Jother[i]))),"Rc swaps two actual axes");
 const inners={};for(const[name,row]of Object.entries({C,F,G,H1,Y,W,Yc,Wc,u,L,c,d:dr}))inners[name]=out(he(row,J));
 axes.push({tau:out(tau),row:J.map(out),rowH:JH.map(out),odd_counts:[jo,jh],inner_products:inners});
 for(let j=0;j<3;j++){
  const k=zeta.findIndex(z=>eq(z,em(tau,zeta[j])));
  const r=vs(F,vm(C,zeta[j])),s=vs(Fp,vm(C,zeta[k]));
  const Ej=va(F,vm(C,esc(zeta[j],13))),Ekp=va(Fp,vm(C,esc(zeta[k],13)));
  ck(s.every((x,i)=>eq(x,ea(em(tau,r[i]),J[i]))),"true D carry");
  ck(Ekp.every((x,i)=>eq(x,ea(em(tau,Ej[i]),J[i]))),"true E carry");
  const expectedGp=va(va(vm(G,tau),vm(H1,esc(es(E(1),tau),13))),vm(J,E(3,-2)));
  ck(Gp.every((x,i)=>eq(x,expectedGp[i])),"true G translation");
 }
}
const J0=vs(vm(F,es(E(1),w)),vm(c,E(2))),J1=vs(vm(F,es(E(1),w2)),vm(c,E(2)));
ck(eq(he(J0,J1),esc(w,-35)),"pair Gram");
ck(va(J0,vm(J1,w)).every((x,i)=>eq(x,em(esc(w2,2),c[i]))),"short c identity");
const frame4=[C,D4,H1,A].map(r=>r.slice(0,4)),inv4=inverse(frame4);
ck(eq(inv4.det,E(17,3)),"first4 determinant");
const cFrom=va(vm(dr,E(2,1)),vm(u,esc(w2,2)));
ck(cFrom.every((x,i)=>eq(x,c[i])),"u-strip c");
const nativeExpected=[
 va(va(A,vm(dr,E(4,1))),vm(u,esc(w2,2))),
 va(va(A,vm(dr,E(4,9))),vm(u,esc(es(E(1),w),6))),
 va(va(A,vm(dr,en(w))),vm(u,esc(w2,-2))),
 va(va(A,vm(dr,E(4,-9))),vm(u,esc(es(E(1),w),-6)))
];
for(let j=0;j<4;j++)ck(nativeExpected[j].every((x,i)=>eq(x,[Y,W,Yc,Wc][j][i])),"native log row");
const roots=[E(-4,-1),E(-4,-9),w,E(-4,9)],diff=[];
for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)diff.push({i,j,norm:out(em(es(roots[i],roots[j]),ec(es(roots[i],roots[j]))))});
const Zstar=vs(W,vm(Y,esc(delta,3)));
ck(eq(he(Zstar,Zstar),E(936)),"Zstar norm");
for(const Jr of [J0,J1])ck(ez(he(Zstar,Jr)),"Zstar is a true common J companion");
ck(mm([Zstar],Rc)[0].every((x,i)=>eq(x,Zstar[i])),"Zstar Rc fixed");
for(const rr of [C,F,G])ck(ez(he(Zstar,rr)),"Zstar retains original carry observations");
const gamma37=E(7,3);ck(eq(em(gamma37,ec(gamma37)),E(37)),"true odd37 anchor");
return{
axes,Gram:[[["37","0"],out(esc(w,-35))],[out(esc(w2,-35)),["37","0"]]],Gram_determinant:"144",
source_integrality:"J_tau and J_tau H are integral CM rows with identical odd half-character",
anchor:{gamma37:out(gamma37),norm:37,core:"beta=-lambda",ray:"pi0=1 modulo37; old parity gives g=1 modulo74"},
Zstar:{row:Zstar.map(out),norm:936,fixed_by:"Rc,Jomega,Jomega2,C,F,G"},
first4_frame:frame4.map(r=>r.map(out)),first4_determinant:out(inv4.det),first4_norm:out(em(inv4.det,ec(inv4.det))),
native_rows_in_A_d_u:[{A:"1",d:["4","1"],u:out(esc(w2,2))},{A:"1",d:["4","9"],u:out(esc(es(E(1),w),6))},{A:"1",d:["0","-1"],u:out(esc(w2,-2))},{A:"1",d:["4","-9"],u:out(esc(es(E(1),w),-6))}],
four_log_roots:roots.map(out),pairwise_root_difference_norms:diff,
common_q_translation:{Dprime:"tau D+Jtau",Eprime:"tau E+Jtau",Gprime:"tau G+13(1-tau)H1+(3-2omega)Jtau",
normalized:"qRc=P(D/kappa^n+tau^-1 J/kappa^n,E+tau^-1 J,G+13(tau^-1-1)H1+(3-2omega)tau^-1 J)/(3bOmega^6)"},
retained:"two one-sided q supports; four disjoint Mellin boundary tubes; G/H1 unrestricted; full kappa^-n terms"
};
}
if(typeof module!=='undefined')module.exports={certifyR556};
if(typeof require!=='undefined'&&require.main===module){process.stdout.write(JSON.stringify(certifyR556(),null,2)+'\n');}
