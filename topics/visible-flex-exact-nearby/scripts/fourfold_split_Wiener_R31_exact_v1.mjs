#!/usr/bin/env node
/** Exact-rational split-Wiener budget. Run from the topic directory.
 * The original gzip endpoint and local-integral report are SHA-verified.
 * This arithmetic report requires the separate R101 factorization proof.
 */
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import zlib from "node:zlib";
function rationalPostPrenewton(summary, pre) {
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;}
  class F {
    constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
    static read(s){if(s instanceof F)return s;s=String(s).trim();if(s.includes("/")){let [n,d]=s.split("/");return new F(n,d);}
      let m=s.match(/^([+-]?)(\d+)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/);if(!m)throw Error("invalid exact decimal "+s);
      let n=BigInt(m[2]+(m[3]||""))*(m[1]==="-"?-1n:1n),e=Number(m[4]||0)-(m[3]||"").length;
      return e>=0?new F(n*10n**BigInt(e)):new F(n,10n**BigInt(-e));}
    add(y){y=F.read(y);return new F(this.n*y.d+y.n*this.d,this.d*y.d);}
    sub(y){y=F.read(y);return new F(this.n*y.d-y.n*this.d,this.d*y.d);}
    mul(y){y=F.read(y);return new F(this.n*y.n,this.d*y.d);}
    div(y){y=F.read(y);return new F(this.n*y.d,this.d*y.n);}
    abs(){return new F(this.n<0n?-this.n:this.n,this.d);}
    pow(k){return new F(this.n**BigInt(k),this.d**BigInt(k));}
    lt(y){y=F.read(y);return this.n*y.d<y.n*this.d;}
    le(y){y=F.read(y);return this.n*y.d<=y.n*this.d;}
    str(){return this.n.toString()+"/"+this.d.toString();}
    decimal(digits=30,up=false){let scale=10n**BigInt(digits),num=this.n*scale;let q=num/this.d,rem=num%this.d;if(up&&rem>0n)q++;if(!up&&rem<0n)q--;
      let neg=q<0n;if(neg)q=-q;let s=q.toString().padStart(digits+1,"0");return (neg?"-":"")+s.slice(0,-digits)+"."+s.slice(-digits);}
  }
  const f=F.read;
  function ball(s){s=String(s).trim();if(s[0]!=="["){let x=f(s);return [x,x];}
    let m=s.match(/^\[\s*(.*?)\s*\+\/-\s*(.*?)\s*\]$/);if(!m)throw Error("unsupported display ball "+s);
    const mid=f(m[1]),rad=f(m[2]);return [mid.sub(rad),mid.add(rad)];}
  function upper(r){return ball(r.upper)[1];}
  function lower(r){return ball(r.lower)[0];}
  const tests=[];
  function check(name,ok){tests.push({name,passed:!!ok});if(!ok)throw Error(name);}
  function upperCheck(name,actual,bound){let b=f(bound);check(name,upper(actual).le(b));return b;}
  check("complete same true object",summary.complete && pre.complete && pre.true_transformed_residual_proved &&
    pre.local_inverse_gate_passed && pre.identity.retarget_descriptor_sha256==="097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052");
  const prefix=pre.exact_quadratic_target.prefix;
  check("actual target CF has bounded positive quotients",prefix[0]===0 && prefix.slice(1).every(a=>Number.isInteger(a)&&a>=1&&a<=8) &&
    JSON.stringify(pre.exact_quadratic_target.periodic_tail)==="[1]");
  let cp=1n,cq=0n,cr=0n,ct=1n;
  for(const a0 of prefix){const a=BigInt(a0);[cp,cq,cr,ct]=[cp*a+cq,cp,cr*a+ct,cr];}
  check("exact CF matrix determinant",cp*ct-cq*cr===1n || cp*ct-cq*cr===-1n);
  let aa=ct*ct+ct*cr-cr*cr,bb=-2n*ct*cq-ct*cp-cq*cr+2n*cp*cr,cc=cq*cq+cq*cp-cp*cp;
  if(aa<0n){aa=-aa;bb=-bb;cc=-cc;}
  check("exact target discriminant",bb*bb-4n*aa*cc===5n);
  const old=summary.endpoint, full=old.full_square, half=old.sharp_half;
  const w=upperCheck("full finite w norm",pre.w_norm,"9e-12");
  const m1=upperCheck("full finite w first derivative",pre.w_derivative_norms[0],"1.2e-9");
  const m2=upperCheck("full finite w second derivative",pre.w_derivative_norms[1],"4e-7");
  const epsh=upperCheck("proved half-return error",pre.resulting_true_preconjugated_half_error,"2.678176e-12");
  const mu=f(pre.identity.exact_parameter_increment);
  check("actual parameter shift inside rounded limit",mu.abs().lt("9e-16"));
  const eta=f("1e-9"),etaNew=f("9.99999e-10");
  check("new full real box contained",etaNew.le(eta.sub(mu.abs())));
  const S0=f("1/512"),R=f("1/1048576"),S=S0.sub(R),wide=f("5/2048");
  check("real w bounds cover inverse circle",S.add(R).le(wide));
  check("J image inside old full strip",S.add(w).lt(S0));
  const da=upper(pre.exact_quadratic_target.old_full_rotation_difference).abs();
  const deltaOmega=f("18e-12");
  check("rotation angle change using pi<4",da.mul(8).le(deltaOmega));
  const U0=f("1.7e-10");check("old whole-box periodic displacement",upper(half.uniform_u).mul(2).le(U0));
  const L=f("1.000001");check("old whole-box full spatial derivative",upper(half.J).pow(2).le(L));
  const P0=upperCheck("old complete P",full.P,"0.010753");
  const Q0=upperCheck("old complete Q",full.Q,"0.333126");
  const T0=upperCheck("old complete T",full.T,"0.118326");
  const B0=upperCheck("old complete B",full.B,"0.005574");
  const sig0=f("0.00223169");check("old genuine twist lower",sig0.le(lower(full.twist_lower)));
  check("continued fraction bound",pre.exact_quadratic_target.all_positive_partial_quotients_at_most===8 &&
    pre.exact_quadratic_target.full_return_small_divisor_K==="5/2");
  const D=f(1).sub(m1),self=deltaOmega.add(U0).add(w.mul(2));
  check("whole-box J inverse self-map",self.lt(R));check("whole-box J inverse contraction",m1.lt(1));
  const V=self.div(D);check("refined output image inside inverse circle",V.lt(R));
  check("wide finite derivative norms cover output image",S.add(V).lt(wide));
  const Jx=L.mul(f(1).add(m1)).div(D);
  const P=P0.div(D);
  const Q=Q0.mul(f(1).add(m1)).add(m2.mul(Jx).mul(P)).div(D);
  const T=T0.add(m2.mul(P.pow(2))).div(D);
  const B=B0.mul(f(1).add(m1).pow(2)).add(L.mul(m2)).add(m2.mul(Jx.pow(2))).div(D);
  const twistFee=Q0.mul(w).add(mu.abs().mul(T0)).add(P0.mul(m1).div(D));
  const sigma=sig0.sub(twistFee);check("new genuine twist positive",f(0).lt(sigma));
  check("actual two half-return composition domain",S.add(epsh).lt(wide));
  const eps=epsh.mul(2),K=f("5/2"),s0=f("3/2048"),delta=f("1/4096");
  const La=f(4).div(sigma),Astar=f(2).mul(f(1).add(P.mul(La))),LH=f(2).mul(K).mul(Astar);
  const C=K.mul(Astar).add(B.mul(LH.pow(2)).div(2)).add(Q.mul(LH).mul(La)).add(T.mul(La.pow(2)).div(2));
  const Z=Q.mul(LH).add(T.mul(La)).add(P.mul(LH));
  const cuts=[f(1).div(C.mul(32)),f(1).div(LH.mul(4)),sigma.div(Z.mul(8))];
  const threshold=cuts.reduce((a,b)=>a.lt(b)?a:b).mul(delta.pow(2));
  const moveP=La.mul(eps).mul(2),moveH=LH.mul(eps).mul(2).div(delta);
  const gates={error_smallness:eps.le(threshold),parameter_margin:moveP.lt(etaNew),analytic_domain_margin:s0.add(moveH).lt(S)};
  function record(x){return {exact_fraction:x.str(),lower_decimal:x.decimal(45,false),upper_decimal:x.decimal(45,true)};}
  return {
    kind:"actual_exact_rational_post_prenewton_R31",
    complete:true,arithmetic:"JavaScript BigInt exact reduced fractions; every displayed decimal is directed",
    true_input_gates:tests,all_true_input_gates_passed:tests.every(x=>x.passed),
    exact_new_parameter:pre.identity.proposed_exact_parameter,
    identity:{retarget_descriptor_sha256:pre.identity.retarget_descriptor_sha256,
      original_endpoint_path:pre.identity.original_endpoint_path,original_endpoint_sha256:pre.identity.original_endpoint_sha256,
      original_H_path:pre.identity.original_H_path,original_H_sha256:pre.identity.original_H_sha256,
      old_exact_parameter:pre.identity.old_exact_parameter,exact_parameter_increment:pre.identity.exact_parameter_increment,
      exact_new_conjugacy:pre.identity.exact_new_conjugacy},
    exact_target:{prefix,periodic_tail:[1],matrix:[[cp.toString(),cq.toString()],[cr.toString(),ct.toString()]],
      primitive_polynomial:[aa.toString(),bb.toString(),cc.toString()],discriminant:"5",K:"5/2"},
    old_full_domain:S0.str(),new_full_domain:S.str(),remaining_parameter_radius:etaNew.str(),
    bounds:Object.fromEntries(Object.entries({P,Q,T,B,twist_lower:sigma,epsilon:eps,K,V,Jx,twistFee}).map(([k,v])=>[k,record(v)])),
    R31:{gates,arithmetic_gates_passed:Object.values(gates).every(Boolean),
      epsilon_threshold:record(threshold),parameter_movement:record(moveP),conjugacy_movement:record(moveH),
      conjugacy_derivative_movement:record(moveH.div(delta)),
      final_analytic_width:record(s0.sub(delta.mul(4))),
      La:record(La),Astar:record(Astar),LH:record(LH),C:record(C),Z:record(Z)},
    actual_R31_accepted:Object.values(gates).every(Boolean),
    actual_flow_data_not_resampled:true,python_post_runner_executed:false,
    no_full_PDE_inverse_or_exact_isometric_surface_inferred:true
  };
}

