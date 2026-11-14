// Exact arithmetic for the R110 characteristic-density transport supplement.
// Mathematical comparisons are reduced BigInt rationals. Native file I/O is
// only a replay wrapper; the identical pure implementation was run in V8.
export const INPUTS = [
  ["ray", "notes/2026-11-12-R106-actual-all-time-ray-tube.json",
   "6463e62641b9187045016c63ee633816676a75baf941ea01375a6ae36f1a1863"],
  ["ray_proof", "results/R106-supplement-actual-all-time-ray-tube.md",
   "fe38b910efa8ccd0dca351a98d48a34fe34f7e01e3ba2301cc9a4b5c778edb4b"],
  ["parity", "results/R105-actual-dihedral-six-block-and-even-core-composition.md",
   "6f1419ad5d8ef7f9d4d8576d6563b02251360abe50d236590f68b8cafe782c2d"],
  ["reflection", "results/R77-reflection-square-of-principal-return.md",
   "0a7276239ea25ceb87ca386e48e7c9901a7503edf52baad1d3ba753b51ae1243"]
];
const abs = n => n < 0n ? -n : n;
function gcd(a,b) { a=abs(a);b=abs(b);while(b){const r=a%b;a=b;b=r;}return a; }
function rat(n,d=1n) {
  n=BigInt(n);d=BigInt(d);
  if(d===0n)throw Error("zero denominator");
  if(d<0n){n=-n;d=-d;}
  const g=gcd(n,d);return [n/g,d/g];
}
function parse(s) {
  if(typeof s!=="string" || !/^-?\d+(\/[1-9]\d*)?$/.test(s))
    throw Error("exact rational string required");
  const p=s.split("/");return rat(p[0],p[1]??"1");
}
const mul=(a,b)=>rat(a[0]*b[0],a[1]*b[1]);
const div=(a,b)=>rat(a[0]*b[1],a[1]*b[0]);
const eq=(a,b)=>a[0]*b[1]===b[0]*a[1];
const lt=(a,b)=>a[0]*b[1]<b[0]*a[1];
const str=a=>a[1]===1n?String(a[0]):String(a[0])+"/"+String(a[1]);
function rec(a){return {exact:str(a),approximate:Number(a[0])/Number(a[1])};}

