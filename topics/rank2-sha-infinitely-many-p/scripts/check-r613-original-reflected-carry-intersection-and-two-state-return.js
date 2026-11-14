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

const delta=E(1,2),w=E(0,1),wb=E(-1,-1),g=E(2,3),gb=ec(g),u=E(1,-1,3);
const metric=[1,6,2,1,1,1];
const inner=(x,y)=>x.reduce((s,c,i)=>ea(s,esc(em(c,ec(y[i])),metric[i])),E(0));
const zero=()=>Array.from({length:6},()=>E(0)),C=zero(),L=zero();C[0]=E(1);L[1]=E(1);
const J=[E(0),E(0),w,wb,E(1),g],A=vs(J,C),H=va(J,vm(C,E(11)));
const R1=[E(0),E(0),E(1),E(0),esc(wb,-2),E(0)];
const R2=[E(0),E(0),E(0),E(1),en(w),E(0)];
const R3=[E(0),E(0),E(0),E(0),en(gb),E(1)];
const frame=[A,H,L,R1,R2,R3],inv=inverse(frame),Gram=frame.map(x=>frame.map(y=>inner(x,y)));
ck(eq(inv.det,E(132)),"whole frame determinant");
ck(eq(inner(J,J),E(11))&&eq(inner(A,A),E(12))&&eq(inner(H,H),E(132)),"physical axis norms");
for(let i=0;i<3;i++)for(let j=0;j<6;j++)if(i!==j)ck(ez(Gram[i][j]),"full orthogonality");
const F=va(J,vm(L,u)),Ft=vs(J,vm(L,u)),D=vs(F,C),Dt=vs(Ft,C),Eplus=va(F,vm(C,E(13))),Eminus=va(Ft,vm(C,E(13)));
const H1=[E(0),E(-1,0,2),esc(delta,-1,2),E(2),E(0),E(0)];
const G=va(vm(H1,E(13)),vm(F,E(3,-2)));
const Gt=G.slice();Gt[1]=en(Gt[1]);
const Y=[E(0),esc(delta,1,2),E(-5,0,2),esc(delta,2),E(1),E(2)];
const W=[E(0),esc(delta,1,2),E(-5,0,2),esc(delta,2),esc(delta,3),E(4)];
const coords=row=>mm([row],inv.inverse)[0];
const fy=coords(Y),fw=coords(W),fg=coords(G),fgt=coords(Gt);
ck(vs(fw,fy).every((x,i)=>eq(x,E(i===5?2:0))),"actual W-Y=2R3");
ck(eq(fy[0],E(0,-1,4))&&eq(fy[1],E(0,-1,44))&&eq(fy[2],esc(delta,1,2)),"native common shear");
ck(coords(D).every((x,i)=>eq(x,i===0?E(1):i===2?u:E(0))),"D+");
ck(coords(Dt).every((x,i)=>eq(x,i===0?E(1):i===2?en(u):E(0))),"D-");
const heis=[];
for(const N of [36,396]){
 const a=1+N/2,greal=N===36?19:595;
 const perm=Array.from({length:N},(_,j)=>(a*j)%N);
 ck(perm.every((v,j)=>perm[v]===j),"half trace involution");
 for(let j=0;j<N;j++){
  const viaE2=j%2?(j+N/2)%N:j;ck(perm[j]===viaE2,"all E2 columns");
  ck(perm[(perm[j]+1)%N]===(j+a)%N,"full X intertwining");
 }
 ck((greal*greal-1)%N===0&&((greal*greal-1)/N)%2===0,"full Weyl centre");
 heis.push({degree:N,g_mod_2N:greal,permutation_multiplier:a,N_over_4:N/4,third_half_period_cocycle:-1,full_weyl_centre_quotient:(greal*greal-1)/N,square_identity:true});
}
ck(595%8===3&&595%99===1,"g396 CRT");ck(19%8===3&&19%9===1,"g36 CRT");
const cTau=E(-323,-360,343);
return {
 field:"Q(omega), omega^2+omega+1=0; [a,b] means a+b omega",
 input_order:["C","L","M","r","c","d"],metric,
 frame_order:["A","H","L","R1","R2","R3"],frame:frame.map(r=>r.map(out)),inverse:inv.inverse.map(r=>r.map(out)),determinant:out(inv.det),Gram:Gram.map(r=>r.map(out)),
 rows:{J:J.map(out),F:F.map(out),F_tau:Ft.map(out),G:G.map(out),G_tau:Gt.map(out),Y:Y.map(out),W:W.map(out)},
 rows_in_frame:{C:coords(C).map(out),J:coords(J).map(out),D_plus:coords(D).map(out),D_minus:coords(Dt).map(out),E_plus:coords(Eplus).map(out),E_minus:coords(Eminus).map(out),G_plus:fg.map(out),G_minus:fgt.map(out),Y:fy.map(out),W:fw.map(out)},
 actual_degrees:{J:11,deltaA:36,deltaH:396,L:6,R3:8},
 standard_half_characters:{J:"odd: degree2 M plus three odd sigma factors",deltaA:"even: odd33 times odd3",deltaH:"even: odd33 times odd3"},
 heisenberg:heis,
 complete_translation_comparison:{J_A:"delta*t",J_H:"delta*t",v_A:"-t",v_H:"11*t",difference:"12*t=6*alpha for t=alpha/2",odd3_period_character:1,alternating_phase:1},
 actual_core_matrices:{A:[[0,1],[1,0]],H:"-chi11 * X",L:"-I",chi11:"the original odd33 absolute sign; chi11^2=1"},
 overlap:"A,L in p^n; H unit; exactly C,F,F_tau units and D_plus,D_minus in p^n",
 normalized_overlap:"M_n=mu_(n mod2)+chi11*lambda*[kappa]_H mu_(1+n mod2)",
 consecutive_elimination:"M_even-chi11*lambda*[kappa]_H M_odd=(I-lambda^2*[kappa^2]_H)mu0",
 native_test:{u:out(u),G_L:out(fg[2]),G_J:out(E(20,17,11)),Y_common:"Y_R-omega H/44+kappa^n(delta L/2-omega A/4)",W:"Y_common+2 R3",c_tau:out(cTau)},
 no_new_central_zero_for_mu1:true,no_transfer_of_original_Dn_unit_value_to_overlap:true
};
})();
report.ray = {pi_mod_11:"2", g_mod_22:"1", chi11:"the original R454 chi_p, compared by fixed delta pullback", no_new_ray:true};
if (typeof module !== "undefined") module.exports = report;
if (typeof require !== "undefined" && require.main === module) {
  const fs = require("fs");
  const data = JSON.stringify(report, null, 2) + "\n";
  if (process.argv[2]) fs.writeFileSync(process.argv[2], data); else process.stdout.write(data);
}
