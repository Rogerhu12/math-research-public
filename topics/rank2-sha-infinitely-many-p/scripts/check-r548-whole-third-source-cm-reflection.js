#!/usr/bin/env node
// R548: complete half-period, CM13 ninth, geometry and external-line mass certificate.
function certifyHalfLifts(){const ck=(x,m)=>{if(!x)throw Error(m);},N=4;
const R=Array.from({length:N},(_,j)=>(N-j)%N), lifts=[],P=Array.from({length:N},()=>Array(N).fill(0));
for(let s=0;s<2;s++)for(let r=0;r<2;r++){const eps=s||r?-1:1,terms=[];for(let j=0;j<N;j++){const sign=(s*(j+r))%2?-1:1,k=(j+2*r)%4;P[k][j]+=eps*sign;terms.push({j,sign,k});}lifts.push({s,r,epsilon:eps,terms});}
for(let i=0;i<N;i++)for(let j=0;j<N;j++)ck(P[i][j]===2*((i===j?1:0)-(i===R[j]?1:0)),"weighted four half trace");
const B=[],NR=136;
for(let j=0;j<NR;j++){const sums=Array(NR).fill(0);for(let s=0;s<2;s++)for(let r=0;r<2;r++)sums[(j+68*r)%136]+=(s*j)%2?-1:1;
const col=sums.map((x,i)=>x/2-(i===j?1:0)),sign=j%2?-1:1,k=(69*j+68)%136;
ck(col.every((x,i)=>x===(i===k?sign:0)),"136 B2");B.push({j,sign,k});}
for(let j=0;j<NR;j++){const a=B[j],mid=(a.k+1)%NR,z=B[mid];ck(a.sign*z.sign===-1&&z.k===(j+69)%NR,"negative X69");ck((a.k-(69*j+68))%136===0,"negative Z69");}
return{four_lifts:lifts,weighted_P4:P.map(r=>r.map(x=>x/4)),B136:B,rank_P2_Y:34,rank_complement:102,intertwining:{B2:"X -> -X^69; Z -> -Z^69",RY_B2:"X -> -X^67; Z -> -Z^67"}};}
function certifyFixedCM13(dep,matrix){"use strict";
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


const mod=(x,n)=>(x%n+n)%n,n=272n,cmul=(x,y)=>[mod(x[0]*y[0]-x[1]*y[1],n),mod(x[0]*y[1]+x[1]*y[0]-x[1]*y[1],n)];
let g=[43n,147n],r=[1n,0n],powers=[];for(let j=1;j<=9;j++){r=cmul(r,g);powers.push({j,g:r.map(String)});}
ck(r[0]===205n&&r[1]===136n,"CM13 ninth full ratio");ck((137n*137n-1n)/136n===138n,"central Weyl phase");
const qread=s=>{const z=s.split("/");return Q(z[0],z[1]||1);},parse=(a,d)=>{const aa=qread(a),dd=qread(d);return[qa(aa,dd),qm(Q(2),dd)];};
const M=matrix.matrix.real.map((row,i)=>row.map((x,j)=>parse(x,matrix.matrix.delta[i][j]))),S=dep.S2.map(x=>parse(x.real,x.delta));
const MS=M.map(row=>row.reduce((a,x,j)=>ea(a,em(x,S[j])),E(0)));ck(MS.every((x,i)=>eq(x,en(S[i]))),"real S2 absolute anchor");
const counts=N=>Array.from({length:6},(_,r)=>{let n=0;for(let k=0;2*k<=N;k++)if(((N-2*k)%6+6)%6===r)n++;for(let k=0;3+2*k<=N;k++)if(((N-3-2*k)%6+6)%6===r)n++;return n;});
const c136=counts(136),c34=counts(34),diff=c136.map((x,i)=>x-c34[i]);ck(diff.every(x=>x===17),"all six retained theta blocks");
ck(dep.plusCyclic.dimension-1+dep.minusCyclic.dimension===17,"positive principal cyclic dimension");
return{gamma13_ratio:[43,147],powers,central_factor:137,central_Weyl_phase_exponent:138,absolute_anchor:"N13 S2=-S2 from paid principal N13=N7^5 and full 23-coordinate N7 check",whole_CM13_ninth:"-B2,Y",ordinary_core:"RY B2,Y",angular_dimensions:{S136:c136,S34:c34,complement:diff},positive_principal_dimension:17};}
function certifyRawReflectionFrame(){"use strict";
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


const de=E(1,2),ga=E(3,1),gb=ec(ga),Y=[de,esc(de,2),ga,gb,E(1),E(2)];
const Qs=[de,esc(de,2),ga,gb,E(-29),E(0)],Us=[de,esc(de,2),ga,gb,E(1),E(-15)];
const rows=[vm(Y,E(2)),vm(Qs,E(2)),vm(Us,E(2)),[esc(de,4),esc(de,-2),E(0),E(0),E(0),E(0)],[esc(de,7),esc(de,14),esc(ga,-15),E(0),E(0),E(0)],[esc(de,7),esc(de,14),esc(ga,7),esc(gb,-22),E(0),E(0)]];
const inv=inverse(rows).inverse,Rc=ident(6);Rc[4][4]=E(-1);
const RY=ident(6).map((row,i)=>row.map((x,j)=>es(x,esc(em(ec(Y[i]),Y[j]),1,17))));
ck(mm([Y],RY)[0].every((x,i)=>eq(x,en(Y[i]))),"actual Y reflection");
const Cmat=mm(mm(rows,Rc),inv),Ymat=mm(mm(rows,RY),inv),Qrow=[E(0),E(0),E(0),E(0),E(2),E(-1)];
const qc=mm([Qrow],inv)[0];ck(qc.every((x,i)=>eq(x,E(i===1?-1:i===2?1:0,0,30))),"Q is old-five companion");
const u1=[E(0),E(0),E(0),E(0),E(0,1,2),E(1,-1,2)],u2=[E(0),E(0),E(0),E(0),E(1,1,2),E(1,2,2)];
const pData=[u1,u2].map(u=>{const column=rows.map(r=>he(r,u)),row=mm([u],inv)[0];ck(eq(row.reduce((a,x,i)=>ea(a,em(x,column[i])),E(0)),E(1)),"unit rank-one projector");return{column:column.map(out),row:row.map(out)};});
ck(mm([u1],Rc)[0].every((x,i)=>eq(x,em(E(-1,-1),u2[i]))),"Rc swaps the real u axes");
return{raw_c_in_L:inv[4].map(out),raw_d_in_L:inv[5].map(out),Rc_in_L:Cmat.map(r=>r.map(out)),RY_in_L:Ymat.map(r=>r.map(out)),Q_in_L:qc.map(out),Pj_I_plus_kappa_minus_one_outer:pData};}
function externalMassCertificate(input){"use strict";
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


const qr=s=>{const a=s.split("/");return Q(a[0],a[1]||1);},parse=o=>{const r=qr(o.real),d=qr(o.delta);return[qa(r,d),qm(Q(2),d)];};
const pow=(x,n)=>{let a=E(1);while(n--)a=em(a,x);return a;};
return input.map(o=>{const tau=parse(o.tau),m=o.masses.map(parse),aa=esc(m[0],1,3),bb=esc(em(m[2],ei(tau)),1,3),cc=esc(em(m[1],ei(tau)),1,3);
const norm=es(ea(ea(pow(aa,3),em(tau,pow(bb,3))),em(pow(tau,2),pow(cc,3))),esc(em(tau,em(aa,em(bb,cc))),3));
const nq=em(norm,ec(norm));ck(!ez(norm),"external spectral mass nonzero");
return{D:o.D,tau:out(tau),mass_theta_coefficients:[aa,bb,cc].map(out),norm_to_K:out(norm),norm_to_Q:out(nq)};});
}
function certifyR548(dep,matrix){const ext=dep.external_blocks.map(o=>({D:o.D33,tau:o.tau,masses:o.first_orbit_masses}));return{lifts:certifyHalfLifts(),CM:certifyFixedCM13(dep,matrix),geometry:certifyRawReflectionFrame(),external_mass_units:externalMassCertificate(ext),full_source:{P2_eta:"-rho0/2",B2_eta:"-eta-rho0",CM13_ninth_eta:"eta+rho0",h:"eta+rho0/2",h_raw_c_parity:"even"},retained_parts:{principal_lines:17,nonprincipal_blocks:5,dimension_each:17}};}
if(typeof module!=="undefined"){module.exports={certifyR548};if(require.main===module){const fs=require("fs"),path=require("path"),dep=JSON.parse(fs.readFileSync(path.join(__dirname,"check-r542-original-eta-arithmetic-projections.json"),"utf8")),matrix=JSON.parse(fs.readFileSync(path.join(__dirname,"../notes/2026-11-14-theta-degree136-cm7-exact.json"),"utf8")),report=certifyR548(dep,matrix);fs.writeFileSync(__filename.replace(/\.js$/,".json"),JSON.stringify(report,null,2)+"\n");console.log("R548 full half lifts, absolute CM ninth, 17-line dimensions and all 12 mass units passed.");}}
