# R133 supplement: the whole old root product, constant-free leading derivatives and separated first-amplitude bounds

2026-11-14, phase_inverse.

**Proved analytic refinement of the inner-root contract.** All bounds below
refer to the actual repaired explicit family, including its full
193-component direction and complex parameter disk. They consume the
already proved root germ and the closed leading formula. They do not
identify a canonical-only bound with a bound on a larger old product.

This also separates the two true forcing components in the first
analytic amplitude. The cancellation of the two characteristic branches
is kept before an absolute bound. No original mean, old primitive,
interface source or unknown part of the full return is removed.

## 1. An old product already covered by the closed formulas

Use the original root domain, sign and field definitions in
[the actual moving principal fold](R133-supplement-actual-moving-analytic-principal-fold.md),
(F.6a)--(F.15), and
[the closed leading theorem](R133-supplement-closed-leading-Airy-amplitudes-and-exact-seam-transmission.md),
(L.13)--(L.17). Set

$$
 R_g=9/10^6,\qquad \sigma_g=3/256,\qquad
 {\cal P}_g=\{|\rho|\le R_g,\ |\operatorname{Im}\phi|\le\sigma_g\},
 \quad \rho=r_*-r.                                      \tag{G.1}
$$

The original coefficients were bounded on the larger angular strip
$1/64$ and on the full original complex radial germ of radius $10^{-5}$.
The checked inequality $3M_0<1/64-3/256$ covers the two characteristic
flows and the common drift flow on all of (G.1).
Therefore the bounds for $A,X_\phi,T,T_\phi,k,\eta$ in (F.7)--(F.15)
hold on this entire old product, before any canonical inverse is used.

In the same way, the mean in
$$
 E_G=\exp[-2\int_{r_*}^r b\langle u^2+Kv^2\rangle\,dr]
$$
is the old-angle mean at fixed complex $r$. Its modulus is bounded
by the original complete Fourier norms on the native strip; an
additional angular widening is unnecessary for this scalar mean.
Thus the scalar bounds $G_+,G_{\rm inv,+},A_0^+,B_2^+$ derived in
(L.13)--(L.17) are also valid on (G.1). They were derived there by
the closed formulas and then restricted to the canonical rectangle.
This assertion uses that derivation, not a reverse implication from
a smaller canonical supremum.

Write $M=A_0^+$, $B_2=B_2^+$ and use the actual $A_+,T_+$.
The complete old-product bounds are

$$
 |a_0|\le M,\qquad |b_0|\le B_2T_+^2,\qquad
 W_g:=M+B_2T_+^2.                                    \tag{G.2}
$$

The root identities hold for every fixed complex $\phi$ and every
complex $|\delta|\le10^{-8}$:

$$
 X(0,\phi)=\phi,\quad A(0,\phi)=\eta_*\sqrt{k_*},
 \quad G(0,\phi)=1,\quad a_0(0,\phi)=1,\quad b_0=O(\rho^2).
                                                               \tag{G.3}
$$

All fractional powers use the original nonzero branches continued
from the positive real root data. In particular the cancellation in
$G(0,\phi)$ is exact on this parameter disk.

These facts are numerical inputs only when their original actual
receipts, hashes, domains and gates are verified. They do not claim
that the piecewise background is holomorphic across a physical seam.

## 2. Remove the exact leading constant before radial Cauchy

For a fixed complex $\phi$ in (G.1), put
$a_0(\rho,\phi)=1+\sum_{k\ge1}a_k(\phi)\rho^k$.
The holomorphic function $M-a_0$ has nonnegative real part on
$|\rho|\le R_g$ and value $M-1$ at zero. Its positive harmonic
real part has mean $M-1$ on every smaller circle. Taking its
nonzero Fourier coefficients gives

$$
             |a_k(\phi)|\le2(M-1)R_g^{-k},
                    \qquad k\ge1.                    \tag{G.4}
$$

Indeed the nonzero holomorphic coefficient is twice the corresponding
coefficient of the real part, whose modulus is bounded by its
nonnegative mean. Letting the circle radius increase to $R_g$
proves (G.4). This argument applies uniformly at every allowed
complex $\phi$; it is not a derivative of an interval enclosure.

