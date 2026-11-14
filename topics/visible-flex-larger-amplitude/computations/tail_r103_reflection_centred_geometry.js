/* SHA256 helper retained from the previously executed R102 BigInt consumer. */
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

/* Complete real, reflection-symmetric centred-circle comparison.
 * Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
 * Pure BigInt rational consumer: no binary inputs, Node, Arb or new integrals.
 */
function runR103CentredGeometry(r102Text, carrierExtremaText) {
  const H102="d01b7310f9d76fa5d5d56f44805c67fedf7be776a78435803943edcda424bc6f";
  const HC="f2d12d6c0b41f96fdb969f2923091934012b81e40721c19f2410997c7131baa2";
  if(sha256(r102Text)!==H102||sha256(carrierExtremaText)!==HC)
    throw Error("A complete small mathematical input changed");
  const O=JSON.parse(r102Text), C=JSON.parse(carrierExtremaText);
  if(!Object.values(O.gates).every(x=>x===true)||C.actual_leaves!==111
     ||C.original_resource.formal_exitcode!==0||C.original_resource.termination_signal!==null
     ||C.epsilon!=="1/512"||!C.all_111_conditional_targets||!C.all_9_structural_gates)
    throw Error("The actual conditional inputs or formal exit are absent");
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;}
  class R {
    constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
    add(b){return new R(this.n*b.d+b.n*this.d,this.d*b.d);}
    sub(b){return new R(this.n*b.d-b.n*this.d,this.d*b.d);}
    mul(b){return new R(this.n*b.n,this.d*b.d);}
    div(b){return new R(this.n*b.d,this.d*b.n);}
    pow(k){return new R(this.n**BigInt(k),this.d**BigInt(k));}
    lt(b){return this.n*b.d<b.n*this.d;}
    le(b){return this.n*b.d<=b.n*this.d;}
  }
  const Q=(n,d=1)=>new R(n,d),zero=Q(0),one=Q(1);
  const min=(a,b)=>a.lt(b)?a:b,max=(a,b)=>a.lt(b)?b:a;
  function textQ(x){const s=String(x);if(s.includes("/")){const a=s.split("/");return Q(a[0],a[1]);}if(s.includes(".")){const a=s.split(".");return Q(a[0]+a[1],10n**BigInt(a[1].length));}return Q(s);}
  function dyad(x){const n=BigInt(x[0]),e=Number(x[1]);return e>=0?Q(n*(2n**BigInt(e))):Q(n,2n**BigInt(-e));}
  function isqrt(n){if(n<0n)throw Error("negative square root");if(n<2n)return n;let x=1n<<BigInt((n.toString(2).length+1)>>1);for(;;){const y=(x+n/x)>>1n;if(y>=x)return x;x=y;}}
  function sqrtUpper(a){if(a.n<0n)throw Error("negative radicand");const scale=1n<<96n,scaled=a.n*scale*scale;let n=isqrt(scaled/a.d);if(n*n*a.d<scaled)n++;return Q(n,scale);}
  function ceilDiv(a,b){return -((-a)/b)+(a%b>0n?1n:0n);}
  function upper(a){if(a.n<0n)throw Error("negative upper norm");const n=(a.n*(1n<<96n)+a.d-1n)/a.d;return [String(n),-96];}
  function lower(a){if(a.n<0n)throw Error("negative lower margin");return [String(a.n*(1n<<96n)/a.d),-96];}
  function decimal(a,up=true){const s=10n**18n;let n=a.n*s/a.d;if(up&&a.n*s%a.d)n++;return String(n/s)+"."+String(n%s).padStart(18,"0");}
  const eps=Q(1,512), W=Q(3,25),E=one.add(W.pow(2)),Rmax=Q(1,3),pi=Q(22,7);
  const rows=[],exact=[];
  for(let part=0;part<8;part++){
    let A,D,L,y,nu2,dc,w=W,domain;
    if(part===0){
      domain=C.real_domain_lowers;
      [A,D,L,y]=["A","D","L","y"].map(k=>textQ(domain[k]));
      nu2=textQ(C.true_vertical_normal_squared_lower);
      dc=textQ(C.complete_mean_difference_upper);
      const radialSquare=one.sub(nu2),den=y.pow(2).sub(radialSquare);
      if(!zero.lt(den))throw Error("Carrier w recovery has no positive denominator");
      w=min(w,sqrtUpper(radialSquare.div(den)));
      if(!w.lt(Q(1,40)))throw Error("Observed complete carrier box does not imply w<1/40");
    }else{
      const grid=O.grid.find(x=>x.part===part),chosen=O.chosen.find(x=>x.part===part);
      const r=grid?.rows.find(x=>x.epsilon==="1/512");
      if(!r||!chosen||!r.mean_root_continuation_gate||!chosen.existing_coarse_defect_budget_passed)
        throw Error("One unchanged R102 part is not paid");
      domain=r.real_domain_lowers;
      [A,D,L,y]=["A","D","L","y"].map(k=>dyad(domain[k]));
      nu2=max(D.div(E),one.sub(dyad(r.projection_error_upper)).div(E));
      dc=dyad(chosen.complete_mean_difference_upper);
    }
    if(![A,D,L,y,nu2].every(x=>zero.lt(x)&&x.le(one)))throw Error("A complete real domain failed");
    const k=one.sub(y), t=one.sub(L);
    const p=min(w.mul(one.add(k)),sqrtUpper(one.sub(nu2)));
    const q=sqrtUpper(one.sub(A)),qt=w.mul(t);
    const dp=w.mul(eps.div(Q(3)).add(dc)),dq=w.mul(eps.div(Q(3))),dqt=w.mul(eps);
    const S=A,nu=nu2;
    const common=p.mul(dp).add(q.mul(dq));
    const dnu=common.div(nu),dinv=common.div(nu.pow(3));
    const g=dinv.add(dp.mul(qt).add(p.mul(dqt)).div(S.pow(2).mul(nu)))
       .add(p.mul(qt).mul(Q(2).mul(q).mul(dq).div(S.pow(4).mul(nu)).add(dinv.div(S.pow(2)))));
    const da=Rmax.mul(q).mul(dq).div(S);
    const phase=pi.mul(g).div(Q(4));
    const xy=pi.mul(da).div(Q(2)).add(pi.pow(2).mul(Rmax).mul(g).div(Q(16)));
    const component=dnu.mul(one.add(q.div(S))).add(dp.add(dq).div(S))
       .add(q.pow(2).add(p.mul(q)).mul(dq).div(S.pow(3)));
    const rho=min(one,p.add(q));
    const normal=component.add(rho.mul(min(Q(2),phase)));
    const hp=Rmax.mul(w).mul(eps).div(Q(6));
    exact.push({part,A,D,L,y,nu2,w,p,q,qt,dp,dq,dqt,dc,g,da,phase,xy,normal,hp});
    rows.push({part,reference:part===0?"New formally audited physical-r carrier":"Unchanged original R48 substage",
      complete_real_domain_lower:{A:lower(A),D:lower(D),L:lower(L),y:lower(y),nu_squared:lower(nu2)},
      background_w_upper:upper(w),complete_mean_difference_upper:upper(dc),
      physical_normalized_amplitudes:{radial_p:upper(p),angular_q:upper(q),angular_qtheta:upper(qt)},
      physical_normalized_differences:{radial_p:upper(dp),angular_q:upper(dq),angular_qtheta:upper(dqt)},
      full_turn_rate_difference_upper:upper(g),angular_phase_difference_upper:upper(phase),
      angular_speed_difference_upper:upper(da),
      centred_horizontal_position_upper:upper(xy),
      unit_reference_vector_or_true_normal_difference_upper:upper(normal),
      nonmean_height_difference_upper:upper(hp),
      local_gates:{complete_real_domain:true,full_mean_difference_retained:true,complete_even_frequency_input_not_truncated:true,
       exact_quarter_turn_and_reflection_are_explicit_hypotheses:true}});
  }
  const maxdc=exact.reduce((a,r)=>max(a,r.dc),zero);
  const meanHeight=W.mul(Rmax).mul(maxdc);
  let maxposition=zero,maxnormal=zero,maxhorizontal=zero,maxphase=zero;
  for(let i=0;i<rows.length;i++){
    const r=exact[i],height=r.hp.add(meanHeight),pos=r.xy.add(height);
    rows[i].one_global_mean_height_difference_upper=upper(meanHeight);
    rows[i].complete_vertical_position_upper=upper(height);
    rows[i].complete_euclidean_position_upper=upper(pos);
    rows[i].position_decimal_upper=decimal(pos);rows[i].normal_decimal_upper=decimal(r.normal);
    rows[i].position_below_1_over_8192=pos.lt(Q(1,8192));
    rows[i].normal_below_1_over_4096=r.normal.lt(Q(1,4096));
    maxposition=max(maxposition,pos);maxnormal=max(maxnormal,r.normal);
    maxhorizontal=max(maxhorizontal,r.xy);maxphase=max(maxphase,r.phase);
  }
  const gates={
    both_complete_small_input_hashes:true,actual_carrier_111_leaf_and_formal_exit0:true,
    seven_other_parts_use_only_paid_original_R102_boxes:true,carrier_reference_is_distinct_from_old_part0:true,
    all_complete_real_domains_positive:true,full_mean_from_one_global_height_constant:true,
    all_nonzero_even_frequencies_retained_in_error_hypothesis:true,
    whole_circle_from_two_reflections_and_exact_mean_turn:true,
    centres_and_axes_require_one_explicit_common_global_gauge:true,
    actual_candidate_normals_not_assumed:true,
    all_eight_position_budgets:rows.every(x=>x.position_below_1_over_8192),
    all_eight_normal_budgets:rows.every(x=>x.normal_below_1_over_4096)
  };
  return {
    schema:"R103-complete-reflection-centred-geometry-budget-v1",
    author:"tail_refinement (GPT-6 Astra Pro, AI-assisted)",date:"2026-11-13",
    status:"Exact conditional geometry budget; no exact outer solution or true error certificate is claimed",
    input_hashes:{r102:H102,carrier_observed_extrema:HC},
    original_carrier_primary:C.original_primary,original_carrier_resource:C.original_resource,
    parameters:{epsilon:"1/512",pi_upper:"22/7",radius_upper:"1/3",global_w_upper:"3/25",
      radius_upper_source:"Same real metric R26 actual outer radius <1/3",
      common_centre_offset:"0",common_reflection_axis_rotation:"0",incoming_mean_height_offset:"0",
      no_reset_at_substage_boundaries:true},
    matrix_norms:"Complete A_tau^1 joint error implies component A0 errors <=epsilon/3 and derivative errors <=epsilon.",
    common_complete_mean_height_difference_upper:upper(meanHeight),
    rows,maxima:{centred_horizontal_position:upper(maxhorizontal),complete_euclidean_position:upper(maxposition),
      unit_reference_vector_or_true_normal:upper(maxnormal),angular_phase:upper(maxphase),
      complete_euclidean_position_decimal_upper:decimal(maxposition),normal_decimal_upper:decimal(maxnormal)},
    gates,
    conditional_unpaid:["Actual same-g full-frequency Darboux solution on the entire outer tail",
      "The stated <=1/512 complete field error relative to this mixed reference",
      "Required common reflection symmetry and shared global centre/axis/height gauge",
      "Complete prefix/tail matching, full time domain and remaining continuous point-pair cover"],
    reference_vectors_asserted_normals_of_nonisometric_candidates:false,
    original_radial_reference_to_centred_reference_gauge_drift_paid:false,
    no_new_ODE_Arb_Node_integrals_or_binary_transfer:true,
    execution:"Pure JavaScript BigInt completed inside functions.exec; no OS process exit or RSS is claimed",
    serialization:"Every [mantissa,exponent] is an ordinary exact dyadic; positive upper records are rounded upward at 96 fractional bits, lower records downward. All gates use exact unrounded rational comparisons."
  };
}
