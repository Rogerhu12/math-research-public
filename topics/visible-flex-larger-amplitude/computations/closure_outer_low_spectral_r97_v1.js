#!/usr/bin/env node
'use strict';
/* Prepared R97/R94-domain version of the full spectral enclosure.
   Same fixed real geometry and outer targets; the low centre is the
   R94 existing projection on the R92 real product domain. A fresh full
   R97 recovery output must be supplied with its exact SHA256.
   This is a new source, not a claim that old R96 values hold on R92.
   Signed index k denotes physical mode2k. Full mean/inverse retained. */
const INPUTS=[
 ['r91','notes/2026-11-12-closure-r91-split-jump-high-exact-ledger.json','badc734ef590c747d62fc75bd57ce2571bd89e8c522604b691406f469d47392f'],
 ['budget','notes/2026-11-12-closure-physical-green-budget-actions-43303787139-1-interval.json','86c9b5604a765a50028865a4f3edae3171d9582052e2b7e7515d0471d8685d45'],
 ['geometry','notes/2026-11-12-closure-physical-green-actions-43303787139-1-interval.json','e3bb0bad3afac3e19d6b811ad068d0b4251b2a1214718dcbd14a2eb98e1aaa03'],
 ['geometry_source','computations/closure_outer_physical_green_geometry_recovered_v2.py','c48606c4e127fb0d3f27479eeed11bff3c5cb69139148633ea4f74a9e1f63829'],
 ['head','notes/2026-11-12-root-r97-full46-cut-recovered-v2.json',null],
 ['r94','notes/2026-11-12-root-r94-full46-cut-exact-ledger.json','5eb45673a9080ae251e77c3203cfc2142ba31850fc244c7e2c8500df774249bc'],
 ['head_source','computations/root_full46_source_cut_transfer_recovered_v2.py','f989a3f2a07b70d0da36be3a05a87509e9d254215d0a11f7726b48b3767189ef'],
 ['family','notes/2026-11-12-root-anisotropic-auxiliary-family-r3-summary.json','17b1d776cdce044722db61c2981d64838d18fd66c6ef3fdd4c48fa183a9a3776']
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


const BITS=128,NEUMANN=4,PASSES=6;
function rec(x){return q(x.numerator,x.denominator);}
function exactBound(x){return x&&Object.prototype.hasOwnProperty.call(x,'numerator')?rec(x):upper(x);}
function up(x){return dyadicUp(x,BITS);}
function compactDyad(x){x=q(x);if(x.b&(x.b-1n))throw Error('not dyadic');return [String(x.a),1-x.b.toString(2).length];}
function coef(a,k){return a.get(k)||q(0);}
function norm(a){return addall([...a.values()]);}
function scaled(a,f){return new Map([...a].map(([k,v])=>[k,up(v.mul(f))]));}
function plus(a,b){const c=new Map(a);for(const [k,v]of b)c.set(k,up(coef(c,k).add(v)));return c;}
function convolution(a,b){
 const c=new Map();
 for(const [j,v]of a)for(const [k,w]of b)c.set(j+k,coef(c,j+k).add(v.mul(w)));
 for(const [k,v]of c)c.set(k,up(v));
 return c;
}
function symmetric(a){return [...a].every(([k,v])=>v.eq(coef(a,-k)));}
function sourceMajorant(caps,V0){
 const A=addall(caps),unit=new Map(),derivative=new Map();
 for(let i=0;i<46;i++){
  const j=2*i+2,t=up(caps[i].div(2*(1+j))),d=up(t.mul(j));
  unit.set(i+1,t);unit.set(-i-1,t);
  derivative.set(i+1,d);derivative.set(-i-1,d);
 }
 // U=K_theta-P and C=K+P_theta share the derivative joint cap.
 // The full two-component K^2+P^2 is bounded by joint unit mass.
 const Qpoly=plus(scaled(convolution(derivative,derivative),q(5,4)),
                  scaled(convolution(unit,unit),q(1,4)));
 const Lpoly=scaled(derivative,q(5,4));
 const mean=up(q(4).mul(V0.pow(2)).mul(A.pow(2)));
 const l=scaled(Lpoly,V0);l.set(0,mean);
 const Bpoly=scaled(Lpoly,q(8).mul(V0).mul(A.pow(2)));
 Bpoly.set(0,up(q(16).mul(V0.pow(2)).mul(A.pow(4))));
 const numerator=plus(Qpoly,Bpoly),ell=norm(l),fnorm=norm(numerator);
 if(!ell.lt(1)||!V0.mul(A).lt(q(1,64)))throw Error('Complete mean/inverse domain');
 let term=numerator,series=new Map(numerator);
 const powers=[new Map(numerator)];
 for(let k=1;k<=NEUMANN;k++){term=convolution(term,l);series=plus(series,term);powers.push(term);}
 const tail=up(fnorm.mul(ell.pow(NEUMANN+1)).div(q(1).sub(ell)));
 if(!symmetric(Qpoly)||!symmetric(l)||!symmetric(series))throw Error('Signed symmetry lost');
 return {A,Qpoly,Lpoly,l,numerator,ell,fnorm,series,tail,powers,
  pair(m){return up(coef(series,m/2).mul(2).add(tail));}};
}
function runSpectralR97(texts,hashes,sourceSha,execution,expectedHeadSha){
 if(!/^[a-f0-9]{64}$/.test(expectedHeadSha||''))throw Error('Supply exact fresh complete R97 input SHA256');
 const docs={},gates={};
 function ck(k,v){gates[k]=!!v;if(!v)throw Error('Unpaid exact spectral gate: '+k);}
 for(const [key,path,pinned]of INPUTS){
  const expected=key==='head'?expectedHeadSha:pinned;
  if(hashes[key]!==expected)throw Error('Changed input: '+path);
  docs[key]=key.endsWith('_source')?texts[key]:parseExact(texts[key]);
 }
 const l=docs.r91,b=docs.budget,g=docs.geometry,h=docs.head,f=docs.family;
 for(const [key,d]of Object.entries(docs)){
  if(key.endsWith('_source'))continue;
  ck('input_'+key+'_complete_gates',d.all_gates===true&&Object.values(d.gates).every(v=>v===true));
 }
 ck('R91_geometry_and_budget_identity',
  l.input_hashes[INPUTS[1][1]]===hashes.budget&&l.input_hashes[INPUTS[2][1]]===hashes.geometry);
 ck('complete_real_Green_identity',b.geometry_sha256===hashes.geometry&&
   g.config.entrypoint_sha256===hashes.geometry_source&&
   b.geometry_entrypoint_sha256===hashes.geometry_source);
 ck('same_fixed_R74_outer_targets_and_geometry',
  g.config.input_hashes[INPUTS.find(x=>x[0]==='family')[1]]===hashes.family&&
  g.config.parameter_axes.length===20);
 ck('fresh_complete_R97_source_and_four_pinned_origins',
  h.source_sha256===hashes.head_source&&
  h.input_identities.r83.sha256==='4ec6d30adb9eb639e658bcaa86873cfed0675ab975d3a8f92778888339f966b2'&&
  h.input_identities.r92.sha256==='9ef88cdeef25ed0dd688082e53b25b5f8aacda2bd67c9dada61c250cefa4052a'&&
  h.input_identities.r94.sha256===hashes.r94&&
  h.input_identities.r78.sha256==='9e891098dd625f7418c48d91ee92db900bd7b0d1c44b2b69c1cdebbd8d03c930');
 ck('new_R92_parameter_domain_explicit',
  h.parameter_domain==='R92 original20 complex polydisc times weighted-l1 transverse26 unit ball'&&
  h.parameter_norm==='max(original20 normalized linf, transverse26 weighted-l1)'&&
  h.gates.all_new_paths_in_complete_domain===true&&h.gates.q4113===true);
 ck('complete_true_head_nonmean_heights_remain_exact',
  h.low_Q_and_P_nonlinear_remainder_identically_zero===true&&
  h.complete_high.head.bands.length===3&&h.complete_high.outer.bands.length===3&&
  h.mean_and_single_cuff_bounds_retained_from_R94===true&&
  h.gates.positive_complete_far_retained===true&&q(0).lt(upper(h.true_far_added_once_per_whole_mass)));
 ck('same_existing_R94_low_projection_domain',
  upper(h.whole_low46.Wtau_b1.chosen_complete_true_DN_minus_exact_linear.uniform_value_upper)
   .le(exactBound(docs.r94.low_nonlinear_K_value)));
 ck('same_source_x_physical_units',
   g.config.physical_source==='N enters K_x, hence Y_2 source is sqrt(r*w^3)*N, no extra r_x');
 const src=texts.geometry_source;
 ck('full_weak_cap_density_retained',
   src.includes('A = E*s+(E+w*w/9)*ell')&&
   src.includes('cap = ((Q+mean)/(1-lead)).upper()')&&
   src.includes('wc = weak_density(g, V, sigma, arb(0), V)')&&
   src.includes('oldcap, ws[0], wl[0], wc[1]'));
 const V0=dyad(g.config.uniform_envelope),sigma=q(17,16);
 ck('same_local_V_and_constant_strip',
   V0.eq(p2(-40))&&g.config.source_tau==='1/64'&&
   rec(l.actual_low_wide_strip).eq(q(18,125)));
 ck('all46_actual_mode_rows',
   b.mode_rows.length===46&&l.low_mode_rows.length===46&&h.mode_rows.length===46&&
   b.mode_rows.every((row,i)=>row.mode===String(2*i+2)&&
    row.mode===l.low_mode_rows[i].mode&&row.mode===h.mode_rows[i].mode));
 const fixed=[],kernel=[],initial=[],rowInputs=[];
 for(let i=0;i<46;i++){
  const row=b.mode_rows[i],wide=l.low_mode_rows[i],hr=h.mode_rows[i],m=2*i+2;
  const exp=rec(wide.exp_upper),lr=rec(wide.linear_wide).div(V0);
  const beta=upper(hr.new_complete_Wsigma1.chosen_complete_true_DN_minus_exact_linear.uniform_value_upper);
  const head=up(dyad(row.complete_weighted_inner_K_trace_to_field_norm).mul(exp).mul(beta));
  const linear=up(lr.add(head)),cap=dyad(row.densities.find(x=>x.density==='weak_candidate_cap').strong_output_row_sum);
  const k=up(cap.div(sigma.pow(2)));
  const first=up(linear.add(rec(wide.source_wide).div(V0)));
  fixed.push(linear);kernel.push(k);initial.push(first);
  rowInputs.push({mode:m,linear:compactDyad(up(lr)),head:compactDyad(head),
   source_kernel_for_cV2:compactDyad(k),initial:compactDyad(first)});
 }
 ck('new_complete_head_no_larger_than_R91',
  addall(rowInputs.map(x=>dyad(x.head))).le(rec(l.actual_low_true_head_wide).div(V0)));
 ck('initial_full_spectral_domain',addall(initial).lt(12));
 const rounds=[];let caps=initial.slice();
 for(let pass=0;pass<PASSES;pass++){
  const S=sourceMajorant(caps,V0),next=caps.map((old,i)=>{
    const proposed=up(fixed[i].add(kernel[i].mul(S.pair(2*i+2))));
    return old.le(proposed)?old:proposed;
  });
  ck('pass_'+pass+'_all46_inductive_enclosure',next.length===46&&next.every((x,i)=>x.le(caps[i])));
  rounds.push({pass,old_total:compactDyad(up(addall(caps))),full_inverse_norm:compactDyad(up(S.ell)),
   full_Neumann_tail:compactDyad(S.tail),new_total:compactDyad(up(addall(next))),
   caps:next.map(compactDyad)});
  caps=next;
 }
 const final=sourceMajorant(caps,V0),middle=[];
 for(let m=94;m<=552;m+=2){
  const pieces=final.powers.map(v=>compactDyad(up(coef(v,m/2).mul(2))));
  middle.push({mode:m,quadratic:compactDyad(up(coef(final.Qpoly,m/2).mul(2))),
   mean_numerator_direct:compactDyad(up(coef(final.numerator,m/2).sub(coef(final.Qpoly,m/2)).mul(2))),
   complete_source_upper:compactDyad(final.pair(m)),Neumann_powers_0_to4:pieces});
 }
 ck('quadratic_pure_middle_support',middle.every(x=>x.mode<186||dyad(x.quadratic).eq(0)));
 ck('mean_numerator_direct_high_support',middle.every(x=>dyad(x.mean_numerator_direct).eq(0)));
 ck('all_signed_complete_Neumann_terms_retained',NEUMANN===4&&q(0).lt(final.tail)&&final.ell.lt(1));
 ck('same_known_solution_not_a_new_fixed_point',addall(caps).le(addall(initial)));
 return {
  status:'Fresh spectral enclosure of the existing R94 low46 projection on the real R92 domain; inspect actual gates',
  author:'exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12',execution,source_sha256:sourceSha,
  input_hashes:Object.fromEntries(INPUTS.map(([key,path])=>[path,hashes[key]])),
  all_gates:Object.values(gates).every(Boolean),gates,
  parameter_domain:'Real restriction of R92 original20 polydisc times weighted-l1 transverse26 unit ball; same fixed R74 outer targets',
  complete_R97_primary_sha256:hashes.head,
  same_existing_low_centre:'R94 projection; old R96 numerical caps are not borrowed',
  physical_source_units:'source-x N, density (s+|ell|) V_I^2; no extra r_x',
  centre_norm:'a_m=(1+m)e^(18m/125)[sup(|P_m|+|P_-m|)/V_I + sup(|K_m|+|K_-m|)/V_I], real conjugate pair masses',
  initial_rows:rowInputs,rounds,final_caps:caps.map((v,i)=>({mode:2*i+2,bound:compactDyad(v)})),
  initial_total:compactDyad(up(addall(initial))),final_total:compactDyad(up(addall(caps))),
  full_inverse_norm:compactDyad(up(final.ell)),
  complete_source_numerator_norm:compactDyad(up(final.fnorm)),
  omitted_Neumann_terms_from:NEUMANN+1,
  complete_Neumann_tail_mass:compactDyad(final.tail),
  middle_complete_sources:middle,
  modes_above552:'No retained degree0..4 numerator/inverse term; use the complete displayed Neumann tail, or the exact support-index geometric tail in the proof.',
  rounding:'Every introduced bound is rounded upward to128 significant dyadic bits; every comparison uses BigInt fractions',
  scope:{actual_middle_Green_paid:false,low_middle_high_joint_fixed_point_paid:false,
    complete_mean_and_inverse_retained:true,no_mean_or_inverse_remainder_deleted:true,
    new_R92_transverse_domain:true,closed_surface_claimed:false},
  no_new_source_ODE_Arb:true
 };
}
if(typeof module!=='undefined')module.exports={runSpectralR97};
if(typeof require!=='undefined'&&require.main===module){
 const fs=require('node:fs'),crypto=require('node:crypto'),argv=process.argv.slice(2),out=argv.shift(),headSha=argv.shift();
 if(!out||!headSha)throw Error('Usage: node closure_outer_low_spectral_r97_v1.js OUTPUT.json COMPLETE_R97_SHA256 [eight input paths in INPUTS order]');
 const texts={},hashes={};INPUTS.forEach(([key,path],i)=>{const buf=fs.readFileSync(argv[i]||path);
  texts[key]=buf.toString('utf8');hashes[key]=crypto.createHash('sha256').update(buf).digest('hex');});
 const sourceSha=crypto.createHash('sha256').update(fs.readFileSync(__filename)).digest('hex');
 const result=runSpectralR97(texts,hashes,sourceSha,{engine:'Node.js BigInt',version:process.version},headSha);
 fs.writeFileSync(out,JSON.stringify(result,null,2)+'\n',{flag:'wx'});
 process.stdout.write(JSON.stringify({all_gates:result.all_gates,output:out})+'\n');
}
