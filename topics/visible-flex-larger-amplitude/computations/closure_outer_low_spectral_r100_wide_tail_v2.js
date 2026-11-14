#!/usr/bin/env node
'use strict';
/* Prepared R100 grouped-domain continuation: consume one whole spectral primary.
   The tail arithmetic is unchanged from executed original-domain R96.
   It applies only after a fresh R100 source reweight and all30 spectral gates.
   The old R97 entries and results stay unchanged. No split-data API transfer.
   Prepared during executor unavailability; no numerical execution claimed. */
const EXPECTED_SPECTRAL_SOURCE='eac90d6f7c816a67590c2c07d031e24d27af0adfd21e1b5ef5411891943b903e';
const BASE_INPUTS=[
  [
    "r91",
    "notes/2026-11-12-closure-r91-split-jump-high-exact-ledger.json",
    "badc734ef590c747d62fc75bd57ce2571bd89e8c522604b691406f469d47392f"
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
    "geometry_source",
    "computations/closure_outer_physical_green_geometry_recovered_v2.py",
    "c48606c4e127fb0d3f27479eeed11bff3c5cb69139148633ea4f74a9e1f63829"
  ],
  [
    "head",
    "notes/2026-11-13-root-r100-complete-source-reweight-r1.json",
    null
  ],
  [
    "r94",
    "notes/2026-11-12-root-r94-full46-cut-exact-ledger.json",
    "5eb45673a9080ae251e77c3203cfc2142ba31850fc244c7e2c8500df774249bc"
  ],
  [
    "head_source",
    "computations/root_hybrid46_complete_source_reweight.py",
    "58e0d7750faa1e9d58458f238c93f7c6cab3803cef3b776c2f01b494287bb5c1"
  ],
  [
    "family",
    "notes/2026-11-12-root-anisotropic-auxiliary-family-r3-summary.json",
    "17b1d776cdce044722db61c2981d64838d18fd66c6ef3fdd4c48fa183a9a3776"
  ],
  [
    "r100",
    "notes/2026-11-13-root-r100-hybrid46-exact-ledger.json",
    "7e6b3c140c57df34ab10f17facbc624104b39fa9870a4eecfcce06bf3ea62ca9"
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


function up(x){return dyadicUp(x,128);}
function cd(x){x=q(x);if(x.b&(x.b-1n))throw Error('not dyadic');return[String(x.a),1-x.b.toString(2).length];}
function numGuard(x){if(typeof x==='number'&&(!Number.isSafeInteger(x)||Math.abs(x)>1e8))throw Error('Unsafe JSON number');if(x&&typeof x==='object')for(const v of Object.values(x))numGuard(v);}
function runWideTailFull(primaryText,sourceSha,execution,hashText,expectedPrimarySha){
 const primarySha=hashText(primaryText);
 if(primarySha!==expectedPrimarySha)throw Error('The complete primary hash differs');
 const p=JSON.parse(primaryText);numGuard(p);
 const rows=p.middle_complete_sources,gates={};
 function ck(k,v){gates[k]=!!v;if(!v)throw Error('Unpaid weighted-tail gate: '+k);}
 ck('fresh_complete30_gates',p.all_gates===true&&Object.keys(p.gates).length===30&&Object.values(p.gates).every(Boolean));
 ck('same_executed_spectral_source',p.source_sha256===EXPECTED_SPECTRAL_SOURCE);
 ck('all_original_pinned_inputs',BASE_INPUTS.every(([key,path,sha])=>key==='head'?p.input_hashes[path]===p.complete_R100_primary_sha256:p.input_hashes[path]===sha));
 ck('new_R100_grouped_real_domain_retained',
  p.schema==='visible-flex-larger-R100-low46-spectral-enclosure-v2'&&
  p.parameter_domain==='Real restriction of R100 six original R74 axes times40 original R59 weighted-l1 axes; same fixed R74 outer targets'&&
  p.parameter_norm==='max(linf_S,weighted_l1_T)'&&p.scope.new_R100_grouped_domain===true&&
  p.scope.old_R92_domain_claimed===false);
 ck('all230_source_rows_preserved',
  Array.isArray(rows)&&rows.length===230&&rows.every((x,i)=>x.mode===94+2*i)&&
  Array.isArray(p.low_complete_sources)&&p.low_complete_sources.length===46&&
  p.low_complete_sources.every((x,i)=>x.mode===2*i+2));
 ck('one_complete_primary_hash_checked',primarySha===expectedPrimarySha);
 const caps=p.final_caps.map(v=>({mode:v.mode,bound:dyad(v.bound)})),V0=p2(-40),A=addall(caps.map(x=>x.bound));
 ck('same46_real_centre_frequencies',caps.length===46&&caps.every((x,i)=>x.mode===2*i+2));
 const eU=q(87,32),eInv=q(3,8);
 ck('strict_rational_exp_comparisons',q(65,24).add(q(1,100)).lt(eU)&&q(8,3).lt(q(65,24)));
 const terms=caps.map(x=>({mode:x.mode,weighted:up(x.bound.mul(eU.pow(x.mode)))}));
 const Aw=up(addall(terms.map(x=>x.weighted)));
 const c0=up(q(4).mul(V0.pow(2)).mul(A.pow(2)));
 const Lw=up(c0.add(V0.mul(q(5,4)).mul(Aw)));
 const Fw=up(q(23,18).mul(Aw.pow(2))
   .add(q(8).mul(V0).mul(A.pow(2)).mul(q(5,4)).mul(Aw))
   .add(q(16).mul(V0.pow(2)).mul(A.pow(4))));
 ck('actual_finite_centre_additional_unit_strip',V0.mul(Aw).lt(q(1,64))&&Lw.lt(1));
 const tailMass=up(Fw.mul(Lw.pow(5)).div(q(1).sub(Lw)));
 const oldTail=dyad(p.complete_Neumann_tail_mass),out=[];
 let strengthened=0;
 for(const row of rows){
  const partial=addall(row.Neumann_powers_0_to4.map(dyad));
  const tail=up(tailMass.mul(eInv.pow(row.mode)));
  const both=oldTail.le(tail)?oldTail:tail;
  const raw=up(partial.add(both)),old=dyad(row.complete_source_upper);
  const result=old.le(raw)?old:raw;
  if(result.lt(old))strengthened++;
  out.push({mode:row.mode,retained_partial:cd(up(partial)),
    weighted_complete_tail:cd(tail),chosen_source_upper:cd(result)});
 }
 ck('all230_sources_retain_full_inverse_tail',out.length===230&&out.every(x=>q(0).lt(dyad(x.weighted_complete_tail))));
 ck('all230_sources_no_weaker',out.every((x,i)=>dyad(x.chosen_source_upper).le(dyad(rows[i].complete_source_upper))));
 ck('strict_improvement_not_a_support_deletion',strengthened>0);
 const blocks=[];
 for(let k=5;k<=61;k++){
  const first=184+92*(k-1)+2,last=Math.min(5758,184+92*k);
  if(first>last)continue;
  const C=up(Fw.mul(Lw.pow(k)).div(q(1).sub(Lw)));
  blocks.push({first_mode:first,last_mode:last,minimum_inverse_power:k,
   common_factor:cd(C),formula:'common_factor*(3/8)^mode',
   first_mode_upper:cd(up(C.mul(eInv.pow(first))))});
 }
 ck('entire_remainder_of_middle554_to5758_covered',
  blocks.length===57&&blocks[0].first_mode===554&&blocks[56].last_mode===5758&&
  blocks.every((x,i)=>i===0||x.first_mode===blocks[i-1].last_mode+2));
 ck('actual_full_low_centre_norm_below10',A.lt(10));
 const result={
  schema:'visible-flex-larger-R100-low46-wide-tail-v2',
  status:'Fresh R100 grouped-domain finite-centre extra-strip complete middle source coefficients; inspect actual gates',
  parameter_domain:p.parameter_domain,parameter_norm:p.parameter_norm,
  complete_R100_primary_sha256:p.complete_R100_primary_sha256,
  author:'exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-13',execution,source_sha256:sourceSha,
  input_hashes:{complete_spectral_primary:primarySha},
  all_gates:Object.values(gates).every(Boolean),gates,
  exact_unpartitioned_v2_sha256:primarySha,extra_strip:'1',original_constant_strip:'18/125',
  exp_positive_upper:cd(eU),exp_negative_upper_factor:cd(eInv),
  same_actual_low_centre_norm:cd(up(A)),wide_centre_norm:cd(Aw),
  mean_bound_kept_from_original_strip:cd(c0),wide_inverse_norm:cd(Lw),
  wide_numerator_norm:cd(Fw),weighted_Neumann_tail_from_power5:cd(tailMass),
  full_point_radius_in_wider_strip:cd(up(V0.mul(Aw))),
  mode_weights:terms.map(x=>({mode:x.mode,bound:cd(x.weighted)})),
  strictly_improved_source_rows:strengthened,source_rows94_to552:out,
  complete_middle554_to5758_blocks:blocks,
  source_units:'pair Fourier coefficient e^(18m/125)|N_m|/[(s+|ell|) V_I^2], source-x',
  norm_quantifier:'sum of separate radial Fourier component suprema; known real low46 solution and its phase orbit',
  no_width_gain_for_unknown_middle_or_high_fields:true,
  new_mean_root_or_source_evaluation:false,new_Arb_ODE_Green:false,
  middle_response_or_full_joint_fixed_point_claimed:false,
  new_R100_grouped_domain_claimed:true,old_R92_domain_claimed:false
 };return result;
}
if(typeof module!=='undefined')module.exports={runWideTailFull};
if(typeof require!=='undefined'&&require.main===module){
 const fs=require('node:fs'),crypto=require('node:crypto'),args=process.argv.slice(2);
 if(args.length!==3)throw Error('Usage: node closure_outer_low_spectral_r100_wide_tail_v2.js OUTPUT.json COMPLETE_INPUT.json EXPECTED_INPUT_SHA256');
 const [output,input,expected]=args;
 const digest=s=>crypto.createHash('sha256').update(s).digest('hex');
 const result=runWideTailFull(fs.readFileSync(input,'utf8'),digest(fs.readFileSync(__filename)),{engine:'Node.js BigInt',version:process.version},digest,expected);
 fs.writeFileSync(output,JSON.stringify(result,null,2)+'\n',{flag:'wx'});
 process.stdout.write(JSON.stringify({all_gates:result.all_gates,output,input_sha256:expected})+'\n');
}
