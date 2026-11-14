#!/usr/bin/env node
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



const report = (() => {

const ep=(x,n)=>{let y=E(1);for(let i=0;i<n;i++)y=em(y,x);return y;};
const trim=A=>{let B=A.slice();while(B.length>1&&ez(B.at(-1)))B.pop();return B;};
const pa=(A,B)=>trim(Array.from({length:Math.max(A.length,B.length)},(_,i)=>ea(A[i]||E(0),B[i]||E(0))));
const pn=A=>A.map(en),ps=(A,B)=>pa(A,pn(B));
const pm=(A,B)=>{let C=Array.from({length:A.length+B.length-1},()=>E(0));A.forEach((a,i)=>B.forEach((b,j)=>C[i+j]=ea(C[i+j],em(a,b))));return trim(C);};
const pc=(A,c)=>trim(A.map(x=>em(x,c)));
const pe=(A,B)=>{let C=ps(A,B);return C.every(ez);};
const P=x=>[x], zero=P(E(0)),one=P(E(1)),u=[E(0),E(1)],u4=[E(0),E(0),E(0),E(0),E(1)];
const G=[6,2,1,1,1],del=E(1,2),aZ=E(-2,1,2),aQ=E(4,3,2);
const Y=[aZ,aQ,esc(del,2),E(1),E(2)],W=[aZ,aQ,esc(del,2),esc(del,3),E(4)];
const gram=(v,w)=>v.reduce((s,a,i)=>ea(s,esc(em(a,ec(w[i])),G[i])),E(0));
ck(eq(gram(Y,Y),E(34))&&eq(gram(W,W),E(72)),"norms");
const cross=gram(Y,W);ck(eq(cross,E(34,-6)),"cross");
const projector=(L,N,t)=>L.map((_,i)=>L.map((_,j)=>pa(P(E(i===j?1:0)),pc(ps(t,one),esc(em(ec(L[i]),L[j]),G[i],N)))));
const applyRow=(L,M)=>M[0].map((_,j)=>L.reduce((s,c,i)=>pa(s,pc(M[i][j],c)),zero));
const MY=projector(Y,34,pn(u)),MW=projector(W,72,u4);
const hp=pc(pa(one,u),esc(ec(cross),1,34)),kp=pc(ps(one,u4),esc(cross,1,72));
const yp=applyRow(Y,MY),wyp=applyRow(W,MY),ywp=applyRow(Y,MW),wp=applyRow(W,MW);
Y.forEach((c,i)=>ck(pe(yp[i],pc(pn(u),c)),"Y true scale"));
W.forEach((c,i)=>ck(pe(wp[i],pc(u4,c)),"W true scale"));
W.forEach((c,i)=>ck(pe(wyp[i],ps(P(c),pc(hp,Y[i]))),"W of PY"));
Y.forEach((c,i)=>ck(pe(ywp[i],ps(P(c),pc(kp,W[i]))),"Y of PW"));
const Dy=ps(one,hp),Dw=ps(one,kp),Delta=es(E(2),esc(del,12));
const Sy=ps(P(esc(del,3)),hp),Ty=ps(P(E(4)),pc(hp,E(2)));
const Sw=ps(one,pc(kp,esc(del,3))),Tw=ps(P(E(2)),pc(kp,E(4)));
const rYn=pc(pm(Sy,Ty),en(ei(Delta))),rYd=pm(Dy,Dy);
const rWn=pc(pm(Sw,Tw),ei(Delta)),rWd=pm(Dw,Dw);
const rY0=em(rYn[0],ei(rYd[0])),rW0=em(rWn[0],ei(rWd[0]));
ck(eq(rY0,E(-14785,-13963,981)),"rY0");
ck(eq(rW0,E(935106,1970400,10678621)),"rW0");
const gamma3=en(em(esc(del,2,21),ei(ep(aZ,3))));
const gamma5=em(esc(em(del,ep(aQ,2)),8,7),ei(ep(aZ,5))),ratio=em(gamma5,ei(gamma3));
ck(eq(ratio,esc(em(ep(aQ,2),ei(ep(aZ,2))),-12)),"universal low-moment ratio");
const c3=em(gamma3,Delta),c5=em(gamma5,Delta);
ck(eq(c3,E(10400,11008,7203)),"original c3");
ck(eq(c5,E(4312960,1031168,117649)),"original c5");
const D=96107589n,C3=esc(en(rY0),D),C0=esc(rW0,D);
ck(C3.flat().every((v,i)=>i%2===0||v===1n)&&C0.flat().every((v,i)=>i%2===0||v===1n),"integer coefficients");
const F=[C0,E(0),E(0),C3,E(D)],Fbar=F.map(ec),NF=pm(F,Fbar);
ck(NF.every(x=>x[1][0]===0n&&x[0][1]===1n),"norm polynomial integral");
const norm=x=>out(em(x,ec(x)));
return {
 field:"Q(omega), omega^2+omega+1=0; each entry [a,b] is a+b omega",
 source:"the unchanged R599/R601 nu_flat on (Z,Q,r,c,d)",
 exact_physical_checks:{YNorm:34,WNorm:72,cross:out(cross),PY:"Y -> -kappa Y; W -> W-hY",PW:"W -> kappa^4 W; Y -> Y-kW"},
 h_coefficients:hp.map(out),k_coefficients:kp.map(out),
 normalized_Y_image:{s_numerator:Sy.map(out),t_numerator:Ty.map(out),denominator:Dy.map(out)},
 normalized_W_image:{s_numerator:Sw.map(out),t_numerator:Tw.map(out),denominator:Dw.map(out)},
 rY:{numerator:rYn.map(out),denominator:rYd.map(out),at_kappa_0:out(rY0)},
 rW:{numerator:rWn.map(out),denominator:rWd.map(out),at_kappa_0:out(rW0)},
 Delta:out(Delta),gamma3:out(gamma3),gamma5:out(gamma5),common_ratio:out(ratio),c3:out(c3),c5:out(c5),
 fixed_bad_polynomial:{denominator:String(D),F_coefficients_low_to_high:F.map(out),norm_coefficients_low_to_high:NF.map(x=>qs(x[0]))},
 denominators:{norm_one_minus_h0:norm(Dy[0]),norm_one_minus_k0:norm(Dw[0]),norm_Delta:norm(Delta)},
 conclusions:{C:"1 + lambda*rY(kappa) + lambda^4*rW(kappa)",total_union:"C*R_n + J_n",complete_remainder:"T - C*R_n - J_n",tail:"J_n in p^(9n) O; J_(n+1)-beta^4*kappa^3 J_n in p^(9n+3) O",negative_five_error:"p^(4n) O after dividing the original denominator times C",no_total_nonvanishing:true}
};
})();
if (typeof module !== "undefined") module.exports = report;
if (typeof require !== "undefined" && require.main === module) {
  const fs = require("fs");
  const data = JSON.stringify(report, null, 2) + "\n";
  if (process.argv[2]) fs.writeFileSync(process.argv[2], data); else process.stdout.write(data);
}