For $0\le r_0<R_g$, $x=r_0/R_g$, define

$$
 A_{\mathrm{osc}}(r_0)=2(M-1){x\over1-x},\qquad
 A_p(r_0)={2(M-1)p!\over R_g^p(1-x)^{p+1}}\quad(p\ge1).
                                                               \tag{G.5}
$$

Then $|a_0-1|\le A_{\mathrm{osc}}$ and
$|\partial_\rho^p a_0|\le A_p$. At a smaller old angular strip
$\sigma_0<\sigma_g$, let $\Delta_\phi=\sigma_g-\sigma_0$.
For the required mixed derivatives,

$$
 \begin{split}
 W^a_{00}&=\min(M,1+A_{\mathrm{osc}}),\\
 W^a_{0q}&=q!A_{\mathrm{osc}}\Delta_\phi^{-q}\quad(q\ge1),\\
 W^a_{pq}&=q!A_p\Delta_\phi^{-q}\quad(p\ge1).
 \end{split}                                          \tag{G.6}
$$

The constant $1$ has no radial or angular derivative.
It must not be charged again in the last two lines. Equations
(G.4)--(G.6) require $M\ge1$; this is a direct numerical gate
and also follows from the exact root value.

## 3. Retain the true quadratic zero of the second component

Since $T=-\rho A^{2/3}$, the same old product gives the analytic quotient

$$
 b_0=\rho^2B(\rho,\phi),\qquad
       |B|\le B_\rho:=B_2A_+^{4/3}.                  \tag{G.7}
$$

At $|\rho|\le r_0$, $\Delta_r=R_g-r_0>0$ and the angular strip
of (G.6), for $0\le p\le2$ and every required $q$,

$$
 W^b_{pq}
 =B_\rho q!\Delta_\phi^{-q}
   \sum_{i=0}^{\min(p,2)}
      {p\choose i}{2!\over(2-i)!}
      r_0^{\,2-i}(p-i)!\Delta_r^{-(p-i)}.
                                                               \tag{G.8}
$$

This is the full product rule for $\rho^2B$ and ordinary
Banach-valued Cauchy applied to $B$. The $p=2$ bound contains
the finite term $2B_\rho$. No division by a root error ball
or replacement by an artificial $\rho^{-1}$ bound occurs.

The sign change between $\partial_r$ and $\partial_\rho$ does
not change these absolute derivative bounds.

## 4. The actual forcing rectangle and inverse-image gates

Use a forcing rectangle
$$
        |T|\le R_T,\qquad |\operatorname{Im}X|\le\Sigma_F
                                                               \tag{G.9}
$$
inside the original canonical rectangle
$R_T\le81/4000000$, $\Sigma_F\le1/128$.
By the original genuine inverse and $T=-\rho A^{2/3}$ its
old inverse image obeys

$$
 |\rho|\le r_F:=R_TA_-^{-2/3},\qquad
 |\operatorname{Im}\phi|\le\sigma_F:=\Sigma_F+M_0 .
                                                               \tag{G.10}
$$

The new consumer must check $r_F<R_g$ and $\sigma_F<\sigma_g$.
It then uses (G.6)--(G.8) at these exact outward bounds. This
establishes the full old-product derivative domain used by the
forcing; the canonical image alone is insufficient.

The exact local degree-zero forcing is the same as in
[the two-region derivative contract](R133-supplement-third-jet-exterior-and-holomorphic-root-budget-for-first-Airy-residual.md),
(D.1)--(D.2). Let

$$
 {\cal D}_0(w)=
 (D^2+\eta^2K\partial_\phi^2-T_0D+V_0)w,\qquad
 D=\partial_r-d\partial_\phi .
$$

Write $W^a,W^b$ for the separate component derivative tables.
If $d_0,d_1,d_r,\eta_+,K_+,T_0^+,V_0^+$ are complete
complex coefficient bounds on the actual inverse image, put

