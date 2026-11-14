#!/usr/bin/env node
// Restore the exact R108 native report after executor loss.
// This reexecutes exact BigInt rational arithmetic and requires the SHA of
// the complete original native report before preserving its execution metadata.
import {readFileSync,writeFileSync} from "node:fs";
import {createHash} from "node:crypto";
import {resolve,dirname} from "node:path";
import {fileURLToPath} from "node:url";
const sha=x=>createHash("sha256").update(x,"utf8").digest("hex");
export const recover=function(inputs){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){let c=a%b;a=b;b=c;}return a;};
 const F=(n,d=1n)=>{if(typeof n==="object"&&n.n!==undefined)return n;n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}if(!d)throw Error("zero");const g=gcd(n,d);return {n:n/g,d:d/g};};
 const add=(a,b)=>{a=F(a);b=F(b);return F(a.n*b.d+b.n*a.d,a.d*b.d);};
 const neg=a=>F(-a.n,a.d),sub=(a,b)=>add(a,neg(F(b)));
 const mul=(a,b)=>{a=F(a);b=F(b);return F(a.n*b.n,a.d*b.d);};
 const div=(a,b)=>{a=F(a);b=F(b);return F(a.n*b.d,a.d*b.n);};
 const pow=(a,k)=>F(a.n**BigInt(k),a.d**BigInt(k));
 const lt=(a,b)=>{a=F(a);b=F(b);return a.n*b.d<b.n*a.d;};
 const dec=x=>{x=String(x);if(x.includes("/")){let [a,b]=x.split("/");return F(a,b);}let m=/^([+-]?)(\d*)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/.exec(x);if(!m)throw Error(x);let e=Number(m[4]||0)-(m[3]||"").length;let n=BigInt((m[2]||"0")+(m[3]||""));if(m[1]==="-")n=-n;return e>=0?F(n*10n**BigInt(e)):F(n,10n**BigInt(-e));};
 const str=a=>a.d===1n?a.n.toString():a.n+"/"+a.d;
 const interval=x=>{if(typeof x==="object"){if("ball"in x)return interval(x.ball);if("numerator"in x){const q=F(x.numerator,x.denominator);return[q,q];}throw Error("format");}
 const s=String(x).trim();if(!s.startsWith("[")){const q=dec(s);return[q,q];}
 const m=/^\[\s*(\S+)\s+\+\/-\s+(\S+)\s*\]$/.exec(s);if(!m)throw Error(s);const c=dec(m[1]),r=dec(m[2]);return[sub(c,r),add(c,r)];};
 const upper=x=>interval(x)[1],lower=x=>interval(x)[0];
 const ceil=(a,k=18)=>{const s=10n**BigInt(k),q=(a.n*s+a.d-1n)/a.d,t=q.toString().padStart(k+1,"0");return t.slice(0,-k)+"."+t.slice(-k);};
 const isqrt=n=>{if(n<2n)return n;let x=1n<<BigInt((n.toString(2).length+1)>>1);while(true){const y=(x+n/x)>>1n;if(y>=x)return x;x=y;}};
 const sqrt=(a,k=24)=>{const s=10n**BigInt(k);let q=isqrt(a.n*s*s/a.d);if(q*q*a.d<a.n*s*s)q++;return F(q,s);};
 const rec=x=>({numerator:x.n.toString(),denominator:x.d.toString(),decimal_upper:ceil(x)});
 const checks=[],check=(name,c)=>{checks.push({name,passed:!!c});if(!c)throw Error(name);};
 const {frame,v0,v1,contact:cap,root}=inputs;
 check("all_original_reports_proved",Object.values(inputs).every(x=>x.proved));
 const identity=frame.identity;
 for(const key of ["exact_parameter_interval","exact_center_parameter","exact_parameter_half_width","origin_inputs_sha256","direction_sha256"])
 check("same_actual_identity_"+key,[v0,v1,root].every(x=>JSON.stringify(x.identity[key])===JSON.stringify(identity[key])));
 check("same_eta_1e-9",identity.exact_parameter_half_width==="1/1000000000");check("R96_all_178_cells",cap.actual_cells===178);
 const wf=(name,order)=>{const x=frame.fields[name].Wiener[String(order)];return add(upper(x.norm),upper(x.error));};
 const t0=dec("1.477443"),I0=dec(".831"),I1=dec("1.489006"),mu0=dec("24.940215"),mu1=dec("31.245346"),Y=dec(".055953");
 check("true_root_height_sup",lt(wf("t0",0),t0));
 check("true_inverse_height_sup",lt(upper(frame.fields.inverse_t0.complex_modulus),I0));
 check("true_inverse_height_physical_first_derivative",lt(wf("inverse_t0",1),I1));
 check("true_root_momentum_shear_sup",lt(wf("root_momentum_shear",0),mu0));
 check("true_root_momentum_shear_physical_derivative",lt(wf("root_momentum_shear",1),mu1));
 const C=cap.constants;check("true_root_angle_derivative_lower",lt(Y,lower(C.root_angle_derivative_lower.lower)));
 const eps=dec(".000001552858"),G=dec("33.417980"),H=F(49,102400),tmin=dec("1.1568");
 check("true_principal_normalized_error",lt(upper(C.epsilon.upper),eps));check("true_covariant_log_height_derivative",lt(upper(C.G0.upper),G));check("true_height_positive_lower",lt(tmin,lower(C.actual_height_lower.lower)));
 check("same_paid_canonical_height",!lt(H,lower(C.canonical_flat_height))&&!lt(upper(C.canonical_flat_height),H));
 check("height_drift_denominator_positive",lt(mul(G,H),1));
 const Tmax=div(t0,sub(1,mul(G,H))),inv=div(pow(Tmax,2),sub(1,eps)),L=dec("2.257");
 check("actual_full_inverse_density_not_height_only",lt(inv,L));
 const B0=F(692327),B1=F(143113),V0=F(5176),V1=F(1186);
 for(const[name,data,order,val]of [["b_M0",v1,0,B0],["b_M1",v1,1,B1],["v0_M0",v0,0,V0],["v0_M1",v0,1,V1]]){
 const row=data.budgets.find(x=>x.high_cutoff===256&&x.weight_order===0&&x.moment===order);check("complete_actual_"+name,lt(upper(row.true_scaled_Wiener_upper),val));}
 const qlo=F(243,25),qhi=F(10);check("complete_actual_q_lower",lt(qlo,lower(v0.true_frequency.lower)));check("complete_actual_q_upper",lt(upper(v0.true_frequency.upper),qhi));
 const L1=div(I1,Y),H2=mul(I0,mu0),L2=div(add(mul(I0,mu1),mul(mu0,I1)),Y),Db=mul(mul(4,qhi),B1),Dv=mul(mul(4,qhi),V1);
 const cm=sqrt(mul(L,H)),c1=sqrt(mul(div(L,pow(tmin,2)),add(div(pow(H,5),20),div(pow(H,2),mul(2,pow(mul(4,qlo),2))))));
 const Ereg=upper(C.regular_mean_extension_energy.upper),contacts=Object.fromEntries(cap.high_root_contact_table.map(x=>[x.canonical_output_cutoff_N,x]));
 const rows=[];
 for(const r of root.budgets){const K=r.canonical_high_cutoff,lam=dec(r.strict_Lambda_lower),cube=dec(r.strict_cuberoot_Lambda_lower);
 check("strict_frequency_lower_K"+K,lt(lam,mul(mul(4,qlo),K+1)));check("strict_cube_lower_K"+K,lt(pow(cube,3),lam));
 let mean=add(div(mul(F(39,100),L1),pow(cube,2)),div(mul(F(54,100),L2),mul(lam,cube)));
 mean=add(mean,div(mul(F(39,100),add(add(mul(Db,I0),mul(B0,L1)),add(mul(Dv,H2),mul(V0,L2)))),mul(pow(lam,2),pow(cube,2))));
 const E=upper(contacts[K].root_extension_energy.upper),cr=sqrt(E),cj=sqrt(add(E,Ereg));
 rows.push({canonical_high_input_cutoff:K,all_output_modes_and_mean_retained:true,Lambda_strict_lower:str(lam),cube_Lambda_strict_lower:str(cube),
 full_mean_functional_upper:rec(mean),complete_gap_mean_fee:rec(mul(cm,mean)),root_contact_mean_fee:rec(mul(mul(cr,cm),mean)),root_contact_R1_coefficient:rec(mul(cr,c1)),root_and_regular_contact_mean_fee:rec(mul(mul(cj,cm),mean)),root_and_regular_contact_R1_coefficient:rec(mul(cj,c1)),root_contact:rec(cr),root_and_regular_contact:rec(cj)});}
 return {kind:"R108_complete_canonical_compact_stream_actual_budget",proved_actual_coefficient_and_mean_budget:true,proved_new_full_cap_gap:false,actual_identity:identity,
 angular_normalization:"unaveraged integral; e_phi=(2*pi/q)^(-1/2); physical e_theta=(2*pi)^(-1/2)",paid_canonical_height:str(H),true_root_height_upper:rec(t0),
 complete_principal_relative_error_upper:rec(eps),complete_height_log_derivative_upper:rec(G),complete_height_upper:rec(Tmax),inverse_density_factor_including_normalized_matrix:rec(inv),clean_inverse_density_factor:rec(L),
 gap_mean_coefficient:rec(cm),gap_R1_coefficient:rec(c1),coefficient_bounds:Object.fromEntries(Object.entries({I0,I1,mu0,mu1,Yprime_lower:Y,L1,H2,L2,B0,B1,V0,V1,Db,Dv}).map(([k,v])=>[k,rec(v)])),tables:rows,checks,
 unpaid_input:"R1 = sup_y || P_can(chi U_completed)(y)/y || from all continuous angles/radii, all cutoff, full E and height terms",
 scope:["Full physical cap with unchanged Robin form; compact primal and solenoidal dual vanish before outer port.","Canonical input high projection never replaces physical projection or removes low output rows.","No new wide-collar geometry was sampled; actual range is only the already proved R96 collar.","A fixed y^2 completion alone does not authorize high-input strong gain; R108 supplies right-input Airy localization."]};
};
const INPUTS=[
  {
    "key": "frame",
    "path": "notes/2026-11-12-ci-actual-root-Cauchy-frame-Fourier-summary.json",
    "sha256": "8c13c40e1ea65eb05a97eaeb79cba1ab49f8ebe734ad598d0b382a0afe6890bf"
  },
  {
    "key": "v0",
    "path": "notes/2026-11-12-ci-canonical-v0-scaled-Wiener-summary.json",
    "sha256": "66112956b245389aa38c3d07244685ad31c29f7aae0575b8986bf80b54459ce8"
  },
  {
    "key": "v1",
    "path": "notes/2026-11-12-ci-canonical-v1-scaled-Wiener-summary.json",
    "sha256": "c0050bf6f15666f1b0283d7d232c10a167d08a4bb69e42c6cc5653dc51c94c3b"
  },
  {
    "key": "contact",
    "path": "notes/2026-11-12-ci-direct-canonical-source-summary.json",
    "sha256": "826bda30e5d42bf47efc4fb5daa3bf6da1361bb2f4ee737486f89be9c597ca09"
  },
  {
    "key": "root",
    "path": "notes/2026-11-12-actual-common-root-high-remainder.json",
    "sha256": "e727251cd6c187ded5782aff3a03401301d21b83fd03d419f31f716862be6253"
  }
];
if(process.argv[1]&&resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 const topic=resolve(dirname(fileURLToPath(import.meta.url)),".."),inputs={};
 for(const s of INPUTS){const raw=readFileSync(resolve(topic,s.path),"utf8");if(sha(raw)!==s.sha256)throw Error("input mismatch "+s.path);inputs[s.key]=JSON.parse(raw);}
 const report=recover(inputs);report.input_reports=INPUTS;
 const native=readFileSync(resolve(topic,"scripts/fourfold_phase_canonical_stream_gap_budget.py"),"utf8");
 report.source_sha256=sha(native);
 if(report.source_sha256!=="990fee2aa077fdc666be234184f4dc89cf2d0944a8039de69f62de1c1c3d7bf7")throw Error("original native source changed");
 report.execution={full_native_entry_executed:true,arithmetic:"Python exact Fraction, integer isqrt, directed rational decimals; no binary floating point",reconstructed_after_executor_loss:true,lost_old_report_reused:false};
 const text=JSON.stringify(report,null,2)+"\n";
 const expected="c1b90d922f0484358397b66c149efeb36e0eeb54412eadc3ae6ad022740d4a7c";
 if(sha(text)!==expected)throw Error("reconstruction differs from observed native report SHA");
 const out=process.argv[2]||resolve(topic,"notes/2026-11-12-R108-canonical-stream-gap-budget.json");
 writeFileSync(out,text);process.stdout.write(JSON.stringify({exact_checks:report.checks.length,original_native_report_sha256:sha(text),byte_identity_verified:true})+"\n");
}
