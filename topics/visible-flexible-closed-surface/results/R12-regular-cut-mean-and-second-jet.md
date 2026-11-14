# A regular-cut holonomy determines the mean slope

2026-11-09, macro_prefix / Astra-visible-flex-950f9f73. Complete conditional proof, independently reviewed PASS and read in full by root before adoption. Review: `../notes/2026-11-09-950f-audit-cut-mean.md`; frozen draft hashes are in the matching review JSON. This is a conditional interface lemma; it does not construct a closed surface or certify the numerical prefix as an exact isometry.

## Statement and conventions

Let F be a C2 isometric immersion near a periodic cut s=s0, with metric

$$g=ds^2+a(s)^2d\theta^2,\quad a=a(s_0)>0,\quad \alpha=a'(s_0)<0.$$

Write z for its third Cartesian coordinate and, on the cut,

$$u=z_s,\quad v=z_\theta,\quad w=z_{\theta\theta},\quad
Q=1-u^2-v^2/a^2>0,\quad L=\sqrt{a^2-v^2}.$$

The horizontal projection of Fθ has length L. Let t be its unit tangent and n=Jt, where J is the positive planar quarter-turn. Use the inward branch

$$F_\theta^{xy}=Lt,\qquad F_s^{xy}=-\frac{uv}{L}t+
\frac{a\sqrt Q}{L}n.$$

Assume the projected tangent has turning number1. This is the branch of the round inward cut used by the current prefix and tail.

Fix the height trace z(θ) and the nonconstant slope u0(θ), with meanθu0=0. Let u=c+u0. On an interval I of means c, suppose Q>0 and

$$u\ge u_{\min}>0,\qquad \frac{\|w\|_\infty}{a}<(-\alpha)u_{\min}.$$

Then at most one c∈I can occur for an exact immersed cut on this branch with turning number1. Consequently, matching the nonconstant slope between two such exact isometries, with the same height trace and metric, also matches their mean slope.

## Proof of the holonomy formula

Let φ be the angle of t, so tθ=φθn. Differentiating the horizontal tangent and meridian and comparing the t components of Fθs=Fsθ gives

$$L_s=\left(-\frac{uv}{L}\right)_\theta-
\frac{a\sqrt Q}{L}\phi_\theta.$$

Use v_s=uθ,

$$L_s=\frac{a\alpha-vu_\theta}{L},\qquad
L_\theta=-\frac{vw}{L}.$$

The terms involving uθ cancel. Since L²+v²=a²,

$$\phi_\theta=-\frac{\alpha+a u w/L^2}{\sqrt Q}.$$

Turning number1 therefore implies

$$\mathcal H(c):=-\frac1{2\pi}\int_0^{2\pi}
\frac{\alpha+a(c+u_0)w/(a^2-v^2)}
{\sqrt{1-(c+u_0)^2-v^2/a^2}}\,d\theta=1.$$

The interval assumptions allow differentiation under the integral. The numerator simplifies exactly:

$$\mathcal H'(c)=-\frac1{2\pi}\int_0^{2\pi}
\frac{w/a+\alpha(c+u_0)}{[1-(c+u_0)^2-v^2/a^2]^{3/2}}\,d\theta.$$

The negative of each numerator is strictly positive by the stated inequality, so H is strictly increasing. Because Q≤1, the explicit lower bound

$$\mathcal H'(c)\ge(-\alpha)u_{\min}-\|w\|_\infty/a=:\eta>0$$

also holds. This proves uniqueness. More generally, two trial means c1,c2 in I satisfy

$$|c_1-c_2|\le |\mathcal H(c_1)-\mathcal H(c_2)|/\eta.$$

Thus a separately validated holonomy residual would quantitatively bound mean mismatch. A sampled metric residual alone is not such a certificate.

## The second height jet then follows algebraically

Let a''=a''(s0). The Darboux equation for the height of an exact isometry is

$$z_{ss}(w+a\alpha u)-(u_\theta-\alpha v/a)^2=-a a''Q.$$

The same strict inequality makes w+aαu negative, uniformly away from zero. Therefore

$$z_{ss}=
\frac{(u_\theta-\alpha v/a)^2-a a''Q}{w+a\alpha u}.$$

Once z and the full first slope u are matched, the complete second height jet is determined: zθθ=w, zsθ=uθ and zss is the displayed quotient. Applying the already-reviewed height-to-Cartesian regular-cut result R6 then gives the Cartesian two-jet up to the required horizontal rigid alignment. This statement requires exact metric data and the indicated branch; numerical coupling still explicitly audits both mean jets and C1 metric error rather than assuming exact identities.

## A coarse quantitative domain covering the present trace

At the current cut a=3/5 and α=−2/√5. The following simple bounds suffice:

$$c\in[.4,.5],\qquad \|u_0\|_\infty\le .02,
\quad \|v\|_\infty\le .005,\quad \|w\|_\infty\le .02.$$

They give u_min≥.38, |u|≤.52 and

$$Q\ge1-.52^2-(.005/.6)^2>.7295.$$

Since 2/√5>.894,

$$\eta\ge .894\cdot.38-.02/.6>.306,$$

and

$$w+a\alpha u\le .02-.6\cdot.894\cdot.38<-.1838.$$

These are rational inequalities apart from the explicitly bounded square root.

For the current computed M12 trace, finite Fourier coefficient absolute sums give

- ||v||∞≤.003925296165132;
- ||w||∞≤.012132742008387;
- ||u0||∞≤.012456261350808;
- mean u≈.447336314418837.

They lie well inside the stated domain. The sums were evaluated using exact rational representations of the stored binary floating coefficients and then rounded outward. These facts certify only the finite polynomial trace's size; they do not turn the approximate prefix into an exact isometry, and the actual nonlinear coupled trace must be checked again.
