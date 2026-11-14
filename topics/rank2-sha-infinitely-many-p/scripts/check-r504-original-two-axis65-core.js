#!/usr/bin/env node
/* R504 exact certificate. All dyadic numbers remain inside the exact
   IEEE-754 integer/dyadic range; no floating approximation is used.
   Run: node check-r504-original-two-axis65-core.js */
function certifyR504() {
  "use strict";
  const ck=(q,m)=>{if(!q)throw Error(m);};
  const a=(x,y=0)=>[x,y], ad=(x,y)=>[x[0]+y[0],x[1]+y[1]],
    su=(x,y)=>[x[0]-y[0],x[1]-y[1]],
    mu=(x,y)=>[x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1]],
    sc=(x,c)=>[x[0]*c,x[1]*c], cj=x=>[x[0]-x[1],-x[1]],
    no=x=>x[0]*x[0]-x[0]*x[1]+x[1]*x[1],
    eq=(x,y)=>x[0]===y[0]&&x[1]===y[1];
  const eye=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>a(i===j?1:0)));
  const dot=(x,y)=>x.reduce((s,t,i)=>ad(s,mu(t,y[i])),a(0));
  const he=(x,y)=>dot(x,y.map(cj));
  const MM=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,x,k)=>ad(s,mu(x,B[k][j])),a(0))));
  const rm=(v,M)=>MM([v],M)[0];
  const om=a(0,1),om2=a(-1,-1),del=a(1,2),I=[0,2,3,4];
  const vv=[a(1),om,sc(om2,-1),a(-1)];
  const U4=eye(4).map((row,i)=>row.map((x,j)=>su(x,sc(mu(vv[i],cj(vv[j])),.5))));
  const U=eye(6);
  for(let i=0;i<4;i++)for(let j=0;j<4;j++)U[I[i]][I[j]]=U4[i][j];
  const Y=[del,sc(del,2),a(3,1),a(2,-1),a(1),a(2)],
    W=[del,sc(del,2),a(3,1),a(2,-1),sc(del,3),a(4)],
    V=[a(2,2),del,a(2,2),a(0),a(2,1),a(2)],
    VU=rm(V,U),R=V.map((x,i)=>ad(x,VU[i])),
    C=[a(.5),a(0),a(-.5,-.5),a(0,-.5),a(-.5),a(0)],
    aa=a(-2,1);
  ck(eq(he(V,V),a(18))&&eq(he(V,VU),a(14.5)),"V axes Gram");
  ck(eq(he(R,R),a(65))&&eq(he(C,C),a(1))&&eq(he(R,C),a(0)),"R,C Gram");
  ck(V.every((x,i)=>eq(su(x,VU[i]),mu(aa,C[i]))),"difference axis");
  ck(eq(he(Y,R),a(34,1))&&eq(he(Y,C),a(1,3)),"Y transport");
  ck(eq(he(W,R),a(58,14))&&eq(he(W,C),a(0)),"W transport");
  ck(eq(he(Y,V),a(17,-3))&&eq(he(Y,VU),a(17,4)),"two Y pipes");

  const H=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]].map(row=>row.map(x=>a(x)));
  const E=[a(1),om,om2,a(1)].map((x,i)=>Array.from({length:4},(_,j)=>j===i?x:a(0)));
  const O=[[sc(om,-1),a(0),a(0),a(0)],[a(0),a(0),om2,a(0)],[a(0),a(0),a(0),om],[a(0),a(1),a(0),a(0)]];
  const T4=MM(MM(E,H),O).map(row=>row.map(x=>sc(x,.5))),T=eye(6);
  for(let i=0;i<4;i++)for(let j=0;j<4;j++)T[I[i]][I[j]]=T4[i][j];
  const RT=rm(R,T),CT=rm(C,T),RTexpected=[a(3,1),a(2,4),a(6,3),a(0),a(-1,1),a(4)];
  ck(RT.every((x,i)=>eq(x,RTexpected[i])),"actual five-sigma R T");
  ck(CT.every((x,i)=>eq(x,i===3?om2:a(0))),"C T = omega^2 xi4");

  const r=C.map(x=>mu(om,x)),k=R.map((x,i)=>su(x,r[i])),
    nk=k.reduce((s,x)=>s+no(x),0),hr=he(k,r);
  ck(k.every(x=>x.every(Number.isInteger))&&nk===66&&eq(hr,a(-1)),"R/C complete lattice phase");
  const k0=W.map((x,i)=>su(sc(x,.5),C[i])),
    nk0=k0.reduce((s,x)=>s+no(x),0),hc=he(k0,C);
  ck(k0.every(x=>x.every(Number.isInteger))&&nk0===19&&eq(hc,a(-1)),"C/W complete lattice phase");

  const Q=[1,2,3,4].map(i=>Array.from({length:6},(_,j)=>
    su(su(a(i===j?260:0),sc(mu(cj(R[i]),R[j]),4)),sc(mu(cj(C[i]),C[j]),260))));
  ck(Q.every(row=>row.every(x=>x.every(Number.isInteger))),"integral complementary rows");
  ck(Q.every(row=>eq(he(row,R),a(0))&&eq(he(row,C),a(0))),"whole companion cross terms");
  const frame=[R.map(x=>sc(x,2)),C.map(x=>sc(x,2)),...Q];
  const Gram=frame.map(row=>frame.map(col=>he(row,col)));

  const invmod=(x,m)=>{let r0=m,r1=((x%m)+m)%m,t0=0,t1=1;
    while(r1){const q=Math.floor(r0/r1);[r0,r1]=[r1,r0-q*r1];[t0,t1]=[t1,t0-q*t1];}
    ck(r0===1,"modular inverse");return((t0%m)+m)%m;};
  const gp=m=>{const p=[Number(23776637887n%BigInt(m)),Number(77586679170n%BigInt(m))],
    inv=invmod(no(p)%m,m);return mu(p,p).map(x=>((x*inv)%m+m)%m);};
  ck(eq(gp(130),a(1))&&eq(gp(520),a(131))&&eq(gp(8),a(3)),"complete CM residues");
  const perm=[];
  for(let j=0;j<260;j++){
    const col=Array(260).fill(0);
    for(let x=0;x<2;x++)for(let y=0;y<2;y++)col[(j+130*y)%260]+=((x*(j+y))%2?-1:1)/2;
    const image=(131*j)%260;
    ck(col.every((x,i)=>x===(i===image?1:0)),"whole S260 half sum");
    ck((131*image)%260===j,"whole S260 square");
    perm.push(image);
  }

  const pts=[];for(let m=0;m<4;m++)for(let n=0;n<4;n++)pts.push([m,n]);
  const ix=t=>((t[0]%4+4)%4)*4+(t[1]%4+4)%4,
    nm=t=>((no(t)%4)+4)%4,ls=[[0,0],[1,0],[0,1],[1,1]],
    det=(x,y)=>x[0]*y[1]-x[1]*y[0];
  const PR=Array.from({length:16},()=>Array(16).fill(0)),
    UC=Array.from({length:16},(_,i)=>Array.from({length:16},(_,j)=>i===j?1:0));
  for(let j=0;j<16;j++)for(const l of ls){
    const m=pts[j],l1=mu(om,l),
      ex=mu(a(29,7),mu(cj(l),m))[1]+nm(l)+det(l1,m);
    PR[ix(ad(m,sc(l1,2)))][j]+=((ex%2+2)%2?-1:1)/2;
    UC[ix(ad(m,sc(l,2)))][j]-=((det(l,m)%2+2)%2?-1:1)/2;
  }
  const expected=Array.from({length:16},(_,i)=>Array.from({length:16},(_,j)=>i===j?1:0));
  for(let j=0;j<16;j++)for(const l of ls)expected[ix(ad(pts[j],sc(l,2)))][j]-=.5;
  ck(PR.every((row,i)=>row.every((x,j)=>x===expected[i][j])),"all sixteen actual sources");
  const ip=n=>[[1,0],[0,1],[-1,0],[0,-1]][(n%4+4)%4],
    e0=pts.map((_,i)=>[i===0?1:0,0]),
    e1=pts.map(t=>[nm(t)%2?.25:-.25,0]),
    h=pts.map(t=>[t[0]%2===0&&t[1]%2===0?-.5:0,0]),
    u=e0.map((x,i)=>[x[0]+h[i][0]/2,0]),
    v=e1.map((x,i)=>[x[0]-h[i][0]/2,0]),
    q=e1.map((x,i)=>ip(-nm(pts[i])).map(y=>x[0]*y)),
    z=q.map((x,i)=>[x[0]-h[i][0]/2,x[1]]),
    apply=(M,vec)=>M.map(row=>row.reduce((s,x,j)=>ad(s,sc(vec[j],x)),a(0)));
  const basis=[u,v,z,h],sp=[1,-1,1,-1],su0=[1,1,-1,-1];
  basis.forEach((vec,j)=>{
    ck(apply(PR,vec).every((x,i)=>eq(x,sc(vec[i],sp[j]))),"R half sum four-source action");
    ck(apply(UC,vec).every((x,i)=>eq(x,sc(vec[i],su0[j]))),"C reflection four-source action");
  });
  return {
    basis:"(u,v,z,h)",coordinates:"(xi1,xi2,xi3,xi4,c,d0)",
    V_prime:V,V_prime_U:VU,R,C,reflection_U:U,
    two_V_gram:[[18,29/2],[29/2,18]],two_V_gram_determinant:455/4,
    R_C_gram:[[65,0],[0,1]],B_coefficient:aa,
    full_frame:frame,full_frame_Gram:Gram,
    frame_determinant_absolute:8*260**4,
    R_minus_omegaC:k,norm_lattice_sum:nk,conjugate_omegaC_times_k:hr,
    W_half_minus_C:k0,norm_lattice_sum_CW:nk0,conjugate_C_times_k0:hc,
    g_mod130:gp(130),g_mod520:gp(520),g_mod8:gp(8),
    K260:"-chi65 * (1/2 sum_{E[2]} T_t)",chi65_square:1,
    chi65_anchor:"sigma(z-8t) sigma(8z+t), diagonal odd Gram (65,65)",
    complete_S260_permutation:perm,complete_16_source_half_sum:PR,
    half_sum_action:sp,C_reflection_action:su0,
    R_core_action_divided_by_chi65:[-1,1,-1,1],
    rectangle_signs:["(-1)^r","1","(-1)^(r+s)","(-1)^s"],
    rectangle_common_scalar:"chi65^r lambda^(r+s)",
    Y_R_pair:he(Y,R),Y_C_pair:he(Y,C),W_R_pair:he(W,R),
    Y_V_pair:he(Y,V),Y_VU_pair:he(Y,VU),
    R_after_T:RT,C_after_T:CT,
    raw_five_sigma_R_norms:RT.map(no),
    mixed_domain_boundary:"The Y and W test must be transposed by the displayed physical R/C contractions; independent companion rows do not delete the resulting carry."
  };
}

if (typeof module !== "undefined") {
  module.exports = { certifyR504 };
  if (require.main === module) {
    const report = certifyR504();
    require("fs").writeFileSync(__filename.replace(/\.js$/, ".json"),
      JSON.stringify(report, null, 2) + "\n");
    console.log("R504 full lattice phases, whole S260, four-source core and physical frame verified.");
  }
}
