function sha256(text) {
  const bytes=[];
  for(const ch of text){const c=ch.codePointAt(0);if(c<128)bytes.push(c);else if(c<2048)bytes.push(192|(c>>>6),128|(c&63));else if(c<65536)bytes.push(224|(c>>>12),128|((c>>>6)&63),128|(c&63));else bytes.push(240|(c>>>18),128|((c>>>12)&63),128|((c>>>6)&63),128|(c&63));}
  const bitLength=bytes.length*8;
  bytes.push(128);while(bytes.length%64!==56)bytes.push(0);
  const hi=Math.floor(bitLength/4294967296),lo=bitLength>>>0;
  for(let j=3;j>=0;j--)bytes.push((hi>>>(8*j))&255);
  for(let j=3;j>=0;j--)bytes.push((lo>>>(8*j))&255);
  const h=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
  const k=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
  const ro=(v,n)=>(v>>>n)|(v<<(32-n));
  for(let off=0;off<bytes.length;off+=64){
    const w=new Array(64);
    for(let j=0;j<16;j++)w[j]=((bytes[off+4*j]<<24)|(bytes[off+4*j+1]<<16)|(bytes[off+4*j+2]<<8)|bytes[off+4*j+3])>>>0;
    for(let j=16;j<64;j++){const x=w[j-15],y=w[j-2];w[j]=(w[j-16]+(ro(x,7)^ro(x,18)^(x>>>3))+w[j-7]+(ro(y,17)^ro(y,19)^(y>>>10)))>>>0;}
    let [a,b,c,d,e,f,g,hh]=h;
    for(let j=0;j<64;j++){const t1=(hh+(ro(e,6)^ro(e,11)^ro(e,25))+((e&f)^((~e)&g))+k[j]+w[j])>>>0;const t2=((ro(a,2)^ro(a,13)^ro(a,22))+((a&b)^(a&c)^(b&c)))>>>0;hh=g;g=f;f=e;e=(d+t1)>>>0;d=c;c=b;b=a;a=(t1+t2)>>>0;}
    [a,b,c,d,e,f,g,hh].forEach((v,j)=>{h[j]=(h[j]+v)>>>0;});
  }
  return h.map(x=>x.toString(16).padStart(8,"0")).join("");
}

// Exact finite consumer for the published complete cell0/seg7 candidate.
// Plain JavaScript BigInt only: no Node API, floating acceptance, ODE or source evaluation.
// The caller must bind the exact input hashes and store the output.
// Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.


