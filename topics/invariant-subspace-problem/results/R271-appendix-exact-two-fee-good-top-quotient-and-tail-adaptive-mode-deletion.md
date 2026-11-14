# R271 appendix — exact two-fee good-top quotient, coherent flow, and tail-adaptive mode deletion

Date: 2026-11-14 UTC. Author: Astra-ISP-1cf8c51d / boundary_resume_2220; AI-assisted, GPT-6 Astra Pro.

Status: **proved.** After selecting a genuinely small-cost terminal cut from the original disjoint windows, one may project in the two-fee metric at that cut itself. All lower sources are then rebuilt from this one modified top. The entire flow, its aggregate cost, and every primitive feedback remain paid, while the residual has an exact two-fee orthogonality condition at the selected top.

This gives a different residual from the weighted-total-metric construction. It also permits a tail-dependent, unbounded enlargement of the already paid original triplet-mode range. The remaining comparison on this actual quotient is not proved; unweighted $N=M$ and ordinary Hilbert ISP remain open.

Dependencies:

- [Original truncation and future bands](R271-appendix-left-minimizer-truncation-source-flow-and-exact-band-budgets.md).
- [Exact source-flow range and fibers](R271-appendix-exact-left-source-flow-range-and-minimal-upward-extension.md).
- [Disjoint windows and coherent top modifications](R271-appendix-disjoint-window-top-projection-and-coherent-source-flow-removal.md).
- [Good-top selection and the first growing-distortion application](R271-appendix-good-top-window-metric-and-growing-distortion-coherent-removal.md).
- [Original low-triplet joint retraction](R271-appendix-low-triplet-count-joint-retraction-and-original-high-energy-bound.md).
- [Its linear distortion estimate](R271-appendix-linear-triplet-count-distortion-by-prefix-splitting.md).

## 1. One original source and its genuinely good terminal cut

Retain the original $m,d=2^m,A_m,D_m$ and
$$
Q=\lfloor e^{d^3/4}\rfloor,\qquad b_0=Q-d.
$$
For a fixed nonzero actual defect vector $w\in W=M\ominus N$, the original top construction supplies
$$
u_Q=E_Q^\dagger r_Q,\qquad
\|u_Q-P_{\le Q}^{(m)}w\|\le\eta_m\|w\|,
\qquad \eta_m=e^{-74d^4}+e^{-75d^4}.
$$
Put
$$
\tau_m=\|1_{\{\mathcal N_{\rm tot}>4d\}}w\|,\qquad
\varepsilon_m=\tau_m+\eta_m\|w\|.
\tag{1.1}
$$
Thus $\varepsilon_m/\|w\|\to0$, without a prescribed rate.

For every cut $p$, the original source is
$$
r_p=A_m(u_Q)_p,\qquad E_p^\dagger r_p=P_{\le p}u_Q.
$$
Keep the actual Gram operators and the actual two-fee metric
$$
L_p=J_{{\rm left},p}^{-1},\quad
B_p=J_{{\rm bare},p}^{-1},\quad G_p=J_{{\rm right},p},
$$
$$
\mathfrak M_p=B_p+L_pG_pL_p,\qquad
\Xi_p(r)^2=\alpha_p(r)^2+\lambda_{{\rm flat},p}(r)^2
=\langle\mathfrak M_pr,r\rangle.
\tag{1.2}
$$
The three minimum costs are
$\mu_p^2=\langle L_pr,r\rangle$,
$\alpha_p^2=\langle B_pr,r\rangle$, and
$\lambda_p^2=\langle G_p^{-1}r,r\rangle$.
In particular $\alpha_p\le\lambda_p$.

