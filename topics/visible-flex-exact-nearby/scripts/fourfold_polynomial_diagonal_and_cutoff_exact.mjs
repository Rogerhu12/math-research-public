#!/usr/bin/env node
// R104. Run from topics/visible-flex-exact-nearby:
// node scripts/fourfold_polynomial_diagonal_and_cutoff_exact.mjs --out notes/2026-11-12-R104-polynomial-diagonal.json
// Optional --bounds path.json requires actual, separately certified finite-window bounds.
import {readFileSync,writeFileSync} from "node:fs";
import {createHash} from "node:crypto";
import {pathToFileURL} from "node:url";

export function r104Core(phaseText, betaText) {
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a};
  const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d}const g=gcd(n,d);return [n/g,d/g]};
  const read=s=>{if(typeof s!=="string")throw Error("fractions must be exact strings");const t=s.split("/");if(t.length>2)throw Error("bad fraction");return Q(t[0],t[1]??"1")};
  const sub=(a,b)=>Q(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
  const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
  const cmp=(a,b)=>(a[0]*b[1]>b[0]*a[1]?1:(a[0]*b[1]<b[0]*a[1]?-1:0));
  const str=a=>a[1]===1n?a[0].toString():a[0]+"/"+a[1];
  const gates=[];
  const check=(name,pass,details={})=>{gates.push({name,pass,...details});if(!pass)throw Error("R104 gate failed: "+name)};
  const p=JSON.parse(phaseText), beta=JSON.parse(betaText);
  check("actual_R102_all_positive_frequency_certificate",
    p.complete_arithmetic===true&&p.all_positive_frequency_pure_phase_gap_proved===true
    &&p.exception_count===0);
  check("exact_R102_scaled_gap",p.uniform_scaled_phase_gap_lower==="17/100");
  check("exact_R102_remainder_contract",
    p.residual_contract.scaled_remainder_at_most==="7/100"
    &&p.residual_contract.remaining_scaled_phase_margin==="1/10"
    &&p.residual_contract.divisor_lower==="1/(5*pi*j)");
  check("same_quadratic_minus_root",p.exact_quadratic.A==="1323907691653283951"
    &&p.exact_quadratic.B_signed==="-1460270480137213085"
    &&p.exact_quadratic.C==="402669666587037055"
    &&p.exact_quadratic.discriminant==="5"&&p.exact_quadratic.root==="minus");
  check("same_actual_beta_interval",p.inputs.beta_interval[0]===beta.beta.lower_exact
    &&p.inputs.beta_interval[1]===beta.beta.upper_exact&&beta.complete===true);
  const lo=read(beta.beta.lower_exact),hi=read(beta.beta.upper_exact);
  check("beta_strictly_above_37",cmp(lo,Q(37n))>0,{lower_exact:str(lo)});
  check("beta_strictly_below_37p1",cmp(hi,Q(371n,10n))<0,{upper_exact:str(hi)});
  check("ordered_beta_interval",cmp(lo,hi)<0);
  const j0=500n;
  const lowSquare=37n*37n,lowRequired=2n*(j0-1n)+1n;
  check("all_low_modes_radial_gap_above_one",lowSquare>lowRequired,
    {j_min:"1",j_max:(j0-1n).toString(),beta_lower_squared:lowSquare.toString(),
     largest_two_j_plus_one:lowRequired.toString()});
  const betaCoarse=Q(371n,10n);
  const atanError=div(mul(mul(betaCoarse,betaCoarse),betaCoarse),Q(3n*j0*j0));
  const allowance=Q(7n,100n),newMargin=sub(Q(17n,100n),atanError);
  check("all_high_modes_atan_error_below_contract",cmp(atanError,allowance)<0,
    {j_min:j0.toString(),scaled_atan_error_upper:str(atanError),
     allowance:str(allowance),unused_allowance_lower:str(sub(allowance,atanError))});
  check("all_high_modes_scaled_gap_above_one_tenth",cmp(newMargin,Q(1n,10n))>0,
    {scaled_phase_gap_lower:str(newMargin)});
  const piHi=read(p.transcendental_enclosures.pi[1]);
  check("exact_Machin_pi_upper_below_22_over_7",cmp(piHi,Q(22n,7n))<0);
  check("low_gap_dominates_global_rational_gap",cmp(Q(1n),Q(7n,110n))>0);
  return {
    kind:"R104_exact_polynomial_diagonal_all_modes",
    complete_scalar_arithmetic:true,
    actual_beta_interval:[str(lo),str(hi)],
    exact_quadratic:p.exact_quadratic,
    model:"d_j=1+exp(2*pi*i*alpha*j)*(1+i*beta/j), j>=1",
    angular_convention:"j is the normalized 2*pi label frequency of R100/R102; no physical-frequency replacement",
    low_modes:{range:["1","499"],j_times_diagonal_modulus_lower:"1",
      reason:"sqrt(j^2+beta^2)-j>1 since beta>37 and 37^2>2*499+1"},
    high_modes:{range:["500","infinity"],scaled_atan_error_upper:str(atanError),
      scaled_phase_gap_lower:str(newMargin),
      complex_diagonal_modulus_lower:"1/(5*pi*j)",
      reason:"radius sqrt(1+beta^2/j^2)>=1 increases squared modulus of 1+radius*exp(i*phase)"},
    all_modes:{complex_diagonal_modulus_lower:"7/(110*j)",
      diagonal_inverse_Hs_plus_1_to_Hs_upper:"110/7",
      normalized_high_inverse_if_Neumann_half_upper:"220/7"},
    gates,
    actual_full_b_multiplier_norm_not_supplied:true,
    actual_strong_four_thirds_remainder_norm_not_supplied:true,
    actual_high_cutoff_not_claimed:true,
    actual_augmented_low_Schur_inverse_not_supplied:true,
    full_PDE_inverse_not_inferred:true
  };
}

