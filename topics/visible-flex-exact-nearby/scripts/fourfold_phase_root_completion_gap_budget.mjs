#!/usr/bin/env node
// R103: exact arithmetic on previously proved complete root/contact reports.
// This does not sample a wider collar or pay a new full-cap primal/dual gap.
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { createHash } from "node:crypto";
import { dirname, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const INPUTS = [
  {
    "key": "v0",
    "path": "notes/2026-11-12-ci-canonical-v0-scaled-Wiener-summary.json",
    "sha256": "66112956b245389aa38c3d07244685ad31c29f7aae0575b8986bf80b54459ce8"
  },
  {
    "key": "root",
    "path": "notes/2026-11-12-actual-common-root-high-remainder.json",
    "sha256": "e727251cd6c187ded5782aff3a03401301d21b83fd03d419f31f716862be6253"
  },
  {
    "key": "contact",
    "path": "notes/2026-11-12-ci-direct-canonical-source-summary.json",
    "sha256": "826bda30e5d42bf47efc4fb5daa3bf6da1361bb2f4ee737486f89be9c597ca09"
  }
];
const sha256 = text => createHash("sha256").update(text,"utf8").digest("hex");

export function rootGapBudget(inputs) {
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;};
  const F=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};};
  const add=(a,b)=>F(a.n*b.d+b.n*a.d,a.d*b.d);
  const mul=(a,b)=>F(a.n*b.n,a.d*b.d);
  const div=(a,b)=>F(a.n*b.d,a.d*b.n);
  const pow=(a,k)=>F(a.n**BigInt(k),a.d**BigInt(k));
  const lt=(a,b)=>a.n*b.d<b.n*a.d;
  const dec=x=>{
    x=String(x).trim();if(x.includes("/")){const [a,b]=x.split("/");return F(a,b);}
    const m=/^([+-]?)(\d*)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/.exec(x);
    if(!m || !(m[2]||m[3]))throw Error("not an exact decimal: "+x);
    const e=Number(m[4]||0)-(m[3]||"").length;
    let n=BigInt((m[2]||"0")+(m[3]||""));if(m[1]==="-")n=-n;
    return e>=0?F(n*10n**BigInt(e)):F(n,10n**BigInt(-e));
  };
  const ballUpper=x=>{
    x=String(x).trim();if(!x.startsWith("["))return dec(x);
    const m=/^\[\s*(\S+)\s+\+\/-\s+(\S+)\s*\]$/.exec(x);
    if(!m)throw Error("unsupported Arb text: "+x);
    return add(dec(m[1]),dec(m[2]));
  };
  const ceilDecimal=(a,k=15)=>{
    if(a.n<0n)throw Error("positive upper only");
    const s=10n**BigInt(k),v=(a.n*s+a.d-1n)/a.d;
    const t=v.toString().padStart(k+1,"0");return t.slice(0,-k)+"."+t.slice(-k);
  };
  const isqrt=n=>{if(n<0n)throw Error("negative sqrt");if(n<2n)return n;let x=1n<<BigInt((n.toString(2).length+1)>>1);while(true){const y=(x+n/x)>>1n;if(y>=x)return x;x=y;}};
  const sqrtUpper=(a,k=12)=>{const s=10n**BigInt(k);let z=isqrt(a.n*s*s/a.d);if(z*z*a.d<a.n*s*s)z++;return F(z,s);};
  const pack=a=>({numerator:a.n.toString(),denominator:a.d.toString(),decimal_upper:ceilDecimal(a)});
  const checks=[];
  const check=(name,value)=>{checks.push({name,passed:!!value});if(!value)throw Error(name);};
  const v=inputs.v0,r=inputs.root,c=inputs.contact;
  check("all_three_original_reports_proved",v.proved&&r.proved&&c.proved);
  check("same_exact_root_parameter_interval",JSON.stringify(v.identity.exact_parameter_interval)===JSON.stringify(r.identity.exact_parameter_interval));
  check("root_half_width_is_1e-9",v.identity.exact_parameter_half_width==="1/1000000000");
  const M0=F(5176),M1=F(1186),qu=F(10);
  const row=m=>v.budgets.find(x=>x.high_cutoff===256&&x.weight_order===0&&x.moment===m);
  check("complete_actual_v0_Wiener_M0",lt(ballUpper(row(0).true_scaled_Wiener_upper),M0));
  check("complete_actual_v0_first_index_moment",lt(ballUpper(row(1).true_scaled_Wiener_upper),M1));
  check("true_q_is_less_than_10",lt(ballUpper(v.true_frequency.upper),qu));
  const Dv=mul(mul(F(4),qu),M1);
  const A=mul(F(27,50),Dv),B=mul(F(39,100),pow(M0,2));
  const H=F(49,102400);
  const roots=r.budgets.map(x=>{
    const L=dec(x.strict_Lambda_lower),t=dec(x.strict_cuberoot_Lambda_lower);
    const exactL=mul(mul(F(4),dec(r.q_rational_lower)),F(x.canonical_high_cutoff+1));
    check("frequency_lower_K"+x.canonical_high_cutoff,lt(L,exactL));
    check("exact_cuberoot_lower_K"+x.canonical_high_cutoff,lt(pow(t,3),L));
    const R0=add(div(A,mul(L,t)),div(B,mul(L,pow(t,2))));
    const C0=div(mul(pow(H,2),R0),F(2));
    return {canonical_input_cutoff:x.canonical_high_cutoff,all_output_modes_retained:true,
      frequency_lower:pack(L),cube_root_lower:pack(t),
      full_root_residual_L2_upper:pack(R0),
      canonical_y2_completion_C0y_L2_upper_on_paid_collar:pack(C0),
      existing_common_root_A_positive_lower:x.positive_A_lower,
      existing_root_comparison_L2_upper:x.root_remainder_L2,
      existing_root_comparison_inverse_upper:x.root_identity_plus_high_remainder_inverse_upper};
  });
  const Ereg=ballUpper(c.constants.regular_mean_extension_energy.upper);
  const Eall=ballUpper(c.constants.all_root_extension_energy.upper);
  const contacts=[{canonical_output_cutoff:"all",root_energy:pack(Eall),
    root_contact:pack(sqrtUpper(Eall)),
    root_and_regular_contact:pack(sqrtUpper(add(Eall,Ereg)))}];
  for(const x of c.high_root_contact_table.filter(x=>[64,128,256,65536].includes(x.canonical_output_cutoff_N))){
    const E=ballUpper(x.root_extension_energy.upper);
    contacts.push({canonical_output_cutoff:x.canonical_output_cutoff_N,root_energy:pack(E),
      root_contact:pack(sqrtUpper(E)),root_and_regular_contact:pack(sqrtUpper(add(E,Ereg)))});
  }
  return {kind:"R103_actual_root_completion_and_energy_gap_contact_exact_budget",
    proved_root_budget:true,proved_new_full_cap_gap:false,
    actual_parameter_identity:v.identity,
    coefficient_bounds:{v0_full_Wiener:pack(M0),v0_index_first_moment:pack(M1),
      physical_canonical_angle_derivative:pack(Dv),root_residual_Gamma_minus_4over3:pack(A),
      root_residual_Gamma_minus_5over3:pack(B)},
    paid_canonical_collar_height:pack(H),root_tables:roots,
    complete_gap_to_contact_constants:contacts,regular_contact:pack(sqrtUpper(Ereg)),
    checks,execution:{arithmetic:"exact BigInt rational arithmetic",new_geometric_sampling:false,
      input_semantics:"The actual three original reports, complete Fourier tails included."},
    limitations:["The explicit R0 formula uses the genuinely canonical R53 polynomial trial.",
      "The old physical-s polynomial trial also has its actual B_yy(0) contribution.",
      "No full paired gap, enlarged collar or PDE feedback inverse is inferred.",
      "The new y^2 completion is part of the trial and has zero root value and first conormal."]};
}

if (process.argv[1] && pathToFileURL(resolve(process.argv[1])).href === import.meta.url) {
  const inputs={};
  for(const spec of INPUTS) {
    const raw=readFileSync(spec.path,"utf8");
    if(sha256(raw)!==spec.sha256)throw Error("input SHA mismatch: "+spec.path);
    inputs[spec.key]=JSON.parse(raw);
  }
  const report=rootGapBudget(inputs);
  report.source_sha256=sha256(readFileSync(fileURLToPath(import.meta.url),"utf8"));
  report.input_reports=INPUTS;
  report.execution={...report.execution,core_executed:true,full_Node_entry_executed:true,
    runtime:"Node.js BigInt; all original UTF-8 input hashes checked"};
  const out=process.argv[2] || "notes/2026-11-12-R103-root-completion-gap-budget.json";
  mkdirSync(dirname(out),{recursive:true});
  writeFileSync(out,JSON.stringify(report,null,2)+"\n");
  process.stdout.write(JSON.stringify({checks:report.checks.length,
    proved_root_budget:report.proved_root_budget,
    proved_new_full_cap_gap:report.proved_new_full_cap_gap,
    source_sha256:report.source_sha256,report_sha256:sha256(readFileSync(out,"utf8"))})+"\n");
}