function splitWienerBudget(summary, pre, localJ, center) {
  const baseline=rationalPostPrenewton(summary,pre);
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;}
  class F {
    constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
    static read(s){if(s instanceof F)return s;s=String(s).trim();if(s.includes("/")){let [n,d]=s.split("/");return new F(n,d);}
      let m=s.match(/^([+-]?)(\d+)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/);if(!m)throw Error("invalid exact decimal "+s);
      let n=BigInt(m[2]+(m[3]||""))*(m[1]==="-"?-1n:1n),e=Number(m[4]||0)-(m[3]||"").length;
      return e>=0?new F(n*10n**BigInt(e)):new F(n,10n**BigInt(-e));}
    add(y){y=F.read(y);return new F(this.n*y.d+y.n*this.d,this.d*y.d);}
    sub(y){y=F.read(y);return new F(this.n*y.d-y.n*this.d,this.d*y.d);}
    mul(y){y=F.read(y);return new F(this.n*y.n,this.d*y.d);}
    div(y){y=F.read(y);return new F(this.n*y.d,this.d*y.n);}
    abs(){return new F(this.n<0n?-this.n:this.n,this.d);}
    pow(k){return new F(this.n**BigInt(k),this.d**BigInt(k));}
    lt(y){y=F.read(y);return this.n*y.d<y.n*this.d;}
    le(y){y=F.read(y);return this.n*y.d<=y.n*this.d;}
    str(){return this.n.toString()+"/"+this.d.toString();}
    decimal(digits=30,up=false){let scale=10n**BigInt(digits),num=this.n*scale;let q=num/this.d,rem=num%this.d;if(up&&rem>0n)q++;if(!up&&rem<0n)q--;
      let neg=q<0n;if(neg)q=-q;let s=q.toString().padStart(digits+1,"0");return (neg?"-":"")+s.slice(0,-digits)+"."+s.slice(-digits);}
  }
  const f=F.read;
  function ball(s){s=String(s).trim();if(s[0]!=="["){let x=f(s);return [x,x];}
    let m=s.match(/^\[\s*(.*?)\s*\+\/-\s*(.*?)\s*\]$/);if(!m)throw Error("unsupported display ball "+s);
    const mid=f(m[1]),rad=f(m[2]);return [mid.sub(rad),mid.add(rad)];}
  function upper(r){return ball(r.upper)[1];}
  function lower(r){return ball(r.lower)[0];}

  const tests=[];
  function check(name,passed){tests.push({name,passed:!!passed});if(!passed)throw Error(name);}
  function record(x){return {exact_fraction:x.str(),lower_decimal:x.decimal(45,false),upper_decimal:x.decimal(45,true)};}
  const gx=summary.g0.summary,old=summary.endpoint,half=old.sharp_half;
  const A=upper(gx.A),E=upper(gx.E),R=f("1/1024"),SX=f("3/1024");
  check("same complete original g0 index",summary.g0.sha256===localJ.original_verified_index.sha256 &&
    localJ.descriptor_sha256===pre.identity.retarget_descriptor_sha256 && localJ.proved);
  check("same complete global local-integral budget",localJ.complete_global_budget_transformation &&
    localJ.original_leaf_count===summary.g0.leaves && summary.g0.completed_segments===550);
  const r72=E.mul(f(1).add(A.div(R))).add(A.pow(3).div(f(2).mul(R.sub(A).pow(2))));
  check("explicit actual R72 remainder",r72.lt("3.779199e-17"));
  const Jtotal=upper(localJ.correction_A_inner).add(upper(localJ.full_remaining_local_fee));
  check("direct Wiener local-integral fee",Jtotal.lt("2.807274e-15"));
  const t=f("17/8192"),iv=f("1/400000"),gapX=SX.sub(t).sub(iv);
  const selfSquare=A.pow(2).mul(f(1).add(f(2).div(gapX)));
  const derivativeSquare=A.pow(2).div(gapX.pow(2)).mul(f(1).add(f(1).div(gapX)));
  check("true X inverse self-map squared",selfSquare.lt(iv.pow(2)));
  check("true X inverse derivative below 1/500 squared",derivativeSquare.lt(f("1/500").pow(2)));
  check("true G derivative covers inverse image",t.add(iv).lt(lower(half.proved_half_derivative_width)));
  const FrefPrime=upper(half.J).div(f(1).sub("1/500"));
  check("actual Fref derivative below 1.003",FrefPrime.lt("1.003"));
  const h2=upper(old.finite_H_constants.Hsecond),Lprime=f(1).add(h2).mul(FrefPrime);
  check("normalized reference L first derivative below 17",Lprime.lt(17));
  check("old H derivative domain covers reference composition",
    t.add(iv).add(upper(half.uniform_u)).lt(lower(half.outer_width).add(lower(old.finite_H_constants.radius))));
  const S=f(baseline.new_full_domain),w=f("9e-12"),m1=f("1.2e-9");
  const gapL=t.sub(S).sub("1e-9"),Lthird=f(34).div(gapL.pow(2));
  check("complete L third derivative below 1e10",Lthird.lt("1e10"));
  const W0=upper(center.chosen_coordinate_norms[0]);
  check("actual chosen W0 norm",W0.lt("3.017e-11"));
  const hSquare=f(1).add(f(2).div(SX.sub(S).sub(w)));
  check("actual sup-to-Wiener Hardy factor below 46",hSquare.lt(f(46).pow(2)));
  check("true X and selected Z interpolation inside Fref domain",
    S.add(w).add(A.mul(46)).lt(t) && S.add(w).add(W0).lt(t));
  const selectionFee=upper(center.coefficient_selection_fees[0]);
  check("actual midpoint fee retained",selectionFee.lt("1e-80"));
  const normalizedTaylor=f("1e10").mul(W0.pow(3)).div(6);
  const originalTaylor=upper(center.complete_Taylor_fees[0]);
  const extra=upper(pre.complete_finite_quadratic_residual)
    .add(upper(pre.complete_finite_composition_Taylor_fee))
    .add(upper(pre.true_first_parameter_source_fee))
    .add(upper(pre.whole_box_second_parameter_Taylor_fee))
    .add(normalizedTaylor).add(originalTaylor);
  check("real whole-box endpoint parameter bound",upper(old.uniform_first_and_second_endpoint_bounds[0]).lt("0.007"));
  const rawPprime=f("0.007").div(f(2).mul(lower(half.outer_width).sub(t)));
  check("parameter spatial derivative below 15",rawPprime.lt(15));
  const mu=f(pre.identity.exact_parameter_increment);
  const muLip=mu.abs().mul(f(1000).mul("0.007").mul(17).add(60));
  check("real parameter Lip reserve below 1e-10",muLip.lt("1e-10"));
  const invH=upper(pre.exact_new_conjugacy_derivative_inverse),kapH=upper(pre.local_inverse_kappa);
  check("finite error inverse factor below 4",invH.div(f(1).sub(kapH.div(2))).lt(4));
  check("H inverse second derivative below 1000",f(4).pow(3).mul(h2).lt(1000));
  const factor=f("1.004");check("complete reference factor with parameter reserve",FrefPrime.add(muLip).lt(factor));
  const halfError=factor.mul(Jtotal.add(r72.add(selectionFee).mul(46))).add(extra.mul(4)).div(f(1).sub(m1));
  const r86=upper(center.coordinate_budget.tails[0]).add(upper(center.coordinate_budget.source_error_fees[0])).add(selectionFee);
  const alternateHalf=factor.mul(Jtotal.add(r86.mul(46))).add(extra.mul(4)).div(f(1).sub(m1));
  const eps=halfError.mul(2),P=f(baseline.bounds.P.exact_fraction),Q=f(baseline.bounds.Q.exact_fraction),
    T=f(baseline.bounds.T.exact_fraction),B=f(baseline.bounds.B.exact_fraction),
    sigma=f(baseline.bounds.twist_lower.exact_fraction),K=f("5/2");
  const s0=f("15/8192"),delta=f("11/32768"),eta=f(baseline.remaining_parameter_radius);
  check("center true half-square fits start strip",s0.add(halfError).lt(S));
  check("strict KAM width nesting",f(0).lt(delta)&&delta.lt(s0.div(4))&&s0.lt(S));
  const La=f(4).div(sigma),Astar=f(2).mul(f(1).add(P.mul(La))),LH=f(2).mul(K).mul(Astar);
  const C=K.mul(Astar).add(B.mul(LH.pow(2)).div(2)).add(Q.mul(LH).mul(La)).add(T.mul(La.pow(2)).div(2));
  const Z=Q.mul(LH).add(T.mul(La)).add(P.mul(LH));
  const cuts=[f(1).div(C.mul(32)),f(1).div(LH.mul(4)),sigma.div(Z.mul(8))];
  const threshold=cuts.reduce((a,b)=>a.lt(b)?a:b).mul(delta.pow(2));
  const moveP=La.mul(eps).mul(2),moveH=LH.mul(eps).mul(2).div(delta);
  const gates={error_smallness:eps.le(threshold),parameter_margin:moveP.lt(eta),analytic_domain_margin:s0.add(moveH).lt(S)};
  return {
    kind:"actual_exact_rational_split_Wiener_R31_budget",complete_arithmetic:true,
    baseline_input_gates:baseline.true_input_gates,split_input_gates:tests,
    all_scalar_and_domain_gates_passed:baseline.all_true_input_gates_passed&&tests.every(x=>x.passed),
    identity:baseline.identity,exact_target:baseline.exact_target,
    scalar_center_fields_read_from_original_gzip:true,local_Wiener_fee_not_multiplied_by_Hardy:true,
    R72_remainder_computed_from_A_E_R_not_subtracted_from_total:true,
    whole_real_parameter_radius:baseline.remaining_parameter_radius,
    new_full_domain:baseline.new_full_domain,KAM_start_width:s0.str(),KAM_width_step:delta.str(),
    split_terms:Object.fromEntries(Object.entries({r72,Jtotal,selfSquare,derivativeSquare,FrefPrime,Lprime,Lthird,W0,
      selectionFee,normalizedTaylor,originalTaylor,extra,muLip,halfError,r86,alternateHalf}).map(([k,v])=>[k,record(v)])),
    actual_inputs:Object.fromEntries(Object.entries({epsilon:eps,P,Q,T,B,twist_lower:sigma,K}).map(([k,v])=>[k,record(v)])),
    R31:{gates,arithmetic_gates_passed:Object.values(gates).every(Boolean),
      epsilon_threshold:record(threshold),parameter_movement:record(moveP),conjugacy_movement:record(moveH),
      conjugacy_derivative_movement:record(moveH.div(delta)),final_analytic_width:record(s0.sub(delta.mul(4))),
      La:record(La),Astar:record(Astar),LH:record(LH),C:record(C),Z:record(Z)},
    all_actual_arithmetic_R31_gates_passed:Object.values(gates).every(Boolean),
    acceptance_requires_separate_split_Wiener_factorization_proof:true,
    no_full_PDE_inverse_or_exact_isometric_surface_inferred:true
  };
}

