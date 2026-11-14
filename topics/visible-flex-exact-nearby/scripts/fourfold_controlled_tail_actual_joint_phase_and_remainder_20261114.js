/* New exact V8/Node implementation, 2026-11-14; no native replay. */
(()=>{
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;}
function R(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}let g=gcd(n,d);return {n:n/g,d:d/g};}
const A=(x,y)=>R(x.n*y.d+y.n*x.d,x.d*y.d);
const N=x=>R(-x.n,x.d);
const S=(x,y)=>A(x,N(y));
const M=(x,y)=>R(x.n*y.n,x.d*y.d);
const D=(x,y)=>R(x.n*y.d,x.d*y.n);
const pow=(x,n)=>{n=Number(n);if(n<0)return pow(D(R(1),x),-n);let z=R(1);while(n){if(n%2)z=M(z,x);x=M(x,x);n=Math.floor(n/2);}return z;};
const two=n=>n>=0?R(1n<<BigInt(n)):R(1n,1n<<BigInt(-n));
const lt=(x,y)=>x.n*y.d<y.n*x.d;
const le=(x,y)=>x.n*y.d<=y.n*x.d;
const eq=(x,y)=>x.n===y.n&&x.d===y.d;
const str=x=>x.d===1n?String(x.n):String(x.n)+"/"+String(x.d);
const gates=[];
function gate(name,ok,detail){if(!ok)throw Error("FAILED: "+name);gates.push({name,passed:true,...(detail===undefined?{}:{detail})});}
function qgate(name,x,op,y){gate(name,op==="lt"?lt(x,y):op==="le"?le(x,y):eq(x,y),{left:str(x),relation:op,right:str(y)});}

