# R144 supplement: the completed forward integral sharply locates the same compact root and reduces its full residual

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved using complete saved bounds and exact rational inequalities.**
The compact-density root already constructed by TM satisfies

$$
             -8\,10^{-13}<\xi_*<-7\,10^{-13}.
 \tag{SR.1}
$$

It is the same root and the same centre, not a new numerical proposal.
Its continuous mean differs from the original raw mean by at most
$2\,10^{-7}$. The full unnormalized same-$\phi$ state difference is
less than $3.847\,10^{-7}$, and the full pair $A^0$ distance to the
selected reference is less than $3.865\,10^{-7}$. The compact
$\xi\chi'$ ordinary source is less than $3.903\,10^{-12}$ in
$L^2_rL^2_\phi$, while the complete second ordinary source is less
than $7.461\,10^{-8}$.

The proof uses the newly completed signed forward endpoint and the
already completed CP/TM/LC bounds. It does not repeat their numerical
integrations or finite-coefficient scans. All original jumps, the
nonmean fluxes and the metric/phase distinctions remain. In particular
the full Gauss--Codazzi solution has not yet been constructed.

## 1. Why the new signed endpoint belongs to the existing quadratic

Every object in this section is the same raw candidate

`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`

at the fixed exact values

$$
 \alpha=\frac{6890507429876859}{9007199254740992},\quad
 \eta_0=-\frac{7789843107295549}{4611686018427387904},\quad
 \nu_0=-\frac{2572625729470897}{72057594037927936}.
 \tag{SR.2}
$$

Write $m=\langle v\rangle$, $U=\langle u^2\rangle$,
$V=\langle(v-m)^2\rangle$, $n=a^2/m^2$ and

$$
 H(r)=\exp\!\left(\int_0^r2\beta(s)U(s)\,ds\right),\qquad R=25/8.
 \tag{SR.3}
$$

The completed fixed-eta0 calculation integrates the exact
fixed-density forward function $Y_f$ from $Y_f(0)=1$. By the
[reference-subtraction identities](R144-supplement-fixed-density-rotational-reference-subtraction.md),
its output fields `D_at_current_right` and
`forward_multiplier_at_current_right` enclose, respectively,

$$
                        D_R=Y_f(R)-n(R),\qquad H_R=H(R).
 \tag{SR.4}
$$

The normalized constant in
[TM.4](R144-supplement-terminal-mean-small-ball-controls-normalized-forward-constant.md)
is exactly $\overline D=D_R/H_R$. The old TM argument bounded this
same number through the terminal waist solution; the new calculation
encloses it directly, with its sign. There is no change of initial
condition, metric, radial variable, amplitude normalization or raw
mean convention.

For the fixed cutoff $\chi$ on $[1/20,9/50]$, set

$$
 j_\xi=1+(1+\xi\chi)(v-m)/m.
$$

[CD.12--13](R144-supplement-compact-density-quadratic-mean-compensator.md)
gives $Y_\xi(R)-n(R)=D_R+\xi A_R+\xi^2B_R$. The
completed [compact moments](R144-supplement-actual-compact-mean-C0-receivers-and-positive-moments.md)
are precisely

$$
 \overline a=-A_R/H_R,\qquad
 \overline b=-B_R/H_R,\qquad
 0\le\overline b\le\overline a/2.
 \tag{SR.5}
$$

Thus the exact equation is the existing TM equation

$$
       P(\xi)=\overline D-\overline a\xi-\overline b\xi^2=0.
 \tag{SR.6}
$$

The compact-moment enclosure over the original affine intrinsic box
contains its original point $\eta_0$. It is used only in that sense.
Its 7721 common cells and the forward calculation's 7296 common cells
are refinements of the same 6144 raw pieces and retain the same
6143 actual interfaces. They do not define different input functions.
The selected continuous repair and $\delta_*$ do not enter (SR.6).

