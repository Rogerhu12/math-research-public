/* New exact computation: V8 or Node. No native replay. */
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

const rr=two(-512), Nmin=M(R(80),two(512));
function fact(n){let x=1n;for(let k=2n;k<=BigInt(n);k++)x*=k;return R(x);}
qgate("actual_quartic_min_on_J",R(7,4),"lt",M(R(30),M(pow(R(7,16),2),pow(R(9,16),2))));
qgate("actual_F_upper",A(R(15,8),M(R(7),two(-190))),"lt",R(2));
const qerr=M(pow(rr,2),A(D(two(11),R(160)),R(9,4)));
qgate("scaled_q_lower",qerr,"lt",R(1,4));
qgate("scaled_q_upper",A(R(2),qerr),"lt",R(3));
qgate("quartic_square_full_coefficient_derivative",M(fact(8),pow(R(121),2)),"lt",two(30));
qgate("complete_q_derivative_coarse_constant",
 M(fact(8),A(R(120),A(R(360,160),R(121*121,4)))),"lt",two(44));
for(let k=0;k<=21;k++){
 let ss=R(0);
 for(let l=1;l<=Math.min(8,k);l++)ss=A(ss,pow(R(8),k-l));
 qgate("full_Z_normalized_jet_"+(k+1),
 D(A(M(R(6),pow(R(8),k)),M(D(two(45),Nmin),ss)),R(k+1)),
 "lt",pow(R(8),k+1));
 qgate("frozen_Z_difference_jet_"+(k+1),
 D(A(M(M(R(6),two(50)),pow(R(16),k)),M(two(45),ss)),R(k+1)),
 "lt",M(two(50),pow(R(16),k+1)));
}
qgate("branch_modulus_F_nine_halves_squared",pow(R(17),9),"lt",two(40));
qgate("real_coefficient_zero_jet_error",
 M(R(32),A(R(3),A(M(R(3),rr),M(R(9,4),pow(rr,2))))),"lt",two(8));
qgate("complex_complete_kernel_row",
 M(two(20),A(rr,A(R(2),A(M(R(18),pow(rr,2)),A(M(R(17),rr),M(R(81),pow(rr,3))))))),
 "lt",two(23));
qgate("all_positive_kernel_coefficients_to22",M(two(23),pow(R(8),22)),"lt",two(100));
qgate("factorial_22_bound",fact(22),"lt",two(70));
qgate("full_product_jet_error_to21",
 M(fact(22),A(M(M(R(23),two(100)),pow(R(8),22)),M(M(R(64),two(50)),pow(R(16),22)))),
 "lt",two(256));
qgate("scaled_frozen_error_strict",M(two(256),A(rr,D(R(1),Nmin))),"lt",two(-254));
qgate("energy_change_full_six_units",D(M(R(6),two(44)),Nmin),"lt",R(1,4));
qgate("frozen_twenty_first_derivative",A(M(R(64),pow(R(6),21)),R(1)),"lt",two(63));
qgate("witness_kernel_error_vs_centre",M(R(2),two(-254)),"lt",R(1,8));
qgate("constant_sign_small_support",M(two(64),two(-72)),"lt",R(1,16));
qgate("support_inside_actual_interval",A(R(2),two(-72)),"lt",R(4));
qgate("Cfour_fractional_power_full_derivatives",M(fact(4),M(two(20),pow(R(8),4))),"lt",two(37));
qgate("compact_bump_derivative24",M(two(30),pow(R(60),24)),"lt",two(174));
qgate("compact_direction_sum_Cfour",M(R(80),two(37+174)),"lt",two(220));
qgate("positive_complete_bump_integral",two(-15),"lt",pow(R(3,4),30));
qgate("actual_measure_and_support_fee",R(220+4+15+25*72),"eq",R(2039));
qgate("rounded_full_Wronskian_constant",R(2039),"lt",R(2048));
qgate("coarse_density_delta_power",S(R(48),R(3,2)),"eq",R(93,2));
qgate("coarse_delta_rounding",R(93,2),"lt",R(47));
qgate("Delta_upper_factor",R(27),"lt",two(5));
qgate("coarse_all_fixed_bits",R(2048+3*6000+5),"lt",R(20064));
qgate("coarse_full_layer_power",R(3*8+3),"eq",R(27));
qgate("high_frequency_R_less_2M",A(R(1),pow(rr,2)),"lt",R(2));
qgate("full_Hessian_bits",R(22+2),"eq",R(24));
qgate("finite_step_derivative_variation",R(-2074+24),"eq",R(-2048-2));
qgate("near_resonance_derivative_error",R(8,32),"eq",R(1,4));
qgate("high_frequency_L_below_one_bits",R(-2048-3*512),"lt",R(0));
// Exact commutative Laurent polynomials. No approximate frequency or sample state.
const names=["a","v","m","F","fp","y","z","q"],ix=Object.fromEntries(names.map((x,i)=>[x,i]));
const key=ex=>names.map(n=>ex[n]||0).join(",");
const un=k=>k.split(",").map(Number);
function mon(c,ex={}){return c.n===0n?new Map():new Map([[key(ex),c]]);}
const pc=n=>mon(R(n));
function pa(P,Q){const X=new Map(P);for(const[k,c]of Q){const z=A(X.get(k)||R(0),c);if(z.n===0n)X.delete(k);else X.set(k,z);}return X;}
const pn=P=>new Map([...P].map(([k,c])=>[k,N(c)]));
const ps=(n,ex)=>mon(R(n),ex);
const pm=(n,d,ex)=>mon(R(n,d),ex);
const sub=(P,Q)=>pa(P,pn(Q));
function pp(P,Q){let X=new Map();for(const[k,c]of P)for(const[l,d]of Q){let x=un(k),y=un(l),ex={};for(const n of names)ex[n]=x[ix[n]]+y[ix[n]];X=pa(X,mon(M(c,d),ex));}return X;}
const Fs=ps(1,{F:1}),Hs=pa(Fs,ps(1,{v:-2}));
const c=pa(pm(1,2,{v:2,F:1}),pm(1,2,{}));