// R102: exact arithmetic consumer of the already published R95 text ledger.
// Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
// No binary input, source evaluation, Node/Arb process, ODE, or new integral.
function deriveR102Budget(ledgerText, summaryText) {
  const assert=(v,m)=>{if(!v)throw Error(m);};
  const hashes={r95:sha256(ledgerText),summary:sha256(summaryText)};
  assert(hashes.r95==="690d9eaeb61311aaf15e47416534020ba04e2391ecde6012ccbaab50cd45559d","R95 text hash mismatch");
  assert(hashes.summary==="806fdb96b9aa6eafd921c07518a5b52218180d2182f7b8d18abb8e3d695638e4","Original summary hash mismatch");
  const R=JSON.parse(ledgerText),S=JSON.parse(summaryText);
  assert(R.exact_bigint_arithmetic_only===true&&R.original_formal_shape_operator.length===8,"Wrong R95 ledger");
  assert(Object.values(R.gates).every(x=>x===true),"R95 input gate missing");
  assert(S.cell===0&&S.segment===7&&S.phase==="formal-complete","Wrong original application");
  assert(S.total_accepted_panels===1740&&S.parts.reduce((a,p)=>a+p.panels,0)===1740,"Incomplete original 1740 leaves");
  assert(S.parts.every((p,j)=>p.part===j&&p.complete_source_cover===true),"Wrong eight part coverage");
  assert(S.same_exact_candidate_and_background===true&&S.complete_mean_and_its_actual_derivative_retained===true,"Candidate/mean identity lost");
  assert(Object.values(S.gates).every(x=>x===true),"Continuous source gate missing");
  assert(R.input_hashes.original===hashes.summary,"R95 original identity differs");
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
  class F {
    constructor(n,d=1n){n=BigInt(n);d=BigInt(d);assert(d!==0n,"Zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
    add(x){return new F(this.n*x.d+x.n*this.d,this.d*x.d);}
    sub(x){return new F(this.n*x.d-x.n*this.d,this.d*x.d);}
    mul(x){return new F(this.n*x.n,this.d*x.d);}
    div(x){return new F(this.n*x.d,this.d*x.n);}
    pow(n){return new F(this.n**BigInt(n),this.d**BigInt(n));}
    cmp(x){const a=this.n*x.d-x.n*this.d;return a<0n?-1:a>0n?1:0;}
  }
  const q=(n,d=1)=>new F(n,d),zero=q(0),one=q(1),two=q(2),three=q(3);
  const min=(a,b)=>a.cmp(b)<=0?a:b,max=(a,b)=>a.cmp(b)>=0?a:b;
  const fromRecord=x=>new F(x.numerator,x.denominator);
  const dyadic=x=>{const e=x.binary_exponent;assert(Number.isInteger(e),"Nonintegral dyadic exponent");
    return e>=0?new F(BigInt(x.mantissa)<<BigInt(e)):new F(x.mantissa,1n<<BigInt(-e));};
  const upper=(p,key)=>{const x=dyadic(p.bounds[key].value.upper);assert(x.cmp(zero)>=0,"Negative norm");return x;};
  const floor=(a,b)=>a>=0n?a/b:-((-a+b-1n)/b);
  const ceil=(a,b)=>-floor(-a,b);
  const show=n=>{const s=n<0n?"-":"",u=(n<0n?-n:n).toString().padStart(19,"0");return s+u.slice(0,-18)+"."+u.slice(-18);};
  function record(x,bits=64){
    const den=1n<<BigInt(bits);
    return {lower:{mantissa:floor(x.n*den,x.d).toString(),binary_exponent:-bits},
      upper:{mantissa:ceil(x.n*den,x.d).toString(),binary_exponent:-bits},
      decimal_lower_18:show(floor(x.n*10n**18n,x.d)),decimal_upper_18:show(ceil(x.n*10n**18n,x.d))};
  }
  function exact(x){return {numerator:x.n.toString(),denominator:x.d.toString()};}
  function strictDyadicBelow(x,bits=40){
    let n=floor(x.n*(1n<<BigInt(bits)),x.d);
    const result=()=>new F(n,1n<<BigInt(bits));
    if(result().cmp(x)>=0)n-=1n;
    return result();
  }
  const w=q(3,25),r=q(1,20),z=w.pow(2),E=one.add(z),sqrtE=one.add(z.div(two)),bg=q(8),target=q(33,4);
  const connection=bg.mul(w).mul(sqrtE),wr=bg.mul(E).mul(sqrtE);
  assert(fromRecord(R.parameters.w_upper).cmp(w)===0&&fromRecord(R.parameters.r_lower).cmp(r)===0,"Background guard differs");
  const bases=S.parts.map((p,j)=>{
    const c=upper(p,"complete_mean_abs"),Rn=upper(p,"R_tau"),Tn=upper(p,"P_theta_W1"),Un=upper(p,"K_theta_minus_P_W1");
    const p0=Rn.div(three),k0=c.add(Rn.div(three)),t0=Tn.div(three),u0=Un.div(three);
    const d0=w.mul(k0),e0=w.mul(p0);
    const A0=upper(p,"signed_actual_nonmean_Hrr_l1").add(upper(p,"mean_physical_hrr_minus_background_abs")).add(connection.mul(d0));
    const B0=w.div(r).mul(u0),C0=w.div(r).mul(k0.add(t0));
    const old=R.original_formal_shape_operator[j];
    for(const [name,x,y] of [["d0",d0,old.gradient_bounds.radial],["e0",e0,old.gradient_bounds.angular_over_r],
      ["A0",A0,old.Hessian_entry_bounds.A],["B0",B0,old.Hessian_entry_bounds.B],["C0",C0,old.Hessian_entry_bounds.C]]){
      assert(x.cmp(fromRecord(y))===0,"R95 baseline mismatch "+j+" "+name);
    }
    const coarse=upper(p,"physical_nonmean_second_source_W1").div(three).add(upper(p,"mean_physical_hrr_minus_background_abs"));
    return {part:j,panels:p.panels,c,p0,k0,t0,u0,d0,e0,A0,B0,C0,coarse};
  });
  function calc(b,eps,dH){
    // The complete mean root is allowed in chat +/- eps before applying R99.
    const p=b.p0.add(eps.div(three)),k=b.k0.add(eps.mul(q(4,3))),t=b.t0.add(eps),u=b.u0.add(eps.mul(q(4,3)));
    const vD=z.mul(two.mul(k).add(k.pow(2)).add(E.mul(p.pow(2))));
    const a=one.sub(z.mul(p.pow(2))),d=one.sub(vD),l=one.sub(k).sub(E.mul(t)),y=one.sub(k);
    assert(a.cmp(zero)>0&&d.cmp(zero)>0&&l.cmp(zero)>0&&y.cmp(zero)>0,"Requested real domain failed");
    const orient=one.sub(z.mul(one.add(k)).mul(t).div(a));
    assert(orient.cmp(zero)>0,"Mean numerator branch failed");
    const CK=k.add(E.mul(t)).div(d.pow(2)).add(q(3,2).mul(vD).div(d.pow(3)));
    const CT=k.add(z.mul(p.pow(2))).div(a.mul(d)).add(vD.div(two.mul(d.pow(2))));
    const CP=E.mul(p).mul(one.add(z.mul(one.add(k)).mul(t).div(a))).div(d.pow(2))
      .add(two.mul(z).mul(p).mul(one.add(k)).mul(t).div(a.pow(2).mul(d)));
    const mscale=E.pow(2).div(l),aK=mscale.mul(CK),aP=mscale.mul(CP),aT=mscale.mul(CT);
    const meanCoefficient=aK.add(aP).div(three).add(aT);
    const meanGate=meanCoefficient.cmp(one)<0;
    const eK=eps.div(three),eP=eK,eT=eps,eTh=eps;
    const ec=meanCoefficient.mul(eps),deltaK=eK.add(ec);
    const N=wr.mul(one.add(z.mul(one.add(k).mul(t).add(p.pow(2))))).add(E.mul(w).div(r).mul(u.pow(2)));
    const FK=wr.mul(z).mul(t).div(l).add(N.div(l.pow(2)));
    const FTh=two.mul(E).mul(w).mul(u).div(r.mul(l));
    const FP=two.mul(wr).mul(z).mul(p).div(l).add(FTh);
    const FT=wr.mul(z).mul(one.add(k)).div(l).add(E.mul(N).div(l.pow(2)));
    const phi=FK.mul(deltaK).add(FP.mul(eP)).add(FT.mul(eT)).add(FTh.mul(eTh));
    const dr=w.mul(deltaK),angular=w.mul(eP);
    // Keep common r in h_theta/r etc. Do not first box h_theta with r_upper.
    const dgrad=b.d0.add(dr),egrad=b.e0.add(angular);
    const Awithout=b.A0.add(phi).add(connection.mul(dr));
    const B=b.B0.add(w.div(r).mul(eTh.add(eP)));
    const C=b.C0.add(w.div(r).mul(eT.add(deltaK)));
    const projection=two.mul(w).mul(dgrad).add(dgrad.pow(2)).add(E.mul(egrad.pow(2)));
    const projectionGate=projection.cmp(one)<0;
    const cap=target.mul(one.sub(projection)).sub(bg).div(sqrtE).sub(B);
    const strictHcap=cap.sub(Awithout), Cgate=C.cmp(cap)<0;
    const A=Awithout.add(dH),lambda=max(A,C).add(B);
    const curvature=bg.add(sqrtE.mul(lambda)).div(one.sub(projection));
    return {meanGate,projectionGate,Cgate,strictHcap,curvature,meanCoefficient,ec,phi,dr,angular,
      a,d,l,y,orient,projection,Awithout,B,C,FK,FP,FT,FTh,aK,aP,aT,
      targetPassed:meanGate&&projectionGate&&Cgate&&dH.cmp(strictHcap)<0&&curvature.cmp(target)<0};
  }
  const epsilons=[q(0),q(1,4096),q(1,2048),q(1,1024),q(1,512),q(1,256),q(1,128)];
  const grid=bases.map(b=>({part:b.part,panels:b.panels,coarse_existing_physical_defect_upper:record(b.coarse),
    rows:epsilons.map(eps=>{
      const a=calc(b,eps,zero),safe=strictDyadicBelow(a.strictHcap);
      const safeNonnegative=safe.cmp(zero)>=0;
      const checked=safeNonnegative?calc(b,eps,safe):null;
      return {epsilon:exact(eps),mean_root_continuation_gate:a.meanGate,mean_difference_coefficient:record(a.meanCoefficient),
        real_domain_lowers:{A:record(a.a),D:record(a.d),L:record(a.l),y:record(a.y),N:record(a.orient)},
        projection_error_upper:record(a.projection),C_hessian_gate:a.Cgate,
        admissible_dH_open_upper:record(a.strictHcap),
        certified_closed_dH_budget:safeNonnegative?exact(safe):null,
        closed_budget_target_passed:checked?.targetPassed??false,
        curvature_at_closed_budget:checked?record(checked.curvature):null};
    })}));
  const chosenEps=q(1,512),chosenH=q(1,20);
  const chosen=bases.map(b=>{const c=calc(b,chosenEps,chosenH),old=calc(b,chosenEps,b.coarse);
    return {part:b.part,panels:b.panels,mean_coefficient:record(c.meanCoefficient),
      conditional_curvature_upper:record(c.curvature),conditional_target_passed:c.targetPassed,
      strict_available_dH:record(c.strictHcap),existing_coarse_defect:record(b.coarse),
      existing_coarse_defect_curvature_upper:record(old.curvature),existing_coarse_defect_budget_passed:old.targetPassed,
      complete_mean_difference_upper:record(c.ec),delta_Phi_upper:record(c.phi),
      physical_radial_gradient_difference_upper:record(c.dr),
      physical_angular_gradient_difference_upper:record(c.angular),
      matrix_row_hrr:{K:record(c.FK.mul(one.add(c.aK))),P:record(c.FP.add(c.FK.mul(c.aP))),T:record(c.FT.add(c.FK.mul(c.aT))),Ktheta:record(c.FTh)}};});
  const gates={
    exact_input_text_hashes:true,original_1740_continuous_leaves_and_eight_parts:true,
    baseline_R95_d_e_A_B_C_reproduced_exactly:true,complete_mean_root_and_true_branch_retained:true,
    all_grid_mean_continuation_domains: grid.every(g=>g.rows.every(r=>r.mean_root_continuation_gate)),
    chosen_nonzero_joint_epsilon_and_nonzero_dH_pass_all_eight:chosen.every(r=>r.conditional_target_passed),
    exactly_seven_existing_coarse_dH_bounds_fit_chosen_epsilon:chosen.filter(r=>r.existing_coarse_defect_budget_passed).length===7,
    existing_coarse_dH_failure_is_only_part0:chosen.every(r=>r.part===0?!r.existing_coarse_defect_budget_passed:r.existing_coarse_defect_budget_passed)
  };
  // The last two are observed finite-data assertions, not prerequisites for truth of R99.
  assert(Object.values(gates).every(x=>x===true),"One declared R102 data gate failed");
  return {schema:"r102-seg7-exact-joint-field-and-physical-defect-budget-v1",
    author:"tail_refinement (GPT-6 Astra Pro, AI-assisted)",date:"2026-11-12",
    input_hashes:hashes,input_paths:{
      r95:"notes/2026-11-12-tail-r95-seg7-curvature-budget.json",
      summary:"notes/2026-11-12-tail-outer-cell0-seg7-span2-centeredJ-r2.json"},
    parameters:{w_upper:exact(w),r_lower:exact(r),E_upper:exact(E),sqrt_E_upper:exact(sqrtE),
      abs_w_r_upper_from_background_K8:exact(wr),connection_upper:exact(connection),target_curvature:exact(target),
      chosen_joint_A1_nonmean_field_epsilon:exact(chosenEps),chosen_physical_defect_dH:exact(chosenH),
      mean_box_radius_equals_epsilon:true,record_dyadic_bits:64,closed_boundary_dyadic_bits:40},
    grid,chosen,
    scope:{same_original_R48_candidate:true,full_mean_root:true,complete_frequency_errors_required:true,
      real_true_Darboux_solution_is_an_external_hypothesis:true,actual_field_error_has_not_been_paid:true,
      candidate_physical_defect_has_not_been_lowered:true,carrier_candidate_is_not_substituted:true,
      part0_finer_per_leaf_physical_defect_still_requires_local_original_gzip:true,
      curvature_failure_or_nonexistence_not_claimed:true,whole_tail_or_full_time_geometry_not_claimed:true},
    computation:{exact_BigInt_rational_arithmetic:true,decimal_displays_not_used_for_gates:true,
      algebraic_output_rounding_outwards:true,binary_primary_reads:0,new_Arb_ODE_Node_integrals:0,
      runtime:"functions.exec V8; no operating-system job or process exit status"},
    gates};
}


function compactR102Result(full) {
  const pair=x=>[x.mantissa,x.binary_exponent];
  const bounds=x=>({lo:pair(x.lower),hi:pair(x.upper)});
  const fraction=x=>x.denominator==="1"?x.numerator:x.numerator+"/"+x.denominator;
  const grid=full.grid.map(p=>({part:p.part,panels:p.panels,
    coarse_existing_physical_defect_upper:pair(p.coarse_existing_physical_defect_upper.upper),
    rows:p.rows.map(r=>({
      epsilon:fraction(r.epsilon),
      mean_root_continuation_gate:r.mean_root_continuation_gate,
      mean_difference_coefficient_upper:pair(r.mean_difference_coefficient.upper),
      real_domain_lowers:Object.fromEntries(Object.entries(r.real_domain_lowers).map(([k,v])=>[k,pair(v.lower)])),
      projection_error_upper:pair(r.projection_error_upper.upper),
      C_hessian_gate:r.C_hessian_gate,
      admissible_dH_open_upper_enclosure:bounds(r.admissible_dH_open_upper),
      certified_closed_dH_budget:r.certified_closed_dH_budget?fraction(r.certified_closed_dH_budget):null,
      closed_budget_target_passed:r.closed_budget_target_passed,
      curvature_at_closed_budget_upper:r.curvature_at_closed_budget?pair(r.curvature_at_closed_budget.upper):null
    }))}));
  const chosen=full.chosen.map(p=>({part:p.part,panels:p.panels,
    mean_coefficient_upper:pair(p.mean_coefficient.upper),
    conditional_curvature_upper:pair(p.conditional_curvature_upper.upper),
    conditional_curvature_decimal_upper:p.conditional_curvature_upper.decimal_upper_18,
    conditional_target_passed:p.conditional_target_passed,
    strict_available_dH_enclosure:bounds(p.strict_available_dH),
    strict_available_dH_decimal_lower:p.strict_available_dH.decimal_lower_18,
    existing_coarse_defect_upper:pair(p.existing_coarse_defect.upper),
    existing_coarse_defect_decimal_upper:p.existing_coarse_defect.decimal_upper_18,
    existing_coarse_defect_curvature_upper:pair(p.existing_coarse_defect_curvature_upper.upper),
    existing_coarse_defect_budget_passed:p.existing_coarse_defect_budget_passed,
    complete_mean_difference_upper:pair(p.complete_mean_difference_upper.upper),
    delta_Phi_upper:pair(p.delta_Phi_upper.upper),
    physical_radial_gradient_difference_upper:pair(p.physical_radial_gradient_difference_upper.upper),
    physical_angular_gradient_difference_upper:pair(p.physical_angular_gradient_difference_upper.upper),
    matrix_row_hrr:Object.fromEntries(Object.entries(p.matrix_row_hrr).map(([k,v])=>[k,pair(v.upper)]))
  }));
  return {...full,grid,chosen,
    serialization:{pair_semantics:"[signed integer mantissa as decimal text, binary exponent] is an ordinary exact dyadic rational",
      outward_bounds:"Lower endpoints round downward; upper endpoints upward to multiples of 2^-64; no display value is used for any gate",
      closed_boundary:"Strictly smaller than the exact open boundary, on the grid 2^-40",
      compact_plain_text_json:true,no_binary_primary_is_contained:true}};
}
function runR102Budget(ledgerText, summaryText) {
  return compactR102Result(deriveR102Budget(ledgerText, summaryText));
}
