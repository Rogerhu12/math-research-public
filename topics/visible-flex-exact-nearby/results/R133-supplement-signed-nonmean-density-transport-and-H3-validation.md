# R133 supplement: signed nonmean density transport and complete H3 validation

2026-11-15, newton_source.

**Proved identities and a new validation contract; no new numerical execution is asserted.** This continues [CT](R133-supplement-regular-density-transport-for-complete-first-coefficient.md) and [PF](R133-supplement-pointwise-root-finite-part-and-complete-true-ray-first-coefficient.md). It defines a new complete angular target. The accepted scalar finite part, ray flow and circle conjugacy are read unchanged.

The family, true root and signs are CT.1--2. Write $P_\perp=1-\Pi$, $I=\partial_\phi^{-1}P_\perp$, and use physical frequencies $4j$ and normalized measure on the period $\pi/2$. Both moving means and both branches remain. A $\rho$ derivative holds the original moving angle fixed.

## SN1. Exact nonmean algebra

Use CT.10; the radial $A=(16\eta\sqrt{k})^{-1}$ is not an operator. Put
$$
 E_\pm=P_\perp(u^2\pm\rho kv^2),\quad
 U=P_\perp u^2,\quad V=P_\perp v^2,\quad
 \bar B=\langle B\rangle,\quad d=-bI E_- .
 \tag{SN.1}
$$
Thus $d_\phi=-bE_-$ and $\langle d\rangle=0$. Since $B=8Aa_r$ and $C=16Aa_r^2$, with $a_r=k_\rho/(4k)-b(1+u^2+\rho kv^2)$,
$$
 \begin{split}
 B_\perp&=-8AbE_+,\\
 C_\perp&=-4b\bar B E_++16Ab^2P_\perp(E_+^2),\\
 D_\perp&=64Ab^2kP_\perp(u^2v^2)
               +2b\sqrt{k}P_\perp(uv_\phi-vu_\phi).
 \end{split}\tag{SN.2}
$$
These are signed Laurent identities. Every product includes all output labels and its mean before the displayed final projection. In particular $P_\perp(E_+^2)$ is not replaced by separately bounded factors.

There is an exact even-source cancellation:
$$
 d_{\phi\phi}=-2b(uu_\phi-\rho kvv_\phi),\qquad
 a_{\rm e}=-\frac12d_{\phi\phi}.
 \tag{SN.3}
$$
The root scalar $g_0=A(0)$ remains parameter dependent. CT.7 gives
$$
 \chi_\perp=-\frac{26}{3}b_*g_0U_*,
 \qquad \bar\chi=A_\rho(0)+\langle B(0)\rangle .
 \tag{SN.4}
$$
A star denotes the same true root. The scalar in SN.4 is the full root mean.

Set $J=b(8A+2g_0/3)$ and $J_*=26b_*g_0/3$. Then
$$
 -P_\perp B_1-\frac{2g_0}{3}d_1
 =\frac{JU-J_*U_*}{\rho}
                   +bk\left(8A-\frac{2g_0}{3}\right)V .
 \tag{SN.5}
$$
Indeed substitute $B_\perp=-8Ab(U+\rho kV)$ and $d_\phi=-b(U-\rho kV)$. In the common root germ the removable quotient is evaluated by
$$
 \begin{split}
 \frac{JU-J_*U_*}{\rho}
 &=J\frac{U-U_*}{\rho}+\frac{J-J_*}{\rho}U_*,\\
 \frac{J-J_*}{\rho}
 &=8b\frac{A-g_0}{\rho}+\frac{26g_0}{3}\frac{b-b_*}{\rho},\\
 \frac{U-U_*}{\rho}
 &=P_\perp\left[\frac{u-u_*}{\rho}(u+u_*)\right].
 \end{split}\tag{SN.6}
$$
These include $\rho=0$ by analytic limits. Away from the root the original signed quotient remains exact. No subtraction of norm upper bounds is used. The radial $A_2$ has exactly zero nonmean projection and is absent from the next source.

