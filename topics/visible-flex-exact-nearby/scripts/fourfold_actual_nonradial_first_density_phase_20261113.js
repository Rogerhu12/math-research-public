"use strict";
/* New exact BigInt implementation. No original Python/native replay is claimed.
   node this-file.js PRODUCER_GIT_BLOB_SHA > output.json
   Proof supplies full-frequency operator statements; these gates only audit
   displayed sufficient rational and exponent budgets. */
const dependencies = {
  "results/R119-supplement-two-parameter-full-tail-chart-reconstructed.md": "a76cb5bb70bd0d2e5a5a48967b16679ef8ed4170",
  "results/R119-supplement-actual-nonradial-first-density-phase.md": "811e36bbc3858a2c3e3792d5103b4f25d38694b9",
  "results/R119-supplement-actual-strict-density-complete-relative-Cauchy.md": "ce2ae0beeb75d96db8f433ee6ebaeb88bfcf96e7",
  "results/R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md": "3d8f5ee032b8b2c1eb73b1cf7f072ed4e8fd7cbc",
  "results/R119-supplement-actual-root-graph-to-fixed-radial-two-port.md": "5e33e4efae59ce6982a230a34d1d17f18e603eda",
  "results/R119-supplement-actual-complete-radial-return-first-phase.md": "0d1fb3753cf159387864cbe7d8b87cab086a0aac",
  "results/R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md": "c8bb47e46fcfa26fa05da0825a597529b2e43dd0",
  "results/R119-supplement-actual-phase-preserving-subprincipal-metric-parameter.md": "ae87a824ab3e58479894df470c9f066969e83241",
  "results/R119-supplement-actual-two-parameter-complete-phase-arithmetic.md": "7d2a2f93a6c1c2ce01931fcba94fb8d1478cb7dc",
  "results/R119-supplement-actual-positive-band-two-end-dn-and-ordinary-source.md": "2d26fdb91363744bfe74ae83ee81bdcce60588af",
  "results/R119-supplement-positive-DN-in-actual-Airy-endpoint-angles.md": "5181b7dd7a03dcac64a4e2b72027ffc9a549a6ca",
  "results/R45-supplement-actual-exact-positive-cap-Airy-contact-and-four-thirds.md": "abdc0be67c66dbdbdd6eecefaba603b05da9b2e3"
};
function run(producerGitBlobSha) {
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
  function Q(a,b=1n){a=BigInt(a);b=BigInt(b);if(b===0n)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return {a:a/g,b:b/g};}
  function mul(x,y){return Q(x.a*y.a,x.b*y.b);}
  function add(x,y){return Q(x.a*y.b+y.a*x.b,x.b*y.b);}
  function sub(x,y){return Q(x.a*y.b-y.a*x.b,x.b*y.b);}
  function pow(x,k){let y=Q(1);for(let i=0;i<k;i++)y=mul(y,x);return y;}
  function lt(x,y){return x.a*y.b<y.a*x.b;}
  function eq(x,y){return x.a*y.b===y.a*x.b;}
  function str(x){return x.b===1n?String(x.a):String(x.a)+"/"+String(x.b);}
  const gates=[];
  function gate(name,pass,detail){gates.push({name,pass:!!pass,detail});if(!pass)throw Error("gate failed: "+name);}
  const H=Q(1,64),sqrtH=Q(1,8);
  gate("finite_part_density_coefficient",eq(mul(Q(5,16),Q(2,3)),Q(5,24)),"(5/16)*(2/3)=5/24");
  gate("half_density_finite_part",eq(mul(Q(1,2),Q(5,24)),Q(5,48)),"half-integral subtracts 5*b/(48*epsilon^(3/2))");
  gate("physical_to_standard_frequency",eq(mul(Q(1,4),Q(2)),Q(1,2)),"-2*b/m=-b/(2*n), m=4*n");
  gate("root_H_and_sqrt",eq(mul(sqrtH,sqrtH),H),"H=1/64, sqrt(H)=1/8");
  gate("positive_height_absorption",lt(mul(Q(5),H),Q(1)),str(mul(Q(5),H))+"<1");
  gate("positive_height_reserve",lt(Q(9,2),Q(5)),"|log(alpha)_xi|<9 gives half-gradient<5 with paid tiny angular term");
  gate("graph_density_fee_exponents",17+13===30,"2^17*b times 2^13*n is 2^30*b*n");
  gate("root_potential_fee_exponents",32-3===29,"2^32*b*n*sqrt(H)=2^29*b*n");
  gate("two_roots_with_state_four",lt(mul(Q(2),mul(Q(4),add(Q(1),Q(1,2)))),Q(16)),"2 roots, n_i=4*Nsharp*X, graph plus half-sized potential <16");
  gate("root_power_below_strict",lt(Q(9,4),Q(5)),"delta^(-9/4)<=delta^(-5), 0<delta<1");
  gate("strict_constant_reserve",130<144,"strict 2^130 is below selected 2^144");
  gate("root_constant_reserve",30+16+4<144,"graph b bound and root/state multiplicities");
  const normexp=sub(Q(5),Q(3,4));
  gate("normalized_beta_delta_power",eq(normexp,Q(17,4)),str(normexp));
  gate("reference_squared_delta_dominance",lt(normexp,Q(20)),"17/4<20");
  gate("reference_squared_constant_dominance",144<10000,"2^144<2^10000");
  gate("reference_polynomial_dominance",lt(pow(Q(134,133),3),Q(2)),"(j+5)^3<2*(j+4)^3 for j>=129; remaining seven powers absorb 2");
  gate("neighbor_reference_polynomial",lt(pow(Q(134,133),10),Q(2)),"worst j=130 ratio, <2");
  gate("neighbor_reference_total_exponent",20+1===21,"delta ratio contributes 2^20, polynomial contributes <2");
  const mult=mul(Q(4),add(Q(1),Q(1n<<21n)));
  gate("component_neighbor_multiplicity",lt(mult,Q(1n<<24n)),str(mult)+"<2^24");
  gate("summed_beta_reserve",160000+24<160032,"actual complete sum <2^160000, multiplicity <2^24");
  gate("actual_X_beta_error",160032-262144===-102112,"normalized beta sum <2^-102112");
  gate("actual_state_root_gate",160000+2-262144<-4424,"n_i<=4*sum(Kref^2*N)*X<2^-102142");
  gate("actual_graph_b2_gate",160000+2-262144<-512,"b^2*n_i is bounded by same paid reference-square sum");
  gate("actual_root_log_derivative_gate",25+160000+2-262144<0,"2^25*n_i<1");
  gate("actual_root_potential_gate",32+160000+2-262144<0,"2^32*n_i<1, |V|<17");
  return {
    status:"passed",computed_at_utc_date:"2026-11-13",
    implementation:"new pure JavaScript exact reduced-rational BigInt",
    execution_claim:"V8 functions execution; not the lost Python/native run",
    producer_git_blob_sha:producerGitBlobSha,
    proof_git_blob_sha:dependencies["results/R119-supplement-actual-nonradial-first-density-phase.md"],
    dependencies,gates_passed:gates.length,gates_total:gates.length,gates,
    mathematical_scope:"Actual nonradial first-symbol/finite-part identification is proved in the linked text. Gates audit its displayed sufficient budgets. No uniform whole-network inverse or solution of F(a,f*)=0 is claimed."
  };
}
if(typeof module!=="undefined") module.exports={run};
if(typeof require!=="undefined"&&require.main===module) {
  const sha=process.argv[2];
  if(!/^[0-9a-f]{40}$/.test(sha||"")) throw Error("pass actual producer Git blob SHA");
  process.stdout.write(JSON.stringify(run(sha),null,2)+"\n");
}
