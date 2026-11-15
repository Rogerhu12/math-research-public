# Metric auxiliary delta and the conditional held-image amplitude budget

Date: 2026-11-15. This is a paper clarification of existing definitions and published formulas. No candidate geometry or Hausdorff computation was performed.

## 1. The recorded 0.266408 value is not a measured held-image amplitude

The value `0.26640845723039297` in [the first full-grid exchange result](full-grid-exchange-first-actual-result-20261114.md), section 4, is the raw auxiliary variable of the **metric epigraph**. The report tests it against the actual metric error eta, records positive `eta - delta`, and correctly preserves the failed auxiliary inequalities. It is not the quantity $\delta_{\rm hold}$ defined by the topic README as the Hausdorff distance of whole images without rigid alignment. No numerical Hausdorff conclusion follows from that value.

The failure of that historical metric epigraph is unchanged. The current maximum metric error remains far from the required $10^{-6}$. This clarification does not turn any existing state into a completed solution.

## 2. Existing full-image support conditions would suffice for amplitude

[R33, sections 3–4](../results/R33-elliptic-core-reach-and-reflected-phase-budget.md) gives the phase family whose image is $R_\alpha S$, where $S=F_0(M)$ and $0\le\alpha\le\pi/2$. Its held inner disks are pointwise fixed by the material shift and ambient rotation. The exact central ellipse has $A=1$, so $S$ contains $(1,0,z_0)$, for example at $z_0=0$ on the central cylinder.

Suppose the **complete continuous** initial image satisfies

$$
|X|\le R_{\rm ball}=101/100,\qquad |y|\le p=38999/100000.
$$

At $\alpha=\pi/2$, its rotated core contains $(0,1,z_0)$. Every point of $S$ has $y\le p$, and therefore

$$
\delta_{\rm hold}\ge d((0,1,z_0),S)\ge1-p=61001/100000.
$$

The ball gives $D\le2R_{\rm ball}=101/50$. Consequently

$$
\frac{\delta_{\rm hold}}D\ge\frac{61001}{202000}
=\frac3{10}+\frac{401}{202000}>\frac3{10}.
$$

The held disk radius $r_c=11/50$ also gives $\operatorname{diam}(H)/D\ge22/101>1/5$. These are the already published support-witness arguments of R33 and [R40, section 5b](../results/R40-bent-flat-tail-normal-chord-and-ball-budget.md), with the currently chosen strip budget inserted explicitly. The arguments do not depend on the coefficients of u or v once the full support conditions hold.

The actual computations only test finite samples of the ball and strip, using declared floating tolerances. They have not certified these support conditions on the complete continuous surface. The central core and caps do not by themselves prove that an unknown connector satisfies them. Thus the current rigorous status is a conditional amplitude budget, not a measured failure at 0.2664 and not a completed continuous amplitude certificate.

## 3. Endpoint length information does not replace the strip condition

For an exact isometric connector, a material radial line has unit speed. Write $t_f=423/500$, with its initial point on the ellipse and its final point on the six-cap outer circle of radius $R=137/500$. The known horizontal bounds at the two ends yield, for every material angle,

$$
|y(t,\theta)|\le\min\{B+t,\ R+t_f-t\},\qquad B=7/25.
$$

Taking the maximum in $t$ gives the u/v-independent bound

$$
|y|\le\frac{B+R+t_f}{2}=\frac7{10},
$$

because the intersection of the two affine bounds lies inside the interval. It is much weaker than the required strip bound. With an a priori operator metric error $\varepsilon$, replace the radial lengths by $\sqrt{1+\varepsilon}$ times those lengths. This remains an upper support bound; it is not an upper bound excluding the desired Hausdorff amplitude.

A related necessary endpoint condition is also immediate: at material angle zero the held-disk edge is $(r_c,0,h)$, while the core port is $(A,0,w_c)$. Hence exact isometry requires

$$
L^2\ge(A-r_c)^2+(h-w_c)^2,
\qquad L=9/10,\quad w_c=1/50.
$$

For metric error at most $\varepsilon$, its left side becomes $(1+\varepsilon)L^2$. Similar inequalities hold at the open-cap interface using its actual exact port position. They are necessary radial-length conditions, not sufficient isolation or reach conditions. No contradiction with the present design is established here.

No u/v-independent upper bound below $0.3D$ is proved for the current fixed design. Whether its connectors can simultaneously satisfy exact metric, continuous support, and the full reach condition remains unresolved. The new 103-column experiment must be assessed first through its actual fixed-height and fixed-domain diagnostics, without confusing the two delta quantities.