## SN2. The complete mean and the new equation

Integrating CT.13 gives
$$
 \langle U_\sigma(s)\rangle=\sigma m_\delta(s),\quad
 m_\delta(0)=0,\quad m_\delta'=\langle G_+\rangle .
 \tag{SN.7}
$$
All divergence terms have zero mean, and the remaining scalar terms reverse sign with $\sigma$. Define $V_\sigma=U_\sigma-\sigma m_\delta$. For $s=\sqrt\rho$,
$$
 \boxed{\quad
 \partial_sV_\sigma+
 2s\partial_\phi[(d+\sigma\eta s\sqrt{k})V_\sigma]
 =F_\sigma,\qquad V_\sigma(0)=0,\quad\langle V_\sigma\rangle=0 ,
 \quad}\tag{SN.8}
$$
with the complete regular source
$$
 \boxed{\begin{split}
 F_\sigma={}&
 \sigma\left\{\frac{JU-J_*U_*}{\rho}
       +bk\left(8A-\frac{2g_0}{3}\right)V\right\}
 -\sigma C_\perp+\sigma\rho D_\perp\\
 &-2\sigma\partial_\phi[d(\chi+s m_\delta)]
       +s d_{\phi\phi}-2s\eta\sqrt{k}\chi_\phi .
 \end{split}}\tag{SN.9}
$$
Every term has zero mean. The last two terms have no $\sigma$. The true mean remains in the density flux.

For any supplied scalar reference $\widehat m$,
$$
 F_\sigma(m_\delta)=F_\sigma(\widehat m)
       -2\sigma s(m_\delta-\widehat m)d_\phi .
 \tag{SN.10}
$$
Its $q$th angular derivative costs at most
$2s|m_\delta-\widehat m|\,\|d^{(q+1)}\|_2$.
Thus using an old reference at $\delta=0$ requires an explicit parameter fee.

The complete known fields have degree at most96. The new source has degree at most384 and $d$ degree at most192. The exact unknown $V_\sigma$ has no cutoff.

## SN3. Read the old radial means

The accepted run43591721337 native contains all3146 strict integrals and the root Taylor finite part; its SHA256 is
cd9ffed6d8c9e107eaac2b50f1846219d8ec90a130555bb91859d465c9bab202.
It is a $\delta=0$ computation. The run43597209022 parameter-transfer native, SHA256
06070fd3b4bd7a3e4ba17d99821c0f6ad06393863bf538f9a8157b6187e60dbb,
supplies the complete same-family parameter derivative.

Let $\mathcal I_\delta(\rho)=\operatorname{FP}\int_0^\rho\langle\Xi_\delta(t)\rangle\,dt$. The exact mean is
$$
 m_\delta(\sqrt\rho)
 =-\frac12\mathcal I_\delta(\rho)
       -\frac{g_{0,\delta}}{3\rho^{3/2}}
       -\frac{\bar\chi_\delta}{\sqrt\rho}.
 \tag{SN.11}
$$
At an original strict endpoint $r$, $\mathcal I_0(r_*-r)$ is the saved root finite part plus the suffix sum of the original signed integrals from $r$ to the accepted root cut. Only stored intervals are added; the old quadrature and root search are not called.

In the common root germ the saved normalized scalar coefficients give
$$
 \begin{split}
 m_0(\sqrt\rho)={}&
 -\frac12\sum_{j=2}^{5}\frac{A_j\rho^{j-3/2}}{j-3/2}
 -\frac12\sum_{j=1}^{4}\frac{B_j\rho^{j-1/2}}{j-1/2}\\
 &-\frac12\sum_{j=0}^{3}\frac{C_j\rho^{j+1/2}}{j+1/2}
 +\frac12\sum_{j=0}^{2}\frac{D_j\rho^{j+3/2}}{j+3/2}
       +\mathcal R_m(\rho),\\
 |\mathcal R_m(\rho)|\le{}&
 \frac{\rho^{9/2}}9
       (M_{A,6}+M_{B,5}+M_{C,4}+M_{D,3}).
 \end{split}\tag{SN.12}
