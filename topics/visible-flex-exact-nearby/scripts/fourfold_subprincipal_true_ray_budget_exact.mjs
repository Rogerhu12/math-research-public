#!/usr/bin/env node
// R106: complete true forward-ray tube, exact rational finite certificate.
// Reproduce from the topic directory:
// node scripts/fourfold_subprincipal_true_ray_budget_exact.mjs . /tmp/R106-ray.json
// All displayed Arb radii are added outward before rational comparisons.
// Approximate numbers below are diagnostic only.
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { pathToFileURL, fileURLToPath } from "node:url";

export const INPUTS = [
  {
    "key": "flow",
    "path": "notes/2026-11-12-complete-flow-43301401638-arithmetic-summary.json",
    "sha256": "f25a3692b36390b3ae8dd7699d4e0ec0c2e74561ac238b11352f1d532a8bfc52"
  },
  {
    "key": "q",
    "path": "notes/2026-11-12-step5-forward-reference-derivative-complete-summary.json",
    "sha256": "d1dd69ac94f5912c828a6e22856badcb69bf324fdc7fc9a43f05493161363dc9"
  },
  {
    "key": "parameter",
    "path": "data/phase_ring_continuation/type_fixed_step02_d5_step5_fixed_tau_parameter_source_certificate.json",
    "sha256": "08b6fb2f3be32b7d2657d756e547134dcb55a54bb67a89d5f44a7fcd2f9f6e76"
  }
];

class Rat {
 constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}let a=n<0n?-n:n,b=d;while(b){const r=a%b;a=b;b=r;}this.n=n/a;this.d=d/a;}
 static p(v){if(v instanceof Rat)return v;if(typeof v==="bigint")return new Rat(v);let s=String(v).trim();if(s.includes("/")){const [a,b]=s.split("/");return Rat.p(a).div(Rat.p(b));}let sign=1n;if(s[0]==="-"){sign=-1n;s=s.slice(1);}else if(s[0]==="+")s=s.slice(1);const parts=s.toLowerCase().split("e"),e=parts.length===2?Number(parts[1]):0;const dec=parts[0].split("."),frac=dec[1]||"";const n=sign*BigInt((dec[0]||"0")+frac);const power=e-frac.length;return power>=0?new Rat(n*10n**BigInt(power)):new Rat(n,10n**BigInt(-power));}
 add(v){v=Rat.p(v);return new Rat(this.n*v.d+v.n*this.d,this.d*v.d);}
 sub(v){v=Rat.p(v);return new Rat(this.n*v.d-v.n*this.d,this.d*v.d);}
 mul(v){v=Rat.p(v);return new Rat(this.n*v.n,this.d*v.d);}
 div(v){v=Rat.p(v);return new Rat(this.n*v.d,this.d*v.n);}
 pow(n){return new Rat(this.n**BigInt(n),this.d**BigInt(n));}
 lt(v){v=Rat.p(v);return this.n*v.d<v.n*this.d;}
 le(v){v=Rat.p(v);return this.n*v.d<=v.n*this.d;}
 str(){return this.d===1n?String(this.n):`${this.n}/${this.d}`;}
 approx(){return Number(this.n)/Number(this.d);}
}

function ballUpper(v){let s=typeof v==="object"?(v.upper||v.ball):String(v);s=s.trim();if(s[0]==="["){const m=s.match(/^\[\s*([+\-0-9.eE]+)\s*\+\/-\s*([+\-0-9.eE]+)\s*\]$/);if(!m)throw Error("unrecognized display ball: "+s);return Rat.p(m[1]).add(m[2]);}return Rat.p(s);}

