# R66 application: the existing segment 5 worst leaf, source span, and complete finite spectrum

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted). Date: 2026-11-12.

This is an application of R48 and [R64](../results/R64-general-outer-mean-and-compatible-defect.md) to the **unchanged** eight-substage candidate in [the segment 5 execution](2026-11-12-tail-r66-seg5-substage-application.md). It locates the cause of the old continuous bound. It does not construct another height, integrate another source moment, or certify an exact outer solution.

## 1. Exactly what was replayed

The old global segment 5 Darboux witness was substage 4, stored positive-integral bin 0, with source interval

$$
I=\left[\frac{513}{1024},\frac{257}{512}\right].
$$

The executed helper reads the original true six-integral bins, the two original shared physical two-jets, and the original five total moment enclosures and bubble coefficients. It rebuilds the same R48 candidate and intersects its bubble enclosures with the saved enclosures. Throughout the following checks it retains the **same entire bin** enclosure for the height primitive and radius. No smaller primitive or radius enclosure is obtained by a new quadrature.

Only the real source range $w,w_x/w,r_x$ and the polynomial substage coordinate are reevaluated on four specified sets: $I$, its two halves, and their common midpoint. Both halves include the common endpoint, so together they cover all of $I$. The old candidate's complete Fourier modes $2,4,\ldots,40$ and the analytic norm width $\tau=1/64$ remain unchanged.

The original R64 general mean and actual derivative routine is called on each of those four sets. In particular, the complete scalar mean $c(x)$ and its actual derivative $c_x(x)$ are enclosed by the existing root and compatibility argument. No PDE second derivative is substituted for the candidate's derivative.

## 2. Complete finite $J$ identity

Write $k$ for the nonmean normalized slope, so the complete normalized slope is $K=c+k$. In the notation of R64, set

$$
z=w^2,\qquad E=1+z,\qquad s=\frac{r_x}{r},\qquad
\ell=\frac{w_x}{w},\qquad
P=\frac{h_\theta}{rw},\quad T=P_\theta,\quad U=k_\theta-P.
$$

The candidate's nonmean derivative is the actual derivative $k_x$ of its R48 polynomial. Define

$$
\begin{aligned}
L_{\rm nm}&=k+ET,\\
J_{\rm lin}&=k_x+\ell(2k+T),\\
J_{\rm quad}
&=(k+ET)k_x-EsU^2+\ell(k^2+zP^2+kT).
\end{aligned}
$$

The complete Darboux numerator is exactly

$$
J=J_{\rm lin}+J_{\rm quad}
  +cJ_{\rm lin}+c_xL_{\rm nm}
  +c_x(1+c)+\ell(2c+c^2).                    \tag{1}
$$

To verify (1), expand $L(K_x+\ell(2K+T))$ with $L=1+K+ET$ and subtract the complete nonlinear numerator

$$
Es(K_\theta-P)^2+
\ell\big[(K+T)^2+z(2KT+T^2-P^2)\big].
$$

All scalar-mean terms in the result are exactly the last three terms of (1). This expansion preserves the full mean and inverse-denominator effects already paid by R64. It is not a projection of the Darboux equation.

Since the saved nonmean height and slope have support $|m|\leq40$, $J_{\rm lin}$ and $L_{\rm nm}$ have the same support, and $J_{\rm quad}$ has support $|m|\leq80$. Consequently

$$
\Pi_{40<|m|\leq80}J
 =\Pi_{40<|m|\leq80}J_{\rm quad},\qquad
\Pi_{|m|>80}J=0.                             \tag{2}
$$

In particular, the entire band $42,44,\ldots,80$ and its negative-frequency partners are computed from the quadratic polynomial directly. They do not depend on the scalar mean bounds and are not discarded. The saved package contains every complex coefficient of the complete finite $J$ enclosure.

For every angle the actual physical Darboux defect is bounded by

$$
\left|\frac{w^2J}{r\,r_xE^2}\right|
\leq
\sup\frac{w^2}{r\,r_xE^2}\sum_{m=-80}^{80}|J_m|.       \tag{3}
$$

The right side uses the zero-strip Fourier $\ell^1$ norm. This is a full-angle bound, independent of angular sampling; the prior R64 $W^1_\tau$ bound is retained separately. For an individual coefficient, $\sup_\theta|J(\theta)|\geq|J_m|$, so a strictly positive lower bound on a coefficient gives a genuine nonzero-defect witness at the specified radial point.

