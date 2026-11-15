#!/usr/bin/env node
// R655: exact complete local sigma^5 data, E80 character, and rank-one tail bound.
// Run: node check-r655-sigma-five-full-schwartz-and-rank-one.mjs
// No packages, network, floating-point arithmetic, or sampled L-values.
const result = (() => {

const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){[a,b]=[b,a%b]}return a}
function q(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]}
const qa=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]), qn=a=>[-a[0],a[1]], qs=(a,b)=>qa(a,qn(b));
const qm=(a,b)=>q(a[0]*b[0],a[1]*b[1]), qd=(a,b)=>q(a[0]*b[1],a[1]*b[0]);
const qe=(a,b)=>a[0]===b[0]&&a[1]===b[1], qj=a=>a[1]===1n?String(a[0]):a[0]+"/"+a[1];
function qpow(a,n){let r=q(1);for(;n;n>>=1,a=qm(a,a))if(n&1)r=qm(r,a);return r}
function field(N,poly){
 const d=poly.length-1,Z=()=>Array.from({length:d},()=>q(0));
 const C=(a,b=1)=>{let z=Z();z[0]=q(a,b);return z};
 const add=(a,b)=>a.map((x,i)=>qa(x,b[i])),neg=a=>a.map(qn),sub=(a,b)=>add(a,neg(b));
 const sc=(a,b,c=1)=>a.map(x=>qm(x,q(b,c)));
 const mul=(a,b)=>{let z=Array.from({length:2*d-1},()=>q(0));for(let i=0;i<d;i++)for(let j=0;j<d;j++)z[i+j]=qa(z[i+j],qm(a[i],b[j]));for(let k=2*d-2;k>=d;k--)for(let j=0;j<d;j++)z[k-d+j]=qs(z[k-d+j],qm(z[k],q(poly[j])));return z.slice(0,d)};
 const eq=(a,b)=>a.every((x,i)=>qe(x,b[i]));
 const pow=(a,n)=>{let r=C(1);for(;n;n>>=1,a=mul(a,a))if(n&1)r=mul(r,a);return r};
 const z=n=>{n=(n%N+N)%N;let x=Z();x[1]=q(1);return pow(x,n)};
 const conj=a=>a.map((x,i)=>sc(z(-i),x[0],x[1])).reduce(add,C(0));
 const json=a=>a.map(qj);
 return{N,d,Z,C,add,neg,sub,sc,mul,eq,pow,z,conj,json};
}
const mod=(x,m)=>(x%m+m)%m;
const fp=(x,y,m)=>[mod(x[0]*y[0]-x[1]*y[1],m),mod(x[0]*y[1]+x[1]*y[0]-x[1]*y[1],m)];
function fpower(x,n,m){let a=[1,0];for(;n;n>>=1,x=fp(x,x,m))if(n&1)a=fp(a,x,m);return a}
const fe=(x,y)=>x[0]===y[0]&&x[1]===y[1];

