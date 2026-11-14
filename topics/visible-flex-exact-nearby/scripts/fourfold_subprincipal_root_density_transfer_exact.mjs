#!/usr/bin/env node
// Complete same-family nonmean root-density migration. Exact BigInt arithmetic.
// Run from the topic: node scripts/fourfold_subprincipal_root_density_transfer_exact.mjs . OUTPUT.json
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL,fileURLToPath} from 'node:url';
export const INPUTS=[
  {
    "key": "old",
    "path": "notes/2026-11-12-beta-exact-affine-step3-collar.json",
    "sha256": "037cd700677da4a34b423de431e9b22ab9903b5cd844a6a9348e6ccd0ee8918d",
    "json": true
  },
  {
    "key": "derivative",
    "path": "notes/2026-11-12-beta-step3-true-derivative-collar-h1e5-domain500.json",
    "sha256": "b387ede87055d0a990cafca12002b8baead5a2415d2d4cef610dde99405efd08",
    "json": true
  },
  {
    "key": "root",
    "path": "notes/2026-11-12-beta-step3-parameter-root-derivative-h1e5.json",
    "sha256": "3284dfe4d3feaa5eeca5f114844c1052b381434fa1bb0c08def1c45d9b845243",
    "json": true
  },
  {
    "key": "ray",
    "path": "notes/2026-11-12-R106-actual-all-time-ray-tube.json",
    "sha256": "6463e62641b9187045016c63ee633816676a75baf941ea01375a6ae36f1a1863",
    "json": true
  },
  {
    "key": "old_kernel",
    "path": "scripts/fourfold_phase_beta_interval.py",
    "sha256": "ff159224bc1870b7580ef6e5f0370a4fcc385ed556d947003a0bb1667e6f4b0f"
  },
  {
    "key": "derivative_kernel",
    "path": "scripts/fourfold_phase_beta_derivative_collar.py",
    "sha256": "0e24abf168309f7f98cb027cf6a30d85026149ae91532d5cbf8e30920957e5a5"
  },
  {
    "key": "derivative_finish",
    "path": "scripts/fourfold_phase_beta_derivative_collar_finish.py",
    "sha256": "273b5e48262d9f4046d4a55f62017e615d57beddbcf9eb27420575602d8135cb"
  },
  {
    "key": "root_kernel",
    "path": "scripts/fourfold_phase_beta_parameter_derivative.py",
    "sha256": "608c541c1469bb45f5ec556751998fc3901f8623f6cca0e7eb77062d5821ce96"
  }
];

class Rat {
 constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}let a=n<0n?-n:n,b=d;while(b){let q=a%b;a=b;b=q;}this.n=n/a;this.d=d/a;}
 static p(v){if(v instanceof Rat)return v;let s=String(v).trim();if(s.includes("/")){let [a,b]=s.split("/");return Rat.p(a).div(Rat.p(b));}let m=s.match(/^([+-]?)(\d*)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/);if(!m||!(m[2]||m[3]))throw Error("bad rational "+s);let n=BigInt((m[2]||"0")+(m[3]||""));if(m[1]==="-")n=-n;let p=Number(m[4]||0)-(m[3]||"").length;return p>=0?new Rat(n*10n**BigInt(p)):new Rat(n,10n**BigInt(-p));}
 add(v){v=Rat.p(v);return new Rat(this.n*v.d+v.n*this.d,this.d*v.d);}
 sub(v){v=Rat.p(v);return new Rat(this.n*v.d-v.n*this.d,this.d*v.d);}
 mul(v){v=Rat.p(v);return new Rat(this.n*v.n,this.d*v.d);}
 div(v){v=Rat.p(v);return new Rat(this.n*v.d,this.d*v.n);}
 abs(){return new Rat(this.n<0n?-this.n:this.n,this.d);}
 pow(k){return new Rat(this.n**BigInt(k),this.d**BigInt(k));}
 lt(v){v=Rat.p(v);return this.n*v.d<v.n*this.d;}
 le(v){v=Rat.p(v);return this.n*v.d<=v.n*this.d;}
 eq(v){v=Rat.p(v);return this.n*v.d===v.n*this.d;}
 str(){return this.d===1n?String(this.n):`${this.n}/${this.d}`;}
 decimalUpper(digits=22){if(this.n<0n)throw Error("positive display required");let scale=10n**BigInt(digits),z=(this.n*scale+this.d-1n)/this.d;return (z/scale).toString()+"."+(z%scale).toString().padStart(digits,"0");}
}

function endpoint(v,sign=1){let s=typeof v==="object"?(sign>0?v.upper:v.lower)||v.ball:String(v);s=s.trim();if(s.startsWith("[")){const m=s.match(/^\[\s*([+\-0-9.eE]+)\s*\+\/-\s*([+\-0-9.eE]+)\s*\]$/);if(!m)throw Error("unrecognized ball "+s);const r=Rat.p(m[2]);if(r.lt(0))throw Error("negative radius");return sign>0?Rat.p(m[1]).add(r):Rat.p(m[1]).sub(r);}return Rat.p(s);}

