# R144 supplement: complete same-phi bridge from the compact mean centre to the selected reference

2026-11-26, visible-exact-astra-198c63d-20261126 / global_geometry.

**Proved from existing complete certificates.** At the same exact physical
parameter $\eta_0$, the TM/LC compact mean centre and the actual selected
reference $Q_{\delta_*}$ differ by less than $1.98\,10^{-5}$ in the complete,
unnormalized moving-state norm at the same $\phi$. The same bound holds in
the complete pair $A^0$ norm. This uses the entire saved LC ball, the
entire centre repair, and the already certified full-body response; no
new numerical target or repeated native evaluation is required.

The new centre is mean-exact at $\nu_0$. Evaluating it at
$\nu_*=\nu_0+\delta_*$ introduces a specific mean and ordinary source,
given below. A true solution derivative $q_\nu$ is not identified with
the explicit reference direction $Z$.

## SB1. Exact objects, common parameter and comparison norm

Fix $R=25/8$ and the original exact parameters

$$
 \alpha=\frac{6890507429876859}{9007199254740992},\qquad
 \nu_0=-\frac{2572625729470897}{72057594037927936},\qquad
 \eta_0=-\frac{7789843107295549}{4611686018427387904}.
\tag{SB.1}
$$

For a complete physical moving state $H=(H_1,H_2)$, use

$$
 \|H\|_{0,\phi}
 =\max_{i=1,2}\sup_{\substack{0\le r\le R\\
              \phi\in\mathbb R/(\pi/2)\mathbb Z}}|H_i(r,\phi)|,\qquad
 \|H\|_{A^0,\mathrm{pair}}
 =\sup_{0\le r\le R}\sum_{i=1}^2
                  \sum_{n\in4\mathbb Z}|(H_i)_n(r)|.
\tag{SB.2}
$$

For the original piecewise state and the compact mean centre, the
suprema include both closed one-sided values at every original
interface. This is the full state sup norm; its notation does not
assert that the remaining nonmean jumps vanish. The second norm
dominates the first and includes the true even mean. Neither component
has been divided by $\alpha$.

The original raw candidate is

$$
 Q^{\rm raw}=(\alpha U,\ s_{\eta_0,\nu_0}+\alpha V),
\qquad
 \mathtt{ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413}.
\tag{SB.3}
$$

Let $Q_0=Q^{\rm raw}+e$ be the exact continuous repair of
[the full-centre repair theorem](R133-supplement-exact-continuous-repair-of-final-centre.md),
with definition SHA256

`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`.

Let $Z$ be the complete unnormalized physical direction of
[the continuous-direction theorem](R133-supplement-explicit-continuous-response-direction-and-true-strip-norms.md).
Its definition SHA256 is

`6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`,

and the original full 193-component trial has SHA256

`ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6`.

The exact reference family used by
[the selected-family theorem](R133-supplement-selected-family-root-finite-part-and-actual-first-phase.md),
(B.2)--(B.3), and
[the core-difference theorem](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md),
(D.1), is

$$
 Q_\delta=Q_0+\delta Z,\qquad \nu_\delta=\nu_0+\delta,\qquad
 \eta_{\rm physical}=\eta_0,
\qquad
 |\delta_*|<d_*:=\frac{9368259853002}{10^{23}}<10^{-10}.
\tag{SB.4}
$$

The selected $\delta_*$ remains the implicit parameter certified there;
it is not replaced by either endpoint. A moving coefficient sometimes
also denoted by $\eta=-\gamma\langle v\rangle$ is not
$\eta_{\rm physical}$.

In (SB.4), the physical $v_0$ already contains $s_{\eta_0,\nu_0}$.
There is no additional $s_{\eta_0,\nu_\delta}-s_{\eta_0,\nu_0}$ term in
this explicitly defined physical reference. If it is expressed instead
as $s_{\eta_0,\nu_\delta}+\alpha V_\delta$, that difference must be kept
in $V_\delta$. This is a statement about the reference's definition,
not a statement that a true PDE solution is affine in $\nu$.

