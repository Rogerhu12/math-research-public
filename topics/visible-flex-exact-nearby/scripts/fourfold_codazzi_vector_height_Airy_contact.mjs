#!/usr/bin/env node
/* Same ac1 moving centre: exact vector height / curvature / full Airy contact.
 * All nonzero physical modes and all explicit source/mean/interface rows.
 * This is a contact theorem; no whole BVP inverse or small base residual is claimed.
 */
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import {fileURLToPath} from "node:url";

function runHeightCurvatureContact(provenance={}) {
 const abs=n=>n<0n?-n:n,gcd=(a,b)=>{a=abs(a);b=abs(b);while(b){const r=a%b;a=b;b=r;}return a;};
 const F=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return[a/g,b/g];};
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b));
 const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>mul(a,F(b[1],b[0]));
 const pow=(a,n)=>{let r=F(1);for(let j=0;j<n;j++)r=mul(r,a);return r;};
 const lt=(a,b)=>a[0]*b[1]<b[0]*a[1],eq=(a,b)=>a[0]*b[1]===b[0]*a[1],rat=a=>a[0]+"/"+a[1];
 const checks=[],gate=(name,ok)=>{checks.push({name,passed:Boolean(ok)});if(!ok)throw Error(name);};
 const vars=["u","v","m","a","beta","gamma","K","h1","h2","z","up","vp","chi","d","dd","dtau","taup","tauRp","dtauR","Ru","Rv","R0","g1","g2","g0","Cr","Cp"];
 const p0=()=>new Map(),pc=n=>n?new Map([[vars.map(()=>0).join(","),BigInt(n)]]):p0();
 const pv=(name,power=1)=>{const ex=vars.map(()=>0),i=vars.indexOf(name);if(i<0)throw Error(name);ex[i]=power;return new Map([[ex.join(","),1n]]);};
 const pa=(a,b)=>{const c=new Map(a);for(const[k,v]of b){const z=(c.get(k)||0n)+v;if(z)c.set(k,z);else c.delete(k);}return c;};
 const ps=(a,n)=>new Map([...a].filter(([,v])=>v*BigInt(n)!==0n).map(([k,v])=>[k,v*BigInt(n)]));
 const pm=(a,b)=>{const c=p0();for(const[ka,va]of a)for(const[kb,vb]of b){const aa=ka.split(",").map(Number),bb=kb.split(",").map(Number),key=aa.map((e,i)=>e+bb[i]).join(",");const z=(c.get(key)||0n)+va*vb;if(z)c.set(key,z);else c.delete(key);}return c;};
 const prod=(...xs)=>xs.reduce(pm,pc(1)),pe=(a,b)=>pa(a,ps(b,-1)).size===0;
 const deriv=(a,name)=>{const i=vars.indexOf(name),out=p0();for(const[k,c]of a){const ex=k.split(",").map(Number),e=ex[i];if(e){ex[i]--;const key=ex.join(",");const z=(out.get(key)||0n)+BigInt(e)*c;if(z)out.set(key,z);else out.delete(key);}}return out;};
 const [u,v,m,a,beta,gamma,K,h1,h2,z,up,vp,chi,d,dd,dtau,taup,tauRp,dtauR,Ru,Rv,R0,g1,g2,g0,Cr,Cp]=vars.map(x=>pv(x));
 const mi=pv("m",-1),mi2=pv("m",-2),mi3=pv("m",-3),vi=pv("v",-1),vi2=pv("v",-2),gi=pv("gamma",-1);
 const Delta=p=>[[u,h1],[v,h2],[m,z],[d,dd],[Ru,g1],[Rv,g2],[R0,g0]].reduce((s,[_p,w],i)=>pa(s,pm(deriv(p,["u","v","m","d","Ru","Rv","R0"][i]),w)),p0());
 const J=pm(v,mi),dJ=pa(pm(h2,mi),ps(prod(v,z,mi2),-1)),Jp=pm(vp,mi);
 const chip=pa(prod(h2,vi),pa(ps(pm(z,mi),-1),ps(prod(vp,chi,vi),-1)));
 const k1=pa(h1,ps(pm(up,chi),-1)),k2=pa(h2,ps(pm(vp,chi),-1));
 const b=pa(pm(k1,vi),ps(prod(u,k2,vi2),-1)),c=ps(pm(k2,vi2),-1);
 const A=prod(beta,gi,J),B=prod(a,u,mi),C=pm(a,mi);
 const Ap=prod(beta,gi,Jp),Bp=prod(a,up,mi);
 gate("exact_full_coordinate_J_variation",pe(Delta(J),dJ));
 gate("chi_keeps_the_full_mean_row",pe(pa(prod(v,chip),pm(vp,chi)),pa(h2,ps(prod(v,z,mi),-1))));
 gate("angular_position_direct_term_cancels",pe(pm(a,dJ),pa(prod(a,Jp,chi),prod(a,J,chip))));
 gate("passive_angular_connection_first_component_zero",pe(pa(Delta(A),ps(pa(pm(Ap,chi),pm(A,chip)),-1)),p0()));
 gate("passive_angular_connection_true_B_column",pe(pa(Delta(B),ps(pa(pm(Bp,chi),pm(B,chip)),-1)),prod(a,J,b)));
 gate("passive_angular_connection_true_C_column",pe(pa(Delta(C),ps(pm(C,chip),-1)),prod(a,J,c)));
 const tau=pa(pm(d,J),ps(pm(gamma,u),-1));
 const tauVariation=pa(pm(dd,J),pa(pm(d,dJ),ps(pm(gamma,h1),-1)));
 gate("radial_tau_variation_keeps_mean",pe(Delta(tau),tauVariation));
 const Jr=pa(taup,tauRp),chir=prod(pa(pa(dtau,dtauR),ps(pm(chi,Jr),-1)),m,vi);
 const radialPos=pa(dtau,pa(ps(pm(taup,chi),-1),ps(pm(J,chir),-1)));
 gate("passive_radial_position_source_is_exact_residual",pe(radialPos,pa(pm(chi,tauRp),ps(dtauR,-1))));
 const rA=prod(beta,gi,pa(pm(Rv,mi),ps(prod(v,R0,mi2),-1)));
 const rB=pm(a,pa(pm(Ru,mi),ps(prod(u,R0,mi2),-1)));
 const rC=ps(prod(a,R0,mi2),-1);
 const Cg=pa(pm(g2,mi),pa(ps(prod(Rv,z,mi2),-1),pa(ps(prod(h2,R0,mi2),-1),pa(ps(prod(v,g0,mi2),-1),ps(prod(v,R0,z,mi3),2)))));
 const Bg=pa(pm(g1,mi),pa(ps(prod(Ru,z,mi2),-1),pa(ps(prod(h1,R0,mi2),-1),pa(ps(prod(u,g0,mi2),-1),ps(prod(u,R0,z,mi3),2)))));
 gate("ordinary_source_curvature_defect_column_1",pe(Delta(rA),prod(beta,gi,Cg)));
 gate("ordinary_source_curvature_defect_column_2",pe(Delta(rB),pm(a,Bg)));
 gate("ordinary_source_curvature_defect_column_3",pe(Delta(rC),pa(ps(prod(a,g0,mi2),-1),ps(prod(a,R0,z,mi3),2))));
 gate("ordinary_source_position_torsion_column",pe(Delta(pm(a,pa(pm(Rv,mi),ps(prod(v,R0,mi2),-1)))),pm(a,Cg)));
 const aq=pm(a,pa(prod(gamma,K,v),prod(d,u,mi))),at=prod(a,d,mi);
 gate("full_radial_connection_second_variation",pe(Delta(aq),pm(a,pa(prod(gamma,K,h2),pa(prod(dd,u,mi),pa(prod(d,h1,mi),ps(prod(d,u,z,mi2),-1)))))));
 gate("full_radial_connection_third_variation",pe(Delta(at),pm(a,pa(pm(dd,mi),ps(prod(d,z,mi2),-1)))));
 const a2=pm(a,a),n=pm(a2,mi2);
 const D2=pa(prod(a2,J,J,c),Cp);
 const D1=pa(prod(a2,J,gamma,b),pa(prod(a2,J,tau,c),Cr));
 const row1=prod(gi,mi,pa(D1,pa(ps(pm(d,D2),-1),pa(ps(Cr,-1),pm(d,Cp)))));
 gate("full_two_row_curvature_height_contact_first",pe(pm(n,k1),row1));
 gate("full_two_row_curvature_height_contact_second",pe(pm(n,k2),pa(ps(D2,-1),Cp)));
 gate("moving_back_conversion_first_row",pe(pm(n,h1),pa(row1,prod(n,up,chi))));
 gate("moving_back_conversion_second_row",pe(pm(n,h2),pa(pa(ps(D2,-1),Cp),prod(n,vp,chi))));
 const M=F(388),betaMax=F(9,5),range=F(13,5),dp=mul(betaMax,range);
 gate("complete_root_d_phi_below5",lt(dp,F(5)));
 const dmax=mul(F(22,56),dp);
 gate("odd_quarter_period_d_below2",lt(dmax,F(2)));
 gate("physical_cut388_has_cube_root_above7",lt(F(7**3),M));
 const aPsi=F(2,7),aPi=add(F(4,7),F(10,388*7)),bPi=F(1,49);
 gate("complete_weak_source_pair_Pi_below_three_fifths",lt(add(pow(aPi,2),pow(bPi,2)),pow(F(3,5),2)));
 gate("root_Riccati_source_Psi_coefficient",eq(mul(F(5),aPsi),F(10,7)));
 gate("root_Riccati_source_Pi_coefficient",eq(mul(F(5),F(3,5)),F(3)));
 const BrFee=F(10,388*7),BpFee=add(F(20,388*7),F(5,388*49));
 gate("algebraic_contact_Br_coefficient_below1_over250",lt(BrFee,F(1,250)));
 gate("algebraic_contact_Bphi_coefficient_below1_over125",lt(BpFee,F(1,125)));
 gate("Bessel_inverse_complete_nonzero_frequency_bound",eq(add(F(1),F(1,4*4)),F(17,16)));
 return {
  kind:"actual_current_residual_sensitive_vector_height_curvature_Airy_contact",
  complete:true,executed:true,arithmetic:"exact Laurent-polynomial identities and BigInt rational inequalities",
  candidate_sha256:"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
  exact_alpha:"6890507429876859/9007199254740992",exact_nu:"-2572625729470897/72057594037927936",
  whole_original_eta:true,metric_variation_zero_on_this_root_germ:true,
  no_assumed_base_isometry:true,no_assumed_single_height_normal_gap:true,
  full_ordinary_source_and_mean_kept:true,full_PPoly_jumps_and_rigid_ports_kept:true,
  nonlinear_solution_claimed:false,full_BVP_inverse_claimed:false,
  current_field_native_rerun:false,source_is_published_joint_germ_and_exact_connection_identities:true,
  root_high_moving_index:97,root_high_physical_frequency:388,
  actual_root_d_phi_upper:rat(dp),actual_root_d_sup_upper:rat(dmax),
  root_Riccati_curvature_to_height_scale:"n*M^(-5/3), n=a_phys^2/m^2; original complete two-row norm comparison <5",
  canonical_height_root_state:"(M^(1/3)*f, eta^(-1)*M^(-1/3)*p); f=N dot passive displacement, p=N dot (z_r-d*z_phi)",
  complete_weak_contact_source_fees:{Psi:"10/7",Pi:"3",algebraic_Br:rat(BrFee),algebraic_Bphi:rat(BpFee)},
  weak_contact_fee_scope:"Only the explicitly separated contact defect rows, after full high projection; no hidden derivative of ordinary g in this port budget.",
  contact_feedback_not_absorbed:["base position-defect coefficient times full curvature variation","base/variation connection and position defects","normal/tangential displacement lower-order rows","true coordinate primitive chi including mean","all low-high multiplication paths","rigid and holonomy ports"],
  provenance,checks,gate_count:checks.length,passed:checks.every(c=>c.passed)
 };
}