export function rootDensityTransfer(parsed){
 const {old,derivative,root,ray}=parsed, gates=[];
 function check(name,ok){gates.push({name,passed:!!ok});if(!ok)throw Error(name);}
 const origin="0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b",direction="8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab";
 check("old nonmean complex collar completed",old.complete===true);
 check("whole fixed-r derivative complex collar completed",derivative.complete===true);
 check("whole true root derivative proved",root.proved===true);
 check("complete true forward ray certificate",ray.complete===true&&ray.proved_region.segments===550);
 check("same exact affine origin",old.origin_inputs_sha256===origin&&derivative.origin_inputs_sha256===origin&&root.origin_inputs_sha256===origin);
 check("same exact affine direction",old.direction_sha256===direction&&derivative.direction_sha256===direction&&root.direction_sha256===direction);
 const p3=Rat.p(old.exact_delta_fraction),p5=Rat.p(ray.proved_region.parameter_center),eta=Rat.p(ray.proved_region.parameter_half_width),wide=Rat.p(derivative.exact_parameter_half_width);
 check("saved exact delta3 center",p3.eq("-7832869216826619/4611686018427387904"));
 check("saved exact delta5 center",p5.eq("-7789843107295549/4611686018427387904"));
 check("same derivative parameter centers",p3.eq(derivative.exact_center_parameter)&&p3.eq(root.exact_center_parameter));
 check("whole Delta5 half width",wide.eq("1/100000")&&wide.eq(root.exact_parameter_half_width));
 check("requested whole eta half width",eta.eq("1/1000000000"));
 const eps=p5.sub(p3).abs().add(eta);
 check("entire current parameter tube in Delta5",eps.lt(wide));
 for(const [name,x] of [["density derivative",derivative],["root derivative",root]])check(name+" exact family endpoints",Rat.p(x.exact_parameter_interval[0]).eq(p3.sub(wide))&&Rat.p(x.exact_parameter_interval[1]).eq(p3.add(wide)));
 check("same original object for old collar and derivatives",old.object_sha256===derivative.center_object_sha256&&old.object_sha256===root.center_object_sha256);
 check("derivative collar binds original collar",derivative.center_collar_sha256==="037cd700677da4a34b423de431e9b22ab9903b5cd844a6a9348e6ccd0ee8918d");
 check("derivative collar binds true root derivative",derivative.root_derivative_report_sha256==="3284dfe4d3feaa5eeca5f114844c1052b381434fa1bb0c08def1c45d9b845243");
 check("true kernel and finishing source identities",derivative.derivative_core_sha256==="608c541c1469bb45f5ec556751998fc3901f8623f6cca0e7eb77062d5821ce96"&&derivative.coefficient_kernel_sha256==="0e24abf168309f7f98cb027cf6a30d85026149ae91532d5cbf8e30920957e5a5"&&derivative.source_sha256==="273b5e48262d9f4046d4a55f62017e615d57beddbcf9eb27420575602d8135cb");
 check("same exact physical cut",old.fixed_cut===derivative.fixed_cut);
 check("same exact common scalar germ",JSON.stringify(derivative.exact_common_span)===JSON.stringify(root.exact_common_span));
 const tlo=endpoint(derivative.root,-1),thi=endpoint(derivative.root),cut=Rat.p(old.fixed_cut),[left,right]=derivative.exact_common_span.map(Rat.p);
 check("whole positive roots and fixed cut in same scalar span",left.lt(cut)&&cut.lt(tlo)&&thi.lt(right));
 const R=Rat.p("1/2500"),S=Rat.p("1/320"),oldR=endpoint(old.radial_radius,-1),newR=Rat.p(derivative.radial_radius);
 const oldS=endpoint(old.sigma,-1).div(4),newS=Rat.p(derivative.sigma).div(4);
 check("positive inner complex root disk",Rat.p(0).lt(R));
 check("entire old and new real collar in inner disk",thi.sub(cut).lt(R));
 check("common physical complex angle strip",S.le(newS)&&S.lt(oldS));
 const T=endpoint(root.root_parameter_derivative),tmin=endpoint(root.root_parameter_derivative,-1);
 check("positive true root derivative",Rat.p(0).lt(tmin)&&tmin.le(T));
 const delta=T.mul(eps),den=R.sub(delta);
 check("parameter line never crosses moving root on boundary",Rat.p(0).lt(den));
 check("shifted complex boundary inside old radial disk",R.add(delta).lt(oldR));
 check("whole parameter line inside derivative radial disk",R.add(delta).lt(newR));
 const minima=derivative.domain.positive_real_minima;
 for(const name of ["area2","radius2","support","a","Fz"])check("complete complex family positive "+name,Rat.p(0).lt(endpoint(minima[name],-1)));
 check("whole complex family has analytic deflated curvature branch",Rat.p(0).lt(endpoint(derivative.domain.deflated_curvature_real_lower,-1)));
 const MG=endpoint(old.domain.G_bound),MH=endpoint(derivative.domain.H_bound);
 check("old nonmean G modulus is positive",Rat.p(0).lt(MG));
 check("true fixed-r H modulus is positive",Rat.p(0).lt(MH));
 const dilation=R.div(den),migrated=dilation.pow(3).mul(MG.add(eps.mul(MH).div(den)));
 check("rational cubic majorizes five-halves dilation",Rat.p(1).le(dilation));
 check("whole current G bound below 9327/200000",migrated.lt("9327/200000"));
 const image=Rat.p(ray.bounds.physical_image_strip.exact),J=Rat.p(ray.bounds.true_label_J_modulus.exact),N=migrated.mul(J),gap=S.sub(image);
 check("true ray image lies inside paid physical strip",image.lt(S));
 check("true ray label remains original H5 label",ray.proved_region.label_strip==="1/1024"&&ray.proved_region.physical_angle==="theta; reference Y(x+2*pi)=Y(x)+pi/2");
 check("true J multiplier positive",Rat.p(0).lt(J));
 check("pulled regularized numerator below 491/10000",N.lt("491/10000"));
 const rec=x=>({exact_upper:x.str(),decimal_upper_22:x.decimalUpper()});
 const theta=[];let fac=Rat.p(1);for(let j=0;j<=4;j++){if(j)fac=fac.mul(j);theta.push({order:j,...rec(migrated.mul(fac).div(gap.pow(j)))});}
 return {kind:"R106_true_fixed_r_parameter_transfer_of_nonmean_root_density",complete:true,arithmetic:"exact BigInt rational bounds; all display radii retained",input_semantics:{density:"original-height reduced Dred of R50/R106, with full ell and zero-order terms retained",G:"rho^(5/2) Dred(t(p)-rho,theta,p), analytically root-deflated",H:"rho^(7/2) partial_p Dred(r,theta,p) at FIXED physical r; not fixed-rho derivative of G"},proved_region:{parameter_center:p5.str(),parameter_half_width:eta.str(),outer_parameter_center:p3.str(),outer_parameter_half_width:wide.str(),complex_root_radius:R.str(),physical_theta_strip:S.str(),real_fixed_cut:cut.str(),common_scalar_span:[left.str(),right.str()],label_strip:"1/1024",leg:"forward",second_leg_or_final_KAM_frame_not_transferred:true},bounds:{parameter_movement:rec(eps),root_parameter_derivative_upper:rec(T),root_movement:rec(delta),boundary_distance_from_any_root_lower:{exact_lower:den.str()},old_G_modulus:rec(MG),whole_fixed_r_H_modulus:rec(MH),dilation:rec(dilation),transferred_G_modulus:rec(migrated),safe_G_bound:"9327/200000",true_physical_image:{exact_upper:image.str()},true_J_modulus:{exact_upper:J.str()},pulled_regularized_numerator:rec(N),safe_pulled_numerator:"491/10000",G_physical_theta_derivatives_on_actual_ray_image:theta},gates,not_proved:["complete root finite-part integral along rays","complex-root-time continuation of true rays","grounded density without an explicit gauge conversion","complete nonmean first phase b","final KAM label multiplier norm","full PDE inverse"]};
}