The four complete numerical records consumed here are:

| Record | Run and SHA256 |
|---|---|
| [FM signed forward endpoint](../notes/fixed_eta0_mean_retraction_ci/run-45778507038-1/fixed-eta0-correlated-mean-retraction.json) | `45778507038/1`, `c45df5750f1e888998d6b3ff47714fa23aa5b4c0163bcdb060bc3ba42cc9b124` |
| [CP moments and all 11 kernels](../notes/compact_mean_c0_receivers_ci/run-45787608966-1/compact-mean-c0-receivers.json) | `45787608966/1`, `0ce421d4a1e14a57915531261c531ce8231a8874aba5dfd704d37f67bb8d7641` |
| [TM original root and mean bounds](../notes/terminal_mean_small_scalar_gate_ci/run-45791979634-1/terminal-mean-small-scalar-gate.json) | `45791979634/1`, `a74d11052da41570a7588d5a79545cfb7295ccf437b3bae971390d59f2b99de6` |
| [LC full state and five sources](../notes/localized_full_state_compact_sources_ci/run-45797426031-1/localized-full-state-and-compact-sources.json) | `45797426031/1`, `60ac20418b405281a3150216e45f7bffd0e73b7625ccc8c383cf4204968b5748` |

FM is complete with its old conjunction `proved=false`; this does
not invalidate its full endpoint balls. Its failed nearby-state and
unchanged-outer-mean gates concern the *fixed-density* retraction,
as proved in the [actual FM report](R144-supplement-actual-fixed-eta0-forward-mean-and-terminal-mismatch.md).
Neither false flag is rewritten here.

## 2. A signed root interval by rational comparisons

The full saved balls, including their radii, imply the following
strict outward rational bounds:

$$
 \begin{gathered}
 -3.301986\,10^{-15}<D_R<-3.301985\,10^{-15},\\
 1.0078<H_R<1.008,\\
 0.00452<\overline a<0.00462,\\
 0.00168<\overline b<0.00172.
 \end{gathered}
 \tag{SR.7}
$$

In particular the negative numerator and positive denominator give

$$
              -3.277\,10^{-15}<\overline D<-3.275\,10^{-15}.
 \tag{SR.8}
$$

Let

$$
                    \rho_s=8\,10^{-13}.
 \tag{SR.9}
$$

Using only (SR.7)--(SR.8),

$$
 \begin{aligned}
 P(-8\,10^{-13})
 &>-3.277\,10^{-15}+0.00452(8\,10^{-13})
                       -0.00172(8\,10^{-13})^2>0,\\
 P(-7\,10^{-13})
 &<-3.275\,10^{-15}+0.00462(7\,10^{-13})<0.
 \end{aligned}
 \tag{SR.10}
$$

Moreover $P'(\xi)=-\overline a-2\overline b\xi<0$ throughout
$|\xi|\le\rho_s$, by (SR.5). This proves (SR.1). The new interval
lies inside the exact old TM radius. The old TM theorem gives
uniqueness in that larger interval, so the root in (SR.1) is
exactly the old root used to define LC's centre. Its value is not
replaced by zero, its midpoint, or either endpoint.

The changed sign information is a statement about the same object.
No scalar root has been fitted to the displayed decimal midpoints.

## 3. A smaller whole mean ball, with every old mean atom

Take the exact rational radius

$$
                         b_s=2\,10^{-7}.
 \tag{SR.11}
$$

The existing [CP proof](R144-supplement-profile-weighted-mean-feedback-polynomial.md)
uses all original raw mean atoms and the ordinary residual through
$E_*=K_0\|R_0\|_\infty+K_J\sum_i|[m]_i|$. Its complete saved bound
is less than $1.894\,10^{-7}$. The full saved 11 kernels are strictly
below the following rationals:

