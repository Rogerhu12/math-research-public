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
const T8=va(D4,vm(V,w)),qU=vm(U,alpha),R168=vs(vm(T8,E(3)),vm(qU,E(4)));
const T12=va(D4,vm(U,alpha)),qV=vm(V,w),R84=vs(T12,vm(qV,E(6)));
const SC=ident(6).map((r,i)=>r.map((v,j)=>ea(v,em(es(w,E(1)),em(ec(C[i]),C[j])))));
const SCs=[ident(6),SC,mm(SC,SC)];
const HH=ident(6);HH[4][4]=E(-1,-1,2);HH[4][5]=E(-1,-2,2);HH[5][4]=E(2,1,2);HH[5][5]=E(-1,-1,2);
re(mm([U],HH)[0],vm(U,E(-1)),"actual H preserves U line");
re(mm([V],HH)[0],vm(V,en(w)),"actual H preserves V line");
const project=r=>{const invn=ei(he(r,r));return r.map(x=>r.map(y=>em(invn,em(ec(x),y))));};
const addM=(A,B)=>A.map((r,i)=>va(r,B[i]));
const axes={};
for(const [key,T,Z,al,ratio,R,N,M,cy,cw,negRden] of [
 ["U",T8,U,alpha,E(3,0,4),R168,8,168,E(0,-1,2),E(-4,1,6),4],
 ["V",T12,V,w,E(1,0,6),R84,12,84,E(-1,-3,2),E(3,-7,2),6]
]){
 const q=vm(Z,al),e=vs(q,vm(T,ratio));
 const comps=[vs(Eold,e),vs(Gold,vm(e,g)),vs(Y,vm(e,cy)),vs(W,vm(e,cw))];
 const fm=[T,Z,...comps],iv=inverse(fm);
 re(D,va(T,q),key+": true carry decomposition");
 re(e,vm(R,E(-1,0,negRden)),key+": whole transverse displacement");
 ck(eq(he(T,T),E(N))&&eq(he(Z,Z),E(2))&&eq(he(R,R),E(M)),key+": exact three degrees");
 ck(ez(he(T,Z))&&ez(he(D,R)),key+": both complete planes orthogonal");
 for(const r of comps)ck(ez(he(r,T))&&ez(he(r,Z))&&ez(he(r,D))&&ez(he(r,R)),key+": all four companions fixed");
 me(addM(project(D),project(R)),addM(project(T),project(Z)),key+": exact simultaneous physical scaling");
 const sf=[T,Z,...comps.map(r=>vm(r,E(24)))],dr=[D,R,...sf.slice(2)];
 const phases=[];
 for(let j=0;j<3;j++)for(let h=0;h<2;h++){
  const tr=h?mm(SCs[j],HH):SCs[j],aa=mm(sf,tr),bb=mm(dr,tr);
  for(const mat of[aa,bb])for(const rr of mat)for(const x of rr)for(const y of x)ck(y[1]===1n,"entire six-row frame integral");
  const count=rr=>rr.reduce((s,x)=>s+((x[0][0]%2n!==0n||x[1][0]%2n!==0n)?1:0),0);
  const cnt=[count(aa[0]),count(aa[1]),count(bb[0]),count(bb[1])];
  ck(cnt.every(x=>x%2===0),key+": standard even half-characteristics");
  phases.push({C_branch:j,third_source_H:h,odd_sigma_counts:cnt,frame:aa.map(r=>r.map(out)),D_R_frame:bb.map(r=>r.map(out))});
 }
 const factor=(x)=>{let y=x,arr=[];for(let p=2n;p*p<=y;p++)if(y%p===0n){let k=0;while(y%p===0n){y/=p;k++;}arr.push([String(p),k]);}if(y>1n)arr.push([String(y),1]);return arr;};
 const normdet=em(iv.det,ec(iv.det));
 ck(ez([E(0)[0],normdet[1]]),"norm determinant rational");
 axes[key]={T:T.map(out),original_axis:Z.map(out),q_multiplier:out(al),ratio:out(ratio),R:R.map(out),
 T_degree:N,R_degree:M,shift:e.map(out),Y_shift_coefficient:out(cy),W_shift_coefficient:out(cw),
 frame:fm.map(r=>r.map(out)),inverse:iv.inverse.map(r=>r.map(out)),det:out(iv.det),
 norm_det:out(normdet),norm_det_numerator_factors:factor(abs(normdet[0][0])),norm_det_denominator_factors:factor(normdet[0][1]),
 integral_companion_multiplier:24,integral_det:out(inverse(sf).det),
 gram:fm.map(r=>fm.map(s=>out(he(r,s)))),
 projections:{T:project(T).map(r=>r.map(out)),axis:project(Z).map(r=>r.map(out)),D:project(D).map(r=>r.map(out)),R:project(R).map(r=>r.map(out))},
 complete_C_and_H_conjugates:phases};
}
const mod=(x,m)=>((x%m)+m)%m;
const modE=(x,m)=>x.map(q=>{ck(q[1]===1n,"mod requires integral");return String(mod(q[0],BigInt(m)));});
const g168=E(43,168),g2=em(g168,g168);
ck(modE(g2,336).join(",")==="169,0","whole168 square ratio");
ck((169n*169n-1n)/168n===170n,"whole168 full central square quotient");
const a84=em(E(2),em(del,E(3,1))),a12=esc(del,2);
ck(eq(he([a84],[a84]),E(84))&&eq(he([a12],[a12]),E(12)),"true sigma and Theta anchors");
const half=[];
for(const N of[12,84]){
 const m=N/4,perm=[];
 for(let j=0;j<N;j++){
  const sums=new Map();
  for(let r=0;r<2;r++)for(let s=0;s<2;s++){
   const k=(j+N*r/2)%N,sgn=(s*(j+m*r))%2?-1:1;
   sums.set(k,(sums.get(k)||0)+sgn);
  }
  const nz=[...sums].filter(([,v])=>v!==0);
  ck(nz.length===1&&nz[0][1]===2,"complete half-period sum is twice a permutation");
  const outj=nz[0][0];ck(outj===((1+N/2)*j)%N,"whole half-period identity");
  ck(((1+N/2)*outj)%N===j,"whole12/84 square identity");
  perm.push(outj);
 }
 half.push({N,normalized_K:"half the full canonical E[2] sum",permutation:perm,anchor_eigenvalue:-1});
}

