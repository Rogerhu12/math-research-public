#!/usr/bin/env node
/** Actual middle-width payment of the full radial transversality cost. */
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
function calculate(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
 const q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};};
 const add=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d),sub=(a,b)=>q(a.n*b.d-b.n*a.d,a.d*b.d),mul=(a,b)=>q(a.n*b.n,a.d*b.d);
 const two=k=>q(2n**BigInt(k)),cmp=(a,b)=>a.n*b.d-b.n*a.d,str=a=>a.n+"/"+a.d;
 const gates=[],gate=(name,a,b,relation="lt")=>gates.push({name,left:str(a),right:str(b),relation,pass:relation==="eq"?cmp(a,b)===0n:cmp(a,b)<0n});
 const j=8193n,J=j+5n;
 gate("delta_log_lower",q(8),q(25,2));
 gate("delta_log_upper",q(25,2),q(16));
 gate("middle_threshold_exponent_is_greater_than_two",q(2),sub(q(j+3n,8),q(40)));
 gate("first_J_is_below_2pow14",q(J),two(14));
 gate("first_layer_exponent_is_above_14",q(14),q(j,512));
 gate("J_induction_geometric_series_ratio_below_one",q(512,J),q(1));
 gate("J_induction_512_power_below_two",q(J,J-512n),q(2));
 gate("constant_log_fee",two(27),mul(two(14),q(J)));
 gate("delta_log_fee",q(285554),two(19));
 gate("J_log_fee",q(144890),two(18));
 gate("all_layer_only_fees",add(add(two(74),two(19)),add(two(18),two(14))),two(75));
 gate("frequency_log_coefficient",q(19966,8),two(12));
 gate("threshold_reciprocal_bit",q(40+75),q(115),"eq");
 gate("frequency_log_reciprocal_bit",q(40+12),q(52),"eq");
 gate("two_nonfrequency_terms",add(two(115),two(52)),two(116));
 gate("layer_delta_exponent",sub(sub(q(1,8),q(1,256)),q(1,512)),q(61,512),"eq");
 gate("frequency_delta_exponent",sub(sub(q(3,4),q(1,256)),q(1,1024)),q(763,1024),"eq");
 gate("first_layer_only_width_fee_less_than_2pow_minus801",q((116n+801n)*512n),q(61n*j));
 gate("first_frequency_width_fee_less_than_2pow_minus801",q((71n+801n)*1024n),q(763n*j));
 gate("sum_of_two_width_fees",q(2,2n**801n),q(1,2n**800n),"eq");
 gate("conversion_to_original_h",q(1,8n*2n**800n),q(1,2n**803n),"eq");
 return {kind:"actual_middle_angular_width_payment_for_compensated_radial_transversality",
 complete:gates.every(x=>x.pass),executed:true,arithmetic:"normalized exact BigInt rational",gate_count:gates.length,gates,
 inputs:{kernel_separation_proof_blob:"8b5e908a0da26a3a6038de2808cbe41c9849f439",compact_control_proof_blob:"5662bf40391a53a2212311406cf7ad63064908fc",compact_control_result:"R119-supplement-quantitative-phase-preserving-compact-control.md",controlled_full_label_proof_blob:"f11edbccd752bf034aa40e71888859d667a04b42"},
 domain:{j_min:"8193",delta:"(2/25)*2^-j",J:"j+5",magnitude_min:"2^-40*delta^-1/8",original_h:"8*delta^1/256"},
 old_derivative_lower:"2^(-2^27)*delta^285554*(j+5)^-144890*M^-19966*exp(-2^74*(j+5)-2^71*M*delta^3/4*sqrt(j+5))",
 log_reciprocal_upper:"2^-800*M*delta^1/256 = 2^-803*M*h_j",
 resulting_derivative_lower:"exp(-2^-803*M*h_j)",
 whole_window_proved:true,all_modes_below_middle_covered:false,finite_parameter_bad_set_proved:false,
 coupled_nonradial_matrix_inverted:false,original_zeta_and_h_unchanged:true,radial_low_source_weight_changed:false};
}
const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--out')throw Error('usage: node this.mjs --out NEW_REPORT.json');
const report=calculate();
report.producer_sha256=createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex');
await writeFile(args[1],JSON.stringify(report,null,2)+'\n',{flag:'wx'});
if(!report.complete)process.exitCode=1;
console.log(JSON.stringify({complete:report.complete,gate_count:report.gate_count,out:args[1]}));
