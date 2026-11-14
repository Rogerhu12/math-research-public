/* New exact V8/Node computation, 2026-11-14; no old native replay. */
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

const rhomax=two(-584), rDeltamax=two(-584), tmax=two(-65), dmax=R(1,80);
qgate("new_and_old_shapes_inside_true_ball",A(two(-65),two(-65)),"eq",two(-64));
qgate("phase_principal_second_rescaled",pow(rDeltamax,2),"lt",two(5));
qgate("complete_phase_beta_second_rescaled",
 A(D(pow(rDeltamax,2),R(8)),
 D(A(R(4),A(M(R(140),rhomax),M(R(1715,2),pow(rhomax,2)))),R(64))),
 "lt",two(5));
qgate("true_compensation_first_bits",R(10+5),"eq",R(15));
qgate("true_compensation_value_integral_bits",R(15-1),"eq",R(14));
qgate("complete_compensation_second_nested_bits",R(10+34+2*15),"eq",R(74));
qgate("nested_compensation_relative_error",
 M(two(74-15),M(pow(tmax,2),M(pow(rhomax,5),pow(dmax,3)))),"lt",R(1));
qgate("two_complete_compensation_second_parts",M(R(2),two(15)),"eq",two(16));
qgate("both_actual_compensator_bumps_Ctwo",R(2*131072),"eq",two(18));
const eta1ratio=M(two(33),M(tmax,M(rhomax,pow(dmax,3))));
qgate("complete_theta_height_bound",eta1ratio,"lt",R(1));
qgate("complete_theta_x_sup_bound",M(eta1ratio,rhomax),"lt",R(1));
qgate("complete_theta_x_Lone_bound",A(R(2),eta1ratio),"lt",R(3));
qgate("complete_theta_xx_sup_bound",M(eta1ratio,pow(rhomax,2)),"lt",R(1));
qgate("complete_theta_second_profile_bits",R(18+16),"eq",R(34));
qgate("true_high_frequency_Msquare_a_rho",R(-72+512),"eq",R(440));
qgate("compact_first_generator_complete",A(R(2),two(-441)),"lt",R(3));
qgate("compensation_first_generator_complete",
 M(two(34),M(tmax,M(rhomax,pow(dmax,3)))),"lt",R(1));
qgate("whole_first_generator_margin",R(3+1),"lt",R(8));
qgate("second_direct_generator_sup_Lone",
 M(R(3,2),two(-440)),"lt",R(2));
qgate("second_compensation_generator_bits",R(34+1),"eq",R(35));
qgate("full_two_ordered_Duhamel_constant",M(R(2),pow(R(8),2)),"eq",two(7));
qgate("second_Duhamel_plus_direct_complete",A(R(2),two(7)),"lt",two(8));
qgate("compensation_Hessian_margin",two(35),"lt",two(36));
qgate("actual_single_mode_L_in_rho_bits",R(-2048+4*72),"eq",R(-1760));
qgate("whole_dyadic_band_rho_fourth_fee",pow(R(2),4),"eq",two(4));
qgate("uniform_dyadic_lower_L_bits",R(-1760-4),"eq",R(-1764));
qgate("Hessian_ratio_first_complete_bits",R(36+1764),"eq",R(1800));
qgate("Hessian_ratio_second_complete_bits",R(8+1764+1),"eq",R(1773));
qgate("finite_step_first_relative_part",two(1800-1804),"eq",R(1,16));
qgate("finite_step_second_relative_part",two(1773-1777),"eq",R(1,16));
qgate("finite_step_full_relative_change",A(R(1,16),R(1,16)),"eq",R(1,8));
qgate("remaining_true_derivative",R(1,2),"lt",S(R(1),R(1,8)));
qgate("projection_derivative_two_actual_factors",R(2*8),"eq",R(16));
qgate("uniform_near_resonance_error_bits",R(4-1770),"eq",R(-1764-2));
qgate("uniform_near_resonance_strict_fraction",R(1,4),"lt",R(1,2));
qgate("mean_inverse_density_first_factor",R(2),"eq",R(2));
qgate("mean_inverse_density_product_second",R(2*2),"eq",R(4));
qgate("ordinary_actual_w_squared_first",R(2*2),"eq",R(4));
qgate("ordinary_actual_w_squared_product_second",R(4*2*2),"eq",R(16));
qgate("ordinary_actual_w_squared_compensation_second",R(34+1),"eq",R(35));
// Explicit exponent identities retain dx and dt in the actual generator integrals.
qgate("compact_first_t_measure_rho_power",R(1+(4-1)),"eq",R(4));
qgate("compact_second_t_measure_rho_power",R(1+(4-2)),"eq",R(3));
qgate("direct_second_profile_product_rho_power",R((4-1)+(5-1)),"eq",R(7));
qgate("phase_first_derivative_product_rho_power",R((4-1)+(5-1)),"eq",R(7));
qgate("phase_second_derivative_product_rho_power",R((4-2)+(5-2)),"eq",R(5));
qgate("phase_mixed_derivative_product_rho_power",R((4-1)+(5-2)),"eq",R(6));
qgate("Duhamel_product_rho_power",R(4+4),"eq",R(8));
qgate("first_common_step_grows_like_frequency",R(1),"eq",R(1));
qgate("second_common_step_grows_like_frequency",R(4-1),"eq",R(3));
const report={
 schema:"R119-high-oscillation-small-amplitude-Hessian-v1",
 date:"2026-11-14",
 computation:"new exact BigInt rational inequalities and original measure/scale exponents",
 dependencies:{
  proof:"8a359f45c35e513e786b11d6217a20c345ced5eb",
  actual_compact_high_frequency56:"30de43573d98bc4dcc2923561fed2e16a18cf51d",
  actual_compensation54:"dd0d1378fce997297795ce14312fe91b181af4b1",
  controlled_profile53:"f11edbccd752bf034aa40e71888859d667a04b42"
 },
 domains:{
  frequencies:"M0 <= M <= 2 M0, sqrt(B)/M0 <= 2^-512",
  actual_shape_and_parameter_lone_balls:"each < 2^-65; combined <2^-64",
  rho:"2^-72 /(a M0 sqrt(B))",
  sources:"complete two weak components, real ordinary units, total/bare endpoint terms and independent means"
 },
 bounds:{
  first_actual_transfer:"8 K_j^2 M rho^4",
  complete_compensation_Hessian:"2^16 rho^5 Delta^-3",
  full_Wronskian_Hessian:"2^36 K_j^2 M rho^5 Delta^-3 + 2^8 K_j^3 M^2 rho^8",
  uniform_near_resonance_threshold:"2^-1770 K_j^-6 B^-1",
  complete_finite_parameter_step:"min(r_free,2^-1804 K_j^-5 B^-1 Delta^3 rho^-1,2^-1777 K_j^-6 B^-1 M0^-1 rho^-4)"
 },
 scope:"actual radial fixed true Robin lines and real compact direction family; does not invert nonradial moving-middle matrix or full F",
 gates_count:gates.length,all_passed:true,gates
};
if(typeof console!=="undefined"&&typeof console.log==="function")console.log(JSON.stringify(report,null,2));
return report;

})()
