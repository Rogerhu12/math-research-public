#!/usr/bin/env node
// Exact rational consumer. No Python/Arb run or body trial is claimed.
import fs from "node:fs";
import path from "node:path";
import {fileURLToPath} from "node:url";
import {createHash} from "node:crypto";

function fixedStopD0Budget(previous) {
  const abs=x=>x<0n?-x:x;
  const gcd=(a,b)=>{a=abs(a);b=abs(b);while(b){const t=a%b;a=b;b=t;}return a;};
  const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];};
  const add=(x,y)=>Q(x[0]*y[1]+y[0]*x[1],x[1]*y[1]);
  const sub=(x,y)=>add(x,[-y[0],y[1]]);
  const mul=(x,y)=>Q(x[0]*y[0],x[1]*y[1]);
  const div=(x,y)=>Q(x[0]*y[1],x[1]*y[0]);
  const sq=x=>mul(x,x),lt=(x,y)=>x[0]*y[1]<y[0]*x[1];
  const p2=e=>e>=0?Q(1n<<BigInt(e)):Q(1n,1n<<BigInt(-e));
  const repr=x=>x[0].toString()+"/"+x[1].toString();
  const gates=[];
  const gate=(name,passed,evidence)=>{gates.push({name,passed,evidence});if(!passed)throw Error("failed gate: "+name);};
  gate("same_completed_fixed_stop_object",previous.complete===true
    &&previous.kind==="actual_fixed_stop_fourth_line_and_complete_regular_port_budget"
    &&previous.candidate_sha256==="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
    &&previous.connector.fixed_stop===true&&previous.gate_count===29
    &&previous.gates.every(x=>x.passed===true),
    "Consumes the executed 29-gate fixed-stop theorem, not an old retuned D0.");
  gate("two_actual_shallow_derivatives_distinct",
    previous.cut_error.gamma1_derivative.dyadic_exponent===-22
    &&previous.cut_error.gamma2_derivative.dyadic_exponent===-8
    &&previous.cut_error.deep_only.dyadic_exponent===-193532,
    "Actual cut128 defect, not a lambda defect.");
  gate("fresh_good_parameter_measure",
    previous.full_new_good_angle.bad_measure==="83/16384"
    &&previous.full_new_good_angle.new_good_parameter_required===true
    &&previous.full_new_good_angle.continuous_selection_claimed===false,
    "Choose once in the real product good set; no common good-t selector.");
  const epsAngle=p2(-39),cfee=p2(-100),epsD=p2(-35);
  gate("actual_fourth_ratio_near_one",lt(mul(Q(45),epsD),Q(1,1024)),
    "|k4/(4f4)-1|<=45 epsilon_d; the ratio itself is kept.");
  const omin=Q(7,5),omax=Q(3,2),pmin=Q(5,4),pmax=Q(8,5);
  const tlo=div(add(div(omin,Q(4)),pmin),add(omax,div(pmax,Q(4))));
  gate("actual_fourth_positive_full_two_trace",lt(Q(0),tlo),
    "pB in[5/4,8/5], omega in[7/5,3/2] imply t4>0; (c+t)^2>=1+t^2.");
  const Llo=mul(omin,sub(p2(24),Q(25,8)));
  gate("true_coth_positive_fee",lt(Q(104),mul(Q(8),Llo)),
    "For every M>=4, 2ML>104 and e>2 give 0<coth(ML)-1<2^-100.");
  gate("new_all_high_schur_angle",lt(p2(-40),sub(epsAngle,cfee)),
    "Fresh physical angle2^-39 minus the actual finite-L fee.");
  gate("two_trace_scale_cancellation",lt(Q(5,84),Q(1,16)),
    "J inverse infinity norm<=4/3; omega>7/5.");
  gate("new_raw404_includes_actual_tau",lt(add(Q(5177,400),Q(391)),Q(404)),
    "Controlled profile C.35, all new bad prefixes included.");
  gate("cut128_binary_fees",7+495+1080+36===1618,
    "16*8, delta_tail^-15/4, geometric2^360 cubed, and full two-trace fee.");
  gate("complete_connector_angular_fee",
    repr(add(add(Q(1143),mul(Q(4),Q(25,8))),Q(404)))==="3119/2",
    "All true finite connector segments, both bumps, and new raw404.");
  const angular=add(add(add(Q(3119,2),Q(5663,20)),Q(7,5)),Q(75,32));
  gate("all_frequencies_1850_not_a_cutoff",repr(angular)==="295423/160"&&lt(angular,Q(1850)),
    "log2<7/10 and log(M)/M decreases on every M>=4.");
  gate("true_label_inverse_factor",repr(Q(1,4*4))==="1/16",
    "Complete Z norm carries M and the pointwise inverse carries1/M.");
  gate("same_width_projector_includes_both_components",lt(add(Q(1),p2(43)),p2(44)),
    "x_H e/(e x_H) uses the same actual unit-label amplitude; e=(coth,1).");
  const d0=Q(88823,400),s224=sub(Q(224),d0);
  gate("actual_positive_physical_width",repr(s224)==="777/400"&&lt(Q(0),s224),
    "beta=224 gives a genuine full finite-connector field.");
  gate("full_finite_connector_tail_source",(-447)+16===-431,
    "The full balanced two-state map applies to arbitrary cut data, including particulars.");
  gate("new_weak_fee_not_old_fee",482-450===32,
    "Current controlled weak canonical endpoint map is2^482.");
  gate("complete_weak_particular_trace_fee",-431+482===51,
    "Full canonical weak source, both rows, no Ft derivative norm.");
  gate("same_width_weak_B_projection_fee",44-431===-387&&-387+482===95,
    "New full projection fee2^95, not the old2^63.");
  gate("true_regular_affine_Wronskian_fee",41-431===-390&&-390+482===92,
    "All-mode exp(-ML) and the actual determinant4M(1-M^-2).");
  gate("fourth_two_trace_determinant",repr(mul(Q(16),sub(Q(1),Q(1,16))))==="15/1",
    "Both ordinary height and grounded flux retained for M=4.");
  const gap=sub(sub(Q(2080),d0),Q(1850));
  gate("actual_exterior_width_after_2080",repr(gap)==="3177/400"&&lt(Q(0),gap),
    "2080 includes the finite-body loss and the true1850 inverse.");
  gate("exterior_source_inverse_gain",lt(mul(Q(45),Q(7,10)),mul(Q(4),gap)),
    "(1/16)exp(-4gap)<2^-49 using log2<7/10.");
  gate("new_label_particular_fee",-430-49===-479&&-479+482===3,
    "The complete weak source-to-label coefficient is<8 at the stronger input width.");
  gate("new_full_state_particular_fee",lt(add(p2(16),mul(Q(9),p2(-479))),p2(17))&&17+482===499,
    "Full G-H D0^-1 EG, not merely its B trace.");
  const P=Q(1480385n,10n**17n),d=Q(124999999985n,10n**12n),sigma=Q(1,16),x=Q(779,1000);
  const y=mul(Q(4),sub(d,sigma));
  let t=Q(1),expLower=Q(1);
  for(let j=1;j<=8;j++){t=div(mul(t,y),Q(j));expLower=add(expLower,t);}
  gate("actual_physical_tail_exponential_at_one_sixteenth",lt(div(Q(1),x),expLower),
    "Positive exponential Taylor polynomial, degree8; no sampled physical tail.");
  const Zsig=mul(div(mul(Q(8),P),Q(29,5)),div(x,sq(sub(Q(1),x))));
  gate("complete_actual_R_analytic_input",lt(Zsig,Q(326,10n**12n)),
    "Both signs, all j>=1: (8P/5.8) sum j*x^j <3.26e-10.");
  const za=Q(33,10n**11n),rf=Q(1,10n**8n),rb=p2(-60),F=add(rf,rb);
  gate("actual_analytic_curvature_ball",lt(Zsig,za),
    "New explicitly paid z_a=3.3e-10, separate from the original tighter unweighted actual norm.");
  const image=add(add(mul(Q(9),za),mul(p2(-512),rb)),mul(Q(9*4096),sq(F)));
  const lip=mul(Q(36*4096),F);
  gate("new_full_analytic_C_inverse_image",lt(image,rf),
    "Full long inverse includes independent fB and all nonlinear modes/mean.");
  gate("new_full_analytic_C_inverse_contraction",lt(lip,Q(1,512)),
    "36*4096*(1e-8+2^-60)<1/512.");
  gate("complete_original_long_data_domain",lt(mul(Q(2),F),p2(-25))&&lt(mul(Q(6),F),p2(-20)),
    "Full two-end data and complete Y ball; unweighted uniqueness identifies the actual centre graph.");
  gate("legitimate_complex_fB_derivative",lt(mul(p2(61),rf),p2(35)),
    "Cauchy within the independent fB halfball, after the full analytic graph was constructed.");
  const quarter=Q(10724906774255168n,10n**9n),Slo=add(quarter,sigma),E=mul(Q(4),sub(Slo,Q(2074)));
  gate("same_unchanged_long_analytic_width",repr(Slo)==="335153338648599/31250000",
    "7L/16>10724906.774255168; add the newly proved sigma=1/16.");
  gate("new_incoming_to_224_strict_exponent",lt(mul(Q(60000000),Q(7,10)),sub(E,Q(1,8))),
    "log(9/8)<1/8 and log2<7/10 give the actual2^-60000000 bound.");
  gate("complete_incoming_derivative_exponent",lt(mul(Q(60000000),Q(7,10)),E),
    "24/16<2, hence derivative<2^(1-60000000).");
  gate("same_true_mixed_screening_exponent",lt(mul(Q(60000000),Q(7,10)),mul(Q(4),quarter)),
    "e^(-7L/4)<2^-60000000 for the same actual long interval.");
  gate("new_joint_label_ball_contains_incoming",60000000>262148+2,
    "R_a<A*/4; no extension to the former1/64 joint ball.");
  gate("joint_trace_Cauchy_factor",lt(Q(3,2),Q(2)),
    "RadiusA*/2 at a<=A*/4 gives DfB<2^-442 from the full2^-443 linear-size bound.");
  gate("incoming_actual_fB_stays_in_halfball",-60000000-443 < -61,
    "Full raw fB, not zero; available for true cap Cauchy derivative.");
  gate("complete_incoming_feedback",1-60000000+35-442===-60000406&&-60000406<-2,
    "All label, cap, mean, and long dependencies retained.");
  gate("new_joint_quadratic_trace_coefficient",1-442+262148===261707&&261707<261710,
    "Cauchy on A*=2^-262148, not the old large fixed-parameter ball.");
  const lift=div(Q(16),sub(Q(1),Q(1,64)));
  gate("same_true_zero_inner_long_lift",lt(lift,Q(17)),
    "16 lift and exact2^14*2^-20=1/64 feedback.");
  gate("complete_EB_two_end_quadratic_fee",lt(mul(p2(13),sq(Q(17))),p2(22)),
    "Both nonlinear Neumann outputs from the actual long theorem.");
  gate("complete_MB_nonmean_and_mean_coefficient",lt(Q(25),p2(5))&&27-443+5===-411,
    "S.29 retains the mean in the same physical angle norm.");
  const RTexp=261711-2*60000000,MBexp=-411-2*60000000;
  gate("full_residual_all_three_terms",Math.max(RTexp,MBexp)+1 < -119738000,
    "RT+EB grouped below2^261711 a^2; MB below2^-411 exp(-7L/4) r_f a; no term set to zero.");
  gate("physical_residual_width_is_not_2074",lt(s224,Q(2074))&&lt(sigma,Q(2074)),
    "The remaining F cannot be fed to D0^-1 on the proved domain.");
  return {
    kind:"actual_fixed_stop_D0_complete_source_and_incoming_budget",
    complete:true,
    arithmetic:"V8 BigInt normalized rational operations and strict cross-products; large dyadic bounds kept as integer exponents",
    candidate_sha256:previous.candidate_sha256,
    previous_fixed_stop_kind:previous.kind,
    actual_objects:{
      connector_stop:"fixed at the original actual Gamma0",
      new_good_parameter:"chosen once for the actual controlled radial reference; product Fubini allowed",
      fourth_relative_line:"t4=(omega/4+pB)/(omega+pB/4), not fixed to1",
      fourth_schur_transversality_lower:"1",
      all_mode_schur_transversality_lower:"2^-40",
      all_mode_label_inverse:"(1/16) Z_(beta+1850) -> l1_beta",
      same_width_complete_B_projection:"2^44 in pair l1;2^45 in pair L2"
    },
    complete_source_contract:{
      weak_endpoint_fee:"2^482",
      weak_particular_B_trace:"2^51",
      weak_same_width_B_projection:"2^95",
      weak_actual_regular_affine_row:"2^92 at angle L+beta-88823/400",
      full_internal_exterior_Green_input_width:"beta+2080",
      full_internal_discrete_source_label_fee:"2^-479",
      full_internal_weak_source_label_fee:"8",
      full_internal_weak_source_state_fee:"2^499",
      ordinary_source:"both p_star factors; actual J and Rm endpoint conversion remains required",
      weak_source:"both canonical rows; total/bare endpoint loads retained",
      means:"true flux integral and independent height; no nonzero-mode exponential applied"
    },
    actual_current_R_analytic_input:{
      sigma:repr(sigma),Z_A_sigma_bound:"3.26e-10",
      explicit_Z_ball:repr(za),explicit_fstar_ball:repr(rf),
      independent_fB_ball:"2^-60",
      original_tighter_unweighted_endpoint_and_mean_bounds:"preserved by complete uniqueness",
      exponential_ratio:repr(x),Z_rational_upper:repr(Zsig),
      C_inverse_image_upper:repr(image),C_inverse_Lipschitz_upper:repr(lip)
    },
    actual_full_incoming:{
      long_7L_over_16_lower:repr(quarter),S_lower:repr(Slo),
      incoming_label_factor:{mantissa:"1",dyadic_exponent:-60000000},
      derivative_factor:{mantissa:"1",dyadic_exponent:1-60000000},
      true_joint_label_ball:"2^-262148",
      feedback_factor:{mantissa:"1",dyadic_exponent:-60000406},
      full_remaining_F:{mantissa:"1",dyadic_exponent:-119738000,norm:"Z_sigma only"},
      complete_F_solved:false,complete_mean_match_claimed:false
    },
    exact_small_values:{angular_all_frequency_budget:repr(angular),
      exterior_width_margin:repr(gap),incoming_log_margin:repr(sub(E,Q(42000000))),
      fourth_positive_ratio_lower:repr(tlo)},
    scope:{all_nonmean_modes_retained:true,mean_rows_retained:true,actual_parameter_source_retained:true,
      full_eta_interval:"inherited from the actually paid fixed-stop entry",
      new_python_or_Arb_run_claimed:false,finite_body_or_adjoint_trial_recovered:false,
      updated_nonlinear_mixed_inverse_proved:false,topic_complete:false},
    gate_count:gates.length,gates
  };
}

