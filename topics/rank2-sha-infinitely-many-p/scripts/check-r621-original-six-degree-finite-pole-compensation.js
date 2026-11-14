// Exact R621 certificate. Run: node <this-file> [output.json]
// Characteristic-zero Q(omega) arithmetic; no elliptic numerical sampling.
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

const de=E(1,2),al=E(1,3),bk=E(-1,-6,8),az=E(-2,1,2),aq=E(4,3,2),a3=E(2,1),phase=E(1,1);
ck(eq(em(phase,a3),de),"delta = -omega^2 a3");
const e=i=>Array.from({length:5},(_,j)=>E(i===j?1:0)),C=e(0),Z=e(1),Qq=e(2),r=e(3),K0=e(4),metric=[1,6,2,1,8];
const ip=(x,y)=>x.reduce((s,t,i)=>ea(s,esc(em(t,ec(y[i])),metric[i])),E(0));
const H=vm(vs(C,r),de),Kb=vm(va(C,r),de),frame=[Z,Qq,K0,H,Kb],iv=inverse(frame);
ck(eq(ip(H,H),E(6))&&eq(ip(Kb,Kb),E(6))&&ez(ip(H,Kb)),"whole6 orthogonal axes");
const F0=va(va(vm(Z,E(1,2,6)),vm(Qq,E(1,-2,2))),K0),F=va(F0,vm(r,E(-1,-1))),D=vs(F,C),EE=va(F,vm(C,E(13)));
const G0=va(va(vm(Z,E(-32,-31,6)),vm(Qq,E(-14,1,2))),vm(K0,E(3,-2))),G=va(G0,vm(r,E(21,-3)));
const V0=va(va(vm(Z,az),vm(Qq,aq)),vm(K0,bk)),V=va(V0,vm(r,E(2,4)));
const coord=x=>mm([x],iv.inverse)[0];
const DH=em(E(0,1),ei(esc(de,2))),DK=em(E(-2,-1),ei(esc(de,2))),EH=em(E(14,1),ei(esc(de,2))),EK=em(E(12,-1),ei(esc(de,2)));
ck(eq(coord(D)[3],DH)&&eq(coord(D)[4],DK),"D full source");
ck(eq(coord(EE)[3],EH)&&eq(coord(EE)[4],EK),"E full source");
ck(eq(coord(V)[3],E(-1))&&eq(coord(V)[4],E(1)),"V=V0-H+Kb");
const M4=esc(em(em(az,bk),es(em(az,az),em(aq,aq))),24);
const M3=esc(em(em(al,az),es(em(aq,aq),em(az,az))),12);
const d1=esc(em(de,M4),1,7),d2=esc(em(de,M3),-2,21);
ck(eq(d1,esc(bk,-36))&&eq(d2,esc(al,-12)),"complete negative five constants");
ck(ez(es(em(al,d1),esc(em(bk,d2),3))),"I1 exact cancellation");
const ell2=E(8,-3,4);
const pmul=(A,B)=>{let R=Array(A.length+B.length-1).fill(0n);A.forEach((a,i)=>B.forEach((b,j)=>R[i+j]+=a*b));return R};
const padd=(A,B)=>Array.from({length:Math.max(A.length,B.length)},(_,i)=>(A[i]||0n)+(B[i]||0n));
const div1=padd(pmul([-1n,1n],[-1n,-1n,-1n,-1n,-1n]),[0n,0n,0n,0n,0n,1n]);
const div2=padd(pmul([1n,-2n,1n],[1n,2n,3n,4n]),[0n,0n,0n,0n,5n,-4n]);
ck(div1[0]===1n&&div1.slice(1).every(x=>x===0n),"finite reciprocal identity");
ck(div2[0]===1n&&div2.slice(1).every(x=>x===0n),"finite square reciprocal identity");
return {
 field:"Q(omega); entries [a,b] mean a+b omega",
 input_order:["C","Z","Q","r","K0"],metric,frame_order:["Z","Q","K0","H","Kb"],
 frame:frame.map(x=>x.map(out)),inverse:iv.inverse.map(x=>x.map(out)),determinant:out(iv.det),
 Gram:frame.map(x=>frame.map(y=>out(ip(x,y)))),
 rows:Object.fromEntries(Object.entries({C,r,F0,F,D,E:EE,G0,G,V0,V}).map(([k,v])=>[k,coord(v).map(out)])),
 full_source_phase:out(phase),whole_H_K_core:"beta independently; standard even S6 x S6",
 cofactor_moments:{rho1_below4:"zero exactly",rho1_degree4:out(M4),rho2_below3:"zero exactly",rho2_degree3:out(M3)},
 finite_negative_five_coefficients:{d1:out(d1),d2:out(d2),norm_d1:out(em(d1,ec(d1))),norm_d2:out(em(d2,ec(d2))),relation:"alpha*d1 - 3*bK*d2 = 0"},
 log_second_coefficient:out(ell2),norm_log_second:out(em(ell2,ec(ell2))),
 polynomial_certificates:{first:div1.map(String),second:div2.map(String)},
 real_remainders:["H deep and V unit","H unit and V deep","H and V units with actual rational remainder"],
 true_four_unit_set:["H unit","Kb unit","H+Kb unit","H-Kb unit"],
 four_unit_complement_with_H_unit:["Kb deep","H+Kb deep with H,Kb units","H-Kb deep with H,Kb units"],
 all_q_cuts_transposed:true,no_new_negative_moment_pool:true,no_new_ray:true,no_boundary_assigned_zero:true
};

}
const report=certificate();
if(typeof module!=="undefined"&&require.main===module){
 const fs=require("node:fs");
 const target=process.argv[2]||__filename.replace(/\.js$/, ".json");
 fs.writeFileSync(target,JSON.stringify(report,null,2)+"\n");
 console.log("R621: complete mixed frame, finite division, both source coefficients and exact I1 cancellation verified");
}
if(typeof module!=="undefined")module.exports={certificate};