Write $Q^{\rm cm}$ for the compact-density centre at the unique TM
root $\xi_*$ certified in
[the actual terminal-mean result](R144-supplement-actual-terminal-mean-small-root-and-density.md).
By
[LC](R144-supplement-localized-full-state-C0-and-compact-source-receivers.md),
(LC.1)--(LC.5), it uses the same exact parameters (SB.1), the same raw
candidate, and

$$
 m=\langle v^{\rm raw}\rangle,\quad w=v^{\rm raw}-m,\quad
 j_\xi=1+(1+\xi\chi)\frac wm,\quad
 m_\xi=m+h_\xi,\quad
 Q_\xi^{\rm cm}=(u^{\rm raw},m_\xi j_\xi).
\tag{SB.5}
$$

Here $|\xi_*|\le\rho$, $|h_\xi|\le b$ are the actual saved TM rational
radii, and
$\chi=4096t^6(1-t)^6$ on $[1/20,9/50]$, with
$t=(r-1/20)/(13/100)$ and $\chi=0$ elsewhere.
This density parameter $\xi$ leaves the metric at $\nu_0$ fixed.

LC's old whole affine intrinsic box was consumed only as an enclosure
of the exact point $\eta_0$. The selected family (SB.4) also explicitly
fixes that point. The present argument neither needs nor infers a
result at every $\eta$ in the box.

## SB2. Complete saved bounds and their scope

The full repair theorem, (V.6) and its complete table, gives

$$
 \|e\|_{A^0,\mathrm{pair}}<e_0:=3.861\,10^{-18},\qquad
 \|\partial_\phi e\|_{A^0,\mathrm{pair}}
       <e_1:=1.970\,10^{-17}.
\tag{SB.6}
$$

The second follows also from the stated inhomogeneous $A^1$ bound.
These cover all 6144 original pieces, all 65 real coefficients and
the complete mean. They are bounds on the actual cumulative repair,
not a replacement of the raw candidate by the repaired one without
paying its difference.

The already proved full-interval bounds
[at (Cδ.2)](R133-supplement-selected-parameter-cap-row-transfer-with-unknown-high-input.md)
are

$$
 \|Z\|_{A^0,\mathrm{pair}}<19,\qquad
 \|\partial_\phi Z\|_{A^0,\mathrm{pair}}<83 .
\tag{SB.7}
$$

Their input is the complete
[response-repair summary](../notes/response_repair_source_ci/run-43597921732-1-complete-known-response-centre-repair/evidence/complete-known-response-centre-repair-source-summary.json),
Git blob `b4baed45ea0038c6aa38de8bd2939447ef2d39e0`.
It covers the entire interval $[0,25/8]$ and all 7721 common rows.
The full raw-response pair bounds are below $18.844974$ and
$82.074100$, and the complete continuous response repair costs less
than $2.292\,10^{-16}$ in $A_{1/64}$. Its support is at most 96,
so its first ordinary angular derivative costs at most 384 times
its $A^0$ bound.

For the potentially ambiguous field name `response_star_A0`, the
entire original
[source](../scripts/fourfold_codazzi_complete_response_repair_source.py),
Git blob `5e8c9311cab02eb88abdec135f26326610aee91e`, SHA256

`6e4e8f1a3f69fdc06c15a0471cedb62abce0740b4825ddf5a0d04de4b984d7ad`,

first forms the whole Bernstein pair bound of the original 193
trial and then adds a nonnegative full mean-error fee. Thus that
saved bound in particular bounds the raw trial. It is not used
here as evidence that the raw trial equals a mean-repaired true
solution derivative. The continuous-direction repair is still
added as in (Cδ.2). No bound restricted to the strict negative
strip is substituted for (SB.7).

The actual LC scientific result is
[the complete file from run 45797426031/1](../notes/localized_full_state_compact_sources_ci/run-45797426031-1/localized-full-state-and-compact-sources.json),
10486 bytes, Git blob `f7b66bcb9ee1d0fc45b52e3d86e6306ba6fe198c`,
SHA256

`60ac20418b405281a3150216e45f7bffd0e73b7625ccc8c383cf4204968b5748`.

