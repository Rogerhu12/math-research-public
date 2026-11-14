# Explicit ideal-length pullback for the nonzero-frontload first piece

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

This exact rational consumer joins two already completed results for the **same unsolved warm**, screen SHA `c782a9bda980b0a31443be14d24444b695b246f58390d8f3bf4932e26807d8fa`: the stored-polynomial/complex-ellipse/Gauss64 certificate and the independently certified ideal degree-22 first piece from `strong_newg_initial_law_analytic_profile_bounds_v2.py`. Its source SHA is `2a51ad3d69e9e86c8b5463264c90b4cf66593f0b60adf7897cb318bb9f96b287`; the ideal certificate SHA is `69b248ccdf9b9656f7bf8f1f94aebbf85889912e4d0a9cace81ad6a88a9fd4f1`. Every profile field and both owned exit-zero records are checked. Neither input is relabeled as a newly accepted solution.

Let S_b denote the actual binary first-piece length and S_* the exact positive root of the ideal length equation. The new comparison is on one specified interval, 0≤s≤S_b, using

\[
 u=s/S_b,\qquad s_*=S_*u.
\]

Thus all final first and second derivatives differentiate with respect to **the same actual s**. The ideal meridian is explicitly pulled back by this affine map; its ideal physical derivative is not silently substituted for the derivative of the pullback.

The independent ideal certificate supplies a positive rational interval containing S_* and exact affine velocity controls C_j^*(S_*)=a_j+b_jS_*. The consumer rechecks the root signs and the positive derivative of the defining quadratic. Its radius controls are the exact quadratic polynomials

\[
 R_j^*(S_*)=1+\frac{S_*}{23}\sum_{i<j}(a_i+b_iS_*).
\]

The right endpoint polynomial is checked to equal 1+AVS_*+Bk0S_*², hence equals 1+δ at the certified root. Differences from the actual stored radius controls are exact quadratic polynomials in S_*; successive Bernstein differences, divided by S_b or S_b², enclose the whole interval. Likewise exact affine control differences give complete normalized-u bounds ε0, ε1, ε2 for the stored and ideal velocities. No spatial samples are used.

Both velocities lie in [0,V], with V<1. If ell>0 is the certified rational lower bound for sqrt(1-V²), then for f(v)=sqrt(1-v²), |f_v|≤V/ell and |f_vv|≤ell^-3. With D1 a common bound on both normalized velocity derivatives,

\[
 \|f_b-f_*\|\le(V/\ell)\epsilon_0=:E_0,
\]
\[
 \|f_b'-f_*'\|\le D_1\ell^{-3}\epsilon_0+(V/\ell)\epsilon_1=:E_1.
\]

Let εS bound |S_b-S_*| and M1 bound |f_*'| in normalized u. The mathematical height primitives, with their common zero left anchor, differ on the actual s interval by at most

\[
 (\epsilon_S+S_bE_0,\quad \epsilon_S/S_b+E_0,\quad
 \epsilon_SM_1/S_b^2+E_1/S_b).
\]

The actual binary Gauss-table partial-primitive costs from the preceding certificate are then added component by component. The resulting complete first-piece bounds are:

| Component | C0 | C1 in actual s | C2 in actual s |
|---|---:|---:|---:|
| Stored radius minus pulled-back ideal radius | <1.212e-16 | <4.608e-15 | <2.172e-13 |
| Mathematical binary-Gauss height minus pulled-back ideal height | <7.620e-15 | <1.183e-14 | <2.147e-13 |
| Meridian vector, using the sum of coordinate bounds | <7.730e-15 | <1.643e-14 | <4.319e-13 |

The exact rational outputs are authoritative. The last row bounds Euclidean norms conservatively by the coordinate sum. Since the ideal unpulled meridian has unit speed, its pullback metric is exactly (S_*/S_b)²; its deviation from 1 is less than 1.636e-16 and the exact ratio is separately retained. This identity concerns the ideal pullback, not the independently rounded stored jet list.

This pays the **first-piece affine length alignment**. Internal floating evaluation, the affine arithmetic used at runtime, joins and coordinate offsets in later pieces, complete surface mean and PDE/metric/curvature/reach assertions still need their own bounds. The actual stored first-piece radius and mathematical Gauss height have not been substituted into the active BVP or declared to be a new target metric.

The owned producer completed all 11 identity/domain/comparison groups with exit 0 in 0.511 seconds and 12,396 KiB peak RSS. Its saved command, exact inputs and hashes reproduce the result with fresh output paths. No ODE, Node, Newton or new geometry samples were evaluated.
