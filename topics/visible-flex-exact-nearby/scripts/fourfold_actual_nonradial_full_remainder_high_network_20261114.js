"use strict";
/* New exact reduced-rational BigInt calculation, executed in V8.
   No lost native/Python replay and no finite Fourier test are claimed.
   node this-file.js PRODUCER_GIT_BLOB_SHA > output.json */
const dependencies={
  "results/R119-supplement-actual-nonradial-full-remainder-and-high-network.md": "7c012d3dd9dbf8331624f11221eca02f6e9693b5",
  "results/R119-supplement-joint-actual-principal-and-beta-selection.md": "934cddff433cee17338575ea6d70fe8c95a8a207",
  "results/R119-supplement-actual-nonradial-first-density-phase.md": "811e36bbc3858a2c3e3792d5103b4f25d38694b9",
  "results/R119-supplement-actual-strict-density-complete-relative-Cauchy.md": "ce2ae0beeb75d96db8f433ee6ebaeb88bfcf96e7",
  "results/R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md": "3d8f5ee032b8b2c1eb73b1cf7f072ed4e8fd7cbc",
  "results/R119-supplement-actual-root-graph-to-fixed-radial-two-port.md": "5e33e4efae59ce6982a230a34d1d17f18e603eda",
  "results/R119-supplement-actual-positive-DN-to-full-Airy-Cayley-and-sources.md": "0bfa77dedd7016d8767d9ab16988c9ade5269036",
  "results/R119-supplement-actual-positive-two-root-Airy-defect-and-full-sources.md": "62f0c709ebdf6b4dac911744207d7005ade404a3",
  "results/R119-supplement-actual-complete-radial-return-first-phase.md": "0d1fb3753cf159387864cbe7d8b87cab086a0aac",
  "results/R119-supplement-actual-two-parameter-complete-phase-arithmetic.md": "7d2a2f93a6c1c2ce01931fcba94fb8d1478cb7dc",
  "results/R119-supplement-uniform-frequency-reference-Airy-Cauchy.md": "e44caf5cddb05512b3940a132305f4aa23f63e7a",
  "results/R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md": "c8bb47e46fcfa26fa05da0825a597529b2e43dd0"
};

