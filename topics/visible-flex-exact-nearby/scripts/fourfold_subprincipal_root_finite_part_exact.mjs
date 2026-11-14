#!/usr/bin/env node
// Actual complete original-height reduced root finite-part bound.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';
export const INPUTS=[
  {
    "key": "migration",
    "path": "notes/2026-11-13-R106-whole-parameter-root-density.json",
    "sha256": "e465844f0880356afd80829a4fc782856db7fc61e513be2669d84a61e80f8a09",
    "json": true
  },
  {
    "key": "collar",
    "path": "notes/2026-11-12-beta-step3-true-derivative-collar-h1e5-domain500.json",
    "sha256": "b387ede87055d0a990cafca12002b8baead5a2415d2d4cef610dde99405efd08",
    "json": true
  },
  {
    "key": "primitive_kernel",
    "path": "scripts/fourfold_phase_beta_interval.py",
    "sha256": "ff159224bc1870b7580ef6e5f0370a4fcc385ed556d947003a0bb1667e6f4b0f"
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

export function coarseRootFinitePart(input){
 const {migration,collar}=input,gates=[];function check(name,ok){gates.push({name,passed:!!ok});if(!ok)throw Error(name);}
 check("previous actual root-density theorem complete",migration.complete===true&&migration.gates.every(x=>x.passed));
 check("same exact current parameter tube",migration.proved_region.parameter_center==="-7789843107295549/4611686018427387904"&&migration.proved_region.parameter_half_width==="1/1000000000");
 check("whole original complex collar complete",collar.complete===true&&collar.exact_center_parameter==="-7832869216826619/4611686018427387904"&&collar.exact_parameter_half_width==="1/100000");
 check("same original infinite geometry",collar.origin_inputs_sha256==="0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b"&&collar.direction_sha256==="8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab");
 const budget=collar.base_input_budget,R=Rat.p(migration.proved_region.complex_root_radius),S=Rat.p(migration.proved_region.physical_theta_strip),R0=Rat.p("1/400"),sigma=Rat.p("31/100");
 check("nested radial input disk",R.lt(R0)&&R0.lt(endpoint(budget.radial_radius,-1))&&R.lt(collar.radial_radius));
 check("nested exact angular input strip",sigma.lt(endpoint(budget.sigma_normalized_x,-1))&&S.mul(4).lt(sigma)&&S.eq(Rat.p(collar.sigma).div(4)));
 const A=Rat.p("11/10"),T=Rat.p("73/10"),Z=Rat.p("3/10");
 check("true circumference radius bound",endpoint(budget.radius_bound).lt(A));
 check("true tangent component modulus bound",endpoint(budget.tangent_bound).lt(T));
 check("true height component bound",endpoint(budget.height_bound).lt(Z));
 const exponent=sigma.sub(S.mul(4)),expLower=Rat.p(1).add(exponent).add(exponent.pow(2).div(2));
 check("actual Fourier ratio below three quarters",Rat.p("4/3").lt(expLower));
 const F=Rat.p(25),Ft=Rat.p("81/10");
 check("complete infinite primitive component bound",A.mul(T).mul(3).add(Z).lt(F));
 check("complete true physical Ftheta bound",A.mul(T).lt(Ft));
 const gap=R0.sub(R),Fr=F.div(gap),Frt=Ft.div(gap);
 const area=Rat.p("9/5"),a0=Rat.p("1/5");
 check("true complete area squared denominator",area.lt(endpoint(collar.domain.positive_real_minima.area2,-1)));
 check("true complete a0 denominator",a0.lt(endpoint(collar.domain.positive_real_minima.a,-1)));
 const Q=Fr.mul(Ft).mul(Frt).mul(6).div(area.mul(a0)),Qsafe=Rat.p("7000000000");
 check("actual complete q bound",Q.lt(Qsafe));
 const kmod=endpoint(collar.domain.deflated_curvature_real_upper).add(endpoint(collar.domain.deflated_curvature_imaginary_absolute_upper)),K=Rat.p(50);
 check("target curvature branch positive",Rat.p(0).lt(endpoint(collar.domain.deflated_curvature_real_lower,-1)));
 check("target curvature factor modulus below 81",kmod.lt(81));
 check("actual complete kstar bound",Rat.p(9).div(a0).lt(K));
 const Rs=Rat.p("1/2500000"),split=Rs.div(2),image=Rat.p(migration.bounds.true_physical_image.exact_upper),J=Rat.p(migration.bounds.true_J_modulus.exact_upper),inner=Rat.p("1/450");
 check("complex square-root disk remains in same radial germ",Rs.pow(2).lt(R));
 const movement=Qsafe.mul(Rs.pow(2)).add(K.mul(Rs.pow(3)).mul("2/3"));
 check("true local complex root ray stays inside smaller physical strip",image.add(movement).lt(inner)&&inner.lt(S));
 const jacExp=movement.div(S.sub(inner));
 check("complete Jacobian exponent below four thirds",jacExp.lt("4/3"));
 const x=Rat.p("4/3");let term=Rat.p(1),sum=Rat.p(1);for(let j=1;j<=20;j++){term=term.mul(x).div(j);sum=sum.add(term);}const tail=term.mul(x).div(21).div(Rat.p(1).sub(x.div(22))),expUpper=sum.add(tail);
 check("exact exponential four-thirds bound below four",expUpper.lt(4));
 const rootLower=endpoint(collar.root,-1),cut=Rat.p(collar.fixed_cut);
 check("actual cut outside the tiny local split",split.pow(2).lt(rootLower.sub(cut)));
 const realN=Rat.p("491/10000"),complexN=realN.mul(4);
 check("previous complete real-time numerator pays realN",Rat.p(migration.bounds.pulled_regularized_numerator.exact_upper).lt(realN));
 const analyticRemainder=complexN.div(Rs.pow(3)),constantCounterterm=complexN.div(split.pow(3).mul(3)),quadraticCounterterm=complexN.div(Rs.pow(2).mul(split)),outerReal=realN.div(split.pow(3).mul(3));
 const total=analyticRemainder.add(constantCounterterm).add(quadraticCounterterm).add(outerReal);
 check("complete single-root reduced finite part below 2e19",total.lt("20000000000000000000"));
 const rec=v=>({exact_upper:v.str(),decimal_upper_22:v.decimalUpper()});
 return {kind:"R106_complete_nonmean_reduced_root_finite_part_coarse_bound",complete:true,arithmetic:"exact BigInt; no new geometric samples",scope:{parameter_center:migration.proved_region.parameter_center,parameter_half_width:migration.proved_region.parameter_half_width,label_strip:"1/1024",physical_theta_strip:S.str(),root_density:"same original-height reduced Dred; not grounded D and not full Fcal/mu",interval:"one actual root to the original fixed physical cut, with the R106 half-integral normalization",reference_label:"original H5/4 initial label, with true endpoint J retained",both_roots:"the same absolute estimate applies by exact radial reflection and the complete all-time J bound"},bounds:{complete_F_component:rec(F),complete_Ftheta_component:rec(Ft),complete_Fr_component:rec(Fr),complete_Frtheta_component:rec(Frt),q_actual_modulus_majorant:rec(Q),q_safe:rec(Qsafe),kstar_safe:rec(K),complex_s_radius:Rs.str(),local_split:split.str(),complex_root_ray_movement:rec(movement),Jacobian_exponent:rec(jacExp),exp_four_thirds_upper:rec(expUpper),complex_J:rec(J.mul(4)),complex_regularized_numerator:rec(complexN),analytic_small_interval_remainder:rec(analyticRemainder),constant_counterterm:rec(constantCounterterm),quadratic_counterterm:rec(quadraticCounterterm),outer_real_integral:rec(outerReal),single_root_reduced_finite_part:rec(total),safe_single_root_bound:"20000000000000000000",safe_two_roots_bound:"40000000000000000000"},gates,not_proved:["effective R104 frequency cutoff compatible with the actual low block","signed finite Fourier reference for b-beta","S angular-divergence integral, ordinary cut fluxes, or root endpoint term in the full phase","complete returned subprincipal phase or full PDE inverse"]};
}

export function checkedCoarseRoot(raw,sourceSha256,sha256){
 const parsed={},verified=[];for(const spec of INPUTS){const s=raw[spec.key];if(typeof s!=="string"||sha256(s)!==spec.sha256)throw Error("input SHA mismatch: "+spec.path);if(spec.json)parsed[spec.key]=JSON.parse(s);verified.push({...spec,utf8_characters:s.length});}
 const out=coarseRootFinitePart(parsed);out.provenance={source:"scripts/fourfold_subprincipal_root_finite_part_exact.mjs",source_sha256:sourceSha256,proof:"results/R106-supplement-coarse-complete-root-finite-part.md",inputs:verified,execution:"Identical pure checkedCoarseRoot/coarseRootFinitePart implementation actually executed with BigInt in V8; native CLI is a replay wrapper.",effectiveness:"A true finite whole-parameter nonmean root bound, deliberately coarse. It is not an effective R104 cutoff or a signed Fourier approximation."};return out;
}

if(process.argv[1]&&pathToFileURL(path.resolve(process.argv[1])).href===import.meta.url){
 if(process.argv.length!==4)throw Error("usage: node SCRIPT TOPIC_DIRECTORY OUTPUT.json");
 const topic=path.resolve(process.argv[2]),out=path.resolve(process.argv[3]);
 const hash=s=>crypto.createHash("sha256").update(s,"utf8").digest("hex");
 const raw=Object.fromEntries(INPUTS.map(x=>[x.key,fs.readFileSync(path.join(topic,x.path),"utf8")]));
 const report=checkedCoarseRoot(raw,hash(fs.readFileSync(fileURLToPath(import.meta.url),"utf8")),hash);
 fs.mkdirSync(path.dirname(out),{recursive:true});fs.writeFileSync(out,JSON.stringify(report,null,2)+"\n");
 console.log(JSON.stringify({complete:report.complete,gates:report.gates.length,finite_part_bound:report.bounds.single_root_reduced_finite_part,sha256:hash(fs.readFileSync(out,"utf8"))}));
}
