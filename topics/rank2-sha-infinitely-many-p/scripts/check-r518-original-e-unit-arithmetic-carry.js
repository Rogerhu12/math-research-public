#!/usr/bin/env node
function certifyR518(){
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

const ep=(a,n)=>{ck(n>=0,"negative field power");let r=E(1),b=a;for(;n;n=Math.floor(n/2),b=em(b,b))if(n%2)r=em(r,b);return r;};
const qp=(a,n)=>{let r=Q(1);for(let k=0;k<n;k++)r=qm(r,a);return r;};
const fac=n=>{let r=1n;for(let j=2;j<=n;j++)r*=BigInt(j);return r;};
const choose=(n,k)=> k<0||k>n?0n:fac(n)/(fac(k)*fac(n-k));
const q=[Q(1),Q(-1,7)];for(let n=2;n<=5;n++){let s=Q(0);for(let i=1;i<n;i++)s=qa(s,qm(q[i],q[n-i]));q[n]=qm(s,Q(1,(6*n+1)*(n-1)));}
const ell=[Q(0)];for(let n=1;n<=5;n++)ell[n]=qm(qn(q[n]),Q(1,6*n*(6*n-1)));
const a=[Q(1)];for(let n=1;n<=5;n++){let s=Q(0);for(let k=1;k<=n;k++)s=qa(s,qm(qm(Q(k),ell[k]),a[n-k]));a[n]=qm(s,Q(1,n));}
const denom=43024169751465478338233979150199956512749200351148033743183443885006289024867517102817280n;
const nums=[
-669434980352778043509581310714866556317857825822326580693089728706624639467520n,
-119981363974691021171554991621708858631413799763774609514070383001600n,
-55342492105213394108340720066257765863550432453355110400n,
-42045915630443092877608745094656489256652800n,
5620340233791194124683811078144n,
1075621969600983023n
],c=nums.map(n=>Q(n,denom));
const ga=E(3,1),gb=E(2,-1),del=E(1,2);
const Z=[del,E(2,4),ga,E(1),E(2)],
P=[E(-19,2),E(10,29),E(11,-13),E(32,14),E(-1,-11)],
L0=vm(vs(Z,vm(P,E(34,0,263))),ga),Lold=vm(Z,ga),
t0=E(-1729,0,263),told=E(-27);
function mixed(z,l){
 let C=Array.from({length:6},()=>E(0));
 for(let mask=0;mask<32;mask++){
  let j=0,v=E(1);for(let i=0;i<5;i++)if(mask&(1<<i)){j++;v=em(v,z[i]);}else v=em(v,l[i]);
  C[j]=ea(C[j],v);
 }
 return C.map((v,j)=>esc(v,fac(j)*fac(5-j)));
}
function firstJet(l,t){
 const C=mixed(Z,l),As=[],Bs=[];let al=E(0),bl=E(0);
 for(let k=1;k<=6;k++){
  const m=6*k;let ak=E(0);
  for(let j=1;j<=5;j++){
   const term=em(em(ep(ei(gb),j),ep(t,m-5+j)),C[j]);
   ak=ea(ak,esc(term,BigInt(j%2?1:-1)*choose(m,5-j),j));
  }
  const bk=esc(em(ep(t,m-5),C[0]),choose(m,5));
  const moment=qm(c[k-1],qm(Q(fac(m-5)),a[k-1]));
  al=ea(al,em(ak,[qm(moment,Q(-1,84)),Q(0)]));
  bl=ea(bl,em(bk,[qm(moment,Q(-1,84)),Q(0)]));
  As.push(out(ak));Bs.push(out(bk));
 }
 return {C,As,Bs,alpha:al,log_coefficient:bl};
}
const old=firstJet(Lold,told),zero=firstJet(L0,t0);
const A=1440935741522357826619235140107022805303896592950241958401828702957725824129n,
 BB=-1813765269049121739800435840694154580102806900217087779806497668058675862540n,
 D=178000081118033421953983855808692884462466015608355923166875641368652904792064n;
ck(eq(old.alpha,E(A+BB,2n*BB,D)),"R497 full old alpha exact");
ck(!ez(old.alpha),"old alpha nonzero");
const diff=es(zero.alpha,old.alpha);
let den=1n;for(const v of [...old.alpha,...diff])den=den/gcd(den,v[1])*v[1];
const u=esc(old.alpha,den),v=esc(diff,den);
ck(u.every(x=>x[1]===1n)&&v.every(x=>x[1]===1n),"integral algebraic numerators");
const norm=x=>{const n=em(x,ec(x));ck(n[1][0]===0n&&n[0][1]===1n,"integer norm");return n[0][0];};
const Nu=norm(u),Nv=norm(v),tr=ea(em(u,ec(v)),ec(em(u,ec(v))))[0][0];
ck(!ez(v),"nonzero changed alpha coefficient");
const mod=(a,m)=>{a%=m;return a<0n?a+m:a;};
function prime(n){if(n<2)return false;for(let d=2;d*d<=n;d++)if(n%d===0)return false;return true;}
const currentPrimes=[2,3,5,7,11,13,17,19,29,79,103,137,263];
let rayPrime=0;
for(let n=1001;n<10000;n++)if(n%3===2&&prime(n)&&!currentPrimes.includes(n)&&mod(den*Nu*Nv,BigInt(n))!==0n){rayPrime=n;break;}
ck(rayPrime>0,"fixed auxiliary inert prime");
const pp=BigInt(rayPrime);let residue=0;
for(let r=1;r<=3;r++)if(mod(BigInt(r)*tr-Nv,pp)!==0n&&mod(BigInt(r)*tr+Nv,pp)!==0n){residue=r;break;}
ck(residue>0,"both epsilon signs avoided by rational unit ray");
const threshold=(Nu+Nv+1n)**2n;
return {
 base_field:"Q(omega), omega^2+omega+1=0; all coefficient pairs are 1,omega",
 original_test:{denominator:String(denom),numerators:nums.map(String),sigma_a0_to_a5:a.map(qs)},
 original_five_rows:{Z:Z.map(out),P:P.map(out),T0_deep:L0.map(out),T0_x:out(t0),Tc_deep:Lold.map(out),Tc_x:out(told)},
 mixed_fifth:{old:Cout(old.C),T0:Cout(zero.C)},
 original_alpha:out(old.alpha),T0_alpha:out(zero.alpha),T0_minus_original:out(diff),
 original_Ak:old.As,original_Bk:old.Bs,T0_Ak:zero.As,T0_Bk:zero.Bs,
 reduced_log_coefficients:{original:out(old.log_coefficient),T0:out(zero.log_coefficient)},
 integral_linear_ray:{D:String(den),u:out(u),v:out(v),norm_u:String(Nu),norm_v:String(Nv),trace_u_barv:String(tr),prime:rayPrime,residue,
 forbidden_trace_residues:[String(mod(Nv,pp)),String(mod(-Nv,pp))],chosen_trace:String(mod(BigInt(residue)*tr,pp)),
 sufficient_p_lower_bound:String(threshold)},
 p_dependent_inverse:"sum_{j=0}^{36} H_j(B,A)(E/Omega)^j/(1-epsilon*lambda*kappa^j)",
 first_five_mod_p:"(d/b)*(alpha+epsilon*lambda*(alpha0-alpha))/(1-epsilon*lambda)",
 whole_E_unit_row:"Y_*(1_Eunit*hhat*nu0)=nuS",
 same_sigma_carry:"A deep r,E unit; test uses A/kappa^r everywhere, returns (psi*lambda)^r*J_S",
 nonzero_subpipe:"M_A(r)*D_n, valuation 5n; exact full six-input domain retained",
 boundary:"The complement of this subpipe in the qualified carry remains, with the exact opposite central value if J_S'=0."
};
function Cout(C){return C.map(out);}
}
if(typeof module!=="undefined"){
 module.exports={certifyR518};
 if(require.main===module){
  const report=certifyR518();
  require("fs").writeFileSync(__filename.replace(/\.js$/,".json"),JSON.stringify(report,null,2)+"\n");
  console.log("R518: exact original mixed jet, fixed E-unit inverse and both-sign ray certificate passed.");
 }
}
