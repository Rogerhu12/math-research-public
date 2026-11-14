"use strict";
/* Independent BigInt implementation, actually runnable without a Python worker.
 * This reconstructs the new rational budget; it is NOT the unavailable native.
 * Reproduction: node THIS_FILE.js > NEW_OUTPUT.json
 */
function computeReconstructedTail47Budget(inputBlobs, implementationBlob) {
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;};
  class Q {
    constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");
      if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
    static q(x){return x instanceof Q?x:new Q(x);}
    add(x){x=Q.q(x);return new Q(this.n*x.d+x.n*this.d,this.d*x.d);}
    neg(){return new Q(-this.n,this.d);}
    sub(x){return this.add(Q.q(x).neg());}
    mul(x){x=Q.q(x);return new Q(this.n*x.n,this.d*x.d);}
    div(x){x=Q.q(x);return new Q(this.n*x.d,this.d*x.n);}
    abs(){return this.n<0n?this.neg():this;}
    pow(k){return new Q(this.n**BigInt(k),this.d**BigInt(k));}
    cmp(x){x=Q.q(x);const a=this.n*x.d-x.n*this.d;return a<0n?-1:a>0n?1:0;}
    text(){return this.d===1n?String(this.n):String(this.n)+"/"+String(this.d);}
  }
  const F=(a,b=1)=>new Q(a,b);
  const dy=k=>k>=0?F(1n<<BigInt(k)):F(1n,1n<<BigInt(-k));
  const gates=[];
  function gate(name,lhs,rhs,relation="<"){
    lhs=Q.q(lhs);rhs=Q.q(rhs);const c=lhs.cmp(rhs);
    gates.push({name,relation,lhs:lhs.text(),rhs:rhs.text(),
                passed:relation==="<"?c<0:relation==="<="?c<=0:c===0});
  }
  const r1=dy(-15),r2=dy(-29),rr1=dy(-16),rr2=dy(-30),Delta=F(80);
  const Sp=x=>F(30).mul(x.pow(2)).mul(F(1).sub(x).pow(2));
  gate("second_bump_Sprime_lower",F(1,2),Sp(F(3,16)));
  gate("second_bump_Sprime_upper",Sp(F(7,32)),1);
  gate("second_bump_absolute_monotonicity",r2.mul(384),Delta.div(2));
  gate("first_bump_log_first",Delta.mul(F(3375,2048)).add(r1.mul(96)),Delta.mul(F(15,8)));
  gate("second_bump_log_first",Delta.add(r2.mul(384)),Delta.mul(F(15,8)));
  gate("first_bump_log_second",Delta.mul(F(45,8)).add(r1.mul(6144)),Delta.mul(6));
  gate("second_bump_log_second",Delta.mul(F(29,5)).add(r2.mul(98304)),Delta.mul(6));
  gate("all_jet_orders_zero_through_four",r2.mul(256).div(r1),F(1,64),"<=");
  gate("full_complex_variation",F(5).add(r1.add(r2).mul(4)),F(28,3));
  gate("full_material_integral_margin",F(10).add(r2.mul(8)),64);
  const sqrtDelta=dy(-64).div(5), e=dy(31).mul(sqrtDelta);
  gate("delta129_exact_square",sqrtDelta.pow(2),F(2,25).mul(dy(-129)),"=");
  gate("fourth_matrix_error",e,dy(-35));
  const b11=F(-1299),b12=F(325,16),b21=F(1235,64),b22=F(-309,1024);
  gate("fourth_ideal_determinant",b11.mul(b22).sub(b12.mul(b21)),F(1,64),"=");
  const radius=F(1,16),den=F(1299).sub(b12.mul(radius)).sub(e.mul(F(1).add(radius)));
  gate("full_complex_cone_denominator",1297,den);
  const image=b21.add(b22.abs().mul(radius)).add(e.mul(F(1).add(radius))).div(den);
  gate("full_complex_cone_invariance",image,radius);
  gate("actual_Mobius_derivative",F(1,64*1297*1297),dy(-26));
  gate("ideal_line_one_step_error",F(65,64).div(1297),F(1,1000));
  gate("unchanged_old_cell_count",4096-128,3968,"=");
  gate("initial_deep_line_difference",F(1,16).add(F(1,64)),F(1,8));
  gate("infinite_error_geometric_sum",F(1).div(F(1000).mul(F(1).sub(dy(-26)))),F(1,999));
  gate("deep_initial_error_below_surrogate",100,26*3968+3);
  const slopeError=e.div(999).add(dy(-100)).mul(70);
  gate("true_fourth_physical_error",slopeError,dy(-38));
  gate("sqrt12_coefficient_lower_square",69*69,20*20*12);
  gate("sqrt12_coefficient_upper_square",20*20*12,70*70);
  gate("true_fourth_lower",14,F(16).sub(F(70,64)).sub(dy(-38)));
  gate("true_fourth_upper",F(16).sub(F(69*7,480)).add(dy(-38)),15);
  gate("first_parameter_Cauchy_fee",dy(-38).div(r1.sub(rr1)),dy(-22),"<=");
  gate("second_parameter_Cauchy_fee",dy(-38).div(r2.sub(rr2)),dy(-8),"<=");
  gate("retuned_stop_difference",dy(-37).mul(15).div(512),dy(-41));
  const x=rr1.add(rr2).mul(2);
  const geo=F(1).div(F(1).sub(x)).mul(F(1).add(rr1.mul(8)).add(rr2.mul(32))).mul(F(9375,131072));
  gate("actual_geometric_profile_margin",geo,F(1,8));
  gate("full_outer_good_set_positive",0,F(1).sub(F(83,16384)));
  gate("real_gamma2_actual_unit_beta_shift_inside",dy(-86),rr2);
  gate("real_gamma1_target_inside",dy(-24).add(dy(-86)),rr1);
  const passed=gates.filter(g=>g.passed).length;
  return {kind:"R119-bundle47-new-BigInt-rational-budget",
    status:passed===gates.length?"passed":"failed",gates_count:gates.length,passed_count:passed,
    implementation:"new JavaScript BigInt reduced rational arithmetic",
    execution_contract:"Every comparison uses exact integer cross multiplication. This report is a new execution, not a Python-run claim.",
    input_git_blobs:inputBlobs,implementation_git_blob:implementationBlob||null,gates,
    historical_unavailable_native_sha256:"7822dcf1b53b5cfe82be4360999ae9fdd7eef3ab6cc6e04b3c538c7a0722ae88",
    historical_native_reproduced:false,python_reconstruction_executed:false,
    not_claimed:["same-width whole-network inverse","nonradial complete beta counterterm","full nonlinear F solved"]};
}
const INPUT_BLOBS = {
  "results/R119-supplement-two-parameter-full-tail-chart-reconstructed.md": "a76cb5bb70bd0d2e5a5a48967b16679ef8ed4170",
  "scripts/fourfold_two_parameter_tail_chart_reconstructed_20261113.py": "56d2ef581042e52d5ef5131c764e4ce1bfcafdf2",
  "results/R119-supplement-actual-phase-preserving-subprincipal-metric-parameter.md": "ae87a824ab3e58479894df470c9f066969e83241",
  "results/R119-supplement-stronger-deep-first-shear-and-complete-local-map.md": "cb2db7a4d9593e75e96344b1c2557fd1a38a0e03",
  "results/R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md": "c8bb47e46fcfa26fa05da0825a597529b2e43dd0",
  "results/R119-supplement-uniform-tail-chart-for-actual-metric-parameters.md": "98386ffd3cffce29599d7eb012350b987a869d47",
  "results/R119-supplement-retuned-fourth-connector-and-common-bumps.md": "4f33b6277074962f7df3009355b44031fa6c1389",
  "results/R119-supplement-actual-exterior-Schur-and-full-weak-Wronskian.md": "bc30d99e60744bf5072558ec2038d3554eae7a7a",
  "results/R119-supplement-actual-complete-radial-return-first-phase.md": "0d1fb3753cf159387864cbe7d8b87cab086a0aac",
  "results/R119-supplement-actual-two-parameter-complete-phase-arithmetic.md": "7d2a2f93a6c1c2ce01931fcba94fb8d1478cb7dc"
};
if (typeof require==="function" && typeof module!=="undefined" && require.main===module) {
  const report=computeReconstructedTail47Budget(INPUT_BLOBS,process.argv[2]||null);
  process.stdout.write(JSON.stringify(report,null,2)+"\n");
  if(report.status!=="passed")process.exitCode=1;
}