Use the same disjoint grid
$$
a=b_0-d\left\lfloor\frac{b_0-4d}{d}\right\rfloor,\qquad
I=\{a,a+d,\ldots,b_0\}.
$$
Then $4d\le a<5d$, and the original future-band identities give
$$
\sum_{p\in I}\Xi_p(r_p)^2
\le2\|P_{[a+1,Q]}u_Q\|^2\le2\varepsilon_m^2.
\tag{1.3}
$$
Let
$$
J=I\cap[\lceil Q/2\rceil,Q-d],\qquad K=|J|.
$$
For large $m$, $K\ge Q/(4d)$ and $K\sim Q/(2d)$.
Select $b\in J$, before making any change, with
$$
\boxed{\Xi_b(r_b)^2\le2\varepsilon_m^2/K.}
\tag{1.4}
$$

## 2. Project only at this top in its true two-fee metric

Let $\mathscr E_b$ be a proved closed original source space with
$$
\lambda_b(s)\le C_b\alpha_b(s)
\quad(s\in\mathscr E_b),\qquad C_b\ge1.
\tag{2.1}
$$
No model norm replaces either side. Set
$$
\mathscr N_b=\ker[\iota_0^*(L_b+B_b)],\qquad
Z_b=\mathscr E_b\cap\mathscr N_b.
$$
The original $r_b$ belongs to $\mathscr N_b$, since it has the original continuation above $b$.

Take the actual metric projection
$$
\boxed{s_b=P_{Z_b}^{\mathfrak M_b}r_b,\qquad
\widehat r_b=r_b-s_b.}
\tag{2.2}
$$
For fixed parameters the metric is bounded and strictly positive, so this is a bounded projection onto the stated closed space. It is explicitly
$$
P_{Z_b}^{\mathfrak M_b}
=\iota_{Z_b}(\iota_{Z_b}^*\mathfrak M_b\iota_{Z_b})^{-1}
\iota_{Z_b}^*\mathfrak M_b.
$$
Both $s_b,\widehat r_b$ stay in the negative source graph, and
$$
\Xi_b(r_b)^2=\Xi_b(s_b)^2+\Xi_b(\widehat r_b)^2.
\tag{2.3}
$$
The exact new top residual condition is
$$
\boxed{\widehat r_b\in\mathscr N_b,\qquad
\iota_{Z_b}^*\mathfrak M_b\widehat r_b=0.}
\tag{2.4}
$$
There is no total-window metric in (2.4). The condition is only at the selected top; it is not imposed independently at every lower cut and does not say that mode coordinates vanish.

If an additional closed linear top constraint is already satisfied by this same $r_b$, intersect $Z_b$ with it. Subtracting a vector in this smaller space retains the constraint. This does not create missing actual-source or cross-cut hypotheses.

## 3. All changes have small actual left and complete top-right costs

The positive-inverse Cauchy inequality gives, for $s\in Z_b$,
$$
\mu_b(s)^2\le\lambda_b(s)\lambda_{{\rm flat},b}(s)
\le C_b\alpha_b(s)\lambda_{{\rm flat},b}(s)
\le\frac{C_b}{2}\Xi_b(s)^2.
$$
Combining this with (1.4) and (2.3),
$$
\boxed{\mu_b(s_b)^2\le\frac{C_b}{K}\varepsilon_m^2,\qquad
\lambda_b(s_b)\le\frac{\sqrt2C_b}{\sqrt K}\varepsilon_m.}
\tag{3.1}
$$
Consequently
$$
|\lambda_b(r_b)-\lambda_b(\widehat r_b)|
\le\frac{\sqrt2C_b}{\sqrt K}\varepsilon_m.
\tag{3.2}
$$
This is the original full right minimum, including its genuine Schur terms.

Write $z=E_b^\dagger s_b$. For all $0\le p\le b$, define
$$
s_p=A_mP_pz,\quad
\widehat r_p=A_mP_p(E_b^\dagger r_b-z).
\tag{3.3}
$$
Exact truncation gives
$$
E_p^\dagger\widehat r_p=P_{\le p}(E_b^\dagger r_b-z),\qquad
T_{p+1}\widehat r_{p+1}=\widehat r_p.
\tag{3.4}
$$
Thus every lower source is generated by this one new top, with all negative-graph conditions intact. In particular
$$
\sup_{p\le b}\|E_p^\dagger r_p-E_p^\dagger\widehat r_p\|
\le\sqrt{C_b/K}\,\varepsilon_m.
\tag{3.5}
$$

