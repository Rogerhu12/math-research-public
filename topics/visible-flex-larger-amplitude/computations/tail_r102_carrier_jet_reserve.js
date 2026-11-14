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


// Exact additional five-jet reserve of the already executed R102 eight-part budget.
// This does not compute the old->PA->CF bridge; it specifies a nonzero sufficient
// target for that independent calculation. All true-field and mean-domain
// hypotheses remain explicit. Author: tail_refinement, GPT-6 Astra Pro, AI-assisted.
function deriveR102BridgeReserve(r95Text, r102Text) {
 const assert=(v,m)=>{if(!v)throw Error(m);};
 const hashes={r95:sha256(r95Text),r102:sha256(r102Text)};
 assert(hashes.r95==="690d9eaeb61311aaf15e47416534020ba04e2391ecde6012ccbaab50cd45559d","R95 text identity");
 assert(hashes.r102==="d01b7310f9d76fa5d5d56f44805c67fedf7be776a78435803943edcda424bc6f","R102 text identity");
 const A=JSON.parse(r95Text),B=JSON.parse(r102Text);
 assert(Object.values(A.gates).every(x=>x===true)&&Object.values(B.gates).every(x=>x===true),"Incomplete prior gates");
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
 class Q {
  constructor(n,d=1n){n=BigInt(n);d=BigInt(d);assert(d!==0n,"Zero denominator");if(d<0n){n=-n;d=-d;}let g=gcd(n,d);this.n=n/g;this.d=d/g;}
  add(x){return new Q(this.n*x.d+x.n*this.d,this.d*x.d);}
  sub(x){return new Q(this.n*x.d-x.n*this.d,this.d*x.d);}
  mul(x){return new Q(this.n*x.n,this.d*x.d);}
  div(x){return new Q(this.n*x.d,this.d*x.n);}
  sq(){return new Q(this.n*this.n,this.d*this.d);}
  cmp(x){const v=this.n*x.d-x.n*this.d;return v<0n?-1:v>0n?1:0;}
 }
 const q=(n,d=1)=>new Q(n,d),rec=x=>new Q(x.numerator,x.denominator);
 const dy=x=>x[1]>=0?new Q(BigInt(x[0])*(1n<<BigInt(x[1]))):new Q(x[0],1n<<BigInt(-x[1]));
 const max=(a,b)=>a.cmp(b)>=0?a:b,one=q(1),zero=q(0);
 const floor=(n,d)=>n>=0n?n/d:-((-n+d-1n)/d),ceil=(n,d)=>-floor(-n,d);
 const dec=n=>{const sign=n<0n?"-":"",u=(n<0n?-n:n).toString().padStart(19,"0");return sign+u.slice(0,-18)+"."+u.slice(-18);};
 const out=x=>({lo:[floor(x.n*(1n<<64n),x.d).toString(),-64],
  hi:[ceil(x.n*(1n<<64n),x.d).toString(),-64],
  decimal_lower_18:dec(floor(x.n*10n**18n,x.d)),decimal_upper_18:dec(ceil(x.n*10n**18n,x.d))});
 const w=q(3,25),r=q(1,20),E=q(634,625),S=q(1259,1250),Cg=q(15108,15625),target=q(33,4),eps=q(1,512),dH=q(1,20);
 const reserveFamilies=[
  {name:"uniform_five_physical_jets",components:[q(1,65536),q(1,65536),q(1,65536),q(1,65536),q(1,65536)]},
  {name:"nonuniform_physical_units",components:[q(1,32768),q(1,1048576),q(1,512),q(1,16384),q(1,524288)]}
 ];
 const results=reserveFamilies.map(family=>{
  const [er,et,err,ert,ett]=family.components;
  const parts=A.original_formal_shape_operator.map((base,j)=>{
   const b=B.chosen[j];assert(base.part===j&&b.part===j&&b.conditional_target_passed,"Part identity");
   // Outward saved R102 outputs already cover the full true error epsilon.
   const meanC=dy(b.mean_coefficient_upper),dr=dy(b.physical_radial_gradient_difference_upper),
      de=dy(b.physical_angular_gradient_difference_upper),phi=dy(b.delta_Phi_upper);
   const dbase=rec(base.gradient_bounds.radial).add(dr);
   const ebase=rec(base.gradient_bounds.angular_over_r).add(de);
   const A_base=rec(base.Hessian_entry_bounds.A).add(phi).add(Cg.mul(dr)).add(dH);
   const B_base=rec(base.Hessian_entry_bounds.B).add(w.div(r).mul(q(4,3)).mul(eps));
   const C_base=rec(base.Hessian_entry_bounds.C).add(w.div(r).mul(q(4,3).add(meanC)).mul(eps));
   const gradient=dBase=>{
    const d=dbase.add(dBase),e=ebase.add(et.div(r));
    return q(2).mul(w).mul(d).add(d.sq()).add(E.mul(e.sq()));
   };
   const omega=gradient(er);
   const Aa=A_base.add(err).add(Cg.mul(er));
   const Bb=B_base.add(ert.div(r)).add(et.div(r.sq()));
   const Cc=C_base.add(ett.div(r.sq())).add(er.div(r));
   assert(omega.cmp(one)<0,"Projection positivity");
   const cap=target.mul(one.sub(omega)).sub(q(8)).div(S).sub(Bb);
   const slackA=cap.sub(Aa),slackC=cap.sub(Cc);
   const K=q(8).add(S.mul(max(Aa,Cc).add(Bb))).div(one.sub(omega));
   const pass=slackA.cmp(zero)>0&&slackC.cmp(zero)>0&&K.cmp(target)<0;
   return {part:j,panels:base.panels,curvature_upper:out(K),A_hessian_slack:out(slackA),
    C_hessian_slack:out(slackC),projection_error_upper:out(omega),passed:pass};
  });
  return {name:family.name,component_order:["h_r","h_theta","h_rr","h_rtheta","h_thetatheta"],
   components:family.components.map(x=>x.n.toString()+"/"+x.d.toString()),parts,
   all_eight_parts_passed:parts.every(p=>p.passed)};
 });
 const gates={exact_input_text_hashes:true,all_original_parts_retained:true,
  R102_saved_positive_bounds_used_outward:true,
  uniform_nonzero_five_jet_bridge_passed:results[0].all_eight_parts_passed,
  nonuniform_nonzero_five_jet_bridge_passed:results[1].all_eight_parts_passed};
 assert(Object.values(gates).every(x=>x===true),"One bridge reserve failed");
 return {schema:"r102-actual-five-jet-bridge-reserve-v1",
  author:"tail_refinement (GPT-6 Astra Pro, AI-assisted)",date:"2026-11-13",input_hashes:hashes,
  field_difference_total:"1/512",new_candidate_physical_defect_budget:"1/20",results,gates,
  hypotheses:{
   original_reference_is_the_R95_R48_candidate:true,
   new_candidate_has_its_own_actual_derivatives_and_complete_mean:true,
   normalized_nonmean_A1_error_old_to_new_plus_new_to_true_at_most_1over512:true,
   all_fields_use_the_R102_same_real_g_and_adjacent_complete_mean_branch:true,
   bridge_five_jet_errors_must_be_paid_from_actual_old_and_new_candidate_derivatives:true,
   new_candidate_full_physical_J_over_L_defect_must_be_paid:true,
   complete_true_Darboux_field_existence_is_external:true},
  scope:{bridge_was_computed:false,true_field_error_was_paid:false,
   complete_mean_height_constant_not_bounded_by_this_curvature_calculation:true,
   no_actual_normal_or_reach_or_full_time_claim:true,
   same_radius_source_angle_physical_polar_derivatives:true},
  execution:{engine:"functions.exec V8",exact_BigInt_only:true,
   input_binary_primary_reads:0,new_Arb_ODE_Node_integrals:0,operating_system_exitcode:null}};
}
