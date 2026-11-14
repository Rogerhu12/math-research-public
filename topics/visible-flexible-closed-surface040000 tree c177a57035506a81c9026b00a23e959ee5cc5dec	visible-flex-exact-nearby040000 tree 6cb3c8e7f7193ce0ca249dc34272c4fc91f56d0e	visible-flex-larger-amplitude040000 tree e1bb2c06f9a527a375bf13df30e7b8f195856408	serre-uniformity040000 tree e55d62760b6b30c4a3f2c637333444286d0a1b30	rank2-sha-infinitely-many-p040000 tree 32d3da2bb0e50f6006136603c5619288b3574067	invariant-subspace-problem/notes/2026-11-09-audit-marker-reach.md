# Independent audit: small fixed markers and reach

Reviewer: Astra independent_audit, 2026-11-09. I did not write the candidate. Review target: `notes/2026-11-09-marker-reach-candidate.md`, SHA256 `58c3044db3757085ef383653fc5c4696182349b85a497d4f29125b060a053c9c`.

**Verdict: PASS as a conditional tool.** The perturbation inequality, the four-marker rigidity argument, and the strict quotient-distance conclusion are correct under the candidate's explicit hypotheses. No candidate closed band or quantitative reach certificate follows merely from this tool.

## Reach estimate

I checked the tangent-chord formula independently against Fefferman–Ivanov–Kurylev–Lassas–Narayanan, *Fitting a putative manifold to noisy data*, PMLR75 (2018), Proposition3 on printed page4. It gives the reciprocal formula and attributes it to Federer1959, Theorem4.18. For the boundaryless C2 embedded submanifolds used here it is the candidate's equation(1). Source: https://proceedings.mlr.press/v75/fefferman18a/fefferman18a.pdf . I did not independently access Federer's original paper.

The proof of (2) is valid: if v=q-p and v_N is its normal projection at p, reach>=rho implies |v_N|<=|v|²/(2rho). The line-integral Taylor remainder contributes at most L|v|²/2. Applying Df(p) to the tangent part lands in the new tangent space, so the distance of the new chord from that tangent space is at most (M/rho+L)|v|²/2. Dividing the lower chord bound m²|v|² by twice this expression proves m²rho/(M+Lrho). The explicit use of a global lower Lipschitz bound is necessary and correctly retained.

For f=id+u, the estimates m=1-eta and M=1+eta follow from the global derivative bound. The argument establishing a global diffeomorphism from eta<1 is also valid: local invertibility, global injectivity, and properness imply an open and closed nonempty image in Rn. Bounded second derivatives make Du globally Lipschitz with constant L in operator norm. The stated full-space extension requirement prevents using the line segment remainder outside the domain of definition.

The unmarked family is one ambient rotational orbit when the fixed unmarked caps are rotationally invariant. Therefore one true baseline reach bound works for all phases. A fixed ambient displacement supported away from every rotating band preserves this reduction and permits (3) uniformly. The comparison with .03(D0+2epsilon) correctly accounts for possible diameter increase; small curvature alone would not establish the baseline reach hypothesis.

## Markers and reflections

For each fixed b>0 and nonzero positive amplitude, the proposed bump is smooth away from its center and support edge, C3 across its support edge, and exactly C^{2,beta} at the center. Along a radial line the Hessian difference has a nonzero constant times r^beta as leading term. Since beta<1, the center is not C3 and not C^{2,alpha} for alpha>beta. On the punctured disk it is smooth. Thus the only new isolated non-C3 points are the four centers.

The support disks lie in the interior of a planar cap, so they are separated from the original non-C3 locus. The original hypothesis that its bad locus has no isolated points ensures that no other isolated points compete with the marker centers after the modification. This hypothesis is indispensable and must apply to the actual unmarked surface, including every seam and pole.

The local Hölder thresholds are properties of the unparametrized embedded surface: orthogonal projection to the tangent plane provides a regular graph, and a hypothetical higher-regularity surface chart would make that same graph higher regularity. Consequently every Euclidean congruence maps centers according to their distinct thresholds. Their positions being fixed throughout the family, each is fixed individually by any putative congruence between two phase images.

Take all four centers in the same planar cap as in the stated implementation. The first three planar centers must be noncollinear. Their equal heights epsilon span a plane parallel to the cap, and the fourth point at height2epsilon lies outside that plane. Thus the four spatial points are affinely independent for every epsilon>0. An element of E(3) fixing them individually is the identity; this excludes improper rotations and reflections too. Together with a strict image-change witness, this proves noncongruence.

There is no conflict between arbitrarily small C2 marker norm and a nonzero Hölder signature. With fixed supports and a fixed smooth ambient cutoff, both derivative bounds are proportional to epsilon. Each signature remains nonzero for every epsilon>0. Hence strict baseline reach margin permits small markers while maintaining the required reach ratio. Marked caps may have nonrotational material metric; because they remain pointwise fixed, that metric is nevertheless the same for all phases, as the README requires.

## Quotient Hausdorff distance

For compact nonempty K,L, a sequence of rigid motions with bounded Hausdorff distance has bounded translations after fixing one point of K. Compactness of O(3) then gives a convergent subsequence. Compactness of K makes the images converge in Hausdorff distance. Therefore zero infimum would imply an exact congruence. This proves (7), and the same bounded-sequence argument proves attainment of the infimum. No effective numerical lower bound for that positive minimum is supplied or needed for the README's strict-positive requirement, provided the exact noncongruence proof applies to the realized surface.

Promotion should retain the explicit hypotheses: actual closed C2 band, open circular collars, genuine global baseline reach margin, marker support separated from all rotating bands, controlled ambient derivative bounds, and verified absence of other isolated non-C3 points. Without these the proof remains an admissible conditional result, not a completion certificate.
