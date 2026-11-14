#!/usr/bin/env node
// Exact certificate; no external dependencies.
const result=(()=>{
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


const w=E(0,1),w2=em(w,w),del=E(1,2),a=E(2,3),l=E(1,3),g=E(3,-2),alpha=E(1,-1);
const row=x=>x.map(t=>Array.isArray(t)?E(...t):E(t));
const c=row([0,0,0,0,1,0]),d=row([0,0,0,0,0,1]);
const D4=[E(1),w2,E(0,-2),E(0),E(0),E(0)],C=vm(row([1,0,-1,1,0,0]),ei(del));
const H1=[E(-1),E(2),w,E(1,1),E(0),E(0)],A=[del,esc(del,2),E(3,1),E(2,-1),E(0),E(0)];
const U=va(c,vm(d,w)),V=vs(c,vm(d,w)),D=va(va(D4,vm(U,alpha)),vm(V,w));
const F=va(D,C),Eold=va(D,vm(C,E(14))),Gold=va(vm(H1,E(13)),vm(F,g));
const Y=va(va(A,c),vm(d,E(2))),W=va(va(A,vm(c,esc(del,3))),vm(d,E(4)));
const re=(x,y,m)=>ck(x.every((v,i)=>eq(v,y[i])),m);
const me=(x,y,m)=>ck(x.every((r,i)=>r.every((v,j)=>eq(v,y[i][j]))),m);


const G=Gold,Wp=[E(4,4),E(2,4),E(4,4),E(0),E(4,2),E(4)];
const pi=[Y,W,Wp,G];
const proj=r=>r.map((v,i)=>r.map((u,j)=>em(ei(he(r,r)),em(ec(v),u))));
const PCmat=proj(C);
const rot=z=>ident(6).map((r,i)=>r.map((v,j)=>ea(v,em(es(z,E(1)),PCmat[i][j]))));
const RC=rot(E(-1)),SC=rot(w);
me(mm(RC,RC),ident(6),"pure C reflection square");
me(mm(mm(SC,SC),SC),ident(6),"pure C cubic rotation");
me(mm(RC,SC),mm(SC,RC),"sixth projection group");
re(mm([C],RC)[0],vm(C,E(-1)),"actual C sign");
for(const rr of [F,...pi,c,d,U,V])re(mm([rr],RC)[0],rr,"C reflection fixes observations and A4 lines");
const H=ident(6);
H[4][4]=E(-1,-1,2);H[4][5]=E(-1,-2,2);
H[5][4]=E(2,1,2);H[5][5]=E(-1,-1,2);
const star=M=>M[0].map((_,j)=>M.map(r=>ec(r[j])));
me(mm(H,star(H)),ident(6),"actual third-source H unitary");
me(mm(H,RC),mm(RC,H),"third source commutes with pure C sign");
re(mm([va(c,vm(d,a))],H)[0],vm(vs(c,d),E(0,2)),"exact mixed pair H image");
const integral=mat=>mat.every(rr=>rr.every(z=>z.every(q=>q[1]===1n)));
const oc=rr=>rr.reduce((s,z)=>s+((z[0][0]%2n!==0n||z[1][0]%2n!==0n)?1:0),0);
const roots=[E(1),w,w2,E(-1),en(w),en(w2)];
const rows=[];
let commonNorm=null;
for(let i=0;i<6;i++){
 const zeta=roots[i],R=rot(zeta);
 re(mm([C],R)[0],vm(C,zeta),"actual C rotation");
 for(const rr of [F,...pi])re(mm([rr],R)[0],rr,"all pi4 and F fixed");
 const Dz=vs(F,vm(C,zeta)),Ez=va(F,vm(C,esc(zeta,13)));
 re(mm([D],R)[0],Dz,"whole D branch transpose");
 re(mm([Eold],R)[0],Ez,"whole E branch transpose");
 ck(eq(he(Dz,Dz),E(14))&&eq(he(Ez,Ez),E(182))&&ez(he(Dz,Ez)),"same exact two-plane");
 for(const rr of pi)ck(ez(he(rr,Dz))&&ez(he(rr,Ez)),"complete four companions");
 const d42=vm(Dz,del),e1638=vm(Ez,E(3));
 ck(eq(he(d42,d42),E(42))&&eq(he(e1638,e1638),E(1638)),"actual covering degrees");
 const fm=[d42,e1638,vm(Y,E(2)),vm(W,E(2)),vm(Wp,E(2)),vm(G,E(6))];
 const fh=mm(fm,H);ck(integral(fm)&&integral(fh),"full original and H frames integral");
 const counts=[oc(fm[0]),oc(fm[1]),oc(fh[0]),oc(fh[1])];
 ck(counts.every(k=>k%2===0),"all complete even half characteristics");
 const det=inverse(fm).det,norm=em(det,ec(det));
 if(commonNorm===null)commonNorm=norm;else ck(eq(commonNorm,norm),"same complete frame determinant norm");
 const dx=Dz[3],ex=Ez[3];
 if(i===0)ck(ez(dx),"only original positive grid branch has x coefficient zero");
 else ck(!ez(dx),"other five branches miss the original D_n grid");
 rows.push({zeta:out(zeta),D:Dz.map(out),E:Ez.map(out),
 frame:fm.map(r=>r.map(out)),H_frame:fh.map(r=>r.map(out)),
 determinant:out(det),norm_determinant:out(norm),odd_sigma_counts:counts,
 grid_x_coefficients:{D:out(dx),E:out(ex)},C_rotation:R.map(r=>r.map(out))});
}
const expectedNorm=2n**20n*3n**10n*7n**3n*13n**2n;
ck(eq(commonNorm,E(expectedNorm)),"common frame determinant exact bad factors");
ck(43%4===3&&43%3===1&&43%7===1,"current full ratio mod84");
ck(((43*43-1)/42)%2===0,"whole42 central quotient even");
ck(1639%4===3&&1639%9===1&&1639%7===1&&1639%13===1,"old full ratio mod3276");
ck(((1639*1639-1)/1638)%2===0,"whole1638 central quotient even");
const gam7=E(3,1),gam13=E(4,1),anchor42=em(del,gam7),
anchor1638=esc(em(gam7,gam13),3);
ck(eq(em(anchor42,ec(anchor42)),E(21)),"actual Theta degree42 anchor");
ck(eq(em(anchor1638,ec(anchor1638)),E(819)),"actual Theta degree1638 anchor");
const v=vm(C,del),Z=row([1,0,-1,-2,0,0]),Qrow=row([1,0,1,0,0,0]),
r=row([0,1,0,0,0,0]),vf=[v,Z,Qrow,r,c,d],iv=inverse(vf);
const flat={};
for(const[name,rr]of Object.entries({F,Y,W,Wp,G,H1})){
 const coeff=mm([rr],iv.inverse)[0];
 ck(ez(coeff[0]),"every actual observed row is C-free");
 flat[name]=coeff.slice(1).map(out);
}
const comb=(n,k)=>{let v=1n;for(let j=1;j<=k;j++)v=v*BigInt(n-k+j)/BigInt(j);return v;};
const kernels=[];
for(let k=0;k<=6;k++)for(let j=0;j<=6-k;j++){
 const ell=6-k-j,terms=[];
 for(let r=0;r<=j;r++)terms.push({
 moment:k+r,F_power:j-r,G_power:ell,kappa_n_power:r,
 coefficient:String(comb(j,r)*14n**BigInt(j-r)*(-13n)**BigInt(r))
 });
 kernels.push({original_exponents:[k,j,ell],terms});
}
return {
 title:"R590 original six carry branches, sole B source, and complete seven-fibre reduction",
 convention:"Exact BigInt Q(omega); E(a,b,d)=(a+b omega)/d; beta=-lambda; no new ray",
 pure_C_reflection:RC.map(r=>r.map(out)),C_projection:PCmat.map(r=>r.map(out)),
 pair_H:H.map(r=>r.map(out)),branches:rows,
 frame_norm_factorization:"2^20 3^10 7^3 13^2",
 full_cores:{degree42:{ratio_mod84:43,central_quotient:44,Theta_anchor:out(anchor42),anchor_norm:21,actual_core:"beta"},
 degree1638:{ratio_mod3276:1639,central_quotient:1640,Theta_anchor:out(anchor1638),anchor_norm:819,actual_core:"beta"}},
 flat_frame:vf.map(r=>r.map(out)),flat_frame_det:out(iv.det),flat_observations:flat,
 exact_seven_fibre_kernel:kernels,
 C_moments:{m0:"1",m2:"0",m4:"0",m5:"0",m6:"-8 b Omega^6"},
 grid_scope:"On the ORIGINAL rho0 and ORIGINAL D_n, q6=q0/6; this is not the same assertion for the projected B source on D_n.",
 arithmetic_scope:"The entire pi4 rows and all original complements are preserved. The odd-C contribution cancels only in the complete partition.",
 checks:"All exact assertions passed."
};

})();
console.log(JSON.stringify(result,null,2));

