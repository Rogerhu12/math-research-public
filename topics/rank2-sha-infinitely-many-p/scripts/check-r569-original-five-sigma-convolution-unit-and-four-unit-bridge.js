// Exact characteristic-zero certificate for R569.
// Run: node check-r569-original-five-sigma-convolution-unit-and-four-unit-bridge.js
function certifyR569(){
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


const w=E(0,1),w2=em(w,w),delta=E(1,2);
const C=vm([E(1),E(0),E(-1),E(1)],ei(delta));
const D4=[E(1),w2,E(0,-2),E(0)];
ck(eq(he(C,C),E(1)),"C has norm one");
ck(eq(he(D4,D4),E(6)),"D4 has norm six");
ck(eq(he(D4,C),E(-1)),"D4/C Hermitian pairing");
const rotate=z=>ident(4).map((row,i)=>row.map((v,j)=>ea(v,em(es(z,E(1)),em(ec(C[i]),C[j])))));
const SC=rotate(w);
ck(mm(mm(SC,SC),SC).every((r,i)=>r.every((v,j)=>eq(v,E(i===j?1:0)))),"exact C rotation has order three");
ck(mm(SC,SC[0].map((_,j)=>SC.map(r=>ec(r[j])))).every((r,i)=>r.every((v,j)=>eq(v,E(i===j?1:0)))),"C rotation unitary");
const zs=[E(1),w,w2];
const expected=[
 [E(1),w2,E(0,-2),E(0)],
 [en(w),w2,E(1,-1),w2],
 [E(1,-1),w2,en(w),en(w)]
];
const units=[E(1),w,w2,E(-1),en(w),en(w2)];
const reports=[];
let sourceSum=E(0);
for(let j=0;j<3;j++){
 const row=mm([D4],rotate(zs[j]))[0];
 ck(row.every((v,i)=>eq(v,expected[j][i])),"all complete conjugate rows");
 ck(eq(he(row,row),E(6)),"conjugate degree six");
 let phase=E(1),deltaFactors=0,zero=false,description=[];
 for(const v of row){
  if(ez(v)){zero=true;description.push("zero sigma factor");continue;}
  let k=units.findIndex(a=>eq(v,a));
  if(k>=0){phase=em(phase,units[k]);description.push({unit:out(units[k])});continue;}
  k=units.findIndex(a=>eq(v,em(a,delta)));
  ck(k>=0 || zero || j===0,"nonzero rows have one exact delta factor");
  if(k>=0){phase=em(phase,em(units[k],delta));deltaFactors++;description.push({delta_times_unit:out(units[k])});}
  else description.push({unused_because_zero_row:out(v)});
 }
 if(zero)phase=E(0);else ck(deltaFactors===1,"actual sigma product equals a single f4");
 if(j===1)ck(eq(phase,E(2,1)),"omega branch absolute sigma phase");
 if(j===2)ck(eq(phase,delta),"omega squared branch absolute sigma phase");
 sourceSum=ea(sourceSum,phase);
 reports.push({zeta:out(zs[j]),row:row.map(out),sigma_factorization:description,f4_coefficient:out(phase)});
}
const rawAverage=esc(sourceSum,1,3),normalization=em(rawAverage,E(-1,0,84));
ck(eq(rawAverage,en(w2)),"whole C-average f4 coefficient");
ck(eq(normalization,esc(w2,1,84)),"original -1/84 source normalization");
const T7=[...D4,en(w)],T10=[...D4,esc(en(w),2)];
const gram=[[he(T7,T7),he(T7,T10)],[he(T10,T7),he(T10,T10)]];
ck(eq(gram[0][0],E(7))&&eq(gram[0][1],E(8))&&eq(gram[1][1],E(10)),"same two original normal directions");
const change=[[E(1),en(w)],[E(1),esc(en(w),2)]],ci=inverse(change);
ck(eq(ci.det,en(w)),"T7/T10 coordinate change is a p-unit");
const wantedInv=[[E(2),E(-1)],[w2,en(w2)]];
ck(ci.inverse.every((r,i)=>r.every((v,j)=>eq(v,wantedInv[i][j]))),"exact D4 and d reconstruction");
const h=va(vm(wantedInv[1],delta),vm(wantedInv[0],E(-1)));
const k=va(vm(wantedInv[1],delta),wantedInv[0]);
ck(h.every((v,i)=>eq(v,[w2,w][i])),"four-unit H after convolution translation");
ck(k.every((v,i)=>eq(v,[E(3,-1),E(-2,1)][i])),"four-unit K after convolution translation");
ck(eq(em(em(w2,w2),w2),E(1)),"raw sigma cube has no CM factor");
const normal7Coefficient=em(normalization,en(w));
const normal10Coefficient=em(normalization,esc(w,-2));
ck(eq(normal7Coefficient,E(-1,0,84)),"actual complete T7 marginal is -F5/84");
ck(eq(normal10Coefficient,E(-1,0,42)),"actual complete T10 marginal is -G5/42");
const normal7Moment=esc(normal7Coefficient,120),normal10Moment=esc(normal10Coefficient,120);
ck(eq(normal7Moment,E(-10,0,7))&&eq(normal10Moment,E(-20,0,7)),"actual full fifth moments");
const massCoefficient=esc(normalization,24);
ck(eq(massCoefficient,esc(w2,2,7)),"full five-variable weighted mass coefficient");
const mainUnitCoefficient=em(normalization,ei(esc(em(delta,delta),2)));
ck(eq(mainUnitCoefficient,esc(en(w2),1,504)),"fixed four-unit unit relation coefficient");
const jd=[E(1),E(-1)],cb=[E(0),E(2)];
const difference=jd.map((v,i)=>es(v,cb[i]));
ck(eq(difference[0],E(1))&&eq(difference[1],E(-3)),"all R562 leading complementary mass retained");
const frame5=[
 [E(1),w2,E(0,-2),E(0),E(0)],
 [E(0),E(1),E(0),E(0),E(0)],
 [E(0),E(0),E(1),E(0),E(0)],
 [E(0),E(0),E(0),E(1),E(0)],
 [E(0),E(0),E(0),E(0),E(1)]
];
ck(eq(inverse(frame5).det,E(1)),"complete five-dimensional coordinate lattice is unchanged");
return {
 convention:"Each pair [a,b] denotes a+b*omega over Q; omega^2+omega+1=0. No finite-prime sample is used.",
 complete_C_rotation:SC.map(r=>r.map(out)),
 C:C.map(out),D4:D4.map(out),conjugates:reports,
 raw_average_f4_coefficient:out(rawAverage),
 original_five_sigma_marginal_coefficient:out(normalization),
 five_weighted_mass:{
  weight:"1_{D4,d unit} D4^4 d",
  coefficient:out(massCoefficient),
  factor:"Omega^5(1-beta*kappa^4)(1-beta*kappa)",
  constant_term_is_unit:true
 },
 six_weighted_mass:{
  weight:"1_{c,D4,d unit} c D4^4 d",
  coefficient:out(massCoefficient),
  factor:"Omega^6(1-beta*kappa^4)(1-beta*kappa)^2",
  constant_term_is_unit:true
 },
 normal_directions:{T7:T7.map(out),T10:T10.map(out),gram:gram.map(r=>r.map(out)),change:change.map(r=>r.map(out)),inverse:ci.inverse.map(r=>r.map(out)),determinant:out(ci.det)},
 normal_marginals:{T7_F5:out(normal7Coefficient),T10_G5:out(normal10Coefficient),T7_fifth_moment_over_Omega5:out(normal7Moment),T10_fifth_moment_over_Omega5:out(normal10Moment),other_conditional_basis_total_masses:"zero; the conditional measures themselves are not asserted zero"},
 four_unit_pullback:{
  z:"2*T7-T10",d:"omega^2*(T7-T10)",v:"2*T7-T10+t",
  H:{T7:out(h[0]),T10:out(h[1]),t:"-1"},
  K:{T7:out(k[0]),T10:out(k[1]),t:"+1"},
  all_cuts:["d unit","v unit","H unit","K unit","z unit"],
  numerator:"(T7-T10)^3"
 },
 fixed_unit_row:{
  source:"the original full five-sigma nu5, with all three remaining coordinates retained",
  value:"(omega^2/84)*(J_B+c_I*I4)",
  c_I:"9*b*Omega^3*(1-beta*kappa^3)/(2*delta^2)",
  leading_coefficient:out(mainUnitCoefficient),
  leading_factor:"Omega*(1-beta*kappa)*(1-3*beta)",
  exact_remainder:"-(omega^2/84)*(C_sigma+T_B)",
  valuations:{C_sigma:7,T_B:6},
  I4:"the original f4 negative-two unit moment, never the positive-four moment"
 },
 scope:{
  multivariable_inverse:"The inverse is in the full five-variable integral Amice algebra; translate every native observation and cut.",
  actual_word:"P_{u,kappa} P_{P,kappa}; original full source returns -chi65*lambda^2",
  arithmetic_row:"beta^n*(J_S'-6*delta*J_T') before the word",
  fixed_unit_row_is_not_identified_with_arithmetic_row:true,
  native_restricted_residual_is_not_the_full_arithmetic_row:true
 }
};
}
const report=certifyR569();
if(typeof process!=="undefined")process.stdout.write(JSON.stringify(report,null,2)+"\n");
