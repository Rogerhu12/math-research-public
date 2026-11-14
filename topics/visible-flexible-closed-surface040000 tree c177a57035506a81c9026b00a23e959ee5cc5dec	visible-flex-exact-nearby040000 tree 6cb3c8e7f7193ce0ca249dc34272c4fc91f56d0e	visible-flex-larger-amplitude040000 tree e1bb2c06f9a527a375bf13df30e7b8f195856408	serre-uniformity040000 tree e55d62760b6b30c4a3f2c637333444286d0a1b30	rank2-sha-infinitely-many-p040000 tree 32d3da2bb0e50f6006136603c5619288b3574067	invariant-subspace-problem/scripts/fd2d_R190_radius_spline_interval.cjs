/* R190 exact rational interval consumer for the COMPLETE radius-spline addition.
 * The accurate B32 base and cut length are explicit dependencies. This module
 * does not replace them by an old delta-bump profile or by a rounded cut.
 * Inputs described as Number are decoded as their exact IEEE binary64 values.
 */
"use strict";
function createR190RadiusSplineInterval(spec) {
  const abs=z=>z<0n?-z:z;
  function gcd(a,b){a=abs(a);b=abs(b);while(b){const r=a%b;a=b;b=r;}return a;}
  function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];}
  const zero=F(0),one=F(1);
  const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
  const cmp=(a,b)=>{const v=a[0]*b[1]-b[0]*a[1];return v<0n?-1:v>0n?1:0;};
  const absF=a=>F(abs(a[0]),a[1]);
  function pow(a,n){let v=one;for(let k=0;k<n;k++)v=mul(v,a);return v;}
  function binary(x){
    if(!Number.isFinite(x))throw Error("nonfinite binary64 input");
    if(x===0)return zero;
    const a=new DataView(new ArrayBuffer(8));a.setFloat64(0,x,false);
    const h=a.getUint32(0,false),l=a.getUint32(4,false);
    const e=(h>>>20)&2047;let m=(BigInt(h&1048575)<<32n)+BigInt(l);
    if(e)m+=1n<<52n;
    if(h>>>31)m=-m;
    const shift=e?e-1023-52:-1074;
    return shift>=0?F(m<<BigInt(shift)):F(m,1n<<BigInt(-shift));
  }
  function R(a){
    if(typeof a==="number")return binary(a);
    if(typeof a==="bigint")return F(a);
    if(Array.isArray(a)&&a.length===2&&!Array.isArray(a[0]))return F(a[0],a[1]);
    if(typeof a==="string"){const v=a.split("/");if(v.length===1)return F(v[0]);if(v.length===2)return F(v[0],v[1]);}
    throw Error("Expected exact rational pair, integer string, or finite binary64 Number");
  }
  function I(a,b=a){a=R(a);b=R(b);if(cmp(a,b)>0)throw Error("reversed interval");return[a,b];}
  const ip=a=>I(a),iz=ip(zero);
  const ia=(a,b)=>[add(a[0],b[0]),add(a[1],b[1])];
  const ine=a=>[neg(a[1]),neg(a[0])],is=(a,b)=>ia(a,ine(b));
  function im(a,b){const v=[mul(a[0],b[0]),mul(a[0],b[1]),mul(a[1],b[0]),mul(a[1],b[1])].sort(cmp);return[v[0],v[3]];}
  function id(a,b){if(cmp(b[0],zero)<=0&&cmp(b[1],zero)>=0)throw Error("interval divisor includes zero");return im(a,[div(one,b[1]),div(one,b[0])]);}
  const scale=(a,b)=>im(a,ip(b));
  function hull(v){if(!v.length)throw Error("empty hull");let l=v[0][0],r=v[0][1];for(const a of v){if(cmp(a[0],l)<0)l=a[0];if(cmp(a[1],r)>0)r=a[1];}return[l,r];}
  const abmax=a=>cmp(absF(a[0]),absF(a[1]))>0?absF(a[0]):absF(a[1]);
  const show=a=>a.map(String);
  const rec=a=>({lower:show(a[0]),upper:show(a[1]),lower_display:Number(a[0][0])/Number(a[0][1]),upper_display:Number(a[1][0])/Number(a[1][1])});
  function decodeInterval(a){if(a&&a.lower&&a.upper)return I(a.lower,a.upper);throw Error("missing exact interval endpoints");}
  function choose(n,k){if(k<0||k>n)return zero;let v=one;for(let j=1;j<=k;j++)v=mul(v,F(n-k+j,j));return v;}
  function derivative(p,k){p=p.slice();while(k--){p=p.slice(1).map((x,j)=>mul(x,F(j+1)));}return p.length?p:[zero];}
  // Exact affine change followed by the power-to-Bernstein identity.
  function polynomialRange(p,l,r){
    const n=p.length-1,d=sub(r,l),q=Array.from({length:n+1},()=>zero),b=[];
    for(let k=0;k<=n;k++)for(let i=k;i<=n;i++)q[k]=add(q[k],mul(mul(p[i],choose(i,k)),mul(pow(l,i-k),pow(d,k))));
    for(let j=0;j<=n;j++){let v=zero;for(let k=0;k<=j;k++)v=add(v,mul(q[k],div(choose(j,k),choose(n,k))));b.push(ip(v));}
    return hull(b);
  }
  const pieces=[
    {l:F(-2),r:F(-1),p:[F(4,3),F(2),F(1),F(1,6)]},
    {l:F(-1),r:F(0),p:[F(2,3),F(0),F(-1),F(-1,2)]},
    {l:F(0),r:F(1),p:[F(2,3),F(0),F(-1),F(1,2)]},
    {l:F(1),r:F(2),p:[F(4,3),F(-2),F(1),F(-1,6)]}
  ];
  function basisRange(t,k){
    if(!Number.isInteger(k)||k<0||k>2)throw Error("only complete C2 jets are exported");
    const v=[];
    if(cmp(t[0],F(-2))<=0||cmp(t[1],F(2))>=0)v.push(iz);
    for(const p of pieces){
      const l=cmp(t[0],p.l)>0?t[0]:p.l,r=cmp(t[1],p.r)<0?t[1]:p.r;
      if(cmp(l,r)<=0)v.push(polynomialRange(derivative(p.p,k),l,r));
    }
    return v.length?hull(v):iz;
  }
  function exactBasisPoint(t,k){
    t=R(t);const weights=[1,-4,6,-4,1],power=3-k;
    let v=zero;
    for(let j=0;j<=4;j++){const q=add(t,F(2-j));if(cmp(q,zero)>0)v=add(v,mul(F(weights[j]),pow(q,power)));}
    return div(v,F(power===3?6:power===2?2:1));
  }
  if(!spec||spec.schema!=="fd2d-R190-accurate-radius-spline-input-v1")throw Error("explicit accurate-grid input schema required");
  const J=spec.radial_basis_count;
  if(!Number.isInteger(J)||J<1)throw Error("positive integer radial basis count required");
  if(!spec.base_definition_binding||!spec.cut_length_enclosure||!spec.cut_length_enclosure.exact_definition_binding||!spec.parameter_binding)throw Error("base, exact cut definition and parameter bindings required");
  const c=R(spec.central_length),S=decodeInterval(spec.cut_length_enclosure),rho=spec.radius_coefficients.map(R);
  if(rho.length!==J||cmp(c,F(13,128))!==0)throw Error("This layer binds the B32 central length 13/128 and all J radius coefficients");
  if(cmp(S[0],c)<=0)throw Error("nonpositive accurate spline length");
  const h=scale(is(S,ip(c)),F(1,J+3)),invh=id(ip(one),h);
  const baseLower=R(spec.base_radius_lower_bound),bound=R(spec.radius_coefficient_bound);
  if(cmp(bound,zero)<0||cmp(bound,baseLower)>=0)throw Error("coefficient bound must preserve positive radius");
  let rmax=zero,minCoeff=zero,maxCoeff=zero;
  for(const r of rho){if(cmp(absF(r),bound)>0)throw Error("actual coefficient outside the declared exact box");if(cmp(absF(r),rmax)>0)rmax=absF(r);if(cmp(r,minCoeff)<0)minCoeff=r;if(cmp(r,maxCoeff)>0)maxCoeff=r;}
  const hp=[ip(one),invh,im(invh,invh)];
  function fromArguments(arguments_,query){
    const cols=[],sum=[iz,iz,iz];
    for(let j=0;j<J;j++){
      const jets=[0,1,2].map(k=>im(basisRange(arguments_[j],k),hp[k]));
      cols.push({parameter_index:j,jets:jets.map(rec)});
      for(let k=0;k<3;k++)sum[k]=ia(sum[k],scale(jets[k],rho[j]));
    }
    // Partition of unity gives a second, independent value enclosure.
    sum[0]=[cmp(sum[0][0],minCoeff)>0?sum[0][0]:minCoeff,cmp(sum[0][1],maxCoeff)<0?sum[0][1]:maxCoeff];
    if(cmp(sum[0][0],sum[0][1])>0)throw Error("inconsistent certified bounds");
    return {schema:"fd2d-R190-complete-radius-increment-jet-box-v1",query,
      derivatives:"fixed physical s",jet_order:["value","first","second"],jets:sum.map(rec),
      radius_parameter_columns:cols,definition:definition(),
      exact_base_jet_included:false,all_complete_spline_terms_included:true};
  }
  function normalizedBox(left,right=left){
    left=R(left);right=R(right);if(cmp(left,right)>0)throw Error("reversed normalized box");
    const t=I(left,right),args=Array.from({length:J},(_,j)=>is(scale(t,F(J+3)),ip(F(j+2))));
    return fromArguments(args,{kind:"accurate normalized t=(s-c)/(S-c)",lower:show(left),upper:show(right)});
  }
  function physicalBox(left,right=left){
    left=R(left);right=R(right);if(cmp(left,right)>0)throw Error("reversed physical box");
    const x=im(is(I(left,right),ip(c)),invh),args=Array.from({length:J},(_,j)=>is(x,ip(F(j+2))));
    return fromArguments(args,{kind:"fixed physical s",lower:show(left),upper:show(right)});
  }
  function definition(){
    return {schema:"fd2d-R190-accurate-radius-spline-interval-definition-v1",
      base_definition_binding:spec.base_definition_binding,
      cut_exact_definition_binding:spec.cut_length_enclosure.exact_definition_binding,
      cut_length_enclosure:rec(S),central_length:show(c),radial_basis_count:J,spacing_enclosure:rec(h),
      radius_coefficients:rho.map(show),parameter_binding:spec.parameter_binding,
      accurate_grid:"h=(S-c)/(J+3); centers=c+(j+2)h; S is the accurate B32 cut, not its binary64 evaluator",
      endpoint_two_jets:"all radius additions are exactly zero at the accurate c and S",
      base_radius_lower_bound:show(baseLower),maximum_actual_coefficient:show(rmax),
      certified_total_radius_lower_bound:show(sub(baseLower,rmax)),
      full_B32_integrals_or_base_jets_recomputed:false,
      base_bound_and_cut_enclosure_are_explicit_caller_certificates:true};
  }
  function addBase(basePacket,increment){
    if(!basePacket||basePacket.schema!=="fd2d-R190-compatible-accurate-base-jet-box-v1")throw Error("missing accurate base jet packet");
    if(JSON.stringify(basePacket.base_definition_binding)!==JSON.stringify(spec.base_definition_binding)||JSON.stringify(basePacket.query)!==JSON.stringify(increment.query))throw Error("base identity or query mismatch");
    if(basePacket.derivatives!=="fixed physical s"||basePacket.jets.length!==3)throw Error("wrong base jet coordinate");
    const jets=basePacket.jets.map((a,k)=>rec(ia(decodeInterval(a),decodeInterval(increment.jets[k]))));
    return {schema:"fd2d-R190-accurate-total-radius-jet-box-v1",query:increment.query,derivatives:"fixed physical s",
      jets,definition:definition(),base_packet_binding:basePacket.packet_binding,
      complete_radius_parameter_columns:increment.radius_parameter_columns};
  }
  function floatingGridComparison(left,right,floatingGrid){
    left=R(left);right=R(right);if(cmp(left,right)>0)throw Error("reversed comparison box");
    if(!floatingGrid||!floatingGrid.binding||floatingGrid.centers.length!==J)throw Error("explicit finite grid identity and centers required");
    const hf=R(floatingGrid.spacing),centers=floatingGrid.centers.map(R);
    if(cmp(hf,zero)<=0)throw Error("nonpositive finite spacing");
    const ifh=div(one,hf),M=[F(2,3),F(2,3),F(2),F(3)],per=[],total=[zero,zero,zero];
    const reciprocalDifference=is(ip(ifh),invh),x=is(I(left,right),ip(c));
    for(let j=0;j<J;j++){
      const offset=add(div(sub(c,centers[j]),hf),F(j+2));
      const dq=abmax(ia(im(x,reciprocalDifference),ip(offset))),errors=[];
      for(let k=0;k<3;k++){
        const scaleDiff=abmax(is(ip(pow(ifh,k)),hp[k]));
        const e=add(mul(M[k],scaleDiff),mul(mul(M[k+1],pow(ifh,k)),dq));
        errors.push(show(e));total[k]=add(total[k],mul(absF(rho[j]),e));
      }
      per.push({parameter_index:j,argument_error_upper:show(dq),basis_jet_error_upper:errors});
    }
    return {schema:"fd2d-R190-rounded-grid-vs-accurate-grid-jet-bound-v1",
      query:{kind:"fixed physical s",lower:show(left),upper:show(right)},
      finite_grid_binding:floatingGrid.binding,finite_spacing:show(hf),finite_centers:centers.map(show),
      accurate_definition:definition(),per_basis:per,total_increment_jet_error_upper:total.map(show),
      full_C2_knots_covered:true,coefficient_rounding_error:0,
      scope:"Exact real spline functions on saved rounded constants versus the accurate grid, with the same exact dyadic rho.",
      floating_arithmetic_operation_roundoff_included:false,
      base_evaluator_error_included:false};
  }
  function returnedPointComparison(s,returnedJets){
    if(!returnedJets||returnedJets.length!==3)throw Error("three actual returned radius-increment numbers required");
    const exact=physicalBox(s),errors=returnedJets.map((v,k)=>show(abmax(is(ip(R(v)),decodeInterval(exact.jets[k])))));
    return {schema:"fd2d-R190-actual-returned-point-radius-jet-bound-v1",exact,
      actual_returned_jets:returnedJets.map(v=>show(R(v))),absolute_error_upper:errors,
      scope:"Pointwise comparison includes every cause of error in these supplied actual returned numbers; it is not a boxwise floating-evaluator bound."};
  }
  return {F,R,I,add,sub,mul,div,cmp,pow,record:rec,decodeInterval,basisRange,exactBasisPoint,
    normalizedBox,physicalBox,definition,addBase,floatingGridComparison,returnedPointComparison};
}
function runR190RadiusIntervalFixture(){
  const coefficients=Array.from({length:12},(_,j)=>j%3===0?-.4:j%3===1?.2:.1);
  const spec={schema:"fd2d-R190-accurate-radius-spline-input-v1",central_length:"13/128",
    cut_length_enclosure:{lower:["177","200"],upper:["177","200"],exact_definition_binding:{kind:"independent rational arithmetic fixture",S:"177/200",not_actual_B32:true}},
    radial_basis_count:12,radius_coefficients:coefficients,radius_coefficient_bound:.4,base_radius_lower_bound:"4/5",
    base_definition_binding:{kind:"conditional base bound fixture; no B32 integral consumed",lower:"4/5"},
    parameter_binding:{kind:"explicit finite binary64 fixture",coefficients}};
  const C=createR190RadiusSplineInterval(spec),F=C.F,zero=F(0),h=F(5011,96000),c=F(13,128),S=F(177,200);
  // Recompute spacing directly: no manually supplied decimal grid.
  const spacing=C.div(C.sub(S,c),F(15));
  let checked=0;
  function contains(a,x){return C.cmp(C.R(a.lower),x)<=0&&C.cmp(x,C.R(a.upper))<=0;}
  for(let m=0;m<=30;m++){
    const t=F(m,30),a=C.normalizedBox(t),truth=[zero,zero,zero];
    for(let j=0;j<12;j++)for(let k=0;k<3;k++){
      const q=C.sub(C.mul(F(15),t),F(j+2));
      const v=C.div(C.exactBasisPoint(q,k),C.pow(spacing,k));
      if(!contains(a.radius_parameter_columns[j].jets[k],v))throw Error("independent truncated-power point not enclosed");
      truth[k]=C.add(truth[k],C.mul(C.R(coefficients[j]),v));checked++;
    }
    for(let k=0;k<3;k++){if(!contains(a.jets[k],truth[k]))throw Error("complete point sum not enclosed");checked++;}
  }
  let boxChecks=0;
  for(let m=0;m<15;m++){
    const box=C.normalizedBox(F(m,15),F(m+1,15));
    for(const d of [1,3,5,7])for(let k=0;k<3;k++){
      const t=F(8*m+d,120);let v=zero;
      for(let j=0;j<12;j++)v=C.add(v,C.mul(C.R(coefficients[j]),C.div(C.exactBasisPoint(C.sub(C.mul(F(15),t),F(j+2)),k),C.pow(spacing,k))));
      if(!contains(box.jets[k],v))throw Error("continuous Bernstein box missed independent rational point");boxChecks++;
    }
  }
  const cFloat=13/128,sFloat=177/200,hFloat=(sFloat-cFloat)/15;
  const floatingGrid={spacing:hFloat,centers:Array.from({length:12},(_,j)=>cFloat+(j+2)*hFloat),binding:{kind:"actual JavaScript binary64 grid computation in this fixture",central:cFloat,end:sFloat}};
  const drift=C.floatingGridComparison(c,S,floatingGrid),driftChecks=[];
  for(const t of [F(1,7),F(1,2),F(6,7)]){
    const s=C.add(c,C.mul(C.sub(S,c),t)),exact=C.physicalBox(s),observed=[zero,zero,zero];
    for(let j=0;j<12;j++)for(let k=0;k<3;k++){
      const q=C.div(C.sub(s,C.R(floatingGrid.centers[j])),C.R(hFloat));
      const v=C.div(C.exactBasisPoint(q,k),C.pow(C.R(hFloat),k));
      observed[k]=C.add(observed[k],C.mul(C.R(coefficients[j]),v));
    }
    const errors=observed.map((v,k)=>{const a=C.decodeInterval(exact.jets[k]),d=C.sub(v,a[0]),e=d[0]<0n?F(-d[0],d[1]):d;if(C.cmp(e,C.R(drift.total_increment_jet_error_upper[k]))>0)throw Error("strict rounded-grid sensitivity bound failed");return e.map(String);});
    driftChecks.push({normalized_point:t.map(String),exact_real_grid_error:errors});
  }
  const ends=[C.normalizedBox("0"),C.normalizedBox("1")];
  for(const e of ends)for(const v of e.jets)if(C.cmp(C.R(v.lower),zero)||C.cmp(C.R(v.upper),zero))throw Error("accurate endpoint two-jet is nonzero");
  return {schema:"fd2d-R190-radius-spline-interval-actual-fixture-v1",passed:true,
    runtime:"pure JavaScript BigInt exact rational arithmetic",OS_process_started:false,
    independent_truncated_power_point_checks:checked,independent_points_inside_continuous_boxes:boxChecks,
    accurate_endpoint_two_jets_zero:true,definition:C.definition(),
    example_nonzero_box:C.normalizedBox("7/30","1/4"),rounded_grid_sensitivity:drift,independent_grid_comparisons:driftChecks,
    actual_B32_base_or_main_candidate_certified:false,
    source_meaning:"complete C2 spline increments and exact rounded-grid sensitivity; all nonrational base inputs remain explicit dependencies"};
}
if(typeof module!=="undefined"&&module.exports){
  module.exports={createR190RadiusSplineInterval,runR190RadiusIntervalFixture};
  if(require.main===module)console.log(JSON.stringify(runR190RadiusIntervalFixture(),null,2));
}