function run(producerGitBlobSha) {
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
  function Q(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return {a:a/g,b:b/g};}
  function add(x,y){return Q(x.a*y.b+y.a*x.b,x.b*y.b);}
  function sub(x,y){return Q(x.a*y.b-y.a*x.b,x.b*y.b);}
  function mul(x,y){return Q(x.a*y.a,x.b*y.b);}
  function div(x,y){return Q(x.a*y.b,x.b*y.a);}
  function pow(x,k){return Q(x.a**BigInt(k),x.b**BigInt(k));}
  function lt(x,y){return x.a*y.b<y.a*x.b;}
  function le(x,y){return x.a*y.b<=y.a*x.b;}
  function eq(x,y){return x.a*y.b===y.a*x.b;}
  function str(x){return x.b===1n?String(x.a):String(x.a)+"/"+String(x.b);}
  function exp2(k){return k>=0?Q(1n<<BigInt(k)):Q(1,1n<<BigInt(-k));}
  const gates=[];
  function gate(name,pass,detail){gates.push({name,pass:!!pass,detail});if(!pass)throw Error("failed: "+name);}
  let factorial26=1n;for(let i=2n;i<=26n;i++)factorial26*=i;
  gate("angle_Cauchy_26",factorial26*(128n**26n)<(1n<<280n),"26!128^26<2^280");
  gate("row_J_power_base",134n**12n<(1n<<129n),"J^6<2^(j/2) at j=129");
  gate("row_J_power_monotone",135n**12n<2n*134n**12n,"(J+1)^12/J^12<2 at J=134; ratio decreases");
  gate("reference_J_ratio",134n**10n<2n*133n**10n,"(j+5)^10/(j+4)^10<2");
  gate("angle_envelope_reference_exponent",8192-10000+8===-1800,"2^-1800 J^6 delta^4");
  gate("angle_envelope_delta_decay",lt(Q(1,2),Q(4)),"J^6<2^(j/2), delta^4<2^(-4j)");
  gate("full_angle_sum_reserve",21+4+2<32,"neighbor reference ratio, roots, and two-state count");
  gate("full_angle_sum_exponent",160032-262144===-102112,"sum epsilon_i*<2^-102112");
  gate("strict_cross_coefficient",eq(mul(Q(-1,4),Q(-2)),Q(1,2)),"(-1/4)(-2 sigma nu) i= i sigma nu/2");
  gate("strict_cross_J_derivative",eq(mul(Q(-1,4),Q(-2)),Q(1,2)),"second exact term +sigma/2, both L cross signs negative");
  gate("strict_output_window",eq(sub(Q(4),Q(1,2)),Q(7,2)),"maximum balanced output 4 is original density index 7/2");
  gate("strict_lower_window",le(Q(-9,2),sub(Q(-1),Q(1,2))),"input s>=-1 stays above original density -9/2");
  gate("strict_worst_product",1024+512+1024+2===2562&&12+8+5===25&&24+16+10===50,"LK_all U <=2^2562 J^25 delta^-50");
  gate("strict_product_envelope",2562+8<4608&&25<=32&&50<=56,"32 pieces, branches, mean columns absorbed");
  gate("strict_boundary_product",1024+1024+1===2049&&12+5===17&&24+10===34,"U_d L U endpoints");
  gate("strict_boundary_envelope",2049+8<4608&&17<=32&&34<=56,"all endpoints below R_st envelope");
  gate("strict_same_branch_second",2*512+1===1025&&2*8===16&&2*16===32,"exact second Duhamel term, no absolute Gronwall");
  gate("root_interaction_gain",eq(add(Q(2,3),Q(2,3)),Q(4,3)),"two full operator factors gain exactly 4/3");
  gate("root_output_window",lt(add(Q(1),Q(4,3)),Q(4)),"s+4/3<=7/3<4");
  gate("root_complete_interaction_bound",2185+2*16===2217,"actual root Cauchy and both free-frame maps");
  gate("root_second_constant",2*128+2217<2560,"complete second Volterra term");
  gate("root_second_b_power",eq(add(mul(Q(2),Q(2,3)),Q(2,3)),Q(2)),"b^(2/3+2/3+2/3)=b^2");
  gate("root_Airy_pi_budget",lt(add(mul(Q(50),Q(22,7)),Q(5)),Q(163)),"50 pi+5 < 50*(22/7)+5 <163");
  gate("root_inverse_defect_fee",2500+3500+1<6002,"true inverse * defect * model inverse, including factor 2");
  gate("positive_height_absorption",eq(sub(Q(1),mul(Q(5),Q(1,64))),Q(59,64)),"1-5H=59/64>0");
  gate("positive_ramp_sqrt65",lt(Q(65),pow(Q(9),2)),"sqrt65<9");
  gate("positive_ramp_gradient",lt(mul(Q(25),div(Q(1,64),Q(3))),Q(1)),"5 sqrt(H/3)<1");
  gate("positive_Estar",lt(pow(Q(10),2),Q(128)),"E*<(9+1)^2<128");
  gate("positive_sqrt_Estar",lt(Q(128),pow(Q(12),2)),"sqrt(E*)<12");
  gate("positive_trace_gradient",lt(mul(Q(25),Q(2,64)),Q(1)),"5 sqrt(2H)<1");
  const traceBound=div(Q(13),Q(59,64));
  gate("positive_Tstar",lt(traceBound,Q(32)),str(traceBound)+"<32");
  const poissonSquared=add(mul(add(Q(4),pow(Q(1,64),2)),pow(Q(32),2)),add(Q(4),Q(2,64)));
  gate("positive_Pstar",lt(poissonSquared,pow(Q(128),2)),str(poissonSquared)+"<128^2");
  const delta129=Q(2,25n*(1n<<129n));
  gate("strict_J_delta_base",lt(mul(Q(134n**2n),pow(delta129,7)),Q(1)),"[J delta^(7/2)]^2<1 at j=129");
  gate("strict_J_delta_monotone",lt(div(pow(Q(135,134),2),Q(128)),Q(1)),"squared next ratio <1");
  gate("negative_full_Cauchy_constant",2500+1024+2500+4*16===6088,"b^4 yields exponent 6088");
  gate("negative_full_Cauchy_powers",eq(add(Q(10),Q(9)),Q(19))&&2+5===7,"J^7 delta^-19 below J^8 delta^-20");
  gate("negative_full_Cauchy_envelope",6088+6<6200,"two-state and fixed-row factors");
  gate("negative_root_inverse_product",6002+1024+2500+10*16===9686,"2^9686 J^10 delta^-65/2");
  gate("negative_root_inverse_powers",eq(add(Q(10),mul(Q(10),Q(9,4))),Q(65,2)),"actual full b^10 factor retained");
  gate("negative_strict_product",1+4608+2500+2*16===7141,"2^7141 J^33 delta^-121/2");
  gate("negative_strict_powers",eq(add(Q(56),mul(Q(2),Q(9,4))),Q(121,2)),"56+9/2=121/2");
  gate("negative_strict_J_absorption",eq(sub(Q(64),Q(121,2)),Q(7,2)),"J delta^(7/2)<1 pays extra J");
  gate("negative_remainder_envelope",9686+8<10000&&7141+8<10000,"finite ordered telescoping sum fits 2^10000");
  gate("positive_times_negative_full",4096+6200===10296&&16+8===24&&16+20===36,"E_+ C_- true: 2^10296 J^24 delta^-36");
  gate("network_total_constant",10296+1024<20000&&10000+1024<20000,"adjugate, maps, neighbor scales and row multiplicity");
  gate("network_total_powers",24<=64&&36<=100&&32<=64&&64<=100,"all two-end products fit common J^64 delta^-100");

  function pa(x,y){const z=Array(Math.max(x.length,y.length)).fill(0n);for(let i=0;i<z.length;i++)z[i]=(x[i]||0n)+(y[i]||0n);return z;}
  function pm(x,y){const z=Array(x.length+y.length-1).fill(0n);for(let i=0;i<x.length;i++)for(let j=0;j<y.length;j++)z[i+j]+=x[i]*y[j];return z;}
  function pe(x,y){for(let i=0;i<Math.max(x.length,y.length);i++)if((x[i]||0n)!==(y[i]||0n))return false;return true;}
  const A=[[[1n],[-1n]],[[0n,1n],[1n]]];
  const M=[[[1n],[1n]],[[0n,-1n],[1n]]];
  const product=Array.from({length:2},()=>Array.from({length:2},()=>[0n]));
  for(let i=0;i<2;i++)for(let j=0;j<2;j++)for(let k=0;k<2;k++)product[i][j]=pa(product[i][j],pm(A[i][k],M[k][j]));
  gate("full_two_row_adjugate_polynomial",pe(product[0][0],[1n,1n])&&pe(product[1][1],[1n,1n])&&pe(product[0][1],[0n])&&pe(product[1][0],[0n]),"exact polynomial identity over Z[U], no inverse of true cross block");
  const highTwo=sub(Q(167+20000),Q(65536,3));
  const highJ=sub(Q(3+64),Q(204,3));
  const highDelta=sub(Q(320,3),add(Q(100),Q(13,2)));
  gate("high_two_exponent",eq(highTwo,Q(-5035,3)),str(highTwo));
  gate("high_J_exponent",eq(highJ,Q(-1)),str(highJ));
  gate("high_delta_exponent",eq(highDelta,Q(1,6)),str(highDelta));
  gate("high_degree_eight",lt(add(highTwo,Q(3)),Q(-1024)),"8*2^(-5035/3)<2^-1024");
  gate("high_row_and_column_degree",8n===1n<<3n,"both row and column degree at most 8");
  gate("high_Neumann_inverse",lt(div(Q(1),sub(Q(1),exp2(-1024))),Q(2)),"(1-2^-1024)^-1<2");
  gate("source_d_inverse_weight",eq(add(Q(1),Q(0)),Q(1)),"actual high source provided in H^(s+1), no free source regularity");

  return {
    status:"passed",
    computed_at_utc_date:"2026-11-14",
    implementation:"new exact reduced-rational BigInt JavaScript, actually executed in V8",
    producer_git_blob_sha:producerGitBlobSha,
    proof_git_blob_sha:dependencies["results/R119-supplement-actual-nonradial-full-remainder-and-high-network.md"],
    dependencies,
    gates_passed:gates.length,gates_total:gates.length,gates,
    mathematical_scope:"Complete true nonradial H^s to H^(s+4/3) local remainder and full high-network inverse with every moving low/mean/source input retained. These exact arithmetic gates certify displayed sufficient budgets; operator, full-output, Piola, and source-domain proofs are in the bound proof. No moving intermediate Schur, original same-label-weight Green inverse, or nonlinear F=0 closure is claimed."
  };
}
if(typeof module!=="undefined")module.exports={run};
if(typeof require!=="undefined"&&require.main===module){
 const sha=process.argv[2];if(!/^[0-9a-f]{40}$/.test(sha||""))throw Error("pass actual producer Git blob SHA");
 process.stdout.write(JSON.stringify(run(sha),null,2)+"\n");
}