export function computeRayBudget(input){
 const {flow,q,parameter}=input;const gates=[];function check(name,value){gates.push({name,passed:!!value});if(!value)throw Error(name);}
 check("full original output verification",flow.complete&&flow.all_original_output_bytes_verified);
 check("all 550 true center spans",flow.g0.completed_segments===550&&flow.g0.leaves===555&&flow.g0.summary.R72_smallness_passed===true);
 check("all 550 finite reference spans and seams",q.complete&&q.segment_count===550&&q.all_550_segments_passed&&q.all_549_base_seams_bitwise_checked&&q.all_549_Q_seams_bitwise_checked);
 check("same finite reference descriptor",flow.endpoint.descriptor_sha256===q.identity.retarget_descriptor_sha256&&q.identity.retarget_descriptor_sha256==="097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052");
 check("true physical parameter source",parameter.proved&&parameter.both_signs_and_negative_half_by_exact_reflection&&parameter.bounds.physical_field_parameter_first_upper.safe_strict_rational_bound==="20");
 check("same actual affine object",parameter.object_sha256==="91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848");
 const eta=Rat.p("1/1000000000"),p0=Rat.p(flow.endpoint.exact_delta_fraction),pl=Rat.p(parameter.exact_parameter_interval[0]),pr=Rat.p(parameter.exact_parameter_interval[1]);
 check("exact requested parameter box included",pl.le(p0.sub(eta))&&p0.add(eta).le(pr));
 check("exact saved center and complete center family",p0.str()==="-7789843107295549/4611686018427387904"&&flow.endpoint.complete_true_center_return===true&&flow.endpoint.complete_true_uniform_parameter_box===true&&Rat.p(flow.endpoint.exact_parameter_half_width).str()===eta.str());
 check("exact complete forward endpoints",q.exact_time_endpoints.length===2&&q.exact_time_endpoints[0].kind==="rational_multiple_of_pi"&&q.exact_time_endpoints[0].numerator===-1&&q.exact_time_endpoints[0].denominator===2&&q.exact_time_endpoints[1].kind==="rational_multiple_of_pi"&&q.exact_time_endpoints[1].numerator===1&&q.exact_time_endpoints[1].denominator===2&&flow.g0.exact_final_time.rational==="0"&&flow.g0.exact_final_time.pi_coefficient==="1/2");
 const S=Rat.p(q.verified_simple_constants.label_strip),m=Rat.p(q.verified_simple_constants.real_part_lower),M=Rat.p(q.verified_simple_constants.modulus_upper);
 check("exact proved reference constants",S.str()==="1/512"&&m.str()==="3/100"&&M.str()==="21/20");
 const thetaDomain=Rat.p(parameter.physical_theta_strip);
 check("whole reference image in physical parameter strip",M.mul(S).lt(thetaDomain));
 const piUpper=Rat.p("22/7"),fp=Rat.p("20"),B1=fp.mul(piUpper).div(m),A=ballUpper(flow.g0.summary.A),E=ballUpper(flow.g0.summary.E);
 check("the whole physical fp envelope is strict",ballUpper(parameter.bounds.physical_field_parameter_first_upper.upper).lt(fp));
 const centerOuter=Rat.p(flow.endpoint.widths.flow).add(ballUpper(flow.g0.summary.R));
 check("reference working strip below paid center field strip",S.lt(centerOuter)&&centerOuter.str()==="1/256");
 const ABox=A.add(eta.mul(B1)),safeA=Rat.p("107/50000000"),SX=Rat.p("15/8192"),s=Rat.p("1/1024"),gap=SX.sub(s),R=S.sub(SX);
 check("uniform parameter displacement bound",ABox.lt(safeA));
 check("closed all-time Picard margin",ABox.mul(2).lt(R));
 const delta1=safeA.div(gap),delta2=safeA.mul(2).div(gap.pow(2)),imageLabel=s.add(safeA),imagePhysical=M.mul(imageLabel);
 check("true coordinate image in reference strip",imageLabel.lt(S));
 const Jmax=M.mul(Rat.p(1).add(delta1)),Jmin=m.sub(M.mul(delta1));
 const Yxx=M.div(S.sub(imageLabel));
 const thetaXX=Yxx.mul(Rat.p(1).add(delta1).pow(2)).add(M.mul(delta2));
 const closeTheta=M.mul(safeA),closeJ=Yxx.mul(safeA).add(M.mul(delta1));
 check("coordinate first derivative error below .00251",delta1.lt("251/100000"));
 check("coordinate second derivative below 6",delta2.lt(6));
 check("true phase Jacobian modulus below 1.06",Jmax.lt("53/50"));
 check("true phase Jacobian real part above .027",Rat.p("27/1000").lt(Jmin));
 check("true physical image below 1/900",imagePhysical.lt("1/900"));
 check("physical second label derivative below 1100",thetaXX.lt(1100));
 check("true angle-reference difference below 2.25e-6",closeTheta.lt("9/4000000"));
 check("true Jacobian-reference difference below .005",closeJ.lt("1/200"));
 const record=x=>({exact:x.str(),approximate:x.approx()});
 return {kind:"R106_all_time_true_ray_from_paid_reference_and_parameter_source",
 complete:true,arithmetic:"exact reduced BigInt rational inequalities; display radii added outward",
 proved_region:{leg:"forward",segments:550,time_endpoints:["-pi/2","pi/2"],parameter_center:p0.str(),parameter_half_width:eta.str(),label_strip:s.str(),label_period:"2*pi",physical_angle:"theta; reference Y(x+2*pi)=Y(x)+pi/2"},
 source_convention:"R80 f_p is physical-theta fixed-tau derivative, r=t(p)sin(tau); g_p=f_p(Y)/Y_x per physical tau, no extra factor 4",
 bounds:{center_true_integrated_defect:record(A),center_source_error_for_identity_only:record(E),uniform_first_parameter_integral:record(B1),uniform_true_integrated_defect:record(ABox),uniform_displacement_safe:record(safeA),coordinate_outer_strip:record(SX),coordinate_first_derivative_error:record(delta1),coordinate_second_derivative:record(delta2),true_label_J_real_lower:record(Jmin),true_label_J_modulus:record(Jmax),physical_image_strip:record(imagePhysical),true_second_label_derivative:record(thetaXX),true_angle_minus_reference:record(closeTheta),true_J_minus_reference_q:record(closeJ)},
 gates,not_proved:["complete nonmean subprincipal phase","finite part root integral","full PDE inverse","second leg obtained without its actual composition"]};
}