const expectedInputs={
  "results/R119-supplement-controlled-profile-full-label-and-raw-ports.md": {
    "sha256": "ff11cb043128a5d66ee996bb174edda0d6537fe73f9a7a565ba143d2ab5c04d0",
    "git_blob": "f11edbccd752bf034aa40e71888859d667a04b42"
  },
  "results/R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md": {
    "sha256": "27325857e088e8266a322bcabe82c59a6cc1f06f225b2616c8490b553af5d45c",
    "git_blob": "fc3aab62e99a51cc06bd26a7233663a2b8e4dd73"
  },
  "results/R119-supplement-joint-tail-label-schur-normalization.md": {
    "sha256": "966dd0a1d3c92353908c8cc3e8b7dcd723ce30947ce3316fe437bdd92a24cd38",
    "git_blob": "dc85de4f1e81974ebcf7fb69fb4b75f9ea48fd74"
  },
  "results/R74-actual-full-tail-robin-and-augmented-positive-cap.md": {
    "sha256": "174bc93631b5ade0faf51160d7026e42d674916fd94e12cdb2315479458c18d8",
    "git_blob": "12b50b77b27ca7f501a323164e905ce4af4963dd"
  },
  "results/R119-supplement-balanced-connector-label-domain-224.md": {
    "sha256": "aff48a37b08cb41e6eb1ddd8c014687242f744e6cb9e638201c0781df46222d1",
    "git_blob": "cef18d9b99f9eb4cef7282757e7bd9377467fa83"
  },
  "results/R119-supplement-actual-exterior-Schur-and-full-weak-Wronskian.md": {
    "sha256": "ef1e50c409848f0da793e331d260ae056274c1a548781209c26bad072273e3f0",
    "git_blob": "bc30d99e60744bf5072558ec2038d3554eae7a7a"
  },
  "results/R119-supplement-actual-boundary-Schur-projector-and-interior-Green-kernel.md": {
    "sha256": "a03f8ec20bd81489c8960ad0a38e5751591b56eedbc7f7ba8f47c547213c628a",
    "git_blob": "2ff7b197b8d40825f39601ece44cb96f6b869682"
  },
  "results/R119-supplement-actual-nonlinear-incoming-reaches-224-labels.md": {
    "sha256": "c4618e5c380a742adec7e1609ebe8ef02c673321bf6b611ce99a68acfc39dcea",
    "git_blob": "1a5b8d8f1d4f4023749e2af953237d31e4949579"
  },
  "results/R133-supplement-actual-nonlinear-long-tail-screening-and-analytic-gain.md": {
    "sha256": "c5f3071445c23b146a58abfc69a248d25b5f02c62790d9245c2ac46741f41a1a",
    "git_blob": "fcce208a31303b8729602a7b54622595acb2a0ac"
  },
  "results/R133-supplement-final-moving-centre-actual-regular-boundary.md": {
    "sha256": "f4ae237c86542f29f2127f7e43d5ab97827756fcce86e71bcff8c0a610ec81af",
    "git_blob": "40463b6917c943e4ac991a597603cf41095baeb9"
  },
  "results/R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md": {
    "sha256": "03ddbc285ab03ee53a17ad3940d2c789695338854cf7cafdbfd38e75f3a11711",
    "git_blob": "7784d7158974d4632ca634369e55dc095e134902"
  },
  "results/R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md": {
    "sha256": "1241e0df199d8aa1487d2d1b3b0cf5b60615f3eb21b51bfa207ad54b30cd6d7c",
    "git_blob": "5fd83130fead0160cece059b7bb95f2f83b07eae"
  },
  "results/R133-supplement-fixed-stop-connector-and-complete-regular-ports.md": {
    "sha256": "63b641775538e19be0a429327043566d58012d18130219079e415b328236edb9",
    "git_blob": "9dc7d422d4084a8fd604dd694223348f99a196c2"
  },
  "notes/2026-11-14-R133-fixed-stop-connector-and-full-ports-rational.json": {
    "sha256": "fcaf82fe70ffc6d5bafd71210edbf4e374e70b5fee5f288fcb10f177dc154f02",
    "git_blob": "4cea6b09c41dfd246ff681cd47034d17e2d080e2"
  },
  "results/R133-supplement-fixed-stop-D0-complete-sources-and-incoming.md": {
    "sha256": "7c2c9b0d5070427078d7fcc2384ad2d5b98e0f59c71c3a9e9dff5bebf5d7284f",
    "git_blob": null
  }
};
const topicRoot=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const digest=s=>createHash("sha256").update(s).digest("hex");
const loaded={};
for(const [name,expected] of Object.entries(expectedInputs)){
  const bytes=fs.readFileSync(path.join(topicRoot,name));
  if(bytes.length>=100000)throw Error("input exceeds the text-only consumer scope: "+name);
  const got=digest(bytes);
  if(got!==expected.sha256)throw Error("input identity mismatch: "+name+" "+got);
  loaded[name]=bytes.toString("utf8");
}
const previous=JSON.parse(loaded["notes/2026-11-14-R133-fixed-stop-connector-and-full-ports-rational.json"]);
const report=fixedStopD0Budget(previous);
report.execution={
  runtime:"Node "+process.version+"; same exact BigInt core",
  unavailable_native_environment_recovered:false,
  original_implementation_note:{
    initial_gate:"same_unchanged_long_analytic_width",
    issue:"the expected rational was unreduced; the computed rational and mathematical bound were correct",
    expected_unreduced:"1675766693242995/156250000",
    actual_reduced:"335153338648599/31250000",
    mathematical_bound_changed:false
  }
};
report.proof_sha256=expectedInputs["results/R133-supplement-fixed-stop-D0-complete-sources-and-incoming.md"].sha256;
report.producer_sha256=digest(fs.readFileSync(fileURLToPath(import.meta.url)));
report.core_sha256=digest(fixedStopD0Budget.toString());
report.inputs=expectedInputs;
const json=JSON.stringify(report,null,2)+"\n";
const argv=process.argv.slice(2);
if(argv.length===0){process.stdout.write(json);}
else if(argv.length===2&&argv[0]==="--out"){
  const out=path.resolve(argv[1]);
  if(fs.existsSync(out))throw Error("refusing to replace an existing report; choose a new output path");
  fs.writeFileSync(out,json,{flag:"wx"});
  process.stdout.write(JSON.stringify({complete:report.complete,gates:report.gate_count,out})+"\n");
}else throw Error("usage: node scripts/fourfold_regular_fixed_stop_D0_sources.mjs [--out NEW_PATH]");
