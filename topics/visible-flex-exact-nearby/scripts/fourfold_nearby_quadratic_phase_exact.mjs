#!/usr/bin/env node
// R102: all arithmetic comparisons use BigInt reduced fractions.
// Run from topics/visible-flex-exact-nearby; no field or ODE samples are recomputed.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

function quadraticPhaseEnumeration(betaDoc, inclusionDoc, preDoc) {
  function gcd(a,b){if(a<0n)a=-a;if(b<0n)b=-b;while(b){[a,b]=[b,a%b];}return a;}
  class F{
    constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}let g=gcd(n,d);this.n=n/g;this.d=d/g;}
    static read(s){if(s instanceof F)return s;s=String(s);if(s.includes("/")){let [n,d]=s.split("/");return new F(n,d);}let m=s.match(/^([+-]?)(\d+)(?:\.(\d*))?(?:e([+-]?\d+))?$/i);if(!m)throw Error("bad rational "+s);let n=BigInt(m[2]+(m[3]||""))*(m[1]==="-"?-1n:1n),e=Number(m[4]||0)-(m[3]||"").length;return e>=0?new F(n*10n**BigInt(e)):new F(n,10n**BigInt(-e));}
    add(y){y=F.read(y);return new F(this.n*y.d+y.n*this.d,this.d*y.d);}
    sub(y){y=F.read(y);return new F(this.n*y.d-y.n*this.d,this.d*y.d);}
    mul(y){y=F.read(y);return new F(this.n*y.n,this.d*y.d);}
    div(y){y=F.read(y);return new F(this.n*y.d,this.d*y.n);}
    pow(k){return new F(this.n**BigInt(k),this.d**BigInt(k));}
    abs(){return new F(this.n<0n?-this.n:this.n,this.d);}
    lt(y){y=F.read(y);return this.n*y.d<y.n*this.d;}
    le(y){y=F.read(y);return this.n*y.d<=y.n*this.d;}
    str(){return this.n+"/"+this.d;}
    decimal(k=25,up=false){const scale=10n**BigInt(k);let num=this.n*scale,z=num/this.d,rem=num%this.d;if(up&&rem>0n)z++;if(!up&&rem<0n)z--;let neg=z<0n;if(neg)z=-z;let s=z.toString().padStart(k+1,"0");return (neg?"-":"")+s.slice(0,-k)+"."+s.slice(-k);}
  }
  const f=F.read;
  const min=(a,b)=>a.lt(b)?a:b,max=(a,b)=>a.lt(b)?b:a;
  function isqrt(n){if(n<0n)throw Error("negative sqrt");if(n<2n)return n;let x=1n<<BigInt((n.toString(2).length+1)>>1);while(true){let y=(x+n/x)>>1n;if(y>=x)return x;x=y;}}
  function atanInverse(m,N){let sum=f(0);let power=BigInt(m);for(let n=0;n<N;n++){sum=sum.add(new F(n%2?-1n:1n,BigInt(2*n+1)*power));power*=BigInt(m)*BigInt(m);}const rem=new F(1n,BigInt(2*N+1)*power);return N%2?[sum.sub(rem),sum]:[sum,sum.add(rem)];}
  const p5=atanInverse(5,80),p239=atanInverse(239,24);
  const pi=[p5[0].mul(16).sub(p239[1].mul(4)),p5[1].mul(16).sub(p239[0].mul(4))];
  const A=1323907691653283951n,B=1460270480137213085n,C=402669666587037055n;
  if(B*B-4n*A*C!==5n)throw Error("wrong discriminant");
  const scale=10n**90n,sq=isqrt(5n*scale*scale);
  if(!(sq*sq<5n*scale*scale&&(sq+1n)*(sq+1n)>5n*scale*scale))throw Error("sqrt interval");
  const alphaDen=2n*A*scale,alphaLo=B*scale-sq-1n,alphaHi=B*scale-sq;
  const alpha=[new F(alphaLo,alphaDen),new F(alphaHi,alphaDen)];
  const sqrt5=[new F(sq,scale),new F(sq+1n,scale)];
  const beta=[f(betaDoc.beta.lower_exact),f(betaDoc.beta.upper_exact)];
  if(!betaDoc.complete)throw Error("the original beta certificate is incomplete");
  const delta=f(inclusionDoc.exact_delta5),mu=f(preDoc.identity.exact_parameter_increment),eta=f("1e-9");
  if(preDoc.identity.old_exact_parameter!==inclusionDoc.exact_delta5)throw Error("geometric parameter center mismatch");
  const tube=inclusionDoc.beta_interval.map(f);
  if(!tube[0].lt(delta.sub(eta))||!delta.add(eta).lt(tube[1]))throw Error("the entire actual parameter tube is not in the beta certificate");
  if(!mu.abs().lt(eta))throw Error("preNewton parameter outside original tube");
  const prefix=[0,1,1,4,2,1,4,...Array(17).fill(1),8,1,1,7,3,7],Qcut=1n<<38n,near=32n;
  let pp=0n,p=1n,qq=1n,q=0n,convergents=[];
  for(let n=0;;n++){const a=BigInt(n<prefix.length?prefix[n]:1);let pn=a*p+pp,qn=a*q+qq;convergents.push({n,a,p:pn,q:qn,pm:p,qm:q});[pp,p]=[p,pn];[qq,q]=[q,qn];if(qn>Qcut)break;}
  let ma=1n,mb=0n,mc=0n,md=1n;
  for(const digit of prefix){const x=BigInt(digit);[ma,mb,mc,md]=[ma*x+mb,ma,mc*x+md,mc];}
  if(ma*md-mb*mc!==1n || mc*mc-md*md-mc*md!==A ||
     2n*ma*mc-2n*mb*md-ma*md-mb*mc!==B ||
     ma*ma-mb*mb-ma*mb!==C)throw Error("exact continued-fraction polynomial identity failed");
  if(prefix.slice(1).some(x=>x<1||x>8) ||
     JSON.stringify(prefix)!==JSON.stringify(preDoc.exact_quadratic_target.prefix))throw Error("continued-fraction source identity mismatch");
  const phiHi=sqrt5[1].add(1).div(2),mapHi=f(ma.toString()).mul(phiHi).add(mb.toString()).div(f(mc.toString()).mul(phiHi).add(md.toString()));
  if(!mapHi.lt(new F(B,2n*A)))throw Error("target is not the minus root");
  const accepted=[],bad=[],seen=new Set();let latticeChecks=0,parityCandidates=0,nearCandidates=0;
  let minimum=null,minimumRow=null;
  const targetMargin=f("1/10");
  for(let n=0;n<convergents.length-1;n++){
    const cn=convergents[n],nx=convergents[n+1];
    const lo=cn.q>2n?cn.q:2n,hi=nx.q<Qcut?nx.q:Qcut;
    if(lo>=hi)continue;
    for(let a=-40;a<=40;a++)for(let b=-32;b<=32;b++){
      latticeChecks++;
      const qv=BigInt(a)*cn.q+BigInt(b)*cn.qm,pv=BigInt(a)*cn.p+BigInt(b)*cn.pm;
      if(qv<lo||qv>=hi||(qv&1n)!==0n||(pv&1n)===0n)continue;
      parityCandidates++;
      const eLo=qv*qv*alphaLo-pv*qv*alphaDen,eHi=qv*qv*alphaHi-pv*qv*alphaDen;
      if(eLo>near*alphaDen||eHi< -near*alphaDen)continue;
      const key=qv+":"+pv;if(seen.has(key))throw Error("candidate duplicate");seen.add(key);nearCandidates++;
      const e=[new F(eLo,alphaDen),new F(eHi,alphaDen)];
      const products=[pi[0].mul(e[0]).div(2),pi[0].mul(e[1]).div(2),pi[1].mul(e[0]).div(2),pi[1].mul(e[1]).div(2)];
      const phase=[beta[0].add(products.reduce(min)),beta[1].add(products.reduce(max))];
      const distance=phase[0].lt(0)?(f(0).lt(phase[1])?f(0):phase[1].abs()):phase[0];
      const norm=A*pv*pv-B*pv*qv+C*qv*qv;
      if(!norm||(norm&1n)===0n)throw Error("norm parity failed");
      const row={j:(qv/2n).toString(),p:pv.toString(),q:qv.toString(),basis_index:n,a,b,norm:norm.toString(),
        q_error:[e[0].str(),e[1].str()],scaled_phase_interval:[phase[0].str(),phase[1].str()],
        scaled_phase_decimal:[phase[0].decimal(20),phase[1].decimal(20,true)],distance_lower:distance.str()};
      accepted.push(row);
      if(minimum===null||distance.lt(minimum)){minimum=distance;minimumRow=row;}
      if(distance.lt(targetMargin))bad.push(row);
    }
  }
  const latticeStep=[pi[0].div(sqrt5[1].mul(2)),pi[1].div(sqrt5[0].mul(2))];
  let latticeGap=null,latticeClosest=null;
  for(let n=1;n<=101;n+=2){
    const point=[latticeStep[0].mul(n),latticeStep[1].mul(n)];
    const gap=beta[0].lt(point[1])?(point[0].lt(beta[1])?f(0):point[0].sub(beta[1])):beta[0].sub(point[1]);
    if(latticeGap===null||gap.lt(latticeGap)){latticeGap=gap;latticeClosest=n;}
  }
  if(!beta[1].lt(latticeStep[0].mul(103))||!f(0).lt(beta[0])||!latticeGap.lt(latticeStep[0].mul(103).sub(beta[1]))||!latticeGap.lt(beta[0]))throw Error("finite nearest-lattice proof missing");
  const tailCorrection=latticeStep[1].mul(new F(A*near*near,Qcut*Qcut));
  const tailMargin=latticeGap.sub(tailCorrection);
  const nonnear=pi[0].mul(near).div(2).sub(beta[1]);
  if(bad.length || !f("17/100").lt(minimum) || !f("17/100").lt(tailMargin) || !f("17/100").lt(nonnear))throw Error("whole pure phase gap failed");
  return {kind:"actual_BigInt_sparse_quadratic_full_phase_enumeration",complete_arithmetic:true,
    all_positive_frequency_pure_phase_gap_proved:true,uniform_scaled_phase_gap_lower:"17/100",
    actual_full_phase_remainder_not_proved:true,Maslov_phase_identification_not_supplied:true,full_PDE_inverse_not_inferred:true,
    residual_contract:{scaled_remainder_at_most:"7/100",joint_coefficient_and_remainder_allowance:"abs(beta_normal_form-beta_certificate)+j*abs(r_j)<=7/100",remaining_scaled_phase_margin:"1/10",divisor_lower:"1/(5*pi*j)",
      power_remainder_cutoff:"j >= max(J0,ceil((100*C/7)^(1/eta))) for |r_j| <= C/j^(1+eta)"},
    exact_quadratic:{A:A.toString(),B_signed:(-B).toString(),C:C.toString(),discriminant:"5",root:"minus",prefix,golden_tail:true,matrix:[[ma.toString(),mb.toString()],[mc.toString(),md.toString()]],matrix_polynomial_identity_verified:true},
    inputs:{beta_interval:beta.map(x=>x.str()),geometric_parameter_tube:[delta.sub(eta).str(),delta.add(eta).str()],
      beta_parameter_tube:tube.map(x=>x.str()),exact_preNewton_shift:mu.str(),pure_phase_only:true,full_normal_form_remainder_not_supplied:true},
    transcendental_enclosures:{pi:pi.map(x=>x.str()),sqrt5:sqrt5.map(x=>x.str()),alpha:alpha.map(x=>x.str()),
      Machin_arctangent_terms:[80,24],sqrt5_integer_scale_digits:90},
    complete_CF_basis_cover:{near_approximation_constant:Number(near),basis_a_bounds:[-40,40],basis_b_bounds:[-32,32],
      q_cutoff:Qcut.toString(),j_tail_start:(Qcut/2n).toString(),convergents:convergents.map(r=>Object.fromEntries(Object.entries(r).map(([k,v])=>[k,typeof v==="bigint"?v.toString():v]))),
      lattice_pairs_tested:latticeChecks,parity_and_denominator_candidates:parityCandidates,near_candidates:nearCandidates},
    distance_goal:targetMargin.str(),finite_minimum_lower:minimum.str(),finite_minimum_lower_decimal:minimum.decimal(25),finite_minimizer:minimumRow,exception_count:bad.length,exceptions:bad,
    tail:{nearest_positive_beta_lattice_index:latticeClosest,corresponding_dangerous_norm_Q:-latticeClosest,lattice_gap_lower:latticeGap.str(),lattice_gap_decimal:latticeGap.decimal(25),
      finite_A_correction_upper:tailCorrection.str(),finite_A_correction_decimal:tailCorrection.decimal(25,true),
      scaled_phase_margin_lower:tailMargin.str(),scaled_phase_margin_decimal:tailMargin.decimal(25),
      nonnear_phase_margin_lower:nonnear.str(),nonnear_phase_margin_decimal:nonnear.decimal(25)},
    finite_candidates:accepted};
}


