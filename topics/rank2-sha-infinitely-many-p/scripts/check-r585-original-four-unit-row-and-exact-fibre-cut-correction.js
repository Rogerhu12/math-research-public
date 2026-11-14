#!/usr/bin/env node
// Exact certificate; no external dependencies.
const result=(()=>{
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


const w=E(0,1),w2=em(w,w),del=E(1,2),a=E(2,3),l=E(1,3),g=E(3,-2),alpha=E(1,-1);
const row=x=>x.map(t=>Array.isArray(t)?E(...t):E(t));
const c=row([0,0,0,0,1,0]),d=row([0,0,0,0,0,1]);
const D4=[E(1),w2,E(0,-2),E(0),E(0),E(0)],C=vm(row([1,0,-1,1,0,0]),ei(del));
const H1=[E(-1),E(2),w,E(1,1),E(0),E(0)],A=[del,esc(del,2),E(3,1),E(2,-1),E(0),E(0)];
const U=va(c,vm(d,w)),V=vs(c,vm(d,w)),D=va(va(D4,vm(U,alpha)),vm(V,w));
const F=va(D,C),Eold=va(D,vm(C,E(14))),Gold=va(vm(H1,E(13)),vm(F,g));
const Y=va(va(A,c),vm(d,E(2))),W=va(va(A,vm(c,esc(del,3))),vm(d,E(4)));
const re=(x,y,m)=>ck(x.every((v,i)=>eq(v,y[i])),m);
const me=(x,y,m)=>ck(x.every((r,i)=>r.every((v,j)=>eq(v,y[i][j]))),m);

const G=Gold,Dm=vs(va(D4,c),vm(d,a)),Wp=[E(4,4),E(2,4),E(4,4),E(0),E(4,2),E(4)];
const f=[C,F,Y,W,Wp,G],iv=inverse(f),pi=[Y,W,Wp,G];
ck(eq(he(F,F),E(13))&&ez(he(C,F)),"true F degree13 and C orthogonality");
for(const z of pi)ck(ez(he(z,C))&&ez(he(z,F)),"all four original observations fixed");
const P0=ident(6).map((r,i)=>r.map((x,j)=>es(x,em(E(1,0,13),em(ec(F[i]),F[j])))));
const original=[c,d,U,V],coef=[E(1,0,13),esc(en(l),1,13),E(4,2,13),esc(w2,2,13)];
const projected=original.map((r,i)=>vs(r,vm(F,coef[i]))),obsRows=[];
for(let i=0;i<4;i++){
 re(projected[i],mm([original[i]],P0)[0],"actual zero-F projection");
 ck(ez(he(projected[i],C))&&ez(he(projected[i],F)),"projected unit conditions depend on pi4 only");
 const cr=mm([projected[i]],iv.inverse)[0];ck(ez(cr[0])&&ez(cr[1]),"projected pi4 expression");obsRows.push(cr.slice(2));
}
const piFrame=[vm(C,del),vm(F,E(3)),Y,W,Wp,vm(G,E(3))];
for(const rr of piFrame)for(const e of rr)for(const x of e)ck(x[1]===1n,"complete odd3/117 frame integral");
const oddCount=rr=>rr.reduce((s,x)=>s+((x[0][0]%2n!==0n||x[1][0]%2n!==0n)?1:0),0);
ck(oddCount(piFrame[1])%2===1,"actual3F standard odd117");
const a117=esc(E(4,1),3);ck(eq(em(a117,ec(a117)),E(117)),"odd117 fixed sigma anchor");
const RC=ident(6);RC[4][4]=E(-1);const RD=ident(6);RD[5][5]=E(-1);
re(mm([U],RC)[0],vm(V,E(-1)),"Rc sends U to minus V");
re(mm([V],RC)[0],vm(U,E(-1)),"Rc sends V to minus U");
re(mm([U],RD)[0],V,"Rd swaps U V");re(mm([V],RD)[0],U,"Rd swaps V U");
const u=vm(va(vm(c,w),vm(d,E(1,-1))),E(1,0,2)),L=va(vm(c,l),d);
re(u,vm(va(U,vm(V,w2)),E(-1,0,2)),"native u line");
re(L,va(vm(U,w),vm(V,del)),"native L line");
const reductions={};
for(const[name,r]of[["U",U],["V",V],["c",c],["d",d],["L",L],["other_u",va(U,vm(V,w))]]){
 const uv=inverse([[E(1),w],[E(1),en(w)]]),cf=mm([[r[4],r[5]]],uv.inverse)[0];
 reductions[name]=es(cf[1],em(cf[0],w2));
}
ck(eq(reductions.L,esc(w,2)),"native L becomes 2omega V");
for(const x of Object.values(reductions))ck(!ez(x),"all A4 lines nonzero on native branch");
re(mm([D],RD)[0],Dm,"actual second D is reflected D");
ck(eq(he(D,D),E(14))&&eq(he(Dm,Dm),E(14))&&ez(he(D,Dm)),"true orthogonal degree14 axes");
re(vs(D,Dm),vm(d,esc(a,2)),"same-branch supports disjoint on d unit");
const swaps={F:vs(F,vm(d,esc(a,2))),E:vs(Eold,vm(d,esc(a,2))),G:vs(G,vm(d,esc(em(g,a),2))),Y:vs(Y,vm(d,E(4))),W:vs(W,vm(d,E(8)))};
for(const[name,r]of Object.entries({F,E:Eold,G,Y,W}))re(mm([r],RD)[0],swaps[name],"complete reflected "+name);
const Td=va(D4,c),X0=vs(c,vm(Td,E(1,0,7)));
const Cd=va(C,vm(Td,E(1,0,7))),Hd=va(H1,vm(Td,esc(g,1,7)));
const Ed=vm(Cd,E(14)),Gd=va(vm(Hd,E(13)),vm(Cd,g));
const Yd=vs(vs(Y,vm(d,E(2))),vm(Td,esc(l,2,7)));
const Wd=vs(vs(W,vm(d,E(4))),vm(Td,esc(l,4,7)));
const frameDD=[D,Dm,Ed,Gd,Yd,Wd],idd=inverse(frameDD);
for(const r of frameDD.slice(2))ck(ez(he(r,D))&&ez(he(r,Dm)),"four common companions retained");
re(Eold,vs(Ed,Dm),"same E depends only on the other axis");
re(G,vs(Gd,vm(Dm,g)),"same G depends only on other axis");
re(Y,vs(Yd,vm(Dm,em(E(2),ei(a)))),"same Y depends only on other axis");
re(W,vs(Wd,vm(Dm,em(E(4),ei(a)))),"same W depends only on other axis");
re(c,va(X0,vm(va(D,Dm),E(1,0,14))),"exact c recovery");
re(d,vm(vs(D,Dm),em(E(1,0,2),ei(a))),"exact d recovery");
re(U,va(X0,va(vm(D,E(2,1,7)),vm(Dm,esc(w2,1,7)))),"exact U recovery");
re(V,va(X0,va(vm(D,esc(w2,1,7)),vm(Dm,E(2,1,7)))),"exact V recovery");
const xc=mm([X0],idd.inverse)[0];ck(ez(xc[0])&&ez(xc[1]),"X0 depends only on common companions");
const norm=x=>out(em(x,ec(x)));
return {
title:"R585 actual four-unit arithmetic row, full norm13 cut correction and antisymmetric two-fourteen branches",
convention:"[a,b]=a+b omega; exact BigInt rational arithmetic.",
original_pi4_frame:f.map(r=>r.map(out)),frame_det:out(iv.det),frame_norm_det:norm(iv.det),
integral_frame:piFrame.map(r=>r.map(out)),integral_frame_det:out(inverse(piFrame).det),
F_zero_projection:P0.map(r=>r.map(out)),projected_rows:projected.map(r=>r.map(out)),
projected_rows_on_pi4:obsRows.map(r=>r.map(out)),physical_F_coefficients:coef.map(out),
original_rows_on_pi4_plus_F:original.map(r=>mm([r],iv.inverse)[0].map(out)),
native_u_branch_reductions_on_V:Object.fromEntries(Object.entries(reductions).map(([k,v])=>[k,out(v)])),
core117:{anchor:out(a117),degree:117,ratio_mod234:"1",actual_scalar:"beta"},
two_fourteen:{D:D.map(out),Dminus:Dm.map(out),frame:frameDD.map(r=>r.map(out)),
inverse:idd.inverse.map(r=>r.map(out)),det:out(idd.det),norm_det:norm(idd.det),
X0:X0.map(out),X0_common_companions:xc.slice(2).map(out),
complete_reflected_observations:Object.fromEntries(Object.entries(swaps).map(([k,r])=>[k,r.map(out)])),
normalized_unit_lines:{T:"unit",c:"X0+T/14",U:"X0+omega^2 T/7",V:"X0+(2+omega)T/7",E:"Ed-T"},
source_core:"beta on both original pure S2 tensors; Rd geometric transport preserves the complete joint"},
sigma_plain_complements:{nonzero_orders:"1 modulo6, full tail starts at7",c_pole_coefficients:["1","3delta"],d_pole_coefficients:["2","4"]},
scope:"The exact F-neutrality correction keeps eight unit-change strips and the F-unit carry exterior. No conditional row is assigned zero.",
checks:"All exact assertions passed."};

})();
console.log(JSON.stringify(result,null,2));
