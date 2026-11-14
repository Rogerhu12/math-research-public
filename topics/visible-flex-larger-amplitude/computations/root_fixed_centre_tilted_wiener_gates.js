#!/usr/bin/env node
/* R108: exact small-input tilted Wiener inverse gates for the unchanged R88 Z0.
 * /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
 * BigInt only for proof arithmetic. Decimal displays are not proof inputs.
 * No ODE, source-row replay, Green integral, cut, or full solution is executed.
 * The six complete source files are all independently below100KB.
 */
"use strict";
/* Exact rational arithmetic. Only powers of two are stripped before the
   ordinary Euclidean gcd; no rounding or arithmetic tolerance is used. */
function assert(ok,message){if(!ok)throw Error(message);}
function gcd(a,b){
 a=a<0n?-a:a;b=b<0n?-b:b;
 if(a===0n)return b;if(b===0n)return a;
 // gcd(2^r*A,2^s*B)=2^min(r,s)*gcd(A,B), with A,B odd.
 const pa=a&(-a),pb=b&(-b),common=pa<pb?pa:pb;
 a/=pa;b/=pb;
 while(b){const t=a%b;a=b;b=t;}
 return a*common;
}
class Rat{
 constructor(n,d=1n){n=BigInt(n);d=BigInt(d);assert(d!==0n,"zero rational denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
 add(q){q=Q(q);return new Rat(this.n*q.d+q.n*this.d,this.d*q.d);}
 sub(q){return this.add(Q(q).neg());}
 mul(q){q=Q(q);return new Rat(this.n*q.n,this.d*q.d);}
 div(q){q=Q(q);return new Rat(this.n*q.d,this.d*q.n);}
 neg(){return new Rat(-this.n,this.d);}
 abs(){return this.n<0n?this.neg():this;}
 cmp(q){q=Q(q);const x=this.n*q.d-q.n*this.d;return x<0n?-1:x>0n?1:0;}
 eq(q){return this.cmp(q)===0;}
 toString(){return this.n.toString()+"/"+this.d.toString();}
 toJSON(){return this.toString();}
}
function Q(x){
 if(x instanceof Rat)return x;
 if(typeof x==="bigint")return new Rat(x);
 if(typeof x==="number"){assert(Number.isSafeInteger(x),"internal noninteger Number");return new Rat(BigInt(x));}
 assert(typeof x==="string","exact input must be a rational or decimal string");
 if(/^[+-]?\d+\/[+-]?\d+$/.test(x)){const p=x.split("/");return new Rat(BigInt(p[0]),BigInt(p[1]));}
 const m=/^([+-]?)(\d+)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/.exec(x);
 assert(m,"invalid exact decimal: "+String(x));const e=Number(m[4]||"0")-(m[3]||"").length;
 assert(Number.isSafeInteger(e)&&Math.abs(e)<=10000,"decimal exponent out of range");
 let n=BigInt(m[2]+(m[3]||""));if(m[1]==="-")n=-n;
 return e>=0?new Rat(n*10n**BigInt(e)):new Rat(n,10n**BigInt(-e));
}



const INPUTS={
  "r88": {
    "path": "notes/2026-11-12-root-linear-centre-local-restored-r1-summary.json",
    "sha256": "94fb941354dbb4769cb7ce80d5f7fd14eed6bdbce893842881c5c949c460288a"
  },
  "source11": {
    "path": "notes/2026-11-12-closure-outer-source-cell11-r1-summary.json",
    "sha256": "f3d06071519f674de420a7fd66de45d14a8274bfb2089bd045bf0bfb2763cf83"
  },
  "source10_original": {
    "path": "notes/2026-11-12-closure-outer-source-cell10-r1-summary.json",
    "sha256": "388f0ea07840bc31851f025aecda7e8e73d9d893596bd088c95f7ea9002fd885"
  },
  "source10_refined": {
    "path": "notes/2026-11-12-closure-outer-source-cell10-refined-moments-r1-summary.json",
    "sha256": "bf4061ba1ca5295245165099d274b637630d16418a9e5283dd58898fb184e0c9"
  },
  "domain11": {
    "path": "notes/2026-11-12-closure-outer-source-cell11-r1-domain-replay.json",
    "sha256": "3299285850f9a4b637d7bbabe6aef4477a8e65803d57b43fbeb9ab7c0e6437d7"
  },
  "domain10": {
    "path": "notes/2026-11-12-closure-outer-source-cell10-r1-domain-replay.json",
    "sha256": "66c3451dc4fd6232b7fe1885467cf15a2f42086f99bd6edffa4bb0c66a4ebc7b"
  }
};
function dyadic(x){
 if(x.upper)x=x.upper;
 assert(typeof x.mantissa==="string" && Number.isSafeInteger(x.binary_exponent),"exact dyadic required");
 const p=Q(2n**BigInt(Math.abs(x.binary_exponent)));
 return x.binary_exponent>=0?Q(x.mantissa).mul(p):Q(x.mantissa).div(p);
}
function pow(q,n){let p=Q(1);for(let j=0;j<n;j++)p=p.mul(q);return p;}
function run(texts,hashText){
 const d={},inputHashes={};
 for(const [key,spec] of Object.entries(INPUTS)){
  assert(typeof texts[key]==="string","missing complete small input "+key);
  const h=hashText(texts[key]);
  assert(h===spec.sha256,"input SHA256 mismatch: "+key);
  inputHashes[spec.path]=h;d[key]=JSON.parse(texts[key]);
 }
 const r=d.r88,old11=d.source11,old10=d.source10_original,ref10=d.source10_refined;
 const a=d.domain11,b=d.domain10;
 const gates={};
 const gate=(k,v)=>{gates[k]=Boolean(v);assert(gates[k],"proof gate failed: "+k);};
 gate("original_R88_actual_all_gates",r.all_gates && Object.values(r.gates).every(v=>v===true));
 gate("original_fixed_centre_source_identity",r.source_sha256==="306b2bc0c49635d731f3bbe91653310f2b2ecba19bcb7437f8ef932f37a5d75b");
 gate("original10793_rows_and10933_profiles",r.original_panels===10793 && r.actual_subpanels===10933 &&
  r.groups.reduce((s,g)=>s+g.panels,0)===10793 && r.groups.reduce((s,g)=>s+g.subpanels,0)===10933);
 gate("all18_ordered_groups",JSON.stringify(r.groups.map(g=>[g.cell,g.segment]))===
  JSON.stringify([11,10].flatMap(n=>Array.from({length:9},(_,j)=>[n,j]))));
 gate("same_tau",r.tau==="1/64" && a.tau==="1/64" && b.tau==="1/64");
 gate("both_original_source_replays_actual",old11.all_gates && old10.all_gates &&
  Object.values(old11.gates).every(v=>v===true) && Object.values(old10.gates).every(v=>v===true) &&
  Object.values(a.gates).every(v=>v===true) && Object.values(b.gates).every(v=>v===true));
 gate("both_complete_domain_replay_hashes",
  old11.original_aggregate_replay_sha256===INPUTS.domain11.sha256 &&
  old10.original_aggregate_replay_sha256===INPUTS.domain10.sha256);
 gate("same_actual_refined_cell10",ref10.all_gates && Object.values(ref10.gates).every(v=>v===true) &&
  ref10.input_hashes[INPUTS.source10_original.path]===INPUTS.source10_original.sha256);
 gate("original_R88_input_chain",
  r.input_hashes[INPUTS.source11.path]===INPUTS.source11.sha256 &&
  r.input_hashes[INPUTS.source10_refined.path]===INPUTS.source10_refined.sha256);
 const expected=Array.from({length:20},(_,i)=>String(2*i+2));
 gate("all_original20_global_unweighted_caps",
  JSON.stringify(Object.keys(r.original_unweighted_component_mass))===JSON.stringify(expected));
 gate("only_actual_linear2and4_replace_original_modes",
  JSON.stringify(Object.keys(r.true_linear_selected_component_mass))===JSON.stringify(["2","4"]));
 const c11=dyadic(a.defect_bounds.complete_mean_abs.value),
       c10=dyadic(b.defect_bounds.complete_mean_abs.value),
       c0=c11.cmp(c10)>0?c11:c10,
       V=Q(1).div(Q(2n**43n)),
       roundingAllowance=Q(1).add(Q(1).div(Q(2n**78n))),
       mean=dyadic(r.maximum_complete_source_domain.mean);
 gate("original_c0_bound_strictly_below_representable_Vcap_square",
  c0.div(Q(4)).cmp(V.mul(V))<0);
 // R84 defines V_I by upward80-bit rounding of sqrt(c0_I/4).
 // The stronger check below reserves ample space even for a second outward
 // round: 2^-43 is exactly representable at every precision used here.
 gate("original_Vcap_with_explicit_extra_rounding_margin",
  c0.div(Q(4)).mul(roundingAllowance).mul(roundingAllowance).cmp(V.mul(V))<0);
 const trials=[];
 for(const k of [1,2,3,4]){
  let P=Q(0),K=Q(0),T=Q(0),U=Q(0);
  for(let m=2;m<=40;m+=2){
   const selected=m===2||m===4;
   const row=selected?r.true_linear_selected_component_mass[m]:r.original_unweighted_component_mass[m];
   let p=dyadic(row.P),h=dyadic(row.K);
   assert(p.cmp(Q(0))>=0 && h.cmp(Q(0))>=0,"nonnegative global component caps");
   // The selected records already contain (1+m) exp(m/64).
   // Dividing only by (1+m) discards exp(m/64)>=1 conservatively.
   if(selected){p=p.div(Q(1+m));h=h.div(Q(1+m));}
   p=p.mul(V);h=h.mul(V);
   const w=Q(1+m).mul(Q(2n**BigInt(k*m)));
   P=P.add(w.mul(p));K=K.add(w.mul(h));
   T=T.add(w.mul(p).mul(Q(m)));
   U=U.add(w.mul(p.add(h.mul(Q(m)))));
  }
  const L=mean.add(K).add(Q("5/4").mul(T));
  const accepted=L.cmp(Q(1))<0;
  const row={q:2**k,P_upper:P.toString(),K_upper:K.toString(),
   Ptheta_upper:T.toString(),Ktheta_minus_P_upper:U.toString(),
   leading_upper:L.toString(),inverse_domain_proved:accepted};
  if(accepted){
   const tailFactor=pow(L,4).div(Q(1).sub(L));
   row.four_term_tail_factor_over_numerator_norm=tailFactor.toString();
   const exponent=k===1?38:35;
   gate("q"+row.q+"_leading_below_2_power_minus_"+exponent,L.cmp(Q(1).div(Q(2n**BigInt(exponent))))<0);
   const tailExp=4*exponent-1;
   gate("q"+row.q+"_tail_factor_below_2_power_minus_"+tailExp,tailFactor.cmp(Q(1).div(Q(2n**BigInt(tailExp))))<0);
   row.simple_tail_factor_strict_upper="2^(-"+tailExp+")";
   row.mode92_cosine_tail_over_numerator_norm_strict_upper=
    "2^(-"+(tailExp+k*92)+")/93";
  }else{
   row.scope="This global cap does not certify this tilted inverse; no failure of the actual denominator is inferred.";
  }
  trials.push(row);
 }
 gate("q2_and_q4_complete_inverse_domains",trials[0].inverse_domain_proved && trials[1].inverse_domain_proved);
 return {schema:"visible-flex-larger-R108-tilted-Wiener-exact-small-gates-v1",
  author:"/root (GPT-6 Astra Pro, AI-assisted)",
  status:"Actually evaluated exact BigInt gates on six complete immutable small inputs",
  input_sha256:inputHashes,all_gates:Object.values(gates).every(v=>v===true),gates,
  arithmetic:"Exact BigInt rational arithmetic; no floating-point proof comparisons",
  fixed_centre:"Original R88 true linear2/4 and unchanged original6..40, no R101 caps",
  original_candidate_complete_mean_global_upper:c0.toString(),
  original_local_norm_envelope_global_upper:V.toString(),
  original_V_definition:"R84 exact upward80-bit dyadic sqrt(original c0_I/4); same V_I everywhere",
  fixed_centre_complete_mean_global_upper:mean.toString(),
  original_source_rows:10793,underlying_original_profiles:10933,
  tilted_norm:"sum_n (1+abs(n))*q^abs(n)*sup_x abs(f_n(x))",
  trials,
  coefficient_rule:"even cosine m: error <= Lq^4*Aq/((1-Lq)*(1+m)*q^m); no extra2",
  no_new_source_rows_or_ODE_or_Green_integrals:true,
  actual_full46_fixed_point_or_cut_or_closed_surface_claimed:false};
}
if(typeof require!=="undefined" && typeof module!=="undefined" && require.main===module){
 const fs=require("fs"),path=require("path"),crypto=require("crypto");
 const args=process.argv.slice(2);
 assert(args.length===4 && args[0]==="--root" && args[2]==="--out","Usage: node source.js --root TOPIC_ROOT --out FRESH_JSON");
 const [root,out]=[path.resolve(args[1]),path.resolve(args[3])];
 assert(!fs.existsSync(out),"immutable fresh output required");
 const texts={};for(const [k,spec] of Object.entries(INPUTS))texts[k]=fs.readFileSync(path.join(root,spec.path),"utf8");
 const hash=s=>crypto.createHash("sha256").update(s,"utf8").digest("hex");
 const result=run(texts,hash);result.source_sha256=hash(fs.readFileSync(__filename,"utf8"));
 fs.writeFileSync(out,JSON.stringify(result,null,2)+"\n",{flag:"wx"});
 process.stdout.write(JSON.stringify({output:out,all_gates:result.all_gates})+"\n");
}
if(typeof module!=="undefined")module.exports={run,INPUTS};
