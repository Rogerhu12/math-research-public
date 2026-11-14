#!/usr/bin/env node
// Exact original-source joint identity and complete fifth-order/mass certificate.
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

const g31=c(2,3),BH=scale(c(103),CH),DH=minus(scale(c(31),Q0),scale(a0,BH));
if(!ce(dot(BH,BH),c(3193))||!ce(dot(DH,DH),c(1612))||!ce(dot(BH,DH),c()))throw Error("hidden orthogonal basis");
if(!eq(norm(g31),q(31)))throw Error("gamma31");
const BHcm=BH.map(Ocoeff);if(BHcm.some(o=>!o.integral))throw Error("BH nonintegral");
const odd=BHcm.reduce((s,o)=>s+(BigInt(o.a)%2n!==0n||BigInt(o.omega)%2n!==0n?1:0),0);
if(odd!==5)throw Error("BH odd character");
const Bcoeff=crow.slice(4).map(t=>cm(c(103),t));
const hidden_change=[Bcoeff,[cs(c(31),cm(a0,Bcoeff[0])),cn(cm(a0,Bcoeff[1]))]];
const hdet=cs(cm(hidden_change[0][0],hidden_change[1][1]),cm(hidden_change[0][1],hidden_change[1][0]));
if(!eq(norm(hdet),q(49972,25)))throw Error("hidden common-domain determinant");
const inds=[0,2,3,4],o2=cp(omega,2);
const TI=[
[cn(omega),c(1),o2,omega],
[cn(o2),cn(omega),c(1),cn(o2)],
[c(-1),cn(o2),cn(omega),c(1)],
[cn(omega),c(1),cn(o2),cn(omega)]
].map(r=>scale(c(q(1,2)),r));
const TT=I.map(r=>r.slice());for(let i=0;i<4;i++)for(let j=0;j<4;j++)TT[inds[i]][inds[j]]=TI[i][j];
assertmat(mm(mm(TT,TT),TT),I,"T cubic");
const D=minus(scale(c(31),C),BH),AA=plus(D,scale(c(72),C));
const Ct=mm([C],TT)[0],Dt=mm([D],TT)[0],At=mm([AA],TT)[0];
assertmat([Ct],[scale(o2,X)],"C independent sigma after T");
if(!ce(Dt[3],c())||!ce(dot(D,D),c(2232))||!ce(dot(D,C),c()))throw Error("five sigma D");
if(!ce(dot(AA,AA),c(7416))||!ce(dot(AA,BH),c()))throw Error("total companion Gram");
const Dcm=Dt.map(Ocoeff),Acm=At.map(Ocoeff);
if(Dcm.concat(Acm).some(o=>!o.integral))throw Error("h source integral axes");
const normalized=[c(30),c(0,21),c(1),c(1),gamma],units=[omega,o2,cn(omega),c(1),cn(o2)],five=[0,1,2,4,5];
for(let j=0;j<5;j++)if(!ce(Dt[five[j]],cm(units[j],normalized[j])))throw Error("sigma unit factor");
if(!ce(units.reduce(cm,c(1)),c(1)))throw Error("five sigma phase");
const pair=[[c(1),c(72)],[c(-1),c(31)]],pairinv=[[c(q(31,103)),c(q(-72,103))],[c(q(1,103)),c(q(1,103))]];
assertmat(mm(pair,pairinv),[[c(1),c()],[c(),c(1)]],"A B pair inverse");
const kB=cd(cm(c(34),omega),c(103)),Th=minus(scale(gamma,Y),scale(cm(c(34),omega),C));
const Krow=minus(scale(gamma,Y),scale(kB,AA));
if(!ce(dot(Th,Y),c())||!ce(dot(Krow,Y),c())||!ce(dot(Krow,BH),c()))throw Error("known arithmetic companion");
for(let j=0;j<6;j++)if(!ce(Th[j],cs(Krow[j],cm(kB,BH[j]))))throw Error("Th decomposition");
function im(x,m){x%=m;return x<0n?x+m:x}
function invm(x,m){for(let t=1n;t<m;t++)if(im(x*t,m)===1n)return t;throw Error("no inverse")}
function cr(a,m,b,n){return im(a+m*im((b-a)*invm(m,n),n),m*n)}
function wm2(a,b,m){return [im(a[0]*b[0]-a[1]*b[1],m),im(a[0]*b[1]+a[1]*b[0]-a[1]*b[1],m)]}
const centers=[31,103].map(s=>{
 const n=72*s,m=BigInt(2*n),g=[cr(91n,144n,1n,BigInt(s)),cr(72n,144n,0n,BigInt(s))],gg=wm2(g,g,m);
 if(gg[0]!==BigInt(1+n)||gg[1]!==0n)throw Error("full square center "+s);
 return {N:n,modulus:String(m),g:g.map(String),g_squared:gg.map(String),Theta_anchor_norm:36*s}
});
const H0=[c(1),c(),c(-1),c(1),c(),c()];


