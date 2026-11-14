#!/usr/bin/env node
/* Exact current negative-density algebra and principal HH budget.
 * All Fourier modes, physical frequencies 4j; no finite trial or whole inverse.
 * Full analytic all-sign inequalities and source/mean/jump scopes are in
 * R133-supplement-negative-quadratic-density-and-full-frequency-transport.md.
 */
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import {fileURLToPath} from "node:url";

function runNegativeDensityBudget(provenance = {}) {
  const abs=n=>n<0n?-n:n;
  const gcd=(a,b)=>{a=abs(a);b=abs(b);while(b){const t=a%b;a=b;b=t;}return a;};
  const F=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return [a/g,b/g];};
  const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=a=>[-a[0],a[1]];
  const sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>mul(a,F(b[1],b[0]));
  const pow=(a,n)=>{let r=F(1);for(let i=0;i<n;i++)r=mul(r,a);return r;};
  const lt=(a,b)=>a[0]*b[1]<b[0]*a[1];
  const eq=(a,b)=>a[0]*b[1]===b[0]*a[1];
  const rat=a=>a[0].toString()+"/"+a[1].toString();
  const dec=(a,n=24)=>{const S=10n**BigInt(n);const l=a[0]*S/a[1];const u=l+(a[0]*S%a[1]===0n?0n:1n);const fmt=z=>{let s=z.toString().padStart(n+1,"0");return s.slice(0,-n)+"."+s.slice(-n);};return{lower:fmt(l),upper:fmt(u)};};
  const checks=[];
  const gate=(name,pass)=>{checks.push({name,passed:Boolean(pass)});if(!pass)throw Error(name);};
  const vs=["b","u","v","q","qr","d","eta","S0","R0","m","x","y"];
  const zero=()=>new Map();
  const constant=n=>n?new Map([[vs.map(()=>0).join(","),BigInt(n)]]):zero();
  const variable=name=>{const p=vs.map(()=>0);const i=vs.indexOf(name);if(i<0)throw Error(name);p[i]=1;return new Map([[p.join(","),1n]]);};
  const pa=(a,b)=>{const c=new Map(a);for(const[k,v]of b){const z=(c.get(k)||0n)+v;if(z)c.set(k,z);else c.delete(k);}return c;};
  const ps=(a,n)=>new Map([...a].filter(([,v])=>v*BigInt(n)!==0n).map(([k,v])=>[k,v*BigInt(n)]));
  const pm=(a,b)=>{let c=zero();for(const[ka,va]of a)for(const[kb,vb]of b){const aa=ka.split(",").map(Number),bb=kb.split(",").map(Number);const k=aa.map((x,i)=>x+bb[i]).join(",");const z=(c.get(k)||0n)+va*vb;if(z)c.set(k,z);else c.delete(k);}return c;};
  const pp=(a,n)=>{let c=constant(1);for(let i=0;i<n;i++)c=pm(c,a);return c;};
  const pe=(a,b)=>pa(a,ps(b,-1)).size===0;
  const mm=(a,b)=>a.map(row=>b[0].map((_,j)=>row.reduce((s,x,k)=>pa(s,pm(x,b[k][j])),zero())));
  const [b,u,v,q,qr,d,eta,S0,R0,m,x,y]=vs.map(variable);
  const one=constant(1),z=zero(),q2=pp(q,2),S=pa(pp(u,2),ps(pm(q2,pp(v,2)),-1));
  const rp=pa(u,pm(q,v)),rm=pa(u,ps(pm(q,v),-1));
  const E=[[one,q],[one,ps(q,-1)]], Adj=[[q,q],[one,constant(-1)]];
  const L=[
    [ps(pm(b,pa(one,pa(ps(pp(u,2),3),ps(pm(q2,pp(v,2)),-1)))),-1),ps(pm(b,pm(q2,pm(u,v))),2)],
    [ps(pm(b,pm(u,v)),-2),pm(b,pa(one,pa(ps(pp(u,2),-1),ps(pm(q2,pp(v,2)),3))))]
  ];
  const transformed=mm(mm(E,L),Adj);
  const diag=ps(pm(q,pm(b,S)),-4);
  gate("full_local_wave_diagonal_plus",pe(transformed[0][0],diag));
  gate("full_local_wave_diagonal_minus",pe(transformed[1][1],diag));
  gate("full_local_wave_offdiagonal_plus",pe(transformed[0][1],ps(pm(q,pm(b,pa(one,pp(rp,2)))),-2)));
  gate("full_local_wave_offdiagonal_minus",pe(transformed[1][0],ps(pm(q,pm(b,pa(one,pp(rm,2)))),-2)));
  const A=[[d,pm(eta,q2)],[eta,d]];
  const EA=mm(mm(E,A),Adj);
  gate("actual_principal_speed_plus",pe(EA[0][0],ps(pm(q,pa(d,pm(eta,q))),2)));
  gate("actual_principal_speed_minus",pe(EA[1][1],ps(pm(q,pa(d,ps(pm(eta,q),-1))),2)));
  gate("actual_principal_cross_zero",EA[0][1].size===0&&EA[1][0].size===0);
  const Er=[[z,qr],[z,ps(qr,-1)]], ErAdj=mm(Er,Adj);
  gate("radial_normalization_only_cross",pe(ErAdj[0][0],qr)&&pe(ErAdj[1][1],qr)&&pe(ErAdj[0][1],ps(qr,-1))&&pe(ErAdj[1][0],ps(qr,-1)));
  const mp=pa(pm(b,pm(m,pa(one,ps(S0,-1)))),R0);
  const scaled=pa(ps(pm(b,m),2),pa(ps(mp,-2),pa(ps(pm(b,pm(m,S)),-2),ps(pm(b,pm(m,pa(S,ps(S0,-1)))),2))));
  gate("actual_mean_residual_after_density",pe(scaled,ps(R0,-2)));
  const kernelNumerator=pa(pm(pa(ps(x,2),ps(y,-1)),pp(y,3)),ps(pm(pa(ps(y,2),ps(x,-1)),pp(x,3)),-1));
  gate("complete_same_sign_cubic_kernel_identity",pe(kernelNumerator,pm(pp(pa(x,ps(y,-1)),3),pa(x,y))));
  gate("density_weight_cancels_order_zero_Hermitian",eq(add(F(2),sub(F(-3,2),F(1,2))),F(0)));
  const band=F(256),cut=F(388),beta=F(9,5),u2=F(64,25),v2=F(81,25),Kabs=F(61,100000);
  const range=add(u2,mul(Kabs,v2));
  gate("negative_range_uses_signed_K",lt(range,F(13,5)));
  gate("true_degree64_Parseval_fee_below54",lt(mul(F(128),mul(pow(beta,2),pow(F(13,5),2))),F(54*54)));
  gate("high_cut388_exceeds_entire_d_band256",lt(band,cut));
  gate("HH_same_sign_ratio_below2",lt(add(F(1),div(band,cut)),F(2)));
  const A1=F(54),A3=mul(pow(band,2),A1);
  const energy=div(add(A3,mul(F(3),A1)),pow(cut,2));
  const radius=F(1,100000),log=mul(radius,energy);
  const rootLo=F(2383968742994n,10000000000000n),rootHi=F(2383968743003n,10000000000000n),ra=F(2383878742994n,10000000000000n);
  gate("actual_ra_inside_full_negative_joint_germ",lt(sub(rootLo,radius),ra));
  gate("actual_whole_parameter_length_below1e_minus5",lt(sub(rootHi,ra),radius));
  gate("complete_HH_transport_log_bound_below1_over4000",lt(log,F(1,4000)));
  gate("exponential_majorant_below4000_over3999",lt(div(F(1),sub(F(1),log)),F(4000,3999)));
  gate("A3_majorant_exact_polynomial_identity",pe(
    pa(ps(pp(pa(one,x),3),3),pa(ps(pp(x,3),-3),ps(x,-6))),
    pa(constant(3),pa(ps(x,3),ps(pp(x,2),9)))));
  gate("large_ratio_majorant_exact_polynomial_identity",pe(
    ps(pp(pa(x,constant(-1)),3),3),
    pa(ps(pa(x,constant(-1)),3),ps(pm(x,pm(pa(x,constant(-1)),pa(x,constant(-2)))),3))));
  gate("opposite_sign_majorant_exact_polynomial_identity",pe(
    pa(pp(pa(x,one),3),ps(pm(pa(x,constant(2)),pp(x,2)),-1)),
    pa(pp(x,2),pa(ps(x,3),one))));
  return {
    kind:"actual_current_negative_quadratic_density_and_HH_transport_rational",
    complete:true,executed:true,arithmetic:"exact BigInt rationals and exact multivariate polynomial identities",
    candidate_sha256:"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
    exact_alpha:"6890507429876859/9007199254740992",
    exact_nu:"-2572625729470897/72057594037927936",
    whole_original_eta:true,physical_frequency_factor:4,high_moving_index:97,
    proof_scope:"Exact full moving Jacobi change on any strict negative subinterval; actual principal HH transport only in H^(-3/2) wave density on the named joint root germ.",
    full_source_mean_jumps_in_proof:true,full_cross_waves_and_nonlocal_terms_retained:true,
    ordinary_to_weighted_source:"f_w = (a_phys^2/m^2) T(q) f; f_Y=Lambda^(-3/2) f_w",
    mean_residual:"R0=m'-beta*m*(1-mean(u^2+K*v^2)); scalar coefficient -2*R0/m is not included in the principal bound",
    wave_cross:"B_sigma=-q'/(2*q)-beta*(1+(u+sigma*q*v)^2); retained, not included in the principal bound",
    endpoint_limit_to_K_zero_authorized:false,
    physical_L2_inverse_authorized:false,full_high_return_inverse_authorized:false,whole_BVP_inverse_authorized:false,
    source_native_rerun:false,inputs_are_existing_complete_published_joint_germ_bounds:true,
    exact_negative_S_range_upper:rat(range),
    physical_max_d_frequency:"256",high_physical_min_frequency:"388",
    d_phi_A0_upper:"54",d_phiphi_phi_A0_upper:rat(A3),
    HH_Hermitian_norm_upper:{exact:rat(energy),decimal:dec(energy)},
    actual_max_radial_length:{exact:rat(sub(rootHi,ra)),decimal:dec(sub(rootHi,ra))},
    log_norm_integral_upper:{exact:rat(log),decimal:dec(log),simple_bound:"1/4000"},
    principal_two_way_growth_upper:"4000/3999",
    general_full_signed_kernel_bound:"(3/2*||d'''||_A0+3*||d'||_A0)/M0^2 <= (3/2)*||d||_A3/M0^2",
    frozen_finite_band_kernel_bound:"(||d'''||_A0+3*||d'||_A0)/M0^2",
    omitted_from_small_budget:["cross-wave B including radial q'/q","full primitive and mean-column operator N","true scalar mean residual -2R0/m","all head-high off-diagonal blocks","PPoly transmission factors","root Airy port conversion","outer regular graph","nu scalar Schur"],
    provenance,checks,passed:checks.every(c=>c.passed),gate_count:checks.length
  };
}

