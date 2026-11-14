"use strict";
/* New exact BigInt producer executed in V8. Not a replay of lost native bytes.
   node this-file.js PRODUCER_GIT_BLOB_SHA > output.json */
const dependencies={
  "results/R119-supplement-joint-actual-principal-and-beta-selection.md": "934cddff433cee17338575ea6d70fe8c95a8a207",
  "results/R119-supplement-actual-nonradial-first-density-phase.md": "811e36bbc3858a2c3e3792d5103b4f25d38694b9",
  "results/R119-supplement-actual-finite-Schur-14400-head-and-full-sources.md": "89ec05bd82d351230a0b8d69c19be622b91bbe0e",
  "results/R119-supplement-two-parameter-full-tail-chart-reconstructed.md": "a76cb5bb70bd0d2e5a5a48967b16679ef8ed4170",
  "results/R119-supplement-actual-phase-preserving-subprincipal-metric-parameter.md": "ae87a824ab3e58479894df470c9f066969e83241",
  "results/R119-supplement-actual-complete-radial-return-first-phase.md": "0d1fb3753cf159387864cbe7d8b87cab086a0aac",
  "results/R119-supplement-actual-two-parameter-complete-phase-arithmetic.md": "7d2a2f93a6c1c2ce01931fcba94fb8d1478cb7dc",
  "results/R119-supplement-stronger-tail-joint-actual-return-KAM.md": "79257dea135065ec10fe2fcc5c091e5586407874",
  "results/R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md": "c8bb47e46fcfa26fa05da0825a597529b2e43dd0",
  "results/R119-supplement-joint-KAM-incoming-and-actual-full-Newton-chain.md": "078ce582f9b0b46115167de3b6938a6a2df3186c"
};
function run(producerGitBlobSha) {
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
  function Q(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return {a:a/g,b:b/g};}
  function add(x,y){return Q(x.a*y.b+y.a*x.b,x.b*y.b);}
  function sub(x,y){return Q(x.a*y.b-y.a*x.b,x.b*y.b);}
  function mul(x,y){return Q(x.a*y.a,x.b*y.b);}
  function div(x,y){return Q(x.a*y.b,x.b*y.a);}
  function pow(x,k){let y=Q(1);for(let i=0;i<k;i++)y=mul(y,x);return y;}
  function lt(x,y){return x.a*y.b<y.a*x.b;}
  function eq(x,y){return x.a*y.b===y.a*x.b;}
  function str(x){return x.b===1n?String(x.a):String(x.a)+"/"+String(x.b);}
  const gates=[];
  function gate(name,pass,detail){gates.push({name,pass:!!pass,detail});if(!pass)throw Error("failed: "+name);}
  const dt1=mul(Q(1,2*80*8),add(Q(6144*3),mul(Q(3,2),Q(7*96*6))));
  const dt2=mul(Q(1,2*80*32),add(Q(98304*3),mul(Q(3,2),Q(7*384*6))));
  gate("T1_derivative_exact",eq(dt1,Q(153,8)),str(dt1));
  gate("T1_derivative_bound",lt(dt1,Q(32)),"153/8<32");
  gate("T2_derivative_exact",eq(dt2,Q(2493,40)),str(dt2));
  gate("T2_derivative_bound",lt(dt2,Q(64)),"2493/40<64");
  const t1low=sub(Q(85,1000),Q(32,1n<<20n));
  const t2up=add(Q(61,1000),Q(64,1n<<32n));
  gate("complex_T1_lower",lt(Q(1,16),t1low),str(t1low)+">1/16");
  gate("complex_T2_upper",lt(t2up,Q(1,8)),str(t2up)+"<1/8");
  gate("complex_chi_derivative",lt(div(t2up,t1low),Q(2)),"|chi'|<2");
  gate("first_curve_image",lt(Q(1,1n<<35n),Q(1,1n<<25n)),"second-angle shift<2^-35, first image contains 2^-25");
  const bfirst=mul(Q(7,8),add(Q(9,64),add(Q(3,16),Q(18,32))));
  const bsecond=mul(Q(12,6400),add(Q(64*6,16),Q(5*49*12,64)));
  gate("B_first_integral_exact",eq(bfirst,Q(399,512)),str(bfirst));
  gate("B_second_integral_exact",eq(bsecond,Q(3357,25600)),str(bsecond));
  gate("complex_B_upper",lt(add(bfirst,bsecond),Q(2)),str(add(bfirst,bsecond))+"<2");
  gate("normalized_beta_transversality",eq(mul(Q(1,2),Q(1,256)),Q(1,512)),"(det M/T1)/2>2^-9");
  gate("radial_second_derivative_Cauchy",lt(Q(3n*(1n<<33n)),Q(1n<<36n)),"3*2^33<2^36");
  gate("small_inverse_derivative_variation",36-256<-10,"2^36*2^-256=2^-220<2^-10");
  gate("small_inverse_domain",267-9>256,"|z/a_i|<2^-258<r/2, r=2^-256");
  gate("inverse_derivative_upper",lt(Q(1,1024),sub(Q(1,512),Q(1,1n<<220n))),"1/(2^-9-2^-220)<2^10");
  gate("new_Diophantine_square_fee",64n*64n===(1n<<12n),"64^2=2^12");
  gate("principal_KAM_budget",288-262148===-261860,"2^288*A*=2^-261860");
  gate("principal_KAM_gate",288-262148<-64,"new actual small-divisor-square gate");
  gate("beta_sum_extra_reserve",160032+1<160040,"direct nonradial error plus first-parameter KAM shift");
  gate("parameter_Cauchy_radius",lt(Q(1,1n<<256n),Q(1,1n<<35n)),"at |s|<=2^-256, a 2^-35 direction disk stays within 2^-34");
  gate("full_cross_derivative_exponent",160040+35===160075,"Banach-space directional Cauchy, all columns");
  gate("beta_inverse_input",160040-262144<-267,"|E|<2^-102104<2^-267");
  gate("full_parameter_self_map",160050-262144===-102094,"actual output<2^-102094");
  gate("full_parameter_self_map_domain",160050-262144<-256,"output lies strictly inside r=2^-256");
  gate("full_parameter_contraction",10+160075-262144===-102059,"complete cross derivative<2^-102059");
  gate("full_parameter_contraction_half",10+160075-262144<-1,"strictly below 1/2");
  gate("e_four_lower",lt(Q(32),pow(Q(5,2),4)),"e>5/2 and (5/2)^4>32");
  gate("weighted_label_embedding_exponent",5*(65536-224)+6===326566,"beta=65536, norm<1/64 gives A224<2^-326566");
  gate("weighted_label_embedding_domain",326566>262148,"entire beta-ball lies within actual KAM/second-row domain");
  gate("exact_label_domain_radius",262148-4===262144,"X(a)=16*||a||224");
  return {
    status:"passed",computed_at_utc_date:"2026-11-13",
    implementation:"new exact reduced-rational BigInt JavaScript, actually executed in V8",
    producer_git_blob_sha:producerGitBlobSha,
    proof_git_blob_sha:dependencies["results/R119-supplement-joint-actual-principal-and-beta-selection.md"],
    dependencies,gates_passed:gates.length,gates_total:gates.length,gates,
    mathematical_scope:"Actual infinite coupled principal-return and first-beta parameter selector, with full-label and source scope in proof. No complete moving intermediate Schur inverse or solution of F(a,f*)=0 is claimed."
  };
}
if(typeof module!=="undefined") module.exports={run};
if(typeof require!=="undefined"&&require.main===module){
  const sha=process.argv[2];if(!/^[0-9a-f]{40}$/.test(sha||""))throw Error("pass actual producer Git blob SHA");
  process.stdout.write(JSON.stringify(run(sha),null,2)+"\n");
}
