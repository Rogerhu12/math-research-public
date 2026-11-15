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



function compute(all,endpoint=0,withRanks=false){
const r670={"flat_rows":{"A":[["-1","1/2"],["2","3/2"],["2","4"]],"D":[["-19/174","19/174"],["31/58","-37/58"],["-43/29","-21/29"]],"Eperp":[["-133/429","133/429"],["217/143","-259/143"],["-602/143","-294/143"]],"Gperp":[["-5843/858","-3715/858"],["-1593/286","-123/22"],["1324/143","-266/143"]],"G00":[["-247/36","-143/36"],["-65/12","-91/12"],["13/2","-13/6"]]}};

const parse=s=>{let a=s.split("/");return Q(a[0],a[1]||1);},read=v=>v.map(parse);
const F=r670.flat_rows,af=F.A.map(read),df=F.D.map(read),ef=F.Eperp.map(read),gf=F.Gperp.map(read);
const N=5,conv=(a,b)=>Array.from({length:N+1},(_,n)=>{let s=Q(0);for(let i=0;i<=n;i++)s=qa(s,qm(a[i]||Q(0),b[n-i]||Q(0)));return s;});
const pw=(a,k)=>{let z=Array.from({length:N+1},(_,i)=>Q(i?0:1));for(let j=0;j<k;j++)z=conv(z,a);return z;};
const xx=[Q(1),Q(-1,7)];for(let n=2;n<=N;n++){let s=Q(0);for(let i=1;i<n;i++)s=qa(s,qm(xx[i],xx[n-i]));xx[n]=qm(s,Q(1,(6*n+1)*(n-1)));}
const logs=[Q(0),...xx.slice(1).map((a,i)=>qm(qn(a),Q(1,6*(i+1)*(6*(i+1)-1))))],sig=[Q(1)];
for(let n=1;n<=N;n++){let s=Q(0);for(let k=1;k<=n;k++)s=qa(s,qm(qm(Q(k),logs[k]),sig[n-k]));sig[n]=qm(s,Q(1,n));}
const minusY=xx.map((a,n)=>n===0?Q(1):qm(Q(-(3*n-1)),a)),as2=pw(sig,2),as6=pw(sig,6),f3=conv(as6,minusY),f1=conv(f3,xx),theta=conv(as2,xx);
const fact=n=>{let s=1;for(let k=2;k<=n;k++)s*=k;return s;},choose=(n,k)=>{let r=1;for(let j=1;j<=k;j++)r=r*(n+1-j)/j;return r;};
const add=(P,R)=>{let T={...P};for(const[k,c]of Object.entries(R)){T[k]=ea(T[k]||E(0),c);if(ez(T[k]))delete T[k];}return T;};
const scale=(P,c)=>Object.fromEntries(Object.entries(P).map(([k,v])=>[k,em(c,v)]).filter(([k,v])=>!ez(v)));
function mul(P,R){
 const T={},PE=Object.entries(P).map(([k,v])=>[k.split(",").map(Number),v]),RE=Object.entries(R).map(([k,v])=>[k.split(",").map(Number),v]);
 for(const[a,c]of PE)for(const[b,d]of RE){let z=a.map((x,i)=>x+b[i]);if(z[0]+z[1]+z[2]>6||z[3]>30)continue;let q=z.join(",");T[q]=ea(T[q]||E(0),em(c,d));}
 return Object.fromEntries(Object.entries(T).filter(([k,v])=>!ez(v)));
}
function linearPower(v,n){let P={"0,0,0,0":E(1)},L={};for(let i=0;i<3;i++){let e=[0,0,0,0];e[i]=1;L[e.join(",")]=v[i];}for(let i=0;i<n;i++)P=mul(P,L);return P;}
function source(i){
 const ei0=i===0?E(-170,-117,9135):E(-170,-291,9135),obs=[...af,E(i===0?1:2),E(i===0?2:-1)];
 let wr=[...df.map((x,j)=>ea(x,esc(em(ei0,af[j]),5))),esc(ei0,-87),esc(ei0,-29)];
 const hh=i===0?E(-5,-9):E(-5,-3);
 if(endpoint)wr=va(wr,vm([...af.map(x=>esc(x,5)),E(i===0?39:-24),E(i===0?-92:97)],esc(hh,endpoint,315)));
 const er=[...ef,E(0),E(0)],gr=[...gf,E(0),E(0)];
 const lp=Array.from({length:5},(_,axis)=>Array.from({length:7},(_,r)=>linearPower([wr[axis],er[axis],gr[axis]],r)));
 const obsp=obs.map(x=>{let P=[E(1)];for(let j=1;j<=36;j++)P.push(em(P.at(-1),x));return P;});
 function factor(base,coeff,axis){
 let P={};for(let h=0;h<=N;h++){let nn=base+6*h;for(let r=0;r<=Math.min(6,nn);r++){let z=nn-r;if(z>30)continue;const c=em([coeff[h],Q(0)],esc(obsp[axis][z],choose(nn,r)));for(const[k,v]of Object.entries(lp[axis][r])){let q=k.split(",").map(Number);q[3]=z;let kk=q.join(",");P[kk]=ea(P[kk]||E(0),em(c,v));}}}return P;
 }
 let flat=add(mul(factor(1,f1,0),factor(2,as2,1)),scale(mul(factor(3,f3,0),factor(0,theta,1)),E(-1)));
 for(let j=2;j<5;j++)flat=mul(flat,factor(1,sig,j));
 flat=scale(flat,E(1,0,42));
 const lc=[E(-1),E(1596,0,143),E(-789,526,143)],six=scale(linearPower(lc,6),E(-1,0,90));
 const full=add(flat,mul(flat,six));
 const Gen=Array.from({length:6},(_,r)=>Object.fromEntries(Object.entries(full).filter(([k,v])=>{let x=k.split(",").map(Number);return x[0]+x[1]+x[2]===6&&x[3]===6*r;}).map(([k,v])=>[k.split(",").slice(0,3).join(","),esc(v,i===0?1:-1)])));
 return{e:out(ei0),observation:obs.map(out),linear_rows:[wr,er,gr].map(R=>R.map(out)),C_component:lc.map(out),gen:Gen};
}
const sources=[source(0),source(1)]; 
// G00=Gperp-(q/14)Eperp, q=-263/38+263 omega/57, so q/14=(-789+526 omega)/1596.
const rat=E(-789,526,1596);
const cols=all.matrix.polys.map(P=>Object.fromEntries(Object.entries(P).map(([k,v])=>[k,read(v)]))),e0=P=>Object.fromEntries(Object.entries(P).filter(([k,v])=>+k.split(",")[1]===0));
const moment=(P,G)=>Object.entries(P).reduce((s,[k,c])=>ea(s,em(c,esc(G[k]||E(0),k.split(",").reduce((a,b)=>a*fact(+b),1)))),E(0));
let rp=[E(1)];for(let i=1;i<=6;i++)rp[i]=em(rp[i-1],en(rat));
const basePoly=Object.fromEntries(Object.entries(all.matrix.base).map(([k,v])=>[k,read(v)]));
const baseMom=[];
const raw=sources.flatMap(s=>s.gen.map(G=>{
 const G00={};for(const[k,c]of Object.entries(G)){let e=k.split(",").map(Number),q=[e[0],0,e[1]+e[2]].join(",");G00[q]=ea(G00[q]||E(0),em(c,rp[e[1]]));}
 baseMom.push({a:moment(basePoly,G),a0:moment(e0(basePoly),G),b:moment(e0(basePoly),G00)});
 return cols.map(P=>({a:moment(P,G),a0:moment(e0(P),G),b:moment(e0(P),G00)}));
}));
const AP=all.matrix.Aplus.map(r=>r.map(read)),AZ=all.matrix.Azero.map(r=>r.map(read)),B=all.polynomial_right_inverse.B.map(M=>M.map(r=>r.map(read)));
const A2=AP.map((R,i)=>R.map((x,j)=>ea(x,esc(AZ[i][j],2)))),B2=B[0].map((R,i)=>R.map((x,j)=>ea(x,esc(B[1][i][j],2))));
const BA=mm(B2,A2),Pi=ident(20).map((R,i)=>vs(R,BA[i]));
function rank(M){let T=M.map(r=>r.map(v=>v)),piv=[],r=0;for(let c=0;c<T[0].length&&r<T.length;c++){let p=r;while(p<T.length&&ez(T[p][c]))p++;if(p===T.length)continue;[T[r],T[p]]=[T[p],T[r]];T[r]=vm(T[r],ei(T[r][c]));for(let j=0;j<T.length;j++)if(j!==r&&!ez(T[j][c]))T[j]=vs(T[j],vm(T[r],T[j][c]));piv.push(c);r++;}return{rank:r,pivots:piv,matrix:T};}
const eta={};for(const s of[1,-1]){
 const jp=raw.map(R=>R.map(x=>es(es(x.a,x.a0),esc(x.b,s)))),jz=raw.map(R=>R.map(x=>ea(x.a0,esc(x.b,s)))),j2=jp.map((R,i)=>R.map((x,j)=>ea(x,esc(jz[i][j],2)))),M=withRanks?mm(j2,Pi):null,rr=withRanks?rank(M):{rank:null,pivots:[]};
 eta[String(s)]={row_plus:jp.map(R=>R.map(out)),row_zero:jz.map(R=>R.map(out)),kernel_at_tau2:M?M.map(R=>R.map(out)):null,rank:rr.rank,pivots:rr.pivots};
}
return{format:"R674 normalized pair of original S34 common sources, u=t=kappa=0 residue",source:sources.map(s=>({...s,gen:s.gen.map(G=>Object.fromEntries(Object.entries(G).map(([k,v])=>[k,out(v)])))})),moments:raw.map(R=>R.map(o=>Object.fromEntries(Object.entries(o).map(([k,v])=>[k,out(v)])))),base_moments:baseMom.map(o=>Object.fromEntries(Object.entries(o).map(([k,v])=>[k,out(v)]))),eta,sigma:sig.map(qs),wp:xx.map(qs),C_sixth_moment:"-8b Omega^6, retained as -b (Clinear)^6/90",scope:"n>=N+1 so u=kappa^N and t=kappa^(n-N) reduce to zero; actual lifts and all shallow/exterior terms still required."};

}

