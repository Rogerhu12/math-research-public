// Exact coefficient checks for the full periodic half-order kernel bounds.
const abs=n=>n<0n?-n:n;
function gcd(a,b){a=abs(a);b=abs(b);while(b){const c=a%b;a=b;b=c;}return a;}
function q(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");
 if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];}
const add=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const sub=(a,b)=>q(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
const mul=(a,b)=>q(a[0]*b[0],a[1]*b[1]);
const lt=(a,b)=>a[0]*b[1]<b[0]*a[1];
const out=a=>({exact:String(a[0])+"/"+String(a[1]),approximate:Number(a[0])/Number(a[1])});
function atanSum(denominator,terms){
 const d=BigInt(denominator);let answer=q(0n);
 for(let k=0;k<terms;k++)answer=add(answer,
   q(k%2?-1n:1n,BigInt(2*k+1)*d**BigInt(2*k+1)));
 return answer;
}
export function computeKernelConstantBudget(sourceSha,consumerSha,proofSha){
 for(const x of [sourceSha,consumerSha,proofSha])
   if(!/^[0-9a-f]{64}$/.test(x))throw Error("complete source SHA required");
 const low=sub(mul(q(16n),atanSum(5,8)),mul(q(4n),atanSum(239,1)));
 const high=sub(mul(q(16n),atanSum(5,9)),mul(q(4n),atanSum(239,2)));
 const gates=[];
 function gate(name,value){if(!value)throw Error(name);gates.push({name,passed:true});}
 gate("Machin lower sum positive",lt(q(0n),low));
 gate("Machin lower below upper",lt(low,high));
 gate("pi lower above 25/8",lt(q(25n,8n),low));
 gate("pi upper below 22/7",lt(high,q(22n,7n)));
 const zero=q(113n,50n),signed=q(12n,5n);
 gate("4/sqrt(pi) strictly below 113/50",
      lt(q(16n),mul(low,mul(zero,zero))));
 gate("6/sqrt(2*pi) strictly below 12/5",
      lt(q(36n),mul(mul(q(2n),low),mul(signed,signed))));
 return {
   kind:"R110_complete_periodic_fractional_kernel_rational_constants",
   complete:true,arithmetic:"exact reduced BigInt; comparisons cross-multiply integers",
   pi_enclosure:{lower:out(low),upper:out(high),
      identity:"pi=16 atan(1/5)-4 atan(1/239)",
      lower_terms:[8,1],upper_terms:[9,2],
      justification:"alternating Taylor sums; positive even truncations are lower, positive odd truncations are upper"},
   universal_coefficients:{
      zero_order_radical:{exact_formula:"4/sqrt(pi)",strict_rational_upper:out(zero)},
      signed_remainder_radical:{exact_formula:"6/sqrt(2*pi)",strict_rational_upper:out(signed)},
      exact_zero_mode_derivative_coefficient:out(q(3n,2n))
   },
   gates,
   contract:{
      physical_derivative:"Dtheta with Fourier frequencies 4k; J=max(1,|4k|)^1/2",
      zero_order:"||[J,a]|| <= O+(4/sqrt(pi))*sqrt(O*||Da||infty)",
      signed_remainder:"||D[J,a]-(Da)J/2|| <= (6/sqrt(2*pi))*sqrt(||Da||infty*||D2a||infty)+(3/2)||Da||infty",
      oscillation:"O bounds ||a-a_c||infty for one actual constant; a_c need not be the mean",
      full_mean:true,full_frequency:true,
      not_a_computed_actual_core_rate:true
   },
   provenance:{
      source:"scripts/fourfold_fractional_kernel_budget_exact.mjs",
      source_sha256:sourceSha,
      native_consumer:"scripts/fourfold_phase_strict_core_kernel_tame_energy.py",
      native_consumer_sha256:consumerSha,
      proof:"results/R110-complete-periodic-kernel-tame-bounds.md",
      proof_sha256:proofSha,
      execution:"The identical pure computeKernelConstantBudget function was executed in V8; native consumer and Node file-I/O wrapper have not run."
   }
 };
}
// NATIVE_CLI: exact replay and file persistence only.
import { readFile,writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { createHash } from "node:crypto";
if(process.argv[1]&&resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 const root=resolve(process.argv[2]??".");
 const outpath=process.argv[3]??"/tmp/R110-fractional-kernel-constants.json";
 const digest=s=>createHash("sha256").update(s,"utf8").digest("hex");
 const source=await readFile(fileURLToPath(import.meta.url),"utf8");
 const consumer=await readFile(resolve(root,"scripts/fourfold_phase_strict_core_kernel_tame_energy.py"),"utf8");
 const proof=await readFile(resolve(root,"results/R110-complete-periodic-kernel-tame-bounds.md"),"utf8");
 const report=computeKernelConstantBudget(digest(source),digest(consumer),digest(proof));
 await writeFile(outpath,JSON.stringify(report,null,2)+"\n");
 process.stdout.write(JSON.stringify({complete:true,gates:report.gates.length,output:outpath})+"\n");
}