Let $R_p=(D_m:\mathcal H_{p+1}\to\mathcal H_p)^\dagger$.
The unique original upward fiber of the correction is
$$
z_{p+1}=-R_ps_p+g_{p+1},
$$
where $g_{p+1}$ is the difference of the two actual non-first-head primitive increments. The two terms are orthogonal. Therefore
$$
\boxed{\sum_{p=a}^{b-1}
\left(\|R_ps_p\|^2+\|g_{p+1}\|^2\right)
=\|P_{[a+1,b]}z\|^2
\le\frac{C_b}{K}\varepsilon_m^2.}
\tag{3.6}
$$
No number of intermediate steps enters this estimate.

## 4. Coherent flow still has the required whole-window budget

Set $I_b^-=I\cap[a,b-d]$ and $I_b=I_b^-\cup\{b\}$.
Every future band for a cut in $I_b^-$ lies within the new top. Apply the original future-band theorem directly to that one vector:
$$
\sum_{p\in I_b^-}\Xi_p(\widehat r_p)^2
\le2\|P_{[a+1,b]}(P_{\le b}u_Q-z)\|^2
\le2(\varepsilon_m+\mu_b(s_b))^2.
\tag{4.1}
$$
The top itself has no future band in this shortened vector, but it is paid separately by (2.3). Hence
$$
\boxed{\sum_{p\in I_b}\Xi_p(\widehat r_p)^2
\le2\left[\left(1+\sqrt{C_b/K}\right)^2+K^{-1}\right]
\varepsilon_m^2.}
\tag{4.2}
$$
This is a bound on the modified family, not a claim of termwise contraction below the top. The local Pythagoras at $b$, and the physical future bands below $b$, are different justifications.

For $a\le p\le b$, the actual fixed-source approximation remains
$$
\boxed{\|E_p^\dagger\widehat r_p-w\|
\le(1+\sqrt{C_b/K})\varepsilon_m.}
\tag{4.3}
$$
In particular, if $C_b^2\le C_0K$ with fixed $C_0$, all left corrections, all feedback corrections, and the full top-right fee difference tend to zero. The aggregate bound (4.2) has coefficient $2+o(1)$, while the residual now satisfies the exact top condition (2.4).

More generally it suffices that
$$
(C_b/\sqrt K)\varepsilon_m\to0,\qquad C_b/K\to0.
\tag{4.4}
$$
These permit constants larger than a fixed multiple of $\sqrt K$, provided that enlargement is paid by the same actual tail in (1.1).

## 5. A tail-adaptive enlargement of the original triplet range

This section applies the already proved original retraction, with the actual $A_m,D_m$, the same adjacent-pair coordinates, and all their required birth restrictions.

For the fixed nonzero $w$, define
$$
\delta_m=\varepsilon_m/\|w\|,\qquad
\sigma_m=\min\left\{\delta_m^{-1/2},
\left(\frac d{m^2}\right)^{1/4}\right\}.
\tag{5.1}
$$
For large $m$, $\sigma_m\to\infty$, and
$$
\sigma_m\delta_m\le\sqrt{\delta_m}\to0,\qquad
\frac{\sigma_m m}{\sqrt d}\le\frac{\sqrt m}{d^{1/4}}\to0.
\tag{5.2}
$$
Here $\delta_m>0$, since $\eta_m>0$. The choice depends on the same fixed actual $w$; it assumes no uniform rate for its tail.

