#!/usr/bin/env node
// Exact certificate for R599. No external packages.
const report=(()=>{
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

function ep(x,n){let y=E(1);for(let j=0;j<n;j++)y=em(y,x);return y;}
const delta=E(1,2), az=E(-2,1,2), aq=E(4,3,2);
const b3=em(esc(delta,4),es(E(1),esc(delta,6)));
const a5=em(ep(aq,2),b3);
const c3=esc(em(b3,ei(ep(az,3))),-1,21);
const c5=esc(em(a5,ei(ep(az,5))),4,7);
const norm=x=>em(x,ec(x));
const deepY=[aq,esc(delta,2),E(1),E(2)];
const deepW=[aq,esc(delta,2),esc(delta,3),E(4)];
const prod=x=>x.reduce(em,E(1));
const m3=esc(es(prod(deepY.slice(1)),prod(deepW.slice(1))),6);
const m5=esc(em(ep(aq,2),es(prod(deepY.slice(1)),prod(deepW.slice(1)))),120);
ck(eq(m3,esc(b3,6)),"complete Theta-channel cubic moment");
ck(eq(m5,esc(a5,120)),"complete Sigma-channel quintic moment, including Sigma m2=2");
ck(eq(c3,esc(em(m3,ei(ep(az,3))),-1,126)),"cubic log coefficient");
ck(eq(c5,esc(em(m5,ei(ep(az,5))),1,210)),"quintic log coefficient");
ck(eq(c3,E(10400,11008,7203)),"c3 exact");
ck(eq(c5,E(4312960,1031168,117649)),"c5 exact");
ck(eq(norm(c3),E(2n**10n*109n,0,3n*7n**5n)),"c3 norm");
ck(eq(norm(c5),E(2n**14n*3n*13n**2n*109n,0,7n**7n)),"c5 norm");
ck(109%64===45&&45!==7,"109 excluded by existing p=7 mod64 ray");
const serialNorm=x=>out(norm(x))[0];
const data={
format:"R599 exact full original five-input low-depth return; rational CM pairs [a,b] mean a+b*omega",
normalization:{b:"17",beta:"-lambda",kappa:"p*lambda^2",dp:"p-1",flat_factor:"1/42",
negative_five:"I1=integral_{Z unit} Z^(-5) dnu_f1",
negative_three:"I3=integral_{Z unit} Z^(-3) dnu_f3, not assumed zero",
four_deep_core:"beta^(4n)"},
observations:{az:out(az),aq:out(aq),deepY:deepY.map(out),deepW:deepW.map(out)},
exact_coefficients:{b3:out(b3),a5:out(a5),m3_without_Omega3:out(m3),m5_without_Omega5:out(m5),c3:out(c3),c5:out(c5)},
norms:{az:serialNorm(az),aq:serialNorm(aq),b3:serialNorm(b3),a5:serialNorm(a5),c3:serialNorm(c3),c5:serialNorm(c5)},
full_series:{
Sigma_channel:"A5(t)=Sigma(aq*t)*sigma(2delta*t)*(sigma(t)*sigma(2t)-sigma(3delta*t)*sigma(4t)); support 5 mod6",
Theta_channel:"B3(t)=Theta(aq*t)*sigma(2delta*t)*(sigma(t)*sigma(2t)-sigma(3delta*t)*sigma(4t)); support 3 mod6",
range:"all original Z-unit negative powers retained; both actual Y/W unit conditions automatic only on the stated rectangle",
moment_tail_bound:"v_p(coefficient at t^m after log)>=-v_p(m)",
source_depth:"R_n=beta^(4n)*dp*(c3*Omega^3*kappa^(3n)*I3+c5*Omega^5*kappa^(5n)*I1)+p^(9n)O"},
complete_compensation:{
O_n:"integral_{Funit outside rectangle} Wtilde_n*ell dnu_flat",
K_n:"integral_rectangle (Wtilde_n-beta^n)*ell dnu_flat",
E_n:"beta^(-n)*(O_n+K_n)=T-R_n",
T:"Jprime_S-6delta*Jprime_T",
B_n:"(1-beta^4*kappa^3)*T-E_(n+1)+beta^4*kappa^3*E_n",
identity:"B_n=R_(n+1)-beta^4*kappa^3*R_n",
negative_five_return:"B_n/[dp*c5*Omega^5*beta^(4(n+1))*kappa^(5n+3)*(kappa^2-1)] = I1 + p^(4n)O",
exact_limit:"the displayed quotient tends to I1 as n tends to infinity",
zero_case:"if I1=0 then v_p(B_n)>=9n+3; T is not assumed zero unless both original central rows are set zero",
q_invariance:"E_n is unchanged between old q6 and new qtilde; O_n and K_n individually need not be unchanged"
},
new_bad_primes:"none; only 2,3,7,13,109 appear in coefficient norms; 109 violates existing p=7 mod64 ray",
assertions:"all exact CM coefficients, two full lowest tensor moments, and coefficient norms passed"
};
return data;

})();
process.stdout.write(JSON.stringify(report,null,2)+"\n");
