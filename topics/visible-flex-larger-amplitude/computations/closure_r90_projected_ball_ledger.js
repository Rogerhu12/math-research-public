#!/usr/bin/env node
'use strict';
/*
R90: exact BigInt audit of the completed actual low46 physical Green data.
No ODE, no source evaluation, no transcendental approximation, no flint.
Run from topics/visible-flex-larger-amplitude:
 node computations/closure_r90_projected_ball_ledger.js OUTPUT.json
Optional positional overrides follow OUTPUT in the order of INPUTS.
Existing outputs are never overwritten. Every JSON numeric token is
preserved as text before conversion; large dyadic mantissas never pass
through an IEEE-754 number. Decimal displays are not used in gates.
*/
const INPUTS = [
 ['geometry','notes/2026-11-12-closure-physical-green-actions-43303787139-1-interval.json','e3bb0bad3afac3e19d6b811ad068d0b4251b2a1214718dcbd14a2eb98e1aaa03'],
 ['budget','notes/2026-11-12-closure-physical-green-budget-actions-43303787139-1-interval.json','86c9b5604a765a50028865a4f3edae3171d9582052e2b7e7515d0471d8685d45'],
 ['head','notes/2026-11-12-root-r78-true-cut-cauchy-r1.json','9e891098dd625f7418c48d91ee92db900bd7b0d1c44b2b69c1cdebbd8d03c930'],
 ['family','notes/2026-11-12-root-anisotropic-auxiliary-family-r3-summary.json','17b1d776cdce044722db61c2981d64838d18fd66c6ef3fdd4c48fa183a9a3776'],
 ['geometry_terminal','notes/ci-recovery-43303787139-1-interval/whole46-physical-green-geometry-terminal.json','f0e0669bf08d837387e6a7d91c7c3fc527e7ba373ba4b79834156c8237946452'],
 ['budget_terminal','notes/ci-recovery-43303787139-1-interval/whole46-ordered-green-budget-terminal.json','1cf04f4025d49941563d7377d5f95ad4503f5b45e697b1423af30c9cf3e9c72d']
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
function runLedger(texts, hashes, sourceHash, execution) {
 const docs={};
 for(const [key,path,sha] of INPUTS){
  if(hashes[key]!==sha)throw Error('changed frozen input '+key);
  docs[key]=parseExact(texts[key]);
 }
 const {geometry:g,budget:b,head:h,family:f,geometry_terminal:gt,budget_terminal:bt}=docs;
 const gates={};
 function check(name,value){gates[name]=!!value;if(!value)throw Error('gate failed: '+name);}
 check('lossless_integer_parser',parseExact('{"a":123456789012345678901234567890,"b":"x23","c":-2,"d":1.5}') .a==='123456789012345678901234567890');
 check('geometry_and_budget_all_original_gates',g.all_gates===true && b.all_gates===true &&
    Object.values(g.gates).every(x=>x===true) && Object.values(b.gates).every(x=>x===true));
 check('complete_head_and_family_original_gates',h.all_gates===true && f.all_gates===true &&
    Object.values(h.gates).every(x=>x===true) && Object.values(f.gates).every(x=>x===true));
 check('formal_geometry_exit_zero',String(gt.exit_code)==='0'&&gt.signal===null&&String(gt.wait4_status)==='0');
 check('formal_budget_exit_zero',String(bt.exit_code)==='0'&&bt.signal===null&&String(bt.wait4_status)==='0');
 const modes=Array.from({length:46},(_,k)=>String(2*k+2));
 check('all46_modes_retained',JSON.stringify(g.config.modes)===JSON.stringify(modes) &&
    JSON.stringify(b.mode_rows.map(x=>x.mode))===JSON.stringify(modes));
 check('same_geometry_exact_hash',b.geometry_sha256===hashes.geometry &&
    b.geometry_entrypoint_sha256===g.config.entrypoint_sha256);
 check('exact_same20_parameter_axes',
    JSON.stringify(g.config.parameter_axes)===JSON.stringify(h.parameter_axes) &&
    JSON.stringify(g.config.parameter_axes)===JSON.stringify(f.parameter_axes));
 check('all20_actual_axes',f.parameter_axes.length===20 &&
    f.parameter_axes.every((a,i)=>a.mode===String(2*i+2) &&
     point(a.relative_radius).eq(a.mode==='4'?q(1,16):q(1,1024)) &&
     point(a.half_axis).eq(point(a.exact_centre).abs().mul(point(a.relative_radius)))));
 check('real_source_tau_sigma_and_all_positions',g.config.source_tau==='1/64' &&
    g.config.parameter_sigma==='17/16' && String(g.counts.original_material)==='10793' &&
    String(g.counts.taylor)==='10870' && String(g.counts.root_brackets)==='8' &&
    String(b.total_subpanels)==='10878' && g.profile_groups.length===18);
 check('all_two_cell_raw_caps_and_half_slope_bound',g.source_identity.length===2 &&
    g.source_identity.every(x=>x.cap_strictly_inactive===true &&
      x.valley_control_exact_zero===true && x.warp_weight_exact_one===true &&
      x.chi_and_j0_exact_one===true && q(0).lt(upper(x.whole_cell_raw_w_upper)) &&
      upper(x.whole_cell_raw_w_upper).le(q(1,2))));
 check('all46_true_W_and_height_denominators',modes.every(m=>
    nonzero(g.config.true_physical_Wronskians[m])&&nonzero(g.config.actual_true_S0_Q[m])));
 check('actual_outer_heights_retained_and_only_above40_zero',modes.every(m=>
    JSON.stringify(b.mode_rows[Number(m)/2-1].actual_outer_Q)===JSON.stringify(g.config.actual_outer_Q[m]) &&
    (Number(m)<=40 || point(g.config.actual_outer_Q[m]).eq(0))));
 check('same_family_hash_in_true_geometry',g.config.input_hashes[INPUTS[3][1]]===hashes.family);
 const selected=Object.fromEntries(b.densities.map(x=>[x.density,x]));
 for(const name of ['weak_local_rho_16','weak_candidate_cap']){
  const row=selected[name];
  check(name+'_uses_full_weak_source_and_correct_output_weight',
   row.all_input_frequencies_allowed===true && row.definition.source_norm==='W_tau_0' &&
   row.definition.output_angular_factor===true && row.definition.output_envelope==='local_V');
 }
 const sigma=q(17,16),rho=q(64),Rold=upper(g.maximum_mean_input_radius),R=q(4).mul(Rold);
 const ratio=sigma.add(rho).div(sigma.add(16));
 check('entire_rho64_domain_within_four_rho16',ratio.le(4));
 check('whole_position_complete_mean_ball',R.lt(q(1,64)));
 const lead=q(5,4).mul(R).add(q(4).mul(R.pow(2)));
 check('complete_Wiener_leading_inverse',lead.lt(1));
 const eta=q(1,4).mul(q(2).mul(R.div(3).add(q(4).mul(R.pow(2)))).add(
   R.div(3).add(q(4).mul(R.pow(2))).pow(2)).add(q(5,4).mul(R.div(3).pow(2))));
 check('complete_metric_square_root_ball',eta.lt(1));
 const test=q(1,64),den=q(1).sub(q(5,4).mul(test)).sub(q(4).mul(test.pow(2)));
 const sourceConstant=q(23,18).add(q(10).mul(test)).add(q(16).mul(test.pow(2))).div(den);
 const derivConstant=q(23,9).add(q(50).mul(test)).add(q(128).mul(test.pow(2))).div(den)
  .add(test.mul(q(23,18).add(q(10).mul(test)).add(q(16).mul(test.pow(2))))
    .mul(q(5,4).add(q(16).mul(test))).div(den.pow(2)));
 check('full_weak_source_constant_below_three_halves',sourceConstant.lt(q(3,2)));
 check('full_weak_derivative_constant_below_four',derivConstant.lt(4));
 const gamma16=dyad(selected.weak_local_rho_16.all46_sum_of_separate_component_suprema);
 const cap=dyad(selected.weak_candidate_cap.all46_sum_of_separate_component_suprema);
 const gamma=q(8).mul(gamma16);
 const LR=dyad(b.all20_linear_centre_local_norm);
 const candidate=dyad(b.crude_complete_candidate_local_strong_norm);
 check('candidate_separate_sup_has_full40_components',candidate.eq(q(40).mul(sigma)));
 const hop=dyad(b.head_weighted_l1_trace_to_local_field_operator);
 const beta=upper(h.complete_coarse_trace_rows.outer.all46_low_nonlinear_K.uniform_value_upper);
 const bh=hop.mul(beta),zero=LR.add(candidate).add(bh).add(cap);
 const image=zero.add(rho.mul(gamma));
 check('strict_full46_projected_contraction',gamma.lt(1));
 check('strict_full46_projected_selfmap',image.lt(rho));
 check('display_contraction_less_one_hundredth',gamma.lt(q(1,100)));
 check('display_full_image_less_52',image.lt(52));
 check('no_finite_Robin_head_replacement',
   g.gates.true_low46_head_slopes_no_finite_Robin_replacement===true &&
   h.gates.complete_auxiliary_far_explicitly_added===true &&
   h.gates.separate_complete_full_frequency_minus_auxiliary_added===true);
 const modeRows=b.mode_rows.map(x=>{
  const w=x.densities.find(v=>v.density==='weak_local_rho_16');
  const c=x.densities.find(v=>v.density==='weak_candidate_cap');
  return {mode:x.mode,weak16_row:r(dyad(w.strong_output_row_sum)),
   rho64_derivative_row:r(q(8).mul(dyad(w.strong_output_row_sum))),
   candidate_source_row:r(dyad(c.strong_output_row_sum)),
   linear_field_row:r(dyad(x.absolute_linear_centre_physical_norm)),
   head_trace_operator_row:r(dyad(x.complete_weighted_inner_K_trace_to_field_norm))};
 });
 // Aggregates were rounded after summing unrounded per-mode entries.
 // They need not dominate a new sum of individually rounded entries.
 const aggregateConsistency={
  rounded_mode_derivative_sum:r(addall(modeRows.map(x=>q(x.rho64_derivative_row.numerator,x.rho64_derivative_row.denominator)))),
  original_aggregate_is_used_without_replacing_by_sum_of_rounded_rows:true
 };
 return {
  status:'Complete exact R90 audit: actual full46 projected whole-field ball; cut consistency and high PDE unpaid',
  author:'exact_closure, GPT-6 Astra Pro, AI-assisted, 2026-11-12',
  execution,source_sha256:sourceHash,
  input_hashes:Object.fromEntries(INPUTS.map(([key,path,sha])=>[path,sha])),
  all_gates:Object.values(gates).every(x=>x),gates,
  parameter_domain:'entire real R74 twenty-axis box; holomorphic extension inside same complex polydisc',
  rho:r(rho),sigma:r(sigma),source_tau:r(q(1,64)),
  rho64_over_rho16: r(ratio),
  old_all_nine_domain_upper:r(Rold),new_whole_position_domain_upper:r(R),
  leading_perturbation_upper:r(lead),metric_square_root_perturbation_upper:r(eta),
  complete_source_coefficient_at_one_over64:r(sourceConstant),
  complete_derivative_coefficient_at_one_over64:r(derivConstant),
  density_comparison_factor:r(8),weak16_full46_green:r(gamma16),
  rho64_full46_green:r(gamma),full_family_candidate_source:r(cap),
  all20_fixed_outer_linear_field:r(LR),full40_component_candidate_norm:r(candidate),
  full46_true_head_trace_value:r(beta),head_to_field_operator:r(hop),
  full46_complete_true_head_field:r(bh),zero_field_map_upper:r(zero),
  full_ball_image_upper:r(image),strict_selfmap_slack:r(rho.sub(image)),
  uniform_solution_relative_norm_upper:r(zero.div(q(1).sub(gamma))),
  mode_rows:modeRows,aggregate_rounding:aggregateConsistency,
  scope:{
   actual_same_two_cells:true,all46_nonmean_projected_equations:true,
   full_algebraic_mean_root_and_exact_leading_inverse:true,
   true_inner_nonlinear_low46_boundary_prescribed_as_beta_of_parameter:true,
   fixed_all20_actual_outer_heights:true,
   independent_mean_height_constraint_added:false,
   all46_inner_cut_height_consistency_paid:false,
   actual_high_head_trace_matched:false,full_high_PDE_paid:false,
   complete_Darboux_or_closed_surface_claimed:false
  },
  formal_computation_evidence:{geometry:gt,budget:bt},
  no_new_Arb_ODE_or_source_integrals:true
 };
}
if(typeof module!=='undefined')module.exports={runLedger,parseExact,INPUTS};
if(typeof require!=='undefined' && require.main===module){
 const fs=require('node:fs'),crypto=require('node:crypto');
 const argv=process.argv.slice(2),out=argv.shift();
 if(!out)throw Error('Usage: node closure_r90_projected_ball_ledger.js OUTPUT.json [six input paths]');
 const texts={},hashes={};
 INPUTS.forEach(([key,path],i)=>{const raw=fs.readFileSync(argv[i]||path);texts[key]=raw.toString('utf8');hashes[key]=crypto.createHash('sha256').update(raw).digest('hex');});
 const sh=crypto.createHash('sha256').update(fs.readFileSync(__filename)).digest('hex');
 const result=runLedger(texts,hashes,sh,{engine:'Node.js BigInt',version:process.version,new_numerical_flow:false});
 fs.writeFileSync(out,JSON.stringify(result,null,2)+'\n',{flag:'wx'});
 process.stdout.write(JSON.stringify({all_gates:result.all_gates,output:out,gates:Object.keys(result.gates).length})+'\n');
}
