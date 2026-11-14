"use strict";
// Exact certificate for R563. No dependencies; no floating-point sampling.
function certifyR563(){
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


const w=E(0,1),w2=em(w,w),del=E(1,2),unit=i=>Array.from({length:6},(_,j)=>E(i===j?1:0));
const c=unit(4),d0=unit(5),H0=[1,0,-1,1,0,0].map(v=>E(v)),C=vm(H0,ei(del));
const D4=[E(1),w2,E(0,-2),E(0),E(0),E(0)],M=va(c,vm(d0,E(2,3))),F=va(va(D4,C),M),D=vs(F,c),R=vm(D,esc(del,2));
const H1=[E(-1),E(2),w,E(1,1),E(0),E(0)],G=va(vm(H1,E(13)),vm(F,E(3,-2)));
const A=[del,esc(del,2),E(3,1),E(2,-1),E(0),E(0)],Y=va(va(A,c),vm(d0,E(2))),W=va(va(A,vm(c,esc(del,3))),vm(d0,E(4)));
const Hp=vm(vs(c,C),del),Kp=vm(va(c,C),del);
const proj=r=>vs(vs(r,vm(c,he(r,c))),vm(D,esc(he(r,D),1,12)));
const Y0=proj(Y),W0=proj(W),G0=proj(G),T=[Y0,W0,G0].map(r=>vm(r,esc(del,12)));
const dstar=va(d0,vm(D,E(1,3,12)));
ck(ez(he(dstar,c))&&ez(he(dstar,C))&&ez(he(dstar,D)),"dstar is retained companion");
const frame=[vm(Hp,E(2)),vm(Kp,E(2)),R,...T.map(r=>vm(r,E(2)))];
const det=inverse(frame).det;
const olddet=E(8895744,25069824);
ck(eq(det,em(esc(del,64),olddet)),"full covered frame determinant");
for(const r of[Hp,Kp]){ck(eq(he(r,r),E(6)),"physical norm6");for(const s of[R,...T])ck(ez(he(r,s)),"all actual companions orthogonal");}
ck(ez(he(Hp,Kp)),"HK orthogonal");
const Hmat=ident(6),p2=[[E(-1,-1,2),E(-1,-2,2)],[E(2,1,2),E(-1,-1,2)]];
for(let i=0;i<2;i++)for(let j=0;j<2;j++)Hmat[i+4][j+4]=p2[i][j];
const hlead=em(w2,em(p2[0][0],p2[0][1]));
ck(eq(hlead,E(2,1,4)),"actual primitive even c^2 coefficient");
const allrows=[];
for(const r of[vm(Hp,E(2)),vm(Kp,E(2))]){
 const rh=mm([r],Hmat)[0];
 for(const q of[r,rh])ck(q.every(z=>z.every(a=>a[1]===1n)),"rho/eta integral even24");
 const parity=q=>q.filter(z=>z.some(a=>(a[0]%2n+2n)%2n)).length;
 ck(parity(r)%2===0&&parity(rh)%2===0,"standard even characteristic");
 allrows.push({rho:r.map(out),eta:rh.map(out),odd_rho:parity(r),odd_eta:parity(rh)});
}
const cmul=(x,y,n)=>{const m=t=>((t%n)+n)%n;return[m(x[0]*y[0]-x[1]*y[1]),m(x[0]*y[1]+x[1]*y[0]-x[1]*y[1])];};
const gp=[43,24],g2=cmul(gp,gp,48);
ck(g2[0]===25&&g2[1]===0&&(25*25-1)/24===26,"whole24 full center");
const AH=[[-1,0,0],[0,0,1],[0,1,0]].map(r=>r.map(x=>E(x))),
AK=[[-1,0,0],[0,0,-1],[0,-1,0]].map(r=>r.map(x=>E(x))),
BB=[[1,0,0],[0,-1,0],[0,0,-1]].map(r=>r.map(x=>E(x))),
RC=[[-1,0,0],[0,1,0],[0,0,-1]].map(r=>r.map(x=>E(x)));
const meq=(A,B)=>A.every((r,i)=>r.every((x,j)=>eq(x,B[i][j])));
ck(meq(mm(AH,AH),ident(3))&&meq(mm(AK,AK),ident(3)),"whole24 square on states");
ck(meq(mm(AH,AK),BB)&&meq(mm(AK,AH),BB),"full simultaneous source relation");
ck(meq(mm(mm(RC,AH),RC),AK),"actual reflection exchanges axes");
ck(eq(BB[2][2],E(-1))&&eq(en(RC[2][2]),E(1)),"D square cannot extend -Rc to new state");
for(const B of[AH,AK,BB])ck(meq(mm(BB,B),mm(B,BB)),"D square commutes both actual cores");
const Rc=ident(6);Rc[4][4]=E(-1);
ck(mm([Hp],Rc)[0].every((v,i)=>eq(v,en(Kp[i])))&&mm([Kp],Rc)[0].every((v,i)=>eq(v,en(Hp[i]))),"physical Rc=-swap");
const cHK=vm(va(Hp,Kp),ei(esc(del,2))),CHK=vm(vs(Kp,Hp),ei(esc(del,2)));
ck(cHK.every((v,i)=>eq(v,c[i]))&&CHK.every((v,i)=>eq(v,C[i])),"physical c C inverse");
const Dzero=vs(F,C),Ezero=va(F,vm(C,E(13)));
ck(va(D,vm(Hp,ei(del))).every((v,i)=>eq(v,Dzero[i])),"actual single carry");
ck(va(D,vm(va(vm(Hp,E(-6)),vm(Kp,E(7))),ei(del))).every((v,i)=>eq(v,Ezero[i])),"full E row");
const yt=va(va(Y0,vm(va(Hp,Kp),ei(esc(del,2)))),vm(D,E(-1,0,12)));
const wt=va(va(W0,vm(va(Hp,Kp),E(3,0,2))),vm(D,esc(del,-1,4)));
ck(yt.every((v,i)=>eq(v,Y[i]))&&wt.every((v,i)=>eq(v,W[i])),"native Y W retained");
const gt=va(va(G0,vm(va(Hp,Kp),em(E(3,-2),ei(esc(del,2))))),vm(D,E(-3,2,12)));
ck(gt.every((v,i)=>eq(v,G[i])),"native G retained");
return{
normalization:{lambda:"-1/barpi",beta:"-lambda",kappa:"p lambda^2",external_HK:"lambda",external_D_square:"lambda^2"},
physical:{H:Hp.map(out),K:Kp.map(out),D12:D.map(out),R144:R.map(out),dstar:dstar.map(out)},
frame:{rows:frame.map(r=>r.map(out)),det:out(det),norm_factors:{"2":28,"3":12,"13":3,"19":1}},
half_character:allrows,
whole24:{g:gp,square:g2,central_exponent:26,anchor:"Theta(2 delta z): normalized eigen -1; hence whole K24^2=I"},
states:["mu0=P_C rho0","muplus=P_C h","muminus=K_H muplus"],
primitive_example:{rho:"[t^3 s c d] = 1/84",h:"[t^3 s c^2]=(2+omega)/336",K_H:"integral involution preserves primitivity"},
matrices:{A_H:AH.map(r=>r.map(out)),A_K:AK.map(r=>r.map(out)),B_Dsquare:BB.map(r=>r.map(out)),R_c:RC.map(r=>r.map(out))},
full_joint_relation:"A_H A_K=B_Dsquare, but B_Dsquare != -R_c on muminus",
continuous_unit_inverse:"(I-lambda A)^(-1) f|axis0 + sum_r>=0 lambda^r A^r (f o P_axis,kappa^r-f|axis0)",
inverse_constant:"(I+lambda A)/(1-lambda^2); even trace and Hasse make 1+-lambda units",
native_Cunit:{cross_term:"S_H S_K f=0",exact_inverse:"U_H U_K f=U_H f+U_K f-f"},
actual_partition:{Dunit:"U_K f",Ddeep:"U_H f",H_shallow:"v(D)=j<n: lambda^j A_H^j f o P_H,kappa^j",H_tail:"D deep n: all r>=n retained, including constant log mass",K_tail:"D+H/delta deep n unchanged; all r retain Dunit"},
mixed_rows:{C:"(t K-s H)/(2 delta)",Dzero:"e D+s H/delta",Ezero:"e D+(-6sH+7tK)/delta",Y:"Y0+(sH+tK)/(2delta)-eD/12",W:"W0+3(sH+tK)/2-e delta D/4",G:"G0+(3-2omega)(sH+tK)/(2delta)-(3-2omega)eD/12"},
depth_transport:"T_r=P_H,kappa^r P_K,kappa^r P_D,kappa^(-2r) maps D deep2r to H,K deepr; all native cuts transpose"
};

}
if(typeof module!=="undefined")module.exports={certifyR563};
if(typeof require!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(certifyR563(),null,2)+"\n");
