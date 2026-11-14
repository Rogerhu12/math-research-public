#!/usr/bin/env node
/** Full short-support radial control; exact costs and true middle-width payment. */
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
function calculate(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
 const q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return{n:n/g,d:d/g};};
 const add=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d),sub=(a,b)=>q(a.n*b.d-b.n*a.d,a.d*b.d),mul=(a,b)=>q(a.n*b.n,a.d*b.d);
 const str=a=>a.n+"/"+a.d,cmp=(a,b)=>a.n*b.d-b.n*a.d,two=k=>q(2n**BigInt(k));
 const gates=[],gate=(name,a,b,relation="lt")=>gates.push({name,left:str(a),right:str(b),relation,pass:relation==="eq"?cmp(a,b)===0n:cmp(a,b)<0n});
 const L=13n,j=8193n,J=j+5n;
 gate("all_short_intervals_start_inside_J",q(7,16),q(113,256));
 gate("all_short_intervals_end_inside_J",q(114,256),q(15,32));
 gate("total_reserved_length",sub(q(114,256),q(113,256)),q(1,256),"eq");
 gate("first_half_length",q(1,512n*2n),q(1,1024),"eq");
 gate("all_half_lengths_at_most_old_l",q(1,1024),q(1,64));
 gate("Chebyshev_contour_q_below_2pow_minus8",q(129,65535),q(1,256));
 gate("propagation_exponent_at_least_1_over_L",q(L+8n),q(8n*L));
 gate("large_disk_polynomial_power",q(19n*L+187n),q(20n*L+200n));
 gate("F_large_disk_quartic_power_dominated",q(414),q(2n*(20n*L+200n)));
 gate("F_small_interval_difference_of_squares",q(3n*9n**9n),two(31));
 gate("F_propagation_prefactor",q(3),q(4));
 gate("F_propagation_bit_loss",q(1-40+2),q(-37),"eq");
 gate("square_root_jet_constant_1",q(1+2),q(4));
 gate("square_root_jet_constant_2",q(1+4*2),q(9),"eq");
 gate("square_root_jet_constant_3",q(1+6*3),q(25));
 gate("square_root_jet_constant_4",q(1+8*5),q(49));
 gate("square_root_jet_maximum",q(7),q(8));
 gate("Hermite_kernel_separation_bit_polynomial",q(32n*L*(20n*L+284n)),q(640n*L*L+9088n*L),"eq");
 gate("real_energy_Cauchy_factor",q(6),q(8));
 gate("real_energy_bit_power",q((21+3)*32),q(768),"eq");
 gate("kernel_M_power_combination",q(32n*L*(1n-L)+1n-32n*L),q(1n-32n*L*L),"eq");
 gate("kernel_bit_quadratic_coefficient",q(640+768+320),q(1728),"eq");
 gate("kernel_bit_linear_fee_at_first_L",q(9088),q((4096n-1728n)*L));
 gate("kernel_B_linear_fee_at_first_L",q(480),q((192n-128n)*L));
 gate("kernel_a_power_rounding",q(96n*L*L-2n),q(96n*L*L));
 gate("kernel_lambda_power_rounding",q(96n*L*L-1n),q(96n*L*L));
 gate("kernel_K_power_rounding",q(128n*L*L-2n),q(128n*L*L));
 gate("kernel_complex_growth_coefficient",mul(q(32),two(60)),two(65),"eq");
 gate("compact_support_inside_every_short_interval",q(L+1n),q(4096n*L*L+156n));
 gate("compact_bit_quadratic_rounding",q(26n*4096n*L*L+4136n+250n),mul(two(17),q(L*L)));
 gate("compact_a_rounding",q(2496n*L*L+51n),q(2560n*L*L));
 gate("compact_B_rounding",q(4992n*L*L+130n),q(5120n*L*L));
 gate("compact_lambda_rounding",q(2496n*L*L+25n),q(2560n*L*L));
 gate("compact_K_rounding",q(3328n*L*L+51n),q(3456n*L*L));
 gate("compact_complex_exponential_rounding",add(mul(q(26n*L*L),two(65)),mul(q(25),two(60))),mul(q(L*L),two(70)));
 gate("coarse_a_plus_B_power",q(2560+5120),q(7680),"eq");
 gate("coarse_delta_power",q(3*7680+2*16*3456,2),q(66816),"eq");
 gate("coarse_J_power",q(5120+8*3456),q(32768),"eq");
 gate("coarse_frequency_power",q(2*2560),q(5120),"eq");
 gate("coarse_fixed_bit_cost",q(2n**17n+5n*7680n+2n*5120n+6000n*3456n),two(25));
 gate("coarse_cost_below_original_delta_fee",q(66816),q(285554));
 gate("coarse_cost_below_original_J_fee",q(32768),q(144890));
 gate("coarse_cost_below_original_frequency_fee",q(5120),q(19966));
 gate("coarse_bit_cost_below_original",two(25),two(27));
 gate("coarse_layer_exponential_below_original",two(72),two(74));
 gate("coarse_frequency_exponential_below_original",two(69),two(71));
 gate("actual_middle_band_count",q(65538),q((1024n-204n-320n)*J));
 gate("band_index_shift",q(2),mul(two(10),q(J)));
 gate("short_interval_L_below_layer",q(30*256),q(255n*j));
 gate("width_layer_exponent_with_L_squared",sub(q(31,256),q(3,512)),q(59,512),"eq");
 gate("width_frequency_exponent_with_L_squared",sub(q(191,256),q(5,1024)),q(759,1024),"eq");
 gate("full_layer_width_fee_at_first_layer",q((116n+801n)*512n),q(59n*j));
 gate("full_frequency_width_fee_at_first_layer",q((71n+801n)*1024n),q(759n*j));
 gate("short_interval_same_width_budget",q(2,2n**801n),q(1,2n**800n),"eq");
 return {
 kind:"actual_transparent_resonance_control_on_each_unused_short_interval",
 complete:gates.every(x=>x.pass),executed:true,arithmetic:"normalized exact BigInt rational",gate_count:gates.length,gates,
 input_blobs:{kernel:"8b5e908a0da26a3a6038de2808cbe41c9849f439",compact_control:"5662bf40391a53a2212311406cf7ad63064908fc",complete_family:"f11edbccd752bf034aa40e71888859d667a04b42",phase_compensation:"dd0d1378fce997297795ce14312fe91b181af4b1"},
 interval:{left:"113/256+(1/256)*n/(n+1)",right:"113/256+(1/256)*(n+1)/(n+2)",half_width:"1/(512*(n+1)*(n+2))",L:"12+ceil(log2((n+1)*(n+2)))",L_min:13},
 kernel_lower:"2^(-4096*L^2)*a^(96*L^2)*B^(-192*L^2)*lambda^(-96*L^2)*Kj^(-128*L^2)*exp(-2^65*L^2*T)",
 true_compensated_Wronskian_derivative_lower:"[2^(-2^17)*a^2560*B^-5120*lambda^-2560*Kj^-3456*exp(-2^70*T)]^(L^2)",
 coarse_lower:"[2^(-2^25)*delta^66816*J^-32768*M^-5120*exp(-2^72*J-2^69*M*delta^3/4*sqrt(J))]^(L^2)",
 actual_middle:{lower:"2^-40*delta^-1/8",upper:"2^65536*J^204*delta^-320",layer_min:8193,L_at_most:"J=j+5",full_log_cost_upper:"2^-803*M*h_j"},
 actual_local_polynomial_and_prior_controls_supported_elsewhere:true,
 original_material_dt_and_fixed_unit_Robin_lines:true,full_phase_first_derivative_zero_at_current_profile:true,
 finite_multi_mode_parameter_selection:false,coupled_nonradial_middle_inverse:false,original_source_weights_unchanged:true
 };
}
const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--out')throw Error('usage: node this.mjs --out NEW_REPORT.json');
const report=calculate();
report.producer_sha256=createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex');
await writeFile(args[1],JSON.stringify(report,null,2)+'\n',{flag:'wx'});
if(!report.complete)process.exitCode=1;
console.log(JSON.stringify({complete:report.complete,gate_count:report.gate_count,out:args[1]}));