export function strongCutoffFromExactBounds(input) {
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a};
  const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<=0n)throw Error("positive denominator required");const g=gcd(n,d);return[n/g,d/g]};
  const read=s=>{if(typeof s!=="string")throw Error("exact fraction string required");const z=s.split("/");if(z.length>2)throw Error("bad fraction");return Q(z[0],z[1]??"1")};
  const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]);
  const ceil=a=>(a[0]+a[1]-1n)/a[1];
  const st=a=>a[1]===1n?a[0].toString():a[0]+"/"+a[1];
  const a=read(input.a_bound),b=read(input.b_bound),beta=read(input.beta_abs_bound),
    rem=read(input.remainder_four_thirds_bound);
  for(const q of[a,b,beta,rem])if(q[0]<0n)throw Error("negative upper bound");
  const k2=mul(Q(4n),mul(a,add(b,beta))),k43=mul(Q(3n),rem);
  const n0=ceil(mul(Q(2n),a)),x=mul(Q(440n,7n),k2),y=mul(Q(440n,7n),k43);
  const ns=[1n,n0,ceil(x),ceil(mul(mul(y,y),y))];
  const N=ns.reduce((m,n)=>m>n?m:n,1n);
  return {kind:"conditional_R104_strong_cutoff_budget",input,
    N0:(n0>1n?n0:1n).toString(),K2:st(k2),K_four_thirds:st(k43),N:N.toString(),
    individual_Neumann_terms_upper:["1/4","1/4"],sum_upper:"1/2",
    diagonal_gap_constant:"7/110",high_inverse_bound:"220/7",
    actual_input_enclosures_must_be_independently_supplied:true};
}

const inputSpecs=[
  {
    "path": "notes/2026-11-12-R102-nearby-quadratic-phase.json",
    "sha256": "401f76fe56d427594345d913ea08a4af7aef9ceb91610c35ce5269bd256169cc"
  },
  {
    "path": "notes/2026-11-12-beta-derivative-independent-cover-and-transfer-audit.json",
    "sha256": "1047f423a77d07aa14093b17fcf28376243857d8bf738b5d62f65f0f3dea7923"
  }
];
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href) {
  const args=process.argv.slice(2);
  const opt=k=>{const i=args.indexOf(k);return i<0?null:args[i+1]};
  const texts=inputSpecs.map(s=>{
    const text=readFileSync(s.path,"utf8");
    const digest=createHash("sha256").update(text,"utf8").digest("hex");
    if(digest!==s.sha256)throw Error("input SHA256 mismatch: "+s.path);
    return text;
  });
  const report=r104Core(...texts);
  report.provenance={input_files:inputSpecs,all_input_UTF8_SHA256_verified:true,
    source_sha256:createHash("sha256").update(readFileSync(new URL(import.meta.url))).digest("hex"),
    runtime:"Node JavaScript BigInt exact reduced fractions",
    mathematical_core_actually_executed:true};
  if(opt("--bounds"))report.conditional_strong_budget=strongCutoffFromExactBounds(
    JSON.parse(readFileSync(opt("--bounds"),"utf8")));
  const output=JSON.stringify(report,null,2)+"\n";
  if(opt("--out"))writeFileSync(opt("--out"),output,"utf8");else process.stdout.write(output);
}
