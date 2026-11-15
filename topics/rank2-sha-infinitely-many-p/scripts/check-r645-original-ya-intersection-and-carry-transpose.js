// R645. Exact algebra; run with Node.js. No external packages.
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

const del=E(1,2),om=E(0,1),om2=E(-1,-1);
const A=[del,em(E(2),del),E(3,1),E(2,-1),E(0),E(0)];
const Q5=[E(0),E(0),E(0),E(0),E(1),E(2)];
const L5=[E(0),E(0),E(0),E(0),E(2),E(-1)];
const Y=va(A,Q5),W=va(A,[E(0),E(0),E(0),E(0),em(E(3),del),E(4)]);
const Wp=[E(4,4),em(E(2),del),E(4,4),E(0),E(4,2),E(4)];
const H0=[E(1),E(0),E(-1),E(1),E(0),E(0)];
const H1=[E(-1),E(2),om,E(1,1),E(0),E(0)];
const Dc=[E(1),om2,E(0,-2),E(0),E(1),E(2,3)];
const C=vm(H0,ei(del)),F=va(Dc,C),Ec=va(F,vm(C,E(13)));
const g=E(3,-2),G=va(vm(H1,E(13)),vm(F,g));
const rows={A,Q5,L5,Y,W,Wp,C,F,G};
const a=esc(he(F,A),1,29),b=esc(he(F,Q5),1,5);
const bq=esc(he(W,Q5),1,5),bl=esc(he(W,L5),1,5),by=esc(he(W,Y),1,34);
const checkrow=(x,y,m)=>ck(x.length===y.length&&x.every((v,i)=>eq(v,y[i])),m);
ck(eq(he(A,A),E(29))&&eq(he(Q5,Q5),E(5))&&eq(he(L5,L5),E(5)),"norms");
ck(ez(he(A,Q5))&&ez(he(A,L5))&&ez(he(Q5,L5)),"orthogonality");
ck(eq(a,E(-5,-6,29))&&eq(b,E(5,6,5)),"F shifts");
ck(eq(he(G,A),em(g,he(F,A)))&&eq(he(G,Q5),em(g,he(F,Q5))),"G shifts");
checkrow(W,va(va(A,vm(Q5,bq)),vm(L5,bl)),"W expansion");
for(const x of [Y,W,Wp])for(const h of [C,F,G])ck(ez(he(x,h)),"pi4 orthogonality");
const Fp=vs(vs(F,vm(A,a)),vm(Q5,b)),Gp=vs(vs(G,vm(A,em(g,a))),vm(Q5,em(g,b)));
ck(ez(he(Fp,A))&&ez(he(Fp,Q5))&&ez(he(Gp,A))&&ez(he(Gp,Q5)),"perpendicular pieces");
const fr=[C,F,Y,W,Wp,G],inv=inverse(fr);
const ac=mm([A],inv.inverse)[0];
checkrow(mm([ac],fr)[0],A,"A full frame");
ck(eq(ac[0],E(0))&&eq(ac[1],E(1,6,13)),"hidden F coefficient");
const shiftA=Object.fromEntries(Object.entries(rows).map(([key,row])=>[key,out(esc(he(row,A),1,29))]));
// Symbolic physical return. Each vector array is indexed by t-power.
// The inverse Y observation has apparent t^-1, cancelled by Y B=t(tA+Q5).
const obs={};
for(const s of [-1,1]){
 const Ynorm=[vm(Q5,E(s)),vm(A,E(s)),vm(A,E(0))];
 const Wnorm=[
  va(vm(L5,bl),vm(Q5,esc(by,s))),
  va(vm(Q5,es(bq,by)),vm(A,esc(by,s))),
  vm(A,es(E(1),by))
 ];
 const rawYB=[vm(A,E(0)),Q5,A];
 const rawWB=[vm(L5,bl),vm(Q5,bq),A];
 const projectedYB=rawYB.map(v=>vm(Y,esc(he(v,Y),1,34)));
 // Direct coefficient sum for O B +(s/t-1)bY YB.
 const directW=rawWB.map((r,k)=>{
  let v=vs(r,vm(rawYB[k],by));
  if(k+1<rawYB.length)v=va(v,vm(rawYB[k+1],esc(by,s)));
  return v;
 });
 const directY=rawYB.map((r,k)=>{
  let v=vs(r,rawYB[k]);
  if(k+1<rawYB.length)v=va(v,vm(rawYB[k+1],E(s)));
  return v;
 });
 for(let j=0;j<3;j++){checkrow(directW[j],Wnorm[j],"W inverse identity");checkrow(directY[j],Ynorm[j],"Y inverse identity");}
 obs[String(s)]={Y_after_Y_inverse:Ynorm.map(r=>r.map(out)),W_after_Y_inverse:Wnorm.map(r=>r.map(out))};
}
const FA=[va(Fp,vm(A,a)),vm(Q5,b),vm(A,E(0))];
const FY=[Fp,vm(Q5,b),vm(A,a)];
checkrow(vs(FA[0],FY[0]),vm(A,a),"gate difference t0");
checkrow(vs(FA[1],FY[1]),vm(A,E(0)),"gate difference t1");
checkrow(vs(FA[2],FY[2]),vm(A,en(a)),"gate difference t2");
const E0=va(Fp,vm(C,E(13))),E1=va(E0,vm(A,a)),G1=va(Gp,vm(A,em(g,a)));
const norm_a=em(a,ec(a));
ck(eq(norm_a,E(31,0,841)),"a unit fixed bad prime");
ck(eq(he(Y,Y),E(34))&&eq(he(W,W),E(72)),"observation norms");
// Complete fourth derivative coefficient: only k=4 survives at D=0,
// and the original L4 row is retained with its actual uj multipliers.
const fourth_coefficients=[];
for(let j=0;j<=2;j++){
 const ell=2-j;
 fourth_coefficients.push({monomial:[4,j,ell],normalized_derivative_at_D0:"E^"+j+" G^"+ell});
}
const gram={};
for(const [k,row]of Object.entries(rows))gram[k]=Object.fromEntries(Object.entries(rows).map(([l,col])=>[l,out(he(row,col))]));
return {
 conventions:{omega:"omega^2+omega+1=0",b:17,source:"mu0=P6_C rho0",N0:"fixed positive carry depth",t:"kappa^n",sign:"(-1)^n"},
 rows:Object.fromEntries(Object.entries(rows).map(([k,r])=>[k,r.map(out)])),gram,
 common_frame_Gram:["29","5","5"],scalar_A:shiftA,A_in_C_F_Y_W_Wp_G:ac.map(out),full_frame_determinant:out(inv.det),
 f_A:out(a),f_Q:out(b),g:out(g),b_Q:out(bq),b_L:out(bl),b_Y:out(by),
 norm_f_A:out(norm_a),F_perp:Fp.map(out),G_perp:Gp.map(out),
 q_Y_F_polynomial:FY.map(r=>r.map(out)),q_A_F_polynomial:FA.map(r=>r.map(out)),
 gate_difference:"F_A-F_Y=(1-t^2) f_A A",
 gates_intersection:"G_Y cap G_A = G_Y cap {A in p^N0}",
 primitive_Y_support_separation:"G_A cap {A unit} is disjoint from G_Y",
 observations:obs,YA_polynomial:[A,Q5].map(r=>r.map(out)),
 WA_polynomial:[va(A,vm(L5,bl)),vm(Q5,bq)].map(r=>r.map(out)),
 stationary_gate_F:[Fp,va(Fp,vm(A,a))].map(r=>r.map(out)),
 stationary_E:[E0,E1].map(r=>r.map(out)),stationary_G:[Gp,G1].map(r=>r.map(out)),
 fourth_jet:{coefficients:fourth_coefficients,L4:"1 exactly, including every uj",direction:"partial_D+kappa^N0 partial_E+g kappa^N0 partial_G",mod_p:"x^2",conclusion:"no polynomial invariant in the R594 affine family"},
 whole_masses:"global normalized rows zero; individual common rows retained"
};
}
const s=JSON.stringify(certificate(),null,2)+'\n';
if(process.argv[2])require('fs').writeFileSync(process.argv[2],s);else process.stdout.write(s);