| Kernel | Upper bound | Kernel | Upper bound |
|---|---:|---|---:|
| $C_{01}$ | 0.002539 | $C_{02}$ | 0.000947 |
| $C_{10}$ | 0.01424 | $C_{11}$ | 0.00702 |
| $C_{12}$ | 0.002615 | $C_{20}$ | 0.95313 |
| $C_{21}$ | 0.006477 | $C_{22}$ | 0.002414 |
| $C_{30}$ | 0.23503 | $C_{31}$ | 0.001993 |
| $C_{32}$ | 0.000743 |  |  |

Insert these into the complete CP polynomials

$$
 \begin{aligned}
 A_0&=\rho_s C_{01}+\rho_s^2C_{02},\\
 A_i&=C_{i0}+\rho_s C_{i1}+\rho_s^2C_{i2}\quad (i=1,2,3),\\
 S&=E_*+A_0+A_1b_s+A_2b_s^2+A_3b_s^3,\\
 L&=A_1+2A_2b_s+3A_3b_s^2.
 \end{aligned}
 \tag{SR.12}
$$

Exact rational substitution gives

$$
       S<1.923\,10^{-7}<b_s,
       \qquad L<0.014241<1.
 \tag{SR.13}
$$

The same complete CP record gives $|m|>1.068$,
$V<0.474<0.689^2$, and the original full raw $v$ gap exceeds $0.09$.
Thus $b_s<\inf|m|$ and

$$
            8\rho_s\sqrt V<8\rho_s(0.689)<0.09.
 \tag{SR.14}
$$

CP's exact contraction proof now applies uniformly to every
$|\xi|\le\rho_s$. The resulting terminal mean is negative and
continuous, satisfies $q(R)=0$ and the original jumps
$[q]_i=-[m]_i$, and has $\|q\|_\infty\le b_s$.
Its density is positive by (SR.14). At $\xi_*$, uniqueness of the
same scalar linear equation identifies this terminal solution with
the waist-normalized forward solution. It is therefore the
already constructed compact mean, now with a sharper bound.

In particular the mean has the exact waist value $-a(0)$ and the
original raw outer mean, and all the original mean source and atoms
have been paid. The construction has not made the nonmean joins zero.

## 4. Full state and selected-reference distance

The complete LC record gives

$$
 \sup_r\|v-m\|_{A^0}<0.986,\qquad
 \sup_r\|j_\xi\|_{A^0}<1.923
       \quad (|\xi|\le\rho_{\rm old}).
 \tag{SR.15}
$$

Here the latter bound was obtained from the row formula
$1+(1+\rho_{\rm old}\chi)W_A/M_-$. Decreasing the parameter radius
cannot enlarge it. It covers the full original circle, not sampled
angular values.

For the exact same centre $Q^{\rm cm}=(u,(m+q)j_{\xi_*})$,

$$
 v^{\rm cm}-v=qj_{\xi_*}+\xi_*\chi(v-m),\qquad
 u^{\rm cm}-u=0.
$$

Consequently

$$
 \begin{aligned}
 \|Q^{\rm cm}-Q^{\rm raw}\|_{A^0,\mathrm{pair}}
 &\le b_s(1.923)+\rho_s(0.986)\\
 &<3.847\,10^{-7}.
 \end{aligned}
 \tag{SR.16}
$$

The full same-$\phi$ componentwise $C^0$ norm is bounded by the same
number. The norm is unnormalized by $\alpha$, includes the actual
even mean, and takes both one-sided values at every raw join.

The existing [SB comparison](R144-supplement-complete-same-phi-bridge-to-selected-reference.md)
gives $\|Q_0-Q^{\rm raw}\|_{A^0,\mathrm{pair}}<3.861\,10^{-18}$,
$\|Z\|_{A^0,\mathrm{pair}}<19$, and
$|\delta_*|<9368259853002/10^{23}$. Therefore

