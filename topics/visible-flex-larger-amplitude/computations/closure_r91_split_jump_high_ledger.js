#!/usr/bin/env node
'use strict';
/*
R91 exact recovered strip/actual-centre audit. Only BigInt rational
operations and a proved positive Taylor remainder for exp are used.
Every JSON numeric token is parsed losslessly. Existing outputs are
never overwritten. Optional input overrides follow OUTPUT in INPUTS order.
No new source evaluation, ODE, interval library, Node worker or CI run is
claimed by the orchestration-runtime execution recorded in the primary.
*/
const INPUTS=[
  [
    "frame",
    "notes/2026-11-12-root-outer-continuous-frame-r1.json",
    "d47f1507427d75c9e94452296cf4e5706e1b3468135d44b486845b1c212f70fe"
  ],
  [
    "frame_base",
    "notes/2026-11-12-root-outer-optimal-frame-r1.json",
    "e726b2006b27c84ac61d73e0d899d504da7997fd7c3775c7ca3b35e175261751"
  ],
  [
    "frame_source",
    "computations/root_outer_frame_continuous_prefix.py",
    "828ea557a5f9b702658eed425cc6344128d7e4be4a13a3efefc1d25b6c302fe5"
  ],
  [
    "head",
    "notes/2026-11-12-root-r78-true-cut-cauchy-r1.json",
    "9e891098dd625f7418c48d91ee92db900bd7b0d1c44b2b69c1cdebbd8d03c930"
  ],
  [
    "budget",
    "notes/2026-11-12-closure-physical-green-budget-actions-43303787139-1-interval.json",
    "86c9b5604a765a50028865a4f3edae3171d9582052e2b7e7515d0471d8685d45"
  ],
  [
    "geometry",
    "notes/2026-11-12-closure-physical-green-actions-43303787139-1-interval.json",
    "e3bb0bad3afac3e19d6b811ad068d0b4251b2a1214718dcbd14a2eb98e1aaa03"
  ],
  [
    "r90",
    "notes/2026-11-12-closure-r90-projected-ball-exact-ledger.json",
    "fcf7c26d57cfe443fb227a62c95df30c1a3b6f1dff7ec5fa90673ad0903b0815"
  ]
];
function parseExact(s) {
 return JSON.parse(s.replace(/"(?:\\.|[^"\\])*"|-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?/g,
  t => t[0] === '"' ? t : '"'+t+'"'));
}
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;}
class Q {
 constructor(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error('zero denominator');if(b<0n){a=-a;b=-b;}const g=gcd(a,b);this.a=a/g;this.b=b/g;}
 add(x){x=q(x);return new Q(this.a*x.b+x.a*this.b,this.b*x.b);}
 neg(){return new Q(-this.a,this.b);}
 sub(x){return this.add(q(x).neg());}
 mul(x){x=q(x);return new Q(this.a*x.a,this.b*x.b);}
 div(x){x=q(x);return new Q(this.a*x.b,this.b*x.a);}
 pow(n){return n<0?new Q(this.b,this.a).pow(-n):new Q(this.a**BigInt(n),this.b**BigInt(n));}
 le(x){x=q(x);return this.a*x.b<=x.a*this.b;}
 lt(x){x=q(x);return this.a*x.b<x.a*this.b;}
 eq(x){x=q(x);return this.a===x.a && this.b===x.b;}
 abs(){return this.a<0n?this.neg():this;}
 record(){return {numerator:String(this.a),denominator:String(this.b)};}
}
function q(a,b){return a instanceof Q?a:new Q(a,b);}
function p2(n){n=Number(n);if(!Number.isSafeInteger(n))throw Error('bad exponent');return n>=0?q(1n<<BigInt(n)):q(1n,1n<<BigInt(-n));}
function dyad(x){return q(x[0]).mul(p2(x[1]));}
function endpoint(x){return q(x.mantissa).mul(p2(x.binary_exponent));}
function upper(x){return endpoint(x.upper);}
function lower(x){return endpoint(x.lower);}
function point(x){const a=lower(x),b=upper(x);if(!a.eq(b))throw Error('expected exact point');return a;}
function addall(xs){return xs.reduce((a,b)=>a.add(b),q(0));}
function maxall(xs){if(!xs.length)throw Error('empty maximum');return xs.reduce((a,b)=>a.lt(b)?b:a);}
function nonzero(x){return upper(x).lt(0)||q(0).lt(lower(x));}
function ceilDecimal(x,digits=28){
 x=q(x);if(x.a<0n)throw Error('positive display only');
 const scale=10n**BigInt(digits),n=(x.a*scale+x.b-1n)/x.b;
 const s=String(n).padStart(digits+1,'0');
 return s.slice(0,-digits)+'.'+s.slice(-digits);
}
function r(x){x=q(x);return {...x.record(),decimal_upward_display:ceilDecimal(x)};}


