#!/usr/bin/env node
/** Actual final-centre outer mean ports; exact BigInt budgets only. */
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
function calculate(){
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;};
  const q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};};
  const add=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d);
  const mul=(a,b)=>q(a.n*b.n,a.d*b.d);
  const lt=(a,b)=>a.n*b.d<b.n*a.d;
  const str=a=>a.n.toString()+'/'+a.d.toString();
  const decimal=(a,p=24)=>{if(a.n<0n)throw Error('only positive outward budgets');const s=10n**BigInt(p),z=(a.n*s+a.d-1n)/a.d;const t=z.toString().padStart(p+1,'0');return t.slice(0,-p)+'.'+t.slice(-p);};
  const epsilon=q(271,250000000),change=q(51,16),low_weight=q(3);
  const high_reflection=q(111,5000000),low_to_high=q(47,2000000);
  const high_fB=q(3,100000),high_rB=q(22),high_rC=q(26);
  const own_fB=q(41,10000000),own_rC=q(50);
  const ec=mul(epsilon,change);
  const exact={
    canonical_stable_high:mul(ec,add(q(1),high_reflection)),
    complete_nonmean_head:add(mul(epsilon,low_weight),mul(ec,low_to_high)),
    independent_fB:add(own_fB,mul(ec,high_fB)),
    physical_Robin_residual:mul(ec,high_rB),
    physical_mean_residual:add(own_rC,mul(ec,high_rC))
  };
  const rounded={
    canonical_stable_high:q(432,125000000),
    complete_nonmean_head:q(3253,1000000000),
    independent_fB:q(4101,1000000000),
    physical_Robin_residual:q(3801,50000000),
    physical_mean_residual:q(50001,1000)
  };
  const waist=q(2693551,10000000000000000000n),amp=q(7,2);
  const waistRounded={
    canonical_stable_high:q(9308,10000000000000000000000n),
    complete_nonmean_head:q(8760,10000000000000000000000n),
    independent_fB:q(11044,10000000000000000000000n),
    physical_Robin_residual:q(20476,1000000000000000000000n),
    physical_mean_residual:q(134678,10000000000000000n)
  };
  const ampRounded={
    canonical_stable_high:q(32578,10000000000000000000000n),
    complete_nonmean_head:q(30659,10000000000000000000000n),
    independent_fB:q(38654,10000000000000000000000n),
    physical_Robin_residual:q(71664,1000000000000000000000n),
    physical_mean_residual:q(471373,10000000000000000n)
  };
  const gates=[],rows={};
  for(const name of Object.keys(exact)){
    const e=exact[name],w=mul(waist,e),a=mul(amp,w);
    gates.push({name:name+'_outer_mean',pass:lt(e,rounded[name])});
    gates.push({name:name+'_waist_before_Gamma',pass:lt(w,waistRounded[name])});
    gates.push({name:name+'_waist_amplitude_before_Gamma',pass:lt(a,ampRounded[name])});
    rows[name]={
      exact_outer_mean_upper:str(e),outward_outer_mean_decimal:decimal(e),
      rounded_outer_mean_upper:str(rounded[name]),
      exact_waist_mean_factor_before_Gamma:str(w),waist_mean_factor_decimal:decimal(w),
      rounded_waist_mean_factor_before_Gamma:str(waistRounded[name]),
      exact_waist_amplitude_factor_before_Gamma:str(a),waist_amplitude_factor_decimal:decimal(a),
      rounded_waist_amplitude_factor_before_Gamma:str(ampRounded[name])
    };
  }
  const mean_coupling=mul(mul(q(49),q(3,100)),q(3686409,5000000000000n));
  const inverse_mean=q(49n*mean_coupling.d,mean_coupling.d-mean_coupling.n);
  gates.push({name:'complete_physical_mean_row_scalar_gap',pass:lt(mean_coupling,q(11,10000000))});
  gates.push({name:'physical_mean_row_inverse_below_50',pass:lt(inverse_mean,q(50))});
  gates.push({name:'physical_mean_fB_column_below_original_outer_budget',pass:lt(mul(inverse_mean,q(819203,10000000000000n)),own_fB)});
  return {
    kind:'actual_final_outer_mean_canonical_ports_and_complete_mean_Schur_rational_budget',
    complete:gates.every(g=>g.pass),executed:true,arithmetic:'normalized exact BigInt rational',
    candidate_sha256:'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413',
    whole_original_eta_interval:true,coordinate:'same moving physical variation h=(delta u,delta v)',
    inputs:[
      {path:'results/R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md',git_blob:'7784d7158974d4632ca634369e55dc095e134902',used:'S.35,S.37,S.38, W>=1/8 and complete low/high/mean/source'},
      {path:'results/R133-supplement-full-scalar-mean-Green-and-residual-sensitive-nu.md',git_blob:'c7454ac2da81690f63ae3a1bbd9aa41643bc0a05',used:'Q.17-Q.23; true scalar mean Green and endpoint factor'},
      {path:'results/R133-supplement-final-waist-amplitude-coordinate-and-mean-Schur.md',git_blob:'511c9ca83972003796c4c4fa456236f32095e3e3',used:'A.13; full amplitude functional norm<7/2, mean retained'},
      {path:'results/R133-supplement-complete-moving-band-and-mean-parameter-Schur.md',git_blob:'a51dbc432d2945bad9a7deb5d985ca021676030b',used:'complete operator and support, no high boundary truncation'}
    ],
    full_mean_outer_gain:rows,gate_count:gates.length,gates,
    physical_mean_scalar_preconditioner:{coupling_upper:str(mean_coupling),inverse_abs_upper:str(inverse_mean),source_and_adjoint_scaling_retained:true},
    independent_fB_norm:'dot H^(2,1/6)',physical_Robin_residual_norm:'H^(1/6)',
    physical_mean_residual_norm:'absolute scalar',head_norm:'all 1<=|j|<=96, ordinary moving L2',
    high_norm:'full same Riccati stable state l2, |j|>=97',
    unknown_Gamma_must_multiply_all_waist_factors:true,Gamma_numerically_certified:false,
    only_homogeneous_outer_contribution_to_waist:true,
    full_body_nonmean_mean_feedback_and_sources_still_retained:true,
    complete_BVP_inverse_proved:false,nu_Schur_nonzero_proved:false
  };
}
const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--out')throw Error('usage: node this.mjs --out NEW_REPORT.json');
const report=calculate();
report.producer_sha256=createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex');
await writeFile(args[1],JSON.stringify(report,null,2)+'\n',{flag:'wx'});
if(!report.complete)process.exitCode=1;
console.log(JSON.stringify({complete:report.complete,gate_count:report.gate_count,out:args[1]}));
