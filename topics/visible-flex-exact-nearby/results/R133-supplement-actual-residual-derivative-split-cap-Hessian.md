# R133 supplement: actual residual derivative split for the same cap direction

## 1. Actual public execution and identity

Public workflow **43621690619**, attempt **1**, succeeded on 2026-11-14.
The mathematical child returned **0**, passed **nine gates**, and consumed
all **1341** original local Hessian rows and **1977** original Hermite
intersections. Mathematical time was **2.042509057000018 seconds**;
recorded child wall time was **5.000518615000033 seconds**. No new
target, trial, endpoint, or original cap residual calculation ran.

Evidence directory:
`notes/residual_split_cap_Hessian_ci/run-43621690619-1-same-w0-residual-split-cap-Hessian/`.

| Evidence | SHA256 |
|---|---|
| Full native, 2694759 bytes | `85b6bbb899ab04549131fd20a7b16209056e2a51cb012bffbd7a6ae590b047c5` |
| Summary, 19477 bytes | `bcdc7998f6a620230ab323fe51bdbb8f920b160d8169d946a3f6ce8299b05e7e` |
| Read repository process snapshot, 11901 bytes | `542eb0344e5f87aaf61b3071e4803f9bb0b91ff1eae255cf75d85ccf1c218f9f` |
| Mathematical producer | `a8b1a68d1be78b6288aa5e6db314caded7f80158045a4e7acb959c7e84c25317` |
| Reviewed worker | `0f5bb7c3c747a5e62ac52b40d17ee7dda398f044c30c6c723dccc4b8e7eb0b9b` |
| Immutable 164-file manifest | `a3b144b5a6e8c9d84c369f97aac1e849e3035bb7067c461ed574b53b1069d842` |

Native: `native/complete-same-w0-residual-split-cap-Hessian.json.gz`.
Summary: `evidence/complete-residual-split-cap-Hessian-summary.json`.
The process hash identifies the repository snapshot actually read, not an
assumed identical Actions-artifact snapshot. Its four recorded real
pull/README checks have empty differences. Last read commit:
`67774f52bafd29607782989c1866291ee20282be`; separately reviewed rules:
`ee26c0a65a2e63c15f2ccfba6714181584416542`.

Candidate:
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`.
Repaired centre definition:
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`.
Same 97-dimensional orthonormal even direction:
`f77f64367593908c9dd3ba8ac318090275a3b59aa43542620858aadce7b0cbd0`.
The interval is $[9/10,25/8]$ at **affine offset zero, meaning fixed
physical $\eta_0$**.

## 2. Complete four-source calculation

The exact identity and joint residual construction are proved in
`2026-11-14-R133-residual-split-cap-Hessian-contract.md`.
For $x=Tw_0$, the known term $-e x_\theta$ remains an ordinary source.
The term $-t_\theta e_h$ becomes
$\partial_\theta(-t e_h)+t(Ch_2-\langle Ch_2\rangle)$.
Both independent mean pairings remain. The divergence source uses the
complete joint module without a radial length factor.

Original raw residual norms are joint Fourier/radial bounds. The repair
contribution is conservatively promoted by all 193 complex slots.
Composition retains the actual inverse-angle displacement and common
nonnegative convex-chord weights. No unknown Fourier cutoff is imposed.

All 1341 new decompositions were consumed. Local selection used the new
decomposition in 726 rows, but that local score did not minimize the
global bound. The consumer compared three **complete** global bounds
and selected the all-new four-source estimate.

| Complete quantity | Directed outward upper bound |
|---|---:|
| New ordinary $B$ source | $1.369001\,10^{-9}$ |
| New ordinary $C$ source, with mean | $1.391734\,10^{-9}$ |
| New divergence $B$ module | $1.623628\,10^{-8}$ |
| New divergence $C$ module, with mean | $1.418663\,10^{-8}$ |
| Four-source physical Green image | $9.297329\,10^{-7}$ |
| Original Hessian resolvent multiplier | $1.003854964897$ |
| Selected same-$w_0$ additive | **$9.333170\,10^{-7}$** |
| Locally mixed complete additive | $9.634153\,10^{-7}$ |
| Previous two-ordinary-source additive | $1.348922\,10^{-6}$ |

The exact selected value starts
$9.33316914410230614809265485970314268606\,10^{-7}$.
Every ordinary/divergence channel, full mean, original closed physical
Green gain, and original Hessian resolvent is paid once.

The old ordinary estimate was dominated by its $B$ cross term
($<4.057676\,10^{-8}$) and $C$ diagonal term
($<3.689806\,10^{-8}$). Their new ordinary bounds are
$<9.478517\,10^{-10}$ and $<1.226619\,10^{-9}$.
The retained divergence channels dominate the new additive.
These are upper-bound components, not actual-error lower bounds.

## 3. Permission and outstanding work

This replaces only the same-$w_0$ Hessian additive in

$$
 \varepsilon_{\mathrm{mov}}(w_0)
 \le H_{\mathrm{res}}\varepsilon_{\mathrm{phys}}(w_0)
       +E_H(Tw_0).
$$

The original complete moving **error-operator** norm still pays the
difference between the actual cut input of $Z$ and $w_0$. The physical
cap error and its fourteen source/boundary fees are unchanged here.
True 97-dimensional, independent mean, and known-high cut conversions
remain mandatory.

The nine gates verify exact local rows, the full physical background,
both completed trial-norm inputs, full means, all gains, the complete
intersection cover, joint module fees, and comparison only of valid
whole additives. They do not prove a new cap error-operator norm, a
complete true cut source, the $1/200$ response-error gate, or the
infinite-dimensional BVP inverse. True-cut and cached Green consumption
remain separate.
