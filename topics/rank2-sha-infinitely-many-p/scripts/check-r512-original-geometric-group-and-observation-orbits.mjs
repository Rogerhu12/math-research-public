#!/usr/bin/env node
const certificate=(()=>{
const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){[a,b]=[b,a%b]}return a}
function q(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]}
const add=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>[-a[0],a[1]], sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>q(a[0]*b[0],a[1]*b[1]), div=(a,b)=>q(a[0]*b[1],a[1]*b[0]);
function pow(a,n){let r=q(1);for(;n;n>>=1,a=mul(a,a))if(n&1)r=mul(r,a);return r}
const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1], qs=a=>a[1]===1n?String(a[0]):a[0]+"/"+a[1];
const c=(a=0,b=0)=>[Array.isArray(a)?a:q(a),Array.isArray(b)?b:q(b)];
const ca=(a,b)=>[add(a[0],b[0]),add(a[1],b[1])], cn=a=>[neg(a[0]),neg(a[1])], cs=(a,b)=>ca(a,cn(b));
const cm=(a,b)=>[sub(mul(a[0],b[0]),mul(q(3),mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0]))];
const cc=a=>[a[0],neg(a[1])], norm=a=>add(mul(a[0],a[0]),mul(q(3),mul(a[1],a[1])));
const ci=a=>[div(a[0],norm(a)),neg(div(a[1],norm(a)))], cd=(a,b)=>cm(a,ci(b));
const ce=(a,b)=>eq(a[0],b[0])&&eq(a[1],b[1]), cj=a=>({real:qs(a[0]),delta:qs(a[1])});
function cp(a,n){let r=c(1);for(;n;n>>=1,a=cm(a,a))if(n&1)r=cm(r,a);return r}
function dot(a,b){return a.map((x,i)=>cm(x,cc(b[i]))).reduce(ca,c())}
function mm(A,B){return A.map(row=>B[0].map((_,j)=>row.map((x,k)=>cm(x,B[k][j])).reduce(ca,c())))}

function cinv(A){
 const n=A.length,B=A.map((r,i)=>[...r,...r.map((_,j)=>c(i===j?1:0))]);
 for(let j=0;j<n;j++){
  let r=j;while(r<n&&ce(B[r][j],c()))r++;if(r===n)throw Error("singular");
  [B[j],B[r]]=[B[r],B[j]];const sc=ci(B[j][j]);B[j]=B[j].map(x=>cm(x,sc));
  for(let i=0;i<n;i++)if(i!==j){const t=B[i][j];B[i]=B[i].map((x,k)=>cs(x,cm(t,B[j][k])))}
 }
 return B.map(r=>r.slice(n));
}
function cdet(A){
 const B=A.map(r=>r.slice());let ans=c(1);
 for(let j=0;j<B.length;j++){
  let r=j;while(r<B.length&&ce(B[r][j],c()))r++;if(r===B.length)return c();
  if(r!==j){[B[j],B[r]]=[B[r],B[j]];ans=cn(ans)}
  const diag=B[j][j];ans=cm(ans,diag);
  for(let i=j+1;i<B.length;i++){const t=cd(B[i][j],diag);for(let k=j;k<B.length;k++)B[i][k]=cs(B[i][k],cm(t,B[j][k]))}
 }
 return ans;
}

