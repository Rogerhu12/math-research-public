#!/usr/bin/env node
// Complete actual-center scalar arithmetic only. No phase field is invented.
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

function computeOneFormBudget(flow,ray){
 const gates=[],gate=(name,value)=>{gates.push({name,passed:!!value});if(!value)throw Error(name);};
 gate("actual whole 550 center g0",flow.complete&&flow.all_original_output_bytes_verified&&flow.g0.completed_segments===550);
 gate("same original index as true all-time tube",flow.g0.sha256===ray.provenance.center_g0_index_sha256);
 gate("same finite reference",flow.endpoint.descriptor_sha256===ray.provenance.reference_descriptor_sha256);
 gate("actual p5 point",flow.endpoint.exact_delta_fraction===ray.proved_region.parameter_center);
 const A=endpoint(flow.g0.summary.A),E=endpoint(flow.g0.summary.E);
 const Sg=Rat.p("1/256"),sigma=Rat.p("3/2048"),s=Rat.p("1/1024"),SB=Rat.p("1/512");
 gate("original paid center working strip",Rat.p(flow.endpoint.widths.flow).add(endpoint(flow.g0.summary.R)).eq(Sg));
 const R=Sg.sub(sigma),d=R.sub(A),delta=sigma.sub(s),L0=SB.sub(sigma),L=L0.sub(A);
 gate("true flow smallness",A.le(R.div(2)));
 gate("source analytic image margin",Rat.p(0).lt(L));
 gate("final Cauchy margin",Rat.p(0).lt(delta));
 const Xr=A.pow(3).div(d.pow(2).mul(2));
 const Er=E.mul(Rat.p(1).add(A.div(R)));
 const square=A.pow(3).div(d.mul(2)).add(A.mul(E));
 const primitive=Xr.add(Er).add(square.div(L0)).add(A.pow(3).div(L.pow(2).mul(3)));
 const K=primitive.div(delta),Q=Rat.p(1).div(Rat.p(1).sub(A.div(d)));
 gate("Jacobian rational majorant",A.lt(d));
 gate("complete primitive remainder per unit source below 3e-13",K.lt("3e-13"));
 gate("source error pullback factor below 1.00002",Q.lt("1.00002"));
 // Endpoint-only omitted local J is deliberately not reclassified as an all-time fee.
 const partialGeneric=A.pow(2).div(R.mul(2));
 const optionalGeneric=K.add(partialGeneric.div(delta));
 const record=q=>({exact:q.str(),decimal_upper_28:q.decimalUpper(28)});
 return {kind:"R106_actual_center_second_order_one_form_transport_prefactors",
   complete:true,arithmetic:"exact reduced BigInt; source display radii included outward",
   scope:{point_parameter:flow.endpoint.exact_delta_fraction,all_time_leg:"forward",
    segments:550,true_defect_strip:Sg.str(),Taylor_strip:sigma.str(),final_label_strip:s.str(),
    required_phase_reference_strip:SB.str(),mean_retained:true},
   bounds:{A:record(A),E:record(E),flow_third_order_tail:record(Xr),
    approximant_flow_error:record(Er),source_square_change_term:record(square),
    primitive_remainder_per_unit_phase_modulus:record(primitive),
    one_form_remainder_per_unit_phase_modulus:record(K),source_error_pullback_factor:record(Q),
    generic_partial_local_second_integral_bound:record(partialGeneric),
    coarse_prefactor_if_all_partial_local_second_terms_are_omitted:record(optionalGeneric)},
   gates,
   exact_finite_contract:"C(t),D(t) must retain complete partial-time local polynomials and all previous-time cross products; the saved endpoint D alone does not meet this contract.",
   not_proved:["actual nonmean phase field modulus or finite coefficients",
      "native seven-field geometry","phase integral","uniform-parameter one-form prefactor",
      "R104 effective cutoff","full PDE inverse"]};
}

const INPUTS=[
  {
    "key": "flow",
    "path": "notes/2026-11-12-complete-flow-43301401638-arithmetic-summary.json",
    "sha256": "f25a3692b36390b3ae8dd7699d4e0ec0c2e74561ac238b11352f1d532a8bfc52"
  },
  {
    "key": "ray",
    "path": "notes/2026-11-12-R106-actual-all-time-ray-tube.json",
    "sha256": "6463e62641b9187045016c63ee633816676a75baf941ea01375a6ae36f1a1863"
  }
];

export {computeOneFormBudget};
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 const data={};
 for(const item of INPUTS){
  const bytes=fs.readFileSync(item.path);
  if(crypto.createHash('sha256').update(bytes).digest('hex')!==item.sha256)
    throw Error("actual immutable input changed: "+item.path);
  data[item.key]=JSON.parse(bytes.toString('utf8'));
 }
 const result=computeOneFormBudget(data.flow,data.ray);
 result.provenance={source:"scripts/fourfold_one_form_budget_exact.mjs",
  source_sha256:crypto.createHash('sha256').update(fs.readFileSync(fileURLToPath(import.meta.url))).digest('hex'),
  inputs:INPUTS,execution:"Identical computeOneFormBudget actually evaluated using BigInt; all ball display radii added outward.",
  proof:"results/R106-supplement-second-order-one-form-pullback.md"};
 const out=JSON.stringify(result,null,2)+"\n";
 if(process.argv[2])fs.writeFileSync(process.argv[2],out);else process.stdout.write(out);
}
