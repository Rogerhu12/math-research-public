# Exact flat-acceleration physical meridian law

This specifies the metric used by the new design trials, independently of the
numerical collocation mesh. The fixed scalar inputs are `vu`, `vd`, `delta`,
`ramp=epsilon`, `ramp_eta=eta`, `cycles` and the unchanged bridge/tail cut. No
physical parameter is allowed to drift during a subsequent fixed-metric
convergence test.

For $0<\eta<1/2$, define $F$ and its primitive $P$ first on $0\le t\le1/2$:

$$F(t)=\begin{cases}
\dfrac{\eta}{1-\eta}\bigl[(t/\eta)^3-\tfrac12(t/\eta)^4\bigr],&t<\eta,\\
\dfrac{t-\eta/2}{1-\eta},&t\ge\eta,
\end{cases}$$

$$P(t)=\begin{cases}
\dfrac{\eta^2}{1-\eta}\bigl[\tfrac14(t/\eta)^4-\tfrac1{10}(t/\eta)^5\bigr],&t<\eta,\\
\dfrac{t^2/2-\eta t/2+3\eta^2/20}{1-\eta},&t\ge\eta.
\end{cases}$$

For $t\ge1/2$, set $F(t)=1-F(1-t)$ and
$P(t)=t-1/2+P(1-t)$. Then $P'=F$, $F(0)=0$, $F(1)=1$,
$F'(0)=F'(1)=0$, $P(1)=1/2$, and $F$ is $C^2$ across its two actual
internal formula boundaries $\eta,1-\eta$. The formulas on either side of
$t=1/2$ coincide polynomially; it is not an additional knot.

For $u\in[0,1]$, the unit pulse and its integral are

$$w(u)=\begin{cases}F(u/\epsilon),&u<\epsilon,\\1,&\epsilon\le u\le1-\epsilon,\\F((1-u)/\epsilon),&u>1-\epsilon,\end{cases}$$

$$I(u)=\begin{cases}\epsilon P(u/\epsilon),&u<\epsilon,\\u-\epsilon/2,&\epsilon\le u\le1-\epsilon,\\1-\epsilon-\epsilon P((1-u)/\epsilon),&u>1-\epsilon.\end{cases}$$

Thus $I'=w$, $I(1)=1-\epsilon$, and the outward first half-cycle of length
$T_u=\delta/[v_u(1-\epsilon)]$ is

$$a(s)=1+\frac{\delta I(s/T_u)}{1-\epsilon},\quad
 a'(s)=v_u w(s/T_u),\quad a''(s)=v_u w'(s/T_u)/T_u.$$

On the return half, of length $T_d=\delta/[v_d(1-\epsilon)]$, replace this by
$1+\delta-\delta I(u)/(1-\epsilon)$, $-v_dw(u)$,
$-v_dw'(u)/T_d$. The endpoints have $a=1$ and $a'=a''=0$, so cycles and the
previously specified turning bridge join at least $C^2$.

Every half-cycle has the normalized formula-boundary knots

$$0,\ \epsilon\eta,\ \epsilon(1-\eta),\ \epsilon,
\ 1-\epsilon,\ 1-\epsilon(1-\eta),\ 1-\epsilon\eta,\ 1.$$

`db6f-prefix-flat-profile.py` version2 inserts all of them in the BVP reference
chart. The earlier version used the identical physical formula but did not
explicitly include the four extra internal flat-ramp boundaries in each
half-cycle. `db6f-prefix-flat-geometry-source.py` inserts all physical and
angular-chart knots when reconstructing either version's checkpoint; it
therefore lets exact-piece interval methods subdivide at the correct locations.

The current main design has $v_u=.17$, $v_d=.18$, $\epsilon=.4$, $\eta=.05$,
one outward cycle, and the tail cut $(r,w)=(.6,.5)$. The completed genuine M8
nonlinear coupling selected $\delta=.07254443456654512$. This delta, the
chart, and all physical tail parameters are now frozen in the convergence
checks. The actual support amplitude, initially .1, is an output in those
fixed-metric solves.