$$
The $B_j,C_j,D_j$ here are complete scalar means. The four $M$ are the original next normalized derivative bounds. This is a restriction of saved bounds, not a new root Taylor calculation.

Suppose the original receipt bounds $\partial_\delta(A,B,C,D)$ by
$(M_A,M_B,M_C,M_D)$ on the same complex $\rho$ disk of radius $R$.
For $0\le\rho<R$ and $|\delta|\le d$,
$$
 |m_\delta-m_0|
 \le d\left[
 \frac{M_A\sqrt\rho}{R^2(1-\rho/R)}
 +\frac{M_B\sqrt\rho}{R(1-\rho/R)}
 +M_C\sqrt\rho+\frac{M_D\rho^{3/2}}3\right].
 \tag{SN.13}
$$
The first two terms cancel the constant and first root coefficients before integration. On a strict interval one may instead use
$$
 |m_\delta-m_0|
 \le d\left[\frac12L_{\mathcal I}(\rho)
    +\frac{M_{g_0}}{3\rho^{3/2}}
    +\frac{M_{\bar\chi}}{\sqrt\rho}\right],
 \quad M_{g_0}\le M_A,\quad M_{\bar\chi}\le M_A/R+M_B .
 \tag{SN.14}
$$
Here $L_{\mathcal I}$ is the original full parameter-derivative integral bound. The old total186751.988620238 is an available conservative bound. Partial cells use the original nonnegative full cell derivative bound, not a proportional fraction of its signed integral.

A scalar interpolant $\widehat m$ needs a separate interior enclosure. Saved endpoints alone do not bound partial integrals. One legal new local receiver uses a complete cell modulus of the mean source, the saved endpoint finite part and the exact counterterms in SN.11. No unproved sign or monotonicity is assumed. Form $\bar\chi_\delta+s\widehat m$ as a signed interval before taking a modulus; bounding these summands independently loses the intended cancellation.

## SN4. Original input restrictions

The exact candidate SHA256 is
ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413.
Its first two original parts cover the full negative interval, with SHA256
5dae124eef0b3004bfea08334c2f2546ade3edc5cb926c665591e42b842babc4
and
3aeb38bf0577207cafcad3a59e43ed5a04a4c9cf9a703c4c3c4088c963a09106.
The complete index fixes all nodes,65 slots and the exact binary64 $\alpha$.

The accepted repair and full193 direction natives have SHA256
6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc
and
87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88.
Their continuity repair is not rebuilt. The accepted root scalarization native
10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f
already contains the exact base root offset and the complete complex193 direction envelope.

On the root piece evaluate the original cubic as a signed polynomial. The constant base offset cancels from $(u-u_*)/\rho$ and remains in $u+u_*$. For $\delta Z$, use the saved complex coefficient envelope and a genuine radial Cauchy difference on its larger disk. Do not divide a whole bound by a zero-containing $\rho$ interval. The same rule applies to $(A-g_0)/\rho$. For $(b-b_*)/\rho$, the original intrinsic germ and
$b_\rho=-(a_{\rm phys}''/a_{\rm phys}-b^2)$ supply a complete removable value.

The169 scalar germ files and626 scalar cells are read in their original order, retaining the normalized point jets, whole final derivative and exact polynomial models. Restricting one saved Taylor model preserves its old remainder. It does not call the original scalar target or regenerate its coefficients.

