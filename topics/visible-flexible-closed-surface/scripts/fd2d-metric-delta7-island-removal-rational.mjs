/* R186: exact scalar island-removal witness from existing small evidence.
 *
 * All decisions use BigInt rational arithmetic. Number is used only to
 * decode specified original binary64 parameters and to display results.
 * This standalone source can run under Node, or in a V8 isolate with an
 * emit(result) argument. It neither reads binary data nor evaluates a field,
 * F/J, BVP, profile ODE, or new Arb intervals.
 *
 * The first actual execution is the ChatGPT functions V8 call preserving
 * this exact source text. Source SHA256 is recorded by its external manifest.
 */
"use strict";

function gcd(a,b) {
  if(a<0n)a=-a;if(b<0n)b=-b;
  while(b!==0n){const r=a%b;a=b;b=r;}
  return a;
}
function Q(n,d=1n) {
  n=BigInt(n);d=BigInt(d);
  if(d===0n)throw Error("zero denominator");
  if(d<0n){n=-n;d=-d;}
  const g=gcd(n,d);
  return {n:n/g,d:d/g};
}
const add=(a,b)=>Q(a.n*b.d+b.n*a.d,a.d*b.d);
const sub=(a,b)=>Q(a.n*b.d-b.n*a.d,a.d*b.d);
const mul=(a,b)=>Q(a.n*b.n,a.d*b.d);
const div=(a,b)=>Q(a.n*b.d,a.d*b.n);
const neg=a=>Q(-a.n,a.d);
const cmp=(a,b)=>{const n=a.n*b.d-b.n*a.d;return n<0n?-1:n>0n?1:0;};
function pow(a,k){let r=Q(1);for(let j=0;j<k;j++)r=mul(r,a);return r;}
function dyadic(m,e){return e>=0?Q(BigInt(m)<<BigInt(e)):Q(m,1n<<BigInt(-e));}
function exactBinary64(x) {
  if(!Number.isFinite(x))throw Error("finite binary64 required");
  if(x===0)return Q(0);
  const buffer=new ArrayBuffer(8),view=new DataView(buffer);
  view.setFloat64(0,x,false);
  const high=view.getUint32(0,false),low=view.getUint32(4,false);
  const exponent=(high>>>20)&2047;
  const fraction=(BigInt(high&1048575)<<32n)|BigInt(low);
  const significand=exponent===0?fraction:(1n<<52n)|fraction;
  const signed=(high>>>31)?-significand:significand;
  return dyadic(signed,(exponent===0?-1022:exponent-1023)-52);
}
function record(x){return {exact:[x.n.toString(),x.d.toString()],display:Number(x.n)/Number(x.d)};}
const checks=[];
function check(name,condition){checks.push({name,passed:!!condition});if(!condition)throw Error(name);}

const zero=Q(0),one=Q(1);
const A=Q("801077783718527","562949953421312");
const D=Q("6507701461550367","4503599627370496");
const L7=Q("4581889784524941","4503599627370496");
const R7=Q("3307833529335461","2251799813685248");
const deltaOld=Q("1836789295023669","144115188075855872");
const deltaNew=exactBinary64(.027),deltaCap=exactBinary64(.08);
const aAtAUpper=dyadic("100232046176162410354410926399048739012901711058992158435288592685611452460697",-256);
const oldKUpper=Q("852552185","8589934592");
const oldGlobalRadiusLower=Q("18103121383342981011","23058430092136939520");
const middleEnd=Q("4458563631096791","4503599627370496");

check("exact old support and target ordering",cmp(L7,A)<0&&cmp(A,D)<0&&cmp(D,R7)<0);
check("old seventh coefficient strictly positive",cmp(deltaOld,zero)>0);
check("new coefficient is the exact binary64 0.027",cmp(deltaNew,Q("7782220156096217","288230376151711744"))===0);
check("original upper bound is exact binary64 0.08",cmp(deltaCap,Q("5764607523034235","72057594037927936"))===0);
check("increase only and within original coefficient box",cmp(deltaOld,deltaNew)<0&&cmp(deltaNew,deltaCap)<0);
check("original global radius bound positive",cmp(oldGlobalRadiusLower,zero)>0);

const width=sub(R7,L7),qLeft=div(sub(A,L7),width),qRight=div(sub(D,L7),width);
check("normalized target lies strictly in the right half of bump support",cmp(Q(1,2),qLeft)<0&&cmp(qLeft,qRight)<0&&cmp(qRight,one)<0);
const pLeft=add(sub(mul(Q(9),pow(qLeft,2)),mul(Q(9),qLeft)),Q(2));
check("increasing quadratic factor is already positive at qLeft",cmp(pLeft,zero)>0);
const bumpSecondLower=div(mul(Q(10240),mul(pow(qLeft,3),mul(pow(sub(one,qRight),3),pLeft))),pow(width,2));
check("exact full-band psi7-second factor bound exceeds 32/5",cmp(bumpSecondLower,Q(32,5))>0);