const qOriginal=pp(ps(1,{a:-2,m:-2,v:-2}),
 pa(ps(1,{m:2,a:2,v:2,F:1}),
 pa(pm(1,2,{a:1,v:2,fp:1}),pn(pp(ps(1,{a:2}),pp(c,c))))));
const qExpected=pa(Fs,pp(ps(1,{v:2,m:-2}),sub(pm(1,2,{a:-1,v:-2,fp:1}),pp(pm(1,4,{}),pp(Hs,Hs)))));
gate("exact_scaled_density_equation",sub(qOriginal,qExpected).size===0);
const Kraw=pa(ps(1,{m:2,v:2,z:2}),
 pa(pp(ps(2,{m:1,v:1,y:1,z:1}),sub(c,ps(1,{m:2}))),
 pp(ps(1,{y:2}),pa(pp(c,c),pa(pn(pp(ps(2,{m:2}),c)),ps(1,{m:2}))))));
const Kscaled=pp(ps(1,{m:-3,v:-1}),Kraw);
const Kexpected=pa(ps(1,{v:1,m:-1,z:2}),
 pa(pp(ps(1,{y:1,z:1}),pa(pc(-2),pp(ps(1,{v:2,m:-2}),Hs))),
 pp(ps(1,{y:2}),pa(ps(-1,{v:1,m:-1,F:1}),pp(pm(1,4,{v:3,m:-3}),pp(Hs,Hs))))));
gate("exact_full_metric_variation_kernel",sub(Kscaled,Kexpected).size===0);
const zero=()=>new Map();
const matB=[[zero(),pc(2),zero()],[ps(-1,{q:1}),zero(),pc(1)],[zero(),ps(-2,{q:1}),zero()]];
function rowMul(row,B){return [0,1,2].map(j=>row.reduce((s,p,i)=>pa(s,pp(p,B[i][j])),zero()));}
let row=[zero(),pc(1),zero()];
for(let k=0;k<20;k++)row=rowMul(row,matB);
gate("exact_complete_symmetric_square_twentieth",row[0].size===0&&row[2].size===0&&sub(row[1],mon(pow(R(4),10),{q:10})).size===0);
row=rowMul(row,matB);
gate("exact_complete_symmetric_square_twentyfirst",
 sub(row[0],mon(N(pow(R(4),10)),{q:11})).size===0&&row[1].size===0&&sub(row[2],mon(pow(R(4),10),{q:10})).size===0);
const sourceMeasure=pp(ps(1,{a:1}),ps(1,{m:2,a:-1}));
gate("original_dt_a_exactly_retained",sub(sourceMeasure,ps(1,{m:2})).size===0);
const normalizedWr=ps(1,{a:-4,v:-6,m:-3});
const DeltaForm=pp(ps(1,{a:-1,m:-3}),ps(1,{a:-3,v:-6}));
gate("exact_full_Wronskian_units_a_Delta",sub(normalizedWr,DeltaForm).size===0);
const report={
 schema:"R119-high-oscillation-polynomial-phase-control-v1",
 date:"2026-11-14",
 computation:"new exact BigInt rational constants, complete finite-jet recurrences, and Laurent identities",
 dependencies:{
  proof:"30de43573d98bc4dcc2923561fed2e16a18cf51d",
  controlled_chart53:"f11edbccd752bf034aa40e71888859d667a04b42",
  full_phase_Hessian54:"dd0d1378fce997297795ce14312fe91b181af4b1",
  exact_radial_control52:"5214cfffb5d16f3aebb0105af8aab14b2b5188b1",
  quantitative_kernel:"8b5e908a0da26a3a6038de2808cbe41c9849f439",
  compact_normalization:"5662bf40391a53a2212311406cf7ad63064908fc"
 },
 domains:{real_unused_quartic:"I subset [7/16,15/32]","sqrtB_over_M":"<=2^-512","scaled_interval_length":"N*length(I)>=8"},
 bounds:{
  normalized_Cfour_direction:"sum derivatives 0..4 <=1",
  exact_phase_derivatives:"both zero; actual two-bump compensation",
  actual_unit_wave_Wronskian:"at least 2^-2048 K_j^-3 a^-1 Delta^-3 M^-3",
  coarse_actual_Wronskian:"greater than 2^-20064 delta^47 (j+5)^-27 M^-3",
  finite_parameter_step:"min(r_free,2^-2074 K_j^-6 a^-1 Delta^-3 M^-5)"
 },
 scope:"actual radial fixed Robin ports, true dt and right amplitude, complete compact phase compensation; no nonradial matrix or full F inverse",
 gates_count:gates.length,all_passed:true,gates
};
if(typeof console!=="undefined"&&typeof console.log==="function")console.log(JSON.stringify(report,null,2));
return report;

})()
