#!/usr/bin/env node
/** Complete ordinary Sobolev source budget for the actual moving root. */
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
function calculate(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
 const q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return{n:n/g,d:d/g};};
 const add=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d),mul=(a,b)=>q(a.n*b.n,a.d*b.d),pow=(a,k)=>q(a.n**BigInt(k),a.d**BigInt(k));
 const lt=(a,b)=>a.n*b.d<b.n*a.d,str=a=>a.n+"/"+a.d;
 const gates=[],gate=(name,a,b)=>gates.push({name,left:str(a),right:str(b),pass:lt(a,b)});
 const rho=q(1,1000000),b=q(9,5),g=q(9,5),B0=q(74,5),B43=mul(B0,q(652)),B73=mul(B43,q(129));
 const remainder=B=>add(add(mul(mul(q(15,4),b),B),mul(mul(q(5,4),b),rho)),g);
 const difference=B=>add(add(mul(mul(q(15,2),b),B),mul(mul(q(15,4),b),rho)),mul(q(2),g));
 const mean=mul(b,add(add(q(28,25),mul(q(2),B0)),rho));
 const meanD=mul(b,add(add(q(56,25),mul(q(4),B0)),mul(q(3),rho)));
 gate("actual_degree_32_four_thirds_weight",pow(q(129),4),pow(q(652),3));
 gate("H_one_third_source_quadratic_coefficient",remainder(B43),q(66000));
 gate("H_one_third_source_Jacobian_difference",difference(B43),q(132000));
 gate("H_four_thirds_source_quadratic_coefficient",remainder(B73),q(8500000));
 gate("H_four_thirds_source_Jacobian_difference",difference(B73),q(17000000));
 gate("complete_even_mean_quadratic_coefficient",mean,q(56));
 gate("complete_even_mean_Jacobian_difference",meanD,q(112));
 const source=mul(q(3,1000),q(66000));
 gate("one_true_root_L2_response_per_radius_squared",mul(q(1,8000),source),q(1,40));
 gate("one_true_root_both_raw_traces_per_radius_squared",mul(q(1,25),source),q(8));
 return{
 kind:"complete_moving_Sobolev_flux_and_actual_root_source_budget",
 complete:gates.every(x=>x.pass),executed:true,arithmetic:"normalized exact BigInt rational",gate_count:gates.length,gates,
 candidate_sha256:"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
 unknown_norm:"sup_r A^3 with vector component l1 sum and weight (1+abs(k))^3",
 radius:str(rho),source_norms:["ordinary Bessel H^(1/3)","ordinary Bessel H^(4/3)"],
 high_state_norms:["X_(4/3)","X_(7/3)"],X_s:"Fourier l2 with polynomial weight (1+abs(k))^s, vector component l1 sum",
 centre_bounds:{A0:str(B0),A_four_thirds:str(B43),A_seven_thirds:str(B73)},
 exact_coefficients:{quadratic_H_one_third:str(remainder(B43)),Jacobian_H_one_third:str(difference(B43)),quadratic_H_four_thirds:str(remainder(B73)),Jacobian_H_four_thirds:str(difference(B73)),complete_even_mean:str(mean),complete_even_mean_derivative:str(meanD)},
 whole_unknown_Fourier_tail:true,complete_mean_retained:true,complete_primitive_retained:true,
 joint_metric_remainder_formula_proved:true,joint_metric_full_body_coefficients_certified:false,
 physical_normalized_second_reference_jet_retained:true,
 source_to_output_total_angular_loss:"4/3 at every stated root Sobolev level",
 root_response_has_zero_linear_ports:true,nonlinear_port_remainders_are_separate:true,
 same_space_contraction_proved:false,full_BVP_inverse_proved:false,
 inputs:[
 {path:"results/R133-supplement-complete-moving-nonlinear-flux-and-metric-remainder.md",producer_sha256:"4031c37716812d50fd78650c6c1352fec245ed36fad7d3de1ea24b9edc0af06a",used:"N.4-N.7 exact full flux and mean; N.15-N.23 exact metric and normalized background"},
 {path:"results/R133-supplement-global-positive-reference-and-current-collar.md",git_blob:"5e89a2ec36f36f2852d47738bc46373fdacf67d1",used:"G.1 actual complete-root source and two raw traces"},
 {path:"results/R133-supplement-current-moving-positive-root-Riccati-and-full-head.md",used:"P.7-P.8 exact current-centre mean and A0 bounds"}
 ]
 };
}
const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--out')throw Error('usage: node this.mjs --out NEW_REPORT.json');
const report=calculate();
report.producer_sha256=createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex');
await writeFile(args[1],JSON.stringify(report,null,2)+'\n',{flag:'wx'});
if(!report.complete)process.exitCode=1;
console.log(JSON.stringify({complete:report.complete,gate_count:report.gate_count,out:args[1]}));
