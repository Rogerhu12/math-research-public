// R115 exact finite constants; all scientific inputs are declared rationals.
// This does not rerun source R72's infinite-tail certificates.
export function runBudget() {
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;}
  function R(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};}
  const add=(a,b)=>R(a.n*b.d+b.n*a.d,a.d*b.d);
  const neg=a=>R(-a.n,a.d);
  const sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>R(a.n*b.n,a.d*b.d);
  const div=(a,b)=>R(a.n*b.d,a.d*b.n);
  const pow=(a,n)=>R(a.n**BigInt(n),a.d**BigInt(n));
  const two=n=>n>=0?R(1n<<BigInt(n)):R(1n,1n<<BigInt(-n));
  const lt=(a,b)=>a.n*b.d<b.n*a.d;
  const eq=(a,b)=>a.n*b.d===b.n*a.d;
  const str=a=>a.n.toString()+"/"+a.d.toString();
  const checks=[];
  function check(name,ok,details){checks.push({name,pass:!!ok,...(details||{})});if(!ok)throw Error("gate failed: "+name);}
  const one=R(1),kap=two(-60),H=R(256,85),r=R(13,48),den=sub(one,mul(mul(R(2),r),kap));
  check("label_quarter_self_map",lt(add(div(H,R(4)),kap),one));
  check("unit_state_contraction",lt(mul(R(2),kap),one));
  check("state_at_label_twelfth",lt(div(H,sub(one,kap)),R(13,4)));
  check("derivative_invertible",lt(mul(mul(R(2),r),kap),one));
  check("DX_norm",lt(div(H,den),R(13,4)));
  const diff=div(mul(mul(mul(R(2),r),kap),H),den);
  check("DX_minus_H",lt(diff,mul(R(2),kap)),{bound:str(diff),claimed:str(two(-59))});
  check("D2R_Cauchy_radius",lt(add(r,R(1,2)),one));
  const d2=div(mul(mul(R(4),kap),pow(R(13,4),2)),den);
  check("D2X_43kappa",lt(d2,mul(R(43),kap)));
  check("D2X_2minus54",lt(d2,two(-54)),{bound:str(d2)});
  check("quadratic_remainder",lt(div(d2,R(2)),two(-55)));
  const beta=R(1467,256);
  check("beta_identity",eq(beta,sub(R(23,4),R(5,256))));
  check("beta_positive",lt(R(0),beta));
  check("beta_above_11_over_2",lt(R(11,2),beta));
  check("constant_width_h5",lt(pow(R(100,9),5),two(18)));
  check("deep_width_h5",lt(two(-15),two(18)));
  check("width_lower_constant",lt(R(1,16),R(9,100)));
  check("delta129_below_2minus132",lt(R(1n,25n*(1n<<128n)),two(-132)));
  check("geometric_mean_integral",lt(one,add(beta,one)));
  check("physical_epsilon_over_rho",lt(mul(R(5,8),two(439)),two(440)));
  check("C2_chart_small_exponent",lt(R(220),sub(mul(R(132),beta),R(536))));
  check("DF_physical_Cauchy",lt(R(6),R(8)));
  check("D2F_physical_Cauchy",lt(R(144),R(256)));
  check("horizontal_jet_all_terms",lt(R(6*1024*4),two(16)));
  check("mean_inverse",lt(R(64,55),R(2)));
  check("exp2012_elementary",3n**2012n < 1n<<4024n);
  check("local_source_constant_port",38+4024+5+6 < 4096);
  check("local_source_constant_jet",38+4024+5+15 < 4096);
  const s=R(11607,4),mm=R(11631,4),mi=R(11603,4);
  check("mean_integral_power",eq(add(s,R(6)),mm));
  check("mean_lift_power",eq(sub(mm,R(7)),mi));
  check("ordinary_port_remaining_power",eq(sub(sub(s,R(2890)),R(39,4)),R(2)));
  check("mean_port_remaining_power",eq(sub(sub(mi,R(2890)),R(39,4)),one));
  check("ordinary_jet_remaining_power",eq(sub(s,R(2893)),R(35,4)));
  check("mean_jet_remaining_power",eq(sub(mi,R(2893)),R(31,4)));
  check("ordinary_jet_flat",lt(beta,R(35,4)));
  check("mean_jet_flat",lt(beta,R(31,4)));
  check("strong_source_direct_margin",4200-(38+4024+5+6)-10>80);
  check("strong_source_mean_margin",4182-(38+4024+6)-10>80);
  check("source_Green_state",lt(div(R(8192),den),two(14)));
  check("source_H_state",lt(div(H,den),R(4)));
  const embedPower=sub(R(2892),R(310,256));
  check("R15_source_embedding_exponent",lt(R(0),embedPower));
  check("R15_source_embedding_margin",lt(R(559),mul(R(132),embedPower)));

  // Sparse exact polynomials, independent of any floating-point algebra.
  const nv=9;
  const key=v=>v.join(",");
  function P(c=0n){const m=new Map();if(c)m.set(key(Array(nv).fill(0)),BigInt(c));return m;}
  function variable(i){const a=Array(nv).fill(0);a[i]=1;return new Map([[key(a),1n]]);}
  function plus(a,b){const c=new Map(a);for(const [k,v] of b){const z=(c.get(k)||0n)+v;if(z)c.set(k,z);else c.delete(k);}return c;}
  function minus(a,b){return plus(a,new Map([...b].map(([k,v])=>[k,-v])));}
  function times(a,b){const c=new Map();for(const [ka,va]of a)for(const[kb,vb]of b){const aa=ka.split(",").map(Number),bb=kb.split(",").map(Number);const k=key(aa.map((x,i)=>x+bb[i]));const z=(c.get(k)||0n)+va*vb;if(z)c.set(k,z);else c.delete(k);}return c;}
  const sq=a=>times(a,a),O=P(1n);
  const [rr,w,wr,kp,pp,pt,kt,kr,zz]=Array.from({length:nv},(_,i)=>variable(i));
  const EE=plus(O,sq(w)),kk=plus(w,kp),DD=minus(minus(EE,sq(kk)),times(EE,sq(pp)));
  const angular=plus(kk,times(EE,pt));
  const B=minus(minus(times(times(rr,angular),plus(wr,kr)),times(EE,sq(minus(kt,pp)))),times(times(times(rr,w),wr),plus(minus(O,sq(pp)),times(kk,pt))));
  const Balt=minus(plus(times(times(rr,angular),kr),times(times(rr,wr),minus(plus(kp,pt),times(w,minus(times(kp,pt),sq(pp)))))),times(EE,sq(minus(kt,pp))));
  check("density_Darboux_polynomial_identity",minus(B,Balt).size===0);
  const detHorizontal=minus(times(minus(EE,sq(kk)),times(sq(rr),minus(O,sq(pp)))),sq(times(times(kk,rr),pp)));
  check("horizontal_determinant",minus(detHorizontal,times(sq(rr),DD)).size===0);
  // Cleared denominator checks for the physical ground-state shear.
  const nu=kp, C=pp, Cr=pt, W=w, Z=zz, rvar=rr;
  const denU=minus(nu,O),U_num=times(W,minus(times(nu,C),times(rvar,Cr)));
  const strain=minus(plus(times(times(times(rvar,W),Cr),denU),times(denU,U_num)),times(times(times(nu,W),C),denU));
  check("horizontal_physical_U_strain",strain.size===0);
  const A=plus(Z,times(rvar,W));
  const fluxLeft=times(times(W,sq(Z)),plus(times(times(A,Z),Cr),times(A,U_num)));
  const fluxRight=times(times(A,sq(Z)),plus(times(times(W,Z),Cr),times(W,U_num)));
  // This compares the two numerators with a dummy U_num; no division by it occurs.
  check("grounded_flux_shear",minus(fluxLeft,fluxRight).size===0);

  return {
    schema:"visible-exact-R115-true-tail-chart-budget-v1",
    scope:"Exact finite rational gates for a proved infinite-tail chart theorem; no new native collar run and no full-feedback claim.",
    inputs:{H:str(H),kappa_upper:str(kap),state_radius:str(r),beta:str(beta),source_power:str(s),source_prefactor_power:4200,
      source_R72_blob:"a7c78793ba18724a4f0553b6ccd55259b8f4df92",
      source_R21_blob:"a3b55246f416d73a4c4fe2b0b1545f0bfee0863d",
      source_R25_blob:"be20257721fed270c59a4024427042fc76ee0073"},
    checks,all_pass:checks.every(x=>x.pass),
    claims:{actual_full_tail_chart:true,all_internal_labels:true,continuous_weighted_sources:true,mean_holonomy_load_retained:true,
      complete_C2_horizontal_reconstruction:true,regular_full_Robin_perturbation_paid:false,global_exact_zero_constructed:false}
  };
}
if(typeof process!=="undefined" && process.argv && /fourfold_true_tail_chart_budget[.]mjs$/.test(process.argv[1]||"")){
  console.log(JSON.stringify(runBudget(),null,2));
}
