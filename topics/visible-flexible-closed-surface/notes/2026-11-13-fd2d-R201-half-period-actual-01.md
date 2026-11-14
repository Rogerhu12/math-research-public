# R201 actual full-half R196 branch: first accepted nonlinear step

This is a finite numerical result. It is not a continuous metric, curvature, reach, seam, or held-set certificate. The exact construction is R201. It permits non-reflection angular fields while retaining the proper half-turn and complete angular closure through an exact mean phase.

## Actual input and explicit new field

The input is the already published strong-gap state
`notes/2026-11-13-fd2d-R196-strong-gap08-zero-04.json`,
55,923 bytes, SHA256
`145f72e8facb8b1f7d9f962d0d7e1f63f952625ab423a76bcf76cc156d408f16`.
It has 30 radial cubic functions, 7 positive angular frequencies and 481 original coefficients. It is not the unpublished fixed-height .600 J32 input. No .605 input was available.

The new 931-coefficient vector copies all 481 old coefficients exactly. For each radial basis function it appends one constant theta coefficient, seven cosine theta coefficients and seven cosine psi coefficients. There is no angularly constant psi coefficient because R201 proves it is a phase redundancy. The frozen profile, spline knots, central seed, height and radius columns retain their original mathematical definitions.

The explicit warm changes are only these three appended entries:

| Global index | Value | Role |
|---|---:|---|
| 692 | .0015 | theta cosine frequency 2 |
| 835 | -.002 | psi cosine frequency 4, different radial support |
| 706 | .0007 | radially varying constant theta |

The old coefficients are unchanged at this warm start. This is a declared new field, not an assertion that the perturbed field is identical to the old one.

## Complete function and derivatives

The adapter integrates the full raw angular functions on $[0,\pi]$ with composite Gauss 8. It includes the full mean-phase parameter chain $\beta_p,\beta_{sp},\beta_{ssp}$. Its primitive uses the R201 full-mean kernels for both horizontal coordinates and the weighted vertical moment. It does not reuse the old quarter reflection or a finite DFT derivative.

Physical Cartesian $X,X_s,X_u,X_{ss},X_{su},X_{uu}$ and every active theta, psi, height, cut-height and radius column are calculated. The curvature guide is the frozen R191 Gram/normal/orthonormal-II calculation. The R203 geometric guide is adapted to half-period sampling, retaining both held targets, both signed width rows and both signed height rows. The cut-height domain is [.41,.62].

The finite objective uses guide 9.5, curvature weight .01, geometry weight 10, radius guide 1.59, width .84 and held distance .65. These are search guides. Their sampled residuals do not prove the corresponding global geometry.

## Actual implementation evidence

The first V8 loader attempt failed with `ReferenceError: require is not defined` before constructing or evaluating the provider. A loader with an explicit unused CommonJS require stub then read the same frozen dependencies. This was a runtime integration failure, not a mathematical rejection.

At five common physical points the zero-injected new family and the old family agreed in the complete Cartesian twojet to at most $7.994\times10^{-15}$; the cut comparison was exactly zero in the finite evaluation.

At eight points a mixed nonzero direction included the new theta cosine, new psi cosine, radial theta constant, height, radius and cut-height columns. The relative Cartesian-twojet difference against centered finite differences was $7.5460\times10^{-12}$; the corresponding actual-curvature hinge relative difference was $1.9938\times10^{-9}$. The source used for this local check was subsequently changed only in the diagnostic label `quarterNodes` to `halfNodes`; the complete later normal/LM evaluation used the final published source.

The full old-quarter versus new-half finite normal comparison, on the exact zero injection and with the same metric, curvature and complete geometry target, gave:

| Quantity | Actual value |
|---|---:|
| Old squared objective | .03366216223145398 |
| New squared objective | .033662162231453976 |
| Maximum absolute difference of old gradient columns | 4.82947e-15 |
| Relative old-gradient difference | 3.87439e-15 |
| Maximum absolute difference of old normal block | 2.04636e-12 |
| Relative old-normal difference | 9.18220e-16 |
| Maximum new-column gradient at the symmetric state | 7.51312e-16 |

The nearly zero new gradient is consistent with the reflection-invariant objective at a reflection-symmetric field. The explicit nonzero warm changes therefore precede the actual new-freedom step; the zero injection alone is not presented as an escape from that class.

## Actual accepted step

The complete calculation ran in functions V8 cell `g4:48` and completed after 170.965 seconds. There was no OS child and no invented exit code. This duration includes both normals in the old-injection comparison, the new warm normal and one true nonlinear trial.

The original scaled band/Schur LM policy used $\lambda=.0011111111111111111$. The first actual full step $\alpha=1$ passed Armijo:

| Quantity | Before | After |
|---|---:|---:|
| Full squared objective | .03417570003372766 | .026862372993332113 |

The actual/predicted reduction ratio was .5237520328620271. Only one actual trial evaluation was needed. The accepted state has all 450 new coefficients nonzero in its finite stored vector; their maximum absolute value is .001987813917332142 and their Euclidean norm is .011417197920286292.

The 931-dimensional solve retained the exact declared radial locality, with block size 31 and half-bandwidth 4. No nonzero off-band entry was discarded. The maximum residual in the original scaled damped equation was $5.13912\times10^{-17}$.

The accepted finite state still has substantial deficiencies:

| Diagnostic | Accepted finite value |
|---|---:|
| Maximum sampled relative metric defect | .32715250284397357 |
| Maximum sampled principal curvature magnitude | 22.79283901525772 |
| Minimum sampled phase-mean radius | 3.057168838349672 |
| Maximum sampled absolute y | .9154611606697547 |
| Maximum sampled excess above the cut-height slab | .017432042727443586 |
| Minimum sampled held-target distance | .5933317852424734 |

These values are retained rather than hidden by the successful Armijo step. They do not meet the strong completion target.

## Reproduction and saved definitions

The accepted checkpoint includes all 931 actual coefficients, all normalized knots, the central seed, profile/candidate identity, complete new layout, source hashes, geometry/curvature settings, the actual trial trace and the actual solve diagnostics. Its schema is `fd2d-R201-full-half-actual-checkpoint-v1`.

With a working Node executor, the new standalone driver reproduces the declared initial branch as follows, from the topic directory:

~~~sh
node scripts/fd2d-run-full-half-position-R201.cjs --input notes/2026-11-13-fd2d-R196-strong-gap08-zero-04.json --candidate notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json --warm-changes notes/2026-11-13-fd2d-R201-half-period-warm-changes.json --out-prefix notes/2026-11-13-fd2d-R201-half-period-reproduce --steps 1
~~~

The driver itself was syntax checked in V8; it was not falsely reported as an executed Node process during the outage. It calls the same actually exercised factories, normal kernel and original actual-value LM policy.

The full half-period provider, geometry wrapper and explicit-block normal kernel are new files. The old R196, R191, R195 and R203 sources remain unchanged. The exact R201 definition still requires complete-integral error bounds and accurate-profile/central-seed composition to support a continuous final certificate. The subsequent developed-tail reference is a separate representation change, particularly because mean section height and inner flat-cuff height differ.