The recorded nonmean physical second derivative is computed with its actual signed combination

$$
(h_{rr})_\perp=\frac{w}{r_x}(k_x+\ell k),       \tag{4}
$$

not from the source equation and not by summing the separate absolute values of the two terms.

## 3. Actual interval results

The table rounds upper bounds outward for readability. The primary JSON stores their exact dyadic upper endpoints.

| Set | Upper/lower ratio for $r_x$ | Original R64 physical bound | Complete $J$ bound (3) | Contribution from $40<|m|\leq80$ |
|---|---:|---:|---:|---:|
| All of $I$ | $<148.413$ | $<4.023377$ | $<1.250880$ | $<2.410910\cdot10^{-15}$ |
| Left half | $<4.555240$ | $<0.084657$ | $<0.025971$ | $<5.647458\cdot10^{-17}$ |
| Right half | $<3.706976$ | $<0.065362$ | $<0.019991$ | $<4.458128\cdot10^{-17}$ |
| Common midpoint $x=1027/2048$ | tightly encloses $1$ | $<0.001627$ | $<0.000244233$ | $<5.469747\cdot10^{-18}$ |

Thus **the entire old leaf $I$**, with the same height primitive hull, has the improved continuous full-angle bound

$$
\sup_{x\in I,\,\theta}
\left|\frac{w^2J}{r\,r_xE^2}\right|<0.025971.          \tag{5}
$$

This conclusion uses both half intervals, not the midpoint. It does not yet replace the maximum over the other leaves of substage 4, over segment 5, or over the complete outer cell.

At the midpoint, the physical $m=2$ Darboux coefficient has certified lower bound greater than $3.0610\cdot10^{-5}$. The actual signed cosine coefficient of $(h_{rr})_\perp$ at $m=2$ is enclosed near $-0.00118570888787002357509$, with enclosure radius below $8.47\cdot10^{-24}$. The complete nonmean $W^1_{1/64}$ norm in (4) is below $0.004112$. These facts distinguish the actual finite candidate's nonzero local defect from the very loose old whole-leaf second derivative bound near $23.45$.

The midpoint is still evaluated with the original entire bin's height-primitive enclosure; therefore it is not a high-precision reconstruction of an independent pointwise ODE solution. The coefficient lower bound is valid for the same exact R48 candidate.

## 4. Consequence for the next continuous verification

At this particular witness, enlarging the angular truncation is not supported by the computed defect decomposition: the entire beyond-height band contributes less than $2.411\cdot10^{-15}$ even on the old wide interval. The $r_x$ interval ratio and the signed finite polynomial calculation explain a large part of the previous upper bound.

The next task is therefore to keep this candidate and impose an explicit positive relative-span criterion on $r_x$ while covering every original positive-moment bin. On each accepted subinterval it must retain the unchanged R64 complete root, its real derivative, all source branches, and all finite coefficients through $|m|=80$. A new maximum can be attributed to an entire segment only after that full coverage has actually completed. A further change of candidate or radial coordinate remains available if the resulting actual residual requires it.

Even a successful full segment bound would remain a candidate residual. The outer finite Green/Schur inverse, the true-head matching error, and the nonlinear existence budget are separate unpaid parts of the outer problem.

## 5. Execution, inputs, and preservation

The actual tool session was **93119**, formally exited with code **0**. The resource wrapper independently recorded child exit code $0$, no termination signal, $2.6532769203186035$ seconds wall time, and peak RSS **31460 KiB**. There was no Node, radial ODE, BVP, or new source integral.

The executable is computations/tail_outer_substage_existing_witness.py, SHA256
215c98362ff3857b8c8c9905ef2cc2804846977ef65126d597b171eb202b5a17.
The primary package is notes/2026-11-12-tail-outer-seg5-existing-worst-witness-r1.json.gz, SHA256
2e6fc7e47f5c1d698a8b16b020f380ec32ec52e3daa83c1fac711f824606f099.
Its resource record is the same prefix ending -resource.json, SHA256
4ac192be11f8fd17c31e05cb53fba4d34f3c013c5857123d95f708e7b477f67a.

The primary records the complete candidate and ready input hashes and the frozen dependencies. The accompanying executed manifest contains the exact command, file sizes, and all stable output hashes. The separate prepared partial-integral worst-leaf probe was **not executed** and is not part of this evidence.