const cert={status:"PASS",checks:[],dyadic:{},quintic:{},character:{},period:{}};
function ck(label,ok){if(!ok)throw Error(label);cert.checks.push(label)}
const A=field(64,Array.from({length:33},(_,i)=>(i===0||i===32)?1:0));
const B=field(15,[1,-1,0,1,-1,1,0,-1,1]);
const a0=A.C(0),a1=A.C(1),z8=A.z(8),sqrt2=A.add(A.z(8),A.z(-8));
ck("sqrt2 square",A.eq(A.mul(sqrt2,sqrt2),A.C(2)));
const odd=[1,3,5,7],sign=[1,1,-1,-1];
let wout=[];
for(let k=0;k<16;k++){
 let t=odd.map((b,i)=>A.sc(A.z(-15*(k*k+8*k*b+4*b*b)),sign[i])).reduce(A.add,a0);
 t=A.sc(A.mul(A.neg(z8),t),1,4);
 const i=odd.findIndex(b=>k===2*b);
 ck("dyadic omega output "+k,A.eq(t,A.C(i<0?0:sign[i])));
 wout.push(A.json(t));
}
let gout=[];
for(const a of odd){
 let t=odd.map((b,i)=>mod(13*a+11*b,4)?a0:A.sc(A.z(-15*(11*a*a+26*a*b+11*b*b)),sign[i])).reduce(A.add,a0);
 t=A.sc(A.mul(z8,A.mul(sqrt2,t)),1,2);
 ck("dyadic gstar output "+a,A.eq(t,A.C(sign[odd.indexOf(a)])));
 gout.push(A.json(t));
}
cert.dyadic={cyclotomic:64,phi:"-chi_{-2}(2x) 1_{v2(x)=-1}",mu_omega:A.json(A.neg(z8)),mu_gstar:A.json(z8),omega_output:wout,gstar_output:gout,norm:1};
const om=B.z(5),rt5=B.add(B.C(1),B.sc(B.add(B.z(3),B.z(-3)),2));
ck("sqrt5 square",B.eq(B.mul(rt5,rt5),B.C(5)));
const M=Array.from({length:5},(_,a)=>Array.from({length:5},(_,b)=>B.sc(B.mul(om,B.mul(rt5,B.z(-6*(a*a+4*a*b+b*b)))),1,5)));
const mv=(M,v)=>M.map(r=>r.map((x,j)=>B.mul(x,v[j])).reduce(B.add,B.C(0)));
const mm=(M,N)=>M.map(r=>N[0].map((_,j)=>r.map((x,k)=>B.mul(x,N[k][j])).reduce(B.add,B.C(0))));
const M2=mm(M,M),M3=mm(M2,M);
ck("five-dimensional omega cube I",M3.every((r,a)=>r.every((x,b)=>B.eq(x,B.C(a===b?1:0)))));
ck("five-dimensional omega unitary",mm(M,M[0].map((_,j)=>M.map(r=>B.conj(r[j])))).every((r,a)=>r.every((x,b)=>B.eq(x,B.C(a===b?1:0)))));
const v=Array.from({length:5},(_,a)=>B.sc(B.add(B.add(B.C(a===0?1:0),M[a][0]),M2[a][0]),1,3));
ck("quintic invariant Mv=v",mv(M,v).every((x,i)=>B.eq(x,v[i])));
ck("quintic invariant even",v.every((x,i)=>B.eq(x,v[mod(-i,5)])));
ck("quintic invariant real",v.every(x=>B.eq(x,B.conj(x))));
const n5=v.map(x=>B.mul(x,B.conj(x))).reduce(B.add,B.C(0));
ck("quintic norm=(1-1/sqrt5)/3",B.eq(n5,B.sc(B.sub(B.C(1),B.sc(rt5,1,5)),1,3)));
ck("quintic norm=v0",B.eq(n5,v[0]));
const root6=B.add(B.C(1),om),r6=Array.from({length:6},(_,i)=>fpower([1,1],i,5));
const roots6=Array.from({length:6},(_,i)=>fpower([1,1],i,30));
let gauss=B.C(0),units5=[];
for(let a=0;a<5;a++)for(let b=0;b<5;b++)if(a||b){
 let x=[a,b],x4=fpower(x,4,5),e=r6.findIndex(y=>fe(y,x4));
 ck("F25 fourth power in mu6 "+a+","+b,e>=0);
 // Local character on units is Teich(x)^(-4); inverse occurs in epsilon Gauss.
 let chiinv=B.pow(root6,e),trace=mod(2*a-b,5);
 gauss=B.add(gauss,B.mul(chiinv,B.z(-3*trace)));
 units5.push({a,b,e});
}
ck("F25 Gauss sum=-5",B.eq(gauss,B.C(-5)));
cert.quintic={cyclotomic:15,matrix:M.map(r=>r.map(B.json)),vector:v.map(B.json),norm:B.json(n5),gauss_inverse:B.json(gauss)};
const r6mod2=Array.from({length:6},(_,i)=>fpower([1,1],i,2)),r3mod2=[r6mod2[0],r6mod2[2],r6mod2[4]];
function chiExp(a,b){
 const u=fpower([mod(a,5),mod(b,5)],4,5),e=r6.findIndex(y=>fe(y,u));
 const j=r3mod2.findIndex(y=>fe(y,[mod(a,2),mod(b,2)]));
 if(e<0||j<0)throw Error("nonunit residue");
 return mod(e-2*j,6);
}
const residues=[];
for(let a=0;a<10;a++)for(let b=0;b<10;b++)if(gcd(BigInt(a*a-a*b+b*b),10n)===1n)residues.push({a,b,e:chiExp(a,b)});
ck("72 units mod10",residues.length===72);
for(const r of residues){
 ck("conjugation inverse "+r.a+","+r.b,chiExp(r.a-r.b,-r.b)===mod(-r.e,6));
 for(const s of residues){const t=fp([r.a,r.b],[s.a,s.b],10);ck("multiplicativity "+r.a+","+r.b+";"+s.a+","+s.b,chiExp(...t)===mod(r.e+s.e,6))}
}
ck("unit-independence mu6",roots6.every(x=>chiExp(...x)===0));
ck("primitive at2",residues.some(x=>mod(x.a-1,5)===0&&mod(x.b,5)===0&&x.e!==0));
ck("primitive at5",residues.some(x=>mod(x.a-1,2)===0&&mod(x.b,2)===0&&x.e!==0));
ck("sixth-order",residues.some(x=>x.e===1||x.e===5));
const pi=[-1,2],epi=chiExp(...pi);
ck("primary pi7 character=-omega",epi===5);
const cmul=(x,y)=>[x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1]];
const actualRoots=[[1,0],[1,1],[0,1],[-1,0],[-1,-1],[0,-1]];
const ps7=cmul(pi,actualRoots[mod(-epi,6)]);
ck("E80 primary pi7=-3-omega",fe(ps7,[-3,-1]));
cert.character={conductor:"(10)",order:6,residues,pi7_exp:epi,psiA_pi7:ps7,finite_local:{at2:"unramified, uniformizer -1",at_delta:"unit sign, uniformizer i",at5:"Teich^(-4), uniformizer -1"},E80_candidates:[4,16]};
function chi2(n){const a=mod(n,8);return a===1||a===3?1:a===5||a===7?-1:0}
function an(n){return B.sc(v[mod(n,5)],chi2(n))}
for(let n=0;n<40;n++){
 ck("Fourier period40 n="+n,B.eq(an(n+40),an(n)));
 ck("Fourier halfperiod20 n="+n,B.eq(an(n+20),B.neg(an(n))));
 ck("Fourier odd n="+n,B.eq(an(-n),B.neg(an(n))));
 if(n%2)ck("Fourier shift10 n="+n,B.eq(an(n+10),B.sc(an(n),mod((n-1)/2,2)?-1:1)));
}
cert.period={alpha:"5/2",kappa:"15*sqrt3/2",h:"sqrt(15*sqrt3/2)/(30*pi*i)",real_weight_scale:"15^(-m)",CM_weight_scale:"5^(-m)",finite_norm:"1-1/sqrt5",negative_one_factor:"5*c5*Omega_p0",b17_scale:"theta^11",bare_reflection:"conjugate Hecke character of E80"};

