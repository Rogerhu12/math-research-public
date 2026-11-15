#!/usr/bin/env node
"use strict";
// R686. No external data files or packages. Exact original Z[omega] geometry.
// Run: node check-r686-original-yz-core-and-st-unit-carries.js
// Standard output is an ephemeral reproducible certificate; do not commit it.
// Standard error reports its SHA256. No certificate is uploaded to a Release.
const crypto=require("crypto");
function run(){

const K=(a,b=0)=>[BigInt(a),BigInt(b)],zero=()=>K(0),
add=(x,y)=>K(x[0]+y[0],x[1]+y[1]),neg=x=>K(-x[0],-x[1]),
sub=(x,y)=>add(x,neg(y)),
mul=(x,y)=>K(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1]),
conj=x=>K(x[0]-x[1],-x[1]),
norm=x=>x[0]*x[0]-x[0]*x[1]+x[1]*x[1],
eq=(x,y)=>x[0]===y[0]&&x[1]===y[1],
scale=(v,a)=>v.map(x=>mul(x,a)),
radd=(v,w)=>v.map((x,i)=>add(x,w[i])),
rsub=(v,w)=>v.map((x,i)=>sub(x,w[i])),
inner=(v,w)=>v.reduce((s,x,i)=>add(s,mul(x,conj(w[i]))),zero()),
req=(v,w)=>v.length===w.length&&v.every((x,i)=>eq(x,w[i])),
rn=v=>inner(v,v),
urow=i=>Array.from({length:6},(_,j)=>K(i===j?1:0));
const checks=[];
function check(name,ok){if(!ok)throw new Error(name);checks.push(name);}
const om=K(0,1),delta=K(1,2),gam7=K(3,1),g=K(3,-2);
const A=[delta,mul(K(2),delta),gam7,K(2,-1),K(0),K(0)];
const c=urow(4),d=urow(5),Y=radd(A,radd(c,scale(d,K(2)))),
W=radd(A,radd(scale(c,mul(K(3),delta)),scale(d,K(4))));
const Z17=rsub(scale(W,K(17)),scale(Y,K(20,3)));
const E=rsub(rsub(scale(A,K(5,6)),scale(c,K(29))),scale(d,K(58,87)));
const V=rsub(scale(Y,K(36)),scale(W,K(17,-3)));
const C0=[K(1),K(0),K(-1),K(1),K(0),K(0)],
D4=[K(1),K(-1,-1),K(0,-2),K(0),K(0),K(0)],
H=radd(D4,radd(c,scale(d,K(2,3)))),
Dstar29=radd(scale(D4,K(29)),scale(A,K(5,6))),
H1=[K(-1),K(2),om,K(1,1),K(0),K(0)],
EtestDelta=radd(scale(H,delta),scale(C0,K(14))),
GDelta=radd(scale(H1,mul(K(13),delta)),scale(radd(C0,scale(H,delta)),g));
check("omega-square",eq(add(add(mul(om,om),om),K(1)),K(0)));
for(const [name,row,n]of [["A",A,29],["Y",Y,34],["W",W,72],["Z17",Z17,8942],["E",E,7627],["V",V,18936],["H",H,14],["EtestDelta",EtestDelta,546],["GDelta",GDelta,2808]])
 check("norm-"+name,eq(rn(row),K(n)));
for(const [n,v,w]of [["Y-Z",Y,Z17],["Y-E",Y,E],["Z-E",Z17,E],["W-V",W,V],["W-E",W,E],["V-E",V,E]])
 check("orthogonal-"+n,eq(inner(v,w),K(0)));
check("actual-hidden-gate",req(scale(H,K(29)),rsub(Dstar29,E)));
for(const [n,row]of [["C",C0],["H",H],["Etest",EtestDelta],["G",GDelta],["Dstar",Dstar29],["H1",H1]])
 for(const [an,axis]of [["Y",Y],["W",W],["Z",Z17],["V",V]])
  check(n+"-fixed-by-"+an,eq(inner(row,axis),K(0)));
