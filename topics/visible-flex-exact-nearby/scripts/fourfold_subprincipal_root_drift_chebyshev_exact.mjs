#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';
export const INPUTS=[
  {
    "key": "collar",
    "path": "notes/2026-11-12-beta-step3-true-derivative-collar-h1e5-domain500.json",
    "sha256": "b387ede87055d0a990cafca12002b8baead5a2415d2d4cef610dde99405efd08"
  },
  {
    "key": "existence",
    "path": "data/phase_ring_continuation/type_fixed_step02_d5_step5_real_parameter_return_existence.json",
    "sha256": "edd1450e9418ad060c54dd64885c7e5e77d3b34ba538d3da16b5395a2737cdc2"
  },
  {
    "key": "migration",
    "path": "notes/2026-11-13-R106-coarse-root-finite-part.json",
    "sha256": "da377ff1bd64f53b436eee714bda394f288cea8c41e167da0a680ea1ab4d6f4e"
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
function computeChebyshevRootDrift(input){
 const gates=[];const gate=(name,b)=>{gates.push({name,passed:!!b});if(!b)throw Error(name);};
 const H=input.collar,E=input.existence,G=input.migration;
 gate("complete original fixed-r derivative collar",H.complete===true);
 gate("previous complete coarse root geometry theorem",G.complete===true&&G.kind==="R106_complete_nonmean_reduced_root_finite_part_coarse_bound");
 gate("actual real-core principal field certificate",E.proved===true);
 gate("same exact affine origin and direction",H.origin_inputs_sha256===E.origin_inputs_sha256&&H.direction_sha256===E.frozen_direction_sha256);
 const p=Rat.p(G.scope.parameter_center),eta=Rat.p(G.scope.parameter_half_width);
 const lo=Rat.p(E.exact_parameter_interval[0]),hi=Rat.p(E.exact_parameter_interval[1]);
 gate("requested real parameter tube inside R75",(lo.le(p.sub(eta))&&p.add(eta).le(hi)));
 const hlo=Rat.p(H.exact_parameter_interval[0]),hhi=Rat.p(H.exact_parameter_interval[1]);
 gate("requested parameter tube inside complex root collar",hlo.le(p.sub(eta))&&p.add(eta).le(hhi));
 const M=Rat.p(7000000000),m=Rat.p(9),R=Rat.p("1/2000"),h=Rat.p("3/10000");
 const outer=Rat.p(3),inner=Rat.p("21/20"),N=22;
 const theta=Rat.p("1/320");
 gate("real drift below nine",Rat.p(E.quotient_bounds_exact.drift).lt(m));
 gate("complex theta strips nested",theta.le(Rat.p(E.physical_theta_strip))&&theta.mul(4).le(Rat.p(H.sigma)));
 const tlo=endpoint(H.root,-1),thi=endpoint(H.root,1);
 const span=H.exact_common_span.map(Rat.p),cut=Rat.p(H.fixed_cut);
 gate("whole complex root disk in one actual scalar germ",span[0].lt(tlo.sub(R))&&thi.add(R).lt(span[1]));
 gate("real Chebyshev interval belongs to actual R75 radial domain",Rat.p(0).lt(tlo.sub(h))&&thi.add(h).lt(Rat.p("1080863910568919/4503599627370496")));
 gate("target root is real and radial",H.semantics.includes("real affine parameter")&&E.limitations.some(s=>s.includes("R37 modified")));
 const F=Rat.p(25),Ft=Rat.p("81/10"),R0=Rat.p("1/400"),gap=R0.sub(R);
 const area=Rat.p("9/5"),aa=Rat.p("1/5");
 gate("complete prior primitive bound",Rat.p(G.bounds.complete_F_component.exact_upper).le(F));
 gate("complete prior true angular tangent bound",Rat.p(G.bounds.complete_Ftheta_component.exact_upper).le(Ft));
 gate("paid positive whole complex area",area.lt(endpoint(H.domain.positive_real_minima.area2,-1)));
 gate("paid positive whole complex a0",aa.lt(endpoint(H.domain.positive_real_minima.a,-1)));
 const coarse=F.mul(Ft.pow(2)).mul(6).div(gap.pow(2).mul(area).mul(aa));
 gate("complete characteristic drift below seven billion",coarse.lt(M));
 const major=h.mul(outer.add(Rat.p(1).div(outer))).div(2);
 gate("outer Bernstein ellipse lies inside complete complex radial disk",major.le(R));
 const tailReal=M.mul(2).div(outer.pow(N).mul(outer.sub(1)));
 const ratio=inner.div(outer);
 const tailComplex=M.mul(2).mul(ratio.pow(N+1)).div(Rat.p(1).sub(ratio));
 const Q=m.add(tailReal).mul(inner.pow(N)).add(tailComplex);
 gate("whole inner ellipse drift below 28",Q.lt(28));
 const majorInner=h.mul(inner.add(Rat.p(1).div(inner))).div(2);
 const minorInner=h.mul(inner.sub(Rat.p(1).div(inner))).div(2);
 const rhoMax=thi.sub(cut),rhoSafe=Rat.p("1/4000"),tube=Rat.p("7e-6");
 gate("true cut is on inward real collar",Rat.p(0).lt(tlo.sub(cut))&&rhoMax.lt(rhoSafe));
 const ellipseTest=rhoSafe.add(tube).div(majorInner).pow(2).add(tube.div(minorInner).pow(2));
 gate("every radius-seven-micro disk along the real root collar fits inner ellipse",ellipseTest.lt(1));
 const rec=x=>({exact:x.str(),decimal_upper:x.decimalUpper()});
 return {kind:"R106_actual_complex_root_drift_from_real_axis_and_Chebyshev",complete:true,
   parameter_center:p.str(),parameter_half_width:eta.str(),physical_theta_strip:theta.str(),
   target_root_semantics:"t=t(p) is the real radial target-curvature root, independent of complex theta; not a nonradial detII root",
   outer_rho_radius:R.str(),real_half_interval:h.str(),outer_ellipse_parameter:outer.str(),
   inner_ellipse_parameter:inner.str(),degree:N,complex_drift_bound:rec(Q),safe_complex_drift_bound:"28",
   coarse_outer_drift:rec(coarse),real_axis_drift_safe:"9",real_Chebyshev_tail:rec(tailReal),
   complex_Chebyshev_tail:rec(tailComplex),inner_semimajor:rec(majorInner),inner_semiminor:rec(minorInner),
   entire_actual_root_collar_rho_upper:rec(rhoMax),uniform_complex_radial_tube:tube.str(),
   tube_ellipse_inclusion_polynomial:rec(ellipseTest),gates,
   not_proved:["signed Fourier coefficient vector of q","complete b-beta or any effective R104 cutoff","a result for a nonradial moving root t(theta)"]};
}

export {computeChebyshevRootDrift};
export function checkedReport(rootDir){
 const input={};
 for(const item of INPUTS){
  const raw=fs.readFileSync(path.join(rootDir,item.path));
  const digest=crypto.createHash("sha256").update(raw).digest("hex");
  if(digest!==item.sha256)throw Error("input SHA256 mismatch "+item.path);
  input[item.key]=JSON.parse(raw.toString("utf8"));
 }
 const result=computeChebyshevRootDrift(input);
 result.provenance={source:"scripts/fourfold_subprincipal_root_drift_chebyshev_exact.mjs",
  source_sha256:crypto.createHash("sha256").update(fs.readFileSync(fileURLToPath(import.meta.url))).digest("hex"),
  inputs:INPUTS,proof:"results/R106-supplement-root-drift-chebyshev.md",
  execution:"Exact BigInt computeChebyshevRootDrift; no new geometry or numerical samples."};
 return result;
}
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 const report=checkedReport(process.argv[2]||".");const text=JSON.stringify(report,null,2)+"\n";
 if(process.argv[3])fs.writeFileSync(process.argv[3],text);else process.stdout.write(text);
}
