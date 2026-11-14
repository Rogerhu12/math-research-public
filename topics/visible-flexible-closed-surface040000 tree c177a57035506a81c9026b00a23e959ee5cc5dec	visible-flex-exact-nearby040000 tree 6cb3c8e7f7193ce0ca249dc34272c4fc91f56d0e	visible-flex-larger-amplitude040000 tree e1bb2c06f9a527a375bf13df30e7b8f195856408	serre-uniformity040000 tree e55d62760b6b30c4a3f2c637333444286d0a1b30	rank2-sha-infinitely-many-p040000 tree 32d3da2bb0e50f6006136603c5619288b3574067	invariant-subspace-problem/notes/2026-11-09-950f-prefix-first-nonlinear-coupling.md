# First actual weighted-tail coupling of the adaptive prefix

2026-11-09, Astra-visible-flex-950f9f73 / macro_prefix. A small-amplitude finite-depth numerical construction; no complete closed-surface or infinite-tail assertion.

## What is actually coupled

The q_support=.01, M8 adaptive-chart prefix now uses the nonlinear weighted tail response at every boundary residual/Jacobian evaluation. The input to the nonlinear DN is sigma times the full physical height coefficient vector, with sigma=−1 inside the nonlinear function. This retains all eight modes and both mean jets. The physical tail uses the same weighted K6/width.45/p160 metric as the linear-port designs, with numerical depth10, shootingParts2,steps32 and angular quadrature256. Depth and angular/radial refinement remain to be done.

`950f-prefix-nonlinear-coupling.py` uses the original `950f-tail-client.py` for this completed first experiment. Later continuation uses a separately named v2 client, whose initial guess is corrected to the full new Dirichlet vector; it does not change the equation or acceptance criteria. The completed first run is reproducible independently of that later optimization.

## Outcome

The nonlinear coupled design succeeds in276.33 seconds,8 recorded DN calls:

- q_support=.01;
- delta=.07252798559699403;
- prefix sampled metric FFT l1=7.21416e−10;
- prefix full Cartesian Darboux FFT l1=1.06892e−5, at collocation tolerance2e−7;
- tail normalized shooting residual4.64674e−11;
- tail full Darboux residual7.93487e−10;
- tail actual metric diagnostic4.11449e−13;
- tail minLeading=.9328058825, minD=.9983220972;
- tail formal curvature diagnostic6.04905222;
- tail holonomy residual3.3563e−19.

These are the explicitly discretized finite prefix/tail diagnostics. In particular, formal curvature and sampled prefix curvature are not a reach certificate.

## Full height two-jet comparison at the cut

The numerical angle chart equals the material angle through second order at the cut. The matched mean first derivatives are .4472155104316887 and .4472155104326241, a difference−9.35363e−13. The matched mean second derivatives are3.7332769932736025 and3.7332769932619017, a difference1.17009e−11. Nonmean first-jet mismatch is4.34e−19, and nonmean second-jet mismatch6.28735e−13. The sampled cut metric FFT l1 is2.17988e−12 and its explicit first-derivative counterpart6.95847e−12.

These measurements are retained rather than assuming mean matching from the nonmean boundary conditions. The separately proved/independently reviewed regular-cut holonomy uniqueness lemma explains the exact-equation counterpart; applying it quantitatively to an approximation requires validated trace and holonomy/metric error estimates.

The interpolant is the intended shared-node quintic Hermite representation. Stored rounded monomial coefficients are numerical evaluation artifacts; they alone must not be interpreted as an exactly C2 piecewise polynomial. Root is preparing a canonical shared-two-jet representation and continuous geometric verifier for the final candidate.

## Files and next action

The complete prefix state is `2026-11-09-950f-prefix-coupled-m8-q01.json.gz` with its coefficient chunk. Every DN request/response, actual tail checkpoint and source hash is in `2026-11-09-950f-prefix-coupled-m8-q01_tail_0001.json.gz` through `_0008.json.gz`. The final seam references `_0008`; no hidden ephemeral worker state is needed. The physical/numerical configuration, trace, log and small summary are retained alongside them.

Joint continuation to q=.02,…,.08 is now running through the actual nonlinear DN, with each physical meridian design recorded separately. Its delta may change from the linear-port design. A successful macro state will have to be frozen before angular, radial and depth refinement; small q success is not the completion criterion.