function dyadicUp(x,bits=96){
 x=q(x);if(x.a<0n)throw Error('nonnegative only');if(!x.a)return q(0);
 const na=x.a.toString(2).length,nb=x.b.toString(2).length;
 let e=na-nb-bits+1,t=x.div(p2(e)),m=(t.a+t.b-1n)/t.b;
 return q(m).mul(p2(e));
}
function expUpper(x,terms=96){
 x=q(x);if(x.a<0n)throw Error('nonnegative exponent required');
 let term=q(1),sum=q(1);
 for(let k=1;k<=terms;k++){term=term.mul(x).div(k);sum=sum.add(term);}
 const next=term.mul(x).div(terms+1),ratio=x.div(terms+2);
 if(!ratio.lt(1))throw Error('Taylor tail geometric ratio unpaid');
 return dyadicUp(sum.add(next.div(q(1).sub(ratio))));
}
function runHighLedger(texts,hashes,sourceHash,execution){
 const docs={},gates={};
 function ck(n,b){gates[n]=!!b;if(!b)throw Error(n);}
 for(const [key,path,sha] of INPUTS){if(hashes[key]!==sha)throw Error('frozen hash '+key);docs[key]=key==='frame_source'?texts[key]:parseExact(texts[key]);}
 const {frame:f,head:h,budget:b,geometry:g,r90:l}=docs;
 ck('original_R68_complete_real_source',Object.values(f.gates).every(x=>x===true)&&f.panels==='10793'&&f.atanh_terms==='8'&&f.log_grid_bits==='128');
 ck('R90_all28_original_gates',l.all_gates===true&&Object.keys(l.gates).length===28&&Object.values(l.gates).every(x=>x===true));
 ck('same_full46_geometry_budget_and_head_hashes',
  l.input_hashes[INPUTS.find(x=>x[0]==='geometry')[1]]===hashes.geometry &&
  l.input_hashes[INPUTS.find(x=>x[0]==='budget')[1]]===hashes.budget &&
  l.input_hashes[INPUTS.find(x=>x[0]==='head')[1]]===hashes.head);
 const last=f.rows[f.rows.length-1],blo=endpoint(last.minimum_frame),bhi=endpoint(last.maximum_frame);
 const phase=endpoint(last.exact_sum_of_certified_panel_phases);
 const pplus=endpoint(last.all_position_pairs_forward_log_prefactor);
 const pminus=endpoint(last.all_position_pairs_inverse_log_prefactor);
 ck('both_endpoint_frame_conversions_retained_in_parent_bounds',blo.eq(p2(-8))&&bhi.lt(18554));
 ck('every_actual_frame_ratio_below_two23',bhi.div(blo).lt(p2(23)));
 ck('actual_phase_and_two_positive_budget_totals',phase.lt(q(21,256))&&pplus.lt(282)&&pminus.lt(289));
 const N=q(10793),epsilon=p2(-25),M=q(8192),kappa=q(21).mul(p2(-20)),Rstar=p2(-34);
 const logTail=q(2).div(q(17).mul(q(3).pow(17)).mul(q(1).sub(q(1,9))));
 const Jerror=q(24).mul(logTail.add(p2(-128)));
 ck('uniform_complete_original_log_error',Jerror.lt(epsilon));
 ck('all10793_jump_errors',N.mul(epsilon).lt(q(1,2048)));
 const cost=q(21,256).add(q(282).add(q(1,2048)).div(M)).add(kappa.mul(571));
 const tau=q(18,125),tauOut=q(1,64),margin=tau.sub(tauOut).sub(cost);
 ck('new_strip_stays_strictly_above_one64',q(0).lt(margin));
 const trueHeadTau=upper(docs.frame_base.true_available_strip_gap).add(q(1,64));
 ck('new_input_strip_is_narrower_than_actual_head',tau.lt(trueHeadTau));
 const G=q(1).add(q(1).div(M)).div(kappa),lambda=G.mul(4).mul(257).mul(Rstar);
 ck('complete_source_inverse_below50000',G.lt(50000));
 ck('complete_high_feedback_below_one300',lambda.lt(q(1,300)));
 const Ds=Object.fromEntries(b.densities.map(v=>[v.density,v]));
 const gam16=dyad(Ds.weak_local_rho_16.all46_sum_of_separate_component_suprema);
 const cap=dyad(Ds.weak_candidate_cap.all46_sum_of_separate_component_suprema);
 const LR=dyad(b.all20_linear_centre_local_norm),hop=dyad(b.head_weighted_l1_trace_to_local_field_operator);
 const beta=upper(h.complete_coarse_trace_rows.outer.all46_low_nonlinear_K.uniform_value_upper);
 const betaWide=upper(h.complete_coarse_trace_rows.head.all46_low_nonlinear_K.uniform_value_upper);
 const sigma=q(17,16),V0=dyad(g.config.uniform_envelope),rho=q(9),factor=q(108);
 ck('same_exact_point_envelope',V0.eq(p2(-40))&&g.config.source_tau==='1/64');
 ck('full_candidate_cap_comparison_for_absolute_nine',q(3,2).mul(rho.pow(2)).div(sigma.pow(2)).le(factor));
 ck('full_derivative_comparison_for_absolute_nine',rho.le(sigma.add(16)));
 ck('absolute_nine_complete_mean_and_inverse_domain',rho.mul(V0).lt(q(1,64))&&
 q(5,4).mul(rho.mul(V0)).add(q(4).mul(rho.mul(V0).pow(2))).lt(1));
 const absImage=LR.add(hop.mul(beta)).add(factor.mul(cap));
 ck('absolute_nine_entire_ball_selfmap',absImage.lt(rho));
 ck('absolute_nine_contraction',gam16.mul(2).lt(1));
 ck('same_R90_solution_by_old_ball_inclusion',rho.add(q(40).mul(sigma)).lt(64));
 const delta=tau.sub(tauOut),rows=[];
 let wideL=q(0),wideN=q(0);
 ck('all46_output_rows_retained',b.mode_rows.length===46&&b.mode_rows.every((x,i)=>x.mode===String(2*i+2)));
 for(const row of b.mode_rows){
  const m=Number(row.mode),e=expUpper(delta.mul(m));
  const cr=dyad(row.densities.find(x=>x.density==='weak_candidate_cap').strong_output_row_sum);
  const lr=dyad(row.absolute_linear_centre_physical_norm);
  const wl=V0.mul(e).mul(lr),wn=V0.mul(e).mul(cr).mul(factor);
  wideL=wideL.add(wl);wideN=wideN.add(wn);
  rows.push({mode:m,exp_upper:r(e),linear_wide:r(wl),source_wide:r(wn)});
 }
 const wideHead=V0.mul(hop).mul(betaWide),Cwide=wideL.add(wideN).add(wideHead);
 ck('actual_all46_projected_solution_in_constant_wide_strip',Cwide.lt(Rstar));
 const Hwide=upper(h.complete_coarse_trace_rows.head.high_bands_value_upper[2]);
 const Hbd=q(256).mul(Hwide);
 ck('nonzero_true_R74_high_initial_trace',Hbd.lt(p2(-181)));
 const kmin=88;
 ck('finite_centre_support_requires_at_least88_inverse_terms',q(184+92*87).lt(M));
 const lead=q(5,4).mul(Rstar).add(q(4).mul(Rstar.pow(2)));
 ck('complete_inverse_neumann_factor',lead.lt(p2(-33)));
 const pureSource=q(256).mul(q(3,2)).mul(Rstar.pow(2)).mul(p2(-33*kmin));
 const pureImage=G.mul(pureSource);
 ck('finite_centre_pure_high_source_below_two2963',pureSource.lt(p2(-2963)));
 ck('finite_centre_pure_high_image_below_two2947',pureImage.lt(p2(-2947)));
 const middle=p2(-41),high=p2(-179).add(middle.div(250));
 const completeDomain=Cwide.add(middle).add(q(18555).mul(high));
 ck('actual_low_centre_plus_declared_middle_high_domain',completeDomain.lt(Rstar));
 const highImage=Hbd.add(pureImage).add(middle.add(high).div(300));
 ck('strict_high_block_selfmap_for_all_declared_middle',highImage.lt(high));
 return {
 status:'Complete exact R91 actual split-jump high inverse, actual low-centre wide-strip bridge, conditional middle/high response',
 author:'exact_closure, GPT-6 Astra Pro, AI-assisted, 2026-11-12',execution,source_sha256:sourceHash,
 input_hashes:Object.fromEntries(INPUTS.map(([key,path,sha])=>[path,sha])),
 all_gates:Object.values(gates).every(x=>x),gates,
 minimum_high_mode:r(M),kappa:r(kappa),tau_initial:r(tau),tau_final_lower:r(tau.sub(cost)),
 total_strip_cost_upper:r(cost),strict_final_strip_margin_above_one64:r(margin),
 uniform_jump_error_upper:r(Jerror),chosen_jump_error:r(epsilon),
 total_jump_error_upper:r(N.mul(epsilon)),single_series_log_tail:r(logTail),
 inverse_source_operator:r(G),full_high_feedback:r(lambda),
 complete_work_domain:r(Rstar),actual_frame_min:r(blo),actual_frame_max:r(bhi),
 absolute_low_field_radius:r(rho),absolute_low_field_image:r(absImage),
 absolute_low_field_contraction:r(gam16.mul(2)),pure_source_scale_factor:r(factor),
 actual_low_wide_strip:r(tau),actual_low_linear_wide:r(wideL),
 actual_low_source_wide:r(wideN),actual_low_true_head_wide:r(wideHead),
 actual_low_complete_wide:r(Cwide),low_mode_rows:rows,
 true_high_initial_lift:r(Hbd),minimum_neumann_index:kmin,
 pure_high_source:r(pureSource),pure_high_field:r(pureImage),
 declared_middle_radius:r(middle),declared_high_radius:r(high),
 complete_low_middle_high_domain:r(completeDomain),high_block_image:r(highImage),
 strict_high_block_slack:r(high.sub(highImage)),
 claims:{low_centre_in_new_strip_paid:true,modes8192_and_above_complete_source_inverse_paid:true,
  true_high_initial_trace_retained:true,full_algebraic_mean_and_inverse:true,
  middle94_to8190_actual_solution_paid:false,low_to_high_and_high_to_low_joint_fixed_point_paid:false,
  low_cut_consistency_paid:false,outer_cells0_to9_paid:false,closed_surface_claimed:false},
 no_new_source_ODE_Arb_or_transcendental_library:true
 };
}

if(typeof module!=='undefined')module.exports={runHighLedger};
if(typeof require!=='undefined'&&require.main===module){
 const fs=require('node:fs'),crypto=require('node:crypto'),argv=process.argv.slice(2),out=argv.shift();
 if(!out)throw Error('Usage: node closure_r91_split_jump_high_ledger.js OUTPUT.json [seven input paths]');
 const texts={},hashes={};
 INPUTS.forEach(([key,path],i)=>{const raw=fs.readFileSync(argv[i]||path);texts[key]=raw.toString('utf8');hashes[key]=crypto.createHash('sha256').update(raw).digest('hex');});
 const sh=crypto.createHash('sha256').update(fs.readFileSync(__filename)).digest('hex');
 const result=runHighLedger(texts,hashes,sh,{engine:'Node.js BigInt',version:process.version});
 fs.writeFileSync(out,JSON.stringify(result,null,2)+'\n',{flag:'wx'});
 process.stdout.write(JSON.stringify({all_gates:result.all_gates,gates:Object.keys(result.gates).length,output:out})+'\n');
}
