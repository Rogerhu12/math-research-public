#!/usr/bin/env node
// R109: actual full-Fourier root comparison for the frozen-linear-potential Airy trial.
// Positive rational arithmetic is rounded only outwards. No geometric sampling.
import {readFileSync,writeFileSync,mkdirSync} from "node:fs";
import {createHash} from "node:crypto";
import {resolve,dirname} from "node:path";
import {fileURLToPath,pathToFileURL} from "node:url";
const sha=x=>createHash("sha256").update(x,"utf8").digest("hex");
const INPUTS=[
  {
    "key": "v0",
    "path": "notes/2026-11-12-ci-canonical-v0-scaled-Wiener-summary.json",
    "sha256": "66112956b245389aa38c3d07244685ad31c29f7aae0575b8986bf80b54459ce8"
  },
  {
    "key": "v1",
    "path": "notes/2026-11-12-ci-canonical-v1-scaled-Wiener-summary.json",
    "sha256": "c0050bf6f15666f1b0283d7d232c10a167d08a4bb69e42c6cc5653dc51c94c3b"
  },
  {
    "key": "root",
    "path": "notes/2026-11-12-actual-common-root-high-remainder.json",
    "sha256": "e727251cd6c187ded5782aff3a03401301d21b83fd03d419f31f716862be6253"
  },
  {
    "key": "stream",
    "path": "notes/2026-11-12-R108-canonical-stream-gap-budget.json",
    "sha256": "c1b90d922f0484358397b66c149efeb36e0eeb54412eadc3ae6ad022740d4a7c"
  }
];
export const rootBudget=function(inputs,progress=()=>{}){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;};
 const F=(n,d=1n)=>{if(typeof n==="object"&&n.n!==undefined)return n;n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}if(!d)throw Error("zero divisor");const g=gcd(n,d);return{n:n/g,d:d/g};};
 const add=(a,b)=>{a=F(a);b=F(b);return F(a.n*b.d+b.n*a.d,a.d*b.d);},neg=x=>F(-x.n,x.d),sub=(a,b)=>add(a,neg(F(b)));
 const mul=(a,b)=>{a=F(a);b=F(b);return F(a.n*b.n,a.d*b.d);},div=(a,b)=>{a=F(a);b=F(b);return F(a.n*b.d,a.d*b.n);},pow=(x,k)=>F(x.n**BigInt(k),x.d**BigInt(k));
 const lt=(a,b)=>{a=F(a);b=F(b);return a.n*b.d<b.n*a.d;};
 const dec=x=>{x=String(x);if(x.includes("/")){const[a,b]=x.split("/");return F(a,b);}const m=/^([+-]?)(\d*)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/.exec(x);if(!m)throw Error(x);let n=BigInt((m[2]||"0")+(m[3]||""));if(m[1]==="-")n=-n;const e=Number(m[4]||0)-(m[3]||"").length;return e>=0?F(n*10n**BigInt(e)):F(n,10n**BigInt(-e));};
 const iv=x=>{if(typeof x==="object")return iv(x.ball||x.upper);const s=String(x).trim();if(!s.startsWith("[")){const q=dec(s);return[q,q];}const m=/^\[\s*(\S+)\s+\+\/-\s+(\S+)\s*\]$/.exec(s);if(!m)throw Error(s);const c=dec(m[1]),r=dec(m[2]);return[sub(c,r),add(c,r)];};
 const upper=x=>iv(x)[1],ceilInt=x=>(x.n+x.d-1n)/x.d;
 const up=(x,k=30)=>{if(x.n<0n)throw Error("negative positive rounding");const s=10n**BigInt(k);return F((x.n*s+x.d-1n)/x.d,s);};
 const plus=(a,b)=>up(add(a,b)),times=(a,b)=>up(mul(a,b)),over=(a,b)=>up(div(a,b));
 const decimal=(a,k=18)=>{const s=10n**BigInt(k),q=(a.n*s+a.d-1n)/a.d,t=q.toString().padStart(k+1,"0");return t.slice(0,-k)+"."+t.slice(-k);};
 const pack=x=>{x=up(x);return{numerator:x.n.toString(),denominator:x.d.toString(),decimal_upper:decimal(x)};};
 const ir=(n,p)=>{if(n<2n)return n;const P=BigInt(p);let x=1n<<BigInt(Math.ceil(n.toString(2).length/p));let count=0;while(true){if(++count>1000)throw Error("root iteration");const y=((P-1n)*x+n/x**(P-1n))/P;if(y>=x){while((x+1n)**P<=n)x++;while(x**P>n)x--;return x;}x=y;}};
 const rootLo=(a,p)=>{const s=10n**24n;return F(ir(a.n*s**BigInt(p)/a.d,p),s);};
 const rootHi=(a,p)=>{const s=10n**24n;return F(ir(a.n*s**BigInt(p)/a.d,p)+1n,s);};
 const checks=[],check=(name,ok)=>{checks.push({name,passed:!!ok});if(!ok)throw Error(name);};
 const {v0,v1,root,stream}=inputs;
 check("original_reports_proved",[v0,v1,root].every(x=>x.proved));
 for(const k of ["exact_parameter_interval","exact_center_parameter","exact_parameter_half_width","origin_inputs_sha256","direction_sha256"])
 check("same_actual_"+k,[v1,root].every(x=>JSON.stringify(x.identity[k])===JSON.stringify(v0.identity[k])));
 check("same_eta",v0.identity.exact_parameter_half_width==="1/1000000000");
 check("complete_R108_mean_budget",stream.proved_actual_coefficient_and_mean_budget===true);
 check("same_R108_parameter_interval",JSON.stringify(stream.actual_identity.exact_parameter_interval)===JSON.stringify(v0.identity.exact_parameter_interval));
 check("q_lower",lt(F(243,25),iv(v0.true_frequency.lower)[0]));
 const airy=S=>{
  const N=24,c=[F(54,100),F(39,100),F(0)],powers=[F(1)];
  for(let n=1;n<=N+3;n++)powers[n]=times(powers[n-1],S);
  for(let n=3;n<=N+3;n++)c[n]=over(c[n-3],F(n*(n-1)));
  let e0=F(0),e1=F(0),tail0=F(0),tail1=F(0);
  for(let n=3;n<=N;n++){e0=plus(e0,times(c[n],powers[n]));e1=plus(e1,times(F(n),times(c[n],powers[n-1])));}
  for(const residue of [0,1]){const n=N-((N-residue)%3)+3;
   const r0=over(pow(S,3),F((n+3)*(n+2))),r1=over(pow(S,3),F(n*(n+2)));
   if(!lt(r0,1)||!lt(r1,1))throw Error("Airy tail");
   tail0=plus(tail0,over(times(c[n],powers[n]),sub(1,r0)));
   tail1=plus(tail1,over(times(F(n),times(c[n],powers[n-1])),sub(1,r1)));
  }
  return{e0:plus(e0,tail0),e1:plus(e1,tail1),tail0,tail1};
 };
 const rows=[];
 for(const r of root.budgets){const K=r.canonical_high_cutoff,L=dec(r.strict_Lambda_lower),cl=dec(r.strict_cuberoot_Lambda_lower);progress("root K="+K);
  check("frequency_K"+K,lt(L,mul(F(972,25),K+1)));check("cube_K"+K,lt(pow(cl,3),L));
  const cu=rootHi(L,3),symbols=[];
  for(const a of [0,1,3]){progress("symbol K="+K+" a="+a);
   const x=v0.budgets.find(z=>z.high_cutoff===K&&z.weight_order===a&&z.moment===0),
      y=v1.budgets.find(z=>z.high_cutoff===K&&z.weight_order===a&&z.moment===0);
   const V=F(ceilInt(upper(x.true_scaled_Wiener_upper))),W=F(3n*ceilInt(upper(y.true_scaled_Wiener_upper)));
   const t=over(W,pow(L,2));check("t_less_half_K"+K+"_a"+a,lt(t,F(1,2)));
   const u=rootLo(sub(1,t),3),s0=over(V,mul(L,cl)),S=over(s0,pow(u,2));check("shift_less_quarter_K"+K+"_a"+a,lt(S,F(1,4)));
   const A=airy(S),binR=sub(sub(1,div(t,3)),u);
   if(lt(binR,0))throw Error("binomial cancellation");
   const ev=plus(times(F(39,100),times(s0,sub(div(1,pow(u,2)),1))),A.e0);
   const ep=plus(times(F(39,100),binR),times(sub(2,u),A.e1));
   symbols.push({weight_order:a,v0_bound:V.n.toString(),v1_bound:W.n.toString(),slope:pack(t),cubic_factor_lower:{numerator:u.n.toString(),denominator:u.d.toString()},root_shift:pack(S),Airy_value_tail:pack(A.tail0),Airy_derivative_tail:pack(A.tail1),value_difference:pack(ev),flux_difference:pack(ep),ev,ep});
  }
  const [z0,z1,z3]=symbols;
  const high=rootHi(plus(times(z1.ev,z1.ev),times(z1.ep,z1.ep)),2);
  const allFlux=times(cu,z0.ep),all=rootHi(plus(times(z1.ev,z1.ev),times(allFlux,allFlux)),2);
  const strong=times(times(pow(L,2),times(cu,cu)),rootHi(plus(times(z3.ev,z3.ev),times(z3.ep,z3.ep)),2));
  const deltaMean=plus(times(F(831,1000),allFlux),times(mul(F(831,1000),dec("24.940215")),over(z0.ev,cl)));
  const oldMeanRow=stream.tables.find(x=>x.canonical_high_input_cutoff===K).full_mean_functional_upper;
  const oldMean=F(oldMeanRow.numerator,oldMeanRow.denominator),newMean=plus(oldMean,deltaMean);
  rows.push({K,old_complete_mean:pack(oldMean),root_change_complete_mean_fee:pack(deltaMean),new_complete_mean:pack(newMean),lambda_strict_lower:r.strict_Lambda_lower,symbols:symbols.map(({ev,ep,...x})=>x),balanced_high_high:pack(high),balanced_all_output:pack(all),balanced_all_output_flux:pack(allFlux),high_high_H0_to_H8over3:pack(strong)});
 }
 return{kind:"R109_actual_frozen_linear_potential_root_budget",proved:true,full_gap_paid:false,actual_identity:v0.identity,
  norm:"diag(barGamma^(1/3),barGamma^(-1/3)); barGamma(0)=1 and barGamma(k)=4q|k| otherwise; not an unproved physical/symplectic inverse",
  rounding:"exact BigInt rationals, each positive arithmetic upper rounded to 30 decimal places, roots enclosed at 24 places",
  Airy_series:"degree 24 plus both complete residue-class geometric tails; c Ai(0)<27/50,c |Ai'(0)|<39/100",
  complete_output_mean_and_low_rows_retained:true,common_symplectic_inverse_included:false,rows,checks,
  limitations:["The full E matrix, every angular derivative, and all cutoff terms remain in the exact residual.",
   "The complete root geometry and coefficient Fourier tails are actual; no new whole-collar geometry is claimed.",
   "High-high bound is not substituted for the separately displayed complete all-output bound."]};
};
if(process.argv[1]&&pathToFileURL(resolve(process.argv[1])).href===import.meta.url){
 const topic=resolve(dirname(fileURLToPath(import.meta.url)),".."),inputs={};
 for(const spec of INPUTS){const raw=readFileSync(resolve(topic,spec.path),"utf8");if(sha(raw)!==spec.sha256)throw Error("actual input hash mismatch: "+spec.path);inputs[spec.key]=JSON.parse(raw);}
 const report=rootBudget(inputs);
 report.input_reports=INPUTS;report.source_sha256=sha(readFileSync(fileURLToPath(import.meta.url),"utf8"));
 report.execution={core_executed:true,full_Node_entry_executed:true,runtime:"Node.js exact BigInt rational arithmetic",new_geometric_sampling:false};
 const out=process.argv[2]||resolve(topic,"notes/2026-11-12-R109-frozen-linear-Airy-root-budget.json");
 mkdirSync(dirname(out),{recursive:true});writeFileSync(out,JSON.stringify(report,null,2)+"\n");
 process.stdout.write(JSON.stringify({checks:report.checks.length,all_passed:report.checks.every(x=>x.passed),source_sha256:report.source_sha256,report_sha256:sha(readFileSync(out,"utf8")),full_gap_paid:false})+"\n");
}
