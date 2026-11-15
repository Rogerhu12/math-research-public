#!/usr/bin/env node
"use strict";
// R695: run only in public Actions. No input data, network or third-party packages.
// The reproducible output is ephemeral; commit only this script, run ID and hash.
const crypto=require("crypto");
const abs=x=>x<0n?-x:x,gcd=(a,b)=>{a=abs(a);b=abs(b);while(b){const t=a%b;a=b;b=t;}return a;};
function q(a,b=1n){if(Array.isArray(a))return a;a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const d=gcd(a,b);return[a/d,b/d];}
const qa=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),
qn=a=>q(-a[0],a[1]),qm=(a,b)=>q(a[0]*b[0],a[1]*b[1]),
qi=a=>q(a[1],a[0]),qe=(a,b)=>a[0]===b[0]&&a[1]===b[1];
const k=(a=0,b=0)=>[q(a),q(b)],ka=(a,b)=>[qa(a[0],b[0]),qa(a[1],b[1])],
kn=a=>[qn(a[0]),qn(a[1])],ks=(a,b)=>ka(a,kn(b)),
km=(a,b)=>[qa(qm(a[0],b[0]),qn(qm(a[1],b[1]))),qa(qa(qm(a[0],b[1]),qm(a[1],b[0])),qn(qm(a[1],b[1])))],
kc=a=>[qa(a[0],qn(a[1])),qn(a[1])],
ke=(a,b)=>qe(a[0],b[0])&&qe(a[1],b[1]),kz=a=>a[0][0]===0n&&a[1][0]===0n;
const norm=a=>km(a,kc(a))[0],ki=a=>{const z=norm(a);return kc(a).map(x=>qm(x,qi(z)));},
kd=(a,b)=>km(a,ki(b)),sc=(a,n,d=1)=>km(a,k(q(n,d)));
const K0=k(),K1=k(1),om=k(0,1),del=k(1,2),eA=k(5,6),
sum=xs=>xs.reduce(ka,K0),rv=(v,a)=>v.map(x=>km(x,a)),
va=(v,w)=>v.map((x,i)=>ka(x,w[i])),vs=(v,w)=>va(v,rv(w,k(-1))),
mm=(a,b)=>a.map(row=>b[0].map((_,j)=>sum(row.map((x,i)=>km(x,b[i][j]))))),
rm=(r,a)=>a[0].map((_,j)=>sum(r.map((x,i)=>km(x,a[i][j])))),
ve=(v,w)=>v.length===w.length&&v.every((x,i)=>ke(x,w[i])),
me=(a,b)=>a.every((r,i)=>ve(r,b[i]));
const I=Array.from({length:3},(_,i)=>Array.from({length:3},(_,j)=>k(i===j?1:0)));
const checks=[];function check(name,ok){if(!ok)throw Error(name);checks.push(name);}
const A=[k(1),k(),k()],Q=[k(),k(1),k()],L=[k(),k(),k(1)],Y=va(A,Q),
bQ=sc(k(11,6),1,5),bL=sc(k(2,12),1,5),bY=sc(k(20,3),1,17),aa=k(17,-3),
W=va(va(A,rv(Q,bQ)),rv(L,bL)),
Z=vs(W,rv(Y,bY)),
E=[eA,sc(eA,-29,5),sc(om,87,5)],
V=vs(rv(Y,k(36)),rv(W,aa));
const C=[Y,Z,E],Cinv=[
[k(q(29,34)),sc(om,87,526),sc(k(1,6),-1,263)],
[k(q(5,34)),sc(om,-87,526),sc(k(1,6),1,263)],
[k(),sc(eA,-17,263),sc(kc(om),3,263)]
];
check("full_YZE_inverse_left",me(mm(Cinv,C),I));
check("full_YZE_inverse_right",me(mm(C,Cinv),I));
const diag=[k(29),k(5),k(5)],ip=(a,b)=>sum(a.map((x,i)=>km(km(x,diag[i]),kc(b[i]))));
check("Gram_Y",ke(ip(Y,Y),k(34)));
check("Gram_Z",ke(ip(Z,Z),k(q(526,17))));
check("Gram_E",ke(ip(E,E),k(7627)));
for(const [i,j]of[[0,1],[0,2],[1,2]])check("Gram_cross_"+i+j,kz(ip(C[i],C[j])));
check("Gram_W",ke(ip(W,W),k(72)));
check("Gram_V",ke(ip(V,V),k(18936)));
check("Gram_WV",kz(ip(W,V)));
function projector(row,N){const col=row.map((x,i)=>kd(km(diag[i],kc(x)),N));return col.map(x=>row.map(y=>km(x,y)));}
const PA=projector(A,k(29)),PW=projector(W,k(72)),PY=projector(Y,k(34));
const aW=sc(aa,1,36),cA=k(q(29,72)),a0=sc(eA,-1,29),bF=sc(eA,1,5),ell0=sc(om,-3,5),
H=[a0,bF,ell0];
check("P_A_idempotent",me(mm(PA,PA),PA));
check("P_W_idempotent",me(mm(PW,PW),PW));
check("P_Y_idempotent",me(mm(PY,PY),PY));
check("Y_PW",ve(rm(Y,PW),rv(W,aW)));
check("A_PW",ve(rm(A,PW),rv(W,cA)));
check("H_is_minus_E_over29",ve(H,rv(E,k(q(-1,29)))));
check("H_PY_zero",ve(rm(H,PY),[K0,K0,K0]));
check("H_PW_zero",ve(rm(H,PW),[K0,K0,K0]));
check("H_PA_equals_a0_A",ve(rm(H,PA),rv(A,a0)));
check("A_PY",ve(rm(A,PY),rv(Y,k(q(29,34)))));
check("Q_PY",ve(rm(Q,PY),rv(Y,k(q(5,34)))));
check("L_PY_zero",ve(rm(L,PY),[K0,K0,K0]));
check("corner_Z_Q",ke(Z[1],sc(k(1,1),87,85)));
check("corner_V_Q",ke(V[1],sc(k(25,87),-1,5)));
check("corner_V_numerator_norm",qe(norm(k(25,87)),q(13*463)));
check("ordinary_ray_excludes_463",463%64!==7);
// Symbolic polynomials in x=kappa^{-1}; coefficients in Q(omega).
function pn(a){a=a.slice();while(a.length>1&&kz(a[a.length-1]))a.pop();return a;}
const pc=a=>[a],p0=pc(K0),p1=pc(K1),
pa=(a,b)=>pn(Array.from({length:Math.max(a.length,b.length)},(_,i)=>ka(a[i]||K0,b[i]||K0))),
pm=(a,b)=>{let r=Array.from({length:a.length+b.length-1},()=>K0);a.forEach((x,i)=>b.forEach((y,j)=>{r[i+j]=ka(r[i+j],km(x,y));}));return pn(r);},
ps=(a,b)=>pa(a,b.map(kn)),pe=(a,b)=>{a=pn(a);b=pn(b);return a.length===b.length&&a.every((x,i)=>ke(x,b[i]));},
psum=xs=>xs.reduce(pa,p0),prv=(v,a)=>v.map(x=>pm(x,a)),pva=(a,b)=>a.map((x,i)=>pa(x,b[i])),
prm=(r,a)=>a[0].map((_,j)=>psum(r.map((x,i)=>pm(x,a[i][j])))),
pmm=(a,b)=>a.map(r=>b[0].map((_,j)=>psum(r.map((x,i)=>pm(x,b[i][j]))))),
pve=(a,b)=>a.every((x,i)=>pe(x,b[i]));
const dA=[k(-1),K0,K1],dW=[k(-1),K1],
lift=v=>v.map(pc),pY=lift(Y),pA=lift(A),pW=lift(W),pH=lift(H);
function invMap(P,d){return I.map((r,i)=>r.map((x,j)=>pa(pc(x),pm(d,pc(P[i][j])))));}
const MA=invMap(PA,dA),MW=invMap(PW,dW),
plusInv=pmm(MW,MA),minusInv=pmm(MA,MW);
const Yplus=pva(pva(pY,prv(pW,pm(dW,pc(aW)))),prv(pA,pm(dA,pa(p1,pm(dW,pc(aW)))))),
Yminus=pva(pva(pY,prv(pA,dA)),prv(pW,pm(dW,pa(pc(aW),pm(dA,pc(cA))))));
check("word_plus_Y_exact",pve(prm(pY,plusInv),Yplus));
check("word_minus_Y_exact",pve(prm(pY,minusInv),Yminus));
const Ydiff=prv(pva(prv(pA,pc(aW)),prv(pW,pc(kn(cA)))),pm(dA,dW));
check("word_Y_difference",pve(pva(Yplus,prv(Yminus,pc(k(-1)))),Ydiff));
const Hplus=pva(pH,prv(pA,pm(pc(a0),dA))),
Hminus=pva(pH,prv(pva(pA,prv(pW,pm(dW,pc(cA)))),pm(pc(a0),dA)));
check("word_plus_full_H_shift",pve(prm(pH,plusInv),Hplus));
check("word_minus_full_H_shift",pve(prm(pH,minusInv),Hminus));
check("word_plus_W_gate",pve(prm(pW,MA),pva(pW,prv(pA,dA))));
check("word_minus_A_gate",pve(prm(pA,MW),pva(pA,prv(pW,pm(dW,pc(cA))))));
const R=[[1n,0n,0n],[0n,0n,1n],[0n,1n,0n]],K=[[0n,1n,-1n],[1n,0n,-1n],[0n,0n,-1n]],
imv=(a,v)=>a.map(r=>r.reduce((z,x,i)=>z+x*v[i],0n)),e0=[1n,0n,0n],
eqv=(a,b)=>a.every((x,i)=>x===b[i]);
check("word_plus_returns_e1",eqv(imv(K,imv(R,e0)),[0n,1n,0n]));
check("word_minus_returns_e2",eqv(imv(R,imv(K,e0)),[0n,0n,1n]));
// Complete fixed first-CM label set. This is not a target-prime scan.
const units=[k(1),om,kc(om),k(-1),kn(om),kn(kc(om))],
g13=k(4,1),g19=k(5,2),labels=[];
const key=x=>JSON.stringify(x,(_,z)=>typeof z==="bigint"?z.toString():z);
let ap=k(1);
for(let j=0;j<18;j++){
 for(let e=0;e<2;e++){const alpha=e?km(ap,g19):ap;
  for(let u=0;u<6;u++)labels.push({j,e,u,alpha,scale:km(units[u],kd(kc(alpha),alpha))});
 }
 ap=km(ap,g13);
}
check("216_CM_scales",labels.length===216);
check("all_CM_scales_distinct",new Set(labels.map(z=>key(z.scale))).size===216);
for(let i=0;i<labels.length;i++)check("CM_scale_norm_one_"+i,qe(norm(labels[i].scale),q(1)));
const m=13n**17n*19n**5n;
check("fixed_odd_cover_coprime",gcd(m,2n*3n*5n*7n*11n*17n*29n*263n)===1n);
check("fixed_cover_square_mod16",m*m%16n===1n);
const payload={
 result:"R695 actual CM word geometry and A/Z full gate transport",
 convention:"omega^2+omega+1=0; x is the formal indeterminate kappa^{-1}",
 parameters:{N:"positive multiple of four",r_k_n:"k<n<2r; k>=3 and 2r-2>k for the two-word intersection",cm_cover:m.toString()},
 first_rows:{A,Q,L,Y,Z,E,W,V},YZE_inverse:Cinv,
 source_matrices:{R,K},word_formulas:{Yplus,Yminus,Hplus,Hminus},
 cm_labels:labels,
 full_gate_statements:[
  "Deep A: both H gates agree only when v(A)>=N+2; keep every Taylor term through degree twelve.",
  "For 2<=v(A)<N+2 the original and shifted H gates are disjoint.",
  "In the original corner the two returned Y valuations are k-1 and k-3.",
  "The CM scale changes A to A+(29/34)(s^{-1}-1)Y and fixes L.",
  "The raw CM fibre sum and the outside unit scale are both retained.",
  "A numerical or reference nonzero row does not eliminate any exterior integral."
 ],
 checks,number_of_checks:checks.length
};
const output=JSON.stringify(payload,(_,x)=>typeof x==="bigint"?x.toString():x,2)+"\n";
process.stdout.write(output);
process.stderr.write("SHA256 "+crypto.createHash("sha256").update(output).digest("hex")+"\n");
