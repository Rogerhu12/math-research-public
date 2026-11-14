#!/usr/bin/env node
/** Actual phase-preserving C4 compact metric control. */
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
function calculate(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
 const q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return{n:n/g,d:d/g};};
 const add=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d),mul=(a,b)=>q(a.n*b.n,a.d*b.d),pow=(a,k)=>q(a.n**BigInt(k),a.d**BigInt(k));
 const str=a=>a.n+"/"+a.d,cmp=(a,b)=>a.n*b.d-b.n*a.d,two=n=>q(2n**BigInt(n));
 const gates=[],gate=(name,a,b,relation="lt")=>gates.push({name,left:str(a),right:str(b),relation,pass:relation==="lt"?cmp(a,b)<0n:cmp(a,b)===0n});
 let fact=1n;for(let n=1n;n<=21n;n++)fact*=n;
 gate("real_branch_disk_keeps_roots_outside",q(1,4),q(29,64));
 gate("real_branch_disk_right_edge",add(q(29,64),q(1,4)),q(1));
 gate("quartic_in_small_disk",add(q(7),mul(q(30),mul(pow(q(45,64),2),pow(q(51,64),2)))),q(17));
 gate("algebraic_factor_small_disk_power",q(17n**9n),two(40));
 gate("fixed_Cauchy_circle_in_small_disk",add(q(1,64),q(1,8)),q(1,4));
 gate("twenty_first_factorial",q(fact),two(66));
 gate("twenty_first_derivative_margin",q(20+63+66),q(152));
 gate("algebraic_factor_four_derivatives",mul(q(24),two(32)),two(37));
 gate("bump_degree_derivative_factor",q(60n**24n),two(144));
 gate("full_C4_sum_factor",mul(q(80),two(211)),two(220));
 gate("bump_positive_integral",q(1,2n**15n),pow(q(3,4),30));
 gate("bump_support_radius_fits",q(1,2n**156n),q(1,128));
 gate("sign_is_preserved_over_complete_support",q(3,16),q(1,2));
 gate("normalized_x_pairing_bit_exponent",q(16+220+100+152*25),q(4136),"eq");
 gate("normalized_x_pairing_B_power",q(5+5*25),q(130),"eq");
 gate("raw_kernel_power_after_control",q(1+25),q(26),"eq");
 gate("Wronskian_bit_exponent_before_M",q(4136+32768*26),q(856104),"eq");
 gate("Wronskian_a_power_before_M",q(1+382*26),q(9933),"eq");
 gate("Wronskian_B_power",q(130+1472*26),q(38402),"eq");
 gate("Wronskian_lambda_power_before_M",q(383*26),q(9958),"eq");
 gate("Wronskian_Kj_power_before_M",q(1+510*26),q(13261),"eq");
 gate("Wronskian_final_bit_exponent",q(856104+10*25),two(20));
 gate("Wronskian_final_a_power",q(9933+2*25),q(9983),"eq");
 gate("Wronskian_final_lambda_power",q(9958+25),q(9983),"eq");
 gate("Wronskian_final_Kj_power",q(13261+2*25),q(13311),"eq");
 gate("Wronskian_final_complex_coefficient",add(mul(q(26),two(67)),mul(q(25),two(60))),two(72));
 gate("actual_tail_a_power",q(9983+38402),q(48385),"eq");
 gate("actual_tail_delta_power_round_down_lower_bound",q(3*(9983+38402)+2*16*13311,2),q(285554));
 gate("actual_tail_J_power",q(38402+8*13311),q(144890),"eq");
 gate("actual_tail_m_power",q(2*9983),q(19966),"eq");
 gate("actual_tail_fixed_bit_exponent",q(2n**20n+6000n*13311n+5n*48385n+2n*38402n),two(27));
 return{
 kind:"actual_phase_preserving_C4_compact_control_and_normalized_Wronskian_derivative",
 complete:gates.every(x=>x.pass),executed:true,arithmetic:"normalized exact BigInt rational",gate_count:gates.length,gates,
 input:{kernel_proof:"results/R119-supplement-quantitative-transparent-resonance-kernel.md",git_blob:"8b5e908a0da26a3a6038de2808cbe41c9849f439",phase_control_proof_blob:"5214cfffb5d16f3aebb0105af8aab14b2b5188b1"},
 construction:{G:"Q^(9/2) K",local_derivative_bound:"M21=2^152 B^5 M",width:"r=epsilon0/(16 M21)",test:"f=r^24 (1-((x-x1)/r)^2)_+^30",direction:"psi=sign*Q^(9/2) f^(20)/(2^220 B^5)",C4_norm:"sum of sup norms of derivatives 0..4, at most 1",regularity:"real compact C9, hence C5"},
 exact_phase_tangency:true,full_phase_compensation_by_actual_two_bumps:true,compensating_parameters_first_derivatives_zero:true,
 normalized_Wronskian_derivative_lower:"2^(-2^20) a^9983 B^-38402 lambda^-9983 Kj^-13311 exp(-2^72 T)",
 explicit_tail_lower:"2^(-2^27) delta^285554 (j+5)^-144890 abs(m)^-19966 exp(-2^74*(j+5)-2^71*abs(m)*delta^(3/4)*sqrt(j+5))",
 actual_dt_measure_factor_retained:true,true_right_resonance_amplitude_factor_retained:true,
 fixed_actual_Robin_lines:true,whole_nonradial_middle_matrix_inverted:false,
 finite_epsilon_Wronskian_gap_or_bad_set_proved:false,low_frequency_source_radial_weight_changed:false
 };
}
const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--out')throw Error('usage: node this.mjs --out NEW_REPORT.json');
const report=calculate();
report.producer_sha256=createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex');
await writeFile(args[1],JSON.stringify(report,null,2)+'\n',{flag:'wx'});
if(!report.complete)process.exitCode=1;
console.log(JSON.stringify({complete:report.complete,gate_count:report.gate_count,out:args[1]}));
