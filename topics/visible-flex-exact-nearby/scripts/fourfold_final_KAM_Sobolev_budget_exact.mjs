// Actual final R101 KAM-coordinate Sobolev bounds.
// All comparisons use reduced BigInt rationals; native I/O only replays them.
export const INPUTS = [
  [
    "kam",
    "notes/2026-11-12-split-Wiener-R31-exact.json",
    "f887bcce5a5ed8f2de2fee6a398aec86b323b91b64560f7cb84a3d6b918d521a"
  ],
  [
    "pre",
    "data/phase_ring_continuation/step5_half_prenewton_43308150283/report.json",
    "030cf8444f5a0cc5058e7ce056b2b310328e7d78a842582273ffb70d2f6f720a"
  ],
  [
    "sobolev",
    "notes/2026-11-13-R116-true-ray-Sobolev-coordinates.json",
    "3917745a9fbf7bcaa792a63c2164edd11565007ab6445da1437f9fe1eb1c9d94"
  ],
  [
    "reference",
    "notes/2026-11-12-step5-forward-reference-derivative-complete-summary.json",
    "d1dd69ac94f5912c828a6e22856badcb69bf324fdc7fc9a43f05493161363dc9"
  ],
  [
    "ray",
    "notes/2026-11-12-R106-actual-all-time-ray-tube.json",
    "6463e62641b9187045016c63ee633816676a75baf941ea01375a6ae36f1a1863"
  ],
  [
    "kam_proof",
    "results/R101-actual-split-wiener-circle-conjugacy.md",
    "de58688c525f1fdf92ca8236a141b3ce640238ff39d72407b0d330c0949e80cf"
  ],
  [
    "r31_proof",
    "results/R31-actual-parameter-circle-normalization.md",
    "e564eec1fce55ea2c341d5af9be8f5a8bede2f057062667823ad0a7a9b992f09"
  ],
  [
    "ray_proof",
    "results/R106-supplement-actual-all-time-ray-tube.md",
    "fe38b910efa8ccd0dca351a98d48a34fe34f7e01e3ba2301cc9a4b5c778edb4b"
  ],
  [
    "sobolev_proof",
    "results/R116-true-ray-Sobolev-coordinates-and-density-tame-bound.md",
    "138bae996321d5e7f933b56836c077c0191eaad266f4806fa25e8cf551d1aed8"
  ],
  [
    "prenewton_proof",
    "results/R100-nearby-quadratic-and-exact-prenewton-transport.md",
    "136fa3a921f6992d32edb653343e77d5f15926c8e1d7d8038ed90552deaa633f"
  ]
];

const abs=n=>n<0n?-n:n;
function gcd(a,b){a=abs(a);b=abs(b);while(b){const r=a%b;a=b;b=r;}return a;}
function rat(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");
 if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];}