const om=c(q(-1,2),q(1,2)), om2=cm(om,om), delta=c(0,1), gamma=c(q(5,2),q(1,2)), gb=cc(gamma);
const q1=[c(q(-3,14),q(-9,14)),c(1),c(),c(),c(q(9,14),q(-1,14)),c(q(9,14),q(13,14))];
const q2=[c(q(11,14),q(5,14)),c(),c(1),c(),c(q(1,7),q(3,7)),c(q(-13,7),q(3,7))];
const Q0=q1.map((x,i)=>ca(x,cm(om,q2[i])));
const iq=dot(q2,Q0);
const Qb=q2.map((x,i)=>cm(gamma,cs(cm(c(5),x),cm(iq,Q0[i]))));
if(!ce(dot(Q0,Q0),c(5))||!ce(dot(Qb,Qb),c(515))||!ce(dot(Q0,Qb),c()))throw Error("hidden two axes mismatch");
const TI=[
[cn(om),c(1),om2,om],
[cn(om2),cn(om),c(1),cn(om2)],
[c(-1),cn(om2),cn(om),c(1)],
[cn(om),c(1),cn(om2),cn(om)]
].map(row=>row.map(x=>cd(x,c(2))));
const inds=[0,2,3,4], T=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>c(i===j?1:0)));
for(let i=0;i<4;i++)for(let j=0;j<4;j++)T[inds[i]][inds[j]]=TI[i][j];
const T2=mm(T,T),T3=mm(T2,T);
for(let i=0;i<6;i++)for(let j=0;j<6;j++)if(!ce(T3[i][j],c(i===j?1:0)))throw Error("T order");
const Y=[delta,c(0,2),gamma,gb,c(1),c(2)], W=[delta,c(0,2),gamma,gb,c(0,3),c(4)];
const Wp=mm([W],T)[0],W2=mm([W],T2)[0];
const orbits=[Q0,Qb].map(row=>[row,mm([row],T)[0],mm([row],T2)[0]]);
for(const orbit of orbits)for(const row of orbit)for(const target of [Y,W,Wp,W2])if(!ce(dot(row,target),c()))throw Error("not common companion");
function rref(A){
 const B=A.map(r=>r.slice()), piv=[];
 let i=0;
 for(let j=0;j<B[0].length&&i<B.length;j++){
  let u=i;while(u<B.length&&ce(B[u][j],c()))u++;
  if(u===B.length)continue;
  [B[i],B[u]]=[B[u],B[i]];
  const sc=ci(B[i][j]);B[i]=B[i].map(x=>cm(x,sc));
  for(let k=0;k<B.length;k++)if(k!==i){const t=B[k][j];B[k]=B[k].map((x,l)=>cs(x,cm(t,B[i][l])));}
  piv.push(j);i++;
 }
 return {matrix:B,pivots:piv,rank:i};
}
const a=cd(dot(orbits[0][1],Q0),c(5)), b=cd(dot(orbits[0][1],Qb),c(515));
const E=orbits[0][1].map((x,i)=>cs(cs(x,cm(a,Q0[i])),cm(b,Qb[i])));
const nf=dot(E,E),rank=rref(orbits.flat());
if(ce(nf,c()))throw Error("no third direction");
for(const row of [Q0,Qb,Y,W,Wp,W2])if(!ce(dot(E,row),c()))throw Error("E orthogonality");
const basis=[Q0,Qb,E], norms=[c(5),c(515),nf];
const torbitMatrix=basis.map(row=>{const moved=mm([row],T)[0];return basis.map((b,i)=>cd(dot(moved,b),norms[i]));});
const Gtarget=[Y,W,Wp].map(a=>[Y,W,Wp].map(b=>dot(a,b)));
const targetDet=cdet(Gtarget);