Its [execution receipt](../notes/localized_full_state_compact_sources_ci/run-45797426031-1/execution.json)
has 16110 bytes, Git blob
`6683e76e103ac9d7ebbe5e30498a1312395e9d18` and SHA256

`f2b92ef6e63f5f54b6ebdd7997265f43100e6921a6da124b58d745b8c9d5104a`.

The complete result retains 7721 closed rows, 6143 original mean
interfaces, 1156 compact rows and 7722 successful saved readbacks.
The field `same_phi_C0_upper` is the entire decimal ball

~~~text
midpoint_integer =
19783981244604355228450852648262197371682635730730763814381525091944624969714533
radius_integer = 1
decimal_exponent = -84
mathematical_direction = upper
~~~

If $M$ denotes that displayed integer, define the exact outward endpoint

$$
 E_{\rm LC}:=(M+1)10^{-84}<1.979\,10^{-5}.
\tag{SB.8}
$$

The inequality is a rational comparison of the entire saved endpoint,
not of the displayed floating midpoint. The full LC proof and
[actual report](R144-supplement-actual-localized-full-state-and-compact-sources.md)
therefore give
$\|Q^{\rm cm}-Q^{\rm raw}\|_{0,\phi}\le E_{\rm LC}$.

There is a useful stronger consequence of the same saved quantity.
On each complete LC row, $W_A$ bounds $\|w\|_{A^0}$ and
$M_-$ is a positive lower bound for $|m|$. Equations (LC.5)--(LC.8)
actually imply

$$
 \begin{aligned}
 \|j_\xi\|_{A^0}
 &\le J_+:=1+(1+\rho X)W_A/M_-,\\
 \|v_\xi-v^{\rm raw}\|_{A^0}
 &=\|h_\xi j_\xi+\xi\chi w\|_{A^0}
 \le bJ_++\rho XW_A.
 \end{aligned}
\tag{SB.9}
$$

The first component of the difference is zero. The complete scientific
source, Git blob `dea3798975f692423aa570740c8d6cb5c8dc8b87`,
computes exactly `J=up(1+(1+E)*WA*invm)`,
`state_change=up(b*J+E*WA)` and the maximum over every row.
Consequently its same saved endpoint also proves

$$
 \|Q^{\rm cm}-Q^{\rm raw}\|_{A^0,\mathrm{pair}}\le E_{\rm LC}.
\tag{SB.10}
$$

This uses the explicit row majorant actually saved by LC. It does
not assert that an arbitrary sup-norm bound controls a Wiener norm,
and it adds no new numerical output or repeated target.

## SB3. The selected-reference bridge and its angular consequence

For any reference parameter with $|\delta|\le d_*$, exact subtraction
gives

$$
 Q^{\rm cm}-Q_\delta
 =(Q^{\rm cm}-Q^{\rm raw})-e-\delta Z.
\tag{SB.11}
$$

By (SB.6), (SB.7) and (SB.10),

$$
 \boxed{\quad
 \|Q^{\rm cm}-Q_{\delta_*}\|_{0,\phi}
 \le\|Q^{\rm cm}-Q_{\delta_*}\|_{A^0,\mathrm{pair}}
 \le E_{\rm LC}+e_0+19d_*<1.98\,10^{-5}.
 \quad}
\tag{SB.12}
$$

The last strict comparison follows already from
$E_{\rm LC}<1.979\,10^{-5}$, $d_*<10^{-10}$ and

$$
 1.979\,10^{-5}+1.9\,10^{-9}+3.861\,10^{-18}
 <1.98\,10^{-5}.
$$

The state is unnormalized throughout: multiplying $Z$ by $\alpha$
again or dropping either mean would change the object.

For possible later coefficient comparisons, the compact-centre
difference in (SB.10) has physical Fourier frequencies at most 128,
at every radial point and on both sides of each join. Thus

$$
 \begin{aligned}
 \|\partial_\phi(Q^{\rm cm}-Q_{\delta_*})\|_{A^0,\mathrm{pair}}
 &\le128 E_{\rm LC}+e_1+83d_* .
 \end{aligned}
\tag{SB.13}
$$