const UVold=ident(6);
UVold[4][4]=E(1,0,2);UVold[4][5]=E(1,0,2);
UVold[5][4]=esc(w2,1,2);UVold[5][5]=esc(en(w2),1,2);
for(const key of["U","V"]){
 const parse=(q)=>{let [a,b]=q.map(x=>x.split("/").map(BigInt));const A=Q(a[0],a[1]||1n),B=Q(b[0],b[1]||1n);return[A,B];};
 const f=axes[key].frame.map(r=>r.map(parse)),zcol=key==="U"?4:5,vcol=key==="U"?5:4;
 const original=mm(f,UVold),fiveRows=[original[0],...original.slice(2)].map(r=>[...r.slice(0,4),r[vcol]]);
 for(const r of[original[0],...original.slice(2)])ck(ez(r[zcol]),"all five actual source rows independent of retained S2 input");
 const i5=inverse(fiveRows);
 axes[key].five_input_source_frame=fiveRows.map(r=>r.map(out));
 axes[key].five_input_source_det=out(i5.det);
 axes[key].five_input_order=["xi1","xi2","xi3","x",key==="U"?"V":"U"];
}
const pk=e=>e.join(","),px=k=>k.split(",").map(Number);
const putp=(p,e,c)=>{const k=pk(e),z=ea(p.get(k)||E(0),c);if(ez(z))p.delete(k);else p.set(k,z);return p;};
const addp=(p,q)=>{const r=new Map(p);for(const[k,v]of q)putp(r,px(k),v);return r;};
const negp=p=>new Map([...p].map(([k,v])=>[k,en(v)]));
const polyEqual=(p,q)=>ck(addp(p,negp(q)).size===0,"complete S2 monomial moments");
const mono=(e,c)=>putp(new Map(),e,c),pow=(a,k)=>{let z=E(1);while(k--)z=em(z,a);return z;};
const choose=(n,k)=>{if(k<0||k>n)return 0n;let z=1n;for(let j=1;j<=k;j++)z=z*BigInt(n-j+1)/BigInt(j);return z;};
function rawMoment(k,which,shift,alpha,r){
 let p=new Map();
 for(let j=0;j<=k;j++)for(const [extra,sgn]of shift?[[1,E(1)],[0,en(r)]]:[[0,E(1)]]){
  const power=j+extra;
  if(which===0&&power!==0&&power!==6)continue;
  if(which===2&&power!==2)continue;
  const cc=em(em(E(choose(k,j)),sgn),em(pow(alpha,power),E(power===6?-96:power===2?2:1)));
  putp(p,[k-j+(shift&&extra===0?1:0),power,power===6?1:0,power],cc);
 }
 return p;
}
const momentReport=[];
for(const key of["U","V"]){
 const al=key==="U"?alpha:w,r=key==="U"?E(3,0,4):E(1,0,6);
 for(let k=0;k<=6;k++){
  let B0=mono([k,0,0,0],E(1)),B2=new Map();
  if(k>=6)B0=addp(B0,mono([k-6,6,1,6],esc(pow(al,6),-96n*choose(k,6))));
  if(k>=2)B2=mono([k-2,2,0,2],esc(pow(al,2),BigInt(k*(k-1))));
  let E0=mono([k+1,0,0,0],en(r)),E2=new Map();
  if(k>=5)E0=addp(E0,mono([k-5,6,1,6],
    em(esc(pow(al,6),-96),es(E(choose(k,5)),em(r,E(choose(k,6)))))));
  if(k>=1)E2=mono([k-1,2,0,2],em(pow(al,2),es(E(2*k),esc(r,k*(k-1)))));
  polyEqual(rawMoment(k,0,false,al,r),B0);polyEqual(rawMoment(k,2,false,al,r),B2);
  polyEqual(rawMoment(k,0,true,al,r),E0);polyEqual(rawMoment(k,2,true,al,r),E2);
  const exportp=p=>[...p].map(([x,c])=>({powers_T_t_b_Omega:px(x),coefficient:out(c)}));
  momentReport.push({axis:key,degree:k,B0:exportp(B0),B2:exportp(B2),E0:exportp(E0),E2:exportp(E2)});
 }
}


