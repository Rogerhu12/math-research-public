#!/usr/bin/env node
// Actual R106 root endpoint bounds from completed R99 and full true-ray inputs.
// Reproduce in the topic: node scripts/fourfold_subprincipal_root_endpoint_exact.mjs . /tmp/R106-root-endpoint.json
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath, pathToFileURL } from "node:url";
export const INPUTS=[
  {
    "key": "root",
    "path": "notes/2026-11-12-ci-actual-root-Cauchy-frame-Fourier-summary.json",
    "sha256": "8c13c40e1ea65eb05a97eaeb79cba1ab49f8ebe734ad598d0b382a0afe6890bf",
    "json": true
  },
  {
    "key": "ray",
    "path": "notes/2026-11-12-R106-actual-all-time-ray-tube.json",
    "sha256": "6463e62641b9187045016c63ee633816676a75baf941ea01375a6ae36f1a1863",
    "json": true
  },
  {
    "key": "root_proof",
    "path": "results/R99-actual-root-cauchy-frame-and-canonical-v1.md",
    "sha256": "df19c58b1359f215684871a66208408417f36870c99b0522eccf79d231f4a479",
    "json": false
  },
  {
    "key": "bulk_derivative",
    "path": "notes/2026-11-12-beta-derivative-independent-cover-and-transfer-audit.json",
    "sha256": "1047f423a77d07aa14093b17fcf28376243857d8bf738b5d62f65f0f3dea7923",
    "json": true
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
export function computeRootEndpoint(root,ray) {
 const checks=[];function check(name,v){checks.push({name,passed:!!v});if(!v)throw Error(name);}
 const record=v=>({exact_upper:v.str(),approximate_only:v.approx()});
 check("same completed true root family and ray",root.proved===true&&ray.complete===true&&root.identity.center_object_sha256===ray.provenance.actual_object_sha256&&root.identity.exact_center_parameter===ray.proved_region.parameter_center&&root.identity.exact_parameter_half_width===ray.proved_region.parameter_half_width);
 const S=Rat.p("1/256"),thetaImage=Rat.p(ray.bounds.physical_image_strip.exact),J=Rat.p(ray.bounds.true_label_J_modulus.exact),gap=S.sub(thetaImage);
 check("true ray image strictly inside root complex strip",thetaImage.lt(S));
 const mt=ballUpper(root.fields.t0.complex_modulus),mi=ballUpper(root.fields.inverse_t0.complex_modulus),my=ballUpper(root.fields.Y_prime.complex_modulus);
 const rawEndpoint=mt.mul(mi).div(gap.mul(2));
 const pulledEndpoint=rawEndpoint.mul(J);
 const c0=Rat.p("5/16").mul(my),pulledC0=c0.mul(J);
 const mtA1=ballUpper(root.fields.t0.Wiener["1"].norm).add(ballUpper(root.fields.t0.Wiener["1"].error));
 const miA0=ballUpper(root.fields.inverse_t0.Wiener["0"].norm).add(ballUpper(root.fields.inverse_t0.Wiener["0"].error));
 const physicalA0=mtA1.mul(miA0).div(2);
 check("root endpoint physical Wiener A0 below 1.146",physicalA0.lt("573/500"));
 check("root endpoint full pulled-label strip modulus below 226",pulledEndpoint.lt(226));
 check("leading root counterterm full label modulus below .098",pulledC0.lt("49/500"));
 return {kind:"R106_actual_root_endpoint_and_leading_counterterm_from_R99",complete:true,arithmetic:"exact BigInt rational upper endpoints, with all display radii added",
  same_parameter_interval:root.identity.exact_parameter_interval,physical_root_outer_strip:S.str(),label_strip:ray.proved_region.label_strip,
  bounds:{physical_root_endpoint_A0:record(physicalA0),root_endpoint_physical_image_modulus:record(rawEndpoint),true_label_root_endpoint_modulus:record(pulledEndpoint),physical_leading_counterterm_modulus:record(c0),true_label_leading_counterterm_modulus:record(pulledC0)},
  normalization:"endpoint = sigma*u_theta/8 = -sigma*t0_theta/(2*t0) in the physical root label; pull back as a one-form by multiplying the actual physical-angle label Jacobian",
  checks,not_proved:["h1/s1 counterterms","continuous root finite-part integral","complete nonmean phase or full PDE inverse"]};
}
function computeRealBulkTransfer(d,ray) {
 if(!d.complete || d.exact_spans!==167 || d.leaves!==265)throw Error("incomplete true fixed-r bulk derivative");
 const p3=Rat.p("-7832869216826619/4611686018427387904"),p5=Rat.p(ray.proved_region.parameter_center),eta=Rat.p(ray.proved_region.parameter_half_width);
 const epsilon=p5.sub(p3).add(eta),B=Rat.p(d.bulk_upper),fee=epsilon.mul(B);
 if(!epsilon.lt("1/100000")||!fee.lt("21/1000"))throw Error("actual real parameter transfer gate failed");
 return {exact_parameter_movement:epsilon.str(),true_fixed_r_real_bulk_Dp_integral:B.str(),real_transfer_fee:fee.str(),readable_fee:fee.approx(),safe_strict_real_fee:"21/1000",old_complex_strip_transferred:false,old_bulk_moduli_extracted:false,old_center_parameter:p3.str(),whole_derivative_parameter_half_width:"1/100000",gates:[{name:"current real box inside true fixed-r derivative family",passed:true},{name:"real density transfer integral fee below .021",passed:true}]};
}
export function checkedEndpoint(raw, sourceSha256, sha256) {
  const parsed={};
  for (const item of INPUTS) {
    if (sha256(raw[item.key])!==item.sha256) throw Error("input SHA256 mismatch: "+item.path);
    if(item.json) parsed[item.key]=JSON.parse(raw[item.key]);
  }
  const report=computeRootEndpoint(parsed.root,parsed.ray);
  report.separate_real_bulk_parameter_transfer=computeRealBulkTransfer(parsed.bulk_derivative,parsed.ray);
  report.provenance={
    source:"scripts/fourfold_subprincipal_root_endpoint_exact.mjs",
    source_sha256:sourceSha256,inputs:INPUTS,
    proof:"results/R106-supplement-existing-bulk-moduli-and-root-endpoint.md",
    root_full_report_sha256:parsed.root.report_sha256,
    root_complex_report_sha256:"b872d49b788f54c0ad8f854b16c1097d6a7ef04162b883b9d0b675ab57db7d05",
    execution:"The identical pure checkedEndpoint/computeRootEndpoint implementation was actually evaluated in V8 with BigInt. Native CLI not run.",
    scope:"Completed input arithmetic, not a new geometric or ray integration."
  };
  return report;
}
if(process.argv[1] && pathToFileURL(path.resolve(process.argv[1])).href===import.meta.url) {
 if(process.argv.length!==4) throw Error("usage: node SCRIPT TOPIC OUTPUT.json");
 const topic=path.resolve(process.argv[2]),out=path.resolve(process.argv[3]);
 const raw=Object.fromEntries(INPUTS.map(x=>[x.key,fs.readFileSync(path.join(topic,x.path),"utf8")]));
 const hash=s=>crypto.createHash("sha256").update(s,"utf8").digest("hex");
 const report=checkedEndpoint(raw,hash(fs.readFileSync(fileURLToPath(import.meta.url),"utf8")),hash);
 fs.mkdirSync(path.dirname(out),{recursive:true});fs.writeFileSync(out,JSON.stringify(report,null,2)+"\n");
 process.stdout.write(JSON.stringify({complete:report.complete,checks:report.checks.length,output:out})+"\n");
}
