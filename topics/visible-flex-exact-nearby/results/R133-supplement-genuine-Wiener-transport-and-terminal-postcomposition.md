# R133 supplement: genuine Wiener transport and terminal postcomposition

2026-11-14, visible-exact-astra-0df / phase_inverse.

This gives a complete way to consume the saved full-frequency phase
transport in **Wiener norms**, without converting a supremum estimate
into a Fourier estimate. It also gives a terminal postcomposition method
that changes the proposed conjugating lift without repeating any of the
169 scalar germs or their finite transported-phase recurrence.

The direct moving principal return, the continuous repaired centre,
the original eta value, and the compact nu remain exactly those of the
root contract. A prefix never proves a whole-return assertion. A small
conjugacy defect still does not prove an exact conjugacy, parameter KAM,
or the existence of a PDE solution branch.

## 1. Norms and a composition lemma

For a periodic function with period pi/2 put

$$
 f(x)=\sum_{j\in\mathbb Z} f_j e^{4ijx},\qquad
 \|f\|_s=\sum_j |f_j|e^{4|j|s}.
 \tag{W.1}
$$

This is a Banach algebra. If $b$ is real and $u$ is periodic, then

$$
 \|f(x+b+u(x))\|_s\le\|f\|_{s+\|u\|_s}.
 \tag{W.2}
$$

Indeed the real translation multiplies each Fourier coefficient by a
number of modulus one, and the power series for $e^{4iju}$ has norm at
most $e^{4|j|\|u\|_s}$. Absolute convergence proves the identity and the
inequality, including infinite Fourier series.

Consequently, for a real scalar speed $c(r)$ and a real periodic drift
$d(r,x)$, every forward or reversed flow of $c+d$ has the form
$x+b(r)+u(r,x)$ with $b(r)$ real and

$$
 \|u(r)\|_s\le\int\|d(t)\|_{s_*}\,dt
 \tag{W.3}
$$

as long as $s$ plus the right side is strictly below $s_*$. To justify
this on a closed subinterval, use (W.2) in the integral equation and a
strict bootstrap; local existence follows by Picard iteration on any
slightly smaller strip. The strict margin continues the flow to the
whole interval. Concatenating paths adds their drift integrals. Thus
(W.3) applies to the actual compositions, not just to each separately
evaluated flow. The real speed can be arbitrarily large without causing
any Wiener norm growth. Differentiating the integral equation similarly
gives an inverse-flow derivative bound $\exp\int\|d_x\|_{s_*}$ whenever
the composed paths lie in this outer strip.

## 2. Exact inputs and widening the saved finite residual

The original producer remains
`fourfold_codazzi_phase_full_transport_Taylor.py`, SHA256
`3254a9225f4933ae11ffbfa1862a50ed1c7c585f03aa11e56606ad758ccc6961`.
It defines a continuous, piecewise radial polynomial reference
$\widehat A_\pm=x+\widehat W_\pm$, of angular degree 64. Its initial
value is exactly the finite dyadic $H$, and every radial value jump is
exactly zero. The complete finite residual has degree at most 128.
The true/model drift difference has degree at most 64; the true/model
speed difference is a scalar. Neither statement removes the intrinsic
scalar remainders.

Use the four physical widths

$$
 b=1/32,\quad s_*=1/16,\quad s_R=1/24,\quad s_I=1/50.
 \tag{W.4}
$$

Write $R_t,R_o$ for the saved integrated residual sums, over **both**
legs, with respectively $|j|\le64$ and $64<|j|\le128$. For each
actual row, multiply its saved uniform complete drift and scalar-speed
errors by its exact radial length and add them, obtaining $D,C$.
The original producer proves these in $A_b$; all four quantities are
consumed from the actual SHA-bound native rows.

The previously completed two-ray analytic native, SHA256
`91f1a3e5900300cd6e66060063e0c9fe5b826e238f68cf9e49f356f0c4ff4071`,
provides genuine Fourier sums, even where its earlier application only
needed supremum bounds. On $A_{s_*}$ it gives

