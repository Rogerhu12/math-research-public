"use strict";
// Exact Q(delta) geometry and normal-jet coefficients for R567.
// No finite-prime nonvanishing inference is made.
const result=(function(){
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


const w=(a=0,b=0)=>c(q(2*a-b,2),q(b,2)), zero=c(),one=c(1),delta=c(0,1);
const va=(a,b)=>a.map((x,i)=>ca(x,b[i])),vs=(a,b)=>a.map((x,i)=>cs(x,b[i])),vm=(a,b)=>a.map(x=>cm(x,b));
const D=[w(1),w(-1,-1),w(0,-2),w(),w(1),w(2,3)], C=vm([one,zero,c(-1),one,zero,zero],ci(delta));
const F=va(D,C),E=va(F,vm(C,c(13))),G=va(vm([w(-1),w(2),w(0,1),w(1,1),w(),w()],c(13)),vm(F,w(3,-2)));
const Y=[delta,cm(c(2),delta),w(3,1),w(2,-1),one,c(2)],W=[delta,cm(c(2),delta),w(3,1),w(2,-1),cm(c(3),delta),c(4)];
const Wp=[w(4,4),w(2,4),w(4,4),w(),w(4,2),w(4)];
const cr=[zero,zero,zero,zero,one,zero],dr=[zero,zero,zero,zero,zero,one];
const X=vs(cr,vm(D,c(q(1,14)))),Z=va(dr,vm(D,cd(w(1,3),c(14))));
const V=[w(1,1),w(0,-1),w(2),zero,w(0,-2),w(0,-2)];
const uc=vm(va(vm(cr,w(0,-1)),vm(dr,w(1,-1))),c(q(1,2)));
const gamma=w(3,1),gammabar=w(2,-1);
const identity=vs(vm(va(uc,vm(D,cd(w(2,3),c(14)))),c(14)),vm(V,gamma));
const Id=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>c(i===j?1:0)));
const H=Id.map(r=>r.slice());H[4][4]=cd(w(-1,-1),c(2));H[4][5]=cd(w(-1,-2),c(2));H[5][4]=cd(w(2,1),c(2));H[5][5]=cd(w(-1,-1),c(2));
const Rc=Id.map(r=>r.slice());Rc[4][4]=c(-1);
const Sc=Id.map((r,i)=>r.map((x,j)=>ca(x,cm(w(-1,1),cm(cc(C[i]),C[j])))));
const proj=(r,v)=>vs(r,vm(v,cd(dot(r,v),dot(v,v))));
const coeff=r=>cd(dot(r,V),c(14));
const axisRows={D,E,G,Y,W,Wprime:Wp,X,Z,L:va(vm(cr,w(1,3)),dr),C};
const coeffs=Object.fromEntries(Object.entries(axisRows).map(([k,r])=>[k,cj(coeff(r))]));
function parityNonzero(z){const aw=sub(z[0],z[1]),bw=mul(q(2),z[1]);if(aw[1]!==1n||bw[1]!==1n)throw Error("nonintegral axis");return (aw[0]%2n!==0n||bw[0]%2n!==0n)?1:0;}
let Vs=V,conjugates=[];
for(let j=0;j<3;j++){const VH=mm([Vs],H)[0];conjugates.push({j,V:Vs.map(cj),VH:VH.map(cj),norm:cj(dot(Vs,Vs)),odd:Vs.reduce((s,z)=>s+parityNonzero(z),0),oddH:VH.reduce((s,z)=>s+parityNonzero(z),0)});Vs=mm([Vs],Sc)[0];}
const up=vm(va(vm(cr,w(0,1)),vm(dr,w(1,-1))),c(q(1,2))),U=vs(vm(up,c(7)),vm(D,w(-1,-1)));

