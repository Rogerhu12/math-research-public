// Exact scalar certificate for the independent R86 full-disk marker.
// This uses the already paid R82/R83 field and the R84 endpoint identity.
// The new epsilon is an exact rational expression, not a rounded binary64.
import { endpointTensorCertificate } from "./endpoint_tensor_exact_certificate.mjs";

export function fullDiskMarkerCertificate(r82, r83) {
  const endpoint = endpointTensorCertificate(r83);
  function need(x,m) { if (!x) throw new Error(m); }
  function gcd(a,b) { a=a<0n?-a:a; b=b<0n?-b:b;
    while(b) { const c=a%b; a=b; b=c; } return a; }
  function Q(n,d=1n) { n=BigInt(n); d=BigInt(d);
    need(d!==0n,"zero denominator"); if(d<0n) { n=-n; d=-d; }
    const g=gcd(n,d); return [n/g,d/g]; }
  const read=s=>{const p=s.split("/");return Q(p[0],p[1]??"1");};
  const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const sub=(a,b)=>Q(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
  const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
  const pow=(a,n)=>Q(a[0]**BigInt(n),a[1]**BigInt(n));
  const eq=(a,b)=>a[0]*b[1]===b[0]*a[1];
  const gt=(a,b)=>a[0]*b[1]>b[0]*a[1];
  const text=a=>a[0].toString()+"/"+a[1].toString();
  function literalDouble(x) {
    need(Number.isFinite(x),"finite original scalar");
    const buffer=new ArrayBuffer(8),v=new DataView(buffer);
    v.setFloat64(0,x,false); const bits=v.getBigUint64(0,false);
    let e=Number((bits>>52n)&2047n);
    let m=(bits&((1n<<52n)-1n))+(e?1n<<52n:0n);
    e=(e||1)-1023-52; if(bits>>63n) m=-m;
    return e>=0?Q(m<<BigInt(e)):Q(m,1n<<BigInt(-e));
  }
  need(r82.status==="actual_complete_marked_column_closed_C2_geometry_certified",
       "R82 actual closed geometry");
  need(r82.source.sha256==="2aebf619d8e835d060c0897fc82446473dbd88fd32836dc5b66ce36f73cf3b7e",
       "R82 original scalar-transfer source");
  need(r82.actual_report.sha256===endpoint.bindings.geometry,"same geometry");
  need(r82.actual_query.sha256===endpoint.bindings.query,"same actual query");
  need(r82.geometry_bundle.sha256===endpoint.bindings.bundle,"same complete field");
  need(r82.source_run.sha256===endpoint.bindings.source_run,"same actual prefix");
  need(r82.finite_stage_count===1152 && r82.literal_span_count===18460,
       "complete original field");
  const oldRadius=read(r82.canonical_marker_radius_exact);
  const oldEpsilon=read(r82.canonical_marker_amplitude_exact);
  need(eq(oldRadius,read("900719925474099/36028797018963968")),"old radius");
  need(eq(oldEpsilon,read("4722366482869643/75557863725914323419136")),"old epsilon");
  // R82's actual source checks marker_radius == Fraction(rCuff)/2.
  const radius=mul(Q(2),oldRadius),epsilon=mul(Q(1600),oldEpsilon);
  need(!gt(epsilon,div(pow(radius,2),Q(25))),"new local geometry gate");
  const oldCanonicalAtNewRadius=div(pow(radius,2),Q(10000));
  need(gt(epsilon,oldCanonicalAtNewRadius),
       "the original canonical constructor must reject this distinct design");
  const [Zlo,Zhi]=r82.cap_height_after_column_exact_interval.map(read);
  need(gt(Zlo,mul(Q(2),epsilon)),"positive graph height");
  const gradient=div(mul(Q(24),epsilon),radius);
  const curvature=div(mul(Q(252),epsilon),pow(radius,2));
  // sqrt(1+x)<=1+x/2, x>=0; no floating-point square root is used.
  const support=div(sub(Zlo,mul(Q(26),epsilon)),
                    add(Q(1),div(pow(gradient,2),Q(2))));
  const radiusSquared=add(pow(radius,2),pow(add(Zhi,mul(Q(2),epsilon)),2));
  const originalRho=literalDouble(r82.whole_radius_upper);
  const originalSigma=literalDouble(r82.whole_support_lower);
  const originalDiameter=literalDouble(r82.whole_diameter_upper);
  need(gt(pow(originalRho,2),radiusSquared),"new cap radius preserves whole bound");
  need(gt(support,originalSigma),"new cap support preserves whole bound");
  need(gt(Q(123,10),curvature),"new cap curvature preserves whole bound");
  const BoverPi=div(mul(epsilon,pow(radius,5)),Q(140));
  const oldBoverPi=read(r82.marker_first_moment_divided_by_pi_exact);
  need(eq(BoverPi,mul(Q(51200),oldBoverPi)),"exact B3 gain");
  need(eq(oldBoverPi,read(endpoint.exact.cap_moment_over_pi)),"same R84 cap");
  const drop=mul(Q(51200),read(endpoint.exact.tensor_norm_squared_drop_strict_lower));
  const requestedDrop=Q(359,10n**16n);
  need(gt(drop,requestedDrop),"new endpoint tensor gap exceeds 3.59e-14");
  return {
    status:"R86_exact_scalar_transfer_and_endpoint_consequence_passed",
    construction:"New exact fixed graph on both full flat disks; all R82 activity unchanged",
    old_source_commit:"4cbd74a0b22de4345fee878d9e06de97dd14c102",
    old_geometry_sha256:endpoint.bindings.geometry,
    old_query_sha256:endpoint.bindings.query,
    radius_exact:text(radius),epsilon_exact:text(epsilon),
    epsilon_definition:"1600 times the old literal epsilon, in exact rational arithmetic",
    epsilon_numerator_bits:epsilon[0].toString(2).length,
    binary64_epsilon_is_not_the_definition:true,
    original_canonical_source_and_query_unchanged:true,
    original_canonical_constructor_rejects_new_parameters:true,
    cap_height_interval_exact:[text(Zlo),text(Zhi)],
    cap_gradient_norm_upper_exact:text(gradient),
    cap_curvature_upper_exact:text(curvature),
    cap_support_lower_exact:text(support),
    cap_radius_squared_upper_exact:text(radiusSquared),
    whole_radius_upper_exact:text(originalRho),
    whole_diameter_upper_exact:text(originalDiameter),
    whole_support_lower_exact:text(originalSigma),
    whole_curvature_upper_exact:"123/10",
    whole_reach_lower_exact:"10/123",
    whole_reach_over_D_lower_exact:text(div(Q(10,123),originalDiameter)),
    new_B3_over_pi_exact:text(BoverPi),
    B3_multiplier_exact:"51200",
    endpoint_tensor_gap_strict_lower_exact:text(drop),
    endpoint_tensor_gap_requested_exact:text(requestedDrop),
    endpoint_tensor_gap_positive_margin_exact:text(sub(drop,requestedDrop)),
    new_metric:"R82 target off the two flat disks; dx^2+dy^2+df_new^2 on them",
    new_target_fixed_for_every_phase:true,
    boundary_f_df_D2f_exactly_zero:true,
    changed_target_is_not_old_problem_refinement:true,
    new_Python_map_evaluator_executed:false,
    new_full_numerical_query_or_mesh_executed:false,
    numerical_Hausdorff_lower_bound_or_multiplier_claimed:false,
    complete_tail_metric_or_lambda_one_claimed:false,
    README_completion_claimed:false
  };
}