$$
 B:=\int_0^{r_*}\|d\|_{s_*}
 <.010507004681650,\qquad
 L:=\int_0^{r_*}\|d_x\|_{s_*}
 <.049312859543357.
 \tag{W.5}
$$

For any trigonometric polynomial of degree $J$,
$\|f\|_t\le e^{4J(t-b)}\|f\|_b$ when $t\ge b$. Hence the finite
model $d_0$ has complete integrated bounds

$$
 B_0=B+e^{256(s_*-b)}D,\qquad
 L_0=L+256e^{256(s_*-b)}D.
 \tag{W.6}
$$

These are upper bounds; using the whole negative-domain $B,L$ also
bounds every actual prefix.

### 2.1 A projected equation used only to bound the finite reference

Put $\widehat a=1+\partial_x\widehat W$. Its exact projected identity is

$$
 \partial_r\widehat a+
 P_{64}\big((d_0+c_0)\partial_x\widehat a+
                         (\partial_xd_0)\widehat a\big)
 =P_{64}\partial_x R_{\rm finite}.
 \tag{W.7}
$$

Here $P_{64}$ is an $\ell^1$ contraction. This identity controls only
the explicitly defined finite reference. All the modes discarded by
$P_{64}$ remain in the genuine residual below.

In the Fourier coefficient equations the real scalar $c_0$ contributes
only imaginary diagonal coefficients and therefore no derivative of
the weighted absolute-value norm. Let the analytic width decrease at
speed $\|d_0\|_{s_*}$. This pays the $d_0\partial_x\widehat a$ term
coefficient by coefficient. The other product costs
$\|\partial_xd_0\|_{s_*}\|\widehat a\|$. The projected source has
integral at most $256e^{256(s_*-b)}R_t$. Across interfaces the exact
reference value and its angular derivative are continuous. Gronwall
therefore gives, simultaneously for both signs and every radial point,