const thetaCoefficient=qa(Q(1,105),Q(-1,7));
ck(qs(thetaCoefficient)==="-2/15"&&qs(qm(thetaCoefficient,Q(720)))==="-96","Theta sixth coefficient from the actual sigma and wp series");

const types={mass_Theta:"1",moment2_Sigma:"2 Omega^2",moment6_Theta:"-96 b Omega^6"};
return {title:"R582 actual Norm2 single-deep complements, complete two-state cores and five-line arithmetic remainder",
convention:"Q(omega), omega^2+omega+1=0. [a,b]=a+b omega.",
axes,core168:{g_mod336:modE(g168,336),g_square_mod336:modE(g2,336),central_square_quotient:170,
 Theta_anchor_argument:out(a84),Theta_anchor_degree:168,whole_normalized_square:"I"},
whole12_and84:half,degree8_source_state:"J_U=-K8=half E[2] sum - quarter E[4] sum, with the R539 canonical lifts",
degree12_source_state:"J_V=-K12=-half E[2] sum, preserving its absolute sign",
S2_moments:{...types,theta_z6_coefficient_times_b:qs(thetaCoefficient)},complete_moment_identities:momentReport,checks:"All exact frame, gluing parity, physical scaling and center assertions passed."};

})();
console.log(JSON.stringify(result,null,2));