$$
 \boxed{
 \|Q^{\rm cm}-Q_{\delta_*}\|_{A^0,\mathrm{pair}}
 <3.847\,10^{-7}+3.861\,10^{-18}
       +19\frac{9368259853002}{10^{23}}
 <3.865\,10^{-7}.
 }
 \tag{SR.17}
$$

This is a state comparison at the same exact physical $\eta_0$.
The compact centre solves its mean equation at $\nu_0$; the selected
reference is associated with $\nu_0+\delta_*$. The explicit changed
mean and ordinary metric sources in SB.15 and SB.18 remain and are
not suppressed by (SR.17). An inverse at one state/metric has not
been transferred to the other.

## 5. All five nonmean source receivers improve without a repeated scan

Let $(b_o,\rho_o)$ be the exact old TM parameters used by LC.
Their complete rational values imply

$$
 b_s<\vartheta b_o,\qquad
 \rho_s<\sigma\rho_o,\qquad
 \vartheta=77/100,\quad \sigma=4\,10^{-8}<\vartheta.
 \tag{SR.18}
$$

The [complete LC source proof](R144-supplement-localized-full-state-C0-and-compact-source-receivers.md),
(LC.9)--(LC.10), is a pointwise positive majorant on every old row.
For clarity set $M=|m|$, $E=\rho\chi$ and

$$
 K_\Delta=|K|b(2M+b),\quad K_b=|K|(M+b)^2,
$$
$$
 A_+=K_\Delta+K_bE,\qquad
 B_+=K_\Delta+K_b(2E+E^2),\qquad
 T=(2A_++B_+\widehat Z_A)Z/4.
 \tag{SR.19}
$$

Under (SR.18),
$K_{\Delta,s}\le\vartheta K_{\Delta,o}$,
$K_{b,s}\le K_{b,o}$,
$E_s\le\vartheta E_o$, and
$E_s^2\le\vartheta E_o^2$. Thus

$$
 A_{+,s}\le\vartheta A_{+,o},\quad
 B_{+,s}\le\vartheta B_{+,o},\quad
 T_s\le\vartheta T_o.
 \tag{SR.20}
$$

Every remaining multiplier in the five LC formulas is nonnegative
and nondecreasing in $b,\rho$. It follows pointwise, and hence in
the same complete radial norms, that

$$
 \begin{aligned}
 F_{u,+,s}&\le\vartheta F_{u,+,o},&
 Q_{u,+,s}&\le\vartheta Q_{u,+,o},\\
 C_{v,+,s}&\le C_{v,+,o},&
 F_{v,\chi,+,s}&\le\sigma F_{v,\chi,+,o},\\
 Q_{v,+,s}&\le\vartheta Q_{v,+,o}.&&
 \end{aligned}
 \tag{SR.21}
$$

For the fourth bound, the whole pointwise expression is
$(M+b)\rho|\chi'|Z$, so the sharper factor $\sigma$ applies.
This retains $\chi'$; it does not discard a radial derivative or
replace an ordinary source by a divergence without its primitive.
The bound also holds under LC's exact integration of $(\chi')^2$.

The saved LC bounds give the following complete consequences:

| Quantity, with the conventions of LC.11 | New strict upper bound |
|---|---:|
| $\|f_u\|_{L^2_r}$ | $6.24085\,10^{-8}$ |
| $\|q_u\|_{L^2_r}$ | $1.39755\,10^{-6}$ |
| $\|c_v\|_{L^\infty_r}$ | $1.190$ |
| $\|f_{v,\chi}\|_{L^2_r}$ | $3.903\,10^{-12}$ |
| $\|q_v\|_{L^2_r}$ | $1.30515\,10^{-6}$ |

These follow by applying (SR.21) to the full old bounds, conservatively
rounded outward to $8.105\,10^{-8}$, $1.815\,10^{-6}$, $1.190$,
$9.757\,10^{-5}$ and $1.695\,10^{-6}$, respectively.
No private fine trace or new coefficient integral is needed.