const add=(a,b)=>rat(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>[-a[0],a[1]];
const sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>rat(a[0]*b[0],a[1]*b[1]);
const div=(a,b)=>rat(a[0]*b[1],a[1]*b[0]);
const pow=(a,n)=>rat(a[0]**BigInt(n),a[1]**BigInt(n));
const eq=(a,b)=>a[0]*b[1]===b[0]*a[1];
const lt=(a,b)=>a[0]*b[1]<b[0]*a[1];
const str=a=>a[1]===1n?String(a[0]):String(a[0])+"/"+String(a[1]);
function parse(s){if(typeof s!=="string"||!/^[-]?\d+(\/[1-9]\d*)?$/.test(s))
 throw Error("exact fraction required");const p=s.split("/");return rat(p[0],p[1]??"1");}
function dec(s){
 if(typeof s!=="string")throw Error("decimal string required");
 const m=s.trim().match(/^([+-]?)(\d+)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/);
 if(!m)throw Error("bad exact decimal "+s);
 const sign=m[1]==="-"?-1n:1n, frac=m[3]??"";
 const n=sign*BigInt(m[2]+frac), exponent=BigInt(m[4]??"0")-BigInt(frac.length);
 return exponent>=0n?rat(n*10n**exponent):rat(n,10n**(-exponent));
}
function upperBall(obj){
 const s=(typeof obj==="string"?obj:obj?.ball??obj?.upper)?.trim();
 if(!s)throw Error("missing ball");
 const m=s.match(/^\[\s*(.*?)\s+\+\/-\s+(.*?)\s*\]$/);
 return m?add(dec(m[1]),dec(m[2])):dec(s);
}
function record(a){
 if(a[0]<0n)return {exact:str(a)};
 const scale=10n**30n, n=a[0]*scale/a[1], rem=a[0]*scale%a[1];
 const fmt=t=>{const s=String(t).padStart(31,"0");return s.slice(0,-30)+"."+s.slice(-30);};
 return {exact:str(a),lower_decimal:fmt(n),upper_decimal:fmt(n+(rem?1n:0n))};
}
export function computeFinalKAMBudget(texts,sha256,sourceSha256){
 const inputs=INPUTS.map(([key,path,digest])=>{
  if(typeof texts[key]!=="string"||sha256(texts[key])!==digest)
   throw Error("missing or changed UTF8 input "+path);
  return {key,path,sha256:digest};
 });
 if(!/^[0-9a-f]{64}$/.test(sourceSha256??""))throw Error("source SHA required");
 const k=JSON.parse(texts.kam),p=JSON.parse(texts.pre),s=JSON.parse(texts.sobolev);
 const r=JSON.parse(texts.ray),q=JSON.parse(texts.reference);
 const gates=[];
 const gate=(name,ok)=>{if(!ok)throw Error(name);gates.push({name,passed:true});};
 const less=(name,a,b)=>gate(name,lt(a,b));
 const equal=(name,a,b)=>gate(name,eq(a,b));
 const zero=rat(0n),one=rat(1n),two=rat(2n),four=rat(4n);
 gate("true R101 arithmetic and all three actual R31 gates",
  k.complete_arithmetic===true&&k.all_actual_arithmetic_R31_gates_passed===true&&
  k.R31.arithmetic_gates_passed===true&&Object.values(k.R31.gates).every(x=>x===true));
 gate("R101 scalar and continuous-domain inputs",k.all_scalar_and_domain_gates_passed===true);
 gate("finite exact preNewton complete without rewriting its old R31 failure",
  p.complete===true&&p.actual_R31_accepted===false);
 gate("R116 all 37 actual coordinate gates",s.complete===true&&s.passed_gates===37&&
  s.gates.every(x=>x.passed===true));
 gate("same complete full-parameter ray",r.complete===true&&
  r.proved_region.segments===550&&r.gates.every(x=>x.passed===true));
 gate("same complete finite reference and both seam checks",q.complete===true&&
  q.all_550_segments_passed===true&&q.all_549_base_seams_bitwise_checked===true&&
  q.all_549_Q_seams_bitwise_checked===true);
 const descriptor="097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052";
 const Hsha="0439d88f10f46d367e44a984db661ac3806a7bd052f46eca14e71594fa8eb2c2";
 const center="-7789843107295549/4611686018427387904",eta=rat(1n,1000000000n);
 gate("same original H and exact J composition",
  k.identity.original_H_sha256===Hsha&&p.identity.original_H_sha256===Hsha&&
  k.identity.exact_new_conjugacy==="H_new(x)=H_old(x+w(x))"&&
  p.identity.exact_new_conjugacy==="H_new(x)=H_old(x+w(x))");
 gate("same original normalized H5 reference descriptor",
  k.identity.retarget_descriptor_sha256===descriptor&&
  p.identity.retarget_descriptor_sha256===descriptor&&
  q.identity.retarget_descriptor_sha256===descriptor&&
  r.provenance.reference_descriptor_sha256===descriptor);
 gate("same real parameter and actual affine object",
  k.identity.old_exact_parameter===center&&r.proved_region.parameter_center===center&&
  s.parameter.parameter_center===center&&
  r.provenance.actual_object_sha256===s.actual_object_sha256);
 equal("whole true-ray parameter radius one billionth",
  parse(r.proved_region.parameter_half_width),eta);
 const mu=parse(k.identity.exact_parameter_increment);
 equal("same exact finite parameter increment",mu,parse(p.exact_dyadic_parameter_increment));
 const parameterMove=add(rat(abs(mu[0]),mu[1]),parse(k.R31.parameter_movement.exact_fraction));
 less("actual final parameter stays in the entire paid ray box",parameterMove,eta);
 const sf=parse(k.R31.final_analytic_width.exact_fraction);
 equal("actual final width, not an assumed derivative estimate",sf,rat(1n,2048n));
 const phi0=rat(1102524382n,100000000000000000n);
 const phi1=rat(3284319905n,100000000000000n);
 less("true KAM displacement outward bound",parse(k.R31.conjugacy_movement.exact_fraction),phi0);
 less("true KAM derivative outward bound",parse(k.R31.conjugacy_derivative_movement.exact_fraction),phi1);
 const w0=rat(9n,1000000000000n),w1=rat(3n,2500000000n),w2=rat(381n,1000000000n);
 equal("finite J paid outer width",parse(p.width),rat(5n,2048n));
 less("complete finite w norm",upperBall(p.w_norm),w0);
 less("complete finite w first derivative",upperBall(p.w_derivative_norms[0]),w1);
 less("complete finite w second derivative",upperBall(p.w_derivative_norms[1]),w2);
 let es=zero,fact=1n;for(let j=0n;j<=5n;j++){if(j>0n)fact*=j;es=add(es,rat(1n,fact));}
 equal("positive exponential series through degree five",es,rat(163n,60n));
 const phi2=div(phi1,mul(es,sf));
 const chi0=add(phi0,w0);
 const m=mul(sub(one,w1),sub(one,phi1));
 const M=mul(add(one,w1),add(one,phi1));
 const L=add(mul(w2,pow(add(one,phi1),2)),mul(add(one,w1),phi2));
 less("complete Phi image fits the already paid J strip",add(sf,phi0),parse(p.width));
 less("complete final-to-original label image fits true-ray strip",
  add(sf,chi0),parse(r.proved_region.label_strip));
 less("strict positive complete chi derivative",zero,m);
 less("chi lower derivative below one",m,one);
 less("chi upper derivative above one",one,M);
 less("complete chi second derivative below 0.024760",L,rat(619n,25000n));
 const invStrip=rat(1n,4096n),invRadius=mul(two,chi0);
 less("optional analytic inverse closed ball inside final strip",add(invStrip,invRadius),sf);
 less("optional analytic inverse contraction from actual derivative",
  sub(M,one),rat(1n,2n));
 const K=rat(1000017n,1000000n);
 less("chi L2 forward and all Hs zero to one, squared",div(one,m),pow(K,2));
 less("chi L2 inverse and all Hs zero to one, squared",M,pow(K,2));
 const scales=[];
 for(const kk of [1n,4n]){
  const kr=rat(kk),fee=div(pow(kr,2),add(one,pow(kr,2)));
  // Each endpoint H2 bound covers the complete three-term H2 norm.
  const H2f=add(mul(M,K),mul(mul(fee,L),K));
  const H2i=add(div(K,m),mul(mul(fee,div(L,pow(m,3))),K));
  const K54=kk===1n?rat(251n,250n):rat(503n,500n);
  less("chi kappa "+kk+" complete forward H5/4 fourth power",
   mul(pow(K,3),H2f),pow(K54,4));
  less("chi kappa "+kk+" complete inverse H5/4 fourth power",
   mul(pow(K,3),H2i),pow(K54,4));
  const old=s.strong_height.find(x=>x.kappa===String(kk));
  if(!old)throw Error("missing old scale");
  scales.push({kappa:String(kk),chi_H2_forward:record(H2f),chi_H2_inverse:record(H2i),
   chi_H5over4_both:record(K54),
   actual_all_time_height_H5over4_forward:record(mul(K54,parse(old.forward_H5over4))),
   actual_all_time_height_H5over4_inverse:record(mul(K54,parse(old.inverse_H5over4)))});
 }
 const fullTwoLegRatio=mul(parse(s.relative_derivative_ratio),div(M,m));
 less("all two-leg relative frames keep the rounded 6.202 bound, squared",
  fullTwoLegRatio,pow(rat(3101n,500n),2));
 const allHalf={
  height_forward:mul(K,parse(s.one_leg.height_Hhalf_forward)),
  height_inverse:mul(K,parse(s.one_leg.height_Hhalf_inverse)),
  density_forward:mul(K,parse(s.one_leg.density_Hminus_half_forward)),
  density_inverse:mul(K,parse(s.one_leg.density_Hminus_half_inverse))
 };
 // Sharper final root chart: reference start is exactly H5/4.
 equal("whole reference bound used at exact initial time",
  parse(q.verified_simple_constants.modulus_upper),rat(21n,20n));
 equal("whole finite reference contains final analytic width",
  parse(q.verified_simple_constants.label_strip),rat(1n,512n));
 const Hprime=mul(four,parse(q.verified_simple_constants.modulus_upper));
 const Rnew=rat(429n,125n),Bnew=rat(1792n,125n);
 less("paid actual Hnew inverse derivative",upperBall(p.exact_new_conjugacy_derivative_inverse),Rnew);
 less("paid actual Hnew second derivative",upperBall(p.exact_new_conjugacy_second_derivative),Bnew);
 const HnewPrime=mul(Hprime,add(one,w1));
 const rm=div(sub(one,phi1),Rnew);
 const rM=mul(HnewPrime,add(one,phi1));
 const rL=add(mul(Bnew,pow(add(one,phi1),2)),mul(HnewPrime,phi2));
 less("actual final-root lower derivative positive",zero,rm);
 less("actual final-root mM exceeds one",one,mul(rm,rM));
 const rhf=rat(39n,20n),rhi=rat(41n,20n),ra=rat(1853n,1000n),rb=rhi;
 less("root inverse square-root lower-derivative budget",div(one,rm),pow(ra,2));
 less("root square-root upper-derivative budget",rM,pow(rb,2));
 less("root complete forward Hhalf fourth power",div(rM,rm),pow(rhf,4));
 less("root complete inverse Hhalf squared",rM,pow(rhi,2));
 const rootScales=[];
 for(const kk of [1n,4n]){
  const kr=rat(kk),fee=div(pow(kr,2),add(one,pow(kr,2)));
  const H2f=add(mul(rM,rb),mul(mul(fee,rL),ra));
  const H2i=add(div(ra,rm),mul(mul(fee,div(rL,pow(rm,3))),rb));
  const uf=kk===1n?rat(22n):rat(34n),ui=kk===1n?rat(605n):rat(1133n);
  less("root kappa "+kk+" complete H2 forward",H2f,uf);
  less("root kappa "+kk+" complete H2 inverse",H2i,ui);
  const h54f=kk===1n?rat(93n,25n):rat(207n,50n);
  const h54i=kk===1n?rat(17n,2n):rat(199n,20n);
  less("root kappa "+kk+" H5/4 forward fourth power",mul(pow(rb,3),uf),pow(h54f,4));
  less("root kappa "+kk+" H5/4 inverse fourth power",mul(pow(rb,3),ui),pow(h54i,4));
  rootScales.push({kappa:String(kk),height_H2_forward:record(uf),height_H2_inverse:record(ui),
   height_H5over4_forward:record(h54f),height_H5over4_inverse:record(h54i)});
 }
 // Explicit mixed physical-kappa4 / final-label-kappa1 contracts.
 const mixedPort=mul(two,allHalf.height_inverse),mixedRootPort=mul(two,rhi);
 less("mixed natural-scale full all-time symplectic port below 4.983",mixedPort,rat(4983n,1000n));
 less("mixed all-time strong inverse below 563, squared",
  mul(two,pow(mul(four,parse(scales[0].actual_all_time_height_H5over4_inverse.exact)),2)),pow(rat(563n),2));
 less("mixed final-root strong inverse below 49, squared",
  mul(two,pow(mul(four,parse(rootScales[0].height_H5over4_inverse.exact)),2)),pow(rat(49n),2));
 return {
  kind:"R116_actual_final_KAM_coordinates_complete_Sobolev_budget",
  complete:true,arithmetic:"exact reduced BigInt rational comparisons; no sampled norm or native rerun",
  identity:{exact_parameter_center:center,parameter_half_width:str(eta),
   final_parameter_distance_bound:record(parameterMove),original_H_sha256:Hsha,
   original_reference_descriptor_sha256:descriptor,
   final_conjugacy:"H_infinity = H o J o Phi",
   original_to_final_label_map:"chi = J o Phi",
   full_time_self_circle_map:"psi_infinity(tau,z) = 4 Theta(tau,chi(z),p_infinity)",
   actual_object_sha256:s.actual_object_sha256},
  actual_KAM_data:{final_width:str(sf),phi_norm:record(phi0),phi_first_norm:record(phi1),
   finite_w_norm:record(w0),finite_w_first:record(w1),finite_w_second:record(w2),
   exp_one_strict_lower:str(es),derived_real_phi_second:record(phi2)},
  chi:{displacement_at_final_width:record(chi0),real_derivative_lower:record(m),
   real_derivative_upper:record(M),real_second_derivative:record(L),
   analytic_inverse_width:str(invStrip),analytic_inverse_displacement:record(invRadius),
   full_height_Hs_and_density_Hminus_s_both_for_0_le_s_le_1:record(K),
   strong_height:scales},
  all_time_final_frame:{
   common_kappa_height_Hhalf_forward:record(allHalf.height_forward),
   common_kappa_height_Hhalf_inverse:record(allHalf.height_inverse),
   common_kappa_density_Hminus_half_forward:record(allHalf.density_forward),
   common_kappa_density_Hminus_half_inverse:record(allHalf.density_inverse),
   relative_same_leg_frame_unchanged:s.relative,
   relative_all_two_leg_frames:{complete_derivative_ratio:record(fullTwoLegRatio),
    full_height_Hs_and_density_Hminus_s_both_for_0_le_s_le_1:record(rat(3101n,500n)),
    reason:"same-leg chi cancels; different legs use their complete derivative ratio, not an uncharged cancellation"},
   physical_kappa4_to_label_kappa1_height_Hhalf:record(allHalf.height_forward),
   label_kappa1_to_physical_kappa4_height_Hhalf:record(mixedPort),
   physical_kappa4_to_label_kappa1_density_Hminus_half:record(mixedPort),
   label_kappa1_to_physical_kappa4_density_Hminus_half:record(allHalf.density_inverse),
   natural_scale_port_both_directions_upper:record(rat(4983n,1000n)),
   natural_scale_height_H5over4_forward:scales[0].actual_all_time_height_H5over4_forward,
   natural_scale_height_H5over4_inverse_upper:record(rat(563n))},
  sharper_final_root_frame:{
   real_derivative_lower:record(rm),real_derivative_upper:record(rM),real_second_derivative:record(rL),
   common_kappa_height_Hhalf_forward:record(rhf),common_kappa_height_Hhalf_inverse:record(rhi),
   common_kappa_density_Hminus_half_forward:record(rhi),common_kappa_density_Hminus_half_inverse:record(rhf),
   strong_height:rootScales,natural_scale_port_both_directions:record(mixedRootPort),
   natural_scale_height_H5over4_forward:rootScales[0].height_H5over4_forward,
   natural_scale_height_H5over4_inverse:record(rat(49n))},
  conventions:{full_mean:"retained; height constants preserved, density integral preserved, no simultaneous mean/high projection",
   physical_frequency:"4k; normalization y=4 theta and density 4 Theta_z",
   zero_mode_weight:"one in every Bessel H^s_kappa norm",
   regular_scalars:"extend by identity; no zero-mean quotient",
   scope:"real Sobolev coordinate maps; same true parameter p_infinity inside paid eta box",
   exact_half_conjugacy:"R77 natural lifts and R101 irrational full conjugacy imply H_infinity^-1 P H_infinity = T_d_star",
   full_two_leg_scope:"second leg is the same forward chart at reflected radius and final label z+d_star; no new composition norm or complex-strip loss",
   full_PDE_propagator:false,full_PDE_inverse:false,density_positive_half_not_claimed:true,
   no_missing_nine_field_report_consumed:true},
  gates,passed_gates:gates.length,
  provenance:{inputs,source_sha256:sourceSha256,
   source:"scripts/fourfold_final_KAM_Sobolev_budget_exact.mjs",
   proof:"results/R116-final-KAM-coordinate-Sobolev-bridge.md",
   execution:"Identical pure BigInt kernel actually executed in functions V8; native CLI not run."}
 };
}

// NATIVE_CLI: file I/O replay wrapper only.
import {readFile,writeFile} from "node:fs/promises";
import {resolve} from "node:path";
import {fileURLToPath} from "node:url";
import {createHash} from "node:crypto";
if(process.argv[1]&&resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 const root=resolve(process.argv[2]??"."),out=process.argv[3]??"/tmp/R116-final-KAM-Sobolev.json";
 const texts={};for(const [key,path] of INPUTS)texts[key]=await readFile(resolve(root,path),"utf8");
 const hash=s=>createHash("sha256").update(s,"utf8").digest("hex");
 const src=await readFile(fileURLToPath(import.meta.url),"utf8");
 const report=computeFinalKAMBudget(texts,hash,hash(src));
 await writeFile(out,JSON.stringify(report,null,2)+"\n","utf8");
 process.stdout.write(JSON.stringify({complete:report.complete,gates:report.passed_gates,output:out})+"\n");
}
