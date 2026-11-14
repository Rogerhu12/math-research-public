#!/usr/bin/env node
/**
 * Exact rational fees for the complete stream antiderivative and an exact
 * free-Airy compact-support benchmark.  No new geometric bound is claimed.
 * The core runBudget() can be executed in V8 without node imports.
 */
import fs from "node:fs";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";
import path from "node:path";

function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
class Q {
  constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");
    if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
  static of(x){return x instanceof Q?x:new Q(x);}
  add(x){x=Q.of(x);return new Q(this.n*x.d+x.n*this.d,this.d*x.d);}
  sub(x){x=Q.of(x);return new Q(this.n*x.d-x.n*this.d,this.d*x.d);}
  mul(x){x=Q.of(x);return new Q(this.n*x.n,this.d*x.d);}
  div(x){x=Q.of(x);return new Q(this.n*x.d,this.d*x.n);}
  pow(k){k=Number(k);if(k<0)return new Q(this.d,this.n).pow(-k);
    return new Q(this.n**BigInt(k),this.d**BigInt(k));}
  lt(x){x=Q.of(x);return this.n*x.d<x.n*this.d;}
  le(x){x=Q.of(x);return this.n*x.d<=x.n*this.d;}
  eq(x){x=Q.of(x);return this.n===x.n&&this.d===x.d;}
  json(){return [String(this.n),String(this.d)];}
}
function floorDiv(n,d){let q=n/d;return n<0n&&n%d!==0n?q-1n:q;}
function decimal(q,digits=18,up=false){q=Q.of(q);const S=10n**BigInt(digits);
  let a=up?-floorDiv(-q.n*S,q.d):floorDiv(q.n*S,q.d);
  const neg=a<0n;if(neg)a=-a;const s=a.toString().padStart(digits+1,"0");
  return (neg?"-":"")+s.slice(0,-digits)+"."+s.slice(-digits);}
function isqrt(n){if(n<0n)throw Error("negative square root");if(n<2n)return n;
  let x=1n<<BigInt((n.toString(2).length+1)>>1);
  for(;;){const y=(x+n/x)>>1n;if(y>=x)return x;x=y;}}
function sqrtBounds(q,digits=70){q=Q.of(q);if(q.n<0n)throw Error("negative radicand");
  const S=10n**BigInt(digits), k=isqrt(q.n*S*S/q.d);
  return [new Q(k,S),new Q(k+1n,S)];}
function boundRecord(q){return {exact:q.json(),lower_decimal:decimal(q,24),
  upper_decimal:decimal(q,24,true)};}

function positiveAiryFundamentals(z,N=40){
  // f(0)=1,f'(0)=0; g(0)=0,g'(0)=1; h''=z h.
  // Only g and f' are needed.  All terms are positive for z>0.
  if(!new Q(0n).lt(z)||N<2)throw Error("invalid positive-series input");
  const z3=z.pow(3);
  let fk=new Q(1n),gk=z,g=z,fp=new Q(0n),dfLast=new Q(0n);
  for(let k=1;k<=N;k++){
    fk=fk.mul(z3).div(new Q(BigInt(3*k*(3*k-1))));
    gk=gk.mul(z3).div(new Q(BigInt((3*k+1)*(3*k))));
    dfLast=fk.mul(new Q(BigInt(3*k))).div(z);
    fp=fp.add(dfLast);g=g.add(gk);
  }
  const rg=z3.div(new Q(BigInt((3*N+4)*(3*N+3))));
  const rf=z3.div(new Q(BigInt((3*N)*(3*N+2))));
  if(!rg.lt(1n)||!rf.lt(1n))throw Error("unpaid positive series tail");
  // The ratios decrease after the retained last terms.
  const tg=gk.mul(rg).div(new Q(1n).sub(rg));
  const tf=dfLast.mul(rf).div(new Q(1n).sub(rf));
  return {gLower:g,gUpper:g.add(tg),fpLower:fp,fpUpper:fp.add(tf),
          gTail:tg,fpTail:tf,gRatio:rg,fpRatio:rf,terms:N};
}