Inserting the unchanged complete raw ordinary sources into
(LC.13), with the actual $\alpha$ already included once, gives

$$
 \begin{gathered}
 \|F_u\|_{L^2_rL^2_\phi}<9.455\,10^{-8},\\
 \|F_v\|_{L^2_rL^2_\phi}<7.461\,10^{-8},\\
 \|Q_u\|_{L^2_rL^2_\phi}<1.39755\,10^{-6},\\
 \|Q_v\|_{L^2_rL^2_\phi}<1.30515\,10^{-6}.
 \end{gathered}
 \tag{SR.22}
$$

In particular $R_v-jR_0$ is retained through the full coefficient
$C_{v,+}$; mean-exactness has not erased that old ordinary source.

## 6. Complete weak sources, transmissions and the limit of the conclusion

The source identity remains

$$
 R_{u,*}=F_u+\partial_\phi Q_u,\qquad
 R_{v,*}=F_v+\partial_\phi Q_v.
 \tag{SR.23}
$$

All ordinary sources have zero angular mean by the original parity
and exact mean subtraction. The finite-centre fluxes have full
physical frequency at most 384. The proven CS receiver therefore
gives, for $0\le s\le1$,

$$
 \|F+\partial_\phi Q\|_{L^2_r\dot H^{-s}_\phi}
 \le4^{-s}\|F\|_{L^2_rL^2_\phi}
        +384^{1-s}\|Q\|_{L^2_rL^2_\phi}.
 \tag{SR.24}
$$

Using $4^{-2/3}<0.397$ and $384^{1/3}<7.27$ yields

| Complete residual norm | New strict upper bound |
|---|---:|
| First row, $L^2_r\dot H^{-2/3}_\phi$ | $1.020\,10^{-5}$ |
| Second row, $L^2_r\dot H^{-2/3}_\phi$ | $9.519\,10^{-6}$ |
| Second row, $L^2_r\dot H^{-1}_\phi$ | $1.324\,10^{-6}$ |
| Pair with both rows in $L^2_r\dot H^{-2/3}_\phi$ | $1.395\,10^{-5}$ |
| Pair with first row in $L^2_r\dot H^{-2/3}_\phi$ and second in $L^2_r\dot H^{-1}_\phi$ | $1.030\,10^{-5}$ |

The pair bounds follow by squaring and adding the unrounded rational
upper expressions from (SR.22)--(SR.24). They are not sums of bounds
expressed in different angular coordinates. The first flux's
$384^{1/3}$ factor has been paid.

The exact original transmission formulas remain
$[u_*]=[u]$ and $[v_*]=m_* (1+\xi_*\chi)[(v-m)/m]$.
The full LC jump majorants are nondecreasing in $b,\rho$, so all
6143 interfaces satisfy the same already saved aggregate bounds,
in particular

$$
 \sum_i\|[v_*]_i\|_{A^0}<2.691\,10^{-12},\qquad
 \sum_i\|[u_*]_i\|_{A^0}<3.370\,10^{-13}.
 \tag{SR.25}
$$

Those are independent transmission sources; none is folded into the
ordinary radial norms in (SR.22). The centre is still piecewise and
its full nonmean residual is still nonzero.

The exact rational calculations and input-endpoint comparisons in
this proof can be checked by
[`fourfold_codazzi_sharp_compact_root_saved_bounds.py`](../scripts/fourfold_codazzi_sharp_compact_root_saved_bounds.py).
It reads only the four complete small records above, performs integer
and rational arithmetic, and calls no native producer, ODE, Fourier
solver, numerical integration or previous scientific target.

This result pays the sharply reduced scalar parameter, the same
centre's complete distance and all five complete changed source
receivers. The remaining full inverse, nonlinear convergence,
negative incoming, complete phase/metric compatibility, actual cap,
height, nonmean transmission and global geometric requirements
remain. The radius improvements alone are not the required exact
closed isometric family.
