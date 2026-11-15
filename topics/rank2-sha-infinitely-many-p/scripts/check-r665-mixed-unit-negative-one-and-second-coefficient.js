#!/usr/bin/env node
// Exact R665 certificate: same original R594 right inverse via the published R659 data.
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




function moments(input){
const parse=s=>{const x=s.split("/");return Q(x[0],x[1]||1);},read=x=>x.map(parse),row=a=>a.map(x=>Array.isArray(x)?E(...x):E(x));
const w=E(0,1),delta=E(1,2),C=vm(row([1,0,-1,1]),ei(delta)),A=row([[1,2],[2,4],[3,1],[2,-1]]),D4=row([1,[-1,-1],[0,-2],0]),H=row([-1,2,[0,1],[1,1]]),g=E(3,-2),aa=E(-5,-6,29);
const D=vs(D4,vm(A,aa)),d=he(D,D),F=va(D,C),Erow=va(D,vm(C,E(14))),Grow=va(vm(H,E(13)),vm(F,g));
ck(eq(d,E(143,0,29))&&eq(he(D,C),E(-1))&&ez(he(D,A)),"actual Dstar norms and non-orthogonal C");
const proj=(V,U)=>vs(V,vm(U,em(he(V,U),ei(he(U,U)))));
const Cp=proj(C,D),Ep=proj(Erow,D),Gp=proj(Grow,D),G00=proj(Gp,Cp);
ck(Ep.every((v,i)=>eq(v,esc(Cp[i],14))),"Eperp=14 Cperp");
const Pm=Object.fromEntries(Object.entries(input.Pres).map(([k,v])=>[k,read(v)])),P0=Object.fromEntries(Object.entries(input.Pconst).map(([k,v])=>[k,read(v)]));
const deriv=P=>{const z={};for(const[k,c]of Object.entries(P)){let e=k.split(",").map(Number);if(e[0]>=2){const fac=e[0]*(e[0]-1);e[0]-=2;z[e.join(",")]=esc(c,fac);}}return z;};
const dp=deriv(Pm),dq=deriv(P0);
function add(P,R){const z={...P};for(const[k,c]of Object.entries(R)){z[k]=ea(z[k]||E(0),c);if(ez(z[k]))delete z[k];}return z;}
const scale=(P,c)=>Object.fromEntries(Object.entries(P).map(([k,v])=>[k,em(v,c)]).filter(([k,v])=>!ez(v)));
function mul(P,R){const z={};for(const[k,c]of Object.entries(P))for(const[l,v]of Object.entries(R)){const a=k.split(",").map((x,i)=>+x+ +l.split(",")[i]).join(",");z[a]=ea(z[a]||E(0),em(c,v));}return z;}
function pow(P,n){let z={"0,0,0":E(1)};for(let i=0;i<n;i++)z=mul(z,P);return z;}
const lin=rr=>Object.fromEntries(rr.map((c,i)=>[[0,1,2].map(j=>i===j?1:0).join(","),c]).filter(([k,v])=>!ez(v)));
const fact=n=>{let a=1;for(let i=2;i<=n;i++)a*=i;return a;};
function gen4(rr){const z=Array.from({length:4},(_,j)=>lin(rr.map(V=>V[j]))),zZ=scale(add(add(z[0],scale(z[2],E(-1))),scale(z[3],E(-2))),E(1,0,6)),zQ=scale(add(z[0],z[2]),E(1,0,2));
return scale(mul(add(mul(zZ,pow(zQ,2)),scale(pow(zZ,3),E(-1))),z[1]),E(1,0,42));}
function moment(P,rr){const gen=gen4(rr);return Object.entries(P).reduce((s,[k,c])=>ea(s,em(c,esc(gen[k]||E(0),k.split(",").reduce((a,i)=>a*fact(+i),1)))),E(0));}
const e0=P=>Object.fromEntries(Object.entries(P).filter(([k,v])=>+k.split(",")[1]===0));
const aRes=moment(dp,[D,Ep,Gp]),aConst=moment(dq,[D,Ep,Gp]),aRes0=moment(e0(dp),[D,Ep,Gp]),aConst0=moment(e0(dq),[D,Ep,Gp]),bRes=moment(e0(dp),[D,Array(4).fill(E(0)),G00]),bConst=moment(e0(dq),[D,Array(4).fill(E(0)),G00]);
const nSign=s=>[aRes,es(es(ea(aRes,aConst),aRes0),esc(bRes,s)),es(es(aConst,aConst0),esc(bConst,s))].map(out);
return{residue:out(aRes),nonzero:!ez(aRes),moments:{aRes:out(aRes),aConst:out(aConst),aRes0:out(aRes0),aConst0:out(aConst0),bRes:out(bRes),bConst:out(bConst)},numerator_eta_plus:nSign(1),numerator_eta_minus:nSign(-1),rows:{C:C.map(out),A:A.map(out),D:D.map(out),Cperp:Cp.map(out),Eperp:Ep.map(out),Gperp:Gp.map(out),G00:G00.map(out)},norms:{D:out(d),Cperp:out(he(Cp,Cp))},D_coefficients:{E:out(em(he(Erow,D),ei(d))),G:out(em(he(Grow,D),ei(d)))},partial_D2_residue:Object.fromEntries(Object.entries(dp).map(([k,v])=>[k,out(v)]))};}
function geometry(){
const row=a=>a.map(x=>Array.isArray(x)?E(...x):E(x)),delta=E(1,2),C=vm(row([1,0,-1,1]),ei(delta)),A=row([[1,2],[2,4],[3,1],[2,-1]]),D4=row([1,[-1,-1],[0,-2],0]),a=E(-5,-6,29);
const D=vs(D4,vm(A,a)),Cp=va(C,vm(D,E(29,0,143)));
const proj=(V,U)=>vs(V,vm(U,em(he(V,U),ei(he(U,U)))));
let frame=[vm(D,E(87)),vm(Cp,E(429)),A];
let R=row([0,1,0,0]);for(const V of frame)R=proj(R,V);
let den=1n;for(const x of R)for(const y of x)den=den/gcd(den,y[1])*y[1];R=vm(R,E(den));
let con=0n;for(const x of R)for(const y of x)con=gcd(con,y[0]);R=vm(R,E(1,0,con));frame.push(R);
for(let i=0;i<4;i++)for(let j=0;j<i;j++)ck(ez(he(frame[i],frame[j])),"full four-input orthogonal frame");
const roots=[E(1),E(0,1),E(-1,-1),E(-1),E(0,-1),E(1,1)];
const all=roots.map(zeta=>{const fr=frame.map(V=>va(V,vm(C,em(es(zeta,E(1)),he(V,C)))));
const count=fr.map(V=>V.filter(x=>{ck(x[0][1]===1n&&x[1][1]===1n,"all six rotated rows integral");return x.some(y=>(y[0]%2n+2n)%2n!==0n);}).length);
return{zeta:out(zeta),counts:count,frame:fr.map(V=>V.map(out))};});
const d13=E(4,1),d19=E(5,2),d79=E(10,3);
ck(eq(he([delta],[delta]),E(3))&&eq(he([esc(d79,2)],[esc(d79,2)]),E(316)),"odd319 two-sigma norm anchor");
ck(eq(he([d19],[d19]),E(19)),"even22 two-sigma anchor");
const pullD=esc(d13,3),pullE=esc(em(em(delta,d13),d19),3);
ck(eq(esc(he([pullD],[pullD]),319),E(37323)),"full D pullback anchor");
ck(eq(esc(he([pullE],[pullE]),22),E(146718)),"full Cperp pullback anchor");
const bL=E(2,12,5),bY=E(20,3,17),h=em(bL,ei(bY)),ell0=E(0,-3,5);
return {frame:frame.map(V=>V.map(out)),norms:frame.map(V=>out(he(V,V))),det:out(inverse(frame).det),six_branches:all,
core_labels:{D:{N:37323,center_modulus:74646,g:["1","0"],scalar:"chi_D",square:1},Cperp:{N:146718,center_modulus:293436,g:["146719","0"],scalar:"eta",square:1}},
anchors:{odd319:["delta","2(10+3omega)"],even22:["delta","5+2omega"],pullD:out(pullD),pullE:out(pullE)},
coefficients:{ell0:out(ell0),h:out(h),h_norm:out(em(h,ec(h))),bL_norm:out(em(bL,ec(bL))),bY_norm:out(em(bY,ec(bY)))},
half_character_warning:"29Dstar alone is not integral on all six C branches; the actual cover is 87Dstar. Dstar is not orthogonal to C."};}
function angle(){
const selectors=[];
for(const k of[1,3,5]){
 const pairType=k===1?{Q:5,L:3}:k===3?{Q:3,L:5}:{Q:1,L:1};
 const js=[];for(let j=0;j<=6;j++)if(((-k-pairType.Q)%6+6)%6===0&&(j+k-pairType.L)%6===0)js.push(j);
 ck(js.length===1&&js[0]===2,"full six-degree odd angular selection");selectors.push({k_mod6:k,pairType,j:js});
}
return {selectors,source_coefficients:{k1:"6b I_Sigma,-1 * moment_X,3 = 36b Omega^3 I_Sigma,-1",all:"2 beta^n kappa^(2n) J_N H_p(kappa^n)",first:"72 b Omega^3 h beta^n kappa^(3n) J_N I_Sigma,-1"},
valuation:{J:"-2N on the same fixed-ray relative-density-one subfamily",deep_odd:"3n-2N+v(I_Sigma,-1) when n>=N and 2n>v(I_Sigma,-1)",tail:"at least 5n-2N",series_coefficient_bound:"v([t^k]H_p)>=-v_p(k); no false integral power-series assertion"},
remaining_domain:"Theta_+-Theta_- = true L-deep odd difference + original L-not-deep mixed-unit remainder; combine with the exact original T exterior from R662"};}
function centers(){
 const mod=(a,m)=>(a%m+m)%m;
 function inv(a,m){let b=m,x=1n,y=0n;a=mod(a,m);while(b){const q=a/b;[a,b]=[b,a-q*b];[x,y]=[y,x-q*y];}ck(a===1n,"unit old modulus");return mod(x,m);}
 const a=23776637887n,b=77586679170n,n=a*a-a*b+b*b;
 const r=[74646n,293436n,638n,44n].map(m=>{const ni=inv(n,m);return{modulus:String(m),g:[mod((a*a-b*b)*ni,m),mod((2n*a*b-b*b)*ni,m)].map(String)};});
 ck(r[0].g[0]==="1"&&r[0].g[1]==="0"&&r[1].g[0]==="146719"&&r[1].g[1]==="0","full exact centers");
 return{pi_R488:[String(a),String(b)],centers:r};
}
function certificate(input){
 const m=moments(input.mass);let den=1n;for(const P of[m.numerator_eta_plus,m.numerator_eta_minus])for(const c of P)for(const s of c){const a=s.split("/");if(a[1]){const z=BigInt(a[1]);den=den/gcd(den,z)*z;}}
 return{format:"R665 original mixed-unit odd branch and negative-one return",input:"published check-r659-frozen-gate-mass-and-full-compensation.json, mass.Pres/Pconst; same original R594 right inverse",moments:m,geometry:geometry(),centers:centers(),angle:angle(),fixed_denominator:String(den),scope:"No new ray. Both eta=+/- quadratic polynomials are retained. The complete shallow mixed-unit domain and original T exterior are not set to zero."};
}

const fs=require('fs'),path=require('path');
const input=JSON.parse(fs.readFileSync(path.join(__dirname,'check-r659-frozen-gate-mass-and-full-compensation.json'),'utf8'));
const output=JSON.stringify(certificate(input),null,2)+'\n';
if(process.argv[2])fs.writeFileSync(process.argv[2],output);else process.stdout.write(output);