const KK=[w(1,1),w(0,-1),w(2),zero,w(-3,3),w(3)];
const u=up;
const R1=Id.map((row,i)=>row.map((v,j)=>cs(v,cm(c(2),cm(cc(u[i]),u[j])))));
const D1=mm([D],R1)[0], V1=mm([V],R1)[0];
const projected=Object.fromEntries(Object.entries({E,G,Y,W,Wprime:Wp,K:KK}).map(([k,r])=>[k,proj(r,V)]));
for(const [k,r] of Object.entries(projected)){
 if(!ce(dot(r,D),zero)||!ce(dot(r,V),zero))throw Error("companion "+k);
 if(!ce(r[4],cm(w(-1,1),r[5])))throw Error("pair ratio "+k);
 const z=mm([r],R1)[0];
 if(!ce(z[4],zero)||!ce(z[5],cm(c(-2),r[5])))throw Error("reflection elimination "+k);
 for(let j=0;j<4;j++)if(!ce(z[j],r[j]))throw Error("first four moved");
}
const commutes=mm(R1,Sc).every((row,i)=>row.every((v,j)=>ce(v,mm(Sc,R1)[i][j])));
const Lp=proj(axisRows.L,V), lK=cd(dot(Lp,KK),c(42));
const nullPair=va(vm(D,w(0,1)),V);
const nullReflection=mm([nullPair],R1)[0];
const expectedD=[...D.slice(0,4),w(3,2),w(0,-1)];
const expectedV=[...V.slice(0,4),w(-1,-3),w(1)];
if(!D1.every((v,i)=>ce(v,expectedD[i]))||!V1.every((v,i)=>ce(v,expectedV[i])))throw Error("normal coefficients");
const negative={
basis:"a+b delta",R1:R1.map(r=>r.map(cj)),R1commutesPureC:commutes,
Dreflected:D1.map(cj),Vreflected:V1.map(cj),
companions:Object.fromEntries(Object.entries(projected).map(([k,r])=>[k,{original:r.map(cj),reflected:mm([r],R1)[0].map(cj)}])),
LprojectedOverK:cj(lK),Lidentity:Lp.every((v,i)=>ce(v,cm(lK,KK[i]))),
sigma_moments_through_seven:{0:0,1:"Omega",2:0,3:0,4:0,5:0,6:0,7:"24*b*Omega^7"},
polynomial_source_operator:"(3+2omega)*Omega*d/dD",
V_polynomial_source_operator:"(-1-3omega)*Omega*(P-T*P_D)+24*b*Omega^7*(-1-3omega)*(3+2omega)^6*P6",
zero_mass_reflected_marginal:true,normal_sigma_coefficients:{aD:cj(D1[4]),aV:cj(V1[4]),aDnorm:cj(cm(D1[4],cc(D1[4]))),aD6:cj(cp(D1[4],6)),seventh_correction:cj(cm(V1[4],cp(D1[4],6)))},reflected_normal_relation:D1.every((v,i)=>i===4||ce(V1[i],cm(w(1,1),v)))
};
const Paxis=vs(up,vm(D,cd(w(-1,-1),c(7))));
const Zstar=vs(Z,vm(Paxis,cd(w(8,3),c(10))));
const pp=(r)=>proj(r,Paxis);
const positiveRows=Object.fromEntries(Object.entries({E,G,Y,W,Wprime:Wp,Zstar}).map(([k,r])=>[k,pp(r)]));
const DH=mm([D],H)[0],PH=mm([Paxis],H)[0];
for(const [k,r] of Object.entries(positiveRows)){
 if(!ce(dot(r,D),zero)||!ce(dot(r,Paxis),zero))throw Error("positive companion "+k);
 const rh=mm([r],H)[0];
 if(!ce(rh[4],zero))throw Error("positive sigma elimination "+k);
}
const Tp=[...D.slice(0,4),zero,w(0,-2)];
const Tm=[...D.slice(0,4),zero,w(0,-1)];
if(!ce(DH[4],w(0,2))||!ce(PH[4],c(q(5,7))))throw Error("positive scalar");
if(!DH.every((v,i)=>i===4||ce(v,Tp[i])))throw Error("positive normal T");
if(!PH.every((v,i)=>i===4||ce(v,cm(cd(w(1,1),c(7)),Tp[i]))))throw Error("positive normal P");
if(!ce(dot(Tp,Tp),c(10))||!ce(dot(Tm,Tm),c(7)))throw Error("norm T");
const sourceFrames=[];
let tm=Tm,tp=Tp;
for(let j=0;j<3;j++){
 const minusOdd=tm.reduce((n,z)=>n+parityNonzero(z),0),plusOdd=tp.reduce((n,z)=>n+parityNonzero(z),0);
 if(minusOdd%2!==1||plusOdd%2!==0)throw Error("source half-character");
 sourceFrames.push({j,T7:tm.map(cj),T10:tp.map(cj),minusOdd,plusOdd});
 tm=mm([tm],Sc)[0];tp=mm([tp],Sc)[0];
}
const f7mass=add(add(mul(q(-1,7),q(2)),q(2,7)),q(7,210));
const f10mass=add(mul(q(-1,7),q(5)),q(10,210));
if(!eq(f7mass,q(1,30))||!eq(f10mass,q(-2,3)))throw Error("theta mass coefficients");
const negMassConstant=cm(c(24),cm(V1[4],cs(cp(D1[4],6),c(5))));
const plusMassConstant=cm(w(-1,-1),c(q(11040,7)));
return {
negative,sourceFrames,
positive:{Paxis:Paxis.map(cj),Zstar:Zstar.map(cj),DH:DH.map(cj),PH:PH.map(cj),
T10:Tp.map(cj),T7:Tm.map(cj),
companions:Object.fromEntries(Object.entries(positiveRows).map(([k,r])=>[k,{row:r.map(cj),Hrow:mm([r],H)[0].map(cj)}])),
movement:Object.fromEntries(Object.entries({E,G,Y,W,Wprime:Wp}).map(([k,r])=>[k,cj(cd(dot(r,Paxis),dot(Paxis,Paxis)))])),
normal_source_phase:cj(w(-1,-1))},
theta_coefficients:{S7_mass_z6:qs(f7mass),S7_m6:"24*b*Omega^6*Lambda0",S10_mass_z6:qs(f10mass),S10_m6:"Omega^6*(720*Lambda6-480*b*Lambda0)"},
fixed_mass_coefficients:{negative:cj(negMassConstant),positive:cj(plusMassConstant),negative_a6_minus5_norm:qs(norm(cs(cp(D1[4],6),c(5))))},
full_native:"beta^(n+1)/(b*Omega^6)*(chi*Fplus(kappa)+Fminus(kappa))",
full_native_first_two_rows:"beta^(n+1)/(b*Omega^6)*(C0+kappa*C1) mod p^2",
remaining_nonzero_test:"C0/p+lambda^2*C1 mod p"
};
})();
console.log(JSON.stringify(result,null,2));