$$
 \|\widehat a\|_{s_*-B_0}\le
 M_a:=\big(\|H'\|_{s_*}+256e^{256(s_*-b)}R_t\big)e^{L_0}.
 \tag{W.8}
$$

Thus, once the explicit gate $s_*-B_0>s_R$ passes, the whole true
transport residual on the wider strip satisfies

$$
 \mathcal R\le
 e^{256(s_R-b)}R_t+e^{512(s_R-b)}R_o
 +2M_a\big(e^{256(s_R-b)}D+C\big).
 \tag{W.9}
$$

The last term keeps the complete even scalar mean and both signs.
The first two terms keep all 257 possible Fourier output coefficients.
No differentiation of a scalar uniform remainder, angular sampling,
or recomputation of a reference polynomial enters (W.9).

## 3. Genuine Wiener error transfer and the root sliver

Let $X_\pm,S_\pm,A_\pm,P$ be the true direct moving rays, inverse rays,
transported $H$, and ordered return of the original root contract.
The error $A_\pm-\widehat A_\pm$ satisfies a transport equation with
the complete residual as its source. To evaluate at the true root,
first follow the plus ray from the waist, then the common drift
backwards to $r_b$, and then, for each source point, the corresponding
principal ray backwards from $r_b$. The common-sliver segment and the
last principal segment occupy disjoint radial intervals. Therefore
their combined drift budget is at most $B$, in addition to the first
plus-ray budget $B$. The complete source/terminal pullbacks consequently
require only

$$
 s_I+2B<s_R;\qquad
 s_R-s_I-2B>.00065265730336.
 \tag{W.10}
$$

The exact common-drift identity
$D_r+dD_x=c((A_-)_x+(A_+)_x)$ pays the uncomputed root sliver. For its
inverse-label derivative compositions we use the conservative separate
three-leg gate

$$
 s_I+3B<s_*;\qquad s_*-s_I-3B>.01097898595505.
 \tag{W.11}
$$

Let $C_*$ denote the original root native's complete one-ray optical
sliver integral, which is less than $2.322547\,10^{-14}$. By (W.2),
(W.3), and the inverse derivative bound the genuine Wiener root fee is

$$
 \mathcal S=2\|H'\|_{s_*}e^L C_*
 <4.985045313942\,10^{-14}.
 \tag{W.12}
$$

This is a new Wiener estimate; the earlier supremum root fee is not
silently relabeled. For any real constant $\Omega$, the complete169
transport now implies

$$
 \boxed{\|H\circ P-H-\Omega\|_{s_I}\le
 \|\widehat W_-(r_b)-\widehat W_+(r_b)-\Omega\|_{s_R}
 +\mathcal R+\mathcal S.}
 \tag{W.13}
$$

Every norm in (W.13) is a Wiener norm. If $m$ is the exact terminal
mean difference and $T_0$ is the norm of its remaining modes, one may
replace the first term by $T_0$ when estimating the derivative, since
$m-\Omega$ is a constant. In particular

$$
 \|(H\circ P-H-\Omega)'\|_0
 \le\frac{T_0+\mathcal R+\mathcal S}{e s_I}.
 \tag{W.14}
$$

This uses $\sup_{t\ge0}te^{-s_It}=1/(es_I)$, directly on the Fourier
sum, and incurs only one derivative loss.

## 4. Changing the proposal at the terminal point only

Let $K(z)=z+k(z)$ be any real finite trigonometric lift, and set
$H_{\rm new}=K\circ H$ and
$\widehat A_{\rm new,\pm}=K\circ\widehat A_\pm$. These are exact
definitions. The new reference is generally not a finite Fourier
polynomial, and no such assertion is required. The exact chain rule gives

$$
 R_{\rm new,\pm}=K'(\widehat A_\pm)R_\pm.
 \tag{W.15}
$$

Both the initial error and all interface jumps remain zero. Since
$\langle\widehat a\rangle=1$ exactly, (W.8) implies
$\|\widehat W_\pm-\langle\widehat W_\pm\rangle\|_{s_R}
\le(M_a-1)/4$. The mean is real. Thus

$$
 M_K=1+\|k'\|_{s_R+(M_a-1)/4},\qquad
 M_{K,*}=1+\|k'\|_{s_*+\|h\|_{s_*}}
 \tag{W.16}
$$

bound the complete reference multiplier and the genuine root multiplier
respectively. For the latter, the path bound (W.11) puts the inverse
label in $A_{s_*}$ before composing with $H$. Consequently

$$
 \boxed{\|H_{\rm new}\circ P-H_{\rm new}-\Omega\|_{s_I}
 \le \|K(\widehat A_-)-K(\widehat A_+)-\Omega\|_{s_R}
       +M_K\mathcal R+M_{K,*}\mathcal S.}
 \tag{W.17}
$$

This formula pays all frequencies of the new reference through the
analytic chain rule. It does not reuse the old residual for free.

### 4.1 Full Laurent exponential terminal enclosure

Write $\widehat A_\pm=x+m_\pm+w_\pm$ with real $m_\pm$ and zero-mean
finite $w_\pm$. For every positive or negative integer $j$,

$$
 e^{4ij\widehat A_\pm}
 =e^{4ijm_\pm}e^{4ijx}
    \sum_{n=0}^{p}\frac{(4ijw_\pm)^n}{n!}
       +\mathcal E_{j,\pm}.
 \tag{W.18}
$$

All powers are full Laurent products. With $z=4|j|\|w_\pm\|_{s_R}$,
the entire omitted exponential tail is bounded by

$$
 \|\mathcal E_{j,\pm}\|_{s_R}
 \le e^{4|j|s_R}e^z\frac{z^{p+1}}{(p+1)!}.
 \tag{W.19}
$$

The real mean factor has modulus one. Multiplying (W.18) by every exact
coefficient of $k$ and adding both signs gives a finite Laurent
polynomial of maximum degree $64p+\deg k$, plus the sum of **all**
weighted tails (W.19). Its coefficients are evaluated by directed Arb
arithmetic, including the transcendental real-mean phase factors.
Subtracting the requested $\Omega$ from the central coefficient before
taking the norm retains the constant mode. The infinite tail bound also
pays its possible constant coefficient. A sampled least-squares solve
may propose the exact dyadic coefficients of $k$; none of its sampled
residuals are part of this certification.

### 4.2 Inverse lift and normalized KAM input

For any outer width $a$, (W.2) gives the explicit bounds

$$
 \|H_{\rm new}-{\rm id}\|_a\le
 U_a:=\|h\|_a+\|k\|_{a+\|h\|_a},
 \qquad
 \|H_{\rm new}'-1\|_a\le
 V_a:=\|h'\|_a+(1+\|h'\|_a)\|k'\|_{a+\|h\|_a}.
 \tag{W.20}
