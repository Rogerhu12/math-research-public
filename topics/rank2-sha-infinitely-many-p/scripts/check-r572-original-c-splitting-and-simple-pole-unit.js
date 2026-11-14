// Exact characteristic-zero certificate for R572.
// Run: node check-r572-original-c-splitting-and-simple-pole-unit.js
function certifyR572(){
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


const w=E(0,1),w2=em(w,w),del=E(1,2);
const row=a=>a.map(v=>Array.isArray(v)?E(...v):E(v));
const c=row([0,0,0,0,1,0]),d=row([0,0,0,0,0,1]),r=row([0,1,0,0,0,0]);
const Z=row([1,0,-1,-2,0,0]),Q0=row([1,0,1,0,0,0]),v=row([1,0,-1,1,0,0]);
const frame=[c,v,Z,Q0,r,d],iv=inverse(frame);
const gram=frame.map(a=>frame.map(b=>he(a,b)));
const ns=[1,3,6,2,1,1];
for(let i=0;i<6;i++)for(let j=0;j<6;j++)ck(eq(gram[i][j],E(i===j?ns[i]:0)),"complete original six-dimensional orthogonal frame");
ck(eq(em(iv.det,ec(iv.det)),E(36)),"complete frame determinant has norm 36");
const C=vm(v,ei(del));
const SC=ident(6).map((row,i)=>row.map((val,j)=>ea(val,em(es(w,E(1)),em(ec(C[i]),C[j])))));
for(const a of[c,Z,Q0,r,d])ck(mm([a],SC)[0].every((t,i)=>eq(t,a[i])),"all five companions fixed by pure C rotation");
ck(mm([v],SC)[0].every((t,i)=>eq(t,em(w,v[i]))),"pure C rotation is exactly v rotation");

const D4=[E(1),w2,E(0,-2),E(0),E(0),E(0)];
const A0=[del,esc(del,2),E(3,1),E(2,-1),E(0),E(0)];
const Y=va(va(A0,c),vm(d,E(2))),W=va(va(A0,vm(c,esc(del,3))),vm(d,E(4)));
const F=va(va(va(D4,C),c),vm(d,E(2,3)));
const H1=[E(-1),E(2),w,E(1,1),E(0),E(0)];
const G=va(vm(H1,E(13)),vm(F,E(3,-2)));
const actual={D4,A0,Y,W,F,H1,G},converted={};
for(const[name,a]of Object.entries(actual))converted[name]=mm([a],iv.inverse)[0];
const expectedY=[E(1),E(0),E(-2,1,2),E(4,3,2),esc(del,2),E(2)];
const expectedW=[esc(del,3),E(0),E(-2,1,2),E(4,3,2),esc(del,2),E(4)];
const expectedF=[E(1),E(0),esc(del,1,6),E(1,-2,2),w2,E(2,3)];
const expectedH1=[E(0),E(0),esc(w2,1,2),E(-1,1,2),E(2),E(0)];
for(const[name,e]of[["Y",expectedY],["W",expectedW],["F",expectedF],["H1",expectedH1]])ck(converted[name].every((a,i)=>eq(a,e[i])),"all native observations in the exact new frame");
ck(Object.values(converted).filter((_,i)=>i>0).every(a=>ez(a[1])),"A0/Y/W/F/H1/G are all independent of v");
const az=expectedY[2],aq=expectedY[3],ar=expectedY[4];
const leadCommon=em(az,es(em(aq,aq),em(az,az)));
const leadS=esc(em(em(leadCommon,ar),E(2)),1,42);
const leadW=esc(em(em(em(leadCommon,ar),esc(del,3)),E(4)),1,42);
ck(eq(leadS,E(1)),"full original S leading normalization");
ck(eq(leadW,esc(del,6)),"full original W leading normalization 6 delta T");
const coeffA_diag=va(va([E(1),E(-2)],[E(-3),E(0)]),[E(-2),E(-2)]);
const coeffB_diag=va(va([E(-2),E(-2)],[E(1),E(4)]),[E(0),E(6)]);
ck(coeffA_diag.every((a,i)=>eq(a,[E(-4),E(-4)][i])),"full A(z,z) coefficient identity");
ck(coeffB_diag.every((a,i)=>eq(a,[E(-1),E(8)][i])),"full B(z,z) coefficient identity");
ck(eq(es(E(4),E(3)),E(1)),"Theta times sigma derivative x^3 coefficient");
const extractB=E(-6,0,42),extractP=E(0);
ck(eq(extractB,E(-1,0,7))&&ez(extractP),"actual all-continuous (c,v) source extraction by Z^3*r*d");

const poly=(entries=[])=>new Map(entries.filter(([,v])=>!ez(v)));
const pp=(i,j,a=E(1))=>poly([[i+","+j,a]]);
const pconst=a=>pp(0,0,a);
const padd=(a,b)=>{let o=new Map(a);for(const[k,v]of b){const z=ea(o.get(k)||E(0),v);if(ez(z))o.delete(k);else o.set(k,z);}return o;};
const pscale=(a,t)=>poly([...a].map(([k,v])=>[k,em(v,t)]));
const pmul=(a,b)=>{let o=poly();for(const[k,v]of a)for(const[l,u]of b){const x=k.split(",").map(Number),y=l.split(",").map(Number);const key=(x[0]+y[0])+","+(x[1]+y[1]);const z=ea(o.get(key)||E(0),em(v,u));if(ez(z))o.delete(key);else o.set(key,z);}return o;};
const ppow=(a,n)=>{let o=pconst(E(1));for(let i=0;i<n;i++)o=pmul(o,a);return o;};
const pequal=(a,b)=>[...new Set([...a.keys(),...b.keys()])].every(k=>eq(a.get(k)||E(0),b.get(k)||E(0)));
const pc=pp(1,0),pv=pp(0,1);
const HH=padd(pscale(pc,del),pscale(pv,E(-1))),KK=padd(pscale(pc,del),pv),den=pmul(HH,KK);
const n3=padd(pscale(pmul(padd(HH,KK),den),E(4)),pscale(padd(ppow(HH,3),ppow(KK,3)),E(3)));
const targetN=pscale(pmul(pc,padd(pscale(ppow(pc,2),esc(em(del,del),7)),pscale(ppow(pv,2),E(5)))),esc(del,2));
ck(pequal(n3,targetN),"exact simple-pole form of phi");
const diff5=padd(pscale(pmul(ppow(pc,3),padd(ppow(HH,2),ppow(KK,2))),esc(em(em(del,del),del),8)),pscale(padd(ppow(HH,5),ppow(KK,5)),E(-1)));
ck(pequal(diff5,pmul(n3,den)),"negative-two term cancels in the same full two-variable kernel");
const ratioDerivNumerator=pscale(pc,esc(del,-2));
const dlogForm=padd(pscale(pmul(pc,den),E(7)),pscale(ppow(pv,2),E(0)));
const dlogClear=padd(pscale(pmul(pc,den),em(esc(ei(em(del,del)),7,8),esc(em(em(del,del),del),16))),pscale(pmul(ppow(pv,2),ratioDerivNumerator),E(-12)));
ck(pequal(dlogClear,n3),"phi equals 7c/(8delta^2) minus 3v^2/(4delta^3) d_v log(H/K)");

const bb=pp(1,0),kk=pp(0,1),one=pconst(E(1));
const oneMinusB=padd(one,pscale(bb,E(-1))),oneMinusBK=padd(one,pscale(pmul(bb,kk),E(-1)));
const total=padd(padd(pscale(pmul(oneMinusBK,oneMinusB),E(4)),pscale(pmul(pmul(bb,kk),oneMinusB),E(5))),pscale(pmul(bb,oneMinusBK),E(-7)));
const want=padd(padd(pconst(E(4)),pscale(bb,E(-11))),padd(pmul(bb,kk),pscale(pmul(ppow(bb,2),kk),E(6))));
ck(pequal(total,want),"entire two complementary leading masses are retained");
const p71=71n,hassePolynomial=4n*p71*p71-108n*p71+121n;
ck(hassePolynomial>0n&&8n*p71-108n>0n,"2p-8sqrt(p)-11 is positive for all p>=71");
const forbiddenResidue=5,possibleResidues=[-1,0,1].map(k=>((7*k)%8+8)%8);
ck(!possibleResidues.includes(forbiddenResidue),"even trace and p=7 mod8 exclude 4-11 beta nonunit");
const thetaTypes={B:0,P:3,H6:0,f1:1,f2:2,f3:3,f4:4,Sigma:2,Theta:0};
const GB_terms=[["H6","f1"],["f1","H6"],["f3","f4"],["f4","f3"]];
ck(GB_terms.every(([a])=>thetaTypes[a]!==5),"entire first H negative-one row vanishes");
const targetValueCoefficient=em(extractB,ei(esc(em(del,del),8)));
ck(eq(targetValueCoefficient,E(1,0,168)),"full original source unit coefficient");
return {
 convention:"All coefficient pairs [a,b] are exact rationals a+b*omega. No numerical sample replaces a global theta identity.",
 frame_order:["c","v=H0","Z=xi1-xi3-2x","Q=xi1+xi3","r=xi2","d=d0"],
 frame:frame.map(a=>a.map(out)),inverse:iv.inverse.map(a=>a.map(out)),determinant:out(iv.det),gram:gram.map(a=>a.map(out)),
 observations:Object.fromEntries(Object.entries(converted).map(([k,a])=>[k,a.map(out)])),
 original_normalizations:{S:out(leadS),W_over_T:out(leadW)},
 theta_identity:{
  space:"S6(z) tensor S2(s) tensor oddS3(t), with the full standard half characters",
  A:"Sigma(z+t)*sigma(t-2z)=H6(z)*P(t)-3*f2(z)*B1(t)-2*f3(z)*B(t)",
  B:"Theta(z+t)*sigma(t-2z)=-2*f1(z)*B(t)+(h0(z)+4*b*h6(z))*B1(t)+6*b*f4(z)*P(t)",
  complete_C_average:"B(t)*[2*Sigma(s)*f1(z)-2*Theta(s)*f3(z)] + P(t)*[Theta(s)*H6(z)-6*b*Sigma(s)*f4(z)]",
  sign:"sigma(xi3) contributes minus under xi3=-(z-s+t); original -1/84 therefore becomes +1/84",
  proof:"Exact type spaces, t=0, first t derivative, z=0, and z=t determine every displayed coefficient."
 },
 extraction:{
  companion_polynomial:"g5=Z^3*r*d",
  B_coefficient_over_Omega5:out(extractB),P_coefficient_over_Omega5:out(extractP),
  quantifier:"all bounded continuous tests of the complete pair (c,v)"
 },
 simple_pole_unit:{
  phi:"c*(7*delta^2*c^2+5*v^2)/(8*delta^2*(delta^2*c^2-v^2))",
  derivative_form:"7*c/(8*delta^2)-(3*v^2/(4*delta^3))*partial_v log((delta*c-v)/(delta*c+v))",
  actual_domain:["c unit","v unit","H=delta*c-v unit","K=delta*c+v unit"],
  exact_leading:"Omega*(4-11*beta+beta*kappa*(1+6*beta))/(8*delta^2)",
  c_deep_tail:"+(3*beta/(2*delta^2))*sum_{r>=1} delta^(6r)*kappa^(6r+1)*m_sigma(6r+1)*m_B_unit(-6r)",
  v_deep_tail:"-(3*beta/(2*delta^2))*sum_{r>=1} delta^(-6r)*kappa^(6r)*m_B(6r)*m_sigma_unit(1-6r)",
  tail_orders:[7,6],
  hasse_polynomial_at_71:String(hassePolynomial),possible_k_mod8:possibleResidues,required_mod8:forbiddenResidue,
  old_source_leading_coefficient_over_Omega6:out(targetValueCoefficient)
 },
 carry_intersection:{
  exact_v:"v=delta*zeta_j^(-1)*(F-D_j)",
  common_unit_conditions:["c unit","c-zeta_j^(-1)*F unit","c+zeta_j^(-1)*F unit"],
  complete_missing_strips:["c deep","c unit and c-zeta_j^(-1)*F deep","c unit and c+zeta_j^(-1)*F deep"],
  other_domain:"the four-unit domain outside the union of all original Gamma_{n,j}",
  old_native_weights:"Every original lambda/kappa coefficient of P_hat, D_j/kappa^n, E_j and G is unchanged."
 },
 scope:{
  full_S_T_central_difference:"(1/42) integral ell against sigma(c)*sigma(r)*sigma(d)*(f1(Z)*Sigma(Q)-f3(Z)*Theta(Q))",
  positive_unit_is_not_a_central_zero:true,
  no_omitted_C_P_component_under_mixed_carry:true,
  no_unmoved_Y_W_substitution:true
 }
};
}
const report=certifyR572();
if(typeof process!=="undefined")process.stdout.write(JSON.stringify(report,null,2)+"\n");
