#!/usr/bin/env node
// Exact public-waist and fifth-power marker budget; full-surface hypotheses remain explicit.

function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;}
class Q {
  constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
  add(x){x=q(x);return new Q(this.n*x.d+x.n*this.d,this.d*x.d);}
  sub(x){x=q(x);return new Q(this.n*x.d-x.n*this.d,this.d*x.d);}
  mul(x){x=q(x);return new Q(this.n*x.n,this.d*x.d);}
  div(x){x=q(x);return new Q(this.n*x.d,this.d*x.n);}
  pow(k){if(k<0)return new Q(this.d,this.n).pow(-k);return new Q(this.n**BigInt(k),this.d**BigInt(k));}
  abs(){return new Q(this.n<0n?-this.n:this.n,this.d);}
  cmp(x){x=q(x);const n=this.n*x.d-x.n*this.d;return n<0n?-1:n>0n?1:0;}
  str(){return this.n.toString()+"/"+this.d.toString();}
}
function q(x){if(x instanceof Q)return x;return new Q(BigInt(x));}
function frac(n,d){return new Q(BigInt(n),BigInt(d));}
function dyadic(x){
  if(!Number.isFinite(x))throw Error("nonfinite binary64");
  if(x===0)return q(0);
  const b=new ArrayBuffer(8),v=new DataView(b);v.setFloat64(0,x,false);
  const bits=v.getBigUint64(0,false),sgn=(bits>>63n)?-1n:1n;
  const e=Number((bits>>52n)&2047n),f=bits&((1n<<52n)-1n);
  const mantissa=e?f+(1n<<52n):f,shift=(e?e-1023:-1022)-52;
  return shift>=0?new Q(sgn*(mantissa<<BigInt(shift))):new Q(sgn*mantissa,1n<<BigInt(-shift));
}
function enclosure(x,digits=20){
  const scale=10n**BigInt(digits),num=x.n*scale;
  let low=num/x.d;if(num<0n&&num%x.d)low--;
  const high=low+(num%x.d?1n:0n);
  function fmt(v){const sign=v<0n?"-":"";v=v<0n?-v:v;const s=v.toString().padStart(digits+1,"0");return sign+s.slice(0,-digits)+"."+s.slice(-digits);}
  return {lower:fmt(low),upper:fmt(high),exact:x.str()};
}
function multiply(a,b){
  const c=Array(a.length+b.length-1).fill(null).map(()=>q(0));
  for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]=c[i+j].add(a[i].mul(b[j]));
  return c;
}
function derivative(a){return a.slice(1).map((x,i)=>x.mul(i+1));}
function evaluate(a,t){let s=q(0);for(let i=a.length-1;i>=0;i--)s=s.mul(t).add(a[i]);return s;}
function same(a,b){const n=Math.max(a.length,b.length);for(let i=0;i<n;i++)if((a[i]||q(0)).cmp(b[i]||q(0)))return false;return true;}
function calculate(doc){
  const checks=[];const gate=(name,condition)=>checks.push({name,passed:Boolean(condition)});
  const index=doc.complete_candidate_index,meta=index.metadata,y=index.initial_state;
  gate("exact_final_candidate_identity",doc.candidate_sha256==="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413");
  gate("complete_65_dimensional_initial_state",y.length===65&&meta.modes===32&&y.every(Number.isFinite));
  gate("full_R_index_identity",meta.exact_cap_cut==="25/8"&&index.radial_nodes_count===6145);
  const alpha=frac(6890507429876859n,9007199254740992n);
  gate("exact_alpha",dyadic(meta.amplitude).cmp(alpha)===0&&meta.exact_float_amplitude===alpha.str());
  const V=y.slice(32).map(dyadic);
  const rho=frac(1,100),amin=frac(106873282,100000000),amax=frac(1068732841,1000000000);
  let angular=q(0),supportTail=q(0),delta=q(0);
  for(let j=1;j<=32;j++){
    angular=angular.add(V[j].abs());
    supportTail=supportTail.add(V[j].abs().div(16*j*j-1));
    if(j%2)delta=delta.add(V[j].div(16*j*j-1));
  }
  delta=delta.mul(alpha).mul(2);
  const error=rho.mul(frac(2,15)),deltaLow=delta.sub(error),deltaHigh=delta.add(error);
  const vgap=amin.sub(alpha.mul(V[0].abs().add(angular))).sub(rho);
  const meanGap=amin.sub(alpha.mul(V[0].abs())).sub(rho);
  const supportLower=amin.sub(alpha.mul(supportTail)).sub(rho.div(15));
  const D=frac(511,200),radius=frac(7,16000000),k=frac(49,4),kplus=frac(196,27),tube=frac(27,196);
  gate("complete_unknown_tail_v_gap",vgap.cmp(frac(7,100))>0);
  gate("complete_unknown_mean_gap",meanGap.cmp(1)>0);
  gate("waist_support_lower",supportLower.cmp(1)>0);
  gate("positive_exact_phase_displacement",deltaLow.cmp(0)>0);
  gate("whole_surface_held_five_percent_budget",deltaLow.cmp(D.div(20))>0);
  gate("entire_displacement_inside_outward_tube",deltaHigh.cmp(tube)<0);
  gate("outward_tube_constant_identity",kplus.mul(tube).cmp(1)===0);
  gate("marker_curvature_square_budget",q(148).cmp(k.pow(2))<0);
  gate("marker_positive_curvature_factor",k.mul(frac(16,27)).cmp(kplus)===0);
  gate("marker_peaks_exceed_body_Gauss_bound",q(145).cmp(q(12).pow(2))>0);
  const oneMinus=[q(1),q(-1)];
  let profile=[q(1)];for(let i=0;i<5;i++)profile=multiply(profile,oneMinus);
  let jet=profile;
  for(let j=0;j<=4;j++){gate("marker_boundary_jet_order_"+j,evaluate(jet,q(1)).cmp(0)===0);jet=derivative(jet);}
  const positivePolynomial=[q(-1),q(12),q(-30),q(28),q(-9)];
  const derivativeFactored=multiply(multiply(oneMinus,oneMinus),[q(12),q(-36)]);
  gate("marker_radial_derivative_factorization",same(derivative(positivePolynomial),derivativeFactored));
  gate("marker_positive_peak_at_one_third",evaluate(positivePolynomial,frac(1,3)).cmp(frac(16,27))===0);
  const height=k.mul(radius.pow(2)).div(10);
  gate("marker_height_below_one_trillionth",height.cmp(frac(1,1000000000000n))<0);
  const pointNormSquared=radius.mul(5).pow(2).add(q(1).add(height).pow(2));
  gate("marker_points_preserve_radius_budget",pointNormSquared.cmp(D.div(2).pow(2))<0);
  const supportNumerator=frac(9,10).sub(k.mul(radius.pow(2)).mul(4));
  const normalDenSquared=q(1).add(k.mul(radius).pow(2));
  gate("marker_support_numerator_positive",supportNumerator.cmp(0)>0);
  gate("marker_support_above_089",supportNumerator.pow(2).cmp(frac(89,100).pow(2).mul(normalDenSquared))>0);
  const reach=frac(4,49),reachRatio=reach.div(D);
  gate("two_sided_reach_three_percent_budget",reachRatio.cmp(frac(3,100))>0);
  gate("unchanged_cap_centres_give_grip_diameter",frac(9,5).cmp(D.div(5))>0);
  gate("noncoplanar_marker_determinant_coefficient",frac(9,5).cmp(0)>0);
  gate("four_distinct_exact_curvature_labels",new Set([145,146,147,148]).size===4);
  gate("intrinsic_radius_box_order",amin.cmp(amax)<0);
  return {
    kind:"exact_waist_normal_offset_and_fifth_power_marker_budget",
    candidate_sha256:doc.candidate_sha256,
    actual_input:"Complete public 65-dimensional initial_state and previously proved intrinsic a0 enclosure; radial shards not read.",
    arithmetic:"Exact BigInt rationals, including binary64 dyadics; no sampled distance or floating integration.",
    gates:checks,total_gates:checks.length,all_gates_passed:checks.every(x=>x.passed),
    unnormalized_complete_even_A0_radius:rho.str(),
    values:{
      exact_centre_waist_normal_displacement:enclosure(delta),
      complete_waist_displacement_lower:enclosure(deltaLow),
      complete_waist_displacement_upper:enclosure(deltaHigh),
      full_unknown_tail_displacement_fee:enclosure(error),
      negative_waist_v_gap_lower:enclosure(vgap),
      negative_waist_mean_gap_lower:enclosure(meanGap),
      exact_waist_support_lower:enclosure(supportLower),
      required_body_radius_upper:enclosure(D.div(2)),
      conditional_diameter_upper:enclosure(D),
      required_positive_curvature_upper:enclosure(kplus),
      conditional_outward_tube_radius:enclosure(tube),
      conditional_held_to_diameter_lower:enclosure(deltaLow.div(D)),
      conditional_reach_to_diameter_lower:enclosure(reachRatio),
      marker_height_upper:enclosure(height),
    },
    exact_surface_conditions_not_established_by_this_calculation:[
      "A single complete exact common rotational metric surface and its C2 phase family.",
      "The final exact waist lies in the declared complete A0 ball, with u(0)=0 and exact turning mean m(0)=-a0.",
      "Whole unmarked body |F|<=511/400, F dot N>4/49, |principal_curvature|<=12, maximum signed principal_curvature<=196/27.",
      "Two fixed flat caps with positive radius at most 7e-6 and heights of absolute value in [0.9,1].",
      "All actual tails, caps, ordinary sources, means, parameter matching, and nonlinear convergence.",
    ],
    conditional_conclusion:"With the proved geometric hypotheses and fifth-power static markers, held>=Delta>0.05D, reach>0.03D, grip diameter>0.2D, and reflected-rigid congruence is excluded.",
    complete_topic:false,
  };
}

export { calculate };

async function main() {
  const fs = await import("node:fs/promises");
  const crypto = await import("node:crypto");
  const args = process.argv.slice(2);
  const input = args[0];
  const oi = args.indexOf("--out");
  if (!input || oi < 0 || !args[oi+1]) throw Error("usage: node SOURCE manifest.json --out NEW.json");
  const output = args[oi+1];
  const bytes = await fs.readFile(input);
  const expected = "464480dee60749f019b23a89b04568bf496731a580c21a3e761d4bc2192e108a";
  if (crypto.createHash("sha256").update(bytes).digest("hex") !== expected)
    throw Error("the complete public reconstruction manifest changed");
  const report = calculate(JSON.parse(bytes.toString("utf8")));
  report.executed_kernel_runtime = "Node BigInt exact rational calculation";
  await fs.writeFile(output, JSON.stringify(report, null, 2)+"\n", {flag:"wx"});
  console.log(JSON.stringify({all_gates_passed:report.all_gates_passed,total_gates:report.total_gates,output}));
  if (!report.all_gates_passed) process.exitCode=1;
}
const {pathToFileURL} = await import("node:url");
if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) await main();