const eta=cd(cs(c(1),omega),c(103)),E0=minus(H0,scale(eta,BH));
if(!ce(dot(E0,E0),c(q(216,103)))||!ce(dot(E0,BH),c())||!ce(dot(E0,DH),c()))throw Error("new companion frame");
const pi=[Y,W,Wp,DH];
for(const r of pi)for(const a of [H0,BH,E0])if(!ce(dot(r,a),c()))throw Error("whole four-output moment frame");
const Er=minus(minus(mm([Q0],TT)[0],scale(c(q(7,10),q(-1,10)),Q0)),scale(c(q(-12,515),q(-2,515)),Qb));
const eunit=c(q(-1,7),q(4,7));
assertmat([Er],[scale(eunit,E0)],"root E normalization");
if(!eq(norm(eunit),q(1)))throw Error("root E unit norm");
const pA=AA.map(a=>AA.map(t=>cd(cm(cc(a),t),c(7416))));
const shifts=pi.map(r=>cd(dot(r,AA),c(7416))),eshift=cd(dot(E0,AA),c(7416));
if(!ce(shifts[1],c())||!ce(shifts[3],c()))throw Error("old W DH should remain fixed");
function cdet(M){M=M.map(r=>r.slice());let out=c(1);for(let i=0;i<M.length;i++){let k=i;while(k<M.length&&ce(M[k][i],c()))k++;if(k===M.length)return c();if(k!==i){[M[i],M[k]]=[M[k],M[i]];out=cn(out)}const pivot=M[i][i];out=cm(out,pivot);for(let j=i+1;j<M.length;j++){const rr=cd(M[j][i],pivot);for(let a=i+1;a<M.length;a++)M[j][a]=cs(M[j][a],cm(rr,M[i][a]));M[j][i]=c()}}return out}
const pg=pi.map(r=>pi.map(t=>dot(r,t))),pgdet=cdet(pg);
if(ce(pgdet,c()))throw Error("four outputs dependent");
const B3co=add(q(2,7),q(3,210));
if(!eq(B3co,q(3,10))||!eq(mul(q(720),B3co),q(216)))throw Error("whole odd3 moment normalization");