Indeed the radial scalars $h_\xi,m,\xi\chi$ in (SB.5) cannot create
new angular modes, so the derivative costs at most 128 on that
difference; the two other terms use their actual whole derivative
bounds. Neither (SB.12) nor (SB.13) bounds a radial derivative,
turns the changed principal coefficient into a zero-order
perturbation, transfers an inverse without its operator estimates,
or assigns finite support to an unknown exact correction.

## SB4. The metric change and the mean source remain explicit

For this section use $\widehat m=\langle v^{\rm cm}\rangle$,
$\widehat j=v^{\rm cm}/\widehat m$,
$\widehat U=\langle(u^{\rm cm})^2\rangle$ and
$\widehat J=\langle\widehat j^2\rangle$.
The completed TM construction gives the scalar mean equation at
$\nu_0$,

$$
 \widehat m'
 =\beta\widehat m
       (1-\widehat U-K_0\widehat m^2\widehat J).
\tag{SB.14}
$$

Keeping the same physical state and evaluating its scalar mean
residual at $\nu_\delta$ gives the exact identity

$$
 \begin{aligned}
 R_{\delta,\mathrm{mean}}(Q^{\rm cm})
 &:=
 \widehat m'-\beta\widehat m
       (1-\widehat U-K_\delta\widehat m^2\widehat J)\\
 &=\beta\widehat m^3(K_\delta-K_0)\widehat J .
 \end{aligned}
\tag{SB.15}
$$

It holds on every original open piece, with the already specified
one-sided traces and mean interfaces. Thus mean-exactness at
$\nu_0$ is not silently transferred to $\nu_\delta$.

For completeness, (D.2) of the core-difference theorem supplies
the exact finite metric changes, with $\gamma=\gamma_{\nu_0}$:

