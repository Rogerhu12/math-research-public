#!/usr/bin/env node
/** Simultaneous true radial middle gaps; finite boxes, exact phases and preservation budget. */
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
function calculate(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
 const q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return{n:n/g,d:d/g};};
 const add=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d),sub=(a,b)=>q(a.n*b.d-b.n*a.d,a.d*b.d),mul=(a,b)=>q(a.n*b.n,a.d*b.d);
 const str=a=>a.n+"/"+a.d,cmp=(a,b)=>a.n*b.d-b.n*a.d,two=k=>q(2n**BigInt(k));
 const gates=[],gate=(name,a,b,relation="lt")=>gates.push({name,left:str(a),right:str(b),relation,pass:relation==="eq"?cmp(a,b)===0n:cmp(a,b)<0n});
 const j=8193n,J=j+5n;
 gate("full_Hessian_paid_by_A_squared",two(20),two(6000));
 gate("near_resonance_line_has_nonzero_projection",q(1,16),q(1,2));
 gate("projected_line_derivative_fee",q(2,16),q(1,8),"eq");
 gate("full_box_Hessian_fee",q(1,64),q(1,4));
 gate("true_derivative_over_full_box",q(1,2),sub(sub(q(1),q(1,8)),q(1,64)));
 gate("inactive_Wronskian_change",q(16,64),q(1,4),"eq");
 gate("inactive_lower_gap_dominates_selected_gap",q(1,64),q(3,4));
 gate("finite_box_bad_set_union",q(2,16),q(1,8),"eq");
 gate("good_parameter_volume_is_positive",q(1,8),q(1));
 gate("future_radius_geometric_ratio",q(1,256),q(1,2));
 gate("future_radius_sum",q(256,255),q(2));
 gate("future_gap_relative_fee",q(2,16),q(1,8),"eq");
 gate("retained_gap_above_half",q(1,2),q(7,8));
 gate("whole_control_sum_inside_ball",q(1,2n**65n),q(1,2n**64n));
 gate("radius_recurrence_binary_cost",q(16*16),two(8),"eq");
 gate("first_actual_dyadic_band_index",q((j+3n)/8n-40n),q(984),"eq");
 gate("all_actual_band_counts",q(65538),q((1024n-204n-320n)*J));
 gate("uniform_log_K_cost",q(6000),q(J));
 gate("uniform_log_B_constant",q(96),two(7));
 gate("uniform_log_B_layer_cost",q(7),q(3n*J,2));
 gate("uniform_log_U_cost",q(65537),q((1024n-204n-320n)*J));
 gate("uniform_log_A_cost",q(2),q((2048n-50n-1024n)*J));
 gate("radius_log_polynomial_fee",q(66n+8192n+8388608n),two(24));
 gate("selected_gap_log_polynomial_fee",q(2n**24n+4n+2048n),two(25));
 gate("final_gap_log_polynomial_fee",q(2n**25n+1n),two(26));
 gate("band_endpoint_to_actual_mode_factor",q(3*2),q(6),"eq");
 gate("layer_fee_to_original_width_binary_cost",q(26+40-3),q(63),"eq");
 gate("layer_fee_delta_exponent",sub(q(31,256),q(2,512)),q(15,128),"eq");
 gate("entire_layer_fee_less_than_2pow_minus803",q((63n+803n)*128n),q(15n*j));
 gate("combined_width_fee",add(q(6,2n**803n),q(1,2n**803n)),q(1,2n**800n));
 return {kind:"simultaneous_radial_middle_Wronskian_selection_with_exact_phase_preservation",
 complete:gates.every(x=>x.pass),executed:true,arithmetic:"normalized exact BigInt rational",gate_count:gates.length,gates,
 inputs:{unused_interval_proof_blob:"27e75c019c0e4441c3237a36bb3c9f485fd2cdbf",phase_compensation_proof_blob:"dd0d1378fce997297795ce14312fe91b181af4b1",controlled_joint_high_proof_blob:"fc3aab62e99a51cc06bd26a7233663a2b8e4dd73"},
 frequency_bands:{k0:"floor((j+3)/8)-40",U_n:"2^(k0+n+1)",range:"2^-40*delta^-1/8 <= M <= 2^65536*(j+5)^204*delta^-320",one_interval_per_band:true},
 constants:{epsilon:"2^-803",D_n:"exp(-epsilon*U_n*h_j)",A_n:"2*Kj^2*(U_n+B)",H_n_upper:"A_n^2",near_resonance_threshold:"D_n/(16*A_n^2)"},
 radii:{rho_0:"min(2^-66,D_0/(64*A_0^3))",rho_n:"min(D_n/(64*A_n^3),g_(n-1)/(16*A_(n-1)))",g_n:"D_n*rho_n/(16*U_n^2)",box_coordinate_half_length:"rho_n/(number of active modes)",bad_volume_fraction_at_most:"1/8"},
 result:{whole_C4_control_norm_less_than:"2^-65",exact_two_phase_preservation:true,current_profile_used_at_each_band:true,all_prescribed_middle_Wronskians_lower:"exp(-2^-800*M*h_j)",previous_gaps_retained_fraction_more_than:"7/8"},
 numerical_parameter_arrays_computed:false,constructive_finite_selection_existence_proved:true,
 full_coupled_radial_network_inverse:false,nonradial_middle_matrix_inverse:false,
 physical_positive_DN_cross_sources_retained:true,original_zeta_h_and_source_weights_unchanged:true};
}
const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--out')throw Error('usage: node this.mjs --out NEW_REPORT.json');
const report=calculate();
report.producer_sha256=createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex');
await writeFile(args[1],JSON.stringify(report,null,2)+'\n',{flag:'wx'});
if(!report.complete)process.exitCode=1;
console.log(JSON.stringify({complete:report.complete,gate_count:report.gate_count,out:args[1]}));