function massRows(all){

const parse=s=>{const x=s.split("/");return Q(x[0],x[1]||1);},read=x=>x.map(parse),row=a=>a.map(x=>Array.isArray(x)?E(...x):E(x));
const w=E(0,1),delta=E(1,2),C=vm(row([1,0,-1,1]),ei(delta)),A=row([[1,2],[2,4],[3,1],[2,-1]]),D4=row([1,[-1,-1],[0,-2],0]),H=row([-1,2,[0,1],[1,1]]),g=E(3,-2),aa=E(-5,-6,29);
const D=vs(D4,vm(A,aa)),d=he(D,D),F=va(D,C),Erow=va(D,vm(C,E(14))),Grow=va(vm(H,E(13)),vm(F,g));
ck(eq(d,E(143,0,29))&&eq(he(D,C),E(-1))&&ez(he(D,A)),"actual Dstar norms and non-orthogonal C");
const proj=(V,U)=>vs(V,vm(U,em(he(V,U),ei(he(U,U)))));
const Cp=proj(C,D),Ep=proj(Erow,D),Gp=proj(Grow,D),G00=proj(Gp,Cp);
ck(Ep.every((v,i)=>eq(v,esc(Cp[i],14))),"Eperp=14 Cperp");
const deriv=P=>{const z={};for(const[k,c]of Object.entries(P)){let e=k.split(",").map(Number);if(e[0]>=2){const fac=e[0]*(e[0]-1);e[0]-=2;z[e.join(",")]=esc(c,fac);}}return z;};
function add(P,R){const z={...P};for(const[k,c]of Object.entries(R)){z[k]=ea(z[k]||E(0),c);if(ez(z[k]))delete z[k];}return z;}
const scale=(P,c)=>Object.fromEntries(Object.entries(P).map(([k,v])=>[k,em(v,c)]).filter(([k,v])=>!ez(v)));
function mul(P,R){const z={};for(const[k,c]of Object.entries(P))for(const[l,v]of Object.entries(R)){const a=k.split(",").map((x,i)=>+x+ +l.split(",")[i]).join(",");z[a]=ea(z[a]||E(0),em(c,v));}return z;}
function pow(P,n){let z={"0,0,0":E(1)};for(let i=0;i<n;i++)z=mul(z,P);return z;}
const lin=rr=>Object.fromEntries(rr.map((c,i)=>[[0,1,2].map(j=>i===j?1:0).join(","),c]).filter(([k,v])=>!ez(v)));
const fact=n=>{let a=1;for(let i=2;i<=n;i++)a*=i;return a;};
function gen4(rr){const z=Array.from({length:4},(_,j)=>lin(rr.map(V=>V[j]))),zZ=scale(add(add(z[0],scale(z[2],E(-1))),scale(z[3],E(-2))),E(1,0,6)),zQ=scale(add(z[0],z[2]),E(1,0,2));
return scale(mul(add(mul(zZ,pow(zQ,2)),scale(pow(zZ,3),E(-1))),z[1]),E(1,0,42));}
function moment(P,rr){const gen=gen4(rr);return Object.entries(P).reduce((s,[k,c])=>ea(s,em(c,esc(gen[k]||E(0),k.split(",").reduce((a,i)=>a*fact(+i),1)))),E(0));}
const e0=P=>Object.fromEntries(Object.entries(P).filter(([k,v])=>+k.split(",")[1]===0));

const cols=all.matrix.polys.map(P=>Object.fromEntries(Object.entries(P).map(([k,v])=>[k,read(v)])));
const jr=cols.map(P=>{const dP=deriv(P);return {a:moment(dP,[D,Ep,Gp]),a0:moment(e0(dP),[D,Ep,Gp]),b:moment(e0(dP),[D,Array(4).fill(E(0)),G00])};});
const db=deriv(Object.fromEntries(Object.entries(all.matrix.base).map(([k,v])=>[k,read(v)])));
const bm={a:moment(db,[D,Ep,Gp]),a0:moment(e0(db),[D,Ep,Gp]),b:moment(e0(db),[D,Array(4).fill(E(0)),G00])};
const AP=all.matrix.Aplus.map(r=>r.map(read)),AZ=all.matrix.Azero.map(r=>r.map(read));
const BM=all.polynomial_right_inverse.B.map(M=>M.map(r=>r.map(read)));
const tt=E(2),At=AP.map((r,i)=>r.map((v,j)=>ea(v,em(tt,AZ[i][j])))),Bt=BM[0].map((r,i)=>r.map((v,j)=>ea(v,em(tt,BM[1][i][j]))));
const values={};
for(const eta of[1,-1]){
 const jp=jr.map(x=>es(es(x.a,x.a0),esc(x.b,eta))),jz=jr.map(x=>ea(x.a0,esc(x.b,eta))),j=jp.map((v,i)=>ea(v,em(tt,jz[i])));
 const rowB=Array.from({length:9},(_,k)=>j.reduce((s,c,i)=>ea(s,em(c,Bt[i][k])),E(0)));
 const delta=j.map((v,i)=>es(v,rowB.reduce((s,c,k)=>ea(s,em(c,At[k][i])),E(0))));
 values[String(eta)]={nonzero_indices:delta.map((v,i)=>!ez(v)?i:null).filter(i=>i!==null),sample:delta.map(out),row_plus:jp.map(out),row_zero:jz.map(out)};
}
return{base_moments:Object.fromEntries(Object.entries(bm).map(([k,v])=>[k,out(v)])),values,column_moments:jr.map(x=>Object.fromEntries(Object.entries(x).map(([k,v])=>[k,out(v)]))),exps:all.matrix.exps};

}

