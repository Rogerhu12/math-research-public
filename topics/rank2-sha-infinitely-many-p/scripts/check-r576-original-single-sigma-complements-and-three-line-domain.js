#!/usr/bin/env node
// Exact certificate; no external dependencies.
const result = (() => {
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


const w=E(0,1),w2=em(w,w),del=E(1,2),a=E(2,3),l=E(1,3),g=E(3,-2);
const row=x=>x.map(t=>Array.isArray(t)?E(...t):E(t));
const re=(x,y,m)=>ck(x.every((v,i)=>eq(v,y[i])),m);
const me=(x,y,m)=>ck(x.every((r,i)=>r.every((v,j)=>eq(v,y[i][j]))),m);
const c=row([0,0,0,0,1,0]),d=row([0,0,0,0,0,1]);
const D4=[E(1),w2,E(0,-2),E(0),E(0),E(0)];
const C=vm(row([1,0,-1,1,0,0]),ei(del));
const H1=[E(-1),E(2),w,E(1,1),E(0),E(0)];
const A=[del,esc(del,2),E(3,1),E(2,-1),E(0),E(0)];
const D=va(va(D4,c),vm(d,a)),F=va(D,C);
const Eb=va(D,vm(C,E(14))),Gb=va(vm(H1,E(13)),vm(F,g));
const Y=va(va(A,c),vm(d,E(2))),W=va(va(A,vm(c,esc(del,3))),vm(d,E(4)));
const Tc=va(D4,vm(d,a)),Rc182=vs(vm(c,E(13)),Tc);
const Cc=va(C,vm(Tc,E(1,0,13))),Hc=va(H1,vm(Tc,esc(g,1,13)));
const Ec=vm(Cc,E(14)),Gc=va(vm(Hc,E(13)),vm(Cc,g));
const Yc=va(vs(Y,c),vm(Tc,E(1,0,13)));
const Wc=va(vs(W,vm(c,esc(del,3))),vm(Tc,esc(del,3,13)));
const ec0=vs(c,vm(Tc,E(1,0,13)));
const Td=va(D4,c),z=vm(d,a),Rd14=vs(Td,z);
const Cd=va(C,vm(Td,E(1,0,7))),Hd=va(H1,vm(Td,esc(g,1,7)));
const Ed=vm(Cd,E(14)),Gd=va(vm(Hd,E(13)),vm(Cd,g));
const Yd=vs(vs(Y,vm(d,E(2))),vm(Td,esc(l,2,7)));
const Wd=vs(vs(W,vm(d,E(4))),vm(Td,esc(l,4,7)));
const ed0=vs(z,Td);
const fc=[Tc,c,Ec,Gc,Yc,Wc],fd=[Td,z,Ed,Gd,Yd,Wd];
const project=r=>{
 const nn=ei(he(r,r));
 return r.map((v,i)=>r.map((u,j)=>em(nn,em(ec(v),u))));
};
const addM=(A,B)=>A.map((r,i)=>va(r,B[i]));
const SC=ident(6).map((r,i)=>r.map((v,j)=>ea(v,em(es(w,E(1)),em(ec(C[i]),C[j])))));
const SCs=[ident(6),SC,mm(SC,SC)];
me(mm(SCs[2],SC),ident(6),"pure C order three");
for(const r of [c,d,Y,W,F,Gb,H1])re(mm([r],SC)[0],r,"required observation fixed by C");
const axis= {};
for(const [key,t,x,f,e,ycoef,wcoef,secondary,scale] of [
 ["c",Tc,c,fc,ec0,E(1),esc(del,3),Rc182,39],
 ["d",Td,z,fd,ed0,em(E(2),ei(a)),em(E(4),ei(a)),Rd14,21]
]){
 const fi=inverse(f),gr=f.map(r=>f.map(s=>he(r,s)));
 ck(ez(he(t,x)),"independent original axes");
 for(const r of f.slice(2)){
  ck(ez(he(r,t))&&ez(he(r,x)),"all four complete companions are orthogonal");
 }
 re(Eb,va(f[2],e),key+": E exact");
 re(Gb,va(f[3],vm(e,g)),key+": G exact");
 re(Y,va(f[4],vm(e,ycoef)),key+": Y exact");
 re(W,va(f[5],vm(e,wcoef)),key+": W exact");
 ck(ez(he(D,secondary)),key+": D orthogonal second axis");
 me(addM(project(D),project(secondary)),addM(project(t),project(x)),key+": same complete two-plane");
 const scaled=[t,x,...f.slice(2).map(r=>vm(r,E(scale)))];
 const scaledDR=[D,secondary,...scaled.slice(2)];
 const phases=[];
 for(let j=0;j<3;j++){
  const fm=mm(scaled,SCs[j]),drm=mm(scaledDR,SCs[j]);
  for(const mat of [fm,drm]) for(const rr of mat)for(const v of rr) for(const q of v)
    ck(q[1]===1n,key+": complete integral C-conjugate frame");
  const oddCount=rr=>rr.reduce((n,v)=>n+((v[0][0]%2n!==0n||v[1][0]%2n!==0n)?1:0),0);
  const cnt=[oddCount(fm[0]),oddCount(fm[1]),oddCount(drm[0]),oddCount(drm[1])];
  ck(cnt[0]%2===1&&cnt[1]%2===1&&cnt[2]%2===0&&cnt[3]%2===0,key+": standard half-characteristics");
  phases.push({j,odd_sigma_counts:cnt,frame:fm.map(r=>r.map(out)),D_secondary_frame:drm.map(r=>r.map(out))});
 }
 axis[key]={frame:f.map(r=>r.map(out)),inverse:fi.inverse.map(r=>r.map(out)),
 det:out(fi.det),norm_det:out(em(fi.det,ec(fi.det))),gram:gr.map(r=>r.map(out)),
 integral_companion_multiplier:scale,integral_det:out(inverse(scaled).det),
 secondary:secondary.map(out),secondary_norm:out(he(secondary,secondary)),
 projection_D:project(D).map(r=>r.map(out)),
 projection_original_first:project(t).map(r=>r.map(out)),
 projection_original_second:project(x).map(r=>r.map(out)),
 projection_secondary:project(secondary).map(r=>r.map(out)),
 exact_shift:e.map(out),Y_shift_coefficient:out(ycoef),W_shift_coefficient:out(wcoef),
 complete_C_conjugates:phases};
}
ck(eq(he(Tc,Tc),E(13))&&eq(he(Rc182,Rc182),E(182)),"c-plane exact degrees");
ck(eq(he(Td,Td),E(7))&&eq(he(z,z),E(7))&&eq(he(Rd14,Rd14),E(14)),"d-plane exact degrees");
ck(eq(inverse(fc).det,E(6188,1092)),"c complete determinant");
ck(eq(inverse(fd).det,E(43316,7644)),"d complete determinant");
const normc=2n**4n*7n**2n*13n**3n*19n,normd=normc*49n;
ck(eq(em(inverse(fc).det,ec(inverse(fc).det)),E(normc)),"c determinant norm factorization");
ck(eq(em(inverse(fd).det,ec(inverse(fd).det)),E(normd)),"d determinant norm factorization");
const G7=E(3,1),G13=E(4,1),G91=em(G7,G13);
ck(eq(em(G7,ec(G7)),E(7))&&eq(em(G13,ec(G13)),E(13)),"actual odd anchors");
ck(eq(G91,E(11,6))&&eq(em(G91,ec(G91)),E(91)),"actual even182 Theta anchor");
ck(183%4===3&&183%7===1&&183%13===1,"full ratio modulus364 CRT");
ck(((183*183-1)/182)%2===0,"complete central identity cocycle, even182");
ck(((15*15-1)/14)%2===0,"complete central identity cocycle, even14");
// Exact generic sigma moment identities. Variables are T,t,b,Omega.
const key=e=>e.join(","), ex=k=>k.split(",").map(Number);
const pp=()=>new Map(), put=(p,e,c)=>{let k=key(e),v=ea(p.get(k)||E(0),c);if(ez(v))p.delete(k);else p.set(k,v);return p;};
const mono=(e,c=E(1))=>put(pp(),e,c);
const pa=(p,q)=>{let r=new Map(p);for(const [k,v]of q)put(r,ex(k),v);return r;};
const ps=(p,q)=>pa(p,new Map([...q].map(([k,v])=>[k,en(v)])));
const peq=(p,q)=>ck(ps(p,q).size===0,"entire generic moment polynomial");
const pow=(x,n)=>{let y=E(1);while(n--)y=em(y,x);return y;};
const bin=(n,k)=>{let q=1n;for(let i=1;i<=k;i++)q=q*BigInt(n-i+1)/BigInt(i);return q;};
function moment(k,shift,r,mult){
 let p=pp();
 for(let j=0;j<=k;j++){
  const coeff=E(bin(k,j));
  for(const [extra,sgn]of shift?[[1,E(1)],[0,en(r)]]:[[0,E(1)]]){
   const m=j+extra;
   if(m!==1&&m!==7)continue;
   const tt=k-j+(shift&&extra===0?1:0),tp=j+extra;
   const bpow=m===7?1:0,om=m;
   const cc=em(em(coeff,sgn),em(pow(mult,m),E(m===7?24:1)));
   put(p,[tt,tp,bpow,om],cc);
  }
 }
 return p;
}
const moments=[];
for(const [which,r,mult]of [["c",E(1,0,13),E(1)],["d",E(1),a]]){
 for(let k=0;k<=6;k++){
  const simple=moment(k,false,r,mult),want=k?mono([k-1,1,0,1],esc(mult,k)):pp();peq(simple,want);
  const shifted=moment(k,true,r,mult);
  let expected=mono([k,1,0,1],em(mult,es(E(1),esc(r,k))));
  if(k===6)expected=pa(expected,mono([0,7,1,7],esc(pow(mult,7),24)));
  peq(shifted,expected);
  moments.push({axis:which,D_degree:k,
   sigma_integral:[...simple].map(([mon,c])=>({powers_T_t_b_Omega:ex(mon),coefficient:out(c)})),
   shifted_sigma_integral:[...shifted].map(([mon,c])=>({powers_T_t_b_Omega:ex(mon),coefficient:out(c)}))});
 }
}
// Whole Norm2 source and original observations, no marginal substitution.
const UV=[[E(1),w],[E(1),en(w)]],uvinv=inverse(UV);
ck(eq(uvinv.det,esc(en(w),2)),"Norm2 frame determinant");
const cUV=uvinv.inverse[0],dUV=uvinv.inverse[1];
const uUV=esc(E(1),1,2);
const us=vm(va(vm(cUV,w),vm(dUV,E(1,-1))),uUV);
re(us,[E(-1,0,2),esc(en(w2),1,2)],"original u is minus (U+omega squared V)/2");
const Fu=va(cUV,vm(dUV,a)),Yu=va(cUV,vm(dUV,E(2))),Wu=va(vm(cUV,esc(del,3)),vm(dUV,E(4))),Lu=va(vm(cUV,l),dUV);
re(Fu,[E(1,-1),w],"full carry pair");
re(Yu,[esc(en(del),1,2),E(3,2,2)],"full Y pair");
re(Wu,[E(-1,2,2),E(7,10,2)],"full W pair");
re(Lu,[w,del],"full L pair");
const rhoPair=[en(w),w],etaPair=[en(w2),E(1)],deltaPair=vs(rhoPair,etaPair);
re(deltaPair,[en(del),en(em(del,w2))],"complete Delta pair source on Theta-Sigma,Sigma-Theta");
re(vs(deltaPair,[deltaPair[1],deltaPair[0]]),vm(rhoPair,E(3)),"whole reflection Delta minus Rc Delta");
const reflectUV=[[E(0),E(-1)],[E(-1),E(0)]];
const RC=[[E(-1),E(0)],[E(0),E(1)]];
me(mm(mm(UV,RC),uvinv.inverse),reflectUV,"actual original c-reflection");
const urow=vm(va(vm(c,w),vm(d,E(1,-1))),E(1,0,2));
const Lrow=va(vm(c,l),d);
const ulDet=inverse([[urow[4],urow[5]],[Lrow[4],Lrow[5]]]).det;
return {
title:"R576 entire single-original-sigma deep complements and exact remaining three-line domain",
coefficient_convention:"Each coefficient [a,b] is a+b*omega; omega^2+omega+1=0. Exact rationals only.",
axes:axis,
cores:{actual_scalar:"beta=-lambda",T13:{degree:13,g_mod_26:1,anchor:"sigma((4+omega)z)"},
T7:{degree:7,g_mod_14:1,anchor:"sigma((3+omega)z)"},
R182:{degree:182,g_mod_364:183,anchor:"Theta((11+6omega)z)",central_quotient:(183*183-1)/182},
R14:{degree:14,g_mod_28:15,anchor:"Theta((3+omega)z)",central_quotient:(15*15-1)/14}},
moment_polynomials:moments,
norm2:{matrix:UV.map(r=>r.map(out)),inverse:uvinv.inverse.map(r=>r.map(out)),
rho_pair_XY:rhoPair.map(out),eta_pair_XY:etaPair.map(out),Delta_pair_XY:deltaPair.map(out),
original_c:cUV.map(out),original_d:dUV.map(out),original_u:us.map(out),
F_pair:Fu.map(out),Y_pair:Yu.map(out),W_pair:Wu.map(out),L_pair:Lu.map(out),
actual_reflection:reflectUV.map(r=>r.map(out)),
remaining_unit_lines:[[E(1),E(1)],[E(1),E(-1)],[E(1),w2]].map(r=>r.map(out)),
u_L_pair_determinant:out(ulDet)},
scope:"Only the exact whole-source scalar rectangles are used. The remaining three-line mixed unit domain is retained; no I4, I1 or original central nonvanishing is asserted.",
checks:"All exact assertions passed; no sample primes or floating point calculations."
};

})();
console.log(JSON.stringify(result,null,2));