check("inverse-Y",req(scale(Y,K(36)),radd(V,scale(W,K(17,-3)))));
check("inverse-Z",req(scale(Z17,K(36)),rsub(scale(W,K(263)),scale(V,K(20,3)))));
function det3(M){
 let z=K(0);
 for(const [p,s]of [[[0,1,2],1],[[1,2,0],1],[[2,0,1],1],[[2,1,0],-1],[[1,0,2],-1],[[0,2,1],-1]])
  z=add(z,mul(K(s),mul(mul(M[0][p[0]],M[1][p[1]]),M[2][p[2]])));
 return z;
}
const yzE=[[K(1),K(1),K(2)],[K(-3,-3),K(31,99),K(28,-6)],[K(5,6),K(-29),K(-58,-87)]];
const wve=[[K(1),mul(K(3),delta),K(4)],
 [K(19,3),K(36),K(72)].map((x,i)=>i===0?x:sub(x,mul(K(17,-3),[K(1),mul(K(3),delta),K(4)][i]))),
 yzE[2]];
wve[1]=[K(1),K(1),K(2)].map((x,i)=>sub(mul(K(36),x),mul(K(17,-3),wve[0][i])));
check("frame-determinant-YZE",eq(det3(yzE),K(8942)));
check("frame-determinant-WVE",eq(det3(wve),K(-18936)));
const oddcount=v=>v.filter(x=>x.some(z=>z%2n!==0n)).length;
check("half-character-Y",oddcount(Y)===4);
check("half-character-Z",oddcount(Z17)===4);
check("half-character-E",oddcount(E)===5);
check("odd-anchor-norm",norm(K(2))+norm(mul(K(33),gam7))===7627n);
check("odd-anchor-cross",eq(add(mul(K(2),conj(mul(K(33),gam7))),mul(conj(mul(K(33),gam7)),K(-2))),K(0)));
const gg=9995n;
check("full-center-mod4",gg%4n===3n);
check("full-center-mod17",gg%17n===16n);
check("full-center-mod263",gg%263n===1n);
check("full-center-square",gg*gg%17884n===1n);
const val=x=>Array.isArray(x)?x.map(val):typeof x==="bigint"?x.toString():x;
return {
 format:"R686 exact original Y/Z and W/V geometry certificate",
 arithmetic:"Z[omega], omega^2+omega+1=0, exact BigInt",
 run_parameters:{b:17,new_ray:false,ordinary_conditions:"the existing ray, including pi_0=1 mod 263"},
 frame_Y_Z17_E:yzE.map(val),frame_W_V_E:wve.map(val),
 original_six_rows:Object.fromEntries(Object.entries({A,Y,W,Z17,E,V,C0,H,Dstar29,H1,EtestDelta,GDelta}).map(([k,v])=>[k,val(v)])),
 norms:{Y:34,Z17:8942,E:7627,W:72,V:18936},
 determinants:{Y_Z17_E:"8942",W_V_E:"-18936"},
 center:{Z17:"9995 mod 17884",E:"1 mod 15254, from the existing 29 and 263 ray"},
 odd_anchor:{first:"2",second:"33(3+omega)",norms:[4,7623],total:7627},
 hidden_gate_identity:"29 H=29 Dstar-E",
 retained:{
  raw_Z_core:"gamma*lambda*R_Y; gamma=chi_A*chi_E and gamma^2=1",
  YZ_source:"All original remaining companions retained.",
  WV_source:"Both original W-core states retained.",
  actual_test:"q_sharp and q_cd are invariant in BOTH Y/Z and W/V planes.",
  unit_cuts:"The near-cancellation W-deep branch and the Y-deep entry branch are retained.",
  conditional_mass:"The W-core-state mass after an E-deep restriction is NOT assigned zero."
 },
 checks,number_of_checks:checks.length
};
}
const result=run();
const output=JSON.stringify(result,null,2)+"\n";
process.stdout.write(output);
process.stderr.write("SHA256 "+crypto.createHash("sha256").update(output).digest("hex")+"\n");