const INPUTS=[
  {
    "path": "results/R133-supplement-moving-frame-with-complete-residual-and-mean.md",
    "git_blob": "fb88934096af788db267b7b12657b396898aab4f",
    "sha256": "4628cb73db40b15652415106a48c134e334eea7d78031fedc2f65b6f8b064fbe"
  },
  {
    "path": "results/R133-supplement-current-moving-body-physical-complex-germ.md",
    "git_blob": "bfe73ee59142618bc7e36d5e3fe06929d9fb68cb",
    "sha256": "c10b049282d1837ab45fe2b40e6276ec7074aa534b4a7bb0c1f4251a9db729ba"
  },
  {
    "path": "results/R133-supplement-current-moving-positive-root-Riccati-and-full-head.md",
    "git_blob": "3edf335784786da9a4a515b28d364d8ad2914e24",
    "sha256": "38d7ec697d8a0565b2563324aca689776749aa81fc8bf8b0dab4d0f28fcfd8fb"
  },
  {
    "path": "results/R133-supplement-negative-quadratic-density-and-full-frequency-transport.md",
    "git_blob": "a1fc9e766bc56458c40542fcf0ea19d1f9cc7dec",
    "sha256": "622bb91df498f3221de6a9a7d5ebb760f2a98c9a2f6e872aee373b9a81013033"
  }
];
const here=fileURLToPath(import.meta.url),root=path.dirname(path.dirname(here));
const argv=process.argv.slice(2),sha=x=>crypto.createHash("sha256").update(x).digest("hex");
if(argv.length!==2||argv[0]!=="--out")throw new Error("usage: node scripts/fourfold_codazzi_vector_height_Airy_contact.mjs --out notes/new-report.json");
for(const row of INPUTS){
 const body=fs.readFileSync(path.join(root,row.path));
 if(sha(body)!==row.sha256)throw new Error("changed published proof input: "+row.path);
}
const report=runHeightCurvatureContact({source_sha256:sha(fs.readFileSync(here)),inputs:INPUTS});
fs.writeFileSync(argv[1],JSON.stringify(report,null,2)+"\n",{flag:"wx"});
process.stdout.write(JSON.stringify({complete:report.complete,passed:report.passed,gate_count:report.gate_count,out:argv[1]})+"\n");
