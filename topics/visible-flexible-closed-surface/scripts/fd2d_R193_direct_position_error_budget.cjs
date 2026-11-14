/* R193 conditional continuous-box metric/curvature budget.
 * Exact BigInt rationals and outward dyadic square roots. No surface solver.
 * Reference residuals, jets and all errors must already be certified on the
 * SAME physical box for the SAME accurate B32/central-curve/grid definition.
 */
"use strict";
function r193DirectPositionBudget(packet) {
  const abs=n=>n<0n?-n:n;
  function gcd(a,b){a=abs(a);b=abs(b);while(b){const r=a%b;a=b;b=r;}return a;}
  function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];}
  function fromNumber(x){
    if(!Number.isFinite(x))throw Error("nonfinite input");if(x===0)return F(0);
    const v=new DataView(new ArrayBuffer(8));v.setFloat64(0,x,false);
    const hi=v.getUint32(0,false),lo=v.getUint32(4,false),exp=(hi>>>20)&2047;
    let m=(BigInt(hi&1048575)<<32n)+BigInt(lo);if(exp)m+=1n<<52n;if(hi>>>31)m=-m;
    const e=exp?exp-1075:-1074;return e>=0?F(m<<BigInt(e)):F(m,1n<<BigInt(-e));
  }
  function R(v){if(typeof v==="number")return fromNumber(v);if(typeof v==="bigint")return F(v);if(Array.isArray(v)&&v.length===2)return F(v[0],v[1]);if(typeof v==="string"){const a=v.split("/");return F(a[0],a.length===2?a[1]:1);}throw Error("missing rational");}
  const z=F(0),one=F(1),two=F(2);
  const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
  const square=a=>mul(a,a);
  const cmp=(a,b)=>{const x=a[0]*b[1]-b[0]*a[1];return x<0n?-1:x>0n?1:0;};
  const max=(a,b)=>cmp(a,b)>0?a:b,min=(a,b)=>cmp(a,b)<0?a:b;
  const af=a=>F(abs(a[0]),a[1]),sum=v=>v.reduce(add,z);
  function nonnegative(v,name){const a=R(v);if(cmp(a,z)<0)throw Error("negative bound "+name);return a;}
  function interval(v){const a=R(v.lower),b=R(v.upper);if(cmp(a,b)>0)throw Error("reversed residual interval");return[a,b];}
  const maxabs=a=>max(af(a[0]),af(a[1]));
  function integerSqrt(n){if(n<0n)throw Error("negative square root");if(n<2n)return n;let x=1n<<BigInt(Math.ceil(n.toString(2).length/2));while(true){const y=(x+n/x)>>1n;if(y>=x)return x;x=y;}}
  const precision=packet.sqrt_precision_bits===undefined?96:packet.sqrt_precision_bits;
  if(!Number.isInteger(precision)||precision<16||precision>512)throw Error("invalid square-root output precision");
  const Q=1n<<BigInt(precision);
  function sqrtLower(a){if(cmp(a,z)<0)throw Error("negative radicand");return F(integerSqrt(a[0]*Q*Q/a[1]),Q);}
  function sqrtUpper(a){
    if(cmp(a,z)<0)throw Error("negative radicand");
    const n=(a[0]*Q*Q+a[1]-1n)/a[1];let r=integerSqrt(n);if(r*r<n)r++;
    return F(r,Q);
  }
  const show=a=>({exact:a.map(String),display:Number(a[0])/Number(a[1])});
  const showI=a=>({lower:a[0].map(String),upper:a[1].map(String),lower_display:Number(a[0][0])/Number(a[0][1]),upper_display:Number(a[1][0])/Number(a[1][1])});
  function symmetricErrorNorm(a,b,c){const tr=div(add(a,c),two),d=div(sub(a,c),two);return add(tr,sqrtUpper(add(square(d),square(b))));}
  if(!packet||packet.schema!=="fd2d-R193-direct-position-box-budget-input-v1")throw Error("wrong complete input schema");
  if(packet.scope!=="certified common continuous physical box"&&packet.scope!=="certified single physical point")throw Error("sample-only input is not a continuous-box certificate");
  if(!packet.bindings||!packet.bindings.accurate_base||!packet.bindings.accurate_central_curve||!packet.bindings.accurate_angle_height_grid||!packet.bindings.accurate_radius_grid||!packet.bindings.reference_fields||!packet.bindings.error_evidence)throw Error("all accurate/reference/error identities required");
  if(packet.derivatives!=="fixed physical s,u"||packet.actual_unit_tangent_definition!==true)throw Error("complete unit tangent and physical derivative definitions required");
  const p=packet.profile_errors,g=packet.angular_errors,b=packet.reference_bounds;
  const ea=nonnegative(p.a,"a"),eas=nonnegative(p.a_s,"a_s"),eass=nonnegative(p.a_ss,"a_ss");
  const ezs=nonnegative(p.Z_s,"Z_s"),ezss=nonnegative(p.Z_ss,"Z_ss");
  const eY=nonnegative(g.Y,"Y"),eYs=nonnegative(g.Y_s,"Y_s"),eYss=nonnegative(g.Y_ss,"Y_ss");
  const eT=nonnegative(g.T,"T"),eTs=nonnegative(g.T_s,"T_s"),eTu=nonnegative(g.T_u,"T_u");
  const aa=nonnegative(b.abs_a,"reference a"),aas=nonnegative(b.abs_a_s,"reference a_s"),aass=nonnegative(b.abs_a_ss,"reference a_ss");
  const a0min=R(b.a_lower),amin=R(packet.accurate_radius_lower);
  if(cmp(a0min,z)<=0||cmp(amin,z)<=0)throw Error("positive accurate/reference radii required");
  const nY=nonnegative(b.Y,"Y norm"),nYs=nonnegative(b.Y_s,"Y_s norm"),nYss=nonnegative(b.Y_ss,"Y_ss norm");
  const nA=nonnegative(b.X_ss,"actual reference X_ss norm"),nTs=nonnegative(b.T_s,"T_s norm"),nTu=nonnegative(b.T_u,"T_u norm");
  const nError=nonnegative(packet.reference_normal_error,"reference normal evaluation error");
  const rE0=interval(packet.reference_metric_residuals.rE),rF0=interval(packet.reference_metric_residuals.rF),rG0=interval(packet.reference_metric_residuals.rG);
  if(cmp(add(one,rE0[1]),z)<0)throw Error("reference |V0|^2 upper bound is negative");
  const nV=sqrtUpper(add(one,rE0[1]));
  // Delta V is formed around the actual reference, preserving its residual.
  const eV=sum([mul(eas,nY),mul(add(aas,eas),eY),mul(ea,nYs),mul(add(aa,ea),eYs),ezs]);
  const eA=sum([mul(eass,nY),mul(add(aass,eass),eY),mul(two,mul(eas,nYs)),mul(two,mul(add(aas,eas),eYs)),mul(ea,nYss),mul(add(aa,ea),eYss),ezss]);
  const dE=add(mul(two,mul(nV,eV)),square(eV));
  // Complete T has norm one: no extra eV*eT term is necessary.
  const dF=add(eV,mul(nV,eT));
  const rE=[sub(rE0[0],dE),add(rE0[1],dE)],rF=[sub(rF0[0],dF),add(rF0[1],dF)];
  const emax=maxabs(rE),fmax=maxabs(rF);
  const relativeMetric=add(div(emax,two),sqrtUpper(add(square(div(emax,two)),square(fmax))));
  const gramDeterminantLower=sub(add(one,rE[0]),square(fmax));
  const gramMinimumLower=sub(add(one,div(rE[0],two)),sqrtUpper(add(square(div(rE[0],two)),square(fmax))));
  const dG=maxabs(rG0),hError=symmetricErrorNorm(dE,dF,dG);
  const out={schema:"fd2d-R193-direct-position-box-budget-output-v1",scope:packet.scope,bindings:packet.bindings,
    derivatives:packet.derivatives,sqrt_precision_bits:precision,all_bounds_exact_rational_or_outward_dyadic:true,
    error_inputs:{profile:packet.profile_errors,angular:packet.angular_errors},
    vector_error:{X_s:show(eV),X_ss:show(eA)},metric_error:{rE:show(dE),rF:show(dF),Gram_operator:show(hError)},
    accurate_residuals:{rE:showI(rE),rF:showI(rF),rG:{lower:["0","1"],upper:["0","1"]}},
    relative_metric_operator_upper:show(relativeMetric),Gram_determinant_lower:show(gramDeterminantLower),Gram_eigenvalue_lower:show(gramMinimumLower),
    curvature_certified:false,main_candidate_claimed:false};
  const det0=sub(mul(add(one,rE0[0]),add(one,rG0[0])),square(maxabs(rF0)));
  const referenceGramPositive=cmp(add(one,rE0[0]),z)>0&&cmp(add(one,rG0[0]),z)>0&&cmp(det0,z)>0;
  out.reference_Gram_determinant_lower=show(det0);
  if(cmp(gramDeterminantLower,z)<=0||cmp(gramMinimumLower,z)<=0||!referenceGramPositive){
    out.unresolved_reason="The supplied continuous bounds do not establish both accurate and reference immersion. No geometric nonexistence conclusion.";
    return out;
  }
  const crossLower=sqrtLower(gramDeterminantLower),cross0Lower=sqrtLower(det0),crossError=dF;
  if(cmp(add(crossLower,cross0Lower),z)<=0){out.unresolved_reason="Square-root precision does not yet give a positive normalization denominator.";return out;}
  const normalError=add(min(two,div(mul(two,crossError),add(crossLower,cross0Lower))),nError);
  const eW=add(div(eTu,amin),div(mul(nTu,ea),mul(amin,a0min)));
  const qL=add(eA,mul(normalError,nA));
  const qM=add(eTs,mul(normalError,nTs));
  const qN=add(eW,mul(normalError,div(nTu,a0min)));
  const qError=symmetricErrorNorm(qL,qM,qN);
  const kappa0=nonnegative(packet.reference_curvature_upper,"reference curvature");
  if(packet.reference_curvature_kind!=="generalized Rayleigh bound for reference H0,Q0 on the same box")throw Error("finite formal/sample curvature cannot be relabelled as a reference bound");
  const kappa=add(kappa0,div(add(mul(kappa0,hError),qError),gramMinimumLower));
  out.normal_error_upper=show(normalError);
  out.second_form_error={L:show(qL),M:show(qM),N:show(qN),operator:show(qError)};
  out.reference_curvature_upper=show(kappa0);out.accurate_curvature_upper=show(kappa);out.curvature_certified=true;
  out.exact_cancellations=["G/a^2=|T|^2=1","N dot (a_s T/a+T_s)=N dot T_s","cross error uses deltaV cross T + V0 cross deltaT","reference actual residual retained before perturbation"];
  if(packet.requested_metric_tolerance!==undefined)out.metric_tolerance_satisfied=cmp(relativeMetric,nonnegative(packet.requested_metric_tolerance,"metric tolerance"))<=0;
  if(packet.requested_curvature_cap!==undefined)out.curvature_cap_satisfied=cmp(kappa,nonnegative(packet.requested_curvature_cap,"curvature cap"))<=0;
  return out;
}
function runR193BudgetFixture(){
  const tiny="1/1000000000000000";
  const packet={schema:"fd2d-R193-direct-position-box-budget-input-v1",
    scope:"certified common continuous physical box",derivatives:"fixed physical s,u",actual_unit_tangent_definition:true,
    bindings:{accurate_base:{kind:"conditional arithmetic fixture; not a repository B32 state"},
      accurate_central_curve:{kind:"conditional fixture"},accurate_angle_height_grid:{kind:"conditional fixture"},
      accurate_radius_grid:{kind:"conditional fixture"},reference_fields:{kind:"explicit bounds below"},
      error_evidence:{kind:"hypotheses of this arithmetic fixture, not measured errors of a main candidate"}},
    profile_errors:{a:tiny,a_s:tiny,a_ss:tiny,Z_s:tiny,Z_ss:tiny},
    angular_errors:{Y:tiny,Y_s:tiny,Y_ss:tiny,T:tiny,T_s:tiny,T_u:tiny},
    reference_bounds:{abs_a:"7/5",abs_a_s:"1",abs_a_ss:"7",a_lower:"4/5",
      Y:"3/2",Y_s:"2",Y_ss:"8",X_ss:"7",T_s:"2",T_u:"4"},
    accurate_radius_lower:"399/500",reference_normal_error:tiny,
    reference_metric_residuals:{
      rE:{lower:"-1/2500000000",upper:"1/2500000000"},
      rF:{lower:"-3/10000000000",upper:"3/10000000000"},
      rG:{lower:"-1/1000000000000000",upper:"1/1000000000000000"}},
    reference_curvature_upper:"7",
    reference_curvature_kind:"generalized Rayleigh bound for reference H0,Q0 on the same box",
    requested_metric_tolerance:"1/500000000",requested_curvature_cap:"15/2"
  };
  const result=r193DirectPositionBudget(packet);
  if(!result.curvature_certified||!result.metric_tolerance_satisfied||!result.curvature_cap_satisfied)throw Error("nonzero conditional budget fixture failed");
  const exact=JSON.parse(JSON.stringify(packet));
  for(const key of Object.keys(exact.profile_errors))exact.profile_errors[key]="0";
  for(const key of Object.keys(exact.angular_errors))exact.angular_errors[key]="0";
  exact.reference_normal_error="0";exact.reference_metric_residuals.rG={lower:"0",upper:"0"};
  const identity=r193DirectPositionBudget(exact);
  if(identity.metric_error.rE.exact[0]!=="0"||identity.metric_error.rF.exact[0]!=="0"||identity.second_form_error.operator.exact[0]!=="0"||identity.accurate_curvature_upper.exact.join("/")!=="7/1")throw Error("exact zero-error identity not preserved");
  const bad=JSON.parse(JSON.stringify(packet));bad.reference_metric_residuals.rE={lower:"-2",upper:"0"};
  const unresolved=r193DirectPositionBudget(bad);
  if(unresolved.curvature_certified||!unresolved.unresolved_reason)throw Error("unproved immersion was silently certified");
  return {schema:"fd2d-R193-actual-conditional-budget-fixture-v1",passed:true,
    nonzero_input:packet,nonzero_result:result,zero_error_identity:identity,
    intentionally_unresolved_input_returns_no_curvature_certificate:unresolved.unresolved_reason,
    OS_subprocess_started:false,main_B32_or_complete_surface_certified:false};
}
if(typeof module!=="undefined"&&module.exports){module.exports={r193DirectPositionBudget,runR193BudgetFixture};if(require.main===module)console.log(JSON.stringify(runR193BudgetFixture(),null,2));}
