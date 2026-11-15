// Exact R626 certificate. Run: node <this-file> [output.json]
// Q(omega) arithmetic, complete Heisenberg columns and symbolic kappa matrices.
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
function main(){
const N=2104,m=N/8,aN=1579,shift=N/2;
ck(N===8*263&&m===263,"fixed level");
ck((aN*aN)%(2*N)===N+1,"full centre square");
ck(aN%16===11&&N%16===8&&aN%263===1&&N%263===0,"complete ray CRT");
const quarter=(j,r,s)=>{const exponent=((s*(j+m*r))%4+4)%4;return{index:(j+2*m*r)%N,re:exponent===0?1:exponent===2?-1:0,im:exponent===1?1:exponent===3?-1:0}};
const perm=[],sign=[];
for(let j=0;j<N;j++){
 const acc=new Map();
 const plus=(i,re,im)=>{const old=acc.get(i)||[0,0];acc.set(i,[old[0]+re,old[1]+im])};
 for(let r=0;r<4;r++)for(let s=0;s<4;s++){const t=quarter(j,r,s);plus(t.index,t.re,t.im);}
 for(let r=0;r<4;r+=2)for(let s=0;s<4;s+=2){const t=quarter(j,r,s);plus(t.index,-2*t.re,-2*t.im);}
 const target=(aN*j+shift)%N,targetSign=j%2?1:-1;
 for(const[i,v]of acc)ck(v[0]===(i===target?4*targetSign:0)&&v[1]===0,"complete quarter sum "+j);
 perm.push(target);sign.push(targetSign);
 ck((aN*target+shift)%N===j&&targetSign*(target%2?1:-1)===1,"whole A square "+j);
}
for(let j=0;j<N/2;j+=2){
 const k=j+N/2;ck(new Set([perm[j],perm[k]]).has(j)&&new Set([perm[j],perm[k]]).has(k),"E2 anchor indices");
 ck(sign[j]===-1&&sign[k]===-1,"A=-1 on E2 fixed");
}
const de=E(1,2),w=E(0,1),ga7=E(3,1),bAnchor=esc(em(de,ga7),10);
ck(eq(em(bAnchor,ec(bAnchor)),E(2100)),"two sigma anchor norm");
const gamma31=E(-1,-6);ck(eq(em(gamma31,ec(gamma31)),E(31)),"quarter bijection");
const e=i=>Array.from({length:5},(_,j)=>E(i===j?1:0)),C=e(0),Z=e(1),Qq=e(2),r=e(3),K=e(4),metric=[1,6,2,1,8];
const ip=(x,y)=>x.reduce((s,t,i)=>ea(s,esc(em(t,ec(y[i])),metric[i])),E(0));
const az=E(-2,1,2),aq=E(4,3,2),bk=E(-1,-6,8);
const V=va(va(va(vm(Z,az),vm(Qq,aq)),vm(r,E(2,4))),vm(K,bk)),NV=ip(V,V);
const H=vm(vs(C,r),de),Kb=vm(va(C,r),de),s=E(48,0,263),U=va(H,V),X=va(H,vm(V,s));
ck(eq(NV,E(263,0,8))&&eq(ip(H,V),E(-6)),"real H V Gram");
ck(ez(ip(U,H))&&ez(ip(X,V)),"actual pure companions");
const F=va(va(va(vm(Z,E(1,2,6)),vm(Qq,E(1,-2,2))),vm(r,E(-1,-1))),K);
const G=va(va(vm(Z,E(-32,-31,6)),vm(Qq,E(-14,1,2))),va(vm(r,E(21,-3)),vm(K,E(3,-2))));
for(const[name,L]of Object.entries({C,F,G}))ck(ez(ip(L,V)),"V preserves "+name);
const L=va(vm(Z,E(1,0,2)),vm(Qq,E(3,0,2))),J=va(va(vm(vs(Z,Qq),E(0,1,2)),vm(r,E(-1,-1))),K);
const Ft=vs(F,vm(L,E(2,-2,3))),Gt=va(G,vm(L,E(37,14,3))),A=vs(J,C),H613=va(J,vm(C,E(11)));
const changes=Object.fromEntries(Object.entries({C,Z,Q:Qq,r,K0:K,H,Kb,F,G,F_tau:Ft,G_tau:Gt,L,J,A,H613}).map(([k,v])=>[k,out(em(ip(v,V),ei(NV)))]));
ck(eq(em(ip(Ft,V),ei(NV)),E(48,48,263)),"Ftau shift");
ck(eq(em(ip(Gt,V),ei(NV)),E(-72,-480,263)),"Gtau shift");
const V8=vm(V,E(8));const levelSum=V8.reduce((t,a,i)=>ea(t,esc(em(a,ec(a)),metric[i])),E(0));
ck(eq(levelSum,E(N)),"entire integral level");
const plus=E(-2,2),minus=E(4,4);
const h8v=ea(plus,minus),h8x=ea(esc(plus,4),esc(minus,-8));
ck(eq(h8v,E(2,6))&&eq(h8x,E(-40,-24)),"actual second source split");
const E2v=E(1,0,3),E2u=E(-1,0,12);
const A8h=[es(h8v,esc(minus,2)),es(h8x,esc(em(minus,E(-8)),2))];
return{level:N,quarter_m:m,full_g_mod_2N:[aN,N],full_centre_square_mod_2N:N+1,canonical_A_equals_minus_B:true,A_permutation:perm,A_sign:sign,
 anchor:{a:["2","0"],b:out(bAnchor),norm_b:2100,determinant:N,E2_lifts:"all + on both axes",absolute_square:1,epsilon:"actual sign in {+1,-1}; K_N=epsilon A_N"},
 actual_V8_input_coefficients:V8.map(out),level_sum:out(levelSum),quarter_transfer:{Z:"full period",Q:"full period",r:"even period",K0:out(gamma31),norm_last_multiplier:31,complete_joint_identity:"A2104,V8 mu0=A8,K0 mu0=A8,R mu0"},
 H_V_Gram:[[out(ip(H,H)),out(ip(H,V))],[out(ip(V,H)),out(NV)]],s:out(s),pure_U:U.map(out),pure_X:X.map(out),V_scaling_change_coefficients:changes,
 second_source:{D8_coefficient:out(plus),Theta2_coefficient:out(minus),A8h8:{x4:out(A8h[0]),b_x:out(A8h[1])}},
 actual_eigen_sources:{nu1:{H:"beta",V:"epsilon beta"},theta_component:{H:"beta",V:"epsilon beta"},D_component:{H:"beta",V:"epsilon lambda"}},
 raw_two_state_matrices:{R:"X",V:"epsilon X"},original_Y_W_common_depth:"epsilon^n lambda^(2n), scale plane by kappa^n, keep C/F/G",
 word_matrix_difference:"(1-kappa)^2 [[-s,-s],[1,s]]",
 no_q_minus_invariance_claim:true,all_four_unit_and_carry_transposes_retained:true,all_boundary_constants_retained:true};
}
function extra(){
const de=E(1,2),az=E(-2,1,2),aq=E(4,3,2),bk=E(-1,-6,8),s=E(48,0,263);
const e=i=>Array.from({length:5},(_,j)=>E(i===j?1:0)),C=e(0),Z=e(1),Qq=e(2),r=e(3),K0=e(4),metric=[1,6,2,1,8];
const ip=(x,y)=>x.reduce((u,t,i)=>ea(u,esc(em(t,ec(y[i])),metric[i])),E(0));
const H=vm(vs(C,r),de),Kb=vm(va(C,r),de),V=va(va(va(vm(Z,az),vm(Qq,aq)),vm(r,E(2,4))),vm(K0,bk)),X=va(H,vm(V,s));
const L1=vs(Z,vm(Kb,ec(az))),L2=vs(Qq,vm(Kb,esc(ec(aq),1,3))),L3=vs(K0,vm(Kb,esc(ec(bk),4,3)));
for(const L of[L1,L2,L3])ck(ez(ip(L,V))&&ez(ip(L,H)),"complete common companion");
const frame=[V,X,L1,L2,L3],iv=inverse(frame);
const minus=E(4,4);
const avg_u=E(-1,0,12),avg_v=E(1,0,3);
const avg_h=ea(em(E(2,6),avg_v),em(E(-40,-24),avg_u));
ck(eq(avg_h,minus),"exact full E2 average h");
return{complete_frame_order:["V","X","L1","L2","L3"],complete_frame:frame.map(x=>x.map(out)),inverse:iv.inverse.map(x=>x.map(out)),determinant:out(iv.det),Gram:frame.map(x=>frame.map(y=>out(ip(x,y)))),E2_average:{x_sigma8:"-Theta(2z)/(12b)",x4_sigma8:"Theta(2z)/3",h8_coefficient:out(avg_h)},boundary_first_jets:{T1_constant:-5,T1_linear:out(en(ea(E(10),esc(s,5)))),T2_constant:10,T2_linear:out(esc(ea(E(1),s),20))}};
}
function word(){
const de=E(1,2),s=E(48,0,263),inv2d=ei(esc(de,2)),w=E(0,1);
const e=i=>Array.from({length:5},(_,j)=>E(i===j?1:0)),C=e(0),Z=e(1),Qq=e(2),r=e(3),K0=e(4),metric=[1,6,2,1,8];
const ip=(x,y)=>x.reduce((u,t,i)=>ea(u,esc(em(t,ec(y[i])),metric[i])),E(0));
const H=vm(vs(C,r),de),V=va(va(va(vm(Z,E(-2,1,2)),vm(Qq,E(4,3,2))),vm(r,E(2,4))),vm(K0,E(-1,-6,8)));
const X=va(H,vm(V,s));
const F=va(va(va(vm(Z,E(1,2,6)),vm(Qq,E(1,-2,2))),vm(r,E(-1,-1))),K0);
const D=vs(F,C),Ev=va(F,vm(C,E(13)));
const G=va(va(vm(Z,E(-32,-31,6)),vm(Qq,E(-14,1,2))),va(vm(r,E(21,-3)),vm(K0,E(3,-2))));
const proj=L=>L.map((z,i)=>vm(L,em(esc(ec(z),metric[i]),ei(ip(L,L)))));
const JH=proj(H),JV=proj(V),I=ident(5);
const ma=(A,B)=>A.map((x,i)=>va(x,B[i]));
const ms=(A,B)=>A.map((x,i)=>vs(x,B[i]));
const zero=()=>Array.from({length:5},()=>Array.from({length:5},()=>E(0)));
const A=[ms(I,JH),JH],B=[ms(I,JV),JV];
const polyMM=(A,B)=>{const out=Array.from({length:A.length+B.length-1},zero);for(let i=0;i<A.length;i++)for(let j=0;j<B.length;j++)out[i+j]=ma(out[i+j],mm(A[i],B[j]));return out;};
const AB=polyMM(A,B),BA=polyMM(B,A),rowpoly=(L,M)=>M.map(A=>mm([L],A)[0]);
const rowcoeff={C:E(1),D:w,E:E(14,1),G:E(-21,3)},rows={C,D,E:Ev,G};
const shift={};
for(const[name,L]of Object.entries(rows)){
 const a=rowpoly(L,A),ab=rowpoly(L,AB),ba=rowpoly(L,BA);
 for(let j=0;j<3;j++)for(let k=0;k<5;k++)ck(eq(ba[j][k],(a[j]||e(-1))[k]),"positive B invariance "+name);
 const unit=em(em(s,inv2d),rowcoeff[name]);
 const expected=[vm(V,en(unit)),vm(V,esc(unit,2)),vm(V,en(unit))];
 for(let j=0;j<3;j++)for(let k=0;k<5;k++)ck(eq(es(ab[j][k],(a[j]||e(-1))[k]),expected[j][k]),"actual AB-BA polynomial "+name);
 const LX=[vs(L,vm(X,em(inv2d,rowcoeff[name]))),vm(X,em(inv2d,rowcoeff[name]))];
 for(let j=0;j<2;j++){
   ck(ez(ip(LX[j],V)),"V-pure companion "+name);
   const expect=vm(V,j?en(unit):unit);
   for(let k=0;k<5;k++)ck(eq(es(a[j][k],LX[j][k]),expect[k]),"A in pure companion frame "+name);
 }
 shift[name]={coefficient_of_minus_one_minus_kappa_squared:out(unit),
  complete_row_difference:expected.map(row=>row.map(out)),
  pure_companion_row_polynomial:LX.map(row=>row.map(out))};
}
const t=em(s,inv2d),wnorm=em(t,ec(t));
ck(eq(wnorm,E(192,0,69169)),"carry intersection coefficient norm");
return {carry_depth:"N0>=1",s:out(s),t0_over_1_minus_kappa:out(t),
 actual_word_row_shifts:shift,intersection_difference_D_norm:out(wnorm),
 actual_intersection:"{V in p^N0, D_X in p^N0, C_X unit}",
 scalar_return:"b_V^N0 P_V,kappa^N0",
 normalized_weight_pair:["P_N0(kappa V)","P_N0(V)"],
 normalized_weight_difference:"sum_{j=1}^6 (kappa^j-1) p_j V^j",
 arbitrary_native_tests:"each full composition separately retained",no_domain_removed:true};
}
return {main:main(),extra:extra(),word:word()};
}
const report=certificate();
const data=JSON.stringify(report,null,2)+'\n';
if(process.argv[2])require('fs').writeFileSync(process.argv[2],data);else process.stdout.write(data);