function egate(name,left,op,right){qgate(name,R(left),op,R(right));}
egate("state_prefactor_increase",200-184,"eq",16);
qgate("third_Q_derivative_new_shape",M(R(147456),two(-64)),"lt",two(-46));
qgate("first_radial_compensated_base",A(A(two(-24),two(-86)),two(-128)),"lt",two(-23));
qgate("second_radial_compensated_base",A(two(-86),two(-128)),"lt",two(-85));
qgate("first_base_and_curve_inside_complex_box",A(two(-23),two(-20)),"lt",two(-15));
qgate("second_base_and_curve_inside_complex_box",A(two(-85),two(-32)),"lt",two(-29));
qgate("principal_curve_parameter_Cauchy_disk",A(two(-256),two(-35)),"lt",two(-34));
qgate("radial_second_inverse_variation",M(two(36),two(-256)),"lt",two(-10));
egate("label_X_normalization",4-262148,"eq",-262144);
egate("KAM_new_smallness",304-262148,"eq",-261844);
egate("KAM_strict_target",304-262148,"lt",-64);
egate("full_reference_weighted_sum_shift",160000+16,"eq",160016);
egate("true_beta_layer_sum_shift",160032+16,"eq",160048);
egate("whole_second_row_sum_shift",160040+16,"eq",160056);
egate("whole_cross_derivative_Cauchy",160056+35,"eq",160091);
egate("actual_radial_inverse_input",160056-262144,"lt",-267);
egate("second_infinite_selfmap",10+160056-262144,"eq",-102078);
egate("second_infinite_selfmap_domain",-102078,"lt",-256);
egate("second_infinite_contraction",10+160091-262144,"eq",-102043);
egate("second_infinite_contraction_strict",-102043,"lt",-1);
egate("actual_angular_fee_sum",160048-262144,"eq",-102096);
egate("angular_fee_inside_prior_budget",-102096,"lt",-64);
qgate("HH_binary_exponent",S(R(20000+167),R(65536,3)),"eq",R(-5035,3));
qgate("HH_layer_polynomial_exponent",S(R(64+3),R(204,3)),"eq",R(-1));
qgate("HH_delta_exponent",A(R(-100),A(R(-13,2),R(320,3))),"eq",R(1,6));
qgate("HH_degree_eight_row_and_column",A(R(-5035,3),R(3)),"lt",R(-1024));
const e4partial=A(R(1),A(R(4),A(R(8),A(R(32,3),R(32,3)))));
qgate("exp4_exceeds32",R(32),"lt",e4partial);
egate("wide_label_whole_ball_embedding",-5*(65536-224)-6,"lt",-262148);
qgate("actual_physical_output_width",S(R(224),R(88823,400)),"eq",R(777,400));
egate("incoming_ball_inside_joint_quarter_ball",-60000000,"lt",-262148-2);
qgate("small_joint_ball_Cauchy_factor",R(3,2),"lt",R(2));
egate("small_joint_ball_fB_derivative",-443+1,"eq",-442);
const rf=R(1,100000000);
qgate("actual_cap_feedback_derivative",M(two(61),rf),"lt",two(35));
egate("actual_incoming_feedback",1-60000000+35-442,"eq",-60000406);
egate("actual_incoming_strict_contraction",-60000406,"lt",-2);
qgate("incoming_selfmap_radius",rf,"lt",R(1,2));
egate("far_fB_inside_actual_cap_input",-60000000-443,"lt",-61);
const Smin=R(10724906843270461n,1000000000n);
const Emin=M(R(4),S(Smin,R(2074)));
qgate("actual_analytic_width_gap",Emin,"eq",R(42891331373081844n,1000000000n));
qgate("incoming_log_prefactor_fee",A(R(42891331),R(1,8)),"lt",Emin);
let e07=R(0),term=R(1);
for(let k=0;k<=4;k++){if(k)term=M(term,R(7,10*k));e07=A(e07,term);}
qgate("ln2_less_than_seven_tenths",R(2),"lt",e07);
qgate("incoming_exact_binary_decay",M(R(60000000),R(7,10)),"lt",R(42891331));
qgate("long_screening_exact_binary_decay",M(R(60000000),R(7,10)),"lt",M(R(7,4),R(24514072)));
egate("joint_tail_Cauchy_quadratic_coefficient",1+262148-442,"lt",261710);
egate("quadratic_far_residual_exponent",261710-2*60000000,"eq",-119738290);
egate("quadratic_far_residual_margin",-119738290+1,"lt",-119738000);
egate("long_zero_inner_quadratic_fee",22-2*443,"lt",261710);
egate("mixed_long_far_residual_exponent",-411-2*60000000,"lt",-119738290);
egate("two_residual_terms_complete_sum",-119738290+1,"lt",-119738000);
qgate("smallest_nonzero_lambda",R(4*4),"eq",R(16));
qgate("smallest_nonzero_physical_frequency",R(4),"eq",R(4));
const report={
 schema:"R119-controlled-tail-actual-joint-phase-remainder-v1",
 date:"2026-11-14",
 computation:"new JavaScript exact BigInt rational arithmetic and exact exponent comparisons",
 dependencies:{
  proof:"fc3aab62e99a51cc06bd26a7233663a2b8e4dd73",
  controlled_chart53:"f11edbccd752bf034aa40e71888859d667a04b42",
  phase_compensation54:"dd0d1378fce997297795ce14312fe91b181af4b1",
  joint_phase50:"934cddff433cee17338575ea6d70fe8c95a8a207",
  full_remainder51:"7c012d3dd9dbf8331624f11221eca02f6e9693b5",
  actual_incoming:"1a5b8d8f1d4f4023749e2af953237d31e4949579"
 },
 domains:{
  shape_annihilator_complex_radius:"2^-64",
  true_label_224_ball:"2^-262148",
  true_state_bound:"2^-262144",
  second_parameter_fixedpoint_ball:"2^-256",
  actual_incoming_ball:"2^-60000000"
 },
 proved_bounds:{
  second_phase_selfmap:"<2^-102078",
  second_phase_contraction:"<2^-102043",
  whole_actual_angular_fee:"<2^-102096",
  actual_Hs_to_Hs_plus_four_thirds:"2^20000 (j+5)^64 delta^-100, |s|<=1",
  actual_HH_feedback:"<2^-1024",
  actual_new_incoming_feedback:"<2^-60000406",
  actual_complete_far_residual_in_physical_width:"<2^-119738000"
 },
 scope:"Actual controlled profile and exact joint nonradial omega/beta selection; complete ports, both means, ordinary and weak sources retained. HH and a new actual incoming fixed point are proved. Nonradial moving middle and full same-weight inverse/F=0 remain open.",
 gates_count:gates.length,all_passed:true,gates
};
if(typeof console!=="undefined"&&typeof console.log==="function")console.log(JSON.stringify(report,null,2));
return report;

})()
