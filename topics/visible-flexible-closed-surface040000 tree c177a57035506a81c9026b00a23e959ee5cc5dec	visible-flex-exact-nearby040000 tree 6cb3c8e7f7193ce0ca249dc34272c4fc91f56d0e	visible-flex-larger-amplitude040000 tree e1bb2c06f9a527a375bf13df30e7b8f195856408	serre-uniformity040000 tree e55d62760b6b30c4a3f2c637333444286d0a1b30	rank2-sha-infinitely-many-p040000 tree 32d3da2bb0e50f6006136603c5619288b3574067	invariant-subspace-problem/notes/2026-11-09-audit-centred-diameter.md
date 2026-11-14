# Independent audit: centred diameter and held displacement

Reviewer: Astra independent_audit, 2026-11-09. I did not participate in writing the candidate proof or the numerical envelope script. Review target: `notes/2026-11-09-centred-diameter-candidate.md`, SHA256 `aab6e1db9e5b905d3fb85c0c9ad18f9b1bdd9694486e854bb1d712d64b70c7fe`. Numerical script SHA256 `ca8f65f730ef1a2b6fd8517cdac8f64825783334884d1001523b0222c119c24c`.

## Verdict

**Sections1–3 pass as conditional geometric lemmas.** They supply neither a completed isometric closed family nor a positive E(3)-quotient displacement. Section4 is only a numerical design screen and must remain so. One concrete radius inconsistency in its proposed use with the named old checkpoint needs to be corrected before this numerical budget can describe a continuous tail attached to that checkpoint.

## Proof checks

For a nonempty compact centrally symmetric set S, the triangle inequality bounds the diameter by twice the maximum norm, and the pair x,-x attains it at a maximum-norm point. The two-sided Hausdorff perturbation estimate with coefficient2 follows by choosing near points independently for both endpoints. Both facts are valid in any Euclidean dimension.

The stated half-turn symmetry of the upper prefix, together with reflection through z=0, indeed produces central symmetry. The reflected pair has the same norm envelope. Including the central column is essential; its norm maximum is attained at u=+-ell and is already covered when the prefix inlet is the entire column section. The tail/cap estimate is a geometric containment inequality and does not assume a nonexistent cylindrical corner is on the surface. An asymmetric marker retained inside the same ball preserves the upper diameter bound even though equality with twice the maximum norm is then no longer justified. The candidate makes that distinction correctly.

For held displacement, p=(0,R,0) is in the image at the specified quarter-turn phase. Every old central-column point is at distance at least R-r from p by its y-coordinate; every other old point is at distance at least ell by its z-coordinate. Taking the infimum over their union gives the stated min bound, hence a directed and then symmetric Hausdorff bound. Only the original image requires the support/separation assumptions. The argument does not permit a free alignment and does not purport to bound delta_E. The union of the two fixed closed cap pieces has nonempty relative interior and has the required diameter when the specified two points have separation at least .2D.

When using these lemmas at ell=.26, record explicitly the needed *continuous* facts R-r>=.26, original noncentral points |z|>=ell, occurrence of the quarter-turn phase, and the stated fixed H. In particular, a sampled y-support is a lower estimate of the continuous maximum, so subtracting it from R yields an upper estimate of R-r. The sampled .26099102072 alone is not a rigorous lower bound. It also does not prove exact isometry or an admissible family.

## Independent rerun and radius correction

I reran the named script on the unchanged M8/aspect1.3 checkpoint with1024 angles and4 subdivisions per stored radial interval, doubling each original setting. Output: `notes/2026-11-09-audit-centred-envelope-rerun.json`. At ell=.26 the sampled centred diameter is4.468548513530465, coarse cylinder diameter4.952830061838891, and maximum height2.1416979838923496, agreeing with the stated values at floating-point precision. This agreement remains a sampling check and does not enclose the continuous maxima.

A separate calculation using my own Fourier basis and direct PPoly evaluation, without importing the candidate solver or the envelope implementation, gives the terminal point at theta=0:

$$\rho_{\rm terminal}=.6008466383529977>.6.$$

The coefficient chunks were hash-verified; metadata and evaluation are in `notes/2026-11-09-audit-terminal-radius.json`. The actual x-axis point is enough to show that a tail continuously attached to this fixed checkpoint cannot have every point at rho<=.6. This is not a continuous-maximum estimate: it is an explicitly evaluated violating point with a gap approximately8.47e-4. Excluding the common boundary from the tail's set does not fix the issue, because continuity retains rho>.6 in a neighborhood of that boundary. The material coordinate r=.6 is not an upper bound for the physical radius of a noncircular isometric section.

A modified conditional budget can take a slightly larger physical radial bound. For instance, using rho<=.601 leaves the height limit sqrt(2.6²-.601²)=2.52958474853, only .00023737960 below the original limit. A more generous rho<=.61 gives2.52742952424. Neither number establishes that any actual nonlinear tail stays inside the corresponding cylinder; it only quantifies an available budget correction. The core radius support and all tail extrema still require continuous estimates.

Thus the abstract condition in Section4 is logically valid, but its rho<=.6 premise is unattainable for a tail attached to the exact saved approximate prefix as named. I recommend promoting only the proved conditional lemmas and retaining the numerical screen with this interface correction and its unverified-hypothesis labels.
