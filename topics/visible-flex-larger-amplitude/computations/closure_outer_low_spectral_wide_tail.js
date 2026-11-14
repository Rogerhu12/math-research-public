#!/usr/bin/env node
'use strict';
/* R96 exact finite-centre weighted Neumann-tail refinement.
   Consumes the actually executed spectral_v2 result, not a new PDE solve. */
const INPUTS=[
  [
    "primary",
    "notes/2026-11-12-closure-low-spectral-v2-primary.json",
    "5bf71c2b56c49a23ec58d7674af65c289a4ff6d0438339c410b35206bc0f8d3e"
  ],
  [
    "part0",
    "notes/2026-11-12-closure-low-spectral-v2-middle-part0.json",
    "61748a5325a8fc4050e60c494dfa42930c31075b002ec488ede1cb2a5dc391e1"
  ],
  [
    "part1",
    "notes/2026-11-12-closure-low-spectral-v2-middle-part1.json",
    "8958b93412ef486f72ce25cbb3a11f28e6b3f4511b433334da555cff46a759cd"
  ],
  [
    "part2",
    "notes/2026-11-12-closure-low-spectral-v2-middle-part2.json",
    "24d54d9b381c0ead5fdfab590687efa50754fac15ae21db01eae57dba988b546"
  ],
  [
    "part3",
    "notes/2026-11-12-closure-low-spectral-v2-middle-part3.json",
    "140f613b10efa60ae9adc7308614ed24d6e91c61ddc5212d345b25f52524223c"
  ],
  [
    "part4",
    "notes/2026-11-12-closure-low-spectral-v2-middle-part4.json",
    "9fe5d45cd536006863b9d43b595e2ddcd493a0edf24c7b10ddfd3df33e9464ee"
  ]
];
const FULL_SHA="e78f8fa461077bb7c22d4b41835eeb82c85cb5321136d35477b6113a0f546e11";
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
function runWideTail(texts,hashes,sourceSha,execution,hashText){
 const docs={},gates={};function ck(k,v){gates[k]=!!v;if(!v)throw Error('Unpaid weighted-tail gate: '+k);}
 for(const [key,path,sha]of INPUTS){if(hashes[key]!==sha)throw Error('Changed input: '+path);docs[key]=JSON.parse(texts[key]);numGuard(docs[key]);}
 const p=docs.primary,rows=Array.from({length:5},(_,i)=>docs['part'+i].rows).flat();
 ck('original_complete26_gates',p.all_gates===true&&Object.keys(p.gates).length===26&&Object.values(p.gates).every(Boolean));
 ck('all230_source_rows_preserved',rows.length===230&&rows.every((x,i)=>x.mode===94+2*i));
 const reconstructed={};
 for(const [key,val]of Object.entries(p)){
  if(key==='modes_above552')reconstructed.middle_complete_sources=rows;
  if(!['middle_complete_sources_parts','complete_unpartitioned_primary_sha256','partition_semantics'].includes(key))reconstructed[key]=val;
 }
 ck('exact_original_complete_payload_reproduced',
  hashText(JSON.stringify(reconstructed,null,2)+'\n')===FULL_SHA&&p.complete_unpartitioned_primary_sha256===FULL_SHA);
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
  status:'Executed exact finite-centre extra-strip Neumann tail and complete middle source coefficients',
  author:'exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12',execution,source_sha256:sourceSha,
  input_hashes:Object.fromEntries(INPUTS.map(([key,path])=>[path,hashes[key]])),
  all_gates:Object.values(gates).every(Boolean),gates,
  exact_unpartitioned_v2_sha256:FULL_SHA,extra_strip:'1',original_constant_strip:'18/125',
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
  middle_response_or_full_joint_fixed_point_claimed:false,new_R92_domain_claimed:false
 };return result;
}
if(typeof module!=='undefined')module.exports={runWideTail};
if(typeof require!=='undefined'&&require.main===module){
 const fs=require('node:fs'),crypto=require('node:crypto'),args=process.argv.slice(2),output=args.shift();
 if(!output)throw Error('Usage: node closure_outer_low_spectral_wide_tail.js OUTPUT.json [six pinned input paths]');
 const digest=s=>crypto.createHash('sha256').update(s).digest('hex'),texts={},hashes={};
 for(let i=0;i<INPUTS.length;i++){const[key,path]=INPUTS[i],buf=fs.readFileSync(args[i]||path);texts[key]=buf.toString('utf8');hashes[key]=digest(buf);}
 const r=runWideTail(texts,hashes,digest(fs.readFileSync(__filename)),{engine:'Node.js BigInt',version:process.version},digest);
 fs.writeFileSync(output,JSON.stringify(r,null,2)+'\n',{flag:'wx'});process.stdout.write(JSON.stringify({all_gates:r.all_gates,output})+'\n');
}