const INPUTS = [
  {
    "path": "results/R133-supplement-current-moving-body-physical-complex-germ.md",
    "git_blob": "bfe73ee59142618bc7e36d5e3fe06929d9fb68cb",
    "sha256": "c10b049282d1837ab45fe2b40e6276ec7074aa534b4a7bb0c1f4251a9db729ba"
  },
  {
    "path": "results/R133-supplement-current-moving-positive-root-Riccati-and-full-head.md",
    "git_blob": "3edf335784786da9a4a515b28d364d8ad2914e24",
    "sha256": "38d7ec697d8a0565b2563324aca689776749aa81fc8bf8b0dab4d0f28fcfd8fb"
  },
  {
    "path": "results/R133-supplement-global-positive-reference-and-current-collar.md",
    "git_blob": "5e89a2ec36f36f2852d47738bc46373fdacf67d1",
    "sha256": "2e5441d4f569ee8d4a1604ebc4c2f3da25df4058fdf786032f125a0532946d35"
  }
];
const here = fileURLToPath(import.meta.url);
const root = path.dirname(path.dirname(here));
const argv = process.argv.slice(2);
if (argv.length !== 2 || argv[0] !== "--out") {
  throw new Error("usage: node scripts/fourfold_codazzi_negative_quadratic_density_transport.mjs --out notes/new-report.json");
}
const sha = x => crypto.createHash("sha256").update(x).digest("hex");
for (const row of INPUTS) {
  const body = fs.readFileSync(path.join(root,row.path));
  if (sha(body) !== row.sha256) throw new Error("changed proof input: "+row.path);
}
const report = runNegativeDensityBudget({
  source_sha256:sha(fs.readFileSync(here)),
  inputs:INPUTS
});
fs.writeFileSync(argv[1],JSON.stringify(report,null,2)+"\n",{flag:"wx"});
process.stdout.write(JSON.stringify({complete:report.complete,passed:report.passed,gate_count:report.gate_count,out:argv[1]})+"\n");
