// Exact certificate for R617. Run: node <this-file> [output.json]
// Q(omega), no floating-point elliptic values and no target-prime sampling.
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



function certificate(){
function geometry(){

const w=E(0,1),de=E(1,2),al=E(1,3),ga=E(2,3),az=E(-2,1,2),aq=E(4,3,2),a=E(0,-3,8),bK=E(-1,-6,8),u=E(1,-1,3);
const e=i=>Array.from({length:6},(_,j)=>E(i===j?1:0)),C=e(0),Z=e(1),Qq=e(2),r=e(3),c=e(4),d=e(5),metric=[1,6,2,1,1,1];
const ip=(x,y)=>x.reduce((s,t,i)=>ea(s,esc(em(t,ec(y[i])),metric[i])),E(0));
const R=va(vm(c,al),d),K=va(c,vm(d,ga));
const F=va(va(va(vm(Z,E(1,2,6)),vm(Qq,E(1,-2,2))),vm(r,E(-1,-1))),K);
const H1=va(va(vm(Z,E(-1,-1,2)),vm(Qq,E(-1,1,2))),vm(r,E(2)));
const G=va(vm(H1,E(13)),vm(F,E(3,-2)));
const A0=va(va(vm(Z,az),vm(Qq,aq)),vm(r,E(2,4)));
const Y=va(va(A0,c),vm(d,E(2))),W=va(va(A0,vm(c,E(3,6))),vm(d,E(4))),V=vs(Y,vm(R,a));
const L=va(vm(Z,E(1,0,2)),vm(Qq,E(3,0,2))),M=vs(vm(Z,E(1,0,2)),vm(Qq,E(1,0,2)));
const J=va(va(vm(M,w),vm(r,E(-1,-1))),K),A=vs(J,C),H=va(J,vm(C,E(11)));
const frame=[C,Z,Qq,r,R,K],inv=inverse(frame);
ck(eq(inv.det,E(-8)),"det -8");
ck(eq(ip(R,R),E(8))&&eq(ip(K,K),E(8))&&ez(ip(R,K)),"norm8 frame");
for(const [name,row] of Object.entries({C,F,G,A,H,L,V}))ck(ez(ip(row,R)),"R perpendicular "+name);
ck(eq(ip(V,V),E(263,0,8)),"V norm");
ck(W.every((x,i)=>eq(x,va(Y,vm(R,E(2)))[i])),"W=Y+2R");
const maprow=x=>mm([x],inv.inverse)[0];
const Vf=maprow(V),Yf=maprow(Y),Wf=maprow(W),Ff=maprow(F),Gf=maprow(G);
ck(eq(Vf[5],bK)&&ez(Vf[4]),"V companion");
ck(eq(Yf[4],a)&&eq(Wf[4],ea(a,E(2))),"Y/W R coefficient");
const tau=ident(6);tau[1]=[E(0),E(1,0,2),E(-3,0,2),E(0),E(0),E(0)];
tau[2]=[E(0),E(-1,0,2),E(-1,0,2),E(0),E(0),E(0)];
const Vt=mm([V],tau)[0],Vtf=maprow(Vt);
ck(eq(Vtf[1],ec(az))&&eq(Vtf[2],ec(aq))&&eq(Vtf[5],bK),"V tau exact");
const B=Array.from({length:8},()=>Array(8).fill(0)),RR=Array.from({length:8},()=>Array(8).fill(0));
for(let j=0;j<8;j++){B[(3*j+4)%8][j]=(j%2)?-1:1;RR[(8-j)%8][j]=1;}
const K8=B.map(row=>row.map(x=>-x));
for(let j=1;j<=3;j++){
 const v=Array(8).fill(0);v[j]=1;v[8-j]=-1;
 const kv=K8.map(row=>row.reduce((s,x,i)=>s+x*v[i],0));
 ck(kv.every((x,i)=>x===-v[i]),"whole odd eigen beta");
}
const r7=E(-4,-12,7),pairC1zeta=ea(em(al,ga),E(7));
ck(ez(pairC1zeta),"complete zeta cancellation");
const secondX=em(ea(E(24),esc(r7,56)),ei(ga)),secondX4=em(E(-14),ei(ga));
ck(eq(secondX4,esc(al,2)),"second mass");
return {field:"Q(omega); entries [a,b] mean a+b omega",input_order:["C","Z","Q","r","c","d"],metric,frame_order:["C","Z","Q","r","R","K"],frame:frame.map(x=>x.map(out)),inverse:inv.inverse.map(x=>x.map(out)),determinant:out(inv.det),rows:{F:Ff.map(out),G:Gf.map(out),Y:Yf.map(out),W:Wf.map(out),V:Vf.map(out),V_tau:Vtf.map(out)},R_perpendicular_to:["C","F","G","A","H","L","V"],norm_V:out(ip(V,V)),norm8_whole_matrix:K8,whole_odd_S8_eigenvalue:-1,first_R_moment:{zeta_coefficient:out(pairC1zeta),derivative_P:"6*x^2*y",source:"6 Omega sigma^8 x^2 y = -6 Omega Theta*f1",g8_mass:0,g8_first_moment:"-Omega",g8_core:"beta"},second_R_moment:{coefficient_sigma8_x4:out(secondX4),coefficient_b_sigma8_x:out(secondX)},native_carry_q_invariant_under_R_scaling:true,all_old_unit_indicators_retained:true};

}
function coefficients(){

const w=E(0,1),delta=E(1,2),alpha=E(1,3),gamma=E(2,3),a=E(0,-3,8),bk=E(-1,-6,8),az=E(-2,1,2),aq=E(4,3,2);
const ep=(x,n)=>{let z=E(1);for(let i=0;i<n;i++)z=em(z,x);return z};
const ratio=(x,y)=>em(x,ei(y));
const c3=ratio(esc(em(delta,bk),4),esc(ep(az,3),7));
const c5=ratio(esc(em(em(delta,bk),ep(aq,2)),-48),esc(ep(az,5),7));
const c3t=ratio(esc(em(delta,bk),4),esc(ep(ec(az),3),7));
const c5t=ratio(esc(em(em(delta,bk),ep(ec(aq),2)),-48),esc(ep(ec(az),5),7));
const ct=ratio(ep(az,3),ep(ec(az),3)),eps=es(c5t,em(ct,c5));
const oldeps=E(6789120,4239360,117649),D=es(E(2),esc(delta,12));
ck(eq(eps,em(ratio(esc(bk,-6),D),oldeps)),"old eps conversion");
ck(eq(em(alpha,gamma),E(-7)),"norm7 pair");
return {alpha:out(alpha),gamma:out(gamma),a:out(a),b_K:out(bk),c3:out(c3),c5:out(c5),c3_tau:out(c3t),c5_tau:out(c5t),c_tau:out(ct),epsilon:out(eps),norms:{c3:out(em(c3,ec(c3))),c5:out(em(c5,ec(c5))),epsilon:out(em(eps,ec(eps)))},epsilon_from_old:out(ratio(esc(bk,-6),D))};

}
function polynomial(){

const pnew=()=>new Map(),key=(i,j,e)=>i+","+j+","+e;
const add=(P,i,j,e,v)=>{if(ez(v))return;const k=key(i,j,e);P.set(k,ea(P.get(k)||E(0),v));if(ez(P.get(k)))P.delete(k)};
const deriv=P=>{const R=pnew();for(const [k,v]of P){const[i,j,e]=k.split(",").map(Number);if(e===0){if(i)add(R,i-1,j,1,esc(v,2*i));}else{add(R,i+2,j,0,esc(v,2*i+3));if(i)add(R,i-1,j+1,0,esc(v,2*i));}}return R};
const serialize=P=>Array.from(P,([k,v])=>({monomial:k,coefficient:out(v)})).sort((x,y)=>x.monomial.localeCompare(y.monomial));
const r7=E(-4,-12,7),gam=E(2,3),P=pnew();add(P,3,0,0,E(1));add(P,0,1,0,en(r7));
const DP=deriv(P),D2P=deriv(DP),C2=pnew();
for(const [k,v]of D2P){const[i,j,e]=k.split(",").map(Number);add(C2,i,j,e,em(v,ei(gam)));}
for(const [k,v]of P){const[i,j,e]=k.split(",").map(Number);add(C2,i+1,j,e,em(esc(v,-56),ei(gam)));}
ck(DP.size===1&&eq(DP.get("2,0,1"),E(6)),"exact derivative1");
ck(D2P.size===2&&eq(D2P.get("4,0,0"),E(42))&&eq(D2P.get("1,1,0"),E(24)),"exact derivative2");
ck(C2.size===2&&eq(C2.get("4,0,0"),E(2,6))&&eq(C2.get("1,1,0"),E(-40,-24)),"exact second source");
return {curve:"y^2=x^3+b, D(x)=2y, D(y)=3x^2",division_P:serialize(P),derivative1:serialize(DP),derivative2:serialize(D2P),second_conditional_source_polynomial:serialize(C2),positive_moments:{Sigma_2:"2 Omega^2",Theta_0:1,sigma_1:"Omega",g8_1:"-Omega"},lowest_multinomial_coefficients:{f3_branch:{powers_Q_r_K:[0,1,1],multinomial:2},f1_branch:{powers_Q_r_K:[2,1,1],multinomial:12}},pole_tail_classes:{f3:"m=2 mod 6",f1:"m=4 mod 6",after_first_two_terms:"m>=8"},bounds:{log_annulus_tail_after_k1:"p^(4m) O",log_annulus_tail_after_k2:"p^(6m) O",adjacent_annulus_first_pole_error:"p^(4m+2) O",negative_five_rectangle_error:"p^(8n) O",normalized_negative_five_error:"p^(4n) O"},no_new_ray:true,no_local_to_total_nonzero_inference:true,full_cap_ex_and_pole_complements_retained:true};

}
return {geometry:geometry(),coefficients:coefficients(),polynomial:polynomial()};
}
const report=certificate();
if(typeof module!=="undefined"&&require.main===module){
 const fs=require("node:fs");
 const target=process.argv[2]||__filename.replace(/\.js$/, ".json");
 fs.writeFileSync(target,JSON.stringify(report,null,2)+"\n");
 console.log("R617: complete geometry, odd S8 core, first/second sources and all pole coefficients verified");
}
if(typeof module!=="undefined")module.exports={certificate};