$$
 L(W)=W_{20}+2d_0W_{11}
 +(d_0^2+\eta_+^2K_+)W_{02}
 +(d_r+d_0d_1)W_{01}
 +T_0^+(W_{10}+d_0W_{01})+V_0^+W_{00}.
                                                               \tag{G.11}
$$

Keep the noncommuting matrix order. Let $\mathsf B$ and
$\mathsf D$ be entrywise absolute bounds for $H^{-1}$ and $H_D$
on that same image. They can be obtained directly from the actual
fold by

$$
 \mathsf B={1\over g_*}
   \begin{pmatrix}1+j&T_+B_T\\B_T&1+j\end{pmatrix},\qquad
 \mathsf D=
   \begin{pmatrix}
    D_X&D_TT_+\\D_T&D_X
   \end{pmatrix},
$$
$$
 D_X=\tfrac23a_+R_g^2B_\phi,\qquad
 D_T=a_+A_-^{-1/3}(1+j),\qquad g_*=1-\varepsilon_D>0 .
                                                               \tag{G.12}
$$

With the actual $\mu_->0$ and full $\vartheta_+$, a sufficient
two-component forcing bound is

$$
 \begin{pmatrix}F_b^g\\F_a^g\end{pmatrix}
 \le\mu_-^{-1}\left[
   \begin{pmatrix}L(W^a)\\L(W^b)\end{pmatrix}
   +\vartheta_+\mathsf B\mathsf D
                     \begin{pmatrix}W^a_{00}\\W^b_{00}\end{pmatrix}
              \right].
                                                               \tag{G.13}
$$

The scalar coefficient bounds and their needed radial derivatives
must come from the original complex germ, exact finite coefficient
formulas, or Cauchy with a recorded positive radial margin. Real-only
larger-window derivative arrays are not substituted for complex
derivatives. In particular all original $\eta_r/\eta$, old means
and the full $r_Q$ contribution in $\vartheta$ remain.

## 5. Separated forced amplitudes on the genuine complex root

The basic root construction is (D.19) of the two-region contract.
Set $\tau=\sqrt T$ and
$v_\pm=a_1\pm\tau b_1$, $v_{\pm,0}=a_0\pm\tau b_0$.
Both $v_{\pm,0}$ and their inverses are bounded on (G.9):

$$
 |v_{\pm,0}|\le B_0,\qquad
 |v_{\pm,0}^{-1}|\le B_0^{-},\qquad |b_0/T^2|\le B_2 .
                                                               \tag{G.14}
$$

For example use $B_0=M+R_T^{5/2}B_2$ and the previously paid
complete branch inverse. Choose $\Sigma_V,\Delta_X>0$ with

$$
  \Sigma_V+\tfrac23R_T^{3/2}+\Delta_X\le\Sigma_F .
                                                               \tag{G.15}
$$

The exact characteristic formula, with the signs fixed by
$(\partial_\tau\pm2i\epsilon\tau^2\partial_X)$, is

$$
 v_\pm(\tau,X)=v_{\pm,0}(\tau,X)
  \int_0^\tau
  {sF_a(s^2,X_\pm(s))\pm F_b(s^2,X_\pm(s))
                      \over v_{\pm,0}(s,X_\pm(s))}\,ds ,
$$
$$
 X_\pm(s)=X\mp\tfrac23i\epsilon(\tau^3-s^3).
                                                               \tag{G.16}
$$

The leading factor solves the same homogeneous characteristic
equation. Its complete division cancels the scalar reaction,
including the original $l,m$ coefficients.

For $s=t\tau$, $0\le t\le1$, the separation of the two paths is
$\frac43|\tau|^3(1-t^3)$. In addition,

$$
 |v_{+,0}(\tau,X)-v_{-,0}(\tau,X)|
                         \le2B_2|\tau|^5,
$$
$$
 |v_{+,0}^{-1}(s,X)-v_{-,0}^{-1}(s,X)|
                   \le2B_2(B_0^-)^2|s|^5 .           \tag{G.17}
$$

