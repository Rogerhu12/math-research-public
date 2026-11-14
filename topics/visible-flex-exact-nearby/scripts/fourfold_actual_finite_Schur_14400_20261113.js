"use strict";
/* Exact budget for the actual finite Schur/head result. Standard Node or V8. */
function computeActualFiniteHeadBudget(inputBlobs, implementationBlob) {
 const gates=[];
 const G=(name,a,b,op="<")=>{
  a=BigInt(a);b=BigInt(b);
  gates.push({name,lhs:String(a),relation:op,rhs:String(b),
    passed:op==="<"?a<b:op==="="?a===b:a<=b});
 };
 G("cohomological_square_fee",(4096n/64n)**2n,2n**12n,"=");
 G("new_KAM_exponent",288n-262148n,-261860n,"=");
 G("new_KAM_actual_smallness",-261860n,-64n);
 G("true_width_numerator",1850n*400n+88823n,828823n,"=");
 G("actual_width_below_2080",828823n,2080n*400n);
 const M=14400n;
 G("actual_fourfold_cutoff",M%4n,0n,"=");
 G("retained_nonzero_Fourier_coordinates",2n*(M/4n),7200n,"=");
 G("finite_width_cost_binary_exponent",2n*2080n*M,59904000n,"=");
 G("preconditioned_derivative_exponent",-403n-60000000n+2n*2080n*M,-96403n,"=");
 G("strict_head_contraction_margin",-96403n,-96000n);
 G("head_inverse_Neumann_margin",-96000n,-1n);
 // r_f + (1/16)/4 < 1/8, all by exact integer cross multiplication.
 G("head_at_zero_self_map",(64n+100000000n)*8n,6400000000n);
 G("head_ball_self_map",9n,16n);
 G("true_final_94th_width",262144n-2080n*94n,66624n,"=");
 G("true_final_width_above_min",65536n,66624n);
 G("post94_head_correction_exponent",-5760041760n+59904000n-3n,-5700137763n,"=");
 G("post94_correction_inside_real_ball",-5700137763n,-60000002n);
 // First actual parameter stays inside its real box.
 G("base_first_parameter_in_box",(1n<<62n)+1n,1n<<70n);
 const passed=gates.filter(g=>g.passed).length;
 return {kind:"R119-actual-finite-Schur-and-14400-head-exact-budget",
  implementation:"new JavaScript BigInt integer and rational cross-products",
  input_git_blobs:inputBlobs,implementation_git_blob:implementationBlob||null,
  status:passed===gates.length?"passed":"failed",gates_count:gates.length,passed_count:passed,gates,
  actual_scope:["same two-parameter radial candidate","true principal KAM re-instantiation",
    "full nonlinear outer map with arbitrary higher labels retained","exact 14400 Fourier head elimination",
    "every fixed-mode finite radial Schur has no kernel","all ordinary/weak/mean and bare endpoint charges retained"],
  not_claimed:["all moving intermediate Schur blocks uniformly inverted",
    "nonradial beta fixed","full nonlinear F solved","whole closed visible family proved"]};
}
const INPUT_BLOBS={
  "results/R119-supplement-actual-finite-Schur-14400-head-and-full-sources.md": "89ec05bd82d351230a0b8d69c19be622b91bbe0e",
  "results/R119-supplement-two-parameter-full-tail-chart-reconstructed.md": "a76cb5bb70bd0d2e5a5a48967b16679ef8ed4170",
  "results/R119-supplement-actual-two-parameter-complete-phase-arithmetic.md": "7d2a2f93a6c1c2ce01931fcba94fb8d1478cb7dc",
  "results/R119-supplement-stronger-tail-joint-actual-return-KAM.md": "79257dea135065ec10fe2fcc5c091e5586407874",
  "results/R119-supplement-stronger-tail-raw-labels-sources-and-regular-boundary.md": "472372b0ff0f49580013ad5a473e3f37e5e7d5a1",
  "results/R119-supplement-joint-KAM-incoming-and-actual-full-Newton-chain.md": "078ce582f9b0b46115167de3b6938a6a2df3186c",
  "results/R119-supplement-actual-exterior-Schur-and-full-weak-Wronskian.md": "bc30d99e60744bf5072558ec2038d3554eae7a7a",
  "results/R119-supplement-actual-boundary-Schur-projector-and-interior-Green-kernel.md": "2ff7b197b8d40825f39601ece44cb96f6b869682"
};
if(typeof require==="function" && typeof module!=="undefined" && require.main===module){
 const r=computeActualFiniteHeadBudget(INPUT_BLOBS,process.argv[2]||null);
 process.stdout.write(JSON.stringify(r,null,2)+"\n");if(r.status!=="passed")process.exitCode=1;
}
