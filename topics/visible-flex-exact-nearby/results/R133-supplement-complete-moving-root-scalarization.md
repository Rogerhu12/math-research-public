# R133 supplement: complete moving root scalarization with its mean

2026-11-14, visible-exact-astra-0df / phase_inverse.

**Proved:** an exact scalarization of the complete moving Jacobi
system at a simple root, together with explicit full-frequency inverse
and commutator estimates. It retains the independent even mean, the
ordinary source, every primitive, and every projected drift. It does
not divide by the vanishing curvature. The numerical instantiation is
specified by the public consumer
`fourfold_codazzi_current_root_scalarization_budget.py`; an actual
execution record is a separate artifact, not asserted by this text.

The background is the exact continuous repair with definition SHA
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`.
The optional parameter family is the already defined explicit family
$Q_\delta=\bar Q+\delta Z$, $\nu_\delta=\nu_0+\delta$, at the single
intrinsic parameter $\eta_0$. Its direction definition is
`6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`.
It is not assumed to be the genuine nonlinear PDE branch.

## 1. Angular spaces and the complete operator

The period is $\pi/2$, the angular measure is normalized, and
$\partial=\partial_\phi$ has multiplier $4ij$. Write
$\Pi f=\langle f\rangle$, $P=1-\Pi$ and $I=\partial^{-1}P$.
For $\sigma\geq0$ use the complete spaces

$$
 \|f\|_{\mathcal A_\sigma}
   =\sum_{j\in\mathbb Z}e^{4|j|\sigma}|\widehat f_j|,
 \qquad
 \|f\|_{H^s_\sigma}^2
   =\sum_{j\in\mathbb Z}(1+16j^2)^s
          e^{8|j|\sigma}|\widehat f_j|^2.                 \tag{N.1}
$$

Thus $H^0_0$ is ordinary $L^2$. Both $P$ and $\Pi$ have norm one,
$\|I\|\leq1/4$ on every fixed space in (N.1), and
$\|M_a\|_{H^0_\sigma\to H^0_\sigma}\leq\|a\|_{\mathcal A_\sigma}$.
The last assertion follows by weighted convolution and Young's
inequality. No finite section is used.

Put $b=a_{\rm phys}'/a_{\rm phys}$, $m=\langle v\rangle$,
$\eta=-\gamma m$, $S=u^2+Kv^2$, and $d=-bIS$. Define

$$
 L_{11}=-b(1+3u^2+Kv^2),\qquad
 L_{22}=b(1-u^2-3Kv^2),\qquad \ell=-2buv.              \tag{N.2}
$$

Here $\eta$ is the characteristic coefficient, not the intrinsic
parameter $\eta_0$. The exact moving equation is (Q.4) of
[the quadratic-density result](R133-supplement-negative-quadratic-density-and-full-frequency-transport.md):

$$
\begin{split}
 D h_1={}&L_{11}h_1+K(-\eta\partial+\ell)h_2
       -2b u_\phi I(uh_1+Kvh_2)+\gamma Kzv_\phi+g_1,\\
 D h_2={}&(\eta\partial+\ell)h_1+L_{22}h_2
       -2b v_\phi I(uh_1+Kvh_2)-\gamma zu_\phi+g_2,
 \qquad D=\partial_r-d\partial,\quad z=\langle h_2\rangle.
                                                               \tag{N.3}
\end{split}
$$

The reflection class is $u,h_1$ odd and $v,h_2$ even. No assertion
that the background residual is zero enters (N.3).

## 2. Projection, independent mean, and exact elimination

Set $f=Ph_2$, so $h_2=f+z$, and define on the complete mean-zero
space

$$
 D_0=\partial_r-PM_d\partial,
 \qquad
 A=P(\eta\partial+M_\ell-2bM_{v_\phi}IM_u)P,           \tag{N.4}
$$

$$
\begin{split}
 B&=P(M_{L_{22}}-2bK M_{v_\phi}IM_v)P,\\
 E&=P(M_{L_{11}}-2b M_{u_\phi}IM_u)P,\\
 C&=P(-\eta\partial+M_\ell-2bM_{u_\phi}IM_v)P,\\
 b_2&=P(L_{22}-2bK v_\phi Iv-\gamma u_\phi),\\
 b_1&=K(\ell-2b u_\phi Iv+\gamma v_\phi).
                                                               \tag{N.5}
\end{split}
$$

$A$ maps odd states to even mean-zero states; its projection is
essential. $C$ maps even mean-zero states to odd states. On odd
states $D_0=D$. Direct projection of (N.3) gives

$$
 D_0f=Ah_1+Bf+zb_2+Pg_2,
 \qquad D_0h_1=Eh_1+KCf+zb_1+g_1.                    \tag{N.6}
$$

The missing even equation is retained independently:

$$
 \boxed{\quad
 z_r=\{b(1-\langle S\rangle)-2bKm^2\}z
       -2bm\langle uh_1+K(v-m)f\rangle+\langle g_2\rangle.
 \quad}                                                        \tag{N.7}
$$

For example, (N.7) also follows by differentiating the exact nonlinear
identity $\langle F_2(u,v)\rangle=bm(1-\langle S\rangle)$.
Consequently no transport mean has been substituted for the physical
moving mean.

Suppose $A$ is invertible on these complete mean-zero spaces, with
inverse $J$. Then (N.6) is exactly equivalent to

$$
 \boxed{\quad
 (D_0-E)J\{(D_0-B)f-zb_2-Pg_2\}-KCf-zb_1=g_1,
 \quad}                                                        \tag{N.8}
$$

coupled to (N.7), with reconstruction

$$
 h_1=J\{(D_0-B)f-zb_2-Pg_2\},\qquad h_2=f+z.        \tag{N.9}
$$

These are identities in both directions. In particular $g_2$ is
inside the flux in (N.8). For an ordinary $L^2$ radial source, (N.8)
is understood in divergence/weak form, not by assuming $\partial_rg_2$
exists in $L^2$. One concrete graph domain is $f,h_1\in
L^2_rH^1_\sigma$, $D_0f,D_0h_1\in L^2_rH^0_\sigma$,
$z\in H^1_r$, and $g\in L^2_rH^0_\sigma$. The weak version retains
the reconstructed flux (N.9). Smooth identities extend to this
domain by density.

Multiplying (N.8) by $A$ gives principal differential expression
$D_0^2+\eta^2K\partial^2$. Its coefficients are regular through the
simple root. The exact commutators and lower operators in (N.4)--(N.9)
remain; this statement does not replace the equation by that principal
expression. No division by $K$ or $\sqrt{-K}$ was made.

## 3. Full-frequency Neumann inverse

On a common complex radial domain suppose

$$
 \|\partial^t u\|_{\mathcal A_\sigma}\leq U_t,\quad
 \|\partial^t v\|_{\mathcal A_\sigma}\leq V_t,\quad
 |b|\leq b_*,\quad |\eta^{-1}|\leq e_*.
                                                               \tag{N.10}
$$

Let $L=P(M_\ell-2bM_{v_\phi}IM_u)P$ and set

$$
 L_t=2b_*\sum_{i=0}^t {t\choose i}U_iV_{t-i}
       +\frac{b_*}{2}\sum_{i=0}^t{t\choose i}V_{i+1}U_{t-i},
 \qquad c=\frac{e_*L_0}{4}.                            \tag{N.11}
$$

Then $\|\operatorname{ad}_\partial^t L\|\leq L_t$ on
$\mathcal A_\sigma$ and $H^0_\sigma$. Indeed $I$ commutes with
$\partial$, its norm is at most $1/4$, and Leibniz's rule gives both
sums in (N.11), with the displayed order of the multipliers unchanged.

If $c<1$, then

$$
 IA=\eta(1+\mathcal C),\qquad
 \mathcal C=\eta^{-1}IL,\qquad
 J=(1+\mathcal C)^{-1}\eta^{-1}I,\qquad
 \|\mathcal C\|\leq c.                                \tag{N.12}
$$

The Neumann series proves both $AJ=JA=1$ on the complete mean-zero
space. Applying $\partial$ to $IAJ=I$ is legitimate and gives $AJ=1$;
the range projection is already in $A$. Parity shows the asserted
odd/even inverse is the restriction of this full inverse. Uniformly in
the two spaces above,

$$
 \boxed{\quad
 \|J\|\leq J_0:=\frac{e_*}{4(1-c)},\qquad
 \|\partial J\|\leq J_1:=\frac{e_*}{1-c}.
 \quad}                                                        \tag{N.13}
$$

The second bound follows directly from
$\eta\partial J=1-LJ$, not from an unjustified commutation of
$\partial$ with the Neumann series. All $j\ne0$ are covered at once.

For the Hilbert scale based on $H^0_\sigma$, the adjoint inverse has
the same bounds. The adjoint of $\partial$ is $-\partial$ in this
pivot space. The adjoint of $L$ need not be a pointwise multiplier
when $\sigma>0$, but
$\|\operatorname{ad}_\partial^t(L^*)\|=
\|\operatorname{ad}_\partial^tL\|$ still holds. Thus (N.11) applies
to its derivative commutators without an assumption about that
adjoint's pointwise formula.

For explicit stronger windows define

$$
 h_0=J_0,\qquad
 h_{l+1}=e_*\left(1+
           \sum_{t=0}^l{l\choose t}L_{l-t}h_t\right),\qquad
 B_k=\left(\sum_{l=0}^{k+1}{k+1\choose l}h_l^2\right)^{1/2}.
                                                               \tag{N.14}
$$

If $U_0,\ldots,U_3,V_0,\ldots,V_4$ are supplied, this gives
$k=0,1,2,3$ and

$$
 \|J\|_{H^k_\sigma\to H^{k+1}_\sigma},\qquad
 \|J^*\|_{H^k_\sigma\to H^{k+1}_\sigma}\leq B_k,
 \qquad
 \|J\|_{H^{-k-1}_\sigma\to H^{-k}_\sigma}\leq B_k.
                                                               \tag{N.15}
$$

To prove (N.14), differentiate $\eta\partial h=g-Lh$ exactly $l$
times. Each $\|\partial^lg\|_{H^0_\sigma}$ for $l\leq k$ is at
most $\|g\|_{H^k_\sigma}$; the remaining binomial terms are
controlled by (N.11). The identity
$\|h\|_{H^{k+1}_\sigma}^2=
\sum_l{k+1\choose l}\|\partial^lh\|_{H^0_\sigma}^2$
then proves the claim. The negative bounds are duality in this fixed
pivot Hilbert scale, not a change from $\sigma$ to a different strip.
Interpolation in particular gives

| Input and output window | Bound |
|---|---:|
| $H^{-5/3}_\sigma\to H^{-2/3}_\sigma$ | $B_0^{1/3}B_1^{2/3}$ |
| $H^{-3/2}_\sigma\to H^{-1/2}_\sigma$ | $(B_0B_1)^{1/2}$ |
| $H^{-2/3}_\sigma\to H^{1/3}_\sigma$ | $B_0$ |

These constants are separate from the same-order $J_0$. They are
not replaced by $J_0$ when a strong Sobolev window is required.

## 4. Radial and drift commutators

The projections in $D_0$ must remain. Exactly,

$$
 [D_0,J]=-J[D_0,A]J,\qquad
 [D_0,A]=A_r-[PM_d\partial,A].                         \tag{N.16}
$$

This follows by differentiating both inverse identities on the
fixed mean-zero space. In particular neither $A_r$ nor the full drift
commutator is zero at a turning root.

Suppose the uniform inverse holds on the complex disk
$|r-r_*|\leq R$. The coefficients, and hence the Neumann inverse,
are operator holomorphic there. On $|r-r_*|\leq R/2$ the Cauchy
estimate gives

$$
 \|J_r\|\leq 2J_0/R,
 \qquad
 \|J_r\|_{H^s_\sigma\to H^{s+1}_\sigma}\leq2B(s)/R,
                                                               \tag{N.17}
$$

where $B(s)$ is the appropriate bound in (N.15) or its interpolation.
These are ordinary radial derivatives on one actual analytic piece.

For a direct same-space bound let

$$
 D_*={b_*\over4}(U_0^2+K_*V_0^2),\qquad
 D_{1*}=b_*(U_0^2+K_*V_0^2),\qquad K_*\geq|K|.
                                                               \tag{N.18}
$$

The formula $d=-bIS$ and $d_\phi=-bPS$ imply these two bounds.
In particular the physical coefficient named `bounds.d` in the old
physical root native is not used for $d$ here. The exact identity

$$
 I M_d\partial=PM_d-I M_{d_\phi}                       \tag{N.19}
$$

on mean-zero inputs shows that $JPM_d\partial$ extends boundedly
to each same-order space. Together with (N.13) and (N.17), it gives

$$
 \boxed{\quad
 \|[D_0,J]\|\leq {2J_0\over R}
                    +J_1(2D_*+D_{1*}/4).
 \quad}                                                        \tag{N.20}
$$

This is a same-order estimate in $\mathcal A_\sigma$ and
$H^0_\sigma$, not a claim of a further angular gain. It pays the
radial dependence needed by (N.8).

The complete lower terms can, for example, be bounded by

$$
\begin{split}
 E_*&=b_*(1+3U_0^2+K_*V_0^2)+(b_*/2)U_1U_0,\\
 B_*&=b_*(1+U_0^2+3K_*V_0^2)+(b_*K_*/2)V_1V_0,\\
 C_{0*}&=2b_*U_0V_0+(b_*/2)U_1V_0,\\
 \|b_2\|&\leq B_*+\gamma_*U_1,\qquad
 \|b_1\|\leq K_*(C_{0*}+\gamma_*V_1).
                                                               \tag{N.21}
\end{split}
$$

Here $C_{0*}$ bounds only $C+\eta\partial$, with its complete
projections. If $m_*\geq|m|$, the absolute mean-row coefficient and
its two state functionals in (N.7) are bounded respectively by

$$
 b_*(1+U_0^2+K_*V_0^2+2K_*m_*^2),\quad
 2b_*m_*U_0,\quad 2b_*m_*K_*V_0.                      \tag{N.22}
$$

In the last expression $\langle(v-m)f\rangle=\langle vf\rangle$;
using $V_0$ is therefore valid. The source mean has norm one. These
bounds retain the complete even mean rather than setting it to zero.

## 5. The actual root inputs and explicit-family transfer

The old complete moving root native has SHA
`397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864`.
Its real root enclosure is

$$
 r_*\in[1191984371497/5000000000000,
                2383968743003/10000000000000].                 \tag{N.23}
$$

It supplies the complete complex rectangle containing every disk
of radius $R=10^{-5}$ about these roots, the moving Wiener strip
$\sigma=1/1024$, the actual candidate piece 2549, and the complete
angular derivatives of physical $u$ and full-mean $v$ through four.
The native field `moving_U_derivative_Astrip` already includes the
candidate amplitude; it is not multiplied by that amplitude again.
The source is
`fourfold_codazzi_moving_turning_complex_germ.py`, SHA
`a3ad50b828c69d3e6f1e9254c1f266535171741ee2cd675d1569ef8f0fac0491`.

Those bounds belong to the original unrepaired candidate. The new
consumer adds the exact root-piece offsets from the complete repair
native, SHA
`6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc`.
It also adds the full explicit-direction fee for every complex
$|\delta|\leq10^{-8}$. This latter fee is obtained by direct complex
Horner evaluation of all 193 response coefficients on the same root
rectangle, followed by the complete exact direction-repair bounds.
The only required original response data are

| Original file | SHA-256 | Actual scope |
|---|---|---|
| `data/current_root_phase_response_20261114/response-full.json` | `ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6` | The original full response index |
| `data/current_root_phase_response_20261114/response-full-part005.npz.gz` | `ce29c19c81e77cb2f2ea9b70edc59af96a869116fa96e2e5375ffa4d61927917` | Original pieces $[2265,2718)$; consumer takes piece 2549 |

The full direction-repair native has SHA
`87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88`.
All its 193 coefficient bounds are retained, including the mean.
This use of one original shard does not claim that the other thirteen
shards were reconstructed in this execution. The negative-interval
direction bounds stop short of the root; they are not extrapolated
to the complex root disk.

If $Z_{u,t}$, $Z_{v,t}$ are the resulting complete norms and
$e_{u,t}$, $e_{v,t}$ are the exact background offset norms, set

$$
 U_t=U_t^{\rm original}+e_{u,t}+10^{-8}Z_{u,t},\quad
 V_t=V_t^{\rm original}+e_{v,t}+10^{-8}Z_{v,t}.          \tag{N.24}
$$

For the reciprocal mean, use the original strictly negative real
part, subtract the actual root mean offset in modulus and
$10^{-8}$ times the complete direction mean bound. For $\gamma$ use
its positive real-part lower bound. Their product gives a nonzero
$\eta$ and the valid $e_*$ in (N.10). No derivative of an interval
error is taken.

The compact metric bump is identically zero on the entire root
germ: its upper support endpoint is $9/50$, strictly below the left
edge of this rectangle. Consequently $K,b,\gamma$ and the intrinsic
root are exactly independent of $\nu_\delta$ there. Only the stated
centre and mean variations must be paid. The actual R31 strip native
`dfb2a174a010d399775240b2bd07a0f547dfee5fc137e12141be9fd8a46e3854`
places its selected explicit-family parameter inside $|\delta|<10^{-8}$.
This includes that parameter in the root calculation without equating
it to a true nonlinear PDE solution.

## 6. What this resolves, and what it does not

Equations (N.7)--(N.9) supply a complete regular scalar formulation at
the current moving root. Its angular inverse, source reconstruction,
Sobolev windows and radial commutator have the explicit contracts
(N.11)--(N.22). This avoids an unsupported identification with a
physical local operator at an approximate background.

The nonlocal root equation still requires its actual two-row turning
connection and quantified remainder. The complete positive high-input
graph, mean/head feedback, and a true-background transfer remain
separate obligations. This result does not turn the finite-part
strict symbol into the final return coefficient, and does not grant
an $O_{4/3}$ return remainder or a global inverse.
