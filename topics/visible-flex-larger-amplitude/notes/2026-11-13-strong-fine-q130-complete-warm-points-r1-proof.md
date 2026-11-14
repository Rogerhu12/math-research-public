# Actual fine q130 complete warm geometry and stored-point bounds

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

## Identity and result

This package consumes the actually accepted M32 q122 baseline with SHA `4c0e13b2ea4e2541e75891a3b4fafa93ffc2f8331cfdcdc7e4083ac3cbfef1ad` and its original complete raw state. The saved six-control increment comes from the identified M28 partial response. It is a design increment, not an M32 Jacobian. The complete prepared 32-mode core is reproduced bit for bit by the actual warm field; the extra four fine modes retain the accepted fine baseline. The earlier full-core/inlet archive is `2026-11-13-strong-fine-q126-q130-full-core-inlet-r1-manifest.json`.

The original constructor is `strong_coarse_response_warm_actual_bvp.py` SHA `ff5acad191d51544bfebaf46902f7e58f89a2e4575130f9b33932aa25ef8972c`. The mean wrapper is `root_actual_coarse_increment_geometry_complete_mean.py` SHA `c986073622d4ebabb2be7d1eea46fe8ac4966a404b56bbc6a6af3b48371092bc`. The explicit corrected frontload anchor SHA is `583af82cdd6bb672325844587d8aac67e47365ccb5152ac2eae543837adc0ffc`; this candidate has the original zero frontload. No original frozen source is edited.

The geometry run actually finished with owned wait4 exit 0 in 293.797880 seconds and peak RSS 192964 KiB. It retained all 2587 original raw nodes and modes. The fixed common grid has 3764 radial coordinates and 768 material angles. Every mean-height integral, first radial mean, and second radial mean uses the complete original M32 rule of 1552 angular nodes and radial Gauss order 6; geometry batching is 8. This is the original physical-s cubic warm interpolant through the raw values, not the accepted physical quintic of a newly solved candidate.

The finite samples give curvature maximum 8.3358960676677523, S=2 max|X|=4.0420837353363543, their product 33.694389914574096, minimum tangent area 0.22033687591655188, and minimum Frenet margin 0.0051320220400644656. The full changed boundary height is saved, with maximum change 4.4545499260923566e-07. The warm wrapper did not solve a new tail, compute a new physical audit, or certify the continuous domain.

## Capturing the actual finite points

The storage-only adapter `root_actual_coarse_increment_geometry_points.py` SHA `d7e56def8759411b626914ec41a80c72f21c4069e4e8484bcac62532642744ba` stores the Cartesian array already produced inside the original geometry loop. Its transformation is exactly reversible to the pinned original main. Mean, height anchor, profile, derivatives, curvature and domain formulas are unchanged. The actual field and point arrays each have shape [3764,768,3]. The point consumer verifies every contiguous chunk, dtype, finite value, SHA and full prepared-core bits before reading the complete 2,890,752-point set.

Let P be precisely these stored Cartesian binary64 triples, interpreted as exact dyadic rational points. The consumer reports separately the explicitly constructed diagnostic set Q=P union Rz(P), Rz(x,y,z)=(x,y,-z). Q is not asserted to be an existing complete closed surface. This distinction prevents using the much smaller one-sided prefix diameter as the full closed-surface diameter.

The exact rational bounds in the primary file give:

| Stored finite set | Diameter lower, displayed | Diameter upper, displayed |
| --- | ---: | ---: |
| P | 2.7484845494059669 | 2.8026330536037132 |
| Q | 4.0420837353363535 | 4.0420837353363552 |

The displayed decimals are summaries; the saved exact numerator/denominator pairs are authoritative. In Q the exhibited nearly opposite pair almost attains the origin-centered upper diameter S. Thus this finite reflected diagnostic does not reveal a material overestimate in S. It neither supplies nor assumes the future global closed-surface D.

## Exact finite-point bound

Every exhibited pair is subtracted and squared with Python Fraction from the actual binary64 coordinates. Its exact squared distance gives a lower bound after an integer-square-root dyadic sandwich at 90 bits. The coordinate extrema also give an exact bounding-box squared diagonal. Additional upper bounds use complete scans about several actual binary64 centers. These centers may be chosen heuristically because the subsequent complete scans certify each enclosing ball independently.

For u=2^-53, the explicit three-coordinate computation qhat=sum(fl(fl(X-c)^2)) has at most five relative factors on each positive contribution: two from the squared subtraction, one multiplication, and at most two positive additions. With all coordinates and centers bounded by 1024 and no overflow, exact squared distance is at most qhat/(1-u)^5+2^-1000. The explicit absolute allowance exceeds the finite number of possible subnormal terms. Taking the maximum over every point and then the exact 90-bit upper square root gives a valid enclosing-ball radius for P; the origin-centered ball also covers its reflection. The minimum of these valid upper bounds remains valid. The selected lower and upper bounds are checked not to cross. This is a proof about the stored rational point set, independent of whether the scientific geometry evaluation itself is interval certified.

The complete 32-core also supplies an exact rational algebraic R7 diagnostic using the original axis-gap and short-axis-radius formulas: axis gap 0.2586240856106527, short-axis radius 1.5214040412927203, and product k0*gap*rho 0.24459738929391259. This does not replace a continuous core or embedding proof.

## Reproduction and storage

The two owned resource records contain the exact original argv and actual exit status. The geometry-prepared record and screen preserve all source and actual-input hashes. The grid is the previously archived `2026-11-13-strong-q122-fine-coarse-warm-geometry-preparation-r1-grid.json`, SHA `e484654f5c06141c1687bef06ff361a103ed96968411bdc1b18161eef37fdd36`. Restore it to the original working path together with the already archived accepted raw arrays, complete partial-response arrays, provider sources, and files listed by the original constructor. Run the recorded geometry command once, then the recorded point-bound command. The resident writer uses deterministic gzip chunks; each regenerated field and point chunk must match the complete manifests. No sampling reduction is permitted in reproduction.

The 36 reproducible derived chunks for this candidate stay in scratch under `geometry-work/m32-q122-r1/q130-tail4-size1035-r1-{field,points}-part*.npy.gz`, as required by repository rule 11. Their full hashes and exact chunk coverage remain in this archive. Only the small source, complete metadata, resources, finite-point certificate and proof are committed. No new ODE, Node, Newton or true-H solve was called by either producer.

## Explicit limits

The curvature and Frenet extrema are finite numerical samples. The exact finite-point bound does not pay physical continuum interpolation, original floating/libm evaluation, global closure, reach, fixed-H geometry, set Hausdorff variation, or Euclidean-motion minimization. The original partial-response combined-half limitations remain unchanged. This package does not establish the topic's completion conditions or a new accepted nonlinear solution.