const oldRadiusUpper=add(add(aAtAUpper,sub(D,A)),deltaOld);
check("saved first-box endpoint radius upper is below 0.865621",cmp(aAtAUpper,Q(865621,1000000))<0);
check("old full-band radius upper is below 901/1000",cmp(oldRadiusUpper,Q(901,1000))<0);
check("certified old K upper is below 1/10",cmp(oldKUpper,Q(1,10))<0);
const increase=sub(deltaNew,deltaOld);
check("actual binary64 increase exceeds 57/4000",cmp(increase,Q(57,4000))>0);

const oldAssLoss=Q(901,10000);
const uniformNewAssLower=sub(mul(Q(32,5),Q(57,4000)),oldAssLoss);
check("simple uniform new a_ss lower equals 11/10000",cmp(uniformNewAssLower,Q(11,10000))===0);
check("uniform a_ss margin exceeds one thousandth",cmp(uniformNewAssLower,Q(1,1000))>0);
const newRadiusUpperForWholeRay=add(add(aAtAUpper,sub(D,A)),deltaCap);
check("all allowed increased profiles have radius below one on the target",cmp(newRadiusUpperForWholeRay,one)<0);
check("middle window ends before changed bump support",cmp(middleEnd,L7)<0);
check("bump right endpoint is exactly the protected terminal start",cmp(R7,exactBinary64(1.4689731783581288))===0);

const directMarginUsingCoarseOldAss=sub(mul(increase,bumpSecondLower),oldAssLoss);
const directMarginUsingSavedKAndRadius=sub(mul(increase,bumpSecondLower),mul(oldKUpper,oldRadiusUpper));
check("direct exact margin dominates simple bound",cmp(directMarginUsingCoarseOldAss,uniformNewAssLower)>0);
check("saved K/radius margin dominates coarse-ass margin",cmp(directMarginUsingSavedKAndRadius,directMarginUsingCoarseOldAss)>0);

const result={
  schema:"fd2d-R186-exact-BigInt-delta7-island-removal-v1",
  passed:true,
  arithmetic:"all assertions and bounds are exact reduced BigInt rationals; displayed Number ratios never determine an assertion",
  actual_origin:{bytes:133721,sha256:"b075e4e5c3dd11b3725eaec47e4d0a5e681d12dd400a4a2e3aff0c3b2f5bd13f"},
  evidence:{
    R182_report:{path:"notes/2026-11-12-fd2d-metric-dyadic34-signed-trace-windows-R182-01-report.json",bytes:12198,sha256:"44d3d9318ffa7b70f7bcc59cebf81df09e72b9c37562c05e1410cdb65b627a68"},
    R182_rows:{path:"notes/2026-11-12-fd2d-metric-dyadic34-signed-trace-windows-R182-01-rows.json.gz",bytes:124843,sha256:"d7f990bcef75ec30311e23d3cf92dadf5736f871f141dd3f7fa62071f7793095"},
    endpoint_radius_source:"late_negative row 0, exact a.upper_binary; actual pre-disconnect tool observation 1da6f9, not a new binary download",
    base_lipschitz_source:"R136 accurate shared-jet/phase definition and R166 sections 1(3),2: |a_base,s|<=1; Hermite Bernstein bound followed by exact phase derivatives",
    profile_family:"same accurate base, same seven saved compact C4 bump supports; only coefficient seven increases"
  },
  target_interval:[record(A),record(D)],
  target_endpoint_semantics:"original R182 exact dyadic support with decimal labels 1.423 and 1.445",
  bump_support:[record(L7),record(R7)],bump_width:record(width),
  old_delta7:record(deltaOld),
  allowed_new_delta7_interval:[record(deltaNew),record(deltaCap)],
  witness_binary64_delta7:record(deltaNew),witness_increase:record(increase),
  normalized_q_left:record(qLeft),normalized_q_right:record(qRight),
  quadratic_factor_at_q_left:record(pLeft),
  exact_independent_factor_psi7_second_lower:record(bumpSecondLower),
  simple_psi7_second_strict_lower:record(Q(32,5)),
  first_box_a_upper_at_A:record(aAtAUpper),
  old_whole_target_a_upper:record(oldRadiusUpper),
  old_K_upper:record(oldKUpper),
  simple_old_a_ss_strict_lower:record(neg(oldAssLoss)),
  simple_new_a_ss_strict_lower:record(uniformNewAssLower),
  direct_new_a_ss_strict_lower_from_coarse_old_ass:record(directMarginUsingCoarseOldAss),
  direct_new_a_ss_strict_lower_from_saved_K_and_radius:record(directMarginUsingSavedKAndRadius),
  new_whole_target_a_upper_for_all_allowed_delta7:record(newRadiusUpperForWholeRay),
  new_whole_target_K_strict_upper:record(neg(uniformNewAssLower)),
  retained_global_radius_lower:record(oldGlobalRadiusLower),
  coast_and_middle_metric_unchanged:true,
  protected_terminal_metric_and_K_unchanged:true,
  complete_body_or_seam_unchanged_claimed:false,
  current_late_positive_K_window_constraints_must_not_be_applied_to_new_negative_K_target:true,
  all_checks:checks,
  first89_box_ratio_maximum_computed:false,
  sufficient_witness_not_optimal_threshold:true,
  new_field_F_J_BVP_body_ODE_or_Arb_intervals_evaluated:false,
  whole_closed_surface_solution_claimed:false
};
if(typeof emit==="function")emit(result);
else console.log(JSON.stringify(result,null,2));