function utf8ByteLength(s) {
  let n=0;
  for (const c of s) { const p=c.codePointAt(0); n += p<128?1:p<2048?2:p<65536?3:4; }
  return n;
}

export function checkedReport(raw, sourceSha256, sha256) {
  const parsed = {};
  const checked = [];
  for (const item of INPUTS) {
    if (typeof raw[item.key] !== "string") throw Error("missing " + item.path);
    const actual = sha256(raw[item.key]);
    if (actual !== item.sha256) throw Error("SHA256 mismatch: " + item.path);
    parsed[item.key] = JSON.parse(raw[item.key]);
    checked.push({...item, bytes_utf8: utf8ByteLength(raw[item.key])});
  }
  const report = computeRayBudget(parsed);
  report.provenance = {
    source: "scripts/fourfold_subprincipal_true_ray_budget_exact.mjs",
    source_sha256: sourceSha256,
    inputs: checked,
    reference_proof: {
      path: "notes/2026-11-12-step5-forward-reference-derivative-complete.md",
      sha256: "fe8e80dbcd97c912456908c213fa8ddec779103e9b1e3b490d573a650b483894"
    },
    proof: "results/R106-supplement-actual-all-time-ray-tube.md",
    center_g0_index_sha256: parsed.flow.g0.sha256,
    reference_descriptor_sha256: parsed.q.identity.retarget_descriptor_sha256,
    actual_object_sha256: parsed.parameter.object_sha256,
    execution: "The identical pure checkedReport/computeRayBudget implementation was evaluated with BigInt in V8; the Node CLI is a byte-verifying replay wrapper.",
    scope: "A new finite certificate combining three already completed continuous certificates. No density, ODE or interval leaf is recomputed or invented."
  };
  return report;
}

if (process.argv[1] && pathToFileURL(path.resolve(process.argv[1])).href === import.meta.url) {
  if (process.argv.length !== 4) throw Error("usage: node SCRIPT TOPIC_DIRECTORY OUTPUT.json");
  const topic = path.resolve(process.argv[2]);
  const output = path.resolve(process.argv[3]);
  const raw = Object.fromEntries(INPUTS.map(x => [x.key,fs.readFileSync(path.join(topic,x.path),"utf8")]));
  const sha256 = s => crypto.createHash("sha256").update(s,"utf8").digest("hex");
  const sourceSha256 = sha256(fs.readFileSync(fileURLToPath(import.meta.url),"utf8"));
  const report = checkedReport(raw, sourceSha256, sha256);
  fs.mkdirSync(path.dirname(output), {recursive:true});
  fs.writeFileSync(output, JSON.stringify(report,null,2)+"\n");
  process.stdout.write(JSON.stringify({complete:report.complete,gates:report.gates.length,source_sha256:sourceSha256,output})+"\n");
}
