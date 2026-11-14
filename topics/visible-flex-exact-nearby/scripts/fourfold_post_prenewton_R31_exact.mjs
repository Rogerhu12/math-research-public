#!/usr/bin/env node
// Exact BigInt rational replay. Run from topics/visible-flex-exact-nearby.
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
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
const specs=[
 ["notes/2026-11-12-complete-flow-43301401638-arithmetic-summary.json","f25a3692b36390b3ae8dd7699d4e0ec0c2e74561ac238b11352f1d532a8bfc52"],
 ["data/phase_ring_continuation/step5_half_prenewton_43308150283/report.json","030cf8444f5a0cc5058e7ce056b2b310328e7d78a842582273ffb70d2f6f720a"]
];
const inputs=specs.map(([file,digest])=>{
 const bytes=fs.readFileSync(file);
 if(crypto.createHash("sha256").update(bytes).digest("hex")!==digest)throw Error("input SHA mismatch: "+file);
 return JSON.parse(bytes.toString("utf8"));
});
const report=rationalPostPrenewton(...inputs);
report.provenance={arithmetic_runtime:"JavaScript BigInt exact rational replay",
 input_summary_path:specs[0][0],input_summary_sha256:specs[0][1],
 input_correction_path:specs[1][0],input_correction_sha256:specs[1][1],
 both_UTF8_input_bytes_SHA256_verified_before_execution:true};
const output=process.argv[2]||"notes/2026-11-12-post-prenewton-exact-rational-replay.json";
fs.mkdirSync(path.dirname(output),{recursive:true});
fs.writeFileSync(output,JSON.stringify(report,null,2)+"\n");
console.log(JSON.stringify({complete:report.complete,actual_R31_accepted:report.actual_R31_accepted,
 gates:report.R31.gates,epsilon_threshold:report.R31.epsilon_threshold,output}));