function certificate(all,g,m){

const parse=s=>{let a=s.split("/");return Q(a[0],a[1]||1);},read=v=>v.map(parse),N=5;
const cv=(a,b)=>Array.from({length:N+1},(_,n)=>{let s=Q(0);for(let i=0;i<=n;i++)s=qa(s,qm(a[i]||Q(0),b[n-i]||Q(0)));return s;});
const qp=(a,k)=>{let P=Array.from({length:N+1},(_,i)=>Q(i?0:1));for(let j=0;j<k;j++)P=cv(P,a);return P;};
const sig=g.sigma.map(parse),xx=g.wp.map(parse),s34=qp(sig,34),exps=[17,14,11,8,5,2],sc=[E(0),E(1),E(-53,0,7),E(-12,0,7),E(-80,0,7),E(-128,0,7)];
const TC=exps.map(a=>{let start=(34-2*a)/6,c=cv(s34,qp(xx,a));return Array.from({length:6},(_,r)=>[r>=start?c[r-start]:Q(0),Q(0)]);}),T=Array.from({length:6},(_,r)=>TC.map(c=>c[r])),S=mm(T,sc.map(c=>[c])).map(r=>r[0]);
const cvE=(a,b)=>Array.from({length:N+1},(_,n)=>{let s=E(0);for(let i=0;i<=n;i++)s=ea(s,em(a[i]||E(0),b[n-i]||E(0)));return s;});
const epow=(a,n)=>{let x=E(1);for(let i=0;i<n;i++)x=em(x,a);return x;};
const yminus=xx.map((x,i)=>i?qm(Q(-(3*i-1)),x):Q(1)),ss2=qp(sig,2),ss6=qp(sig,6),f3=cv(ss6,yminus),f1=cv(f3,xx),theta=cv(ss2,xx);
const af=[E(-2,1,2),E(4,3,2),E(2,4)],fac=(base,c,a)=>c.map((v,h)=>em([v,Q(0)],epow(a,base+6*h)));
let aa=cvE(fac(1,f1,af[0]),fac(2,ss2,af[1])),bb=cvE(fac(3,f3,af[0]),fac(0,theta,af[1]));
let uu=aa.map((x,i)=>es(x,bb[i]));for(const a of[af[2],E(1),E(2)])uu=cvE(uu,fac(1,sig,a));uu=uu.map(x=>esc(x,1,42));
const unweighted=[E(0),...uu.slice(0,5)];ck(unweighted.every((x,i)=>eq(x,S[i])),"original full S normalization, all six low coefficients");
const p=1009n,w=374n,md=x=>(x%p+p)%p;
for(let d=2n;d*d<=p;d++)ck(p%d!==0n,"auxiliary field is prime");ck(md(w*w+w+1n)===0n,"exact auxiliary CM embedding");
function iv(a){a=md(a);let b=p,x=1n,y=0n;while(b){let q=a/b;[a,b]=[b,a-q*b];[x,y]=[y,x-q*y];}ck(a===1n,"auxiliary denominators all units");return md(x);}
const qm0=s=>{const a=s.split("/");return md(BigInt(a[0])*iv(BigInt(a[1]||1)));},ef=x=>md(qm0(x[0])+w*qm0(x[1]));
const mul=(A,B)=>A.map(R=>B[0].map((_,j)=>md(R.reduce((s,x,k)=>s+x*B[k][j],0n))));
function eliminate(M,rhs){let A=M.map((R,i)=>rhs?[...R,rhs[i]]:R.slice()),det=1n,pivs=[],r=0,ncol=M[0].length;
 for(let c=0;c<ncol&&r<M.length;c++){let j=r;while(j<A.length&&A[j][c]===0n)j++;if(j===A.length)continue;if(j!==r){[A[j],A[r]]=[A[r],A[j]];det=md(-det);}let d=A[r][c];det=md(det*d);A[r]=A[r].map(x=>md(x*iv(d)));for(let i=0;i<A.length;i++)if(i!==r){let z=A[i][c];A[i]=A[i].map((x,j)=>md(x-z*A[r][j]));}pivs.push(c);r++;}
 return{A,rank:r,det: r===M.length&&ncol===M.length?det:0n,pivots:pivs,solution:rhs?A.map(R=>R.at(-1)):null};
}
const AP=all.matrix.Aplus.map(R=>R.map(ef)),AZ=all.matrix.Azero.map(R=>R.map(ef)),BM=all.polynomial_right_inverse.B.map(M=>M.map(R=>R.map(ef))),
 A2=AP.map((R,i)=>R.map((x,j)=>md(x+2n*AZ[i][j]))),B2=BM[0].map((R,i)=>R.map((x,j)=>md(x+2n*BM[1][i][j]))),BA=mul(B2,A2),PI=BA.map((R,i)=>R.map((x,j)=>md((i===j?1n:0n)-x)));
const piv=[0,1,2,3,4,13,15,16,17,18,19],bp=all.matrix.target.map((x,i)=>md(ef(x)-ef(all.matrix.basePlus[i])-2n*ef(all.matrix.baseZero[i]))),xp=mul(B2,bp.map(x=>[x])).map(R=>R[0]);
const sj=S.map(x=>ef(out(x))),s0=[...sj,...Array(6).fill(0n)],s1=[...Array(6).fill(0n),...sj],result={};
for(const eta of["1","-1"]){
 const RR=g.eta[eta],J2=RR.row_plus.map((R,i)=>R.map((x,j)=>md(ef(x)+2n*ef(RR.row_zero[i][j])))),MK=mul(J2,PI),K=MK.map(R=>piv.map(j=>R[j]));
 const massrow=m.values[eta].row_plus.map((x,j)=>md(ef(x)+2n*ef(m.values[eta].row_zero[j]))),massK=mul([massrow],PI)[0];
 const aug=K.map((R,i)=>[...R,md(-s0[i]),md(-s1[i])]);aug.push([...piv.map(j=>massK[j]),0n,0n]);
 const base=g.base_moments.map(x=>md(ef(x.a)+ef(x.a0)+BigInt(eta)*ef(x.b))),orig=mul(J2,xp.map(x=>[x])).map((R,i)=>md(R[0]+base[i]));
 const oldmass=md(ef(m.base_moments.a)+ef(m.base_moments.a0)+BigInt(eta)*ef(m.base_moments.b)+massrow.reduce((s,c,i)=>s+c*xp[i],0n));
 const rhs=[...orig.map(x=>md(-x)),md(1n-oldmass)],sol=eliminate(aug,rhs);ck(sol.rank===13&&sol.det!==0n,"whole augmented determinant nonzero");
 const dual=eliminate(K[0].map((_,j)=>K.map(R=>R[j]))),free=Array.from({length:12},(_,i)=>i).find(i=>!dual.pivots.includes(i)),left=Array(12).fill(0n);
 left[free]=1n;dual.pivots.forEach((p,i)=>left[p]=md(-dual.A[i][free]));
 const dot=v=>md(v.reduce((s,x,i)=>s+x*left[i],0n));
 ck(sol.solution[11]!==0n&&sol.solution[12]!==0n,"both original-S scalar numerators nonzero");
 result[eta]={matrix:aug.map(R=>R.map(String)),det:String(sol.det),left_row:left.map(String),left_pairings:{S0:String(dot(s0)),S1:String(dot(s1)),original:String(dot(orig))},old_normalized_J:String(oldmass),rhs:rhs.map(String),solution:sol.solution.map(String),c0:String(sol.solution[11]),c1:String(sol.solution[12])};
}
let den=1n;function visit(x){if(typeof x==="string"&&/^-?\d+\/\d+$/.test(x)){let d=BigInt(x.split("/")[1]);den=den/gcd(den,d)*d;}else if(Array.isArray(x))x.forEach(visit);else if(x&&typeof x==="object")Object.values(x).forEach(visit);}
visit({rows:Object.fromEntries(["1","-1"].map(s=>[s,{p:g.eta[s].row_plus,z:g.eta[s].row_zero}])),mass:m,base:g.base_moments,S:S.map(out),B:all.polynomial_right_inverse.B,A:[all.matrix.Aplus,all.matrix.Azero],poly:all.matrix.polys});
return{format:"R674 paired full S34 arithmetic adaptation with the original negative-one coefficient retained",
pivots:piv,columns:piv.map(j=>all.matrix.exps[j]),S_basis:sc.map(out),S_jets:S.map(out),S_basis_matrix:T.map(R=>R.map(out)),
base_moments:g.base_moments,mass_rows:{plus:m.values["1"],minus:m.values["-1"],base:m.base_moments},
auxiliary:{p:"1009",omega:"374",tau:"2",eta:result,interpretation:"The exact auxiliary reduction proves fixed characteristic-zero determinant and scalar-numerator polynomials are nonzero. No ordinary p sampling inference."},
fixed_denominator:String(den),
actual_lift:"For fixed N, invert the actual 13 by 13 matrix at u=kappa^N, t=0, retaining all lambda/kappa, both C-unit core terms and all nine constraints. The resulting q_N^dagger is independent of n.",
target:"The two frozen whole sources are c0 S and c1 S, with both scalars units; normalized J_N is exactly 1.",
remaining:"All six positive t coefficients, the E shallow domains including layer zero, the original Y exteriors and both complete mixed T tests remain. No N-direction recurrence is inherited by the N-dependent adapted family."};

}

