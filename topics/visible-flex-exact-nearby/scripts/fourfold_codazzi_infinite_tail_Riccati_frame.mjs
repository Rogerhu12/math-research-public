#!/usr/bin/env node
/** Full signed-frequency frame and actual infinite-tail budget. */
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
function calculate(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
 const q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return{n:n/g,d:d/g};};
 const add=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d);
 const mul=(a,b)=>q(a.n*b.n,a.d*b.d);
 const pow=(a,k)=>q(a.n**BigInt(k),a.d**BigInt(k));
 const lt=(a,b)=>a.n*b.d<b.n*a.d;
 const eq=(a,b)=>a.n*b.d===b.n*a.d;
 const str=a=>a.n.toString()+"/"+a.d.toString();
 const gates=[];const gate=(name,left,right,relation="lt")=>gates.push({name,left:str(left),right:str(right),relation,pass:relation==="eq"?eq(left,right):lt(left,right)});
 const b=q(9,5),U=q(26),V=q(18,5),Up=q(432),Vp=q(172),rho=q(1,1000000);
 const drift=[mul(b,add(mul(q(2),U),mul(q(2),V))),mul(b,q(2))];
 const a=[mul(b,add(mul(q(6),U),mul(q(2),V))),mul(b,q(4))];
 const e=[mul(b,add(mul(q(2),U),mul(q(6),V))),mul(b,q(4))];
 const bc=[mul(mul(q(2),b),add(U,V)),mul(q(2),b)];
 const reaction=[0,1].map(j=>mul(q(2),add(add(a[j],e[j]),mul(q(5),bc[j]))));
 const primitive=[mul(b,add(add(add(Up,U),add(Vp,V)),add(add(Up,V),mul(q(4),add(Vp,U))))),mul(b,q(7))];
 const transport=drift.map(x=>mul(q(17,2),x));
 const full=[0,1].map(j=>add(add(transport[j],reaction[j]),primitive[j]));
 const comm=[mul(q(129),full[0]),full[1]];
 const commTransport=[mul(q(129,2),drift[0]),mul(q(1,2),drift[1])];
 const c1=[add(comm[0],commTransport[0]),add(comm[1],commTransport[1])];
 const atRho=p=>add(p[0],mul(p[1],rho));
 gate("signed_frame_constant_squared",q(8),q(9));
 gate("neighbouring_transport_constant_cubed",mul(pow(q(5,3),3),q(32)),q(216));
 gate("centre_mode_32_weight_cube",pow(q(129,97),2),q(8));
 gate("global_frame_D_bound_squared",q(3),q(4));
 gate("drift_linear_exact",drift[0],q(2664,25),"eq");
 gate("drift_quadratic_exact",drift[1],q(18,5),"eq");
 gate("transport_linear_exact",transport[0],q(22644,25),"eq");
 gate("transport_quadratic_exact",transport[1],q(153,5),"eq");
 gate("reaction_linear_exact",reaction[0],q(47952,25),"eq");
 gate("reaction_quadratic_exact",reaction[1],q(324,5),"eq");
 gate("primitive_linear_exact",primitive[0],q(83754,25),"eq");
 gate("primitive_quadratic_exact",primitive[1],q(63,5),"eq");
 gate("complete_high_remainder_linear_exact",full[0],q(6174),"eq");
 gate("complete_high_remainder_quadratic_exact",full[1],q(108),"eq");
 gate("complete_high_remainder_per_rho_below_6200",atRho(full),q(6200));
 gate("first_commutator_linear_exact",comm[0],q(796446),"eq");
 gate("first_commutator_per_rho_below_800000",atRho(comm),q(800000));
 gate("first_triangular_forcing_per_rho_below_810000",atRho(c1),q(810000));
 gate("highest_transport_coefficient_per_rho_below_110",atRho(drift),q(110));
 const E=q(18262183,1261),h=q(9,1000000),newE=add(E,mul(q(6200),rho));
 gate("base_high_contraction_survives",mul(h,newE),q(2,15));
 gate("H1_high_contraction_survives",mul(h,add(newE,add(q(5),mul(q(110),rho)))),q(2,15));
 const asPoly=p=>({linear:str(p[0]),quadratic:str(p[1])});
 return{
 kind:"all_signed_frequency_Riccati_frame_and_infinite_tail_budget",
 complete:gates.every(x=>x.pass),executed:true,arithmetic:"normalized exact BigInt rational",
 gate_count:gates.length,gates,
 domain:{physical_frequencies:"4j",high_min_abs_frequency:388,weight:"(1+abs(k)/388)^(2/3)",state_radius:str(rho),state_norm:"A^3=l1 sum (1+abs(k))^3 of both moving components",candidate_sha256:"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"},
 bounds:{frame_all_signs:"3 R^(2/3)",transport_after_exact_skew:"(17/2) norm(d_phi)_A_w",local_reaction:"2 (norm(a)+norm(e)+norm(b)+4 norm(c))_A_w",drift:asPoly(drift),transport:asPoly(transport),reaction:asPoly(reaction),complete_primitive:asPoly(primitive),complete_high_remainder:asPoly(full),first_commutator:asPoly(comm),first_triangular_lower_forcing:asPoly(c1)},
 reference_hypotheses:{positive_p_and_g:true,W_at_most_4:true,K_over_W_at_most_1:true,log_frequency_derivatives_at_most_1:true,principal_speed_is_actual_perturbed_mean:true},
 inputs:[
 {path:"results/R133-supplement-global-positive-reference-and-current-collar.md",git_blob:"5e89a2ec36f36f2852d47738bc46373fdacf67d1",used:"G.9-G.10,G.15-G.22; same full reference and actual centre budgets"},
 {path:"results/R133-supplement-complete-moving-band-and-mean-parameter-Schur.md",git_blob:"a51dbc432d2945bad9a7deb5d985ca021676030b",used:"B.3-B.4 full derivative, primitive and mean rank"},
 {path:"results/R133-supplement-current-moving-positive-root-Riccati-and-full-head.md",used:"P.8 current-centre complete A0 fields"}
 ],
 both_frequency_signs:true,infinite_unknown_tail_retained:true,primitive_intermediate_zero_removed_only:true,mean_rank_high_to_high_zero_by_input_mean_only:true,
 low_high_and_mean_couplings_are_separate:true,full_BVP_inverse_proved:false,nonlinear_contraction_proved:false,
 radial_candidate_native_reconstructed:false
 };
}
const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--out')throw Error('usage: node this.mjs --out NEW_REPORT.json');
const report=calculate();
report.producer_sha256=createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex');
await writeFile(args[1],JSON.stringify(report,null,2)+'\n',{flag:'wx'});
if(!report.complete)process.exitCode=1;
console.log(JSON.stringify({complete:report.complete,gate_count:report.gate_count,out:args[1]}));
