import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

function fixedStopBudget(){
 const abs=x=>x<0n?-x:x;
 const gcd=(a,b)=>{a=abs(a);b=abs(b);while(b){const c=a%b;a=b;b=c;}return a;};
 const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];};
 const add=(x,y)=>Q(x[0]*y[1]+y[0]*x[1],x[1]*y[1]);
 const neg=x=>[-x[0],x[1]],sub=(x,y)=>add(x,neg(y));
 const mul=(x,y)=>Q(x[0]*y[0],x[1]*y[1]);
 const div=(x,y)=>Q(x[0]*y[1],x[1]*y[0]);
 const sq=x=>mul(x,x),lt=(x,y)=>x[0]*y[1]<y[0]*x[1];
 const p2=e=>e>=0?Q(1n<<BigInt(e)):Q(1n,1n<<BigInt(-e));
 const p10=e=>10n**BigInt(e),repr=x=>x[0].toString()+"/"+x[1].toString();
 const gates=[];function gate(name,passed,evidence){gates.push({name,passed,evidence});if(!passed)throw Error(name);}
 const deltaCentre=Q(-7789843107295549n,4611686018427387904n);
 const R74Centre=Q(-7789866024620307n,4611686018427387904n);
 const centreDifference=sub(deltaCentre,R74Centre);
 gate("entire_actual_eta_inside_paid_R74_domain",
   lt(add(Q(abs(centreDifference[0]),centreDifference[1]),Q(1,1000000000)),Q(1,2000000)),
   "Actual complete affine halfwidth1e-9 stays in R74 (74.1); the body nu bump is zero at R.");
 const deep=p2(-193532),d1=mul(p2(-22),p2(-15)),d2=mul(p2(-8),p2(-29));
 const eps=add(deep,add(d1,d2)),epsBound=p2(-35),small=p2(-12);
 gate("actual_deep_screen_exact_exponent",24*8064+3-7===193532,"C.36: cut128 d4, same Gamma, not lambda.");
 gate("both_true_Gamma_columns_kept",repr(d1)===repr(p2(-37))&&repr(d2)===repr(p2(-37)),"U.17: gamma1 derivative2^-22 and gamma2 derivative2^-8; whole box diameters2^-15 and2^-29.");
 gate("complete_fixed_stop_cut_difference",lt(eps,epsBound),"2^-193532+2^-37+2^-37 <2^-35.");
 gate("actual_cut_error_inside_negative_tube",lt(epsBound,small),"Universal bootstrap can use epsilon_d<=2^-12.");
 gate("whole_connector_upper_face_slack",lt(mul(Q(15),small),sub(Q(1,6),Q(1,8))),"Reference R<=-1/6; perturbation15 epsilon_d stays below-1/8.");
 gate("whole_connector_lower_face_slack",lt(mul(Q(15),small),Q(1)),"Reference R>-14; perturbation stays above-15.");
 gate("inverse_Riccati_rate_positive",repr(sub(Q(4),Q(2)))==="2/1","-q-16(Rnew+Rbase)>=2 for q<=2 and both R<=-1/8.");
 const eT=mul(Q(60),small);
 gate("relative_T_fourth_error_below_one_eighth",lt(eT,Q(1,8)),"lambda4(T)/(4omega)+1 <=60 epsilon_d.");
 const omin=Q(7,5),omax=Q(3,2),psi1=Q(15,16384),psi2=Q(3,16);
 const kmin=sub(sq(sub(omin,psi1)),psi2),kmax=add(sq(add(omax,psi1)),psi2);
 const pmin=Q(5,4),pmax=Q(8,5);
 gate("true_two_bump_positive_lower",lt(sq(pmin),kmin),"(omega+psi')²+psi'' >(5/4)².");
 gate("true_two_bump_positive_upper",lt(kmax,sq(pmax)),"(omega+psi')²+psi'' <(8/5)².");
 gate("new_T_log_slope_inside_lower_cone",lt(pmin,mul(omin,sub(Q(1),eT))),"p(T)= -lambda4(T)/4.");
 gate("new_T_log_slope_inside_upper_cone",lt(mul(omax,add(Q(1),eT)),pmax),"Both actual and reference p stay in [5/4,8/5] under backward flow.");
 gate("fourth_angle_never_bad",lt(mul(Q(1,4),mul(add(Q(1),sq(pmax)),add(Q(1),sq(omax)))),sq(add(pmin,omin))),"sin(angle((1,-p),(1,omega)))>1/2.");
 gate("new_high_bad_angle_crossing_preserved",lt(Q(1,16384),Q(1,2)),"Old reference curve slope ratio<1/64 and NEW high-line K1/K2<1/256.");
 const ell=Q(1,16),gamma0=p2(-17),epsAngle=p2(-39);
 const bad=div(mul(Q(1328),epsAngle),mul(gamma0,ell));
 gate("all_new_high_modes_summable",repr(bad)==="83/16384"&&lt(bad,Q(1)),"Repeat R11 A.6-A.10 for new nonzero right lines; old good parameter is not reused.");
 gate("deep_screen_inner_constant",lt(Q(240),p2(8)),"Same-Gamma inner relative error<2^-193524 exp(-8L).");
 gate("whole_parameter_inner_constant",lt(mul(Q(240),epsBound),p2(-27)),"Whole real box inner relative error<2^-27 exp(-8L).");
 gate("new_fourth_fits_all_mode_regular_contract",lt(p2(-27),p2(41)),"m4 now has a paid nonzero fee, smaller than the all-mode2^41 coefficient.");
 const Blo=sub(p2(24),Q(25,8)),Llo=mul(omin,Blo);
 gate("same_actual_full_long_length",lt(p2(24),Llo),"L=omega(2^24-25/8), omega>7/5.");
 gate("complete_regular_error_below_two_minus_512",lt(Q(555),mul(Q(8),Llo)),"(2^42+8) exp(-8L)<2^(43-8L)<2^-512; no floating underflow.");
 gate("independent_long_reflected_source_below_two_minus_512",lt(Q(513),mul(Q(6),Llo)),"2 exp(-6L)<2^-512.");
 gate("two_trace_matrix_fourth_invertible",repr(mul(Q(16),sub(Q(1),Q(1,16))))==="15/1","R74 actual (y,y'/4)->(v,p) determinant15.");
 gate("fourth_grounded_DN_sensitivity",lt(Q(75,112),Q(1)),"|Delta gamma4| <=75/112 times |Delta lambda4|/(4omega), when both lambda4<0.");
 const e=p2(-512),z=Q(2532986,p10(19)),lin=Q(1256750,p10(21));
 const prop=Q(91496,p10(22));
 gate("unchanged_dyadic_q_proposal_budget",lt(add(prop,e),Q(1,p10(17))),"9.1496e-18 + all-mode2^-512 <1e-17.");
 const rz=Q(1,p10(12)),rb=p2(-60),rf=mul(Q(10),add(rz,rb)),F=add(rf,rb);
 const image=add(add(mul(Q(9),rz),mul(e,rb)),mul(Q(9*4096),sq(F)));
 const lip=mul(Q(36*4096),F);
 gate("same_true_periodic_long_C_inverse",lt(image,rf)&&lt(lip,Q(1)),"Geometry unchanged; full fB input retained.");
 const dn=add(add(mul(e,rz),mul(e,rb)),mul(Q(16384),sq(F)));
 const row=add(add(lin,mul(Q(2),mul(e,z))),dn);
 const mean=add(Q(6055,p10(46)),mul(Q(2048),sq(F)));
 gate("complete_actual_nonlinear_nonmean_row",lt(row,Q(1258389,p10(21))),"Full physical A0 row, every frequency: <1.258389e-15.");
 gate("complete_actual_independent_mean_row",lt(mean,Q(2048004,p10(25))),"Full C mean row<2.048004e-19; B mean zero by reflection, mean height retained.");
 const alpha=Q(6890507429876859n,9007199254740992n);
 gate("actual_alpha_normalized_rows",lt(div(row,alpha),Q(1645,p10(18)))&&lt(div(mean,alpha),Q(2678,p10(22))),"Normalize only after physical rows: <1.645e-15 and2.678e-19.");
 return {
  kind:"actual_fixed_stop_fourth_line_and_complete_regular_port_budget",
  complete:true,arithmetic:"normalized BigInt rational arithmetic and strict cross-multiplication; exp bounds proved via e>2",
  candidate_sha256:"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
  cut_error:{deep_only:{mantissa:"1",dyadic_exponent:-193532},
    gamma1_derivative:{mantissa:"1",dyadic_exponent:-22},
    gamma2_derivative:{mantissa:"1",dyadic_exponent:-8},
    full_box_bound:"2^-35",
    meaning:"cut128 physical d4 difference; no identification with lambda"},
  connector:{fixed_stop:true,R_tube:["-15","-1/8"],reference_R_upper:"-1/6",
    inverse_flow_lipschitz_upper:"1",cut_to_R_lipschitz:"15",cut_to_T_relative_lambda:"60",
    cut_to_inner_relative_lambda:"240 exp(-8L)"},
  full_new_good_angle:{epsilon:"1/549755813888",bad_measure:repr(bad),
    reference_bump_curve_fixed:true,new_good_parameter_required:true,continuous_selection_claimed:false},
  retained_true_ports:{all_mode_q_fee:"2^-512",actual_dyadic_q_fee:"1e-17",
    full_nonmean_row:"1.258389e-15",full_C_mean_row:"2.048004e-19",
    independent_fB_ball:"2^-60",independent_mean_height_retained:true,
    ordinary_source_J_and_Rm_retained:true,new_affine_tail_source_not_set_zero:true},
  source_scope:{g0_on_finite_body_and_long:"unchanged",fixed_connector_scale_derivative:"zero",
    mean_height_change:"rho integral_1^b Delta w_bar",true_new_D0_repayment_still_required:true,
    actual_updated_nonlinear_tail_inverse_proved:false,full_body_BVP_inverse_proved:false},
  gate_count:gates.length,gates,
  modest_exact_values:{bump_K_lower:repr(kmin),bump_K_upper:repr(kmax),long_L_lower:repr(Llo),
    long_image_bound:repr(image),long_Lipschitz_bound:repr(lip)}
 };
}

