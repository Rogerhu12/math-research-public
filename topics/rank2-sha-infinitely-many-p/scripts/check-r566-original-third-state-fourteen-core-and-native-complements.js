"use strict";
function certifyR566(){
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

const A12=D,D14=vs(F,C),Q1008=vs(R,vm(Hp,E(12)));
const Hbar=vs(Hp,vm(D14,esc(del,1,7)));
const X=vs(c,vm(D14,E(1,0,14))),Z=va(d0,vm(D14,E(1,3,14))),E0=va(F,vm(C,E(13)));
const frame14=[D14,vm(Kp,E(2)),Q1008,...T.map(r=>vm(r,E(2)))];
const det14=inverse(frame14).det;
ck(eq(det14,em(det,em(E(7),ei(esc(del,2))))),"exact new full determinant");
ck(eq(he(D14,D14),E(14))&&eq(he(Q1008,Q1008),E(1008)),"true degree14/1008");
ck(eq(he(Hbar,Hbar),E(36,0,7)),"orthogonal Hbar norm");
ck(vs(Q1008,vm(Hbar,E(-14))).every(ez),"Q1008=-14 Hbar");
ck(vs(Hbar,vm(vs(X,vm(E0,E(1,0,14))),del)).every(ez),"actual pi5 hyperplane");
for(const r of[Y,W,E0,G,Kp,Hbar])ck(ez(he(D14,r)),"D14 fixes complete observations");
for(const r of T){ck(ez(he(D14,r))&&ez(he(Kp,r))&&ez(he(Q1008,r)),"three complete orthogonal first blocks");}
ck(ez(he(Kp,Q1008))&&ez(he(D14,Q1008)),"full three-axis orthogonality");
ck(eq(esc(he(Hp,D14),1,14),esc(del,1,7))&&eq(esc(he(A12,D14),1,14),E(6,0,7)),"true shrinking coefficients");
ck(eq(esc(he(C,D14),1,14),E(-1,0,14)),"C units become E units");
ck(vs(E0,vm(vs(Kp,Hbar),em(E(7),ei(del)))).every(ez),"E=7(K-Hbar)/delta");
const HH=ident(6),pair=[[E(-1,-1,2),E(-1,-2,2)],[E(2,1,2),E(-1,-1,2)]];
for(let i=0;i<2;i++)for(let j=0;j<2;j++)HH[i+4][j+4]=pair[i][j];
const SC=ident(6);for(let i=0;i<6;i++)for(let j=0;j<6;j++)SC[i][j]=ea(SC[i][j],em(es(w,E(1)),em(ec(C[i]),C[j])));
const par=q=>q.filter(x=>x.some(a=>(a[0]%2n+2n)%2n)).length;
const checks=[];let power=ident(6);
for(let j=0;j<3;j++){
 const rows=mm(frame14,power),after=mm(rows,HH);
 for(const arr of[rows,after])for(const row of arr)ck(row.every(x=>x.every(a=>a[1]===1n)),"all PC/eta frame rows integral");
 for(let k=0;k<3;k++)ck(par(rows[k])%2===0&&par(after[k])%2===0,"standard first three even characteristics");
 checks.push({j,first_three:rows.slice(0,3).map(r=>r.map(out)),eta_first_three:after.slice(0,3).map(r=>r.map(out)),parity:rows.slice(0,3).map(par),eta_parity:after.slice(0,3).map(par)});
 power=mm(power,SC);
}
const u=va(vm(c,esc(w,1,2)),vm(d0,esc(es(E(1),w),1,2)));
const up=vs(u,vm(D14,E(-1,-1,7)));
ck(vs(up,vm(vs(X,vm(Z,E(2,1))),esc(w,1,2))).every(ez),"native positive strip");
return{
frame:{rows:frame14.map(r=>r.map(out)),det:out(det14),norm_factors:{"2":26,"3":11,"7":2,"13":3,"19":1}},
D14:D14.map(out),Hbar:Hbar.map(out),Q1008:Q1008.map(out),norm_Hbar:"36/7",
complete_three_conjugates:checks,
whole_source:{space:"S14(D14) tensor S24(2K) tensor S1008(Q) tensor full three companions",minus:"mu-= -K_K mu+, so D14 remains whole S14 and has scalar beta",core:"-I on all three normalized sources"},
geometric:{D14:"D12+H/delta",Hbar:"H-delta D14/7=delta(X-E/14)",H_after:"Hbar+delta kappa^n D14/7",D12_after:"-Hbar/delta+6 kappa^n D14/7",C_after:"E/14-kappa^n D14/14",E:"7(K-Hbar)/delta"},
native_unit_complement:{K_side:"beta^n times original pi5 row restricted to Hbar unit",H_side:"beta^n times original pi5 row restricted to Hbar deep",new_source:"mu- cancels by the complete K-unit inverse, not by factorizing its gluing",original_cut:"14X-E unit/deep, with Eunit and both original strips retained"},
normalization:"f_n o P_D14,kappa^n=f_flat exactly for all n>=1; all E/G/Y/W and both log masses preserved"
};

}
if(typeof module!=="undefined")module.exports={certifyR566};
if(typeof require!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(certifyR566(),null,2)+"\n");
