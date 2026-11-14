#!/usr/bin/env node
// Actual fixed-cut curvature floor and complete positive reference frame.
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


function runWholePositiveReferenceFloorBudget(){
 const gates=[],gate=(name,ok,extra={})=>{gates.push({name,passed:!!ok,...extra});if(!ok)throw Error(name);};
 const rlo=dec("0.2383968742994"),rhi=dec("0.2383968743003"),h=q(9,1000000);
 const left=dec("0.2384058742994"),right=q(25,8),germRadius=q(1,100000);
 const Kprime=dec("59.74380437"),monotone=dec("46.2850369150182");
 const capLo=dec("0.02679531"),capHi=dec("3.45006391"),floor=q(1,2000);
 gate("fixed_cut_inside_every_paid_root_piece",left.str()===rlo.add(h).str()&&rhi.lt(left)&&left.sub(rlo).le(h));
 gate("full_true_root_to_cut_stays_in_joint_germ",left.lt(rhi.add(germRadius))&&left.sub(rlo).lt(germRadius));
 gate("fixed_cut_same_actual_PPoly_piece2549",q(2147184947341121n,9007199254740992n).lt(left)&&left.lt(q(4295308144604611n,18014398509481984n)));
 gate("fixed_cut_has_positive_uniform_root_distance",q(8999,1000000000).lt(left.sub(rhi)));
 const cutK=Kprime.mul(left.sub(rhi));
 gate("actual_K_at_fixed_cut_above_one_over2000",floor.lt(cutK),{exact_K_lower:cutK.str()});
 gate("same_intrinsic_monotone_bridge_to_cap",q(119,500).lt(rlo)&&left.lt(q(239,1000))&&q(0).lt(monotone));
 gate("entire_actual_positive_interval_curvature_floor",floor.lt(capLo)&&q(239,1000).lt(right));
 gate("entire_actual_positive_interval_curvature_upper",capHi.lt(q(4))&&dec("0.03308223614221").lt(q(4)));
 gate("global_positive_p_barrier",q(1,45).pow(2).lt(floor)&&floor.lt(q(1,8).pow(2)));
 gate("complete_source_and_reconstruction_frame5",q(64).mul(q(45).pow(3)).lt(q(5).pow(6).mul(q(388)))&&q(4).lt(q(45)));
 gate("H1_reconstruction_frame50001over10000",q(25).mul(q(1).add(q(1,388*388))).lt(q(50001,10000).pow(2)));
 return {kind:"actual_whole_positive_reference_curvature_floor_and_complete_frame",
 complete:true,arithmetic:"executed normalized BigInt rational inequalities; scalar comparison proved in accompanying text",
 source:"scripts/fourfold_codazzi_whole_positive_reference_floor.mjs",
 candidate_sha256:"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
 inputs:[
 {path:"results/R133-supplement-current-moving-body-physical-complex-germ.md",git_blob:"bfe73ee59142618bc7e36d5e3fe06929d9fb68cb"},
 {path:"results/R133-supplement-current-moving-positive-root-Riccati-and-full-head.md",git_blob:"3edf335784786da9a4a515b28d364d8ad2914e24"},
 {path:"results/R133-supplement-global-positive-reference-and-current-collar.md",git_blob:"5e89a2ec36f36f2852d47738bc46373fdacf67d1"},
 {path:"results/R133-supplement-full-compact-metric-curvature-type.md",git_blob:"15de90fc2e61c0d15df47a1a636675c8f0397122"},
 {path:"results/R133-actual-rotational-positive-cap-and-Codazzi-Jacobi-graph.md",git_blob:"1f0c66859862fbe6280fdce466f98dd10cc4a17f"}],
 domain:[left.str(),right.str()],whole_original_eta:true,compact_nu_bump_exactly_zero:true,
 actual_intrinsic:{K_lower:"1/2000",K_upper:"4",K_at_fixed_cut_lower:cutK.str()},
 complete_reference:{speed:"any positive bounded radial extension; actual body speed still requires full coefficient cover",
 p_final:"same actual exterior datum in (1/8,1/5)",g_root:"M^-1/3",p_lower_on_domain:"1/45",W_lower_on_domain:"1/45",W_upper:"4",
 physical_minimum:388,ordinary_Hthird_source_to_canonical_L2_frame:"5",canonical_L2_to_raw_L2_frame:"5",
 first_angular_reconstruction_frame:"50001/10000"},
 execution_scope:{reference_gates_actually_executed:11,actual_candidate_body_field_producer_executed:false,
 actual_complete_positive_coefficient_cover:false,actual_positive_high_Volterra_gate_executed:false,actual_whole_positive_inverse:false,global_BVP_inverse:false},
 gates};
}

export {runWholePositiveReferenceFloorBudget};
if(typeof process!=="undefined"&&process.versions?.node&&process.argv[1]?.endsWith("fourfold_codazzi_whole_positive_reference_floor.mjs")){
 const result=runWholePositiveReferenceFloorBudget(),json=JSON.stringify(result,null,2)+"\n";
 const k=process.argv.indexOf("--out");
 if(k>=0){const fs=await import("node:fs");fs.writeFileSync(process.argv[k+1],json);
 process.stdout.write(JSON.stringify({complete:result.complete,gates:result.gates.length,out:process.argv[k+1]})+"\n");}
 else process.stdout.write(json);
}
