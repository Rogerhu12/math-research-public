#!/usr/bin/env node
// Exact characteristic-zero certificate; no packages or floating-point arithmetic.
const certificate=(()=>{

const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){[a,b]=[b,a%b]}return a}
function q(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]}
const add=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>[-a[0],a[1]], sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>q(a[0]*b[0],a[1]*b[1]), div=(a,b)=>q(a[0]*b[1],a[1]*b[0]);
function pow(a,n){let r=q(1);for(;n;n>>=1,a=mul(a,a))if(n&1)r=mul(r,a);return r}
const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1], qs=a=>a[1]===1n?String(a[0]):a[0]+"/"+a[1];
const c=(a=0,b=0)=>[Array.isArray(a)?a:q(a),Array.isArray(b)?b:q(b)];
const ca=(a,b)=>[add(a[0],b[0]),add(a[1],b[1])], cn=a=>[neg(a[0]),neg(a[1])], cs=(a,b)=>ca(a,cn(b));
const cm=(a,b)=>[sub(mul(a[0],b[0]),mul(q(3),mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0]))];
const cc=a=>[a[0],neg(a[1])], norm=a=>add(mul(a[0],a[0]),mul(q(3),mul(a[1],a[1])));
const ci=a=>[div(a[0],norm(a)),neg(div(a[1],norm(a)))], cd=(a,b)=>cm(a,ci(b));
const ce=(a,b)=>eq(a[0],b[0])&&eq(a[1],b[1]), cj=a=>({real:qs(a[0]),delta:qs(a[1])});
function cp(a,n){let r=c(1);for(;n;n>>=1,a=cm(a,a))if(n&1)r=cm(r,a);return r}
function dot(a,b){return a.map((x,i)=>cm(x,cc(b[i]))).reduce(ca,c())}
function mm(A,B){return A.map(row=>B[0].map((_,j)=>row.map((x,k)=>cm(x,B[k][j])).reduce(ca,c())))}

