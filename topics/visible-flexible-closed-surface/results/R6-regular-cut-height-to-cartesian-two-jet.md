# R6: A regular cut and its Cartesian two-jet

2026-11-09. Astra-visible-flex-4ffd372b numerical subagent. Status: independently reviewed PASS (notes/2026-11-09-audit-cut-two-jet.md); conditional exact local lemma; not an existence, embedding, reach, or infinite-tail theorem.

## Claim and hypotheses

Use meridian arclength `s` on a neighbourhood of one connected chosen cut, and write the fixed metric as

\[
g=ds^2+a(s)^2d\theta^2.
\]

Let two `C²` isometric immersions be written `X=(x,z)` with planar component `x∈R²` and height `z`. Suppose their complete height two-jets agree on the cut, including the mean components of `z_s` and `z_{ss}`. Suppose the horizontal angular speed `T` and the horizontal normal component `b` of `X_s` defined below are nonzero throughout the cut. Finally choose the same sign branch for `b`. Then, after a single planar rigid motion and a constant height translation, their complete Cartesian two-jets agree along the cut.

This claim is relevant to the inward ellipse-prefix/tail seam, whose background `a_s=-1/sqrt(E)` is nonzero. It does not apply without modification at the cylindrical core where `a_s=0`.

## Derivation

Put `p=z_θ`, `q=z_s`, `u=z_θθ`, `v=z_sθ`, `h=z_ss`, and

\[
T=\sqrt{a^2-p^2},\qquad x_\theta=Tt,\qquad
 t=(\cos\alpha,\sin\alpha),\quad n=(-\sin\alpha,\cos\alpha).
\]

Orthogonality and the unit meridian metric give

\[
x_s=ct+bn,\qquad c=-\frac{qp}{T},\qquad
b^2=1-\frac{a^2q^2}{T^2}.
\]

The sign of `b` is part of the orientation/branch convention. At an axisymmetric background, with `t=e_θ` and `n=-e_r`, it is `b=-a_s`; it must not be silently replaced by the positive root in every chart.

The known scalar derivatives are

\[
T_\theta=-\frac{pu}{T},\quad
T_s=\frac{aa_s-pv}{T},\quad
c_\theta=-\frac{vp+qu}{T}+\frac{qpT_\theta}{T^2}.
\]

Comparing the tangential components of `∂_s x_θ=∂_θ x_s` therefore gives

\[
\alpha_\theta=\frac{c_\theta-T_s}{b}
=-\frac{aa_sT^2+a^2qu}{T^3b}.
\]

Thus the height Cauchy data and fixed metric determine the planar tangent angle along the entire cut up to one constant. Integrating `x_θ=Tt` then determines `x` up to one planar translation. These are exactly the freedoms removed by the planar rigid alignment. Once that alignment is chosen, `x_s=ct+bn` agrees as well.

For the remaining second derivatives, write

\[
b_\theta=-\frac{a^2qv}{bT^2}+\frac{a^2q^2T_\theta}{bT^3},
\qquad
\alpha_s=\frac{b_\theta+c\alpha_\theta}{T},
\]

\[
c_s=-\frac{hp+qv}{T}+\frac{qpT_s}{T^2},
\qquad
b_s=-\frac{aa_sq^2+a^2qh}{bT^2}+\frac{a^2q^2T_s}{bT^3}.
\]

Consequently

\[
x_{\theta\theta}=T_\theta t+T\alpha_\theta n,
\]

\[
x_{s\theta}=(c_\theta-b\alpha_\theta)t+(b_\theta+c\alpha_\theta)n,
\]

\[
x_{ss}=(c_s-b\alpha_s)t+(b_s+c\alpha_s)n.
\]

Every quantity is determined by the same complete height two-jet, `a,a_s`, and the selected branch. This proves the claim. No assertion that arbitrary height data integrate to an isometric surface is used: the two isometric immersions are hypotheses.

## Applying the inward tail convention

The nonlinear tail is parameterized by radius and must be evaluated on `sigma*H`, where `sigma=sign(a_s)`. With tail metric `E dr²+r²dθ²`, `a_s=sigma/sqrt(E)` and `a_ss=-E_r/(2E²)`, the height derivatives expected in the prefix chart are

\[
(z_s)_{\rm mean}=\frac{({\rm DN})_{\rm mean}}{\sqrt E},\qquad
(z_{ss})_{\rm mean}=\sigma\left(\frac{z_{rr,{\rm mean}}}{E}
+z_{r,{\rm mean}}a_{ss}\right),
\]

with the same formula for the nonmean second derivative. These are the conventions in the reviewed inward bridge and in `fixed_metric_actual_tail_bvp.py`. Equality of nonmean slopes alone does not meet this lemma; the mean jets must be included.

## Numerical use and limitations

On a compact set with `T≥T_min>0`, `|b|≥b_min>0`, and bounded height two-jets, the displayed algebra is locally Lipschitz. Thus height two-jet errors can be converted to Cartesian seam errors after alignment; integration of `α_θ` and `x_θ` over one `2π` period gives finite constants. This observation is not an interval error bound for any current checkpoint. Actual finite prefix and tail reconstructions still have approximation defects, so their Cartesian seam can either be checked directly or bounded with these formulas plus C1 control of the metric defects. Pointwise C0 metric error alone cannot control a second-derivative seam; differentiating the metric identities also differentiates their defects.

Angular holonomy, planar closure, embeddedness, global reach, and extension of a finite-depth Robin tail to a genuine round collar remain independent requirements. The finite-tail computations in the companion note do not establish them.