const Cvec=[c(q(1,2)),c(),cm(c(q(1,2)),om2),cm(c(q(-1,2)),om),c(q(-1,2)),c()];
const U=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>cs(c(i===j?1:0),cm(c(2),cm(cc(Cvec[i]),Cvec[j])))));
const TU=mm(T,U);const TU2=mm(TU,TU), cent1=mm(TU2,T),cent2=mm(T,TU2),cent3=mm(TU2,U),cent4=mm(U,TU2);const centralTU2=cent1.every((row,i)=>row.every((x,j)=>ce(x,cent2[i][j])))&&cent3.every((row,i)=>row.every((x,j)=>ce(x,cent4[i][j])));
let tp=TU, traces=[];
for(let j=1;j<=12;j++){traces.push(tp.reduce((acc,row,i)=>ca(acc,row[i]),c()));tp=mm(tp,TU);}
const frame=[Y,W,Wp,Q0,Qb,E], frameDet=cdet(frame), Ti=cinv(frame), block=mm(mm(frame,T),Ti);
const commonGram=basis.map(a=>basis.map(b=>dot(a,b)));
const I=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>c(i===j?1:0)));
const Tpow=[I,T,T2],Zpow=[I,TU2,mm(TU2,TU2)];
const YY=[],WW=[],sourceY=[],sourceW=[];
function integralCM(x){
 const a=add(x[0],x[1]),b=mul(q(2),x[1]);
 return a[1]===1n&&b[1]===1n;
}
for(let j=0;j<3;j++)for(let e=0;e<2;e++){
 const mat=mm(Zpow[j],e?U:I),row=mm([Y],mat)[0];
 if(!row.every(integralCM))throw Error("nonintegral Y orbit");
 if(!ce(dot(row,row),c(34)))throw Error("Y orbit norm");
 YY.push(row);sourceY.push(cm(cp(om2,j),e?cn(om):c(1)));
}
for(let j=0;j<3;j++)for(let i=0;i<3;i++){
 const row=mm([W],mm(Tpow[i],Zpow[j]))[0];
 if(!row.every(integralCM))throw Error("nonintegral W orbit");
 if(!ce(dot(row,row),c(72)))throw Error("W orbit norm");
 WW.push(row);sourceW.push(cm(cp(om2,j),[c(1),c(),cn(om2)][i]));
}
function rowKey(row){return row.map(x=>qs(x[0])+","+qs(x[1])).join(";");}
if(new Set(YY.map(rowKey)).size!==6||new Set(WW.map(rowKey)).size!==9)throw Error("duplicate orbit");
const YsGram=YY.map(a=>YY.map(b=>dot(a,b)));
const Yrank=rref(YY),Wrank=rref(WW);
const group=[];
for(let i=0;i<3;i++)for(let j=0;j<3;j++)for(let e=0;e<2;e++)group.push(mm(mm(Tpow[i],Zpow[j]),e?U:I));
if(new Set(group.map(A=>A.map(rowKey).join("/"))).size!==18)throw Error("group size");

return{
 variables:["xi1","xi2","xi3","xi4","c","d0"],
 Q0:Q0.map(cj),Qb:Qb.map(cj),norms:[cj(c(5)),cj(c(515))],q_inner:cj(iq),
 orbits:orbits.map(o=>o.map(row=>row.map(cj))),
 geometric_group_order:18,Y_orbit:YY.map(row=>row.map(cj)),Y_orbit_amplitudes:sourceY.map(cj),Y_orbit_rank:Yrank.rank,Y_orbit_Gram:YsGram.map(row=>row.map(cj)),W_orbit:WW.map(row=>row.map(cj)),W_orbit_amplitudes:sourceW.map(cj),W_orbit_rank:Wrank.rank,orbit_span_rank:rank.rank,TU_square_central:centralTU2,TU_square:TU2.map(row=>row.map(cj)),TU:TU.map(row=>row.map(cj)),common_six_frame_determinant:cj(frameDet),T_in_complete_common_frame:block.map(row=>row.map(cj)),TU_traces:traces.map(cj),E:E.map(cj),E_norm:cj(nf),
 Q0T_decomposition:{Q0:cj(a),Qb:cj(b),E:cj(c(1))},
 T_on_common_three:torbitMatrix.map(row=>row.map(cj)),
 retained_Y_W_Wprime_Gram:Gtarget.map(row=>row.map(cj)),retained_Gram_det:cj(targetDet),
 comment:"Actual six-input computation; no new core assigned to E solely from this geometry."
};
})();
process.stdout.write(JSON.stringify(certificate,null,2)+"\n");