const fifth=(()=>{

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

const om=c(q(-1,2),q(1,2)),gam=c(q(5,2),q(1,2)),bg=cc(gam),eta=cd(cs(c(1),om),c(103));
const z=[c(0,1),c(0,2),gam,c(1),c(2)];
const dd=[c(-15,15),c(q(63,2),q(-21,2)),c(q(1,2),q(-1,2)),c(1),c(q(1,2),q(3,2))];
const lh=[c(1),c(),c(-1),c(),c()],le=lh.map((t,i)=>ca(t,cm(c(q(0),q(1,103)),dd[i]))),qe=cd(ca(c(72),cm(c(31),om)),c(103));
function fact(n){let r=1n;for(let i=2;i<=n;i++)r*=BigInt(i);return r}
const choose=(n,k)=>fact(n)/(fact(k)*fact(n-k));
function pol(l){let p=[c(1)];for(let i=0;i<5;i++){const a=Array.from({length:p.length+1},()=>c());for(let j=0;j<p.length;j++){a[j]=ca(a[j],cm(p[j],l[i]));a[j+1]=ca(a[j+1],cm(p[j],z[i]));}p=a;}return p}
function al(l,qx){const p=pol(l);let inn=c();for(let a=1;a<=5;a++){const r=q((a%2?1n:-1n)*choose(6,5-a)*fact(a)*fact(5-a),BigInt(a));inn=ca(inn,cm(c(r),cm(cp(qx,1+a),cm(cp(ci(bg),a),p[a]))));}return cd(cn(inn),c(84*216))}
const ah=al(lh,c(1)),ae=al(le,qe);
const exp=cd(ca(c(-3221),cm(c(5000),om)),c(27n*7n**6n));
if(!ce(ah,exp))throw Error("R522 H0 first five does not match");
const lc=(a,b)=>a/gcd(a,b)*b,B=cs(ah,ae),den=[...ah,...B].reduce((d,t)=>lc(d,t[1]),1n),u=cm(c(den),ah),v=cm(c(den),B);
const nu=norm(u),nv=norm(v),tr=mul(q(2),cm(u,cc(v))[0]);
const mo=x=>String((x%1013n+1013n)%1013n);
return {eta:cj(eta),alpha_H:cj(ah),alpha_E:cj(ae),E_after_T_L:le.map(cj),E_after_T_x:cj(qe),
integer:{denominator:String(den),u:cj(u),v:cj(v),norm_u:qs(nu),norm_v:qs(nv),trace:qs(tr),threshold:String((nu[0]+nv[0]+1n)**2n)},
mod1013:{den:mo(den),Nu:mo(nu[0]),Nv:mo(nv[0]),Tr:mo(tr[0]),difference:mo(tr[0]-nv[0])}};

})();


function rr(s){const t=s.split("/");return q(BigInt(t[0]),t[1]?BigInt(t[1]):1n)}
const rcc=o=>c(rr(o.real),rr(o.delta));
const ep=fifth.E_after_T_L.map(rcc).concat([rcc(fifth.E_after_T_x)]);
const fp=[c(1),c(),c(-1),c(),c(),c(1)].map((x,i)=>cs(x,ep[i]));
let mass=[c(1)];
for(let i=0;i<6;i++){const z=Array.from({length:mass.length+1},()=>c());for(let j=0;j<mass.length;j++){z[j]=ca(z[j],cm(mass[j],ep[i]));z[j+1]=ca(z[j+1],cm(mass[j],fp[i]));}mass=z;}
if(!ce(mass.reduce(ca,c()),c())||ce(mass[0],c()))throw Error("local mass polynomial");
return {
 status:"complete four-output, original-source transpose and nonzero fifth coefficient checked exactly",
 H0:H0.map(cj),H0_norm:3,odd3_even_basis:"-y_wp sigma^3",odd3_z6:"3b/10",odd3_moment6:"216 b Omega^6",
 B:BH.map(cj),eta:cj(eta),E0:E0.map(cj),E0_norm:"216/103",
 root_E_relation:{multiplier:cj(eunit),norm:"1"},
 four_outputs:["Y","W","Wprime","D_H"],pi4:pi.map(r=>r.map(cj)),pi4_Gram:pg.map(r=>r.map(cj)),pi4_Gram_determinant:cj(pgdet),
 A:AA.map(cj),A_norm:7416,A_projector:pA.map(r=>r.map(cj)),
 inverse_test_shifts:shifts.map(cj),inverse_E0_shift:cj(eshift),
 corrected_test:"sum j=0..6 binom(6,j) eta^j E0^(6-j) B^j / (216 b Omega^6 (1+lambda kappa^j))",
 full_joint_identity:"pi4_* [1_(B unit) corrected_test nu_mu] = pi4_*nu_mu for all four original states",
 carry_joint_identity:"normalized pi4, complete test and B-unit on Gamma_r; even r for h, r divisible by8 for all four",
 fifth,
 local_mass_polynomial:mass.map(cj),
 local_mass_c0_norm:qs(norm(mass[0])),
 local_mass_exact:"-5 omega^2/(126b) beta^(5n) kappa^(5n) (1+lambda kappa) sum_j c_j/(1+lambda kappa^j)",
 nonzero_actual_domain:"R deep n, B unit, 31 A/kappa^r-72B deep n; r even",
 warning:"all normalized Y/Wprime and E0 arguments must be transported; the full carry complement remains"
};

})();
process.stdout.write(JSON.stringify(certificate,null,2)+"\n");
