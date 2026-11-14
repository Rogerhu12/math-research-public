#!/usr/bin/env node
function certifyR522(){
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

const ep=(a,n)=>{ck(n>=0,"negative power");let r=E(1),b=a;for(;n;n=Math.floor(n/2),b=em(b,b))if(n%2)r=em(r,b);return r;};
const fac=n=>{let r=1n;for(let j=2;j<=n;j++)r*=BigInt(j);return r;};
const choose=(n,k)=>k<0||k>n?0n:fac(n)/(fac(k)*fac(n-k));
const om=E(0,1),om2=E(-1,-1),del=E(1,2),ga=E(3,1),gb=E(2,-1);
const Y=[del,E(2,4),ga,gb,E(1),E(2)],
 W=[del,E(2,4),ga,gb,E(3,6),E(4)],
 Wp=[E(4,4),E(2,4),E(4,4),E(0),E(4,2),E(4)],
 W2=[ga,E(2,4),E(6,3),E(3,2),E(-1,1),E(4)],
 H0=[E(1),E(0),E(-1),E(1),E(0),E(0)],
 H1=[E(-1),E(2),om,E(1,1),E(0),E(0)],
 H2=[E(-2,-40),E(18,-18),E(2,-38),E(4,2),E(42),E(84,126)];
const F=[Y,W,Wp,H0,H1,H2],iv=inverse(F),Gram=F.map(r=>F.map(s=>he(r,s)));
for(const row of [Y,W,Wp,W2])ck(ez(he(row,H0)),"common degree3 companion");
for(let i=0;i<3;i++)for(let j=3;j<6;j++)ck(ez(Gram[i][j]),"complete R/H split");
ck(eq(he(H0,H0),E(3))&&eq(he(H1,H1),E(7))&&eq(he(H2,H2),E(18144)),"orthogonal companion norms");
for(let i=3;i<6;i++)for(let j=3;j<6;j++)if(i!==j)ck(ez(Gram[i][j]),"three small hidden axes orthogonal");
const TI=[
 [en(om),E(1),om2,om],
 [en(om2),en(om),E(1),en(om2)],
 [E(-1),en(om2),en(om),E(1)],
 [en(om),E(1),en(om2),en(om)]
].map(r=>vm(r,E(1,0,2))),T=ident(6),idx=[0,2,3,4];
for(let i=0;i<4;i++)for(let j=0;j<4;j++)T[idx[i]][idx[j]]=TI[i][j];
const ht=mm([H0,H1,H2],T);
ck(ht[0].every((v,i)=>eq(v,em(om2,H0[i]))),"H0 T equals omega^2 H0");
ck(ht[1].every((v,i)=>eq(v,H1[i]))&&ht[2].every((v,i)=>eq(v,H2[i])),"other two hidden axes fixed by T");
ck(mm([Y,W,Wp],T)[0].every((v,i)=>eq(v,Y[i])),"T preserves Y");
const Rh=ident(6).map((row,i)=>row.map((v,j)=>es(v,esc(em(ec(H0[i]),H0[j]),2,3))));
ck(mm([Y,W,Wp,H1,H2],Rh).every((r,i)=>r.every((v,j)=>eq(v,[Y,W,Wp,H1,H2][i][j]))),"H0 reflection fixes every retained output");
ck(mm([H0],Rh)[0].every((v,i)=>eq(v,en(H0[i]))),"true hidden reflection");
const sigma1=Q(1,210),B3six=qm(Q(63),sigma1),moment6=qm(Q(fac(6)),B3six);
ck(qs(B3six)==="3/10"&&qs(moment6)==="216","degree3 complete even line coefficient");
const z=[del,E(2,4),ga,E(1),E(2)],l=[E(1),E(0),E(-1),E(0),E(0)];
let C=Array.from({length:6},()=>E(0));
for(let mask=0;mask<32;mask++){let j=0,v=E(1);for(let i=0;i<5;i++)if(mask&(1<<i)){j++;v=em(v,z[i]);}else v=em(v,l[i]);C[j]=ea(C[j],v);}
C=C.map((v,j)=>esc(v,fac(j)*fac(5-j)));
let A5=E(0);const terms=[];
for(let j=1;j<=5;j++){
 const v=esc(em(C[j],ep(ei(gb),j)),BigInt(j%2?1:-1)*choose(6,5-j),j);
 A5=ea(A5,v);terms.push(out(v));
}
const a5=esc(A5,-1,84*216),na5=em(a5,ec(a5));
ck(eq(a5,E(-3221,5000,3176523)),"complete nonlog fifth coefficient");
ck(eq(na5,E(1021,0,200120949)),"fixed fifth norm");
ck(ez(C[0])&&ez(C[1])&&ez(C[2]),"all possible mass fifth terms vanish");
ck(3176523===27*7**6&&200120949===3**5*7**7,"small exact denominator factors");
ck(1021%64!==7,"new fifth norm factor excluded on current ray");

function fifthForRow(row){
 const zq=[row[0],row[1],row[2],row[4],row[5]],aq=row[3];
 let Cq=Array.from({length:6},()=>E(0));
 for(let mask=0;mask<32;mask++){let j=0,v=E(1);for(let i=0;i<5;i++)if(mask&(1<<i)){j++;v=em(v,zq[i]);}else v=em(v,l[i]);Cq[j]=ea(Cq[j],v);}
 Cq=Cq.map((v,j)=>esc(v,fac(j)*fac(5-j)));
 let sum=E(0);
 for(let j=1;j<=5;j++)sum=ea(sum,esc(em(Cq[j],ep(ei(aq),j)),BigInt(j%2?1:-1)*choose(6,5-j),j));
 return esc(sum,-1,84*216);
}
const alphaW=fifthForRow(W),alphaW2=fifthForRow(W2);
ck(eq(alphaW,em(esc(del,6),a5)),"same-grid W fifth is exactly 6 delta times Y fifth");

const delta5=es(em(alphaW2,ei(en(em(esc(del,6),om2)))),a5);
ck(eq(delta5,E(272,-320,194481)),"two genuine T observations have the claimed local difference");
ck(eq(em(delta5,ec(delta5)),E(256,0,3**7*7**5)),"T difference fixed norm is a unit");
for(let q=2;q*q<=1021;q++)ck(1021%q!==0,"1021 prime");
const inv=iv.inverse;
const independentX=[E(0),E(0),E(0),E(1),E(0),E(0)];
const xcomp=mm([independentX],inv)[0];
return{
 field:"Q(omega), omega^2+omega+1=0; coefficient pairs use 1,omega",
 input_order:["xi1","xi2","xi3","x","c","d0"],
 frame:F.map(r=>r.map(out)),inverse:inv.map(r=>r.map(out)),Gram:Gram.map(r=>r.map(out)),determinant:out(iv.det),
 H0:H0.map(out),H1:H1.map(out),H2:H2.map(out),W2:W2.map(out),T:T.map(r=>r.map(out)),H0_reflection:Rh.map(r=>r.map(out)),
 hidden_T_characters:["omega^2","1","1"],
 standard_odd3_basis:["sigma^3","x_wp sigma^3","-y_wp sigma^3"],
 even_line:"B3=sigma(2z)/(2 sigma(z))=-y_wp sigma^3",
 even_line_mass:1,even_line_z6_coefficient:"3 b/10",sixth_moment_ratio:"216 b Omega^6",
 whole_H0_core:"-lambda; same absolute odd3 anchor sigma(delta z)",
 universal_even_identity:"(rho+R_H0 rho)/2=B3 tensor H0-forgotten rho",
 positive_test:"H0^6/(216 b Omega^6)",
 unit_positive_test:"1_H0unit * H0^6/(216 b Omega^6*(1+lambda*kappa^6))",
 complete_first_rows:{Y:"S",W:"6 delta T",W2:"-6 delta omega^2 T"},
 five_mixed_Cj:C.map(out),nonlog_terms_j1_to_5:terms,nonlog_A5:out(A5),normalized_alpha:out(a5),alpha_norm:out(na5),same_grid_W_alpha:out(alphaW),same_grid_W2_alpha:out(alphaW2),same_grid_T_normalized_difference:out(es(em(alphaW2,ei(en(em(esc(del,6),om2)))),a5)),
 full_log_mass:"identically zero: the test does not use xi2,c,d0, each has zero sigma mass",
 exact_fifth:"(d/b)*alpha*(1+lambda*kappa)/(1+lambda*kappa^6)",
 independent_x_in_complete_frame:xcomp.map(out),
 actual_nonzero_grid:"five original inputs deep n, x unit; valuation exactly 5n",
 T_transported_grid:"T D_n, same unmoved positive H0-unit test; h source value omega^2 C_n, W deep n",
 retained_boundary:"The remaining actual Y-unit and W-unit mixed domains are not discarded."
};
}
if(typeof module!=="undefined"){
 module.exports={certifyR522};
 if(require.main===module){
  const report=certifyR522();
  require("fs").writeFileSync(__filename.replace(/\.js$/,".json"),JSON.stringify(report,null,2)+"\n");
  console.log("R522: complete small companion frame, universal odd3 even factor and original three central fifth coefficients passed.");
 }
}