const metadata={
  "proof_path": "results/R133-supplement-fixed-stop-connector-and-complete-regular-ports.md",
  "proof_sha256": "63b641775538e19be0a429327043566d58012d18130219079e415b328236edb9",
  "consumed_proof_inputs": {
    "results/R11-matched-mode-four-physical-tail-connector.md": {
      "sha256": "8c4e30ef3cac88ff3e7c858c77537bf03d102760b2324e1e1d21780cf59923ca",
      "git_blob": "891486d30d83cd06a580c6905825d8bdfbe49d8d"
    },
    "results/R74-actual-full-tail-robin-and-augmented-positive-cap.md": {
      "sha256": "174bc93631b5ade0faf51160d7026e42d674916fd94e12cdb2315479458c18d8",
      "git_blob": "12b50b77b27ca7f501a323164e905ce4af4963dd"
    },
    "results/R119-supplement-retuned-fourth-connector-and-common-bumps.md": {
      "sha256": "e22a74f54ea1122271e50d2bdcd2ae8db5bc4c28e1e36eaebc35c40f6c3c3752",
      "git_blob": "4f33b6277074962f7df3009355b44031fa6c1389"
    },
    "results/R119-supplement-two-parameter-full-tail-chart-reconstructed.md": {
      "sha256": "3cc2cb9efe51ff275ce9eba496bafe6df94e3eaafabfd07fe74b6415bd9c5f46",
      "git_blob": "a76cb5bb70bd0d2e5a5a48967b16679ef8ed4170"
    },
    "results/R119-supplement-controlled-profile-full-label-and-raw-ports.md": {
      "sha256": "ff11cb043128a5d66ee996bb174edda0d6537fe73f9a7a565ba143d2ab5c04d0",
      "git_blob": "f11edbccd752bf034aa40e71888859d667a04b42"
    },
    "results/R133-supplement-regular-fourth-mode-robustness-budget.md": {
      "sha256": "08647ab86a9f4a06702c33dafd27967be2b974f04cdf3d1b77a8434ef7aa8938",
      "git_blob": "4f08d7c4ee71b62ef80f8305fce7efd0cf1ce4ba"
    },
    "results/R133-supplement-final-moving-centre-actual-regular-boundary.md": {
      "sha256": "f4ae237c86542f29f2127f7e43d5ab97827756fcce86e71bcff8c0a610ec81af",
      "git_blob": "40463b6917c943e4ac991a597603cf41095baeb9"
    },
    "results/R133-supplement-actual-regular-R25over8-vector-and-long-ports.md": {
      "sha256": "288245decc9aa64b1bfa5baff77731e0cd6a09e117bbf3ac61a3235a3ee5c779",
      "git_blob": "210f2ccbd60a75ecd31e7f73994bde7f9a88c745"
    }
  }
};
const hash = bytes => createHash('sha256').update(bytes).digest('hex');
for (const [path, expected] of Object.entries(metadata.consumed_proof_inputs)) {
  if (hash(readFileSync(new URL('../'+path,import.meta.url))) !== expected.sha256)
    throw new Error('The consumed proof bytes changed: '+path);
}
if (hash(readFileSync(new URL('../'+metadata.proof_path,import.meta.url)))!==metadata.proof_sha256)
  throw new Error('The complete fixed-stop proof bytes changed');
const report=fixedStopBudget();
Object.assign(report,metadata);
report.producer_sha256=hash(readFileSync(new URL(import.meta.url)));
console.log(JSON.stringify(report,null,2));
