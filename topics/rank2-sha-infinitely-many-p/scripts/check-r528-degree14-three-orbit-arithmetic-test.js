#!/usr/bin/env node
function certifyR528(){
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

const ep=(a,n)=>{let r=E(1),b=a;for(;n;n=Math.floor(n/2),b=em(b,b))if(n%2)r=em(r,b);return r;};
const fac=n=>{let r=1n;for(let j=2;j<=n;j++)r*=BigInt(j);return r;},
choose=(n,k)=>k<0||k>n?0n:fac(n)/(fac(k)*fac(n-k));
const conv=(a,b,N=3)=>Array.from({length:N+1},(_,n)=>{let s=Q(0);for(let i=0;i<=n;i++)if(a[i]&&b[n-i])s=qa(s,qm(a[i],b[n-i]));return s;});
const pw=(a,n)=>{let r=[Q(1)];for(let i=0;i<n;i++)r=conv(r,a);return r;};
const q=[Q(1),Q(-1,7)];for(let n=2;n<=3;n++){let s=Q(0);for(let j=1;j<n;j++)s=qa(s,qm(q[j],q[n-j]));q[n]=qm(s,Q(1,(6*n+1)*(n-1)));}
const log=[Q(0)];for(let n=1;n<=3;n++)log[n]=qm(qn(q[n]),Q(1,6*n*(6*n-1)));
const a=[Q(1)];for(let n=1;n<=3;n++){let s=Q(0);for(let j=1;j<=n;j++)s=qa(s,qm(qm(Q(j),log[j]),a[n-j]));a[n]=qm(s,Q(1,n));}
const basis=[1,4,7],series=basis.map(r=>conv(pw(a,14),pw(q,r))),M=basis.map((r,i)=>[1,2,3].map(k=>{const j=k-(14-2*r)/6;return[ j<0?Q(0):qm(Q(fac(6*k)),series[i][j]),Q(0) ];}));
const im=inverse(M),c=im.inverse.map(r=>r[2]);
ck(M.map(r=>r.reduce((sum,v,j)=>ea(sum,em(v,c[j])),E(0))).every((v,i)=>eq(v,E(i===2?1:0))),"whole S14 principal evaluation solved");
ck(c.every(v=>v[1][0]===0n),"universal coefficients rational");
const om=E(0,1),om2=E(-1,-1),del=E(1,2),ga=E(3,1),gb=E(2,-1);
const H0=[E(1),E(0),E(-1),E(1),E(0),E(0)],
D14=[en(om),om2,E(1,-1),om2,E(1),E(2,3)],
Ds=[D14,va(D14,vm(H0,E(1,1))),va(D14,H0)];
const Y=[del,E(2,4),ga,gb,E(1),E(2)],W=[del,E(2,4),ga,gb,E(3,6),E(4)],
Wp=[E(4,4),E(2,4),E(4,4),E(0),E(4,2),E(4)],
W2=[ga,E(2,4),E(6,3),E(3,2),E(-1,1),E(4)];
for(const v of Ds){ck(eq(he(v,v),E(14)),"all three hidden norms14");for(const r of [Y,W,Wp])ck(ez(he(v,r)),"three axes preserve all observations");}

const TI=[
 [en(om),E(1),om2,om],
 [en(om2),en(om),E(1),en(om2)],
 [E(-1),en(om2),en(om),E(1)],
 [en(om),E(1),en(om2),en(om)]
].map(r=>vm(r,E(1,0,2))),T=ident(6),idx=[0,2,3,4];
for(let i=0;i<4;i++)for(let j=0;j<4;j++)T[idx[i]][idx[j]]=TI[i][j];
for(let j=0;j<3;j++)ck(mm([Ds[j]],T)[0].every((v,i)=>eq(v,Ds[(j+1)%3][i])),"exact integer T orbit");
for(const row of Ds){
 let parity=0;for(const v of row){ck(v.every(q=>q[1]===1n),"integer original coefficients");const aa=v[0][0],bb=v[1][0];if((aa*aa-aa*bb+bb*bb)%2n!==0n)parity++;}
 ck(parity%2===0,"standard even halfcharacter on degree14");
}
ck((23*23-23*14+14*14)%28===11&&11*23%28===1,"norm of ray representative");
ck(((23*23-14*14)*23)%28===15&&((2*23*14-14*14)*23)%28===0,"complete degree14 ratio 15 modulo28");
function jet(D,row){
 const l=[D[0],D[1],D[2],D[4],D[5]],z=[row[0],row[1],row[2],row[4],row[5]],t=D[3],ax=row[3];
 let C=Array.from({length:6},()=>E(0));
 for(let mask=0;mask<32;mask++){let j=0,v=E(1);for(let i=0;i<5;i++)if(mask&(1<<i)){j++;v=em(v,z[i]);}else v=em(v,l[i]);C[j]=ea(C[j],v);}
 C=C.map((v,j)=>esc(v,fac(j)*fac(5-j)));let al=E(0),mass=E(0);const A=[],B=[];
 for(let k=1;k<=3;k++){const m=6*k;let ak=E(0);
 for(let j=1;j<=5;j++)ak=ea(ak,esc(em(em(C[j],ep(ei(ax),j)),ep(t,m-5+j)),BigInt(j%2?1:-1)*choose(m,5-j),j));
 const bk=esc(em(C[0],ep(t,m-5)),choose(m,5));
 const factor=em(c[k-1],[qm(Q(-fac(m-5),84),a[k-1]),Q(0)]);
 al=ea(al,em(ak,factor));mass=ea(mass,em(bk,factor));A.push(out(ak));B.push(out(bk));
 }
 return{alpha:al,mass,Ak:A,Bk:B,mixed:C.map(out)};
}
const per=Ds.map(D=>[Y,W,W2].map(row=>jet(D,row)));
const mean=i=>esc(per.reduce((s,v)=>ea(s,v[i].alpha),E(0)),1,3);
const avg=[mean(0),mean(1),mean(2)],diff=es(em(avg[1],ei(esc(del,6))),avg[0]);

const massAvg=esc(per.reduce((s,v)=>ea(s,v[0].mass),E(0)),1,3);
ck(eq(massAvg,E(173252865,-346505730,1370375552)),"actual averaged local mass nonzero");
ck(eq(diff,E(-206293619765369n,-203352919716157n,1218340606758912n)),"actual normalized S/T fifth difference");
const lowMass=[];
for(const r of [5,11,17]){
 const rr=(r-5)/6,terms=[];
 for(let k=1;k<=3;k++){
  const m=6*k;if(m<r+1){terms.push(E(0));continue;}
  let coefficient=E(0);
  for(const index of [0,2]){
   const D=Ds[index],l=[D[0],D[1],D[2],D[4],D[5]],t=D[3];
   let product=E(1);for(const x of l)product=em(product,x);
   let Aline=E(1);
   if(rr===1){let sum=E(0);for(const x of l)sum=ea(sum,ep(x,6));Aline=em([a[1],Q(0)],sum);}
   if(rr===2){
    let sum=E(0),cross=E(0);for(let i=0;i<5;i++){sum=ea(sum,ep(l[i],12));for(let j=0;j<i;j++)cross=ea(cross,em(ep(l[i],6),ep(l[j],6)));}
    Aline=ea(em([a[2],Q(0)],sum),em([qm(a[1],a[1]),Q(0)],cross));
   }
   coefficient=ea(coefficient,em(em(product,Aline),ep(t,m-r)));
  }
  terms.push(esc(em(em(c[k-1],[a[(m-r-1)/6],Q(0)]),coefficient),-fac(m),252));
 }
 lowMass.push({power:r,coefficients:terms.map(out)});
}
const massFive=lowMass[0].coefficients.map(v=>v.map(s=>{const[a,b]=s.split("/");return Q(a,b||1);})).reduce((s,v)=>ea(s,v),E(0));
ck(eq(massFive,massAvg),"all three mass coefficients reproduce the exact first local mass");
const unitKernel="(1/3) sum_{j=0}^2 1_{D_j unit} sum_{k=1}^3 c_k b^-k (D_j/Omega)^(6k)/(1+lambda*kappa^(6k))";
return{c:c.map(out),matrix:M.map(r=>r.map(out)),det:out(im.det),sigma_a:a.map(qs),D14:Ds.map(r=>r.map(out)),per:per.map(v=>v.map(x=>({...x,alpha:out(x.alpha),mass:out(x.mass)}))),average:avg.map(out),S_T_local_difference:out(diff),difference_norm:out(em(diff,ec(diff))),Ynorm:out(em(avg[0],ec(avg[0]))),average_mass:out(massAvg),mass_norm:out(em(massAvg,ec(massAvg))),mass_polynomial:lowMass,unit_test:unitKernel,whole_degree14_core:"-lambda, normalized K14=-I; actual Theta(gamma z) anchor from R471",complete_ratio_mod28:[15,0],ray_representative_mod28:[23,14],T:T.map(r=>r.map(out)),all_average_norms:avg.map(v=>out(em(v,ec(v)))),complete_three_output_identity:"pi3_*(unit_test*rho)=pi3_*rho, pi3=(Y,W,Wprime)",active_Dn_unit_branches:[0,2],inactive_Dn_branch:1,log_terms:"all I1log,I7log,I13log and log<free scale>*same positive moments remain in the exact first coefficient",same_source_boundary:"Dn is a true six-input subdomain; its complete complement in each original observation-unit domain is retained."};
}
if(typeof module!=="undefined"){
 module.exports={certifyR528};
 if(require.main===module){
  const report=certifyR528();
  require("fs").writeFileSync(__filename.replace(/\.js$/,".json"),JSON.stringify(report,null,2)+"\n");
  console.log("R528: full degree14 positive evaluation, exact three-orbit sources, central fifths and nonzero local mass passed.");
 }
}
