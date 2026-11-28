// New R87 extension: rhi=23/20 and a Jensen upper bound for first-strip height.
// This does not replace the frozen rhi=11/10 certificate.
// Reuses R55's exact polynomial/Bernstein method; these are new profile inputs.
// No field arrays or BVP. Actual execution is recorded separately.
function certificate() {
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
  const one=Q(1),eta=Q(1,20),delta=Q(3,50),vu=Q(9,20),vd=Q(1,2);
  const L0=Q(10,57),L2=Q(4,45),coast=Q(1,855);
  const A0=div(mul(vu,L0),Q(2)),A2=div(mul(vu,L2),Q(2));
  const totalArea=add(A0,add(mul(vu,coast),A2));
  if(cmp(totalArea,delta)!==0)throw Error("upstroke area mismatch");
  const Tup=add(L0,add(coast,L2)),Td=Q(1,5);
  if(cmp(Tup,Q(227,855))!==0)throw Error("upstroke length mismatch");
  const rlo=Q(21,20),rhi=Q(23,20),radius2=pow(Q(67,50),2),K2=Q(1936,1323);
  const k=Q(1,2),S=Q(27,40),B=Q(27,10),z=div(vu,k);
  let asinLo=Q(0),term=z;
  for(let j=0;j<6;j++){
    asinLo=add(asinLo,term);
    term=mul(term,mul(pow(z,2),Q((2*j+1)*(2*j+1),2*(j+1)*(2*j+3))));
  }
  const chiSquaredLo=mul(pow(asinLo,2),div(rlo,mul(B,add(one,mul(rlo,A0)))));
  const chiGap=sub(chiSquaredLo,pow(S,2));
  positive(chiGap,"characteristic square gap");
  const root2=sub(pow(k,2),pow(vu,2));
  const protectedCurvatureSquared=div(pow(div(B,rlo),2),root2);
  const curvatureGap=sub(pow(Q(123,10),2),protectedCurvatureSquared);
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
  const D=Q(67251,25000),wH=Q(27,50),alpha=Q(4,5),b=Q(3,10);
  const J=add(mul(Q(2),S),b);
  const coreUpper=add(Q(3),mul(sub(Q(3),k),div(J,sub(Q(111,53),J))));
  positive(sub(Q(111,106),add(S,b)),"core material domain");
  const coreGap=positive(sub(Q(123,10),coreUpper),"core curvature margin");
  if(cmp(mul(Q(2),S),add(add(wH,alpha),Q(1,100)))!==0)throw Error("sweep equality");
  const sineLo=x=>sub(x,div(pow(x,3),Q(6)));
  const heldLo=mul(sub(div(Q(433,250),k),Q(44,21)),sineLo(div(mul(k,alpha),Q(2))));
  const HLo=mul(div(Q(2),k),sineLo(div(mul(k,wH),Q(2))));
  const heldGap=positive(sub(heldLo,div(D,Q(10))),"held margin");
  const HGap=positive(sub(HLo,div(D,Q(5))),"H diameter margin");
  // Threefold convex perimeter 2*pi implies h_Gamma>=pi/(3*sqrt(3))>3/5.
  positive(sub(pow(Q(26,15),2),Q(3)),"sqrt3 upper witness");
  positive(sub(div(Q(333,106),mul(Q(3),Q(26,15))),Q(3,5)),"core support lower");
  positive(sub(Q(19),pow(Q(87,20),2)),"sqrt19 lower witness");
  const heightFactor=sub(one,div(pow(vu,2),mul(Q(8),pow(k,2))));
  const circleSupportLo=sub(mul(Q(3,5),Q(87,200)),mul(Q(9,10),mul(mul(rhi,L0),heightFactor)));
  const circleSupportGap=positive(sub(circleSupportLo,Q(87,1000)),"protected circle support margin");
  const postColumnSupport=Q(41,500),reachLo=Q(10,123);
  const supportFocusGap=positive(sub(postColumnSupport,reachLo),"full support to focus margin");
  const reachGap=positive(sub(reachLo,mul(Q(3,100),D)),"conditional reach ratio margin");
  return {
    status:"proved_by_exact_rational_arithmetic",
    scope:"new single-up-ramp m3 reference first up/down cycle only; no BVP, tail, exact C2/C3 solution or full surface inferred",
    delta_ref:repr(delta),r_interval:[repr(rlo),repr(rhi)],
    up_stages:[[0,"9/20",repr(L0)],["9/20","9/20",repr(coast)],["9/20",0,repr(L2)]],
    down_stages:[[0,"-1/2",repr(Ld)],["-1/2","-1/2",repr(Cd)],["-1/2",0,repr(Ld)]],
    up_area:repr(totalArea),up_length:repr(Tup),down_length:repr(Td),period:repr(add(Tup,Td)),
    core_curvature:repr(k),protected_halfwidth:repr(S),first_ramp_reference_peak_acceleration:repr(B),
    first_ramp_area:repr(A0),arcsine_lower_six_terms:repr(asinLo),
    characteristic_squared_lower:repr(chiSquaredLo),characteristic_square_margin:repr(chiGap),
    protected_curvature_squared_upper:repr(protectedCurvatureSquared),protected_curvature_square_margin:repr(curvatureGap),
    envelope_squared_radius:repr(radius2),n3_radius_factor_squared_upper:repr(K2),
    core_and_held_budget:{weighted_support_radius_upper:"2/3",
      halfwidth:repr(S),transition:repr(b),target_curvature:repr(k),phase_endpoint:repr(alpha),
      compensated_window_integral:repr(J),core_curvature_upper:repr(coreUpper),core_curvature_margin:coreGap,
      H_width:repr(wH),each_sweep_margin:"1/200",H_interval_offsets:["13/100","67/100"],
      H_diameter_lower:repr(HLo),H_absolute_margin:HGap,held_lower:repr(heldLo),held_absolute_margin:heldGap,
      D_upper:repr(D),H_ratio_lower:repr(div(HLo,D)),held_ratio_lower:repr(div(heldLo,D))},
    protected_circle_height_factor_upper:repr(heightFactor),
    protected_circle_support_lower:repr(circleSupportLo),protected_circle_support_margin:circleSupportGap,
    conditional_complete_geometry:{unmarked_uninserted_D_upper:"67/25",unmarked_support_lower:"87/1000",
      full_curvature_upper:"123/10",column_lengths:["1/200","1/100"],marker_D_cost_upper:"1/25000",
      final_D_upper:repr(D),post_column_support_lower:repr(postColumnSupport),
      reach_lower:repr(reachLo),support_focus_gap:supportFocusGap,reach_absolute_margin:reachGap,
      reach_ratio_lower:repr(div(reachLo,D)),all_full_surface_hypotheses_still_unpaid:true},
    boxes:count,minimum_Bernstein_gap:repr(min),
    relative_metric_1e6_envelope_gap:positive(sub(min,mul(Q(1,1000000),radius2)),"relative metric envelope gap"),
    pieces:summaries
  };
}
console.log(JSON.stringify(certificate(),null,2));
