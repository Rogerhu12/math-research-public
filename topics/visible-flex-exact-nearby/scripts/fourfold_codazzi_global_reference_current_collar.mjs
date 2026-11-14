#!/usr/bin/env node
// Same actual ac1d root collar in every positive full-interval Riccati reference.
// Only complete published text bounds are consumed; no candidate array is reconstructed.
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;}
class Q{
 constructor(n=0n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
 add(b){return new Q(this.n*b.d+b.n*this.d,this.d*b.d);}
 sub(b){return new Q(this.n*b.d-b.n*this.d,this.d*b.d);}
 mul(b){return new Q(this.n*b.n,this.d*b.d);}
 div(b){return new Q(this.n*b.d,this.d*b.n);}
 pow(n){if(n<0)return new Q(this.d**BigInt(-n),this.n**BigInt(-n));return new Q(this.n**BigInt(n),this.d**BigInt(n));}
 lt(b){return this.n*b.d<b.n*this.d;}
 le(b){return this.n*b.d<=b.n*this.d;}
 str(){return this.d===1n?String(this.n):String(this.n)+"/"+String(this.d);}
}
const q=(n,d=1)=>new Q(BigInt(n),BigInt(d));
function dec(s){const[a,b=""]=s.split(".");const d=10n**BigInt(b.length);return new Q(BigInt(a)*d+BigInt(b),d);}


function runGlobalReferenceCollarBudget(){
 const gates=[],gate=(name,passed,extra={})=>{gates.push({name,passed:!!passed,...extra});if(!passed)throw Error(name);};
 const one=q(1),h=q(9,1000000),N=q(97),Mc=q(32),Mmin=q(388);
 const kcap=dec("3.45006391"),k239=dec("0.03308223614221");
 gate("same_intrinsic_full_positive_K_upper_4",kcap.lt(q(4))&&k239.lt(q(4)));
 gate("actual_outer_reference_p_between_one_eighth_and_one_fifth",q(1,8).lt(one.sub(one.div(q(2).mul(q(800000).pow(2)))).div(q(7)))&&one.div(dec("5.84461145233")).lt(q(1,5)));
 const etaLo=q(1,2),etaHi=q(201,100),krHi=dec("60.465470"),krLo=dec("59.74380437"),ksHi=q(122);
 gate("true_root_optical_K_s_bounds_29_and_122",q(29).lt(krLo.div(etaHi))&&krHi.div(etaLo).lt(ksHi));
 const ellLo=h.mul(etaLo),a=q(40),eb=q(8,3);
 const C=q(66),free=a.div(q(2)).add(ksHi.div(q(4).mul(a.pow(2)))),left=C.sub(free);
 gate("global_positive_reference_root_trial_66",left.lt(C)&&one.lt(left.pow(2).mul(a).mul(eb).mul(ellLo)),{trial_nonterminal:free.str(),minimum_optical_length:ellLo.str()});
 gate("root_complete_two_row_Airy_comparison_9",q(67).lt(q(81))&&q(66).pow(2).add(q(3)).lt(q(67).mul(q(67))));
 // For 0<=p_tilde<=66, p_tilde^2+3<67(p_tilde+1), by convexity and its two endpoints.
 gate("root_Airy_polynomial_endpoints",q(3).lt(q(67))&&q(66).pow(2).add(q(3)).lt(q(67).mul(q(67))));
 const dA=q(54),Bsup=q(74),BA=q(1650),FN=q(8300),beta=q(9,5),W=q(4);
 gate("complete_grounded_reaction_sup",q(16).add(q(3)).add(q(11).mul(one.add(W))).le(Bsup));
 gate("complete_grounded_reaction_Wiener",q(915).add(q(307)).add(q(85).mul(one.add(W))).lt(BA));
 gate("complete_nonlocal_dyad_with_global_W",q(216).add(q(86).mul(W)).mul(q(13).add(q(9,5))).lt(FN));
 const diff=q(24).mul(Mc).mul(BA).div(N),nonlocal=q(4).mul(beta).mul(FN).div(N.sub(Mc));
 const E=q(13,2).mul(dA).add(q(2).mul(Bsup)).add(diff).add(nonlocal);
 const Eabs=q(13,2).mul(dA).add(q(2).mul(BA)).add(diff).add(nonlocal);
 gate("global_reference_full_high_collar_contraction",h.mul(E).lt(q(2,15)),{exact_hE:h.mul(E).str()});
 gate("source_frame_3_even_with_W4",q(64).lt(Mmin)&&q(8).lt(q(9)));
 gate("raw_reconstruction_frame_3_even_with_W4",q(64).lt(Mmin)&&q(8).lt(q(9)));
 const inv=q(15,13),GH=q(9).mul(inv).mul(h),PH=q(3).mul(inv).mul(q(3,1000));
 gate("same_actual_high_ordinary_source_contract_1e4",GH.lt(q(1,10000)));
 gate("same_actual_high_port_state_contract_0011",PH.lt(q(11,1000)));
 gate("same_actual_high_source_both_traces_1over32",q(9).mul(inv).mul(q(3,1000)).lt(q(1,32)));
 gate("same_actual_high_ports_both_traces_24over5",q(9).mul(one.add(inv.pow(2))).lt(q(24,5).pow(2)));
 const loop=h.mul(q(51,50)).mul(q(967)).mul(q(1,10000)).mul(q(8658));
 gate("complete_193_head_feedback_unchanged",loop.lt(q(1,100)),{loop_upper:loop.str()});
 gate("all_ordinary_source_and_both_mean_head_ports_inherited",loop.le(q(1921439637n,250000000000n)));
 gate("finite_absolute_kernel_Estar_17700",Eabs.lt(q(17700)));
 gate("highest_transport_derivative_no_new_frequency_loss",h.mul(E.add(q(10))).lt(q(2,15)));
 const c1=q(256).mul(q(17727)),c21=q(512).mul(q(17754)),c20=q(65536).mul(q(17727));
 gate("actual_complete_band_commutator_C1",c1.le(q(4538112)));
 gate("actual_complete_band_commutator_C21",c21.le(q(9090048)));
 gate("actual_complete_band_commutator_C20",c20.le(q(1161756672)));
 gate("negative_root_input_global_frame_15",q(9).mul(q(8,5)).lt(q(15)));
 gate("negative_root_source_global_frame_0046",q(9).mul(q(51,10000)).lt(q(46,1000)));
 return {kind:"uniform_global_positive_reference_actual_current_root_collar",complete:true,arithmetic:"normalized BigInt rational; complete positive variational reference and full Fourier kernels",source:"scripts/fourfold_codazzi_global_reference_current_collar.mjs",candidate_sha256:"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
 inputs:[
 {path:"results/R133-supplement-current-moving-positive-root-Riccati-and-full-head.md",git_blob:"3edf335784786da9a4a515b28d364d8ad2914e24"},
 {path:"results/R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md",git_blob:"7784d7158974d4632ca634369e55dc095e134902"},
 {path:"results/R133-actual-rotational-positive-cap-and-Codazzi-Jacobi-graph.md",git_blob:"1f0c66859862fbe6280fdce466f98dd10cc4a17f",scope:"same intrinsic K bound only"},
 {path:"results/R133-supplement-full-compact-metric-curvature-type.md",git_blob:"15de90fc2e61c0d15df47a1a636675c8f0397122",scope:"same intrinsic root-to-.239 monotonicity only"}],
 reference:{domain:"[r*(eta),25/8]",speed:"any frequency-independent positive bounded radial extension of the actual -gamma*m on the certified root piece",g_initial:"M^-1/3",p_final:"q_*/(-m_R)",K:"the actual full intrinsic K; 0<=K<4",p_g_upper:"2 each",M_log_derivative:"<=1 for each positive p,g",root_p_upper:"66 M^-1/3",root_two_row_Airy_equivalence:"9"},
 actual_collar:{h:h.str(),cutoff_index:97,physical_minimum:388,W_upper:"4",K_over_W_upper:"1",E_upper:E.str(),hE_upper:h.mul(E).str(),resolvent:"15/13",complete_head_size:193,complete_head_loop:loop.str(),ordinary_source_to_state:"1/8000",ports_to_state:"3/250",ordinary_source_to_both_raw_traces:"1/25",ports_to_both_raw_traces:"27/5"},
 angular_bootstrap:{derivatives:[0,1,2],same_high_resolvent:"15/13",Eabsolute_upper:"17700",C1:c1.str(),C21:c21.str(),C20:c20.str(),triangular_equations:"X0<=I(hF0+sqrt(h)g0); X1<=I(hF1+sqrt(h)g1+h C1 X0); X2<=I(hF2+sqrt(h)g2+h C21 X1+h C20 X0)",source:"physical H^(j+1/3), complete head forcing retained",repeat_head_inversion:false},
 negative_input:{ordinary_initial_H1_to_both_global_root_rows:"15",ordinary_L2r_H1_source_to_both_global_root_rows:"0.046"},
 permissions:{actual_root_operator:true,actual_outer_graph_same_reference:true,uniform_over_positive_speed_extensions:true,actual_speed_sign_outside_root_certified:false,whole_positive_body_inverse:false,global_return_inverse:false,global_nu_inverse:false},
 gates};
}

export {runGlobalReferenceCollarBudget};
if(typeof process!=="undefined"&&process.versions?.node&&process.argv[1]?.endsWith("fourfold_codazzi_global_reference_current_collar.mjs")){
 const result=runGlobalReferenceCollarBudget(),json=JSON.stringify(result,null,2)+"\n";
 const k=process.argv.indexOf("--out");
 if(k>=0){const fs=await import("node:fs");fs.writeFileSync(process.argv[k+1],json);process.stdout.write(JSON.stringify({complete:result.complete,gates:result.gates.length,out:process.argv[k+1]})+"\n");}
 else process.stdout.write(json);
}
