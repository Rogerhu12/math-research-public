#!/usr/bin/env node
/** Quantitative separation of the actual radial transparent-resonance kernel. */
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
function calculate(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
 const q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return{n:n/g,d:d/g};};
 const add=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d),mul=(a,b)=>q(a.n*b.n,a.d*b.d),pow=(a,k)=>q(a.n**BigInt(k),a.d**BigInt(k));
 const str=a=>a.n+"/"+a.d,cmp=(a,b)=>a.n*b.d-b.n*a.d;
 const gates=[],gate=(name,a,b,relation="lt")=>gates.push({name,left:str(a),right:str(b),relation,pass:relation==="lt"?cmp(a,b)<0n:relation==="le"?cmp(a,b)<=0n:cmp(a,b)===0n});
 const two=n=>q(2n**BigInt(n));
 gate("quartic_on_fixed_complex_disk",add(mul(q(30),mul(pow(q(1025),2),pow(q(1026),2))),q(7)),two(46));
 gate("quartic_square_root_modulus",add(q(1),mul(q(16),q(7,30))),pow(q(3,2),4));
 gate("all_four_roots_in_unit_disk_at_J_centre",add(q(3,4),q(3,64)),q(1));
 gate("simple_root_separation_squared",q(1,16),q(7,30));
 gate("real_J_Q_upper_factor",add(q(7),q(15,8)),q(9));
 const x=q(7,16),oneMinusX=q(9,16);
 gate("real_J_S_prime_lower",q(7,4),mul(q(30),mul(pow(x,2),pow(oneMinusX,2))));
 gate("real_J_S_second_lower",q(7,8),mul(q(60),mul(q(15,32),mul(q(17,32),q(1,16)))));
 gate("fixed_disk_chebyshev_balance",mul(q(258),q(129,65535)),q(1));
 gate("cauchy_interpolation_remainder_factor",q(1024,1022),q(2));
 gate("degree_19_extrapolation_factor",q(131074),two(18));
 gate("real_P_norm_factor",mul(q(2),q(3n**9n)),two(16));
 gate("degree_19_complex_P_factor_exponent",q(18*19+16),q(358),"eq");
 gate("Hermite_four_roots_five_jets_factor",q(4n*(2n**15n)*5n*16n*15300n),two(40));
 gate("Hermite_root_separation_factor_exponent",q(40+2*19),q(80));
 const C=[1,2,3,5,7];
 for(let j=1;j<=4;j++)gate("square_root_jet_step_"+j,q(1+2*j*C[j-1]),q(C[j]*C[j]),"le");
 gate("F_complex_growth_dominates_both_terms",add(two(414),two(716)),two(717));
 gate("F_real_error_factor",q(3n**19n),two(31));
 gate("F_interpolated_constant",mul(q(3),two(374)),two(376));
 gate("P_root_jet_factor",mul(q(7),two(358)),two(361));
 gate("real_K_separation_constant",add(q(1),two(441)),two(443));
 gate("abstract_gap_exponent",q(443*64),q(28352),"eq");
 gate("positive_energy_wave_comparison",q(55),q(128));
 gate("actual_energy_jet_comparison",q(1329+23+1782+990+22),two(14));
 gate("actual_energy_jet_scale_exponent",q(7+14),q(21),"eq");
 gate("root_jet_to_real_sup_constant",q(36),q(64));
 gate("actual_normalized_gap_exponent",q(28352+48*64),q(31424),"eq");
 gate("actual_normalized_B_power",q(960+8*64),q(1472),"eq");
 gate("actual_normalized_M_power",q(63+64),q(127),"eq");
 gate("initial_scaled_complex_state_factor",q(9),q(10));
 gate("mu_on_fixed_complex_disk",mul(q(1024),add(q(8),two(45))),two(56));
 gate("full_complex_ODE_and_density_growth",add(mul(q(5),two(56)),q(2)),two(60));
 gate("complex_polynomial_prefactor",q(400),two(10));
 gate("final_constant_bit_exponent",q(31424+127*10),q(32768));
 gate("final_complex_exponential_coefficient",mul(q(127),two(60)),two(67));
 gate("actual_a_lower_comparison_squared",q(384),q(400));
 gate("actual_a_upper_comparison_squared",q(256),q(384));
 gate("final_delta_power",q(3*(382+1472)/2+16*510),q(10941),"eq");
 gate("final_J_power",q(1472+8*510),q(5552),"eq");
 gate("final_mode_power",q(2*383),q(766),"eq");
 gate("final_fixed_tail_bit_exponent",q(32768+510*6000+5*(382+1472)+2*1472),two(22));
 return{
 kind:"actual_transparent_resonance_kernel_quantitative_separation",
 complete:gates.every(x=>x.pass),executed:true,arithmetic:"normalized exact BigInt rational",gate_count:gates.length,gates,
 true_profile:{j_min:8193,delta:"(2/25) 2^(-j)",a:"delta^(3/2)/(8 sqrt(6))",Delta:"j/2 < Delta < 3(j+4)",B:"Delta/a",Q:"7+30 B x^2 (1-x)^2",J:"[7/16,15/32]",centre:"29/64",half_width:"1/64",complex_radius:1024,root_observation_radius:2},
 normalizations:{m:"nonzero fourfold physical m, abs(m)>=4",lambda:"m^2",left_wave_state:"Euclidean norm 1 in (sqrt(k)u,u_t/sqrt(k)); k=sqrt(7m^2-16)",full_real_Cauchy:"Kj=2^6000 (j+5)^8 delta^-16",phase_kernel_span:"P/Q^(9/2), deg(P)<=19"},
 abstract_lower:"2^-28352 B^-960 kappa^64 M^-63",
 actual_kernel_lower:"2^-32768 a^382 B^-1472 lambda^-383 Kj^-510 exp(-2^67 T)",
 T:"1+Delta+chi; chi=1+abs(m)*sqrt(a*(1+Delta))",
 explicit_tail_lower:"2^(-2^22) delta^10941 (j+5)^-5552 abs(m)^-766 exp(-2^69*(j+5)-2^66*abs(m)*delta^(3/4)*sqrt(j+5))",
 outputs:{complete_actual_kernel_distance_in_Linfinity_from_both_phase_kernels:true,frequency_uniform_formula:true,normalized_C4_control_direction_constructed:false,true_Wronskian_derivative_gap_after_phase_correction_proved:false,all_moving_Schur_inverse_proved:false},
 inputs:[{path:"results/R119-supplement-phase-preserving-actual-finite-Schur-controls.md",git_blob:"5214cfffb5d16f3aebb0105af8aab14b2b5188b1",used:"actual scalar ODE, density wave ports, real full Cauchy Kj, both phase kernels and exact symmetric-square identity"}],
 no_native_candidate_or_discrete_frequency_samples_used:true
 };
}
const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--out')throw Error('usage: node this.mjs --out NEW_REPORT.json');
const report=calculate();
report.producer_sha256=createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex');
await writeFile(args[1],JSON.stringify(report,null,2)+'\n',{flag:'wx'});
if(!report.complete)process.exitCode=1;
console.log(JSON.stringify({complete:report.complete,gate_count:report.gate_count,out:args[1]}));
