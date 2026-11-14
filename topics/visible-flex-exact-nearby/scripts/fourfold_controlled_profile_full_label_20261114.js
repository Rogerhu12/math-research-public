/* R119 controlled-profile full-label budget, 2026-11-14.
   Exact BigInt rationals and Laurent polynomials. This is a new JavaScript
   computation, not a replay of a previous Python/native result.
   Run: node topics/visible-flex-exact-nearby/scripts/fourfold_controlled_profile_full_label_20261114.js
*/
(function () {
"use strict";
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
function peval(c,x){let z=R(0);for(let k=c.length-1;k>=0;k--)z=A(M(z,x),c[k]);return z;}
function deriv(c){return c.slice(1).map((z,k)=>M(z,R(k+1)));}
const Sp=[0,0,30,-60,30].map(z=>R(z)), Spp=deriv(Sp), Sppp=deriv(Spp);
const xl=R(7,16), xr=R(15,32);
qgate("support_after_old_bumps",R(3,8),"lt",xl);
qgate("Sprime_lower_on_J",R(7,4),"lt",peval(Sp,xl));
qgate("Ssecond_lower_on_J",R(7,8),"lt",peval(Spp,xr));
qgate("Sthird_negative_left",peval(Sppp,xl),"lt",R(0));
qgate("Sthird_negative_right",peval(Sppp,xr),"lt",R(0));
qgate("support_away_from_peak",xr,"lt",R(1,2));
qgate("peak_gap",R(1,128),"lt",S(peval(Sp,R(1,2)),peval(Sp,xr)));
qgate("shape_cannot_change_monotonicity",two(-20),"lt",M(R(8193,2),R(7,8)));
qgate("complex_slide_keeps_short_platform",R(7,8),"le",S(R(1),R(1,8)));
const j=R(8193), dm=R(8196), dp=R(8197), K=two(128);
qgate("short_generator_low_window",M(M(R(32),K),two(-160)),"le",two(-27));
qgate("exponential_small_argument",two(-27),"lt",R(1,2));
qgate("short_insertion_uses_full_ordered_product",D(M(R(192),R(64)),R(12)),"le",two(10));
qgate("three_platform_telescope_coefficient",A(A(R(20),R(60,256)),R(5,3)),"lt",two(5));
qgate("complete_matrix_error_below_2pow267",A(M(two(10),pow(K,2)),M(two(5),K)),"lt",two(267));
qgate("same_2pow272_error_preserved",two(267),"lt",two(272));
qgate("relative_cone_error_preserved",two(149-160),"eq",two(-11));
qgate("interior_Gauss_full_product",D(M(M(M(R(2),R(4)),R(8)),R(8)),R(12)),"lt",two(12));
qgate("interior_flow_safe_prefactor",M(R(512,12),K),"lt",two(140));
qgate("homogeneous_five_derivative_fee",R(100000),"lt",two(17));
qgate("finite_contraction",two(140+27+158-352),"eq",two(-27));
qgate("mean_compressed_inverse_relative",two(19+158-352),"eq",two(-175));
qgate("finite_quadratic_exponent",R(153+25+2*158),"lt",R(496));
qgate("full_nonlinear_coefficient_margin",R(496),"lt",R(512));
qgate("correction_physical_binary_margin",R(48+184+4),"lt",R(240));
qgate("correction_angle_conversion_margin",R(240+6),"lt",R(248));
qgate("correction_actual_relative_ball",M(R(640),two(-112)),"lt",R(1,4000000));
qgate("correction_Cauchy_ratio_exponent",S(R(4+248+352-500),R(25)),"eq",R(79));
qgate("correction_Cauchy_ratio_small",S(R(79),M(R(9471,8),dm)),"lt",R(-1));
qgate("physical_Ctwo_prefactor_margin",R(184+158-149+7),"le",R(200));
qgate("log2_integer_endpoint_for_Jplus47",R(14),"lt",D(j,R(128)));
qgate("log2_integer_monotonicity_for_Jplus47",R(3*128),"lt",R(2*(8193+47)));
const betaLog=S(D(j,R(256)),M(R(191,256),dm));
qgate("actual_beta_over_h_binary_bound",betaLog,"lt",R(-6082));
qgate("1024_beta_paid",A(R(10),betaLog),"lt",R(0));
qgate("strong_radial_constant_absorbed",R(480*175*3,2),"lt",M(R(16),dm));
const highNeg=A(R(-38),M(R(31,256),dm));
qgate("high_cap_negative_term_binary",R(954),"lt",highNeg);
const logMmax=A(R(-40),D(dp,R(8)));
qgate("high_cap_positive_log",A(R(482-131),M(R(312),A(R(1),logMmax))),"lt",two(34));
qgate("high_cap_net_contraction",A(S(two(34),two(954)),R(2)),"lt",R(0));
qgate("high_frequency_derivative_gate",R(312*4),"lt",two(950));
qgate("high_layer_derivative_gate",R(39,1024),"lt",S(R(1,16),R(1,256)));
const qGlog=S(R(156),M(R(15,32),dm));
qgate("new_low_Green_error",qGlog,"lt",R(-3600));
qgate("normalized_low_error_positive_decay",R(0),"lt",R(15,32));
qgate("old_prefix_still_controls_Green",R(24998080,1000000000),"lt",R(1,32));
qgate("Galerkin_log_integer_endpoint",R(14),"lt",R(8198,512));
qgate("Galerkin_log_integer_monotonicity",R(3*512),"lt",R(2*8198));
const global=A(M(R(3,2),R(4100)),M(R(485,4),R(8196)));
const radiusLog=A(S(A(R(397),global),M(R(249,2),dm)),A(M(R(10,256),dp),R(5*8198,512)));
const nonlinearLog=A(S(A(R(496),global),M(R(249,2),dm)),M(R(14,256),dp));
qgate("both_global_factors_radius_gate",radiusLog,"lt",R(-19689));
qgate("both_global_factors_nonlinear_gate",nonlinearLog,"lt",R(-19542));
qgate("radius_deep_layer_derivative",A(R(-249,2),A(R(10,256),R(5,512))),"lt",R(-124));
qgate("nonlinear_deep_layer_derivative",A(R(-249,2),R(14,256)),"lt",R(-124));
qgate("Ctwo_flat_exponent",R(0),"lt",S(R(127),R(5,256)));
qgate("reference_square_relative_deep_exponent",R(104),"lt",S(S(R(249,2),R(20)),R(5,256)));
qgate("full_relative_sum_only_added_16_bits",R(200-184),"eq",R(16));
qgate("raw_extra_fee_polynomial_at_600",R(100000*600+300000),"lt",two(26));
qgate("raw_extra_fee_is_tiny",two(26-800),"lt",R(1,1000));
qgate("raw_old_plus_new_cost",A(R(40763493,1310720),R(1,1000)),"lt",R(32));
qgate("raw_new_allowance_dominates_exact_terms",R(88896),"lt",R(100000));
qgate("raw_new_constant_dominates_exact_terms",R(251328),"lt",R(300000));
qgate("raw_Mstar_log_greater_than_600",R(600),"lt",M(A(R(-40),R(8196,8)),R(2,3)));
gate("geometric_width_denominator",2n*(511n**256n)>512n**256n,
     {identity:"2*(511/512)^256>1"});
qgate("all_actual_angle_width_sum",M(A(R(35712,100),R(1,16)),R(1025,1024)),"lt",R(358));
qgate("raw404_actual_total",A(R(5177,400),R(391)),"lt",R(404));
qgate("fourth_full_prefix_contraction_exponent",R(-24*8064-3+7),"eq",R(-193532));
qgate("mean_total_flux_constant",M(M(R(4),two(10)),R(2)),"le",two(13));
qgate("mean_height_slope_constant",M(two(13),two(9)),"eq",two(22));
qgate("mean_direct_source_constant",R(12*16*2),"lt",two(13));
qgate("ordinary_mean_Ctwo_positive_flat_power",R(0),"lt",R(19,4));
qgate("shape_Cauchy_domain_distance",S(two(-20),two(-21)),"eq",two(-21));
qgate("slide_Cauchy_domain_distance",S(R(1,8),R(1,16)),"eq",R(1,16));
qgate("Gamma1_Cauchy_domain_distance",S(two(-15),two(-16)),"eq",two(-16));
qgate("Gamma2_Cauchy_domain_distance",S(two(-29),two(-30)),"eq",two(-30));

/* Laurent ring variables: r,p,u=mu_j,rho,q=sqrt12,m,b=(log p)_y,i.
   q^2=12 and i^2=-1 are reduced exactly. */
const nv=8, iz={r:0,p:1,u:2,rho:3,q:4,m:5,b:6,i:7};
const key=e=>e.join(",");
const unpack=k=>k.split(",").map(Number);
function mono(c,ex={}){let e=Array(nv).fill(0);for(const [v,n] of Object.entries(ex))e[iz[v]]=n;
 let a=Math.floor(e[4]/2);e[4]-=2*a;c=M(c,pow(R(12),a));
 let b=Math.floor(e[7]/2);e[7]-=2*b;if(b%2)c=N(c);
 const z=new Map();if(c.n)z.set(key(e),c);return z;}
const pc=n=>mono(R(n));
function padd(x,y){let z=new Map(x);for(const[k,v]of y){let a=A(z.get(k)||R(0),v);if(a.n)z.set(k,a);else z.delete(k);}return z;}
const pneg=x=>new Map([...x].map(([k,v])=>[k,N(v)]));
const psub=(x,y)=>padd(x,pneg(y));
function pmul(x,y){let z=new Map();for(const[k,a]of x)for(const[l,b]of y){let e=unpack(k),f=unpack(l);let ex={};Object.keys(iz).forEach(v=>ex[v]=e[iz[v]]+f[iz[v]]);
 z=padd(z,mono(M(a,b),ex));}return z;}
function pdiff(x,v){let z=new Map();for(const[k,c]of x){let e=unpack(k),n=e[iz[v]];if(!n)continue;e[iz[v]]--;let ex={};Object.keys(iz).forEach(w=>ex[w]=e[iz[w]]);z=padd(z,mono(M(c,R(n)),ex));}return z;}
const pm=(c,e)=>mono(c,e), ps=(n,e)=>pm(R(n),e);
const nu=pmul(pm(R(1,12),{}),psub(ps(1,{m:4}),ps(1,{m:2})));
const qInv=ps(1,{q:-1});
const k=pmul(psub(ps(1,{m:2}),pc(4)),qInv);
const Ap=[[k,pmul(nu,ps(1,{p:-1}))],[ps(-1,{p:1}),pneg(k)]];
const T=[[pmul(nu,ps(1,{rho:-1,r:-4})),pc(0)],
 [ps(-1,{m:2,p:1,q:-1,rho:-1,r:-4}),ps(1,{r:4,q:-1,u:-1})]];
const mu0=ps(1,{u:1,p:1,rho:-1,r:-8});
const invMu0=ps(1,{u:-1,p:-1,rho:1,r:8});
const Q=psub(pc(7),ps(1,{q:1,b:1}));
const Bt=[[pc(0),invMu0],[pneg(pmul(pmul(ps(1,{m:2}),mu0),Q)),pc(0)]];
function matmul(X,Y){let Z=Array.from({length:X.length},()=>Array.from({length:Y[0].length},()=>pc(0)));
 for(let i=0;i<X.length;i++)for(let j=0;j<Y[0].length;j++)for(let k=0;k<Y.length;k++)Z[i][j]=padd(Z[i][j],pmul(X[i][k],Y[k][j]));return Z;}
function dy(P){return padd(pmul(ps(1,{r:1,q:-1}),pdiff(P,"r")),pmul(ps(1,{p:1,b:1}),pdiff(P,"p")));}
const TB=matmul(T,Bt), AT=matmul(Ap,T);
for(let i=0;i<2;i++)for(let j=0;j<2;j++){
 const lhs=padd(dy(T[i][j]),pmul(qInv,TB[i][j]));
 gate("exact_total_flux_homogeneous_entry_"+i+j,psub(lhs,AT[i][j]).size===0);
}
const srcPhysical=[[pneg(invMu0),pc(0),pc(0)],[pc(0),pc(1),ps(-1,{i:1,m:1})]];
const transformed=matmul(T,srcPhysical).map(row=>row.map(P=>pmul(P,qInv)));
const expected=[
 [pneg(pmul(nu,ps(1,{r:4,q:-1,u:-1,p:-1}))),pc(0),pc(0)],
 [pm(R(1,12),{m:2,r:4,u:-1}),pm(R(1,12),{r:4,u:-1}),pm(R(-1,12),{i:1,m:1,r:4,u:-1})]
];
for(let i=0;i<2;i++)for(let j=0;j<3;j++)gate("exact_weak_source_column_"+i+j,psub(transformed[i][j],expected[i][j]).size===0);
const determinant=psub(pmul(T[0][0],T[1][1]),pmul(T[0][1],T[1][0]));
gate("exact_two_trace_determinant",psub(determinant,pmul(nu,ps(1,{q:-1,rho:-1,u:-1}))).size===0);
const ordinaryF=ps(1,{u:2,p:2,r:-14});
const ordinaryN=pm(R(1,12),{u:1,p:2,r:-10});
gate("ordinary_source_recovered_exactly",psub(pmul(expected[1][1],ordinaryF),ordinaryN).size===0);
gate("mean_source_y_orientation_exact",psub(pmul(qInv,ordinaryF),pmul(ps(1,{q:1,u:1,r:-4}),ordinaryN)).size===0);
const Ap2=matmul(Ap,Ap);
const sqTarget=pmul(pm(R(-1,12),{}),psub(ps(7,{m:2}),pc(16)));
gate("constant_platform_square_11",psub(Ap2[0][0],sqTarget).size===0);
gate("constant_platform_square_12",Ap2[0][1].size===0);
gate("constant_platform_square_21",Ap2[1][0].size===0);
gate("constant_platform_square_22",psub(Ap2[1][1],sqTarget).size===0);

const report={
 schema:"R119-controlled-profile-full-label-exact-v1",
 date:"2026-11-14",
 computation:"new V8 JavaScript; exact BigInt rational and Laurent-polynomial gates",
 dependencies:{
  new_proof_blob:"0c8c70a954f01399d06394c1865ce64610a26ea2",
  phase_preserving_control_blob:"5214cfffb5d16f3aebb0105af8aab14b2b5188b1",
  stronger_local_map_blob:"cb2db7a4d9593e75e96344b1c2557fd1a38a0e03",
  stronger_full_label_blob:"c8bb47e46fcfa26fa05da0825a597529b2e43dd0",
  stronger_raw_source_blob:"472372b0ff0f49580013ad5a473e3f37e5e7d5a1",
  original_R72_blob:"a7c78793ba18724a4f0553b6ccd55259b8f4df92",
  two_parameter_tail_reconstruction_blob:"a76cb5bb70bd0d2e5a5a48967b16679ef8ed4170"
 },
 scope:{
  new_profile:"j>=8193; two true downward slides and C4 compact shapes; exact unchanged endpoints",
  all_modes:"real high blocks retained; same Mhat, complete local nonlinear map and all internal labels",
  mean:"complete holonomy-one mean and independent height; weak total flux and two source components",
  excluded:"whole nonlinear far F, nonlinear moving-middle Schur, original same-weight full internal Green"
 },
 first_layer_binary_bounds:{
  beta_over_h:str(betaLog), high_negative_log2:str(highNeg),
  green_error_log2:str(qGlog), local_radius_ratio_log2:str(radiusLog),
  full_nonlinear_factor_log2:str(nonlinearLog)
 },
 gates_count:gates.length, all_passed:true,gates
};
if(typeof console!=="undefined"&&typeof console.log==="function")console.log(JSON.stringify(report,null,2));
return report;
})()
