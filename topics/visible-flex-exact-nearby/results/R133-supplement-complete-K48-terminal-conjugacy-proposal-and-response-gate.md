# R133 supplement: complete K48 terminal proposal and full response gate

2026-11-14, visible-exact-astra-0df / phase_inverse.

**Proved for the true direct moving return of the fixed repaired centre.**
An exact48-mode real postcomposition $K$ of the earlier $H$ removes the
complete terminal nonconstant defect to less than
$2.325725500632\,10^{-18}$ on $A_{1/24}$. All3169 Laurent coefficients,
all infinite exponential tails, the full169-germ true residual and
both $K'$ multipliers are paid. The transported reference and all scalar
germs are reused, without a new radial integration.

Writing $G=K\circ H$ and denoting the saved exact dyadic terminal
proposal by $\Omega_{\rm p}$, the actual result is

$$
 \boxed{\|G\circ P-G-\Omega_{\rm p}\|_{A_{1/50}}
 <1.463768620259\,10^{-13}.}
 \tag{K.1}
$$

Here $\Omega_{\rm p}=.431847169889226952573690371954978949\ldots$ is
an exact specified dyadic, not an asserted true rotation. Its exact
fraction is retained in the native. The ordered return's actual
translation angle lies within the displayed bound of that dyadic.
The result also pays the change in the explicit-family parameter row
and gives a quantitative error contract for replacing its proposal
$Z$ by a true full response. It does not claim an exact conjugacy or
a PDE solution branch.

## 1. The exact48-mode proposal and every terminal output

The input is the completed169-germ genuine Wiener native
`5886183adea04c0c51e6ac6705574f5c91554838d7b6018c4428041a033ab38a`.
Its terminal phases have exactly64 retained modes on each leg,
with their complete real means.

The script `fourfold_codazzi_phase_terminal_Arb_head_proposal.py`
first solves a96-by96 real Arb matrix assembled from the complete
terminal phase modes and order24 Laurent exponentials. The matrix
merely chooses48 sine and48 cosine coefficients. Each chosen
coefficient is then replaced by the exact dyadic represented by its
Arb midpoint. These numbers define

$$
 K(x)=x+\sum_{j=1}^{48}(a_j\sin4jx+b_j\cos4jx).
 \tag{K.2}
$$

The finite matrix solve is not an inverse of the infinite circle
operator. Its small head residual is not used as a full error bound.
The independent source
`fourfold_codazzi_phase_terminal_postcomposition.py` evaluates the
whole expression
$K(\widehat A_-)-K(\widehat A_+)$ by the full Laurent formula and
remainder (W.18)--(W.19) of the companion Wiener theorem.
Every product up to degree $64\cdot24+48=1584$ is retained. Both
positive and negative exponential tails for every one of the48
postcomposition modes and both transported phases are included.

The actual complete enclosure gives

$$
 \begin{aligned}
 T_{\rm nonmean}&<2.325725500632\,10^{-18},\\
 T_{\rm exponential\ tail}&<2.688849097004\,10^{-39},\\
 \|K'-1\|_{A_0}&<1.421793858340\,10^{-8}.
 \end{aligned}
 \tag{K.3}
$$

In particular $K$ is a real oriented analytic lift. The full
nonmean norm is summed over all3168 nonconstant Laurent coefficients,
with the remaining central coefficient retained for every target
comparison. No sampled residual, Fourier projection, or deleted
constant enters (K.3).

An earlier binary64 proposal with24 modes is preserved as an actual
weaker attempt. Its complete nonmean norm was
$3.883127798839\,10^{-11}$. Increasing the proposal space and using
Arb removes both that unresolved terminal part and high-mode proposal
roundoff; the certification procedure and original169-germ transport
are unchanged.

## 2. Complete residual, root and inverse-coordinate costs

For the new exact reference $K(\widehat A_\pm)$ the chain rule gives
$R_{{\rm new},\pm}=K'(\widehat A_\pm)R_\pm$.
The proved reference and root multiplier norms are

$$
 M_K<1.000001104876,\qquad M_{K,*}<1.000001986943.
$$

Thus the complete new true source and genuine Wiener root fees are

$$
 M_K\mathcal R<9.652398411090\,10^{-14},\qquad
 M_{K,*}\mathcal S<4.985055218942\,10^{-14}.
 \tag{K.4}
$$

Their sum, the actual central coefficient minus $\Omega_{\rm p}$,
and (K.3) prove (K.1). Relative to the earlier bounded-seven target,
the whole error is instead less than
$5.553045010343\,10^{-11}$; that larger number retains the actual
constant target mismatch. The angular derivative does not contain
this constant mismatch and satisfies

$$
 \|\partial_\phi(G\circ P-G-\Omega)\|_{A_0}
 <2.692451910125\,10^{-12}
 \tag{K.5}
$$

for every constant $\Omega$.

The complete composition inequalities give, on $A_{1/50}$,

$$
 \|G-{\rm id}\|<.003672400503798,\qquad
 \|G'-1\|<.017212160390558.
$$

The inverse-lift margin for physical width1/64 is greater than
$.0007025994962$, and
$\|(G^{-1})'\|_{A_{1/64}}<1.017513607411$.
The Wiener contraction argument of (W.20) therefore supplies the
actual inverse, not merely a real inverse extended by assertion.
For the normalized family

$$
 F_\delta(x)=4G\big(P_\delta(G^{-1}(x/4))\big)
 \tag{K.6}
$$

