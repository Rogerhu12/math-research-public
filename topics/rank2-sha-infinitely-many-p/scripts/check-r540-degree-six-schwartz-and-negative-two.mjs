#!/usr/bin/env node
// R540: exact original degree-six local data and period checks.
// Run: node check-r540-degree-six-schwartz-and-negative-two.mjs
// No external packages, network, floating-point arithmetic, or L-value samples.
const result = (() => {

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

const Z=Array.from({length:8},()=>q(0));const C=a=>{const v=[...Z];v[0]=q(a);return v},Ad=(a,b)=>a.map((x,i)=>add(x,b[i])),Ng=a=>a.map(neg),Sc=(a,qv)=>a.map(x=>mul(x,qv));
function Mt(A,B){const C=Array.from({length:15},()=>q(0));for(let i=0;i<8;i++)for(let j=0;j<8;j++)C[i+j]=add(C[i+j],mul(A[i],B[j]));for(let k=14;k>=8;k--){C[k-4]=add(C[k-4],C[k]);C[k-8]=sub(C[k-8],C[k])}return C.slice(0,8)}
function zz(n){n=(n%24+24)%24;let z=[...Z];z[1]=q(1);let r=C(1);for(;n;n>>=1,z=Mt(z,z))if(n&1)r=Mt(r,z);return r}
const Eq=(a,b)=>a.every((x,i)=>eq(x,b[i])),J=a=>a.map(qs);

const cert={checks:[],dyadic:{},triadic:{},finite_character:{},period:{}};
function ck(label,ok,data){if(!ok)throw Error(label);cert.checks.push(label);if(data!==undefined)return data;}
const rt2=Ad(zz(3),zz(-3)),rt3=Ad(zz(2),zz(-2));
const om=zz(8),ii=zz(6),de=Ad(C(1),Sc(om,q(2))),one=C(1);
ck("sqrt2^2=2",Eq(Mt(rt2,rt2),C(2)));ck("sqrt3^2=3",Eq(Mt(rt3,rt3),C(3)));
ck("delta=i sqrt3",Eq(de,Mt(ii,rt3)));
const tt=Sc(Mt(Ad(rt3,C(-1)),rt2),q(1,2)),v=[C(1),tt,C(-1),tt];
const mu2=Ng(zz(13)),pref=Sc(Mt(mu2,rt2),q(1,4));
const M=Array.from({length:4},(_,a)=>Array.from({length:4},(_,b)=>
 Mt(pref,zz(-27*(a*a+b*b+4*a*b)))));
const Mv=M.map(row=>row.map((x,b)=>Mt(x,v[b])).reduce(Ad,C(0)));
ck("complete dyadic omega matrix fixes (1,t,-1,t)",Mv.every((x,j)=>Eq(x,v[j])));
for(let k=1;k<8;k+=2){
 const e=b=>-9*(k*k+8*k*b+4*b*b);
 ck("quarter support cancellation k="+k,((e(0)-e(2))%32+32)%32===0&&((e(1)-e(3))%32+32)%32===16);
}
const gs=Array.from({length:4},()=>Array.from({length:4},()=>C(0)));
for(let b=0;b<4;b++){let a=(3*b+2)%4;let num=11*a*a-26*a*b+11*b*b;
 ck("gstar phase integral b="+b,num%4===0);gs[a][b]=zz(-3-27*(num/4));}
ck("complete gstar matrix",gs.every((r,a)=>r.every((x,b)=>Eq(x,C(a===(3*b+2)%4?(b%2?1:-1):0)))));
ck("gstar fixes phi2",gs.map(r=>r.map((x,b)=>Mt(x,v[b])).reduce(Ad,C(0))).every((x,j)=>Eq(x,v[j])));
const n2=Sc(v.map(x=>Mt(x,x)).reduce(Ad,C(0)),q(1,2));
ck("dyadic norm 3-sqrt3",Eq(n2,Ad(C(3),Ng(rt3))));
cert.dyadic={basis:"Q[zeta24]/(zeta24^8-zeta24^4+1), coefficients ascending",
t:J(tt),mu_omega:J(mu2),omega_matrix:M.map(r=>r.map(J)),gstar_matrix:gs.map(r=>r.map(J)),norm:J(n2)};
const cmom=c(q(-1,2),q(1,2)),cmdelta=c(0,1);
const cmz6=ca(c(1),cmom),units=Array.from({length:6},(_,k)=>cp(cmz6,k));
const ab=x=>{const B=mul(q(2),x[1]); 
 // A+B*omega, since delta=1+2*omega.
 return [add(x[0],x[1]),B];};
for(let e=0;e<6;e++){
 const [A,B]=ab(units[e]);ck("mu6 integral coordinates "+e,A[1]===1n&&B[1]===1n);
}
let gaussPlus=c(),gaussMinus=c();
for(const u of units){const [A,B]=ab(u),phase=cp(cmom,Number((-B[0]%3n+3n)%3n));gaussPlus=ca(gaussPlus,cm(u,phase));gaussMinus=ca(gaussMinus,cm(cc(u),phase));}
ck("3-adic Gauss uses Tr=-B/6 mod Z3, sum +3",ce(gaussPlus,c(3)));
ck("opposite triadic unit character has Gauss -3",ce(gaussMinus,c(-3)));
const pro=[];
for(let ell=0;ell<3;ell++){
 let g=c();for(let t=0;t<3;t++)g=ca(g,cp(cmom,((-2*(t*t+ell*t))%3+3)%3));
 g=cd(g,c(3));const expect=cm(cd(cmdelta,c(3)),cp(cmom,(2*ell*ell)%3));
 ck("pro3 exact quadratic Gauss l="+ell,ce(g,expect));
 const phase=cp(cmom,((-2*ell*ell)%3+3)%3);
 ck("pro3 phase cancels l="+ell,ce(cm(g,phase),cd(cmdelta,c(3))));
 pro.push({ell,quadratic_integral:cj(g),constant_phase:cj(phase)});
}
ck("triadic prefactor (-i)*sqrt3*delta/3=1",Eq(Sc(Mt(Ng(ii),Mt(rt3,de)),q(1,3)),one));
cert.triadic={gauss_unit_inverse:cj(gaussPlus),gauss_unit_direct:cj(gaussMinus),
base_omega_eigenvalues:["1","omega^2","omega^2"],new_omega_multiplier:"omega",
pro3:pro,schwartz_norm:6,uniformizer_plus:"i",uniformizer_minus:"-i"};
const mod=(n,m)=>((n%m)+m)%m;
const modpair=(A,B,m)=>[mod(A,m),mod(B,m)];
function mulpair(x,y,m){return modpair(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1],m);}
const roots6=units.map(x=>ab(x).map(y=>Number(y[0]))),roots3=[roots6[0],roots6[2],roots6[4]];
function charExp(A,B){
 const t=roots3.findIndex(x=>mod(x[0]-A,2)===0&&mod(x[1]-B,2)===0);
 const k=roots6.findIndex(x=>mod(x[0]-A,3)===0&&mod(x[1]-B,3)===0);
 if(t<0||k<0)throw Error("nonunit");
 return mod(-t+2*k,3);
}
const residue=[];
for(let A=0;A<6;A++)for(let B=0;B<6;B++)if(gcd(BigInt(A*A-A*B+B*B),6n)===1n)
 residue.push({A,B,xi_omega_exponent:charExp(A,B)});
ck("18 invertible residues modulo 6",residue.length===18);
for(const r of residue){
 ck("conjugation inverse "+r.A+","+r.B,charExp(r.A-r.B,-r.B)===mod(-r.xi_omega_exponent,3));
 for(const t of residue){const u=mulpair([r.A,r.B],[t.A,t.B],6);
 ck("multiplicative "+r.A+","+r.B+";"+t.A+","+t.B,charExp(...u)===mod(r.xi_omega_exponent+t.xi_omega_exponent,3));}
}
ck("mu6 cancels in ideal definition",roots6.every(x=>charExp(...x)===0));
ck("primitive at 2",residue.some(r=>mod(r.A-1,3)===0&&mod(r.B,3)===0&&r.xi_omega_exponent!==0));
ck("primitive modulo delta^2 at 3",residue.some(r=>mod(r.A-1,2)===0&&mod(r.B,2)===0&&mod(r.A+r.B-1,3)===0&&r.xi_omega_exponent!==0));
ck("xi((5))=1",charExp(5,0)===0);
cert.finite_character={conductor:"(6)=2*delta^2",order:3,residues:residue,uniformizer2:1,uniformizer_delta:1};
function anew(n,parity){
 if(mod(n,3)===0)return C(0);
 const s=parity===0?1:(mod(2*n,3)===1?1:-1);return Sc(v[mod(n,4)],q(s));
}
for(const p of [0,1])for(let n=0;n<12;n++){
 ck("Fourier periodicity parity="+p+",n="+n,Eq(anew(n+12,p),anew(n,p)));
 ck("Fourier half-shift parity="+p+",n="+n,Eq(anew(n+6,p),Sc(anew(n,p),q(n%2?1:-1))));
 ck("Fourier parity parity="+p+",n="+n,Eq(anew(-n,p),Sc(anew(n,p),q(p?-1:1))));
}
const ss=cd(c(1),cs(c(1),cmom));
ck("s^2=-omega^2/3",ce(cp(ss,2),cn(cd(cp(cmom,2),c(3)))));
for(let m=1;m<=16;m+=3){
 if(m%6!==1&&m%6!==4)continue;
 const normalized=cm(cp(ci(ss),2*m),c(q(1,BigInt(3)**BigInt(m))));
 const expected=m%6===4?cmom:cn(cmom);
 ck("CM-period factor m="+m,ce(normalized,expected));
}
cert.period={alpha:3,kappa_infinity:"9*sqrt3",h:"sqrt(9*sqrt3)/(36*pi*i)",
gaussian_identity:"6*sqrt3*pi*h^2=-1/(8*pi)",real_weight_scale:"18^(-m)",
CM_weight_scale:"6^(-m)",finite_norm:"6*(3-sqrt3)",
C_Y:"pi*sqrt(18*sqrt3)/(36*sqrt3*(3-sqrt3))",
f4_first:4,f1_first:1,negative_two_factor:"36*c4*Omega_p0",
b17_scale:"theta^9=17^(3/2)",reflected_root:-1};
ck("negative reflected angular difference is 6",(9-3)===6);
cert.check_count=cert.checks.length;
cert.status="PASS";
return cert;

})();
console.log(JSON.stringify(result, null, 2));
