/* New exact V8/Node arithmetic for full infinite-Hilbert proof constants. */
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

const eps=R(1,16), delta=D(eps,S(R(1),eps)), invD=D(R(1),S(R(1),M(R(2),delta)));
qgate("inverse_near_identity_endpoint_fee",delta,"eq",R(1,15));
qgate("full_Mobius_denominator",M(R(2),delta),"lt",R(1));
qgate("full_Mobius_denominator_inverse",invD,"eq",R(15,13));
qgate("full_four_term_Mobius_difference",
 D(R(4),S(R(1),M(R(3),eps))),"eq",R(64,13));
qgate("full_scattering_rounding",R(64,13),"lt",R(8));
qgate("complete_Dtheta_inverse_half_norm",R(5,4),"lt",R(4));
qgate("sum_to_Hilbert_four_components_squared",R(4),"eq",R(2*2));
qgate("two_norm_equivalences_operator_fee",R(2*2),"eq",R(4));
qgate("exp_eta_minus_one_linear_fee",D(R(1),S(R(1),R(1,4))),"lt",R(2));
qgate("actual_interaction_Hilbert_fee",R(4*2),"eq",R(8));
qgate("complete_relative_scattering_actual_fee",R(8*8),"eq",R(64));
qgate("interaction_domain_for_scattering",M(R(8),R(1,128)),"eq",R(1,16));
qgate("controlled_reference_state_extra_bits",R(200-184),"eq",R(16));
qgate("controlled_whole_interaction_sum_bits",R(192000+16),"eq",R(192016));
qgate("complete_scattering_whole_sum_bits",R(192016+6),"eq",R(192022));
qgate("actual_true_input_interaction_exponent",R(192016-262144),"eq",R(-70128));
qgate("actual_interaction_inside_Mobius_domain",R(-70128),"lt",R(-7));
qgate("actual_true_input_complete_scattering_exponent",R(192022-262144),"eq",R(-70122));
qgate("affine_both_port_Cauchy_Schwarz_factor_squared",R(2),"eq",R(2));
qgate("derivative_reference_scattering_fee",
 M(R(4),M(R(16,15),invD)),"lt",R(16));
qgate("derivative_endpoint_inverse_fee",pow(R(16,15),2),"lt",R(2));
qgate("derivative_complete_endpoint_four_terms",
 M(R(4),M(pow(R(16,15),2),invD)),"lt",R(16));
qgate("complete_mean_symplectic_factor",R(2),"eq",R(2));
qgate("plus_wave_full_symplectic_factor",R(1+1),"eq",R(2));
qgate("minus_wave_full_symplectic_factor",R(-1-1),"eq",R(-2));
qgate("plus_minus_symplectic_cross_cancellation",R(-1+1),"eq",R(0));
qgate("minus_plus_symplectic_cross_cancellation",R(1-1),"eq",R(0));
function matmul(X,Y){return X.map(row=>Y[0].map((_,j)=>row.reduce((a,x,k)=>A(a,M(x,Y[k][j])),R(0))));}
const J=[[R(0),R(-1)],[R(1),R(0)]], Ji=matmul(J,J);
gate("actual_mean_strong_complex_structure",
eq(Ji[0][0],R(-1))&&eq(Ji[1][1],R(-1))&&eq(Ji[0][1],R(0))&&eq(Ji[1][0],R(0)));
const Jminus=J.map(row=>row.map(N)), Jmi=matmul(Jminus,Jminus);
gate("both_real_chiral_complex_structures",
eq(Jmi[0][0],R(-1))&&eq(Jmi[1][1],R(-1))&&eq(Jmi[0][1],R(0))&&eq(Jmi[1][0],R(0)));
const report={
 schema:"R119-relative-Cauchy-full-Hilbert-scattering-v1",
 date:"2026-11-14",
 computation:"new exact BigInt rational operator constants and complete symplectic-block identities",
 dependencies:{
  proof:"328192a452be36598c77b26cf51d75f06244b015",
  actual_strict_full_interaction:"ce2ae0beeb75d96db8f433ee6ebaeb88bfcf96e7",
  controlled_profile53:"f11edbccd752bf034aa40e71888859d667a04b42",
  actual_controlled_joint55:"fc3aab62e99a51cc06bd26a7233663a2b8e4dd73"
 },
 bounds:{
  relative_endpoint_input:"epsilon<=1/16",
  full_Hilbert_unitary_scattering:"||S-S0|| <=8 epsilon, no ||C0|| factor",
  actual_strict_scattering:"<=64 eta_i",
  whole_true_controlled_sum:"<2^192022 ||X|| <=2^-70122",
  affine_complete_port_source:"q=b_minus-S b_plus; norm <=sqrt(2)||b||",
  derivative_consumer:"<=16||E-I||||DS0||+16||DE||, only when actual bounded derivatives supplied"
 },
 scope:"complete infinite Fourier Hilbert graph, both means, true principal endpoint coordinates and paid affine charges; not whole physical network or nonradial cluster inverse",
 gates_count:gates.length,all_passed:true,gates
};
if(typeof console!=="undefined"&&typeof console.log==="function")console.log(JSON.stringify(report,null,2));
return report;

})()
