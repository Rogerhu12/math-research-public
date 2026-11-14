# Independent audit: tangent-angle threefold core

2026-11-09. Reviewer: independent_audit, not involved in the candidate construction.
Status: **PASS as a local exact core and conditional separation lemma.** No assertion about the nonlinear prefix/tail, a closed surface, reach, or the full task follows from this review.

## Frozen source

- `notes/2026-11-09-tangent-angle-core-candidate.md`
- SHA256 `4409d1ba39c6474e834d887424ee778bcc6f302d09dc578eaefe13ab29d76275`
- Git blob of reviewed bytes `1d1ef2e454c68d56f36f1c550e78f0e6f3e8d7b2`
- Independent exact-rational evaluation: `2026-11-09-audit-tangent-angle-core-bounds.json`.

## 1. Closure, convexity, and the fixed cylinder metric

Set $\tau=2\pi/3$. From $\phi(\theta+\tau)=\phi(\theta)+\tau$, each third-period tangent integral is the previous one rotated by $e^{i\tau}$. Their sum is zero. The zero-mean primitive therefore exists, is periodic, and has exactly the same equivariance. Unit speed and $\kappa=1+3b\cos3\theta$ are immediate by differentiating the exact tangent, so $0<b<1/3$ gives positive curvature and a single turn.

To check embeddedness without assuming it, fix a parameter $\theta_0$ and its normal $n_0=e^{i\phi(\theta_0)}$. The derivative of $\gamma\cdot n_0$ is $-\sin(\phi-\phi(\theta_0))$. Strict monotonicity of $\phi$ implies strict decrease until the opposite normal and strict increase thereafter. Hence $\theta_0$ is the unique maximizing parameter for this normal. Any repeated curve point would contradict uniqueness for the first point's normal. Thus the curve is simple and strictly convex. The generalized cylinder has exactly $ds^2+d\theta^2$.

The same argument applies to the finite multi-sine angle under $\sum_j3j|b_j|<1$. Closure and speed do not need that inequality; it is a sufficient condition for strict convexity.

## 2. Fourier identities and the truncation bounds

The product of the two absolutely convergent exponential series gives the stated Bessel expansion. Integrating $i e^{i\phi}$ divides its coefficient by $1+3k$, which never vanishes. For $k\ge0$, replacing $(j+k)!$ by $k!$ bounds the coefficient by $e^{B^2/4}(B/2)^k/k!$. This also justifies all fixed-order angular derivatives.

For the first derivative, sum the positive and negative omitted indices. Their successive factorial terms have ratio at most $x/(M+2)$. For the second derivative, the paired frequency magnitudes sum to $6k$, and the corresponding ratio is at most $x/(M+1)$. This reproduces both candidate bounds. The position estimate follows from the least omitted denominator $3(M+1)-1$.

Using the rational majorant $e^{B^2/4}<1/(1-B^2/4)$, the independently evaluated bounds at $B=11/50$, $M=8$ are

| Quantity | Rigorous upper bound, rounded upward |
|---|---:|
| Position tail | $5.116\times10^{-16}$ |
| First derivative tail | $1.331\times10^{-14}$ |
| Second derivative tail | $3.596\times10^{-13}$ |
| Squared-speed defect | $2.661\times10^{-14}$ |

The JSON retains the exact rational values, so these displayed decimals are only outward-rounded presentations. Here $M=8$ means the Bessel indices $|k|\le8$; the Cartesian series uses frequencies $1+3k$, up to absolute frequency 25. It does not mean a Cartesian Fourier cutoff at frequency 8. The exact curve is isometric; its finite projection has the displayed small defect. Subsequent nonlinear prefix propagation needs a separate tail-error estimate.

## 3. Support gap and whole-surface distance

At $\theta=0,\pi/3$ the normals are the corresponding radial directions, and the series is radial there. Subtracting their support values gives a factor $1-(-1)^k$. For positive odd $k$, combining the negative coefficient $J_{-k}=-J_k$ gives
$$
2J_k\left(\frac1{3k+1}+\frac1{3k-1}\right)
=\frac{12k}{9k^2-1}J_k.
$$
The defining alternating series has decreasing terms for $0<b<1/3$; its first positive term exceeds the next negative term. Thus every $J_k(b)>0$ for $k\ge1$, and
$$
\Delta_b\ge\frac32J_1(b)\ge\frac{3b}{4}-\frac{3b^3}{32}.
$$
At the exact rational $b=11/50$, the last expression is $656007/4000000=.16400175$. No sampled support maximum is used.

For a supporting point of the rotated cylinder at height zero, every point of the initial central cylinder is separated by at least $\Delta_b$ in the selected normal projection. Every remaining point is separated vertically by at least $\ell$, under the stated isolation hypothesis. Hence its distance from the complete initial surface is at least $\min(\Delta_b,\ell)$. A phase-reparametrized core has the same rotated image, so this statement is independent of material parametrization. The actual complete phase family, isolation, and diameter bound remain required.

## 4. Parameter jets

Differentiating $i e^{i\phi}$ at fixed material $\theta$ gives
$$
\partial_{b_j}\gamma'=-e^{i\phi}\sin(m\theta),\qquad m=3j,
$$
and differentiating in $\theta$ gives precisely
$$
-m\cos(m\theta)e^{i\phi}-i\phi'\sin(m\theta)e^{i\phi}.
$$
The parameter derivative of the tangent retains the threefold equivariance, so its full-period integral is zero. Its zero-mean periodic primitive is therefore the parameter derivative of the centered curve. All identities are valid on the exact family; there is no implicit arclength inversion to differentiate.