$$

If $V_a<1$ and $s+U_a<a$, the equation
$v=- (H_{\rm new}-{\rm id})({\rm id}+v)$ is a contraction in the
closed radius-$U_a$ ball of $A_s$. It supplies the true inverse lift
$H_{\rm new}^{-1}={\rm id}+v$, with $\|v\|_s\le U_a$ and
$\|(H_{\rm new}^{-1})'\|_s\le(1-V_a)^{-1}$.
Taking $a=1/50$ and checking $s=1/64$ explicitly therefore converts
(W.17) to an $A_{1/64}$ bound for
$H_{\rm new}PH_{\rm new}^{-1}-{\rm id}-\Omega$.
Under $x=4\phi$, the normalized circle strip is $1/16$ and its defect
bound is four times the physical one.

For the separately proved bounded-seven target, the complete fourth
root of unity gap gives an inverse multiplier at most $36|j|$.
Directly in the physical Wiener norm its loss is

$$
 \sup_{j\ne0}36|j|e^{-4|j|\delta}\le\frac9{e\delta}.
 \tag{W.21}
$$

There is no extra derivative from a supremum-to-Fourier conversion.
The circle-only multiplier against 1 also has the sharper bound
$9|j|/4$, by the ordinary bounded-seven irrationality estimate.
Neither bound alone proves any KAM smallness inequality or the true
parameter Schur complement.

## 5. Consumer and scope of actual executions

The source
`scripts/fourfold_codazzi_phase_Wiener_transport_lift.py` consumes the
SHA-bound full residual rows and the complete analytic/root natives.
It checks the two composition margins and the projected-reference
strip gate, and emits genuine whole-return error fields only if the
input has all169 germs and reaches the exact original endpoint.

The actual complete execution consumed the public Actions169-germ
terminal from run43580721166, including all3095 radial rows and the
original127 saved native checkpoints. All eight gates passed in 1.74
seconds. It proves $M_a<1.073185023901$ and
$\mathcal R<9.652387746401\,10^{-14}$, and activates (W.13) on the whole
negative interval. The complete terminal nonmean norm on $A_{1/24}$
is less than $3.242805004413\,10^{-9}$. Thus the genuine
$A_{1/50}$ defect for the new bounded-seven target is less than
$3.298859061709\,10^{-9}$ and its real angular derivative is less than
$5.965075704791\,10^{-8}$.

The native is
`notes/2026-11-14-R133-complete169-genuine-Wiener-phase-defect-native.json.gz`,
SHA256
`5886183adea04c0c51e6ac6705574f5c91554838d7b6018c4428041a033ab38a`.
The separate result
`R133-supplement-complete169-true-return-defect-and-explicit-family-twist.md`
records its provenance and the now-unconditional error gates for the
already defined explicit parameter family. The earlier123-germ
consumer check remains only a prefix check and is not used for these
whole-return values.

The formula (W.17), the Laurent remainder, and the inverse-lift gate
are independent of how $k$ is proposed. An actual improved terminal
certificate must save its exact $k$, full Laurent norm, all exponential
tails, both multiplier fees, and all source hashes. Parameter KAM still
needs its quantitative derivative bounds and Schur row. In particular,
the already certified explicit family $\overline Q+\delta Z$ must not
be identified with a genuine PDE solution branch until the complete
response error $q_\nu-Z$ and the coupled inverse costs are paid.