$$
 \gamma_\delta=\gamma e^{\delta\chi/2},\qquad
 K_\delta=e^{-\delta\chi}
       \left(K_0+\delta\frac{\beta\chi'}{2a^2\gamma^2}\right).
\tag{SB.16}
$$

The functions $a,\beta$ and the physical $\eta_0$ are unchanged.
Both differences vanish outside the exact compact support.
There is no division by $K$, including near the genuine root.

One can also retain the full ordinary metric source without
linearizing it. At a fixed physical $Q=(u,v)$, set
$m_Q=\langle v\rangle$, $I=\partial_\phi^{-1}P_{\ne0}$,

$$
 J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix},\qquad
 d_Q=-\beta I(u^2+Kv^2).
$$

By the complete nonlinear equation (D.3),

$$
 F_\nu(Q)=(d_Q I_2+\gamma_\nu m_QJ(K_\nu))Q_\phi
             +\beta(-u,v)-\beta(u^2+K_\nu v^2)Q .
\tag{SB.17}
$$

Write $\Delta K=K_\delta-K_0$ and
$\Delta(\gamma J)=\gamma_\delta J(K_\delta)-\gamma J(K_0)$.
Direct subtraction, with the same $Q$ and its full mean, gives

$$
 F_{\nu_\delta}(Q)-F_{\nu_0}(Q)
 =-\beta\Delta K\{I(v^2)Q_\phi+v^2Q\}
       +m_Q\Delta(\gamma J)Q_\phi .
\tag{SB.18}
$$

Therefore the ordinary residual $Q_r-F_\nu(Q)$ changes by the
negative of (SB.18). At $Q=Q^{\rm cm}$ this keeps both the
nonmean transport and the full mean coefficient. Changing the
metric while keeping this state does not change its existing
interface jumps; those complete jumps remain obligations of
the GC solve. The LC/CS residual bounds at $\nu_0$ and the old
selected-family inverse cannot be relabelled as bounds at this
new pair of state and metric without paying the corresponding
differences.

## SB5. What a true nu response must still supply

Suppose a genuine $C^1$ branch of complete physical solutions
$Q^{\rm true}(\nu)$ at fixed $\eta_0$, with the same angle/gauge
normalization, is later established. Write
$q_\nu=\partial_\nu Q^{\rm true}(\nu)$.
Since $Z$ in (SB.4) is one fixed explicitly defined function,
the fundamental theorem of calculus gives

$$
 Q^{\rm true}(\nu_*)-Q^{\rm true}(\nu_0)
 =\delta_*Z+
       \int_{\nu_0}^{\nu_*}(q_\nu-Z)\,d\nu .
\tag{SB.19}
$$

The integral is oriented if $\delta_*<0$. In particular,

$$
 \|Q^{\rm true}(\nu_*)-Q^{\rm true}(\nu_0)\|_{0,\phi}
 \le19d_*+
   \int_{\min(\nu_0,\nu_*)}^{\max(\nu_0,\nu_*)}
                \|q_\nu-Z\|_{0,\phi}\,d\nu .
\tag{SB.20}
$$

No completed result used here bounds the last integral.
A residual bound for the proposed response $Z$, or a finite
matrix alone, does not remove it. If the eventual exact solve
is performed directly at the already fixed metric $\nu_*$,
(SB.19) is unnecessary, but the true correction at that metric
must still be controlled.

## SB6. Usable posterior geometry budgets

There are two distinct, consistent ways to measure a future exact
GC correction.

First, if an actual solution $Q^\#$ at $\nu_*$ satisfies
$\|Q^\#-Q^{\rm cm}\|_{0,\phi}\le r_{\rm cm}$, then

$$
 \begin{aligned}
 \|Q^\#-Q^{\rm raw}\|_{0,\phi}
     &\le E_{\rm LC}+r_{\rm cm},\\
 \|Q^\#-Q_{\delta_*}\|_{0,\phi}
     &<1.98\,10^{-5}+r_{\rm cm}.
 \end{aligned}
\tag{SB.21}
$$

In particular $r_{\rm cm}\le8\,10^{-5}$ would put both distances
strictly below $10^{-4}$. This leaves a concrete remaining
state budget; it is not a proof that such a correction exists.

Second, if the solve is instead centered directly at
$Q_{\delta_*}$ and
$\|Q^\#-Q_{\delta_*}\|_{0,\phi}\le r_{\rm sel}$, then

$$
 \|Q^\#-Q^{\rm raw}\|_{0,\phi}\le e_0+19d_*+r_{\rm sel}.
\tag{SB.22}
$$

There is no reason to add $E_{\rm LC}$ again in this second
case. If a true branch is transported from a known correction
of $Q^{\rm cm}$ at $\nu_0$, combine (SB.20) with that correction
and $E_{\rm LC}$; its unknown integral remains part of the
posterior budget.

To connect either genuine state estimate to the original geometry,
put

$$
 \epsilon=\|Q^\#-Q^{\rm raw}\|_{0,\phi},\qquad
 t=|\nu_*-\nu_0|\le d_* .
$$

For $\epsilon\le10^{-3}$ and $t\le10^{-5}$, the already proved
[complete geometry response](R133-supplement-complete-C0-state-and-nu-geometry-response.md),
(C.1)--(C.3), applies at this exact same $\eta_0$:

$$
 \begin{aligned}
 \|\Delta\text{frame}\|_{C^0,\mathrm{op}}
 &\le b_Q+15.736315\epsilon+.304809t,\\
 \|\Delta\text{position}\|_{C^0}
 &\le b_F+1.950540b_Q+30.196406\epsilon+.105999t,\\
 \|\Delta S\|_{C^0,\mathrm{op}}
 &\le141.332651\epsilon+3.988052t .
 \end{aligned}
\tag{SB.23}
$$

The full-angle outer world-frame and position errors $b_Q,b_F$
are independent inputs. Keeping the same outer algebraic state
does not by itself prove a common world anchor, remove the
outer-height requirement, or prove Euclidean holonomy.
The algebraic $S$ becomes the geometric second fundamental
form only for the established exact GC immersion.

All references above concern the finite design comparison
$\nu_0\to\nu_*$. An eventual nonrigid continuous flex family must
keep its chosen metric fixed, including $\nu_*$ and $\eta_0$.
Varying $\nu$ is not that family. The remaining full GC solve,
phase compatibility, matching, closure and nonrigidity must be
proved in the same fixed metric.
