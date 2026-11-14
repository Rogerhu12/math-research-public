#!/usr/bin/env node
import fs from 'node:fs';
import crypto from 'node:crypto';
import {pathToFileURL,fileURLToPath} from 'node:url';
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
function computeIntegratedRayBudget(old,integrated){
 const gates=[],gate=(name,ok)=>{gates.push({name,passed:!!ok});if(!ok)throw Error(name);};
 gate("old whole-time true ray certificate complete",old.complete&&old.proved_region.segments===550);
 gate("actual integrated source certificate complete",integrated.complete&&integrated.proved_integrated_actual_parameter_density_moduli);
 gate("same fixed finite reference",old.provenance.reference_descriptor_sha256===integrated.descriptor_sha256);
 gate("same actual center",old.proved_region.parameter_center===integrated.exact_center_parameter);
 const p=Rat.p(old.proved_region.parameter_center),eta=Rat.p(old.proved_region.parameter_half_width);
 const plo=Rat.p(integrated.exact_parameter_interval[0]),phi=Rat.p(integrated.exact_parameter_interval[1]);
 gate("exact whole eta-box included",plo.le(p.sub(eta))&&p.add(eta).le(phi));
 gate("source and reference strips match",integrated.label_strip==="1/512"&&integrated.reference_q_real_lower==="3/100"&&integrated.reference_q_modulus_upper==="21/20"&&integrated.actual_source_physical_strip==="1/56");
 gate("true complete ordinary and turn cover",integrated.ordinary_leaf_count===169&&integrated.ordinary_leaves.length===169&&!!integrated.turn);
 const B1=endpoint(integrated.true_integrated_reference_density_moduli.B1);
 const B2=endpoint(integrated.true_integrated_reference_density_moduli.B2);
 const A=Rat.p(old.bounds.center_true_integrated_defect.exact);
 const ABox=A.add(eta.mul(B1)),safeA=Rat.p("7/6250000");
 const S=Rat.p("1/512"),SX=Rat.p("15/8192"),s=Rat.p("1/1024");
 const m=Rat.p("3/100"),M=Rat.p("21/20"),gap=SX.sub(s);
 gate("exact integrated B1 improvement",B1.lt("1077.689852253")&&B1.lt(old.bounds.uniform_first_parameter_integral.exact));
 gate("exact integrated B2",B2.lt("9646.363329155"));
 gate("full physical source image",M.mul(S).eq(integrated.reference_physical_image_upper)&&M.mul(S).lt("1/56"));
 gate("uniform displacement bound",ABox.lt(safeA));
 gate("complete all-time Picard margin",ABox.mul(2).lt(S.sub(SX)));
 const delta1=safeA.div(gap),delta2=safeA.mul(2).div(gap.pow(2));
 const imageLabel=s.add(safeA),Jmax=M.mul(Rat.p(1).add(delta1)),Jmin=m.sub(M.mul(delta1));
 const Yxx=M.div(S.sub(imageLabel));
 const thetaXX=Yxx.mul(Rat.p(1).add(delta1).pow(2)).add(M.mul(delta2));
 const closeTheta=M.mul(safeA),closeJ=Yxx.mul(safeA).add(M.mul(delta1));
 const imagePhysical=M.mul(imageLabel);
 gate("actual coordinate image",imageLabel.lt(S));
 gate("true Jacobian remains positive",Rat.p("285/10000").lt(Jmin));
 gate("true phase Jacobian modulus below 1.052",Jmax.lt("263/250"));
 gate("true Jacobian-reference gap below .0026",closeJ.lt("13/5000"));
 gate("actual physical angle-reference gap below 1.18e-6",closeTheta.lt("59/50000000"));
 gate("actual physical strip below 1/900",imagePhysical.lt("1/900"));
 const rec=v=>({exact:v.str(),decimal_upper_28:v.decimalUpper(28)});
 return {kind:"R106_integrated_parameter_source_true_all_time_ray_refinement",
  complete:true,arithmetic:"exact reduced BigInt with all displayed radii added outward",
  proved_region:old.proved_region,source_convention:old.source_convention,
  bounds:{uniform_B1:rec(B1),uniform_B2:rec(B2),center_A:rec(A),
   uniform_A:rec(ABox),safe_displacement:rec(safeA),
   coordinate_outer_strip:rec(SX),coordinate_first_derivative_error:rec(delta1),
   coordinate_second_derivative:rec(delta2),true_label_J_real_lower:rec(Jmin),
   true_label_J_modulus:rec(Jmax),physical_image_strip:rec(imagePhysical),
   true_second_label_derivative:rec(thetaXX),true_angle_minus_reference:rec(closeTheta),
   true_J_minus_reference_q:rec(closeJ)},
  gates,
  limitations:["Only the complete actual moduli B1/B2 are consumed; no signed mean or phase coefficients are inferred.",
   "The finite reference Y is fixed throughout the real parameter interval; B1 is an integral for physical-time fixed-tau fp divided by Yx.",
   "No extra factor 4 is inserted. The normalized label is x and the actual angle is theta.",
   "This refines the already paid whole-time ray tube; it is not a nonmean phase integral, PDE inverse, or seven-field geometry computation."]};
}
export {computeIntegratedRayBudget};
const INPUTS=[
  {
    "key": "old",
    "path": "notes/2026-11-12-R106-actual-all-time-ray-tube.json",
    "sha256": "6463e62641b9187045016c63ee633816676a75baf941ea01375a6ae36f1a1863"
  },
  {
    "key": "integrated",
    "path": "notes/2026-11-12-step5-integrated-parameter-source-budget.json",
    "sha256": "1157bc1b8ad6f70b9fbd65aeaee6152da842e066d22b216cd2ca87620e5f5a41"
  }
];

if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 const data={};
 for(const item of INPUTS){
  const bytes=fs.readFileSync(item.path);
  if(crypto.createHash('sha256').update(bytes).digest('hex')!==item.sha256)
   throw Error('changed true scientific input '+item.path);
  data[item.key]=JSON.parse(bytes.toString('utf8'));
 }
 const r=computeIntegratedRayBudget(data.old,data.integrated);
 r.provenance={source:"scripts/fourfold_integrated_true_ray_budget_exact.mjs",
  source_sha256:crypto.createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex'),
  inputs:INPUTS,execution:"The identical computeIntegratedRayBudget was actually evaluated with exact BigInt; all ball display radii were added outward.",
  proof:"results/R106-supplement-integrated-ray-and-boundary-bidisk.md"};
 const bytes=JSON.stringify(r,null,2)+"\n";
 if(process.argv[2])fs.writeFileSync(process.argv[2],bytes);else process.stdout.write(bytes);
}