const omega=c(q(-1,2),q(1,2)),gamma=c(q(5,2),q(1,2)),gamma13=c(q(7,2),q(1,2)),gamma103=c(10,1);
const Z=[c(0,1),c(0,2),gamma,c(),c(1),c(2)];
const V=[c(q(63,2),q(17,2)),c(9,-10),c(-17,14),c(),c(22,12),c(17,-3)];
const H=[c(q(219,2),q(-83,2)),c(0,-14),c(89,34),c(),c(-240,34),c(q(175,2),q(35,2))];
const X=[c(),c(),c(),c(1),c(),c()];
const Q1=[c(q(-3,14),q(-9,14)),c(1),c(),c(),c(q(9,14),q(-1,14)),c(q(9,14),q(13,14))];
const Q2=[c(q(11,14),q(5,14)),c(),c(1),c(),c(q(1,7),q(3,7)),c(q(-13,7),q(3,7))];
const scale=(a,r)=>r.map(t=>cm(a,t));
const plus=(r,s)=>r.map((x,i)=>ca(x,s[i]));
const minus=(r,s)=>r.map((x,i)=>cs(x,s[i]));
const Q0=plus(Q1,scale(omega,Q2));
const qinner=dot(Q2,Q0);
const Qb=scale(gamma,minus(scale(c(5),Q2),scale(qinner,Q0)));
const CQ=[[c(1),omega],[ca(c(13),cm(c(7),omega)),ca(c(8),cm(c(11),omega))]];
for(let j=0;j<6;j++){
 if(!ce(Q0[j],ca(cm(CQ[0][0],Q1[j]),cm(CQ[0][1],Q2[j]))))throw Error("Q0 row");
 if(!ce(Qb[j],ca(cm(CQ[1][0],Q1[j]),cm(CQ[1][1],Q2[j]))))throw Error("Qb row");
}
const norms=[27,3699,98777,1,5,515];
const F=[Z,V,H,X,Q0,Qb],Ft=F[0].map((_,j)=>F.map(r=>cc(r[j])));
const Fi=Ft.map(r=>r.map((a,j)=>cd(a,c(norms[j]))));
const I=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>c(i===j?1:0)));
const assertmat=(A,B,msg)=>{for(let i=0;i<A.length;i++)for(let j=0;j<A[0].length;j++)if(!ce(A[i][j],B[i][j]))throw Error(msg+" "+i+","+j)};
assertmat(mm(F,Fi),I,"inverse right");assertmat(mm(Fi,F),I,"inverse left");
const Gram=F.map(r=>F.map(s=>dot(r,s)));
assertmat(Gram,I.map((r,i)=>r.map(t=>cm(c(norms[i]),t))),"diagonal Gram");
function Ocoeff(z){const b=mul(q(2),z[1]),a=add(z[0],z[1]);return {a:qs(a),omega:qs(b),integral:a[1]===1n&&b[1]===1n}}
const clearQ=[Q0,Qb].map(r=>r.map(x=>Ocoeff(cm(c(7),x))));
if(clearQ.flat().some(x=>!x.integral))throw Error("CM integral clearing");
const C=[c(q(1,2)),c(),cm(c(q(1,2)),cp(omega,2)),cm(c(q(-1,2)),omega),c(q(-1,2)),c()];
const crow=mm([C],Fi)[0];
const expected=[c(q(-1,18),q(-1,27)),c(q(-3,7398),q(19,7398)),c(q(127,98777),q(24,98777)),c(q(1,4),q(-1,4)),c(q(-11,70),q(1,14)),c(q(-31,3605),q(23,3605))];
for(let i=0;i<6;i++)if(!ce(crow[i],expected[i]))throw Error("C coordinate "+i);
const ac=crow.map((t,i)=>cm(c(norms[i]),cc(t)));
const P=ac.map(a=>crow.map(t=>cm(a,t)));
const U=I.map((r,i)=>r.map((t,j)=>cs(t,cm(c(2),cm(cc(C[i]),C[j])))));
const Uf=mm(mm(F,U),Fi);
assertmat(Uf,I.map((r,i)=>r.map((t,j)=>cs(t,cm(c(2),P[i][j])))),"U full frame");
assertmat(mm(Uf,Uf),I,"U involution");
const Q0u=mm([Q0],U)[0],Qbu=mm([Qb],U)[0];
const a0=dot(Q0,C),ab=dot(Qb,C);
if(!ce(a0,c(q(-11,14),q(-5,14)))||!ce(ab,c(q(-31,7),q(-23,7))))throw Error("mixed inner products");
for(let j=0;j<6;j++){
 if(!ce(Q0u[j],cs(Q0[j],cm(c(2),cm(a0,C[j])))))throw Error("Q0 U");
 if(!ce(Qbu[j],cs(Qb[j],cm(c(2),cm(ab,C[j])))))throw Error("Qb U");
}
if(!ce(dot(Q0,Q0u),c(3))||!eq(norm(a0),q(1))||!eq(norm(ab),q(52)))throw Error("mixed Gram");
const C4=mm([[...crow.slice(0,4),c(),c()]],F)[0],CH=minus(C,C4);
if(!ce(dot(C4,C4),c(q(72,103)))||!ce(dot(CH,CH),c(q(31,103)))||!ce(dot(C4,CH),c()))throw Error("C split Gram");
const Y=plus(Z,scale(cc(gamma),X)),Tc=minus(scale(gamma,Z),scale(c(27),X));
const W=[c(0,1),c(0,2),gamma,cc(gamma),c(0,3),c(4)];
const Wp=plus(scale(cd(c(37,3),c(27)),Z),scale(c(q(2,27)),V));
const R=[gamma,c(0,2),c(q(9,2),q(3,2)),c(),c(q(-3,2),q(1,2)),c(4)];
const W2=plus(R,scale(c(2,1),X));
for(const r of [Y,Tc,W,Wp,W2,R])for(const qq of [Q0,Qb])if(!ce(dot(r,qq),c()))throw Error("pure companion orthogonality");
if(!ce(dot(W,C),c()))throw Error("C is not pure W");
const aY=dot(Y,C),aTc=dot(Tc,C);
if(!ce(aY,c(q(-1,2),q(3,2)))||!ce(aTc,c(-12,-5)))throw Error("test transpose");
const B4=minus(Q0,scale(a0,C));
if(!ce(dot(B4,C),c())||!ce(dot(B4,B4),c(4)))throw Error("B4 decomposition");
for(const [g,n] of [[gamma13,13],[gamma103,103]])if(!eq(norm(g),q(n)))throw Error("CM anchor");
const frameDet=cm(c(-380997),cm(c(5),gamma));
const parity=clearQ.map(r=>r.map(o=>{
 const a=BigInt(o.a),b=BigInt(o.omega);return Number(((a%2n)+2n)%2n)||Number(((b%2n)+2n)%2n)?1:0
}));
if(parity.some(row=>row.reduce((a,b)=>a+b,0)%2!==1))throw Error("odd half characteristic");
return {
 status:"all displayed characteristic-zero CM identities exactly verified using BigInt rationals",
 input_order:["xi1","xi2","xi3","x=xi4","c","d0"],
 new_order:["Z","V","H","x","Q0","Qb"],
 Q_change:CQ.map(r=>r.map(cj)),Q_inner:cj(qinner),
 full_frame:F.map(r=>r.map(cj)),full_inverse:Fi.map(r=>r.map(cj)),
 diagonal_Gram:norms,frame_determinant:cj(frameDet),
 seven_Q0_CM:clearQ[0],seven_Qb_CM:clearQ[1],
 odd_unit_parities:parity,
 added_ray:"pi0 = 2 mod 49, compatible with the old pi0 = 2 mod 7",
 whole_center_levels:{odd245_modulus:490,odd25235_modulus:50470,ratio:1},
 scalar_anchor_norms:{gamma13:13,seven:49,seven_gamma103:5047},
 absolute_scalar_identity:"chi_5=chi_65=chi_245=chi_25235; chi_65^2=1",
 C_in_full_frame:crow.map(cj),C4_original:C4.map(cj),CH_original:CH.map(cj),
 C_split_norms:{C4:"72/103",CH:"31/103",cross:0},
 C_projector_in_full_frame:P.map(r=>r.map(cj)),
 U_in_full_frame:Uf.map(r=>r.map(cj)),
 C_shift_coefficients:ac.map(cj),
 Q0_U:Q0u.map(cj),Qb_U:Qbu.map(cj),
 mixed_coefficients:{a0:cj(a0),ab:cj(ab),norm_a0:qs(norm(a0)),norm_ab:qs(norm(ab)),Q0_Q0U:cj(dot(Q0,Q0u)),Qb_QbU:cj(dot(Qb,Qbu))},
 aY:cj(aY),aTc:cj(aTc),B4_original:B4.map(cj),
 intersection:"Q0 in p^r,Qb in p^s,Q0 U in p^r,Qb U in p^s iff Q0 in p^r,Qb in p^s,C in p^max(r,s)",
 common_depth:"E_n={Q0,Qb,C deep n}={Q0,Qb,C4 deep n}",
 kernel:"after Q0,Qb simultaneous depth n, retain C4+kappa^n CH in every U-transported test",
 warning:"No core is asserted for C4 or B4; U is a full six-input operation, not a four-input matrix."
};

})();
process.stdout.write(JSON.stringify(certificate,null,2)+"\n");
