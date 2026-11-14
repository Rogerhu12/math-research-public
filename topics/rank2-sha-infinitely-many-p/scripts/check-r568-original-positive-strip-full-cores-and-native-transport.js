"use strict";
// Exact complete certificate for the positive native strip.
function certifyR568(){
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
const c=unit(4),d=unit(5),x=unit(3),H0=[1,0,-1,1,0,0].map(v=>E(v)),C=vm(H0,ei(del));
const D4=[E(1),w2,E(0,-2),E(0),E(0),E(0)],D=va(va(D4,c),vm(d,E(2,3))),F=va(D,C),E0=va(F,vm(C,E(13)));
const H1=[E(-1),E(2),w,E(1,1),E(0),E(0)],G=va(vm(H1,E(13)),vm(F,E(3,-2)));
const A=[del,esc(del,2),E(3,1),E(2,-1),E(0),E(0)],Y=va(va(A,c),vm(d,E(2))),W=va(va(A,vm(c,esc(del,3))),vm(d,E(4)));
const Wp=[E(4,4),E(2,4),E(4,4),E(0),E(4,2),E(4)];
const u=va(vm(c,esc(w,1,2)),vm(d,esc(es(E(1),w),1,2)));
const P=vs(u,vm(D,esc(w2,1,7))),Rp=vm(P,E(14));
const X=vs(c,vm(D,E(1,0,14))),Z=va(d,vm(D,E(1,3,14))),Zs=vs(Z,vm(P,E(8,3,10))),Sp=vm(Zs,E(20));
const Q10=vs(D,vm(u,esc(w,2)));
ck(eq(he(D,D),E(14))&&eq(he(P,P),E(5,0,7))&&eq(he(Zs,Zs),E(3,0,20)),"physical positive norms");
for(const[r,s]of[[D,P],[D,Zs],[P,Zs],[u,Q10]])ck(ez(he(r,s)),"exact orthogonal axes");
ck(eq(he(Rp,Rp),E(140))&&eq(he(Sp,Sp),E(60))&&eq(he(Q10,Q10),E(10)),"integer theta norms");
const expR=[em(E(-2),w2),em(E(-2),w),E(4),E(0),E(2,9),E(5,-3)];
const expS=[esc(w,2),E(2),E(4,4),E(0),E(3,-3),E(3)];
ck(Rp.every((v,i)=>eq(v,expR[i]))&&Sp.every((v,i)=>eq(v,expS[i])),"exact full positive rows");
const Q2=[E(1),en(w2),E(0),E(0),E(0),E(0)],Q3=[E(1),w2,w,E(0),E(0),E(0)];
const rest=[vm(Q2,E(3)),vm(Q3,E(3)),vm(x,E(3))];
const frame=[D,Rp,Sp,...rest],iv=inverse(frame);
for(const r of[D,Rp,Sp])for(const s of rest)ck(ez(he(r,s)),"all three retained companions");
ck(eq(em(iv.det,ec(iv.det)),E(514382400)),"positive full determinant norm");
const HH=ident(6),hp=[[E(-1,-1,2),E(-1,-2,2)],[E(2,1,2),E(-1,-1,2)]];
for(let i=0;i<2;i++)for(let j=0;j<2;j++)HH[i+4][j+4]=hp[i][j];
const zeta=[E(1),w2,w],conjugates=[];
const parity=q=>q.filter(v=>v.some(a=>(a[0]%2n+2n)%2n)).length;
for(let j=0;j<3;j++){
 const Dj=vs(F,vm(C,zeta[j])),Pj=vs(u,vm(Dj,esc(w2,1,7))),Rj=vm(Pj,E(14));
 const Zj=va(d,vm(Dj,E(1,3,14))),Sj=vm(vs(Zj,vm(Pj,E(8,3,10))),E(20)),Qj=vs(Dj,vm(u,esc(w,2)));
 const rH=mm([Rj],HH)[0],sH=mm([Sj],HH)[0],qH=mm([Qj],HH)[0];
 for(const row of[Rj,Sj,Qj,rH,sH,qH])ck(row.every(v=>v.every(a=>a[1]===1n)),"all C-conjugate original/eta rows integral");
 ck(eq(he(Rj,Rj),E(140))&&eq(he(Sj,Sj),E(60))&&eq(he(Qj,Qj),E(10)),"all conjugate levels");
 ck(eq(rH[4],E(10))&&eq(rH[5],E(4))&&eq(sH[4],E(0))&&eq(sH[5],esc(w2,6)),"actual half-period conjugacy");
 ck(eq(qH[4],E(0))&&eq(qH[5],esc(w,-2)),"whole10 actual row");
 const rp=parity(vm(Rj.slice(0,4),E(1,0,2))),sp=parity(vm(Sj.slice(0,4),E(1,0,2)));
 ck(rp===(j===0?2:4)&&sp===(j===0?2:4),"all shared half-characters positive");
 conjugates.push({j,R:Rj.map(out),S:Sj.map(out),Q10:Qj.map(out),RH:rH.map(out),SH:sH.map(out),QH:qH.map(out),shared_R_odd:rp,shared_S_odd:sp});
}
const SC=ident(6);for(let i=0;i<6;i++)for(let j=0;j<6;j++)SC[i][j]=ea(SC[i][j],em(es(w,E(1)),em(ec(C[i]),C[j])));
let cp=ident(6);const rest_checks=[];
for(let j=0;j<3;j++){
 const rows=mm(frame,cp),rh=mm(rows,HH);
 for(const arr of[rows,rh])for(const r of arr)ck(r.every(v=>v.every(a=>a[1]===1n)),"whole common positive frame including companions");
 rest_checks.push({j,companions:rows.slice(3).map(r=>r.map(out))});cp=mm(cp,SC);
}
const blocks={};
for(const N of[140,60]){
 const m=N/4,cols=[];
 for(let j=0;j<N;j++){
  const v=Array(N).fill(0);
  for(let s=0;s<2;s++)for(let r=0;r<2;r++){
   const eps=(s||r)?-1:1,phase=(s*(j+m*r))%2?-1:1;
   v[(j+N*r/2)%N]+=eps*phase/2;
  }
  v[j]--;const k=((1+N/2)*j)%N;ck(v.every((a,i)=>a===(i===k?-1:0)),"whole weighted B column");
  cols.push({j,k,sign:-1});
 }
 const actual=N===140?211:91,base=1+N/2,center=N+1;
 ck((center*base)%(2*N)===actual&&((center*center-1)/N)%2===0,"all full center phases");
 blocks[N]={g:actual,ratio:base,center,central_exponent:(center*center-1)/N,columns:cols,anchor:N===140?"[2gamma7]*odd5, scalar chi65":"[2]*odd15, scalar chi65"};
}
ck(11%10===1&&(11*11-1)/10===12,"whole10 central scalar");
const R1=[[E(1),E(0)],[E(1),E(-1)]],change=[[E(1),E(1,0,2)],[E(0),E(1)]];
const RR=mm(mm(inverse(change).inverse,R1),change);
ck(RR.every((r,i)=>r.every((v,j)=>eq(v,[[E(1,0,2),E(3,0,4)],[E(1),E(-1,0,2)]][i][j]))),"source column matrix");
const Delta=[[E(3,0,2)],[E(-1)]],Gamma=[[E(3,0,2)],[E(1)]];
ck(mm(RR,Delta).every((r,i)=>eq(r[0],[E(0),E(2)][i]))&&mm(RR,Gamma).every((r,i)=>eq(r[0],Gamma[i][0])),"actual positive strip source return");
const UQ=[[esc(w2,1,7),E(1)],[E(5,0,7),esc(w,-2)]];
ck(eq(inverse(UQ).det,E(-1)),"u Q10 common-deep determinant");
const Hbar=vs(vm(vs(c,C),del),vm(D,esc(del,1,7)));
const table={},rem={};
for(const[name,row]of Object.entries({E:E0,Y,W,Wprime:Wp,G,Hbar,L:va(vm(c,E(1,3)),d)})){
 ck(ez(he(row,D)),"all native observations D-orthogonal");
 const aa=em(he(row,P),E(7,0,5)),bb=em(he(row,Zs),E(20,0,3));
 table[name]={P:out(aa),Zstar:out(bb)};
 const rr=vs(vs(row,vm(P,aa)),vm(Zs,bb));
 rem[name]=rr.map(out);for(const s of[D,P,Zs])ck(ez(he(rr,s)),"complete native residual companion");
}
ck(rem.Y.every((v,i)=>v.every((a,j)=>a===rem.W[i][j])),"same true Y W remainder");
const padd=(a,b)=>Array.from({length:Math.max(a.length,b.length)},(_,i)=>ea(a[i]||E(0),b[i]||E(0)));
const pmul=(a,b)=>{const z=Array.from({length:a.length+b.length-1},()=>E(0));a.forEach((v,i)=>b.forEach((q,j)=>z[i+j]=ea(z[i+j],em(v,q))));return z;};
const psub=(a,b)=>padd(a,b.map(en));
const Aword=[[[E(5,0,7),E(2,0,7)],[E(0),esc(w,-2),esc(w,2)]],[[esc(w2,-5,49),esc(w2,5,49)],[E(0),E(2,0,7),E(5,0,7)]]];
const pdet=psub(pmul(Aword[0][0],Aword[1][1]),pmul(Aword[0][1],Aword[1][0]));
ck(pdet.every((v,j)=>eq(v,E(j===2?1:0))),"true full two-step determinant kappa^2");
const ptr=padd(Aword[0][0],Aword[1][1]);
ck(ptr.every((v,j)=>eq(v,[E(5,0,7),E(4,0,7),E(5,0,7)][j])),"true full two-step trace");
return{
word:{matrix:Aword.map(r=>r.map(p=>p.map(out))),det:pdet.map(out),trace:ptr.map(out),physical:"P_u,kappa P_P,kappa"},
axes:{D14:D.map(out),P:P.map(out),R140:Rp.map(out),Zstar:Zs.map(out),S60:Sp.map(out),Q10:Q10.map(out),rest:rest.map(r=>r.map(out))},
frame:{det:out(iv.det),norm:out(em(iv.det,ec(iv.det))),norm_factors:{"2":6,"3":8,"5":2,"7":2}},
conjugates,rest_checks,whole_blocks:blocks,whole10:{g:11,central_exponent:12,scalar:"chi65 fixed by the nonzero common full (D,P)=(u,Q10) joint"},
source_column_R1:RR.map(r=>r.map(out)),
source_core:"P and Zstar both -chi65 lambda R1; D14 beta; same true PC two-state only",
u_Q10:UQ.map(r=>r.map(out)),
native_projection_table:table,native_remainders:rem,
positive_native_return:"N_plus,n= -2 chi65 lambda beta^n/(b Omega^6) times h^C tested on Zstar unit with full E,Y,W,G after P->kappa P",
preserved_boundary:"No positive-axis core is assigned to R563 muminus; all cuts and all D^k coefficients retained"
};

}
if(typeof module!=="undefined")module.exports={certifyR568};
if(typeof require!=="undefined"&&require.main===module)process.stdout.write(JSON.stringify(certifyR568(),null,2)+"\n");
