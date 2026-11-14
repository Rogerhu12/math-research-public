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
function deriveSeg7Curvature(raw) {
  const input={original:JSON.parse(raw.original),resource:JSON.parse(raw.resource),
    background:JSON.parse(raw.background),original_sha256:sha256(raw.original),
    resource_sha256:sha256(raw.resource),background_sha256:sha256(raw.background)};
  const assert=(condition,message)=>{if(!condition)throw Error(message);};
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
  class F {
    constructor(n,d=1n){n=BigInt(n);d=BigInt(d);assert(d!==0n,"Zero denominator");
      if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
    add(x){return new F(this.n*x.d+x.n*this.d,this.d*x.d);}
    sub(x){return new F(this.n*x.d-x.n*this.d,this.d*x.d);}
    mul(x){return new F(this.n*x.n,this.d*x.d);}
    div(x){return new F(this.n*x.d,this.d*x.n);}
    pow(n){return new F(this.n**BigInt(n),this.d**BigInt(n));}
    cmp(x){const a=this.n*x.d-x.n*this.d;return a<0n?-1:a>0n?1:0;}
    rec(){const k=10n**18n,a=this.n*k,b=this.d;
      const upper=a>=0n?(a+b-1n)/b:a/b;
      const lower=a>=0n?a/b:-((-a+b-1n)/b);
      const show=n=>{const sign=n<0n?"-":"",u=(n<0n?-n:n).toString().padStart(19,"0");
        return sign+u.slice(0,-18)+"."+u.slice(-18);};
      return {numerator:this.n.toString(),denominator:this.d.toString(),
        decimal_lower_18:show(lower),decimal_upper_18:show(upper)};}
  }
  const q=(n,d=1)=>new F(n,d),zero=q(0),one=q(1),two=q(2),three=q(3);
  const max=(a,b)=>a.cmp(b)>=0?a:b;
  const dyadic=value=>{const m=BigInt(value.mantissa),e=value.binary_exponent;
    assert(Number.isInteger(e),"Noninteger exponent");
    return e>=0?new F(m*(2n**BigInt(e))):new F(m,2n**BigInt(-e));};
  const upper=(part,key)=>{const v=dyadic(part.bounds[key].value.upper);
    assert(v.cmp(zero)>=0,"Negative norm");return v;};
  const parse=s=>{const a=s.split("/");return new F(a[0],a.length===1?"1":a[1]);};
  const original=input.original,resource=input.resource,background=input.background;
  assert(input.original_sha256==="806fdb96b9aa6eafd921c07518a5b52218180d2182f7b8d18abb8e3d695638e4","Wrong original hash");
  assert(input.resource_sha256==="912ad6200027fdb445cd3e8636c1f6cd404a3480d2c013b6c4722e6888016820","Wrong resource hash");
  assert(input.background_sha256==="27e9cac085dd4913cdf14526fec847613bede8fae5367ae72cc143f25b254083","Wrong background hash");
  assert(resource.exitcode===0&&resource.termination_signal===null,"Original audit did not formally pass");
  assert(original.cell===0&&original.segment===7&&original.phase==="formal-complete","Wrong complete application");
  assert(Object.values(original.gates).every(v=>v===true),"Missing original continuous gate");
  assert(original.parts.length===8&&original.parts.every((p,j)=>p.part===j&&p.complete_source_cover),"Missing full part");
  assert(original.parts.reduce((s,p)=>s+p.panels,0)===1740,"Missing continuous leaves");
  assert(JSON.stringify(original.modes)===JSON.stringify(Array.from({length:20},(_,j)=>2*j+2)),"Mode set differs");
  assert(parse(original.tau).cmp(zero)>=0,"A nonnegative angular width is required");
  assert(original.source_hashes["tail_outer_general_mean_bounds.py"]==="4b16b860eb89d7b8f19d7f8ff05642ea0122b0a2016d4be623d5483430023a5c","Different mean/norm source");
  assert(original.source_hashes["tail_outer_substage_span_refinement.py"]==="85bf30e818e7ab92107a5f5a537225afb9273877327bf6e0092b303b01a1b5d8","Different same-mode Hrr source");
  assert(background.real_background_curvature_paid===true&&background.all_cells_background_curvature_bound===8,"Background curvature unpaid");
  const ready="notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json";
  assert(original.input_hashes[ready]===background.input_hashes[ready],"Different actual real source");
  const w=q(3,25),r=q(1,20),E=one.add(w.pow(2)),sqrtE=one.add(w.pow(2).div(two));
  assert(dyadic(background.outer_cell0.segment7_complete_log_blend_slope_upper.upper).cmp(w)<0,"Wrong segment7 cap");
  assert(parse(background.outer_cell0.node12_radius_lower.exact).cmp(r)>0,"Actual radius lower failed");
  const backgroundK=q(8),target=q(33,4),eta=q(1,8192);
  const connection=backgroundK.mul(w).mul(sqrtE);
  function calculate(part,error){
    const c=upper(part,"complete_mean_abs"),R=upper(part,"R_tau"),
      T=upper(part,"P_theta_W1"),U=upper(part,"K_theta_minus_P_W1"),
      Hrr=upper(part,"signed_actual_nonmean_Hrr_l1"),
      meanHrr=upper(part,"mean_physical_hrr_minus_background_abs");
    const Kbound=R.div(three),Pbound=R.div(three),Tbound=T.div(three),Ubound=U.div(three);
    const d0=w.mul(c.add(Kbound)),e0=w.mul(Pbound);
    const A0=Hrr.add(meanHrr).add(connection.mul(d0));
    const B0=w.div(r).mul(Ubound);
    const C0=w.div(r).mul(c.add(Kbound).add(Tbound));
    const d=d0.add(error),e=e0.add(error.div(r));
    const A=A0.add(one.add(connection).mul(error));
    const BCextra=error.mul(one.add(one.div(r))).div(r);
    const B=B0.add(BCextra),C=C0.add(BCextra);
    const epsilon=two.mul(w).mul(d).add(d.pow(2)).add(E.mul(e.pow(2)));
    assert(epsilon.cmp(one)<0,"Positive projection lost");
    const Lambda=max(A,C).add(B);
    const curvature=backgroundK.add(sqrtE.mul(Lambda)).div(one.sub(epsilon));
    return {part:part.part,panels:part.panels,
      derivative_error: error.rec(),gradient_bounds:{radial:d.rec(),angular_over_r:e.rec()},
      Hessian_entry_bounds:{A:A.rec(),B:B.rec(),C:C.rec()},
      epsilon_upper:epsilon.rec(),matrix_operator_upper:Lambda.rec(),
      formal_or_conditional_curvature_upper:curvature.rec(),
      normal_vertical_squared_lower:one.sub(epsilon).div(E).rec(),
      target:target.rec(),margin:target.sub(curvature).rec(),target_passed:curvature.cmp(target)<0};
  }
  const formal=original.parts.map(part=>calculate(part,zero));
  const conditional=original.parts.map(part=>calculate(part,eta));
  const fromRec=a=>new F(a.numerator,a.denominator);
  const maximum=rows=>rows.reduce((a,b)=>fromRec(a.formal_or_conditional_curvature_upper).cmp(fromRec(b.formal_or_conditional_curvature_upper))>=0?a:b);
  const gates={
    original_formal_exit0:true,complete_eight_parts_1740_true_leaves:true,
    full_twenty_modes_and_complete_mean:true,actual_same_mode_Hrr_not_PDE_substitution:true,
    W1_to_real_l1_divisor_three_from_minimum_mode_two:true,
    identical_real_background_ready:true,background_K8_w3over25_r1over20_paid:true,
    full_original_formal_matrix_below_33over4:formal.every(x=>x.target_passed),
    actual_solution_with_stated_derivative_error_below_33over4:conditional.every(x=>x.target_passed)
  };
  assert(Object.values(gates).every(x=>x===true),"One exact budget gate failed");
  return {schema:"r95-exact-seg7-existing-candidate-curvature-budget-v1",
    author:"tail_refinement (GPT-6 Astra Pro, AI-assisted)",date:"2026-11-12",
    input_hashes:{original:input.original_sha256,resource:input.resource_sha256,background:input.background_sha256},
    parameters:{w_upper:w.rec(),r_lower:r.rec(),E_upper:E.rec(),sqrt_E_upper:sqrtE.rec(),
      background_curvature:backgroundK.rec(),connection_upper:connection.rec(),
      minimum_mode:2,real_l1_divisor:3,uniform_physical_polar_derivative_error:eta.rec()},
    original_formal_shape_operator:formal,conditional_actual_shape_operator:conditional,
    maxima:{original:maximum(formal),conditional:maximum(conditional)},
    complete_mean_included:true,background_E_equals_1_plus_w_squared_is_real_function_identity:true,
    exact_bigint_arithmetic_only:true,new_Arb_ODE_Node_source_integrals:false,
    candidate_isometry_or_existence_claimed:false,true_solution_error_currently_paid:false,
    actual_full_tail_curvature_certificate:false,full_time_geometry_claimed:false,gates};
}