function bundle(all){
 const g=compute(all,0,false),m=massRows(all),c=certificate(all,g,m);
 const base="check-r674-double-s-arithmetic-adaptation";
 c.matrix_files={eta_plus:base+"-eta-plus.json",eta_minus:base+"-eta-minus.json"};
 const files={[base+".json"]:JSON.stringify(c,null,2)+"\n"};
 for(const e of["1","-1"]){
 const R=g.eta[e],data={format:"R674 fixed characteristic-zero residue rows",eta:e,
 row_order:"i=0 then i=1; in each block original Y Taylor powers 0,6,12,18,24,30",
 column_order:"R594 original twenty C^i F^j G^(6-i-j) columns",
 normalization:"b^(1-r) times original source coefficient [z^(6r)]; i=1 includes its actual epsilon=-1 source normalization",
 formula:"J_eta(tau)=row_plus+tau row_zero; full B_C sixth moment -8b retained",
 row_plus:R.row_plus,row_zero:R.row_zero};
 files[base+(e==="1"?"-eta-plus":"-eta-minus")+".json"]=JSON.stringify(data,null,2)+"\n";
 }
 return {main:c,files};
}
if(typeof module!=="undefined")module.exports={compute,massRows,certificate,bundle};
if(typeof require!=="undefined"&&require.main===module){
 const fs=require("fs"),path=require("path");
 const all=JSON.parse(fs.readFileSync(path.join(__dirname,"check-r594-two-source-six-carry-compensation.json"),"utf8"));
 const out=bundle(all);
 if(process.argv[2]){fs.mkdirSync(process.argv[2],{recursive:true});for(const[n,t]of Object.entries(out.files))fs.writeFileSync(path.join(process.argv[2],n),t);}
 else process.stdout.write(JSON.stringify(out.main,null,2)+"\n");
}
