# A closed unit-speed threefold core with rapid Fourier convergence

2026-11-09, Astra-visible-flex-4ffd372b. Complete local construction and bounds; pending independent review. This is a planar cylinder inlet, not a closed flexible surface.

## 1. Exact curve and generalized cylinder

Let \(0<b<1/3\), set \(\phi(\theta)=\theta+b\sin3\theta\), and choose the zero-mean primitive
\[
\gamma_b'(\theta)=i\exp(i\phi(\theta)),\qquad \int_0^{2\pi}\gamma_b(\theta)\,d\theta=0.
\]
The tangent field satisfies \(\gamma_b'(\theta+2\pi/3)=e^{2\pi i/3}\gamma_b'(\theta)\). Its integral over a full period is zero, because the three successive third-period integrals sum with multipliers \(1,e^{2\pi i/3},e^{4\pi i/3}\). Thus the primitive is periodic, has the same threefold symmetry after its mean is fixed, and has exact speed one. Its signed curvature is
\[
\kappa(\theta)=\phi'(\theta)=1+3b\cos3\theta>0.
\]
The tangent makes exactly one positive turn. More explicitly, for any fixed normal direction the projection of the curve decreases until the opposite normal and then increases back to its starting value, since its derivative is the scalar product of the unit tangent with that normal. The point with that normal is consequently the unique supporting point. This proves strict convexity and embeddedness. The cylinder \(F(s,\theta)=(\gamma_b(\theta),s)\) has exact metric \(ds^2+d\theta^2\), independent of b. Curvature lies in \([1-3b,1+3b]\).

The same closure and unit-speed identities hold for \(\phi=\theta+\sum_{j=1}^J b_j\sin(3j\theta)\). Strict convexity follows, for example, from \(\sum_j3j|b_j|<1\). Higher b_j are extrinsic core parameters and do not change its intrinsic circle metric. They need not preserve constant width.

## 2. Explicit coefficients and elementary tail bounds

For k≥0 define
\[
J_k(b)=\sum_{j=0}^\infty\frac{(-1)^j(b/2)^{2j+k}}{j!(j+k)!},\qquad J_{-k}(b)=(-1)^kJ_k(b).
\]
Multiplying the absolutely convergent power series of \(\exp[(b/2)z]\) and \(\exp[-(b/2)z^{-1}]\) on |z|=1 gives
\[
 e^{ib\sin\psi}=\sum_{k\in\mathbb Z}J_k(b)e^{ik\psi},\qquad
 \gamma_b(\theta)=\sum_{k\in\mathbb Z}\frac{J_k(b)}{1+3k}e^{i(1+3k)\theta}.
\]
No denominator vanishes. Absolute convergence of all differentiated series follows from the factorial coefficient bound
\[
 |J_k(b)|\le e^{B^2/4}\frac{(B/2)^k}{k!},\qquad 0\le b\le B<1/3,\quad k\ge0.
\]
It follows directly by discarding signs and using (j+k)!≥k!. Let x=B/2 and let γ_M retain |k|≤M. With \(E=e^{B^2/4}\), geometric comparison of successive factorial terms yields
\[
 \|\gamma_M'-\gamma'\|_\infty\le \epsilon_1
 :=\frac{2E x^{M+1}}{(M+1)![1-x/(M+2)]},
\]
\[
 \|\gamma_M''-\gamma''\|_\infty\le \epsilon_2
 :=\frac{6E x^{M+1}}{M![1-x/(M+1)]}.
\]
For the second bound the positive and negative k contributions have total multiplier (1+3k)+(3k−1)=6k. The position tail is at most ε1/[3(M+1)−1]. In particular,
\[
 \big\|\,|\gamma_M'|^2-1\,\big\|_\infty\le2\epsilon_1+\epsilon_1^2.
\]
These are exact-arithmetic analytic bounds, separate from floating evaluation. For rational B=.22 they can be evaluated entirely with rational arithmetic after replacing E by the larger 1/(1−B²/4). They explain why this inlet need not inherit the long Fourier tail of the earlier sinusoidal support function at fixed arclength.

## 3. A rigorous support gap for a phase rotation

The outward normal is e^{iφ}. At θ=0 and θ=π/3 these are exactly the corresponding radial directions, and the curve points there are radial by the real coefficient formula. Write h for the true support function of this convex curve. Rotation by π/3 gives the support difference in direction π/3:
\[
 h_{R_{\pi/3}\gamma}(\pi/3)-h_\gamma(\pi/3)
 =h_\gamma(0)-h_\gamma(\pi/3)
 =\sum_{\substack{k\ge1\\k\text{ odd}}}\frac{12k}{9k^2-1}J_k(b)=:\Delta_b.
\]
For 0<b<1/3 the alternating defining series has decreasing term magnitudes. Therefore every J_k(b)>0 for k≥1 and
\[
 \Delta_b\ge\frac32J_1(b)\ge\frac{3b}{4}-\frac{3b^3}{32}.
\]
At the exact rational b=11/50 this lower bound equals **.16400175**. The numerically summed gap is about .1641033204; the exact lower bound is the one usable without a numerical error enclosure.

If this core is extruded through |z|≤ell in a complete initial surface and the remaining surface lies in |z|≥ell, then the rotated supporting point at z=0 has distance at least min(Δ_b,ell) from the entire initial surface: projection on the chosen normal controls distance to the central cylinder, and vertical separation controls the rest. Taking ell=.164 gives the conditional held-distance bound .164. This is the same isolation argument as R3, with support directions rather than an ellipse axis. It still requires an actual complete family and a diameter upper bound.

## 4. Parameter derivatives without an implicit arc inversion

For a coefficient b_j in the multi-sine angle, set m=3j. At fixed material θ,
\[
 \partial_{b_j}\gamma'=-e^{i\phi}\sin(m\theta),
\]
\[
 \partial_{b_j}\gamma''=-m\cos(m\theta)e^{i\phi}
 -i\phi'\sin(m\theta)e^{i\phi}.
\]
The parameter derivative of γ is the zero-mean periodic primitive of the first formula. Its mean derivative vanishes by the same threefold argument. Thus a Fourier primitive gives the full inlet Jacobian without differentiating an inverted arclength map. These formulas concern the exact curve; any finite projection and the nonlinear Frenet prefix retain their own errors.
