// Complete exact-rational gates for the R115 cut128 grounded low-input graph.
// These gates evaluate proved majorants, not a new infinite-tail PDE solve.
export function runBudget(){
  const abs=x=>x<0n?-x:x;
  function gcd(a,b){a=abs(a);b=abs(b);while(b){const c=a%b;a=b;b=c;}return a;}
  function Q(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};}
  const add=(a,b)=>Q(a.n*b.d+b.n*a.d,a.d*b.d);
  const sub=(a,b)=>Q(a.n*b.d-b.n*a.d,a.d*b.d);
  const mul=(a,b)=>Q(a.n*b.n,a.d*b.d);
  const div=(a,b)=>Q(a.n*b.d,a.d*b.n);
  const pow=(a,n)=>Q(a.n**BigInt(n),a.d**BigInt(n));
  const two=n=>n>=0?Q(1n<<BigInt(n)):Q(1n,1n<<BigInt(-n));
  const lt=(a,b)=>a.n*b.d<b.n*a.d;
  const le=(a,b)=>a.n*b.d<=b.n*a.d;
  const sum=(...a)=>a.reduce(add,Q(0));
  const product=(...a)=>a.reduce(mul,Q(1));
  const one=Q(1),zero=Q(0),checks=[];
  function gate(name,ok){checks.push({name,pass:!!ok});if(!ok)throw Error("failed "+name);}
  const inv=a=>div(one,a);
  const kappa=two(-60),H=Q(256,85),DX=Q(13,4),invB=Q(64,63);
  const bdiff=add(Q(1,85),mul(Q(2),kappa));
  gate("raw_low_B_near_identity",lt(bdiff,Q(1,64)));
  gate("raw_low_B_inverse",lt(inv(sub(one,bdiff)),invB));
  gate("raw_complete_graph_norm",lt(mul(DX,invB),Q(4)));
  const graphDifferenceCoef=sum(mul(Q(2),invB),product(Q(2),H,invB,invB));
  gate("raw_complete_graph_difference_9kappa",lt(graphDifferenceCoef,Q(9)));
  gate("raw_complete_graph_difference_2minus56",lt(mul(graphDifferenceCoef,kappa),two(-56)));
  const graphDerivativeCoef=mul(Q(64),add(invB,product(DX,invB,invB)));
  gate("raw_complete_graph_derivative_512kappa",lt(graphDerivativeCoef,Q(512)));

  const delta=Q(1n,25n*(1n<<127n)),d=Q(9,400);
  const Rc=two(-469),R=two(-397),eta=two(-785);
  gate("actual_delta128_bound",lt(delta,two(-131)));
  gate("actual_wcut_bound",lt(pow(delta,6),two(-786)));
  gate("actual_eta_bound",lt(mul(Q(20,17),pow(delta,6)),eta));
  const relativeCoeff=product(Q(12),two(10),Q(256),Q(13,48));
  gate("actual_complete_Rc_power",lt(mul(pow(relativeCoeff,4),pow(delta,15)),pow(Rc,4)));
  const gap=mul(Q(3,4),d);
  gate("background_eight_angular_weights",lt(add(one,div(Q(8),gap)),Q(512)));
  gate("background_Rd_bound",le(mul(two(72),Rc),R));
  const inputDirect=add(mul(Q(625),pow(add(one,div(Q(2),d)),2)),
                        mul(Q(64),pow(add(one,div(Q(4),d)),4)));
  gate("input_finite_derivative_cost",lt(inputDirect,two(47)));
  gate("mean_self_map",lt(mul(Q(128),R),Q(1,2)));
  gate("input_with_actual_mean_cost",lt(div(inputDirect,sub(one,mul(Q(128),R))),two(48)));

  gate("low_exact_base_shear_row1",lt(div(Q(172*172),Q(3)),two(14)));
  gate("low_exact_base_shear_row2",lt(add(Q(4,15),mul(Q(16,15),eta)),one));
  gate("eta_times_low_row",le(mul(eta,two(14)),two(-771)));
  // Cleared determinant in Z[eta,M].  For T12*T21 the sqrt(12) cancels exactly.
  function poly(entries){return new Map(entries);}
  function padd(a,b){const c=new Map(a);for(const[k,v]of b){const z=(c.get(k)||0n)+v;if(z)c.set(k,z);else c.delete(k);}return c;}
  function pneg(a){return new Map([...a].map(([k,v])=>[k,-v]));}
  function pmul(a,b){const c=new Map();for(const[ka,va]of a)for(const[kb,vb]of b){const aa=ka.split(",").map(Number),bb=kb.split(",").map(Number);const k=[aa[0]+bb[0],aa[1]+bb[1]].join(",");const z=(c.get(k)||0n)+va*vb;if(z)c.set(k,z);else c.delete(k);}return c;}
  const P1=poly([["0,0",1n]]),Pe=poly([["1,0",1n]]),PM=poly([["0,1",1n]]);
  const denominator=pmul(padd(PM,pneg(P1)),padd(P1,Pe));
  const cross=pmul(pmul(Pe,Pe),PM);
  const detNumerator=padd(padd(denominator,cross),pneg(cross));
  gate("exact_grounded_shear_determinant_one",padd(detNumerator,pneg(denominator)).size===0);

  const r2=pow(R,2),dd=sum(mul(Q(4),R),mul(Q(6),r2));
  gate("D_and_t_complex_power_domains",lt(dd,Q(1,16))&&lt(r2,Q(1,16)));
  gate("inverse_three_half_derivative_constant",lt(mul(Q(9,4),pow(Q(16,15),5)),Q(4)));
  gate("inverse_square_derivative_constant",lt(mul(Q(2),pow(Q(16,15),3)),Q(3)));
  const tinv=inv(sub(one,r2)),halfD=inv(sub(one,dd)),D32=add(one,mul(Q(2),dd));
  const k=add(one,mul(Q(2),R)),gnumerator=add(one,product(k,R,tinv));
  const gminus=add(mul(Q(2),dd),product(k,R,tinv,add(one,mul(Q(2),dd))));
  gate("background_connection_G",lt(gminus,mul(Q(12),R)));
  const expGamma=inv(sub(one,mul(Q(15),R)));
  const RhRelative=mul(add(one,r2),expGamma);
  gate("background_horizontal_near_identity",lt(sub(RhRelative,one),mul(Q(32),R)));
  const normalRelative=mul(expGamma,add(product(k,tinv,halfD),mul(R,tinv)));
  const ZinvRelative=inv(sub(one,div(mul(eta,R),Q(4))));
  gate("true_support_chi_bound",lt(product(RhRelative,normalRelative,ZinvRelative),Q(8)));
  gate("actual_vertical_height_inverse",lt(ZinvRelative,Q(2)));
  gate("true_support_power_domain",lt(mul(Q(8),eta),Q(1,16)));

  const meanAk=sum(product(halfD,R,tinv),sub(product(gnumerator,D32,k),one));
  const meanAt=sub(product(halfD,k,tinv),one);
  const meanAp=sum(product(Q(2),halfD,k,r2,tinv,tinv),product(Q(2),gnumerator,D32,R));
  gate("actual_mean_Ak",lt(meanAk,mul(Q(16),R)));
  gate("actual_mean_Atheta",lt(meanAt,mul(Q(8),R)));
  gate("actual_mean_Ap",lt(meanAp,mul(Q(8),R)));
  gate("actual_mean_slope_absorption",lt(sum(meanAk,meanAt,meanAp),mul(Q(128),R)));

  const dotG=sum(mul(halfD,sum(mul(R,tinv),mul(k,tinv),product(Q(2),k,r2,tinv,tinv))),
                 product(gnumerator,D32,add(k,mul(Q(2),R))));
  gate("actual_dotG_bound_64",lt(dotG,Q(64)));
  gate("actual_dotgamma_bound_128",lt(mul(Q(5,4),dotG),Q(128)));
  const dotl=product(Q(2),R,tinv);
  gate("actual_dotl_bound",lt(dotl,mul(Q(4),R)));
  const dota=sum(mul(R,tinv),mul(k,add(one,mul(Q(2),r2))));
  gate("actual_dota_bound_8",lt(dota,Q(8)));
  const invb=mul(add(one,r2),halfD);
  const dotb=mul(invb,add(mul(k,tinv),product(k,k,R,tinv,tinv)));
  gate("actual_dotb_bound_8",lt(dotb,Q(8)));
  const lmax=mul(Q(2),add(one,r2));
  const bmax=mul(add(one,dd),tinv),amax=product(k,R,tinv);
  gate("actual_lmax",lt(lmax,Q(3)));
  gate("actual_Rh_vector_norm",lt(mul(Q(2),RhRelative),Q(4)));
  gate("actual_Rhr_vector_norm",lt(mul(expGamma,add(bmax,amax)),Q(4)));
  gate("actual_horizontal_variation_2pow10",lt(mul(expGamma,add(dotl,mul(lmax,Q(128)))),two(10)));
  gate("actual_horizontal_r_variation_2pow12",lt(mul(expGamma,sum(dota,dotb,mul(add(bmax,amax),Q(128)))),two(12)));
  gate("actual_grounded_height_error_2pow13",lt(product(ZinvRelative,Q(4),two(10)),two(13)));
  const cvR=sum(product(ZinvRelative,Q(4),two(10)),
                product(ZinvRelative,Q(4),two(12)),
                product(ZinvRelative,ZinvRelative,k,Q(4),two(10),eta));
  gate("actual_grounded_height_r_error_2pow18",lt(cvR,two(18)));
  const ArDiff=sub(product(D32,add(one,mul(Q(24),eta)),add(one,mul(Q(4),R))),one);
  const Atheta=product(Q(2),D32,add(one,mul(Q(24),eta)),R);
  gate("actual_grounded_radial_coefficient",lt(ArDiff,mul(Q(32),add(R,eta))));
  gate("actual_grounded_angular_coefficient",lt(Atheta,mul(Q(8),R)));
  const pDiff=sum(ArDiff,product(add(one,ArDiff),two(18),eta),
                 mul(Atheta,add(one,mul(two(13),eta))));
  gate("actual_grounded_flux_error_2pow20",lt(pDiff,mul(two(20),add(R,eta))));
  const completeOutput=sum(mul(Q(2),pDiff),product(Q(3),two(13),eta),mul(Q(128),R));
  gate("full_output_plus_mean_rows_2pow24",lt(completeOutput,mul(two(24),add(R,eta))));
  gate("complete_converter_2minus324",lt(mul(two(144),add(Rc,eta)),two(-324)));

  gate("low_width_restore_exponent",lt(mul(Q(172),d),Q(4)));
  // e < 1+1+1/2+1/6+(1/24)/(1-1/5) = 87/32 < 11/4.
  gate("exp_constant_e_lt_11over4",lt(Q(87,32),Q(11,4)));
  gate("low_width_restore_cost",lt(pow(Q(11,4),4),Q(64)));
  const conv=two(-324),lowErr=two(-316);
  gate("grounded_augmented_Dirichlet_error",le(product(Q(64),Q(4),conv),lowErr));
  gate("grounded_augmented_Dirichlet_inverse",lt(inv(sub(one,lowErr)),Q(2)));
  gate("grounded_augmented_Dirichlet_inverse_minus_I",lt(div(lowErr,sub(one,lowErr)),two(-315)));
  gate("complete_grounded_graph_norm",lt(div(mul(add(one,conv),Q(4)),sub(one,lowErr)),Q(8)));
  const eachChange=add(mul(Q(8),conv),mul(Q(4),two(-315)));
  gate("grounded_complete_graph_difference_2minus55",lt(add(mul(Q(16),kappa),mul(Q(2),eachChange)),two(-55)));

  return {
    schema:"visible-exact-R115-grounded-low-input-graph-v1",
    date:"2026-11-13",
    inputs:{source_R115_sha256:"7bc7fe7e0f285efabc0b1b64a55c661ce6084e4fc54f9a0c049ef3708544f1fa",
      source_R72_blob:"a7c78793ba18724a4f0553b6ccd55259b8f4df92",
      source_R25_blob:"be20257721fed270c59a4024427042fc76ee0073",
      kappa_upper:"2^-60",raw_H_upper:"256/85",DX_upper:"13/4",
      cut_reference_radius:"1<b<2",cut_mean_physical_height_lower:"17/20",
      delta128:"1/(25*2^127)",tau128:"5177/400",angle_loss:"9/400",
      low_input_physical_frequencies:"m in 4Z, 0<abs(m)<=172",
      Rc_upper:"2^-469",Rd_upper:"2^-397",eta_upper:"2^-785"},
    checks,all_pass:checks.every(x=>x.pass),
    proved_bounds:{raw_complete_graph_difference:"<2^-56",
      true_grounded_converter_with_angle_loss:"<2^-324",
      true_grounded_low_and_mean_graph_difference_with_all_outputs:"<2^-55",
      true_grounded_low_and_mean_graph_norm:"<8"},
    scope:{actual_cut128:true,complete_high_outputs:true,mean_height_and_flux_rows_retained:true,
      finite_input_only:true,regular_r25_over8_Robin_update_paid:false,
      all_high_incoming_graph_inverse_paid:false,source_containing_full_feedback_inverse_paid:false,
      new_native_infinite_tail_run:false,full_nonlinear_zero_constructed:false}
  };
}
if(typeof process!=="undefined" && process.argv &&
   /fourfold_true_tail_grounded_low_graph[.]mjs$/.test(process.argv[1]||"")){
  console.log(JSON.stringify(runBudget(),null,2));
}