const specs=[
 ["notes/2026-11-12-complete-flow-43301401638-arithmetic-summary.json","f25a3692b36390b3ae8dd7699d4e0ec0c2e74561ac238b11352f1d532a8bfc52"],
 ["data/phase_ring_continuation/step5_half_prenewton_43308150283/report.json","030cf8444f5a0cc5058e7ce056b2b310328e7d78a842582273ffb70d2f6f720a"],
 ["data/phase_ring_continuation/step5_local_J0_symmetric_ci/report.json.gz","f77211c4d7710dae2a737558ceae980c4d780666d4f91f2a730004981802d301"],
 ["data/phase_ring_continuation/step5_complete_flow_ci_43301401638/actual_endpoint.json.gz","f8d958ce1af4cac5d4053d8c7569d33c049a917d84094e55944842fad4228328"]
];
const docs=specs.map(([file,digest])=>{
 const raw=fs.readFileSync(file);
 if(crypto.createHash("sha256").update(raw).digest("hex")!==digest)throw Error("input SHA mismatch: "+file);
 return JSON.parse((file.endsWith(".gz")?zlib.gunzipSync(raw):raw).toString("utf8"));
});
const [summary,pre,J,endpoint]=docs;
if(endpoint.descriptor_sha256!==J.descriptor_sha256 || endpoint.descriptor_sha256!==pre.identity.retarget_descriptor_sha256)
 throw Error("original reports describe different actual geometric families");
const result=splitWienerBudget(summary,pre,J,endpoint.center_endpoint);
result.provenance={input_files:specs.map(([path,sha256])=>({path,sha256})),all_original_SHA256_verified:true,
 source_sha256:crypto.createHash("sha256").update(fs.readFileSync(new URL(import.meta.url))).digest("hex"),
 arithmetic_runtime:process.version,original_gzip_read:true,new_density_or_ODE_evaluation:false};
const output=process.argv[2]||"notes/2026-11-12-split-Wiener-R31-exact.json";
fs.mkdirSync(path.dirname(output),{recursive:true});fs.writeFileSync(output,JSON.stringify(result,null,2)+"\n");
console.log(JSON.stringify({complete_arithmetic:result.complete_arithmetic,input_gates:result.baseline_input_gates.length+result.split_input_gates.length,
 gates:result.R31.gates,epsilon:result.actual_inputs.epsilon,threshold:result.R31.epsilon_threshold,output}));