Cauchy in the remaining angular margin gives
$\|\partial_X(F/v_{\pm,0})\|\le B_0^- F^g/\Delta_X$.
The same product, rather than independently differentiated
quotients, is used here.

For the $F_b$ contribution to $a_1=(v_++v_-)/2$, retain the
opposite signs in (G.16) before bounding. Its three terms are
the difference of the outer leading factors, the difference of
the inner branch inverses, and the angular path separation.
The exact integrals give respectively

$$
 B_2B_0^-R_T^3F_b^g,\qquad
 {B_0B_2(B_0^-)^2\over6}R_T^3F_b^g,\qquad
 {B_0B_0^-\over2\Delta_X}R_T^2F_b^g .
$$

For the $F_a$ contribution to
$b_1=(v_+-v_-)/(2\tau)$, the same three differences give

$$
 {B_2B_0^-\over2}R_T^3F_a^g,\qquad
 {B_0B_2(B_0^-)^2\over7}R_T^3F_a^g,\qquad
 {B_0B_0^-\over5\Delta_X}R_T^2F_a^g .
$$

The same-sign terms require no branch cancellation. Consequently
the following complete separated bounds hold:

$$
 \begin{split}
 |a_1|\le A_1^g:={}&{B_0B_0^-R_T\over2}F_a^g\\
 &+\left[
 {B_0B_0^-\over2\Delta_X}R_T^2+
 B_2B_0^-\left(1+{B_0B_0^-\over6}\right)R_T^3
 \right]F_b^g ,
 \end{split}                                          \tag{G.18}
$$

$$
 \begin{split}
 |b_1|\le B_1^g:={}&B_0B_0^-F_b^g\\
 &+\left[
 {B_0B_0^-\over5\Delta_X}R_T^2+
 B_2B_0^-\left({1\over2}+{B_0B_0^-\over7}\right)R_T^3
 \right]F_a^g .
 \end{split}                                          \tag{G.19}
$$

These hold on $|T|<R_T$, $|\operatorname{Im}X|\le\Sigma_V$,
for both signs of the physical input frequency. Uniqueness and
$v_+(-\tau)=v_-(\tau)$ remove the apparent singularity at zero.
The estimates in (G.19) also follow by taking the holomorphic
limit at $\tau=0$; no bound proportional to $1/\sqrt{|T|}$
is used.

The factors $1/6,1/7,1/2,1/5$ above are the exact integrals of
$t^5,t^6,1-t^3,t(1-t^3)$ together with the displayed half and
characteristic coefficients. They are not fitted numerical gains.

## 6. Inner derivative and original-piece identification

Choose $R_i<R_T$, $\Sigma_i<\Sigma_V$. Ordinary Cauchy now applies
separately to $a_1,b_1$ with constants $A_1^g,B_1^g$ and the
positive gaps $R_T-R_i$, $\Sigma_V-\Sigma_i$.
Composing with the actual old fold retains all first and second
chain-rule terms, exactly as in (D.22)--(D.24).

The entire real set on which this estimate is used must satisfy
$|\rho|A_+^{2/3}<R_i$ and
$|\operatorname{Im}\phi|+M_0<\Sigma_i$.
It must remain inside the true original root piece, with the
true root uncertainty retained. The outer real-piece construction
and this inner analytic construction solve the same initial-value
problem with the same zero common root trace. On their overlap,
uniqueness identifies the actual amplitudes and derivatives.
No artificial interface source is introduced.

An optional future enlargement may use the explicitly continued
single root-piece cubics as auxiliary holomorphic coefficients.
That would be a new auxiliary complex-domain calculation: all
intrinsic denominators, all 65 repaired base and 193 direction
components, the fold and forcing margins must be proved there.
Only the restriction inside the original physical root piece is
identified with the actual piecewise background. This paragraph
grants no such larger numerical domain.

The present lemma grants a sharper finite inner recipe. A public
consumer must execute its actual domain and coefficient gates.
It does not itself pay the full local $\mathcal L_0w_1$ source,
the old inverse remainder on $w_1$, all propagated seams, the
finite head or the final strong-return inverse.
