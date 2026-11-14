/* Exact R187/R190 saved-axis ellipse perimeter and accurate normalization.
 * This consumes binary64 AXES as the mathematical seed; it does not solve a
 * different exact-gap problem. Positive rational series and geometric tail.
 */
"use strict";
function certifySavedEllipseNormalization(input) {
  const abs=n=>n<0n?-n:n;
  function gcd(a,b){a=abs(a);b=abs(b);while(b){const r=a%b;a=b;b=r;}return a;}
  function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];}
  const z=F(0),o=F(1),two=F(2);
  const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
  const cmp=(a,b)=>{const v=a[0]*b[1]-b[0]*a[1];return v<0n?-1:v>0n?1:0;};
  function R(v){if(Array.isArray(v)&&v.length===2)return F(v[0],v[1]);if(typeof v==="string"){const a=v.split("/");return F(a[0],a.length===2?a[1]:1);}throw Error("exact rational pair/string required");}
  function decodeBits(text){
    if(typeof text!=="string"||!/^0x[0-9a-fA-F]{16}$/.test(text))throw Error("full binary64 bit string required");
    const x=BigInt(text),e=Number((x>>52n)&2047n);if(e===2047)throw Error("nonfinite axis");
    let m=x&((1n<<52n)-1n);if(e)m+=1n<<52n;if(x>>63n)m=-m;
    const shift=e?e-1075:-1074;return shift>=0?F(m<<BigInt(shift)):F(m,1n<<BigInt(-shift));
  }
  function enclosure(a){const l=R(a.lower),r=R(a.upper);if(cmp(l,r)>0)throw Error("reversed enclosure");return[l,r];}
  const ip=a=>[a,a],ia=(a,b)=>[add(a[0],b[0]),add(a[1],b[1])];
  const ine=a=>[neg(a[1]),neg(a[0])],is=(a,b)=>ia(a,ine(b));
  function im(a,b){const v=[mul(a[0],b[0]),mul(a[0],b[1]),mul(a[1],b[0]),mul(a[1],b[1])].sort(cmp);return[v[0],v[3]];}
  function id(a,b){if(cmp(b[0],z)<=0&&cmp(b[1],z)>=0)throw Error("zero interval divisor");return im(a,[div(o,b[1]),div(o,b[0])]);}
  const precision=input.output_precision_bits===undefined?192:input.output_precision_bits;
  if(!Number.isInteger(precision)||precision<32||precision>512)throw Error("invalid output precision");
  const Q=1n<<BigInt(precision);
  function floor(a){return a[0]>=0n?a[0]/a[1]:-((-a[0]+a[1]-1n)/a[1]);}
  const ceil=a=>-floor(neg(a));
  function record(a){const l=F(floor(mul(a[0],F(Q))),Q),r=F(ceil(mul(a[1],F(Q))),Q);return{lower:l.map(String),upper:r.map(String),width:sub(r,l).map(String),lower_display:Number(l[0])/Number(l[1]),upper_display:Number(r[0])/Number(r[1])};}
  function factoredPerimeter(A,B,n){
    const C=div(add(A,B),two),q=div(sub(A,B),add(A,B)),q2=mul(q,q);
    if(cmp(A,z)<=0||cmp(B,z)<=0||cmp(q2,o)>=0)throw Error("positive axes required");
    let term=o,sum=z;
    for(let k=0;k<n;k++){
      sum=add(sum,term);
      term=mul(term,mul(q2,F(BigInt(2*k-1)**2n,4n*BigInt(k+1)**2n)));
    }
    const tail=div(term,sub(o,q2));
    return {mean:[mul(C,sum),mul(C,add(sum,tail))],C,q,tail:mul(C,tail),terms:n};
  }
  if(input.schema!=="fd2d-R187-saved-binary-ellipse-normalization-input-v1")throw Error("explicit saved-axis schema required");
  if(!input.bindings||!input.bindings.a0_certificate||!input.bindings.source_and_candidate||!input.axes||!input.axes.A_bits||!input.axes.B_bits)throw Error("complete axis and accurate target identity required");
  const A=decodeBits(input.axes.A_bits),B=decodeBits(input.axes.B_bits);
  const n=input.terms===undefined?64:input.terms;if(!Number.isInteger(n)||n<1||n>512)throw Error("positive declared series length required");
  const a0=enclosure(input.target_mean_radius);if(cmp(a0[0],z)<=0)throw Error("positive target mean radius required");
  const p=factoredPerimeter(A,B,n),scale=id(a0,p.mean),scaledA=im(ip(A),scale),scaledB=im(ip(B),scale);
  const gap=im(ip(sub(A,B)),scale),hi=cmp(A,B)>=0?A:B,lo=cmp(A,B)>=0?B:A;
  // Curvature of (scale*A cos(theta),scale*B sin(theta)).
  const inverseScale=id(p.mean,a0);
  const kmin=im(ip(div(lo,mul(hi,hi))),inverseScale);
  const kmax=im(ip(div(hi,mul(lo,lo))),inverseScale);
  const out={schema:"fd2d-R187-saved-binary-ellipse-normalization-certificate-v1",
    definition_kind:"saved exact dyadic axes, followed by accurate target-a0/perimeter normalization",
    bindings:input.bindings,axes:{A_bits:input.axes.A_bits,B_bits:input.axes.B_bits,A:A.map(String),B:B.map(String)},
    target_mean_radius:record(a0),perimeter_mean_radius:record(p.mean),
    normalized_scale:record(scale),normalized_A:record(scaledA),normalized_B:record(scaledB),
    normalized_axis_gap:record(gap),entire_central_curve_curvature_minimum:record(kmin),
    entire_central_curve_curvature_maximum:record(kmax),
    positive_series:{terms:n,C:p.C.map(String),q:p.q.map(String),geometric_tail_upper:p.tail.map(String),all_terms_nonnegative:true},
    output_precision_bits:precision,
    exact_gap_root_solved:false,material_angle_inverse_certified:false,
    full_B32_profile_or_surface_certified:false};
  if(input.requested_gap_exact!==undefined)out.gap_minus_requested=record(is(gap,ip(R(input.requested_gap_exact))));
  if(input.finite_observations){
    out.finite_observations=input.finite_observations;
    const pairs=[["mean_radius","perimeter_mean_radius",p.mean],["normalized_A","normalized_A",scaledA],["normalized_B","normalized_B",scaledB],["gap","normalized_axis_gap",gap]];
    out.observation_differences={};
    for(const [key,label,truth] of pairs)if(input.finite_observations[key+"_bits"]){
      const v=decodeBits(input.finite_observations[key+"_bits"]);
      out.observation_differences[label+"_minus_saved_finite"]=record(is(truth,ip(v)));
    }
  }
  return out;
}
function r187ActualSmallGapSeedInput(){
  return {schema:"fd2d-R187-saved-binary-ellipse-normalization-input-v1",
    axes:{A_bits:"0x3ff0767c5c4cf6bc",B_bits:"0x3fef535f1f0053de"},
    target_mean_radius:{
      lower:["27719700236759097884554771118456953527345486985901636753515972114122835",String(1n<<234n)],
      upper:["55439400473518195769109542236913907054690973971803273507031944228245679",String(1n<<235n)]},
    terms:32,output_precision_bits:192,requested_gap_exact:"1/20",
    bindings:{
      a0_certificate:{path:"notes/2026-11-12-fd2d-balanced-moments-taylor-01.json",bytes:8881,sha256:"0da13490030b82f536a921a97083b38f606ab604e7c7195c9053fb7975fa4b03",field:"enclosures.a0.binary_lower/binary_upper; integer mantissas copied without Number conversion",scope:"This accurate a0 enclosure is valid independently of the file's unrelated requested-width preference."},
      source_and_candidate:{provider_path:"scripts/fd2d-direct-position-designed-metric-provider-R190.cjs",provider_sha256:"cc45895fcf75972ee4339e5b86da70aaa589cb6491b2dbb29da26f1409771abb",candidate_path:"notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json",candidate_sha256:"9c903de99a0ca295db7d99e4dfec837db7778a7e20bc07abd6035a63e59a938d"},
      actual_axis_evidence:"The two exact IEEE-754 binary64 bit strings were provided by root from the current gap .05 provider seed; no 55-step search was repeated."}
  };
}
function runR187SavedEllipseCertificate(){
  const input=r187ActualSmallGapSeedInput(),result=certifySavedEllipseNormalization(input);
  const circle=JSON.parse(JSON.stringify(input));circle.axes={A_bits:"0x3ff0000000000000",B_bits:"0x3ff0000000000000"};delete circle.requested_gap_exact;
  const check=certifySavedEllipseNormalization(circle);
  if(check.positive_series.geometric_tail_upper[0]!=="0"||check.normalized_axis_gap.lower[0]!=="0"||check.normalized_axis_gap.upper[0]!=="0")throw Error("accurate circle identity failed");
  return {schema:"fd2d-R187-actual-small-gap-saved-axis-consumption-v1",passed:true,
    actual_input:input,actual_result:result,exact_circle_identity_check_passed:true,
    OS_subprocess_started:false,main_surface_certified:false,
    scope:"Actual current small-gap central seed only; exact perimeter, normalization and complete central-curve curvature. No angle inverse or main nonlinear solve."};
}
if(typeof module!=="undefined"&&module.exports){module.exports={certifySavedEllipseNormalization,r187ActualSmallGapSeedInput,runR187SavedEllipseCertificate};if(require.main===module)console.log(JSON.stringify(runR187SavedEllipseCertificate(),null,2));}
