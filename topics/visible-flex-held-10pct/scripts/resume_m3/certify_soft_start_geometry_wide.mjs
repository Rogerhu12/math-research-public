// Exact new scalar envelope for the wider R55 subrange. Does not rerun its old r<=1.05 boxes.
function certificateWide() {
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
  const Q=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b===0n)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return[a/g,b/g];};
  const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]),div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
  const cmp=(a,b)=>{const x=a[0]*b[1]-b[0]*a[1];return x<0n?-1:x>0n?1:0;};
  const pow=(a,n)=>{let v=Q(1);for(let j=0;j<n;j++)v=mul(v,a);return v;};
  const choose=(n,k)=>{if(k<0||k>n)return 0n;let v=1n;for(let j=1;j<=k;j++)v=v*BigInt(n-j+1)/BigInt(j);return v;};
  const pAdd=(a,b)=>Array.from({length:Math.max(a.length,b.length)},(_,i)=>add(a[i]||Q(0),b[i]||Q(0)));
  const pScale=(a,b)=>a.map(x=>mul(x,b));
  const pMul=(a,b)=>{const r=Array.from({length:a.length+b.length-1},()=>Q(0));for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)r[i+j]=add(r[i+j],mul(a[i],b[j]));return r;};
  const affine=(a,l,h)=>{const r=Array.from({length:a.length},()=>Q(0));for(let i=0;i<a.length;i++)for(let j=0;j<=i;j++)r[j]=add(r[j],mul(a[i],mul(Q(choose(i,j)),mul(pow(l,i-j),pow(h,j)))));return r;};
  const bernstein=(a,l,h)=>{const c=affine(a,l,h),n=c.length-1;return c.map((_,k)=>{let b=Q(0);for(let j=0;j<=k;j++)b=add(b,mul(c[j],Q(choose(k,j),choose(n,j))));return b;});};
  const repr=a=>a[0].toString()+"/"+a[1].toString();
  const positive=(a,name)=>{if(a[0]<=0n)throw Error(name+" is not strictly positive");return repr(a);};
  const one=Q(1),eta=Q(1,20),delta=Q(3,50),vu=Q(9,20),vd=Q(1,2),vstar=Q(13,100);
  const L0=Q(104,1425),L1=Q(128,2025),L2=Q(4,45),coast=Q(13024,346275);
  const A0=div(mul(vstar,L0),Q(2)),A1=div(mul(add(vstar,vu),L1),Q(2)),A2=div(mul(vu,L2),Q(2));
  const totalArea=add(add(A0,A1),add(mul(vu,coast),A2));
  if(cmp(totalArea,delta)!==0)throw Error("upstroke area mismatch");
  const Tup=add(add(L0,L1),add(coast,L2)),Td=Q(1,5);
  if(cmp(Tup,Q(90964,346275))!==0)throw Error("upstroke length mismatch");
  const rlo=Q(21,20),rhi=Q(11,10),radius2=pow(Q(67,50),2),K2=Q(1936,1323);
  const asinLo=add(add(Q(13,20),div(pow(Q(13,20),3),Q(6))),mul(Q(3,40),pow(Q(13,20),5)));
  const chiGap=sub(mul(Q(4),pow(asinLo,2)),mul(Q(15,8),add(one,A0)));
  positive(chiGap,"characteristic square gap");
  // At r >= rlo, K_mer^2 <= (15/8)^2 / (rlo^2*(k^2-vstar^2)) < (123/10)^2.
  const root2=sub(pow(Q(1,5),2),pow(vstar,2));
  const curvatureGap=sub(mul(mul(pow(Q(123,10),2),pow(rlo,2)),root2),pow(Q(15,8),2));
  positive(curvatureGap,"protected curvature square gap");
  // The exact flat-ramp primitive has three polynomial pieces.
  const left=Array.from({length:6},()=>Q(0));
  left[4]=div(one,mul(Q(4),mul(pow(eta,2),sub(one,eta))));
  left[5]=neg(div(one,mul(Q(10),mul(pow(eta,3),sub(one,eta)))));
  const middle=[div(mul(Q(3,20),pow(eta,2)),sub(one,eta)),
                neg(div(eta,mul(Q(2),sub(one,eta)))),
                div(one,mul(Q(2),sub(one,eta)))];
  const right=pAdd([Q(-1,2),one],affine(left,one,Q(-1)));
  const pieces=[[left,Q(0),eta],[middle,eta,sub(one,eta)],[right,sub(one,eta),one]];
  const gapPolynomial=(aRef,sRef)=>{
    const a=pAdd([one],pScale(pAdd(aRef,[Q(-1)]),rhi));
    const s=pScale(sRef,rhi);
    return pAdd([radius2],pAdd(pScale(pMul(a,a),neg(K2)),pScale(pMul(s,s),Q(-1))));
  };
  const upGap=sub(radius2,add(mul(K2,pow(add(one,mul(rhi,delta)),2)),pow(mul(rhi,Tup),2)));
  positive(upGap,"upstroke envelope gap");
  let min=upGap,count=1;
  const summaries=[{piece:"upstroke",boxes:1,minimum_gap:repr(upGap)}];
  const cover=(name,aRef,sRef,l,h,parts)=>{
    const p=gapPolynomial(aRef,sRef),width=div(sub(h,l),Q(parts));
    let local=null;
    for(let j=0;j<parts;j++){
      const lo=add(l,mul(Q(j),width));
      const bs=bernstein(p,lo,width);
      for(const z of bs){positive(z,name+" Bernstein coefficient");if(local===null||cmp(z,local)<0)local=z;if(cmp(z,min)<0)min=z;}
      count++;
    }
    summaries.push({piece:name,boxes:parts,minimum_gap:repr(local)});
  };
  const Ld=Q(2,25),Cd=Q(1,25),vdLd=mul(vd,Ld);
  for(let i=0;i<pieces.length;i++){
    const [P,l,h]=pieces[i];
    cover("down acceleration "+i,pAdd([add(one,delta)],pScale(P,neg(vdLd))),[Tup,Ld],l,h,8);
  }
  cover("down coast",[sub(add(one,delta),div(vdLd,Q(2))),neg(mul(vd,Cd))],[add(Tup,Ld),Cd],Q(0),one,1);
  for(let i=0;i<pieces.length;i++){
    const [P,l,h]=pieces[i];
    const aRef=pAdd([one],pScale(pAdd([Q(1,2),Q(-1)],P),vdLd));
    cover("down relaxation "+i,aRef,[add(add(Tup,Ld),Cd),Ld],l,h,8);
  }
  const D0=Q(67,25),ell=Q(1,100),D=add(D0,ell),K=Q(123,10);
  const supportBefore=Q(87,1000),supportAfter=sub(supportBefore,div(ell,Q(2)));
  const reach=div(one,K),reachRatio=div(reach,D);
  const H=Q(13493439,25000000),held3=Q(1653761667,5600000000),held4=Q(2770344693,7918400000);
  const Hratio=div(H,D),held3ratio=div(held3,D),held4ratio=div(held4,D);
  positive(sub(supportAfter,reach),"support versus focal radius");
  positive(sub(reachRatio,Q(3,100)),"reach ratio");
  positive(sub(Hratio,Q(1,5)),"held-patch diameter ratio");
  positive(sub(held3ratio,Q(1,10)),"m3 held ratio");
  positive(sub(held4ratio,Q(1,10)),"n4 held ratio");
  positive(sub(K,Q(120000,9801)),"conditional R21-tail curvature");
  return {
    complete_surface_conditions:{
      D0:repr(D0),cylinder_full_length_upper:repr(ell),D:repr(D),
      actual_global_K_upper:repr(K),support_before:repr(supportBefore),support_after:repr(supportAfter),
      reach_lower:repr(reach),reach_over_D:repr(reachRatio),
      H_diameter_over_D:repr(Hratio),m3_held_over_D:repr(held3ratio),n4_held_over_D:repr(held4ratio),
      current_q060_tail_inherits_R21_background:false
    },
    status:"proved_by_exact_rational_arithmetic",
    scope:"R55 wider design subrange only; new upper r=1.1, first cycle only; no tail or solution inferred",
    delta_ref:repr(delta),r_interval:[repr(rlo),repr(rhi)],
    up_stages:[[0,"13/100",repr(L0)],["13/100","9/20",repr(L1)],["9/20","9/20",repr(coast)],["9/20",0,repr(L2)]],
    down_stages:[[0,"-1/2",repr(Ld)],["-1/2","-1/2",repr(Cd)],["-1/2",0,repr(Ld)]],
    up_area:repr(totalArea),up_length:repr(Tup),down_length:repr(Td),period:repr(add(Tup,Td)),
    characteristic_square_margin:repr(chiGap),protected_curvature_square_margin:repr(curvatureGap),
    envelope_squared_radius:repr(radius2),n3_radius_factor_squared_upper:repr(K2),
    boxes:count,minimum_Bernstein_gap:repr(min),pieces:summaries
  };
}
console.log(JSON.stringify(certificateWide(),null,2));