export function checkedTransfer(raw,sourceSha256,sha256){
 const parsed={},verified=[];
 for(const spec of INPUTS){const text=raw[spec.key];if(typeof text!=="string")throw Error("missing "+spec.path);const h=sha256(text);if(h!==spec.sha256)throw Error("SHA mismatch: "+spec.path);if(spec.json)parsed[spec.key]=JSON.parse(text);verified.push({...spec,utf8_characters:text.length});}
 const out=rootDensityTransfer(parsed);
 out.provenance={source:"scripts/fourfold_subprincipal_root_density_transfer_exact.mjs",source_sha256:sourceSha256,proof:"results/R106-supplement-moving-root-density-transfer.md",inputs:verified,execution:"The identical pure checkedTransfer/rootDensityTransfer functions were actually executed with BigInt in V8 after reading all eight original UTF8 inputs. The Node CLI is a byte-checking replay wrapper.",recovery:"Reconstructed after executor/store loss, then actually rerun; 42 gates in this version. This is not a claim of byte identity with the unpublished earlier 41-gate version."};
 return out;
}

if (process.argv[1] && pathToFileURL(path.resolve(process.argv[1])).href===import.meta.url) {
 if(process.argv.length!==4)throw Error("usage: node SCRIPT TOPIC_DIRECTORY OUTPUT.json");
 const topic=path.resolve(process.argv[2]),output=path.resolve(process.argv[3]);
 const sha256=text=>crypto.createHash("sha256").update(text,"utf8").digest("hex");
 const raw=Object.fromEntries(INPUTS.map(x=>[x.key,fs.readFileSync(path.join(topic,x.path),"utf8")]));
 const report=checkedTransfer(raw,sha256(fs.readFileSync(fileURLToPath(import.meta.url),"utf8")),sha256);
 fs.mkdirSync(path.dirname(output),{recursive:true});
 fs.writeFileSync(output,JSON.stringify(report,null,2)+"\n");
 console.log(JSON.stringify({complete:report.complete,gates:report.gates.length,G:report.bounds.transferred_G_modulus.decimal_upper_22,N:report.bounds.pulled_regularized_numerator.decimal_upper_22,report_sha256:sha256(fs.readFileSync(output,"utf8"))}));
}
