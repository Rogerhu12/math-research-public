// Exact rational consequence of R83 plus the R84 reflection/tensor proof.
// No quadrature, floating-point gate, or Hausdorff-distance bound is used.
// The caller supplies the published R83 small record at commit
// 4cbd74a0b22de4345fee878d9e06de97dd14c102.
export function endpointTensorCertificate(r) {
  function need(v, m) { if (!v) throw new Error(m); }
  function gcd(a, b) { a = a < 0n ? -a : a; b = b < 0n ? -b : b;
    while (b) { const c = a % b; a = b; b = c; } return a; }
  function Q(a, b = 1n) { a = BigInt(a); b = BigInt(b);
    need(b !== 0n, "zero denominator");
    if (b < 0n) { a = -a; b = -b; }
    const g = gcd(a, b); return [a/g, b/g]; }
  function read(s) { need(typeof s === "string", "fraction must be text");
    const p = s.split("/"); need(p.length <= 2, "bad fraction");
    return Q(p[0], p.length === 2 ? p[1] : "1"); }
  const add = (a,b) => Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const sub = (a,b) => Q(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
  const mul = (a,b) => Q(a[0]*b[0],a[1]*b[1]);
  const div = (a,b) => Q(a[0]*b[1],a[1]*b[0]);
  const pow = (a,n) => Q(a[0]**BigInt(n),a[1]**BigInt(n));
  const gt = (a,b) => a[0]*b[1] > b[0]*a[1];
  const eq = (a,b) => a[0]*b[1] === b[0]*a[1];
  const str = a => a[0].toString()+"/"+a[1].toString();
  const bound = {
    source_run: "1ad1682601655468ecacfe22867d20fe849e87406fac64f1d3b3f9c36ab63891",
    packet: "81f6eb0f5c253c13d6aaaa320adbf95bfc6c59dca7a45b888bacd7b6991b770c",
    bundle: "3b312be557d67cda05624e41d46266925fbe3836c48759c613ede6cf52c70b98",
    mean: "161eec0d27afb4a0b81c84ef85c5849259f1c9faf39093bfedfce099fc2fbbe9",
    query: "877e68d97868524ed3cde4bca1090fbe8a4a207370e7b6c761da2b5963378cab",
    geometry: "57480474eab2110d41053fee5ada0f02548dbb1b9e2fbaf56b9a16ce9fea742c",
    combine: "f109408b33c9726fcdc22efeed555c4889edcd8bc96c3cd1ad526fe6833d0676"
  };
  need(r.source_run.sha256 === bound.source_run, "source run");
  need(r.accepted_packet_sha256 === bound.packet, "accepted packet");
  need(r.geometry_bundle.sha256 === bound.bundle, "complete bundle");
  need(r.entire_mean_sha256 === bound.mean, "entire mean");
  need(r.actual_query_sha256 === bound.query, "actual query");
  need(r.geometry_report_sha256 === bound.geometry, "whole geometry");
  need(r.combine_report.sha256 === bound.combine, "actual moment combine");
  need(r.mean_nodes === 1168, "mean quadrature identity");
  need(r.full_modes_retained.join(",") === "170,25", "complete spectrum");
  const ell = read("5764607523034235/1152921504606846976");
  const rc = read("900719925474099/36028797018963968");
  const eps = read("4722366482869643/75557863725914323419136");
  need(eq(read(r.cylinder_total_length_exact_binary),ell), "literal total length");
  need(eq(read(r.complete_cut_width_exact),
          read("1080863910568919/9007199254740992")), "literal cut width");
  const bOverPi = div(mul(eps,pow(rc,5)),Q(140));
  need(eq(read(r.cap_third_moment_divided_by_pi_exact),bOverPi),
       "same canonical cap coefficient");
  const Alo = read(r.whole_activity_real_interval_exact[0]);
  const Ahi = read(r.whole_activity_real_interval_exact[1]);
  const coarse = Q(139,1000);
  need(gt(Ahi,Alo) && gt(Alo,coarse), "true activity exceeds coarse bound");
  const alpha = Q(9,20), x = mul(Q(3),alpha);
  // 1-cos(x) >= x^2/2-x^4/24 for 0<=x<=27/20.
  // This is the alternating cosine-series remainder bound.
  const trigLower = sub(div(pow(x,2),Q(2)),div(pow(x,4),Q(24)));
  need(eq(trigLower,Q(989253,1280000)), "exact cosine bound");
  need(gt(trigLower,Q(0)), "positive cosine bound");
  // B3 = pi*eps*rc^5/140 > 3*eps*rc^5/140.
  const capStrictLower = mul(Q(3),bOverPi);
  const dropStrictLower = div(mul(mul(coarse,capStrictLower),trigLower),Q(2));
  const target = Q(7,10n**19n);
  const gap = sub(dropStrictLower,target);
  need(gt(gap,Q(0)), "tensor norm squared drop exceeds 7e-19");
  return {
    status: "exact_rational_endpoint_tensor_consequence_passed",
    scope: "Same R82/R83 lambda002 raw-H field; R84 reflection proof required",
    source_record_commit: "4cbd74a0b22de4345fee878d9e06de97dd14c102",
    source_record_path: "topics/visible-flex-held-10pct/notes/2026-11-28-actual-closed-third-activity-and-separation.json",
    bindings: bound,
    exact: {activity_lower: str(Alo), coarse_activity_lower: str(coarse),
      endpoint_alpha: str(alpha), three_alpha: str(x),
      one_minus_cos_lower: str(trigLower), cap_moment_over_pi: str(bOverPi),
      cap_moment_strict_lower: str(capStrictLower),
      tensor_norm_squared_drop_strict_lower: str(dropStrictLower),
      requested_drop_lower: str(target), positive_gap: str(gap)},
    hypotheses_from_R84_not_numerically_inferred: [
      "Exact same-map y-reflection at alpha=0 makes A3 real",
      "C3 symmetry and z-reflection remove all rank-three lower weights",
      "I3(alpha)=abs(A3*exp(3i*alpha)+B3)^2/4"
    ],
    endpoint_noncongruence_including_reflections: true,
    numerical_Hausdorff_lower_bound_claimed: false,
    whole_metric_claimed: false,
    README_completion_claimed: false
  };
}
