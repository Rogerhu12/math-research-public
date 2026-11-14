#!/usr/bin/env node
// Uniform current moving positive-root inverse with an arbitrary A^3 Fourier tail.
// Inputs are explicitly bound, proved whole-object text envelopes. No binary native reports are read.
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



function runNearbyRootInverseBudget(){
 const gates=[],gate=(name,ok,extra={})=>{gates.push({name,passed:!!ok,...extra});if(!ok)throw Error(name);};
 const one=q(1),rho=q(1,1000000),h=q(9,1000000),sqrtH=q(3,1000);
 const beta=q(9,5),K=q(61,100000),U=q(8,5),V=q(9,5),U1=q(27),V1=q(86);
 const Ec=q(18262183,1261),highInv=q(15,13);
 const dE=q(6200).mul(rho),dAd=q(810000).mul(rho);
 gate("perturbed_real_mean_speed_stays_in_actual_open_interval",
  q(1,2).lt(dec("0.5025436590").sub(beta.mul(rho)))&&dec("2.004892").add(beta.mul(rho)).lt(q(201,100)));
 gate("perturbed_real_mean_stays_negative",q(1).lt(dec("1.1197077044").sub(rho)));
 gate("perturbed_physical_angle_remains_positive",dec("1.119807069").add(rho).lt(q(28,25))&&q(2,5).lt(one.sub(dec("0.599103154")).mul(dec("1.1197077044")).sub(rho)));
 gate("HH_tail_and_first_commutator_input_bounds",
  q(6174).mul(rho).add(q(108).mul(rho.pow(2))).lt(dE)&&q(796446).mul(rho).add(q(108).mul(rho.pow(2))).add(q(129).mul(q(2664,25)).mul(rho).add(q(18,5).mul(rho.pow(2))).div(q(2))).lt(dAd));
 gate("same_actual_HH_resolvent_after_infinite_tail",h.mul(Ec.add(dE)).lt(q(2,15)));
 gate("one_angular_derivative_same_resolvent",h.mul(Ec.add(dE).add(q(5)).add(q(110).mul(rho))).lt(q(2,15)));
 const du2=q(2).mul(U).mul(rho).add(rho.pow(2));
 const dv2=q(2).mul(V).mul(rho).add(rho.pow(2));
 const duv=U.add(V).mul(rho).add(rho.pow(2));
 const dL=beta.mul(q(4).mul(du2.add(K.mul(dv2))).add(q(2).mul(one.add(K)).mul(duv)));
 gate("true_raw_local_matrix_difference",dL.lt(q(36).mul(rho)));
 const du21=q(2).mul(U1.add(U)).mul(rho).add(q(2).mul(rho.pow(2)));
 const dv21=q(2).mul(V1.add(V)).mul(rho).add(q(2).mul(rho.pow(2)));
 const duv1=U1.add(V1).add(U).add(V).mul(rho).add(q(2).mul(rho.pow(2)));
 const dL1=beta.mul(q(4).mul(du21.add(K.mul(dv21))).add(q(2).mul(one.add(K)).mul(duv1)));
 gate("true_raw_local_matrix_angular_derivative",dL1.lt(q(840).mul(rho)));
 gate("local_multiplier_Hthird_by_L2_H1_interpolation",q(36).pow(2).mul(q(876)).lt(q(105).pow(3)));
 const dD1=q(2).mul(beta).mul(du2.add(K.mul(dv2)));
 gate("complete_P0_sup_fee_in_drift_derivative",dD1.lt(q(12).mul(rho)));
 gate("complete_primitive_drift_sup_fee",q(2,5).mul(q(12)).lt(q(5)));
 gate("drift_multiplier_Hthird_by_interpolation",q(5).pow(2).mul(q(17)).lt(q(8).pow(3)));
 gate("complete_head_Hthird_weight",q(1+384*384).lt(q(8).pow(6)));
 const row=U.add(K.mul(V)),X=q(113),X1=q(38656);
 gate("complete_centre_nonlocal_row",row.lt(dec("1.602")));
 gate("full_primitive_L2_H1_bound",q(17,16).pow(2).mul(q(16)).lt(q(19))&&q(17).lt(q(17,16).pow(2).mul(q(16))));
 const dN0=beta.div(q(2)).mul(row.add(X).mul(rho).add(rho.pow(2)));
 const dN1=q(2).mul(beta).mul(q(17,16)).mul(q(2).mul(row).mul(rho).add(X.add(X1).mul(rho)).add(q(2).mul(rho.pow(2))));
 gate("complete_nonlocal_L2_difference",dN0.lt(q(104).mul(rho)));
 gate("complete_nonlocal_L2_to_H1_difference",dN1.lt(q(150000).mul(rho)));
 gate("complete_nonlocal_infinite_output_Hthird",q(104).pow(2).mul(q(150000)).lt(q(1200).pow(3)));
 gate("mean_rank_full_infinite_output_Hthird",beta.lt(q(2)));
 const dHL=q(8*384*8).add(q(105*8)).add(q(1200)).add(q(2));
 const dLH=q(384*5+12+36+104);
 gate("complete_infinite_tail_head_to_high_source",dHL.le(q(26618)),{coefficient:dHL.str()});
 gate("complete_infinite_tail_high_to_head",dLH.le(q(2072)),{coefficient:dLH.str()});
 const AHs=q(8659),ALH=q(968);
 gate("absolute_complete_head_high_bounds",q(8658).add(dHL.mul(rho)).lt(AHs)&&q(967).add(dLH.mul(rho)).lt(ALH));
 const dHead=q(384*5+36+104+2).add(q(384).mul(beta));
 gate("complete_head_generator_with_true_new_radial_mean",
  q(384).mul(q(201,100)).add(q(384*2+31+212)).add(dHead.mul(rho)).lt(q(1800)));
 gate("head_exponential_uniform",one.div(one.sub(q(1800).mul(h))).lt(q(51,50)));
 const GH=q(1,10000),PH=q(11,1000);
 gate("complete_high_source_and_ports_unchanged",q(9).mul(highInv).mul(h).lt(GH)&&q(3).mul(highInv).mul(sqrtH).lt(PH));
 gate("complete_high_traces_unchanged",q(9).mul(highInv).mul(sqrtH).lt(q(1,32))&&q(9).mul(one.add(highInv.pow(2))).lt(q(24,5).pow(2)));
 const EL=q(51,50),GL=h.mul(EL),PL=sqrtH.mul(EL),loop=GL.mul(ALH).mul(GH).mul(AHs);
 gate("all_193_head_high_feedback_below_one_percent",loop.lt(q(1,100)),{exact_upper:loop.str()});
 const resL=q(100,99);
 const lfL=resL.mul(GL),lfH=resL.mul(GL).mul(ALH).mul(GH),lgL=resL.mul(PL),lgH=resL.mul(GL).mul(ALH).mul(PH);
 gate("complete_head_response_matrix",lfL.lt(q(1,100000))&&lfH.lt(q(1,1000000))&&lgL.lt(q(31,10000))&&lgH.lt(q(1,10000)));
 const hfL=GH.mul(AHs).mul(q(1,100000)),hfH=GH.add(GH.mul(AHs).mul(q(1,1000000)));
 const hgL=GH.mul(AHs).mul(q(31,10000)),hgH=PH.add(GH.mul(AHs).mul(q(1,10000)));
 gate("complete_high_response_matrix",hfL.lt(q(87,10000000))&&hfH.lt(q(102,1000000))&&hgL.lt(q(269,100000))&&hgH.lt(q(111,10000)));
 const fullSource=q(1,100000).add(q(1,1000000)).add(q(87,10000000)).add(q(102,1000000));
 const portFrob=q(31,10000).pow(2).add(q(1,10000).pow(2)).add(q(269,100000).pow(2)).add(q(111,10000).pow(2));
 gate("complete_ordinary_source_to_state_1over8000",fullSource.lt(q(1,8000)));
 gate("complete_ports_to_state_0012",portFrob.lt(q(3,250).pow(2)));
 const lowTrF=sqrtH.mul(EL).mul(one.add(ALH.mul(q(87,10000000).add(q(102,1000000)))));
 const lowTrGL=EL.add(sqrtH.mul(EL).mul(ALH).mul(q(269,100000)));
 const lowTrGH=sqrtH.mul(EL).mul(ALH).mul(q(111,10000));
 gate("complete_low_right_trace",lowTrF.lt(q(1,250))&&lowTrGL.lt(q(103,100))&&lowTrGH.lt(q(17,500)));
 const highTrF=q(1,32).mul(one.add(AHs.mul(q(1,100000).add(q(1,1000000)))));
 const highTrGL=q(1,32).mul(AHs).mul(q(31,10000));
 const highTrGH=q(24,5).add(q(1,32).mul(AHs).mul(q(1,10000)));
 gate("complete_high_two_end_trace",highTrF.lt(q(7,200))&&highTrGL.lt(q(21,25))&&highTrGH.lt(q(483,100)));
 gate("complete_both_raw_traces",q(1,250).add(q(7,200)).lt(q(1,25))&&
  q(36,25).add(q(21,25)).pow(2).add(q(17,500).add(q(483,100)).pow(2)).lt(q(27,5).pow(2)));
 // Higher source on the complete, now infinite head-driven output.
 gate("fourfold_Bessel_A3_to_polynomial_B3",q(5).pow(6).lt(q(4).mul(q(17).pow(3))));
 gate("complete_head_Hfourthird_weight",q(1+384*384).pow(2).lt(q(3000).pow(3)));
 gate("centre_Bone_third_and_Bfourthird_weights",q(129).lt(q(6).pow(3))&&q(129).pow(4).lt(q(660).pow(3)));
 const dSB13=q(4).mul(q(78)).mul(rho).add(q(4).mul(rho.pow(2)))
 .add(K.mul(q(4).mul(dec("10.8")).mul(rho).add(q(4).mul(rho.pow(2)))));
 gate("complete_drift_Bfourthird_difference",dSB13.lt(q(313).mul(rho))&&beta.mul(q(5,4)).mul(q(313)).lt(q(706)));
 const us=q(13*660),vs=q(660).mul(V);
 const dusq=q(4).mul(us).mul(rho).add(q(4).mul(rho.pow(2)));
 const dvsq=q(4).mul(vs).mul(rho).add(q(4).mul(rho.pow(2)));
 const duvs=q(2).mul(us.add(vs)).mul(rho).add(q(4).mul(rho.pow(2)));
 const dLs=beta.mul(q(4).mul(dusq.add(K.mul(dvsq))).add(q(2).mul(one.add(K)).mul(duvs)));
 gate("complete_local_Bfourthird_difference",dLs.lt(q(320000).mul(rho)));
 const Xs=q(302*660),Ys=us.add(K.mul(vs));
 const dNs=beta.div(q(2)).mul(q(2).mul(Ys.add(Xs)).mul(rho).add(q(4).mul(rho.pow(2)))).mul(q(3000));
 gate("complete_nonlocal_head_to_Hfourthird",dNs.lt(q(1123000000).mul(rho)));
 const dHL1=q(706*384*3000).add(q(320000*3000)).add(q(1123000000)).add(q(4));
 gate("complete_infinite_head_output_Hfourthird_difference",dHL1.lt(q(3000000000)),{coefficient:dHL1.str()});
 gate("absolute_complete_head_output_Hfourthird",q(8658*641).add(q(3000000000).mul(rho)).lt(q(5560000)));
 gate("single_angular_commutator_complete_C1",q(4538112).add(dAd).lt(q(4538113)));
 return {kind:"actual_current_moving_root_uniform_A3_infinite_tail_inverse",complete:true,
 arithmetic:"executed normalized BigInt rational inequalities; complete infinite Fourier operators",
 source:"scripts/fourfold_codazzi_current_root_nearby_infinite_tail.mjs",
 candidate_sha256:"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
 inputs:[
 {path:"results/R133-supplement-global-positive-reference-and-current-collar.md",git_blob:"5e89a2ec36f36f2852d47738bc46373fdacf67d1"},
 {path:"results/R133-supplement-current-moving-positive-root-Riccati-and-full-head.md",git_blob:"3edf335784786da9a4a515b28d364d8ad2914e24"},
 {path:"results/R133-supplement-current-moving-body-physical-complex-germ.md",git_blob:"bfe73ee59142618bc7e36d5e3fe06929d9fb68cb"},
 {path:"results/R133-supplement-all-frequency-frame-and-infinite-tail-neighbourhood.md",git_blob:"f07df1671d97116a78050b14dfb717d18b86a407"}],
 domain:{left:"r*(eta)",right:"r*(eta)+9/1000000",whole_original_eta:true,actual_piece:2549,no_internal_seams:true},
 neighbourhood:{real_reflection_pair:true,uniform_radial_A3_radius:rho.str(),norm:"sum over physical k in 4Z of (1+|k|)^3 times the absolute two component Fourier coefficients",arbitrary_unknown_Fourier_tail:true,includes_mean:true},
 reference:{radial_speed:"-gamma*(m_c+mean(h2)); redefined exactly",outside_extension:"arbitrary positive bounded extension, only a reference; actual outside sign not asserted",global_Robin:"the same fixed positive outer reference datum as the global-reference result",W_upper:"4",root_Airy_two_row_factor:"9"},
 high:{first_index:97,physical_minimum:388,E_centre:Ec.str(),tail_E_per_radius:"6200",complete_hE:h.mul(Ec.add(dE)).str(),resolvent:"15/13",first_derivative_resolvent:"15/13",commutator_C1:"4538113"},
 head:{reflection_dimension:193,all_means_retained:true,high_to_low_raw:"968",low_to_high_Hthird:"8659",low_to_high_Hfourthird:"5560000",complete_feedback:loop.str(),head_generator:"1800"},
 complete_bounds:{source_L2r_Hthird_to_state_L2:"1/8000",ports_to_state_L2:"3/250",source_to_both_raw_traces:"1/25",ports_to_both_raw_traces:"27/5"},
 H1_bootstrap:{head_solved_once:true,X0:"<=15/13*(3h*(F0+8659*L)+sqrt(h)*G0)",X1:"<=15/13*(3h*(F1+5560000*L)+sqrt(h)*G1+h*4538113*X0)",F0:"ordinary high source L2r H1/3",F1:"ordinary high source L2r H4/3",G1:"angular derivative of the complete high two incoming ports",raw_head_H1_factor:"385",raw_high_H1_from_X0_X1:"3*(X0+X1)"},
 permissions:{actual_moving_Jacobi_on_A3_neighbourhood:true,complete_head_high_inverse:true,full_unknown_tail:true,all_source_and_mean_rows:true,one_angular_derivative_bootstrap:true,
 H2_neighbourhood_bootstrap:false,nonlinear_same_space_contraction:false,whole_positive_body_inverse:false,global_return_inverse:false,global_nu_inverse:false,nearby_external_regular_graph:false,physical_variation_bridge_paid_here:false},
 gates};
}

export {runNearbyRootInverseBudget};
if(typeof process!=="undefined"&&process.versions?.node&&process.argv[1]?.endsWith("fourfold_codazzi_current_root_nearby_infinite_tail.mjs")){
 const result=runNearbyRootInverseBudget(),json=JSON.stringify(result,null,2)+"\n";
 const k=process.argv.indexOf("--out");
 if(k>=0){
  const fs=await import("node:fs");fs.writeFileSync(process.argv[k+1],json);
  process.stdout.write(JSON.stringify({complete:result.complete,gates:result.gates.length,out:process.argv[k+1]})+"\n");
 }else process.stdout.write(json);
}
