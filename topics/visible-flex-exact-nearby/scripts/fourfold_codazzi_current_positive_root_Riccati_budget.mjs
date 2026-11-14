#!/usr/bin/env node
// Current ac1d... moving positive-root all-frequency contract.
// Pure normalized rational arithmetic. Inputs are proved outward text bounds;
// no binary native reports or sampled candidate coefficients are read.
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
function runBudget(){
 const gates=[],g=(name,yes,values={})=>{gates.push({name,passed:!!yes,...values});if(!yes)throw Error(name);};
 const M=32,N=97,h=q(9,1000000),sqrtH=q(3,1000),one=q(1);
 const rlo=dec("0.2383968742994"),rhi=dec("0.2383968743003"),R=q(1,100000);
 const left=q(2147184947341121n,9007199254740992n),right=q(4295308144604611n,18014398509481984n);
 const mgap=dec("1.1197077044"),mupper=dec("1.119807069"),thetaDerivativeExcess=dec("0.599103154");
 const physicalAlo=dec("0.5025436590"),physicalAhi=dec("2.004892");
 const D0=dec("0.705336"),D1=dec("7.302797");
 const KprimeLo=dec("59.74380437"),KprimeHi=dec("60.465470");
 const etaLo=q(1,2),etaHi=q(201,100),gammaLo=q(25,56),betaHi=q(9,5);
 const uSup=q(8,5),vA0=q(9,5),uA0=q(13),u1A0=q(216),v1A0=q(86);
 const Kmax=q(61,100000),KoptLo=q(29),KoptHi=q(122);
 g("h_square_root_exact",sqrtH.pow(2).le(h)&&h.le(sqrtH.pow(2)));
 g("root_union_and_h_strictly_inside_actual_piece",left.lt(rlo.sub(R))&&rhi.add(R).lt(right)&&rhi.add(h).lt(right));
 g("strict_complex_margin_includes_root_enclosure",h.add(rhi.sub(rlo)).lt(R)&&q(9,10000000).lt(R.sub(h).sub(rhi.sub(rlo))));
 g("eta_from_actual_physical_a_and_mean",etaLo.lt(physicalAlo)&&physicalAhi.lt(etaHi));
 g("gamma_lower_from_eta_mean",mupper.lt(q(28,25))&&gammaLo.le(etaLo.div(q(28,25))));
 g("gamma_upper_and_rotational_gap_beta_budget",etaHi.div(mgap).lt(betaHi));
 g("actual_u_real_sup",D0.div(gammaLo).lt(uSup));
 g("actual_u_phi_real_sup",q(8,5).mul(D1).div(gammaLo).lt(q(27)));
 g("finite_u_A0_and_A1",q(8).mul(uSup).lt(uA0)&&q(8).mul(q(27)).le(u1A0));
 g("complete_v_A0",mupper.mul(one.add(thetaDerivativeExcess)).lt(vA0));
 g("complete_v_A1",q(128).mul(mupper).mul(thetaDerivativeExcess).lt(v1A0));
 g("actual_positive_K_and_optical_slope",KprimeHi.mul(h).lt(Kmax)&&KoptLo.lt(KprimeLo.div(etaHi))&&KprimeHi.div(etaLo).lt(KoptHi));
 g("Kmax_below_one_over_1600",Kmax.lt(q(1,1600)));
 g("frequency_ratio_bound",N>=2*M);
 g("reference_W_upper_below_one_third",q(6).pow(3).lt(q(4*N))&&Kmax.lt(q(1,36)));
 g("reference_K_over_W_comparison_constants",q(366).lt(q(8).pow(3))&&q(366).div(KoptLo).lt(q(13))&&q(21,40).lt(one));
 g("tanh_one_lower_by_positive_exponential_series",q(1).add(q(2)).add(q(2)).add(q(4,3)).add(q(2,3)).add(q(4,15)).lt(q(8))&&q(7).lt(q(1).add(q(2)).add(q(2)).add(q(4,3)).add(q(2,3)).add(q(4,15))));
 g("uniform_W_lower_barrier",q(1,2).lt(q(2,3))&&q(1,4).lt(KoptLo.mul(q(1,2))));
 g("Wronskian_log_frequency_bound",q(3,2).lt(q(3,2).pow(2)));
 g("Airy_weighted_frequency_constants",q(5,3).pow(3).mul(q(4)).lt(q(3).pow(3))&&q(5,3).pow(3).mul(q(32)).lt(q(6).pow(3)));
 const Ssup=q(13,5);
 g("S_sup_from_complete_real_fields",uSup.pow(2).add(Kmax.mul(vA0.pow(2))).lt(Ssup));
 g("sqrt_128_below_23_over_2",q(128).lt(q(23,2).pow(2)));
 const a1=q(54);
 g("full_d_phi_Wiener_budget",betaHi.mul(q(23,2)).mul(Ssup).lt(a1));
 g("reaction_a_sup_16",betaHi.mul(one.add(q(3).mul(uSup.pow(2))).add(Kmax.mul(vA0.pow(2)))).lt(q(16)));
 g("reaction_e_sup_3",betaHi.mul(uSup.pow(2).add(q(3).mul(Kmax).mul(vA0.pow(2))).sub(one)).lt(q(3))&&betaHi.lt(q(3)));
 g("reaction_offdiag_sup_11",q(2).mul(betaHi).mul(uSup).mul(vA0).lt(q(11)));
 g("reaction_a_Wiener_915",betaHi.mul(one.add(q(3).mul(uA0.pow(2))).add(Kmax.mul(vA0.pow(2)))).lt(q(915)));
 g("reaction_e_Wiener_307",betaHi.mul(one.add(uA0.pow(2)).add(q(3).mul(Kmax).mul(vA0.pow(2)))).lt(q(307)));
 g("reaction_offdiag_Wiener_85",q(2).mul(betaHi).mul(uA0).mul(vA0).lt(q(85)));
 const Binfty=q(34),BA=q(1336),F=q(3700);
 g("whole_weighted_reaction_infinity_34",q(16).add(q(3)).add(q(11).mul(q(4,3))).lt(Binfty));
 g("whole_weighted_reaction_Wiener_1336",q(915).add(q(307)).add(q(85).mul(q(4,3))).lt(BA));
 g("complete_nonlocal_weighted_product_3700",u1A0.add(v1A0.div(q(3))).mul(uA0.add(vA0)).lt(F));
 const Es=[];
 for(const s of[0,1,2]){
  const drift=[6,18,48][s],diff=[3,9,24][s],nonlocal=[4,8,16][s];
  const E=q(drift).add(q(1,2)).mul(a1).add(q(2).mul(Binfty))
    .add(q(8*diff*M,N).mul(BA)).add(q(nonlocal,N-M).mul(betaHi).mul(F));
  Es.push(E);
 }
 g("E0_below_11408",Es[0].lt(q(11408)),{exact_upper:Es[0].str()});
 g("same_space_base_contraction_below_one_eighth",h.mul(Es[0]).lt(q(1,8)));
 g("H1_contraction_below_one_third",h.mul(Es[1]).lt(q(1,3)),{exact_upper:Es[1].str()});
 g("H2_contraction_below_five_sixths",h.mul(Es[2]).lt(q(5,6)),{exact_upper:Es[2].str()});
 g("H1_H2_frequency_commutator_constants",
   q(8,3).pow(3).mul(q(256)).lt(q(18).pow(3))&&
   q(8,3).pow(3).mul(q(32)).lt(q(9).pow(3))&&
   q(11,3).pow(3).mul(q(2048)).lt(q(48).pow(3))&&
   q(11,3).pow(3).mul(q(256)).lt(q(24).pow(3)));
 g("source_and_state_factor_3",q(8).lt(q(9)));
 const res=q(8,7),Ghigh=q(1,10000),Phigh=q(11,1000);
 g("ordinary_moving_high_source_gain_below_one_over_10000",q(9).mul(res).mul(h).lt(Ghigh));
 g("ordinary_moving_high_port_gain_below_011",q(3).mul(res).mul(sqrtH).lt(Phigh));
 g("complete_high_trace_source_below_one_over_32",q(9).mul(res).mul(sqrtH).lt(q(1,32)));
 g("complete_high_trace_port_below_24_over_5",one.add(res.pow(2)).lt(q(8,5).pow(2)));
 const rootTrial=q(2).add(KoptHi.div(q(64))).add(one);
 g("root_reference_two_way_Airy_frame_factor_5",rootTrial.lt(q(5))&&q(24).lt(q(25)));
 g("right_reference_two_way_soft_Airy_frame_factor_6",q(65).lt(q(9).pow(2)));
 // Exact complete finite-head couplings; this is not a finite QR inverse.
 g("drift_sup_below_2",q(2,5).mul(betaHi).mul(Ssup).lt(q(2)));
 g("d_phi_sup_below_5",betaHi.mul(Ssup).lt(q(5)));
 g("complete_local_raw_matrix_below_31",q(16).add(q(3)).add(q(11)).add(Kmax.mul(q(11))).lt(q(31)));
 const row= uSup.add(Kmax.mul(vA0)),col=q(27).add(v1A0);
 g("full_primitive_nonlocal_part_below_163",betaHi.div(q(2)).mul(row).mul(col).lt(q(163)));
 g("true_mean_rank_part_below_49",betaHi.mul(q(27).add(Kmax.mul(v1A0))).lt(q(49)));
 const AHL=q(962),ALH=q(967),AHs=q(8658);
 g("full_head_high_L2_and_Hthird_couplings",q(4*(N-1)*2+31+163).le(AHL)&&q(4*(N-1)*2+5+31+163).le(ALH)&&q(9).mul(AHL).le(AHs));
 g("complete_high_shell_Hthird_factor_9",q(1+640*640).lt(q(9).pow(6)));
 g("finite_head_full_generator_below_1800",q(4*(N-1)).mul(etaHi).add(q(4*(N-1)*2+31+212)).lt(q(1800)));
 const EL=q(51,50),x=q(1800).mul(h);
 g("head_exponential_by_geometric_majorant",one.div(one.sub(x)).lt(EL));
 const GL=h.mul(EL),PL=sqrtH.mul(EL),rho=GL.mul(ALH).mul(Ghigh).mul(AHs);
 g("complete_low_high_return_contraction_below_one_percent",rho.lt(q(1,100)),{exact_upper:rho.str()});
 const inv=q(100,99);
 const lfL=inv.mul(GL),lfH=inv.mul(GL).mul(ALH).mul(Ghigh);
 const lgL=inv.mul(PL),lgH=inv.mul(GL).mul(ALH).mul(Phigh);
 g("complete_head_response_matrix",lfL.lt(q(1,100000))&&lfH.lt(q(1,1000000))&&lgL.lt(q(31,10000))&&lgH.lt(q(1,10000)));
 const hfL=Ghigh.mul(AHs).mul(q(1,100000));
 const hfH=Ghigh.add(Ghigh.mul(AHs).mul(q(1,1000000)));
 const hgL=Ghigh.mul(AHs).mul(q(31,10000)),hgH=Phigh.add(Ghigh.mul(AHs).mul(q(1,10000)));
 g("complete_high_response_matrix",hfL.lt(q(87,10000000))&&hfH.lt(q(102,1000000))&&hgL.lt(q(269,100000))&&hgH.lt(q(111,10000)));
 const fullSource=q(1,100000).add(q(1,1000000)).add(q(87,10000000)).add(q(102,1000000));
 g("whole_frequency_source_gain_below_one_over_8000",fullSource.lt(q(1,8000)));
 const portFrob=q(31,10000).pow(2).add(q(1,10000).pow(2)).add(q(269,100000).pow(2)).add(q(111,10000).pow(2));
 g("whole_frequency_port_gain_below_012",portFrob.lt(q(3,250).pow(2)));
 // Full endpoint traces, including the two retained low means.
 const lowRightF=sqrtH.mul(EL).mul(one.add(ALH.mul(q(87,10000000).add(q(102,1000000)))));
 const lowRightGL=EL.add(sqrtH.mul(EL).mul(ALH).mul(q(269,100000)));
 const lowRightGH=sqrtH.mul(EL).mul(ALH).mul(q(111,10000));
 g("complete_low_right_trace",lowRightF.lt(q(1,250))&&lowRightGL.lt(q(103,100))&&lowRightGH.lt(q(17,500)));
 const highTrF=q(1,32).mul(one.add(AHs.mul(q(1,100000).add(q(1,1000000)))));
 const highTrGL=q(1,32).mul(AHs).mul(q(31,10000));
 const highTrGH=q(24,5).add(q(1,32).mul(AHs).mul(q(1,10000)));
 g("complete_high_two_end_trace",highTrF.lt(q(7,200))&&highTrGL.lt(q(21,25))&&highTrGH.lt(q(483,100)));
 g("low_two_end_port_factor_144",one.add(q(103,100).pow(2)).lt(q(36,25).pow(2)));
 const tracePort2=q(36,25).add(q(21,25)).pow(2).add(q(17,500).add(q(483,100)).pow(2));
 g("whole_frequency_two_end_trace",q(1,250).add(q(7,200)).lt(q(1,25))&&tracePort2.lt(q(27,5).pow(2)));
 return {
  kind:"actual_current_moving_positive_root_Riccati_all_frequency_contract",
  complete:true,arithmetic:"normalized BigInt rational inequalities; no binary native reads",
  candidate_sha256:"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
  source:"scripts/fourfold_codazzi_current_positive_root_Riccati_budget.mjs",
  inputs:[
   {path:"results/R133-supplement-current-moving-body-physical-complex-germ.md",git_blob:"bfe73ee59142618bc7e36d5e3fe06929d9fb68cb",scope:"all current-centre quantities used here"},
   {path:"results/R133-supplement-actual-physical-fold-and-full-Airy-collar.md",git_blob:"90daf082281a7dfd6616f62e5c187795bf2324ea",scope:"only same intrinsic whole-eta Kprime bound, no old nonradial quantity"},
   {path:"results/R133-supplement-complete-moving-band-and-mean-parameter-Schur.md",git_blob:"a51dbc432d2945bad9a7deb5d985ca021676030b",scope:"complete moving operator, band, parameter, mean, physical boundary formulas"}
  ],
  domain:{left:"the true current intrinsic root r*(eta)",right:"r*(eta)+9/1000000",whole_original_eta:true,one_actual_PPoly_piece:2549,joins_inside:false},
  high:{first_index:N,first_physical_frequency:4*N,complete_unbounded_frequency_set:true,reference:"true positive scalar Riccati/Wronskian DN at both ends; Robin M^(2/3)",full_E_upper:Es[0].str(),contraction_upper:h.mul(Es[0]).str(),base_resolvent:"8/7",H1_resolvent:"3/2",H2_resolvent:"6"},
  head:{max_index:N-1,reflection_dimension:2*(N-1)+1,with_global_scalar_parameter:2*(N-1)+2,all_allowed_means_retained:true,shell_first_index:N-2*M,shell_last_index:N-1,complete_schur_contraction_upper:rho.str()},
  all_frequency_bounds:{source_L2r_Hthird_to_state_L2:"1/8000",incoming_ports_to_state_L2:"3/250",source_to_complete_two_end_raw_moving_traces:"1/25",incoming_ports_to_complete_two_end_raw_moving_traces:"27/5"},
  ports:{low:"both complete head Cauchy rows at the true root, including means",high:"stable reference row at true root and unstable reference row at right endpoint",root_soft_Airy_frame_both_directions:"5",right_soft_Airy_frame_both_directions:"6"},
  permissions:{same_moving_operator:true,physical_theta_variation_bridge_paid_by_this_report:false,negative_return_paid:false,whole_positive_body_paid:false,exterior_regular_graph_paid:false,nonlinear_full_BVP_paid:false},
  gates
 };
}
export {runBudget};
// NODE CLI; the exact core above also runs unchanged in a JS isolate.
if(typeof process!=="undefined"&&process.versions?.node&&process.argv[1]?.endsWith("fourfold_codazzi_current_positive_root_Riccati_budget.mjs")){
 const result=runBudget(),json=JSON.stringify(result,null,2)+"\n";
 const k=process.argv.indexOf("--out");
 if(k>=0){const fs=await import("node:fs");fs.writeFileSync(process.argv[k+1],json);process.stdout.write(JSON.stringify({complete:result.complete,gates:result.gates.length,out:process.argv[k+1]})+"\n");}
 else process.stdout.write(json);
}