the initial KAM lift may be the identity, with $M_0=R_0=1$.
The normalized initial strip is1/16, and the error bound is four
times the corresponding physical one.

Since $G$ and the true return are real oriented degree-one lifts,
let $F=GPG^{-1}$ in physical coordinates. Pointwise (K.1) gives
$|F(x)-x-\Omega_{\rm p}|<\epsilon$. Iterating and summing this
inequality yields
$|F^n(x)-x-n\Omega_{\rm p}|<n\epsilon$.
Division by$n$ and the translation-number limit proves the stated
true rotation enclosure. This argument does not assert differentiability
of the rotation-number function or an exact conjugacy.

## 3. The actual parameter row after postcomposition

For the explicitly defined family
$Q_\delta=\overline Q+\delta Z$, $\nu_\delta=\nu_0+\delta$,
the physical average parameter row of (K.6) is exactly

$$
 \Sigma_G=\left\langle G'(P)\,\partial_\delta P\,G'\right\rangle.
 \tag{K.7}
$$

The change of variable is $x=G(\phi)$; its Jacobian $G'$ and the
other derivative $G'(P)$ are both retained. The average in (K.7)
is independent of the chosen constant target angle because the
initial KAM lift is the identity.

Put $\kappa=\|K'-1\|_{A_0}$ and $H_*=\|H'\|_{A_0}$. The actual
complete true-return parameter bound $P_1$ from the169-germ
transversality consumer gives

$$
 |\Sigma_G-\Sigma_H|
 \le(2\kappa+\kappa^2)H_*^2P_1
 <1.251717448822\,10^{-8}.
 \tag{K.8}
$$

The earlier row lower bound already paid its coordinate correction
and hence is also a conservative lower bound for $\Sigma_H$.
Subtracting (K.8) proves

$$
 \boxed{\Sigma_G>.0018683163861347376626>1/540,\qquad
       \Sigma_{G,x}>.0074732655445389506506>1/135.}
 \tag{K.9}
$$

The actual source is `fourfold_codazzi_phase_K48_parameter_row.py`.
This is the row of the explicit family, not the row of a hypothetical
PDE solution family.

## 4. A usable full-response error gate without assuming conjugacy

The full counterterm theorem (P.1), (P.17)--(P.25) has already proved
on the same continuous background

$$
 \|D_QP[e]\|_\infty
 <1.273240\|e\|_{L^2_r(E_0)},\qquad
 \|D_QP[e]\|_\infty
 <1.274436\|e\|_{L^2_rL^2_\phi}.
 \tag{K.10}
$$

These inequalities retain the entire negative body, the true root,
all angular modes and the even mean. There is no $q^{-1}$ weight.
They are statements about the return derivative and do not require
an exact circle conjugacy.

Apply (K.10) directly to (K.7). Because $G'>0$ and
$\langle G'\rangle=1$, one obtains the sharper one-factor estimate

$$
 |\Delta\Sigma_G|
 \le\|G'\|_\infty\|D_QP[e]\|_\infty,\qquad
 \|G'\|_\infty<1.015523233862.
 \tag{K.11}
$$

The measure $G'd\phi$ is used only as a positive probability measure
in this estimate; it is not assumed invariant. Thus (K.11) remains
valid before true conjugacy is proved.

The exact rational hypothesis

$$
 \boxed{\|q_\nu-Z\|_{L^2_r(E_0)}\le1/6500
 \quad\hbox{or}\quad
 \|q_\nu-Z\|_{L^2_rL^2_\phi}\le1/6500}
 \tag{K.12}
$$

would leave the true same-background full-response physical row
greater than respectively
$.0016693925703990$ or $.0016692057141239$, both strictly greater
than1/600. The normalized row would then exceed1/150.
The native explicitly records that (K.12) has not yet been supplied.
The full regular inverse defining $q_\nu$ must keep the original
mean and physical fourth-mode rows. A change to an eventual nonlinear
background is a separate error and is not hidden in (K.12).

## 5. Actual sources and native records

The48-mode proposal was generated in4.79 seconds, and the independent
complete Laurent certificate passed all six gates in5.82 seconds.
The files are:

- `scripts/fourfold_codazzi_phase_terminal_Arb_head_proposal.py`;
- `scripts/fourfold_codazzi_phase_terminal_postcomposition.py`;
- `scripts/fourfold_codazzi_phase_K48_parameter_row.py`;
- `scripts/fourfold_codazzi_phase_K48_response_error_contract.py`;
- `notes/2026-11-14-R133-complete169-Arb-head48-terminal-proposal.json.gz`;
- `notes/2026-11-14-R133-complete169-terminal-postcomposition48-p24-native.json.gz`;
- `notes/2026-11-14-R133-complete169-K48-explicit-parameter-row-native.json.gz`;
- `notes/2026-11-14-R133-K48-full-response-error-contract-native.json.gz`.

The full K48 certificate is20482 bytes, SHA256
`9f71c7b4b9e77f4df4d399365770b01c9f44503a9ecf136cd2b5c5877f98caf7`.
Its exact finite coefficients make the proposal independently
reproducible without rerunning the head solve. The preceding24-mode
attempt remains in its distinct native and is not relabeled as a
successful48-mode calculation.

The companion bounded15 arithmetic result chooses a nearby exact
quadratic target and pays its new all-frequency gap. Full R31 still
requires the uniform parameter-family bounds $P,Q,T,B$ and its actual
smallness/domain inequalities. The completed phase calculations do
not replace the full PDE inverse, the response error, the physical
operator bridge, or the strong high-frequency remainder.