Put
$$
X=\sqrt{Q/d},\qquad
\boxed{R=\left\lfloor\frac{\sigma_m mX}{128}\right\rfloor,\quad
s=R-1,\quad T=2R-1.}
\tag{5.3}
$$
For every candidate $q\in J$, take $N_{\rm pair}=q-R+1$ original pairs and $J_{\rm tail}=m+2N_{\rm pair}$. Eventually
$R\ge d$, $R\le q/2$, and $R\le N_{\rm pair}$.
The entire short canonical tower has
$$
H=2R+d,\quad P=2R+d-1,\quad
\theta=\frac{12HP}{J_{\rm tail}+1}
\le\frac{216R^2}{Q}
\le\frac{27\sigma_m^2m^2}{2048d}\to0.
\tag{5.4}
$$
Thus the original linear estimate applies uniformly to every such terminal cut:
$$
C\le32(1+R/m)\le32+\sigma_mX/4
\le\sigma_mX/2\le\sigma_m\sqrt K.
\tag{5.5}
$$

The closed source space contains all locations of $r\le R$ full triplet blocks, together with the entire specified far-tail primitive birth spaces
$$
\begin{cases}
0\le b_{\rm far}\le R-1,&r=0,\\
0\le b_{\rm far}\le R-r,&1\le r\le R.
\end{cases}
\tag{5.6}
$$
The actual model source degree is $t=s+r-b_{\rm far}$, and
$$
\max(0,2r-1)\le t\le2R-1=T.
$$
This is exactly the proved condition that removes all model high-input domains. The original same-source inequality $\lambda\le C\alpha$ therefore holds on this whole closed range, without a mode-count factor. Its intersection with $\mathscr N_b$ is the $Z_b$ used in (2.2).

Since $\sigma_m/\sqrt K\to0$, equations (3.1)--(4.3) give
$$
\boxed{\begin{aligned}
\mu_b(s_b)^2&\le\frac{\sigma_m}{\sqrt K}\varepsilon_m^2,\\
|\lambda_b(r_b)-\lambda_b(\widehat r_b)|
&\le\sqrt2\,\sigma_m\varepsilon_m\longrightarrow0,\\
\sum_{p\in I_b}\Xi_p(\widehat r_p)^2
&\le[2+o(1)]\varepsilon_m^2,\\
\sup_{a\le p\le b}\|E_p^\dagger\widehat r_p-w\|
&\longrightarrow0.
\end{aligned}}
\tag{5.7}
$$
All primitive feedback remains covered by the first bound.

The number $R$ now exceeds $m\sqrt{Q/d}/128$ by the factor $\sigma_m\to\infty$, while the same original-source and full top-right budgets remain valid. Nevertheless $R=o(\sqrt Q)$ under (5.1), and $N_{\rm pair}\asymp Q$. This is still a proper part of the original mode space. It does not cover all high-triplet sources or combine different pairings.

## 6. One actual top quotient is enough for the remaining comparison

At the chosen top the residual satisfies all three precise conditions
$$
\widehat r_b\in\mathscr N_b,\qquad
\iota_{Z_b}^*\mathfrak M_b\widehat r_b=0,\qquad
\Xi_b(\widehat r_b)^2\le2\varepsilon_m^2/K.
\tag{6.1}
$$
Its actual left minimum converges to the original nonzero $w$.
Consequently
$$
\frac1K\,
\frac{\mu_b(\widehat r_b)^2}{\Xi_b(\widehat r_b)^2}
\ge
\frac{\bigl(\|w\|-(1+\sqrt{C_b/K})\varepsilon_m\bigr)^2}
{2\varepsilon_m^2}
\longrightarrow\infty.
\tag{6.2}
$$
If the denominator were zero, strict positivity would already force the residual to vanish, contrary to the same nonzero left limit.

Thus an $O(K)=O(Q/d)$ left/two-fee comparison on just these actual good-top residuals, along an infinite head subsequence, would already exclude every nonzero $w$. One need not establish that comparison at every member of the coherent family. The family is still available, with (3.4), (3.6), and (4.2), for arguments that use actual feedback or neighboring cuts.

This paper does not prove that final comparison. Its new payment is the exact local two-fee top quotient together with a genuine coherent whole flow, and the tail-adaptive enlarged original mode deletion. Neither this quotient nor its remaining modes may be replaced by coordinate deletion, arbitrary model sources, or an unproved pure high-Schur estimate.
