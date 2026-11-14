# Independent audit: regular-cut Cartesian two-jet lemma

Reviewer: Astra independent_audit, 2026-11-09. I did not write the lemma or participate in the main prefix/tail construction.

Review target: `notes/2026-11-09-fixed-metric-cut-two-jet-lemma.md`, SHA256 `cd7a103e99790a51c3b644141092171365af8e92b06c8ee7e57ff82626b80598`.

**Verdict: PASS for the exact local lemma, on one connected cut with the stated nonzero T and b and common branch.** Its formulas determine all Cartesian derivatives through order2 from the complete height two-jet and fixed metric, up to one proper planar rotation and translation. The stated planar rigid-motion freedom includes this sufficient alignment. No nonlinear existence or closure is inferred.

## Formula checks

Let x_theta=T*t and x_s=c*t+b*n with n obtained from t by a positive quarter-turn. The exact metric identities imply

$$T^2=a^2-p^2,\qquad c=-qp/T,\qquad b^2=1-a^2q^2/T^2.$$

I independently differentiated these equations. The expressions for T_theta, T_s, c_theta, b_theta, c_s, and b_s in the candidate all agree. Comparing the tangential part of x_theta_s with x_s_theta gives

$$b\alpha_\theta=c_\theta-T_s=-\frac{aa_sT^2+a^2qu}{T^3},$$

including its sign. Comparing the normal part gives T*alpha_s=b_theta+c*alpha_theta, again with the signs as stated.

Since both immersions have the same scalar fields in these equations, their tangent-angle derivatives agree. On a connected cut the two tangent directions differ by one constant planar rotation. This remains valid around a closed angular period by working with an angle lift: both angle lifts have the same increment. Integrating x_theta then leaves only one translation. With the same chosen sign of b, the aligned x_s agrees. The candidate's three displayed second-derivative formulas follow directly by differentiating t and n; therefore the aligned x_thetatheta, x_stheta, and x_ss agree as well.

The complete height two-jet hypothesis supplies h=z_ss, so b_s and c_s are determined without invoking a further Darboux existence theorem. A constant vertical translation is harmless if one describes the height values modulo a constant; if the literal height values already agree, that translation is simply zero. For multiple disjoint cuts, separate rigid alignment constants would be determined on each component unless global geometry links them; the lemma is stated for one chosen cut.

The sign branch is essential. For a rotational reference with t=e_theta and n=-e_r, b=-a_s. Thus taking a positive root indiscriminately would change the inward/outward branch. T>0 and |b|>0 are precisely the nondegenerate horizontal projection conditions used by the proof. They fail at the standard vertically extruded cylindrical core, as the note correctly says.

## Inward-tail chain rule

Writing the standard positive-background tail height as u(r,theta) and the prefix height as z=sigma*u with r_s=sigma/sqrt(E) gives

$$z_s=u_r/\sqrt E,\qquad z_{ss}=\sigma(u_{rr}/E+u_r a_{ss}),\qquad a_{ss}=-E_r/(2E^2).$$

The same formulas apply to the mean and nonmean components. Evaluating the nonlinear DN on sigma*H, rather than moving sigma outside a nonlinear map, is necessary. These expressions coincide with the previously independently checked inward-bridge convention.

## Quantitative caveat for approximate maps

The exact displayed algebra is locally Lipschitz with denominator bounds T>=T_min>0 and |b|>=b_min>0 and bounds on the remaining inputs. Integrating the angular formulas over a finite period preserves a finite error constant after one alignment.

For approximate isometries, however, **pointwise C0 metric error alone is insufficient to bound a Cartesian two-jet seam**. The differentiated metric identities introduce first derivatives of the metric error. A quantitative extension therefore needs suitable C1 bounds on the metric defects, or a direct Cartesian two-jet comparison. For example, a small oscillatory material reparametrization s->s+(epsilon/k)sin(ks) of a planar radial graph leaves the entire height jet zero and changes its metric by O(epsilon), while producing Cartesian second-derivative changes of order epsilon*k. This demonstrates why the candidate's phrase "plus the metric defects" must include their derivative control when used quantitatively. This qualification does not affect the exact lemma.

## Finite M8 diagnostic labeling

I also read `2026-11-09-fixed-metric-actual-tail-interface.md`, `fixed_metric_progress.md`, `fixed_metric_cut002_finite_convergence.json`, the recording worker, and its manifest. All28 entries in `fixed_metric_artifact_manifest.json` matched their listed local SHA256 values at audit time. The frozen tail snapshot hash is the same source independently audited in `2026-11-09-audit-cut-tail.md`.

The physical parameters are unchanged between the stated M4 and M8 cap=.02 tests. M4->M8 changes the mode count, angular quadrature, and actual cusp-integration grid; the notes explicitly acknowledge that this is not a pure frequency-only comparison. The subsequent M8 radial64->128 pair changes only the radial solve/audit resolutions among the stated configuration fields, preserving the physical source and numerical calibration settings.

The labeling correctly distinguishes tiny shooting residuals from the full normalized Darboux defect. The latter stays near2.96944e-8 under M8 radial doubling; this is evidence that this radial change does not dominate the observed defect, not evidence that the full defect is converging to zero. No additional frequency/depth limit or exact collar is established. The algebraically tiny metric diagnostic does not certify the induced metric of a globally developed approximate Cartesian map. Such a conclusion would still require an integrability/development error estimate or an actual map audit.

The notes now explicitly separate the N80 finite-tail data from the later N160 geometry and state the independently found deep-background curvature failure. This is the correct scope. The finite M8 diagnostic can remain as reproducible local evidence, but cannot serve as a completion certificate or as fixed-geometry refinement evidence for a new N160 candidate.

### Author clarification checked

The author subsequently appended the explicit C1-metric-defect/direct-Cartesian-audit qualification. I checked that addition in the updated lemma, SHA256 `227653108145c193dca156e6a282d3e291231121ec0c5bd6139c31d8993fa1e2`. The exact proof is unchanged and remains PASS; the quantitative caveat above is now explicitly reflected in the candidate note.