export function runBudget(){
  const checks=[];
  function check(name,ok){checks.push({name,passed:!!ok});if(!ok)throw Error(name);}
  const qLower=new Q(243n,25n),qUpper=new Q(10n);
  const H=new Q(7n,2000n),Ai0Lower=new Q(7n,20n);
  const stream=[];
  for(const K of [64,128,256,512,1024]){
    const J=K+1;
    const c0=new Q(1n).div(qLower.mul(new Q(BigInt(4*J))));
    // 2*pi^2/3 < 20/3, with pi^2<10.
    const c2=c0.mul(new Q(20n,3n));
    const hsHigh=sqrtBounds(new Q(40n,BigInt(3*(J-1))))[1];
    const c2High=c0.mul(new Q(10n,3n).add(hsHigh));
    const meanSq=new Q(2n,BigInt(3*(J-1)**3));
    const meanUpper=sqrtBounds(meanSq)[1];
    check("high-restricted Hilbert-Schmidt refinement at K="+K,c2High.lt(c2));
    check("stream fee improves the unlocalized inverse at K="+K,
          c0.lt(new Q(1n).div(qLower.mul(4n))));
    stream.push({K,input_first_index:J,
      complete_D_inverse_fee_C0:boundRecord(c0),
      complete_D_inverse_fee_C2:boundRecord(c2),
      high_restricted_commutator_factor_C2_upper:boundRecord(hsHigh),
      high_restricted_D_inverse_fee_C2:boundRecord(c2High),
      fee_if_an_independent_B_operator_bound_is_known:{
        B_operator_norm_coefficient:boundRecord(c0),
        extra_C2_coefficient:boundRecord(c0.mul(hsHigh))},
      mean_row_fee_C2_upper:boundRecord(meanUpper),
      retained_outputs:"all k != 0, both signs; k=0 is the separate mean row",
      strong_right_weighted_fee:"C0+(2*pi^2/3)*C2 < C0+(20/3)*C2"});
  }
  const cases=[
    [64,new Q(2n,3n),new Q(65n,100n)],
    [128,new Q(16n,15n),new Q(36n,100n)],
    [256,new Q(5n,3n),new Q(16n,100n)],
    [512,new Q(8n,3n),new Q(3n,100n)],
    [1024,new Q(21n,5n),new Q(2n,1000n)]
  ];
  const benchmark=[];
  for(const [K,Z,claimed] of cases){
    const J=K+1,lambdaUpper=qUpper.mul(new Q(BigInt(4*J)));
    check("complete upper Airy coordinate at K="+K,
          H.pow(3).mul(lambdaUpper.pow(2)).lt(Z.pow(3)));
    const f=positiveAiryFundamentals(Z,40);
    check("positive g and fprime at K="+K,
          new Q(0n).lt(f.gLower)&&new Q(0n).lt(f.fpLower));
    const product=f.gUpper.mul(f.fpUpper);
    const sqrtLower=sqrtBounds(new Q(1n).add(new Q(1n).div(product)))[0];
    const gapSq=Ai0Lower.pow(2).mul(2n).mul(sqrtLower.sub(1n));
    const gapLower=sqrtBounds(gapSq)[0];
    check("positive exact gap lower bound at K="+K,new Q(0n).lt(gapSq));
    check("stated free-model exclusion at K="+K,claimed.lt(gapLower));
    benchmark.push({
      K,input_first_index:J,lambda_upper:boundRecord(lambdaUpper),
      actual_H:boundRecord(H),safe_Z_upper:boundRecord(Z),
      fundamental_g_upper:boundRecord(f.gUpper),
      fundamental_fprime_upper:boundRecord(f.fpUpper),
      complete_positive_series_g_tail:boundRecord(f.gTail),
      complete_positive_series_fprime_tail:boundRecord(f.fpTail),
      gap_square_lower:boundRecord(gapSq),gap_lower:boundRecord(gapLower),
      simple_strict_lower:boundRecord(claimed),
      scope:"exact free C0=diag(1,y) model, same decaying-Ai two root traces; no actual-DN exclusion"});
  }
  return {
    kind:"complete-stream-antiderivative-and-free-Airy-compact-benchmark",
    method:"exact BigInt rational sums, decreasing-ratio tails, integer square roots",
    proved_math_fee_table:true,proved_new_geometry:false,
    proved_actual_wide_cap_gap:false,
    inputs:{
      canonical_q_strict_lower:qLower.json(),canonical_q_strict_upper:qUpper.json(),
      free_Airy_Ai0_strict_lower:Ai0Lower.json(),covered_chart_H:H.json(),
      q_source:"R99; same eta=1e-9 object",
      q_summary_path:"notes/2026-11-12-ci-canonical-v1-scaled-Wiener-summary.json",
      q_summary_sha256:"c0050bf6f15666f1b0283d7d232c10a167d08a4bb69e42c6cc5653dc51c94c3b",
      actual_frequency_record:{
        ball:"[9.72096290 +/- 5.78e-9]",
        lower:"[9.7209629014673150163017290026346018 +/- 1.61e-35]",
        upper:"[9.7209629057729377912822066321041348 +/- 3.09e-35]",
        mid_float:9.720962903620126,radius_upper_float:2.152811387490239e-9},
      Airy_initial_source:"2026-11-13-R109-paired-E-and-short-collar-gap.md, exact Gamma integral proof",
      chart_source:"2026-11-12-canonical-far-chart-complete.md, full far aggregate SHA256 5fe35e8d9c9e8b53875e242b1fd11995a805c382d95de929593c8f2fd92210b3"},
    stream,free_model_benchmark:benchmark,checks,
    limitations:[
      "No geometric source symbol C0/C2 is newly bounded here.",
      "The free-model compact lower bounds are not lower bounds for the actual DN map.",
      "A noncompact exterior match may have zero free-model gap.",
      "The regular mean and root mean remain separate full-network channels."
    ]
  };
}

if(process.argv[1]&&fileURLToPath(import.meta.url)===path.resolve(process.argv[1])){
  const out=process.argv[2];if(!out)throw Error("usage: node source.mjs output.json");
  const result=runBudget();
  result.execution="native Node exact BigInt entry";
  result.source_sha256=crypto.createHash("sha256").update(fs.readFileSync(fileURLToPath(import.meta.url))).digest("hex");
  fs.mkdirSync(path.dirname(out),{recursive:true});
  fs.writeFileSync(out,JSON.stringify(result,null,2)+"\n");
  console.log(JSON.stringify({checks:result.checks.length,passed:true,
    source_sha256:result.source_sha256,
    gap_lower_K256:result.free_model_benchmark.find(x=>x.K===256).gap_lower.lower_decimal}));
}