function points(p){let n=1;for(let x=0;x<p;x++)for(let y=0;y<p;y++)if(mod(y*y+y-x*x*x-1,p)===0)n++;return n}
const n2=points(2),n7=points(7),n13=points(13);
ck("minimal curve a2=0",n2===3);ck("E80 a7=-5",n7===13);ck("E80 a13=-5",n13===19);
ck("torsion gcd reductions is1",gcd(BigInt(n7),BigInt(n13))===1n);
const allowed=Array.from({length:24},(_,k)=>k).filter(k=>k%4===0&&k%6===4);
ck("complete K-valued conductor5delta candidates",allowed.join(",")==="4,16");
const invAt7=allowed.map(k=>{
 const residue=fpower(pi,k,5),e=r6.findIndex(x=>fe(x,residue));
 const val=cmul(pi,actualRoots[mod(-e,6)]);
 return {k,value:val,trace:2*val[0]-val[1]};
});
ck("the two conductor candidates have distinct exact a7",invAt7[0].trace===-5&&invAt7[1].trace===5);
const b2=q(0),b4=q(0),b6=q(5),b8=q(0);
const discr=qn(qm(q(27),qpow(b6,2))),c6=qn(qm(q(216),b6));
ck("minimal invariants",qe(discr,q(-675))&&qe(c6,q(-1080)));
const logLower=(x,N)=>{const y=qd(qs(x,q(1)),qa(x,q(1)));let t=y,s=q(0),y2=qm(y,y);for(let k=0;k<N;k++,t=qm(t,y2))s=qa(s,qd(t,q(2*k+1)));return qm(q(2),s)};
const log10lo=logLower(q(10),40),logcLo=logLower(q(1000,419),16);
let H10=q(0);for(let n=1;n<=10;n++)H10=qa(H10,q(1,n));
const gammaUB=qa(qs(qs(H10,log10lo),q(1,20)),q(1,1200));
const qlt=(a,b)=>a[0]*b[1]<b[0]*a[1];
ck("Euler constant upper bound<.578",qlt(gammaUB,q(578,1000)));
ck("-log(.419)>.869",qlt(q(869,1000),logcLo));
const lo=q(1047,2500),hi=q(419,1000);
let eLow=q(1),et=q(1);for(let n=1;n<=4;n++){et=qd(qm(et,lo),q(n));eLow=qa(eLow,et)}
ck("exp(.4188)>500/329",qlt(q(500,329),eLow));
const head=qm(q(2),qs(qa(qa(q(-578,1000),q(869,1000)),lo),qd(qpow(hi,2),q(4))));
const r=q(329,500),tail=qd(qpow(r,4),qm(lo,qs(q(1),r)));
const gap=qs(head,tail);
ck("analytic derivative bound > .02",qlt(q(1,50),gap));
cert.curve={short:"y^2=x^3+80",minimal:"y^2+y=x^3+1",map:"(x,y)=(4X,8Y+4)",discriminant:-675,conductor:225,tate:{at3:"III, vDelta=3, f=2",at5:"II, vDelta=2, f=2"},point:[1,1],reductions:{p2:n2,p7:n7,p13:n13},two_character_tests:invAt7,root:-1};
cert.analytic_rank={c_interval:[qj(lo),qj(hi)],exp_bound:qj(eLow),head_lower:qj(head),tail_upper:qj(tail),derivative_lower:qj(gap),argument:"root -1; exact functional-equation E1 sum; a2=a3=0; |an|<=2n"};

cert.check_count=cert.checks.length;
cert.checks=cert.checks.filter(x=>!/^multiplicativity |^conjugation inverse |^F25 fourth power |^Fourier /.test(x));
return cert;

})();
console.log(JSON.stringify(result,null,2));
