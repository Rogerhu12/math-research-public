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

const pow=(x,n)=>{let a=E(1);for(let j=0;j<n;j++)a=em(a,x);return a;};
const dot=(r,v)=>r.reduce((s,c,i)=>ea(s,em(c,v[i])),E(0));
const norm=x=>em(x,ec(x));
const del=E(1,2),a=E(-2,1,2),b=E(4,3,2),b3=E(76,8);
const tau=ident(5);tau[0][0]=E(1,0,2);tau[0][1]=E(-3,0,2);tau[1][0]=E(-1,0,2);tau[1][1]=E(-1,0,2);
ck(mm(tau,tau).every((r,i)=>r.every((x,j)=>eq(x,E(i===j?1:0)))),"complete involution");
const G=Array.from({length:5},(_,i)=>Array.from({length:5},(_,j)=>E(i===j?[6,2,1,1,1][i]:0)));
const transpose=A=>A[0].map((_,j)=>A.map(r=>r[j]));
const Gt=mm(mm(tau,G),transpose(tau));
ck(Gt.every((r,i)=>r.every((x,j)=>eq(x,G[i][j]))),"complete Hermitian isometry");
const factors=[[E(2),E(0)],[E(1),E(1)],[E(1),E(-1)]],tau2=tau.slice(0,2).map(r=>r.slice(0,2));
const transformed=mm(factors,transpose(tau2));
const expected=[factors[2],vm(factors[1],E(-1)),factors[0]];
ck(transformed.every((r,i)=>r.every((x,j)=>eq(x,expected[i][j]))),"three real sigma factors: sign minus");
const Y=[a,b,esc(del,2),E(1),E(2)],W=[a,b,esc(del,2),esc(del,3),E(4)];
const Wp=[E(0),E(4,4),esc(del,2),E(4,2),E(4)];
const F=[esc(del,1,6),E(1,-2,2),E(-1,-1),E(1),E(2,3)];
const H=[E(-1,-1,2),E(-1,1,2),E(2),E(0),E(0)];
const Grow=va(vm(H,E(13)),vm(F,E(3,-2)));
const Yt=mm([Y],tau)[0],Wt=mm([W],tau)[0],Ft=mm([F],tau)[0],Gtrow=mm([Grow],tau)[0];
ck(eq(Yt[0],ec(a))&&eq(Yt[1],ec(b)),"two CM coefficient conjugates");
ck(Wt.slice(0,3).every((x,i)=>eq(x,Yt[i])),"common transformed free part");
const free_image=[E(1),E(-1),E(0),E(0),E(0)];
ck(eq(dot(Y,free_image),E(-3,-1)),"old Y on reflected strip");
ck(eq(dot(W,free_image),E(-3,-1)),"old W on reflected strip");
ck(eq(dot(F,free_image),E(-1,4,3)),"old F on reflected strip");
const rho=em(a,ei(ec(a))),ct=pow(rho,3);
const c3=en(esc(em(b3,ei(pow(a,3))),1,21)),c5=esc(em(em(pow(b,2),b3),ei(pow(a,5))),4,7);
const d3=en(esc(em(b3,ei(pow(ec(a),3))),1,21)),d5=esc(em(em(pow(ec(b),2),b3),ei(pow(ec(a),5))),4,7);
ck(eq(d3,em(ct,c3)),"entire negative-three leading line cancels");
const eps=es(d5,em(ct,c5));
ck(eq(eps,E(6789120,4239360,117649)),"actual negative-five coefficient");
ck(eq(norm(eps),E(102865305600n,0,40353607n)),"negative-five norm");
ck(eq(norm(ea(E(1),ct)),E(400,0,343)),"global arithmetic scalar unit norm");
const ker=[E(4,-1),E(0,7),E(-3,-1),E(2,3),E(7)];
ck([Y,W,Wp,Grow].every(r=>ez(dot(r,ker))),"old pi4 kernel");
ck(eq(dot(Yt,ker),E(18,6)),"new arithmetic row does not descend old pi4");
return {
 field:"Q(omega), omega^2+omega+1=0; each entry [a,b] is a+b omega",
 source:"unchanged nu_flat=(f1_Z Sigma_Q-f3_Z Theta_Q)*sigma_r*sigma_c*sigma_d/42",
 full_tau:tau.map(r=>r.map(out)),
 sigma_factor_identity:{original:factors.map(r=>r.map(out)),transformed:transformed.map(r=>r.map(out)),permutation:[2,1,0],sign:-1},
 physical_rows:{Y:Y.map(out),W:W.map(out),Y_tau:Yt.map(out),W_tau:Wt.map(out),F_tau:Ft.map(out),G_tau:Gtrow.map(out)},
 reflected_strip:{inverse_rows:[tau[0].map(out),tau[1].map(out)],equivalent:"Z,Q units; Z+Q in p^n; r,c,d in p^n",oldYmodpn:out(dot(Y,free_image)),oldWmodpn:out(dot(W,free_image)),oldFmodpn:out(dot(F,free_image)),norm_F_coefficient:out(norm(dot(F,free_image)))},
 rho:out(rho),c_tau:out(ct),c3:out(c3),c5:out(c5),c3_tau:out(d3),c5_tau:out(d5),epsilon_tau:out(eps),
 norm_epsilon:out(norm(eps)),norm_epsilon_factorization:"2^22*3^2*5^2*109/7^9",
 norm_one_plus_c_tau:out(norm(ea(E(1),ct))),
 old_pi4:{kernel:ker.map(out),Y_tau_on_kernel:out(dot(Yt,ker)),preserved:false},
 actual_statements:{total_g:"-(1+c_tau)*T",rectangle_g:"d_p*beta^(4n)*epsilon_tau*Omega^5*kappa^(5n)*I1 + p^(9n)O",negative_five_error:"p^(4n) O, same depth n",tau_image:"disjoint from original rectangle and both R601 core images",transported_carry:"(Wtilde*ell) compose tau - c_tau*Wtilde*ell",no_unit_claim_for_transported_weighted_local:true,no_total_nonvanishing:true}
};
})();
if (typeof module !== "undefined") module.exports = report;
if (typeof require !== "undefined" && require.main === module) {
  const fs = require("fs");
  const data = JSON.stringify(report, null, 2) + "\n";
  if (process.argv[2]) fs.writeFileSync(process.argv[2], data); else process.stdout.write(data);
}