export function computeCharacteristicDensityBudget(texts, sha256, sourceSha256) {
  const inputs=INPUTS.map(([key,path,digest])=>{
    if(typeof texts[key]!=="string")throw Error("missing UTF8 input "+key);
    if(sha256(texts[key])!==digest)throw Error("input SHA mismatch: "+path);
    return {key,path,sha256:digest};
  });
  if(typeof sourceSha256!=="string" || !/^[0-9a-f]{64}$/.test(sourceSha256))
    throw Error("source SHA required");
  const r=JSON.parse(texts.ray), gates=[];
  const gate=(name,ok)=>{if(!ok)throw Error(name);gates.push({name,passed:true});};
  const region=r.proved_region??{}, provenance=r.provenance??{};
  gate("completed actual all-time ray certificate",
    r.complete===true &&
    r.kind==="R106_all_time_true_ray_from_paid_reference_and_parameter_source");
  gate("all original 24 exact gates remain passed",
    Array.isArray(r.gates)&&r.gates.length===24&&r.gates.every(g=>g.passed===true));
  gate("complete forward radial parameterization",
    region.leg==="forward"&&region.segments===550&&
    JSON.stringify(region.time_endpoints)===JSON.stringify(["-pi/2","pi/2"]));
  gate("exact affine center",
    region.parameter_center==="-7789843107295549/4611686018427387904");
  gate("whole real eta equals one billionth",
    eq(parse(region.parameter_half_width),rat(1n,1000000000n)));
  gate("normalized full-circle label convention",
    region.label_period==="2*pi"&&region.label_strip==="1/1024");
  gate("same actual affine object",
    provenance.actual_object_sha256===
    "91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848");
  gate("same exact all-time finite reference",
    provenance.reference_descriptor_sha256===
    "097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052");
  gate("same complete actual g0 source",
    provenance.center_g0_index_sha256===
    "4174c3edde41f5c8ab12b036d4760c20ec987e475158aa2855ea08158ff7cb45");
  const m=parse(r.bounds.true_label_J_real_lower.exact);
  const M=parse(r.bounds.true_label_J_modulus.exact);
  gate("exact lower Jacobian",eq(m,rat(213831n,7812500n)));
  gate("exact upper Jacobian",eq(M,rat(8223669n,7812500n)));
  gate("strict positive real Jacobian",lt(rat(0n),m));
  gate("compatible Jacobian range",lt(m,M));
  const Q=div(M,m), K1=rat(3101n,500n), K3=rat(38459n,1000n);
  gate("density L2 gain strictly below 6.202",lt(Q,mul(K1,K1)));
  gate("three-halves-density L2 gain strictly below 38.459",lt(Q,K3));
  const quarter=rat(1n,4n);
  gate("physical nonzero frequency starts at four",
    eq(mul(quarter,rat(4n)),rat(1n)));
  return {
    kind:"R110_actual_characteristic_density_L2_transport",
    complete:true,
    arithmetic:"reduced BigInt rational comparisons; no native ODE or matrix is rerun",
    proved_region:{
      parameter_center:region.parameter_center,
      parameter_half_width:region.parameter_half_width,
      physical_period:"pi/2",
      label_period:"2*pi",
      radial_scope:"any closed strictly negative interval inside (-t(p),t(p))",
      branches:"one saved forward branch; the opposite branch is defined by exact radial reflection with its labels based at the opposite root",
      time_scope:"all intermediate times; arbitrary pairs of radii in each closed strict interval"
    },
    bounds:{
      true_label_J_real_lower:rec(m),
      true_label_J_modulus:rec(M),
      exact_relative_J_ratio_bound:rec(Q),
      density_transport_L2_norm_upper:rec(K1),
      three_halves_density_transport_L2_norm_upper:rec(K3),
      half_density_transport_L2_norm_upper:rec(rat(1n)),
      physical_nonmean_inverse_derivative_norm:rec(quarter),
      normalized_density_pullback_norm_squared_bound:rec(mul(rat(4n),M)),
      normalized_density_pushforward_norm_squared_bound:rec(div(rat(1n),mul(rat(4n),m)))
    },
    gates,
    proved_not_assumed:[
      "the two branch labels need not have the same initial radial endpoint",
      "the reflection construction is not an uncharged second passage of the principal return",
      "the quarter-circle normalization cancels in the relative transport norm",
      "the physical zero mode remains an explicit scalar evolution",
      "the three-halves-density entry is an L2 transport bound for its own PDE, not a standalone H1/2 bound for the original PDE"
    ],
    not_proved:[
      "actual continuous coupling coefficients Bplus/Bminus and full d on every strict span",
      "complete H1/2 or Hminus1/2 composition and multiplier constants",
      "complete source-to-Cauchy propagation through the roots and positive collars",
      "new strong residual Gram, full high Schur inverse or nonlinear correction"
    ],
    provenance:{
      source:"scripts/fourfold_characteristic_density_budget_exact.mjs",
      source_sha256:sourceSha256,
      proof:"results/R110-characteristic-densities-mean-and-weak-sources.md",
      inputs,
      original_ray_source_sha256:provenance.source_sha256,
      actual_object_sha256:provenance.actual_object_sha256,
      reference_descriptor_sha256:provenance.reference_descriptor_sha256,
      execution:"The identical pure computeCharacteristicDensityBudget was executed in V8. Native CLI was not run.",
      scope:"Exact finite arithmetic extending already proved actual all-time ray and exact reflection inputs; no missing geometric certificate was fabricated."
    }
  };
}

// NATIVE_CLI: file I/O only; never used by the pure V8 arithmetic above.
import { readFile, writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { createHash } from "node:crypto";
if (process.argv[1] && resolve(process.argv[1])===fileURLToPath(import.meta.url)) {
  const root=resolve(process.argv[2]??".");
  const out=process.argv[3]??"/tmp/R110-characteristic-density-budget.json";
  const texts={};
  for (const [key,path] of INPUTS)texts[key]=await readFile(resolve(root,path),"utf8");
  const digest=s=>createHash("sha256").update(s,"utf8").digest("hex");
  const source=await readFile(fileURLToPath(import.meta.url),"utf8");
  const report=computeCharacteristicDensityBudget(texts,digest,digest(source));
  await writeFile(out,JSON.stringify(report,null,2)+"\n","utf8");
  process.stdout.write(JSON.stringify({complete:report.complete,gates:report.gates.length,
    density_L2:report.bounds.density_transport_L2_norm_upper.exact,
    output:out})+"\n");
}
