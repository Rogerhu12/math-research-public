#!/usr/bin/env node
'use strict';
/* R93: exact positive-prefix reconstruction and actual high inverse at 5760.
   NEW source. The existing R68/R78/R91 data and all real frames stay fixed.
   BigInt rationals only. A replay CLI is provided; execution provenance is
   recorded by the actual caller, never inferred from this file's existence. */
const INPUTS=[
 ['frame','notes/2026-11-12-root-outer-continuous-frame-r1.json','d47f1507427d75c9e94452296cf4e5706e1b3468135d44b486845b1c212f70fe'],
 ['frame_source','computations/root_outer_frame_continuous_prefix.py','828ea557a5f9b702658eed425cc6344128d7e4be4a13a3efefc1d25b6c302fe5'],
 ['head','notes/2026-11-12-root-r78-true-cut-cauchy-r1.json','9e891098dd625f7418c48d91ee92db900bd7b0d1c44b2b69c1cdebbd8d03c930'],
 ['r91','notes/2026-11-12-closure-r91-split-jump-high-exact-ledger.json','badc734ef590c747d62fc75bd57ce2571bd89e8c522604b691406f469d47392f']
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

function ceilGrid128(x){
 x=q(x);if(x.a<0n)throw Error('positive log grid');
 return q((x.a*(1n<<128n)+x.b-1n)/x.b,1n<<128n);
}
function originalSeriesLogUpper(x){
 x=q(x);if(x.lt(1)||q(2).lt(x))throw Error('original log normalization');
 const z=x.sub(1).div(x.add(1)),zz=z.mul(z);
 let power=z,result=q(0);
 for(let k=0;k<8;k++){result=result.add(power.div(2*k+1));power=power.mul(zz);}
 return ceilGrid128(result.add(power.div(q(17).mul(q(1).sub(zz)))).mul(2));
}
const ORIGINAL_LOG2=originalSeriesLogUpper(q(2));
function originalLogUpper(x){
 x=q(x);if(x.lt(1))throw Error('original positive log branch');
 let k=x.a.toString(2).length-x.b.toString(2).length,P=p2(k);
 if(x.lt(P)){k--;P=P.div(2);}
 const normalized=x.div(P);
 if(k<0||normalized.lt(1)||!normalized.lt(2))throw Error('original binary range');
 return ceilGrid128(ORIGINAL_LOG2.mul(k).add(originalSeriesLogUpper(normalized)));
}
function fromRecord(x){return q(x.numerator,x.denominator);}
function runExact5760(texts,hashes,sourceSha,execution){
 const docs={},gates={};
 function ck(k,v){gates[k]=!!v;if(!v)throw Error('Unpaid R93 gate: '+k);}
 for(const [key,path,expected] of INPUTS){
  if(hashes[key]!==expected)throw Error('Frozen input '+key);
  docs[key]=key==='frame_source'?texts[key]:parseExact(texts[key]);
 }
 const f=docs.frame,h=docs.head,l=docs.r91,last=f.rows[f.rows.length-1];
 ck('R91_full28_actual_gates',l.all_gates===true&&Object.keys(l.gates).length===28&&Object.values(l.gates).every(x=>x===true));
 ck('R78_full_actual_head_gates',h.all_gates===true&&Object.values(h.gates).every(x=>x===true));
 ck('R68_complete_original_frame_identity',f.panels==='10793'&&f.atanh_terms==='8'&&f.log_grid_bits==='128'&&Object.values(f.gates).every(x=>x===true));
 ck('same_R91_frame_head_and_source_identity',l.input_hashes[INPUTS[0][1]]===hashes.frame&&l.input_hashes[INPUTS[1][1]]===hashes.frame_source&&l.input_hashes[INPUTS[2][1]]===hashes.head);
 ck('exact_frozen_log2_reproduced',ORIGINAL_LOG2.eq(endpoint(f.log2_upper)));
 const source=texts.frame_source;
 ck('positive_sums_and_endpoint_formula_retained',
  source.includes('positive_forward+=max(Q(0),nf,jf)')&&
  source.includes('positive_inverse+=max(Q(0),ni,ji)')&&
  source.includes('all_position_pairs_forward_log_prefactor=record(positive_forward+global_endpoint_cost)')&&
  source.includes('all_position_pairs_inverse_log_prefactor=record(positive_inverse+global_endpoint_cost)'));
 const bmin=endpoint(last.minimum_frame),bmax=endpoint(last.maximum_frame);
 ck('same_actual_frame_conversions',bmin.eq(p2(-8))&&bmax.lt(18554)&&q(1).lt(bmax));
 const endpointCost=originalLogUpper(q(1).div(bmin)).add(originalLogUpper(bmax));
 const plus=endpoint(last.all_position_pairs_forward_log_prefactor).sub(endpointCost);
 const minus=endpoint(last.all_position_pairs_inverse_log_prefactor).sub(endpointCost);
 ck('exact_positive_totals_recovered',q(0).lt(plus)&&q(0).lt(minus)&&plus.lt(266)&&minus.lt(274));
 const phase=endpoint(last.exact_sum_of_certified_panel_phases);
 ck('actual_phase_uses_exact_same10793_bounds',last.cumulative_panels==='10793'&&q(0).lt(phase)&&phase.lt(q(21,256)));
 const epsilon=p2(-25),N=q(10793),error=N.mul(epsilon);
 const M=5760,kappa=p2(-18),tau=q(18,125),tauOut=q(1,64);
 ck('uniform_jump_error_inherited_from_all_real_ratios',fromRecord(l.uniform_jump_error_upper).lt(epsilon)&&fromRecord(l.total_jump_error_upper).eq(error));
 const cost=phase.add(plus.add(error).div(M)).add(kappa.mul(plus.add(minus)));
 const stripSlack=tau.sub(tauOut).sub(cost);
 ck('actual_split_strip_has_positive_margin',q(0).lt(stripSlack));
 const availableHeadGap=fromRecord(l.tau_initial);
 ck('same_initial_strip_identity',tau.eq(availableHeadGap));
 const G=q(M+1,M).div(kappa);
 ck('exact_source_inverse',G.eq(q(11798528,45))&&G.lt(p2(19)));
 const A=p2(-34),contraction=G.mul(4).mul(257).mul(A);
 ck('complete_mean_source_feedback_below_one60',contraction.lt(q(1,60)));
 const C=fromRecord(l.actual_low_complete_wide),V0=p2(-40),local=C.div(V0);
 ck('actual_R74_low_centre_wide_domain',C.lt(A)&&local.lt(12));
 const bands=h.complete_coarse_trace_rows.head.high_bands_value_upper;
 const rest=upper(bands[1]),infinite=upper(bands[2]),Hbd=q(256).mul(rest.add(infinite));
 ck('both_true_rest_and_infinite_initial_traces_retained',q(0).lt(rest)&&q(0).lt(infinite)&&Hbd.lt(p2(-152)));
 let kmin=0;while(184+kmin*92<M)kmin++;
 ck('exact_finite_centre_support_tail_index',kmin===61&&184+60*92<M&&184+61*92>=M);
 const ell=q(5,4).mul(A).add(q(4).mul(A.pow(2)));
 ck('full_mean_inverse_geometric_ratio',ell.lt(p2(-33)));
 const pure=q(256).mul(q(3,2)).mul(A.pow(2)).mul(p2(-33).pow(kmin));
 const pureField=G.mul(pure);
 ck('pure_complete_high_source',pure.lt(p2(-2072)));
 ck('pure_complete_high_field',pureField.lt(p2(-2053)));
 const rm=p2(-43),rh=p2(-149).add(rm.div(50));
 const domain=C.add(rm).add(q(18555).mul(rh));
 ck('same_actual_frame_physical_sum_of_sup_conversion',q(1).add(bmax).lt(18555)&&q(1).div(bmin).add(1).le(257));
 ck('complete_low_middle_high_mean_domain',domain.lt(A)&&A.lt(q(1,64)));
 const image=Hbd.add(pureField).add(contraction.mul(rm.add(rh)));
 const simpleImage=p2(-152).add(p2(-2053)).add(rm.add(rh).div(60));
 ck('actual_high_ball_selfmap',image.lt(rh));
 ck('simple_display_high_ball_selfmap',simpleImage.lt(rh));
 ck('declared_middle_and_high_ranges_are_disjoint',M%2===0&&(M-2)===5758);
 return {
  status:'Complete exact R93 5760-plus source inverse and conditional high response',
  author:'exact_closure (GPT-6 Astra Pro, AI-assisted)',execution,source_sha256:sourceSha,
  input_hashes:Object.fromEntries(INPUTS.map(([key,path])=>[path,hashes[key]])),
  all_gates:Object.values(gates).every(Boolean),gates,
  actual_original_panel_count:10793,
  source_interval_minimum_high_mode:M,
  exact_original_log2:r(ORIGINAL_LOG2),
  exact_physical_endpoint_cost_removed_from_strip_only:r(endpointCost),
  exact_positive_forward_total:r(plus),exact_positive_inverse_total:r(minus),
  exact_actual_phase_total:r(phase),complete_jump_error:r(error),
  kappa:r(kappa),tau_initial:r(tau),tau_final_lower:r(tau.sub(cost)),
  total_strip_cost:r(cost),strict_final_strip_margin:r(stripSlack),
  source_inverse:r(G),full_mean_feedback:r(contraction),
  actual_low_centre_constant_strip_physical_norm:r(C),
  actual_low_centre_same_V_norm:r(local),
  actual_head_rest_input:r(rest),actual_head_infinite_input:r(infinite),
  true_balanced_high_initial_lift:r(Hbd),finite_centre_first_possible_high_term:kmin,
  full_inverse_ratio_upper:r(ell),pure_high_source:r(pure),pure_high_field:r(pureField),
  middle_radius:r(rm),balanced_high_radius:r(rh),complete_physical_work_domain:r(domain),
  high_block_image:r(image),simple_image:r(simpleImage),strict_image_slack:r(rh.sub(image)),
  saved_even_middle_modes_relative_to_R91:(8192-M)/2,
  remaining_even_middle_modes:(M-94)/2,
  scope:{
   original_R74_parameter_domain_only:true,
   new_R92_transverse_domain_claimed:false,
   same_real_background_and_frame_data:true,
   fixed_given_middle_94_to5758:true,
   complete_middle_equations_solved:false,
   full_low_middle_high_joint_fixed_point_paid:false,
   all46_cut_consistency_paid:false,
   outer0_to9_or_closed_family_claimed:false
  },
  no_new_source_ODE_Arb_or_transcendental_library:true
 };
}
if(typeof module!=='undefined')module.exports={runExact5760};
if(typeof require!=='undefined'&&require.main===module){
 const fs=require('node:fs'),crypto=require('node:crypto'),argv=process.argv.slice(2),out=argv.shift();
 if(!out)throw Error('Usage: node closure_r93_actual_positive_prefix_high_ledger.js OUTPUT.json [four input paths]');
 const texts={},hashes={};
 INPUTS.forEach(([key,path],i)=>{const raw=fs.readFileSync(argv[i]||path);texts[key]=raw.toString('utf8');hashes[key]=crypto.createHash('sha256').update(raw).digest('hex');});
 const sourceSha=crypto.createHash('sha256').update(fs.readFileSync(__filename)).digest('hex');
 const result=runExact5760(texts,hashes,sourceSha,{engine:'Node.js BigInt',version:process.version});
 fs.writeFileSync(out,JSON.stringify(result,null,2)+'\n',{flag:'wx'});
 process.stdout.write(JSON.stringify({all_gates:result.all_gates,gates:Object.keys(result.gates).length,output:out})+'\n');
}
