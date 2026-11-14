#!/usr/bin/env node
/* R109: complete-source polynomial linearization and frequency-difference
 * tail. /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
 * Exact BigInt proofs and already executed immutable R108/R88 small inputs.
 * This does not evaluate a new source-row Jacobian or cut map.
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
 r108:{path:"notes/2026-11-13-root-r108-tilted-wiener-exact-gates.json",
  sha256:"e5c28ae70288c46f50da826eceaee684c1350260f694f0409123f8066878026a"},
 r88:{path:"notes/2026-11-12-root-linear-centre-local-restored-r1-summary.json",
  sha256:"94fb941354dbb4769cb7ce80d5f7fd14eed6bdbce893842881c5c949c460288a"}
};
function pow(x,n){let r=Q(1);for(let j=0;j<n;j++)r=r.mul(x);return r;}
function two(e){return e>=0?Q(2n**BigInt(e)):Q(1).div(Q(2n**BigInt(-e)));}
function dy(x){if(x.upper)x=x.upper;return Q(x.mantissa).mul(two(x.binary_exponent));}
function run(texts,hash){
 const d={},inputs={};
 for(const[k,spec]of Object.entries(INPUTS)){
  assert(hash(texts[k])===spec.sha256,"complete small input SHA mismatch: "+k);
  d[k]=JSON.parse(texts[k]);inputs[spec.path]=spec.sha256;
 }
 const gates={};const gate=(k,v)=>{gates[k]=Boolean(v);assert(gates[k],"gate failed: "+k);};
 const r=d.r88,p=d.r108;
 gate("R108_all18_actual_gates",p.all_gates && Object.keys(p.gates).length===18 && Object.values(p.gates).every(v=>v===true));
 gate("R108_original_R88_identity",p.input_sha256[INPUTS.r88.path]===INPUTS.r88.sha256 &&
  p.source_sha256==="440357edf50eaebb5fc1c1a2d5d383dd63ec06631673fec45474f74cf7a5cd33");
 gate("R88_actual_source_and_coverage",r.all_gates && Object.values(r.gates).every(v=>v===true) &&
  r.source_sha256==="306b2bc0c49635d731f3bbe91653310f2b2ecba19bcb7437f8ef932f37a5d75b" &&
  r.original_panels===10793 && r.actual_subpanels===10933);
 const R0=Q("1/64"),Rd=Q("1/128");
 gate("quadratic_mean_norm_below_quarter",Q("29/144").cmp(Q("1/4"))<0);
 const leading=Q("5/4").mul(R0).add(pow(R0,2).div(Q(4)));
 const numerator=Q("23/18").add(Q("5/8").mul(R0)).add(pow(R0,2).div(Q(16)));
 const tailCoeff=pow(Q("5/4").add(R0.div(Q(4))),4).mul(numerator).div(Q(1).sub(leading));
 gate("approximate_complete_inverse_domain",leading.cmp(Q(1))<0);
 gate("complete_four_term_inverse_tail_coefficient_below4",tailCoeff.cmp(Q(4))<0);
 gate("mean_cauchy_circle_inside_original_domain",Rd.mul(Q("4/3")).cmp(R0)<0);
 gate("inverse_cauchy_circle_inside_original_domain",Rd.mul(Q("6/5")).cmp(R0)<0);
 const meanDerivative=Q(680).mul(pow(Q("4/3"),4)).mul(Q(3));
 const inverseDerivative=Q(4).mul(pow(Q("6/5"),6)).mul(Q(5));
 gate("exact_mean_cauchy_constant",meanDerivative.eq(Q("174080/27")));
 gate("exact_inverse_cauchy_constant",inverseDerivative.eq(Q("186624/3125")));
 const fullDerivative=meanDerivative.add(inverseDerivative.mul(pow(Rd,2)));
 gate("complete_DN_minus_Dpolynomial_coefficient_below6450",fullDerivative.cmp(Q(6450))<0);
 gate("source_error_coefficient_below681",Q(680).add(Q(4).mul(pow(R0,2))).cmp(Q(681))<0);
 gate("6450_below_8192",Q(6450).cmp(two(13))<0);
 const V=Q(p.original_local_norm_envelope_global_upper);
 let total=Q(0);
 for(let m=2;m<=40;m+=2){
  const row=(m===2||m===4)?r.true_linear_selected_component_mass[m]:r.original_mode_component_mass[m];
  total=total.add(dy(row.P)).add(dy(row.K));
 }
 const Rsigma=total.mul(V);
 gate("same_global_radial_first_Rsigma_below_2_minus40",Rsigma.cmp(two(-40))<0);
 gate("same_global_Rsigma_inside_derivative_domain",Rsigma.cmp(Rd)<0);
 const globalDerivative=Q(6450).mul(pow(Rsigma,3));
 gate("global_strong_to_weak_Jacobian_tail_below_2_minus107",globalDerivative.cmp(two(-107))<0);
 const tilted=[];
 for(const q of [2,4]){
  const row=p.trials.find(x=>x.q===q);
  const R=Q(row.P_upper).add(Q(row.K_upper));
  const rExponent=q===2?38:36,dExponent=q===2?101:95;
  gate("q"+q+"_global_strong_radius_below_2_minus"+rExponent,R.cmp(two(-rExponent))<0);
  gate("q"+q+"_inside_original_derivative_ball",R.cmp(Rd)<0);
  const coefficient=Q(6450).mul(pow(R,3));
  gate("q"+q+"_full_Jacobian_tail_prefactor_below_2_minus"+dExponent,coefficient.cmp(two(-dExponent))<0);
  const a=Q("64/63").div(Q(q)),fold=Q(1).add(pow(a,2)).div(Q(1).sub(pow(a,2)));
  tilted.push({q,global_radial_first_strong_radius_upper:R.toString(),
   exact_derivative_tail_prefactor_upper:coefficient.toString(),
   strict_simple_prefactor:"2^(-"+dExponent+")",
   even_frequency_folded_weight_sum_upper:fold.toString(),
   formula:"cosine output m from sineP/cosineK input n: prefactor*(1+n)*(q^(-abs(m-n))+q^(-m-n))"});
 }
 const samples=[];
 for(const[m,n]of [[92,2],[92,4],[92,40],[92,92],[42,2],[6,4]]){
  const choices=[{kind:"original_sigma",value:two(-107).mul(Q(1+n)).mul(pow(Q("64/63"),Math.max(0,n-m)))}];
  for(const q of [2,4]){
   const exponent=q===2?101:95;
   const factor=Q(1).div(pow(Q(q),Math.abs(m-n))).add(Q(1).div(pow(Q(q),m+n)));
   choices.push({kind:"q"+q,value:two(-exponent).mul(Q(1+n)).mul(factor)});
  }
  choices.sort((a,b)=>a.value.cmp(b.value));
  samples.push({output_m:m,input_n:n,selected_bound:choices[0].kind,
   strict_Jacobian_tail_over_c_bg_per_unit_amplitude:choices[0].value.toString(),
   scope:"error DN-DN4 only; the complete finite signed DN4 must still be evaluated and added"});
 }
 return {schema:"visible-flex-larger-R109-source-polynomial-and-Jacobian-tail-v1",
  author:"/root (GPT-6 Astra Pro, AI-assisted)",status:"Actually evaluated exact BigInt gates; no new source-row Jacobian or physical integration",
  input_sha256:inputs,all_gates:Object.values(gates).every(v=>v===true),gates,
  arithmetic:"Exact BigInt rational operations and comparisons",
  constants:{working_radius:R0.toString(),derivative_radius:Rd.toString(),
   approximate_leading_at_working_radius:leading.toString(),
   complete_inverse_tail_coefficient:tailCoeff.toString(),
   mean_derivative_cauchy:meanDerivative.toString(),inverse_derivative_cauchy:inverseDerivative.toString(),
   complete_derivative_coefficient_at_radius:fullDerivative.toString(),
   derivative_slack6450:Q(6450).sub(fullDerivative).toString()},
  original_R88_V_upper:V.toString(),
  original_R88_global_radial_first_Rsigma_upper:Rsigma.toString(),
  original_R88_global_derivative_tail_upper:globalDerivative.toString(),
  global_strict_operator_tail:"<2^(-107) from joint strong A_sigma,1 to density-normalized weak A_sigma,0",
  sigma:"1/64",tilted,samples,
  polynomial:"N4=Pi_perp [Q+ell(2c2D0+c2^2)]*(1-L2+L2^2-L2^3), L2=D0+c2",
  retained:"complete mean error, all inverse terms, finite numerator zero mode and c2^2, exact Dc2, all signed Fourier modes",
  no_new_source_ODE_Green_or_cut_execution:true,
  actual_full46_closure_or_closed_surface_claimed:false};
}
if(typeof require!=="undefined" && typeof module!=="undefined" && require.main===module){
 const fs=require("fs"),path=require("path"),crypto=require("crypto");
 const a=process.argv.slice(2);assert(a.length===4 && a[0]==="--root" && a[2]==="--out","Usage: node source.js --root TOPIC_ROOT --out FRESH_JSON");
 const root=path.resolve(a[1]),out=path.resolve(a[3]);assert(!fs.existsSync(out),"fresh immutable output required");
 const texts={};for(const[k,spec]of Object.entries(INPUTS))texts[k]=fs.readFileSync(path.join(root,spec.path),"utf8");
 const hash=s=>crypto.createHash("sha256").update(s,"utf8").digest("hex");
 const result=run(texts,hash);result.source_sha256=hash(fs.readFileSync(__filename,"utf8"));
 fs.writeFileSync(out,JSON.stringify(result,null,2)+"\n",{flag:"wx"});
 process.stdout.write(JSON.stringify({output:out,all_gates:result.all_gates})+"\n");
}
if(typeof module!=="undefined")module.exports={run,INPUTS};