function compactCandidateLedger(result) {
  return {kind:"complete_sparse_quadratic_phase_finite_candidate_ledger",
    columns:["j","odd_p","basis_index","a","b","norm_Q","scaled_phase_lower_decimal","scaled_phase_upper_decimal"],
    rows:result.finite_candidates.map(x=>[x.j,x.p,x.basis_index,x.a,x.b,x.norm,...x.scaled_phase_decimal])};
}

const specs=[
  [
    "notes/2026-11-12-beta-derivative-independent-cover-and-transfer-audit.json",
    "1047f423a77d07aa14093b17fcf28376243857d8bf738b5d62f65f0f3dea7923"
  ],
  [
    "notes/2026-11-12-step5-beta-parameter-inclusion.json",
    "f2505eaf23e4405af3f8efde6270e4e0405f538b930096556fe6789c3a58503e"
  ],
  [
    "data/phase_ring_continuation/step5_half_prenewton_43308150283/report.json",
    "030cf8444f5a0cc5058e7ce056b2b310328e7d78a842582273ffb70d2f6f720a"
  ]
];

const docs=specs.map(([file,expected])=>{
  const raw=fs.readFileSync(file);
  if(crypto.createHash("sha256").update(raw).digest("hex")!==expected)throw Error("input SHA differs: "+file);
  return JSON.parse(raw.toString("utf8"));
});
const result=quadraticPhaseEnumeration(...docs);
const ledgerText=JSON.stringify(compactCandidateLedger(result))+"\n";
const output=process.argv[2]||"notes/2026-11-12-R102-nearby-quadratic-phase.json";
const ledgerPath=output.replace(/\.json$/,"-candidates.json");
if(ledgerPath===output)throw Error("output must have .json extension");
result.complete_finite_candidate_ledger={path:ledgerPath,sha256:crypto.createHash("sha256").update(ledgerText).digest("hex"),rows:result.finite_candidates.length};
delete result.finite_candidates;
result.provenance={input_files:specs.map(([path,sha256])=>({path,sha256})),all_input_UTF8_SHA256_verified:true,
  source_sha256:crypto.createHash("sha256").update(fs.readFileSync(new URL(import.meta.url))).digest("hex"),
  runtime:process.version,all_comparisons:"exact reduced BigInt rational arithmetic",
  no_new_geometric_or_ODE_computation:true};
fs.mkdirSync(path.dirname(output),{recursive:true});
fs.writeFileSync(ledgerPath,ledgerText);
fs.writeFileSync(output,JSON.stringify(result,null,2)+"\n");
console.log(JSON.stringify({complete_arithmetic:true,all_positive_frequency_pure_phase_gap_proved:result.all_positive_frequency_pure_phase_gap_proved,
  candidates:result.complete_finite_candidate_ledger.rows,finite_minimum:result.finite_minimum_lower_decimal,tail_margin:result.tail.scaled_phase_margin_decimal,output}));