The compact intrinsic changes are exactly
$G_\delta=e^{\delta w/2}G_0$ and
$K_\delta=e^{-\delta w}(K_0+\delta T w')$,
using the accepted scalar and compact-$T$ models. They vanish near the root. The mean-dependent $\eta=-G_\delta\langle v_\delta\rangle$ still changes there and is not frozen with the metric.


## SN5. Signed references and their complete residual

A new computation may choose a finite Fourier, piecewise polynomial reference $\widehat V_\sigma$ with zero mean. Its coefficients are exact dyadic rationals; a floating calculation may propose them. No cutoff is assigned to the exact target.

Put $a_\sigma=2s(d+\sigma\eta s\sqrt{k})$. For a scalar reference $\widehat m$, validate
$$
 \mathcal E_\sigma
 =\partial_s\widehat V_\sigma
       +\partial_\phi(a_\sigma\widehat V_\sigma)
       -F_\sigma(\widehat m).
 \tag{SN.15}
$$
A degree-$N$ reference requires every signed residual label through
$\max(N+192,384)$, including mean. Complete Laurent products precede norms; there is no aliasing allowance.

The exact error has source
$-\mathcal E_\sigma-2\sigma s(m_\delta-\widehat m)d_\phi$.
For $q=0,1,2,3$, its source column is bounded by
$$
 f_{\sigma,q}\ge
 \|\partial_\phi^q\mathcal E_\sigma\|_2+
 2s|m_\delta-\widehat m|\,\|d^{(q+1)}\|_2 .
 \tag{SN.16}
$$
Signed interval polynomial or Bernstein enclosures must cover each complete radial cell. Values only at interpolation nodes do not validate the residual.

Source polynomials, reference coefficients and signed intermediate arrays stay temporary in the same public run. Their complete validation and final norm can be published as a small conclusion. If a reference is used, it is proposed and validated while this new source is still available, rather than regenerating an accepted source later.

A reference value jump at an interface is paid as a four-entry angular-norm impulse. The true target is continuous by PF and the original strict-frame matching. Background derivative jumps remain in the separate higher-order return remainder.

## SN6. Four-state H3 energy

For real $a$, the equation $\partial_s f+\partial_\phi(af)=F$ gives, with $z_q=\|\partial_\phi^qf\|_2$,
$$
 D^+z_q\le
 (q+\tfrac12)\|a_\phi\|_\infty z_q
 +\sum_{\ell=2}^{q+1}{q+1\choose\ell}
       \|a^{(\ell)}\|_\infty z_{q+1-\ell}
 +\|\partial_\phi^qF\|_2,\qquad0\le q\le3 .
 \tag{SN.17}
$$
The differentiated first term $af^{(q+1)}$ contributes
$-\tfrac12a_\phi|f^{(q)}|^2$ by real integration by parts; the remaining diagonal coefficient is $q+1$. An upper Dini derivative, or positive norm regularization followed by its limit, covers zero norms.

For SN.8, $a^{(\ell)}=2s d^{(\ell)}$. Real optical translation has no angular derivative and no energy growth fee. The $q=3$ row needs the genuine fourth derivative of $d$. The source through $q=3$ also contains the fifth derivative of $d$ from SN.3 and therefore needs complete state derivatives through order4. These orders are not inferred from lower norms without their fees.

Let $M_i$ be the nonnegative lower-triangular4-by-4 majorant of SN.17 on a real cell of length $h_i$. Set $\lambda_i=\max\operatorname{diag}M_i$ and $N_i=M_i-\operatorname{diag}M_i$. Since $N_i^4=0$,
$$
 E_i=e^{\lambda_i h_i}
          \sum_{k=0}^{3}\frac{h_i^kN_i^k}{k!},\qquad
 z_{\rm out}\le E_i(z_{\rm in}+h_if_i).
 \tag{SN.18}
$$
This is a componentwise upper bound for the complete Duhamel solution. Initial and interface errors enter the same four-state coordinates, in actual radial order.

One may switch from $s$ to original $r$ after the root collar with
$ds=|dr|/(2\sqrt\rho)$. Both ordinary source and coefficient lengths are transformed. No point count replaces the measure.

The exact physical Fourier norm is
$$
 \|f\|_{H^3}^2
 =\sum_{j\in\mathbb Z}(1+16j^2)^3|f_j|^2
 =z_0^2+3z_1^2+3z_2^2+z_3^2 .
 \tag{SN.19}
$$
Both signs and the mean are included before any exact nonmean identity is used. A supremum over radius is not interchanged with an angular sum.

## SN7. Terminal scalar and true-angle density

At $\rho=r_*$, define
$$
 A_{\mathrm{term},\delta}
  =\frac{g_{0,\delta}}{3r_*^{3/2}}
       +\frac{\bar\chi_\delta}{\sqrt{r_*}}
       +m_\delta(\sqrt{r_*})
  =-\frac{\mu_\delta}{2}.
 \tag{SN.20}
$$
This follows from SN.11 for the same complete scalar finite part. At the selected parameter its existing certificate is read; $\mu_0$ is not substituted.

Let $j=\mathcal H'$ be the true selected conjugacy and put
$$
 q_\sigma=V_\sigma(\sqrt{r_*})
       +\frac{\sigma\chi_\perp}{\sqrt{r_*}}
       +\sigma A_{\mathrm{term},\delta_*}(1-j).
 \tag{SN.21}
$$
These functions have zero mean. CT.20 gives
$$
 c-\mu_{\delta_*}
  =U_{R_\Omega^{-1}}U_{\mathcal H^{-1}}q_-
                      -U_{\mathcal H^{-1}}q_+ .
 \tag{SN.22}
$$
The real rotation is an isometry. No new ray flow or two-leg numerical reconstruction is needed at the terminal endpoint.

The existing [AC](R133-supplement-actual-conjugacy-density-transfer-for-complete-first-coefficient.md) gives the conservative bound
$$
 \|c-\mu\|_{H^3}
 \le2^{20}\big(\|q_-\|_{H^3}+\|q_+\|_{H^3}\big).
 \tag{SN.23}
$$
The new computation retains signed terminal references and may consume the already accepted finite conjugacy $G=K48\circ H$ and actual strip error to sharpen the true $j$ and inverse-density derivative bounds. It reads finite coefficients without refitting them, and pays the complete analytic correction and the true density measure. A finite approximation is never silently identified with the exact $j$.

The postcomposition native has SHA256
a44d6a6b2d0bad07d60e323142fd266b8dd91a645afa9d306fe22c8794a84f60.
The refined angle native has SHA256
dfb2a174a010d399775240b2bd07a0f547dfee5fc137e12141be9fd8a46e3854.
Any sharper scalar constants are new consumers of these originals and need their actual domains. The original KAM iterations are not repeated.

## SN7a. Concrete read-only true-angle derivative consumer

Write $G=K_f\circ H_f$ for the two fixed exact finite lifts, keeping the symbol $\mathcal H$ for the true conjugacy. Read their original sine/cosine coefficients, and read from the selected successful strip-refinement row
$$
 E_0\ge\|\mathcal H-G\|_{A_\tau},\quad
 E_1\ge\|\mathcal H'-G'\|_{A_\tau},\qquad \tau=1/128 .
 \tag{SN.24}
$$
The fields are physical_true_conjugacy_minus_G_norm and
physical_true_conjugacy_derivative_minus_Gprime_norm. They belong to that same selected theorem and parameter; a different R31 loss is not identified with it by assumption.

Let $h_i\ge\|H_f^{(i)}\|_\infty$ and
$k_i\ge\|K_f^{(i)}\|_\infty$. For $i=1$, include the identity derivative. The higher derivatives are complete finite trigonometric sums of the read coefficients. Real composition stays on the real circle, so complete derivative bounds are
$$
 \begin{split}
 g_1&=k_1h_1,\\
 g_2&=k_2h_1^2+k_1h_2,\\
 g_3&=k_3h_1^3+3k_2h_1h_2+k_1h_3,\\
 g_4&=k_4h_1^4+6k_3h_1^2h_2
          +3k_2h_2^2+4k_2h_1h_3+k_1h_4 .
 \end{split}\tag{SN.25}
$$
These are new complete derivative targets, not a rerun of a circle iteration or terminal return residual.

Set $b_0=1$ and $b_q=(q/(e\tau))^q$ for $q>0$. Complete signed Fourier sums give
$$
 \epsilon_q=\min(E_1b_q,E_0b_{q+1}),\qquad
 \|(j-G')^{(q)}\|_2\le\epsilon_q,\qquad
 \|j^{(q)}\|_\infty\le g_{q+1}+\epsilon_q,\quad0\le q\le3 .
 \tag{SN.26}
$$
For $q=0$ the second estimate includes the full derivative. AC's independent bounds $31/32\le j\le33/32$ remain available. The Fourier estimate uses
$\sup_{t\ge0}t^q e^{-\tau t}=b_q$; it is not a finite-frequency truncation.

For the sharp inverse-density constant, put $a=(\inf j)^{-1}$ and
$J_i\ge\|j^{(i)}\|_\infty$ for $i=1,2,3$. The four rows of a nonnegative lower-triangular matrix $D$ are
$$
 \begin{split}
 D_0&=(a,0,0,0),\\
 D_1&=(a^3J_1,a^2,0,0),\\
 D_2&=(3a^5J_1^2+a^4J_2,3a^4J_1,a^3,0),\\
 D_3&=(15a^7J_1^3+10a^6J_1J_2+a^5J_3,\
       15a^6J_1^2+4a^5J_2,\ 6a^5J_1,\ a^4).
 \end{split}\tag{SN.27}
$$
These follow by differentiating $(f/j)\circ\mathcal H^{-1}$ three times. The actual measure is $dx=j\,d\phi$. Consequently, for
$W=\operatorname{diag}(1,\sqrt3,\sqrt3,1)$, any certified matrix bound gives
$$
 \|U_{\mathcal H^{-1}}f\|_{H^3}
 \le K_H\|f\|_{H^3},\qquad
 K_H=\sqrt{\sup j}\,\|WDW^{-1}\|_{2\to2}.
 \tag{SN.28}
$$
For example the Frobenius norm is a complete upper bound; a certified tighter norm may replace it. The same true $j$ is used in all factors.

The new run can validate the signed functions
$$
 q_\sigma^G=V_\sigma+
       \frac{\sigma\chi_\perp}{\sqrt{r_*}}
       -\frac{\sigma\mu}{2}(1-G'),\qquad
 E_j=(\epsilon_0^2+3\epsilon_1^2+3\epsilon_2^2+\epsilon_3^2)^{1/2}.
 \tag{SN.29}
$$
Their terminal means vanish. SN.21--22 imply
$$
 C=\|c-\mu\|_{H^3}
 \le K_H\{\|q_-^G\|_{H^3}+\|q_+^G\|_{H^3}
                                       +|\mu|E_j\}.
 \tag{SN.30}
$$
The finite composition $G'$ is evaluated as an exact known analytic function, with its full Fourier tail if approximated. It is a new density-coefficient target; the accepted terminal return polynomial is not regenerated. The two complete signed-reference norms and $E_j$ are kept as separate small conclusions, so a later improvement of the true-angle error need not reconstruct the source or its reference.

## SN8. Execution and scope

The new public computation evaluates only the new nonmean source, complete validation residual, four-state energy and terminal coefficient. Roots,3146 scalar integrals,169 scalar germs, original rays, circle iterations, repairs and successful Green products remain unchanged inputs.

The audit separately verifies candidate and scalar coverage, root-piece identity, both signs, full193 direction labels, all means, every parameter and positive inverse-radius gate, true-angle convention and ordinary radial measure. Structural completeness alone does not imply a small coefficient.

A successful conclusion bounds the complete $C=\|c-\mu\|_{H^3}$ on the selected explicit background. The strong return remainder, direct exponential remainder, incoming graph, finite border, high inverse on that same background and nonlinear global surface remain separate obligations. Neither $C$ nor the scalar $\mu$ certifies those maps.
