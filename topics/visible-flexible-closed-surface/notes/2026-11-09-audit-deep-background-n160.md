# Independent audit: default N160 deep rotational background

2026-11-09. Reviewer: independent_audit, not involved in construction.
Status: **PASS for the unchanged rotational cells n≥160.** This does not certify the finite physical warp, its joins, or any nonrotational Darboux perturbation.

## Sources and independence

The exact R28 result was read from current GitHub, blob `cf9881e3ae2c2797a61213ab099dbec239be5f0d`, before the N160 candidate was supplied. The reviewed candidate is `notes/2026-11-09-closing-deep-background-n160.md`, Git blob `741d96844cdbcdbc140aadc39891933025bb0f77`; its rational audit script has Git blob `ff87bc934d8e09352dc825388c2bae11a6790477`. Full SHA256 values and a separate normalization check are in `2026-11-09-audit-deep-background-n160-inputs.json`.

I checked the bounds algebraically and ran the supplied Fraction script independently without editing it. Its assertions all pass. This review uses the canonical R28 root existence result; it does not turn a numerically calibrated root into an exact one.

## Calibration and normalization

For $\delta_n=.006\,2^{-n}$, $c_n=.05\,2^{-n/2}$, R28 gives an exact mode-two calibration root in $[1/2,2]$ at every $n\ge80$, because
$$
792 e^{384c_n}(384c_n+36\delta_n^2)<33.
$$
The rational majorant at $n=80$ is below $1.384\times10^{-8}$. The selection must be fixed inside that bracket; uniqueness is unnecessary for the background estimate. All five profile levels lie below 64, and every logarithmic transition jump is bounded by $H_n=\log(128/\delta_n^2)$.

For the present $r_c=1/4,w_{cut}=1/2$, the exact raw length and normalization are
$$
Y=6\delta_0+\frac{6(.05\delta_0)}{1-2^{-3/2}},\qquad
\epsilon=\frac{w_{cut}r_c^7 e^{7Y/\sqrt{12}}}{(2\delta_0)^{11/4}}.
$$
The source's $Y<.03888$ and $e^{7Y/\sqrt{12}}<10/9$ are rigorous. As an additional independent normalization bound, $(1/50)^4<\delta_0^3$ gives $\delta_0^{3/4}>1/50$, while $2^{11/4}>6$. Hence
$$
\epsilon<\frac{1953125}{248832}<7.85.
$$
Its floating diagnostic value is about 6.32176708786. More sharply for the derivative estimate, the normalization cancels the fractional power of $\delta_0$ and directly gives
$$
W_n=\epsilon64\delta_n^{7/4}/r_c^7
<\frac{80000}{81}2^{-7n/4}.
$$
Thus the old R28 numerical constants from $r_c=.966$ have not been imported.

## Derivative, curvature, and C² closure

For a log-quintic transition, $|p_x|\le64(15/8)H_n$ and $|r_x|=r\eta_n/\sqrt{12}$. Differentiating $w=\epsilon\delta_n^{7/4}p/r^7$ therefore gives
$$
|w_r|\le B_n:=\frac{\sqrt{12}W_n(15/8)H_n}{r_c\eta_n}+\frac{7W_n}{r_c},
\quad \eta_n=.0003\,2^{-3n/2}.
$$
This also dominates the plateau derivatives. At $n=160$, $H_n<241$; exact rational substitution yields
$$
W_{160}<5.085\times10^{-82},\quad
B_{160}<.018942193<.02,
\quad W_{160}/r_c<2.034\times10^{-81}.
$$
The first term is bounded by a constant times $2^{-n/4}(1.4n+16.9)$, with step ratio at most $4846/5621<1$ for all $n\ge160$. The second term decreases geometrically. Consequently these bounds hold throughout every retained deep cell, not merely at sampled points.

For the rotational radial graph, $|\kappa_r|=|w_r|/(1+w^2)^{3/2}\le B_n$ and $|\kappa_\theta|=|w|/(r\sqrt{1+w^2})\le W_n/r_c$. Both vanish uniformly toward the cuff. Constant extension of the graph height across $r_c$ has matching zero first and second derivatives, so it is C². The exact-rational remaining-height majorant is approximately $2.25415\times10^{-132}<10^{-131}$, using the geometric tail of the actual radial length.

The statement is stable under arbitrary changes confined to finitely many shallower cells only in this limited sense: the unchanged deep rotational background retains this bound. It does not transfer a nonlinear stable manifold, or a bound for the height perturbation, across those modifications.
