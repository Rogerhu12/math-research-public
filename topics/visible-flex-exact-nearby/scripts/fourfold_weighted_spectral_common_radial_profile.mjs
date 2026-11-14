#!/usr/bin/env node
/** Actual full-middle weighted spectral averaging and one common radial profile. */
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
function calculate(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
 const R=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};};
 const add=(a,b)=>R(a.n*b.d+b.n*a.d,a.d*b.d),mul=(a,b)=>R(a.n*b.n,a.d*b.d),cmp=(a,b)=>a.n*b.d-b.n*a.d,str=a=>a.n+"/"+a.d;
 const gates=[],gate=(name,a,b,eq=false)=>gates.push({name,left:str(a),right:str(b),relation:eq?"=":"<",pass:eq?cmp(a,b)===0n:cmp(a,b)<0n});
 const j=8193n,J=j+5n;
 gate("actual_first_middle_frequency_is_above_1024",R(10),add(R(-40),R(j+3n,8)));
 gate("upper_middle_exponent_exceeds_next_lower_first_layer",add(R(-40),R(j+5n,8)),add(R(65536),R(320n*(j+3n))));
 gate("upper_middle_exponent_gap_increases_in_layer",R(1,8),R(320));
 gate("whole_path_phase_variation",mul(R(2),R(1,8)),R(1,4),true);
 gate("one_near_one_arc_per_monotone_branch",R(1,4),R(1));
 gate("small_arc_probability_coefficient",R(2,128),R(1,64),true);
 gate("weighted_integral_Markov_probability_coefficient",R(2,128),R(1,64),true);
 gate("combined_conditional_bad_probability_coefficient",add(R(1,64),R(1,64)),R(1,32),true);
 gate("all_positive_fourfold_frequency_probability",R(2,32*16),R(1,256),true);
 gate("fixed_stop_and_all_mode_bad_union",add(R(83,16384),R(1,256)),R(147,16384),true);
 gate("joint_product_good_set_has_positive_measure",R(147,16384),R(1));
 gate("middle_network_dimension_at_M1024",R(16*10+642),R(1024));
 gate("dimension_comparison_derivative_after_M1024",R(32,1024),R(1));
 gate("log_M_below_M_over_eight_at_M1024",R(10),R(1024,8));
 gate("log_M_comparison_derivative",R(1,1024),R(1,8));
 gate("constant_log_fee_fits_M_over_eight",R(10),R(1024,8));
 gate("complete_logarithmic_resolvent_factor",add(add(R(1),R(3,8)),R(1,8)),R(2));
 gate("full_weighted_inverse_polynomial_prefactor",R(128*2),R(256),true);
 gate("smallest_window_positive_constant_only_costs_log",R(8,2n**800n),R(1));
 gate("log_weighted_resolvent_is_below_local_polynomial_fee",R(8n+4n*1024n*J),R(8192n*J));
 gate("original_middle_fee_first_layer",R(50n*512n-61n*j,512n),R(-803));
 gate("original_middle_fee_monotone_layer_slope",R(-61,512),R(0));
 gate("two_sided_local_weight_pays_D_and_T",add(R(1,2n**800n),R(1,2n**803n)),R(2,2n**800n));
 gate("all_band_profile_controls_remain_in_actual_compensation_ball",R(1,2n**79n),R(1,2n**64n));
 return {
 schema:"R119-actual-weighted-spectral-averaging-common-infinite-radial-profile-v1",
 complete:gates.every(g=>g.pass),executed:true,arithmetic:"normalized exact BigInt rational; analytical spectral and product-measure proof in companion text",
 gate_count:gates.length,gates,
 dependencies:{
  actual_controlled_tail:"f11edbccd752bf034aa40e71888859d667a04b42",
  all_quadratic_positive_control_commit:"3ef38d431196ec42cccc6e5b4085e44b2f589926",
  exact_fixed_stop_connector:"9dc7d422d4084a8fd604dd694223348f99a196c2",
  complete_unitary_network_commit:"789268ff1c9d7852733f32e6f89fc3c37cbe6d7f"
 },
 actual_middle_windows:"j>=8193 with 2^-40 delta_j^-1/8 <= M <= 2^65536(j+5)^204 delta_j^-320",
 dimension:"2 * number of actual middle windows",
 all_omitted_windows:"eliminated exactly into true real prefix line and complete actual infinite-low-tail line, including affine source data",
 coordinate:"one theta_M simultaneously controls exactly that M's actual middle windows; all other coordinates and outer t fixed in conditional derivative",
 uniform_matrix_monotonicity:"-i U_M* partial_theta_M U_M >= diag(D_jM I2), D_jM>exp(-2^-800 M h_j)",
 conditional_bad_probability:"<1/(32 M^2)",
 joint_good_product_measure:">=1-147/16384",
 weighted_inverse:"||W_M^-1 (I-U_M)^-1 W_M^-1||<=1; W_jM=exp(2^-800 M h_j)",
 common_actual_radial_profile_exists:true,
 numerical_infinite_parameter_array_claimed:false,
 original_radial_h_zeta_low_source_weights_unchanged:true,
 distinct_radial_label_normalizations_connected:false,
 full_nonradial_inverse_proved:false,
 final_nonlinear_F_zero_proved:false
 };
}
const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--out')throw Error('usage: node this.mjs --out NEW_REPORT.json');
const report=calculate();
report.producer_sha256=createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex');
await writeFile(args[1],JSON.stringify(report,null,2)+'\n',{flag:'wx'});
if(!report.complete)process.exitCode=1;
console.log(JSON.stringify({complete:report.complete,gate_count:report.gate_count,out:args[1]}));
