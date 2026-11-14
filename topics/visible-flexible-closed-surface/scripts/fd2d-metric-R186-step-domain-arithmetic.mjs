/* R186 exact step-domain arithmetic.
 * Standalone UTF8 source: functions V8 or Node; no OS-dependent numerics.
 * All proof comparisons use reduced BigInt rationals.
 * An ideal affine step is not an executed solver trial.
 */
function r186StepArithmetic(input = {}) {
  const abs = a => a < 0n ? -a : a;
  function gcd(a,b) { a=abs(a); b=abs(b); while(b){const t=a%b;a=b;b=t;} return a; }
  function F(n,d=1n) { n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g]; }
  const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=a=>[-a[0],a[1]];
  const sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
  const cmp=(a,b)=>{const d=a[0]*b[1]-b[0]*a[1];return d<0n?-1:d>0n?1:0;};
  function binary(x) {
    if(!Number.isFinite(x))throw Error("finite binary64 required");
    const a=new ArrayBuffer(8),v=new DataView(a);v.setFloat64(0,x,false);
    const hi=v.getUint32(0,false),lo=v.getUint32(4,false),e=(hi>>>20)&2047;
    let n=(BigInt(hi&1048575)<<32n)|BigInt(lo),power;
    if(e){n|=1n<<52n;power=e-1023-52;}else power=-1074;
    if(hi>>>31)n=-n;
    return power>=0?F(n<<BigInt(power)):F(n,1n<<BigInt(-power));
  }
  function read(x,fallback) {
    if(x===undefined)return fallback;
    if(typeof x==="number")return binary(x);
    if(Array.isArray(x)&&x.length===2)return F(x[0],x[1]);
    throw Error("use a binary64 number or [exact numerator,exact denominator]");
  }
  const out=a=>({exact:a.map(String),display:Number(a[0])/Number(a[1])});
  const zero=F(0),one=F(1),m=F("7782220156096217","288230376151711744");
  const M=F("5764607523034235","72057594037927936");
  const d0=read(input.origin,F("1836789295023669","144115188075855872"));
  const d1=read(input.endpoint,M),within=x=>cmp(x,neg(M))>=0&&cmp(x,M)<=0;
  if(!within(d0)||!within(d1))throw Error("origin/endpoint violates the original binary64 .08 box");
  const needed=alpha=>add(d0,div(sub(m,d0),alpha));
  let alphaEnter=null,entryKind;
  if(cmp(d0,m)>=0)entryKind="origin_already_meets_R186_lower";
  else if(cmp(d1,d0)<=0)entryKind="no_increasing_direction";
  else {
    alphaEnter=div(sub(m,d0),sub(d1,d0));
    entryKind=cmp(alphaEnter,one)<=0?"entry_on_ideal_unit_segment":"endpoint_still_below_R186_lower";
  }
  const steps=[F(1),F(1,2),F(1,4),F(1,8)];
  const requirements=steps.map(alpha=>({
    ideal_step:out(alpha),endpoint_required:out(needed(alpha)),
    compatible_with_original_upper:cmp(needed(alpha),M)<=0
  }));
  const universal=cmp(d0,m)<0?div(sub(m,d0),sub(M,d0)):zero;
  let requested=null;
  if(input.step!==undefined){
    const alpha=read(input.step);
    if(cmp(alpha,zero)<0||cmp(alpha,one)>0)throw Error("step must be in [0,1]");
    const ideal=add(d0,mul(alpha,sub(d1,d0)));
    requested={step:out(alpha),ideal_delta7:out(ideal),ideal_R186_membership:cmp(ideal,m)>=0&&cmp(ideal,M)<=0};
  }
  let actual=null;
  if(input.actual_trial!==undefined){
    const d=read(input.actual_trial);
    actual={delta7:out(d),R186_delta7_membership:cmp(d,m)>=0&&cmp(d,M)<=0,
      other_six_box_middle_rows_radius_and_tail_certificate_not_checked:true};
  }
  return {
    schema:"fd2d-R186-exact-Armijo-step-domain-v1",
    arithmetic:"exact BigInt rationals; Number only decodes provided binary64 inputs and displays ratios",
    origin:out(d0),endpoint:out(d1),R186_delta7_lower:out(m),original_delta7_upper:out(M),
    origin_is_b075_default:input.origin===undefined,
    default_endpoint_is_only_the_original_box_upper_not_an_executed_QP:input.endpoint===undefined,
    entry_kind:entryKind,ideal_alpha_enter:alphaEnter?out(alphaEnter):null,
    minimum_possible_ideal_alpha_under_original_endpoint_box:out(universal),
    endpoint_requirements:requirements,requested_ideal_step:requested,
    actual_trial_membership:actual,
    existing_domain_Armijo_trial_acceptance_changed:false,
    no_F_J_BVP_body_or_profile_box_evaluated:true
  };
}
const r186StepInput=typeof process!=="undefined"&&process.argv&&process.argv[2]
  ?JSON.parse(process.argv[2]):(globalThis.r186StepInput||{});
const result=r186StepArithmetic(r186StepInput);
if(typeof emit==="function")emit(result);
else if(typeof console!=="undefined")console.log(JSON.stringify(result,null,2));
