"use strict";
/* New exact BigInt budget for the actual fixed-label rho^5 response.
   Analytic IVP, full source propagation and mean arguments are in the proof. */
function computeCompactProfileLabelResponse(inputBlobs,implementationBlob){
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

const x=R(7,16);
const sx=A(S(M(R(10),pow(x,3)),M(R(15),pow(x,4))),M(R(6),pow(x,5)));
qgate("actual_S_left_endpoint",sx,"lt",R(1,2));
qgate("actual_S_greater_than_three_eighths",R(3,8),"lt",sx);
qgate("first_descent_delta_exponent",S(M(R(2),R(3,8)),R(1)),"eq",R(-1,4));
qgate("second_descent_delta_exponent",S(R(3,8),R(1)),"eq",R(-5,8));
qgate("first_descent_covered_by_second",R(-5,8),"lt",R(-1,4));
qgate("two_canonical_component_margin",R(33),"lt",two(6));
qgate("canonical_full_cell_power_margin",R(262+210),"lt",R(480));
qgate("mean_source_ball_n",R(1,64),"lt",R(1,32));
qgate("fourfold_cutoff_radius_fee",R(4**10),"eq",two(20));
qgate("halved_width_radius_fee",R(2**10),"eq",two(10));
qgate("true_derivative_Cauchy_fee",M(R(3,2),two(158+10)),"lt",two(170));
qgate("true_physical_derivative_fee",M(R(3,2),two(200+10)),"lt",two(212));
const j=R(8193), ld=A(j,R(4));
const internalLog=A(R(480+20-19689-24),A(D(ld,R(32)),M(R(4),ld)));
qgate("actual_internal_subinterval_ball_first_layer",internalLog,"lt",R(14000));
qgate("actual_internal_true_input_below_quarter",R(14000-262144),"lt",R(-2));
qgate("actual_original_half_width_input",R(10-19689-262144),"lt",R(-2));
qgate("actual_background_n_first_layer",R(210-352-19689-262144),"lt",R(-6));
const monotone=S(R(5),S(S(R(249,2),R(4)),R(13,256)));
qgate("actual_internal_ball_all_layer_monotonicity",monotone,"lt",R(0));
qgate("ceil_argument_log_ratio",R(81,64),"lt",R(2));
qgate("fractional_h_ratio",R(2),"lt",pow(R(9,8),R(8).n));
const cutoffLeft=A(R(14),A(D(j,R(128)),D(ld,R(256))));
const cutoffRight=A(R(-5),M(R(3,8),A(j,R(3))));
qgate("actual_fourfold_Galerkin_cutoff",cutoffLeft,"lt",cutoffRight);
qgate("actual_cutoff_monotonicity",R(3,256),"lt",R(3,8));
const n=R(1,64);
qgate("source_R_k_with_one_width",D(A(R(8),M(R(152),n)),R(3)),"lt",R(32));
qgate("source_Rp_theta_with_two_widths",R(8,3),"lt",R(3));
qgate("source_Rk_plus_Rp_theta",R(32+3),"lt",R(64));
qgate("actual_nu_f_four_derivative_fee",R(32,9),"lt",R(32));
qgate("actual_profile_source_exponent",A(R(-5,4),R(-2)),"eq",R(-13,4));
qgate("actual_source_log_constant",R(6+258+8+210),"lt",R(490));
qgate("actual_full_integral_log_fee",R(490+1),"eq",R(491));
qgate("actual_true_linearized_endpoint_log_fee",R(491+170),"eq",R(661));
qgate("actual_radial_measure_delta_gain",A(R(-13,4),R(3,2)),"eq",R(-7,4));
qgate("actual_endpoint_strong_source_margin",R(661-2),"lt",R(672));
qgate("actual_full_label_response_margin",R(672+17),"lt",R(768));
qgate("actual_gauged_local_field_log_fee",R(491+212-200-2),"lt",R(512));
qgate("actual_gauged_global_field_margin",R(768+12+1),"lt",R(832));
qgate("actual_gauged_local_field_covered",R(512+1),"lt",R(832));
qgate("actual_mean_global_sum_fee",R(832+160017+1),"lt",R(160900));
qgate("actual_mean_compact_integral_fee",R(14+160016+1),"lt",R(160900));
qgate("actual_Pj_delta_exponent",A(R(7,4),R(14,256)),"eq",R(231,128));
return{
 schema:"visible-exact-R119-actual-compact-profile-label-response-v1",
 implementation:"new exact V8 BigInt rational computation; not recovered Python native",
 input_blobs:inputBlobs,implementation_blob:implementationBlob,
 gates,gate_count:gates.length,all_passed:gates.every(x=>x.passed),
 actual_contracts:{
  endpoint_source:"2^672 h_j^-14 delta_j^-7/4 rho^5 ||X||_X_beta",
  fixed_original_label_response:"2^768 h_j^-14 delta_j^-7/4 rho^5 ||X||_X_beta",
  full_gauged_physical_field:"2^832 (N_i^c)^# ||X||_X_beta h_j^-14 delta_j^-7/4 rho^5",
  mean_height:"2^160900 h_j^-14 delta_j^-7/4 rho^5 ||X||_X_beta, plus the one independent height constant and separate reference-height term"
 },
 scope:"Actual same-current-Gamma source-free nonlinear background, all modes, original weighted labels, actual complete truncated IVP and tangent mean; profile compensation columns and physical network remain separate",
 retained:["all actual Fourier output","both nonlinear mean identities and independent height","full source first component","actual ordinary and weak source units","total/bare weak endpoint traces"],
 excluded:["new arbitrary label width","arbitrary L1 sources receiving rho5 for free","same-width derivative of naked pullback","claim of full nonradial network inverse"]
};
}
if(typeof module!=="undefined"&&module.exports)module.exports=computeCompactProfileLabelResponse;
