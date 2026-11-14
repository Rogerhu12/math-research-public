#!/usr/bin/env node
// R559: whole degree144 square core, native exclusive carry and exact C projection.
function certifyR559(){
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


const w=E(0,1),w2=em(w,w),del=E(1,2),gam=E(3,1),gb=ec(gam),unit=i=>Array.from({length:6},(_,j)=>E(i===j?1:0));
const c=unit(4),dr=unit(5),H0=[1,0,-1,1,0,0].map(v=>E(v)),C=vm(H0,ei(del));
const D4=[E(1),w2,E(0,-2),E(0),E(0),E(0)],M=va(c,vm(dr,E(2,3))),F=va(va(D4,C),M),V=vs(F,c),R=vm(V,esc(del,2));
const H1=[E(-1),E(2),w,E(1,1),E(0),E(0)],G=va(vm(H1,E(13)),vm(F,E(3,-2)));
const A=[del,esc(del,2),gam,gb,E(0),E(0)],Y=va(va(A,c),vm(dr,E(2))),W=va(va(A,vm(c,esc(del,3))),vm(dr,E(4)));
const L=va(vm(c,E(1,3)),dr),u=va(vm(c,esc(w,1,2)),vm(dr,esc(es(E(1),w),1,2)));
const HH=ident(6),pair=[[E(-1,-1,2),E(-1,-2,2)],[E(2,1,2),E(-1,-1,2)]];
for(let i=0;i<2;i++)for(let j=0;j<2;j++)HH[i+4][j+4]=pair[i][j];
const RH=mm([R],HH)[0];ck(R.every(x=>x.every(q=>q[1]===1n))&&RH.every(x=>x.every(q=>q[1]===1n)),"whole R144 rows integral");
ck(eq(he(V,V),E(12))&&ez(he(V,c))&&ez(he(V,C)),"orthogonal plane12");
ck(eq(he(R,R),E(144)),"whole144");
const half=vm(R,E(1,0,2));let odd4=0;for(let i=0;i<4;i++){ck(half[i].every(q=>q[1]===1n),"first4 fullperiod");if(half[i].some(q=>(q[0]%2n+2n)%2n))odd4++;}
ck(odd4===3&&eq(half[5],E(-4,1)),"three odd shared factors and d multiplier");
const N=144,B=[];
for(let j=0;j<N;j++){
 const col=Array(N).fill(0);for(let s=0;s<2;s++)for(let r=0;r<2;r++)col[(j+72*r)%N]+=((s*j)%2?-1:1)/2;
 col[j]--;const k=(73*j+72)%N,sgn=j%2?-1:1;
 ck(col.every((v,i)=>v===(i===k?sgn:0)),"whole B144 column");
 B.push({j,k,sign:sgn});
}
for(let j=0;j<N;j++){const a=B[j],b=B[(a.k+1)%N];ck(a.sign*b.sign===-1&&b.k===(j+73)%N,"full negative X73");ck(a.k===(73*j+72)%N,"full negative Z73");}
const mod=(x,n)=>((x%n)+n)%n,cmul=(x,y,n)=>[mod(x[0]*y[0]-x[1]*y[1],n),mod(x[0]*y[1]+x[1]*y[0]-x[1]*y[1],n)];
const gp=[91,72],sq=cmul(gp,gp,288),central=cmul([145,0],[73,144],288);
ck(sq[0]===217&&sq[1]===144&&central.every((x,i)=>x===sq[i]),"actual full center");
ck((145*145-1)/144===146,"even central Weyl phase");
const P4=Array.from({length:4},()=>Array(4).fill(0));
for(let s=0;s<2;s++)for(let r=0;r<2;r++)for(let j=0;j<4;j++)P4[(j+2*r)%4][j]+=(s||r?-1:1)*(s*(j+r)%2?-1:1)/4;
for(let i=0;i<4;i++)for(let j=0;j<4;j++)ck(P4[i][j]===((i===j?1:0)-(i===(4-j)%4?1:0))/2,"whole weighted odd projection");
const proj=r=>vs(vs(r,vm(c,he(r,c))),vm(V,esc(he(r,V),1,12)));
const Y0=proj(Y),W0=proj(W),G0=proj(G),T=[Y0,W0,G0].map(r=>vm(r,esc(del,12)));
const frame=[c,H0,R,...T],inv=inverse(frame),ndet=em(inv.det,ec(inv.det));
ck(eq(inv.det,E(8895744,25069824))&&eq(ndet,E(484615600275456)),"complete frame");
const invariants={Y,W,L,u,V,H1,G,c};
for(const[name,row]of Object.entries(invariants))ck(ez(he(row,C)),"C rotation preserves "+name);
for(const tau of[w,w2])ck(ez(he(vs(vm(F,es(E(1),tau)),vm(c,E(2))),C)),"C preserves J37");
const zeta=[E(1),w2,w],perm=[];for(let j=0;j<3;j++){const k=zeta.findIndex(z=>eq(z,em(w,zeta[j])));ck(k===(j+2)%3,"exact q branch permutation");perm.push([j,k]);}
const inner={};for(const[name,row]of Object.entries({Y,W,Yc:vs(Y,vm(c,E(2))),Wc:vs(W,vm(c,esc(del,6))),u,L,H1,G,dr,C,c}))inner[name]=out(esc(he(row,V),1,12));
const r0=[[E(-1),E(1)],[E(0),E(1)]],d2=r0.map(r=>r.map(en));
const hs=[[E(1,0,2)],[E(1)]],ds=[[E(1)],[E(-1)]];
ck(mm(d2,hs).every((r,i)=>eq(r[0],en(hs[i][0]))),"D square h negative");
ck(mm(d2,ds).every((r,i)=>eq(r[0],[E(2),E(1)][i])),"D square delta");
const HHk=vm(vs(c,C),del),KKk=vm(va(c,C),del);
ck(eq(he(HHk,HHk),E(6))&&eq(he(KKk,KKk),E(6))&&ez(he(HHk,KKk))&&ez(he(HHk,V))&&ez(he(KKk,V)),"true norm6 outputs");
return{
V12:V.map(out),R144:R.map(out),R144H:RH.map(out),
g144:gp,g144square:sq,B144_ratio:[73,144],central_factor:145,central_phase_exponent:146,
anchor:"sigma(12z): normalized K=-1; B2=+1; hence whole K144^2=B2",
B144:B,weighted_half_P4:P4,shared_odd_count:odd4,d_half_multiplier:out(half[5]),
two_source_Dsquare:d2.map(r=>r.map(out)),
frame:{rows:frame.map(r=>r.map(out)),det:out(inv.det),norm:out(ndet),norm_factors:{"2":16,"3":11,"13":3,"19":1}},
D_projection_coefficients:inner,
C_mu3:{branch_permutation:perm,preserved:Object.keys(invariants).concat(["Jomega","Jomega2"]),surviving_odd3:["-y sigma^3","sigma^3"],killed:"x sigma^3"},
HK6:{H:HHk.map(out),K:KKk.map(out),Gram:[[6,0],[0,6]],full_rho_kernels:["sigma(delta(h+k)) B0(k-h)","sigma(delta(h+k)) B3(k-h)"],retained:"R144 and all three T companions; K unit cannot be forgotten"},
exclusive_carry:{depth:"2m>=n",plus:"c-C deep n,C unit",minus:"-c-C deep n,C unit",
small_parameters:["kappa^(2m-n)","kappa^(2m)"],actual_remaining:"u_perp deep,L_perp unit; four separate native Mellin unit cuts"}
};
}
if(typeof module!=='undefined')module.exports={certifyR559};
if(typeof require!=='undefined'&&require.main===module)process.stdout.write(JSON.stringify(certifyR559(),null,2)+'\n');
